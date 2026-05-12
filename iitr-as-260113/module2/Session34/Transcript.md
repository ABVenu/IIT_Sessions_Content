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

Hi, everyone, very good evening, folks, am I audible to all of you?

8:30

Hi, folks, am I audible?

8:36

Okay, great, good evening everyone and a very, very warm welcome to all of you in the new class and the new topic.

8:48

And I think these are the two last classes of this second module, right?

8:54

This is the last second class of this last second module.

8:57

And then I think after that you will have the evaluation, correct?

9:02

Folks, yes, no.

9:09

Yes, this Sunday you have the evaluation.

9:10

Again, the rule remains same.

9:13

Please make sure that all of you attempt the exam.

9:15

We have studied a lot more.

9:18

then what you need to clear the exam, right? So please, please do make sure that all of you are

9:23

attempting the exam. Okay. I'm not sure about it, Vishwanath, about the revision classes or

9:30

the revision week. I think the Maasai team will be able to communicate, will be communicating

9:35

that particular thing to all of you. Okay? And whatever dates you have been communicated, so your

9:40

schedule will be as per those dates, okay? I also get the schedule from the team, okay?

9:48

Just like you get, I also get the schedule from the team. Okay, no worries. So let's get started. Is my screen visible to all of you?

9:57

Did I miss something important? No, no, no, sir. We have not started as of now. We are just getting started.

10:02

Okay? Okay. So folks, today we will be talking about some software engineering fundamental concepts like APIs and JSONs. Okay? So today, today we will be talking about mainly two things. Okay. One is APIs.

10:18

Okay. Different terms and terminologies related to APIs. For example, HTTP methods, you have get, put, post, patch, put, these kind of methods. When do we use these methods? What are the use cases of these methods? We will talk about that. And other fundamental concepts like HTTP status code. So whenever you make an API request, you get some status, along with the response, you get some status code, right? Whether the request was successful, whether the request was not successful, et cetera, right? And we will also be talking about. And we will also be talking about. And we will also be talking about.

10:48

about something called as JSON.

10:50

Okay. Now tell me everyone, in the previous module, when we were talking about fast APIs, right?

10:56

Do you remember we had a couple of classes on Fast API?

10:59

Remember that? We had few classes on Fast API, Pyrentic, etc.

11:05

Do you remember we talked about these things? Did we talk about these things?

11:09

Maybe did we just use the name of these these things, APIs, JSON, objects, etc.?

11:17

Okay? So today we've talked about these things.

11:18

We will be talking about these things in detail, and we will be also talking about that why these things are very important, right? From the point of view of AI app development, right? Generally, we see that terms like APIs, rest APIs, HTTP protocols, your HTTP methods, HTTP status code, etc.

11:40

Generally, we see that these things are required for a software engineer, right? So for long, long time in the tech world, we need these

11:48

things to implement APIs, implement web APIs, implement applications, implement websites.

11:54

But now, if you are implementing an AI application also, still you need to have a very strong understanding of,

12:01

still you need to have a very strong, you can say that in-depth understanding of APIs, HTTP methods,

12:08

request bodies, HTTP status code, JSON, JSON structure, JSON parsing, JSON dumping, etc, etc. So even if you're working

12:18

as an AI app engineer, AI app developer, right? Or agentic AI expert, still you

12:24

need to understand these things in very much of detail. For example, let me give you a very, very

12:29

simple example, simple idea, right? That how app development, how AI app development also

12:36

needs the term also needs the understanding of APIs. For example, everyone, let's see if you're building

12:43

a travel, travel,

12:48

Let's say if you're building a AI travel agent.

12:59

Okay, so if you're building an AI travel agent, now let's say everyone, if this agent is supposed

13:06

to tell you the website, what do you say, the flight prices, it can book the flight tickets for you,

13:12

it can book the hotels for you, it can book Airbnb for you. For example, if this is

13:18

is your travel agent, right? If this is your travel agent, this is your application,

13:23

now this application, even, user is interacting with this application. Now, if let's say

13:27

you are giving, let's say this application has some LLM, okay, assume that this application has some

13:33

LLM. Now, if you're giving some prompt to this LLM to generate an itnery, so it will generate

13:39

an itinary, after the itinary gets generated, then you give a prompt to this application, to this AI agent

13:45

to book the cheapest flight first.

13:48

you. Now tell me everyone, to book a flight, first of all, even before booking the flight,

13:52

to check the prices of the ticket, to check the prices of the flight. Once your agent will be

13:57

able to check the prices, then only it will be able to decide, right, that this is the cheapest flight.

14:02

Can I say that it will have to make a call, it will have to call some travel agency like Make My Trip,

14:09

some third-party travel aggregator like Make My Trip, Go-I-Bebo, Expedia, etc. For hotel booking,

14:16

it might have to call, let's say, make my trip, booking.com, Airbnb, etc.

14:20

Right? So your application needs to make a call to, needs to make a call to, let's say, make my trip.

14:27

Now, if at a time, can you, so, first of all, first of all, before I go into the depth of this call,

14:32

can I say that for our application, this make my trip, is acting like a,

14:38

this make my trip is acting like a third-party agent, right?

14:43

Third-party tool, can we say that?

14:46

Folks, yes or no?

14:55

Similarly, everyone, at a time, can you integrate more than one third-party tool?

15:00

Make My Trip, Expedia, Go-I-V-Bee-Go, because you might have to compare the prices, right?

15:06

Also, at a time, everyone, you might have to check the prices from direct airlines also.

15:11

Because everyone, a lot of times you will realize that, if, let's say, there is some flight ticket on Make My Trip, which is, let's say,

15:16

$500, right? The same ticket might be slightly cheaper on directly on Air India.

15:22

Because, like, there will be some commission of Make My Trip,

15:25

Make My Trip will be giving you some offers, right, etc, etc.

15:27

So, you might have to check with Air India also, right?

15:31

You might have to check with Indigo also, right?

15:34

So there might be multiple third-party calls that you might have to make.

15:39

Is that point clear to all of you?

15:41

Now tell me everyone how your AI application, how your travel agent is communicating,

15:46

with Make My Trip. How your travel agent is communicating with Air India? How your travel

15:51

agent is communicating with, let's say, maybe Indigo. Can you tell me? How this communication

16:00

is happening? So, can I say that in this communication, application is making a request, right? So

16:07

your travel agent, your AI application is making a request. Definitely around in request,

16:13

can I say that you'll have to pass some input parameters? For example, let's say you know,

16:16

need the flight details from Delhi to Bangalore, right, for this date, this time, etc, etc,

16:22

for two people, for four people, etc. You pass all of these parameters in the request,

16:28

right, in the request input, then your Make My Trip will give you the response back. Is that idea

16:33

to all of you? So this is a complete request response cycle. So this is a request response cycle.

16:41

Now, how this communication is happening? Now, tell me one, can I see that this is that this

16:46

make my trip application must provide you some functionality that you can make a call to and

16:52

you can expect the response back in a particular manner. Yes or no. So if Make My Trip is not

16:58

exposing any functionality, will you be able to make a call? Can you directly make a call to let's say

17:03

maybe J.B. Morgan? So J.P. Morgan is a very big investment banking, like throughout the world.

17:10

If you want to use their functionalities, you'll have to pay hefty money to that, to that company, right?

17:15

You cannot directly make a money, you cannot directly make a call to their functionalities

17:20

just like that. So it means that everyone there will be some contract. So if your travel agent is

17:25

making a call to make my trip, it means that there must be some contract between application and

17:31

make my trip. If you see everyone, in the previous few classes, we have talked about, like we have

17:35

executed open AI APIs. Remember that? That from our Python application, we make a call to

17:41

open AI. Now tell me everyone, can us that for that API call to be seen?

17:45

successful, open AI must be providing that functionality publicly that you can make a call to.

17:51

Obviously, for that you need authentication. You need to create an account on open AI. You need to

17:55

put some balance, right? You need to have some money in that account, right? Definitely. And then you

17:59

need to give the API key. Using that API key only, you will be able to make a call. Correct or not?

18:07

Correct? Similarly, everyone, that your application can make a call to make my trip. And then

18:11

Make My Trip will give you some kind of response. Similarly, this application

18:15

can make a call to Air India. This application can make a call to Indigo and so on. And you

18:21

will expect a response back. This call is called as an API call, right? This call can be treated

18:28

as an API call. Are you guys getting this point? So whenever two parties have some kind of contract,

18:33

right? Now tell me everyone, if our travel agent and make my trip, if they do not have a contract

18:39

between them, now what do we mean by contract? Contract means that they have some signed agreement.

18:44

that Make My Trip will say that, like that will have some kind of terms and conditions.

18:50

So Make My Trip will say that, okay, if you want to use my functionality, you will have to pass me

18:56

parameters in a particular manner, in a particular way. And then I will give you the response

19:01

back in a particular way. It means that if you don't follow that contract, right? If you don't

19:06

pass the details that Make My Trip is expecting you to pass, don't you think that Make My Trip is expecting

19:09

you to pass, don't you think then Make My Trip will, might fail the API call, might not give you

19:14

the proper response, it might fail, correct or not? For example, let's say if Make My Trip

19:19

expects the source and destination and the date, minimum three parameters. If you don't provide

19:24

the source, will you get the expected response from the API from Make My Trip? Will you get the

19:29

expected response from Make My Trip? Obviously not, because you are not providing the proper input

19:34

parameters. So API is nothing but everyone, a functionality which is exposed by some entity

19:41

that other entities can use. Also, API is nothing.

19:44

can be treated as some kind of contract between two parties that if you want to use my functionality,

19:50

give me these parameters, I will take your request, I will process your request, and I will give you

19:55

the response back, that you can use. Makes sense to all of you? Makes sense to all of you?

20:02

So can we say that everyone? If I write this simple definition, please let me know if this makes

20:06

sense to all of you. That APIs. First of all, everyone, what is the full form of word API?

20:12

What is a full form of word API?

20:14

Otherwise, API stands for application.

20:33

Application programming interface.

20:35

So this is the full form of word API.

20:39

Although like this, you can say that the definition, the full form, the full form,

20:44

form might not be making a lot of sense if you're learning this for the very first

20:47

time, but if you understand the concept of interfaces, right? So a lot of object-oriented programming

20:52

like programming languages like Java, etc., they have the concept of interfaces. Now, interface

20:58

is nothing but kind of a contract, right, when you sign a contract. Now, when you sign a contract

21:03

with some company, you will have to adhere to that contract, right? You will have to adhere to that contract.

21:08

You'll have to follow the guidelines of that contract. Similarly, everyone, API act like

21:14

an interface between two parties, right? So for example, let's say, this is party, this is,

21:19

this is let's say, some client, right? And let's say everyone, the server could be as simple as,

21:26

let's say, Open AI. Right? So guys, what Open AI does is, now if you want to make a call to Open

21:32

AI, right, so Open AI has exposed an API, right? So first of all, in your client, let's say, for example,

21:39

if you're using a Python client, it means that your client is implemented in Python. You can implement

21:44

in any language. It can be, for example, let's say, when you use chat gptt.com, when you use

21:49

the chat gpt website, your browser is the client, right? So now, in that case, everyone, you

21:53

don't have to call an API request manually. Because what happens is when you just write the prompt,

22:00

right, your browser or your chat gpt website automatically makes an API call from front end to

22:05

backend, right? But when your client is actually a backend application, for example, Python or Java,

22:11

etc. What you do is everyone, you create a client object. Remember that?

22:16

First of all, you'll have to install open AI software, Open AI library, PIP3 install OpenAI,

22:23

then you import Open AI from Open AI import open AI. Then you create a client object. Client is equal to

22:29

open AI. And then what you do? Client. Dot responses.orgate. Remember that?

22:35

Client.dot responses. Create. Now, when you make a call like this, first what you do?

22:41

First, you create an open AI client object.

22:48

First, you create a client object. And then what do you do?

22:56

Right? Then everyone, you pass some parameters here. For example, let's see you pass. You pass, first of all, you need to pass some model. That which model you are trying to use here.

23:11

Let's say GPD 5.2. Then everyone, you can pass some instructions.

23:18

Right? Then everyone, you pass some input that is prompt.

23:26

Folks, do you remember this or not? Do you remember this or not? That yes, we have made this call, I think, multiple times in the exact same way.

23:35

Right? So first you create a client object, then you do client. Responses. Create. Now everyone, you can say that.

23:41

this is a contract between you as a client and Open AI as an application or as a server.

23:48

Now everyone, if you try to change this, let's say instead of create, if you want to use some other method,

23:53

let's say maybe some XYZ method, or instead of create, let's say you have insert method.

23:58

Is it necessary that open AI must be providing that method?

24:03

Not really, right? If you want to use the open AI functionality, you will have to follow a particular contract.

24:09

Now instead of create, let's say, I say that okay, instead of create,

24:11

I will make a insert call. Do you think that insert method will be supported by the open AI

24:16

application server? Maybe not. It will not support it because there is no, that method is not part of

24:23

the contract. So everyone, when you are, like when you are using the open AI application, when you

24:30

are creating a client, you are indirectly, directly, what you are doing is you are signing

24:36

a contract. It means that you can only use the functionalities within the defined contract.

24:41

Now, how will you check the contract details?

24:43

Because manually, we did not, physically, we did not sign any contract, right?

24:47

But for that contract everyone, for that API contract details, you'll have to go to the documentations.

24:53

Every company will have some documentation.

24:56

For example, let me show you the documentation details of Open AI.

25:01

Let me log in, I think I got logged out.

25:11

If I go to my documentation, if I go to this API docs, if you see everyone, this is the documentation, right? And for every kind of API request, there are different models. There are different sections. How will you use it? Right? So this is how you use the application. So everyone now, if you see, this is a contract that you need to follow. Now, apart from that, if you try to make a call to other functionality, which is not defined in the contract, that functionality might not.

25:41

not work, may not work. Is that point clear to all of you? Absolutely. Different applications will have different

25:46

formats, right? For example, if you use Open AI, Open AI from Star Redis versus if you use Gemini, if you use Clod,

25:54

definitely these are different companies built at different times, built at, built by different people, right? So definitely

26:01

they will have different contracts, right? So how you use Open AI, can I say that how your application is

26:07

talking to Open AI, Open AI, versus how your application is being.

26:11

being used is using Gemini, how your application uses Claude, that will be different.

26:18

Correct or not? So this will be different or not?

26:22

Obviously, different companies, different way of making a call, different functionalities, different

26:26

function names, different input parameters, different return types, and whatnot. So it will be

26:31

very difficult, correct everyone? That, for example, now everyone, can I say that this is a very,

26:36

very general use case. Let's say today you are using Open AI. I will give you a very good

26:41

analogy for this. Today you are using Open AI and let's say your application is running for

26:46

one month, two months, six months. After that, after six months, you realize that, let's say

26:50

the bill of Open AI is very big. You will have to pay, like Open AI is becoming very expensive

26:55

for you. They are charging a lot. Now you research about it and you search that and you come across a

27:02

conclusion that, okay, Gemini is better than Open AI for your particular use case, a particular model

27:07

of Gemini and for example, let's say it is 10 times cheaper. For example,

27:11

let's say if you are paying $100 to Open AI, let's say you will have to just pay

27:16

$10 to $15 to Gemini per month. Will you definitely, would you definitely want to migrate from

27:22

Open AI to Gemini? Tell me, Hesano. I'm not writing anything. I was just scribbling. Would you

27:29

want to migrate from Open AI to Gemini to tell me everyone? If let's say it is giving you 10x better

27:35

cost efficiency. Let's see if your bill is, let's say maybe one lack dollar, $100,000.

27:41

And now from Gemini, you just have to pay $10,000.

27:47

It is a big saving, right? Absolutely is.

27:51

Every company would do that.

27:52

But now tell me everyone, if you are using Open AI today and your application is assume that

27:57

your application is pretty big.

27:59

And tomorrow you want to migrate from Open AI to Gemini.

28:01

So Gemini will have their own contract, own APIs, own functionalities, etc.

28:06

Don't you think you will have to make a lot of changes in your application to move from

28:11

from Open AI to Gemini, you'll have to change this, you'll have to change this,

28:15

you'll have to change this, different input parameters. So a lot of changes you'll have to do.

28:19

Correct? The way you are getting an output from Open AI is going to be different than the

28:25

way Gemini will give you the output. So definitely you'll have to make a lot of changes.

28:30

The only thing everyone, if you have to make a lot of changes in your application, it will take

28:34

few days of time. You will have to deploy people for that. Let's say you are paying huge salaries

28:40

to your AI developers.

28:41

and those people are actually going to work on that part.

28:44

So you'll have to decide that also.

28:46

So whenever you're migrating from one application to another application or one API contract

28:50

to another API contract, sometimes it is very, very difficult.

28:53

That's why everyone, there is a concept of MCP.

28:56

I think you must have heard about the concept of MCP in AI applications.

29:00

That's why generally we don't talk to these applications directly.

29:03

We talk to these applications via, you can say that, via a third-party tool, which is MCP.

29:08

So MCP gives you an easier way.

29:12

MCP is not part of today's class. I just gave you the idea.

29:15

We will discuss that separately.

29:16

MCP is a very big topic.

29:18

We will see that separately.

29:19

But is the idea clear to all of you?

29:22

You can say that MCP acts like your relationship manager.

29:26

All of us, multiple people have relationship managers with their bank, with their bank, right?

29:31

So whenever you have to discuss, whenever you have any query about credit card, about other things, right?

29:37

You just discuss.

29:38

you just give the query to relationship manager.

29:40

This is how MCP also works.

29:43

That you give the query to MCP.

29:45

MCP will talk to OpenAI or Gemini or whatever, right?

29:47

You don't have to deal the complexity.

29:49

You don't have to worry about the complexity part.

29:51

But I hope the idea of API is making sense to all of you, right?

29:55

APIs are nothing but the contract between two parties that you make a call, get the response.

30:01

Make a call, get the response.

30:02

Does it make sense to all of you?

30:05

Right?

30:06

So let me write a very simple definition of API.

30:08

everyone that what are APIs everyone?

30:10

APIs are nothing but.

30:11

APIs are the bridges are the bridge are the bridge between the agent's brain.

30:38

and real world software, software applications.

30:53

For example, everyone, like what is the definition of this, right?

30:58

Now everyone, in this, I have taken a very simple example that when LLM is part of your AI application.

31:03

But everyone now tell me, how many companies do we have in the world who have their own LLMs?

31:08

Does every company build their own LLM?

31:12

No, right?

31:13

Building an LLM is a multi-million dollar thing.

31:16

And it takes years and years to do that.

31:18

So it is not a very simple thing.

31:20

So even every application does what?

31:22

They have a contract with some third party LLM generally, right?

31:25

Most of the time.

31:26

So for example, Open AI, right?

31:28

This might be Open AI, that is GPD or Gemini, etc.

31:33

So guys, don't you think when your application,

31:36

when your A.A.A.A.A. application makes a call to LL.

31:38

LLM makes a request to LLM, then you get the response back.

31:46

So don't you think this is also an API call?

31:49

This is also an API call.

31:51

So that's why I did not take this initially.

31:54

Now you will understand that yes, 100%.

31:57

This is also an API call.

31:59

When you want the LLM to generate the itinary,

32:02

you are a travel agent, you are building an application for travel agent support system

32:07

using AI.

32:08

So your application takes the input parameter from the user.

32:12

You creates a well-designed, well-written system prompt.

32:16

Then that well-written system prompt you give to the LLM via API, gets the response back,

32:21

then you give the response back to the user.

32:24

This is the definition of API.

32:25

Let me write one more definition of API, everyone.

32:28

I wrote it at one place, just a second.

32:37

Yeah.

32:38

So an API is a contract.

32:50

An API is a contract between two software components,

33:07

that defines what request can be sent, what request will be sent, what request will be sent and what response will be received?

33:37

I think let me close this. It is a bit difficult to have this on the top. Okay, now I think

33:43

it should be visible, right? So I'm just, I have just written this definition even. Sorry for that.

33:46

And ATI is a contract between two software component that defines the contract defines that

33:51

what request will be sent. How will you make a request and what response will be received?

34:07

What response will be received? Is the definition second, is this definition

34:13

also making sense to all of you? Have a look at it and tell me if this definition is also clear.

34:22

Everyone clear? Right? Let me write a smaller and the most easiest definition to one design.

34:29

An API is a structured way.

34:36

Okay? I think it is a structured way.

34:37

yellow color is visible, right? This pen color is visible. API is a structured way. Structured way.

35:07

Is that point clear to all of you? So are these three lines clear to all of you?

35:12

Are these three lines clear to all of you?

35:16

Okay. Now let's talk about everyone, let's how the modern day applications are structured.

35:25

Whether you talk about a simple application, a simple website, a mobile application, Android,

35:30

iOS, or an AI application, whatever, any software application, right? How any software, any software,

35:36

software application is structured. How any modern? So, guys, what are the different components of any, any, any software application? Can you tell me?

36:06

What are the different components of any software application?

36:09

What are the major components do you see?

36:12

Yes, front end, backend, and database, right? So can I say?

36:33

say that everyone? Typically, what happens?

36:36

So there is a user.

36:37

User is, anyways, we have the user.

36:41

So generally there are three main components of the application.

36:45

We have the front end of the application.

36:53

We have the front end of any application.

36:55

We have the backend of the application.

36:59

And we have the database.

37:05

Correct.

37:06

Now everyone, front end can be what?

37:10

What? Can you give me some examples of frontend?

37:13

Can you give me some examples of frontend?

37:17

Can you give me some examples of frontend?

37:19

Is website a front end?

37:23

Is website a front end?

37:26

Yes.

37:27

Is mobile application a front end?

37:29

Swigi application, Zomato application, Uber application.

37:35

application, they are also frontend, right?

37:38

So, and everyone now, let's say other ways of frontend could be like a client, I would say, can

37:45

us say that like your Alexa or your watch, right?

37:49

Is that also a frontend?

37:51

Frontend is the way for the user to access your application, as simple as that.

37:57

However, the user is accessing your application that is called as front end.

38:02

It can be your website, it can be your iOS application, it can be Android application, it can be Android

38:05

It can be a watch application. It can be Alexa. It can be via voice. It can be via audio or whatever. Make sense, everyone.

38:15

And then everyone, there comes the concept of backend, right? Now, what happens everyone? Let's say you go to Amazon website.

38:21

Okay? Let's say you go to Amazon.com.

38:35

You go to Amazon.In. Now everyone, on Amazon.In, you search something. You search for,

38:46

let's say, iPhone, and then you press enter. You search for iPhone and then you press enter.

38:52

Now everyone, you get a lot of results, right? You get a lot of results. Now, tell me, the results that

38:58

you're getting, do you think that that data, like you get a lot of results, right? Maybe let's say

39:03

20, 30 products you get in the result.

39:05

Whatever data you are getting in the response after you search for any term, was that

39:11

data present in your laptop or present in your mobile phone? Was that data already present in your

39:17

system? Answer is no. That data was not present in your system. So now where that data is coming

39:24

from? Initially that data was not present in your system. So where that data is coming from?

39:35

an API call. Does it make sense to all of you? Folks, yes or no? At least people

39:42

can respond. Yes, no. Maybe if you feel that, okay, you have to type yes multiple times,

39:49

no multiple times, even if you say YN, you can save your time. Okay? YN also works. It means that

39:56

you are getting that response back via API call. So what happens everyone? Whenever you perform

40:00

any operation, whenever you do any activity on any website, on any website, on the

40:05

on mobile application, when you click something, when you click a button, when you touch

40:09

on particular thing, what happens everyone? An API call gets triggered. So in the back end

40:14

everyone, like in the front end code, every action is being noticed or is being taken into consideration

40:21

by the application. So for example, let's see if you go to Amazon, there are a lot of buttons,

40:25

right? Everything you can click upon, that is a button, that is acting like a button. So when

40:28

you click on something, for example, after writing iPhone, when you click on search, it generates,

40:33

it triggers an API call. So your front-end application makes an API call to whom,

40:39

to the backend. Because backend is the actual brain of your application, which is actually

40:44

doing all the processing. So your front-end, this is your front-end application. This is your front-end

40:53

application, and your front-end application generates an API call to the backend. So this is

40:59

slash search. Now everyone, this is the endpoint. This is the endpoint. This is the endpoint.

41:03

Now what happens, everyone? When you make an API call, you can see the browser link.

41:08

You can see the link in the, in the URL on the browser. You will notice that on Amazon,

41:14

you will see the link like this. HTTPS, slash slash, www. Amazon.in. I'm not writing

41:21

that initial part, right? So you will see that Amazon. Dot in slash s. S stands for

41:27

search. Slash s, question mark, and then everyone, whatever search query that you are passing.

41:33

For example, if you're searching for iPhone, you will say that query is equal to iPhone.

41:38

Okay? Then it might have some other metadata also, which is required to execute the request.

41:42

But this is how the typical structure of an API looks like. Every Amazon API will have, can I say that,

41:50

if I write the complete HTTP URL as well. So you will see something like this, HTTPS,

41:56

column, slash, www.w.w.m. You will see something like this. Now, folks, can I see something like this? Now, folks, can I

42:03

that this part, this HTTPS, Amazon.in, this will be common in all the Amazon APIs.

42:11

Whenever you want to, if you want to search a product, if you want to place an order, if you want to go to

42:15

cart, if you want to add a product to the cart, if you want to see your orders, if you want to cancel

42:19

an order, whatever operation you do, this part will be common. Yes or no? Whatever operation

42:26

you perform, this part is always going to be common for all the Amazon APIs, Amazon functionalities.

42:33

This is everyone, you can say that. This is the protocol, HTTP protocol, the protocol on which

42:38

internet works. And more important part everyone is this, this www. Amazon.in. This is the domain,

42:46

everyone, the domain of the application, right? Like Amazon.com, flipcard.com, masai school.com,

42:53

etc. So these are domains. And then everyone, whatever you see after slash, this is your API

43:00

name.

43:01

the name of the API, right? The name of the API is generally, technically, it is called

43:08

as API endpoint. This is the end point of the API. This is API endpoint. Is that point clear

43:16

to all of you? This is API endpoint. I will show you this in demo. Don't worry. And then everyone,

43:24

after question mark, you have this query parameter. Okay. The parameter for this API

43:31

query, right? This is query parameter. Is that point cleared all of you? Is that point cleared all of you?

43:46

Now let me show you this thing, everyone. If you go to Amazon, right? If you go to Amazon, everyone,

43:54

and if I search for any product, let's say if I search for maybe iPhone, right, you will see this thing, right?

44:01

Are you able to see this? Amazon.com slash S, question mark, K is equal to iPhone.

44:06

Just copy this. And after this, everyone, all of these are parameters that are automatically coming

44:11

from the browser, from the front end, which are required for communication. What is the

44:16

meaning of slash s? It is just the name of the API. It is just the name of the API. It is called

44:22

this API endpoint. Now in Amazon, everyone, the API endpoint is slash S. Slash is not very,

44:29

very much readable. But if you go to flip card.

44:31

that everyone. If you go to Flipcard, you will see that if I, if you search for iPhone,

44:39

if you search for iPhone now, what is a query? Now what is a query? Look at the query. Look at the

44:49

API call. Flipcard.com slash search. Now do you see that slash search? So folks,

44:56

this Flipcard.com, www.com, www.com, www.com, www. amazon.com, dot in,

45:01

These are the domain names. So all the APIs that you perform on these platforms,

45:06

the domain will be seen. What is going to change the end point, the name of the API, that is slash

45:12

search, slash orders. If you want to perform any operation on orders, if you want to cancel the

45:18

order, if you want to see all the details of the orders, et cetera, et cetera, if you want to

45:23

place an order, if you want to, let's say, track, right, if you're tracking some order, if you click

45:27

on tracking, then the API call could be the, the one.

45:31

What could be the name of the API?

45:32

www.amazon.m. slash tracking slash order ID, right?

45:38

That you want to track this particular order ID. Does that make sense to all of you?

45:44

Folks, is that point clear to all of you? Just a second, I think. Yeah. Everyone clear?

45:57

Okay, folks, now we will be seeing these APIs. Do not worry. So, I hope. I hope.

46:01

everyone is clear with the definition of API. Now, front end, everyone knows whatever

46:05

user sees in front of them, that is front end. And then everyone, the request goes to the back end.

46:11

Okay? So there is a backend component which is working behind the scenes, which is not

46:14

directly accessible to the user. Okay? So this is back end of Amazon.com.

46:25

Right? So what this backend will do, everyone?

46:27

So guys, what is the task of the backend? I would say that backend will get the API

46:36

request. So first of all, everyone, a big company like Amazon Flipcard, they might have thousands

46:40

of APIs, right? They might have thousands of functionalities. Yes and no? Correct? Then everyone,

46:48

every functionality can have a lot of complexity also. For example, when you search, after searching

46:52

also everyone, you can put a lot of filters. Okay? If you go to, let's say, if you search for any

46:57

product on Amazon, then you can put filters. Delivery within two days, price less than this,

47:02

greater than this, within this range, right? This is the color, this is the RAM, etc, etc.

47:07

Right? So these complexities, like these complexities are associated with any API call.

47:13

So what your backend does is, back end takes the API request. It processes this request.

47:18

Right. For example, everyone, if you go to a restaurant, if you go to a restaurant, what do you do?

47:24

you sit on the table and a waiter comes to you, you give the request to the waiter.

47:29

Then what your waiter does?

47:31

waiter takes the request, takes your input parameter that you want to have these dishes,

47:36

and the waiter passes on the request to the chef, to the kitchen.

47:41

He goes to the kitchen, gives your request there.

47:44

Now, chef prepares the dish. It will take some time.

47:47

And then chefs gives the response, the item to the waiter, and waiter gives you back.

47:53

You can say that.

47:54

everyone, front end acts like a waiter. Does that make sense for all of you? That front end

47:59

is typically acting like a waiter. Because what front end does, it takes the request back.

48:05

Frontend does not do any kind of processing as such. Frontend takes the request. For example,

48:11

what you want to search, what you want to order, if you want to track the order, if you want

48:15

to see the order details, etc, etc. Frontend takes your input parameter. Frontend gives the request

48:21

to the waiter, sorry, waiter gives the request to the chef. Chef is actually the back end.

48:27

Now, guys, whether you are going to act, let's say, you can say that, most important part of any restaurant,

48:33

don't you think, like, even if the service is not that good, it might be okay. Even if other things

48:38

are not good, it is okay. But if the food is not good, then it is something that cannot be compromised,

48:43

correct? Other things may be compromised, correct? And if the food is really good, maybe you might be

48:51

ready to forget about other things. Even if some things are here and there, you might be

48:55

okay with that. Because that is the most important component of any restaurant. Similarly,

49:00

everyone, for any entire software application, right, if you club all the things, for the entire

49:07

software application, I would say if you have to give the importance, right, what is the most

49:12

important component? That is going to be the backend. Because if back end is not properly structured,

49:17

if the backend is not properly working, if the backend is very, very slow,

49:21

Let's say backend takes your request and to search the products related to iPhone,

49:25

back end is taking 10 minutes of time.

49:28

Doesn't matter how beautiful the website is for Amazon.10. But if to search iPhone, a simple

49:34

keyword, it takes 5 to 10 minutes of time. Does it really matter how good the website is,

49:40

how beautiful the website is? No, people are not going to use it, right? Because the backend is not

49:47

properly scaled, back end is not properly working. It is taking 10 minutes

49:50

to search a very simple item, right? So that's why everyone back-end is the most important

49:55

thing, which takes the request and it processes the request. It processes the request. Is that point

50:02

clear to all of you? Yes or no? Is everyone clear? Yes or no? Okay. Now everyone tell me that if you

50:14

talk about Amazon, right, Amazon will have millions of products, multiple millions of products, and it will have

50:19

millions of users of data. Do you think that all the data, products data, users data,

50:24

tracking data, orders data, everything, can be present in the backend? Typically not. Even for

50:33

a smaller application, like Amazon is a very big application, but even for a smaller application

50:37

with only few thousand users, you generally don't store the data inside the backhand application

50:43

because backend applications, ideally, if you store data as well, if you do processing as well, it will

50:48

become very blotty, right? It will become very big application because data is also there,

50:53

processing is also there. So what do you do? You follow a simple approach of separation of concerns.

50:58

You try to separate the responsibilities. You try to divide the responsibilities. So you give the

51:02

backend the responsibilities of processing and everyone, you have a separate component of database.

51:08

So if you're searching something, backend will process the request, back end will identify what

51:13

input parameter is coming, what type of request user is making, etc. And then backend will make a call to

51:17

the database, right? For whatever request, some data is required. You give the query that,

51:23

okay, user is searching for iPhone. So database will give you the products back, right? And then

51:29

that, whatever data you are getting from the database, you might have to do some processing on the data

51:35

to send in a particular format and then you send the response back to the front-end application.

51:41

This is the complete cycle, everyone. So user makes a request to the front-end. Front-end makes a request

51:46

to the back-end.

51:47

And makes a request to the database. Database gives the response back. The response comes back to the front end. And then front end makes a request, sends the response back to the end user. This is the complete cycle of the application. Does that make sense for all of you?

52:17

This is a typical structure even every application follows in the entire world.

52:22

Every application, on a high level, it follows the same architecture.

52:25

Front-end, backend databases. There might be some more components as the complexity grows.

52:29

There will definitely be slightly more components as the application grows, as the scale grows, obviously.

52:35

But again, you can typically divide any application into three major components, front-end, front-end, backend database.

52:41

Now everyone tell me how and where you can structure your AI agents into this.

52:47

this software in this kind of application. Where the agent comes into picture.

52:53

What do you need to build for an agentic AI application?

53:01

Where does agent comes into picture? Do you build agents on the front end, on the back end or on the

53:08

database? Absolutely correct. Generally, you write the code for agents on the backend on the

53:14

back-end application. Then everyone front-end will definitely have, but

53:17

front-end user will not be aware, right? So for example, if you're using

53:20

MicMetreb, the chatbot, or the Amazon chatbot, or the Svi chatbot, do you really

53:26

see that, okay, you are talking to an agent or you are talking to some different software application?

53:30

Not really. For an end user, it is just a front-end. Through the front-end, you are giving the message,

53:36

front-end is taking the message, giving to the backend. Now everyone, in that message,

53:41

based on the request coming in the message, based on the message coming from the user, then your

53:46

backend will decide that do I need to create an agent for that? If you are asking to book a flight,

53:52

then back-end needs to create a separate agent for that. If you are trying to cancel the flight,

53:56

back-end might have to create separate agent for that. If you're trying to book a hotel,

54:00

there might be a separate agent for that. If you want to generate an itnery, there might be a separate

54:05

agent for that. So back-end is the brain of the application that will decide what agent we need to

54:11

create. So generally, everyone, where does the agent comes into the picture in the backend application?

54:16

Does that make sense to all of you?

54:22

Right? Let me give you some example, everyone, and then I think we will go for a break.

54:27

Okay? So let's have an example, right? Let's say, everyone, you go to Amazon or let's say you go to

54:32

Swiggy and you go to my orders. What kind of API call you are making? If you click on my orders,

54:39

what kind of API call you are making?

54:46

You are trying to get the details, right? Can I say that? Get the order IDs, get the order

54:52

details for a particular user. Correct? So what API request you are making? Let's say

55:02

the API call is like, show my orders, correct?

55:16

show my orders, correct or not? Right? Now, how the typical flow will look like?

55:25

Can I say that everyone? First of all, the user clicks on my orders.

55:38

User clicks on my orders? User clicks on my orders. Then everyone, from the request,

55:46

Frontend is getting the request. So after this, front end sends the request, sends the API request to the back end?

56:06

Yes, no, everyone? Frontend sends makes the API request to the back end. After this, everyone,

56:12

Backend will receive the API request.

56:18

Backend receives the API request. Then everyone, back end might have to validate the request. For example,

56:27

everyone, let's say if I'm logged in, right? If I'm logged in, then backhand might validate that

56:32

whether the user is, for example, even if I want to see my orders, I should be logged in, right?

56:37

I cannot see the orders without logging in. Right? So back end will check that whether the user is properly

56:42

log in or not. So back end might validate the user. Backend validates the user.

56:49

Okay? After validation everyone, what happens? Backend? Now guys, the order details, where the order details will be present?

57:12

the backend or will it be present in the database? Database? Backend makes a query or

57:18

back end sends a query to database. Sends a query to DB. What kind of query could be everyone? For example,

57:27

let's say if this is a very simple SQL database, can I say that a simple query like select, start

57:33

from orders where user ID is equal to 1, 2, 3. For this user, give me all the orders, correct? As simple as that.

57:42

Correct or not? Absolutely yes. Then everyone, back-end. Now, database sends the response to back-end.

57:52

And then, the response to back-end, and then's the response-to-back-end.

58:12

sends the response back to front end.

58:19

Back to front end.

58:25

This is how typically it works.

58:28

Please let me know if this complete flow is making sense to all of you or not.

58:42

Is everyone clear? Have a look at it and tell me.

58:49

Now I will just show you, before we go for a break, let me also show you a slightly more technical

58:56

view of this flow. Folks, front end makes a call to back end. Now what type of call is it going

59:06

to be? Now on a high level level there are like four type of calls, right? Any operation can be divided

59:12

into four types, CRUD, create operation, read operation, update operation, delete

59:20

operation. Now if you are trying to get the details of all the orders of one, it is a create

59:26

operation, read operation, update or delete. What type of operation is it? It is a read

59:32

operation because you are just trying to read the data. You are not doing any changes. You are

59:36

not doing any update. For read operations, everyone, the API call is of type get because you are trying

59:42

to get the details. Let's say get slash orders, right? And then everyone, let's say just

59:49

slash orders and maybe the order ID, maybe the user ID might be coming from, let's say the login

59:55

credentials or the token. Slash orders. Does it make sense for all of you? Slash orders. Because this

1:0:02

is the API call. Get type, get is the type of the call. Slash orders is representing get all the orders

1:0:10

for the user who is making the call. Does it make sense to all of you? Then everyone,

1:0:16

the request goes to the backend. Backend will understand the query. Backend will process

1:0:20

the query. Then back end will make a call to database. Now everyone here, you will, maybe you might

1:0:26

make a SQL query. Simple SQL query. Simple SQL query, simple SQL query, like select star from DB,

1:0:33

select start from orders where user ID is equal to this. And DB will send the response back to the back

1:0:38

right? So let's say this is step number one. This is step number one. This is step number one. This is step number two. Backend will send the response back to database will send the response back to back end. And back end will prepare the response and send it back to the front end. This is more technical thing because now we have talked about get and SQL query. Is this is this thing also making sense for all of it?

1:1:08

Okay. So folks, now I think if this is clear, we can take a break now. Okay. Just one more thing. What kind of response you will expect at this stage. Finally, what type of response you will get? Can is that, let's say, you will get the list of orders.

1:1:38

be list of orders. Correct? Absolutely correct? So guys, one order will look

1:1:49

like this. Let's say this is order ID, right? Some order ID. Like maybe the date of the order,

1:1:56

when this order was placed, okay, item in the order and so on, like something like this. This is one, this is how one order looks like. But you will have a list

1:2:08

of such orders. So simply cut and you will have a list, order one, then next order and so on. Is that point clear to all of you? This is the kind of response you can expect from the above API. List of orders. Is the idea clear to all of you?

1:2:38

Folks clear? Now what type of data is it, everyone? What type of data is it? What type of data is it?

1:2:49

This is type of JSON. Okay? This type of representation is called as JSON representation of the data. We will see what JSON is. How do we use JSON? Right? After the break. Everyone clear till this point of time or not?

1:3:08

Is everyone clear? Then we can have a break. I will share the link of the notes.

1:3:13

Please go through the link.

1:3:19

We can have maybe 12 to 13 minutes of break.

1:3:26

We can meet around 915, 916.

1:3:33

Okay? See you after the break everyone.

1:3:38

Thank you.

1:4:08

Thank you.

1:4:38

Thank you.

1:5:08

Thank you.

1:5:38

Thank you.

1:6:08

Thank you.

1:6:38

Thank you.

1:7:08

Thank you.

1:7:38

Thank you.

1:8:08

Thank you

1:8:38

Thank you

1:9:08

Thank you

1:9:38

Thank you

1:10:08

Thank you

1:10:38

Thank you

1:11:08

Thank you

1:11:38

Thank you

1:12:08

Thank you

1:12:38

Thank you

1:13:08

Thank you

1:18:08

Hi,

1:18:11

I am I am I am I am I am how everyone.

1:18:23

I am how I am how audible?

1:18:25

Okay.

1:18:26

Okay.

1:18:27

So let's get started with

1:18:29

Let's get started with the next

1:18:33

which is the rest API's.

1:18:36

Okay.

1:18:37

So, so folks, let's get started with the next topic, which is the rest APIs. Okay. So as of now, we have understood the rest API's.

1:18:38

term APIs. But there is a term which comes very very frequently almost every time with

1:18:46

API that is rest. Now everyone this term rest APIs is a very frequent thing that you must have heard

1:18:55

about right? So API is what we have discussed and there is a term called rest as well. Have you

1:19:01

heard about rest? Correct. Okay. So guys, rest

1:19:08

is actually a short form of this representational, representational, representational

1:19:35

of rest, S and T.

1:19:38

So this is a this is a full form. REST. Now rest, you can see that everyone, the term rest just tells you

1:19:47

you how to design your APIs. Simple. How to design and structure our APIs. For example, everyone, we saw that.

1:20:07

We saw that API name slash search. Although search is an operation, but most of the

1:20:13

times you will see API's name like slash orders, right? If let's say you are making a payment

1:20:19

call, let's say Amazon is making a call to payment gateway for the payment. So you will see that

1:20:23

slash payments. Okay. If you're trying to create a user, if you're trying to update some

1:20:30

user details, if you're trying to delete a user, right? So you will see slash users.

1:20:35

slash, let's say, students, something like this. So most of the API names everyone,

1:20:44

you will see like this. This idea is coming from rest. Again, this is not a mandatory thing again.

1:20:50

If it is your application, you can give whatever name you want. It is not a hard and fast rule

1:20:56

that you will have to design your APIs in a particular way. No, you can define your APIs. You can define your

1:20:59

APIs in whatever name, in whatever way you want. This is not at all.

1:21:05

a strict way or a strict policy. This is just a convention that most of the people

1:21:11

follows. As simple as that. So rest says that anyone, like the what is the rest principle

1:21:17

says? Rest principle says that our APIs should be structured around the resources. So

1:21:24

what it says, let me write the definition. Rest principle.

1:21:35

It says that APIs should be structured around the resources.

1:22:05

but the data that they are working upon. Can I say that everyone? Every API will be working

1:22:11

on some data. It might be creating some data. It might be updating a data. It might be reading

1:22:16

a data. It might be deleting the data. Right? So every API will be performing any of these

1:22:26

operations, CRUD. And guys, now to do these operations, you need some data. Correct? So for example,

1:22:33

if you're going to Amazon, you might be, let's say, you might change your phone number,

1:22:38

you might change your address, you might place an order, you might delete an order, that is cancel

1:22:43

the order, you might, let's say, change the order, anything you can do. So don't think every operation

1:22:49

comes under these four categories? Now everyone, whenever you can think of any operation that you do

1:22:55

online, can I say that, you are performing one of these operations on some data. Data is nothing

1:23:02

but resource. You are performing one of these operations on any of the resource.

1:23:06

Maybe a user resource. You might be updating the user, creating a user, deleting a user,

1:23:11

etc. You might be creating an order, updating an order, etc. You might be generating a payment.

1:23:16

You might be canceling the payment. You might be updating the payment status, whatever. Similarly,

1:23:21

students also. So API names, APIs should be structured around the resources. It means that

1:23:27

this is how your APIs should be structured slash orders. It means that,

1:23:32

This API is talking about, is doing some operation on orders. It can be create, it can be update, it can be delete. Does that make sense to all of you?

1:23:44

Does it make sense to all of you?

1:23:49

Okay. Okay. Now, everyone, the rest principle says that, that the operation that you are performing,

1:24:02

Ideally, it should not be the part of your API signature or API endpoint. For example,

1:24:10

let's say, if you sign up, you're creating a user, correct? If you're trying to sign up,

1:24:17

it means that you are creating a new user in the back end, in the database. If you're log in,

1:24:22

then you might be updating the user details because you might be creating a token. Or

1:24:27

user can change their phone numbers or user can delete their account. So can I say that everyone,

1:24:31

for user. These might be different operations. Let's say create user. This can be one API.

1:24:40

Then update user details if you're changing phone number, address, password, whatever, right?

1:24:45

Update user. You might be get user, right? You might be get the, you might be, you might want to get the

1:24:54

user details, get user, delete user, right? So if you see everyone, again,

1:25:04

four operations, C, R, U, D, R means get only, right? Rate means get only. Now, as per the rest

1:25:12

principles, this is not a good way of naming your API. Again, everyone, functionality

1:25:19

wise, does it really matter whether you are giving the name of the API like this or something?

1:25:24

something else. Functionality-wise, does it really matter? No, functionality-wise, it does

1:25:29

not really matter. It is just a convention, which REST says. And everyone, honestly, a lot of people

1:25:35

follows REST, but after certain extent of time, after some certain point of time, it is not 100%

1:25:41

possible to follow REST. So what REST says? That whatever operation you are performing,

1:25:47

it should not be the part of API endpoint. Rather, instead of this.

1:25:54

What you should have is, you should just have an endpoint slash users. Now, what operation

1:25:59

you are performing on user should be defined by the HTTP method, that is get method,

1:26:05

put method, or let's say, get, post, put, put or delete. It means that everyone, when your front end

1:26:17

makes a call, right? When your front end makes a call to the back end, in the front end code, you can

1:26:23

select what type of method call, what type of API call you want to make to the backend. So

1:26:29

you want to make a get call, you want to make a put call, you want to make a patch call, you want to make

1:26:34

a post call, etc. So everyone, if you make get call, see, if you make a get call, add slash users.

1:26:44

If you see API endpoint is get, API endpoint is slash users, the method type is get. What type of

1:26:51

API is this? What type of API operation is this? It is a read operation. Correct?

1:26:59

Get user details. Then you can pass some ID also that get me the user details of this ID. Okay.

1:27:05

Then if you make a post call slash users, post slash users, right? So it is a read call.

1:27:16

Then it is a post means a create call. Okay. So guys, post, post,

1:27:21

means create operation. When you want to, when you need to create some resource on the

1:27:26

backend, right? When you're creating an order, when you are creating a user, etc. Are you

1:27:31

guys getting this point? Are you guys getting this point? Okay. So, get means read or you can

1:27:41

say that, get means fetch resource.

1:27:51

fetch resource, right? Then we have post. Post means create. You are creating a resource,

1:27:58

right? Post means creating a resource or add a new resource. Okay? Add a new resource.

1:28:12

Then everyone, we have, if you see, C, R, then next is update. Update everyone, there are two methods that you can make

1:28:20

for update. One is put, one is patch. What is the difference between them? I will talk

1:28:26

about it. First, let's talk about patch actually. Okay, patch slash users. So guys, patch means

1:28:34

update. Patch means update. Now, guys, for example, let's say if you already have an account

1:28:45

at Amazon and you want to change your address, you want to change your phone number, you want to change your email

1:28:50

ID. You want to change your password. It means that everyone in any of these operations, can I say that you are partially updating the user? You're not replacing the complete user, right? You're just updating one or two or three details, right? One or two or three attributes about the user. So patch means partial update. When you just want to update few attributes about the entity, not you don't want to replace a complete entity. Rather, you just want to replace, you just want to update few attributes, one or two or three.

1:29:20

Right? So it is called us partial update. Is that concrete all of you? Partial update.

1:29:28

Right? Then everyone, wouldn't it create confusion if we have endpoints with the same name? It does not. Generally it does not because as a developer, you will be aware of these things.

1:29:38

It might create confusion for people who are not aware of these principles. Right? But if you're aware of these principles, then it will not.

1:29:46

Right? But yes, that is one disadvantage. What if let's say, you want to have.

1:29:50

have two type of get methods. One method is get the get me the detail of all the users or get me

1:29:58

the details of a particular user. Then don't you think both of them will be slash users, okay? And type of

1:30:04

method will be get. In that case, answer is yes, it can create a confusion. So that's why

1:30:09

what I said initially that you generally don't follow or you cannot follow rest principle

1:30:15

100%. But these are the principles everyone. Just try to follow one or two times like

1:30:20

for a few APIs. At certain point of time, you will always realize that it is not practically

1:30:25

feasible to follow this rest principles. So you disobey that role as well. Completely okay. Because

1:30:31

these are just good practices. These are just good practices. What about option calls? What I did

1:30:37

not get what about like what do you mean by options? So is the patch clear to all of you? First

1:30:45

of all of you, is the patch clear to all of you? When you just want to update few attributes about the entity.

1:30:50

Then everyone, there is a put method as well. Put is also update everyone. But if you want

1:30:56

sometimes, you might have to replace the complete user. Replace kind of means that, for example, let's say there is a user at Masai. Now that user has, let's say, if we want to replace that

1:31:14

complete user, ID will remain same, right? But we want to replace the complete object altogether.

1:31:20

For example, let's say if it is possible at some institute, at some, let's say, at some academy,

1:31:25

it is possible that you can transfer your ownership.

1:31:28

For example, let's say generally I think some online gym things like maybe cult, etc.,

1:31:33

that gives you this option, that you can transfer your membership to some other user.

1:31:37

Correct?

1:31:38

Now, assume that, I'm giving you that scenario, maybe think hypothetically.

1:31:42

Let's say cult, cult fit provides you to transfer your membership.

1:31:46

Now while transferring the membership from one person to another person, what it does?

1:31:50

is it will replace the membership details, it will replace the membership details from

1:31:56

the current user to the new user. So don't you think everyone, in that case what is

1:32:00

happening is that the membership object is completely getting replaced from the old user

1:32:06

to the new user. So it means that everyone here, if you see, this is also an update operation,

1:32:12

this is also an update operation, this is also an update operation. Both of these are

1:32:16

update operations only. But in the first one, you are just updating

1:32:20

few parameters, one, two, three, four parameters. Maybe let's say out of 10 parameters,

1:32:24

you're just updating two parameters. That is partial updateer. Put me, what you do? You replace the

1:32:30

complete object altogether. It means that you don't want to have the current object. You just want to

1:32:35

replace the current object with some new entity. Now you don't have any instance of the old object.

1:32:42

Are you guys getting this point? Yes or no? Just let me have a sip of water. Just give me a second.

1:32:50

Sometimes in the summer it is very difficult to speak for even 10 minutes without having a sip of water.

1:33:07

Generally in the summers this problem we face, right? Anyways. So are these four different type of methods

1:33:13

cleared all of you? Get, post, put, patch. Then everyone, there is other type of method which is

1:33:20

which is I think self-explanatory when you want to delete a resource. In delete,

1:33:25

there is nothing complex slash users, delete a resource. If you want to delete a particular

1:33:32

user, for example, let's say some of the applications gives you to delete your profile. If you go

1:33:37

to your profile, you can select, you can click on delete operation. It will delete your

1:33:40

complete profile from the system. So this is a delete operation. So if you see everyone,

1:33:50

All the crud operations are defined here. So let me highlight these methods. We have a get method. Get means getting the resource, reading the resource. Post means creating some data, adding a new resource. Patch means update, partial update, put means update, but replacing the complete object, updating the entire object. Delete means delete.

1:34:14

Everyone clear? Until this point of time, yes or no.

1:34:20

Okay. Now, for example, you know, let's say at Amazon, you have some product, get product

1:34:30

API. Okay? So let's say you have get product details API.

1:34:36

Okay. Let's take an example, everyone, of Masai School, right? So let's say get courses.

1:34:48

Right? Get course details.

1:34:49

Now, guys, can I say that at Masai, there might be, let's say, 20 courses or 30 courses.

1:34:55

Correct? Now, when you go to the home page, you will see that courses section. If you click on

1:35:01

courses section, if you click on courses section, don't you think it will show you all the

1:35:05

courses, all the 20, 30 courses? Yes or no? So when you click on courses button, what do you

1:35:12

think what type of API call is being made by front end to the back end? What kind of API?

1:35:19

call front end might must be making to the back end get call. Okay, very good. So it must be a

1:35:25

a get call. What will be the end point? Slash courses. Right? Slash courses. So guys,

1:35:32

what this slash courses does? Get details of all the courses.

1:35:49

Get details of all the courses. Correct, everyone?

1:36:02

Now, tell me everyone, if you want to get the detail of all the courses, do you want any input parameter

1:36:07

to this? That course ID 1, course ID2, course ID 3, etc. If you want to get the detail of all

1:36:14

the courses, do you want any input parameter? Maybe not. But everyone, now, if you go to the

1:36:18

Maasai school website and when you go to a particular course, let's say if you click on a

1:36:22

particular course, let's say software engineering or let's say agentic system design, if you click on

1:36:27

that, now tell me everyone, it will also be a get call, it will be also a course's call, but for that

1:36:34

everyone, because you are trying to fetch, you are trying to get the details of a particular course,

1:36:40

then you need to give the idea of the course. Correct or not? Then only you will be able to fetch

1:36:45

the details of a particular course. Then everyone, you can say that. It will also be a get

1:36:50

call. Get slash courses. Then everyone, you will have to give the course ID or course, maybe let's

1:36:58

say course unique number. Let's say course ID 1, 2, 3. So slash 1, 2, 3, everyone. Slash courses

1:37:05

slash 1, 2, 3. It will give me the details of course ID, get, get,

1:37:15

details of the course with ID 1-2-3. Is that point clear to all of you? Yes or no.

1:37:32

It is as simple as that even, you know, that like when a teacher goes to the, to the, to the classroom,

1:37:41

and when when teacher asks a general question, everyone will respond.

1:37:45

But when teacher will ask the question to a particular student, they will take the name of the

1:37:49

student or they will take the role number of the student. So that the query is only applicable to

1:37:54

the particular student. Same thing. Right. So now everyone, this type of parameter, you can also

1:38:00

pass, like, now do you see that everyone, I think there was a question that, okay, how do we identify these

1:38:06

things? This is also get, this is also get, this is slash courses, this is slash courses. Now everyone,

1:38:11

if you see, if you make an API call without input parameters, you know,

1:38:15

without any ID, it means that you are trying to get the detail of all the students, you are trying

1:38:20

to get the detail of all the courses. If you make a get call at slash courses and after slash

1:38:26

if you pass a number, then you are trying to get the details of a particular course with this ID. Is

1:38:32

that point clear to all of you? Is that point clear to all of you? Okay. Then everyone now, after

1:38:39

get, let's try to understand about post query. Okay.

1:38:45

For example, everyone, now we want to create a post, right? Post means we want to create a post means we want to create an entity, create a resource. For example, let's say at Amazon, there is a slash orders API. So we make a post call slash orders. Now tell me everyone to create an order. Do you need multiple things? Order ID, date of the order, who plays the order, what is a product in the order, etc, etc. So order will have multiple things, right? And how will you pass the multiple things?

1:39:15

Now, one order, like, depending on how many details you are trying to store for a particular order,

1:39:20

can I say that one order can have 100 parameters also?

1:39:25

One product can have hundreds of parameters also. Now, everyone, when you want to pass multiple things,

1:39:31

multiple parameters, and you don't know how many parameters it can have, it can be 10 parameters,

1:39:36

it can be 1,000 parameters also. Then you pass generally, with post methods, you pass request body.

1:39:42

because everyone, if you have to pass hundreds of parameters after slash slash slash,

1:39:48

don't think it will be very difficult to read. If I pass 100 parameters like this, slash x,

1:39:54

slash y, slash z, slash a, slash B, etc. It will be very difficult for anyone to read.

1:39:59

That's why everyone, what comes into the picture? Request body comes into the picture.

1:40:05

Is that point clear to all of you? Request body comes into the picture. And in request body, everyone,

1:40:10

what do you pass? You pass whatever.

1:40:12

details you want to pass inside the product, uh, inside the order. For example, let's say

1:40:16

you pass that create an order, generate an order with order ID. One, two, three, some order

1:40:26

ID, right? Let's say maybe product, what product is there in the order? Or let's say date of the order.

1:40:38

What is the date of the order? What is the date of the order? What is the status of the order?

1:40:42

delivered or not delivered, et cetera. And there can be any number of parameters.

1:40:47

Is that point clear to all of you? Yes or no. So when you pass this kind of JSON object,

1:40:55

inside the input, this is called as request body. This is the body of the request that you are

1:41:02

making a call to. And generally, everyone, request body is passed in post APIs as well. And in some

1:41:08

other type of APIs, we will see that. Everyone clear? Yes.

1:41:12

Okay. Then everyone, for patch or put, let's say for patch first.

1:41:29

Okay, let's say patch slash user. So I want to update the details of this user with ID 1, 2, 3.

1:41:36

Now, guys, in patch also, it is a, it is a partial update. But in partial update also, it is mandatory.

1:41:42

that how many attributes you can update?

1:41:45

1, 2, 3, 4, 10, 20, 100.

1:41:47

Let's say, in our system, we are storing 100 attributes for a user.

1:41:51

Out of 100 attributes, you can update 1, 2, 10, 20, 30, any number of parameters.

1:41:57

So again, everyone, is it a good decision to pass the parameters that you want to update for a user with this ID

1:42:04

in the, in the URL, in the endpoint? No.

1:42:09

That's for everyone. In patch also, you can have a request body.

1:42:12

In patch also, you can have a request body.

1:42:18

And inside the request body, everyone, you can pass whatever parameters you want to update for the user.

1:42:23

For example, let's say I want to update the phone number of the user.

1:42:28

I want to update the phone number of the user.

1:42:30

I want to update the address of the user.

1:42:37

I want to update the address of the user.

1:42:40

Is that point clear?

1:42:42

to all of you? Is that not clear to all of you? Now tell me everyone, can you

1:42:52

follow the same kind of structure for put also? Because input also, you are replacing the complete

1:42:59

object. So what you can do? Replace a product with the, replace a user with this ID, replace all the

1:43:06

existing details with these new details. So for patch and put also, everyone, you can use request

1:43:12

body.

1:43:12

Is that all of you? For delete, do you need a request body? For delete, do you really

1:43:21

need a request body? Maybe not. Okay? Maybe not. Because delete can what you can

1:43:28

do? You can simply say that, okay, delete a user with ID 171. That's it. Delete a user with

1:43:37

ID 171. Is that concrete all of you?

1:43:42

Is that point clear to all of you? Yes or no? Okay. So is the concept of HTTP methods

1:43:51

also clear to all of you? Get, put, post and patch, update, delete, everything. Okay. Now everyone,

1:43:58

every API will have a following structure. Structure of API request. This is very simple concept. Let's talk about this.

1:44:04

structure of API request. Typically, everyone, every API structure will look

1:44:17

like this. First of all, it will have the end point. That is the URL. That is slash orders,

1:44:26

slash users, slash payments, etc. Then it will have the method, whether it is a get method, put method,

1:44:34

post method and whatnot, then it will have the headers. Now generally everyone, in the

1:44:41

headers, what kind of details are present? For example, if you are logged into Amazon on your

1:44:47

browser, right? Do you need to log in every day or after every few minutes, do you need to log in?

1:44:53

no, right? You can place an order. For example, for months and months, everyone, you don't have to

1:44:59

log in again and again. By what happens everyone, when you log in for the first time, your

1:45:04

server gives you a token, the authentication token, right? And the browser stores that

1:45:10

token. Now tell me, if I'm logged in with my, let's say, Masai account, or with my Amazon account,

1:45:16

with my FlipCard account, and when I try to place an order, that order will be placed on my account.

1:45:22

How FlipCard server or back, or Amazon server identifies that, that Deepak is trying to place

1:45:27

an order, or Shilpe is trying to place an order, or Nisarg is trying to place an order, with authentication,

1:45:33

with the token, with the login credentials, correct? Who is logged in? Now, do you really

1:45:41

pass your credentials again and again? That who are you? What is your email ID? What is your password?

1:45:45

Do you do that again and again every day? No. Because the token is present in the browser.

1:45:52

And the browser, with every request, browser sends the token to the server.

1:46:03

about the user are generally attached in the headers, right? So I will show you this

1:46:09

in the upcoming class, don't worry, that on the browser, in the request everyone, browser attaches

1:46:15

a lot of information. And the header information, the header of the request contains the user

1:46:22

credentials, the details, for example, the token. So that server can identify that whether this

1:46:27

is a legitimate user or this is not a legitimate user. Are you guys getting this point? URL we know

1:46:33

slash orders. This is URL. Method is get put post, get put, post,

1:46:38

patch, delete. Headers is used for authentication details. And then everyone, we have request body.

1:46:46

Now, body is not always mandatory, everyone. Some requests may have body. Some requests may not

1:46:51

have body. Also, everyone, header. Is header also mandatory? Is header also mandatory?

1:47:01

Answer is no. Heder is also not mandatory.

1:47:03

everyone? Why? Because header can be empty also. For example, you can do a lot of operations

1:47:08

without login also. You can watch a lot of videos on YouTube without login. But everyone

1:47:14

tell me, if you are trying to watch a private video on YouTube, for example, like a lot of channels,

1:47:19

they have their join button. Correct? You can pay some amount of money and you can join their

1:47:25

channel membership. Now, if you are not logged in, can you watch a private video of that channel?

1:47:33

membership video of that channel. For example, let's take a very simple example. Can you watch a movie on Netflix without login without having a subscription? No. For that everyone, you need to login. Can you watch free videos on YouTube without login? Yes. Are you guys getting this point? But in URL, we don't have the methods that you don't see because the front end is attaching these things internally, right? That you don't see in the browser in the URL. So those requests, those parameters, header, body, methods,

1:48:03

they are going internally via the front end to the back end. Makes sense. For example, for example, everything has a proof.

1:48:14

Go to Amazon, go to inspect element, right? Go to network. And let's try to make a request. Let's say I make a search request iPhone. And you will see that as soon as I search, you will see that.

1:48:33

you will see that search request slash s.

1:49:03

I think one, go to Flipcard, go to InspectCard, go to InspectElement, close, go to network tab,

1:49:16

and search for iPhone. And here, everyone, you will be able to search, see this request very easily, search.

1:49:24

Do you see that now the search request? So if in the network tab, you will be able to see all

1:49:28

the request and responses coming over the network. Whether Frontend is making a request,

1:49:33

frontend is receiving the response, you will be able to see in the network tab. Now, when you go to

1:49:37

slash search this thing, this is showing you the search API. You can go to the headers. Do you see that

1:49:43

everyone? First of all, in the headers, right, inside the headers, there are multiple sections, right? You will see

1:49:48

that request method is get. Are you able to see that? Request method is get. So guys, this is not

1:49:54

the actual header. It is containing a lot of things, right? The header, it will have here. Content type is

1:50:00

HTML and it will have, like, it has multiple components, right? And then everyone,

1:50:08

you see the get request and everyone, then you see the request URL. Okay? And then everyone,

1:50:14

you will also see that, yeah, you see that request headers. In this request header, everyone,

1:50:22

if you see I'm not logged in. So that's what everyone, you will not see any token kind of thing here,

1:50:27

right? But now you try to make a request after login.

1:50:30

Right. Then you will be able to see a lot of other user specific details also. As of now,

1:50:35

if you see everyone, it is just having very common details like the user is trying to use Google,

1:50:40

user is using Google Chrome, Mac operating system, etc., etc. These are called as user agent,

1:50:46

user details. Okay? But if you try to make this kind of request via after login, then definitely

1:50:53

you will see this request header separately. But Chirap, does that answer your query?

1:50:59

Yes, that's kind of a question.

1:51:00

Correct.

1:51:01

Payload, same as body.

1:51:03

If you are passing any body, you will be able to see the, see that, see that content inside the payload.

1:51:11

And whatever response is coming that you will be able to see in the response tab.

1:51:16

As of now, there is no payload as such because it is a get request.

1:51:19

This is just the payload.

1:51:21

But when you try to make an order, then you might be able to see a lot of data inside the payload

1:51:24

also because a lot of information goes to the back end when you make a post request.

1:51:28

Folks, how many feel clear?

1:51:30

So, like you, as a user, you might not be attaching all of these details manually.

1:51:35

Get, put, post, delete.

1:51:37

That's front end will automatically attach in the request.

1:51:40

Okay?

1:51:41

Folks, clear.

1:51:47

Okay?

1:51:48

So guys, URL we all know.

1:51:51

For example, let's say if I give you an example of URL, this is how a URL looks like.

1:52:00

This is how a URL looks like.

1:52:09

Then method, it can be get, put, patch, post, delete, okay?

1:52:23

Then headers may everyone, you add the authentication details.

1:52:26

How the header typically looks like, everyone?

1:52:29

It is also kind of a JSON.

1:52:30

object. Here, first you have content type. That what type of content you are passing?

1:52:40

Content type. Generally, it is JSON. Generally, it is JSON. And then everyone, you have more

1:52:47

information like authorization, etc. Okay? And body we all know, it is a JSON object for put,

1:52:53

post, request, etc. Is that concrete to all of you? Yeah, application slash JSON.

1:53:00

Is that point clear to all of you? Yes or no? Okay. Now everyone, this is the API

1:53:06

request. Then let's talk about the API response.

1:53:14

Let's talk about the API response. Now, guys, in API response, first you have the status code.

1:53:26

First, you have the status code. Now, for example, everyone, in the Flipcard request,

1:53:30

Did you see the status code as 200? Did you see the status code as 200?

1:53:42

Right? If you go to FlipCart, if you search, go to Inspect Element, search iPhone, go to network tab, see search request, see the headers, you see that status code 200.

1:53:58

200 means green light.

1:54:00

That means okay. It means that you can do that operation. Now if you try to, let's say, if you try to here, let's say, maybe go to this product and then you, let's say, click on buy now. I think it will not even show you by now because you are not logged in here. But still, let's try this.

1:54:25

Yeah. Now let's see if you click on buy now and you see that it is directing you to login.

1:54:30

Okay. And then everyone somewhere, like you try to do this when what happens. For example, let's say if you're trying to make some

1:54:41

operation for which you are not accessible. For example, let's say there is a, there is a, there is a, there is a portal for Masay School,

1:54:49

masai school, masai school.com slash admin where you can add the course, delete a course, create a class, delete a class, right? You can access admin functionalities.

1:54:58

Now, if you try to access that, do you think that you will have the access to that admin portal?

1:55:04

Do I have the access to that admin portal?

1:55:06

Answer is no. Right? So now everyone, for that, you will get the status code as 403.

1:55:11

403 means unauthorized. So for different use cases, everyone, there are different status codes.

1:55:17

For example, for some use cases, you might have seen 404. Page not found. Correct?

1:55:23

404, page not found. Sometimes you might have seen, you might have seen 500.

1:55:28

Internal server error. Have you seen these things? 502, bad gateway.

1:55:34

Correct? It means that for different, different use cases, you have different status codes.

1:55:38

So that your front end can identify whether the request was successful or not successful.

1:55:43

If it was not successful, what was the error code? What was the status code? Why did it say?

1:55:48

Then everyone, API response also can have headers because in the response also, some authentication details might be coming in response also.

1:55:58

When you try to log in for the first time, don't you think when you log in, in the input,

1:56:02

there is no header. There might not be any authentication details. But in the output, in the response,

1:56:07

you might be getting a token. Correct, everyone? So header can be there in the request as well,

1:56:12

in the response as well. And everyone, in the response as well, there can be request,

1:56:17

a response body. There can be body as well in the response also. Is that point clear to all of you?

1:56:28

Now let's talk about everyone, status codes. So these are standard HTTP status codes,

1:56:34

everyone. You don't have to remember them, but let me just show you some of the most common

1:56:40

status codes used over the internet. For example, everyone, 200. 200 status code is used for

1:56:47

for okay. If the request was successful. Request successful.

1:56:58

Everyone, clear? Then everyone, if you are trying to create some resource and that

1:57:04

resource was created successfully, it will give you 201, right? It means that new resource created

1:57:14

successfully. New resource created successfully. Then everyone, you have 4.00. 4.00 means it was bad,

1:57:24

it is bad request.

1:57:28

bad request right then you have 401 unauthorized 500 it is internal server error

1:57:45

right and so on so guys there are a lot of status codes hundreds of status code you

1:57:55

don't have to remember all of them but what you can understand is everyone

1:57:58

that any status code starting with 2, 2x, 200, 2001, etc. This typically means success.

1:58:09

Right? Any status code starting with 4.00, 404, 402, 401. This means there is some client issue.

1:58:21

Clients mistake. For example, everyone, if you try to access, Massey is,

1:58:28

school.com slash ABC. Is that page actually available?

1:58:34

Masaise school.com slash ABC. Is that page actually available? No, that page is not available.

1:58:41

So what will you, what will you get? What error you will get? You will get 404. Page not found.

1:58:48

Correct. Now, whose mistake is this? Is this server mistake or client mistake?

1:58:56

If you're trying to access a page, which?

1:58:58

does not exist. It is your mistake. It is my mistake. So it is client's error.

1:59:03

If you are trying to access massyschool.com slash admin and you get 401 unauthorized. Whose mistake is

1:59:10

this? If you're trying to access a page for which you are not authorized, you don't have access.

1:59:16

You will get an error. That is expected behavior. So 4XX means client's mistake. If there is

1:59:22

some issue on the client side, then it will give you 5XX. Okay?

1:59:28

This is server's mistake.

1:59:33

For example, even sometimes server is not able to process the request, server is down, server is busy, and so on.

1:59:41

Bad request means that, for example, if you don't pass proper input parameters.

1:59:44

For example, let's see if you're trying to make a call to Make My Trip and you are not passing the source to get the flight details.

1:59:51

So Make My Trip can give you the response 4-00, bad request.

1:59:54

That this request is not correct. This is incorrect request.

1:59:58

Make sense? Chirac.

2:0:05

Okay, perfect. Now let's talk about everyone JSON.

2:0:10

Now, how many few are aware of JSON?

2:0:28

JavaScript object notation, right? And it is a lightweight text format. What is JSON? It is a lightweight, because it is easy to read, easy to send over the network from server to client, client to server, etc. It is a lightweight text format.

2:0:58

used to send information structured information between systems over in the network.

2:1:17

Between systems over the network.

2:1:19

That is what JSON simply means, right?

2:1:21

How a JSON looks like, right?

2:1:23

Jason simply looks like, looks like, looks like this.

2:1:26

I wrote it here.

2:1:27

Yeah.

2:1:28

This is how a JSON looks like.

2:1:30

Now, guys, is it easy to read, easy to understand, easy to pass over the network?

2:1:36

Tell me? Yes. So it is

2:1:43

easy to read and easy to parse.

2:1:50

Easy to read and easy to parse.

2:1:52

Right? What is the meaning of parsing, everyone? In this context, what is the meaning of parsing?

2:1:58

Parse means, everyone, let's say if you get this JSON, right?

2:2:04

So guys, JSON is a text format.

2:2:06

Now if you're trying to read the text format in the Python language.

2:2:12

What Python does is everyone, in the Python language, you will have to convert this text

2:2:15

into a Python object, so that everyone, if you want to get the status of the order, you can get

2:2:22

the object that you're creating, let's say orders, order dot status.

2:2:26

Make sense, everyone?

2:2:28

Does that make sense to all of you?

2:2:30

Order dot status.

2:2:32

So parsing means converting an object into JSON or vice versa.

2:2:37

Does it make sense to all of you?

2:2:39

Because languages understands object.

2:2:43

User understands text.

2:2:46

Like you and me, we user understands text.

2:2:50

Python or any language, they understands object.

2:2:53

So guys, what you need to do is if you have an object, if you have this JSON, you can convert

2:2:58

this JSON into an object.

2:3:00

Right?

2:3:02

This is called as parsing.

2:3:04

Once you understand this as an object, can you simply get the date,

2:3:07

order dot get date, order dot ID, order dot status?

2:3:12

So then it will be easier for you to understand and get the user attributes,

2:3:17

individual attributes.

2:3:19

Because at the end of the day, JSON looks like a Python dictionary.

2:3:23

Right?

2:3:24

So if initially it is complete, it is completely coming as a text, so

2:3:28

do you think you'll have to convert that into an object or a dictionary so that you can individually

2:3:33

access these attributes.

2:3:36

You can individually access these attributes, right, everyone?

2:3:41

Right?

2:3:42

So in Python, it is very, very extremely simple to work with JSON, right?

2:3:51

Because in Python, everyone, there is a module called as JSON.

2:3:54

So what do you do?

2:3:55

You simply do import JSON.

2:3:57

Okay? You simply do import JSON.

2:4:02

And everyone, this module, JSON module gives you lot of functionalities.

2:4:07

Out of these two functionalities, everyone, it gives you two major functionalities.

2:4:12

One is JSON dot loads, right?

2:4:20

And JSON dot dumps.

2:4:25

I will show you this in code as well, everyone.

2:4:26

code as well, everyone.

2:4:28

Okay?

2:4:29

So what this JSON.

2:4:30

Dot loads does, is everyone, it decodes.

2:4:35

It decodes JSON string because everyone, JSON is a string or text format.

2:4:41

If you see, if you notice, it is a text.

2:4:43

That is, it is a string format.

2:4:45

So this complete string, you need to convert into object.

2:4:48

So you need to decode this string.

2:4:50

So JSON.

2:4:52

So JSON.

2:4:53

It decodes, decodes, decode JSON string.

2:4:56

and JSON dumps.

2:5:01

It encodes it encodes

2:5:06

It encodes

2:5:09

Python object into JSON strings.

2:5:13

So if you see everyone, it is straightforward.

2:5:23

What load function does?

2:5:25

It converts.

2:5:26

into Python object, okay?

2:5:29

And dumps converts Python object into JSON.

2:5:33

Is that point clear to all of you?

2:5:36

Is that point clear to all of you?

2:5:40

Is that point clear to all of you?

2:5:43

Okay.

2:5:44

Now, guys, what do you say?

2:5:46

In JSON also, you have different data types, string, integer,

2:5:50

bullion, list, dictionary, etc.

2:5:53

Let me show that to you.

2:5:55

So instead of writing this complete,

2:5:56

I can copy paste this screenshot.

2:5:59

Yeah.

2:6:00

If you see everyone, these

2:6:13

data types in JSON, right?

2:6:15

So this is string data type.

2:6:17

This is integer, double, bullion, null, list, right?

2:6:23

This is another dictionary, city, country, etc.

2:6:25

country, etc.

2:6:26

So all of these data types are just like integer, string, bullion, double, etc.

2:6:31

All of these data types are also supported in JSON.

2:6:35

Makes sense, everyone?

2:6:40

Make sense?

2:6:41

Okay.

2:6:41

Now let's talk about everyone parsing.

2:6:54

you have been given a JSON string and you need to convert converting JSON string into Python object.

2:7:18

Okay.

2:7:19

So I think let me show you this in the code.

2:7:24

This we do via this function JSON loads.

2:7:32

Let me directly show you this in the code.

2:7:54

This is our right.

2:8:06

The code I have already added in the nodes, so nothing to worry.

2:8:11

So what I can do everyone, I will just simply show you this demo.

2:8:14

So what you can do everyone is you can import this JSON module, import JSON.

2:8:19

And this, after importing this JSON module, for example, let's say you have this JSON string.

2:8:24

Okay?

2:8:25

And let me copy paste this JSON string even.

2:8:28

And assume that this JSON string we have got as a response from some API, right?

2:8:34

So if you see this is a JSON string, let's say as it is we have got this response, where the

2:8:39

order ID is there, the customer details are there, whose order is this, items in the order,

2:8:45

and status is placed.

2:8:47

Is the JSON response making sense to all of you?

2:8:50

Is the JSON making sense to all of you?

2:8:52

Simple right?

2:8:53

It is JSON text.

2:8:54

JSON string. Now everyone, what you can do is we can convert this JSON string, convert

2:9:02

this JSON string into a Python dictionary. Now for example, everyone, if I ask you that

2:9:07

from the above dictionary, give me the name of the product, laptop and mouse. Can you easily

2:9:17

do that? If this is a string, this is a string, can you easily give me the price of laptop?

2:9:24

of the mouse or the status or the email of the customer. Can you easily give me that?

2:9:29

No. We cannot give that, we cannot do that directly. But what do you can do everyone? You

2:9:34

can simply do order, let's say some order object is equal to JSON. Dot loads. Use this

2:9:41

loads function and load this JSON string in the Python dictionary. And then if you want what

2:9:48

you can do, now you can do order dot, let's say, print order ID.

2:9:54

Then I will show you other details also.

2:9:58

Order.

2:9:58

Order ID.

2:9:59

Sorry, order ID.

2:10:02

Now because this is a dictionary, you can access like this.

2:10:05

Now go to terminal and execute Python 3, first class.

2:10:11

And you will say that order ID 101.

2:10:14

Now even if you see, let's say, okay, give me the order.

2:10:18

First, give me the customer, if I want to see the customer, if I want to see the customer email ID, first

2:10:24

go to the customer, inside customer go to give me the email. And now you will see that the email

2:10:28

of the customer. Now let's say if I ask you that give me the items and item may give me the

2:10:35

first item. Okay? Items. Because in items, everyone, you see that? Items is a list. And tell

2:10:44

me the 0th item. Tell me the name of 0th item. Do you see that? Do you see that? Do you see that?

2:10:54

Now it is a dictionary. Now you can easily iterate over every value. It is laptop.

2:10:59

This is the meaning of loads function. Is that point clear to all of you? It is a meaning of loads function.

2:11:09

It is a meaning of loads function. How many if you are able to understand this? I have added

2:11:13

the code in the code, complete code in the nodes. Okay? No worries. So you can go through that.

2:11:19

Okay? Then everyone, the second topic is.

2:11:24

You can also stringify a JSON. What is the meaning of stringify? Let's see.

2:11:28

Stringy find JSON in Python. Now what is the meaning of this? It is the opposite.

2:11:40

So guys, loads or parsing, what we have done in parsing? Parsing means converting JSON

2:11:45

string into Python object or Python dictionary. Here it is the opposite. Converting Python object

2:11:50

or Python dictionary into JSON.

2:11:57

Converting Python dictionary

2:11:58

into JSON.

2:12:05

Makes sense, everyone?

2:12:09

For this, we have a function called as a JSON.

2:12:12

Dumps.

2:12:17

JSON.

2:12:19

Is that point clear to all of you?

2:12:20

Right? Now, for example, again, if you want to see the demo for that, very, very simple.

2:12:29

Comment it out. Let's say, sorry, why it did not comment out?

2:12:39

Let's say you have some order. And order is a type of JSON where you have, let's say, order ID.

2:12:47

It is an order ID 101. Right? Let's say it is an order ID 101. Right. Let's say it is.

2:12:50

product ID. Product ID, maybe let's say 1000. Okay? Product name is let's say iPhone.

2:13:08

Price of the product is let's say, okay? Something like this. Does it make sense to all of you?

2:13:20

Cannot assign literal here. Maybe you meant, you meant this.

2:13:26

Oh, sorry, guys, you will have to give the column, right?

2:13:34

Because it is a dictionary, right? It is a key value pair.

2:13:38

Makes sense, if you want? And now what do? You do, you do.

2:13:41

JSON data is equal to JSON. Dot dumps. Jason dot, yeah, dumps. And this JSON data.

2:13:50

What is the name of this? Order. Order. And then you print JSON data. And then you execute it. Now you are getting in the form of JSON. This is the type of JSON. Now if you try to print the type of JSON data, it will show you it is a type of string. String means like JSON is also a type of string. Does that make sense to all of you?

2:14:20

Folks, yes or no?

2:14:26

Now, everyone, tell me, in the previous classes, I think in the, what do you say, in the vector search class, in the Rack class, have we worked on the real open AI project?

2:14:45

Real Open AI API.

2:14:50

For example, let's say if I show you e-commerce rag, okay, this is what we have built or vector search or e-commerce rag, right?

2:15:04

In this everyone, if you see, if you have to work on any open AI, what do you do? You install open AI, create an open AI client, and then finally you make a call via open AI client.

2:15:20

responses. Create. So this is an API call. This is, if you see, call LLM. So this is how we make

2:15:27

a call to open AI API. Does it make sense to all of you? And for that, everyone, you would need the

2:15:33

API key. For that, API key, you need to set in the environment variable. Does it make sense to all

2:15:40

of you? Okay. So folks, this is what we wanted to discuss about the API.

2:15:50

I think we have covered a broad category of concepts. Now, how to call Open AI API or Gemini API.

2:15:58

For example, let's say we have already seen how to call open AI APIs in the past.

2:16:03

Install open AI, get the API key, set the API key, create the client, make a call, get the response, and use the response.

2:16:11

This is typically the flow. Now tell me everyone, if in future you want to use Gemini instead of opening it.

2:16:18

Definitely the way is going to be different. For that, you know,

2:16:20

you will have to probably search on the Gemini documentation or just go to GPT or any LLM and just ask them,

2:16:27

I want to use Gemini in my project.

2:16:29

Please give me a simple way to call Gemini APIs via Python code.

2:16:33

It will give you the entire process.

2:16:35

Again, the process will be similar.

2:16:37

Just the name of the functionality is can be different.

2:16:40

You will have to create an account, get the API key, put some balance, set the API key, create the client, make an API call, get the response, etc.

2:16:50

Does it make sense to all of you? Everyone clear?

2:16:55

So how many of you understood all the concepts from today's class?

2:17:02

Now, folks, we have a quiz. Do you want to have the quiz? Let's have the quiz. Just maybe two, three minutes of time it will take, maybe five minutes of time.

2:17:13

Okay, so let's have a quiz, everyone. So let's go to, let me have, let me open the quiz.

2:17:20

Okay, where is a quiz link for me, where is a quiz link for today?

2:17:50

Yes, there is.

2:17:55

Okay, so I think evaluating and improving RAC system, the name is wrong, right?

2:18:00

So you're not finding it in this field.

2:18:03

No, no, I got it, got it.

2:18:05

I think the name of the lecture was wrong.

2:18:07

So folks, can you join the link of the quiz?

2:18:10

Can you join the quiz link?

2:18:11

So either you can scan the QR code or you can join via this link.

2:18:20

Folks, please join. I think at least 30, 35 people should join the link.

2:18:50

on 30 people being start okay so let's start okay so let's start everyone uh so here we go the first question

2:19:13

how the number have the numbers reduced since the module one evaluation you mean the number of

2:19:19

of people in the class?

2:19:24

Some answer is like some number has reduced. Answer is like typically some drop happens after

2:19:30

every module generally. Okay, what is the main responsibility of database? It happens in every course.

2:19:39

I think by the end of the module, by the end of the course, only like the people who are very

2:19:45

serious, they stay, but some people drop in between.

2:19:49

What is the main responsibility of database layer?

2:19:53

Very simple, everyone, storing and managing data.

2:20:06

Second question.

2:20:19

For such simple questions, how may we can have like 20 seconds of time going forward.

2:20:28

Okay, Keta, very good.

2:20:32

Third question.

2:20:42

Create a new resource.

2:20:48

Very good. All of you have voted. It is post.

2:21:01

Fourth question, I think we are going very fast today. People are answering it very fast.

2:21:10

Which status code usually means new resource was created successfully?

2:21:17

It is 201.

2:21:25

It is 201.

2:21:27

It is 2.0.2 is successful.

2:21:29

But when you are talking about a new resource created successfully, it is 201.

2:21:33

I wrote it in the notes as well.

2:21:39

See.

2:21:41

Correct, everyone, 201.

2:21:45

Okay?

2:21:47

Here we go, the last question of the class.

2:21:51

500 internal server error usually means.

2:22:17

There is some error on the server side. What you don't know?

2:22:23

Right?

2:22:24

Some error happened while server was processing the request, right?

2:22:27

Server failed while processing the request.

2:22:29

Great.

2:22:30

So, let's see everyone, the final leaderboard.

2:22:33

I think Renzhen is at the top.

2:22:37

Very good.

2:22:39

Then Chimmey, Mettle, Ashley, Casper and then Sankhate.

2:22:44

Okay.

2:22:45

Great.

2:22:46

Thank you everyone.

2:22:47

I hope all of you enjoyed the class.

2:22:49

Now I'm launching the feedback poll.

2:22:51

Please take the feedback pool.

2:22:52

And once you take the feedback poll,

2:22:54

please feel free to drop off.

2:22:56

We are done with the class.

2:22:57

Thank you.

2:22:58

Have a good day.

2:22:59

Good night.

2:23:00

Take care.

2:23:01

And see you all on Wednesday now.

2:23:02

Thank you.

2:23:03

Thank you, everyone.

2:23:04

Take care.

2:23:05

Bye.

2:23:06

Have a great night.

2:23:07

Have a great day.

2:23:17

Okay, done. Thank you everyone. Bye-bye.