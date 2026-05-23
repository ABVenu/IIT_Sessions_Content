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

Hi everyone, very good evening.

6:24

Folks, am I audible to all of you?

6:29

Hi everyone, am I audible?

6:34

Okay, great, good evening everyone and welcome to the class.

6:38

So folks, in this particular session, we are going to start with Langchain.

6:42

I'm still not fully recovered.

6:45

Okay, so what I'll do is I'll keep my...

6:48

camera off today okay just because I'm not feeling well so I hope that is that

6:54

should be okay with all of you right I am feeling much better than Monday but still

7:02

not 100% recovered okay yeah so I'll keep my camera off just for today and today

7:08

we'll be starting with Langchain I think this is our very first class on

7:13

Langchain right in the past we have never discussed about Langchain is that correct

7:18

yeah correct so folks let's get started with the first video on lanchine exactly so now

7:33

in one of the classes we just had a quick overview of all the frameworks just i would say that

7:40

was a definition class where i just gave you the definition of x framework y framework z framework and so

7:46

So today, everyone, we are officially starting with one of the most widely used framework, which is Langchain.

7:58

Is, can everyone see my screen? Can everyone see my screen?

8:04

Okay, great. So let's get started with Langchain. Now tell me everyone what, what do you understand by the word Langchain?

8:13

What understanding do you have of the word Langchain?

8:16

Whatever you know about Langchain, please do let me know.

8:22

Language chain, okay?

8:27

It is used to make our LLM pipeline state full. Okay, sure. That is one of the feature, one of the most

8:37

important feature rather, but not the only one. It has other components as well, but that's correct.

8:43

What about other people?

8:46

includes memory very good what about other things anyone else i think we have

8:53

got around just three or four answers in the chat what about other people okay let me write

9:01

down the definition of Langchain framework from the official documentation of

9:06

langchain okay and then we will try to build our thought process on that and eventually

9:11

everyone we are going to talk about the core components of Langchain and then

9:16

then we will see a very basic code as well today.

9:19

Okay.

9:19

We will have more classes on Langchain and there we will see some more advanced use cases.

9:23

But today's focus is more going to be towards understanding the core components of

9:29

Langchain.

9:29

Okay.

9:30

So what is Langchain?

9:32

Now, as of now everyone, like including like a lot of people in the industry who are working in

9:38

the field of software development and who has even very less exposure to the AI development applications

9:44

or AI applications.

9:46

They just think that AI applications are all about what?

9:51

They just think that AI applications are just about talking to LLM, correct even?

9:56

That if you talk to LLM, get the response, this is an AI application, correct or not?

10:04

This is what most of the people actually think that AI application is nothing but just we have to talk to the LLM and get the response and give that response to the user.

10:14

That is what an AI application all about for most of the people.

10:19

But do you really think that in today's environment, in today's world, where AI is becoming so powerful

10:25

and the use cases are becoming so complex, so advanced, can we just say that AI applications are

10:31

just about calling LLM APIs, calling LLM and just getting the response? Absolutely not.

10:38

In real world applications, everyone, we will have to do a lot of stuff, even after calling,

10:44

even before calling LLM and even after calling LLM. LLM is going to be there.

10:49

LLM is anyways the brain of any AI application.

10:52

It is not going to be replaced.

10:54

But modern day AI applications are not only about calling LLM APIs.

11:00

Is that point clear to all of you?

11:01

Yes or no.

11:03

That modern day AI applications are not only about calling LLM APIs.

11:08

That's where everyone frameworks like, that's where frameworks like landchain

11:14

comes into the picture. Is that point clearly to all of you? That's where frameworks like

11:19

Lankchain comes into the picture. There are a lot of other frameworks as well, everyone. Lankchain is

11:24

one of the frameworks, right? So what is Lankchain, everyone? It is an open source. Lank chain, it is an open source.

11:44

which is used for building for building for building for building

11:55

LLM powered application if you see everyone LLM is going to be there

12:00

LLM powered applications

12:04

but how by connecting

12:14

models. Models means large language models by connecting models. Then everyone you will

12:21

have prompts also by connecting models, prompts, prompts, tools, memory, retrievers, generators and

12:34

what not. Multiple components. And you can say that and workflows in a structured way.

12:44

workflows in a structured way. Is this definition making sense to all of you?

12:55

That it is an open source framework which is used for building LLM powered applications

12:59

by connecting models. If you see these are the different components that we will talk about

13:04

later on models, prompts, tools, memories, retrievers, workflows together in a structured way.

13:12

Is that point to all of you?

13:17

So, Lankchain can be described as an open source framework. It gives you some pre-built

13:24

architecture that you can use and that you can integrate with the common use cases, right? So LLM,

13:31

so LLM, so Lanchine helps us, to build real world LLM applications which will have multiple things together,

13:40

which will have agents also which can do some tasks, which can take multiple prompts,

13:46

which can, for example, tools, everyone, it can send an email, it can book a ticket, it can do

13:53

other tasks as well, right? Then it can be stateful also. Because if you are building real world

13:59

applications and real world applications, if they do not have any memory, then definitely they are not

14:05

very usable. Makes sense, everyone? Correct? Retrievers also. Now everyone,

14:10

reverse means what? Rack kind of applications. Now, guys, only having an LLM or only having a model,

14:17

is that sufficient for a real world application?

14:21

Sorry. Can LLM answer every query of the world? For example, if you want to have, if you want to

14:29

build a chatbot, a customer support chatbot for your internal use case, right, which can ask,

14:36

which can answer customer queries based on your internal company.

14:40

policies. Definitely only LLM is not going to be helpful, right? Makes sense, everyone?

14:47

You need to have what? You need to have vector database. Right? You need to store documents

14:52

inside vector database. And everyone, when you store documents inside vector database, you will

14:58

have to probably first create chunks, divide documents into multiple parts. Then these chunks,

15:03

for these chunks, you create embeddings, right? And these embeddings, you store into vector

15:10

database. And then everyone, when any query comes in, you perform semantic search on

15:15

vector database, whatever query user is passing, and then based on that, you give the answer to the user.

15:22

So that is also that you can perform using Lankchain. Is that point clear to all of you?

15:31

Everyone clear?

15:34

Folks, yes or no? So guys, now, why Lankchain? The point is, why do we need Lankchain? The point is why do we need

15:40

Lanchine, why can't we do these things without even using Lankchain? Any thought process?

15:47

What do you think about this? That where does Lankchain exactly fit inside the agentic

15:54

AI applications? Why do we exactly need a Lank chain?

16:02

Think about this, that why do we need any framework in general? Right? For example, everyone, in

16:09

Python to build APIs. In Python, we have a framework called as Fast API.

16:15

Remember that? We discussed about Fast API framework. Why do we have Fast API framework?

16:21

even if we don't have a Fast API framework, can we still do the task of Fast API, what fast API is

16:29

providing you without even using Fast API? Can we do that? Can we do that? Yes, we can do that? Yes, we can do that?

16:35

Right. But don't you think everyone, the amount of effort that you'll have to start.

16:39

the amount of code that you'll have to write, the time it is going to take to do the same task

16:45

without Fast API is going to be much, much more than than using a framework.

16:52

And guys, a lot of times you have a lot of repetitive thing, right? For example, everyone,

16:56

you have to do some tasks today, right? And you have to build, let's say, APIs in Python today.

17:01

Do you think that you are the only one in the world who is going to write APIs in Python?

17:06

Do you think so? Not really, right? Not really. Not.

17:09

Not really, right? Probably millions of people are going to write APIs in Python every single day.

17:14

Now everyone, if everyone is spending a lot of time in just doing the repetitive stuff again and again,

17:20

which everyone has to do in the exact same way, only what changes? Business logic changes, correct?

17:25

everyone? Only business logic changes. So don't think even the world will develop at a very slow speed,

17:32

correct? The real development will happen at a very slow speed. And we will always be focused or we will

17:38

always be spending a lot of time on solving simpler problems. Guys, if we can outsource this

17:44

thing, if we can build frameworks so that it can take care of the general things. Don't you think

17:49

engineers and scientists can think of can solve actually the real problems? What do you think about it? The

17:57

complex problems are the one? Yes or no, everyone? So that's why everyone in every framework,

18:03

right? In every development environment, we have the concept of frameworks. And what framework does

18:08

everyone is framework actually gives you the functionalities which are going to be used by

18:14

millions of people, by a lot of people in the world, so that you don't have to implement it again and

18:19

again. It can take care of the basic stuff. And as an engineer, you can focus on the real development.

18:25

You can focus on the business logic, the actual logic that your application is going to serve to the

18:30

user. Is that point clear to all of you? Yes or no. Folks, clear? So this typically what happens,

18:37

typically what happens? Let's say, let's talk about that. Where does the language

18:41

comes into the picture? Now, let's say there is a user which is using your application. So user will

18:48

make a call to the UI, the application, mobile application, right? For example, let's say

18:54

you are checking, let's say, let's say you have built a, maybe a travel agent portal, where user can go,

19:01

and that is obviously AI assisted and agentic AI application with which users can use and book

19:06

their travel tickets on the AI platform. And this is a completely AI driven application.

19:12

So guys, can I say that you'll have the application or the UI or the website for that. So user will

19:16

interact via application or the UI. So user will give the input parameter. And when user will give

19:22

the input parameter, the request will go to the backend application. Now, folks, in the backhand

19:26

application, can I say that you will have to write the entire code for the agentic application,

19:32

for the agentic AIs to create agents, what every agent.

19:36

will perform to call the weather API, to call the Make My Trip API, to call the database,

19:41

to perform semantic search, right, to send an email, to check the itnery, etc, etc. Correct,

19:48

ever? Yes or no? So everything will come under the backend application. So guys, all of these things

19:54

you can do manually also, right? You can write an agent to talk to Make My Trip. You can write an agent

20:00

to talk to maybe let's say Expedia. You can write an agent to book flight tape. You can write an agent to book flight

20:05

tickets. You can write an agent to book hotel tickets and so on. You can do all this stuff. But don't

20:11

think even, it means it is going to take a lot of time. Correct or not? It is going to take a lot of time.

20:16

Also, when you do so many stuff, it is also prone to errors. You might end up making some error.

20:23

Correct? So what you can do everyone is, here comes a concept of frameworks like land chain.

20:30

Guys, as I'm saying frameworks like language. So landchain is not the only framework. Right.

20:35

So, guys, what land chain gives you? Langchain kind of gives you an orchestration layer, right?

20:42

So what Langchain gives you? Let me write down.

20:47

Langchain gives you an orchestration framework layer.

20:55

Orchestration layer.

21:00

Right? And this layer, everyone.

21:03

Sorry.

21:05

This orchestration layer even, it can actually talk to, it can give you the support of LLM.

21:18

It can give you the support of multiple type of databases.

21:23

It can give you the support of multiple type of tools.

21:25

It can be Make My Trip. It can be Expedia.

21:29

It can be Gmail. It can be Outlook. It can be whatever.

21:33

It can give you the support of embeddings.

21:35

Right? It can give you the support of embeddings. It can give you the support of multiple

21:42

type of APIs. And so. So, folks, now if you see, if you don't have the land chain in between,

21:49

don't think all of these things you will have to do on your own. Manually, you will have to write the

21:54

stuff for everything. Right? Manually, you'll have to do everything again and again, again and again,

22:00

right? But everyone, if you have land chain in between, langchain, in between, langchain takes a

22:05

lot of complexity on its head, right? Langchain takes care of a lot of responsibility

22:12

on its head and Langchain says that, okay, as a developer, you don't worry about these things

22:19

a lot. I will give you a set framework. I will give you a set framework, a set of a series of steps

22:26

that you can directly follow and build any kind of AI-driven applications very, very easy, right?

22:33

it also gives you ways to write prompts and whatnot.

22:38

Right? Let me give you a very simple example, everyone. For example, let's say if you are using

22:42

LLM. Now everyone, today, you might be using open AI. Correct or not? Right? Now everyone,

22:50

today you are using open AI. And do you think that you, if today you have using, you have started using

22:56

open AI, that forever you will keep on using open AI? Is that 100% true? Is that? Is that

23:03

a guarantee? Absolutely not. That is not at all a guarantee, right? Because everyone

23:09

tomorrow, Open AI might become more expensive. Open AI maybe might not release a lot of new features.

23:16

That's why you might move, you might want to move to Gemini. Okay? Because let's say Gemini has started

23:23

started developing more features than Open AI and Gemini is more cost efficient. Now guys tell me, if let's

23:31

say you don't have this framework internally and you are manually talking to the LLM,

23:37

which is open AI today. And tomorrow you want to migrate to Gemini. Don't you think even you'll

23:42

have, you might have to do a lot of code changes in this migration. You might have to make a lot

23:49

of code changes in this migration if you are moving from open AI to Gemini. And everyone,

23:56

this framework actually supports this feature of free.

24:01

migrating from one API or one LLM API to another LLM API, one database to another

24:08

database, one tool to another tool, one embedding model to another embedding model, it gives you

24:15

very easy ways. Because everyone, it is kind of, you can think of that it is acting like a manager

24:20

or it is acting like a, you can say that personal relationship manager, which is going to manage

24:27

the application relations with all of these external things.

24:31

Makes sense, everyone? It gives you the flow which you can directly use to talk to these

24:38

things externally very easily. Makes the flow modular. You can think of that. Absolutely correct.

24:45

Right. It gives you a modular way in which you can talk to these things very easily. And in future,

24:50

if you want to migrate from one LLM to another application to another LLM, it will be relatively very, very

24:56

simpler. Is that point clear to all of you? Absolutely. It kinds of gives you plug and play model.

25:01

After some time, everyone, when we will, when we will see the code, then it will make much more sense.

25:10

Okay?

25:12

How many of you are clear till this point of time?

25:15

So Langchain standardizes the model interaction so that as a developer, we can, we can, we can switch more easily from one provider to another provider.

25:27

It can be.

25:31

It can be LLM. It can be some kind of database. It can be some kind of tool.

25:37

Okay.

25:39

Okay. Now, everyone, if you see the word Lank chain, the most important term in this is the word chain.

25:50

Okay.

25:57

The most important word in this is chain. So let's talk about.

26:01

everyone what this chain is. But before we talk about chain, let's talk about different other things.

26:07

So how do we develop applications in Lank chain? So we can simply say that in Lank chain,

26:11

in Lank chain, in Lank chain, we build applications.

26:31

by connecting small reusable components together.

26:46

Just a second even, I think it is not writing properly by connecting small reusable components together.

26:57

So guys, don't you think, if you arrange these small components together.

27:01

They form the chain. Think about this.

27:08

Correct? For example, let's say, everyone, let's say you have a prompt.

27:12

Once you write the prompt, the prompt you will pass to LLM.

27:16

Right? Then whatever is the output of LLM, you will give to maybe, let's say, some agent.

27:22

Right. Agent will make a call to tool. Tool might make a call to database and so on.

27:28

Correct, right? This is the complete flow.

27:29

So do you see that, everyone?

27:31

build applications by connecting small reusable components. Don't you think this is one

27:36

component? This is one component. This is one component. This is one component. And so on. All of

27:41

these are small, small components which you are tying together to build the bigger application.

27:48

And now see this definition and tell me if this is making sense. We build applications by

27:54

connecting small reusable components. Small reusable components. The components which you can reuse.

28:01

Right. In the future. These components, everyone, are called as runables.

28:11

These components are called as.

28:27

Right. This is just a definition everyone. These are called as runnables. This is just a definition everyone. These are called as runnable.

28:31

Now, what are exact runnables, everyone? A runnable is a unit of work.

28:57

A unit of work. So, yes, there are other different types of work that can be invoked. So yes, there are other different types of

28:59

invoked also, invoke or stream or batch or transformed, right? We will talk about that.

29:04

But for now, I'm just using the word invoked. A runable is a unit of work that can be invoked

29:09

with other components.

29:15

Is the definition of runable also making sense to all of you? With other components.

29:26

This is the definition of runnable.

29:27

Right? Now, what are the different examples of runnable? Some examples of runnable?

29:37

Right. So one example is everyone? LLMs. Right. Another example could be retrievers.

29:48

Right? Retrievers. Some kind of tools. Right? Some kind of chain. Some kind of chain.

29:55

Right? Some kind of, there is a concept of output parser as well.

30:02

Now, what is output parcel? We'll talk about this, everyone. That once you get the output,

30:06

you will convert the output in a particular way, right? Maybe let's say JSON, right? That is called us

30:12

output parser. Also, everyone, when we are going to write the prompts, should we give the prompt

30:18

in a hard-coded way? Should we hard-cote the prompt?

30:23

Should we hard-code the prompt?

30:25

What is the meaning of hard coding the prompt? For example, let's say, if you're building a learning assistant for your students, right? Learning assistant for your students, that students can use that AI agent to learn or to ask their doubts. If, let's say, everyone, if I ask that, ask that agent or ask that application, that please explain me about Fast API. So, guys, if you give this hard-coded prompt,

30:55

Don't you think every time the question will change? Let's say today I want to ask for Fast API.

31:01

Someone else wants to ask for, let's say, LangChain. Someone else wants to explain about Java and so on.

31:07

Correct, everyone? So don't you think even, you'll have to keep on writing the prompt again and again.

31:11

Correct? So what do we do, everyone? We don't write the hard-coded prompt. Rather, we give the prompt in a template way.

31:19

Okay? This is called as prompt template. So Langchain gives you the ways,

31:25

which you can write prompt in a templated way. So you can keep the variables in curly brackets

31:31

and whenever the user query changes, you can change the value of this variable. Absolutely correct. Are you

31:39

guys getting this point? So we will talk about this. So Langchain gives you this way. Right? Chirac,

31:45

what is runable? Runable is nothing but these components, right? For example, as we saw that there is a

31:51

prompt, let's say, you give the prompt to the LLM. LLM gives the

31:55

you the response. That response you give to the agent. Agent, let's say, might make a call to

32:00

the tool or let's say database, right? From database, you do something else, right? So if you see,

32:05

all of these are small, small components. If you combine these components, this is building your entire

32:11

application. So each of these components are called as runnable. Make sense, Chirac? Each of this

32:18

component is called as runnable. Is that point clear to all of you?

32:25

Okay? In a very simple way, everyone, if I want to tell you the simplest logic of, what do you say,

32:34

the simplest application that you can build using Lankchain is without any agent, without any tool,

32:40

without any external API, without any database, without any embedding, what could be the simplest

32:46

application that you can build? Chain is all this chain, right? Step by step things are happening.

32:52

Right? Prompt you are giving to LLM. Don't you think.

32:55

this is a chain. Series happening in the series, right? One step after another and solve.

33:01

Right? The simplest application example that you can build using LLM is you have a prompt or you have

33:06

the user input, right? This user input, you write in the prompt template, correct? You prepare

33:15

a prompt template from that. And this prompt template, you send it to LLM. Whatever output you are getting

33:24

from the LLM, you convert it via output parser, and whatever output is returning,

33:31

you send it to the user as a response, final response. So guys, don't you think this is also

33:37

a very simple example? I think one of the simplest application that you can build using Lanchine.

33:43

If you see, it is nothing but a simple LLM application, where you are making a call to LLM

33:48

and finding the response, getting the response back. Correct or not?

33:54

Sorry, clear ever? So if you see, all of these are runnable.

34:01

Every component is one runnable.

34:05

Folks, everyone clear? Yes or no?

34:14

Okay. Okay. Now everyone, the next question comes as, what is chain?

34:21

What is chain?

34:24

So this chain is nothing but everyone. The sequence, the sequential steps, a chain is a sequence

34:33

of connected steps which happen in a particular series, which happens one after another, right?

34:40

So chain is nothing but a sequence of.

34:54

connected steps sequence of connected steps is that point clear to all of you correct

35:03

now everyone I will just write small small definition so that everyone is at the

35:09

you can say that at the same pace okay agent everyone knows because these

35:16

terms we will be using in Lank chain again and again agent is someone who can decide the next

35:24

path or the next step they can run parallelly also depends okay but if you

35:34

run parallelly if you see that there are multiple if you have multiple chains then

35:38

these multiple chains can run parallelly that is also possible we will see that in the

35:42

next to next class right next and next to next class we'll see that okay agent is

35:49

everyone agent is what agent is someone who can decide what to do next

35:54

agent can decide the next steps okay for example everyone if you ask a query to the

36:13

agent to the agent to the agentic AI application that uh let's say maybe what is the weather in

36:18

in bangalore right now give me the weather in ferranite because most of the

36:24

Indian weather websites they give the weather in the degree Celsius but you want the

36:28

weather in the Fahrenheit now what agent needs to do in this if you ask the agent to give you the

36:34

weather of Bangalore for today and in Fahrenheit not in degree Celsius what do you think

36:40

about it can I say that agent will first of all decide what to do and how agent will

36:50

think about it that what I need to do should I call the weather

36:54

API should I call database should I call maybe make my trip what should I call

37:00

how agent will decide this tell me everyone how agent will get the power of reasoning

37:12

power of thinking because you should have a brain to think about this right that if this is

37:18

the task that I've got how will I be able to answer this task

37:24

obviously LLM everywhere right so every agent also will have the support of LLM so

37:31

guys in the LLM also because LLMs are trained on humongous amount of data and they they will also

37:37

have the list of all the tools that you have given or that you have incorporated so it can

37:43

decide that based on the query which tool should I make a call to and will I have the

37:49

answer of this query or not if you ask the current weather of Bangalore obviously LLM will

37:53

have the will not have the answer for that so LLM knows it so LLM will be able to

37:58

decide that okay hey agent please make a call to weather API so when LLM will make a call

38:03

to weather API right this is how LLM will make a call it will get the temperature in let's

38:09

say degree Celsius then agent might make a call to the calculator and let's say whatever

38:14

calculation we need to do to convert degree Celsius into Fahrenheit it will do that and give

38:18

the final response to the user is that point clear to all of you

38:23

Yes, absolutely sure we use LankChain to implement chain of thought as well.

38:28

Absolutely correct.

38:31

Folks, is the idea clear to all of you?

38:39

Okay.

38:41

Now, guys, let's talk about core components of Lankchain.

38:53

Now tell me everyone, what do you think about what are the core components of

39:09

Lanchine?

39:12

Any guesses?

39:14

First one is everyone, models, not only LLM.

39:18

Folks, can I say that models can be of different categories?

39:22

Models.

39:23

Models can be large.

39:23

language models. Models can be, you can say that, the embedding models. Correct?

39:32

Then you have prompts.

39:36

Okay, then you have prompts. Then you have chains, everyone. We will see all of these one by one.

39:43

Then we will have chains also. We will have memory also.

39:53

We will have indexes also.

40:05

Everyone, clear? So these are typically six, what do you say?

40:11

Six core components that we have inside the Lank chain.

40:15

Now let's start with the first one, which is models.

40:20

I think everyone understand the concept of models.

40:22

So as Lankchain supports different types of models, right?

40:26

So Lankchain supports different type of models and you can use different type of models for different

40:32

different use cases. For example, you can use LLMs. Do we already know what are the use cases

40:38

of LLMs? When do we use LMs? Why do we use LLMs?

40:46

Right? So LLMs, LLMs we use for generation. When we want to use some kind of general.

40:52

A.I. Right? If you want to generate some text, some kind of, let's say, let me write it down.

41:01

Text to generation, some data generation, text, audio, video, etc., generation.

41:07

Also some kind of reasoning. Correct? Now, guys, there are other type of models as well,

41:13

which are called as chat models. Can someone tell me what do you mean by chat models?

41:22

What do we mean by chat models? I think we have not talked about them a lot, but

41:30

they are not very, very different from LLMs. So guys, chat models are built on top of LLMs only,

41:38

but they are not very good with reasoning. They cannot think a lot. What they can do is they can

41:42

just give you, they are just good for chatting. Okay, so they are built on top of LLMs and chat models are

41:50

mainly used for conversational use cases, right? They can take a list of messages, right,

41:57

as input and it can return the chat message or the response that you should return. Right. So if you see,

42:04

there is not a very big difference between chat models and LLMs, you can use LLMs as well for conversational

42:10

part, right? You can use chat models as well. But sometimes these are used differently. The names are

42:16

used differently. That's why I'm writing it here. But chat models are not anything.

42:20

much, much different than LLMs because the core idea is LLM only in chat model also.

42:30

Only text generation with limited context. That's correct, Ravi. Okay. Other type of models could be

42:36

text embedding models. I think this is something that we have already used, right? GPT small models,

42:43

GPT, large models, right? These are some examples which are used to create embeddings.

42:50

Shivam, they can be. Absolutely. Text, embedding models. Okay. One thing which is very,

43:00

very important, everyone, is that Lanchine abstracts the differences of different providers. Okay. What does that mean,

43:07

everyone? For example, if you're using any LLM, or if you're using any kind of chat model, if you're using any

43:12

embedding model, you don't have to talk to them one by one, one by one, as we discussed previously, right?

43:17

So it gives you an abstraction. Okay.

43:20

So what you can do is you can talk to Lanchine framework and Lankchain internally will take care of talking to these frameworks individually.

43:29

Right? You don't have to talk to them one by one on one on one on basis.

43:35

Sorry. Are you guys getting this point?

43:40

Folks, yes.

43:43

Okay. So this is the first core component of Lankchain.

43:47

Folks, when we will write the code, some part in today's class, some part in today's class, some part in,

43:50

in the next class, then you'll get a fair understanding of all of these four components,

43:54

or all of these core components.

43:56

Okay? For now, we are just understanding the definition of them. Okay. Then everyone, we have

44:01

prompts. Everyone knows about what is a prompt?

44:11

Okay, absolutely yes. So prompts are nothing but the instructions.

44:20

we send to, we send to the model to the model to the model to get the desired output.

44:50

very, very interestingly, or I would say very, very beautiful is that it gives you different

44:57

ways in which you can write the prompt. As I said everyone, that we should never, ever hard code the

45:04

prompt. It's, we should never do that. Because if you're hard coding the prompt, everyone, it will be

45:10

very, very difficult for you to scale the application. Correct, everyone? It will be very difficult

45:15

for you to scale up the application. So it gives you different type of templates. So the

45:20

The first type of template it provides you is the prompt template.

45:27

Prompt template.

45:30

So what prompt template does is, prompt template is, you can say that these are the kind of

45:37

blueprints that uses variables or placeholders to generate dynamic prompt with the help

45:45

of the input from the user. Makes us everyone?

45:49

By filling the variable values.

45:50

you can customize the prompt. You can rewrite the prompt. You can re- you can rewrite the prompt.

45:56

You can reuse the prompt. Correct? So what is prompt template and you want prompt template is blueprints, template blueprints, which uses

46:20

placeholders, these placeholders are what, everyone?

46:28

Placeholders or variables, right?

46:35

To generate dynamic input.

46:50

But Langchain gives you a specific way to use that.

46:57

Okay, everyone?

46:58

Then everyone, there is a small, there is a small difference of, like, a slightly different type of template, which is called us chat prompt template.

47:08

Okay?

47:09

In chat prompt template, everyone, you can pass a list of messages.

47:13

Okay?

47:13

For, and this is specifically used for chat models.

47:18

That for chat models.

47:20

For chat models,

47:24

Lanchine offers.

47:26

Lankchain offers.

47:45

Lankchain offers templates.

47:50

to form list of messages.

47:56

Is that point clear to all of you?

48:01

Everyone clear?

48:09

Then everyone, it also?

48:12

Under prompts only, it has prompt template.

48:14

It has something called as selectors also.

48:19

Selectors also.

48:20

example selectors.

48:24

Guys, can you relate this term example selectors with some kind of prompting techniques that we have

48:31

used in the past, that we have seen in the past?

48:35

Few short prompting, very good.

48:37

So, guys, don't you think to improve the overall LLM performance or the prompt performance,

48:41

we can include some example, maybe one or two or three, right?

48:46

So that we can say that, okay, if this is the example, this is the kind of response that we're expecting.

48:50

If this is the prompt, this is the kind of response that we are expecting.

48:54

Now, the third answer, give the third prompt, now LLM will generate the answer,

49:00

which is similar to these, these two kind of prompts.

49:04

Right.

49:05

So don't you think even this is called as few short prompting to improve the prompt performance.

49:10

So you can select, right?

49:13

That if you have used the same kind of API, same kind of prompts in the past, you can select that, okay.

49:18

This is the prompt and this is the kind of response that we will.

49:20

are liking that we are looking for makes sense everyone let me write it down that

49:27

to improve to improve the prompt performance to improve the prompt performance right

49:50

we can include some examples which is called us, which is called as few short prompting.

50:20

if this is making sense to all of you or not.

50:33

Okay, now, everyone, coming to the next core component, we have discussed two of them as of now.

50:41

We have discussed about models.

50:42

We have discussed about prompts.

50:43

Now let's discuss about chains.

50:50

Okay. Now, chains are nothing but everyone. These are the sequence of chain is a sequence

50:58

of connected steps. Sequence of connected steps. That process is a process is input. That process is

51:20

input through multiple components components sequence of sequence of connected steps that processes input through multiple components and using them we can combine multiple steps together in a single pipeline.

51:50

It is very, very similar to kind of a pipeline process, right?

51:54

That things will happen sequentially in the form of pipeline.

51:58

Everyone clear? In the form of pipeline.

52:03

Right. Now, guys, there are a certain type of chains we have in Langchain.

52:09

One is called as LM chain.

52:15

One is called as LLM chain.

52:17

Now, guys, this is one of the most common chain pattern.

52:20

which combines the prompt template, the model, and then generates the response.

52:26

Simple.

52:27

This is the type of, this is called as LLM chain.

52:30

Okay, that you have the prompt, pass it to the LLM.

52:33

Output parser is always optional.

52:36

Output parcel you will only use when you want to generate the output in a specific way.

52:41

Right?

52:41

If you want a general output, you don't even need parser.

52:45

You can directly return the response.

52:47

Right?

52:49

So LLLLR.

52:50

chain is the chaining technique which combines, combine prompt template, model template, model, and output parcel.

53:20

output parser is, anyways, optional.

53:29

Okay?

53:30

So you pass your variables, the prompt, for prompt you are using template, you replace the variable

53:36

values inside the prompt template, you pass the prompt to the model, you get the response back.

53:41

This is called as LLM chain, as simple as that.

53:43

So when we add an output format, only then the output parser is invoked, you will have to configure that.

53:49

it is it is not going to be automatic okay so you will have to tell that for example it says

53:54

something like this that if user is asking the output in a particular way then only you will

53:59

invoke output parcel okay obviously LLM can LLM can decide that LLM will have the power of

54:07

reasoning okay then everyone other type of chaining technique that we have out there is

54:14

something called a sequential and composite chains

54:19

So sequential and composite chains.

54:34

Now guys, if you see, if you have this LLM chain, don't you think this is the easiest and the most simplest, simplest use case, that you have the input, you generate the prompt, call the LLM, get the response back.

54:49

Simple. Correct, everyone? Correct or not? Yes. But everyone, sometimes the use case

54:57

will be complex, right? For more complex use case, everyone, you can develop a sequential series of steps,

55:04

a chain, right, where the output of one component or one runable will act like the input, will act like an

55:13

input to the next component. Correct, everyone? That is called as sequential.

55:19

Right? Composite means what everyone? Sequential means what? Sequential simply means that there is component A, calling component B, calling C, calling D, calling E. And let's say after that you have the final response. This is what a sequential chaining means. Okay? Composite everyone, it is even more complex that you have some kind of branching logic.

55:49

have some kind of branching logic. Okay? So you have, let's say, A, A is talking to B. B is calling C. After

55:57

C, everyone, let's say you have multiple steps. Okay. Depending on some condition, some logic, you may call

56:03

X, you may call Y, you may call Z. And after that, there is a different flow. After that also, it can,

56:09

there can be some branching logic. Are you guys getting this point? Because everyone, nowadays,

56:16

the applications can be very, very complex.

56:19

So you can have some parallel chaining also, parallel execution also, right?

56:32

For example, let me give you a very good example of parallel execution or parallel chaining.

56:39

Let's say, everyone, if you're uploading a video on some platform, let's say YouTube.

56:43

Once the video gets uploaded, don't you think multiple processing happens on the video?

56:48

For example, for that video, YouTube, first of all, might be checking the copyright issues.

56:55

YouTube might be checking the community guidelines.

56:57

YouTube might be generating the captions, right?

57:00

YouTube might be generating that video into multiple formats, 420p, 360p, 1080p,

57:06

in different qualities, 720p and so on.

57:09

So guys, can all of these things should be performed one after another?

57:13

checking copyright, checking community guidelines, generating captions,

57:18

converting video into different formats?

57:20

Do you really need to do them after one after, like in one after another way?

57:26

First, we should do this, then this, then this, then this, then this?

57:29

Not really.

57:30

Don't you think everyone, all of these steps are independent of each other?

57:36

Yes or not ever?

57:38

These are independent steps.

57:40

And if these steps are independent, can't you do them in parallel?

57:44

This step, this step, this step.

57:46

You can have multiple agents.

57:48

which will do these things in parallel, right?

57:51

For that, you can use parallel kind of chaining concept.

57:56

Everyone, clear?

58:03

Folks, clear or not?

58:04

We will do all this stuff, don't worry.

58:06

So, folks, we have discussed three type of three core components as of now, model, prompt, and chains.

58:12

Okay?

58:12

So now let's take a break here, exact, in between.

58:15

And these three, we will discuss after break.

58:18

Okay, after break.

58:21

So, I will give you the link of the notes.

58:28

We will take a break of maybe five minutes I will give you to revise the notes and maybe 10 minutes

58:35

of break.

58:36

Okay, so we will have around 13 to 15 minutes of break.

58:39

These are the nodes.

58:40

So it's currently 9-2, 93.

58:41

Let's meet around 9-17.

58:44

Okay?

58:45

So please go through the nodes and then we will continue.

58:48

See you after the break.

59:18

Thank you.

59:48

Thank you.

1:0:18

Thank you.

1:0:48

Thank you.

1:1:18

Thank you.

1:1:48

Thank you.

1:2:18

Thank you.

1:2:48

Thank you.

1:3:18

Thank you.

1:3:48

Thank you.

1:4:18

Thank you.

1:4:48

Thank you.

1:5:18

Thank you.

1:5:48

Thank you.

1:6:18

Thank you

1:6:48

Thank you

1:7:18

Thank you

1:7:48

Thank you

1:8:18

Thank you

1:8:48

Thank you

1:9:18

Thank you

1:16:48

Hi,

1:16:55

Hi, everyone, I am I am I am I am I am I am I am I am audible,

1:17:00

Hi, everyone, I'm audible.

1:17:02

Hi, everyone, I'm audible.

1:17:04

Okay, so now everyone let's talk about the fourth component, which is memory.

1:17:09

I think memory is memory is something that we have already talked about the fourth component, which is memory.

1:17:18

short-term memory, long-term memory, conversational memory and whatnot.

1:17:21

So memory in lanchain, like memory in any AI application, it helps to maintain the context between

1:17:29

the interactions.

1:17:30

It is very, very crucial for any kind of AI applications.

1:17:34

For example, if you are building an AI application and after every sentence, if you, if your application

1:17:40

or if your agent forgets the context, then in the entire, like in the complete prompt, like in

1:17:48

every prompt, you'll have to give the complete context again and again.

1:17:51

And if you give the complete context again and again, obviously what will happen, the context

1:17:55

window will expire soon, you will consume more number of tokens, the responses will be slow and what not.

1:18:01

User experience will not be very good. Correct, everyone?

1:18:06

Folks, yes or no?

1:18:10

Correct. So memory helps to maintain context in the conversations.

1:18:18

helps to maintain the context within within interactions, within conversations, within conversations, you can say that.

1:18:38

within conversations okay so integrating memory with your chains or agents

1:18:49

it enables to generate context aware and coherent responses right let me write it down and then

1:18:57

we'll try to understand this right that integrating memory I'm just reading this statement

1:19:02

from the official documentation integrating

1:19:08

memory, integrating memory with chains or, with chains or agents,

1:19:36

to generate context aware, context aware, responsive responsive responsive responsive

1:20:01

over multiple turns.

1:20:10

Folks, please go through this definition.

1:20:13

Slightly more technical, I would say, but it is like one of the best definition that fits for memory.

1:20:21

That fits in the concept of memory.

1:20:23

Please go through this and let me know if it is making sense to all of you.

1:20:31

Making sense everyone?

1:20:35

Integrating memory within agents or chains enables them to generate context aware.

1:20:40

It is very important.

1:20:41

This term we will be coming across multiple times context aware.

1:20:45

Now let me give you a very simple example for that.

1:20:47

Folks, if you ask an LLM, let's say if you give, if you ask the agent, the travel agent to generate an itinary with that agent does not have the context, that that agent does not have the concept of memory.

1:21:00

it will give you a very, very general itenary for your prompt.

1:21:05

But everyone, if that agent you have already used and that agent has a lot of context about you as a user,

1:21:12

as a traveler, and then if you ask the it italy, don't you think it will include all the things

1:21:17

which you like and it will generate the itinary basis on your preferences?

1:21:22

So that is called as context aware, right?

1:21:25

When LLM generates the answer, basis on the context about the user it already has,

1:21:30

it is called as context-aware response.

1:21:34

Makes sense, everyone?

1:21:36

And coherent. Coherent is, which is matching with the preferences, right, over multiple turns.

1:21:42

It means that everyone, even if you ask multiple, even if you take multiple turns, right, it will give you context-aware response.

1:21:50

It will not forget the context across multiple turns.

1:21:54

Everyone, clear?

1:21:56

So, folks, there are different types of memory, conversational, short-term, long-term, etc.

1:22:00

right that we have already talked about in the past cool now let's move to the fifth

1:22:07

core component which is indexes what do you think about indexes everyone this is the term that

1:22:13

we have not used a lot of times but yet it is quite important indexes this is the term that we have

1:22:25

not used very very frequent if you can tell me

1:22:30

what indexes are, where they might be relevant.

1:22:36

Any guesses?

1:22:39

So like index of the components of the chain, uh, not exactly.

1:22:46

Database, very good.

1:22:48

When do we use databases?

1:23:00

are used, indexes are used to organize, organize and retrieve document data,

1:23:30

used to organize and retrieve document data which is mostly essential for right i will explain the

1:23:40

definition as well indexes are used to organize and retrieve document data which is essential for

1:24:00

which is essential for rag-based applications is that point clear to all of you

1:24:09

now everyone let's say what do we mean by index six exactly now everyone in rack-based applications

1:24:16

what do we have can i say that we connect our l-lm right or we connect our AI-based application

1:24:22

with a vector database correct everyone we connect our appellation we connect our appellation we connect our

1:24:30

with vector database and in this vector database everyone we store a lot of documents we store a lot of documents

1:24:40

obviously after embeddings after chunking etc etc but still everyone if you have thousands of documents

1:24:47

don't you think searching across thousands of documents will be very difficult it will take a lot of time

1:24:53

the process will be very slow correct and there comes the concept of indexes

1:25:00

now with the help of indexes everyone what you can maintain is you can maintain some

1:25:04

extra information that what document is present at what memory address in the vector database

1:25:09

so that instead of iterating through instead of going through the entire vector database to

1:25:14

search for a document you can go to a particular place where that document is placed and you can

1:25:21

find out that document very very easily right for example everyone in books it is meta data that's

1:25:26

correct in any book have you seen that at the back

1:25:30

of the book there is index or at the front of the books also there is an index right at the back

1:25:36

of the book there is a different type of index at the front of the book there is a different type of

1:25:39

index in index front table in the front of the book at the starting of the book what is what does

1:25:45

it contain that this page number starts with page and starts with page number seven this topic starts at

1:25:53

page number 20 this chapter starts at page number 40 correct now if you are looking to read a particular

1:26:00

topic or a particular chapter you don't have to iterate through the complete book

1:26:05

you can just go to the index look at the page number and directly go to that page number

1:26:11

don't you think everyone the index table makes your chapter search very fast

1:26:15

make your makes your search very fast correct even this is what indexes also means in

1:26:23

databases everyone clear

1:26:30

okay so guys langchain gives you a lot of support for documents because one of the major

1:26:36

advantage or one of the major use case of langchain is to build rag based applications right so

1:26:43

when we talk about for example it's a rag based applications there are there is a concept of vector

1:26:48

databases you need to load the documents you need to split the documents you need to store the documents

1:26:53

you need to find embeddings all of these things are efficiently supported by langchain

1:27:00

framework is that point clear to all of you for example langchain gives you

1:27:03

functionality to load documents from different sources you can load pdf images c sves uh right

1:27:11

comma separated values excel files you can also split them into chunks and then store them into

1:27:17

the vector database makes us everyone and inside the vector database langchain will also help you

1:27:23

to create indexes on top of that so that the search will be faster

1:27:30

is everyone clear with this yes or no okay very good then everyone coming to the

1:27:38

last core component which is agents i think agent is something that we already know okay

1:27:47

just to complete the loop let's write the a small definition about agents agents in langchera

1:27:54

dynamic decision-making components that can select actions or tools based on the

1:28:00

user input right so agents

1:28:06

agents are dynamic

1:28:15

dynamic decision making but how will it manage we think we

1:28:30

don't need to worry about it uh can you tell me the context about it what uh in which

1:28:35

context you are referring this how it will manage the apia of different vector database okay

1:28:43

you mean that whether we are using chroma db or we are using x y z db etc yes that will

1:28:49

be taken care by langchain okay so langchain will take care of that if you're not using

1:28:55

langchain then you'll have to worry about it how will you create the indexes right

1:29:00

and what kind of indexes will be better right otherwise uh like if you're using

1:29:04

langchain langchain will orchestrate all these things all of you understand the meaning of

1:29:09

orchestration orchestration this word i think i have told in the past right or you might be knowing

1:29:17

already very popular term you might have heard the term orchestra orchestra right so there is a group

1:29:24

of people who performs this dance right

1:29:30

and there is a person in between which is managing all these people so every person in the group

1:29:36

is playing a different type of musical instrument right now this person in between in the middle

1:29:43

if you see look at this person right this guy this guy is managing all of these people right if this person

1:29:50

the middle guy is not there then it will be very difficult to manage these many people

1:29:55

at the same time playing different instruments correct

1:30:00

so this central guy the central person is acting like a orchestrator orchestrator right and it is

1:30:07

managing all of these components so beautifully so that the entire output is soothing the entire output is

1:30:15

the entire output is the desired output makes us similarly lanchine also acts like an orchestrator right in

1:30:21

langchain application also in a i application also you will have a lot of components database

1:30:26

vector database embedding tools APIs database and whatnot right lot of things will be

1:30:32

there APIs and whatnot now if you are going to manage all of them individually it will be very

1:30:37

difficult for you so you hire an orchestrator just like this central person that central

1:30:44

person will do the duty and it will manage it will talk to all of them individually so you

1:30:49

don't have to talk to the individual components this is what exactly Langchain also does

1:30:56

make sense everyone okay okay okay so agents are dynamic

1:31:03

dynamic decision-making components decision-making components that can select actions

1:31:26

or tools based on the user input based on the user input based on the user input

1:31:51

right.

1:32:21

Yes everyone. So everyone clear with all the six components still now.

1:32:51

great so now everyone let's move to the next component now uh move to the next part now that

1:32:57

the next part is the installation and setup okay so let's try to install lanchain okay and let's try to

1:33:06

use it for the very very first time in a very very simple example okay let me just show you an example

1:33:15

of first everyone before we actually go to the code and installation let me first just show you uh

1:33:21

the example of a prompt template okay so that we can directly use it after this

1:33:51

structure with the variables okay for example everyone let's say if you have this

1:34:02

prompt right if you like a prompt uh if you write a prompt like this that let's say explain

1:34:09

SQL uh maybe let's say SQL query or SQL joins or xq let's say let's take this

1:34:22

example let's say explain SQL indexes in SQL databases also everyone there is a concept of index

1:34:27

in every database index is there is there the concept is there the concept is the concept is the concept

1:34:31

remains same indexes are something which makes the query faster which makes the database search faster right so

1:34:39

explain SQL indexes to beginner students in simple way to beginner students to beginner students in simple way in simple words so folks if you have this prompt now is this a prompt template is this a prompt template answer is no this is a hard-coded prompter how can you convert this into a template is if you convert this

1:35:09

everyone now why this is not a template because tomorrow if you have to search if you have to uh if you want to explain

1:35:16

something else to some different type of students beginner intermediate advance and in some different tone simple words difficult words

1:35:24

uh maybe let's say heavy words and whatnot right so you will have to write the prompt again and again so instead of this

1:35:30

everyone what you can exactly do is you can write a template and you can put all of these things into a variable right that

1:35:39

explain the topic you can put inside a bracket to what kind of students you can put inside

1:35:53

the audience that what kind of audience you are catering audience students in type of words in what type of words.

1:36:08

let's say what style of words what type of words so if you see everyone these

1:36:20

three things you have moved to variable is that point clear to all of you all of you and now everyone

1:36:29

you can change this topic let's a topic is sequel indexes or java or python or fast API audiences let's

1:36:37

let's say intermediate students or beginner or advanced style may you can add simple and

1:36:42

practical difficult words and whatnot right so it gives you reusability so template gives you

1:36:49

use you useability correct or not everyone so it gives you reuseability folks clear

1:37:07

okay so now everyone let's move to the implementation part just give me a second let me

1:37:15

start visual studio

1:37:37

let me share my visual studio screen is the visual studio screen uh visible to all of you

1:37:52

of you okay let's create a new folder lanchine apps okay and open this of now if you

1:38:04

So as of now if you see this complete folder is currently empty.

1:38:09

Okay and what we're going to do we will open the terminal.

1:38:34

what was the command v env let me just sorry sorry

1:39:04

source VENV bin activate.

1:39:26

Yeah, and now everyone here what we will do we will install first of all all all the required

1:39:33

for now we just need lanchine so what we're going to do pip3 install langchain okay so let

1:39:44

let it download everyone let it get installed done so the lanchain has been installed so first of all

1:39:51

everyone what we are going to do is what we are going to do is we will write a very simple application

1:40:00

let's call it as app one dot p1

1:40:03

Okay, in this app 1.py, what we are going to do is we will simply call LLM using

1:40:09

Langchain. Sounds good. So for that everyone, first of all, Langchain gives you a way to talk to,

1:40:17

let's say, open AI. So from Langchain, you will have to do Langchain underscore open AI, import.

1:40:30

Let's say we are using open AI.

1:40:32

the name of that application is chat open AI okay so you can use the chat API from open AI

1:40:39

and you can invoke it so first you will create the LLM object or let's say the client object

1:40:44

client is equal to chat open AI and how can you do that you just have to pass the model

1:40:52

model is equal to let's say you are using GPT-5.2 okay you will use this claim but if you want to

1:41:01

use this everyone first before this what you'll have to do is before even you use open a

1:41:07

what you will have to do you'll have to set up the API key correct so let me set up the API

1:41:16

key let me go to platform open AI let me go to API keys create a new API key this is

1:41:28

let's say 20th of May

1:41:31

copy and export it so export open a i underscore API underscore key is equal to this done

1:41:43

and now we will be able to use open AI API

1:41:46

sounds good everyone everyone clear till this point of time okay and now everyone we will

1:41:56

invoke this API via client so client dot invo

1:42:01

there is a method called invoke and here you can pass a prompt prompt is let's say

1:42:05

maybe explain the same example that we took explain SQL indexes to the beginner

1:42:14

students in simple words okay and we will get sir we will get the response let's

1:42:23

store this in the response response response is equal to client dot invoke this

1:42:31

do we have we'll talk about that Rajat there are different ways we'll talk

1:42:35

about it okay is this way clear to all of you very simple for now okay and finally everyone we

1:42:48

will print the response dot content okay let's try to print the response only let's

1:42:56

see what all the values are coming is this around four five lines of code making sense

1:43:01

to all of you or not okay so uh let's try to run this code everyone go to the terminal

1:43:20

and run this python three ab one dot bi

1:43:31

okay so this is not installed kha sorry sorry everyone so i think we just

1:43:37

installed open a i right uh sorry we just installed lanchine pip install langchain this we installed

1:43:45

yes and we need to install lankchain open a as well lankchain hyphen open ai so earlier we just

1:43:59

install langchain not langchain open ai okay and now this is done and let's try to make a call

1:44:05

now and now if you say everyone the call is going to open a i let's wait for some time sorry

1:44:23

yeah if you see everyone now we are getting the response right and we are getting a pretty decent response

1:44:29

you can pass multiple values here for example if you want to pass the context the context

1:44:33

window uh the limit what do you say the instructions the role etc right for now we are just passing

1:44:40

the model okay and if you see inside this we have a content paid content uh content content part right

1:44:48

content is equal to a SQL index is this this and after that content everyone we have other things

1:44:54

also that how many tokens are there in the prompt how many total tokens we have

1:44:59

have consumed right total tokens 551 right audio token zero model which we have

1:45:06

used gpt 5.2 right model provider open ai and whatnot so guys most of these things are not of any use for

1:45:13

us for now so we will just print the content response not content and now if you just execute it we will

1:45:20

just get the prompt we will just get the content in the response so folks this is the idea of

1:45:27

invoking open eye now as of now you might be thinking that depok why do we need an

1:45:32

a new framework all together for this right we were able to do the same thing without lankchain also

1:45:39

with the same complexity right in the same lines in the same number of lines of code correct or not everyone

1:45:51

folks yes or no absolutely yes we were able to do so but now everyone if you see this use case is one of the

1:45:57

simplest use cases that you have seen now everyone i will show you a very good use case

1:46:02

that if you see in this use case as of now we are hard coding the prompt but let's try to make make

1:46:10

use of prompt template yes this yes exactly here you might not be able to see the value or the importance

1:46:17

of language because there is no state involved as of now there is no memory involved there is no agent

1:46:22

involved there is no database there is no embedding there is no uh document loading document chunking

1:46:27

nothing that's why it is very easy now everyone let me try to involve prompt template

1:46:33

in this okay so let's go to the application everyone and let's see let's try to do the same thing

1:46:39

if you see we are getting the content okay so let me copy pay let me comment it out and let me put

1:46:47

let's try using prompt template in the above API column okay for this everyone we will have to

1:46:57

use few things which are already there we will use the same component from

1:47:07

lank chain open ai import chat open ai from langchain open eye import chat open i from langchain open eye import

1:47:15

chat open i and from langchain not open ai

1:47:21

from langchain dot core core core dot core dot dot i think this also we need to install

1:47:51

okay it is already there dot prompts import prompt template okay so we will now use

1:48:03

prompt template and then you will see that okay this is pretty good to use right then everyone

1:48:08

we will create the client object as it is without any change langchain open ai okay using the same gpt 5.2

1:48:19

model then everyone we will write the prompt

1:48:25

prompt underscore template is equal to prompt template dot

1:48:35

there is a function called as promprom why this is not getting auto-completed it is not installed properly

1:48:46

land chain core let's try to do one thing before even we do this let's try to run

1:48:56

yeah it is not properly installed what is the name of the module

1:49:16

folks let me just check one thing that do i need to install something else also

1:49:46

PIP 3 install Lanchine Core that we already installed, right, PIP3.

1:50:16

install langchain hyphen core it is already there okay okay let's try to use it

1:50:28

it should prompt template so guys here we will write the prompt uh the prompt template

1:50:34

from template and here everyone what we will do is we will write a prompt here in this way

1:50:38

okay so what we're going to do is we will say that explain explain explain what we're going to do is

1:50:46

explain let's say some topic explain some topic to some audience some kind of audience

1:50:55

okay explain this topic to some kind of audience okay explain this topic to some kind of audience and i

1:51:00

will give some requirements here what requirements we will give

1:51:05

requirements are maybe or let's make it very easy explain sequel indexes to beginner students in

1:51:16

let's say uh what was it style of words okay is this prompt template making

1:51:24

sense to all of you right very simple and then everyone what we're gonna do is

1:51:46

the prompt in the same way okay this is very simple that i understand but let's try to

1:51:51

write requirements only explain topic uh to these students with these requirements let's write

1:51:58

requirements also okay requirements maybe we will say that the first requirement is give the answer

1:52:04

in a particular tone use this tone simple tone difficult tone etc etc right use this tone right then everyone

1:52:15

give one real life analogy to explain the concept right and then everyone

1:52:25

there is one more line that we will add uh let's say word count that keep the explanation or keep

1:52:30

the response within let's say hundred words or within uh let's say boundary or limit

1:52:39

within within these many words is this prompt also making sense all of you

1:52:43

sorry right and now everyone using this prompt template we will build the final

1:52:51

prompt that prompt is equal to prompt template dot prompt template dot format

1:53:00

write something here in this format everyone we will give the topic topic is equal to what topic will be let's

1:53:10

say SQL indexes sequel indexes then audience will be what let's say beginner

1:53:19

beginners then everyone the next is tone so all of these are acting like variables right

1:53:27

tone is let's say maybe simple tone right and let's say limit is 100 words or limit is let's say 200 words

1:53:35

are you guys getting this point so all of these variables that you have defined in the all of the

1:53:40

place holders that you have defined in the curly brackets they are acting like variables now

1:53:44

and inside this prompt template dot format function you can provide the value of each of these

1:53:51

variables one by one are you guys getting this point are you folks getting this point and finally everyone

1:53:58

what we're going to do is response is equal to client dot invoke right and now we will give this

1:54:05

prompt folks have a look at it and tell me if everyone is clear there is

1:54:10

simple straightforward right okay and finally we will print a response dot

1:54:19

content okay let's try to run this okay module not found folks there is some problem

1:54:31

here lang chain core okay if you see there is a spelling mistake this is prompts clear and

1:54:40

now it is running fine let's wait for few seconds for the response now everyone if

1:54:51

you see we are getting the response back are you guys getting this point this code is also working

1:54:55

absolutely fine with langchain everyone clear now everyone see how easy it is here everyone we are

1:55:03

hard coding these values but do anything in reality these values we will take from the user right so let's say if you

1:55:09

want to change the value you are taking the value from the user langchain components to

1:55:16

beginner students in simple tone in let's say 1,000 words okay you can just change the value and the entire

1:55:26

code will work as it is without any difference folks how many of you are 100% clear with the code

1:55:38

so let me just write couple of comments here in the code so that you can refer it easily

1:55:50

if you see everyone we are getting the response back and this response is pretty detailed because we have

1:55:55

increased the limit of thousand words right so langchain core components okay tools models

1:56:03

template it's prompt chains etc this is what we have already discussed so everyone this

1:56:08

is what we are creating the prompt template from creates a reusable prompt template right

1:56:18

here we are it will this function format function will replace variables with actual values

1:56:26

provided by the user at the runtime at runtime at runtime okay okay

1:56:38

invokes lLM API to get the response okay fine okay now everyone there is one

1:56:52

concept as well that i would just like to highlight today in detail anyways we are going to discuss

1:56:56

in the future in the future classes so you are saying that we can set these variables from the

1:57:00

user input like maybe semantic search and then pass into a prompt template so whether or not the user uses a hard

1:57:06

code template see user user gives the prompt internally you are actually creating

1:57:13

the prompt that you will pass to the llm right so you can say that there is a middle agent or a middle way

1:57:20

or let's say there is a middle person who will take the user input from the user input the middle person

1:57:25

might extract the useful information give it to the template then generate the final prompt then pass it to the

1:57:36

make sense yeah so just one more thing everyone for today's class uh let's talk

1:57:47

about something called as okay i think this a pretty uh slightly bigger topic anyways this we are

1:57:59

going to discuss in the next class as well i'm i will just announce this right that what is l c ean so guys

1:58:06

if lcel stands for what anyone knows about it lcel stands for langchain expression language it stands for

1:58:20

langchain expression language can i ask details of how we will mine the data pass to the template using

1:58:30

regular expressions i think we have done that in uh uh in the rack class

1:58:36

right so yeah depends depends on uh for example it's a lot of times what happens is right

1:58:41

that uh you expect the user input not in the form of template not in the form of prompt

1:58:46

you expect the input from the user in the form of fields

1:58:51

right that give the value to this field give the name give the age give the gender right

1:58:57

give that source give the destination right so user can just fill in the blanks and

1:59:03

those variables you will pass inside the prompt template

1:59:06

to generate the final one makes sense uh sorry okay depends from uh application to

1:59:16

application okay so guys langchain expression language what it does is it simply allows you to

1:59:23

connect your components with the help of uh components like a pipeline it helps you to connect components

1:59:33

with like a pipeline okay so what l c e

1:59:36

us LCEL helps us or allows us allows us to connect components like a pipeline.

1:59:53

What does that mean everyone? Anyways, I'm going to show you this in the next class in very, very

1:59:58

detail, right? For example, everyone, you have a prompt. Okay, the prompt you need to pass to the

2:0:06

LLM. And whatever response you are getting from the LLM, you will pass to the output parser.

2:0:13

Correct. So guys, this is a pipeline. How will you build this kind of pipeline? How will you build this kind of

2:0:17

pipeline using LCEL. So guys, you can say that LCEL is a functionality or a sub functionality provided to us

2:0:26

by Langchain, just like template, just like output parser, etc. Okay. Let's write a very, very basic code using

2:0:32

Lankchain expression language and then we will, we are done with the class. Okay.

2:0:38

So what we're going to do is we will create a new app 2.py, a new file. And here everyone, we will

2:0:44

again import the same thing. First of all, Lankchain, first of all, Lankchain, open AI, import,

2:0:52

chat open AI, then from Lankchain core.compts, import, prompt template. And then, from Lankchain, core.

2:1:02

And then everyone, from Lankchain core, we will also import from Lankchain core dot, import, import, import, output, import, import, output, import, import, import, import,

2:1:32

string output parser. STR output. Why this is not coming in the auto suggestion.

2:1:45

Anyways, so these two things we have already used. Now we are adding one more feature, which is output

2:1:50

parser. Everyone, clear? We are just adding one more feature, which is called as output parser.

2:1:56

Okay? We will use the same way to create the client.

2:2:02

paste. Okay. Then we can use the same prompt template itself. No need to write again and again. Use the same

2:2:12

prompt template. Copy to app 2.py. Then create an output parser object. St.R output parser.

2:2:32

folks, what we're going to do is we will create a chain now. And how do we create a chain?

2:2:39

Now, if you see, Brian, you want to create a chain, but first you need to decide the series of steps in the chain.

2:2:49

In this everyone, can I say that the series of steps is going to be prompt, then LLM, and then what do you see, the output parser?

2:2:58

Correct? So, for better naming, for a better understanding, let's call it as LLM.

2:3:02

LM. Okay? So can I say that even? The chain is going to be something like this. That create a prompt, pass it to LLM and then go to output parser. Correct?

2:3:13

So, guys, how do you create this? Create a prompt template.

2:3:19

Okay? Prompt template. Go to prompt template.

2:3:25

Then you use the pipe symbol. Okay. So guys, you can name this prompt only for better understanding. Just give prompt.

2:3:32

For from prompt, go to LLM and then go to output parser.

2:3:37

So guys, when you use this pipe symbol, okay?

2:3:40

So Lanchine will automatically understand that, that these are individual components, right?

2:3:45

And prompt, you need to pass to LLM.

2:3:48

And whatever output LLM will generate, you will pass to output parser.

2:3:52

This is the chain that you have created with the help of pipe symbol.

2:3:56

This is how you create a chain in Lankchain.

2:3:59

Are you guys getting this point?

2:4:01

This is a syntax more or less, right?

2:4:02

This is the syntax provided by Lankchain.

2:4:07

Are you guys getting this point?

2:4:08

We will see a lot of examples on this.

2:4:09

You will get familiar.

2:4:10

But for now, is this clear to all of you?

2:4:14

Okay.

2:4:15

And now, folks, what we're going to do is we will invoke this chain, chain dot invoke.

2:4:21

Okay.

2:4:21

Now tell me everyone to invoke this chain, what input do you need?

2:4:28

Can is that you need four input parameters to pass to the prompt?

2:4:32

right? That you can pass inside the JSON, right?

2:4:40

That what is topic is, let's say, SQL indexes.

2:4:45

Then audience is, let's say, beginners.

2:4:53

Then tone is, let's say, simple.

2:5:02

is, let's say, 100.

2:5:07

Are you guys getting this point?

2:5:10

Folks, is the syntax making sense to all of you?

2:5:20

Okay?

2:5:21

And finally, everyone, we will just print the, okay?

2:5:24

So, whatever response you are getting from this chain,

2:5:32

pause. So, let me elaborate what we have done. Same thing, prompt template, same thing,

2:5:39

LLM, same thing, output parser. So if you see, there are three components. First is prompt, second is

2:5:44

LLM, third is output parser. Okay? And then everyone, this string output parser, actually we'll

2:5:51

discuss in the next class, okay, in detail. We are creating a chain out of it. The only thing that you

2:5:56

need to remember is how are we creating chains? We are not telling LLM that you need to call this, you need to

2:6:02

start from this, then you need to call this from A to B to C to D. We are not telling

2:6:07

them. But Langchine will understand that because we are using the pipe symbol. So if we are

2:6:12

writing A, pipe symbol B, pipe symbol C, pipe symbol D, Langton will automatically understand that.

2:6:18

We need to start our execution from A. Output of A we need to pass to B as an input. Output of B,

2:6:24

we need to pass to C as an input, and so on. Everyone clear?

2:6:32

Okay.

2:6:36

And then everyone, we will finally print the response.

2:6:40

So go to the terminal.

2:6:45

Clear and run app 2.pi.

2:6:49

Okay, there is some error. What is this error?

2:6:52

Input to prompt template is missing limit.

2:6:54

Oh, sorry.

2:6:55

It is limit, right?

2:6:57

Not word count.

2:6:58

Give the word limit.

2:7:00

Okay.

2:7:01

It maps one to one.

2:7:02

If you see everyone, it is very easy to build applications using Langchain.

2:7:11

After two, three classes, you will appreciate it.

2:7:13

And this is the response that we are getting.

2:7:15

Now tell me, everyone, I think you will automatically understand the meaning of output parser.

2:7:21

If you are printing a response here in app 1.py, okay?

2:7:27

Let's say if I run app 1.p.py, I am printing the response here without to output.

2:7:32

parser? What response you are getting? Let's see. Without output parser, let's see

2:7:42

what response you are getting? Do you remember that we were getting the complete response

2:7:46

object? Correct? Yeah. If you see, we are getting the complete response object in which

2:7:57

content is there, right? And lot of other fields are there. Retriever is there. Right. Right.

2:8:02

not retriever. Tokers are there, completion tokens, model name, fingerprint,

2:8:08

ID, log props and whatnot. But if you are using STR output parser or string output parser

2:8:17

in app 2.py, and now if you run app 2.py, do you see that we are just getting the

2:8:25

response or the content, not the complete object? This is the main difference. I hope this makes

2:8:32

all of you. Right? So we can simply say that, we can simply say that, that without,

2:8:41

yeah, here I can write a comment here, without string output, parser, model, model returns the

2:9:00

complete response object. Correct? With

2:9:07

string output parser, what model returns?

2:9:15

We get a, we get the, we just get the content string string string string string,

2:9:30

Everyone clear?

2:9:38

Folks, how many of you are clear? Yes or no?

2:9:42

How to generate response in streaming format here? We will see that, Abyshe. We'll see all those things.

2:9:47

Right. So, for example, for example, Abyshek, coming to your question, there are different ways in which you

2:9:53

can make the IPA call. So, here you are making via invoke. Okay? You can do stream here. You can do batch here.

2:10:00

Okay. So there are three ways invoke slash stream slash batch. We will see that in the next class. Okay.

2:10:09

What if we had unset parameters variables somewhere in the middle of the chain, rather than at the first

2:10:13

component will chain, invoke, understand the same way. Unset parameters, then you will have to give some

2:10:20

define, you have to give some default value for that. Okay. I'll have to check the way for that.

2:10:26

But you can definitely give the default value. If the user is not passing those value, you will

2:10:30

fall like you will fall back to the default one okay yeah okay so folks that is it for today's

2:10:37

class uh let me first of all push the code to get up let me quickly create the repository

2:11:00

books, books, uh,

2:11:30

there is a code. The code is present at this link. You can access it here. And let me push the notes as well.

2:12:00

Yeah, folks, these are the class class notes.

2:12:30

Would you please check?

2:12:38

Okay, so let's have the quiz now.

2:12:42

Okay, uh, so folks, I think I don't have the quiz for today's class.

2:12:50

I think I don't have the quiz for today's class. I think a quiz was not there, right, Samya. I forgot to add the link, I guess.

2:13:00

Okay, no worries, everyone. So we'll have the quiz today. We'll have the quiz in the next class.

2:13:05

Just wait for a few seconds, everyone. It will get loaded because the nodes are pretty heavy.

2:13:10

So it takes GitHub to process this. Okay? Because GitHub does this asynchronously. Okay. That's why it is not available for now.

2:13:21

Just try this after a few seconds, it will be working. Yes, now for Mukul, it is working.

2:13:26

Folks, how many of you like the today's class? How many of you got everything from today's class?

2:13:30

Thank you so much for attending the class, everyone. Despite being, I was not well. Thank you so much for attending.

2:13:41

Thank you so much for attending. I will launch the feedback poll now. Please take the poll. And then we can drop off. Okay. Thank you, everyone. Have a good day. Take care. Good night. And bye-bye.

2:13:49

Thank you, folks. I think we have covered pretty good things about Langchain in the first class itself.

2:13:58

We will have few more classes on Langchain to discuss all the in-depth fundamentals of Langchain, along with a lot of working solutions on Langchain, right?

2:14:07

We will build multiple projects as well going forward.

2:14:14

Any resource? Gurkreth, in the last class, we had last class on Olam. In the Olam. In the Olamma,

2:14:19

notes, you will find the resource. In fact, in the last class, I showed you that how can you do

2:14:23

that via local LLM? If you want to see the Langchain with local LM, then you'll have to go through

2:14:28

the documentation of LLM. Document of Langchain. Okay? There were a lot of things that I was doing

2:14:34

differently in more difficult ways. So it was very useful. Very good, sorry, very good. That is a goal.

2:14:39

That is the entire goal for this series of lectures, right, to make development easier and more efficient.

2:14:45

Okay. Done. Thank you so much for the feedback, everyone. Have a good day.

2:14:49

And we can end the class. Thank you. Bye-bye. And take care. Bye-bye.

2:15:19

Thank you.

2:15:49

Thank you.

2:16:19

Thank you.

2:16:49

Thank you.

2:17:19

Thank you.

2:17:49

Thank you.

2:18:19

Thank you.