# Assignment Subjective

Total Questions: 1  
Difficulty: Medium  
Type: Practical Implementation

---

## Q1 (Practical, Medium)

Build a **Campus Voice Bulletin Processor** in Python. The hostel office sends short voice updates; your script should turn each bulletin into a **spoken summary** a student can listen to on the way to class.

### Problem Statement

Create a single program that runs the full **Speech-to-Text → Summarize → Text-to-Speech** pipeline on the course sample audio.

Your program must:

1. Load **`GROQ_API_KEY`** from a `.env` file (use `python-dotenv`).
2. Read the local audio file **`sample_voice_note.mp3`** (download it first from the course link if needed):
   `https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module4/session51/sample_voice_note.mp3`
3. Implement **`speech_to_text(audio_path)`** using Groq Whisper (`whisper-large-v3`, `response_format="text"`).
4. Implement **`summarize(transcript)`** using Groq chat with a prompt that asks for **exactly 3 short bullet points** and says **do not invent details**.
5. Implement **`text_to_speech(summary, out_path)`** using **gTTS** and save **`spoken_summary.mp3`**.
6. In **`main()`**, run all three stages in order and print:
   - the **transcript**
   - the **summary**
   - the resolved path to **`spoken_summary.mp3`**
7. Load **`sample_transcript.txt`** (same S3 folder as the audio) and print two simple quality flags:
   - `library_hours_captured`: `True` if the model transcript mentions library hours (e.g. contains `"10"` or `"ten"` and `"library"`, case-insensitive)
   - `student_id_captured`: `True` if the transcript mentions student ID (e.g. contains `"student"` and `"id"`, case-insensitive)

Use model **`llama-3.1-8b-instant`** for summarization (or the current equivalent fast Groq text model).

### Expected Output (sample shape)

Your run should print labeled sections similar to:

```
=== TRANSCRIPT ===
Hello. This is a short campus update. The library is open until 10 PM. Please carry your student ID.

=== SUMMARY ===
- Library open until 10 PM
- Carry student ID
- Short campus update

=== SPOKEN SUMMARY FILE ===
/path/to/spoken_summary.mp3

=== QUALITY FLAGS ===
library_hours_captured: True
student_id_captured: True
```

Exact transcript and bullet wording may vary slightly; quality flags should be `True` when main facts are captured.

### Submission Instruction

- code all the points mentioned in the VS Code in single `.py` file
- run the code and verify its working
- then submit the code in the code editor/answer box in the LMS

---

## Answer Explanation (Complete Ideal Solution)

### Step-by-step Walkthrough

1. Place `sample_voice_note.mp3` and `sample_transcript.txt` in the same folder as your script (download from the course S3 links).
2. Create `.env` with `GROQ_API_KEY=your_key_here`.
3. Build three functions — `speech_to_text`, `summarize`, `text_to_speech` — and call them in order from `main()`.
4. Reuse **one** `Groq` client for STT and summary.
5. Clean summary text for gTTS (replace bullets/newlines with speakable sentences).
6. Run simple string checks on the transcript for library hours and student ID before printing quality flags.

### Complete Reference Code (Single File)

```python
import os
import re
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq
from gtts import gTTS


AUDIO_FILE = Path("sample_voice_note.mp3")
TRANSCRIPT_FILE = Path("sample_transcript.txt")
SPOKEN_OUTPUT = Path("spoken_summary.mp3")
WHISPER_MODEL = "whisper-large-v3"
CHAT_MODEL = "llama-3.1-8b-instant"


def get_groq_client() -> Groq:
  load_dotenv()
  api_key = os.getenv("GROQ_API_KEY")
  if not api_key:
    raise ValueError("Set GROQ_API_KEY in your .env file.")
  return Groq(api_key=api_key)


def speech_to_text(client: Groq, audio_path: Path) -> str:
  if not audio_path.exists():
    raise FileNotFoundError(f"Missing audio file: {audio_path}")
  with audio_path.open("rb") as audio_file:
    result = client.audio.transcriptions.create(
      file=audio_file,
      model=WHISPER_MODEL,
      response_format="text",
    )
  return result.strip() if isinstance(result, str) else str(result).strip()


def summarize(client: Groq, transcript: str) -> str:
  prompt = (
    "Summarize in exactly 3 short bullet points. "
    "Keep only useful facts. Do not invent details.\n\n"
    f"Transcript:\n{transcript}"
  )
  response = client.chat.completions.create(
    model=CHAT_MODEL,
    messages=[{"role": "user", "content": prompt}],
    temperature=0.2,
  )
  return response.choices[0].message.content.strip()


def text_to_speech(summary: str, out_path: Path) -> Path:
  speakable = summary.replace("-", " ").replace("\n", ". ")
  tts = gTTS(text=speakable, lang="en")
  tts.save(str(out_path))
  return out_path.resolve()


def quality_flags(transcript: str) -> dict[str, bool]:
  text = transcript.lower()
  library_hours = ("library" in text) and (("10" in text) or ("ten" in text))
  student_id = ("student" in text) and ("id" in text)
  return {
    "library_hours_captured": library_hours,
    "student_id_captured": student_id,
  }


def main() -> None:
  client = get_groq_client()

  transcript = speech_to_text(client, AUDIO_FILE)
  print("=== TRANSCRIPT ===")
  print(transcript)

  summary = summarize(client, transcript)
  print("\n=== SUMMARY ===")
  print(summary)

  spoken_path = text_to_speech(summary, SPOKEN_OUTPUT)
  print("\n=== SPOKEN SUMMARY FILE ===")
  print(spoken_path)

  flags = quality_flags(transcript)
  print("\n=== QUALITY FLAGS ===")
  print(f"library_hours_captured: {flags['library_hours_captured']}")
  print(f"student_id_captured: {flags['student_id_captured']}")

  if TRANSCRIPT_FILE.exists():
    expected = TRANSCRIPT_FILE.read_text(encoding="utf-8").strip()
    print("\n=== EXPECTED SAMPLE TEXT ===")
    print(expected)


if __name__ == "__main__":
  main()
```

### How the Code Works

- **`get_groq_client`** loads one API key for both STT and summary.
- **`speech_to_text`** uploads the MP3 to Groq Whisper and returns plain text.
- **`summarize`** sends the transcript to a Groq chat model with a strict 3-bullet prompt.
- **`text_to_speech`** uses gTTS (no LLM key) to write `spoken_summary.mp3`.
- **`quality_flags`** applies simple keyword checks taught in the transcript quality checklist.
- **`main`** chains the three pipeline stages and prints labeled output.

### Alternative Valid Approaches

- Download samples with the `requests` snippet from the course notes before running `main()`.
- Compare transcript to `sample_transcript.txt` with a side-by-side print instead of keyword flags.
- Wrap each stage in `try/except` and print which stage failed (STT, summary, or TTS) before re-running.
- Use a separate `download_samples.py` run once locally; submit only the pipeline `.py` if your LMS allows.
