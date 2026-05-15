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

Hi,

15:40

Hi, uh, very good evening

15:43

Good evening, everybody.

15:44

We'll be starting on here.

16:06

Good evening, everybody.

16:10

Good evening, everybody.

16:36

into my folder. So I've already uploaded this for all of you. There it goes.

16:43

All if you can please take the contents from here. And I'll be talking about this today.

16:53

Just to give you a little bit of brief, I think some people are still here to join. Just

16:58

waiting to check if everyone's joined in.

17:06

And guys, this is one more, like, humble, humble request to all of you, like, please try to join everybody on time.

17:18

So I know most of you, all 25 of you are still here, but, but I really hate to keep you guys waiting.

17:26

So just let's ensure we all start on time and that way we can also end on time.

17:30

So one of the things we are really trying to do at Masai is to make sure we stick to the timings so that if we start on time, we can

17:36

can end on time. And again, it's just my request to everybody that please be on time. Again,

17:42

most of you are, but I think some people are still to join. So anyways, so. Okay.

18:06

So, guys, just to kind of give you a little bit of context in terms of what we'll be covering today, this is the overall agenda of the session that we are going to be doing.

18:18

Last session, we spent a lot of time discussing what is machine learning.

18:22

We talked about machine learning, supervised learning, different types of ML problems, what is a regression problem, what is a classification problem.

18:31

So we spent a lot of time in the last session discussing about all those pieces.

18:36

this session, today's session will be getting, you know, getting a little deeper into data cleaning.

18:44

And why is it important? Because if you look at a typical machine learning workflow, it is very important that we take the raw dirty data, we clean that data, and then we can build machine learning models using that particular clean data.

19:03

So that is where data cleaning is a lot of.

19:06

a very, very important step in this particular puzzle.

19:12

Right? So you all work with basic data frames in the initial part of our session, right?

19:18

So we talked about Pandas data frames and you are working with CSV files, right?

19:23

even in our last few sessions, we were working with MatplotLib, Lib, C-Born, a little bit of Pandas we worked on.

19:31

And if you remember the kind of data sets that we used, there could be multiple issues in the data.

19:36

oftentimes you might have some values which are missing, you might have some data points which are outliers, which are, you know, which are not in the right context.

19:48

So a lot of those kinds of issues will be there overall. Just give me one second, guys.

20:06

Sorry for the introduction. So it's very important that most of the times this data will be in different, different formats, right?

20:17

So if you talk about, we might have, we might have integers, we might have data which is in a string type of format.

20:24

We might have some data which is in a, which is in a text kind of format. We might have, let's say we have a salary column.

20:30

And for some reason, the values are coming in negative. So these are some real issues that might be there in the data.

20:36

So these are some of the things that we will have to do.

20:39

We will have to take the data set.

20:41

We load the data sets.

20:42

We have to spot what's going wrong.

20:44

You have to find missing values.

20:46

Oftentimes your data can contain missing values.

20:49

So how do we handle missing values?

20:51

How do we fix missing values?

20:53

In your Panda sessions, you might have done, you might have used a function called Phil N.A.

20:57

So we'll see how we'll see.

21:00

Removing duplicates.

21:01

Your data can have duplicates.

21:02

So we'll see how to remove some duplicates.

21:05

Converting text into.

21:06

numbers because remember machines cannot handle text data everything that we are doing

21:11

in the world of machine learning it is always in the form of equations and match. If you relate

21:20

back to Monday session, we discussed about that beautiful example, no x, y combinations

21:26

1.2, 3 comma 4, 5.6 like that. And we were able to build a mathematical model which is y

21:33

equal to x plus 1. So we are able to see that.

21:36

So everything is in the form of an equation. And because everything isn't the form of an equation,

21:42

it machines will inherently always work with numerical data. Machines will always inherently work with

21:50

numerical data numbers. Numbers are what we are discussing. That's the intuition. So if you,

21:56

if your data is not in a numeric format, imagine we have a city column, right? We discussed these case studies

22:04

in our last course. We did that Matplotlib, the data visualization course, right? And we had a

22:09

region column. We are a city column. Region of values, what will be north, east, southwest? This

22:17

regions are right? What do you do with that? How do you frame an equation with a, with something that is

22:24

not a number? If your value north, then what do you do? Two into north? You cannot, right? So we have to figure

22:30

out ways to convert that into a numeric format. We learned some methods.

22:34

there. Scaling numbers so that they are on the same level. Oftentimes you might have a

22:40

column and the values will be in very, very different scales. Some will be very high, some will be

22:46

very low. So how do we get it in the same scale? So all of these things will need to be done. And finally,

22:54

we'll talk about another very interesting thing called, you know, data leakage. That is exactly

23:00

what is actually talked about here. Making sure our cleanup doesn't accidentally change.

23:04

cheat the model. I'll talk about something called leakage here. We haven't seen that yet.

23:08

And this is how we start from a completely raw, dirty data. And we get towards a clean data

23:14

by performing all these set of steps. We'll see the comprehensive case study today. And once we have

23:21

that clean data, everything else is still the same, what we talked about. Input output

23:27

combination, X, Y combination. And based on that, you will build the model. So, so this is the

23:34

big picture idea of what we are getting at. Okay, overall. And one very important term that we

23:41

tend to use in machine learning in the real world, I wanted to just share with all of you here. It's called

23:47

garbage in garbage out. So garbage in, garbage out. This is the term that you will basically

23:57

hear a lot in ML. And why it is important is because if you again recall the discussion we had on Monday,

24:04

the ideas of supervised learning that we talked about are because supervised learning

24:08

maybe we need to have x and y clearly defined input output combinations x y combinations right

24:15

so if your data but if this input output that data itself is not in the right format then what

24:27

models will you build other data i think may so whatever models and whatever relationships you learn on the data because

24:34

What was the crux of Monday? Data is nothing but this, right? On this data, I will use some algorithm.

24:42

I will use some algorithm and based on that, I will build a mathematical model.

24:47

So I will have the data. I will use some algorithm. And based on that, I will end up building a mathematical model,

24:55

which is nothing but the rules or the equation or the function that we talked about.

24:58

If your data is wrong, so the function being wrong.

25:04

That's why it's very important to clean the data.

25:06

Get it into the right format.

25:08

If this is wrong, everything else downstream goes wrong.

25:11

Which equation will be that's why it is such a critical phase.

25:16

And usually data scientists spend a lot of time doing data cleaning and data preparation.

25:21

Model building is usually the easiest step.

25:24

Because if you, if you're our data ready got, building the models is very easy.

25:29

And we will take a step into that from next week onwards.

25:32

Next week onwards, I'll see how to do.

25:34

do regression. Monday, we're a little quickly, because Monday's session was not a practical

25:38

session. Today is a completely practical session. Monday was not meant for that. Monday,

25:42

the whole session is theory taught. But so Monday, we've, we've had to help to build a classification

25:49

model. But next week will be totally on that. Next week will be, so we'll see that in more detail.

25:53

So today, data cleaning, we will get our data ready. And from next week onwards, on that

25:58

data, we will try to build models. Regression models will. And next to next week, classification models

26:03

that's the flow. Now, moving on, let's get into this step by step by step.

26:10

Let us see this. And I'll take you back to my notebook now. And you can all follow along with me.

26:19

You can all follow along with me. Then you might, it might be confusing. Just follow along with me.

26:24

And you can always try out the notebooks later on. Side side may if you want to do it up up. But I would

26:31

suggest just follow along with me.

26:33

Now, first thing, we are importing Numpai and Pandas. That is the first thing we are doing.

26:38

And here are three data sets that I'm taking.

26:43

Okay? Okay. So, first we're discussion

26:44

sure we'll DF underscore car data sets again. So I'm just creating some sample data search.

26:51

I'm not taking anything massive today. We can see that in more detail next week onwards.

26:56

Next week onwards, when we're, when we're, when we are trying to learn the methods.

27:01

So, we are trying to learn the methods. So that, I've taken simplified data.

27:03

datasets to explain the topics to me. So I've created a sample data set called DF underscore

27:09

car. I have created one more sample data frame called the DF underscore student. It is to understand

27:15

student performance and it's how marks who are, kind attendance, how great, like that. And we have created

27:19

another sample data set called DF underscore Eta. So first I want to analyze DF underscore car. Yeah,

27:26

it's a Panda's data frame, right? Yeah, so I think it's very obvious what the data contains.

27:33

I have to walk you through it. First, you have the brand, then the year of manufacture. What is the fuel

27:39

consumption type? What is the number of kilometers driven? What is the number of kilometers driven? And

27:45

what is the price of the car? This is your features. Brand is year, fuel, is, kilometers driven, or price? These are the

27:52

features we have right now. Similarly, we have DF underscore student. This is your student ID. Marks,

27:59

from, attendance and grade here. So student ID is. So you are. So you are basic. So you are basic

28:03

tracking the student's performance. Let's say we will be doing something like this at Maasai also.

28:08

For every student, we will have an ID. We will know how much of marks you got in a particular

28:12

exam. We will know your attendance based on how people are attending the live classes. And we will

28:17

also know your grades. So this is the kind of information that we will be maintaining internally

28:22

at Massi at a much larger scale because we will do a lot of analytics based on your class

28:26

participation and X Y set parameter, so many things, right? So. And finally,

28:32

we have a df underscore ecom where we we have a very simple sample e-commerce data

28:40

e-commerce data is where we have the order ID we have the product we have the quantity and we have the price

28:45

you have got you know data sets so okay so subsequently i will start my conversation with the car data set

28:50

this is what i'm going to focus on to start with you get a car data set is what i will focus on now

28:55

now so these are some general things that

29:02

you know we have been discussing already in our panda session so

29:06

so first first thing you do one of the first things you should go back and do is you should go back

29:12

and do a dot head this is this is this is simple data

29:16

but in in a more real world scenario what you should do you should go back and do df.

29:21

head here we've made full data to display here we display is also a very popular function we use

29:26

and this from we'll know what data in what does this data look like okay so what are the

29:31

the issues you are able to see so first there is a there is a nan value there is a nan value

29:36

in the particular uh kilometers driven column and what does that mean what does that particular

29:42

nan value actually mean the nan value actually means that the nan value particularly

29:46

means that we it is a missing value so we have information about all the other cars but the nan

29:53

means a missing or unavailable value in that particular column it means the kilometers

29:57

driven entry for that particular car is missing or which

30:01

any reason maybe the odometer where your kilometers

30:04

where you can't maybe it malfunctioned or then

30:06

or then we have reading we've seen right or the device

30:09

reading that's wrong or whatever they can be any number of reasons

30:13

or then under the reason could be you know we are we are trying to measure the

30:17

kilometers driven but you can't

30:19

now you can't let's say before you collect the reading

30:24

the car owner they have they reset

30:26

this is like a resale data set you're looking at kind of a secondhand

30:31

or second-hand car market where people are trying to sell their cards so when you're listing the car on the

30:37

platform you know, that's the car in the car in the car

30:39

way that so this is the you know this is more like the real world use case of this if you want me to

30:43

give you an example uh a used car marketplace a very good example will be spini.com

30:50

spini.com will be a great example

30:51

spini is very nice you know it's very nice i have also personally purchased a car from here

30:56

also good very reliable i think they're they're the startup company and fairly fairly fairly

31:01

good i think i think this this particular uh second-hand market is only going to grow and i

31:09

i i personally see a lot of analytics getting used in this market particularly because second-hand

31:14

a second-hand a market is where trust is very important and having the right data and parameters

31:18

are very important you're how you evaluate kind of the cari's right or product's right

31:23

this is a laptop electronics so i think this is a huge huge place huge huge market over on and they are

31:29

trying to get it right so whenever you see you see

31:31

people are uh let's see you want to explore some cars you can see how people list cars

31:40

right this is how the people will list the cars and this is how you have to explicitly give kilometers

31:44

driven so whenever you so let's say these are people who want to sell their car so you're

31:48

your car you're going here here okay sort by uh low to high we can do okay and you can take a look at it

31:54

you can take a look at it what are the cheapest cars available right now and people will have to

31:59

list out people will have to explicitly list out

32:01

what is the you know what is their the overall kilometers of what is their overall

32:07

diesel all that so i think this has to be very very accurately listed okay

32:14

and here here there's a kaii khani kind of a very different conversation but if they you know if you

32:20

asked me uh we discussed about regression on monday

32:25

we've made monday we discussed on monday discussion discussion discussed

32:28

so if i have to give you a beautiful example of this spinning is also using regression

32:34

to estimate the car price how about that so this this particular car price is predicted on the

32:43

basis of regression mortgage so so uh you can take a look at it here here what is spinny basically

32:50

doing they are looking at all the different parameters of the car so basically umka studio

32:55

is that the car and they try to look at a completely 360 degree image of the car so basically

33:03

he has car's the whole image here number one they will have the image of the car number two they will

33:09

have the normal features of the car registration come manual have third-party insurance hey whatever

33:14

rto where's what location what is it's up there's a part part of it's there's a part part of it that

33:19

if you're a tier two three or three city's carri is compared to a tier one city carri is it will

33:25

I'm just telling you what the features will be right quality report are now

33:29

core system supporting interiors AC exterior lights they will measure they will give us

33:34

for everything so based on all these scores and you say this score

33:38

can't say this score how can't you because score is all pictures are now

33:42

look if i go a little deeper they will also give you they will also give you an idea

33:48

about the different problems in the car now look here here here

33:53

very interesting they will tell you what the vr and tier is

33:56

it now vr and tier here has

33:58

kaha defect they're kind of

33:59

problems here you'll be able to see that as well right

34:03

and based on all of these parameters they are trying to estimate what is the

34:07

what is the what is the price of the car

34:09

other going to dent there

34:11

scratch he will say you see

34:15

very interesting and the reason i wanted to show you is because

34:17

this is a real world thing this is actually getting used

34:20

they are looking at the surface area of the scratch

34:23

you see here here there's a little scratch here so you know what they do behind the

34:27

scenes they are trying to measure what is the surface area of the scratch

34:31

image data set when we go to the world of computer vision

34:35

we're a technical term used that they call segmentation so

34:38

segmentation use and they try to find out

34:40

that these these scratches can be find out what is the surface area of the scratches

34:46

this is your feature is like a feature this is like the feature for this particular car right

34:53

and based on all of this you are trying to predict what is the price of the car

34:56

this is a surface area. If the gari's overall surface area, let's say is some meter square or some

35:03

feet square, so then you're trying to measure what is the surface area of that particular thing?

35:07

Some percentage in scratches measure. Scratches is different, dent is different,

35:12

glass crack is different, windshield crack is different. There are different different

35:15

different categorizations of cracks you will have. But anyways, so what I'm getting at from a big

35:21

picture idea is, you know, this is this is.

35:23

exactly what Monday's class was on and I'm again repeating this because it's so important.

35:27

The techniques, though, we'll keep learning new things, but what I really want you to get

35:33

comfortable and get very confident about is when you go to any real world problem,

35:39

okay?

35:40

Now, real world aspect in things. That's what I try to do a lot in my classes.

35:44

So when you relate to real world problems, can you frame it as an ML problem?

35:48

So here here your x-1 is the picture. Your x-1 is the picture. What is the image of the car?

35:53

Okay, X2 will be like, you know, your features of the car.

35:58

Like, for example, what is the year?

36:00

Year of Manufacture.

36:01

What is X3?

36:02

X3 will be like the fuel type.

36:04

Fuel type, what is X4?

36:07

X4 will be, let's say, for example, you know, what are the scratches, dense and scratches in the car?

36:14

That is your export.

36:15

These will be all the different, different features of the car.

36:18

And based on all of these parameters, you are ultimately trying to predict what is the car brands.

36:23

That is what you are trying to do.

36:24

So that makes it a regression problem.

36:27

Now, I'm going to say, sir, model to train because you already have a lot of historical data

36:31

which you have used to train the model.

36:35

This is the big picture idea.

36:36

So Spinney also has this massive equation.

36:38

If you think about it, they will also be having this massive equation that they have built

36:42

behind the scenes, Y equal to something times X1 plus something times X2 like that.

36:47

And next time a user uploads a picture of a card based on the different different features of the card,

36:52

the model.

36:53

will predict what is the price of the car.

36:56

So this is just a very small practical thing I wanted to share with you.

37:01

So asai-cues data set we have here.

37:03

So whenever you see any data set, it can that it's an automator reading there.

37:06

We're going to nan.

37:08

So now what we will do, we will have to investigate this data and we'll have to impute the missing

37:14

value.

37:14

I mean, missing value include the moving.

37:16

So let us see that.

37:17

Let us see how we can go back and do that.

37:19

So fixing logically incorrect values.

37:22

So we're how to do?

37:24

Okay, if you're car data set, this nan here, okay?

37:29

That is one issue.

37:30

What other issues are we able to observe?

37:31

Let us first investigate the issues.

37:33

The first step, we have to investigate the issues.

37:36

Number one issue is kilometers is, kilometers driven is nan.

37:40

What is the other issue you are able to see in the car data set?

37:42

Friends, anybody?

37:44

Are you able to spot any other issue in the car data set?

37:49

Or what are you looking you see in the car's data set?

37:52

Anybody?

37:59

Yes, very good.

38:00

Price is negative.

38:01

Very good.

38:02

Price is negative.

38:03

This is no, it's not going to be.

38:05

Very good.

38:05

So this is the kind of thing that you will have to do.

38:07

Whenever we work on real problems,

38:09

you will have to,

38:10

you will have to question, is it even possible?

38:12

Can price negative be?

38:13

Not can't.

38:14

So this is an example of a logically inconsistent value.

38:18

It is not possible.

38:20

So missing value is an issue.

38:21

And this is a issue.

38:21

And this issue is price negative.

38:25

And there can be multiple reasons for this.

38:27

One reason could be,

38:29

that you know,

38:29

prediction by mistake,

38:31

it could be.

38:32

Whatever reason the prediction is,

38:33

you know, went wrong.

38:35

Number one.

38:37

Number two, the price is coming out to be negative

38:39

due to other factors.

38:42

But it's a, it's a problem.

38:44

Now let's look at the student data set.

38:46

D.F. Under suppose, student, our dosra data set.

38:48

Second data set.

38:49

What are the issues in this data set?

38:51

It is similar, similar order.

38:53

Right?

38:54

You can see, here here on the marks is NAN.

38:57

S-03, I don't know the students' marks missing.

39:00

NAN is, NAN stands for missing value.

39:03

Right?

39:03

I'm sure in Python, you have already seen some instance of NAN, right?

39:07

NAN stands for missing value.

39:09

But we don't know what it is.

39:12

Whenever you see this,

39:13

if you question to ask now, okay, why is it missing?

39:16

Student's value of missing, why is that particular value missing?

39:20

Could be any number of things?

39:21

reasons. It could be with, you know, they said a student was absent. So, everybody else wrote

39:27

the exam, that particular student did not write the exam. That exam was present in it. So,

39:31

what's what marks did? Or then, other thing be

39:35

that the student wrote the exam, but due to some glitch in the system, teacher in

39:42

the marks update here, but the marks did not get updated to the database.

39:47

Again, any number of details. Number two, we have a logically inconsistent value, which is,

39:51

is grade, minus 10. Now, grade is supposed to be A, B, C, D like that. You minus 10

39:57

how can't. So this is the way how you try to spot issues in the data, and that is the reason

40:03

why it takes a lot of time. But it's just there's no tools, you have to manually

40:08

do it. Yeah, you can write some commands like you can go back and use a described method, all that you

40:13

can do. But you will ultimately have to use your domain knowledge and your intelligence and your

40:19

understanding of the business, your understanding of the domain.

40:23

Let's see our student data set.

40:24

We have some of it.

40:25

We have to say, what are we trying to analyze?

40:27

So based on that, we have to say, okay, this is some issue in this data.

40:31

And finally, the ecom data sets, e-commerce data set if you see, we have a particular, again,

40:36

a nann value, and we have an inconsistent value, which is minus 5.com.

40:40

Now, how do we fix this?

40:44

What are we doing?

40:45

We must fix the impossible values manually.

40:49

Right? Exactly. Exactly. That's what we are discussing here.

40:53

So, car case, what are we doing? And again, I want to clarify one thing.

40:58

I might be using some methods. That method may be right, may not be right. There is no one

41:03

correct answer for this. And that is one thing I want to just stay out right. And see, whenever you

41:08

work on real problems, whenever you have real world use cases in make, you will see a lot of

41:13

scenarios when these kinds of questions will come at the back of your mind.

41:16

Is this the right approach? Are we doing it in the right way?

41:19

you will have a lot of these questions that usually come up.

41:23

So the approach that you follow can be completely different from the approach I follow,

41:28

because your reasoning might be different.

41:30

As long as you are able to explain,

41:33

if you're able to explain, you're fine, please keep that at the back of your mind.

41:37

So if you ask me, sir, how can't handle this, what am I doing?

41:41

I am simply converting this from absolute value.

41:44

That's it.

41:46

Python may ABS function.

41:47

All of you know there's an ABS function in Python.

41:49

So ABS functions and what we can do?

41:51

We can convert this into, we can convert this into a positive, a positive value.

41:58

We can, we can use the ABS function in Python to convert it to a positive value.

42:02

You can see that.

42:03

And that is exactly what we are doing in the, in the code here.

42:06

So we are seeing DF car price.

42:08

Not aBS.

42:10

Okay, we can, we can, if I, if I do this for you, this is my DF car price.

42:18

And you can clearly see.

42:19

that this is a negative value, right?

42:23

But the moment I do a dot abs, dot abs stands for absolute value.

42:29

It is a function that returns the absolute value of the argument.

42:33

Absolute value of the absolute value of what is?

42:35

If negative, then sign huddered.

42:39

Positive numbers will remain positive.

42:42

Negative numbers will become positive.

42:46

I repeat, what is absolute value?

42:47

So negative numbers will become positive.

42:51

Positive numbers will remain possible.

42:53

That is absolute value.

42:54

So when I run the code, you will see minus 20,000 will become 20,000.

42:58

That is exactly what I'm doing in the code.

43:01

And I'm simply replacing DF card price with that.

43:03

That's it.

43:04

That is the way how we are working it out.

43:06

That's the intuition.

43:07

I hope everyone's alive.

43:09

Now, again, you will ask me, you know, sir, sir, what is?

43:15

So what is the approach that we are, excuse me, what is the approach that we are kind of,

43:22

uh, uh, so is this the way we will do it?

43:26

Are we going to go back and, you know, use the absolute value method?

43:32

Is this the way we will be doing this?

43:34

Well, up to you.

43:36

I'll say, then minus 20,000, galat value.

43:38

We'll us to hathen.

43:39

It's fine.

43:40

It's up to you.

43:41

This is one approach I'm trying to share with you.

43:43

Could be that while update.

43:45

in the system, that's 20,000 to get minus 20,000 update can be. That is the reason I'm using

43:49

absolute value. But some of you in the class can question me. Some of in the class can also,

43:54

you know, go back and, you can go back and question me. That is it, is it possible? Is it possible

44:04

that, you know, that this value itself is incorrect? It is absolutely possible that the value itself

44:12

is incorrect. Probably value incorrectly.

44:15

G, it's incorrect. So then, then that is also a possibility. The value itself is incorrect.

44:20

So in that case, what is what I will have to do? I will have to go back and drop that entire record.

44:25

Maybe the entry itself is incorrect. Either I drop it or I replace with absolute. That is completely up to me.

44:32

So that's what I said. The approach is completely up to me. Okay? Here. Here we have what we did?

44:37

We're only absolute answer replaced here. Second, coming to DF underscore student grade.

44:43

Okay. DF underscore student grade.

44:45

What am I doing? I'm replacing minus 10 with np.

44:50

Because minus 10 is not a possible grade.

44:54

This grade possible not. You cannot have a grade which is minus 10.

44:59

So now what will I do? So what will I do? This we'll

45:01

here. Here we can't absolutely. How else not we're going?

45:05

That's not. No, no, grade. I don't know the grade. I don't know the grade.

45:09

So the moment you have this kind of a thing, it is as good as unknown. I don't know.

45:15

minus 10 may be. So for the time being, whenever you see these kinds of issues that

45:20

do not make sense, you try to handle it like what we did here. You try to handle like what we did here.

45:27

Otherwise, what you do? You simply try to replace that with npdnpdn. That is exactly what I'm

45:32

doing in the second use case. I'm simply trying to replace that with npdnpdn. And the third use case,

45:37

we have df, ecomprice.abase. And we're replacing that with this. And now let us see the fixes that we did.

45:45

You can see car, we were able to fix that particular minus 20,000 sorted ABS. NAN is fine. See, NAN is not a problem. We'll come to the missing value part in the next phase. But all that we try to do here is we try to fix the logically incorrect values. Whatever values were logically incorrect, we tried to fix it. Okay. So whichever values were logically incorrect, we tried to inherently fix those values. So the logically incorrect values we tried to fix it. That's it.

46:15

mission. Okay, that's the idea. Similarly, we have DF underscore student. DF underscore student. If you see once again,

46:22

we were able to, you know, replace that minus 10 grade with nal. Because we don't know minus 10. It is,

46:29

it is something I don't know right now. So abicali I have replaced with nine. And then later on in the next phase,

46:34

we will discuss what to help what to do with this. Sorted. And ecom also, if I run the code, we will see that we have

46:40

replaced this negative price with the positive price. So this is how we have done.

46:45

the level one cleaning. Data cleaning is a very iterative process. First you do this,

46:49

then you will have to do something more than something more. We'll see a series of different

46:53

different steps right now. So whatever we have seen here was a very intuitive way of figuring out

47:01

how to clean the data. And we had to use our own common sense. We have to think about.

47:05

Price negative not be positive. Grade minus 10. This is unknown. This is what we had to apply our

47:13

common sense and figure out.

47:15

Okay, something like that.

47:16

Now, I'm going to example.

47:18

Now, now, Ip.

47:19

IPL game, okay.

47:20

A IPL is a match.

47:21

And you have IPL data.

47:24

Every row stands for a particular IPL data set.

47:27

Match level data.

47:29

Match 1 is this versus this.

47:31

It's this.

47:32

This rung score.

47:33

It's 4, 8, this is 8.

47:34

Right?

47:35

Now you tell me, imagine there is a,

47:37

let me draw this out for me, okay?

47:39

So you have a match here.

47:41

This is the match ID.

47:45

This is your match ID.

47:47

This is your number of runs code.

47:50

This is your number of force.

47:53

And it's your number of sixes.

47:56

Okay, or your number of force are your number of sixes.

47:59

Force and success.

48:01

If you take a look at it, each and every row is a match.

48:05

You are tracking number of runs, how force, how six is.

48:07

Now think about it.

48:09

One, number of success is what number of success is.

48:14

I'll give a look at it.

48:15

example to you, I'm an example to you.

48:17

Let's say,

48:19

I'll give an example to you.

48:24

You have a data set.

48:26

We've written that 1216 in match in.

48:29

Can it be?

48:30

It can be.

48:31

It can.

48:32

I mean, no, that's obvious.

48:35

But,

48:36

now, this is the criteria satisfy

48:38

if you look at it.

48:40

If you look at it,

48:41

it's, it's following your criteria.

48:44

This is following your criteria.

48:45

if you're greater than 0,

48:46

negative, not.

48:47

Negative is obvious.

48:48

It's not.

48:49

But this for you,

48:50

you need common sense.

48:51

Now, this, only somebody who understands cricket,

48:54

only somebody who knows the game.

48:57

Now, IPL in B's over,

48:59

and now, is the problem?

49:01

Is it possible?

49:02

Is it possible?

49:03

Is 121-6 as possible in a game?

49:05

No, this is where I told you you

49:07

have to use your common sense.

49:09

A lot of data science is based on that.

49:11

A lot of data science and real world data science

49:13

is based on this particular data

49:15

cleaning. In the real world, your initial data will be in a dirty format.

49:19

That's not right.

49:21

Initial data in these problems aren't.

49:23

You know, there are 121-6s that, you know, you know, is hit in the match.

49:28

So what do you do?

49:30

Is it possible? No, it's not possible because there are 20 overs in a game.

49:35

20 overs, each over six balls.

49:37

I mean, 120 balls are in one innings in.

49:42

Okay, well, well, my mistake is.

49:44

it's my mistake. My mistake. I should have clarified,

49:50

two innings are. So two innings are, so 240 games, you know?

49:53

So, can't 2.401?

49:55

It's not.

49:56

Because 20 overs one side, 20 overs the other side, maximum.

50:00

I'm considering, max to max.

50:03

120 balls. Let's leave out no wide and all that.

50:06

No ball, wide ball, wide ball.

50:08

So, now 240s, there's a shaka no can't have that many number of sixes.

50:11

You can't have that many number of sixes. It's just not practically.

50:14

possible. So these are the logical inconsistence that you have to spot. So if you are solving a problem and if you observe this kind of thing, what will you do? You will replace this with what?

50:27

Your criteria to satisfy it negative. You will replace this with NP. Nan. Nan, this is what I meant.

50:35

This is a grade minus 10 may be. This is a 121. This is a 121.

50:40

You know what?

50:41

the number of sixes are unknown. I don't know. I have to find out.

50:46

So you get the idea. I hope everyone's aligned on this. Now.

50:51

Now we will see the different ways we can handle missing values.

50:56

Okay. What are the different ways we can go back and handle missing values?

51:00

So I just wanted to check in your in your Panda sessions. Did you get a chance to see this thing, fill in it?

51:06

I'm sure you have seen someone to fill in it. Just wanted to check with others.

51:10

Everybody fill in it.

51:11

you? Let me know, guys, all of you, all of you have seen. All of you must have seen

51:17

this kind of code. I will definitely do it again here. But as you have seen, fill an A with mean,

51:22

fill in a with median, right? Okay. Okay. Okay. Okay. Okay. Let's, let's relate to that. Let's

51:33

Let's relate to that. Now, so first, my analysis will be on the car data set. So car data set. So car data set

51:39

what we have? We have first level of fixed. Step by step we are going. Second level,

51:44

we are able to see that the kilometers driven, one of the values is N-A-N. Okay. The fourth row

51:50

in this particular data set is N-N-N-N. That is what we are able to see right now. The fourth row

51:58

in this particular data set that stands for N-N-N-N-N-N-N- is a N-value that we are able to see right now.

52:04

That is the fourth row that you are able to see. That's N-N.

52:09

That's a intuition. Okay. Now, so this is NANN, we've got right now, all of you can see.

52:19

So now the important thing is, how do we, how do we impute it? Right? So we have a missing value right now.

52:27

And now what we have to do is we have to impute the missing value. It is referred to as missing value.

52:39

imputation. Another term that we use for this is called missing value. Missing value

52:52

imputation. Imputation is what is the meaning of imputation in English? In English the term

52:59

imputation means substitution. Substitution, substitute. Impute means to substitute. You have some value

53:08

you are trying to impute or substitute that value with something else.

53:13

This is your imputation point. So we have a value nan. Now we have to figure out a method

53:20

to replace or substitute that missing value with something else.

53:28

Now what are doing? Now whatever methods you have seen, all are valid methods, no problem.

53:33

One of the methods you have done is mean. So first, mean median, so people know. So,

53:38

I can imagine I give you five values, 10, 20, 30, 40, 50. So mean

53:49

the meaning of average? What is the meaning of average? What is average? Average,

53:53

you add up all the values. 10 plus 20 plus 30 plus 40 plus 50. You add up all the values and you

54:00

divide by 5. That is the way how we define average. Okay. So 10 plus 20 plus 30 plus 40 plus 50 divided by 5.

54:08

You take all the values and you divide by 5.

54:12

You add up all the values and you divide by 5.

54:14

That is the way how we define mean.

54:16

So we will do 10 plus 20 plus 30 plus 40 plus 50 divided by 5.

54:26

This is your average over.

54:28

And turns out the average that we are getting right now is equal to 30.

54:33

The average is coming out to be equal to 30.

54:36

Everybody knows the mean.

54:37

Mean, matter of average.

54:38

Now, what is median?

54:41

That means the different color.

54:42

What is median just to summarize the topic?

54:44

Median can mean?

54:46

So, this your five numbers are.

54:48

Can you tell me, guys, what is the median of these five numbers?

54:51

How do we calculate as a median?

54:53

Median what is.

54:54

Five number of median here?

54:56

Tell me, please, write on the, write on the chat.

54:59

What is the median for these five values?

55:08

Okay, very good, 30, absolutely.

55:20

So median I'm calculate how do we calculate median?

55:23

We sort the data in ascending order or descending order.

55:27

We first data sort kind of ascending or descending order in.

55:29

Ascending or descending order and then we find out what is the middle value of it.

55:32

That's that's your median is 30.

55:35

So you sort in ascending order, 10, 20, 30, 40.

55:38

you have five values and you simply try to find out what is the middle value out of these five values.

55:44

So whatever five values, whatever five values that we have right now, whatever five values that we have right now, whatever five values that we have right now, what is the midiate value out of these five values?

55:59

So what is the middle value out of these five values?

56:02

That's the intuition behind the medium. That's the idea. So we have mean and we have minimum.

56:08

Now, coming back to the concept of imputation of the kilometers driven column.

56:14

How do we impute it?

56:16

How do we impute the kilometers driven column?

56:18

So there is a nan value that we see right now.

56:21

And we have to impute this particular, we have to impute this particular missing value.

56:28

We have a nan value and we have to now impute this particular missing value.

56:32

Let's see how we can do that.

56:35

So the code that we are using specifically here is fill N.A.

56:38

DF cars kilometer driven fill an A DF car dot mean.

56:43

So we are calculating what is the mean of that column and we are filling that missing value with the moon.

56:48

Everybody has done this thing.

56:49

All that it means is we are simply calculating what is the average.

56:53

This average what is the average.

56:55

20, 30, 30, you find out the average and you simply replace this with the average.

57:02

This is a very safe way and a very simple way how we are involved.

57:05

computing the value, but I will discuss some challenges with this approach.

57:08

Okay, everybody has seen this basic approach, but this is a good and a very baseline way we can do things.

57:14

But there is a small problem with this approach which I will discuss.

57:16

I will discuss what is the, what is the issue with this approach?

57:19

I will come to that.

57:24

One other thing I wanted to clarify is the issue of duplicates, right?

57:29

Why is it important to remove duplicates?

57:32

See, rig the system by counting.

57:35

the same road twice. So what does it mean to say? If you go back to the conversation that we

57:41

had before, imagine we are trying to do, trying to build a model to predict the car price or predict

57:51

something. So based on some X, we are trying to predict some Y. Okay, you have got to put

57:56

X is nothing but the inputs or the features. So X is nothing but the inputs or the features. So X is nothing but the inputs

58:04

or the features. And based on that, we are trying to predict the output

58:12

Y, which is nothing but the output or the labels. That's what we are trying to do. Okay. So we

58:20

are the inputs or features and based on that, we are trying to predict what are the outputs

58:23

or labels. That's what we are trying to do overall. Okay. Now, if you think about it, we,

58:30

what are we trying to do in supervised learning? We have lots and lots of input, output, or X,

58:34

we have lots and lots of these X, Y combinations like this. This is what we have been

58:39

discussing all this file. Now, if you think about it, if the data is duplicated, if we have

58:48

duplicates, if I give you duplicate data, you can think about that credit default, a study

58:57

we did last Monday, right? If we have two customers duplicate here, same data, same data, if we

59:04

give two times, the model might end up getting biased.

59:09

Now the same example, do you know, right? So if I have to give you a better analogy

59:17

based on whatever I explained on Monday, so you're showing a picture of an apple,

59:22

I'm just trying to give you an exact example of this, and you're saying it is called an apple.

59:27

The next example is exactly the same. Maybe an apple, which looks exactly the same.

59:34

And you're here here, it's an apple. So the teacher is showing the exact same example

59:38

and saying, yeah, be apple and this is an apple. So there is no variety that kid is learning, right?

59:43

The kid will, is seeing that, the first day maybe teacher may be this apple, I'm learning that.

59:50

Second day also teacher is showing the same thing and telling me. So the kid is reinforcing,

59:55

that yeah, yeah, apple. But you're the same example

59:58

are you. You're not producing. So duplicates can create issues.

1:0:04

And this is, this is not the right thing to do.

1:0:06

You should, you should not try to include duplicates in machine learning.

1:0:10

So whenever you see duplicates, try to drop it.

1:0:12

Because the model might end up getting biased.

1:0:15

You, you show it examples of apples.

1:0:17

I have no problem.

1:0:18

But why don't you show an apple like this?

1:0:20

After a rotate kind of, you know.

1:0:21

A psal.

1:0:22

This is where the kid will end up learning the orientation.

1:0:26

Yeah, if a fruit is oriented like this, then we happen.

1:0:29

Not the exact same thing.

1:0:30

So that is what I meant by the concept of duplicates, right?

1:0:33

So whenever you see duplicates, right?

1:0:33

So whenever you see duplicates, the key takeaway, please drop duplicates, always.

1:0:37

Please drop duplicates.

1:0:38

Now, so missing value, as I said, missing values.

1:0:42

The first, missing value in the problem, what is?

1:0:44

This problem is what?

1:0:45

Problem is the problem is.

1:0:46

The problem is that, the missing values will typically tend to crash tomorrow.

1:0:50

If your data in the data,

1:0:53

the same first, you will not be able to do machine value.

1:0:56

You have machine learning carry.

1:0:58

Okay.

1:0:59

You want to see that.

1:1:01

I have an example.

1:1:03

I think it will be nice to see a small example, right?

1:1:06

This is your, this is your, this is your DF car data, right?

1:1:10

And last session we have you co-lab introduced here, so I will generate with AI.

1:1:15

Let's build a basic model, okay?

1:1:17

So, your data is brand, year.

1:1:21

So we have this thing.

1:1:25

Well, let's take a simpler one.

1:1:27

Correct.

1:1:28

So whenever data, whenever your data consists of missing value,

1:1:33

what will happen your SK learned algorithms will not work your SK learn algorithms will not work your

1:1:40

scale on algorithms will just not work because your data is missing and other up

1:1:45

this way model gonna something very similar to how I did it on Monday okay if I if I

1:1:51

if I go back and build my models on this data your models will not work because your data

1:1:54

is missing so that is the reason why you will have to go back and handle the missing

1:2:00

value.

1:2:01

So we talked about mean, we talked about median.

1:2:05

We can fill with median also.

1:2:07

And finally, there is something called mode.

1:2:10

So mode will come very nice for the grade column.

1:2:15

If you're a grade column, you see, you're here here here.

1:2:17

There's now here.

1:2:18

So question is how do we, how do we impute the missing value for the grade column?

1:2:25

Two of the students have got grade A, one student got grade B, one student got grade C.

1:2:30

So, this missing is.

1:2:34

So how will you impute the missing value?

1:2:37

So you will find out what is the mold of the data.

1:2:39

So mode of the data, what the mode of the data?

1:2:42

This grade column is two grades A, two grades A, one B, one C, and this is missing.

1:2:49

That is what you're able to see.

1:2:51

So two of these, two of these grades are A.

1:2:55

One of the grades are, one of the grade is B, one of the grade is C.

1:2:58

and one of the grade is missing.

1:3:01

That is what you're able to see on the screen.

1:3:03

One grade is A, one grade is one is B, one is C, and one is missing.

1:3:07

Nan.

1:3:09

So what is the mode of the data?

1:3:10

Mode is A.

1:3:11

Mode is that particular value that occurs a maximum number of times.

1:3:16

This data, grade's the column is its mode is A.

1:3:22

So I will replace this with A.

1:3:24

It is taking an educated guess.

1:3:26

It is not accurate.

1:3:28

It is not accurate.

1:3:29

I'm again repeating.

1:3:31

There is no perfect way of doing things.

1:3:32

This is only an approximation we are talking about in the class.

1:3:36

Now, let me tell you the more practical way to impute missing value.

1:3:40

Okay?

1:3:41

So, this, shall, go go go.

1:3:42

We've basically lenay here, which you guys have already seen.

1:3:44

So price replaced over, grade mode, so everything is sorted.

1:3:49

Everything is sorted, right?

1:3:50

So you have managed to clean the data at a basic level.

1:3:55

Now what I want to do is, I want to take a small.

1:3:58

small five minute digression and give you an idea of another way you can impute missing

1:4:04

value.

1:4:05

A more practical curriculum.

1:4:06

So that is not in the curriculum.

1:4:09

The curriculum focuses only on the field and a part.

1:4:12

That's all that we are looking at it right now.

1:4:14

But now let us understand a little bit about how else we can go back and impute missing

1:4:19

value in practice.

1:4:21

So imagine a scenario, imagine a scenario where

1:4:28

So I'm going to take a, I'm going to take a small example with everybody here.

1:4:33

So let's say, let's say we have the, we have the experience of a person or, okay, experience with it.

1:4:46

Experience of a person.

1:4:52

And I'll give you, I'll take one of the other, one other feature.

1:4:55

Experience here or marks have.

1:4:58

okay and based on that we are trying to predict how much of offer that person would

1:5:07

have got offered salary this could be a very good use case even at mass high school

1:5:15

right setting we have a lot of learners from across the country uh majorly and if you see we have a lot

1:5:20

of historical data about our learners we know uh some of some people have come with experience some folks

1:5:25

do not have experience though uh we have a

1:5:28

very wide full of learners in our database and if you if you take a look at it we will know

1:5:35

their experience we will know how much marks they secured in the exam in whatever uh you know examinations

1:5:43

we are uh whatever uh examinations we are doing and based on that we are trying to predict what

1:5:49

is their offered salary okay so we already have this data we have the experience we have the marks

1:5:55

and we know how much salary they were offered in the last phase when say uh we know their

1:6:02

experience we know their marks we know their salary and based on that we are trying to build a model

1:6:06

can we build a mathematical model where based on a person's experience and based on how much of marks

1:6:11

they are securing can we predict how much salary they might potentially get and this is a this is a

1:6:16

a this is a very interesting analytics problem now nobody is getting it right now like there's no one

1:6:22

company in the world that is getting this right nobody even recruiter

1:6:25

are failing in this actually but this could be an amazing problem you can solve if you can develop

1:6:30

an examination if you can create an examination right so in fact in fact you know let me share with you

1:6:39

this is this is this is something i was doing uh so when i was working for a company called elitmus this

1:6:44

is this is just wanted to share with you a slightly unrelated thing i think most of your fresh so i thought

1:6:49

it will be interesting to you elitmus is one of india's uh still very very popular pressure equipment platform

1:6:55

and when i was working there back in uh you know back in 2014 so 2014 when i was

1:7:01

working on it we were actually solving exactly the same type of problem okay so this is actually

1:7:06

elitmus so this is a company and when i was when i was when i was working at elitmus in

1:7:13

2014 we were we were solving the same problem actually we were looking at a person's experience

1:7:20

we were looking at a person's uh uh or since marks how much of marks they were scoring in our

1:7:25

it was like a cat kind of exam you know we used to test people on verbal ability uh quantitative

1:7:31

reasoning and uh quantitative aptitude verbal ability and and and uh logical reasoning lr

1:7:39

lr d r lr basically is what it's it's very much a cat kind of exam this was a very real world thing

1:7:45

you know so i personally worked on it i can relate to it or not and i was part of the tech team i

1:7:49

built a solution here using machine learning and we were actually able to select people who had the highest

1:7:55

probability of converting those jobs essential drives woulda cgi

1:8:00

drives were fresher drives it was completely a fresher platform and this is the use case

1:8:05

basically so even if you think of it from a massai's school perspective also if you

1:8:10

if you're from masai's perspective if you take it with so we have the experience of a person

1:8:14

whose experience what experience what we have the marks of a person of masai exams

1:8:19

in our exams are also pretty scientific right so i'm not person

1:8:25

working in the tech teams i cannot comment how much of analytics we are doing but i'm sure

1:8:29

there's a lot of analytics we are doing at the at the question level with exam level and if we are

1:8:34

able to accurately do it based on that we can predict very accurately how likely that person

1:8:40

is to get a job in this company and how much of salary that person might uh expect it's very

1:8:48

interesting you know like how some of these things come together overall but it's a very hard problem

1:8:54

okay now let's come back what i was discussing so here let's say

1:8:59

i have uh experience of the person experience is let's say

1:9:04

five years

1:9:06

some examples let's say experience let's say it's the two years

1:9:09

marks go get um

1:9:13

okay mark same let's let's let's let's all 90 let's

1:9:16

all right and it's offered salary

1:9:18

out of your five now okay

1:9:20

as salaries in latch

1:9:22

let's experience three years

1:9:24

mark's like same i'm not varying the marks okay guys i'm not i'm not playing with the marks too

1:9:29

much

1:9:29

his salary a salary a six luck

1:9:31

chel so let's let's let's let's get it okay

1:9:33

okay

1:9:36

one there's his experience is

1:9:38

he's 11 year

1:9:39

right now

1:9:40

and his marks

1:9:42

also same is I'm taking the same marks here

1:9:46

and let's say

1:9:47

his offered salary

1:9:48

a year and let's say his offered salary

1:9:50

and see very interesting

1:9:52

this is problem framing again

1:9:54

quick part of our Monday's discussion

1:9:55

okay Monday

1:9:57

but this is very important

1:9:59

I personally feel Monday was a very important

1:10:02

plus.

1:10:03

Okay, you have problem

1:10:03

is to understand.

1:10:04

Python in what is?

1:10:05

You know two line

1:10:06

code,

1:10:06

you'll copy paste

1:10:07

can say everybody will solve the problem

1:10:09

but if you don't even know how to think

1:10:10

what will you do

1:10:11

so the thought process is very, very important

1:10:14

the thought process is very important

1:10:16

I would say

1:10:16

okay

1:10:19

so now that is a very important

1:10:22

So you need to understand the thought process

1:10:24

how you frame the problem.

1:10:26

So framing the problem is important.

1:10:27

So you have historical data

1:10:29

from the past cohort,

1:10:32

the past cohort that graduated

1:10:33

that is those are the people

1:10:35

from who I'm collecting this data.

1:10:38

So past cohort graduate

1:10:39

who I'm collecting the data from there.

1:10:42

So we know experience

1:10:43

is itna, marks, it's a salary,

1:10:45

that mana for money to meet.

1:10:48

Experience it's, marks, it's enough and

1:10:50

that lady or that gentleman

1:10:52

and got this marks.

1:10:54

This we know.

1:10:56

This is 11-year-year-old experience

1:10:57

has, marks 90

1:10:58

he, he's

1:10:59

salary has 20-luck-ca.

1:11:01

Okay?

1:11:02

I'm taking an example.

1:11:03

Usually our cohorts do not have

1:11:05

people with so much of an experience.

1:11:07

I'm just giving an example.

1:11:09

There will be some folks,

1:11:10

obviously, but it's very less

1:11:11

comparatively.

1:11:13

And let's say there is one more person

1:11:14

with 15 years experience

1:11:17

and whose salary is 30 lakhs.

1:11:19

We're like same there, okay?

1:11:22

I'm getting into something very interesting.

1:11:25

Now, we have,

1:11:26

we have, we have,

1:11:27

a other man who's,

1:11:30

his experience

1:11:33

is around,

1:11:36

uh,

1:11:36

we can say that experience of the person is around one year,

1:11:41

his one year,

1:11:43

his year, his salary,

1:11:46

and we're,

1:11:46

we're one more value, okay?

1:11:47

One more value, okay.

1:11:49

Let's take one more value.

1:11:51

So,

1:11:52

we can take one more.

1:11:56

It's,

1:11:56

he's 17-sale

1:11:57

experience and

1:11:59

it's a salary

1:12:00

we'll let's

1:12:00

50-lark, okay?

1:12:02

Now,

1:12:02

you can't see what

1:12:03

what will

1:12:03

now

1:12:04

data.

1:12:05

And finally,

1:12:06

I'm collecting

1:12:06

data for one more

1:12:07

person.

1:12:09

His has a

1:12:09

year's a year

1:12:10

experience and

1:12:12

that one

1:12:12

man's also

1:12:13

but

1:12:14

his salary

1:12:14

we don't know

1:12:15

his salary

1:12:16

is nan

1:12:16

is the classic

1:12:18

problem that we

1:12:18

solved today.

1:12:20

Right?

1:12:20

So you'll

1:12:21

what will?

1:12:22

you'll

1:12:22

mean from impute

1:12:23

because that is what you know.

1:12:25

What will you do?

1:12:27

Sir,

1:12:27

missing value

1:12:27

there's no problem.

1:12:29

We all know how to do it.

1:12:31

What are you?

1:12:33

Okay.

1:12:33

You all know how to do it.

1:12:35

So what do you know?

1:12:38

Sir,

1:12:39

salary will.

1:12:40

As far as salary

1:12:41

are,

1:12:42

average,

1:12:42

we'll take.

1:12:43

Okay,

1:12:43

make out.

1:12:44

5 plus 7

1:12:45

plus 20

1:12:47

plus 30

1:12:48

plus 30

1:12:48

plus 50

1:12:50

divide by 5.

1:12:52

How much?

1:12:56

Let's do the math.

1:12:57

50 plus 30, 80,

1:12:58

100, 112 by 5.

1:13:02

which is how much?

1:13:04

110 by 5.

1:13:06

5 to the 10.

1:13:09

5 to the 10.

1:13:11

20.

1:13:12

I hope I'm correct,

1:13:13

22.4.

1:13:15

So mean is coming out to be 22.4.

1:13:18

Very good.

1:13:20

Your problem solved.

1:13:21

Sir.

1:13:22

impute from 22.4

1:13:23

It's done.

1:13:25

See what I'm getting at.

1:13:26

It is not just a Python thing.

1:13:27

Machine learning and data science is not something

1:13:29

that you have two techniques

1:13:30

seek low,

1:13:31

fill and A,

1:13:31

it was and you,

1:13:33

and you, and,

1:13:34

and, and, and,

1:13:34

no, you have to,

1:13:35

up,

1:13:35

domain knowledge is very important.

1:13:37

You know,

1:13:37

you need to

1:13:38

know,

1:13:38

what a one year experience

1:13:40

person's salary

1:13:41

20 to 1%4

1:13:41

is not?

1:13:43

No,

1:13:43

technically,

1:13:45

technique-wise what we did

1:13:46

was correct.

1:13:47

You mean,

1:13:47

mean,

1:13:48

median,

1:13:48

or anything,

1:13:49

maybe,

1:13:49

maybe 20-lack

1:13:50

are, not?

1:13:51

You say,

1:13:51

this are median

1:13:52

this are median.

1:13:52

Median

1:13:53

if you'll

1:13:53

be 20-luck

1:13:54

or not.

1:13:54

Mean

1:13:55

will you

1:13:55

will

1:13:55

then be

1:13:55

22.4

1:13:56

lakh

1:13:56

so if

1:13:57

you

1:13:57

you use

1:13:58

either of

1:13:59

the

1:13:59

methods

1:13:59

you are

1:14:00

effectively

1:14:01

imputing

1:14:01

this

1:14:01

value

1:14:02

with what?

1:14:03

I'll use

1:14:04

a blue

1:14:04

color

1:14:04

vice.

1:14:04

Okay.

1:14:05

You are

1:14:05

effectively

1:14:06

computing

1:14:07

this value

1:14:07

with 22.4.

1:14:10

Technically

1:14:10

we are

1:14:11

correct.

1:14:13

Dot fill and a

1:14:14

code one line

1:14:14

copy paste

1:14:15

or

1:14:15

from where from

1:14:15

you can

1:14:16

come

1:14:16

to

1:14:17

but is it

1:14:18

correct

1:14:18

correct

1:14:19

not

1:14:19

because

1:14:20

because

1:14:20

one

1:14:22

year

1:14:22

experience

1:14:23

person

1:14:23

can

1:14:23

not

1:14:23

know

1:14:24

we're

1:14:25

so we

1:14:26

we're

1:14:26

we're

1:14:26

how we

1:14:27

solve

1:14:28

in real

1:14:28

world in

1:14:29

mean and

1:14:30

medium and

1:14:30

is a

1:14:30

valid approach

1:14:31

I agree

1:14:32

with you

1:14:32

even we

1:14:33

when we

1:14:33

build

1:14:33

baseline

1:14:33

models

1:14:34

you

1:14:34

you

1:14:35

you know

1:14:35

we

1:14:36

used

1:14:37

on Monday

1:14:38

something

1:14:39

called a

1:14:39

baseline

1:14:40

model

1:14:40

so

1:14:41

baseline model

1:14:43

is something

1:14:43

that is like

1:14:44

the first

1:14:45

it tradition

1:14:45

we have data

1:14:46

we have data

1:14:46

algorithm

1:14:47

use

1:14:48

and model

1:14:48

we're a

1:14:49

baseline

1:14:49

model

1:14:50

to start with

1:14:51

we

1:14:51

we're

1:14:52

we're just to start

1:14:53

with it

1:14:53

in that kind of

1:14:56

a baseline

1:14:56

model

1:14:57

this approach is okay

1:14:59

but this

1:15:00

is okay

1:15:01

but this is not

1:15:02

an accurate

1:15:03

approach

1:15:03

in the down

1:15:04

so

1:15:05

how can

1:15:05

let me

1:15:06

remove all this

1:15:06

this

1:15:06

was the problem

1:15:09

so the

1:15:11

normal

1:15:11

mean imputation

1:15:12

will not work

1:15:13

so what

1:15:14

can't be

1:15:14

any thoughts?

1:15:17

Let me hear from you.

1:15:19

What do you think

1:15:19

that you

1:15:20

think this

1:15:20

the one year

1:15:21

experience

1:15:21

of a

1:15:22

person is,

1:15:23

how

1:15:24

impute

1:15:24

kind of

1:15:25

it is an

1:15:26

imputation

1:15:26

problem, right?

1:15:27

How do we impute it?

1:15:30

How do we impute it?

1:15:34

Five by two.

1:15:38

Uh,

1:15:38

so

1:15:40

so what we can

1:15:41

basically do is that

1:15:43

here we're

1:15:44

what we do in these kinds of cases is,

1:15:47

okay?

1:15:47

So for a minute,

1:15:48

we try to do in this kind of a scenario is

1:15:53

we treat it like we solve it using machine learning.

1:15:58

We're machine learning

1:15:59

use and solve

1:16:00

and for a minute,

1:16:02

just to make it clear so that you guys don't get confused,

1:16:05

yeah,

1:16:05

we're a feature let,

1:16:06

I will not call it the output,

1:16:09

I will call it an input feature.

1:16:10

I'm this for X-free.

1:16:11

So these are all features

1:16:12

just to be absolutely clear.

1:16:14

So these are X,

1:16:15

these are all inputs

1:16:16

and these are

1:16:18

these are the different

1:16:20

terms that we can use,

1:16:21

right?

1:16:21

We have already talked about it.

1:16:24

So here

1:16:24

there are

1:16:25

so feature you're

1:16:25

input to do you.

1:16:26

Output is a

1:16:27

too far as

1:16:27

can now

1:16:29

how we impute

1:16:30

impute

1:16:30

so we impute this

1:16:32

using machine learning.

1:16:35

So instead of

1:16:36

just finding out the

1:16:36

average and then

1:16:37

substituting with the

1:16:39

average, what we do,

1:16:40

we try to predict

1:16:41

this value using

1:16:43

the experience.

1:16:44

I'm experience used

1:16:46

and predict

1:16:46

there are

1:16:46

if you want to

1:16:48

apply your basic

1:16:48

strategy,

1:16:49

what we can do is

1:16:50

we can do is

1:16:50

we can

1:16:52

say okay

1:16:53

1 to 10

1:16:54

bins

1:16:54

bins

1:16:55

bins

1:16:55

we can't

1:16:56

just

1:16:56

we've

1:16:56

discussed

1:16:57

if you remember

1:16:58

my

1:16:58

session on

1:17:00

histogram

1:17:00

I covered

1:17:01

histogram with you guys

1:17:02

have

1:17:02

histograms

1:17:03

we discussed

1:17:04

bins

1:17:04

right?

1:17:05

so

1:17:05

we can't

1:17:06

we can say

1:17:07

okay

1:17:07

0 to 10

1:17:09

0 to 10

1:17:11

10

1:17:11

to 10

1:17:13

10

1:17:13

in 1 to 3

1:17:14

1 to 3

1:17:14

1 to 3

1:17:16

1 to 3

1:17:18

10 to

1:17:19

20

1:17:19

that average

1:17:20

how average

1:17:20

that is

1:17:22

50 plus

1:17:23

30 plus

1:17:23

20

1:17:23

is

1:17:24

100 by 3

1:17:25

is 33

1:17:26

33.3

1:17:26

Now

1:17:28

winning

1:17:28

and then you can

1:17:29

say

1:17:29

yeah

1:17:30

something like that

1:17:31

it's

1:17:31

it's logic

1:17:32

it's logic

1:17:32

right

1:17:32

and then you say

1:17:33

okay

1:17:33

this person with

1:17:35

experience

1:17:35

1

1:17:36

who has most likely

1:17:37

predicted

1:17:38

salary 6 over. This is one approach you can use. The second approach you can use is

1:17:41

a more advanced approach is where we try to predict. We predict X3 using X1 and X2.

1:18:01

X2 use and X2 use from X2, we predict

1:18:03

we predict kx1 and X2 use

1:18:05

we're same set set X3 predict

1:18:07

to predict kind.

1:18:07

So, basically.

1:18:08

it is like saying,

1:18:09

we're

1:18:09

here two

1:18:10

things

1:18:10

we'll make a model

1:18:12

to predict

1:18:13

whatever

1:18:15

principles we talked

1:18:16

about on Monday,

1:18:17

it is something like

1:18:18

we're

1:18:18

we're both

1:18:18

consider

1:18:19

and a model

1:18:20

to make a model

1:18:20

so

1:18:20

end result

1:18:21

will be some

1:18:22

equation.

1:18:23

Some equation

1:18:23

let's say

1:18:24

let's say

1:18:24

let's say man

1:18:25

x3 will be

1:18:26

equal to.

1:18:26

I'm just giving

1:18:26

a very

1:18:27

you know,

1:18:27

very ballpark

1:18:28

understanding.

1:18:29

X3 will be

1:18:29

equal to

1:18:29

let's say

1:18:30

you know

1:18:32

something like

1:18:33

you know, something like

1:18:33

you know

1:18:35

something like

1:18:35

you know,

1:18:38

2 times X1, 2 times X1 considered

1:18:41

2 times X1

1:18:43

plus 2 times X1 plus let's say,

1:18:46

you know,

1:18:48

2 times X1 plus let's say,

1:18:51

allow me to think a little 0.01

1:18:53

current 0.01 currently to 0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0. I'm

1:19:03

okay. I'm just giving an example. It didn't, it doesn't have to be this way.

1:19:05

but I'm just trying to take some ballpark numbers to make it easy to understand.

1:19:08

understand, okay? Or plus 0.05 here. Okay? So this is your

1:19:12

whole equation.

1:19:13

okay?

1:19:13

So I hope everyone's aligned.

1:19:15

So I am getting a little deeper. This is again. I'm getting a little deeper. This is again a

1:19:20

little bit different of topic I'm going, but

1:19:22

something I feel all of you should know at a slightly advanced level, how things are

1:19:27

actually done.

1:19:28

So when we have to predict this particular

1:19:32

offered salary, the missing value,

1:19:34

we try to predict, we try to predict, we try to predict. We try to predict, we try to

1:19:38

first build a model between X1, X2 and X3.

1:19:42

I'm model to make. It's like we try to build a model to predict.

1:19:46

So we try to predict X3 using X1, X2.

1:19:50

All features are. We make model

1:19:51

we'll make a model. This is like the model.

1:19:55

First, we will train the model. We will build that particular model,

1:19:59

that particular mathematical function between X1, X2, X3.

1:20:03

As a model been made it. When we have a new data, there are two, mind you.

1:20:07

Monday we discussed.

1:20:08

One is model training.

1:20:09

Existing data on model to model.

1:20:11

Naya data on prediction.

1:20:13

So the model been made, when we have the new data, we will do the prediction.

1:20:16

Let me use the green color.

1:20:18

So what will go?

1:20:19

2 into X1, substitute for 2 into 1, 2 plus 91.91 plus 1.

1:20:27

So this will be 2 plus 2 plus 0.91 plus 0.05.

1:20:36

So this maxed, how it?

1:20:38

2.96, which will be 2.96.

1:20:42

So the model will predict 2.96.

1:20:44

And I'm sure you will agree with me, this is the much believable value.

1:20:47

Much more believable value.

1:20:48

Okay, so this is actually how it happens in practice, which is a more accurate method.

1:20:52

Because if we'll mean, then, then, the whole column of mean, uh, lay, that is not a very accurate method.

1:20:58

Okay, so a little match.

1:20:59

But I want to take a pause right now to understand if everybody followed what I discussed here.

1:21:03

Okay?

1:21:08

Okay. I'm just going to pause just to allow all of you to take some breath and understand, okay?

1:21:14

Clear there, guys, everybody?

1:21:15

Next time you come across any problem going forward.

1:21:18

Okay, okay, exercises for what we will do is to make it easy.

1:21:21

We'll average, impute, kharge, but this is something you should keep in mind.

1:21:25

When we come to machine learning topics from next week onwards, you will get a better flavor in terms of how this is actually done.

1:21:32

Okay?

1:21:34

Is it okay?

1:21:35

All of you with me?

1:21:36

Others, let me know.

1:21:38

So we are basically imputing the value.

1:21:54

We are basically imputing the value using prediction.

1:21:58

I'm predict basically.

1:21:59

So we are using the available features and trying to predict the value of the other feature.

1:22:04

That's the way how we work in to watch.

1:22:08

Explain about the calculation again, which one, which one actions?

1:22:12

This one you follow, the modeling part.

1:22:14

This one, this is just an example I'm talking about.

1:22:19

I'm just saying, you have X1, X2, X-T, in case you're wondering, sir, how did you get to this?

1:22:25

I just took an example.

1:22:27

This is not derived from something on.

1:22:29

I'll just took an example.

1:22:30

But actually, this will be created by algorithms later on.

1:22:33

We will see that later.

1:22:34

But how did I exactly come up with these numbers?

1:22:36

I just took some.

1:22:38

sample numbers.

1:22:40

This is to help demonstrate the model part to you.

1:22:43

But yeah, it's a type of equation.

1:22:45

at the end of the day.

1:22:47

But this is the spictitious numbers I've taken right now, okay?

1:22:50

The first part is you, you know, you have a model, you have to do some rules.

1:22:54

The next part is next time you have some new X1, X2, you try to predict what is a new XC.

1:22:59

That's the way you try to go about it, okay?

1:23:03

Chalroo.

1:23:05

Okay, great.

1:23:07

Now, moving on.

1:23:08

The next phase, we will look at some intermediate concepts and the next phase is basically

1:23:12

how do we go and convert text data into numbers?

1:23:19

Because machines cannot understand text data.

1:23:21

So these are the things we are left out with the left off with handling categorical data.

1:23:25

This is the phase we will discuss called encoding.

1:23:27

That's number one.

1:23:28

We will discuss different types of encoding techniques.

1:23:31

Number two, we will discuss something called scaling.

1:23:33

Instead of two major topics that are left.

1:23:35

And number three, finally, we will discuss about something.

1:23:38

called data leakage. So there are three broad topics that are left down.

1:23:41

Okay. Easy. So we can take a short break right now. Let's take a five minutes break.

1:23:46

Okay. And we'll come back after the break and continue on with these three other modules

1:23:51

run out. Okay. I'll see all of you back in, in five minutes from now.

1:24:08

Thank you.

1:24:38

Thank you.

1:25:08

Thank you.

1:25:38

Thank you.

1:26:08

Thank you.

1:26:38

Thank you.

1:27:08

Thank you.

1:27:38

Thank you.

1:28:08

Thank you

1:28:38

Thank you.

1:29:08

Thank you.

1:29:38

Thank you

1:30:08

Thank you

1:30:38

Thank you

1:31:08

Thank you

1:31:38

Thank you

1:32:08

Thank you

1:32:38

Thank you

1:33:08

Thank you

1:34:08

Hey, folks, uh,

1:34:38

welcome back we will continue on and now i will talk about a very interesting topic which is

1:35:01

how do we encode data different types of encoding techniques and once again the important thing is let's say

1:35:08

we again have this df underscore car data frame and if you particularly look at it this particular

1:35:14

data has some categorical data right like for example we have a brand maruti if you will is

1:35:21

petrol diesel and we have already seen right in machine running what we are trying to do is we are

1:35:26

trying to formulate equations we are trying to formulate some some mathematical equations like

1:35:31

y is some function of x like that and how do we do this here how do we go back and you know work this out

1:35:38

in this particular scenario because all that we are trying to do is we are trying to formulate

1:35:42

some some mathematical equations here so how do we work it out how do we in practice

1:35:50

do this thing how does it work out and that's exactly what we are what we are trying to do overall

1:35:56

right because machines cannot work because if you try to build a machine learning model

1:36:02

on this kind of data it will give an error and that is a practical reality you cannot

1:36:07

build a machine learning model on this kind of data so imagine this is your x and this is

1:36:11

your y you cannot build an equation on this so we have to learn different types of encoding

1:36:16

techniques and here i will talk about uh two specific type of encoding techniques

1:36:20

label encoding and one hot encoding so to explain these concepts in a better way

1:36:25

what i will do i'll take you to my notes i'll take you to my notes

1:36:37

so there are two broad categories of data that we have one is obviously numeric data if you

1:36:45

see in in in in python there's int and float that you guys have worked with all this while

1:36:49

right int and float that is numeric data anything that is not a number is what is referred

1:36:56

to as categorical data shtr types basically whenever you are in inherent data type is str and

1:37:02

the pander's data type is object that is what is referred to as a category

1:37:07

data now categorical data can be further classified into two types one we have something called

1:37:15

nominal data and second we have something called ordinal data so what is ordinal data let's talk about

1:37:23

that first ordinal data is that kind of data where a distinct order exists there is a distinct order

1:37:32

in which the values are coming are going to come that is what is referred to as ordinal data and

1:37:37

repeat ordinal data is that kind of data where there is a distinct order in which the

1:37:44

values are supposed to come just to plan some that is what is referred to as ordinal data wise okay

1:37:50

now moving on what could be some examples of this imagine we have a column called

1:37:59

size okay so let's say they have a size column whatever be the context let's say car-fi data

1:38:07

set and we have a size column right now so yeah i think this will be a good use case in the same

1:38:13

uh car data set not look like that we can have so let's say we are adding a a size column to it look

1:38:20

let's take a red column we're adding a size column to it you have a size column here and let's say

1:38:27

this is small this is medium this is large this is small this is medium

1:38:34

very practical example okay same data in

1:38:37

If you think about it, small is less than medium, medium is less than large.

1:38:46

We all agree on that.

1:38:48

Now, no here here here here says, no, sir, medium large is more. I mean, all of you agree that

1:38:53

medium is less than large. We all agree on the order. See, what I'm getting at is,

1:38:58

data in order is small mediums and medium large to come. And this order we all agree. You and me

1:39:05

we both agree on the order. That is what I'm getting at is.

1:39:07

that is what I'm getting at the order is something we both agree on so small is less than

1:39:14

medium medium is less than large and there's an order that we both agree on that's the important thing

1:39:19

we agree on the order so what we do in this kind of a case is there's an inherent order that exists

1:39:26

so we can simply replace this if your values are now i mean just one two three say replace

1:39:33

we can say small is one

1:39:37

let me is a different color here we can say small is one uh medium is two and large is three

1:39:48

small is one medium is two and large is three so this can simply work on the basis of this

1:39:53

see of the counter that's the way how we can work it out

1:39:58

if straight forward this is all what label encoding basically refers to if i go and uh

1:40:05

take you back to my snippet once again all

1:40:07

we are doing is whenever we see the value small we replace with one it is like a simple replace function

1:40:13

in python our replace function use can replace straight away you can do a replace that's it

1:40:18

you replace small with one you replace medium with two and you replace large with three that's it so

1:40:24

whatever categorical data we had this was a categorical data we could not have directly work with

1:40:29

this kind of data okay machines don't understand this data we are simply taking this and you are simply

1:40:34

replacing that with this so um us go

1:40:37

one two three say replace for the integers replace and after we replace them with integers

1:40:44

after we are able to successfully replace that with integers we will only work with this column

1:40:48

this go on drop for doing

1:40:51

we'll go ahead we'll drop it down we'll completely drop the other column and we will

1:40:56

only use this column and we'll proceed ahead that's the way how it works out okay i hope everybody

1:41:02

is clear with this this is what how we handle ordinal data but please remember in

1:41:07

the practice ordinal data is very rare. Ordinal data you'll

1:41:10

you'll not see. Ordinal data is very there. The other kind of

1:41:13

categorical data that exists that is much more frequent is what is referred to as

1:41:18

nominal data.

1:41:18

Every time in whatever the real ball data we work with, you will always see

1:41:24

something called nominal data. Nominal data is something we will always see.

1:41:28

Obviously it's got ulta is that kind of data where no distinct order exists.

1:41:35

So nominal data is that kind of data where no distinct order exists. So nominal data is that kind of data.

1:41:37

where no distinct order exists. That is what is referred to as nominal data. And if you take a look at it,

1:41:43

this is how we can, you know, define the intuition of nominal data here. So we once again have a city column.

1:41:51

You have a city column. You have city column. You have D, C.M. And the values in the city column

1:41:59

are BCM. This is your city column. So city column is there. We have Bangalore, Shendai, Mumbai. These are the

1:42:05

about the three values in the city column that we have right now, Banglo, Chennai, Mumbai.

1:42:10

And what we can go back and do here is we can effectively kind of, again, we have to somehow figure out a way

1:42:20

to convert this into numbers.

1:42:22

Because we can't this value in the way. Another very important thing is this is there is no order

1:42:28

in this data. You cannot say that Bangalore is less than Chennai or Chennai is less than Mumbai.

1:42:33

This data in order not.

1:42:35

So it is not an ordinary data.

1:42:37

If ordinary, then I could have replaced this with 0, 1, 2, but there's no order.

1:42:42

And if you try to hard code an order, what, what would have, data is wrong.

1:42:48

I don't want a situation where I explicitly hard code an order and I say,

1:42:53

yeah, Bangalore is less than Chennai, Chenna is less than Mumbai.

1:42:57

That's not. I do not want to explicitly, excuse me, I do not want to explicitly, excuse me, I do not

1:43:04

want to explicitly provide some kind of an order here. I don't want to do that.

1:43:09

So in that kind of a scenario, we do something called dummy importing or one hot encoding.

1:43:14

We create one column. Now I'm talking about the approach and the technique. We create one column for each

1:43:20

and every individual category. So we'll Bangalore's a column, Chennai to a column banon,

1:43:25

we'll make one column for each and every individual category. And whichever city is present,

1:43:32

So this one row, so it will be one mark.

1:43:36

Bangalore to one mark, Chennai, Mumbai, and Mumbai, zero, mark.

1:43:40

That's the way how it is it worked out?

1:43:41

Okay?

1:43:41

This particular row corresponds to Chennai.

1:43:45

So Chennai to Chennai to one mark and Bangloor, Mumbai to 0-0 mark

1:43:48

straight forward.

1:43:50

And finally, this particular row corresponds to Mumbai.

1:43:53

So Mumbai to we'll mark one mark and Bangladesh to, we will mark zero each.

1:43:58

That's the way how we can work it out.

1:44:00

Okay, so this is a simple way how we do something called one hot end.

1:44:02

encoding or dummy encoding. Okay. And once the encoding part is done, encoding

1:44:06

we are simply converting the data into a numeric format. I mean, encode kind of it. Okay. So

1:44:12

one approach was, other order he, then one, two, three, say, import, in that order.

1:44:16

Other order, any, there. If order not, if there, one, two, three, may be. Then I cannot say

1:44:21

Bangalore, Chennai from, Chennai, Mumbai, say come. I cannot do that. If I'm, I'm inducing

1:44:26

bias in the data. We're not going to. So in that case, what I do? I go back and, I simply use

1:44:32

something called one hot encoding or dummy encoding. So I create one column for each and every

1:44:37

individual category. Just the categories, it's the column for out. And wherever that particular

1:44:42

value is present, market one. And wherever that particular value is not present, market zero. So

1:44:48

once the importing is done, please drop that column. This is your final data. It's

1:44:52

over the machine value. Simple. That's the way how we work it out. So once it is done, this is the final

1:44:58

data set on which you will do machine. That's important.

1:45:02

I hope everybody's alive. This is the, this is the data that you will see in the real world.

1:45:05

If you come back to my, uh, come back to my data set right now.

1:45:09

You have brand and fuel. I think the answer is in front of you.

1:45:13

Petrol diesel. Can you say petrol diesel? Can you say diesel petrol's than

1:45:16

there? We can not do that, right? Can you say Maruti is less than Hyundai? Hyundai is less than Honda?

1:45:22

No. This is completely nominal data.

1:45:25

Don't object type. If you're df car dot info is a very nice way to understand the overall

1:45:30

structure of your data. You've seen info.

1:45:32

already in your Panda sessions, right? So here from you

1:45:35

you'll get that object type are, this object type are. So these two are

1:45:39

categorical data and do no nominal data. Nominal data. Nominal data, of course,

1:45:44

some will say, because order not. And what you will do in this kind of data, you will do

1:45:49

one hot encoding or dummy encoding. Okay? Okay. Simple thing. Everybody's clear. Everybody's

1:45:56

clear. Is the concept okay? Code. I will show you. Only one line of code. We will see.

1:46:01

But I want to just pause for a minute.

1:46:02

it and again, take a confirmation from all of you. If everybody is clear, let me know this.

1:46:07

This is the concept. How do we handle categorical data? Ordinal? Order. Ha. Nominal. Order.

1:46:14

Nominal. We do label encoding. Nominal. We do one hotel coding. Okay. This is what we will see in the

1:46:21

code right now. Okay. Okay. Clear. This is yet another kind of data cleaning that we do.

1:46:27

You see the flow. How we are going through the steps. This is one more kind of data cleaning that we have

1:46:32

discusses. And these are all needed to be done before we build our model.

1:46:38

If we're not this thing not, we'll, we'll make them. We have to do all of these things

1:46:43

before we go and build them all. All of these things need to be accurately done.

1:47:02

So now, how do we implement this in the code, guys? Coming to the code, you can see, we

1:47:28

already discussed that there are two nominal columns we have right now. Brand a nominal

1:47:33

column. He will like nominal data type. These are both categorical columns. So we will use a

1:47:38

particular Python function called PD. Get dummies. We are using a particular Python function

1:47:44

called Pandas function called Get dummies. And this say we want one hot encoding. Level encoding is

1:47:51

very simple. That you are replace. Dot replace functions have label encoding. There's a specific

1:47:56

label encoder also that we have, but I always suggest use it a simple way of label

1:48:01

encode replace a constructive, no problem. And get domains is what we can use for doing one hot encoding.

1:48:07

To start with, I will, we'll see some other ways of seeing doing the leakage and all that we'll

1:48:12

discuss. But to start with for now, this is the simple way we can go back and do something called

1:48:17

one hot encoding. So we give the data frame as an input. D type equal to interim carter so that you get

1:48:24

zeros and ones. And columns is brand and fuel. When you run the code, this your encoded data

1:48:30

here. Now, there were three different brands of car we had, Maruti, Hyundai and Honda, Toyota.

1:48:37

Four brands. Or four brands for four brands for four columns. One, two, three, four.

1:48:43

And similarly, there are two types of fuel. We had petrol and diesel. And for each of the categories

1:48:47

of fuel, we are getting a columnage, petrol and diesel. And this is the one hot encoding that has

1:48:52

happened. Wherever, petrol was.

1:48:54

there. Petrol 1, diesel is zero. Wherever diesel was there, diesel one,

1:49:00

petrol zero. And look, we've seen, we've seen the Vuel column to out of the brand column to

1:49:03

have. And now, if you look at this entire data frame, all data numbers are. If you go back

1:49:09

and check DF car encoded, if you go back and do this right now, DFcarcordid.

1:49:14

Info, if you, if you're you, if you're just in info method, you, you'll see, everything in detail.

1:49:18

Now, this data, I can say, is ready for machine level. This is the way how we go back and do

1:49:23

something for encoding.

1:49:24

is a mandatory step. If your data in any

1:49:26

any kind of object type data, your

1:49:30

machine learning algorithms will not work.

1:49:32

If you have a relationship not can't. The equations

1:49:34

not make. You think for yourself, how do you

1:49:37

multiply some string? Two into, what is

1:49:40

two into patrol? What is three into

1:49:44

Maruti? What is? What is it? What is

1:49:46

three into Maruti? What is it? We cannot calculate those things.

1:49:48

So we have to do this. We have to do this. And mostly

1:49:51

99.99% is the time.

1:49:54

you will always encounter nominal data.

1:49:57

Ordinal data in practice, in practice, okay?

1:50:00

Or always you will see nominal data.

1:50:02

Let's move on.

1:50:04

Simple piece of code snippet piece of form called get them.

1:50:07

This is what we discussed.

1:50:08

Now, the next core topic that we are seen is something called scaling.

1:50:13

So scaling idea is very simple.

1:50:15

Scaling is effectively something where we go back and,

1:50:23

so what we do in scale.

1:50:24

scaling is hard. Yeah, yeah. Exactly. This is, this is all what we are trying to do,

1:50:33

action. What are the things that we have to do to get our data ready for machine learning? These are

1:50:37

exactly all the things that we are trying to do. So in order to get our data ready for machine

1:50:41

learning, these are all the things that we are doing. First, analyze the data or figure out inconsistencies.

1:50:47

Missing data may, right? Data may outliers. You try to figure out. So these are all the things that we are going to

1:50:54

figure out whether our data has any problems or not. Is my data consisting of strings?

1:50:59

How do I, if my data consists of some categorical data, how do we encode it? I'm case a label encoding

1:51:05

cutting. I'm going to say one hot encoding. So these are the things that we are that we have. All these

1:51:10

are the steps that we hold on. Okay. Make sense? These are all the steps. And the next part is

1:51:16

we are talking about something called scaling. So we'll see what scaling is. So at a very high level,

1:51:21

before I, you know, get into the deeper aspects of the conversation at a very high level.

1:51:26

What we are trying to do in scaling is, in scaling, in scaling, we are trying to effectively.

1:51:35

So, so in scaling, we are trying to effectively go back and take different, different scales of data.

1:51:45

And we are trying to convert all of it to the same skills.

1:51:49

So scaling shrinks.

1:51:51

all the numbers to a similar range so that every feature gets an equal vote.

1:51:58

Let me take a moment to explain that, what I'm trying to say.

1:52:03

If you're your final data, this is your DF encoded data frame.

1:52:08

This is your intermediate data frame.

1:52:10

We discussed the concept.

1:52:12

You look here here here, a kilometers driven, price, brand, all that we've got.

1:52:18

Now, you can clearly see some of the values are,

1:52:21

other values are very small whereas some of the values are very large. Some of the values

1:52:28

are really small, 2017, 2018, 2016. Some values are very small, whereas some values are very large.

1:52:34

So the data is present in very, very different scales. So whatever data we are seeing

1:52:40

on the screen right now, this data, all this data is present in very, very different scales.

1:52:46

So that is the reason why it is very important to scale our data.

1:52:49

And whatever scaling we are discussing is only done for numerical features.

1:52:57

Jo encoded features we've made, you know, up us to scale not going, just to clarify it.

1:53:02

Please keep that at the back of your mind, okay?

1:53:05

And the specific type of scaling I will talk about right now.

1:53:08

We are in this particular topic right now, just to clarify.

1:53:12

These are all from your notes which will be shared later.

1:53:13

And the specific type of scaling that we are discussing right now is,

1:53:19

what is referred to as mean max table. I will start with that conversation.

1:53:25

See, here we know notes in a lot of we've made a good example. You can take

1:53:27

take, like, age. Now, persons age can range from 20 to 60.

1:53:32

Yeah, or 10 or 20 or or 60 or 70 or, 100, 100, 100, 150, or 200 will. I don't think anybody in

1:53:39

this world has 200 age. But tonight is maximum

1:53:42

is. But if you can't salary look, imagine in the same data frame, if you consider a salary column,

1:53:48

if you look at, then salary, then $20,000 be

1:53:51

can't be $30,000 be

1:53:52

$1,000 be

1:53:55

can you see how

1:53:59

the scales are so drastically

1:54:03

different? If you're

1:54:05

these two columns side by side

1:54:06

think for a minute,

1:54:08

your age which is ranging from

1:54:11

0 to 150

1:54:13

and here your salary

1:54:15

that is ranging from 0 all the way to

1:54:18

one crore. So, this becomes a big problem in machine learning.

1:54:26

So if you feed this to a machine learning model,

1:54:31

the model might assume that salary is more important simply because its numbers are bigger.

1:54:40

This is a very important thing.

1:54:42

Now, if you're these two features side by side, if you try to go and build a model,

1:54:48

The model will...

1:54:49

Because see, what is machine learning?

1:54:51

If you go back to the conversation we had on Monday,

1:54:54

machine learning what is where you are trying to teach a small kid,

1:54:58

right?

1:55:00

You're showing it lots and lots of examples

1:55:01

and you're trying to teach a small kid.

1:55:03

Yeah, machine learning and what?

1:55:05

You're showing it lots and lots of examples

1:55:07

and you're trying to teach a small kid.

1:55:09

That is what machine learning is at a very high level.

1:55:11

That's the idea.

1:55:15

That is all machine learning is right now.

1:55:17

You're showing it lots and lots of

1:55:18

examples and you're teaching it, you know, that's the big picture idea. Now, if you think

1:55:29

about it, if you think about it, guys, salaries are very high value. If you try to train a

1:55:41

machine learning model, the model might end up thinking the salary is more important. I should give more

1:55:48

to this feature and I should give less importance to the age feature because it's not

1:55:54

important. So feature scaling is a very important part. Feature scaling brings all the numerical

1:56:01

columns to a comparable range so that the model doesn't get biased. Now what do, although the

1:56:09

original values are very different, we're scaling and we're doing it. And I will teach you exactly how

1:56:16

it happens. So a technique from mathematically, the second technique in code. So min-max scaling

1:56:22

is the approach we will see right now. It's called normalization. It's a scaling technique. It's a

1:56:27

scaling technique, very popular scaling technique. And all that this technique doesn't, it squeezes all

1:56:32

the values into a range of 0 to 1. This is what it does. That's the important thing. Now,

1:56:41

let us see a small example in terms of how this is one.

1:56:46

working. So what I will do, let me see if I have a already have a snippet

1:56:54

related on this. Just allow me a minute. These are, these are all I will share with you guys.

1:57:00

Okay. So whatever I, uh, I discuss in my class and make it a point to share all this with me.

1:57:16

Thank you.

1:57:46

I was trying to check if I've actually got it in my notes.

1:57:59

I'll try to do it in front of you.

1:58:02

So let's take the same example of age and salary.

1:58:04

Because I want to show you one example from scratch.

1:58:06

Because if you a one calculation, it will be very, very nice to follow the rest.

1:58:11

So in code, it is nothing.

1:58:12

It is very simple in code.

1:58:13

We will discuss that, but I want to do in pen and paper one example.

1:58:16

so that you guys are really confident he internally how it is happening okay so age

1:58:22

later this is the age column and we also have the um salary column and though he dohi examples

1:58:31

let's okay this is feature x1 and this is feature x2 that is what we have right now now

1:58:40

so age the values are let's say for example 10

1:58:46

you'll get 20 you'll get 30 you'll get 40 you'll get 50 i'm taking some ballpark numbers i hope

1:58:56

just to simplify the calculation or salary values go yeah uh as an example i'll take the same

1:59:05

scale okay so that's easy to calculate 200 000 that's

1:59:09

salary was 3 lakh his salary was 4 lakh

1:59:16

I'll do a whole slagic. This is the thing. Simple data set.

1:59:20

Okay, let's just to, you know, so that I have to write less.

1:59:24

You can save some time. Now, the basic formula of min max scalar. Min max scalar, this is what we are discussing

1:59:35

right now. The basic formula for min max scalar would be the scaled value.

1:59:46

will be equal to x minus min divided by max minus min.

1:59:59

Yeah, your formula is. I don't think it's very hard to elect you.

2:0:05

It's very simple. So, let us see. Let us see what it means, okay? So, so,

2:0:10

first we have our past, our past age column. And I will try to differentiate to differentiate.

2:0:16

the scaled values using the red color. So we have scale age. And we, and we, and let us calculate

2:0:30

scale days. I must go x1 prime and and here we have scaled salary and we call it x2 prime.

2:0:46

This was simplicity, okay? So just to clarify, this is the formula that we'll be using.

2:0:50

The scaled value will be basically this. The next time anybody asks you what is the scaled value?

2:0:55

The scaled value will be nothing about this. Yeah, the scaled value. Okay, just to clarify it.

2:0:59

Now, let's move on.

2:1:06

Give me one second, guys.

2:1:08

Just give me one second. Just give you one second.

2:1:16

Okay. So people can direct to it. I just wanted to make a little space for myself.

2:1:22

Take up. Now, um, now let's do the calculation. So what we have here is the scaled value of age.

2:1:33

What is? Then minus. So first you, what do you do? First, how do we do scaling? You look at the age column. You find out what is the mean? What is the mean of it?

2:1:45

and what is the max of it? That's it. That's the first thing we'll do. So what is the main of it?

2:1:53

Main 10 here. What is the max of it? Max 50 here. This is what you learn from your original data.

2:2:02

The original data has original columns you have to this is the pattern that you learn from the original data.

2:2:09

So you learn the patterns from the original data that the minimum value is 10, the maximum value is 50.

2:2:14

Similarly, you go to the salary column. And again, you tell me, what is the minimum value?

2:2:20

10,000. And what is the maximum value?

2:2:26

50,000. That's it. There is this. So minimum value is 10,000. And maximum value for your

2:2:35

50,000. That's the thing that you are ready to get. This is what we have learned from the original data

2:2:41

that is present in the columns. That's it. Min, it's it. Min, is the maximum.

2:2:44

That's straightforward. Now, coming to the scaled value of age, what is the scaled value of age?

2:2:50

The scaled value of age is nothing but we take the original value of age, which is 10.

2:2:58

It will be 10 minus 10 divided by 50 minus 10. This will be equal to 0. So scaled value of age for 10 will be equal to 0.

2:3:12

this value is. So value minus min divided by max minus 0.

2:3:18

Okay. Okay. Moving on, 20 minus 10 divided by 50 minus 10. If you calculate this,

2:3:30

again, how's the way? Value minus min divided by max minus minimum. So 20 minus the minimum.

2:3:37

So 10 divided by 40, 10 by 40, 10 by 40, 0.25.

2:3:42

There it is.

2:3:46

Next, 30 minus 10, divided by 50 minus 10.

2:3:55

You get 20 by 40.5.

2:3:58

Next, 40 minus 10.

2:4:03

Okay, this analysis.

2:4:04

X, I mean, the value minus the minimum by the max minus min. That's it.

2:4:08

Divided by 50 minus 10.

2:4:11

This is how about?

2:4:12

3 by 4, what 0.75.

2:4:15

See how symmetrically we have lined it from 0 to 1.

2:4:17

I hope you are able to observe.

2:4:18

But the values could be we are shrinking them in a scale of 0 to 1.

2:4:22

That's it.

2:4:23

That's the beauty of this technique.

2:4:25

And last was, 50 minus 10, divided by 50 minus 10.

2:4:30

So the maximum value will always become 1 and the minimum value will always become 0 in this approach.

2:4:36

Okay?

2:4:37

Next, we're on salary to do.

2:4:39

And the interesting part is after doing scale.

2:4:42

the max has become 0. The mean has become 0. You can see the minimum value

2:4:51

has become 0. And the maximum value has become 1. Yes, Kding after we can only be

2:5:00

related to it. Now, let's do the same thing for scale sanity. Scale salary come

2:5:04

a two examples in time. So 10,000 minus, mean is 10,000.

2:5:12

divided by 50,000 minus 10,000.

2:5:22

This is zero.

2:5:24

One more, let's.

2:5:25

The next one, only, last one, only I will do.

2:5:27

And we can do the middle one, 30,000.

2:5:29

Okay, middle one, your point 25 way, okay?

2:5:32

Yeah, your point 25 be same way.

2:5:36

Next one I will show you, 30,000.

2:5:40

This value is.

2:5:42

minus, mean, divided by max minus mil.

2:5:52

This is how about 20,000 by 40,000 is 0.5.

2:5:57

Similarly, this got 0.75. Similarly, it got 0.75. So the very interesting takeaway from this

2:6:04

conversation would be, now, original scales where we have, we had age and salary, and these values were

2:6:10

very different, right? Age was very small.

2:6:12

was very large. And this is exactly what I told you.

2:6:15

If your values, if your scales are a lot go, then if you build models on this data,

2:6:22

those models will be biased.

2:6:24

But after we have done the scaling, I'm a min-max scaling here up here.

2:6:29

After we have done the min-max scalar, we have converted the age from 0 to 1.

2:6:35

And we have converted the salaries from 0 to 1.

2:6:38

I'm the values go same scales.

2:6:41

And that's the biggest benefit.

2:6:42

I hope everybody's alive. That's the biggest benefit of this case. Okay. Now, moving on.

2:6:56

Is it okay? I'm going to, I'm going to, I'm going to pause for a minute right now. There's a lot of

2:7:03

calculation I showed you, but I hope it was easy. If you, anybody has any doubts, anybody wants people

2:7:10

talk about it. Let me pause on this for a minute. All good guys. Please let me know.

2:7:17

Did you all understand how is feeling happening? You see, this thing in code is one line.

2:7:23

Aged. I'm going to write in Python way how it is done. Just like we discussed one hot encoding.

2:7:27

PD.gat dummies was the syntax you use, right? You are able to get the encoded values same way.

2:7:32

This in code is one line of code. We will see that shortly. But is the concept clear, all of you? Please let me know.

2:7:40

Is the concept clear? Okay. Only others has responded. Whatever the rest of you?

2:7:51

Quick, guys.

2:8:10

Let me know, guys. Very sorry for bothering you, asking you to respond like this, because I think the, you know, the chat is the only way I get to know how you're following the things. So, please let me know. If you want me to repeat anybody, you're saving, I mean in doubts, please don't hesitate to stop me, okay? Because I'll go in one flow, but if you face any difficulty, any confusion, please don't hesitate to stop me. I'm happy to, you know, go over it again.

2:8:40

Calculation part scary? Okay, which part did you find scary?

2:8:45

And I'm very glad that you shared with me. Very glad that you shared with me.

2:8:49

And this is exactly what I want. Honest feedback. Let me go. I'll help you out. No way.

2:8:53

Where where you have difficulty?

2:8:55

But I mean. Max, Min, Min, where do you have the difficulty? You want to tell me?

2:9:01

We can spend another five minutes. No problem. We have enough time today. Don't worry.

2:9:05

You want me to take you through it once again?

2:9:10

Because this Python is nothing. See, again, I, I, I, one thing I'm telling you is the concepts are most important.

2:9:16

Because this is, when you're in Python, so let me give you a sneak peek in Python.

2:9:21

In Python, we'll what we'll do. Python in both a line of code, that's it.

2:9:25

That's it. Okay, that's it. That's it. Kothom, Minmax. Minmax is nothing but you initiate minx killer.

2:9:32

Min max, which is on? Ase is on salary to do. Whatever I was doing manually,

2:9:36

now Python to say, that these two columns, you have on this on min max scaling.

2:9:40

That's it. You use something called dot pit transform for up a min, max killer. That's it.

2:9:46

This is one line of coded python.

2:9:49

Behind the scenes, this is all that is going on. Okay? So, Utkars, can I, can I repeat it once again for you?

2:9:57

Two, three minutes?

2:9:58

That's after, if you're tickers had, you, please let me know. If you understood after this,

2:10:03

let you. So, so first of the, you know, we have, you know, we have an age column and we have a salary column.

2:10:10

So, this I'm additionally showing. You're just shown the thing. So, but I think

2:10:18

I wanted to make sure you at least understand some of the nuances. How we're done. You're not getting

2:10:23

into so much of calculation in our notes. But still, at least one calculation if you follow,

2:10:28

you will follow the other ideas very well. Okay. Okay. All. Yeah. Exactly.

2:10:34

Ultimately, from the content and the course perspective, what is important is the, is your class

2:10:40

notes. You have to be aligned with your class notes. Oftentimes in my sessions,

2:10:44

I will give you a lot of other case studies in our real world scenario. I'll definitely make it a point

2:10:49

to cover your notes and more. I mean, my classes are always like notes plus much more. So

2:10:56

notes that the minimum from the course perspective, you should be good. But the much more part is like

2:11:02

where, okay, that, that means, you know, but you don't expect examinations and all to be based on

2:11:09

that by the way. Examinations should be totally based on your class.

2:11:14

Yeah.

2:11:15

Yeah, exactly.

2:11:16

Fit transform, this sort of thing you will have to relate to it.

2:11:21

And for that, we have the glossary, right?

2:11:23

At the very end, if you see, Akshar,

2:11:25

all sessions'ar, you'll get a glossary

2:11:26

can't.

2:11:28

How difficult is this?

2:11:29

If you'll look, the broad ideas that we discussed today,

2:11:32

Pandas, head, info, describe, is null, fill and A, drop duplicates,

2:11:36

here.

2:11:39

You are getting these notes, right?

2:11:42

I think at the end of every class, you're all seeing this in your dashboard.

2:11:46

All of you have this.

2:11:47

Even last session, you will have these notes, right?

2:11:50

What we talked about is min-max scalar.

2:11:52

Just say, Akshad, you are saying pit transform, transform,

2:11:56

all here.

2:11:57

You know, we talked about imputation, normalization,

2:12:00

all of these are available.

2:12:02

This will be a great recap of the class classes that we are doing.

2:12:07

Okay, let me recap.

2:12:08

Let me recap the concept.

2:12:09

and I need another 15, 20 minutes here to wrap up those things.

2:12:17

So we have the age column.

2:12:19

Utker says for you, okay.

2:12:21

Age column, the values are 10, 20, 30, 40, 50, and salary column, the values are 10,000, 20,000,

2:12:27

30,000, 40,000, 50,000.

2:12:29

There are five values of age, five values of salary.

2:12:32

So you have to do scaling on this data.

2:12:34

You have to age-ki-upar scaling kering and salary-co-scaling to scaling.

2:12:37

You have to scale the data, right now.

2:12:39

So, what is the minimum value of age, 10?

2:12:43

What is the maximum value of age 50?

2:12:46

What is the minimum value of salary 10,000?

2:12:49

What is the maximum value of salary?

2:12:51

50,000?

2:12:52

EMN and max say salary.

2:12:53

Yeah, men and max say age.

2:12:54

Okay, done.

2:12:56

Simple.

2:12:58

Now, we have to calculate the scaling.

2:13:04

So scaling the formula is, Kutkars.

2:13:06

Scaling the formula says X minus min by max minus.

2:13:09

minus, simple.

2:13:11

You have it.

2:13:12

If you have any value, the scaled value is given by X minus min by max minus mean.

2:13:20

But the value minus the minimum divided by the maximum minus minimum.

2:13:26

That is the way how we do scaling.

2:13:28

Now, if you take a look at the scaled values right now, take a look at it.

2:13:34

Age on age.

2:13:34

First, let's focus on age.

2:13:38

If you see, 10.

2:13:39

minus the minimum. What is the minimum of the age column?

2:13:43

Age column is the minimum 10. So 10 minus 10 divided by max minus means 50 minus 10.

2:13:53

So what kind of 0 is. So, what is the scaled value of age, which is the original age 10 years

2:14:00

say, his scaled value is 0. Okay? We have scaled the data. Next, the original age of the person was 20.

2:14:09

The original age of the person was 20.

2:14:13

What is the scaled age of the person?

2:14:15

It is 20 minus 10 divided by 50 minus 10.

2:14:20

0.25. So 20 minus 10 is 10 divided by 4 is 0.25.

2:14:25

This scaled age is.

2:14:27

Okay?

2:14:28

Both car. Are you with me?

2:14:30

All good.

2:14:31

Look, here here original scale in 20.

2:14:32

Now it's 0.25 will.

2:14:36

Here there 30.

2:14:38

30. 10, calculate for 0.5.

2:14:39

Similarly, 40.75. 50, 1. So these were the original age values. These are the scaled

2:14:48

values. We have shrunk the values in a scale of 0 to 1. This is your scaling. And this kind of

2:14:56

scaling is called min max scaling.

2:14:58

Asi, a other type of scaling which is called a standard scale, but the concept is very similar.

2:15:02

His mathematics is not required. Mathematics here also is not required, but at least I just wanted to show you

2:15:07

how it is going to. So there is one more kind of scaling we have.

2:15:09

have, which I'll show you in the code. And same thing, Utkarsh, we are doing with respect

2:15:14

to the salary column. Now, look, salary's value values 10,000 to 50,000 is there. Minimum

2:15:22

value of salary is there. And here we are calculating the scaled value of salary. What is the

2:15:29

scaled value of salary? The value minus min, so the 10,000 minus the minimum, divided by max minus

2:15:36

minus minimum. So the scaled value of salary is coming out to be zero.

2:15:38

salary. The salary is coming out to be good. So similarly, we are taking another

2:15:45

30,000 minus minimum by this point five. So the best part is that the original values of age and

2:15:53

salary were like this. And after we have scaled the data, the scaled values of age and salary

2:15:59

are coming up this. This is a scaled values of age and the scaled values of salary.

2:16:03

On a range of 0 to 1, this is on a range of 0 to 1.

2:16:06

Okay. Are you with me, Utkars? Comfortable now? This is what scaling is. Okay. Now, this entire thing, in code, okay? So, okay, so, okay, first of all, because I'll make it a point to share all these

2:16:19

snippets with you. Later that I'm like project. So I'm just going to make sure I'll put it right up on your

2:16:25

drive. So this one.

2:16:36

Okay. So I'm just going to.

2:16:42

Okay. So I'm just going to.

2:16:42

Okay. So I'm just going to.

2:17:00

Conceptually, how I'm going to, okay? And now, okay? And then you know, there's two snippets I use, one for

2:17:01

encoding and what for scaling? Conceptually, how it's happening. And now in code,

2:17:07

this is the way how we do this in the code. In code, this is the way how we go, how we go back

2:17:12

and do this. All if you can see. In code, this is the way how we do it. So we use something called

2:17:16

a min-max scalar. So let me take you back to the code. In code, how do we do it? We use something

2:17:22

called min-max scalar. We instantiate min-max scalar. And we use something called fit underscore transform. That's it.

2:17:28

This is the simple way how we do get the code. So the code is nothing but

2:17:31

one second place, I think, uh, so it seems to have hanged. Please allow you in the match.

2:17:46

Now it's fine. Sorry. Zoom was now. Okay. So now we have the code here. And this is the way how we do

2:17:53

midmax scale and in the code. Updak structure from SK learn dot pre-processing. All the major pre-processing libraries are imported from here.

2:18:01

So from SK learn, we are importing min-max scalar.

2:18:05

Scalar equal to min-max scalar and scalar. That's the way how we do it.

2:18:10

Fit transform is the way how we do it. Fit transform. And I will spend some more time talking

2:18:14

about this right now as we speak. Here there are two things. One fit, second transform.

2:18:19

Now, first, fit carer. Fit is that you are trying to learn what is the min and the max. And then

2:18:24

on that basis, you are calculating what is the scaled value. So both of these things are happening

2:18:29

together fit underscore transform. That is the meaning of fit transform. And we are doing

2:18:33

fit transform on the age and the salary economy. That is the way how we have to do it. So libraries

2:18:38

we have to import everywhere. Absolutely. Numphai, Pandas. Jae am we import same way, you will have to import

2:18:44

SKLearn.t. So we are looking at a new library called SK learn. Excuse me. And whatever

2:18:52

machine learning that we discuss in our upcoming sessions going forward, SK learn is going to be the

2:18:59

main machine learning library that we will use in Python. Okay, SK learn will be the main

2:19:05

machine learning library that we will be using Python going forward.

2:19:09

SK learn. What is SK learn stand for? It stands for psychic learn. That is the main machine

2:19:15

learning library will be using going forward. Okay. So this is the way how we do scaling. So just remember

2:19:22

fit underscore transform. That's it. So scalar dot fit underscore transform. We can get the scale value.

2:19:29

So similarly, there is one more kind of scaling technique called a standard scalar. So you don't have to remember it mathematically.

2:19:38

Psychet, correct. No, not, not that. It's actually called psychic, psychit, psychet. That is a full form for a scaler,

2:19:48

a lecture. Okay. So psychic learn will contain all the different machine learning algorithms,

2:19:54

different types of pre-processing techniques. So this all the things your psychic learn in

2:19:58

that go up, okay? Just to clarify. Okay. So this is another kind of scaling technique

2:20:03

called standard scalar, something very similar. This is our mathematics is not required, but what is required

2:20:07

is the, uh, the implementation, fit, underscore transform. Same thing. There's no difference here.

2:20:13

Okay. Now, finally, we will look at another, uh, the, the final thing, very, very interesting topic on

2:20:19

leakage. What is data leakage? Just give me one second, girls.

2:20:26

Browser seems to be a hangy in a little bit.

2:20:28

Let's second to click on my collab notebook for some reason. Just give me one second

2:20:39

second place. They're going to have a mouse going to go and click not going to click

2:20:45

not for some reason. Give me one minute please.

2:20:58

Thank you.

2:21:28

Just give me one minute. I'll give me one minute. I'll try to

2:21:41

to give me one second place.

2:21:58

Let me just a minute race.

2:22:28

Thank you.

2:22:58

Thank you.

2:23:28

Thank you.

2:23:58

Thank you.

2:24:28

Thank you.

2:24:58

Thank you.

2:25:28

Hi, guys, sorry, I'm back, I'm back, I'm back, I'm back, uh,

2:25:32

all you guys, I'm back, uh, just right, uh, just

2:25:47

just restarted my system, uh, just restarted my system. Now's fine, allow me minute.

2:25:52

I will just share my minute. I will just share my screen, please.

2:26:02

All right, perfect.

2:26:32

Thank you.

2:27:02

Thank you.

2:27:32

Okay.

2:27:36

Okay, perfect, tell you let's

2:27:41

there was some, I think now, now, now it's right. Now, now, now it's started.

2:28:01

Okay, let's start on. And the final piece that we are going to do today, the final piece that we're going to do today is something called

2:28:08

data leakage. That's the last part of what I will be covering right now, data leakage. Let us see what

2:28:16

data leakage is and what is the concept of data leakage. Okay, let me scroll all the way down. So we have

2:28:21

talked about scaling. You talked about scaling the concept of scaling. We have seen how to implement scaling.

2:28:27

And this is what I was trying to do in my notebook while my system froze.

2:28:31

you can you can go ahead and see you can you can see all of you here this is the simple way that we discuss how we can go back and do scaling okay very simple uh i will use minmax scalar

2:28:47

so that's the one that we learned right now let us use minmax scalar okay from sk learn dot free processing import minmax scalar that is the library that you want to use whatever i talked about all this while was the concept

2:29:01

whatever be the value, we will shrink it on a scale of 0 to 1.

2:29:05

That is what we are doing.

2:29:07

And remember, the scaling is something we should do only on the numerical column.

2:29:11

Jobin numerical column, that we're scaling correct.

2:29:13

Year column, kilometer driven column and price column.

2:29:16

Only on these columns, we are doing a scaling, right?

2:29:20

So I will choose these three columns and I am doing scalar.

2:29:24

And I am doing scalar dot fit transform, DF encoded columns to scale, fit transform.

2:29:28

So this is my Minmax scalar.

2:29:31

let me instantiate min max scalar here there it is and when i do this you can see all the

2:29:37

values are now shrunk on a scale of zero to one okay so in case you're wondering that sir

2:29:42

so that's not i was using a different kind of scaling concept is the same

2:29:47

sort of a different kind of scaling but min max scalar is what we discussed let's stick to that for now

2:29:51

there are some other kinds of scaling that you will practice and learn data but for now this is

2:29:55

min back scale the concept is what is important code will be the same everywhere

2:29:58

scalar dot fit transform is what we one do two things here one is dot fit when you say

2:30:04

dot fit it is learning it is learning what is the mean and what is the max and dot transform is where

2:30:11

it is doing the actual calculation okay so if you go back to that thing which i uploaded here

2:30:17

when you say dot fit it is calculating what is the mean and what is the max mean or max

2:30:21

and when you say dot transform it is doing the actual calculation that means

2:30:25

value minus min by max minus mean it is doing that actual calculation

2:30:28

and the final end result is these numbers okay so now you can see that kilometer's driven

2:30:33

price here all are in the same scales that's the best thing okay that is the concept of scaling

2:30:38

at a high level finally last thing of the class is data leakage this is what i i'm going to talk

2:30:44

about so um the basic idea of data leakage is what what is what is the basic concept of data

2:30:52

language if you go back to what we talked about in our in our monday session we took a beautiful

2:31:06

analogy of a person preparing for an examination you are preparing for an examination

2:31:12

you have textbooks you have mawk question paper so from the textbook you are learning the concepts

2:31:19

and then you are implementing the concepts on the mock question paper

2:31:22

that is the thing so you are learning the topics on the textbook and based on whatever

2:31:32

topics you are learning from the textbook you are implementing those topics in the mock question

2:31:36

paper you are implementing those topics in the mock question paper right you're

2:31:44

solving the mock question paper I've solved the risk so leakage of

2:31:50

is that the question paper should not get leaked out.

2:31:54

The mock question paper are you should not see that beforehand.

2:32:01

Only then you will be able to evaluate yourself truly.

2:32:06

You're preparing for you, mock question paper,

2:32:08

mock question, uh, mock exam of the first day, you know paper

2:32:12

if that's the mock exam by the point is.

2:32:15

If you have mock exam of some one, two questions

2:32:17

if you go to go and then you go ahead and then you go ahead and then you go ahead and exam exam

2:32:19

exam, then you will get 99% test accuracy, right?

2:32:25

But that 99% of point can I hope everybody's getting the story.

2:32:30

11th May, 11th make a folder here, right? We talked about this.

2:32:34

This is our diagram. We talked about on Monday, right?

2:32:37

Now, look, we are learning the patterns on the textbook.

2:32:42

We're textbook's a pattern seeker.

2:32:44

And joe patterns on textbooks from textbook seeker. And the patterns we're

2:32:47

that we are we are trying to evaluate ourselves on that.

2:32:55

So if any way, it's any way we can get some questions,

2:32:58

question answers, then I will get a high test accuracy.

2:33:03

But that high test accuracy does not mean that I learned well.

2:33:07

That high test accuracy just means I cheated.

2:33:10

Now, as a paper leaked on.

2:33:11

The paper leaked so how does that, how does that test result even matter?

2:33:17

So that is the concept of data leakage.

2:33:19

Same example you have been. It's like a student seeing the exam paper before the exam.

2:33:23

The marks will be great.

2:33:25

Test accuracy will be amazing.

2:33:26

But they have actually learned nothing.

2:33:30

That's the way to be correct.

2:33:32

Okay.

2:33:33

So how do we prevent this from happening?

2:33:42

What is the correct way of scaling the data?

2:33:45

Now, I'm the data scaling away, whatever we talked about all this file, what is the correct way to do it?

2:33:51

This is the correct way to do it.

2:33:54

Upd X sector, what we are doing.

2:33:57

We have X, we have Y.

2:34:00

We do train test split.

2:34:01

We already saw the train test split briefly in the last session.

2:34:05

So train test split we do what we do, guys.

2:34:07

We take the entire X comma Y.

2:34:10

And we split the data 80% into training, 20% into testing.

2:34:14

This is your default.

2:34:15

ratio and the training data is X train, Y train, and the testing data is X test,

2:34:21

Y test. That is what we end up doing in train test plate. Here you specify the test size.

2:34:28

And here I'm giving the name of the scaling. I can use min-max scalar, standard scalar,

2:34:32

or be quite a scalar scaleers. For the content perspective, we can stick to two of them.

2:34:38

And here I will do scalar. Scalar. Dot fit transform on the train data, X-trained data.

2:34:42

So we always only fit on the training data.

2:34:49

That means we learn the patterns only on the trained data.

2:34:53

And based on whatever patterns we learn on training, we implement on testing.

2:34:59

We're not doing.

2:35:00

So if I go back and relate it back to my demo,

2:35:03

we've in demo maybe this thing,

2:35:05

you explained here.

2:35:06

If you take a look at it, the same thing I have explained here also.

2:35:12

Here I have got my DF underscore car underscore encoded, right?

2:35:17

I should not do scaling on the whole data.

2:35:21

This is the full data.

2:35:22

This we're not scaling not.

2:35:24

Imagine the objective is that we want to build a model to predict car price.

2:35:28

That's the objective is.

2:35:29

Like the Spini use case, I started my session with today.

2:35:31

And a spini.com use case was.

2:35:34

Our brand what is, kilometer is, here, how is.

2:35:36

And based on that, you want to build a regression model to predict that its price

2:35:40

is how far and that.

2:35:41

This is your use case.

2:35:42

So, first, you separate for X, what, Y, what, straight forward.

2:35:46

Then, then train test, split, data to split.

2:35:49

Simple thing is.

2:35:50

Until here we are sorted.

2:35:52

You have taken the whole data.

2:35:54

You have split your data up.

2:35:56

80% of training, 20% of it into testing.

2:36:00

Done.

2:36:00

Everybody sorted.

2:36:01

Now we will start to scale.

2:36:04

Now we will start to scale.

2:36:05

Now we first initialize standard scalar or min-max scalar.

2:36:09

Both of them, you can just remember.

2:36:10

Minmack scalar scaleer, we have, we can just remember.

2:36:10

Minimax scalar, we have made mathematically discussed.

2:36:13

Standard scaler, I'm just about you, that's how it's like, so you can instantiate standard

2:36:18

scale.

2:36:19

This is a function type of thing.

2:36:22

And SC dot fit underscore transform on X underscore train.

2:36:27

That means, what you're doing is on the train data, you learn the scaling, you learn the scaling

2:36:34

and apply it.

2:36:36

I'm fit care you, you're fit care, you, you're doing, and then you're just for it.

2:36:40

I think maybe it will be better if I go back and show you in the context of min-max itself,

2:36:47

it will be easier to, for people to digest it.

2:36:52

So min-max-on-kertain here.

2:36:54

And if you take a look at it,

2:36:58

so what is going to happen here?

2:37:01

Conceptually, if I do min-max, let me write it down for you.

2:37:07

So, here is your data.

2:37:10

Data, it's my, this is my data, X, comma, y, hey, okay?

2:37:13

Sorry, that is my.

2:37:15

Yeah, this is my data, X, comma, Y.

2:37:16

What happened?

2:37:40

Thank you.

2:38:10

Give me one second, guys.

2:38:40

Oh, okay.

2:39:10

Thank you.

2:39:40

Thank you.

2:40:10

Okay, I think, yeah, I think the zoom, I think the zoom is creating some issue. Very sorry, guys.

2:40:27

So, coming back to the zoom is creating some issue. Very sorry, guys. So coming back to the scaling part, I was trying to explain this. Let's go back right to the part which I was

2:40:34

I was discussing. And I was just about to use my pen before again, again,

2:40:40

the zoom screwed up. Ah, right. Okay. Let's move on. I wanted to explain this to all of you

2:40:48

nicely, how it's happening. So we have, uh, so we have the price here. All if you can see, we are trying

2:40:57

to predict the price. So first we have data, uh, uh, the first we have data for whatever data we have taken.

2:41:02

We have taken the whole data. And we have split it. Right. We have split the data.

2:41:09

And now this is your entire.

2:41:10

data here. This is your x comma y is. We're

2:41:13

this. We're here. Here

2:41:15

here it's here. X train, Y, train.

2:41:18

X train.

2:41:20

Y train.

2:41:24

And this

2:41:25

is the X test, Y test.

2:41:28

Okay?

2:41:29

This is.

2:41:29

This is your X test, Y test.

2:41:35

Now, one thing I want to clarify to all of you is,

2:41:39

all of you is. All of the things.

2:41:40

that we are discussing as part of data cleaning.

2:41:43

I'm from whatever we have discussed.

2:41:44

We talked about handling inconsistent values.

2:41:48

We talked about handling missing values.

2:41:49

We talked about scaling.

2:41:50

We talked about encoding.

2:41:52

One hot encoding, label encoding.

2:41:56

All of these things that we are talking about.

2:41:58

We are doing only on features, not the output.

2:42:01

We're always X-Pay-Prey-Pen-N-N-N-H-Prey.

2:42:03

Please remember that on a few.

2:42:04

Okay?

2:42:05

So next time when you do this,

2:42:07

min-max scalar dot fit transform, X-Prain,

2:42:10

Now, look, we're X-pacrere.

2:42:11

We're doing it only on the features.

2:42:15

That means we are analyzing the X,

2:42:19

whatever values are coming in X frame.

2:42:22

This can be one value, it can be multiple values, whatever.

2:42:26

So, we are doing dot pit underscore transform here.

2:42:31

Here we are transform current.

2:42:34

And whenever we do pit transform, what is happening is,

2:42:37

we are looking at all the values.

2:42:40

in this column, and we are finding out that,

2:42:43

that the column is, whatever values we have in the column,

2:42:49

what is the mean of it,

2:42:53

and what is the max of it?

2:42:55

That is what you do when you say dot fit.

2:42:57

Now, when you're fit kind of fit,

2:42:58

then you're learning on the training data.

2:43:02

We always do fit on the training data.

2:43:04

We never do it on test.

2:43:05

That's what I'm talking about data leakage here.

2:43:07

And that leakage we prevent, we are always doing.

2:43:10

doing it on train and never on test.

2:43:12

Okay, you can clearly see we are doing dot fit on the train data.

2:43:17

We are learning what is the mean and what is the max on the training data.

2:43:21

And based on that, we are doing the actual transformation.

2:43:25

That means we are calculating the actual scale values.

2:43:28

The value minus min by max minus minimum the chemical calculate proper.

2:43:31

That's the thing.

2:43:32

And finally, on the testing data, we are only doing dot transform.

2:43:36

So whatever patterns we learned on training,

2:43:39

using those patterns, we are going and simply transforming the testing.

2:43:44

Here we have, we're not finding out what is the mean and what is the max.

2:43:50

In the testing data, whatever min and max value we learned on training, we are simply using that

2:43:56

on the testing.

2:43:58

That is the way how we are doing this.

2:44:00

So this is a very, very important thing.

2:44:01

Just remember all of you.

2:44:03

So when you split your data, X train, Y, X test, Y test, Y test, Y test.

2:44:06

Yeah, your template going forward.

2:44:08

I think to.

2:44:09

Today is the first time you're seeing the course.

2:44:10

It might look a little confusing.

2:44:13

But going forward, whenever you're doing any real world machine learning problem,

2:44:17

this your template is going forward.

2:44:20

Okay, so going forward, you will always do fit transform on the X train.

2:44:25

You get the X train scaled values.

2:44:28

And with whatever learnings you had, whatever min and max you learned on the train,

2:44:33

because I always textbook will learn for whatever learnings you had on the textbook, you will

2:44:38

use that and simply transform the test, X test, so scale clear.

2:44:43

And then the final model will be, that's a scaled data on.

2:44:48

If I have to just write it down here, you here, you did all of that and you, you created

2:44:55

X train scale and you created X test scale.

2:45:01

This key up on this up on a model to.

2:45:04

And that's the pipeline of machine learning that we will get deeper into next week.

2:45:07

So that's, we, we're not.

2:45:08

that is not the intent, but just wanted to clarify that now that you have X-trained scaled

2:45:12

and X-stained scale, now you have transformed scaled data been here.

2:45:16

Now, this-upor-upor-up algorithm use of a model-banao-k, dot-fit, and then you will do dot-fitt.

2:45:22

But all of that you are now doing on the scaled data.

2:45:25

Okay, I hope everybody's getting a hang of what is scaling and most importantly,

2:45:33

how do we prevent data leakage? What is the idea of data leakage? So this, this class was

2:45:38

the last part, the last 5, 10 minutes was more about just explaining to you, just explaining

2:45:43

to you at a very high level key, but the data leakage is what is the intuition behind the data

2:45:48

leakage? That's the idea. Okay. Any questions, guys? Any questions, anybody?

2:46:08

Now, exactly.

2:46:38

the learning part on the explain and we are doing the main part on the test correct test

2:46:41

if you have evaluated but no correct absolutely that's what it that's what it broadly refers to yes

2:46:46

that's right you can clear all of you any other questions so just to summarize the conversation

2:46:54

whatever we did if i just have to come back to the notes uh what we did here at a very high level

2:46:59

so i think i think i think again once you get your materials i think this will be a great way to

2:47:04

uh kind of recap the key takeaways we look

2:47:08

at imputation, encoding, scaling and always split before you scale. This was the main takeaway

2:47:13

towards the end of the class, okay? So,

2:47:15

but like, whenever we'll scale, or some, any transformation, you do, always split your data.

2:47:22

X train, Y train, X test, Y test, testing, training, data split it. You learn, you learn on the training

2:47:29

and you apply on the testing. Just keep that to the back of your mind. Okay, so we discuss the concept

2:47:34

behind that. And these are some of the general, uh, very, very,

2:47:38

glossary of some of the important things that we talked about in the class today okay all right

2:47:45

so um any other questions guys all good all good i just quickly mark the topics also what we did today

2:48:08

pretty much based on our content categorical data preparation encoding we talked about

2:48:12

encoding what is label encoding what is uh one hot encoding we talked about that idea as well

2:48:18

we also explored the concept of scaling right what is normalization i'm

2:48:23

mathematically discussed and then at a high level we looked at this and we will apply it it's not

2:48:26

the only class we are doing scaling so next next course when we get into machine learning

2:48:30

how we apply can get in more detail and finally most important we talked about

2:48:35

uh data leakage and also a small summary of all the different steps that we that we apply when

2:48:41

it comes to uh handling messy data what are the things that are involved here okay all right

2:48:47

so uh so that's all from my end thank you all of you uh so i'll pass it over to pratap right now

2:48:53

so thank you everybody and uh next week we start off with machine learning and obviously we'll be using

2:48:59

all of these techniques in a lot of detail in the next class as we go along right and

2:49:06

uh hope you had a good learning and i will see all of you once again in the next week thank you

2:49:10

thank you all of you yeah uh thank you sir for the lecture and i will be releasing the feedback poll now

2:49:22

okay guys so the feedback poll should be live

2:49:30

please fill the feedback form and we can then start with the metimeter quest

2:49:52

shared the link one second okay and where is the okay

2:50:22

Yeah, guys, I'm sharing the screen now and we'll start with the MENTimeter quiz now.

2:50:52

not okay two people have still not answered the pool so please do that and we can start

2:50:59

okay I'll keep sending the link here okay it seems everyone has voted

2:51:11

all right anyone who wants to join the metameter please do so I'll wait for another

2:51:17

for another one minute okay okay

2:51:47

another 20 seconds anyone else who wants to join please join

2:51:58

I'm ending the feedback pool okay all right five four three one

2:52:17

First question is live. Why deleting all rows with missing values may be a poor choice for a small data set.

2:52:27

So if there is a missing value in a row and you just delete the entire row, why could it be a bad idea?

2:52:37

These are fairly simple questions.

2:52:47

Oh, okay. I expected. So, okay, so basically in, if you have a data set, right, and in the data set, there are only like few values, a few rows, right? So, so for example, that card data set with search hold, if you have,

2:53:17

had like what, seven, eight rows at most. If you remove a row just because one row has an

2:53:25

NAN or a negative number, you are reducing the data significantly, right? Because initially

2:53:33

there were eight rows and now you have reduced two rows. So that's like what, a 25% reduction

2:53:41

almost in the data. You have removed a quarter of the dataset. So,

2:53:47

So that is why it may waste valuable information is the correct answer because you don't want to blindly remove data from the rows. I really don't understand why people have selected these two options.

2:54:06

Obviously, it will never create duplicate rows because you're deleting rows.

2:54:12

And this is this does this does this does not even make sense.

2:54:17

changes categorical values into numerical ones. That cannot happen unless you are using some sort of encoding. So, okay, good job to the four people who actually got that correct. All right. Next question.

2:54:47

With statement best describes imputation.

2:55:17

So this should be again another easy easy to solve. Yeah. Great, great. Everyone got that correct. Then what?

2:55:28

Okay. It's a little worried given the previous question. Okay. All right. Great. So yes, it is basically replacing all of the values that are there previously.

2:55:47

It seems we have lost a couple of players. Okay. Lost one more one player it seems. Should I wait or should I go ahead? Thumbs up if I should go ahead.

2:56:17

Okay. It's like 30% of the people saying. All right. Next question then. Yeah.

2:56:30

Okay, okay. I'm going. I'm going that. Why is label encoding potentially problematic for unordered categories?

2:56:38

Remember, label encoding is when you encode things with a number. So if for, for example,

2:56:47

Mumbai, Mumbai can be Mumbai, Chennai, Kolkata. These are unordered categories, right? There is no order in them. And if you use label encoding, not one hot encoding, label encoding to create some sort of encoding that will be like 0, 1, 2, 3 or even random strings. Yes. Great, great, great job. So everyone did that get that correct. Awesome.

2:57:17

I don't think an explanation is required since everyone did get it correct already.

2:57:24

Okay.

2:57:47

Why is calling fit transform on the test set, usually incorrect?

2:57:54

Remember, we call usually, we call fit transform on width set.

2:57:58

Sir just now had covered this.

2:58:02

There were, we split the data into training, test and validation and then we use fit transform

2:58:12

and then after Fit Transform, we get the learned weights.

2:58:25

Okay, great, great, great.

2:58:26

So most of you did get it correct.

2:58:28

It causes scalar or transformer to learn from the test data.

2:58:31

This is what is meant by data leakage, basically.

2:58:36

Okay, there is no, it does not delete any test labels and it

2:58:42

prevents training data from being scaled is just, I don't know. Someone just guessed or something, but then, yeah, it causes the scalar or transformer to learn from test data. That is the correct answer.

2:59:12

I thought it would be the second last question.

2:59:14

But then, okay, that was the, that was a tougher one.

2:59:17

The next one will be relatively easy.

2:59:20

If I remember correctly.

2:59:24

Yeah.

2:59:27

A row appears twice in a dataset

2:59:31

with exactly the same values in every column, which pair of commands is best to detect and remove this issue.

2:59:38

So,

2:59:41

So, yeah, I mean, I'm sure you can guess from the options.

2:59:47

This one shouldn't be too difficult.

2:59:50

Yeah, yeah.

3:0:04

So initially you will use D.F. Duplicated to find all of the values.

3:0:10

values and dot sum is going to give you the number.

3:0:15

So Df dot duplicated is going to give you a list of true, false, true, false.

3:0:21

Better word would be a series of true false for every single duplicate row or duplicate row.

3:0:30

Right.

3:0:31

And then when you do sum, it will just add up all of those truths.

3:0:36

Right.

3:0:37

So you will get the number of duplicated.

3:0:39

duplicated rules and then you can just do df dot drop duplicates.

3:0:44

I mean the correct answer would be to do just df dot drop duplicates, but obviously the question says you need to detect the issue as well.

3:0:54

So the correct answer is then this.

3:0:57

Yeah.

3:0:58

The other options don't really make much sense if you think about it.

3:1:02

So all right.

3:1:04

Great job guys.

3:1:06

And with that we are at the end of the end of the

3:1:09

the session.

3:1:16

All right.

3:1:18

Yeah.

3:1:19

So congratulations, Metal, whoever that was.

3:1:23

And with that, I will end the session now.

3:1:28

Thank you all for joining and I will see you guys tomorrow in the tutorial session.

3:1:34

I hope you have, I hope you try to solve the assignment.

3:1:37

And if you have any doubts.

3:1:38

have any doubts I'll address those okay all right then bye bye guys have a good

3:1:45

