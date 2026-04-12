# Pre-read: AI Agents — When Software Stops Following Only Fixed Rules

## The hook

You have already used systems that feel less like a rigid form and more like a helper: maps that reroute when traffic changes, food apps that search, compare, and checkout in one flow, or a chat that looks up *your* order instead of giving the same reply to everyone. That shift—from “press A, then B, always the same” to “understand my goal and figure out the steps”—is what this session is about. We give it a clear name—**AI agent**—and unpack **how** such systems are put together, in plain language. This matters for how products are built now and for any role where you will work with or evaluate “smart” automation.

## The problem

**What if** every tool you used only worked when reality matched a script written months ago? The moment something new happened—a train full, a job post only on LinkedIn, a user who already gave their date of birth—the system would either error out or keep asking silly questions. **What if** you also needed software to chase a goal over many steps (search, compare, call an API, confirm, message the user) without a human clicking through each micro-instruction? Ordinary “do exactly what was programmed” systems are not enough for that. The hard part is describing **what makes a system genuinely goal-driven and adaptive**, and **what can still go wrong** when one piece is weak.

## The solution preview

The “hero” of this session is the **AI agent** idea itself—not as hype, but as a **pattern**: perceive the situation, decide what to do, act, and repeat until the job is done. We will separate **agents** from **traditional** systems (think ATM vs a support flow that reasons about *your* case). Then we open the “engine room” and study **four parts** every agent leans on: **planning** (ordered steps), **reasoning** (smart choices when things change), **memory** (what to hold for now vs what to save for later), and **action** (real calls, searches, messages—not only silent thinking). We close by seeing how these fit into a single loop: **Observe → Think → Act**. This session is **concepts first**; you already know Python basics, and later you will **build** agents with code—today we build the mental map so that code has meaning.

## A simple analogy from the session

The notes compare an agent to an **efficient secretary** asked to organise a big company event. The secretary does not randomly book a caterer on impulse. They **plan** the sequence, **reason** when two venues clash with the budget, use **memory** (old notes, vendor lists, what the boss liked last year), and finally **act**—calls, emails, bookings. **Planning** is “what steps, in what order?” **Reasoning** is “given what just happened, what is the best move *now*?”—like the captain’s plan in the dressing room versus decisions on the field mid-match. That split runs through the whole class.

## In plain words

- **AI agent (simple):** Software that works toward a goal by sensing context, deciding, and doing things—without you specifying every tiny step.
- **Traditional system:** Follows fixed rules; unusual inputs often break it or get ignored.
- **Short-term memory:** What this chat or task needs *right now*—like conversation context; it goes away when the session ends.
- **Long-term memory:** Saved profile, past choices, files—things that stay across days, like data on a drive you open again later.
- **Action:** Anything that actually changes something outside—API call, search, email, even the reply text you see. Thinking alone does not deliver food or confirm an order.

If a new term appears in class, we will tie it back to ideas like these—no jargon for show.

## Questions we will crack in class

1. How do you tell **planning** (“steps before you start”) apart from **reasoning** (“best move after something unexpected”)—using examples like trains, cricket, or a sudden traffic jam on the road?
2. Why do agents need **both** short-term and long-term memory—and what goes wrong when the agent “forgets” mid-task or starts every chat from zero?
3. What is the **Observe → Think → Act** loop, why is it a **loop** and not one straight line, and where do real examples—from cancelling an order to ordering food—show each stage?

## After this session, you will be able to

- Explain what an **AI agent** is and how it differs from a **traditional** system, with examples you could use in an interview or team discussion.
- Name and describe the **four core components**—planning, reasoning, memory, action—and connect them to the **secretary** and other stories from the notes.
- Contrast **short-term** vs **long-term** memory and why each matters for useful, personalised behaviour.
- Walk through the **Observe → Think → Act** cycle and recognise it in walkthroughs like food ordering or job applications.
- Spot **common failure modes**—bad plan order, lost context, wrong priority in reasoning, shaky action—and say why agent mistakes can hurt more than a wrong static-page answer.

Bring your curiosity: we are setting the foundation for the agent-style systems you will soon start shaping in Python.
