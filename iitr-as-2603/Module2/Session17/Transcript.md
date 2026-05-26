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

Hi, everybody. We'll just be starting on.

9:18

Thank you.

9:48

Okay, I'm just sharing my screen.

9:51

Just allow me a minute, guys.

9:52

So, so I'll settle down.

10:18

Thank you.

10:48

Thank you.

11:18

Thank you.

11:48

Thank you.

12:18

Thank you.

12:48

All right.

12:52

So, uh, let's start on with the

12:55

So, uh, let's start on with the session here, guys.

13:11

So I have to today is a very interesting session and it pretty much continues on from where we left off last time.

13:17

of last time. So last session, we had a very introductory discussion in terms of what

13:23

is regression. We looked at what is regression. We looked at the different aspects of regression

13:30

we explored in the session. And we also looked at a very basic piece of code how to build a model.

13:36

So at this point in time, we are very comfortable with how to take our data, how to split the data into training data, testing data,

13:42

and how to basically evaluate the model.

13:44

And in the last session, we also explored at a very basic

13:47

level, what is overfitting, what is underfitting, what is good fit. So that was the thing that we saw, right? So I'm just going to take you back to a little bit of what we saw in the last class. I think that was 18th May, 20th May. So 28th May, we saw this, you know, a very simple linear regression demonstration in the session where we were able to take a sample data set. We were able to take the data. We were able to split the data into training, testing. We understood the concept of what is splitting.

14:17

What is trained data? What is test data? So we always learn the patterns from trained data. And we always evaluate the patterns on the basis of the unseen test data, okay? And on the training data, we fit the linear regression model. And based on whatever linear regression model that we fit on the training data, we go and evaluate that model on the training data and the testing data. So we talked about that. Okay. So now, so we also looked at two very, very important two very important activities.

14:47

accuracy we have something called train accuracy. We also discussed about something called test accuracy.

14:52

And so what is training accuracy?

14:55

Training accuracy is how accurate, how well the model is able to perform on the,

15:00

you know, on the test, on the, on the revision. So while you're, you know, while you're using,

15:07

while you're evaluating yourself on the training data, the revision set, how well the model is

15:11

able to perform on that, that is training accuracy. And test accuracy means how well the model is

15:15

performing on the, on the unseen test, unseen question paper.

15:18

That is how we define the test accuracy.

15:21

So that is the way to look at it.

15:23

Okay.

15:23

So we looked at all these and we understood intercept.

15:26

We understood coefficients.

15:28

Okay, we also understood the concept of residuals.

15:31

Residuals means errors.

15:32

Okay, so regression is about the best fit line.

15:35

We are trying to find what is the best fit line.

15:37

And residuals basically mean what is the difference between the actual and the predicted.

15:41

So we talked about that as well.

15:43

And finally, towards the end of the conversation,

15:45

went into the concept of overfitting versus underfitting.

15:48

It was a very, very important conversation that we have.

15:50

And we talked about this diagram.

15:52

To simplify the understanding, we talked about this diagram,

15:54

and we understood the meaning of underfitting.

15:57

What is underfitting?

15:58

Underfitting is that kind of,

16:01

is that property of a machine learning model where the train and test errors both are very high.

16:07

So whatever model you built, the training error is also very high,

16:10

and the test error is also very high.

16:11

So that is how we understand the meaning of underfitting.

16:14

And overfitting,

16:15

is that kind of that property of a model, whose train error is very low, but whose test

16:19

error is very high. That is how we define overfitting.

16:22

Underfitting means the train and test errors both are very high. The training error is also

16:25

very high and the corresponding test error is also very high. That is underfeit model. That means

16:30

the model has actually not learned anything. That is underfitting. And overfitting basically means

16:34

the train error is very low. That means the model is performing extremely well on the training data.

16:38

So on the training data, it is not making any mistakes. But on the unseen test data, it is actually

16:42

making a lot of mistakes. So that is how we understand the

16:45

you know, the concept of overfitting. And then obviously we have the good fit model.

16:49

The good fit model is something that we have in between. That is how we go back and define the meaning

16:53

of a good fit model. So this is again something I just wanted to very quickly recap because

16:57

these are related aspects for the session today. Today's session is, I would say,

17:01

comparatively lighter because conceptually there is a lot that we have talked about so far. Just one

17:08

or two new ideas that I will discuss. But majorly, I want to drive this session as a hands-on session.

17:14

We will do some exercises. We will do a bit of hands-on. I'll encourage you guys to do some

17:19

hands-on. So we want to dedicate a good half and hour, 40 minutes in the session for hands-on

17:23

activities. But broadly, the concepts are very much related to what we discussed in the last session.

17:28

Okay. So that way, concept-wise, it is comparatively lighter. So the topic for today is basically,

17:34

you know, it is basically regularization. So we are discussing something called regularization.

17:40

And that is what we'll be, you know, what we'll be talking about. And just to,

17:44

very quickly summarize the ideas in terms of what we will be doing in this particular session.

17:49

So we will talk about the concept of regularization. We will talk about what, you know,

17:55

a regularization is. We will get into model comparison. This is the part where we will see a significant

18:00

amount of hands on. So we'll understand how to compare models. Like we will build a basic linear

18:06

regression model. Then we will regularize it and we will see how the accuracy metrics are changing.

18:11

we will talk about different evaluation metrics all this file. We have already used.

18:15

We've already used some error metrics. So we'll try to formalize that today what these evaluation

18:19

metrics are. Again, the objective is not to bore you with formulas. The objective is to actually

18:24

show you things in code. Just to build that intuition that, okay, this is accuracy, this is error.

18:28

But we don't want to get into formulas and all this year. Okay. Error analysis. This is the basic

18:33

discussion we will do. And finally, you know, we'll talk about a bit of a practical perspective in terms of

18:38

choosing metrics. So it's a, I mean, concept wise, it's a pretty light session that we'll be

18:43

doing here. All right. Now, so, we talked about the concept of overfitting in the last session

18:53

and just to very quickly summarize this one second for you. What is overfitting? Overfitting is a

18:59

property of machine learning where, you know, it's basically an overfeit model is that model, where the model

19:07

performs very well on the trained data. That means you learn the patterns on the training

19:12

very well. But when you try to evaluate that, that particular model on an unseen test data,

19:19

it performs very poorly. So training may gives you very good results, but testing made is giving

19:24

extremely poor results. That is what an overfit model basically reprocessing. So let me start

19:31

directly with the code. So let us simulate a real world scenario. So what I have

19:37

will do is I'll simulate a real world scenario. Imagine we are predicting housing prices.

19:42

It's a classical regression problem. So we've got different different features of the house. And based

19:47

on the different different features of the house, we are trying to predict what is the price of the

19:51

house. That is what we are trying to solve. So we have got many, many features of the house. And based on all

19:56

the different different features of the house, we are trying to predict what is the price of the house. That is

20:02

what we are trying to do. So based on all the different different features of the house, we are trying to predict and

20:06

estimate what is the price of the house. So we have total 80 features about the house.

20:11

There are total 80 features we have about the house. And as I said, based on the different

20:15

different features of the house that we have, we are trying to predict and we are trying to

20:19

estimate what is the price of the house. Now, if you look at it, all 80 features of the house

20:25

may not be important, right? Now, this may not be important. Like if you talk about a typical

20:29

housing data, what are the things that really impact the price? I think by now we are

20:36

already done quite a bit of machine learning sessions and we, we understand things a little better

20:44

today, right? What are we really trying to do in ML? You have an input, you have a typical

20:51

housing data. You have the different, different features of the house. But the size of the house,

20:58

number of bedrooms, number of bathrooms, locality of the house.

21:06

we can talk about income level of the locality.

21:08

The place that home is, it's the income level

21:10

like we say it's a very posh area.

21:13

So locality is okay, but how posh is it?

21:15

And there are different indicators.

21:17

India in a census survey. So you can find out per capita GDP of the area, those kinds of things.

21:23

So, you know, so these are all the different, different features of the house.

21:27

And based on that, the output will be what is the price of the house?

21:30

You have if you're going to buy property to where this is, there are basically a lot of portals where you can estimate the price.

21:36

of the property. They estimate the price of the property. Now that you have

21:39

property based on your age of the property, your, you know, it's a one BHK, 2BHK, a lot of

21:46

websites will actually predict what is the price of the house. So that's the use case. Now, all the

21:51

80 features may not, may not be important. Ultimately, what is the most important predictor

21:56

of a house price size? All other things are important, but that's not as important.

22:02

Yeah, but that's not as important. Ah, but number of bedrooms, bathrooms are related.

22:05

If a house is, then number of bedrooms are more, the bathroom too. I'm just saying,

22:11

like, the most important factor is size. Let me give you one example.

22:18

Pollution level of a locality.

22:21

The locality in the locality, it's there price of impact not.

22:26

No, it won't. No, it don't type of settings in India in. There are, you can look at places like

22:33

Gurgao, some of the most expensive real estate in the world.

22:35

There are there, that's not a very, like, clean air. It's a very extremely bad pollution

22:43

levels in that area. That area in that area, it's a little better, but still NCR region, pollution

22:49

is very high. So you've got extremely expensive real estate, but pollution is high. And at the same time,

22:54

you've got, you know, bungalows and villas, let's say comparatively better. If Hyderabad, maybe there's a place

23:01

called Jubilee Hills. That is regarded as, you know,

23:05

the most expensive real estate in India.

23:09

There pollution level come, but prices are more.

23:13

One example. You let's just a rural area. You go.

23:15

Pollution is not, but price be less.

23:19

And you, you know, you another extreme lay.

23:22

City in a city. City in a well-planned neighborhood with a lot of greenery, lot of trees.

23:27

Like, Banglore Airport, Devon Hali, where there, the developers and properties,

23:31

very nice, very nice area, not much pollution, not much traffic, nice place.

23:35

Okay. Pollution is come, but prices are very much. So you've got all the things. So what I'm

23:40

getting at is pollution is not a good predictor of price. Size and amenities are very good

23:46

indicators of the price of the property. But pollution level of a locality is not a good predictor of

23:52

price. It's not that pollution is a price. Are you getting it? So we are basically

23:59

trying to identify which of the features are actually important. If we're not a X's basis

24:04

in this way to predict can we have, so how can't tell you, what feature,

24:12

what's a input actually impacts the output? And this is part of what we are trying to achieve today.

24:18

You can see the other 75 feature was total garbage. Like Color of the Neighbors car. I'm

24:24

here here here, here I'm example. Now, Color of the Neighbors cat, but how to house to do it. You know,

24:30

you know, now, now feature to be a feature. Now, there's a house, there's a house. A lot of some, you can't.

24:34

You're just saying, okay, color of the person's cat,

24:36

that basis, price for the difference.

24:38

So out of 80 features, only five are actually important.

24:42

These are the features like size, number of bedrooms, number of bathrooms,

24:46

locality matter, but the other is 75 important than we are.

24:50

Okay? And you can see, if you try to fit a model,

24:54

if you try to fit a model on all these features,

24:57

which is what I'm trying to do,

24:58

I've a data set simulate here.

25:00

This is a simulation data, and I just wanted to discuss it briefly with you,

25:04

Python in a function called make underscore regression.

25:09

This is a very nice function. I don't want you to memorize it.

25:12

So this is a very nice function that you can use to simulate data.

25:15

If you have a upna put up to make underscore regression can.

25:19

So I've here here here a data simulate here.

25:22

I've here 80 features, 80 features mean feature 1, feature 2, feature 3, all the way to feature 80.

25:28

These features have no definitions as such.

25:31

But I'm just trying to simulate that same exercise for you.

25:34

See, there are 80 features of the house, and based on that, we are trying to predict what is the price of the house.

25:39

Now we're what we're going to do, we're on this data on, we're standard linear regression

25:42

and I want to tell you that how standard linear regression will fail.

25:47

Okay, so let's let's. So we can do a min-max scalar. This is the standard best practice. Always do it.

25:54

Always do. Here, the min-max scale here here here is. Scaling is already mostly scaled data. But,

25:58

it's always a good practice to do scaling. So first you do the train test split. Standard process as last week,

26:03

whatever we talked about.

26:05

That's after we are doing a min-max scaleer and then we are doing a linear regression.

26:08

Now, you you can't manually be can't.

26:10

This thing, this thing are pipeline's as we.

26:12

I taught you pipelines last week, pipelines are easier.

26:15

Because pipeline in the code come to write.

26:17

You can, now, you can't.

26:19

So we are first doing scaling.

26:21

Remember, fit, transform on train and transform on test.

26:24

And here we are building the linear regression model.

26:26

The moment I run this code, you'll be able to see we are getting catastrophic overfitting.

26:30

This is the key challenge that will happen.

26:32

especially in scenarios when you have a lot of, lot of features.

26:37

Here, 80 features are trying to fit a model based on 80 features.

26:42

And that is the reason why the model is tremendously overfitting.

26:45

It's a tremendous amount of overfitting that we are able to see on the screen right now.

26:50

So how can we solve? What can we do about it?

26:52

What is the problem? What is the challenge?

26:55

So for a minute, let us also take a look at the model's brain.

27:00

So the models we've built here here.

27:01

Linear regression. Dot fit, which we have made.

27:02

And this concept we've last week learned here. Whenever you do linear regression,

27:07

you're always learning the value of M and the corresponding value of C.

27:13

You're, you know, right?

27:15

So let us, let us see the models wait right now for a minute. So you can see the models weight's right now.

27:20

So you can see the models weights have become like this.

27:24

Look at how wildly these numbers swing. Some are massively positive and some are massively negative.

27:30

Some are massively negative. Some, some are massively negative. Some, which, good values are positive.

27:32

positive and some values are very low. It's a huge swing. What it means is,

27:39

and this interpretation, we've made last session, weight, what is, weight,

27:42

what's the coefficient. Right? Model. Dot coiff underscore,

27:45

means coefficients, M1x1 plus M2, x2. This is we know that. We know that. We know that.

27:51

It's the matter is that one unit increase in this feature leads to a massive increase in the output.

27:57

But on the other hand, one unit increase in that feature leads to a massive increase in the output. But on the

27:58

other hand, a other hand, one unit increase in that feature leads to a massive reduction

28:03

in the output. And this is overfitting. Overfitting is, that means lots of twists and turns. Your

28:08

model is not stable right now. I mean, there are so many features we have, so much of noise is there. So you can

28:16

actually see, it assigned crazy weights to features that actually don't matter. And the model is memorizing

28:22

the data. So 100% training, the model is overfitting. Basically, it is doing very well on training.

28:28

but it is performing very poorly on testing.

28:30

Or coefficients are also very, very high.

28:32

Just remember, coefficients are extremely high.

28:35

So what do we do in this kind of a scenario?

28:37

In this kind of a scenario, there are two strategies that we have.

28:41

Number one strategy, we have something called ridge regression, which is called L to regularization.

28:48

So most importantly, here we have a term used called regularization.

28:54

Okay?

28:55

Regularization of what?

28:56

So, regularization is basically a very nice way to reduce overfitting in the model.

29:02

Okay? We try to reduce the power of the model. So we use regularization to reduce the power of the model.

29:08

So that is exactly what we are doing right now. You can see all of you.

29:16

Okay, you can see this one.

29:19

So whatever we are seeing right now, linear regression is basically

29:26

Ridge regression would be nothing but linear regression.

29:29

Only thing is that we will penalize the large weights.

29:32

There is a little bit of math around it which you don't have to remember.

29:35

But just remember that all that we are trying to do, we are trying to reduce the power of the model.

29:42

This term is regularization.

29:44

Regularization is a way to reduce the power of the model.

29:47

The model we're going to reduce the power reduce current.

29:51

That is what regularization will do.

29:53

Now, current, the basic model, the linear regression.

29:56

use in, that our weight's coefficient is very much.

30:01

So, so, now we will, we will forcibly shrink the weights of all the features down towards 0.

30:09

Towards zero, exactly zero, not going, smoothing out the crazy swings.

30:14

And how we'll achieve it, we will achieve that using a parameter called alpha.

30:18

So we will vary a parameter called alpha and we will reduce those weights and we will reduce the power of the model.

30:24

And we will reduce the power of the model. And we'll overfitting go come.

30:26

So looking at the code, the code is ridge alpha equal to 0.2.

30:33

As I made here here here, you instantiate here is you instantiate something called ridge.

30:39

And they are both coming from the same package.

30:41

As you go up here, look, here we look, we import care from SK learned linear model,

30:46

import linear regression, comma, ridge, comma, lasso.

30:49

So code is very simple.

30:50

Just in one line in everything will do.

30:52

So linear regression, we already know, two new things we are seen today, ridge or lasso.

30:56

that's the only intuition. Now, moving on, so Jessica, we go ahead and instantiate rich

31:04

equal to this. We will do model.fit and let us train the model, 99% training, 93% testing.

31:12

Instantly, you can see the improvement happening. So what has happened right now, if you compare the

31:16

thing. And most importantly, if you go back and look at the model coefficients, you will start

31:22

to see that ridge has shrank the crazy numbers down. So nobody dominated.

31:26

model. Now, now numbers, now, look. Now, look, the first one feature,

31:30

now, look, look, how it got, 29. The first one, next one feature, 17th,

31:35

now, look, how, how much, six. So it has shrunk it. So it has, so it has basically

31:40

reduced those crazy swings. And most importantly, the ridge has effectively

31:45

effectively ensured, the features important, whichever features are not important,

31:51

their weights are struck down dramatically. And most importantly, it is a regularized.

31:56

technique. So we always do this. Here we're, we'll never do region lasso regression.

32:03

We will usually do this in a scenario where you want to prevent overfitting. If you already have a model

32:08

that is overfitting a lot, you will do regional lasso regression to basically prevent the amount of overputing.

32:13

That is the intuition. So that's the concept why this kind of regression is basically used.

32:21

And very important, if you remember the conversation last week, I told you that overfitting.

32:26

fitting, underfeiting is a very relative concept.

32:30

Koi b model perfectly overfit not.

32:32

Kaui model perfectly underfeit not.

32:35

So overfitting and underfitting is a very relative term.

32:38

Okay, so models are always relatively more overfit and models are always relatively more undercut.

32:43

That's the way to be able to be able to.

32:44

So we will have a relatively more overfit model and we will have a relatively more underfeit model.

32:50

That's the intuition.

32:51

So relative overfitting will happen and relative underfeiting will happen.

32:54

That's the way to look.

32:55

look at the whole thing okay so if you if you compare the numbers right now

33:00

here they put training accuracy was 100% and testing was 85% remember the numbers

33:05

all of you training was 100 testing was 85 so let me if it's easy for you I'll

33:10

try to you know I'll try to use a notepad and show you so iteration one the training

33:18

was the training was this testing was this ticket yeah yeah without uh

33:25

regularization and regulation kind of regulation kind of after number's okay and now you can compare guys

33:30

this is after regularization the numbers have become like this and i'm sure all of you can

33:37

all of you can tell me all of you can all of you will believe me that this is a more good fit model

33:43

he overfit all of you can see this is overfitting and this model after regularization

33:47

regulation means this means reducing the power regularized means reducing the power

33:55

this is the way to remember regularization reducing the power you're regularizing somebody

33:58

that means you're penalizing you know you know up his power reduce

34:02

you're up his overfitting reduce are you so we have made it this model let me write a few

34:08

statements this model is this model is less over fit is less over fit it is less overfit

34:18

okay this model is more good fit though no statement we can't we can't

34:24

is more good fit less overfit because because here

34:28

there training come here testing is better model and this is exactly what we want

34:33

now now now now look at training score come and testing

34:35

we have more good fit model more good fit model is more good fit model

34:39

less overfit model overfitting come here overfitting

34:42

there overfitting quite there train

34:43

was a very test very

34:44

was very come here comparatively the difference in the

34:47

train or test for difference is that

34:48

kind of

34:49

so i mean overfitting component produced

34:52

produced okay but model has become better i think which is obvious because the testing score the

34:57

mock testing score is much higher okay so this is the way how you will compare so theory

35:01

we don't have to get too much into this but what is more important is uh you will have to understand

35:06

the uh the concept the implementation when you're actually doing the labs when you're uh comparing

35:12

seven eight different models you're comparing it's compare kare you that that that thing is something

35:18

everybody should be very very clear with how do we go back and evaluate

35:22

in that context now moving on guys uh let us see this in action

35:34

so i hope everyone's clear uh only thing in rich regression is that

35:39

coefficients to reduce what again coefficient zero not and now level three this

35:45

this level two are rich regression level three is what is called lasso regression

35:49

Lasso regression

35:50

again use called L1 regularization.

35:53

Please remember this all of thing.

35:55

Now, what is the good thing about lasso regression?

35:58

Lasso regression is a good thing

35:59

is a good thing is that here the features are all struck down to zero.

36:04

Here there features, the features are all struck down to zero.

36:09

That is the intuition behind lasso regression.

36:12

That is the idea.

36:13

So code,

36:15

the same to same.

36:17

Code is same.

36:17

Code in the same.

36:19

You can see the code right now.

36:21

Lassau alpha, alpha, alpha, a value we have.

36:24

Same way, dot fit and dot score we did.

36:26

And the interesting part is lasso is even better, even better.

36:30

You're here.

36:31

99% or 93% are.

36:33

Now, here here, look, the testing score 97%

36:35

but.

36:36

I mean, good fit and it's an even better model.

36:40

Excellent generalization.

36:41

And you know the even, the best part about lasso?

36:44

The best part about lasso is when you go and take a look at the coefficients,

36:47

If you, when you will start to realize that most of the coefficients have been struck down to zero.

36:55

Look at the beautiful thing.

36:56

Most of the coefficients are all useless features.

36:59

So that is the reason why Lassow is an even stricter rule.

37:07

So if a feature is useless, I will mathematically crush its weights to zero.

37:14

Ridge was not doing that.

37:15

Ridge was also penalizing.

37:16

Ridge be reduced.

37:17

There was the worst. Here, here's the worst.

37:19

Ridge was saying, okay, I will shrink the numbers.

37:23

I, I, my numbers for shrinker.

37:25

If the feature important not, I will make them spawned.

37:28

But it was not making it zero.

37:30

The features were all there.

37:31

All the Sarii features there were here.

37:33

It was better, but Lassow is even better.

37:35

Lasso says if a feature is not important, I will remove it.

37:38

And that is the reason why Lassau acts as an automatic feature selected.

37:43

It is an automatic feature selected.

37:45

It's better.

37:45

It's very good.

37:46

It's actually very powerful.

37:47

So, when we're linear regression, we're lasso

37:50

we use many times as a default because lasso acts as a very good feature selector.

37:55

So, like you here you have a lasso use, dot fit, score and you will actually start to see

38:00

when you look at the coefficients, most of these features have become like zero.

38:06

Here you head of 15 here you have,

38:08

all, no problem.

38:09

There are 80 features, all do it.

38:11

You can't see here.

38:12

You can't here.

38:13

This is a full display not.

38:14

But you have a display, you have to do that.

38:16

But you get a nice.

38:17

idea, right?

38:18

You get an idea in terms of what's going on here.

38:21

There are 20 features and most of the features you can see.

38:23

You have head, here here here, you look at the tail.

38:26

Most of the features are shrunk to zero.

38:28

Can you see?

38:29

Here here here feature important.

38:31

You know, either features you are important.

38:33

You know, feature number 61 is something.

38:35

This is something.

38:36

This is your number of bedrooms.

38:37

This is number of bathrooms.

38:39

But all the features almost like zero.

38:42

So this is the beautiful thing about Lasso.

38:44

This is the beautiful thing about Lasso regression.

38:46

So you're effectively.

38:47

building a model on lesser number of features.

38:50

Now you're going to, sir,

38:51

feature, feature of coefficient zero,

38:53

so what is the

38:55

so, you know, so what is the thing about it?

38:59

Coefficient zero is what is what?

39:03

Why equal to MX plus C?

39:05

Why equal to MX plus C if you take a look at it?

39:08

If the coefficient is zero, that feature is not even used right?

39:11

That's the way to look at it.

39:13

If a feature coefficient is zero

39:15

then the feature itself is not considered in the equation.

39:17

So that's the way to do that.

39:19

So shake, that is the internal mathematics.

39:20

That is not part of the general discussion.

39:22

So you can ignore that.

39:23

That is the internal mathematics behind how it is happening.

39:26

And that is based on things like gradient descent and other things

39:29

which the curriculum doesn't get into.

39:31

It's under internal math is.

39:33

On its basis, your whole thing derive on.

39:35

In fact, linear regression in the math

39:37

there.

39:38

There are a calculus,

39:39

and all that.

39:41

But that is your implementation in nature.

39:43

That is the internal mathematics of how it's happening.

39:45

So how it's happening.

39:46

So how does Lasso know?

39:47

which features are useless.

39:48

So that is how the mathematics is built behind the scenes.

39:52

So behind the match, behind the scenes,

39:56

there's your gradient descent on that basis

39:59

it is able to figure out.

40:01

Okay, but coming back, summarizing,

40:03

implementation, how will?

40:05

First, you have linear regression.

40:06

First, you see,

40:07

okay, is my model overfitting?

40:09

Is my model underfitting?

40:10

Is my model underfitting?

40:11

As you've seen,

40:12

that you've seen,

40:13

now you decide,

40:15

Now you decide, okay, now we have to reduce the power of the model.

40:20

Now I have to reduce the power of the model.

40:21

Now I have to reduce the overfitting.

40:22

This is the pattern.

40:23

This is the way how approach, okay?

40:25

First, linear regression.

40:26

You see, overfitting is,

40:28

so now you decide, okay, now I have to reduce the power.

40:30

I have to reduce the overfitting.

40:31

If your linear regression is not overfitting,

40:34

okay?

40:39

If your linear regression is not overfitting,

40:41

then what you will do?

40:43

Then you will go back and you will, you will,

40:45

you will not do lasso and rich.

40:47

Then you're tab up regularization

40:49

need to be regularization up

40:50

if your model is overfitting.

40:54

If your model is not overfitting,

40:55

you will not go back and do regularization.

40:58

Okay? So here up here overfitting

40:59

so what you will go back and do?

41:00

You will look at the coefficients,

41:02

the weights and you're able to see the weights are very high.

41:05

Some features are weight is very high.

41:06

Some features are way is very low.

41:08

You're able to see that pattern.

41:10

Next, level two, what are we doing?

41:12

We are doing ridge regression and two regularization.

41:15

So we are doing ridge regression.

41:18

We are doing L2 regularization.

41:20

Then we've seen, what we've seen what in ridge?

41:22

In the ridge in the model has become better.

41:24

Weights have been shrunk a little.

41:26

Kinalize kitchens,

41:26

we've reduced, the model has become better.

41:29

Lasso next level even better.

41:30

Lasso is L1 regularization

41:32

just remember.

41:34

Lasso is even stricter or weights to we're zero greater.

41:38

Even stricter.

41:38

And it's an even better quality model.

41:40

And lasso access what we refer to as feature selection.

41:44

If a feature is not important,

41:45

lots of strikes on its weights all the way to zero.

41:48

That is an important concept to keep in mind.

41:51

Now, just one small thing I want to clarify.

41:54

This particular term that you see on the screen,

41:58

this term we're a hyper parameter katea.

42:01

This is our side contentment in today, but anyways, I'll talk about it.

42:04

This particular term is what is referred to as a hyper parameter.

42:07

What am I, what is the term I'm using?

42:11

This go home hyper parameter kater, okay?

42:15

And the process of tuning this hyperparameter is what is referred to as hyperparameter tuning.

42:21

So some of you might ask me,

42:23

sir, here alpha value we're two legal.

42:26

So, two things.

42:27

First, the first thing, sir, alpha's default value is what is?

42:30

So, if you're here alpha,

42:32

if you can't offer, you know, the interesting part is,

42:35

when you say alpha equal to zero,

42:37

observe the code all of you.

42:39

Same lasso, observe the code all of you very carefully.

42:42

That's why we're saying,

42:43

we're saying, it's in the internal mathematics set.

42:45

which we're not getting into.

42:46

But just remember, when you make alpha equal to zero,

42:49

this will behave exactly like linear regression.

42:53

Yeah, the linear regression.

42:55

So alpha zero,

42:56

that is what is going on behind the scenes.

42:59

Alpha zero,

43:00

there is no regularization.

43:02

Natti top level.

43:03

Alpha equal to zero means there is no regularization.

43:05

And remember, as you increase the value of alpha,

43:09

let me write it down.

43:10

As you increase the alpha,

43:14

as you increase the alpha, as you increase the alpha,

43:15

we, we increase the regularization.

43:21

It is like a tuning knob.

43:24

Like, AC's the remote is, you're increased

43:26

temperature, reduced, the temperature come

43:29

and you're trying to choose what is that right temperature in between.

43:32

This is called the hyperparameter.

43:35

You try different different values

43:36

and you see which value is giving you the highest test accuracy.

43:40

That's the thing.

43:41

Actually, we're doing it.

43:42

Here we're manually not manually not, we're functions like.

43:45

But you'll take alpha equal to zero, then you will take alpha equal to 0.

43:50

So the same very part, alpha point one's what will.

43:52

Alpha point one's said, look, model has become slightly better.

43:55

Sora better was, sort of better than alpha point one's.

43:58

Okay.

43:59

If you're alpha very bad off, then what will?

44:02

On the, on the contrary, if you make it alpha very high,

44:04

alpha copened there, then what will be?

44:06

All the end up end up and then, so there is no regularization.

44:12

This is like complete over-fitting.

44:14

If alpha equal to, then.

44:15

to zero, this is complete over the two.

44:17

And as you increase the alpha, what is happening?

44:20

As you increase the alpha, you increase the regularization.

44:23

That means you, you reduce the power of the model more and more and more.

44:27

As if alpha increase, here here we, if we have alpha to 20, you see what,

44:32

when I make my alpha value equal to 20, very interesting.

44:35

Same thing, everything, all, everything same.

44:37

Now, look, here here training 3% was, testing 3% of.

44:42

You know, guys, what is going on behind the scenes?

44:43

So, it's the matter of this is, that alpha equal to 20.

44:47

I mean, we've got it so regularized.

44:49

Sure, regularize means that if you have a kid at home,

44:55

if you put too many constraints, you know, too many constraints, you cannot do this,

44:59

you cannot do this, he cannot do this, he cannot do this, he cannot do this.

45:00

That will do it?

45:01

There's nothing to do.

45:02

You know, it's like you have tied, its hands and legs,

45:04

that, that's nothing can't be.

45:06

You know, regularization,

45:07

you're controlling, you're putting too many constraints.

45:10

You know, it's power really reduced.

45:12

You know, a free man.

45:13

a free moment, you're free to roam, you know, like, think of it that way.

45:18

You're free to think.

45:19

Now, what you've got, you, you've got it in jail.

45:21

So, what can do you?

45:23

Think of it that way.

45:24

So regularization means you're literally putting somebody in a jail.

45:27

So the alpha is what is, you're using to control how strict that jail is.

45:33

As you increase the alpha, you make your jail more and more strict.

45:36

Alpha go to 20.

45:37

It's like, it's like, it's a very strict jail in downed.

45:41

He can't do.

45:42

He can't.

45:43

or she shackled.

45:44

Hathpire, back, yeah, and you can see the results.

45:49

Like, we have alpha to 20%.

45:50

You can see, you can see, training is 3%, testing is 3%.

45:53

This is a very, very poor quality model.

45:55

I mean, that's not able to.

45:57

How can't see it?

45:57

He can't, it's not can't.

45:59

You've got it's all back to him.

46:00

How will that model even learn?

46:02

It's shackled.

46:03

Half-pire, back, you know, it's intuition are all.

46:08

If I have to go to one level deeper, if you're wondering,

46:10

if you're wondering, sir, what is happening?

46:12

Internally, what is happening?

46:13

is, internally what is happening is, as you increase the alpha a lot, most of your features

46:20

become zero.

46:22

All the features almost zero are the coefficients, basically.

46:26

So, alpha 20, so we've been very extreme area.

46:28

Alpha equal to zero, what is what is?

46:30

There is absolutely no constraint.

46:35

Yeah, this is the other extreme.

46:37

So we are trying to find out the right value of alpha in between.

46:40

What is that right kind of regulation?

46:42

Fuller constraint will.

46:43

Not not, that's not that, but we will go back and try to find out that alpha

46:49

value in between.

46:50

And this process of trying to find that ideal value of alpha is what is referred to as hyperparameter

46:55

theory.

46:56

Okay?

46:57

Now, you'll ask, sir, can, can't, can we this, uh,

47:00

can we, uh, can we, uh, can't, uh, manually do?

47:02

Like we have you seen, one, two, three, four, or so, they're not.

47:05

This we're, we're, we can't a for each loop.

47:08

You've seen a porridge loop. You can run a for each loop, okay?

47:12

And using a porridge loop, okay? And using a porridge loop,

47:13

You can try to print out different, different alphas.

47:17

You're allagal alpha and you can build different, different models, and you can choose the best one.

47:22

So this is the iteratively, you can get out of those, generally speaking.

47:26

Okay?

47:28

But, yeah, but, yeah, it's kind of other methods, functions, which we will see later, not in today's

47:33

session, but this is the general idea.

47:36

So what is the key takeaway?

47:37

We have seen linear, we have seen bridge, which is called L2, we have seen lasso, which is called L1.

47:41

I don't know we are regularizing and

47:45

and generally speaking, yeah,

47:48

I mean, if you're regularize

47:49

so, if you're just a lot more regularize

47:51

you, then Gourtec, accuracy reduce

47:53

as I told you, if you regularize too much,

47:56

accuracy will reduce.

47:57

But if you regularize a little, it's a good thing.

48:00

We've seen, we've seen here here

48:02

here here all right, but you've never

48:04

regularized it, so accuracy burned

48:06

now, so little bit of regularization is good.

48:10

I think the best thing will be,

48:11

if I take you back to my last week's demonstration,

48:15

you're here here here,

48:16

so this is it like alpha equal to zero.

48:21

Think of it that way.

48:23

Everybody remembers this diagram.

48:24

This is alpha equal to zero.

48:27

Alpha equal to zero,

48:28

there is no regularization.

48:29

Overfitting.

48:30

Overfitting.

48:31

No regularization.

48:33

Model is overfitting.

48:34

You're all of constraint not.

48:35

He's anything.

48:35

He is doing it is learning too well.

48:38

It has all the power to learn.

48:40

It is overfitting.

48:41

running two males, memorizing.

48:43

Now, on the other extreme,

48:45

like I've seen

48:46

you demo here,

48:47

you've got a alpha value

48:48

very lot.

48:49

theoretically,

48:50

there's no constraints

48:50

there.

48:51

Alpha value could

48:51

be there.

48:52

So I've here

48:53

here alpha 20 or

48:54

300 or 100

48:54

or whatever is.

48:56

So this is like an

48:56

underfeit model.

48:58

You've seen

48:58

3%, 3%

48:59

down.

49:00

Now you'll

49:00

say,

49:01

3%

49:01

sir,

49:02

it's more be

49:02

more than,

49:02

it will put.

49:03

You know,

49:03

alpha

49:04

100 low,

49:04

1,000

49:05

look,

49:05

check

49:06

code is with you.

49:07

And you will

49:08

start to see that

49:09

this type

49:09

underfitting

49:10

are.

49:11

And you will

49:11

And now you

49:12

say, sir,

49:12

what is, sir,

49:12

what is,

49:13

you're in the

49:15

you will have to find out.

49:16

Or this is the number you will have to find out.

49:18

Here, you

49:19

have you need to

49:19

get out, okay,

49:21

what is that right value of alpha?

49:22

Here there's

49:23

about two

49:23

we're

49:24

okay, we can check

49:25

we can't

49:25

check we are

49:25

we are trying to find out

49:28

what is that

49:28

ideal value of alpha

49:29

where we are

49:30

getting the good fit model.

49:31

And this

49:32

we have to

49:32

machine learning in

49:33

if you look at

49:34

a real world ML project,

49:35

this is all that we are

49:36

trying to do.

49:38

We are trying to find out

49:39

what is the best

49:41

value of alpha and for

49:42

which particular value of alpha

49:44

we are trying to find

49:45

the best big model.

49:46

So that is all that we are trying to do

49:47

in, you know,

49:49

machine learning.

49:49

We are trying to find that

49:50

optimum value of the

49:51

hyperparameter

49:52

for which we have the best model.

49:54

That's what we are trying to

49:55

go back and do.

49:57

Okay?

49:58

Okay,

49:59

okay, all of you.

50:01

I've given a very interesting

50:02

Cagle case study here

50:04

related to the housing prices.

50:06

Something that people can look at.

50:08

I'll give you some time

50:08

a little later in the class

50:10

to

50:11

explore this, but

50:11

this is a very interesting

50:13

data set in.

50:14

So class

50:14

I'm a, you know,

50:16

I'm a sample

50:17

for you know,

50:18

but this is

50:19

the very real world

50:20

housing prices

50:21

regression data set.

50:22

So whatever I created,

50:24

I simulated,

50:25

I'm, we

50:25

did so as si

50:25

featured simulate

50:26

but in case

50:27

some of you are curious

50:28

that, sir,

50:29

this is a real

50:29

data set

50:30

is actually a very nice

50:32

data set.

50:33

And Cagle, this is

50:34

actually a

50:35

live competition.

50:36

So this is a

50:37

Cagle's life competition.

50:38

The very popular

50:39

competition,

50:39

you can already start to see.

50:41

This was a very old competition.

50:42

This is not new.

50:44

And it's an ongoing competition.

50:45

When the Kegel started,

50:46

when it's the competition

50:47

is going to.

50:48

And you can see,

50:49

there are like 900,000

50:50

entrants,

50:51

so

50:51

many people have submitted

50:52

and it's amazing.

50:54

And you're

50:55

so you can see what is the

50:56

data set.

50:58

So what

50:58

things you can do you

50:59

can go to the

51:02

data section.

51:03

You can go to the data section.

51:04

You can see what kind of

51:05

data we have.

51:05

And this is what I was trying to say.

51:07

This is your data

51:07

fields are.

51:09

See?

51:09

Property, sale, price.

51:10

You can you can go

51:10

this is the, this is like the output

51:13

Y, and these are all input access

51:14

are zoning, linear,

51:17

lot size, type of road access,

51:19

type of alley, general shape of property,

51:21

these are all your features.

51:23

Very interesting.

51:24

And you know, the reason I like to

51:26

mention these examples in Kaggle is because

51:28

whatever I show you in the code,

51:30

see, ultimately you have to quote

51:31

you have to ultimately get the practicals done.

51:34

All the theory and all, to some extent,

51:36

just that we're just enough

51:37

we're talking in class in.

51:38

But beyond that, I really,

51:40

I really encourage my students to go

51:42

and do things in the real world.

51:44

So you can use

51:46

some templates.

51:49

You can use some templates. You can use

51:51

all tools use

51:52

and use absolutely fine.

51:55

But what you get is you actually

51:56

get help.

51:58

It's not as if outside the class you

52:01

like, sir, you can't have this big data set

52:02

set up. You can't. You can't.

52:04

You know linear regression

52:05

you know. You know basic

52:07

things, you know,

52:07

how to build a model. How to build a model.

52:10

Accuracy, test accuracy.

52:12

At least a linear regression,

52:13

we know.

52:14

More other things we'll look.

52:15

Other than ML classes are

52:16

more.

52:16

Other than other things we are yet to see.

52:20

Lasso,

52:21

know, rich,

52:21

you know, basic model

52:22

can make good fit, basic

52:23

basic, you know.

52:24

You know scaling,

52:26

you know power transform,

52:27

you know the Min-max scalers.

52:29

Basic things you can do.

52:30

You can do.

52:30

You can go to the

52:33

code section.

52:34

This is the favorite part.

52:35

You can go to the code section.

52:36

Sort by the best kernels

52:37

and here from here you can

52:38

seeks.

52:39

There are some amazing

52:40

solutions that people are posted.

52:42

So some of them might be a little advanced,

52:45

but what you can do is

52:46

here here

52:48

linear regression

52:48

could be,

52:49

because people do

52:50

what do they do

52:50

make

52:51

make sure you can

52:53

actually search.

52:56

You can actually search.

52:56

You can search.

52:56

You want to

52:58

search notebooks

53:00

where they have solved using linear

53:01

regression.

53:02

Okay, so I'm here

53:03

here per

53:03

regularized linear model,

53:05

which is very related to our

53:06

class today.

53:07

So our class is about

53:08

regularization.

53:09

I would say,

53:09

related to the session

53:10

today. This is a very nice thing.

53:12

You see, here here

53:12

there's a great data set for

53:14

lasso.

53:15

Here there's a

53:15

80, 85 features

53:16

have in the data set.

53:18

So real data set

53:18

is.

53:19

So,

53:19

there's a

53:19

already solved

53:20

here.

53:20

So based on this,

53:22

you,

53:22

you know,

53:22

a class

53:22

concept here,

53:23

and

53:24

go and go to

53:24

here

53:24

here in Cagle

53:24

in the,

53:25

so this is the,

53:26

you know,

53:26

this is what I

53:27

encourage you

53:27

to do in the

53:28

upcoming classes also.

53:29

So I will

53:30

share a lot of

53:31

these external

53:31

resources.

53:32

So please go back

53:33

and use

53:34

use them as

53:34

reference.

53:35

Here you can

53:37

see some of these

53:38

external solutions and see

53:39

here here

53:40

then then you

53:40

okay, so

53:41

it's,

53:41

it's so simple, it

53:44

you know, it's so simple.

53:45

Now you have to

53:46

access collab

53:47

guys,

53:47

just one small thing

53:48

you have to

53:49

login

53:49

can't, okay,

53:50

just one thing you'll have to do.

53:51

Mobile number

53:52

verification

53:53

and OTP

53:53

login

53:54

that is the only thing.

53:55

Like you

53:55

can go to any

53:58

uh,

53:58

you can go to any kernel

53:58

and you can just go

54:00

and say copy and

54:00

repeat and

54:00

repeat in collab.

54:01

So your

54:02

collab access already

54:03

so it

54:03

so it's

54:03

so it cangle

54:04

directly will go ahead.

54:05

It says

54:06

open in collab

54:07

so I've made

54:07

so this the

54:08

this one has solved

54:09

is this is a very nice way you can actually, you know, work through it.

54:15

Alexandra Pappi-U.

54:18

Pappy-U.

54:20

You know, they've

54:20

solved

54:20

you.

54:22

You know,

54:22

not very hard.

54:24

Difficult is,

54:24

sale price.

54:26

What is?

54:26

What is?

54:27

Nothing.

54:27

Get dummies,

54:27

are, fill and they are.

54:29

There's no.

54:31

Once you start seeing some of these solutions,

54:33

you will start feeling confidence.

54:35

And confidence is the only thing in the world.

54:36

More,

54:37

nothing.

54:38

Some things you will know.

54:39

some things you will not know, but ultimately you will have confidence.

54:41

Yeah, I mean, we have a Kaggle

54:43

that's a big data set

54:44

that we've got to understand, and that confidence is a deadly thing.

54:48

Okay, so that is, that is the confidence

54:49

I want to instill in the class.

54:51

What I mean?

54:52

Once you learn the basic ideas,

54:54

you're like a solution

54:55

you know, you can't

54:56

you know confidence is that.

54:57

We don't know.

54:58

You know, what is it.

54:59

What is?

55:00

It's trained, you've made CSB

55:01

you've done, trained test you've

55:02

did, you're doing missing value,

55:05

imputation, basic missing value.

55:07

They know what?

55:07

They did, dummy variables create

55:08

here, imputation, missing value

55:10

imputeed that's it.

55:11

And there's nothing.

55:12

And, they go, and they

55:13

go ahead and they made

55:13

model built

55:14

okay?

55:15

Here, here they know

55:15

reed regression

55:16

different, different

55:19

alphas did.

55:20

Now,

55:20

look,

55:20

just that I'm

55:20

we're saying,

55:21

that alpha's

55:22

no, nobody knows.

55:24

Nobody knows.

55:25

Nobody knows.

55:25

We, none of us know

55:26

what is the right

55:27

value of alpha to risk.

55:27

Kis can't know.

55:28

He know,

55:29

he tried different, different

55:30

alphas did.

55:31

List in values

55:32

did,

55:32

and other alpha

55:33

and whichever

55:34

alpha is giving the

55:35

highest test accuracy,

55:36

he chose.

55:38

Okay, so this is

55:38

what is going on behind the scenes.

55:39

You can see.

55:40

Here they've

55:41

there they've been lasso

55:41

and in lasso

55:42

in a lot of

55:43

different alphas

55:43

strike here

55:44

and he's

55:44

finally selecting

55:46

what is the

55:46

best model.

55:47

This is

55:47

other things

55:48

like Z boost

55:48

we have not

55:49

discussed here.

55:50

So you can

55:50

actually look at

55:51

these kinds of

55:52

solutions actually.

55:53

So the code

55:54

was only like what,

55:55

hardly if you

55:55

lines,

55:56

if you look like

55:56

similar to

55:57

what we have

55:58

done.

55:58

It's not very

55:58

difficult, right?

56:00

So,

56:01

so what is the

56:02

key takeaway?

56:03

Lassow is a feature

56:03

selector.

56:04

When you

56:04

laso

56:05

we have

56:05

two things

56:07

we have

56:07

seen.

56:08

tuning, you have to find the right value of alpha.

56:12

If you increase alpha, you are regularizing the model.

56:15

You're regularize

56:15

correct.

56:17

So,

56:18

uh, or lasso say benefit

56:19

what is the benefit of lasso?

56:21

It acts as a kind of a feature selector.

56:23

If you, uh, you know, you can, you can basically take a certain value of alpha.

56:27

You can do lasso regression and it acts as a kind of a feature selector.

56:31

The unimportant features are struck down to zero.

56:34

The weights and coefficients of the unimportant features are all struck down to zero.

56:38

And the model becomes more robust.

56:42

That is the important thing to keep in mind.

56:45

All right.

56:46

So I hope everyone's clear.

56:48

I've given another very nice external resource sample for you.

56:51

Medical cost personal data sets.

56:53

This is a very interesting use case and I just wanted to take a,

56:56

you know,

56:57

minute to talk about it.

56:59

India in it's insurance.

57:00

I'm sure many of you in this class,

57:02

you would have taken automobile insurance.

57:05

You have two wheelers,

57:06

you're going to insurance.

57:08

how it's how much, $700, $800, $700, $700, $400,000, $4 wheeler car

57:14

can do it depends on the year of registration.

57:16

It will be $4,000,000.

57:18

So India is static.

57:20

If you're third party comprehensive,

57:22

if insurance are you, it's a static value.

57:25

They will ask you,

57:26

Bari can make-all model, what year-of-registration

57:28

what is, owner what, that's it.

57:31

And based on that, there are some buckets.

57:33

That's a bucket basis of pricing

57:34

and premium.

57:37

Same for health insurance.

57:38

If you want to buy health insurance, they will ask you,

57:41

what is your age, what is your medical condition,

57:43

so your rules are you?

57:47

But are we really doing machine learning?

57:50

Are we really machine learning?

57:52

Are we really predicting what is the premium based on your factors?

57:58

And that is an amazing application.

58:00

That is the application that we are talking about right now.

58:03

So how do we predict,

58:05

how do we predict the insurance premium?

58:08

How do we predict the insurance premium?

58:14

Okay, medical cost, personal data set up.

58:16

You can see what we are trying to do.

58:23

How do we predict the insurance premium?

58:25

Based on the age of the person, the sex, the BMI, the number of children,

58:30

this is the bachia.

58:31

That's a factor over.

58:32

If your more a child, then maybe, I don't know, like,

58:36

age factor will, because if your age is high risk factor,

58:38

more than male, female, so I don't think there's any studies there.

58:44

So it's the same probabilities of diseases.

58:47

BMI obviously is a factor.

58:48

If your body mass index is a lot, so obesity is a factor.

58:52

So BMI is an important, you know, indicator of health.

58:55

If your BMI barred jae, then risk more.

58:57

Okay.

59:08

much more if you have more children, you know, because you have to provide for them.

59:11

So those are all very subtle factors that insurance companies will look at.

59:15

Are you a smoker or non-smoker?

59:16

Smoker, so obviously, your probability of cardiovascular risk, health, you know, risk

59:24

increases, cancer risk increases.

59:28

And finally, region matters.

59:29

On where's where from the country or which part of the country or which part of the world you're from?

59:35

And this is a very interesting, you know, case study.

59:38

you know, if you're a global insurance company

59:43

is, you know, imagine you're a global insurance company serving customers from across the world.

59:49

You will naturally see that people in the northern hemisphere are healthier.

59:53

This is, now, northern hemisphere is what?

59:56

If you're you're not, if you're northern hemisphere, what is northern hemisphere?

59:59

Where you're going to USA, Canada, all the whole Europe are.

1:0:02

And Russia is actually quite developed.

1:0:05

So now, whatever is war is a different thing, but Russia is actually quite developed.

1:0:08

compare Russia with it. And so that's why we call it, you know, there is a term that

1:0:13

is used called the global south. And the other hand, you've got southern hemisphere.

1:0:17

East are, west are, okay. If you look at the insurance company, what will see? If you look at

1:0:21

a insurance company, that what will be? If you're north from, if you're east from, if you're

1:0:27

south-east Asia, maybe your probability of health risk is much higher. But if you're

1:0:33

probably from a different part of the world, maybe your probability of health risk is going. Again,

1:0:37

that, that's a different thing. But what I'm getting at is, how can we use

1:0:48

data science to predict a person's premium?

1:0:52

It's not that you've been application to bring to 32. And India in India may, India in India

1:0:58

made, this model not, because India may be government regulations. There are all the model not. Because

1:1:01

India may be government regulations. I, RDII, they have everything, they have everything, they have

1:1:06

insurance regulatory development authority of India that is the main

1:1:11

regulatory body that is managing all insurance schemes in the country. So there's a lot of

1:1:19

regulation involved in that. But I think it will be a great, great use case. I'm sure

1:1:23

wrong of you agree. So can we look at the historical data? Can we build a model?

1:1:29

I mean, it's a kind of, it's a kind of a kind of. I'm just trying to help you with the framing.

1:1:35

And this is what I'm looking forward to.

1:1:38

This is what you need to do.

1:1:41

See, problems, approach is all same.

1:1:45

Nothing. I'm sure you guys are already doing classes.

1:1:48

You're doing exercises also in the, when I'm not with you, you're having the T Session.

1:1:53

You're all in classes in exercises.

1:1:55

And you're already realizing the approach is the same.

1:1:58

Approach is the same.

1:1:59

The data is the same.

1:2:00

The train test rate.

1:2:01

We're doing model.

1:2:03

So the approach is the same.

1:2:04

Nothing changes.

1:2:05

Now, the approach is the same.

1:2:05

The only thing is, can you frame the problem?

1:2:07

Do you have the vision that you, you

1:2:09

have the vision, that you

1:2:10

understand the domain, and can you frame the problem?

1:2:14

And believe it or not, this is the kind of make or break thing

1:2:16

that happens in interviews also.

1:2:18

Because in interview in the interview in linear regression,

1:2:19

so all know, dot-fittance,

1:2:22

all know know,

1:2:22

train test, all know, lasauris, all know.

1:2:26

There is no rocket science about what I taught you today.

1:2:28

Absolutely no rocket science.

1:2:30

But what is the rocket science?

1:2:31

What is the differentiates you from 100,000 people is,

1:2:34

can you, let's say, your insurance is Tata AIG with.

1:2:39

Okay, Tata AIGC can't, you have?

1:2:43

Can you go there.

1:2:43

You know, this problem, sataq, so, I mean, you know, can be predicted.

1:2:48

You can be able to say.

1:2:49

Maybe not everybody will think about it.

1:2:51

That's just the question of the job gave, 99% of the other people.

1:2:55

But can you frame the problem?

1:2:58

That, yeah, this is the problem in the insurance sector.

1:3:01

This is the problem in the health sector.

1:3:03

So, sir, we can this can solve.

1:3:04

we can use machine learning to solve it.

1:3:07

So whenever you're going next for any company interview or you're planning for any interview,

1:3:12

always think, you, that company, in, that context, we can't use

1:3:17

to make, make, ML use to, that context.

1:3:18

That context, we can't generate a LLMC use.

1:3:21

Obviously, when we come to those topics later on.

1:3:23

Okay?

1:3:24

Anyways, so the big picture idea would be, obviously, we will take the data, we will build the model exactly

1:3:29

as I told you, why as a function of X, we will build a model.

1:3:32

And next time, we will use that model for doing the regular.

1:3:34

Those steps are model training and model prediction.

1:3:37

So next time we have a new person who, you know, who wants to take insurance, who

1:3:43

will have their details, how he has, who's how much worker, or not,,,,,,,,,,,,,,,,,,,,

1:3:50

where, they're age, how is, what, their pre-existing diseases, how much, based on all those

1:3:54

factors, the model will calculate what is the person's premium that the person has to pay.

1:3:59

And I think you will agree this is going to be more accurate, because if your, if your risk factors

1:4:04

a lot more than you have to be. Obviously, it should be. But actually,

1:4:08

now, actually, that's not. You know, the funny thing about the health insurance sector in our

1:4:13

country is, you are also 32. Let's see, your friend is also 32. Do you, don't know, two, two

1:4:18

two are two years. You are a very healthy person. But that's, of the health is bad. But there

1:4:24

are no metrics that we actually have to evaluate. Don't know same premium there are. Actually,

1:4:30

and coverage will be made. So it's a little flawed, actually. But there are a lot of improvements,

1:4:34

we can potentially make. Now, if you if you're, uh, automobile insurance

1:4:39

in driving, you know, vehicle insurance, two-wheeler, four-wheeler,

1:4:44

that's, now, now, not everybody drives the same way, right? But everybody spent the same insurance.

1:4:51

Ideally, what should be? People who are at the highest risk of accidents,

1:4:57

who are unsaved drivers, who are, who are good driving, who, they, who are more money

1:5:00

need to be. But this are some great potential avenues that we have.

1:5:08

Let's move on, guys. This is again from a use case perspective. The larger solutioning will

1:5:13

remain the same. What he, X, and the up, and you can up on, you can't see how we are

1:5:17

solutions to. Okay. Now, next part of our discussion, we are moving into evaluation metrics.

1:5:30

I just, I just wanted one thing, you have to remember that, that ridges, uh, L2 and

1:5:40

and excuse me, lasso is L1. He can just keep this at the back of your mind.

1:5:45

Ridge, L2, it's, L2, it's, but you just keep this at the back of your mind. Now, we are entering

1:5:53

into another, you know, very, very interesting conversation around evaluation metrics. So the next phase

1:6:00

that we are entering into. And what are the different, different types of evaluation metrics?

1:6:04

This even we've made to formalize the discussion. And I try to formally introduce some of

1:6:10

these, some of these evaluation metrics for you. What these evaluation metrics really are.

1:6:15

So let us see that. Let us see that. I think here is a nice diagram that I wanted to kind of show

1:6:20

you to, again, pictorially help you understand all that we discussed today. So when you do not

1:6:25

regularize a model, it becomes somewhat like this. This is something like this. This is a

1:6:29

I already shared with you. So, if you're not regularize not, if it's

1:6:33

control not. Regularize, I mean control. If you're not, if you control

1:6:37

if you're not, then what happens? So, the model tries to open, will overfeit.

1:6:43

Bucca who, but it's like that. But if you regularize it, it becomes more controlled. The

1:6:49

process becomes more controlled. This is what it is. This is the general idea. This is what

1:6:54

you're trying to achieve. A jada regularize it, then they'll learn not. But you have to achieve. But you have to

1:6:58

achieve the optimal amount of regularization and how we're how we achieve

1:7:02

using the alpha hyperparameter okay?

1:7:04

We're all the other values and we're doing it. Just this

1:7:07

just this. You know, guys, L2 is rich. L2 is rich and L1 is lassoe. Just remember.

1:7:14

Okay. Now. Now,

1:7:16

Chal, moving on. Now let's come to different types of evaluation metrics.

1:7:22

So we have all been using the score function to see how well the model

1:7:27

captured the mathematical pattern.

1:7:29

We've scored to

1:7:30

have the same time.

1:7:31

We've got dot score, dot score

1:7:33

did. Now the concept is,

1:7:36

now the concept is, now

1:7:36

the dot score is what?

1:7:38

Intuitively, again, not

1:7:39

mathematical.

1:7:40

Mathematics may

1:7:41

it's not the intent of the class

1:7:43

or the curriculum,

1:7:44

but intuitively what is the meaning

1:7:46

of dot score?

1:7:47

What dot score is

1:7:48

what are

1:7:50

some of these other

1:7:51

evaluation metrics that we have?

1:7:53

Specifically, we'll

1:7:54

talk about M.A.E.

1:7:56

We will talk about

1:7:57

something called RMAC.

1:7:59

I'll take you to our content also.

1:8:01

We'll specifically talk about MAE.

1:8:03

We'll talk about RMAC.

1:8:05

And we'll talk about RMAC.

1:8:07

So these are three specific

1:8:08

evaluation metrics

1:8:10

that I will be discussing right now.

1:8:12

That is what we'll see.

1:8:14

Now,

1:8:15

you guys want to take a short break and come back?

1:8:19

That would be good.

1:8:21

Yeah. So we can take a

1:8:22

yeah, we can take a short break.

1:8:27

Okay, five minutes, we can take a break.

1:8:31

Guys.

1:8:46

And by the way, guys, all these contents are in the 25th May folder.

1:8:47

As I always do before the classes,

1:8:50

it is all part of the 25th May folder.

1:8:53

A core thing here,

1:8:54

which I haven't come to, that is going to be a small.

1:8:57

case study, that will be the last thing of today.

1:9:01

So this is our over will go in the next five minute, you know, half an hour or so.

1:9:05

We'll keep a little bit of time for a small case study.

1:9:07

So we'll end uprolet, so we'll end uproats in, okay?

1:9:10

Yeah. So but these are the contents generally for today.

1:9:12

You can access them from the 25th May folder.

1:9:15

I will see you back after five minutes.

1:9:27

Thank you.

1:9:57

Thank you.

1:10:27

Thank you.

1:10:57

Thank you.

1:11:27

Thank you.

1:11:57

Thank you.

1:12:27

Thank you.

1:12:57

Thank you

1:13:27

Thank you

1:13:57

Thank you

1:14:27

Okay.

1:14:34

Welcome back.

1:14:35

Welcome back.

1:14:36

Let us continue on.

1:14:57

Okay. So. All right, we'll continue on. So we are just about to discuss the different types of evaluation metrics.

1:15:07

So, so first we will talk about we will talk about these three metrics, M-A-E, R-M-M-M-A-C and R-square.

1:15:14

What these things are. So as I told you, dot score is something we have already been using for a long time.

1:15:20

Dot score. And this dot score is the dot score is, what the dot score is.

1:15:25

So all this while I've been explaining, that dot score is a kind of an accuracy.

1:15:31

That is just a general term we have been using in the classes so far.

1:15:36

We can correct that a little.

1:15:38

Yeah, dot score is a way to calculate how accurate the model is.

1:15:43

You have the model fit and you and you dot score did, and that's accuracy you know

1:15:49

that is what dot score will tell you.

1:15:51

Dot score will tell you on an average how accurate the model is.

1:15:55

So, I mean 85% score is what is giving you 0.85 score? What is the meaning of 0.85 score?

1:16:05

What is the meaning of 0.85 score?

1:16:09

This is the meaning of 0.85 score?

1:16:10

This is, generally, what it means is it means 85% of the time, on an average, you are able to predict correctly, intuitively.

1:16:22

Look, look. Regression in what are we trying to do?

1:16:27

If you remember the conversation, let me use my pen.

1:16:30

Very intuitively, what are we trying to do?

1:16:34

We have a lot of X and we have Y here.

1:16:37

We have a lot of data points.

1:16:39

These are all the data points we have right now.

1:16:43

And you are trying to find the best fit line.

1:16:45

I'm best fit line, basically.

1:16:47

Now if you think about it intuitively,

1:16:49

this line is that will never pass through all the

1:16:52

the points, this all the points will not pass it.

1:16:54

Right?

1:16:55

The line will never pass through all the points.

1:16:57

As we already discussed.

1:16:58

The line will never pass through all the points, as we already discussed.

1:17:03

Right? The line will never pass through all the points as we already discussed.

1:17:07

Now.

1:17:10

So, how accurate is it?

1:17:13

Now, how accurate is it?

1:17:15

Now, what is the accuracy of parameter?

1:17:16

When we are 85% score, dot score, then 0.85 by a test accuracy.

1:17:21

Test accuracy.

1:17:22

code for test accuracy, 85% bias.

1:17:25

This is that this line, based on the X,

1:17:31

what is the Y is, how accurately we are able to predict the Y?

1:17:37

Okay?

1:17:38

Sometimes the Y is very far away.

1:17:40

Sometimes the predicted is very far away.

1:17:42

Sometimes the predicted is very close.

1:17:44

Sometimes it's on the line.

1:17:46

Sometimes the perfect prediction is

1:17:48

very different.

1:17:49

Residuals are very different.

1:17:50

Residuals on the right.

1:17:51

Actuals predicted.

1:17:52

So that is what this score is kind of telling you.

1:17:55

This basis, a mathematical formula, which in our content in just list out here,

1:17:59

and we'll show that you don't have to get deep into it.

1:18:02

But the intuition is important.

1:18:03

Next time, 85% is it.

1:18:05

That's why I've been using the term accuracy on this file.

1:18:07

Because of accuracy is it?

1:18:09

Conceptually, if you understand how accurate is it?

1:18:13

How accurate is your best fit line?

1:18:15

So those best fit line, 85% of the time you're able to correctly predict.

1:18:20

The rest of 15% the residue also very different.

1:18:22

Incompan that way.

1:18:22

Now, remember, we also talked about the fact that the inverse of accuracy is what is called error.

1:18:30

So, and further I want to add one more thing.

1:18:35

This score is basically nothing but R squared.

1:18:39

This is the term that we are technically using in our content also.

1:18:45

So this is the R squared we have defined R squared more formally here.

1:18:50

This we have R squared here defined defined.

1:18:53

So R squared 85% means the model explains 85% of why the scores spread above and below the average.

1:19:03

So it's a little technically but what it means is how accurately you're able to explain the X from the Y's.

1:19:09

And R squared, it's generally the higher it is the better it is overall.

1:19:14

And R squared is the score basically.

1:19:17

R squared is basically the score accuracy.

1:19:19

Think of it that way.

1:19:20

So how much variation does the model explain?

1:19:23

So this is your R squared mathematical formula which you don't have to get into.

1:19:27

But I just wanted to show you.

1:19:28

So there is a certain way it is getting derived.

1:19:30

And intuitively, the higher the value, the better it is.

1:19:34

Keep that at the back of your mind, okay?

1:19:36

But don't have to memorize the formula at all.

1:19:38

But just remember, whatever we were calculating all this while, dot score, dot score,

1:19:41

what we are doing.

1:19:43

Because you go, you will, whenever it's a regression model, you will always do dot score.

1:19:48

You will get something called art square.

1:19:49

get something called R squared. So this is what that R squared is.

1:19:52

But, but classification model for remember, this is,

1:19:55

that R squared not, we're not going to.

1:19:57

So classification we are entering into from, I think, from next session only

1:20:01

our classification on taking it.

1:20:03

But this is only for regression what we are discussing.

1:20:05

So dot score is giving you the R squared.

1:20:08

And what is the inverse of, what is the inverse of accuracy?

1:20:13

What is the inverse of this?

1:20:15

The inverse of this is the error.

1:20:17

So you have two types of errors.

1:20:18

There are two different errors. We have

1:20:20

a model which is, let's say, 90% accurate.

1:20:24

If you have a model that's 90% accurate,

1:20:27

it's, it's a 10% error will.

1:20:29

conceptually that's the way.

1:20:31

If you have a model that's 100% accurate,

1:20:34

that there's no error in it.

1:20:36

What error is it?

1:20:37

If there is a model that is 100% accurate,

1:20:40

that model will give you 0% error.

1:20:42

If a model is 95% accurate, that model will give you 5% error.

1:20:47

So the more the accurate,

1:20:48

the lower the quantum of error.

1:20:50

The more accuracy will,

1:20:52

that's the way to look at it overall.

1:20:54

That's the intuition.

1:20:56

So that is the way to look at it.

1:20:58

That's what we are basically talking about.

1:21:00

Okay.

1:21:01

So there are two types of errors we have.

1:21:04

It's on this,

1:21:06

up, this and on this, behind a bit of match.

1:21:08

If you want to see, I'm

1:21:10

a formula here here but you don't have to

1:21:12

memorize it in detail.

1:21:13

So there are two types of errors.

1:21:15

M.A.E and R.M.M.A.S.

1:21:18

And again, I'm repeating, don't get confused.

1:21:20

Practical, real world, we will generally stick to dots four.

1:21:25

The workflow we have been discussing all this fine.

1:21:28

Data loget, train test plates we will do.

1:21:30

We will do dot fit and we will do dots four.

1:21:32

Usually that's what you will do.

1:21:34

Okay?

1:21:35

Error is used only for interpretation purpose.

1:21:39

This only interpretation for purpose for use what you are.

1:21:42

That's the only way to look at it.

1:21:44

Just keep this back of your mind on a few.

1:21:46

Okay?

1:21:47

Now.

1:21:48

So, what are the, what are the different errors? Let us see this. Let us talk about this.

1:21:55

What is, what is M-A-E and what is R-M-A-C?

1:21:58

So first I will start out writing a couple of formulas.

1:22:03

Just a second.

1:22:06

You got disconnected.

1:22:08

Maybe a second data.

1:22:18

That's complete. Okay.

1:22:48

Just give me one minute guys. I had the other monitor that got disconnected.

1:22:56

If it comes back up, just give me a minute.

1:22:58

In the meantime, you can take a minute.

1:23:01

I am already sharing my screen.

1:23:03

Just take a minute and re-through it in the meantime.

1:23:05

Let's try to connect back my other monitor.

1:23:07

Let's give me one minute, please.

1:23:18

In the meantime, all of you just read through the definitions, okay?

1:23:28

Just read through the definitions.

1:23:30

Pretty self-explanatory.

1:23:32

You can you understand what it's not at all difficult.

1:23:35

But I'll explain it anyways, okay?

1:23:37

Just go through it once. I'll explain any ways.

1:23:48

So, um, okay, perfect.

1:24:18

So MAE basically stands for, let me just take a minute to write it down.

1:24:27

M&E, just with a formula for what M&E basically stands for.

1:24:32

This is what I mean absolute error, because you've already read out here

1:24:36

right?

1:24:37

And what is not given here is the formula.

1:24:39

Because the formula actually is no,

1:24:40

but I'm just trying to explain this in intuitive way.

1:24:42

Because if we're not going to tell you,

1:24:44

you can't this is what you can't

1:24:45

this is what is the absolute difference,

1:24:47

what is.

1:24:48

all be like, you know, rocket sign. So let me, it's a very simple formula. Okay. And,

1:24:52

it's not needed, but it's, it'll be useful for you to understand the rest of the stuff.

1:24:58

Okay? So let's see this. Now, first we calculate the error. Error

1:25:02

what kind of what is. Error is what is residual. If you remember, we

1:25:06

have error last session in discussed. First, you fit the best fit line on your data, and then you

1:25:12

find out the difference between the actual value and the predicted value. Or what's the difference

1:25:17

say actual or predicted in between, that we're

1:25:19

error kept. So first you calculate the error,

1:25:22

then we find out the absolute value of the error, and then we take the mean of the

1:25:29

end of the mean of the absolute values. That is how we find out mean absolute error.

1:25:35

So first we calculate what is the error. I repeat again, first we calculate what is the error,

1:25:40

number one. Number two, we find out what is the absolute value of the error.

1:25:47

we find out what is the absolute value of the error.

1:25:51

And we find out the mean of the absolute value.

1:25:55

So,

1:25:57

if we're intuitively you're going to,

1:26:00

let me just do this for a minute.

1:26:02

This is your x or your y is.

1:26:04

This is your data points.

1:26:06

So you have,

1:26:08

x, y,

1:26:09

combination, whatever story for regression we have discussed all this point.

1:26:12

So this is from the last class, what we talked about.

1:26:14

So

1:26:16

If you have the best fit line

1:26:18

you have two things,

1:26:20

let me use a different color.

1:26:22

You have actual value,

1:26:24

and here you have you have predicted value.

1:26:26

We already discussed this.

1:26:28

This is a residual.

1:26:29

So actual minus predicted is called a residual.

1:26:32

So if you're this data point,

1:26:34

then its residual here.

1:26:35

If you are this data point that

1:26:37

the residual is this is this is

1:26:38

residual here.

1:26:39

This is the residual here,

1:26:40

this are all the different,

1:26:43

different residuals that you have, right.

1:26:45

Now all that we have,

1:26:46

we are trying to do is we are trying to find out all these residuals.

1:26:49

Now, you see how we're

1:26:50

see how we can

1:26:52

how we can't.

1:26:54

So we're not going to

1:26:55

we're not.

1:26:56

These are all errors.

1:26:57

So how we'll take.

1:26:58

So,

1:26:59

so we're actually.

1:27:00

So y,

1:27:01

actual minus y predicted.

1:27:04

So we'll

1:27:06

one or any point

1:27:07

actual minus predicted

1:27:09

then we take the absolute value of it.

1:27:12

Now you will say, sir,

1:27:13

absolute Q

1:27:14

what are?

1:27:15

Absolute is what is?

1:27:16

is like modulus. You know, if you know in match, there is a,

1:27:19

a,

1:27:20

an operator is modulus.

1:27:22

Modulus,

1:27:23

if you're,

1:27:24

if you're,

1:27:25

typically given like this,

1:27:27

bracket,

1:27:28

you know,

1:27:30

so the positive value of,

1:27:33

that 5 will.

1:27:34

But if you're modulo of minus 5

1:27:36

then,

1:27:37

that what will be,

1:27:38

that what will be,

1:27:39

Python in

1:27:40

in a modular operator,

1:27:41

you know,

1:27:42

you know,

1:27:43

if it's modulo of positive value,

1:27:44

it will give you the value itself.

1:27:46

If this module of the negative value,

1:27:48

it will return only the positive part out of it.

1:27:51

And it is important,

1:27:53

because if you are the residuals

1:27:54

look,

1:27:55

some residuals are,

1:27:56

some residuals are negative,

1:27:58

but we don't know that

1:27:59

we don't know

1:28:00

we don't know

1:28:01

we don't know,

1:28:02

we don't know

1:28:03

we

1:28:04

that's what

1:28:05

error is

1:28:06

that

1:28:07

error is positive or

1:28:08

or is not our concern.

1:28:10

So we

1:28:11

we'll make

1:28:12

we'll make

1:28:13

,

1:28:14

we'll make,

1:28:15

we're going to calculate is

1:28:16

what is

1:28:17

magnitude of error

1:28:18

how is

1:28:19

it,

1:28:20

that's

1:28:21

positive direction or

1:28:22

or negative in

1:28:23

not my concern.

1:28:24

How much is,

1:28:25

what is the magnitude

1:28:26

of the error?

1:28:27

Now,

1:28:28

look,

1:28:29

there are absolute value

1:28:30

and then

1:28:31

we'll make

1:28:32

i equal to

1:28:33

summation and divide by

1:28:34

end.

1:28:35

All the points

1:28:36

add and

1:28:37

average over.

1:28:38

That is the way how we

1:28:39

calculate the MAE.

1:28:41

Okay,

1:28:42

so basically

1:28:43

I wanted to keep the expression

1:28:45

simple, so if you

1:28:46

if you're

1:28:47

if you're

1:28:48

if you're

1:28:49

here

1:28:50

and I equal to 1 to

1:28:51

1 to n

1:28:52

we're

1:28:53

So mathematically

1:28:54

the expression looks like this

1:28:55

you know

1:28:56

again it's not to scare you

1:28:58

but

1:28:59

just wanted to complete the story

1:29:00

so I just wanted to

1:29:02

complete the story

1:29:03

this is how the whole story adds up

1:29:06

so Y actual

1:29:07

YP2

1:29:10

plus dot or not

1:29:12

all the way you're adding up all the

1:29:14

point divide by n

1:29:15

So you're taking one of these points,

1:29:18

that's

1:29:19

actual minus predicted

1:29:20

What is?

1:29:21

Absolutely,

1:29:22

next point

1:29:23

actual minus predicted

1:29:24

what is

1:29:25

absolute value

1:29:26

you keep adding them divide by n

1:29:27

or that is what gives you

1:29:28

mean absolute error

1:29:29

and this is what the official definition is

1:29:31

it is the average

1:29:33

of the absolute differences

1:29:35

between actual and predicted.

1:29:37

So you can

1:29:38

you

1:29:39

I think this is exactly what we discussed here.

1:29:42

Okay guys,

1:29:43

everyone's with me.

1:29:44

one's with me.

1:29:45

Everyone's with me.

1:29:46

Can you give me a small yes on chat?

1:29:48

Everyone's okay.

1:29:50

I went into a bit of maths to explain, but I hope everyone's clear.

1:29:53

Do let me know, guys.

1:29:55

You know, guys.

1:29:56

See, the match is not difficult.

1:29:58

If you, if you directly

1:29:59

formula,

1:30:00

you'll, then it's hard.

1:30:01

But the way I explained,

1:30:03

first error,

1:30:04

then absolute, then mean.

1:30:08

Like, calculate.

1:30:09

And,

1:30:10

look,

1:30:11

you know,

1:30:12

So first you,

1:30:13

you're error

1:30:14

then

1:30:15

it's absolute value

1:30:16

then it's a mean

1:30:17

that is what MAE stands for.

1:30:19

It is a definition of error.

1:30:21

Now we will tell me, sir,

1:30:23

now you will tell me, sir,

1:30:24

now,

1:30:25

that's what I'm telling you.

1:30:27

In a regular machine learning workflow

1:30:28

work flow,

1:30:29

you're just

1:30:30

just to

1:30:31

where it is getting used,

1:30:33

I will talk about it,

1:30:34

but from a practical model building perspective,

1:30:37

dot score,

1:30:38

to our discussion.

1:30:40

You're dot fit

1:30:41

and dot score.

1:30:42

Just,

1:30:43

score's more,

1:30:44

the model is,

1:30:45

score come up,

1:30:46

the model is

1:30:47

then you

1:30:48

asked, sir,

1:30:49

error,

1:30:50

Phil,

1:30:51

let's talk about it.

1:30:52

Error is used to interpret the model.

1:30:55

You have a model

1:30:56

made

1:30:57

85% error are you,

1:30:59

but sorry,

1:31:00

85% is the score.

1:31:01

So it will give you

1:31:02

approximately 15% error.

1:31:04

So

1:31:06

it is used to interpret the model.

1:31:09

The end user,

1:31:10

the customer is,

1:31:11

customer is,

1:31:12

he's got to

1:31:13

that model in

1:31:14

that

1:31:15

customer is

1:31:16

dot score

1:31:17

not

1:31:18

doesn't know

1:31:19

that

1:31:20

accuracy not

1:31:21

that

1:31:22

business term

1:31:23

that

1:31:24

model in

1:31:25

how you

1:31:26

if you

1:31:27

if you

1:31:28

real

1:31:29

world

1:31:29

analogies

1:31:30

so

1:31:31

say

1:31:32

take into

1:31:34

the

1:31:34

suigi

1:31:35

you, you

1:31:36

ordered

1:31:37

so you said

1:31:41

a beautiful regression problem. They are looking at the different

1:31:44

factors and they are trying to predict how much of time,

1:31:48

just give you one second guys.

1:32:11

Okay.

1:32:14

Um,

1:32:15

Okay.

1:32:22

Um,

1:32:23

Sorry.

1:32:26

So,

1:32:43

if you look at Swiggy,

1:32:44

what is Swiggy doing?

1:32:46

Swigy is

1:32:47

you are

1:32:48

what

1:32:49

they're

1:32:50

looking at

1:32:51

traffic conditions

1:32:52

and

1:32:53

whether

1:32:54

and

1:32:55

based on that it is

1:32:56

looking at the available

1:32:57

delivery agents

1:32:58

and that

1:32:59

that's all

1:33:00

account

1:33:01

that's trying to predict

1:33:02

estimated time of delivery.

1:33:03

But he usually is very accurate.

1:33:04

He's

1:33:05

he's very accurate

1:33:06

that he's

1:33:07

accurate about how he's

1:33:08

taking time in preparing,

1:33:09

how time

1:33:10

taking

1:33:11

that time to reach

1:33:12

it.

1:33:13

It's actually a very interesting

1:33:14

regression problem, by the way, we think about it.

1:33:17

Now,

1:33:18

Mano Sriki's regression model.

1:33:19

Okay,

1:33:20

the new order placed

1:33:21

you were,

1:33:22

you have a app in

1:33:23

and the model is predicting

1:33:24

how much time it takes to deliver.

1:33:26

That model

1:33:28

certain accuracy

1:33:29

but

1:33:31

what,

1:33:32

we're customers to

1:33:33

what

1:33:34

we can't,

1:33:35

that

1:33:36

you know,

1:33:37

you said,

1:33:38

order in 20 minutes

1:33:40

for,

1:33:41

five minute delay,

1:33:42

that is the meaning of

1:33:44

how far is, how different are the actuals from the predicted?

1:33:49

So, a delivery app is off by 4.5 minutes on average across 100 orders.

1:33:56

That is MAE.

1:33:57

I'm right.

1:33:59

Now,

1:33:59

both places are

1:34:01

now, you're

1:34:02

if you say,

1:34:03

Swigie has predicted it,

1:34:04

20 minutes in,

1:34:05

that will be in 15 minutes in,

1:34:06

that's bad.

1:34:07

Maybe you are outside.

1:34:09

Oftentimes, what people do is,

1:34:11

who,

1:34:11

office at home home

1:34:12

and then they order.

1:34:13

you're,

1:34:14

you know,

1:34:15

it's going to be

1:34:15

20 minutes

1:34:16

and he'll be

1:34:16

that's also bad.

1:34:19

That is also bad.

1:34:21

Error

1:34:22

to have,

1:34:22

model predicted

1:34:24

something actual is

1:34:25

five minutes.

1:34:27

Error is there.

1:34:28

And on the other hand,

1:34:29

the model

1:34:30

predicted

1:34:30

a 20 minute,

1:34:31

but he came

1:34:32

30 minutes.

1:34:32

That was error.

1:34:34

So we are trying to

1:34:35

understand on an average

1:34:36

how

1:34:36

different are the actuals

1:34:39

from the predicted

1:34:40

on an average,

1:34:42

on an absolute terms.

1:34:43

So this end users for

1:34:45

to understand

1:34:46

so let's say

1:34:47

you're

1:34:48

presenting

1:34:49

you're presenting

1:34:51

you are trying to

1:34:52

explain to them

1:34:52

how well your

1:34:53

application is doing,

1:34:54

how well your

1:34:55

predictions are doing.

1:34:56

So M&E can be

1:34:57

a very nice

1:34:57

metric you can go back and use.

1:35:00

Okay, so

1:35:00

key takeaway, so you can see.

1:35:03

And stakeholders

1:35:04

want a plain language

1:35:05

numbers.

1:35:05

Stakeholders,

1:35:06

means for customers.

1:35:07

Customers for

1:35:07

for customers for

1:35:07

for customers for

1:35:08

to understand.

1:35:10

On an average,

1:35:10

how different are the actual

1:35:11

from the predicted?

1:35:12

How different are?

1:35:13

How different?

1:35:13

So model building

1:35:15

for dot score R squared

1:35:17

we use

1:35:17

can't,

1:35:18

but model

1:35:19

interpretation

1:35:20

when you want to

1:35:21

interpret a model,

1:35:22

we use,

1:35:23

we prefer using

1:35:23

these kinds of error

1:35:24

metrics.

1:35:27

Okay, is it okay?

1:35:27

I'll talk about RMAC,

1:35:29

but I took a lot of time

1:35:30

to cover this,

1:35:30

but just wanted to clarify.

1:35:31

People are okay,

1:35:32

I've just got only three

1:35:33

responses.

1:35:34

Others are all fine.

1:35:36

The mathematics you

1:35:37

understood,

1:35:39

what is the intuition you understood?

1:35:40

Please let me know

1:35:41

with a quick yes on chat guys.

1:35:42

if you all follow this part,

1:35:45

you know?

1:35:47

And for that matter, anything,

1:35:48

if you've talked about so many things so far,

1:35:50

so just let me know.

1:35:51

Everyone's good.

1:35:55

Always good to hear some yeses.

1:35:56

So, you know, it feels like I'm talking to

1:35:58

all of you. Yeah, just just keep

1:36:01

the engagement alive guys, okay?

1:36:03

Yeah, yeah.

1:36:04

All of you, let me know, please.

1:36:07

Thank you. Thank you, others.

1:36:08

Thank you. Thank you to each one of you responding.

1:36:10

Good some time to respond.

1:36:12

Others, come on guys, 10 seconds, I want to know from everybody.

1:36:18

You know, you know, you know, I will, I will explain again.

1:36:22

Do not worry.

1:36:23

You know, please let me know.

1:36:29

Somebody has been written in Cuban Day.

1:36:31

What is that?

1:36:33

Um, uh,

1:36:34

I can see a lot of people are pinging in the host and panelist section as well, actually.

1:36:51

Okay, okay, okay, to be a lot of people, most of the people are pinged already.

1:36:55

Okay, ch'allo, no problem. Great. And it's great to know that everyone has followed.

1:36:58

So now, moving on, moving on. Now we will see RMAC.

1:37:04

RMAC is also a kind of an error metric.

1:37:06

This is a kind of error and concept is the same.

1:37:11

Now, what is RMAC?

1:37:12

Exactly, let us see that.

1:37:15

Again, you know, you know,

1:37:16

formula a little bit more than to

1:37:19

then, then, then, it's, I mean, it's,

1:37:20

you mean, here here actually,

1:37:21

a half dooddh drawed there. But I think you need to know the formula

1:37:23

to understand RMAC what is happening.

1:37:26

So let us see that.

1:37:28

So I will write down RMAC for you.

1:37:30

Root mean,

1:37:31

square, square.

1:37:34

error. So first we calculate the error. Then we square the error. Then we take the mean of the square error. Then we take the root of it. That is RMSC point. Okay. So error is nothing but actual minus predicted. So error is nothing but. So what is error? Error is nothing but. Why actual minus why predicted? Then we square the error. Then we take the mean of the squared error.

1:38:04

Then we take the mean of the square error.

1:38:09

There, there is the mean of the square error that we have.

1:38:15

And then we take the root of it.

1:38:23

This is your RMASC.

1:38:24

Looks like a very complicated formula.

1:38:27

But if you just follow the general pattern right now of here, it's very similar.

1:38:32

So the first, error, error is nothing but.

1:38:34

Same story. You have data points.

1:38:38

Same thing you can relate to.

1:38:40

You have got to. You have got to the data points.

1:38:41

You have the first regression line drawed.

1:38:44

Regression line in respect, you have actual minus predicted errors.

1:38:49

You will have the difference between, you know, actual and predicted. Errors will be there, right?

1:38:53

What is the errors?

1:38:55

So error is nothing but actual minus predicted.

1:38:58

First, error calculate it.

1:39:00

Then then, square, then, then, then, then, it's square, then, then, out of the mean,

1:39:03

all the errors you have, you mean to, you square errors can mean.

1:39:08

This is the biggest difference.

1:39:09

Here we're absolute here we're, here we're squared here we're squared.

1:39:13

That is the biggest difference.

1:39:14

And then we're rooted.

1:39:16

Okay?

1:39:18

This is the difference is what are.

1:39:19

So, like, the part same is.

1:39:21

The interpretation is very, very similar.

1:39:23

But I would say, you can see that it is very much like M-A-E,

1:39:28

it is very much like M-A-E, but large mistakes count more than small.

1:39:33

once. So this is kind of better. It is kind of better.

1:39:36

Because if the mistake is more, if the residuals are more, if the difference between

1:39:43

actual and predicted is more, so if you're if you're square kind of better, then, so value

1:39:48

or a more better would. So that is the good thing about RMSC. So RMASE tends to penalize

1:39:56

bigger mistakes. So just keep this at the back of your mind. Otherwise, don't know interpretation

1:40:01

same.

1:40:03

just a little bit of theory that we have here.

1:40:05

Don't know, the interpretation same.

1:40:06

But in practice, in practice, we're prefered.

1:40:10

If you ask me, sir, what is it that we prefer using in practice?

1:40:13

We're, we, we're in real world in what use we?

1:40:15

We're usually RMS use them.

1:40:17

And we'll we'll try it in it.

1:40:19

Thus, formulas, there, functions, all that is useless.

1:40:23

Now that you know the concept,

1:40:26

that error, square, mean, root,

1:40:29

you can't know it in NAMPi in.

1:40:31

you have model

1:40:32

done, dot fit

1:40:34

dot predict

1:40:35

and predictions

1:40:36

are, actual manas

1:40:38

predicted

1:40:38

and that square

1:40:39

and it's

1:40:40

made,

1:40:40

it's a main

1:40:40

and the root

1:40:41

you can actually

1:40:42

calculate RMAC

1:40:43

right using

1:40:43

NNP

1:40:44

it's a simple function

1:40:45

you can use.

1:40:46

I will teach you that

1:40:47

and I will also

1:40:48

teach you the function

1:40:48

that's the

1:40:49

Python's function

1:40:50

we'll

1:40:51

both we'll

1:40:51

let me

1:40:51

let's see.

1:40:52

Okay, but to summarize the conversation,

1:40:56

, 85% accuracy,

1:40:57

your score is your score

1:40:58

that tells you the R squared,

1:40:59

how accurate is the model,

1:41:01

which corresponds to 15% error.

1:41:03

The more accurate the model,

1:41:05

the more the score of the model,

1:41:06

the lower the error of the model.

1:41:08

The model's score,

1:41:08

the better

1:41:09

the more accurate the model,

1:41:11

the more it's scored,

1:41:12

the lower the error.

1:41:13

The lower the mistakes will do.

1:41:15

So that's the way to kind of look at it.

1:41:17

Overall.

1:41:22

Okay. So now, uh, let us move on.

1:41:42

Now let's get going and we'll see our small implementation here.

1:41:47

We'll see a small implementation.

1:41:52

Evaluation metrics, whatever we talked about here,

1:41:54

these are the evaluation metrics for you,

1:41:55

all if you can take a look at it.

1:41:57

So, now we've

1:41:57

what we've done.

1:41:58

So until here, we have taken the data,

1:42:01

we have built a model.

1:42:02

We'll same thing here.

1:42:04

We'll show the dot score

1:42:04

we'll already discussed here.

1:42:07

What is the meaning of dot score?

1:42:08

And now I will show you what is

1:42:10

how to calculate RMAC.

1:42:13

So this is mean absolute error

1:42:14

kind of function is.

1:42:15

So very simple.

1:42:17

You know, here we've imported here.

1:42:19

There is a function called

1:42:20

mean absolute error.

1:42:21

Similarly,

1:42:22

there is a function called, you know,

1:42:24

so you're your main squared error

1:42:26

to be function.

1:42:28

So mean absolute error

1:42:29

and root mean squared

1:42:31

kind of function is.

1:42:32

So this is everything.

1:42:33

You know,

1:42:33

it's all right.

1:42:34

You know,

1:42:36

the function is.

1:42:36

Now that we know the concept,

1:42:38

you know the concept,

1:42:38

you know, the function fall

1:42:39

and two things are you

1:42:40

are your, so

1:42:41

so nothing can't.

1:42:42

Okay, very simple.

1:42:43

You can see this one.

1:42:45

We can import

1:42:45

we can import

1:42:45

okay, and you can

1:42:47

scroll all the way down.

1:42:49

And you can see

1:42:50

that,

1:42:51

first,

1:42:52

do, I've taken my data, I have built the model.

1:42:55

We've made the model.

1:42:55

We've made the model.

1:42:55

We've done dot fit already here

1:42:58

here on, we've got

1:42:59

score already here

1:43:00

here

1:43:00

and we are doing

1:43:02

predict.

1:43:03

We are doing

1:43:03

dot predict and

1:43:04

we are calculating the

1:43:05

predicted values.

1:43:06

And now we can see

1:43:07

that what is the

1:43:08

mean absolute value

1:43:09

epsilon?

1:43:10

Actual minus predicted.

1:43:11

So here here

1:43:12

your MAE

1:43:12

will be.

1:43:13

So you can say

1:43:14

on an average

1:43:15

we are this much

1:43:16

from the actuals.

1:43:18

Okay, so

1:43:18

this is your simple

1:43:19

calculation

1:43:20

here.

1:43:22

Okay.

1:43:22

So you're your

1:43:24

linear regression

1:43:25

and this

1:43:26

your lasso regression

1:43:27

migration

1:43:27

is

1:43:27

intuitively.

1:43:29

Okay?

1:43:29

So you,

1:43:29

you're

1:43:30

manually

1:43:30

be

1:43:31

if you're

1:43:32

saying

1:43:33

that sir,

1:43:34

manually

1:43:34

do we're,

1:43:35

okay,

1:43:35

we're

1:43:35

okay,

1:43:36

we're going to,

1:43:37

you want to try out,

1:43:38

no problem.

1:43:40

Why test?

1:43:40

In fact,

1:43:41

in fact,

1:43:41

it can be an

1:43:42

exercise for you.

1:43:43

I've

1:43:43

I want people to

1:43:45

we have enough

1:43:46

time today,

1:43:47

I want people to

1:43:48

because it is a basic

1:43:49

basic Python exercise.

1:43:50

Okay.

1:43:51

So what

1:43:52

you have to do.

1:43:53

This

1:43:53

we'll

1:43:54

we'll

1:43:55

comment

1:43:55

will

1:43:55

make the

1:43:55

call

1:43:56

we

1:43:56

will

1:43:58

not use

1:43:59

AI.

1:44:00

So I

1:44:01

want you to

1:44:01

go

1:44:01

and

1:44:02

do the

1:44:03

calculate

1:44:05

the

1:44:05

calculate the

1:44:05

mean

1:44:09

absolute

1:44:13

error

1:44:13

mean

1:44:16

absolute error

1:44:17

using

1:44:18

raw

1:44:21

using

1:44:22

basic

1:44:23

numphi

1:44:25

fai and

1:44:27

Python functions.

1:44:27

that's it.

1:44:30

This is what you will have to do.

1:44:32

Try

1:44:33

try to guys.

1:44:34

Try it.

1:44:34

Here here

1:44:35

there's just

1:44:35

just

1:44:36

formula

1:44:37

you already import

1:44:38

something and you are just

1:44:39

applying it.

1:44:40

But now you will have to use

1:44:41

that learning that I taught you.

1:44:43

MIAE is basically

1:44:45

let me

1:44:46

let me ping this to all of you.

1:44:47

This is what you will be required to do.

1:44:49

Okay?

1:44:49

I'm expecting

1:44:50

people to try it out and you can bring me on chat what what what you did.

1:44:54

Okay, yeah.

1:44:56

Please try it by yourself.

1:44:57

Don't use AI.

1:44:58

AI, AI

1:44:59

but don't use that.

1:45:01

I genuinely want you to think,

1:45:04

think through it and try.

1:45:05

Okay, think through it and try.

1:45:08

Enough.

1:45:09

So M-A-E, error.

1:45:11

Actual managed predicted.

1:45:13

Then after,

1:45:13

it's absolute value

1:45:15

and then then it's mean-term.

1:45:17

That's it.

1:45:18

That is what you will have to calculate.

1:45:20

Now, you have to

1:45:25

think it's a little bit of the mind

1:45:26

how to Python

1:45:27

in absolute value modules.

1:45:28

But it's very simple

1:45:30

I can give you a small hint.

1:45:32

In NAMPi, there is a function

1:45:33

called NP.abS.

1:45:34

I can give you a small hint.

1:45:36

You can use np.abS to calculate absolute value

1:45:39

in Python.

1:45:40

So just a small hint for everybody.

1:45:44

Take two minutes, everybody

1:45:45

and please calculate the errors for me.

1:45:50

You know,

1:46:20

Thank you.

1:46:50

Thank you.

1:46:52

Thank you.

1:46:54

Thank you.

1:46:56

Thank you.

1:47:26

Right anybody.

1:47:40

Anybody, anybody,

1:47:42

step by step, I can, I can help you a little,

1:47:44

step by step, I can help you a little.

1:47:46

Step by step, everybody can do it.

1:47:48

So first step, what do you do?

1:47:52

What do?

1:47:53

First step is what?

1:47:54

First step is what?

1:47:55

First step is why test?

1:47:56

Actual minus predicted.

1:47:58

How do we?

1:47:59

Actual is this,

1:48:01

or predicted is nothing but

1:48:02

Freds underscore lasso.

1:48:05

This is your predicted value.

1:48:06

This your predictions,

1:48:07

what are.

1:48:08

Lassau regression, the predictions

1:48:09

are,

1:48:10

we're we're storing,

1:48:11

we're storing,

1:48:11

we're not predicting.

1:48:12

This is your predictions.

1:48:14

Okay?

1:48:15

So this is,

1:48:16

if you do this,

1:48:16

it will give you an array

1:48:17

which will give you

1:48:18

actual minus predicted

1:48:19

difference.

1:48:21

Okay,

1:48:21

and this is your NAMPai array,

1:48:23

okay?

1:48:25

So what you can do now?

1:48:26

This is the first step I've done for you,

1:48:28

difference, error.

1:48:30

Now,

1:48:31

error of the absolute value,

1:48:32

okay?

1:48:32

so how do you find out the absolute value?

1:48:34

Now,

1:48:35

now now, now,

1:48:35

np. abs,

1:48:36

you can do np.abs on this.

1:48:41

If you do np.abs,

1:48:42

you will get the absolute value.

1:48:44

Now,

1:48:44

look,

1:48:45

all negative signs positive

1:48:46

is positive.

1:48:48

And now, finally,

1:48:49

this will give you an array,

1:48:51

or this

1:48:52

up what I will do?

1:48:53

I will do np.

1:48:54

M.P.D.

1:48:54

mean on this.

1:48:55

That's it.

1:48:56

Okay?

1:48:58

Simple.

1:48:58

You can this can manually

1:48:59

be can.

1:49:00

And your answer

1:49:02

how it's coming out

1:49:04

to be 20.37.

1:49:05

And you'll be able to see

1:49:06

very interesting.

1:49:08

This answer 20.37

1:49:09

is exactly what we calculated here.

1:49:11

Same thing.

1:49:12

Same thing.

1:49:12

No difference.

1:49:14

So if you,

1:49:14

we're,

1:49:15

we're here

1:49:17

back back and

1:49:18

if you're like,

1:49:20

if you're like,

1:49:21

this function

1:49:22

use and you will get the

1:49:23

exact same answer.

1:49:24

We'll cool same to same,

1:49:25

right down to the last

1:49:26

this one place.

1:49:27

Now,

1:49:27

look,

1:49:27

we have manually

1:49:28

and we've

1:49:29

done the

1:49:30

same answer.

1:49:32

So the concept of

1:49:33

error is very important.

1:49:34

Now,

1:49:34

how you can't

1:49:34

calculate

1:49:34

that is not important,

1:49:36

but the concept of error

1:49:37

is very important.

1:49:38

What is it?

1:49:40

Okay?

1:49:41

Everyone is okay.

1:49:43

Let me know, please.

1:49:43

Let me know on chat.

1:49:45

All of you understood.

1:49:47

We've made it

1:49:47

manually did,

1:49:48

mean absolute error,

1:49:50

what it is.

1:49:52

Everyone is okay.

1:49:53

And what is the difference

1:49:54

between M-A-E or R-M-M-M-A-C?

1:49:56

RMSC in what we, RMASC, we're square

1:49:58

if a particular error is very high,

1:50:02

that gets more weightage.

1:50:04

That we magnify

1:50:05

kind of.

1:50:08

So both are errors in a way.

1:50:12

It's not absolutely

1:50:14

absolutely required, but just wanted to

1:50:15

additionally show you what, how to calculate this thing.

1:50:21

Okay,

1:50:22

next up, we have the concept of the pipeline.

1:50:26

Now, we have talked about pipelines in the last class I showed you at a basic level.

1:50:30

But you can see, we can see,

1:50:31

we're all the whole thing we can bring in pipeline

1:50:33

in the last demo

1:50:35

we made a few sales back, what I was doing.

1:50:38

First, we had data

1:50:39

trained test split.

1:50:41

We are first doing Minmax scalar.

1:50:43

Min max scalar.

1:50:43

We're first scaling

1:50:44

and then we've got to go and

1:50:46

lastow ridge here.

1:50:48

Okay, so first step was we are doing minmax

1:50:49

and second step was we are doing ridge, lasso, whatever.

1:50:53

But what you can now do is you can actually define a pipeline.

1:50:56

You have a pipeline define

1:50:57

and that's the pipeline

1:50:58

in the first

1:50:59

you have min-max caler

1:51:00

for you,

1:51:00

that's right.

1:51:02

You can instantiate a pipeline

1:51:03

in that pipeline

1:51:04

first you do

1:51:05

you know,

1:51:06

a min-max scalar

1:51:07

then you go back and do

1:51:08

lasso

1:51:08

alpha equal to

1:51:09

this thing.

1:51:10

So that's the way

1:51:11

how you can incorporate

1:51:12

this thing.

1:51:12

So this is a

1:51:13

pipeline

1:51:13

can be able.

1:51:14

So first you go

1:51:15

and do

1:51:15

min-max scalar

1:51:16

second,

1:51:17

you go back

1:51:17

and do this thing.

1:51:20

Okay,

1:51:20

so industry

1:51:21

pipeline

1:51:21

dot fit

1:51:22

X-Train

1:51:23

comma

1:51:23

Y frame.

1:51:24

Okay?

1:51:25

So we are

1:51:26

simply using that pipeline,

1:51:29

so pipeline

1:51:29

we can make the same to same.

1:51:32

Your code

1:51:32

no difference

1:51:33

no difference to same.

1:51:35

Everything will be the same.

1:51:36

You can here

1:51:36

alpha value two

1:51:37

but you

1:51:38

can see that

1:51:38

can't be exactly the same.

1:51:39

Now, you

1:51:40

see,

1:51:40

if we took alpha

1:51:42

equal to two,

1:51:43

we got 96%

1:51:44

97%

1:51:45

we had manually

1:51:46

done manually

1:51:46

right?

1:51:48

Yeah, we

1:51:48

had manually

1:51:48

I got

1:51:50

96, 97 and

1:51:51

even when I

1:51:52

use a pipeline,

1:51:53

I use a pipeline,

1:51:54

I'm waiting the same

1:51:55

answers.

1:51:56

The only difference is the code looks a lot cleaner.

1:51:59

This is the very practical way

1:52:00

how you will do things in the real world.

1:52:02

And the best part about pipeline is that

1:52:04

you're here on

1:52:05

where you can't

1:52:05

if you go back to our

1:52:09

conversations we did

1:52:10

in the prior session.

1:52:11

I'm a lot

1:52:12

a lot of things discussed

1:52:13

I'm a simple imputeer

1:52:14

discussed here.

1:52:15

We've made one hot end coder

1:52:16

discussed here,

1:52:17

get dummies,

1:52:18

label encoder.

1:52:19

We talked about

1:52:20

power transformer.

1:52:22

We talked about

1:52:22

what mean max scalar,

1:52:23

scaling a kind of

1:52:24

so there are so many

1:52:25

different types of free

1:52:26

processing techniques you have.

1:52:27

And you can actually have

1:52:28

multiple pre-processing techniques here.

1:52:31

And this is we take the

1:52:33

original data,

1:52:34

raw data, we put it through multiple pre-processing steps.

1:52:38

We're pre-processed, scale

1:52:39

and we import

1:52:41

we do all of that

1:52:42

and it's end to make model

1:52:44

and we do all of that.

1:52:44

And these things we can

1:52:45

in pipeline in because it makes it very easy

1:52:48

to elect you.

1:52:50

So now we will finally go to the

1:52:52

final case study of the class.

1:52:55

This is what I was

1:52:56

trying to talk about the case study today.

1:52:58

So we'll see a beautiful case study

1:53:00

where we will consider,

1:53:02

you know,

1:53:02

the California housing kind of a data set.

1:53:05

So here we'll consider

1:53:07

and we will see a,

1:53:08

you know,

1:53:09

a very interesting use case

1:53:10

that here on how your lasso

1:53:13

and bridge regression is getting used.

1:53:15

Just to give you a little bit of context

1:53:17

about the California housing data set.

1:53:19

I want people to just

1:53:21

take a minute and read through it once.

1:53:26

I think I might have mentioned this in brief before,

1:53:30

but today we will actually solve it using region lasso.

1:53:34

This is the California housing prices data.

1:53:36

So everyone can take a couple of minutes to just go to Kaggle,

1:53:40

go to the link and see if you are comfortable with this data set.

1:53:43

Just give it a read once, all of you.

1:53:45

Then I will take you through the solution.

1:53:47

You don't have to solve it.

1:53:48

The solution is already given in the drive link.

1:53:50

So you can just go through the dataset,

1:53:53

then I will take you through it.

1:53:55

Okay.

1:53:56

Everybody take five minutes to go through this, please.

1:54:01

Take five minutes, all of it, please.

1:54:26

Thank you.

1:54:56

Thank you.

1:55:26

Thank you.

1:55:56

Thank you.

1:56:26

Thank you.

1:56:56

Thank you.

1:57:26

So everyone's everyone's gone through it.

1:57:28

Just going to give it just going to give it a minute here.

1:57:56

Thank you.

1:58:26

Thank you.

1:58:56

Thank you.

1:59:26

Thank you.

1:59:56

Thank you.

2:0:26

Okay.

2:0:30

Okay.

2:0:31

So,

2:0:32

California,

2:0:33

again,

2:0:34

it's a

2:0:35

again,

2:0:50

it's a different

2:0:52

we are looking at the different

2:0:53

the different

2:0:54

of the different features of

2:0:55

of a particular district and we are trying to predict what is the

2:0:59

median housing value of the district.

2:1:02

So these are different features of the district we have,

2:1:05

total rooms, latitude, longitude, age, population, bedrooms and all that.

2:1:09

And based on that, we are trying to estimate what is the, you know, the median housing value in the district.

2:1:15

That is what we are trying to predict overall.

2:1:18

So that's the particular problem that we are trying to solve.

2:1:23

Okay?

2:1:24

Okay. All right. So now let's go back to the data set, the problem statement, the exercise. Sorry. So we will, we will take the data here, fetch California housing. It's a, this is the pre-built function that we are using. And what will this do? This will actually go and fetch the entire California housing data as a data frame. If you want to take a look at it, let me show you how, what this code will do behind the scenes. This code will actually fetch

2:1:54

the California housing data as a data frame. And this is how you'll be able to see this. You can see this one. You know, you can, again, format this in a better way. But you can see the data, the housing value, all that has been captured. Okay? The exact same data set, which I showed you, this data has been captured. So all the fields and all the columns are there. This is the pre-built data set that we are using.

2:2:19

Next, what we do? We specify what is the X and what is the Y. Just like the machine.

2:2:24

learning concept we specify what is the x and what is the y so x is nothing but the data and y is nothing

2:2:29

but the target so this is how we have specified uh specifically what is the x and what is the y

2:2:36

okay next up what is so um so what is the next thing that we are uh you know going and doing

2:2:45

so uh next thing we are going ahead and using a very very interesting thing called polynomial features

2:2:52

and this is a slightly different thing that we are doing right now. I'll give you a very basic idea

2:2:57

because here we're simulation for right. If you if you California housing data

2:3:00

look this is only nine features. You have basically

2:3:05

we, we're, we're going on. There are eight features we have. The original data set has

2:3:12

20,000640 rows and there are total eight features. That's it. Now we are what we are

2:3:20

what we are using a function called polynomial features and we are creating complex

2:3:26

combinations of features. Mathematics in polynomials what are.

2:3:32

you have x1 x2. X1 into x2 x2 x1 x2 x2 x2 x2 x2 x2 into x3 x3 x3 into x4 x4

2:3:40

x4 square into x5 these are all polynomials

2:3:44

you are trying to combine different different different variables in different

2:3:50

different ways and you're creating a new feature.

2:3:53

We're here we're just we're similate

2:3:56

Now, now,

2:3:57

you know, you have three features have, you have

2:3:59

age, room, there, income, you have three

2:4:01

you have multiplied and a feature

2:4:02

made that we're

2:4:04

we're here randomly

2:4:05

do that's it. You don't have to enter into the

2:4:09

details and how it's happening, but this is the big picture idea.

2:4:12

Now you can you ask us how we're doing

2:4:14

why we're doing? Because I

2:4:17

I want to tell you, I want to

2:4:17

you want to tell you that

2:4:18

original data in

2:4:19

eight features, which are

2:4:21

I am trying to simulate

2:4:24

and I am trying to create a massive

2:4:26

data set of 164 features for you.

2:4:30

And we're on this basis to

2:4:31

you'll tell you,

2:4:33

same thing that we have discussed

2:4:34

all through the class in linear

2:4:35

and lasso regression today.

2:4:38

Now we have been

2:4:39

164 features been

2:4:40

we have taken the original

2:4:44

set of features.

2:4:45

We have

2:4:45

a lot of permutation combinations

2:4:47

here, we have

2:4:48

other other features

2:4:49

made it.

2:4:50

There are some of

2:4:51

some of the features

2:4:51

that's no

2:4:52

mean

2:4:52

is like if I

2:4:54

ask you

2:4:54

if I ask you

2:4:54

that age into

2:4:55

rooms into

2:4:56

income

2:4:56

can

2:4:56

what does

2:4:58

the feature

2:4:58

mean?

2:4:58

No.

2:4:59

There are

2:4:59

a lot of

2:4:59

features we

2:5:00

have created that

2:5:00

don't make

2:5:01

any sense.

2:5:03

So

2:5:03

we have

2:5:05

created are too

2:5:06

many

2:5:06

unnecessary

2:5:07

features.

2:5:09

We have

2:5:10

simulate

2:5:10

to simulate

2:5:10

for

2:5:10

here.

2:5:12

And we

2:5:12

we're

2:5:13

we're

2:5:13

going to

2:5:13

I will

2:5:15

demonstrate

2:5:16

overfitting

2:5:16

and then

2:5:18

then we'll

2:5:18

then we'll

2:5:18

will see

2:5:21

that we'll see

2:5:21

that

2:5:21

laso regression

2:5:22

from

2:5:22

unimportant features

2:5:23

can't

2:5:23

yeah,

2:5:24

yeah,

2:5:24

good question

2:5:25

actually

2:5:25

they're

2:5:26

but since you

2:5:27

ask the

2:5:27

question

2:5:28

degree three

2:5:28

means

2:5:29

degree three

2:5:29

polynomial

2:5:30

is

2:5:30

you

2:5:30

mean you're

2:5:31

so you're

2:5:32

okay

2:5:33

so

2:5:33

this is you

2:5:34

are like

2:5:34

degree three

2:5:35

is

2:5:35

so age

2:5:37

into rooms

2:5:37

into

2:5:37

income

2:5:38

that x1 into x2

2:5:39

into x3

2:5:39

degree three

2:5:40

is

2:5:40

so age

2:5:42

cube

2:5:42

degree three

2:5:42

would

2:5:43

if you

2:5:43

if you are only

2:5:43

if you are only

2:5:45

only combining

2:5:45

two variables

2:5:46

or

2:5:47

then you

2:5:47

that's the

2:5:47

variable

2:5:47

of the square

2:5:48

you have

2:5:48

you

2:5:48

have been

2:5:51

either

2:5:51

it could be either

2:5:51

yeah

2:5:53

so

2:5:54

so

2:5:54

we're

2:5:54

three

2:5:55

can't

2:5:56

if you

2:5:58

if you're

2:5:59

if you

2:5:59

if you're

2:5:59

if you're

2:6:00

if you can't

2:6:03

answer

2:6:04

you have seen features

2:6:06

so we're

2:6:07

just to answer

2:6:08

just to answer your

2:6:09

question

2:6:09

it's not required

2:6:10

others can ignore it

2:6:11

not required,

2:6:12

just to answer

2:6:12

Gourthek's question

2:6:13

on taking this up, okay?

2:6:14

So

2:6:14

Gourthegh is just for you

2:6:15

if you.

2:6:16

If you

2:6:16

if you're here

2:6:17

here on degree three

2:6:17

then what

2:6:18

what are?

2:6:19

What are the

2:6:21

additional features

2:6:21

that are getting

2:6:22

created?

2:6:23

I'll tell you

2:6:23

so

2:6:23

X1 Q

2:6:25

so

2:6:26

so

2:6:26

degree three

2:6:27

what is

2:6:28

you are

2:6:29

creating

2:6:29

all

2:6:30

possible

2:6:31

permutation

2:6:31

combinations of features

2:6:32

until degree

2:6:33

one be

2:6:34

is

2:6:34

two be

2:6:35

being done right, two be

2:6:35

and three

2:6:35

is just keep that

2:6:36

in the back of your mind

2:6:37

okay

2:6:37

so

2:6:38

so what are

2:6:39

so that is

2:6:39

I'm

2:6:40

I'm

2:6:40

squared

2:6:40

square

2:6:40

are

2:6:40

x2

2:6:42

square

2:6:42

are

2:6:42

X1

2:6:45

here

2:6:45

this

2:6:46

all

2:6:46

degree

2:6:47

two

2:6:47

got

2:6:47

Okay, you're okay until here.

2:6:50

X1 square

2:6:51

and I'm sorry

2:6:54

I missed out X3 square

2:6:55

I'm sorry I missed out X3 square

2:6:55

X3 square

2:6:59

actually

2:7:00

you have

2:7:00

three

2:7:01

pieces

2:7:01

so it

2:7:02

will

2:7:02

it's

2:7:02

there

2:7:03

but I think

2:7:05

you're

2:7:05

getting

2:7:05

it's old

2:7:05

then

2:7:06

then you're getting

2:7:07

your

2:7:07

X1, X2

2:7:08

okay

2:7:10

X1 X2

2:7:11

then

2:7:12

then

2:7:13

then

2:7:13

then

2:7:14

then

2:7:16

X2 X2

2:7:17

X3

2:7:17

these

2:7:18

these

2:7:18

all

2:7:18

degree

2:7:19

two

2:7:19

to

2:7:20

end

2:7:20

degree two means

2:7:21

mathematically

2:7:22

mathematically

2:7:22

degree two

2:7:22

means the

2:7:23

highest power is too

2:7:24

these

2:7:25

are all features that are getting created.

2:7:27

Now X1, X2, X3 are like age,

2:7:30

age, rooms and income.

2:7:31

This is the features

2:7:32

mean,

2:7:33

but when you're

2:7:34

combining

2:7:35

you're making some features

2:7:35

like age square,

2:7:37

income square,

2:7:38

this has no

2:7:38

that is what I'm

2:7:40

trying to simulate right now.

2:7:41

We're 164 features

2:7:43

want to

2:7:43

show these are

2:7:45

useless features actually.

2:7:47

Okay, so

2:7:48

degree two

2:7:48

means you're treating

2:7:49

you're treating all

2:7:51

degree one features.

2:7:52

These are degree one features.

2:7:54

These are all degree

2:7:54

degree

2:7:55

two features and

2:7:57

these are

2:7:59

these degree three features.

2:8:02

Good,

2:8:02

okay,

2:8:03

question answer,

2:8:04

there's

2:8:05

your question answer,

2:8:05

you know?

2:8:06

Okay,

2:8:06

and

2:8:07

one more add

2:8:08

a more add

2:8:08

your degree

2:8:09

zero features

2:8:09

be just wanted to

2:8:11

add this.

2:8:12

So,

2:8:12

your additional feature

2:8:13

which is one

2:8:14

that's,

2:8:15

now it's

2:8:15

just a bias

2:8:16

coefficient feature

2:8:17

but

2:8:17

X to be power zero.

2:8:18

Now

2:8:19

X to be power zero

2:8:19

is always

2:8:20

like equal to

2:8:22

one,

2:8:22

okay?

2:8:22

Now you're with me?

2:8:25

Yeah, okay?

2:8:42

Now, now, now let's come back to the conversation.

2:8:45

Now let's come back to the conversation.

2:8:46

We made a data set

2:8:47

set made,

2:8:48

then after that we will do linear regression

2:8:52

and you are able to clearly see

2:8:53

the linear regression is a,

2:8:54

linear regression is a, is a very, very poor quality model.

2:8:57

Now, look,

2:8:57

training accuracy is so, so high and testing is so low.

2:9:01

It's zero to be

2:9:01

come and more than more bad.

2:9:03

This is a tremendous amount of overfitting

2:9:04

we are able to see.

2:9:05

This is exactly what I wanted to demonstrate.

2:9:07

When you take a data set like this

2:9:09

where there are so many redundant features,

2:9:11

164 features I'm made right?

2:9:13

You can actually see the tremendous amount

2:9:15

of overfitting that is happening.

2:9:17

Tremendous amount of overfitting.

2:9:19

The unstable complex features

2:9:21

cause massive mathematical instability

2:9:23

and the data is highly overhaul.

2:9:24

What will?

2:9:25

What we're?

2:9:26

Now, we'll make it pipeline,

2:9:27

min-max caler,

2:9:28

we will standard best practice.

2:9:30

And number two, we will do lasso regression.

2:9:32

Lasso regression, okay?

2:9:34

With alpha equal to 0.001, hyperparameter.

2:9:37

Remember, we don't know the right number.

2:9:39

We will have to tune it.

2:9:40

Real we have this to tune it.

2:9:42

We'll back in.

2:9:43

But today we have seen the basic idea.

2:9:46

Of 0, low, up 1, low,

2:9:47

or 2, no,

2:9:48

and you find out that value of alpha

2:9:50

for which you get the best accuracy.

2:9:52

So what are we expecting?

2:9:53

So what are we expecting?

2:9:54

Same thing, pipeline,

2:9:55

make dot fit, dot score.

2:9:57

Same thing.

2:9:58

Dot score from what comes?

2:9:59

R squared is helpful to tell you

2:10:02

how good is the model and

2:10:04

it's interpret from RMS.

2:10:07

The idea should be clear.

2:10:09

So now, let us go back and run this.

2:10:14

Let us run this.

2:10:16

And you can see that once we apply min-max and lasso together,

2:10:19

framing score is 61, testing score

2:10:21

is 57, more good fit model.

2:10:23

model.

2:10:24

Model good fit.

2:10:25

And the best part is that out of 164 features, this is the best part.

2:10:30

This is the amazing part.

2:10:32

Out of 164 features, Lasso realized most were just redundant noise.

2:10:36

And that's going to be.

2:10:38

We have randomly features.

2:10:39

It has mathematically deleted 156 features.

2:10:43

156 of those features, its weight is 0.

2:10:46

156, the features is its weight zero.

2:10:49

You can here.

2:10:50

You can do it.

2:10:51

this is your pipeline, so you can actually go and see what those features are.

2:10:55

It's how coefficient zero, you can see.

2:10:57

It kept only eight most important features to make the prediction.

2:11:01

That's it.

2:11:02

That's it.

2:11:03

164 message.

2:11:05

But it's only the original art which we had.

2:11:08

So this is just wanted to simulate this for you,

2:11:11

how it's happening.

2:11:13

That's regularization for you.

2:11:15

Now,

2:11:16

now a question is that, sir,

2:11:17

regularization we always going to do regularization?

2:11:20

Are we always going to do regularization?

2:11:21

No, you will only do regularization if your model is overfitting.

2:11:26

If your model is overfit only then you can do regularization.

2:11:30

If the model overfit not, then you're regularized.

2:11:32

Because regularize what is?

2:11:33

Regularize is what is.

2:11:34

Regularize is that you want to constrain something.

2:11:37

So, if you're going to go to it,

2:11:39

constraint it, right?

2:11:40

Isn't it?

2:11:41

That is another thing to keep in mind.

2:11:42

This is not something you will always do.

2:11:44

iteration one, you will always do normal linear regression.

2:11:46

Iteration two, you will go back and do something for lasso regression.

2:11:51

Okay? Now, finally, last, last thing I will talk about.

2:11:55

This, you do not worry, this is the next thing that is coming from the next session onwards.

2:11:59

This is the magic thing.

2:12:01

I like to call it the magic thing, but, okay, so let us see.

2:12:06

Same thing I will do.

2:12:09

So I'll share it you at last way, okay?

2:12:11

I will just share this with you at the end, what it is.

2:12:14

And here I will use, we'll use a different algorithm.

2:12:20

A different algorithm. A different and more powerful algorithm.

2:12:27

And let us see that.

2:12:33

Called.

2:12:37

You see the power of Gemini?

2:12:41

We've got nothing.

2:12:42

I'm just, I'm just typed here.

2:12:44

I want to use a more powerful algorithm.

2:12:46

It has understood that we have linear try.

2:12:48

Lasso tried.

2:12:49

I got a slightly better.

2:12:50

model and now I want to try something even more powerful.

2:12:53

And it is automatically recommending random forest.

2:12:56

Random forest is actually the topic for next to next week.

2:12:59

Sorry, next week.

2:13:02

Monday's session we're random forest.

2:13:04

It is a more powerful algorithm.

2:13:06

And this is just to show you from a code perspective,

2:13:08

how beautifully you can do this.

2:13:10

Let us see, nothing changes in the code.

2:13:12

I don't want to confuse you, but I just want to show you from a code perspective.

2:13:16

Just from a court perspective, the story remains the same.

2:13:19

We've done.

2:13:20

Look, guys.

2:13:21

Same to same thing.

2:13:22

Okay?

2:13:23

Now here we're just train accuracy or test accuracy.

2:13:26

Let me just copy the code.

2:13:29

Just I will do the train accuracy in test accuracy.

2:13:32

Nothing.

2:13:33

That's it.

2:13:34

The code remains the same.

2:13:35

Nothing has changed.

2:13:36

That's the pipeline.

2:13:37

Just linear regression,

2:13:38

we have random forest regression

2:13:39

that means it is a more powerful algorithm.

2:13:42

That's it.

2:13:43

It is a more powerful algorithm.

2:13:44

So we can try this out.

2:13:46

So we can absolutely try this out on the original data.

2:13:48

And you will.

2:13:49

usually see that the results will be a little better.

2:13:51

Okay, so you can here.

2:13:52

Shaih, we've got a quite actually struggle.

2:13:56

But usually with random forests, we will, you know,

2:13:59

it's a very powerful algorithm.

2:14:01

And we'll usually see that the results will be a lot better.

2:14:03

It takes a lot of time to run also.

2:14:05

But we will see that it will generally give us better results overall.

2:14:09

Okay, so it's the last thing that I wanted to share with all.

2:14:12

It will take a while to run.

2:14:13

It will take a while to run actually.

2:14:15

Yeah.

2:14:17

Because there are like 164 features.

2:14:19

we have created. So lots and lots of features have created.

2:14:22

So that's why it's going to take a little time to run.

2:14:25

But eventually we will be able to see that the overall accuracy and the R squared,

2:14:29

your model here, usually the model will be very good with these kinds of methods.

2:14:35

But what is going on behind the scenes?

2:14:37

That is part of our next session.

2:14:39

Okay? That is part of our next session.

2:14:42

This will take a while to run.

2:14:44

Sure.

2:14:45

So that's to summarize the entire conversation for

2:14:49

what we did today, guys.

2:14:51

So I think it's been a long discussion today.

2:14:53

So we have talked about regularization.

2:14:56

We understood what is the meaning of regularization.

2:14:59

We understood the impact of regularization and model behavior.

2:15:03

Alpha, how we control kind of

2:15:05

different types of evaluation metrics.

2:15:07

We talked about it.

2:15:09

Error analysis, how we identify

2:15:11

recidivize is kind of related to what we did.

2:15:14

And also a very important practical perspective,

2:15:16

that we choose.

2:15:17

And choosing what?

2:15:18

What?

2:15:19

Choosing what is?

2:15:20

When you're building a model, you will use R squared to get a score, get an accuracy, right?

2:15:26

And when you're, when you have to interpret interpretation

2:15:29

he will use RMAC and MAE kind of metrics.

2:15:33

And there are also, what was the difference between these two?

2:15:36

We have discussed that RMAC penalizes, RMAC penalizes high errors.

2:15:43

If the difference between actual and predicted is very high, RMAC will penalize that.

2:15:47

That is the other thing that we also look there.

2:15:49

This is the summary of our entire session.

2:15:53

And you can actually see this, this is still taking time.

2:15:55

This is a lot of time.

2:15:56

So just wanted to show you that in real world,

2:15:59

I think this is the great case study where you can start to realize

2:16:02

that in real world, when you're working with massive data sets,

2:16:05

with lots and lots of features, these models can sometimes take days and even weeks to run.

2:16:09

Now, in our case, we are able to do DETASIS class for

2:16:12

so we are able to do Dots fit in a matter of minutes or seconds,

2:16:16

seconds, four, second in our model been made.

2:16:18

model, but that will not happen in production.

2:16:21

When in real world, like Svigi

2:16:22

the delivery prediction model

2:16:25

made, Uber made a model to predict the price

2:16:28

that he will have to pay for the cab ride.

2:16:31

These models have taken a tremendous amount of time to train.

2:16:34

Uber's data scientists and Swigi's data scientist

2:16:37

they've also in Jupyter notebook models

2:16:39

have been made. It's also data.

2:16:41

They have data. They're models would have taken

2:16:44

days and weeks to train.

2:16:46

Weeks, quite literal.

2:16:47

Not kidding, it's weeks.

2:16:49

Weeks is very standard.

2:16:50

But just that they have more powerful hardware, better compute,

2:16:53

and it takes runs faster.

2:16:55

Okay, okay.

2:16:57

Okay, guys, all good.

2:16:58

So I will pause at this point in time.

2:17:01

So thank you, everybody.

2:17:02

And from here, we go to the next session,

2:17:05

which will be on classification.

2:17:06

So classification, we'll more be interesting things.

2:17:10

And as I told you, whatever, the last part,

2:17:12

what we did here, random forest,

2:17:14

this we will see in our next classification session.

2:17:17

Okay, so this is.

2:17:17

the next thing that we will be doing here.

2:17:20

Okay.

2:17:21

So thank you, all of you.

2:17:22

I will give it to Pratap over to you.

2:17:26

And have a good night, everybody.

2:17:27

Have a good night.

2:17:28

And I will see you in the next session on Wednesday.

2:17:31

Yeah.

2:17:31

Take care.

2:17:32

Take care all of you.

2:17:34

And this, this notebook is already shared with you.

2:17:36

This is what I talked about.

2:17:38

I think this is going to take a time to while to train.

2:17:40

I will keep it running.

2:17:41

What just how it's kind of, you know, you can access it.

2:17:44

So 25th May is the folder.

2:17:45

Same, same cohort.

2:17:47

So every day, I'm creating the folder name by the date and I'm familiar.

2:17:52

So same is the, okay, you can access.

2:17:56

So thank you guys.

2:17:57

Thank you so much.

2:17:57

Have a great night and I will see you in the next class.

2:18:01

Okay.

2:18:02

Thank you, sir.

2:18:03

Just one thing.

2:18:05

If you can just take mark the points on the sheet.

2:18:08

Yeah, yeah, sure.

2:18:09

I'll do that.

2:18:10

I'll do that.

2:18:11

Sure, sure.

2:18:12

I'll do bye.

2:18:13

Okay.

2:18:15

Yeah, sure.

2:18:15

I'll do that.

2:18:17

Okay.

2:18:17

yeah and okay all right so students I'm releasing the feedback bowl now and as usual after the

2:18:26

feedback poll you can join the Mendi-meter quiz all right

2:18:33

also copy copy link

2:18:39

Mentiator quiz

2:18:47

Okay.

2:19:04

Sir, let me know when I can share the screen if everything is okay.

2:19:14

Yeah, yeah, yeah.

2:19:15

Oh, I thought I stopped sharing.

2:19:16

I'm so sorry.

2:19:17

Oh, I'm sharing, huh?

2:19:20

Yeah, go from.

2:19:20

Okay, I thought I stopped.

2:19:22

Okay, yeah, sure, sure.

2:19:23

Please, please.

2:19:23

Please, you can carry on.

2:19:24

Yeah, I'm done.

2:19:25

Thank you, guys.

2:19:25

Thank you.

2:19:26

Great night.

2:19:27

Thank you.

2:19:27

Yeah, please carry on.

2:19:29

Yeah.

2:19:31

All right.

2:19:32

Yeah.

2:19:33

Yeah.

2:19:33

Yeah.

2:19:34

There are still five students, it seems, who have not voted.

2:19:41

Are you guys able to see the poll?

2:19:46

If someone is not able to,

2:19:47

to see the poll just let me know in the chat.

2:20:01

About three people left, I guess.

2:20:04

Anyone who's not able to see the poll?

2:20:17

All right, once there are like 11 or 12 players, I'll start the MENTimeter quiz then.

2:20:35

There are three people that are still left to vote, two people now.

2:20:43

Wait, four people roughly.

2:20:47

Guys, can anyone, is anyone not able to see the Menti meter quiz?

2:20:54

Or the feedback poll, I mean the feedback poll.

2:21:08

Is anyone not able to join the Mentiator quiz or they are not able to see the feedback poll?

2:21:13

Message in the chat, please.

2:21:15

Okay, it seems everyone is voting.

2:21:16

It seems everyone is voted.

2:21:17

Okay.

2:21:20

All right, just seven players?

2:21:25

Can I get at least 10?

2:21:31

10?

2:21:46

Fine.

2:21:48

Thumbs up if you want me to start the minty minute request then.

2:21:53

Three, four. Five. Okay. All right. I guess I'll start.

2:22:16

So, yeah, this is fairly easy.

2:22:23

It's something sir asked you guys to keep in mind.

2:22:26

Pretty much as it is.

2:22:31

Okay.

2:22:36

Expect everyone would have gotten this correct.

2:22:39

Yeah.

2:22:40

Awesome.

2:22:41

Great job.

2:22:46

All right. Next question.

2:23:16

Again, this is, I think fairly easy.

2:23:27

All right.

2:23:30

It seems everyone is voted.

2:23:33

Oh, okay.

2:23:36

So, yeah, higher alpha means stronger shrinkage because you are trying to reduce.

2:23:45

So they are.

2:23:46

analogy that sir gave was a jail cell, right? If you increase the alpha, you are decreasing the,

2:23:54

you are making the jail stronger, kind of. So yeah, the correct answer is stronger shrinkage.

2:24:02

Okay, moving on.

2:24:16

In SK learn dot score for linear regression returns what?

2:24:32

Yeah, this one is a little, oh, everyone is voted very quickly.

2:24:40

Okay.

2:24:42

Yeah, it returns R square error.

2:24:45

So.

2:24:46

So, okay. I'm not sure why people voted RMSC. But yeah, in SK Learn score returns R

2:24:56

square. And so it did actually cover that point as well. So yeah, moving on. These are all like mostly

2:25:08

factual questions, not something that you will need to really understand.

2:25:16

Okay. Next question. Second last question. Which report is strongest before deployment? So when I say report which may, which are the, like, which is the parameter or the number that is very important, whether it is R square or train score or test metrics or coefficients.

2:25:46

It's a little tricky question actually. I have to, should think about it. Oh, awesome. Most of you did get it correct. Amazing. Yeah. So before deployment, your most important scores are test metrics, basically. R square coefficients, our train scores. These are all like there, but your test matrix is the one that is most important.

2:26:16

All right. Last question. Root mean square error is most sensitive to what?

2:26:33

Is it sensitive to large errors? Is it sensitive to small errors?

2:26:38

Low alpha or feature names?

2:26:46

and it seems they're voting at random.

2:26:51

Yeah, so root mean square error is very sensitive to large errors because understand that you are taking a square, right?

2:27:00

And you do a square and then you take a square root of it.

2:27:03

It's like if you imagine a right angle triangle, then the root mean square error is basically like the hypotenuse.

2:27:12

the bigger the difference between the two sides, the larger your hypotenuse will be, right?

2:27:21

So think about it like that, geometrically.

2:27:25

You can also do it like mathematically, like taking a couple of examples.

2:27:31

With small errors, the square is usually very small, and then addition of that and then you do square root of that.

2:27:40

So the output is not.

2:27:42

very large but with very large errors the RMSC is very like RMSC magnifies that a lot.

2:27:52

So all right with that we are at an end of where at the end of the quiz.

2:28:02

Yeah you you guys were answering like very fast. I'm a little concerned. Oh, okay.

2:28:09

Sheik was at the last at the start like first question.

2:28:11

First question now is on the top.

2:28:14

Congratulations. Great job.

2:28:17

All right. With that, we can end this Menti meter presentation.

2:28:25

Science, if you're still there, maybe you can show the random forest output if it is done.

2:28:33

If not, yeah, up to you.

2:28:41

Hello, sir.

2:28:49

Okay, I think he's not there. Maybe he forgot to leave the meeting.

2:28:54

All right.

2:28:54

Guys, with that, we are going to end the, we are going to end today's session.

2:28:59

I will see you all day after tomorrow, Wednesday, where we will be covering,

2:29:06

science will be covering logistic regression fundamentals.

2:29:09

Okay?

2:29:11

All right.

2:29:11

Have a good night, guys. Bye-bye.

2:29:15

Oh, there's something in Q&A. One second.

2:29:18

Sorry, I get the concepts but unable to apply in practice.

2:29:20

Need guidance in practice.

2:29:22

So there is going to be a session on Friday for more practical.

2:29:29

Like, it is more of more practical associated.

2:29:33

And I would request you to attend that.

2:29:35

And then the tutorial on Saturday, if you still have, still feel that you are not able to practice

2:29:40

and you need.

2:29:41

any practical guidance.

2:29:43

The tutorial on Saturday, I will be taking and there you can ask me.

2:29:48

And we can have some maybe practice problems.

2:29:53

All right.

2:29:55

With that, we are at the end of session and then I'll close it.

2:29:59

Okay?

2:30:01

All right.

2:30:02

Bye, bye, guys.

2:30:03

Thank you.