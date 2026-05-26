# Pre-read: LangChain Tools: Custom Tools and Tool Calling

Imagine you are using a smart assistant to plan an airport trip. You ask, "Can I leave at 6 PM?" A basic assistant may reply, "Leave early, traffic may be high." It sounds polite, but it is still only a guess.

Now imagine a better assistant. It checks traffic, compares it with your flight time, calculates the travel gap, and then gives a clear answer. It is not only **talking**. It is using real abilities to solve a real problem.

That is the direction modern AI applications are moving towards. A useful assistant should be able to call a calculator, check a database, search a document, contact an API, or validate an input.

But this creates an important challenge: **how do we let an AI use tools without making the system messy, hidden, or unsafe?**

## Why This Matters

Think about an online shopping support bot. A customer asks, "Where is my order?" If the bot simply guesses, the customer may receive wrong information. The correct behaviour is to check the order system, read the current delivery status, and then explain it in normal language.

This is where **LangChain custom tools and tool calling** become powerful. They help us move from an AI that only gives text replies to an AI system that can request specific actions in a structured way.

The key idea is simple: the model does not secretly run anything. It says which tool it wants, what details it wants to send, and why that tool may help. Then the application can inspect the request, run the tool, and pass the result back to the model.

This makes the system easier to trust because developers can see what the model asked for and understand what happened if something went wrong.

## Think Of A Restaurant

Imagine a busy restaurant during dinner time. A customer tells the waiter, "I want a masala dosa and filter coffee." The waiter does not cook the food. The waiter understands the request, writes a clear order, and sends it to the kitchen.

The kitchen prepares the order and sends it back. The waiter then serves it to the customer in a friendly way.

In this analogy, the **AI model** is like the waiter. The **tool** is like the kitchen. The **tool call** is like the written order that clearly says what needs to be done.

If the order is unclear, the kitchen cannot prepare it properly. If an item is not available, the waiter must handle that situation sensibly. In the same way, an AI application must handle tool selection, tool inputs, tool results, and tool failures.

This is the heart of tool calling: the model plans, the application executes, and the final answer is created after the tool result comes back.

## The Concepts You Will Meet

You will learn how to define a **custom tool**. A custom tool is a specific ability created for the AI system. It may calculate something, look up information, transform data, or call an external service.

You will also meet **@tool**, which is a LangChain way of marking an ability as available for the AI system to request.

Next comes **bind_tools**. Binding tools means giving the model a selected list of tools it can ask for. The model must choose from the approved options.

Then you will inspect **tool_calls**. A tool call is the model's structured request to use a tool with certain details. Developers can inspect this request and understand the model's intended action.

After the tool runs, its output must be returned to the model properly. That is where **ToolMessage** comes in. It carries the tool result back into the conversation.

You will also explore **error handling**. Real tools can fail because an API is unavailable, information is incomplete, or an argument is incorrect. A strong system treats these issues as recoverable signals, not instant disasters.

In this pre-read, you'll discover:

- **Understand** why AI assistants need tools instead of only text generation.
- **Discover** how a model can request a tool in a structured and inspectable way.
- **Learn** how tool results are passed back into the conversation.
- **Recognize** why graceful error handling is important for reliable agentic systems.

## What You Will Be Ready To Do

After this topic, you will start seeing AI applications differently. A chatbot is not just a box that replies with text. It can become a controlled system that plans, requests tool support, receives results, and explains the answer clearly.

You will be ready to:

- Design small tools with clear names, input types, and descriptions.
- Explain why tool descriptions affect the model's tool selection.
- Build a manual loop where the model requests a tool, the tool runs, and the model gives the final response.
- Handle tool failures in a way that keeps the user experience stable.

## Why It Is Important For Agentic Systems

Agentic systems need more than long prompts. They need controlled abilities, reliable execution, useful traces, and safe recovery when something goes wrong.

This matters in real projects because business data, user records, calculations, search results, and APIs usually live outside the model. Tool calling gives the model a clean way to request those resources and gives developers a clean way to control the request.

Once this idea becomes clear, advanced AI workflows become easier to understand. Tools, memory, retrieval, evaluation, and automation all become parts of one bigger system where the model does not do every job alone.

## Questions To Carry Into The Session

- If two tools sound similar, how can the model choose the right one?
- What should happen when the model chooses the right tool but sends weak input?
- How can a tool failure become a helpful recovery message instead of a crash?
- How can traces help developers diagnose tool-selection and argument problems?
