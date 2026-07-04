# Multimodal Pipelines (Speech and Vision Models)

## Introduction

In the **previous** session you practised **retrieval tuning** on a fixed eval set — measuring **hit rate**, classifying **retrieval vs generation** failures, and proving **before/after** improvement. That work stays in the **text + documents** world.

This session adds **speech** and **vision**. You will build a **multimodal pipeline**: speech becomes text, text becomes a short summary, and the summary becomes speech again. You will also try a simple **vision** step (image → short description).

**What you will learn:**

- Map a **multimodal agent pipeline**: audio in → text → summary → audio out, and where image → description fits
- Run **Speech-to-Text** on a short sample audio file and check transcript quality
- **Summarize** the transcript with **one cloud provider**
- Integrate **Text-to-Speech**, run the full pipeline once, and try a **vision** step

**Lab rule:** Heavy model work runs on a **cloud API**. Your laptop only downloads small sample files and prints results.

**One provider for this lab:** These notes demonstrate everything with **Groq** and a single key, `GROQ_API_KEY`. You do **not** need two LLM keys for this session. After the lab, you may try the **summary** and **vision** steps with **Ollama Cloud** instead (that path uses `OLLAMA_API_KEY` only — still one key, not both at once).

---

## What Multimodal Means

Most agent labs so far used **text in** and **text out**. Real products also use voice notes and photos.

- **Official Definition:** **Multimodal** AI systems accept or produce more than one type of data, such as text, audio, or images.
- **In Simple Words:** The agent can work with more than typed words.
- **Real-Life Example:** WhatsApp lets you send text, voice notes, and photos in one chat. A multimodal pipeline does a similar mix, step by step.

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
Sample audio file (voice note)
        |
        v
[1] Speech-to-Text (STT)  -->  transcript text
        |
        v
[2] Summarize (cloud LLM)  -->  short summary text
        |
        v
[3] Text-to-Speech (TTS)  -->  audio file (spoken summary)
```

### Where Vision Fits

Vision is a **parallel input path**, not a replacement for speech.

```text
Sample image file (photo / screenshot)
        |
        v
[Vision] Image --> short description (cloud vision model)
```

### Provider Choice (Read Once)

| What you need | This lab (shown in notes) | Other option to try later |
|---|---|---|
| Speech-to-Text | **Groq** Whisper | — |
| Summarize | **Groq** chat model | **Ollama Cloud** chat model |
| Text-to-Speech | **gTTS** (network TTS, not an LLM key) | Same |
| Vision | **Groq** vision-capable model | **Ollama Cloud** vision-capable model |
| API key for the lab | **Only** `GROQ_API_KEY` | If you switch provider: **only** `OLLAMA_API_KEY` |

**Important:** You are **not** required to run Groq and Ollama Cloud together. Pick **one** cloud LLM provider for the session.

### Activity — Label the Pipeline

For each item, write **STT**, **Summarize**, **TTS**, or **Vision**.

| Task | Stage |
|---|---|
| Turn a voice note into text | |
| Turn a long transcript into 3 bullets | |
| Turn summary text into an `.mp3` file | |
| Turn a canteen menu photo into one sentence | |

**Suggested answers:** STT, Summarize, TTS, Vision.

---

## Setup — One Key and Sample Files

### Install light Python packages only

```bash
pip install groq python-dotenv gTTS pillow
```

These packages are **clients**. They call remote services. They are not full speech or vision models on your laptop.

### Environment variable (one key only)

Create a `.env` file in your project folder (do **not** commit it to Git):

```text
GROQ_API_KEY=your_groq_key_here
```

- Create a Groq key from [console.groq.com](https://console.groq.com)
- Do **not** add an Ollama key for the main lab path in these notes

**Common mistake:** Creating two keys and thinking two LLMs are required for one pipeline.

**Better habit:** One provider, one key, three pipeline stages.

### Sample files used in this lab

Download these course sample files before you code.

| Sample | What it is | Download link |
|---|---|---|
| Sample audio | Short campus voice note for Speech-to-Text | [sample_voice_note.mp3](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session51/sample_voice_note.mp3) |
| Sample transcript text | Expected words in the voice note (for quality check) | [sample_transcript.txt](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session51/sample_transcript.txt) |
| Sample image | Simple notice image for vision | [sample_notice.jpg](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session51/sample_notice.jpg) |

**Sample transcript text (same content as the text file):**

```text
Hello. This is a short campus update.
The library is open until ten PM.
Please carry your student ID.
```

Save downloads in your project folder with these names:

- `sample_voice_note.mp3`
- `sample_transcript.txt`
- `sample_notice.jpg`

### Full Code — Download Sample Files

```python
# Download course sample audio, transcript text, and image from S3

from pathlib import Path  # Local file paths
import requests  # HTTP download


SAMPLES = {
    "sample_voice_note.mp3": (
        "https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/"
        "iitr-as-2601/module4/session51/sample_voice_note.mp3"
    ),  # Sample audio for STT
    "sample_transcript.txt": (
        "https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/"
        "iitr-as-2601/module4/session51/sample_transcript.txt"
    ),  # Sample transcript text for quality check
    "sample_notice.jpg": (
        "https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/"
        "iitr-as-2601/module4/session51/sample_notice.jpg"
    ),  # Sample image for vision
}

for filename, url in SAMPLES.items():  # Download each sample once
    path = Path(filename)  # Local target path
    response = requests.get(url, timeout=60)  # Fetch from S3
    response.raise_for_status()  # Fail clearly if link is missing
    path.write_bytes(response.content)  # Save file bytes
    print("Saved:", path.resolve())  # Confirm local path
```

**How the code works:**

- Each sample is downloaded from the course S3 link
- Files are saved next to your script with fixed names
- Later steps read these local files only

Run this block once before Speech-to-Text, summary, and vision.

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

**Common mistake:** Starting with a long, noisy recording.

**Better habit:** Use the short course sample audio first.

### Full Code — Speech-to-Text with Groq

```python
# Speech-to-Text using Groq Whisper (one cloud key only)

import os  # Read environment variables
from pathlib import Path  # File paths
from groq import Groq  # Groq cloud client
from dotenv import load_dotenv  # Load .env values


load_dotenv()  # Load GROQ_API_KEY from .env
api_key = os.getenv("GROQ_API_KEY")  # Single lab key
if not api_key:  # Stop early if key is missing
    raise ValueError("Set GROQ_API_KEY in your .env file.")  # Clear setup error

client = Groq(api_key=api_key)  # One client for this lab
audio_path = Path("sample_voice_note.mp3")  # Course sample audio
if not audio_path.exists():  # Check download step was done
    raise FileNotFoundError("Run the sample-file creation code first.")  # Setup reminder

with audio_path.open("rb") as audio_file:  # Open audio as binary
    result = client.audio.transcriptions.create(  # Cloud STT call
        file=audio_file,  # Audio bytes
        model="whisper-large-v3",  # Groq hosted speech model
        response_format="text",  # Return plain transcript text
    )

transcript = result.strip() if isinstance(result, str) else str(result).strip()  # Normalize text
print("Model transcript:")  # Label output
print(transcript)  # Show STT result

expected = Path("sample_transcript.txt").read_text(encoding="utf-8").strip()  # Load sample text
print("\nSample transcript text:")  # Label expected text
print(expected)  # Show expected words for quality check
```

**How the code works:**

- Groq runs **Whisper** in the cloud
- Your laptop only uploads the small audio file
- You print both the model transcript and the sample transcript text to judge quality

### Activity — Score Your Transcript

| Question | Your note |
|---|---|
| Did STT capture library hours? | Yes / No |
| Did STT capture student ID instruction? | Yes / No |
| Close enough to use for summary? | Yes / No |

---

## Summarize the Transcript

A transcript can be long and messy. Agents usually need a **short summary**, not every spoken word.

- **Official Definition:** **Summarization** reduces a longer text to the main points while keeping important facts.
- **In Simple Words:** Turn a long voice note into a short briefing.
- **Real-Life Example:** After a meeting, you send three bullet points instead of the full recording.

### Full Code — Summarize with Groq

```python
# Summarize transcript text using Groq chat (same GROQ_API_KEY)

import os  # Environment variables
from pathlib import Path  # File paths
from groq import Groq  # Same Groq client family
from dotenv import load_dotenv  # Load .env


load_dotenv()  # Load key
api_key = os.getenv("GROQ_API_KEY")  # Single lab key
if not api_key:  # Require key
    raise ValueError("Set GROQ_API_KEY in your .env file.")  # Setup error

client = Groq(api_key=api_key)  # Cloud client
# Prefer live STT output; fall back to sample transcript text if needed
transcript_path = Path("sample_transcript.txt")  # Course sample text
transcript = transcript_path.read_text(encoding="utf-8").strip()  # Load transcript text

prompt = (
    "Summarize the transcript in exactly 3 short bullet points. "
    "Keep only useful facts. Do not add new information.\n\n"
    f"Transcript:\n{transcript}"
)  # Clear summary instruction

response = client.chat.completions.create(  # Cloud chat call
    model="llama-3.1-8b-instant",  # Fast Groq text model (verify current name if needed)
    messages=[  # Chat messages
        {"role": "user", "content": prompt},  # Ask for summary
    ],
    temperature=0.2,  # Steady factual tone
)

summary = response.choices[0].message.content.strip()  # Extract summary text
print("Summary:")  # Label output
print(summary)  # Show bullets
```

**How the code works:**

- The same `GROQ_API_KEY` powers summary after STT
- The prompt blocks invented facts
- Low `temperature` keeps the summary stable

### Try the Other Provider Later (Optional)

These notes use **Groq**. If you want to try **Ollama Cloud** for summary only, use **only** `OLLAMA_API_KEY` in a separate experiment (do not mix both keys in one confused setup).

```python
# Optional later practice: summarize with Ollama Cloud instead of Groq
# Use this in a separate script with only OLLAMA_API_KEY set.

import os  # Environment variables
from openai import OpenAI  # OpenAI-compatible client
from dotenv import load_dotenv  # Load .env


load_dotenv()  # Load OLLAMA_API_KEY only for this experiment
api_key = os.getenv("OLLAMA_API_KEY")  # Ollama Cloud key
if not api_key:  # Require key for this optional path
    raise ValueError("Set OLLAMA_API_KEY only if you are trying Ollama Cloud.")  # Setup note

client = OpenAI(  # Ollama Cloud client
    base_url="https://ollama.com/v1",  # Ollama Cloud endpoint
    api_key=api_key,  # Single key for this experiment
)

transcript = (
    "Hello. This is a short campus update. "
    "The library is open until ten PM. "
    "Please carry your student ID."
)  # Same sample transcript text

response = client.chat.completions.create(  # Cloud summary call
    model="llama3.2",  # Confirm tag on ollama.com/library
    messages=[
        {
            "role": "user",
            "content": (
                "Summarize in exactly 3 short bullet points. "
                "Do not invent details.\n\n"
                f"Transcript:\n{transcript}"
            ),
        }
    ],
    temperature=0.2,  # Steady tone
)

print(response.choices[0].message.content)  # Show Ollama Cloud summary
```

**How the code works:**

- This is an **optional alternate provider**, not a second required key for the main lab
- Main lab path stays on **Groq only**

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

from gtts import gTTS  # Network TTS client
from pathlib import Path  # File path helper


summary = (
    "- Library open until 10 PM\n"
    "- Carry student ID\n"
    "- Short campus update"
)  # Replace with model summary from previous step

speakable = summary.replace("-", " ").replace("\n", ". ")  # Make text speakable
tts = gTTS(text=speakable, lang="en")  # Build speech request
out_path = Path("summary_spoken.mp3")  # Output spoken summary
tts.save(str(out_path))  # Write mp3 file
print("Spoken summary saved to:", out_path.resolve())  # Confirm path
```

**How the code works:**

- Summary text is cleaned into speakable sentences
- `gTTS` requests speech from a remote service
- `summary_spoken.mp3` is saved for playback
- No extra LLM API key is involved

---

## Full Speech Pipeline — One Key End to End

Connect the three stages in one script. This is the main deliverable of the session.

### Full Code — Speech-to-Text → Summary → Text-to-Speech

```python
# Full pipeline on Groq for STT + summary, gTTS for speech output
# Only one LLM key is required: GROQ_API_KEY

import os  # Environment variables
from pathlib import Path  # File paths
from groq import Groq  # Single cloud provider for this lab
from gtts import gTTS  # Network TTS
from dotenv import load_dotenv  # Load secrets


load_dotenv()  # Load .env
api_key = os.getenv("GROQ_API_KEY")  # Only LLM key for this lab
if not api_key:  # Require Groq key
    raise ValueError("Set GROQ_API_KEY in .env")  # Setup error

client = Groq(api_key=api_key)  # One client reused for STT and summary
audio_path = Path("sample_voice_note.mp3")  # Course sample audio
if not audio_path.exists():  # Ensure sample exists
    raise FileNotFoundError("Run the sample-file creation code first.")  # Setup reminder


def speech_to_text(path: Path) -> str:
    with path.open("rb") as audio_file:  # Open audio file
        result = client.audio.transcriptions.create(  # Groq Whisper STT
            file=audio_file,  # Audio input
            model="whisper-large-v3",  # Hosted speech model
            response_format="text",  # Plain text transcript
        )
    return result.strip() if isinstance(result, str) else str(result).strip()  # Clean text


def summarize(transcript: str) -> str:
    prompt = (  # Strict summary prompt
        "Summarize in exactly 3 short bullet points. "
        "Keep only useful facts. Do not invent details.\n\n"
        f"Transcript:\n{transcript}"
    )
    response = client.chat.completions.create(  # Groq chat summary
        model="llama-3.1-8b-instant",  # Fast text model
        messages=[{"role": "user", "content": prompt}],  # User message
        temperature=0.2,  # Stable tone
    )
    return response.choices[0].message.content.strip()  # Summary text


def text_to_speech(summary: str, out_file: Path) -> Path:
    speakable = summary.replace("-", " ").replace("\n", ". ")  # Speakable text
    tts = gTTS(text=speakable, lang="en")  # Build TTS request
    tts.save(str(out_file))  # Save mp3
    return out_file  # Return path


transcript = speech_to_text(audio_path)  # Stage 1: audio -> text
print("\n=== TRANSCRIPT ===")  # Section label
print(transcript)  # Show transcript

summary = summarize(transcript)  # Stage 2: text -> summary
print("\n=== SUMMARY ===")  # Section label
print(summary)  # Show summary

spoken_path = text_to_speech(summary, Path("summary_spoken.mp3"))  # Stage 3
print("\n=== SPOKEN SUMMARY FILE ===")  # Section label
print(spoken_path.resolve())  # Show final audio path
```

**How the code works:**

- Stage 1 uses Groq Whisper on `sample_voice_note.mp3`
- Stage 2 uses the same Groq client to summarize
- Stage 3 uses gTTS and needs no LLM key
- One cloud LLM provider, one key

### Activity — Pipeline Run Card

| Stage | Output | Pass? |
|---|---|---|
| Speech-to-Text | transcript text | Yes / No |
| Summarize | 3 bullets | Yes / No |
| Text-to-Speech | `summary_spoken.mp3` | Yes / No |

If any stage fails, fix **only that stage**, then re-run.

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

import os  # Environment variables
import base64  # Encode image bytes
from pathlib import Path  # File paths
from groq import Groq  # Same lab provider
from dotenv import load_dotenv  # Load secrets


load_dotenv()  # Load .env
api_key = os.getenv("GROQ_API_KEY")  # Single lab key
if not api_key:  # Require key
    raise ValueError("Set GROQ_API_KEY in your .env file.")  # Setup error

image_path = Path("sample_notice.jpg")  # Course sample image
if not image_path.exists():  # Ensure download step was done
    raise FileNotFoundError("Run the sample-file creation code first.")  # Setup reminder

image_b64 = base64.b64encode(image_path.read_bytes()).decode("utf-8")  # Encode image
client = Groq(api_key=api_key)  # Cloud client

response = client.chat.completions.create(  # Vision request
    model="meta-llama/llama-4-scout-17b-16e-instruct",  # Vision-capable Groq model (verify current name)
    messages=[  # Multimodal message
        {
            "role": "user",  # User provides image + instruction
            "content": [  # Mixed content list
                {
                    "type": "text",  # Text instruction
                    "text": "Describe this image in one or two short sentences. Focus on useful facts only.",
                },
                {
                    "type": "image_url",  # Image content
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{image_b64}",  # Inline image
                    },
                },
            ],
        }
    ],
    temperature=0.2,  # Steady description
)

description = response.choices[0].message.content  # Extract description
print("Image description:")  # Label output
print(description)  # Show vision result
```

**How the code works:**

- The sample image is encoded and sent to Groq
- The model returns a short description
- No second API key is required

If the vision model name changes, check the current vision model list in the Groq console and update the `model=` string only.

### Optional: Vision with Ollama Cloud Later

Same rule as summary: try this **instead of** Groq vision, not in addition, if you want the other provider.

```python
# Optional later practice: vision with Ollama Cloud (OLLAMA_API_KEY only)

import os  # Environment variables
import base64  # Encode image
from pathlib import Path  # Paths
from openai import OpenAI  # OpenAI-compatible client
from dotenv import load_dotenv  # Load .env


load_dotenv()  # Load OLLAMA_API_KEY for this experiment only
api_key = os.getenv("OLLAMA_API_KEY")  # Ollama Cloud key
if not api_key:  # Require key for optional path
    raise ValueError("Set OLLAMA_API_KEY only if trying Ollama Cloud.")  # Setup note

image_path = Path("sample_notice.jpg")  # Same sample image
image_b64 = base64.b64encode(image_path.read_bytes()).decode("utf-8")  # Encode image

client = OpenAI(  # Ollama Cloud client
    base_url="https://ollama.com/v1",  # Cloud endpoint
    api_key=api_key,  # Single key
)

response = client.chat.completions.create(  # Vision chat request
    model="llava",  # Confirm vision tag on ollama.com/library
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Describe this image in one or two short sentences.",
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{image_b64}",
                    },
                },
            ],
        }
    ],
    temperature=0.2,
)

print(response.choices[0].message.content)  # Show description
```

**How the code works:**

- Optional path for students who want to compare providers
- Main notes path remains **Groq-only**

### Activity — Speech vs Vision Inputs

| Question | Your answer |
|---|---|
| What input did speech use? | |
| What input did vision use? | |
| What output type is shared by both paths? | |
| When would you use vision instead of speech? | |

**Suggested direction:** Speech uses audio; vision uses an image; both can produce text; use vision for posters, screenshots, and diagrams that were never spoken.

---

## Troubleshooting

| Symptom | Likely cause | What to try |
|---|---|---|
| `401` / unauthorized | Missing or wrong `GROQ_API_KEY` | Recheck `.env`; restart terminal/notebook |
| Sample file not found | Download step skipped | Run the sample download code first |
| Empty transcript | Silent or corrupt audio | Re-download `sample_voice_note.mp3` from the course link |
| Vision model error | Model name changed | Pick a current vision model in Groq console |
| Summary invents facts | Prompt too loose | Keep “do not invent details” in the prompt |

**Important rule:**

> If one stage fails, test STT, summary, TTS, and vision as separate functions. Do not add a second LLM key to “fix” a failed stage.

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
| Multimodal | Using more than one data type (text, audio, image) |
| Pipeline | Ordered stages where each output feeds the next step |
| Speech-to-Text (STT) | Audio → transcript text |
| Transcript | Written form of spoken audio |
| Summarization | Long text → short useful points |
| Text-to-Speech (TTS) | Text → spoken audio file |
| Vision | Image → text description |
| Groq | Cloud provider used in these notes for STT, summary, and vision |
| `GROQ_API_KEY` | Only LLM API key required for the main lab |
| Ollama Cloud | Other provider you may try later for summary and vision |
| `OLLAMA_API_KEY` | Key used only if you switch to the Ollama Cloud experiment |
| `groq` | Python package for Groq cloud calls |
| `gTTS` | Network Text-to-Speech client (no LLM key) |
| `python-dotenv` | Loads secrets from `.env` |
| `requests` | Downloads sample files from S3 |
| `base64` | Encodes image bytes for vision requests |
| Sample audio | `sample_voice_note.mp3` from course S3 |
| Sample transcript text | Expected words for quality check |
| Sample image | `sample_notice.jpg` from course S3 |
