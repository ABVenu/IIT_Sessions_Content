# Hands-On: Build a Multimodal Agentic App

## Introduction

In the **previous** session you built a **multimodal pipeline**: Speech-to-Text on a short voice note, a summary, Text-to-Speech of that summary, and a simple **vision** step (image → short description). Those stages still ran as **separate demos**.

This session joins them into one **recipe mini-app**. You upload a food photo, dictate ingredients, and let an **agent guardrail** check whether the photo and the spoken list belong together. If they align, the app writes a recipe and speaks it; if not, it refuses — **no recipe and no audio**.

**What you will learn:**

- Capture spoken ingredients with **Speech-to-Text**, display the text, and store it
- Run **vision** on an uploaded image to extract ingredients or a scene
- Compare both inputs, **refuse** mismatches, then generate a **recipe** + **TTS** audio
- Optionally generate a **dish preview** if a non-Groq image API is available
- Demo one **happy-path** run and at least one **guardrail failure**

**Lab rule:** Heavy model work stays in the cloud. These notes use **one** LLM key, `GROQ_API_KEY`, for Speech-to-Text, vision, and the text agent. Text-to-Speech still uses **gTTS**, as in the previous session. Image generation is optional and is **not** required on Groq alone.

---

## From Separate Stages to One Mini-App

A pipeline is useful. A product is a pipeline plus a **decision**.

- **Official Definition:** A **multimodal agentic app** takes more than one input type (here: image + speech), uses an agent to **decide** whether the run is valid, and then either completes the task or **refuses**.
- **In Simple Words:** The app looks at the fridge photo, listens to what you said you have, checks they match, then cooks — or politely says no.
- **Real-Life Example:** You send a hostel kitchen photo of tomatoes, onions, and rice, and you say those same items. A helpful roommate writes a tomato-rice recipe and reads it aloud. If you accidentally send a **railway** selfie, they do not invent a “train curry”.

You already know **Speech-to-Text**, **vision**, and **Text-to-Speech**. The new skill is the **alignment / guardrail** step in the middle.

### App flow (lock this before coding)

```text
(1) Upload food / ingredients image
(2) Dictate ingredients → Speech-to-Text → show and store text
(3) Vision analyzes the image
(4) Agent checks alignment + guardrails
(5) If OK → structured recipe; if fail → refuse with retry guidance
(6) Text-to-Speech → audio file of the recipe
(7) Optional: image generation → dish preview (skip if you only have Groq)
```

![Recipe mini-app flow from upload and dictation through Speech-to-Text, vision, alignment guardrails, recipe generation, and spoken audio, with a refuse branch when inputs do not match](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session40/session40-01-app-flow.png)

**Common mistake:** Generating a recipe from *any* photo plus *any* speech.

**Better habit:** Treat guardrails as a **required agent step**. No alignment → no recipe → no audio.

### Activity — Name the Step

Write the step number (1–7) for each job: speak the recipe file; check photo vs speech; extract items from the photo; store the transcript.

**Suggested answers:** 6, 4, 3, 2.

---

## Setup — Same Key, New Sample Files

Install the same light clients as the previous session:

```bash
pip install groq python-dotenv gTTS requests
```

Create a `.env` file (do **not** commit it to Git):

```text
GROQ_API_KEY=your_groq_key_here
```

Create the Groq key from [console.groq.com](https://console.groq.com). You do **not** need a second LLM key for the core path.

### Sample files used in this lab

| Sample | What it is | Download link |
|---|---|---|
| Kitchen photo | Tomatoes, onions, and rice — happy-path image | [sample_kitchen.jpg](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session40/sample_kitchen.jpg) |
| Railway photo | Train platform — irrelevant image for the fail demo | [sample_railway.jpg](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session40/sample_railway.jpg) |
| Spoken ingredients | Voice: “I have tomatoes, onions, and rice.” | [sample_ingredients.mp3](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session40/sample_ingredients.mp3) |
| Cement dictation | Voice: “I have cement, bricks, and steel rods.” | [sample_cement.mp3](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session40/sample_cement.mp3) |

Use the course samples first so everyone tests the **same** happy path and the **same** refusal. Your own fridge photo can wait until the pipeline works.

### Full Code — Download Sample Files

```python
# Download kitchen photo, railway photo, and both sample audio clips
from pathlib import Path  # build local file paths
import requests  # download files from the course links
BASE = "https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session40/"
SAMPLES = {  # local name -> file on S3
    "sample_kitchen.jpg": BASE + "sample_kitchen.jpg",
    "sample_railway.jpg": BASE + "sample_railway.jpg",
    "sample_ingredients.mp3": BASE + "sample_ingredients.mp3",
    "sample_cement.mp3": BASE + "sample_cement.mp3",
}

for filename, url in SAMPLES.items():  # one download per sample
    path = Path(filename)  # save in the current folder
    response = requests.get(url, timeout=60)  # fetch the bytes
    response.raise_for_status()  # stop if the link failed
    path.write_bytes(response.content)  # write the file
    print("Saved:", path.resolve())  # show where it landed
```

**How the code works:** Each sample is saved with a fixed name. Run this block once before Speech-to-Text and vision.

---

## Capture Spoken Ingredients with Speech-to-Text

The mini-app must **hear** the ingredient list, **show** it on screen, and **store** it for the later agent check. That is the same Speech-to-Text habit as the previous session, now used as product input.

- **Official Definition:** **Speech-to-Text (STT)** converts spoken audio into written text (a transcript).
- **In Simple Words:** It types what you said you have in the kitchen.
- **Real-Life Example:** WhatsApp voice-to-text turns “tomatoes, onions, and rice” into a message you can copy.

Live microphone capture is optional at home. In class, run STT on `sample_ingredients.mp3` so the stored text is reliable.

![Two inputs for one agent run: a kitchen photo and a spoken ingredient list, both stored as text the later guardrail can compare](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session40/session40-02-two-inputs.png)

### Full Code — Speech-to-Text, Display, and Store

```python
# Speech-to-Text: spoken ingredients -> printed text -> saved file
import os  # read the API key
from pathlib import Path  # check audio and save transcript
from groq import Groq  # cloud Speech-to-Text client
from dotenv import load_dotenv  # load .env into the process

load_dotenv()  # read GROQ_API_KEY from .env
api_key = os.getenv("GROQ_API_KEY")  # fetch the key string
if not api_key:  # fail early if the key is missing
    raise ValueError("Set GROQ_API_KEY in your .env file.")
client = Groq(api_key=api_key)  # one Groq client for this script
audio_path = Path("sample_ingredients.mp3")  # course voice clip
if not audio_path.exists():  # download step may have been skipped
    raise FileNotFoundError("Run the sample-file download code first.")
with audio_path.open("rb") as audio_file:  # upload the small mp3
    result = client.audio.transcriptions.create(  # Groq Whisper
        file=audio_file, model="whisper-large-v3", response_format="text",
    )
spoken_text = result.strip() if isinstance(result, str) else str(result).strip()
print("Stored spoken ingredients:")  # display for the user
print(spoken_text)  # the text the agent will use later
Path("spoken_ingredients.txt").write_text(spoken_text, encoding="utf-8")
print("Saved to spoken_ingredients.txt")  # confirm storage
```

**How the code works:** Groq Whisper turns the clip into text. You print it (display) and write `spoken_ingredients.txt` (store). The later agent must read this stored text, not a second guess.

### Activity — Check the Stored Text

Note Yes/No: Did the transcript mention tomatoes? Onions? Rice? Close enough to use for alignment?

---

## Vision — Extract Ingredients or a Scene

Speech gave you one list. Vision must give you a second list from the **photo**. Only then can the agent compare them.

- **Official Definition:** A **vision** model accepts image input and returns text such as a caption, scene label, or ingredient list.
- **In Simple Words:** The model looks at the photo and says what is in it.
- **Real-Life Example:** A grocery app camera can list “tomato, onion, rice” from a counter photo — or “train on a platform” from a railway photo.

Ask vision for **edible items** when the photo is food. If the photo is not food, ask for a **short scene label**. That scene label is what the guardrail will reject.

### Full Code — Vision on the Uploaded Image

```python
# Vision: kitchen or railway photo -> ingredient list or scene label
import os  # read the API key
import base64  # encode the image for the API
from pathlib import Path  # locate the photo
from groq import Groq  # same cloud client
from dotenv import load_dotenv  # load .env

load_dotenv()  # read GROQ_API_KEY
api_key = os.getenv("GROQ_API_KEY")  # fetch the key
if not api_key:  # stop if missing
    raise ValueError("Set GROQ_API_KEY in your .env file.")
image_path = Path("sample_kitchen.jpg")  # change to sample_railway.jpg later
if not image_path.exists():  # download step may have been skipped
    raise FileNotFoundError("Run the sample-file download code first.")
image_b64 = base64.b64encode(image_path.read_bytes()).decode("utf-8")
client = Groq(api_key=api_key)  # one Groq client
prompt = (  # food list or non-food scene
    "If this photo shows food or cooking ingredients, list the edible items "
    "as a short comma-separated list. If it is not food, describe the scene "
    "in one short sentence. Do not invent items that are not visible."
)
response = client.chat.completions.create(  # vision chat call
    model="meta-llama/llama-4-scout-17b-16e-instruct",  # Groq vision model
    messages=[{"role": "user", "content": [
        {"type": "text", "text": prompt},  # the instruction
        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_b64}"}},
    ]}],
    temperature=0.2,  # keep the description stable
)
vision_text = response.choices[0].message.content.strip()  # model output
print("Vision output:")  # display for the user
print(vision_text)  # this string goes to the alignment agent
Path("vision_output.txt").write_text(vision_text, encoding="utf-8")
```

**How the code works:** The photo is encoded and sent to Groq vision. Kitchen photos should list tomatoes, onions, and rice; railway photos should describe a train or platform.

### Activity — Two Photos, Two Outputs

Run vision once on `sample_kitchen.jpg` and once on `sample_railway.jpg`. Write one line for each. Which output is safe to cook from?

---

## Alignment and Guardrails — The Required Agent Step

You now have **two texts**: spoken ingredients and vision output. The agent’s job is to decide: cook, or refuse.

- **Official Definition:** An **alignment check** compares two modalities (here: image understanding vs spoken text) and flags mismatch, irrelevance, or unsafe content. A **guardrail** is the rule that **blocks** the rest of the pipeline when the check fails.
- **In Simple Words:** If the photo and the voice note do not belong to the same cooking story, stop.
- **Real-Life Example:** A canteen cook will not follow “make tomato rice” if you handed them a photo of the **railway**. They also will not cook if you dictated **cement and bricks**.

![Alignment guardrail: matching kitchen photo and speech continue to a recipe; a railway photo or a cement dictation is refused](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session40/session40-03-alignment-guardrail.png)

### What should fail

| Case | Image | Spoken text | Expected decision |
|---|---|---|---|
| Happy path | Kitchen (tomatoes, onions, rice) | “I have tomatoes, onions, and rice.” | **Aligned** → recipe + audio |
| Irrelevant image | Railway platform | Same kitchen speech | **Refuse** — photo is not food |
| Unsafe / nonsense speech | Kitchen | “I have cement, bricks, and steel rods.” | **Refuse** — not edible |
| Ingredient mismatch | Only tomatoes and onions | “I have fish, prawns, and coconut.” | **Refuse** — lists do not match |

**Common doubt:** “Can the model still invent a nice recipe from a train photo?” It *can* invent. Your **product** must not allow it.

**Better habit:** If `aligned` is false, skip recipe generation and skip Text-to-Speech. Print a **clear retry message** instead.

The agent should return **JSON**, not a paragraph, so your Python code can branch:

```json
{
  "image_is_food": true, "spoken_is_food": true, "aligned": true,
  "reason": "Both lists are edible and overlap.",
  "user_message": "Inputs look aligned. Creating a recipe.",
  "vision_items": ["tomato", "onion", "rice"],
  "spoken_items": ["tomato", "onion", "rice"]
}
```

On failure, `aligned` is `false` and `user_message` tells the user what to fix (new photo, new dictation, or both).

---

## Generate a Structured Recipe, Then Speak It

Only after a **pass** should the text agent write a recipe. Only after a recipe exists should Text-to-Speech run.

- **Official Definition:** A **structured recipe** is a fixed shape: **title**, **ingredients**, and numbered **steps**. **Text-to-Speech (TTS)** converts that text into a spoken audio file.
- **In Simple Words:** Write a small cooking card, then read it aloud.
- **Real-Life Example:** A hostel cookbook page for “Tomato Onion Rice”, plus a voice note you can play while you cook.

Keep the recipe **simple and vegetarian-friendly** for this lab: pantry items plus the aligned ingredients. Do not add meat, alcohol, or extra spices that were never in the inputs.

![Happy-path outputs: a structured Tomato Onion Rice recipe card and a recipe_audio.mp3 file the student can play](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session40/session40-04-happy-path-outputs.png)

Text-to-Speech here uses **gTTS**, the same network speech service as the previous session. It is **not** a second LLM key. If the guardrail failed, show a calm retry message and create **neither** `recipe.txt` nor `recipe_audio.mp3`.

![Graceful refusal: a clear retry message on screen, with recipe and audio shown as not created](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session40/session40-05-refusal-ux.png)

---

## Full Mini-App — One Run with Guardrails

Connect the stages in one script. Change only `IMAGE_PATH` and `AUDIO_PATH` at the bottom to switch between the happy path and a failure demo.

### Full Code — Vision + Speech-to-Text + Guardrail + Recipe + Text-to-Speech

```python
# Recipe mini-app: STT + vision + alignment guardrail + recipe + TTS
import os  # read GROQ_API_KEY
import json  # parse the guardrail JSON
import base64  # encode the uploaded image
from pathlib import Path  # local files
from groq import Groq  # STT, vision, and text agent
from gtts import gTTS  # speak the recipe
from dotenv import load_dotenv  # load .env

load_dotenv()  # read the key
api_key = os.getenv("GROQ_API_KEY")  # fetch it
if not api_key:  # fail clearly
    raise ValueError("Set GROQ_API_KEY in your .env file.")
client = Groq(api_key=api_key)  # one Groq client for all LLM stages

def speech_to_text(path: Path) -> str:  # audio -> stored transcript
    with path.open("rb") as audio_file:  # open the clip
        result = client.audio.transcriptions.create(  # Groq Whisper
            file=audio_file, model="whisper-large-v3", response_format="text",
        )
    text = result.strip() if isinstance(result, str) else str(result).strip()
    Path("spoken_ingredients.txt").write_text(text, encoding="utf-8")  # store
    return text  # also return for this run

def vision_analyze(path: Path) -> str:  # image -> ingredients or scene
    image_b64 = base64.b64encode(path.read_bytes()).decode("utf-8")  # encode
    prompt = (  # food list or non-food scene
        "If this photo shows food or cooking ingredients, list the edible items "
        "as a short comma-separated list. If it is not food, describe the scene "
        "in one short sentence. Do not invent items that are not visible."
    )
    response = client.chat.completions.create(  # Groq vision
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[{"role": "user", "content": [
            {"type": "text", "text": prompt},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_b64}"}},
        ]}],
        temperature=0.2,
    )
    text = response.choices[0].message.content.strip()  # vision text
    Path("vision_output.txt").write_text(text, encoding="utf-8")  # store
    return text

def check_alignment(vision_text: str, spoken_text: str) -> dict:  # required guardrail
    prompt = (  # force a JSON decision
        "You are a safety checker for a home-cooking app. Compare the vision "
        "output with the spoken ingredient list. Return JSON with keys: "
        "image_is_food (boolean), spoken_is_food (boolean), aligned (boolean), "
        "reason (string), user_message (string), vision_items (array of strings), "
        "spoken_items (array of strings). Set aligned=false if the image is not "
        "food, the speech is not edible food, the lists clearly mismatch, or the "
        "request is unsafe/nonsensical. user_message must be polite retry guidance "
        "when aligned is false.\n\n"
        f"VISION:\n{vision_text}\n\nSPOKEN:\n{spoken_text}"
    )
    response = client.chat.completions.create(  # Groq text agent
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        response_format={"type": "json_object"},  # parseable output
    )
    return json.loads(response.choices[0].message.content)  # dict for branching

def generate_recipe(vision_text: str, spoken_text: str) -> str:  # only after a pass
    prompt = (  # structured cooking card
        "Create one simple home recipe using only the aligned ingredients plus "
        "basic pantry items (oil, salt, water). Return plain text with: Title, "
        "Ingredients (bullets), Steps (numbered). Keep it short. Do not add meat "
        "or extra ingredients that were not implied.\n\n"
        f"VISION:\n{vision_text}\n\nSPOKEN:\n{spoken_text}"
    )
    response = client.chat.completions.create(  # Groq text agent
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    recipe = response.choices[0].message.content.strip()  # recipe text
    Path("recipe.txt").write_text(recipe, encoding="utf-8")  # save
    return recipe

def speak_recipe(recipe: str, out_file: Path) -> Path:  # text -> mp3
    speakable = recipe.replace("#", " ").replace("*", " ")  # cleaner speech
    tts = gTTS(text=speakable, lang="en")  # network TTS, no extra LLM key
    tts.save(str(out_file))  # write recipe_audio.mp3
    return out_file

def run_mini_app(image_path: Path, audio_path: Path) -> None:  # full flow
    print("\n=== (2) SPOKEN INGREDIENTS (STT) ===")
    spoken = speech_to_text(audio_path)  # capture, display, store
    print(spoken)
    print("\n=== (3) VISION ===")
    vision = vision_analyze(image_path)  # extract ingredients or scene
    print(vision)
    print("\n=== (4) ALIGNMENT / GUARDRAIL ===")
    verdict = check_alignment(vision, spoken)  # required agent step
    print(json.dumps(verdict, indent=2))
    if not verdict.get("aligned"):  # refuse path
        print("\n=== (5) REFUSED ===")
        print(verdict.get("user_message", "Please try again with a food photo and edible ingredients."))
        print("No recipe generated. No audio file created.")
        return  # skip recipe and TTS
    print("\n=== (5) RECIPE ===")
    recipe = generate_recipe(vision, spoken)  # structured recipe
    print(recipe)
    print("\n=== (6) TTS AUDIO ===")
    audio_out = speak_recipe(recipe, Path("recipe_audio.mp3"))  # speak it
    print("Saved:", audio_out.resolve())


# Happy path (default). For a fail demo, swap the paths below.
IMAGE_PATH = Path("sample_kitchen.jpg")  # or sample_railway.jpg
AUDIO_PATH = Path("sample_ingredients.mp3")  # or sample_cement.mp3
if not IMAGE_PATH.exists() or not AUDIO_PATH.exists():  # samples missing
    raise FileNotFoundError("Run the sample-file download code first.")
run_mini_app(IMAGE_PATH, AUDIO_PATH)  # one complete agent run
```

**How the code works:** Stages 2 and 3 store the transcript and the vision text. Stage 4 is the **required** JSON guardrail: if `aligned` is false, the function **returns early** with no `recipe.txt` and no `recipe_audio.mp3`. If it passes, Groq writes a short recipe and gTTS reads it aloud.

---

## Demo — One Happy Path and One Refusal

Run the mini-app **twice**. Do not skip the failure demo. Guardrails that you never test are not guardrails.

### Happy path

Keep the default paths: `sample_kitchen.jpg` + `sample_ingredients.mp3`.

| Check | Expected |
|---|---|
| STT text | Tomatoes, onions, and rice |
| Vision text | Same kitchen items (wording may differ) |
| `aligned` | `true` |
| Files created | `recipe.txt` and `recipe_audio.mp3` |

Play `recipe_audio.mp3`. You should hear the recipe, not the original voice clip.

### Guardrail failure (pick at least one)

**Railway image:** `IMAGE_PATH = Path("sample_railway.jpg")` and keep `sample_ingredients.mp3`.

**Cement dictation:** keep `sample_kitchen.jpg` and set `AUDIO_PATH = Path("sample_cement.mp3")`.

| Check | Expected |
|---|---|
| `aligned` | `false` |
| Message | Clear retry guidance (new photo and/or edible speech) |
| Recipe / audio | **Not** created for this failed run |

Delete any old `recipe.txt` / `recipe_audio.mp3` before the fail run if you want a clean folder. The important proof is the printed **REFUSED** block.

### Activity — Demo Run Card

Mark Yes/No: Happy path produced a recipe? Happy path produced audio? Railway or cement run refused? Message told you what to fix?

---

## Optional — Dish Preview Image

A dish **preview** is a generated picture of the finished recipe. Groq in this lab does **not** provide image generation, so this step is optional.

- **Official Definition:** **Image generation** creates a new picture from a text prompt (for example, “a plate of tomato onion rice”).
- **In Simple Words:** After the recipe is ready, draw a preview photo of the dish.
- **Real-Life Example:** A cookbook cover sketch of the plate, not a photo of your raw tomatoes.

If you have another provider’s key (for example an OpenAI image API), call it **only after** alignment passed and the recipe exists. If you only have `GROQ_API_KEY`, skip this step. The core mini-app is already complete.

```python
# Optional: dish preview prompt (needs a non-Groq image API; skip on Groq-only)
from pathlib import Path  # read the saved recipe
recipe = Path("recipe.txt").read_text(encoding="utf-8")  # only after a passed run
prompt = "Simple Indian home-cooked plate: " + recipe[:200]  # short prompt
print(prompt)  # send this to your image API if you have one
```

**How the code works:** It prepares a prompt from the real recipe only after a passed run. Skip it if you only have Groq.

---

## Troubleshooting

| Symptom | Likely cause | What to try |
|---|---|---|
| `401` / unauthorized | Missing or wrong `GROQ_API_KEY` | Recheck `.env`; restart the notebook |
| Sample file not found | Download step skipped | Run the sample download code first |
| Empty STT text | Silent or corrupt audio | Re-download `sample_ingredients.mp3` |
| Vision / JSON error | Model name changed or extra text | Update the vision model; keep `json_object` |
| Recipe or old audio after a fail | Skipped `aligned` check, or leftover files | Return early; delete old `recipe_audio.mp3` |

**Important rule:** If one stage fails, test Speech-to-Text, vision, and the guardrail as separate functions. Do not add a second LLM key to “fix” a failed stage.

---

## Key Takeaways

- A **multimodal agentic app** joins **vision**, **Speech-to-Text**, a **text agent**, and **Text-to-Speech** into one user journey — not four disconnected demos.
- **Alignment / guardrails** are a **required** step: compare the photo with the spoken list before you cook.
- On failure, **refuse gracefully**: a clear retry message, **no recipe**, **no audio**.
- On success, return a **structured recipe** and a **spoken** `.mp3` the user can play while cooking.
- **Image generation** is optional and needs a non-Groq provider; the Groq path alone is enough for the core app.

These habits carry into later agent work, where the system must **remember** user preferences across runs and still refuse unsafe requests instead of completing every prompt.

---

## Important Commands, Libraries, Terminologies Used

| Term / Item | Meaning in this lesson |
|---|---|
| Multimodal agentic app | Image + speech in; agent decides; recipe or refusal out |
| Speech-to-Text (STT) | Spoken ingredients → stored transcript |
| Vision | Photo → ingredient list or scene description |
| Alignment check | Compare vision text with spoken text |
| Guardrail | Block recipe and audio when the check fails |
| Graceful refusal | Clear retry message; no recipe; no audio |
| Structured recipe | Title + ingredients + numbered steps |
| Text-to-Speech (TTS) | Recipe text → `recipe_audio.mp3` |
| Groq / `GROQ_API_KEY` | Cloud key for STT, vision, and the text agent |
| gTTS | Network TTS used to speak the recipe |
| Image generation | Optional dish preview; not required on Groq |
| Groq models | Whisper STT; Llama 4 Scout vision; Llama 3.1 Instant for guardrail + recipe |
| Sample files | `sample_kitchen.jpg`, `sample_railway.jpg`, `sample_ingredients.mp3`, `sample_cement.mp3` |
