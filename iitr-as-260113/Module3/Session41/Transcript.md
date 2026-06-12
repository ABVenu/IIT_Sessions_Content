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

Thank you.

5:48

Thank you.

6:18

Thank you.

6:48

Thank you.

7:18

Thank you.

7:48

Thank you.

8:18

Thank you.

8:48

Thank you.

9:18

Thank you

9:48

Thank you

10:18

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

Thank you.

11:06

Thank you.

11:36

Thank you.

12:06

Thank you.

12:36

Thank you.

13:06

Thank you.

13:36

Thank you.

14:06

Thank you.

14:36

Thank you

15:06

Thank you

15:36

Thank you

15:38

Thank you

15:40

Thank you

15:42

Thank you

15:44

Thank you

15:46

Thank you

15:48

Thank you

15:50

Thank you

15:52

Thank you

15:54

Hi everyone.

16:24

Very good evening to all of you.

16:26

We'll start in a couple of minutes.

16:28

Welcome, Deepak sir.

16:31

Yeah.

16:32

Thank you.

16:33

Thank you, Samia.

16:34

So folks, what I was typing is, by mistake, I sent the message halfway.

16:40

So today's class is built on the rag application,

16:43

the rag application that we built in the last class.

16:46

So before we start, I think the strength is on the lesser side.

16:48

Take five to seven minutes of time just to go through the code.

16:52

Okay.

16:52

So I am sending the.

16:54

code right away in the chat.

16:55

Please go through this link, everyone.

16:57

Just try to revise what we did in that class.

17:01

Does it make sense, everyone?

17:03

Please try to go through this.

17:13

So this is one thing.

17:16

And the other thing was, yeah, I think just go through this file.

17:21

Take five minutes of time, go through this file.

17:23

Then today.

17:24

This class will be very easy for you to understand.

17:26

Okay?

17:27

Sure.

17:28

In the meantime, I think more people will also join.

17:30

Because today is like the non-class day for all of you,

17:34

not the regular class.

17:35

That's why people might take some time to join.

17:54

Thank you.

18:24

Thank you.

18:54

Thank you.

19:24

Thank you.

19:54

Thank you.

20:24

Thank you.

20:54

Thank you.

21:24

Thank you.

21:54

Hi,

22:24

Am I audible?

22:31

Okay.

22:32

How many of you have you gone through the code that I just

22:36

just shared in the chart.

22:40

Done?

22:41

Okay.

22:45

So guys, guys, today's today's class is based on

22:50

on the rag.

22:51

So we will just try to integrate

22:53

tools with the Rack as well, right?

22:55

So initially we learned Lanchine applications, build an application using Lankchain

23:00

with only tool.

23:02

Then we built a Rag application.

23:04

Now we will integrate both of these today in today's class, right?

23:06

So let's get started with today's discussion, everyone.

23:09

In the previous class, what did we do?

23:12

Can I say that?

23:13

We had, everyone can see my screen, right?

23:15

I have not shared the screen yet.

23:17

Sorry.

23:20

Yeah, is my screen visible now?

23:23

the iPad screen.

23:24

Yeah.

23:25

So now in the last class, IP1, what did we do?

23:28

We had, let's say, a user question.

23:30

So if a user ask a question, what did we use to do?

23:35

From user question, we used to retrieve the documents, correct?

23:53

retrieve documents.

23:59

Then after retrieving documents, everyone, what do we do?

24:02

We put these documents in the prompt.

24:05

Put documents or chunks, basically.

24:13

Then what do we do?

24:14

We add these chunks in the document.

24:17

Put chunks in the prompt.

24:22

Remember that?

24:23

the context we give in the prompt as a variable, and then we pass it in the input parameter,

24:28

and then this we pass to LM, everyone, and then LLM generates the final answer using this context.

24:38

LLM generates the final answer.

24:40

Does that make sense for all of you?

24:41

So this is step number one, step number two, step number three, and step number four.

24:46

This is a complete step by step process that we follow.

24:49

In this lecture, everyone, in this session, we will move one step ahead,

24:53

we will start building an agent, which will decide, right?

24:57

If you see everyone as of now, are we deciding whether we should retrieve documents or not?

25:02

Are we deciding that?

25:04

No, right?

25:04

We are always retrieving the documents.

25:06

But now today we are going to build an agent which will decide whether to retrieve documents or we

25:12

should use a tool or we should call a tool or maybe we should do both or we should call an LLM, whatever,

25:18

right?

25:18

So what we are going to build today, right?

25:21

So this we built in last class.

25:23

In last class, we built

25:37

we built the below application, the below flow, the below flow.

25:53

We will be implementing this flow.

25:55

That user ask a question.

26:02

User ask a question.

26:05

Then this question, we pass to the agent.

26:10

This question we pass to the agent.

26:12

And this agent decides.

26:23

whether to retrieve or call some tool call any tool call tool or call tool tool or both in some cases we might have to take both the actions also right both or maybe no tool whatever right any option can be there and then finally we generate the answer

26:53

So basically after this, if let's say retrieval is decided by the agent, then we will

27:01

again go through this step, retrieve documents, put that in the prompt, pass it to LLM, generate the final

27:06

answer, but this is going to be the flow.

27:08

Now we will have to, we will be putting some extra logic internally, the agent logic, which will

27:14

decide whether we should call a tool or we should call some retriever and whatnot.

27:18

Is the idea clear to all of you?

27:19

Okay.

27:23

Now, this particular thing everyone is called this retrieval tool.

27:27

Now, why do we need this retrieval tool?

27:30

See, a normal retrieval is just a search component.

27:33

This is what a normal retrieval does.

27:35

But what an agent can do is, agent does not directly under, like agent, agent directly does not, agent does not, agent does not directly call the tool or the retrieval document.

27:45

It can decide basis on the query.

27:47

Right.

27:48

We can configure that.

27:49

in these scenarios, call the tool, in these scenarios, call the, let's say, call the retriever

27:55

and whatnot.

27:56

So, a retrieval tool, everyone, there is a concept of retrieval tool.

28:04

So we are going to build a retrieval tool, which can decide, which can take a decision autonomously.

28:12

So this is called as retrieval tool.

28:14

Is everyone clear?

28:17

Okay.

28:17

How to create?

28:18

We will see that.

28:19

in the code.

28:20

Okay?

28:21

Now, for example, even this is one example that I've taken.

28:24

Let me probably take a screenshot and let me show you this particular thing, right?

28:31

First of all, there is a concept, then I will copy the screenshot also.

28:45

Let me take the screenshot as well.

28:49

So before we actually go to the next topic, let's talk about tool arbitration first.

29:10

Now, what is tool arbitration.

29:12

Now, what is tool arbitration?

29:14

It is the ability.

29:19

It is the ability to choose the right tool.

29:31

Ability to choose the right tool is called as tool arbitration.

29:35

Generally, we make a mistake, everyone, that we don't give proper tool descriptions.

29:39

If you remember in the tools classes, in the, like, in the class where we created multiple tools,

29:43

do you remember that?

29:44

We gave proper tool descriptions?

29:47

Remember that?

29:47

in the string format, inside the function, those tool descriptions should be very, very proper,

29:55

and also the tool name should also be very good.

29:57

So that your LLM or any agent can decide autonomously that which tool we should call for what purpose.

30:03

It is very important.

30:04

Generally, everyone, we give, let's say, because of not giving a proper tool description,

30:09

some vague tool descriptions do you give, this ability can hamper.

30:14

Right?

30:15

Your agent might not be able to call the right to.

30:17

because of proper, because of having not proper tool description.

30:22

Does it make sense to all of you?

30:23

So a tool description should clearly answer, what does tool do?

30:28

When should we call that tool?

30:30

What is the agenda of that tool?

30:32

Right? What, like, what is the requirement that particular tool, like, what is the requirement

30:38

that a particular tool fulfills?

30:40

Does that make sense to all of you?

30:43

Okay.

30:44

Now everyone, let me copy the screenshot now.

30:47

And let's see this example for an editech student assistant, support assistant.

30:53

Right?

30:53

So let's say, everyone, if you ask a query, what is a refund policy?

30:57

In this refund policy, everyone, let's say, which is a correct tool?

31:01

Because for refund policy, do you need to go to vector database and check the refund policy document?

31:07

Tell me, do you need to go to refund database and check the refund policy document?

31:11

Yes.

31:11

So that's why we will have to go to retriever.

31:14

So now retriever is also acting like a tool here.

31:16

We will go to retriever.

31:17

Then everyone, what is my ticket status?

31:20

What do you think, everyone?

31:21

In this case, what is my ticket status?

31:23

What is the status of my order?

31:24

Something like that.

31:25

Do you need to make a call to vector DB?

31:28

Do you need to make a call to vector DB?

31:30

No, no vector database is required.

31:32

Here you need to make a call to database, right?

31:34

Basically, let's say there is a tool which can make a call to orders database or tickets database

31:39

and let you know the status of order or ticket.

31:42

Does it make sense to all of you?

31:43

So here we will call ticket status tool.

31:45

There is a separate tool.

31:46

For example, if you remember,

31:47

get order status. We created this tool, which will make a call to database and get the

31:51

order status. Here, we will make a call to ticket, ticket status tool. Can I get the batch change

31:58

if I miss three classes? Again, Retriever. Because this is again, depends, this also depends on

32:04

policy. Does it make sense for all of you? This also depends on policy. Then everyone,

32:08

what is the status of my refund ticket? What is the status of my refund ticket? Again,

32:12

everyone, what we need to do in this case? What is the status of my refund ticket? Do we need to call

32:17

some tool or should we make the retriever call? Should we retrieve the policy documents?

32:22

What do you think? What is the status of my order or my ticket? If you see, of my refund ticket?

32:28

If you see, it is saying possibly both, right? First of all, everyone, we need to make a tool call,

32:34

right? Which will tell you the status, right? Here also we are making a tool call. Here also we

32:38

will make a tool call. But everyone, why it is saying possibly both? Because it is a refund ticket,

32:45

right? Depending on the status, everyone.

32:47

If you go one step ahead, like if you just want to do what user is asking for, you just make

32:53

a tool call, get ticket status, and tell you the ticket status. But don't you think everyone,

32:58

you can go one step ahead and also add some extra information about the refund depending on the status.

33:03

For example, if status is not approved, right, rejected, then you can attach some policy information

33:09

and let the user know why and on what basis your refund was not approved or rejected.

33:15

Are you guys getting this point? Yes or no?

33:17

Folks, so that's why possibly both. Correct? Very good. Now, in this case, everyone,

33:24

who own IPL 2025? Right? In this case, everyone, do you see any tool call, any rag call, any retrieval call?

33:32

Answer is no. Right? So if, if everyone, you are not putting proper guardrails, then you can directly make a

33:38

tool, you can directly make a call to LLM, right? And give the answer. But should we do that? Should we allow these

33:45

kind of questions on Amazon chatbot, on Swigi chatbot, should these kind of questions be

33:50

answered? Absolutely not. These kind of questions should never be answered. That's why we're out of

33:57

domain refusal. You can put proper guardrails and in the prompt, etc, and there are certain different

34:02

ways also. We'll talk about them. And you can put, you can reject these kind of questions, that these are out of

34:07

domain and this question I will not answer. Is everyone clear with proper understanding? This is a problem

34:13

people talk about on Reddit a lot where people ask DSA question to McDonald's

34:18

chatbot. Yes, and then McDonald's chatbot might be answering that if it is not properly

34:22

handled, right? Correct. Now everyone, let's start with the coding part. Let's start

34:31

writing the code just a second.

34:43

Yeah. So let me start with Visual Studio.

34:52

So we will open our project, new open folder, and we will open the same application, LandChine

34:59

Apps.

35:00

Okay.

35:09

If you see, a lot of code we are writing in this folder.

35:12

Good.

35:13

enough. So now everyone, we are going to write multiple tools here, right? So first,

35:18

we will create, let's say, the example that I'm going to take today, that we are going to take

35:22

today is course support rag agent, very, very similar to what we have done in the past,

35:26

but we will have tools like get course policy searched, right? For that, you'll have to make a rag

35:31

call, right? Then you might have to make a call, let's say you will create a tool for getting the ticket

35:37

status, right? And we will create a fake database. First of all, everyone, let's install all

35:42

the things. Let's make sure that all the things are installed, although most of the things are

35:45

already there. PIP3 install. First, we need to install Lankchain. Lankchain 4. Although everyone,

35:56

we have already installed these things, so nothing to worry about. Okay, one more thing even.

36:01

Let me tell you a better way of defining these things. Folks tell me, if let's say you have

36:06

20, 30 different dependencies and if you install like this, is that a good idea? Dependency 1,

36:11

dependency 2, dependency 3, dependency 4, dependency 5? No. Did I tell you in any of the classes,

36:16

did I tell you requirements dot TXT? Okay, yes. Okay, I have already explained this, very good.

36:26

So, guys, whatever dependencies you need, you can define here. For example, we need

36:29

land chain, we need land chain four, we need land chain classic, we need land chain, classic, we need land chain,

36:41

chain open AI, we need Lanchine, Croma, we need Lanchine text, hyphen splitters, right?

36:52

For now, we need these dependencies, right? And what I can do now is PIP3, install hyphen R,

37:00

requirements. TX2. Just install this everyone. And all the dependencies, even if you have 50, 60 dependencies

37:06

here, you don't have to write them one by one. Just maintain all of these at one place. In fact,

37:11

everyone in bigger projects, it is very, very important to maintain all the dependencies in one

37:15

folder. Because everyone, when you start working on any project, right, by default,

37:19

like, how will you get to know that these many dependencies are required or we need these,

37:23

these dependencies? If they are maintained at one commonplace, then it will be easier for a new developer

37:28

to identify those dependencies, right? And they can easily install it. Now, after this, everyone,

37:34

we will start creating the agent, okay?

37:41

So what we will do is, first we will create the retrieval agent, and let's name it as ragagagent.

37:48

Okay?

37:48

Rag agent.p.y.

37:50

And from here, everyone, we will start writing the code.

37:53

And there are a lot of things that we need to write, Langchain underscore open AI, import, chat, open AI,

37:58

and open AI embeddings from Langchain underscore 4.

38:06

Dot, documents, import, import, import.

38:11

document. Okay. From Langchain underscore 4. Dot prompts, import, chat prompt template,

38:27

import message placeholder, okay? From Langchain underscore, I think this is slightly boring task

38:36

that I'm doing. Can I copy paste all of these?

38:40

Can I copy paste?

38:41

Okay. So just a second. So all these dependencies we need.

38:49

Okay. If you see chat open AI embeddings, document, prompt template, message placeholder, human

38:56

message, AI message, tool. Do you remember human message, AI message? Now it means that

39:03

we are going to add memory also. Remember that? Chat message history. Chat history, correct.

39:09

Create retrieval tool. This is one.

39:11

One thing that we are importing, we are importing, chroma, Chromea database,

39:15

text splitter, agent executor, and create tool calling agent, right?

39:18

Now if you see, we are combining a lot of functionalities in one place, right?

39:21

So first everyone, we will have a lot of raw documents.

39:25

So these are the raw, raw documents we have everyone.

39:28

So let me copy paste it.

39:32

There are like four or five set of documents we have written.

39:37

We can directly copy paste them.

39:40

Now if you see everyone today.

39:41

We are not creating them directly in the files, right?

39:43

We are directly giving a raw document.

39:45

And inside this raw documents, you have a document object.

39:49

Remember that?

39:50

Earlier what we were doing everyone in the last class, create corpus me,

39:53

we had these documents and then we were storing them in the files.

39:56

Okay? And then we were retrieving them, then we were using them.

39:59

Remember that?

40:00

First, we are storing them in the file and then at the time of ingesting,

40:04

you were creating these documents.

40:07

See, not ingesting, create corpus.

40:11

stateless memory. Somewhere we were creating the document object, right?

40:21

Correct. But here everyone, if you see, I'll have to check that. But here, if you see everyone,

40:25

what we have done is we are directly creating the document object. Okay? So that we don't have

40:29

to do that from scratch. We have already done that in the last class. Can you see that even? We

40:33

have five, six documents. So one is career services policy, batch change policy, project

40:38

submission policy, attendance policy, and refund policy.

40:41

So these five, six documents we have. Now everyone, what we are going to do is we are going to create

40:46

chunks of these documents. So we are going to, first of all, create a text splitter

40:50

is equal to recursive, recursive, corrector, text, splitter. And here, everyone, we are going to

41:01

pass the chunk size, is let's say maybe chunk size is 100 or 500, whatever.

41:05

Anyways, our documents are very small. Even if you don't create chunk size, it's okay.

41:09

And chunk overlap is, let's say, maybe, 50, 75, 80. Okay? Again, 10, 15%.

41:15

Then everyone, what we do, we create split documents. We split the documents, split documents. And we do

41:24

text splitter. Dot split documents. And here we pass the raw documents.

41:33

Okay. And then what we do, everyone, we create embeddings. So first of all, we create the embedding model.

41:39

Embeddings is equal to which model we are going to use? Text embedding three small.

41:47

The same model that we have used in the last class also, right? I think the same model we have used in

41:51

the last class. Correct. Okay. Embedings we have created. Now we are going to create a vector store.

41:58

I hope all of you remember this thing. Chroma. Dot Chrome documents.

42:05

Store these documents split after splitting, right?

42:09

use embeddings, right? And use collection name. This is a collection name.

42:17

Collection name is equal to, let's say, we already have some collection, right? Inside this,

42:25

what is a collection name we used in the last class? And today, we will use a different collection

42:30

name. In this, we use e-commerce policy docs. Okay? But today we can give a separate

42:37

collection name because this is kind of a separate data.

42:39

separate set of document. This is course policy correction, right, or whatever,

42:47

documents, right?

42:49

Course policy correction. This is the vector database that we have, vector store we have created.

42:53

Now we will create a retriever, right? Retriever is equal to vector store.

43:00

Dot as retriever. And what we do? Search type is equal to, search type is equal to semantic or similarity.

43:09

Similarity. And then we provide search arguments, which is, let's say, K-value

43:18

3. Everyone remember this? This is what we have already done. Now everyone, we will create a retrieval

43:24

retrieval tool. So course, policy. This is a good revision. Create retrieval tool. The same thing

43:34

we did in the last class also. Rag app. See? As retriever.

43:39

Now, prompt. And here, if you see, correct? Now, if you see everyone, in the last

43:47

class, we didn't create a tool. Correct? Now, everyone, if you see, we are creating a retriever

43:53

tool. Earlier, we just created a retriever object. Now, using this retriever, everyone, we are

43:59

going to create an agent. Because now agent, we are going to give more auto, like you can

44:04

say that more power, that agent can decide autonomously, should we call the retriever or should we

44:09

not call the retriever. So here, everyone, we are giving kind of more independence, right?

44:13

So we are going to pass the retriever. Retriever is equal to, this is the retriever. Then everyone,

44:18

the name of the tool, the name of the tool is, let's say, the same thing, course policy tool.

44:29

Okay? Then we are going to provide some description. And what description, everyone, what this tool does?

44:35

And this is the description, everyone, that we are going to provide. Let me copy paste it.

44:38

Okay? Just look at this description, everyone, that what this tool does, searches official

44:44

course, course policy documents for refund, refund rules, attendance requirements, right?

44:49

batch change policy, project submission deadlines, and whatnot. Just the course, you can say that,

44:54

the tool description. This is the proper tool description that we have given. Does that make

44:59

sense to all of you? Now, folks, what we are going to do is, we are just going to create, if you see,

45:03

this tool is going to make a call to retriever. Can you see that? This is a retrieval.

45:08

Retriever tool. Okay. This is a retrieval tool. Okay. And now we are going to create,

45:15

because now we are going to basically create two agents. One is retriever tool agent, which is going to

45:20

make a call to the retrieval, basically the policy search, searching the documents. And we are also

45:25

going to create a non-retriever tool agent. What is the use case of this? You will just get it while

45:30

writing the code. For example, everyone, let's say name itself will explain you. If let's say you create a

45:36

function which is get ticket status. Okay. Get ticket status and we are going to define this

45:43

at the rate tool annotation. Have we imported tool? Yes. Okay. At the rate tool annotation. And here

45:49

we will pass the ticket ID. Is this point clear to all of you? Yes or no? Okay. And everyone again

45:59

provide a proper tool description like this. Look at this. Proper tool description.

46:06

This particular tool is used for what? It returns the support ticket status for the given

46:12

ticket ID. Use this tool when the user ask about the ticket status, refund request status,

46:17

etc., etc. for a given ticket ID. Okay? This is a tool description. Always make sure that

46:22

tool description is proper. For this everyone, we are just creating a fake database.

46:27

Okay. Just inside the function only, I can create a fake database here.

46:33

Okay. In this fake database, everyone, you have let's say, four ticket.

46:36

and the status of these tickets. Okay. Does that make sense to all of you?

46:42

Just a fake database. And finally everyone, we will return fake ticket database.

46:46

Dot get. Okay. First, what we are going to do everyone is get the ticket.

46:52

Ticket status. Ticket status, fake database. Dot get from the ticket ID. Okay. And everyone,

47:05

if ticket status not found, if not ticket status, then we can simply say that we can return.

47:12

We can return ticket status not found for the given ticket ID. Yes and my folks. Are you guys

47:25

getting this point? Ticket ID. Okay. And else everyone, we will just get the ticket status,

47:32

get the ticket status and return it. And we will directly return ticket status here.

47:37

Right? I think everyone is well aware of this coding till now. Now everyone, how many tools we have

47:43

created? Now we have two tools. Okay. So what we used to do, we used to create a list of tools, right?

47:50

We used to create a list of tools. And we have the course policy tool and we have the get ticket status

47:57

tool. Does that make sense everyone? We have these two tools. Now what we used to do now?

48:02

Tell me, after creating the list of tools, what we used to do now?

48:07

What is the next step? What are the steps pending?

48:12

Prompt template is pending and LLM is pending, right?

48:15

Use an LLM. So we are going to create an LLM is equal to chat, open AI, and model is equal to

48:23

some model, let's say, open AI, GPT 5.2, we will use GPT-5.2, comma, and temperature value if you want to

48:32

set is equal to 0. Everyone aligned till this point of time, yes or no?

48:42

Okay? Yes, we're going to do that. We're going to do that, Mughal, absolutely correct. Now we are

48:46

going to write the prompt. Okay? Prompt is equal to chat prompt template. Dot prom messages

48:54

and write the prompt template here. So what we're going to do everyone is,

49:02

Okay, so let me, in fact, let me copy-paste the prompt template so that we don't

49:13

write it again and again.

49:18

This is the prompt template that we have.

49:25

Just take one minute of time, read about it, try to understand the meaning of chat history, agents

49:32

scratch pad and let me know. Let me do word wrap. Okay? Just read this prompt

49:42

template and try to identify the meaning of every single word, message placeholder, variable name is

49:49

equal to chat history, variable name is equal to agent scratch pad. We have discussed everything.

49:57

Did we discuss all these things in the last few classes? Have we discussed all these things? Have we discussed

50:02

all these things in the last few classes, yes. So take one minute of time, read about it.

50:06

At what and how we are writing the prompt template.

50:12

So you are a helpful customer, course support assistant. You have access to two tools.

50:19

One is course policy search and one is get ticket status. This is the description of course policy

50:25

search. This is the description of get ticket status. These are the rules. If the question is

50:30

about official course policy, use this tool. If the question is about the ticket

50:34

status, use this tool. If the question needs both policy and ticket status use, you can use both

50:40

the tools also. First, let's say user is asking about the status of the ticket and then they are

50:44

asking about some other question as well, for which you might have to refer the policy documents.

50:49

If the question is outside course support, politely say the user, that you can only help

50:53

with the course policy and support tickets. When answering from documents mentioned that,

50:58

answer is based on the available policy document. Keep answer clear and student friendly.

51:03

Because this is a student assistant, right? For some ed tech. Folks, yes or no? Is this

51:09

part clear to all of you? Okay, perfect. Then we have the chat history. Why do we maintain the chat

51:19

history? Can someone write down in the chat? Why do we do that? And what this component is all about? This

51:25

component is all about? Absolutely, correct? Giving the memory.

51:38

So we are making our tool with memory. So that our agent can remember the context from different,

51:44

let's say, from different messages. Okay? It can, for example, in one of the messages, you have given,

51:50

let's say, this is my ticket ID. Now in the second message, you say that, please track it. Please tell me the status of it.

51:55

How does the student support agent will remember it with the help of chat history?

51:59

Then everyone, we have the human input, the query that human will ask, the user will ask,

52:03

and then we have the messages placeholder, right, which is agent scratch pad. So whenever you have a tool

52:08

calling agent, always have agent scratch pad. So agent scratch pad, so agent scratch pad observes the tool,

52:15

right? It stores tools observability, what tool you have called, what output it has given,

52:20

whether the tool has succeeded or not succeeded, et cetera, et cetera. Okay. Now we are going

52:25

to finally create an agent. As of now, we have just created the tools. Now we are going to

52:28

create the final agent, like create tool calling agent. Create tool calling agent. And here we are

52:35

going to provide the LLM is equal to LLM. Then we are going to provide the tools. Basically,

52:40

we are binding the tools, and then we are going to provide the prompt template also. Is that

52:47

point cleared all of you? And now we just have to invoke this agent. Now, should we invoke this agent

52:52

manually, agent. Invoke. Should we do that? Or did we learn some new thing that we can

53:00

use? Should we do agent. invoke? No, right? We should create an agent executor. Remember that?

53:11

I think you guys are not revising things, right? Agent Executor. Correct? Agent Executor. What all the

53:18

parameters we used to pass inside agent executor? Any, any guesses?

53:22

Just one two examples. I don't want the complete list. Let's see how many of you can

53:27

recall. Generally, what parameters we should pass inside the agent executor. Even if you don't

53:33

remember, right, you should be able to, you will be able to figure out if you just try to understand

53:37

what agent executor does. What is the requirement of agent executor? Absolutely, we need to

53:42

pass agent, absolutely correct. We need to pass tools, absolutely correct. Then, remember, something

53:50

called as max iterations. We can set max iterations. Then we can pass all of these are

53:56

obviously optional parameters, verbose. If you want the debugging to be enabled, verbose, you can pass

54:02

return intermediate steps, absolutely correct. Handle parsing errors, correct. All of these things

54:08

you can pass here. Right? So we are going to have an agent here. We are going to have

54:14

we are going to have tools here. We are going to have verbose is equal to true.

54:28

Then we are going to have max iterations is equal to let's say three and so. Is that point clear to all of you?

54:37

You can pass more parameters also depending on the requirement. And then everyone, we are going to

54:41

maintain the chat history. Initially, the chat history is going to be empty.

54:45

Okay. Now we will write a function to execute this agent. Define, right? Define, ask,

54:55

agent. And this will take the user input, user query, which is going to be of type string.

55:04

And this will also return string. Okay. And what this query, what this function does, this function simply

55:10

says it sends the user query to the agent and stores conversation in the stores

55:23

conversation history in in chat history in chat history in chat history in chat history

55:30

manually correct or not everyone folks yes or no now we are going to get the response

55:39

is equal to agent executor dot execute dot invoke.

55:47

Okay. And what do you have to pass inside this is you have to pass the input,

55:54

the user query which is coming in the query,

55:57

uh, in the input parameter, user query. And then everyone, you will pass the chat history.

56:01

Chat history is equal to chat history. That's it.

56:09

Now, after you get the response, everyone, do you remember that?

56:12

We need to maintain this chat history manually, right?

56:17

We did binding of tools in agent. Do we need to? Yes, that's correct.

56:20

So here also we need to pass the tools. Here also we need to pass the tools.

56:26

Okay? Now everyone, we need to maintain the chat history.

56:29

That from this response, we will get the actual answer.

56:35

Answer is equal to response.

56:37

May say, give me the output.

56:39

And now what we do in the chat history?

56:41

What we used to do in the chat history, how we used to maintain chat history?

56:46

By how we used to maintain chat history?

56:54

Guys, anyone remembers that, we have done that couple of times.

56:58

How we used to maintain the chat history manually?

57:09

No one. No one remembers.

57:13

Okay, how, what is the chat history? What is chat history ultimately?

57:18

It is nothing but the human message, the AI message.

57:21

What query you are asking, what response you are getting. What query you are asking, what response

57:25

you are getting. So here is the user query, right? Here is the user query. And here is the AI query,

57:30

basically the response. Don't you think? We just have to append

57:34

human message or yeah, human message or human query, append human message and

57:42

AI message inside in the chat history. This is what we need to do. Folks, yes or no?

57:51

Folks, yes or no? Simple. Chat history dot append a human message object we create

57:58

and where we pass content is equal to user query. And then we have to do chat history.

58:04

append, a AI message, and content is equal to, what do you say, the answer that

58:10

we are getting in the output. This is what we have to make sure, right, that we are appending the

58:14

chat history. And finally, folks, we are going to return the answer. Finally, we are going to

58:19

return the answer. Does that make sense to all of you? Yes or no. Does that make sense to all

58:26

of you? Yes or no. Now, what you have to do? We are going to take a break now. Because everyone

58:31

see, honestly, this code, if you understand, this code, the code that we have written today,

58:38

how much time it took? Hardly 20 minutes. Because it took us 20 minutes to write this code,

58:43

because guys, we have spent at least last 10 classes on learning these individual concepts, right?

58:49

Understand? Agent, memory, chat history, agent scratch pad, this tool calling agent and whatnot.

58:57

LLM, all these things, embeddings, all these things we have spent maybe 10,

59:01

to 20 classes to learn these things. And now it just took us 20 minutes to write this board.

59:07

Do you, do you know that? Understand understood? Now, in this code, everyone, if you see every

59:12

concept is there, think about rag, it is there. Think about memory, it is there. Think about

59:19

chat history, it is there. Think about LLM, it is there. Think about prompt template, it is there.

59:23

Think about tool, it is there. Think about tool calling agent, it is there. Think about agent executor, it is

59:29

there. Think about documents, it is there.

59:31

chunk there. Overlapping, there. Embedings there. Every single thing. That generally we talk about

59:39

in AI courses. It is all there in this code. Correct? Now what we are going to do, everyone, is before we are

59:46

going to, before we execute this code, I want all of you to spend some time on going through this code

59:51

line by line by heart. I never tell you to remember code. In fact, you don't have to remember code,

59:57

but at least try to understand the meaning of every single line in this code. Right?

1:0:01

It is very, very important. And if you understand this code, it means that you have understood everything,

1:0:06

what we have learned in the last few months, right? So, this is Lanchine, Rag, tool, agent.

1:0:15

Okay?

1:0:16

Tool, calling agent.

1:0:21

Let's push. Let's push the code. And this is the code. The code is available at this link.

1:0:31

So this pile is this one.

1:0:46

Take your time, everyone. Please go through the code. Please make sure that. And I would be more than happy to take any of your doubts after the break. And I will be happy if you ask doubts.

1:0:54

Okay? Please make sure that you go through every line of code, just like 200 lines of code, not not even 200.

1:1:00

Okay?

1:1:01

So maybe take seven minutes to write the code, to understand the code, nine, and then maybe 10 minutes of break.

1:1:08

Okay? So let's meet after the break. In the meantime, you can go through the code.

1:1:31

Thank you.

1:2:01

Thank you.

1:2:31

Thank you.

1:3:01

Thank you.

1:3:31

Thank you.

1:4:01

Thank you.

1:4:31

Thank you.

1:5:01

Thank you.

1:5:31

Thank you.

1:6:01

Thank you.

1:6:31

Thank you.

1:7:01

Thank you.

1:7:31

Thank you.

1:8:01

Thank you

1:8:31

Thank you

1:9:01

Thank you

1:9:31

Thank you

1:10:01

Thank you

1:10:31

Thank you

1:11:01

Thank you

1:19:01

Okay,

1:19:04

Hi, so, so,

1:19:05

so let's

1:19:06

so let's get

1:19:07

so let's

1:19:09

we are

1:19:10

we are

1:19:11

we're

1:19:12

just

1:19:14

through

1:19:15

through

1:19:16

through the output

1:19:17

uh, so let's get started.

1:19:19

And now,

1:19:20

I'll

1:19:22

I think we are mostly done with the class.

1:19:24

We just have to

1:19:26

execute the class.

1:19:27

I'll just have to execute the code.

1:19:28

I'll just walk you through

1:19:29

through the output and just I will show you some

1:19:31

one or two more things, right?

1:19:33

That was the agenda of the class.

1:19:35

So let's start writing the, let's start running the code first of all, right?

1:19:39

So what we're going to do is, okay, so as of now, we have not written the, we have not given the query, right?

1:19:44

We have not given the query.

1:19:46

So we can give some sample queries.

1:19:48

For example, let's say maybe query 1 is equal to, let's say, what is

1:20:01

policy. What is different policy? And this query, you can pass to the agent, which is, let's say you say, print user query is

1:20:18

query one. And then what you do, everyone, you print AI answer response, you call the

1:20:29

call the function ask agent with the query one.

1:20:34

And similarly when you do this thing, okay, and then the second query everyone is let's say, what

1:20:43

is the status of ticket, let's say, TKT, 51001, okay?

1:20:54

And then you have this query to query two.

1:20:59

query to, query to.

1:21:06

Okay, initially when we started embeddings, the data into vector database, we also insert the metadata.

1:21:13

Is it still happening through the framework?

1:21:15

In this case, yes. If you see, in the document, we are giving some metadata also.

1:21:19

Okay? Now, in this metadata, there can be a lot of other fields also, let's a type of document, right?

1:21:25

Then when this document was the last updated, last,

1:21:29

updated time and multiple other things you can have in the metadata.

1:21:33

Okay?

1:21:34

So for now, we just have this metadata source, but you can add any number of metadata here.

1:21:40

Create retriever tool felt like a new topic.

1:21:44

Is it a different way?

1:21:45

No.

1:21:46

It is not a different thing altogether.

1:21:48

Create retriever tool.

1:21:49

It is just a, you can say that if you see, there is a tool calling agent, right?

1:21:53

There is a function called as tool calling agent.

1:21:56

Similar to that, you are creating this retriever as a tool.

1:21:59

Right?

1:22:00

Because now this is going to act like a tool, right?

1:22:03

If you see, earlier what was happening, this retriever was just a functionality.

1:22:08

And you are always calling the functionality.

1:22:10

But now what you are doing is you are creating now a retriever as a tool that your agent can

1:22:14

decide, that should I call this tool or should I not call this tool?

1:22:18

Make sense, Billah?

1:22:19

Now your agent can actually decide.

1:22:21

Should I call this?

1:22:21

Should I not call this?

1:22:22

So we are just creating this as a tool.

1:22:24

Nothing different.

1:22:25

Okay?

1:22:27

It is very, very similar to at the rate tool annotation, absolutely correct.

1:22:32

Okay.

1:22:33

Using at the rate tool, you are creating a functional tool using, if you do use this function create

1:22:38

retriever tool, it creates a tool as a retriever with retriever.

1:22:42

Okay?

1:22:43

Can we start writing, can we start running the application now, Python 3?

1:22:47

Okay, as of now we have given two queries, right?

1:22:49

Query 1, query 2.

1:22:50

I think good enough, we can give maybe one or two more queries, right?

1:22:54

For example, everyone.

1:22:55

Let's say if you give, for now, let's run it, Python 3, ragagent hyphen dot PY.

1:23:10

Okay, let's see everyone, what output we generate.

1:23:17

Okay, there is some problem here.

1:23:19

Open AI API key.

1:23:20

As expected, this is something that we need to do every time.

1:23:24

So export.

1:23:25

Open AI API key is equal to this.

1:23:55

Yeah, so everyone, we are getting some output here.

1:24:02

Let's see.

1:24:03

First of all, this is the user query.

1:24:04

What is the refund policy?

1:24:06

And then everyone, if you see, agent executor starts execution.

1:24:09

And then if you see, invoking this tool with this query.

1:24:13

Now everyone, if you see, what is refund policy?

1:24:15

Do you think here, course policy tool, which is basically a rag-based tool, a retriever tool.

1:24:21

This should get executed, course policy tool.

1:24:24

If you see, what is this tool, everyone?

1:24:27

Course policy tool.

1:24:29

This is Create as Retriever.

1:24:33

Yeah, course policy tool.

1:24:34

This is rag-based tool, right?

1:24:36

And what it is saying, everyone, refund policy, and it is giving you the refund policy.

1:24:40

This is a refund policy.

1:24:42

Okay?

1:24:43

And then everyone, after this, we have another query.

1:24:47

Yeah.

1:24:47

Then we have second user query.

1:24:49

What is the status of this ticket?

1:24:51

The status of this ticket, everyone, is get ticket status.

1:24:54

This thing.

1:24:54

tool we are invoking, get ticket status with ticket ID this.

1:24:58

And then we are getting the ticket status.

1:25:01

Does it make sense to all of you?

1:25:02

Expected response time is two working days.

1:25:05

So it is working absolutely fine.

1:25:07

Now let's do one thing, everyone.

1:25:09

Let's give a slightly different type of query.

1:25:12

First of all, is the working, making sense to all of you till now?

1:25:17

Okay.

1:25:18

Now, let's try to change the query a bit.

1:25:21

Okay?

1:25:24

Let's give a multi-turn query.

1:25:32

What is the meaning of multi-turn query?

1:25:34

Can anyone try to guess the meaning of multi-turn query?

1:25:46

It means that let's say you are asking about the, let's say you want to call both the tools.

1:25:50

So you are asking about the ticket status as well.

1:25:52

And then you are asking that maybe some.

1:25:54

something about the status.

1:25:55

Okay?

1:25:56

So let's say everyone, you give the ticket ID.

1:25:58

My, what is the status of my?

1:26:01

The status of my ticket 1002.

1:26:12

What is the status of my ticket?

1:26:14

And tell me the refund policy.

1:26:19

Refund policy.

1:26:21

Okay?

1:26:22

Tell me the refund policy.

1:26:23

Let's say this.

1:26:24

the query that we are getting. Let's make it query three, query three, query three, okay?

1:26:31

Is this multi-tool query making sense to all of you?

1:26:38

Okay, perfect. Let's try to run this application now.

1:26:42

So it should call both the tools. First, it should call the get ticket status tool.

1:26:46

Then it should call the get course policy tools.

1:26:52

Okay? Refund policy.

1:26:54

First, it is calling the ticket status, get ticket status, right?

1:26:59

Your batch change request has been approved.

1:27:01

New batch starts next Monday.

1:27:02

This is the ticket status.

1:27:04

Then it is calling the course policy tool.

1:27:06

Okay?

1:27:07

Then it is returning the policy.

1:27:09

Is that point clear to all of you?

1:27:14

Actually, what it is doing everyone is, it is returning, it is return, it is showing every out,

1:27:17

all the policies.

1:27:19

And then at the end, it is giving you this output, right?

1:27:22

The refund policy.

1:27:23

This is actually, this is actually the main output.

1:27:24

Riven policy based on available policy documents.

1:27:28

Does that make sense for all of you?

1:27:33

Folks, clear?

1:27:34

Now, what all the topics we are using here?

1:27:37

First of all, everyone, let's try to revise all these things.

1:27:40

Are we using documents object?

1:27:42

Are we using document object from Lankchain, core, dot, documents?

1:27:47

Yes, we are using documents object.

1:27:49

Then we are using chunking.

1:27:54

Then we are chunking.

1:27:54

the documents, chunking or splitting the documents.

1:27:57

Then we are creating embeddings of these documents, right?

1:28:00

then what everyone?

1:28:01

After creating the embeddings, what is the third step?

1:28:03

What is the fourth thing that we are doing?

1:28:07

storing embeddings into vector database.

1:28:16

Okay?

1:28:16

Into vector store.

1:28:19

Then after vector store, everyone, we are creating

1:28:24

a retrieval tool, right?

1:28:28

then we are creating retrieval tool

1:28:30

is basically the name of the tool is

1:28:31

course, policy, tool.

1:28:37

Then we are creating a tool.

1:28:39

Get ticket status tool.

1:28:41

Get ticket status tool.

1:28:46

Okay? I think that's it.

1:28:49

These are the things that we are doing everyone.

1:28:51

And finally, everyone, we are creating LLMs, we are creating a list

1:28:54

of tools. Then we are creating the agent. Then we are creating the agent

1:28:58

executor. Yes, absolutely correct. That before LLM or in fact before LLM we are creating the prompt

1:29:07

template. Okay. Then we are creating agent executor. That's it. Everyone clear. Then finally we are

1:29:21

invoking the agents.

1:29:24

Okay. So tool calling is working absolutely fine in our scenario in this example.

1:29:30

Does it make sense, everyone?

1:29:34

Now the final part for today's class. Just the last thing.

1:29:38

Anyone has any doubt in these things, everyone?

1:29:41

Agent Scratchpad, chat history, anything. I hope everyone is, everyone remembers, right?

1:29:46

Okay. Tell me one thing about Agent ScratchPad. What agent Scratchpad does?

1:29:51

Just one line answer.

1:29:53

Scratch.

1:29:54

Let's see how many of you remember? Scratch pad.

1:30:08

So, maintains information, information regarding tools, tool callings. Okay. So you can say that.

1:30:24

Without tool execution, without tool execution, without agent scratch pad,

1:30:39

without agent scratch pad, the tool calling agent won't be able to track track track.

1:30:54

Is this point clear to all of you? Just look at this. Without agent's crash pad,

1:30:59

the tool calling agent won't be able to track tool calls properly. Sounds good, everyone.

1:31:08

Okay. And finally, everyone, we are going to create a something called as test pack. Okay. Test package.

1:31:16

Okay. We will create a set of queries, everyone, basis on which we can, uh, sorry, do you have any

1:31:22

question. You have put a question mark. Okay, no worries. Test package, everyone.

1:31:30

So finally, it's very important to test the, uh, test your complete flow, your complete code. For that,

1:31:37

everyone, we have something called as compact evaluation, eval, pack. Okay, compact, evaluation, pack.

1:31:45

Now, you can say that everyone, this is just a terminology. No need to remember this as such. You can say that

1:31:51

an EvalPack is a small set of test cases used to check, used to check, used to test and validate the

1:32:05

agent behavior. Okay. And EvalPack is a small set of test cases used to test and validate the agent behavior.

1:32:21

Now, let me show you the Eval evaluation test cases.

1:32:28

Okay?

1:32:30

So we can maybe comment this out as well.

1:32:33

And these are the test cases.

1:32:34

Just have a look at this everyone.

1:32:35

I have already written these test cases earlier.

1:32:37

So these Eval cases, everyone, first is the name of the test case is refund policy.

1:32:42

Here we are asking some question about the refund status, right?

1:32:46

A refund something related to refund.

1:32:48

What tool we are expected to call in this course policy tool?

1:32:51

expected keywords in the answer, seven days, refund, 30 days, etc.

1:32:56

And failure type is bad.

1:32:58

What can go wrong?

1:32:59

What fails?

1:33:00

Weak retriever or missing retrieval.

1:33:02

What if, let's say, your agent is not able to properly retrieve the data?

1:33:05

You are asking about refund and let's say your agent is retrieving some other information about the batch change or other policies.

1:33:13

Or it is not calling the retrieval tool as such.

1:33:16

Completely it is missing the tool call.

1:33:18

This is the first test case.

1:33:20

Similarly, everyone, we have multiple.

1:33:21

test cases which are checking different different scenarios for all these use cases, right?

1:33:26

The second is check the ticket status.

1:33:29

We should call this tool.

1:33:29

This is the expected tool.

1:33:31

What keywords are expected?

1:33:33

What can go wrong, right?

1:33:35

then again, the next tool, again the next test case, next test case and so on.

1:33:40

Is everyone clear with the set of test cases that we have here?

1:33:43

Is everyone clear with the set of test cases that we have here?

1:33:46

Now let's execute.

1:33:51

the above Eval test cases.

1:33:58

Okay?

1:33:59

So we have everyone, what we can do is we can just iterate over this Eval cases.

1:34:04

That for each case in Eval case, we can just, we just need to execute this, right?

1:34:10

So first of all, we can print the, let's say the test case name, which test case we are executing.

1:34:16

Test case name.

1:34:19

which test case we are executing?

1:34:22

Let's say case, give me the name value of this test case.

1:34:26

Okay?

1:34:27

Then we have, let's say, what input we are passing?

1:34:33

Input is, in this case, everyone, we have the input field, print the input field.

1:34:42

Then we have everyone, expected tool call.

1:34:49

expected tool call, case may expected tool tool.

1:35:00

Okay, then everyone get the output, ask agent, pass the user query, what is the user query,

1:35:10

what is the input, this is the input, pass this input to the agent, right, you will get the output and

1:35:18

what are you going to do everyone is, let's say the agent output, agent output, you are

1:35:26

printing here in the output.

1:35:29

Is that point clear to all of you?

1:35:33

Okay?

1:35:34

Then everyone, you can check these, these things also.

1:35:37

What are the expected keywords?

1:35:38

And in this output, whether do you have these expected keywords or not.

1:35:41

You can check that.

1:35:42

You can even make it even more validations.

1:35:45

You can add more and more validations here.

1:35:47

So now let's try to do.

1:35:48

execute this rag agent hyphen pi now we are going to run the test cases here okay please

1:35:55

pass ah sorry because everyone the point is that because i closed the terminal that's whether

1:36:02

the API key got revoked so i'll have to set it again

1:36:18

Now let's try to execute the code.

1:36:31

Yeah.

1:36:32

So look at the first query, everyone.

1:36:34

The first query, test case name, refund policy.

1:36:36

This is the input query.

1:36:37

This is an expected tool.

1:36:38

Then everyone you are invoking this tool and then you are getting some data, right?

1:36:42

Finally, everyone, what output you are getting?

1:36:45

We are printing that.

1:36:48

agent output.

1:36:51

Where the output is there.

1:36:52

Yeah, this is the agent output, everyone.

1:36:54

Yes, based on the available policy documents.

1:36:56

This is the policy document.

1:36:58

Then everyone, it executes the next test case.

1:37:00

This is the next input.

1:37:02

This is the tool, expected tool call.

1:37:04

And you can check all these things.

1:37:06

Right?

1:37:06

It is executing all the test cases one by one, one by one in the order.

1:37:10

Is everyone clear with this?

1:37:15

Is everyone getting this point?

1:37:17

Right.

1:37:18

After the class, everyone, what you can do is, right?

1:37:21

You can see that.

1:37:22

Try to validate.

1:37:24

I have added this code in the notes anyways.

1:37:26

You can try first and then you can try to refer from the notes as well if you want.

1:37:32

Try to validate the expected keywords also.

1:37:37

Try to validate expected keywords as well.

1:37:40

Then also everyone, you can try to validate the expected tool call also.

1:37:44

expected tool call try to validate this tool call as well.

1:37:55

Okay?

1:37:56

Is that, is the point clear to all of you?

1:38:03

Okay.

1:38:04

Now, the next topic.

1:38:07

If your tool fails, right?

1:38:09

What are the different, what could be the different possible reasons?

1:38:12

Let's say, if it is failing.

1:38:13

How can you, let's say, if you, let's say, if you.

1:38:14

want to add some, what kind of failures can happen? First of all, first common failures,

1:38:21

some common problems or some common failures while executing the core, while executing a rag-based agent.

1:38:37

And guys, by the way, whatever we have learned today, this is called us agentic rag, rag with agents.

1:38:42

Okay. Yesterday, in the last class, we built a normal rag. Today, we have built an

1:38:47

agentic rack, right? Tool-based rag, right? Some common failures while executing the rack-based,

1:38:55

let's say, or let's say, agentic rag. What are the common errors that can happen? First,

1:39:00

common error, everyone, first error could be wrong tool call. Correct? Let's see you are not calling the right

1:39:06

tool. You are not calling the expected tool. Because in reality, there might be hundreds of tools,

1:39:12

The code might be very complex. And somehow, for some scenario, your agent is not calling

1:39:16

the right tool, right? So what could be the output for this? What could be the fix for this?

1:39:23

What could be the fix for this? Generally, you will see that improving the tool description works.

1:39:31

Improve tool description. Most of the time, it works. Right? Maybe check prompt again.

1:39:38

Check prompt as well. You might have written something wrong in the prompt.

1:39:42

prompt again, right? Cross-check the prompt again. Generally for this, everyone,

1:39:47

with this idea, this particular error of wrong tool call can be fixed. Okay? Does it make sense,

1:39:54

everyone? Okay? Now, other common failure could be what? Let's say your system is going through

1:40:03

weak retrieval policy or weak retrieval is happening. It means that maybe you are calling the right tool,

1:40:10

but let's say you are asking about the refund, but somehow your rag-based system, it is not

1:40:14

checking the refund data. It is, let's say, it is trying to check other policies. It is not able

1:40:19

to retrieve the correct data. It is retrieving the weak data, the weak retrieval policy. What could

1:40:25

be the issue for this and how can you fix it? What could be the issue for this, everyone?

1:40:35

There are possible things, right? Maybe embeddings could be a reason that you are not creating

1:40:39

proper embeddings, right? Chunks could be one reason. Chunk size is too large. Chunk size

1:40:46

too large or too small. Correct? Embedding can be one reason. Chunk size can be one reason. Chunk

1:40:55

overlap can also be one reason. Try to change chunk overlap value also. Absolutely correct. Top the K

1:41:01

value, right? Let's say if K is too low, right? Don't you think even this can be one problem?

1:41:07

Yes or no? Correct?

1:41:12

Change, try to change the K value. Also everyone tried to use different search policy also. Let's say

1:41:17

similarity search is not enough. Similarity search is not enough in your use case. So do you remember

1:41:24

that even there are different ways in which you can search? For example, similarity search.

1:41:28

One of them we learned about MMR search. Remember? One of them was MMR search. So you can try

1:41:34

changing these values as well. Correct?

1:41:37

correct? Absolutely correct. Now these are the things and these are the

1:41:48

these could be the problems as well and these could be the fixes also. Then everyone, other

1:41:54

error could be this is the first second. Other third type of common failure could be everyone

1:42:02

over refusal. Now what is the meaning of over refusal? Right. So for example,

1:42:07

everyone if the user ask about that what is the attendance requirement for placement

1:42:11

support? But agent replies that I cannot answer that the document, but the document still contains

1:42:16

the answer. Okay. It means that you are asking some question. Your agent is not answering

1:42:22

the question, but still, even if the data is there. It means that your agent is refusing to answer

1:42:30

very frequently. Correct everyone? Absolutely correct everyone. Too strict. What could be the fix?

1:42:37

And what would be the reason for that? To strict prompt or restrictions.

1:42:46

Right? Correct, Evan? You have given very strict prompt. And because of that, it is refusing more number of queries than expected.

1:42:54

Right? Let's say if you have asked, if we have asked the agent to refuse aggressively.

1:43:07

Correct, everyone? This could be one problem.

1:43:13

Again, tool description can be one thing, everyone.

1:43:18

Tool description. If you can make it better, then for example, let's say the tool description is not up to the mark.

1:43:24

Even if you are trying to call the agent, even if you're trying to call the tool, but it is because of tool description, you are not able to make a tool call.

1:43:32

Right? And it is refusing it. Can this be the reason? Yes. So maybe check tool description as well.

1:43:37

Right? Folks clear or not. What could be the other error? Right? What could be the fourth error?

1:43:46

Right? Missing memory. Right? For example, everyone, let's say if you don't have the memory in your application, then agent won't be able to retain the context. Correct.

1:44:07

agent won't be able to retain the context and it will not be able to give you proper answer. Does that make sense to all of you?

1:44:15

Okay. So now what could be the fixes, everyone? Let's say one fix could be chat history, right? Agent Scratchpad.

1:44:24

Agent Scratch pad, right? Maybe chat history is not getting appended properly.

1:44:31

Not appending chat history properly.

1:44:37

Does that make sense to all of you?

1:44:44

Folks clear? Yes or no?

1:44:47

So these are the few things, everyone, that we were talking, that we had to talk about for today's class.

1:44:52

Now, there is one more thing that we can have because we have some time today.

1:44:56

Just a second.

1:45:06

Just one.

1:45:07

more thing, where is it? The mind map. In last two, three classes, I forgot to discuss

1:45:21

this. Anyways, like in every class, it is not going to change very, very aggressively. This is what the

1:45:27

mind map. This is how the mind map actually looks like for our module, right? So if you just look at it

1:45:32

everyone, in the previous module, we covered about agentic foundations, architecture, Python and

1:45:37

APIs. And we learned about LLM basics, prompting and backend foundations like

1:45:42

fast API, etc. This was one module. Then in the last module as well, we learned about

1:45:48

rag, rag pipeline, chunking, embeddings, vector search, similarity search, memory, concept of memory,

1:45:55

concept of retrieval, etc. Then in the current module, till the last session, we have, we have already

1:46:01

learned about rag, langchain rag pipeline, loaders, chroma database, langchain expression language,

1:46:07

grounding comparison with and without retrieval. If you use rag, what is output? If you don't

1:46:13

use rag, what is output? We have compared the outputs very, very clearly. And everyone, in the current

1:46:17

session, we have combined these things. And in the current session, if you see, we have built a rag

1:46:22

tool, integrated and rag tool and integrated Langchain agent. We have combined the concept of

1:46:29

agentic AI with rag. So we have used create retrieval tool, second tool, basically the ticket status tool we

1:46:37

have created. And we have also implemented memory so that our agents can answer,

1:46:42

our agent can answer multi-term query, right? For example, in one query I give, this is my ticket ID.

1:46:47

In the second query, I ask about the status. Will my agent be able to work in this scenario? Will my

1:46:54

agent be able to work in this scenario? Yes, multi-turn memory? Yes. Then everyone, we have from

1:47:01

standalone rag chain to one agent with memory and tools. We have already implemented it. Sounds good, everyone.

1:47:07

Okay. Then I think even some real-life use cases, we have talked about n number of times.

1:47:12

If you see, support bots can, that remembers the thread and pick the right action. We have already

1:47:19

discussed this number of times. And unified memory, retrieval, auxiliary tools in one workflow. We have

1:47:26

implemented all these things in one workflow. Okay. And guys, in the next module, we will be talking

1:47:30

about multi-agent collaboration and deployment. And then we will have the capstone project, etc.

1:47:37

This was the mind map for today's class. Do you all know where this mind map is, you can access?

1:47:45

Don't say that, give us the link. For every class, the mind map is automatically added in your pre-reads.

1:47:52

Okay, pre-reads of every class will contain this mind-map and you can just go through that, like just for a few seconds, right?

1:47:58

And everyone now, we can mark what all the topics we have covered in today's class. So if you see, create an integrator, integrate retrieval tools into

1:48:06

land-chain agent workflow, yes. Combine retrieval tools and auxiliary tools for multi-agent

1:48:12

execution, yes. Enable multi-turn interaction with conversational context and memory. We have implemented

1:48:19

chart history. Absolutely yes. And then everyone, route queries between retrieval and non-retrival,

1:48:25

basically call the retriever, not call the retriever. Evaluate agent performance using bounding

1:48:30

evaluation scenarios and eval packs. So we have already seen the agent, whether it is performing correct or

1:48:36

not correct. Is this point clear to all of everyone? We have covered all these topics in

1:48:40

today's class. Okay. So that's it for today's class, everyone. I think we should have

1:48:45

quiz today, but unfortunately, we don't have the quiz. But anyways, we have written the code.

1:48:51

Okay. So everyone clear with all the concepts for today's class.

1:48:56

Everyone clear with all the concepts for today's class.

1:49:01

Yes. So guys, I am launching the feedback poll. Please take the poll.

1:49:06

Yes, practice you will have to do.

1:49:13

Okay, practice is something that we cannot escape from, especially when it comes to coding part.

1:49:36

Do you have any other examples which we can try from apart from assignments?

1:49:48

Not very handy I have, but I think if you Google about it, you will get a bunch of questions. But

1:49:53

at least, first, you should target to write the code what we are doing in the class as well as the assignment.

1:50:00

After that, maybe think of other things. Otherwise, if you don't complete these things and then you are trying to do,

1:50:06

other things, then it may not help a lot.

1:50:09

Okay?

1:50:10

Folks, please take the feedback poll.

1:50:12

55% people have taken the feedback poll.

1:50:14

I request all of you to take the poll.

1:50:36

Thank you.

1:51:06

Folks, I think all the feedback, we can end, we can end the feedback poll.

1:51:36

Thank you.

1:51:39

So we'll maybe wait for maybe a few minutes, okay, if anyone has any doubt.

1:51:43

Sure, sure.

1:51:44

Maybe 955, after 55.

1:51:48

Sure.

1:51:50

Guys, if you have any doubts, please feel free to drop the doubts in the chat section.

1:51:56

Yeah, who are also there.

1:51:58

If you have any questions, you can ask.

1:52:06

Thank you.

1:52:36

Thank you.

1:53:06

Thank you.

1:53:36

Thank you.

1:54:06

Thank you.

1:54:36

Thank you.

1:55:06

Thank you.

1:55:36

Thank you.

1:56:06

Thank you.

1:56:36

Thank you.

1:57:06

Pila, if you are building a project for resume, this is a good prototype, right?

1:57:14

This is good prototype, right?

1:57:15

This is good for prototyping that what we are building.

1:57:17

But if you are building a project for the resume, then it should have more things.

1:57:20

Maybe it should have some database, right?

1:57:23

The queries or the like all these chat history, you should store in the database.

1:57:28

You should have maybe some front end also, maybe some mobile application or a simple website with which

1:57:33

you connect your backend and database.

1:57:34

Then it is one.

1:57:35

then it is worth adding in the resume.

1:57:38

Okay?

1:57:39

Then it is worth adding in the resume that will have more weightage.

1:57:41

If you just add this, it might not get a lot of weightage, definitely it will get some weightage,

1:57:46

but better if you can add the front end, if you can add a real database with this, right, then

1:57:52

it will definitely be very good.

1:57:59

Yeah.

1:58:05

Thank you.

1:58:35

Thank you.

1:59:05

Thank you.

1:59:35

Thank you.

2:0:05

Okay. What kind of front-end is not part of our course.

2:0:20

Is not part of our course.

2:0:22

Okay.

2:0:23

Front-end is not part of our project of this cohort.

2:0:25

The cohort table is agentic system design.

2:0:28

So we are going to, like, we are discussing agentic things.

2:0:31

I need feedback on a multi-agent system logic for agentic things.

2:0:32

I need feedback on a multi-agent system logic for agentic

2:0:35

content research, right, social distribution system I have started working on.

2:0:40

How can I arrange that for next week?

2:0:42

This is, okay, so you want some feedback on your personal project?

2:0:47

Feedback from me or like a group feedback?

2:1:05

If you want a group feedback, then you'll have to upload your project somewhere,

2:1:09

then circulate a form, right?

2:1:12

Then people will fill the form.

2:1:17

If you want from me, then you can send an email to me.

2:1:20

I will mostly be able to check the project over the weekend.

2:1:25

Saturday, Sunday, okay?

2:1:35

You know,

2:1:37

Thank you.

2:2:07

Thank you.

2:2:37

Thank you.

2:3:07

Thank you

2:3:37

Thank you

2:4:07

Thank you

2:4:37

Thank you

2:5:07

Thank you

2:5:37

Thank you

2:6:07

Thank you

2:6:37

Thank you

2:7:07

Thank you,

2:7:13

Good, good night.

2:7:14

Alright, have a great weekend.