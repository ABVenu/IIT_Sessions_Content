# Multimodal Pipelines (Speech and Vision Models)

## Introduction

In the **previous** session you built **Agentic RAG** — agents that **decide when and what to retrieve**, rewrite queries, call retrieval as a tool, and stop with clear conditions. That work still lives in the **text + documents** world.

This session adds **speech** and **vision**. You will build a **multimodal pipeline**: speech becomes text, text becomes a short summary, and the summary becomes speech again. You will also try a simple **vision** step (image → short description).

**What you will learn:**

- Map a **multimodal agent pipeline**: audio in → text → summary → audio out, and where image → description fits
- Run **Speech-to-Text** on a short sample audio file and check transcript quality
- **Summarize** the transcript with **one cloud provider**
- Integrate **Text-to-Speech**, run the full pipeline once, and try a **vision** step

**Lab rule:** Heavy model work runs on a **cloud API**. Your laptop only downloads small sample files and prints results. These notes use **Groq** with one key, `GROQ_API_KEY`. After the lab, you may try **summary** and **vision** with **Ollama Cloud** instead (`OLLAMA_API_KEY` only — still one key, not both at once).

---

## What Multimodal Means

Most agent labs so far used **text in** and **text out**. Real products also use voice notes and photos.

- **Official Definition:** **Multimodal** AI systems accept or produce more than one type of data, such as text, audio, or images.
- **In Simple Words:** The agent can work with more than typed words.
- **Real-Life Example:** WhatsApp lets you send text, voice notes, and photos in one chat. A multimodal pipeline does a similar mix, step by step.

![Multimodal overview showing text questions, voice notes, and campus notice photos as three input types that can produce written answers, spoken summaries, or short image descriptions](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session51/session51-01-multimodal-overview.png)

| Modality | Input example | Output example |
|---|---|---|
| Text | Typed question | Written answer |
| Audio | Voice note | Spoken summary |
| Image | Hostel notice photo | Short description |

---

## Map the Multimodal Agent Pipeline

Before coding, lock the flow on paper. Each stage has one job.

- **Official Definition:** A **pipeline** is a fixed sequence of steps where the output of one step becomes the input of the next.
- **In Simple Words:** An assembly line for data.
- **Real-Life Example:** In a bank, a form is filled → checked → approved → receipt printed. Each desk does one task.

### Speech Pipeline (Main Path)

```text
Sample audio → [1] Speech-to-Text → transcript
             → [2] Summarize → short summary
             → [3] Text-to-Speech → spoken summary (.mp3)
```

![Speech pipeline flow from campus voice note through Speech-to-Text, summarization, and Text-to-Speech to a spoken summary the student can listen to](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session51/session51-02-speech-pipeline-flow.png)

### Where Vision Fits

Vision is a **parallel input path**, not a replacement for speech.

```text
Sample image → [Vision] Image → short description (cloud vision model)
```

![Vision as a parallel input path where a campus notice photo is sent to a cloud vision model and returns a short text description alongside the main speech pipeline](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session51/session51-03-vision-parallel-path.png)

### Provider Choice (Read Once)

| What you need | This lab (shown in notes) | Other option to try later |
|---|---|---|
| Speech-to-Text | **Groq** Whisper | — |
| Summarize | **Groq** chat model | **Ollama Cloud** chat model |
| Text-to-Speech | **gTTS** (network TTS, not an LLM key) | Same |
| Vision | **Groq** vision-capable model | **Ollama Cloud** vision-capable model |
| API key for the lab | **Only** `GROQ_API_KEY` | If you switch provider: **only** `OLLAMA_API_KEY` |

**Important:** You are **not** required to run Groq and Ollama Cloud together. Pick **one** cloud LLM provider for the session.

![Cloud lab setup showing a light laptop downloading sample files while heavy speech and vision models run in the cloud with one API key and gTTS as a separate speech service](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session51/session51-04-cloud-laptop-one-key.png)

### Activity — Label the Pipeline
Write **STT**, **Summarize**, **TTS**, or **Vision** for each task: voice note → text; long transcript → 3 bullets; summary text → `.mp3`; canteen menu photo → one sentence.
**Suggested answers:** STT, Summarize, TTS, Vision.

---

## Setup — One Key and Sample Files

Install light clients only:

```bash
pip install groq python-dotenv gTTS pillow
```

These packages call remote services. They are not full speech or vision models on your laptop.

Create a `.env` file (do **not** commit it to Git):

```text
GROQ_API_KEY=your_groq_key_here
```

Create a Groq key from [console.groq.com](https://console.groq.com). Do **not** add an Ollama key for the main lab path.

**Common mistake:** Creating two keys and thinking two LLMs are required. **Better habit:** One provider, one key, three pipeline stages.

### Sample files used in this lab

| Sample | What it is | Download link |
|---|---|---|
| Sample audio | Short campus voice note for Speech-to-Text | [sample_voice_note.mp3](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session51/sample_voice_note.mp3) |
| Sample transcript text | Expected words in the voice note (for quality check) | [sample_transcript.txt](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session51/sample_transcript.txt) |
| Sample image | Simple notice image for vision | [sample_notice.jpg](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session51/sample_notice.jpg) |

**Sample transcript text:**

```text
Hello. This is a short campus update.
The library is open until ten PM.
Please carry your student ID.
```

Save downloads as `sample_voice_note.mp3`, `sample_transcript.txt`, and `sample_notice.jpg`.

### Full Code — Download Sample Files

```python
# Download course sample audio, transcript text, and image from S3
from pathlib import Path
import requests

SAMPLES = {
    "sample_voice_note.mp3": (
        "https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/"
        "iitr-as-2601/module4/session51/sample_voice_note.mp3"
    ),
    "sample_transcript.txt": (
        "https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/"
        "iitr-as-2601/module4/session51/sample_transcript.txt"
    ),
    "sample_notice.jpg": (
        "https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/"
        "iitr-as-2601/module4/session51/sample_notice.jpg"
    ),
}

for filename, url in SAMPLES.items():
    path = Path(filename)
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    path.write_bytes(response.content)
    print("Saved:", path.resolve())
```

**How the code works:** Each sample is downloaded from the course S3 link and saved with a fixed name. Later steps read these local files only. Run this block once before Speech-to-Text, summary, and vision.

---

## Speech-to-Text on the Sample Audio

Speech-to-Text turns sound into words the rest of the pipeline can use.

- **Official Definition:** **Speech-to-Text (STT)** converts spoken audio into written text (a transcript).
- **In Simple Words:** It types what was said in the voice note.
- **Real-Life Example:** YouTube auto-captions turn a video’s speech into text under the video.

### Transcript Quality Checklist

After STT, compare your model transcript with `sample_transcript.txt`.

| Check | Good sign | Problem sign |
|---|---|---|
| Completeness | Main points are present | Large missing chunks |
| Names / numbers | Times and IDs look right | Garbled numbers |
| Meaning | Same message as sample text | Different meaning |
| Noise | Clean sentences | Random extra words |

![Transcript quality checklist comparing Speech-to-Text output against expected campus update text for completeness, numbers, meaning, and noise](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session51/session51-05-transcript-quality-check.png)

**Common mistake:** Starting with a long, noisy recording.

**Better habit:** Use the short course sample audio first.

### Full Code — Speech-to-Text with Groq

```python
# Speech-to-Text using Groq Whisper (one cloud key only)
import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("Set GROQ_API_KEY in your .env file.")

client = Groq(api_key=api_key)
audio_path = Path("sample_voice_note.mp3")
if not audio_path.exists():
    raise FileNotFoundError("Run the sample-file creation code first.")

with audio_path.open("rb") as audio_file:
    result = client.audio.transcriptions.create(
        file=audio_file,
        model="whisper-large-v3",
        response_format="text",
    )

transcript = result.strip() if isinstance(result, str) else str(result).strip()
print("Model transcript:")
print(transcript)

expected = Path("sample_transcript.txt").read_text(encoding="utf-8").strip()
print("\nSample transcript text:")
print(expected)
```

**How the code works:** Groq runs **Whisper** in the cloud; your laptop only uploads the small audio file. Print both the model transcript and the sample transcript text to judge quality.

### Activity — Score Your Transcript
Note Yes/No for: Did STT capture library hours? Did STT capture student ID instruction? Close enough to use for summary?

---

## Summarize the Transcript

A transcript can be long and messy. Agents usually need a **short summary**, not every spoken word.

- **Official Definition:** **Summarization** reduces a longer text to the main points while keeping important facts.
- **In Simple Words:** Turn a long voice note into a short briefing.
- **Real-Life Example:** After a meeting, you send three bullet points instead of the full recording.

### Full Code — Summarize with Groq

```python
# Summarize transcript text using Groq chat (same GROQ_API_KEY)
import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("Set GROQ_API_KEY in your .env file.")

client = Groq(api_key=api_key)
# Prefer live STT output; fall back to sample transcript text if needed
transcript = Path("sample_transcript.txt").read_text(encoding="utf-8").strip()

prompt = (
    "Summarize the transcript in exactly 3 short bullet points. "
    "Keep only useful facts. Do not add new information.\n\n"
    f"Transcript:\n{transcript}"
)

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.2,
)

summary = response.choices[0].message.content.strip()
print("Summary:")
print(summary)
```

**How the code works:** The same `GROQ_API_KEY` powers summary after STT. The prompt blocks invented facts, and low `temperature` keeps the summary stable.

### Try the Other Provider Later (Optional)

These notes use **Groq**. If you later try **Ollama Cloud** for summary, use **only** `OLLAMA_API_KEY` in a separate script (OpenAI-compatible client at `https://ollama.com/v1`). Do not mix both keys in one confused setup. The main lab path stays on **Groq only**.

---

## Text-to-Speech Integration

Turn the summary back into audio so a user can **listen** to the result.

- **Official Definition:** **Text-to-Speech (TTS)** converts written text into spoken audio.
- **In Simple Words:** The computer reads the summary aloud.
- **Real-Life Example:** Google Maps speaks turn-by-turn directions.

TTS here uses **gTTS**. It is a network speech service. It is **not** a second LLM and needs **no** `GROQ_API_KEY`.

### Full Code — Speak the Summary with gTTS

```python
# Convert summary text into an audio file with gTTS
from gtts import gTTS
from pathlib import Path

summary = (
    "- Library open until 10 PM\n"
    "- Carry student ID\n"
    "- Short campus update"
)  # Replace with model summary from previous step

speakable = summary.replace("-", " ").replace("\n", ". ")
tts = gTTS(text=speakable, lang="en")
out_path = Path("summary_spoken.mp3")
tts.save(str(out_path))
print("Spoken summary saved to:", out_path.resolve())
```

**How the code works:** Summary text is cleaned into speakable sentences. `gTTS` requests speech from a remote service and saves `summary_spoken.mp3`. No extra LLM API key is involved.

---

## Full Speech Pipeline — One Key End to End

Connect the three stages in one script. This is the main deliverable of the session.

### Full Code — Speech-to-Text → Summary → Text-to-Speech

```python
# Full pipeline: Groq for STT + summary, gTTS for speech output
# Only one LLM key required: GROQ_API_KEY
import os
from pathlib import Path
from groq import Groq
from gtts import gTTS
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("Set GROQ_API_KEY in .env")

client = Groq(api_key=api_key)
audio_path = Path("sample_voice_note.mp3")
if not audio_path.exists():
    raise FileNotFoundError("Run the sample-file creation code first.")


def speech_to_text(path: Path) -> str:
    with path.open("rb") as audio_file:
        result = client.audio.transcriptions.create(
            file=audio_file,
            model="whisper-large-v3",
            response_format="text",
        )
    return result.strip() if isinstance(result, str) else str(result).strip()


def summarize(transcript: str) -> str:
    prompt = (
        "Summarize in exactly 3 short bullet points. "
        "Keep only useful facts. Do not invent details.\n\n"
        f"Transcript:\n{transcript}"
    )
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return response.choices[0].message.content.strip()


def text_to_speech(summary: str, out_file: Path) -> Path:
    speakable = summary.replace("-", " ").replace("\n", ". ")
    tts = gTTS(text=speakable, lang="en")
    tts.save(str(out_file))
    return out_file


transcript = speech_to_text(audio_path)
print("\n=== TRANSCRIPT ===")
print(transcript)

summary = summarize(transcript)
print("\n=== SUMMARY ===")
print(summary)

spoken_path = text_to_speech(summary, Path("summary_spoken.mp3"))
print("\n=== SPOKEN SUMMARY FILE ===")
print(spoken_path.resolve())
```

**How the code works:** Stage 1 uses Groq Whisper on `sample_voice_note.mp3`. Stage 2 uses the same Groq client to summarize. Stage 3 uses gTTS and needs no LLM key. One cloud LLM provider, one key.

### Activity — Pipeline Run Card
Mark Yes/No for each stage output: Speech-to-Text → transcript text; Summarize → 3 bullets; Text-to-Speech → `summary_spoken.mp3`. If any stage fails, fix **only that stage**, then re-run.

---

## Vision Basics — Image to Short Description

Speech is one modality. Vision is another. Here you send the sample image to a **cloud vision model** and get a short description.

- **Official Definition:** **Vision** models accept image input and return text such as a caption or description.
- **In Simple Words:** The model looks at a picture and tells you what it sees.
- **Real-Life Example:** A phone gallery search finds “beach photos” by understanding image content.

### Full Code — Describe the Sample Image with Groq

```python
# Vision basics: sample image -> short description using Groq
# Still uses only GROQ_API_KEY
import os
import base64
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("Set GROQ_API_KEY in your .env file.")

image_path = Path("sample_notice.jpg")
if not image_path.exists():
    raise FileNotFoundError("Run the sample-file creation code first.")

image_b64 = base64.b64encode(image_path.read_bytes()).decode("utf-8")
client = Groq(api_key=api_key)

response = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": (
                        "Describe this image in one or two short sentences. "
                        "Focus on useful facts only."
                    ),
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{image_b64}"},
                },
            ],
        }
    ],
    temperature=0.2,
)

description = response.choices[0].message.content
print("Image description:")
print(description)
```

**How the code works:** The sample image is encoded and sent to Groq; the model returns a short description. No second API key is required. If the vision model name changes, check the Groq console and update the `model=` string only.

### Optional: Vision with Ollama Cloud Later

Same rule as summary: try Ollama Cloud vision **instead of** Groq vision, not in addition. Use **only** `OLLAMA_API_KEY`, send the same base64 image, and pick a current vision model from the Ollama library. Main notes path remains **Groq-only**.

### Activity — Speech vs Vision Inputs

Answer briefly: What input did speech use? What input did vision use? What output type is shared by both paths? When would you use vision instead of speech?

**Suggested direction:** Speech uses audio; vision uses an image; both can produce text; use vision for posters, screenshots, and diagrams that were never spoken.

---

## Troubleshooting

| Symptom | Likely cause | What to try |
|---|---|---|
| `401` / unauthorized | Missing or wrong `GROQ_API_KEY` | Recheck `.env`; restart terminal/notebook |
| Sample file not found | Download step skipped | Run the sample download code first |
| Empty transcript | Silent or corrupt audio | Re-download `sample_voice_note.mp3` |
| Vision model error | Model name changed | Pick a current vision model in Groq console |
| Summary invents facts | Prompt too loose | Keep “do not invent details” in the prompt |

**Important rule:** If one stage fails, test STT, summary, TTS, and vision as separate functions. Do not add a second LLM key to “fix” a failed stage.

---

## Key Takeaways

- A **multimodal pipeline** chains modalities: **Speech-to-Text → summary → Text-to-Speech**, with **vision** as an image-to-text path.
- This lab uses **one cloud provider (Groq)** and **one key (`GROQ_API_KEY`)**. You do not need two LLMs for one pipeline.
- **Speech-to-Text** creates a transcript; compare it with the course **sample transcript text**.
- **Text-to-Speech** uses **gTTS** and is not a second LLM key.
- You may later try **Ollama Cloud** for summary and vision with **only** `OLLAMA_API_KEY` — still one provider at a time.

These skills help you design agents that accept voice notes and images, then return short spoken or written answers in later product work.

---

## Important Commands, Libraries, Terminologies Used

| Term / Item | Meaning in this lesson |
|---|---|
| Multimodal | More than one data type (text, audio, image) |
| Pipeline | Ordered stages; each output feeds the next step |
| Speech-to-Text (STT) | Audio → transcript text |
| Transcript | Written form of spoken audio |
| Summarization | Long text → short useful points |
| Text-to-Speech (TTS) | Text → spoken audio file |
| Vision | Image → text description |
| Groq / `GROQ_API_KEY` | Cloud provider and only LLM key for the main lab |
| Ollama Cloud / `OLLAMA_API_KEY` | Optional later provider; one key at a time |
| `groq`, `gTTS`, `python-dotenv`, `requests`, `base64` | Python clients and helpers used in the lab |
| Sample files | `sample_voice_note.mp3`, `sample_transcript.txt`, `sample_notice.jpg` |
