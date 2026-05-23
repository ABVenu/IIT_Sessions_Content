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

Hi, everyone.

12:09

Hi, everyone.

12:36

for the session.

12:38

Yeah, we'll start in a couple of moments

12:40

when we read at this job.

12:42

So you can start with the V-WOL.

12:44

By welcome.

13:06

Thank you.

13:36

Thank you.

14:06

Thank you.

14:36

Thank you.

15:06

Thank you.

15:36

Hi,

15:43

Thank you.

15:44

Thank you.

16:06

very good evening, folks. Am I audible to all of you?

16:09

Hi, everyone.

16:12

Am I audible?

16:13

OK, great.

16:16

Good evening, everyone.

16:17

And welcome to the class.

16:19

I think this is the last class of your module, right?

16:23

Of second module.

16:25

Correct.

16:27

From the next class, the new module will start.

16:30

And the new topics will be LangChain, Langraph.

16:34

We will be starting with the agent.

16:36

into key frameworks from the next module, correct?

16:40

Okay, great.

16:42

So folks, let's get started.

16:44

And in today's class, we will be talking about tool integration in AI agents.

16:52

What do we mean by tools in AI agents?

16:57

What do we mean by tools in AI agent?

17:02

When you make a call to some external

17:05

entity to get some work done, right? For example, let's say if you are a travel agent,

17:12

you might have to make a call to make my trip. You might have to make a call to Expedia.

17:16

If you have to schedule a meeting, you might have to make a call to Outlook, right?

17:24

You might have to connect with database also. Database is also going to act like an external tool.

17:30

You might have to call Weather API to get the latest weather information for a particular city.

17:35

Right? So when your AI agent, when your agent makes a call to some third party, to some external or internal, right? So this party can be external or internal. Internal means like, for example, it can be your own database also. So database is not part of your third party. Database is also part of your application, right? But it is a separate entity altogether. So database is also considered as a tool. Okay? So now everyone, when agent makes a call to any third party,

18:05

Maybe let's say, Make My Trip, Expedia, or even database.

18:09

How that interaction is going to happen?

18:11

How that communication is going to happen?

18:17

That communication is going to happen via APIs.

18:22

Correct?

18:24

That communication is going to happen via APIs.

18:29

I think there is some issue with my pencil.

18:33

Correct?

18:34

And, guys,

18:35

API is we have discussed in the previous class.

18:37

API stands for application programming interface.

18:43

Application.

18:48

Programming interface.

18:51

So, folks, let's have a quick recap of few things which we are going to use in today's class.

18:58

For example, APIs, a bit of JSON structure, a bit of HTTP methods, right?

19:04

So what?

19:05

What is an API, everyone? Let's talk about what is an API?

19:11

API is a contract between two parties which will help them to communicate with each other. Can we say

19:18

that? It is a contract between two parties that allows the software systems to communicate

19:24

with each other, correct? So API, you can say that. It is a contract.

19:35

Between two software systems, between two software systems that helps or that allows them to

20:05

communicate with each other.

20:11

That allows them to communicate with each other.

20:18

Is that pointly to all of you? Yes or no?

20:23

Folks, yes or no?

20:28

Okay. And then everyone we discussed about the request response cycle.

20:35

What is request response cycle, everyone?

20:42

What is request response cycle?

20:50

Did we discuss this request response cycle in the previous class?

21:05

Okay, we did not formally define it, but I'm sure that you know that already.

21:09

But let's formally define that.

21:11

Now everyone can I said any two software systems which are interacting over the network, over the

21:16

internet, can us say that one of them is going to act like a client?

21:24

One of them is going to act like a client?

21:28

Yes and no?

21:30

And one of them is going to act like a server.

21:33

So any.

21:35

typical communication that happens over the network that is called as client server

21:40

architecture because one entity is going to be there who is going to act like a client and client

21:45

is the one everyone who initiates the request who makes the request who needs some information

21:50

who needs the data who needs to who wants to make some operation some execution so that is what

21:56

client is the client is the component which makes a request so client makes a request to the

22:04

Okay?

22:05

Client makes a request to the server.

22:07

Now what server will do?

22:10

Server, once server gets the request, server processes the request, correct, everyone?

22:16

So if you remember, I think we discussed this, that front end makes a request, front end the

22:20

request goes to the backend, back end processes the request and then back end gives the

22:24

response back, right?

22:27

Backend processes the request and then back end will give the response back.

22:31

So this is request and response.

22:34

cycle.

22:35

This is request and we are getting the response back.

22:44

Is that pointly to all of you?

22:46

So client is making a request to the server.

22:48

Server processes the request and server gives the response back to the client.

22:52

This complete cycle is called as request response cycle.

22:57

Does that make sense to all of you?

22:58

Yes or no?

23:02

Does it make sense to all of you?

23:03

Yes or no?

23:04

Right?

23:05

Now everyone, this client and server, I hope you understand this idea that this client

23:11

and server, these terms are relative terms.

23:13

For example, everyone, in one communication, for example, in this request response cycle, this entity

23:19

is acting like a client, this entity is acting like a server.

23:23

But everyone, do you think that this server might also need some data from some external party, for

23:28

example?

23:29

Let's say this.

23:30

See, at the end of the day, what is client, what is server, they are nothing but machines.

23:34

So technically they are machines only, but logically you are calling them client or a server.

23:39

Client is the one who needs the data, server is the one who will process the request and gives

23:43

the data back, gives the response back.

23:45

Now everyone, can this machine, which is acting like a server in this communication, is it possible

23:51

that this server might act like a client in some other communication?

23:56

Is it possible?

23:57

Is it possible?

23:59

Absolutely yes.

24:03

So for example, if this server makes a request to let's say maybe weather API, let's say,

24:12

make my trip, right?

24:14

It is making a call to let's say make my trip.

24:16

So don't you think everyone in this communication, this server, like this machine, which was acting

24:21

like a server in the previous communication, this is going to act like a client because it is

24:26

a one who is going to initiate the request.

24:29

So this will initiate the request.

24:31

Now this will process the request.

24:33

and it will give you the response back.

24:36

Does that make sense to all of you?

24:37

It will give you the response back.

24:39

Everyone clear?

24:40

Right?

24:41

So you will get the response back.

24:42

So guys, these terms, client and server, these are, these depends on the situation.

24:48

Absolutely correct.

24:49

So client and server, these are relative terms according to the situation, absolutely correct.

24:53

Maybe, let me give you an example, right?

24:56

I will strictly go in the details of the backend development.

24:59

I hope it will make sense.

25:01

For example, even when you.

25:03

when you try to place an order at Amazon, right?

25:05

Do you think that the entire Amazon backend is one code base?

25:10

It is very interesting.

25:12

Do you think that the entire code base of Amazon is just one single piece of code?

25:16

One single code base?

25:18

Absolutely not.

25:19

So guys, you can assume that Amazon's back end is such a big application, right?

25:24

So it cannot be one single code base.

25:27

Right?

25:27

So at least there are like 20, 30, 50 different microservices.

25:31

These are called as microservices.

25:33

When you divide the codebase into small, small components.

25:36

But as per the, at the scale of Amazon, these are not technically small components, right?

25:40

They are itself in, they are itself pretty big.

25:43

Because if you see that, Amazon has a lot of things internally.

25:47

Amazon has order functionality, everything related to order, placing an order, canceling an order,

25:52

deleting an order, tracking an order, updating the order, etc., etc.

25:55

Then related to products, there are a lot of products.

25:58

You can add a product, you can delete a product, you can update the product, you can update the product,

26:01

you can maybe change the product details and whatnot.

26:05

Then everyone, there is a payment ecosystem, right?

26:07

Payment is itself a complete, bigger system altogether.

26:11

Then there is a notification system, right?

26:14

Then there is an inventory system to maintain the inventory.

26:17

Then there is a, let's say, a tracking system which will track the products which are in transit,

26:23

placed orders.

26:24

So all of you understand, then these components are handled by millions of software engineers across the world.

26:30

So, do you think that it is feasible, it is technically feasible for millions of people

26:36

across the world.

26:37

They are working on a single code base and they can work so efficiently.

26:42

The entire application can work efficiently for millions of people in the world at a time.

26:49

Do you think so?

26:50

Absolutely not.

26:51

It is not technically possible.

26:53

So what Amazon has done is, Amazon has created small, small code bases, different

26:58

different code bases.

26:59

So what they have done is, they, they, they, have done is they, they,

27:00

there is a order component which will take care of order service, everything related to order.

27:05

Then there is a, let's say, a product service, which will take care of all the things related to product.

27:10

Then there is an inventory service which will take care of inventory.

27:13

Then there is a delivery service which will take care of the delivery of products.

27:16

Then there is a notification service, there is a payment service, etc.

27:19

Make sense, everyone?

27:20

Are you guys getting some basic idea about this?

27:23

That entire Amazon's codebase is divided into small, small components, individual components,

27:28

so that you can handle them easily, right?

27:31

So now everyone, when you're trying to place an order, when you go to Amazon.com, and when you click on buy now,

27:36

right, you go to the orders page, correct?

27:39

From the products page, you are going to order's page.

27:41

So I'm just giving you a very basic understanding about this.

27:45

So let's say, everyone, internally, when you click on buy now, can I say that everyone, when you

27:50

click on place order, can I say that the front end must be making a call to order service

27:55

to place the order because the placement of order.

27:58

This functionality is present inside order service, correct or not?

28:04

This functionality is definitely present inside order service.

28:06

Correct or not, everyone?

28:09

Right?

28:09

So the call, the API call should go to order service.

28:12

Then everyone, to place an order, what do you need?

28:16

Can I say that, to complete the order, you need to first make the payment.

28:20

So can I say that everyone, once you click on buy now, once you click on buy now, you go to order space

28:25

and then finally you go to like, after that you go to go to,

28:28

the payments page, correct?

28:30

So you are making a call to order service, but order service internally makes a call to

28:34

payment service to initiate the payment, right?

28:40

Now, guys, don't you think in this communication, order service is acting like a client for payment

28:46

service?

28:48

Authentically, like there will be a lot of other things also, Sandhya, there will be hundreds of other

28:52

things.

28:52

I'm just giving a very, very basic example.

28:55

So guys, in this communication, all of you agree.

28:58

that order service is acting like a client for payment service or not.

29:04

So it is acting like a client and now payment service is acting like a server.

29:11

Correct? Because order service makes a request to get some data to do some operation of payment,

29:16

payment service will process the request. But everyone, generally what happens, for payment,

29:22

you need to make a call to, like every company does not implement payment gateway on their own.

29:27

They have.

29:28

have to make a call to third party payment gateway, like Razor Pay, phone pay, PayPal, etc.

29:33

So Canvas 3rd. This payment service will make a call to third party service, third party API,

29:40

third party gateway, which is Razor Pay. So payment service will make a call to Razor Pay. Tell me yes or

29:47

know if you want? It will make a call to Razor Pay. Now everyone tell me, in this communication,

29:55

client is order service, server is payment service.

29:58

service. But what about in this communication? When payment service is making a call to

30:02

razor pay, payment service is acting like a client or a server. Payment service is acting like a client or a server.

30:12

Absolutely yes, it is acting like a client here. Okay. So now you can see that here it is acting

30:18

like a client. Okay? You can say that here it is acting like a client. Here it is acting like a server.

30:24

And in this communication everyone, it is acting like a client.

30:28

And Razor Pay is acting like a server which will serve the request.

30:33

So server is what?

30:34

Who is server?

30:35

Server is the machine which will serve your request.

30:38

When you make a request, that machine will get your request.

30:41

It will identify what kind of request is it, what processing we need to do, what operation we need to perform, what data we need to return.

30:48

That is what a server is.

30:50

Now when Razor Pay will get the request, Razor Pay will serve Amazon's Payment Service's request.

30:55

It will initiate the payment, it will complete the payment.

30:57

the payment and then it will give you the it will give the response back.

31:01

Is that point cleared all of you?

31:03

And once the payment service gets the response back, then payment service will give, we'll

31:07

give the response back to the order service.

31:10

This is typical flow of client and server.

31:15

Is everyone clear with two things here.

31:18

Client server architecture and request response cycle.

31:23

And client and server, these are relative terms, okay?

31:27

The only thing that you need to understand is, then that you need to remember is,

31:30

client is the one who initiates the request, server is the one who serves the request.

31:35

So this is.

31:57

Okay, let's move to the next thing now.

32:02

Okay, just one quick recap.

32:05

So guys, we are just having a few recaps and then we will finally make a call to like the tools for today's class.

32:12

Okay, can we call payment service?

32:14

Actually not.

32:16

It is not really a middleware.

32:18

Because middlewares are the parts which are technically not doing anything, right?

32:24

Technically you don't do a lot of processing in the middleware.

32:26

But here.

32:27

if you see payment service is itself a component, okay?

32:31

It is itself a component.

32:32

So it is not just acting like a middleware.

32:34

Rather, it is using razor pay as a tool to get the work done.

32:39

Okay, middle wares are the parts which are not doing a lot of work on their side.

32:43

They are just acting like a middle component.

32:46

But here payment service is a real component.

32:49

Okay.

32:50

Yeah.

32:52

Now everyone, what are the different type of H2TP methods we have seen in the

32:56

we have seen in the previous class, we have seen in the previous class, post, put or patch,

33:22

patch and then we saw delete. So these are the methods that we have seen. So

33:35

what is get about? Get is about reading the data, fetching the resource. It is a fetch

33:41

operation. Post is creating the resource, generating something. Put or patches update.

33:51

is partial update when you would just want to update few parameters, few arguments,

33:56

put this kind of a replacement when you want to replace a complete object altogether. And then everyone

34:01

you have delete, delete is delete. Delete is very straightforward. It is delete only.

34:07

Okay. Now everyone, if I give you, let's say, two APIs. Can you tell me the difference

34:14

between them? Let's say if there is an API get slash orders. And there is another,

34:21

another API, get slash orders slash ID 123. Could you tell me what do you think,

34:31

what difference could be there between these two APIs? What difference could be there

34:39

between these two APIs? Absolutely. So guys, now again, is it a, what do you see,

34:48

is it a standard thing that, okay, if you make a request, get,

34:51

request to slash orders, it will always give you all the orders. No, it ultimately

34:56

depends on the implementation. But if I tell you the general behavior, it will give you fetch,

35:01

it will fetch all the orders. This is the general behavior we are talking about. Fetch all

35:08

the orders or fetch the order with ID 123. Fetch the order with ID 1, 2, 3. Fetch the order with

35:21

ID is equal to 1, 2, 3. Is that point cleared all of you? This is the general behavior that we have discussed.

35:30

Okay? Okay. Then everyone, we talked about HTTP status codes.

35:44

H2TP status codes. For example, let me ask you, what about 200 everyone?

35:51

1. First, tell me about 200. 200 is, request is okay, successful. What about

35:59

201? Okay, request successful?

36:08

2001. 201 means also everyone, but 201 generally return when you create a new resource.

36:21

For example, if you're trying to place an order, an order was created successfully, then you

36:26

will return 201. New resource created successfully.

36:38

Okay? Then everyone, let's say you have 404 or 401.

36:45

First, tell me 404, not found. If you're trying to access some resource, which is not available,

36:51

you will get 404 not found, page not found or resource not found. Then 401, unauthorized.

37:02

Okay, 502, 501, bad gateway, 502, internal server error and so on. So guys, you know, you don't have to

37:09

remember all of them, but generally, if you walk on them multiple times, you will remember these

37:15

few status codes which are very, very frequently used, but you can remember this.

37:21

particular table. This is very easy to understand, easy to remember also, that there are

37:27

majorly three categories of status codes. Majorly, there are three categories only. So category

37:35

wise, it will be relatively easier for you to learn to remember. So first category is 2XX, that is

37:51

200, 201, etc. 4xx, 400, 401, 402, 403, 404, etc. And then 5XX, 501, 501,

38:00

500, etc. So, guys, 200 status code, we return when request is successful. There is no error.

38:09

Okay? Now there can be different type of success. That's why you can define 2.00, 201, and so on.

38:15

4.00, everyone, when there is a client error, when user is making some mistake, and because of

38:21

their mistake, right, because of their mistake, some error is coming. For example, let's say

38:27

everyone, if you are not passing correct credentials, then it is your problem. It is my problem

38:32

if I'm not trying to, if I'm not able to log in to my account. It is not server's problem,

38:37

right? Then it will give me, let's say, 401, unauthorized. If I'm trying to access some page,

38:41

which is not available, I will get 404, right? It is my problem that I am trying to access some page

38:46

which is not created by the company. Similarly, 5XX.

38:51

This is server's mistake. If server has made some mistake, server has, server is not able to process the request,

38:58

server is not able to understand the request, server is down, internal server error, bad request, and whatnot.

39:05

Is that point clear to all of you? Yes or no.

39:12

Okay? Then everyone, we discussed JSON. Now, this why we are discussing this again. Because everyone, don't you think the tool is one of the most

39:21

important thing that you are going to use for AI agent. Because if you don't integrate any

39:25

tool with your AI agent, your AI agent, like what operation they will do. To perform any operation,

39:31

you will have to perform, you will have to integrate a tool. It can be make my trip, it can be

39:36

a weather API, it can be database, it can be any API. So guys, if you have to integrate a tool

39:43

with your AI application, with your agent, you need to make a call, you need to call them via.

39:49

you need to call them via API. And if you are working with APIs, everyone, you need to

39:54

understand which method to call. Should we make a call to get method, post method, put, patch or

40:00

delete. This thing, we need to understand. Then everyone, once you get the response from the, from the

40:06

party, from the third party, then what response you are getting? How do you interpret the response?

40:12

If, let's say, for example, if it is giving you 404, it means that you are trying to make a wrong

40:17

API call, that API does not exist. If you're trying to, if you make a request and then you

40:22

get, let's say, 401, it means that you are not, your API key might be wrong. Right? Your login

40:28

credentials are not correct. You have not logged in successful. Right. And everyone now, in what

40:33

format do we generally send the data over the network? In what format do we generally send the data over

40:40

the network? In the form of JSON. And what is JSON, everyone?

40:47

JSON is JavaScript object notation.

40:51

Okay? JavaScript object notation.

41:06

So it is the most common data format used between the APIs between the software systems for communication.

41:17

In most common data format, format used for communication, most common data format used for communication between,

41:47

software systems. It can be agents, it can be any software system.

41:53

Okay? And it is nothing but it is very, very similar to Python dictionary.

41:59

Correct? What is ID? What is, let's say, name of the student, name of the user?

42:05

Just comma separated values, right? Age, right? And whatnot. Is that one key to all of you?

42:15

Is everyone clear? Okay. Now everyone let's talk about the actual API call, right? The actual agent tool call. Now, this agent tool call is also treated as a function call. Okay? It is also called as function calling in AI agents.

42:42

Function calling in AI agents.

42:45

Now, what exactly is function calling in AI agents? Now, what you can do is everyone? For example, let's say, to your agent, you define multiple tools which are available.

42:55

For example, let's say, Make My Trip is available, database is available, right?

42:59

Whether API is available, calculator is available, and let's say database is available and so on. Let's say you define a list of all the tools which are available in your system.

43:08

Then what your agent should do?

43:11

Don't you think your agent should be able to decide this autonomously, that which, which,

43:15

tool should it make a call to? Should it make a call to database? Should it make a call to

43:20

make my trip? Should it make a call to this? Should it make a call to that? Make sense everyone?

43:25

This type of tool calling is called as function calling. So what do you do everyone? Function

43:31

calling simply means that that AI model, right? AI model, you give AI model a list of available tools or

43:38

functions and allowing the agent or allowing the AI tool to decide which tool they want to use. They

43:45

want to call. Does that make sense for all of you? So function calling, let me write the

43:50

definition. This means, or we can say that, function calling means, giving an AI

44:15

model, a list of available tools or functions. So guys, here we are using these

44:32

terms interchangeably, tools or functions, right? Function calling means giving an AI model, a list of

44:38

available tools or functions and allowing them and allowing it to decide which tool to call.

45:08

Make sense?

45:13

Now tell me everyone, here we are seeing that AI model.

45:16

Now, AI model will decide which tool to call.

45:20

Because everyone, at the end of the day, what is the brain of your application?

45:24

When we say that agent will do this, agent will do that.

45:27

But who is getting the work done from the agent?

45:30

Who will guide the agent that, okay, what needs to be done?

45:34

Can you tell me?

45:34

Who will guide the agent what needs to be done?

45:38

It is the model. Model means large language model. That is the actual brain of any

45:51

AI application. But do you think that everyone, the AI model itself will directly make a call

45:56

to the tool? Make my database, whatever, right? Do you think so? That AI model will make a call

46:02

to the tool? Actually not. AI model does not make a direct call to the tool. Rather, what

46:08

does. It just gives the response. It just decides that is a brain. Brain will just

46:14

decide what to do. Now your body will take the action. Similarly, agent will take the action.

46:19

Right? What agent does? Agent will give the prompt to the LLM tool that okay, this is what we want

46:25

to do. And these are the available tools that we have. Then based on the prompt, it will take, it will

46:30

decide it. It will apply the brain, the model. And model will give that, okay, this particular information

46:35

is, this is how it should come. And then you can.

46:38

probably make a call to this thing. You can call to this is the idea. Now you can make a call

46:43

to make my trip to book the tickets. Or you can make a call to whether I pay to check the weather.

46:48

Is that point clear to all of you? The model only says, please make a call to this tool and get the work

46:55

done. Okay? So for example, let's say everyone, if you're building an agentic AI

47:03

application or let's say a complete agent application, which will have the connection, which will have the

47:08

activity of a weather API. Let's say maybe assume that it is as good as, it is as simple as

47:14

chart GPD. Let's say you have a chart GPD and chart GPD is a very basic application, let's say,

47:19

and you ask that what is the current weather of Delhi? Now, obviously, the LLM will not have this

47:25

information because LLMs have the cutoff date. So LLM might have a cutoff date of, let's say,

47:29

two to three months old. So LLM obviously does not know what is the current weather in Delhi. So what

47:35

LLM will do? LLM will decide what I can.

47:38

do based on the query that, okay, I don't have an answer for that. Either you can configure

47:42

the LLM in such a way that it can simply give the prompt that, okay, I don't know the answer.

47:46

Right? But what LLM will do? LLM will decide what to do. So LLM will give the task, so you

47:52

have written an agent, right? So agent will get the output from the LLM, that okay, LLM will decide

47:57

that okay, I don't have this data, but please make a call to whether API, get the data and return

48:02

like, then we will return to the user. So what agent will do? Agent will make a call to whether

48:07

API, get the data, give the data to the LLM, and then LLM will re-formulate the answer

48:13

that you can directly return to the user. The LLM will have to generate the answer in a user-friendly

48:18

way, in a presentable way. Does that make sense to all of you? Okay, so folks, this is a typical flow

48:27

of a function calling. Okay? Let me just copy paste this. So there are like a lot of steps here.

48:34

So instead of writing them, I can directly copy-paste it. First, everyone, you take two minutes

48:41

of time and read about it. Okay? First, you have to read and then we'll discuss. Have a look at it.

49:02

just take two minutes of time and let me know once you understand it once you go through this

49:06

just tell me yes or no in the chat once you complete it just read these nine steps

49:32

Thank you.

50:02

Okay, Neserk.

50:32

Done. I have got reply from three people. What about other people?

50:38

Folks, please go through this.

50:40

Okay, a lot of people.

50:44

Okay, a lot of people have done.

50:56

What if?

50:57

What if external tools have authentications? Okay, we'll talk about it.

51:01

Okay.

51:02

In fact, not what if. External tools will have authentication multiple times, almost every time, right? Until or unless, like you are building a very simple application that might not need authentication, but most of the time you would need authentication. If you are booking a ticket, if you are booking a hotel, if you are sending an email, if you are scheduling a meeting, right? So these things will have authentication. We'll talk about it. Okay. A lot of people have gone through

51:32

read every one. Now let's try to understand one by one. So I will also read all the steps one by one and then I will keep on explaining every step. So first thing is you give a question. Let's say, for example, what is the weather of Bangalore or what is the current weather of Delhi? Then AI model will check, the LLM will check that. Does it have that information? If yes, automatically it will not make a tool call and it will return it. It will generate the answer. It will and it will return the answer. If not, model selects a tool.

52:02

So model might have a list of tools which you have already created and which you have already given the access to the tool.

52:08

So the LLM, model already knows what all the tools do, does it have the access to?

52:16

Right? So then model generates a structured argument for that tool.

52:21

Now, for example, everyone, weather is a very simple thing, right? For whether, what do you need? You need the time, current time, let's say, and the city name. That's it.

52:29

But assume that, let's say, you have to make a tool.

52:32

you have to make a tool call to make my trip.

52:34

And you want to check the flights from Delhi to Bangalore, from place A to place B, for a certain date, and let's say maybe for two adults, for three adults, etc.

52:43

For two people, three people and whatnot.

52:45

Now, everyone, model generates to, like, based on the prompt, based on the user's query, model will generate the arguments, the input parameters for the tool.

52:55

What input parameters do you need to pass to the tool?

52:58

Now, everyone, model will generate the arguments.

53:01

But if you see that, in the step number five, we have written that, application validates the argument, right?

53:07

For example, everyone, if you're even making a call to make my trip to check the flight from place A to

53:13

place B for a certain date. But let's say everyone, somehow, the user has not passed or let's say model

53:19

missed, because ultimately everyone, LLM can also make mistakes. Can LLM makes mistake?

53:26

Yes, user can make a mistake? Obviously yes. What if everyone, the source is not.

53:31

given or the date is not given in the argument or the destination is not given.

53:36

Then even if you make a API call to the Make My Trip, will you be able to get the desired output?

53:42

Will you be able to get the desired output?

53:44

Will you be able to get the desired output? Obviously not. So that's why everyone, it's very important

53:47

for the application. Application means, what is the meaning of application here?

53:51

Application needs the agent or the Python code that you are going to write.

53:55

In the code, before making a tool call, we should validate whether the tool, whether the tool, whether

54:01

arguments are as expected or not? Are you guys getting this point?

54:06

Neserk? That why application needs to validate the arguments?

54:11

What if, let's say, you're checking the weather of, you want to check the weather of

54:14

Bangalore, but what if, let's say, the city itself is missing? And now, what if city itself is

54:20

missing? How will you validate it? Right? So that's why. Then I want step number six,

54:25

application executes the actual Python function API or like you might have to execute the function,

54:30

you might have to make the API call, do that. And then tool returns the response. And when we

54:38

say returns the response, returns data, in what format we will receive the data? How do we give the

54:44

model ability to tell if it needs a tool? How does it generate the arguments needed? See,

54:50

arguments will be generated based on the prompt and sometimes, like for example, let's say if you're

54:55

using large language models, they are, they have been trained on.

55:00

humongous amount of data. So they all, they can understand the natural language.

55:06

Right? So if, first of all, first of all, if you ask a query to them, they would, they would be able

55:14

to understand that whether do they have the answer for that or not? Okay, do they have the required

55:19

information or not? If yes, they will generate. If not, then they will go to the tool, the list of tools.

55:25

Now, which tool to call? For every tool, you have some description, that use this tool to

55:30

to make a call to let's say make my trip, make a call to make my trip when you want to check

55:34

some flights data, make a call to weather API to check the weather data, and so on. Now based

55:39

on that, they will make a, they will decide which tool to call. Make sense sure. And also can

55:45

the model have ever the ability to know it needs a new tool. It can recommend you, right? Maybe

55:51

based on if your tool, if your LLM is smart enough, if your LLM is advanced enough, then it can tell

55:57

you that okay, maybe out of four defined tools, I could not.

56:00

find the best, I could not find the tool for this particular use it so that I'm trying to,

56:05

I'm now calling the best tool available. I'm recommending the best tool available, but it might

56:10

not be 100% true. Okay, but yes, LLM can be smart in the future as well so that it can decide,

56:17

it can also tell you that, okay, we don't have a proper tool for this particular use this. Absolutely.

56:22

So you see, the root of every AI application is LLM. If your LLM is not smart enough, almost all of you

56:29

decisions are going to be wrong. Because LLM is the brain, if your brain is not giving you

56:35

the right decision to make, right? Then you see, agents just follow LLM. Agents will just do what

56:42

LLM will ask them to do. If LLM is not smart enough, then I don't think so. Like you will be able

56:48

to, like we will be able to build a good agentic AI application. Makes sense? Will agents,

56:55

true data, which was returning from tool every time, agents will not store.

56:59

if you want to store the data from the like it depends what kind of data is there if you need to store you can have a database right for every tool or whatever data you are getting from the tool if it is required to store then you can have a separate database for that okay so tool returns the data in the form of jason right then application sends the tool result back to the model model will generate the answer based on the context right and then we will return the context then we will generate then we will return the generated

57:29

answer to the final user. This is the complete step. How many of you are 100% clear with this?

57:36

This is the complete flow of any agentic AI application when you want to make a tool call.

57:46

Okay? Okay. Okay. I think also everyone in the notes, I have given like a couple of more examples. You can go through that. How many if you go through notes,

57:59

on a regular basis. What is the flow if a model, if a model, if model, if model, if model,

58:05

if model, first of all, model does not use a tool. Model, first of all, model does not use

58:11

a tool. It can be model, it can be other model also, right? It can be some tool. It can be model. Model

58:18

It can be model. Model does not make a call to the tool directly. If you see, model just tells you

58:22

what tool to call. Okay, Vishfana? Then agent makes a call to the tool.

58:29

Make sense? See, even after live classes, even after like for the revision I'm talking about.

58:38

So once your class is over, right? So for example, to revise the class, to revise the content, how many

58:45

if you go through the notes on a regular basis? I do, very good. When I need to revise the class,

58:53

I use notes because it is easier to read, then to sit for two hours again. Very good, that's correct.

58:59

Again, everyone, I think I have emphasized that multiple times, please do go through the notes,

59:05

not exactly, like, you can go through the class notes also. They are also pretty good in terms of depth,

59:10

but also you can go through the typed notes, right? For every class, you get the typed notes, right?

59:16

On your LN, on your, what do you say? LMS, sorry. On your LMS, right, on your dashboard, you get the typed notes.

59:25

Please go through those notes. Those are pretty detailed notes. And I add a lot of

59:29

examples in those notes, right? Those examples I take from multiple sources. Sometimes I generate

59:35

from GPT also, then I try to refine it. Sometimes I get it from educative. Sometimes I try to get it from

59:42

different websites. So these are the nodes which I curate from different sources. Okay. So these are not

59:48

just simple AI generated notes. Okay. So I have multiple paid subscriptions. For example,

59:54

I have paid subscription for educative and other platforms. So I do get the content from

59:59

these different sources, then I curate those notes. So if you are going through those notes,

1:0:04

you can essentially say that, that you have gone through different resources for one particular

1:0:10

section, for one particular topic. Okay? You can do that, definitely. Okay, what Ehmr has done?

1:0:25

Okay, you have downloaded all the notes. Is that this, is that what?

1:0:29

you're saying? Okay, Hammer has created one Google sheet in which he has taken

1:0:40

the, he has mentioned the PDF. All of you can also do that. Maybe it will take half an hour,

1:0:46

sit over the weekend, download all the notes, give proper names, right? Maybe if these class names

1:0:51

are not very much relatable, give whatever names do you think are the best for that particular class,

1:0:56

create a sheet. Maybe I think there will be like, as of now, how many classes we have done?

1:0:59

around 30, 35 classes. Just keep on creating that sheet. And by the end of the module,

1:1:04

you will see that all the PDFs you will have downloaded in your laptop with the links, with proper links.

1:1:11

Okay. Those notes are not present on GitHub. On GitHub, I upload the handwritten notes.

1:1:18

Okay, Vishwanah. On GitHub, I upload the handwritten notes in the class, the notes that we write in the class.

1:1:25

If you're cool with sharing Google sheet, then please do. That is not my sheet. That is Amher's

1:1:29

Emmer's sheet. Emmer Tariq. Okay? I have not created any such sheet. Okay, okay. So now

1:1:39

everyone, we can move to the next thing. Now, folks, what we are going to do is, we are also going to learn

1:1:44

about establishing a connection of our AI application with database. Okay? So, for example,

1:1:51

everyone, this is your AI application, essentially your Python application. This is your application layer.

1:1:59

This is your application layer. And you want to connect this application layer

1:2:09

with, you want to connect this application layer with database. Now everyone tell me, should we connect

1:2:17

this application layer with database manually? Should we establish this connection manually?

1:2:21

First of all, can we do that? Yes, we can do that. But should we do that? But should we do that?

1:2:29

Answerism. Because everyone, if you connect this manually, right, without using any library,

1:2:38

without using any functionality, it will be very slow, it will be time consuming, etc. So that's

1:2:43

everyone, there is a concept of database drivers. Okay? So database drivers, these are the drivers or these are the

1:2:50

drivers or these are the, you can say that, the libraries or the, or the functionalities, which

1:2:56

helps you to connect with database faster. Right. Or database drivers.

1:2:59

driver, it acts like a connector that allows your application to connect with database and

1:3:05

it will be slightly faster. So there is a concept of database drivers. Then everyone, there

1:3:10

is a concept of ORM, right? I think I remember we have talked about ORM. Yes or no. I think

1:3:19

we have talked about ORM, right? What is the ORM meaning everyone? ORM stands for object,

1:3:29

relational mapping. Right? So guys, ORM libraries can easily help you to map your

1:3:38

Python classes with relations. Relation means table. So for example, let's say you have a class user,

1:3:45

right? You have a class user in your Python code. And you were saying that every user will

1:3:49

have ID, every user will have name, every user will have age, every user will have college,

1:3:55

every user will have marks and so on. And you have defined data type also for these

1:4:02

attributes. Now everyone tell me, if you want to store these user details for every user, right?

1:4:09

Definitely in your organization, you might have thousands of users. Will you create a separate

1:4:15

user entity for each user? And you need to store them? So can I say that everyone? This

1:4:21

user class, you may want to convert that.

1:4:25

into a database table. That somehow, if I can get a user table in the database and every

1:4:32

user will have these entities, these attributes, ID attribute, name attribute, name attribute, age, college,

1:4:48

and marks. If somehow we can do this everyone, will our life be sorted.

1:4:55

So that we assume that we don't have to create this table from scratch manually.

1:5:01

If someone can give us this table automatically, magically, that I have this class in my Python

1:5:08

code, okay? I have this class in my Python code and I want a corresponding table in the database.

1:5:14

So name of the table can be anything, name of the, for example, let's say as simple as that name

1:5:19

of the table is also going to be similar as name of the class. And all the attributes of the class will

1:5:24

become all the columns of the table. If you can achieve that, will it, is it going to

1:5:29

help, is it going to save us a lot of time, a lot of efforts? For example, everyone, in bigger systems,

1:5:36

in bigger applications, you might have thousands of classes and you might have to create those

1:5:41

thousands of tables from scratch in the database. But everyone, ORM helps you to do this

1:5:47

automatically. ORM maps. If you see the definition of ORM, it helps you. It helps you.

1:5:54

you to map your object. Object means object you create a what? You create an object of a class.

1:6:01

So ORM helps you to map class into relations. Relations are of, relations are also called

1:6:09

as tables in the relational databases. So ORM library helps you to map your classes into tables

1:6:15

automatically. And I will show you this thing. Does it make sense to all of you?

1:6:24

Okay? Now everyone, SQL alchemy, I will come to SQL Alchemy. Sequel Alchemy, SQL

1:6:34

Alchemy is not only ORM. SQL Alchemy gives you other functionalities also. So you can use

1:6:39

SQL Alchemy with ORM without ORM. Okay. Now coming to that point only, eventually I will

1:6:45

give you the idea for that also. Now everyone, if you are, let's say, if I tell you that,

1:6:50

okay, you have to write some queries to create a table, to delete a table, to

1:6:54

create some resource, basically to any, to perform any operation, right? To create something,

1:6:59

to update something, to get something, right? Because everyone in real systems, you might have

1:7:03

to, when you want to get some data, when you want to fetch some data, would you always want

1:7:09

to fetch data from a single table? Would you always want to fetch the data from a single table?

1:7:16

Not really, you might have to, you might want to fetch the data from multiple tables, right? Those

1:7:20

are called as join operations. Now tell me everyone, from your Python application.

1:7:24

application, if you perform SQL queries, if you perform SQL queries, if you perform SQL queries, if you perform SQL queries, if you are writing them manually and you are making a query to database, and these queries, you are writing

1:7:52

manually. You are writing manually. What do you think? Is that a good approach? If you're

1:7:59

writing SQL queries manually, like select star, from, table, where ID is equal to this, join with this,

1:8:06

group by, etc., etc. First of all, can we do that? Can we write SQL queries directly in

1:8:13

Python and execute them? Can we do that? Answer is yes, we can do that? We can write SQL queries

1:8:21

manually. But everyone, in fact, people used to do that. For example, we have talked

1:8:26

about in the previous classes, in the last model, we have talked about SQL alchemy. So SQL

1:8:30

alchemy, what is SQL alchemy? It is a library, it is a framework, which helps you to, which

1:8:36

helps you to connect with databases easily. It gives you the support of database drivers automatically.

1:8:43

It gives you the support of ORM. Also, it can help you to write queries automatically. You just

1:8:48

have to tell that what you want to do. Right?

1:8:51

and it will give you the functions that you can call and internally it will convert those functions

1:8:56

into the corresponding query. Because everyone, first of all, if you're writing SQL queries manually,

1:9:01

it is time-consuming effort, it will take a lot of time. Also, along with that, it can be prone to errors

1:9:07

also. Because everyone, if you're doing a lot of, if you're writing a lot of queries manually, it can

1:9:12

also lead to some mistakes. You might make some mistakes, correct or not?

1:9:21

yes or no, it might, you might end up making some mistake. And that's why we will

1:9:25

use SQL alchemy. Okay? That's why we will use SQL alchemy. I will talk about SQL alchemy

1:9:32

a bit more, that what exactly is SQL alchemy. And along with that everyone, SQL alchemy also

1:9:38

helps us with the support of ORM. Internally, by default, it comes up with the support of ORM

1:9:44

also. It means that you can use SQL alchemy to write SQL queries automatically, to connect

1:9:50

with database easily, right, to establish your connection easily, as well as you can help,

1:9:55

you can take help from SQL Alchemy to get the support of ORM. For example, now you want to

1:10:00

convert your table, you want to convert your class into table automatically. It can do that

1:10:05

on your behalf. Now, let's take a break. And after the break, everyone, we will be writing a lot

1:10:11

of code. We will just be having probably 10 to 15 minutes of discussion around SQL Alchemy,

1:10:15

and then for almost one hour, we will be writing the code. Makes us almost 45 minutes, we will

1:10:20

we will spend on coding. Correct? Okay. Link of the nodes. Link of what? Link of the nodes? These notes.

1:10:50

So these are the notes for the class as of now. So it's 903 everyone. Let's take a break of around

1:10:56

12 to 13 minutes. Let's meet around 916, 917. Okay? Let's meet after the break and then

1:11:20

Thank you.

1:11:50

Thank you.

1:12:20

Thank you.

1:12:50

Thank you.

1:13:20

Thank you.

1:13:50

Thank you.

1:14:20

Thank you.

1:14:50

Thank you.

1:15:20

Thank you

1:15:50

Thank you

1:16:20

Thank you

1:16:50

Thank you

1:17:20

Thank you

1:17:50

Thank you

1:18:20

Thank you

1:18:50

Thank you

1:24:50

Hi

1:24:54

Hi

1:24:58

Hi,

1:25:00

Hi, everyone

1:25:01

Hi,

1:25:02

everyone.

1:25:03

Okay.

1:25:04

Okay.

1:25:05

So now, everyone, uh,

1:25:22

while, while, uh, while using, while using, uh, while using, while using,

1:25:23

using the input parameters from, let's say, LLM will generate the arguments,

1:25:30

and then before sending it to the tool, any tool, we will have to validate it. Okay? For example,

1:25:37

if something is present, something is not present, something is integer, something is string, something

1:25:42

is bullion, etc. One thing is we can do that manually. If type of this is equal to string, if type of this is equal

1:25:48

to string, if type of this is equal to is equal to bullion, if this is empty, if this is not empty,

1:25:52

We can do that manually also. But what is a better way? If you do that manually, it is going to take a lot of time, a lot of if else conditions are going to be there.

1:26:01

But have we learned any library which can help us to validate objects easily?

1:26:08

Pidentic. Remember that? So I will also show you some examples of

1:26:16

Piedentic today. Okay? Why Pencil is not working? Yeah, Piedentic as well. Okay.

1:26:22

So Pidentic is a Python library which is used for data validation and for multiple use cases, right?

1:26:29

I hope all of you remember Piedentic, right?

1:26:31

So using Piedentic, you can make something mandatory, something optional, you can set the default value, right?

1:26:39

You can check the data type, you can define the data type.

1:26:41

If it is string, the value should be string.

1:26:44

If it is mandatory, the value should be available.

1:26:46

Otherwise, it will raise some value error.

1:26:49

Okay? Perfect.

1:26:50

Then if you want the next thing, that.

1:26:52

we're going to talk about is all of these details have already added in the notes again just

1:26:57

for your reference. And in detail, we have already talked about in the previous classes, right?

1:27:05

Now let's talk about SQL alchemy. And then we will start with coding part.

1:27:16

Okay. What do you understand by the term SQL alchemy? What do you think SQL alchemy?

1:27:22

alchemy is about?

1:27:28

SQL alchemy is database?

1:27:29

Okay?

1:27:30

What about other people?

1:27:35

Is SQL alchemy a database?

1:27:37

A database?

1:27:38

No, not at all.

1:27:49

SQL alchemy is not a database. It is a library.

1:27:51

SQL alchemy is a Python library.

1:28:06

SQL alchemy is a Python library that helps us to interact with database.

1:28:19

that helps us to interact with database. Does it make sense to all of you?

1:28:32

Okay, so there are two major styles of SQL alchemy. Basically, you can use SQL alchemy in two ways.

1:28:38

One is SQL alchemy core.

1:28:49

Sorry.

1:28:50

This is, there are two ways in which you can use SQL Alchemy.

1:28:57

One is SQL Alchemy core and SQL Alchemy ORM.

1:29:00

Okay.

1:29:01

Now I think everyone SQL Alchemy core we have used in the previous classes, correct?

1:29:09

I remember that we have used SQL Alchemy core, right?

1:29:12

That's why I will give you the example of ORM, right?

1:29:14

Core, what is the difference between Core and ORM is that in the ORM, if you see that

1:29:19

If you're using SQL Alchemy ORM, then SQL Alchemy can automatically convert your tables,

1:29:25

your classes into tables, right? It can map the classes and tables together. It will be very easy

1:29:29

for you. But everyone, if you're using SQL Alchemy code, then you'll have to write the tables on your own.

1:29:34

If you want, I can show you the previous code as well. I think I remember correctly. If I remember

1:29:41

correctly, I think we have done this. Okay. What was our name of the project? I think we do

1:29:49

we did that in Pythintic demo Python classes.

1:29:57

I don't remember the name of the...

1:30:03

I don't remember the name of the project actually, but I remember I did that.

1:30:11

Okay, I'll find it out on GitHub. It will be easier. Okay.

1:30:15

Now everyone, anyways, SQL Alchemy ORM is the more frequently used one.

1:30:19

So we will be using that particular idea today.

1:30:23

Okay. So ORM means database.

1:30:49

sorry, Python class into database table. This is the correct idea.

1:30:59

Okay, Python class into database table. Okay? And attributes will be the class. Class

1:31:07

will be mapped to the database table.

1:31:14

Okay. Now I think we can get started and we can write some.

1:31:19

code to check. Okay. And now everyone, in this, we will also be calling the tools.

1:31:25

We will be connecting with database. So this is going to be kind of a full-fledged application.

1:31:30

Okay. This is kind of getting a, creating a full-fledged application. So we can open some project.

1:31:36

We can use, let's say, the rag one, or we can create a new project actually. The new project

1:31:42

could be name as agent, tool call.

1:31:49

agent tool call. Or what we can do is instead of this, we can go to, okay, let's create

1:32:00

a new project. Okay, agent tool call. And inside this everyone, we will create a new file called

1:32:05

as, let's say, app.py, application.py. And inside this, everyone, let's go to terminal. We will

1:32:12

have to install all the libraries. So after installing this, first of all, we will have to create a virtual

1:32:17

environment, right? So it is Python.

1:32:19

H.m. M. V-E-NV. V-E-NV. Sorry, Python 3. Okay. And now, activate it. Okay. Activate the virtual environment. And once it does it,

1:32:41

everyone, we will install the libraries. And what all the libraries do we want? We want to install PIP3, install, PIDEN-TIC.

1:32:49

P.I.3 installed SQL alchemy.

1:33:19

Do we need to install a separate ORM as well? Do we?

1:33:26

Yeah, we would need open AI 3.

1:33:49

But is it a part of SQL Alchemy only? I'm just taking that. Orm needs to be installed. No.

1:33:59

ORM is a part of SQL Alchemy only. Perfect. Then everyone, we are done. And let's get started with

1:34:03

the coding part now. Okay? So with the coding part, first of all, let's start writing the class,

1:34:09

the base class. You remember that from Pidentic, we will, we were importing base model from Piedentic

1:34:14

import base model. Remember that? Right? And then we will create the first step is create the

1:34:23

first step is create the first step is create the SQL alchemy base class. Okay. So class base base base.

1:34:44

SQL alchemy, import, create engine, select. These are the things that we need.

1:34:57

And everyone, if you want any class to be taken by ORM, you need to import from SQLalchemy.

1:35:02

. . We need to import declarative base class. Okay. And other things I will show you

1:35:14

So first you need the base class and this is coming from declarative base. And this is just a placeholder even. You don't do anything inside this base class. Okay. And then everyone you create the second step is product class. Okay. So this class we are going to create a table for that right in the database. So what we will do? Class product. This is getting extended from declarative base class or base class only because base class is coming from declarative base class. And here everyone,

1:35:44

you define all the attributes. So first everyone, you define the table name also. That, for example,

1:35:50

everyone, that what should be the table name of this class when ORM will create the table for this

1:35:56

automatically? Because now you are using ORM, right? Now you are using ORM. So ORM will create a table for this.

1:36:02

How you want to create a table? What name do you want to give? Let's say we want to give the name of

1:36:07

the table as products. Make sense, everyone?

1:36:12

Make sense everyone. And then.

1:36:14

everyone you define ID, what all the parameters do you have? Then everyone along with ID,

1:36:19

you need to define the data type of ID, right? That what data type do you need of this attribute? And along

1:36:28

with that also, for that you need the mapped attribute. Map. That what is the data type of this?

1:36:35

That you write in map, that this is an integer value. Now everyone can is that, okay, this is integer in the

1:36:42

Python code. But can us that now, you can apply some properties, some constraints,

1:36:47

like primary key, foreign key, auto increment, null, not null, etc. Inside the database,

1:36:54

that is everyone you can define via mapped column. So you can import one more thing, which is mapped column.

1:37:01

And with the mapped column, if you want to define some properties for this column, you can do that. For

1:37:05

example, is this a primary key? Yes. Okay. ID is a primary key. Then is this auto increment, let's say true.

1:37:12

Is this auto increment true? Then you can define other parameters like maybe nullable, right?

1:37:17

Is equal to true or false? Unique is equal to true or false. Does that make sense for all of you?

1:37:22

So if you want to apply some properties on any attribute, you can give via mapped column. Okay. And then everyone,

1:37:28

every product will have, let's say, name, product will have, sorry, it will have comma.

1:37:34

Every product will have, why it is not coming.

1:37:40

Name. Name. Name will have.

1:37:42

Mab, string. Then it will have, let's say, product will have category.

1:37:51

Category will also be string.

1:37:59

Okay? And let's say product will have, let's say, price also.

1:38:03

Price. Price is going to be, let's say, integer. And it will have, let's say, in-stock,

1:38:08

whether this product is actually available or not. So it will be bullion.

1:38:11

Mabbed and bullion. Is the class making sense to all of you? Is the class making sense to all of you?

1:38:19

Is the class making sense to all of you? Okay. Okay. Now everyone, when you want to search

1:38:28

some product, okay, that I actually, I will show you that later on. Okay. That I will show you later on

1:38:33

also for the search operation. Okay. So they are coming from Pidentic. Fine. Now, everyone, let's

1:38:40

try to create an engine. We will try to connect with database. Create engine. So what do we

1:38:45

want? We want a simple database, an in-memory database to be created in the same folder. So what we

1:38:50

will do? We will simply use a SQLite. I think, if you remember, we have used that already.

1:38:54

SQLite, colon, slash, slash, and then you can give any name of the database. For example,

1:39:01

let's say e-commerce.d.b. Okay, e-commerce.dd.d. That's it. Does it make sense to all of you?

1:39:07

Okay. And you can give, let's say, echo is equal to false. Echo is equal to false. It is an optional

1:39:13

parameter. It just simply means that whether whatever queries, whatever data you want to, you will insert,

1:39:20

do you want any output in the terminal? Do you want to print anything in the terminal or not? Why we are

1:39:26

giving echo is equal to false? If you give echo is equal to true, there will be a lot of print statements.

1:39:32

But it is completely optional. I think by default, it is true. Even if you keep it true, it is okay.

1:39:37

Okay. So this is create engine. Everyone clear? This is how you connect with database.

1:39:44

So what it does everyone? It will try to find out a database with this name in the current folder.

1:39:49

If it is able to find good enough. If not, it will connect, it will create an engine. It will create a database and then it will establish the connection of our Python application with this database with this engine.

1:40:01

And everyone now, with this engine, we will connect with database and then we will perform the operations.

1:40:07

Make sense, everyone?

1:40:13

Okay? Now, folks, as of now we have established the connection and now to connect with database

1:40:20

and to create all the tables, what we will do? We will simply use this operation called as

1:40:25

the base class gives you a function, gives you an attribute called metadata, and it gives you a function

1:40:31

called create all. What this create all function does is that in this all the classes which

1:40:36

are coming from the base class.

1:40:37

see, we have created a base class. This class is coming from declarative base and

1:40:42

this product class is coming from base class. So what it does everyone is that go to all the

1:40:47

metadata of the base class and create all the tables which are coming from the base class automatically

1:40:53

on this engine, on this connection. So for example now, as of now we have only one table,

1:40:58

one class which is product class. So it will create a table for this particular class on this

1:41:03

connection, that is on this database. Does it make sense to all of you?

1:41:07

Okay? And now everyone, what we will do is we will insert some sample data in database.

1:41:20

Okay? Insert some sample data in the database. So for that, everyone, we will have to establish a session. So we will import the session.

1:41:29

And after importing the session, what we're going to do is it is a lot of code. Maybe let's write it all.

1:41:37

Okay, let's not copy paste. So first we will define the function. Let's say insert data,

1:41:46

insert data into database. And what we will do, we will establish the connection with session.

1:41:51

A session means everyone, you are starting a new session with the database. You are establishing a

1:41:55

session with the database, which database, which is present at this engine. With, like, if you see

1:42:01

everyone, like with means just open a session with this engine and just give a name to the

1:42:07

let's say session. So you can establish the database. You can, you have established a connection with the engine and you can access that connection via this session. Okay. And what we will do? First, you will check what all the products are there. Okay. Maybe what you can do? You can check if already products are there or not. If not, then you can insert the products. Make sense? Or you can directly create some products. Okay.

1:42:37

You can directly create a list of products. And everyone, instead of writing that data, I can copy paste this data like this.

1:42:48

Okay, just a second. Let me copy the complete list. And if you see, this data is nothing but like this. So it is a list of how many products? Like six products.

1:42:58

Product name is this. Product name is this. Category is mobile. Price is this. Stock is true.

1:43:03

Is this sample data making sense to all of you?

1:43:07

Right? Is this sample data making sense for all of you? And guys, this session gives you a function

1:43:13

called as add all. If you want to add one product, you can use add function. If you want to add multiple

1:43:18

products, you can use add all function. And add all function mean you can pass the list of products.

1:43:23

So what it will do, everyone? It will automatically iterate through the complete list and it will keep on

1:43:28

adding all the products to the session. And finally everyone, whenever you are making any right

1:43:32

changes, you need to commit those changes. Right. You need to commit those changes. And after these,

1:43:36

And after these few lines of code, everyone, you will be able to insert these six products in the database table.

1:43:45

Is everyone clear?

1:43:51

Is everyone clear?

1:43:57

Okay. And now everyone, we will write a function to search.

1:44:00

Define search product. Let's say search product. To search product, everyone, you can, you can,

1:44:06

search based on multiple things. For example, let's say, generally the search is not

1:44:11

going to be as simple as, let's say, just give me the product with this name, right? Just

1:44:16

give me the product with this description. When you perform a search on e-commerce website,

1:44:22

that can be quite a complex search, right? For example, you are giving some description also.

1:44:26

You are giving the price limit also, right? That give me, show me the mobile phones, but only the

1:44:31

mobile phones which can be, which are in stock, which are the price, the price,

1:44:36

between 70,000 to 80,000 and whatnot, correct? So you can pass multiple parameters in

1:44:41

the search criteria, correct or not? So you can make multiple, you can pass multiple search

1:44:47

criteria. So that's why everyone, we are taking input data in the input parameter, let's say

1:44:53

input data. This should be a dictionary. Okay, this should be a dictionary. Why this should be a dictionary

1:44:59

because you can pass multiple parameters, right? Maybe something like this.

1:45:06

Let's say input data is like this. For example, let's say a product name is matching

1:45:12

with, let's say, mobile phone. Or let's say category is mobile phone. Category is mobile.

1:45:21

Category is mobile. And then let's say maybe in stock is true. You don't show me the products

1:45:30

which are not available. Okay? And then let's say starting price.

1:45:36

70,000. Ending price. Are you guys getting this point? So that's why we are taking

1:45:50

a dictionary. Okay? That's why we are taking a dictionary. And everyone now in the output also,

1:45:56

it can return a list or it can also return a dictionary. Okay? In the output also, because output will

1:46:02

be a list of products or it can be a dictionary of products.

1:46:06

Is that point clear to all of you?

1:46:10

Now everyone, whatever input is coming, should we validate this input?

1:46:15

And everyone, this is one comment that I can add.

1:46:17

So yes, I'm referring the code that I've written in the notes.

1:46:19

So you can also refer that.

1:46:22

So if you see, this is the tool, this is the function call.

1:46:25

You can say that tool or function call that an AI agent can call.

1:46:32

Okay.

1:46:33

Yes, we can do that.

1:46:36

It depends on that what kind of input we are defining Vishwanat, what kind of input parameters

1:46:41

we are defining, we can do that. But if you see that between 70k to 80K, like how will you validate

1:46:47

it, whether the user is passing in the correct way or not? But if you are passing in this way,

1:46:52

then you will be able to validate it. How? I will show you that. Okay. And what is going to be the

1:46:56

flow? Receive dictionary in the input from the agent. Now we need to validate using Pidentic.

1:47:02

Are you guys getting this point? We should validate this object via Pidentic.

1:47:06

Why we should validate it? Because everyone, there should be maybe, there might be some

1:47:11

parameters which are mandatory to search, correct? Input validation, some things might

1:47:17

be mandatory, some things might be optional. Okay? So what you can do, you can create a

1:47:21

pidentic class, a base model class, and you can give the name of the class as something like

1:47:26

this, product, search, input. If you need an input to search the product, you can create an object

1:47:34

like this so that you can validate it automatically. And this is coming from base model.

1:47:39

Okay. And what it should contain? It should contain, let's say, category. Okay, it should contain

1:47:44

category, which is of type string. And everyone now you can define more properties around it. Let's

1:47:48

a field you can import from Pidentic, you can import field. Right? It should not be mandatory. It should not

1:47:59

be optional. It is a mandatory field. Also, you can define, let's say, maximum length is equal to one.

1:48:03

It means that it should not be an empty string. What if, let's say, you pass category is

1:48:10

equal to just like this, right? Just to pass the mandatory filter. Then everyone, let's say

1:48:17

max price. You say that, okay, I want the products to be present always less than 1,000. Right.

1:48:24

So you can say that, okay, max price is integer and is it mandatory? Answer is yes. And also everyone

1:48:29

you can define parameters like it should be greater than zero. Right? It's, it's, it's, it's,

1:48:33

like the price cannot be lessens you, right? And everyone only show me in stock.

1:48:39

Only in stock, right? And it is a bullion and it is by default too. It means that even now

1:48:46

if you see, we are making this attribute as optional. Sounds good, everyone. So you can create a very

1:48:52

basic product search input base model, a bi-identic filter, by dintic class, so that you can validate

1:48:58

it. And everyone now, whatever input you are getting, you can now validate it, validated input,

1:49:03

okay, by converting them into this type, right? And now, if you remember, you must have

1:49:11

discussed, we must have discussed this thing. Unpacking. So what we are doing, everyone? We have

1:49:17

a dictionary and what we are doing? Convert this dictionary into an object of this type. If there

1:49:23

is any error, if there is any validation error, the code will fail here. If there is no validation

1:49:27

error, then we will get a validated input object of this type. Remember that?

1:49:33

an unpacking. Two star means unpacking. Converting a dictionary into a

1:49:39

pyrintic model. Folks, yes or no?

1:49:42

No. Okay. Now everyone, can there be a error here? Can there be an exception here?

1:49:56

Tell me, can there be an exception? Yes. This line can throw an exception? What if you are

1:50:02

not passing something in the right way, right? So we should use try catch, okay? Because we need

1:50:07

to handle the exceptions, right? Try and here we will use accept and accept what type of error. It will,

1:50:13

it will return validation and error, right? I think validation error. Do we need to import it? Yeah, I think.

1:50:32

validation error as error. Okay. And here you can write, let's say you can pin,

1:50:40

you can give some message. Let's say maybe you can return an object like this. Let's say,

1:50:46

is the response success? No. False. Success is not. All right. What error we are getting?

1:50:54

Error is, let's say, invalid, input provided. Okay? And if you want more details,

1:51:07

then you can provide error. This error object will have details. Dot details. Dot details.

1:51:12

Dot errors. It will show you the errors. Does it make sense to all of you? So you can return

1:51:17

like this so that user will understand that what input, what wrong thing they have provided.

1:51:22

Okay? And now everyone, if you can, if you know, if you can, if you can, you can, if you can,

1:51:24

this is correct. Okay, comma here. If this is correct, everyone. If the accept block does not execute,

1:51:32

if the input was correct, then now what we will do? Now can I say that? Make a call to database. Make a

1:51:40

call to database and search for the product. Search the database. Search the database. Search to the table.

1:51:50

Correct everyone. Again, everyone, we will have to create a session with a

1:51:54

session on this engine as session. And we will write a query like this. Query is

1:52:01

equal to, query is equal to select from product, select from product class, dot where.

1:52:12

Select star from product where. Now you have to add the condition. Where, product dot category

1:52:17

is equal to validated input. Dot category. Correct or not?

1:52:22

product dot price, because you are passing the max price, right, product dot price,

1:52:29

should be less than read equal to validated input dot max price. Are you guys getting this point

1:52:35

or not? Fokes, yes or no. Why there is a error here?

1:52:45

Sorry, double equal to, right? Equal to this, less than equal to this. Also,

1:52:50

you can, if you want to add any other filter, you can,

1:52:52

do that. But I hope this makes sense to all of you. I hope this makes sense to all of you.

1:53:03

And then everyone, because if you see stock price, stock is also coming right, in stock. So, but everyone,

1:53:09

if you see in stock is a, in stock is a, what do you see, is a optional parameter, right? It is a bullion

1:53:18

and it is optional. So, can you say that?

1:53:22

of product dot in stock is equal to validated input dot in stock or only in stock. Can you do

1:53:34

that? That if this is null, if this is not there, it will take the true value, right? If you provide

1:53:41

it, it will take that value, else it will take true value, right? Is that point clear to all of you? So

1:53:47

the query is done. Okay. And everyone now, what we will do?

1:53:52

we will execute this query and then we will get products from db is equal to session dot execute

1:54:00

session dot there is a different functionism session dot scalers execute this query and all give me

1:54:08

all the results right because it can give you multiple results. So scalers is the function that

1:54:13

we that you need to execute in order to execute the query and whatever input you are getting

1:54:19

get me or whatever output you are getting, if you use

1:54:22

all, it will give you all the products that you are getting from the search query. Is that point clear to all of you?

1:54:33

Okay. And what we can do everyone? We can return these products from DB. We can return

1:54:42

these products from DB. Folks, is that point clear to all of you?

1:54:52

Now what we're going to do everyone is we will write this complete flow in one shot.

1:55:03

So let's say we find complete agent flow or let's say let's say let's call it as agent flow. What

1:55:11

agent does generally do? So agent for we will have a user message or let's say a user query,

1:55:17

right, agent will get some user query in the input which is of type string. Okay.

1:55:22

and what we what we will do is now everyone can I say that here we can create a client object

1:55:31

which is of open AI do you already know that how to make a client how to make an open AI call

1:55:36

so can we just simulate the function call as of now

1:55:41

method return type which return type of which method

1:55:52

this thing it will just print maybe no need to return anything it will just print it okay

1:56:00

here also everyone uh what you will get return okay there is one problem actually uh if you see

1:56:07

uh in this search product method we have defined the return type as dictionary but everyone

1:56:12

i think i remember correctly if i remember correctly their products from db you get in the

1:56:18

list format so ideally what you should do is don't you think this list of

1:56:22

you should try to convert it into dictionary of products.

1:56:26

Huh?

1:56:27

Maybe and that's why problem because I'm not sure about what is going to be the data, what is going to be the data,

1:56:33

what is going to be the data type of this response.

1:56:36

Let's remove the data type.

1:56:38

Okay, we'll see what data type is coming here.

1:56:41

And whatever it is, it is okay.

1:56:43

So whenever you are not sure about the return type, you can skip it.

1:56:46

And once you're sure, you can write it.

1:56:50

Make sense, everyone.

1:56:53

So now everyone, what we can do is we can define a tool call like this.

1:56:59

Tool call like this.

1:57:02

And this is something that we give inside the application, inside the AI application.

1:57:06

For example, first you define the tool name.

1:57:09

Tool name is, let's say, search products tool.

1:57:15

And guys, now this search products tool, actually, you can give this name, search product tool.

1:57:19

product rule. So yes, can database also act like a tool? Does database also acts like a tool?

1:57:25

Yes? I'll have to check that. Why do you think it will be a list of dictionary?

1:57:35

List of dictionary. If you see that, okay, every product is going to be a dictionary. That's correct.

1:57:39

It should be. It should be. Okay. So that's why if you have to change it, so it should be a list and then list of dictionary.

1:57:47

But anyways, even if you don't write it.

1:57:49

the return type, it is okay. Okay. So let's change the name of the function and we will give the same name here.

1:57:55

So this is the tool name. Okay, database can also be act, can also act like a tool. So this is also tool.

1:58:01

For this tool, everyone, what arguments do you need? What arguments do you need for this tool? We need category.

1:58:13

For example, let's say category is we are passing some sample input mobile and let's say max price.

1:58:19

is, let's say, 50,000. And let's say, only have, only in stock, only include this.

1:58:30

And this is, let's say, true. Does it make sense to all of you? Let's say everyone, this is the

1:58:35

tool call that you are, that you are encapsulating, that you are writing. And using this, using this

1:58:43

JSON, we will try to make a tool call. Okay. And now what we will do everyone is, let's say,

1:58:47

we will have the tool result or tool output. Now, guess, in reality, in real applications,

1:58:55

you will have multiple tools inside the tool call. Okay, if you see as of now, there is only

1:59:03

one here. But in reality, what you will have, this tool calls will be a list. Okay, and here you

1:59:09

will have multiple tools defined like this. So for example, as of now, you just have one tool,

1:59:17

here. Okay. And then there can be another tool. For example, let's say there can be a tool

1:59:25

for Make My Trip. Okay. Then there can be a tool for Expedia. There can be a tool for Weather

1:59:31

API and so on. And then you will use LLM to decide which tool to call. So LLM can tell you, should

1:59:37

I call this tool? And generally, even you can give some description also about the tool, right?

1:59:42

That this tool, we will call to search the products from database. So what LLM can do?

1:59:47

LLM can understand this information and based on the data that the user is passing,

1:59:53

the query that user is passing, it can decide which tool will be helpful in this particular query.

1:59:58

So for now, we just have one tool here. So it is just a simple JSON. Are you guys getting this

2:0:05

point? For now, it is just a simple JSON. Okay. And now for tool call, we will just call this particular

2:0:13

tool. Okay. And in the information,

2:0:17

Input parameters, what we will do, we will just pass these arguments. Ideally, these arguments

2:0:22

should be coming from the user, but just for verification it, just for verifying it quickly, we are

2:0:27

just hard coding these arguments. But these arguments might be coming from user query as

2:0:32

well. Okay? So what we will do? Tool calls, tool calls. For now, there is only one tool call.

2:0:38

And from here, get the arguments. How many if you are getting this point? So it is a simple function

2:0:44

call. You can say that, it is just a simple function call. And we will

2:0:47

we will try to print tool output.

2:0:51

Tool output. Does that make sense to all of you? Yes or no.

2:1:00

So what we have simulated, if you see, we are just, we have just simulated a real database

2:1:04

with a real product table, inserted real products into the database, and then we are making

2:1:09

a function called to fetch the products. Now, in reality, what is going to happen is,

2:1:15

maybe let's try to run this code and then we will try to simulate the real AI application

2:1:20

also. How many if you're clear till this point of fine? Just have a look at the code and let me know.

2:1:26

Created a product class, which is coming from the base class, then creating all the tables

2:1:32

automatically via ORM. If you see, we have not written any query to create the tables,

2:1:37

then inserted some sample data in the table, then created a pidentic base model class for

2:1:43

validating the input parameters, the arguments, and then return a function to search

2:1:48

from the database, simple again using the session. Again, everyone, if you see here as well,

2:1:53

are we writing any SQL query? Are we writing any SQL query? No, there is no SQL query because

2:2:01

everything will be taken care by ORM internally. Okay? Getting the products from database,

2:2:06

returning them as it is, and just we are simulating the sample workflow. Right? And now what we can

2:2:12

do everyone is we can call all of these functions one by one. Okay. So either we can call

2:2:17

these functions in the main function or we can call these functions like agent flow manually also.

2:2:25

Okay. First everyone, before before even you call the agent flow, you will also have to

2:2:30

call right, insert data. Insert data function and then agent flow. For now, even I can remove this user

2:2:40

query as well because there is no concept of LLM as of now. We can just make a call to simple

2:2:47

agent for. Is that point clear to all of you? Yeah, you can write this in the main function also.

2:2:55

It is okay. How many if you're clear? So should we try to run this now?

2:3:01

Clear.

2:3:02

Python 3 and amp.py. Pyre. Let's see everyone.

2:3:10

Okay. Now if you see there is a small problem here. If you see there is a what we are checking

2:3:21

mobile, maximum price, 50,000. Is there a mobile phone with less than 50,000? I think yes.

2:3:29

There are two mobile phones less than 50,000. And everyone, if you see the stock, in stock is

2:3:34

equal to true, there is only one. So this one plus 12R is coming, right? Ideally, it should come in

2:3:40

the output. Because the arguments that we are passing are true, 50,000, less than 50,000,

2:3:48

correct? So only one product should come in the response, which is this one. Folks, yes or no?

2:3:54

And which is coming also. There is only one product. But do you say that everyone, it is coming as a

2:3:59

product object. It is coming as a list and inside the list, it is coming as a product object. We are

2:4:06

not able to see the product details. It means that we will have to, we will have to convert.

2:4:10

this product object into a kind of a JSON structure. Right. Okay. So what we can do?

2:4:19

Products from DB. Got it. So what we can do, everyone, is we will iterate over this for every product. In products from DB, we will create a list. Product, outputs,

2:4:40

an empty list. And what we're going to do everyone is that product outputs dot append.

2:4:52

Okay. So what we can do everyone is. Yes, we need to convert object into JSON, right? And that is what I was

2:5:00

thinking. So now everyone, the output that you are getting, that you are getting in the product object.

2:5:06

So you will have to create an object and then you'll have to add it.

2:5:10

So either you create a product object. Okay, got it. So let's say product dot, append.

2:5:21

JSON. Dot loads. I think we can do that also. But if you see,

2:5:33

so we have a list of products and every product is an object, a Python object.

2:5:40

But actually, if you see, it is coming from, it is coming from database.

2:5:45

Okay. Let me check whether it will work or not. It is giving us the memory pointer. Yeah,

2:5:49

it is giving you the address. It, in something unpacking, we are doing wrong. No, no. It is

2:5:56

giving you the object. Okay. If you see, every object, every reference, let me just show you this thing.

2:6:07

what happens is that in every application like what object gets created. If you are creating

2:6:14

an object like this and when you do product product is equal to new product, right, the product is

2:6:19

just a reference. It is just a variable name. Right. And this object is actually created at a

2:6:25

particular memory address. Okay. So for example, if you see it is, let's say some memory address,

2:6:32

this memory address that you see, right, some random memory address like zero, X.

2:6:37

1, etc. So this is some memory address x1102 something. Okay. Now if you see, if you try

2:6:44

to print it, for example, in this case, even if you don't want to do this, whatever object you are getting,

2:6:49

whatever output you are getting, if you, if you directly can do that, so it is a list, right?

2:6:54

It is a list. So get an element at 0th index, right? And then try to print its, let's say, product name.

2:7:03

Try to print it product name. So it should give you.

2:7:07

1 plus 2LR. Make sense? Right? You can try to, like, you can do this also.

2:7:14

Make sense. So when you do dot, it means that you are going to that address, okay? So when you do dot,

2:7:20

right, so let's say this is the product reference. When you do dot, dot means you are going to that address,

2:7:26

dot means referencing. You are going to this address and whatever value of the name, you are reading it

2:7:32

and printing it. Okay.

2:7:33

Okay. So if you make it, let's say, 60,000, then you might get more products. Are you guys getting this point? Or let's say if you make it one lack, you might make it, you might get it more. You are getting iPhone 50. Okay, what is happening? I think less than one lack and in stock true. Why we are getting only one?

2:7:58

because we are just doing zero right we are just doing zero right we are just doing

2:8:09

zero i thought that why we are only getting one so this is a list everyone you can also do like this for

2:8:14

for a product p in tool output you can just try to do this p dot name

2:8:28

P. Name. Now we want why we are getting iPhone 15, 24, 12R 15, again and again,

2:8:44

again and again, why so? Why we are getting iPhone 15 so many times, S24 so many times, 12R so many times.

2:8:52

Because if you want, this insert function we executed multiple times. So one, one product has

2:8:58

has been added again and again. Correct or not? One product has been added again

2:9:02

and again. Correct. That's why it is coming multiple times. But I hope the simulation is making

2:9:07

sense to all of you. I hope the simulation is making sense to all of you. Okay. Okay. Okay.

2:9:14

So guys, the complete explanation I have added. Now one thing that I would want all of you to try to do that, everyone is, try to integrate LLM here.

2:9:28

tell me how can you try to integrate an LLM here? Can you show the database? Yeah, sure.

2:9:34

Databases like this. Okay? Actually, what you can do is these are six products we have added, right?

2:9:44

You can delete some of these products.

2:9:58

So that query was executed four times.

2:10:19

Okay, now you have only six products.

2:10:22

Okay, while deciding which query to choose, we can use LM. It can read the comments.

2:10:28

A see which function to use. That's correct. We can define multiple queries like the one we did. We can do that as well. Absolutely. Okay. We can do that as well.

2:10:37

Cool, Sandhya. This is how the database looks like. Okay. Now everyone, try to integrate a data, try to integrate Open AI API here. Can you tell me how can you do that? Just last thing for today's class. I think Open AI API we have integrated like 10 times.

2:10:58

Now, I want all of you to take the initiative and try to do that. How will you do that?

2:11:06

How can you take that?

2:11:12

Can you tell me?

2:11:26

Guys, I'm not asking about the first.

2:11:28

code. I'm asking about the logic. Code, I know. All of you can write it or you can take the

2:11:33

reference from the previous classes. I know that import open AI, from open AI, import open AI,

2:11:39

client is equal to open AI, set the API key, etc. Can I say that everyone? You will get the user

2:11:46

query in the input. Take the user query in the input and then give this query to the LLM, write a prompt,

2:11:55

right? Let's assume that you have multiple APIs, you have multiple

2:11:58

tools. You have search tool. You have weather tool. You have make my trip tool and

2:12:02

whatnot. And then write a prompt to the LLM that, okay, this is the prompt, this is the user query.

2:12:08

Please decide. Please try to solve the query. If you're not able to solve, don't make up the answer.

2:12:14

Just make a tool call from this list of tools. So you have to pass this list of tools to the LLM

2:12:20

and let the LM decide which tool it should call internally. It will call the tool. It will tell you. It will just give you.

2:12:28

give you in the response, which tool to call. And then you make a tool call. Here, if you see,

2:12:33

there is only one tool call, so we are manually making a tool call. But ideally, if we want this tool name,

2:12:39

this instead of search product tool, this tool name should be coming from the LLM and then you will

2:12:45

make a call. Is that point clear to all of you? Yes or no. So logically, this is what we're going

2:12:54

to do if you are integrating LLM in a agentic AI application.

2:12:58

I think the rest of the things we have already done in the previous classes.

2:13:01

So folks, how many of you are 100% clear with the main agenda for the class, which is your database integration, Pidentic, that we have already seen.

2:13:09

It was a quick revision of Pidentic.

2:13:11

Second thing was your, and one more thing, everyone.

2:13:15

Let's say if you give a wrong input, right, let's say, category may you give, let's say, maybe one, two, three, four.

2:13:22

If you see, this is an integer, you're passing integer, but category should be a string.

2:13:28

Because everyone you are using Pidentic here, you are using, you are validating the input

2:13:33

via Pidentic. It should give you some validation error. But everyone, the code should not break

2:13:38

because you are handling the exception. You are not throwing the exception. You are just

2:13:42

handling the exception. It should return this error. Right. And let's see everyone. And go to

2:13:49

the terminal. If you see,

2:13:58

Okay, user query, remove it.

2:14:05

Yeah, because there is no output.

2:14:11

So, okay, you are returning this.

2:14:21

Okay, now what you can do is do is

2:14:28

See now. Success is false? That was the query successful? No. What error you are getting

2:14:37

invalid input provided? What is the detail? Detail is automatically coming from the exception.

2:14:42

And if you see look, attribute category, input should be a valid string. Is it good enough

2:14:48

for the user to understand what wrong input they are passing? Based on tool name, yes,

2:14:58

on tool name. Also, you can add a description here. That when to use this tool,

2:15:04

for what purpose this tool is required? Okay? Vishwanath? Yeah. Folks, is the validation part

2:15:17

also clear to all of you? Okay. Now everyone, let's, this is it for today's class. Now, what we're going to do is, let me push the

2:15:28

For this, I will have to create a new repository. This is the first time we are writing this code.

2:15:33

This is a new project basically, so we will have to create a new repository.

2:15:38

So let me just write it, agent.

2:15:58

So if this is the code, can you see that?

2:16:13

Okay, if this is the code, can you see that?

2:16:20

What if tool name and description differs from what it does?

2:16:28

Vishwanap, if you are saying that you are giving different tool name and different

2:16:34

description, it means that your input is itself incorrect, incorrect. In that case, LLM might make

2:16:41

mistake. See, first of all, if you are giving the description, tool name does not matter. Most

2:16:47

of the times, tool name does not matter. But you should have a proper description, right? Tool name

2:16:53

can be anything. They are just functions mean. You can also give F1, F3.

2:16:58

function 1, function 2, function 3. But you should provide a proper description to the tool

2:17:03

so that it will help LLM to decide the right, the right tool to call.

2:17:08

Okay?

2:17:09

So the code has been pushed everyone.

2:17:12

I will just upload the notes as well.

2:17:19

And then everyone we will have a quiz.

2:17:28

Thank you.

2:17:58

So if these are the notes for today's class, could you check if you're able to access, okay, I think I'll, I sent the link to host.

2:18:21

Now this is the code link, everyone, and this is the code link, everyone, and this is the

2:18:28

I have shared the notes as well for today's class and the code as well.

2:18:31

Can you check if it is accessible to all of you?

2:18:33

And now we will have the quiz.

2:18:58

Today, very easy quiz.

2:19:02

Okay, so let's start everyone. Please join the quiz either via QR code or you can use this link to join the quiz.

2:19:11

Let's wait for at least 25 to 30 people to join the quiz and then we'll start.

2:19:28

Thank you.

2:19:58

Okay, let's start the quiz everyone.

2:20:05

Okay, let's start the quiz everyone.

2:20:11

Okay, reduce the time. I'm not sure what time do we have today for the quiz for every question.

2:20:21

Let's see.

2:20:25

Okay, going forward somewhere we can have like maybe 20 seconds of

2:20:28

time for the question. Okay. Okay, straightforward. Let's move to the next question now.

2:20:51

Which data format is commonly used in modern APIs?

2:20:58

Simple, again, Jphone.

2:21:13

Almost all of you got it right, very good.

2:21:28

Okay, resource not found, very good.

2:21:58

200

2:22:28

It is very straightforward, successful.

2:22:37

And here we go to the last question.

2:22:58

What is the use case of P P P Pyrentic?

2:23:13

is used for data water.

2:23:16

Data training.

2:23:18

Data training, data styling, data styling, data storing, or data validation.

2:23:28

It is used for data validation.

2:23:33

Okay, so we are done with the questions, everyone.

2:23:35

So let's see the leader board.

2:23:37

Seems like Kathy is at the top.

2:23:42

No, I think ET will go at the top.

2:23:44

Okay, Peelings, who is Peelings?

2:23:47

Funny name.

2:23:51

Saban, great.

2:23:52

Keep it up.

2:23:53

Good work, everyone.

2:23:55

So that's it for the class, everyone.

2:23:57

How many if you enjoyed the class?

2:23:59

How many if you understood all the topics for the class?

2:24:02

Mainly the agenda for the class was to teach you SQL Alchemy, ORM, Pidentic.

2:24:08

Pyrintic was a revision only.

2:24:10

All of you understood?

2:24:11

Very good.

2:24:12

So now we will launch the feedback poll, everyone.

2:24:15

Please take the feedback poll and then feel free to drop off.

2:24:20

Once we are done with the feedback poll, please feel free to drop off.

2:24:27

Okay, I think everyone has given the feedback. Thank you so much everyone.

2:24:57

Okay, thank you, everyone.

2:25:12

Thank you, everyone.

2:25:15

Thank you, sir.

2:25:16

We'll meet tomorrow if you have any doubts and then all the very best for your evaluation.

2:25:25

Yeah, so.

2:25:26

So these guys have evaluation on this week, right, weekend?

2:25:29

Yes, that's what I have been in front.

2:25:32

Okay, anyone has any doubt?

2:25:34

I can stay for a few minutes if you would like to discuss anything.

2:25:38

Sure, sure.

2:25:39

Yeah, anyone?

2:25:42

Maybe Samya, if you want to ask anything.

2:25:45

Samya, I think your kakal, right, the tutorials.

2:25:48

Oh, tutorial, right.

2:25:49

Okay, so if you want to ask anything right now, feel free.

2:25:52

If you want to ask something in the tutorial, please do prepare for.

2:25:56

tomorrow and go through the concepts.

2:25:59

If you have anything, then you can ask Somia tomorrow.

2:26:02

Okay.

2:26:03

Yeah, if you want, you can just list of your topics that you want me to discuss or we can go

2:26:08

over assignments as we usually do.

2:26:13

Yeah, I think we do have the feedback poll for that as well.

2:26:16

If you want, Somia, you can launch that also.

2:26:19

People can fill some doubts if they have.

2:26:23

We can do that.

2:26:24

Let's do that.

2:26:26

Yeah, yeah, maybe just for 30 seconds.

2:26:34

Take you.

2:26:35

Thank you, everyone.

2:26:36

Bye.

2:26:37

Thank you for now.

2:26:42

Note that there were more many extra sessions.

2:26:47

We are just launching this goal so that if you have any doubts, I can take it up tomorrow.

2:26:52

Yeah.

2:26:56

Thank you.

2:27:26

Thank you.