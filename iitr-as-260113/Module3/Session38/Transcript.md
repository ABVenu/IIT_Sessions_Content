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

Hi everyone, very good evening, folks, am I audible to all of you.

16:54

Hey, everyone. Am I audible?

16:57

Okay, great. Good evening, everyone and welcome to the class.

17:01

I think some people are still having issue in joining the class.

17:04

People are asking for the meeting link.

17:07

Does people have any problem in joining the class today as well?

17:11

Somia, could you check how can we share the meeting link with the people?

17:16

I think someone is asking.

17:18

Yes, I've shared it in the section.

17:20

Yeah, thank you, thank you.

17:22

Folks, this is the meeting link, so please feel free to use this link to join the class.

17:28

Maybe let's wait for a minute or so and then we'll get started for more people, just wait for more people to join.

17:34

People might be having some trouble in joining the class.

17:37

In the meantime, can everyone see my screen?

17:41

Can everyone see my screen?

17:44

Okay, great.

17:46

Perfect.

17:47

So let's wait for a minute and then we'll get started.

17:50

Today we have a lot of interesting stuff to cover.

17:52

Okay.

18:22

So what are we going to see today is, today, we will continue our discussion with Langchain.

18:28

And if you have observed that we are having a good number of classes on Langchain, because given that,

18:34

Langchain is a very, very widely used framework for building agents.

18:38

In fact, for building real time and real world agents, right?

18:46

Lanchine provides us good support for databases, for vector databases, for external tools.

18:52

for building rag-based applications and whatnot.

18:56

So whatever kind of use case that we have in today's world, we can implement that using Langchain.

19:01

So Langchain is very powerful, very flexible, and very, I would say, practical framework, right?

19:09

And today we will see few more properties of Langchain, right, and we will see the implementation as well today.

19:14

So first of all, everyone, we are going to build few agents today with the help of Langchain.

19:19

Now, before we actually get started with the actual implementation,

19:22

I will just spend maybe 10, 15 minutes on the idea that what idea we are going

19:28

to follow in today's class, right?

19:29

So first of all, everyone, what generally happens, let's say if user is asking a query, first

19:34

we send the query to whom, the query will go to whom, query will go to whom, query will go to whom, which

19:48

like join for this session or continue with current link.

19:52

any uh you can if you have already joined then uh there is no issue right amurjit correct

20:00

if people have joined then why do they need to join violin i think the same thing right

20:05

sorry come again what is this question i did not understand completely like amarjit is asking

20:10

so much like join for this same thing right why do they why do they same only you're same only

20:19

if you can join from your uh like browser or

20:22

you can use zoom link to join from the either you can join from your lmf or you can join from the link

20:28

same thing right so your attendance will be marked if not then you can reach out to the support team of

20:32

massay yeah correct correct thank you so guys first of all when we send a query the query goes to the

20:37

lLM right then what lLM does query goes to the lLM then what lLM does

20:43

LLM decides the next action right correct LLM

20:52

decides the next action what LLM decides everyone that for example let's say if there is

21:04

some query which can be answered without any tool can there be some query which LLM can

21:09

answer without any tool there is no requirement of tool calling correct correct so

21:15

there can be two ways everyone right so LLM can decide either tool call is required or

21:21

tool call is not required right?

21:22

So we can say that either tool call required and here we can say that no tool call required.

21:35

Correct or not?

21:38

Now if no tool call is required then who will generate the answer even LLM generates

21:45

the final response correct?

21:52

LLM gives the final response, correct or not?

21:58

Yes or no, if tool call is required, then our system makes a tool call, whether it is database

22:08

or whether API or make my trip or whatever, we make a tool call.

22:12

Tool gives the response, tool sends the response and what do we do we do with this response

22:21

everyone is pre-cashing access call also considered as tool call. Not really.

22:28

So maybe technically you can say that yes, that is a tool call if you are caching, right? Caching

22:33

is also kind of a database. Correct? Technically you can say that right. Yes, that is also tool call because

22:38

that is also an external tool like a database. Correct. Now this tool response, everyone, what do we do?

22:44

We give this tool response back to the LLM so that LM can...

22:51

LLM generates the final user-friendly response.

23:03

User friendly response.

23:10

Correct or not, everyone?

23:12

This is a complete flow that we have.

23:14

Now everyone, today we are going to introduce a couple of new terms.

23:18

Is everyone clear with this particular workflow, first of all?

23:21

Right? Today we are going to introduce a few new terms. Just let's walk through all of those terms, right? First term is tool. Everyone knows what tool is. No need to mention that again. Tool is an external tool which can be also considered as a Python function, right? And how do we decide, how do we create a tool in Python or Lanchine using at the rate tool annotation, okay? Or at the rate, tool decorator. Correct? So if you want to create, if you want to define any

23:50

Python function as a tool, then you can use, at the rate, tool decorator.

23:57

Correct or not, everyone? Okay? Then everyone, we have tool calling agent. Okay? Tool calling agent

24:04

is we already know the agent which calls the tool. So all of these terms are going to, they are going to be there

24:10

in the code. That's why I'm defining them. Tool calling agent. Okay, perfect. Then everyone, the next thing that we

24:19

have is there is a function called as, now how do we create a tool calling agent,

24:24

the agent which will call the tool? So there is a function which comes via Lankchain. Langchain,

24:29

Lankchain gives the support of this. The function name is create tool call agent.

24:36

Create tool call agent. Does it make sense to all of you? Create tool call agent. This basically

24:48

creates the tool and it connects all the things, right? For example, to create a tool which

24:54

will call the agent. What do you need? You need to connect the prompt with LLM. You give the prompt

25:00

to LLM. Then LLM decides which tool to call. Then you call the tool, correct? So these are the things

25:07

that you need to connect. So you give the prompt to the LLM. LLM decides, or maybe let me write it

25:14

in this way. Take a first you have the tool. First you have the prompt.

25:18

Prompt you give to LLM, okay? LLM decides which tool to call and then you finally

25:25

call the tool. Folks, yes or no? Yes or no?

25:30

Correct? So this function we can directly use to create a tool in Lanchine. So this is a separate

25:40

function that comes. Okay, how do we use this function? We will see that in the code. You

25:44

just call this function. You provide the LLM model, you provide the tool, the LLM model, you provide the tool, the list,

25:48

list of tools and then you provide the prompt. But everyone, this particular function is just

25:54

used to create the agent. If you see, create tool call agent. So it creates the agent which can

26:00

call the tool. But does this actually makes a tool call? Does this actually makes a tool call? Answer is

26:08

no. This does not execute the tool. It just creates the action that, okay, you can do that action.

26:15

But to actually call the agent tool, to actually call the tool via agent, you have another

26:22

class in Lankchain, which is called as agent executor, which is called as agent executor.

26:32

Okay? What is agent executor, everyone? Agent executor is the, you can say that, is the runtime manager

26:37

in Lankchain. Okay? So it is nothing but a runtime agent.

26:45

in Lanktine. So basically this agent executor will take care of which tool to call.

26:57

Basically, it will take care of that you have the prompt, pass the prompt to LLM, check the output of

27:03

LLM, which tool LLM has decided to call, and make a call to that particular tool. So this is what

27:08

agent executor does, right? So agent executor asks what, ask LM, what to do. Then if, if

27:15

LLM says that we have to call this particular tool and which all the arguments we need to pass,

27:20

what all the input parameters we need to ask, we need to pass to the tool call.

27:24

Agent Executor will pass those parameters to the tool call. It calls the tool, gets the output,

27:29

and that output, it sends back to the LLM, that, hey, LLM, this is the tool response that we have got.

27:34

Please convert this tool response in a user-friendly way. It converts the tool response in the user-friendly way,

27:39

and then we return back to the user. This is the complete flow that we have. Are you guys getting this point?

27:45

Now, folks, again, the syntax of this, the execution of this, we will see.

27:52

Okay? As of now, I'm just making you familiar with these terms.

27:55

Okay? So tool, we already know.

27:58

Tool calling agent is nothing but the agent which can call the tool.

28:01

So this function comes in the, comes in Lanchine that we can use to call to create the agent.

28:07

This is the function call that we need to make.

28:09

Finally, we have the agent executor which will actually call the agent, which will actually execute the agent, which will actually execute the agent.

28:15

to call the tool. Are you guys getting this point? Yes or no. So what agent executor

28:23

does? Let me write it down few pointers. Agent executor, it runs the agent, executes the agent. It runs the agent.

28:45

And it tracks what have been done. It tracks the status, which tool has called.

28:52

Because there can be hundreds of tools. It tracks the status of tool calling, which tool has been

28:57

called, what input we have passed, what output we have received, whether a tool calling has failed or not.

29:02

If failed, what is the output, what is the response, what is the error message?

29:06

Right. Also, everyone, there is a concept of max iteration. We will talk about it. It can also limit

29:15

the number of iterations. It also limits the number of iterations. It can handle errors.

29:30

What errors tool are returning, etc., etc. And takes the final output and send it back to the

29:35

LLM. Are you guys getting the meaning of agent executor? See everyone. Now, let's see the complete flow.

29:41

Forget about all these terms for now. Just see the flow basically.

29:45

Let's say, everyone, you have multiple tools, right?

29:47

Tool 1, tool 2, tool 3, tool 4, etc. Now you have LLM.

29:53

Can I say that you need a manager who can pass the prompt to LLM and see what tool LLM has decided to call?

30:01

Then make a that, make a call to that particular tool, right?

30:05

Get the output and let's say pass it back to the LLM and like or pass it to the user.

30:10

Do you need a person for that task or not?

30:13

Pass the prompts to the LLM?

30:14

Get the output. Identify which tool LLM has decided to call. Make a call to that tool.

30:20

Make sure that we are passing the correct arguments because every tool might have different

30:24

set of arguments. We need to pass the correct input parameters. Pass correct input parameters.

30:30

Get the output. Now everyone, when you make a tool call, is it 100% assurance you have that tool call

30:36

will always succeed? It will always be success. That tool call will never fail. Not really.

30:41

tool call can 100% fail? Correct or not? Tool is called means it should execute, right?

30:47

Tool is called yes. Tool call means executing the tool. When you call a tool, it means you are

30:52

executing the tool, running the tool. Okay? Tell me everyone, can a tool call fail? Can a call to the tool or

31:01

tool execution can fail? Folks, why we are so slow today to give the response?

31:09

100% yes. Tool call can definitely.

31:11

fail for n number of reasons. Network failure, API internet failure, right? Or let's say

31:17

server is down, database is down, timeout issue. If you're making a call to database, database server

31:23

is very busy, right? And it took a lot of time. The timeout issue can happen. So you need someone

31:29

who can manage these failures also. That what error has happened, whether input was wrong,

31:34

output was wrong, etc, etc. So all of these things agent executor can do on your behalf. So this is

31:40

the manager, right? If you see runtime agent or runtime manager, you can call it as a manager.

31:46

It is a runtime manager in Langchain, which can manage multiple tools. It can help you in executing

31:53

the tools. What output is coming from the tool? Which tool we are calling? Which tool is returning the

31:59

output? Which tool is failing, etc, etc. Monday, please? Okay. Are you guys getting the point of agent

32:04

executor as well? Okay.

32:10

Then everyone, we have something called as max iterations.

32:20

Guys, I think we have introduced the concept of max iterations in last class or I think in one of the last

32:28

classes, right? We have introduced the concept of max iterations. When a tool fails, right? Can I say that

32:35

you might want to retry the tool? Because a lot of times, everyone, you might get some transient

32:40

issue. Transiate means some temporary issue. Maybe let's say network failure, maybe database

32:47

server was busy, the tool was busy, right? Some server was very server crashed. So you might

32:55

want to retry after some time. But everyone, don't you think there should be some limit on the retry?

33:00

Otherwise tool might, tool call, you might do infinite number of times. And if you keep on making

33:06

the tool call infinite number of times, your server will crash. Correct or not, everyone? Your

33:10

server may crash. Correct? So that's why everyone, we have a concept of max

33:15

iterations. So we can tell the agent executor that the max iteration values, let's say, three.

33:21

That you don't have to execute tool more than three times. If it fails one time, you can retry

33:26

one more, retry one more. That's it. You don't have to retry infinite number of times. And this is a very,

33:30

very practical and production handy approach. Then everyone, other concept that we are going to

33:36

see today is handle parsing errors.

33:40

Okay, so you can also tell agent executor to handle parsing errors.

33:46

Now everyone, handle parsing errors, this is a bullion parameter, right?

33:49

This is an integer parameter. You can make it one or two or three, whatever value you want

33:53

to provide. Handle parsing errors, you can make it true or false. Right. This value can either

33:58

be true or false. Now everyone, handle parsing errors says that if there was any error

34:05

while parsing the output. Because everyone, if you remember, uh,

34:10

we saw in one of the classes, I think last to last class, that agent output comes in an object format, correct?

34:17

Or the tool output comes in an agent, you know, or LLM output comes in an object format, right?

34:22

Response object, some AI message object, and there are a lot of things.

34:27

So a lot of times everyone, we need to, for example, in one of the classes, in a couple of classes,

34:31

we used string output parser.

34:33

Remember that?

34:35

That we can parse the output in the string format because most of the time we just,

34:40

we are just concerned about the string output.

34:43

We are not concerned about 100 other parameters.

34:46

So we parse the response object into string output.

34:51

Can there be some error while parsing the input?

34:55

For example, let's say if the output itself is not correct, output is coming in the wrong format,

35:00

and then you are trying to parse it.

35:02

Can there be some error at that point of time?

35:05

Can there be some error at that point of time?

35:07

Absolutely correct.

35:08

Those are called as parsing.

35:10

errors, right? Those are called as errors which we get while parsing the data. If you make

35:16

this parameter true, handle parsing error is equal to true. That means, if you make it true,

35:23

it means that you are telling the agent or you are telling the agent executor that do not crash

35:28

immediately. Don't crash. Immediately, it is kind of a try-catch block, handling exceptions.

35:38

Are you guys getting this point?

35:40

Don't crash immediately, rather send the parsing error, send the parsing error, send the parsing error back to the agent.

36:10

observe and check. So, guys, don't you think it is very, very similar to? In fact,

36:14

not similar to. It is exactly what we do in exception handling. That whatever point, whatever piece

36:21

of code can throw an exception, we write that in the tri-block. And if this code throws an

36:27

exception, that goes to accept block. Except this exception. And then we provide some meaningful

36:33

message to the client that, okay, your code has failed because of so-and-so reason. Please try to

36:38

rectify this error, right? Please provide correct input, the code failed because of this

36:42

error, et cetera, et cetera. We provide a meaningful message to the client. This is what exactly

36:47

handle parsing error does. Correct everyone, folks, yes or no? Correct. We will see all these things.

36:57

Now everyone, if you see, slowly, slowly we are moving towards building production grade

37:02

applications. Have you observed this thing? Slowly, slowly we are moving towards

37:07

production grade applications, correct? And final thing, everyone, don't crash immediately.

37:12

Send parsing errand back to the agent so that agent can check. And last point is, giving a chance

37:17

to the agent to recover. So it gives a chance. Give a chance. Give a chance.

37:32

to the agent to recover. Folks clear?

37:41

When tool call, when tool call fails, will we need to have fallback mechanism? Yes, we need to have a fallback

37:48

mechanism. That's why generally we have retry mechanism, max iterations, right? This thing. Right?

37:56

But even after this, right, even after, let's say three attempts, if the tool call still fails, then we have to write

38:02

manually in the code, then we have to decide that what we want to do. Should we stop the agent

38:06

or should we retry after some time or should we tell the user that maybe try again after some time,

38:12

we will have to figure it out. But at least for first three times or two times or five times, we

38:16

retry. That if that error is recoverable, that we can recover from that error or not. Okay?

38:23

Okay? Okay. Okay. Okay. One more thing, everyone, now we will move to the coding part.

38:30

We have a lot of code to write today. This is, if you remember, in the last class, we started this series

38:36

of mind mapping, right? My mental map or mind map. That what we cover in the class, what we are going to

38:43

cover in the class, and what we have already covered in the past session and how it is going to help in the

38:47

future modules, right? So if you see everyone in the previous module, again, the same thing we have

38:52

covered Python and APIs, LLM basics. It is exactly same thing even. This is something that

38:57

Massey team has introduced and we have a, like in every lecture we need to just go through this for a

39:03

minute or so. It does not, it will not take more than one minute, right? So previous module, this is

39:07

what we have covered. The same thing we saw in the last class also, basics of LLM, prompting techniques,

39:12

backend foundations like fast API, Pidentic, etc. And in other module, we saw agent components like memory,

39:19

tool, rag, memory, retrieval, react loop, etc. These are what we, these are the things that we saw

39:25

in the previous module as well. So basically, we have covered two modules as of now. This is the third

39:29

module. In the current module, we have covered Olama, in the last class we covered Olama, local models,

39:36

slang chain, expression language, chains, tool, tool calling, etc. If you combine the foundational

39:43

knowledge of LMs, prompt, techniques, back-end, then components like memory, rag, databases,

39:49

is, and then this module, if you combine this, then everyone, we will be able to see

39:56

from manual tool loops. Now, in today's class, we are going to see that how we can use

40:02

agent executor kind of thing to execute tools automatically. How can we automate that process,

40:08

right? If you see maximum number of iterations in the last class, do you see that we had to write a

40:12

for loop? Correct? In one of the classes, we wrote a for loop, where iteration is equal to

40:17

1 iteration less than equal to 5 and then keep on calling the tool. If in between any error

40:23

comes in, right, retry the tool, otherwise come outside the forelough. Remember that? We wrote this

40:29

retry mechanism manually, right? But now we are slowly, slowly moving towards the production grade

40:36

applications, production grade agents that we have, we are relying upon the frameworks now, right?

40:41

the automated things now, right? And then everyone, if you see the real life use case, how assistants

40:46

pick tools in order to, in order with safe limits, right? Safe limit means that if a tool is

40:52

failing, it should not keep on retrying infinite number of times. Server can crash because of that.

40:57

And after this, everyone, we will, if you see, we will be able to create. After the course completion,

41:03

we will be able to build the complete agent with memory, rag, etc, etc. Right? So this is a mental

41:08

map, everyone. This particular map will be added in your pre-reads, okay? So you can refer it from there.

41:14

Okay? Most of the maps for

41:16

the subsequent classes are going to be similar. Just the content for that class will

41:21

be added. Okay? Sounds good. Folks, clear or not? Clear or not. Okay. Now everyone,

41:33

let me share my screen with all of you. What is how?

41:46

What is happening? My visual studio is not starting up. Just a second even.

42:16

started having this map. This will be added in the pre-reads of the class. Okay? For today's

42:22

class, the map has already been added in the pre-reads. Why Visual Studio is not starting?

42:46

everyone? Start writing the code? Perfect. So folks, what we're going to do

42:54

is we will open the same folder, Langchain app. And here everyone, we will create a new file.

43:10

That file we are going to call it as langchain. Let's call it as agent executor.

43:21

P-y. Okay. So now everyone, we will start writing the code. So first of all, we will install

43:27

all the libraries. I think all the libraries are already there. Just let's install just to make

43:33

sure that we are not missing anything.

43:40

Okay. So what all the things do we need?

43:46

Install, land chain, open AI, core, that's it. Okay? All the things are already there. Requirement already

44:00

satisfied. Done. Okay. Now we will install. We will import all these things. From landchain,

44:07

open AI, import. We will use this.

44:10

chat open AI feature to create the open AI model to connect with open AI model. Then we will

44:16

use Lanchine underscore core dot tools. We will import a tool. Remember that? We imported tool

44:26

in the last class also. So this gives us at the rate tool decorator. Then we will import

44:30

Lankchain core say prompts import prompt template or we will use let's say chat prompt template. There is not much

44:40

difference. Prompt template is more general thing and chat prompt template is mainly

44:46

used for chat conversational use cases. Okay. And everyone, we are going to install one more thing

44:51

which is called as Messages Placeholder. What is this message? Message Placeholder? I will

44:56

explain you this thing going forward. Okay, we are going to use this thing which is pretty new for all

45:01

of us, right? And then everyone, we will import from Langchain. Agents, we will import

45:08

agent executor. Okay, this comes from classic, yeah? Classic. Classic dot agents.

45:21

Import. Okay, I need to check this, everyone. So let's install this for now. If there is any error,

45:27

we will, I will Google about it. Langchain.com, we need to import agent executor.

45:38

and we will import create tool calling agent. Folks, are all the imports making

45:47

sense to all of you? I think what we are not aware of is messages placeholder. Rest all the

45:53

things we are already aware of. Correct? Yes. Now everyone, we will have a fake database.

46:01

Like just we have almost in every class, we will create a fake database. Just like a e-commerce website, we

46:07

have a sample orders database. Okay? So we have order ID 101. Status is shipped.

46:13

City is Delhi. Amount is this. Two days for delivery. Order ID 102. Status cancelled.

46:19

City, Bangalore. Amount is this. Delivery day is zero. Status ID, order ID 103, delivered,

46:24

Mumbai amount. Delivery day is zero. Is the orders database making sense to all of you?

46:32

Is the orders date, fake database clear? Perfect. Then everyone, we will write a function

46:37

as get order status. For this, we will have the order ID in the input string and

46:47

this will also return the string in the input. It will return the order status and this is going

46:51

to be a tool. Add the rate tool. Is that point clear to all of you? Okay. Then everyone,

47:01

what this function does actually is, this function returns, get the correct.

47:07

get the current status of order ID provided in the input. Now, when to use

47:22

this tool? Use this tool when the user asks about the order status, about the order status,

47:37

for a specific order ID. Is the comment clear to all of you? Is the comment clear

47:47

to all of you? So guys, we will fetch all the order. We will fetch the order details. Order is

47:51

equal to orders.org. Get about, get the rate of this order ID. Right. And we will simply check

48:02

if this order is not there, what does that mean everyone? Order not found?

48:07

return no order found for the given order ID. And what is the order ID? Let's say

48:20

order ID. And we can use a string formatting. Correct even? Else, what we're going to return,

48:28

everyone? Else, what we will return? We will return in the output. We will return. Let's say, what is the current order status?

48:37

Let's say order with ID. Formatting. Order with ID is currently, if you see everyone, what we are saying, is currently is delivered, is cancelled or shipped. Currently we can remove is, we can say that order from this order, get the status.

49:07

order, give me the value of status. Is that conclude all of you?

49:14

Okay? If you want to print the city, you can give city also that this order is for order

49:21

and give the value of city. Okay? If you also want to provide the order amount,

49:37

order. Order amount. Just give order bracket amount, right?

49:45

Amount. Correct. So, guys, is the function clear to all of you? Is the function clear to all of you?

49:56

Okay? Now we are, now, folks, we are going to write the function, define, calculate.

50:01

What is not clear in this? Sohail?

50:10

What is not clear in this? Could you please tell me? We have the orders dictionary. From that

50:16

orders dictionary, whatever order ID is given, we are getting the order object. If order is not

50:21

present, we are simply saying that order not found. If we found the order, we are returning the status

50:28

of the order, the city of the order, and the amount of the order.

50:31

of the order. Correct? That's it. Just four or five lines of code. Correct?

50:38

Getting the order from the dictionary, if not found, say order not found. If found, return the things.

50:45

Return the order details. Okay? Then we will, we will have another function which is called us

50:50

calculate refund amount. Okay, calculate refund amount. Here again, everyone, we will have the order

50:55

ID, which will be of type string, which will also return the type string. Okay. This will also be

51:01

a tool call at the rate tool. And what this function simply does everyone is,

51:09

what this function does is, it will calculate, calculate the refund amount of the given order ID.

51:26

Right? Now, now, when do we want to use this tool? Use this tool. Use this tool to,

51:31

to calculate the refund, use this tool when user asked about refund for a given

51:48

a given order ID for a specific order ID. That's it. Is it. Is the description clear, everyone?

52:01

order from the database, uh, orders dot get, order ID. And again, we will check

52:09

if order not found, if order not found. Again, we can simply say that the same thing.

52:19

Else, what we're going to do? We'll check. Is the idea clear to all of you?

52:24

Folks, yes or no? Okay. Now, we can simply say that. Now, we can simply say that. Now,

52:31

basically the refund amount is going to depend upon the order status, right? So we can simply

52:38

say that if order caste status is equal to equal to cancelled. If order cost status is equal to

52:45

cancelled. If order cost status is equal to equal to cancel. Now, it means that if order has

52:53

been cancelled, then customer is eligible for refund, right? Whatever is the type of order, we will simply say

52:58

that refund amount of the order, order ID, is refund amount of the order of the order ID, is,

53:23

if the refund amount of the order ID, is just simply put order. Dot, order ca amount. Then, you are a look at it and tell me.

53:28

you are eligible for refund, correct? And whatever amount you have paid, you will be eligible.

53:33

Then everyone, we will write another if condition. If order is delivered, then the condition is going

53:38

to be slightly different. We will say that, we will say that, we will say that, we'll say that,

53:58

order ID this has already been delivered, right, has already been delivered, has already been delivered, and the refund eligibility, we can write it in a separate, has already been delivered, has already been delivered.

54:28

a refund eligibility depends on policy, product policy. Are you guys getting

54:44

this point? Just we are writing some random output. Is that point clear to all of you? Okay, so if you

54:50

say even, if this, then this, order not found, order status cancelled, order status delivered. The only

54:57

The only thing that is remaining is shipped. If the order has been shipped, then what do we need to do then?

55:06

Right? So we can simply say that return. If order is shipped, we can simply say that that, that

55:11

that, uh, order ID this has been shipped.

55:27

You can say that?

55:33

What should I say? Let's say we can say that refund cannot be calculated at this time.

55:43

At this stage.

55:45

So, right, so basically you can tell in a bit more detail that either you cancel the order right now, or once the order gets delivered, then put it for the return.

55:54

When the item is shipped, you cannot ask for the refund.

55:57

Is the idea clear to all of you? So these are the two tools that we have created

56:02

as of now. Everyone clear? Okay? Folks, yes, no? Then there is going to be one more

56:11

tool, everyone. In fact, the last tool that we are going to write, let's say, estimate delivery

56:17

status or delivery status or estimate delivery timeline. Okay? Again, we will get the order

56:24

ID in the string format. And again, we will return in the string format. So what we're

56:28

going to return is, what this function is going to do is, estimates, delivery timeline for the order

56:41

ID. When do we need to call this tool? When do we need to call this tool? Use this tool when

56:48

user ask for the ETA or delivery time estimation, estimation, delivery

57:05

time line for a specific order ID. Is that point clear to all of you? Focke's clear?

57:18

Everyone here. So, guys, in this, what do we need to do?

57:26

If the order is canceled, you can say that order has already been canceled. You cannot check the delivery

57:33

status. If the order is delivered, you can say that order has already been delivered. If the order

57:38

is shipped, then you can say that if the order is shipped, this one, right? Then you can say that,

57:45

delivery, you can expect the delivery within next two days. Correct, everyone?

57:48

Simple thing. Again, get the order from the database. Order is equal to orders dot get the data,

57:57

get the value of this order ID. Okay? And we will simply say that if order cast status is equal to

58:09

equal to, you can check that whether the order is delivered, shipped, etc. First, we can say that,

58:14

if the order is shipped, you can simply say that.

58:18

order with this order ID is has been shipped and is expected and is expected to arrive in how to get order

58:41

what is the value of this variable? Delivery days, these many days.

58:57

Clear everyone.

59:05

It's expected to arrive in four days, four days, two days, days, correct? If order has, if you are you, expected to arrive in four days,

59:06

for four days, two days, five days, etc. Correct? If order has been delivered,

59:16

delivered, then what do we, what do we redone? We can simply say that.

59:26

Order has already been delivered while you are checking the status. Okay? We can see that.

59:34

Okay. Hook's clear.

59:36

ID this has already been delivered. If the order is canceled, then we can also say that.

59:44

That order has been canceled. Again, why you are checking the status. Order has been

59:50

been canceled. So, there is no delivery timeline. There is no delivery timeline. There is no delivery timeline

1:0:04

estimate. Everyone clear? Folks clear? Now everyone, I think we are good.

1:0:17

Okay? Order can be this. Order can be this. First, we need to check this thing, right? That

1:0:22

order not found. So we can check this thing. We can copy paste this. Okay. Sunday I think we should

1:0:32

use else. So, guys, should we use else here? Or if is okay.

1:0:40

Okay, should we use if, else if, or else? Okay, should we use else if here?

1:0:47

And else here. Very good, Shora. So, guys, does not matter. Right? Honestly, does not matter.

1:0:59

The reason I, for this everyone is, Sandhya, the reason for this everyone is, Sandhya, the reason for

1:1:02

this is because if you see, what we are doing is inside if condition, we have return statement.

1:1:08

For example, if, let's say, you have this if condition, which is true, then you go inside the if

1:1:14

condition and this return statement gets executed. As soon as the return statement gets executed,

1:1:19

does the remaining part of the code executes, remaining part of the function executes? No. Return means,

1:1:24

return the value and terminate the function. Return means return the value, terminate the function. So if this

1:1:30

condition is true, you will never come to these if conditions. If the second, if this if condition is

1:1:35

true, you will never come to the third if condition and so on. Okay. So whether you write if else if,

1:1:40

else if, else, if, or you write if, if multiple if conditions generally works when you have return

1:1:47

statements. Otherwise, if you don't have the return statement, then multiple if conditions can also

1:1:51

execute in certain scenarios. I hope this makes sense to all of you. Okay. And everyone now,

1:2:00

For example, let's say if the maybe, maybe, maybe, let's say, if there is some order

1:2:05

on which status is not shipped, not delivered, no, cancelled.

1:2:11

Then do you think for them, for that order, none of the if conditions will execute.

1:2:16

If the order, if order exists in the database, but order status is not shipped, not canceled, not

1:2:23

delivered. So don't you think for that, none of these if conditions will execute.

1:2:27

So how can we handle that? Simply, you can say that.

1:2:29

if there is some order, for some order, if any of the if condition did not execute, then you can

1:2:36

simply say that, that for this order, delivery status, delivery status for order ID is unknown.

1:2:46

For order ID is not available.

1:2:53

Correct, everyone? Okay. So these are the three tools that we have written as of now.

1:2:59

Guys, everyone clear with the tool, all the three tools that we have written, yes or no.

1:3:07

Okay? Now everyone, we will create a list of tools. We will write down all the tools at one place.

1:3:13

Okay? Tools.

1:3:16

Create a list of tools. The first tool is get order status. The second tool is calculate refund.

1:3:23

The third tool is estimate delivery time. Okay. These are the three tools. Now everyone, we need to create the LLM model.

1:3:29

How do we create the LLM? Out of these, all the imported things, whatever we have imported,

1:3:35

what particular object or what particular class we should use to create the LLM object?

1:3:46

Out of these. What do you think? Should we use chat prom template, message holder, agent executor?

1:3:53

Obviously, chat OpenEI, right? So chat OpenEI is a class for which we are going to create an instance.

1:3:59

to create the tool, right? To create the LLM object or the model object, right?

1:4:05

So guys, which model we are going to use? Let's say we are going to use the model, GPT 5.2. This is the

1:4:11

pet model that we are using. You can use some easy model also. This is pretty advanced model. I think now

1:4:17

recently OpenA has launched a new model, which is GPT 5.5. Okay? And everyone, we can set the temperature

1:4:23

value, which is again, everyone, not mandatory to provide. It will use by default some value. We can

1:4:29

provide it zero. Zero means more deterministic, right? Temperature value is equal to zero means

1:4:35

more deterministic. Correct? Then everyone, we will write a prompt. And for prompt, everyone,

1:4:43

should we hard code the prompt? Should we hard code the prompt? Not real, right? We will use a

1:4:50

prompt template. So chat prompt template. Dot prompt messages and we will write the prompt here.

1:4:55

Now, guys, prompt is pretty big. So that we, like, I am.

1:4:59

I'm copying that. Okay? I am copying that. Okay. So yeah, this is the prompt, everyone.

1:5:06

So if you see even we are using chat prompt template. Do you remember that? This chat prompt template

1:5:11

we have used in the past also. That chat prompt template is used to create the prompt template for conversational

1:5:18

use cases. If you have a conversation. So one thing, system will respond, then human will respond. So you

1:5:24

have to provide two prompts, right? That to the system, what prompt you are giving?

1:5:29

you are a helpful e-commerce support assistant. Use tools only when required.

1:5:33

If the user asks about the specific order, use the relevant tool. If the user asks for a general

1:5:38

question, answer directly without the tool, etc. So this is the prompt that we are going to pass

1:5:43

to the user. Is that concrete to all of you? Folks clear? Then what human is saying? Human is

1:5:52

giving to one parameter basically input. Input means basically the query. Okay. And for that

1:5:57

everyone, we are using messages placeholder.

1:5:59

Just wait for some time. I will explain you the meaning of message is placeholder.

1:6:03

Make sense? Just hold on for some time. Maybe just 15, 20 minutes. I will come back to this thing.

1:6:09

First, I will give you the demo. Then I will show you that what this message placeholder does.

1:6:14

Is the prompt template clear to all of you?

1:6:20

Now, everyone, do you see that? We have all the things, right? We have the prompt. We have the LLM. And we have the tools.

1:6:28

Now can we create an agent to aggregate all these three things? Can we create an agent to

1:6:36

aggregate all these three things? For that everyone, we use the function called as create tool calling

1:6:42

agent. So this is what I was talking about. Okay? This we are going to use this function. Create

1:6:48

tool agent. Is everyone clear? Correct? So what we are going to use? Create an agent.

1:6:54

agent is equal to create tool calling agent and we are going to pass that what

1:7:02

is the LLM? This is the LLM. You can call this as model also if you just want to avoid confusion.

1:7:09

LLM. Then we are going to pass the tools. What all the tools we have available tools? So tools is

1:7:15

equal to tools, the list of tools we are providing. And then we are providing the prompt.

1:7:21

Prompt is equal to this prompt. So we have created.

1:7:24

an agent successfully. How many of your crystal clear till this point of time?

1:7:33

But absolutely correct till this point of time. We have successfully created an agent. But have we triggered this agent. Have we executed this agent? Has this agent been executed yet? No. This agent has not been executed yet. Who is going to execute this agent?

1:7:54

Who is going to execute this agent?

1:8:01

Now, in the previous classes, everyone, absolutely correct, Mukul, in the previous classes,

1:8:05

we used to manually call the invoke method. And when we call the invoke method, we will have to

1:8:09

take care of iterations, error parsing, parsing errors, etc. manually. But we are going to use

1:8:15

agent executor now. Who is going to execute the agent now? We are going to use, once I have not discussed this

1:8:22

as of now. As I said, a couple of times.

1:8:24

This we are going to talk about in next 20 minutes.

1:8:27

First, I will show you the demo, then we will discuss this what this is giving us.

1:8:31

Okay? Why we are using messages placeholder. I have not discussed this as of now.

1:8:36

Okay? Assume that this is just a placeholder. Okay. I will just fill in the blanks after some time.

1:8:42

I will just first give you the demo what this is doing. Then I will explain. Sounds good.

1:8:49

Okay. Who is going to execute the agent? We are going to use agent executor for that.

1:8:54

Folks, clear or no? We are going to use agent executor for that. Sounds good or not?

1:9:01

Folks, yes or no? Okay. Now we need to create the agent executor. So if you see, we have

1:9:11

already imported agent executor from Langchain. Agents and now we will build agent executor. So,

1:9:17

it's 9 p.m. should we take a break at this moment so that all of you can go through the code if you want.

1:9:22

Yeah. Folks, please, please take five minutes of time and go through the code because I want

1:9:29

all of you to be very, very comfortable with this particular code so that the next piece of code

1:9:33

will become automatically very easy for you to understand. Okay? So we are going to use agent

1:9:38

executor or create tool calling agent. Okay? So this is the link, everyone. Please go through this.

1:9:52

So this is the code for today's class. Please have a look at it and

1:10:05

we will have the, we'll have a break now. So it's 9 p.m. everyone, take 3 to 5 minutes of time to go through

1:10:10

the code, 7, 8 minutes of time to have a break. So we'll meet around 9.13, 9, 12 to 9.30. Let's

1:10:19

have 12 to maybe 14 minutes of break. Okay? See you after the break.

1:10:22

And then we'll complete this code.

1:10:52

Thank you.

1:11:22

Thank you.

1:11:52

Thank you.

1:12:22

Thank you.

1:12:52

Thank you.

1:13:22

Thank you.

1:13:52

Thank you.

1:14:22

Thank you.

1:14:52

Thank you.

1:15:22

Thank you

1:15:52

Thank you

1:16:22

Thank you

1:16:52

Thank you

1:17:22

Thank you

1:17:52

Thank you

1:18:22

Thank you

1:18:52

Thank you

1:24:22

Hi

1:24:27

Hi,

1:24:31

Hi, everyone,

1:24:33

uh, shall we all, shall we all, shall we start, shall we start, shall we start, shall we start.

1:24:34

Hi, shall we all, shall we start.

1:24:51

Hi, everyone, shall we start? Hi, everyone.

1:25:04

So let's get started, everyone. So now we need to create the agent executor.

1:25:17

So what we will do? We will simply create agent, let's say, executor, whatever the name is, agent executor is

1:25:23

is equal to create the agent executor and what all the parameters we need to pass here.

1:25:27

The parameters that we need to pass here, they are very, very important and we are going to discuss all of them

1:25:31

one by one. First, we need to define the agent. Okay, that which agent we have created.

1:25:38

So this is the agent we have created. Agent, which agent, this is the agent. Then everyone, we need to

1:25:43

pass all the tools. Okay? Because ultimately agent is going to call the tools, right? Then everyone, we are

1:25:51

going to pass something called as verbose is equal to true. Right? If anyone knows the meaning of verbose,

1:25:58

do let me know. Else I will explain in some time. Then we will

1:26:01

pass max iterations. Max iterations is equal to let's say maybe you can define three or five.

1:26:09

Let's go with three for now. And we will say handle parsing errors is equal to true. And we will also say

1:26:19

one more thing, which is return intermediate steps is equal to true. So guys, don't worry about

1:26:28

these three, four parameters. I think max iterations you already know.

1:26:31

But still, we will discuss all of them one by one. So these three, four things and this

1:26:36

message placeholder. So these things we will discuss after execution. Don't worry. Everyone

1:26:41

clear? That we have created the agent executor. Everyone clear? We have created the agent

1:26:47

executor. Now we will just execute this agent executor. So agent executor. Okay. Take the user

1:26:55

query in the input parameter. Let's say the user query is maybe let's say what is my

1:27:01

order status. What is the, what is the status of my order? Okay. And the order ID

1:27:11

is, let's say, ORD. I think what is the order ID? OrD 101. Let's say this is the order ID. Ordi

1:27:18

101. Everyone, clear? Absolutely. Verbo's is used for debugging. I will explain. Don't worry.

1:27:24

Okay. So guys, we will invoke this and we will pass simply what we're going to pass is that what is

1:27:29

the input parameter. The input value is this query. This is what we need to pass. Everyone

1:27:35

clear with all the things step by step. Everyone here. So this is going to result,

1:27:43

this is going to return some result. So.

1:27:59

going to do is we will just print the final result. So let's say, results say, print the output.

1:28:07

Okay. Now, this output, we already know. Okay, let's do one thing. Let's try to just print the results.

1:28:15

Okay, result. And everyone, there is one more thing that we will, that we would want to print is

1:28:19

that basically if you see everyone, do you see that return intermediate steps? What do you think

1:28:26

the meaning of this is?

1:28:29

on intermediate steps. Any, any guesses? Just tukka. What could be this? The name?

1:28:38

What name suggesting? Can I say that even if you have a big agent, agentic AI application

1:28:44

in between steps, absolutely correct. Now everyone, let's say if you have an agentic AI application

1:28:49

with 1020 tools. Now which, like you see the, you give the input, you get the final output.

1:28:55

But even if you remember, is that enough for an application developer, for an AI developer?

1:28:59

Is that enough? That you see the input, you give the input, get the output. Not really. Not really, right?

1:29:05

As a developer, you want to see what all the intermediate steps are executing in between, right?

1:29:10

which, what is the first agent which is getting called, the second agent, the third agent, if the error is happening, if there is some error, the error, the error is happening at what particular place, what error is getting, etc, etc.

1:29:21

So that's why everyone, we make this return intermediate steps is equal to true.

1:29:25

If you make this value true, if you set return intermediate steps,

1:29:29

equal to true, that simply means that whatever agent executor is going to perform,

1:29:35

please return all the data or all the intermediate steps in the result. Okay, in this result,

1:29:43

all the intermediate steps are going to be there. If you want to see all the intermediate steps,

1:29:48

you can simply iterate over this thing, right? So it will actually give you two things. You can

1:29:53

enumerate over it. You can iterate over it. So you can have, let's say, agent, let's say, index.

1:29:59

and let's say step, okay, in enumerate, and you can iterate over result and intermediate steps.

1:30:11

Intermediate steps. I think everyone knows the meaning of enumerate, right? Start is equal to 1.

1:30:19

Everyone knows the meaning of enumerate. So enumerate simply means that everyone, that you need to iterate over this value, right?

1:30:25

For example, let's say inside this value, so this is going to be kind of a list.

1:30:29

So you are going to iterate over this list and you are starting the index from 1, right?

1:30:33

You are just giving the index 1 so that you can go to index 1, index 2, index 3, index 4.

1:30:38

So for example, let's say, in this results intermediate, in this list, there are four elements.

1:30:43

So you are starting from, like, you are iterating over all the indexes starting from 1.

1:30:49

You are just giving the start value 1. If you don't give this value, it will by default start the

1:30:54

indexing with 0. If you give this value, it will start the indexing from 1. But ultimately, you are

1:30:59

iterating over all the values in this list. Are you guys getting this point?

1:31:05

Okay? Folks, yes, no. Okay? Then everyone, what we need to do is,

1:31:13

so why are we skipping you? We are not skipping the first value. Okay? You can say that in

1:31:20

enumerate function, whatever index you give, indexing starts from that number. Okay, indexing starts for

1:31:26

that number from that number. If you give, indexing is equal to,

1:31:29

to 100. It will start from like its first index will become 100, second index will become

1:31:34

101, third index will become 102 and so on. Okay, if you give, let's say 65, the first index,

1:31:40

instead of zero, it will become 65. So that it is easier for you to traverse. That's why we are

1:31:44

starting. Generally, we start with 1, because it is easier for us to understand from 1, that this is the first

1:31:49

value, second value, third value, fourth value, and so on. Okay? Make sense, everyone?

1:31:55

Now, folks, if you want now, if you want, first, I can show you this print. Okay? Don't worry.

1:32:01

Always everyone don't try to copy-paste everything, take it. If you don't understand this thing,

1:32:06

no worries. Let's try to print this. Then automatically we will understand the structure and then it

1:32:11

will be easier for us to iterate, right? This thing, return intermediate steps is equal to true.

1:32:16

So when you set this value to true, in the result, all the intermediate steps, the internal steps,

1:32:23

that what agent is doing step by step, that will be present in this value, intermediate

1:32:27

steps. Okay, Shishir? So we are setting this value to be true when we are creating the agent

1:32:35

executor. Folks, how many if you're clear till this point of time? How many if you're clear till this

1:32:41

point of time? Okay, now let's do one thing everyone. Let's try to execute the code. Okay, one thing that we

1:32:45

have not done is we have not set up the API key of OpenAI. Okay, so let's go to platform.

1:32:51

dot opena.com. I am already logged in. Let me set up an API key. Let's create an API key.

1:33:02

Demo API key. Create the API key. Copy. Go to terminal. Go to terminal and do export OpenAI underscore API underscore.

1:33:21

equal to this. Done. And now we will do everyone, Python 3, Langchain, agent,

1:33:29

Executor. P.Y. Everyone, should we execute this now?

1:33:36

Python 3, Langchain, agent executor, P.Y. Let's execute. So, let's see everyone, what it does.

1:33:44

Okay, there is some error. Cannot import name agent executor from Langchain. I think if you remember,

1:33:49

I gave you this disclaimer that it might not be the right import. Let me just check

1:33:55

this everyone, what is the right import. So it is not able to import agent executors from

1:33:59

langchain. Agents. So there is another way everyone, which is Lankchain underscore classic dot agents.

1:34:07

Langchain underscore classic dot agents. So ideally this should work.

1:34:13

Module not found. Okay? Let's try to import this.

1:34:19

Okay, let's install this. It is already there. Okay, something is getting installed.

1:34:31

Yeah, if you see, it is executing. Entering new executor chain, getting the output, everyone. And if you

1:34:37

see, it is automatically telling us entering new agent executor chain, correct?

1:34:43

Invoking get order status. Do you see that, everyone? Invoking agent executor, uh, get order status.

1:34:49

Now tell me everyone, in the entire query, this is the query, right? Have we told that you need to call

1:34:57

this agent? Did we tell that you need to call get order status agent?

1:35:03

We have been about? No, we did not tell. Still everyone, it is able to invoke get order status

1:35:08

with order ID this. And if you see even are we, we are not even inting this, that invoking this

1:35:13

order agent. It is already, it is automatically coming from agent executor. Right? So agent executor

1:35:18

is a very helpful framework, is a very helpful library from long chain. Okay? So order with

1:35:23

ID is shipped. This is the city. This is what we are returning, right? This is what we are

1:35:28

returning. Order with ID, this is already shipped. City is Delhi. Order amount is 2,500. Your

1:35:33

ID is currently shipped. Is that point clear to all of you? Destination is city and so on. If you want,

1:35:39

I can also check the estimated delivery time. Just tell me, where this is coming from? If you want, I can

1:35:47

also check the estimated delivery time. Just tell me, where this is coming from? Have we

1:35:52

return anywhere? Have we written anywhere? In the code, have we return anywhere? No, this is what

1:36:00

LLM is reasoning. This is the mind. This is the brain of LLM. Because LLM is thinking that, okay,

1:36:05

if user is asking about the status, do you think the next step could be what? LLM is all about

1:36:10

probability, about the next item. So LLM is thinking that, okay, if order status, user is checking

1:36:17

right now, what could be the next thing? We can recommend or we can give LLM, we can give

1:36:23

the user a recommendation that if you want, you can, if you want to check the status of your delivery,

1:36:28

or if you want to check the delivery timeline, I can tell you, estimate it every time. How

1:36:33

agent is, how LLM is able to recognize that is, because everyone, in the agent executor, we are

1:36:38

giving the list of tools. And inside the list of tools, folks, we have all these agents

1:36:42

define. And one of the agent that we have is estimate delivery time. So,

1:36:47

agent is, the LLM is thinking, LLM is able to reason, think about it that, okay, the next

1:36:52

tool could be a delivery time estimation. Is that point clear to all of you? It is taking hints,

1:37:00

right? And then everyone, it finished the chain, right? And this is the output that we are returning.

1:37:04

Then everyone, if you want, I can also check estimate it, et cetera, et cetera, now. This is the final

1:37:09

output, everyone. This, everyone, this is what is coming inside the, if you see, intermediate steps.

1:37:15

Okay? If you just want to probably, maybe, okay, just for a separator, I just want to show you that what is result intermediate steps, then it will be easier for us to iterate also, right? So this is, if you see, this is the result intermediate, right? So in this is, if you see, this is the result intermediate, right? So in this everyone, there is tool agent action, the first thing.

1:37:45

And then there is, yeah, if you see there is only one agent which is being triggered.

1:37:51

So if you see, there is, which tool is getting called, get order status, right?

1:37:56

And everyone, if you see, there is only one tool which is getting called here, right?

1:38:00

So there is only one value inside this tool, inside this status also, correct everyone?

1:38:04

There is only one tool call.

1:38:06

Getting the point.

1:38:07

I will also give you an example of all the three tool calls, one by one, one by one.

1:38:12

Then you will see that, this intermediate steps will be a bigger list.

1:38:15

Now, everyone, if you want to iterate over it, what do you want to print from this?

1:38:19

I want to print from this particular list of intermediate steps.

1:38:23

I want to print which tool has been triggered, which tool we have called, what input we have passed

1:38:28

to the tool and what may be the observation, right?

1:38:31

If you see inside this, see the log.

1:38:37

Do you see that even in the log?

1:38:39

Like the log is also coming, right?

1:38:40

That which tool is getting invoked?

1:38:42

Invoke, invoking, get order status with order ID.

1:38:45

this. Then this is message log, AI message chunk. And there is some input also.

1:38:52

What is the name of that value? Tool underscore input. Okay? See this. Order ID is this.

1:39:00

Where is tool underscore input, input, input.

1:39:07

Finish, this is model name. Yeah, this is the model name. This is the model name. This is the model

1:39:10

that we are calling.

1:39:12

Finish reason.

1:39:15

Name is this. Yeah, look at this everyone. Tool calls. Name of the tool is this.

1:39:21

Argument is order ID. Then total tokens consume 345. Input tokens, etc. This. This. So I hope

1:39:30

this makes sense to all of you. Now everyone, if you just make it false, okay? Now let me do one thing,

1:39:35

everyone. Let me, let's make it false. As soon as you make it false, everyone, and then you execute,

1:39:40

then let's see what happens. Now do you see that even? First of all, if this,

1:39:45

the value is false, then this value itself is not coming. Right? You're like, how can you print it?

1:39:51

Right? If you set return intermediate steps is equal to true, then only intermediate steps will come

1:39:56

in the output in the result. Otherwise, they will not come. Are you guys getting this point? That what is

1:40:01

the significance of this one, this part? Correct? Right? Then everyone, let's make it true. And make

1:40:09

verbose is equal to false. I will now automatically you will understand the meaning of verbose.

1:40:15

Folks, you are able to follow me, right?

1:40:19

Okay.

1:40:20

Verbo's car, there is a different way to check.

1:40:23

So at least by this idea you are clear with this, right?

1:40:26

That what is coming in intermediate steps.

1:40:28

Now, if you want to print, if you want to get more idea about what is happening in the intermediate steps,

1:40:33

now you can check, you can have what action is taking, action, comma, observation.

1:40:40

So there are two things right here, that what is action here?

1:40:44

So, inside this tool, there is a index, comma, step, okay.

1:40:49

Observation. These two values will come in the step in every step. So this is basically

1:40:55

one step, okay? From this step, we will take two values and we will print. Let's say

1:41:01

this is which particular step number. Step. Index. Or let's say, let's say,

1:41:14

index. We are printing first, you can say that first iteration, second iteration, okay?

1:41:21

Then we will print which tool is getting triggered?

1:41:24

F tool called or tool selected.

1:41:36

Action. Dot, tool, what input we are passing to the tool?

1:41:44

tool input, action dot tool input, then what tool is observing? I will talk

1:42:01

about observability just in some time, tool observation.

1:42:09

observation is right so everyone so in for every step we are printing these things

1:42:23

as of now how many steps are there in this example for this query how many steps are

1:42:27

there how steps means how many tools are getting triggered only one right so now let's

1:42:32

again go to the terminal okay clear the terminal

1:42:36

let me delete this in clear execute see what is happening executing this uh invoking this and now just look at this

1:42:45

first index is like you can say that step number one right uh in the first index in the first step you are

1:42:53

select you have selected get order status this is the input ID this is the input value that we are

1:42:58

passing to the tool order ID 101 and tool observation is that order ID with this is shift this is the

1:43:03

tool observation this is what tool has observed or

1:43:06

the output of the tool are you guys getting this point folks yes or no okay now let me

1:43:13

change the query a bit right what query we can give maybe let's say if you want multiple tools to execute

1:43:19

can you tell me some example of the query let's say let's not delete this query let's write a new query

1:43:25

can you give me some example of the query in which i want let's say maybe multiple tools to execute

1:43:31

maybe let's say i can say that for a particular order ID check the status and let me know

1:43:38

let me know the refund amount right let's say for order ID let's say for order ID

1:43:46

let's say for order ID ORD 102 102 check the status tell me the the delivery time delivery

1:43:57

estimate and refund amount now in this everyone don't you think all the three tools will be

1:44:06

triggered to check the status to check the delivery estimate check the refund amount correct or not if our

1:44:14

lm is working absolutely fine if our agent is working absolutely fine it should be able to call all the

1:44:18

three tools now let's see everyone so what we will do is uh index one two three or better is step step one

1:44:26

step two step three okay and for before every step

1:44:33

execute this let's see entering new executor chain invoking this see invoking this see invoking

1:44:43

get order status estimate delivery calculate refund getting the point or not so first of all all

1:44:48

the three tools are getting triggered correct now let's see the refund let's see the result

1:44:54

result intermediate steps that what is happening in the intermediate step because everyone

1:44:58

you are not the user you are the developer of this application so user might not be see when

1:45:03

you are using Uber application you might not be and you are interacting with the chatbot you might

1:45:08

not be interested in the intermediate steps that what Uber did what all the steps did Uber execute

1:45:14

to get you the refund but as a developer you need to know that right as a user you should not know that

1:45:20

in fact that is hidden correct but as a

1:45:24

as a developer it is mandatory right otherwise if anything goes wrong how will you

1:45:27

debug that now everyone if you see step number one may we called get order status step number two may

1:45:33

we called estimate delivery step number three may we called calculate refund is that point clear to all of

1:45:38

of your folks the complete idea everyone is clear step by step is everyone clear

1:45:48

folks please let me know please be very very energetic now for last 20 minutes

1:45:54

okay we had a complete demo now let's talk about some of the things is everyone

1:46:05

clear with this idea return intermediate steps i now i will ask you a few questions is everyone

1:46:12

clear with this what is the what is the what what if the tool does not exist for the prompt provided then

1:46:18

it will fail right uh let's say if you try to execute this for a particular let's say uh place

1:46:23

let's say maybe uh book a flight ticket for me then it will behave in a different way right let's

1:46:31

try to do this how does this behave right let's say and you say that uh and the refund amount

1:46:40

also book a flight for me from Delhi to banglore let's see how it behaves for 5th of june

1:46:53

okay let's see everyone clear okay is the comment while defining the tool is used by the

1:47:02

lm lm use the name of the tool as well and the comments as well okay so the name of the tools

1:47:07

should also be defined in the uh you can say that in the correct way also the tool description

1:47:14

right the the comment that you are giving or the tool description that you are giving that should

1:47:18

be well described okay both the things

1:47:23

okay now everyone clear if you see i have added one more command in the prompt book a flight

1:47:28

do we have any any provision of booking the flight have we any tool for that have we any

1:47:33

integration for that no let's see how it behaves so if you see it executed first three tools

1:47:43

correctly and then what it did if you see everyone get order status estimate delivery time

1:47:48

calculate refund all the three tools but executed absolutely correct

1:47:53

right now the next thing everyone flight booking request this now see the output it is coming from

1:47:59

llm i can't book the flights from here can help you to find the best options simple this is how tool is

1:48:05

behaving right and who is deciding this everyone who is deciding this element who is giving this

1:48:11

is this response lm is that point clear to all of you mokul is your question clear and if you see everyone

1:48:16

in the in the intermediate steps also only three steps are coming steps means which tools you are calling

1:48:23

okay which tools you are calling okay now let's try to understand all these things

1:48:27

one by one uh the different things that we have learned we have used here first of all everyone

1:48:32

return intermediate steps everyone clear with this give me a quick thumbs up return intermediate

1:48:36

steps everyone clear okay then everyone we have max iterations what is the meaning of max iterations

1:48:43

we have already discussed max iterations everyone we use if in case tool fails then how many

1:48:50

maximum times it should retry right if you have three times right maximum

1:48:55

iterations is equal to three it will retry three times after three times it will stop it will

1:49:00

just stop it will not execute further okay then we have verbos is equal to true now verbos

1:49:07

is equal to true everyone it simply shows the internal execution logs internal execution logs okay

1:49:15

so if you see everyone in the intermediate steps lot of logs are coming right those are

1:49:20

are coming because of verbose okay if you make it false the logs will not come

1:49:25

like what is happening internally is that point clear to all of you okay and this everyone we have

1:49:31

learned already okay handle parsing errors while uh while uh executing tools while calling the tools

1:49:46

and it gives a chance it gives a chance to the agent to recover if some issue happens

1:49:59

during perfect is that point clear to all of you is everyone clear

1:50:09

okay now the last thing everyone that we have not discussed as of now is what

1:50:16

is this message placeholder okay this message is placeholder now this message is placeholder

1:50:27

what this does is this message is placeholder everyone if you see we are providing a variable name

1:50:33

is equal to agent scratch pad okay so you can say that everyone agent scratch pad

1:50:38

scratch pad is the working is the agent's working memory working memory

1:50:50

working memory during uh you can say that during the current request during the current

1:50:59

request or during one during one request it is not across the request because once you once the

1:51:05

agent gets completed right once one tool or one

1:51:08

execution pipeline once one chain gets completed right the new agent will have new memory

1:51:14

it is like a conversation right so agent scratch pad is the variable that contains the working memory

1:51:21

during one request right it actually stores it stores what tool was called called and what result

1:51:38

we receive now tell me everyone if this value is not there if agent scratch pad is not

1:51:44

there if you see here clearly what we have seen don't you think everyone that if let's say get order

1:51:51

status is returning some output that output we might need to use as an input for other step

1:51:58

the output of second step we might want to use for third step and so on now don't think there

1:52:03

should be some component who should remember or who should have some small part of memory which

1:52:08

which agent can use and check which tool we call in the first step what input did

1:52:13

we pass what output it received and that output we need to use for the second step the output of second

1:52:19

step we want to use for the third step and so on this is what everyone the task of agent scratch pad

1:52:25

is is the point clear to all of you okay so we can say that we can also say that the agent scratch pad

1:52:38

agent scratch pad stores the tool calls and tool observations what is the meaning of observations

1:52:49

what output it returned observations right if you say even we tried printing tool observation right

1:52:56

what did we get in tool observation we are getting the output of the tool correct what tool is

1:53:02

returning what is the observation of the tool if tool is returning some error if tool is throwing some error

1:53:08

in the observation we will get that error is that point clear to all of you

1:53:14

right now let's say everyone if you if we don't have tool agent scratch pad now tell me what do you

1:53:19

think what will happen if or let's say without agent scratch pad what will happen

1:53:25

without agent scratch pad what will happen what do you think what will happen without agent scratch pad

1:53:31

don't you think agent cannot properly continue with multiple tool tools execution all of you agree with this

1:53:49

it will act like an absolute issue that's correct yes or however agent forgets absolutely correct

1:53:56

which tool did it call what output output did it receive what tool it needs to call again what

1:54:01

output did it what output from the previous tool it got now there is no state of that

1:54:06

now there is no one who is maintaining that right so it will become very clumsy process because if you

1:54:12

have multiple tools if there is single tool it is okay you did you do not need to remember anything

1:54:17

but if there are multiple tools right and if you forget which tool you have already triggered right

1:54:22

then how will you call the second tool are you guys getting this point

1:54:28

I'll have to check that sure yeah we'll have to check that but

1:54:31

i hope the idea is clear to all of you okay perfect so guys i think we have

1:54:39

written every line of code from scratch today correct or not now one thing everyone that we want to

1:54:46

implement now at the last in this is observability the concept of observability what is the meaning

1:54:53

of observability is a general concept it is not a i or agentic a i concept of the observability simply

1:55:00

means that basically you see not only logs it is about monitoring of your application

1:55:06

right so as a developer you need to see you need to have very good idea about which tool is getting

1:55:11

triggered how much time tool is taking what is the latency of the tool right which tool is taking how

1:55:17

much time which tool did it uh which tool execution failed for what reason what argument did it did we

1:55:23

pass etc etc correct everyone folks clear this is called us observability and if you

1:55:30

this is also referred as in terms of like a langchain it is also called as step level

1:55:36

observability step level observability because everyone you need to observe all the tools step by step

1:55:43

because there might be multiple tools that you execute in multiple steps right as we saw if there

1:55:48

are three steps it means three tools are getting executed so you need to see the logs you need to

1:55:54

see the which tool is getting triggered in which number on which number which tool is getting triggered etc

1:56:00

right now from these outputs everyone which parameters from these uh parameters

1:56:09

which parameters are actually helping us in observability if we want to know which tool is getting

1:56:16

triggered which input did we pass what output we are getting uh whether we are getting logs or not what

1:56:23

parameters are helping us is observability mostly used for governance for agents or something beyond

1:56:29

observability is used for checking whether your entire application is working

1:56:34

fine or not if something goes wrong if some execution fails you would want to check which tool failed

1:56:41

what input did we pass what log tool return what error did the tool return this is observability

1:56:49

okay traceability is tracing the error for example if there are 10 steps which are happening and if the

1:56:56

execution failed at ninth step right out of 10 steps let's say execute uh the

1:57:02

execution failed at nine step then you want to trace from step number one how did step number one

1:57:09

whether it was correct or not what was the output of step one it passed to step two then it passed

1:57:14

to step three then four so you need to you trace the complete journey of the request that is called

1:57:19

a traceability traceability you can again do with logging and intermediate steps correct if you have

1:57:25

intermediate steps you can it can help you to trace the request right everyone getting

1:57:30

the point what is the meaning of traceability that if out of 10 steps if your execution failed at any

1:57:37

intermediate step how would you know that why did the execution failed at a particular step how will you

1:57:44

check why did it fail by checking the intermediate steps one by one getting the point everyone

1:57:51

so these parameters are helping from observability point of view

1:57:55

return intermediate steps and verbose is equal to true in fact handling handle

1:58:01

parsing errors is also helping us in observability uh right or error handling it is error handling

1:58:07

more of more of it is that point clear to all of you folks clear okay then everyone i have

1:58:19

added one or two extra steps uh to handle errors in the code right you if you want to check you can check that

1:58:25

otherwise this is good enough this is good enough then everyone the last five minutes

1:58:30

i would like to spend on testing the application which is called as cohort there is a concept of

1:58:35

cohort test pack okay now how do we perform cohort text pack so first of all it is nothing but

1:58:41

a test pack is nothing but a test pack is a collection of

1:58:48

predefined queries to validate the agent behavior

1:58:55

it is nothing but test cases correct or not everyone so to test our application

1:59:03

do we write the do we write a series of test cases correct everyone correct now everyone

1:59:11

tell me in a simple software application you can check input output for example if you're

1:59:15

writing a mathematical problem you can check input output but for agentic AI application

1:59:20

if you just check input and output is that sufficient care that this

1:59:25

This is the input, this is the output.

1:59:27

Is that sufficient?

1:59:29

No.

1:59:30

What do you need to check?

1:59:32

For agentic AI application,

1:59:34

checking only input and output is not enough.

1:59:50

Rather we need to check, we need to check the complete journey.

2:0:03

Correct or not?

2:0:06

That is intermediate steps.

2:0:09

Intermediate steps.

2:0:11

This is what we want to implement.

2:0:15

So folks, for this particular thing what you can write is you can write us here.

2:0:19

So if you want to test.

2:0:20

the entire application, you can write some test cases here. I can give you some examples.

2:0:24

But generally in the production environment, we don't write the test cases in the same file.

2:0:29

What we do is we write a separate file.

2:0:31

So you can write test cases in a separate file.

2:0:34

So let's say, Lanchain, what is the name of this application?

2:0:42

Langchain agent-executor test.

2:0:45

Agent-executed test.

2:0:49

You can create a new application and you can write some test cases.

2:0:52

Now, in this test pack everyone, you should cover all the possible scenarios.

2:0:56

What are the possible scenarios we have for our application?

2:0:59

Any guesses?

2:1:01

What all the possible scenarios we have?

2:1:05

One is single tool call or first of all, no tool call, single tool call,

2:1:11

two tools, three tool calls, correct, and order ID not found, correct?

2:1:17

maybe on a high level, these three or four ways we have, right?

2:1:22

Scenarios we have.

2:1:24

Folks, yes or no?

2:1:26

So, instead of writing all the things from scratch, I can copy paste this.

2:1:31

I have added all these things in the notes, you can check.

2:1:33

So if you see, the first test case, T1 is single tool call status.

2:1:38

Queries this query class, right?

2:1:40

Query class is just like, just kind you are giving a name to the test case.

2:1:46

And what is the expected?

2:1:47

tool for this particular use case.

2:1:49

For this query, how many tools we need to call, which all the tools, get order status.

2:1:54

For single tool delivery, estimate delivery.

2:1:58

For multi-tool call everyone, for order ID 102, check the status, also tell the refund amount.

2:2:04

All the three tools should get triggered, right?

2:2:07

Check the status, not delivery estimate, right?

2:2:10

So two tool calls, right?

2:2:13

Get order status and calculate refund.

2:2:15

Folks clear?

2:2:17

Guys, yes or no?

2:2:19

Right?

2:2:20

Then no tool.

2:2:22

Explain what the refund means.

2:2:23

If you just ask a simple query, explain me AI.

2:2:26

Explain what is AI.

2:2:27

Does LLM needs to make a tool call in that scenario?

2:2:30

If you ask, what is the meaning of refund?

2:2:32

Explain me refund.

2:2:33

No tool call.

2:2:34

Expected tool calls empty.

2:2:36

Okay?

2:2:37

Then missing order ID.

2:2:38

Again, no tool call.

2:2:40

Okay?

2:2:41

In this everyone, if you see, if you pass this query,

2:2:46

if you pass this query, if you pass this query,

2:2:47

query to the LLM, don't you think LLM will first check there is, like there is no order

2:2:51

ID here?

2:2:52

LLM is smart enough to find that there is no order ID.

2:2:55

So this is what is called as HV1, TestPack, correct?

2:2:59

Focus clear.

2:3:05

And then you can execute all of these test pack.

2:3:08

You can execute all of these test pack to the query, right?

2:3:11

If you want, I can write the simple function here.

2:3:14

Let's say you can write a function.

2:3:16

Run, test.

2:3:17

pack, right? And you can simply iterate over these test cases for each test case

2:3:26

in test pack. For each test case in this test pack, you will get this JSON object, right?

2:3:33

In this JSON object, you have ID, query, query class and this, right?

2:3:37

So first, get the test case ID.

2:3:40

Let's say print, test, test.

2:3:47

test case ID.

2:3:58

Test case ID.

2:4:03

ID.

2:4:04

What is the problem here?

2:4:16

Okay.

2:4:17

not a variable. We can put this outside.

2:4:20

Correct?

2:4:21

Oh, there is one extra call.

2:4:35

Test case ID is this?

2:4:37

Then what type of test case is this?

2:4:40

Let's say test case class class.

2:4:47

test case query class we can print it and then what test case query we have.

2:5:01

Test case query we have.

2:5:17

What is the query here?

2:5:19

query class?

2:5:20

Sorry, query.

2:5:21

Okay, we can print all these things everyone.

2:5:23

And now what we need to do?

2:5:24

We need to execute the agent, right, for every query.

2:5:28

So what we will do?

2:5:29

For every test case, we will do, result is equal to, and we need to import from Lanchine agent executor,

2:5:37

okay?

2:5:38

Implement, agent executor, import, what do you say, agent executor?

2:5:46

Correct everyone?

2:5:48

Folks, yes, no?

2:5:49

Because we want to execute it, right?

2:5:50

We will import it and simply we will do agent executor.

2:5:54

Invoke.

2:5:55

And while invoking everyone, what do we need to pass?

2:5:58

What do we need to pass?

2:6:00

We need to pass.

2:6:03

In the input, we need to pass the test case query.

2:6:07

And what is the query, everyone?

2:6:08

This is a query.

2:6:10

Folks clear.

2:6:12

And now everyone we can check whether the output is correct, output is not correct, whether it is working

2:6:15

whether it is working fine or not fine.

2:6:17

Everyone clear?

2:6:19

Now that is your task.

2:6:21

Refer from the notes and complete it.

2:6:23

You just have to compare

2:6:25

what output you are getting here,

2:6:27

whether the result, inside the result,

2:6:30

from the results in the intermediate steps,

2:6:33

will we get all the tool list?

2:6:35

What tools are getting called?

2:6:38

Which all the tools are getting triggered?

2:6:40

We will have all the list.

2:6:41

Step by step in the intermediate steps, yes.

2:6:43

And this is the actual

2:6:45

tools which are getting triggered and here we have expected tools.

2:6:49

Can you compare whether actual tools are getting, are equal to expected tools or not?

2:6:55

So how will you get the actual tools?

2:6:59

Actual tools is equal to what?

2:7:04

From this result, get the, like you will have to check how the tools are coming in the intermediate

2:7:10

steps.

2:7:11

Just extract it.

2:7:12

Is everyone clear?

2:7:14

folks clear right now I can put a comment here

2:7:21

compare the list of expected tools and expected and actual tools.

2:7:32

This is what is called as test pack or cohort test pack.

2:7:37

Okay?

2:7:38

I hope everyone is clear from today's class.

2:7:43

Okay?

2:7:44

Everyone, if you remember, in the last class, I think we copied a lot of code, right?

2:7:49

Because last class, what was happening is the code was a lot, okay?

2:7:53

Just like today's class.

2:7:54

But in last class, because we copied, I think some of you did not understand, correct?

2:7:59

So that's why in today's class, we have written everything from scratch.

2:8:03

We did not copy anything, apart from prompt, obviously, right?

2:8:06

and the test cases.

2:8:07

We did not copy anything.

2:8:09

I hope everyone is clear.

2:8:11

Give me a thumbs up.

2:8:14

okay okay let me push the code everyone and let me upload the notes as well

2:8:44

Folks, these are the notes for today's class.

2:9:01

Could you check just after a few seconds?

2:9:14

So folks, this is the code for today's class.

2:9:31

Can you check if this is also accessible to all of you?

2:9:44

Okay.

2:9:45

Folks, that's it for today's class.

2:9:47

I hope all of you enjoyed the class.

2:9:49

Correct?

2:9:50

I'm encountering 404 not found error when trying to access the link of my GitHub repository after

2:9:55

creating it.

2:9:56

Could you help me with troubleshoot why the link is not working?

2:9:59

That is very strange.

2:10:01

Is the link correct?

2:10:04

Links might not be correct, otherwise there should not be any problem.

2:10:10

Can you send the link right now?

2:10:14

Can you send the link right now?

2:10:21

Just check if you're not creating a private repository, but if you are logged in, then you will

2:10:25

be able to access the private repository also.

2:10:27

If I create some private repository on my GitHub account, and if I have not, if I have not given

2:10:33

you the access, you will not be able to access it, you will get 404, right?

2:10:37

Otherwise if you are locked in, if you are created public repository, then there is no chance

2:10:42

you are not able to access.

2:10:43

Public repository, anyone can access.

2:10:46

Even I can access, anyone in the class can access without any login or not.

2:10:50

For example, the link that I gave you in the chat for every class, these are public repositories.

2:10:55

Even if you're not logged in, you can still access these repositories because these are publicly available.

2:11:01

Everyone clear?

2:11:02

So can we launch the feedback poll if everyone is aligned with today's class?

2:11:06

Can we launch the feedback pool?

2:11:08

Okay, very good.

2:11:09

So everyone here is a feedback poll.

2:11:10

In the meantime, Unmole, you can share the link.

2:11:12

So, folks, please take the feedback pool.

2:11:16

If you like the class, take it accordingly and let me know if you have any concern.

2:11:21

Thank you, everyone. Have a good day. Take care. Bye.

2:11:24

If there is no doubt, feel free to drop off. We are done. Thank you, everyone. Good night. Take care and have a good day.

2:11:30

One thing to everyone. So have you tried implementing what Sir has done in today's class.

2:11:40

If someone is still doing, I would request you to please complete that and we'll wait

2:11:47

for maybe two, three minutes to take up some doubts and then we can finish.

2:11:53

Yeah.

2:11:54

Is that okay?

2:11:55

Yeah, yeah, sure, sure, sure.

2:11:56

No quiz today because this was mainly a implementation-based session.

2:12:01

Okay, when we have more conceptual session, we will have quiz.

2:12:05

For me, you're saying we should wait, we will wait for a few minutes for people to have any doubt.

2:12:09

for sure yeah if they are actually running the entire thing yeah yeah i'll be happy if you

2:12:18

have any doubt i can take your doubts so i can take your doubts if you are running maybe guys what you

2:12:23

can do is you can just try to get the code from you can try to refer the code also from github right

2:12:27

entire code is available on github

2:12:29

guys unmole this is not the problem of repository this is a problem of

2:12:40

this is a problem of if you see the site configured at this address does not contain the requested

2:12:45

file you are trying to you are trying to access something which does not exist this is not a

2:12:50

repository it is the website that you have created you on githup.io domain okay unmole uh medetwal

2:12:59

git up.io this is a website this is not a repository okay so this is the site issue that this

2:13:05

particular page right uh that you are created that uh methoverse hyphen universe hyphen

2:13:11

this is not present on the page on gethub.io on your website okay this is not a repository by the way

2:13:29

first of your request very few of you are left to fill the feedback code

2:13:37

this complete so how to resolve this this is a wrong page now how do i anyone know that which page

2:13:43

whether you have created that correctly or not whether that resource exists or not whether that

2:13:47

website name is correct or not whether that domain that you have created right uh let's say your

2:13:51

name dot git up dot iu whether that is correctly configured or not okay there can be under

2:13:56

reasons this is not a repository repository when you create it will be 100% accessible

2:14:01

100% but now if you are created this let's say if i create a website on githup.io domain

2:14:07

Deepakasera.g.g.cira dot i.o, there can be 100 different issues that can happen. DNS is not

2:14:12

configured, IP address is not configured, right? The github.io is not able to assign you a domain,

2:14:18

multiple reasons can be there. And at the last, the simple reason could be the URL that you are accessing.

2:14:25

First of all, are you able to access this particular.

2:14:26

thing or not right this particular thing is not available right if you see this is itself

2:14:35

not available unmole medaithwal dot githwall. This domain itself is wrong okay and mole it means that the domain is

2:14:44

not correctly created now if the domain itself if amazon dot in is not a correct website then you cannot

2:14:50

access amazon dot in slash products slash orders something right so this domain itself is wrong

2:14:56

Getting the point?

2:14:59

Okay?

2:15:00

A one check k'all, how you created this domain, did you miss any configuration or not?

2:15:05

100% there is a configuration miss.

2:15:07

So this typically happens when you create a new website, when you create a new platform,

2:15:11

sometimes you miss the IP address or the DNS entry or there is something called as

2:15:16

name server, NS entry, something like that.

2:15:19

Okay?

2:15:20

I am unable to access.

2:15:22

Vishanath try for some time.

2:15:23

It will be accessible, 100%.

2:15:25

Right?

2:15:25

It takes sometimes.

2:15:26

to get processed. If you see this link is, okay, no, no, don't go to this link. Go to this.

2:15:36

And the notes that I have uploaded today, which is how many minutes ago, this one. Go to this link.

2:15:43

That link was wrong. Okay, that link was wrong. Okay, feedback poll is done, so.

2:15:53

Yes, sir, I think we have taken the doubts.

2:15:56

Can we add date stamp in the name of file?

2:16:01

I can do that, Sishir.

2:16:03

I can do that, right?

2:16:05

The date stamp, right?

2:16:05

The date in the file name or maybe what do you say?

2:16:10

Or what do you say?

2:16:11

The commit.

2:16:13

Okay, I can do that.

2:16:14

Okay?

2:16:15

Or, for till now, if you want to search for anything, is I think you can sort them.

2:16:20

Some, is there is, is there any way you can sort them basis on the,

2:16:23

sort based on the time.

2:16:29

One of the, okay, does GitHub provides that?

2:16:32

Okay, in settings, et cetera.

2:16:33

GitHub must be providing that.

2:16:34

You can sort based on the commit timeline.

2:16:38

Okay?

2:16:39

If you go to all the commits, there should be some way.

2:16:42

Yeah, yeah, you're here, no, all users.

2:16:47

Okay, you can check for a particular date.

2:16:48

But from next class, I'll do that.

2:16:51

Okay?

2:16:53

Yeah.

2:16:53

I need to have a, I need to add a loop of checking quality of topics generated by trending topic.

2:16:59

Will observability, I'm trying to build, will observability and traceability be useful?

2:17:03

100%.

2:17:04

Observability and traceability will always be useful.

2:17:06

Does not matter how simple application you are building.

2:17:09

Does not matter how bigger application you are building.

2:17:11

Always have proper observability and verbose, proper locking mechanism.

2:17:17

Okay.

2:17:19

Okay.

2:17:20

Okay, I think, are we done for me?

2:17:23

Yes.

2:17:23

Sir, we can conclude this session.

2:17:25

Okay.

2:17:26

Thank you, everyone.

2:17:26

Thank you, so many.

2:17:27

Have a good day.

2:17:27

And good night, everyone.

2:17:30

Thank you, everyone.

2:17:30

Thank you, sir.

2:17:32

We'll meet a jan, in the way.