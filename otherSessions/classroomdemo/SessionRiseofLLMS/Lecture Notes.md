# The Rise of Large Language Models

## What these notes cover

Computers, the internet, and web apps already make life faster. They still follow instructions exactly as someone wrote them. They do not decide.

These notes follow how machines learned to work with **language**, and how that became the AI people use every day: ChatGPT, Gemini, Claude, and the live assistants that can see and talk.

- How **traditional software** differs from **AI**
- How **NLP** made AI something anyone can use, by speaking or typing ordinary language
- The rise of **large language models (LLMs)**, from the first GPT models to today
- How an LLM produces the next word
- What **GPT** and **Project Astra** do now: models that reason, see, talk, and start to act

Machine learning, neural networks, and deep learning are named briefly. The focus is language.

---

## 1. Software that follows rules, and software that decides

### A phone already shows the difference

You may have used **face unlock**.

<image src="https://coding-platform.s3.amazonaws.com/dev/lms/tickets/c7bf5c19-a7a2-48cd-8727-2962bea3b831/HZswk1YVUZlgqwp0.png" width="300px" />

Another person also has eyes, a nose, and a mouth. The phone still stays locked.

A rule such as “if a face has two eyes, unlock” would open for almost everyone. Face unlock does something else. It **matches a pattern** it learned from your face and **decides** whether this face is yours.

That decision is the start of **artificial intelligence (AI)**: a system that handles a task which used to need a person to look, judge, or choose.

### Traditional software

Traditional software is a list of instructions.

- A programmer writes every case in advance.
- The program checks those cases and does exactly what the code says.
- The same input gives the same result.
- A new situation that was never written down has no answer, unless a person adds a new rule.

A railway warning built only with traditional software can turn on a light when a sensor says “something large moved.” It cannot, by itself, decide that the thing on the track is an elephant.

### AI

AI is trained on many examples. It looks for patterns, then makes a useful guess on a new case.

- Face unlock guesses “this is the owner.”
- A spam filter guesses “this mail is junk.”
- A camera near a track can guess “this shape and walk is an elephant.”

The guess can be wrong. A language model can make the same kind of mistake. That is covered with hallucinations later in these notes.

| | Traditional software | AI |
| --- | --- | --- |
| How it is built | A person writes the rules | A model learns patterns from examples |
| What it does with a new case | Only what the rules already cover | Makes a decision from what it has seen |
| A railway sensor | “Something moved, turn on the light” | “This looks like an elephant, warn the driver” |
| Language | Menus, keywords, fixed commands | Ordinary sentences, questions, and answers |

![Traditional software turns on a signal when something moves. AI looks at the track and warns that an elephant is there.](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/othersessions/classroomdemo/session-rise-of-llms/rules-vs-ai-decision.png?v=20260925)

---

## 2. Watch: an elephant, a camera, and a decision

🎥 [E-Eye: An AI-Based Elephant Movement Prediction Model](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/4c52f3b8-4507-47f7-86c2-326d41cb325e/1UbaIsJ3NgtZNFL0.mp4)

<iframe
    width="640"
    height="360"
    src="https://coding-platform.s3.amazonaws.com/dev/lms/tickets/4c52f3b8-4507-47f7-86c2-326d41cb325e/1UbaIsJ3NgtZNFL0.mp4"
    title="E-Eye: AI-Based Elephant Movement Prediction"
    frameborder="0"
    allowfullscreen
></iframe>

### Think and reflect

What can this system do that a fixed program cannot?

- Older software could flash a warning or switch on a hazard light when a sensor fired. It still could not decide whether an elephant was actually there.
- The AI system looks at features such as **size, shape, the way the animal walks**, and **thermal or movement patterns**.
- When the pattern matches an elephant near the track, it can **warn train drivers** without a person watching every camera.
- The same idea shows up far beyond railways: recognise a face, a tumour on a scan, a spoken sentence, or the next word in a message.

The same kind of decision later moved from **seeing an animal** to **reading and writing language**, and then to assistants that can see a room and talk about it.

---

## 3. A short history, only the turns that lead to language

AI is older than ChatGPT. Most of that history is a search for machines that can do one hard human task at a time. Language is the task that changed daily life.

| Year | What happened | Why it matters |
| --- | --- | --- |
| 1950 | Alan Turing asks, “Can machines think?” | The question is older than the products. |
| 1956 | John McCarthy coins the term **artificial intelligence** | The field gets a name. |
| 1997 | IBM **Deep Blue** beats chess champion Garry Kasparov | A machine can beat a person at a closed game with rules and search. It does not understand a conversation. |
| 2011 | IBM **Watson** wins *Jeopardy!*; Apple releases **Siri** | Language starts to show up in products: quiz clues, and a voice you can talk to. The answers are still narrow. |
| 2017 | The **Transformer** paper, *Attention Is All You Need* | The architecture behind almost every modern LLM. A model can look across a whole sentence and decide which words matter to each other. |
| 2018 | **GPT-1** (OpenAI) and **BERT** (Google) | Language models become a research method, not a demo. |
| 2020 | **GPT-3** | A single large model can write, answer, and follow many tasks it was not separately programmed for. |
| 2022 | **ChatGPT** opens to the public (30 November) | Ordinary people can talk to an LLM. This is the start of the rise most of us felt. |
| 2023 | **GPT-4**, **Claude**, **Llama**, **Gemini** | One lab’s chatbot becomes a race. Models get stronger, and some can look at images. |
| 2024 | **GPT-4o** and Google’s **Project Astra** | Models that handle text, voice, and sight in one conversation. Astra points at an assistant that sees what you see. |
| 2025 | **GPT-5** | Fast answers and slower “thinking” answers sit in one system. |
| 2026 | **GPT-5.6**, **GPT-Live**, **Gemini Live** and **Gemini 3.8 Live** | Today’s models write, reason, see, talk in real time, and begin to use tools. |

In short:

1. For decades, AI mostly won at **closed tasks** (chess, a quiz, a voice command).
2. From 2017 onward, the winning idea for language was: **train a huge model to predict what comes next**, then teach it to be a helpful conversational partner.

### 1997 — Deep Blue wins at chess

IBM’s **Deep Blue** beat world chess champion Garry Kasparov in New York in May 1997. The score was 3.5–2.5. It was the first computer to defeat a reigning world champion under standard tournament time controls.

Deep Blue searched millions of chess positions and followed rules of the game. It did not understand a conversation.

![IBM Deep Blue, the RS/6000 SP computer that defeated Garry Kasparov in 1997. Photograph by James the photographer at the Computer History Museum, CC BY 2.0.](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/othersessions/classroomdemo/session-rise-of-llms/deep-blue-computer.jpg?v=20260925)

🎥 [Deep Blue vs Kasparov: How a computer beat the best chess player in the world (BBC News)](https://www.youtube.com/watch?v=KF6sLCeBj0s)

### 2011 — Watson wins at Jeopardy!

In February 2011, IBM’s **Watson** beat Jeopardy! champions Ken Jennings and Brad Rutter. The clues were written in ordinary language, with puns and odd phrasing. Watson had to understand the clue and give an answer fast enough to buzz in.

This is an early public face of **NLP**. The answers were still for one quiz show. Asking Watson an open question the way people ask ChatGPT was not yet the product.

![Watson’s Jeopardy! contestant podium, shown on a stage replica at the Computer History Museum. Photograph by Atomic Taco, CC BY-SA 2.0.](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/othersessions/classroomdemo/session-rise-of-llms/watson-jeopardy-stage.jpg?v=20260925)

🎥 [IBM Watson: Final Jeopardy! and the Future of Watson](https://www.youtube.com/watch?v=lI-M7O_bRNg)

---

## 4. A few words behind an LLM

These words sit around LLMs. The definitions below are enough to follow the rest of the notes.

- **Machine learning (ML):** the computer learns a pattern from data, instead of a programmer writing every rule. Spam detection and face unlock are machine learning.
- **Neural network:** one family of machine-learning methods, loosely inspired by connected cells in the brain. Many small units pass signals forward and adjust during training.
- **Deep learning:** neural networks with many layers. Those extra layers are what made speech, images, and long text practical.
- **Natural language processing (NLP):** teaching a computer to work with the language people already speak and write.

### NLP is why anyone can use AI

Older software asked you to learn *its* language: a menu, a button, a keyword, or a line of code. If you did not know the command, you could not use the tool. That kept a lot of AI inside labs and specialist apps. Face unlock is powerful, and you still cannot ask it a question.

**NLP** is the field that turns that around. The computer takes a normal sentence — a question, a request, a paragraph — and does something useful with it.

For years, NLP was narrow. A phone could follow “set a timer for 5 minutes” and fail on almost anything else. Large language models are NLP that finally became broad enough for everyday talk. You type or speak the way you would to a person. You do not learn a command list first.

**AI stopped being a special screen for a special task, and became something anyone can open and talk to.** ChatGPT, Gemini, and Claude are that door.

![Old software asks for a command code. NLP takes a normal sentence, so anyone can use AI.](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/othersessions/classroomdemo/session-rise-of-llms/nlp-ordinary-language.png?v=20260925)

An LLM is a deep-learning model trained on a very large amount of text (and, in newer systems, images and audio too). It is the NLP system behind those products.

---

## 5. What a large language model is

**Large language model (LLM):** a model trained on an enormous amount of text. You ask a question in ordinary language, and it answers in sentences. You give it a draft, and it rewrites it.

Nobody wrote a separate rule for each question. The model has one habit, the same habit as the word suggestions on a phone keyboard.

You type `I am`. The keyboard offers `going`, `fine`, `sorry`. It is guessing the next word from sentences it has seen before.

An LLM does that for a whole reply. It writes **one word, then asks itself what should come next**, and repeats until the answer is finished.

### Watch one sentence get written

Start with what the person typed:

`When I hear rain on my roof, I`

The model does not jump to a full sentence. It only chooses the **next word**. From text it was trained on, rain on a roof often leads to someone doing something indoors. Its top guesses might look like this:

| Next word | How strongly the model leans that way |
| --- | --- |
| cook | strongest guess |
| warm | a close second |
| cower | possible, less common |
| nap | possible, less common |
| relax | possible, less common |

These are the favourites, not the full list. Thousands of other words are possible, so even the winner is only a slice of the total. A diagram of this moment often shows small percentages such as 9.4% for “cook soup” and 5.2% for “warm up a kettle.” **Cook** ranks ahead of the others.

Suppose it picks **cook**. The sentence is now:

`When I hear rain on my roof, I cook`

It runs the same guess again. After “cook,” **soup** is a strong next word. The sentence becomes:

`When I hear rain on my roof, I cook soup`

Then the same loop continues:

`… cook soup` → `in` → `my` → `kitchen`

```text
When I hear rain on my roof, I
        → cook
        → soup
        → in
        → my
        → kitchen.
```

A long answer is this loop hundreds of times. A question, a poem, and a block of code are all produced the same way: **one next piece, then the next.**

![The model starts from “When I hear rain on my roof, I”, picks cook as the strongest next word, then grows the sentence one piece at a time.](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/othersessions/classroomdemo/session-rise-of-llms/llm-next-word.png?v=20260925)

![How LLMs work](https://coding-platform.s3.amazonaws.com/dev/lms/tickets/5db4251f-5896-48b7-bded-44385d69191f/PAEksixScuNQjfCn.png)

### Temperature: which guess it is allowed to pick

**Temperature** decides whether the model must take the top guess or may take a lower one.

- **Low temperature.** Stay with the strongest guess. Here, that is **cook**, then **soup**. Ask the same question again and the reply stays close to the same words. Use this when you want a steady, factual answer.
- **High temperature.** The top guess can lose to a weaker one. The sentence might become “warm up a kettle” or something less ordinary. Ask again and the wording changes. Use this when you want a more surprising line.

Same as a phone keyboard. The first suggestion is the safe one. A higher temperature is the model sometimes tapping a suggestion further down the list.

### Two words you will see next to this idea

- **Token.** The “word” in the loop is often a chunk, not a whole dictionary word. `"ChatGPT"` might be split into `Chat`, `G`, `PT`. The model still adds one chunk at a time.
- **Hallucination.** The reply can be fluent and still be wrong. The model is continuing a pattern, not checking a fact it is sure of. “Albert Einstein invented the light bulb” sounds confident and is false. Check anything that matters.

GPT means **Generative Pre-trained Transformer**: this kind of model, trained first to guess the next chunk of text, then shaped so people can talk to it.

---

## 6. The rise, in six chapters

### Chapter 1 — The Transformer (2017)

Before 2017, language systems were slow to read a long sentence and easy to lose the thread. The Transformer let a model weigh every word against every other word in one pass. That paper is the common ancestor of GPT, BERT, Gemini, Claude, and Llama.

**Transformer** is the design that made large language models possible.

### Chapter 2 — Research models (2018–2021)

| Model | When | What changed |
| --- | --- | --- |
| GPT-1 | June 2018 | OpenAI shows the recipe: pre-train a Transformer on books, then adapt it to tasks. |
| BERT | October 2018 | Google’s model reads a sentence in both directions. It later sits behind much of Google Search. |
| GPT-2 | February 2019 | Text becomes coherent enough that OpenAI releases it in stages, worried about misuse. About 1.5 billion parameters. |
| GPT-3 | 2020 | A large jump in scale. One model writes, answers, and translates with little task-specific training. It is offered to developers through an API, not yet as a public chat app. |
| GitHub Copilot | 2021 | The same idea, pointed at code. A comment in plain language starts to become a program. |

**Parameters** are the numbers the model adjusts while training. They are its stored patterns. GPT-3’s lesson for the public was blunt: more scale, on this recipe, produced abilities nobody had written as separate features.

These models were still mostly for researchers and developers. A person on a phone did not “talk to GPT-3.”

### Chapter 3 — ChatGPT, and the public rise (2022–2023)

On **30 November 2022**, OpenAI released **ChatGPT** as a free research preview, built on the GPT-3.5 series. The model underneath was a cousin of GPT-3. The product was new: a box where you type in ordinary language and a reply comes back.

That is the moment the rise of LLMs left the lab.

What followed in 2023 turned one chatbot into an industry:

| When | What arrived | Why people noticed |
| --- | --- | --- |
| February 2023 | ChatGPT Plus | A paid, faster tier. AI becomes a subscription, like music or video. |
| March 2023 | **GPT-4** | A clear step up in reasoning. It can take an image as input, not only text. Microsoft’s new Bing (later Copilot) runs on it. |
| March 2023 | **Claude** (Anthropic) | A second serious conversational model, built with a strong focus on safer replies. |
| 2023 | **Llama** (Meta) | A strong model family that others can download and build on. The rise is no longer one company’s API. |
| September 2023 | ChatGPT can see, hear, and speak | You can show it a photo and talk to it, not only type. |
| November 2023 | GPT-4 Turbo, custom GPTs | Longer documents, and a way for people to wrap a model in a small specialist assistant. |
| December 2023 | **Gemini** (Google) | Google’s multimodal family, the successor line to Bard. Text, images, audio, and code in one model family. |

By the end of 2023, “LLM” meant a product you could open, not a paper you could cite.

**Generative AI** means models that **create**: a paragraph, a picture, a clip, a piece of code. An LLM is the text engine inside that larger wave. Image models (DALL·E, and later native image generation inside GPT) and video models (Sora) sit beside it. They share the “learn a pattern, then produce a new example” idea. The language models are what people talk to.

### Chapter 4 — Models that see and hear (2024), including Project Astra

2024 is the year the chat box starts to share your senses.

**13 May 2024 — GPT-4o (“omni”).**  
One model takes in and produces text, audio, and images. Voice stops feeling like “speech-to-text, then a text model, then text-to-speech.” You can interrupt it. It can talk about what it sees. A smaller **GPT-4o mini** follows in July, cheap enough to replace older chat models for everyday use.

**May 2024 — Project Astra (Google DeepMind).**  
Shown at Google I/O as a research prototype of a **universal assistant**:

- You point a phone camera at the world, or later wear prototype glasses.
- You talk naturally. It talks back, without a stiff “wake word, then wait.”
- It uses what it sees: a screen, a room, an object, a diagram.
- It remembers useful details across the conversation.
- It can call tools such as Search, Maps, Gmail, and Calendar, and highlight the thing on screen it means.

Astra is not “another chatbot tab.” It is the bet that an LLM should sit **in the room with you**, seeing what you see.

Through 2025, pieces of that prototype became something millions of people can open: **Gemini Live** (camera, screen sharing, spoken conversation) on Android and iOS. The fuller Astra experience — glasses, deeper memory, acting on your behalf — stayed a prototype with trusted testers, including work with blind and low-vision users who need a visual interpreter.

Same year, a second shift starts inside OpenAI. In **September 2024**, the **o1** models are trained to spend time thinking before they answer. Hard maths and multi-step problems get a different kind of model, not just a bigger chat model.

### Chapter 5 — From a chat reply to a system that can act (2025)

The useful question stops being “which chatbot writes the nicest paragraph?” It becomes “can the model decide it should slow down, look something up, or use a tool?”

| When | Step | What it means |
| --- | --- | --- |
| Early 2025 | OpenAI **Operator**, **deep research**, then a ChatGPT **agent** | The model can browse, research across steps, and use a computer on your behalf. |
| April 2025 | **o3** | Reasoning models that use tools while they think, not only after they finish a paragraph. |
| 7 August 2025 | **GPT-5** | The fast chat line and the slow reasoning line join. One system chooses when to answer quickly and when to think longer. Sizes such as GPT-5 mini and GPT-5 nano cover cheaper, faster jobs. |
| 2025 | Gemini 2.5, Claude 4, Llama 4 | Google, Anthropic, and Meta keep the same race: longer context, stronger reasoning, agents, and multimodal input. |

With GPT-5, “the chat model” and “the thinking model” sit in one product. The product routes the question.

### Chapter 6 — Today (2026): GPT-5.6 and Astra’s live assistants

The rise did not stop at GPT-5. Through late 2025 and 2026 the version numbers moved quickly: GPT-5.1, GPT-5.2, GPT-5.4, GPT-5.5, then **GPT-5.6** on **9 July 2026**.

The models in use now:

**GPT-5.6 (OpenAI), July 2026.**  
The current frontier GPT generation, in three tiers:

- **Sol** — the strongest tier, for the hardest work
- **Terra** — a balance of ability and cost
- **Luna** — the fast, cheaper tier

The same generation is built to call tools, coordinate more than one agent, and sit inside ChatGPT, Codex (the coding agent), and the API. In July 2026 OpenAI also shipped **GPT-Live**, voice models that can listen and speak at the same time, replacing the older Advanced Voice Mode.

**Project Astra, carried into Gemini Live.**  
Astra’s camera understanding, screen sharing, and spoken dialogue are in the Gemini app people already use. On **15 September 2026** Google released **Gemini 3.8 Live** and **Gemini 3.8 Live Extended Thinking**: live conversation with real-time sight and language, plus a mode that keeps talking with you while it reasons through a harder task and uses tools in the background. Glasses and the full trusted-tester Astra prototype remain the further step, not the everyday app.

Put the two side by side:

| | GPT line, today | Project Astra / Gemini Live, today |
| --- | --- | --- |
| Where you meet it | ChatGPT, Codex, API, desktop app | Gemini app, Search Live, and the Astra prototype |
| What “now” feels like | A strong writer and reasoner that can use tools, code, and live voice (GPT-5.6, GPT-Live) | A conversation about what the camera or the screen is showing, with memory and tool use (Astra → Gemini Live → Gemini 3.8 Live) |
| The shared direction | An assistant that does not only reply. It sees, talks, and takes a next step. | The same direction, from the prototype that made “point the camera and talk” famous. |

Other families sit in the same present: Anthropic’s Claude (through the Claude 4 and later lines), Meta’s Llama, and open models people can run themselves. GPT and Astra show the arc most clearly: **text predictor → public chatbot → model that sees and hears → model that acts.**

---

## 7. How this connects back to the elephant

The elephant system and GPT-5.6 look different. The decision is the same kind of move.

| Elephant video | An LLM today |
| --- | --- |
| Many examples of animals, shapes, and movement | Enormous examples of language, and now images and audio |
| A guess: “this is an elephant near the track” | A guess: the next word, the next step, the next action |
| A warning goes out without a person staring at the camera | A draft, a search, a booking, or a code change can start from one sentence |
| A wrong guess is dangerous on a railway | A wrong guess is a hallucination in an essay, a medical note, or a piece of code |

Traditional software would need a new rule for every animal, every sentence, and every task. The LLM bet is the opposite: learn language at a huge scale, then point that skill at whatever the person asks.

That is why the rise matters for anyone who builds software or simply uses it. The interface is no longer only buttons. It is a sentence, a photo, a camera pointed at a room, and — with Astra and with agent features in GPT — a request that the system should go and do the next step.

---

## 8. Key points

1. **Traditional software follows rules. AI makes a decision from patterns.** Face unlock and the elephant video are the proof.
2. **NLP lets anyone use AI.** You do not learn the software’s commands. You ask in ordinary language, and an LLM answers.
3. **An LLM is a next-word predictor at a huge scale**, shaped so the continuation is a useful answer.
4. **The public rise starts on 30 November 2022**, with ChatGPT. Everything before that is the research path: Transformer (2017), GPT-1 (2018), GPT-3 (2020).
5. **2023 is the race** (GPT-4, Claude, Llama, Gemini). **2024 is senses** (GPT-4o and Project Astra). **2025 is thinking and action** (GPT-5). **2026 is the assistant you can talk to while it looks and works** (GPT-5.6, GPT-Live, Gemini 3.8 Live).
6. **Fluent is not the same as true.** Check the answer when the fact matters.

---

## Sources

Dates follow public announcements, so a rollout to every country or every plan can be a few days later.

- OpenAI model history: [Introducing GPT-5](https://openai.com/index/introducing-gpt-5/), [Model Release Notes](https://help.openai.com/en/articles/9624314-model-release-notes)
- Google: [Project Astra](https://deepmind.google/models/project-astra/), [Gemini as a universal assistant (I/O 2025)](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-universal-ai-assistant/), [Gemini 3.8 Live (15 September 2026)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/)
