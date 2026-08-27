# Multimodal Pipelines (Speech and Vision Models)

## Introduction

In the **previous** session you practised **retrieval tuning** on a fixed eval set — measuring **hit rate**, classifying **retrieval vs generation** failures, and proving **before/after** improvement. That work stays in the **text + documents** world.

This session adds **speech** and **vision**. You will build a **multimodal pipeline**: speech becomes text, text becomes a short summary, and the summary becomes speech again. You will also see where a simple **vision** step (image → short description) fits alongside the speech path.

Before the main lab, we also revisited **multimodal RAG** — how PDFs with pictures need smarter **parsing** before chunking and embedding.

**What you will learn:**

- Map a **multimodal agent pipeline**: audio in → text → summary → audio out, and where image → description fits
- Run **Speech-to-Text** on a short sample audio file and check transcript quality
- **Summarize** the transcript with **one cloud provider (Groq)**
- Integrate **Text-to-Speech**, run the full pipeline once, and try a **lite vision** step with **Hugging Face** captioning models

**Lab rule:** Heavy model work runs on a **cloud API**. Your laptop only downloads small sample files and prints results.

**One provider for the speech + summary lab:** These notes demonstrate STT and summary with **Groq** and a single key, `GROQ_API_KEY`. **gTTS** handles speech output and needs no LLM key. After the lab, you may try the **summary** step with **Ollama Cloud** instead (that path uses `OLLAMA_API_KEY` only — still one key, not both at once).

**Where to run the code:** **Google Colab** is beginner-friendly because many libraries are pre-installed. Local editors (for example VS Code or Antigravity) work too, but you install packages yourself. Either path is fine for this lab.

---

## Multimodal RAG — Parsing PDFs with Images

Real PDFs are not plain text. Manuals, invoices, and hostel notices often mix **paragraphs**, **tables**, **charts**, and **pictures**.

- **Official Definition:** **Document parsing** extracts structured content from files before chunking and embedding in a RAG pipeline.
- **In Simple Words:** Read the PDF properly first — text, images, and tables — before you split it into chunks.
- **Real-Life Example:** A fan datasheet PDF has logos, wiring diagrams, and spec tables. A text-only loader would skip the pictures.

### Why parsing matters in RAG

The RAG steps after parsing stay the same: **chunk → embed → store → retrieve → generate**. What changes is the **input step**.

| Loader type | What it reads | What it skips |
|---|---|---|
| Plain text / PyPDF loader | Selectable text in the PDF | Images, charts, scanned text in pictures |
| **LlamaParse** (cloud) | Text, images, tables; can auto-chunk and embed | — |
| **PyMuPDF** (open source) | Similar parsing goals locally | Heavier setup on your machine |

**Common mistake:** Assuming every PDF is “just text” because a simple demo worked.

**Better habit:** Inspect one real PDF. If pictures carry facts, use a **multimodal parser** before chunking.

### Multimodal chunks

In **multimodal RAG**, each **text block** and each **extracted image** can become its own chunk. Both get **embeddings** so retrieval can return words or visuals.

![Multimodal overview showing text questions, voice notes, and campus notice photos as three input types that can produce written answers, spoken summaries, or short image descriptions](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session51/session51-01-multimodal-overview.png)

**Tools to explore later:** [LlamaParse](https://cloud.llamaindex.ai) (free tier for practice) and the Python library **PyMuPDF** for open-source parsing.

---

## What Multimodal Means

Most agent labs so far used **text in** and **text out**. Real products also use voice notes and photos.

- **Official Definition:** **Multimodal** AI systems accept or produce more than one type of data, such as text, audio, or images.
- **In Simple Words:** The agent can work with more than typed words.
- **Real-Life Example:** WhatsApp lets you send text, voice notes, and photos in one chat. A multimodal pipeline does a similar mix, step by step.

Behind the scenes, every modality is converted to **numbers** (tokens and embeddings) before the model reasons. Text, audio, and images all pass through an **embedding** step internally.

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

![Speech pipeline flow from campus voice note through Speech-to-Text, summarization, and Text-to-Speech to a spoken summary the student can listen to](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session51/session51-02-speech-pipeline-flow.png)

### Where Vision Fits

Vision is a **parallel input path**, not a replacement for speech.

```text
Sample image file (photo / screenshot)
        |
        v
[Vision] Image --> short description (image-captioning model)
```

![Vision as a parallel input path where a campus notice photo is sent to a cloud vision model and returns a short text description alongside the main speech pipeline](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session51/session51-03-vision-parallel-path.png)

In class we ran the **speech path live**. The **vision** step was introduced conceptually; **Groq does not host image models**, so the lite vision try uses **Hugging Face** captioning models on your machine or another hosted vision API.

### Provider Choice (Read Once)

| What you need | This lab (shown in notes) | Other option to try later |
|---|---|---|
| Speech-to-Text | **Groq** Whisper | — |
| Summarize | **Groq** chat model | **Ollama Cloud** chat model |
| Text-to-Speech | **gTTS** (network TTS, not an LLM key) | Same |
| Vision (lite step) | **Hugging Face** image-captioning model | Other hosted vision APIs |
| API key for the speech + summary lab | **Only** `GROQ_API_KEY` | If you switch summary provider: **only** `OLLAMA_API_KEY` |

**Important:** You are **not** required to run Groq and Ollama Cloud together. Pick **one** cloud LLM provider for summary experiments.

![Cloud lab setup showing a light laptop downloading sample files while heavy speech and vision models run in the cloud with one API key and gTTS as a separate speech service](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session51/session51-04-cloud-laptop-one-key.png)

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

### Install light Python packages

```bash
pip install groq python-dotenv gTTS pillow requests
```

For the optional vision step, install captioning dependencies separately:

```bash
pip install transformers torch
```

These packages are **clients** or **model loaders**. Heavy speech models run on **Groq**; captioning models download from **Hugging Face** when you first run the vision script.

### Environment variable (one key only)

Create a `.env` file in your project folder (do **not** commit it to Git):

```text
GROQ_API_KEY=your_groq_key_here
```

- Create a Groq key from [console.groq.com](https://console.groq.com)
- Do **not** add an Ollama key for the main lab path in these notes

**Common mistake:** Creating two keys and thinking two LLMs are required for one pipeline.

**Better habit:** One provider, one key, three speech-pipeline stages.

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

![Transcript quality checklist comparing Speech-to-Text output against expected campus update text for completeness, numbers, meaning, and noise](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session51/session51-05-transcript-quality-check.png)

You can also ask an **LLM-as-judge** to score transcript quality, but start with a **human read** against the sample text on short clips.

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
        model="whisper-large-v3",  # Groq hosted Whisper model
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

Customize the **system message** to control summary shape — for example “exactly 3 bullets” or “include only policy facts.”

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

TTS here uses **gTTS** (Google Text-to-Speech). It is a network speech service with a generous free tier. It is **not** a second LLM and needs **no** `GROQ_API_KEY`.

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
out_path = Path("spoken_summary.mp3")  # Output spoken summary
tts.save(str(out_path))  # Write mp3 file
print("Spoken summary saved to:", out_path.resolve())  # Confirm path
```

**How the code works:**

- Summary text is cleaned into speakable sentences
- `gTTS` requests speech from a remote service
- `spoken_summary.mp3` is saved for playback
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

spoken_path = text_to_speech(summary, Path("spoken_summary.mp3"))  # Stage 3
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
| Text-to-Speech | `spoken_summary.mp3` | Yes / No |

If any stage fails, fix **only that stage**, then re-run.

---

## Vision Basics — Image to Short Description

Speech is one modality. Vision is another. Here you send the sample image to an **image-captioning model** and get a short description.

- **Official Definition:** **Vision** models accept image input and return text such as a caption or description.
- **In Simple Words:** The model looks at a picture and tells you what it sees.
- **Real-Life Example:** A phone gallery search finds “beach photos” by understanding image content.

**Groq does not host image models.** For this lite step, use a **Hugging Face** captioning model locally (or another hosted vision API). Behind the scenes, many vision models use **CNN**-style feature extraction before generating text.

### Full Code — Describe the Sample Image with Hugging Face

```python
# Vision basics: sample image -> short description using Hugging Face
# Install first: pip install transformers torch pillow

from pathlib import Path  # File paths
from transformers import pipeline  # High-level model loader


image_path = Path("sample_notice.jpg")  # Course sample image
if not image_path.exists():  # Ensure download step was done
    raise FileNotFoundError("Run the sample-file creation code first.")  # Setup reminder

captioner = pipeline(  # Build image-to-text pipeline
    "image-to-text",  # Task type
    model="Salesforce/blip-image-captioning-base",  # Lightweight caption model
)

result = captioner(str(image_path))  # Run caption on local file
description = result[0]["generated_text"]  # Extract caption text
print("Image description:")  # Label output
print(description)  # Show vision result
```

**How the code works:**

- The `pipeline` helper downloads the model on first run
- The sample image path is passed directly to the captioner
- Output is a short natural-language description you can feed into a later RAG or agent step

**Common mistake:** Expecting the same `GROQ_API_KEY` to handle images.

**Better habit:** Treat vision as a **separate tool** on a parallel path, just like in the pipeline diagram.

### Activity — Speech vs Vision Inputs

| Question | Your answer |
|---|---|
| What input did speech use? | |
| What input did vision use? | |
| What output type is shared by both paths? | |
| When would you use vision instead of speech? | |

**Suggested direction:** Speech uses audio; vision uses an image; both can produce text; use vision for posters, screenshots, and diagrams that were never spoken.

---

## Real-World Applications

The same building blocks appear in products you already use.

### Masai / Zoom — class transcripts and AI Summary

- **Zoom** runs **Speech-to-Text** on live session audio.
- Transcripts are stored as **embeddings** in a **vector database**.
- **AI Summary** and **AI Tutor** retrieve relevant transcript chunks to answer student questions about what was taught.

This is **STT + RAG**, not only summarization.

### YouTube and NotebookLM

- **YouTube** auto-captions are a live **STT** example on long videos.
- A **YouTube summarization pipeline** can: extract audio → STT → summarize → optional TTS.
- **NotebookLM** ingests a YouTube URL, stores the transcript in a vector store, and supports **Q&A** plus **audio overview** (summary read aloud with TTS).

### Customer support and voice-enabled RAG

- A caller speaks → **STT** → agent reasons → **TTS** reply (no human typing).
- In text RAG apps, a **microphone button** can run STT on the question, retrieve chunks, and optionally **read the answer aloud**.

### ChatGPT voice mode (conceptual)

- Voice input is transcribed, processed by the chat model, and spoken back with **TTS**.
- Summarization happens only when the product or prompt asks for it — not on every voice turn.

---

## Choosing Cloud Models — Benchmarks (Quick Reference)

When a client asks “Groq or OpenAI or Anthropic?”, compare **benchmarks** and your own eval data.

| Benchmark | What it tests |
|---|---|
| **MMLU** | Broad knowledge and reasoning |
| **HumanEval** | Code generation |
| **TruthfulQA** | Factual accuracy |
| **SWE-bench** | Software engineering tasks |

**Groq** is strong on **speed and cost** (open-source models, infrastructure pricing). **OpenAI** and **Anthropic** models often score higher on reasoning benchmarks but are **paid**. Pick based on task, budget, and your own fixed eval set — not marketing alone.

---

## Troubleshooting

| Symptom | Likely cause | What to try |
|---|---|---|
| `401` / unauthorized | Missing or wrong `GROQ_API_KEY` | Recheck `.env`; restart terminal/notebook |
| Sample file not found | Download step skipped | Run the sample download code first |
| Empty transcript | Silent or corrupt audio | Re-download `sample_voice_note.mp3` from the course link |
| Vision model download slow | First Hugging Face run | Wait for model cache; try a smaller BLIP model |
| Summary invents facts | Prompt too loose | Keep “do not invent details” in the prompt |

**Important rule:**

> If one stage fails, test STT, summary, TTS, and vision as separate functions. Do not add a second LLM key to “fix” a failed stage.

---

## Key Takeaways

- A **multimodal pipeline** chains modalities: **Speech-to-Text → summary → Text-to-Speech**, with **vision** as a parallel image-to-text path.
- **Multimodal RAG** needs strong **parsing** (for example LlamaParse or PyMuPDF) before chunking PDFs that contain pictures and tables.
- This lab uses **one cloud provider (Groq)** and **one key (`GROQ_API_KEY`)** for STT and summary. **gTTS** handles spoken output with no LLM key.
- **Groq does not host image models** — use **Hugging Face** captioning or another vision API for the lite image step.
- Real products (class recordings, YouTube tools, NotebookLM, voice agents) reuse the same STT → text → LLM → TTS pattern you built today.

These skills help you design agents that accept voice notes and images, then return short spoken or written answers in later product work.

---

## Important Commands, Libraries, Terminologies Used

| Term / Item | Meaning in this lesson |
|---|---|
| Multimodal | Using more than one data type (text, audio, image) |
| Multimodal RAG | RAG where chunks can include text and images from parsed documents |
| LlamaParse | Cloud document parser that extracts text, images, and tables from PDFs |
| PyMuPDF | Open-source Python library for PDF parsing |
| Pipeline | Ordered stages where each output feeds the next step |
| Speech-to-Text (STT) | Audio → transcript text |
| Transcript | Written form of spoken audio |
| Summarization | Long text → short useful points |
| Text-to-Speech (TTS) | Text → spoken audio file |
| Vision / image captioning | Image → text description |
| Groq | Cloud provider used for STT and summary in this lab |
| `GROQ_API_KEY` | LLM API key for the main speech + summary lab |
| Ollama Cloud | Optional alternate provider for summary experiments |
| `OLLAMA_API_KEY` | Key used only if you switch to the Ollama Cloud experiment |
| gTTS | Google Text-to-Speech client (no LLM key) |
| Hugging Face | Model hub used for local image-captioning in the lite vision step |
| `transformers` | Python library for loading captioning pipelines |
| `groq` | Python package for Groq cloud calls |
| `python-dotenv` | Loads secrets from `.env` |
| `requests` | Downloads sample files from S3 |
| LLM-as-judge | Optional automated scoring of transcript quality |
| Sample audio | `sample_voice_note.mp3` from course S3 |
| Sample transcript text | Expected words for quality check |
| Sample image | `sample_notice.jpg` from course S3 |
