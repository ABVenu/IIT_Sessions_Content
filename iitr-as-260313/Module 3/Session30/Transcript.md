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

Thank you.

4:30

Thank you

5:00

Thank you

5:30

Thank you

5:32

Thank you

5:34

Thank you

5:36

Thank you

5:38

Thank you

5:40

Thank you

5:42

Thank you

5:44

Thank you

5:46

Thank you

5:48

Thank you.

6:18

Thank you.

6:48

Thank you.

7:18

Thank you.

7:48

Yeah, guys, we can do it for everyone to join, then we can start.

8:02

My thing the voice is clear to everyone, right?

8:04

Can you help me?

8:05

I have already uploaded the notes of today's Lasas as well as well as the program.

8:11

So if you see here, probably another section of notes are already attached.

8:17

I've updated the PPD also.

8:19

We can wait for the late 5 for folks to join and then we can start.

8:22

I think the voice is clear and sharp, right?

8:24

You can hear me as well.

8:27

Today we will just try to make an announcement on the last session that we were having.

8:32

We will try to discuss the memory part that is there.

8:34

So yeah, we can wait for other folks to join and then we can start.

8:47

Thank you.

9:17

Thank you.

9:47

I think you will see me as well.

9:55

Let's wait I think two minutes at max and when we can start and we can do.

10:17

Thank you.

10:47

Thank you.

11:17

So P Puraze, like, are you not able to open get up.

11:34

Are you not able to open GitHub up?

11:38

Like if you see my current screen.

11:42

Are you not able to open GitHub?

11:46

Like if you see my current screen and you click here, are you not able to open the node starter there?

11:47

Like if you open this particular link that I've pasted, I can see clearly all the notes from 27, 28, 29 and 30 glass are present, right?

11:55

And you can see here in coding examples, all the codes are present.

11:59

Every code you will open, you will get the lecture number also.

12:03

Like for example, this is 23.

12:05

This could be a different lecture, then this could be a different lecture.

12:09

So did you open that?

12:17

I'm not sure like what is the issue.

12:30

So let's get started.

12:32

I think we can start with today's lecture.

12:34

So yeah, one by one we can start.

12:38

So yeah, today you will see this slide.

12:42

Till now, what we have done is we have understood about what is

12:46

what is like Lankchain, how to build a basic Lanchine, how it is calling different functions that are there.

12:53

We even saw that how to build a basic AI agent that can call third-party applications in the last class.

12:59

So today's class is just an extension of the last class.

13:03

What we are trying to do is we are trying to use memory now.

13:06

Like for example, currently if I send AI, any particular message that is there.

13:12

And if you remember in the last class also we discussed about it, that if I asked

13:16

a question calculate 5 plus 30 and if an AI agent it does not have any memory.

13:21

If I ask it this particular part, what was my previous question?

13:24

It will not be able to remember because it does not have memory.

13:28

Every question or every prompt that you are asking or every query that is coming is a new query for it.

13:34

So in order to solve that particular problem, what we are having, we are having memory component in the AI agent.

13:40

So today what we will try to see is we will try to see that how memory we will try to include.

13:45

include.

13:46

So later on other things also we will see.

13:48

But currently the main idea today is who have memory associated with an AI agent.

13:53

So let's start one by one we can see very quickly what are the things that are there.

13:58

The first thing is that why do you need memory with AI agent?

14:02

The main need of memory is this.

14:06

That what you want to do is you want your AI agent to remember the previous question that is present.

14:11

If that previous question is not there, then you will like every time you

14:15

you have to tell the entire context from scratch.

14:17

So that is why memory is needed in order to store a particular conversation, in order to

14:22

store context of a particular conversation that is present.

14:26

So let's say that if I have a stateless LLM, what is the stateless LLM, that each fall is independent.

14:33

Independent means that today if I type, send an email to this particular email address, then I

14:38

calculate 5 plus 6, both of them, they are completely different.

14:42

There is no relation between them.

14:44

Currently, if I type,

14:45

I try to include memory with that particular AI agent.

14:47

So what will happen?

14:48

It will remember the first question also.

14:50

That the first question was sending a email.

14:53

The second question was calculating preference, calculation of any particular mathematical problem.

14:58

So it will remember everything.

15:00

So whatever you ask, like for example, the same thing with Chad GPD does.

15:04

Then if I asked chat GPD that what is the previous message that I gave, then chat GPD will be able to

15:10

reply that.

15:11

So that's a main scenario that will happen.

15:13

So yeah, but this is how it.

15:15

it will work. So you need to remember that rather than like till now, whatever AI agent

15:21

that we have built, whatever things we were having, each fall or each query that we were having,

15:26

it was independent. Each query it was having a different scenario. That is the main thing,

15:31

that each query is independent of the previous question that is present. I think this idea is clear.

15:36

That is why we have introduced a memory part. And if you remember in the diagrams also that I was drawing,

15:42

I was having AI agent. Every AI agent, every AI agent,

15:45

what are the components that AI agent will have?

15:49

What are the components AI agent will have?

15:52

So we can see here this particular part that every AI agent, it will have multiple components.

15:57

The first main component will be the brain, that will be LLM, then there will be another component

16:03

that will be tools, then there will be another LLM, that will be what, that will be this particular

16:10

part, the memory part. So in order to remember the particular information, what we need is, we need, we need,

16:14

we need this memory component that is there. So yeah, this particular part we will try to see.

16:19

So today we will learn about this memory component because in the last two classes, what we have seen

16:25

is we have seen about the LLM component, that this LLM component is coming from Olam.

16:31

We have talked about how we can integrate multiple tools, how we can call all these particular

16:35

tools directly ourselves also. We have seen that how automatically LLM will call these tools,

16:41

even that particular part we have seen. Today, the main entire

16:44

will be that we will try to see this particular component that is the memory part.

16:48

So one by one we will get started and we will try to cover this memory part that is there.

16:52

And once this is covered, almost our basic AI agent we will be able to create with the help of LAMCchain framework.

16:58

So LampChair is a framework that is helping us write the code.

17:02

So today you will see this that in order to make this AI agent, I will be using inbuilt functions of LampChain that are present,

17:08

which help me with the memory part.

17:10

So one by one, let's get started and let's try to see that particular part.

17:14

So we can see here, like for example, we can see this that these are the messages that are there.

17:22

Like there are different, different functions that are present.

17:24

One by one I'll go to like different functions that are there.

17:28

Rather than directly seeing the theoretical part, let's go to the like concept that is there and then we can have.

17:35

Line chain we can create in this also edit and also we can see.

17:39

That example also we can do but first let's understand the coding part that is there for

17:44

this class and then other things we can talk about.

17:47

Let me open the code.

17:49

So yeah, let me open that.

18:14

up. So this is a program that I've already written, which is Lanchine Memory Program.

18:19

And you can see it's a big program. So one by one, let's get, let's talk about it.

18:24

You can see this that multiple different imports and everything will be present. So all those things we will see.

18:29

First of all, let's talk about the imports that are there. Like for example, you can see these many imports are written.

18:36

All these imports, what they are trying to do is, they are trying to help and import the already created functions that are there.

18:42

Like for example, 2E function.

18:43

example, 2E function we have already seen before, prompt part we have already seen before.

18:48

Message placeholder, we are seeing it for the first time.

18:51

If you remember in the last to last class, we have already seen human message and AI message.

18:57

So you know that whenever a query, it is going from us to LLM, then it's a human message.

19:03

Whenever a query or whenever the response, it is coming from AI to us, it's an AI message that is present.

19:10

Same way in order to remember the chart history and everything.

19:12

the chat history and everything, there is another inbuilt class that we will be using.

19:17

And there are other classes also that are present. All these classes we will talk about.

19:21

And there is the same land chain agents that we were using. I think it might be present from

19:26

classic package.

19:27

If you remember, in the last class also we saw that this package was not existing. So probably if you

19:34

remember the tool class that we had, where we were having different different, I think we were calling

19:41

entire tools and everything.

19:42

there we had this particular part that we were using all these things from LankChin Classic Agent.

19:49

So I'll update that because Lanktian Classic Agent can'tridae over.

19:53

Otherwise it will not have other things.

19:55

So I'll go to the code very quickly, which is the memory one. I'll update this line.

20:12

So we can see here this particular part that this is the Lankchain agent in which AI agent executor and create tool calling is present.

20:25

And we can see this is chart for Lama part. All these things you can see.

20:28

Today, new functions we are having, new things we are having, all those new things we will try to talk about.

20:34

So one by one I will start from the main function and let's see the new functions that we are having today.

20:41

First of all, you can see this that.

20:42

This is a function that I've created for manual memory set up.

20:46

So one by one, let's try to see what is happening here.

20:49

You can see that I'm trying to build an agent in which I'm storing the memory,

20:55

like whatever messages are there in an array.

20:58

So this is a scenario where I'm trying to demonstrate you that how manual memory can be stored.

21:04

Like for example, if you open chat GPD, I'll show you that demo also.

21:09

I'll share my other screen.

21:11

I think we have already discussed that.

21:12

part.

21:13

Do we remember the chat GPD demo that we discussed for calculation and what is the first

21:19

question that is there?

21:21

So if you see here, I think this kind of demo we have already discussed.

21:25

In this kind of demo, we can see here that we wrote a particular prompt that we got some answer.

21:31

So if I asked chat GPD, what is my first question?

21:33

It remembers that.

21:35

So you can see this that if I need to store all these conversations, I can directly store it in

21:40

an area right in order to remember everything.

21:42

can do that. So same thing I'm trying to show you that if I have to manually do it, then whatever

21:48

answer we will get. Like for example, if I call the particular agent and in that particular

21:54

agent, I've asked the complete chat history that is present, whatever message I am giving,

21:59

all these messages and everything, I am trying to store again and again. So you see,

22:04

chat history and that we are always appending what message gave from our side and what is

22:10

a message that AI has given.

22:11

this way we will try to do this particular part.

22:14

So this way what will happen is, like for example, if I ask AI that what is my, like my order ID

22:22

is this, and there is some data that we have like already defined.

22:27

So if I ask AI this particular part, that where is my, my order ID is this particular part,

22:32

it will do something, but all this conversation or the entire conversation, it will be stored

22:37

inside the history part.

22:39

So you will see whatever.

22:41

Whatever we are typing, like if you see the second question that I have written here,

22:46

it is what is the status of it?

22:49

So now, in order to understand what is it, it needs to remember that in the previous call,

22:56

we gave this particular part.

22:58

Like, for example, if this chat history is not there, if this chat history, like every time

23:03

the messages that are coming, if that thing is not present or that thing is not preserved,

23:09

then you will see this that, it will never be able to answer what.

23:11

is the status of it. But currently, since, like, it remembers that what is a conversation,

23:18

and we have given all the previous conversations that are there in an array, so it will be able

23:23

to tell me the correct answer. So we will try to run that part and we will see that part. Is that idea

23:28

clear?

23:32

This part are you able to understand? So this is the first function that I have written. In this first

23:37

function, a lot of things are there from the last class. Like, for example, if you remember,

23:41

In the last class, we have already seen how do we build an agent executor?

23:46

Like, first we add the brain, then we add the tools, the prompt, and the LLM.

23:51

LLM is nothing but the basic chart model from Olamma we are having.

23:56

We can see which model we are using. Like, for example, if I click here, you can see the model name is Lama 3.1.

24:02

I can even run it with Quen model and even that result I can see.

24:06

But in order to run the program, we will need Lama 3.1.

24:10

The next thing is that the base.

24:11

you are everything, whatever we are writing, those things we will provide.

24:16

We are creating an agent tool. And then we are creating an agent executor so that it can be

24:22

executed. If you remember that all these functions we already saw in the last class, like you remember

24:28

there was some function which was giving internal steps also. There was a function which was giving

24:33

internal execution loops. If I turn this verbose to false, then you will see just that.

24:39

You will not get internal outputs. That which tool is.

24:41

getting called and everything. If I turn it to true, then only I'll get that latest data,

24:46

that what are the internal tools that are getting called. Is that idea here? This idea, are you able

24:53

to understand? Guys, is this part clear or not clear? So we can see here this particular thing

25:04

that currently I've set it to true and all the parsing errors we are setting to true. And if let's say any call is failing, then it will retry three times.

25:11

So these basic values we have added and we have built an agent.

25:15

Only the new thing that we are doing is the first function that I have created, that is manual memory.

25:21

In that manual memory, how I am maintaining the memory, whatever message I am getting,

25:26

whatever message is getting coming from the human, whatever message is coming from AI, everything will be stored.

25:32

So you will see this that.

25:35

Since here, everything is getting stored in the chat history, which is a array.

25:39

So the first thing will be,

25:41

what is my order? My order is 102. That will be stored. Then what will be the response of that

25:47

particular part? That thing will be stored. Then if I ask it, what is the status of it? That will be

25:53

stored. This way, since every conversation is stored, that is why it will be able to pull the

25:59

correct tool here. Is that idea clear or not clear? This function, you are able to understand

26:04

manual function, where I'm creating a manual memory with the help of array. Is that part clear,

26:10

guys? Is this part clear or not clear?

26:26

Correct. So let's go to the next function that is present. The next function is how to create

26:32

stateless memory. So let's try to see that. So we can see what is the what will happen in case of stateless.

26:38

Let's stateless. Stateless means it's the same agent which is working without any memory.

26:46

So here you can see this that currently every time the chat history that I'm sending,

26:51

it is empty. It is a fixed empty thing. So you can see since it is empty,

26:56

this means that AI is not aware what was a previous message. Now since it does not know what

27:02

is a previous message then what will happen. If I ask it that let's say if I ask it,

27:08

this particular question in the turn 1 we should write here what is my order ID so you will see

27:14

this that if i ask what is my order ID it will like be able to tell me that okay the order ID

27:21

is this particular thing and the status as this thing if i ask it what is the status of it it

27:26

won't be able to reply why because this history is every time empty is this thing clear

27:33

tell here this part is clear so you can see this that in this particular part what

27:38

I'm trying to do, I am trying to show the stateless behavior that is present. I think this

27:43

idea is also clear. The next thing is that we are trying to see automatic memory. So first thing

27:49

is manual memory with the help of array in which everything will walk. In second thing, we don't

27:55

have any particular memory. If I don't have any particular memory, it will behave as an agent as it's the

28:02

same agent that we created in the last class. This yawala agent is that we made last class. So if you see

28:08

this is the same food that we wrote in the last class as well. In which you can see this

28:12

that we are passing verbose is equal to true. We are passing the necessary tools. We are

28:17

passing max iteration and handling parsing errors. All these things we have discussed before.

28:22

Only thing that currently what I'm trying to do is I am just calling here the AI agent and I am passing

28:28

the user input and I'm seeing that chat history is empty. I've got to take what manual

28:34

function. If I show you this manual function, can you see here the

28:38

chat history that i am passing it's a global array like it's a array that i have made here and this

28:44

array or list it is storing all the messages that are there every time whatever

28:49

message is coming from human as well as a i it will be stored is that part clear

28:57

global but who is function for global so every time when i'm calling this particular function then this

29:03

is not empty it contains the previous messages so you will see this that the first message is that the first

29:08

will be that what is my order ID order ID is 102 that will be stored then whatever

29:14

result that we are having that particular thing will be stored because here here we

29:17

here we're here here we're stored as well as the answer from AI that particular

29:24

thing will be stored now again user query will come what is the status of it so it will

29:29

understand that what is the status it remembers from the past conversation that

29:34

status hundred and two order to each other so it will reply with that

29:38

is that thing clear currently everything is forward in a normal area right raoul this

29:43

in this function we are using a normal array is that idea clear then there is another function

29:48

that we have built the second function this particular function in this function what we have done

29:53

is we are saying that if i pass every time the history empty then this is just a demo to show you

30:00

that if a i agent is not present with memory then what particular thing will happen it will be completely

30:07

empty. Is that idea clear? This idea are you able to understand?

30:16

Till here this part is clear?

30:37

Now we can see here this particular part. Like we can see here that if I click on this

30:47

particular link, this is a new function that I've created. In this new function, what I'm trying

30:52

to do, I am using new functions. These are the new functions that we are seeing today.

30:57

The first of all new function is runable with message history. What this function will do is

31:04

it's an internal function that is created.

31:06

which will manage the entire running section of message history.

31:11

What is the meaning of running?

31:13

So if you see this, that in a single conversation, like for example, whenever we are building with AI,

31:19

there is a complete chat history that is maintained.

31:21

Like for example, if you see here this example also,

31:25

can you see here that everything that I am writing, there is a complete history that is maintained.

31:30

Same way if I open any other chat window, complete history of messages will be present.

31:36

Is that idea clear?

31:39

This idea are you able to understand?

31:43

So we can see here this particular part that if I write this, then the renewable function, what it will try to do is,

31:50

it will maintain, it will manage the entire history. So you can see this that it will manage the entire

31:56

chat history and it will store the sequence of messages that are there. Like for example,

32:01

whatever messages AI agent is having, it will try to store that. Now this will,

32:06

will have multiple different things like it will have multiple different parameters that are there

32:11

one by one we can see all the parameters like for example if we scroll down then you can see this

32:17

that multiple different parameters are there now these parameters sometimes we have to use

32:23

sometimes even some of the parameters are not required like for example the first parameter

32:28

will be agent executor which is your entire agent the agent part is remaining the same

32:33

The agent we are creating here.

32:38

Only one new thing we have added that we are creating another agent which has memory and this

32:44

particular agent is created with this new function. Now this new function, it has multiple different

32:49

things. The first new thing is get session history. So you can see this that this session history

32:56

is a function that I have created and it is depending upon some other class. So you can see this

33:02

that I am trying to use

33:03

land chain database in order to store all the messages.

33:08

If you remember in stage three, or you can see in this particular function, what I was

33:13

doing is I was using manual array.

33:16

And this array, I was every time appending all the messages inside this

33:22

array and then I was able to remember the context so that AI is aware of entire chart

33:28

history, AI is aware of the entire context.

33:31

But currently, rather than doing that, what I am trying to do is, I am trying to use internal functions.

33:37

So there are multiple internal functions that are there, one by one we will talk about that.

33:43

The first internal function that we created is a renewable message history function, which will

33:48

maintain the sequence of messages that are there. In order to store the messages, there is a in-memory

33:54

database class that is present. So if you see, that is this particular class, in-memory chat messages.

34:01

What it is doing is it is storing all the messages internally.

34:05

So you can see this is managing my entire database.

34:08

It has multiple functions and internally it can use multiple different things in order to manage the messages and find out the messages.

34:17

So or he multiple sessions store.

34:20

Multiple sessions as a if you remember that this is a single conversation that you are having.

34:26

Now you might have multiple different conversation.

34:29

Our conversation is a message over.

34:31

Like, for example, in this conversation, you can see these messages are present.

34:35

If I scroll here and if I probably open this particular chart, you can see this that this is another

34:41

conversation that I'm having. Same way if I click here and if I open, let's say, this particular

34:47

part, you can see this that this is another conversation that we are having.

34:51

For every conversation, different, different messages are there. Or we can see for every session,

34:56

there is a different, different conversation or different charts are there.

35:00

it will try to maintain this.

35:02

This particular internal in-memory database or it's an in-memory tool that is present.

35:09

What it will do is it will try to find out all the existing messages, all the existing messages for a separate session.

35:17

So you can see this that this session history, it will maintain this, that this particular session in, these are the messages that are present.

35:25

So those particular messages or those particular history, we will try to determine.

35:30

Once we do that part, then though we are just following the necessary tools that are there.

35:36

If you see here that what things we are trying to do is, like for example, let's see from here,

35:42

if I ask it, what is the status of this particular order, which is Order 101.

35:49

Now, if I go to this particular order, my agent will be called up.

35:53

Now, when the agent is getting called up, I am saying that I am passing some configuration.

35:58

This particular configuration is nothing but the session ID that is there.

36:03

That this, this, that just focus here very seriously, then only you will be able to understand.

36:12

What I am trying to show you is, I am trying to show you that how chat GPD is working with the help of a scratch program that we have written.

36:22

If you see here chart GPD, you can see here that if I go to this math calculation function,

36:28

Can you see? Here I have asked, calculate 5 plus 8. It is saying 13. If I ask it a question, what is my first question?

36:39

Then it will tell you that this is your first question. Now, if you see this another message that I have written, what is the conversation or what is a question that I asked in the last chat that I did?

36:50

So this conversation is from a different chat. It's from a different session. So it is not aware of that.

36:57

Same way, the current program that we are having, it is storing session IDs.

37:03

Every session has a different chat window.

37:07

So if I draw a diagram in order to explain you this particular part better, you can see this, that there are two main functions that today we are working of.

37:16

One by one, let's talk about these functions in detail.

37:19

So first of all, you can see there is this particular class that is present or this class has multiple different functions.

37:26

I'll write down the number.

37:27

name also. The name is this which is storing. It is storing the history of all the

37:39

messages. So this is the first class that we are seeing. This particular class, what it can do is,

37:45

it is a in memory or in memory, as you can easily remember. In memory means internally it will store.

37:51

Every time the program is restarting, then it will lose the memory. There is no fix.

37:57

memory. Like for example, if I use something called this PostgreSQL database, or if I use any

38:02

external database, then you will see this that though they will store permanently memory. In memory

38:08

gets refreshed every time the server restarts or the program restarts. This point you need to remember.

38:14

So you can see this that this particular class, what it can do is it can store the messages automatically.

38:23

Now, what is the meaning of that it will store all the messages, but it is

38:27

is also taking one thing. It is storing all the messages in kind of a dictionary fashion.

38:33

Dictionary fashion, if you remember, key value pair. That if I have some session one,

38:38

like for example, the math calculation that I did, it is present in session one. So it will

38:43

store the entire history. It will say that humans said this, like the section will be something

38:49

like this, that human said this particular part that calculate.

38:57

5 plus 8. Okay. So human is saying this particular part, same way AI is saying this thing, that the answer is 30. Now, if I ask again, that human is saying, what was my first question?

39:16

So if I see here this particular part, then what will AI say? A. I will say that the first question was this particular part.

39:24

Now, if you remember, like, it will reply me.

39:27

with this thing. Now, if I ask here this thing that what was my last question in another

39:32

session, then it will not be aware of. Why? Because this kind of class, this is generally

39:39

supported everywhere in any AI agent that we are building, even in chart GPD, that to store the exact

39:45

messages, right? What they are trying to do is they are taking one session or this session is also

39:50

called as conversation. That this particular session, it will store the entire messages that are there.

39:56

Now, if I change the session, let's say that if I create here and any other session that is present.

40:02

If I write here, let's say, uh, session two, what will this particular session to do is this particular session two, it will not have any context.

40:13

So if I ask here that human, if I say that what was my first question, it will not be able to reply.

40:21

Here I will say that I don't have the context.

40:26

This example is clear that this particular class, what it is trying to do, it is trying to store in-memory messages based on the session ID.

40:35

The session is, it's a message stored in a single conversation.

40:38

Then a second session is, it's a message is store-gare-gare-but they will never be able to interact with one another.

40:44

So this part only I am written here.

40:46

So if you see here this particular part, like for example, if you see here this thing, you can clearly see this, that in turn one, what I'm trying to do is,

40:56

I am saying that in session a, this is a session that I'm having, that I have written here.

41:01

My order ID is one, like what is my order ID?

41:04

Yeah, I will reply something.

41:06

If I ask what is the status of it, it will be able to reply.

41:09

But if I change here session to different thing, let's say if I just change any name or I write anything,

41:16

then if I ask it, what is my order ID, it won't remember.

41:19

Why?

41:20

Because since it is a different session, you can see this session will make changes to what?

41:25

it will make changes to the configuration.

41:28

And what is that configuration all about?

41:30

The configuration is all about storing the history.

41:33

So this particular session history, it is taking session ID.

41:40

So now, when when that history is stored.

41:45

So you can see whatever history I'm having, that particular history is stored and it is returned to me.

41:50

If I again ask session A, then that history is stored.

41:53

But as soon as soon as, as,

41:55

as I change the session, then those things will not be stored.

41:58

Even I have printed everything that what is stored in each session and what are the messages that are present.

42:04

So everything we will try to review and we will see that particular part.

42:08

But these are the two functions that are there.

42:11

The first function is this in memory class that is present.

42:14

This particular class, it will store all the messages in a memory list.

42:18

Internally, it can use a dictionary.

42:20

It can use any particular database that it wants.

42:22

We don't have to worry about it.

42:24

The next.

42:25

is this particular function which will try to build a agent with memory history.

42:29

So what is doing?

42:31

This agent for a agent with functionality there.

42:35

Like till now the agent that we have built this particular agent, this agent only has what thing?

42:40

This agent has three things, which is LLM, tools and prompt.

42:43

It does not have memory.

42:45

So in order to build an agent with memory, what we are doing is we are calling this particular function.

42:49

So it is returning an agent, which is having a memory.

42:53

And what it is trying to do is, it has much.

42:55

multiple things. It has a normal agent. It has the session history calculator,

42:59

which will return the history and everything. Now you can see this that. It has some basic keys

43:04

which are like input message key that will tell us that, okay, what are the inputs and

43:10

everything we have passed in order to understand what things are given by user, what things

43:16

are given by human. Let's say, you can see this that here I am passing user input.

43:21

This user input, my order is one zero one.

43:25

order to identify that this message was given by a human. I am writing a input, right? From

43:31

this it will understand. If I just say here this particular thing, like for example, if I write

43:36

here, human, and then here also I have to write human. So that internally it is aware of

43:44

which messages are given by human. Is that idea clear? So you can see this that currently

43:50

here I have written input. That is why here also I am writing input. So this is just

43:55

identify that which messages they are actually coming from the human part. So as I

44:01

shown you a demo also, that if you want to change it, let's say that you want to change it to

44:06

change it to human here. That means all the input that you are providing. This is a human input.

44:11

Then you need to provide here also human. I think this idea is clear. This idea you are able to understand.

44:22

Guys, is this thing clear or not clear?

44:25

So we can see this that we have written a prompt also. Like for example, if I go to the starting part, let's see the prompt that we have right on. So I'll show you this now.

44:44

So again, we can see the program. So we can see from the start we have imported all the necessary things that are present.

44:51

We have imported the model and everything. These are the basic things which we already do.

44:55

You can see this that currently I have just for demo purpose that I have added two orders.

45:01

The status of one zero one is shipped. The status of one zero two is canceled.

45:06

And I have created a get order function tool. This is like a you can say it's a basic function which

45:11

LLM will try to call. So currently there is only one tool which LLM will call when that particular tool will be get order function.

45:19

It will call it automatically. Since it is calling it automatically, that is why you can see here this particular part.

45:25

that I am building this agent executor so that I don't have to call it automatically who will call.

45:34

LLM will call.

45:35

So that is why I have registered a tool here and this tool is nothing but a basic function that will get called and it will just tell me what is the order status.

45:44

So you can see this is a tool that I have registered.

45:47

Now you can see this is a system prompt that is present.

45:50

In this system prompt, I have written multiple things.

45:52

I have written that you are a helpful customer support agent.

45:55

that is present. So you can see that particular part. You can see if a user gives an

46:01

order ID, remember this conversation. For follow-ups, track it. What or what is a status use?

46:08

You can see use the order ID from chat history. So you can see since I have written here

46:13

this chat history, right? And I am passing here a message is also that it will remember the entire

46:21

chat history that is there. In order to remember that I've created this very

46:25

which is chat history. So you can see it chat history is a internal function that is

46:30

provided by Lanchine which will try to store the necessary chat history.

46:36

So what is the conversation is what chat history is? So what will be the prompt

46:40

execute? When LLM to go to it will have this system prompt. It will have the human as well as

46:49

well as the input that human has given. It will also have this particular chat history. Now if you

46:55

remember the other thing. Like for example, if I go back, I scroll here in the program,

47:00

if you see this particular part. In this part, if you see this particular function that I have

47:04

written, in this function, you can see that I have passed a chat history as empty.

47:12

Since here chat history is empty, what will happen is that he joe prompt

47:16

is a templated prompt. This prompt is nothing but a templated prompt that is there. It will have

47:23

system input. It will have chat history and it will have human input. So

47:30

our function is this particular function if we go to the manual function that is present. You can see

47:37

this particular function is passing Chad history as empty. Since it is passing chat history as

47:43

empty, it will not get any data. Like for example, it will not have that particular data. It will have

47:49

only the human input that is there. Is that part clear? This. This

47:53

part are you able to understand?

47:59

So that is why if you see here that this chat history that I am giving, same kind of

48:06

chat history key I have provided, that it is aware of what is the chat history. So

48:11

this history messages are where are? That chat history is. So he's chat history

48:16

store it will use that particular chat history in the system prompt also in order to answer

48:23

everything.

48:23

that particular thing it will do apart from that whatever output we are attaching

48:29

so you can see this that since we are returning here the final output we are saying that

48:33

the final message is that the output we are stored so that we can easily return it

48:38

and then only you can see that directly whatever output that is there we will just try to

48:43

print that output so this is nothing but for telling that this is a key of output and

48:49

whatever output are you can consider that everything here that is present is

48:56

nothing but a dictionary so output it has the necessary output that is there which model will

49:02

return and that particular thing we will try to display like we will try to return here

49:07

and that thing will be displayed from this part this part are you able to understand

49:19

this part are you able to understand so one by one we can see the entire program

49:27

one more time so i'll repeat the entire program and one by one let's try to see so we

49:32

can see first we have imported multiple different things you can see this that all these

49:37

things we have already imported in past classes today we are seeing two or three new things

49:42

one is the message playlist folder one is in memory chat history and one

49:49

is runable with message history that is present apart from that this line i need to

49:54

change on get up so i'll change that once i run the program and i'll push this fort currently i think

49:59

this line is not pushed so you can see that part also you can see everything is present here all the

50:05

things are present in this part now you can see all the orders details are present and the order status

50:12

is also present up so you can see this is just normal feature data that i have given so that LLM

50:18

LLM can call the necessary tools and everything and it can actually find out the order data

50:23

in real time cases rather than this particular part we will be calling the actual APIs that are

50:30

there correct so that particular thing is there apart from that you can see that i've defined all

50:36

the tools so this is just the tool calling part that is present that we are calling a external

50:41

function in order to get the order status and everything there rather than a python function

50:46

our API call can also be there i think this idea is clear right this idea are you able

50:54

to understand the next part that we have written is that we have written a prompt in this

51:00

prompt you can see three things we have written the first thing is a system prompt the which you

51:06

can see here this is a system prompt which is telling to remember everything now it can only

51:11

remember if it has chart history so you can see this that that particular chat history i've added here

51:16

so you can see all these things i'm storing that history we let's

51:20

to store for storing this chat history inside a prompt you can see i've used this

51:27

placeholder it is just providing a message to a prompt

51:32

we have a message attach to that

51:34

to that for us

51:35

we're saying it's nothing but a prompt template part which can store a list of messages

51:41

so this particular variable the variable name is chat history and it will store all the messages

51:46

after that we will pass the human input joe our human input query that we can

51:53

see this that this agent will fill agent will add all the details like for example all the steps which

51:59

agent is doing everything that it is figuring out from everything that is stored inside agent scratch

52:04

pad so whatever agent is doing let's say agent is making a tool call or if agent is doing any

52:11

x y z scenario figuring out things from chat history all these things i'm storing in

52:16

agent scratch pad so even if i want i can even print that part

52:21

apart from that you can see this code this is just creating the model so

52:25

we joe the model create that we have already done in the last time so if you remember we

52:33

created an agent that agent is having three things which is the llm tool and the prompt that is there

52:39

apart from that i have added one example this example is for manual memory that today if you

52:46

don't want to use the internal memory that is present what you can do is you can use

52:52

your own array and that particular array can maintain and store all the memory part so if you see here

52:58

this particular thing you can see this that it will store the chat history it will store entire

53:05

data that is present like for example if i ask it what is the order and everything it will store the

53:11

entire human messages it will store the ai messages that are there everything it will try to store

53:16

so this way i am trying to build a function which is storing manual memory then i've created another

53:22

function which is running without memory so here you can see the chart history is empty

53:26

but in the previous question we are passing this array which is storing all the memory messages

53:31

that are there apart from that we can see we have created one more function and this one more

53:38

function what it will do is it will store all the necessary messages and all the necessary sessions so here we are

53:45

using lanchain's internal memory system so we are trying to use lanchain internal memory

53:51

system in order to store everything every information so first we created a normal agent then on

53:58

the top of that using the agent that is already created we are creating another agent with memory

54:04

that memory agent will be session compatible that if this is a session then it stores history

54:10

of the messages if the session is different then different messages history will be there

54:15

for every session it will store a different message history that is a particular

54:19

part then you can see multiple here terms are written there is a human term that is present so

54:25

human you human yeah to be our agent who we're giving which input you are given like for example earlier

54:34

i was writing here input since here i am saying that this input contains human input message

54:39

in order to tell a i that this message is actually provided by a human what how it will know this

54:45

Like the LLM can't know this human input hacking here.

54:49

So that particular part I have written.

54:51

Same way in order to tell it that where from where to pick chat history and everything,

54:56

I am telling that variable which is chat history.

54:59

Once agent has given the final output, I want to store that output in output key that is there.

55:05

So that particular output key will contain the final output and that is why here you can see I'm writing

55:11

result of output. So this way basically what it will do is

55:15

it will say that okay but this is the final output that came

55:19

we are extracting that output and we will return that data once we return that data

55:24

that particular part will be printed is that part clear

55:28

so lanchine internally will store the history with the help of what it will

55:32

store the history with the help of in-memory session storage that is there

55:36

so you can see this is the in-memory database or you can say in-memory

55:40

implementation which will store the entire message history

55:43

internally it can use any text stack

55:45

and it will store the data for every session like session a it will have a different

55:52

memory storage session b will have a different memory storage i think till here this part is clear

55:58

this part are you able to understand so since here two sessions are there so if i ask it in a single

56:05

session that what is the order ID and what is the status it will be able to remember but if i

56:10

change the session then it will all be aware of which is the order ID you are asking so that particular

56:15

thing will happen so if i just update the program also like for example if i write here

56:21

get status i can just uh

56:45

this program that is there i'll go to the specific folder this is coding examples

56:50

coding examples in there we'll name chain with memory so we mary we can see this program

56:58

is there if any error is there i'll try to fix that error but before that error we we need to

57:03

check if olama the latest model we are having or not i'll just write here olama list

57:10

list and i'll try to check if i'm having olama's 3.1 list and i'll try to check if i'm having olama

57:15

test is present so since 3.1 is there and i have written 3.1 in the program it will

57:21

it should work so i can directly say python 3 if it is failing then i'll try to install

57:29

necessary things but let's try to see so currently you can see even the agent logs and everything

57:34

will come up that is why you can see all these things in green color right they are the internal logs

57:40

if i just disable that particular part even that thing will work up some error is there

57:44

is there but that error we will fix let's go to the first above part and see the basic

57:49

output so currently you can see we can see here this particular part that one by one let's try to see that

57:57

denote we have this manual history on in this manual history on what thing i have done is i am asking

58:04

a question that what is the order id 102 so it it will tell me that the order id is this particular part

58:11

and if i ask it what is the status of it

58:14

then you can see this that i'll just disable all the logs so that it is not that much confusing

58:21

so i'll scroll up i'll go to verbose is equal to false to the locks skip as i'm like we will

58:27

not be able to read properly so since we want to read the output properly i'll go here

58:36

i'll type here false if i type here false now internally no logs will be printed so let's do that part

58:44

now we can read the output in a better way so let's try and then we can go to the

58:55

other thing also we can fix that error and then we can see so if you see here we can see if i ask

59:01

it what is the order 102 so you can see this that currently the order is it remembers the order

59:08

id like the order id is 102 and then if i ask what is

59:14

is the status of it so you can see it is saying clearly that since your order has been

59:19

cancelled we will not be able to proceed with original request so he is

59:24

he says it can't say it's because he has here here remember

59:28

got here and here we have created a manual array in order to check and see how like

59:35

memory is working so currently in this particular part we can see here this thing

59:39

that we have stored the memory properly like a ii need order id remember

59:44

and order ID what is 100 and 2. So if I'm

59:48

I'm asking what is the status of it then it is clearly saying that it is cancelled which is

59:53

correct like for example if you see here that it is cancelled. If I here

59:58

here here maybe delivered

1:0:00

then change is gonna let's try that so you can see I have made that change that

1:0:05

it is delivered and I'll go here and I'll again ask I'll again run the program

1:0:11

so you can see here that

1:0:14

now it is saying order hasn't successfully delivered if you have any other questions

1:0:19

you can ask them so that particular part we have seen i think this first stage three is clear to

1:0:25

everyone right stage three are you able to understand now see the stage four part that is there

1:0:33

like for example stage four page are there in which memory is off and you can see it will

1:0:38

try to remember order id 102 but obviously has order id

1:0:44

Why are you because chat history is not there then it is saying this particular part

1:0:51

that it cannot use it so you can see this that if you share the order ID now I'll remember it for

1:0:59

our conversation if not please let me know how we can proceed accordingly so this is just a

1:1:06

basic scenario to see that particular part apart from that this is a depreciated warning you don't

1:1:11

have to worry about this warning this is a

1:1:14

normal warning that is there that Lanchine

1:1:16

instead of Lanchine function

1:1:18

is runable with

1:1:21

a message history it is depreciated

1:1:24

and we can use LAN graph

1:1:27

system that is there

1:1:29

so it is just a warning that is coming

1:1:31

I'll check the below error that is coming

1:1:33

it is I think due to the same thing

1:1:35

that our function depreciate

1:1:37

okay I'll just fix the import of that

1:1:40

and then we can discuss the third scenario

1:1:42

but I think the stage

1:1:44

3 and 4 are clear to everyone right this part are you able to understand this much

1:1:49

which I've highlighted right now

1:1:50

now

1:1:56

yeah print to have

1:2:00

correct kind of like for example if you see here I have printed this everything

1:2:06

turn 2 depends upon turn 1 it I have already printed that right all these print

1:2:10

statements are written here that is why it is coming is that idea is that idea

1:2:14

clear.

1:2:21

Guys, still here this part is clear.

1:2:25

So let's try to see the next part.

1:2:27

I'll just fix it, I'll show you the GitHub till then.

1:2:30

If I go here to this part, you can like, let me just fix the program.

1:2:35

I think one minor change we need to do, but this is the program that we are having.

1:2:40

So if you open this particular link, you will be able to get it.

1:2:43

to get it. This is the program and I think everyone has the getup repository, right?

1:2:48

So in the main get up repository you can open it.

1:2:50

Let me fix the import issue till then and then we can try.

1:3:05

Till then you can copy paste the program and probably try to run the like first two stages that are there.

1:3:12

We need to just fix the import part. I'll just quickly fix it. I'll just quickly fix it. I'll see if I can actually fix the Langraph's warning.

1:3:30

That is a warning that is there. That Langeink of that function depreciate. It's a warning. It's a warning.

1:3:37

So this kind of messages that you can see, right? It's just a warning.

1:3:41

It's just a warning that is coming up.

1:3:50

Here, this part is clear. Are you able to understand the meaning of the program?

1:3:54

Is the program meaning to everyone? Meaning are you able to understand?

1:4:11

This is the mini clear or not clear?

1:4:41

but warning part we will do. But yeah, let's try to see the demo once again.

1:4:46

So now you can see the last stage that is there, which is this particular stage, which is that what we are trying to do is, we want to use automatic memory.

1:4:56

Now this particular automatic memory, it is coming from where you can see this is that in session A, like whenever a user cushion I have not printed, but the user question is, what is the status of order 101.

1:5:09

So you can see it remembers.

1:5:11

Like if I, I'll just print that also. Like for example, if I go here to this part, I can write here some code again even so that you understand the program properly.

1:5:23

We can say this that session 8 turn 1 and I can say that human input.

1:5:30

In the human input, I can say the human input is what? It is what is my order ID 101. This is my human input. And in session A only.

1:5:41

What is the human input that is there? I can say the human input is what is the status of it. So that will properly print to be over.

1:5:58

So you can see once it is printed, I think I, yeah, now it is correct. So this is for session A. Or a section B.

1:6:11

I think that's going to be up now. Human input, turn 1. What is my order ID? So let's try. Now what I'll do is, I'll go here.

1:6:27

I'll tight here now again. So let's try to see. So you can see this that now proper output is coming. That session A, human input is what is my order ID?

1:6:41

It will remember that order ID is 101. If I ask what is the status of it, then it remembers that the order ID has been shipped and everything and it is knowing.

1:6:53

In session B, you can see this that if I ask what is the order ID?

1:6:57

Then you can see it is saying that it does not have any order ID in the history. So this particular part is there.

1:7:03

You can see currently two sessions we have stored. So that is why you can see two sessions are there and all the messages that are present.

1:7:11

Like why you are seeing here four messages. One message will be what is my order ID?

1:7:17

Second message, it remembers AI's your response over.

1:7:21

Then we can see here that the second message will be what is the status of it or the AI response over that will be present.

1:7:29

Same way we can see here this particular part that what is the order ID? And apart from that we can see all the like these two messages are there that was stored in session B. That is why that count is printed.

1:7:40

If you want, I can even show you how all the messages also.

1:7:45

So let's try even that.

1:7:47

Like rather than printing the length of everything.

1:7:52

Let's just print the messages also and we can even see the messages that are there.

1:7:57

It would a like or jada jada jaya like it will try to print multiple different things, but let's try.

1:8:06

So if we try here this particular part, let's see.

1:8:10

So you can see these are the messages. Can you see now?

1:8:14

This proper, the internal message shown are, that all messages are.

1:8:18

Just if you can see here the order ID is 101. That is a message.

1:8:24

AI's what? AI is remember. Then we can see human messages. What is the status of it?

1:8:32

So you can see this that. If I just decrease the size of this also, you can see here that human's message is.

1:8:40

What is the status of it? And AI's a message.

1:8:43

AI's message in output. It will be this particular part.

1:8:47

That the message is that the order 101 has been shipped. You can expect the delivery within next few days.

1:8:56

So if we have all messages look at, we can see. We can even see the length of the messages.

1:9:01

Four messages are here. Here we can see only two messages are there. What are the two messages?

1:9:07

The first message is what is my order ID? The next message is,

1:9:10

I don't have order ID in the history. That is the AI message that is there.

1:9:14

So this way we have done it. I think this part is here to everyone, right?

1:9:19

So even if you want to print the exact messages, you can do that change.

1:9:24

But currently that change is not required. I'll just push the latest program that is there.

1:9:36

Once I've pushed the latest program, you guys can try to run it.

1:9:40

particular part you can see. So if I go to very quickly to Firefox, you can see here

1:9:46

this is the latest link that is present. So Pura, right? Are you aware of that, that you have

1:9:52

to use the updated link?

1:9:53

Apne rei repository, then open the program, then the link will open. So if you just open

1:10:01

the previous session, it might not open, right? Because I organize the folders in a different

1:10:05

way after a session. So just open the main repository. Main repository, same. I was

1:10:10

you look at the program that is there.

1:10:13

So for that, this is the main link that is there.

1:10:17

In this main link, you will find out everything.

1:10:19

So we can see today we are discussing this

1:10:21

Lanchine of memory program.

1:10:23

So this is the 30th lecture program.

1:10:25

You can see the program is updated and everything,

1:10:27

whatever we have done is present.

1:10:29

And even I think that session,

1:10:31

what I've been latest add together, that is also present.

1:10:34

All the things we can see here.

1:10:36

Is this part clear?

1:10:40

I'm still here at this part, are you able to understand? Can you try running the program also now?

1:11:03

I have updated the program.

1:11:05

Let me remove the warning in the background also somehow, if I can remove the warning in the background.

1:11:09

remove the warning also. Let me try that. Is, did anyone try to run the program? Are you able to run the program?

1:11:34

Are you able to run the program? If you can run the program, can you write in chat?

1:11:38

Yeah, right?

1:11:39

Lama 3.1 will be required.

1:11:41

If it will install it, then it will be correct.

1:11:43

Otherwise, not it will.

1:11:46

We can ignore the warning that is there.

1:11:53

I think warning,

1:11:55

Ignoration part that we can do.

1:11:56

Langraph to we will not use.

1:11:58

So I think warning ignore function I have added.

1:12:01

Yeah.

1:12:02

I think that particular part we can do.

1:12:05

So I'll just push that latest code also.

1:12:07

code also. So that warning will also stop coming. It's a minor warning.

1:12:12

It's just this is that function now

1:12:14

being.

1:12:15

We're going to go.

1:12:16

We'll land change and land graph's a function use

1:12:18

but land graph's function we'll see

1:12:21

again.

1:12:22

So once we learn that part, then we can see.

1:12:24

So I'll do that.

1:12:26

I'll say get commit update content and I'll push that change also.

1:12:31

So once I push it, if I now run it,

1:12:34

like for example, now if I try to run this particular

1:12:37

thing we can see here that now warning will also not come up and you can see all the three things are working

1:12:46

I think warning hey we can ignore that warning that warning is not required

1:12:51

we can see this that the order ID is present like this is the array part where it is able

1:12:59

to remember the memory and everything it remembers the exact detail then we can see here that if I

1:13:06

ask the status of it is able to tell me the status as well currently it's

1:13:10

successfully delivered i can change to canceled also if i want apart from that we can see here

1:13:16

this particular part that if i don't want to store the like if i don't store the memory and everything

1:13:22

then it will never remember that so that is why you can see it is showing here this particular part

1:13:27

that it does not remember the order ID and everything and here we are using internal memory we are

1:13:34

using two functions the first function is run able with message history the second function

1:13:39

is this one which is session storage which is session

1:13:42

storage store and it will store the chat history so you can see in session eight

1:13:48

remembers the id very clearly but in session b does not remember the id so that is it right

1:13:53

like that is the entire program i think this part you are able to understand is this part clear

1:13:59

Olama pull command is now Olama pull can't and then you need to write

1:14:07

the exact thing like for example if i go here I can say Olama pull and if I want to run this

1:14:16

program then I need to run this particular part if you can run

1:14:19

then you there is a separate command for that so quen

1:14:23

run and then the command will be this even with quen you can you can try to run it but

1:14:29

then you have to update the program with that part so that particular part you can do

1:14:34

i'll remove the warning code i think that warning code is not working is it saved yeah i think

1:14:41

that warning part is not required i can remove it currently we will get a minor warning but that is okay

1:14:52

so if we go here very quickly let me update the final

1:14:59

and

1:15:01

you know,

1:15:29

What, what?

1:15:42

What?

1:15:43

What?

1:15:46

Will I'll list and see you.

1:15:51

Shat Yara is first.

1:15:52

I'm not sure if

1:16:02

Lanching internally is changing to depending upon which model it is using that.

1:16:06

But Ullama list and look, go on.

1:16:15

Share your screen.

1:16:19

People are you able to run the program?

1:16:22

Can you hear me?

1:16:27

Yeah, let me give you the permissions to share the screen as well.

1:16:31

Are there people any other doubt I'm like, did you understand the program or not?

1:16:40

Yeah, share your screen.

1:16:43

Just given that.

1:16:52

you see my screen now?

1:16:58

Yeah, I can see it.

1:16:59

Yes, yes.

1:17:00

Just give me one.

1:17:05

So here I'm using Lama 3.1 and

1:17:09

environment file is there,

1:17:11

environment file click on Envi file.

1:17:14

Envi file.

1:17:16

It's no, there.

1:17:19

So, man, program,

1:17:21

the program like read the program open the program that you have written or yeah

1:17:27

now do you just open the program yeah now scroll down

1:17:33

now you read line number 72

1:17:37

line number 72 is saying OS dot environment dot get

1:17:45

Olamma model to what is what is what is what is what

1:17:49

Get what is.

1:17:50

What is in the environment from the model

1:17:52

name get

1:17:53

is a

1:17:54

if it

1:17:55

if it's not

1:17:56

not

1:17:57

like my case in

1:17:58

because I have

1:17:59

I have an environment

1:18:00

file

1:18:01

just you

1:18:02

you go

1:18:03

open your environment file

1:18:05

I'm not sure if this

1:18:07

is the environment file

1:18:08

or another is an environment file

1:18:09

but this environment file

1:18:10

in the first line

1:18:11

delete

1:18:12

delete the first line

1:18:14

or just comment it

1:18:15

yeah

1:18:15

now run the program it will

1:18:17

start failing

1:18:19

Lama 3.1 and now it will not work because

1:18:23

Lama 3.1

1:18:23

you have not

1:18:24

I've never

1:18:27

I've always run

1:18:28

with coin

1:18:29

so I thought

1:18:30

that we're

1:18:31

there we've

1:18:32

did it but

1:18:32

here we have

1:18:33

same model

1:18:34

used

1:18:34

So here I

1:18:35

to try catch

1:18:36

like it's like

1:18:37

try to fetch it

1:18:38

from E and me

1:18:39

if any ENB is

1:18:40

there then good to go

1:18:42

otherwise it will try

1:18:44

to find out Lama

1:18:44

so currently it will

1:18:45

try to hit Lama

1:18:46

and Lama is not there

1:18:48

even we can't

1:18:49

can just write a basic program

1:18:51

to print the model name also

1:18:52

if you just write

1:18:53

print main function in there

1:18:55

then it will try to do that

1:18:57

so now you can see it's failing right

1:18:59

because it is not able to find out anything

1:19:01

and ENV

1:19:02

in a year one line up

1:19:04

uncommette

1:19:04

so look

1:19:05

coin

1:19:05

going to go and

1:19:06

and now

1:19:08

now a main

1:19:09

open main

1:19:10

before running open main

1:19:12

uh

1:19:14

uh

1:19:16

this might define

1:19:17

scroll down scroll down

1:19:18

scroll down scroll down

1:19:18

scroll down, down, more down, more down, main function.

1:19:28

Uh,

1:19:29

this my number

1:19:30

two hundred,

1:19:31

779K

1:19:32

pelle,

1:19:32

709

1:19:33

just about like the print model name.

1:19:36

I mean,

1:19:36

I'll,

1:19:36

I just print.

1:19:40

I think you ran the program.

1:19:42

I'm not sure.

1:19:43

Yeah, just write print.

1:19:47

And then write

1:19:48

yeah bracket

1:19:49

and write model name

1:19:51

model name

1:19:55

capital I enter the bus

1:19:56

johar enter on the bus

1:19:57

and close it close it

1:20:00

close it

1:20:00

bracket

1:20:01

type close bracket

1:20:05

type close bracket right

1:20:08

yeah save this and run it

1:20:11

so now you will see the model name

1:20:12

will be Quinn

1:20:13

if you just change the model name

1:20:15

in the end we also do other thing

1:20:16

then also it will

1:20:17

you will see it will work

1:20:19

getting the idea right how it is working

1:20:21

currently it's

1:20:23

picking from EnV file if you install

1:20:25

Lama model then it will work just see the output

1:20:27

of first thing the first thing will be the

1:20:29

model name now

1:20:30

and that model name will be

1:20:33

quen 3.8

1:20:34

which be value

1:20:35

so it will load that

1:20:39

particular model and it will do that

1:20:40

you can see right

1:20:44

quen a guy

1:20:44

and now it's all yeah

1:20:45

now it's why can't

1:20:46

why it's why it's going to

1:20:47

your ENV in the ENV in

1:20:49

any ENV in there

1:20:49

be Lama

1:20:50

then if

1:20:52

if Lama is installed

1:20:53

then ENV

1:20:54

if it will be

1:20:54

not going not

1:20:55

like my case

1:20:56

in NV

1:20:56

then it is using

1:20:57

every

1:20:57

defined value

1:20:58

that is there

1:20:59

correct

1:20:59

so basically

1:21:01

if you don't

1:21:03

give

1:21:03

3.1

1:21:04

it's not necessarily

1:21:05

it will take it from

1:21:06

the amount of

1:21:07

yeah right

1:21:08

the code clearly

1:21:09

clearly says that

1:21:10

right

1:21:10

code in the

1:21:10

code in like

1:21:11

get from

1:21:12

ENV first

1:21:13

otherwise if

1:21:14

ENV is not there

1:21:15

then take Lama

1:21:16

correct

1:21:16

correct?

1:21:17

That is

1:21:19

another question is regarding the output parser.

1:21:23

So currently we're

1:21:24

everything

1:21:25

we're print in this format,

1:21:26

but let's say we

1:21:27

have a tabler format

1:21:29

print

1:21:30

so how do we alter things

1:21:32

and where do we change things

1:21:34

for the output parser

1:21:35

so that we can

1:21:36

but

1:21:38

mainly decorate it

1:21:39

or

1:21:40

in some

1:21:41

if let's

1:21:41

table format

1:21:42

in a data

1:21:43

print

1:21:47

this data

1:21:48

we need to

1:21:48

this data we need to use

1:21:52

Pandas for that

1:21:53

like Panda can convert

1:21:54

any textual data into

1:21:56

tabular data

1:21:57

right we can use a library

1:21:58

called as Panda or NAMPai

1:22:00

and generally I think

1:22:01

Panda will easily convert the data

1:22:03

whatever data you are having

1:22:04

you can store it into CSV file

1:22:06

and then convert it and print it

1:22:08

and pass

1:22:08

like CSV format

1:22:09

so you can read about

1:22:11

Panda's library that is there

1:22:12

it will easily convert it

1:22:13

even Nampai Panda

1:22:14

easily we can use

1:22:15

and we can do that part

1:22:16

Hello.

1:22:17

Hello.

1:22:21

The AI part is clear, right?

1:22:22

What all functions we talked about and all these things.

1:22:26

Yeah.

1:22:27

Basically I was building on

1:22:30

in this session on the program

1:22:32

running on I was building on agent

1:22:34

using a simple memory

1:22:36

where I wanted to print a list of

1:22:39

all the profiles from Nogpri

1:22:42

where if a user gets input

1:22:44

as Java,

1:22:45

so Java,

1:22:46

this I've made

1:22:47

this video

1:22:48

is

1:22:49

uploaded

1:22:50

you are

1:22:51

you know,

1:22:52

you're doing

1:22:53

know,

1:22:54

and all the

1:22:55

things

1:22:56

sheet in

1:22:57

all right,

1:22:58

right,

1:22:59

but in general

1:23:00

this video

1:23:02

is already

1:23:03

there on YouTube, right?

1:23:04

Did you have the video link?

1:23:06

Um

1:23:07

I don't have a

1:23:08

I'll go through it,

1:23:09

I'll go through it,

1:23:10

yeah

1:23:11

Yeah,

1:23:12

I have the same project I've already

1:23:13

built it and even

1:23:14

I think in Basile Life

1:23:15

they have uploaded it

1:23:16

even if you don't find it there,

1:23:18

like you can, I can share you a

1:23:20

white link of that video, you can just watch it on YouTube.

1:23:22

I've already made this project and made a video on that also

1:23:26

and share the link.

1:23:28

Okay, I think that

1:23:29

real API used

1:23:30

but this is just I'm mocking

1:23:32

Yes, yes, yes, yes

1:23:34

I used.

1:23:35

Correct, correct, correct, correct.

1:23:37

And I'm actually

1:23:39

many times I'm facing problems regarding the line chain

1:23:42

so versions are different

1:23:44

like for this one.

1:23:45

like for this one also, this was,

1:23:47

until unless I used classic dot agents

1:23:49

of the last 10 re-water.

1:23:51

So, like, how do we deal with such kind of problems

1:23:53

of reversion regarding?

1:23:54

These kind of agents,

1:23:55

like,

1:23:56

this kind of a bit of time,

1:23:58

because every time some package will go off.

1:24:01

So we will have to find out the latest package.

1:24:03

It's like that

1:24:05

every year there is a new iPhone that comes up, right?

1:24:08

Same way every year a new package will come up.

1:24:10

That thing will never stop, right?

1:24:12

So, yeah.

1:24:14

So production,

1:24:15

version no, if you're

1:24:17

No, if they're not.

1:24:18

If they're not,

1:24:19

if they're,

1:24:20

like in companies also once you go,

1:24:21

there will be like,

1:24:23

you will always get a notification that this

1:24:25

package is getting upgraded so you can

1:24:27

fix your code beforehand so that your code does

1:24:29

not start breaking up.

1:24:31

So that particular thing we always have to do.

1:24:33

Correct?

1:24:35

Okay.

1:24:36

Yeah.

1:24:37

I think till here, everyone is able to understand the program, right?

1:24:41

Riju can and clear the program.

1:24:43

Hello, can you hear?

1:24:48

Uh-huh.

1:24:49

Yeah, I'm, I'm asking that we,

1:24:51

we have class used in-memory for

1:24:54

In-memory for.

1:24:56

In-memory, yeah.

1:24:57

So that class use,

1:24:59

why we are using class?

1:25:00

Class use not,

1:25:02

is it taking some argument as form of object

1:25:06

or are we creating class due to some different reasons?

1:25:09

Already in-built class,

1:25:11

so we're just used?

1:25:12

class, just use

1:25:13

this particular thing we are doing.

1:25:16

Okay, I mean,

1:25:18

okay, okay, got it.

1:25:19

We're in-build class

1:25:20

use in-build class

1:25:21

use in the

1:25:22

other thing also.

1:25:24

Like if I want to build, I can do.

1:25:27

It is not

1:25:28

correct.

1:25:29

It is not,

1:25:30

like you have

1:25:31

You can

1:25:32

use

1:25:33

you can use

1:25:34

you,

1:25:35

other databases

1:25:36

post-grey SQL,

1:25:37

anything you can use.

1:25:38

Just we have

1:25:39

added,

1:25:40

that area,

1:25:41

is SQL, Superbase, Neon, any other database that you think of,

1:25:45

you can add that.

1:25:46

We can add.

1:25:47

And another thing is,

1:25:48

like,

1:25:49

let me, let me

1:25:50

DQ class use

1:25:51

and that

1:25:52

you can use that

1:25:53

correct.

1:25:54

You can store

1:25:55

all messages, that is correct.

1:25:57

Okay.

1:25:58

I just this is

1:25:59

asking

1:26:00

because

1:26:01

okay,

1:26:02

I mean,

1:26:03

there are there

1:26:04

I will discuss it later with you,

1:26:05

but thanks.

1:26:06

Yeah, yeah.

1:26:07

I think till here,

1:26:08

guys, everyone is able to understand.

1:26:10

Did you understand the

1:26:11

the program logic and everything, whatever we are writing, is that part clear?

1:26:41

are you able to run the program?

1:26:46

Program everyone is able to run right?

1:26:48

Go on Aminash?

1:27:10

Go on, Amidash.

1:27:12

Uh-huh.

1:27:14

Section, one more question regarding the memory.

1:27:16

So you told that we are using the memory capabilities

1:27:19

of LangChain for this agent, right?

1:27:22

Go on, go on.

1:27:24

Yeah, so, but,

1:27:26

uh,

1:27:27

agent I was in,

1:27:28

um,

1:27:29

if I could say,

1:27:30

so in SQL based,

1:27:32

he suggested

1:27:33

me to use

1:27:34

locally installed,

1:27:35

yeah.

1:27:36

Locally,

1:27:37

uh,

1:27:38

locally,

1:27:39

uh,

1:27:40

maybe a local

1:27:41

correct

1:27:42

correct

1:27:43

correctly

1:27:44

conversations or history

1:27:45

and session

1:27:46

ID

1:27:47

everything

1:27:48

but how do we do it

1:27:49

externally?

1:27:50

Like,

1:27:51

um,

1:27:52

uh,

1:27:53

we need,

1:27:54

this

1:27:55

store and we

1:27:56

can use

1:27:57

use,

1:27:58

some,

1:27:59

we use

1:28:00

then only it will

1:28:01

work.

1:28:02

Okay.

1:28:03

Yeah,

1:28:04

and uh,

1:28:05

and uh,

1:28:06

okay, and another question is,

1:28:08

like,

1:28:09

Now we

1:28:10

the course

1:28:11

is

1:28:12

we've got

1:28:13

for vector embeddings,

1:28:14

the suggested ones are

1:28:15

pine cone or

1:28:16

and then

1:28:17

but I come

1:28:18

from a space

1:28:19

that deals in SAP.

1:28:20

So basically

1:28:21

I'm SAP developer and I came to know

1:28:23

that in SAP

1:28:24

space people are using

1:28:26

the HANADB

1:28:27

which is the primary database type

1:28:29

for SAP applications

1:28:31

and where

1:28:32

there

1:28:33

people

1:28:34

For HANA for

1:28:36

HANDB

1:28:37

in HANDB

1:28:38

of them

1:28:39

that

1:28:40

that's

1:28:41

but

1:28:42

but

1:28:43

they're

1:28:44

on-premise

1:28:45

HANADB in

1:28:46

there's a

1:28:47

cloud also

1:28:48

that

1:28:49

a

1:28:50

platform

1:28:51

that

1:28:52

they

1:28:53

create

1:28:54

so they had

1:28:55

something for a

1:28:56

cloud connector

1:28:57

or something for

1:28:57

DB where they were able to

1:28:59

create

1:29:00

embedings and

1:29:01

and store them

1:29:02

I'm

1:29:03

on-premise

1:29:04

DB in

1:29:04

try here but it's not

1:29:06

not allowing me

1:29:06

so I just wanted to ask

1:29:08

is it really

1:29:08

really regarding the DB or a kind of

1:29:11

middleware or something that allows you to

1:29:13

store embeddings in D.

1:29:14

That means in a way,

1:29:15

DB can store anything.

1:29:16

Yeah, DB can store anything.

1:29:18

Internally,

1:29:19

so they're fast queries,

1:29:20

chroma,

1:29:21

DMA, DMA, and these

1:29:21

built used

1:29:22

so they're

1:29:23

fast

1:29:23

can't

1:29:24

But on-premise HANA

1:29:26

database used

1:29:27

you're saying

1:29:28

you're saying?

1:29:29

No,

1:29:30

that

1:29:31

cloud

1:29:31

stored

1:29:31

on-premise

1:29:33

Hanna DIP in

1:29:34

there was

1:29:34

that

1:29:35

capability

1:29:35

not.

1:29:36

On-premise HANA DIP in.

1:29:37

No,

1:29:37

no.

1:29:38

No,

1:29:38

like that.

1:29:39

Uh,

1:29:40

a CIP or

1:29:41

a

1:29:42

portal,

1:29:43

where they, I mean,

1:29:44

for different customers,

1:29:45

you have the capability

1:29:46

to store your

1:29:48

database contents into into

1:29:50

cloud,

1:29:51

SAPE cloud.

1:29:52

Do you basically

1:29:53

hosted

1:29:54

AWS or Azure

1:29:56

database.

1:29:58

But that

1:29:59

Azure database

1:30:00

in there be multiple

1:30:01

database.

1:30:02

There are different database.

1:30:03

There are different database.

1:30:05

Which database they are using that we need to

1:30:07

figure out.

1:30:08

Getting my point.

1:30:09

Like on-premise

1:30:11

in the

1:30:12

database used

1:30:13

to store embedding,

1:30:14

and are they fetching

1:30:15

embeddings regularly?

1:30:16

Like, are they building a Rack

1:30:18

kind of system in order to do that, or like,

1:30:20

what is the U.S.

1:30:21

Yeah.

1:30:22

So it's basically

1:30:24

they are dealing with document grounding,

1:30:25

what we're doing in Rack actually.

1:30:27

They're calling document grounding or that

1:30:29

that same use are.

1:30:31

But

1:30:32

it's a kind of POC that my friend is doing and I came to

1:30:35

that he was able to store,

1:30:37

store, his team was able to store the embeddings in HANADB, that is in cloud.

1:30:41

First, they were on-premise on-premise

1:30:43

tried here.

1:30:44

Storing is possible.

1:30:46

Storing, I agree, is possible.

1:30:48

But the main thing is that are they able to do similarity search?

1:30:51

Did you check with them that are they able to do similarity search or not?

1:30:55

That similarity search, how much efficiently are they doing that matters, correct?

1:31:01

Yeah, so I did some research to that from my side.

1:31:05

And where, where you know,

1:31:06

the similarity search can't make

1:31:08

it.

1:31:09

Correct.

1:31:10

So that's the thing that

1:31:12

that's not,

1:31:13

that's not,

1:31:14

because you know

1:31:15

you,

1:31:16

you know,

1:31:17

we're in

1:31:18

classification of machine learning

1:31:19

algorithms

1:31:20

in many places

1:31:21

where embedding

1:31:22

store

1:31:23

but

1:31:24

embedding we can

1:31:25

store can

1:31:26

but if we

1:31:27

if we

1:31:28

need to

1:31:29

that we need to

1:31:30

that we need to

1:31:31

that we

1:31:32

actually we can

1:31:33

if we

1:31:36

search

1:31:37

so this

1:31:38

it's a extra

1:31:39

similar

1:31:40

to the

1:31:41

cost of operation right

1:31:42

no database

1:31:43

can normally do

1:31:44

similarity

1:31:45

search they should be built in such

1:31:46

that they are able to

1:31:47

support similarity search

1:31:49

that is that part

1:31:50

being into

1:31:51

they create DBJ

1:31:52

yeah

1:31:54

okay

1:31:55

I'll just try to know more because

1:31:57

in SAP space they're doing the same thing

1:31:59

and rolling document grounding

1:32:00

so we're back in

1:32:01

so we try to know

1:32:02

to know that similarity search

1:32:03

can support

1:32:04

database

1:32:05

Yeah.

1:32:07

I'll do it from myself.

1:32:09

Okay,

1:32:10

yeah,

1:32:11

we need to see that part.

1:32:14

Yeah, we need to see that part.

1:32:18

Go on, Pankch, what is a doubt you are having?

1:32:22

Hello?

1:32:26

Yeah, Punk,

1:32:32

we cannot hear you.

1:32:34

Go on.

1:32:35

Yeah,

1:32:36

my simple question is,

1:32:37

Sachum,

1:32:38

which we

1:32:39

we have

1:32:40

memory saved

1:32:41

agent through

1:32:42

uh

1:32:43

that

1:32:44

we're

1:32:45

if we're using

1:32:46

then

1:32:47

what we're

1:32:48

and

1:32:49

speed fast

1:32:50

of

1:32:51

If we

1:32:52

we have

1:32:53

we

1:32:54

can use

1:32:55

that we

1:32:56

can

1:32:57

that we're

1:32:58

we're

1:32:59

using

1:33:00

we're going to

1:33:01

we're

1:33:05

we use

1:33:06

so same thing

1:33:07

the same thing we

1:33:08

we're

1:33:09

in-memory

1:33:10

we're using

1:33:11

that we're

1:33:12

we can

1:33:13

connect

1:33:14

we can connect

1:33:15

but when we

1:33:16

we're

1:33:17

we're

1:33:18

we need to

1:33:19

so we're

1:33:20

we're in-memory

1:33:20

database use

1:33:21

but same

1:33:22

but same in

1:33:22

locally

1:33:23

install and we

1:33:24

we're

1:33:25

this same thing

1:33:26

so we can't

1:33:27

so like any

1:33:28

any external database

1:33:29

and partner with

1:33:30

and we can't

1:33:31

we can't use

1:33:32

memory

1:33:33

what is

1:33:33

the

1:33:34

the program

1:33:34

run

1:33:34

every time it

1:33:35

will load the memory.

1:33:36

It will not

1:33:37

be persistent.

1:33:38

If we're

1:33:39

persistent

1:33:40

we're

1:33:41

then we're

1:33:42

third-party database

1:33:43

use

1:33:44

like post-grey SQL and anything.

1:33:45

I think that

1:33:46

that part

1:33:48

I was making

1:33:50

basically

1:33:51

that

1:33:52

agents with

1:33:53

connectivity

1:33:53

that

1:33:54

database

1:33:55

because

1:33:56

because my database

1:33:56

is

1:33:57

that's why I asked

1:33:58

correct, correct.

1:33:59

So I think

1:34:01

I think database

1:34:02

a

1:34:03

big

1:34:04

and then

1:34:05

we're

1:34:06

and then

1:34:07

we're

1:34:08

we're

1:34:09

what

1:34:10

you're

1:34:11

you're

1:34:12

using

1:34:13

you're

1:34:14

I'm

1:34:15

on

1:34:16

hello

1:34:18

hello

1:34:19

hello

1:34:21

hello

1:34:22

hello

1:34:24

hello

1:34:26

I

1:34:27

I think

1:34:31

it later on

1:34:32

I think

1:34:35

can you hear me right?

1:34:36

Yes, you're audible.

1:34:37

Yeah, Koppel, I think we can start the quiz if you want to give a break you

1:34:42

can give and otherwise we can start a quiz and everything that is there.

1:34:46

Let's give 10 minutes break.

1:34:49

Okay, sure, sure I'll start that.

1:35:01

You know,

1:35:31

You know,

1:36:01

You know,

1:36:31

I guess

1:36:35

you're

1:36:36

I think

1:36:37

I think

1:36:38

I think

1:36:39

you're

1:36:40

me

1:36:41

I think

1:36:42

you're

1:36:43

Hello

1:37:01

I'm

1:37:03

you

1:37:04

I'm

1:37:06

I'm

1:37:08

I'm

1:37:10

I

1:37:11

You

1:37:13

Thank you.

1:37:43

Thank you.

1:38:13

Thank you.

1:38:43

Thank you.

1:39:13

Thank you.

1:39:43

Thank you.

1:40:13

Thank you.

1:40:43

Thank you.

1:41:13

Thank you.

1:41:43

Thank you

1:42:13

Thank you

1:42:43

Thank you

1:42:45

Thank you

1:42:47

Thank you

1:42:49

Thank you

1:42:51

Thank you

1:42:53

Thank you

1:42:55

Thank you

1:42:57

Thank you

1:42:59

Thank you

1:43:01

Thank you.

1:43:31

Thank you.

1:44:01

Thank you.

1:44:31

Thank you.

1:45:01

All right.

1:45:05

All right. So if there are no more queries, then we can move forward with feedback pool. Please stay back for a minor quiz.

1:45:31

Thank you.

1:46:01

Thank you.

1:46:31

Thank you.

1:47:01

I can see only.

1:47:05

I can see only half of the people have participated.

1:47:20

Others are there.

1:47:31

All right, so let's move forward.

1:47:44

I'm sharing my screen.

1:48:01

Either you can scan this QR code given over here, or you can just go to this website minty.com and enter this code.

1:48:20

I'm pasting this code in the chat as though.

1:48:31

Isn't my screen visible?

1:48:38

Let me re-share then.

1:48:52

I think half of you are not able to be.

1:49:01

Now it is visible, right?

1:49:16

In case you are not able to see the QR code, just go to this website Menti.com and enter this

1:49:21

code.

1:49:22

I have pasted this code in the chat as well.

1:49:30

All right, so let's get started.

1:50:00

So here is your first question.

1:50:07

What is the purpose of chat history and line chain agents?

1:50:11

And the options are to store previous conversation turns to execute Python code to create embeddings or to load documents.

1:50:30

And the correct option is, it is used to store previous conversation turns.

1:50:49

Let's have a quick look on the leader boom.

1:51:00

Moving on to the second question.

1:51:07

Which placeholder stores the tool execution steps during the current run?

1:51:17

And the options are chat history, conversation memory, agent scratch pad or session store.

1:51:30

And the correct option is agent to scratch back.

1:51:53

Moving on to the leaderboard, let's see how it looks like.

1:51:59

after the second question.

1:52:01

Buckle up for the third question, students.

1:52:10

Here it is.

1:52:15

What does optional is equals to true option allow in messages placeholder?

1:52:21

And the options are automatic database storage, multiple LLMs in one form,

1:52:26

unlimited chat history or an empty history,

1:52:29

on the first truck.

1:52:59

Let's look at the leader board now.

1:53:06

Moving on to the fourth question for the day.

1:53:13

Which placeholder is used to reserve space for previous conversation messages?

1:53:22

And the options are tool placeholder,

1:53:26

from template or memory slot.

1:53:28

slot.

1:53:32

And the correct option is P, messages placehold.

1:53:54

Let's have a look on the leaderboard now.

1:53:58

Moving on to the fifth question.

1:54:11

What should be depended first after calling in who function in manual memory mode and the options are human message,

1:54:22

AI message, system message or tool message.

1:54:28

The correct option is human message.

1:54:54

Let's see the scoreboard now.

1:54:58

Moving on to the sixth question.

1:55:11

In the automatic memory example, what is used as the key to separate users histories?

1:55:22

Order ID, input, session ID or output.

1:55:28

And the correct option is stationites.

1:55:47

Let's have a quick look on the scoreboard now.

1:55:58

Moving on to the seventh question.

1:56:10

What happens in a stateless agent and the options are.

1:56:16

Previous messages are restored permanently.

1:56:19

The agent remembers every conversation.

1:56:21

The agent automatically summarizes chats or every call starts with empty history.

1:56:28

and the correct option is D.

1:56:48

Stateless agent has every calls starts with empty history.

1:56:58

Let's move on to the scoreboard.

1:57:02

Finally, we have reached to the final question for the day.

1:57:19

And here it is.

1:57:23

There is in-memory chat message history stored and the option.

1:57:27

And the options are RAM, SQL database, vector database, or cloud stores.

1:57:33

And the correct option is RAM.

1:57:54

Let's have a look on the final score.

1:57:56

on the final scoreboard.

1:58:06

Congratulations, Sudansh.

1:58:08

So let's stop here for today.

1:58:10

We'll meet tomorrow.

1:58:12

Till then, bye-bye.