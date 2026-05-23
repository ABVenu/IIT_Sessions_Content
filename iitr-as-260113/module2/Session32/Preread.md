# Pre-read: Working with APIs and JSON

## The World Runs on Conversations — Between Software

Think about the last time you ordered food on Swiggy. You tapped a few buttons, and within seconds the restaurant got your order, your payment went through, and a delivery partner was assigned — all at the same time.

You were just using an app. But behind the scenes, **dozens of software systems were talking to each other** — the Swiggy app, the restaurant's system, the payment gateway, and the delivery partner's app. None of these were built by the same team. Yet they all communicated perfectly.

How? Through something called an **API**.

---

## What If You Had to Do It Manually?

Imagine you're building an AI agent that answers user questions. The agent needs to:

- Ask an AI model (like ChatGPT) for a response
- Fetch user data from a database
- Send a message back to the user

Now imagine doing all of this **by hand** — copying data, switching between systems, reformatting every piece of information before passing it along. For one user, maybe manageable. For 10,000 users sending requests every second? **Impossible.**

This is the exact problem that **APIs and JSON** solve. They give software — including your AI agents — a **standard, structured way to talk to any other system**, anywhere in the world.

---

## Meet the Heroes: APIs and JSON

**API** stands for *Application Programming Interface* — but don't let the name scare you. Think of it like a **waiter in a restaurant**.

> You (the customer) don't walk into the kitchen and cook your food. You tell the waiter what you want, the waiter goes to the kitchen, and brings back exactly what you ordered. The API is that waiter — it takes your request, delivers it to the right system, and brings back the response.

And **JSON** (*JavaScript Object Notation*) is simply **the language the systems use to write notes to each other**. It looks like this:

```json
{
  "name": "Riya",
  "city": "Bengaluru",
  "score": 95
}
```

Clean. Structured. Readable — even by humans. This is how every modern app, every AI model, and every agent packages and exchanges information.

---

## How Does It All Fit Together?

Every application — whether it's Instagram, GPay, or a custom AI agent — is built in layers:

| Layer | What It Does |
|---|---|
| **Frontend** | What you see and interact with (buttons, screens) |
| **Backend** | The brain — it runs the rules and logic |
| **Database** | The storage — it remembers all the data |

These layers don't sit in the same room. They talk to each other using **APIs**. Here's a simplified version of what happens when you tap "Place Order" on any app:

```
You tap button
  → Frontend sends API request to Backend
    → Backend queries the Database via another API
      → Database returns data
        → Backend sends API response back to Frontend
          → You see "Order Confirmed!"
```

Your AI agent lives in this exact same world. When it calls OpenAI's model to generate a reply, it's doing the same thing — **sending a structured API request and receiving a structured JSON response**.

---

## In this pre-read, you'll discover:

- **How APIs act as the universal communication layer** between any two software systems — apps, databases, and AI models
- **What REST APIs are** and how HTTP methods like `GET`, `POST`, `PUT`, and `DELETE` map to everyday actions (read, create, update, delete)
- **How JSON structures data** as key-value pairs — and why it feels familiar if you've used Python dictionaries
- **How AI models like ChatGPT are also accessed via APIs** — sending a prompt as a request and getting a reply as a JSON response

---

## A Peek at the Language APIs Speak

When two systems talk via an API, they use **HTTP status codes** to say how the conversation went. You've probably seen these already — you just didn't know their names:

| Code | Meaning |
|---|---|
| `200 OK` | All good! Here's your data. |
| `201 Created` | Done! New record was created. |
| `404 Not Found` | That page/resource doesn't exist. |
| `401 Unauthorized` | You're not allowed in here. |
| `500 Internal Server Error` | Something broke on the server's side. |

Every time your agent makes an API call, it should **check this status code first** — just like checking whether the waiter actually brought your food before you start eating.

---

## What Happens When an Agent Calls an AI Model?

Here's something fascinating — when your agent sends a message to an AI model, it's **not magic**. It's just another API call. Here's the flow:

1. Your agent prepares a **structured JSON request** with the user's prompt
2. It sends a **POST request** to the OpenAI (or Gemini, or any other) API
3. The AI model processes it and sends back a **JSON response**
4. Your agent **reads the JSON**, extracts the reply, and decides what to do next

This means understanding APIs isn't just a backend developer's skill. **It's the core skill for anyone building AI agents.**

---

## Before the Session — Think About This

Here are a few questions to keep in the back of your mind. We'll answer all of them live:

> **1.** Every time you use UPI to pay someone, multiple apps talk to each other in under 2 seconds. How do they all understand each other perfectly despite being built by different companies?

> **2.** When you ask ChatGPT something, is there any difference between how that works and how a weather app fetches today's temperature? (Hint: the answer might surprise you.)

> **3.** If JSON is just a way to write structured data, why can't we just use plain text or a spreadsheet instead? What would go wrong?

These aren't trick questions — they're the exact real-world scenarios we'll trace through in the session. If you walk in curious about even one of them, you'll walk out with answers that change how you see every app you use.

---

*See you in the session — bring your curiosity!*
