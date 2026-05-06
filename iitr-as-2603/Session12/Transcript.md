0:00

Thank you.

0:30

Thank you.

1:00

Thank you.

1:30

Thank you.

2:00

Hi, everyone and very good evening.

2:10

We'll start this session and next two or three minutes.

2:30

Uh, Rahul, can you make me the host please?

2:42

Hello, Rahul.

2:59

Yeah, can you make me the host please?

3:00

Please?

3:01

Yeah, yeah, I'll do.

3:02

Give me a minute.

3:03

Okay.

3:04

Good.

3:05

Good.

3:06

There is a good.

3:22

There was a yeah.

3:24

Just wait for a minute.

3:26

Everybody, please join.

3:29

I know, I know, don't worry, don't worry. We are back on track. Everybody's here. I think, I know there was some joining issues, but we are back on practice.

3:46

Yeah, yeah.

3:52

Okay, so.

3:59

give you the I'll make you the host here one second.

4:06

Okay. Yeah.

4:29

All right, great. So do we have everybody or Pratab, do we wait for a few minutes? What do you say?

4:39

Let's wait for maybe two minutes and then we can start.

4:45

Okay.

4:46

Okay.

4:47

Okay.

4:48

Okay.

4:59

Thank you.

5:29

Thank you.

5:59

Sir, sir, I think you can start.

6:13

Okay, done. Let's start. Okay, done. Let's start. Okay.

6:29

All right, folks, once again, very good evening to everybody.

6:59

So let's start on here. I'll share my screen with all of you.

7:03

Hope everybody is doing well.

7:06

Today we start on with a very interesting topic which is on the data visualization and EDA.

7:11

That's the core agenda of today's session.

7:14

Plotting and storytelling with data is what we are discussing here.

7:17

At a high level, we will be seeing how we can go ahead and take the data and explore the different insights from our data.

7:28

from our data and how do we go back and use our data to basically tell a story.

7:33

This is storytelling with data is what we are exploring in the session broadly.

7:39

And the big picture idea that we have discussed so far, if you see, we are coming to the session after SQL,

7:46

and just to clarify the big picture idea, whatever we have seen, whatever we have discussed so far,

7:52

we have discussed SQL, and in SQL, we have seen how we can kind of

7:57

of take the data and how we can write a query, we can extract the results.

8:03

And now this part of the session is more about how do we visualize the data.

8:08

Whatever results we are getting, how do we understand how good is the quality of our data,

8:13

what are the issues in the data, how do we visualize our data in different, different ways.

8:17

So these are the aspects that we are discussing primarily in this particular leg of the session.

8:22

So inspects the data is the most important part.

8:25

And there is a term that we use called EDA.

8:28

Like EDA, what is the, what is the full form of the term EDA?

8:32

EDA stands for exploratory data analysis.

8:36

That means we are trying to explore the data.

8:39

You guys have already seen a little bit of Pandas in your last session.

8:43

I think after that we started SQL.

8:45

So you would have taken a data frame, you would have done a group buy, value counts,

8:51

sort of both functions, you have seen that conversation.

8:53

So we will extend that conversation.

8:54

We're going to be working with Pandas only. And only differences, yes, we will see some different aspects of the data, explore the different aspects of our data.

9:06

And most importantly, the core objective of the session is to visualize our data.

9:11

How do we use Matplotlib? How do we use plot? And how do we use these libraries to visualize our data in different ways?

9:18

Basic visualizations we look at now. This is a continuing session.

9:23

you know, Wednesday also we are having a continuing plus of this, where we'll continue the conversation, whatever we are having, all the way to Wednesday also.

9:32

Okay. Now, so these are, in case you're wondering, sir, what is Matt Plotlib and what is Plotley?

9:39

What is Matplotlib and what is Plotley? These are both Python libraries.

9:43

Now, as we'll demo as usual, I'll share a Jupyter notebook with you.

9:48

Here we demos are both data visualization libraries that you have.

9:53

You have a data frame that.

9:55

That data frame, how you will visualize you?

9:57

Right?

9:58

You, you are line chart, how are bar chart how can make?

10:01

How are you?

10:02

I'm sure some of you can relate to it.

10:06

But in case you don't know, I'll discuss it.

10:08

I'll talk about what is the line, what is the bar, what is the scatter.

10:11

So I'll give me the introduction to that entire piece.

10:13

So Matt Plotlip is a very basic visualization library in Python.

10:18

And Plotley is a slightly more advanced library that we have.

10:22

that we have in Python for building visuals, dashboards, and all that.

10:26

We will discuss that also.

10:29

So kind of a light session, but then generally speaking,

10:33

we'll see a lot of demos, a lot of case studies, as always as I try to do in my classes,

10:38

not just a theory, but I'll try to incorporate a lot of demos and case studies with all of you as we go along.

10:43

That's the big picture idea of how we will face the class, okay?

10:47

Akshut, the session folder remains the same.

10:51

So this is the main cohort 2603 that I've already shared with you.

10:57

So please, you know, access the main link and everything is there in the main link.

11:02

Okay, so it's all, it's all there.

11:04

So I'm grouping the session dates by session dates.

11:08

So today we are in 4th of May.

11:10

A 4th of May, go.

11:11

You will broadly cover this particular slides and we'll cover this particular

11:16

Jupiter notebook IP by NB file.

11:18

I've already shared this with all of you.

11:20

People can use.

11:21

it and you can follow along with me, okay?

11:24

But I will highly recommend in the class you please follow what I'm doing.

11:28

So that up connect Kharpao.

11:30

Don't run the demos.

11:31

It's very simple.

11:32

Connect the concept is where I'll focus on more in the class.

11:35

Demo stock is very easy.

11:36

Once the ideas are clear, you will see the notebook is very simple.

11:39

But I'll walk you through the entire notebook and more.

11:41

Beyond, we'll see some other reference data sets and all that we'll see.

11:45

Right.

11:46

So let's move on.

11:50

Let's start on.

11:51

So first things, first, what we will do.

11:53

We will be taking the data.

11:57

We'll be reading the data from a data frame.

11:59

If you see the top of the funnel, top of the funnel

12:01

top of the funnel in the dirty data.

12:03

You have one thing has

12:05

that whatever data that we are getting from the source,

12:09

the data is usually in a very raw and dirty format.

12:14

That data in many problems are usually.

12:16

And that problems I'm how investigate

12:19

we use a method called.

12:20

We use a method called.

12:21

dot info.

12:22

You know, when Pandas did the first thing you

12:25

you do,

12:26

you do data in data frame in load

12:28

and

12:29

the other thing you do something called dot head.

12:32

Dot head is used to see the top five rows.

12:35

Next, what you do,

12:36

dot info.

12:37

Dot info you can see

12:39

what data is,

12:40

what columns,

12:41

data types are

12:43

integer or float

12:45

or string or

12:48

or bullion

12:49

or bullion

12:51

You can use the info method for it, right?

12:53

You've seen it all.

12:54

Next, take a very important method

12:56

out here, describe method,

12:57

where from where we

12:58

know what data's mean,

12:59

what is,

13:00

median,

13:01

null values,

13:03

you know, right?

13:04

Data in missing values are.

13:06

Any values, you would have done this

13:09

in your Pandas module,

13:10

is NA,

13:11

how we check for NANS in Panda's data frame.

13:12

And third

13:17

is where we can do fill in it.

13:19

If there is,

13:20

if it is to handle it,

13:21

So, this is broadly what we are trying to do.

13:26

We are trying to take the raw data from here.

13:29

We're going to analyze

13:30

we'll,

13:31

data to what problem is it,

13:33

we'll clean

13:34

and we'll not do.

13:36

There are many things here.

13:37

Today we will only learn, I would say,

13:39

1% or 2% of the techniques.

13:41

There's more that will follow as we go along.

13:43

But we will clean the data at a very basic level.

13:45

And then we'll go and then

13:46

we'll plot

13:47

and then we'll plot to.

13:48

So this is your raw data.

13:49

This data in a lot of mistakes

13:50

there are many mistakes will

13:52

be in the data.

13:53

We'll investigate the data,

13:55

we'll analyze the data,

13:56

the data in the data in the problems

13:57

and then we'll both resolve

13:58

and then

13:59

then we'll make charts

14:00

line chart, bar chart.

14:02

This is the big picture idea of how we will

14:04

proceed now.

14:06

And this entire thing is what is called

14:08

EDA. Exploratory data analysis.

14:11

I hope the concept is absolutely clear.

14:14

Now,

14:16

so first let us go and use these

14:19

methods on our data frame, okay?

14:23

So let me go back to my notebook.

14:25

Let me quickly go back to my notebook here.

14:28

Demo. IP by NB.

14:31

I've already shared that.

14:33

Guys, one thing I request you,

14:35

now drive link bookmark to

14:37

every class, you have

14:39

drive link right?

14:40

Just just bookmark the drive link,

14:42

you know?

14:43

Neither we will have to share it every session.

14:46

So please go to copy link

14:48

and you can.

14:49

just keep it bookmarked, okay?

14:51

And I think Prath can also share that all of you.

14:55

So you can all like keep it bookmarked.

14:57

Okay.

14:58

Yeah, I'm also bookmarked.

15:00

Yeah, yeah.

15:02

Sure, sure.

15:04

So I will just go ahead and continue with this notebook.

15:10

We are in session 12 today.

15:13

Exploratory data analysis.

15:14

This was the full form I used, guys.

15:16

So this is a simple acronym.

15:18

acronym. Sometimes, you know, data scientists, we use the term called EDA.

15:22

So EDA what we say,

15:23

exploratory data analysis.

15:25

I mean, I'm going to explore them.

15:26

This is very deep.

15:28

You know, let's not make any mistake.

15:30

This is extremely deep.

15:31

And what we have tried to cover in the course is

15:34

at a limited level, because

15:36

again, our core focus agentic AI is.

15:39

So I don't want to tell you that

15:41

I'm trying to make all of you

15:43

advanced data scientists in this one class.

15:44

No, that is not the expectation.

15:46

The expectation is that expectation is that

15:47

is that we have basic things

15:49

so that everybody knows

15:51

that, yeah, this is an entire universe.

15:54

I just wanted to let you know, okay?

15:56

So, now, let's move on.

16:00

So first I'm importing the necessary packages,

16:03

import Pandas, import NAMPai,

16:05

import MAD plot lip, these are all the necessary packages.

16:09

And this are our two new packages

16:11

which you have,

16:12

you have definitely seen NAMPY PANDAS which I know.

16:14

You have definitely seen NAMPY PANDAS which I know.

16:16

You have sessions of this.

16:18

But these are two very new things for you.

16:20

These are both visualization libraries in Python.

16:22

Matplotlib or plotly.

16:25

Let's go.

16:26

First, we will take a sample data set.

16:29

So what we have here here a sample data set

16:31

called data underscore retail.

16:33

Now, there are several ways to load data.

16:36

Now here I'm taking a sample data.

16:39

But you guys have done case studies before.

16:41

You can normally

16:43

asa-be-loader-c-c-cars-c-cd-cd-cd

16:45

underscore CSV.

16:46

Now read CSV can read CSV.

16:47

You can't.

16:48

You can't any data to load

16:49

there is no problem.

16:50

And we will see more of these demos as we get deeper into the machine learning sessions.

16:54

When we're machine learning in the machine learning in

16:56

so we're using real data use.

16:58

But for now, since this is the introductory session, we will use some sample mock data.

17:03

Okay?

17:04

So I'm creating a simple retail data set,

17:07

where month column, sales column, marketing, spend and category.

17:10

These are the three columns that we have right now.

17:14

And I wanted to quickly show you.

17:15

you what the data looks like for a minute, okay?

17:17

If you want to see, our data underscore retail, it looks somewhat like this.

17:21

This is what my data frame looks like. Just one second.

17:24

There goes my data underscore detail. If you see, we can just display the dataset.

17:31

If you just display, or if you look at the top five rows of your data, that's how my data frame will look like.

17:38

So, sorry, let me just show you the top five rows of your data.

17:44

data underscore retail and we can just show you the top five rows what the what the top five rows of our data frame actually are.

17:52

So this way you can you should be able to see what the what the top five rows of our data actually are.

18:00

Okay. So now the thing is if you look at it intuitively, what kind of data do we have right now?

18:07

Month sales, marketing, spend category, straightforward, right?

18:11

So month a column is, sales, a column.

18:14

So for every month, we are able to track how much sales happened, and we are also tracking how much marketing spend happened, and for which category.

18:22

So understanding of the data is the key.

18:24

That's the first thing I want to start my session with.

18:26

When you're all the first you're doing,

18:29

first you know, what kind of data are we working?

18:32

So what is the meaning of the data?

18:35

What is the meaning of each and every row?

18:37

Every row is what is the meaning of each and every row?

18:38

Every row is what is.

18:40

This January data is,

18:42

In electronics category, you have marketing spend this, and your overall sales is $12,000.

18:48

Marketing spending the company in that month in marketing in the marketing in

18:52

Now, marketing there are many of the banners, social media advertisement,

18:56

Google's ads are very expensive.

18:59

You have to buy credits from Google, YouTube ads,

19:03

news paper ads, TV advertisement, or anything.

19:07

There are many, or then marketing spend, a marketing team maybe.

19:11

team, you're hiring a marketing team, giving them some credits.

19:14

All these are part of marketing expenses.

19:17

So January, the company has spent in marketing, but,

19:20

sales it was.

19:21

Okay?

19:22

In March, this is what we are tracking.

19:25

This is the meaning of our data.

19:27

So, understanding is important.

19:30

Data is what is?

19:32

What data is?

19:33

If you're not, then what do we do?

19:35

All these concepts are useless.

19:37

Look, guys, you know,

19:39

you understand, you know, like pandas you have.

19:41

I'll give a simple example.

19:43

You have learned all of Icon, you have learned all pandas,

19:46

you have all of pandas,

19:47

you'll all of all of all these things.

19:49

Now, let me, we'll make basketball data,

19:51

or baseball data think.

19:53

And you'll be surprised to know,

19:55

you'll be surprised to know,

19:57

baseball is one of those, this one,

20:01

one of those games,

20:05

which, you know, which, you know, which,

20:09

which is one of the earliest, like, a lot of data science has been inspired by, by baseball, you know.

20:14

A large part of data science that we do is inspired by,

20:18

was originally inspired by baseball.

20:22

So,

20:23

there are basically, I'm not able to recall.

20:26

There's a, there's a very famous movie.

20:29

Actually, as I'm talking to, I'm trying to recall.

20:32

What is the name of that movie?

20:33

There was a name of a movie where this coach joined, you know, a particular baseball team.

20:39

and then they transform the fortune.

20:42

So they were they're actually, like, looking at the numbers and then they decide

20:48

they're going to, who player, where he'll select.

20:51

It was a complete underdog team.

20:53

Like, you have an underdog, right, BJP was like an underdog in Bengal.

20:58

But they won.

20:59

So you're using data analytics to figure out that, okay, I think this person will do well here,

21:04

this person will do well here.

21:06

So they are also using a lot of data science to do it, right?

21:08

do it. So, now it's used everywhere, right? But this was actually a very nice, baseball is one of those games, you know, where I would say a lot of data, data science was used or in the way.

21:20

So, now, I think it's name. The movie's name is actually called Moneyball. Okay? You can see this movie. I think you'll be inspired by this a lot.

21:29

Now, you can see 2,000 Rihara movie is. Brad Pitt is the lead actor and this is based on a true story. And you can see, it's one of the

21:38

it's very, very popular. Abake set you, Rotten Tomatoes in 94%

21:42

too, very nice, very inspiring movie, given that you guys are, you know, doing this journey

21:47

on data and then AI and all that. So, so here here he's described here.

21:53

You're using data science and analytics to change the fortunes of a team.

21:58

Now, why am I talking about this? Why am I talking about this?

22:01

Now, now, it's all the way to, all the teams, Rajasthan Royals may,

22:08

Royal Challenger, Calcutta Night Riders. Every team has their own analysts who are doing something

22:14

very, very similar. They're also using Python, they're using other tools, visualization tools

22:18

to look at player performance, figuring out who can hire, who's auctioned, how

22:23

pay how much money, so everything. All right now again, why am I talking about this related to

22:29

my discussion? The reason I'm talking about this is because if you have a baseball

22:33

if you don't even know the game of baseball, then what you don't even know the game of baseball or

22:38

all of the Python that you learn, it's useless. You cannot do anything. So that's why I'm saying

22:46

it, you know, it looks like a, it looks like a very simple data frame. But what I'm again

22:51

stressing on is, you know, data to say by data, what is, what is this, yeah, this, you're

22:56

simple like advertising data, I've explained to you, but if I give you a baseball data, honestly, I also

23:01

don't know baseball much, okay, a baseball in baseball, what do you call it, what do you call it,

23:06

home run, whatever, there are many rules in the game. I always, I'm, I'm, I'm, I'm, I'm, I'm, I'm, I'm, I'm, I'm,

23:08

I also don't know personally baseball, okay? I don't know the game. I don't know the game.

23:11

But domain knowledge is very important. If you give me a baseball data, for all my data science

23:16

knowledge and all the engagements I've done, everything I know, but I will still be very unsuccessful.

23:21

Because I'm a game kind of not. We don't know. We don't know, that you know, that columns use

23:25

to use, as a visual source can. So this is the first thing I wanted to plan. So having domain

23:31

knowledge is very important. And next time, you know, if I relate it to your interview and your job and your

23:37

career. Next time you're interviewing for a company in a similar kind of a data role, be very,

23:42

very good with the company business. The company, what are they doing? Tools to say everybody will

23:48

learn the concepts. Everybody will learn the topics one bill. But can you really apply these in the company

23:55

business? Make example. Let's say you're, you're interviewing for American Express. Yeah, visa, master card,

24:02

credit card company, or then you're in the, you're interviewing for, uh, uh, uh, you're interviewing for, uh,

24:07

angel broking, you know, some investment bank or equity research,

24:10

you're, you're, and you're interviewing for a data science or a data analyst position.

24:17

Whatever, I'm just giving an example.

24:19

Now, you're going to expect not

24:22

that you, he will ask you what pundas, what is, missing value, how to handle?

24:25

They will not ask you general questions.

24:27

They will give you problems from their field of work.

24:31

You have a stock market data, Nifty, last week, closing returns, they'll,

24:36

and you're from there from here, here here here,

24:39

this percentage, what are you?

24:41

So if you, if you know, if you're, if you can't tell them,

24:46

that, sir, I know this is missing value.

24:48

We're here here, you know, you're missing what, but

24:50

there missing can't, what is?

24:52

If you've never markets, not seen, stock markets,

24:55

then you cannot do anything.

24:57

So domain knowledge is very important.

24:58

And this is something nobody can teach you.

25:00

We are trying to teach you the ideas, but

25:02

something I'm encouraging to, as you are going through the course.

25:06

get into the habit.

25:08

Perthageo, telecom for you, finance for you,

25:10

health care, for you understand what is going on in the industry.

25:14

Okay, you study a little bit about finance.

25:18

So if you're interviewing for a master card or a visa or American Express,

25:22

you guys know that American Express in credit card network

25:25

when I swipe my card merchant machine, how the payment network is happening.

25:31

So just a general thing I wanted to clarify them.

25:34

Now, so back to our problem statement.

25:36

This is our data set.

25:37

So, then we look at the top five rows.

25:41

This thing you have all done.

25:42

So I'm not repeating the same story again.

25:44

So this is data.

25:45

Dot head.

25:46

Dot info.

25:47

What you'll know what

25:48

what is the information about the columns?

25:53

So you've got total four columns right now,

25:55

month, sales, marketing, spend, category.

25:57

And you can see what is the data type of each and every column.

26:00

So this is object type,

26:01

meaning string type data, categorical data.

26:04

This is a numerical type.

26:05

This is numerical type.

26:07

This is the result of the info method.

26:12

Info method.

26:13

Next step, we do a missing value count.

26:18

So missing value count, so kind of care,

26:19

up here from here from here.

26:21

If you can here here, we can clearly see

26:24

we can clearly see that the sales value has nine non-null values.

26:29

All these other columns have 10 non-null values.

26:32

The sales column has nine non-null values.

26:34

So, I mean, one missing is.

26:37

Okay?

26:37

But there's a N.A value,

26:38

which we have here here can't a number.

26:42

NAN is a missing type in Python.

26:45

All of you know that, right?

26:47

Or if you know that's in Pantas

26:47

may have, so here clearly we see it.

26:49

Non-Nal.

26:51

Okay?

26:51

Now,

26:52

uh,

26:54

now, uh, uh,

26:54

the question is,

26:55

sir,

26:55

care what do you expect us to do?

26:57

So what do you expect us to do?

27:00

This is again a long conversation, but for today,

27:02

uh, I will discuss with you two.

27:04

approaches, okay?

27:05

Two approaches.

27:07

So, the first, this sales is,

27:08

this is missing, right?

27:10

So when you do info, you know,

27:10

you know, you know,

27:11

you know, you know,

27:11

that you're missing

27:12

here.

27:13

Now, you're

27:13

what are you

27:14

here?

27:15

Number one, you can go back

27:17

and you can,

27:18

uh,

27:20

you can, uh, you

27:20

you can, uh,

27:20

you know,

27:21

now,

27:22

first thing,

27:23

that sales missing

27:23

because if

27:24

if the company

27:25

April's data

27:26

there,

27:26

then, then why is it that is missing?

27:30

They can be any number of reasons.

27:32

Uh,

27:33

one of the reasons could be that,

27:34

let's say, you know,

27:35

the company has published their,

27:37

their reports in a delayed manner.

27:40

That could be one reason.

27:42

Company has published their reports in a delayed manner.

27:44

Delayed reporting has.

27:46

So at the point at which you are kind of

27:51

collecting the data, the sales for that particular month is missing.

27:55

So that missing are.

27:56

If sales missing,

27:57

then you have this data roll

27:58

and this is only five rows, right?

28:02

If you look at the complete data,

28:04

let me show you, this is my D.F. Sains, right?

28:08

This, if we just do this,

28:15

DF sales, if we print

28:16

then, it's okay,

28:17

that's okay,

28:18

one is missing.

28:19

Baki January to October from,

28:20

is there.

28:21

No, no problem there.

28:22

So now you have to take a call

28:23

that should I proceed with this data.

28:25

No, so we have to remove the room.

28:27

See, one of the thumb rules that I use

28:29

and what enterprises usually use is,

28:33

if your data missing,

28:34

there are other methods which we will also discuss in due course of time.

28:41

But there is a very common terminology that we use in the industry, which is called,

28:49

we're type here here.

28:50

It's called garbage in garbage out.

28:53

But if your data is bad, you know, if your data is bad,

28:58

whatever you do using that data will also come out to be bad.

29:02

So if you're, if you have.

29:04

bad data, I mean, this is bad data.

29:06

Now, if we're looking, if we go and proceed along with, you know, this particular data,

29:14

so the,

29:15

the other than analytics we're going, that's one thing to keep in mind.

29:21

So garbage in garbage out.

29:22

Please keep that at the back of your mind, okay?

29:25

So Nan is effectively a good example of, like, this is a good example of that thing.

29:30

So simple approach, please remove that rule.

29:32

Number one.

29:34

Number two, what can do?

29:38

The simplest way you can handle the missing value is to replace with the average.

29:43

It's not the most accurate way. Mind you, we are guessing.

29:47

Or this go on what, what we say? Let me take my marker pen.

29:50

Just once again. I'll just take my marker pen for you.

29:53

We call it, we call it imputation.

29:57

We call it missing value.

30:04

imputation. So we can go back and impute that with a missing value.

30:09

We can impute the missing value. So simplest way is to go and remove the missing value.

30:14

If you don't want to remove, if you're looking, sir, nine rows are 10 rows.

30:18

Then we are removing a lot of data actually. I would still say the best option is to remove

30:24

it. Please remove it. That's the best practice. For all the things that we talk about, best

30:28

practice, work with clean data. Even if it's less data, it's okay. But it's actually clean data.

30:33

number one, remove it. Number two, just for teaching the technique, we can impute with a

30:38

mean. So here here, you're here, you what you're going?

30:42

NAN to hathed. Nan can't do. NAN key other than the rest of the main

30:46

make out the average of the rest of the records. Find out the average and then impute this with

30:52

the average. That's the way how you will have to work towards it. So for all the remaining

30:57

sales values that you have right now, please find out what is the average and then, you know,

31:01

impute with.

31:03

respect to the average. So that's the way how we, how we go back and work towards it.

31:07

Now, average how you know, you know, you know, dot mean, you can do is dot describe.

31:13

Right, so dot describe, if you're, if you're going, this dot head o'gia, dot info, we've described

31:17

here, dot info, dot head, dot info, and this is over here. So here here, your summary statistics

31:23

are jacques. So very important, this will give you. So, uh, so, all that I'm saying,

31:30

Akshar, just to repeat once again for you, what I'm saying.

31:33

saying, uh, so what I'm saying is you can, you can impute this value, right? So do, do options

31:42

there. First option is to drop, drop the value. Apuro rhoda do the whole. That

31:48

all problem is solved. Okay. Number one. Number two, you impute the missing sales value.

32:03

with an average.

32:06

You, you impute the missing sales value with an average.

32:12

And what is the meaning of impute? Impute means substitute.

32:17

Impute can mutle.

32:18

That is the meaning of impute. Impute means substitute.

32:22

That is the meaning of impute.

32:23

Impute means substitute.

32:24

That you want, that you, that you, that you want to substitute that particular missing value with the average.

32:31

Now, Akshad, average, average, how to calculate?

32:33

average is basically nothing but you take all these sales values right and you find

32:38

out what is the average of all these sales values you take all these sales values right now

32:43

and you please calculate what is the average across all these sales values what is the average

32:48

find it out and you simply replace this nan with the average so this will give you a a good

32:56

estimation that okay i don't know exactly what the sales for that particular month of april is but

33:01

at least second guess

33:03

that in the whole year average it is, so maybe sales in April maybe around that value

33:08

was okay.

33:10

Aksha Dario clear.

33:11

Please let me know.

33:15

And its, its, what is the way how we do it?

33:17

We use something called fill in a.

33:19

We use something called fill in a.

33:23

So,

33:23

head method got, info,

33:26

and described

33:28

if you describe,

33:29

if you describe,

33:30

if you describe, then here here mean

33:31

mean came a $21,000.

33:33

21,000 is my mean right now.

33:35

And all that I'm doing right now, if you look at the code, what is the code I've written?

33:40

DF sales dot fill N.A with the mean.

33:44

So I'm filling the missing value with the mean.

33:45

This is the code where I'm doing that.

33:48

Okay, you can't see.

33:49

You can you?

33:50

We will fill it with the average sales to maintain the trend.

33:55

Data missing, so what will?

33:57

If you're going to, if it's a data missing is,

33:59

so you please fill that sales value.

34:01

dot fill N.A.

34:02

Phil NA is the Fonda's function.

34:04

You might have seen this in your Pandas probably.

34:06

So fill NA is the Pandas function.

34:08

Where any NAA will,

34:09

we want to replace those NAs with the average.

34:13

This is your simple syntax.

34:15

So you'll you,

34:16

so your final data will,

34:17

that's there will be

34:17

missing not.

34:19

Okay?

34:21

So we'll run

34:21

let me run the code and show you

34:24

what is DF dot DF sales right now.

34:26

You have DF save,

34:27

we'll see.

34:28

Guys, remember,

34:29

here April's missing was right?

34:31

Please remember, April had a missing value right now.

34:33

April in NAN.

34:35

April had NAN.

34:37

So before April had NAN.

34:38

And after I imputed, if I run DF sales again,

34:42

here we run it.

34:43

Now, look, April's impute had two years.

34:46

This is the imputation or substitution.

34:49

This is the simple concept I wanted to highlight to you.

34:52

Now, one more thing I want to talk about.

34:55

Here here two different data.

34:58

Numeric data have and we also have categorical data.

35:01

Numeric data is sales, marketing spent.

35:04

These are all numbers, right?

35:05

So if numeric data,

35:07

it's, you can, you can't

35:09

make, minimum, minimum,

35:12

but if there's

35:14

a categorical data,

35:15

categorical data,

35:16

I mean,

35:17

object type data.

35:18

When you're Fandaas

35:19

in dot info

35:19

you, that object type data

35:21

is right?

35:21

Here on, I mean, I'm sure you have seen

35:23

these kinds of things, right?

35:25

So when you go and do something called

35:27

dot info,

35:29

when you do dot info,

35:30

what you actually see on the screen is

35:32

the entire description of the columns.

35:37

Okay?

35:37

So this is the

35:39

other term we use

35:40

we call it metadata.

35:42

Metadata,

35:42

what is the structure of my data?

35:45

That is the inference that you're able to get.

35:48

So for these object type columns,

35:50

if we're investigate

35:50

to do,

35:51

then what are we can't?

35:53

we can't make maximum minimum

35:54

because they are not numbers, right?

35:57

So we cannot apply simple

35:58

numeric operations on this

36:00

on this particular type of data.

36:02

We cannot apply numeric functions.

36:04

So for this we have to apply

36:05

something called value counts.

36:08

So what we do is we do something

36:09

called value counts.

36:11

We do something called

36:12

value counts and value counts use

36:13

and we look at, okay, group by

36:16

category and tell me how many

36:17

instances we have for those

36:22

categories.

36:23

So this is a kind of syntax

36:26

which I'm sure you have already seen in Pandas.

36:28

So category

36:29

you have a column and when you do

36:31

DF category dot

36:33

value counts, what do you get?

36:35

You end up getting something like this.

36:38

Something like this.

36:39

Where you can see, okay, electronics

36:41

are 4th, apparel in

36:43

4, and furniture in 2.

36:45

Okay, this is the intuition.

36:46

So what we are discussing right now is

36:48

numbers how to analyze

36:49

analyze? Averages and

36:51

maximum, minimum, like that.

36:54

And categories

36:55

how analyze?

36:57

Categories, you can't, you can't

36:57

you can't say electronics plus apparel average

37:02

average.

37:02

So there we try to find out

37:04

that's the way how we work towards it.

37:06

That's the way how we work towards it.

37:08

Now, now from here, let us get to the next phase of our session,

37:13

which is Matt Plot Lift.

37:14

We will start plotting some charts.

37:16

Here, most of the Pandas things you have already seen

37:18

at a basic level.

37:19

So it was just a very small kind of a recap.

37:22

Now the main thing that we will get into

37:23

is charts, visualizations, okay?

37:26

How do we visualize our data?

37:27

So back to the same data frame, back to the same sales data frame.

37:33

I will just load my DF underscore sales here.

37:38

Again, when you start with data visualization,

37:40

whatever I have discussed initially, that remains true here also.

37:44

You have to understand what your data refers to.

37:48

What is the meaning of your data?

37:50

Every month, sales, say, marketing spend,

37:52

category, you need to understand your data very well.

37:55

Okay?

37:56

And here we will learn about two,

37:57

specific types of charts. First, we will use something called the line chart. And second,

38:02

we will be using something called the bar chart. So these are two different types of charts and

38:06

visualizations will be, we'll be discussing.

38:10

So just to summarize the conversation, this is a very nice visual where I wanted to summarize what

38:14

we talked about. So you read kiyah, you, you know, shape, data structure sumja, dot head. And then these

38:21

are the three, four things we talked about in four. And this is what I told you. This is the main

38:25

difference between numerical data and cat.

38:27

categorical data. If you have a numerical data, like sales, then you

38:32

all you can you see? This is a minimum 59.9. It's a maximum 120.50.50.

38:38

0. You can see that. If the column is a number, you can get these metrics.

38:43

But if column is category, if category is, you, you know,

38:46

what's maximum? You have three values are. You, tell me, what maximum? You, how can you? There's

38:52

nothing called maximum. There's nothing called average.

38:54

So what we do? That we do, what we're doing. This for, this we're

38:57

categorical columns for. Okay. Just keep this at the back of your mind. We find out

39:03

counts for categorical columns. Now, moving our prince. So now we will get a little deeper

39:09

into, into another very interesting concept, which is called an outlier. So a term use

39:16

and this particular term is called an outlier. So what is an outlier? So what is an outlier?

39:20

outlier is basically a data point that is very different from the rest of the

39:27

fact.

39:29

That we're outlier. So I'll give an example to you. Let's say you are looking at salaries of

39:36

we are looking at salaries of 100 people in the company.

39:42

Our company is. Your company is employees. And we are looking at

39:47

salaries of 100 people in the company.

39:50

Now, the, I mean, most sattaki, some people are making a lot of money and some people are

40:02

comparatively making very less amount of money.

40:06

Some people who are making a lot of money and some people are making, most are making a certain

40:11

amount of money and some people are making a lot of money.

40:15

Okay. So that, those data points are what we refer to as outliers.

40:20

Okay.

40:20

So it's related, what I will do now, here the concept that is a specific concept that I'm

40:27

getting into right now with all of you. We are getting into a specific kind of concept called

40:31

skewness. So what I am getting at, what I'm getting at right now is a very specific kind of concept

40:37

called skewness at a very high level. It is not a very difficult thing. Don't be, don't be intimidated.

40:44

It's not difficult at all. So I'm going to use a couple of my notes right now. Just allow me one

40:49

minute, guys. I will just quickly pull up a couple of my notes right now.

41:00

So we're what kind of, we're doing, some, we're saying you,

41:03

what we're making, you, we'll make it, so that it's easy, right? Not everything will be just

41:07

slides and notebooks, but a lot of the times what I do is I actually put effort to create some, you

41:13

know, interesting stuff for you guys. So here it goes. You can see a small example right now. So

41:19

So, yeah, SQL. No, no, no, no, no. SQL is totally a different thing. SQL says, we are back to Python world. SQL was just two classes. That's it. SQL is just an introductory thing we wanted to give you. How do you connect to a database? How do you write a select query? That's it. So we are back to the Python world. So we are back to the Python world and for the rest of the journey, you will only see Python. And I will tell you a little while later,

41:49

then what connect? If you're

41:50

if you're saying that you're saying, sir, SQL and Python

41:52

connect to, that we'll, we'll look as we go along. But

41:56

Matt plot leave is nothing to do with SQL. Okay. Okay. Okay. You see. Uh, sorry,

42:04

uh, what's your, what's your name? Gourthage, right? But how do I, how do I spell your name?

42:09

Uh, because you know the email ID is come like,

42:13

please use your proper names on Zoom so that I can address you properly. Okay.

42:17

Okay, please use your proper names on Zoom, right? Gurtheg, yeah, so Gurtig, so Gurtig,

42:23

just to answer your question, okay, so Gourteg just to answer your question, SQL is basically

42:30

whatever we have seen, SQL is not a data visualization tool.

42:35

There you have data to visualize not. So we'll, we'll come and we'll, we'll go

42:38

many things are, we're, we'll, we'll, we'll, we'll, um, um, um, um, um, um, um, we're beautiful charts

42:41

and these stuff, that's your question. Okay, okay? SQL is not meant for this.

42:47

SQ will is just meant for retrieving data in a tabular format.

42:51

That's it.

42:52

SQ will map.

42:52

You can't just to clarify.

42:55

Okay.

42:56

Let's let me come to the concept.

42:59

The concept is a little bit more interesting.

43:02

But it's just a little time will be.

43:04

The concept will be around like

43:06

around five minutes or so,

43:08

five to ten minutes of concept.

43:10

You have concept,

43:11

you know, code is one line.

43:13

Code in case.

43:14

Once the concept is clear.

43:16

So we are basically discussing

43:17

something called writes to distribution. And we are specifically discussing a topic called

43:22

a histogram.

43:24

This histogram what is a histogram?

43:27

Let's understand that face.

43:29

So I'm going to go off screen for a while because you don't want to see me.

43:33

I don't want to distract you by, you know, showing my face all the time.

43:36

Let's get back to the content.

43:37

Okay.

43:38

Now, let's see this.

43:40

So 3.3.3.

43:42

So the first, up upar what is we have the salaries, right?

43:45

One second.

43:46

I think.

43:46

So we have salaries of 15 people in the company.

43:55

So what you have on the screen right now are salaries of 15 people in the company.

44:00

And these salaries are 333-34-7-99-13-14-14-19.

44:06

So these are the salaries of 15 people in the company.

44:10

These are the salaries of overall, excuse me, 15 people in the company.

44:16

But I can see you guys that most of the, and this is typically the structure of any

44:21

IT company, right?

44:23

I'm sure at the end of the force, all if you are targeting to join an IT company or at least

44:27

a technology-oriented road, then you're going to go and you are all trying to become

44:31

Gen-AI, agentic experts and you want to work in some technology company,

44:35

where you have this is typically the structure.

44:38

Most people are, will be at a junior level, making around like not, not three, obviously.

44:42

You guys, I'm surely be targeting higher roles.

44:45

But let's just say.

44:46

average will be something around 5, 6, 7.

44:49

And then there will be some CEO who will be making like 50, 60.

44:52

So outlier here.

44:54

Let's say this person will be your manager.

44:57

Eunice lakh is the person salary annually, a lot of money, right?

45:02

So at least at a junior level, that's a lot of money.

45:05

But there is no limit to how much you can earn.

45:08

So on this luck is like a huge amount of money in Indian salary.

45:12

But I work in Qatar.

45:12

So if you're earning 19, 19, 19, lakhs in middle.

45:16

least, you are actually poor.

45:19

19 lakhs annually in Qatar and Middle East, Dubai is actually, you're a poor person there.

45:24

Quite literally, you're a poor person if you're making this amount of money.

45:29

Anyways, so now, yeah, outlier is, this is basically an outlier that you're able to see on the

45:35

screen.

45:37

So, now we're what we want to understand the distribution of our data.

45:44

Right?

45:45

We are.

45:46

We are trying to understand what is the distribution of data.

45:50

333344799 13, 13, 14, 14, 19.

45:57

We are trying to understand what is the distribution of the data.

46:00

So how can we're going to try to look at the distribution of our salaries.

46:09

So left-in-side in, we are going to try to look at the distribution of our salaries.

46:10

So left-hand side, we're going to bings in divide.

46:14

So 0 to 5, there are how many people, 7 people?

46:16

6 to 10, there are how many people, 4 people, 11 to 15, there are 3 people, and 16 to 20,

46:23

there is 1 person.

46:25

Okay?

46:26

So, 0 to 5, 7 people, 6 to 10, 4 people.

46:32

Now, you'll ask, sir, this, how are you?

46:34

So you can take a look at it.

46:36

Now, look, look, see, 0 to 5 in how many people are there?

46:40

3, 3, 3, 3, 3, 4, 4, 4.

46:42

7 are in, 0 to 5 bucket in.

46:43

I mean, we're at 1,000,000,000, values, okay?

46:46

So 0 to 5 bucket in, that, there are, there are 7 people, right?

46:50

Then, now, now, now, now, see, salary bills, 6 to 10 in 10, in 4 people?

46:55

Simple are, guys.

46:56

11 to 15,000, how many people earn are, 3 people earn, right?

47:00

And 16 to 20, how many people are making?

47:02

One person is making.

47:04

So what have we, what have we done right now?

47:07

What did we?

47:08

We made company in surveyed, all the salary asked,

47:11

people have responded, how much money they are making,

47:14

and we are simply constructed.

47:16

a distribution table, left-hand side, we have a distribution table

47:20

made the whole data, okay?

47:22

We have built a distribution table of the whole data,

47:26

where I'm trying to demonstrate to you how much,

47:29

how many people are earning those amounts of money.

47:33

We have a count just.

47:35

If we, if we'll give you an analogy,

47:39

like we have value counts,

47:41

some time back we have value counts,

47:43

we have done, you have pander's made,

47:44

categorical column for, we have,

47:45

column for we were finding, that how

47:47

electronics is, how this category,

47:49

value pounds.

47:50

This is a similar kind of count we are doing.

47:53

Okay, simple.

47:55

Now, all that we are trying to do is

47:57

we are trying to visualize this data on the right-hand side.

48:01

This is your histogram.

48:03

I know,

48:05

some first, many of you will be probably looking at this diagram

48:09

and telling me, sir, this bar chart is.

48:11

The first thing, people will probably think it's a bar chart.

48:14

But let me say,

48:15

plan on. We'll also

48:16

we talk about.

48:17

So, what have I done here?

48:19

What have I done here?

48:21

I have actually gone ahead and created,

48:26

we have created something called,

48:28

something called univariate analysis.

48:31

Univariate analysis.

48:36

Univariate analysis.

48:39

And univariate is what is what

48:41

you?

48:42

If you break it,

48:43

uni is one variant is variable.

48:44

is variable. This is analysis of a single numerical variable.

48:50

So univariate is nothing but analysis of a single numerical variable. There is a single variable

48:55

called salary. That is a numerical variable.

48:57

Because salary values of numbers are, right? We have a numerical variable and salary

49:01

of these values numbers. So, so we are trying to understand,

49:06

that what is the distribution of all the values in the salary?

49:13

salary thing, right? So this is what a histogram is.

49:20

Histogram is always a kind of a univariate analysis technique.

49:23

So x-axis is a salary.

49:27

Y-axis is a frequency or a count.

49:30

Y-axis is a frequency or count.

49:32

X-axis is a salary.

49:34

Y-axis-go-gia frequency or count.

49:36

And what you're seeing here is like a kind of a distribution.

49:40

So 0 to 5, there are 7 people.

49:42

Same story.

49:43

6 to 10 there are 4 people, 11 to 15, there are 3 people, and 16 to 20 is 1%.

49:51

I'm pretty sure most of you, in fact, all of you,

49:55

or so you might not have

49:57

because schooling is something we have probably done long back here.

50:01

In my case, it's being more than 20 years, obviously,

50:03

but many of you are younger, much younger than me, obviously.

50:06

But yeah, you've probably done this in your school days.

50:09

This is like class 7, 8 months.

50:11

There we have similar things.

50:13

Distribution table.

50:14

Histograms we actually in school level.

50:17

So now you ask you, sir,

50:19

we have this Univari-a why say it?

50:21

Because you, you know,

50:22

first when we started the analysis,

50:23

we had a single variable.

50:25

We only had one single variable.

50:28

We are only one single variable for salary.

50:31

You have nothing, there was no,

50:33

account, there were just salary there.

50:36

We have only company's salaries.

50:38

We have just company's salaries.

50:40

All that we have.

50:41

What we did was we took the salary column and we created Binge.

50:45

We made the frequency column for

50:47

made.

50:48

We have additionally a column add here.

50:51

This is something we have created.

50:53

We were in our data not initially.

50:55

Our data was only a single column.

50:57

That is why we call it Univariate Analysis.

51:00

We are this

51:02

we are trying to understand

51:05

what is the distribution of this data.

51:06

We are trying to understand what is the distribution of this data.

51:10

Single variation.

51:11

So we have count

51:13

our end from the frequency

51:15

our end created.

51:16

And coming to the chart,

51:18

x-axis is the bin,

51:20

y-axis is the derived column,

51:22

the column we've made.

51:23

This is your histogram.

51:25

Now you are you

51:27

say, sir, this is bar chart

51:28

like it.

51:29

Now, now,

51:30

we'll tell you,

51:31

bar chart is part of our next discussion.

51:33

But okay,

51:34

now,

51:35

same story if I have to explain bar chart.

51:37

Here is an interesting thing, guys.

51:39

Bar chart is actually by video.

51:40

So we're here.

51:41

Here it's a whole confusing

51:43

but we're going to

51:44

we're here.

51:45

We're here.

51:46

This bar chart is actually

51:49

bi-variable.

51:51

Bar chart is actually bi-variate.

51:55

Bar chart is bi-variate.

51:58

It's

52:01

two variables involved here.

52:04

If we're a simple example

52:05

for a bar chart,

52:07

a very good example would be exactly the use case

52:09

we are doing today.

52:10

Now you,

52:11

You have category, right?

52:13

You have category a column.

52:15

You have sales a column.

52:17

These are the two columns you have right now.

52:19

There is a category column, there is a sales column.

52:21

Right? We have a category column.

52:23

We have a sales column.

52:25

And this is the great use case where you can create a bar chart.

52:28

You create a bar chart.

52:29

X axis has your category.

52:31

X axis your category

52:37

and y-axis your sales

52:38

and there is the bar chart that you can go and create.

52:41

This is the bars, individual bars,

52:43

and you can absolutely go ahead and create the bar chart.

52:46

So, your, this is basically your, we can say this is the category of electronics.

52:56

So for different categories you can find out the sales.

52:59

And most importantly, you are able to see there are two variables involved.

53:02

That's why we call it Y variant.

53:04

X axis is a valid variable, which you have you here on,

53:07

and Y axis sales is also a valid variable,

53:09

which you have here here.

53:10

These are two variables that you have right now,

53:12

x-axis and y-axis.

53:14

So this is the biggest difference between histogram and bar chart.

53:18

So sometimes when we look at these two plots, we sometimes get confused.

53:22

This are the same here, right?

53:24

So this looks the same right now.

53:27

But if you try to get a little deeper,

53:30

if you try to get a deeper, you will realize that

53:33

this is not the same, right?

53:36

So when you go a little deeper, you will realize it doesn't look like the same.

53:39

It doesn't look the same.

53:40

the same at all, right? So yeah, this is basically what a bar chart is. So bar chart is by

53:46

variant analysis. There are two variables, okay? And we will see some examples of that

53:52

and and histogram is a uni variant analysis. That's the inference that we are able to,

54:00

we're able to get here overall at a high level.

54:10

Okay. Now,

54:12

coming, everybody's okay, everybody fine. All of you are with me.

54:17

Please let me know with a quick yes on chat.

54:19

All of you, let me know.

54:22

Okay, Akshar is followed, okay.

54:25

Akshah, yeah, just to clarify the answer to that is yes.

54:29

I'll, yeah, just to clarify.

54:31

All of you are okay.

54:32

All of you are okay.

54:33

Can all of you confirm?

54:35

Everyone's following, right?

54:36

So I'm taking a little time on this, because the concept is a little deep.

54:39

sort of deep. So I'll give you some more examples so that people understand this better. But do, do, do let me know if you're all following. Okay.

54:48

Others are all fine. Guys, let me know, please. Please let me know. Okay. Great to see. Great to see all your responses.

55:00

Give me one short example of outlier.

55:04

Okay, Akshad outlier of an example of. Okay. You can. Uh, you. Uh, upro.

55:08

You look at any, any data point that is different from normal.

55:13

Any data that's different from normal, any data that is different from normal is what we call an outlier.

55:20

Okay, so I repeat again, any data point that is different from normal is what is an outlier.

55:27

That's one way to do that it.

55:29

So outliers are basically data points that are different from normal.

55:34

So you take rainfall data data in a particular.

55:37

in a particular place. Every day you take precipitation data, rainfall data. You're

55:42

every day, you're going to every day, millimeter notes. So every day the rainfall is like,

55:48

let's say, 0.1 millimeter, one millimeter. One millimeter. Let's say, I don't know, 50 millimeter. That's

55:55

like an absolute cloudburst, as they call in English, right? Cloudburst means a massive amount of

56:01

rainfall in a short period of time. So, every day, on an average, there's a certain amount of rainfall.

56:07

Now, a, a, there's a huge amount of down port that happens in Bangalore or Bombay, and the whole city is like flooded.

56:15

So that is like an outlier, right?

56:17

So there's a, the value is very high on that particular day.

56:20

Rest of the days, it's all normal.

56:23

Okay, okay. So outliers, high be was up, low be, low be, is.

56:27

And so this is, this is an example of an outlier, which is on the higher side.

56:31

Most people are making money three, four, five, seven. One person is making a tremendous amount of money.

56:37

So, what is, what is the impact of this in the real world?

56:44

So the data will become right skewed.

56:47

If you look at the shape of your data right now, if you look at the shape of your data right now, the shape of your data becomes right skewed.

56:53

This is what will basically happen if your data consists of outliers.

56:58

Okay, if your data consists of significant amount of outliers, your data will become right skewed.

57:03

You have a right skewed data over. So most of the people in the company are making,

57:07

average to less amount of money and few people are making a tremendous amount of money.

57:13

If you look at the shape of the data, this is what we call a right skewed or positively skewed

57:19

distribution.

57:19

This is what we're what we call it right skew kew or positive skew kew. We call it right skew or positive

57:25

skew. That's how we look at it. You just ignore this part, please. But this thing is important.

57:32

Right skew or positive skewed. Why? Because this graph is kind of skewing.

57:37

towards a positive x-axis. So most of the values are average to low. Most people are

57:44

making average to less amount of money. If you have d'a-zero to five, there are seven people.

57:48

I know, uh, uh, uh, six to, uh, 10, there are four people. Most people are in this zone. Most people,

57:53

if you see, are in this zone. You know, most of the people are in this zone, but only one person is in this

57:59

zone. So the graph is right skewed or positively skewed. Right, skew, skew, skew, skew. The term I'm using

58:05

is called skew. Let me write it.

58:07

again for you. Right. Skew. S-KU-W or positive skew. We call it skewness.

58:19

Okay. And we'll, we'll, we're back in how to handle it. Right now, I'm just trying to tell you the

58:25

issues in the data. So, yeah, outline is a problem. How do we handle it is a later topic.

58:30

We'll on machine learning in here. I will discuss with you how to handle it. But right now, we are

58:33

only investigating. Remember, the topic name is exploratory data.

58:37

We're trying to explore the issues in our data.

58:39

Then we will learn some techniques how to handle it.

58:43

Okay, so this is what is meant by Rice Q.

58:47

Now, similarly, there is something called LEPSQ.

58:52

What is LEPSQ?

58:54

Left skew?

58:55

Left skewed data, this is the example I'm taking for all of you.

58:59

Subdek, Saki, I have marks of students in an examination.

59:06

So I basically have marks of students in an examination right now.

59:13

So imagine I'll just use the red color.

59:19

This is the marks of students in an exam that we are tracking.

59:22

And you can see most of the marks are very high.

59:23

90-Hogia, 91-ho-go-go-people.

59:25

People are securing very high marks, right?

59:28

These are the scores that we are getting right now, 89, 88.

59:33

These are the marks that we have right now.

59:36

And few of the marks are extremely low, right?

59:41

I'll come to that, Arnika, don't worry, I'll come to that.

59:44

Right, but you understood univariate?

59:45

You're okay with univariate?

59:47

Okay, okay.

59:49

Univariate is fine, right?

59:50

What we are discussing right now is univariate, I'm bi-variate.

59:52

We're by variant, don't worry.

59:53

Right now it is univariate, right?

59:56

Univariate, means single variable.

59:59

That is our focus right now.

1:0:01

I'll come to the other one again later.

1:0:03

Okay, I'll come to that, don't worry.

1:0:05

Why do we call it univariate?

1:0:06

because we only have a single variable, salary.

1:0:10

So, we're first salary here.

1:0:13

We're from the frequency, I find out what is the count,

1:0:16

how many people in each bin, and then we plot the graph.

1:0:20

This is the histogram.

1:0:23

We are able to understand the distribution of our data.

1:0:27

The other example, what are we doing?

1:0:30

We are again seeing an example of univariate analysis.

1:0:35

And here we are trying to understand.

1:0:36

understand the distribution of marks.

1:0:40

Let's let's take an example of a, uh, uh,

1:0:45

frequency is not considered a variable, uh, good things because frequency was originally

1:0:48

not there, right?

1:0:50

Frequency was originally not part of my variable.

1:0:52

Frequency to have, we made.

1:0:54

Original data in initially there was no frequency, right?

1:0:57

We, we made it to plot for me.

1:1:00

That's why we're we're univariate caret.

1:1:03

Okay?

1:1:04

So most of the students, they secured high,

1:1:06

marks. Now, man, the paper is easy. So, everybody scored high marks, 95, 96, 99.

1:1:12

And there is one person who scored, let's say, five. Okay. Well, whatever reason.

1:1:17

If he can be any number of reason. Yeah, so that was pari not

1:1:21

or then they were sick, or they got some grace marks, whatever, you know. So this is what

1:1:28

is called a left skewed distribution.

1:1:32

If you're up this basis, then we call it a left skewed kind of a distribution. So we call it a left skewed

1:1:36

kind of a distribution. So this is exactly what I have tried to visualize here for you.

1:1:42

Update sector, this is exactly what, uh, what we are trying to, uh, what we are trying to, uh,

1:1:50

you know, visualize here overall. That's intuition. This is what we are trying to visualize here

1:1:58

right now. So most of the, uh, again, we are looking at, uh, once again, we are looking at, uh, uh,

1:2:06

Bins, we have grouped our data into BIN, Salary Bins, and we are finding the counts.

1:2:11

Is that the accounts that we are getting, uh, sorry, this is just like salary, we can do the same for

1:2:15

marks also.

1:2:15

Marks go Bins may consider and in univariate. Why? Because we only have a single variable right now.

1:2:23

Yeah, say up, uh, first you calculate what, how many students got, uh, different, different

1:2:29

buckets of marks and then you try to visualize it.

1:2:32

Now, you'll see, the 80 to 90 bucket is, so it's not very visible here, but it's an example I'm trying to show you.

1:2:41

Now, look, the 70 to 80's a bucket here, here's a lot.

1:2:46

The 80 to 90's bucket here, here are a lot of people here, a lot of students here.

1:2:51

Many students got 80 to 90. Many students got 70 to 80.

1:2:54

Many students got 60 to 70. This is, right?

1:2:57

Many students got 60 to 70.

1:2:59

Many students got 60 to 70. A lot of people here here on marks made. You're able to

1:3:02

the counts frequency. Y axis, always frequency, okay? Whenever you do histogram,

1:3:08

right? Jabi, javvy, let me just write it down. Histogram. Y axis is always frequency. This is

1:3:21

always going to be a kind of count. So, y-axis will always be frequency. Y-axis will always be a kind

1:3:27

of a count. That's the way how we look at it. So, y-axis will always be frequency.

1:3:32

Y axis will always be a kind of account.

1:3:37

That's the, that's the way how we look at it. Okay. So, and you can clearly see that there is one

1:3:43

person who has got, that there is one person who has got a very, a very, a very less amount of money.

1:3:52

Very less number of marks. Sorry. So most of the people have secured a high marks,

1:3:58

80 to 90, 70 to 80, 60 to 70. And there is a one person who has secured.

1:4:02

10 to 20. Okay, you can see, 15, 5 to 15 in between. This is one person who's

1:4:07

scored ready. This is. This is our left skewed distribution. This is what we say?

1:4:11

This is left skewed distribution. Left skewed or negatively skewed. Okay. So simple

1:4:21

concept is. Right now, we just discuss the concept of skew. Now, it's what repercussion is.

1:4:26

Why this problem is? What is the same in all things we'll discuss in ML. As I told you, it's a, it's a

1:4:32

connected topic. So right now, today, the key learning is we just understood what is skew.

1:4:37

We have skewned. And why is it left skew? Negative skew? Because you can you? This is going

1:4:44

towards the negative x-axis. This is origin, right? This is your negative side or your positive side. It is

1:4:49

skewing towards the negative side. Whereas here, it is positive skew, right-stue. Right-stue. Right-side

1:4:54

is right-sue is. Left side by going to left side by go. Okay, now.

1:5:02

Okay, let's go.

1:5:05

Ah, well, absolutely. By variant, let's see. No problem. I hope this is absolutely clear. Univariate. Now, what is bi-variate? Let us see.

1:5:13

I will show you absolutely.

1:5:16

By-variate is exactly what we are doing.

1:5:25

Bi-variate is exactly what we are doing here in our current use case.

1:5:31

This is a beautiful example.

1:5:32

of a bi-variate analysis. Let us see that. So all if you can take a look at it.

1:5:43

This is your marketing spend. This is your category. So a very good example of bi-variate analysis

1:5:51

would be something like this. X-axis is your category. Why-axis is your category? Y-axis is your

1:6:02

I think spent have. Okay. And you can plot that okay. You have group buy

1:6:10

in PANDAS right? Now we have SQL maybe group by discused by discussed. PANDAS may connect

1:6:14

P-D dot group buy. All of you recall that now, you know? So same way, if you

1:6:18

make it go, electronics is a category. I'm just trying to show the mock chart for you.

1:6:23

Electronics is this is so, isn't? I know? I'm just giving an example, guys. The numbers may not

1:6:30

not be perfect. So just forgive me for that.

1:6:32

Apparel is something like.

1:6:35

It's kind of it.

1:6:36

That's kind of it. And finally, this is apparel.

1:6:39

And here here here one other category is, which is furniture.

1:6:41

Furniture, furniture, it's a very commoner.

1:6:44

Okay. I want to just want to just want to show you the proper visualization.

1:6:49

So, anyway, it's just whatever.

1:6:52

This is furniture. Okay.

1:6:55

This is called a bivariate analysis.

1:6:58

Why? Because, if you look, here the two variables are, it means the different color.

1:7:02

Here here on variable one category, variable to spend, both these variables are part of my data.

1:7:07

Category or spend is part of my data.

1:7:09

Original data are part. They are both variables.

1:7:12

That is why we call it, that is why we basically call it bivariate analysis.

1:7:17

Why is it called bivariate analysis? Because this is, there are two variables that we are tracking right now.

1:7:22

Variable one is category and variable two is fend.

1:7:26

So analysis of two variables, so hence we call it bivariate analysis.

1:7:30

And this is where bar chart is very, very useful.

1:7:32

And more importantly, this is your x-axis is one of the variables will have to be a

1:7:42

categorical variable.

1:7:43

The other, your number is.

1:7:45

One, your non-numeric variable has.

1:7:49

The other, your numeric variable is.

1:7:51

And this is how we look at a, okay?

1:7:54

Gurtej and Arnika, you guys are fine.

1:7:57

We will discuss that.

1:7:59

We'll discuss that.

1:7:59

And guys, set your settings to everyone.

1:8:02

Chat settings, everyone. So easy it'll. Everybody will get to know your questions, right?

1:8:06

Okay. So just make your chat settings to everyone. So that when you ask the questions, everybody will get to see.

1:8:13

Yeah. Uh, good discussion. Two numeric variables, what is it? I'm discussing. Very good question.

1:8:18

Most scatter plot are. We, we'll compare. Right now, our discussion is limited to histogram versus bar chart.

1:8:25

So what is the key takeaway from our conversation?

1:8:27

Abhi, our demo may have. Let's come back to our demo.

1:8:32

Okay, Arnica, I hope you got it, right?

1:8:34

By barriette was fine with you.

1:8:37

So if we look at only the sales column,

1:8:40

if we're in sales column, okay?

1:8:43

We'll say, we'll say,

1:8:43

hey, sales's distribution,

1:8:45

this your histogram over.

1:8:47

You can't this kind of histogram.

1:8:49

Code two lines, okay?

1:8:51

That we'll tell you.

1:8:52

We'll tell you.

1:8:52

We'll tell you, don't worry about that.

1:8:54

Code, we will see.

1:8:55

But you can just go, you can just go and create a distribution plot of the sales data.

1:9:02

So how will it look like?

1:9:05

X axis will be like sales.

1:9:09

And Y axis will be something like a frequency.

1:9:11

Bins, you know, count.

1:9:16

And you can track, okay, how many of the instances we have.

1:9:19

This your histogram will be.

1:9:21

Okay?

1:9:21

Now if you tell me, no, I want to see category-wise sales.

1:9:25

Now we have category-wise sales.

1:9:26

We need.

1:9:27

We have X-axis in category-wise.

1:9:28

need.

1:9:31

And y-axis in sales.

1:9:34

Then it becomes by variant.

1:9:35

Two variables go and it becomes a bar chart.

1:9:38

Because you're up category-wise, group by category-wise, you want to see the sales.

1:9:41

Okay.

1:9:42

Category-wise, region-wise sales.

1:9:44

You know?

1:9:45

A team-wise number of runs.

1:9:47

IPL in you want to know which teams scored the number of highest number of sixes.

1:9:51

Okay?

1:9:51

So these are examples of bar chart.

1:9:55

So that I said, the first first said that data is very important.

1:9:58

need to understand your data, what your data refers to.

1:10:01

Now that we broadly know the concepts, we'll see more, we'll discuss more use cases.

1:10:08

Or a line chart, line chart to care, there is not much to talk about.

1:10:11

All of you know line charts.

1:10:13

Line charts are very good for showing trends over time.

1:10:16

Trends, meant X axis has to be some kind of a time.

1:10:20

So, so in a line chart, the X axis basically refers to some kind of a time.

1:10:26

line chart may x-axis basically refers to some kind of a some kind of a time.

1:10:41

That is what x-axis basically refers to.

1:10:45

Let us see.

1:10:46

I think I think the best way to again learn this is to see a small demo.

1:10:49

Let us see this in action.

1:10:51

So we have the same data right now.

1:10:54

First, I will do the charts for all.

1:10:56

that we just show you the visualization part.

1:10:58

Then I will walk you through the code part.

1:11:01

So back to the same data set once again.

1:11:04

So here here you have a month column and a sales column.

1:11:08

This is the perfect example for doing a line chart.

1:11:11

You can see how X axis month, Y access sales.

1:11:14

That's the use case for a line chart.

1:11:16

Now trend to understand.

1:11:19

That's January in sales it was and October in sales increased all the way to this.

1:11:24

This is a great use case.

1:11:26

for using something called the line chart line chart is very very good for this

1:11:29

kind of a scenario so that's the use case where line chart again i repeat line chart is very

1:11:34

very good line chart is very good especially for understanding the basic trend that's the thing

1:11:41

now what kind of a trend are we looking at right now we add we have something called

1:11:49

we have something called an uptrend so we are specifically looking at

1:11:55

looking at something called an up trend.

1:11:59

Up trend means there's a there's a there's a small increase.

1:12:07

Up trend is what you're able to see.

1:12:09

But it is continuing to increase over time.

1:12:13

And whenever you are trying to do this kind of a sales analysis, trend analysis,

1:12:17

line charts are very, very useful. What could be some other practical examples of

1:12:20

line charts? I think the best example of line charts could be your nifty and

1:12:25

all that right? You, you know nifty 50 50 up. Nifty is the Indian stock markets, right?

1:12:32

So, you Google in Nifty 50 search

1:12:33

your line chart is. Okay.

1:12:35

You, you last one month's data, look. Last six-month data, look.

1:12:38

Now, look. You know, this is the great example of a line chart.

1:12:42

Line charts are, again, they are examples of bivariate analysis. This is bivariate.

1:12:46

Is it? So bivariate, we've discussed

1:12:50

now. Now, you know, how interesting this is. This is also bivariate. This is also bivariate.

1:12:55

This is bi-variate. But this bi-variate how are? X-axis is some kind of a time and Y-axis is

1:13:03

some kind of a number. X-axis always time. In line chart, X-axis will always be a time.

1:13:11

You can see S&SX, NIFTI, sorry. NIFTI, sorry, NIFTI, it was somewhere here.

1:13:19

Then, it was kind of stable. And then, you know, the February end of, from there, Israel

1:13:24

strikes through here. Iran was struck and I think after that there was a huge dip. And

1:13:29

after that recovery, now if we say there is a bit of a dip because I think they are again

1:13:33

considering some military action on Iran. So there's also some dip happening. So you can see

1:13:37

this pattern. Because this is a great use case for a line chart. And it's very interesting.

1:13:41

You can take second one year, five year. You can you see COVID pattern. You can see a beautiful

1:13:47

uptrend. This is a great example of a line chart again where you can start to see what the nifty was all the way

1:13:54

into early 2000, how it increased over a period of time. And you can see all the way to

1:13:59

2020, there was a big deep due to COVID. This COVID market. Markets up called here.

1:14:04

And then once again, you can see this interesting pattern that's playing out. So these are

1:14:09

examples of line charts, basically. We can talk about anything. You know, Nipti analysis

1:14:14

or sales analysis. You know, you are trying to track the company sales. So, basically,

1:14:19

you're, basically, you know, y-axis in could do anything. X-axis, it's always time. Now, you know, why-axis

1:14:23

in this. Stock price, gold price,

1:14:26

asset price,

1:14:27

it's, company's sales

1:14:28

and, player's run is

1:14:29

a player run and exist

1:14:31

are. Let's say, Sachin,

1:14:33

what is the total number of sixes?

1:14:35

Sachin has been hitting over the last

1:14:37

X number of years.

1:14:39

Sachin has been playing since 2000, right?

1:14:41

You know, 2000s like 2005,

1:14:43

so I think at least I have seen him.

1:14:46

But you can track it, very interesting,

1:14:48

so this can be number of sixes.

1:14:51

It can be number of sixes.

1:14:52

It can be number of sixes.

1:14:52

number of sixes or number of hundreds,

1:14:54

that line chart would.

1:14:56

Year-wise, you are tracking how many sixes they are hitting.

1:14:59

These are all beautiful examples of line charts.

1:15:02

So, by variant, but

1:15:03

always an axis number, okay?

1:15:05

Please keep that at the back of your mind.

1:15:08

Next, this our bar chart

1:15:09

we've already explained what bar chart.

1:15:11

We'll show in, don't worry.

1:15:13

Code is syntax and I always

1:15:14

encourage people never to remember syntax.

1:15:17

Concepts to understand.

1:15:18

Concepts to understand.

1:15:18

If you're not clear, then

1:15:20

then code, what will be?

1:15:21

First thing is concept.

1:15:22

If you know the concept, people will forgive you for forgetting the code.

1:15:26

Believe me, in today's market, today's world of AI,

1:15:29

even if you do not remember the code, it is absolutely okay.

1:15:33

But you have to know things to understand,

1:15:35

that you can't what use are.

1:15:36

Now, look, this is bi-variate.

1:15:38

Month versus sales.

1:15:40

This is bi-variate.

1:15:41

This is a big-variate.

1:15:42

Now, you'll ask, sir, then both bivariate are,

1:15:45

so how we decide we'll decide what we are?

1:15:47

So, as I've said, if you have,

1:15:48

if you have time, then line chart will,

1:15:50

always.

1:15:51

But if your category,

1:15:52

it will always be a bar chart.

1:15:55

This is an example of a bar chart.

1:15:57

You can clearly see group by apparel,

1:15:59

your total sales, how it's how much?

1:16:01

And group by furniture,

1:16:03

you can see how furniture for total sales

1:16:04

is quite. So this is the difference

1:16:07

between line chart and the bar chart.

1:16:09

This is in a horizontal manner.

1:16:13

This is also like a horizontal view of the bar chart.

1:16:15

We are able to see.

1:16:17

Now coming to the code, I don't want to again

1:16:20

make you memorize the code,

1:16:21

but just wanted to show you at least so that people

1:16:22

can see the code. So you can see.

1:16:25

This is the way how we do the plotting using

1:16:27

Matlot lid. Please don't memorize it.

1:16:29

You can't you.

1:16:29

You can't remember it.

1:16:31

There are hundreds of functions we have

1:16:33

and we strongly discourage you for memorizing all this.

1:16:36

Please don't memorize this.

1:16:37

So, DFP at t dot

1:16:40

So the first argument is,

1:16:42

this your x-axis in.

1:16:44

So df sales month is part of your x-axis

1:16:46

and d-f sales, sales is part of your y-axis.

1:16:50

X-axis.

1:16:51

And back-y-axis.

1:16:52

These are all the formatting properties have.

1:16:56

You're saying,

1:16:56

we've got here a lot for you to understand it.

1:16:59

You can here here here,

1:17:00

see what is the line color is.

1:17:02

Now, line is blue.

1:17:03

You're what you're now?

1:17:04

So you're not to this.

1:17:06

Marker is zero.

1:17:07

I mean, add dots to the data points of visibility.

1:17:10

Okay?

1:17:11

So here we're here, we're here

1:17:12

dots there.

1:17:13

So when the line is going, every dot,

1:17:15

every data point we're here

1:17:16

dot down there.

1:17:17

That's your marker equal to zero.

1:17:19

Line width and line with.

1:17:21

Line with.

1:17:22

time style.

1:17:23

Simple.

1:17:24

So this is the simple mat-plot flip command.

1:17:25

You can you can't it.

1:17:26

You can't it.

1:17:27

We can't it.

1:17:28

We can't let it.

1:17:29

Let's just, let's just

1:17:31

even if I remove this.

1:17:33

Even if I remove this absolutely,

1:17:35

your code will run absolutely fine.

1:17:38

Your code will run absolutely fine.

1:17:42

Let me completely remove this part.

1:17:44

And if you run the code,

1:17:46

your code will run absolutely fine.

1:17:48

Now look,

1:17:49

but,

1:17:50

I don't need it.

1:17:51

All right.

1:17:52

All right.

1:17:53

So sometimes the code can look really simple.

1:17:55

I could have done this for you also.

1:17:57

But then I just wanted to show you that the other variables are.

1:17:59

So this is the simplest way to remember plotting.

1:18:02

Do you.

1:18:03

PLT dot plot.

1:18:04

X axis and y-axis.

1:18:05

And just there.

1:18:06

All the plots will look only give X axis y-axis.

1:18:09

The other arguments are.

1:18:11

Okay?

1:18:12

That you just wanted to clarify about.

1:18:14

Now,

1:18:15

next thing what we do?

1:18:17

This is optional.

1:18:18

This is not.

1:18:19

But if you can give nothing that.

1:18:20

like it.

1:18:21

PLT.

1:18:22

Title.

1:18:23

Title is nothing but the overall title of your plot.

1:18:26

So the plot's title of your title.

1:18:28

Your title is your title.

1:18:30

This is a title.

1:18:32

Next, you can see X label, Y label.

1:18:35

X axis's the label.

1:18:37

And PLT dot shows to render the plot.

1:18:40

That's it.

1:18:41

Second, we are seeing a vertical bar chart.

1:18:44

Same thing.

1:18:45

So first we have group buy

1:18:46

then PLT dot bar.

1:18:48

Same way.

1:18:49

X axis is this.

1:18:50

that's it.

1:18:51

Color, ignore.

1:18:52

Please.

1:18:53

This is the optional argument.

1:18:54

You don't have to do it.

1:18:55

Most important, you have to write PLT dot bar and you have to give X axis.

1:18:59

What is the category?

1:19:00

Y axis is the same.

1:19:02

That's it.

1:19:03

Again, we discuss the last one, which is the horizontal bar.

1:19:06

Again, color ignore.

1:19:08

This is the formatting kind of option.

1:19:10

But these are mandatory options.

1:19:11

You have to give you.

1:19:12

You have to tell you.

1:19:13

Now you are plot.

1:19:14

You are, then you are to tell you.

1:19:15

If you are,

1:19:16

to specify,

1:19:17

so these are mandatory options.

1:19:19

What you are seeing?

1:19:20

on the screen right now.

1:19:21

We have to specify what is the category, what is the sales.

1:19:24

Okay?

1:19:25

So this is the basic plotting that I wanted to show you.

1:19:27

So key takeaway, we discussed about something called a bivariate analysis.

1:19:31

We have two types of bivariate analysis studied.

1:19:34

If there, time's some component, then that line charted.

1:19:37

We can.

1:19:38

You can measure.

1:19:39

This is a nifty trend,

1:19:40

gold prices, asset prices.

1:19:42

Today markets,

1:19:43

it's a little up up and then it,

1:19:45

then it went,

1:19:46

so elections kind of impact would.

1:19:48

But tomorrow you might see with BJP, this might see.

1:19:49

see with bjp's massive victory markets usually tend to increase you know bjp with a strong mandate you'll see nifty share markets will go up unless some other massive news comes up but you can expect that tomorrow also the trend will go up okay now uh coming to this thing understanding dimensions under sorry understanding distributions sorry so line chart if there is a time and if you have a categorical data if you have a categorical data then we create a bar chart or a

1:20:19

kind of a column chart, that's kind of a column chart.

1:20:21

But two variables are we have.

1:20:24

Okay.

1:20:25

So understanding distributions, histograms and statter plots.

1:20:29

So histograms are we know.

1:20:31

This we have a new topic of.

1:20:33

This is a new topic over.

1:20:34

This we have already discussed.

1:20:36

It shows the distribution of a single numeric variable.

1:20:40

And what we have used here, guys.

1:20:43

We have discussed something called univariate analysis.

1:20:46

So we have mentioned here here

1:20:48

I have here mentioned but you guys know it. You guys are better. So you know what is univariate now. So a single numeric variable.

1:20:55

Excuse me. This is called a uni variant analysis.

1:20:58

Okay.

1:20:59

It's quite interesting.

1:21:01

And if we have two numeric variable,

1:21:04

so we have to scatter plot use.

1:21:06

If I have to just kind of,

1:21:09

10 minutes break.

1:21:12

I'm happy to be.

1:21:14

But I'm happy to be.

1:21:15

But class sort of late started.

1:21:17

Not my fault, but you guys want to break? What do you say?

1:21:22

We can like a five minute.

1:21:25

What do you say?

1:21:26

Five minutes?

1:21:27

But class delay will not.

1:21:28

That we don't want to ideally.

1:21:30

But I think five minutes is fair, right?

1:21:31

Okay.

1:21:32

Let's take a five minutes break.

1:21:33

Yeah.

1:21:34

Yeah, we have time. We are fine.

1:21:35

I think we are good on the content today.

1:21:37

That's light.

1:21:38

So I think five minutes should be fine.

1:21:40

Yeah, that should be fine.

1:21:42

Okay, five minutes break turns.

1:21:47

Thank you.

1:22:17

Thank you.

1:22:47

Thank you.

1:23:17

Thank you.

1:23:47

Thank you

1:24:17

Thank you

1:24:47

Thank you

1:25:17

Thank you

1:25:47

Thank you

1:26:17

Thank you

1:26:47

We

1:26:54

Welcome.

1:26:55

Welcome back back.

1:26:58

Welcome back.

1:26:59

Welcome back. We'll start on here. We'll start on here.

1:27:16

on here.

1:27:19

I hope everyone's back.

1:27:46

Okay, great. Yeah.

1:27:50

I'm just just starting.

1:27:51

Just wanted to give all a few time to settle down.

1:27:54

Yeah, let's move on.

1:27:56

Let's move on guys.

1:27:58

So what we discussed here just to summarize the conversation very broadly,

1:28:02

what we covered until now, we have looked at, you know, two different types of charts here.

1:28:07

So we are seeing something called the, yeah.

1:28:12

So we have explored something called the line chart.

1:28:15

chart just a while back we talked about what is a line chart and you can clearly see that in a line chart we are looking at basically a trend.

1:28:24

So it's Y variant.

1:28:26

X axis we have some kind of a time.

1:28:28

Y axis we have some kind of a number.

1:28:30

So that is how we look at a line chart.

1:28:33

Excuse me.

1:28:34

Bart chart is where we are looking at also by variates.

1:28:38

But in X axis, you've got some category.

1:28:40

You have got some category.

1:28:42

And y-axis in some number

1:28:44

always, so we are looking at category-wise sales or region-wise sales, player-wise number of runs.

1:28:51

If you're a IPL context in a great example of bar chart could be, you know, what the analysts will do typically.

1:28:59

He will see who the player, your x-axis in player

1:29:03

and your y-axis in number of sixes-hook.

1:29:06

So you're tracking which player had the number, most number of sixes.

1:29:11

You can plot it as a bar chart.

1:29:13

So whichever player is it, the highest sixes will have the highest bar.

1:29:17

So these are all examples of bar charts.

1:29:19

Okay, now?

1:29:20

Next, we looked at single column distribution histogram.

1:29:23

This we have a single column here.

1:29:25

If you have single column here, sales analysis or salary analysis,

1:29:29

something like that, we'll do a histogram.

1:29:31

We will have only a single variable.

1:29:33

So what we'd, we'd, we'd we'd say,

1:29:35

count's column, and then we'd plot it out.

1:29:37

And we discussed concept like the right skew.

1:29:40

And we also discussed something like left skew.

1:29:42

What do we call it?

1:29:44

We call it either positive skew, right skew, skew,

1:29:48

S-K-E-W, and we call it left skew or negative skew.

1:29:53

S-K-E-W.

1:29:54

That's the way how we look at the whole thing.

1:29:56

And finally, we also understood the concept of correlation,

1:29:59

the scatter-plot.

1:30:00

Scatter plot to have we discussed here, but this is scatter-plot.

1:30:02

Remember, if we complete the story,

1:30:04

scatter-plot is also bivariate.

1:30:06

This is also bivariate.

1:30:09

This is bivariate.

1:30:11

But here, it's a bivariate.

1:30:12

variant of two numerical variable this is also a numeric y-axis is also numeric so we are looking at a distribution of two

1:30:23

numeric variables x-axis is also a numerical variable and y-axis that you're seeing is also a numerical

1:30:28

variable so that's the use case of a scatter plot okay so we will see some examples of that but

1:30:33

just wanted to clarify the four types of plots that we are looking at right now

1:30:38

it's a ball yeah so i i mean cricket may uh if you ask me scatter plot kind of

1:30:42

example what is. So, it could be relationship between force and sixes.

1:30:48

The data could be something like this.

1:30:51

Your, your player is, okay?

1:30:54

One is your player name.

1:30:56

I'm just trying to curate a data from scratch.

1:30:58

Yogiya number of force.

1:31:00

How many force is.

1:31:02

You get how sixes are.

1:31:03

And you're trying to find some relationship.

1:31:06

Every row, again, I'm again repeating, understanding of the data is very important.

1:31:10

You know,

1:31:11

what is one row? What is one row? What is one column? So that understanding is very important.

1:31:17

So when I'm plotting a data like this, this player-wise analysis is.

1:31:21

Every player, you'll know, this player's of this player has hit 1004s and like 76s.

1:31:28

This player has hit, let's say, let's say, 96s. This player has hit, let's say, 74s and 506s.

1:31:35

So you'll buy and large a correlation digger. So scatter plot is like a numeric. It's like a relation.

1:31:40

It's like a relation.

1:31:41

between these two columns. Two numerical columns. You've got a sixes column and you've got a force column. And scatter plot is like a kind of a, you know, visualization, distribution of like a relationship between these two columns that you're able to see. On one hand, you're able to see number of force. On one hand, you've got number of sixes. And you're looking at the relationship between these two columns. And that is what we call a scatter plot. Every dot that you see, every dot that you see on the scatterer.

1:32:11

plot is basically one row of data. One row of data is every dot that you see on the scatter plot.

1:32:17

One row of data, that is a dot on the scatter plot. That's what we are able to observe right now.

1:32:22

Every dot is like one row of data on the scatter plot. So we say we can clearly say, that we're

1:32:31

a relationship, we're going to. I'm a correlation. Correlation, matter of relationship between two

1:32:35

variations. And in the context of the current table, if this is number of force,

1:32:41

and it is a number of sixes. What can you say?

1:32:45

You can say, you say, usually, when the number of force is more, the number of successes is also more.

1:32:52

So players who are typically hitting more force are also hitting more sixes.

1:32:56

That pattern clear, because in boundaries in the four, chaka, six, is. So, players who are hitting force are also usually eating more sixes.

1:33:03

And use, you can have some outliers. You might have some outliers like, you know, cricketers who are only hitting sixes.

1:33:08

So chock ain't like, like, maybe you will have a dot somewhere here.

1:33:10

like this is the layer who is only hitting sixes. So the number of force are very low,

1:33:15

but the number of six is the very high. Or the other way round, which just ground might feel

1:33:19

right. The number of force are very high, number of sixes are very low. This is the kind of pattern

1:33:23

that you would be able to see on the screen, right? So I hope everybody is absolutely clear right now.

1:33:34

Okay. So this is a bi-variate analysis that you are able to see on the screen. By-variate.

1:33:40

analysis and this is the thing about the scatter plot that we, that we discussed. And we can,

1:33:45

we can talk about some more examples. So this is one. I'll come to some more examples as we go along.

1:33:50

But this is just a very theoretical understanding of the different types of charts we are talking

1:33:53

about. So sari variate is bi-variate. This is bi-variate, by-variate. Scatter is also bi-variate. This is

1:34:00

bi-variate with the time. By-variate with the category. And this is bi-variate in both are numbers.

1:34:05

X-axis be number, y-axis be number. Okay. Okay.

1:34:08

Okay.

1:34:09

A one example.

1:34:10

This is our use case actually.

1:34:12

This is, let's say, study time versus marks.

1:34:14

So we have x-axis which is amount of time you're studying.

1:34:18

And y-axis is how much of marks your security?

1:34:21

So we've got student-level data.

1:34:23

Let's say we have a student-level data.

1:34:25

Board exam of survey or whatever.

1:34:28

And we are tracking that.

1:34:30

Can we find a relationship?

1:34:31

Can we find some relationship between how much time you are spending,

1:34:34

studying versus how much marks you're getting?

1:34:36

typically, if people are spending a lot of time studying, they're usually getting high marks.

1:34:41

That is like a very strong relationship or a strong correlation that you're able to see.

1:34:46

If you're spending more time studying, then you're definitely getting higher marks.

1:34:50

So we will see a positive correlation here.

1:34:52

So this scatter plot here. I hope everybody's aligned.

1:34:56

And then we discussed this beautiful example.

1:34:58

We saw this bar chart, how it's going. And again, do not memorize these things at all.

1:35:02

So we looked at the simple syntax of how to plot the bar chart, pltt.

1:35:06

Any kind of plot that you're doing using matplotlib,

1:35:10

we're plt dot use.

1:35:12

Plot dot bar, PLT dot hist, PLT dot scatter.

1:35:17

And the most important learning will be in terms of syntax, X, comma, Y.

1:35:22

If you're this one thing, it's from you can't quite, X, X, comma, Y.

1:35:28

This is all optional but you have to say what is X axis, what is y axis?

1:35:32

What is y axis?

1:35:33

You have to say, X level, do, Y level, do.

1:35:36

This is X level, this is Y level, and this is PNT dot grid.

1:35:40

The grids, okay?

1:35:41

This is a simple way how we understand the syntax.

1:35:45

Okay, now coming to some examples of distribution plots here,

1:35:49

right?

1:35:50

Z-axis be able to absolutely.

1:35:52

That's really relevant not, but Z-axis is your scatter-plot.

1:35:54

You can, you can.

1:35:56

And this is what we have with respect to histograms and scatter-plot.

1:36:02

Okay, all if we can give it a glance, everybody,

1:36:05

and we will be discussing this.

1:36:06

This we'll be demo will look at.

1:36:08

But what I'm focusing on right now is from a code perspective.

1:36:12

Code is very simple.

1:36:14

There's nothing in code in.

1:36:15

So PLT.Bar we discussed.

1:36:17

We've, what kind of code discussed?

1:36:19

PLT. bar, is, right?

1:36:23

PLT dot plot.

1:36:23

PLT dot plot, we've been line for the bar chart.

1:36:28

PLT dot hist for the histogram.

1:36:31

You know?

1:36:31

What is.

1:36:32

What is?

1:36:32

It's nothing.

1:36:33

It's very simple.

1:36:34

Dot hist.

1:36:35

And PLC are scattered for the scatter plot.

1:36:37

You can see the code is very simple.

1:36:40

The other concept is one.

1:36:42

Histogram is when we have a univariate thing.

1:36:46

So this is student marks distribution.

1:36:48

Same way that I discussed in my slide.

1:36:51

So that same thing, we have here here for example.

1:36:54

Okay?

1:36:54

Now, you can see, we are divided our marks into bench.

1:36:59

A lot of students got average to high marks.

1:37:02

And few students got very low marks.

1:37:04

So this is what?

1:37:05

skewed? What kind of skew are we looking at?

1:37:07

We are looking at an example of a left skew distribution.

1:37:11

Most of the students got average to high marks and some of the students got very low marks.

1:37:16

So we are looking at a kind of a left skew or a negatively skewed distribution.

1:37:21

That's the way how we are looking at the whole thing.

1:37:24

And what about this one?

1:37:26

How?

1:37:28

Yeah.

1:37:29

Yeah. I will talk about it.

1:37:30

I don't worry. Yeah. Yeah. What is the scatography? We'll see. We'll see.

1:37:33

Histograms, we've got quite, but how, how we'll see. Don't worry.

1:37:39

So, first, this data is.

1:37:41

So before we understand the scatter plot, let us, let us see our data for a minute.

1:37:46

What kind of data do we have, basically?

1:37:49

So the kind of data we have here is, the kind of data we have here is something like this.

1:37:54

Upka the data frame will have, the data frame will have a column called hours.

1:38:00

and the column called marks.

1:38:06

This is your data frame.

1:38:08

So, first, data, the structure is to.

1:38:11

Whenever we do any kind of analysis,

1:38:13

we have to all understand the structure of our data.

1:38:15

That data, what is each row?

1:38:18

So you have a student's surveyed.

1:38:19

Let's say at Masai school, we are,

1:38:21

we have got many, many students across the country who are enrolled across all our courses,

1:38:25

right?

1:38:26

So we are trying to do a small survey to understand,

1:38:28

is it true that if you spend more time?

1:38:30

you get more marks, right?

1:38:32

I'm not saying marks are the only indicator of a person,

1:38:35

but let's say generally that's the way we evaluate right.

1:38:38

So we want to just do a small survey.

1:38:41

So every student, we are capturing the data.

1:38:44

So this data we're capturing,

1:38:45

every student for it.

1:38:46

So how it's how long time per day,

1:38:48

how much marks to go,

1:38:49

how much time per day,

1:38:49

how much marks were.

1:38:51

So we are looking at the total number of hours you are spending

1:38:54

and how much marks you are securing.

1:38:56

The total number of hours you are spending,

1:38:57

how much marks are securing, and so and so forth.

1:38:59

So that's the information.

1:39:00

we are able to get right now.

1:39:03

So the total number of hours you're spending and how much marks here is equal to.

1:39:08

The total number of, you know, hours year spending and how much marks you are security.

1:39:12

That's the inference we are able to make right now.

1:39:15

That's an inference, right?

1:39:16

And if you see, this is a use case for the scatterflow.

1:39:20

Aksha, first, so we, we're the graph use kind of, so scatter use.

1:39:24

Because there are two variables and two numerical variables, you have.

1:39:27

You have it, you've got it.

1:39:28

X axis or Y axis is.

1:39:30

This is your scatterplot.

1:39:32

Now, you're your question is, sir, this is what can I understand out of it?

1:39:38

So we can understand the relationship.

1:39:41

If you, if you, you know, if you look at this plot for a minute, what you are able to see right now?

1:39:48

You are able to see, you are able to see the kind of a relationship.

1:39:52

One second, guys.

1:39:56

So if you're able to see the plot right now, you are able to explore the relationship.

1:39:59

You can see that.

1:40:00

that as the number of hours increases, the final marks is also increasing.

1:40:05

So, you're looking at.

1:40:07

As X goes up, Y also goes out.

1:40:09

This is relationship between the two variables.

1:40:12

That means, students who are studying more, on an average, are getting more marks.

1:40:16

You can take one example and then I think you will follow the rest.

1:40:22

Let's say, up here one student, look.

1:40:24

This is how long time?

1:40:26

This two gantaparer, right?

1:40:27

And this person got 20 marks, right?

1:40:29

You just take one example.

1:40:30

If you have a data point in example, this person is studying for two hours and got 20 marks on an average, right?

1:40:38

And you have this person studied for seven hours and got 80 marks.

1:40:46

Okay, so this is where we can see the relationship.

1:40:50

And this only we have two points explain to give you.

1:40:53

But you can obviously do this for across all the data points, right?

1:40:56

You can clearly see the pattern on an average that.

1:41:00

As students are studying more, they are getting more and more marks.

1:41:06

Okay, okay?

1:41:06

Akshet, I hope this is clear.

1:41:08

So this is what is, what is it called?

1:41:10

It is called a positive correlation or a positive relationship.

1:41:14

Okay, again, I'm taking you back to our school days.

1:41:17

You know, I'm sure that term, so now called direct proportion.

1:41:20

But if one value increases, the other value also increases.

1:41:24

That means as X increases, as X increases, as X increases, as X increases, as X increases,

1:41:30

Y also increases.

1:41:34

So X if hours is going up, the marks that you're securing is also going on.

1:41:39

That is the inference behind what is referred to as relationship and core relation.

1:41:43

And also this is very interesting because you, you see, up on up on the capping go.

1:41:47

I mean, beyond the point, even if you study for more than direct proportion, 12 hours, 13 hours, 17 hours.

1:41:52

So, so up on up and that's the inference we are able to get.

1:41:55

Very interesting.

1:41:57

So this is the capping.

1:42:00

Okay? Are you able to understand?

1:42:03

Yeah.

1:42:05

That's a different thing.

1:42:06

That's a different thing.

1:42:08

That we actually pivot table, Gurdtage.

1:42:09

You have, shahed in Pandoz, which we're doing pivot tables and we're doing.

1:42:13

There is no visualization that we use for that.

1:42:16

Yeah, good question, Gourtage.

1:42:17

So we use our pivot table.

1:42:19

You have X axis in a group, and a group, and it's a count, but it's not common.

1:42:24

We don't, we don't visualize that kind of data usually.

1:42:27

But we can use the pivot table in some form to visual.

1:42:30

Or then we stack charts use that in the way.

1:42:32

Okay.

1:42:37

Okay.

1:42:40

Okay.

1:42:40

Okay.

1:42:40

Aksha, I hope that answers your question.

1:42:42

Okay.

1:42:42

Is it okay?

1:42:43

You followed.

1:42:44

X axis, y axis.

1:42:45

Interpretation is clear.

1:42:48

Right?

1:42:49

Right?

1:42:49

Okay.

1:42:50

Let's go.

1:42:51

Very good.

1:42:53

So let us see the demo right now.

1:42:55

So demo,

1:42:55

so demo to what's not.

1:42:56

But once the concept is clear, as I always say,

1:42:59

the demo is the easiest part.

1:43:00

demo in a very simple.

1:43:02

Here I'm taking a different data set and I'm taking an at-tech student performance data set.

1:43:08

Let's say you work for Masai School and we have a data set for 200 students showing how many hours they study and how much marks they received.

1:43:15

So we have a random data set

1:43:16

made, okay, this is real data not.

1:43:18

So we have a random data set made.

1:43:20

Okay, we'll let's show the data is what?

1:43:22

This is your DF students.

1:43:23

So data set looks somewhat like this.

1:43:27

Okay?

1:43:28

So a data set looks somewhat like this.

1:43:30

So we have a survey here.

1:43:31

Imagine this is a Zoom class.

1:43:33

So similarly, we have a Zoom class organized here.

1:43:35

We all, as we, as we feedback, form, form based in last.

1:43:38

We're similarly,

1:43:39

we're sending us, and we are asking you,

1:43:41

that you how many hours on a day you study?

1:43:44

And we will be tracking how much marks those students got.

1:43:47

It is very easy that we can collect this kind of a data

1:43:49

and this is how we want to do our own and basis.

1:43:52

Okay, something like this.

1:43:54

Okay, 200 rows.

1:43:56

So we have two variables right now.

1:43:57

So we have two variables right now.

1:43:59

So bi-variate, numeric.

1:44:00

and this is exactly where scatterplot comes in handy.

1:44:05

So first, here we've got data to create then first we will do the histogram.

1:44:11

Again, most important part of the code is this.

1:44:13

If you're just plp.is, it's just plp.is.

1:44:15

It's just you have to do.

1:44:17

Baki, whatever we have done optional.

1:44:20

Color, formatting, edge color,

1:44:21

these are all of things.

1:44:23

You know all these things.

1:44:25

Wherever you see all these nonsense is just formatting stuff.

1:44:27

Most importantly, you have to single variable entered.

1:44:30

Like, dot bar, we have to give x, comma, y.

1:44:33

Dot scatter, we have to give x, comma, y.

1:44:35

You have to give x-axis, y apsis.

1:44:37

So histogram in just one single variable that is marks.

1:44:42

I want to see the distribution of my marks column.

1:44:46

That's it.

1:44:46

Title, x, label, y level, same to same.

1:44:49

Now, now now, now make histogram.

1:44:51

This your histogram, very simple, okay?

1:44:54

And similarly, this is the code for the scatter plot.

1:44:57

As I told you, these are all additional arguments for formatting.

1:45:00

it. Most importantly, our study versus marks.

1:45:04

X accessed our study or Y accessed.

1:45:07

Whatever I discussed in the slide is in the code for you.

1:45:10

Very simple.

1:45:11

Okay.

1:45:12

And you, you can you can't quite.

1:45:16

Again, I'm telling you, we're just looking at how to explore the data,

1:45:20

how to explore the different patterns in the data.

1:45:23

Now, Java machine learning in the next module,

1:45:27

we will try to get a little deeper and understand that it's relevance what is.

1:45:30

That time we, we're going to correlation back from.

1:45:33

Now you have just correlation

1:45:35

that relationship, if one is going up, the other is going up.

1:45:39

Just to understand.

1:45:41

But this,

1:45:43

what's the other thing?

1:45:44

When we start building models,

1:45:46

how is this important?

1:45:48

We will see that in the upcoming course.

1:45:50

Right?

1:45:50

Just for now, we are again doing just EDA.

1:45:53

We're just exploring the pattern.

1:45:54

That patterns are how to make models buntier is the next course.

1:45:58

And finally, we have another very, very, very.

1:46:00

very interesting library called plotly.

1:46:03

Abitak, what were we using?

1:46:04

We were using something called mat plot clip.

1:46:06

We were using something called mat plotly.

1:46:08

Matt plotly used by we were plotting the different charts.

1:46:11

And now we will be using something called plotly.

1:46:13

Plotly is also a very similar kind of a library.

1:46:16

And it is a very similar visualization library that we have in Pistol.

1:46:22

In the Python.

1:46:23

So Plotly is a very popular and very interactive visualization library, I would say.

1:46:29

Very interactive kind of.

1:46:30

a, you know, visualization library is what you have.

1:46:33

That's what, that's what Plotley, you know, basically is referring to.

1:46:39

So now let's go back and see Plotly and what are the different things that you get.

1:46:46

Nothing, there's nothing different.

1:46:47

It's the same story.

1:46:49

Same charts.

1:46:50

Only thing is, it is slightly better, slightly more interactive.

1:46:53

And quote, it's a little easy.

1:46:55

Okay, so Plotly in the same thing.

1:46:57

Similar syntax, there's difference there.

1:46:58

You have, you know, here here.

1:46:59

First, we have a mock data set.

1:47:01

Data, Startups, Company, valuation, funding, country, industry.

1:47:06

So this is my data set right now.

1:47:07

And if you just want to see your data,

1:47:09

because it's very important to understand your data first,

1:47:11

let me show your data set first,

1:47:14

what kind of data we have curated first.

1:47:17

This is your data set.

1:47:20

So the very first step of data analysis,

1:47:22

which we actually make, the very first step is we try to look at this data set,

1:47:26

and we try to figure out what kind of chart.

1:47:29

charts can we build using this data.

1:47:31

This data use, what kind of visualizations can we create?

1:47:34

What kind of charts can we create?

1:47:36

What kind of visualizations we can create using this particular data set?

1:47:38

That's the first thing we try to do.

1:47:40

We try to figure out the kind of visuals we can create.

1:47:43

So, first, you know,

1:47:44

this to study.

1:47:45

That same story is.

1:47:47

DF startups.

1:47:48

Dothead, dot, info.

1:47:49

Nothing.

1:47:50

The same story, right?

1:47:50

And that is where you take a call as to,

1:47:55

sorry, I think, what you're going to share.

1:47:59

So we have the, this is fine.

1:48:14

So first thing that you try to do again is the dot head.

1:48:17

Dot head say, you have some data what type of data we have got.

1:48:20

Next, you do something called dot info.

1:48:23

You try to figure out what type of, you know, what type of,

1:48:27

D.F startups. Info.

1:48:30

You try to figure out whether we have any missing values or anything of that sort.

1:48:34

That's the next thing you try to do.

1:48:36

These are all the general stuff that you figure out.

1:48:38

And it is based on these that you try to curate in your head,

1:48:42

what kind of analysis we have to go back and do.

1:48:46

So whatever type of data we have right now,

1:48:48

we have to figure out what type of analysis we should be doing

1:48:51

on this particular data set.

1:48:52

That's the thing we have to do.

1:48:55

So we'll keep it simple for now.

1:48:57

Now, I think we know the concepts.

1:48:58

Here there time of time chart won't.

1:49:00

We cannot build a line chart.

1:49:03

First, you have you mind-map.

1:49:04

What can we do? What type of charts can we create?

1:49:07

Based on what I've talked about, right?

1:49:09

Based on our focus area for today.

1:49:10

So line chart not, because time is nothing is we have.

1:49:13

So first we will do a scatter plot.

1:49:16

So you have funding valuation or funding billions based on scatter plot.

1:49:21

So scatter plot will be like,

1:49:23

it will show me the relationship between.

1:49:27

funding versus valuation.

1:49:29

So can we find out that, okay, companies that get funded more are typically valued more?

1:49:34

Or usually it's usually if a company gets a lot of funding,

1:49:38

its valuation also increases.

1:49:39

It's obvious, unless there are some rare scenarios.

1:49:41

If you see all these companies like Open AI, Anthropic, these are some of the top of,

1:49:46

some of the most valuable companies in the world, right?

1:49:48

So it's a quite funding.

1:49:50

They are very well funded.

1:49:52

Private companies, Open AI listed not, Anthropic listed, not.

1:49:55

Open AI is the maker of chat, GPD.

1:49:57

All of you might have heard, right?

1:49:58

Everyone knows it.

1:49:59

This is our course here.

1:50:01

So companies that are funded more are usually valued more.

1:50:04

So first, I recommend that even before you start writing the code,

1:50:08

and that's the way how you learn.

1:50:10

You first, an empty sheet, blank sheet.

1:50:12

You know, you.

1:50:13

You know, data frame to say, what data is, what columns are,

1:50:16

what's numeric are,

1:50:17

what categorical column,

1:50:19

and what time column is.

1:50:21

And you're rough sheet in,

1:50:23

rough sheet in, okay.

1:50:25

We're here funding funding.

1:50:27

If we're going to go here, we'll here valuation

1:50:29

will.

1:50:30

And we'll scatter plot.

1:50:33

And you can't.

1:50:34

And you can draw

1:50:35

that expectation what,

1:50:36

expectation will, I will see something like this.

1:50:38

So you want to, you are expecting a positive relationship.

1:50:43

The companies that usually have more funding,

1:50:45

usually will have more valuation.

1:50:46

This is what you expect.

1:50:47

So if you might go,

1:50:49

then you go to Python in code.

1:50:50

Python,

1:50:51

in the code in,

1:50:53

there is.

1:50:54

Plt dot scatter.

1:50:55

Bracket down.

1:50:56

Bracket down.

1:50:56

X comma Y.

1:50:57

There's nothing.

1:50:59

Now,

1:50:59

Germany in Germany in

1:51:00

Germany in a second

1:51:01

in a second.

1:51:01

That's what I'm

1:51:02

again telling you.

1:51:03

The concept is more important.

1:51:04

The code is useless.

1:51:05

Okay?

1:51:06

Code you can,

1:51:07

like, it's so simple,

1:51:08

but you can again,

1:51:08

use some AI tools

1:51:09

and figure out the code.

1:51:10

But concept,

1:51:10

you cannot use AI to help you with concepts,

1:51:12

right?

1:51:12

If you don't even know

1:51:13

what is a scatter plot,

1:51:14

then AI cannot help you

1:51:15

like real time

1:51:17

understand that,

1:51:18

okay, this is how you do it

1:51:19

and I think.

1:51:21

That's all.

1:51:22

Well, AI,

1:51:23

there's a lot to do

1:51:24

whatever we are

1:51:25

discussing,

1:51:25

EDA that we are

1:51:26

discussing,

1:51:27

this is a

1:51:27

AI tools are.

1:51:28

So then we

1:51:29

we'll

1:51:29

not say,

1:51:30

we'll teach

1:51:32

about some

1:51:33

libraries,

1:51:34

which will

1:51:34

everything.

1:51:35

You don't have

1:51:35

to do

1:51:35

anything.

1:51:36

All of what we

1:51:37

are

1:51:37

discussing right now,

1:51:38

all these

1:51:38

will get done

1:51:39

automatically.

1:51:40

There are some

1:51:40

Python packages

1:51:41

which

1:51:42

will do all

1:51:44

of it for you

1:51:44

automatically.

1:51:45

And this is

1:51:46

what is

1:51:46

referred to as

1:51:46

auto EDA.

1:51:48

So

1:51:49

the whole

1:51:50

everything

1:51:50

everything we are

1:51:53

discussing, whatever

1:51:53

we are writing,

1:51:55

all this will not matter.

1:51:56

But understanding and interpretation will matter.

1:51:59

Your line chart

1:52:00

will be, bar chart,

1:52:01

will be

1:52:01

histogram

1:52:02

but you have to interpret

1:52:04

that is what

1:52:04

things, right?

1:52:07

Let's go.

1:52:07

Let's go.

1:52:08

PX, but bar,

1:52:10

you'll be the name of your data

1:52:11

frame,

1:52:11

company or valuation.

1:52:13

X axis

1:52:13

what is,

1:52:13

y axis is.

1:52:14

That's simple, straightforward.

1:52:16

This is plotly

1:52:16

plot is.

1:52:17

So if you

1:52:17

if you're plotly

1:52:18

a plot, very similar.

1:52:19

X axis is,

1:52:20

y-axis

1:52:20

here is,

1:52:21

so

1:52:21

it's not

1:52:21

the only thing is it

1:52:23

is interactive.

1:52:24

So you're

1:52:24

here on here

1:52:24

click

1:52:24

you can

1:52:25

interactive,

1:52:26

so that's the

1:52:26

best part

1:52:27

about

1:52:27

Plotoo.

1:52:28

Okay,

1:52:28

so it is

1:52:29

interactive.

1:52:30

And second,

1:52:31

use case,

1:52:31

PX.

1:52:32

Scatter, X axis

1:52:33

is this is,

1:52:34

y-axis

1:52:34

here, and

1:52:35

color by

1:52:36

yeah,

1:52:37

over name is

1:52:37

very interesting.

1:52:39

So this is the

1:52:39

normal

1:52:39

scatter plot,

1:52:40

which we

1:52:40

discussed

1:52:41

already,

1:52:42

X-axis funding,

1:52:43

Y-axis valuation.

1:52:44

What you have done

1:52:45

is right now,

1:52:45

try variant,

1:52:46

actually four variables.

1:52:47

Yeah,

1:52:48

three variables

1:52:49

here.

1:52:50

X is Y, and we are

1:52:52

colored by something.

1:52:53

We are colored by

1:52:53

country.

1:52:54

So,

1:52:54

yeah,

1:52:55

general pattern

1:52:55

is positive.

1:52:56

You can see,

1:52:57

you know,

1:52:57

the

1:52:57

funding is,

1:52:58

there's

1:52:58

valuation

1:52:58

so I think as

1:52:59

expected we are

1:53:00

seeing a

1:53:00

positive relationship.

1:53:02

And we are

1:53:02

also able to

1:53:03

see the values

1:53:04

by respective

1:53:05

countries,

1:53:05

that's the

1:53:06

countries in

1:53:06

what are.

1:53:08

Okay,

1:53:08

now.

1:53:09

Now,

1:53:09

you can see,

1:53:09

very clearly

1:53:10

USA is legal,

1:53:11

and China is

1:53:12

also very close.

1:53:13

So here

1:53:13

here here

1:53:13

it's a simulated

1:53:14

data,

1:53:15

so we've got quite

1:53:15

, but if you're

1:53:16

if you're able to

1:53:17

if you can't

1:53:17

so it will be a positive relationship.

1:53:20

What is the benefit of using plotly?

1:53:22

First of all, you can over over it and you can see the details.

1:53:24

This is your normal mat plot

1:53:25

limit

1:53:25

not going to be.

1:53:27

Normal mat plotly

1:53:27

we cannot do this, right?

1:53:28

So,

1:53:29

but in plotly,

1:53:30

it is very interactive,

1:53:31

number one.

1:53:32

And number two,

1:53:33

you're here

1:53:33

if money is a lot of data,

1:53:36

you can,

1:53:36

you can,

1:53:36

you know,

1:53:36

you can,

1:53:38

I think the best way to do it is

1:53:40

I'm in the other case

1:53:41

I'll make a better idea

1:53:44

that

1:53:44

so I think

1:53:46

let me do that

1:53:47

if we create a simple

1:53:49

plotly scatter plot

1:53:50

for this one

1:53:51

here

1:53:52

here here

1:53:52

here here

1:53:53

this is your

1:53:54

DF students

1:53:55

so I want to create a

1:53:57

plotly

1:53:57

chart for

1:53:58

DF students

1:53:59

take

1:53:59

so here

1:54:00

here

1:54:00

quote

1:54:00

I can use the same

1:54:04

code for it

1:54:04

nothing changes

1:54:06

okay

1:54:06

there it is

1:54:08

and

1:54:09

and

1:54:09

the scatter plot

1:54:11

I want to do the same thing

1:54:12

with Plotley

1:54:13

and you see

1:54:13

a difference

1:54:13

this is

1:54:13

matte plot

1:54:14

is not interactive

1:54:15

not

1:54:15

very static

1:54:16

right

1:54:16

and if you see

1:54:17

this one

1:54:18

it will be

1:54:18

really interesting

1:54:19

so

1:54:20

this is your

1:54:20

DF students

1:54:21

DF

1:54:23

students

1:54:23

okay

1:54:24

and

1:54:25

this is

1:54:25

our

1:54:26

studied per week

1:54:26

let me see

1:54:27

exactly

1:54:27

hour

1:54:29

study per week

1:54:30

okay

1:54:30

our study

1:54:31

and this

1:54:31

and this

1:54:32

is

1:54:32

March

1:54:32

X axis

1:54:35

accessed

1:54:35

got our study

1:54:36

and y access

1:54:37

So we are

1:54:38

March

1:54:39

and size

1:54:43

we all

1:54:44

we need

1:54:44

this is not required

1:54:46

not required

1:54:47

title

1:54:48

doesn't

1:54:48

need

1:54:49

take

1:54:49

let us

1:54:49

question

1:54:50

I told you

1:54:52

all this is redundant

1:54:56

columns

1:54:57

what is

1:54:57

most important is

1:54:58

x axis

1:54:58

y axis

1:54:59

as long as you get this

1:55:01

right

1:55:01

everything is

1:55:01

sorted

1:55:02

okay

1:55:02

this is sorted chart

1:55:04

and you can make a plotley's chart

1:55:06

and you can see see how

1:55:07

how

1:55:07

cool it is. Okay, compared to the static

1:55:09

matplot clip chart, same

1:55:11

we've done in Plotley

1:55:11

right?

1:55:13

This code

1:55:13

shared

1:55:13

not

1:55:13

so we're

1:55:14

we're paying

1:55:15

so people can

1:55:16

do this also.

1:55:17

You can already

1:55:18

start to see the

1:55:19

plotly chart is so cool.

1:55:20

So first

1:55:21

you can over

1:55:21

you can see

1:55:22

individual students

1:55:24

can't make

1:55:24

how much

1:55:24

how are studied

1:55:25

every data point is

1:55:26

like a student

1:55:27

you can

1:55:27

see

1:55:27

and the best part

1:55:28

the feature I like the most

1:55:29

about

1:55:30

plotly is

1:55:30

you can

1:55:32

interactively zoom

1:55:33

you can interactively zoom

1:55:33

you can zoom

1:55:33

can zoomed

1:55:34

imagine this is a lot of

1:55:36

students right

1:55:36

here

1:55:37

students

1:55:37

there are

1:55:38

200 data

1:55:39

points

1:55:39

here

1:55:39

so it's very

1:55:40

hard to

1:55:40

see

1:55:41

sometimes it

1:55:41

gets

1:55:42

very clumsy

1:55:42

let's say

1:55:43

let's say

1:55:43

you

1:55:44

you

1:55:44

what are

1:55:46

what are the

1:55:47

what are the

1:55:47

patterns

1:55:47

happening

1:55:48

between

1:55:48

four to

1:55:48

six hours

1:55:49

or

1:55:49

or

1:55:51

let's

1:55:51

here

1:55:51

five to six

1:55:52

hours

1:55:52

so

1:55:53

turns out there

1:55:53

are

1:55:54

lot of

1:55:54

students who are

1:55:55

here

1:55:55

five to six

1:55:56

hours

1:55:56

in a year zone

1:55:56

so you

1:55:57

have

1:55:57

you

1:55:57

can

1:55:59

actually

1:55:59

select this

1:56:00

portion

1:56:00

see very

1:56:01

interesting

1:56:01

you can

1:56:02

actually select

1:56:02

you're just

1:56:03

dragging the mouse

1:56:04

and selecting

1:56:04

moment I

1:56:05

release my

1:56:06

hours

1:56:06

observe very carefully

1:56:07

moment I release my mouse see how we are now zoomed into that portion.

1:56:11

How cool is that?

1:56:12

So this is like an interactive zoom.

1:56:15

So these are things in plotany

1:56:16

so

1:56:17

you can explore

1:56:19

and you can further zoom.

1:56:21

You can further zoom.

1:56:23

You can further zoom.

1:56:24

How cool this is.

1:56:25

Can you see?

1:56:26

How cool this is?

1:56:27

You can zoom into it.

1:56:28

You can zoom into it like that.

1:56:29

You can get into it

1:56:30

and you can see at a very granular level

1:56:32

what exactly is happening

1:56:34

right now, inside it.

1:56:37

So that's the intuition of

1:56:38

this thing.

1:56:42

See, both can be used for

1:56:44

both purposes, good thing.

1:56:46

So limitations, so as a

1:56:47

matplot clip's limitations

1:56:49

is the basic limitations of matplotly, but it is not

1:56:54

interactive. It is not interactive, I would say.

1:56:57

So matplot clip is static. It is not interactive.

1:57:00

So zoom, hover, exploring the dense data,

1:57:03

all these things

1:57:04

harder. You cannot do it directly. But Plotley is interactive. It's much easier for

1:57:08

exploration. But I want to clarify one thing. You ask me what is the limitation. So this limitation

1:57:12

is the slow. So because it is giving you so many visual features. This is simple

1:57:16

and 200 rows of data. But in practical real world, if you have tens of thousands of

1:57:20

data, plotly can get very slow. Even this rendering, this is all using your system

1:57:25

RAM. So system is quite slow when you're using plotly. It'll become very, very like, you know,

1:57:31

like, you know, like, think of it that way. Okay. So this could be

1:57:34

some other limitations I would say. Okay. Yeah. What is that? To analyze the data, where can we

1:57:42

analyze the data better than a scatter plot? No, no, it depends, right? Scatter plot is meant for a different

1:57:46

purpose, and histogram is meant for a different purpose. You have both. You know, so if you

1:57:51

say, sir, we have this data right now, where is that? So if you tell me that, sir, I have this data.

1:57:56

This data, this data, so we're what we can't? We use

1:57:59

or we'll histogram use. We'll say, you both. We'll say, you? You're both. You're, you know,

1:58:03

scatter plot use case. You want to analyze funding versus valuation. That's scatterplot

1:58:08

got two variables analysis here. That is one analysis you will get. Second, you're

1:58:14

histogram. You can study the distribution of valuations. You want to study the skew. So for the same

1:58:23

data frame, you can do multiple charts. You can just like how we were doing here, right? Make sense. Both

1:58:29

will serve different use cases. Histogram will help you understand what is the skewness.

1:58:33

data rights you are left skew here. Whereas a scatter plot will help you find the relationship

1:58:38

between the different variables. Positive relationship or negative relationship. Okay. Akshar clear. Absolutely.

1:58:44

All good. Okay.

1:58:49

Okay. Excellent. And now the last part is there is nothing new. This is just like the part where we are

1:58:55

just wanted to show you a few case studies. And also very important. It is like whenever you are doing data on

1:59:01

data visualization use, you know, you know, you know,

1:59:03

to annotate your data also. Now because by annotation be important.

1:59:06

If you look, we've seen, we've made line chart so made. But what we want to do is we want to annotate

1:59:11

our data that what is happening. What is the events that are happening right now? That is also very

1:59:15

important. So what I want to do is I want to extend the ideas. Now, we will take the next 10 minutes

1:59:20

and what I've given right now, very interesting. I've given a lot of use cases here. A lot of very

1:59:24

interesting sample data sets have given. And through these sample data sets, okay, you can now explore

1:59:30

and we can have a very broad discussion in terms of.

1:59:33

of how these charts can be used.

1:59:35

These are all caggle data sets. So we will see how to apply a little bit of EDA,

1:59:40

matplotly, plotly, and in all these real data sets.

1:59:43

All of these are caggle datasets. So we'll start our conversation with the sales

1:59:49

superstore data set. You can see. This is the sales superstore data set that we are able to see

1:59:55

right now. And here here, if you can see, if you can't see, so you can completely ignore the coding part.

2:0:03

But just remember, you, whenever we use something called dot annotate.

2:0:08

So dot annotate use and we can use it.

2:0:10

We can use it. So we have summarized whatever we are, you know, we have seen right now.

2:0:15

So the code can get a little heavy, but this is the broad idea.

2:0:18

Okay, this is pretty much been the overall discussion pointers for today.

2:0:22

Describe is null.

2:0:24

Value counts we've seen.

2:0:26

PLT dot plot, dot bar, dot histogram, dot scatter, dot show is to render the plot.

2:0:31

And finally the annotate is for the,

2:0:32

for those lines and markers basically.

2:0:35

So this is the intuition.

2:0:36

So now these are a few Kaggle case studies that I wanted to take you through.

2:0:40

Number one is the sample sales superstore data.

2:0:43

Okay.

2:0:44

After this go take for a minute.

2:0:47

All of you can just give it a glance all of you.

2:0:50

So we'll take around five minutes.

2:0:52

So you can just take a look at this data set.

2:0:56

So this is a huge data set.

2:0:57

It's not possible to do in a session.

2:0:59

But my idea is that I wanted to give you a little exposure.

2:1:02

so that you are able to see how some of these things can be done in the real one,

2:1:07

like a real Kaggle data set, a real competition, how you think some similar things can be applied.

2:1:13

So just give it a read on a few.

2:1:15

So context is given, data is given, just eye over it, just a preview there.

2:1:21

You just a bit just a bit of data and then we will have a small discussion in terms of what type of analysis can be done on this data section.

2:1:32

Okay.

2:1:43

So Superstore sales is the first one we will see.

2:1:47

Then we will see education.

2:1:48

Then we see finance.

2:1:49

All three are real data sets we have taken.

2:1:51

Ha, huge, massive.

2:1:52

Not expected in the classroom.

2:1:53

Obviously, I don't want you to, but yeah, part of it is to tell you,

2:1:57

you can load it from Kaggle, you can load the data.

2:2:00

It's a massive data set.

2:2:01

It's not doable in the classroom setting.

2:2:02

but just wanted to educate you so that people can uh what's that uh yeah yeah you need yeah

2:2:08

you don't need to download it no need to download it guys just just just wanted you to see the data set

2:2:12

that's it yeah just wanted to see that you don't have to download okay no need to download

2:2:18

yeah i need to log into caggle to download and all that no need to do that just go and explore

2:2:22

the data everybody and we have another very interesting data for student performance in exams

2:2:30

this is your second data set.

2:2:33

This is a very interesting data.

2:2:35

Gender, race, ethnicity, parental level.

2:2:38

So what degree?

2:2:40

Parents have got it.

2:2:42

That's how much data.

2:2:43

Lunch.

2:2:44

This is like I think some kind of a

2:2:46

subsidized lunch

2:2:50

or something like that.

2:2:52

So test preparation,

2:2:53

math in math and reading

2:2:55

in the score.

2:2:56

So you're trying to correlate.

2:2:56

It's a very interesting data set by the way.

2:2:58

So this is part of a massive message.

2:3:00

survey that was done. And you're tracking different students,

2:3:04

his gender, race, what is, what parents' education? Do they have enough money to buy lunch?

2:3:11

Or are they taking three subsidized lunch? And how is all this impacting?

2:3:17

He's got to get how? Very interesting. So you're trying to understand is, is, is your

2:3:24

parents' level of education having an impact on marks?

2:3:28

Is the fact that you're going to?

2:3:30

you're having free lunch, having an impact on marks.

2:3:34

I mean, it's because if you, yeah, this is very interesting again.

2:3:37

Is your test preparation having an impact on marks?

2:3:41

That's the use case of this data set.

2:3:44

And the third one use case is.

2:3:45

The third one use case is, it's a unique on startup data set.

2:3:49

Something very similar to what we discussed in last.

2:3:53

So I wanted to just take you, take you through like some sample problems, right?

2:3:58

So yeah.

2:4:00

I think the animation is very funny.

2:4:04

So whatever, this is the real data again.

2:4:06

So I apping up.

2:4:11

So,

2:4:15

AI people are doing all sorts of animations, no?

2:4:18

So in elections also, the news channels are showing all sorts of animations.

2:4:21

So what kind of made them.

2:4:23

So anyways, there is so much you can do with AI today, right?

2:4:28

Anyways, so this is also a very nice real data.

2:4:30

said based on exactly what I discussed, funding versus valuation.

2:4:32

So same thing, but only differences here are real data.

2:4:36

That was fictitious data which I created, but this is real data, SpaceX, Vildance.

2:4:39

You'll have valuation digger.

2:4:41

Date joint, country, city, industry, investors, what are.

2:4:45

So this is again a very interesting data set that you have right now.

2:4:48

Okay, so these are again three real data facts.

2:4:51

Now, you can go over it and then we can have a short discussion.

2:4:54

This will be another 10 minutes, 5 minutes max we can take.

2:5:00

And these are a few general ideas that I've given you, what it is, right?

2:5:10

So what kind of insights you will find?

2:5:12

Again, there's many more you can get, but again, it's a huge data set.

2:5:15

So as you see these three datasets, these are mostly the kind of insights that you'll be getting.

2:5:20

How to analyze the data, which is, how to analyze can analyze it?

2:5:23

What charts are based on whatever content we discussed, these are the kind of charts that you can potentially create.

2:5:30

Okay, that's the, that's the intuition, okay?

2:5:32

Let's take five minutes. I'll give you time to maybe see the data briefly,

2:5:36

come back to my notebook, see my screen, and see the insights that I'm deriving from this,

2:5:42

and then we can discuss.

2:5:51

Yeah, we are on, we are on time today, 10, 20.

2:5:59

Don't try to do.

2:6:00

download the data, guys. That's not the expectation.

2:6:02

Expectation is just the concept.

2:6:03

You just concept. Now just concept to say, okay, okay, sales data, so

2:6:06

this data, so how do I visualize it?

2:6:09

How we visualize it? How we visualize it?

2:6:11

Student performance data, so how to visualize it?

2:6:13

And then start-up data are how to visualize it. That's it.

2:6:16

This is more of a more of a home exercise.

2:6:18

So if it's time, I'm just asking you to kind of, you know, give it a glance and see.

2:6:22

But it's more of a more of a homework kind of thing that I intended.

2:6:26

Every class, I will try to give you some of these small, small case studies so that people can

2:6:29

go back and you have enough time to practice. That's the idea.

2:6:34

Take it.

2:6:52

When we will do project, where we do visualizations or analysis?

2:6:57

Yeah.

2:6:59

what a real world project is, you know, you have got like a data set.

2:7:03

So we'll be giving a raw data to you.

2:7:06

That on up, you have to take the data.

2:7:08

You have to understand your data. Dot head, dot info, dot describe.

2:7:13

Now, tell us how many missing values.

2:7:15

What columns are?

2:7:16

What columns are?

2:7:17

five columns. And that five columns, like you're in Cagle in Cagle in to

2:7:20

say, okay, in Cagle in everything is given to you.

2:7:23

So if you go to Cagle, it's already telling you,

2:7:25

that this number, this date, and how many unique values are.

2:7:29

value counts, right? So Cagle in mostly it is all given to you. But you can absolutely

2:7:34

look at this data and you can figure out what type of insights you can get from this data.

2:7:41

So that is the thing, definitely. So that is the first step of any data analysis task.

2:7:46

You know data for data to say, data the issues are outliers. And see, this is, that's why I say a lot of

2:7:54

it is based on domain knowledge. This may actually, no syntax need. If you're going to say, sir,

2:7:59

some magical methods, which we can do it. No, it is all based on common sense.

2:8:04

The first thing that I started with, right? So you would have seen how I drove my session today.

2:8:08

I was always relating it back to the business. So Python's aspects

2:8:12

is quite come and it's quite come going forward as we get deeper into the classes. The coding and the

2:8:19

programming part is, I would say, a very small part. People often get confused and nervous,

2:8:24

that, sir, this code is, but actually the coding is just a

2:8:28

how do I say? It's like a language. It's like you speak in English, in Hindi. It's just like a language.

2:8:35

And ultimately, you're solving a business problem. You have to always understand from the business sense,

2:8:40

what are we doing? Like, IPL example, or baseball example, I gave you that money ball example. So that is where it all starts from.

2:8:49

What are we trying to solve? Like this is students' performance.

2:8:53

This when you're you, when you're going to take, the first thing that will come to my mind is not,

2:8:58

bar chart, not that we're making, that we're trying to do. And nobody

2:9:05

will tell you that. Definitely in the classes, I'm what we'll give you projects. We'll give you

2:9:11

projects. We'll tell you, please solve this question, solve this question. But you have to be so good

2:9:16

that you have to reach the level where looking at the data, you are able to frame your own

2:9:22

questions. Like how I gave you some examples. Like can you? How I gave you some examples? Like can you

2:9:28

you find out that whether a person's parental level of education has any impact on math

2:9:35

school. But certainly? Not very difficult. What can't? How can't? You might have a hypothesis.

2:9:42

If if parents are educated not, then, then it's, if a lot of parents educated not? So, it can't be

2:9:46

educated not be. Batcha educated not be. Maybe, maybe at a government level,

2:9:52

some survey going to, that, okay, is it true that if parents are less educated, they,

2:9:57

probably discourage their students from attending school or college and that's why the

2:10:02

scores are lower. Could be. Could be. That's a very obvious pattern. Okay? So can we prove that?

2:10:10

Can we prove that? So, um, interesting point. So, you're in x-axis. So, you're

2:10:16

a parental level of education, you know? See, everything started with the business problem.

2:10:22

We're the first data to see, the problem to solve what? And then we're going to do it?

2:10:25

And then we go back, bar chart, these up, you do parental education,

2:10:30

and why access, you take score? And you can do, that if you're parental education low,

2:10:37

I mean, it's, yeah, high school, maybe the parents only went up to high school,

2:10:41

this is high school, so score is a lot. If parents' master's degree, if the parents themselves

2:10:46

are highly educated, so you, if you go to score is it. So, you go to score is, so,

2:10:50

the child is very educated. So whatever, I mean, that may not be true, but I think,

2:10:55

The patterns are also very obvious. If you look at a general survey across all Indian,

2:11:01

you know, big businessmen, up there. But I'm just giving an example, right? If you look at

2:11:08

their schooling, you look at the kind of colleges they attend and all, right? So that's very different,

2:11:11

right, compared to maybe a normal person. So they say, my father is not Mukesh and Banai, right? So,

2:11:16

like, we have all grown up in normal families, like most of us probably, right? So that's the thing.

2:11:21

So, yeah, so you can probably do a small survey.

2:11:25

parental education or parental background, say, what is the pattern. So this is the kind of

2:11:30

bar chart that you will get. So this is your bar chart used to go. Okay,

2:11:34

the x-axis in a category, y-axis is a number. So same, here here, scatter-plot

2:11:39

here. Scatter-plot, yeah, it would be. Scatter-plot, yeah, it would be. Very interesting. And

2:11:45

it's a correlation not going to, it. It's very interesting. Maths are a different skill, reading

2:11:48

is a different skill, right? Reading, is a different skill, right? Reading, meaning,

2:11:50

I mean, if someone, a English is a good, which has reading skills

2:11:54

are not necessarily, they're related. Not necessarily, and this is very interesting.

2:11:58

Now, you'll plot to you, which you'll see what you'll see. It's necessary

2:12:02

not, that if somebody's match score is good, it's, it's not there are a lot of people

2:12:07

who are very good in aptitude and maths and quickly solving problems, but

2:12:10

their reading score is a lot. So this positive correlation

2:12:14

not will. So that's the kind of inference you can get. See how I'm starting with the problem,

2:12:19

I'm starting with the business, the domain.

2:12:20

things to understand. And then we are getting it to Python. So Python is a very small part of

2:12:26

the analysis. Okay, right? Now, like I've forced versus sixes here.

2:12:31

Now, now, what, chocka, what is, people should know. If some of you in this class doesn't know

2:12:35

cricket, then it's different. So, he, it's true. It's not. It's not. It's not. But the same way,

2:12:42

if I go to baseball, a baseball is a very popular game in USA. In India, in India, in baseball,

2:12:47

I don't know. Baseball, yeah, who plays baseball in our country. So now that's what it is.

2:12:55

If I give a baseball data set to you, you what you can't do that data to take? Same way, this is,

2:13:01

this is again part of your analysis. You, you take IPL data set. And I, and I'm very sure you guys

2:13:09

will be fascinated with this data set. You'll make this data. You'll make this data set. This is 20,000 to solve

2:13:13

like IPL data. This is 2008 to 2020, 25, all IPL seasons of data. And you can see exactly the

2:13:20

kind of stuff that we have discussed. Match type, innings, batting team, bowling team,

2:13:24

over the ball, how run score was, everything will get. And all these analytics will be

2:13:30

discussed. You can do that. Okay. So this is like, again, I'm sure you've probably heard of Katham.

2:13:35

We'll see, we'll see some more exercises later on on this one. But here on other be columns

2:13:40

which we've not done here.

2:13:42

Ball number, batter, batter position, runs total, how many runs

2:13:46

were, how many boundaries were. My point is,

2:13:50

if you're not

2:13:50

cricket in the way, so you'll

2:13:52

what you'll say, what a striker, what non-striker

2:13:55

are, you're getting the point, right?

2:13:56

All this Python and EDA and bar chart is the secondary thing.

2:14:00

First things first, as I said, if it's from a job perspective,

2:14:03

whichever company that you're going, if Rajasthan Royals is hiring you

2:14:06

for their IPL team, you're getting

2:14:08

you have to get to get, first.

2:14:10

that's the thing. So these are again for your, for your, you know, for your, for your, for your home

2:14:17

analysis, home exercise. So office for day to just go over it. Don't load yourself in the

2:14:22

classroom. I just wanted to give you some little time to understand. Yes.

2:14:27

Ah, absolutely. Arham as, you know, exactly. Ashraf, sorry. Yes. Yeah, we can compare order data

2:14:34

and shift data to understand how much variation. Yes, exactly. Exactly. Very good. Very good.

2:14:37

Order is time pekiya. Shipping is time per whoa. So our various.

2:14:40

You can get some orders in Amazon, what you are you, but

2:14:44

both back in shipping will. Very nice. Very nice. Very good thing. Just

2:14:48

then bar shipping order. Why? Why? Some products you have ordered? Turing in 30 minute

2:14:54

shipping got. And one day in delivery. But there are some products you ordered

2:14:58

that. That's a problem. So Amazon will want to do a logistical analysis and try to identify

2:15:04

that's what product say? There are shipping time. Very good. See how we are trying to solve a business

2:15:10

problem.

2:15:10

First, we're solving.

2:15:12

Then, then we go to Python in this

2:15:13

implement

2:15:14

okay. So that is all for

2:15:17

from my end.

2:15:18

So, yeah, so thank you.

2:15:20

I'll hand it over to Prath from here.

2:15:22

And just to summarize the

2:15:24

conversation,

2:15:27

so

2:15:28

shared is, Neha. Everything is shared.

2:15:30

So these are again the

2:15:31

general things that we have seen today.

2:15:34

The EDA workflow. We have seen

2:15:36

basics of map plot clip, right?

2:15:38

Basics of plot.

2:15:40

like some basic charts we have seen. What are the basic charts of plotly?

2:15:45

Choosing the right chart. Now we

2:15:47

use the bar charts, scatterplot, line chart. We have seen that. And also at a very high level

2:15:52

how to do annotation. How do we analyze different charts? How do we think in terms of a business

2:15:57

problem? So these are a very broad topic areas. As I told you, this continues on to next session.

2:16:03

So the other session is next to next day. It is the continuation. So here we

2:16:07

here we have a real data set take and make. Here here we have

2:16:10

concept. Next, the class will be working on a real data set.

2:16:13

Summary, readiness, plotly. So we're we use

2:16:17

using and we're a big data set to make a big data set for

2:16:19

things. That is going to be the agenda for the next session.

2:16:26

All right. Great. So,

2:16:28

time for the quiz. And from my end, I will

2:16:30

hand it over to Prata. Thank you. Thank you. Thank you all of you.

2:16:32

Once again, guys. Hope you had a good session with me.

2:16:36

And I will see you all in the in the next session.

2:16:40

Thank you.

2:16:42

Uh, Sneha, once again, for, you know, the profile is shared.

2:16:45

As I've mentioned, all these are shared already from my end.

2:16:50

So I've already shared this file.

2:16:51

The only thing that is pending, uh,

2:16:54

because this we have

2:16:54

a lot of us, this I will share. But everything is in the main folder,

2:17:01

okay? Can one of you, can one of you share the link with us, Neha?

2:17:04

Yeah, I'm sure.

2:17:05

Yeah, just, just, just so that we are clear. Okay.

2:17:09

And I think if you can,

2:17:10

guys have a WhatsApp group or something. So,

2:17:11

then it's just share in WhatsApp.

2:17:13

It's hardly takes a second to just save it, okay?

2:17:16

Just save that thing.

2:17:17

So what I'm doing is I'm just keeping all the contents in one folder.

2:17:21

So that is easy for you guys, okay?

2:17:24

Yeah,

2:17:26

but my point is we have to use our own intelligence also.

2:17:31

Now, AI in the AI to do something

2:17:33

if you tell me, accept AI, then we can take a CSB, upload in Germany,

2:17:38

and we can take a CSB, upload in Germany, and that's all

2:17:39

then there is nothing to do only. But I think part of what is making us different

2:17:45

from hundreds and thousands of other people are that we are learning the concepts.

2:17:50

Now, company ultimately, that's the value is. Now, if you're telling me that there's

2:17:54

Germany, then, then, then, then, then, then why will they hire you?

2:17:58

It's got to be getting it right. Yeah, but there's a balance. I'm not saying that you should

2:18:04

never use it, but I'm saying that you have to balance may use can be.

2:18:07

I mean, what the concepts you have to understand.

2:18:09

Coding map, I use that. I encourage that. That is, that is actually my method of teaching and because I work with so many enterprises, we interview a lot. That is our method of interviewing also.

2:18:20

We encourage you to understand the concepts well.

2:18:23

Then if you have to use for you. No problem.

2:18:26

Python code you don't have to memorize, but concepts, you should. You should, you should know the concepts what we are doing, right? Yeah. Thank you guys. Thank you. I will take your leave now.

2:18:39

Yeah. Thank you, sir. I am going to be releasing the feedback poll now, students. Please fill the feedback pool and then you can join the Menti meter quiz.

2:18:54

The feedback pool should be live now.

2:18:58

I'm also sharing the link of Menti meter quiz in the chat and I'm sharing the screen.

2:19:09

About 15 or 20 seconds more till the feedback poll closes.

2:19:39

Please, quickly vote for, like, fill the feedback poll.

2:19:45

I'm seeing two people.

2:19:49

I'm seeing two or three people have still not felt the feedback pool.

2:19:59

That is a way to mark your attendance, so please do that.

2:20:03

And we can start with the 20 meter quiz now.

2:20:07

Share Kauways, I'm not sure what you are saying when you say can't be open meeting in Zoom app.

2:20:21

You have it open in your Zoom app, right?

2:20:24

Or you're joining from a browser.

2:20:26

Anyways, fine, I think, for today.

2:20:29

Okay, guys, I'm ending the poll now and I'm starting the Mentiator quiz.

2:20:36

Okay.

2:20:37

Please start joining.

2:20:39

I think a lot of people should be already joined.

2:20:42

All right. Great.

2:20:45

Ending the poll in three, two, one.

2:20:50

All right.

2:20:54

Guys, I'm going to start the Mettometer quiz now.

2:20:58

The problems, the questions today are also relatively easy.

2:21:04

There might be just one or two difficult ones.

2:21:06

Actually, just.

2:21:07

one. So good luck. All right, starting now.

2:21:12

What is the primary goal of ADA? So I think this is just to check whether you guys

2:21:26

are actually paying attention in class or not.

2:21:32

The answer should be pretty obvious.

2:21:36

All right, yeah.

2:21:56

So the correct answer is to understand the data structure and the patterns in the data.

2:22:00

Yeah, this is the one.

2:22:02

Cleaning, missing values and building predictive models are not.

2:22:05

models are not the primary goals of ETA. That is, so you have to clean missing values

2:22:11

in order to do EDA and building predictive models is like, comes after ETA.

2:22:17

So, yeah.

2:22:19

Awesome. We are going on to the next question now.

2:22:35

If mean is significantly higher than median, the distribution is likely what?

2:22:49

Just as a quick reminder, median is the value that is if you sort the data set

2:22:58

or if you sort the variable, then the median is the value that sets in the right in the middle.

2:23:04

So for example, if I say,

2:23:05

say I have something, if I have randomly arranged numbers from 0 to 10.

2:23:12

So sorry, not 0 to 10, then 5 will be, yeah, yeah.

2:23:19

So this is something I think is Serra has already touched upon a bit, but let me just quickly

2:23:26

show that.

2:23:28

Oops.

2:23:29

Okay.

2:23:34

Let's see.

2:23:35

Let me just quickly show that actually.

2:23:37

So if I have a data set, right, something like this, and this is say 0 and this is say 10.

2:23:49

So somewhere here if it is 5, right, 5 is the main and also the medium.

2:23:57

So this is a uniform data set or it is, you can say it is symmetric on both sides, right?

2:24:02

0 to 5 the same distance as 5 to 10.

2:24:04

But why would a mean higher than median signify right skewed data is because, say, for example, this is the data set.

2:24:17

And the median is always going to be in the middle if it is a sorted data set, right?

2:24:21

So the value here will be the lowest, okay, and here will be the highest.

2:24:29

So ignore the, yeah.

2:24:33

So this is the midpoint, right?

2:24:36

And that is going to be the median always.

2:24:41

Okay. But if you're mean, right, if the total number of values, sum of total number of values divided by the number of values is lying somewhere here, right?

2:24:52

So the data set will look like this.

2:24:55

You see how it is right sided a little bit.

2:25:00

This is the mean.

2:25:03

Yeah. So that is why this is going to be the correct answer. Right skewed. Left skewed is when the median is ahead of the mean or towards the right of the mean. Okay? So all right. I think this is something sir will cover more in detail, but good job you guys.

2:25:33

All right, next question.

2:25:40

Anyone else who wants to join?

2:25:43

Okay, I'm going to start.

2:25:47

No good thing. This was not a left skewed graph. It was a right skewed graph.

2:25:54

Because as I explained, if you still have a doubt, just message in the chat, I think.

2:26:00

Maybe I answered it.

2:26:02

All right. Next question.

2:26:10

Which plot is most suitable for detecting outliers visually in a single variable?

2:26:14

Okay. So whether it is a line plot, histogram bar chart or a pie chart.

2:26:30

You have to find a line plot, histogram bar chart or a pie chart.

2:26:31

You have to find.

2:26:32

the outliers, the extreme values, so to say, visually, and you're dealing with a single variable.

2:26:41

I think I've tried to put as many hints as possible. Yeah, so most of you did get it correct.

2:26:48

It's a histogram. You can use a line plot, but line plot is not going to be most suitable in this case.

2:26:57

Because so line plot will give you the correct answer.

2:27:01

correct answer, yes, but then histogram is going to be a better output.

2:27:05

Yeah, because you can see the extremes.

2:27:08

Like, there will be the lowest here and then highest here.

2:27:12

And if these two bars are like too high, like really high,

2:27:16

and everything else is right somewhere in the middle,

2:27:19

then you will see that there is some problem with the data set.

2:27:23

So that's why histogram is better.

2:27:26

Also, the reason why line plot would not be a good idea is because

2:27:31

with line plot, if there is a high point somewhere in the middle of the data set,

2:27:36

you will have a, you will be seeing a line sloping from the low point to the high point.

2:27:41

So it will be like a triangle and that makes it a little difficult to see the exact outlayer.

2:27:48

And in that case, histogram is a better option.

2:27:52

That's right.

2:27:54

Alright, so we are seeing fairly mixed.

2:27:59

Some people are able to.

2:28:00

some people are able to answer correctly some questions and others are able to answer other questions correctly.

2:28:06

Great. It seems most of you were paying attention though. So good job.

2:28:12

Anyone who wants to join?

2:28:14

Alright. Yeah, okay. I can start the next question.

2:28:20

Last question?

2:28:24

Oh wait, this is the second last question.

2:28:30

Which feature makes Plotley superior to Matplotlib for dashboards?

2:28:34

Or, well, you can say instead of dashboards, you can also say EDA.

2:28:40

Remember I'm saying Plotly superior, so I'm not talking about large quantities of data.

2:28:48

Because Plotly is, plotly gets a little slower when you're dealing with very large quantities of data.

2:29:00

Awesome, awesome. Yes, interactivity is the correct answer and most of you did get that correct.

2:29:06

So we're going to move on to the next question.

2:29:09

Oh, this is like people are really answering, there's no one clear winner who is able to answer all the questions.

2:29:28

Interesting.

2:29:29

Interesting. Okay. I think there was a 15th player also. Should I just start?

2:29:43

Last question guys. This one is slightly tricky as is tradition.

2:29:59

Okay, so you are like comparing a revenue side by side of, say, for example, two products.

2:30:12

The important point is which part is best?

2:30:15

Obviously, all of these charts you can use and you can get an idea, but there is one best answer.

2:30:23

Awesome. Awesome. Amazing.

2:30:28

Yes.

2:30:29

chart is going to be the best option for comparing revenue across products and not histogram because we are comparing when we are there are multiple variable there are multiple products so we won't be using a histogram in that case and scatter plot and line chart of course you can use them

2:30:48

scatter plot is going to be showing you like a cloud and unless you know how to interpret it well it's going to be a little difficult bar chart is usually the easiest to explain

2:30:59

in the this revenue comparison. So that is why our chart is the correct option.

2:31:05

All right guys. With that, we are at the end of the session.

2:31:10

Let's just see the leader board.

2:31:17

All right, I think Farinder might be, yep, Ferender has won this one. Congratulations.

2:31:26

And with that, we are going to end the session.

2:31:28

we are going to end the session. Thank you so much guys for joining. Have a good night. We'll see you in the next session. And I hope your exam, evaluation was well. It went well on Sunday. You have another evaluation, so I hope you guys are prepared for that. Okay? Good luck. And yeah, please keep your doubts ready for the revision session that will be happening on Thursday.

2:31:58

more doubts you raise to me in advance, in advance would be better.

2:32:03

If you raise it in the class, that is also fine.

2:32:06

The more doubts you raise, I will be able to answer them clearly.

2:32:09

Okay? Do get all of your doubts and problems solved.

2:32:13

All right?

2:32:15

Okay, guys.

2:32:16

See you, see you on Wednesday.

2:32:19

Bye bye.

2:32:21

Good night.