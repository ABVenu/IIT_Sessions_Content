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

Hi, everybody, very good evening.

12:13

We're just starting waiting for all to join.

12:16

Just maybe another few minutes we will wait and start on.

12:20

Hope all of you are doing good.

12:36

Thank you.

13:06

Thank you.

13:36

Thank you.

14:06

Thank you.

14:36

Hi, folks. Yeah, we just start on.

14:42

And as always, I always like to start my classes with a, you know, a quick introduction, very quick doubt clearing.

14:52

So any, any questions people had from what we discussed in the last session, right?

14:56

We started off with SQL.

14:58

So you got some time to probably, you didn't get a lot of time, I know, but you got a day's time or.

15:06

So anything you would like to ask me from the last session, something that you, you know, that you had any questions on?

15:14

I remember the last class there was a quiz that was asked, order of execution.

15:18

So I will discuss that once again today just to let you know, because today we are actually completing the whole flow group by having.

15:24

So, so, such, the order of execution, we'll talk about.

15:27

But any other general questions that you would like to discuss, we can take a quick five minutes for any basic Q&A that you would like to do with me.

15:36

before we start on with the flow.

15:39

Anybody?

15:40

Anybody wants to ask me anything at all?

15:43

Please.

15:47

And you know, guys, I always say that you are the folks who make the class successful.

15:51

So please try to ask as many questions as you can.

15:53

Second thing, what I always encourage people to do is set your chat settings to everyone.

15:58

Let's say, ask you, questions, put you going.

16:00

Everyone will get to know what you're asking.

16:02

So don't send it to only hosts and panelists.

16:05

So it's just between.

16:06

So when you're asking any questions or when I'm, you know, putting out something, let's not do private chats.

16:12

Let's all involve the whole class, take it.

16:14

Sub subset for no to everyone.

16:16

Otherwise, what happens is no, like, you will feel like there's nobody, like there's no response.

16:20

Like nobody's swinging anything.

16:22

So just set it to everyone.

16:24

I was, we have also enabled from RL.

16:26

So subset for no, everyone went.

16:28

So that like the class is interactive.

16:30

So whenever people are asking questions, everybody knows.

16:34

Okay.

16:35

Okay.

16:36

Great.

16:43

Harsh, again, you are sitting to hosts and panelists.

16:46

Okay, I'm just, yeah, because, you know, it's okay, you know, guys, I'm just letting you know.

16:50

Some of you might not know.

16:52

So you will see our small option below zoom.

16:54

Everyone is.

16:55

So that everyone can.

16:56

Okay?

16:57

Uh-huh.

16:58

Yeah, yeah.

16:59

Prath is also helping you guys.

17:01

Okay.

17:02

Great.

17:06

Okay.

17:07

Okay.

17:08

Okay.

17:09

Contents for the session, as always, I will make it a point to upload it right in the beginning

17:14

of the class and you can all navigate over to, uh, okay, let me share my screen.

17:19

I think my screen is not shared here.

17:20

Cheers to second, guys.

17:22

Here's the second.

17:24

Okay.

17:25

Excellent.

17:26

So, if there are no questions we can see.

17:35

we can start on. And today is 29th of April. So new folder and all of you can find

17:45

the contents of today's session under the 29th of April section. Okay. And you can

17:51

please navigate to this folder and you can find the content. Okay. All if you can see this

17:56

here. So today I have actually kept some exercises, some proper exercises. Last class, unfortunately,

18:05

those exercises were, unfortunately, the solutions were shared with you. But today,

18:10

I have consciously kept some exercises where the pattern that we will follow today is I will show you

18:16

one SQL query or sart-sat-sa-up, we have exercises. So that is the whole objective, right? Otherwise,

18:22

the setup remains very similar. You will be using the SQL, the same SQL compiler that we used

18:31

last session. So please use the same one.

18:35

compiler. Dot MySQL that we used last class. And that is the basic editor that you

18:39

will be using for the session today also, right? I hope everybody remembers in case you

18:43

have forgotten that, this is the IDE that you need to use. And if some of you are using MySQL

18:49

Workbench, please feel free. Please feel free. You can use that also. But since it is not a

18:54

very detailed and deep database module, we are not encouraging you. If you want to set it out

19:00

just for learning, if you're going to understand for installing it, if it's absolutely free. Please feel free.

19:05

But otherwise, you can just do the demos.

19:07

SQL remains the same irrespective of where you are doing this stuff.

19:12

We are trying to, we are trying to ensure that you understand the syntax, the queries,

19:18

what the queries are written.

19:19

The focus is not too much in understanding a database.

19:22

The database is a massive product.

19:24

That a laxai module, a other side course, but relevant to agentic AI,

19:29

relevant to AI, whatever SQL is required, that is what we are teaching you at my side here.

19:34

Okay.

19:34

So do not try to get deep into a MySQL course. And some of you might be like going to

19:39

W3 schools and seeing some demos. So that very extensive thing. You can ask me questions. I'm happy

19:44

to answer any kind of question. But generally from a course perspective, we are not venturing into

19:49

very detailed topics in SQ1. Okay. Okay. So let's start on. Today, what is the broad

20:00

agenda of the session? I wanted to quickly call.

20:04

follow out the agenda what we are going to be discussing. We're going to be discussing joints.

20:08

And we're going to be talking about group by having and joins. These are the three primary

20:13

things that we're going to be covering in the class today. So that will be grouped by having and

20:19

joins that we'll be discussing today. Okay. And just as we covered in the last session,

20:25

we will be seeing that the parallels with respect to pandas. You have made pundas and same pattern

20:33

we'll follow. We'll focus on.

20:34

on SQL and we'll see the corresponding similar demos with respect to Pandas.

20:38

So without any further I do, let's get going. Okay. Let's get going. Okay.

20:44

So before that, let me quickly go back and talk about the broad structure of a query that we wrote

20:54

in the last session. If you want me to show you that, just so that everybody is aligned,

20:59

everybody is absolutely sorted or his related, a question asked,

21:04

quiz may I remember, the order of just one second, the order of execution of a select query,

21:12

let me start right from there and then we'll get into the Pandas one, group by part, actually.

21:22

Just a second, size.

21:31

And do not worry, I'm trying to do not do this in my SQL database.

21:34

product so that you get a complete flavor of this also.

21:38

So you can this, you can't, you can see, absolutely fine.

21:41

But you are free to do it on the one compiler.com.

21:45

Okay.

21:45

So, so first what I will do, I have got the Maasai Analytics database.

21:50

So first we're delete it.

21:52

And if you remember, we have discussed that these are all databases.

21:56

Our first thing is database management system.

21:59

It's in there's a quite many databases.

22:00

New schema, Sakela, Scyl, Scyon, these are all databases.

22:03

and what we can. Let me open up today's script. This is a script for today. I can easily

22:09

load it up. Let me quickly load it up here. And this is what I will broadly walk you through.

22:15

Okay. Same way, you up is go one compiler. Right now, please follow along.

22:21

Sart-up. So right now, you please follow along. Then you can do along with me later on. Okay.

22:26

So, so first, what I will do, I will go and quickly run the initial part, create a database.

22:32

So first, S-11, our session 11, right? So I will create a database called Masai Analytics S-11.

22:38

So let me show you step-by-step how is happening. And at any point in time, if you guys get stuck, please ask me.

22:43

Please don't hesitate to ask me, okay? So I will quickly execute this query. And the moment I execute the query,

22:49

this we'll filter it. Now, look, here here here a database been, okay?

22:52

Masai Analytics database been. It's in under, we're all the tables stored. Okay?

22:55

Okay, we will use a command called Use Maasai Analytics S11.

23:00

This means what is?

23:01

This means we are going to be using this database for doing all our future work.

23:06

And a very interesting thing we'll observe.

23:08

This, this is the my SQL workbench is, in this kind of, as you have this query execute

23:12

are, you. You know, currently this new schema black in, bold in.

23:16

Bold, it means, it's current active.

23:18

As we're going, as we'll execute it, you, you know, see, very interesting.

23:22

That means, this is my active database right now.

23:25

So here is from schema. Schema and database are one and the same thing.

23:28

If you look at the terminology of my SQL, schema and database broadly mean the same thing.

23:33

There are some general differences, but they mean the same thing.

23:36

Now, next, what I will do, within this database, there are no tables that exist.

23:40

So what I will do? I will first create my customer's table.

23:43

We've seen last time.

23:44

So this is the query for create table.

23:47

This is the way how you create a table.

23:49

And second, we will insert, we will go and insert some values into the customer table.

23:53

Okay, same way, I will create a table called orders and I will insert some values into the

23:58

orders table.

23:59

Okay, this is how I have managed to go and do the create and insert table statements.

24:06

Okay.

24:08

Let me just go and show you what my tables look like.

24:10

I will refresh and you can take a look at it.

24:12

This is my customer's table.

24:14

I can show you this is what it contains and this is my orders table.

24:17

If you want to see what are the contents of the tables,

24:20

now look at a very basic level, just at a very basic level.

24:22

These are what the contents of my table are.

24:24

So customer ID in customer ID, customer ID, customer name, city.

24:28

And order table, we have our past order information.

24:30

Order ID, customer ID, order amount, delivery date.

24:34

So first what I want to discuss with all of you, just to connect the dots with respect to the last session.

24:40

Because connect there, right?

24:41

See, all the modules are connected.

24:43

Whenever we are doing any future session, and I don't have to repeat it, I'm sure you've been doing this in the previous classes also,

24:51

there is always a connect with the previous class.

24:54

It's not a new topic and, so that is not how we will be going about it.

24:59

There is always a connect.

25:00

Use go, please explain.

25:02

Ah, use is, okay, okay, okay, Harsh, use in what do you?

25:06

Use, what is, you are trying to use that particular database.

25:10

That's a thing.

25:11

Okay, just one small thing I want to clarify.

25:14

One small thing I want to clarify.

25:15

If you're this one compiler in order, then you want to use kind of, okay?

25:20

Just wanted to let you know.

25:21

I'm trying to show you like how the thing actually happens.

25:26

But if you go one compiler, I think I should remove it,

25:31

or so you guys might get confused.

25:34

Actually, good that you, good that you called it out.

25:37

So let's see if I can open it up in a text editor.

25:40

Actually, open it going to just one second.

25:42

So let me share this file with you, just one second.

25:47

And I wanted to just mention this because if you try to run this in your

25:50

the online IDE, this can't.

25:54

Let me just go and delete this part.

25:57

We'll back from share it.

25:58

Don't worry.

26:00

Okay, so, yeah.

26:03

All that question.

26:04

And, okay, it's okay, no problem there.

26:07

And don't worry, this is only for sharing with you guys.

26:09

This is nothing to do with my demos.

26:11

But just so that people can run it in the one compiler IDE,

26:16

there database creation error data data.

26:19

That you don't know.

26:20

So just use my correct.

26:20

updated file.

26:22

So people who are doing it along with me, you can use the updated file.

26:26

First, for you just to explain this once again to you, what we are trying to do, we are trying

26:31

to effectively create this database, okay, and use this.

26:37

Use, I mean, we're activate it.

26:40

So this is our database, we're just to activate it.

26:43

I mean, I mean, I can run select statement on this particular database.

26:49

So now you can go and say select start.

26:50

from, select start from, uh, or up table called table can't just type

26:56

cust.

26:57

Now,

26:57

this is the way how it will work out.

26:59

You can do select start from cust.

27:01

This is the,

27:02

this is the general idea.

27:03

You can you got it right.

27:04

Uh,

27:04

you know?

27:05

Now,

27:05

look,

27:05

if I go and say, use,

27:08

do so just one more thing.

27:10

SQL is case insensitive.

27:13

And this is a very important thing.

27:14

I wanted to clarify, uh, you know, because, you know, you guys are coming from the

27:18

world of Python.

27:19

So you should know that SQL is.

27:20

case insensitive.

27:21

Okay?

27:22

Here, case matter not.

27:23

Case does not matter.

27:26

Sometimes, we, look, use, we're in capital,

27:28

use, we're in small,

27:29

so it does not matter.

27:31

Okay?

27:32

So the case does not matter.

27:33

You can write this in capital, write this in small.

27:35

Customers, you can write in capital,

27:36

writing small.

27:37

They are all read in the same way.

27:39

Just keep this at the back of your mind.

27:41

If I say, use new schema,

27:43

it means I'm using the new schema database.

27:46

Now, look, we're just this

27:47

we're doing this,

27:48

we're here activated.

27:49

This is our other one schema.

27:50

which we're in the end in this.

27:52

You don't have to worry about this right now,

27:54

but this is the way how we can do it.

27:56

Okay?

27:57

I hope everybody's clear.

27:59

Okay, let's.

28:00

This was your question.

28:01

Again, Hirsch, you can change it to everyone.

28:04

So, moving on, tables have been.

28:09

Everyone has seen the table's customer table,

28:11

and just to quickly go and run a very basic query here.

28:16

We were able to discuss a select statement last session.

28:19

Okay.

28:20

and so we can run a simple select query from the orders table.

28:27

We have our orders table right.

28:29

So on the orders table, I can run a simple select query.

28:32

So what could be a simple select query I can write?

28:35

I can say select, select star from, select star from orders.

28:41

Select star from orders.

28:43

Just say you start typing, the table name will automatically get filled up.

28:46

This is called auto-complete.

28:48

Select star from orders and always enter.

28:49

orders and always end with semicolon.

28:51

So first, this is again related to that question.

28:54

You were asked.

28:55

First, from from from which table?

28:57

So select star from orders.

28:58

First, from which table are we talking about?

29:00

We are talking about the orders table.

29:02

So orders table related we're talking about.

29:04

So select star from orders.

29:06

We are selecting all the columns.

29:09

And then what we're doing?

29:11

We're where condition lay here.

29:13

Table orders were.

29:14

First, we'll select the table select

29:16

then we filter.

29:18

Then we filter.

29:19

and what is the filter condition I want to do?

29:22

Let's say I want to get all the rows where the order amount is, let's say greater than 8,000.

29:29

Okay.

29:30

Where order amount, where order amount, order amount, order amount, order amount.

29:37

Okay?

29:39

So select start from orders where the order amount, this is greater than 8,000.

29:45

This is just another another thing that I'm doing.

29:48

that I'm doing. So what is the meaning of this query?

29:51

This query is the query?

29:52

This is the query basically refers to, sorry, I think my mistake is empty.

29:59

It should be order underscore amount.

30:03

So the query, just a second place.

30:18

So I'm here here.

30:28

So that you can see the table also parallelly side by side.

30:32

Okay?

30:33

So all if you can see, select start from dot orders table.

30:37

This is your table name here.

30:39

Where order amount is greater than 8,000.

30:41

This is the way to look at it.

30:43

So where order amount is greater than 8,000.

30:45

And order underscore amount is basically the column.

30:47

the column. You can, you can filter on the basis of the column name. You can select on the basis of the column name.

30:53

Okay, so this is the final table I end up getting.

30:56

So order of execution, what first we're, where,

30:59

the first we're from use here.

31:01

We are studying what table we want to access.

31:03

Then we've filtered.

31:04

Only extract those rows.

31:06

Only give me those rows.

31:08

And then what we do?

31:10

Then we,

31:11

uh,

31:12

then we, uh,

31:13

then we're,

31:15

column.

31:16

And column here you go here.

31:17

Let's say you want to select, let's say, for example, order underscore ID,

31:23

order underscore ID, and comma, order underscore amount.

31:28

So this is the way you look at it.

31:30

So first from, then where, then select.

31:32

This is the basic order of execution of a select query.

31:34

Just keep this at the back of your mind, all of you.

31:36

So based on what are the things we have discussed,

31:38

so this is the general order of execution as we talk about.

31:42

So from, where, then, then select it,

31:44

then then select it.

31:45

Okay?

31:46

Okay?

31:47

So just to clarify,

31:49

order what?

31:50

From?

31:51

From?

31:52

From?

31:53

Then where from?

31:54

From, say we have a table selected,

31:56

that's what is used for filtering?

31:58

From that table,

32:01

what are the rows I require?

32:03

What are the next thing we do?

32:05

Then we go back and do select.

32:07

Okay?

32:08

Then we'll see what else we do.

32:10

Select me if you see, very interesting,

32:12

we are saying select these columns.

32:13

select these columns select how select what do you mean how select object

32:20

I'll select say you are able to choose

32:23

select maybe we are giving column name of select with

32:28

we are talking about columns we want to select order ID and order amount from that

32:33

table our orders table in order stable I want to select those two

32:37

columns up start be car sark you start we could get me all the columns okay make sense

32:42

star basically means get me all the columns that's the way to look at it star means get me

32:49

all the columns huh star

32:52

means get me all the columns because just say we've started here star select in

32:55

column selection so easy way to remember is that in where we do a row selection we're

33:01

selecting which rows we're filtering it and select may

33:05

we're column selection for if I do star I'm taking all the columns and if I specify the column

33:10

names that means I'm saying hey I only want those

33:12

I want only those comments okay I hope that is clear

33:17

okay okay so select strong go where

33:22

go select it's select what I do I know next what I do I know next

33:26

okay after now this disorder by now this disorder may have

33:30

here you order need you this whole thing order man in order

33:32

so when we're data to look at it is always better to see the order in

33:37

descending order okay order amount I want to see which are my orders which are the

33:40

highest value

33:42

Mano, yeah, Amazon's order ID say.

33:44

Whenever somebody places an order with Amazon,

33:46

that's the order ID generate

33:47

so that's the use case.

33:50

Management wants to see what are the top 10 orders.

33:53

Let's say they are doing a lottery and, you know,

33:55

just say people who are spent the most and people who ordered the most,

33:58

they get some draped.

34:00

So what I will do?

34:02

From, where it's selected

34:04

a result set been made, a table return

34:07

now I want to go back into order by,

34:10

order by order amount.

34:12

D.E.S.C.

34:15

Okay?

34:16

Easy.

34:17

Syntax, I'm in all right,

34:18

you know, all the word by DESC, straightforward.

34:21

This is your descending order

34:21

is soughted.

34:23

So select after

34:24

order by.

34:26

Order by is

34:27

only sorting

34:27

is.

34:28

First, you

34:29

you're result set return

34:30

from where select

34:31

result set return

34:32

got.

34:33

Then after you

34:34

after you've got

34:34

sort

34:34

done, but

34:37

management

34:37

to put the

34:38

is that all the

34:39

orders, right?

34:40

I don't want to see

34:40

see everything.

34:41

Now,

34:42

final what?

34:42

I want to limit by three.

34:44

I only want to see the top 10.

34:46

So this is the takeaway from the last session.

34:49

This is the whole last session

34:49

takeover here.

34:50

So limit of 10 we can do

34:52

so we can see the top 10.

34:53

And finally,

34:54

after order by,

34:55

we will go back and do a limit.

34:57

Okay, everybody's with me.

34:59

Guys, please, let me know with a small yes on chat.

35:02

If all of you are clear,

35:03

order of execution of a typical select query.

35:06

We'll just more bichita

35:07

add right now.

35:08

So this is the thing that we have talked about.

35:11

Basic, order of execution.

35:12

Simple use cases.

35:13

I'm, as I did the code, I tried to explain it.

35:17

How are we?

35:18

How do you think?

35:19

It's not that you remember

35:21

that you have,

35:22

you have to remember

35:23

you.

35:24

You don't memorize me.

35:25

What we do

35:26

sometimes?

35:27

We have been taught

35:29

school and college days,

35:30

unfortunately,

35:31

including me.

35:32

I've been taught the same way.

35:33

But you should not memorize it.

35:35

It's not that syntax

35:36

you have to remember,

35:37

no.

35:38

But you should understand it conceptually.

35:39

What we are doing.

35:40

So, first from,

35:41

from this table, then

35:43

then wear, filter,

35:45

then select,

35:46

what columns you need,

35:47

then order by,

35:48

sort,

35:49

and then limit for.

35:50

I only want to sit at top ten.

35:52

That's it.

35:53

This is the five-minute summary of last session.

35:55

Let's move on.

35:57

Everybody is with me.

35:59

I only have four responses.

36:02

What about the rest of you?

36:03

All of you are okay?

36:04

Let me know, guys, if you're all clear.

36:06

All good.

36:09

Any doubt?

36:10

Anybody wants me to go over at once.

36:11

once again, all clear.

36:13

Clear?

36:14

Okay.

36:15

Keep responding, guys.

36:18

Because only when you respond, I will get to know that you are following.

36:22

Which will be some doubt, so, so keep asking me, okay?

36:25

Keep asking me.

36:27

Let's move on.

36:29

Okay?

36:31

Okay.

36:41

Let's move on, guys. Let's come back to our,

36:48

come back to our demo here, over on.

36:52

So select.

36:53

So here we're aggregations,

36:55

the main agenda today will be to learn aggregations.

36:57

What are the different types of aggregations we have?

37:00

So as the practice, we will go to the slides and we will see some parts from there also.

37:04

So these are the different aggregate functions.

37:07

So count, average,

37:09

Min is, max, it's, sum.

37:11

This is not anything is not.

37:13

Everyone can understand what these things mean.

37:15

So count is used for counting the number of rows.

37:17

Average is used to calculate the mean.

37:19

You have a column, like order amount.

37:21

You have it. You have an average to average.

37:23

Min is used to extract the minimum value.

37:26

What's minimum order amount?

37:27

Max is used to extract the maximum value.

37:29

What's maximum amount?

37:31

And sum is what will be?

37:33

All the values add over.

37:34

Now, sum of order amount.

37:35

You'll see that across all the invoices that were

37:38

that were across all the orders that were placed, the total order about

37:42

this is.

37:43

This is all aggregations are.

37:44

This is not there.

37:45

Now we're problems if we get clear.

37:47

This is the basic theory of what the aggregations are.

37:50

I'm sure you might have seen some of these things in your Pandas.

37:52

We'll be connected you can.

37:54

We will see that as we go now.

37:56

Okay?

37:57

Now, moving on.

38:00

Just one thing I wanted to clarify to all of you.

38:05

I think this diagram will help you

38:07

you beautifully understand what we are trying to do in aggregation.

38:12

If you want to understand at a very high level.

38:14

So what we are trying to do,

38:16

we are collapsing rows into summary values.

38:20

So aggregation is what you have?

38:23

If you have 1,000 rows of data,

38:27

when you aggregate you,

38:29

all is in my session folder,

38:32

just to let you know.

38:33

My materials are all with you already in folder

38:35

you have 1,000 rows of data.

38:38

You are basically aggregating that into one single value.

38:43

Who have aggregation is okay?

38:45

That's why we say we are collapsing the rows into summary values.

38:49

That's the intuition.

38:51

So let us see the example here.

38:53

So we already discussed the orders concept.

39:04

see an example of this thing count start how it is happening. Let us see that.

39:11

Just a second time. Just a second. Orders here. Okay.

39:19

Okay.

39:21

Okay. The order table. All of you are able to see this one right now. And the whole

39:29

idea is we want to find out. We want to find out what are the total number of records in the table.

39:34

what are the overall number of records in the table?

39:37

So this, so right now, whatever table we have right now,

39:41

we want to find out what are the total number of records in the table.

39:45

Okay, so let's go and execute the query.

39:48

Here in case you wondered, there was 0,

39:51

because there was a small mistake.

39:53

We've made database to select me select the right database.

39:56

And I will run this query once again, and this is how it looks like.

39:59

Okay?

40:00

There are total 45 records in the orders table.

40:03

Okay.

40:04

Normally, you can select star from orders.

40:07

This is absolutely clear.

40:09

We already talked about it.

40:11

You can, we already talked about it.

40:13

You can see.

40:14

There are total how many rows?

40:15

There are many rows in the table.

40:18

Select start from orders.

40:20

Now we are going to count.

40:21

Now we have to aggregate.

40:23

I don't want to see all the columns.

40:26

I don't want to see all the columns.

40:28

There are orders table.

40:29

Get me the records from the orders table.

40:33

All records.

40:34

and then,

40:35

that's it.

40:37

This is all I'm saying.

40:39

Now, if this looks complex,

40:42

you can this can't as you can't

40:43

select count star from orders.

40:45

You can this is the way to look at it.

40:48

So, the reason why we say as of total underscore orders,

40:53

this is what is the alias.

40:55

This is to rename the column alias.

40:57

It's to rename the column.

41:00

If you select count star from orders

41:02

what will happen?

41:03

Column count start.

41:04

Okay?

41:05

So what are?

41:06

Aggregation?

41:07

You have a lot of rows.

41:08

You have those rows.

41:09

You have that one row in one aggregate value.

41:11

This is the meaning of aggregation.

41:13

This is the meaning of aggregation.

41:15

So count star is a way to count the number of rows from a table.

41:18

Very common, very common use case.

41:20

So these are the three queries that you have.

41:22

All if you can see.

41:24

Next, we can see.

41:25

The other functions we can see.

41:27

So that's the order stable.

41:29

You can individually be able.

41:31

You can also,

41:32

you can do.

41:33

Okay.

41:34

This is a simple query.

41:35

You can see what we can.

41:36

What we can do select start.

41:41

The whole order stable has everything.

41:44

I don't want all the rows.

41:47

I might have thousands of rows in the order table.

41:49

I don't want everything.

41:51

All that I want is,

41:52

we sum of order amount,

41:54

which I want to rename as total revenue.

41:57

This is,

41:59

we have average of order amount

42:01

It's been.

42:02

We need a max of order amount.

42:03

We need.

42:04

and we have a min of order amount

42:06

and we need.

42:07

And you can validate it.

42:09

Look, here we have orders of what we did.

42:11

Order amount of maximum value 42,000

42:13

and the order amount of minimum value

42:16

actually has 10 here.

42:18

So 300 G.

42:20

So this is the way how we think of aggregate function.

42:22

Whenever we aggregation

42:23

we are shrinking the number of rows.

42:26

Always.

42:27

If we have 100 rows,

42:28

we have it, we can convert them.

42:30

That's the general idea.

42:31

Not always, it can be more than one row also.

42:33

more than one row also, but that's the broad idea.

42:35

Okay, here all of you are with me.

42:38

Simple.

42:39

Now we have an exercise just to, you know, get you practice.

42:42

So this is the pattern we'll follow.

42:44

We'll, okay?

42:45

We'll see.

42:46

You can all do along with me.

42:47

So that you can all do along with me.

42:49

Simple, right?

42:51

All of you are with me, guys, basic aggregation is okay.

42:54

Now, all of you, please do exercise 1.1.

42:57

Find the total number of orders

43:01

and maximum order amount in the order to be.

43:03

It is simple.

43:05

Reputation, but I'm just trying to see if you can get me the data in exactly the format that I require.

43:11

All of you do this.

43:13

Go to one compiler, set up your environment.

43:16

You set up for you.

43:17

That you'll, you'll do that.

43:20

Take my script, table.

43:22

Same way, if you want me to help you,

43:24

we'll do you.

43:25

We'll do it together with you.

43:28

Because most of you might have the one compiler.

43:30

So just select the entire data until here.

43:32

until here.

43:33

This create and insert to do this one.

43:39

I showed you this last time.

43:41

So you just start from here.

43:43

Drop table orders.

43:44

First you have the table create

43:46

insert into customer.

43:48

Then create orders table, insert into orders.

43:51

That's it.

43:52

This is all that you need to do.

43:53

Okay.

43:54

And after you do that, you just click on run.

43:55

That's it.

43:56

You are going and creating these two tables.

43:58

Done.

43:59

Until here, all of you do.

44:00

And then you can go and then you can go and

44:01

you can go and run the respective queries.

44:03

So you, you, this one query run and see

44:05

the first one.

44:07

Just to help you with the setup,

44:10

you can run this query,

44:12

and you can see what is the result you're getting.

44:15

Just to get some more space here.

44:17

And if I run the code,

44:19

if I run the code now,

44:21

we'll be able to see this is what I'm getting.

44:23

Exactly the output that I was getting,

44:25

you are also able to see the same output.

44:27

So you have here from here from us,

44:28

all of you.

44:29

I hope the setup is ready.

44:30

Any challenge with the setup is ready.

44:31

the setup, please let me know.

44:32

Okay?

44:33

Setup ready is.

44:34

Same as last session.

44:35

Okay?

44:36

Now you have this one.

44:37

There's a handout PDF.

44:39

We've shared not.

44:40

We've shared after.

44:41

But I want everybody to do along with me.

44:45

Follow our with us.

44:46

So that by the end of these two hours,

44:48

I will do demos and you will do demos along with me.

44:51

That is the objective, okay?

44:54

So people who are able to complete,

44:57

just let me give you two, three minutes of time.

45:00

If you're setting this time,

45:01

just being up in the online editor, please write this out.

45:04

And let me just ping the exercise also.

45:07

These are the two things that we are doing, 1.1 or 1.2.

45:14

It's simple, just to get comfortable with the select query, we are trying to do this, take.

45:29

I will wait for a few minutes for all.

45:31

Thank you.

46:01

you can find guys this should not take much time so i'll be a little fast here so what about the first one first one

46:19

first one kya o go select find total number of orders anybody wants to ping me the query

46:25

ping me the query whatever query you ping you ping you ping first person who brings the query i will run that

46:31

Come on, guys.

46:38

Please share with me what query I should run for exercise 1.1.

47:01

anybody. You guys are already already above. You just already above. You just have to tweak this.

47:31

Okay, you have just column select. That's it. Aggregations are already explained here. And the hint is you already given here. How you need to print out the values? We already did this. And now you just have to select only those corresponding records. It's a straightforward one.

47:51

Okay, very good, very good, Sneha. So here, just alias missing.

47:55

Baki, but very good. Only alias is missing. And table name orders. Okay.

48:01

Yeah, but great, great. Very nice.

48:31

Okay, excellent, excellent.

48:36

Account start. And very nice way to format it also.

48:40

I quite like around the way you formatted the query.

48:45

That is very nice the way you did that.

48:47

And that is actually done for readability.

48:48

Now, look, they've got in lines breaked.

48:51

And that is also a very good practice.

48:53

When we complex SQL queries,

48:55

these spaces matter not just to let you know.

48:58

You just to let you know,

48:59

you here here, there's just matter not.

49:00

So, it doesn't matter.

49:01

Okay?

49:02

Yeah, this syntax error.

49:03

But the white spaces are ignored.

49:05

Like, Python in this error, right?

49:07

But SQL is very liberal.

49:08

You can give any number of wide spaces, any number of tabs, no problem.

49:13

Okay?

49:14

For readability purpose, you can do all that stuff, okay?

49:17

So see how I've organized my query.

49:19

So same way you need to do it.

49:21

Okay, yeah.

49:23

Excellent.

49:24

So let me run the code here, all of you.

49:29

So select counts are as total audits, comma, maximum order amount as max amount from audits.

49:35

That's the way to look at the query.

49:37

And this thing important is, because people get confused, you know.

49:41

Some books in some books are written,

49:43

but please keep in mind that these spaces are ignored.

49:48

So you'll like, sir, here here space diar, should I give a space?

49:52

Again, remember, SQL is very liberal.

49:55

Case matter not.

49:58

Spaces matter.

49:59

If you give us enter, space, tab, that ignore.

50:03

Okay?

50:04

Very liberal.

50:05

Okay?

50:06

So just keep this at the back of your mind.

50:07

For readability, just to understand the things properly,

50:10

we'll use.

50:12

So this is the way how your query will look like.

50:14

Count star and max of order amount.

50:17

Exercise number 1.2.

50:19

How do we do it?

50:21

Same thing is.

50:24

I'm not waiting on this.

50:26

Same thing is.

50:28

So.

50:29

You are trying to select all the records from the orders table.

50:32

First, we have average calculated.

50:34

And as is the column name alias that we're providing.

50:39

All of you are with me?

50:41

Everybody?

50:43

Simple. Until now, all good.

50:46

Now.

50:48

Guys, before I come to the next phase of my conversation,

50:51

I wanted to ask you this question.

50:53

You have pundas have seen group by?

50:56

Group by, you have seen group by?

50:57

You have seen Group by?

50:58

You have seen.

50:59

Group Bai, you've seen in Pantas in just wanted to understand from you.

51:03

You have seen something called Group Bai and Pandas.

51:06

Right?

51:07

Group BIDF.

51:08

It's a common query. Right?

51:10

Chalo, it's really.

51:11

Related.

51:12

Everything related.

51:13

Okay?

51:14

Excellent. Excellent.

51:16

Excellent.

51:17

Let's now understand the idea behind group by.

51:20

Let's.

51:22

Let's just a second one, sir.

51:29

Okay.

51:36

So now moving on.

51:57

Just one

51:58

Just one thing I want to clarify.

51:59

keep this at the back of your mind.

52:01

Giam made code may use not.

52:03

But whenever you do count start,

52:05

it is used to calculate the absolute number of rows.

52:09

When you have count start

52:10

it is typically used to calculate the total number of rows,

52:13

which we have now in code in

52:15

but please remember there is also something called

52:18

count of the column name you can give.

52:21

So if you get count of column name,

52:24

it will give you the total number of rows which are not null.

52:27

Just remember this.

52:28

Just remember this.

52:29

not be a big thing going forward, but just remember that when you do count of a column name,

52:34

it will only count those rows which are not null.

52:38

So here, there's not that

52:39

for a difference if you look at the order table,

52:42

if you just look at my complete order table,

52:45

so we have data is simple,

52:47

we've got no null values,

52:48

all the values are valid.

52:51

So here here here,

52:52

if you go and say,

52:55

select count star,

52:57

and if you

52:58

and if you try to say count of,

53:03

I'm column name let's count of order amount,

53:08

order underscore amount, if you do this, it will not

53:12

if you do this, it will not make a difference.

53:15

Okay, you know,

53:16

so this will give you the same record.

53:18

Okay, so this will give you the same record.

53:21

But if my order amount consisted of nulls,

53:25

count star will take the absolute row.

53:27

Count star, you know, what,

53:28

count star does, count star,

53:29

up your serial number basis,

53:31

that it's 45 rows are.

53:33

But when you say count of the column name,

53:36

when you say count of the column name,

53:39

what will happen?

53:40

It will count only the non-n null value.

53:43

So that is the way how the concept broadly works out.

53:47

That's the basic idea, okay?

53:49

Okay.

53:50

Okay, very nice.

53:51

So count one is also going to count all the rows,

53:55

basically.

53:56

So, it's not common syntax.

53:57

So, there are many variations in text.

53:59

But yeah, if you count one be

54:01

basically counts all the rows.

54:02

Think of that.

54:03

It's a non-null constant.

54:04

It's a different way of writing the query.

54:06

But usually it is not a common practice.

54:08

Some counts start use.

54:09

But count one will also do the same thing.

54:12

Okay.

54:13

Now, moving on.

54:16

Let us see the idea behind group by.

54:19

What we are trying to do in group by, okay?

54:22

So what is the objective right now?

54:25

We have multiple customer IDs.

54:26

Multiple customer IDs.

54:27

Okay.

54:28

We have multiple customer IDs.

54:30

We want to group by customer ID and we want to find out every customer ID

54:35

how total order amount in.

54:38

See what?

54:39

Look what?

54:40

Multiple customers place order.

54:41

If you look at the order table, if you look at the main orders table,

54:45

there are multiple customers who are placing orders, right?

54:49

Multiple customers are placing orders.

54:53

This order ID is different customers

54:55

different customers have.

54:56

So if you look at the customer ID 1 is,

54:59

imagine this was a purchase the customer did today

55:03

and this was the purchase the customer did tomorrow, yesterday.

55:07

So this is the same customer.

55:09

They both are all the different swiggy

55:11

in Amazon and purchased.

55:12

But the same customer has ordered two times.

55:15

This is your customer ID 4.

55:18

They have 1.106 order ID phased

55:20

to,

55:21

I mean,

55:23

same customer has 1,11

55:25

$1,500,000.

55:27

And the same customer for is probably ordering something else again, $138, $1,200.

55:33

Now this is spread out, right?

55:37

Management, what they want to do, what is the real world use case of this?

55:41

If you're Amazon, these e-commerce sites in, imagine Swigy,

55:44

this is very real use case.

55:46

You know, in Swigy in, they have something called a Swigy Black program.

55:50

Now, Swigy One's subscription free in

55:52

free.

55:53

You can take a Swigy one subscription into.

55:54

You can take a Swigy one subscription into.

55:55

very low cost.

55:56

But, the Swigy one black subscription is,

55:59

one black is invite only.

56:01

And you know how if you

56:03

if you try to search that Swigy one black,

56:07

you will not see.

56:08

Unless Swigy enables the invite for you,

56:11

or somebody else invites you, you will not see one black.

56:14

You will not see one black.

56:16

Customer support cannot do anything.

56:18

So back in what they try to do,

56:20

they are trying to find out each and every customer.

56:23

They are trying to find out every customer.

56:24

They are trying to find out every.

56:25

customer, what is the total order value that they are placed?

56:28

This is group by use case.

56:30

We'll see.

56:31

We all individual orders of data, we'll

56:33

we'll find out

56:35

what is the overall order amount.

56:38

So that is the use case of group by.

56:40

That is exactly what we are trying to do.

56:42

So that's the use case.

56:44

That is exactly what we are trying to do here.

56:46

And that is the concept behind this particular query.

56:48

The next query on group by, which we are able to see on the screen right now.

56:53

The idea is very simple.

56:54

The idea is very simple.

56:55

Very simple. We are breaking summaries down by category.

56:59

This is your group by customer ID.

57:01

It is from.

57:03

And what are we selecting?

57:05

Now what do we want to print?

57:07

We want to print out those customer IDs and also the sum of the order amounts.

57:11

This is your group by answer.

57:13

Okay.

57:14

Now you have the customer ID, the 4 is multiple rows.

57:16

Remember?

57:17

So now we have group by customer ID.

57:20

Now 4's one row can be one row

57:22

when you do group by, we will have only one row for that.

57:25

4. Because customer 4, now we are

57:27

total. This is your

57:29

this.

57:31

Everybody can relate to it.

57:33

Everybody can relate to it.

57:34

So you group by the customer ID and you're finding out,

57:37

okay, what is the total order amount for each and every customer ID?

57:40

And this is your alias. This is the way how you

57:43

show the data, render the data.

57:45

And now you can do you can do

57:48

you know, all the stuff that we discussed.

57:50

Now order by, limit koro, all that will follow.

57:53

So just to

57:54

just to

57:55

continue on with the order of execution.

57:57

What are the learnings until now?

57:59

First, prom.

58:00

Pronged.

58:01

Pronged.

58:02

Then, then group by.

58:03

Grouping, then, then then select.

58:05

Select is the last thing that we do.

58:07

Okay?

58:12

Very similar to your Pandas Group by.

58:14

I hope everybody is alive.

58:15

So Pandas Group by be the way going.

58:17

No difference, I think.

58:18

Okay.

58:19

All of you are able to relate to it,

58:20

relate to the Pandas,

58:21

corresponding Pandas group by function also.

58:24

Same way.

58:25

can do the Pandas Group by function as well.

58:27

How do we do the same thing in Pandas?

58:29

How do we do the same thing in Pandas?

58:32

So df. df.group by order amount of some.

58:36

So this is the corresponding query, how it looks like in Pandas.

58:40

Just to clarify.

58:42

Imagine you have a customer table.

58:43

If you have pandas in group buy

58:45

so this is the way how we will look at it.

58:48

Let us quickly complete these two.

58:51

Here here, there a little bit more

58:52

a little bit of them directly not kicked you.

58:54

I have not exactly they're going to be a copy paste.

58:57

Please complete 2.1 and 2.2, all of you.

58:59

Same way, you will have to apply a group by function.

59:06

What is the use case again?

59:08

You want to group by each and every customer ID

59:11

and you want to find out kitha orders overall place here.

59:14

That's it.

59:15

This is what you want to do.

59:16

How many total number of orders they have placed?

59:19

Okay, 2.1, 2.2, all of you.

59:24

Everybody has a setup ready already. Please try it out.

59:30

This, we'll, we'll another very interesting thing

59:32

which is having.

59:33

Having Plosome, we'll see.

59:35

I will wait for two minutes.

59:40

Everybody should do it, okay?

59:42

Everybody.

59:54

Thank you.

1:0:24

Done, guys, whatever the first one, 2.1.

1:0:44

Okay, Sneha has pinged.

1:0:47

Okay, Sneha always try to print the customer ID also.

1:0:53

Select.

1:0:54

Okay, just to let you know.

1:0:56

Because if you only show order amount or max of order amount,

1:0:59

then the result you'll not know

1:1:01

just to explain to you what I'm discussing.

1:1:05

Just to just for me to clarify what I'm explaining.

1:1:11

If you here here, if you're here

1:1:14

here if you are, see,

1:1:16

this is your,

1:1:19

queries valid,

1:1:22

just to clarify,

1:1:23

I'm terrified.

1:1:24

It's very interesting.

1:1:25

Quarry is valid, but you can't

1:1:26

know,

1:1:27

that you can't

1:1:29

just to let you know.

1:1:30

You're still grouping by each and every customer,

1:1:33

and you're calculating the sum for each and every customer,

1:1:36

but remember, select statement will show is a column selection.

1:1:40

So you are only selecting this column.

1:1:43

But no, you want to show the customer ID column also.

1:1:46

So always as a best practice, when you group buy

1:1:48

you, you'll always, you'll always

1:1:51

just keep this at the back of your value.

1:1:52

Just keep this at the back of your value.

1:1:53

Okay, let's.

1:1:54

Okay, you.

1:1:55

Quarry revise for him.

1:1:56

Others, let me hear from somebody else.

1:1:59

Others, let me hear from somebody else.

1:2:29

Yeah, very nice.

1:2:38

Customer ID or count of customer ID.

1:2:40

You can start be here.

1:2:41

If you here on the same answer, right?

1:2:44

Yeah, yeah, very good.

1:2:46

Very good.

1:2:47

All good.

1:2:49

Everybody?

1:2:50

Others.

1:2:52

Everybody else is fine.

1:2:53

The next 2.2, I want to hear from somebody else.

1:2:56

Apart from, say, huh, and you come.

1:2:58

Somebody else.

1:2:59

So 2.1, once again, let me do this straightforward once again.

1:3:10

So group by customer ID, we want to display the customer ID and count of star.

1:3:18

For each and every customer, I want to show, that this

1:3:21

orders placed here.

1:3:23

Okay, this is very interesting because you'll

1:3:25

you can see which are the customers who have placed the most number of orders.

1:3:28

of orders.

1:3:29

Okay?

1:3:30

Okay?

1:3:31

Next one.

1:3:32

Guys, a variation.

1:3:33

A variation.

1:3:34

A variation.

1:3:36

Again, going by the order of execution of a select statement.

1:3:42

First, we have ordered table selected from orders.

1:3:46

Then we have group buy.

1:3:48

For every customer ID, we calculated count how it.

1:3:52

Done, sorted, right?

1:3:54

From group by, select.

1:3:56

Done.

1:3:57

Now, you know?

1:3:58

I want to sort my data in descending order of total,

1:4:05

this ending order of total orders, total number of orders.

1:4:09

Management to look at that who are those customers who ordered the most?

1:4:14

So, group by to go go-gia,

1:4:17

but I want to now, finally, order by, what?

1:4:22

Order by what?

1:4:23

Order by what?

1:4:24

Order by this thing?

1:4:27

total orders.

1:4:29

Because this is your end in okay?

1:4:32

The order by will always happen at the end.

1:4:35

The order by will always happen at the end.

1:4:38

So we want to order by total orders D-E-S-C.

1:4:43

Okay?

1:4:44

So, let me show the query once again on a few.

1:4:47

So, we've done here here.

1:4:49

You can see what this is the final query how it looks like.

1:4:53

So order by was not expected as part of the problem statement,

1:4:56

but I just wanted to do.

1:4:57

give you a variation.

1:4:58

So this is a better way to render my data.

1:5:01

So we are slightly increasing the complexity of our queries.

1:5:04

So from, first from,

1:5:06

then from,

1:5:07

then we've groupinged.

1:5:08

For every customer, we've made count,

1:5:10

but that count in order,

1:5:11

not.

1:5:12

So we're last in what kind of

1:5:14

from,

1:5:15

group by, select here,

1:5:16

results at a table,

1:5:18

and then we are ordering by total orders DESC.

1:5:22

And this total orders is an alias.

1:5:24

This is the reason why aliases are very helpful.

1:5:26

very helpful. Order by always

1:5:28

always selects after.

1:5:29

You see,

1:5:30

select statement we have an alias here.

1:5:32

So that's the reason why when you do order by,

1:5:35

you can use the same alias here.

1:5:37

So this is your order of execution.

1:5:39

From, then group by, then select, then order by.

1:5:43

And then it's then,

1:5:44

then you'll say, sir,

1:5:46

we're not going to do,

1:5:47

so what will do?

1:5:48

So what will do?

1:5:49

I want to only see the top 10 orders.

1:5:53

That's it.

1:5:54

or the top fight is.

1:5:55

This is your hope.

1:5:57

Okay?

1:5:58

That's it.

1:5:59

This is the takeaway.

1:6:01

Okay?

1:6:02

So let me summarize the order of execution.

1:6:04

Once again, until now, whatever we have talked about.

1:6:07

From?

1:6:08

From?

1:6:09

What?

1:6:10

What?

1:6:11

Here, where clause is.

1:6:13

Weare.

1:6:14

Then we're going.

1:6:15

Then we group by.

1:6:16

Then we group by

1:6:18

then.

1:6:19

Then we select.

1:6:21

Then we'll order by

1:6:23

and then we'll limit.

1:6:25

Limit always last.

1:6:26

Limit is like head of pie in Python.

1:6:29

This is the way how you will do the things.

1:6:31

Okay?

1:6:32

Clear is all of you?

1:6:35

I hope I ping you.

1:6:37

Okay.

1:6:38

Okay.

1:6:39

Very nice. Very nice.

1:6:42

Very nice.

1:6:44

Okay.

1:6:46

Muhammad, great.

1:6:48

Thank you.

1:6:49

Count customer ID you have pinged.

1:6:50

Do you?

1:6:51

account?

1:6:52

No, okay.

1:6:53

So you have all.

1:6:54

All right.

1:6:55

Good.

1:6:56

Good.

1:6:57

Okay.

1:6:58

Yeah.

1:6:59

Minimum and maximum order amount for every customer.

1:7:00

Let us see.

1:7:15

So 2.2.

1:7:16

Let us run this.

1:7:19

And here once again, you're grouping by customer ID and you want to show what is the minimum order amount and what is the maximum order amount for each and every customer ID.

1:7:27

So that's the way to render it.

1:7:29

Simple.

1:7:30

All if you are able to understand, this is the grouping idea.

1:7:34

Yeah, very nice. Very nice.

1:7:37

Now, now,

1:7:39

we have.

1:7:41

We have one thing in the whole select clause.

1:7:44

Actually, topic-wise two things back here.

1:7:46

Number one, we will discuss having plots.

1:7:48

And number two.

1:7:49

we will discuss joints. That's it. So what is the having clause? So here

1:7:54

to sort it. We are all clear, that's up.

1:7:57

First, from, then where, then group by, then select, then order by, then limit it.

1:8:04

We'll copy it.

1:8:06

Let me bring it all the way here.

1:8:09

Okay. Sorry, where did that go?

1:8:14

Let me bring it all the way here. And here I will discuss the having clause.

1:8:18

clause. All I will do is, I'm here having done this.

1:8:23

This your revised order of execution.

1:8:26

What we are explaining here.

1:8:27

Remember, this is the way the order of execution will happen to.

1:8:31

From the table, first filter, get with a revised table, and in each and every step along the way,

1:8:38

this is for you to remember, just for you to think through it.

1:8:42

At each and every step, a resultant table be made.

1:8:46

Okay.

1:8:47

So first you have the complete table. Then you do the where. You get a, you get a filtered version of the table.

1:8:54

Then you do group by. You get a further filtered version of the table.

1:8:59

Then you have having. So group by or having say, what are you get a filtered version of your table.

1:9:05

Basically. So having is like a filter of group by.

1:9:08

And then you do select.

1:9:10

Now, that column select and then you do order by and then you do a limit.

1:9:15

Okay, that's the concept.

1:9:16

That's the concept.

1:9:17

Now, let's talk about it.

1:9:18

Let's talk about having in a bit more detail, what is happening in the having clause.

1:9:22

A easy way to remember this is that having is a very special kind of filtering that happens with group by.

1:9:29

Whenever we have group buy you will always go and do having.

1:9:34

So having is, remember, having is like a special kind of filtering that is done inside group by.

1:9:40

So that's the way to think of having.

1:9:41

Just we're where clause use the thing.

1:9:43

So similarly, having is a special kind of

1:9:46

where clause used inside group by you?

1:9:48

Who your having can.

1:9:50

So just to explain this to all of you,

1:9:55

where versus having?

1:9:57

Now look, here we have explained the whole thing right now.

1:10:02

So having will always happen after grouping.

1:10:06

This will always work with grouping and it always uses aggregate functions.

1:10:12

Because having always always uses groups

1:10:14

use.

1:10:15

When you use by you, you're having used by.

1:10:17

That's the way how the whole thing will work out.

1:10:20

Having will always happen with group by.

1:10:23

So having is a special kind of where clause.

1:10:27

This group by is a word clause.

1:10:28

You can this is just for your simplicity.

1:10:31

Wear clause, as we've seen,

1:10:33

this is the grouping before it is.

1:10:36

It is a simple filter that is working before grouping.

1:10:39

That is the order of execution is,

1:10:42

if you remember,

1:10:43

First we do from, then we do where?

1:10:45

That's it.

1:10:46

Just like the last session.

1:10:48

We have a full table.

1:10:50

There are only work on these rows.

1:10:52

You have a filter then.

1:10:54

Then you go group,

1:10:55

what you do what you do.

1:10:56

But where is happening before group by?

1:10:58

Having is a special kind of filter that happens after group by.

1:11:02

Just remember that.

1:11:03

So once you understand that,

1:11:05

the rest of the journey is very smooth.

1:11:08

So what are we doing?

1:11:10

What are we doing?

1:11:11

You have customer address group and you try to find out the total order amount.

1:11:18

And please filter only those rules where the total order amount is greater than 10,000.

1:11:25

And that is the one that you eventually want to surrender.

1:11:28

So this is your final end result.

1:11:31

Okay?

1:11:32

All if you can see.

1:11:34

Same to same here.

1:11:35

If you, maybe what I can do is, let me show you this result.

1:11:40

If you're having to execute, then this is your result will.

1:11:44

Every customer ID, you can see the total order amount.

1:11:48

So you can see that total order amount.

1:11:50

So you can see some order amounts which are actually less than 10,000.

1:11:54

Like this is 6.

1:11:57

And this is this is 8.

1:12:00

This is 10,000.

1:12:02

So we need 6 or 8 not need.

1:12:05

The other thing is group B.

1:12:07

Group B is.

1:12:09

So, uh...

1:12:10

Group buy has, some have, all that is the same.

1:12:12

Nothing changes.

1:12:14

But we only want to show, we only want to go back and show those customer IDs

1:12:20

where the total sum amount is greater than 10,000.

1:12:23

We only want to show those customer IDs that a total sum amount is more than 10,000.

1:12:28

That is what we want to go back and do.

1:12:30

That's not to go back and do.

1:12:31

So, so first first you,

1:12:33

group buy, then you have having,

1:12:36

group buy filtering,

1:12:38

only take those records.

1:12:40

This result in the table, okay?

1:12:42

This resultant table may only take those records which are more than 10,000.

1:12:46

And then you show customer ID and some of the amount.

1:12:50

Now, look here here the final result is this number 6 or number 8 will be missing.

1:12:56

You can see.

1:12:57

Customer ID 6 and customer ID 8 are missing.

1:13:01

5 is missing. 5 shah maybe, okay?

1:13:04

So 6 and 8 are actually missing.

1:13:06

You can see that in option.

1:13:08

Okay?

1:13:09

everybody is with me. So this is filtering groups after aggregation. It is a special kind of wear clause that is happening after the grouping operation is successful. Okay. I hope everybody is clear. Okay. All if you are okay. All if you are okay with me.

1:13:39

We can we will get better.

1:13:45

That's the idea.

1:13:46

And all of you take a look at this one.

1:13:50

Look at this one.

1:13:53

Look at this one all of you.

1:13:56

This is a very tricky use case.

1:14:00

We're not going to be.

1:14:02

Let's see how you are able to do it.

1:14:05

This is very tricky.

1:14:06

We have to do 3.1 and 3.2.

1:14:08

3.1 is very simple. 3.2 is very simple. 3.1 is slightly tricky.

1:14:15

Now, how it is tricky? What tricky is that I will wait for you to solve.

1:14:20

All of you try this out.

1:14:23

And after this we'll go to joints.

1:14:30

Everyone try 3.1. 3.1 is a little tricky.

1:14:33

You have to read the problem.

1:14:35

Understand.

1:14:37

Understand.

1:14:38

The difference between,

1:14:40

understand the difference between where and having.

1:14:43

What we have?

1:14:44

Remember, having always happens with group by.

1:14:47

Okay?

1:14:48

Or having will always work with aggregate functions.

1:14:52

Whereas where is a normal filter,

1:14:54

you have last week,

1:14:56

you know?

1:14:57

So you can't understand.

1:14:58

You have to understand that first.

1:15:01

You have to understand that first.

1:15:03

Yeah, so please try it.

1:15:07

Thank you.

1:15:37

Thank you.

1:16:07

Okay, so Neha asking something something.

1:16:21

Others, let me know what the right query will be.

1:16:37

Thank you.

1:17:07

Thank you.

1:17:37

okay okay great thank you mahmat

1:17:41

from order where you're using wear clause also okay

1:17:47

so having a yoga guys

1:17:50

nice

1:17:52

Neha has mom other pink others

1:17:56

no way perfect perfect

1:18:00

you see i encourage you i encourage you

1:18:03

if anybody in today's anybody in today's world is not using AI

1:18:06

not using AI, we are wasting our time.

1:18:09

We are totally wasting our time.

1:18:11

Please use AI.

1:18:12

I encourage you.

1:18:13

You can't understand

1:18:14

you.

1:18:15

You can't get in five minutes

1:18:17

something things are

1:18:18

if you're going,

1:18:19

if you're going to be

1:18:20

that's okay, it's okay,

1:18:22

absolutely fine.

1:18:23

I'm a supporter of AI.

1:18:25

Now use GPT, Gemini,

1:18:27

please, please, absolutely.

1:18:29

Brother.

1:18:33

Yeah, guys, set your chat settings to everyone

1:18:35

so that people can see.

1:18:36

like so that everyone is able to see everyone's messages.

1:18:38

So from next class, every session, all of you just set your settings to everyone.

1:18:48

I wish you have having used here.

1:18:50

I wanted to think for a minute.

1:18:51

I'll explain in a moment.

1:18:53

Yeah, I told you that having should always have aggregation.

1:18:57

Hello?

1:18:59

You know, our customer rate is a group here, right?

1:19:01

But order is not for every customer, right?

1:19:04

I thought so for a minute, should it come in where or should it come in having?

1:19:10

The other parts of what you did is correct, okay?

1:19:31

Very good, very good, excellent.

1:19:33

and amazing. I mean, where clause may go? Good to see that people are able to, you know, figure it out.

1:19:39

And as I said, use a bit of AI, I'm fine with that, but understanding concepts.

1:19:43

Okay? It's okay. Absolutely fine.

1:19:50

Okay. So where clause will? Most of you have done it. All of you, almost all of you who are

1:19:55

think we have got it right. Okay? So the, uh, the answer to the question would be, this is a three point.

1:20:03

1. So 3.1 would be where plus? Okay? So we have a step by step

1:20:09

step. We have to understand the thing step by step. So first you want to take all the records

1:20:17

from your orders table where the delivery date is greater than this, right? So if you go back to the

1:20:22

session last week, sorry, a few days back, what did we do? How did we solve the problem?

1:20:29

So subse pre'a'a'a'i we are selecting all the rows from the rows from the.

1:20:33

the, uh, from the order table where the delivery date is greater than this, okay?

1:20:41

Group I having, all right? This is absolutely clear with you. This we know. This is

1:20:46

what is. This means what is? Now, order's table select

1:20:48

and get me all those delivery, all those rows where the delivery date is greater than this.

1:20:54

That's the first and foremost criteria. Okay. Uh, what got got. Uh, what got? Date value is

1:20:58

incorrect. Okay, you know, there's a little issue. Let me just check this. Uh, let me just check this.

1:21:03

that is not correct, I guess, just a second.

1:21:05

The 20, 23, 10, 10, you need to just go and set the form of the, just give a second.

1:21:33

you know, we've got this space there. So this space

1:21:35

need to. The problem is that, just in case you guys are wondering, that, sir,

1:21:40

what went to, let me tell you, uh, yeah.

1:21:44

This is a second, let me share with you.

1:21:54

So, yeah, let me share with you. So, yeah, let me share with you. This,

1:22:03

you, you must not have spaces within the date column, okay? Whatever.

1:22:08

So date, here here spaces, no, so by mistake, here spaces are,

1:22:12

okay? You, now, look, here spaces are there. Anyways, so my, so the point is that

1:22:15

this is the normal query. This we have already discussed, right?

1:22:20

This we have already discussed. Normal query is select start from orders where the delivery

1:22:24

date is greater than something. We are trying to select all those records with the delivery date

1:22:29

is greater than this. He is normal where clause is.

1:22:31

And then that you have the refined data, now we will go and do a group buy, now we will do a group buy on customer ID.

1:22:42

We will do a group buy on customer ID.

1:22:44

And then for every customer ID, we will find some of the amount.

1:22:48

That's the idea.

1:22:49

So first from, then, then, filter, we don't want to consider any people whose deliveries happened before 10th October 2020.

1:23:01

Management is case. Management only wants to know last three years, last two years, who are my highest spenders.

1:23:08

This is case.

1:23:10

You have a problem of use case. The problem of use case is that. The problem is that management only

1:23:14

wants to know. So if I have to put a business statement here, the business statement would be,

1:23:23

we want to know, we want to know the highest spending customers.

1:23:31

In the last two years, yeah, two and a half years, whatever.

1:23:35

Abi, does October, 203, what was there, Pachis, this is two and a half years, approximately, we can say,

1:23:43

in the last two and a half years, who are my highest pending customers?

1:23:47

That is what we want to know.

1:23:48

Who are my top spending customers?

1:23:50

See, how we can frame the problem in different ways.

1:23:54

Oftentimes when questions are given to you,

1:23:56

when interviews, when you are asked questions, you're not just asked a question, you're not just asked a question

1:23:59

the print days and, yeah, we've done academically you asked, because we are discussing

1:24:04

the topics today in, you know, from the basics.

1:24:08

But sometimes when interviews are asked, interviews where they will ask you like this.

1:24:12

So based on the problem statement, you know, you'll say what they are asking you.

1:24:18

So they are asking you, that here up to you don't say, you know,

1:24:21

that delivery date, say, kind of, filter, do, no, you have to figure out.

1:24:24

Now, because asking the question like this and asking the question like this is one of the same thing.

1:24:29

Okay, everyone's someone to understand.

1:24:32

So, okay? I hope all of you are okay.

1:24:34

Some of you who wrote Arnika, I think this is for Arnika and like, and also, also, also Saurav.

1:24:43

No, sorry of, Arnika and, uh, uh, uh, Ayush.

1:24:49

I hope you guys are able to understand, okay?

1:24:51

You guys are able to understand the, uh, why we are considering the wear clause here.

1:24:56

Where is only used for individual dose, well.

1:24:58

Right.

1:24:59

And you got that absolutely right, Ayush.

1:25:01

You got that absolutely right.

1:25:02

Where is used for individual rows, whereas this only works on aggregate groups.

1:25:07

Okay, so here here you have to use where clause use can be.

1:25:10

Because the first we have to filter based on the delivery date.

1:25:13

That's after we go, we'll gop.

1:25:15

You know?

1:25:16

Make sense?

1:25:16

This is the way how we will be solving this.

1:25:21

Next one is very easy.

1:25:23

This is the simple one.

1:25:24

This is the simple one.

1:25:26

Right.

1:25:27

So this is where we have to find.

1:25:29

out group by customer ID, find average amount and having average amount greater than 5,000.

1:25:37

That will be the use case for 3.2.

1:25:39

This is exactly the same way I did sum.

1:25:41

I'm just some already explained to you.

1:25:43

Average will be exactly the same as some.

1:25:45

Same as same.

1:25:46

Same as sum.

1:25:47

And then you can order by also.

1:25:50

You know, you know, just to clarify, yeah, order by customer ID can.

1:25:55

I have been ordered by an order amount be.

1:25:57

Either way.

1:25:59

both ways you can do it.

1:26:02

This is how we will be looking at it.

1:26:07

So now, guys, we will be moving to our joint.

1:26:12

And I wish, I hope you are clear.

1:26:15

Clear, I know, where clause?

1:26:16

I hope you are okay.

1:26:18

And before I move on to joints, I wanted to ask you,

1:26:22

have you guys explored a bit of joints in Pandas?

1:26:23

You've done here.

1:26:24

I'm sure there are two tables you might have seen and you might have worked with it, right?

1:26:28

Just wanted to.

1:26:29

clarifying.

1:26:30

Pandas in you have joined the syntax

1:26:31

on, on equal to the way how we take table one, data frame one, comma, data plan two,

1:26:38

on, you might have seen some of that.

1:26:41

Let me know, please.

1:26:47

Pandas in join how do?

1:26:48

What is the syntax?

1:26:51

What is the method to join in Pandas?

1:26:55

Anybody?

1:26:56

As I mean, group by, so pandas in pandas may join in.

1:26:59

What, guys? What is the method to join in Pandas?

1:27:04

p-d-dot? Import Pandas as PD. PD. What do we do? P-D dot what?

1:27:12

You guys have seen joins, right? Guys, just for my understanding.

1:27:16

After, they've seen, right? Table one, table two, how to join in Pandas?

1:27:29

Hello, everybody, everybody's quiet first.

1:27:34

So on, guys.

1:27:36

Yeah, we'll go for a break shortly, but just to answer me, just for my understanding.

1:27:41

You know, you've seen, right?

1:27:43

Yeah, that's okay. That's okay. That's okay.

1:27:44

But merge you've seen, just wanted to check.

1:27:53

Yeah, yeah, thank you, Fiddush.

1:27:54

Fidosh, you have seen, you've seen merge, right?

1:27:56

You've seen this in the class.

1:27:57

You've seen this in the class.

1:27:59

Hello, guys.

1:28:09

Okay, that's all I wanted to know. I'll, okay. I will recap. I'll recap. Don't worry.

1:28:14

Recapping is one thing. Teaching from scratch is another thing. So once you tell me,

1:28:18

sir, we've seen a little bit, we've, we've, we're going to be right? Don't worry. It's not as if I will just

1:28:23

tell you the syntax. Ney, but knowing that you've seen it, I can draw the connect better.

1:28:27

So we'll connect and you'll say, yeah, here here there's this. It helps me explain the concept

1:28:33

in a better way. Okay? Okay? Chalo. Very good. So we will see joints now. That is the last part of the

1:28:39

thing that we have right now in the session. So joints we'll see inner join, left join, we'll see

1:28:46

different types of joints. I will recap that for you. Okay. And after that, we will do some case studies

1:28:51

just like how we discussed in the last session. Okay. So we can take a short break right now. We are

1:28:57

almost at 9, 920 on the clock. So let us take five minutes break, okay?

1:29:01

Get some water, get some rest, all of you, and let's come back after the group.

1:29:05

Okay? Okay. Let's take a short break and come back.

1:29:27

Thank you.

1:29:57

Thank you.

1:30:27

Thank you.

1:30:57

Thank you.

1:31:27

Thank you.

1:31:57

Thank you.

1:32:27

Thank you.

1:32:57

Thank you.

1:33:27

Thank you.

1:33:57

Thank you.

1:34:27

Thank you.

1:34:57

Thank you.

1:35:27

Thank you.

1:35:57

Thank you

1:36:27

Thank you.

1:36:57

Thank you

1:37:27

Thank you

1:37:57

Hi,

1:38:04

Hi, folks, welcome back.

1:38:34

So let's move on. So now we'll be continuing on with

1:38:38

with our joints and we'll explore the different different types of joints and we'll explore the different types of joints and the final part we will do

1:38:44

we will do some case studies where um, uh, which case studies are going and on the basis

1:38:50

exercises will be also solving together.

1:38:52

That's the agenda for the next for the next one hour.

1:38:56

So so first I want to explain the general I want to explain the general concept

1:39:04

of why a database, okay?

1:39:09

You know, you know, when I talked about this a little theoretically.

1:39:13

We have last to last day when we did about first class, I had that time explained to you the origin

1:39:20

of databases, why databases were invented, what was the history, what was the background, how people

1:39:26

used to store data in flat files before, and what were the challenges. So database system,

1:39:34

what happens is we are able to store the whole thing in multiple tables and multiple

1:39:43

connected tables. All these tables are by themselves connected. I mean, of course, a schema diagram

1:39:48

where there are like seven, eight different tables, each of them are connected. So that is the real

1:39:53

world scenario.

1:39:56

Our abe's use case is it's a lot simpler. So we have two tables right now. So you can see, we have two tables right now.

1:40:00

So you have a, so we have a, just a second, guys. So we have a simple customer table and we have a simple

1:40:12

orders table. So orders table may our schema looks somewhat like this and customer table

1:40:20

in our schema looks somewhat like this. Right. So customer table, imagine this is again

1:40:27

Amazon kind of a use case. So Amazon has

1:40:30

every customer's details will, right? Whenever you do a K-Y-C, whenever you register on Amazon,

1:40:35

you account created, you whatever you did, so this data will be in your account in your account. So every

1:40:40

row is a customer. We will know what is the customer ID. We will know what is the customer name.

1:40:45

We will know the city. Which city the customer belongs to? That's all the information

1:40:48

you have to are all right. So I repeat again, we will know the customer ID. We will know the

1:40:53

the customer name. We will know the city. Which city the customer is from.

1:40:57

All right. All right.

1:41:00

So that is the number one thing.

1:41:02

Number two, we have the order stable.

1:41:06

Order stable in the order stable in the order stable we will have information about the orders that were placed.

1:41:14

Which order was placed? Who is the customer who placed the order?

1:41:18

What was the value of order?

1:41:19

They've got what was the value of order? And finally, we are talking about the delivery date.

1:41:25

What is the delivery date that we are talking about when the order was delivered?

1:41:30

So if you think through these two tables, what is the common column between these

1:41:36

two tables? We have customer table and we have orders table. If you think about it, the common

1:41:41

column is customer ID. Correct. People were saying Pandas'a syntax, you pinged here on equal to.

1:41:49

When you're on equal to, he will do on equal to customer ID.

1:41:52

Okay? Okay. Second thing. This is from a theory perspective, this is from a theory perspective. It's

1:41:58

the other relevance not going to be but just from a theory perspective, remember,

1:42:03

you know, our customer table is, okay? Let me explain this in a better way for you.

1:42:09

So this is a bit of a bit of a mistake here. So let me just write it down in a bit, you know,

1:42:14

a better way for all of you. Okay. So you just write it down a bit of a better way for you.

1:42:20

So this is your, uh, yes, you have the audits table. So, so, you have your, you have the audits table.

1:42:28

Um, just a second time, huh?

1:42:34

I'm just for him, uh, I'll just to erase. And, uh, I'll explain this. Okay? And this, I'll explain this. Okay? I'll explain this. Okay? And, uh, you know? And, uh, this is. And, uh, this. And, uh, this is your block.

1:42:58

color let's. And here here we, uh, it's, order amount. Okay? This is order amount.

1:43:07

This is order amount. Okay. This is called a primary key.

1:43:16

We have it's called the primary key. We call it. We take it. This table in order ID is called the primary key.

1:43:24

And this table on customer ID is called the foreign key.

1:43:28

Clear? Now can see this. Everyone can see this one in action. So primary key is the unique identifier in the base tables.

1:43:38

So, every table in, there's, some, no, what, primary key is. Primary key is what is? Primary key.

1:43:43

What is? Look, this is your partas in. And this is the special thing about databases. The conversation we had on Monday.

1:43:51

Monday, we had you said, this is the biggest difference between storing something in a data frame versus, like, database.

1:43:57

So data frame in these are constraints. What we are talking about right now at a very high level is something called constraints.

1:44:07

These were amazing things in databases. When databases were invented, these were some amazing things that started happening.

1:44:15

So some of a example they think. Let's say I open up an Excel.

1:44:23

Excel is an example of a flat file, up CSV, text file, TXT file, which be sort of.

1:44:27

Excel is such a popular thing. Most of you, that's the first thing you'll come to your mind.

1:44:31

Okay, Excel in some data, okay? So if you create a customer ID column, okay?

1:44:37

Here we can customer table can be able. I can have customer ID here and I can have customer name here. No problem.

1:44:45

No problem. No, okay? Now, Excel may I can have this. See? Customer ID can repeat. But is it possible? Imagine with your, you're a banking application.

1:44:57

You are a commercial bank for, and by the same customer ID repeat

1:45:01

that's a blunder, right? How can you have two customers with the same ID? It's impossible.

1:45:07

Impossible. So system we allow not to do. So these are limitations of these

1:45:13

platforms like Excel and other platforms where, like you don't have those constraints in post.

1:45:19

See, there are ways to do it. Now you'll say, yeah, sir, can't say, data validation,

1:45:23

some macros, like. See, I'm not saying that it cannot be done. There are ways around it.

1:45:27

You know, that's an Excel specific conversation, but there are way, but Excel is not meant for that.

1:45:31

Excel will not enforce.

1:45:33

That enforce, that you know, but the moment you talk about a database,

1:45:38

database, you can specifically define a particular column as a primary key.

1:45:43

You can it's a primary key.

1:45:46

Or this will typically happen during the table creation case.

1:45:50

So primary key is that particular column that uniquely identifies every single row.

1:45:56

unique identity. So customer table in the customer ID. So if you're customer table

1:46:02

look at customer table, customer table in every customer ID unique. So customer ID is the primary

1:46:10

key. When it comes to order table, every order ID unique is. Because when customers are

1:46:15

placing orders, every order ID is unique. You cannot have order ID 101. Amazon may say order

1:46:20

order ID replicated here 101. That's a problem. Amazon will never do that. Every time you go to the

1:46:26

cart and place and order, that is unique order ID. So orders table in order

1:46:31

ID unique. So this is what I wanted to clarify in this particular part of the demonstration.

1:46:35

Customer table in the primary key. Orders table in the primary key.

1:46:40

A go to foreign key. Forn key. What are. Foreign key is basically that table,

1:46:47

a column in the related table that references the primary key of another table. So, so the example

1:46:53

that you are able to see right now on the screen is

1:46:56

this. So this side go. This is the foreign key. So the customer ID of

1:47:03

from the orders table is related to the customer ID of the customer ID of the customer

1:47:09

table. This is your foreign key primary relationship. So the backy the same thing. So

1:47:14

the other things that you've seen is the same idea. Nothing is different. Only different

1:47:20

thing. Theoretically, what we have studied is the primary key what is the meaning of a primary key. You

1:47:25

don't have primary keys in Pandas. So primary key is a unique identifier. It's a it's a

1:47:31

column that uniquely identifies every row. That primary key is. And foreign key is basically the

1:47:37

other related column. So the customer table which customer ID is primary key, that is linking to

1:47:44

which corresponding column in the other table. So that column just for foreign key catch. That's

1:47:50

the concept. That is what we call the, you know, the foreign key.

1:47:55

Okay. So now, um, give me one second, guys. A lot of lightning happening

1:48:08

in my area right now. Just one second. Let me just, uh, let me just, uh, just along me a minute, huh? Yeah.

1:48:15

Just give me a second.

1:48:16

And it once happened with me before, the whole computer

1:48:28

he's all right. So I never take chances nowadays. Whenever there's lightning, I try to

1:48:33

plug off my devices. Just give me one second. Uh, okay, I think we can take it too. I think

1:48:42

we can take it. No problem. So I'll just give you one second. Just give me one second.

1:48:46

Okay. So now, now that we are now that we understand the basic idea of what is the

1:48:56

what is the primary key, what is the foreign key and how these two tables are related. Now on the

1:49:04

basis of this, we will write our very first inner join query. We will write our very first inner join

1:49:09

query. You guys already know what is inner join. This is the corresponding syntax in this thing.

1:49:16

Okay. Where do I stay? Right now, I am in India. So in India, I am from Calcutta. I also have a house

1:49:23

in Bangalore. I travel around. And I also have a residency in Qatar. So I'm actually spent six,

1:49:28

seven months there. So right now due to the war, I'm back in India. So yeah, so very much native of Calcutta,

1:49:35

from Calcutta. And then I stay in Bangalore also for much of my work. Yeah. Okay.

1:49:44

So came back here for the elections.

1:49:46

today. Today we are the elections here in Bengal, right? Big elections here that happened.

1:49:53

So yeah, yeah, exactly. Okay, guys. So inner join, all of you can see the query.

1:50:03

Everyone can see the query. So select from order stable, inner join customer stable on

1:50:11

o.comer ID equal to c. That is what we are trying to do.

1:50:16

okay. O dot customer ID equal to c. This is the inner joint condition and you want to select

1:50:23

these two. So let's understand this. Let's go step by step. Let's understand what is it that we are

1:50:29

you know, trying to do here. Let us understand this step by step. Okay. So so first what I will

1:50:35

do, I will go and draw my tables. So of course, some jane for let me do that. So order ID, customer ID,

1:50:45

amount or delivery date.

1:50:46

Or customer table we have this. So let me just write it down. Okay. So let me just write it down.

1:50:56

So here we have the orders table. So orders table may we have. We have order ID.

1:51:16

and delivery date. Okay.

1:51:19

Okay. This, these are the records in your orders table.

1:51:30

Okay.

1:51:32

Customers table in what got?

1:51:34

Customer's table. You've got, you've got three columns. What are the three columns? Let me just

1:51:40

quickly look it up. I think it was customer ID.

1:51:44

Customer ID. Customer ID. Customer name or city.

1:51:46

Okay, customer ID, customer name or city. So let me is a different color.

1:51:53

You have your customer ID.

1:51:55

It's your customer's table. Okay. So we have customer ID.

1:52:05

Customer name or city. These are the three, these are the three columns in the customer's table.

1:52:16

That's what we have right now.

1:52:19

And now, we are trying to join these two tables.

1:52:25

What are the common column?

1:52:26

The common column is customer ID.

1:52:29

Syntax, all of you, inner join.

1:52:31

Customers as C, very important.

1:52:33

Whenever you are doing inner join, you must use aliases.

1:52:37

Mandatory.

1:52:38

You're, you know, you're just a bit bit.

1:52:39

Why this important?

1:52:40

The reason is because you have you to callums refer to that from which table you want to

1:52:45

choose which particular column.

1:52:46

You want to refer, you want to refer that, hey, from the column, from the order table,

1:52:52

I want to refer to order ID.

1:52:54

And from the customer's table, I want to refer to customer name.

1:52:58

So, aliases are very, very important.

1:53:00

You must use aliases to make life easy for it.

1:53:03

Okay, best practice scenario.

1:53:04

Always use aliases.

1:53:07

Again, going back to the order of execution, subse prele, what are we doing?

1:53:11

Guys, hello, subse prele from inner joints.

1:53:14

This is the first thing that you are doing.

1:53:16

So you're taking the orders table, you're inner joining that with customer on this particular condition.

1:53:24

Same to same as we have discussed during our Panda session.

1:53:29

So, first, you will do this.

1:53:32

You are taking the orders table, merging with the customer's table on this particular condition.

1:53:38

Return what will? Return, all those records which are common.

1:53:44

All those customer IDs which are up.

1:53:46

on table 1 as well as table 2, I will return those rows.

1:53:51

So, first, we have joined here.

1:53:54

And then from that final resultant table, look, again, I repeat.

1:54:00

This is the joint condition, right?

1:54:02

Once you do this, okay, let me, let me show this to you.

1:54:07

Because unless you see this in action, you will really not relate to it.

1:54:11

Let me go back to my testing.

1:54:13

So if I go and do the inner join.

1:54:16

quickly, guys,

1:54:20

Kuch ne'i karengu. If I do this, select start, what will happen?

1:54:26

This is the normal query.

1:54:27

Orders, Leah, inner join customers, and we are doing select start.

1:54:32

When I do this, I will have total seven columns that will be returned.

1:54:37

Because you merge-hoeing, join-in-in-me, we are basically merging all the columns.

1:54:42

You will see, I will get seven columns as an output.

1:54:46

Pour from here.

1:54:46

are three from here. Exactly in that order. Okay? Order ID, customer ID,

1:54:51

order amount, delivery date. Or, orders, four.

1:54:54

Or customer ID, customer name, city. Here, three. And we are only returning those records.

1:55:01

You here, you know, you know, so where the customer names are, matching. This is what you guys

1:55:06

already know. And we are returning all the columns. So first, join and select the columns.

1:55:13

Start and select here. Everything is returned. But then, if you don't,

1:55:16

want to return everything. You can select. You have to what you need? If you only want

1:55:22

key, okay, orders table say, I only want order ID. Order's table say I only want order amount.

1:55:30

Customer table say, I only want customer name or customer tables I only want city. You can do that.

1:55:36

First, this will happen. The complete resultant table with seven columns will be formed.

1:55:43

Done.

1:55:43

So you're your from, join.

1:55:45

That's all the first,

1:55:46

then after select

1:55:47

remember the order of execution.

1:55:49

First, your join

1:55:50

from,

1:55:51

and join,

1:55:52

first. If I have to just

1:55:55

quickly take a digression and correct this

1:55:56

for you,

1:55:57

the first we will do from,

1:55:59

okay?

1:56:00

From and join.

1:56:02

Here we're from and join.

1:56:03

Here we're from and join. Okay? This is the first thing.

1:56:05

From and join.

1:56:06

Then where?

1:56:07

Then group by having, select, order by limit.

1:56:09

This is your updated order of execution.

1:56:12

Okay?

1:56:12

Because whenever you were,

1:56:13

do from and join, you are getting the result

1:56:15

and table. The final result and table

1:56:17

will come when you do for it from and join.

1:56:20

Okay, all of you? So simple

1:56:21

thing is. If you're here, then final

1:56:23

your four columns will be. Very simple.

1:56:26

And you can already start to see why

1:56:27

alias are important.

1:56:28

Mandatory, not, guys. If you tell me,

1:56:30

if you said, mandatory

1:56:31

not, you're not, you can, but it is a better way.

1:56:34

Because sometimes, you know, in practice

1:56:36

databases, when you look at real world databases,

1:56:38

the table names are very big.

1:56:39

So it's easy to use aliases.

1:56:43

All yeses means the alternate names.

1:56:47

Okay, that's a way we look at it.

1:56:50

So I hope everybody is clear.

1:56:53

So similarly, we also have a concept of left join.

1:56:56

I'm not repeating the whole thing again because you guys have done this.

1:56:59

So we can rather do some case studies in this time.

1:57:01

So inner join, your matching rows are getting returned.

1:57:05

What is left join?

1:57:06

Left join is basically where you are returning.

1:57:10

So sometimes you need all the records from one side.

1:57:13

regardless of a match. So that is where left join is very useful. It keeps everything from the left.

1:57:19

So all the matching pros are returned and it keeps everything from the left. So that's the use

1:57:24

use case of left join. Okay. So these are the two types of joints we have. Okay.

1:57:34

Okay. Now moving on, you can also do multi-table joints. Real world scenarios and use cases are much more

1:57:41

complex. In fact, if you want, we'll, we'll make a real world a query in a minute. So you can

1:57:46

actually get a flavor that, what kind of complex can. I will just show you. By the time I close,

1:57:52

we'll show you, we'll show you, which is based on seven tables. Seven tables. Seven tables. It's not

1:57:57

very difficult because all that you do is you take the student's table, join with the sports table on this

1:58:05

condition. So the way you think about it, the way you try to understand this is step by step. So

1:58:10

so first you are joining this with this.

1:58:13

Okay?

1:58:13

So first you're joining these two.

1:58:15

Your resultant table

1:58:16

a year, then you are taking that

1:58:18

resultant table and you're joining with this.

1:58:21

That's the way how you think about it.

1:58:22

So even if you're joining seven tables, it is not very complex.

1:58:25

You know, we make it complex, but

1:58:26

the way you think about that join is that you look

1:58:30

at we are merging two tables at a time.

1:58:33

First, students or score go joined here.

1:58:35

Resultant table came and then

1:58:37

those resultant or modules for join here.

1:58:39

Final table are.

1:58:39

that's the way how we look at it okay i hope everybody's aligned okay so this is the way how we go about the

1:58:49

process of joining multiple tables just to show you the syntax you don't have to we don't have a

1:58:53

case study for this but this is just to show the syntax to you what is it what do we do in

1:58:58

real world scenarios okay now we'll get to some real world scenarios we will discuss some of these

1:59:02

you know real world scenarios here okay so before that uh to join exercises

1:59:08

then we'll do some practical scenarios also where we'll put all of the things together

1:59:13

this is a interesting query we will do and then we'll get into some real world case studies

1:59:17

the exact same thing we will replicate okay so first point one and four point two guys everybody

1:59:24

let us do this it'll be good practice for all of us so 4.1 and 4.2 everybody please try this out

1:59:38

with this now it is completely exercise time so we have enough time

1:59:51

left i think around uh we'll take another 20 25 minutes for some exercises okay

1:59:56

and we will try to solidify these ideas more and then take up some questions with all of you

2:0:00

Okay.

2:0:30

Thank you.

2:1:00

Thank you.

2:1:30

Thank you

2:2:00

Thank you

2:2:30

Thank you

2:3:00

Thank you

2:3:30

Okay, very good, very good, very good guys,

2:3:45

so left, so the left join is okay,

2:3:49

here the left join is okay, here the left join is not relevant not because because you know, we don't have any null values.

2:3:54

So, okay, you can do it like an inner join only.

2:3:57

You can do it like an inner join only.

2:3:59

But from a

2:3:59

syntax perspective of you will have to do left joint that's it instead of writing inner join you will write left join but here it makes no difference because you know we we we don't have any null values right now so

2:4:11

going matching records in a sorry not null value going matching records like we don't have any like records which so here i you know it shouldn't be any difference

2:4:21

let me just check before i confirm this to you let me just check i want to be very sure that that is the case one second customer ID one two three

2:4:29

here.

2:4:30

24th up here.

2:4:32

There are customer ID

2:4:33

here.

2:4:34

There are customer ID

2:4:35

is not coming.

2:4:37

Is it coming?

2:4:38

Yes,

2:4:39

yeah, I think here your

2:4:40

Farrat not

2:4:41

anyway.

2:4:42

That's okay.

2:4:43

I just wanted to clarify.

2:4:44

Okay,

2:4:45

let's see.

2:4:46

Okay, let's see.

2:4:59

Okay.

2:5:29

So this is your, this is our first one.

2:5:32

We are doing inner join here.

2:5:33

The first one, you can see, get a list of all order IDs along with the corresponding customer name.

2:5:37

So we want the order IDs also, customer IDs also.

2:5:40

So we want information from both the tables.

2:5:43

So again, use case of a join orders, inner join customers on this particular condition because

2:5:48

this matching column is.

2:5:49

Okay, just you have pd.murge here and then O.

2:5:51

dot order ID equal to c.

2:5:53

C.comer name and C dot customer name.

2:5:54

So from this table, you want the order ID and from the customer table, you want the customer table.

2:5:58

You want the customer name.

2:5:59

so that's the matching condition that we are getting right now okay so you're able to see

2:6:02

order ID and customer name is returned next one next one what are we required to do next one we are required

2:6:10

to go and print out show all customers name and city and their order amounts including customers

2:6:22

who haven't ordered anything to host are that there are some customers who have not ordered anything

2:6:26

so they will be there in the customers table but they will not be there in the customer's table but they will not be there

2:6:29

in the orders table. So matching records will anyways be returned, but we will also return

2:6:34

cases of customers who are not in the order stable because customers table is main table. Whenever

2:6:40

you register with Amazon, let's say there is a customer ID 100. So that's customer's table

2:6:44

but that 100 never order in order table. So then we do a left join. Okay, exactly how you saw

2:6:52

in our data frames. Okay. So you can see this one. So again, customer name city and

2:6:59

these are the things that will be returned. Okay, all of you can see.

2:7:06

Okay, everyone can see this. Okay, this is a very interesting use case. This is a very interesting

2:7:09

use case, Rohan Das. So actually, actually, one is a, a,

2:7:12

customer has, which has ordered not. So let us see, very interesting. Here

2:7:16

we have customer ID, let's see what is. So c.c dot, uh,

2:7:21

c dot customer underscore ID. So there is a, it turns out there is a customer called

2:7:28

Rohan Das who has not ordered anything. So very interesting. You can see

2:7:36

it. Its customer ID5. So Rohan Das is there in the customer table. They

2:7:41

registered with Amazon with. Rohan Das is there. Okay. And it's primary. He's from Calcutta. But

2:7:47

if you see, this customer ID5 has never ordered anything. If you're

2:7:51

the orders table, then this customer has never ordered not. Now, look. Now, look,

2:7:55

look, customer ID5 has any. So this is a beautiful use.

2:7:58

left join, okay? So this condition of our left join. So if you do inner join, very interesting.

2:8:05

This thing if we're in inner join, right? This thing if you're iner join,

2:8:10

you can't, whenever you do inner join, what is the difference, guys? Rohan Das will not come.

2:8:18

Baking, all right? So Rohan Das not will not. Now, look, customer ID pipe, right? Okay. So

2:8:24

if you're not. So if you're, so if you're a better way to understand to, so you know, so you're order by,

2:8:27

order by customer ID. Okay?

2:8:31

Order by, uh, yeah, C dot customer ID.

2:8:34

And if you do that, you will actually see that Rohan Das is not there.

2:8:38

Customer ID 5 is not there.

2:8:40

So when you do inner join, only the matching rows will come.

2:8:43

So customer ID 4 a, but 5 skipped.

2:8:45

Sixth is 6th, 6th.

2:8:47

Okay?

2:8:48

But the moment you do left join, the moment you do left join, same to same query, the moment you do it this way.

2:8:55

Now, you can see, here, Rohan Das will, okay?

2:8:59

3 was, 4 was, and 5 was, and 5 in, we are printing out the customer ID,

2:9:05

corresponding customer name, which is Rohan Das,

2:9:07

corresponding city, customer table, but

2:9:10

corresponding order table has its order amount, so that null came.

2:9:14

So it's not. See everybody, what is the meaning of left join?

2:9:16

I'm just trying to recap.

2:9:17

I'm assuming everybody has seen this before, okay?

2:9:20

It's just a small recap.

2:9:21

Okay, so we'll share all share with you.

2:9:24

So I'll be sharing this with you.

2:9:25

Whatever variation.

2:9:25

I'm doing is updated file I'll be sharing by the end of the class. Don't worry.

2:9:30

All of you, everyone with me? Please confirm to me on chat.

2:9:34

All of you are with me?

2:9:36

So what I said, whatever I explained.

2:9:40

Please let me know, guys.

2:9:42

If any doubts is there, please ask me.

2:9:45

All clear everybody understood the use case with Rohan Das. What is going on?

2:9:52

Others are all good. Only three of you have.

2:9:54

So it, guys.

2:10:00

Okay?

2:10:03

Final thing, we'll

2:10:04

a query that combines everything.

2:10:07

This is actually a very interesting business question.

2:10:10

So you'll see, I won't say it's a very complex query,

2:10:12

but fairly complex,

2:10:14

fairly complicated.

2:10:15

Looks quite big.

2:10:17

And it's a very interesting business question.

2:10:20

I'm going to solve

2:10:21

so solve care.

2:10:22

So what do you want to do?

2:10:24

you want to find out who are the who are the customers who are the customers

2:10:33

who are the customers from Mumbai who have spent more than 20,000 in total

2:10:39

you have everything select who are in join who are group by having order by everything

2:10:46

except for limit who limit me to do last minute so

2:10:49

everything so this is how the business problem will be

2:10:54

framed. So management wants to know who are the customers from Bombay who have spent

2:10:59

more than 20,000 in total. Let's say they want to find out some of the top customers, give them

2:11:04

some offers and whatever. Let's say some Mumbai promotion campaign is happening, whatever,

2:11:08

okay? So how can't. So how's the first from and this is also a very best practice way

2:11:15

how you write the query. First of the query, this is also something I want to teach you. Always leave blank.

2:11:21

Now first select start not.

2:11:24

First, just leave a blank and say select from.

2:11:26

Now, first, from from from customers, inner join this. And then you start exactly in the order

2:11:32

you write the query. Okay. So customers, inner join orders on customer ID. This is the common

2:11:40

column. So this is your first from from and join. Next, you're only looking at customers from

2:11:47

from Bombay. This is your filter. Where city is Bombay. So city,

2:11:54

to Bombay. Filtered. Okay. Okay. Next, we are grouping by customer ID and customer

2:12:02

name. Because we want to find out which customers have spent more than 20,000 in total. So now that

2:12:09

we have filtered all those customers specific to Bombay, I want to find out who are those customers now.

2:12:14

Group caro us and group based on ID and name. Find out who are those customers,

2:12:19

which's total order amount is greater than 20,000. So group by Kia.

2:12:24

Having here. Having is a filter within group by, remember. And I'm printing out both of them.

2:12:31

And what is it that I want to ultimately display? I want to display their name.

2:12:36

P.customer name. The count. The number of orders. Count. You can here star be. Goh

2:12:41

not. Count start be going to. And sum of order amount. So that's the complete thing. And you want to

2:12:47

sought by higher spenders first. So order by descending order. This your final end to end query

2:12:53

Okay. Fairly advanced one, fairly complex one. Whatever we have, you know, we are seeing

2:12:58

right now. So again, I repeat, from, join, you get the final result and table.

2:13:06

Join, kind of result and table.

2:13:08

Then after where? Filtered.

2:13:11

Then, then group by.

2:13:12

Then, then aggregate. Find out for every customer, what is the order amount, total order

2:13:16

amount. What is their total order value?

2:13:18

And then we are going and setting the condition.

2:13:22

only get me those customers whose order value total is greater than 20,000.

2:13:26

Cliving clause in. And finally, only select those corresponding columns.

2:13:30

And finally, select after last, it was the order 5.

2:13:33

I hope everybody's clear.

2:13:36

And if you want up, last make limit, do you want to find out the top two.

2:13:39

So limit of two can go to last make. Only the two which you opt.

2:13:45

Okay.

2:13:45

Okay. Let's go and simulate some practical case studies where we will see some

2:13:50

some interesting, you know, use cases in action.

2:13:55

So this is to simulate students and schools.

2:13:58

Basically, okay.

2:13:59

So there are two tables I've given you slide now.

2:14:02

And here, very interesting, what I have done, I have gone ahead and I have actually

2:14:06

initialized the primary key.

2:14:08

I was explaining the primary key, but you can't see,

2:14:11

during the creation of the table itself, I have defined the primary key.

2:14:15

So here here we have two tables initialized here.

2:14:18

So this is a small ed tech kind of,

2:14:20

a use case.

2:14:21

You have a students table.

2:14:22

You have a scores table.

2:14:23

Imagine something like a massage pool where we will have a student's table.

2:14:27

We will also be having a tech team, a database where we have the information about all

2:14:31

the students.

2:14:32

So this your student's table.

2:14:34

Okay?

2:14:34

Let me create the table.

2:14:36

Or this your score stable.

2:14:38

Okay.

2:14:39

Let me do this.

2:14:40

I will insert some dummy values.

2:14:44

Insert into how yeah.

2:14:46

And finally, we will look at some sample queries.

2:14:49

Okay.

2:14:50

So we can ignore.

2:14:50

these parts these are I think again things we know already so we can ignore this

2:14:53

part and we straight away come to the demo exercises. So objective is to go and solve these

2:14:58

exercises right now. Let me go and let me go and show you the tables for a minute. What are the

2:15:11

two tables I created right now? So we have created something called the students table and

2:15:16

something called the scores table. You have got two tables somewhere select here.

2:15:20

So we are on to our new case study, a different table data.

2:15:28

So students table has information about all the students, student ID, name or batch.

2:15:32

And this is what we call the primary key.

2:15:34

Because every student ID is unique.

2:15:36

And finally, scores may we will have information about score ID.

2:15:40

A ID is a score.

2:15:41

Okay.

2:15:42

Which students secured what score?

2:15:44

Let's say there is a student ID one, Rohan, Roshan, whatever name you take, right?

2:15:48

And which module, how much marks they got?

2:15:50

Something like that. Okay. So this is the use case. And what I wanted to do, you have to go and

2:15:57

solve these two exercises. Okay. Exercise A1, exercise A2. Everybody try it out. In case you are

2:16:02

doing it in the one compiler, I will guide you. I will guide you. So just go ahead and clean it out.

2:16:08

It is one compiler in kind of one compiler. Like you might have too much there. So just go and

2:16:13

clean it. You off it. This is the easy way to get started. So just refresh it once. Or what you

2:16:19

can do is you can just go and kind of use this link again. Just select and use this link

2:16:26

again. Now you go back say select and you can just recreate your tables. Okay. So you can start

2:16:34

directly from here. You can start directly from here. Create table. Students create table

2:16:41

stores. Insert values into tables in students. Students insert values into scores. Simple.

2:16:47

Okay. Okay.

2:16:48

here from you. See, create table student, create table score, uh, insert into a student,

2:16:54

insert into score. Okay. Okay. And just click on run. Table

2:16:58

and now just go ahead and solve this problem. Solve these two exercises in the same order.

2:17:05

So exercise A1, exercise A2.

2:17:18

Let me know. I think I would really like all of you to do this.

2:17:24

This will be a good practice with respect to joins group by having everything that we have

2:17:28

discussed so far. We'll try to see some case studies based on that.

2:17:48

Thank you.

2:18:18

Thank you.

2:18:48

Thank you.

2:19:18

Thank you.

2:19:48

All good guys, let me know, let me know, and I think the best

2:20:02

All good, guys. Let me know. And I think the best way to work towards this is try to draw the tables.

2:20:10

So you guys can actually draw out, okay? So run the query, tables for

2:20:15

don't try to solve the problem directly. Okay? So in case you are trying to do this in your one

2:20:21

compiler. So how do it just to make it easy for you, just to make it easy for you. You just to make it

2:20:25

easy for you. You can this is the way how you should do it. This is the way how you should do it. Don't

2:20:30

just directly, you know, start writing the join. It will be hard. So first try to

2:20:34

display the tables. And here it's easy because you're up outputs at

2:20:38

right. So select start from students, select starts from scores. Try to display both the tables

2:20:46

and then try to think in terms of that. Okay, okay, yeah our student table here. This

2:20:51

our score table. And then based on that, how do I solve the problem? Okay. So as you are seeing

2:20:56

the table, now you try to see how you can solve the problem. Because now you'll be able to

2:21:00

see the data structure. You need be able to see what are the columns, what are the joins, okay?

2:21:04

So this is the way how you should mentally frame the query. Definitely there is AI that you can use,

2:21:08

but this is the way how you should frame it mentally. Everybody tried this out. These are

2:21:15

slightly tricky, okay? Won't be directly, you to think a little and then frame that way.

2:21:30

Thank you.

2:22:00

Thank you.

2:22:30

Okay.

2:22:58

Great.

2:23:00

I hope the queries are running. Everybody also make sure you are running the

2:23:05

queries in one compiler.

2:23:06

Okay.

2:23:30

Thank you.

2:24:00

Thank you.

2:24:30

What about the rest of you, everyone, everyone's able to do this,

2:25:00

Thank you.

2:25:30

Thank you.

2:26:00

Thank you.

2:26:30

Okay.

2:26:37

Okay.

2:27:00

Thank you.

2:27:30

All.

2:27:34

All right.

2:27:37

All right.

2:28:00

talk about this. So the first one would be the first one as, as you rightly messaged.

2:28:07

This is the way how we will solve the first one, exercise A1. And I will share this with this with everybody.

2:28:14

You can once again see I'm taking the students table. I'm taking the scores table, joining based on student ID.

2:28:20

and then we are grouping by the student ID and student name because for every student I want to show what is the average marks.

2:28:27

This is like your pandas group by.

2:28:30

And then I want to ultimately display the name and their average marks.

2:28:34

So that's the way how we are looking at it. So for every person, I can see what is their name and average mark.

2:28:40

If you want to display this in a better way, what you can do? It is not asked in the problem, but you can do an order by, you can do an order by average underscore mark.

2:28:49

I have ordered by and order by say you can display this in a better way. You can see who are those students who secured, like who are getting the highest marks.

2:28:58

this is the way to do that.

2:29:01

So Ria is the top most avarice food.

2:29:03

Next, Jasmine, then Pia, then Frank, then Manoche and so and so forth.

2:29:08

Okay.

2:29:09

Next question.

2:29:12

Exercise number two.

2:29:14

Second exercise.

2:29:15

Let us see this in action.

2:29:17

There it is.

2:29:18

This is the way how we will do this.

2:29:22

How to run the code on one compiler where I get the data.

2:29:26

No, no, that's what I explained Arnika.

2:29:28

I explained exactly that only.

2:29:31

Just do it this way.

2:29:33

There it is.

2:29:34

Create table.

2:29:35

Create tables, core, same thing.

2:29:37

Whatever I'm displaying here, you can create the thing here also.

2:29:41

So in one compiler, what you do, just run the create table.

2:29:45

So behind the scenes, your table is getting creative.

2:29:47

First, create the tables, insert the value into the tables, and then select star.

2:29:51

Okay?

2:29:52

And then let me copy paste the same fold.

2:29:55

See how it will beautifully execute.

2:29:58

So now.

2:29:58

Now, I have students and scores table already created, right?

2:30:03

So this is our first exercise.

2:30:06

Now run it.

2:30:07

Everything will come.

2:30:08

It will be displayed in the right order.

2:30:10

So first you have this, then this, then this output.

2:30:13

This is the final output that we created.

2:30:15

So whenever you run a select query, the outputs will be shown this way.

2:30:22

One after the other.

2:30:25

Okay, it.

2:30:25

Karnik, I hope you are clear.

2:30:27

So you can take exactly my screen.

2:30:28

and put it in one compiler and it will work the same way.

2:30:32

No problem.

2:30:34

Okay?

2:30:34

Next exercise.

2:30:36

If you want me to run this also, let us do this.

2:30:39

Okay?

2:30:40

Let us run the next one.

2:30:42

If you want to clean this up, you can do that.

2:30:44

You can do that.

2:30:46

Next one will be this.

2:30:49

So select,

2:30:51

again, join the students with score,

2:30:57

where batch is data and data.

2:30:58

analytics and module is Python and marks is more than 80.

2:31:02

It's a wear condition.

2:31:05

And we want to eventually return the name and the marks.

2:31:09

There it is.

2:31:10

So this is the thing that we'll get me.

2:31:14

So you are able to see exactly as per what is asked.

2:31:17

Find students in data analytics whose code because this will not come in having, right?

2:31:21

There's no group by.

2:31:23

Yeah, paper, join karni or where can do.

2:31:25

There's no question of aggregation.

2:31:27

We just have to show the name-wise mark.

2:31:28

That's it. That's the use case.

2:31:34

Okay?

2:31:36

Ahcho.

2:31:54

So we can skip this. Let's skip this one. Let's skip this one. Let's skip. Let us skip. Let us come to the next one. Let us come to the next one.

2:31:58

I'll share. Let us do the last one. That is ride-hilling. This is the ride-hilling case study.

2:32:04

So we'll two table, we'll make riders and drivers. Exactly how things happen in the context of

2:32:09

Ola, Uber, right? So we'll do tables banayers, riders and drivers. And I will insert some

2:32:15

values into drivers and insert some values into rides. And now we will go and solve some of these

2:32:21

questions. So these are the two tables that I have right now. One is the driver's table. Or

2:32:28

And just to help you understand the schema a little better, you can see the driver's table, driver ID, driver name joined it.

2:32:37

Driver related data. So driver made up joined the platform. Who is the driver like that?

2:32:42

This primary key. And ride stable, every time you book an Uber ride, every time you book a ride with Uber or Rola or whatever, a ride ID gets created behind the scenes.

2:32:52

Who a transaction is, who your activity, ride. So who booked the ride? Which driver took that right? How much fairer?

2:32:58

was paid and was the status completed or not? So this is used for driver level tracking.

2:33:04

You have tracked to give them some performance bonuses, things like that.

2:33:10

Okay? Now, this is the business use case. Okay? Exercise C1, C2. Last of the two case studies we will do.

2:33:19

All of you try to solve it. All of you try to solve it. This is exactly how enterprises will also work.

2:33:26

Right? So again, everything is based on a business problem.

2:33:28

How you're framing the problem. You want to reward your top earning drivers.

2:33:34

Top earning drivers phone. If drivers are making more money, if drivers are giving more business,

2:33:38

then Uber's commission is, right? They are taking 35, 40% of the money in commissions.

2:33:43

If you have a driver that is giving you more business, then that is good for Uber, right?

2:33:48

You want to find out who those drivers are. And they have models, right? Uber in whatever drivers are.

2:33:52

whichever drivers are giving you more business and who are doing well, Uber promotes them to Uber black.

2:33:57

Uber black may, to go to Uber black thing, the drivers need to, you know, have a certain

2:34:03

minimum rating and certain minimum number of trips. These are criteria OTA. So based on that,

2:34:07

Uber will reward some of these top performing drivers. Everybody, last two exercises.

2:34:27

Thank you.

2:34:57

Thank you.

2:35:27

Thank you.

2:35:57

Thank you.

2:36:27

this is a bit of a difficult one you will have to put some thought around it right out all of all of you

2:36:35

all of you and while you and while you guys are solving this i wanted to just quickly

2:36:43

complete the story here just one final piece here and you can continue on with this this is the

2:36:48

5th into sequel bridge just wanted to talk about this last part okay i think we can all relate to this

2:36:53

this just say i'm a group i did the same thing in

2:36:57

in Pandas is this group by dot sum. This is the bridge. Same to same concept.

2:37:01

There is no difference, right? Okay, but I think some of you found the SQL query is easier

2:37:06

to relate to. Whatever we did in a join and on, the same command in Pandas is this dot merge.

2:37:13

Okay. And finally, whatever left join we discussed, the same command in Pandas is this.

2:37:19

This is the sequel to Python bridge. And the last part that I've already discussed multiple times is this.

2:37:24

The order of execution. Very, very important. So from.

2:37:27

First, prom and join. Then do the where, then group by having select order by limit.

2:37:36

That's the order of execution. Just keep this at the back of your mind.

2:37:41

Yeah, you can continue on with the eating. And I will just discuss one last point just for a couple of minutes

2:37:47

after you complete this exercise. And then we'll go to the quiz and other things.

2:37:53

Just all of you complete the exercise. Okay, murmur does paint.

2:37:57

So interesting case study is because we are trying to use all the aspects we have discussed in that class.

2:38:07

That's the form of this last case study. We are trying to use everything. Join where group Y having

2:38:12

everything. Except for limit we are using everything.

2:38:27

Thank you.

2:38:57

Oh, exactly the last thing I will talk about it. I remember. I remember. Once you want to complete this. I remember. Once you complete this goal. I remember. Once you complete this dernier, I remember. Once you complete this. I remember.

2:39:25

once you complete this case study that's the last thing there is there's actually nothing to show you

2:39:29

there's only one package i will discuss is very simple i will show you that don't go i will show you that how to

2:39:35

write in pandas

2:39:55

you know how many

2:39:57

you know

2:39:59

Thank you.

2:40:01

Thank you.

2:40:31

Thank you.

2:41:01

okay everybody is done can we discuss all of you yeah wanted to want it all of you to do this

2:41:16

genuinely so the last of the use cases let us see finally how we'll work towards it

2:41:24

so we want to reward our top earning drivers

2:41:31

and this i'm not running this i'm just trying to show you directly from here because anyways

2:41:35

i'll be sharing this uh hand out notes with you so uh i'll be sharing this with all of you

2:41:42

and you can see this one so again join the driver's table with the rights table on the driver

2:41:50

id because in both the tables the driver id is common and you want to only show completed rights

2:41:56

so please filter by completed and then you want to know for the driver who have earned more than

2:42:01

500 in total so if we group caro and find out that having some of fair at the total fair

2:42:08

across all the drivers should be more than 500 so that's the way how we want to do it so let me just

2:42:15

show this to all of you how this looks like in the code so this is how it will look like

2:42:24

okay everybody can see this in action so we are able to see who are the drivers and what are their

2:42:29

and i think the last thing you can always do an order by because order by say

2:42:33

you know like order by total learning that's the best practice thing to do

2:42:39

otherwise the results are not sorted right you want to see uh the results in descending order

2:42:45

by total learnings okay so this is the way how the query will look like so rancho is obviously

2:42:50

the best driver by a long margin you can see by a long margin he is the best driver so join who are

2:42:58

where was filter got the only completed drives we are tracking group by driver

2:43:04

find out the total fair they've earned and uh show that and group by uh order by the earnings

2:43:14

okay done all of you last thing i will talk about this is the last one again here

2:43:20

here here here here having ne'i ever remember having is is filtered on this is the way how you will do it

2:43:28

drivers and rights join right status is cancelled you want to find out the number of

2:43:35

canceled rights for driver because that that can be a penalty at times right so can we

2:43:39

find out which are those uh uh uh drivers who are doing too many cancellations

2:43:43

and can we find that out grouped by those uh driver ID and driver name and can we go back

2:43:49

and find out the number of cancelled rights so this simple data so basically most of the

2:43:55

drivers have only got one cancelled right each the rest of way how

2:43:58

we look at the solution so what i will do guys i'll be sharing this uh file with you okay

2:44:05

and the last thing that i will talk about and as always rightly say is panda SQL very simple

2:44:11

there is actually nothing to talk about it here very simple so pandas SQL is basically like a

2:44:17

very nice way where you can write SQL queries right within pandas okay so simple some example

2:44:22

let's do that just it'll take hardly two minutes more okay so what i will do right now

2:44:28

is i will go ahead and uh create a simple demo data frame for you

2:44:38

okay and this is how your data frame looks like all if we can see this just a second guys i

2:44:44

forgot to select the column so that's how your data frame looks like right now everybody can see

2:44:58

okay so there goes my data frame on let me just quickly do this once again

2:45:11

just select my problem and uh there is my data frame a sample sample demo data frame is what i've

2:45:18

chosen and now what i want to do i want to run a basic sql operation on this data frame so we can use

2:45:25

use something called panda's sql right normally if you

2:45:28

which data frame operation karni then you have to go and write the panda syntax but turns out

2:45:34

there is a particular package in python called panda's sql if you use pandas sql you can run these

2:45:39

kinds of queries you will have to install pandas sql so we have to go to terminal and i think

2:45:45

all of you know how to install a package right everybody knows that so you have to go to this

2:45:49

and you have to pip install uh pip install pandas sql so wep install the panda's sql module

2:45:56

panda sql right so if you can install this and after you do this this is a simple piece of

2:46:04

code that you will have to write okay very simple this is the simple way how you can do it so

2:46:10

yeah your data frame here df okay and all you have to do is import it and just write the query here

2:46:16

here here here your select query will go which you guys find it very easy now okay so you can

2:46:20

treat a data frame like a table now you know so your data frame here you can create it like a table right

2:46:26

now that is the simple way how you can work towards it okay so this is the way of

2:46:31

we have our install here right now and you can see i can effectively run this or here our

2:46:38

results are here isn't this cool guys isn't this cool isn't this cool up there

2:46:42

here here here our data frame so whatever we've been discussing in squel you can go and run those

2:46:47

exact same operations using panda this is the last part of what i wanted to cover

2:46:52

with all of you okay i'll share this notebook also with you okay where is

2:46:56

simple you can take any data frame you can take a data frame with seven rows you can take a

2:47:00

data frame with seven billion rows which for it need perfect same to same the queries will work

2:47:04

of a data frame though up does data frames know all that you have to do is whatever

2:47:10

learnings we had in the class you can basically wrap it inside a sequel query so you can take

2:47:15

select uh something from df inner join df2 inner join df3 you can do everything and all that you will

2:47:22

do right now is you will do sql df query so after

2:47:26

your python environment in jithn every data frames there

2:47:29

that's on whatever is in your runtime right now you are simply running sql df

2:47:35

a query you're just running this query so whatever data frames are there you know it will

2:47:40

operate on all your data frames and it'll treat them as tables

2:47:43

or the final result set here you're your final result set

2:47:46

okay where will group by all the typical sq query will work

2:47:51

okay i hope it's clear all of you so i can just share it here only with everybody

2:47:56

and uh that will be pretty much all that we have uh yeah okay always i hope we are clear

2:48:06

everyone's fine but just remember guys once you're running this thing you will have to pip

2:48:10

install panda sql because panda sql is not a uh built-in package you will have to install it

2:48:16

make sure you're installing panda sql and then you can write all your because sometimes the

2:48:20

data frame syntax can be confusing right so if you're up

2:48:23

if you look sql jada easy in terms of syntax where group buy then you can absolutely do this things

2:48:28

i must warn you from a performance perspective this is not very good it's easy to understand

2:48:33

easy to learn but not very good from a performance perspective it's a little slower actually so

2:48:38

just for using purpose learning purpose this is nice to know but if you're asking me from a real

2:48:43

world scenario what do we actually do we don't use this because it is very slow comparatively so

2:48:48

panda sql is slow compared to normal panda syntax please keep that at the back

2:48:53

of your mind because this a layer it's a layer on top of your regular pandas okay

2:48:57

okay all right great so uh yeah that's all from my end uh right so i'll hand it over to pratab

2:49:03

prathap you can take over yeah thank you sir just before i take over oh yeah yeah sure sure sure

2:49:09

sure absolutely i remember uh yeah so yeah so yeah right so just to summarize all the things that we

2:49:14

covered guys uh yeah we looked at everything so we talked about group by aggregations we talked about

2:49:23

having flaws in detail we looked at inner join joining tables we talked about

2:49:27

multi-table queries understood the ideas around how inner join works across multiple tables

2:49:33

and finally the last part of you know funder versus sq will so these are the general requirements of the

2:49:38

session but obviously we have seen a lot lot more than what is just listed here yeah thank you thank you

2:49:43

Pratap thank you to the others as well and yeah so i'll i'll hand it over to you yeah okay so guys i'm

2:49:52

going to release the feedback poll now and yeah the feedback poll should be up now thank you so

2:50:04

i have the feedback poll up guys and i'm going to start to share my screen also for the mitymeter quiz

2:50:22

guys also just to update i will just go and update the files on the drive for you once again okay

2:50:28

so you can refer on to the updated files as well okay oh yeah before i forget thank you so

2:50:38

much sir for i mean for another amazing lecture and yeah okay okay

2:50:52

all right so it seems everyone has voted i am going to be sharing the link again in the

2:50:58

chat for the mentimeter quiz and i'm going to start it okay and pull close all right

2:51:17

okay students quickly join the mantimeter quiz

2:51:47

anyone else who wants to join they can join i'm just going to wait for about

2:52:04

about 10 seconds more and then i'm going to start okay i'm starting

2:52:34

easy questions based on what sir has covered one or two might be difficult these are the

2:52:46

ones that i think you should be that i mean this is the one you should be able to answer everyone

2:52:51

should be able to answer easily what is count star return

2:53:04

okay yeah so there it's not number of non-null values in a column that is because

2:53:14

you are using count star if you define if you use count with a column name then the first answer

2:53:21

first option becomes correct otherwise this is the correct answer and sum of values in a column

2:53:28

is not there's a you have to use aggregate sum for that so all right next next

2:53:34

way okay next question next question about about i think about 10 participants seven

2:53:56

people are only playing rest are watching or what okay next question started started

2:54:03

what happens when there is no match in a left join.

2:54:33

one would be getting this correct oh okay row is removed no row is not removed um for a

2:54:40

left join because whatever is the left side index that you're joining the table on uh

2:54:48

if there is no match then the null value will be inserted in the right table okay all right next question

2:55:03

all right i'm starting seems only seven people are oh there's an eight one i think

2:55:33

so if okay yeah so if okay yeah so if you guys remember left join you have all rows from the left table

2:55:56

and right join you have all rows from the right table amazing every single one of you got that correct

2:56:01

so great great job all right right right

2:56:15

question uh should i wait for the 8 player or not let me know in the chat okay all right

2:56:31

What happens if you use where average salary is greater than 50,000?

2:57:01

this one is a bit tricky yeah yeah so uh it was it was intentionally it was a tricky

2:57:14

and it will not be filtering after grouping it will cause an error because you will you cannot

2:57:20

have uh where with an average this thing uh you will be having instead of having there will be a having word

2:57:28

the word is having here instead of where so if it converts to having automatically if this

2:57:35

was a correct answer then so uh in sq it doesn't correct it doesn't convert to having automatically

2:57:44

but if it did then this would not throw an error and so then it would not be a wrong thing but two of you

2:57:51

did get it correct it does cause an error so awesome awesome this was a tricky question

2:57:58

the next one is going to be a long tricky question so intentionally i have removed the time limit

2:58:07

and you guys have a lot of time to kind of play it out maybe even write it down in the notebook or work through it

2:58:16

okay but i want everyone to be able to give the correct answer okay the next one is going to be a tricky question so

2:58:28

it's basically it's just an sq query that uh you have to give me the results for okay no time

2:58:35

limit on this one and the well no no no first person first come first serve nothing like that

2:58:43

uh and the time limit for this is what two minutes so i'm sure you guys can do this

2:58:54

okay i want everyone to try i think one person has already given

2:58:58

up and voted. I want everyone to try.

2:59:28

understand the options understand the query and try it out and don't don't worry about answering first

2:59:39

take your time if you need there's no whoever answers first gets the most point

2:59:47

nothing like that this is based this is based on one of the last like your last like your lecture

2:59:58

if you can solve this in like two minutes, then you can solve this in like two minutes, then you should be able to

3:0:23

to really work through your evaluation questions very fast.

3:0:28

all right i think we are done awesome awesome really awesome most of you got it correct

3:0:47

i think the one person who just uh clicked instantly without looking might have gotten that wrong

3:0:53

amazing and you guys did understand this correctly that there will be null as an average

3:1:00

because it's a left join okay awesome awesome guys now let's see

3:1:09

congratulations nia all right now with that we are done with today's session

3:1:24

right session and i will see you guys in the upcoming i think it's a tutorial or it's a revision

3:1:32

session i'm not i'll see you guys in the upcoming session okay have a good night night bye