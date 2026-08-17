lecture ID:

Course Name: Certification in Agentic Systems and Design / Software Engineering with AI

Target Audience : Students from any backgorund may not be necessarily form tech background


session duration: 1hr  50mins

Session Notes Length: 480 lines to 500 lines max

title: Hands-On: Build a Multimodal Agentic App

objective: Build a simple recipe mini-app that combines vision,  speech-to-text and text-to-speech (with optional image generation)  and refuses mismatched or irrelevant inputs gracefully.	

type of session: theory/implementation/mixture of theory + implementation / You take the call

topics be covered: Vision ingredient/scene analysis; STT capture & store; alignment / guardrail checks; recipe generation; TTS audio output; optional image gen; graceful refusal UX	


detailed subtopics to be covered:
* Capture a spoken ingredient list with STT, display it as text, and store it for the agent run
* Run a vision model on an uploaded image to extract ingredients or scene description
* Compare vision output with the dictated text and flag irrelevant images or ingredient mismatches
* Refuse unsafe or nonsensical runs gracefully (no recipe / no audio) with a clear user-facing message
* Generate a structured recipe from aligned multimodal inputs (title, ingredients, steps)
* Produce a TTS audio file that reads the generated recipe aloud
* Optionally generate a dish image when an image-generation API is available (stretch; not required on Groq alone)
* Demo one happy-path run and at least one guardrail failure (e.g. railway image or cement dictation)

Recipe Agentic Mini-App. Core path = Vision + STT + text agent + TTS on Groq (or equivalent). 
Image generation is optional stretch via a non-Groq provider if available.

 Guardrails are a required agent step. 
 
 App flow: 
 (1) Upload ingredients/food image 
 (2) Dictate ingredients → STT → show and store text 
 (3) Vision analyzes image 
 (4) Agent checks alignment + guardrails 
 (5) If OK create recipe; if fail refuse with retry guidance 
 (6) TTS → audio file of recipe 
 (7) Optional image gen → dish preview.