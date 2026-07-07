0:00

Thank you.

0:01

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

Thank you.

8:18

Thank you.

8:48

Thank you.

9:18

Thank you.

9:48

Thank you

10:18

Thank you

10:48

Thank you

10:50

Thank you

10:52

Thank you

10:54

Thank you

10:56

Thank you

10:58

Thank you

11:00

Thank you

11:02

Thank you

11:04

Thank you

11:06

Thank you

11:08

Thank you.

11:38

Thank you.

12:08

Thank you.

12:38

Thank you.

13:08

Thank you.

13:38

Thank you.

14:08

Thank you.

14:38

Thank you.

15:08

Thank you

15:38

Thank you

16:08

Thank you

16:10

Thank you

16:12

Thank you

16:14

Thank you

16:16

Thank you

16:18

Thank you

16:20

Thank you

16:22

Thank you

16:24

Thank you

16:26

Thank you

16:28

Thank you.

16:58

Yeah, hi guys. We can wait for everyone to join in then we can start. I think the voice is clear to everyone, right? Can you hear me?

17:28

Thank you.

17:58

Thank you.

18:28

Thank you.

18:58

Thank you.

19:28

Thank you.

19:58

Thank you.

20:28

Yeah.

20:58

see me and hear me as well, right? I'll just share the screen. In the background, I've already pushed the coding changes that are there.

21:05

Like for example, if you see, I've just updated the code that we are going to discuss today and I've updated the lecture notes also.

21:12

I think the voice is clear and sharp, right? Can you hear me? I think we are good to go. So we can see this that the PPD and everything I have already uploaded. I have updated the coding example also that we will discuss today.

21:26

And yeah, other things also.

21:28

we will try to see. I've updated the notes also before only. So you can read it after the class as well. So I think we can start.

21:35

So like till now what we have discussed this. We have discussed a lot of functions that are required or that are actually present in Lanchine.

21:43

Lankchain. Langein is nothing but a framework that is there. That particular framework, it is helping us to write code easily.

21:50

Like it is having internal functions so that we can build anything with AI easily. We are just using those internal functions that are there.

21:58

And using that, we are trying to write the code.

22:00

Today we will try to see that how using LAM chain, we can actually build a complete agent as well.

22:05

So one by one, I think we can start.

22:07

So let's start with this particular part.

22:10

You can see here this particular thing that, first of all, we will try to, like if you remember, we have already seen the theory of AI agent.

22:18

Do you remember what are the three main components of any agentic system?

22:22

Like whenever we are building any AI agent, then what will be the three main components?

22:27

Do you guys?

22:28

remember that part. Like for example, we can see here this particular thing, that

22:34

our AI agent, it will always have three things. What are the three things? The first thing

22:38

will be that it will have a LLM, that will be the main brain of AI agent, that will try to do almost

22:44

everything. Apart from that, we will try to have a memory, like that memory can be short-term memory

22:50

or long-term memory. Apart from that, we can have different, different third-party tools that LLM

22:55

can call and get the job done. So our AI-A-A-Ele-L-L-L-L-L-A-L-L-L-L-Rer.

22:58

agent is doing an end-to-end task. In order to do that end-to-end task, what it requires, it requires

23:03

third-party tools. That it can integrate with Gmail, it can integrate with IRCTC, it can integrate

23:09

with any other third-party application. So whenever we require such things, what we use is,

23:15

we try to use these kind of scenarios. I think this part you remember, right? That AI agent, it has

23:21

tool, it has memory, and it has LLM, and that particular LLM is the main brain. So today we will

23:28

try to see that how our agent can be executed and what are the different ways in which we can

23:33

write an agent with the help of LAMChail. So I think yeah, one by one we can get started.

23:38

So let's start about this particular part. You will see this that what I'll try to do is I'll try to

23:44

today write a loop. Like if you remember in the last class, we were writing some manual steps that were

23:51

there and that particular manual steps, they were getting some job done. Like for example, if you remember,

23:56

we were able to see that if I write a query that this particular part that we are let's say

24:02

calling like we are just saying that find out the status of the ticket then it is able to understand

24:08

which tool to call and everything was happening manually like we have defined all these tool manually

24:13

if you remember we described three tools one was for finalizing the payment and everything

24:19

one was for calculating the status of the ticket and one was for course eligibility so we were

24:25

using at the rate tool and then we were defining that particular part today what we

24:29

will try to do is today we will try to see different things that are there like for example i'll try to see

24:35

how our agent executor will work so one by one we will try to see that particular part is the main

24:41

idea of the session clear right uh the main idea are you able to understand like if you see here this

24:49

particular part like if i open here the get up also you can see this that in the last class we have done

24:54

basic tool calling and all the tools that i have defined these tools they were i defined

25:00

using these four functions we focused on add the rate tool we focused on bind tools we focused on

25:05

tool calls tool messages and we understood with the help of the diagram flow today we are trying to do

25:11

something different what we are trying to do is we are trying to see here this particular part that how

25:16

like how entire tool we can define and what are the things that we can use so one by one we will start

25:24

page so yeah we will try to see what are these agent executor and everything what are the

25:30

iterations all these functions we will talk about so all this part we will try to see i think one by one

25:35

we can go ahead and see that particular part so let's try to see this so we can see here like first of all

25:47

we need to understand what are the steps that are there in an AI agent or we can call it as one exact

25:54

loop that in one loop whenever user is coming from the start what all things are happening so you

26:00

can see this that user will write any query that particular query could be anything like for example my

26:05

query could be that i want to book a flight from hetherabad to banglore or my query would be that what is

26:10

the final price of this particular stock or what is a percentage increase in this particular stock

26:16

user query could be anything so the first step is that user will enter any particular query that particular

26:22

query it will go to the llm that is present so l lm will understand the query

26:28

l llm will decide whether a tool needs to be called or not you have already seen in the last

26:32

class that well sometimes the tool is getting called sometimes the tool is not getting called

26:37

also like for example if you remember the query where i was writing something that we need to

26:43

generate a motivational line then in those cases tool will not be called also so if let's say that if

26:49

no tool is called then llm will answer directly llm is

26:52

very good with generation of data so it can easily generate proper data that is present if

26:58

let's say tool call is needed selected tool will be executed that selected tool will give the

27:03

necessary result whatever output from the tool is coming it will be sent to llm

27:09

llm will read the customer query or the user query that is present it will understand the output

27:15

that is given by the tool and then it will generate a user friendly output and i think you remember

27:20

this entire steps right like we have seen this

27:22

steps manually in the last class today one more extra things we will try to see this part

27:28

are you able to understand or not this idea is clear to everyone

27:37

correct right so if you see today we will try to see how our agent will execute these things

27:42

now how this particular flow will change so all these things i'll try to show you so you will see

27:48

that before like jumping into the program and with a

27:52

help a program only we will try to see there will be some functions that i will be writing

27:57

in that particular program the functions that in last class if you remember we were using at the aid

28:02

tool we were using different different tools we were using binding tools all these things we were

28:08

having but today we will try to do different things like we will have a tool calling agent we will have

28:13

an agent executor we will have some maximum iteration by maximum iteration i mean that

28:18

sometimes a loop is running we will keep on running it unless everything is

28:22

updated and then there is this scratch pad that is present so all those things we will try to see

28:28

so one by one let's try to go ahead and see what all these functions they are doing and what like what

28:35

is the main purpose so you can see this that there is a tool calling agent like rather than

28:40

discussing the theory first i think we can see from the program because i think it will be a little bit

28:46

more relatable and then we can come back to the theoretical part so let me directly open the program

28:52

and show you what these functions are meaning these are easy to understand not much

28:57

complicated part is there let me directly show you that part

29:01

so you can see in the main repository that is there i've already added a

29:18

agent file that is there this particular agent file that is there this particular agent file it

29:22

contains multiple things so one by one let's try to see what we are trying to do i'll

29:27

directly go to the main function and try to show you different different how i am building a agent

29:32

and what are the different functions that i'm writing and what is the meaning of all those functions

29:37

function so if you see first i'm trying to build an agent executor what is this agent

29:42

executor it will try to execute the entire AI agent that we have built in this entire AI agent what are the

29:48

things that we are having first of all you remember that there is a model

29:52

that model is the same lLM model if i want currently i will be using local

29:57

olama only and you have already seen this function chart olama which is just a external function which

30:03

is provided by lang chain that will help me connect to olama here any particular model

30:08

and everything i can write down i'll try to create a agent so you can see inside a agent currently

30:15

what things we are passing we are passing the lm we are passing the list of tools and we are passing the

30:22

now what do you think is this prompt like can you tell me whether it will be a user prompt

30:27

or a system prompt

30:33

guys do you think it will be a user prompt or a system prompt it will be a system prompt that will be

30:38

writing so you can see this that currently it's a system prompt in which i have written here first

30:43

of all this thing that you are a helpful e-commerce support assistant you can use all the

30:49

tools that required human input also whatever user

30:52

query is there i am providing so i'm providing multiple different prompts but the first prompt that is

30:57

there i am setting up the role so that my AI agent it is aware of what it needs to do so the first

31:04

prompt is actually for the role part and then whatever query user has given that also we are passing otherwise

31:10

it will not know that what we need to do like it will have a role and everything but exactly it needs to

31:17

to whatever it needs to do that should be told by the human message that is there that human message we

31:22

will come to but you can see this that first step is we are trying to create our tool

31:28

calling agent now remember this it's not a complete agent currently what we are trying to build

31:35

is we are saying this particular part that we want llm to make the call to tool itself in the last class

31:43

in the last program that we have seen if you see this particular program also i can again open that

31:49

particular program if you see lLM is telling me that okay these are the tool

31:56

starter present and lLM is telling me that these are the tools that are present and then i am

32:02

manually calling this part today we are just replacing this manual operation this part you need to

32:08

remember otherwise you will be confused that we are not building the entire AI agent yet

32:14

we are just building an agent which will call the tool also this is the step

32:19

that we are doing like that is a main change that we have done from this class from last class

32:24

to this class that last time lm was telling me the name of the tool starter there and once those

32:31

names of the tools were present i was manually calling them like for example if i figure out the tool

32:37

name arguments and id i used to call that particular tool you can see this that here this inmo

32:42

function i have written and it is calling the tool starter there but today we are not doing this

32:47

particular part today the step is different what is the step that we are trying to do in today's

32:53

class we are doing this particular thing that we will make sure that we are able to call the tools

32:58

directly also so if you see here what i have done is and passing three things in the agent so the first

33:05

new function that we are studying today is create tool calling agent and this tool calling agent what

33:11

it will do is it will create an agent and that particular agent it will have the llm it will have the tool

33:17

and it will have the necessary prompt that is there is this part clear if you see the starting

33:23

of this particular program you can see this that i'm importing the tools i'm importing the

33:28

message and everything if you remember in the last class we have already seen these messages

33:32

that whatever message is coming from the human it will be a human message whatever messages are

33:38

coming from the tools that will be a tool message and all these things we are trying to use so these

33:42

libraries i think are easy to understand correct right so

33:47

the main idea that we need to remember i'll again show you the program here the first

33:54

step that we have done is the first step is to build a particular agent inside this particular

34:00

agent what i am doing i am creating a tool calling agent in which three things have passed

34:05

llm tool and the prompt the first part of this prompt is a system prompt and then i am passing

34:10

the human query or the input that is present after this you can see this that i am calling another function which

34:17

is agent executor agent executor means that it will try to execute the entire flow this

34:24

function mainly what it will try to do is it will run the actual agent that is there in this multiple

34:30

different things i have written i am passing the agent that we created i am passing the necessary

34:36

tool starter there and currently you can see these are the tools that are present like for example i've

34:41

created all the different tools using lanchine so you can see one tool is get order status

34:46

this tool if you remember that these tools are nothing but similar functions that are there

34:52

only thing is that in each function i have written here at the rate tool at the rate tool will

34:57

register this particular function as a tool in lanchine so what this thing is trying to do is it is

35:04

trying to register it is trying to consider this function as a third party tool that is

35:11

present is that idea clear so you can see this that in in reality it is a

35:16

function only only thing is that we are considering it as a third party tool that is present

35:22

same way there is a calculate refund amount function that is present and estimate delivery timeline

35:29

now all these tools have written here also all these tools i have passed to the llm as well

35:35

all these tools are passed to the agent executor also now if you see there is one more

35:40

keyword which is max iteration so this basically will help us prevent any repetitive

35:46

like for example in one time if i give a query and that particular query is failing let's say

35:53

the model is down or the request is failing due to any internal error or whatever error is coming

36:00

so this particular part max iteration will make sure that this agent it will run ad max three times

36:07

after three times if it is not working then it will fail it will give some failure

36:12

message that it tried three times but now also it is not working but the main item

36:16

is so that we are never like we are never stuck in an endless loop or we are never

36:22

stuck in a infinite loop in order to prevent that particular part what i'm trying to do i am trying

36:27

to use this keyword which is max iteration apart from that verbose is also there handling parsing

36:33

errors are also there return intermediate steps are also there so you can see this that these are other

36:39

other keywords like for example once i install all the things i will be able to show you the

36:45

the definition of these functions as well that what these functions are doing like i need to

36:49

run the program for that once we run that program we will see that what all different parameters

36:55

we can pass in these functions also but you can see these are some extra steps which will help us

37:01

while displaying the output properly like for example whatever agent is trying to do each

37:06

step agent is executing whatever things it is trying to do it will be printed if i have said

37:12

return intermediate steps is equal to true if i set it to false then it will not work the same

37:17

thing you can see handling parsing errors if i like if i don't set it then if there is a parsing error

37:25

agent can get stuck in middle also so just to handle that particular part this particular value we have

37:31

set to true so these are the things that i've written like currently you can see here in this particular

37:37

step i am trying to execute all these functions like the main

37:42

idea of this particular part is that all these functions that are registered in langchain all

37:48

the tools that are registered in langchain they should be automatically called rather than

37:53

writing a for loop and then manually calling it we want the entire llm to actually call them is that

38:00

idea clear this idea is clear to everyone so one by one we will try to see yeah right we will try to see

38:12

that part that if there is a delay or not that part also let's see like the next

38:18

thing that i have written is i have written some demo queries like for example one demo

38:23

query is what is the status of this particular order for another order i have checked the delivery

38:28

status the status and the refund amount what is a delivery timeline of this particular order

38:34

this is a query i am trying to run all the queries that are there inside these run queries if you

38:39

see i am just invoking the function

38:42

I am just invoking the function. I'm not doing anything like on my own. I am just calling

38:49

this invoke part in which user queries passed. So now what will happen is the agent executor

38:54

that we have created, this particular agent executor. Inside this only one input we are passing

39:01

which is from the prompt. As soon as the input will change, the user input will be changing

39:07

here. So the agent that will be created, it will always have different prompt. Like for example,

39:12

in case of first user query if the first user query is something like this like we can see

39:19

here the first user query will be what is the status of this particular order so that particular

39:25

query will grow inside a prompt agent will be created from that and that agent will be executed

39:31

i think this idea you are able to understand so you can see in this part we are just following the

39:36

function that is there for every step we are trying to fetch the intermediate steps also that

39:42

what model is thinking what llm is doing all those intermediate steps i am also

39:48

displaying here that in this step this particular tool is called and all the inputs and everything

39:53

you can see here in this part i think this idea is clear this part are you able to understand

40:02

so you can see apart from that i've written some test cases also so that test cases

40:06

part let's discuss later on what i'll try to do is i'll try to see what is a model here

40:12

I think the model I have written is Lama.

40:15

I think Lama is a good model in background I can even start

40:19

seeing that particular part if I can quickly download Lama and then again we will try to discuss this

40:24

that what we are trying to do.

40:30

Currently I have only quen model so what I'll try to do is I'll update in this program quen model

40:36

and what I'll do is I'll try to run this program and show you the output so that you are able to relate that

40:42

what is happening in intermediate step once you understand that particular part then

40:46

almost all the functions will be clear once those functions are clear and everything we have

40:51

discussed then you only you can try to run it till then in the background since it will take good

40:56

amount of time i'll try to download lama uh 3.1 as well so that in background this happens so let me

41:03

download it in the background and i'll open a new terminal and in this new terminal i'll try to go to the

41:09

next step yeah i think i need to again activate the environment

41:20

once i activate this environment i'll go to my coding examples i'll say lanchine agent

41:29

and i'll write python 3 and the 4.pb is the name apparently the model is

41:35

quen okay i think i need to install langchain and everything

41:39

i'll install it i think my environment got messed up a little bit i'll fix that part in the

41:46

background but till here this idea is clear the basic idea are you able to understand let's discuss

41:52

the theory let me just install lanchet and everything in the background

42:00

let me run all the commands very quickly basic part are you able to understand about these

42:07

functions you get a basic idea on these functions so one by one let's talk about

42:26

these functions that i've written so we can see this like for example the first thing is that we

42:31

have a create tool calling agent this is the main decision maker or you can say this is the

42:37

main function in which three things or four things generally we supply we supply the lm we

42:43

supply the necessary tools we supply the prompts later on you will see we can even supply the memory

42:49

also all these things we can supply on once we do that particular part we have other function which is

42:55

the agent executor this is creating a agent this is executing that particular agent so inside

43:02

it multiple different things i can see like when it is executing an agent

43:07

that agent might be calling multiple tools if i need to see intermediate step if i

43:13

need to change the tool starter there if i need to change the agent all these things i can provide

43:18

in this particular function so all these functions they are existing where all these functions

43:24

they are existed inside land chain is that idea clear this part are you able to understand

43:31

let me install all the things in the background as well guys the first two things

43:37

are you able to relate or not then you can see we have this function which is maximum

43:44

iteration this maximum iteration what it is trying to do it is doing here this particular part that

43:49

how many times we want that particular action to run if i want it generally we run it only one or two

43:54

times or three times at max not more than that because if in three times it is failing then there might

44:00

be some issue in the agent only and not in the like working or anything apart from that if you remember

44:07

there is parsing errors so if you remember that all the messages that are coming from

44:12

llm if you remember they are in a proper format they are in a i message format sometimes whenever i

44:19

try to convert a i message format into normal string and they are not able to parse it due to internal

44:25

issue it can happen so you can see this that in order to avoid those errors what i can write is i can

44:32

set this handle parsing errors to true if i had set it to true then all

44:37

the parsing errors like whenever we are converting a i message to a normal string or whenever

44:42

we are converting a human message to a normal strength or anything any type of conversion is

44:48

there in those cases to avoid the parsing errors we can add this particular function this agent scratch

44:54

pad also we can see scratch pad will generally show me how different variables or how different memory part

45:01

is changing like for example if a i agent is calling some particular tool and that tool internally requires

45:07

variable then how the memory is changing like how their variables values is changing and all

45:13

these things are changing like all the memory part is stored inside agent scratch pad apart

45:18

apart from that if you want to see intermediate steps for that also there is another function

45:23

which we saw in the program also so everything like for example every small detail that you

45:31

see inside a AI agent we can actually print it and see it that part only i'll try to show once

45:36

like we try to run the program. Let me check if all the PIP and everything is installed and then we can go ahead.

45:47

Lama 3.1 is almost ready to download. I'm just downloading all the other libraries.

45:53

Till here this part are you able to understand?

46:06

Yeah, right. Currently no piping is installed because we have already created everything. So that part will not be required.

46:27

Yes, right. All some of these methods are not compulsory. Like for example, if you see handling parsing errors, agent scratch pad, maximum iterations,

46:36

they are having default values also. So even if you don't write it inside the functions,

46:41

then also it will work. Only creating agent is required, agent executor is required,

46:47

agent executor again that if I don't write this part or if I don't write this part, then the default

46:52

value it will be used. So even that is not compulsory.

47:06

So let's try to see this particular part like we can see here. I think let me just quickly fix the environment also.

47:15

What is the issue?

47:22

Can you try running the program also once?

47:25

Like if you have downloaded Lama or just copy paste the program and then try to run it?

47:31

It might require Lama's this Lama.

47:35

this Lanchine Classic package. So let can you try just once?

47:49

Probably I think I'm not very sure, but I think these require Langean Classic.

47:57

Yeah, so I think you guys have to install this particular command, which is PIP install or PIP 3 install, this

48:05

particular part. I'll change it. I think LangChain Classic may agents. We have to install this thing. PIP install. Are you able to run the

48:21

command that I've shared in the chat? Can you try it very quickly?

48:35

for you. Okay, sorry. Let me paste it again. Now I think you can see it right.

49:05

That command is working right?

49:22

No, right, it will not occupy huge amount of memory.

49:25

Lanscher will not occupy huge amount of memory.

49:27

Ullama can occupy, but Ullama, you can run with quen model, which is the lowest model that is there.

49:35

Yeah, I think that will be needed.

49:42

So let me also change the program and push it.

50:02

If you have installed the command that I've shared, you can try.

50:05

running it again by updating the command. You need to update the main program. I'm pushing

50:12

that changes also in the background. If you see GitHub should be updated in next to one minute.

50:18

So I think it's updated right now. So you can use the latest program that is there. I've updated it.

50:23

Yeah. Now it is working. So we can see it is working. So we can see it is working. So we can

50:35

see very good results. Yeah, I am running it with this thing. It's a huge result that is there.

50:42

So let's try to see this part. Currently, please focus right now here. I am again discussing the output

50:48

and everything and then you can run the code later on also. Just focus on this particular part

50:54

right now and then we can go ahead. So you can see this that I have updated the program also. That program

51:00

will start running up. So yeah, Langchain Classic.

51:05

say you do it. Copy paste it clearly. I gave you the exact command that is there, right? Let me show.

51:16

If you see here, this command is there. PIP install.

51:27

What command I gave? Lanchine classic. Or PIP 3 install you have to do. So you can see it's working.

51:35

I tried it right now. This is the command right.

51:39

Lank chain you've after hyphen, say, so make sure that you are entering the command properly.

51:46

I have tested this command. It is working. And for you also, it will work. So let's discuss the output.

51:52

I'll share the command again in the chat. And for other people also, it's working. If you

51:57

write this spelling correctly, it will work. So let's see. I'll, I'll show the output. Please focus on the output right now.

52:04

So you can see this that. I have argued.

52:05

this question. What is the status of this particular order? So if I ask this particular

52:10

question, can you see agent has started executing? So it is calling some particular function or some

52:17

particular tool. What is that tool? Getting our order status. And currently if you see in this

52:23

particular part, I have hard coded these things. Like for example, in order to fetch the order

52:28

status and everything, you can see there is a basic database that I've created that order 101 made,

52:35

the status is shipped. The city is Delhi. The amount is this and the delivery days is this.

52:40

So I've just written this kind of data so that we can see proper answers. Otherwise, we will not be

52:45

able to see proper answers and everything. So we can see the order is currently shipped for Delhi

52:50

and the amount is 2,500. The tool response that was used to define the data. You can see this is

52:58

that this is the tool response that is there. And the tool response that was used for all

53:05

order 1, which is currently shipped with an amount of 2,500. The step 1 is get order status.

53:11

Input was this. Order 2001 is currently shipped and this. So this is the like the tool response

53:18

that was there. And then again, it is checking for different different orders. Like here I have

53:23

written different queries. Like for example, if I show you this particular part.

53:29

I have printed actually a lot of part. Like if you see in the first query, what I am trying to do, I'll just

53:35

uncomment this part and run it again so that we don't have that much output. Otherwise,

53:41

it can be a, it can be a, it can be a little bit confusing. I'm running the output again. Let's

53:49

try to see it again and see this part. So you can see this that currently if I write here

53:56

this part, what is the status of this particular order? So entire agent executor, it will start the

54:03

chain. It will call the necessary tools that.

54:05

present. You can see this that currently this order, it is in Delhi and the mount is

54:11

2,500. How it knows because it is checking this data that is present in the database. So you

54:17

can see I've created a hard-coded database from which it can pick the data. So it is picking the data

54:23

from this part that the status is shipped, the city is Delhi and the mount is 2,500. If you see

54:29

here this particular part, like for example, if you see this part, which is

54:35

Here you can see I am printing the step and everything. Here I think extra space I've added.

54:40

I'll just remove this space also and then again try to run it.

54:44

So we can see this that this space, if we see the output.

54:49

We can see different, different steps that are there. Like for example, currently only one step it is taking.

54:55

The agent, it is calling the tool to retrieve the status, which is currently shipped for Delhi and the amount is $2,500.

55:02

Get order status is called.

55:05

And the input is ORD101. And ORD101, it is currently shipped to Delhi and the amount is $2,500.

55:13

So you can see this is that this is the result of first query. It is showing me everything.

55:18

That which tool it is following, what is the input and everything, and what is happening, and what is the

55:24

final answer and everything. Same way for order 200 to check the status, delivery estimate and the

55:31

refund amount. So it will check this particular part. It will give me this recipe.

55:35

that order 102. It is currently canceled for Bangalore and the amount is 1,800.

55:42

We can verify it also. Like, for example, if I see here this part, the delivery status is zero days. The order is cancelled.

55:52

And the city is Bangalore amount is 1800. So correct answer it is giving. It is again saying that it is

55:58

canceled and no delivery timeline is existing. And this is the final thing. So the order is canceled. So the order is

56:05

canceled, it understands that the refund amount is 1,800. Since the order is canceled,

56:10

that is why it is saying that the refund amount is $1,800. And delivery estimate, it does not exist.

56:17

So if you see the question, I have asked in the question, the status delivery estimate and the refund amount,

56:23

that is why you can see it is giving me a proper answer. So all these things that you see right in

56:28

orange color and light green color, this is the final response that is there. In this final response,

56:34

in order to get this final response.

56:36

Multiple times, multiple tools has been called.

56:39

You can see this, that get status, get order status has been called.

56:45

Estimate delivery timeline is called.

56:48

Calculate the refund amount is called.

56:50

So you can see step by step which tool is getting called.

56:53

So the main idea of this particular part is right.

56:57

Like if you see here whenever I am calling the agent in the agent executed, since I have written

57:04

here, return intermediate steps is equal to true. That is why I am able to print this thing.

57:11

Otherwise, I will not be able to print this particular part. And you can see this that I have written

57:16

that space, right? Since I'm writing that space, if you see in the output part, that is why this space is

57:22

coming. Otherwise, it will be like step one, step two, step three. So these are the three steps that

57:27

we can see using which it is doing everything. Like using this particular part, it is giving me

57:33

proper response. So this is a response that is coming. And we can see this that

57:37

entire agent may joe be the status of this particular order is cancelled. Whatever things

57:44

it is trying to do, whatever output it is generating, this is the final thing. All these things

57:50

it is getting from different, different tools that are present. Same way if I ask it,

57:54

what is a delivery timeline for this particular order? So it will invoke some particular function.

58:00

It will say no order is present. It seems that.

58:03

there is an issue with order information. However, I can look up again. So it is again trying

58:08

to look up and it can see this that this particular order. If you see this particular order that is

58:16

there, it is not existing. Currently, you can see order 103, 101 and 102 is there. If I try to run it

58:22

with ORD 999, then that order is not existing. Since it is not existing, it called the first

58:28

tool which is estimate delivery timeline. Why it is calling estimate delivery timeline? Why it is calling estimate delivery

58:33

because the question is what is the delivery timeline for this order? That is why it is calling that particular tool. Is this idea clear? This part are you able to understand or not understanding?

59:03

Yes, right. It auto evaluates the query that is there. It finds the necessary tools, how it is finding the necessary tools.

59:13

Because we have defined all the tools. Like if you see, I'll again explain the program in detail from the scratch.

59:19

So let's try to see. So one by one, let's try to see different different parts. You can see we have this agent executor. Inside this agent executor, I have given the model name, URL and temperature, everything.

59:32

Here can you see that when you see that.

59:33

I am defining a tool calling agent. In that particular part, I am passing the tools. I am passing

59:40

the prompt and I'm passing the LLM. So it knows here at this particular point that what are the tools that are there.

59:47

Whenever agent is executing, there also am passing the same list of tools that are there. If I pass different

59:53

list of tools, then other things will happen. Like it might call other tools also that are there. But generally we will try to keep the same tools that are there in the agent and at this.

1:0:03

place. Here in order to see the execution logs, like for example, if I make it to false, okay. Now you will see that internal logs will not come up. Like for example, if I run this program again, then some internal logs will not show up. Currently you can see only this much is coming. Do you remember earlier pink pink, green, green and different colors were coming? Do you remember that part?

1:0:33

Correct, right? So you can see that what is the main purpose of this verbose?

1:0:38

The main purpose of verbose is to show internal execution.

1:0:43

If we'll say false karder then we will not be able to see.

1:0:46

Then you can see this that currently nothing is failing, but if it would be failing, then it will try two, three times.

1:0:53

Currently you can see in one go only it is able to find out everything. Like in one step it is finding out everything.

1:0:59

Here in three steps it is finding out everything. Because three things we need to calculate.

1:1:03

That is why three tools it is falling. Otherwise, you can see this that it will like if it now I cannot ask it to fail, but if it was failing, then it will retry three times. That is the main purpose of this particular part, which is maximum iterations. Now, if let's say that I make this parsing error to false. Now, if there is any parsing error, right, then in between it will fail. So I'm now it depends upon luck that if parsing error comes on.

1:1:33

not. I can try to run it, but if there is internally some parsing error, you will see that it will crash.

1:1:40

But currently, we are not that lucky that it is all. There is no parsing error, so that is why it is not crashing.

1:1:46

But if there was any parsing error, then in between it might have crashed. Currently, we cannot see that part, but you can even change it and then try.

1:1:55

If you actually set this particular value to false, which is return intermediate step, then this program might not run.

1:2:03

because you can see this that I am trying to print all the steps.

1:2:07

But here here there you see these steps are coming because I am writing that flag is equal to true.

1:2:16

I am writing here in the program, this particular part, return intermediate steps as false.

1:2:22

If I write it as false, then no steps will come.

1:2:25

So let's try running this program again.

1:2:29

So you can see this that if I now try to run the program, you can see it is failing.

1:2:33

Why it is failing? Because steps are not coming.

1:2:35

So why steps are not coming? Because you have said this to false.

1:2:39

If I set it to true and I again run it, then you can see this that.

1:2:45

Now it will work and you should be able to see steps and everything that is there.

1:2:49

Is this idea clear?

1:2:53

This part are you able to understand?

1:2:56

So you can even try these things like verbose if you make it true, then you will see automatically internal logs will start coming.

1:3:03

Those are internal logs. Now those logs internally they have set the color. So that is why this color is coming. You can see all these are internal logs which are coming in different different colors, right? Like pink color, light green color and all these colors. These are internal logs. So I am not printing them. Agent is printing them. So you can see this that they have defined that colors. I have not defined it. So if I set it to false, I will not see any internal logs. And what I can do is I can even run the program normally.

1:3:33

And I can see this kind of output.

1:3:35

So this output will make things more clear that if I ask the status, then you can see only status it will try to show.

1:3:43

If I ask this particular question that what is a delivery timeline?

1:3:48

Then it will again call delivery.

1:3:50

Like currently it is not calling the delivery timeline.

1:3:53

Yeah, it is calling the correct tool, which is get delivery timeline.

1:3:56

Here if I ask three things, the check status, the delivery estimate and the refund amount.

1:4:02

Then it is called.

1:4:03

correct tools, which is get order status, estimate delivery timeline, calculate

1:4:08

refund amount. So it is calling the correct tools and it is giving correct answer. Since I have

1:4:12

already downloaded Lama model also, I can do here this particular part that rather than this

1:4:17

quen model, I can update it here to the Lama model as well. And even if I run it, then also

1:4:24

it will go out. So with Lama model also we can try.

1:4:33

Now it will use the Lama model and we can see this that same thing will come up.

1:4:39

So you can see this that Lama model currently what it is doing.

1:4:43

It is calling the same tools get order status.

1:4:46

It is calling here three tools.

1:4:48

Here it is calling one tool.

1:4:50

And you can see almost same responses are there.

1:4:57

Which steps you are talking about Nupur?

1:5:01

So we can see this.

1:5:02

see this like let's see one by one. I'll show you the entire program from scratch. So one by one we can discuss.

1:5:09

So we can see initially I've added here this particular part. This is only for importing thing.

1:5:14

And you can say today we have imported a new package. What is a new package? Lankchain Classic. It contains the agent.

1:5:22

So in order to have this particular line, what do you need?

1:5:25

You need to run this command, which is written on the program also.

1:5:29

PIP install Lanchine Classic.

1:5:31

classic. So I'm pasting this command, which is PIP install Lanchine Classic.

1:5:36

Or you can see here PIP 3 install Lanchine Classic. So if you run that particular part,

1:5:41

then only it will work. Correct. Then otherwise we can see this that if I just write Lank Chain

1:5:47

agents, it will not work. So even that part I've added here. Dot Env file I'm loading up. This is just

1:5:53

for if you want to run rather than currently I'm running from local models. If you want to run it from

1:5:59

the cloud model also, then you want to run it from the cloud model also, then you

1:6:01

you can use the NV file and then import it. The temperature is zero only. Like currently,

1:6:06

everything is coming from directly the static values that are there. Now this order database,

1:6:12

it's a in-memory database that I've created. This in-memory database, it is just telling the results. Like,

1:6:19

for example, for this particular order, these are the details that are there. For this particular

1:6:24

order, these are the details that are there. For this particular order, these are the details that are there.

1:6:29

So you can see this that this part is there. Now I've registered multiple tools.

1:6:35

These tools are actually inbuilt Python functions only. Same thing which we did it in the last class.

1:6:40

Same thing we are trying to do now. That we have taken some inbuilt functions that are present and each

1:6:45

function is we are registering it as a tool. So you can see this is that this is another function. We are

1:6:51

registering it as a tool. This is another function we are registering it as a tool. This particular

1:6:56

part we are trying to do. I have added three tools.

1:6:59

and I have made a list of tools as well.

1:7:01

If you remember in the last class, we were having a tool map also,

1:7:06

which was telling that this name pay, this is the tool.

1:7:08

That was required because I was manually calling all the necessary tools that are there.

1:7:14

Today, since I'm not calling all the tools manually, that is why I've not created that kind of map.

1:7:19

So this part you need to remember, like you can carefully analyze the last program that we had in the last class.

1:7:26

Like if you check here this particular part, which is,

1:7:29

Lanchine voila. You can see this program. In this program if you see that I have defined here

1:7:38

all the tools and I am calling a tool map because I need to call tools manually. I need to manually

1:7:44

call all the tools. That is why I am writing this particular part. But today we are not doing that

1:7:49

because we want to automate that particular part and how that automation we are doing. We are doing

1:7:55

that automation with the help of new functions that we are learning today. What are the new functions that we are learning

1:7:58

today. What are the new functions? We can see two new functions are there and their

1:8:03

parameters are there. So you can see the first function is tool calling agent. We are creating

1:8:08

an agent. Agent is comprised of three things. Like it can have prompt. That prompt is a main prompt.

1:8:14

That what it needs to do. It can have memory also. Currently we are not keeping any memory. Why?

1:8:20

Because there is a single query. Remember this particular part. That each query is not related to

1:8:28

the previous query that is there. If I wanted here, multiple queries. Do you remember?

1:8:34

I'm not sure if I'm not sure if I've shown you that example where on N8N, that memory example,

1:8:40

have I shown you? I can show you that particular part also, but I think you need to understand this thing.

1:8:49

Like, do you remember that chat GPD example that we discussed for short-term memory and long-term memory?

1:8:54

I think in short-term memory and long-term memory, we did discuss that part.

1:8:58

I'll show you. I think chat GPD example, you remember that chat GPD is aware of all the conversations that are there.

1:9:07

And I'll show you that in an example also right away. So you can understand that part. But the main idea is currently our agent does not have memory. Since it does not have memory, it does not know what is a previous question. Like for example, if I ask it here, let's say the first question is what is the status of the order. And if I ask it, what was a

1:9:28

previous question, then it won't be able to reply because it does not have memory.

1:9:32

It has only the system prompt. It has the LLM. And it has other things that are there, which are the necessary

1:9:40

tools that it can call. Because currently the main idea is to see how tools are working. So that is

1:9:46

why you can see here that these tool calling part we have added. Once we add that particular part,

1:9:53

we can see here this thing that I have created a basic LLM. I have called. I have called.

1:9:58

a agent. So this is a new function that is there, which is the tool calling agent.

1:10:02

Inside this tool calling agent, what I am trying to do, I am trying to pass LLM tools, prompt and

1:10:08

everything, memory we are not passing. And then to execute this particular agent, what we are doing,

1:10:14

we are writing that what is the agent tools. We saw these are nothing but different, different parameters

1:10:20

of the function. If I write verbose equal to true, I'll see more logs. I'll see the internal logs that are there.

1:10:27

If I write verbose equal to false, I'll not see the internal logs.

1:10:31

If sometime the agent is failing, then on retry, it will do Atmex 3 retries. After that, it will

1:10:37

completely fail and crash. If I write it more, then it will retry many other times.

1:10:44

If I write here parsing errors to false, internally currently there is no parsing error.

1:10:48

So even if I write true or false, nothing will change. But generally it is used to handle all the

1:10:53

parsing errors that are there. Intermediate steps will.

1:10:57

if you write intermediate steps equal to true, then only you will be able to see these kind of

1:11:03

intermediate steps. Like for example, you can see three steps are getting called and all these things

1:11:08

are happening. Is that idea clear?

1:11:17

Guys, this part are you able to understand?

1:11:23

So you can see the main idea is that I have written here this part.

1:11:27

that return intermediate steps. They are telling me about this thing. That what are the

1:11:32

intermediate steps? Intermediate steps? It means that our tool call, like

1:11:37

any query for a multiple tool call are like for example if we see this particular

1:11:41

query in this query multiple tools are getting called. Since multiple tools are getting

1:11:46

called we can see this kind of result. I think this idea is clear.

1:11:52

By I have run this program with intermediate steps equal to true right? If I run

1:11:57

it with false, then then steps are trying to print all the steps, then it will

1:12:03

definitely fail, right? Is that idea clear? Shandy. So if you see this, that if I write it false

1:12:09

and then try to run it because you are writing this code. If I don't write this code, then it will

1:12:14

work. Like for example, if I comment this code and then what I do is I write here intermediate

1:12:20

step equal to false. And now I'll run it, it will work. So let's

1:12:27

try that. Since now I'm not printing the intermediate step, there shouldn't be any

1:12:34

such error unless and until other error can happen. So you can see now it is working. So it is

1:12:41

directly giving me the answer that this order is shipped in Delhi. This order is I think order 102,

1:12:50

it is saying canceled. Ideally, I don't think, okay, it is canceled only. Correct. It is saying.

1:12:55

And here you can see this is that. This order.

1:12:57

does not exist. Correct, right? So yeah, correct thing it is saying. So if I want

1:13:04

intermediate steps, I can see it that part from here and I can print those intermediate steps also.

1:13:10

Even that part we have seen. Apart from that, let me check. Prompt we have discussed,

1:13:18

LLM we have discussed. Then apart from that, this is nothing but printing the intermediate steps and

1:13:23

everything. That part we have seen. Apart from that, I have.

1:13:27

added some basic test case that which tool should be called or not. So this is just

1:13:32

verifying whether the tool is getting properly called or not. So if I even run this particular

1:13:37

part, then you will see this that it will just check whether tools are called properly or not.

1:13:42

So even that part I can check. So you can see these are the orders and you can see this

1:13:53

that it is we are just verifying. I have just verified here.

1:13:57

that whether the tools are properly getting called or not. Like for example, if the query is,

1:14:02

what is the status of 101 order? Then since this particular query is there, it should call get order

1:14:08

status. So we can see it is passing. It is calling all the three. It is passing. If I ask

1:14:14

can a book for a flight from Mumbai to Delhi, it shouldn't call any particular tool. It is passing.

1:14:20

Where is my refund amount? It should actually call like this particular thing. The expectation.

1:14:27

what is my refund amount? I think this test case is incorrect. We should ideally

1:14:33

like if we see here in the query, what is there? Yeah. If no order ID is there, then it should not call.

1:14:42

That is the main idea. But even if it is falling, it depends upon the model. Like,

1:14:47

this pass or fail is, it actually model dependent. Like if I change here the model, then things will change.

1:14:54

And if I use here chat GPT's a good model, then

1:14:57

all of them will pass because that model is strong. Like for example, if I use here

1:15:02

quen model and then try to run, then you will see different output will come up. So let's even try that.

1:15:11

So now I am running the test case with when model. So you can see only this test is failing.

1:15:21

What is my refund amount? Because as soon as it sees refund key, what it calls that particular tool,

1:15:27

refund, but it should only call it based on the order ID. I think even if we don't

1:15:32

write since we have written refund, it will definitely call it, but it won't be able to execute

1:15:38

anything because order ID is not there. So ideally, it shouldn't call, but it depends upon the model.

1:15:43

Like, we cannot do anything because we don't do not call. Call to model is using its brain and then

1:15:51

doing it. We cannot change that particular part. But you can see these are nothing but basic test cases.

1:15:57

I have written to verify whether correct tool is getting called or not.

1:16:01

I think this part is clear, right?

1:16:04

This part are you able to understand?

1:16:07

Sunupur we can wait, right?

1:16:08

Currently I think till here, this entire program are you able to understand?

1:16:15

Which step you are saying?

1:16:17

I mentioned the steps, right?

1:16:18

If you see here this particular part that I have registered all the tools and I have provided a list of tools that are there.

1:16:25

If I've provided a list of tools that are there.

1:16:27

Then this agent, this particular agent that is present.

1:16:30

If you see inside this particular thing, I provided the list of tools.

1:16:34

So it is aware of all the tools that are existing.

1:16:37

Is that idea clear?

1:16:41

Guys, this part are you able to understand or not?

1:16:57

We can discuss our doubts in like one by one.

1:17:00

But till here, the basic working of program is clear.

1:17:04

So you can also run the program now and execute it.

1:17:07

But I think this part is clear.

1:17:09

Yes, right.

1:17:10

Binding is done automatically.

1:17:12

Currently, we can see this.

1:17:13

We don't have to call these binding functions that are there.

1:17:16

If you have installed everything, how many of you are able to run the program?

1:17:22

Guys, how many of you are able to run the program?

1:17:27

We are checking using the step part, right?

1:17:31

Like using the step part only we are checking whether which tool call is made or not.

1:17:36

We can even print the internal logs and see that.

1:17:39

We saw that particular thing, right?

1:17:40

All the internal logs were coming that which tool is getting called.

1:17:44

Correct?

1:17:47

So, Bunkajam, you land chain, install.

1:17:49

You have your environment isn't set.

1:17:52

So that's how it will be?

1:17:55

Your environment is not set properly.

1:17:57

that is why it is not working.

1:17:59

Just set the environment properly, it will start working.

1:18:16

Let me see if I can show you other part of this.

1:18:22

Yeah, so I'll show you one more thing.

1:18:24

I think this thing also you need to understand.

1:18:27

So you can see this that once you install it and restart Visual Studio.

1:18:32

Remember this, that once you install it and then restart Visual Studio,

1:18:36

then you will see this particular part that there are multiple things that I can provide.

1:18:40

Like for example, I can even provide how to format messages and all.

1:18:44

I can provide multiple things.

1:18:46

There are many functions.

1:18:47

There are different functions for providing memory also.

1:18:50

Those also we can see.

1:18:52

But there is one main function which is create tool calling agent.

1:18:55

This particular age, like this.

1:18:57

particular function is expecting LLM tools and the main prompt that is there.

1:19:01

Apart from that, we can see there is this agent execute function.

1:19:05

In this multiple things I can provide the agent, the tools, the intermediate step if you want or

1:19:11

not, maximum iteration. So we can see this that at max the maximum iteration can be 15,

1:19:17

not more than 15 I think it will take. Apart from that execution time also we can provide all these

1:19:22

things we can provide. Apart from that, I think early stopping method is there.

1:19:27

that if I want agent to stop early, that thing also I can provide.

1:19:31

Parsing error also I can provide.

1:19:33

So you can see a lot of functions are there, which we can provide.

1:19:36

But currently we are using the default value of those functions.

1:19:40

I think this idea is clear.

1:19:41

You don't have to set up ENV file for this particular program.

1:19:45

Since we are using all the models which are locally running, you don't have to set up that.

1:19:50

Currently, you can run it with this configuration, like whatever configuration I am using.

1:19:56

Let me again run this.

1:20:04

I'll push the latest code.

1:20:08

I think currently for me also, the environment is not activated.

1:20:13

I need to activate the environment properly and then only it will work.

1:20:17

I'll open a new terminal and see if environment is getting activated.

1:20:23

No, environment is not active.

1:20:25

Now I think.

1:20:26

it is active.

1:20:30

So if environment is not active, then it will not run.

1:20:33

So you can see for me also same error is coming that no module name this because environment

1:20:38

nae active.

1:20:39

One bar environment active then you will see the program will start working.

1:20:42

So you can see this that this is the thing that is happening.

1:20:46

All the steps I can see that these are the steps that are present.

1:20:50

I can see all different steps that are there.

1:20:52

Mainly two main functions we are using.

1:20:54

What is the first main function?

1:20:56

the first main function that is present.

1:20:59

It is this one, which is tool calling agent, this one.

1:21:04

And the other function that we are having is the agent executor.

1:21:07

I think this idea is clear.

1:21:09

Till here, this part are you able to understand?

1:21:17

Still here, this part is clear.

1:21:22

Only one second, a one setting is required, right?

1:21:25

You need to install.

1:21:26

all these things that are there.

1:21:30

Till here, I think the idea is clear.

1:21:32

You can run it in this way currently.

1:21:34

I'll push the latest code also.

1:21:36

You can copy paste the latest code.

1:21:45

So you can run it without the intermediate step.

1:21:49

So if you copy paste the latest code, then intermediate steps will not be there and you will see this

1:21:53

kind of output.

1:21:54

This output is more readable.

1:21:56

So this particular output you can see.

1:21:58

You can use the latest code and fix your environment.

1:22:02

Then if you run it, it will work.

1:22:03

I think till here, this thing is clear.

1:22:06

So you might have to activate the environment, right, Pankraj?

1:22:09

We can share your screen in some time and then we can see.

1:22:12

I think till here, this idea is clear.

1:22:14

How many people are able to run the program and understand all these functions?

1:22:17

Can you write in chat?

1:22:23

So you can see whatever demo code I've written in the PPP.

1:22:26

same demo code I have already written and we have discussed the entire program.

1:22:30

You can check out the same thing in the PPD as well as in the nodes.

1:22:33

Correct, right?

1:22:34

Go on Avanish, what is the doubt you are having?

1:22:37

Mm-hmm.

1:22:38

One by one we can see that part and then probably we can see the issues that other people are facing.

1:22:44

Go on Aminash, what is it out?

1:22:46

Then probably I think who was there, yeah, go on.

1:22:49

Mm-hmm.

1:22:50

Hello?

1:22:53

Can you have me?

1:22:55

Yes, yes.

1:22:56

go on.

1:22:57

So I was just checking here in the line after the definitions have been done, tools that you

1:23:04

have declared.

1:23:05

Which which?

1:23:06

Which?

1:23:07

Which?

1:23:08

And the tools that you have defined.

1:23:10

Okay.

1:23:11

I have defined all the tools.

1:23:12

Okay.

1:23:13

Line number one that is explored.

1:23:15

Get all right.

1:23:16

You find an estimate.

1:23:18

So, I mean, you explained it later, but I just wanted to understand more on that part.

1:23:23

If we add into that or how, how do you explain it?

1:23:25

How do the entire flow work somewhere?

1:23:27

How do we use this tool?

1:23:29

And getting from last class also.

1:23:32

Just a little bit more light on with that.

1:23:35

It's slightly difficult for me.

1:23:37

Currently what we are trying to do is we are doing this particular part

1:23:40

that we are having here internal functions that we are registering as a tools.

1:23:45

And we have created a list of tools that are there.

1:23:47

Now if you see in lag chain, all the functions that are creating,

1:23:51

like all the functions that we are calling,

1:23:53

they require the sequence.

1:23:54

the sequence of tools that are there that the agent can internally call.

1:23:58

Now those tools can be anything, like those tools, let's say that today, if I want to integrate

1:24:03

with any third party API, like for example, I want to integrate with any SGK or any particular

1:24:09

API that is there, then we will have to write some code, like we will define a particular function.

1:24:15

That particular function might be internally talking with IRCTC.

1:24:18

So inside this particular code, I'll call IRCTC and do that particular part and I'll register

1:24:24

it as a tool. So what will happen is model will understand. If user is saying anything

1:24:29

related to IRCTC, it will call that function. And this particular function will internally,

1:24:34

what it will do is it will try to call that particular API. Is that part clear?

1:24:40

Yes. Now you are able to understand, right? So let's say that if we change the example,

1:24:44

currently we are just finding everything from the database part. But ideally what I could have done

1:24:50

is I could have called here real APIs. Like for example, this API might be calling

1:24:54

internally Amazon. In order to get the refund and everything, it might be calling API of

1:24:59

Razor Pay. In order to get the delivery timeline of everything, it might be calling, let's say,

1:25:03

Swiggy. So now these functions internally can call APIs and how they will call API. That particular

1:25:11

part we have already seen in the API call example. So if you see here this particular screen,

1:25:17

then you can see here that different different APIs we can call. Like for example, we can specify the URL.

1:25:22

we can specify the request and everything, whatever we want to make.

1:25:26

We can call those APIs, store the result in JSON format, and everything can be done.

1:25:31

So you can see that these functions are nothing but calling real-time APIs.

1:25:35

So these functions can also be registered as a tool.

1:25:37

I can just write here one more line, add the rate tool, and they will be registered.

1:25:41

And then my AI agent will be understanding.

1:25:44

Okay, if user is asking this particular thing and this data is coming from external part,

1:25:49

then it will automatically call the tool.

1:25:51

I think this idea.

1:25:52

is clear. Right? Correct, right? This way a model can understand and relate based on

1:25:59

user query that went to call which particular tool, correct?

1:26:04

Not. I think till here, this part is clear. Now, let's go to the next person. I think

1:26:13

Nupur, you were able to understand this thing. Did you understand what things we were discussing?

1:26:22

Yes, hello. Can you hear me?

1:26:24

Go on.

1:26:25

My question is regarding the tools.

1:26:29

Whatever it is defined under the tool, three tools in this particular example, do we need to write these tools on our own?

1:26:36

Or how does it work basically in like in practice?

1:26:38

But only just now we discuss that these tools we have to define on our own.

1:26:42

Like for example, if I want my model to call any particular API, then that particular API code we need to write here.

1:26:49

Currently, we are writing basic code which is fetching some data.

1:26:52

from orders and everything. Like for example, it is just a nothing but a dictionary that is

1:26:56

created, which is fetching some data. Same part you can see here also it is giving, fetching the

1:27:01

results from dictionary. There are also the same thing. But later on, what I can do is I can actually

1:27:06

replace it with API calls that are there. Like as we learned in the API class that we can call

1:27:12

different different APIs. So we can write that particular code and in real time model we'll be

1:27:17

calling some API and that particular API might give real time data. Like for example, I can change

1:27:22

use this particular code and I can make it an agent which where the user query is like

1:27:26

what is the current temperature of Bangalore then it will internally call the weather API

1:27:30

get the real temperature of Bangalore and return me the real temperature. So these things can

1:27:35

be done. So I have to on my whole point is that at the route after that or at the rate tool after

1:27:41

that whatever defined definition is there for the tool. We have to write I have to understand

1:27:45

this whole thing what is happening in this particular commands and all the commands.

1:27:49

Correct right. That particular part you need to

1:27:52

write it. You need to understand currently the meaning. If you remember that I've already

1:27:56

shared you a video on context engineering, right? Did I, did you watch that video?

1:28:01

No, no, I have not. I have the link, but definitely. Just watch it, right? You will understand

1:28:06

that writing code is not a big thing. Like for example, these days anyone can write code.

1:28:11

The only thing is that you should have mean understanding how the code is working. So I'm sharing

1:28:16

one more video link that how you can do something called as advanced by coding using the

1:28:21

advanced context engineering. I've shared the video in the chat. You can watch that particular

1:28:26

video. So we just have to do the context set up. And that once that particular context setup is done,

1:28:32

we can easily write the code. So that won't be a big issue. Correct? Okay. My next question is

1:28:37

regarding that steps, intermediary steps, which you're saying that three steps in my output as well,

1:28:43

the steps are there. My question of where are these steps defined in my whole command? In the command,

1:28:49

and is there any steps defined?

1:28:50

We have to find it right. Like if you see here this particular line, which is line number

1:28:54

190, we are saying intermediate steps is equal to true.

1:28:57

True. This means that this means that when the agent is executing, it will be calling

1:29:02

multiple tools starter there.

1:29:03

Who joe be tools call carer, he will store

1:29:05

that he'll call as a step. Now, so the three tools are the three steps.

1:29:12

Correct, right? So if I ask this kind of a question, yeah. So if I ask this

1:29:16

find a kind of a question that we find the check status delivery timeline.

1:29:20

an in refund amount. Then you will see this diet. What it will do is it will call the agent.

1:29:25

Agent will internally call three tools. And that three tools will be registered as a step. And

1:29:29

then we are printing that particular part. That is why when I am running the program,

1:29:33

we can see all these steps are coming. Like all the steps that are there, they are coming here.

1:29:38

They are coming here because I'm manually printing them. I have stored that result from get

1:29:43

functions is equal to true. And then I'm printing them. That is a thing that is happening.

1:29:47

Now I got it. Thank you. So, thank you.

1:29:50

Thank you.

1:29:51

Thank you.

1:29:52

Yeah.

1:29:53

Let's move to the next person.

1:29:55

I think Rajesh Taneja, where are you stuck at?

1:29:58

Other people, I think, are you able to understand?

1:30:03

Go on, Rakish. Where are you stuck at?

1:30:08

Hello.

1:30:10

Can you hear me?

1:30:12

Yeah, I can hear you. Go on.

1:30:14

I'm just trying to understand the difference from the previous class to this class and the

1:30:19

and the tools that we're discussing, right, the list of the tools.

1:30:23

So in the previous class, what we said, we have to manually call the tools and discuss

1:30:27

we're seeing the agent executor would call.

1:30:30

Correct, right? In the last class, we were saying that the lag chain can directly call,

1:30:35

like, we have to understand that LLM can return the necessary tools that are there.

1:30:40

And we were finding out the tools and then we were manually calling them with the help of invoke

1:30:44

function. So these all steps we were doing. So this was a very big step.

1:30:49

In actually these steps are not required today we are trying to see this particular part.

1:30:53

We are just doing an upgrade to the last class that there are some other functions that are created.

1:30:59

Like for example, the functions are execute the call, create a tool calling agent and agent executor where they will understand everything and they will internally call the tool.

1:31:08

So now we have the complete understanding that if I ask any particular query that what's the temperature of Bangalore right now.

1:31:15

Or let's say what are the flights from Hedrabart to Bangalore.

1:31:18

Then internally,

1:31:19

rather than writing these kind of functions, I could have written a weather API code.

1:31:23

I could have written a sky scanner code which can find out all the flights.

1:31:27

So model will in real time call the necessary tools, get the real time data and give you the necessary

1:31:31

data that is there. Correct. Yeah. This is all local versus when we have to call it to the net,

1:31:36

right? Using your place. Correct, correct, correct. Yes. Okay. Thank you. Yeah. Go on,

1:31:43

Pankaj. Where were you stuck at? Yeah, issue are, Pankaj.

1:31:49

Yeah, Rahul Verma also, go on.

1:31:51

What, where are you stuck at?

1:31:57

Hello.

1:31:58

Yeah, go on.

1:31:59

I can share my ad.

1:32:02

I'm getting there as in the program.

1:32:05

Share your screen.

1:32:07

Okay.

1:32:19

So did you install the libraries and other things correctly?

1:32:31

You are on mute, Rahul Verma. Can you quickly share your screen?

1:32:36

Okay.

1:32:37

Yeah.

1:32:38

Just just a second.

1:32:40

Ridjoo, till then, do you have a theoretical doubt or what is a doubt you are having?

1:32:45

Yeah, theoretical doubt means you can hear me, right?

1:32:49

Yeah, yeah, I can hear you go on.

1:32:51

Yeah, yeah.

1:32:51

So when we are actually, instead of writing the local database and local ports there,

1:32:57

if we are actually trying to get it from the outside, outside tools,

1:33:02

get it integrated with the outside tools.

1:33:05

Then my question is, suppose those outside tools will be having their own vector DV as their

1:33:11

information base, right?

1:33:13

That can have a vector debut or it can call third party IPAs also to get the data, right?

1:33:17

Every time it's not compulsory.

1:33:19

we will make vector DB.

1:33:20

We will make it once we are having a rag part, right?

1:33:23

Yes, yes.

1:33:24

But here, I mean, we are not using the rag part, but we are actually just trying to see the

1:33:30

agentic behavior of the of the Lanchin.

1:33:33

But here, if we want to integrate any RAD, then like for doing that.

1:33:38

I think we'll be doing that in Lanchine, there is a function that is there.

1:33:42

You like Lanchine has a specific function of Rag, which internally creates a vector database and

1:33:47

does everything.

1:33:48

So it will be.

1:33:49

present in Lanchin core only are a Lanchin rag part.

1:33:52

So I think we will be covering that in this force also.

1:33:55

I think later on classes it will come up.

1:33:57

Okay, okay, bro.

1:33:58

And another thing, I had a question on the grounding and with the cosine thing,

1:34:03

uh, thing basically.

1:34:05

So, uh, will you discuss it now or at the end of the class because that will be

1:34:10

something out of the context of this class?

1:34:13

Yeah, let's fix this.

1:34:15

I think Rahu's were my error than we get to see.

1:34:18

Yeah.

1:34:18

Okay.

1:34:19

Rahul, can you type it, Rulama pull?

1:34:22

Olama pull and look at Olama list type.

1:34:25

Olama list.

1:34:27

Olama space list.

1:34:30

Now we're looking at quen model.

1:34:31

Now, one program in the run you.

1:34:33

Program in the program in the top of go.

1:34:37

Goophe scroll up.

1:34:38

Here here model's name is right.

1:34:39

Right.

1:34:41

Point, 0.5.

1:34:45

scroll to a one.

1:34:46

All right.

1:34:49

Just this is.

1:34:51

Name, right.

1:34:52

Ullama list you can't see.

1:34:53

You can't.

1:34:54

A terminal a little bit.

1:34:55

Terminal to throw up.

1:34:56

Strow.

1:34:57

Yeah.

1:34:58

Good.

1:34:59

Okay.

1:35:00

Ollama 2.5, 0.8.

1:35:02

Okay.

1:35:03

Now, now,

1:35:04

yeah,

1:35:05

type, Python.

1:35:06

code.py.

1:35:07

Pye.

1:35:08

So run

1:35:14

run.

1:35:15

It's then.

1:35:16

It's then.

1:35:17

Entering, and execute and execute.

1:35:20

So.

1:35:21

So,

1:35:22

up you're up there was a error

1:35:24

was going to.

1:35:25

This same.

1:35:26

I don't know how it's going.

1:35:29

Thank you.

1:35:30

Correct.

1:35:31

Right.

1:35:32

Okay.

1:35:33

Thank you.

1:35:34

I think till here, this idea is clear, right?

1:35:37

Where I had a little,

1:35:40

whether I had a little,

1:35:41

how to be damaged,

1:35:42

if I'm going to verify the answer is correct or not.

1:35:45

In the temperature part, it is.

1:35:46

temperature part it is giving the result from actual data right as far as I remember like if you see in the temperature part we were actually calling a API so like for example if you see here in this particular part we are actually calling the API of temperature that is there so it will give the real time manse right it is not giving any hard-coded data. This is hard-coded

1:36:07

code it is finding out the real-time temperature so if you try to return this if you try to run this API call part and you can even

1:36:16

will try this, try with cursor or anti-gravity or even plot you can try that you can take this program and make it into an AI agentic program, which is falling real-time API. I think that part also will be there in the later on modules. So even that particular part we will try to do where what we are trying to do is, we will try to see that how our AI agent is falling API calls. Even that part I think will come up.

1:36:41

So Amir, the answer to that particular question is that what we will

1:36:46

try to do this. We will try to the temperature that is coming. It's not hard-coded. It's a real-time answer that is there. Correct.

1:36:56

I think till here any other doubts from this particular class? I think till here, the doubts of this class are clear, right?

1:37:10

Now, did you go on? What is our doubt you were having related to which point? You were having doubt related to what?

1:37:15

grounding. So we are using the grounding in the rack basically. Now grounding is being

1:37:22

used before the generation step, right? Correct, right? So that

1:37:27

like augmentation step is a part, or generation step? It's a part. I mean? Generation step

1:37:34

after we've laid. Now, generation step in generation step in we can ground our answer. As a let's

1:37:39

let's say, if we, if we're in prompt me be told me, that like, like, how we're, like, like, we're

1:37:44

prompt me constrain. Same thing we're here in ground maybe trying to try

1:37:48

are specifying some constraints, which they were

1:37:51

specifying some constraints, which they'll do any full to output not

1:37:53

do so only that particular part we are doing. Apart from that,

1:37:56

so nothing extra thing is there. So it is part of the generation only.

1:38:01

Right, right. So we're just to, I mean, it's

1:38:02

to, I mean, it's to, I mean, three set, can't, five set, can set,

1:38:06

or seven sets, I mean, I'm a lot more. I'm set not going to, so it's a good. But

1:38:11

suppose we are doing that as three or five, or we have,

1:38:14

making that modification. So, is it a part of grounding? Is it a, I mean,

1:38:19

three or five, we're not? We're rank's not? The chunking in

1:38:23

we're ranking, we're making, like, like, right? But, I mean, I'm saying, but I mean,

1:38:31

I'm saying, suppose I've five did, or seven, so, so, so it's a lot of options,

1:38:35

he's got, right? Correct, correct. So, yeah, so after we're getting, so

1:38:39

we're all the options, then we're getting, that we're strict prompt for a lot. So, like, for example,

1:38:44

the user query comes, we embeds, we have embed from here from vector DBs

1:38:49

ranes, if our ranks are like, let's say, five to seven.

1:38:53

So if since my ranks are five to seven, I'll try to make this, like, in the user

1:38:57

prompt, we are sending here this particular part, we are sending the user input and the

1:39:01

chunking part. And now, now I've got here from here from here from, then the LLM

1:39:06

generation in prompt is, that I'm very strict to. I'm more strict to make that. I'm more strict

1:39:09

I think that if any chunk is useless,

1:39:11

it directly ignore it. I'll just

1:39:13

this constraint add to that answer

1:39:15

we have grounded. That it could

1:39:17

it would be the seventh chunk from

1:39:18

some of the wrong answer

1:39:19

made, so we've made up new

1:39:21

product to add. So as

1:39:23

as we're just as we

1:39:23

this chunk, this number

1:39:25

increase, we'll, like, we're

1:39:27

we're, like, we're, like,

1:39:29

more come to, like,

1:39:30

this problem more strict

1:39:31

more stricted.

1:39:32

System prompt to be more strict

1:39:34

context, I mean, in the constraint part

1:39:37

in, correct, correct.

1:39:38

Correct, correct.

1:39:38

So, actually, to discuss that scenario,

1:39:42

only I have come to the chunking part from grounding.

1:39:46

So the grounding we're doing, suppose I

1:39:48

I'm running, suppose I've ranked,

1:39:50

your middle somewhere,

1:39:51

I've got quite, not quite

1:39:53

much, but not right?

1:39:55

And suppose in the middle, something,

1:39:57

five or something, I've

1:39:58

made so that it does not miss out on any particular chunk

1:40:01

to, I mean, for becoming very strict.

1:40:05

So that, after, the grounding strategy,

1:40:07

in the way we're discard

1:40:09

and downing strategy can be

1:40:11

decided based on the system

1:40:13

prompt only, right?

1:40:14

Correct, absolutely correct.

1:40:15

So you're the diagram

1:40:16

you're in it, you know, you know,

1:40:17

like, if we're doing,

1:40:18

if we're three things

1:40:19

are making, where we're

1:40:21

like that we're taking,

1:40:22

so we're not strict

1:40:23

not so strict prompt

1:40:24

not, because we're three

1:40:26

only chunk, but if I

1:40:27

if I'm five

1:40:28

do it, then that

1:40:29

better will, but if I

1:40:30

I need, like,

1:40:33

five, a good chunk,

1:40:34

chunk, so I'm more strict

1:40:35

to have this strategy

1:40:37

this is always better

1:40:38

in racked case

1:40:39

so we're

1:40:40

we're here

1:40:40

strict answer

1:40:41

will be the strict answer

1:40:43

is our grounded

1:40:43

answer kind of

1:40:44

but if we're

1:40:45

our chunk of

1:40:46

we're making

1:40:46

we're making

1:40:47

basic a system prompt

1:40:48

we'll

1:40:48

make the three of

1:40:49

go up

1:40:50

go and

1:40:51

whatever three chunks

1:40:51

make and then

1:40:52

that's chunk

1:40:53

and then the chunk

1:40:53

answer

1:40:53

to try try

1:40:54

this one part

1:40:55

and this

1:40:57

grounding

1:40:58

we're from

1:40:59

we're from

1:40:59

we're through

1:41:01

correct?

1:41:01

correct, correct

1:41:02

system problem get through

1:41:03

are all right

1:41:04

okay okay

1:41:05

here

1:41:05

we're actually

1:41:06

actually

1:41:06

not doubt

1:41:07

so I'm

1:41:08

asked

1:41:08

because I'm

1:41:09

the causal

1:41:09

similarities

1:41:10

are that

1:41:11

that's

1:41:11

I'm

1:41:12

know that

1:41:12

I'm

1:41:13

looking at

1:41:13

the angle of

1:41:13

I'm

1:41:14

know that

1:41:15

so if we're

1:41:15

making

1:41:15

lesser

1:41:16

number in

1:41:17

rank

1:41:17

so

1:41:17

that is

1:41:18

basically

1:41:18

very similar

1:41:20

so

1:41:20

that is

1:41:21

why it is

1:41:21

patching

1:41:22

actually

1:41:22

one or two

1:41:23

chunks

1:41:23

only

1:41:23

that is

1:41:24

that

1:41:24

really

1:41:26

if it's

1:41:26

but really

1:41:28

if you are

1:41:28

10.

1:41:29

so

1:41:29

then I'm

1:41:31

if I if I

1:41:31

if I're one or two

1:41:31

to

1:41:32

for making

1:41:33

that cosine similarity

1:41:34

very straight

1:41:35

okay

1:41:35

and

1:41:35

will

1:41:36

and I'll

1:41:36

let's

1:41:37

I'm

1:41:38

I want

1:41:39

I think I

1:41:40

want to

1:41:40

I think I

1:41:42

need a

1:41:42

and I'm

1:41:42

grounded

1:41:42

and then

1:41:43

then the final

1:41:44

version

1:41:45

will

1:41:45

I'm

1:41:46

there

1:41:47

on that's

1:41:48

that's why I

1:41:49

was asking

1:41:50

the question

1:41:50

that's what I

1:41:51

think you

1:41:51

showed right now

1:41:52

right now.

1:41:54

Right,

1:41:54

so right

1:41:54

so we're

1:41:55

I think

1:41:56

we're saying

1:41:56

I think

1:41:58

if we're

1:41:58

we're

1:41:58

in two point

1:41:59

between

1:41:59

distance

1:41:59

we're I think

1:42:00

we're I think

1:42:00

exactly

1:42:01

discussed

1:42:02

exactly discussed

1:42:02

and if

1:42:03

if we

1:42:04

if we

1:42:04

know

1:42:04

that

1:42:05

any two

1:42:05

things

1:42:05

are in

1:42:06

or we're

1:42:07

we're

1:42:07

we're

1:42:07

we're going to

1:42:08

use

1:42:09

in order to

1:42:09

calculate that

1:42:10

and that.

1:42:10

and that

1:42:11

and that

1:42:12

and

1:42:12

they're

1:42:13

in

1:42:13

there's

1:42:14

not

1:42:14

there's

1:42:15

so I think

1:42:16

that's

1:42:16

that's

1:42:16

it's

1:42:17

yeah.

1:42:17

Yeah,

1:42:17

that's

1:42:18

that's

1:42:18

internally

1:42:19

decided

1:42:19

or where

1:42:20

where

1:42:20

what kind of

1:42:21

that is

1:42:23

happening

1:42:23

all internally

1:42:24

yes.

1:42:25

Uh,

1:42:25

yeah,

1:42:25

yeah,

1:42:26

correct,

1:42:27

and

1:42:28

and this

1:42:28

agentic case

1:42:29

in,

1:42:29

you're

1:42:30

in the

1:42:30

land

1:42:30

chain

1:42:30

that were

1:42:31

I was just

1:42:33

just a thing

1:42:33

was I was just a

1:42:34

I'm

1:42:34

trying

1:42:35

that

1:42:35

I'm,

1:42:35

I'll,

1:42:36

I'll,

1:42:36

I'll ask

1:42:37

I'll

1:42:38

then I'll

1:42:38

will,

1:42:38

when I'll

1:42:39

that you'll

1:42:40

you'll

1:42:40

you're

1:42:41

correct,

1:42:41

so we're

1:42:42

we're

1:42:42

we're

1:42:43

using,

1:42:43

we're

1:42:44

we're using

1:42:44

how we're

1:42:45

yeah,

1:42:45

how

1:42:46

how we're

1:42:46

and we

1:42:47

can't

1:42:47

how we

1:42:48

we're

1:42:49

we're not,

1:42:49

we

1:42:50

we've

1:42:50

we've

1:42:50

made,

1:42:50

and we

1:42:51

we're back, and we

1:42:51

we're

1:42:51

we're

1:42:52

we're making and we

1:42:55

and we're

1:42:55

yeah,

1:42:55

yeah,

1:42:56

yeah,

1:42:56

so there I'll

1:42:57

I'll ask

1:42:58

my next question

1:42:59

actually,

1:42:59

okay,

1:43:00

thank you.

1:43:01

Yeah,

1:43:04

Yeah.

1:43:06

Yeah, go on,

1:43:07

Pankaj.

1:43:10

I think your program is working, right?

1:43:18

Hello.

1:43:21

Yeah, your voice is not clear.

1:43:23

I'm not able to hear you.

1:43:24

I think other people are not able to hear you.

1:43:27

Okay.

1:43:29

My

1:43:29

Project code is working.

1:43:34

Go on, go on.

1:43:36

You,

1:43:37

uh, you, you know,

1:43:37

the

1:43:38

Lanking tools

1:43:39

I've seen,

1:43:39

that's the basic concept

1:43:40

that

1:43:40

I'm

1:43:41

maybe a little

1:43:43

briefed

1:43:43

that we're

1:43:44

that we're

1:43:45

we're doing

1:43:45

uh,

1:43:46

we're doing,

1:43:47

agent,

1:43:48

uh,

1:43:49

automatically, but

1:43:50

we have a

1:43:51

query has my,

1:43:52

that we're doing it,

1:43:52

we're doing it,

1:43:54

this is,

1:43:54

this is the code

1:43:54

which is by default

1:43:55

create

1:43:56

over?

1:43:56

No,

1:43:57

no, we're

1:43:57

we define

1:43:58

we're doing,

1:43:58

we're doing,

1:44:00

so,

1:44:00

if you're doing, so,

1:44:00

if you're,

1:44:01

if you're,

1:44:01

if you're,

1:44:01

if you're,

1:44:02

we're doing,

1:44:03

we're doing,

1:44:04

so even

1:44:05

if we've

1:44:05

we've got this

1:44:06

the program

1:44:06

here we've

1:44:07

we've written

1:44:08

we're in

1:44:09

this in this

1:44:09

we're going to

1:44:10

we're

1:44:11

that we're

1:44:12

that we're

1:44:13

like,

1:44:14

we're like,

1:44:14

we're

1:44:14

this tool,

1:44:15

you know,

1:44:16

this tool defined

1:44:17

and they're

1:44:18

and they're

1:44:18

and they're

1:44:20

a array or list

1:44:20

and we're

1:44:21

we've passed

1:44:23

here.

1:44:25

So,

1:44:25

so we've

1:44:25

we've passed

1:44:26

so we're

1:44:27

these

1:44:27

all these details

1:44:27

here are here

1:44:28

here are here.

1:44:28

So agent

1:44:29

executor in and

1:44:29

and tool calling agent

1:44:31

in there we've made a correct

1:44:32

correct.

1:44:33

Correct.

1:44:34

Okay, so one thing,

1:44:35

uh,

1:44:36

this, uh,

1:44:36

yeah,

1:44:36

uh,

1:44:37

we're the

1:44:38

agent,

1:44:38

uh,

1:44:39

the tools are

1:44:40

,

1:44:40

they're

1:44:40

right,

1:44:41

secondly,

1:44:42

uh,

1:44:43

the query,

1:44:44

uh,

1:44:45

last,

1:44:45

I mean,

1:44:45

three,

1:44:46

four sessions

1:44:47

pre,

1:44:47

uh,

1:44:48

created,

1:44:48

that we,

1:44:49

we're,

1:44:50

we're coding,

1:44:50

we're,

1:44:51

we're coding,

1:44:52

we're done by the

1:44:53

uh,

1:44:54

uh,

1:44:54

element.

1:44:55

Correct, right,

1:44:55

correctly,

1:44:56

right,

1:44:56

currently,

1:44:56

right,

1:44:57

so,

1:44:57

so I,

1:44:58

, I,

1:44:58

the way way,

1:44:59

that we're,

1:45:00

,

1:45:00

they say,

1:45:00

one,

1:45:00

one,

1:45:00

one,

1:45:01

one,

1:45:01

video,

1:45:02

that pipe coding

1:45:03

in that type coding,

1:45:03

I,

1:45:03

I,

1:45:04

let's say,

1:45:05

let's say,

1:45:06

if I'm

1:45:06

let's say,

1:45:06

if I'm

1:45:07

let's say,

1:45:07

if I'm

1:45:08

,

1:45:09

if I'm

1:45:10

if I'm

1:45:10

this code,

1:45:10

so I'm

1:45:11

how I'm

1:45:11

,

1:45:12

we're going to

1:45:13

, we're

1:45:14

we're doing,

1:45:15

and we're

1:45:15

doing, but

1:45:17

when we

1:45:17

have a

1:45:18

project, like

1:45:19

a project,

1:45:19

even I think I

1:45:20

think I,

1:45:21

that I think,

1:45:22

I've

1:45:23

, I think,

1:45:24

I'll upload, I

1:45:25

upload and I'll

1:45:25

do you, so you

1:45:26

see, you're

1:45:27

, you're not

1:45:29

writing code, I am

1:45:30

just setting up the

1:45:31

context properly, and now the new thing has come in market, which is called us loop engineering, where you

1:45:37

will be writing some loops that are there, that we have

1:45:39

AI

1:45:40

everything so that it's writing

1:45:44

everything, we are not even writing prompts and everything.

1:45:47

So even that part I'll make a video and I'll share you on YouTube, so that video you guys can

1:45:53

watch.

1:45:54

Once I make it, I'll tell you that part.

1:45:56

Also, I think I'm not able to pick up your phone.

1:45:58

Why? Because I have like on Saturday, Sunday,

1:46:01

also I'm having three, four classes and I need to record multiple videos for everything.

1:46:06

So yesterday also I was not having time.

1:46:08

I was not even having time for eating food.

1:46:11

So currently it's going like that.

1:46:13

But probably in this week,

1:46:14

once whenever I have time, I'll give you a call back.

1:46:17

I've saved your number already.

1:46:19

So I'll give you a call back once I'm free this week.

1:46:22

Currently till Thursday, I need to record like after this class also, I need to record two, three

1:46:26

videos.

1:46:26

Then again, I have to do multiple other things.

1:46:29

Every morning I have to go to office.

1:46:30

once I come from office, I need to take some or other class.

1:46:34

So that is why I don't get, like, I don't have any time in my life these days.

1:46:39

So that is why I'm not able to pick your call.

1:46:41

But once I'm free, probably on this Friday, I think I might be free.

1:46:45

Or this Saturday, I have no class, luckily.

1:46:48

So probably this Saturday or Friday, I'll give you a call.

1:46:52

Definitely, not an issue.

1:46:53

Yeah, that thing we can do.

1:46:55

Yeah.

1:46:56

Okay, then I think we have discussed almost every part that is there.

1:47:00

Just try to.

1:47:00

watch this recording. And today I'll for sure try that I upload more videos.

1:47:05

Probably in night, I will be uploading a new project today. So that video you can check out

1:47:11

like on YouTube only. I'll share you on Thursday's class, but neither it will playlist

1:47:16

in the playlist may I'll add. And yeah, apart from that same video will be uploaded on Masai

1:47:21

Live also. You can watch it there also. I think tomorrow's a free cohort start

1:47:25

where they will be publishing my videos. So you can check that out. Okay then.

1:47:30

Yeah, go on.

1:47:33

My, uh, Masai Live is actually, uh, asking for subscription.

1:47:37

Uh, I'm YouTube at all right.

1:47:40

All right. Thank you.

1:47:42

No, you don't have a pain anything. Yeah.

1:47:43

Most probably if you see, I think, uh, I'm not sure which one they have done.

1:47:51

Yeah, I think this is, is it paid?

1:47:56

I think it's a chah. It's get only one you can watch another.

1:48:00

are paid. But I'll do that, I'll do that and I'll share you the link directly. So you can watch it.

1:48:06

Yeah.

1:48:10

Yeah, definitely Dereja, I'll share. I think two videos are there currently, which I've shared. One is this link.

1:48:16

I'll properly create a playlist today and I share those videos. Yeah.

1:48:22

So, Ajie, you will have to install that particular, uh, this thing, right?

1:48:27

Lankhin classing agent.

1:48:28

You have to install it.

1:48:29

So that particular part you have to install otherwise it will not work right.

1:48:35

So do that particular thing, install, pip install, that command run that is written in the program,

1:48:41

which is pip install Langchain agent, LangChain agent, once you do that particular part, it will come up.

1:48:52

Yeah, that particular thing you can do. I'm sharing this probably in this only I'll share the update the videos or

1:48:59

probably I'll create a new playlist that is there. And then I'll upload.

1:49:02

Claude videos, I think three videos are there. Those you can watch. I have shared the link in the chat as well.

1:49:08

Okay, then I think we are almost done. Koppel, if you want to give a break,

1:49:12

then probably you can give a 10 minutes break or you can directly start the quiz. In last session,

1:49:16

also we directly started the quiz. But if you want, you can give a 10 minutes break and then have a

1:49:20

quiz, even that works.

1:49:23

I can also start a break like timer for 10 minutes and then we can have a quiz, like whatever.

1:49:29

you say. I think we can wrap up this session because we have already taken too much of query

1:49:37

and probably I'll go with feedback poll and followed by the quiz.

1:49:45

Done, that works works. I've shared the GitHub link in the chart.

1:49:51

Guys, I'm just releasing the feedback poll and stay back for a short quiz. And then,

1:49:59

finally we'll wrap up the session today.

1:50:07

Saksham, can you make me host?

1:50:13

Oh, sorry, sorry, I'll make you the host.

1:50:25

Yeah, I've made you the host.

1:50:29

as well. Thanks. Yeah.

1:50:59

Thank you.

1:51:29

Thank you.

1:51:59

Thank you.

1:52:29

All right.

1:52:33

So let's get started with a short with a short quiz on

1:52:49

on Mintimeter, I'm sharing.

1:52:59

So you guys can either scan this QA code given here or just

1:53:14

you guys can either scan this QA code given here or just go to www.mns.m.com and enter this code given here.

1:53:25

I'm pasting this code given here.

1:53:29

Thank you.

1:53:59

Thank you.

1:54:29

All right. So let's get started with the very first question.

1:54:41

So here is your first question.

1:54:43

What is the main purpose of create tool calling agent function?

1:54:48

And the options are to decide when and which tool to use, create a database to store

1:54:54

history or to display graphs.

1:54:59

The correct option is to decide when and which tool to leave.

1:55:11

Let's have a quick look on the leaderbone.

1:55:28

Moving on the second question.

1:55:29

Which component runs the agent loop safely and the options are chat prompt template, agent executor,

1:55:43

messages placeholder or add tool.

1:55:59

The correct option is agent executor that runs the agent loop safely.

1:56:13

Let's have a quick look on the leaderboard now.

1:56:25

Moving on to the third question.

1:56:28

What does max iterations control?

1:56:39

And the options are number of tools created, number of users, maximum number of agent action loops or the number of prompts.

1:56:58

The correct option is max iterations controls maximum number of agent action.

1:57:10

So this is how the leaderboard looks now.

1:57:15

Let's move on to the next question.

1:57:27

Which parameter helps recover from output parsing errors and the options are verbose, return intermediate steps, max iterations or handle parsing errors.

1:57:57

Handling errors.

1:58:15

Let's move on to the fifth question.

1:58:27

and the options are intermediate reasoning and tool traces, final answers only, or database records or user passwords.

1:58:57

And the correct option is intermediate reasoning and tool traces.

1:59:04

Let's have a quick look on the scoreboard now.

1:59:09

Moving on to the sixth question.

1:59:22

Which placeholder is used to include the user's query in the prompt and the options are agent scratch pad, input, intermediate steps or tool calls.

1:59:39

The correct option is input.

2:0:09

have a look on the leaderboard.

2:0:11

Moving on to the seventh question.

2:0:17

What is the role of the add the rule tool decorator?

2:0:27

It options are converts a Python function into a Langchian tool to

2:0:33

Starts the agent, stops execution, or creates prompt.

2:0:37

And the correct option is it converts a Python function into a Lantern.

2:0:48

Let's have a look on the pre-final scores.

2:0:54

Moving on to the last question for the day.

2:1:06

for the day.

2:1:07

If no suitable tool exists for a user query, the agent should and the options are, invent a new tool,

2:1:19

re-try forever, crash with an error, or give a direct fallback response.

2:1:36

The correct option is, if no suitable tool exists, then it should give a direct fallback response.

2:2:01

Let's have a final leader one.

2:2:06

Congratulations, Mayles.

2:2:18

With that, we have come to and into our session.

2:2:22

See you on Thursday.

2:2:26

Till then, bye-bye.

2:2:27

Good night.