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

Thank you.

4:54

Thank you.

5:24

Thank you.

5:54

Thank you.

6:24

Thank you.

6:54

Thank you.

7:24

Thank you.

7:54

Thank you.

8:24

Thank you

8:54

Thank you

9:24

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

Thank you.

9:46

Thank you.

10:16

Thank you.

10:46

Thank you.

11:16

Thank you.

11:46

Thank you.

12:16

Thank you.

12:46

Thank you.

13:16

Thank you

13:46

Thank you

14:16

Thank you

14:18

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

Thank you.

14:38

Thank you.

15:08

Thank you.

15:38

Thank you.

16:08

Thank you.

16:38

Thank you.

17:08

Thank you.

17:38

Very, very good evening

17:48

just waiting for everyone to join in all of you.

17:53

So we will just be starting out here.

18:08

Thank you.

18:38

Thank you.

19:08

Thank you.

19:38

All right, folks, so let us start on here and just to clarify the context in terms of where we are and what all we have done as part of our journey until now.

19:48

So this is where we are after we wrapped up module 1, Python and module 2 machine learning.

19:54

We are in the four generative AI agents module.

19:59

So we have done quite a lot until now.

20:01

We have explored basic prompt engineering.

20:04

We have also explored, you know, how we build

20:08

drag systems, retrieval augmented generation. We talked about the React framework with respect to agents. And we also talked about other things in terms of rate limiting, prom versioning and other things. Okay. And today's session, it will be, again, a slightly different kind of a session. So it's not a not exactly a very core generative AI related topic, but yes, it is very relevant with respect to whatever we have done so far and whatever we will do going forward. So this session is kind of

20:37

a very related session, I would say. But yes, it will not be related to agents and all that here. But yes, it is very related session to what we will see.

20:45

It is more about the JSON schema. So whatever we have been doing until now, if you see, you know, we were writing a prompt. We were writing a very detailed system message. And on the basis of that particular prompt, on the basis of that particular system message, we were generating a response. Okay. Now, today's session will be more about how we can generate that response in a more accurate way.

21:06

and how we can write a prompt in a better way and why it is so important to have a very structured response.

21:13

Because so far we did not have that conversation.

21:16

So far it was more like, okay, you know, you output something, you output some, you know, you give some system message, right?

21:22

But it's very important for that output of a language model to be in a particular format, in a particular schema.

21:28

And today's class is more about understanding the whys of it.

21:31

Why is it important for that outputs to be in a structured format?

21:35

why it is important to have a structured output for agents. That is what we will see.

21:41

And we will also discuss some mechanisms for doing that. How do we define the JSON schema? How do we

21:46

incorporate it? So we can see that overall. Right. And as I told you, as we do this particular

21:51

session, you can very nicely connect the dots back to whatever we have covered before,

21:56

whatever we have talked about until now, and obviously whatever we will see going forward.

22:00

So very, very important things. Because one important concept is one important.

22:05

If you look at it from a overall course perspective, where this session actually is very important is,

22:12

the output of a generative AI application and whatever applications we have seen so far, if you relate back to the Tesla demo and there's so many other use cases we saw, like the medical notes assistant, you know, like that use case where you are out inputting medical notes and the language model will parse that information and.

22:35

try to generate structured content out of it. Like what is the age, what is the diagnosis,

22:41

what is the gender. So if you look at it in this context, every time the application is outputting

22:48

something, which we are just printing out in Python and we are just seeing, okay, what is it outputting.

22:53

But in the real world, that will not always be the case. So the output of a LLM application may not just

23:00

be displayed. The output of a LLM application may just go to another application.

23:05

as an input. So what I'm getting at is the output of one LLM application might just be the input to another application. That is what's going to happen. So whatever output the application gives you will just be the input to another application. And that's the way how the whole thing is, and that's exactly where the session fits in. Just to help you connect the dots with respect to what I'm talking about. I'm going to take you back to the class notes file. This is the same, you know, you know,

23:35

use case we have done before. Everybody understands this story.

23:38

System message, user message, how we write a prompt. And if you remember this particular use case, we,

23:43

you know, we covered in detail. All of you can take a look at it. And what I will do right now is I will just go ahead and let me just run this

23:50

for a minute. Okay. Let me just execute this code for a minute. We've already seen this. We've already done this before.

23:57

So it's not new. And just as a small recap, everybody can just give it a read once. You can just read the system message.

24:04

All of you give it a read one.

24:05

just so that you can, you know, let's just kind of remember the use case once again, whatever we do. This is the same

24:11

medical notes assistant use case that we already discussed. Okay, you're an assistant to a hospital

24:16

administration and your objective is to basically generate. What is the objective? Your objective is

24:22

to generate the medical, you know, extract information from the medical notes. So we are clearly

24:29

stating the things in the system message that, okay, you will be given the medical notes as input.

24:35

And from the medical notes, you please extract relevant information out of it in a JSON format.

24:41

Right? See, we are doing it in a very open-ended way. We just giving it in a very open-ended way that please, from this particular, whatever, you know, medical notes are given to you.

24:54

You please try to extract the information in a JSON format. And we are also explicitly stating the age, gender, diagnosis, weight, and smoking.

25:02

This is the thing. This is one way we have done this.

25:05

Let me, let me clarify a slightly different proposition to all of you.

25:12

Let me clarify a slightly different, you know, a slightly different proposition to all of you.

25:16

What if we had done this in a slightly different way, right? For a minute, let's say, I'm going to create

25:23

a new cell here. For a minute, let's say the system message was written this way, right? Let's say,

25:27

you know, I will not, I will not mention JSON here. This is the demo, right? I will not mention the word

25:34

Jason here. Okay? And I will just say that okay, you're an assistant to a hospital

25:42

administration team. Medical notes will be given to us input. Please expect relevant information

25:47

as mentioned below. That's it. You're just giving it this way. That's it. You're just saying age

25:52

and you're not giving any other information. Age, gender, diagnosis, weight and smoking. I think you can

26:03

immediately understand the difference in the prompt now. In the, in this particular

26:08

system message, you're, you're keeping it very open in it, right? And if you, if you remember

26:14

the use case we discussed in our session, what is the use case for what we are trying to do here?

26:20

This is not just a simple print statement, right? So the end application will not just display

26:28

the results. Here for the demo, yes, I'm just showing you that, okay, the results will be displayed this

26:33

way. But this is not how we want the results to be. Ultimately, we want the information to be

26:40

extracted from your medical notes and we want that to be eventually saved back in a table, a database

26:48

table. That is what we want, right? We want to extract the information from the medical notes, right? I repeat

26:57

again, we want to extract the information from the medical notes. And after we extract the information from the medical

26:59

notes. And after we extract the information from the medical notes, we want to eventually

27:05

save it back in a Pandas data frame or a table. If you remember, this was what we talked about. You want

27:09

to eventually save it back in a data frame or you want to write it back to a SQL table. So we are

27:15

taking that unstructured data and we are eventually saving it in a structured format. So my point is

27:20

that this is the real world how LLM applications are working today. It is not just that you write a prompt

27:28

and the application will give an answer that somebody will see. No, somebody may not necessarily

27:31

see this. But when you give the medical notes as input, it will extract the information out of it

27:37

and you want to eventually save it back in a database table. Hence, it is extremely important.

27:43

The formatting is given importance to it. And everybody has done SQL in your module 1.

27:49

At a basic level, all of you know. Everybody knows Panta's data frames, obviously.

27:54

And you all know and you all appreciate that if we have a

27:58

a smoking column. Smoking can be either yes or not, right? It cannot take any other value.

28:04

Can we enforce those constraints. Now, whatever output the language model is generating,

28:12

how do you ensure that those constraints are enforced? That is what today's session is about.

28:20

See, like for example, if I, if I go back and give this kind of a system message,

28:23

it is very open-ended, right? See, you give it some medical note.

28:28

And this is a zero shot prompt. The language model will analyze those medical notes and it will

28:35

try to extract some information out of it. What is the information? It will extract information like,

28:40

okay, what is the age, what is the gender? What is the diagnosis? Smoking? The answer to this question

28:46

could be, okay, it is not necessarily yes or no, but let's run it. I think once we run it,

28:50

we'll get some idea. Let's run the code and we will start to see the answer. Look at this. See,

28:54

current smoker. See this. Interesting. Right.

28:58

Look at the answer. I'm getting. Now, the problem is that, the problem is that my system message was very

29:06

linear. I did not enforce any conditions. I did not enforce a specific defined schema. And that is why

29:16

the language model was able to generate a more open-ended response. The smoking came out to be current smoker.

29:21

Hey, what is the problem with this guys? I'll tell you the problem with this.

29:25

And it is another interesting thing. The weight came.

29:28

out to be 80 KGs. The age came out to be 35 years. What is the problem with this? Can you save this

29:38

back in this particular Panda's data frame or a database table? Let me, let me hear from the audience here.

29:44

What is what do you think is the issue here right now? System message was very open-ended,

29:48

very lenient, right? And because of that, this is the answer I got. We are not debating the answer.

29:53

Answer to say it. Answer may no problem. Answer is absolutely correct. The problem. The problem. The

29:58

The problem is that when you want to take this output and save it somewhere else, you want to save it back into a data frame or you want to save it back in a database table.

30:08

The issue is that in that situation, you will be getting errors.

30:15

Because you can clearly see my data frame right now is accepting what? Look at my data frame. It is accepting integer values, right?

30:23

The weight column is accepting integer value. The age column is accepting integer value.

30:28

So, there is a certain defined format in which my data has to be.

30:32

That's the whole idea of a Pandas data frame, right? It's like a table. And the table will have

30:36

different columns and different columns will have data types. All of you know this. The story remains

30:41

the same when you want to eventually write it to an SQL table also, right? If you want to write

30:46

it to a SQL table also, the story remains the same. In a proper database, different

30:54

columns will have different data types, right? So,

30:57

the age column might have a data type integer. The weight column might have a data type integer.

31:03

The smoking column will have a data type string. But the problem is if you see, right, weight 80 and 35

31:08

we can store, but here the weight is coming out to be 80 kgs. I cannot directly store it back in

31:13

this table. See the problem, guys? So even if I do that, even if I end up doing that, I cannot save

31:20

it back in this table. And that is the issue that we are facing. And furthermore, it is unreliable.

31:26

If I give a different kind of a question, the language model will respond differently.

31:32

Multiple executions, the language model might give a different response.

31:35

Because we are not enforcing a certain criteria.

31:38

Sometimes it will give year.

31:39

Sometimes it will give 35 YRS.

31:42

Sometimes it will give 80 KG.

31:43

Sometimes it will give 80 KG.S.

31:46

Which be what I'm getting at is you have to enforce a standard.

31:51

The output we want in a certain defined format.

31:53

So that is what we are trying to enforce.

31:56

So that downstress.

31:56

Whatever applications are coming downstream, those applications can read the data and those applications can work properly.

32:05

So whatever output is coming from your language model, this will go to some other downstream application.

32:13

It could be a database. It could be a table. It could be some other website or whatever. And that

32:20

is where that is why this particular structure is very, very important. In what structure or in

32:26

what format my data is basically presenting.

32:30

I hope this is absolutely clear to all of you.

32:32

And I hope everybody is able to appreciate the why of the session.

32:36

See, often time, when we do our class, we just end up learning some topics.

32:39

But this is to help you understand the whys.

32:43

Why are we doing this?

32:45

Why are we learning something?

32:47

What is the value out of what we are learning today?

32:50

And what is the improvement that we will make?

32:52

This was a very bad system message.

32:54

We already saw that.

32:55

What is the improvement that we will make?

32:58

We will not use the system message.

33:00

We will use this system message instead.

33:01

And you can see we are clearly explicitly stating the schema of the output.

33:07

What schema the output should follow?

33:09

You're explicitly stating that.

33:10

And now this is the kind of response that we are expected.

33:14

Even there are problems here and we will discuss that.

33:16

Like for example, you know, this is coming like back takes Jason, some other straight text is coming.

33:21

So this is also not a good thing.

33:23

And we will discuss ways how to fix it.

33:25

Okay, so we want to get our output in a more structured and a more proper manner.

33:29

That is what we want to achieve.

33:33

All right.

33:35

Now, let us move on.

33:36

Let us come back to our content.

33:38

I'll use a mix of some of my notes and the session content as well.

33:42

Right.

33:43

So the entire session is basically focused on how do we get structured outputs for agents.

33:49

Right?

33:49

As I told you, a free form text, it will break the code.

33:53

You cannot, you cannot write a free form text, right?

33:55

So whatever you want the language model to output, you should try to output in a structured manner.

34:04

You should try to output in a structured manner.

34:06

Let's say for example, here, you're an assistant to an hospital administration.

34:10

Extract relevant information as mentioned below in a JSON format.

34:13

You want it in this format.

34:14

You want it in this structured format.

34:16

You don't want this to be outputted like this.

34:22

So give it a read everybody.

34:24

Your refund.

34:25

take 5 to 7 days probably. I have raised it for you now. Once it is processed, you will get

34:29

the money in your account. Might take a little longer if the bank is slow these days. Let me know

34:34

if you need anything else. Thank you. So this is basically, let's say for a minute, the business

34:43

use case here is, let's say, we are talk, you know, we are in a chat board kind of an application

34:48

and an end user. He can just give me one second. I'll just use my pen. Just give you one second.

34:55

Thank you.

35:25

So as everybody can see this right now, the context is that you are the end user, right? Let's see you're the end user, right? Let's see you're the end user. This is you as the end user. And you're, you're in a chat kind of an assistant. Let's see you buy something on Amazon platform and you're chatting with the Amazon bot. Okay? So you ask a question. You ask a particular question. This is the kind of the rag you and a

35:55

and all that we discuss. You ask a particular question in the interface and the assistant is giving this response.

36:00

Okay, it doesn't look perfect right now. Let me just maybe, um, draw this a bit better. So the context is like this

36:09

where you are the end user. You're the end user right now. And you are seeing a kind of a web interface. This is like the chat assistant. Okay. This is the chat assistant. You know, you get a small

36:25

box here where you can ask a question and you can hit enter and you can get the answer. So you are the user. You enter this question. You have a query. You ask this question. And this is the same story we talked about before. That's your user message. It will be combined with some system message and the LLM API call will be made. And let's say this is the response the language model gives. This is the response the language model gives. Now as I told you, if this was a simple application,

36:55

where on the basis of your question, we are just okay with this response and all is good.

37:00

No problem. I mean, we are just asking the question and you're able to generate a response on the basis of that.

37:05

All is good. No problem. But that is not what it is. That is not what this is,

37:10

you know, I would say this is restricted to do. It is not just that, you know, we ask a question and you

37:17

generate this particular response. So it's not that we ask a question and you generate this response, no.

37:23

But this response will, it is not just that you, the assistant will bring this response. No. But based on whatever question you type, imagine a dashboard will get created. And in that dashboard, the different aspects will come up. So free form text will not work. I don't want the assistant to simply generate a free form text response. I will ask a question. I just don't want a simple text response. I will ask a question. I just don't want a simple text response.

37:53

But rather, wouldn't it be incredible, if based on my question, the assistant is able to, first level, it is able to generate some answer. And second level, it is able to generate a structured JSON, just like how I showed in the last demo, information extraction, and generate my output in a more structured format. So the idea is like what, it will take probably five to seven days. I have

38:23

it for you. So it's a refund request, right? So maybe you go and tell the customer care, I'm not happy with the products and all that. And the customer care says, okay, you know, we will raise a refund and all that stuff. So what, so what is the structured output. Okay. Category refund, priority medium, summary is this. And need, human response. Needs humans means do you want to talk to a human agent? That is false. It's a structured response. And this is what we want our language model to generate right now. We want our LLN not to generate this.

38:53

But we want our LLM to generate this.

38:57

So based on the user question, we want our language model to generate this.

39:02

Why? Because eventually, we want to go back and get this kind of a dashboard.

39:09

And if you if you look at it, when, you know, when it comes to this kind of a dashboard, a user will ask the question.

39:14

And based on the different things that the language model outputed, okay, JSON output, right?

39:21

by the support system. There's a support system and that will retrieve that automated

39:25

JSON output. Okay? And it will automatically update it. It will automatically update. The category

39:34

refund and no, a new ticket number has been created. Category refund has been inserted. Priority

39:39

medium has been inserted. Summary has been inserted and needs human review no. This is just like

39:44

inserting values on a database table. The story remains the same right. See what, what is the normal

39:49

normal workflow the way things used to happen until now. You call up Amazon customer care

39:55

and you say you want to raise a refund request, Amazon customer care manually goes and they create a

40:00

ticket for you. That is a normal workflow how it happens today. They will go, they will click on some

40:06

website. Just like this, they will do it. They will click here. Maybe they'll take it, they'll be a create

40:11

ticket option or go to the ticket number down and they manually create. They will manually create an

40:15

open ticket or an order for you, to get a return request for you. But what we are saying,

40:19

is you want a complete automated way of doing it. You want this ticket creation also to be

40:23

automated. So, so what is going on guys? What are you looking at right now? It's a dashboard. It's a

40:28

web application. It is as good as a website. It's a website. Support Kayaik website. It's

40:35

like a website that you have. And the information in a website is at the backend stored in some

40:40

database. There is some backend database where this information is getting stored, right? All websites

40:45

you have, even if you look at Facebook. Now, when you go to Facebook and you look at all

40:49

things your friends and your friend requests and all that. How is it coming? There is some

40:53

backend database where all this is getting stored. You have all seen SQL a little bit. But ultimately

40:58

everything behind the scenes is stored in some kind of database with the structured format.

41:04

So here also, whatever you are seeing on the website, whatever we are seeing on this web page

41:09

right now, is definitely stored in some backend database. So this is like an insert statement that

41:18

we did exactly like what I talked about here. The moment the assistant extracted

41:23

this information, what did you do? It rode this back into a table. This got inserted into a table

41:30

or a database. It was a row inserted to a database table. That was the idea, right? I give you the medical

41:36

notes. You extract the information, you write it back to a database table. The same story we are

41:41

talking about here. You ask a question. The LLM will generate a JSON output. And this,

41:48

this is exactly going to be like a row added to a table, a row added to a kind of a table

41:55

where there's the column called category, column call priority. This is like a table where we are

42:00

going to add that information. And this application, this portion of the application will

42:06

simply read the information from that table. And this is, this is practically how a lot of

42:12

all the web applications and websites are configured nowadays. When they are, you know, whenever

42:16

you see something there, they are actually pulling the data.

42:18

from some table. But what table in case are, first of all, have you thought through that?

42:22

So first, how is the table insert happening? That table insert is happening from here.

42:27

So language model will give an output. You insert the rows. You insert into a table.

42:35

Sorry, you insert into a table. Let me just do it for you once again. You insert the values into a table.

42:43

Insert into a table. Insert the value.

42:48

into some kind of a table. And then the application will simply read from that table.

42:54

Whatever table you've got right now, the application will simply read the information from that

42:57

particular table. So that is the thing that we are looking at right now. And that is why once again,

43:02

having the structured format is very, very important. See, needs human, needs human joe,

43:08

it. Means what? In the application, I'll give an example to you. This is, this will be something

43:14

like a drop down. This drop down type of option over. Now, if somebody,

43:18

was manually doing it. Oftentimes it happens, right? When you're creating a ticket, when you're

43:22

filling a form. Now, what you'll drop down in click? Do option. This is the manual way you will do

43:28

it, right? But here, what is going on? Here, what is going on? Here it is like, whatever language model

43:34

is outputing, whatever the previous language model outputted, this same data is getting used here in this

43:40

application. It is very important that this information is present in a certain format. So whatever is

43:45

coming here, the same thing will be inputted. Actually, it will be like false.

43:48

Maybe the color coding also will change.

43:52

Human review, no, green may are. That means it's a good thing, right?

43:55

Human review is a good thing. If, if a green is a green air, that means you're saving effort.

43:59

Oftentimes, when you're talking to an AI agent, sometimes we think, okay, please connect me to a human.

44:03

That is not a good sign. That means you are, you're, and oftentimes we get into waiting cues and all, right?

44:09

because human agents will have to invest their time. They will have to service you. So many of these

44:13

agents are getting more automated. So if we do not need a human review, then that is a good thing.

44:17

So if the language model outputed, based on the status of your ticket, it is, it is false.

44:23

And you might ask me, sir, how does it figure out that this? Because, you know, because as I said,

44:28

like, you know, on the basis of this, the language model figured out it is not an urgent query.

44:34

The customer is not asking for human intervention. The customer is okay with my. And sometimes you might

44:38

have seen, right, you might have seen in Swiggy and all, let's say you got a bad product or something.

44:43

It gives an automated response. It doesn't connect you to the chat agent.

44:47

customer care agent. And it says, okay, we will give an automatic refund to you. Are you okay? Will you accept

44:52

the refund? So that is like Neve-Juman Falls. That whole a workflow in automatically code

44:56

in. So you say, okay, you attach the picture of your food and you say, okay, I got mutton biryani instead

45:01

of chicken biryani. And Swigie will give a next automated response saying, it's an agent working,

45:07

by the way, something very similar to that, Swig is also doing. So Swigie will give a response saying,

45:12

okay, a refund process. Do you want to accept 250 in your wallet? If yes,

45:16

say yes and I will close the ticket. That is what they are doing behind the scenes. So based

45:21

on whatever question you are asking, the language model is generating a particular structured

45:26

response and based on that structured response, the application values are getting updated.

45:31

The backend table is getting updated. You're insert or or update or it. That is what is going on.

45:36

And then if you want, you can show it in some dashboard. Dashport one are the optional. This is like an

45:40

optional thing that we are trying to see right now. Okay. So again, I hope everybody is understanding

45:45

the idea behind what we are trying to achieve. Okay. So we have already been writing a lot of

45:50

prompting and all these things we've been doing. But this will, this will probably add a very new

45:55

perspective and very new dimension to what we are discussing here. I'll give you one more beautiful

45:59

use case for this thing. Okay. Look at the Tesla demo that we did. Tesla demo, we did it over several

46:05

sessions. We asked a question, what is the annual revenue of Tesla in the year 2022.

46:11

Okay. Now, different people in the audience got different kind of answers. Some people reported 80,

46:15

$5.58 million. Some people reported something. Okay, let me, I think it will be better if I just

46:22

maybe open up my wide board and explain to you. Let's go back to that Tesla use case for a minute.

46:45

Okay, here it goes, everybody can see this one. This is the use case we have right now. Let us see.

47:15

the question, what is the annual revenue? Imagine this is like a chat application,

47:22

right? So end users will ask this question. What is the annual revenue in the year? 2022? I think we

47:34

can debate about it. Maybe my system message was not the best. That's right. People got different

47:38

answers, right? People got different answers. They're getting 84,000 something. I think it's

47:41

84,000, some million or something. Somebody might get an answer like this.

47:48

Somebody might get an answer like this. A comma, a comma, okay? Million dollars. Okay. Somebody might get

47:56

an answer this way. Eighty-four billion dollars. Or then dollar prior. It could be, right? It could be.

48:03

Eighty-four thousand million is nothing but 84 billion. Right? It could also be something like, uh, uh, 84.0.

48:11

billion dollars. Dollars is basically not coming as a symbol. It's coming as a word. It could be. My answer is not wrong. My answer is still grounded in the context. So rag system is not giving the wrong answer. The problem is the language model is not enforcing the same output structure. And let me give you another one final use case. My output could also come this way. And some of you did report this as well. My output can also come this way. The annual revenue.

48:41

The annual revenue is 84 billion dollars. So my answer can also come in this particular manner. I hope everybody is with me. Now, what is the problem with this approach? It is for the normal chat-based system. I think we are good. We are good. There is no problem. You can ask a question, get a response, and everybody was happy with

49:11

in the last class. I'll tell you the problem. The problem is what if the output of this system becomes

49:19

the input to one more system? This eventually will become the input to another application. Another

49:27

application will take this as input and it will do some processing based on that. So you ask a question,

49:34

what is the annual revenue in the year 2022? And let's say there is a website if

49:41

eventually I want this information to be displayed in a kind of a website. And in that website, you know, we will have this question and we will have the answer. But the answer is only a small numeric field. The answer will only be a numeric field. Okay. So here the user asks the question. So this to give you the, I'm just giving a very general use case. Okay. So this is, this is how the initial thing looks like. User will ask the question. User is asking the question. They hit enter. And here it is looking like this.

50:11

ask that question.

50:14

Take it enter. What was the question? The question was this. What is the annual revenue? I'm not writing

50:17

the whole thing. This is the question, right? This is what the user asked the question. And now the assistant

50:23

response joe here. Whatever application you create, remember when you design a website, this

50:31

will appear on the website, the application. When you design that website, you will have to design that front

50:35

end, right? At front end you will have to design. Let's say in that front end, you have to design. Let's say in that

50:39

front end, you've only kept a numeric box.

50:41

It is not a text box. It is not somewhere where an entire string will come, but this will be only a numeric box.

50:48

This, this assistant, this particular section can only display a number.

50:53

Nothing else can come. I mean, you might have seen these kinds of things in, you know, while filling of web application forms and all, right?

50:58

Upch registration form fill up and it is asking you for your age. Your age can be 20, 30, 40, whatever.

51:04

But you cannot enter my age as iron, right? You cannot enter a string. If it is accepting a number, if this field in

51:11

the website is accepting only a number. And if you try to, you know, enter some kind of a character or

51:17

something, it'll give an error. And that is exactly what we are discussing in this class today. Given this

51:24

question, oftentimes if you don't frame your system message correctly, if you don't format your outputs

51:32

correctly, you will face these kinds of issues. And you can clearly see this is the issue we have faced. That's

51:37

why I think you can connect the dots with all the previous classes now. These are issues we have faced,

51:41

consistently before. Our outputs were inconsistent. Sometimes it was giving something.

51:46

Sometimes it was giving something. And we never had any way of validating that schema. And now we

51:50

will see how to do it. You can all of you have with me. What we want here is to write our system message

51:56

in a very accurate way so that the answer is coming as a integer. Even if it is 84 million,

52:05

whatever that number is, I want my answer to be like this. Eighty-four thousand and million,

52:11

and add 6 zeros to it. I want this to be coming here. I want the answer to be coming

52:17

like this 84 and add 6 zeros here. I don't want million dollars. I don't want D.E. I don't want

52:24

because the machine honestly cannot recognize these symbols. I told you it's a text. It's an integer

52:28

numeric box. Just like adding it to a database table. I hope everybody is now appreciating the importance

52:35

of formatting, especially in scenarios where the output of an application becomes an input to some other

52:40

application. And that application can be a simple web application, a website, or it can be a

52:45

database, or it can be some other thing. Because that next application requires the data in a certain

52:52

format. And it is very important to enforce that format. That is the important thing. Right.

52:58

Okay. So I hope everybody's with me. All of you with me. Let's move on.

53:06

Here the same story has been talked about why agents need structured outputs. I'm going to go

53:10

this again. And as I told you, like, you know, it is important. Like, you know, so it is important

53:15

because otherwise the websites and all will break. So we talked about that already. Now, how do we do

53:19

do it? Now the question is how all this while we were discussing the problem relating it to the

53:24

past sessions. What was the issue? Now let us discuss how do we solve the problem. Problem for solve

53:29

Jessica. Let us talk about that. So we use what we call a JSON schema. A JSON schema is the blueprint

53:37

your application owns. This is like the blueprint that we are talking about.

53:40

about. Okay. So what is the blueprint we are discussing right now? The blueprint is your

53:44

your JSON schema. And this is a slightly, you know, a slightly important thing, a slightly

53:52

different thing than what we have discussed before. So before you start working on any application,

53:58

it is extremely important to define a JSON schema. Some of you might have heard about it in

54:04

your Python session. I'm not briefly discussed here. But Jason is basically very, very,

54:10

similar to a Python dictionary. You can see the structure of a JSON is very similar to a Python

54:15

dictionary. This is just to kind of explain to you what basically JSON is. So JSON is nothing but a

54:21

data format, very close to a Python dictionary. It's a data format. It is a kind of a data format. It is a very,

54:28

very popular data storage format. And very important, the structure of a JSON is very similar to a Python

54:34

dictionary. Just like dictionaries have key and value pairs. All of you remember, dictionary has something

54:40

called a key and the value pair. This is the key. You give a colon and you give

54:44

the corresponding value. Again, you have the key. You give a colon and you give the corresponding

54:48

value. So JSON has this kind of a key value kind of a context. Right. There's a key. You give a colon

54:54

and you give the value. There's a key. You give a colon and you give the corresponding value. So

54:59

this is the key value kind of context we have in the JSON. Right. So similarly, just like in the

55:05

dictionary's. Okay. That's the idea. So this is how our typical JSON schema schema looks like.

55:10

And you can see what are the information we have got right now. This is the sample JSON schema that we have

55:15

designed. Okay. And this is how we are doing this. What are the things we have here for now? Let us see.

55:22

So this is the, this is the sample JSON schema that you can see on the screen. Everybody just give it a glance once, please. I think, see this entire session, I will be taking up the same use case, the e-commerce agent assistant use case.

55:34

So that you can relate to it. The story remains the same. I want you to have that connect with what we discussed in the first,

55:39

20, 25 minutes in the class, whatever I talked about. So this is what you ultimately want to output.

55:45

So whatever language model you have, the, you want to output category, priority, summary,

55:50

needs human and this. These are the five things you want to output. And see how we are specifying that in the

55:56

JSON. In the JSON, we are clearly specifying the entire structure of how it should, it should look like.

56:03

Okay. So I will explain this to all of you. Before that, just give it a glance.

56:09

all of you once. Just give it a glance. I'll explain to you. Just give it a glance

56:13

in the meantime. And this is a separate JSON file in. Just to show you, I have my notes as well

56:21

here, which I'll be sharing with you later. What I've done here, you can see I've actually created

56:26

this particular file for you, right? Let me, in fact, let me run, you know, start the runtime again and

56:32

show you. So here what I'm doing, I'm actually creating that JSON for you. I'm defining the same structure.

56:39

And then I am basically saving that schema data. This is like a Python dictionary, right? So I'm creating a Python dictionary. And I'm saving that particular Python dictionary, jason. I'm dumping that particular schema data Python dictionary into a JSON file, which is called disk.Json. So you can already start to see that JSON and Python dictionaries are interchangeable. If your data isn't a JSON, you can load into a dictionary and vice versa. If you have a dictionary, you can load that back to a JSON.

57:09

they're interchangeable in that context, okay? So let me quickly go ahead and execute this code to sum it a little bit.

57:15

Initial parts so that you can see the JSON getting created. And then we can again talk about that JSON. What is it doing?

57:21

The content for the session as as usual is in the files. I've already shared with you. Today we are in 23rd June.

57:30

Everybody will see the contents, the IP by NB file here. It's a easy, easy content. So it's a pretty less code we have today comparatively.

57:39

But yeah, I think the topic is very, very important because there's something very different compared to what we have seen before.

57:44

But the code is very light for today, over all. Okay. So let us run this. Let us execute this.

57:49

Let us execute this. And now you can go ahead and let us create these two folders. And we are going to be creating two folders right now for.

58:09

proper management. We'll be creating a folder called schemas and we'll be also creating a folder called prompts. And you remember this we talked about in our last to last session last session. We talked about prom versioning and why it is important to version the prompts in a correct way. This is the standard practice will be following. We will have a separate prompts folder and we'll be storing the prompts in a TXT format or a JSON form, whatever, whatever the formats be. We want to version our prompts correctly. Okay. And we want to also go back and store our schemas. This is where we will store our schema.

58:39

And this is how the Jason schema basically looks like.

58:43

So what are we doing? We are first creating a Python dictionary and then we are simply dumping that dictionary in this particular JSON file.

58:51

And if you take a look at it, this is how it looks like. This is the big picture idea of what we achieved.

58:55

We have created a simple JSON file that is like a blueprint. It is like a blueprint.

59:00

You know, it is like a typical application form. When you sit for examinations, you get an application form that you have to fill up in a certain way.

59:08

work blueprint. So people cannot just randomly enter their name, their phone number,

59:12

their email address, wherever they like. It's not like an empty blank sheet. It's like a, it's like an

59:17

application form. All the fields are present. You have to fill up your name only there. You have to fill up

59:22

your mobile number only there. You can fill up your email ID only there. It's like an application form.

59:26

So that's like a blueprint. It's like a schema. It gives a structure. And this is how it looks like.

59:31

You can take a look at it. Okay. So all that I would like you to do is just take a minute and go through this

59:36

particular JSON file on a few so that everybody is clear what it means. Okay. And then we will get

59:41

a little deeper into it right in the class. Okay. Everybody give it a glance, please. Everybody

59:47

give it a glance please. Yeah, that is right. Uvara. You have made a good point. It is very

59:52

important in multi-agent communication because the output of one agent will go to another agent and that

59:57

agent will accept data in a certain format. See, it is like, you know, it's like, the idea is very similar

1:0:03

to a function call. And I think we talked about this in our last.

1:0:06

React session. A tool is nothing but a Python function. A tool is nothing but a Python function

1:0:11

at the end of the day. You can have a Python function that accepts input argument in a certain

1:0:16

format. So whatever output a certain function is giving you, that will become the input to another

1:0:21

function. And that function will accept input only in a certain format. So yes, what you what you said

1:0:26

is absolutely right. Okay. Yeah. So everybody, please give it a glance, this one.

1:0:36

Thank you.

1:1:06

Thank you.

1:1:36

Okay, hope everybody is aligned on this and you can clearly see, clearly see the things that we have given here. This is the proper structure of our JSON. These are actually recognized keywords.

1:1:58

In case you're wondering that, sir, are these are these recognized keywords? Yes, they are recognized keywords in Jason.

1:2:04

So whenever you create a JSON file,

1:2:06

you know, a JSON file just like how we have treated here. These are recognized keywords

1:2:10

in a JSON file. Type. Type basically stands for object. Means the output must be one JSON object. It

1:2:17

cannot be multiple JSON objects. So that is the type. Required means all the five fields must always

1:2:24

be present. The output must contain all the fields. You cannot have a scenario where one of those

1:2:31

things are missing. So whatever language model is outputting, the language model must output,

1:2:36

all the five things. Like if you go back to the medical notes example, it should absolutely

1:2:40

output age, diagnosis and something. Even if a medical notes does not have that information,

1:2:44

it should still output that field and say none, like it was doing before. Right. So required. Required

1:2:49

means these fields must come. This must come in the output. Properties very important. Properties

1:2:54

defines each field's type and constrain. So what, so in the properties, you're looking at each and

1:3:00

every of the fields, like category, priority, summary needs human and suggested reply. Imagine they are

1:3:06

columns in a table. And you are saying, okay, what is the data type of that column?

1:3:10

What is the accepted data type of that column? What kind of data type is expected in that column?

1:3:16

And also, what are some other constraints? Like, for example, we say type is this and type is

1:3:21

Boolean. Bullion is a recognized data type in Python. All of you know, either is a true or false will be

1:3:26

the values. And e-num basically stands for the allowed values. Enum stands for allowed values.

1:3:34

What are the values which are allowed? That means the category fee can only have billing, shipping,

1:3:40

product and other. It's like a drop down. Think of it like, you know, if you're in a particular website

1:3:44

and you're filling up an application form, you often get a drop down. Okay, what is the category? You can only

1:3:49

fill up from those four categories, nothing other than that. So we are enforcing this in the schema.

1:3:55

We are enforcing this as a property that whatever output the language model is giving, the output must

1:4:00

follow this standard. You cannot generate a category which is different from the four we have

1:4:05

listed. You cannot create a generate a priority that is different from the ones we have listed.

1:4:10

And you cannot generate a summary that is not satisfying this criteria. So we are clearly saying

1:4:16

that summary should also be a string and the minimum length should be five and the maximum length should be

1:4:20

200. That is, that is the constraints. So the properties is where we specify those constraints.

1:4:26

Required, all these five fields must come and these are the constraints. The constraints, the

1:4:30

five fields are satisfying. So this is what we have basically done.

1:4:37

Okay. So that is, so it is preferred. It is definitely preferred that you, that you do it.

1:4:41

It's definitely preferred that you do it. So the more you, so the more detail you add, the more detail you

1:4:46

add, the better your application becomes. So it's definitely preferred. See, like any which case,

1:4:52

if you are creating the JSON, you know, see, if your, if your question is, do we have to do it like,

1:4:57

not really, not really, but the required field.

1:5:00

should be there. But preferred, I would say, as a best practice, you should still try to do it.

1:5:06

Like, don't skip anything. But yes, I mean, if you're asking me from a general practice perspective,

1:5:12

what we do, we put only the fields that are present and required here. So whatever required fields are

1:5:18

there, only those for that the properties are usually there. Okay. That's one way to look ahead.

1:5:25

Okay. All right. So I hope everybody is aligned. Everybody is clear. And this is exactly how

1:5:30

how your how the schema should be defined okay so whatever application you're

1:5:36

building whatever output that application will give you you should take each and every

1:5:40

of that aspect and you should specify that okay my output should be in this particular

1:5:44

format okay that is the thing okay can we all think of a similar kind of a schema for our

1:5:50

you know for our hospital administration use case we were doing that medical notes one right

1:5:55

so can you can you can you all think of a schema for that particular model okay i'm just

1:6:00

going to bring up that thing. It could be a small class activity we can do, right? It could be a small

1:6:05

class activity we can do. So let me go back to my prompt engineering thing. So we can all

1:6:14

write a similar schema for this particular exercise, right? So exactly how I explained this one,

1:6:20

exactly how I explained this one. Let me ping this to the audience on chat. Exactly how I,

1:6:25

how I did this one. I want you to create a similar schema, a very, very similar schema for my, for my

1:6:30

hospital assistant use case. What do you think a similar schema will look like for this

1:6:35

particular use case? Okay. So everybody just maybe take a minute and try to figure out.

1:6:42

This is not a schema. This is like the prompt that we are writing, but we want a schema. A schema is

1:6:46

like a JSON. You want to separately create them. Remember I told you prompt is different. Prompt is

1:6:51

what you will eventually store here. We have not come to that yet. But right now we are only creating

1:6:55

the schema. So you might ask me, okay, Sayan, what do we do with the schema? The scheme. The scheme.

1:7:00

is what is used for validation. Right at the end, and we'll come to that exercise right at the end,

1:7:06

we will use the schema for validation. So here, medical notes also, you write a certain system

1:7:12

message, you give a user message, and the language model is giving a certain response. You will take

1:7:16

that response and we will use it for validation. It's okay. So you will take that response and you will

1:7:22

validate against your schema.jason file, whether all the criteria are satisfied with respect to the schema.

1:7:28

That's how the thing happens in practice. Whatever outputs the language models are

1:7:33

giving, you will take that output and you will compare against the schema that is already there,

1:7:38

the saved blueprint or the safe schema that is already there and you will evaluate on the basis of that.

1:7:43

That is it matching? Are all the fees coming? Are all the fields coming of the same time?

1:7:48

Okay. Are all the required fees there and like that? This is how it will look like. Okay. So I hope

1:7:54

everybody is getting the big picture idea. Why output formatting and how?

1:7:58

output formatting is done okay so everybody please try to you can you can ping on chat you can

1:8:04

ping on chat what the sample uh the sample jason for this particular medical notes will look like

1:8:10

you can use a bit of chat gpt if you want so i can i can ping you the system message and please use a

1:8:17

bit of chat gpt i'm fine with that see our objective is learning our objective is not to make you uh

1:8:21

right from scratch our objective is learning so i'm fine if you can use a bit of chat gpt and you can generate

1:8:27

what the uh you know what the schema for this will look like okay so please try it out

1:8:32

just take a minute all of you i just want to know what that dot jason file will look like

1:8:39

what what what will that what will that schema look like what will be required what will be just

1:8:43

just think about it.

1:9:13

i would like everybody to attempt okay everybody please attempt okay okay everybody

1:9:19

everybody should attempt give it a try and and and as we do this class we'll be able to

1:9:27

beautifully draw the connect with everything we have done so far this is the normal information

1:9:32

extraction task you can connect it back to rags how and why the formatting is so important okay

1:9:43

okay thank you for sharing others and it is it is it is it is going to be a little

1:9:54

you know kind of up to you subjective it's not like a hard evaluation we are doing but uh it is

1:10:02

it is just what you think is the right schema okay so we just want to we just want to we just want to

1:10:07

encourage you to think encourage the thought process in the class actually it is not of like a perfect

1:10:12

answer we are expecting like like let's say for example uh smoking

1:10:17

of smoking the enum what some of you might ask me that sir smoking

1:10:21

is smoking is a required field for smoking can't be yes no will it be smoker non-smoker

1:10:26

no no no no information we have you know that information we didn't you know

1:10:30

that information not you know what information not you can do it in your way we are okay with

1:10:35

that okay now okay now smoking the value is that yes no be was or true false be was supposed to

1:10:41

that is smoker non-smoker be on smokers that's up to you up your application

1:10:44

how you'll your website how will your website how will it right so that is okay that is okay

1:10:49

it's not like a hard thing but we just want you to think around it okay ameth has also

1:10:54

paint thank you amit let's see others take a minute all of me and let me also share with you

1:11:05

this thing so that you can take a look at it okay while you're pirating the thing

1:11:11

I repeat again, type may object a proper required will be whatever fields are

1:11:14

absolutely required the language model must output these fields and properties will define the

1:11:19

constraints of those fields what the data type will be and what the uh enum will be

1:11:23

enum means what the required values will be what the possible values will be that's it very

1:11:28

simple very simple okay because has also messaged good because others I hope you are all trying

1:11:41

I will give it another minute.

1:12:11

Thank you.

1:12:41

Actually, actually diagnosis will be hard to do you know, you know, so

1:12:55

you can't also ping.

1:12:56

So Bhavik diagnosis, you can restrict not?

1:12:58

Age is fine.

1:12:59

Your gender is also okay.

1:13:00

Male, female, other, okay.

1:13:02

Hypertension, like, sorry, weight is okay.

1:13:05

Smoking be okay.

1:13:06

But diagnosis you can't restrict within one of the categories, right?

1:13:10

Okay.

1:13:11

Diagnosis can be a string, but you cannot restrict diagnosis to only those five varieties.

1:13:15

Yeah, that's a valid use case.

1:13:17

I mean, I think, but from your perspective, whatever application you're designing,

1:13:21

that's how you can keep it.

1:13:23

Maybe the doctor can only diagnose those cases, but generally the diagnosis will be like a string.

1:13:28

So that it's more open-ended.

1:13:29

People can enter any diagnosis.

1:13:31

The language model should be able to output any kind of diagnosis.

1:13:34

Yeah, correct.

1:13:35

You will not give an enum for diagnosis.

1:13:36

You will just keep it at a string.

1:13:37

Now say, min lens, do max length, something like that.

1:13:40

You know, how we can do.

1:13:41

we have done it this way.

1:13:42

Somebody.

1:13:43

It should be a minimum to maximum.

1:13:44

And this is another very interesting way how you can enforce constraints.

1:13:48

You know, we talked about max tokens that are part of LLM outputs.

1:13:51

And this is another way how you can enforce constraints.

1:13:54

You can enforce constraints in the same manner.

1:13:57

Okay, we can all enforce constraints in the same manner.

1:14:00

This is one other way we can do it.

1:14:11

What is that? Category.

1:14:19

Suggest.

1:14:21

Senghis.

1:14:26

The rest.

1:14:40

Rest.

1:14:41

But I think you have just given a sample answer.

1:14:48

Right what you've got you have done.

1:14:50

But I think it's just a sample answer.

1:14:53

It's a sample answer.

1:14:54

But you have to give the schema.

1:14:57

Schema.

1:14:58

What is the structure?

1:15:00

What is the blueprint?

1:15:01

I think what you have done is you have given the whole answer.

1:15:04

What the language model is outputting?

1:15:06

You got it, right?

1:15:08

Okay.

1:15:09

Okay.

1:15:10

Okay.

1:15:11

Okay.

1:15:13

Happy to see everybody's trying.

1:15:15

Okay.

1:15:16

All right.

1:15:17

Now let's discuss.

1:15:18

Maybe I can pick up one of your, one of the examples from one of you and we can discuss.

1:15:24

Ali is asking, is it right?

1:15:27

Ah, absolutely.

1:15:28

I think we can, we can take your thing or we can take one of the use cases.

1:15:35

Yes, it's multiple ways you can do it.

1:15:38

Maybe I'll just give kind of 30 seconds.

1:15:40

Thank you.

1:16:10

Thank you.

1:16:40

Thank you.

1:17:10

Okay.

1:17:17

So,

1:17:19

this is no,

1:17:24

there is no right.

1:17:25

There is no.

1:17:26

There is no.

1:17:39

Different people have done.

1:17:40

different ways, right?

1:17:42

And this is how your sample Jason will look like.

1:17:44

And they can be different ways you can do it.

1:17:46

For example, this is what Ali Ping.

1:17:48

So Ali, this looks okay.

1:17:50

This looks absolutely fine.

1:17:52

You're saying required age, gender, diagnosis, weight and smoking.

1:17:55

These are the five required fields.

1:17:57

And you've also specified the properties nicely.

1:17:59

And if you guys see Ali has also given

1:18:03

something called description.

1:18:05

Ali has also added something called description.

1:18:07

Description is optional.

1:18:08

So I did not show this in my code.

1:18:09

not show this in my code, but you can also use description. The description is giving you one additional detail describing what that field is used for.

1:18:16

Description we have used for. So gender is also fine.

1:18:19

Male, female other. This is what I told is not fine.

1:18:22

Because in our typical real world application, you see, diagnosis is more open in it, right?

1:18:27

The application should be able to read your medical notes and it should be able to generate, you know, a string diagnosis kind of a summary.

1:18:35

It should be able to generate a, you know, like a string diagnosis kind of a summary.

1:18:38

of a summary. That is what the application should be able to do in a way.

1:18:42

Right? So that is the idea. So, so enum, obviously you should not put.

1:18:49

So what you should put for diagnosis? Your diagnosis should rather be like this.

1:18:54

It will be something like this. Okay, if I just go back and correct this one.

1:18:59

Yes, so this will be somewhat like this.

1:19:03

So diagnosis will be somewhat like this.

1:19:07

Let me just print it out. All if you can see. So it will be like type string.

1:19:11

Maybe minimum length is five and maximum length is 200. I hope everybody's aligned.

1:19:15

Next is the same story we have talked about, you know, like, it's for a separate code type string and

1:19:20

same format where you can do it. The weight is also okay and smoking is also fine. This is another

1:19:25

thing I was mentioning. Some of you were mentioning, some of you were mentioning like true calls. Some

1:19:29

of you are saying yes, no. Some of you are saying smoke or non-smoker. Absolutely fine. Up to you.

1:19:34

Okay. Now another thing that

1:19:37

you know, that I did not see.

1:19:39

People did not actually do this.

1:19:41

It's like null.

1:19:43

NU-Dabularly not available.

1:19:44

Information not available.

1:19:45

Now, there can be cases where, based on the medical notes, if you remember, the use case that we did,

1:19:51

there was a second use case where based on the medical notes, the language model actually predicted

1:19:55

that the person's smoking is, weight is none, diagnosis is none.

1:19:59

But in the medical notes, the person's weight is not there.

1:20:02

In the medical notes, the person's diagnosis is not there.

1:20:05

So we have to give some.

1:20:07

provision for that also. So maybe you can add that extra category here. It is possible that

1:20:12

weight can be none also. Absolutely. Piedentic is another thing. So again, Pranjal, we are not

1:20:18

talking about Piedentic particularly today, but you are absolutely right. Pidentic is another thing that we

1:20:23

will talk about in a later session. And we can also use it for data validation. You're right.

1:20:28

So this is how your typical suggestion schema for our current problem will look like. And most of you,

1:20:35

most of you like you got it right okay you you did it the correct way okay

1:20:41

all right very good let's move on let's continue the conversation forward so we talked about the

1:20:46

concept of jason schema and we also talked about why it is important right now let's continue on

1:20:54

and again just to clarify this output that you're getting whatever the language model outputs

1:21:00

eventually that will be part of some website it will be part of some website as i don't you so

1:21:05

whatever your language model will output.

1:21:08

Okay, so based on the question you are asking the support ticket assistant will generate some

1:21:15

response and based on that response, they will auto update your application.

1:21:22

So that is the big picture idea of this whole application that we are trying to think.

1:21:27

Okay, so so the workflow should be clear to you.

1:21:30

So this is like the user.

1:21:32

So the end user will go back and ask a question.

1:21:34

end user will ask a question and based on that particular question the uh the the llm will be called

1:21:41

and the assistant will generate a response the assistant response will be in the

1:21:47

form of a jason sorry the assistant response will be uh in this particular format assistant response

1:21:53

will be like in a typical structured jason format the response will come and that jason response

1:22:00

whatever uh jason response comes should match this schema and that response is what exactly

1:22:10

reflects back on this application this is the front end exactly what i was explaining a while back

1:22:17

but let's say the response is something like okay category is uh billing

1:22:22

if we manually can manually see manually support ticket up raise

1:22:25

you can go to create ticket and you can manually fill the category manually fill the priority

1:22:30

manually fill the summary okay manually can manually

1:22:33

what are we discussing we are discussing of completely automated support agent

1:22:40

so we are saying you are the end user okay you are the end user

1:22:45

this is exactly how the workflow will look like you're the end user you ask a question

1:22:49

you have a dashboard like this right you you you have a kind of a dashboard so you so let's say

1:22:54

we are too lazy we don't want to go to the create support ticket and then click on create

1:22:58

and then enter all this we are too lazy

1:23:00

what we will do we will simply type a prompt we have a particular text box here we will

1:23:05

simply write what we want what kind of a ticket we want or something and you simply hit enter

1:23:10

so what are we doing user message dia you're making an API call to the language model

1:23:16

and based on that the language model will generate a response and remember this has to be a

1:23:22

very structured response the same story we've been discussing all this while this response has to be in a very

1:23:27

structured format this will be a very structured response the response has to come in a very

1:23:32

structured format this is this is the you know a response in a structured format you're getting

1:23:38

and you have to compare that response to whatever response we got just like that jason we have to

1:23:44

compare that response to this particular schema this is the schema right you have a schema

1:23:50

and remember your response must sorry i think the word is not readable

1:23:56

schema it should be it should match the schema that means in that response the language

1:24:04

model created based on the user request response should contain the category what is the priority

1:24:09

what is the summary and all these things should be there and they should match the schema

1:24:13

none of the field should be missing all the field should come and they should contain only these values

1:24:18

what response object in everything should be exactly as it is okay once the validation

1:24:23

is done i will call it validation i'll use a green color here it's the validation we will see this in

1:24:28

python in a moment once the validation is passed once it is tick mark once it is past what we will

1:24:35

do we will take this response and we will write it back to this front end application the application

1:24:41

front end is again uh like imagine a typical web application or a website

1:24:48

where whatever response you have here those same things are written back to the front end so the

1:24:53

category is auto selected but if the category let's say here is billing so it is almost like the billing

1:24:58

is auto selected that is automatically a record for billing is created priority let's say a low

1:25:04

so low is auto selected you don't have to manually do it you just type the question the language model

1:25:10

generated some response and automatically based on that is dashboard was auto updated and the ticket

1:25:14

was automatically created so that is the big picture idea that we are trying to

1:25:18

to achieve summary agia needs human maybe let's say is coming out to be false it's like a radio

1:25:22

button and suggested reply whatever that is okay i hope everybody is getting an idea in

1:25:28

terms of what the schema is and how it is going to be useful okay so this is the same story we

1:25:34

have talked about this before and now we are coming to the aspect of the system message

1:25:39

okay um what's that ali has asked a question sir just wanted to confirm uh

1:25:44

sorry i missed that ali i was just explaining the concept in the meantime

1:25:48

uh what is that question so i just wanted to confirm will we define everything about output in system

1:25:53

message yes yes system message will give uh you know uh in a way yes you will you will define that

1:26:00

exactly so ideally both will do that the system message gives the task and the output instruction

1:26:06

but the exact uh exact structure types required fields and allowed value should be defined in the

1:26:11

jason schema so in a way both but then i i would say uh uh

1:26:15

uh uh what you have to give some idea about it in the in the system message obviously in the

1:26:20

system message you will have to give the general idea but uh you will still have to maintain

1:26:25

all that information in the structured in the in the in the structured jason file also

1:26:32

okay ali i i think i think if you read this system message this will answer your question

1:26:37

and it is exactly what you mentioned see we are giving this in detail in the system message

1:26:42

so system message we are clearly stating what

1:26:45

the category should be what the priority value should be what the summary will be we have to

1:26:49

also clearly state that all keys are mandatory and we are also clearly stating what the

1:26:56

values should be within these things we are also clearly stating maximum 200 characters

1:27:02

and we're also clearly stating the valid values so in a way yes what you say this is correct but

1:27:08

if i have to add one more aspect to it the jason should still be there but if i go and do this here

1:27:14

you can see i'm creating the i created the jason here what i talked about the jason is the

1:27:20

the schema right yes you have to state everything in the system message correct you have to but the jason

1:27:25

is more useful for validation purpose the jason is not part of the prom jason you will anyways put because

1:27:30

this is part of the validation this is the schema this is for validation so the final validation we will do

1:27:36

using the jason but system message is part of your prom so you will have to put in the system message

1:27:41

and you can see this is exactly how my system prompt will look like

1:27:44

we must strictly enforce the required shape in the prompt text itself so the model knows the exact

1:27:49

rules i think just to answer your question early okay so i hope this is clear to you so this is

1:27:56

exactly how your prompt text will look like and if i run the code if i run the code you can see

1:28:00

this is exactly how your prompt text will look like so we are creating uh this particular prompt

1:28:06

text you can see system v1 underscore system dot pxp

1:28:10

exactly using the approach we followed in the last session this is the prompt version that we have done we have created

1:28:14

version one of system message okay and this is that txp prom that we have created

1:28:18

you can everybody give it a glance please all of you see if you're absolutely okay with this

1:28:24

this is it that system message that we have created just now i wanted to clarify one thing

1:28:30

uh please ignore these uh slashes and new lines and all that okay these are just placeholders in

1:28:35

python but these will not be uh appearing in the string here just just wanted to clarify so this is

1:28:41

exactly how you're how your you know the system message of the prompt looks like

1:28:47

okay i hope this is clear you've got nothing much we were talking about the same thing only

1:28:52

we were just uh so i i hope you followed the part where i was talking about the jason schema

1:28:58

so jason schema will be used for validation purpose and the second thing i was just i was just

1:29:03

talking about now is we were discussing the system message so we were just saying that in the

1:29:07

system message also the same instruction should be given

1:29:11

exactly if in the ui the same thing uh if it has different then we have to update the system

1:29:15

prompt and jason both exactly you know ankid uh a best way to do it is to work backwards

1:29:21

um first um so first ui's sure we start from the application we start from the end result

1:29:25

um end say should do kartay and then we trace backwards so we start from the end what do i want

1:29:30

my end to look like my application what do i want the kind of answers my application to give we

1:29:35

start from there so that basis where we create our schema because schema is like

1:29:41

like our blueprint that our checklist is like my checklist you seema is like my checklist

1:29:44

you look here here scheme is our checklist is that's it and then you work backwards

1:29:51

and create your dress system prompt okay i hope this is clear

1:29:57

ha exactly exactly we will use we will save the jason schema in a separate file then use that

1:30:04

files part to do validation that is right only that is exactly what we did correct we will

1:30:09

exactly do it what you say we will use that files path for validation down the line

1:30:13

down the line's your response i will we will take that response and we will we will we will

1:30:17

compare that response with this jason schema that we created you're absolutely right what what

1:30:23

you say okay if anything is missing in the response unkid that will go as part of error handling

1:30:31

that is part of the error handling workflow so that your try catch blocks try except blocks

1:30:35

a box a but now up to how you want to handle it either the application can error out

1:30:41

or it will show another prompt to the end user saying okay please fill it up that is up to you

1:30:45

how you want to handle it but yes if the jason validation fails then definitely like how you want to

1:30:50

handle the error is basically now up to you it is like a typical try except block in python so other

1:30:56

if the validation error is going to happen then you can decide how you want to handle it whether

1:31:00

you want the user to re-enter or you want to correct the prompt and all that stuff okay but

1:31:05

but definitely ideal cases the application should error out it should error out

1:31:09

because if the language model is you know if we are expecting four five fields

1:31:16

you're like this okay you're five required field there you're exam form

1:31:20

are you have five field but you've only filled up four fields language model is only outputing four

1:31:25

fields so five not are four are there so what error will so that error

1:31:28

should ideally but you can handle it in a different way who up to you up to okay okay so system

1:31:35

message is also okay with all of you i think this is also straightforward we have created our

1:31:39

system message everybody can see and now we will go back and uh uh do this okay now what are some other

1:31:46

things to take care of what are some other things to take care of a few other things

1:31:50

uh no no system message plus uh user message is the output jason schema validation is

1:31:59

is only used for validation part so ali just to correct what you just now said just to correct what you just now

1:32:05

it system plus user is our prompt right and based on that we call the drought model

1:32:13

and we get the output response this is whatever we have discussed so far nothing changes here okay

1:32:21

the only new part of today's session is that we talked about how you can take that response and how you

1:32:27

can validate against your schema this is your validation part it this we have already discussed all these

1:32:34

classes this is the new part that we are enforcing today got it i hope you are absolutely

1:32:38

okay so we are taking that regenerated response and we are trying to compare with the schema

1:32:42

and we are trying to validate whether that response is following the structure of the schema

1:32:47

are all the fields coming are all the required fields there are all the fields coming in the right

1:32:52

data time are all the fields following the same values and so that is what we are doing

1:32:56

you can't you know that's what we are doing that's that's in a way what we are doing right

1:33:02

we are doing that only but yeah in jason schema there are certain properties and formatting that we are using

1:33:07

which you don't have to put in the system message system message may it's it will be processed by

1:33:12

a language model so you don't have to hard code it this way this is the way to do it ali this is the way to do

1:33:17

it see that way so even last class if you remember we did prom versioning we created so many

1:33:22

different versions of prompts so then we have we made here this is the best practice

1:33:26

way of doing it. Otherwise what happens is now, Ali, it is basically goes back to the session

1:33:32

we did on prompt versioning. Why are we doing that? We are doing that for modularity. You want to reuse

1:33:37

the same thing multiple times. Just say mano, out a schema and we want to reuse that in multiple places.

1:33:43

Instead of hard coding that in a system message, if you can keep it as a separate file,

1:33:46

it becomes easier to reuse in multiple places. Okay, are you with me? So that is the reason why we

1:33:51

create separate files for these things. And we and and this is more like the, you know, more like a typical

1:33:56

project folder, the typical project organization, how it looks like. You know, you will want to

1:34:00

have your prom stored in a separate file. You want to have your schema stored in a separate file

1:34:05

so that you can later reference it back. This your entire repository may have. Okay,

1:34:10

you know, because all this will be part of your project folder. Tomorrow, your customer will want to see

1:34:15

that, you by, you've got to do you. You got it? So if you are keeping everything hard-coded in your

1:34:22

code, then how will you know? Tomorrow, some customer comes.

1:34:26

back to you and asks you please show me what kind of validation you did so then you can

1:34:30

straight away open up your jason schema and show hey this is the validation we used okay i'll give you

1:34:35

a core example i'll give you one more example i'll give you one more beautiful example let's say

1:34:41

tomorrow your requirements change our requirement change okay whoch okay new field that or you want the

1:34:46

application to do something else you don't have to open the jupiter notebook you don't have to open you don't have to

1:34:54

touch the jupiter notebook you don't have to open you don't have to touch the jupiter notebook you will only

1:34:56

open up your jason schema you will only open up your system message txt file and you can just make your

1:35:03

redits here if your if your application expectations are different if your final expectations are different

1:35:10

you're here here here here here just schema for modify kalli system prompt to modify and that's it

1:35:17

for testing purpose you can always go back to the jupiter and run the code but my point is if you hard

1:35:22

code all these things in your notebook then every time you have to go back to your notebook and do it

1:35:26

which is not the best way so this is the better way to manage the thing in a proper way

1:35:30

and just like we talked about prompt versioning the same applies for schema also you will

1:35:36

have schema versioning also and you have the version one here version two me

1:35:39

requirements change you might have a version two schema version three schema so there will be

1:35:44

different schema versions also right okay i hope this is absolutely clear to all of you

1:35:56

Ali i hope that answers your question okay okay um it's i think ubrage is more about

1:36:03

defining the limits in the schema and then validating the agent's output against them it's not a full

1:36:08

pleasure agentic session this one is not a we are not getting too much into agents in this

1:36:12

class okay so it's more about it's more about comparing the output with the schema okay so that's what

1:36:20

we are trying to do here okay so let's come let's come back and let's look at the next part okay let's look at

1:36:26

that the next part parsing model outputs safely what are the other things to take care of so far

1:36:33

we talked about creating the prompt text we talked about creating the jason schema these are two pieces we

1:36:39

talked about now we will be discussing what other things we should do to parse our outputs more accurately

1:36:47

what are the other things we can do to parse our outputs more accurately what we can do so let us see that

1:36:52

okay in the meantime uh we can take a short uh maybe five minutes water break if you want to

1:36:58

so let's take a quick water break and come back yeah guys can take a quick water break and come back

1:37:04

if you want apart from that if others want to ask me any questions i'm on open okay

1:37:10

so this will be only a few other things left out in the class today it's as i told you like

1:37:14

it's a lighter session in terms of the cold but the concept is very very important whatever we

1:37:19

are seeing here okay so yeah so people can just take a short break and come back

1:37:22

Thank you.

1:37:52

Thank you.

1:37:54

Thank you.

1:38:24

Thank you.

1:38:54

Thank you.

1:39:24

Thank you.

1:39:54

Thank you.

1:40:24

Thank you.

1:40:54

Thank you.

1:41:24

Thank you

1:41:54

Thank you

1:42:24

Okay.

1:42:27

Okay.

1:42:28

Okay.

1:42:30

Okay, guys, welcome back everybody.

1:42:54

here. So let's continue the conversation and what we will talk about right now is what else we can do with our outputs.

1:43:03

So we have defined the specific schema that we will use to validate and our output should come

1:43:09

in a certain format. That is one part. But what we have to do is we have to turn the model's raw string into a Python dictionary and then compare with a JSON.

1:43:23

Because what does the large language model return? Large language model is the output. The output of an LLM is a string.

1:43:30

The output of an LLM is basically a string.

1:43:34

So we have to take that and you have to parse it. What is the meaning of parsing?

1:43:38

Parsing means you are trying to take a certain output and you are trying to convert it into a certain format.

1:43:42

You are trying to parse it.

1:43:44

We are trying to extract some information out of it to get it into a certain format.

1:43:49

Because you cannot compare a string with a JST.

1:43:52

a JSON schema, right? Because what did I tell you all this file? We want to, we want to take that model's output.

1:44:00

Whatever raw string, the model outputted, we have to convert that to a Python dictionary,

1:44:05

and then we can validate against that particular schema JSON. This will be very easy to compare now,

1:44:13

because remember I told you JSON is like a dictionary. So the key takeaway is whatever output you are

1:44:19

getting, you should try to convert it to a dictionary. Try to convert it to a dictionary.

1:44:21

Try to convert it to a dictionary so that you can do a comparative analysis with that schema JSON.

1:44:27

So that is the big picture idea.

1:44:32

But very important, production code must clean first and then parse.

1:44:37

Parsing is actually very hard.

1:44:40

And I will tell you some real use cases here.

1:44:43

Back to our same, you know, this, this use case I talked about before.

1:44:48

Now, look here here here we're here we're saying here I'm bolder.

1:44:50

Here we're saying, okay, I will give the medication.

1:44:51

notes and please extract this information out of it. What was the output? I'm clearly

1:44:55

telling that, okay, you have to output a JSON. You output the following in a JSON format. This information

1:45:00

should be there. But what did the language model actually output? Did it give the output the way I

1:45:05

wanted? What do you think I actually need in this output? Ama chaiyea? Do I need this? This is a very

1:45:12

common issue. When you're when you're getting outputs from language models, this is called backtick.

1:45:18

Backtick is a small sign that you will see on your key.

1:45:21

I think if you take a look at it, your keyboard here.

1:45:25

Keyboard here.

1:45:26

The escape of the next sign is, back tick is.

1:45:29

This is the escape.

1:45:30

Top left in escape.

1:45:32

The escape in the

1:45:33

escape that is usually called the back tick.

1:45:36

That is the back tick sign and this is very common.

1:45:38

Backticks are very common in LLM outputs.

1:45:41

That is useless for me.

1:45:42

We don't need back tick.

1:45:44

Here they are Jason.

1:45:45

Jason, I don't want that to be printed.

1:45:47

It is printing a string, right? I don't want this to be printed.

1:45:50

My expectation.

1:45:51

expectation is only this part.

1:45:53

I mean, it's not so much.

1:45:55

All useless.

1:45:56

And this is the very real world challenge that you will face

1:45:59

when you're dealing with large language models.

1:46:01

Oftentimes, LLMs will respond with a lot of information,

1:46:05

but you actually don't need all that information.

1:46:09

One, our schema is,

1:46:11

but whatever output we are getting, we have to parse that,

1:46:15

we have to clean our output and then validate with our schema.

1:46:19

So a big part of what is.

1:46:20

A big part of what we are talking about is actually very important.

1:46:23

It's not just the, you make a GROC API call, you get an answer.

1:46:28

But whatever answer you're getting is that even what is expected?

1:46:33

Because that is a very important thing.

1:46:35

And how do we do that for the session perspective?

1:46:37

We have kept it very basic.

1:46:38

Right?

1:46:39

And I think as for our notes, if you see there are a few basic things we are trying to do.

1:46:43

Number one, we are trying to strip the markdown fences.

1:46:46

What the backtigs, we're trying to remove that.

1:46:49

Number two, we are trying to.

1:46:50

extract the main JSON object.

1:46:52

And number three, we are trying to parse that particular JSON.

1:46:55

Who JSON may say we are trying to extract information out of it.

1:46:57

These are the three broad things that we are trying to do, which I have demonstrated in a simple example here.

1:47:02

Let us see that.

1:47:04

So number one, what am I doing?

1:47:07

If the model puts mark down code blocks around the response, this removes them.

1:47:11

This is the same backtakes thing that I talked about.

1:47:14

So if I run this code, what will this code do?

1:47:16

Before, um, here peck function defined here.

1:47:19

This one you can ignore.

1:47:20

Yeah, there pithon code will regular expressions where you can ignore that.

1:47:24

But basically what it means is it is it is saying that okay, if you find this particular matching pattern,

1:47:30

if any of these kinds of special characters are present, you can please ignore it.

1:47:34

So I'm just defining this particular function.

1:47:37

This is like a, think of it like a typical data cleaning function in Python.

1:47:41

You can give it any dirty stream and it will clean that string for you.

1:47:45

It's like a template you can create it.

1:47:47

And here here what am I doing?

1:47:48

I'm just trying to call that function.

1:47:50

We are calling that particular function.

1:47:52

So before, my original LLM response was like this.

1:47:56

Exactly what I was explaining here.

1:47:58

LLM has my response here.

1:48:00

So this is exactly how my response is right now.

1:48:03

And after what will?

1:48:04

After response is this one.

1:48:06

You want to try my current this one.

1:48:09

It'll be interesting.

1:48:11

This can try this.

1:48:12

We can try this out.

1:48:14

You can try this.

1:48:14

And you will see the same kind of answer we will get.

1:48:17

The same kind of answer we will get.

1:48:19

The same kind of answer we will get.

1:48:19

Back ticker back, you can give some, give this information.

1:48:23

The same way you can enter this thing.

1:48:25

And what will happen is after, after what will happen is only this part will come.

1:48:29

So this backticks will be remote and this Jason will be remote.

1:48:32

This is what I'm getting.

1:48:33

So this is the first part of data cleaning that we did.

1:48:35

We have stripped it.

1:48:36

We have stripped those special characters and the word JSON and all that useless stuff from the strip up here.

1:48:43

Sometimes, some cases are jay characters are here,

1:48:45

is not very common, very common.

1:48:48

as you get into deeper into practice, I've observed it again.

1:48:52

Number two, step number two, we extract the JSON object.

1:48:56

Now, look, here here here, what happens is,

1:48:59

oftentimes, some text be a lot.

1:49:03

Yeah, that's the JSON's word to remove.

1:49:05

That is fine.

1:49:06

But it also has this text.

1:49:08

I mean, there might be some other stray text that might also come.

1:49:12

Okay, now, look,

1:49:13

this case, here is the output.

1:49:15

This we don't need.

1:49:16

Now, sure here is the output.

1:49:18

I mean, this is no, this is no, this is not like a special character, but this is like a stray text.

1:49:24

We don't want this.

1:49:25

We just want this portion.

1:49:26

And that is what the second function will do.

1:49:28

Second function will take any stray text.

1:49:31

I mean, my model output can come like this.

1:49:33

Sure, here is your output.

1:49:34

This is it.

1:49:34

Sometimes language model will output like, okay, here is the output.

1:49:37

But I don't want to see that text.

1:49:38

That text is useless for it.

1:49:39

I only want to extart from that, you know, from the here.

1:49:43

Now, look, here here here here.

1:49:44

I'm saying, text dot find the first.

1:49:48

curly brace, that is the start of my dictionary, and I want to find the end curly brace.

1:49:53

That is the end of my dictionary.

1:49:55

Or what start or end-ke-bechme, once you've got the indexes,

1:49:58

what start or end-ke-bechme, you want to get that string.

1:50:00

You want to return the text from here to here.

1:50:03

This is a bit of Python we are doing right now, but you can, this is what we are doing.

1:50:07

So we are finding out, find out the first curly brace, find out the last curly brace,

1:50:11

and get me all the text in between.

1:50:14

So this is the second thing that we are doing.

1:50:16

And the final thing that we are doing is,

1:50:18

Combine the steps above and safely convert the string to a Python dictionary using JSON.

1:50:24

Now all set.

1:50:25

We have we've made backtics removed the JSON word removed.

1:50:28

We've also removed any stray text.

1:50:31

Abhi, we have just here.

1:50:33

Now what we're going to do.

1:50:34

Now, this is what we will take.

1:50:37

We will take this thing.

1:50:38

See, see, this is the end, the complete end to end.

1:50:41

Complete end to end.

1:50:42

You will enter a string as input.

1:50:44

String, which is the model's response is.

1:50:48

User asks a question, language model gives a response.

1:50:50

Model-cage response, that will be the input here.

1:50:54

Models response will be the input.

1:50:55

First you call the first function, strip markdown fences, the first function.

1:51:00

So, probably you strip the markdown fences, remove the backticks.

1:51:02

Second, we call the second function, extract JSON object.

1:51:05

You remove the irrelevant text, step two, and whatever output you're getting,

1:51:09

you are now doing JSON. Loads.

1:51:12

So it will convert the string into a Python dictionary.

1:51:16

Very important because remember, whatever you are getting,

1:51:18

you're getting here.

1:51:19

You know, it is not a dictionary.

1:51:22

I'm sorry, it is not a dictionary.

1:51:24

This is the Python string.

1:51:27

This is string object.

1:51:28

The way to do it is you could take this string and you have to run this command, jason.

1:51:32

Dot loads and that will convert it to a dictionary.

1:51:35

And this is what this particular code will do.

1:51:38

Okay, you can actually print out your data.

1:51:41

You can here data for print for you can take a look at it.

1:51:44

You can, you can take a look at your data.

1:51:47

Sorry, I think.

1:51:48

We have to do it inside the function.

1:51:50

We have a print statement color because this is like a local variable.

1:51:53

So we can print our data here.

1:51:55

We can print our data here.

1:51:57

We are calling the actually we're not calling the function.

1:52:00

I'm sorry.

1:52:00

We're not calling the function yet.

1:52:02

So we can go back and print our data.

1:52:05

And once we print our data, I'm actually doing the validation in the next step.

1:52:09

Next step may I'm actually doing the same thing.

1:52:11

So we can print our data.

1:52:12

And if you print your data, now that data will be like our dictionary.

1:52:15

Okay.

1:52:15

Dictionary dictionary.

1:52:17

Okay.

1:52:18

So this is.

1:52:18

This is the complete end result what we have achieved.

1:52:20

So just to walk you through again, we get the raw LLM response.

1:52:27

Your car raw LLM response here, which is basically in a string format.

1:52:32

This is this language model response is in a string kind of a format.

1:52:38

First, we are doing strip markdown pences.

1:52:42

First we are doing strip markdown pences.

1:52:44

Next, we are doing extract JSON.

1:52:48

And next we are doing JSON. Loads.

1:52:56

And what is this last step doing?

1:52:58

This last step is used for converting this to a dictionary.

1:53:01

Because until now, everything is a string.

1:53:03

Here here this one step here, we've made backticks removed here.

1:53:06

Irrelevant text removed.

1:53:07

It still remains a string at this point in time.

1:53:10

Here I'm converting it to a dictionary.

1:53:12

And what is the last thing we will do?

1:53:14

Just to complete the flow.

1:53:16

What is the last thing we will do, guys?

1:53:18

The last thing would be, we will simply compare this with our schema.

1:53:22

The schema dot JSON, we already saved here.

1:53:25

Now we can easily compare.

1:53:26

Because now, this be dictionary for got.

1:53:28

This is a dictionary kind of a format.

1:53:31

So now we can compare that too.

1:53:32

I hope everybody is aligned with what we are doing.

1:53:36

Okay.

1:53:36

And I think as one of you were mentioning a while back, I think Ankit was maybe saying, I think,

1:53:41

this is something that we will do in a much better way using Pidentic later.

1:53:45

Just wanted to mention the term, but don't worry about that.

1:53:48

now. Okay. So this is only the first session of this. But down the line, we will

1:53:52

explore something called Pidentic, which will do the same kind of data validation in a much more

1:53:56

robust way. But the ideas will remain very, very similar. The ideas will remain very, very similar.

1:54:03

Okay. So now let us, let us look at the complete flow. This is your F-validate underscore ticket function.

1:54:10

And just to kind of clarify that here we have given a nice kind of a diagram to explain exactly what

1:54:15

we talked about. Up there for messy model output.

1:54:18

in fences and extra text. This is the thing I was talking about, like, here

1:54:21

your back takes are, this is typically how the, how the language model will return the answer.

1:54:26

Exactly the story that was playing out in my medical notes example,

1:54:30

after asa answer will, but we don't want that. We want to clean it up.

1:54:33

So you're strip car over, so what will, jason-wala thing that. This is how you will get it.

1:54:37

The final jason extracted will be like this. And then what you will do, you will do jason.

1:54:41

That we convert it to a python dictionary like this. And you can extract the information neatly.

1:54:46

Status is this, message here, code, here, read,

1:54:48

and this is the thing that we want to achieve.

1:54:52

Okay. So these are some of the things that we are doing. And the last part that we will do is

1:54:56

we will add that validate ticket. The validation part is what we will be doing. So the validation

1:55:00

part is what we'll be doing. And why is validation important? These are some other things to keep in

1:55:05

mind. Okay. This is the end result what we are trying to achieve. The validation part.

1:55:10

Okay. Can we use the React thought action observation within Jeson schema? Uh,

1:55:16

Ankit, uh, react. Yeah. React.

1:55:18

So that depends on your agent use case, right?

1:55:21

If a agent's use case, then you can definitely do it.

1:55:24

It depends on your agent use case.

1:55:27

Ah, it's possible.

1:55:28

Jason schema can structure the agents action, action, action, input, observation and final output also.

1:55:34

But in production, the way you usually do it is you validate tool inputs and final answers.

1:55:40

Thoughts up use naked. But what you, what you do in production is that, you know, you will use your

1:55:45

tool inputs with the final answers. So today I am not.

1:55:48

integrating the react thing here, but we'll, we'll

1:55:50

we'll back me, we'll. I think there it is better done using PIDANTIE.

1:55:58

It will be a better way. But yes, just to clarify, when it comes to agents, when we will see

1:56:01

the agents part later, we will use the tool out, the tool calls, basically.

1:56:07

Because what are you, what are you outputting in an agent? Agent, out, agent's output

1:56:11

what is basically like a tool call. So based on a particular question, you're trying to decide

1:56:16

what tool to call.

1:56:17

that tool execute

1:56:18

that tool answer. So agent my

1:56:21

workflow is a little different, which we have not

1:56:23

focused on today. That's not the focus, but

1:56:24

we're going to be back in, how to react

1:56:26

how can. But to answer your question, you can,

1:56:29

but in a slightly different way.

1:56:32

Ali, not really. It's actually very easy.

1:56:35

Because I've talked about so many things today,

1:56:37

it might look a little confusing, but

1:56:38

okay, let me summarize for in two minutes what we did.

1:56:41

Two minutes in two minutes, what I did, let me summarize.

1:56:43

Step number one, we've made jason's schema

1:56:45

created. I think you're okay with that.

1:56:48

I'm a schema created. This is our

1:56:49

validation team.

1:56:51

Step number two, we have system message created.

1:56:53

System message is needed because you want the language

1:56:55

model to generate the output in a certain manner.

1:56:58

So step number one, we have schema

1:56:59

created. Step number two, we

1:57:01

we've Jason's, the system message

1:57:03

text was, that created.

1:57:05

Are you okay with me until now?

1:57:08

These two things, you're absolutely fine.

1:57:10

Okay, let's.

1:57:11

Let's go. We're just three

1:57:13

functions discussed here.

1:57:15

Function number one, strip mark down fences, remove backtick.

1:57:19

Backtick, out.

1:57:21

Function number two, irrelevant text

1:57:24

I mean, like, if it's like, if it's

1:57:25

it, it's like, it's like, it's

1:57:26

this kind of it. This is function number two

1:57:28

and function number three,

1:57:31

function number three,

1:57:33

please convert it to a Python dictionary.

1:57:35

Three function we've used to.

1:57:38

The first function we're here call

1:57:39

what will this function do only? It will remove the backtick.

1:57:43

Second function, it will remove any irrelevant text.

1:57:45

And third function will convert the final string

1:57:48

that I'm getting into a Python dictionary.

1:57:50

That's our final output.

1:57:53

Are you with me?

1:57:54

Is it okay?

1:57:55

Three function I'm used here.

1:57:58

Yeah, to your file.

1:57:59

Chotha function is just for validation purpose.

1:58:02

That's it.

1:58:02

It's just a validation part.

1:58:03

I'm yet to talk about it.

1:58:04

This is just the validation part.

1:58:05

But until now, we have only used three functions.

1:58:09

Now, coming to the,

1:58:12

coming to the validation part,

1:58:14

I hope you are okay.

1:58:14

Ali, let me know.

1:58:15

Is it fine?

1:58:19

Three functions I've used, okay?

1:58:20

Only three cleaning functions we have used.

1:58:23

Okay?

1:58:23

If you have any doubts, please ask me.

1:58:25

I'll repeat it again for you.

1:58:27

Okay.

1:58:29

Here we're finally validation

1:58:30

are.

1:58:32

So validates the fast data

1:58:34

against our required business rules.

1:58:38

And required business rules

1:58:40

in what will?

1:58:41

Required business rules is nothing but our schema.

1:58:45

So here basically we

1:58:47

have our JSON to parts

1:58:48

and the output

1:58:50

is here we're comparing

1:58:51

that is basically

1:58:54

what we are doing here.

1:58:56

So I will run this

1:58:58

for the time being.

1:59:00

Let's,

1:59:00

let me explain this to you

1:59:01

and we are putting this entire thing

1:59:02

together into the final grog pipeline.

1:59:05

So all that it is doing is,

1:59:06

it is checking?

1:59:07

That by the keys are, is it in the required keys?

1:59:10

What I mean,

1:59:11

the five keys are it within the required keys?

1:59:14

Are all the categories within the

1:59:15

allowed categories and are all the priorities within the allowed priorities?

1:59:19

I should not have a priority beyond these values.

1:59:22

So we are checking if everything is in the right set of values.

1:59:25

Are all the keys coming and are all the keys in the right format?

1:59:29

Some of the things we are testing.

1:59:31

And this is the full GROC pipeline that we are using right now.

1:59:34

Abdeco, here here what I'm doing.

1:59:36

First I'm importing grog.

1:59:37

I'm instantiating the API key.

1:59:40

The model name is Lama Versatile.

1:59:42

And we are loading the system.

1:59:45

message, system message is already saved in the TXT file.

1:59:49

So what I'm doing with open, with open, system prompt is equal to this.

1:59:54

This is my system prompt.

1:59:56

Okay?

1:59:57

This is my system prompt.

1:59:58

We can already see that.

2:0:00

Or this function, when we call k, this is like my user prompt.

2:0:04

Whenever I call the function, this is my user prompt.

2:0:07

This is your system prompt, which we've already defined here.

2:0:10

Or when I call this function eventually, this is going to be like my user prompt.

2:0:14

Based on that, you call the grop.

2:0:15

model, you get the response.

2:0:17

And also very important is, when you're going to, we also give another additional argument

2:0:22

saying this.

2:0:23

This is also slightly new.

2:0:24

We have discussed not earlier.

2:0:26

But this is the nice way you can force Grog into JSON syntax mode.

2:0:31

So language models may have this way you can output.

2:0:32

So one is you can explicitly write in the system message, okay, generate a JSON and all that stuff,

2:0:38

what we were doing.

2:0:39

Right?

2:0:39

We were saying, okay, please, output in a JSON format.

2:0:43

But you can also explicitly give an argument saying,

2:0:45

response format equal to type JSON object.

2:0:47

You can't say you.

2:0:48

So you will get the raw output.

2:0:50

And I already told you that raw output can contain problems.

2:0:53

A lot of problems can.

2:0:54

The story remains the same.

2:0:56

You've made input message via.

2:0:58

The input message basis,

2:0:59

the response got created.

2:1:00

But the response may not be clean data.

2:1:02

So you take that raw output and what you do,

2:1:05

you go and first,

2:1:07

you go and take that raw output and you just parse that entire output.

2:1:12

You call that function safe parse model JSON.

2:1:15

This function three things.

2:1:17

First, back take remove.

2:1:18

Next, it will remove an irrelevant text.

2:1:20

And third, it will finally give you that parsed dictionary out of it.

2:1:23

All of you recall that now.

2:1:25

So from that raw string output, I'm getting a nicely parsed dictionary.

2:1:32

Nicely parsed dictionary.

2:1:34

This our dictionary output is.

2:1:36

And the last thing that I will do is I will take that dictionary output, the language model returned.

2:1:42

And I will compare that dictionary output with my language model returned.

2:1:42

And I will compare that dictionary output with my.

2:1:45

my JSON schema.

2:1:47

And, and us' basis, I'm, you know, I will get a response.

2:1:53

I'm comparing this with my JSON schema.

2:1:55

And this is exactly what the validate ticket function is doing.

2:1:59

So validate ticket in what I'm doing.

2:2:01

I'm simply comparing the dictionary output with the JSON schema.

2:2:06

And you can run a live test.

2:2:08

We can run a live test right now.

2:2:09

Now, look, here here we have an example defined here.

2:2:11

Where is my order 4-4-1-2?

2:2:13

It was supposed to arrive yesterday.

2:2:15

I was charged twice.

2:2:16

I'm just giving a couple of message samples right now.

2:2:18

If I run the code, you can see what me, let me execute the code right now.

2:2:24

If I run the code, you can take a look at it.

2:2:26

The customer message was, where is my order 4-4-1-2?

2:2:29

It was supposed to arrive yesterday.

2:2:31

And on the basis of that, the raw model output.

2:2:33

So what is happening?

2:2:35

You have a message.

2:2:36

This one-pail-vall-s sample is right?

2:2:37

So the first sample, you're printing the sample message.

2:2:41

Your sample message is where is my order?

2:2:44

Right.

2:2:44

So this is like.

2:2:45

the user message. You are calling the function classify message with the parameter

2:2:48

message. Okay, so basically this is like your user message now. And on the basis of that

2:2:54

user message, you are going to generate the response and the response is coming out like

2:2:58

this. You have a raw model output response. Okay, so this is not in the, sometimes it can have

2:3:05

issues. So we are now we are parsing and the dictionary is returned. This is that final dictionary

2:3:11

that we are getting. What are they? Saktio, I think, like in this

2:3:15

particular case you can see that indeed, you know, the everything is perfect because you can

2:3:21

see the categories within the respective buckets, priorities within the respective buckets, priorities within

2:3:24

the respective bucket, summary missing is correct. This is expected. So all these fields are

2:3:30

returned exactly the way we expect. So my, my JSON schema is match. And this matching is happening

2:3:36

is happening in the validate function. Validate function in the validate function. Okay, this is exactly.

2:3:42

How we are validating we are doing in the validate function. We are passing. We are passing

2:3:45

that output, you are passing that output, and you are comparing that with what?

2:3:49

We are comparing that with what? We are basically comparing that with our, this thing. We are

2:3:54

comparing that with our keys, whatever our adjacent is basically. So here, Ali, what we have

2:4:01

done is just for simplicity, I've hard coded this year. I'm here here here put put here. But if you want

2:4:06

to get a little deeper, what we will practically do, what we will practically do is we will do it

2:4:12

this way. Okay, this is what we will practically do.

2:4:15

what are we doing we are loading the schema okay so here the code is a little messy

2:4:21

what what what we have done that's why I wanted to simplify the code a little for you but since

2:4:25

you want to understand the the actual thing this is how it will look like you will load your

2:4:30

schema you will load your prompt you have your schema. jason dot loads whatever schema you created

2:4:35

you will load your schema and you will load your prompt and you will get the response

2:4:39

response say you will get the parts response and you will call this validate function and of the

2:4:45

Therefore, validate function, there are two inputs that you are passing. You will give the

2:4:49

past final response, your dictionary and you will also pass the schema. So the validate function will take

2:4:56

these two inputs and it will return either correct or whatever it is. This is your validate or raise

2:5:01

function. And if you want to see, sir, what is happening inside the validate or raise function.

2:5:06

Let me show you, this is what is happening inside the validate or raise function. This is what is going

2:5:12

on. The validate function is taking these two things and

2:5:15

input. It is taking the dictionary. That means the predicted response it is taking

2:5:20

as input, the language model, what is returning, and it is also taking the schema as an input, and it is comparing

2:5:25

the two. How it is doing? This is back to some Python that we are doing right now. You can see that

2:5:30

in that schema, we are checking the okay. Is the key, whatever key you're getting in the output,

2:5:38

is that matching the required parameters? Okay.

2:5:45

Now, right? So I did not want to run through the entire thing. That's why I didn't want to confuse the others, but I just wanted to take it.

2:5:52

So this is the way we are doing it. So you are you. So you're doing it. So you're

2:5:54

both of the simplicity for what I have done, I have hard coded these values. Actually, this

2:6:00

this is. This is your JSON's here. I think I can just do it for you. Just so that people will refer to this code.

2:6:07

These are, these are hard coded for the demo.

2:6:15

these will actually come from the JSON schema file.

2:6:25

So you have my code which will run perfectly and you also have another sample code we will

2:6:31

give in the content where we have given you that part.

2:6:33

You have schema say loaded and check the idea remains the same.

2:6:36

Okay, so you have allowed categories.

2:6:39

The only thing is that instead of hard coding it, you can pull it from the JSON and it is not very hard

2:6:43

to do it.

2:6:43

So allowed categories for how can you do it?

2:6:47

You can go to the JSON and you can extract the allowed categories.

2:6:53

What is your required variable basically?

2:6:56

So you have to just say that JSON file got required.

2:7:00

So what are the values of that required?

2:7:03

So instead of hard coding that particular dictionary,

2:7:05

you can just fetch it from here.

2:7:06

So that is the only thing.

2:7:08

That is the only thing.

2:7:10

That is the only thing.

2:7:10

Okay, I hope everybody's clear.

2:7:13

Everybody is aligned on this and you can take a look at it.

2:7:16

So my schema is perfectly matching right now.

2:7:19

And you can also simulate one more use case where let's say the cema is not matching.

2:7:23

Of course our input the schema is not matching.

2:7:26

You can check it.

2:7:26

Maybe you can also try to change the system message.

2:7:29

You can try to generate a different kind of thing and you can see the output.

2:7:32

So a big takeaway of the session was how, you know, validation is so important.

2:7:37

And you can see some examples here on the final thing.

2:7:39

We can see some examples.

2:7:40

here. Let's say, you know, this is the output we are getting type refund, amount is this,

2:7:45

currency is this, this is what we are getting. So this is, you can see this is failing.

2:7:50

You can, this is failing because it is not matching the business tools.

2:7:53

These are a required fields.

2:7:55

Yeah, yeah, this is fail. Why will? Because here all the fields are. See, only the

2:7:59

LLM responded with type amount and currency. But, you know, this is like a gatekeeper,

2:8:04

validator. Validator says, hey, I need all the five fields. But you have only three. I will not allow you.

2:8:09

I will not allow you. I will not allow you. So these three are rejected. Turns out this guy is allowed.

2:8:15

Why is this now allowed? Because type, amount, he, currency, needs human, category. All these are there.

2:8:21

And all these are following the right business rules like what we discussed. So this guy, output isn't the exact perfect format.

2:8:29

And this is exactly what the validation will do. So we take the raw LLM response. We parse it. We clean it.

2:8:34

And we get the final dictionary response. And we compare that dictionary response. And we compare that dictionary response.

2:8:39

with the JSON schema. And based on that, we pass them through. And that is actually what is routed to your

2:8:46

UI. That's the user interface in. Because if you don't parse it, if you don't do that cleaning,

2:8:52

if you have the wrong data, this problem, now you will tell me, you, sir, why do it? Because if you're the

2:8:59

gatekeeper, you're the gatekeeper and you allow this guy to go here. You have this guy to go here.

2:9:02

You have it allowed this to allow it here. So what problem will? Problem here here here here

2:9:07

There are type amounted currency. Here here. Here, there's need, human, value. So,

2:9:11

it's what can't what will I put here? So when you go to the front-end user interface, I don't

2:9:17

have a value to add here. Here. Here here category, even. So category we're

2:9:22

we're going. Now, a ticket you're raising. That category is a category, it's a required field.

2:9:26

If you don't have a category, what support ticket will you raise? So how can you allow that person

2:9:30

to pass to the gate? You cannot. That is why data validation is important. So again, it is about the big

2:9:35

picture. We have not murder.

2:9:37

the agent's angle here, but this was a generic discussion to help all of you understand and appreciate

2:9:41

why. Why is parsing important? Why is parsing very, very important? Okay. So it's a very

2:9:48

light session comparatively if you see. I think the takeaways are not much. Jason schema we saw. And we also

2:9:54

explored a few functions that we can use to clean our model response. And most importantly,

2:10:00

you know, the part where we are comparing the output with our schema. So that these are the

2:10:05

core takeaways for the session. So the content is already shared with you. I've

2:10:10

already shared the file on the 23rd June folder. I've added some comments here so that it's easy

2:10:15

for everybody. So you can run the code. This will hardly take a few minutes to execute. You guys can

2:10:19

run the code. Take some time. In the meantime, if you have any questions, we can take it up. But I hope

2:10:25

everybody is clear with the session. All if you're okay. Everybody is absolutely clear. In fact,

2:10:30

next session, we are starting out with agents. This will be another very interesting plus. So we'll

2:10:35

use these learnings going forward. It will be a end-to-end workshop we will do on rags and all that

2:10:40

we have discussed so far. But yeah, I think just to kind of clarify the today's session once again,

2:10:44

so we talked about the JSON schema. What is the meaning of a JSON schema? Prompting the model to

2:10:49

return the JSON that conforms to the schema. We are writing a proper system message. We talked about

2:10:55

that. How we are creating a system message to return the right JSON. Parsing the model output. We talked

2:11:01

about three functions particularly, how we do that. And finally validate the

2:11:05

required field some work as a validation. So whatever output response I'm getting, how do we

2:11:09

validate it back with the JSON schema that we originally created? Okay, so these were the key takeaways

2:11:14

from our session today. Any questions? Rajdip is clear. Thank you, Rajdip. Others are all okay.

2:11:19

Do let me know. Final check. Everybody's clear, guys.

2:11:35

Okay, I'm here. I'm here for a while. In the meantime, Arsita, I mean, over to you. Over to you. You know, I think

2:11:43

Vishal has asked a question. Vishal, uh-huh, you've asked him in Q&A. So, uh, let me take it up. In the

2:11:53

meantime, Arshita, you can take over and I will, I primarily answer Vishal's question. So,

2:11:57

Vishal has asked a question, sir, well, applying a rag engineer role. So demonstrating

2:12:01

functionality is the minimum, I would say. But Vishal, for a rag engineer role, but Vishal, for a rag engineer role,

2:12:05

it's much stronger if you package it like a real product, I would say.

2:12:09

Maybe a small deployed web app or clean API, you know, maybe a API.

2:12:14

Just say Gradyo in whatever we talked about. So those kinds of things would be good, right?

2:12:18

What we have, what we have done. So you want to show it. Like, just a Tesla demo we saw,

2:12:24

Vishal, right? So up end users to do what you actually did. Right? Maybe a clean GitHub repo,

2:12:30

an architecture diagram, make an architecture diagram. You know, you take the document, you

2:12:35

the chunking, very similar to how I explained in the class. So those things, you know,

2:12:40

so what matters most is showing the retrieval quality, chunking, embedding choices,

2:12:45

citations, latency. Latency is also important. How long it takes to get a response. It's not

2:12:51

always the accuracy visual. Accuracy to take, you can write a good prompt and you can get an accurate

2:12:55

response. But imagine in the real world, if a, you know, if a system takes 10 seconds to give a response,

2:13:00

nobody will wait. So the latency is actually a very important factor.

2:13:04

right? So these are all very, very important ideas of, you know, I hope this is clear,

2:13:12

Vishal. Okay?

2:13:15

Answers your question? Let me know.

2:13:19

Good. I know there are few career-related questions people have, and I plan to take this, you know,

2:13:23

we can have a separate session career. So a lot of you have these questions on careers and roles and all

2:13:29

that. I've talked to the team. We might do a master class sometime. I think it will be helpful.

2:13:34

use these learnings going forward, how you can incorporate in your resume,

2:13:38

GitHub is one aspect, that's where repo how can make us. I think these kind of things we can,

2:13:43

you know, we can talk about another session. Yes. Okay, any other questions, guys?

2:13:53

Yeah, yeah, yeah. Yeah, we can we can keep a session for that. I, you know, it will be helpful,

2:13:57

of course. Yes. Yes. Yeah.

2:14:04

Okay. How this module will keep our learning in next module. Next module is more into the advanced agents, Ubrach. If you ask me, how is the next module relevant?

2:14:29

And, yeah, so next module is more into this thing. If you, if I go back to the, you know, the, maybe the detailed curriculum also.

2:14:39

So just to walk you through it overall at a very high level, so we are getting into complete agent development in the next module.

2:14:46

If you look at the contents of the next module, we're going to long graph in, that is totally into agents.

2:14:51

This module kind of plays the foundations for a lot of what we are trying to do, right? We talked about API calls.

2:14:58

We talked about latency. We talked about.

2:14:59

writing a prompt. We talked about versioning. We're talking about outputs parsing.

2:15:04

Rag got, a little agent got. But we are getting deeper into agents in the next module. So we start

2:15:11

off with advanced rag. First three sessions are on advanced rag. And the next module onwards,

2:15:16

we completely get into advanced agents. Langraph is actually a very popular framework that we use for it.

2:15:22

I mean, Langchain, Thora both have made, but Langchain, we will see React framework again. We will see some

2:15:28

examples of that again. Yes. Landchain kind of, we see, we look, we look,

2:15:31

basically. But you have to remember, Langchain is more of an orchestration library. It is just a

2:15:37

library that we have. But we'll be explore it again. Yes, we will have some more demos for that again.

2:15:42

And the other, the second aspect, Ubrach, what the next module will cover is on the deployment part.

2:15:48

Because all this while we are discussing about development.

2:15:50

You've made some use case, you built something. But the next module will focus more on the deployment part.

2:15:56

How do we deploy it?

2:15:58

Right. So maybe create a streamlit interface and a little bit of LLM ops.

2:16:03

These are some very new ideas that we haven't talked about.

2:16:05

Let's say a prompt baner you. How do you keep a track of it? What kind of responses you are getting? How do you save it?

2:16:11

So we'll see a much better way of doing things.

2:16:13

Like we made from prompt versioning discussed here last session. Okay.

2:16:17

Prom versioning made, it was very basic. We talked about a prompt registry. But that's not the best case of best way of doing it.

2:16:23

In reality, we use tools like ML flow. We use other tools to version prompts in a better way.

2:16:28

it. We will see some more advanced things in this particular lake of the journey,

2:16:33

specifically on LLMOP. Docker is not a big part of the session because Docker is in a different

2:16:38

direction, Ubrach. It's not part of the general modules, but some of these additional things we,

2:16:43

you know, we might keep some master classes for it. But it is not part of the regular model because

2:16:47

Docker will get into a different direction. That's a little infrastructure in. But yeah,

2:16:52

when we are talking about LLMOX, I can, I can introduce personally from my end. I'm a little introduction

2:16:57

but it is not part for Docker Kubernetes is a very different thing.

2:17:05

Chalo.

2:17:08

Ankit, you've got a question. I wanted to just take up this last question.

2:17:11

Because latency matters, but reliability also matters.

2:17:14

Both matter. Latency is also tenacity and retrys are for transient features like rate limits,

2:17:19

timeouts, flaky APIs. Why did we talk about that?

2:17:22

Retry? Why do we? Because if API timeout, then then then then what?

2:17:27

Like, all these things we are doing to, like, with the assumption that my application will

2:17:32

work. If your API itself is timing out, you're getting a 401 error, then nothing will work, right?

2:17:38

So those are there for a different aspect. But, but, but, but those are error handling things.

2:17:45

Apisco SSO, they are like try except blocks. What if there's an issue? What if there is a problem?

2:17:50

What if there's a rate limiting I'm facing? Then we will do retrys. That is the way to look at it.

2:17:55

Okay. So yes, you keep retrys.

2:17:57

all use some back off and you balance reliability against the added delay. There'll be some

2:18:02

delay, but that's one way to look at it. Okay. Okay. Okay. So, Arsita, over to you. We are just,

2:18:12

I think, five minutes out of time today. But yeah, thank you to the Azas for waiting. So maybe

2:18:17

with the mentimeter quiz is there. So you can take it up. And I will see all of you in the next session.

2:18:24

Thank you, everybody. Yeah.

2:18:27

Thank you very much for the wonderful session.

2:18:31

Students, the poll is already done. So if you have run the code, please type in the chat box that you're done with it and you're able to run it successfully.

2:18:57

Okay. I suppose everybody should be comfortable. Very simple code. Just execute it. Okay?

2:19:06

Should be able to do it within a matter of human age.

2:19:11

Sangita error not should. Ideally, you're starting. Go to restart session, start right from the beginning.

2:19:18

Ideally, it should work fine. Maybe somewhere it could have happened to you executed some intermediate cell.

2:19:24

So variables could override for. That could be one.

2:19:27

reason. You just restart session, safe side.

2:19:31

Sure, start. Run all the cells in the order.

2:19:34

Yeah, or one more thing

2:19:35

is it might maybe you're running some cell or

2:19:38

some cell or some cell previously you've got done execute. So

2:19:40

could variable not defined are

2:19:43

here. Sure. Sure.

2:19:47

Okay. Okay. So I hope

2:19:51

it is running for everyone.

2:19:53

Sangita, you can follow the suggestions given by sir. If

2:19:57

If not, then we can try it again in the TA session one more time.

2:20:02

So we will close the session here.

2:20:03

Thank you everyone for joining it and thank you, sir.