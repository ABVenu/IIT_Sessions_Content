# Masterclass: How Computers Work & Operating Systems

## What You Will Learn in This Session

In previous lessons you started writing Python programs — creating variables, printing output, and running simple calculations. Your programs worked, but the computer itself stayed a mystery. You typed code, clicked Run, and something happened on screen. What was going on inside the machine? Why do apps sometimes slow down, freeze, or crash even when your logic looks correct?

In this masterclass, you will open the lid on that mystery. You will learn:

- Why treating a computer as a **black box** leads to confusion when things go wrong.
- What the **CPU**, **RAM (memory)**, and **storage** actually do when your program runs.
- How the **Operating System (OS)** manages programs, users, and resources behind the scenes.
- What a **process** is, why every running program gets a unique **Process ID (PID)**, and why programs sometimes "wait" instead of running.
- How the **file system** organizes your code, data, and documents — and why you sometimes get "permission denied" errors.

By the end, you will have a mental model of the machine that makes debugging, performance thinking, and future programming topics much easier to understand.

---

## Why Programmers Need to Understand the Machine

Before we look at individual parts, let us answer a simple question: why should a programmer care about hardware and operating systems at all?

### The Black Box Problem

- **Official Definition:** A **black box** is a system whose internal workings are hidden — you only see what goes in and what comes out, not how it works inside.
- **In Simple Words:** Treating your computer as a black box means you press a button and hope for the best, without understanding what happens between your click and the result.
- **Real-Life Example:** Imagine using an ATM. You insert your card, enter the PIN, and cash comes out. If the ATM suddenly says "Transaction Failed," you have no idea whether the problem is your bank balance, the network, the cash tray, or the machine's software. You are stuck guessing.

Most beginners treat their computer exactly like that ATM. They type code, click Run, and if an error appears they assume "my code is wrong." But that is only one of many possible reasons.

### What Can Go Wrong Beyond Your Code

Here are real situations where the code logic is correct, but the program still fails or behaves badly:

- **Slow program:** Your program reads a very large file from the hard disk. The logic is fine, but storage is physically slow compared to RAM. The program spends most of its time *waiting* for data, not *computing*.
- **App crash:** You open 15 browser tabs, a video editor, and a game at the same time. Your computer runs out of **RAM**. The OS decides to shut down one of the apps to free memory. Your work is lost — not because of a bug in your code, but because the machine ran out of resources.
- **Permission denied:** You try to save a file in a system folder (like `/etc` on Linux or `C:\Windows` on Windows). The **OS** blocks you because only administrators have write access there. Your save logic is correct, but the OS enforced a security rule.
- **Frozen screen:** You start a heavy download and a large file copy at the same time. Both tasks compete for **disk access**. The machine becomes sluggish — not because of bad code, but because two programs are fighting over the same storage channel.

Without understanding the machine, every one of these situations feels like "random magic failure." With this session's knowledge, you will be able to say: "The program is slow because it is waiting for storage I/O," or "The app crashed because RAM was full," or "The file did not save because of an OS permission rule."

### Why This Matters for Your Career

As a software professional, you will face questions like:

- "Why is the server response time high?" — Often a **CPU** or **memory** bottleneck, not a code bug.
- "Why did the deployment fail?" — Could be a **permission** issue on the production server.
- "Why does the app work on my laptop but not on the cloud?" — Different **OS**, different **file paths**, different **resource limits**.

Understanding the machine separates a *coder* (someone who writes syntax) from a *programmer* (someone who understands what the machine does with that syntax).

![Black box vs understanding the machine — closed laptop with vague guesses on one side, and the same machine explained with CPU, RAM, storage, and OS layers on the other so failures feel less random](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitreict-se-2606/masterclasses/sessionmc1/sessionmc1-01-black-box-vs-reality.png)

### Activity: Black Box vs Reality

Think about the last time something went wrong on your computer or phone — an app was slow, a file did not open, a download got stuck, or an update failed.

1. Write down **two guesses** you would make if you were treating the machine as a black box (e.g., "the app is bad," "my internet is slow").
2. Now rewrite those guesses using one of these machine-level terms: **CPU busy**, **RAM full**, **storage slow**, **permission blocked**, **process waiting**. You may not get it perfectly right, but the goal is to start thinking in terms of real machine reasons.

---

## The Hardware Team: CPU, Memory, and Storage

Now that you understand *why* the machine matters, the next step is to meet the three main hardware components that work together every time a program runs. Think of them as a team — each has a specific role, and the speed of the whole team depends on how well they coordinate.

### CPU: The Brain That Executes

- **Official Definition:** The **CPU (Central Processing Unit)** is the electronic circuit inside a computer that executes instructions by performing arithmetic, logic, control, and input/output operations.
- **In Simple Words:** The CPU is the brain of the computer. It does the actual work — adding numbers, comparing values, making decisions, moving data around.
- **Real-Life Example:** Think of a chef in a restaurant kitchen. The chef reads the recipe (instructions), picks up ingredients (data), and follows each step one by one. The chef is fast, but can only do one step at a time in a single hand.

#### How Fast Is a CPU?

Modern CPUs can execute **billions of instructions per second**. That sounds unlimited, but remember — your computer is not running just your program. The web browser, the music player, the OS itself, background updates, antivirus scans — all of these are competing for the same CPU.

- **Practical example:** When you are on a video call (Zoom, Google Meet) and also running a heavy download, the video may start lagging. The CPU is busy handling the download data *and* encoding/decoding the video stream at the same time. There is only so much it can do per second.

#### What Are CPU Cores?

- **Official Definition:** A **core** is an independent processing unit within a CPU. A multi-core CPU has more than one core, allowing it to execute multiple instruction streams simultaneously.
- **In Simple Words:** If one CPU core is one chef, a quad-core CPU is four chefs working in the same kitchen. They can cook different dishes at the same time.
- **Real-Life Example:** In a hospital, one doctor can see one patient at a time. If four doctors are on duty, four patients can be examined simultaneously. More cores = more parallel work.

Most laptops today have 4 to 8 cores. This is why your machine can handle a browser, a music player, and a code editor at the same time — different cores handle different tasks.

#### Cache: The CPU's Quick-Access Shelf

- **Official Definition:** **Cache** is a small, very fast memory located physically close to (or inside) the CPU that stores copies of frequently used data and instructions.
- **In Simple Words:** Cache is like keeping your most-used items on the desk right in front of you instead of getting up and going to the cupboard every time.
- **Real-Life Example:** While cooking, you keep salt, oil, and the spatula within arm's reach on the counter. You do not walk to the pantry for salt every 30 seconds. Cache works the same way for the CPU.

Cache is much smaller than RAM (typically a few megabytes) but much faster. The CPU checks cache first. If the data is there (**cache hit**), it saves time. If not (**cache miss**), it fetches from RAM, which is slower.

### RAM: The Working Desk

- **Official Definition:** **RAM (Random Access Memory)** is volatile, temporary memory used by the computer to store data and instructions that are actively being used or processed.
- **In Simple Words:** RAM is your working desk. Whatever you are actively working on right now sits on the desk. When you turn off the computer (or clear the desk), everything on it disappears.
- **Real-Life Example:** When you are studying for an exam, you spread your notebook, textbook, pen, and calculator on your study table. That table is your RAM. The bookshelf where the textbook normally lives is your storage.

#### What Happens When RAM Is Full?

- **Official Definition:** When RAM is exhausted, the OS uses a technique called **virtual memory** (or **swap**), where it moves less-used data from RAM to storage temporarily to free up space.
- **In Simple Words:** When your desk is full, you move some papers to the shelf to make room. But every time you need those papers again, you have to walk to the shelf and bring them back. This back-and-forth is slow.
- **Real-Life Example:** Imagine you are cooking three dishes at once but your kitchen counter can only hold ingredients for two. You keep putting one dish's ingredients back in the fridge and pulling out another's. The cooking takes much longer because of the constant swapping.

This swap process is why your computer becomes visibly **sluggish** when RAM is nearly full — the machine spends more time moving data between RAM and storage than actually computing.

#### Common Doubt: "RAM vs Storage — What Is the Difference?"

| Feature | RAM | Storage (SSD/HDD) |
|---|---|---|
| **Speed** | Very fast (nanoseconds) | Slower (microseconds to milliseconds) |
| **Persistence** | Data disappears when power is off | Data stays even after shutdown |
| **Size** | Typically 4–32 GB | Typically 256 GB – 2 TB |
| **Purpose** | Hold data currently being used | Store all programs, files, and OS permanently |
| **Analogy** | Study table | Bookshelf / cupboard |

### Storage: The Long-Term Home

- **Official Definition:** **Storage** (SSD or HDD) is non-volatile memory where the computer permanently keeps the operating system, applications, files, and data — even when the machine is powered off.
- **In Simple Words:** Storage is your cupboard, bookshelf, or filing cabinet. Everything lives there permanently until you delete it.
- **Real-Life Example:** Your college notes stored in a folder inside your bag. They stay there even when you are not studying. When you need them, you pull the folder out and put it on your desk (RAM).

#### SSD vs HDD

- **Official Definition:** An **SSD (Solid State Drive)** stores data on flash memory chips with no moving parts, while an **HDD (Hard Disk Drive)** stores data on spinning magnetic platters with a mechanical read/write head.
- **In Simple Words:** SSD is like an electronic notice board — instant access. HDD is like a record player — it needs to physically spin to the right spot before reading.
- **Real-Life Example:** Finding a contact on your phone (SSD-like) vs flipping through a thick paper phone directory page by page (HDD-like).

### Putting It All Together: What Happens When You Open an App

Let us trace what happens when you double-click a program (say, a web browser) on your laptop:

1. **Storage → RAM:** The OS locates the browser's program files on your **storage** (SSD/HDD) and loads the necessary instructions and data into **RAM**.
2. **RAM → CPU:** The **CPU** starts reading instructions from **RAM** and executing them one by one — drawing the window, loading the home page, setting up network connections.
3. **Cache helps:** Frequently used instructions (like the code that renders text on screen) get copied into the CPU's **cache** so the CPU does not have to fetch them from RAM every time.
4. **Results → Storage:** When you bookmark a page or download a file, the data travels back from RAM to **storage** for permanent saving.

This cycle — storage to RAM to CPU to storage — happens millions of times per second while any program is running.

- **Practical example:** When you open WhatsApp Web in a browser, the browser program is loaded from storage to RAM. The CPU processes the JavaScript code. Images and chat data are fetched over the network and stored temporarily in RAM. When you download a photo, it goes from RAM to storage.

![CPU, RAM, and storage working together — program loaded from storage cupboard to RAM kitchen counter, CPU brain executing instructions, with cache as fast spices-on-table helper and speed labels from slowest to fastest](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitreict-se-2606/masterclasses/sessionmc1/sessionmc1-02-cpu-ram-storage-team.png)

### Activity: Map Your Own Machine

Open the **Settings** or **About** section of your laptop/phone and find:

1. **Processor name** (e.g., Intel i5, Apple M2, Ryzen 5) — this is your CPU.
2. **Number of cores** (e.g., 4 cores, 8 cores).
3. **RAM size** (e.g., 8 GB, 16 GB).
4. **Storage type and size** (e.g., 256 GB SSD, 512 GB SSD, 1 TB HDD).

Write these four values down. Now answer: if you open 20 Chrome tabs, a video editor, and a game at the same time, which component is most likely to become the bottleneck — CPU, RAM, or storage? Write one sentence explaining your reasoning.

### Activity: The Restaurant Kitchen Analogy

Imagine a busy restaurant kitchen:

- The **chef** is the CPU — does the actual cooking.
- The **kitchen counter** is the RAM — holds ingredients and dishes currently being prepared.
- The **pantry / cold storage** is the storage — holds all ingredients permanently.
- The **spice rack next to the stove** is the cache — keeps the most-used items within arm's reach.

Now think about these scenarios and identify which component is the bottleneck:

1. The chef is fast but the counter is tiny — only two plates fit at a time. Every dish requires walking to the pantry. **Bottleneck:** ___
2. The counter is huge but there is only one chef for 50 orders. **Bottleneck:** ___
3. The chef and counter are fine, but the pantry door is jammed and ingredients come out very slowly. **Bottleneck:** ___

Answers: (1) RAM, (2) CPU, (3) Storage.

---

## The Operating System: The Manager Behind the Scenes

You have met the hardware team — CPU, RAM, and storage. But hardware alone is useless without something to coordinate it. You cannot have 50 programs all trying to use the CPU and RAM at the same time without someone deciding who goes first, who gets how much memory, and who is allowed to access which files. That coordinator is the **Operating System**.

### What Is an Operating System?

- **Official Definition:** An **Operating System (OS)** is system software that acts as an intermediary between computer hardware and application software, managing hardware resources and providing services for programs.
- **In Simple Words:** The OS is the manager of your computer. It decides which program runs when, how much memory each program gets, which files each program can access, and how hardware devices (keyboard, screen, disk) are shared.
- **Real-Life Example:** Think of a hostel warden. The warden allocates rooms (memory), manages entry/exit rules (permissions), coordinates shared spaces like the mess hall and laundry (shared resources), and handles complaints (error handling). Without the warden, residents would fight over rooms and resources. The OS does the same job for programs.

### Common Examples of Operating Systems

You use an OS every day: **Windows** on most PCs, **macOS** on MacBooks, **Linux** (Ubuntu, CentOS) on servers and developer machines, **Android** on most phones, and **iOS** on iPhones. When you deploy a web application in your career, it will almost certainly run on a **Linux** server — even if you develop on a Windows or Mac laptop.

### The Five Key Responsibilities of an OS

The OS does many things, but for a programmer, five responsibilities matter the most:

#### 1. Process Management

- **What it does:** The OS starts programs, stops them, pauses them, resumes them, and keeps track of every running task.
- **Why it matters:** When you open Chrome, Spotify, and VS Code at the same time, the OS is the one making sure each program gets a fair share of CPU time. Without process management, one program could hog the CPU and freeze everything else.
- **Practical example:** On your phone, when you switch from Instagram to WhatsApp, the OS *pauses* Instagram (saves its state) and *resumes* WhatsApp. When you switch back, Instagram picks up exactly where you left off. The OS managed both processes seamlessly.

#### 2. Memory Management

- **What it does:** The OS allocates RAM to each running program, ensures one program's memory does not overlap with another's, and handles the situation when RAM runs out (using swap/virtual memory).
- **Why it matters:** If two programs accidentally wrote to the same RAM location, data would get corrupted. The OS prevents this by giving each program its own protected memory space.
- **Practical example:** You are editing a document in Google Docs and playing a YouTube video at the same time. The OS makes sure the video data in RAM does not overwrite your document data. Each program "thinks" it has memory all to itself, but the OS is silently managing the partitions.

#### 3. File System Management

- **What it does:** The OS organizes files into folders, maintains a catalog of where every file is stored on the disk, and controls who can read, write, or delete each file.
- **Why it matters:** Without a file system, your 500 GB of data would be one giant unorganized blob. You would have no way to find your assignment from last week.
- **Practical example:** When you save a Word document as `Assignment_1.docx` in your `Documents` folder, the OS records the file name, its size, creation date, and the exact location on the disk where the data is stored. When you open it next time, the OS uses this record to find and load the file.

#### 4. Device and I/O Management

- **What it does:** The OS manages communication between the CPU and external devices — keyboard, mouse, monitor, printer, USB drives, network cards, etc.
- **Why it matters:** Each device speaks its own "language" (protocol). The OS uses **drivers** to translate between the program's requests and the device's protocol.
- **Practical example:** When you press a key on your keyboard, the keyboard sends an electrical signal. The OS receives it through a driver, figures out which key was pressed, and sends that information to the active program (e.g., your text editor). All of this happens in milliseconds without you noticing.

#### 5. Security and Permissions

- **What it does:** The OS enforces rules about who (which user or program) can access which resources — files, folders, network, devices, and even certain CPU instructions.
- **Why it matters:** Without permissions, any program could read your passwords, delete system files, or send data over the network without your knowledge.
- **Practical example:** On your laptop, you can read files in your home folder but not in another user's folder. If you try, you get **"Permission denied."** This is the OS protecting one user's data from another. The same rule applies to programs — a regular app cannot modify system files unless it is given administrator/root privileges.

#### Common Doubt: "Why Do Permission Errors Happen?"

Permission errors are one of the most common frustrations for beginners. Here is why they happen:

- Every file and folder on your computer has a set of **permission rules** — who can read it, who can write to it, and who can execute it.
- When you or your program tries to perform an action that violates these rules, the OS blocks the action and returns an error.
- This is **not a bug** — it is a security feature. The OS is doing its job by protecting resources.
- **Practical example:** You download a script and try to run it. The terminal says "Permission denied." This usually means the file does not have "execute" permission. The file is fine; the OS just needs to know you explicitly want to allow execution.

![Operating System as resource manager — OS coordinator handling process management, memory allocation, file system access, device I/O, and security permissions like a hostel warden organizing shared resources](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitreict-se-2606/masterclasses/sessionmc1/sessionmc1-03-operating-system-manager.png)

### What the OS Does When You Run a Program

Let us trace the OS's actions when you double-click an app or type a command in the terminal:

1. **Creates a process:** The OS creates a new process — a running instance of the program — and assigns it a unique **Process ID (PID)**.
2. **Allocates memory:** The OS reserves a portion of RAM for this process so it has space to work without interfering with other programs.
3. **Loads instructions:** The OS reads the program's instructions from **storage** and places them into the allocated **RAM**.
4. **Sets up file access:** If the program needs to read or write files, the OS prepares the file connections (called **file descriptors**).
5. **Schedules CPU time:** The OS places the process in a queue. A component called the **scheduler** decides when this process gets its turn on the CPU.
6. **Execution begins:** The CPU starts executing the process's instructions from RAM.

All six steps happen in a fraction of a second. You double-click, and the app window appears — but underneath, the OS performed a complex coordination sequence.

### Activity: Spot the OS at Work

Think about these everyday scenarios and identify which OS responsibility is involved:

1. You plug in a USB drive and your computer shows a notification: "New device connected." — **OS responsibility:** ___
2. You open Task Manager (Windows) or Activity Monitor (Mac) and see a list of running programs. — **OS responsibility:** ___
3. You try to delete a file in `C:\Windows\System32` and get "Access Denied." — **OS responsibility:** ___
4. Your laptop slows down when you open too many apps, and you see "Low memory" warning. — **OS responsibility:** ___
5. You save a photo and find it later in your Downloads folder. — **OS responsibility:** ___

Answers: (1) Device/I/O management, (2) Process management, (3) Security/permissions, (4) Memory management, (5) File system management.

---

## Processes: Programs in Action

You now know that when you run a program, the OS creates something called a **process**. This section digs deeper into what a process is, how it differs from the program file, and why processes have different states.

### Program vs Process

This distinction is fundamental and comes up in interviews, debugging, and system design:

- **Official Definition:** A **program** is a static set of instructions stored as a file on storage. A **process** is a dynamic, running instance of a program loaded into memory with its own state, resources, and execution context.
- **In Simple Words:** A program is the recipe written in a book on the shelf. A process is someone actually cooking that recipe right now — with ingredients out, the stove on, and a timer running.
- **Real-Life Example:** You have a `.docx` file on your desktop — that is the program (static file). When you double-click it and Word opens with the document loaded — that is the process (active, running, using RAM and CPU).

**Key insight:** You can have multiple processes from the same program. If you open two separate Chrome windows, that is two processes running from the same Chrome program file. Each has its own memory, its own tabs, and its own PID.

### What Is a Thread?

- **Official Definition:** A **thread** is the smallest unit of execution within a process. A single process can have multiple threads that share the same memory space but execute independently.
- **In Simple Words:** If a process is one chef cooking a meal, threads are the chef's two hands — they can do different small tasks (chopping and stirring) at the same time, but they share the same workspace.
- **Real-Life Example:** In a word processor, one thread handles your typing, another thread checks spelling in the background, and a third thread auto-saves the document every few minutes. All three threads belong to the same process (the word processor) and share its memory.

For now, just know that threads exist inside processes. You do not need to create or manage threads at this stage of learning.

### Process ID (PID): The OS Ticket Number

- **Official Definition:** A **PID (Process ID)** is a unique integer assigned by the OS to every process at the time of its creation, used to identify and manage that process.
- **In Simple Words:** PID is the token number you get at a bank or service counter. It uniquely identifies your turn (your process) among all the other people (processes) waiting.
- **Real-Life Example:** At a hospital, every patient gets a unique registration number. The doctor, nurse, and pharmacist all use that number to track the patient. Similarly, the OS uses the PID to track every process — to pause it, resume it, give it CPU time, or terminate it.

Every time you open an app, it gets a unique PID. If the app crashes and you reopen it, the new instance gets a fresh PID. You can see all running PIDs in **Task Manager** (Windows), **Activity Monitor** (Mac), or by running `ps aux` in a terminal.

### Process States: Why Programs Sometimes "Wait"

A process is not always actively running. The OS juggles many processes, and at any moment, each process is in one of several **states**:

- **New / Created:** The OS has just created the process. It exists but has not started running yet.
- **Ready:** The process is prepared to run and is waiting in line for the CPU. Think of it as standing in a queue at a counter.
- **Running:** The CPU is actively executing this process's instructions. Only one process per CPU core can be in the "Running" state at a given instant.
- **Waiting / Blocked:** The process is paused because it is waiting for something — a file to load from disk, data from the network, or input from the user. It cannot use the CPU until the wait is over.
- **Terminated:** The process has finished its work (or crashed) and the OS is cleaning up its resources (freeing RAM, closing files).

#### The Lifecycle in Plain Language

Imagine you are at a busy government office to submit a form:

1. You enter the office and get a token (**New**).
2. You sit in the waiting area until your number is called (**Ready**).
3. You walk up to the counter and the officer processes your form (**Running**).
4. The officer says "bring a photocopy from the machine outside." You leave the counter and go to the photocopy machine. Your form processing is paused (**Waiting / Blocked**).
5. You come back with the photocopy, wait for your turn again (**Ready**), then the officer finishes your form (**Running**).
6. Your work is done. You leave. (**Terminated**).

This is exactly how the OS manages processes. A process cycles between Ready, Running, and Waiting many times before it finally Terminates.

#### Common Doubt: "Why Does My Program Stop Responding?"

When a program "freezes" or shows "Not Responding," it is usually because:

- The process is **Blocked/Waiting** for something that is taking too long — a slow disk read, a network request that timed out, or a database query on a large table.
- The process is stuck in an **infinite loop** — the CPU is executing instructions, but the instructions keep repeating without ever finishing. The program *is* running, but it is not making progress.
- The OS is **overloaded** — too many processes are competing for the CPU, and this particular process is not getting enough CPU time to respond to your clicks.

Understanding process states helps you diagnose these situations instead of just saying "it crashed."

### How the OS Schedules Processes: A Simplified View

With dozens (sometimes hundreds) of processes running, the CPU cannot serve all of them simultaneously. The **scheduler** is the OS component that decides which process gets the CPU next.

- **Round-Robin:** Each process gets a small, equal time slice (say, 10 milliseconds). After the slice, the OS pauses the process and gives the CPU to the next one in line. This is why your music keeps playing while you type — both programs get rapid, tiny turns that *feel* simultaneous.
- **Priority-Based:** Some processes get more CPU time than others. System-critical processes (like the OS kernel) get higher priority than a background update. When you are on a video call and also downloading a file, the OS gives higher priority to the call because real-time communication cannot tolerate delays.

You do not need to configure the scheduler manually. But knowing it exists explains why even a single-core computer can seem to run multiple programs "at the same time" — it is switching between them extremely fast.

![Program vs process vs thread and process states — recipe book as stored program, two cooks running the same recipe as separate processes with PID ticket numbers, helpers as threads, and lifecycle states from New to Terminated](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitreict-se-2606/masterclasses/sessionmc1/sessionmc1-04-process-lifecycle-pid.png)

### Activity: Explore Running Processes on Your Machine

Open a **terminal** (or Task Manager on Windows / Activity Monitor on Mac) and observe:

1. **How many processes** are currently running? You will likely see 100+ even though you only opened a few apps. Many are background OS processes.
2. **Pick any three processes** and note their **PID** and **name**. Try to guess what each one does based on its name (e.g., "chrome" is the browser, "spotify" is the music player, "kernel_task" or "System" is the OS itself).
3. **Close one application** (like a browser window) and check the process list again. The process should disappear — it has moved to the **Terminated** state and the OS has freed its resources.

### Activity: Process State Matching

Match each real-world scenario to the correct process state:

| Scenario | State |
|---|---|
| You just opened a new app and it is loading for the first time. | ___ |
| An app is actively responding to your clicks and showing results. | ___ |
| A file download is in progress and the app is waiting for network data. | ___ |
| You closed the app and it is no longer in the process list. | ___ |
| The app is ready but another app is currently using the CPU. | ___ |

Answers: New/Created, Running, Waiting/Blocked, Terminated, Ready.

---

## File Systems: How Data Lives on a Machine

Processes explain how programs **run**. File systems explain how programs and data are **stored and organized** so the OS can find them, protect them, and serve them to the right process when needed.

### What Is a File System?

- **Official Definition:** A **file system** is a method of organizing, storing, and retrieving files on a storage device. It defines how data is named, stored, and accessed.
- **In Simple Words:** A file system is like the catalog in a library. The library has thousands of books (files), and the catalog tells you which shelf, row, and position each book is in. Without the catalog, finding a specific book would mean searching every shelf randomly.
- **Real-Life Example:** Think of a large hospital. Every patient has a medical file. These files are stored in organized cabinets — sorted by department, then by year, then by patient name. The filing system (file system) makes it possible for any doctor to find any patient's records quickly.

### Files, Folders, and Paths

#### What Is a File?

- **Official Definition:** A **file** is a named collection of data stored on a storage device. It can contain text, images, code, videos, or any other type of information.
- **In Simple Words:** A file is a single document — your assignment, a photo, a song, a Python script.
- **Real-Life Example:** A single page of notes in your notebook.

#### What Is a Folder (Directory)?

- **Official Definition:** A **directory** (commonly called a folder) is a container within the file system that can hold files and other directories, creating a hierarchical structure.
- **In Simple Words:** A folder is a labelled box that groups related files together.
- **Real-Life Example:** A labelled section in a filing cabinet — "Semester 1 Assignments," "Family Photos," "Music."

#### What Is a Path?

- **Official Definition:** A **path** is a string that specifies the unique location of a file or directory within the file system hierarchy.
- **In Simple Words:** A path is the full address of a file — starting from the top-level location all the way down to the specific file.
- **Real-Life Example:** A postal address: "Room 204, Block B, Hostel 5, IIT Campus, City." Each part narrows down the location.

**Examples of paths:**

| OS | Example Path | Meaning |
|---|---|---|
| Windows | `C:\Users\Priya\Documents\assignment.docx` | File `assignment.docx` inside `Documents` folder of user `Priya` on the C drive |
| Mac/Linux | `/home/priya/documents/assignment.docx` | Same idea, different format — forward slashes, no drive letter |

Notice the difference: Windows uses **backslashes** (`\`) and Mac/Linux use **forward slashes** (`/`). This is a common source of bugs when code written on one OS is run on another.

### How the File System Organizes Data

The file system creates a **tree structure** (hierarchy):

- At the top is the **root** — `C:\` on Windows, `/` on Mac/Linux.
- Inside the root are folders like `Users`, `Program Files`, `etc`, `home`.
- Inside those are more folders and files, branching out like a tree.

Every single file on your computer has a unique path from the root to its location. The OS uses this path to locate the file on the physical storage device.

#### Metadata: Data About Data

For every file, the file system also stores **metadata** — information *about* the file, separate from the file's actual content:

- **File name** and **extension** (e.g., `notes.txt` — name is `notes`, extension is `.txt`)
- **Size** (e.g., 2.4 KB)
- **Creation date** and **last modified date**
- **Permissions** (who can read, write, or execute this file)
- **Owner** (which user created or owns the file)

This metadata is what you see when you right-click a file and select "Properties" (Windows) or "Get Info" (Mac).

### Permissions: The Guards at Every Door

- **Official Definition:** **File permissions** are access control rules set by the OS that determine which users or processes can read, write, or execute a specific file or directory.
- **In Simple Words:** Permissions are guards at the door of every file. They check your identity and decide if you can enter (read), modify (write), or run (execute) the file.
- **Real-Life Example:** In a college, the library is open to all students (read access), but only librarians can add or remove books (write access). The server room is locked — only IT staff can enter (no access for others).

#### The Three Permission Types

| Permission | Symbol | What It Allows |
|---|---|---|
| **Read** | `r` | View the contents of the file |
| **Write** | `w` | Modify, add to, or delete the file |
| **Execute** | `x` | Run the file as a program or script |

Permissions are set for three categories: **Owner** (file creator), **Group** (team members), and **Others** (everyone else). Each category can have any combination of read, write, and execute.

#### Why "Permission Denied" Happens

When you see "Permission denied," it means one of the following:

- You are trying to **write** to a file you can only **read**.
- You are trying to **execute** a file that does not have execute permission.
- You are trying to **access** a folder or file owned by another user or the system.
- You are a regular user trying to modify a **system-protected** location.

This is always the OS enforcing rules — not a random error. Understanding this saves hours of frustrated debugging.

![File system organization — folder tree with full path address, library catalog map metaphor, and read write execute permission icons showing how the OS locates and protects files on disk](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitreict-se-2606/masterclasses/sessionmc1/sessionmc1-05-file-system-paths-permissions.png)

### Activity: Explore Your File System

Do the following on your own machine:

1. **Navigate to your home folder** — on Windows, open `C:\Users\YourName`; on Mac/Linux, open `/Users/YourName` or `/home/YourName`.
2. **Count the top-level folders** you see (Documents, Downloads, Desktop, etc.). These were created by the OS when your user account was set up.
3. **Right-click any file** and check its properties/info. Note the **size**, **creation date**, **modified date**, and **permissions** (if visible).
4. **Try this thought experiment:** If the OS did not organize files into folders with names and metadata, how would you find your assignment from two weeks ago among thousands of files?

### Activity: Permission Scenario Matching

For each scenario, identify what type of permission is needed and whether it would typically be granted:

| Scenario | Permission Needed | Typically Granted? |
|---|---|---|
| You want to open and read a README file in a project folder. | ___ | ___ |
| You want to edit a configuration file in the system directory. | ___ | ___ |
| You want to run a downloaded script from the internet. | ___ | ___ |
| A teammate wants to view your shared project files. | ___ | ___ |

Answers: (1) Read — yes, (2) Write — no, needs admin, (3) Execute — may need explicit permission, (4) Read — yes if shared with group.

---

## Key Takeaways

- A computer is **not** a black box. It has measurable limits in **CPU speed**, **RAM capacity**, and **storage speed** — and understanding these limits helps you explain failures instead of guessing.
- The **CPU** executes instructions, **RAM** holds data being actively used, and **storage** keeps everything permanently. They work as a team: storage → RAM → CPU → storage.
- The **Operating System** is the manager that coordinates processes, memory, files, devices, and security. Every time you run a program, the OS performs a complex sequence of steps in the background.
- A **process** is a running instance of a program with its own PID and lifecycle states (New, Ready, Running, Waiting, Terminated). Understanding states helps you diagnose why programs freeze or slow down.
- The **file system** organizes data into a tree of files and folders, tracks metadata, and enforces **permissions** (read, write, execute) that protect your data and the system.

This foundation connects directly to your future sessions. When you start writing larger programs, handling files, debugging errors, and eventually deploying applications to servers, you will use these concepts daily. The difference between "my code is broken" and "the server's RAM is full" is exactly the knowledge you built today.

---

## Important Terminologies and Concepts

| Term | What It Means | Analogy |
|---|---|---|
| **Black Box** | A system whose internals are hidden | ATM — you see input/output but not the mechanism |
| **CPU** | Executes instructions — the brain of the computer | Chef in a kitchen |
| **Core** | An independent processing unit within a CPU | Multiple doctors on duty at a hospital |
| **Cache** | Small, fast memory near the CPU for frequently used data | Spice rack next to the stove |
| **RAM** | Temporary working memory for active programs | Study table / kitchen counter |
| **Virtual Memory / Swap** | OS technique to use storage as overflow when RAM is full | Moving papers to the shelf when desk is full |
| **Storage (SSD/HDD)** | Permanent data storage that survives shutdown | Bookshelf / cupboard / filing cabinet |
| **SSD** | Solid State Drive — fast, no moving parts | Phone contact search |
| **HDD** | Hard Disk Drive — slower, spinning platters | Flipping through a phone directory |
| **Operating System (OS)** | System software managing hardware and programs | Hostel warden coordinating rooms and rules |
| **Process** | A running instance of a program with its own memory and PID | Recipe being cooked right now |
| **Thread** | A smaller execution unit inside a process | Chef's two hands doing tasks simultaneously |
| **PID (Process ID)** | Unique number the OS assigns to each process | Hospital patient registration number |
| **Process States** | New, Ready, Running, Waiting, Terminated | Government office queue stages |
| **Scheduler** | OS component that decides which process gets CPU time | Office token-calling system |
| **File System** | Method of organizing files on storage | Library catalog |
| **Directory / Folder** | Container for grouping files | Labelled section in a filing cabinet |
| **Path** | Full address of a file in the file system | Postal address |
| **Permissions (r, w, x)** | Rules controlling read, write, execute access | Guards at the door |
| **"Permission Denied"** | OS blocking an unauthorized action | Security guard refusing entry |
