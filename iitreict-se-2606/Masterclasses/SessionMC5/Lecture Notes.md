# Masterclass: Understanding Libraries & Frameworks

You have been writing programs by hand. Loops, functions, pages, clicks, and data requests were **direct implementation**: you decided each step and typed it.

That skill is the foundation of coding. A real product still needs it for the parts that are unique to the idea.

A railway booking service, a college result portal, or a UPI screen is not one student file typed from a blank page. Most of the working parts were **already built by other people**. Your job grows into knowing those parts, choosing among them, and writing only what the product still lacks.

This lesson names that landscape in plain language: **module**, **package**, **library**, **framework**, **software**, **system**, and **design**.

![Build every feature from scratch versus write your unique rule and reuse modules, packages, and libraries — direct implementation is training, products lean on shared code](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitreict-se-2606/masterclasses/sessionmc5/sessionmc5-01-scratch-vs-reuse.png?v=20261013)

## What You Will Learn in This Lesson

In earlier lessons you implemented behaviour yourself. You organised code into files, installed Python tools, built pages, updated the screen on clicks, and called remote data.

This lesson builds the map those lessons were walking on. Upcoming lessons build screens in a component style, then shape server programs with a backend framework.

In this lesson, you will learn:

- The **demerit** of writing every feature **from scratch** in a real product
- Why teams need **reusable code** to build **faster** and **more consistently**
- What a **module** is, and what a **package** is
- What a **library** is, and what a **framework** is
- When a **library is enough**, and when a **framework is needed**
- Why **component** tools such as **React** became important for user interfaces
- How **software**, a **system**, and **design** sit above those names
- How a developer **chooses** what to write and what to adopt

By the end, you will label a tool by who stays in control, and you will explain a product as software inside a system shaped by design.

---

## What Direct Implementation Trained You to Do

**Direct implementation** means you write the steps of a feature yourself, in the order the computer should follow.

- **Official Definition:** **Implementation** is the act of turning a decided behaviour into working code.
- **In Simple Words:** You do not only name the idea. You write the instructions that make it happen.
- **Real-Life Example:** Knowing “the canteen needs change” is the idea. Counting the notes and coins yourself is the implementation.

Your earlier work was this practice, on purpose.

- You stored values, branched with conditions, repeated work with loops, and named jobs as **functions**.
- You arranged data in lists and dictionaries, and you wrote simple search and sort steps yourself.
- You split a script across **files**, **imported** one file from another, and installed extra Python tools.
- You structured a page, made it respond to clicks, and showed data that came from another computer.

**Need:** If you skip this layer, every library looks like magic and every bug looks like a mystery.

**Logic:** Employers still expect you to trace a failing feature. That skill comes from having built small features yourself.

**Common doubt:** “Was the hand-written sort a waste if products reuse code?” It was training. In a product you call a trusted sort because you already know what sorting is for.

Once the steps are yours, the next question is which steps the world has already solved.

---

## The Demerit of Writing Every Feature from Scratch

**From scratch** means you build a feature as if nobody has shipped that solution before.

- **Official Definition:** **Building from scratch** means implementing a capability with only the language basics, without adopting an existing, trusted solution for that capability.
- **In Simple Words:** You mill the flour, sew the bag, and bake the bread, even when a good loaf is already sold.
- **Real-Life Example:** A result portal that re-codes leap years, password storage, and a private error style on every screen.

- **Time goes to plumbing.** Weeks go to calendars and pop-ups while the college rule is still unbuilt.
- **Solved problems come back with bugs.** Dates, money rounding, and sorting edges already have tested answers.
- **Security weakens.** Login, payment, and file upload fail in ways a homemade approach hides.
- **The product looks uneven, and repair becomes personal.** One teammate uses red text, another uses an alert, and only the author can find the click logic.
- **The same work is typed twice.** A header or a server call is copied, then fixed in only one place. The next developer expected a familiar tool.

**Need:** Speed and consistency are why teams adopt shared code. Reuse moves thinking to the product rule, the boundaries, and the choice of tool.

**Common doubt:** “Is reuse the same as copying a friend’s file into my project?” Copying a file you do not understand is still a private dialect. Reuse means adopting a maintained solution and learning the contract it offers.

**Activity — Scratch or reuse:**  
Mark **Write** or **Reuse** for a result portal: two marks added on the page, a leap day, password storage, one heading colour, one header style on twenty screens, sorting ten names.

Suggested reading: Write, Reuse, Reuse, Write, Reuse, Reuse. Use the language’s sort unless the goal is to study sorting itself.

Those demerits are about features. The next headings name the units people use when they stop rebuilding every feature alone.

---

## A Ladder You Can Keep in One Notebook

Read the ladder from the small unit toward the wider decision. Steps 1 to 7 widen the unit you are naming. **Design** is the choice you make at every step, not a bigger box around the system.

| Step | Name | The promise in one line |
|---|---|---|
| 1 | **Function** | One job inside your file, with a name you chose |
| 2 | **Module** | One importable file of related jobs |
| 3 | **Package** | A named, versioned bundle you can install |
| 4 | **Library** | Ready code **you call** while you keep the flow |
| 5 | **Framework** | A skeleton that **calls your code** and keeps the flow |
| 6 | **Software** | The programs and data that perform a job |
| 7 | **System** | Software plus machines, people, rules, and other software |
| 8 | **Design** | The decisions about parts, duties, and trade-offs |

![Terminology ladder from function and module through package, library, and framework to software and system — design is the choice at every step, and libraries versus frameworks differ by who calls whom](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitreict-se-2606/masterclasses/sessionmc5/sessionmc5-02-terminology-ladder.png?v=20261013)

**Need:** For a module, package, library, or framework, ask what the **unit** is and **who calls whom**. Software, system, and design keep those names and widen the zoom.

You already used the first rungs when you named a function and imported another file. The next heading freezes what that file actually is.

---

## Modules: One File with a Clear Job

A **module** is the first unit that lets a program grow beyond a single script.

- **Official Definition:** A **module** is an importable unit of code, usually one file, that groups related names so other code can use them.
- **In Simple Words:** One notebook for one subject. Other notebooks can refer to it by name.
- **Real-Life Example:** A file that only handles marks calculations, imported by the file that prints the result page.

A module gives related functions a home and a public boundary, so two people can own two files. You already moved from one long script to a small multi-file program.

An **import** lets one file use names from another. A **namespace** keeps those names apart, so two modules may each have a function called `format`.

![Module import inside your project versus a versioned third-party package installed with pip or npm — team files, standard library, and installable bundles](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitreict-se-2606/masterclasses/sessionmc5/sessionmc5-04-module-and-package.png?v=20261013)

**Need:** Without modules, a product becomes one endless page. Every fix risks an unrelated feature.

**Logic:** A module is still **your** team’s code inside the project. It is reuse inside the project. The whole industry does not share that file until you publish it.

**Common doubt:** “Is every file a module?” A file is a module when other code is meant to import it. A scratch file you only run is a script. The browser’s `document` is a **platform** name you call, not a file you ship.

**Activity — File or module:**  
Write **Script** or **Module**: `result.py` imported by `main.py`, `try_once.py` never imported, a JavaScript file that exists only to be imported.

Suggested reading: Module, Script, Module.

A module travels with your project. A package is how code travels **between** projects and people.

---

## Packages: The Box You Install

A **package** is the unit of **distribution**. It is how someone else’s modules arrive on your machine with a name and a version.

- **Official Definition:** A **package** is a versioned, installable bundle of software, usually modules plus metadata such as name, version, and dependencies.
- **In Simple Words:** A sealed kit from the shop. The label says what is inside and which edition you bought.
- **Real-Life Example:** The kit your project installed with a package tool, listed so a teammate can install the same edition.

Words that travel with packages:

- **Official Definition:** A **package manager** is the tool that finds, installs, updates, and removes packages.
- **In Simple Words:** The shop clerk for code. Python projects often use **pip**. JavaScript projects often use **npm**.
- **Real-Life Example:** You asked the clerk for a named kit, and the project remembered that kit for the next machine.

- **Official Definition:** A **dependency** is another package your project needs in order to work.
- **In Simple Words:** Your kit needs a battery sold separately. That battery is a dependency.
- **Real-Life Example:** A chart package that itself needs a smaller maths package.

- **Official Definition:** A **version** is a numbered release of a package, identifying one snapshot of its behaviour.
- **In Simple Words:** The edition on the label, so the team shares one snapshot.
- **Real-Life Example:** Two laptops install edition 2, so a fix on one laptop matches the other.

Two families sit beside packages:

- A **standard library** ships with the language. Python’s JSON tools live there. You import them, and you usually do not install them.
- A **third-party** package is written by others and installed into the project.

**Need:** Teams pin versions so a working laptop still matches the next laptop.

**Logic:** A package is a **box**. The box may hold a library, a framework, or a terminal tool. The box is a different idea from the job inside it.

**Common doubt:** “In Python, a folder of modules is also called a package.” There, package means a **folder you can import**. With pip, package means the **installable release**. A coursework file becomes that release only after it has a name, a version, and metadata.

**Activity — Box or contents:**  
Label **Module**, **Package**, or **Package manager**: one imported Python file, pip, a versioned release, npm.

Suggested reading: Module, Package manager, Package, Package manager.

The box is now on disk. The next split is the important one for products: does **your code call the tool**, or does **the tool call your code**?

---

## Libraries: You Keep the Steering

A **library** is reusable code that does a defined job when **your program asks**.

- **Official Definition:** A **library** is a collection of reusable code that your program calls to perform specific tasks, while your program remains in control of the overall flow.
- **In Simple Words:** A toolbox. You pick up the hammer when you need it. The hammer does not plan your day.
- **Real-Life Example:** A date library that answers “is this a real calendar date?” while your page still decides what happens next.

How you recognise a library:

- You **start** the program, decide the order, and **call** only the function you need.
- Sorting, JSON, and similar helpers often come from the **standard library**.
- Selecting an element or fetching data is a **platform API** you call while you still own the page.
- A chart or calendar package is a library when one job changes and the story of the app stays yours.

**Need:** Libraries remove specialised jobs so every project does not re-implement leap years or low-level drawing.

**Logic:** The contract is small. You learn the calls you use, and you keep the shape of the product.

**Common doubt:** “Is a library always downloaded?” The standard library and browser APIs are libraries in spirit. A download is the extra case.

Importing only brings names in. Who **leads the flow** is the next test.

Your code leading the flow is the library case. Many products eventually need the opposite bargain.

---

## Frameworks: The Tool Keeps the Steering

A **framework** is reusable structure that decides the shape of the work and **calls your code** at the right moments.

- **Official Definition:** A **framework** is a reusable skeleton of a program that defines architecture and control flow, and invokes your code to fill in the product-specific behaviour.
- **In Simple Words:** A school timetable. The bell decides when you enter class. You bring the homework the timetable cannot invent.
- **Real-Life Example:** A web framework that receives each browser request, then calls **your** function for “show this student’s marks.”

This reversal has a standard name.

- **Official Definition:** **Inversion of control** means the framework decides when your code runs, instead of your code deciding when the framework runs.
- **In Simple Words:** The tool calls you. You do not call the tool for every tiny step.
- **Real-Life Example:** An exam invigilator says when to start. You do not tell the invigilator that the exam has begun.

What you still write, and what the skeleton gives:

- Your **product rule**, the words on the button, and the settings the framework left open.
- A stable **place** for each kind of work, a **lifecycle** around your rule, and one pattern for errors and screens.

**Need:** When many people touch many screens, private style costs more than one shared map.

**Common doubt:** “Does a framework replace libraries, or is it a language?” A framework often **hosts** libraries and is written **in** a language such as Python or JavaScript. The framework leads the flow. The library still does one job when called.

**Activity — Who calls whom?**  
Write **My code calls the tool** or **The tool calls my code** for a date check, a server route that runs your marks function, a sort of ten names, and a UI skeleton that refreshes a card after data changes.

Suggested reading: My code calls the tool, the tool calls my code, my code calls the tool, the tool calls my code.

That steering test is the difference between the two bargains. The next table sets them side by side.

---

## Library and Framework Side by Side

![Library versus framework — your program calls a library while you keep the flow; a framework owns the outer flow and calls your code slots (inversion of control)](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitreict-se-2606/masterclasses/sessionmc5/sessionmc5-03-library-vs-framework.png?v=20261013)

Use this table when a blog calls everything a “tech stack” and the names blur.

| Question | Library | Framework |
|---|---|---|
| Who owns the overall flow? | **Your program** | **The framework** |
| Who starts the work? | You call a function when you need it | The framework calls you at defined moments |
| How much structure arrives? | A job, or a family of jobs | Folders, lifecycle, and rules for the whole slice of the app |
| What do you write? | The story, plus calls to the tool | The pieces that fit the skeleton’s slots |
| Cost if you pick it too early | Extra dependency for a tiny job | A large map for a product that is still one page |
| Cost if you pick it too late | Copy-pasted helpers drift apart | Every teammate invents a private architecture |
| Everyday picture | Hammer in a toolbox | Franchise layout of a shop |

Boundary cases still use the same test. **React** is taught as a UI library, while teams say “framework” because its rules shape the screen. **Angular** arrives as a framework.

A page framework can wrap React. A server framework receives the request and calls your route. A date helper is library use, and a required lifecycle is framework use.

The table is the definition. The next two headings are how you choose.

---

## When a Library Is Enough

Choose a **library** when you still narrate the program and only one job is hard.

- The product has **one flow**, and the hard part is a specialty such as dates, charts, or validation.
- You use a handful of calls, and dropping the tool later touches **one area**.
- A notice page, a file-summary script, one borrowed widget, or browser coursework stays in this weight.

**Need:** A library saves a solved specialty and leaves the story in your hands. If you cannot name the tool’s job in one line, you may be adopting a skeleton.

**Common doubt:** “A serious product must start with a framework.” Correct behaviour and a clear map make a product serious. A one-screen tool can be a small program plus a library.

When the **map itself** is the problem, the library no longer covers the need.

---

## When a Framework Is Needed

Choose a **framework** when product **structure** would otherwise be reinvented every week.

- **Many screens** or **routes** must share loading, errors, and navigation.
- Several people add features at once, and newcomers need one predictable place to work.
- Later features get faster and fail in one understandable way. The first days are slower, and edition upgrades become your duty.

**Need:** A framework should **surround** the unique rule, such as who may download a marksheet. The rule remains your implementation.

**Common doubt:** “Will the framework write the product?” It writes the **shape**. Marks policy and the words on the button remain yours.

**Activity — Pick the weight:**  
Write **Library** or **Framework**: one calendar widget, twenty shared admin screens, a one-file JSON summary script, five developers adding pages all year, leap-year checks.

Suggested reading: Library, Framework, Library, Framework, Library.

Changing screens are where you meet this choice next, because updating a page by hand is still fresh.

---

## Why Component Tools Such as React Became Important

Earlier interface work selected an element, changed its text, and attached a click. That **manual screen repair** is honest practice. It becomes a demerit when one screen has many living parts.

- The list in memory can say three items while the page still shows two.
- One filter must update a list, a count, an empty message, and a button.
- Teammates invent private repair styles, and a card gets copy-pasted, then fixed in only one copy.

A **component** is the unit that answered those demerits.

- **Official Definition:** A **component** is a self-contained piece of a user interface that owns the structure, presentation, and data for one part of the screen.
- **In Simple Words:** A named block, such as a result card, that you describe once and place many times.
- **Real-Life Example:** One station card on a travel app, repeated for every stop, after a search.

![Component tree with one source of truth updating related UI pieces versus manual DOM repair with tangled per-element edits — why component libraries such as React emerged](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitreict-se-2606/masterclasses/sessionmc5/sessionmc5-05-component-ui-model.png?v=20261013)

- **Official Definition:** A **component library** (and, when it also brings the app skeleton, a **component framework**) builds the interface as components and keeps the screen in step with their data.
- **In Simple Words:** You describe the cards. The tool repaints what changed.
- **Real-Life Example:** “Seats left” updates the card, the colour, and the pay button from the same facts.

These tools emerged because web products became long-lived applications. Hand updates did not stay consistent across teams. A shared block, built once, kept buttons and forms behaving the same way.

- **Official Definition:** **React** is a JavaScript library for building user interfaces from components.
- **In Simple Words:** You describe components and their data. React updates the browser view to match.
- **Real-Life Example:** A todo row, a counter, and a filter bar as three components.

Read React with the steering test.

- React is a **library** because your code creates the component tree and still chooses routing and data loading unless another tool supplies them.
- It still **shapes every screen**, which is why jobs say “React framework.” Treat it here as the UI library that introduces components.
- **Angular** arrives as a framework. **jQuery** only shortened DOM calls. Upcoming lessons use React in code.

**Need:** A changing screen needs one source of truth and a repeatable block.

**Logic:** React does not know a college grace-mark policy. You still implement that rule inside the component.

**Common doubt:** “Why pair a library with frameworks?” The **problem** is whole-screen consistency. The **tool** stays a library until a skeleton such as a page framework is wrapped around it.

**Activity — Repair or component:**  
A seat click must change seat colour, fare, and the continue button. Label the manual-repair thought and the component thought.

Suggested reading: manual repair lists each element to tweak. A component description says those three blocks reflect the selected seat, and the tool updates them.

Components are still **software**. The next step places that software inside a system, and names design as the choice of fit.

---

## Software, Systems, and Design

A file is never the whole product. These three words keep the zoom levels apart.

### Software

- **Official Definition:** **Software** is the set of programs, libraries, and related data that instruct a computer to perform tasks.
- **In Simple Words:** Instructions, plus the data that travels with them, that a computer can run.
- **Real-Life Example:** Your script, a date library, Chrome, and a booking site’s programs are all software.

Keep three splits handy.

- **Application software** is what a person uses for a job: a browser, a result portal, an editor.
- **System software**, such as an operating system, manages the machine so applications can run.
- A **library** and a **framework** are software used as building materials. The portal you ship is software made with those materials.

**Common doubt:** “Is a website software?” The programs that produce the pages are software. The full act of booking a ticket is a system.

### System

- **Official Definition:** A **system** is an organised set of parts that work together for a purpose, including programs, machines, data, networks, people, rules, and other software.
- **In Simple Words:** The whole arrangement that delivers the outcome, beyond one app icon.
- **Real-Life Example:** A train booking joins the passenger, the browser, booking software, a payment service, railway records, and staff who handle failures.

A **program** can finish a task on one machine. A **system** still depends on outside parts: power, network, another company’s API, and a human process when software stops.

Calling a remote **API** uses someone else’s running system. Importing a **library** uses someone else’s code inside your program. Both were already built, and they fail in different places.

**Need:** Call the whole path “my website,” and you will search your file while the payment partner is the part that failed.

**Logic:** System-scale design asks which software talks to which, what happens when one part is down, and who is allowed to decide.

**Common doubt:** “Is the browser inside my system?” On a web product, the user’s browser is where frontend software runs. You do not ship the browser, and the path still includes it.

### Design

- **Official Definition:** **Software design** is the set of decisions about a program’s parts, each part’s responsibility, and how the parts interact.
- **In Simple Words:** What is a module, what is borrowed, and what you will write.
- **Real-Life Example:** Marks maths live in one module, dates come from a library, and twenty screens follow one framework.

- **Official Definition:** **System design** is those decisions at product scale: which software, machines, external services, and rules keep the outcome reliable.
- **In Simple Words:** The map of the whole service, beyond one repository.
- **Real-Life Example:** Payments go to a trusted payment system, seats stay in the railway system, and your software coordinates the steps.

**Design** chooses parts and duties, including library versus framework. **Implementation** writes the behaviour you still own inside that choice.

**Need:** Implementation without design rebuilds structure by accident. Design without implementation never ships a working rule.

**Logic:** Your earlier implementation practice gives these words a memory: files, installs, pages, clicks, and API calls.

**Common doubt:** “Is design a diagram?” A diagram can record design. The decisions themselves are the design, even as a short note about a module boundary.

**Activity — Name the layer:**  
Label **Module**, **Package**, **Library**, **Framework**, **Software**, **System**, or **Design**: a grade file that is imported, a versioned release you install, a date tool you call, a skeleton that calls your request function, Chrome, passenger plus site plus payment partner plus railway records, the decision that twenty screens share one skeleton.

Suggested reading: Module, Package, Library, Framework, Software, System, Design.

These names help when they change what you pick on the next feature.

---

## How You Choose in Product Work

Write these answers before you install a tool.

- **Unique rule:** grace-mark policy is yours to implement. Leap years are a solved specialty.
- **Inside or outside:** a library joins your program. An API is another system you talk to.
- **Who leads:** you lead with a module or a library. A shared skeleton leads when you choose a framework.
- **How often:** one use can be a small library. A pattern across the product wants a shared module or a framework.
- **Trust and cost:** prefer a maintained tool for security, money, and login. Budget a framework’s slow first day on purpose.

Professionals grow in this order: implement small behaviours, group them into **modules**, install a **package** for a solved specialty, stay with **libraries** while one flow is yours, adopt a **framework** when the map must be enforced, then describe **software** inside a **system** whose **design** the next person can read.

**Common doubt:** “Must I memorise every library name?” You need the categories, the steering test, and the habit of reading what a tool promises. Names will attach as upcoming lessons use them.

**Activity — Four lines:**  
For “students download a marksheet,” write the rule you will implement, one thing you will reuse, library or framework for a single button on a page you already own, and one system outside your file.

Suggested reading: you implement who may download and what the file contains, and you reuse a trusted PDF or login check. A library fits one button on a page you own. The system includes the student, browser, server, marks store, and login service.

---

## Names That Often Get Mixed

| What people say | Accurate placement |
|---|---|
| “Python is a framework” | Python is a **language** |
| “JavaScript is a library” | JavaScript is a **language** the browser runs |
| “pip is a library” / “npm is a framework” | Both are **package managers** |
| “I imported JSON, so I used a framework” | Python’s JSON tools are a **standard-library module** |
| “`fetch` means I installed a package” | `fetch` is a **browser platform** capability |
| “A module and a package are the same” | A module is imported. A package is a **named, versioned bundle** |
| “A library calls my whole app” | A library **waits for your call**. A framework **calls you** |
| “React writes my product rules” | React updates **UI structure**. Rules stay your implementation |
| “React and Angular are the same kind” | React is a **UI library**. Angular is a **framework** |
| “The website is the system” | Site programs are **software**. The **system** includes users and partners |
| “Design means the colours” | **Design** here means structure, duties, and trade-offs |
| “Copy-paste is reuse” | Reuse adopts a **maintained contract** |
| “From scratch is more professional” | It is right for learning and for **unique rules** |

**Activity — Correct the sentence:**  
Rewrite: “We installed React with pip, so Python’s framework will call our HTML file, and that is the whole railway system.”

Suggested reading: React is a JavaScript UI library, installed with the JavaScript package manager. The railway system still includes passengers, servers, data stores, and partner services.

---

## Key Takeaways

- **Direct implementation** writes a **unique product rule**. **From scratch** is a weak default for solved work: it costs time, repeated bugs, weak security, and uneven screens.
- **Libraries** and **frameworks** exist so teams build **faster** and **more consistently**. A library is called by you. A framework calls you.
- A **module** is imported. A **package** is the versioned bundle a package manager installs.
- Use a **library** for one specialty inside your flow, and a **framework** when many screens need one map. **React** is the UI library that made **components** the normal way to build those screens.
- **Software** is programs and data. A **system** adds machines, people, rules, and other services. **Design** chooses the parts, including library versus framework.

Upcoming lessons implement interfaces in React’s component style. Later, a backend framework will receive requests and call your server code. The same steering test applies there.

One-breath summary: **write the unique rule, import a module you own, install a package you trust, call a library while you steer, adopt a framework when the map must be shared, and describe software inside a system you designed on purpose.**

**Say-aloud checks:**

- Why is a homemade password store a demerit?
- Why is pip a package manager?
- Why does a framework invert control?
- Why can React be a library and still shape every screen?
- Why is a payment partner part of the system?

If an answer is shaky, reread that heading. You are ready for component-based UI when those five answers stay short and accurate.

---

## Important Commands, Libraries, Terminologies Used

| Term | Meaning (quick revision) |
|---|---|
| **Direct implementation** | You write the steps of the behaviour yourself |
| **From scratch** | Building a capability without a trusted existing solution |
| **Module** | An importable unit, usually one file, with its own namespace |
| **Package** | A named, versioned, installable bundle |
| **Package manager** | The installer. **pip** for many Python projects, **npm** for JavaScript |
| **Dependency** | Another package your project needs |
| **Version** | The numbered edition of a package |
| **Standard library** | Modules that ship with the language |
| **Third-party package** | Software from outside the language, installed into the project |
| **Platform API** | A capability the browser or runtime gives you to call |
| **Library** | Reusable code **your program calls**; you keep the flow |
| **Framework** | A skeleton that **calls your code** and sets the flow |
| **Inversion of control** | The framework decides when your code runs |
| **Component** | One self-contained piece of the interface |
| **React** | A JavaScript **library** for component-based user interfaces |
| **Angular** | A JavaScript **framework** with a full application structure |
| **jQuery** | A DOM-call **library** from an earlier style of page repair |
| **Web framework** | Server software that receives requests and calls your route code |
| **Software** | Programs, libraries, and related data that perform tasks |
| **System** | Parts working together: software, machines, people, rules, other services |
| **API (remote)** | Someone else’s **running** system that your software talks to |
| **Software design** | Decisions about parts, duties, and how parts interact |
| **System design** | Those decisions at the scale of the whole product |
| **Unique rule** | The product behaviour only your team knows and must implement |
