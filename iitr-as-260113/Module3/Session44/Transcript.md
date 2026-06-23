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

Thank you.

16:24

Thank you.

16:54

Thank you.

17:24

Thank you.

17:54

Thank you.

18:24

Thank you.

18:54

Thank you.

19:24

Thank you.

19:54

Thank you

20:24

Thank you

20:54

Hi, everyone.

21:00

Very good evening, folks.

21:02

Am I audible to all of you?

21:03

Hi, everyone.

21:06

Am I audible, visible and my screen is also visible to all of you?

21:12

Okay, great.

21:13

Good evening everyone and welcome to the class.

21:16

Okay, great.

21:18

So today, I think today's class is the last class of this module, right?

21:23

From next class, that is the next week, we will start the new module.

21:28

Okay?

21:29

And in the new module, we will be talking about a lot of frameworks of building agents like N8N,

21:35

crew AI, etc., etc.

21:37

We'll be having multiple agents discussion in the upcoming module.

21:40

And all the information and all the knowledge that we have gained in last two, three modules, right?

21:46

I think this is the third module, right?

21:48

If I remember the number correctly, whatever information we have gained in three modules, we will try to

21:53

incorporate those things in the next module.

21:56

Sounds good?

21:57

Sounds good, everyone.

21:59

Okay, so let's get started with today's discussion, everyone.

22:02

Today's class is very, I would say, a straightforward class.

22:05

There will be slightly few things that we will discuss might be new,

22:10

but 80, 90% of the things, maybe 70% of the things that you already know.

22:15

But we are just going to take different examples, different use cases, hands on, right?

22:21

As the title of the class is hands on,

22:22

hands on real world use cases.

22:24

We will walk through some of the use cases, right?

22:28

So let's get started everyone with today's discussion.

22:31

So first of all, what is the agenda of the class?

22:33

We will be discussing at least maybe two, three, four use cases,

22:36

real world use cases of building agentic AI application.

22:39

But what are we actually going to implement?

22:42

Right?

22:43

We will take multiple examples.

22:44

Implementation wise, everyone.

22:46

We will implement something called as HR onboarding assistant.

22:51

Any cases, what this might be?

22:54

HR onboarding assistant.

23:09

This agent we are going to implement.

23:11

Now everyone, when you join a new company,

23:13

can I say that you have to go through a lot of formalities.

23:16

You have to complete certain trainings,

23:18

join some orientation sessions and whatnot.

23:20

and whatnot. Correct or not, everyone?

23:22

So all these things, we would try to automate.

23:26

Because everyone, whenever you join a company, there will be one person

23:29

who will be guiding you through all these things,

23:32

that this is step one, step two, step three, and so on,

23:34

and that person will have to do a lot of things manually.

23:37

We will try to understand that.

23:38

Can we automate those things with the help of the agentic AI application?

23:43

And ultimately, everyone, this is something that we are going to implement.

23:47

Let me copy this instead of writing this.

23:49

instead of writing this completely,

23:51

why this is not getting copied?

23:58

Okay, anyways, let me read that.

24:02

An HR onboarding assistant is an agent that helps new employees

24:07

to understand the joining formalities, benefits,

24:11

right, leaves, insurance benefits, etc., etc.

24:16

Equipment setup, a laptop will be given, then you have to

24:19

to set up the laptop, leave policy, some mandatory trainings, orientation sessions, etc., etc.

24:24

All these things we would try to automate using an HR onboarding assistant.

24:28

Everyone, clear?

24:30

Okay. Now everyone, before we implement the HR onboarding assistant, we should try to understand

24:35

that most of the enterprise agents, right?

24:38

All of you understand what is the meaning of enterprise agent?

24:41

All of you understand the meaning of enterprise agent?

24:45

Tell me.

24:48

If you know, tell me the meaning of...

24:52

Enterprise means what?

24:53

Enterprise means company.

24:54

Okay?

24:55

Now when you run an agent at a company level, not only for testing, not only for demo, exactly, a production grade agent, they follow certain scenario, right?

25:04

Let me copy that.

25:06

Right?

25:07

So I think, yeah, this will get copied.

25:09

This is a big flow.

25:16

flow. Instead of drawing this, I just want to, yeah. This is the common enterprise agent pattern, everyone, that generally

25:26

production level, production grade applications, specifically agents, follows. User ask a business

25:31

question, right? That question related to finance, onboarding, HR, joining, and whatnot.

25:37

Agent, like the agent that you have implemented, it will try to understand the content or the context

25:42

or the intent. Intent means the idea.

25:46

behind the question, that what you are trying to ask, agent retrieves policies or business

25:51

context. This is RAG, right? You, your agent will retrieve the policy documents from vector database.

26:00

So this is a RAG application. Then agent calls tools, right? For example, if you want to send an email,

26:05

if you want to pay the taxes, right? If you want to apply for a leave, if you want to allocate a laptop,

26:10

all of these, everyone do anything? These are agent tasks. These are tools that you have to implement.

26:14

These are external actions that you have to.

26:16

have to take. So you have to write multiple tools. There will be tools. And then

26:19

everyone, agent will also have to validate the response, right? As per the rules. Whatever

26:24

rules you have defined to your agent, your agent should always respond within those rules.

26:29

It should not answer randomly. Okay? And finally, everyone, agent will reply with the final

26:34

response plus some evidence, right? For example, everyone, do you remember the concept of citation?

26:41

That whenever you are answering everyone, if you can give the citation, if you can do the citation,

26:44

or if you can do some, attach some sources, that as per this policy, this is the rule.

26:49

As per this log, as per this document, this is the rule. So you provide the evidence and then you can

26:54

also tell the user the next steps. That, for example, let's say if you have applied, let's say you

27:00

have allocated a laptop to the new employee. Okay? You have allocated a laptop to the new employee.

27:06

Then after allocating the laptop, then you can give them the next steps that, okay, you can follow

27:10

this document to set up your laptop. Does that sound good to all of you?

27:14

Does that sound good to all of you?

27:16

So this is what HR onboarding assistant, everyone, we are going to implement.

27:20

Let me give you one more example that how can we use agent in finance domain, in finance domain?

27:27

So let's talk about finance use case.

27:36

Let's talk about finance use case.

27:40

Now, what do you think, everyone?

27:42

Can we use agentic AI applications in?

27:44

in the world of finance?

28:14

Thank you.

28:44

Sorry, everyone.

29:14

Folks, am I audible to all of you?

29:18

Okay, sorry, somehow my internet went off.

29:21

I have to, I had to connect with my hotspot.

29:24

Okay, internet completely went off.

29:26

Anyways, let me share my screen again.

29:28

And Somia, I think you will have to make me the co-host again.

29:32

I'm not getting the everyone option if I have to share anything.

29:36

Okay?

29:37

Is my screen in visit now, everyone?

29:39

Yeah.

29:40

So folks, we were talking about finance use case, right?

29:43

That finance may, there are a lot of use cases.

29:44

Guys, I don't have the host rights.

29:49

I think once Somiya is there.

29:51

Sama, are you there?

29:57

Guys, am I audible to all of you?

29:59

Cauchel is saying I cannot hear.

30:00

He cannot hear.

30:02

Am I audible?

30:03

Yes, Kossal try to rejoin.

30:07

Okay, perfect.

30:08

So guys, in the finance use case, what can be done using agent, right?

30:11

I was taking this example, everyone, that if let's say I have,

30:14

have built or let's say we have built an agentic AI application to approve reimbursement

30:19

automatically. So, every company provides a lot of reimbursement. For example, internet reimbursement,

30:23

Wi-Fi reimbursement, mobile reimbursement, travel reimbursement and whatnot. Now, everyone, let's say if

30:29

that agent approves reimbursement randomly, if I went on a personal travel and still I apply for the reimbursement

30:37

and that agent approves it, don't you think it is a blunder? Correct? It is a blunder. Before approving or

30:44

not approving the reimbursement, the agent should check the reimbursement policy of the company.

30:50

Any approval or disapproval cannot be done randomly. If you are approving it, it should be as per

30:55

the policy. If you are disapproving it, if you are rejecting the reimbursement, it should also be as per

31:00

the policy. Is that point clear to all of you? For example, everyone, like a lot of businesses,

31:05

they have to pay GST every month, right? Whatever GST they collect from the customer, they have to

31:10

pay every month. Don't you think even this process can also be automated? That GST?

31:14

or tax policies, right? These can be automated. Then everyone, some invoices can be generated,

31:20

vendor payments can be validated and whatnot. All these things can also be done via, all these things

31:25

can also be done via agentic AI. Is the idea clear to all of you? Everyone clear? So what kind of

31:33

agents we can have, for example, let's say, get employee grade. For example, check the employee status.

31:39

Like, for example, at different levels, you have different reimbursements, right? For example,

31:44

fresher will get a different reimbursement policy. And for example, let's say if some employee is

31:49

very senior, they might get different reimbursement policy. So you might have to check the employee status,

31:54

employee grade, then you have to calculate the reimbursement amount, then you have to pay the reimbursement

31:58

and whatnot. All these things can be done using agentic AI application. Now let's come back to our

32:03

actual use case, everyone, which is HR onboarding assistant. So this is actually a very practical

32:08

example, a very real world example of agentic

32:14

AI application. A lot of companies are already doing this. Okay? Absolutely. So it is a very

32:21

practical use case, everyone. HR onboarding assistant. Now, what are the common questions that an employee

32:27

can ask, right, when they are joining new to any company, right? What documents do I need before

32:33

joining? For example, your Adhar card, pan card and whatnot, right? So you can write an agent to validate

32:37

these details, correct or not? Basically, to do the background verification of the employee. To check the

32:43

employee history, correct? Which companies they have worked upon, which companies

32:49

they have worked in, whether they have worked in the companies they have mentioned in the resume

32:52

etc, etc. Then everyone, given the laptop, right, you will have to allocate a laptop to the new

32:59

employee at the time of joining, right? Then everyone, you have to allocate the trainings also. You have

33:03

to block, you have to send the event or you have to send the calendar invite to the employee

33:09

for mandatory trainings, onboarding trainings. And all these things can be automated.

33:13

everyone, clear? So, guys, do you see that in HR onboarding assistant as well, we are going to have

33:19

some kind of vector database? Because for everyone, for example, let's say, at the time of onboarding,

33:25

companies gives you relocation bonus. Okay? For example, let's say if you're traveling,

33:29

etc. You can get the amount reimbursed up to a particular limit. Let's say 50,000 rupees, 1 lakh

33:34

rupees. So that employee can get the travel expenses getting reimbursed, right? But everyone tell me,

33:43

we can automate this. But again, the agent needs to verify the policy details, right? That

33:49

what is a reimbursement limit? Whether the invoice is valid or not, invoice is accurate or not, right? If

33:55

the employee is not asking for random reimbursements and whatnot. So all these things, everyone, all of you

34:00

understand that, you need to store policy documents in the vector database, just like we have done

34:04

previously. Correct? Then only agent will be able to validate the policy documents. Correct or

34:09

not? Absolutely. Then everyone, uh,

34:13

Other example could be content use case. For example, even a lot of people are actually writing agents to automate the content. For example, let's say they have to upload a video on YouTube or they have to write a LinkedIn post or they have to write a post on Facebook, Twitter, etc. They can automate that. So just use the agent and automate the agent that I have given you the list of topics. Every day, same time, upload the post automatically. Given the prompt, upload the post automatically, so that my consistency remains in.

34:43

Everyone, clear? By the way, everyone, I also try to upload content on LinkedIn very, very regularly, but somehow I am not able to do so.

34:54

Okay? I try my best. Sometimes I am very regular. Sometimes I'm not. So feel free to, okay, I cannot send message to everyone. All of you have my LinkedIn ID.

35:07

Search my name on LinkedIn. Once Swamia is there, I will also send the link to all of you.

35:13

Please do follow me on LinkedIn. I try to write content regularly. And also I'm planning to maybe do something in future. So you will get notified about it.

35:22

Okay. Thank you. Thank you. Thank you, thank you, thank you, sir. Okay. So guys, you can also write a content creator agent, right, which can upload the content automatically on your behalf given a proper prompt. Everyone clear with this example as well?

35:37

Okay. Now everyone, let's start with the implementation part. And we are going to implement HR onboarding assistant. In this HR,

35:43

onboarding assistant, everyone. These are the things we will try to implement. This agent, this agentic AI application, it should be able to search or it should be able to retrieve policies, HR policies, company policies. It should be able to take actions, okay? For example, action means assigning the trainings assignment to the new

36:13

employee. Training's assignment to the new employee. For example, let's say maybe allocating a laptop.

36:24

Allocating a laptop, etc. So all these things that we want, we will try to implement. So should we

36:33

start the implementation, folks? Should we start the implementation? Okay. Let me share my

36:43

board screen with all of you. I think all these things you already know by now, right?

36:48

It was just a quick recap for 10, 15 minutes. That's what we are going to do. I believe that if you're

36:53

attending these classes, then I think you must have got a very, very fair understanding of all these

36:58

things, right? That what all the things we can automate using agents and what all the things we should

37:02

take care of. So everyone, let me share my screen. And now we will create.

37:13

a new project. Either we can create a new project, folks, or what we can actually do is

37:17

we can use the existing folder so that you don't have to manage so many repositories. That is the only

37:22

reason. Yeah. So this is our folder, everyone, Langchain app. And here we will write one more

37:30

application for, I understand the code, but sometimes remembering the syntax is a task. Again,

37:35

once you don't have to remember the syntax. No one can do that. Once you do practice, right,

37:39

once you write the code for maybe two times, three times, once you build two, three, you build two, three,

37:43

four, five applications, then eventually you will start remembering some of the things.

37:47

To the point, you don't have to remember step by step everything. Okay, Bench? You just have to remember

37:53

the context that, okay, this is how we build an application. And how will you start remembering that?

37:56

If you build maybe five, four or five applications, automatically it will start building up.

38:01

Okay, don't spend a lot of efforts on remembering things. Okay? Okay. So guys, let's get

38:07

started and we will implement a new file here.

38:13

And let's call it as HR onboarding. Can we create a new repository? Should we create a new

38:20

repository, folks? Or should we use the same one? The only reason that I was doing this is because you don't

38:26

have to manage so many repositories then. That is the only reason. And this is just going to be one

38:31

file, HR onboarding assistant. That's it. Okay? I don't have any problem in creating a new

38:36

project as well. I have tried to give better names. For example,

38:43

if you see, all the rag applications, they have Langchain Rag. Okay. So if you have to,

38:48

let's say, revise the rag code, you just have to go through these four files, right? If you have to go

38:53

to memory part, if you want to understand the memory part, these are the two files for memory. Without

38:57

automation, with automation. Then if you want to go through stateless agent, then this is the file.

39:05

Okay. Yes, there is only one file, much. So better if we can continue in the same folder. So HR.

39:13

onboarding agent.py. Okay, let's start writing the code everyone. Again, we will go to the terminal

39:22

first of all and we'll try to install the required dependencies, right? Required libraries, required

39:27

frameworks. We already have it just to make sure that we don't miss anything. That's why we

39:32

are downloading it. Install Lanchine. Then we are going to use Open AI, LankChain,

39:38

open AI, right? Langchain, Langchain, long chain core. That's it. Let's install all these

39:46

things everyone. All of them are already there. Requirement already satisfied. Okay? Then everyone will start

39:51

writing the code. Now, what all the things we would need from here is, from Langchain underscore

39:59

core, we would import Langchain. Dot documents because everyone, do you remember that?

40:08

we need to have documents for storing that into the database, into the vector database, policy documents, right?

40:16

So, import, document object. We have done that already. We have used it already. Lankchain underscore code. This is something new, everyone that we are trying now.

40:26

Vector stores. Okay. As of now, everyone, for vector database, what did we use earlier in our classes for vector database? For vector database?

40:35

Croma database. Today I will show you that Lanchine also

40:38

gives you an in-memory vector store. This is a new thing that we are learning today. Okay,

40:42

Lankchain also gives you a vector store that you can use. Everyone, clear? So from Lankchain code

40:48

dot vector stores, we need to import in-memory vector store. As the names suggest everyone,

40:54

this is a vector database, which is coming from Lankchain in memory. Okay, that means it will store

41:00

memory, it will store the code in memory. It will store the data in memory. From Lankchain. Dot tools,

41:06

import tools. Obviously, we are going to write a lot of tools today. And then everyone,

41:11

to create agent, if you remember from Lanchine.Agent, we have already used this create agent. Remember

41:18

that? Create agent, we have used, tool we have used, document we have used, in memory vector

41:24

store is new thing that we are using. Okay? It will have some limitation, obviously. It will be by

41:29

default, like, obviously, the maximum amount of data that you can store in memory is the limit of

41:35

your laptop, not more than that, right? But in production systems, you may not be using

41:40

in memory. You may be storing the actual database like Croma. Okay? And then everyone from,

41:46

because we have to generate the embeddings from Langchain underscore open AI, we will import

41:54

open AI embeddings. Okay? Is everyone clear till now? Now everyone's step number one. Okay.

42:03

Step number one is, we have HR policies, HR policies, HR policy, HR policy documents.

42:13

Okay? So I have already created a set of documents, a sample HR documents data. Let me copy that.

42:21

So this is a sample HR documents, everyone. If you can see this, if you see, this is one document, this is another document, this is next document and so on. So total we have five, six documents.

42:32

And if you see every single,

42:33

the content of the document is this. Before day one, every new employee must complete

42:37

verification, bank account details, non-disclosure agreement, NDA, emergency contact details, and

42:43

whatnot. And everyone, the source of the policy, this is first document. This is second document. This

42:50

is third document. And this first document is around pre-joining formalities. Then second document

42:55

is around leave policy. Third document is around mandatory trainings. Fourth document is around

43:00

benefits and insurance and so on. Is everyone clear with this sample database?

43:08

Is everyone clear with the sample policies database? Okay. Then everyone, just to make our application

43:14

work, just to write the working code, we would need some sample employees also. Okay, second step is

43:20

we would have some employees database. Employees database. Okay. So everyone, I have two sample

43:27

sample employees, E101, name is this, E102, name is this. Everyone clear?

43:35

Okay, name is this, role, location, remotely, and so on. Sample database. I have a question

43:42

whether we can make a function that would work, that would work from. I have a function. Whether we can

43:48

make a function, I did not get this point. I have a question whether we can make a function that would

43:54

work from. Sorry, can you please elaborate?

43:57

we can do that. We can do that. I think we have done that in the previous classes also.

44:03

Okay. Okay. Now everyone, the third step is embedding model. Embedding model. Okay. We can use external

44:14

documents also like PDF1 word. In one of the classes I showed you that, right? Once, I think in the last

44:18

module, I don't remember the class name, but in one of the classes, I showed you the entire step-by-step

44:24

process. We have done that. Okay. Just to make, just to not.

44:27

repeat the content again and again, I'm taking this sample database. Okay? Then everyone

44:34

creating the embedding model and let's say embeddings, embeddings is equal to open AI embeddings. And

44:40

here everyone, you can define the model. Which model we are going to use for embedding? The model is

44:47

going to be text embedding three small. This is the model, everyone, which comes from open AI. I think we have

44:55

used that in the past as well multiple times.

44:57

Then everyone, we will create a vector store.

45:01

Instead of using chroma database, we are using in-memory store today, in-memory vector store.

45:06

So in-memory vector store. And here, everyone, we will provide the embedding.

45:09

Which embedding model we are going to use? We are going to use this above model.

45:14

Can you see that, everyone? Everyone clear till now?

45:17

First, we created the embedding model, and then we are providing this inside the vector store.

45:21

Because vector store ultimately is going to use the embedding model to create the embeddings while

45:25

storing the data as well as, while storing the data, we need to use embedding model.

45:30

Also, when do we use to, when do we need to use the embedding model again?

45:35

While retrieving the data. Correct? While search also, you convert the query into embedding

45:40

and then you perform similarity search. Everyone remember? Okay. And then everyone, in this vector

45:46

store, we will add these documents that we have defined above. And what is the name of the

45:51

document? HR documents. So it will automatically create the embeddings and store.

45:55

in the database. In vector store. Is everyone clear? Very easy to use, right?

45:59

just two lines of code. And your vector database is ready. Okay? Then everyone, we will create the

46:05

retriever for this. We will create the retriever for this to retrieve the data. So vector store.

46:11

Dot as retriever, same function we have used in the past also as retriever. Can anyone

46:16

recall what things we need to pass inside the retriever? Any guesses? If you remember, if you can

46:25

try to remember the rag class. Should I show you that? Lanchine Rag app. And if you see

46:31

everyone, we have created a retriever here as retriever. Here we have to provide the search similarity,

46:37

the search types as well as arguments. That's it. All the above things you have already defined

46:43

in the vector store, collection name, embedding function, etc. parser, whatnot. You have already

46:47

parse the data. The only thing that, and documents, you don't need documents to pass at the time

46:52

of retrieving. Documents, you have already stored.

46:55

You have already stored the documents inside the vector database. So here you just need to pass the similarity search as well as the top. How many elements do you want? Also everyone search this search type, that is similarity. It is optional in vector store. So here you can just pass the search arguments. Search K arguments. And here everyone, you need to provide the K value. Okay? K value is equal to three. Okay. That I need top three matching elements.

47:25

top three matching documents. Is that point clear to all of you?

47:30

Everything we have done in the past, we are just using it again.

47:36

Correct or not, everyone?

47:40

Okay. Now everyone let's create a tool. The first tool, this is the step number four.

47:46

So tool for searching HR policies.

47:55

Okay, tool for searching HR policy. So you define a function deaf.

47:58

Name of the tool could be, let's say, search HR policy. To search HR policy, everyone,

48:08

what input do you need everyone? What do you need everyone? What do you think? How will you search the

48:11

HR policy? HR document object contains metadata? Yes, it contains metadata also.

48:17

Right, Chandan. It contains the page content and metadata. Okay.

48:23

Tell me everyone, to search policy.

48:25

you need the query, right? That for this query, for example, if your query is about reimbursement,

48:30

then it should retrieve the reimbursement document. If your query is about leave, it should retrieve the

48:35

leave policy document. So you will provide the query. Correct or not, everyone? As of now, this is a

48:42

normal function. How will you make this as a tool? With, at the rate, tool annotation. Correct

48:47

or not? With at the rate, tool annotation. And inside this, everyone, what is the first thing

48:52

that you give inside the tool?

48:55

Inside the function, what is the first thing that you define everyone?

48:58

You write the function description. Remember? And this description should be very good.

49:03

Should be self-explanatory. Okay? So what this tool does? This tool search. This tool search HR policy documents and search and retrieve and return the relevant

49:25

policy documents to the, uh, documents, right? For the given, for the user query.

49:36

Is this, is this, uh, description making sense to all of you?

49:42

Is this description making sense to all of you? You can also add this one more description that

49:46

use this tool to use this tool when the user ask, ask.

49:55

about onboarding, leave policy, reimbursement policy. What all the policies

50:04

we have? Join pre-joining, leave policy, mandatory trainings, benefits, and so on. So, onboarding,

50:12

leave policy, benefits, and so on. So, onboarding, leave policy, benefits, insurance, trainings,

50:20

etc. Is that point clear to all of you? Is that point clear to all of you? Is that point

50:27

clear to all of you? Yes, no? Okay. And then everyone, you will simply do what? That documents,

50:35

the retrieved documents, you will simply do vector store, uh, sorry, retriever, dot invoke

50:41

this query. That for this query, give me the document. So it will automatically perform the

50:47

similarity search and it will give you the top three matching documents.

50:50

Is that point clear to all of you? It will automatically perform the similarity

50:54

search and give you top three matching documents based on the similarity based on the

50:59

semantics. And everyone, you can also see if not docs, if docs is null. So you can also return

51:04

that for this query, no relevant policy document found for the query this. Let's say for the given

51:18

query, no policy document found. Is that point clear to all of you, folks? Don't we need to

51:26

do the embedding of the query? It will automatically do that. It will automatically do that. Okay?

51:36

Here also if you see, here also, if you see, uh, I think there, if you see query, yeah, if you see

51:44

the question we are passing as it is. Internally, it will create the embedding and then it will perform

51:48

similarity search. Here also if you see, we are passing the question as it is. Okay, this is the

51:52

question we are passing as it is. Internally, it will create the embedding and then it will perform

51:56

the similarity search. Without embedding, similarity search cannot be performed. Do we also

52:00

give the usage and output example in the documents or are they redundant for the agent? Do we give the usage

52:08

and output examples in the document string? You can give. Again, it is optional. You can give. In this

52:14

string you are asking, right? Yes, you can use. Yes, you can use.

52:18

you can definitely provide. Example usage. Again, like may not be required. May not be,

52:23

maybe agent might able to figure it out. But better if you provide, I think there is no problem in that.

52:29

Okay. But it does not matter a lot, I guess. Okay. Then everyone, finally, what we have is we will

52:35

create the results array. Empty results array. And what you do, everyone, is you will iterate through

52:42

each doc for doc in documents. What you will do is, you get the source of the source of the

52:48

document? How will you get the source of the document every one? Source means meta data, right?

52:52

So can I say that from the document, go to metadata and get the source value? Okay? From each document,

52:59

document dot metadata, dot get the value of source. Is that point clear to all of you? Correct?

53:10

Because you have to give the source as well. That if I am answering this query, right, if I'm giving you

53:15

this answer, this answer is coming from this policy document. This is the source of this

53:18

correct everyone? That's why we are using, we are extracting the source from the document.

53:24

Okay? Now what if everyone, let's say this source does not exist? For example, by mistake, for some

53:30

document you forgot to provide the source. Then what will happen? What this value will get? What

53:37

will be the value of source now? It will be null. It will be none, right? So guys, you can provide a default

53:42

value here. Do you know that? In get function, you can provide the default value. That if the source is not

53:48

available, you can make it unknown. Everyone clear? You can make it an unknown source. Is that

53:58

point clear to all of you? So unknown will become the default value. And then everyone, the section,

54:03

the actual content of the document. Section means what? If you see, this section, not the content actually.

54:08

Kind of you can say that. Source means the name of the document. Section means the type of the

54:13

document. Everyone clear? So similarly everyone, you can copy base this.

54:18

that now give me the section of the document. That what this document is all about.

54:24

Is everyone clear? And guys, in this results folder, you will append, right? You will append this

54:30

source and section and document content. Okay? So what will you do everyone is? In the string format,

54:37

you will upload, you will do this. Let's say for example, you will add the source. Definitely you can

54:42

make it formatted string. That this is the source. This is the section. And this is a source. And this

54:48

is the content. Okay. And how will you get the content, everyone?

54:53

Content is nothing but page content. Okay, document dot page content. Document, doc,

55:00

content is equal to doc. Dot. Is that point clear to all of you? Okay. And here everyone,

55:09

you will see that page document content. This is how everyone, you will add all these things in the, like,

55:17

separated by any symbol. And if you see one string represents the information about one

55:23

document, everything is there, source is there, section is there, page content is there. Again,

55:28

I'm telling you one of the ways. It's not mandatory that you have to do the same way. Can we

55:32

implement a wear condition, wear condition to metadata in this retriever like we did in earlier rag?

55:39

What condition? Which condition do you mean, Shantro?

55:46

Yes, yes. You can do that.

55:47

See, this vector store, there we used a chroma database. Here we are using vector

55:56

database, vector store, in memory vector store. So the functionalities may be different. Okay,

56:01

the chroma data, like this vector store, in memory vector store must be having slightly limited

56:05

functionalities because chroma is a different type of database. It gives you much more flexibility.

56:10

Okay. So if you have to use advanced functionalities, then maybe you can go with, what do you say,

56:15

the chroma database. Okay?

56:17

Is that point clear to all of you?

56:19

And finally, everyone, we will just return this results.

56:24

Okay? So is this tool making sense to all of you folks? Yes or no?

56:29

Okay. Then everyone, we will write another tool,

56:33

DEF, get employee information. Get employee profile.

56:39

To get the employee profile, everyone, what input parameter do you need?

56:44

What input parameter do you need everyone?

56:51

You need, obviously, employee ID.

56:57

And employee ID will be of what type?

57:00

It is, let's say, string type, or integer type, whatever.

57:03

Okay? Here we are, we are taking string type.

57:06

And this is also a tool.

57:08

Okay, here also everyone, you can write a small description of a

57:13

a small description of the tool, that what this tool does, that this tool, this tool,

57:20

tool to get the employee information from the given, for the given employee ID. So use this tool, use this tool to use this tool to use this tool to

57:43

fetch employee information from database. Is this point clear to all

57:54

of your folks? Okay. And how will you do that everyone? Simple. Employee is equal to

58:00

employees dot get the employee for this employee ID. Okay. If the employee is not there, if not

58:08

employee, if employee is not found, then you can read.

58:13

return a string here, right? You can return a string. Something like this, let's say,

58:19

employee, with ID, employer ID, not found in the database. Is everyone clear? Is everyone clear?

58:37

Okay. You can make, like, I will tell you one more way that you can make it slightly more sophisticated, right?

58:43

For example, everyone, I'll give you one more idea here. Let's say, if you just want to check

58:49

the employee is there or not, you will call this function with some employee ID. And if you are

58:55

getting this string, don't you think, everyone, it will be slightly difficult for you to compare

58:59

this string that whether the employee was found or not? What if in the return, if I just

59:05

send the status, found not found, along with this string, will that be better? So instead of

59:12

just returning this string, what if I return something like this? And then tell me everyone

59:16

whether it is better or not. Okay? So you can send some found status, right, whether it is

59:21

found or not. So here it is false. And then everyone, you can pass some message also. And this string

59:26

you can pass in the message. What do you think? Is it going to be slightly better? Now, what will

59:31

happen everyone now? You call this function. You get this JSON object. From this JSON object, let's say

59:36

response. Response. You can quickly check whether you found the employee or you could not

59:42

found the employee. You could not find the employee. Getting this point, everyone,

59:47

just a slightly different way of using this. Okay? And here everyone, if employee is not null,

59:54

then what you will do is, you will return again a JSON object. You will have the found value. Found

59:59

is obviously true now. Then a message. Or let's say maybe employee ID you can say.

1:0:05

Employee ID is anyways coming in the input. So maybe you can skip also. Employee ID. Also everyone,

1:0:10

you can pass the actual employee.

1:0:12

Employ. Employ. But everyone now tell me, how will you pass this employee here? How will you

1:0:18

pass this employee here? Employee is an object. Correct? Employee is an object. This is an object.

1:0:25

This you will get as an employee. How will you pass this inside the JSON? Don't you think even

1:0:32

this is itself a JSON? This is itself a JSON. You just have to attach this with the JSON. Correct.

1:0:40

So what you can do everyone is, because you are converting this into kind of a string JSON from objects. See, as of now, you are getting employee object. Now you want to convert that into JSON, string JSON. What you can simply do is you can do double star. If you remember everyone, this double star we have used in Pidenti class. What is this called as? Can anyone recall? What is this called as double star? Unpacking. Very good.

1:1:04

A lot of people remember that. Very good, everyone. I'm very happy that you are remembering the concepts from the previous classes. Unpacking.

1:1:10

So you are just unpacking the object into the, in the form of JSON.

1:1:13

And you are sending that in the JSON object.

1:1:16

So this is the get employee profile everyone. This is the tool.

1:1:20

Is that point clear to all of you? Yes or no.

1:1:28

Okay?

1:1:29

Then everyone, you can write another tool for training recommendation.

1:1:34

Define. Get training.

1:1:40

for employee ID or for role. Let's say you are taking the role. If you see everyone

1:1:44

can as to that, the trainings will be different for different role. For backend engineer, there

1:1:48

will be different training. For product managers, there will be different trainings. Okay? So what

1:1:52

you will take is everyone, you will take the role in the input and you will also write this as a tool.

1:1:58

Are you guys getting this point?

1:2:04

Folks clear, yes or no. And here everyone, you will write, let's say, what this tool does,

1:2:10

this tool is used to get the mandatory trainings, mandatory training recommendations

1:2:21

for a new joining, a new employee based on their role. Is the tool description making sense

1:2:32

to all of you, everyone? Okay. For this, everyone, you will have maybe a sample database of common trainings.

1:2:40

Okay. Let's say there is a list of common trainings.

1:2:46

Okay. In this common trainings list, everyone, you will have lists like maybe security training.

1:2:53

Okay. Maybe let's say code of conduct.

1:2:57

That these are the common training that every employee has to go, irrespective of the rule.

1:3:01

Data privacy. Data privacy. Right. Then everyone, let's say maybe anti-harassment or

1:3:10

any kind of those trainings, right? Anti-harassment training. Is that concrete

1:3:20

all of you? These are the common trainings. Okay? Then everyone, there is a role-specific training.

1:3:30

A role-specific trainings. And for role-specific trainings, everyone, you will have to create a dictionary here.

1:3:40

that's for backend engineer. Let's say what are the trainings, everyone? Let's say maybe

1:3:45

you can store multiple trainings here. Let's say Python, Fast API, maybe Agentic AI, something like

1:3:58

this, okay? Is everyone clear? And then everyone, you will have, let's say, product training for product

1:4:03

manager. Okay? Maybe let's say client interaction training.

1:4:10

Okay. Then everyone you have, let's say, maybe data handling training, client data handling.

1:4:21

Is that point lead to all of you? These are just the common trainings as well as the role-specific trainings.

1:4:27

For now, we just have two roles. In future, if you have more roles, you can keep on adding here. Okay? And everyone, what do you have to return now is? What do you have to return now is? Can I say that everyone, that what are the mandatory trainings?

1:4:40

mandatory trainings that every employee has to go to, has to go through. Can I say that common

1:4:46

trainings will be mandatory trainings? Okay? And for role specific training,

1:4:52

role specific training, role specific trainings will be from this dictionary, get this, get the role specific training

1:5:07

for the given rule. Is this function also clear to all of you? Have a look at it and

1:5:13

tell me, is this tool also making sense to all of you? Okay. So, we are done with almost half

1:5:21

of the code, right? So we can go for a break now, everyone. And I'm pushing this code to GitHub,

1:5:27

giving you the link. Please go through this. What we have done till now? HR on boarding assistant.

1:5:37

Okay, go to the GitHub link and have a look at it.

1:6:07

Okay. Please go through this and it's 855. Take 5 to 7 minutes of time to go through the code.

1:6:16

5 to 7 minutes of break. So let's meet around 9, 10. Okay? And then we'll continue a discussion.

1:6:21

Please go through the code. If you have any doubt, ask after the class. Okay? See you after the break everyone.

1:6:37

Thank you.

1:7:07

Thank you.

1:7:37

Thank you.

1:8:07

Thank you.

1:8:37

Thank you.

1:9:07

Thank you.

1:9:37

Thank you.

1:10:07

Thank you.

1:10:37

Thank you.

1:11:07

Thank you.

1:11:37

Thank you.

1:12:07

Thank you.

1:12:37

Thank you.

1:13:07

Thank you.

1:13:37

Thank you.

1:14:07

Thank you

1:14:37

Thank you

1:15:07

Thank you

1:15:37

Thank you

1:16:07

Thank you

1:16:37

Thank you

1:17:07

Thank you

1:20:07

Thank you

1:20:37

Hi everyone. We are back. I have one

1:20:41

I have one question regarding HR policy document. In this policy, we are using only

1:20:45

only document three times. Why we are not using document one?

1:20:48

We are using document three times. We are using document three times. What do you mean by that? You mean this document?

1:20:55

Amarjid, you mean this document?

1:21:01

So this is see, this is document object. See, this is document object which lanchin gives us. Okay, if you see this is document object which lanchin gives us. Okay, if you see, this is the document object and inside

1:21:10

you are passing two things, page content and metadata.

1:21:13

This is document object.

1:21:15

Okay?

1:21:16

So all of these are actually document objects.

1:21:20

Make sense, Amarjid?

1:21:22

So that Lantern can understand that.

1:21:23

These are documents actually.

1:21:25

Okay.

1:21:26

So folks, let's move forward.

1:21:28

I hope all of you have gone through the code in the break, right?

1:21:33

Correct?

1:21:34

Okay.

1:21:34

Now everyone, we have three tools now.

1:21:36

How many tools we have?

1:21:37

One, two, and three.

1:21:39

Three tools we have implemented, vector store we have implemented.

1:21:42

Now everyone, it's time to give the system prompt.

1:21:45

Okay.

1:21:45

So it's a fourth step.

1:21:48

This is the fifth step.

1:21:51

A tool to get the employee profile.

1:21:58

Okay.

1:21:59

Then this is the tool to get mandatory.

1:22:09

training trainings for a given rule.

1:22:13

Okay.

1:22:13

Now, everyone, the seventh step is the system prompt.

1:22:17

Everyone knows what is system prompt, everyone?

1:22:19

Please let me know.

1:22:26

Tell me.

1:22:28

System prompt is a prompt that will go to your LLM.

1:22:31

Right?

1:22:32

And can I say that system prompt will be given with every query?

1:22:36

In system prompt, you define set rules.

1:22:39

that what rules your LLM should follow?

1:22:41

Correct or not, everyone?

1:22:44

Clear, everyone?

1:22:45

Okay.

1:22:45

So guys, I already have the system prompt.

1:22:47

It is very big.

1:22:48

So instead of writing it again, I can copy-paste this.

1:22:52

Okay?

1:22:52

So this is your system prompt.

1:22:54

So what is this?

1:22:55

What is the system prompt, everyone?

1:22:56

You are a HR onboarding assistant for a company.

1:22:59

What are your responsibilities?

1:23:00

Help new employees understand onboarding steps, leave policy, benefits, etc.

1:23:05

Use HR policy for this.

1:23:07

Use, we can get.

1:23:09

remove this one.

1:23:12

Yeah.

1:23:13

So this is step number four,

1:23:16

five,

1:23:17

and six.

1:23:19

If you see,

1:23:20

use HR policy whenever

1:23:21

answer depends on a company policy,

1:23:23

use company employee profile,

1:23:25

look up whenever the answer

1:23:27

needs personalization.

1:23:29

Never invent a policy.

1:23:30

Don't try to create your own policy.

1:23:32

If evidence is not found,

1:23:33

say that HR confirmation is required.

1:23:35

Okay?

1:23:35

It means that ask for the human approval,

1:23:37

right?

1:23:38

Human assistance.

1:23:39

Always include evidence, source IDs, et cetera, citation.

1:23:42

Keep an answer clear, professional, and concise.

1:23:45

What is the format of the answer?

1:23:47

Give the answer.

1:23:48

Give the evidence.

1:23:49

What actions have been taken?

1:23:50

And if there is any escalation,

1:23:53

if there is any next step.

1:23:55

Is everyone clear with this?

1:23:58

Okay?

1:23:59

This is system problem.

1:24:01

Then, folks, step number eight comes in model,

1:24:04

or basically LLM.

1:24:06

So everyone, we will simply use this model.

1:24:09

is equal to, let's say, model name,

1:24:12

which model we are going to use?

1:24:13

Maybe, let's say we can use GPT 5.2.

1:24:18

GPD 5.2.

1:24:19

Correct, everyone?

1:24:20

Now we will create the agent.

1:24:22

Step number nine is to create the agent.

1:24:26

Now, to create the agent, everyone,

1:24:28

we all know that we will use a function called as create agent.

1:24:31

And inside this create agent function, everyone,

1:24:33

we will have to pass all the things.

1:24:35

For example, let's say, we will, first of all,

1:24:37

we will pass the model,

1:24:38

which model our agent is going to use.

1:24:40

Our agent is going to use this model.

1:24:42

Then we are going to provide the list of tools.

1:24:44

Remember?

1:24:45

So here, everyone, before creating the system prompts,

1:24:48

we can create list of tools here.

1:24:50

In this list of tools, everyone,

1:24:52

we will add the name of all the tools.

1:24:54

First tool was search HR policy.

1:24:57

Second tool is get employee profile.

1:24:59

Third tool is get mandatory trainings.

1:25:02

Get training recommendations.

1:25:04

Everyone clear?

1:25:05

So these are the three tools that we have.

1:25:07

And these tools,

1:25:08

access, I will provide to the, we will provide to the agent, tools.

1:25:13

Is everyone clear?

1:25:15

List of tools.

1:25:18

We will provide the list of tools.

1:25:20

Is everyone clear?

1:25:23

Everyone clear, yes or no?

1:25:25

And then everyone we will provide the system prompt like this.

1:25:28

This is how we will create the, this is how our agent will be created.

1:25:32

Everyone clear?

1:25:33

And then everyone we will simply,

1:25:35

10th step is simply call the agent or invert.

1:25:38

the agent.

1:25:43

And how do we invoke the agent, everyone?

1:25:46

Earlier also we have written the same function, ask agent function.

1:25:49

Here, the query will come in.

1:25:51

User query will come in, which is of the type string.

1:25:55

And this function will just execute the agent.

1:25:58

And how everyone?

1:25:59

We will get the result by invoking the agent, agent dot invoke.

1:26:04

Okay.

1:26:04

Also everyone, you can do one more thing here that you can also provide some

1:26:08

description here. Now, you can ask one question here that, Deepak, this is not a tool.

1:26:13

This is a simple internal function that we are implementing, right?

1:26:16

Then why do we need description here? Correct?

1:26:21

Why do we need description here?

1:26:24

Yes or no, everyone? Yes. Any guesses?

1:26:27

Even if it is not a tool, everyone, every function, ideally, you can provide some description

1:26:32

so that, like in a company, when a lot of people are working, what use case you have

1:26:38

implemented in that function. If this function is very big, I will not have to go through

1:26:42

the entire implementation, right? If I just want to understand that what this function does,

1:26:46

I can just go through the description. Correct? So I can write a simple description here that

1:26:51

this function invoke the agent, invokes the agent for the user query and get the final response.

1:27:02

That's it. Always make a habit everyone. You provide proper description to all of every function.

1:27:08

Is that point clear to all of you? And here, everyone, when we invoke, what we have

1:27:13

to provide everyone? We have to provide, we have to provide the user quail. Okay? So if you remember

1:27:21

everyone, I think if I remember correctly, we have implemented that in the past also, that here

1:27:25

we actually provide two prompts. Okay? Here we actually provide two prompts. One, we provide system

1:27:33

prompt, that this is the system prompt, and then we provide the user prompt. Remember that?

1:27:38

Folks, yes or no? But don't you think everyone, the system prompt you have already

1:27:44

provided here. The system prompt you have already provided here. So we just need to provide the user

1:27:48

prompt. And if you go through some previous code, you will find this, that what is the role? We are

1:27:54

providing, first of all, the user prompt. Okay? And the content of the prompt is, the content of the prompt is

1:28:03

the user query which is coming in the input. We will provide like this.

1:28:08

Is this function, invocation, making sense to all of you, everyone?

1:28:13

Okay, actually, there is a small difference here. Sorry. It is not like this. You have to provide this

1:28:19

in messages. Okay? Uh, like this. You need to follow the syntax very carefully, everyone.

1:28:27

Like this.

1:28:32

It is quite complex to understand. But generally, uh, but generally, you will always,

1:28:38

you can always copy paste this from Google. Just change the values. Okay? Got it, Nesak?

1:28:47

How many if you're clear with this? We have done this, I think, n number of times. I have just

1:28:52

showed you one different way that you can provide system prompt because system prompt is constant. It is

1:28:57

not going to change with every query. So system prompt you can provide to the agent at one place. Or if you

1:29:01

want to provide here as well, you can do that. For example, here, you can give something like this also. You can

1:29:06

provide one more JSON value. You can provide role. Role is, let's say, system. And then you

1:29:12

can provide the content here. Okay? And content is system prom. You can do this also. Everyone clear?

1:29:19

You can do this also. How many if you're clear till this point of time, yes or no?

1:29:28

Okay. So get the final response, everyone. Response from the user, response from the agent.

1:29:36

you will get the result. Okay, we have already got the result. But does not that waste

1:29:40

context window? It is what it is right. It does not waste the context window as such. But

1:29:46

system prompt is something that is mandatory. For every query, don't you think your

1:29:51

LLM should follow these things? Okay? Your LLM should follow these things for every query.

1:29:57

So this is mandatory. Even if like it will consume tokens, nothing can be done.

1:30:06

Okay. Does not matter whether you provide here or you provide here. It is the same thing.

1:30:12

Okay. Here also this system prompt will always be given to LLM with every query. Here also it is the same

1:30:17

thing. Just different way of writing. Okay. System prompt will go with every query. Okay.

1:30:23

Wherever you provide it does not matter. Okay. Finally you get the result everyone and what

1:30:29

should we return from the result? We can let's say directly return the result.

1:30:36

In this result, everyone, a lot of things will be there. We will only be interested in the

1:30:42

content, the string content. Do you remember everyone that you can actually use parser also? You can

1:30:49

actually use parser also? Okay? For now, let's return the entire result as it is. And now everyone,

1:30:55

the last step is executing the, let's say, maybe executing, execute agent with

1:31:06

user queries. Okay. So folks, what we can do is maybe let's say we can have a user query.

1:31:13

Something like maybe, what could be the user query? Maybe, maybe, maybe. Let's say maybe if I ask

1:31:23

about leaves, how many leaves, how many leaves does a full time employee receives or gets?

1:31:33

How many leaves does a full-time employee gets? This is the query, everyone. Clear?

1:31:40

This is the query and we will get the final answer is equal to, we will ask the agent with this query

1:31:47

and we will finally print the answer. That's it. Is this point clear to all of you, everyone? Yes or no?

1:31:56

Is this point clear to all of you? This is how we can implement it. And finally, we can

1:32:00

clear the terminal and execute this agent.

1:32:03

Python 3, HR onboarding agent. Let's execute this. Okay, it will not work because

1:32:10

of API key. We forgot to give the API key. So let's go to Platform.Op.com, create an API key.

1:32:33

Copy the key, set it in terminal. Export, open AI, API, API, E is equal to this. Execute this. And now again, execute the book. Let's see. What result do you get?

1:33:03

Okay. Do you see that everyone, we are getting a lot of content? Okay? This is the AI message

1:33:10

inside the entire response. This is the human message. Correct, everyone? Can you see that? The highlighted

1:33:16

part? This is the human message. Do you remember in one of the classes we actually talked about

1:33:22

this AI message and human message? In one of the classes, we talked about the AI message and human

1:33:29

message. What do they do? Simple, nothing but everyone.

1:33:33

LLM creates, Lanktine creates these objects, that this is AI message object, which

1:33:38

is coming from AI, and this is human message object which user is giving, basically the query,

1:33:42

that is coming from the user. Okay? And then everyone, this is the content. Content is coming

1:33:47

out to be empty here, because the content is actually here. Tool message, inside tool message,

1:33:53

everyone. Can you see the content now, everyone? This, just look at the content. Just look at the content.

1:33:59

HR policy, do you see that? The name of the policy? Because we are asking about.

1:34:03

about leave. The name of the policy document, HR policy, 002, second policy.

1:34:09

What this policy is about? This is about the leave policy. And then everyone, you get the entire

1:34:13

content of the policy that full-time employee receives 24 paid leaves, etc, etc. This is

1:34:18

the answer that we are getting. Okay? Now, this is actually the content of the tool. Okay,

1:34:24

this is what tool is fetching. But should we return this content as it is to the user? Do we return the

1:34:30

entire policy document as it is to the user? No. So that's a

1:34:33

everyone, if you see, this is the tool message, which is coming from the tool, the output of

1:34:38

the tool. But then everyone, somewhere you will see that, AI message. This AI message, see the

1:34:43

content inside this AI message. This answer, we are going to return to the user that as per the

1:34:48

company leave policy, full-time employee receives 24 paid leaves per current calendar year.

1:34:55

Leave request must be submitted via HR portal, etc. Right? So this is what we are getting. And what

1:35:00

evidence we are getting everyone? What is the evidence of this information?

1:35:03

Evidence is this policy document. Can you see everyone? Because in the system prompt we have given this.

1:35:09

That please add evidences. Also actions taken. You will be able to see actions taken also.

1:35:15

What actions have been taken? What action have been taken? Searched HR policy document for full-time employees.

1:35:21

Can you see that? This was the action. Action means what? Action means what? Action means tool.

1:35:29

Correct? Which tool you have triggered?

1:35:31

Is everyone clear this? Yes or no?

1:35:38

Okay? I hope and I hope everyone is clear. Is there any escalation needed? If you meant a specific

1:35:44

leave type, then there is some escalation because all these things we are returning in the answer.

1:35:49

Answer, evidence, action and escalation. So guys, a lot of data is coming. Do you really want this much of data?

1:35:57

Do you really want this much of data? Not really, right? It is very complex to understand.

1:36:00

So what you can actually do is everyone from this complete result object, it is a bit

1:36:05

difficult to extract. So that's why we use string output parser.

1:36:10

Correct? We can pass, we can use the output parser. Or everyone, I actually did this before the

1:36:15

class as well. Let me show you how can you get it. Otherwise, it is not very straightforward to get

1:36:21

the final response, final content only. Yeah. So if you just want to get the message, final message,

1:36:28

or let's say the, yeah, final message.

1:36:30

let's say what you can do is from result the result that you are getting from the

1:36:35

result get the messages okay so in the results there is a messages section from the messages

1:36:42

section give me the last value getting the point if you see everyone this is the last value right

1:36:48

so there are a lot of messages this is the last value minus one means last index remember in python

1:36:55

this is the last message give me give me the last message and from the last message

1:37:00

What do I want everyone? I just want the content of that message. That's it. Okay? And instead of

1:37:06

this everyone, just return the final message. Are you guys getting this point? If you spend five minutes

1:37:13

on this, you will understand this right? If you see ultimately this is nothing but in result what you are

1:37:17

getting messages. Correct everyone? You are getting messages. So inside the messages, what is a message?

1:37:24

Messages is nothing but a list. See this square bracket. So first is human message. Then some other message.

1:37:30

But what do I want is I want the last message. This is the last message. Give me last value. And from the last value, everyone, I just want the content value. See. Can we see that? I just want the content value from the last message. It is very easy to understand if you think step by step. Where is it? Yeah. This is the last message. Inside this, there is a content value. This is how we can extract it. And now we can remove it. And now if you try to execute it again, you will just get the

1:38:00

actual answer from the LLM, not so many things inside the result object.

1:38:06

Yeah. See everyone. This is the final answer that we are getting from the LLM.

1:38:11

Is everyone clear? Yes or no?

1:38:16

Is everyone clear yes or no?

1:38:24

Okay. This is what we wanted to discuss everyone. The entire code I will push to GitHub as well as

1:38:30

you will find the complete code in the notes as well. Okay. And in the notes, you might find,

1:38:34

you may find one or two extra information that is up to you, that whether you want to implement that

1:38:39

or not. I would recommend you to implement few extra things as well on top of this. Okay.

1:38:45

Now, what kind of extensions you can do on this? Okay. Let me give you some idea. Okay.

1:38:51

In one of the classes, everyone, do you remember that we talked about human feedback?

1:39:00

We integrated human feedback. Remember that? In one of the Langchain classes, I think

1:39:07

two, three weeks back, we integrated human feedback. And for that human feedback, your application

1:39:12

will wait for the input. Remember that or not? Your application will wait for the human to provide

1:39:18

the input, whether for approval, for disapproval, any kind of thing, right? So what you can do everyone

1:39:23

is you can add human feedback, right? So what you can do is just refer.

1:39:30

Absolutely, correct. Turn 1 and turn 2, absolutely. So what you can do as a task is, everyone, try to integrate human feedback in the above HR assistant agent.

1:39:47

Clear, everyone? Try to integrate human feedback in the above HR assistant agent. Clear?

1:40:00

Then everyone, the last topic for today's class, which is evaluation harness.

1:40:06

Okay? This is also mentioned in the today's agenda.

1:40:11

Tell me, everyone, have we already ran evaluation test cases on one of our agent?

1:40:17

In one of the classes, complete class was there just to run evaluation. Let me, let me remind you.

1:40:23

Here you will find out evaluation.jason.

1:40:30

Yeah. See, can you write same kind of test cases in JSON file for HR onboarding assistant also?

1:40:37

What values do you need for evaluation? That? Some ID. Then what input you are providing some sample query?

1:40:46

Then what is the expected output? Expected output is which tool your agent should use ideally for this query?

1:40:53

What tools it should not use? What sources document it should refer to, right? That this query should be

1:41:00

answered from a, let's say, refund policy. This query should be answered from a leave

1:41:04

policy. You do that, and then you can add some keywords that this should contain this,

1:41:08

for example, let's say, for this leave. No only thing you can say that, okay, it should

1:41:11

100% for a full-time employee, it should contain the value 24? Correct? You can check this, right? Once you

1:41:18

do this, everyone, and should refuse, no. It should not refuse the query. If it is a valid query, it should not

1:41:22

refuse. If you're asking anything about random thing, it should refuse the query. Can you write these

1:41:27

similar kind of test cases for HR onboarding assistant as well?

1:41:32

folks, yes or no? Okay? So this is your kind of an assignment. Try to do this because we have already

1:41:42

done that. Okay? And how to use these evaluation agents? That also we have seen that, how to compare

1:41:48

these things one by one step by step. Is everyone clear?

1:41:57

Is everyone clear? Anyone has any doubt till this point of time?

1:42:27

through the uh sorry what you are saying uh you are asking that can i walk you through this

1:42:33

uh the evaluation part yeah okay let's go through this first of all everyone this is how you define

1:42:39

the evaluation cases in jason file okay and then everyone in which particular uh yeah there is the file

1:42:47

everyone where we used it and how did we use it let's see so everyone this uh what this is if you see

1:42:53

see uh all of these things are optional everyone the trace etc if you want to maintain a more information

1:42:57

if you want to maintain a lot more information about your agent for example how much time it is

1:43:02

taking what query is coming what response we are giving and how many times the queries are

1:43:06

coming and whatnot then you can use this contact current trace right for this we are using context

1:43:11

vars right so we use context where so every valuation gets its own trace for every valuation you will

1:43:16

note down the latency how much time this agent took how much time this agent took okay tools can write

1:43:23

to the currently uh so we use context where so that every

1:43:27

evaluation gets its own trace so that tools can write to the currently active trace without

1:43:33

receiving it explicitly as a function argument right what what happens is everyone inside every tool right

1:43:38

for example if you see this is one tool in this tool everyone after we we are executing the query

1:43:45

and also everyone if you see we are starting the timer again this is optional thing this is just very

1:43:50

advanced level of concept that we understood we are starting the timer then we are adding this input adding this data

1:43:57

to the we are recording this event right what this recording event does it is

1:44:01

adding to the traces right how much time it is taking etc etc right and if you see everyone

1:44:07

finally we are executing the query we are invoking uh getting the basically getting the documents and then

1:44:13

everyone we are appending this data to the tools and finally everyone once you do this in the runner code

1:44:18

we are actually running the test cases and then we are comparing okay whether it is a failure for

1:44:25

example let's say you execute the query right for example here if you see we are executing

1:44:29

the query what tools it used what documents did it retrieve and a final answer in the normalized

1:44:37

form just the content and then everyone if you see if the tool is not in the expected tools right if

1:44:45

let's say your agent did not call the expected tool then it will add to the failure correct that this

1:44:51

is failed this particular thing failed this test case failed

1:44:55

because of what reason the reason was that expected tool not use that your agent was

1:44:59

expected to use this particular tool but somehow it did not call this tool is everyone getting this

1:45:04

point is everyone getting this point similarly even you compare all the things if document is not

1:45:13

found if phrase is not found if basically the value is not found and finally everyone if everything looks

1:45:18

good for you compare everything if there is error and whatnot if the answer was refused but it was not

1:45:25

opposed to be refused and finally everyone you set the status is equal to pass if there is no failure

1:45:32

then you say that the test case has passed is everyone clear is everyone clear okay this is how you can

1:45:41

evaluate so you can if you want to go through this one this evaluation you can go through these two files

1:45:46

okay these two files okay so guys this class was just kind of a revision class do you see that in this class we have

1:45:54

mostly we have already learned the things we have tried to implement again correct or

1:46:00

not just a different example just a different real world use case the reason for this class everyone

1:46:05

is that this was just a revision class before the end of your current module in the current module everyone

1:46:10

we have specifically learned lang chain right which is one of the most widely used which is one

1:46:16

of the most important framework out there and in this class we have just revised all the concepts which we

1:46:22

have discussed in the past just before your module even

1:46:24

when is your module evaluation everyone when is your module evaluation fifth right so i think

1:46:31

you have decent amount of time everyone you have like 10 to 5th like 12 13 days please make sure that you

1:46:36

revise enough things go through all the things if you're attending all the classes then it will not be

1:46:41

difficult for you to to clear the evaluation okay that's it for this class everyone now i'm open

1:46:48

for any doubt you have in the past we have around like 15 20 20 minutes almost

1:46:54

Now, I am open for the doubts.

1:46:57

If you have any doubt, you can ask your doubts and otherwise feel free to drop off.

1:47:01

I will launch the feedback poll now, everyone.

1:47:04

Everyone clear with all the things about Langdain.

1:47:07

Tell me before I launch the feedback poll.

1:47:11

Everyone clear with all the things about Langdain.

1:47:14

Not only today's class I'm asking, right?

1:47:16

If you connect the dots from first session of this module, then second, then third, all of these were built on top of each other.

1:47:24

Please go through all the things.

1:47:26

You have 13 days of time that is more than sufficient, right?

1:47:29

I think that is good enough time to revise for your.

1:47:32

Chirag, in one of the classes, we have already done that.

1:47:35

You will have to go through the, just one time, go through the LMS,

1:47:40

and in the LMS you will find the lecture where we discussed it in detail.

1:47:44

For almost 1 hour, 30, 40 minutes, we have discussed that.

1:47:47

Okay?

1:47:49

Yeah.

1:47:51

Got confused with the agent memory execution.

1:47:53

For agent everyone,

1:47:54

If you see, memory, we have implemented already, right?

1:47:57

So we use chat message history, right?

1:47:59

Somewhere here.

1:48:00

So if you see, yeah, if you see here, this is the manual memory.

1:48:05

So we create a chat history.

1:48:06

So whenever we are getting the response from the agent,

1:48:09

so whatever is the human message and AI message, we are adding to the chat history.

1:48:13

Okay?

1:48:14

And then we are, then agent will keep on using this chat history every time.

1:48:18

If there is any previous context.

1:48:20

Okay.

1:48:21

Then in the next code, memory auto,

1:48:24

We discuss in-memory chat history.

1:48:27

In this, everyone, we are manually maintaining the chat history.

1:48:31

Can you see that?

1:48:32

We are maintaining the chat history manually.

1:48:34

But in auto, we are using it automated way of managing the history

1:48:39

via in-memory chat message history and runable with message history.

1:48:45

So these are the two things that we are using.

1:48:47

None of the objects or connections being created, how here are getting closed, does Python auto-closes it?

1:48:54

None of the objects or connections being created close.

1:48:58

Which connections?

1:48:59

Actually, in this case, we don't have any connection as such.

1:49:03

Okay?

1:49:03

If you see today's code, what connection do you think we have the agent?

1:49:07

We have the, we have the, we have open.

1:49:13

Not vector database?

1:49:14

Yes, yes, vector database.

1:49:15

Correct.

1:49:15

We have to use database.

1:49:17

Cauchally saying, have missed few classes.

1:49:19

We'll catch up and get back.

1:49:20

Today's class, Kenda, gave me an overall picture.

1:49:22

Actually, this class was kind of a revision class.

1:49:24

Okay, and you attended maybe the right class.

1:49:26

So if you go through the previous classes, then you will find that all these things we have

1:49:30

discussed one by one step by step.

1:49:32

Okay, question?

1:49:33

And if you still get any doubt, feel free to ask any doubt in the future classes.

1:49:38

Okay?

1:49:40

Your question is there.

1:49:42

Shantanu, which connection do you think is open?

1:49:45

Objects we don't have to close.

1:49:47

Connections, we may have to close.

1:49:48

But here, if you see, there is no connection as such, right?

1:49:50

You might be thinking that we are making this model call.

1:49:53

What model is not a connection?

1:49:54

You're just making an API call whenever it is required.

1:49:57

Apart from that, there is no connection.

1:49:58

Connection, we establish generally with databases.

1:50:01

You establish the connection, and once your task is done, then you close that connection.

1:50:06

You don't have to close it.

1:50:08

Okay?

1:50:09

Because as of now, if you see, these are, this is in memory.

1:50:12

Okay?

1:50:12

If you see, this is in memory.

1:50:14

In memory, you don't have to close it.

1:50:15

If your database is running on a separate machine, right?

1:50:19

Then you have to establish the connection.

1:50:21

Okay, then that, what do you say?

1:50:24

For example, let's say you are using SQL database.

1:50:26

How do you connect with SQL database via, let's say, SQL Alchemy?

1:50:29

So SQL Alchemy gives you a function, let's say, to close the connection.

1:50:33

I don't remember the exact function for ChromaDB as well.

1:50:36

If you search about the chroma DB, how to establish, how to close the connection, you will get the function.

1:50:41

But yes, for external databases, you can close the connection by calling a simple function from that library.

1:50:48

Is API key provided by Masai or should we buy?

1:50:51

You don't have to buy the API key or you don't have to pay the money asset.

1:50:54

you can use the free models. For example, for practice, you can use O-Lama.

1:50:58

In one of the classes, we have discussed O-Lama also, right?

1:51:01

That you can pull a model. You can download a small model on your laptop and you can use it.

1:51:05

You don't have to pay for that.

1:51:07

How these applications work in real time like production, like multiple people asking the question?

1:51:12

That is the scalability problem that companies solves, right?

1:51:16

So this application is deployed on a very powerful server.

1:51:19

And you can say that multiple, when multiple questions will come, multiple instances of

1:51:24

this application will run. Multiple threads will be there. And one thread will execute

1:51:29

one query at a time. Okay? Right? One thread will execute one query at a time. So if let's say,

1:51:36

for example, one million users are there. So there might be thousands of machines and each machine

1:51:40

might be handling thousands of queries. So how do we evaluate noise in our responses even when it has

1:51:48

the right info, but it dumps, this is, this comes under module, this comes under model evaluations. We will talk about that

1:51:54

in the last module. Okay? There are ways to handle the noises and to identify the wrong

1:52:02

output. We'll do that. Can we save chat history in the Croma database or any NoSQL database?

1:52:07

Cromar database ideally is not meant for saving the chat history, but you can do that definitely.

1:52:12

Or you can do that in any NoSQL database, right? It is just what is it? Like, it is just a simple

1:52:17

array for every conversation. So you just have to keep on maintaining the JSON objects. Okay? And you can

1:52:22

maintain in any database. Any NoSQL database, like maybe Cassandra will be good,

1:52:27

even Redis might be good, right? Or document database might be good. For like learning and creating

1:52:34

local tools, Olama is the best option, I think? Yes, absolutely correct. Without paying anything,

1:52:38

for free. Can you again explain K is equal to three means, for example, if you're, if you're

1:52:44

having thousands of documents, and if you're giving any query, now for that query, you have to perform

1:52:50

similarity search. And when you perform similarity search, you get some output. Now,

1:52:54

there might be, let's say, like, how will you find, like how many documents you want in the output? You give

1:52:58

that via K value. That, there are thousand documents. With the help of similarity search, you are

1:53:04

finding the similar kind of documents with the query. But how many similar documents do you want? I want

1:53:08

top three similar documents. Top most, three most similar documents with respect to the query.

1:53:15

Makes sense, Mukul? Three most similar documents. Right? And this K-Vasal.

1:53:20

you can keep on changing one, three, five, etc. Generally, three to five works best.

1:53:26

Okay? Okay. How would we write code in module three evaluation? Can you share some practice questions in the class?

1:53:37

You mean the current module evaluation, Akershi?

1:53:42

Practice questions, see, in every class, these are the questions only, right? All of these are

1:53:46

questions only. Now how, Masai will give you the question that, unfortunately, I am

1:53:50

may not be aware of because I have not got the kind of questions as of now, a sample paper.

1:53:55

I think maybe, Somia, are you there? So, I will talk to Somia offline and I will tell Somia to

1:54:05

discuss with the Maasai team and in your, I think you must be having the tutorial session, right,

1:54:09

this week also. Correct? So in the tutorial session, you can ask Somia that Somia will give you some

1:54:14

clarity about it. He will discuss with the team. Next module is code heavy. What do you want?

1:54:19

Code heavy, not code heavy. What do you guys prefer? Coding heavy or not very code heavy?

1:54:28

Both. Exactly. Very good answer. It should be both. It should not be like only coding or not

1:54:34

non-coding. If you see this module was code heavy. Next module is less code heavy. Next module we will

1:54:40

see also no coding agents, no coding tools. For example, N8. Okay? So if you see this module and the next

1:54:48

module, if you combine, it will give you a very fine balance of coding and non-coding.

1:54:52

Make sense, everyone? Is that point clear? Okay. So everyone clear with all the things?

1:55:02

So should I launch the feedback poll now? I hope everyone, all of you are getting a lot of information

1:55:06

from my side and I'm trying to share as much as possible that I could, right? And I hope all of you

1:55:11

are learning a lot. Okay. So I'm sharing the feedback poll. Please take the feedback poll.

1:55:16

Okay. Okay. Guys, I'm not.

1:55:18

the host, I'm not getting the option for feedback poll. Samaya, are you there?

1:55:48

Thank you.

1:56:18

So, ma'amia, are you there you there you there?

1:56:48

Thank you.

1:57:18

Hi, I got a reply from someone.

1:57:28

He's just coming.

1:57:31

I am the host as well, but why I am not able to see the feedback to see the feedback poll.

1:57:48

Thank you.

1:58:18

Folks, give me two minutes, sorry, but

1:58:48

cool now.

1:58:56

No, no, guys, not to you, I'm asking to Somia.

1:59:18

I think there is some issue from the while organizing the meeting while scheduling the meeting.

1:59:26

I'm a game developer. I'm trying to integrate these agents in the game. I will share with you as I got

1:59:30

some progress. Very good, very good ones. Keep it up. And sure, reach out to me if you need any help

1:59:37

or if you develop something good, then also reach out to me.

1:59:48

Thank you.

2:0:18

Guys, I think there is some issue in the feedback. This is not coming at all.

2:0:28

Okay, so maybe then we can drop off then. Okay, or maybe I have asked Formia to check with the program

2:0:36

team. There might be some issue from the scheduling side that while scheduling the meeting, they

2:0:40

might have forgot to add the feedback form.

2:0:48

Thank you.

2:1:18

Okay, everyone, then I think it will take some time. Maybe if you want to drop off, you can drop off.

2:1:48

I'm right now searching that and I'm opening that in front of me.

2:1:56

Yes.

2:2:02

The concept is mental health support.

2:2:04

Both with logic, the chat, not,

2:2:05

to assume,

2:2:06

a vision,

2:2:07

emotion,

2:2:08

action,

2:2:09

the agent,

2:2:11

the agent,

2:2:13

the agent,

2:2:14

the patient,

2:2:15

for the patient,

2:2:17

uh,

2:2:17

clinical attention.

2:2:18

Actually,

2:2:31

idea is very good, uh, sure, uh, what I would recommend is, I will also have to spend some time on

2:2:38

this that, uh, if I can help you, uh, like if I want to help you in that way, that what all the things

2:2:43

can be added, right?

2:2:44

We might have to brainstorm.

2:2:45

And, uh, I would recommend you.

2:2:46

I would recommend you go through some existing projects in the market right now,

2:2:50

and then try to get some value content from them, that what kind of things they have integrated.

2:2:55

Okay?

2:2:57

But we will have to, I think, brainstorm, right?

2:3:00

But idea is very good.

2:3:02

Yes, I think everyone the host has joined.

2:3:05

Let's see if we can get the feedback poll now.

2:3:09

Okay, but idea is very good, sure.

2:3:10

Please proceed with this.

2:3:12

Go through some existing projects which are there in the market.

2:3:15

Yes, now everyone.

2:3:16

we can see the feedback poll. Please take the feedback poll now, and then we can drop off the call.

2:3:46

can close the session for today.

2:3:48

Thanks, thank you.

2:3:49

Thank you, thank you, Priyanka.

2:3:50

Thank you for joining.

2:3:51

And thank you, everyone.

2:3:52

Have a good day.

2:3:53

And all the very best for your evaluation.

2:3:54

We have learned a lot.

2:3:56

All the concepts we have learned in detail in practical,

2:3:58

right?

2:3:59

Feel free to ask, any doubt, if you want to,

2:4:01

if you go through any revision, if you revise concepts,

2:4:03

and if you're getting it out, feel free to ask.

2:4:05

Okay.

2:4:07

Thank you. Thank you.

2:4:08

Thank you, everyone.

2:4:09

Bye-bye.