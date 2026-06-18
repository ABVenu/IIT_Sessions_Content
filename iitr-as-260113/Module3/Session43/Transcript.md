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

Hi,

21:01

Hi,

21:02

Hi, everyone

21:04

Hi, everyone.

21:05

Hi, everyone, very good evening to all of you.

21:23

and welcome to the lecture.

21:25

We'll start in a couple of minutes to people are still joining.

21:29

Warm welcome to you and sir as well.

21:34

So you can start with a new point.

21:53

Thank you.

22:23

Thank you.

22:53

Thank you

23:23

Thank you

23:53

Thank you

24:23

Thank you

24:53

Thank you

24:55

Thank you

24:57

Thank you

24:59

Thank you.

25:29

Thank you.

25:59

Thank you.

26:29

Thank you.

26:59

Thank you.

27:29

Thank you.

27:59

Hi, everyone, very good, very good evening, folks, am I audible to all of you?

28:17

Hi, everyone, am I audible?

28:20

Okay, great, good evening everyone and welcome to the class.

28:27

Sorry, I got a bit late.

28:29

I was in some other call for some time, yeah. Cool. So guys, if you remember, what did we do in the last class? What did we discuss in the last class?

28:40

Tell me. We discussed about debugging evaluations, correct? We can create eval. Dot jason file and write all the evaluation test cases in a JSON file. And then we saw that how can we run, how can we create results

28:58

dot CSV file. How can we analyze the data? How can we analyze the steps? Which tool is getting

29:04

triggered? What input we are passing to the tool? Not only that, everyone, we also added some kind of

29:09

monitoring logic. For example, let's say how much time every agent is taking. Remember that? This is what

29:14

we discussed in the last class. Now everyone, today's class is going to be the kind of a continuation of

29:19

the previous class. Today we will be talking about slightly more, you can say that, some theoretical

29:23

terms, right? Which you can consider, which you may consider, while

29:28

debugging the application. Everyone, clear? While debugging a land chain agent, while going

29:34

through the land chain agent, okay? Again, you might see some overlap of today's class with the previous

29:39

classes, but because these are the topics which are like this only, right? These are very easy topics.

29:45

The only thing is that there is no much practice required. I would say more practice you need for

29:51

building the agents. Okay. And for debugging, for testing, et cetera, if you know what we did in the last

29:57

class and if you can just follow that, that is more than sufficient. So today we are just going to

30:01

talk about some theoretical, conceptual terms and technologies, right? Tools and terms,

30:07

etc., which actually comes very handy when you actually talk about debugging. Okay? Mostly we are going to

30:12

have kind of a conceptual discussion today. I think for last maybe 10 to 15 in classes, we have been

30:17

constantly writing code, correct? Almost in, or not almost. In every class, we have written code,

30:23

right? Today, there will be no coding class as such. Today, we will just be kind of,

30:27

I will be doing some kind of discussion around debugging and iterating over the agents, right?

30:33

Let's get started.

30:36

So can everyone see my iPad screen?

30:43

Can everyone see my iPad screen?

30:47

Yes, okay. So now everyone, let's talk about the concept of debugging.

30:51

What is the meaning of debugging everyone?

30:54

I think this term we use a lot of time.

30:57

without even discussing this, tell me what is the meaning of debugging?

31:13

Debugging is everyone that if something goes wrong in your application, for example, let's say, if your tool or let's say if your agent is not giving you the expected output, it is failing somewhere, right?

31:27

it is not working as expected. Let's say it is refusing the answer. It is not

31:31

refusing the answer. It is calling the different tool, right? There can be hundreds of reasons

31:35

because of which your agent may fail. Now, in any of these scenarios, everyone, if the agent is

31:40

failing, there can be hundred different reasons for that failure. Finding at what particular place,

31:45

because in bigger applications, you will have a lot of code. Now, when you have so many code files,

31:52

so many lines of code, then it becomes very difficult for anyone to find.

31:57

out and to pinpoint where exactly the issue is, what wrong line of code you have

32:02

written or what you have missed, right? Because of which you are not getting the expected

32:06

output from the agent, because of which your agent is not working as expected. This process

32:12

of finding or pinpointing the exact place where the error is coming from, why your agent

32:18

is failing, why your agent is not working as expected, this process of finding and resolving

32:24

the bug in your application.

32:27

is called as debugging. So there's a very important term inside debugging is this bug.

32:32

Okay? This bug is the important term. Just look at this word bug. Bug. Bug means any error in your

32:37

code, any issue in your code. If your code is not working as expected, then what do you do, everyone?

32:42

You have to find out the root cause. You have to figure out the root cause and try to find the

32:48

resolution for that. That why this particular code is failing. This process is called as debugging.

32:52

Now everyone, if you remember, in the last class, we saw that. If you're solving some mathematical

32:57

problem. If you're solving some DSA problem. Can you simply say that, how can you debug an application?

33:02

If that application is a simple input output application, that for this input, you are expecting

33:08

this output. Correct. If this output is coming, your application is working fine as expected. If this

33:14

output is not coming, your application is not working as expected. Simple.

33:19

Correct. This is the simplest understanding that we can have, right? This is how you identify

33:24

issues in traditional applications.

33:27

which do not have a lot of workflows. But in agentic AI application, everyone, there are a lot of

33:31

flows that you have, right? There is a complete workflow, right? So let's say user gives the input,

33:36

this input, this input passes via LLM, then LLM identify as a tool, then you pass some input to this tool,

33:42

this tool is returning some output, then this output we might be using as an input to another tool,

33:46

and there might be hundreds of such tools, right? And then everyone finally you are giving the

33:51

answer to the user, right? This is how the complete journey is looking like. Now, if you

33:56

you have to debug such a complex workflow, obviously you cannot just expect input versus

34:01

output comparison. Correct? You cannot simply say that for this input, this should be the output. Because

34:06

your tool or your agent can fail because of hundreds of reasons. What if data is not correct? What

34:11

if your agent is refusing the answer? If, even if let's say it is a valid question, right? Even

34:16

if user is asking a valid question, still your agent is refusing it. We need to figure out why our agent

34:23

is refusing it. Is the tuning wrong? Is the data wrong?

34:26

or is the prompt wrong? Or is the LLM not able to understand the query?

34:32

Again, for this particular error also, for this particular issue also, there might be like multiple

34:37

reasons for that. So as a software engineer, we need to identify what error your code is giving,

34:43

what bug is there, what is the bug in your application, and because of that bug, like why that bug is

34:48

happening, what could be the root cause of that bug and what not? Sounds good to all of you. Everyone clear?

34:55

This is called as debugging. Now, when agent fails everyone, the problem, we cannot simply

35:01

say that the model is bad. Can we simply say that? Because LLM is not good. That's why my agent is not

35:05

working fine. Is that the solution, everyone? Is that the solution? Not at all. You cannot simply say

35:12

that your agent is not working because your LLM is bad or your model is bad. Model you can change. That is

35:17

not an excuse. Now you have to figure out that what exactly went wrong. What exactly is not working

35:23

out. Prompt is wrong. Variables are wrong. For example, some input, some wrong

35:28

you are passing to the tool because of which tool is not working as expected. Tool does not

35:32

have proper API keys, right? Tool is taking a lot of time for calling the APIs. Multiple

35:38

reasons could be there and we need to figure out these exact reasons. Okay. Now, this is what

35:45

we are going to discuss everyone and let's move ahead. Now when there is something called as failure

35:50

class. While debugging, you will

35:53

come across, you may come across this term called as failure class. Now, what is

36:03

this failure class, everyone? Let me write it down. Failure class is nothing but is a category of failure class.

36:09

It is a category of. It is a category of. It is a category of. It is a category of. It is a category of.

36:23

defect responsible for an incorrect agent response.

36:53

wrong response. Now you identify that, what is the issue because of which your agent is not

37:00

working as expected. That is what is called as failure class. Now, honestly, tell me everyone,

37:04

does it really matter whether you know this term or not? Honestly, tell me. If you want,

37:08

if you call it failure class or anything else, it does not matter. These are just few terms and

37:12

technologies everyone with respect to the agentic AI application, which you should be aware of.

37:18

Although, honestly, these theoretical terms are not very important. Right. The only thing

37:23

that you need to understand is maybe for, let's see, if you're reading some documentation,

37:27

there you see the term failure class or some terms that we are going to see in today's class,

37:31

so that you at least feel familiar, that these are the terms that we at least we know,

37:35

at least we have heard about them. That is the only reason. Okay. This is what a failure class is.

37:40

Now let's talk about everyone, common land chain agent failure cases. Okay. What are the

37:45

possible scenarios? What are the possible issues that can happen? Okay. So some common

37:53

Langchain agent, some common langchain agent,

38:03

failure classes. Okay? So let's try to understand this. It means that what are the common errors that you are,

38:20

what are the common errors or common issues you may face while building an agentic

38:26

AI application using Langchain, right? First of all, everyone, the most common one is wrong

38:32

tool selection. Everyone aligned with this?

38:40

Wrong tool selection. Is everyone aligned? Is everyone aligned? That you selected the wrong tool

38:45

tool, which is not expected. Let's say if, let's say, you have to get the order status.

38:50

So ideally, you should make a tool call to get order status. If you're making a tool call, let's say,

38:55

maybe some calling the weather API, etc., then it is a wrong tool selection. What could

38:59

be the possible reasons of wrong tool selection, everyone? Let's say if user is asking about the return

39:05

policy and let's say agent is calling the tool of, let's say, get ticket status.

39:11

Completely wrong. What could be the possible reason of a wrong tool selection?

39:15

me everyone if we have not given the tool description properly absolutely correct

39:23

if the tool name is incorrect tool description is not up to the mark right that could be the

39:28

potential reasons of wrong tool selection it means that it is very very important you give a better

39:33

a good tool name a descriptive tool name and the tool description is good enough okay tool description

39:40

is detailed enough okay now everyone other reason could be let's say

39:45

missing tool call first we saw that the tool itself let's say you are calling a wrong

39:55

tool but here everyone if if let's say the tool is not itself getting called okay so agent is answering

40:01

without even tool call again everyone it means that your prompt might be missing correct inside the

40:07

prompt also right we have to write it down right that these are the available tools use this tool for this

40:12

use case use this tool for this use case right if let's say for example

40:15

if you miss writing a particular something about a particular tool in the prompt obviously your

40:21

LLM will not be able to call that particular tool okay everyone clear missing tool call these are the

40:28

potential issues for that then everyone we have let's say third issue could be this one bad tool arguments

40:37

it means that you're calling the tool but arguments you are not passing correctly what is the

40:41

meaning of arguments everyone the input that you pass to the tool okay

40:45

So to the tool, whatever tool you are calling, that would expect some input,

40:50

order ID, ticket ID, whatever, right?

40:52

If you are not calling the tool with the correct input parameter, obviously you will not get

40:56

expected output.

40:57

You are not, you will not get expected output.

41:00

Okay?

41:01

Then everyone, fourth most common issue could be weak retrieval.

41:14

This is very important.

41:15

And tell me, what is the meaning of weak retrieval?

41:20

What could be the meaning of weak retrieval?

41:32

Tell me everyone, think about it.

41:36

Very good, Ravi.

41:38

Ravi has already given the answer.

41:41

Now, guys, if you let's say, if you are building a rag application, a rag application, a rag application, a rag

41:45

agentic rag, a rag with agent.

41:47

Then everyone, you have to retrieve the documents or chunks, relevant chunks from the database.

41:52

If your retrieval is not up to the mark, can I say that your tool, basically you are retrieving

41:57

wrong data or the information is not sufficient?

42:01

Now, there are two reasons for that.

42:02

That first reason is, first reason is what?

42:11

Folks, just give me a second, I'm getting a call.

42:15

Hi.

42:45

got a call. Yeah, we can continue now. So the fourth, everyone is weak retrieval.

42:51

Now, in this weak retrieval, everyone means that, that if you're building a, if you're building a rag-based

42:56

application, to answer the query, you have to make a call to the database, fetch the relevant documents

43:01

with the help of similarity search. You perform similarity search, you give the K value that you want

43:06

top three documents, top four documents, top five documents. Now, if the document that you're,

43:11

the chunks or the documents that you're retrieving, if those.

43:15

documents are not having the proper information. Then obviously everyone, your final

43:21

answer is not going to be the correct answer. Correct everyone? So this could be one problem of weak

43:27

retrieval. Now, what could be the reason of weak retrieval? First, everyone is that the documents itself

43:32

does not have relevant data. Guys, if the documents does not have relevant data, then you cannot expect that

43:39

when you're retrieving, magically you will get all the data, right? So you need to make sure that the

43:43

documents that you're inserting inside the system, those at least, those are up to the mark.

43:47

You have enough information inside those documents. Once you have inserted the proper documents

43:53

inside the system, now when you are retrieving, you are performing similarity search. Now, everyone,

43:58

quite possible that the K value is too high or too low. For example, if you take, let's say,

44:01

K value is equal to 1, you might not get enough information only from the first chunk, because similarity

44:07

search only works on the cases of probability. It cannot give you the exact answer, word to word search.

44:13

Correct, everyone? So whenever you are performing similarity search, you need to make sure

44:17

that you are giving enough room for getting the complete context. Are you guys getting this

44:22

point? Right? So whenever you are not able to retrieve the correct document, the relevant context from

44:28

the rag application, try to change the type of search. At least do the comparison that what kind

44:34

of information you are getting for similarity search. Then another approach that you can use is

44:37

MMR search. Also try to change the K value. K value is equal to three. Generally, three to five.

44:43

works best most of the times, but you can play around with this, play around with this

44:47

if you have a problem of weak retrieval in your application. Is everyone clear with this?

44:54

Everyone clear with this? Okay. Then everyone, other issue could be hallucinated answer.

45:13

Now, what is the meaning of this, everyone? Hallucinated final response. This, I would say

45:18

up to some extent, hallucinated final response is somewhat related to weak retrieval only. Can we

45:24

say that? It is kind of related to weak retrieval only. That if your retrieval is not good,

45:28

if you're not getting enough information, even in a non-rag application, if your LLM does not

45:34

know the context about the query, still it can answer you maybe the wrong information with more

45:39

confidence. This is hallucination answer. Hallucinated final answer.

45:43

Right? Then everyone, there is one problem which becomes very, very, I would say,

45:49

very, very prominent on big, on high scale, right, when you have a lot of users. But is it possible

45:53

even with grounded responses? Up to some extent, yes. If you're, let's say, if your retrieval is

45:59

weak, it means that you are not able to fetch the relevant context from the RAG database.

46:04

Still, let's say you don't get enough context, right? The retrieval is weak, but still you are trying

46:09

to give an answer. That can be hallucinated answer.

46:13

Right? If you're not able to retrieve the proper data from the rack. Right, Ravi?

46:18

Then still if you are trying to give the answer, because see, how would you know? Right? If you have

46:23

retrieved, you executed the similarity search, you got three top three chunks. Now you don't know

46:29

that whether this is a weak retrieval or it is a strong retrieval. Assume that if it is a weak retrieval,

46:34

then you give this context to the LLM, LLM will try to give you the answer based on this context only.

46:40

Correct. If this context itself is not up to the mark,

46:43

obviously the final answer will also be not up to the mark. It may be hallucinated. So this is something

46:49

that we get to know after multiple feedbacks from the user. Let's say, for example, again,

46:54

the human in the loop will come into the picture. You will gather the feedback. And if you start getting

46:59

this feedback multiple times, that a lot of users are complaining that answers are irrelevant.

47:05

Then you will come back and you will see those queries. And then you will identify that, yes,

47:09

the answers are hallucinated. We are not, we are not able to retrieve the problem.

47:13

context from the because of weak retrieval. Then you try to find out the reason for that.

47:18

Okay. Now coming to the next common error, everyone, which becomes very, very important at a big scale,

47:26

at a high scale, that is over refusal or under refusal. Would you try to guess what this means

47:34

either your application is doing over refusal or your application is doing under refusal. Any guesses,

47:43

could be the meaning for this. Over or under refusal? Any idea?

47:55

Guardrails are not optimized. Can you explain that? What is the meaning of refusal, by the way?

48:01

What is the meaning of refusal?

48:08

Refusal means that your query is getting rejected. Correct? You have a

48:13

set some guardrails that, okay, I will not, you have given an, you have given a restriction

48:18

to your agent that don't answer any unnecessary queries. Don't answer any unrelated queries. Let's say

48:24

if you are building a chatbot agent for a, for Masai, let's say. And if someone is asking any

48:29

question which is not related to technology, teaching, etc, etc. Masai batch, don't answer it.

48:34

That is the meaning of refusal. If you have not, you have not given proper guard railing to your agent,

48:41

can it do over-refusal? Can it reject a query even if it is related to the application,

48:49

related to the company? It can still reject, right? Under-refusal means that some of the queries

48:56

which your agent was supposed to reject, but still it is answering it. It means that under-refusal.

49:04

Now, very tricky situation. That how will you find out that under-refusal and over-refusal?

49:08

Right? Again, everyone, you have to run your application for a long period of time in the

49:12

production environment. Keep on gathering the feedback from the user and then try to identify that

49:19

whether your application is over-refusing the queries or it is under-refusing the queries. Then you'll

49:28

have to work on the context or you will have to work on the restrictions that you are putting inside

49:33

the prompt. Does it make sense to all of you? Absolutely. Absolutely, Abhishek, very good.

49:38

Are you guys getting this point?

49:43

So, over-refusal means agent refuses to answer even if it is a relevant question.

49:49

Under-refusal means that agent answers are unsupported or out-of-of-domain questions as well.

49:56

Okay? So I think let me write it down. Under-refusal means

50:08

answers. Under refusal means agent answers, unsupported or out of domain, agent answers. Okay? Over-refusal means that agent is refusing to answer.

50:38

refusing the queries.

50:45

We can say that agent refusing even the related queries.

51:07

which were supposed to be answered, which were supposed to answer.

51:37

The seventh one is over tool calling, right?

51:41

Let's say if you got stuck in a loop, looping, or excessive tool call.

51:54

I think everyone, this is something that we need to make sure as a software engineer while writing

51:59

the code, that you are not calling the tools unnecessary.

52:02

Right? Sometimes everyone, if you remember in one of the classes, we, not in one of the classes, I think,

52:07

two, three times we discussed about max iterations.

52:10

Absolutely, very good, very good, uh, I was about to come to that point.

52:14

If you remember, we talked about max iterations.

52:16

Sometimes everyone, if the tool call is failing, we have to retry, right?

52:20

Now, if everyone, let's say the tool is unavailable, the API is unavailable.

52:24

If you keep on retrying, retrying, retrying, retrying, then you will fall into infinite loop.

52:28

So you need to make sure that you are properly putting the limit, how many times you should call

52:33

the tool. Otherwise, you may fall into the trap off, you may fall into the trap off, you may fall into the

52:37

of infinite loop.

52:39

Does it make sense to all of you?

52:42

Correct?

52:45

Then everyone, this is one issue, seventh point, and the eighth point is the eighth point is,

52:50

the last point, that whether your tool response is slow, slow response.

52:56

For this, everyone, you need to make sure that you are measuring the time properly.

53:00

And you should put alarms on that.

53:02

This is called as monitoring or observability.

53:07

observability.

53:09

Now, what is the meaning of observability or monitoring everyone?

53:12

What do you do is, in the last class, do you remember that we measure the time?

53:16

Correct?

53:17

At the start of the tool call, measure the start time, measure the end time.

53:20

The difference is the amount of time that your tool has taken.

53:24

What you can do everyone is, you can now see if, let's say, millions of people are using squeaky chatbot every day.

53:30

Is it manually possible for any company to monitor that how much time our agent is taking,

53:36

how much time it should take, how much time it should not take.

53:39

Which query it is taking, for which query it is taking more time, for which query it is taking less time.

53:44

Is it practically possible to monitor this manually?

53:47

When you have millions of customers every day?

53:51

Is it possible to manage, to observe this manually? Not practical, it is not possible.

53:56

So what do you do everyone? There are a lot of tools comes in the market.

54:00

There are a lot of companies which have built these technologies for observability.

54:06

What do you need to do is everyone, whenever you, let's say, for example, you measure the time at the beginning, you measure the time at the end.

54:11

Whatever is the difference, everyone, for every request, for every user, for every query, they will start plotting that on a graph.

54:19

Let's say, this is the graph.

54:22

Let's say, these are the request and this is, let's say, the time.

54:26

So what you do, everyone is, you will keep on drawing the graph.

54:30

Let's say this request took this time, this time, this much time, this much time, this much time, and so on.

54:35

Okay.

54:35

So let's say, on an average.

54:36

this much time your agent is taking.

54:38

And let's say everyone assume that.

54:39

I'm just giving you some small glimpse of it.

54:43

Let's say this is the healthy range.

54:44

Okay?

54:45

This is how your agent is, this much time your agent is taking, right?

54:49

So I'm just drawing this like this.

54:52

So let's say this is how your agent is taking the time.

54:55

And let's say everyone, this is a healthy range.

54:57

Okay? This is a healthy range.

54:59

Let's say this, between this and this, it is a healthy range.

55:01

This is a regular range, how much time it takes.

55:04

But everyone at some point of time.

55:06

If, let's say, something went wrong in your system.

55:09

Suddenly, let's say, if the time start increasing, increasing, increasing, it means that till this

55:14

point of time, everything was okay.

55:16

But now after this point of time, something went wrong.

55:19

For example, let's say your database is over occupied now.

55:21

And your database queries are becoming slow.

55:23

Your vector database has become slow.

55:25

Your agent is making excessive tool calls because of which your agent has started consuming more

55:29

memory, more time.

55:31

And there can be hundreds of different reasons.

55:33

Don't you think, everyone, this is how you can monitor it.

55:36

And everyone, what we do is, what we do here is, let me draw in this way.

55:41

This is the healthy range of everyone.

55:43

Now, everyone, there are automatic tools.

55:46

There are a lot of companies which are working in this domain.

55:48

You can set an alarm that, let's say, if the memory utilization, the time utilization,

55:53

if it is crossing a particular threshold, let's say, if let's say time goes beyond a particular

56:04

threshold, then raise an alert.

56:10

So, raise an alert to the manager of that team or software engineer of that team.

56:16

So that once this alert has been raised, you will automatically get to know that your agent or

56:22

your application is taking more than expected time.

56:24

Now, you should check this right now.

56:27

Yes and everyone?

56:27

It means we can create a cutoff type, absolutely correct.

56:29

For example, let's say the healthy range is maybe between, let's say, 400,000.

56:34

or let's say maybe one to two seconds.

56:36

One to two seconds is the healthy range.

56:38

Now, if your agent is taking between one to two seconds, good enough.

56:43

But if, let's say, at three seconds, three seconds is not at all healthy.

56:47

Now, everyone, you should raise an alert at three seconds that your agent is taking more than

56:51

expected time.

56:52

Your agent is taking more time.

56:53

Please log in and check right now.

56:55

Now, everyone, this is level one alert.

56:57

Now, most of the companies, most of the software engineers, they misses level one alert.

57:02

They don't give a lot of.

57:04

importance to level one alert.

57:06

Now everyone, if, let's say this was an intermittent issue, if this was a temporary issue,

57:12

will the time come in the healthy range after some time?

57:15

Let's say something like this.

57:16

Again, it will come in the healthy range.

57:18

If it was a temporary issue.

57:20

But everyone, if it is a permanent issue, the time will keep on increasing, increasing, increasing.

57:25

At five seconds, let's say, everyone, at five seconds, you will put level two alert.

57:29

This is, this was.

57:34

Level 1 alert.

57:36

Here, everyone, you will raise level 2 alert.

57:42

Here you will raise level 2 alert.

57:45

Are you guys getting this point?

57:48

Correct.

57:50

Now everyone, most of the software engineers, most of the teams,

57:53

they give a lot of importance to level 2.

57:55

If level 2 also gets missed everyone at, let's say, maybe 6 seconds or 7 seconds,

58:00

you can put level 3 alert.

58:01

And this is the final alert that you have.

58:03

Right?

58:04

And this generally goes to the manager, their managers, and whatnot.

58:08

Is everyone clear?

58:09

Folks, yes or no?

58:11

This is how you monitor.

58:13

And these kind of graphs, everyone, you don't only have only for time, all the critical components.

58:19

For example, what do you need to observe?

58:21

What all the factors, we should observe, right?

58:25

We should observe the time.

58:27

Time is very important that you should not, your agent should not take more than expected time.

58:32

You should observe memory.

58:34

If your agent is consuming more than expected memory, don't you think soon,

58:38

your agent will go out of memory, and once what happens if your phone or your mobile phone,

58:43

your laptop goes out of RAM, if RAM is overconsumed, your laptop starts hanging, right?

58:49

Your laptop starts, stops responding.

58:52

Your laptop stops responding.

58:53

It means that everyone, if your application stops responding, it means that it will not be able

58:57

to take more requests.

58:59

Again, a very critical thing.

59:00

Okay.

59:00

And there are many more things as well, time, memory, number of things.

59:04

failures, right?

59:13

Number of failures and whatnot.

59:16

Is everyone clear?

59:19

So these are the things that we need to observe everyone.

59:25

Okay.

59:29

Okay.

59:30

Now one thing, everyone, that one term, that, uh, one term that, that comes

59:34

multiple times that might come when you are going to implement these things in the future

59:39

or when you are going to read any article, that final for debugging everyone, although we have already

59:48

discussed this term indirectly, let me just introduce the term.

59:52

Now, while debugging everyone, there are two things that you can debug.

59:55

One is, you can just debug the final answer versus final answer.

1:0:04

answer versus the trajectory answer.

1:0:11

What is the meaning of this?

1:0:12

Can you try to guess the meaning of final answer versus trajectory?

1:0:18

While debugging, you need to make sure that whether you are checking the final answer or the trajectory.

1:0:27

Very good, Sandia.

1:0:28

Absolutely.

1:0:29

Trajectory means everyone, the path, the step by step path, or the way, the way, the

1:0:34

the complete workflow that our agent followed, absolutely correct, right?

1:0:38

So, trajectory means the path are agent followed.

1:0:53

Is this point clear to all of you?

1:0:58

Everyone clear?

1:1:01

Okay, cool enough, cool everyone, good enough.

1:1:04

Then everyone, we have the next step, which is remediation strategy by defect category.

1:1:11

Okay?

1:1:11

So, for example, everyone, that how would you, I will just reiterate the same thing.

1:1:15

We have already discussed most of these pointers.

1:1:18

In fact, I will copy paste also.

1:1:22

Yeah, I'll add it in the notes also.

1:1:24

Basically, how do you solve a particular problem?

1:1:28

For example, wrong tool selection.

1:1:30

What can you do?

1:1:31

Improve the tool name, improve the tool description.

1:1:34

make more examples and like give more examples and make your system prompt better.

1:1:41

If your agent is calling wrong tool, what can you improve, how can you make it better?

1:1:46

Improve the name of the tool, improve the tool description, like check the system prompt,

1:1:52

give more examples that for what kind of queries you should make this tool call.

1:1:57

This is one issue.

1:1:58

Bad tool arguments, right?

1:1:59

You need to improve the tool schema and give proper input parameters.

1:2:04

Missing tool call, right?

1:2:05

Then everyone, if the tool call is missing, how can you make this better?

1:2:10

Missing tool call, how can you make this better?

1:2:13

How can you solve this kind of problem?

1:2:15

If your agent is missing a tool call, how can you solve this problem?

1:2:24

Tell me, everyone.

1:2:25

What could be the reason of a tool missing call?

1:2:31

Tell me, tell me, me everyone, this is how you become.

1:2:34

an AI engineer.

1:2:35

Optimize tool name, tool description, system prompt, absolutely correct.

1:2:38

What else?

1:2:40

Absolutely correct?

1:2:42

Sometimes everyone, small, small things can make a lot of difference because we don't know how your

1:2:47

LLM is going to perceive the query.

1:2:49

Yes or no?

1:2:50

We can just, we are just predicting it that this is how LLM should perceive the query.

1:2:55

But everyone, for example, one very small reason could be absolutely,

1:3:00

enforce proper flow, tool name, tool, not available, tool description, everything is correct.

1:3:04

that we discussed earlier also.

1:3:06

One thing could be, let's say inside the system prompt, don't you think you need to add a line,

1:3:11

must call this tool for these kind of queries.

1:3:15

Correct or not?

1:3:17

You must call this tool for these kind of queries.

1:3:22

Guys, yes or no?

1:3:23

Folks, yes or no?

1:3:24

Sometimes just adding the word must can make a difference.

1:3:28

Who knows?

1:3:29

Sometimes adding one more example can make a difference.

1:3:32

For example, you have just given one example.

1:3:34

But let's say must call this tool for this kind of queries.

1:3:38

Let's say your LLM is not able to perceive that properly.

1:3:41

Correct?

1:3:42

Correct?

1:3:44

Makes sense everyone.

1:3:45

LLM is not able to perceive that one example properly.

1:3:47

You add one or two more examples, right?

1:3:49

You add maybe two, three more examples.

1:3:51

And suddenly your LLM will start making a tool call.

1:3:53

Because now you have given proper context to the LLM

1:3:55

that for what type of queries you should make this tool call.

1:3:59

Must is a keyword in the system problem?

1:4:00

No, no.

1:4:00

Must is not a keyword.

1:4:01

Must is just a normal word.

1:4:03

Sometimes.

1:4:04

When you are using the must word, it means that you are enforcing the LLM to call this tool for this use case.

1:4:10

Makes sense, Sharia?

1:4:13

Okay.

1:4:14

For weak retrieval, everyone, if your application is suffering with a problem of weak retrieval,

1:4:20

how can you solve this?

1:4:22

How can you remediate this?

1:4:26

K value, tune the K value, try to change the K value, try to change the K value, try to change the type of the search, try to put some filters also.

1:4:33

So, in Rack class, do you remember that we added some metadata filters, the type of document,

1:4:38

the name of the document, et cetera, right?

1:4:39

You can use the metadata filters to make sure that you are actually searching the correct set of

1:4:44

documents.

1:4:45

Small, small things can make big differences.

1:4:47

Hallucination, right?

1:4:48

Now, if your application is giving you the hallucinated response, then you can add some grounding

1:4:53

rule that answer only from retrieved tool.

1:4:57

Don't answer out of the box.

1:4:59

Don't answer on your own.

1:5:00

Just answer based on the tool call,

1:5:03

based on the database call, whatever retrieved context you have.

1:5:07

If your retrieved context is not good enough, reject the answer.

1:5:11

Refuse the question.

1:5:12

Refuse the query.

1:5:13

Correct, everyone?

1:5:15

Is everyone clear?

1:5:17

Then everyone, how can you solve the over-refusal process, issue?

1:5:22

Over-refusal.

1:5:24

If your application is overly refusing the queries, how can you solve it?

1:5:30

You can?

1:5:31

If some restrictions you have.

1:5:33

have given, right? Those restrictions, you might have to strict. Make it strict, right?

1:5:39

Make sense. Set strict rules, guardrails, right? Then under refusal,

1:5:45

under refusal means that some of the rules might not be added properly in your application,

1:5:52

right? In your prompt. Again, both of these things can be solved using setting correct rules.

1:5:57

Whether you might have to relax the rules, you might have to make them even more strict.

1:6:02

Excessive tool calls.

1:6:03

Add max iterations, right?

1:6:05

Now, define the proper limit on the tool call, that how many times we should call the tool.

1:6:11

High latency, everyone.

1:6:12

If the time, let's say, if your, let's say, if your agent is taking more than expected time, then what can you do?

1:6:24

Reduce the number of, reduce the number of unnecessary tool costs.

1:6:28

Reduce the number of unnecessary retrievals that you are making.

1:6:31

Right?

1:6:31

Try to remove unnecessary.

1:6:33

things, right? Also, everyone, you can add some cash logic. Everyone knows a basic thing about

1:6:38

cash. Everyone knows some basic thing about cash. That what is cash? You can add some

1:6:43

caching logic also. That can also improve your latency, right? That can also make your timing better

1:6:49

that how much time your agent is taking to answer a particular query. Then everyone, if your infrastructure

1:6:55

cost is very high, okay? Let's say if your agents are running absolutely fine, but the cost is

1:7:00

very high. How can you optimize the cost?

1:7:02

how can you optimize the cost?

1:7:13

Let's see.

1:7:15

LLM selection dynamically, very good point.

1:7:18

Limit the number of tool calls.

1:7:19

Very good.

1:7:21

How can you optimize the cost?

1:7:24

LLM is very important thing, right?

1:7:25

Because maybe most of the time, most of the cost, you are spending in LLM call.

1:7:30

If you are not using,

1:7:32

If you're using already a very advanced model, but your use case is not that advanced,

1:7:37

then why you are wasting money on an advanced model?

1:7:40

Move to a cheaper model.

1:7:42

Now instead of using just one model, you can select the models dynamically based on the type

1:7:47

of query.

1:7:48

If the query is very unique, very complex, you can use a better model.

1:7:52

If the query is very simple, you can use cheaper model.

1:7:55

What else, everyone?

1:8:02

What else could be the problem?

1:8:03

Better context, prompt, caching, ideal top K chunking.

1:8:07

Very good point.

1:8:08

Right?

1:8:08

Don't you think, everyone, like if you are passing a lot of data inside the prompt, then also the

1:8:12

cost will be very high because cost is directly measured by the number of tokens.

1:8:16

Correct?

1:8:17

How many tokens you are consuming?

1:8:18

If you're consuming more number of tokens, then you can make the prompt size better.

1:8:23

Right?

1:8:23

You can improve your prompt size.

1:8:25

If the prompt is very big.

1:8:27

Make the context size better.

1:8:28

Let's say if you are passing, let's say, two very big.

1:8:32

files inside the context to the LM.

1:8:34

Obviously, LLM is going to take a lot of time and it is going to cost a lot because it will have

1:8:39

to go through all the files.

1:8:40

So only provide relevant context inside the prompt so that you are not passing any irrelevant data

1:8:45

to the prompt so that the cost will come down.

1:8:48

Are you guys getting this point?

1:8:52

Use smaller chunks.

1:8:53

Very good.

1:8:54

If the chunks are small, then you will pass smaller chunks to the LLM and obviously the cost will be

1:9:00

improved.

1:9:02

Let me share this entire thing with all of you.

1:9:06

Let me add this in the notes.

1:9:32

What upend?

1:10:02

Why it is not copying?

1:10:18

No.

1:10:32

is what we have discussed, that how can you solve a particular problem in AGNTKI?

1:10:37

Sounds good, everyone.

1:10:41

Okay, so can we take a quick break at the moment? So it's 9, 855, almost 9. So let's take maybe a 15

1:10:48

minutes of break. Let's meet, let's reconvene at 9pm. In the meantime, you can go through the notes

1:10:54

as well. I am sharing the link with all of you. And then we will continue our discussion. Again, everyone

1:10:58

today's class is very small, like very basic class, I would say, as, as

1:11:02

compared to what we have discussed in the previous classes. They were very advanced classes.

1:11:06

Today's classes, just like you can say that cherry on the top of the previous classes. Why it is not

1:11:10

creating the link? Okay, anyways, everyone, I'm leaving this on the screen. It is not able to create

1:11:14

the links for some reason. See you after the break, everyone.

1:11:32

Thank you.

1:12:02

Thank you.

1:12:32

Thank you.

1:13:02

Thank you.

1:13:32

Thank you.

1:14:02

Thank you.

1:14:32

Thank you.

1:15:02

Thank you

1:15:32

Thank you

1:16:02

Thank you

1:16:32

Thank you

1:17:02

Thank you

1:17:32

Thank you

1:18:02

Thank you

1:18:32

Thank you

1:19:02

Thank you

1:19:32

Thank you

1:20:32

Thank you.

1:21:02

Thank you.

1:21:32

Thank you.

1:22:02

Thank you.

1:22:32

Thank you.

1:23:02

Thank you.

1:23:32

Thank you.

1:24:02

Thank you.

1:24:32

Thank you

1:25:02

Thank you

1:25:32

Thank you

1:25:34

Thank you

1:25:36

Thank you

1:25:38

Thank you

1:25:40

Thank you

1:25:42

Thank you

1:25:44

Thank you

1:25:46

Thank you

1:25:48

Thank you

1:25:50

Thank you.

1:26:20

Thank you.

1:26:50

Thank you.

1:27:20

Thank you.

1:27:50

Thank you.

1:28:20

Thank you.

1:28:50

Thank you.

1:29:20

Thank you.

1:29:50

Thank you

1:30:20

Thank you

1:30:50

Thank you

1:30:52

Thank you

1:30:54

Thank you

1:30:56

Thank you

1:30:58

Thank you

1:31:00

Thank you

1:31:02

Thank you

1:31:04

Thank you

1:31:06

Thank you

1:31:08

Thank you.

1:31:38

Thank you.

1:32:08

Thank you.

1:32:38

Thank you.

1:33:08

Thank you.

1:33:38

Thank you.

1:34:08

Thank you.

1:34:38

Hi, everyone. Am I audible?

1:34:41

Sorry, sorry, folks.

1:34:45

I'm getting repetitive calls of my work today.

1:34:49

I think this happened last week, right?

1:34:52

That when I was not available to take one class, when did this happen?

1:34:58

I think Monday, right?

1:35:01

Monday, Wednesday.

1:35:02

Correct.

1:35:03

That is the only reason that nowadays the work has increased a lot, right?

1:35:07

And yeah, that's the only reason I was getting a call.

1:35:12

Repetatively, I was trying to avoid it, so I thought that let's take it for five minutes, but somehow it got extended.

1:35:19

Okay, no worries.

1:35:20

Anyways, we have lesser content today.

1:35:23

So the next thing, everyone, that we are going to talk about is something called as prompt patching.

1:35:29

Again, everyone, you, the meaning you already know.

1:35:33

The only thing is I'm just introducing the concept, the term, right?

1:35:37

the meaning you already know.

1:35:38

What do you think prompt patch is?

1:35:41

Just you apply patch.

1:35:44

Do you know the meaning of patch, by the way?

1:35:47

Patch is a common term that you use at multiple places in software development.

1:35:51

Patch is just the difference, the delta, right?

1:35:54

If you are making some improvements, you are making some changes, right?

1:35:58

So everyone, if you make some changes inside the prompt, you are adding some restriction,

1:36:03

you are removing some restriction, you are making some restrictions stricter.

1:36:06

a stricter. That is called as prompt patch. Simple, right? Everyone clear?

1:36:12

If you just quick, if you just make some fixes in the prompt, which is, that is called as prompt patch.

1:36:19

Then everyone, there is some term called as tool patch. There is a term called as tool patch.

1:36:27

If you make changes in the tool, right, if you change the tool description, tool name, tool output, tool input, tool

1:36:33

a tool structure output, what not.

1:36:35

That is called as tool patch.

1:36:37

Makes us everyone?

1:36:39

Okay?

1:36:40

Then there is new term which is called as retrieval tune.

1:36:44

Retrieval tune.

1:36:48

Retrieval tune.

1:36:53

What is the meaning of retrieval tune?

1:36:55

You want to tune the retrieval.

1:36:59

That if you are trying to get the data from the retrieval,

1:37:02

the retriever, but the data is not up to the mark, the context is missing.

1:37:07

Then what do you do?

1:37:08

You try to tune the retrieval process by changing the K value, by changing the similarity.

1:37:13

Basically the search algorithm, right?

1:37:16

Changing the chunk size, etc.

1:37:18

Make sense everyone?

1:37:20

Okay?

1:37:22

Everyone clear?

1:37:24

Okay.

1:37:25

Then everyone, as I discussed this concept of this concept, right, observability,

1:37:31

observability. Now, related to that, I would like to discuss something called as quality

1:37:36

matrices, quality metrics. Now guys, how would you measure whether your agent or whether your

1:37:43

application is working fine or not, working up to the map or not? Don't you think you should have

1:37:47

some metrics designed to identify the quality of your agent? Correct? That whether your agent

1:37:55

is performing as expected or not, working as expected or not, this is what we do in quality

1:38:00

metric, right? What you can do everyone is you can define multiple types of quality

1:38:04

metric, right? For example, let's see you can just have the final response to, basically the response

1:38:10

accuracy, whether your response is accurate or not. Tool accuracy, whether your agent is able

1:38:16

to call the right tool or not. If you remember, in the last evaluation class, we discussed about

1:38:21

this, right? That whether you are calling the right expected tool or not. So in the evaluation. JSON,

1:38:27

we created a list of expected tools, right?

1:38:30

And then in the output we observed that whether our agent is calling these expected tools

1:38:35

or not, right? Make sense everyone? Then argument accuracy, whether your arguments are correct

1:38:41

or not. Retrieval accuracy, whether your retrieval is good or not. Groundedness, correct? Groundedness

1:38:48

means that whether your answer is supported by the data or not, is based on policy data or not.

1:38:53

It is not random answers. Then everyone, let's say there is a refusal accuracy. Now you kind of, after

1:38:58

some, after running your applications for some time in the production, you will have some

1:39:02

kind of approximate percentage. That on an average, out of 100 queries, let's say on an average, five

1:39:08

queries gets rejected. But someday, everyone, one day, if that 5% becomes 50%, 20%, 30%.

1:39:15

Don't think now this is a serious matter, that how your agent suddenly started refusing more than

1:39:23

20, 30% queries, but the ideal percentage is around 5%. Correct even? Again, you need to check it.

1:39:28

that refusal percentage or refusal accuracy is within the range.

1:39:33

Okay, latency. On an average, how much time your system takes, right?

1:39:37

This thing, right? On an average, this is a normal range of the latency.

1:39:41

Someday if the latency increases up to a certain threshold, correct? How would you tackle that?

1:39:47

Then everyone, token utilization, right? You will always have some rough idea that how many tokens

1:39:53

are being consumed on an average every single day, approximately.

1:39:56

someday, everyone, if the token consumption becomes 2x, it is becoming doubled, or it is

1:40:02

increasing by 30, 40, 50%. This is an unexpected growth, right? Correct, everyone? Your token

1:40:08

utilization should not increase like more than 10% on an average. If there is a unprecedented,

1:40:14

unexpected growth, then we need to tackle that. Does that make sense to all of you? Does that make

1:40:19

sense to all of you, everyone? Okay? These are a few things, everyone. I have already added this thing

1:40:25

in the notes, in the type notes, you can go through that. Again, uh,

1:40:31

now the next very good concept that I would say is something called as cost versus latency trade-off.

1:40:47

Can you try to guess everyone, what is the meaning of cost versus latency trade-off? Any idea, any,

1:40:55

example. Anything you can think of. Cost versus latency trade-offs.

1:41:12

Everyone now tell me if you want to reduce the latency, premium model, okay, okay, take a few more

1:41:19

seconds of time. I believe some people might be typing. LLM is costly, but fast and vice versa.

1:41:24

Very good point. The cost per tokens, okay? What is this, what is the meaning of trade-off?

1:41:31

To get something, you will have to pay something, right? Yes, no? Exchange. Let's say, for example,

1:41:38

if you want better performance of your laptop, you will have to pay two, three-lac rupees to Apple,

1:41:42

get the best laptop, latest laptop, right? What you are getting? You are getting the performance

1:41:47

laptop, high-performance laptop. What is the trade-off? You are paying something. Right? Very, very, very,

1:41:54

simple statement, something to get something to lose. That is a statement, right? This is

1:41:58

what the meaning of trade-off is. Okay? Now everyone, cost versus latency trade-off, it is one of the most

1:42:04

important trade-off that everyone discusses at a senior level, right? Can I say that even, you can always

1:42:10

make your system best performing system. Keep on adding more and more infrastructure. Use the best

1:42:16

hardware. Use the Mac, like the ultimate laptop, ultimate server, highest possible RAM, best quality RAM, right?

1:42:24

You can keep on increasing the cost. Your latency will keep on coming down.

1:42:27

But everyone, how much trade-off you are okay with? You cannot spend infinite amount of money, right?

1:42:32

You cannot spend infinite amount of money. That's why everyone, everything has a cost.

1:42:36

Every improvement has a cost. But you cannot keep on improving infinitely because you don't have

1:42:40

infinite money. So you'll have to find out the base idea that this much latency I am okay with.

1:42:46

And for this particular latency to achieve, I am ready to spend this much amount of money.

1:42:52

Is that point clear to all of you?

1:42:54

I'm ready to spend this much amount of cost.

1:42:57

Is the idea clear to all of you?

1:43:00

Okay? Now I will give you some common examples, some common changes that increases the quality,

1:43:07

but it will also increase the cost. For example, everyone, if you have, let's say maybe, if you take

1:43:12

slightly higher K value, instead of, let's say, three, retrieving three documents, let's say

1:43:17

you are retrieving five documents.

1:43:20

Now, can I say that everyone, you will get more context now?

1:43:24

And this context, you can pass to the LLM to get better answer.

1:43:28

But everyone, instead of passing three chunks, if you're passing five chunks to the LLM,

1:43:32

obviously the token utilization will be high.

1:43:34

Your LLM will consume more number of tokens because the prompt will become bigger.

1:43:38

The input will become bigger.

1:43:40

And overall number of tokens that your LLM consumes, it is input tokens plus output tokens.

1:43:45

Are you guys getting this point? This is one example.

1:43:47

Other example, everyone is, let's say, better LLM.

1:43:50

If you use a very high quality LLM, obviously the quality of,

1:43:54

the answer, the quality of your agent will be better. But at what cost, you will have to pay more money.

1:44:00

That LLM is cheap. LLM is costlier. Are you guys getting this point?

1:44:07

Makes sense, everyone? Then you can set larger context window, right? You can pay more money to the LLM

1:44:13

company and you can buy the more context window. If the context window is bigger, will your agent work

1:44:19

in a better way? Let's assume that you are using some agent. You're building some. You're building

1:44:24

some agent for a bigger task, for a continuous and continue task. You need bigger context window.

1:44:29

For a bigger context window, you are paying more money to the to the LLM. And if you are paying more

1:44:33

money, you are getting better context in the LLM. These are some tradeoffs, everyone, that you can,

1:44:40

what you want. You want this quality, but at what cost. What cost you are ready to pay for that.

1:44:46

Is everyone clear with this? Yes or no? Okay. Then everyone, I think,

1:44:54

that's it. This is what we wanted to discuss, I guess. Prompt patching, tool patching.

1:45:01

Now, tell me everyone. This prompt patching, tool patching, retrieval tuning. These three things

1:45:08

have we already done in multiple classes? Try to change the prompt. Output will change. Try to add a restriction.

1:45:15

You are like you are making the agent more stricter. Right? Retrieval tuning. In one of the classes, do you

1:45:22

remember that we tried changing the K value. We can change the similarity search also.

1:45:28

So basically when you make a call, I forgot the name of that, when you make a call to the collection,

1:45:34

collection. Search, you can provide what type of search do we want? Remember? Let me show that to you

1:45:40

that how can you change the search behavior. Just a second, everyone. Let me share my screen of Visual Studio.

1:45:52

Yeah.

1:45:56

Yeah. Can everyone see my screen now?

1:46:22

previous rag application, let's say. Do you see that everyone here?

1:46:32

Retriever is equal to vector store dot as retriever. In this retriever everyone, if you see we are

1:46:39

passing the search type, where we are passing similarity. If you see that similarity search,

1:46:45

let's say, if you let's say just for comparison, let's say how similar, what kind of outputs you are

1:46:49

getting via similarity search. What kind of outputs do you get via similarity search? What kind of outputs do you get via

1:46:52

some other type of search. So you can change the search behavior here. What type of search

1:46:57

algorithm you want to use? Then everyone, the search arguments. You can change the K value. Okay? And this is how

1:47:03

everyone, this is called this retrieval tuning, right? You are trying to tune the retrieval. You try multiple

1:47:09

algorithms, you try multiple K values. After that, you come to one conclusion that this particular algorithm

1:47:14

is working good for my use case. Does that make sense to all of you? Then everyone, you can tune chunk size

1:47:20

also, right? At the time of creating the corpus, if you see, we have ingesting, while

1:47:26

ingesting, if you remember, this is the chunk size we have given, okay, splitter, right? While,

1:47:32

when we talked about recursive character, text, splitter, we are defining the chunk size. Now,

1:47:38

how do you measure this, that the quality metric, that whether your retrieval is good or not?

1:47:42

Can I say that retrieval, first of all, depends on how you are ingesting the data? If your input is not

1:47:47

good, you cannot, you cannot expect better output, obviously, right? So what do

1:47:51

everyone? You set the chunk size. You give a proper chunk size, right? Maybe set it for 800,

1:47:58

check the output. Set it for 500, check the output. Set it for 600, check the output. Again, everyone,

1:48:02

you try to give the combination of chunk size and chunk overlap, right? Try different combinations

1:48:08

and you will see that the output behaviors are changing. And maybe you try for maybe 10, 20 iterations

1:48:13

in real applications, try for 10, 15 applications, prepare a particular

1:48:17

document for same query, like give multiple test cases to all the scenarios, then compare

1:48:23

the output, right? For both positive cases, negative cases, refusal cases, happy cases, not happy

1:48:29

cases, etc. Is that point clear to all of you? This is how you tune the retrieval. Okay? Is everyone

1:48:37

clear? Okay. So I think everyone, this is what we wanted to discuss. That's it. I think the content for the

1:48:47

was just one hour of content today. Let me see whether we have covered all the topics

1:48:54

or not. In fact, everyone, we can try some time, right? We have some time. So what I can do

1:49:00

everyone is, if you see here, we have Langchain Rag app, right? So what we need to do is

1:49:09

all these things are already there. What I can actually do, let's create a corpus. Creating the corpus

1:49:14

files are already there in the document folder. All of these are the files.

1:49:18

Dot MD files. Let me show you some demo. Okay. And then everyone inside ChromaDB, it is there.

1:49:23

So what I can do everyone is I can delete, I am deleting this ChromaDB. Okay, I'm deleting this

1:49:28

chroma DB because I want to create it from scratch. And let's go to the ingest now. Let's try to run

1:49:34

this ingest. Where is Lankchain Rag ingest?

1:49:41

Yeah. This is step number two. First step was

1:49:44

to create a corpus, right? Remember that, everyone? To create the files in the document's folder.

1:49:50

Second step is to ingest these files. While ingesting these files, everyone, you can tune this behavior.

1:49:55

So on an average, everyone, how many correctors we have, maybe 100 characters? So let's take the

1:50:03

value to be, let's say, 50. Okay? And the chunk overlap is, let's say, just 10 correctors.

1:50:11

Sounds good, everyone. And let's try to run this appellate.

1:50:14

application. Okay? So everyone, for this, I would need the API key. Let me set the API key first.

1:50:44

E. Okay. Set it everyone. And now let's try to run this application, Python 3,

1:50:53

lanchain rag ingest.py. What this ingest functionality is doing everyone, if you see, it is creating

1:51:01

the loader, data loader, it is loading the documents, then it is splitting the documents,

1:51:06

it is creating the chunks. And then everyone, if chroma directory does not exist, it is creating

1:51:11

the directory. If it is already existing, it is deleting the directory, then

1:51:14

it is creating the embeddings. It is creating the Croma store. And then finally,

1:51:18

everyone adding the documents to the vector database. So basically it is the loading, chunking and

1:51:23

storing part. Okay? We are loading the documents, splitting into chunks, creating

1:51:28

embeddings and storing these embeddings into vector database. Simple. Let's try to run this application

1:51:33

everyone. And ideally it should create these documents. Now do you see, we have five documents.

1:51:40

But do you see that now, total number of chunks are different now. Earlier, we took a very

1:51:44

value. So there was no chunking logic, right? Chunking was technically not happening,

1:51:49

right? Because the chunk size was 800, right? And our document itself does not have 800 text. Correct

1:51:56

or not? Now, at least the chunks are getting created. Is everyone clear with this? Is everyone

1:52:02

clear with this? Yes or no? Okay. Now what we are going to do everyone is, now we are going to run this

1:52:08

application now, this Lanchchain Rag app. In this Lanchine Rag app, what this Lanchine Rag app is doing

1:52:14

everyone. It is creating the LLM, creating the embeddings, creating the Croma store, creating

1:52:20

the Retraver, creating the prompt template. Then everyone, we are creating the rag chain. That first

1:52:26

we have the context, passing the context as a prompt to the prompt, then passing to LLM, then finally

1:52:32

passing to the parser. We are giving some query, we are invoking the chain. And then finally we are

1:52:37

printing the answer. Very good. Now let's try to run this application here. Because see, we just

1:52:42

are five documents, small documents, query is very straightforward. You may not

1:52:46

see a very considerable difference in the output. But when wide varieties of output comes on real

1:52:52

platforms like Svigi, Amazon, etc., then there is a considerable difference if you change the chunk

1:52:57

size. Now, Python 3, Lankchain, Raggap.Py. If you execute this everyone, you will see some

1:53:06

difference. Let's see the query and then we'll try to create more chunks.

1:53:12

Okay, if you see, it is asking, I don't know based on the provided documents and what

1:53:17

is the query everyone? What is the return window for baby items? If you remember for baby items,

1:53:20

we don't have any data right? Correct? Let's add electronics items. Electronics items.

1:53:28

Okay. Folks, a second.

1:53:42

Yes, everyone. So, everyone. So do you.

1:54:12

see that now? For this also it is not working why? Return window of electronics items.

1:54:19

I don't know based on the provided documents. Why? Inside the documents, return policy, right?

1:54:27

It is a return window. Return policy has, it has the electronics right? Okay. Now what could be the problem here?

1:54:42

If you see, if you are creating a chunk size of 50, most probably what is happening

1:54:47

everyone, I think if you calculate the number of characters here, total there are 63 characters.

1:54:54

It means that everyone, chunk missed it. Can you see that everyone? If you see, there are total,

1:54:59

these are total 50 characters. Till this point of time, they are 50 characters.

1:55:03

Right? This is the actual production ready thing. If you see, these are 50 characters, it will go to chunk 1.

1:55:10

Next 50 characters starting from here.

1:55:12

these are 50 characters. They will go to chunk number two. Now do you say that

1:55:20

everyone, these, like for example, let's say, first 50 characters from here to here, let me create

1:55:26

a separate data for this, let's say, these are 50 characters, right? So what I will do is create

1:55:34

a new file, for example. This is chunk number one. Okay? Then next 50 characters.

1:55:42

These are, this is second chunk.

1:55:46

Correct even, this is chunk number two.

1:55:51

This is chunk number two. This is chunk one, chunk two.

1:55:58

Now let's create a new chunk three.

1:56:03

And chunk three says that from here to 50 characters.

1:56:11

This is the next chunk. I will just show you four chunks and you will get the problem here.

1:56:24

Then everyone, this is till can. And after can everyone, these are 44, 50. These are 50 characters.

1:56:35

And everyone, this is chunk number four. And obviously there is some chunk number four. And obviously there is some chunk

1:56:41

overlap also. It means that in chunk number one, you will store. Now, what is the chunk

1:56:47

overlap? Everyone, we are giving 10. In ingestion, we are giving chunk overlap of 10. Correct, everyone?

1:56:54

It means that 10 characters of the current chunk or the next chunk, we will store in the current chunk,

1:56:58

right? So what we're going to do is, these are 10, 10 characters, 11 correctors. This is 10 characters.

1:57:05

So assume that this is chunk overlapping. This is overlap. Then everyone with this, we will store the

1:57:10

10 characters of the next chunk. This is 10. This is 10. Here. Then, now tell me everyone. If these are the four chunks, assume that, and there are many more chunks, if I ask you, if you perform similarity search on these four chunks,

1:57:40

that what is the return window of electronics item? Can you get that information perfectly from these four chunks?

1:57:48

Return window of electronics item. This is the configuration that we have created.

1:57:53

Chunk size is 50. chunk overlap is 10. Tell me everyone here, there is no match. But here, everyone,

1:57:59

in chunk number two, you see that electronics is a matching criteria. Electronics is matching. It means that

1:58:05

this chunk will come in the context. But in this chunk, everyone, do you have any information related to

1:58:10

any information related to a return window?

1:58:15

No, right? Return window is in chunk number four, right?

1:58:19

Returned within only seven days. Do you see that now? There is a wide gap. That's why the answer is not coming.

1:58:25

Let me show you one very interesting stuff now. What we're going to do is, let's go to ingestion. Let's go to ingestion.

1:58:31

Now we don't have to delete the chroma DB because if you see in the code itself, we are doing that automatically, right?

1:58:36

That if chroma DB, chroma directory exists, delete it.

1:58:40

It will automatically delete. But while ingesting the new data now, let's create a chunk size of,

1:58:46

let's say, 150 and chunk overlap of 20. Makes sense? Let's increase the chunk size. Okay? And now let's

1:58:55

try to run this ingestion pipeline once again. Okay? Now, if you see, now there are total 21 chunks.

1:59:04

Earlier, how many chunks were there? 59. Too many chunks. But now we have 21 chunks.

1:59:10

Correct? Now we have ICS 21. Now let's try to run the same code with the same query, which is RAG app. And the question is, what is the return window of electronics items? If you try to run this everyone, you will get the answer.

1:59:27

Are you guys getting the answer? Are we getting the answer? See, this is the difference. Same data, same input. Everything is same.

1:59:40

changed the data. Only how you are storing the data can make your application from completely

1:59:46

no output to the correct output. Correct everyone, this is the importance of retrieval tuning.

1:59:52

Retrieval tuning says that this is very important, everyone, retrieval tuning. What all the things

2:0:06

you should take care of while retrieval tuning?

2:0:10

Right? Chunk size. Chunk overlap. Chunk size, chunk overlap and K value, search algorithm, and so on. Are you guys getting this point? These are all the things we should take care of while tuning the retrieval. And wrong chunk size, wrong chunk overlap can make your application completely go wrong.

2:0:38

Okay? Folks, everyone, clear?

2:0:42

Similarly, everyone, you can try to do a patch in the prompt. For example, if you go to RAG app, and here, everyone, let's say if you change something in the prompt.

2:0:49

For example, let's say here, you want to add some strictness, right?

2:0:52

Don't use outside knowledge, mention, this, this, this. Let's say, everyone, you can make more strictness here that do not answer.

2:1:01

Do not. Although I think I have already written this. Do not answer any.

2:1:08

any out of domain query strictly. This is a domain, this is prompt patching

2:1:21

that you have added more improvement inside the prompt. Folks clear? Folks clear everyone. Then you

2:1:31

can also make some changes in the tool, tool description, tool name, etc. Tool input, tool output. That is tool patching.

2:1:37

I think everyone, this is what we wanted to discuss in today's class, and this was a very good demo,

2:1:42

that how chunk size, chunk overlap can actually ruin the application and make the application.

2:1:47

Let me make the changes.

2:1:55

Let's say testing.

2:2:07

Okay, so folks, let me upload the notes as well. We are done with the class. How many of you got

2:2:14

everything from the class? All of you understood everything? I think today's class was very,

2:2:21

very simple. Because even the module has completed, right? This is the last class, I think,

2:2:25

of the module. Now, the new module will start, and in the new module, we will have new problem statements,

2:2:29

like new things. For example, if I show you what all the things we are going to cover in the new module,

2:2:34

that is going to be even more interesting.

2:2:36

because now you have a lot of context about the coding, about building the agents, right,

2:2:41

agentic system design. You are already aware of that thing. Now, the next module is going to be

2:2:46

around the deployment. Okay? Let me just upload the notes and let me show you.

2:2:56

Okay, notes have been uploaded. And now...

2:3:06

So, guys, let's mark the topic what we have discussed already. This is the last class.

2:3:17

We discussed all these things. You can see that. Tracing, quantitative scoring. We also gave some

2:3:24

score, right? Then debugging. Today we have discussed identify and categorize common agent failures. Yes.

2:3:30

Apply prompt tool level patches. We have done that. Tune retrieval configurations done.

2:3:34

major agent performance using quality matrices, we have discussed about it. Then I trade on

2:3:39

agent configurations, controlled agents and comparative analysis. Just we have to compare different

2:3:44

parameters that how your agent is performing. Now, let me show you this mind map also, everyone.

2:3:50

This is the mind map for today's class. Okay.

2:3:59

Yeah. If you look at this, everyone, what we have covered. In the previous module, we have covered, we have

2:4:04

word, agentic foundations, Python APIs, etc. LLM basics, prompting,

2:4:08

backend foundations. Another module previously we discussed about memory, rag, et cetera,

2:4:13

rag pipeline, building rack pipeline, chunking, embedding, search, etc. Current module,

2:4:18

till last session, we have discussed evaluation harness, right? JSON, right? In the last class only

2:4:23

we saw that JSON evaluation, etc. Now in the last, in today's session, everyone, we have discussed

2:4:28

all these things. Failure class, prompt patching, tool patching, etc. Quality matrices. Now, this

2:4:34

is how these things are going to be used in the real life. Real life, me everyone, you will

2:4:38

ship agents that improve without guesswork. There is no guesswork. There is always a quality metric

2:4:43

that you are performing, that you are using to make sure that your agent quality is up to the

2:4:47

mark. Then, of course, again, in the next model that I was talking about, we are going to talk about

2:4:54

multi-agent collaboration and deployment. We will see slightly more advanced use cases of

2:4:59

multi-agents. We will see some frameworks, right? And we will see the

2:5:04

deployment part. How do we deploy these agents on a public APIs? Okay, how publicly we can

2:5:10

expose our agents. Is that point clear to all of you? Focke's clear. Okay. In the next, everyone, if I

2:5:21

tell you what all the things we are going to discuss, we are going to discuss about multi-agent architecture.

2:5:28

We are going to discuss about N8N. We are going to talk about crew AI, autogen, chat GPT agent,

2:5:34

right, LLM operations, deployment and monitoring, governance, right, scaling, control cost for

2:5:41

agent systems, and designing a complete multi-agent system for any business use case. Next module

2:5:47

is going to be slightly more practical module. This module was also slightly more on the coding side.

2:5:53

Next module is not going to be a coding heavy module. Next module is going to be a platform heavy

2:5:58

model. We will be using these, I would say we will be using these frameworks like N8N, Cure

2:6:04

autogen, etc. To make these, to make agentic AI applications.

2:6:12

I think we were also going to discuss about module 3 examination dates. For this module,

2:6:17

the dates are not announced. Niserk, I'm not sure. I think from next week only. Okay, I don't

2:6:25

think there is a break. Why would we start on 29th? July 5 and July 19th. I think then you have

2:6:31

enough time, enough time on, for the exam, exams. Okay? So that's it, everyone.

2:6:38

If you have any confusion with respect to date, et cetera, everyone, I would recommend you reach out

2:6:42

to the Maasai support team. They will be the right POC for that, because these dates are,

2:6:46

unfortunately, I'm not aware of. And if there is any change, I might not be aware of the latest changes

2:6:51

on that. Let me check with the team, Ravi, then. I think you will also get to know, I will also

2:6:57

get to know. Because as far as I, I have not got any information regarding.

2:7:01

this. Okay. That's right. Thank you, everyone. Everyone got, everyone understood all the things from

2:7:07

today's class. Cool. Okay. Easy class. And now everyone, I'm launching the feedback pool.

2:7:14

Please take the feedback poll and then we can drop off. We are done with the class. Thank you so much.

2:7:18

Have a good day and take care.

2:7:31

Thank you.

2:8:01

Okay. Thank you, everyone. Have a good day. Bye-bye. And good night. Take care. Thank you so much.

2:8:08

Thank you, sir. Thank you, everyone. We will again meet on Friday with your tutorial session.

2:8:14

Tomorrow we're not having a tutorial. So please note that we have the session on Friday.

2:8:20

