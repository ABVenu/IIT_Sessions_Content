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

Thank you

5:20

Thank you.

5:50

Thank you.

6:20

Thank you.

6:50

Thank you.

7:20

Thank you.

7:50

Thank you.

8:20

Thank you.

8:50

Thank you.

9:20

Thank you

9:50

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

Thank you

10:38

Thank you

10:40

Thank you.

11:10

Thank you.

11:40

Thank you.

12:10

Thank you.

12:40

Thank you.

13:10

Thank you.

13:40

Thank you.

14:10

Thank you.

14:40

Thank you

15:10

Thank you

15:40

Hi,

15:47

Hi, everyone.

15:48

Hi, everyone.

15:49

A very good evening to all of you.

16:08

Welcome to the session.

16:10

Welcome, Deepak sir.

16:12

We'll start in a couple of minutes.

16:15

People are still joining.

16:19

So you can start with one.

16:40

Good one, very good evening.

16:47

Books.

16:49

Am I audible to all of you?

16:55

Hi, everyone.

17:09

Hi, everyone. Am I available?

17:13

Okay, great.

17:14

Good evening, everyone and welcome to the class.

17:17

So, folks, let's get started with the application.

17:21

And today we are going to talk about tool calling via Langchain.

17:27

So today we will see Langchain applications with tools application, with implementation of tools.

17:36

Okay.

17:37

Now, can you tell me what tool?

17:39

are tools are and when do we need?

17:48

For what kind of operations do we need tools?

17:51

Actually, what more thing, everyone, before we actually start with today's content.

18:08

Okay.

18:09

walk through this, right?

18:11

Let's see this.

18:13

Can everyone see the GitHub screen?

18:19

Let's spend maybe two minutes on this.

18:22

I have only received this today.

18:24

Okay, so I will also walk you through with you guys.

18:27

Okay.

18:28

Basically, this is a mind map that we will try to cover in every,

18:33

in every session, what we are covering, why we are covering,

18:36

how we are going to utilize that, etc., etc., etc.

18:38

etc. Now, if you see everyone, the mind map for today's class, right?

18:43

In the previous module, what we have covered,

18:45

we have covered agentic foundation and architecture.

18:48

Correct.

18:49

We have learned about basics of LLM, prompt engineering, backend foundations,

18:52

like FID intake, fast API, etc., right?

18:55

Direct everyone?

18:56

This we have already covered?

18:58

Folks, yes or no?

19:00

LLM basics, foundations, backend foundations, prompt engineering, etc.

19:05

Then folks, this was the first module.

19:07

In the second module.

19:08

module we covered agent components like memory, tools, rags, retrieval, etc.

19:14

Where we talked about APIs such as tools, vectors, retrieval, retrieval, and generator, etc.

19:22

In the current module, everyone, until this point of time, we have learned about Olama and LangChain

19:27

foundations, correct?

19:29

And in today's session, everyone, we are continuing our discussion with Langchain,

19:34

where we are going to talk about tool calling via land chain.

19:37

Okay, how can we use?

19:38

utilize the Lankchain as a framework to call tools, right?

19:43

How can you build your own tools as well?

19:45

How can you call external tools as well?

19:47

And then everyone, this is the entire mind map.

19:51

And the course path will follow like this.

19:55

It will turn Lankchain into action-ready systems by the end of this module.

20:00

Yes, that's correct.

20:01

Foundation for agents' memory and Rack tools.

20:04

The next module is going to be multi-agent collaboration and deployment.

20:07

and deployment.

20:08

How can we build multiple agents together?

20:10

How can we build a multi-agent architecture?

20:12

And also we will see a few things related to deployment.

20:15

How can you deploy your application?

20:18

Okay?

20:19

We will also be looking at frameworks like N8N, new AI, auto gen,

20:23

monitoring, tracing and guardrains, right?

20:27

Basically, what all the things you should take care of while

20:30

deploying the application?

20:32

How can you protect your application?

20:33

How can you make your application secured?

20:36

Okay.

20:37

This is everyone.

20:39

We will see that real-life use case of these applications.

20:42

How assistants, like how agents or assistants can call calculators, databases, and APIs.

20:48

Don't you think even all of these are nothing word?

20:50

Your tools, calculator is a tool, database is acting like a tool.

20:55

If you are using some external API, like Weather API, make my trip, book my show, etc.

21:00

These are also called as external tools or API.

21:04

Okay?

21:06

Right? And everyone, this particular concept we will be using in the Capstone project as well.

21:13

We will be having, we will build an autonomous system.

21:18

And we will use tools, memory, rag, evaluation, deployment, etc.

21:22

I think this we already know.

21:24

Okay, these are the things that we are going to cover.

21:27

Okay, now let's come back to notes.

21:29

Is the mind map clear to all of you?

21:31

Is this diagram clear to all of you?

21:33

I can share this diagram also with all of you.

21:35

with all of you. Okay. Anyways, everyone, need not to share because this particular diagram,

21:40

team will be adding in the pre-reads. For every lecture, do you receive the pre-reads from the

21:46

Maasai team on your dashboard, on your LMS? Yes or no? For every lecture, you must be getting

21:54

a pre-read. How many people see that? How many if you go through the pre-reads?

22:05

If you go through the pre-reads,

22:07

few people go through, but few people might not be going through the pre-reads.

22:17

Those people might be going through the notes directly.

22:20

It is okay.

22:21

But going forward, this particular mind map will be added with the pre-rates of every lecture.

22:26

Okay?

22:27

This is what I got from the team.

22:29

Anyway, now let's get started with today.

22:31

Can everyone see my iPad?

22:33

No.

22:34

Okay.

22:35

Let's see my iPad screen now.

22:40

Now, everyone, let's say if you have an AI application with only LLM.

22:47

Is it okay now? Is it better now?

22:58

Okay. Then let me rejoin the session, everyone.

23:04

Let me leave the webinar and...

23:09

Okay, let me rejoin everyone.

23:14

I think there might be.

23:34

Folks, am I audible now?

23:37

And is it slightly better?

23:42

Is the voice better now?

23:45

It's crystal clear now.

23:47

Okay, I think just rejoining the work, nothing else.

23:51

Okay? Fine, everyone, let's say you just have an application with only LLM.

23:58

Now tell me everyone, with only LLM, can you fetch external data?

24:03

Can you fetch external data?

24:03

Can you make a call to database? Can you make a call to external APIs?

24:07

Tell me if you just have an LLM? No. If you just have an LLM-based application,

24:13

definitely your system will be knowledgeable.

24:15

You can respond the queries. You can respond to the queries.

24:19

You can answer the queries. But can you perform any action?

24:23

Answer is no. To perform action everyone, you will have to combine LLM with external tools.

24:30

Correct or not?

24:32

you will have to combine LLM with external tools.

24:36

Correct or not?

24:37

Yes.

24:38

This is what we are going to see today.

24:40

Right?

24:41

So, guys, an external tool can act like a database.

24:44

Now, in RAG applications, everyone, if you remember, in retrieval augmented generation,

24:48

did we connect our AI application with a database, with a vector database?

24:53

Tell me?

24:56

Yes.

24:58

Don't you think, everyone, for a Rack-based applications,

25:01

Bector database is also acting like an external tool.

25:05

I think I remember that I discussed this point in that class also.

25:09

That is also acting in external tools.

25:12

But everyone in Lankchain, you can also call these via functions.

25:18

You will see that by the end of the class.

25:21

In Lankchain, tools are nothing but

25:25

tools are callable functions that you can call, that you can execute.

25:30

Tools are.

25:31

are callable functions with well-defined input inputs and outputs.

25:40

With

25:45

inputs.

25:51

And outputs.

25:52

Correct or not?

25:58

Okay.

25:59

Screen is not shared.

26:00

is not shared, it should be visible now.

26:04

Right?

26:05

In Lankchain, tools are the callable functions with well-defined inputs and outputs.

26:09

Correct?

26:10

Very good.

26:11

Now everyone, generally what happens, right?

26:13

When you make a query, when user sends a query,

26:17

query, first of all, everyone, goes to the LLM.

26:21

Okay?

26:22

What LLM does everyone?

26:23

Can I say that LLM decides?

26:25

First of all, first of all, the query goes to the LLM

26:28

and NLM will check that can I?

26:29

will check that can I answer the query?

26:31

Okay?

26:32

Do I have an answer for this query?

26:34

If LLM has an answer for that query,

26:37

LLM will answer the query,

26:39

because LLM has reasoning capability,

26:42

LLM can think,

26:44

LLM is acting like a brain of the system,

26:46

LLM can actually decide that do I need to make a call to the external

26:50

correct?

26:52

So LLM asks itself,

26:54

LN decides

26:59

LLM decides, what it decides?

27:01

Can I answer the query?

27:03

Can I answer directly?

27:05

Okay, can I answer directly?

27:19

If LLM can answer directly,

27:22

then LLM can decide what tool should I call?

27:26

So the tool call will happen.

27:28

will happen either LLM might make a call to database,

27:32

LLM might make a call to Xpedia,

27:34

book my show, make my trip, or some database,

27:37

weather API, etc, etc.

27:39

Right?

27:40

Then everyone LLM decides which tool to call, okay?

27:43

Which tool

27:49

to call?

27:52

Then everyone,

27:54

after LLM decides which tool to call,

27:57

application calls that.

27:58

that tool.

27:59

Application calls the tool.

28:09

Okay?

28:10

Application calls the tool.

28:12

Now tool will send, we'll give the response, right?

28:15

Now, tool response, can we return directly to the user?

28:19

Whatever response we are getting from the tool, can we directly give that response to the user?

28:25

Sorry.

28:27

Generally, we don't.

28:28

give the response directly to the user because tools may return the output

28:32

in a different, different format.

28:33

For example, everyone, Make My Trip can return the output in a different format,

28:37

Expedia can return the output in a different format,

28:40

or different tools or database can return the output in a different format, etc.

28:44

But everyone, if the client, if the user is using your application,

28:48

then you need to take care of the output structure that you are sending back to the user.

28:53

That output is in the proper format, it is a user-friendly format, etc.

28:57

Right?

28:58

So whatever tool result we are getting, tool result is sent back to the LLM.

29:10

Sent back to the LLN.

29:13

And finally everyone, LLM gives user-friendly response.

29:28

LLM gives user-friendly response.

29:33

Is that point clear to all of you?

29:35

Yes or no.

29:36

This is the complete idea that we are going to implement in today's class.

29:43

Okay?

29:44

Now everyone, if you have to build any tool in Lankchain,

29:48

it is a very simple thing because at the end of the day,

29:50

if you see, tool is nothing but a function.

29:53

Inside that function, you can make a call to database,

29:56

you can make a call to make my trip, you can make a call to.

29:57

trip, you can make a call to any weather if anything.

30:00

For Lankchain, it is a tool, right?

30:03

A tool is nothing but a callable function.

30:05

Right?

30:06

So, for example, if you define this any function,

30:10

let's say call, make my trip, or fetch data from database.

30:14

Petch from database.

30:18

Let's say this is a function.

30:20

This is a function that you have implemented in Lankchain or Python.

30:25

How can you tell Lankchain?

30:26

How can you tell Lankchain?

30:27

that, okay, it is not a normal function, rather it is a tool, right?

30:31

So you can just define at the rate tool decorator.

30:34

Okay?

30:35

So any tool that you want to define in Langchain,

30:38

you can use at the rate tool annotation.

30:43

Okay, this is called as tool decorator.

30:50

Is that point clear to all of you?

30:52

We are having trouble joining today's session after multiple attempts.

30:56

Okay, Gaurish. I joined just now today due to LMS issue.

31:03

Okay. Soami, could you please raise this issue to the tech team or to the PEOC, to the right POC?

31:15

I think a lot of people are having some trouble in joining the session.

31:26

Okay, folks, let's do one thing then. Let's wait for one minute. Let me check.

31:56

Okay.

32:03

Are you there?

32:26

Okay, I think people have joined now.

32:36

So let's just have a quick recap.

32:39

What we have discussed, everyone, is we have just discussed about what tools are.

32:42

I think tools is something that we have discussed multiple times in the previous sessions,

32:47

that what are tools? Tools are external functions or the functionalities that you call to get some external data, to call to the database,

32:55

or let's say if you want to check the weather, if you want to book a ticket, etc, etc.

33:00

If you want to do any action, you do that action via tool.

33:04

Now, what is the difference between a normal LLM-based application and an agentic AI-based application?

33:11

LLM can just tell you what to do.

33:13

Right? LLM cannot take any action, correct?

33:16

LLM-based application cannot take any action autonomically independently.

33:22

But if you want to make a AI-based application.

33:25

application autonomous so that it can take decisions and as well as it can execute those decisions, it can take actions also.

33:35

Then we have to make them autonomous.

33:37

We have to connect them via external tools so that they can make a call and they can decide.

33:42

Right.

33:43

For example, let's say if you are creating an itineri using LLM based application, so LLM based application can tell you the italy

33:50

there, you can travel there, you can go there, you can go there, Delhi to Bombay, Bombay to this, this, etc.

33:54

etc. But LLM-based application cannot book a flight for you.

33:58

It cannot book a cap for you. It cannot book a hotel for you.

34:02

Correct or not, everyone?

34:07

Right? But if you add external tools, for example, if you can give the access to the Make My Trip API,

34:13

then it can also book a ticket for you.

34:16

Right? Also, if you can connect multiple airline partners or multiple airline websites with your agent,

34:23

then it can also compare which airline is cheaper and then it can tell you that, okay, this is a cheaper airline.

34:29

Can you please confirm if I can book this particular ticket?

34:32

If you confirm, that agent can also book a ticket on your behalf.

34:37

Is everyone clear?

34:38

Folks, yes or no?

34:42

Right?

34:42

So today we are going to use these tools and how do you build any tool in Lankchain using this ad the rate tool decorator?

34:49

On any function, everyone, if you add this at the rate tool, it becomes a tool.

34:53

it is acting like a tool now okay folks clear whoever have like all the people

35:04

who join late gaurish uh shantanu toheel etc all the people who join late now is that clear

35:11

okay now everyone if you want to build a basic tool you can write a simple let's say for example

35:17

maybe let's say you build a function called as define def get order status get order status get order status and in the input you give order ID and this order ID is let's a string format okay now everyone what you can do you can take a call to database here

35:47

It can be a real database. It can be a vector database. It can be a SQL database.

35:53

It can be some external API. For example, everyone, let's say you can also make a, like, if your database is externally hosted, right?

36:01

You can also make an API call that, okay, give me the status of this particular order, and you get the status.

36:06

Make a, let's say, make a DB call.

36:17

order status for the given order ID or the provided order ID.

36:29

Okay, this is what the function is.

36:32

And if you want to define this as a tool, then you do that at the red tool.

36:37

Is that unclear to all of you?

36:47

Okay. And you can return the data in any format. You can return the data in the form of JSON. You can return the data in the form of string, et cetera, etc. Okay. Now, one more thing, which is very important is that while writing the tools, don't try to write the tools without proper description, right? Or just don't return, let's say, vague output from the tool, right? Please make sure that if you're building a good production-based application, make sure that if you're building a good production-based application, make sure that,

37:17

you are writing the tool in the production ready way.

37:20

Makes sense, everyone, that you are giving proper input parameters, you are giving proper output parameters,

37:26

you are defining proper output format, etc.

37:30

Right?

37:30

Because everyone, in production environment, tool quality matters a lot.

37:36

Because everyone, if you don't write proper tools, right, if they are not taking proper input parameters,

37:41

if they are not returning proper output parameters, then it becomes very difficult.

37:45

Right?

37:45

in the production to debug, what went wrong?

37:49

Now, let's say, if any particular tool fails, right?

37:53

Why did that tool, why did that particular tool fail?

37:56

How do you debug it?

37:58

Right?

37:58

So, tool quality is very important.

38:03

Very important in production systems.

38:08

Is that point cleared all of you?

38:11

Very important in production systems.

38:15

Always use proper input and output structure.

38:45

mass defined.

38:54

Everyone?

38:56

Also, everyone, there are a few good practices that you should follow.

39:00

Tool names are generally written, are generally written in snake case format.

39:15

Everyone knows snake case format?

39:25

Small case characters and words are separated by underscore.

39:30

For example, let's say, get underscore order, underscore status.

39:36

This is called a snake case format.

39:39

For example, let's say if you have to create a ticket, create ticket, or create a different ticket.

39:45

So create is a word, different is a word, ticket is a word, right?

39:49

All of them are small case correctors separated by underscore.

39:54

Is that point clear to all of you?

39:59

Okay.

39:59

Again, everyone, it is a recommendation.

40:02

It is not a hard and fast rule.

40:04

Are you guys getting this point?

40:06

It is a recommended approach.

40:09

Okay.

40:09

First, let's just go through these things and then we will write the actual tool as well.

40:14

Okay.

40:15

Now, also, you know, so.

40:15

everyone, one thing that we can use is that, which is very important in fact, that we said

40:22

that, okay, tools, the tools should have proper input and output structures or schemas.

40:29

How can you define the input or output schema?

40:41

How can you define the input or output schema?

40:45

How can you enforce that?

40:49

Have we learned any library in Python which can help us to define the structure?

40:55

That okay, this should be string, the length should be 10, it should not be null, it should be optional, it can be optional.

41:02

If optional, we can do that via Pidentic.

41:07

I hope everyone is well aware of Pidentic.

41:11

Correct or not?

41:13

Everyone is well aware of Pidentic.

41:14

that you can define a pidentic base model and you can say and you can tell that this particular

41:20

field should be a string, this particular field should be an integer.

41:23

If it is integer, it should be greater than zero, it should be less than 100.

41:27

If it is spring, then the length, minimum length should be 10, maximum length should be 100,

41:31

etc, etc.

41:32

Whatever restrictions you want to do that, you can define that.

41:36

Correct?

41:39

Now, how do we do that?

41:41

Let me write it down in a very, very short.

41:44

For example, let's say you are defining this tool, create refund ticket.

41:48

So first, everyone, you define the class, the input for refund.

41:54

Refund input, right?

42:00

Obviously, everyone, you have imported base model already.

42:05

Base model.

42:07

Okay.

42:09

Then everyone, you define all the values here, let's say, order ID.

42:14

For example, order ID string.

42:16

And everyone, in this string, everyone, for example, give any input.

42:21

For example, let's say, if any restriction description, description you can provide,

42:24

whether it is optional or mandatory, if it is option, then what is the default value, right?

42:29

If it is string, what is the minimum length, et cetera.

42:30

You can do that inside the field operator, right?

42:33

Then everyone, you can define all the input parameters like this.

42:36

Now, when you define the function here, the tool here, let's say, define the function,

42:42

create,

42:44

refund ticket, right, create refund ticket, then you can define this at the red tool.

42:55

Now, if we say that, okay, let's say this refund ticket is going to take the object, is going to take

43:02

this refund object in the input, right?

43:04

What does it need?

43:05

It needs all the fields like order ID.

43:11

And let's say, this is the reason of refund.

43:14

the date of the product, et cetera, et cetera, all these fields.

43:18

Now, how can you enforce that whatever values, like, basically you want to enforce these restrictions

43:24

on these input parameters?

43:26

So what do you can do, everyone?

43:27

Inside the tool annotation, inside the tool decorator, you can do that arcs.

43:33

Arg means arguments, input parameters.

43:36

Args underscore schema, what schema does input arguments follow?

43:43

refunding.

43:44

Is that point clear to all of you?

43:50

That input arguments will follow this particular structure.

43:54

Now, automatically, Pyrentic will make sure that order ID should be string.

43:59

It should follow all of these field properties.

44:03

Does that make sense for all of you?

44:04

All of these will follow these field properties.

44:09

Are you always getting this point?

44:11

So, Identic will automatically make sure that.

44:16

So we are calling the refund input class.

44:18

We are not calling the refund input in this case.

44:20

We are thinking that, okay, for this particular tool, for this particular tool, argument means,

44:26

and it's means arguments.

44:28

Argument means input parameter.

44:30

That input parameter follows this particular schema.

44:34

That whatever properties you have applied for refund input, they will be applicable on the arguments

44:40

for this function.

44:42

Makes sense, Mr. Right?

44:48

If JSON, then you can do that.

44:51

Okay?

44:52

If it is JSON, then we can do that.

44:54

Yes.

45:00

JSON.

45:00

Does it guarantee the JSON structure?

45:04

What if, like, inside JSON, you cannot define other properties like that,

45:07

for example, order ID,

45:09

should be of, let's say, five length.

45:12

That is very difficult, right?

45:14

But with Pidentic, you can do that.

45:16

This is an optional field.

45:17

This is a mandatory field.

45:18

If this is optional, then what is the default value?

45:20

Right?

45:21

If, let's say there is some integer field, right?

45:23

It should be greater than equal to zero, less than 50.

45:25

You can only do that via Pyrtic automatically.

45:30

Correct or not?

45:32

Yeah.

45:34

Okay.

45:35

Now, everyone, Langchain, you will have to bind the tools, right?

45:39

Now, what is the meaning of binding the tool?

45:42

Let's say, everyone, if you're defining 10 tools in your language and application,

45:47

how model will decide which all the tools does it have, or how model will decide which tool to call?

45:53

For that, everyone, don't even think you will have to tell the model that these are the tools which are available.

46:03

Correct, everyone.

46:04

So, you can use a function called as bind tools.

46:07

I will show you that in the implementation.

46:09

that inside the model, you can do model, whatever model object you have, model dot bind tools,

46:15

and then you can provide a list of tools.

46:18

Okay, something like this.

46:20

Anyways, I will show you this in the implementation part.

46:24

Bind tools.

46:26

So, whatever model object you have created, you can do model dot bind tools, and here you can provide the input parameter in the form of list.

46:38

Clear, everyone?

46:39

Okay. So that model will understand that, okay?

46:45

We have the access to all of these tools. All of these tools are available.

46:51

Okay?

46:53

Okay. Now, everyone, let's do the next part now.

47:04

Okay. I think we are okay and we can definitely start with the implementation part now.

47:09

We are good enough.

47:11

The code for today's class is going to be very big, right?

47:14

It is not going to be difficult, rather it is going to be, it is going to have multiple lines of code.

47:19

Okay, multiple prompts are going to be there, multiple comments are going to be there,

47:22

multiple tools are going to be there, but those tools are going to be very straightforward.

47:26

Okay.

47:27

So implementation wise, it is not to be very difficult.

47:30

It is just going to be long.

47:31

Okay.

47:32

So, let's start writing this.

47:34

I'm just checking that.

47:36

We can directly start with the code.

47:39

What no issue?

47:51

What issue is there?

48:08

I able to hear.

48:09

Okay, try to rejoin.

48:11

There is some issue on Zoom site.

48:15

My mic seems to be good.

48:20

My mic is not buggy.

48:22

Okay, let me, maybe I can also try to rejoin.

48:24

You can also try to rejoin.

48:26

Okay, let me rejoin.

48:39

Is it better now, everyone?

48:47

Okay.

48:47

This is a home issue.

48:49

This is not hardware issue.

48:52

Anyways, is my code screen visible?

48:55

Is my visual screen visible?

48:58

Folks, we will open the folder.

49:00

The last chain, applications.

49:09

I will create a new folder.

49:11

Maybe let's call it as, I rejoin the session.

49:17

That's right.

49:17

Okay.

49:25

And tools.

49:29

Inside this, everyone, I will.

49:35

The voice is still breaking.

49:39

Is the voice fine now?

49:47

I'm not sure what it is happening.

49:48

There is some issue with the zoom.

49:53

Folks, let's continue then.

49:59

I think it will get better inside.

50:02

Okay.

50:04

If it gets better, do let me know.

50:06

So we'll go inside Langchain tools.

50:08

We will do.

50:09

We will create a new virtual environment and then we will activate the virtual environment.

50:39

We will create a folder.

51:09

Let's say create a new appellate.

51:39

3. Okay. We will install all the

51:42

we will install all the required library.

51:47

We would need Pyrintic. We would need Lankt.

51:49

We would need Lanchet.

51:51

Okay.

51:52

So

51:55

Terminal and we will install PIP3

52:00

install.

52:01

I.U.

52:02

OpenA.

52:06

Open A.I.

52:08

Let it talk.

52:12

Is it becoming slightly better everyone, the voice?

52:15

Definitely there is a zoom issue.

52:17

The internet is good.

52:18

My hardware does not have any problem.

52:24

Is it still having a lot of issue?

52:27

The voice.

52:29

The audio.

52:34

Not a lot.

52:36

The IP3 is tall Pynetic.

52:38

Okay.

52:40

So.

52:45

Identic is already there.

52:48

In top of your screen, it actually shows your smartphone.

52:53

If my mic is muted, then how can I, like how my voice will come to you?

53:01

Obviously, yes.

53:07

Correct.

53:08

Inconsistent. Definitely a room issue.

53:14

Okay.

53:15

So folks, are the steps clear till now?

53:18

Yeah, definitely a zoom issue.

53:20

Not my hardware issue.

53:24

Okay, so we created a new folder I have known Lanchetan tools.

53:27

Then we created a virtual environment.

53:28

We installed Lanchine OpenA.

53:30

As well as we installed Pidentic.

53:32

Now what we've got on the product?

53:34

We will define the open AI API key.

53:37

Go to the terminal.

53:38

And let me create an API key here.

53:41

We will go to platform.

54:08

Environment variable.

54:09

So, one, A.I,

54:10

and two RAPI is equal to

54:13

Right here.

54:15

Okay.

54:17

Yes, now.

54:18

This is how we do that.

54:20

Very good.

54:21

Then everyone, we will define the model name.

54:23

Whatever model we want.

54:25

Is equal to, let's say GPD.

54:30

That's it.

54:34

Then everyone, we will import.

54:35

We will start writing the code now.

54:37

We will improve.

54:38

all the required letters we will import JSON.

54:41

Which class is this?

54:43

Which class you are talking about, Foscal?

54:46

P.

55:01

Typing model we will import literal.

55:05

Typing, we will import literal.

55:06

typing, import, et cetera.

55:11

Then we will import Pidentic, base model and speed.

55:15

From Finantic, import base model and field.

55:20

And we will import these things.

55:24

Okay, I'm copying and pasting here so that we don't have to write again again.

55:31

Thanks again.

55:32

We are importing chat models.

55:34

From chat models, we are importing init.

55:35

Chat models.

55:36

model then from tools everyone we are importing the tool decorator that we are going to

55:40

use on top of every tool then lanchain.

55:43

Dot messages we are importing tool message.

55:45

What is this tool message?

55:46

We will see that.

55:47

Okay, we will use this.

55:48

Now let's start writing the code.

55:50

Okay.

55:51

Now everyone, we are going to write one tool for checking the order status of database.

55:56

Right?

55:57

For that, everyone, will we have to set the entire database,

56:00

whether it is SQL, MySQL,

56:03

we will have to set up the entire database.

56:05

data. So it is going to take a lot of time because we want to test the tool calling.

56:11

The class is not about setting up the database, creating the table,

56:16

inserting the data, and then checking this data.

56:19

The main idea of the class is to check whether the tool call is happening or not.

56:23

For that, is it okay if we use a mock database or a fake database.

56:29

Fake orders database. Is it okay?

56:34

Yes.

56:36

Is it okay if we use a fake order database, just like this, a normal dictionary.

56:42

That this is the order ID and this is the detail of that order ID.

56:46

This is the order ID.

56:47

These are the details of that order ID and so on.

56:50

Okay.

56:51

Then everyone, we will create a policy database.

56:56

Similarly, we have a policies database.

56:58

Okay.

56:59

If you see, for refund, this is the policy.

57:02

For shipping, this is the policy.

57:03

For shipping, this is the policy.

57:04

warranty this is the policy.

57:06

This policy information should be coming in the form of documents.

57:11

We should code those documents.

57:13

We should chunkify those documents.

57:15

We should create the embeddings, create a vector database and store these embeddings

57:19

or store the documents into the vector database.

57:22

That is the ideal scenario.

57:24

But have we already tried that and done that?

57:27

We have already done that, right?

57:30

Quite a long time, right?

57:31

Quite a number of times.

57:33

So that's why we will focus.

57:34

mainly on the idea.

57:35

That how tool works.

57:37

Then everyone, for, first of all, we will create the tool number one.

57:41

That, to check the order status.

57:44

For order status, everyone, what input do we need?

57:49

For checking the order status, we need order ID.

57:53

So what we can do, everyone?

57:54

We can define the tool number one,

57:56

okay?

57:57

Tool number one, let's say get order status.

58:03

Okay?

58:04

the order ID, which is a format of string.

58:07

That's it.

58:08

But everyone, what if?

58:09

Now everyone, let's say, you are saying that order ID should be strings.

58:14

But it's a enforcement that order ID you cannot pass as anything else apart from string.

58:20

Now, right, if you remember, this is what is called as type hinting.

58:25

Remember that, that you are giving a hint that order ID is string.

58:29

If you pass order ID as integer, will it give you any error?

58:33

because this is not enforcing the data.

58:42

So enforce the data type, we will have to use Pyrentic.

58:45

So what we can do, everyone?

58:46

We can create a class, let's say, order, status, input.

58:49

That what input do we need for order status?

58:51

We will import from base model.

58:53

We will import from base model.

58:57

We will see that order ID.

58:59

Order ID should be string.

59:03

And everyone, if you want to put any more validations, you can do that.

59:06

For now, you can just provide the description that order ID should be in the format,

59:14

format of something like this.

59:18

ORD, ORD 1001.

59:23

Correct?

59:24

This is how an order ID looks like.

59:26

So that user does not park the wrong format.

59:30

Are you guys getting this point?

59:32

So you can define in this way.

59:34

And because this is the tool, you can use the ad-the-rate tool annotation and you can give

59:38

ARG schema should be order input, order status input.

59:44

Is this point clear to all of you? Yes or no?

59:49

Folks, how many if you are clear, this is what we saw in the notes as well.

59:54

Now, whatever properties you have defined inside this base model class, inside this pidentic model,

59:59

those properties will be applicable to order ID.

1:0:01

to order ID. That is, it should be string.

1:0:04

If user tries to pass in a different way, it will fail.

1:0:06

It will give you a validation error.

1:0:09

Okay?

1:0:10

Then everyone, I will copy paste the code because it is very, very simple thing.

1:0:14

Okay?

1:0:15

You are getting the order ID.

1:0:17

You just have to go to orders database in this orders database.

1:0:21

Check if order ID is present.

1:0:23

If yes, take the order status,

1:0:26

else return order ID not so.

1:0:28

But I can do everyone, I can copy base this.

1:0:30

copy basis.

1:0:31

Just have a look at it.

1:0:32

See what we are doing.

1:0:34

What this function does?

1:0:35

Always everyone, as a good practice, always try to give proper statement or proper comment

1:0:41

to each and every tool.

1:0:43

So that if any other developer is also using your tool, using your function in the future,

1:0:49

if trying to change your function, if trying to, let's say, develop something else, right,

1:0:54

for that they need to refer your function, they can check.

1:0:57

They will be able to understand.

1:0:59

What this tool does?

1:1:00

it fetches the order status, item details, payment status, and delivery ETA.

1:1:04

Use this tool only when the user ask about the status delivery, shipping, or ETA of a specific order item.

1:1:13

Is this statement good enough to understand what this tool does?

1:1:18

Now you don't even have to go through the entire implementation, right?

1:1:22

If you want to see this implementation, if you want to understand it, you don't even have to spend two minutes on understanding the code.

1:1:29

It is pretty much clear.

1:1:31

So what we do, everyone?

1:1:32

We convert the order ID into the upper status, then we get the order.

1:1:35

If we don't get the order, we return an error in the form of JSON, right?

1:1:40

Status OK, false, error type, order not found.

1:1:43

Message is no order ID found.

1:1:45

Okay, else we will return okay.

1:1:47

Status is equal to true and order is equal to this.

1:1:50

We are returning the order details.

1:1:52

Is this tool implementation making sense to all of you?

1:1:55

No.

1:1:57

Is this tool implementation making sense?

1:1:59

to all of you?

1:2:00

Okay.

1:2:01

Similarly, everyone, we will implement another tool which is refund policy.

1:2:04

For refund policy, everyone, we will have to refer the policy lookup, right?

1:2:09

We'll have to do the policy lookup.

1:2:11

First of all, we'll have to check what is the type of, what do you say?

1:2:16

What is the type of request where it is, whether it is a refund policy, refund request,

1:2:20

or it is a shipping request, or it is a warranty request.

1:2:23

For that, we have written, I have written this one.

1:2:29

because there are a lot of tools that we're integrating.

1:2:33

That's why I am using the pre-written code.

1:2:38

So everyone, we are creating another base model class.

1:2:43

Okay.

1:2:46

This is from here.

1:2:50

This is a policy lookup input coming from base model.

1:2:55

The topic, everyone.

1:2:57

Topic?

1:2:58

No, literal.

1:2:59

Literal can take value refund, shipping, or warranty.

1:3:03

Then we are using is equal to feel that policy topic, this is the policy topic, may be one of these things.

1:3:11

Could you explain me this slide?

1:3:13

What is the meaning of literal?

1:3:14

And why we are using this here?

1:3:29

It is kind of tag.

1:3:37

Not really tagged.

1:3:38

Folks literal says that the topic value can be one of them.

1:3:42

If you try to give any other value, for example, if I try to give, let's say, delivery, it will not work because

1:3:49

literal says that the value of the topic can be one of these three values.

1:3:53

It can be either refund, it can be either shipping, or it can be either warranty.

1:3:58

warranty.

1:3:59

Clear?

1:4:00

It can be either one of them.

1:4:02

Okay?

1:4:03

And then everyone, we have the tool.

1:4:05

Again, we are taking topic in the input parameter and we are defining ARGs.

1:4:09

Is equal to policy lookup input.

1:4:12

A small comment here, look up company policy for refund shipping or warranty.

1:4:16

Use this tool when the user ask about the rules or eligibility or timelines or the company policy.

1:4:23

Right?

1:4:24

What we do?

1:4:25

JSON data format.

1:4:27

Okay is equal to.

1:4:28

this is the topic, this is the policy.

1:4:30

Make sense, everyone?

1:4:32

Now tell me everyone, here do we need to check whether the policy is present in the policy database or not?

1:4:38

Defund or shipping or warranty?

1:4:40

What if user passes something else apart from these three?

1:4:43

Do we even have to check this?

1:4:45

Here?

1:4:47

Do we check?

1:4:48

Do we need to check if the user is passing the correct policy?

1:4:55

Do we need to do that?

1:4:57

No, right?

1:4:59

Because we have already defined that in Pyrentic.

1:5:02

Pidentic will take care of that.

1:5:04

If you are providing a different value of policy, apart from these three,

1:5:08

Pyrentic will give you a validation error.

1:5:11

That is the idea of pirentic, right?

1:5:14

That is the benefit of pyrtic.

1:5:15

Folks, are you getting this point here or no?

1:5:18

Should we handle that error?

1:5:24

No need to handle.

1:5:26

Because Piedentic.

1:5:27

give you that, right?

1:5:28

Whatever error you are, like Pidentic gives you that validation error, right?

1:5:32

That if you provide, let's say, topic as general.

1:5:35

If that is not among these three, then Piedentic will give you a validation and saying that, okay,

1:5:40

topic should be among these things.

1:5:42

Okay, topic can only take one of these values.

1:5:45

Now let's write another tool, everyone.

1:5:50

Again, I'm writing this again.

1:5:53

Tool number three, create refund ticket.

1:5:56

About that, everyone.

1:5:57

Here, we are creating a base model class, we are creating a pidentic class, refund ticket input.

1:6:03

What all the things we need to create a refund ticket?

1:6:08

We need an order ID, which is of type string, we need a reason.

1:6:11

Reason is, a reason can be either damaged or late delivery, right?

1:6:16

Customer note, what customer is passing, right?

1:6:18

What, like, customer explanation, why they are asking for the refund.

1:6:22

Is the pyrantic base model structure clear to all of you, refund ticket input?

1:6:27

here.

1:6:29

Okay?

1:6:32

Right?

1:6:33

And then I will write the function to the refund ticket.

1:6:37

So this is going to be slightly bigger function, but very easy to go through this one by one.

1:6:47

Again, everyone, we are using the RX schema that input should follow this particular structure.

1:6:51

We are having the order ID, we are having the reason, we are having the customer node.

1:6:55

So, a small comment here.

1:6:57

create a refund ticket for an existing paid order.

1:7:00

Use this tool only when the user gets paid or file a refund request.

1:7:08

What we're doing?

1:7:09

Getting the order ID, getting the order details from the orders database.

1:7:13

If order is not present in the database, that means it is a order not found error.

1:7:17

We are returning this output.

1:7:19

If order, payment status is not paid.

1:7:22

If you have not paid for the order, then you cannot expect for the refund.

1:7:27

You cannot raise a ticket for the refund.

1:7:29

So what we are returning in the form of JSON?

1:7:31

Error type, payment not completed.

1:7:33

Cannot create a refund for this order ID because payment status is incomplete or whatever, right?

1:7:38

Payment is not completed.

1:7:39

Are these two if conditions making sense all of these?

1:7:42

If order not found and payment is not paid?

1:7:45

If payment is not completed.

1:7:48

Are these two if conditions clear to all of you?

1:7:52

Right?

1:7:54

books?

1:7:55

Yes, no.

1:7:56

Okay.

1:7:57

Then, everyone, we are returning, we are creating a ticket ID, some random ticket ID we are creating.

1:8:02

Okay?

1:8:03

Then refund tickets ID, if you see, refund tickets, okay?

1:8:06

So, folks, what we can do is we can create a refund tickets, dictionary.

1:8:12

Refund tickets as an empty dictionary.

1:8:14

As of now, there is no refund ticket initially, but what we will do, whenever we create a refund ticket,

1:8:19

we will give the ticket ID, what we have just created here, some random ticket ID

1:8:23

if one, then we will give ticket ID is equal to this, order ID is equal to this,

1:8:27

is equal to this, customer note is equal to this, status is equal to created.

1:8:31

This is the refund ticket that we are created, the sample database.

1:8:36

Everyone, clear?

1:8:41

And then everyone, everyone, we are returning some JSON data, that ticket created, and this is a message.

1:8:48

How many if you're clear with this sample tool for, tool?

1:8:53

Everyone, clear?

1:8:57

Is everyone here, yes or no?

1:9:05

Okay? And everyone, we will have to register all the tools, just creating a list of tools.

1:9:09

We have three tools as of now.

1:9:11

Get order status, lookup policy, and create refund ticket.

1:9:14

Correct?

1:9:14

We have to register all the tools in a list.

1:9:17

So that this list, I can pass to the model.

1:9:20

So that model will also know that these are the tools that we have.

1:9:27

Okay, okay, then you know, we will.

1:9:39

Okay, now we are done with almost half of the code.

1:9:42

Do you want to go through this code and take a break at this moment?

1:9:48

We are done with half of the code, almost half, more than half of the code.

1:9:53

I can comment.

1:9:57

Calling my heart.

1:10:27

Thank you.

1:10:57

Thank you.

1:11:04

I'm going to get here.

1:11:27

Okay.

1:11:57

Thank you.

1:12:27

Why this file is not?

1:12:57

Okay, I'll figure it out everyone. I think there is some problem in Git.

1:13:13

I think I'm managed of something.

1:13:16

Anyway, so I'm leaving this code on the screen.

1:13:18

You can have a look at it.

1:13:19

Then we'll see after the break.

1:13:21

6905 in 1.

1:13:22

Let's have a break.

1:13:23

Let's have a break of 1012 minutes.

1:13:24

It's made around 9.

1:13:25

Okay.

1:13:27

Thank you.

1:13:57

Thank you.

1:14:27

Thank you.

1:14:57

Thank you.

1:15:27

Thank you.

1:15:57

Thank you

1:16:27

Thank you

1:16:57

Thank you

1:17:27

Thank you

1:17:57

Thank you

1:18:27

Thank you

1:18:57

Thank you

1:19:27

Thank you

1:19:57

Thank you

1:26:57

Okay

1:27:01

Now,

1:27:04

Am I am I'm not

1:27:05

No,

1:27:06

No,

1:27:07

Now,

1:27:08

Now,

1:27:09

Now,

1:27:11

let's write

1:27:26

the next thing that is let's create the model.

1:27:29

To create the model, we will simply set, we'll create a model object like this.

1:27:35

Model is equal to Init chat model.

1:27:41

So this init chat model function is coming from, you can see that.

1:27:47

You can see that.

1:27:49

This is coming from Langchain.

1:27:51

dot model.

1:27:52

So this is the function that we can directly use to create the model.

1:27:55

And here, everyone, you just have to pass that for this particular chat model, which underlying model you want to use.

1:28:03

So model name, this is a model that we want to use.

1:28:07

If you want to pass other parameters like, let's say, other parameters are completely optional.

1:28:12

For example, if you want to pass temperature, right, that how you want your model to behave, let's say,

1:28:17

temperature is equal to 0 or 1 or maybe 1 is a good idea.

1:28:21

And other parameters, like if you want to have some limit or

1:28:25

limit on the number of what do you say limit on the number of tokens etc

1:28:32

and you can do that but for now let's just create a model with these two parameters

1:28:37

the model name and the temperature

1:28:40

what's good if you want

1:28:43

okay now folks what we need to do is we need to see in this model do we have the tools

1:28:51

does this model knows about these tools

1:28:55

Does this model knows about the tools?

1:28:59

Answer is no.

1:29:01

Right?

1:29:02

So what we need to do everyone is we need to find models with the tools.

1:29:05

Now there are two things that we can do everyone is.

1:29:08

Okay, let me go with the simpler one.

1:29:11

You can simply do model, give some name model with tools is equal to model.

1:29:16

Find tools.

1:29:18

Bind tools and you can define the you can give the tools here.

1:29:25

Is that point clear to all of you?

1:29:26

You can give the tools.

1:29:27

List of tools here.

1:29:28

Is that point clear to all of you?

1:29:30

Okay?

1:29:31

That's it.

1:29:32

Okay?

1:29:33

That's it.

1:29:34

Execute tool.

1:29:39

Okay?

1:29:40

Okay.

1:29:41

Okay.

1:29:42

Now folks, we will start in open the tools one by one.

1:29:48

We will write a function for that.

1:29:50

Execute tools.

1:29:52

Execute tool call safely.

1:29:54

Whatever names.

1:29:55

it is right let's try to focus on the implementation right what does

1:30:01

what this function does everyone is execute a model emitted tool call safely

1:30:06

instead of crashing the program right I will tell you that what is the meaning of safely here

1:30:12

example let's say you're making a call to the tool let's say database or make my trip

1:30:18

can that tool call fail can that tool call fail

1:30:24

Yes, tool call can fail for multiple reasons.

1:30:29

Tool call can fail for authentication issue because of rate limiting because of network failure

1:30:35

because of server goes down, etc.

1:30:37

If your tool call is failing, should you crash the entire application?

1:30:43

Should the entire application crash?

1:30:45

Ideally not.

1:30:46

So what you should do everyone is whenever you are making a tool call,

1:30:49

you should always handle the exception.

1:30:52

Like this.

1:30:54

should always use try catch blocks or try accept blocks while calling the tools here.

1:31:00

This is called as calling the tools safely.

1:31:03

Clear?

1:31:04

Calling the tools safely.

1:31:06

So what we are doing everyone is we will get the tool name.

1:31:09

Tool call.

1:31:10

What is this tool call?

1:31:13

I think this tool call.

1:31:15

This tool call is coming as of in the form of dictionary.

1:31:22

Just a second there you will.

1:31:23

they do it.

1:31:25

Passing this is the tool call.

1:31:28

Okay, got it.

1:31:45

So just wait for a few seconds.

1:31:47

You will get this what this tool call is.

1:31:49

And for now, you can just assume that this tool call is nothing but a dictionary.

1:31:52

dictionary.

1:31:53

Where all the tools are mentioned.

1:31:55

And this is the tool name.

1:31:56

This is the tool function name.

1:31:58

Okay.

1:31:59

So tool called.

1:32:00

Get whatever name you want to execute.

1:32:02

Okay.

1:32:03

Give the name of the tool.

1:32:06

Get the ID of the tool.

1:32:07

You will get the structure of this in a second.

1:32:10

Okay.

1:32:11

When we will write the next function.

1:32:12

Then we will

1:32:13

Okay.

1:32:15

Where this name is coming from.

1:32:19

Tool call name and I.

1:32:21

We will have to define the name here and we'll have to give the ID here.

1:32:26

Okay.

1:32:31

Okay, got it.

1:32:33

So guys, let's, if you see we have a list of tools,

1:32:36

let's create a tool by name for tools.

1:32:40

For each tool in tools, what we will do is

1:32:45

just iterate over this list of tools and what you can do is

1:32:50

creates a tools by name create an empty dictionary

1:33:00

and simply do what tools by name

1:33:06

tool dot name

1:33:10

so basically we are just creating a tool dictionary

1:33:17

okay so this dictionary will look like this

1:33:20

tools by name.

1:33:27

That what is the name of the tool?

1:33:29

Let's say ABC and the function.

1:33:31

Okay.

1:33:33

Let's say the name of the tool is get order status

1:33:37

and this function we need to call for get order status.

1:33:39

So this is the name of the tool.

1:33:41

This is the actual tool that you need to call.

1:33:43

So we are just creating a dictionary out of it

1:33:45

because some of the functions in Lanchine they expect dictionary.

1:33:48

Okay.

1:33:49

So,

1:33:50

This tools by name from this tool, from this dictionary,

1:33:54

we are getting the,

1:33:56

the first way, basically what we are doing everyone is,

1:33:58

this is the tool that we will need to call.

1:33:59

We will get the name of the tool,

1:34:01

we will get the idea of the tool.

1:34:03

Okay.

1:34:04

What is this tool called?

1:34:05

You will just get it when we will call this function.

1:34:07

Okay.

1:34:08

So we will get the name of the tool.

1:34:10

We will get the idea of the tool.

1:34:11

From this name everyone, we will get which tool we can call,

1:34:15

which tool we need to call from the dictionary of tools.

1:34:18

Give the tool name.

1:34:19

We will get the tool.

1:34:20

the name of the function.

1:34:21

Getting the point till this point of time.

1:34:24

Are these three lines clear?

1:34:26

Can we directly keep the tools in the dictionary?

1:34:29

You can do that.

1:34:30

Even this is not required.

1:34:32

This is not required.

1:34:34

But the point is, if I change this, I will have to change a lot of things in the code.

1:34:39

But definitely we can optimize this later on.

1:34:41

Okay, Nissan?

1:34:43

But yes, you can definitely find a better approach if that is visible.

1:34:47

Guys, everyone clear that we are getting the tool.

1:34:49

getting the tool with the name. What name of the tool?

1:34:52

From that name of the tool, we are getting the name of the function, which function we need to call.

1:34:56

If selected tool is none, then we will return a tool message.

1:35:00

What is this tool message, everyone?

1:35:02

Error type is equal to unknown tool that you are trying to call a tool which does not exist.

1:35:06

Tool is not available.

1:35:08

That's it.

1:35:09

Okay. Else everyone, if tool, the selected tool is a valid tool name, then what will you do?

1:35:15

You will just call selected tool.invoke.

1:35:18

So basically everyone,

1:35:19

this invoke function, where this function is coming from, any cases, where this invoke function is coming from?

1:35:28

This invoke function is coming from Adderate tool decorator.

1:35:32

When you decorate any function with this Adderate tool function or at the rate tool decorator,

1:35:38

then this becomes a Langthian component.

1:35:41

And every Langton component has an invoke function.

1:35:44

Remember, in the last class, when we executed this code, we used invoke function.

1:35:48

Use invoke function, chain dot invoke.

1:35:50

Remember, every Lanchine component has an invoke function.

1:35:54

And because this particular function, every function is, we are defining as a tool.

1:35:59

So this function, every tool will have an invoke function.

1:36:03

We will say that, okay, please invoke this particular tool.

1:36:06

We are putting this in the try block because tool call can break.

1:36:10

If the tool call fails for any reason, then we are expecting the error,

1:36:15

try and accept block.

1:36:17

In the except block, we are having to try and accept block.

1:36:18

having an error and then we are passing the tool message,

1:36:21

case on down dumps, what is the error we are getting,

1:36:24

and the message that we are getting in the error.

1:36:27

Is this making sense to all of you?

1:36:29

There's more, it will be more clear when we will actually execute this.

1:36:33

Okay?

1:36:34

And then everyone, we will add a manual feedback loop.

1:36:40

Then we will add a manual feedback loop.

1:36:43

This manual feedback loop, if you see this is nothing, but simple thing.

1:36:47

simple thing, run customer support agent, we are getting the query, and we are getting the customer, we are getting the maximum steps.

1:36:55

And how many times we need to execute?

1:36:57

Because a lot of times what happens everyone is, let's say if you are getting the query,

1:37:01

if you are not satisfied, you can again run the agent.

1:37:03

Again, you can run the agent if you are not satisfied with the response.

1:37:07

Correct or not?

1:37:08

You can keep on running the agent multiple times.

1:37:10

But ideally you should not be running the agent in finite number of times, right?

1:37:14

There should be some limit.

1:37:16

That is what we are defining here.

1:37:17

So what message we are giving?

1:37:19

The role is the system.

1:37:21

System means the agent or the application, the Langgen application.

1:37:24

And the content is that you are a helpful customer support agent.

1:37:28

You can use tools when you need to, when you need order data, policy data,

1:37:32

or when the user wants to create a refund ticket.

1:37:35

Are we clearly defining to the, are we clearly defining to the LLM,

1:37:40

giving the instruction to the LLM, in what all the scenarios you can use the tool?

1:37:44

Correct?

1:37:46

Yes.

1:37:47

You can use the tool to get the order information, order data, policy data, or when you want to create a refund ticket.

1:37:53

If a tool returns an error, explain the issue clearly and ask the user for the missing or corrected information.

1:38:00

This is the system prompt that we will give to the system.

1:38:03

Then if you want, this is the user query, that's it, what is coming in the input parameter.

1:38:08

Clear? Is the message clear to all of you?

1:38:11

Right?

1:38:12

The message from the system from the user.

1:38:14

Then if you want, we will execute this loop five times,

1:38:17

maximum five times, then AI message is equal to model with tools.

1:38:21

What is this model with tools?

1:38:23

This is the model object that we created after binding the tools.

1:38:26

Correct, everyone?

1:38:27

So, we are giving the messages here.

1:38:30

Now, can I say that this is what LLM will execute?

1:38:33

Correct or not?

1:38:35

This is what LLM will execute.

1:38:37

And LLM will give you some message.

1:38:39

That message, everyone, we are appending to the messages array.

1:38:42

So, we are just printing the content of the message, etc.

1:38:46

And now everyone what happens is, in AI message,

1:38:51

AI message, like this is just a output everyone.

1:38:53

You can call it as response also, whatever you want to call it as.

1:38:56

Just for simplicity, we are calling it as AI message.

1:38:59

This is just the name of the variable.

1:39:01

In this AI message, everyone, there will be multiple pointers.

1:39:04

One is the content.

1:39:05

What content tool is written?

1:39:07

What content LLM is written?

1:39:09

But everyone, based on the user query,

1:39:11

can LLM also decide which tool to call?

1:39:15

Okay?

1:39:16

that you are printing here if LLN is deciding some tool to call.

1:39:19

If there is no tool call,

1:39:21

can I directly return the content of the message,

1:39:23

content of the response?

1:39:25

Yes.

1:39:26

If not, if there is a tool call,

1:39:28

then we will iterate over the tool call because everyone see.

1:39:32

If you want, let's say if you give a query life,

1:39:36

please raise a support ticket for this order ID.

1:39:39

Correct?

1:39:40

Please raise a refund request for this order ID.

1:39:43

Now, will you directly

1:39:45

start, will you directly call the agent or will you directly call the tool

1:39:50

to raise the refund request?

1:39:53

No, right?

1:39:54

First you check the order status, right?

1:39:56

Then do raise the, then you call the tool to create the refund ticket.

1:40:00

So don't think ever, in that case, there will be two tool calls.

1:40:03

So tool calls will have two parameters here.

1:40:05

We'll have two values here.

1:40:07

So you will execute tool one,

1:40:09

then whatever message you are getting appending to the message,

1:40:12

and then this is the tool content and the tool message.

1:40:14

the tool message.

1:40:15

So you will execute all the tools one by one.

1:40:18

Because LLN can decide more than one tool to call.

1:40:21

Correct or not?

1:40:23

There may be more than one tool to call.

1:40:26

There can be one.

1:40:27

There can be more than one.

1:40:28

If there is no tool to call, we will directly return the content.

1:40:31

Folks, yes or no?

1:40:35

Else we will return the simple thing.

1:40:40

I could not complete the request within the allowed number of steps.

1:40:43

So what you will do, everyone, you will execute this loop five times.

1:40:46

If you still cannot return the response within these,

1:40:49

could not return the response within these number of attempts,

1:40:52

you will simply return that I could not complete the request within these very price.

1:40:57

Okay?

1:40:58

And then everyone we will execute the query like this.

1:41:01

Okay?

1:41:02

So we will have a list of queries.

1:41:04

Okay.

1:41:05

So we have five queries.

1:41:06

Where is my order ID?

1:41:07

Can I get a refund?

1:41:08

Create a refund request?

1:41:10

Create a refund ticket.

1:41:11

Tell me a joke about databases.

1:41:12

These are the five.

1:41:13

queries that we have or six queries, right?

1:41:15

Five queries.

1:41:17

So we will test all of these one by one.

1:41:20

Clear?

1:41:21

Everyone clear?

1:41:24

Yes or no?

1:41:25

And then everyone, we will iterate over all of these queries.

1:41:29

Okay?

1:41:30

Then we will print equal to just a separator.

1:41:33

Then this is the query.

1:41:34

This is the final answer.

1:41:36

Print the final answer.

1:41:38

Okay?

1:41:39

So let's try to understand everyone.

1:41:41

Let's try to execute.

1:41:42

And then we will again walk through the complete code.

1:41:46

I will again walk you through the complete code.

1:41:49

So one is we will run now Python 3.

1:41:53

I have not B.M.

1:41:56

No such a file or death.

1:42:01

I'll check two.

1:42:03

There is one problem and one.

1:42:08

This is not written in I signal.

1:42:11

The problem.

1:42:12

Not home.

1:42:31

You can over answer.

1:42:33

I think there are some different.

1:42:41

We have this.

1:42:42

and here we can do

1:42:44

It's gone.

1:42:46

It's gone.

1:42:47

It would actually open here.

1:42:49

Okay.

1:43:06

Now the code is running.

1:43:11

Okay.

1:43:12

See everyone.

1:43:13

So the code is running.

1:43:14

Let's wait for the response.

1:43:16

So if you see the first user query, this is the user query.

1:43:19

Then everyone if you see for what is, where is my order ID?

1:43:23

Where is my order ID this?

1:43:25

What is the model response?

1:43:27

Step 1 may tool call?

1:43:28

Make this tool call.

1:43:30

Getting the point.

1:43:31

Which tool, which LLM we are using everyone?

1:43:35

Which LLM we are using?

1:43:37

Folks, we are using GPT.

1:43:40

Correct?

1:43:41

So GPT is able to.

1:43:42

to identify which tool to call.

1:43:44

Then what is the tool response?

1:43:46

This is the tool ID, random tool ID we are giving.

1:43:49

Right?

1:43:50

And then everyone the content is order ID, this item is wireless mouse

1:43:53

because we are making a call to database

1:43:55

and we are getting the order ID, the data of order.

1:43:58

Then step number two, right?

1:44:01

In step number two, everyone, what are we doing?

1:44:04

In step number two, what are we doing?

1:44:06

If you see, where is my order ID?

1:44:11

we are refining the response okay just one thing everyone

1:44:18

step number one step number two and

1:44:23

as well I can get the response

1:44:25

here and any

1:44:27

phone calls we have

1:44:32

where we are making step number one

1:44:35

not really one

1:44:37

and actually let's do one thing let's do one thing

1:44:40

just make

1:44:41

just print also

1:44:43

print

1:44:45

toll calls

1:44:47

okay

1:44:49

Toll underscore

1:44:50

How many tools

1:44:54

A.I.Message

1:44:55

is telling us to call

1:44:56

Okay?

1:44:57

Now go to the terminal

1:44:59

execute this again.

1:45:00

Actually let's do one thing even let's not execute

1:45:02

this for five queries directly

1:45:04

Let's execute this only for one query first

1:45:07

So that it will be easier for us to understand.

1:45:10

understand.

1:45:11

Okay, everyone.

1:45:12

We are just executing this for one query for a number.

1:45:15

Okay.

1:45:16

Execute this.

1:45:17

So this is the user query.

1:45:28

See.

1:45:29

For this user query, everyone, what do you think?

1:45:31

For this user query, how many tools we need to call?

1:45:36

How many tools we should call?

1:45:39

only one tool, right?

1:45:46

Because user is only asking about order ID.

1:45:49

So which tool we are calling?

1:45:52

Which tool LLM is recommending?

1:45:55

LLM is just recommending to call get order status, correct?

1:45:59

Cooks, yes or no?

1:46:03

Correct?

1:46:08

So, we are.

1:46:09

We are calling this particular tool.

1:46:11

Guys, yes or no?

1:46:13

Are you guys understanding this point or not?

1:46:15

No response in the chat.

1:46:17

Okay? So only this tool LLM is recommending,

1:46:22

then LLM will, we will make this tool call.

1:46:25

And after we make this tool call, everyone, we are getting the order status.

1:46:28

Order information, correct?

1:46:29

We are getting the order information.

1:46:31

Now we will tell me if there is only one tool

1:46:34

LLM is recommending,

1:46:35

how many times this particular loop will execute?

1:46:38

loop will execute it.

1:46:40

How many times this particular loop will execute it?

1:46:44

Only one time.

1:46:45

Because there is only one call, LLM has recommended.

1:46:48

So you will only execute one time.

1:46:50

And in the second step, right, in the second step, we will get the final response.

1:46:55

So if you see, in step number two, this is the model response, the content is this.

1:47:02

And if you would like to tell your CT etc., this is the data that we are generating in the tool.

1:47:07

And this is the final response.

1:47:08

response.

1:47:09

So do you see that everyone?

1:47:10

LLM is able to identify which tool to call based on the query, automatically.

1:47:15

Correct?

1:47:16

Can you identify how LLM is able to do so?

1:47:21

Because everyone if you see, first of all, are we using a good LLM?

1:47:25

Yes, we are using GPT, GPD 5.2, which is very powerful.

1:47:30

Tell me everyone, if we give the query to the GPT and if we give the tool names to the GPT,

1:47:37

Will GPT be able to decide that which tool should I call for what type of query?

1:47:43

If you are asking a refund query, do you think that probably LLM will decide this tool to call on a high level?

1:47:52

Until or unless it specifically needs that.

1:47:55

Not really.

1:47:56

For refund, LLM will understand that this tool we need to call.

1:48:00

For order status, this tool we need to call.

1:48:02

Now let me show you something more interesting.

1:48:04

So now what we will do everyone is, instead of giving this question,

1:48:07

where is my order with this ID?

1:48:10

Let me give this thing.

1:48:12

Can I get a refund if my...

1:48:14

or create a refund ticket for this because the item is damaged?

1:48:18

Yeah.

1:48:19

Let's give this query.

1:48:20

Can I get a refund of my item if it is damaged?

1:48:23

Let's say this is the query that we have.

1:48:25

Okay?

1:48:26

Now let's try to execute.

1:48:28

Now just see, this is the user query.

1:48:36

user query. Now, LLM will decide which tool to call. Let's see which tool LLM decides.

1:48:43

Which tool LLM should decide everyone for this query. What do you think? To check, to check first

1:48:52

of all, policy. Look up policy, right? First of all, we should check the policy, right? Guys,

1:48:58

now don't you think based on the policy, then LM can decide that whether we should call the refund ticket or not.

1:49:05

Correct or not?

1:49:07

Correct, so first it will call the lookup policy, right?

1:49:12

So this is the lookup policy and tool result is, okay, true, topic is refund.

1:49:17

Policy says what?

1:49:18

Refunds are allowed within seven days of delivery for damage or wrong products.

1:49:23

Okay?

1:49:24

Then what is the model response, everyone?

1:49:26

Yes, if your item is arrived damaged, you are eligible for a refund.

1:49:30

This is the response that we are returning to the user.

1:49:33

Now, if you see everyone, we are waiting for.

1:49:35

or we are asking the user, if you want, I can open a refund ticket.

1:49:38

Please share your order ID, example, this.

1:49:41

If you see everyone, this is the, this is coming from description.

1:49:44

Please share your order ID and a brief note.

1:49:48

Correct. And this is the final response.

1:49:50

Is this working as expected or not?

1:49:55

Folks, are the tool call, are we making the tool calls specifically or not?

1:50:01

Let me show you one more example now.

1:50:03

Let's say.

1:50:05

Let's change the query a bit.

1:50:07

And let's say we are having create a refund request for this user.

1:50:11

Create a refund ticket for order ID this because item is damaged.

1:50:15

For the LLM to identify the right tool, should we name the tool correctly?

1:50:30

Absolutely.

1:50:31

It is very, very important.

1:50:32

If you don't name the tools correctly, then,

1:50:35

LMs can mess up.

1:50:37

Okay.

1:50:42

So everyone, create refund ticket.

1:50:43

This is the tool that LLM is calling right now.

1:50:46

And finally, even, you will be able to see the refund ticket as well.

1:50:48

It will generate the refund ticket.

1:50:51

And as of now, we are not printing the refund ticket array or dictionary.

1:50:55

We can print it out, right?

1:50:57

And you will be able to see that.

1:50:58

The ticket is getting created.

1:51:00

Right?

1:51:02

This is the code, everyone.

1:51:03

I hope this code is clear to all of you.

1:51:04

is clear to all of you.

1:51:05

Now I can comment it out.

1:51:08

In fact, let me change the name of this application.

1:51:11

Let's say rename this.

1:51:14

Langchain tool.

1:51:17

Tools.

1:51:31

P-Y.

1:51:32

Okay, this is the code for today's class, everyone.

1:51:38

Can you see, can you see the code now?

1:52:02

This is the code file for today's class.

1:52:13

Can all of you see that?

1:52:16

Now everyone, this is what we wanted to discuss for today's class.

1:52:19

Now I think there is very...

1:52:21

Now, one more thing, everyone, for each and every line of code, whatever we have done in the class,

1:52:27

whatever I have explained to you in the class, everything, every line of code,

1:52:31

every line of code I have explained in maximum possible detail in the notes.

1:52:36

Is that point clear?

1:52:38

Every line of code.

1:52:40

Whatever, like what bind tool is using, what is tool message, what is AI message,

1:52:44

how we are making the tool call, what is the use case of this array,

1:52:48

what is the use case of add the date tool annotation, everything I have added in the notes.

1:52:53

Okay?

1:52:54

Folks clear.

1:52:56

Now just the last part for today's class, everyone, just

1:53:00

a few things. Now we have a bit of theoretical part that what all the things we should take

1:53:07

care of while writing the tools.

1:53:10

Let me share my iPad screen now.

1:53:13

Is my iPad screen visible to all of you?

1:53:18

Okay.

1:53:20

So guys, there is something called as error, error containment patterns.

1:53:29

containment patterns.

1:53:36

What are these patterns, everyone?

1:53:38

That how do you basically tackle the errors, right?

1:53:42

Right?

1:53:43

How can you avoid the errors or if error happens, how can you tackle them better?

1:53:47

Because in production environment, you'll have very big langchain applications or Langraphs or any

1:53:52

agentiki applications.

1:53:53

So how will you make sure that if error happens, how can you rectify that easily?

1:53:58

First pattern.

1:53:59

everyone, it says that, that you should always return structured error objects.

1:54:06

Return structured error objects.

1:54:23

Did you see that in the code when there was an error, were we returning proper error message?

1:54:28

upper error message, status, true, false, good, bad, etc.

1:54:35

This is how bad or good error message looks like.

1:54:39

If you just written something went wrong, is it actually explaining that what went wrong?

1:54:44

No, it is a very general message, right?

1:54:49

It is a very general message, something went wrong.

1:54:51

It is not a very good way.

1:54:53

So ideally you should send more details to the user so that we can,

1:54:58

identify that easily. What went wrong? This is first pattern. Everyone clear?

1:55:03

Very well understood, simple thing, right? Correct? Second thing everyone is that we already saw

1:55:11

in the code as well, that we should always catch tool exceptions. As we saw in the code,

1:55:18

that whenever you are calling a tool, you should never make a call to the tool directly.

1:55:23

Always enclose that in a try-catch block. So that if error happens, you know, you are calling a tool, you should never make a call to the tool directly.

1:55:28

You can catch it. Correct? If you see, we did something like this in the code.

1:55:36

See? Let me copy paste this. Did we do something like this? That instead of directly making a call to the tool, we added tri-catch block.

1:55:46

So that even if tool calls, you can handle that scenario.

1:55:52

Correct? This is a second pattern. Third pattern, everyone is, validate in third pattern.

1:55:58

parameters before calling the tool. Valid arguments or input.

1:56:11

Before calling the tool.

1:56:17

Validate arguments.

1:56:21

Correct?

1:56:23

Everyone clear?

1:56:25

So I think this is, we have done via Pidentic.

1:56:27

pidentic.

1:56:28

Fourth pattern says that everyone, keep the tools minimal.

1:56:40

What does that mean, everyone?

1:56:42

If you think that there is a tool which is becoming very big, right?

1:56:46

There are a lot of functionalities you are adding in the same tool.

1:56:49

Try to divide that into multiple tools.

1:56:52

So that in future, if any error happens, you can rectify that easily.

1:56:56

If there is a tool with, let's say, 1,000 lines of code, definitely it will be very difficult

1:57:02

for you to identify if something goes wrong inside that tool.

1:57:06

Correct? Correct.

1:57:07

So always try to keep the tools minimal and deterministic.

1:57:12

So that you can determine what is going wrong, what is going right, etc.

1:57:16

It is called as deterministic.

1:57:26

Also, everyone, you should always put a limit, right, on output size of the tool.

1:57:35

Limit, tool output size.

1:57:42

What does that mean, everyone?

1:57:44

Tool output size means that, that don't try to return so many things from the tool.

1:57:52

Because everyone, if tool returns a lot of data, don't you think tool will automatically become

1:57:56

come a bit slower?

1:58:01

Correct or not?

1:58:01

Yes.

1:58:02

So that's why everyone, to make sure that the cost is efficient, the latency is not very high, right?

1:58:07

You should always make sure that tool is only returning important data.

1:58:12

Tool is not returning some redundant data.

1:58:16

Clear, everyone?

1:58:21

Okay.

1:58:23

Then everyone, there is a small thing.

1:58:26

that is the part of today's class, which is diagnosing, diagnosing, tool selection.

1:58:51

And argument false. What is the meaning of this? Very simple, which we have already seen while writing the code.

1:58:55

Okay.

1:58:56

Who decides which tool to call?

1:59:13

LLM?

1:59:14

So if you see everyone inside LLM, the message that you are giving to LLM, please make sure that

1:59:20

you are giving a proper description there and you are telling LLM very, very clearly that you

1:59:26

have to call the tool in these, these scenarios.

1:59:29

If you see everyone, see the content.

1:59:32

You are a helpful support agent.

1:59:34

Use tools to call, use tools for these, these use cases.

1:59:40

Getting the point.

1:59:41

If you want to get the order data, if you want to get the weather data, if you want to get the policy data,

1:59:46

if you want to book a flight, if you want to send an email, use these tools.

1:59:50

Correct?

1:59:51

So that everyone, LLM will not try to generate the data for end.

1:59:56

any of these use cases. If LLM will try to generate the data for these use cases, don't

2:0:02

you think that will fall under the category of hallucination? Correct? LLM will try to generate

2:0:08

some order data, some policy data, some random things, right? LLM should not do that. For these

2:0:14

kind of scenarios, we need to tell LLM very, very clearly that please don't do things on your

2:0:20

own for these scenarios. Please make a tool call. Use the list of tools that we have given to you.

2:0:26

or not? This is what is called as everyone, diagnosing tool selection. So LLM

2:0:31

should be able to select the tools correctly. Okay? And everyone, always before making your application

2:0:39

what do you say, live, making your application in the production, please make sure that you're

2:0:45

testing your application on at least like 10, 20, 30 test cases. That for these, these

2:0:51

scenarios, is my LLM or is my overall application working fine? Is the correct?

2:0:56

tool calling happening? Is my LLM recommending the correct tool? Is my application

2:1:01

calling the correct tool or not? Are you guys getting this point? Also one more thing,

2:1:08

everyone, because you are giving the entire access to the tool, right? And you are using at the rate

2:1:15

tool annotation. So whatever message, whatever tool description you are providing, right?

2:1:21

Sorry. One second, everyone. Let me show you the code once again. Right. So, guys, so guys,

2:1:26

for every tool, you are using at the rate tool annotation, correct? For example,

2:1:31

this one, you are using at the rate tool annotation. So whatever, now, how tool selection is

2:1:39

done by LLM? One thing is definitely the name of the tool. That's correct. Also, everyone,

2:1:44

LLM can also access this tool description. Are you guys getting this point? LLM can also

2:1:50

access this tool description. How? Because this tool description, everyone, automatically

2:1:56

goes via at the rate tool annotation. So, when you give the name of the tool to the LLM in

2:2:03

the list of tools, LLM can access the tool description. If you provide a wrong tool name or a wrong

2:2:09

tool description, then LLM may get confused. So that's why it is very important for us to give the

2:2:15

correct tool name and the correct tool description. Otherwise, LLM may recommend wrong tool.

2:2:23

LLM might get confused.

2:2:25

Clear, everyone?

2:2:26

Okay, I think that's it. And wrong arguments, everyone, definitely. There is a very,

2:2:33

very high possibility that user might give wrong arguments that we have already seen, that we have

2:2:41

already catered via Pyrintic. Okay? Don't forget to use Pidentic in, in production application,

2:2:48

because user can provide wrong input parameters and your application should be able to

2:2:53

validate them automatically via Pyrintic.

2:2:56

Okay. One more thing, everyone, that when we make a tool call, when we make a first call to model or LLM,

2:3:08

LLM tells us which tool to call. Then we call the tool. Then we get the response. Should we directly

2:3:14

return that response to the user? We make a LLM call. LLM gives the tool name, which tool to call.

2:3:21

Then we make a tool call. We get the response. Should we return that response as it is to the user?

2:3:26

to the user? No, right? We should again pass that response to the LLM to generate a user-friendly

2:3:34

response. See, which tool to call? Call the tool. Whatever tool result we are getting, pass it to

2:3:41

LLM. And then generate the response in a user-friendly way. Getting the point? Generate the response

2:3:47

in a user-friendly way. Clear or not?

2:3:56

Okay? So, guys, these are all the things that we wanted to discuss for today's class. I hope

2:4:02

everyone is clear. How many of you are clear with all the things that we discussed today?

2:4:08

Major thing was code. If you can understand, if you have understood the code, if you have missed

2:4:13

anything inside the code, everyone, no worries. Just go through the code and go through the notes.

2:4:18

In the notes, everyone, I have added each and every line, explanation of each and every line

2:4:23

inside the notes. Whatever we have discussed, even like more details about that,

2:4:28

we have added in the notes. So let me upload the notes on GitHub.

2:4:53

Folks, can you see today's class notes?

2:5:00

This is the link, everyone.

2:5:01

Can all of you access the notes? Can you please check?

2:5:19

check now, Wamsi, always the notes are accessible within few seconds because it is a heavy,

2:5:25

heavy PDF. So it takes a few seconds of time for GitHub to process, to upload. Okay, now access.

2:5:34

It should be visible now. Just refresh the page.

2:5:46

Okay.

2:5:47

Okay.

2:5:49

Before we launch the feedback poll, everyone clear with all the agenda points for the today's class.

2:5:54

Also, let's mark what all the topics we have covered in today's class. That is also important.

2:6:15

Okay. Can everyone see my screen? Which screen?

2:6:19

I don't know which screen is visible. It is not showing me.

2:6:36

Anyways, let me share it again. Yeah. Now. Okay. So everyone, what we will do is see,

2:6:43

what all the topics we have covered? Author, Langchain, native tools and with typing and description. Yes, we have

2:6:49

done that. Model emitted structured tool outputs, tool calls, and relate them to intended

2:6:55

runtime behavior, yes. Orcastrate, orchestrate a manual tool feedback loop that arrives at a coherent

2:7:02

final model. Our tool call is also expecting the user input at some point of time to create the refund

2:7:08

ticket, etc. Error containment patterns done. And then diagnostic, diagnosing also is done, the topic that we

2:7:16

discussed at the end. Just simple thing, that how can you make?

2:7:19

make sure that your tool call is correct. Your LLM is able to select the correct tool.

2:7:24

Okay? GitHub is showing 404. Guys, I can access the notes. See. I think the notes are pretty big.

2:7:41

That's why it might be taking time. See, I can access the notes. Okay. Maybe wait for a few

2:7:49

seconds, it should be visible. Okay. So if feedback poll is in front of you, please

2:7:58

take the feedback poll. We are done with the class. Feel free to drop off once you, once you fill

2:8:03

the feedback form. Thank you. Have a good day. Take care and bye-bye.

2:8:19

Thank you.

2:8:49

Guys, not sure why we are getting one or two rating today. Was the class bad? Was the class that bad today? I think we have got one, one rating, one, two rating. If there is any feedback, do let me know in the comments.

2:9:09

Guys, if you have any feedback related to Zoom or audio or anything, I think this is not the right feedback poll. The feedback poll only

2:9:19

about the session, about the instructor. Okay?

2:9:27

If you have given one rating, two rating, for any tech issue, you can let me know. Is that the case?

2:9:42

Folks, please let me know because it is, like, it is monitored. Okay, as an instructor for me, it is important.

2:9:49

Shantanu, can you please tell me? Is it because of the tech issue?

2:9:57

And guys, if you have given one, two, three rating only for the tech issue, do let me know. So that

2:10:01

at least I let the team know. Okay. What about other people? Shantanu has mentioned that clearly. Thank you for

2:10:12

that, Shantanthu. What about other people?

2:10:19

Folks, that's not the right thing.

2:10:22

If, please let me know, if there is a feedback, this feedback is regarding the technical things or technical issues that we faced in the class.

2:10:32

For example, some people were, some people were not able to join the class via Zoom link.

2:10:38

Then there was an audio issue.

2:10:40

Is it because of that?

2:10:49

Okay, then, okay. Anyways, thank you. Thank you. Thank you. Bye-bye. Take

2:11:03

and have a good day. See you in the next class.

2:11:19

Thank you.

2:11:49

Anyone if left to vote in the poll, please do that

2:12:07

please do that.

2:12:19

Thank you everyone for joining. Thank you, sir. We'll meet again on Friday for the tutorial. If you have any doubts, please food free to join.

2:12:49

Thank you.

2:13:19

Thank you.

2:13:49

Thank you.