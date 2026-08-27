# Assignment Objective

Total Questions: 10

Difficulty Flow: Easy -> Moderate -> Hard

Question Types:
- 6 MCQ (Single Correct): Q1-Q6
- 4 MSQ (Multiple Correct): Q7-Q10

---

## Q1 (MCQ, Easy)

Ankit's college app lets students send **text messages**, **voice notes**, and **photos** in one chat. The backend can process each type differently. What does **multimodal** mean in this product context?

A. The app only accepts typed English text  
B. The system can accept or produce **more than one type of data** (such as text, audio, or images)  
C. Every input must be converted to SQL tables first  
D. The app can only output spoken audio  

**Correct Answer:** B

**Answer Explanation:**  
**Multimodal** systems work with multiple data types — text, audio, images, and more — not just typed words.

**Why other options are wrong:**  
- A: That describes text-only systems, not multimodal.  
- C: SQL is one structured-data path; multimodal is broader than SQL conversion.  
- D: Multimodal outputs can be text or audio; speech-only output is too narrow.

---

## Q2 (MCQ, Easy)

Meera receives a 90-second **voice note** from the hostel office. Her agent must produce a short written summary. Which pipeline stage must run **first**?

A. Text-to-Speech  
B. Speech-to-Text  
C. Image captioning  
D. Vector retrieval  

**Correct Answer:** B

**Answer Explanation:**  
Audio must become **text (a transcript)** before an LLM can summarize it. **Speech-to-Text** is stage 1 in the speech pipeline.

**Why other options are wrong:**  
- A: TTS converts text **to** audio — it runs at the end, not the start.  
- C: Image captioning applies to photos, not voice notes.  
- D: Retrieval may come later in RAG products; it is not the first step for raw audio.

---

## Q3 (MCQ, Easy)

YouTube plays a lecture video and shows **auto-captions** beneath it while the professor speaks. Which technology is doing the real-time conversion from speech to on-screen text?

A. Text-to-Speech  
B. Speech-to-Text  
C. Semantic chunking  
D. SQL agent routing  

**Correct Answer:** B

**Answer Explanation:**  
Auto-captions are a real-world **Speech-to-Text** use case: spoken audio → written transcript.

**Why other options are wrong:**  
- A: TTS goes from text to speech, the opposite direction.  
- C: Chunking splits documents for RAG; it does not transcribe live audio.  
- D: SQL agents query structured databases, not video speech tracks.

---

## Q4 (MCQ, Easy)

For the main speech + summary lab, Divya uses **Groq** for Whisper STT and chat summarization, and **gTTS** for the spoken `.mp3` output. How many **LLM cloud API keys** does she need for the Groq STT + Groq summary path?

A. Zero  
B. One (`GROQ_API_KEY`)  
C. Two (Groq + gTTS)  
D. Three (Groq + Ollama + Hugging Face)  

**Correct Answer:** B

**Answer Explanation:**  
One **`GROQ_API_KEY`** powers both Groq Whisper and Groq chat summarization. **gTTS** is a separate network TTS service and is **not** an LLM API key.

**Why other options are wrong:**  
- A: Groq cloud calls require an API key.  
- C: gTTS does not count as an LLM key.  
- D: Ollama and Hugging Face are optional alternate paths, not required together for the main lab.

---

## Q5 (MCQ, Moderate)

Rohan built `audio → transcript → summary → spoken_summary.mp3`. He also wants a **one-sentence description** of a canteen **menu photo** that was never spoken aloud. Where should the vision step sit architecturally?

A. Replace Speech-to-Text entirely for all inputs  
B. Run as a **parallel input path** (image → short description) alongside the speech pipeline  
C. Insert vision only between summarization and Text-to-Speech  
D. Use the same Groq Whisper model on the JPEG file  

**Correct Answer:** B

**Answer Explanation:**  
Vision is a **parallel path**: image in → text description out. It does not replace the speech pipeline.

**Why other options are wrong:**  
- A: Speech and vision serve different input types; one does not replace the other.  
- C: Vision is not a mandatory middle step between summary and TTS.  
- D: Whisper is for audio; images need a captioning/vision model.

---

## Q6 (MCQ, Moderate)

Sneha indexes a fan datasheet **PDF** that contains logos, wiring diagrams, and spec tables. Her current **PyPDF-style loader** only reads selectable text and skips pictures. What is the best **next step** before chunking for multimodal RAG?

A. Increase top-k only  
B. Use a **multimodal document parser** (for example LlamaParse or PyMuPDF) to extract text and images  
C. Delete all images from the PDF manually  
D. Abandon RAG and use only keyword search on filenames  

**Correct Answer:** B

**Answer Explanation:**  
When pictures carry facts, you need **document parsing** that extracts images and text **before** chunking and embedding.

**Why other options are wrong:**  
- A: top-k tuning does not recover skipped image content.  
- C: Deleting images loses information the RAG system needs.  
- D: Filename search ignores document content entirely.

---

## Q7 (MSQ, Moderate)

After running Groq Whisper on `sample_voice_note.mp3`, Kavya compares the model transcript with `sample_transcript.txt`. Which checks belong on a **transcript quality checklist**?

A. **Completeness** — main points are present  
B. **Names / numbers** — times and IDs look correct  
C. Summary must contain exactly 10 bullet points  
D. **Meaning** — same message as the expected sample text  

**Correct Answers:** A, B, D

**Answer Explanation:**  
Quality checks focus on whether the transcript is **complete**, **accurate on facts/numbers**, and **faithful in meaning** before summarization.

**Why option C is wrong:**  
Bullet count is a **summarization** format rule, not an STT quality checklist item.

---

## Q8 (MSQ, Moderate)

Which statements are **true** for the **main speech pipeline lab** (Groq STT + Groq summary + gTTS)?

A. Groq hosts **Whisper** for Speech-to-Text  
B. **gTTS** requires `GROQ_API_KEY` to generate speech  
C. The **same Groq client** can be reused for STT and chat summarization  
D. Groq provides ready-to-use **image captioning** models for the lite vision step  

**Correct Answers:** A, C

**Answer Explanation:**  
Groq runs Whisper and chat models under one key. One `Groq` client handles both STT and summary calls.

**Why options B and D are wrong:**  
- B: gTTS is a separate TTS service with **no** Groq LLM key.  
- D: **Groq does not host image models**; vision uses Hugging Face or another vision API.

---

## Q9 (MSQ, Hard)

Which real-world product flows correctly map to **Speech-to-Text → text processing → optional Text-to-Speech**?

A. **YouTube auto-captions** on a lecture video  
B. **NotebookLM audio overview** after ingesting a video transcript  
C. Describing a hostel notice **photo** using only the Whisper model  
D. A **voice customer-support agent** that listens, reasons, and speaks a reply  

**Correct Answers:** A, B, D

**Answer Explanation:**  
YouTube captions, NotebookLM audio overviews, and voice support agents all use STT and often TTS around text/LLM steps.

**Why option C is wrong:**  
A **photo** needs an **image-captioning / vision** path, not Whisper (audio STT).

---

## Q10 (MSQ, Hard)

Which statements about **multimodal RAG** and document parsing are correct?

A. After parsing, the RAG flow is still **chunk → embed → store → retrieve → generate**  
B. Each **extracted image** can become its own chunk with embeddings  
C. A plain text-only PDF loader always extracts **diagrams** as searchable text automatically  
D. Text-only loaders **skip images** in PDFs that may carry important facts  

**Correct Answers:** A, B, D

**Answer Explanation:**  
Parsing improves the **input** step; downstream RAG stages stay the same. Images can be separate chunks; plain loaders miss image content.

**Why option C is wrong:**  
Diagrams embedded as pictures are often **skipped** by text-only loaders — that is exactly why multimodal parsing is needed.
