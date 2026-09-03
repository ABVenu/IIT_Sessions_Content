## Iteration 1 QC Report

### Content Coverage
- Rating (1 to 5): **5**
- All five metadata subtopics covered: need for the internet to connect users, servers, and services; demerit of isolated systems; request–response role of the internet; DNS name-to-address mapping; HTTPS for secure communication. Browser sequence included to match the lecture title.

### Creativity
- Rating (1 to 5): **4**
- Indian-relatable analogies (IRCTC, UPI, kirana register, Amma in contacts, railway enquiry, sealed envelope). Student-facing activities present.
- Gaps: few comparison tables, thin browser-internals depth (URL parts, many requests per page, cookies), overlapping delay/path explanation.

### Structural Adherence
- Rating (1 to 5): **4**
- Started with `# Masterclass: Internet & Browser Internals`. Definition / Simple Words / Real-Life Example pattern present. Connecting sentences present. Key Takeaways and terminology table present. No code, as required for this masterclass; activities used instead.
- Issues found: first draft was **422 lines** (under the 480–500 cap). Informal line "Keep it human." Isolated-system definition used the internal phrase "(in this session)."

### No Logical Mistakes
- True
- DNS presented as lookup, not as the website itself. HTTPS split into encryption vs identity. Isolated systems allowed where offline is the correct design.

### No Presentation Mistakes
- False
- Notes under the stated length cap. One informal instruction line. At least one paragraph later exceeded the 3-sentence rule after expansion started.

### No Previous Session Number References
- True
- Uses "previous masterclass" and "later work" only.

### No Metadata / Internal Reference in Student Notes
- True
- No duration, no "keep it lite", no session IDs in headings. The phrase "(in this session)" inside a definition was treated as internal tone and removed in revision.

### Actions taken after Iteration 1
- Expanded local-vs-network table, ISP definition, delay vs loss vs busy server, DNS resolver, wrong-DNS risk, HTTPS can/cannot table, URL parts, multi-request page load, cookies, scheme term.
- Replaced "Keep it human." Removed "(in this session)." Split 3-sentence-rule violations. Removed undefined "firewall/port" wording.
- Brought length into the 480–500 range.

---

## Iteration 2 QC Report (post revision)

### Content Coverage
- Rating (1 to 5): **5**
- All metadata topics remain fully covered with definitions, need/logic/doubts, tables, and student-facing activities. Title topic (browser internals) is taught as the sequence that runs DNS, HTTPS, request, response, render, cache, and cookies.

### Creativity
- Rating (1 to 5): **5**
- Contact-list and postcard/envelope analogies, isolated-vs-connected table, HTTPS can/cannot table, URL anatomy table, six-word address-bar activity, seven-step path trace, password-safety cases. No code, by design.

### Structural Adherence
- Rating (1 to 5): **5**
- Clean `# Masterclass: Internet & Browser Internals` start. No metadata in headings. 3-sentence rule restored. Bold terms and bullets throughout. Official Definition / In Simple Words / Real-Life Example on core terms. Connecting sentences between sections. Student-facing activities (not instructor prompts). Key Takeaways (5 bullets + future link). Terminology table at the end. Notes length **483 lines** (within 480–500).

### No Logical Mistakes
- True
- Request–response is the conversation; internet is the carrier. Packets need IP addresses; DNS supplies them. Failed DNS blocks the start; wrong DNS can send traffic to the wrong machine. HTTPS protects the pipe and checks the name; it does not prove the business is honest. Cache can show a stale page without the path being broken.

### No Presentation Mistakes
- True
- No image placeholders yet (images deferred until notes are approved). Headings are direct. No code blocks. Activities are written to the student.

### No Previous Session Number References
- True
- Uses "previous masterclass" and "later work" only.

### No Metadata / Internal Reference in Student Notes
- True
- No duration, no "keep it lite", no session IDs, no internal dial language.
