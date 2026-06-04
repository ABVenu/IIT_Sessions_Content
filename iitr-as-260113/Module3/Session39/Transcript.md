0:00

Thank you.

0:30

Thank you.

1:00

Thank you.

1:30

Thank you.

2:00

Thank you.

2:30

Thank you.

3:00

Thank you.

3:30

Thank you.

4:00

Thank you

4:30

Thank you

5:00

Thank you

5:02

Thank you

5:04

Thank you

5:06

Thank you

5:08

Thank you

5:10

Thank you

5:12

Thank you

5:14

Thank you

5:16

Thank you

5:18

Thank you

5:20

Thank you.

5:50

Thank you.

6:20

Thank you.

6:50

Thank you.

7:20

Thank you.

7:50

Thank you.

8:20

Thank you.

8:50

Thank you.

9:20

Thank you

9:50

Thank you

10:20

Thank you

10:22

Thank you

10:24

Thank you

10:26

Thank you

10:28

Thank you

10:30

Thank you

10:32

Thank you

10:34

Thank you

10:36

Thank you

10:38

Thank you

10:40

Thank you.

11:10

Thank you.

11:40

Thank you.

12:10

Thank you.

12:40

Thank you.

13:10

Thank you.

13:40

Thank you.

14:10

Thank you.

14:40

Thank you

15:10

Thank you

15:40

Thank you

15:42

Thank you

15:46

Hi,

15:50

Hi,

15:52

Hi,

15:53

Hi,

15:54

everyone

15:56

Good evening

15:57

Good evening.

15:58

Good evening.

16:16

Am I audible to all of you?

16:20

Am I audible?

16:21

Okay, good evening everyone and welcome to the class.

16:26

Let's wait for two, three minutes.

16:28

We'll start in a couple of minutes.

16:30

We are waiting for more people to join and then we'll get started.

16:46

Thank you.

17:16

Thank you.

17:46

Thank you

18:16

Thank you

18:46

Thank you

19:16

Thank you

19:46

Thank you

20:16

Thank

20:18

you

20:46

Thank you.

21:16

Thank you.

21:46

Hi, everyone.

21:49

Hi, everyone.

22:16

to the session we can start in a couple of minutes people are joined still so you can start

22:23

welcome yeah so maia the strength is a bit less today yeah we can wait for a couple

22:30

of minutes yeah we'll start in one minute at 8 10 sure yeah

22:46

Thank you.

23:16

Yeah.

23:23

Hi, everyone.

23:25

So let's get started.

23:43

First of all, everyone, good evening and welcome.

23:45

And welcome to the class.

23:46

So in today's class, everyone, okay, first before I give you the agenda for the class,

23:51

can you tell me what we have done in the last, maybe two to three, three, four classes,

23:56

what we have been constantly doing in last three four classes, what we have been learning

24:03

in last three to four classes, what are we trying to do?

24:08

We are trying to build what we are trying to build, we are trying to build agents, correct?

24:14

We are trying to build agents.

24:15

We are trying to build agents.

24:16

using Lanchine framework.

24:18

Okay?

24:19

Then everyone, we built agents with, let's say,

24:23

with tools, without tools.

24:25

We built Lanchine expression language,

24:27

simple agency application with database,

24:30

fake database, etc.

24:32

Right?

24:33

And in the last class, everyone, we built multiple tools.

24:36

Remember that?

24:37

With at the rate tool annotation,

24:39

then we saw multiple ideas about tool execution.

24:43

Sorry.

24:45

Like,

24:46

agent executor and whatnot.

24:48

Just give me a second.

24:50

Everyone, clear?

24:54

So we built agents in the last class with multiple tools, right?

25:02

Get, I think if I remember correctly, get order status, get delivery status, and give me delivery

25:09

estimate, timeline, etc., etc.

25:11

And then we saw that we can use agent executor to invoke all of these tools automatically.

25:16

And LLM will decide that which tool it is going to trigger.

25:19

Based on the name of the tool, based on the tool description, and based on its reasoning

25:23

capability, it will decide which tool we need to trigger.

25:27

Correct?

25:28

It can call one tool for a particular query.

25:31

As per the query, it can decide to call two tools, three tools, multiple tools as well.

25:37

Also everyone, for some query, it might not also call any tool.

25:42

Yes or no?

25:43

For some query, it might not also call any tool.

25:45

Yes.

25:46

or no? Correct. So it completely depends on the query whether it wants to make how many tool calls, 0, 1, 2, 3, anyone.

25:52

Right? Now everyone, as of now, whatever we have seen, we have not implemented memory as of now.

25:58

Although in the last class, we saw some idea about messages placeholder. Remember that?

26:03

We saw one idea of messages placeholder. Today, everyone, we are going to dive deep on that.

26:08

So today we are going to implement agents with memory.

26:16

Today we are going to build agents or build agentic AI application with memory.

26:46

using Langchain.

26:56

Is everyone clear?

26:58

So build agentic AI application with memory using Langchain.

27:03

This is what we are going to learn today.

27:05

Everyone clear?

27:06

Now just to get started everyone, what if memory is not there?

27:11

What will happen if memory is not there in the agents?

27:15

Or before even I have.

27:16

ask this question. Let me ask even a simpler question. By default, the tool call that you

27:22

make to LLM, is that stateless or stateful? The default tool call that you make to LLM, right? So,

27:30

for example, let's say if you create an open AI object in Python, and then you make a tool call,

27:34

right? Responses dot create, OpenAI client dotResponses. Create, pass any prompt. And then you make

27:40

another prompt. So for example, let's say in the first turn or in the first request, you ask that

27:45

what is the status of my order ID this? It will give you the status, for example, right?

27:50

And let's say everyone, if you ask same query about track it, right? Something like that.

27:57

Tell me the refund status of it. Will it be able to understand the meaning of it here?

28:01

Will it be able to interpret that in the previous message you have already given the order ID?

28:07

Answer is no. Because by default, the tool, by default, the LLM call is stateless. Okay? So you can say that. A normal LLLL

28:15

call. A normal LM call is stateless, correct? It means that it cannot remember

28:35

the context of the, like, it cannot remember the conversation, it cannot remember the context, right?

28:42

it will not be able to maintain the context. So if you are passing some information in

28:46

a message, then if you want to use the same information in the next message, it will not be able

28:50

to retain that. It will not be able to understand that. Everyone clear? Right? But everyone

28:57

in Langchain, right? In Langchain, do you remember that in the last class, we saw conversational memory

29:05

in Langchain, right? What is the meaning of conversational memory?

29:12

Do you want to maintain the context of the conversation across the, inside one conversation?

29:22

Conversational memory means, what is the meaning of this? Let's try to understand this, right? What is the meaning of

29:27

conversational memory? If you remember everyone in the last class, do you remember that? We saw that something called

29:33

a message is message is placeholder. What that messages placeholder does is, it actually tries to maintain some

29:39

kind of conversational memory. How? We'll see that today.

29:42

detail. But everyone, what happens is with every query, you can, you actually attach all

29:48

the previous messages also. Correct? That all the messages that you are getting and all the questions

29:53

that you're asking to the LLM, to the application, and the answer that you are getting. What happens?

29:59

The answer and the response, the query and the response, Langchain or our agent can maintain that

30:06

at some place. And if you ask third question, with the third question, all the

30:12

previous messages, previous queries and previous responses will also be shared with the third

30:18

query. Then you get the third response. Now, when you pass the fourth query, when you ask the fourth

30:23

query, with the fourth query, the previous message, the previous responses, previous messages basically,

30:29

and the fourth query will be passed. Now, if you do that everyone, if you try to maintain the conversational

30:33

memory in such a way that you are maintaining, let's say, in an array, right, in a list, you are maintaining

30:38

every query and its response. Q1, let's say, query.

30:42

1, response 1, query 2, response 2, query 3, response 3. Now, when you ask query number

30:47

4, if you pass all these messages, all these previous messages, which is query 1, response 1,

30:53

query 2, response 2, query 3 response 3. If you pass these things with query 4, will you be able

31:00

to, will your LM be able to understand the context of the query, of the query number 4? If you are passing

31:06

all the previous messages, tell me a son, if you pass all the previous messages, then yes, it will be able

31:12

to understand this, right? So what happens, everyone? In land-chain, everyone, how do you

31:16

maintain the conversational memory is that you pass the previous messages? Now, when I say everyone

31:24

the previous messages, that means both query and responses, right? Query plus responses also.

31:36

And along with this, everyone, you also pass the current user message.

31:42

current user query. So whatever query, user is currently asking, with that, you pass all

31:48

the previous messages also. Then let's say everyone, if you have some agent prompt, right? Some

31:54

system prompt, right? That you have to pass always, that you are passing every time, right? And

31:59

then everyone you are passing to LLM, and then LLM can take it forward. Is that point clear to all of you?

32:04

So this is the whole idea. That in LL, in LNG, you can actually do this with very simple terms. How we will

32:11

see that in today's class. This is how we can maintain conversational memory. Don't

32:15

you think, everyone, if you are maintaining a list of every query and its response, so don't

32:21

think that is nothing but conversational memory? Within a conversation, if you maintain the every query

32:26

and the response of every query, Q1, R1, Q2 R2, Q3, R3, like that. Don't you think it is nothing

32:33

but a conversational memory only? Correct? Now everyone, we are not going to build a simple chatbot. We are

32:41

going to build a chatbot with agents and with memory. So we are going to build an LLM

32:46

powered application today. LLM powered application with tools. So if you have LLM powered

33:04

application with tools, don't you think this becomes an agentic AI application? But we will also integrate

33:11

memory as well. So today we will introduce the concept of memory as well. Everyone aligned

33:16

till this point of time. So I'm just telling you first of all that what are we going to build

33:20

today? And then it will be easier for you to understand that. Okay. Now everyone, let's start

33:25

about, let's talk about what are the key terms that we are going to focus in today's class while

33:30

implementation and conceptually. First term that we will come across multiple times today is

33:36

message is placeholder.

33:38

message is placeholder. Now what is the meaning of messages placeholder? Let's

33:49

talk about that in detail today. If you remember, we use this in the last class. Correct?

33:53

Okay. So what is this messages placeholder? So guys, it is used inside prompt template.

34:02

First of all. And specifically everyone, it is used inside chat prompt template.

34:17

Okay.

34:22

Used inside chat prompt template.

34:23

template and it is used when used when we want to inject right it is used when we want to inject

34:46

basically in short it is used for conversational memory and when you want to inject a

34:52

previously, previous messages inside the prompt. When we want to inject a list of

34:59

of previous messages into the current prompt, then we use messages, messages placeholder.

35:22

point, folks, yes or no? It is used inside chat prompt template. This is one thing

35:31

that you need to remember. And it is used to inject a list of messages. So basically everyone,

35:36

what messages placeholder does is, internally, it maintains a list of every query and its response.

35:42

Let's say query one, this is the response of query one. This is query two, response of query two.

35:49

Query three, response of query three. So you maintain a list of all.

35:52

the previous messages. Look at this. All the previous messages. Now when you ask the

35:58

question, when you ask the current question, the previous messages will be attached with the current

36:05

prompt. So basically, don't you think everyone, you are giving the context of the conversation

36:09

to the LLM? Correct? With this list of previous messages, don't you think you are providing the entire

36:16

context to the LLM? Yes, no, everyone? In the memory, right? In the, like, you can say that, the program

36:22

execution. For example, Chirag is asking like, where is it stored, the list of messages.

36:28

By default, it will be stored. If you just execute that in the program, for example, when you

36:32

create a dictionary, where that dictionary is stored. For example, in the last class, we created

36:36

a fake database. Where that fake database is stored? In the working memory of the application, correct?

36:41

Correct? In the working memory. And if you restart the application, entire data will be lost.

36:46

Similarly, by default, it will be stored also in the memory. If you want, you can also store this in the database

36:50

for permanent storage. But for now, we'll now.

36:52

you're only going to focus in the memory, the working memory. Is the meaning of messages,

36:57

place, holder making sense to all of you? Okay? Now everyone, when you create a list of previous

37:05

messages, now in this list kind of thing, everyone, right? It is in this list kind of thing. Every

37:11

iteration, don't you think it will have two messages. One is the human message or AI, one is the human

37:17

message, the query that you give, and the prompt and the response that you are getting, which is AI message.

37:22

Okay? So guys, when we say all the previous messages, previous messages means basically the human

37:33

message, the prompt that you are giving. And AI message. Human message and AI message. Is that point clear to all of you? Right? One small.

37:52

in internal detail about messages placeholder, everyone, that messages placeholder actually

37:57

does not store the messages itself. It just creates a place. You can say that messages placeholder

38:04

is like an array. It does not store messages on its own. There are different components for that. I'll

38:09

talk about it. But you can say that messages placeholder is an array inside which the messages placeholder is

38:16

an array inside which these messages will be stored. So it creates a slot. It creates a memory location

38:22

or a list or an array where messages will be stored. Okay? So you can say that

38:26

messages placeholder is a list. Correct, everyone? Now, inside messages placeholder, if you remember,

38:33

we used something called as, uh, just a second even, I'll have to put the charger.

38:38

This is one problem. I don't have the connector now.

38:46

So what I can do.

38:52

screen individually. Yeah. Is the screen visible to all of you now?

38:59

Correct. Sure. Absolutely correct. Now everyone, inside messages placeholder, if you remember,

39:03

we passed something called as agent scratch pad. Remember that? Agent Scratch Pad. Okay. That is

39:10

a variable that we set inside Messages Placeholder. Similar to that, everyone, there are different

39:14

there are different variables that you can set. One of them is called as chat history. So inside

39:21

message is placeholder. You can set the variable called as chat history. What this

39:26

chat history does is, it is, as the name suggestable, it is used to store, store previous

39:34

conversation. And conversation means human message and AI message. Store previous conversation.

39:43

Is that point clear to all of you? It is used to store the previous conversation,

39:47

which is human message and AI message. So for example, let's say chat, chat.

39:51

history looks something like this. So first of all, everyone, it will be a list

39:58

of messages. The first element inside this is let's say going to be something like this. First is human

40:04

message. So again, human message is going to be an object or a class. Okay. And here you

40:11

pass the human message. Let's say the content of this human messages. Let's say whatever query you are

40:17

asking. Where is my order ID this? Okay. Then everyone, what response you have?

40:21

are getting for that. AI message. What response AI is returning? Then again, you will

40:26

have some content here. Is that point clear to all of you? You will get some content here. Similarly,

40:32

next human message and then next AI message and it will keep on running again and again and again.

40:40

Is that point clear to all of you, everyone? Yes or no. Folks clear or not. So you will keep on

40:49

appending. Every human message, AI message. Now everyone, no need to write

40:55

this much. Yeah. Correct. Now everyone, what you can do is while invoking the agent, right? So if you

41:00

remember in the last class, we created agent executor. Correct? We created agent executor. And when we are

41:08

executing this agent, agent executor. Invoke, we pass multiple parameters. Set, return intermediate steps

41:17

is equal to true, verbose is equal to true, right? Max iterations is equal to three,

41:21

and whatnot. You pass a lot of things. One more parameter that you can pass inside agent

41:26

executor is chat history. Right? You can pass this chat history here. This chat history

41:33

you can pass here. Is that point clear to all of you? Correct or not, everyone? This is how you

41:41

can pass chat history. Okay? I will give you the demo of all of them. Don't worry. We will

41:47

everything inside the code as well. Then the next thing that comes everyone is, which we have seen

41:51

already in the previous class, which was agent scratch pad. Can someone remember the, can someone

41:57

tell me the meaning of agent scratch pad? What did I explain in the last class? Agent Scratch Pad?

42:11

First of all, it is not same as chat history. Okay?

42:17

Obviously, the name is different, task is different. It is not same as chat history.

42:23

What chat history is storing everyone? Chat history is storing the previous messages.

42:28

Previous conversation messages, right? Chat history stores the previous conversation history.

42:34

But agent scratch pad, it stores, if you remember, I said that, it stores the tools behavior,

42:41

agent's behavior, correct? What tool are being called, which agent is being triggered, etc, etc.

42:46

So what agents scratch?

42:47

does is it stores, it stores the agent's current turn, agents current turn, agents

43:02

current turn and work. Current turn, whose current turn is this? Because there might

43:10

be multiple agents and their work. What tool they are calling? What tool they are calling? What work

43:16

they are doing basically intermediate steps. Correct? It helps you to get intermediate

43:21

steps. So let's say Agent 1 is calling tool 1. Agent 10 is calling tool 4. So all these things

43:26

are stored inside agent scratch pad. Does that make sense to all of you? Okay. Now everyone,

43:32

if I say, if you are creating a tool calling agent, will you prefer chat history or will you

43:40

you prefer agent scratch pad? For tool calling agent, generally scratch pad is used. Generally, agent scratch pad is used? Generally, agent scratch pad is used. Because in tool calling agent,

44:10

calling agent everyone, you need to maintain which tool is being called, which tool is calling

44:14

which agent, correct, and so on. So you need to maintain that. Everyone, clear?

44:18

clear? Okay. Now I think everyone, we can start implementing the concept. So agent scratch pad,

44:30

we have already seen in the last class. I will again give you a small demo for that. But the main focus

44:34

is going to be the chat history. We will see that how does the chat history actually works. Our tool

44:39

outputs stored in it. By default, not. If you want, you can store it. Not in the agent

44:43

scratch pad separately. Because agent scratch pad, it is in the working memory. If you want something

44:48

to be stored permanently, then you will have to integrate database separately. You'll have to

44:53

integrate database that whatever output is coming, I will store that in the database so that it will

44:57

persist permanently. Does that make sense, Chirac? Does that make sense, everyone? Okay. Now let's

45:07

move to the implementation folks.

45:09

Let me share my screen.

45:20

Okay, so we will open the same folder.

45:37

Open folder. And we are writing, I think, our code in Langchain app, right? Yeah.

45:44

So Langchain app. So here, we are writing the folder. We are writing the code here. And today we will

45:49

write, we will create a new file here. I have one doubt the where does the scratch pad exist? Like

45:55

in which layer, application layer? Okay. So these variables like chat history, etc. By default,

46:00

they are in the application layer. For example, let's say if you are, we are going to write an

46:03

application, right, some file, dot p.pythin file. Now, once you, once you,

46:07

stop the code once your code execution gets completed. Now, when you're going to execute the

46:12

next time, do you think that the previous messages will be there? Like whatever you stored in the chat history?

46:18

Do you think so? That the previous messages will be there? No, right? The previous messages will not be there.

46:26

Because what happens is, by default, all of these things are happening in the application layer.

46:31

And once you restart the application, everything gets restarted. So by default, they are in the RAM.

46:35

Now, if you want to store them permanently in the database, you will have to implement database.

46:39

You will have to use database. Makes sense, Sankethe? Yeah. So let's start everyone. So we will

46:49

build a new application today. And the application is, let's say, lanchained agent with memory.

46:56

.py.

47:05

what are we going to build? Let's say build a small agent. Now because we are going to build

47:14

a agent with memory, built a small agent with memory. This is very important. Build a small agent

47:22

with memory. Who can? Which can remember the order ID, let's say, order ID.

47:35

shared by the user in the previous messages. Correct, everyone? Correct. Now, the agent can call

47:56

a order status checking, order status tracking tool. So there is a tool that we are going to implement, just like the previous class.

48:04

then agent can understand the user query and should be able to call the tools

48:21

based on the query. Correct, everyone. Okay? And most importantly, we will compare.

48:34

Compare both with memory and without memory scenarios. Then only we will be able

48:42

to see that. What is the significance of memory? As of now, we have always seen these things

48:47

on nodes while like theoretically. Today we will see the demo. Compare both with memory and

48:52

without memory scenarios for the above agent for scenarios for this agent. Is the task clear

48:59

to all of you? So we are going to do a lot of things today, right? A lot of steps we are going to implement.

49:04

Okay. Now let's go to the terminal. Let's install if something is missing. Just to verify

49:10

everyone, I think all the things are already there. So Lanchine, PIP3, install, Lankchain,

49:17

Lankchain, OpenEI, we are going to use OpenEI, then Lanchine Classic. Install all of them.

49:26

Done. Now we will import few things. First of all, also everyone we need to set the API key. So let me

49:34

me go to platform.openAi.com. Let me set the API key. Export OpenAI underscore API

49:41

underscore key is equal to this. API key.

50:04

copy

50:09

Done.

50:10

And now we are going to import all the required libraries.

50:14

So what do we need?

50:16

From Lanchine underscore open A import.

50:21

Chat open EI.

50:23

From Lanchine

50:25

from Lanchine

50:27

Lanchine

50:28

dot prompts

50:34

chat prompt template, import messages placeholder that we just discussed,

50:40

from Lanchine underscore core dot messages, import.

50:47

Now everyone, because now we are going to see, are we going to see, are we going to see the message here,

50:52

see the query here, which can remember the order ID. If you need to remember the order ID,

50:57

you need to maintain the chat history, right? To maintain the chat history, if you see what is

51:01

chat history, the human message, the AI message.

51:04

Correct? So every query will have a response. Query is the AI response,

51:09

query is the human message, response is the AI message.

51:11

Response is the AI message.

51:14

Right?

51:15

So from Lankchain core dot messages, we will import human message and AI message.

51:21

Correct everyone?

51:22

Is that point clear to all of you?

51:25

So these are two classes that we are importing from Lankchain.Messages.

51:29

Then everyone from Lankchain underscore core.

51:33

tools. We will import tool annotation, tool decorator, correct? Then everyone, we will

51:40

import agent executor from Langchain underscore classic dot agents, import agent executor, and

51:50

also import create tool calling agent that we used in the last class also. Is everyone

51:56

clear with all these five, seven things that we have imported? Everyone is clear with this.

52:03

Everyone, clear?

52:07

Then everyone, we will write the first tool, which is create a, create a function, let's say,

52:14

get order status.

52:18

Okay?

52:19

Here everyone, we will pass the order ID, string, it will return string, and we are going to define

52:26

add the red tool annotation.

52:28

This tool annotation will define that, this is a tool, okay?

52:32

Otherwise, this will be a normal function.

52:35

And what this tool does is everyone, it returns the status of the order ID given by the user.

52:52

Now we also need to give one instruction to LLM.

52:55

Use this tool when the user is asking for, asking for the order status.

53:02

or users asking about the order tracking status, order status or whatever,

53:15

okay?

53:16

Now what do we need to do everyone?

53:18

Okay, we need to create a fake database also.

53:21

So either you can create outside or I can create here only.

53:25

I can create a fake database and I can create this as a dictionary where I can.

53:32

have let's say ORD 101 and what is the status let's say status is out for delivery I'm

53:42

just writing a very simple small database right if you remember in the last class I think we

53:45

created a bigger database right just like this so this time we are creating a small

53:49

database or we can copy paste this also right this is also perfectly fine I can copy page

53:55

this also no need to write it again right

54:02

So we have the fake database.

54:04

So what we will do?

54:05

Get the order, orders dot get from order ID, get the order of this order ID and we will see if not order

54:15

then we will simply return that we will simply return.

54:21

Order with the given order ID.

54:32

with the ID, order ID, not found.

54:44

Else everyone, we will simply return, simple thing, we will simply return, let's say, return,

54:54

order, dot, inside this order, let's say, status.

55:00

We will simply return order dot, order.

55:02

status, okay? Order status is this. Is everyone clear? Simple function, everyone. Now, because we are going to talk about the memory today, right? Assume that there is only one tool, right? Because we have already

55:32

already seen multiple tools. Let's say there is only one tool that we are going to use today.

55:36

And the tool is get order status. This is the tool. Get order status. Everyone clear? So in the last

55:42

class, we created three different tools. And in the list, we added three tools. Remember that? If you see,

55:47

tool one, tool two, tool three, and we added three tools in the list, right? Today we have only one tool.

55:54

Everyone clear? Okay. Now we will create LLM. Create LLM. How do we create LLM? How do we create LLM?

56:02

is equal to chat open AI. What do we need to set inside this, everyone? What do we need to set

56:09

inside this? First, do we need to set API key? Mukul? API key, we have already set inside

56:21

environment variable, right? So we don't have to set it again. Right? So we need to set the model.

56:26

Model is GPT 5.2. Let's say GPT 5.2. Correct.

56:32

And if you want, you can set the temperature is equal to zero. That's it. Is the model creation

56:38

clear to all of you? Correct? Now we are going to create a prompt template with message

56:50

messages placeholder. Placeholder. Okay? Let's do that. So prompt is equal to chat prompt template.

57:02

And here we write the prompt. Remember that? In the last class, this is how we wrote.

57:08

Right? Same thing, right? Same thing we wrote. Folks, correct or not?

57:13

Okay. Now, today it is going to be slightly different, right? We are just going to add a few

57:20

more parameters here. First of all, everyone, in this, create a list. First you need to provide the system prompt.

57:32

Okay. The system prompt. What do we need to pass? Let's say we need to pass

57:38

these things. You are a helpful customer support agent. Rules are if a user gives the order ID,

57:44

then you need to remember it for the conversation, correct? If a user ask a follow-up question,

57:49

track it, where is it? What is the status of it? And then use the previous order ID from the chat

57:55

history. Correct? Use tools when order status is required. If no order is available,

58:01

I'll politely ask the user to provide the order status or order ID. This is what we want

58:06

to use. Let me copy pages. Just have a look at it and tell me if this system prompt is clear

58:14

to all of you or not. Just let me know if this system prompt is clear to all of you or not.

58:22

Just read all these lines.

58:31

Everyone clear? This is the system prompt. Correct? Now it won't. See, in the chat prompt template, see what happens? When you are passing the first prompt, the first query, you are initiating the conversation. Will there be any chat history? When you are passing the first query, when you are asking the first query, will there be any chat history? No.

59:01

When you ask the first question, you get the response. Then you ask the second question.

59:05

For that second question, everyone, will you have some chat history where one human message,

59:09

one AI message is there? Correct? You need to maintain that. Now, when you ask the second question,

59:16

don't you think in the prompt of the second question, the first AI message and the first

59:23

human message should also be carried forward, carried forward? Should also be forwarded along with the second prompt.

59:31

everyone, that is why we need to give chat, we need to define chat history here.

59:35

So here, everyone, what we are going to tell is that, okay, inside the prompt, use messages placeholder

59:41

as well. In this messages placeholder, use the variable name, chat history, that I want you to

59:47

maintain chat history. Is that point clear to all of you? Chat history. Okay? Also, everyone,

59:53

there is one more parameter that you need to write is optional. Optional is equal to two. I will come

59:58

back to the meaning of optional. Just for now, you can understand that. As I just discussed,

1:0:03

when you pass the first message, when you ask the first question, will there be any chat history

1:0:09

before that? Will there be any chat history before that? No. It means that chat history can be empty

1:0:17

also. It is not mandatory that always you will have the chat history. If you are asking the first

1:0:21

question, chat history will be empty. That's why we are saying optional is equal to true. I will come

1:0:25

back to this in detail. But is the high level clear?

1:0:28

Is the high level clear?

1:0:31

Okay? Now we need to pass the human message.

1:0:36

Right? Order does not matter, I guess. You can pass in any order. Or we can check this particular thing.

1:0:41

We can verify this. Right? That human query, that what is a human query?

1:0:45

Human query will come in the input parameter, right? This is, we will write in the curly bracket, input.

1:0:51

Everyone clear?

1:0:51

Here, human query is not hard coded. It will come in the...

1:0:58

Is everyone clear? Yes or no?

1:1:08

What is this? Very difficult syntax to remember.

1:1:12

If you see in the last class, everyone, it was slightly simpler.

1:1:16

We gave the chat message, we gave the human input, and then we just gave the agent scratch pad.

1:1:21

In the previous to previous class, we did not even use scratch pad.

1:1:25

Right? So this is how we are evolving.

1:1:27

Every class, we are diving deep into one new concept.

1:1:30

Last two classes, two three classes back, we just gave system prompt and human prompt.

1:1:36

Remember?

1:1:38

Remember?

1:1:38

Then in the last class, previous class, Monday co, we started building tool calling agents.

1:1:44

For tool calling agents, we need agent scratch pad also.

1:1:47

That agent scratch pad stores the information or the intermediate steps

1:1:51

about the tools, what tool is doing, what input they are getting, what output they are

1:1:55

returning, what error they are returning, etc. Today we are adding one more thing, which is the chat

1:2:00

history as well. But everyone now tell me, if you have a tool calling agent, is this agent

1:2:05

also going to call the tool? Do you still have a tool call in the current agent also that we are

1:2:10

building today with memory? Tell me, do you have a tool here as well? Yes, we have tool here

1:2:16

as well. So don't do you think, everyone, you need a tool calling. You need a tool calling. You

1:2:21

we need to store tool information also in agent scratch pad. So we will copy, we will add the same

1:2:26

thing, message placeholder with variable name agent scratch pad. Agent scratch pad. So do you see that

1:2:34

now? We have agent scratch pad as well and we have chat history as well. Both of these things we are

1:2:39

using here. Folks clear? Okay? So folks, let me just write a small comment here that converse a previous

1:2:51

of the conversation will be inserted in the chat history. Okay? And agent scratch pad

1:3:04

is used for what? Add a comment here. Let's say tool calling agents intermediate steps will be maintained or will be stored here. Is that point clear to all of you?

1:3:19

So, folks, please be attentive and give me yes or no, if this is clear. We are going

1:3:25

very slow, right? Because these things you are learning for the very first time. And small, small

1:3:30

terms, once you understand it, you will never ever forget about it, right? Okay. Now once the

1:3:36

LLM is ready, the prompt is ready, what do you need to do now? The last step. If the tool is ready,

1:3:43

if the LLM is ready, if the prompt is ready, you need to create the agent. So finally you can,

1:3:49

create the agent, create tool calling agent. And in this tool calling agent, right?

1:3:57

In the chat history or in the agent scratch pad, you are asking about agent scratch pad,

1:4:02

in the agent scratch pad, you say that let's say there are 10 agents. So agent scratch pad will

1:4:08

maintain agent one is calling tool one. This is the input. This is the output. Agent 4 is calling, let's say,

1:4:15

tool 5. This is the input. This is the input.

1:4:19

Okay? So now we are going to create an agent with the function, create tool calling agent.

1:4:24

In the last class also, we did the same thing. See, tool calling agent. So we will pass LLM,

1:4:29

we will pass tools, we will pass prompt. Same thing, exactly same thing, right? LLM is equal to

1:4:35

LLM, prompt is equal to prompt. Tools is equal to tools. Everyone clear? Right? And

1:4:46

finally when we are going to create agent executor.

1:4:49

executor is equal to. So you have, as of now, you have created an agent, till line number

1:4:56

83, you have created an agent. Now you are, you need to create an executor who will allow us to

1:5:03

execute the agent. Is that point cleared all of you? Correct. Put here, we have only one agent.

1:5:14

So don't we think you need to maintain for one agent also, that in, see, one agent and one tool.

1:5:19

Correct. Now, again, it is not mandatory. It is optional. It is good to have.

1:5:25

Right? But even if one agent fails somewhere and you want to check the intermediate steps,

1:5:30

how will you check it? If you have this information, then only the intermediate steps will be maintained,

1:5:34

right? Then only you will be able to check if something goes wrong. If you want to debug the issue.

1:5:40

Correct? That's why. But this is completely optional. It is not required.

1:5:46

Okay? Now everyone, in the agent executor, if you remember, we gave lot of things, agent.

1:5:49

tools, verbose, max iterations, handle parsing errors, return intermediate steps.

1:5:55

You can pass all of them. But for simplicity today, I will pass today, let's say, first of all, I will

1:6:00

give the agent, I will give the list of tools. And let's say I can give verbose is equal to true.

1:6:06

Otherwise, this is also optional. Okay. Otherwise, this is also optional. If you want to try for

1:6:11

other parameters like max iterations, if you want to try for handle parsing errors, if you want

1:6:17

to try for return intermediate steps. You can set them, right? For all of them, we have

1:6:21

saw that, we saw the demo in the last class. Correct? Folks, clear or not? Now we are going

1:6:28

to execute this. Okay? Now we are going to execute this. Let's see. So, response is equal to,

1:6:36

agent executor. Dot invoke. And while invoking everyone, in the last class, what did we provide?

1:6:44

We just provided input query.

1:6:47

Correct or not? We provided input query. Fokes clear. So we will provide input query.

1:6:55

And what is the input query, everyone? Whatever let's say user input is coming. Maybe let's say the

1:6:59

user input is coming as something like this. Let's say maybe. Okay, this is going to be a JSON object.

1:7:05

Okay. Input queries high. Let's say.

1:7:17

Let's do one thing. Let's not hardcoded. Because I would want to give you a proper demo.

1:7:25

So let's do one thing, everyone. Let's add a variable here. Let's say we will get this input from the user.

1:7:31

Because everyone, if you just give one, if you hard code it, will you be able to check that whether

1:7:35

it is maintaining the history or not? Whether it is remembering the order ID or not?

1:7:41

No, right? Now everyone, would you want to see the chat history? That how chat history is being,

1:7:47

maintained by the, you can say that, maintained by the, you say that message placeholder.

1:7:54

Do you want to see that? If you want to see the chat history also, what you can do is you can create

1:7:58

an array, chat history array, name could be whatever you want, and create it empty.

1:8:02

Okay? Now, if you create a chat history, and here you can pass another parameter, that because I

1:8:09

want to remember the chat history also, chat history, and this is the array in which I

1:8:17

want to maintain the chat history. Name could be whatever does not matter, right?

1:8:21

because you have said name here chat history, this is what matters. Here you cannot pass anything

1:8:24

random because this is the variable name. But here, you say that okay, chat history I want to maintain

1:8:30

in this array. I want to maintain in this list. Is everyone clear? Okay? And let's say everyone,

1:8:38

you get answer or let's say you get from this response, you print, you print from this response.

1:8:47

This response will have multiple things. I just want to print the output from this response.

1:8:52

Response say, give me the output. How many if you're clear till this point of mind? Now we are going

1:8:56

to execute this.

1:9:01

Okay. So what I can do everyone is I can write this inside a function. Let's say define.

1:9:17

Ask agent. And here you will provide the user input, which is going to be type of,

1:9:31

let's say, string. And all the code you can copy paste here. This is the chat history. That history,

1:9:36

you can maintain globally also outside the function.

1:9:47

Fine. And then everyone, you will print it. Is everyone clear with the simple function?

1:10:00

Is everyone clear with the simple function? Okay. Now everyone, what we are going to do is we are going to, let's say, run agent on multiple turns. Multiple turns. So what you will do everyone is, first you will give turn one.

1:10:17

Okay. And you can print that, print, let's say. This is turn one. And in turn one,

1:10:26

everyone, what you're doing is you are giving user underscore input is equal to something, let's say,

1:10:32

hi. Maybe let's say my order ID is, let's say, take any order ID, 1.02.

1:10:41

My order ID is 102, right? And you say that, then you call this function.

1:10:47

Let's say. Now if you want to print what, you want to print the user input. Let's say,

1:10:57

user input. What user input is coming? And then you want to print the AI response. What response

1:11:07

is coming from AI? Response coming from AI. Right? Now actually what you can do is instead of

1:11:16

printing this, you can return this.

1:11:23

Okay? Let's say everyone ask agent, is calling the agent, invoking the agent,

1:11:28

whatever response is coming, it is returning it.

1:11:31

Why we are invoking agent executor in line 98, it should automatically be invoked. How it will

1:11:36

automatically invoke? Shim, did you attend the last class? I think you were there, right?

1:11:42

It's like agent never invokes automatically.

1:11:47

Tool will get automatically invoked based on your query.

1:11:51

Agent is something that you have to start.

1:11:53

Correct? In the last class also, if you see we created an agent, take care, we created an agent,

1:11:58

then we created an executor and then we invoked the agent via executor.

1:12:04

Correct? So what you do is you are creating an agent.

1:12:07

Then if you don't execute it, it will not magically run.

1:12:12

You will have to invoke the agent and once you invoke the agent, it will make a call to the

1:12:18

LLM and then it can tell, LLM can tell which tool to call.

1:12:22

Then agent can make a tool call automatically.

1:12:25

Tool call can happen automatically once the agent is running.

1:12:29

But agent will not be invoked automatically.

1:12:32

Clear or not?

1:12:33

Clear?

1:12:34

Clear?

1:12:35

Okay, very good.

1:12:36

Now everyone, I'm just trying to do this.

1:12:39

So for every user query if you see, I am calling the

1:12:42

agent and whatever response agent is returning, I will print it.

1:12:45

So let's say this is the AI response and this is the user input that we are passing here.

1:12:50

So if the turn one, are these four lines of code clear to all of you?

1:12:56

Are these four lines of code clear to all of you?

1:13:00

Then everyone I will have multiple search terms.

1:13:03

Print, let's say, just a separator everyone.

1:13:06

I want to separate the output and also add a new line operator.

1:13:10

And then what I will do everyone?

1:13:11

I will do this for turn 2 as well, copy paste.

1:13:14

This is turn number 2, okay?

1:13:17

For turn number 2 everyone, let's say my task is, my query is, in the first turn I have given my order

1:13:23

ID, in this, in the second query, in the second turn I say that, where is it, where is it now?

1:13:29

That's it, okay, where is it, okay?

1:13:33

Or what's the status of it, not?

1:13:38

What is the status of it?

1:13:41

tell me in the second turn, am I telling my order ID?

1:13:45

Am I telling my order ID?

1:13:47

No.

1:13:48

If the conversation history or the chat history is maintained properly, then my agent should

1:13:54

be able to recognize the meaning of it, correct or not?

1:13:58

Then it should be able to understand the meaning of it.

1:14:00

Because I have already passed the, I have already passed the order ID in the previous message.

1:14:05

Correct everyone?

1:14:09

And then everyone, I think two turns are going.

1:14:11

enough, okay, just to test it.

1:14:18

Folks, everyone clear?

1:14:21

Could you please?

1:14:23

I will have to check the exact syntax for that, that what is actually, where does it store?

1:14:29

I'll check maybe in the break.

1:14:31

Okay, I don't remember exactly what object or what variable name does it exposes to print.

1:14:38

Okay?

1:14:39

Folks, everyone clear with the code?

1:14:40

So, is everyone clear?

1:14:44

Okay.

1:14:45

Now what I'm doing is, I'm giving you some time to go through the code before we execute.

1:14:48

Try to understand, it's 9 p.m also.

1:14:51

Let's take a break at this moment.

1:14:55

When we are learning so intense things, right?

1:14:59

So time does not, like, time flies.

1:15:02

I thought that it is just like 9.30, 9.40.

1:15:05

Now, when I saw the time, it is already 9pm.

1:15:07

I thought it is around 8.30.

1:15:10

Okay. Anyways, everyone. So I will do add, submit, agent with memory. And get push.

1:15:20

So now folks, we will have this.

1:15:35

This is the code everyone, agent executor, agent memory.

1:15:40

Okay, just go through the code everyone. Let's have a break. It's 902. Let's meet around 915,

1:15:46

916. Let's have a 13, 14 minutes of break. Spend 5 minutes on going through the code, reviewing

1:15:51

the code, and for 7, 8 minutes, you can have a break. Okay? See you after the break, everyone.

1:16:10

Thank you.

1:16:40

Thank you.

1:17:10

Thank you.

1:17:40

Thank you.

1:18:10

Thank you.

1:18:40

Thank you.

1:19:10

Thank you.

1:19:40

Thank you.

1:20:10

Thank you.

1:20:40

Thank you

1:21:10

Thank you

1:21:40

Thank you

1:22:10

Thank you

1:22:40

Thank you

1:23:10

Thank you

1:23:40

Thank you

1:24:10

Thank you

1:24:40

Thank you

1:25:10

Thank you

1:25:40

Thank you

1:28:40

Yeah,

1:28:44

Okay,

1:28:48

Yeah, Hi, Hi, Hi, Hi, Hi, everyone, am I am I am I,

1:28:52

Yeah, Hi, Hi, am I am I am I

1:29:02

Hi, everyone, am I audible?

1:29:06

Okay, now let's try to run this code everyone.

1:29:12

So Python 3, 3, land chain agent with memory,

1:29:17

with memory.

1:29:18

.

1:29:19

Should we try to execute now?

1:29:21

folks, yes, no.

1:29:25

Okay?

1:29:26

Let's do that.

1:29:31

So there is some error.

1:29:36

Missing credentials.

1:29:38

I set the API key, right?

1:29:40

Export open AI API underscore key.

1:29:45

Open AI API key, yes.

1:29:50

Let's execute the code now.

1:30:12

Now there is a different problem.

1:30:14

Input should be in the instances of sequence.

1:30:20

One validation error, type input value.

1:30:25

I think the correct thing is here we are getting which line, this line, agent executor, agent executor, I think

1:30:39

input should be an instance of sequence.

1:30:45

You didn't set the parameter.

1:30:49

Oh, guys, this is tools, not tool.

1:30:53

Okay, that was wrong.

1:30:55

List, right?

1:30:57

That was a problem.

1:31:00

Yeah, so if you see, this is turn 1, user ID is, user input is high, my order ID is this, then agency

1:31:10

is saying, what would you like to do next?

1:31:13

Then in turn 2, I say that, what's the status of it?

1:31:17

Now do you see that everyone?

1:31:19

Here, we are not able to see the order ID.

1:31:23

We have enabled these things, but still, what is the AI response?

1:31:28

I can help track it.

1:31:30

Could you share the order ID?

1:31:33

First of all, everyone, do you see that where application is working absolutely fine, application

1:31:40

is executing, but it is still not able to use the chat history.

1:31:44

It is not able to still use the order ID, correct or not?

1:31:48

I have already given the order ID.

1:31:49

but still it is not able to use it.

1:31:51

Why we don't?

1:31:52

Because we have missed one step, right?

1:31:54

We have missed one step.

1:31:55

Can anyone guess what step we have missed?

1:31:58

What step we have missed everyone is?

1:32:02

There is one, you can say that one disadvantage here.

1:32:06

The disadvantage is, see, you are in the messages placeholder, you are saying that I want to use chat history.

1:32:14

But unfortunately, this chat history, messages placeholder will not.

1:32:18

will not maintain automatically.

1:32:21

If you see everyone, you are passing chat history here, absolutely correct, Shoria.

1:32:26

We have to append it.

1:32:27

When, once you pass the chat history here, everyone, you will have to append it.

1:32:32

That chat history dot append, first you have to pass the human message.

1:32:37

That human message.

1:32:38

What is the content of the human message?

1:32:40

The user ID, the user input.

1:32:42

This is the input that we are passing in a human message.

1:32:46

Then everyone, we will have to append the AI message.

1:32:48

A.I. Message.

1:32:50

Right?

1:32:51

AI message is what?

1:32:52

What content we are getting?

1:32:53

This content we are getting as a AI message.

1:32:56

Are you guys getting this point?

1:32:57

Now everyone, this is one disadvantage that if you are using chat history, you will have to maintain,

1:33:03

you will have to keep on appending for every agent run, for every task, for every query,

1:33:09

you will have to maintain or you will have to append chat history manually.

1:33:14

Is that point clear to all of you?

1:33:16

We will solve this problem.

1:33:17

We will see.

1:33:18

way also.

1:33:19

But when you define message placeholder here, it is just, you can say that it is just a placeholder.

1:33:25

It will not store messages automatically.

1:33:27

You are just notifying, you are just telling that, okay, I am going to maintain chat history.

1:33:31

Please make space for it.

1:33:33

Please use it.

1:33:34

So what I will do?

1:33:35

I will pass chat history while invoking the agent.

1:33:38

Is that point clear to all of you?

1:33:40

Now if you do this everyone, now if you execute this, so message placeholder is just allocates.

1:33:48

Absolutely correct.

1:33:49

Message placeholder.

1:33:50

See, what is the meaning of placeholder?

1:33:51

Placeholder is like, let's say you have in school, right?

1:33:55

You must have booked seats just by placing your item.

1:33:59

Correct?

1:34:00

Let's say you place your pencil, you place your pen and you say that this is my place.

1:34:05

So what you are doing, you are putting a placeholder.

1:34:07

That this place is reserved.

1:34:09

This is exactly what placeholder also does here.

1:34:11

Messages placeholder means that you are reserving the memory.

1:34:14

Right?

1:34:15

You are saying that, okay, please allocate the memory.

1:34:17

I am going to put the memory.

1:34:18

messages here.

1:34:19

Everyone clear?

1:34:20

Now once you execute this everyone, let's see now it is going to work or not.

1:34:24

First input is this is my order ID.

1:34:26

Now second turn is what is the status of it?

1:34:29

Now see that everyone.

1:34:31

When the second turn comes, what is the status of it?

1:34:34

Now is it automatically able to call the get order status with order ID 102.

1:34:39

Now it is able to recognize that this is the order ID that user passed in the first message.

1:34:45

Is that point clear to all of you?

1:34:48

This is the status.

1:34:49

Order status is cancelled.

1:34:51

This is how you build an agent with memory.

1:34:55

How many if you are clear with this?

1:34:58

This is how you build an agent with memory.

1:35:03

Okay?

1:35:04

Now everyone, this is the idea of optional is equal to true.

1:35:10

If you don't make optional is equal to true, then chat history will become mandatory.

1:35:15

Then you will have to pass it.

1:35:17

Right?

1:35:18

If optional is equal to true means, optional is equal to true means,

1:35:23

optional is equal to true means, let's say, or you can say that, optional is equal to true makes the chat

1:35:38

history parameter as optional.

1:35:44

Is everyone clear?

1:35:46

Here, folks, please give me some confidence so that I can move forward.

1:35:51

I can give you next example.

1:35:52

Everyone clear with this.

1:35:53

If anyone has an out, you can ask.

1:35:56

So, chat history is working absolutely fine.

1:35:58

How do we decide multi-turn sessions, when does it make sense to store data in the chat history

1:36:04

in a separate database?

1:36:05

Chat histories, generally in the production systems, chat histories are always stored in a database, right?

1:36:10

First, you use it in a session and then you store it in a database.

1:36:13

For example, if you use chat GPT, chat GPT, you can either.

1:36:16

go to any conversation even if you did it two years back.

1:36:20

It means that they are storing your chat history permanently in the database.

1:36:24

Right?

1:36:24

So as per the use case, if you want to have permanent persistence, you can do that.

1:36:29

Okay?

1:36:30

Folks clear.

1:36:33

Now everyone, what I will do is, I will give you an example of this.

1:36:37

I will copy paste this entire code.

1:36:39

I will do this entire code.

1:36:41

And I will create the another example, Langchain.

1:36:46

agent, stateless.

1:36:49

I don't want to maintain history, although I have already given you an example when we did not

1:36:53

append the messages.

1:36:54

Now, if you just want to see the code of this completely, what I will do everyone is, instead of

1:37:00

passing chat history here, instead of maintaining the chat history, instead of appending

1:37:05

to chat history, can I say that just pass empty here?

1:37:10

Just pass empty error here.

1:37:12

Folks tell me yes or no?

1:37:13

Just do this and your agent will become stateless.

1:37:16

you are not maintaining chat history.

1:37:19

Correct or not?

1:37:22

Folks, clear or not?

1:37:24

Correct?

1:37:24

So I have written the code so that you can check later on also.

1:37:27

Do passing the check, chat history mandatory?

1:37:30

No.

1:37:30

Because you are passing, that's the reason.

1:37:32

We are making it optional is equal to true.

1:37:34

If you don't pass optional is equal to true, then it is mandatory.

1:37:38

Then Langchain will raise an error if you don't pass a proper chat history.

1:37:43

Okay?

1:37:44

Yes.

1:37:45

Now, everyone.

1:37:46

We had a complete demo of with memory without memory.

1:37:51

But everyone, don't you think manual appends?

1:37:53

The messages that we are appending manually, do you think that it is a very good idea?

1:37:57

It is a very good approach?

1:37:59

Not really.

1:38:00

No one would want to do that, right?

1:38:02

So everyone, let's build another file.

1:38:06

Lanchine, agent, memory, auto, dot p.y.

1:38:13

Now we are going to use some idea which will build.

1:38:16

help us, right? So you can say that which will help us update the chat history automatically.

1:38:21

This is going to be slightly different code. So you can say that manual append

1:38:27

is maybe is okay for projects, for learning projects, but not good for production applications.

1:38:40

Correct? Correct. Because it is error prone, right?

1:38:46

manual append is prone to errors.

1:38:49

What if, let's say you forget to do that, forget to add the message, prone to errors?

1:38:53

What if everyone, you change the, let's say, you change the order?

1:38:58

Something like that, anything can happen.

1:39:00

And that's why everyone, we have something called there.

1:39:02

There is a new component that we are going to introduce now, which is runable with message history.

1:39:10

So as the name suggests everyone, that you can run the agent with message history automatically.

1:39:15

So this new component is what Lanchine provides us.

1:39:19

Now, what this component does?

1:39:21

Runable with message history, right?

1:39:26

You can say that Lankchain provides,

1:39:30

provides this to automatically,

1:39:40

automatically load the previous messages.

1:39:45

inject them into the prompt and append them into the prompt and append the new user, append the user message and

1:40:15

Don't you think this is what we want, right?

1:40:20

That someone should append the user message and AI message after the response.

1:40:25

And this is what exactly we were doing, right?

1:40:27

That once you get the response, once you actually get the response, you are appending it manually.

1:40:32

I want to do this automatically.

1:40:33

Is that point clear to all of you?

1:40:36

Is that point clear to all of you?

1:40:39

Now what we are going to do everyone is we will copy paste a lot of code from the existing ones,

1:40:43

the what we have already written.

1:40:44

First of all, I will import the same thing.

1:40:45

things. Open AI. I will import open AI, chat open AI. Then I need chat prompt template,

1:40:52

messages placeholder. Then I will, I would need tool. I need human message. I need, now human message

1:40:58

and AI message will not be required because we are not going to use that directly. Now agent

1:41:04

executor will be required. Create tooling agent will be required. A couple of new things will be required,

1:41:09

which is, so do you understand this right? That now I have removed AI message and human message.

1:41:13

Because now we are not going to use them manually.

1:41:15

automatically.

1:41:16

It will happen.

1:41:17

Right?

1:41:18

So from Langchain underscore core dot chat history, I will import something called as in-memory

1:41:27

chat history.

1:41:28

In-memory chat history, even if you see as the name suggests, this is the component where the actual

1:41:34

chat message history is going to be maintained in memory.

1:41:38

In memory means in the working application, in the ramp.

1:41:42

Everyone clear?

1:41:42

Not in the database.

1:41:43

In the working application.

1:41:44

In the working memory.

1:41:45

Is that point clear to all of you?

1:41:48

They are just two lines of code white.

1:41:51

We can do that.

1:41:52

I'm just telling you automated way also.

1:41:54

Lanchine provides you automated way also.

1:41:57

But in bigger applications, that can also be a concern of doing that.

1:42:02

Also everyone, we need to import runable history from Lanchine underscore core.

1:42:09

Import runables.

1:42:12

We will import.

1:42:15

Runable with message history.

1:42:19

So these are the two things that we have imported in you.

1:42:21

Is everyone clear?

1:42:22

Folks, clear?

1:42:24

Now I will have the, we will have the same fake database, same tool, copy paste.

1:42:31

We have just written it, no need to write it again and again.

1:42:35

Then what is the next thing, everyone?

1:42:36

After this, we will create the LLM, we will create a list of tools, go to memory, create a list

1:42:42

of tools, create a LLM, create a LLM, create a LLM.

1:42:45

list of tools, create a LLM.

1:42:48

Now we are going to write a chat prompt template.

1:42:51

I will copy paste it again.

1:42:53

Guys, we have just written it right?

1:42:55

So it is okay to copy.

1:43:01

Okay?

1:43:02

Now, again the same thing.

1:43:04

If user gives an order ID, remember it in the conversation, resolve follow-up questions,

1:43:09

tools to check the status, etc.

1:43:11

And then everyone, we are providing the chat history, optional is equal to true.

1:43:14

to true, human input and agent scratch pad, no change at all.

1:43:18

Clear.

1:43:19

Clear, everyone.

1:43:20

We have just written it, right?

1:43:22

Why to write it again and again?

1:43:24

Then again we will create the agent with the same thing.

1:43:26

Agent is equal to create tool calling agent with LLM, prompt and tools.

1:43:32

Okay?

1:43:33

Then we will create the agent executor.

1:43:35

Same thing.

1:43:37

And this is why everyone I say that, once you start writing the code,

1:43:41

a lot of things will be automatically you will keep on understanding.

1:43:44

If you see 90% of the code is almost same, right?

1:43:48

Exactly the same.

1:43:49

Now, some changes will happen now.

1:43:51

Now tell me everyone, do you need to maintain the chat history per conversation or across

1:43:58

conversations?

1:43:59

The chat history makes sense for a particular conversation or multiple conversations

1:44:04

chat history, you will store at one place.

1:44:07

Is it per conversation or across conversations?

1:44:11

It is obviously per conversation.

1:44:13

Can you?

1:44:14

we call a conversation also as a session.

1:44:18

One conversation is one session.

1:44:22

Now even technically,

1:44:24

Lanchine defines it as a session.

1:44:27

Okay? So what we do everyone is we create a

1:44:30

we create a function, define, get session history.

1:44:36

Right? So you maintain the conversation per session.

1:44:40

So you give the session ID, right, which is going to be string.

1:44:43

to be string, let's say session one, session two. See everyone, you are, let's say,

1:44:47

100 people are using chat gpt.

1:44:49

Assume that chat gpt is a very small application, only 100 people are using.

1:44:52

Now 100 people, let's say person 1, person 2, person 3, and person 100, all of them are talking to

1:44:58

chat gpt, they are all having one one conversations.

1:45:01

So these are different, different sessions.

1:45:03

Assume that session 1, session 2, session 3.

1:45:05

Don't you think chat gpt should create a separate session for each conversation and maintain

1:45:10

the user history or the message history per conversation?

1:45:12

three per conversation or per session, correct or not?

1:45:16

This is the whole idea, right?

1:45:17

So what we are doing everyone is we will create a session, you can say that, a session store.

1:45:25

Okay?

1:45:26

This is going to be a simple dictionary.

1:45:27

You will get the meaning of this.

1:45:28

You can see that this is going to, this is a nothing but session wise memory store.

1:45:33

Okay?

1:45:35

So you are going to provide a session wise memory store.

1:45:37

Again everyone, it is optional and giving you slightly more advanced way.

1:45:41

And everyone, if you give the session.

1:45:42

ID, you get the history of that session, right?

1:45:45

And what, in what way you store the history?

1:45:48

You store the history in memory, chat, message history.

1:45:51

Okay?

1:45:52

So what this function does everyone is, I'm just writing for your understanding.

1:45:55

It has nothing to do with LLM, etc.

1:45:58

So it returns, returns the chat history, chat history for the given session of

1:46:11

or conversation.

1:46:13

Is that point clear to all of you?

1:46:15

Returns the chat history for the given session or conversation.

1:46:18

Make sense, everyone?

1:46:20

For example, let's say if you assign a conversation ID.

1:46:23

So let's say one conversation ID, you give the conversation,

1:46:26

it will give you the chat history.

1:46:29

Now, given, I could have done this very simply.

1:46:31

Can I remove all these things and just assume that there is only one session for now?

1:46:36

Can I do that for easy, you can say that, for easy execution?

1:46:40

easy execution.

1:46:41

Assume that there is only one session and we can do that, right?

1:46:45

So it is okay.

1:46:46

So if session ID is not present, if let's say, so what do you do everyone?

1:46:51

You try to get the session from the store.

1:46:53

So if session ID is not in store, right?

1:47:01

So what do you do?

1:47:03

It means that if this session ID, if you're asking about the session ID, if this is not present

1:47:08

in the store, it means that there is no conversation for that.

1:47:10

So you can create a new conversation.

1:47:15

You can create a, you can initiate the conversation.

1:47:19

Or you can simply return empty conversation, right?

1:47:23

Do you see that?

1:47:23

We are returning empty conversation because it does not exist.

1:47:27

Okay?

1:47:28

Otherwise, we will return store session.

1:47:32

So if everyone, if session ID does not exist, you are assigning a, you are assigning a empty conversation

1:47:39

and then you are returning it.

1:47:40

If session ID exist, you are returning what you have stored in the store.

1:47:45

I can remove this function also, everyone, if you want, later on, I can remove this function also,

1:47:49

but I hope the idea is clear.

1:47:52

Okay?

1:47:54

Now everyone, you have to do what?

1:47:56

We have created agent executor and we have created agent, everything we have done.

1:48:01

Now you have to create one more thing, slightly different.

1:48:05

So, just follow this with me and then I will explain.

1:48:10

Agent.

1:48:10

with memory. So as of now, everyone, does this agent that you have created, or this agent

1:48:16

that you have created, have, is this agent aware of in-memory chat history or runable

1:48:23

chat history, runable with chat history? Is this aware? No, this is not aware. So what we are

1:48:30

going to do everyone is, we are going to create another agent with memory. Agent with memory is

1:48:35

equal to runable chat with history and we are going to provide these parameters.

1:48:40

First is agent executor.

1:48:42

Then everyone, get session history.

1:48:45

Just a second, everyone.

1:48:46

I think someone is on the door.

1:48:47

Just a second.

1:49:10

Yes. So everyone, we will tell that this is the agent with memory. The above agent is without memory.

1:49:19

So we will create an agent with without memory. Then we will create an agent executor. Now finally,

1:49:25

we will create a final agent. So you can say that this agent is just an intermediate agent. This is not

1:49:29

going to work in reality. This agent we are going to invoke, agent with memory, that this is the agent

1:49:34

executor. Get session history is the function to get the session history, to get the conversation

1:49:39

history. And everyone, we will pass input message key that with what value we are

1:49:46

passing the input? If you see, this is the key, right? This is the variable name. Okay? Then everyone,

1:49:52

we will have where we are storing the history. History message key. Where we are storing the

1:50:02

history. We are storing the history in the prompt. If you see, this is the variable we are giving,

1:50:07

chat history. So with this we will provide. Okay. And everyone, where we are going

1:50:13

to get the output, we are going to get the output, we are going to get the output in this output variable.

1:50:16

I know slightly tricky, but it is not something that we can do anything about it. It is what

1:50:22

it is, we can try to understand it, right? Agent Executor have. So we are, what we are doing

1:50:27

is what agent executor we have, now we are, you can say that with this agent executor,

1:50:33

is the memory associated as of now? Tell me. Is the memory associated as of now? Tell me. Is the

1:50:37

memory associated with this agent executor? No. It is not associated. Now what we are doing

1:50:43

everyone is we are associating memory with this agent executor and we are passing an object of

1:50:50

runable with message history. That run this agent or run this agent executor with message

1:50:57

history. That run this agent executor with message history with these some variables. That

1:51:02

to get the history, we have to call, we can call the function get session history.

1:51:07

Input, basically the input variable name is input. Chat history is going to be

1:51:12

maintained in the chat history array or the variable name. And output messages will be, output

1:51:18

will be having the variable name of output. You can give whatever you want here, right? Whatever you

1:51:23

want. Is that point clear to all of you? That output you will get in the output variable.

1:51:27

Now what we are going to do everyone is we are going to, so similar to this everyone with memory,

1:51:32

what did we do? What about tool history? What do you mean by tool history?

1:51:37

That is there in the scratch pad, right? Any ways that we are not going to use right now,

1:51:42

but that will be maintained by scratch pad. Yes. So everyone now, if you see, we ran, we wrote this

1:51:50

function, ask agent, right? We will write this function also here, but in a slightly different

1:51:54

way because now the way to call the agent will be slightly different. Okay? So we will do ask agent,

1:52:00

ask agent, and we will pass session ID. Now, we will

1:52:07

which session you are sending a message to? Don't think even it will, let's say for example,

1:52:12

you are, you are having multiple conversations. Let's say in the chat GPD, you open two windows,

1:52:16

window one, tab one, tab two, tab two. You open two windows of chat GPD. In window one, you are

1:52:21

having one conversation. In window two, you are having different conversation. If you ask a message in

1:52:26

conversation one and then the second message you ask in conversation two, will conversation two be

1:52:31

able to understand what do you have asked in conversation one? In the first tab, will it be able to understand? No.

1:52:37

This is what we are implementing here. That with every message, everyone, when you ask a message to chat GPD,

1:52:42

with every conversation, right? So, for example, if I show you, uh, just a second, let me show this to you.

1:52:56

See, this is the chat GPD. This is chat GPD, uh, this is chat GPT, everyone, right? If I ask any question,

1:53:01

like, uh, let's say, uh, hi, this is my order ID.

1:53:07

101, although chat gpt will not be able to understand anyways, okay? Now if I do this,

1:53:11

if you see, one conversation will start. And do you see that this conversation ID is there? Do you say

1:53:18

that this conversation ID is there? Now, if I open another conversation, if I go to chat GPT, and if I ask

1:53:25

another question, let's say, explain me, agentic AI, right? Now everyone tell me, both of these

1:53:32

are different conversation IDs, right? This is conversation ID 1. This is conversation ID 2. Correct.

1:53:37

or not everyone? Now everyone, if I ask, let's say maybe if I ask some question here, what is my

1:53:42

order ID? What is my order ID? Now, depending on the implementation, chat GPD may not be able

1:53:47

to understand because these are two different conversations. Correct or not?

1:53:51

folks, yes or no? This is what we are implementing. So when you are passing the message,

1:53:55

chat GPT says that this message, user is asking, this query user is asking, in which conversation?

1:54:01

Only question is not important. Conversation ID or session ID is also equally important.

1:54:05

Because if you ask same question in a different conversation, GPD might not be able to answer it.

1:54:12

Folks, yes or no? Right? So you will have the conversation ID, the session ID here, right, which

1:54:18

is of the type, let's say string. Right? Also, you will have the user input parameter, the user input

1:54:26

that is coming, user input, which is also of type string. And then everyone, we are going to implement,

1:54:32

let's say result or response.

1:54:35

is equal to agent with memory dot invoke. Now we are going to invoke this agent.

1:54:42

Correct or not, everyone, we are going to invoke this agent with memory. Correct? So what we will

1:54:46

pass everyone? We will pass different fields here. First of all, we will pass the input parameter.

1:54:51

And what is the input parameter, everyone? The user input which is coming. Correct. This input,

1:54:56

input message key, that what is the key or what is the variable name for input? Input.

1:55:02

Right? This is how Langchain or Agent with memory will be able to.

1:55:05

to understand that input is the actual input parameter. Correct? If I make use of any other

1:55:11

variable here, will it be able to understand that this is actually the user input? No. So you will

1:55:15

have to provide input here. Then everyone, you provide config here. Inside the config, everyone,

1:55:20

you provide just the session ID, right? You provide the session ID like this. Let's say,

1:55:25

this is configurable. I could have made it very easy for all of you to understand, but I thought

1:55:32

that let's try to implement this in the maximum productionized.

1:55:35

way. So you provide session ID. Let's say session ID is everyone. Whatever

1:55:41

session ID is coming in the input. Is this point clear to all of you? So to execute the agent,

1:55:45

you are providing the input and session ID. Clear? And then finally everyone, you return the response

1:55:53

and inside the response output. Okay? Folks, just have a look at it. If you see just a different

1:56:01

way, just what we did in agent with memory, manually.

1:56:05

almost same thing we are doing, only slightly different. Maybe let's say 95, 90 to 95% code is

1:56:13

same. Just 5 to 10% changes are there. Agree? Agree or not? So what we are going to do everyone is,

1:56:19

now we are going to execute multiple terms, let's say. So what we do everyone? I can say that, okay? I can

1:56:24

assign some session ID, some random session ID. Let's say session ID is for customer

1:56:29

user 1. Okay? User ID 1. Okay, let's say 0-0-0. This is the

1:56:35

session ID, assume that. Okay, this is session ID. And then everyone, I can

1:56:40

copy paste this part. Or I can write it again. So I will say print, turn 1, take the user ID,

1:56:54

let's say, uh, user input, and then let's say the query is high, uh, uh, user input. And then let's say the

1:57:05

my order ID is ORD. What is the order ID then?

1:57:12

ORD 101. Let's say this is the order ID.

1:57:16

Okay, this is my order ID. Okay. And we will say that okay. Uh, user input.

1:57:27

Then if you say, paint, uh, AI response, you get the AI response. You get the AI response.

1:57:35

Now for this, everyone, you will have to call the ask agent function with the session ID,

1:57:44

with the first of all, you will have to pass the session ID, which is session ID, and you have

1:57:49

to pass the user input. Is that point clear to all of you?

1:57:53

Folks clear? Right?

1:58:05

Now, this is turn 2, right? And ask for the status, right?

1:58:15

Bracket up. Okay? Or let's say, what is the status of it? Okay? What is the status of it? You are not providing the order ID now. This is the user input you are passing. And again, if you see, we are passing the same session ID in the same conversation. Is that point clear to all of you? Now, once we have the demo for this, then,

1:58:35

we will pass different session IDs also. Then we will see that whether it is maintaining,

1:58:40

it is able to use the data of different conversation also, different session also. Is this making

1:58:44

sense to all of you? Folks, clear or not?

1:58:50

Guys, yes or no? If you see in the entire code, are we appending the messages? Are we appending the messages

1:58:58

manually? Are we maintaining the messages manually? No. So now everyone, go to terminal.

1:59:05

Clear the terminal and now let's try to execute Python 3May, Lanchain, agent, memory

1:59:14

with auto, all right? Let's try to execute this.

1:59:18

Hi, my order ID is this, see, my order ID is this, and then it is able to track it, right? And

1:59:25

then if you see, order ID is this, and then the second thing is, everyone, turn to, what

1:59:32

is the status of it? And it is automatically calling, get,

1:59:35

order status with the order ID 101. Is it able to remember the order status without even

1:59:41

appending the chat history manually? Tell me, yes? So we have one application supporting

1:59:46

multiple sessions on front end. Absolutely correct. Absolutely correct. Guys, is the code

1:59:52

working fine? That we have a code, we have the code where chat history is being maintained

1:59:58

automatically. Is that point clear to all of you? Do you, do you want me to show the stored history also?

2:0:05

Show the stored history. Stored memory. Do you want me to show you that? Okay.

2:0:11

So for example, let's say everyone, for this particular session ID, I want to show you what messages are stored, right?

2:0:17

So what you can do is for, first of all, you can say that, for go to each message, let's a message in, store, go to this session ID, and in this session ID even, we are going to have messages.

2:0:32

Okay? So if you see everyone, inside this session,

2:0:35

inside this store, what are we storing? We are storing in-memory chat message history, right?

2:0:40

So in this chat message history, it stores, it gives you messages. Okay, it gives you messages.

2:0:46

So you can iterate over it. Uh, uh, there is a problem here. What is a problem?

2:1:05

messages, right? And now everyone, we will simply print what? Let's say, I will have to check

2:1:13

the syntax for that, message content. Type message. Ha. So this is something like this.

2:1:25

That print the type of the message, whether it is an AI message or human message. For each

2:1:30

message, print the type and the name of this, whether it is a human message.

2:1:35

Again, everyone, this is a syntax, nothing can be done. And then, and then what is the content of the

2:1:46

message? Okay, now let's try to execute this once again.

2:1:55

Let's see the content of the content which is being stored internally.

2:2:00

do, what is the status? It is able to use the status. Now see. See the final

2:2:04

stored message, everyone. AI responses, your order ID is currently shipped. Okay? Human message.

2:2:10

Actually, let's do one thing, everyone. Sorry for this. Let me also print.

2:2:16

Stored messages in memory.

2:2:26

Then only we will be able to identify what is actually in the memory.

2:2:30

Because AI also returns a lot of data, right?

2:2:32

And we cannot identify what exactly is the content of the message, right?

2:2:36

If you see, stored message in the memory, just look at this.

2:2:38

This is the message history which is being stored internally.

2:2:41

Just look at this. Human message, AI message. Human message, AI message.

2:2:46

Is that point clear to one of you?

2:2:48

This is the message history which is being stored internally in the system.

2:2:53

Folks clear?

2:2:55

Human messages, hi, my order ID is this.

2:2:57

AI messages, thanks. I have noted down your order ID, etc.

2:3:00

etc. Human messages, what is the status of it? Order ID is currently shipped.

2:3:05

Correct? So now we have successfully implemented both the scenarios. In fact, all the three

2:3:10

scenarios. Stateless, without history, with history, two scenarios. Manual update, manual append,

2:3:16

automatic append. Everyone clear? Folks, yes, no, yes, no. Now one last thing, everyone.

2:3:28

Now, let's say if you're having a conversation, right? If you are having a conversation,

2:3:33

and in that conversation, let's say you have thousands of messages. Don't you think everyone,

2:3:38

if you keep on storing every message in memory chat history, your RAM will overflow

2:3:45

or your RAM will, like, get consumed very fast, right? Your RAM will overflow. Obviously, you will have

2:3:52

limited RAM, right? You don't want to store all the messages in the history. If you have unlimited RAM,

2:3:57

you can do that. But generally we don't have unlimited RAM. So you put a limit, right? And you

2:4:02

might have seen that after a certain limit also, chat GPT also starts forgetting in a conversation.

2:4:07

You have thousands of messages, although nowadays the limit of chat GPT is pretty high. And if you pay the

2:4:12

money, if you get the premium subscription, it is very high, right? Most of the times we don't even interact

2:4:17

so many things. We don't even have so many interactions within the same conversation. But generally everyone

2:4:23

for production use cases, it is very high. But let's say, if you want to put a limit,

2:4:27

that how many messages you want to store, then there is a concept of something called

2:4:32

as rolling conversation history. Rolling conversational history. Right? For example, everyone,

2:4:43

what you can do is rolling conversation history simply means that, that when you are defining

2:4:48

this chat history, right, you are defining this chat history, you can define one more parameter

2:4:53

called as n underscore messages is equal to 10.

2:4:57

It means that it will always maintain 10 messages. First, second, third, up to 10.

2:5:03

As soon as you have the 11th message, what it will do now? If you get the 11th message,

2:5:08

but the limit is already 10. Limit is only 10. Then it will remove the first one.

2:5:13

Okay? It is a window. First you have the window. If the window gets completed, then it

2:5:19

will slide the window. It will roll the window. So the first message will get deleted from

2:5:25

the memory, right? And the 10th message is, you will get deleted from the memory.

2:5:27

or 11th message will be added. So at any point of time, inside your conversation

2:5:31

history, you can have maximum 10 messages, whatever value you define here. Is that point clear

2:5:36

to all of you? Okay. So I'm not going to do that here. Let's not change the code. It is perfectly

2:5:46

working fine. Right. So we can do that. To pass the rolling history, we can set

2:5:57

the value of n messages in messages placeholder. Okay? And what this does everyone is,

2:6:11

this keeps only let's say n messages. This keeps only defined, whatever value you have defined, 5, 10, 20, 100, only

2:6:24

defined number of messages in the history at any point of time. Is the meaning clear to all of you?

2:6:32

Now this is your assignment. Try to do this. Right? So you can either have a full history. If you don't

2:6:40

give this value, if you don't give the value of n underscore messages, everyone, will the history be,

2:6:45

will the history will always be full? Correct. History will always be full, right? It will store all the

2:6:51

messages and rolling history. So guys, can we decide which one we should use? First of

2:6:56

which one is better? Which one is good? Which one is good? Full or rolling? Which one is best?

2:7:03

Obviously full, right? If you can maintain full, it is always better. But there will always be

2:7:08

trade off. Right? You cannot store unlimited number of messages for every session. There is always

2:7:14

one limit that you should put. Right? Otherwise your memory will overflow. Everyone clear?

2:7:21

or not? Okay. This is what we wanted to discuss for today's class. One last thing

2:7:27

that I want to tell you, just one good, just few good practices, or some common errors that can help

2:7:35

you in debugging the application, right? Common errors in history, common errors in memory, right? Or let's

2:7:46

say, you can say that common debug points. I would say common debug points. That these points, you can

2:7:51

use to debug the application if something goes wrong. First of all, everyone,

2:7:57

sometimes what happens is most of the times, like maybe some of the times, placeholder name we give wrong.

2:8:04

Wrong. Common errors. Common debunk points or errors. While building agents with memory,

2:8:21

Langchain. Okay? Wrong placeholder name. It means that, for example, let's say,

2:8:29

here we provide wrong placeholder, right? This variable name. It might be a problem. Then other error

2:8:34

could be everyone. Let's say, if we forget to append in the history, append in the chat history,

2:8:44

if you're doing manually and then if you forget, can it lead to some errors? Can it lead to unexpected behaviors?

2:8:51

Right?

2:8:55

Folks, see, sir know?

2:8:59

And let's say append messages in wrong order. So guys, ideally what should be the order?

2:9:07

First, you should append the user message. If you see, what did we do? First, we appended the user

2:9:12

message, ideally. Human message and then AI message. This is the correct order. You will never

2:9:17

get the AI message first, right? First, you have the human message.

2:9:21

Right? Correct or not?

2:9:26

One very big mistake that people sometimes make is shares common memory, common memory across

2:9:35

sessions, across sessions or conversations. Should we ever do that?

2:9:43

Should we ever do that? Should we ever do that?

2:9:47

No. So these are the common debug pointers that we should take care of while

2:9:51

implementing the agents with memory in blockchain. Is everyone clear?

2:9:57

Folks clear? So this is what we wanted to discuss for today's class. I hope today's class was

2:10:02

at least for me, it was very interesting. I found it very interesting. We saw a lot of things

2:10:08

in today's class and stateless with memory, manual update, automatic update. Okay? Perfect.

2:10:15

So guys, let's commit the code.

2:10:19

How many of you found it interesting?

2:10:21

and exciting. That yes, we built multiple agents today with memory.

2:10:27

Guys, memory is the most complex topic. And there are a lot of startups. There are a lot of

2:10:32

AI companies which are working on the field of memory. A lot of startups are being built. A lot of

2:10:40

startups have been built in last few months, few years. And a lot of startups are going to be

2:10:44

built in next few months, next few years, which are going to solve the problem of memory.

2:10:49

memory is very common and very big problem. How do you manage memory? Because if you want,

2:10:54

you can, the best way is store everything. But you cannot store everything. It is very, very difficult

2:11:00

to store everything because memory is limited. You need to make sure that, that you are storing efficiently.

2:11:06

You are storing only required information. Now, to solve these problems, there are a lot of companies

2:11:11

and a lot of startups have been built, which are of billion dollar valuations. Okay? So you will find

2:11:15

a lot of resources and a lot of opportunities in this area in the future.

2:11:19

And right now also. Okay? So let's push the code everyone. So this is the code, first of all, for today's class.

2:11:49

It was really interesting, but I will have to go through. Yes, code you will have to go through. It will take time. Okay? Don't try to remember the code. You don't have to remember the code. You just have to get some sense out of it. Understand the logic first. Just try to get some sense out of it. Guys, I don't remember any of this code. Do you think I remember all this code? I refer this during the class. Okay? I have written this code once, multiple, not once, multiple times on my own. Now, I refer the notes while writing the code. Okay? Because no one can remember.

2:12:19

these small, small variables, right? And I'm not, I'm not working on this for last 20 years, so that I will remember.

2:12:24

I have also got the exposure just like last few years.

2:12:27

Correct? And things are changing very rapidly.

2:12:30

Right? So today, you are learning some code. Maybe six months down the line, the code will change.

2:12:34

Right? The logic will change. New variables will be introduced. New functions will be introduced. So it's not,

2:12:39

there is no point of remembering the code. Correct, everyone? There is no point in remembering the code,

2:12:45

spending your efforts in remembering. And honestly, you cannot remember also.

2:12:49

Okay.

2:12:51

So folks, I will upload though.

2:13:19

So this is the code for today's class.

2:13:26

These are the notes. Code I have already shared with all of you. These are the notes.

2:13:32

Okay. So folks, I'm launching the feedback poll. Please take the feedback pool and we can drop off now.

2:13:38

We are done with the class. Thank you so much. Have a good day. Take care and bye. See you in the next week now.

2:13:43

Have a good weekend. Have a good Saturday Sunday. Enjoy. Take some time to revise concepts also.

2:13:49

I think if you spend just two hours, it is good enough.

2:13:52

Rest of the time, you can enjoy and see you on Monday now.

2:13:55

Have a good day. Take care and good night.

2:13:58

Thank you for attending the class, everyone.

2:14:01

Please take the feedback poll. We are done.

2:14:03

Thank you. Thank you, everyone.

2:14:14

Folks, please take the feedback poll. We can drop off then.

2:14:19

backpool, you can drop off. We are done.

2:14:49

Okay, Somia, everyone has filled the feedback poll so we can end the class.

2:14:55

Thank you, everyone. Take care and goodbye. Thank you, Samia.

2:15:00

Thank you, sir. Thank you, everyone for joining.

2:15:05

We'll meet tomorrow with the Quddin. If you have any, dogs, please, we'll join.

2:15:11

Good night.

2:15:19

