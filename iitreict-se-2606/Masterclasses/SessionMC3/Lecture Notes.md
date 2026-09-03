# Masterclass: Internet & Browser Internals

## What You Will Learn in This Session

In the previous masterclass you learned that two programs on the same laptop can feel different because they follow different **algorithms**. That session was about work *inside one machine*: how a plan grows as data grows, and why you compare methods before you choose one.

This session is about work *between machines*. A search that is fast on your laptop is not enough if the result must come from a server in another city, reach a payment service, and return safely to the user's phone.

You will learn:

- Why modern software products need the **internet** to connect **users**, **servers**, and **services**.
- Why building a product as a fully **isolated system** (no network) creates serious limits.
- How **request and response** is the basic conversation of networked software.
- How a request actually **travels** from a browser to a distant machine and back.
- Why **DNS** maps human-readable names to machine addresses.
- Why **HTTPS** is needed for secure, reliable communication.

By the end, you will look at a website or an app and ask: "Who is talking to whom, how did the name get resolved, and is the path protected?" — not just "The page opened."

---

## Why Modern Applications Need the Internet

Before we talk about browsers, names, and security, we need a clear reason. Why can so many products not live on one laptop at all?

### Users, Servers, and Services Are Not in One Room

- **Official Definition:** A **software product** is an application that people use to complete a job — booking a ticket, sending money, checking results, or chatting with a friend.
- **In Simple Words:** A product is not "a file on your computer." It is a tool that many people use, often at the same time, from many places.
- **Real-Life Example:** IRCTC is not a program that lives only on one railway clerk's PC. Lakhs of travellers open it from phones and laptops across India.

Those travellers are **users**. The machines that store trains, seats, and bookings are **servers**. The extra helpers — SMS, email, payment — are **services**. The internet is what lets the three meet.

- **Official Definition:** The **internet** is a worldwide network of networks. Independent computers and organisations connect through agreed rules so they can exchange data.
- **In Simple Words:** The internet is a public road system for computers. Your phone, a college server, and a bank server can send messages even though they do not sit in the same building.
- **Real-Life Example:** A letter can travel from a village post office to a city GPO because there is a postal network. A UPI payment travels from your phone to a bank for the same kind of reason — there is a computer network.

![Users, servers, and services meeting through the internet — students on phones and laptops on one side, a shared server holding bookings and marks on the other, and helper services for SMS, payment, and email connected through a central internet hub](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitreict-se-2606/masterclasses/sessionmc3/sessionmc3-01-users-servers-services.png)

### What "Need the Internet" Actually Means

A modern product usually needs the network for three jobs at once:

- **Reach users wherever they are.** The same result portal must work in a hostel, at home, and on mobile data.
- **Keep one shared truth.** Seat number 14 on a train cannot be sold twice because two people opened two separate copies of a file.
- **Call other specialised services.** Your app may not send SMS itself. It asks an SMS service. It may not store card details itself. It asks a payment service.

**Need:** If users, data, and helper services live in different places, a product that never leaves one machine cannot do the job.

**Logic:** The internet is not a decoration around software. For most products, it is the path that makes the product possible.

A quick way to see the difference:

| Kind of program | Where the latest truth lives | Needs the internet? |
|---|---|---|
| Calculator, local notepad | Only on your device | No |
| Photo editor that never uploads | Only on your device | No |
| Result portal, UPI, ticket booking | On a **server**, shared by many users | Yes |
| Chat app with media and backup | On servers, plus a copy on your phone | Yes |

### Common Doubt: "Is Every Program an Internet Program?"

No. A calculator on your phone, a notepad file, or a photo editor that never uploads can work **offline**. Those tools do not need a shared live record or a distant service.

The moment many users must see the *same* latest data — wallet balance, exam seat, cricket score, hostel mess menu that updates daily — isolation breaks the product.

### Activity: Name the Three Parties

Pick one app you used today: **WhatsApp**, **GPay**, **Swiggy**, a **college portal**, or **YouTube**.

1. Write who the **user** is (you, on which device).
2. Write what the **server** must be storing (chats, balance, menu, marks, videos).
3. Write one **service** that is probably not the main app itself (SMS OTP, map, payment, email).

If you can name all three, you already see why that product depends on the internet.

---

## The Problem with Isolated Systems

Once you see that users, servers, and services sit in different places, the next question is: what goes wrong if we refuse the network and keep everything on one machine?

### What an Isolated System Is

- **Official Definition:** An **isolated system** is software that runs only on one computer, stores all data on that computer, and has **no network communication** with other machines.
- **In Simple Words:** Isolated means "this laptop is the whole world." Nobody else can reach the data, and the program cannot ask any other program for help.
- **Real-Life Example:** A kirana shop that keeps accounts only in one paper register on one desk. If the owner is away, if the register is lost, or if a second shop opens, that single book cannot serve everyone.

Isolation is not always wrong. It is wrong when the *product* needs sharing, updates, or outside services.

### Demerits of Building Products Without a Network

Fully isolated products hit the same walls again and again:

- **No shared live data.** Two admission clerks cannot update the same seat list. One USB copy becomes stale the moment the other copy changes.
- **No multi-device access.** The student has a phone. The office has a desktop. Isolated software forces everyone onto one machine.
- **Single point of loss.** If that hard disk fails, the product and the records disappear together.
- **No outside services.** You cannot send an OTP, take a UPI payment, or show a live train status without talking to another system.
- **Painful updates.** A new version must be copied by hand to every machine. Miss one PC, and users run old, buggy software.

**Need:** Isolation looks simple on day one. The demerit appears when the second user, the second device, or the first payment arrives.

**Logic:** If the truth must be one, it cannot live as five private copies with no way to talk.

Isolation is still the right design for some tools: a marks calculator, a draft essay that should not leave your laptop, or an exam app that must not call the network during the test. The demerit is not "offline exists." The demerit is using isolation for a product that is actually a shared, live, multi-user system.

### Common Doubt: "Can't We Just Copy the File Every Evening?"

Copying a spreadsheet to a pen drive is a kind of transfer, but it is not reliable communication.

- Copies go stale. Someone books a seat after you copied the file.
- Copies conflict. Two people edit two copies. Which one is correct?
- Copies are insecure. A pen drive can be lost, read, or overwritten.

That is why networked products do not "share by copying folders." They send **requests** and get **responses** against one shared server (or a planned set of servers).

![Isolated system versus a connected product — one desk with a single paper register and USB drive that can be lost, next to many phones and an office PC sharing one live server so everyone sees the same latest data](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitreict-se-2606/masterclasses/sessionmc3/sessionmc3-02-isolated-vs-connected.png)

### Activity: Isolated vs Connected

For each product, write **Isolated** or **Must be connected**, and one reason.

| Product | Isolated or connected? | One reason |
|---|---|---|
| A marks calculator that never saves online | | |
| IRCTC seat booking | | |
| A diary app that stays only on your phone | | |
| GPay sending money to a friend | | |
| Attendance for 4,000 students across two campuses | | |

Suggested direction: calculator and private diary can stay isolated. Booking, payments, and multi-campus attendance must be connected.

---

## Request and Response: How Networked Software Talks

Isolation fails because machines need a conversation. The standard conversation on the internet is simple: one side **asks**, the other side **answers**.

### Client, Server, Request, Response

- **Official Definition:** A **client** is the program that starts a conversation by sending a request. A **server** is the program that waits for requests, does work, and sends a response.
- **In Simple Words:** The client is the customer. The server is the counter. The customer asks for something; the counter replies.
- **Real-Life Example:** You stand at a railway enquiry window and ask, "Is the 12801 running today?" That question is a request. The clerk's answer is a response.

Your **browser** is a very common client. So is a mobile app. The machine that holds the website or the API is the server.

- **Official Definition:** A **request** is a structured message that says what the client wants (open this page, fetch this balance, place this order). A **response** is a structured message that returns the result (the page, the number, success or failure).
- **In Simple Words:** Request is the question. Response is the answer. Nothing useful happens until both travel.
- **Real-Life Example:** In UPI you tap "Pay." Your app sends a request with amount and UPI ID. The bank systems send a response: success or failure.

### The Internet's Role in This Conversation

The internet does not "know" your ticket. It **carries** the request and the response.

- The client and server can be thousands of kilometres apart.
- Many requests can travel at once, from many users.
- Each message must be delivered to the *right* machine, not a random one.

**Need:** Without a shared path, the client can only talk to files on its own disk.

**Logic:** Request–response is how software stays simple. The browser does not store every train. It asks. The server does not draw buttons on your phone. It answers.

### What a Typical Round Trip Looks Like

A page open is not one magic flash. It is a loop:

1. You type a name or tap a button in the **browser** (or app).
2. The client builds a **request**.
3. The request travels across the **network** to the correct **server**.
4. The server checks rules, reads data, and builds a **response**.
5. The response travels back. The client shows it to you.

If any step fails — wrong address, broken path, blocked security, busy server — you see a spinner, a timeout, or an error page. The algorithm on the server can be excellent and you still see failure, because the *path* failed.

### Common Doubt: "Does the Whole Website Sit Inside My Browser?"

No. Your browser stores some files for speed (you will see this later as **cache**), but the live truth — your balance, your booking — stays with the server. Refreshing a page is often a new request for a fresh response.

### Activity: Write One Conversation

Choose **GPay**, **IRCTC**, or a **result portal**. In your notebook, write four lines:

1. **Client:** who asks (browser or app).
2. **Request:** what is being asked (one sentence).
3. **Server:** what it must check or fetch.
4. **Response:** what comes back on success, and what comes back on failure.

Write ordinary sentences. You are practising the shape of the conversation, not writing software.

---

## How a Request Travels Across the Network

You now know *what* is sent. The next skill is *how* it moves. A request does not jump from your laptop to "the internet" as one solid brick.

### Addresses, Packets, and Hops

- **Official Definition:** An **IP address** is a numerical label that identifies a device (or a reachable interface) on a network, so other machines know where to send data.
- **In Simple Words:** An IP address is a computer's postal address. Without it, a message has nowhere to go.
- **Real-Life Example:** "Deliver this parcel to Flat 12, Block C" works. "Deliver this to Ramesh" does not work if the courier has no address. Machines are the same: they need numbers.

- **Official Definition:** A **packet** is a small chunk of data with a destination address, a return address, and a piece of the original message.
- **In Simple Words:** Large messages are cut into envelopes. Each envelope travels, then the receiver puts the letter back together.
- **Real-Life Example:** A long letter sent as several postcards, each numbered 1 of 8, 2 of 8, and so on.

Your request is split into packets. Packets travel through **routers**. Each router reads the destination and forwards the packet to the next hop. This is why a request "crosses" many networks, not one private wire.

### The Path in Plain Order

When you open a site from a phone on college Wi-Fi, the usual path looks like this:

1. The **browser** prepares the request.
2. Your **device** sends packets to the nearby **router** (Wi-Fi or mobile tower).
3. The **Internet Service Provider (ISP)** carries those packets into the wider internet.
4. Packets hop across many networks until they reach the **destination server**.
5. The server's **response** packets travel the return path to your device.
6. The browser **assembles** the response and shows the page.

- **Official Definition:** A **router** is a device that forwards packets toward their destination by choosing the next network hop.
- **In Simple Words:** A router is a junction. It does not read your email for meaning. It reads the address on the envelope and sends it onward.
- **Real-Life Example:** A railway junction does not open passenger luggage. It sends the train toward the next station on the route.

- **Official Definition:** An **Internet Service Provider (ISP)** is the organisation that connects your home, college, or mobile connection to the rest of the internet.
- **In Simple Words:** The ISP is the local post office for packets. Your Wi-Fi reaches the router; the ISP carries traffic beyond the campus or house.
- **Real-Life Example:** A village post office accepts your letter and hands it to the wider postal network. Your college Wi-Fi alone cannot reach a server in another city.

![How a request travels across the network — browser to device to router to ISP through internet hops to the server, with a request arrow going out and a response arrow coming back](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitreict-se-2606/masterclasses/sessionmc3/sessionmc3-03-request-path.png)

### Delay Is Not the Same as a Broken Path

Two different path problems feel the same to a beginner ("the site is slow"), but they are not the same:

- **High delay:** Packets arrive, but they take time. Festive IRCTC traffic and a crowded hostel Wi-Fi both add waiting.
- **Packet loss:** Some envelopes never arrive. The browser may retry, or it may show an error after waiting.
- **Server busy:** The path is fine. The counter has a long queue. Your request arrived; the response is late.

A correct algorithm on the server cannot hide a weak first hop. A perfect Wi-Fi signal cannot hide a server that is down.

### Why the Path Must Be Reliable

Software products fail in public when the path is weak, even if the server logic is correct.

- **Delay:** Packets sit in a queue. The page feels slow.
- **Loss:** Some packets never arrive. The client retries or shows an error.
- **Wrong destination:** A mis-addressed request never reaches the real server.
- **Open path:** If anyone in the middle can read the packets, private data leaks. That is why HTTPS exists (next major topic after names).

**Need:** Users will not trust a product that "sometimes books, sometimes vanishes." Reliable delivery is part of the product.

**Logic:** Networking is not a side subject. It is how request and response stay honest across distance.

### Common Doubt: "If My Wi-Fi Is On, Is the Whole Path Fine?"

Wi-Fi is only the first hop. The ISP can be congested, or the destination server can be down.

A college network rule can also block a site even when the signal is full. A correct first hop is necessary, not sufficient.

### Activity: Trace Seven Steps

Open any website you already use (news, college site, or a shop). Without using developer tools, write the seven steps in your own words:

**Browser → Device → Router → ISP → Internet hops → Server → Response back.**

Circle the step you understand least. That circled step is usually either **naming** (DNS) or **security** (HTTPS) — the two topics that come next.

---

## DNS: From Human Names to Machine Addresses

Packets need an IP address. People do not want to remember IP addresses. **DNS** is the bridge between those two facts.

### Why Machines Cannot Live on Names Alone

- **Official Definition:** A **domain name** is a human-readable name for a site or service, such as `irctc.co.in` or `google.com`.
- **In Simple Words:** A domain name is the name you type. It is for humans.
- **Real-Life Example:** You save "Amma" in your phone. The phone still dials a number. You never type the number, but the call cannot happen without it.

Routers forward using **IP addresses**, not friendly names. If the browser only had `irctc.co.in` and no number, the packets would have no destination.

### What DNS Does

- **Official Definition:** **DNS (Domain Name System)** is a worldwide, distributed directory that maps domain names to IP addresses (and related records).
- **In Simple Words:** DNS is the internet's contact list. You give the name. DNS returns the number.
- **Real-Life Example:** Directory enquiry used to work like this: you say "I want the number for the district hospital," and you get a phone number. DNS is that enquiry for computers.

**Need:** Billions of devices cannot print a paper phone book of every site. Names also change servers. The mapping must be looked up, not carved into every laptop forever.

**Logic:** DNS is not the website. It is the *lookup* before the real request can be addressed.

- **Official Definition:** A **DNS resolver** is the helper that accepts a name-lookup question from your device and returns the matching IP address.
- **In Simple Words:** The resolver is the person you ask, "What is the number for this name?"
- **Real-Life Example:** You do not walk to every hospital in the city. You ask one enquiry desk. That desk may check its own list or call another desk. You still get one number back.

### What Happens When You Type a Name

A simplified, correct sequence:

1. You type `www.example.com` in the **address bar**.
2. The browser asks: "Do I already know this IP?" (recent **DNS cache**).
3. If not, the device asks a **DNS resolver** (often your ISP or a public resolver).
4. The resolver finds the authoritative answer: this name → this IP (or these IPs).
5. The browser now has a machine address and can send the **request** to that IP.

If DNS fails, the site is not "down" in the way students first think. Your laptop never received a destination number, so the request cannot start.

![DNS mapping a human-readable name to a machine address — address bar showing irctc.co.in, a resolver answering what the number is, then an IP address so the request can start, with a phone-contacts analogy](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitreict-se-2606/masterclasses/sessionmc3/sessionmc3-04-dns-lookup.png)

Wrong DNS is more dangerous than failed DNS. A failed lookup shows an error. A *wrong* lookup can send you to the wrong machine while the name in the address bar still looks familiar. That is one reason you still check the full domain and still need HTTPS after the name is resolved.

### Common Doubt: "If I Know the IP, Do I Still Need DNS?"

You can sometimes open a site by IP, but people will not remember it, certificates and virtual hosts often expect a **name**, and IPs change when companies move servers. DNS exists so humans keep using names while machines keep using numbers.

### Activity: Fill the Contact List

Complete this table in your notebook.

| What a human types | What the machine needs | Who maps one to the other |
|---|---|---|
| `sbi.co.in` | an **IP address** | |
| a friend's name in your phone | a **phone number** | Phone contacts |
| a college website name | | **DNS** |

Write one sentence: "If DNS is wrong, the request goes to the *wrong number* — like dialling a shop that moved."

---

## HTTPS: Why Communication Must Be Secure

DNS gets you to *a* machine. That is not enough. You must reach the *right* machine, and the conversation must not be readable on the road.

### The Problem with an Open Path

- **Official Definition:** **HTTP (Hypertext Transfer Protocol)** is the set of rules for sending web requests and responses — pages, forms, files — between a client and a server.
- **In Simple Words:** HTTP is the language of "please give me this page" and "here is the page."
- **Real-Life Example:** A postcard. The message is written in ordinary words. Anyone who handles the postcard can read it.

On a shared network — college Wi-Fi, a cafe, a mobile hotspot — an open HTTP conversation can leak passwords, session details, or form data. Isolated systems avoided this by never sending data. Networked systems must protect the path.

HTTP was enough when many pages were public posters: a notice, a timetable, a news article with no login. The moment the request carries a password, an OTP, a UPI PIN, or a personal result, an open postcard is the wrong design.

### What HTTPS Adds

- **Official Definition:** **HTTPS** is HTTP sent over a secure layer (commonly **TLS**). It encrypts the conversation and helps the client verify the server's identity using a **certificate**.
- **In Simple Words:** HTTPS is a locked cover around the same request–response talk. Outsiders see noise, not your password. The lock also helps confirm you reached the real bank site, not a look-alike.
- **Real-Life Example:** A sealed, addressed envelope instead of a postcard — plus a stamp that shows the sender is really the bank branch, not a stranger in the market.

**Need:** The internet is a shared road. Shared roads need locks if the cargo is private.

**Logic:** Reliability is not only "packets arrived." It is "packets arrived unread and at the genuine counter."

### Encryption and Identity, Separately

Students often mix two ideas. Keep them apart:

- **Encryption** protects *content*. A person in the middle cannot read the form you submitted.
- **Identity (certificate)** protects *who*. You have more reason to believe you are talking to `yourbank.co.in`, not a fake page that only *looks* similar.

HTTPS does **not** mean the company is honest, the offer is real, or the page is free of mistakes. It means the *pipe* is protected. A scam site can still use HTTPS.

| What you hope | What HTTPS can do | What HTTPS cannot do |
|---|---|---|
| Nobody on Wi-Fi reads your password | Encrypt the path | Stop you from typing on a fake-looking site |
| You reached the real named server | Check the **certificate** against the name | Prove the business is trustworthy |
| The page is correct | Protect delivery of whatever the server sent | Fix wrong marks or a scam offer |

### What You See in the Browser

- A **padlock** (or similar indicator) next to the address usually means HTTPS is in use.
- The address starts with `https://`.
- A warning page appears when the certificate is expired, mismatched, or not trusted. That warning is the browser doing its job. Do not click through it for banking or college login.

### Common Doubt: "I Have HTTPS. Can I Type Passwords Anywhere?"

No. HTTPS protects the road. It does not prove the *business*. Check the **domain name** carefully. `sbi.co.in` and a look-alike spelling are not the same destination. DNS plus HTTPS plus your own reading of the name work together.

### Activity: Open or Locked

For each case, write **Safe enough to type a password?** Yes or No, and why.

1. College Wi-Fi, site shows `https://` and the correct college domain.
2. Cafe Wi-Fi, site shows `http://` and asks for net-banking details.
3. Padlock present, but the name in the address bar is a misspelt bank.
4. Browser warning: certificate is not trusted, and the page asks for UPI PIN.

Suggested direction: (1) Yes, path is protected and name matches. (2) No, open HTTP. (3) No, wrong identity. (4) No, identity check failed.

---

## What the Browser Does When You Open a Page

DNS and HTTPS are not floating ideas. They run **inside a sequence** that the browser starts every time you press Enter.

### The Browser as a Network Client

- **Official Definition:** A **web browser** is a client program that takes a URL, talks to the network, and turns the response into a page you can read and click.
- **In Simple Words:** The browser is the app that "goes to websites." Internally it is a careful sequence of lookups, secure connections, requests, and display.
- **Real-Life Example:** A travel desk: you say the hotel name, the desk finds the address, calls on a private line, asks for the tariff, and writes the answer on a slip for you.

### One Address Bar, Many Hidden Steps

When you enter `https://www.example.com/results`:

1. The browser **reads the URL**: scheme (`https`), name (`www.example.com`), path (`/results`).
2. It uses **DNS** to turn the name into an IP address.
3. It opens a connection to that IP (think of it as starting a phone call).
4. It completes the **HTTPS** (TLS) handshake so the call is encrypted and the certificate is checked.
5. It sends the **HTTP request** for `/results`.
6. It receives the **response** and **renders** the page (text, layout, images).

| Piece of the URL | Example | What the browser learns |
|---|---|---|
| **Scheme** | `https` | Use a secure conversation |
| **Domain name** | `www.example.com` | Which name to resolve with DNS |
| **Path** | `/results` | Which page or resource to request |

You only see the last step. Internally, naming, addressing, security, and request–response all happened first.

![What the browser does when you open a page — six steps from reading the URL, DNS to IP, opening a connection, HTTPS lock and certificate, sending the request, and rendering the page, with HTTP as an open postcard versus HTTPS as a locked envelope](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitreict-se-2606/masterclasses/sessionmc3/sessionmc3-05-https-browser-sequence.png)

One page is often **many** requests, not one. The first response may be only the skeleton of the page.

The browser then requests images, layout files, and scripts. Each of those is another short request–response trip. A "page load" in daily language is a bundle of jobs.

### Tabs, Cache, and Why Pages Feel Instant

- **Tabs** are separate page contexts. One tab can wait on a slow server while another tab stays usable.
- **Cache** is a local copy of files the browser already downloaded. Repeat visits feel faster because some responses are reused.
- Cache can also confuse you: you might see an *old* page until you refresh. The network path is fine; the browser reused a stored response.

After login, the server still needs a way to recognise *you* on the next request. The browser may store a small token (often called a **cookie**) and send it with later requests.

That is not magic memory inside the page. It is the client carrying a ticket so the server can continue the conversation.

**Need:** If you treat the browser as a TV that "just shows channels," every spinner and warning will feel random.

**Logic:** Browser internals are the student-facing view of everything in this session: isolated software cannot do this sequence; networked software must.

### Activity: Narrate the Address Bar

Write a six-line story of opening your college site or a news site, using these words once each: **URL**, **DNS**, **IP address**, **HTTPS**, **request**, **response**.

If one word is missing, that step is the one to revise before you close the notes.

When a page later "does not load," this six-word story is your checklist. Name, number, lock, ask, answer — find which word failed.

---

## Key Takeaways

- Modern products connect **users**, **servers**, and **services**. The **internet** is the shared path that makes that possible; it is not an optional extra around a single file.
- Fully **isolated systems** fail when data must be shared, when a second device appears, when a disk dies, or when a payment or OTP service is required.
- Networked software talks in **request and response**. The client asks; the server answers; the internet carries both.
- A request **travels** as **packets** via routers and an ISP to an **IP address**. A working Wi-Fi hop is only the start of the path.
- **DNS** maps human **domain names** to machine addresses. **HTTPS** encrypts the conversation and helps verify the server. The **browser** runs this sequence every time you open a page.

You will use this model in later work whenever an app "cannot reach the server," a login warning appears, or a page is slow. Algorithm skill tells you how hard the server works. Internet skill tells you whether the question even arrived.

---

## Important Commands, Libraries, and Terminologies

| Term | What It Means | Analogy |
|---|---|---|
| **Internet** | Worldwide network of networks that exchange data | Public road system for computers |
| **User** | Person (and their device) using the product | Traveller at a ticket window |
| **Server** | Machine/program that waits for requests and replies | The ticket counter and its ledgers |
| **Service** | Helper system (SMS, payment, email, maps) | A specialist desk the counter calls |
| **Isolated system** | Software with no network, all data on one machine | One paper register on one desk |
| **Client** | Program that starts the request | Customer at the counter |
| **Request** | Structured question from client to server | "Is this train running today?" |
| **Response** | Structured answer from server to client | Clerk's yes/no plus details |
| **Browser** | Client that fetches and displays web pages | Travel desk that calls and writes a slip |
| **URL** | Address you type: scheme, name, path | Full instruction: how, whom, which page |
| **Scheme** | The `http` or `https` part of a URL | "Send a postcard" vs "send a sealed envelope" |
| **IP address** | Numerical network address for a machine | Flat / block postal address |
| **Packet** | Small addressed chunk of a larger message | Numbered postcard in a set |
| **Router** | Forwards packets to the next hop | Railway junction |
| **ISP** | Provider that connects you to the wider internet | Local post office that links to the national network |
| **DNS** | Directory that maps domain names to IP addresses | Phone contacts / directory enquiry |
| **DNS resolver** | Helper that answers "what IP is this name?" | One enquiry desk you ask |
| **Domain name** | Human-readable site name | "Amma" in the contact list |
| **DNS cache** | Recently remembered name-to-IP answers | A number you dialled yesterday |
| **HTTP** | Rules for web request and response | Postcard language |
| **HTTPS** | HTTP over a secure encrypted layer (TLS) | Sealed envelope plus verified sender |
| **TLS** | Security layer that encrypts the path | The lock on the envelope |
| **Certificate** | Credential used to check server identity | Stamp that the branch is genuine |
| **Encryption** | Turning data into unreadable form for outsiders | Sealed cover; middlemen see noise |
| **Padlock** | Browser sign that HTTPS is in use | Visible lock on the door |
| **Cache** | Browser's local copy of earlier files | Photocopy kept on your desk |
| **Cookie** | Small data the browser stores and sends again | A token slip so the counter remembers you |
| **Render** | Turn the response into a visible page | Writing the clerk's answer onto a slip |
)
