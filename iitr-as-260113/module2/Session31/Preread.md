# Pre-read: Evaluating and Improving RAG Systems

Imagine you order a pair of shoes from an online store. Before buying, you ask the website assistant a simple question: "Can I return this if the size is wrong?"

The assistant replies confidently, "Yes, you can return it anytime within 90 days."

That sounds helpful. But what if the actual company policy says returns are allowed only within 7 days? Now the customer may feel cheated, the support team may receive complaints, and the business may lose trust. The problem is not just that the assistant gave a wrong answer. The bigger problem is that it gave a wrong answer with confidence.

This is one of the most important challenges in AI products today. Building an AI assistant is exciting, but making it reliable is what makes it useful in the real world.

In the last few sessions, you worked with a **RAG assistant** for an e-commerce use case. **RAG** means **Retrieval-Augmented Generation**. In simple words, it is a system where the AI first searches for useful information from **business documents**, such as return policies, shipping rules, or product details, and then uses that information to answer the user.

But here is the interesting part: just because a **RAG system** is working does not mean it is working well.

It may **retrieve** the wrong policy. It may miss the most important paragraph. It may answer from memory instead of using the **retrieved content**. It may mix two policies together. Sometimes, it may even create an answer that sounds correct but is not supported by the company documents. This kind of unsupported answer is called a **hallucination**. In simple English, the AI is saying something without proper proof.

That is why this session is about **evaluating and improving RAG systems**.

## Why This Matters

Think of a **RAG assistant** like a customer support executive sitting with a big policy manual.

If a customer asks, "When will my order be delivered?", the executive should not guess. They should open the correct page, read the shipping policy, and answer based on that. If they open the returns page by mistake, the answer will be useless. If they read only half the rule, the answer may be incomplete. If they ignore the manual and answer from memory, the business is taking a risk.

A **RAG system** works in a similar way.

The **retriever** is like the person searching the manual. The **generator** is like the person explaining the answer to the customer. For the final answer to be reliable, both parts must work well. The system must find the right information, and then it must speak only from that information.

In **production AI systems**, this is not optional. A shopping assistant, banking chatbot, HR policy bot, legal helper, or healthcare support tool cannot simply "sound smart." It must be checked, measured, improved, and monitored again and again.

## The Real Challenge

Let us say your e-commerce assistant has access to these company policies:

- Return and refund policy
- Shipping and delivery policy
- Product warranty policy
- Cancellation policy
- Payment and offer rules

Now customers start asking real questions:

- "Can I return a damaged item after 10 days?"
- "Is express delivery available for furniture?"
- "Will I get a refund if I cancel after shipping?"
- "Can I exchange a product bought during a sale?"

These questions are not always direct. They may involve multiple conditions. The system must understand what the customer is asking, **retrieve** the correct **policy sections**, and give an answer that is clear, accurate, and **grounded**.

**Grounding** means the answer is based on the retrieved business information, not on random guessing.

This is where **evaluation** becomes powerful. Instead of just asking, "Did the AI give an answer?", we ask better questions:

- Did it retrieve the correct policy?
- Did it ignore irrelevant information?
- Did it answer exactly according to the policy?
- Did it avoid unsupported claims?
- Did it explain the answer in a useful way for the customer?

Once we can identify where the system is failing, we can improve it step by step.

## How We Improve a RAG System

Improving a **RAG system** is a bit like improving search results in an online shopping app.

If you search for "black running shoes" and the app shows formal shoes, sandals, and socks, the problem is not the payment page. The problem is **search quality**. Maybe the product tags are weak. Maybe the ranking is poor. Maybe the app is showing too many unrelated results.

In the same way, if a **RAG assistant** gives a poor answer, we need to check where the issue started.

Sometimes the document **chunks** are too large. A **chunk** is a small piece of text created from a bigger document. If the chunk is too large, it may contain too many mixed ideas. If it is too small, it may miss important context. So we may change the **chunk size** and **overlap**. **Overlap** means keeping a small repeated part between two chunks so that the meaning does not break suddenly.

Sometimes the assistant retrieves too few results. If we ask it to look at only one policy section, it may miss another important section. This is where **top-k tuning** helps. **Top-k** simply means how many matching pieces of information the system should bring back. A higher number may give more coverage, but also more noise. A lower number may be precise, but may miss useful information.

Sometimes the system needs **metadata filtering**. **Metadata** means extra labels added to information. For example, one policy chunk may be labelled as "returns," another as "shipping," and another as "warranty." If the user asks about delivery time, filtering by shipping can help the system avoid unrelated return policy content.

Sometimes the **prompt** needs improvement. The prompt is the instruction we give to the AI model. For a policy-based assistant, the prompt should clearly say: "Use only the **provided context**. If the answer is not present, say that the policy does not provide enough information." This reduces **hallucinations** and makes the assistant more trustworthy.

## What You Will Learn

In this pre-read, you'll discover:

- How to identify weak or incorrect answers from a **RAG assistant**.
- How to understand whether the system **retrieved** the right **policy sections**.
- How to detect **hallucinations** (confident answers without proper support).
- How **chunking**, **top-k tuning**, **metadata filtering**, and **prompt design** can improve answer quality.

## What Happens After Building

A common beginner mistake is thinking that once the chatbot gives responses, the project is complete. In real companies, that is only the first milestone.

The next stage is **testing**. Teams create realistic customer questions and compare the answers with the actual business rules. They check whether the AI is accurate, whether it missed key information, and whether it is safe to show to customers.

Then comes improvement. If the assistant is weak on return-related questions, the team may improve return policy **chunks**. If it gives long and confusing answers, the **prompt** may be refined. If it retrieves too many unrelated sections, **metadata filtering** may be added. If users keep reporting bad answers, that **user feedback** becomes a signal for the next improvement cycle.

This is called **continuous evaluation**. It means the system is not improved once and forgotten. It is monitored and refined over time, just like how apps receive updates after users start using them.

## What's Next

After this session, you will be able to:

- Test a **RAG assistant** using realistic customer queries.
- Separate **retrieval** problems from **response-generation** problems.
- Improve answer quality using **chunking**, **retrieval tuning**, and better **prompts**.
- Explain why **production AI** systems need regular **evaluation** and **feedback loops**.

You will also start thinking like an AI product builder, not just someone who connects tools together. That mindset is important because real users do not care how advanced the system is behind the scenes. They care whether the answer is correct, helpful, and trustworthy.

## Interesting Questions for the Live Session

In the main session, we will work through questions like:

- If an assistant gives the right final answer but **retrieves** the wrong **policy section**, should we call the system successful?
- How do we decide whether increasing **top-k** improves quality or only adds more confusion?
- What should the assistant say when the company policy does not contain enough information to answer the customer?

By the end of the live class, you will see how small, practical changes can make a **RAG assistant** much more reliable. The goal is not only to build an AI system that answers. The goal is to build one that answers with **evidence**.
