0:00

Thank you.

0:02

Thank you.

0:32

Thank you.

1:02

Thank you.

1:32

Thank you.

2:02

Thank you.

2:32

Thank you.

3:02

Thank you.

3:32

Thank you

4:02

Thank you

4:32

Thank you

4:34

Thank you

4:36

Thank you

4:38

Thank you

4:40

Thank you

4:42

Thank you

4:44

Thank you

4:46

Thank you

4:48

Thank you

4:50

Thank you

4:52

Thank you

4:54

Thank you.

4:56

Thank you.

5:26

Thank you.

5:56

Thank you.

6:26

Thank you.

6:56

Thank you.

7:26

Thank you.

7:56

Thank you.

8:26

Thank you

8:56

Thank you

9:26

Thank you

9:28

Thank you

9:30

Thank you

9:32

Thank you

9:34

Thank you

9:36

Thank you

9:38

Thank you

9:40

Thank you

9:42

Thank you

9:44

Thank you

9:46

Thank you

9:48

Thank you.

9:50

Thank you.

10:20

Thank you.

10:50

Thank you.

11:20

Thank you.

11:50

Thank you.

12:20

Thank you.

12:50

Thank you.

13:20

Thank you

13:50

Thank you

14:20

Thank you

14:22

Thank you

14:24

Thank you

14:26

Thank you

14:28

Thank you

14:30

Thank you

14:32

Thank you

14:34

Thank you

14:36

Thank you

14:38

Thank you

14:40

Thank you

14:42

Thank you.

14:44

Thank you.

15:14

Thank you.

15:44

Thank you.

16:14

Thank you.

16:44

Thank you.

17:14

Thank you.

17:44

Thank you.

18:14

Thank you

18:44

Thank you

19:14

Thank you

19:16

Thank you

19:18

Thank you

19:20

Thank you

19:22

Thank you

19:24

Thank you

19:26

Thank you

19:28

Thank you

19:30

Thank you

19:32

Thank you

19:34

Thank you

19:36

Thank you.

19:38

Thank you.

20:08

Thank you.

20:38

Thank you.

21:08

Thank you.

21:38

Thank you.

22:08

Thank you.

22:38

Thank you.

23:08

Thank you.

23:38

I think we can begin the session.

23:41

I think we can begin the session.

23:44

Abtita, I'm an audible.

23:50

Yes, you're audible.

23:53

Yeah, we can begin the session.

24:08

Thank you.

24:38

Thank you.

25:08

Can we start the session?

25:38

Thank you.

26:08

I think he's not available yet, but we usually do start by 8.15, so I think he should be starting soon.

26:24

Okay, good evening all of you. We are just starting out in a

26:28

in just a few minutes, couple of minutes.

26:38

Thank you.

27:08

Thank you.

27:38

Thank you.

28:08

Thank you.

28:38

Thank you

29:08

Hi, good.

29:12

Good evening all of you, good evening all of you, welcome to the session.

29:28

And today we have a very interesting.

29:31

We have a very interesting session.

29:32

Today we'll be starting out officially with agents.

29:35

So until the last session, we talked.

29:37

talked extensively about rags and just make me share my screen just one second.

30:07

Thank you.

30:37

Okay, yeah, so I hope all of you are able to see my screen.

30:41

And once again, as I mentioned, just to start the, set the context, what we talked about in the last session.

30:47

We looked at the fundamentals of, you know, how to build models.

30:53

We looked at how to, in terms of language models, we understood what large language models really are.

30:59

So we developed some intuition around that.

31:02

And so far in the curriculum, we have seen drags in a lot of

31:07

detail. So we discussed about the entire workflow of rags, how to build a rag system.

31:11

Last session was very interesting. We talked about memory, two memory,

31:15

long-term memory, short-term memory. How do we set the memory context? And today's session,

31:21

we talk about a very, very important topic called tools, agents. So we are formally introducing

31:29

agents in today's session. And we will discuss what agents are in today's session, right?

31:34

So what is the idea behind

31:37

discussing agents, what is the real life context about this today's session, particularly.

31:41

So the real world context and the overall use case of this session is that all of a sudden,

31:47

today's language models, whatever LLMs we are having right now, see, all this file, it was just a

31:51

question answering engine, right? All the LLMs that we have seen so forth, you ask a question,

31:55

you get a response. Again, you ask a question, get a response. Again, you ask a question, get a response.

32:01

So this is how we have seen the LLMs and language models, large language model will behave in a certain

32:07

way, right? You ask a question, generator response, ask a question, generator response.

32:11

That's how the whole, you know, workflow has been so far. But all of a sudden, now we are,

32:17

excuse me, now we are discussing how these large language models, whatever LLMs we are discussing

32:25

right now, how these large language models, you can now use for doing stuff. Not only is it that,

32:34

you know, you ask a question and they will generate an answer, but.

32:37

But now you, you know, we want to ask a question and you, and you want to use these large language

32:41

models for getting things down. We want to, you want to do stuff. So that is the business

32:46

value for this particular session. Okay. So now moving on. And obviously this is a starting

32:55

point to all that we will do in module four. We are still in module three right now. And if you see

32:59

module four is all about agentic design, but this is the, this is the starter modules that we are

33:03

getting into. And as we go to module four, we'll build on.

33:07

top of these concepts and we'll design more advanced agents as we go to that. All right.

33:13

So let us start on. And so today we'll be discussing about what an AI agent is. We will explain a very

33:23

interesting paradigm called a React paradigm. React paradigm is what we'll be talking about in today's

33:28

session. What is the React paradigm? And React is thought, action, observation. What is the

33:33

meaning of it we will discuss? Very interesting. And we'll do some very

33:37

real world demos today using a Google search API. We will actually use a light Google

33:42

search API. I'll show you how to connect to that. And we'll also use a Python tool. And we'll see

33:48

some very interesting demos. See, like for example, if I ask a question, what is the closing

33:56

price of Nifty in today's trade? You have to go and do an internet search, right? So we will see

34:04

how we can answer these kinds of questions using a tool call.

34:07

using the server search API. We will see that just like we have created the GROC API. Today we will also create a search API key. And I will show you how to do that. And finally, the big picture idea is we will build a complete Python React agent. We will build a complete Python react agent and the search React agent. We will be building two agents in our class. That's the idea. All right. So now, what are agents? What, you know, our agents?

34:37

And I think this is, what I want to do is let me, let me open up a small diagram that will help you really connect the dots and help you understand what agents really are.

34:51

What are we doing behind the scenes when we, when we talk about agents, what agents really are.

34:58

So, again, I'm going to give you a small analogy here. You can see.

35:05

agents are nothing but LLM plus tools. This is the simple diagram that we will use as reference for the rest of our session. And as I told you, so far, we have been dealing with only large language models, LNMs. We ask the question. You make an API call to the LLM and the LLM generates a response. So you write a prompt. All the exercises we have done, zero short, few short, chain of thought. You write a complete prompt, rack prompt, whatever. At the end of the day, what are you doing?

35:35

even in a RAC system, what are you doing? Ultimately, you're making an LLM call.

35:39

You're sending the question, you're sending the context. The LLM is processing that and is generating a response.

35:44

So all these exercises we have done, we are only dealing with the LLM.

35:49

Now what we are trying to do is. So, you know, if I have to give you an analogy, it is like saying all this while,

35:56

you are dealing with the LLM, which is like the brain of the system. You ask a question and the brain is able to give the answer.

36:03

So the brain is not able to move, like, it's not able to run around, do things for you.

36:08

You know, let's say you say, fetch groceries for me. It cannot do that. So right now,

36:12

our large language model is restricted. It can only think and it can answer.

36:18

I know, it can think and it can answer. But if I ask my large language model, you try this out. You go

36:25

to chat, GPT, and say, please fetch me groceries from the nearby store and give it to my doorstep.

36:30

It cannot do it, obviously, right? What will it do?

36:33

it can reason, it can tell you, you know, it can tell you, okay, please, I cannot do this and whatever, but it cannot get the job done.

36:42

So now, what we are doing is we have the brain already built. We have the LLM, which is the brain.

36:49

And now we are adding hands and legs. We're adding limbs.

36:55

So that it can move around, it can get things done. It can get tasks done. And those hands and legs and limbs are what we call tools.

37:03

That is the analogy that I'm trying to give all of you.

37:06

So, so you are now making the large language model more powerful by giving it ability to get things done.

37:15

You're making it more powerful by giving it the ability to get things done.

37:18

That is exactly what, excuse me, what, what, you know, what agents really are.

37:28

You're giving the LLM ability to get things done.

37:32

It can get things done more.

37:33

accurately. Okay, I hope everybody's, everybody's aligned, everybody is getting a sense.

37:40

I'm going to give you one more analogy. I'm going to give you one more analogy. So for example,

37:45

here, what you are able to see on the screen. And this combination of LLM plus tools is what we call

37:52

an agent. Next time anybody asks you, what is an agent exactly? There can be hundreds of general definitions,

37:57

you know, AI agent, something that does something automatically and all. You know, those are all

38:01

general conversation. Next time, when you're talking in a proper technical term, what is an agent?

38:07

Agent is LLM plus tools. You have a large language model. You integrate that with tools and that is

38:14

effectively what, you know, an agent is. The agent is nothing but LLM plus tools. That is what,

38:19

you know, it basically refers to. So again, coming to the use case that you are seeing on the

38:28

me if the user asks the question, how many customers have subscribed to the term deposit?

38:34

Let's say the user asks the question, how many customers have subscribed to the term deposit? If the user

38:38

asks the question, what will happen? So based on whatever question the user asks, the LLM will

38:47

now think, and it will also go back to the respective tools it is connected to, external tools.

38:55

And all of a sudden, the language model is not just able to answer questions based on what it knows,

39:02

because that was what we were doing all this one. There's a brain, RLM is like a repository of knowledge,

39:08

trained on a tremendous amount of data, right? We've been talking about all that.

39:13

So you ask a question, the RLM is able to relate to all that it knows and give the answer. But now,

39:17

all of a sudden, if you ask this question, the LLM doesn't know. How many customers have subscribed to the

39:22

term deposit? How am I supposed to know? I'm sorry, I don't know.

39:25

I need to connect to a specific database. I need to enter the right credentials. I need to pick up

39:31

the right table. I need to run the select query. You've all done select statement, right? Select

39:35

start from a particular table name. And only then you will get to know how many customers are

39:40

subscribed to the term deposit. It's not something the LLM has learned and it is not something the LLM has in

39:46

its own internal memory. So we are now taking that large language model and we are adding

39:55

external tools. You know, we are, we are adding external tools. And that's what the agent

40:03

basically is. You're adding external tools here. And what are the tools we are adding

40:09

right now? We are adding a search engine tool. We're adding a Python runtime tool and we're

40:14

adding a database tool. There are three tools we have added. This is take an example. And these are

40:19

all external tools. That means this is not like where the LLM can answer questions based on his knowledge

40:24

base. This is where the LLM will be able to go and look up in search. It will be able

40:28

to go and look up in a database. A SQL database it can connect to. I said that my SQL. You have

40:35

all done my SQL. All it can go and let's say, connect to a Python runtime. And I can get things

40:41

done. And this combination of LLM plus tools taken together is what we call an agent. And the reason why people

40:47

say why agents are so powerful? Why are agents so powerful? Because as I say, now not only are LLLN

40:54

able to think, LLMs are only able to think, but now if you look at the combination of LLM plus

40:59

tools taken together, if you give it access to enough number of tools, right now it's only the

41:03

three tools we are talking about, search engine, Python runtime database. What if you give it

41:09

access to multiple tools, other tools, Facebook tool, Google search tool, maps tool, a robot

41:14

tool, maybe you're giving a language model access to a robot tool, some other, you know,

41:20

like a robot dog or something, you know, or a robot vacuum.

41:24

Now all of a sudden you ask that same question that, hey, please get me my, a mango, get

41:30

me a mango from this shop two kilometers away. So now the LLM is not just able to think and

41:35

answer, but the LLM is able to get things done. The LLM is able to understand what you asked.

41:40

It's able to talk to that external tool, the robot dog and the dog is going and fetching the stuff

41:46

for you and giving them back to you. So this system as a whole is what is called an agent. And in this

41:52

example also if you see what's happening is you ask a question the LLM now accesses

41:57

the database tool because it has to talk to the database tool it cannot directly answer it

42:02

has to talk to the database tool to answer that question it talks to the database tool

42:06

and based on that it you know it is able to formulate that answer that's what agents

42:13

are guys I hope everybody is aligned and the story is clear what it is I'm going to give you

42:18

one more analogy okay I'll give you give you one more analogy and I'm sure you'll be

42:22

convinced after this. The new topic I know there'll be some confusing

42:25

confusion. Let me give you one more analogy and you'll be convinced. I'm 100%

42:29

sure you'll be convinced. Let's take this analogy. The LLM is like the

42:33

manager. This is like a manager. Okay. The manager is somebody who will not do

42:41

anything, not quite. You know, it's not like that in today's world. Today everybody has to

42:45

work. So go on other days when managers were giving orders to other people, other people

42:49

are working, you know, everybody has to work to work.

42:52

everybody has deliverables but let's just say for this example the the manager is the person

42:57

who doesn't do anything the manager is the person who only plans the manager comes in the morning

43:03

sees what are the tasks are there manager has got three people in the team these are the workers

43:11

okay tools are the workers workers are the people who have to get the things done

43:16

the manager will say search engine is a worker one the python runtime is worker two database is worker three

43:22

so manager will do all the advance work they will do all the nice work they will see the request

43:28

and they will give it to worker one worker one you do it manager will get another request and it will figure

43:35

out what to do and it will give it to worker two worker to the person who is actually doing the task

43:40

so this is the analogy that you can also think of manager plus worker combination and this is like

43:46

you know the client let's imagine this is the client

43:52

so the manager is the person who will directly interface with the client

43:55

the workers will not talk to the client there's always that the front office you

44:01

know that interaction the person you interact with like project managers delivery

44:05

managers the other ones who will usually talk to the clients you know like junior

44:10

developers will not talk to the client okay so uh that's how it is you know there's a there's a

44:15

funny thing like you know when i i used to work in imposes you know like again i don't know how the

44:20

story is right now

44:22

this was back in 2011 it was amazing campus and you know i was in my sole campus actually that time

44:28

and uh very interesting you know whenever client visits used to happen you know we we felt like

44:33

animals in a zoo they used to see us no we cannot talk to anybody because we were asked not to

44:37

so clients will only talk to managers but we were like animals in a zoo so they used to come and see oh

44:42

you know we are all like thousands of people working in india office so they all come to see us so

44:48

anyways so uh the idea is clients will only talk to managers right

44:52

so clients will only talk to managers client will give the request to the manager

44:59

and the manager is that very smart intellectual being who is able to figure out how to get things

45:04

done that's the lLM right at nm is the the main brain think about it that way and that's the main

45:10

brain so so so so so the client asks the question and the manager is now able to reason

45:17

and think that hey how do i how do i get this thing done for my client

45:22

i have got three workers in my team i hired last month i have three workers in my team and the

45:27

manager should know everything about their workers right if you're part of a team the manager

45:31

should know everything about you so the manager knows what the search engine guy can do the

45:35

manager knows what the python runtime guy can do and the manager knows what the database

45:40

i can do and if you have to go one level deeper in case you're wondering uh sir what are these

45:45

things exactly these are like python functions so these things are basically python functions

45:50

we will see the code in a while you will realize how easy it is in a while okay these are basically

45:55

python functions so the manager should know what each and every worker in the team is capable of

46:01

doing and based on that the manager will delegate the task to the respective workers the manager will not

46:07

send a complete client request to the workers because that is not what the manager will do of course

46:12

the manager has a road and you know it's not not to say the manager is not doing anything the manager

46:16

is able to understand that very complex query from the client it is able to understand the

46:21

organization needs they're able to understand the client needs is able to understand who can do what

46:25

different workers have different schedules some people are on leave some people are not on leave so the

46:31

manager is the person who is acting as an orchestration library an orchestrator

46:36

a scheduler planner because the manager is able to do all the reasoning that's the brain

46:42

so the manager assigns the work based on the request it is getting

46:46

The manager says, say, say database guy,

46:49

database guy, please get the work done for me.

46:51

The manager assigns the work to the database guy.

46:54

And the database guy is the person who will complete that task and give the results back to the manager.

47:01

And the manager will now see what's the work done correctly because the manager is the brain.

47:06

The manager is super smart.

47:07

The manager understands what work was done, what is needed.

47:12

He or she will not do the work, but, you know, when you see, if you're

47:16

a manager, if you dedicate the task to somebody, you know what to get back, right?

47:19

You know, I cannot say write a Python program and you draw me a picture of mountain and the sun and clouds

47:24

and give it to me, right? At least that was common sense manager should have, right?

47:28

This is the request is how many customers have subscribed to the term deposit.

47:31

You give it to a database guy. Data base guy is able to complete the work.

47:34

Database guy cannot draw a, you know, a picture of sun, moon and stars. So the manager should know

47:39

that. If a mistake is made, manager should have the ability, should have the ability to go and

47:46

reassign that task to the same worker or the different worker.

47:51

It is the iterative process.

47:53

And this will keep happening, going on and on and on and on.

47:56

It's like the project cycle will keep going on and on and on until the manager gets the

48:00

perfect answer from the entire team combined.

48:04

And once the manager gets the perfect answer, I'll use a green color because the task is

48:08

complete now, the manager will give it back to the client.

48:11

The client is happy, manager is happy, team is happy.

48:14

So this is basically how you think.

48:16

of agents. And the reason why people say that agents are so powerful today, agents are able to,

48:21

there's so many stories we hear, right? You know, like, you're all hearing about so many stories

48:26

and so many, you know, ideas around agents. The reason why agents seem to be so scary is because

48:30

if you look at it, intuitively in agents, what happens is the, if you can have enough number of external

48:40

tools, if you can connect enough number of external tools,

48:46

that's where it gets very scared because all of a sudden, you know, it will start to get things done.

48:52

It is not only able to think and reason, it is able to get things done. And that's the part that is very scared.

49:01

I can give an example to you, right? Let's say database. Let's a file system. There's another guy who is able to work through your file system. Let's add a few more workers to the team.

49:15

Let's say there is another guy who is able to work through your file system. Let's add a few more workers to the team. Let's say there is another guy.

49:16

who is able to connect your bank account and get things done.

49:19

And I say there is another guy who is able to connect to your uh, uh, uh, zero-thah account

49:24

and get things and all of you, many of you might know zero-thai is the stock market platform,

49:28

stop-broking platform, zero-thaka-eat and zero-ha coin. And zero-da also as agents, you know,

49:33

not today, but later on when we go to some of the advanced topics and show a live demo,

49:37

not with real money, but and show a live demo, how you can connect to zero-dha and how you can do things.

49:42

Now what if, what if you're giving connectivity to external

49:46

tools now. Now all of a sudden you can talk to a file system. You can talk to a bank account.

49:53

You can talk to a zero-thah-tight. So these are all external tools. These tools can connect your

49:58

bank account. They can execute instructions, credit debit. These systems can talk to your zero-th-thi-thi-thi-thi-th.

50:05

These systems can talk to your local file system. And they're able to get things done. So we are not

50:11

just limited to asking a question, getting an answer. We are now able to.

50:16

to execute commands, the manager is able to execute commands to the workers and the tools,

50:21

and the tools are able to get things done. And the scary part is if something goes wrong,

50:26

like in a file system tool, it can delete the wrong file. The bank account tool, it can debit

50:33

$10,000 rupees, and the zero-hackight, it can, you know, completely, you know, your portfolio will be gone maybe

50:40

in a matter of a day. I'm just saying, these are real things that have happened. And that's a scary part. Or

50:45

maybe if you go back to a database, an entire production database can be deleted by mistake.

50:51

And how difficult it is to delete a production database? How difficult? Nothing. Nothing.

50:55

Trunket data, truncate, delete command you can do. There are delete commands you can do. There are drop

51:01

commands you can do. There's a drop database. All of you know, it's a drop database command, right? You do drop database.

51:06

What will happen? The whole database will be gone. Obviously, there'll be controls, you know, administration

51:11

controls will be there. But, but I'm just saying, this is the reason why agents,

51:15

scary because, uh, because they're able to get things done, if the reasoning is not right,

51:23

if the manager sends the wrong instruction, so far it was like, you know, you ask, and many of you

51:28

have seen, right? In chat, GPT, oftentimes we get wrong answers. So all this while we were limited to,

51:32

okay, you know, we are getting a wrong answer. It's not impacting us. You ask the question again and

51:36

you, you know, you, you see what results we are getting. But now all of a sudden, you, you know, all of a sudden,

51:43

what do we have? All of a sudden, the manager is giving instructions to get things done

51:49

to the tools. And if the manager gives a wrong instruction, the tools will do the wrong thing.

51:56

That's why they're scary. Right? And An Ankit, absolutely, you asked a question, can Alex stop preparing

52:00

the shopping list? Absolutely, it's an agentic concept. Whatever you're saying. So you can think

52:04

of the large language model, which is the manager, you give it an instruction that, hey, please place

52:08

an order for me for this item. It will reason. It will prepare a shopping list. It will place the order.

52:13

repeat the money from the Amazon pay and it will complete the task. So that is

52:17

completely an agent. Okay. Now, I hope the manager worker analogy will really stick with

52:29

everybody. This is like a simple way to think through what agents are. Next time,

52:33

anybody thinks of agents. You know, you can think of it like there's a manager, there's a worker.

52:38

That's it. There can be hundreds of workers. It can be hundreds of tools. Tools are nothing but

52:42

workers. They are able to get things done. Ah, yes, yes. I mean, good, good point. Yes.

52:48

There have been cases on that. In fact, there is this other, you know, very, very, very popular framework,

52:54

actually, open claw. I'm sure people would have heard of it. It is a, it is an agent that you can

52:59

install in your file system. And that is very scary because I was talking about this tools and

53:03

if you install that agent in your file system, you know, we have heard of cases where people's files

53:10

were deleted overnight. Gone.

53:12

And you're giving it always permissions, right, the operating system level permissions.

53:18

So again, the idea is still the same. You still are the language model that is reasoning.

53:23

Ah, WhatsApp, telegram, everything. It can control everything, right? It can control every aspect of it.

53:29

We have agentic browsers today. We have agentic browsers today, which are able to reason and get things

53:33

done for you, like Comet browser. We can literally, actually, WhatsApp is blocked in Comet.

53:40

Comet blocks WhatsApp. If you try to open WhatsApp from Comet.

53:42

Facebook blocks your WhatsApp accounts temporarily. So that's another thing. But if the language model

53:49

does the wrong thing, what will happen? It will execute the wrong command. It will delete the wrong

53:58

files. All this will happen. As you rightly said, WhatsApp and Telegram, if you have connections too.

54:05

And if the LLM, the manager gives a wrong command to the WhatsApp too, the wrong message too, the wrong

54:12

will be posted to somebody else.

54:16

Now let us understand how this is happening a little bit more in detail, right?

54:21

And then we will straight here we go to the hands on today.

54:24

So this is pretty much it. This is the general concept of an agent.

54:27

So we have the React paradigm. This is the paradigm. This is the basic framework based on which agents are working.

54:34

Now, some of you who are coming from full stack development codes and all that,

54:38

you might have heard of React, reason and act. This is like a, you know, you

54:42

you can think of it like a front-end development framework, but it's not. This is not the same

54:45

react we are talking about. So this react is basically the, you know, this, this particular react is

54:52

effectively the agentic paradigm that we are discussing. This is the agentic paradigm that we are

54:59

explicitly looking at right now. Okay.

55:12

So what is the React paradigm right now?

55:17

So we have thought action observation, thought action observation, thought action observation, thought action observation.

55:22

So this is the chain or the loop that you are following.

55:26

So first you think, then you act, then you observe.

55:31

Again, you think, you act, you observe.

55:33

Again, you think you act, you observe.

55:36

Excuse me, we do multiple thought action observations, thought action observations and all that.

55:42

And at the end of the day, we get the final solution.

55:46

So React basically stands for what is the full form of React, it is reason and act.

55:53

So React stands for reason and X. First you want to reason and then you want to act.

55:58

So React, I repeat, stands for reason and act.

56:02

That's what React stands for.

56:04

So and the framework broadly looks like first you think what to do, there's a thought.

56:10

then you act and then you observe whatever, you know, observations you are getting, right?

56:16

So first you think what you do.

56:18

The first you think, this is like exactly the analogy of the manager and the worker that we talked about.

56:24

So customer asked a question to the manager, LNN, and the manager first thinks.

56:31

Manager is the person who is having the brain.

56:34

Let me say workers don't have the brain.

56:36

So the manager is the person who is able to think, what to do.

56:38

Let's just say.

56:39

The manager is the person who is able to think what to do.

56:39

Let's just say.

56:40

has the brain to get things done, right?

56:42

The client sends a request, manager thinks hot, then the manager acts.

56:48

Manager figures out, he's going to do.

56:51

Okay.

56:51

And then the worker completes the task manager observes.

56:55

Come who, not?

56:57

Again, manager thinks, okay, does this solve the problem for the client?

57:05

Though it does not, then again, you act, again, you observe.

57:09

And this happens, this keeps going on and on and on, exactly the analogy that we were discussing,

57:13

thought action observation, thought action observation, thought action observation, thought action

57:16

observation, this will get the final solution.

57:22

And some of you might be wondering that, science just looked incredible, but how do we do it?

57:27

How do we do it?

57:28

Well, we have a system message.

57:29

All the magic is happening in the system message.

57:32

I will show you the system message very shortly.

57:33

What is it?

57:34

Again, it's a starter session today.

57:35

We won't get very much into the details of it, but at least you will get a sneak peek into it,

57:39

that's, okay?

57:42

100%, Mahmath.

57:44

Ali, yeah, absolutely, 100%.

57:46

What you're saying is absolutely, right?

57:47

Definitely, definitely.

57:48

All the magic is in the system message.

57:51

You have to talk to the manager, right, Ali.

57:54

If you, so, so Ali, let's look at the analogy.

57:58

You are the client and you say, okay, I don't want this to happen.

58:02

So you have to give that instruction to the manager.

58:05

And manager means LLN.

58:07

And how do you give instructions to the LL?

58:09

system message of the LLM.

58:11

So that particular thing that you mentioned, that I do not want to delete sensitive files.

58:16

I don't want to delete database.

58:18

I only want to run, insert, update, select, delete, you know, select queries, not insert

58:23

update queries.

58:24

All of this reasoning you will specify in the system message of the agent.

58:29

The system message of the agent is where you will specify all these details, right?

58:33

Makes sense.

58:36

Setting guardrails.

58:38

Yeah, guardrails is another.

58:39

topic, you know, again, we'll see guardrails again specifically later.

58:42

But yeah, for now, a simplicity, you know, a simple way, what you can do is you can explicitly

58:48

incorporate, you can explicitly incorporate these kinds of things in your system message.

58:53

And this is very important because if you don't explicitly tell the manager what it can do,

58:57

what it cannot do, the manager will give the wrong instruction.

59:01

Go if you put me put me, go and delete the file, that he'll do.

59:04

But it's very important that you give the constraint, you know.

59:07

what I'm saying is, you know, what I'm saying is, imagine this is the LM, Tiki.

59:12

We want an example with it, tools and workers, okay, and you have a file system tool.

59:18

Because there's a file system tool.

59:20

I'm just giving a, you know, just a very big picture understanding, what it refers to, okay?

59:24

So, let's the client request here.

59:26

Client asks the question to the manager.

59:28

Please go and delete the files.

59:30

Please go and delete all the files in my file system.

59:32

Clients request.

59:33

What will the LLM do?

59:35

LLM, socha.

59:36

Okay, what is my client asking?

59:37

Okay, fine, delete the file.

59:38

Okay, no, no, file system guy, manager assigns the task file system guy to.

59:43

So file system guy will execute the OS command and all the files are gone.

59:46

Is it the manager's mistake?

59:47

No, manager's what mistake is.

59:49

Client center request manager is only servicing that.

59:52

Okay, if the client says delete the file, manager will do it.

59:57

How do you prevent that?

59:59

Well, you will have to go and do all this magic in the system message.

1:0:04

There are other ways to do it also, but for now, whatever we have discussed, so,

1:0:07

for system message, we have a restriction way.

1:0:12

Amit was mentioned a interesting term called guardrail.

1:0:15

Guard drill is a term that we use.

1:0:18

So some term use, guardrail, what kind of safeguards are we going to do?

1:0:21

So we'll explicitly mention in the system message that,

1:0:24

most you cannot, cannot delete files.

1:0:26

Even if by mistake, you host, by mistake, mistakes can happen, right?

1:0:29

You know, people can make all sorts of mistakes.

1:0:31

You know, the client's account might get hacked.

1:0:33

We hacked to a client account.

1:0:34

How can't do?

1:0:36

Somebody hacked into the client account.

1:0:37

account and giving the instructions.

1:0:38

You don't know, right?

1:0:40

So client account to hack and go,

1:0:42

any instruction, did you delete the files?

1:0:43

LLM cannot service it.

1:0:45

LLM will not know who is the bad guy, who is the good guy.

1:0:48

Who is the good guy?

1:0:48

He's what? LLM will simply get the question,

1:0:50

Trump, give the response.

1:0:52

But LLM will have restrictions at its level

1:0:57

where it will understand, okay, this is what I can do.

1:0:59

This is what I cannot do.

1:1:01

That's one way for you got.

1:1:03

Yeah, yeah.

1:1:05

Yeah, exactly, exactly.

1:1:07

in future, we're already doing this.

1:1:08

We're already doing this.

1:1:09

It's very much a big part of what's happening today.

1:1:12

And I think, I think, absolutely.

1:1:15

I think it's very scary and also it's very interesting.

1:1:17

There's so much you can do.

1:1:18

So much you can do is only growing today.

1:1:21

And again, I mean, we'll see more examples as we go along, but it's growing.

1:1:25

It's already very, very big.

1:1:30

Exactly.

1:1:31

Self-criticism can't.

1:1:32

A simple thing is prompt engineering.

1:1:34

Basically prompt-cheek-se-se-like-na.

1:1:36

System message has to be a very big.

1:1:37

very detailed prompt basically okay ah something like that exactly exactly like

1:1:43

like chat gpt repuises to answer some questions you can give that system message okay now uh

1:1:49

with that let's move on so i i want to really focus more on the the hands on today hands on is very

1:1:55

interesting today and this is pretty much the summary and what we will see today is the now we will

1:2:01

go back and see exactly what this paradigm is and uh using this react paradigm how we can go back and

1:2:07

explicitly uh solve the problem so let us go to the uh the hands-on just give me

1:2:17

one minute guys i'll share this with you don't worry i'll share this with you don't worry i'll share the

1:2:25

notes and my slide with you also

1:2:37

folder is 11 June that's the folder for today all the contents are part of your folder

1:2:49

right now as we speak and now let me quickly go ahead and uh open up the grok python search data frame

1:2:56

agent okay so first i will take you through the notebook and parallelly as i take you through the notebook

1:3:00

i will discuss some theoretical concepts periodically in this notebook okay that's the way how we will

1:3:05

go through the session

1:3:07

Now, first things first, we will, we will install the necessary packages that are required here.

1:3:17

So let us go ahead and install the necessary packages.

1:3:20

Let me just give me one second.

1:3:21

Let me, Dr. Buk here. Okay, perfect. Yeah. So we will go and install the all the necessary

1:3:43

packages that we have right now and let me install it. And most of these are all land chain related packages that we

1:3:50

used in our last rag session they will really make it very easy for us to build agents and

1:3:54

going forward uh land chain is will be a very very important library that we'll be using to get things

1:4:00

done so we are installing all the necessary packages okay and this is our package for google search

1:4:07

results that we are using to connect to the live google search okay i i i can share the set up

1:4:14

with all of you how we are doing this how we are explicitly doing this part i can discuss a set up with you

1:4:19

so so the name of the website is called surper dot dev this is very interesting

1:4:32

the name of the website is surper dot dev you guys can set this up later it'll ask you for an email address

1:4:38

password it's a free account they give you 2500 credits for free which is i think quite a lot for

1:4:44

learning and demos and all these things and what i have done is i've gone to

1:4:49

surper.def is basically a search playground it is you know it is give you know it helps

1:4:55

you do google search programmatically see google search we can always go to google.com and we can

1:5:00

search you know we're not talking about that we are saying programmatically how do we do

1:5:04

google search that is what the serp API is okay it's an API so that means uh inside the code inside

1:5:12

the code if i show you inside the code i show you inside the code i can run command

1:5:19

like who is the founder of tesla this is google not this is the programming

1:5:23

environment so i can go and ask this question it will call the search API so this request will hit

1:5:28

the search API Google search and it will get the response back here query one that's how

1:5:33

that's the way the search API will work out maybe you can see this one in action okay

1:5:44

you have to create an API key as i mentioned there's an API key that you will have to create

1:5:49

So once you are done with this, you need to go and create an API key.

1:5:52

This you guys can do later the same way that I set up GROC.

1:5:55

GROC maybe we have a so everybody today has the GROC to a set up.

1:5:59

So similarly you can also set up the surfer.diff.

1:6:02

You can go to API key.

1:6:03

You can create an API key, just make sure that you are created the API key.

1:6:08

And then what is the next story?

1:6:10

Go back to Colap Secrets, go to Google Collab Secrets.

1:6:14

The same way that we added, the same way that I added GROC APIP, all our sessions.

1:6:19

we were using GROC API key, right?

1:6:21

The same way I have added GROC API, similarly, you will add something called surfer API key.

1:6:27

You will give it the name, Surfer API key.

1:6:32

Let me print to show you, add to Collap Secrets, name will be Surper API key, and the value will

1:6:39

be whatever you copy and paste from here.

1:6:40

You copy the value and you go back and paste it here, that's it.

1:6:44

So this is how you set up your surfer access.

1:6:47

And you can programmatically do search from here on which, okay?

1:6:53

So what did we talk about here?

1:6:54

We talked about how we can set up the surfer tool.

1:6:57

What is that surfer tool?

1:6:58

What is that search tool?

1:7:00

Which will come in very, very handy going forward.

1:7:02

Okay.

1:7:04

Next, I have already installed the necessary packages.

1:7:08

Now I will do the import.

1:7:10

Is that the import commands?

1:7:11

And here I'm going to just go and set, fetch the server API key.

1:7:16

And also fetched.

1:7:17

the GROC API key and instantiate the model.

1:7:21

Because we will instantiate the model.

1:7:24

So the name of the GROC model we are using is Lama 3.370 billion versatile.

1:7:30

So we will instantiate the model.

1:7:34

And this is the thing that we are doing right now.

1:7:37

So we are simply fetching the GROC API key.

1:7:39

And with the GROC API key, we are simply instantiating the LAM model, the Grog LLM.

1:7:44

And we are also instantiating the surfer API.

1:7:46

We are fetching it.

1:7:47

from Collab Secrets and we are assigning it to the server API key variable.

1:7:51

So that part is over.

1:7:54

Now let's move on.

1:7:55

Lankchain implements React, as I discussed on.

1:7:57

React framework.

1:7:58

This is the basic way how we will be seeing agents right now.

1:8:02

React stands for reason and act.

1:8:04

Based on a question, the agent will first reason what to do.

1:8:07

The manager will first reason what to do.

1:8:08

And then it will go and act on the basis of that.

1:8:14

Now, moving on.

1:8:17

First things first, what I will do.

1:8:20

I will create the two tools, right?

1:8:26

I will create the two tools.

1:8:28

If you recall my slide right now, I said that, you know, so we want to create two tools here.

1:8:36

So one of the tools that we have right now is the Python runtime tool.

1:8:44

So what is this Python runtime tool?

1:8:46

the Python runtime tool is basically nothing but Python Ripple.

1:8:50

So we were instantiating a tool called Python Ripple, which is a predefined tool from Langchame.

1:8:55

We're importing it.

1:8:56

We don't have to write anything there.

1:8:58

Today's class, we are simply importing the tools.

1:9:01

So two tools we will see in the class today, Python Rappel tool and Google Server API tool.

1:9:09

So what do these tools do?

1:9:11

The Python Rappel tool will be used to execute Python.

1:9:16

Just to show you, if I import the Python repo tool and if I run this code, see, it is actually printing out this Python command.

1:9:24

And you can write anything. You can write anything. You can, you can, you know, you can, you can go back and incorporate any other Python query.

1:9:39

Maybe I can show you another one. So simulate, show another, show another, show another, show another, uh,

1:9:46

small Python demo using the Python Ripple tool and you'll be able to see how it is

1:9:58

able to write the Python inside it, right?

1:10:02

So you can write any Python query inside and the Python Ripple tool is the guy that is

1:10:07

the guy that is responsible for running that port.

1:10:09

Okay, I think the people can relate to it.

1:10:13

Ah, ha, ha, ha, we write in, uh, we write in, we write in, uh, we write in, uh,

1:10:16

books, correct, absolutely. But this is where you want to programmatically do it.

1:10:21

You want to programmatically do it.

1:10:24

Okay. If I click on accept and run, you will see that I'm getting 30.

1:10:33

So, interesting thing is, if I go and take this thing, you know, I think, Anket, I'll try to answer your

1:10:40

question in a better way. Let me go back to chat GPD for a minute.

1:10:44

ChatGPT is a chat interface.

1:10:46

If I ask this question, sorry, what happened here?

1:10:51

Let me just swing this.

1:10:53

Control C, control B, okay.

1:10:56

Ankit, what do you think I'll get?

1:10:59

Think about it.

1:11:00

If Chad GPT was calling a Python Ripple tool, imagine this is a Python Ripple tool.

1:11:08

So, yeah, I mean, you're right.

1:11:09

I mean, I'm actually showing the demo in Jupiter only, but that's not how it will be in the real world.

1:11:13

Real world, it will be some other application, right?

1:11:15

there there will be no Python.

1:11:17

You're calling the Python Rappel tool so that it can execute the code.

1:11:21

Now, chat GPT is sorry, Python, no, but people will give a query.

1:11:25

People will write something in text.

1:11:27

People will write a question in text format.

1:11:30

And chat GPD has to solve it.

1:11:32

It has to use Python and try to understand what is somebody asking.

1:11:38

So, so it will use the Ripple tool.

1:11:45

it will use the Python tool that will internally execute the code and it will return the results to you.

1:11:53

See, it has converted that to Python.

1:11:55

Got it?

1:11:56

I'm saying, this chat GPT internally is.

1:11:59

Now, what we are?

1:12:00

We're our thing, we're making.

1:12:02

That's a difference.

1:12:02

Chat GPT already is doing it.

1:12:05

And this is really cool.

1:12:05

You can edit be, you can see, you can run this.

1:12:10

So you can run this.

1:12:12

If you click on it, look, do you see?

1:12:14

The raffle is actually.

1:12:15

open.

1:12:17

So, and I think, I think, another very interesting thing that I want to talk about today is, now that we are

1:12:27

discussing agents as LLM plus tools and all this, these are also agents.

1:12:31

Whatever you are seeing on the screen, you know, chat GPT, chat GPT, heck yeah, the agent.

1:12:35

So, you know, I asked a question, this is a built-in agent.

1:12:39

Obviously, in our course, we are trying to build agents ourselves.

1:12:42

That is why we are using that programming environment.

1:12:44

but chat GPT is already a built-in agent.

1:12:47

So far we were just using chat GPT generally as a LLM.

1:12:50

But actually chat GPT is an agent, it is able to get things done.

1:12:54

Depending on what question you are asking, it is able to figure out what to do.

1:12:58

So what is intelligently figure out the right.

1:13:00

So what is happening is, see, I'm the client.

1:13:04

So let me add one more layer on top of it.

1:13:06

I'm the client.

1:13:08

The client is asking the question.

1:13:11

Client is asking the question.

1:13:14

The question will hit the manager, LLM.

1:13:17

This is the manager?

1:13:21

Internally, it will be a GPT model, right?

1:13:23

And the manager will reason.

1:13:25

Okay, whatever the customer has asked, how do I solve it?

1:13:28

Who, who, which guy can solve this?

1:13:31

Chad GPT also internally has multiple tools built into their system.

1:13:35

So they have a Python Ripple tool, something like a Python Ripple tool.

1:13:38

It has access to a Python Ripple guy.

1:13:44

it has access to a search tool internet search tool and this is the demo that we are

1:13:50

doing today but what I wanted to show is chat gpt exactly does this the chat gpt also is connected to these

1:13:55

two tools it has a rappel tool and it also has a search tool this is this combination is a system

1:14:01

is what we call the agent the next time you you you get a question the manager reasons what to do

1:14:05

which tool to call so based on whatever question is asked the manager is reasoning that okay we want to call

1:14:12

the python ripple tool we want to call this particular tool we want to call the python

1:14:17

ripple tool based on whatever question is asked the manager is reasoning we want to call the python

1:14:22

repel tool and the python repel tool is getting the job done for me if you ask a different

1:14:29

question let me show you on the same demo if you ask a different question okay if i ask a different

1:14:35

question if i say what is the capital of delhi

1:14:42

you can see react framework in action if i ask the question what is the capital of delhi which

1:14:46

tool is being used the search tool is being used actually not search honestly this is this is

1:14:51

relying on the models innate intelligence okay leave this out let's say what is the closing

1:14:57

what is the latest closing price of nifty if i asked this question it will use the search

1:15:08

tool it will use a search tool and it is it is it is it is it is it is it is it is it is it is it is it is it is

1:15:12

now figuring out the manager is able to figure out they for writers and all these sources

1:15:15

are being referred to yeah there was some make yeah here here

1:15:20

but depending on the question the client is asking the manager is reasoning

1:15:24

that now i need to call the search tool this is not a python guy's thing i need to

1:15:28

call the search tool the search tool will answer the question get me the results

1:15:34

and and this is the classic example of an agent next time you're using any kind of

1:15:39

this chat gpt or jemini any of these kinds of tools you know it's an agent behind the

1:15:44

things absolutely you can have uh huh chat gpt may built in there chat gpt has built in here chat

1:15:49

gpt has built in uh interpreters for everything so you can actually build one single agent

1:15:54

that has all the interpreters correct you can have it have that okay now moving on

1:16:09

let me remove this one wise so the really interesting part is that we are able to see something

1:16:25

that we will exactly build today that's an interesting part right so you know we'll be building

1:16:28

this exact same system today and you just got a sneak peek into how chat gpt is exactly doing it

1:16:34

that's a that's a really cool part okay

1:16:39

so now moving on ah so just to answer your question she just uh yeah so sonar cube

1:16:45

is something that you can you can read about you can actually read about you can

1:16:49

you can actually read about you know sonar cubes it gives an API then that is something that

1:16:54

can yeah it's a code analysis tool for multiple languages

1:16:58

okay something called sonar cube can read about it

1:17:05

okay automatic static port analysis platform used by developers

1:17:09

supports i think we need to see that it gives you what kind of mcp servers it gives you mcp

1:17:15

is another topic altogether but the best part is that you know it it it's a platform and just like

1:17:21

we are using python ripple and all you can instead use sonar cube so now users can ask a question

1:17:26

and they can use a sonar cube tool and that can analyze every language out there okay so so you can

1:17:32

read about it and when i come talk about mcp servers later he will relate to it how to integrate that as a

1:17:36

tool okay so just to answer your

1:17:39

question okay now moving on let us go back so we have defined the python

1:17:54

ripple tool programmatically this is what we have instantiated right now that's the python

1:17:58

ripple tool and now what i will do i will go and wrap it as a tool this is a something that you will

1:18:06

have to do as a syntax okay we just wrap it as a tool

1:18:09

so what have i done right now i've created the python ripple tool that's the python

1:18:13

ripple tool and if you you're giving it the name python underscore repel and you're asking it the

1:18:19

question a python shell and you're giving a very clear description this is what is very important

1:18:24

whenever you're instantiating tools in you know a tools in you know agents context you need to be

1:18:32

very very clear what these tools are capable of doing so that sort of you need to be very clear

1:18:38

about the context what these tools are capable of doing the context has to be very

1:18:43

clearly defined what the tools can do what the specific tools can do the context has to be

1:18:50

defined very far very clearly so we are explicitly uh instantiating the two tools here

1:18:57

the tool that we have defined is called python rebel and here i am giving a very clear

1:19:02

description of the tool remember a tool is the worker and what you are seeing on the screen right now

1:19:07

is the bio data of the worker that is one way to interpret the thing so what you are seeing

1:19:12

on the screen is like the biodata of the worker this is the bio data of the worker that you'll see

1:19:18

this is the worker's biodata okay so now uh moving on and this is important because this is

1:19:28

what the manager will refer to when the manager is trying to select which tool to call the manager

1:19:33

will refer to that okay so where are we right now we have defined the tool called pi can

1:19:37

we have described that tool and now we will simply invoke the tool and test

1:19:41

okay this is the way how you invoke the tool you have already discussed this right

1:19:47

similarly we will instantiate a tool called surper this is the same search tool that we are

1:19:52

that we are defining surper underscore search here we're

1:19:55

make our search tool

1:19:57

okay and the description we are also giving what this surfer tool will do

1:20:04

and now we will go

1:20:07

and test this tool see it is actually searching life from the internet who is the founder of

1:20:14

Tesla it is going and searching live from the internet and if you want to be absolutely

1:20:19

sure what it is doing are you can see exactly what it is doing then go back to the logs

1:20:25

for up log they go back to the digger that today it is the day is 11th of June

1:20:32

and you can see who is the founder of Tesla this query run over and how many credits are you

1:20:37

i got used up and how much of response time was taken search to you want to search

1:20:42

to work that means it went to the internet it searched that query and it actually returned that answer

1:20:46

to me it is actually getting locked in server also so where are we right now we have just

1:20:52

created two tools that's what the story is right now we have created a python ripple tool

1:20:57

that is my python guy let's say i'm the manager i've hired two people that's my python guy who

1:21:01

can do all the python work and i have a search guy if i want to go to the internet and search guy if i want to go to the

1:21:07

the internet and search something i'm a lazy person i'll ask my search person to go and go

1:21:11

and go to google and search please go to google and search this thing please tell me who is the founder

1:21:16

the search tool will answer it okay and now we will go and instantiate the agent

1:21:23

now we will go and instantiate the agent and this is a simple way how we can instantiate the agent

1:21:29

so what are the aspects so the first agent that i'm building is just a

1:21:37

python repel agent with only a single tool and the next one i will do is an agent with

1:21:44

two tools and what you are seeing on the screen right now is a very basic react agent and what is

1:21:51

an agent remember llm plus tools plus prompt prompt was the manager system message

1:22:00

so llm is the language model that we already created before tools is basically nothing but the

1:22:06

a repple tool whatever ripple tool that we have and prompt is the manager's system message

1:22:14

ah sure sure i will i will i will do that so sure absolutely uh so if you see

1:22:21

what is that amit uh ameth is a question sir if python underscore repel dot run

1:22:25

ah amit i get it i get it absolutely that's a good question it's a good question uh

1:22:29

it is a bit of a technicality inside lounge chain you got that right uh i think you you are wondering

1:22:34

so it felt a little repetitive so the first we test here then we're

1:22:38

you have to do it to build an agent you have to wrap it in a tool

1:22:41

so this is the this tool is coming from lanchine

1:22:45

lanchine is the high level library that we're you know using to do all this right

1:22:49

so you can see tool is imported from lanchine not agents so lankchain

1:22:53

land chain mandates it that you have to wrap it this way you have to

1:22:58

explicitly give it in this format you have to specify the name of the tool

1:23:02

and you have to specify the description

1:23:04

this is how we're making the search tool we have to give the name of the

1:23:09

tool the description that's it you have to do it this thing now we can build agents which can

1:23:15

call the tools what's that from xy thing what do you mean xy can you can you repeat ali from

1:23:27

where do you want me to repeat shall i shall i shall i just start from here is it okay are you are

1:23:31

okay with the tools right we created python rappel tool two

1:23:34

and we created a google search tool right i hope it's clear oh x plus y thing x plus

1:23:45

why was just a testing we were doing okay what did we do in the x plus y thing i can show you no problem

1:23:50

look at this so ali we wrote a command right we have a tool you agree we have a tool called python rebel

1:23:58

that's a tool that we actually created called python ripple

1:24:04

now what is the python raffle tool the python raffle tool is something that can take a python

1:24:10

code and can run the python code that is what a raffle is a raffle is like a runtime okay what is a

1:24:16

raffle a raffle is like a runtime they say colab is a runtime you can write a python code and it will

1:24:20

execute the code so similarly a python raffle is just an interactive runtime with runtime then

1:24:26

up you can enter any piece of code here and this runtime will execute that and return the result back to you

1:24:34

make sense are you with me this is all we are just we just we just created the tool and

1:24:40

we are simply testing the tool and the and where are we right now we are saying that hey we

1:24:47

have created two tools that we do two tools we have got the python ripple tool and we've

1:24:52

also got the search tool two tools are ready and now we will use these two tools and build an

1:24:56

agent so first agent we are building is using only the repell tool we are using the

1:25:04

tool and trying to build the agent let us see so there is the

1:25:09

reference tool that we are using and we are trying to build the agent so agent is

1:25:18

llm plus tools plus prompt and as amit rightly uh pined on chat this is the actual

1:25:25

link for the sample react prompt whatever i was talking about uh in the beginning of the class

1:25:30

if you remember i was mentioning about thought action observation and all that and i told you

1:25:34

that this entire react framework reason and act thought action observation this entire react

1:25:40

framework is explicitly given in the system message of your manager so whatever is your is your

1:25:47

manager's system message the react framework is explicitly uh mentioned in the system message

1:25:53

of your manager so this is the manager system message and you can see the react framework is

1:25:58

explicitly given question thought action observation this is the template okay as i told you today is our

1:26:03

first agent class. So it's just a template. But obviously, you know, as we go deeper into the

1:26:08

classes, we will write our own prompts. But this is the, this is the template we are using.

1:26:13

It's a very popular template. It's coming right from the official, uh, lanchain community,

1:26:17

official lanchain community. We are taking it from there. And if you are relating to this

1:26:22

code, he said your code, what is this up dot pull? This is nothing but we are, we are, you know,

1:26:27

we are simply using the prompt. Okay, how do we use it programmatically? We have, we have to go and

1:26:32

pull the prompt from this thing. That's it. This is all that we are doing. So we are simply

1:26:36

using this prompt. This is the prompt we are using. So what is the agent right now? LLM

1:26:44

plus tools, workers, plus the prompt. The manager prompt. Hey, what is the prompt to do,

1:26:53

Ali? Prompt is going to, it's a system message, right? I think we understand system message, right?

1:26:58

The system message is the one responsible for, uh,

1:27:02

you know, controlling the behavior of your manager. That's what the system message will

1:27:06

do, right? Make sense? So you're explicitly telling the manager what it can do and what it

1:27:12

cannot do. So that is what the system message is for. Of course, we will write them, but not

1:27:21

today. Today, I'm just trying to show you a default from the official blankchain community.

1:27:25

The most popular react from the planchain has given us. But of course, going forward, you have to go and

1:27:30

customize and write your own thoughts.

1:27:32

Okay. So, you know, some of the things we were discussing that this is what you can do. This is what you cannot do. But this is the general template. Everything that you do will be based on this template. Some of the things you will have to put exactly as it is. Like question, thought, action, input. This has to be similar. And then you add and add some more things on top of it, what it can do, what it can do, what it can't do, what it cannot do, what can connect to. Just like how we write a prompt. This is the template react prompt that you're seeing on the screen. Okay. Unket, I hope you're also clear, right?

1:28:02

Okay. Now, moving on. Now we have the sample query. This is the sample, you know, query that we have here. And now what we will do, based on the sample query, we want to execute this query. We want to go back and execute this query and we want to see the results. We want to execute the query and we want to effectively see the results. And it's very interesting. You know, I wanted to show the execution to you. Very interesting how it's going to work.

1:28:32

Right. You can take a look at it. This is the, this is the question I want to solve. If 450 amounts to $630 in six years, what will it amounts to in two years at the same interest rate?

1:28:46

If, if 630, you know, as you can imagine, it is a simple interest kind of problem, no, PRT by 100. We have seen that right. So, so user asks the question. So we have already built the agent.

1:28:59

Remember agent we have already been LLM plus tools plus prompt.

1:29:03

And now we want to test the agent with this particular quail.

1:29:08

If 450 amounts to $6.30 in six years, what will it amounts to?

1:29:17

What's that? Oh, oh.

1:29:22

Yeah. So we're just testing the agent, Sangita. Right now we just testing the agent. We have created the agent.

1:29:29

We created the agent here. Agent is nothing but LLM plus tools plus prompt.

1:29:34

We created the agent, right? And now we are simply trying to test the agent.

1:29:39

So you can follow on from here. We're just testing the agent. If I go and write this query and if I execute the query, and if I execute the query, you can see very interesting.

1:29:49

It will enter into the thought action observation look. Can you see? It's taking, it's still taking time.

1:29:53

It's still thinking, still thinking, still thinking, still thinking.

1:29:59

making a lot of syntax errors. And eventually it should be able to solve it.

1:30:06

Let's see. Nothing I'm doing. Okay. I'm just just given it to the LLN, the manager.

1:30:13

And it is the manager's responsibility to take my, to take my, to take my whatever question I've asked,

1:30:20

and it's the manager's responsibility to go and solve it. Okay. You can see. This is the thought action

1:30:29

observation syntax we are able to see. And let me just go and run this again. I think we ran the time limits here.

1:30:36

So very interesting. What is happening here is, if you, if you, if you take a look at it, it is, it is looking at the input, whatever input,

1:30:59

you have given and it is effectively trying to go through this entire thought action observation

1:31:04

sequence. So first it is thinking what we have to do. So we should calculate the interest

1:31:10

rate first. So based on the question, the manager is first reasoning. The manager is first reasoning

1:31:17

what it has to do. Thought. Then it is figuring out which tool to call. And in this demo we have only

1:31:23

one tool, which is only the referral tool that we have. So then the manager is going to call the

1:31:27

Rappel tool. So once it figures out that, okay, this is what we have to do. Now it

1:31:32

calls the Ripple tool. And this is the input to the Ripple tool. So the manager is the person

1:31:39

responsible for reading the client question. And based on the client question, the manager is

1:31:45

responsible for reasoning and giving it in the right format. This is a thought action observation

1:31:51

sequence. It is now calling the Ripple tool. The Ripple tool is giving some.

1:31:57

response and then on the basis of that the manager again is not happy

1:32:03

manager is again seeing that okay the response is not correct okay response is not

1:32:07

correct and based on that it is able to and finally it solved it 500 3.41 but it took a lot

1:32:12

of price actually the best part is that the react framework is able to figure out and I

1:32:17

wanted to show this this is syntax that are not from my end this is a syntax that are from the

1:32:20

agent's reasoning okay and I'm it to answer your question the agent is

1:32:24

selecting tools automatically how does it figure out

1:32:27

what's tool to call that magic is in the react framework. See, we are explicitly saying

1:32:31

the action to take should be one of the tool names. So the manager, so in this prompt,

1:32:38

the system message you will explicitly specify that based on the question, you look at the tool

1:32:43

description. Remember we created tool descriptions. So search tool, we have a description

1:32:47

and the Python repel tool will be a description. So when the manager gets the question from the

1:32:52

line, the manager will figure out which who is the right guy who can answer, solve,

1:32:57

problem. So that is the intelligence the manager has. Okay. So you can see we are

1:33:03

explicitly guiding it and the way to do that is you have to write the right from system message.

1:33:10

Correct. I mean, it's semantic search means the LLN is using its own intelligence. Exactly.

1:33:14

Okay. It's figuring out what to do and it's figuring out which tool to call. Exactly. You can think

1:33:18

of it like a semantic search. Correct. So the tool description is also like an embedding and

1:33:22

correct. I mean, that's the intuitive way how you can think about it.

1:33:27

But this is a really exciting part. When you look at that reasoning chain, it calls the Python

1:33:31

Ripple tool. And the Python Ripple tool is, you know, kind of not able to solve it. Again,

1:33:37

the manager calls the Python Ripple tool. Again, it gives syntax error. Again, it calls. This entire thing

1:33:41

it is doing within that reasoning sequence. So somewhere it is making mistakes, right?

1:33:47

Somewhere it is making mistakes. We have to calculate the rate of interest, right? If you see rate

1:33:51

of interest, you have to calculate PRT by 100. So what is the rate of interest? It's just a typical simple

1:33:56

interest component test problem.

1:33:57

and every time it is giving a syntax error.

1:34:01

And now automatically, here also syntax error.

1:34:04

Now the next time it calls the Rappel tool, it has figured out automatically.

1:34:07

It has resolved it.

1:34:09

And now we can see the interest rate is coming out as 5.7%.

1:34:13

And now that we have the interest rate, we can calculate the amount after two years.

1:34:18

So first you find the rate of interest and then you find out how much will the amount grow after two years.

1:34:22

So again, you call the Python Ripple tool.

1:34:24

This time you specify P, you specify the rate of interest.

1:34:27

specify number of years. We means the manager. The manager is the orchestration guy,

1:34:32

right? And the Python repel person will calculate, okay, the amount is going to be $503.41. All of what

1:34:41

you're seeing in green is the intermediate steps. This is the final answer that you will see at the

1:34:45

end. So when you're building a chat application, this is the kind of thing you will see. You will not

1:34:49

be seeing all that, you know, all this reasoning, thought action, observation. This is just for,

1:34:53

you know, I just wanted to show you this beautiful react in action.

1:34:57

I hope everybody is getting a feel for it.

1:35:01

So based on a particular question, how we are able to figure out what is the best tool to call it.

1:35:07

And the next demo is even more interesting because here what I've done, here I've basically used, I've used both the tools together.

1:35:17

The story remains the same.

1:35:19

What is an, what is an agent?

1:35:21

An agent is nothing but an agent is nothing but LLM plus tools plus prompt.

1:35:26

This time we have the language.

1:35:27

language model, the LLM, the manager.

1:35:30

These are the list of two tools that we have, the word purse, and the prompt is nothing but

1:35:34

the React prompt that we have here.

1:35:37

So we have the LLM, the tools and the prompt, the React prompt.

1:35:42

That's what we have right now. And this is the React agent.

1:35:47

And now we will try this out. This is very interesting. We are asking the question, what is the latest

1:35:52

stock price of NVIDIA? Help me calculate. It's actually quite a hard question.

1:35:57

It is quite a hard question, right?

1:36:00

Quite a difficult question.

1:36:01

What is the latest stock price of NBDR?

1:36:04

Please help me calculate if I had invested $100 a week back, how much money would I have today?

1:36:10

Right?

1:36:11

I think I'm asking a very difficult question to start with.

1:36:14

Let me make it a bit simpler.

1:36:16

Then I will come to this demo.

1:36:18

Let me make it a little simpler.

1:36:20

Let me say, let me say, instead.

1:36:27

What is the closing stock price of Nifty today?

1:36:39

This is the exact thing we did in chat GPD.

1:36:42

What will happen is behind the scenes when I hit enter, this is like the client asking the question, right?

1:36:48

This is like the client asking the question.

1:36:51

But the manager will reason which tool to call and the manager will reason.

1:36:57

Understand, I, to answer this question, I have to talk to the search tool.

1:37:01

So when I run the code, you will see the search tool is actually getting called.

1:37:04

Surfer search is getting called.

1:37:06

And surfer search is going to give you the right results.

1:37:08

It's running several queries.

1:37:10

Stock price today, 11 June, nifty closing, nifty, 50.

1:37:13

It's going to give you the right answer after the couple of search.

1:37:16

And it's able to tell you that the final, the final closing stock price is coming out to be this.

1:37:25

It is eventually giving you the right answer.

1:37:26

It's still reasoning. The manager wants to be very sure, right?

1:37:29

Because based on the question the manager is thinking, okay, I will give it to my search tool.

1:37:34

And this is the final result of the search tool.

1:37:36

The closing stock prices, so and so.

1:37:39

Beautiful.

1:37:40

So this is the, you know, that beautiful thought, action, observation, chain, in action.

1:37:45

Every time you ask the question, it, it selects a search tool.

1:37:49

It is able to intelligently select that tool.

1:37:51

Remember, my agent right now has two tools.

1:37:54

Now, depending on the question I'm asking, it is.

1:37:56

is able to select the search tool, search tool, search tool, search tool for search.

1:38:02

Okay.

1:38:03

You want you, you want to see another example, interesting example.

1:38:07

So let me in the same example, go and ask something else.

1:38:15

Let me go and ask, okay?

1:38:17

Let me go and ask something else.

1:38:18

This time I will ask, I will go and ask a Python query.

1:38:26

So I will pretty much go and ask the same question, right?

1:38:37

This is the same question I can go and ask, right?

1:38:40

And we call the Python Ripple 2.

1:38:42

If you go and do that, it will call the same Python Ripple 2.

1:38:46

And now this is that more advanced question I asked here, if you see,

1:38:51

what is the latest stock price of NVIDA?

1:38:54

So, please help me calculate, if I invested $100 a week back, how much money would I have today?

1:39:05

This is a difficult question.

1:39:07

It has to do two things.

1:39:09

First, it has to go and access the search tool.

1:39:12

It has to get me what is the latest stock price of Nvidia today.

1:39:16

Then it has to go back to one week back, understand what was the Nvidia stock price then.

1:39:23

And with respect to what was the Nvidia stock price then.

1:39:23

And with respect to that, it has to calculate if I invested 100, how much will I get to this?

1:39:27

Quite a complex one.

1:39:28

And as you can imagine, the manager is the person doing all the orchestration.

1:39:31

I'm only writing a statement in English in front of you.

1:39:34

But the manager is able to look at this query and it is able to figure out that, hey, first I have to use the search tool to get the NVIDIA stock price.

1:39:43

And then I will use the Python Drepl tool to do the actual calculation.

1:39:47

That's the magic of agents.

1:39:50

I mean, I will once again run this code.

1:39:52

You can see that thought actually.

1:39:53

observation sequence playing out.

1:39:56

See, first action is surfer search.

1:39:58

What is NVIDIA's current stock price?

1:40:01

Then it's trying to find out NVIDIA's historical stock price.

1:40:04

And based on that it will try to figure out last week's stock price.

1:40:07

And now what it does, very interesting, it is calling the Python Ripple tool.

1:40:12

Now it is calling the Python Ripple tool.

1:40:16

Now based on the Python, it's still running actually.

1:40:19

It's still running.

1:40:21

Let us see.

1:40:23

The interesting part will be to look at that React framework and get a sense of as to what is happening.

1:40:32

Again, the syntax error, it is writing this entire thing by itself.

1:40:36

The Python Ripple tool is writing.

1:40:37

Remember, it called the Python Ripple tool, because that's my Python guy.

1:40:40

The Python guy will write the syntax, but it's made a mistake.

1:40:43

So manager figures out.

1:40:44

It's a mistake.

1:40:45

So it will again autocorrect.

1:40:47

Again, it makes a mistake, autocorrect.

1:40:48

It will keep doing this over and over again until it is able to completely answer my question.

1:40:53

That's a really cool part of what agents.

1:40:55

And as a developer, how do you go back and manage this process?

1:41:00

You can go back and manage this process using the system message.

1:41:03

You can explicitly control this entire process using the system message.

1:41:09

Okay, that's the intuition.

1:41:12

That is a good question.

1:41:13

That is a good question.

1:41:14

We've actually hit the maximum number of rate limit.

1:41:16

Actually, that's the problem.

1:41:17

Can you see?

1:41:18

I think that's no issue that we are facing.

1:41:21

The rate limit reached in the organization.

1:41:23

Okay.

1:41:24

So that's the reason why it actually stopped here.

1:41:28

But yes, Prangel, that's a very good question.

1:41:30

You can give a stopping criteria.

1:41:32

And this is one other thing I want to talk about in agents.

1:41:34

Agents can use up a lot of tokens.

1:41:36

So the moment you're in the world of agents right now,

1:41:38

please remember that they can use up a tremendous number of tokens.

1:41:42

And if you see that, you know, one of your language models are kind of gone,

1:41:46

you will have to go back and use another language model.

1:41:49

Okay.

1:41:51

So I think here I have used my list.

1:41:52

I have used of my tokens per day quota.

1:41:55

I will have to go and explicitly use a different model.

1:42:00

But I think, I think, again, you can execute this one later,

1:42:04

but just wanted to share, share with all of you.

1:42:06

This is that rate limit, can you see?

1:42:08

It says rate limit reached, per day limit reached.

1:42:13

And, but before that error happened, it was able to beautifully go ahead and do exactly what we expected.

1:42:21

It was doing a service.

1:42:22

search. It was trying to find the NVIDIA stock price first. So manager got the question.

1:42:26

It figured out I have to use the search tool. Then manager figured out I have to use the historical

1:42:31

Nvidia stock price. What was it last week? And then it calls the Python Repple tool

1:42:36

to do all the math. At least, I and invested 100 last week. What was the stock price then?

1:42:42

And now what, how much is the 100% grow today? That's intuition. Okay.

1:42:49

Ah, absolutely. Absolutely. Absolutely. So, um, absolutely. So, um, absolutely. So, um,

1:42:52

Amit, you can, you can opt to see the output, uh, however way you want.

1:42:56

If you see response output, then you'll be able to see that whole thing.

1:42:59

And this is obviously for developers, but definitely for, uh, you know, like in a real world

1:43:03

scenario, when you're building a application, like let's say you want to build a front-end application,

1:43:08

then obviously these kinds of things we will not show.

1:43:10

Then the only the last part is what you'll be showing.

1:43:13

But this is very, very useful because as we were discussing, oftentimes agents can do incorrect things.

1:43:17

So debugging agents is very important.

1:43:19

So as a developer is not just, you know, building an agent.

1:43:22

But a big part about generative AI and these kinds of applications is how do you monitor it?

1:43:28

How do you monitor these systems to ensure they are doing the right thing?

1:43:31

Okay.

1:43:31

Yeah.

1:43:33

And this is also a very good question from Pranjan.

1:43:35

Pranjal asks a question.

1:43:36

How does it know when to stop the loop?

1:43:38

Very good question.

1:43:39

Or sometimes we have a hard stop right idea because otherwise the reasoning can continue happening, happening, happening.

1:43:45

So in fact, in the, in the framework that we are using right now, Prangel, there's a particular argument called max iterations.

1:43:51

So we can use.

1:43:52

use something called max iterations. And just like we were doing in the last session,

1:43:56

if you remember max stops. So we can use something called max iterations or max stops to ensure

1:44:01

that that thought action observation loop is doing maximum this many times. Otherwise, what will

1:44:05

happen? Otherwise, I will end up with these kinds of issues. You will end up your tokens.

1:44:09

And tokens can be very costly. Here we are using grok. But in reality, you know, you can end up

1:44:15

getting charged a lot of money. It can be very costly. Okay. I hope this answers your question.

1:44:22

Okay, okay. Great questions, guys. All right. So just to summarize the idea of agents here,

1:44:31

I hope everybody's clear. So we can take a break right now. There's a lot of so many things we are talking about today.

1:44:35

So yeah. So we'll just circle back from the break and recap the journey once again. So let's take a quick five minutes or ten minutes here. And we'll circle back after five minutes.

1:44:52

Yeah, we can do that. We can do that. So Ali, so Ali, what I did was, uh, Lama was actually a more powerful model, but absolutely. I mean, now that I'm seeing that Lama is, the limits are getting over, we can absolutely shift to Jemma. You can use the Jemma model, which has very liberal token limits.

1:45:16

Absolutely, you can do that. Absolutely. Try it out. Yeah.

1:45:22

Thank you.

1:45:52

Thank you.

1:46:22

Thank you.

1:46:52

Thank you.

1:47:22

Thank you.

1:47:52

Thank you.

1:48:22

Thank you.

1:48:52

Thank you.

1:49:22

Thank you.

1:49:52

Thank you

1:50:22

Thank you

1:50:52

Thank you

1:51:22

Thank you

1:51:52

Thank you

1:52:22

Thank you

1:52:52

Thank you

1:53:22

Thank you

1:53:52

Thank you

1:54:22

Thank you

1:54:52

Thank you

1:55:22

Thank you

1:58:22

Okay,

1:58:26

So welcome back, welcome back, welcome back, welcome back, we'll be

1:58:29

Okay, so welcome back, we'll be starting on here, we will be starting on here.

1:58:44

And so we have managed to we have managed to complete this, we have managed to complete this, uh, this very

1:58:52

interesting demo where we were able to see

1:58:56

framework in action. Okay? So hope everybody is clear with how the how the agent is inherently

1:59:03

working behind the behind the scene. So we are able to see how the how the agent is specifically working.

1:59:11

So depending on whatever question you're asking, the React agent is able to figure out which tool to call

1:59:17

and based on that it is able to give the answer. Okay. So just to summarize the entire conversation, just to take you to

1:59:26

the, the whole flow. What did we, what did we basically do in the, in the session? So, so we, we, we, we created mainly two tools, right?

1:59:36

We have the Rappel tool and we had the circle search tool. These are the two main tools that we have.

1:59:41

Okay. And all that we are trying to do now is we are trying to build a, you know, a React agent, which is going to be able to talk to these tools.

1:59:54

Okay.

1:59:54

that is what we looked at. Okay. What is the paradigm and what is the framework that agents are using?

2:0:02

It is using the React framework and React framework and React stands for reason and action.

2:0:08

Okay. And we saw that thought action observation chain. So next time you ask the question, the agent is

2:0:13

first going to reason what to do next. Then it will figure out what is the tool it has to use.

2:0:21

then it will get the tool output and then it will keep repeating the thought action

2:0:30

observation multiple times and eventually it will give the final answer.

2:0:37

Ah, Ripple, Rappel tool nothing, well, Ali, Ripple is nothing but a runtime.

2:0:42

What is the Rappel tool? So, Raffle tool is nothing but a runtime. It's a Python runtime.

2:0:49

So, Ali, this is the Python Rappel tool.

2:0:51

I think the description will help you understand exactly what this tool does. Can you see?

2:0:55

It is a Python shell that is used to execute Python commands. So if you give it a, so that is what the Ripple

2:1:05

tool is doing. If you give it a valid Python command, the Rappel tool will execute that Python

2:1:11

command. Ah, so the calculations were also given in Python. Same exercise we also did here. If you see,

2:1:19

If I'm giving a particular thing in Python, this is exactly how I will write it in Python, right?

2:1:25

The Rappel tool will execute the results in Python.

2:1:30

Calculations be if you see the calculations also, Ali, if you're referring back to the calculations, how it did.

2:1:35

Same thing. So the Rappel tool, what will the Ripple tool see as the input?

2:1:41

The Rappel tool will see this as the input. Can you see import math dot, import math, given this, this, this is what the Rappel tool will see.

2:1:49

This is the input for the rebel tool.

2:1:53

And based on that, it is simply executing that and giving the answer.

2:1:59

Okay.

2:2:04

Are you clear, Ali? Are you absolutely clear what is going on?

2:2:09

It is just a Python code that you're giving it.

2:2:12

And I'm repeating, this is not the code that you are writing.

2:2:14

This is the code that the LLM is writing.

2:2:16

The manager is writing for you, right?

2:2:18

You are only describing.

2:2:19

what is the problem you are trying to solve, right? You are writing the problem that you are

2:2:24

trying to solve. Now, absolutely, absolutely, okay. That is right, what you say. Both will be done in

2:2:28

Python, absolutely. You are only writing the question in English. This is the client asking the question.

2:2:34

The client will ask the question to the manager. LLM is the person who will reason. LLM is the person

2:2:39

who is responsible for understanding the question and converting that into the action input and figuring out

2:2:46

what tool to assign the work to. So the LLM will.

2:2:49

now assign that work to the Python repel tool, the Python Rappel worker. And remember that

2:2:56

worker will accept the input in a certain format. The worker will not be able to understand other formats.

2:3:01

There is a very specific kind of format the worker will understand. So you will have to also give

2:3:05

the input to the Rappel tool in a very specific format. That's the intuition. So there is a very specific

2:3:12

format in which you will have to give that input as well. And that is exactly what the manager is doing.

2:3:19

The manager is understanding the client question.

2:3:21

It is able to figure out to solve that problem, which tool to call.

2:3:25

And it is also able to frame that Python query.

2:3:29

And it is able to give to that Python Ripple tool.

2:3:32

Now, why is the mistake made?

2:3:34

The mistake is made because the manager framed the query wrong.

2:3:37

If Python syntax error, there is a syntax error in this particular Python query,

2:3:41

whatever be, then maybe there may be some string is.

2:3:45

Then again, the manager tries to correct.

2:3:48

Manager is trying to correct.

2:3:49

Guys, now you run this command against syntax error.

2:3:52

And it keeps doing this many, many times.

2:3:54

And finally, finally, the manager is able to get the right input to the Rappel tool.

2:4:01

Abiwo, as a input, their Rappel code.

2:4:05

See, all this file, it was coming in this triple quotes.

2:4:07

Can you see if it was coming in these triple quotes, the backtakes?

2:4:10

This was causing the syntax error.

2:4:13

This was not a valid Python command.

2:4:14

That is the reason why it was getting syntax error.

2:4:16

But this action input is what the manager is creating.

2:4:19

And now finally the manager says, okay, now you solve this.

2:4:24

The Python repel will now execute this and it is giving the answer.

2:4:29

Fine, I hope this is absolutely clear.

2:4:31

This is the internal thought process of the React agent, how it is working behind the scenes.

2:4:36

Okay, Ankit, I hope you are clear, convinced, yeah.

2:4:42

Ah, you can, you can give both. That's right.

2:4:45

So this is the thing. Reasoning, reason what to do.

2:4:48

Figure out what is the two.

2:4:49

name, get the input and hot action observation many, many, many, many times until you get the final

2:4:57

answer. And that is the way the React framework actually works out. This is exactly what we discussed

2:5:02

here. And then obviously, as part of the journey, we did the setup. We used land chain to make things

2:5:08

very simple. We use built-in tools today. Two built-in tools we used, Python, Ripple, and Serper,

2:5:14

Google Surper. These are the two tools we may be used today. But going forward, we will create our own

2:5:19

own tools. Today we used these two built-in line chain tools. But going forward,

2:5:24

we will create our own tools. And it is very simple to create a tool. A tool is nothing

2:5:30

but a Python function. Going forward, when we go and create our own tools, we will simply write functions

2:5:35

ourselves. Here we are not doing that. Here we are just using a built-in library, but we can also

2:5:40

create our own tools. So this is how the snippet looks like. We already discussed this. We're

2:5:45

creating the Python Repple tool. And this is how we are using the search.

2:5:49

tool. Remember, it is very important to give a proper description. Because this is like the

2:5:54

bio data of the worker. A tool is nothing but the worker, right? You have to give the bio data of the

2:5:58

worker, what the worker can do, what the worker cannot do. That's the intuition. So that's the

2:6:05

basic idea how to invoke the tool, how to build the tool and finally that React agent.

2:6:13

Okay, React agent is nothing but LLM plus tools plus prompt. So this is the final piece of what we talk

2:6:19

And what was the final demo that we did? The final demo was where we used multiple

2:6:24

tools. So this was the React agent where there were multiple tools that we used. Search tool and

2:6:29

Rappel tool both. So now you have the LLM that has two tools. And based on the question,

2:6:35

it is able to intelligently think which tool to call. So if you're asking it a search related

2:6:40

question, it will call the search tool. If you ask it a Ripple related question, it will call the

2:6:44

Ripple tool. And that's the way how it is working.

2:6:49

I hope everybody is aligned. Everybody understood the idea of what is going on. What is agent and all that? Any questions else? I hope everybody's clear. And you know, going forward, the interesting part is going forward, we will also be using Rags as a tool. Whatever

2:7:07

rag we have discussed over the last four, five sessions, whatever rag we discussed, even that rag will be a tool going forward. So we will use the rag as a tool going forward. So that is the

2:7:18

interesting part.

2:7:22

One query, when we pull the template from Lanksmith, we still need description to mention.

2:7:27

No, no, no, no, no. Lankspit is already a built-in built-in. So when you say hub dot pull, this one,

2:7:34

when you say hub dot pull 870 React, when you do that, this is already a prompt, this is the prompt

2:7:40

that you're pulling. So what is this thing? What is this from? This is like a prompt template. This is

2:7:44

a complete prompt template. You are using that prompt template. You can, of course,

2:7:48

you can go and you can make your own edits. This is like a system message for your LLMunkins,

2:7:54

got it? You don't have to describe this. So if you see my code, I am simply specifying prompt equal to

2:8:02

react prompt. So whatever I pulled in here, that's a React prompt, and I'm simply specifying this.

2:8:06

But in a more real scenario, as we do the exercises in the more advanced modules, we will write our

2:8:11

own React prompt because this is where we will specify the guardrails, the constraints,

2:8:15

what the agent can do, cannot do, all these kinds of things. Okay.

2:8:18

this is where you will specify all those factors.

2:8:27

Ah, absolutely, okay. Yes, yes, uh, tool description must be proper to answer your question.

2:8:32

Absolutely. This is what I meant, okay. How are we creating the tool? This is how we are creating the

2:8:36

tool. You use the tool plus wrap it in brackets. Give the name of the tool. Give the description of the

2:8:42

tool. This is what I meant. So when I said description, description will go here.

2:8:47

Okay. I hope I hope.

2:8:48

it is clear. So you have to describe the tool correctly because if the tool is not described

2:8:54

correctly, and one of you asked me this question before, sir, how does the manager know, the LLN know

2:8:59

which tool to call it? It is through the description. Otherwise, how will the LLN know, right? LLM will know

2:9:04

which tool to call based on the description that you're doing. So the, so it is like saying the manager

2:9:09

should know what you, you know, your bio data, your CV, what you can do, what you cannot do. So your biotas

2:9:14

should be very clear. It should be very detailed.

2:9:15

for it and uh ali absolutely i mean what you are saying is right but that is exactly whether

2:9:23

like there is nothing much we can do about it that is that is the that is a cost that you will have to

2:9:27

accept so rag and other tools will be using a lot of tokens and that is the reality and yes very

2:9:34

important giving the wrong description can lead to the wrong tool being called or the tool may not

2:9:38

be called absolutely getting the description right is very important see uh uh

2:9:42

the example i like to give is let's see you're a worker but you in your cb you say i can sing

2:9:47

dance you know you're giving a different you know this bit biodata so if the manager sees that if the manager

2:9:53

gets some requests they will say okay unkidq you please sing but that is not what uncit does right so if your

2:9:57

biotta is wrong if your description is wrong then for the wrong thing the manager will call that tool

2:10:03

and the tool will give the wrong answer that's the analogy again whenever you think of agents

2:10:08

try to you know try to think of that manager worker analogy okay

2:10:12

yeah but your point is right whatever you say the tool may not be called correct

2:10:21

what is that how the code will uh sanghita has asked a question how the code will work if it

2:10:25

it is all depending on the prompts to give and then we get the calling correct yeah absolutely

2:10:30

absolutely everything ultimately depends sangita on the quality of the prompt absolutely

2:10:36

whatever prompt you're giving and and i think you know some of the things like like like yeah

2:10:42

exactly that is something that you have to make your um correct this is this is completely

2:10:47

domain knowledge ali like how do we make the description perfect like there is no general answer

2:10:52

to it you have to you have to just use your domain knowledge and you have to mention this in a

2:10:58

correct way you know how have we written prompts before if you go back to the prior sessions

2:11:02

how did we write a system message how did we write user message how did we write

2:11:05

forms before got it so we have to we have to iterate and we have to you know we have to

2:11:10

get it right think of it that way so so it is your system uncle you are building it right

2:11:16

if you're building it you will have to describe it yourself think of it this way ah

2:11:20

that's correct you can use jemini that's different but my thing is correct and that is actually

2:11:26

our right thing also you can use jemini to help you create a good description

2:11:30

right thank you sankeith are you clear

2:11:35

absolutely clear what it is we will get our own tools absolutely and you are absolutely

2:11:45

right we will create our own tools but yeah i mean it's that's what we will do and a tool is nothing

2:11:50

but a function and we will see in the further sessions we will create our own tools but the

2:11:55

framework will be the same the only thing that we change is this is we're doing here we will not

2:12:00

import this tool by default this in this in this under a function down then we'll

2:12:05

and now that you can create a function now that so a python function will become a tool

2:12:10

going forward or that function can't that you can do anything and that is why tools are so powerful

2:12:15

there's nothing that you cannot do inside a tool okay right now we're just using a lankchain default

2:12:19

right to search or python repel today's topic because today's focus was more on introducing

2:12:25

what is an agent so that you understand that react and you understand the framework how the agent is able

2:12:30

to call the tool but going forward our python

2:12:35

functions will become tools we will write our own python functions and they will you know

2:12:40

basically be tools very good any other questions guys absolutely clear and you know this is very

2:12:55

interesting and just wanted to take a go to germany i think i might have shown this before but

2:12:59

since we are discussing about agents today it'll be so nice to show you in jemini

2:13:05

is also an agent if i ask the question what is the capital of india so jemini also is an

2:13:13

agent that is connected to multiple tools if i ask this question jemini will know that to answer

2:13:19

this question i can just uh answer the question as it is fact retrieval i can answer it from my

2:13:27

own internal memory next i ask the question what is the what is the closing

2:13:35

what is the closing uh stock price of nvdia today if i go and ask that question this time

2:13:50

the jemini will reason i have to call the search tool i have to call google search which is

2:13:54

integrated inside jemini it is searching the web can you see it is searching the web this is a tool call

2:13:58

it is doing a tool call and based on that it is giving the answer so based on whatever question you're

2:14:03

asking it is able to smartly figure

2:14:05

what tool to call this is a live example of an agent and let me show you something even more

2:14:10

interesting what are the top finance what are the top finance emails i have received now very

2:14:25

interesting i am just asking a simple text based question i am asking sending the question to the

2:14:30

manager manager will reason hey what is my client asking asking

2:14:35

and to answer that question who is the best guy who can answer this question and the manager

2:14:39

will assign that uh task to the best guy and who is the person who can answer this question well google

2:14:44

workspace tool you will see very interesting it will actually connect to my gmail it is connecting to

2:14:49

gmail it is connecting to what is actually connecting to gmail personal context is connecting to my

2:14:55

google workspace and gmail and based on that it's going to answer that question it is doing a tool call

2:14:59

so in the same in the same uh interface i gave three

2:15:05

different i did three different tool calls jeming is a built-in agent so these are actually you know

2:15:12

real real emails i received these are real emails i tr and you know some payments and all these are

2:15:20

are real emails are received okay and then i can ask another question show me see this is that

2:15:27

this is the slide i'm presenting right i think this is a different account but i can show me the

2:15:35

i don't think i've got uploaded there let me think what can i show you so show me the

2:15:42

uh so i'm just thinking of a ppt where i'm just thinking of a ppt where i have talked about i have talked about i have talked about

2:16:05

the basics of cnn and explained about the missing spatial context now guys this is a

2:16:21

different topic don't worry what is a cnn and all again i'm asking the question the agent the jimini agent

2:16:26

is figuring out to answer that question what tool it has to call and it will call the google workspace tool

2:16:31

tool now he's what call can you connect to my google workspace can you see connecting to

2:16:37

google workspace it is figured out that it is the access to the workspace tool and now from the

2:16:42

workspace tool who that ppt utah leah there here here content and you answer to how incredible this is

2:16:48

so all of a sudden we don't just have a we don't just have a we don't just have a ln that is able to

2:16:56

hear a question and give a response but the language model is able to look at the question and reason

2:17:00

what it has to do use the right tool and answer it and that's why it's so powerful

2:17:08

it analyzes immediately and then uh this is this is this is the same react framework that is

2:17:16

going on behind the since the manager gave me the final answer only after thinking

2:17:21

see this is that cn and basics and can you see this is this is the actual ppt this is the actual ppt

2:17:26

can you see this is also giving me the link to the ppt from where it has given me the

2:17:30

that given that thing so i'm the client asking the question manager called the workspace tool

2:17:38

it got the ppt manager is giving me a refined answer and i can go back to that ppt i can click on the

2:17:42

link it will open up that ppt and my google drive drive dot google.com you can see this is the real

2:17:47

ppt i'm seeing and in that ppt you're able to see the exact things i talked about convolution

2:17:52

neural networks and all is what i actually covered in that ppt that's a different topic but it's quite

2:17:56

incredible how it's able to give me the live link to my google drive

2:18:00

that's the intuition okay sankeith i hope you are clear uh okay absolutely anjohn

2:18:14

absolutely you will give the smart brain to use our functions exactly that is what we will do

2:18:19

in the real world we will write our own uh we will we will we will go and write our own tools exactly

2:18:26

and uh you know she just has asked a question she just to answer your question uh yeah absolutely

2:18:30

i mean she just to answer your question a react agent is just a reasoning policy

2:18:34

it decides the thought action observation input but react agent executor is the runtime wrapper

2:18:41

that actually runs the loop if you look at it from a code perspective uh this is the actual

2:18:46

executor this is the agent you're building this is this is part of how you have to do it she just

2:18:49

i think part of it is just the syntax but this is where you're just building the agent you are saying okay

2:18:54

this is the agent but this is the actual executor that you're creating

2:18:57

ultimately when you come to the code this executor is what you're

2:19:00

invoking okay i hope this answers the question but i think part of it is just the you know the

2:19:04

library that you're using and this is the way you're to do it is a syntax think of it that good okay

2:19:10

i hope that answers for you okay okay

2:19:20

ah absolutely you can use two more tools in the same request absolutely and maybe i can ask

2:19:25

questions about yeah i can ask questions about other things like photos

2:19:30

and all those things also i can do that okay in the same thing i can ask for some other relevant

2:19:36

examples of that yes yeah so how did you add user input where is that here no this is nothing

2:19:43

i just you just use the same code it will it will create it'll create if you write it this way the

2:19:48

user input will be you know this is how it is you just you just put it in collab it'll yeah it will come

2:19:55

it will come just use the same code as it is it will come okay use the same code as it is it will come

2:20:00

i did not explicitly do it myself but you just add use the same code and it will create that input

2:20:07

because you're accepting user input right yeah yeah it's it's more of a jemini specific thing but yeah

2:20:15

yeah but yeah all right when you whenever you do it this way hash and at the rate that's how it looks at it okay

2:20:29

yeah but we are not

2:20:30

explicitly creating this interface and you can do this in gradio also by the way it doesn't you

2:20:35

don't have to do it here you can do it with gradio also your gradio and streamlet is what we have used

2:20:39

in our sessions so you can use that as well by the way okay yeah okay great if we already

2:20:48

have powerful tools so of course i mean we are trying to build our own tool but definitely

2:20:57

germany is a very general purpose tool ali

2:21:00

but what we are trying to do is we are trying to create something more specific to our

2:21:04

use cases where jemini's general purpose it is connecting to google drive google maps google search

2:21:09

but think about an enterprise think about a real enterprise now you will have a requirement to

2:21:14

connect to multiple tools multiple external tools you might have a requirement to connect to

2:21:19

a database you might have a requirement to connect to excel uh csb you might have a requirement

2:21:24

to connect to other external tools in your enterprise that is the use case we are trying to build our

2:21:29

own custom tools Gemini is a built-in agent right but we are trying to build our own agents

2:21:34

in our field of work okay so you have to understand your business you have to let's say i

2:21:40

csa bank i ssa bank might decide tomorrow that hey we want to create an agent for our customers

2:21:46

so customers can go to icasa bank.com they can log in internal banking and they can talk to the chat

2:21:52

agent and the chat agent will automatically get things done so if you say start transfer money to

2:21:59

able to so we already have some of those features at a very basic level but we can make it

2:22:03

more advanced with the tool integration in different companies we are trying to create our own tools and

2:22:08

i hope that answers the question for me okay great so any other questions guys so a lot of

2:22:16

lot of questions from everybody great to see great to see people were so excited to learn about agents

2:22:22

today of course and yeah i have shared the

2:22:29

the contents in the drive link okay and again just to summarize the

2:22:34

summarize the context of what we what we talked about today today the main agenda of the

2:22:41

session was we looked at what agents are specifically what are agents

2:22:48

and we understood the react framework what the react framework is okay we understood

2:22:54

the concept of how to build a react agent and from there we were able to see

2:22:59

a very small demo in terms of how we were able to use the react agent and call make calls

2:23:05

to the two tools so this is how we uh base the session today okay all right guys uh

2:23:15

yeah thank you so much guys uh and we will uh in fact there was just one last thing i wanted to show

2:23:21

you i don't know if you guys know this in jemine there's a very nice feature see i already asked

2:23:26

several questions capital of india was a generic question

2:23:29

here it called the search tool here it called the uh google mail tool here it called the

2:23:36

workspace tool and here it will call the google photos tool you can ask the question show me the top

2:23:43

uh pictures i took from right related to mountains i think i've taken a lot of mountain

2:23:54

pictures let's see if it's able to answer general question but based on the

2:23:59

question the agent should be able to reason that i'm asking a question about uh retrieving

2:24:06

information from google photos so can it uh actually this is a typo i hopefully it'll correct it

2:24:13

let's see it should be able to connect to my uh google photos account and it and it see it's actually

2:24:21

given the right answer these are all my images these are all my images can you see so it has it has

2:24:27

it has connected to my google photos the agent has figured out that i'm asking a question

2:24:31

related to photos it has connected to photos and it is able to answer that question so very

2:24:36

recently uh so jemini has integrated google photos integration also which you are able to see

2:24:43

how come we will know the pre-existing tools list in the code uh in the code in the code

2:24:47

you will have to define you will have to define you you so here if you see unket we are defining the agent

2:24:53

has what tools not pre-existing we are building our own agent

2:24:57

okay we are building it right who created the agent we only bid it our agent right now has two tools

2:25:04

the people at germany built their own agent they have their own set of tools so we will of course know that

2:25:10

from this particular line of code right tools equal to whatever list of tools you provide you can have

2:25:14

two tools you can have 100 tools like you were asking one of you were asking okay uh

2:25:18

like anchich was asking can i have two more tools yes you can have two one you can have two

2:25:21

two comma something comma you can add the list of tools in the after comma okay

2:25:27

okay great okay guys we will have to put a stop to the discussion today great to introduce

2:25:35

agents today and we will continue on and obviously this is the start there's so much to talk about

2:25:39

there's so many more classes to go so we will continue on and i hope this uh gave you a very nice

2:25:45

sneak peek into the world of agents what it is and what agents are about and from here we

2:25:51

will be like i will hand it over to archita thank you everybody uh good night have a good night have a

2:25:57

great week weekend ahead and i will see you in the session next week yeah thank you thank you everybody

2:26:13

students the poll is live you can take some time fill that in we will start with the quiz shortly meanwhile

2:26:21

you can also try running the code that was shared for today's session

2:26:27

Thank you.

2:26:57

Thank you.

2:26:59

Thank you.

2:27:29

Thank you.

2:27:59

Thank you.

2:28:29

Thank you.

2:28:59

Okay, let us start with the quiz now.

2:29:17

Let us start with the quiz now.

2:29:19

Here's the first question of the day.

2:29:29

Why do we describe tools in a schema format?

2:29:36

That is correct to help the model

2:29:50

and use the tool correctly.

2:29:55

Second question.

2:29:58

What must be done before an agent can use a tool?

2:30:04

Correct, we must register the tool and bind it to the agent or the executor.

2:30:28

Third question, what is the correct order in the model tool execution cycle?

2:30:58

Correct.

2:30:59

It is proposed call, run function and return result to the model.

2:31:11

We can have multiple iterations but the flow remains the same.

2:31:17

After a tool executes, what should happen next?

2:31:27

Correct. The result is fed back to the model.

2:31:44

Final question of the day.

2:31:52

What is the main purpose of function?

2:31:55

in agents.

2:31:59

That is correct. The main purpose is to enable agents to invoke tools using structured arguments and results.

2:32:22

Let's look at the leader board now.

2:32:24

Now.

2:32:31

Very close win but Man Simran is the winner for today.

2:32:38

So congratulations.

2:32:40

I hope all of you have filled the pool.

2:32:45

Yes, I see 100% participation.

2:32:47

So thank you guys.

2:32:49

We will end the session here.

2:32:51

I hope you all have a good night.