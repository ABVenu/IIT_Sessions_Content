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

Hello, good evening everybody. Yeah, we will just be starting on.

16:54

Thank you.

17:07

You

17:24

Thank you.

17:54

All right, guys, we'll get started.

18:24

here and today's session will be on data leakage and class imbalance.

18:30

A very interesting topic will be will be doing here.

18:34

All right.

18:54

I have a bit of a cold today, guys, so I'll still try to be as energetic as possible, but just do forgive me if, you know, my energy is lacking a little today. Okay.

19:16

Okay. Anyways, let's let's get going. Let's get started.

19:24

And we'll be, just to lay down the context once again, we'll be talking about data leakage and we'll understand what data leakage is.

19:32

We already briefly introduced that in the last session.

19:35

We talked about what data leakage is and very broadly speaking, we are always trying to fit the model on the training data.

19:45

We are always trying to fit the model on the training data and then we are trying to do predictions on the testing data.

19:52

We should never do any kind of.

19:54

kind of fit on the test data. That's the idea that we talked about, right? The analogy that we

19:59

took about, we took in the last session was we talked about the example of a live examination.

20:07

Imagine you're taking up a, you're preparing for an examination. So the idea would be that you will

20:12

always, you will always go back and prepare from the textbook and based on whatever you prepare from the

20:19

textbook, you will go and solve that on the unseen question paper. You will, you will, you will, you will, you will

20:24

evaluate yourself on the unseen question paper, right? So you should not see the question

20:29

paper in advance. That's the idea. You should not see the question paper in advance, right? That's that's

20:36

one important thing to keep in mind. Okay. So if you, so you cannot go back and effectively

20:44

take the test data and do some kind of fit on it. Okay, so that's the big picture idea of what is

20:49

data leakage. So we'll start from there and we'll look at some other things as we go along.

20:54

So, this is the Jupiter notebook for our session today, 18th May. I've already uploaded that.

20:59

There's a lot of stuff here. You'll see. And this is the main notebook that we will discuss. And I will also

21:04

talk about a small, excuse me, kind of a template, just a small PDF that I'll walk you through,

21:13

which talks about the things that we will discuss. Okay. So what is data leakage once again? What is the

21:18

concept of data leakage? Okay, data leakage as we as we say is like a silent cheater, right?

21:24

Why do we say it's a silent cheater? Because if you remember the example from our last session,

21:29

last class may, whatever example I took up. If you remember, we did min-max scalar,

21:34

okay. And I think it'll be best if I take you back to that notebook and discuss today's 18th May. Last

21:40

session was, I think, on 13th, 13th, 13th, there is our demo file. It'll be best if I just take you there

21:48

and show you. So, and if you remember, towards the end, we talked about, we talked about,

21:54

something called min-max scalar. Let me take all, take you all the way down. So we started

22:00

talking about feature scaling, what is feature scaling. Then we just discussed about something

22:04

called min-max scalar. We've made a min-max scalar concept we discussed about. We also talked about how it's

22:08

happening. So you take the entire column, you find out what is the minimum and maximum value in the

22:13

column, and then you do the scaling. And what is the formula for scaling? You take the value minus

22:18

mean, divided by max minus mean. So that is the way how we go back and do the scaling, right? So we do the

22:24

value minus mean divided by max minus min. So that's the way how we go back and do

22:30

mean max scaling here overall, right? That's the intuition. So everyone can see. And here is

22:38

the concept of how we did data leakage in our last session. If you remember, we took the card

22:43

and coded data and we instantiated minmax scalar and I did fit transform on X train and I did transform

22:49

on X test. This is the important thing how we should go back and do it. This is the

22:53

actual practical real world way how we should always build pipelines in machine learning right you

22:58

can see we are not doing dot fit on the whole data right because the whole data will include

23:04

training data as well as testing data we are not in we are not going back and doing dot fit on the entire

23:09

data we are going and uh doing fit and transform on the train and when i do fit and transform on the train

23:18

what is happening it means on the training data whatever features you have whatever columns you have we are

23:23

learning what is the minimum value we are learning what is the maximum value on the

23:28

features and based on that we are doing the scaling so that is the fit and transform fit is

23:33

basically learning fit means we are always learning something when i say dot fit

23:37

dot fit basically means you're learning something and dot transform means based on whatever you

23:41

have learned you are transforming that particular column you're doing value minus min divided by

23:46

max minus mean i hope all of you recall that i think this was the that beautiful explanation we did last

23:51

session if you remember so when i say dot

23:53

fate we are literally we are literally calculating for every column hey what is the mean

23:58

and what is the max and when we are doing dots transform we are going and taking each and every

24:03

value and we are doing value minus the uh value minus the um excuse me

24:10

value minus the mean divided by max minus min so this is what we are doing behind the scenes okay

24:16

i hope everybody is clear how we how we but this is a

24:23

and transform on test okay now from that let's come back to the uh to our current uh notebook

24:32

and i'll simply take you through the flow in today's session it's a comparatively easy session

24:37

i think the concepts are all pretty much sorted initial part we will see the data leakage

24:42

part one is completely on data leakage we'll talk about leakage through feature scaling so some part of

24:47

it is very much related to what we already discussed last session if you remember see this is

24:51

minmax scalar we are again taking minmax scale today

24:53

right so it'll be a bit of an overlap we've already seen this part okay and then towards the

24:58

end we have got a class imbalance and accuracy so we'll talk about something called accuracy

25:03

precision recall at a very conceptual level today okay and then i've given some claggle exercises

25:09

and all so it's a competitively lighter session that we have today now first of all we start with

25:14

the concept of leakage via missing values imputation so last session we did take some time and

25:21

discuss about different types of imputation techniques

25:23

right so we talked about how do we do fill any if you have if you have if you have nan values or

25:28

any values how do we go back and impute them we talked about some of those things as well in the

25:33

class right so what is the way we impute the values and all we discussed about you know those

25:38

foundations so data imputation is something we you know we covered and if you uh

25:44

if you go back and remember the conversation we use the basic python methods we did not

25:51

really use any framework right so if you

25:53

you look at it we did we did not really use any frameworks per se we didn't use any frameworks

25:59

per se we just use used you know basic approaches for doing the imputation right so what we are

26:05

seeing today we are actually using a framework called a simple imputer that is what we are

26:12

using today so this is my data set first of all first of all what i've done is i've just curated a

26:16

simple uh data set all if you can see right so it's a it's a sample data that i'm creating right now so

26:23

student a column has score a column and this is your data set right now everybody can see this

26:31

and i've also done the train test plate a very basic train test plate i've done

26:36

test size equal to 2 test size equal to 2 so by the way this is very interesting we can say

26:42

test size equal to point 2 that is how we did in the last session if you say point 2 that means

26:46

fraction is taken that means 20 percent of the values are used for testing that is the intuition behind

26:52

that is the intuition behind when i say test size equal to point 2 okay but when i say

26:58

test size equal to 2 what it means is that i'm keeping aside 2 rows of data for testing

27:03

i've got overall 6 rows of data and out of overall 6 rows of data i'm keeping aside 2 rows of

27:08

data for testing so that is the test size equal to uh 2 that we have done right now all if we can see

27:13

so this is nothing but the training data and testing data that you can see on the screen

27:18

and very clearly on the training data you can see that the score has a nan value so we already

27:22

talked about this last session what are the different ways to do the imputation we have mean

27:25

imputation we have median imputation and we also talked about a very practical way of imputing the missing

27:31

value so the so the practical the practical is that you can predict what is that missing

27:36

value going to be based on the other parameters okay so as we get deeper into ml we will

27:41

see those techniques because today you will not be able to relate to that i think once we get

27:45

into regression classification uh two three weeks from this from today you'll be able to relate to it better

27:51

how do we impute missing values using other features okay but here uh we will do a simple mean

27:57

imputation so mean imputation how did we learn this in the last class so we simply do use something

28:03

called fill in a right we simply did fill in a replace function fill in a these are the things that

28:08

we can do and at a very basic level we can go back and do uh mean imputation right we can impute with the

28:14

mean of the particular column turns out that there is something called simple imputer which can do the

28:20

exact same thing in a better way right because all your mean imputation and all that we were doing on the

28:25

entire data we were not actually splitting and doing it in a certain way but and but today we

28:30

understand the concept of leakage we understand that so so the principle that we learned

28:37

is that we will always take the data and we will always first do the split even before you

28:43

start with anything else you should always go back and do the split first you should take the entire data

28:48

and you should always split your data you should always split your data into what is training and

28:52

what is testing so take the data and please split your data into what is training and what is

28:57

testing and then on the train data you go and do your workflow

29:02

train data may go after impute or whatever you want to do right so for example if i talk about this

29:07

current exercise uh so you've got 40 60 80 and nan right so it is your training data now imagine

29:13

we are doing a main imputation so mean imputation until last week was what until last week we

29:18

mean imputation was like you take the entire column and you find out the average across the entire

29:24

column and based on that you impute the missing value based on the average that is what we discuss right

29:30

so today we are going to tell a different story today we will say that we will first take the

29:35

whole data we will split the entire data into training data and testing data okay so we'll take

29:39

the whole data split into training data testing data whatever we have done okay that is sorted

29:44

and on the train data we will do a fit transform so whatever trained data we will do a fit transform so whatever

29:48

we have got right now on the training data what we will do excuse me on the training data we will

29:54

go back and do a fit transform okay that means on the trained data we will learn what is the mean

30:01

so what is the average on the training data 40 60 80 average so we will use something

30:07

called simple imputer we will use something called simple imputer that will do exactly this work

30:11

right we will say strategy equal to mean and when we said dot fit dot fit always always

30:18

means that we are learning something we will learn the math from train that's what i meant

30:22

right so we will we will we will learn the math from the from the train that's one way to look at it

30:28

okay that's the that's the that's the way to look at it so we will learn the math from the from the

30:35

train okay so whatever training data you've got 40 60 80 we are learning what is the average

30:39

or what is the mean from the training data so mean kittal

30:43

but if I use simple imputer the mean will be 60 okay we learn the mean to be 60 so so when

30:50

I say fit underscore transform give me one minute I'll just use my pen allow me a minute I'll

30:55

just take out my marker pen just a minute guys just give me a minute okay

31:13

Thank you.

31:43

Thank you.

32:13

Thank you.

32:43

Okay, just got it here.

33:13

So, guys, as I said, you know, I'm just going to, just going to demonstrate this for you

33:30

once again. So we have the data and we have split our data into training data and testing

33:34

data, right? And when we use simple imputer strategy equal to mean what we are doing is,

33:39

so if I, if I say simple imputer, I'll say simple imputer dot fit under

33:43

transform. So moment I say simple imputer dot fit underscore transform, what will it do? It is doing

33:51

two things. One, it is looking at the train data. It is looking at the training data. And based on

33:57

the training data, it is finding out what is the mean. We are doing strategy equal to mean.

34:01

So based on the training data, we are finding out what is the mean based on the training data,

34:06

right? And based on whatever average you find out on the training data, we are transforming the testing

34:12

data that is what we are basically doing here okay so we are taking the data we are doing

34:18

a dot fit on the entire training data and whatever mean that we find on the training what is the

34:24

mean on the training 60 because on the training data the mean is very clearly 60 now so fit will

34:33

learn what is the mean on the mean on the training and whatever mean that we found on the training

34:37

data now what we will do we will go back and transform that means we will impute that n

34:42

with 60. That's it. So the final resultant set would be, the final result and set that you

34:49

end up getting would be 40, 60, 60 80. This nan will be replaced by this nan will be replaced by 60.

34:55

So that is what will happen. Let's say. So end result, what will be like imputed train. And what will the

35:05

imputed train look like? The imputed train will look like. The imputed train will look like.

35:12

something like this. A40. Let me write it down. A40, B60, right? Um, C 60 and D80. That is how the whole imputed train will look like. Okay? I hope everybody's clear. And now coming to the test data. What are we going and doing on the test data? So on the test data, we are going ahead and

35:42

we are going ahead and whatever patterns we used in, whatever patterns we used in the train,

35:49

we are going ahead and we are simply going ahead and replicating those patterns in the test. So whatever

35:54

patterns we learned on the train, so we learned a pattern which is mean equal to 60. So whatever pattern we

36:00

learned on the training data, I'm simply using that particular pattern on the testing data.

36:07

So let me just go back and do this thing. So s, sI dot transform.

36:12

I will do S.I.D. Transform. So I'm not doing fit transform anymore. I'm simply doing

36:18

S.I.D. Transform. And I will get imputed test. So what I'm getting right now is imputed test.

36:26

So, you're here here 60 learned here. That same 60 will be used to impute this.

36:33

As not that test, we're back saying, we're going to mean calculate and do. That is not what we do. Whatever

36:37

average we calculated here, the same average is used to impute here. That's the intuition.

36:42

right? So I will just go back and do this thing. E and F.

36:51

So we already know F is 90. And what about E? You will impute nan with 60. That's it. This is how

36:57

your final results. Results it will basically look like. Okay. I hope this is absolutely clear.

37:02

All right. Now we will go and implement this thing in the code. Let us see how this looks like in the code.

37:09

Let us see how this looks like in the code guys.

37:12

Thank you.

37:42

Now I'm going to just clean this up a little bit the visualization here I'll keep the visualization here itself.

38:12

I just wanted to show you how exactly we have done this.

38:14

That it can very beautifully relate what is basically going on, right? You can see here.

38:24

What we have written in the training?

38:42

Thank you.

39:12

Yeah, just to answer your question, what we have written in the training data means 9 equal to 60. Correct. Correct. In testing data also 9 is 60. Exactly. Exactly. That is exactly. That is exactly. That is exactly how I imputed this thing. Can you see?

39:40

That is exactly how I imputed the data here.

39:42

training data may we are learning the pattern.

39:47

So we learned that 9 is equal to 60 in the training data.

39:50

And based on whatever pattern we learned in the train, we are simply going and using that same pattern in the test.

39:59

That is exactly what we did. And if you take a look at the code right now, that is exactly what we are doing in the code.

40:04

We are saying dot fit of DF train score.

40:08

We are saying dot fit of DF train score.

40:12

That means we are.

40:12

We are learning the patterns. We are learning the mathematics on the training data, right?

40:18

What it means is we are learning the mathematics on the training data and whatever math we learned

40:23

on the training data, we are going and implementing that on the train data and the test data. Got it?

40:37

If I go and run the code, this is what you will be able to see. Exactly what I showed here.

40:42

This is exactly what you will be able to see.

40:44

Let me show you the whole view together.

40:46

So you can see the, the diagram that I drawn.

40:50

And you can also go back and see the exact transform data that we are able to see.

40:58

Okay.

41:00

Akshad, I hope that answers your question.

41:09

Okay?

41:10

So simple enough, the code is simple enough.

41:12

And this will be true for every kind of transformation.

41:15

Right now, we are starting out with imputation, but going forward whenever we do any kind of data

41:20

transformation, any kind of imputation or any kind of data transformation when we go and do,

41:25

it will be the exact same set of steps we will follow. It will remain exactly the same.

41:35

All right. Now, let's move on.

41:40

Can I move on? Everybody is clear. Any.

41:42

questions on this. Let me pause for a minute here. Any questions. I hope this is clear.

41:47

So this is, this is giving you a slightly different idea in terms of how we do imputation, right?

41:51

All this while we were doing imputation using, I know, we were doing imputation just using

41:55

panda's methods, fill and a right? And you can see the difference right now. Now we can do the train

42:00

test split. And now we can do a much more better way of imputation without any leakage.

42:07

We can avoid leakage and we can go back and do imputation. That's the, that's the intuition, right?

42:12

So this is what is going on right now. Everybody can see.

42:17

Let's move on to the next one.

42:19

Leakage via feature scaling. This we already talked about last session. I will just repeat the same

42:24

flow right again. And you can again see. We should never go back and do it this way.

42:31

So first, this is my data, right? This is my data set. Attendance percentage, attendance

42:35

average, target. So this is the this is the dataset that we have right now. I've just created

42:40

a simple sample data right now. So based on your attendance percentage,

42:45

based on your attendance assignment average, you are trying to predict whether the person

42:48

will pass or fail. Okay. So that's what we are trying to predict. Let's say. That's the use case

42:54

where one stands for pass and zero stands for fail. Okay. So everybody in the audience can

43:02

understand what is X and what is Y. So X is nothing but this. That is your input X and this.

43:09

Right. So input X is nothing but your percentage, how, how much attendance you're getting

43:16

in the classes and your assignment average. How much of test scores you're getting? That is your input

43:21

X. And based on that, we are trying to predict what the target will be. We are trying to predict

43:30

the target on the basis of this. So we are trying to predict what is the target on the basis of this.

43:36

That is the problem that we are trying to predict.

43:44

So as you can clearly see, the attendance and assignment values are coming out in, they are basically

43:51

the attendance and assignment values are in different scales. They are basically on a scale of

43:56

0 to 100, right? They are in very different scales. But I want to go and scale my data.

44:02

That is the use case we discussed already. We should do scaling.

44:06

But and also remember what we are doing here, we are simply taking X and Y.

44:11

So whatever target column you have, we are dropping the target.

44:16

So everything else is part of my X, right? We can relate to that.

44:20

So if I just go and print out what is X right now, this is my data, the complete data frame.

44:25

But if I just go and print out what is X, X is nothing but these two. We cannot relate to it, right?

44:29

This is my X features. And what is my Y? My Y is nothing but my target. My Y is my target. That's it.

44:36

So X and Y split we have done. Next, what will we do? Next, ideally we should go and do.

44:43

Ideally we should go and do train test split. That is the ideal thing. Next, ideally we should

44:49

do train test split. What we are not doing that here. Ideally we should do train test split,

44:54

but here we are going and doing fit transform on the entire data, on the entire X. Now one thing I

45:00

also want to clarify, remember friends, these are all what we refer to as data pre-processing.

45:06

techniques, right? Even last session, part of what we discussed and, you know, today,

45:10

whatever we are seeing, these are all what we refer to as data pre-processing techniques, right?

45:15

Please remember, these data pre-processing techniques cannot be done. These data pre-processing

45:23

techniques, they cannot be done on the, they cannot be done on the outputs. We should always perform

45:33

these kinds of pre-processing techniques on the features.

45:36

not on the outputs. That is one important thing to keep in mind. So we are simply taking

45:41

the entire data, X and Y. X is nothing but the input, Y is the output. That is sorted and then we are

45:48

simply saying fit transform of X. But this is not the right way to do it. This is not the right way to do

45:53

it. We should always go and split the data, train test split we should do and then we should go back

45:58

and do this thing. This is what I wanted to show you that this is wrong, leakage occurred. Why,

46:04

why do I say leakage occurred? Because the scalar learned the minimum and maximum of the test data

46:09

before the split. So the moment you say min-max dot fit transform, right? The moment you do this,

46:17

you know, if you want me to go a little deeper, I can do that. Let me, let me go a little deeper and show you.

46:22

Very interesting. It's very interesting, you know, there's no end to what we can do, basically.

46:26

So the moment I go back and do this, when I say min-max, see, very interesting, like moment I start

46:31

typing in collab, what did I do, I just type min.

46:34

As I have typed here, Kolab, we automatically it's giving a tab, right?

46:38

It is automatically giving me a kind of a, this thing.

46:44

And when I do a tab, you can see, data underscore min,

46:47

right? That means, it is telling me that, hey, whenever I did that dot fit, whenever I did that dot fit

46:54

and transform, whatever I did, okay? So, what is the minimum value we learned?

47:01

And at the bottom, I can also pretty.

47:04

out. Again, I'm able to Min Max. And Collab is automatically figured out. Gemini is

47:10

automatically figure out. I want to know the maximum. What is the maximum value I learned?

47:15

And this is the interesting part, guys. Because if you look, we have actually learned the

47:21

mean and max from the entire data. Because we have put the full X on it. This is galathe. So this,

47:27

this is to tell you the mistake. Mistake is. Mistake is that we have data not split

47:32

not really. We should always split the data and do it. Exactly what I explained here, right?

47:37

I explained this to you here. You should always take the data. The first thing you should do is

47:41

is train to split. Then you should apply your transforms. But, excuse me, if we go and do it

47:47

this way, if we go and do it this way, if we go and do it this way, if we go and do it this way,

47:52

this is the incorrect way of doing things. Now, look, this whole data we, we've found out what

47:57

these two column of mean what is? First column of minimum is 65.

48:03

But second column's minimum, I think, around 45. That's what we are able to figure out.

48:09

First column minimum is 65. Second column minimum is 45. And if you look at the data max,

48:18

we are finding out what is the first column max. And we are finding out what is the second column

48:23

max. First column max key is the second column max. We are able to find out what is the second column max. We are able to

48:27

that out. That's the intuition, right? We are able to find out what is the first column

48:33

max value and what is the second column max value. That we can find out. That we can find out. That's what

48:40

we are able to see. So, you can take a look at it, all of you. Data main, data max, right?

48:46

Problem is, we're putting on the whole data on. This is, we're not going to. So what is the

48:51

right approach? What is the right approach? Let's see that. The right approach would be,

48:57

this. We'll data split kren test split x comma y test size equal to 0.2. So 20% of my data

49:05

is going for testing. We have seen this already in the last class. So you have your X train,

49:09

X test. We are not concerned. Because remember, all of what we are discussing. All of what we are

49:18

discussing is is always on the, is always on the, uh, uh, features, inputs. X pay for

49:26

even this technique what we are discussing this technique is. We use a term called

49:34

feature scaling. What do we call it? We call it feature scaling. And broadly, collectively,

49:44

all these techniques are what is referred to as feature engineering. Let me use one more word.

49:52

We have actually mentioned these terms before. Just trying to mention it again. We have feature

49:55

engineering. So we are, as you can see, we are using the term features. We are

49:59

engineering the features. Whatever original features are there, we are trying to take the original

50:04

features and we are trying to create better features out of it. That is what is referred to as

50:08

feature engineering. We have an original set of features or inputs and we are using the original

50:13

set of features and we are trying to create better quality features. So feature scaling is a kind of

50:18

method, imputation is a kind of method. So all these are part of feature engineering methods.

50:23

Khabi khabbaughan, um, this data pre-processing be kate. So when we say,

50:25

So when we say data pre-processing, this is what we are trying to see.

50:30

Data cleaning, data pre-processing is basically nothing but feature engineering.

50:33

And we are doing this operation only on the X.

50:37

Now, you ask you, sir, outputs, why not? Why not? Because output to

50:40

know, when you're dealing in the real world, what are we trying to do in machine learning?

50:47

Based on X, we are trying to predict why?

50:50

Yeah, training data, you have up to output there. But when you're trying to ultimately make a prediction,

50:54

you have that you have there output data not there.

50:58

That is the reason why these operations must never be performed on the outputs.

51:02

So they are all with the features.

51:06

Just to summarize once again, guys, I hope everybody's aligned.

51:09

So we talked about why we should not do this on the whole data?

51:13

Because leakage occurred.

51:14

So we should always do the train test split.

51:16

This your training data, or your testing data is sorted.

51:20

Now what we can't?

51:21

Industry standard way.

51:22

What do we do?

51:23

We always do.

51:24

We always do fit, transform, extrane.

51:29

And this, the thing is, we, we it's going to side-sat-sart,

51:32

we can it separately, we can't.

51:34

In books and articles, you will see people write it separately.

51:38

They write fit separately, transform separately.

51:41

So people write fit and transform separately. In books and articles, that's how they do it.

51:46

Right? So fit and transform are not the same here.

51:48

So you're fit-alach-alach-alike-s-sac-sac-sac-sac-said. So fit and transform,

51:52

and transform when you're applying together, what it means is, first you're learning the patterns

51:58

on your X-Strain and you're getting X-rain scaled, and then you are simply saying min-max

52:03

dot transform. That's the intuition. And I think you can relate to it. This is exactly what I explained

52:09

in the first part of my session. Yeah, I have explained here, right? Let me just undo this for a minute.

52:16

Just a minute, guys. I wrote some other stuff here actually. Now look, this exactly the what I discussed.

52:21

Nothing is different. I started my class with this today. So data, train test split.

52:26

This is what we get. We are doing fit transform. We are getting the train, the scale train data.

52:32

And we are doing dot transform and we're getting the scale test data.

52:36

Scale train, imputed train, because feature engineering we are doing.

52:40

Split is not actually called feature engineering action.

52:43

Split is the first part that you are doing. Split is more like data splitting we are doing. So

52:47

split-ca-back-john-jure that is called feature engineering. What is?

52:51

is not feature engineering because split is what what is split split is

52:55

nothing but you're taking the entire hundred rows of data and you're simply going and saying

52:59

80 percent of my data is this 20 percent is this that's it that is for split and so split may

53:04

we are not doing any feature engineering right got it i hope you're okay

53:09

okay okay so now moving on and this is the same way we will be doing this is the same way we will be doing this

53:21

overall you can see another very interesting use case right now i have a diabetes

53:27

data set i will take a simple uh simple diabetes uh data set right now just to kind of

53:33

demonstrate a practical case study so what i will do i will just quickly uh

53:41

share a diabetes data set with you so it's a very interesting uh real world case study

53:48

where we are looking at the different features of a person

53:51

and based on the different features of a person we are trying to predict whether a person

53:56

is diabetic or the person is not diabetic that is what we are trying to predict okay so

54:01

based on the different uh features of the person we are trying to predict is the person

54:05

diabetic or is the person not diabetic that's the use case okay so let me go and quickly

54:13

read through this data set just give me one second

54:43

I'll just quickly download this quickly download this,

55:12

solve in the folder and just to give you a little bit of context in terms of what this is

55:17

so you can see we are looking at the different uh features of a person it's a cagull data set actually

55:22

so maybe it'll be better if i ask you to just read through the real world caggle exercise once

55:29

just to get a sense of what this problem statement is all about then we will discuss okay this is the

55:35

cagull case study this is a real case study where we are actually applying machine learning all of you can

55:41

can give it a glance once then we'll discuss okay you can just give it a

55:53

basic here just glance through it what what the problem statement is and all that's it

55:58

just give it a glance and then we'll discuss

56:11

I don't know.

56:41

Thank you.

57:11

Thank you.

57:41

You don't have to read through the features in detail.

58:11

many take me. I just try to understand the context. It's a very, very popular data set in machine learning.

58:17

Then up, we will discuss.

58:41

Thank you.

59:11

Thank you.

59:41

Thank you.

1:0:11

Thank you.

1:0:41

Okay, guys, I hope everyone's gone through it.

1:0:57

So we are looking at the different features of a person and based on that we are trying to predict is the person suffering from diabetes or not. That's what we are trying to do.

1:1:07

Now, you see, here here, data explained the data set, same data set we are using right now.

1:1:14

So we are looking at the different features of the person.

1:1:19

Pregnancies, glucose.

1:1:21

Glucose, what the blood glucose. How much of blood sugar you have got?

1:1:24

Okay?

1:1:26

Blood pressure, skin thickness, insulin, BMI.

1:1:30

All these are the features of the person.

1:1:32

And based on that, we are trying to predict is the person suffering from diabetes or the person is not suffering from diabetes?

1:1:37

So, 0 means the person is not suffering from diabetes, and 1 means the person is suffering from diabetes.

1:1:44

Okay? So, based on all the different features of the person, we are trying to predict is the person suffering from diabetes or not.

1:1:52

So, the outcome variable is what we are trying to predict.

1:1:55

Yeah, the outcome 1 or or outcome 0.

1:1:57

Okay? Okay. Outcome will either be 1 or outcome will be 1.

1:2:00

or outcome will be 0. That is what we are trying to estimate right now.

1:2:03

Outcome will be 1 or outcome will be 0. That is the thing.

1:2:06

Okay? I hope this is clear. Everybody is aligned. Now, moving on.

1:2:16

Um, yeah, yeah, it's a different patients, obviously, right?

1:2:24

Every row, Arnica, corresponds to a different person, right?

1:2:28

Every row is a different person. Obviously, each and every row is a different person.

1:2:36

So, this is person 1, person 2, person 3. Yeah.

1:2:43

So now what I will do? Let me quickly upload my data here.

1:2:46

Ah, whether that is part of the data. So that is, I think, that is part of your data only.

1:2:52

And it is actually a very diversified sample set that is taken here, actually.

1:2:57

Okay. I will upload my data first. Let's go on. Let me upload my data.

1:3:02

I'm going to quickly upload my data here.

1:3:06

So, excuse me, guys.

1:3:25

So I've uploaded the diabetes.

1:3:26

CSB data set you can see right now.

1:3:29

Okay.

1:3:36

I will load the data into a Pandas data frame.

1:3:40

So this is p.d.

1:3:41

REATCSV.

1:3:43

I will load it into a Pandas data frame.

1:3:49

And you can clearly see this is exactly the data that we discussed before, right?

1:3:54

So every row stands for a person.

1:3:57

And we are looking at the different, different features of the person.

1:4:01

We have pregnancies, we have glucose, we have blood pressure, skin thickness, insulin, BMI.

1:4:06

So these are different, different features of the person we are seeing.

1:4:10

And based on that, we are trying to predict the outcome.

1:4:14

The outcome is what we are trying to predict.

1:4:16

So based on all the different, different features of the person,

1:4:20

we are trying to estimate what is the outcome.

1:4:23

Outcome will be either one or outcome will be zero.

1:4:25

Outcome one means person will have diabetes.

1:4:28

Outcome zero, means person will not have diabetes.

1:4:30

Simple.

1:4:31

Straightforward, okay?

1:4:33

Now, here here we have inmax scaling.

1:4:35

what we will do? Same story, you drop the outcome column rest, everything else is part of my X, right?

1:4:42

You drop the outcome column, everything else is part of my x, and outcome is part of my Y.

1:4:50

That's it. Okay?

1:4:53

So you drop the outcome column.

1:4:56

Everything else that we get is part of my input X and outcome is part of my output Y.

1:5:02

Outcome is output Y.

1:5:04

So that is output Y.

1:5:05

is what we are able to see on the screen right now.

1:5:06

Outcome is output Y.

1:5:08

Train test split.

1:5:10

Same story.

1:5:11

I will use Minmax Killer.

1:5:12

I will use Min Max Killer, but we already covered.

1:5:15

And here again, fit transform on X train.

1:5:18

I'm scaling the train data based on whatever patterns I learned on training.

1:5:24

And based on those same patterns, I'm transforming the test data.

1:5:28

And now, all along the way, I'm doing it only on the X's.

1:5:32

We don't touch not.

1:5:34

Outcome come touch.

1:5:35

Okay?

1:5:36

This is your transformed data frame.

1:5:38

Look at this all of you.

1:5:39

This is your input, features.

1:5:41

So PD.

1:5:42

Data frame, X train standard.

1:5:44

Yeah, your X train standard.

1:5:45

Column names we can replace.

1:5:47

How many columns are there?

1:5:48

How many features are there?

1:5:49

There are eight features.

1:5:50

0, 1, 2, 3, 4, 5, 6, 7.

1:5:52

There are 8 features we have right now.

1:5:54

So these are a total 8 features that you are able to see right now.

1:5:57

These are the 8 features that we are able to see right now.

1:6:01

All of you can take a look at it.

1:6:03

Okay?

1:6:05

I hope everybody is clear how we go and do scaling and what is the meaning of scaling.

1:6:10

The concept should be clear.

1:6:11

And scaling is a very, very important part of how we do real world problem solving.

1:6:16

Whenever you are doing any kind of real world problem solving, scaling is a default thing that you will always go and do.

1:6:21

Always, always.

1:6:22

Whenever you get any data set, you will always go and do scaling.

1:6:25

Always.

1:6:26

Just one small thing, we have discussed this last class also, guys, remember,

1:6:29

we're scaling encoded values but not going.

1:6:32

Just keep this at the back.

1:6:33

of your mind.

1:6:34

Normal values will come,

1:6:35

encoding not going.

1:6:36

Okay?

1:6:37

So just keep this at the back of your mind, all of you.

1:6:40

All of you.

1:6:41

Now, let's move on.

1:6:42

Let's move on.

1:6:45

Let's move on.

1:6:49

And now we will get to the next part of my conversation,

1:6:54

which is called class imbalance.

1:6:56

What is class imbalance?

1:6:58

What is the meaning of class imbalance?

1:7:01

So,

1:7:02

So, all of you remember, classification problems that we studied on the,

1:7:08

in the very first session that we discussed,

1:7:13

we discussed about classification.

1:7:16

Classification use cases I discussed here.

1:7:19

And what are we trying to do?

1:7:24

What are the two different types of machine learning?

1:7:27

In one type of machine learning, you are trying to predict only the numerical outputs.

1:7:31

In one type of machine learning, you are only trying to predict what are the numerical

1:7:36

outputs and that is what is referred to as regression.

1:7:40

So regression is that type of machine learning where the output is a number.

1:7:46

We are trying to predict a numerical output.

1:7:49

That regression is, right?

1:7:52

Or you actually in what detail in the next class onwards, we are actually getting deeper into regression, classification.

1:8:00

I haven't models not made.

1:8:02

All this file, if you see our conversations,

1:8:04

we've actually just talked about the basic ideas of ML.

1:8:07

We are still yet to build a model.

1:8:09

That is, that is the part we are yet to see.

1:8:11

We have only talked about how to split,

1:8:12

how to handle meeting missing value, data leakage.

1:8:15

We are talking about all the other prerequisite concepts so far.

1:8:18

But I'm actually models of that now that we will start from the next class onwards.

1:8:22

But anyways, we have talked about regression,

1:8:25

where we are trying to predict a numerical output.

1:8:29

So regression is where we are trying to predict

1:8:30

trying to predict some kind of a numerical output.

1:8:33

And classification is where we are trying to predict a kind of a categorical output.

1:8:38

So that is what we are trying to do in classification.

1:8:41

We are trying to predict a kind of a categorical output in classification.

1:8:44

So, if you look at a real world scenario,

1:8:48

as you are able to see on the screen right now,

1:8:51

this is a credit card fraud detection use case.

1:8:55

Very common use case. I don't have to talk about it.

1:8:57

If you look at all the major credit card companies,

1:8:59

credit card companies out there,

1:9:01

Oh, excuse me guys, Visa, MasterCard got, American Express,

1:9:04

okay?

1:9:05

You guys are all using credit cards, right?

1:9:08

Yeah, there are debit cards.

1:9:10

I don't want to just say credit cards.

1:9:11

Debit cards are up, UPI go.

1:9:13

They're all telling the same story, basically, okay?

1:9:17

So, you might have seen sometimes when you do a transaction,

1:9:20

when you're transactions are you,

1:9:22

and if it's a highly risky transaction,

1:9:25

imagine you're doing a transaction in the middle of the night.

1:9:27

our credit card like,

1:9:29

you take the credit card out and you take it somewhere

1:9:32

and you swipe it for five lakh rupees

1:9:34

and a five lakh rupees

1:9:36

in 12 midnight in some store or something.

1:9:38

So immediately the bank will call you.

1:9:41

The bank will identify that it is probably a fraud transaction.

1:9:44

The bank will do a preventive call to you

1:9:47

and your transaction will be blocked.

1:9:49

They will authenticate the transaction.

1:9:51

So this is a very real world way how fraud detection happens today.

1:9:54

Maybe it was not a real fraud.

1:9:56

Maybe it was not a real fraud.

1:9:57

just genuinely you are trying to do a transaction or anything, right,

1:10:00

middle of the night, you can go to a hospital also tomorrow.

1:10:03

Hospital go there, a big bill or emergency,

1:10:05

or if you have,

1:10:06

you clear to pay credit card,

1:10:08

then the card accepted.

1:10:09

Because the bank what are?

1:10:10

Bank is, bank,

1:10:11

you're saying,

1:10:12

you've never,

1:10:13

you've never,

1:10:14

three-lark swipe

1:10:15

so that is a very clear fraud for the bank.

1:10:17

Bank is a very clear fraud for the bank.

1:10:18

Bank is thinking that a fraud

1:10:19

bank is thinking that

1:10:20

the night at two-bages

1:10:21

who will take your credit card

1:10:22

and three-lark

1:10:23

swive.

1:10:24

Last four-year

1:10:25

your credit card used

1:10:26

not.

1:10:27

So it might be a very genuine use case.

1:10:30

You have genuinely

1:10:31

it is a use case.

1:10:34

This is actually what's going on today.

1:10:36

Banks are doing this in a big way.

1:10:38

Not just banks,

1:10:39

but the card operators, I would say.

1:10:41

The intermediaries, we're talking about Visa,

1:10:42

MasterCard, American Express.

1:10:44

The intermediaries are doing this in a big way,

1:10:46

I would say.

1:10:48

So, first of all, the framing of the problem is very important.

1:10:53

So,

1:10:54

when we are problem framing

1:10:56

we're framing of the problem

1:10:58

was what we talked about in our

1:11:00

very first machine learning session.

1:11:02

So problem framing how will, guys?

1:11:04

Problem to frame how can.

1:11:06

So, the first, data what will?

1:11:08

Here our data what will.

1:11:10

This is my input X, okay?

1:11:13

This is my input X, right?

1:11:15

This is your input X.

1:11:17

And

1:11:18

this your output Y is

1:11:21

output Y is.

1:11:23

Output Y will be fraud.

1:11:26

Yes or no.

1:11:27

This you have to predict

1:11:28

very real world use case.

1:11:30

This is actually what a lot of things happen today.

1:11:32

Now, see, whenever we train a machine learning model, what do we do?

1:11:36

We always go and train the model on some training data.

1:11:39

We always go and train the model on the trained data.

1:11:44

And based on whatever patterns we learn on training, we go and evaluate the model on the unseen test data.

1:11:50

That's the way how we go about it.

1:11:52

So we always go and learn the patterns.

1:11:55

Learn the patterns on the training.

1:11:56

You have your transaction data.

1:11:58

Here are your date here.

1:11:59

You're the merchant.

1:12:04

You're the merchant.

1:12:05

You have the amount.

1:12:07

All these different different things you have got.

1:12:09

Amount.

1:12:11

Okay?

1:12:12

How kind of the price of swiped?

1:12:14

What's the merchant in swiped?

1:12:15

Which day you swiped?

1:12:17

Actually, here point of sale

1:12:19

reference be there.

1:12:20

Sometimes you're the exact POS machine

1:12:22

you used,

1:12:23

the merchant machine used

1:12:24

the machine used,

1:12:25

right?

1:12:26

What is the category of the outlet?

1:12:28

If banks, see, they provide

1:12:29

where you swipe

1:12:30

somebody is giving that,

1:12:32

some payment providers are giving that.

1:12:33

So it's also important

1:12:35

it.

1:12:36

It's got GPS, you know?

1:12:37

That's why we sometimes say,

1:12:39

that's why we sometimes say,

1:12:41

that, that's not that network not are,

1:12:42

because it's connected

1:12:43

that.

1:12:44

That's not a Mazaak device

1:12:45

there.

1:12:46

There's a lot of parameters, by the way.

1:12:47

So banks can track it.

1:12:48

If you ever swipe a card and do some fraud,

1:12:50

like everybody will know,

1:12:52

that where from swiped were,

1:12:53

that card

1:12:54

where from swiped.

1:12:55

when police investigations are

1:12:57

right, so they will know that

1:12:59

where that card was swiped,

1:13:00

you can't spoof those things,

1:13:03

those networks, okay?

1:13:05

Anyways, so you're your POS location

1:13:07

we call it a point of sale machine,

1:13:09

that's a feature here.

1:13:11

Okay, time of the transaction

1:13:13

be a feature of the transaction.

1:13:15

So this will be different different features we have right now

1:13:18

and we are capturing different

1:13:20

different transactions historically.

1:13:21

This is your machine learning here, right,

1:13:23

historical data we have got lots and lots and lots of

1:13:25

of historical data, input, output combination.

1:13:27

So we are saying, hey, you know, transactions like this are fraud.

1:13:30

Yeah, fraud yes or a fraud no.

1:13:34

These are fraud yes, and these are fraud no.

1:13:40

So we have lots and lots of input output or X, Y combinations right now.

1:13:45

Patterns like this are fraud yes, patterns like this are fraud no.

1:13:48

Patterns like this are fraud yes, patterns like this are fraud, no.

1:13:51

And based on that, we are trying to build a model.

1:13:53

So the machine is trying to learn the,

1:13:55

the relationship from our data.

1:13:57

So we are trying to learn the patterns basically.

1:13:59

So patterns like this, transaction patterns like this are corresponding to fraud yes.

1:14:03

And transaction patterns like this are corresponding to fraud no.

1:14:07

And what you'll be.

1:14:08

You will say, sir, how do you know,

1:14:10

you know, you?

1:14:11

This is the idea of machine learning, right?

1:14:14

Machine learning is

1:14:16

you are already using data that is known to you.

1:14:19

And you are trying to learn a pattern

1:14:21

to predict on some future data.

1:14:23

So this

1:14:24

they're going to 5 years ago transaction's.

1:14:27

We have that data is.

1:14:29

Now, mano, if someone's transaction was.

1:14:31

Now, if someone had phone and bank to

1:14:33

say, he's fraud,

1:14:34

my card in some fraud got.

1:14:36

So bank will record can.

1:14:37

This data is a retrospective data,

1:14:40

archived data.

1:14:41

Bank's historical data records may be

1:14:43

that,

1:14:44

so transactions were, actually, bank not,

1:14:46

card operators I'm talking about.

1:14:48

So,

1:14:49

a transaction was fraud not,

1:14:51

that transaction was fraud,

1:14:52

that's a transaction fraud is.

1:14:53

That transaction fraud.

1:14:54

as a transaction fraud.

1:14:55

You're looking at lots and lots of X, Y combination.

1:14:58

Back to what we discussed about in machine learning before.

1:15:00

Okay?

1:15:01

So,

1:15:03

big picture idea is what are we trying to predict?

1:15:05

What are we trying to predict?

1:15:06

We are trying to predict whether the transaction is a fraud or not a fraud.

1:15:10

Fraud yes or fraud.

1:15:11

No, we are predicting.

1:15:12

That is what we are trying to do.

1:15:14

Okay.

1:15:15

Now,

1:15:16

coming back to the content of our topic here,

1:15:19

class imbalance,

1:15:20

this is our use case.

1:15:22

Now, discussion point is.

1:15:23

First, problem framing, we've seen.

1:15:26

This is it?

1:15:27

What type of problem is it?

1:15:29

Regression or classification?

1:15:31

Guys, question for everybody.

1:15:33

First, this is it a regression problem?

1:15:35

Is it a classification problem?

1:15:37

Come on, guys.

1:15:39

Is it regression? Is it classification?

1:15:41

Is it classification?

1:15:53

Thank you.

1:15:55

And

1:15:57

you.

1:15:58

Thank you.

1:16:28

Thank you.

1:16:58

Thank you.

1:17:02

Thank you.

1:17:28

Classification, absolutely correct, absolutely correct.

1:17:35

Absolutely correct.

1:17:36

Absolutely correct.

1:17:38

Very good.

1:17:40

Very good.

1:17:41

So, well, very good.

1:17:43

You know,

1:17:44

you also, sir, what you asked

1:17:45

asked you, sir, what question you have?

1:17:46

No, it's okay.

1:17:47

I just wanted to get all of you to be a little active.

1:17:50

Very, very good, very good.

1:17:52

Good to hear some voices, all of you.

1:17:54

Very good.

1:17:56

So, classification, obvious is right?

1:17:57

Because we are trying to.

1:17:58

to predict a class.

1:17:59

Distinct class, exactly.

1:18:00

As you rightly said, as you rightly said,

1:18:01

Nickup, we are trying to predict a distinct class.

1:18:04

Regression is what you're going to

1:18:06

where you're trying to do a

1:18:09

some kind of a rainfall prediction, weather prediction,

1:18:12

stock market prediction,

1:18:13

you have a regression.

1:18:15

Right?

1:18:16

classification is that you are trying to predict is it yes or no.

1:18:19

Yes no prediction.

1:18:20

That is classification, okay?

1:18:22

That's what we are able to see.

1:18:24

Now, what is class imbalance?

1:18:26

Now, we have a classification problem,

1:18:28

so imbalance of what is?

1:18:30

So, the imbalance is you,

1:18:31

answer you are in front of you.

1:18:33

As I told you, my notebooks are very self-expertory.

1:18:35

You're here here,

1:18:36

you'll here, so you'll see you'll see

1:18:38

very self-explanatory.

1:18:39

It didn't come out, right?

1:18:41

I mean, if you look at real data,

1:18:44

if you,

1:18:46

if you,

1:18:47

if you,

1:18:48

if you look at the real data

1:18:50

if you look at the real data,

1:18:53

if you look at the real data,

1:18:55

if you look at the overall data,

1:18:56

data right now, 90% of the transactions are normal.

1:19:04

99% of the transactions are normal,

1:19:07

it's class 0, 99% of the transactions are normal,

1:19:13

class zero is,

1:19:16

and 1% of the transactions are fraud.

1:19:20

If you're historical data that

1:19:22

if you will, if you if you look at the historical data

1:19:24

Thinker.

1:19:25

If you look at the historical data, if you look at the historical

1:19:26

data right now in this context, most transactions will not be fraud.

1:19:33

It's not that every day fraud are, right?

1:19:35

Fraud is very rare.

1:19:36

If you're 100 transactions from there, one fraud next to be less than

1:19:39

this is what is referred to as class imbalance.

1:19:44

Class imbalance means that out of 100 transactions, if you see,

1:19:47

a very small portion of transactions will be fraud.

1:19:49

Backey, all are not fraud over.

1:19:51

Out of 100 transactions, if you look at a very small minority will be fraud.

1:19:56

That is what is referred to as class imbalance.

1:19:58

That is what is referred to as class imbalance.

1:20:00

So, 99% are normal transactions.

1:20:03

Only one person fraud will.

1:20:05

Now, the part is it, this is the problem is.

1:20:08

Now, you'll think,

1:20:09

okay, sir, okay,

1:20:11

the imbalance is, so, so what is, problem is?

1:20:14

I mean, if your data is,

1:20:17

you mean, you here,

1:20:19

you mean, here here, all noes are,

1:20:21

okay, you're saying, okay,

1:20:23

this transaction fraud,

1:20:24

hey, this transaction fraud,

1:20:25

not it, this transaction fraud,

1:20:27

not only one fraud.

1:20:30

What is the problem?

1:20:31

Question for you again.

1:20:32

Question for you.

1:20:33

Who will tell me?

1:20:34

Now, we, we can't

1:20:35

understand what is the class imbalance

1:20:36

is?

1:20:37

Inbalance,

1:20:37

there are very few of one class.

1:20:42

So, what is the problem

1:20:43

in the context of machine learning?

1:20:45

Machine learning in the issue

1:20:45

is.

1:20:47

Question for everybody.

1:20:49

Problem why are, guys?

1:20:50

Anybody?

1:20:51

Anybody wants to tell me?

1:20:55

Take your time, 30 seconds.

1:21:25

Anybody? Okay, no answers?

1:21:40

Yeah, I may not have explicitly talked about it.

1:21:42

I have not discussed in detail.

1:21:44

I'm just checking to see people's an answer.

1:21:46

This you've done in class in detail in any discussed because this is again,

1:21:48

what is the thing?

1:21:51

Okay, Prasat has answered.

1:21:53

People, please answer to everyone.

1:21:54

Everyone.

1:21:55

Okay, so everyone can see your answers that way.

1:22:01

What is the issue?

1:22:02

If my data has class imbalance, what is the issue?

1:22:06

That is the question.

1:22:08

That is the question I'm asking.

1:22:10

If data in class imbalance, then what issue?

1:22:15

Yes, and and, and, and I think Aweiss has also answered it briefly.

1:22:21

And Prasad has also answered it briefly.

1:22:23

Prasad is saying that machine learning model,

1:22:25

will start to focus on the majority class.

1:22:29

Jo Jada are there, the model will tend to focus more on that.

1:22:34

And it's correct. You're absolutely right. You're absolutely right.

1:22:38

And if you, and if you, if you, if you, if you look at it, I think, I think you will remember the concept of,

1:22:51

when we talked about machine learning, how many an analogy diogen.

1:22:55

like a small kid in a kindergarten.

1:22:59

Just a teacher and your teacher is teaching the kid.

1:23:01

If you remember the machine learning first class that we did, no, I showed you lots and lots

1:23:04

of examples of objects.

1:23:06

I showed you examples of mobile, example of that water bottle, something like.

1:23:11

So imagine you're teaching a small kid.

1:23:15

And you're showing it lots of examples of the phone.

1:23:17

You're showing it lots of examples of the phone.

1:23:21

Ki phone is aza ha, you're showing the phone in different different ways, right?

1:23:25

But you're showing the phone.

1:23:25

only showing one example of the mouse.

1:23:28

But one-y-a-one, you're rotating in different, different ways,

1:23:33

and you're showing tens of thousands of examples.

1:23:37

So the kid will learn the phone very well.

1:23:39

That phone's patterns very much as well.

1:23:42

But you, the mouse is, it will not understand the mouse that well.

1:23:45

Because mouse, you know, you're not an example, you know.

1:23:49

So, machines learned the way kids learned.

1:23:53

Machines learned the way humans learn.

1:23:55

If we're, if we're going to,

1:23:59

if we're just about 10 times,

1:24:01

there is something I'm teaching you 10 times and there is something I'm teaching you once,

1:24:05

which one will you learn better?

1:24:06

Obviously, the one I'm teaching you 10 times, right?

1:24:08

It's obvious right.

1:24:10

That's the reason.

1:24:11

So the model will be more focused on the majority class.

1:24:15

But if you're trying to build a machine learning model based on this data, right?

1:24:20

What will happen?

1:24:22

There are more examples of no frauds.

1:24:25

So, the model will try to learn,

1:24:28

the model will try to predict towards no fraud.

1:24:31

The model will try to majorly predict no frauds.

1:24:33

That will know fraud predict kind of no frauds.

1:24:36

It will try to predict more of no frauds.

1:24:38

That is what will happen behind the scenes right now.

1:24:41

It will, it will bias towards the majority class.

1:24:43

That is the problem.

1:24:44

That is the issue that we'll be facing.

1:24:47

Because we are showing it five examples of no frauds.

1:24:49

Only one example of fraud.

1:24:51

So fraud what is.

1:24:53

Machine will not understand.

1:24:55

The machine has seen a lot of examples of not frauds.

1:24:57

That's almost.

1:24:58

That pattern,

1:24:59

you know, but fraud can't

1:25:01

do you see any of

1:25:01

that's the issue.

1:25:04

So,

1:25:04

that is number one.

1:25:06

It will become biased in its prediction

1:25:08

and it will bias more towards the majority class.

1:25:10

Majority class,

1:25:11

the one that is occurring more number of times.

1:25:14

If you take the same story forward here,

1:25:16

here we have called on cold by this.

1:25:18

So we have here here by two columns

1:25:19

via transaction amount and is fraud.

1:25:21

Same story.

1:25:22

I'm just creating a random data set in Pandas, right?

1:25:24

just to demonstrate that for you.

1:25:25

This input, this input, you can put the same story here.

1:25:31

Yeah, output column here.

1:25:32

And you can clearly see there are 990 examples of no frauds.

1:25:35

And there is only 10 examples of frauds.

1:25:38

There are 990 examples of no frauds and there is only 10 examples of frauds.

1:25:42

That's what you're able to see on the screen.

1:25:44

There are 990 examples where frauds did not happen.

1:25:47

And there are only 10 examples where frauds happened.

1:25:52

That's the inference we are able to see right now.

1:25:54

There are 10 examples of frauds.

1:25:56

So, this is the imbalanced data that you're able to see right now.

1:26:00

Class imbalanced.

1:26:03

Okay?

1:26:05

Now, how do we deal with it?

1:26:06

We'll see that.

1:26:07

You have a issue.

1:26:09

Let me go and come back to the code again.

1:26:24

So what I'm trying to say is, this is, you have our data

1:26:47

now let's let's get our focus back to the data.

1:26:50

Whatever data is given to us right now.

1:26:53

This is your transaction amount.

1:26:54

This is your transaction amount, right?

1:27:06

You have a transaction amount.

1:27:07

And based on that, you are trying to predict fraud.

1:27:12

E's fraud.

1:27:16

Yeah, you're able to see that.

1:27:21

So we can clearly see this is your X and this is your Y.

1:27:23

You have your input out.

1:27:24

put X, Y combinations.

1:27:26

So we can say that, hey, you know, patterns, when the amount is this, it is not a fraud.

1:27:31

Zero.

1:27:32

Amount is this, not a fraud.

1:27:34

Amount is this not a fraud. Amount is this not a fraud.

1:27:36

It's all zero's.

1:27:37

Only one, one.

1:27:39

So what is the problem you will face?

1:27:42

This problem what, what, problem?

1:27:43

It's the problem here will be, the problem here will be that the model, the model will make more of

1:27:49

zero predictions.

1:27:51

When you eventually build a model on this data, it will become biased.

1:27:54

towards zeros.

1:27:55

The model will only start predicting zeros.

1:28:00

Let me write it down.

1:28:02

So, if you go and build a model on this data,

1:28:07

model will only predict zeros.

1:28:14

And the interesting part is, if we're here here

1:28:16

a column behind here we're not split,

1:28:19

train test split ideally for, we need to do this.

1:28:22

Right now I'm discussing class imbalance.

1:28:24

see, but ideally, as we discuss,

1:28:26

we have, we first data, take,

1:28:27

train, test, put, and we're back.

1:28:29

So, we're all the data we're doing.

1:28:31

But the concept remains the same, even if I do train test,

1:28:33

nothing changes, okay?

1:28:35

So,

1:28:36

this is your actual Y, okay?

1:28:37

I will call it Y actual.

1:28:39

And this your predicted Y, I'll call it Y predicted.

1:28:42

I'll call it Y predicted. Whatever the model predicted,

1:28:43

the model will always predict zeros.

1:28:46

This is what I meant to say.

1:28:48

So, this is your dummy model.

1:28:51

This model, too, this model, do we're not?

1:28:52

This model is this model?

1:28:54

See, it is like saying,

1:28:56

you have a doctor to biddered.

1:28:58

He, the doctor to do not know.

1:29:00

Digri, biggri,

1:29:00

nothing made.

1:29:02

Patient, a doctor,

1:29:03

the doctor,

1:29:03

he said, you don't have,

1:29:04

don't have disease.

1:29:06

Patient had a doctor

1:29:07

to call, doctor,

1:29:07

they don't have disease.

1:29:09

For every patient, the doctor is saying,

1:29:10

you don't have disease, don't have disease.

1:29:13

So what we are seeing on the screen right now

1:29:14

is what is called a dummy classifier.

1:29:19

We call it a dummy classifier.

1:29:22

A dummy model.

1:29:24

A dummy classification model.

1:29:28

It's as good as a useless model.

1:29:30

He's not doing.

1:29:32

All is predicting zeros only.

1:29:34

And this dummy model is useless model.

1:29:37

But still, you will realize, very interesting.

1:29:39

It is giving you accuracy of how much?

1:29:42

Four out of five entries are correct?

1:29:44

80%.

1:29:45

That's the best part.

1:29:47

This is your accuracy paradox.

1:29:50

And this is the issue of class imbalance.

1:29:51

Whenever your data is imbalance,

1:29:53

whenever your data is in a,

1:29:54

inherently imbalanced.

1:29:55

This is the kind of problem that you will face.

1:29:58

The models that you end up building will be biased.

1:30:02

They will eventually become dummy models.

1:30:04

And they will only try to predict a certain class well.

1:30:08

And what will happen is,

1:30:10

if you ultimately accuracy measure

1:30:12

can't, accuracy will still come out to be high.

1:30:15

Because you have this actual data.

1:30:16

Why actual?

1:30:17

This is originally you have you.

1:30:19

And this model has predicted.

1:30:22

But if you're a model may predict here.

1:30:23

But if you compare can,

1:30:24

actual and predicted, that is what we do, right?

1:30:25

How do we calculate accuracy?

1:30:28

Accuracy is nothing but an actual to predicted comparison.

1:30:31

If by actual y'i here, or model in predict here, that's it.

1:30:37

And you can clearly see out of total five entries of data, four out of five are correct.

1:30:41

So accuracy 80%.

1:30:42

And this is what is called, this is what is called the accuracy paradox.

1:30:47

If I scroll down, this is what is exactly what we refer to accuracy paradox.

1:30:52

That's, that's, that's, that's, that's not.

1:30:54

99% accuracy, but it got zero frauds.

1:30:57

Okay, fraud detected you incurpar.

1:30:59

Every transaction it is saying no fraud, no fraud, no fraud, no fraud.

1:31:03

Not a single fraud it predicted, but still it got 99% accuracy.

1:31:08

And that's what we call the paradox.

1:31:11

Now, how do we solve the problem?

1:31:14

So, to solve the problem, we go back and we use something.

1:31:22

something called Confucian matrix.

1:31:24

Confucian matrix is actually not part of today's session.

1:31:27

So we have just, we'll actually see Confucian matrix in more detail in the next session.

1:31:33

But today, we want to give you a basic idea of the approach.

1:31:37

That we're how to solve it?

1:31:39

If I just take you to my notes once again,

1:31:43

this is class imbalance, right?

1:31:44

Everybody's clear.

1:31:46

We talked about class imbalance.

1:31:48

And we talked about the accuracy paradox.

1:31:49

Why accuracy is misleading?

1:31:52

If we have imbalanced data, this is why accuracy is misleading.

1:31:57

And we talked about that.

1:31:59

99% accuracy, this is the problem.

1:32:02

So accuracy is not the best metric to use.

1:32:06

So, whenever our data is imbalanced, we should not use accuracy.

1:32:11

We'll use more use and that is actually called a recall.

1:32:14

So recall, I will introduce you today.

1:32:16

We'll introduce what is precision recall intuitively.

1:32:18

But this more detail we'll next week will.

1:32:22

classification. I have actually given you some snippets on Confucian matrix and all,

1:32:26

but that is not part of today. Today, we will just give you the intuition of what is recall.

1:32:31

And then we will go ahead. Okay. So just for the time being, keep in mind, keep in mind that

1:32:37

accuracy will not work. So accuracy is not, not, will not work in the case of imbalance data.

1:32:49

Okay. Accuracy will not work in the case of imbalance data.

1:32:55

That's the idea thing. Okay. Now, moving on.

1:32:57

So if you take a look at the accuracy paradox once again, we are getting 99% accuracy.

1:33:14

So we are getting 99% accuracy here. And 99% accuracy basically means that

1:33:19

The model is, it's actually a dummy classifier. It's a dummy model, but it is, it is only 99% accurate.

1:33:29

It is a dummy model, but it is only 99% accurate. That is what we are able to see.

1:33:33

So, we don't use accuracy in practice. So in practice, some accuracy use name can't.

1:33:40

What we do is we use something called precision and recall.

1:33:45

Instead, what do we use? Instead, we use something called precision and we use something called recall.

1:33:49

Now, let's see, what is the meaning of precision? What is the meaning of recall?

1:33:53

Intuitively, right? Intuitively. I'll discuss part of it today. What is, what is this precision recall? And most importantly, what is this false negative?

1:34:02

And what is this false positive? We'll intuitively try to understand these, these terms right now.

1:34:10

What is precision recall? And intuitively, what is false negative and what is false positive? Let us see that.

1:34:19

So, what I will do, I will take you back to my notes right now for a minute.

1:34:29

And everybody can go ahead and take a look at this particular portion.

1:34:38

Just a second, guys.

1:34:49

Thank you.

1:35:19

I will just give it a glance right now. Just all of you give it a glance right now. Then I'll explain to all of you. What is it? So everybody just give it a glance here. All of you. So everybody just give it a glance here. All of you. So I will just briefly cover the confusion matrix here for all of you. What is it? There's a lot of things here. So everybody just give it a glance. Take your time. And this will be the majority of the thing that we'll do in the class today. Okay. So this is this is what we have. We will see in detail.

1:35:47

And using this technique, we can solve that problem just now.

1:35:52

we just discussed.

1:35:53

So we have the first problem discussed.

1:35:54

Problems what is?

1:35:56

If you have an imbalance class, if you have imbalance class, if you have imbalance class, like frauds, like health,

1:36:03

every real world data will always be imbalanced.

1:36:07

If you talk about credit card fraud detection, health, disease detection,

1:36:12

you know, disease detection, you know, diabetes one of the data set I'm not you share

1:36:14

here, right? Out of every hundred patients, only if you will be diabetic, most will not

1:36:21

be diabetic. That is the real world scenario, right? Only if you will be diabetic. Imbalanced.

1:36:27

Inbalance will be everywhere, always. Right? And accuracy will not be the good metric in that case.

1:36:35

Because if the model predicts all of a particular class, it will still show high accuracy. So what is

1:36:40

the solution? The solution is here. Okay? So everybody give it a glance, all of you. Then I will

1:36:44

discuss. We can take a break, huh? We can take a short break also and come back.

1:36:51

So in the meantime, let us take a break, right? Good time to take a break and we can take a quick

1:36:57

break and come back and we'll resume on with Confucian matrix after the break.

1:37:14

Thank you.

1:37:44

Thank you.

1:38:14

Thank you.

1:38:44

Thank you.

1:39:14

Thank you.

1:39:44

Thank you.

1:40:14

Thank you.

1:40:44

Thank you.

1:41:14

Thank you.

1:41:44

Thank you.

1:42:14

Thank you

1:42:44

Thank you

1:43:14

Thank you

1:43:44

Thank you

1:44:14

Thank you

1:44:44

Thank you

1:45:14

Thank you

1:45:44

Thank you

1:51:44

Okay,

1:51:48

Hey,

1:51:52

Hey,

1:51:56

Okay,

1:52:00

guys, welcome back.

1:52:01

We'll just start on.

1:52:31

Thank you

1:53:01

Thank you

1:53:31

So, all of you, please, please, please, please,

1:53:43

please continue on with the

1:53:45

with the

1:53:46

Confuci on with the Confucian matrix, everybody.

1:54:01

I hope everyone's gone through it already.

1:54:10

I'm just going to give it a few more minutes.

1:54:12

And just to clarify, what is, what is this D, uh, D, D and D&, basically stands for diabetes, not

1:54:19

not diabetes, just to clarify, okay?

1:54:21

Diabetes, not diabetes.

1:54:22

So that is the context we are discussing guys, okay?

1:54:25

Let's let's let's see.

1:54:31

So we are trying to build a model to predict whether the person is diabetic or not diabetic.

1:54:57

So Diabetic stands for D and not Diabetic stands for NG

1:55:01

So that is the problem that we are trying to solve.

1:55:03

Okay?

1:55:04

So diabetes stands for D.

1:55:06

And not diabetes stands for ND.

1:55:09

These are two classes that we have right now.

1:55:11

Like we have a fraud

1:55:12

did some time back.

1:55:13

Right now we are doing diabetes, not diabetes.

1:55:15

And one more

1:55:18

nomenclature that we are using right now is

1:55:20

negative or positive class.

1:55:22

So negative class is basically

1:55:25

positive class is the one that you are trying to predict.

1:55:28

So we are trying to predict diabetes right.

1:55:30

So diabetes is the positive class.

1:55:31

So whatever you are trying to predict, that is typically the positive class and not diabetes is a negative plus.

1:55:39

So these are the two classes that we have right now.

1:55:42

Okay? Diabetes is the positive class and not diabetes is a negative plus.

1:55:46

Now, let's say, let's go back to that Pima diabetes exercise that we did already.

1:55:53

And based on the different features of a person based on the pregnancy, blood pressure, glucose,

1:56:00

body mass index and these, these parameters.

1:56:03

We are trying to predict whether a person is diabetic

1:56:07

or whether a person is not diabetic.

1:56:10

So let's say we are trying to predict diabetes equal to yes

1:56:13

or diabetes equal to no.

1:56:16

That is what we are trying to do.

1:56:18

We are trying to predict diabetes equal to yes or

1:56:20

diabetes equal to no.

1:56:22

That's the problem that we are trying to solve.

1:56:24

Okay, class we are trying to predict.

1:56:26

Diabetes class.

1:56:27

Either yes or no will.

1:56:29

Okay.

1:56:30

you're trying to do overall, right?

1:56:32

Based on the features we are trying to predict the glass.

1:56:36

Okay.

1:56:37

Now, we have taken the data, we have built a model, model we have made the model.

1:56:44

Now we are trying to evaluate the model.

1:56:47

What we are seeing on the screen, this particular confusion matrix that we are seeing on the screen,

1:56:53

this is relevant for model evaluation.

1:56:56

Like we last last case study, I'm a little bit earlier,

1:56:59

we have got actual, we have predicted,

1:57:01

we have got actual frauds,

1:57:03

predicted fraud not fraud,

1:57:05

and we are comparing the two.

1:57:07

And we saw 80% accuracy.

1:57:09

The same thing we are trying to do here.

1:57:11

We have data.

1:57:12

We have used the model

1:57:14

we have used the data, we have built a model.

1:57:17

And now we are trying to

1:57:19

use that model

1:57:22

to do predictions

1:57:25

on the test data.

1:57:27

And we are coming to

1:57:28

And we are comparing the predicted values with the actual values.

1:57:31

We are trying to compare the predicted values with the actual values.

1:57:34

What the model predicted, what are the model actuals.

1:57:37

That is what we are trying to do.

1:57:39

What is what the model predicted versus what is the model actuals?

1:57:43

That's what we are trying to do right now.

1:57:45

And you can see

1:57:47

the predicted will always come along the columns

1:57:52

and the actuals will always come along the rows.

1:57:55

That is what is happening right now.

1:57:56

So you can see the predicted is coming along the columns.

1:57:57

is coming along the columns. So predicted 01 and actual 01. This is what we call the

1:58:06

Confucian matrix. This is what we call the Confucian matrix. It's a slightly different term

1:58:12

and a new name that we are using right now. So we have used some algorithm, we have built a

1:58:18

model, we have model, right? We have, we have some data, we have used some algorithm, we have built a model

1:58:22

on the train data. Whatever we did is on the train data, how many train data my model

1:58:29

made, right? And now whatever model we have built on the train data, we want to use that model

1:58:39

and do predictions on the test data. We want to use that same model and do predictions on the

1:58:46

test data. Test data we want to do predictions.

1:58:52

So you'll have two things. One is you will have the actual values.

1:58:56

And we'll see why is we're based. Actual why is what

1:58:58

is what is.

1:58:59

What are. So that is what you're comparing. That is the context of what it is right now.

1:59:05

Just to clarify. So so far you are probably seeing a lot of numbers. I hope this gives you the right context.

1:59:11

Now you're able to see. There are like, so we are talking about model comparison right now.

1:59:18

I'm model compare car.

1:59:22

the predicted value versus what is the actual value? So then there are 35 such cases where

1:59:26

model predicted one actually also one. That's called a true positive.

1:59:33

The next time anybody asks you what is the meaning of a true positive?

1:59:37

True positive means model predicted positive. That's the way to remember it, right? You will say

1:59:42

model predicted positive and the prediction is true. So there are 35 such cases. If you're

1:59:51

if you see this matrix, there are 35 such cases where the model predicted one,

1:59:57

diabetes and actually also one diabetes.

2:0:01

True positive. So train data we have

2:0:04

we made data and made a data and classification model

2:0:07

been made. And now we want to use that model. So whatever model we have built on the

2:0:12

trained data, whatever patterns we learned, right?

2:0:16

Model training what is? Model training, what is? Model training,

2:0:18

we are learning the patterns right on the train data.

2:0:21

So whatever patterns we learned on train, now we want to use those patterns on the test.

2:0:27

We want to use those patterns on the test.

2:0:30

We want to know how, how it is performing on the test data.

2:0:33

Test data in how to perform correct, right?

2:0:35

That is what we want to go back and do.

2:0:39

How is it performing on the test data?

2:0:44

And that is exactly where the evaluation part comes in.

2:0:47

Evaluation.

2:0:47

What is what we do that is what we discussed in the first session.

2:0:51

Textbook, you learn the patterns and you're evaluating that on the mock question paper.

2:0:56

So, you have 35 cases

2:0:58

where the model predicted, based on whatever patterns it learned,

2:1:03

they predicted, that, yeah, diabetes is.

2:1:06

But actually also diabetes is true positive, correct prediction.

2:1:11

Similarly, there is something called true negative.

2:1:12

What is true negative?

2:1:14

True negative, there are 88 such true negatives.

2:1:17

True negative is what is?

2:1:20

There are 88 such true negatives.

2:1:21

where model predicted negative class and the prediction is true.

2:1:26

There are 88 such cases where model predicted negative class and prediction is true.

2:1:31

So 88 true negatives.

2:1:32

So these are the total number of correct predictions.

2:1:34

What you are seeing on the screen?

2:1:36

So what you are seeing on the screen is the total number of correct predictions.

2:1:39

88 true negative are 35 true positives say?

2:1:43

These many correct predictions you have right now.

2:1:46

88 true negatives and 35 true positives.

2:1:51

And whatever else you see right now are the incorrect predictions.

2:1:58

And what are they called false negative or false positive?

2:2:02

That is what I will spend a big part of my time today.

2:2:04

Okay?

2:2:05

Actually, this confusion matrix is not part of today.

2:2:07

I know there have been some stray one or two questions you might see.

2:2:11

But because these topics are so related, no, guys,

2:2:13

that kind of a topic will be.

2:2:15

Kut, you know, so we are going in a flow, right?

2:2:19

Machine learning is a gigantic topic.

2:2:21

So sometimes like, like,

2:2:22

today's session in Confucian matrix actually not.

2:2:26

But the point is, if you, if you see the actual content,

2:2:31

if I don't talk about Confucian matrix,

2:2:33

I can't talk about false positive.

2:2:35

This has no meaning, right?

2:2:37

So I'm introducing Confucian matrix.

2:2:39

But I'm also warning you, I'm also telling you,

2:2:42

that the Confucian matrix is you back in back in.

2:2:45

When we actually come to classification, I think, next to next week.

2:2:49

Or then next week's classification should be.

2:2:51

Next to next week we'll classification caring.

2:2:54

That is when we will see this in more detail.

2:2:56

Or detail in more detail, we'll go.

2:2:58

But without talking about Confucian matrix, like, we cannot do false positive.

2:3:02

So that's why I'm just telling you,

2:3:04

that it's how is it even coming?

2:3:08

Just to, just so that you are absolutely clear.

2:3:11

Now, what is false positive?

2:3:13

False positive is.

2:3:14

False positive means model model predicted positive.

2:3:19

and the prediction is false.

2:3:22

That is the meaning of false positive.

2:3:26

I mean, the first, positive negative

2:3:27

what is?

2:3:28

positive class,

2:3:28

I mean diabetes predict here.

2:3:31

Model predicted positive class.

2:3:33

Positive class,

2:3:33

like, disease positive.

2:3:36

What? You have the disease.

2:3:39

So model predicted positive.

2:3:42

So model predicted one.

2:3:45

But actually, it is zero.

2:3:47

So there are 11 such false positives.

2:3:49

False positive also stands for false alarm, no?

2:3:52

It's like a false alarm.

2:3:54

There are 11 cases where the model predicted that the person has a disease.

2:4:00

They've a false alarm raised.

2:4:01

But it turns out actually the person does not have a disease.

2:4:04

Model has one predicted, but actually, it's a zero.

2:4:07

It's a false alarm.

2:4:09

You've got a patient to come up a false alarm create,

2:4:12

that, yeah, you might have a disease, but then actually you don't have a disease.

2:4:17

And you know what sometimes sometimes.

2:4:19

and you'll be surprised to know in the medical industry,

2:4:25

a false positive is acceptable.

2:4:27

False positive error, right?

2:4:29

Galathe.

2:4:30

I mean, model may predict

2:4:31

that the person does not have a disease.

2:4:34

Sorry, model has predicted that you have a disease.

2:4:38

But actually, you don't.

2:4:39

But if you go a little deeper and try to understand,

2:4:42

all doctors are diagnosing based on that only.

2:4:45

All doctors, so he, as he is diagnosed kind of.

2:4:47

When you go and see a doctor, the doctor, the doctor will,

2:4:49

we'll inherently start with some assumptions.

2:4:53

He will,

2:4:53

that's in terms of the basis

2:4:55

assume that maybe you have your condition

2:4:57

is, this condition, this condition, this condition, yeah.

2:4:59

Allerg, other conditions

2:5:00

your device will give you might have this condition,

2:5:03

this condition, this condition.

2:5:05

And the doctor will give you medicines based on those conditions.

2:5:08

That's the way how it will work out in practice.

2:5:11

Right?

2:5:12

That's the way how it will work out based on that thing.

2:5:14

Doctor will give you medications based on it.

2:5:17

So, doctor will inherently assume,

2:5:19

that you have this disease and

2:5:21

that basis on the basis of treatment

2:5:22

unless otherwise proven incorrect.

2:5:25

That happens actually.

2:5:27

False negative what is?

2:5:28

That's more deadly.

2:5:30

False negative is even more deadly.

2:5:32

False negative means model predicted negative plus

2:5:35

but prediction is false.

2:5:40

Model predicted negative but prediction is false.

2:5:44

So there are 20 such cases where model predicted you don't have a disease.

2:5:49

Excuse me, but actually you have a disease.

2:5:53

So there are 20 such cases where model predicted,

2:5:56

you don't have a disease.

2:5:59

I repeat, there are 20 such cases where model predicted you don't have a disease.

2:6:04

But in reality, you have a disease.

2:6:07

So 20 of those cases, you actually have a disease in 20 of those cases.

2:6:12

You are able to see that.

2:6:13

That is what is referred to as false negative.

2:6:17

That is actually very dangerous.

2:6:19

So doctor has predicted that disease not.

2:6:22

But actually you have a disease.

2:6:23

That is even more dangerous.

2:6:26

From a modeling perspective,

2:6:29

which are those instances where the model was correct?

2:6:33

And this, we're just accuracy,

2:6:35

we're accuracy about accuracy in a bit.

2:6:37

What is that accuracy?

2:6:39

Accuracy is nothing but TN plus TP by total.

2:6:43

Accuracy is nothing but true negative plus true positive divided by total.

2:6:47

That is how we define the accuracy of a system.

2:6:49

that means out of total 154 records

2:6:53

this total 154 rows

2:6:55

out of total 154 rows

2:6:58

out of total 154 rows of data

2:7:01

that is there in the testing

2:7:03

testing in the testing

2:7:04

total 154 rows are right

2:7:06

that is the evaluation data

2:7:08

that's the mock question paper

2:7:09

go back to the first class what we discussed

2:7:12

you're going to train pay model

2:7:13

and mock question paper

2:7:15

model evaluate kare.

2:7:16

So whatever you learned

2:7:18

that learning

2:7:19

is right?

2:7:21

This is your mock question paper

2:7:22

in.

2:7:22

Mock question paper

2:7:22

in 154 questions

2:7:24

have.

2:7:25

So

2:7:25

those learnings

2:7:27

with that 154

2:7:28

questions

2:7:28

solve

2:7:28

and the questions

2:7:30

actual answer

2:7:31

will be

2:7:31

why actual is known

2:7:32

learning

2:7:34

basis on why

2:7:35

predicted

2:7:35

find out

2:7:36

to find out

2:7:36

both.

2:7:37

That is your

2:7:38

Confucian matrix

2:7:38

is.

2:7:39

There's nothing

2:7:40

there's nothing

2:7:40

actually.

2:7:41

Very simple.

2:7:43

So this thing

2:7:44

that you're seeing

2:7:45

is on the test

2:7:46

data,

2:7:47

mock question paper.

2:7:48

Actual

2:7:49

answers

2:7:49

what are?

2:7:50

Answer

2:7:51

what is

2:7:51

and the model

2:7:53

predict

2:7:53

what is a

2:7:55

zero

2:7:55

or one

2:7:56

and

2:7:56

on

2:7:57

the basis

2:7:57

you are

2:7:59

able to

2:7:59

get a more

2:8:00

deeper

2:8:01

picture

2:8:01

into how

2:8:02

the model

2:8:03

is actually

2:8:03

working.

2:8:05

The accuracy

2:8:06

paradox

2:8:06

we were

2:8:06

talking about

2:8:07

sometime back

2:8:07

this

2:8:09

this

2:8:09

shall go

2:8:09

I will

2:8:10

show you

2:8:11

how

2:8:11

although this was

2:8:12

not part

2:8:13

of today's

2:8:14

conversation

2:8:14

but I think

2:8:15

you will

2:8:15

but this is

2:8:17

actually

2:8:17

be very helpful

2:8:18

for you.

2:8:18

If

2:8:18

it's

2:8:19

without

2:8:19

you

2:8:19

you'll be confused.

2:8:20

If I

2:8:20

don't

2:8:20

talk

2:8:21

about it,

2:8:21

it will be

2:8:21

confused

2:8:21

that

2:8:22

how

2:8:22

how

2:8:22

resolved

2:8:22

you

2:8:23

but now

2:8:23

that

2:8:24

you

2:8:24

know

2:8:24

this

2:8:24

I

2:8:24

I will be so simple.

2:8:26

it'll be very, very simple

2:8:30

to understand what is it.

2:8:33

Let me go about it once again.

2:8:36

I will talk about it once again.

2:8:37

I will talk about it once again for all of you.

2:8:39

What is it?

2:8:39

What is going on behind the scenes?

2:8:43

Ah,

2:8:44

very good question.

2:8:45

Aksha has asked a very good question.

2:8:47

Why is it called confusion matrix?

2:8:49

I'm very, very happy that you're very curious,

2:8:50

actually.

2:8:51

Normally,

2:8:51

what is we assume

2:8:52

could, sir,

2:8:53

we'd say say,

2:8:54

I could have also done the same.

2:8:56

I could have said,

2:8:56

guys, it's a term, remember,

2:8:58

yeah,

2:8:58

I will not do that, right?

2:9:01

This is a bookish

2:9:01

thing is,

2:9:02

a term here,

2:9:03

yeah,

2:9:03

but no,

2:9:03

actually there's a reason.

2:9:06

It's a reason.

2:9:06

It's called

2:9:06

because it shows

2:9:08

where the model gets

2:9:09

confused between the classes.

2:9:12

It's sort of deep

2:9:13

I'm just trying to answer the question,

2:9:14

Aksh.

2:9:15

Look, what are we trying to do?

2:9:16

We are trying to classify

2:9:17

between zero and one.

2:9:19

I mean,

2:9:19

here here either

2:9:20

disease or not disease

2:9:21

or not disease.

2:9:21

You have.

2:9:22

You have a patient.

2:9:23

You have a disease

2:9:24

or not.

2:9:24

not disease

2:9:25

I'm

2:9:25

separate

2:9:26

can't

2:9:26

you.

2:9:28

So the

2:9:28

model is getting

2:9:29

confused between

2:9:30

the classes,

2:9:31

actual and

2:9:31

predicted.

2:9:32

That is the

2:9:33

intuition

2:9:33

behind the

2:9:33

term Confucian

2:9:34

matrix.

2:9:35

So the

2:9:36

term

2:9:36

confusion

2:9:36

us use

2:9:37

because the

2:9:38

model is

2:9:38

actually getting

2:9:39

confused.

2:9:40

And that

2:9:40

confusion

2:9:41

to understand

2:9:41

we are

2:9:42

we draw

2:9:42

are.

2:9:43

We're

2:9:44

we're trying to

2:9:45

where is the

2:9:45

model getting

2:9:46

confused.

2:9:47

What are

2:9:47

those cases

2:9:48

where the

2:9:49

model is

2:9:49

predicting

2:9:50

one but

2:9:52

actually it is

2:9:52

zero and where

2:9:53

are the

2:9:53

cases where

2:9:54

it is predicting

2:9:55

zero but

2:9:55

actually it is

2:9:56

one.

2:9:56

Where is the

2:9:56

the model getting

2:9:57

confused?

2:9:57

That's

2:9:57

we're

2:9:58

we're going to

2:9:58

confusion

2:9:58

matrix

2:9:58

can

2:9:58

make.

2:9:59

Remember

2:10:01

this is

2:10:02

actually a

2:10:03

simple comparison

2:10:04

between actual

2:10:06

and predicted

2:10:07

values.

2:10:08

The Confucian matrix

2:10:10

is a

2:10:10

simple

2:10:11

is a simple

2:10:13

comparison

2:10:14

between the

2:10:16

actual values

2:10:17

and the

2:10:19

predicted

2:10:19

values.

2:10:20

That is what

2:10:20

the

2:10:21

confusion

2:10:21

matrix

2:10:21

basically is.

2:10:23

So along the

2:10:24

predicted, you have predicted zero, predicted one.

2:10:27

And along the actual zero, I

2:10:29

again repeat

2:10:29

because it's a sort of a new topic

2:10:30

is so

2:10:31

I know I'm probably boring you guys

2:10:33

when we've been doing this so often now, but

2:10:34

anyways,

2:10:35

it's important actually.

2:10:36

Today's the most

2:10:36

important topic

2:10:37

is there.

2:10:37

And there's

2:10:38

other

2:10:39

other than 10,

2:10:39

2,

2:10:40

5, 10 minute

2:10:41

but this is actually important

2:10:42

so I'm just taking

2:10:43

some effort to go over it once again.

2:10:46

So that you guys

2:10:46

really understand it.

2:10:48

So,

2:10:48

once again,

2:10:50

the train data

2:10:51

we have

2:10:52

algorithm used

2:10:53

we,

2:10:54

we have built the model on the train data.

2:10:57

And whatever

2:10:58

model we built,

2:10:59

model means what is

2:10:59

what is the model is.

2:11:02

And whatever

2:11:03

model you built on the train,

2:11:06

you are now trying to

2:11:07

evaluate that model on the test.

2:11:09

So whatever

2:11:10

model we built on the training data,

2:11:12

now we are trying to evaluate

2:11:13

that model on some test data.

2:11:16

You,

2:11:16

um,

2:11:16

we have a mock question paper,

2:11:17

test data

2:11:17

that we're evaluating

2:11:18

that,

2:11:19

okay?

2:11:19

That's the context.

2:11:20

We are now trying to evaluate that

2:11:22

model on the test data.

2:11:23

and we are getting some predicted values.

2:11:26

So the Confucian matrix is nothing but an actual to predicted comparison.

2:11:30

It is nothing but a simple actual to predicted comparison.

2:11:32

We have actuals along the rows and we are predicted along the columns.

2:11:37

Actual to predicted.

2:11:39

So out of total 154 records in the mock question paper, we can see.

2:11:45

There are 99 actual zeros.

2:11:47

There are 55 actual ones.

2:11:49

This we have got.

2:11:50

This answer key.

2:11:51

Now, you will say, sir, how can't know actual?

2:11:53

Actual, you know, then what mark question paper?

2:11:55

Now, mahog question paper, then it's answer can be.

2:11:57

You, when you solve it, you, you'll, you can't answer's marked, that predicted value

2:12:01

will you go.

2:12:02

You'll, you know, that's going to compare it.

2:12:05

Otherwise, how will you know, that we've been a exam for a good prepared or not?

2:12:08

You have an answer key, actuals?

2:12:12

So there are 99 actual not diabetic cases, and there are 55 actual diabetic cases.

2:12:20

That is what we are able to see.

2:12:23

If you take a look at it, there are 88 cases which are true negative.

2:12:26

True negative, matter of model predicted zero, actual zero.

2:12:28

So there are total 88 true negatives we are getting.

2:12:33

There are 35 true positives we are getting.

2:12:35

The 35 such cases where model predicted one and actually also one.

2:12:40

I repeat, there are 35 cases where model predicted one, actually also one.

2:12:45

And, excuse me.

2:12:48

And the errors, what are the errors the model is making?

2:12:52

The errors are the,

2:12:53

nothing but FN and FP.

2:12:55

The errors are nothing but false negative and false positive.

2:12:58

So false negative, you can see there's 20 false negatives.

2:13:01

So that means there are 20 such cases where model predicted zero, actually it is one.

2:13:05

So there are 20 such cases where model predicted zero actually it is one.

2:13:10

And there are 11 cases where model predicted one, actually it is zero.

2:13:13

These are the mistakes the model is making.

2:13:15

And that's what you're able to see right now.

2:13:17

So Confucian matrix is helping you understand the mistakes the model is making.

2:13:20

Now, the accuracy, we're all the accuracy.

2:13:23

What is the accuracy?

2:13:25

Accuracy, the more detail in next class, we're going.

2:13:28

Because that's when we actually start building models.

2:13:29

Models building, we have not even started so far.

2:13:32

But all the intuitions we have discussed so far.

2:13:34

Accuracy is nothing but TN plus TP by total.

2:13:38

Your total 154 rows are,

2:13:40

that total 154 from the correct predictions are.

2:13:43

That's where your accuracy is.

2:13:44

So accuracy is giving you an overall picture.

2:13:47

Now, now you accuracy go, it is giving you an overall picture into how,

2:13:50

overall the model is doing.

2:13:52

But it is not telling you individually at a class level how the model is doing.

2:13:57

I'm not mistakes not.

2:13:59

Accuracy is giving you an overall idea how the model is doing.

2:14:01

That's the intuition.

2:14:02

Okay?

2:14:03

I hope everybody is, everybody is clear.

2:14:07

Everybody is clear.

2:14:08

Now, to continue the conversation and to basically close the conversation,

2:14:15

again, I'm repeating, we will come back to this once again.

2:14:18

We actually have it in our upcoming.

2:14:20

course actually. So this our topic here already. We'll come back to it. But just,

2:14:24

just I want to complete the flow by discussing precision recall. What is precision, what is

2:14:30

recall? So I hope FPFN idea is clear. I hope everybody is absolutely clear with what is FP

2:14:35

and what is FN. False positive or false negative concept is very, very important. So it all started

2:14:41

with class imbalance. 991. This is the typical example of class imbalance. What I talked about in the

2:14:48

class. Majority class is this, minority class is it.

2:14:51

Like, only one example of fraud will be there, 99 examples of not fraud will be there.

2:14:56

If you if you're, model will be biased.

2:14:59

But the model will only learn the majority class well.

2:15:01

He always not fraud predict, he will always normal predict.

2:15:04

How the model behaves on skewed data.

2:15:07

So this is the problem. If the model sees not fraud thousands of times and fraud only a few

2:15:13

times, the model will always try to predict not fraud.

2:15:18

And if he will come out to be very high.

2:15:22

That is exactly what I discussed.

2:15:23

So accuracy is misleading on an imbalance data.

2:15:26

Accuracy is misleading.

2:15:29

And this is where the concept,

2:15:32

the concept of precision recall and false negative, false positive actually comes in.

2:15:37

Okay?

2:15:37

So just to clarify what is false negative and false positive once again?

2:15:42

False positive matter false alarm.

2:15:44

False positive matter false alarm.

2:15:45

False positive matter false alarm, basically.

2:15:47

It's a false alarm.

2:15:48

Model predicted, doctor predicted, you have a disease, but actually you don't.

2:15:52

So coming back to our use case, if you're here here on whatever lazy estimation that we did, right?

2:16:00

So here also I have the data set.

2:16:04

We have got 990 examples of frauds and we have got 10, sorry, we've got 990 examples of not frauds

2:16:10

and 10 examples of frauds, right?

2:16:14

That's what we have right now.

2:16:15

There are 990 examples of not frauds and there are 10 examples of frauds.

2:16:18

That's what we are able to see.

2:16:21

Next, what we are doing?

2:16:23

We are going ahead and doing a random prediction.

2:16:26

Let's say the model is a dummy classifier.

2:16:28

It is predicting all zeros.

2:16:30

Actually, thus once hey, but my model is only predicting zeros, right?

2:16:35

And then what is happening?

2:16:36

If you try to compare the accuracy, 99% tag up, that is what I meant by the accuracy paradox.

2:16:42

Okay?

2:16:43

We'll get a, excuse me, we'll get a, we'll get an accuracy paradox.

2:16:48

Now the interesting thing is if I go back and try to if I go back and try to create the confusion

2:16:54

matrix of this data, all of you take a look at it, very interesting.

2:16:58

I took some time to explain this to all of you today, okay?

2:17:01

When I go back and do this, I'm it's like to look and give to you, okay?

2:17:05

Now, look, very interesting.

2:17:07

Now, you, you know, how easy it is to understand me, okay?

2:17:10

Although this is a machine learning topic, but I'm still talking about this so that you understand

2:17:14

it well, okay, so if you take a look at it.

2:17:18

This is the actual and this is the predicted.

2:17:25

This is the predicted.

2:17:27

This is the predicted.

2:17:29

This is the predicted.

2:17:31

And this is based on whatever concept you have studied, this is 0.

2:17:39

1 and this is 0 1.

2:17:42

That's what we are able to see.

2:17:45

0101.

2:17:47

01.

2:17:48

So class 0, class 1, class 1, class 0, class 1, that's what we are able to see right now, guys.

2:17:53

That's the intuition.

2:17:55

Predicted versus actual.

2:17:57

You're able to see that, right?

2:17:59

The answer is in front of you.

2:18:02

Now, now look, look, accuracy, what is?

2:18:04

This is your true positive.

2:18:07

This is your true negative.

2:18:10

This is your false positive.

2:18:13

This is your false negative.

2:18:15

Right?

2:18:16

I hope everybody is clear.

2:18:17

Everybody can see this.

2:18:20

Right?

2:18:21

Right?

2:18:22

What is CC?

2:18:24

See?

2:18:25

Oh, okay.

2:18:30

Oh my god. I'm so bad with every patient.

2:18:38

Okay.

2:18:39

See C C.

2:18:40

This is first time I'm in the same in a different league.

2:18:45

I think.

2:18:46

Okay.

2:18:47

Or maybe I'm not that much into all the WhatsApp and all that.

2:18:51

That's why probably.

2:18:53

Okay.

2:18:54

Okay.

2:18:56

Great.

2:18:57

So now, you know, TP is 0.

2:19:01

TN is 990.

2:19:03

So accuracy, what is accuracy?

2:19:06

What is accuracy?

2:19:09

This is obvious.

2:19:10

I mean, without this we understand because

2:19:13

the model

2:19:15

all zeros predicted

2:19:17

so 99% is accurate.

2:19:19

But you can calculate

2:19:20

you.

2:19:21

Accuracy is nothing but

2:19:23

TN plus Tp

2:19:25

divided by total.

2:19:27

Okay?

2:19:28

It is 0

2:19:30

plus 990

2:19:31

divided by 1,000.

2:19:33

990 by thousand.

2:19:37

How that will?

2:19:38

99% would.

2:19:39

Excuse me.

2:19:41

Can you see guys?

2:19:42

99% accuracy.

2:19:43

a model which is 99% accuracy.

2:19:45

That's what we are able to see on the screen right now.

2:19:48

99% accuracy model.

2:19:51

Is it a good model? No, it's a horrible model.

2:19:54

And I'll tell you why.

2:19:55

Because accuracy is not a good metric.

2:19:59

If you take a look at the Confucian matrix,

2:20:01

if you take a look at the Confucian matrix,

2:20:03

you'll see that the model is not doing any one predictions.

2:20:08

This column,

2:20:11

zero is.

2:20:12

This is this one fraud column is, right?

2:20:15

Predicted fraud.

2:20:16

So whatever, whatever model you have built right now,

2:20:20

that model is not predicting any frauds, right?

2:20:23

The model is not predicting any frauds right now.

2:20:27

That is what is going on right now.

2:20:30

There are zero fraud predictions the model is doing.

2:20:33

That's the intuition, okay?

2:20:35

I hope this is clear, absolutely clear.

2:20:39

What else?

2:20:40

There are.

2:20:41

10 false negatives.

2:20:42

That's the other issue.

2:20:45

Everyone's clear.

2:20:46

10 means false negative.

2:20:48

Whenever you see this thing, you relate it back to what I talked about here.

2:20:52

This one bottom left corner,

2:20:55

that's false negative.

2:20:57

And one, guys, you can ask

2:20:59

that, sir,

2:21:00

sir, this 01 is.

2:21:02

You can ask you, sir,

2:21:03

this is, sir, this is this is 0?

2:21:05

That's the valid question.

2:21:07

This is Python convention.

2:21:09

If you've rotated, if you call 0 something 1, something, it will be

2:21:12

just remember this.

2:21:14

So, it's a kind of a lot of

2:21:15

look at it.

2:21:16

If you go to Google Images,

2:21:17

there, this thing is the wrong explained

2:21:18

sometimes.

2:21:20

So, most people don't even know.

2:21:22

Most people just say,

2:21:24

actually, it's Python convention, right?

2:21:26

01 is a Python convention.

2:21:28

Alphabetical order in Python.

2:21:31

So you're here, here,

2:21:33

here,

2:21:34

the original data we have here

2:21:36

output in 01 is.

2:21:38

Now, I'm here about you.

2:21:40

Let's say,

2:21:42

uh,

2:21:43

you have class that's categorical string value

2:21:47

then it's alphabetical order

2:21:48

in alphabetical order.

2:21:50

Alphabetical order, sorted in alphabetical order.

2:21:52

A to Z are smallest to largest.

2:21:54

That is how it is assigned.

2:21:56

Predicted, actual.

2:21:58

That's it.

2:21:59

Or 10 false negatives, guys.

2:22:01

That is very bad.

2:22:02

That means there are 10 such cases where model predicted you don't have,

2:22:05

you're not a fraud.

2:22:07

The transaction is not a fraud, but actually it's a fraud.

2:22:11

So there are 10 such cases where model predicted transaction is not a fraud, but actually it's a fraud.

2:22:15

That's what's going on right.

2:22:17

I hope this is absolutely clear.

2:22:19

All of you are aligned.

2:22:21

And this is to answer the question of the accuracy paradox.

2:22:24

So when given these kinds of imbalanced problems,

2:22:27

if we only use accuracy, it's a problem.

2:22:31

So we have learned Confucian matrix.

2:22:33

And the moment I start using Confucian matrix, we are able to get a clear idea.

2:22:36

idea that this is a horrible model.

2:22:38

Because this model is,

2:22:40

this model here, there's no broad predict any

2:22:42

here. The right-hand side column is empty.

2:22:44

And there are 10 false negatives.

2:22:48

This is a more problem.

2:22:50

Okay? Make sense.

2:22:52

Finally, to complete the story,

2:22:55

this might be a little mathematical, but

2:22:58

again, the objective is not to get into math today in detail.

2:23:01

The objective is not to get into math today.

2:23:03

I think, but I just wanted to

2:23:05

just wanted to give you the intuitive understanding so that you, you know, you basically look at it.

2:23:12

You know, interestingly, our session agenda says, you know, talk about this without formula,

2:23:20

but if you don't know the formula, you cannot relate to it.

2:23:23

You, you know, formula can't even know,

2:23:24

now?

2:23:25

Then I have to give you apple banana examples and then you'll be get confused.

2:23:29

So I have to talk about some formula today, okay?

2:23:32

So without formula is not related.

2:23:33

It has to be with formulas.

2:23:34

So some.

2:23:35

basic formula I will tell you. So, and, but you can relate to it.

2:23:39

So here, we are sorted.

2:23:40

We have seen Confucian matrix.

2:23:42

We have seen T and T P, FN, F and FP.

2:23:45

And now what is precision recall?

2:23:47

Final thing, what is precision recall?

2:23:50

Precision recall is basically this.

2:23:53

Precision recall is basically this.

2:23:56

Here, there a little formula aspect

2:23:59

this is the only formula I'm trying to show you right now.

2:24:02

Okay?

2:24:03

What is precision?

2:24:04

It is TP by TP.

2:24:05

plus fp. You all know what is tp, you all know what is fp.

2:24:08

We are okay.

2:24:10

So once you know that, this is how we calculate precision.

2:24:13

That's it. That's all you just remember.

2:24:15

And what is recall?

2:24:16

This is how we calculate recall.

2:24:18

Intuitively, precision, it tells you the ability to predict correctly.

2:24:24

So precision tells you the ability to correctly predict.

2:24:29

So what is precision?

2:24:31

Precision tells you the ability to correctly predict.

2:24:35

And what is recall? Recall tells you the ability to correctly detect.

2:24:40

Okay, so precision tells you the ability to correctly predict.

2:24:44

And recall tells you the ability to correctly detect.

2:24:48

How well you can detect something.

2:24:51

See, if I have to explain to you a little bit more intuitively here,

2:24:54

that here, here here here here here

2:24:56

you see what is the precision of the one class?

2:25:00

One class's precision what is the precision of the one class?

2:25:02

So out of total 46,

2:25:05

Predicted diabetes cases, 35 of them are correct.

2:25:11

So the precision is 35 by 46.

2:25:14

How do we define precision 35 by 46?

2:25:18

Out of 46 predicted diabetic cases 35 are correct.

2:25:22

So precision is 35 by 46.

2:25:25

How well you are predicting diabetes.

2:25:28

And recall tells you how well you are able to detect diabetes.

2:25:32

If you look at the actual test data, there are 55 actual diabetes cases.

2:25:36

There are 55 actual diabetes cases.

2:25:39

Now, if our test data in 55 actual diabetes cases,

2:25:42

so 55 cases may say 35 I'm able to detect that equality.

2:25:51

Okay?

2:25:53

So, just to help you remember, you can remember it this way.

2:25:59

Precision is like a column total.

2:26:01

Column case.

2:26:02

calculate.

2:26:03

So we say out of this many predicted, how many I am able to correctly predict.

2:26:09

Out of 46 predicted 35, we are able to correctly predict.

2:26:13

Whereas recall tells you, out of actual 55, this much we are able to actually detect, correctly

2:26:20

detect.

2:26:21

So out of actual 55, out of actual 55 once, we are able to detect 35 correctly.

2:26:28

That's what, that's how we are able to understand the intuition of recall.

2:26:31

recall.

2:26:32

So that's recall for you.

2:26:34

That's the idea.

2:26:35

Okay?

2:26:36

I hope this is clear.

2:26:37

Everybody is clear with what is precision and recall.

2:26:39

But actually a formula is, but this is the way to remember.

2:26:42

Okay?

2:26:43

Now, here to Confucian matrix have.

2:26:47

So, another way to remember precision recall is that these are class level accuracy.

2:26:53

Just like all this while we were discussing about the overall accuracy of the model.

2:27:00

And we were talking about the accuracy paradox.

2:27:03

You have an imbalanced data, imbalanced class problem,

2:27:06

a dummy classifier is,

2:27:11

that's only not fraud predicts right now.

2:27:13

You have a dummy classifier that is only predicting not frauds right now.

2:27:16

That is only predicting not frauds.

2:27:18

The model is only predicting not frauds.

2:27:20

That is what it is doing.

2:27:23

And

2:27:25

accuracy is coming out to be 99%.

2:27:30

But the moment you look at the class level accuracy, you will see the class level accuracy will actually be very low.

2:27:38

And that is exactly what is happening in my demo also.

2:27:41

Abdeco, for the same use case, my precision and recall values are coming out to be very low.

2:27:46

So we have talked about precision. We have talked about recall.

2:27:50

And what is F1 score? F1 score is like a combination of precision and recall.

2:27:54

2 PR by P plus R. That is what F1 score is. It's a formula.

2:27:57

Let's just remember.

2:27:58

So F1 score is like a new kind of accuracy.

2:28:00

even think of it that way.

2:28:01

Yeah, we will come back to this once again in our classification discussion, but for now,

2:28:05

for today, the broad agenda was to just tell you how to think through it,

2:28:11

uh, frame a problem in your mind, take a data, build a model, evaluate the model,

2:28:17

build the Confucian matrix, actual versus predicted.

2:28:20

So, this is the Confucian matrix that we are able to see, actual versus predicted.

2:28:24

And now based on that, you can find out what is TN, TP, F and FP.

2:28:28

You can find out what is TN, NTP, F and FP.

2:28:29

You can find out what is TNTP.

2:28:30

and FP based on the Confucian matrix you can find that out. And we get the precision recalls based on that.

2:28:39

So what is precision again? The ability to correctly predict. How well you are able to predict.

2:28:45

There are 46 actual ones. We are predicting for sorry, sorry, sorry. There are 46 predicted ones.

2:28:51

Out of 46 predicted ones, column total, 35, we are able to correctly predict it.

2:28:56

What about precision? How precisely we are able to predict?

2:28:59

And recall, what accurately we are able to detect?

2:29:03

In your data, 55 actual diabetic loggs,

2:29:05

we're from those of them.

2:29:07

This is your precision and recall.

2:29:10

And both of combined, we get F1 score.

2:29:12

So these precision recall F1 scores are what we call class level accuracy.

2:29:18

So, now we were discussing overall accuracy.

2:29:20

The whole model accuracy is what? DN plus DPSA. Normal, overall.

2:29:24

That was not giving us the correct picture.

2:29:25

We already saw that. Accuracy paradox.

2:29:27

Now we are now.

2:29:29

We have something better in our hands.

2:29:31

Now we have class level accuracy.

2:29:33

Now, the zero class is,

2:29:34

that we can out of accuracy,

2:29:36

precision recall F1 score.

2:29:38

And the one class is,

2:29:39

that we can't exactly accuracy

2:29:40

we can't precision recall f1 score.

2:29:42

And then we'll get a better idea

2:29:43

how the model is doing.

2:29:45

That's the concept.

2:29:47

And now this is to summarize the conversation.

2:29:51

Code is nothing, one line of code.

2:29:53

There's a function called Confucian underscore matrix.

2:29:55

Here there actual is,

2:29:56

there are predicted,

2:29:57

there.

2:29:58

Okay.

2:29:59

So, this we already discussed.

2:30:01

Accuracy was 99% useless.

2:30:03

Paradox.

2:30:04

We already talked about it.

2:30:05

Accuracy does not help.

2:30:06

So what we do?

2:30:07

We create a classification report.

2:30:09

It's called classification report

2:30:11

where we will see the class level accuracy.

2:30:14

The zero class is,

2:30:15

its performance is how is?

2:30:17

Precision Recall F1 score

2:30:19

and how is?

2:30:20

And the one class is,

2:30:22

the precision recall F1 score is.

2:30:24

Answer are you are in.

2:30:26

Answer are you already know what's going on.

2:30:28

know what's going on.

2:30:29

So the one class is,

2:30:31

the model is doing very poorly for the fraud class.

2:30:33

The model is doing very poorly for the fraud class.

2:30:35

That's not performing.

2:30:36

Poorly is the other part.

2:30:38

The model is useless.

2:30:39

It is unable to detect.

2:30:41

It is unable to predict any frauds.

2:30:43

It is unable to detect any frauds.

2:30:45

So the model is,

2:30:46

the fraud's not doing in a real world scenario,

2:30:49

bank's management, CEO,

2:30:51

pay developers hire and say,

2:30:53

well, model,

2:30:54

for a fraud detect for me.

2:30:55

And you've made this.

2:30:57

And you've made this.

2:30:58

I said, sir, I made model

2:30:59

99% accuracy.

2:31:01

But when people start to,

2:31:02

when people start to actually investigate,

2:31:04

they will see that this is a useless model.

2:31:06

Accuracy is 99%.

2:31:08

But they will evaluate based on these parameters.

2:31:10

That,

2:31:11

that's what you've made that

2:31:13

model is unable to detect any frauds.

2:31:16

Got it?

2:31:17

So this is the concept of imbalance and how we

2:31:20

identify imbalance

2:31:22

and what is the problem of imbalance

2:31:24

using Confucian matrix.

2:31:27

That was a new topic we saw.

2:31:28

and we also discussed about something called classification report.

2:31:32

Okay.

2:31:33

And just to clarify, this was the first level discussion,

2:31:36

we will again come back to this in our classification topics.

2:31:39

Okay,

2:31:40

where we actually model binae

2:31:41

we'll actually model bina,

2:31:43

because model building we have not come to yet.

2:31:46

There we will build models and we will once again talk about this particular thing.

2:31:51

Now, fixing imbalance.

2:31:53

How do we fix imbalance?

2:31:55

We use something called smote.

2:31:57

So Smote is one of the techniques that we can use to fix imbalance.

2:32:01

So, this is our data.

2:32:03

So I think the straightforward one we are actually doing right now.

2:32:06

What are we doing?

2:32:08

Baseline model we are trying to build.

2:32:10

We have x, we have, we have y.

2:32:12

We have trained test split.

2:32:13

We have an algorithm used called logistic regression.

2:32:16

Just assume that for a minute.

2:32:18

Logistic regression is an example algorithm we are using for classification.

2:32:23

Just imagine that for a minute.

2:32:25

Dot fit kia.

2:32:26

We have predicted here.

2:32:27

here, right?

2:32:28

F1 score is like a combination action.

2:32:30

What is F1 score?

2:32:31

F1 score is like a combination of precision and recall.

2:32:35

So just to come back to this once again, what is F1 score?

2:32:38

F1 score is basically nothing but a, think of it like a combination of precision and recall.

2:32:43

It is a mean, it is 2 PR by P plus R.

2:32:46

Precision recall we have understood.

2:32:47

F1 score is like a combination.

2:32:49

There is no definition of F1 score.

2:32:51

F1 score kind of definition because you can't define what is 2 PR by P plus R.

2:32:55

We can define precision, you can define recall.

2:32:57

But you can't define this.

2:32:58

This is like a combination.

2:32:59

To be more specific, Akshad, it is the harmonic mean of precision and recall.

2:33:04

Again, I'm avoiding these formulas today.

2:33:06

But since you are asking, it is the harmonic mean of precision and recall.

2:33:09

I mean, you mean, you kind of average is you a average idea.

2:33:15

On an average, how is the model, how well is the model predicting?

2:33:19

And how well is the model detecting?

2:33:21

So on an average, you're getting up both these parameters.

2:33:25

That is what it tells you.

2:33:27

Okay? Is it fine, Akshut?

2:33:31

Is it fine? Okay. Uh-huh. Let's move on.

2:33:38

So what we have done right now is we have once again used a basic model, baseline model we are using

2:33:44

right now called logistic regression. And we are fitting the model on the train data, X train by train.

2:33:52

And we are doing that prediction. And we are creating the confusion matrix. And we are getting the confusion matrix.

2:33:56

and we are getting this. Look at this all of you.

2:33:59

This is exactly the problem when we train a model on imbalanced data.

2:34:04

This is exactly what I explained.

2:34:05

When we imbalanced data in model can train the model will always predict not frauds.

2:34:12

The model will not predict any frauds.

2:34:13

That is only predicting not frauds. It is not predicting any frauds. That is what is going on right now.

2:34:20

So we use something called Smote.

2:34:23

Smote stands for synthetic minority oversampling technique. That is what Smote's

2:34:26

for it stands for synthetic minority oversampling technique. So basically the concept

2:34:30

is what? It is nothing but it just, it just uses math to generate brand new synthetic fraud

2:34:38

examples. That is all it does. The algorithm is not required here, but the concept is important.

2:34:43

So above so you, our past actual data may there were 990 not frauds and there were 10 frauds.

2:34:50

Right. Actual data may that is what we had. We had 990 examples of not frauds and we had 10

2:34:56

examples of frauds. So what we do in Smote is we take those 10 examples of frauds

2:35:02

and we try to create many more synthetic fraud examples. So we take those 10 fraud examples

2:35:09

and we try to create many more fraud examples. Many more synthetic fraud examples.

2:35:13

We try to create. That is what we do in Smote. We try to create many more synthetic fraud

2:35:19

examples. And this is the code for it. This is the code for it. This is the code for it.

2:35:24

you can you can see this is straightforward smote we are instantiating bit resample

2:35:29

we've and then we're back from we're smote's on model

2:35:35

and if i run that you will see that this is a much improved model

2:35:40

the model is starting to predict on the this cases this is better than this right

2:35:48

now here there are two false negatives here there are zero false negatives better model

2:35:52

Actually, we have classification report here here.

2:35:55

I can add a line to print the classification report maybe.

2:35:59

Again, Jemina is all going to do anything actually.

2:36:02

So let me just print the classification report.

2:36:04

You can see the incomplete input.

2:36:08

Oh, sorry, the bracket is missing.

2:36:11

Now, if you're going to, answer you're in front of you.

2:36:14

This is the baseline model without Smote.

2:36:16

Normal data we've made.

2:36:18

We have explained here, right?

2:36:20

I told you that the class level matrix are all the

2:36:22

zero, useless model.

2:36:24

Fraudphe's not going to do.

2:36:25

Now we've smote here,

2:36:27

we've got fraud-s synthetic examples add

2:36:29

here.

2:36:30

Now if I go and do this,

2:36:32

if I go and do this, okay?

2:36:35

Let's go and do this.

2:36:37

If I go and run the code now,

2:36:39

you can see the answer in front of you.

2:36:41

Look at that marginal improvement I got.

2:36:43

Look at this guys.

2:36:45

Now look at here.

2:36:46

Accuracy, forget it.

2:36:48

What is important is one class.

2:36:49

The class matter care

2:36:51

banks management has paid you money to identify fraud.

2:36:54

They want you to identify frauds.

2:36:58

That's it. So now my model is identifying frauds.

2:37:01

And the best thing is that,

2:37:03

recall is 100% out of all the frauds that actually happened,

2:37:06

we have all the frauds identified.

2:37:08

That's a very good thing.

2:37:09

So it's better than what we had before.

2:37:11

Behavior from all it's zero.

2:37:12

Now it's better than what we had before.

2:37:15

Okay, I got it.

2:37:16

So that is the big picture idea of what we have managed to achieve here.

2:37:20

And these are some sample case studies I've given where you can actually kind of go and take a look at it.

2:37:27

Whatever I explain credit card fraud detection, this is a very nice data set, very nice practical data set.

2:37:33

This is also a very nice disease data set.

2:37:35

I've discussed about these two broad use cases today.

2:37:38

Yeah, your credit card fraud detection data set.

2:37:41

You can go over.

2:37:42

It's all there in my notes.

2:37:43

I've shared my notes with you.

2:37:45

It's all in my notes.

2:37:47

And very real world thing.

2:37:49

Okay.

2:37:49

So this is a real world.

2:37:50

credit card data in 2013 from European card holders.

2:37:53

You can see how the data is arranged.

2:37:55

A lot of features are there.

2:37:56

And a second one is on stroke prediction.

2:37:58

Very interesting.

2:37:59

We're looking at the different features of a person and we are trying to predict whether the person

2:38:03

will suffer from stroke or not.

2:38:05

So this is how you can use.

2:38:07

And both very, very good examples of highly imbalanced data.

2:38:11

Which in practical may ho go.

2:38:14

If you, if you're a saw patients' sample look at,

2:38:17

so from one of the stroke over.

2:38:18

So, that is the reality of the industry.

2:38:21

If you're doing any classification model in the real world,

2:38:24

yeah, to disease prediction caro, fraud detection caro,

2:38:27

anything you do, anything you do,

2:38:31

you will always encounter imbalance.

2:38:33

And smote is one of the ways to do it.

2:38:35

And there are other things that we will see.

2:38:37

But smote is one of the methods, okay?

2:38:39

Generally.

2:38:43

Yeah.

2:38:44

And, uh,

2:38:48

Finally, one last idea that I wanted to briefly cover, although this is going to be part of my,

2:38:54

part of the machine learning conversations, briefly we will talk about it.

2:39:01

Just give me one second.

2:39:06

This is actually kind of a very nice use case, you know, you can pictorially see it.

2:39:10

So this your original data.

2:39:12

This your original data is right.

2:39:14

You can see four class, four reds and four blues.

2:39:16

When you do smart, you get something like this.

2:39:18

to artificially increase the number of examples.

2:39:21

So what it does is, the neighborhood is where we try to create some more samples.

2:39:25

That is what we do.

2:39:26

Okay, I think there's a better picture.

2:39:28

If you, if some of you're interested, this is, this is something I have seen from this

2:39:34

site called machine learning mastery.

2:39:35

It's a good site actually. Machine learning mastery.

2:39:38

Here here, the example is a,

2:39:40

kaffi actually, so they've explained it very nicely visually, you can take a look at it.

2:39:46

Okay, this is the classic example.

2:39:48

of smote, you can see. There are lots of data points we can see.

2:39:51

So, you have the blue stand for not frauds. The oranges are for frauds.

2:39:55

So there are like thousands of not frauds and there is only 10 or 20 frauds.

2:40:00

So what is smote doing? It is taking those orange points. And in the vicinity,

2:40:04

it is trying to artificially create more frauds.

2:40:07

But it's like saying, if you know, if you know, there's some fraud here, then it's

2:40:11

around-b-b-b-b-b-you-b-b-b-b-b-you-try. You're trying to synthetically create some data.

2:40:15

So when you do smote on this data, you actually end up getting something.

2:40:18

like this.

2:40:20

This your original data, right?

2:40:22

Smote-karned-ka-back, it was the same thing.

2:40:24

It was the same thing we here here here.

2:40:26

Smote-karned-karned-up,

2:40:27

this is something.

2:40:28

You synthetically end up getting a data set like this.

2:40:31

You're getting more examples of oranges, basically.

2:40:33

This is this thing what will be, the model will be more robust.

2:40:37

And you will end up getting better precision recall matrix.

2:40:43

Because the model will start performing better on the one-class.

2:40:47

It will predict better, it will detect.

2:40:48

better. Mano, remember, precision, how well you're able to predict.

2:40:53

Recall, what I mean, how where you're able to detect. Keep that in mind and keep my formula at the

2:40:57

back of the mind. That's it. As long as you remember this table, that is it. That is it. That is it

2:41:01

that you need to remember. Okay? And yeah, that was the part. And finally, there's one last piece that we

2:41:09

had, which is called, you know, kind of cross-validation, which is actually related to our

2:41:15

our next piece and what I want to do is at least just briefly talk about it, but anyways,

2:41:22

we'll take it up in detail in machine learning. So what is, what is cross-validation? I just want to

2:41:26

kind of explain to you intuitively, but again we're making in detail. And so all that we do in cross-validation

2:41:36

is that we try to do multiple train test pitch. So if you remember the conversation, what I had with you

2:41:45

on day one, day one where I talked about how you take a data, how you split a data into training and

2:41:51

testing. Train may up model go learn and test in you evaluate the model. You train the model

2:41:59

on training data, evaluate the model on testing data. That's what you do. And we get one single

2:42:04

test accuracy. But in cross-validation, what we do is we don't get one accuracy. We get 10 accuracies.

2:42:11

So we, so it's like saying we don't have one mock paper. We have 10 mock papers.

2:42:15

And we try to take whatever model we learned and we try to evaluate that model on 10 different

2:42:22

mock papers and calculate an average. That is the intuition of cross-validation, what we do. If I have to

2:42:29

give you one more example to a beautiful example to help you think through it. Imagine you go for

2:42:34

an interview. A lot of you will take interviews now. Okay. So I've interviewed or do you ever go through

2:42:45

one round of interview? You go through multiple rounds of interview. And

2:42:49

all the other rounds by other questions. Multiple questions are asked to you. That's the intuition.

2:42:55

You go through multiple rounds of interview, right? So, so if you, if you are only asked

2:43:04

one question, if you only went through one round of interview, what would have happened?

2:43:10

You would have performed like, it will be fluke chance, right? So to be more robust, to

2:43:15

to make the process more robust, they take you through multiple rounds of interview.

2:43:18

Multiple rounds of interview are conducted. That is basically what goes on behind the scenes.

2:43:22

Multiple rounds of interview are conducted. That's the big picture idea.

2:43:28

So we, you go through round one, round two, round three, round four, round five,

2:43:31

or two, round ten. Across the ten rounds, we see how you performed in each round.

2:43:36

Round one, what was your accuracy? Round two accuracy, accuracy, round three accuracy, accuracy,

2:43:40

round four accuracy. Accuracy. That's all the rounds of what, what are you? Okay. And

2:43:45

on that we are we have got accuracy for each of the rounds and now we are calculating

2:43:48

an overall accuracy. Overall accuracy. What overall accuracy? Yeah, what I cross-validation.

2:43:55

I mean, we are making the evaluation process more robust. If I have to again give you the

2:44:00

analogy based on the mock question paper what we studied. A bit of we were discussing that you are

2:44:05

solving one mock question paper. And that one mock paper in your performance

2:44:09

how is? Now in cross-validation what we were doing, we will have five mock papers. You are

2:44:15

10 mock papers.

2:44:16

Practice in we do, in real world, what we can't?

2:44:19

Can we make a mock paper solve?

2:44:21

No.

2:44:21

We have the trained data.

2:44:22

We learned the patterns.

2:44:24

And what we learned from our textbook,

2:44:27

we actually saw 10 mock papers.

2:44:29

Thus, mock question paper

2:44:30

solve.

2:44:31

Mock paper 1, how much,

2:44:32

how much?

2:44:33

We will calculate the performance on

2:44:36

every single mock paper.

2:44:37

And take an average.

2:44:39

That's only okay cross-validation.

2:44:41

I'm just giving the intuition today.

2:44:43

This is a completely machine learning topic which we

2:44:45

we will start in the next class onwards.

2:44:47

Next class onwards, we actually start up with regression.

2:44:50

And regression to do classes rang.

2:44:53

Classification, we have two classes.

2:44:55

And that is how we will be, you know, basing through.

2:44:59

So, yeah, and just to kind of summarize the conversation, what we did.

2:45:06

So we have talked about data leakage.

2:45:08

Data leakage too, it's a continuing discussion.

2:45:10

So it was something we discussed briefly on the last class.

2:45:13

And today also we talked about data leakage.

2:45:15

leakage. So we looked at the concepts behind data leakage, what it is.

2:45:20

We introduced the concept of class imbalance. We spent a lot of time discussing this, right?

2:45:26

Understand the impact of imbalance. What is the impact of imbalance? Right. In balance,

2:45:31

accuracy is not the best metric. We talked about that. We introduced precision recall.

2:45:37

So the year we are saying conceptual only, but there is nothing called conceptual. Unless I discuss in

2:45:40

detail, you can't explain precision recall, but that's okay. I think that's what the, how

2:45:45

it is written. So I'm just trying to do. But we have actually went through it is in detail.

2:45:49

Okay. But this is something we will again, you will again see this in our classification session in

2:45:54

detail. Okay. So we have seen this in a lot of detail. What is precision? What is recall? What is

2:45:58

F1 score? Along with formulas we have seen also in detail. Okay. And we have also seen how to handle

2:46:04

imbalance and the conceptual, only the conceptual, only the conceptual, only the conceptual understanding of what is

2:46:08

cross validation. So cross validation, as I said in code will be seen later. Okay. So,

2:46:12

so basically we have discussed the concept of averaging results.

2:46:15

So we averaging Q are.

2:46:17

Just like mock paper example we saw.

2:46:19

So these are the pieces that we saw overall in the session today.

2:46:23

So, fine. Thank you guys. That will be all from my end. And I think the

2:46:28

the Confucian matrix part took a little time.

2:46:31

Rest, I think we are, we are wrapping up on time today.

2:46:35

Hope we had a good session today. I'll pass it over to Pratap for the quiz.

2:46:40

Thank you. Thank you, everybody. Once again, have a good night.

2:46:45

I'll see you all in the next session. Next session we start with ML. Next session is actually on linear regression.

2:46:49

We finally started machine learning.

2:46:51

Abbe all this while we are talking about model building, model building, model building.

2:46:54

You won't be wondering, sir, where are model? We are finally going to see model in the next class, right?

2:47:00

Okay. Yeah, yeah. How can we practice this? What do you mean? What do you mean?

2:47:06

What the practice? Like, it's through my notes, right? I'm sharing a lot of notes with you.

2:47:11

By the way, this is the cohort link. So this is I've already shared you.

2:47:15

Take it.

2:47:17

So, this is the, this is the cohort link.

2:47:23

Anna? So this I've already shared with you. And you'll be able to access. And I think rest of the rest is all,

2:47:29

I've shared, I think, part of it is through my notes. Part of it is through all the Kaggle exercises.

2:47:34

If you go through my notes, I'm sharing a lot of reference content here.

2:47:40

The Maasai content is also very good. We have also curating very good content for you in terms of how,

2:47:45

you can study relevant content for you with a lot of case studies.

2:47:49

So I think it's a, it's so learning in today's world is very unstructured, you know.

2:47:54

I think this will again be a different session where we can talk more about it.

2:47:58

But you have to be very comfortable with the unstructured way of learning.

2:48:03

Our education system may, but honestly, even I have grown up in the same education system.

2:48:09

And honestly, if you ask me, I've wasted maybe 15, 20 years of my life.

2:48:12

If you're given another chance and another day, you'd probably think if a school college

2:48:18

go and what was going to go ahead. So, basically. So I think you have to be very comfortable with

2:48:24

the non-linear way of learning. The unstructured way of learning. Problem is our school college

2:48:32

we have been given too much structure. Our education system, our societal structures, our parents and all

2:48:37

teachers and tutors, who a linear structure built up. A, then B, then C,

2:48:42

then D, then E.

2:48:44

And one in kind of disconnect. We are all confused.

2:48:46

What go ahead. The world is broken.

2:48:49

But then we have to...

2:48:50

Learning in today's world is an art.

2:48:53

And you have to be very comfortable with the unstructured way of learning.

2:48:57

It is very clumsy.

2:48:59

There's a lot of noise.

2:49:00

There's a lot of things that are happening today.

2:49:02

And you have to be very comfortable in that.

2:49:04

Here here linear, there is no.

2:49:07

Although we are trying to put together a content to teach you linearly.

2:49:10

As a teacher, I will tell you have to be comfortable with the knowledge.

2:49:12

non-linearity. I'm teaching you some things right now in the class.

2:49:18

You'll class after course explore

2:49:20

you. You'll go to YouTube may go. News per go. Let's say large language models.

2:49:25

Agents is our is our course. Right. So we have not started it.

2:49:28

But that will not stop you from exploring. Right.

2:49:30

You go ahead and go ahead and go ahead.

2:49:32

Sir, yeah, what is what is what is. And you will do that. And I am encouraging you to do that.

2:49:36

I'm telling you you have to be comfortable with that non-linear way of learning.

2:49:40

school model not is.

2:49:43

that class two in,

2:49:44

so class seven

2:49:45

class seven can't do that book

2:49:47

in that time.

2:49:48

Here there's

2:49:49

there's a class two

2:49:49

be,

2:49:50

class seven be

2:49:50

online.

2:49:52

And you have to be very

2:49:53

comfortable with that.

2:49:55

So that is how we

2:49:56

have to practice and learn

2:49:57

Akshat.

2:49:57

So it's a long

2:49:58

conversation.

2:49:59

I wanted to just

2:50:00

keep it very brief today.

2:50:02

But I think we can do a small

2:50:03

career session later on

2:50:04

with all of you

2:50:05

based on interviews and

2:50:06

hiring tips and I'm sure

2:50:07

that will be

2:50:08

people will be interested in that.

2:50:10

We can

2:50:10

take it up. We can take up a separate class just to talk about all this with all of you.

2:50:14

Okay. Yeah. Thank you. Thank you all of you. So I'll pass it over to Pratap from you. Yeah. Thank you guys.

2:50:23

Yeah. So thank you, sir for the session. And thank you guys for attending it. I will now release the

2:50:31

feedback poll. Once the feedback poll is done, you can start joining the Mentimeter quiz. I am

2:50:40

in the link for that as well.

2:51:10

All right. A few people have not completed the feedback poll. So please quickly complete the feedback poll and then you can join the Mentimeter quiz.

2:51:40

Kirti, if poll is not showing for you, that's fine. I can't relaunch it right now, but maybe in the next one, then you will be able to do it.

2:51:52

Okay. Is anyone left for the polling or if not, then you can just quickly join the Menti meter quiz session and I'm seeing there are only seven people, seven players right now. So do join. I'm sending the link here.

2:52:10

Okay, Anjali, no problem if you're not able to see the pole.

2:52:30

That's okay.

2:52:32

you can you can attempt it next time anyone else who is uh trying to join the

2:52:44

mente meter quiz you can just send a message in chat or else i'll start in about 30 seconds

2:53:02

Okay, 10 more seconds till the Menti meter quiz is showing started.

2:53:32

A model gets 99.8% accuracy on a data set.

2:53:37

What would be the interpretation?

2:53:43

So it's a fraud, not fraud, data set.

2:54:02

obvious actually. Yes, great job guys. It seems some people are just guessing,

2:54:12

but then still good job. Most of you did get that correct.

2:54:32

Suppose we are going with nine players only then.

2:54:39

Why can duplicates across train and test inflate evaluation scores?

2:54:47

So there are duplicates in both train and test.

2:54:53

So.

2:55:07

Yeah. So the model is effectively seeing the same case.

2:55:22

same case during training and testing. The duplicates will be there in both train and test.

2:55:28

The test set becoming larger than the training set is not a problem. So that does not really inflate

2:55:37

evaluation scores. Usually the, or the test set becoming larger is not really

2:55:43

I'm not aware of that if it's a previous question.

2:55:58

But okay, moving on to the next question.

2:56:04

By the way, yeah, just very quickly, the test set becoming larger than the training set is not a problem and it does not really affect.

2:56:13

evaluation scores in any way.

2:56:17

All right?

2:56:29

Right?

2:56:31

It seems we lost a player.

2:56:37

Okay, there we know.

2:56:42

A team balances the training data with oversampling and then also balances the test set before reporting final performance.

2:56:57

So oversampling is basically increasing the number of samples.

2:57:12

Yeah, so that is correct.

2:57:23

The reported test result may not reflect the real world class distribution because we have used oversampling

2:57:31

to increase the number of samples in the test set.

2:57:38

And that may not be not be accurate.

2:57:41

accurate may not reflect the real actual this thing distribution so great

2:57:52

job guys that was one of the difficult questions you guys have the correct idea

2:57:59

and that's the most important thing to get the correct intuition so yeah you're

2:58:06

there you're almost there what is the main trade-off of under sampling the majority class

2:58:11

understand under sampling means you are taking less number of samples from the majority class okay this is regardless of train test this is in the data set itself

2:58:41

Yes. So most of you did get that correct. It is basically throwing away useful majority class information, as in it can throw away useful majority class information.

2:58:52

Um, yeah.

2:58:57

One of the ways to fix this is the sampling imbalance fixes with Sir has explained and he will be going in more detail in the next sessions.

2:59:07

Okay, last question guys.

2:59:11

All right.

2:59:22

Okay.

2:59:25

Okay.

2:59:29

Excuse me.

2:59:34

A fraud model catches 30 out of 100 real fraud cases.

2:59:38

It produces very few false alarms.

2:59:40

which description best fits the model. Understand, 30 out of 100 real fraud cases, okay?

2:59:48

So which is the, which is like the guess, which description like would fit best?

3:0:09

Okay, yeah. So very quickly, 30 out of 100 real fraud cases it has caught. Now, as sir has explained at the very end, and if you guys remember, basically, it is trying to catch all the fraud cases. And out of 100 cases, it has caught 30. But it is accurately catching these 30, right?

3:0:39

So the precision is very high because whatever it is predicting as a fraud is going to be included in the fraud.

3:0:49

But as you remember, recall is the ability of actually being, uh, so if the model was, say, 70 or 80 out of 100 real fraud cases, that would have been a good recall, right?

3:1:06

actually being able to predict what is the real fraud that would have been a good recall but it is not predict it is letting go a lot of those fraud cases and instead it is focusing more on precision and that is why the precision is very high and the recall is very low that's right this was a little difficult question because it was the application of what you have just learned but that's okay most of you

3:1:36

have gotten the correct intuitions and obviously in the next few lectures, sir will build up more on this.

3:1:43

So no worries if you got it wrong.

3:1:49

All right. Great, great.

3:1:53

Oh wow, Arnica came in clutch. Good job. Okay. All right. With that, we are at the end of the

3:2:02

session. Looking forward to seeing you in the next session.

3:2:06

that will be an exciting machine learning linear regression session.

3:2:11

So yeah. All right. Good night, guys. See you on Wednesday.