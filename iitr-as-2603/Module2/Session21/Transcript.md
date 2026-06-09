0:00

No, no.

0:01

No.

0:02

No.

0:03

No.

0:04

No.

0:05

No.

0:06

No.

0:07

No.

0:08

No.

0:09

No, the other

0:11

wheelchair down

0:12

and he'll be able.

0:39

Thank you

1:09

Thank you

1:39

Thank you

1:41

Thank you

1:43

Thank you

1:45

Thank you

1:47

Thank you

1:49

Thank you

1:51

Thank you

1:53

Thank you

1:55

Thank you

1:57

Thank you

1:59

Thank you

2:01

Thank

2:06

Thank you.

2:36

Thank you.

3:06

Thank you.

3:36

Thank you.

4:06

Thank you.

4:36

Thank you.

5:06

Thank you.

5:36

Thank you.

6:06

Thank you.

6:36

Thank you

7:06

Thank you

7:36

Thank you

7:38

Thank you

7:40

Thank you

7:42

Thank you

7:44

Thank you

7:46

Thank you

7:48

Thank you

7:50

Thank you

7:52

Thank you

7:54

Thank you.

8:24

Thank you.

8:54

Thank you.

9:24

Thank you.

9:54

Thank you.

10:24

Thank you.

10:54

Thank you.

11:24

Thank you.

11:54

Thank you.

12:24

Thank you

12:54

Thank you

13:24

Thank you

13:26

Thank you

13:28

Thank you

13:30

Thank you

13:32

Thank you

13:34

Thank you

13:36

Thank you

13:38

Thank you

13:40

Thank you

13:42

Thank you.

14:12

Thank you.

14:42

Thank you.

15:12

Thank you.

15:42

Thank you.

16:12

Thank you.

16:42

Thank you.

17:12

Thank you.

17:42

Thank you.

18:12

Thank you

18:42

Thank you

19:12

Thank you

19:14

Thank you

19:16

Thank you

19:18

Thank you

19:20

Thank you

19:22

Thank you

19:24

Thank you

19:26

Thank you

19:28

Thank you

19:30

Hi, everybody.

20:00

Good evening, all of you. We will just be starting on.

20:14

Good evening, everybody.

20:30

Thank you.

21:00

Thank you.

21:30

Thank you.

22:00

All right, so folks, let's start on here and just to quickly set the context in terms of what we have done, what we have discussed so far, where we are in the curriculum so far.

22:18

I'm just going to take you through, you know, this brief journey.

22:22

So previous session, previous module was on Python, the current module, we are still in the machine running module.

22:29

We've discussed quite a bit until now, we have covered supervised learning, we have covered unsupervised learning, and today we are discussing something called time series.

22:39

So time series problems are again very much related to what we have done so far, but there are some newer ideas, some key ideas that we will discuss in this session, and time series kinds of problems are very useful in scenarios and in domains where there is

22:59

some kind of time component involved. If you look at use cases like stock markets and all these

23:04

kinds of use cases, these are the kind of scenarios where time series forecasting comes in very, very handy.

23:11

Typically, the stock market kind of context and all these kinds of contexts, you can see time series forecasting is a very,

23:16

very handy, you know, kind of a thing in those kinds of scenarios. Okay, so you are trying to, let's say,

23:23

predict the sales of a company, you're trying to predict the energy of a company, energy demand, you are trying to

23:28

predict and those kinds of things. So, so whenever there is some kind of time component involved,

23:34

you know, be you're trying to predict the sales, we are trying to predict the energy and these

23:39

kinds of things. These are the kind of scenarios where, as I say, time series forecasting comes in

23:46

handle. Okay. Now, moving on. So we will, we will talk about it. And obviously the next module,

23:54

this is only a few more sessions left in the machine learning module.

23:58

And we're going to be very soon starting out with the generative AI module, where we, you know, that's the thing that I'm sure most of you are waiting for.

24:07

So we'll be talking about generative AI from the, from the next module onwards.

24:12

So there we will see things like large language models.

24:17

We will explore concepts like agents, rags, and all these kinds of things who will talk about.

24:23

Okay, that's the intent.

24:28

So now, moving on, let us quickly jump into our session and understand what time series really is. So this is the contents that I've uploaded in the 8 June folder. Now, as I told you, what do we mean by time series kind of data? What is it, what is it that usually refers to? Well, as I said, like, if you look at the official definition of time series, the official, the official,

24:58

definition of time series is nothing but a sequence of data points recorded at successive

25:04

points in time. So time is a very important component. If you look at all the examples we have done so

25:09

far, you know, be it regression, beat classification, you go back to all the use cases that we have worked on so

25:15

part. In all these use cases, the data points were not recorded at intervals of time. If you, you know,

25:22

let's say for example, the diabetes classification use case, you know, we are looking at the features of a person to

25:27

predict whether the person is diabetic or not. So how is the data collected? Every row of

25:32

data, what is it? Each and every row is not each and every time interval. Every row stands for one

25:40

person. Every row stands for one patient. So we are basically cracking this kind of patient level data

25:47

or person level data is what we are tracking. That's the intuition. Similarly, if you look at the other

25:55

use case, you know, if you go back to the other one, not the disease diagnostics one, but if you look at

26:01

the credit default forecasting, we are looking at the different features of the transaction. And based on

26:08

that, we are trying to predict whether the transaction is a fraud or the transaction is not a fraud.

26:13

If you go back and look at the fraud detection, you know, use case, transaction fraud detection,

26:19

how are you doing that? How are you doing transaction fraud detection? What is each row? If you look at

26:23

that data set, what is every row of data? Every row of data basically corresponds to

26:28

a credit card transaction. It is not recorded at points in time. A transaction happened,

26:35

that is recorded. Their patient level data we have. Okay, and if you go back to several other

26:41

use cases we have done, let's say California housing prices. Every row stands for a house.

26:47

Every row stands for a district in California. We are looking at district level data.

26:53

On the contrary, if you look at time series data, time series data will be arranged like this.

26:59

Simple. So there has to be some component of date, time present here. You can imagine a data frame

27:05

where every row stands for some time. Now, that time is something that we can debate about it.

27:12

What is the interval that you take? It can be daily. I think here we are taking daily, first January, second

27:18

January, third January, or it can be hourly, it can be weekly, it can be monthly, it can be monthly, whatever.

27:23

But this kind of a data set where every row stands for some kind of a time, that is what is referred to as time series data.

27:33

Another very important thing when we talk about time series data is, if you see, arranged in time order.

27:41

I just wanted to highlight this term again for you, arranged in time order. So the organization of your data and the sorting of your data also matters a lot here.

27:50

That means whatever data that you see on the screen,

27:53

If you look at all the other exercises we have done so far, in all those other exercises,

27:59

you know, if you think about it, what we covered in all those other exercises, if you see,

28:04

well, it was not as if our data was sorted in any order.

28:11

Go back to the diabetes data set that we worked on.

28:16

If you look at the Pima diabetes data set that we worked on, what did we do there?

28:20

What did we fundamentally do in the Pima diabetes data?

28:23

sector. So, what did we, what did we fundamentally do in the Pima diabetes data search?

28:30

Every row was a person. Every row was like the, you know, the, we are the features of the person.

28:36

Each and every row corresponds to the features of the person. That's what we are tracking. Each and every

28:42

row stands for the features of the person. And it is not necessary that the data has to be arranged

28:51

in a particular order. If you look at that entire data frame, person one can come first,

28:56

person seven can come later, person nine can come before, doesn't matter. Whatever supervised learning

29:02

we have done so far, model. Dot fit, X, train, Y train. That's been the standard code we've been writing,

29:07

right? We're saying model. Dot fit X, train, so we are fitting a model on the train data. So anybody

29:12

you say model. Dot fit, X train, what is going on? What is happening when you say model.

29:17

dot pick. The order is ignored. The order does not matter. The order fundamentally does

29:24

not matter. So that's the way how we are going about it. But if you look at time series data,

29:30

the order matters. Whether you put first January, then second January, then third January,

29:35

that data must be in an order. Like for example, see, if I, I cannot just take third January and put

29:41

it in between the two. No, I cannot do that. The entire solution can get missed up. And I'll give you more

29:47

examples to justify what I'm saying. So, so a key takeaway is the order of the data is very,

29:52

very important, right? So that's one way to look at it. And I think this is, again, a very nice thing

29:56

that we are saying. A weather station records temperature at the hour. So over a year, you will get

30:01

86, 8760 recording readings in order. And this is very real world. If you look at many weather

30:06

stations across the world, they'll be recording data on a daily basis. Every day, what is the temperature

30:11

they'll be recording. Right. And, but if you shuffle them randomly, if you take the data and if you

30:16

shuffle them randomly, it will become meaningless. So right now we are able to see a certain

30:22

trend. We can, you know, we can say, okay, first January, second January, third, fourth, fifth,

30:26

six, 17, 18. So we can do a 15 day forecast. We can see a trend. Imagine you're looking at a 15 day

30:31

forecast and the dates are all jumbled up. It becomes meaningless. So time series data must be in a certain

30:37

order. That's very, very important. So order matters in time series. Okay, the order matters in time series.

30:43

that is a very, very important thing I wanted to clarify. Now let's get a little

30:46

deeper and understand two very important concepts in time series, which is called trend and

30:51

seasonality. What is the meaning of trend and what is the meaning of seasonality? What do these

30:55

things actually refer to? So trend is basically what is referred to as a consistent long-term

31:04

movement. That means on an average, what is going on, right? So a very good example would be,

31:12

I think, you know, we can, we can take a, uh,

31:16

Take a look at this particular time series data up.

31:19

You have got quarter one, quarter two, quarter three, like this. Or maybe we can take a more real world use this because we already have like, you know, maybe we can take Nifty, 50, 50, 50, right, or Sensex, right?

31:32

So the stock markets, what is the trend today?

31:35

Today the markets were down, you can see. But anyways, we can take a look at, let's say, the patterns that played out.

31:44

So one month the markets are also down, you can see.

31:46

Okay, very interesting. Anyways, we'll go back to the max print. Now, if you look at it, the stock markets in India over the last 1990 onwards, all the way to 2020, it has been more than 30 years of data we are seeing on the screen right now. And very interesting, there have been lots of fluctuations, like sometimes the markets have increased, sometimes the markets have decreased. This is that excellent example of time series data. First of all, how do you, how do you understand?

32:16

understand this data set. Every row stands for a particular time interval, right? So I think markets will always

32:23

have day level data. So what you're able to see right now is every day. Can you see? I'm hovering my cursor on this and being saying

32:30

third May 2024, what is the sense X. Okay? First 10th, November, 23, what is the sense X? So we are looking at every day level data.

32:39

So same way that we were seeing on the screen here. Every day is like one row. And for every every day,

32:46

Every day here we are tracking what is the stock price. So that makes it a time series data. And what is trained? So obviously there are a lot of fluctuations happening. You can see sometimes the price is going up, sometimes the price is going down. A lot of fluctuations are definitely happening. There was a COVID drop that happened 2020. There was a massive drop that happened. Again, the markets recovered. Again, the Iran war, if you see, I think around this point in time, 2026, around this time. Again, there was a massive drop. And the drop is still happening right now. It's not recovered, actually.

33:16

The point is, there are a lot of these fluctuations that, you know, that are basically happening.

33:22

But the interesting part is,

33:25

trend is telling you on an average, what is the overall pattern? What is the average?

33:31

That is what we understand by the trend. So trend refers to the overall pattern.

33:36

Trend refers to the average pattern. On an average, what is going on? So sometimes the prices will increase.

33:42

Sometimes the prices will decrease. But on an average, what is happening in the course of the last 30 years?

33:46

And that is what trend tells you. And I think if you look at the stock markets and as any, every investment analysts tell you that markets are always in an up trend, I think they're always trending up on an average. If you, if you, barring fluctuations and all, even if you look at the last one year data, not happened in the last one year, right?

34:03

Actually, one year markets are down.

34:05

See, that's another. See, that's another matter. I think the Iran war played a big role. If you see the markets were majorly stagnant and there was a big drop. I mean, if you look at the five-year data, five-year data, five-year is a good interval to see. This is a trend, right? It's trending.

34:16

up. Yes, there have been minor fluctuations, but overall by and large is trending up. That is what friend basically

34:23

refers to. That is the meaning of trend. What is the overall pattern? The long-term direction in time series data, that is what

34:30

trend is. Is it consistently going up? Is it consistently going down or is it extract? And trend is usually observed over

34:37

a longer duration. You want to take a bigger sample of data and understand the trend on the basis of that. And as I say, you know,

34:46

Because you are looking at a big picture view, the big picture direction, you know, you completely zoom out of daily ups and downs.

34:53

You're not interested in that, but you're looking at the overall patterns. What is happening?

34:57

Okay. So there are so many other kinds of analysis that you can do that. Now coming to seasonality.

35:04

What is seasonality? Seasonality tells you regular repeating patterns at fixed known intervals.

35:12

That is what is referred to as sustainability. I think this example was.

35:16

very nicely given if you see and the x-axis we have time. Again, this will be like quarter and

35:22

year combination. So quarter one of a certain year, quarter two of a certain year like that. And value is,

35:27

let's say, let's say this is like some kind of price data or whatever, in the e-commerce data,

35:33

whatever. As you can clearly see, there is a trend that is visible. The trend is basically an up-trend,

35:40

right? So if you see there's an up-trend that is happening. That means on an average, there's an increase. There's an increase

35:46

that we are able to see. So on an average, what is happening? On an average, there's an

35:52

increase that is happening. That is the uptrend that you are able to see on the screen.

35:58

Seasonality basically tells you what are the regular repeating short-term variations. That is what

36:03

is reference as a seasonality. So trend is the, on an average, what is the overall direction? That is what we call

36:11

the trend. And he on an average, what is the overall direction? That is the trend.

36:16

And seasonality is nothing but the fluctuations that are happening on a, on a daily basis.

36:25

So that is what is referred to as a similarity. So whatever fluctuations are happening on a daily

36:29

basis, that is a similarity. These are the regular repeating, short-term variations or the

36:35

regular repeating short-term fluctuations that are happening. And that is what we call the

36:40

similarity. That's a situation. I hope everybody is aligned with what is this, okay?

36:46

And if you think about it, why is it happening? Why is, why are we seeing the fluctuations, right?

36:52

So fluctuations can happen, right? See, long term it is increasing. But all of a sudden,

37:00

you know, there is a small seasonal fluctuation that is happening. Maybe I can use a bit of Gemini

37:06

to mock up another nice diagram for you. So we can look at, you know, a very good example of

37:11

seasonality. So we can take an example of some classic cases.

37:16

where seasonality actually happens. Like they say festival sales, Amazon sales and these

37:21

kinds of context if you see. Seasonality is a very real thing. There's nowadays are very real thing.

37:26

Or maybe ice cream sales. Ice cream sales will peak every summer or maybe air conditioning.

37:31

Very interesting air conditioning, you know, sales if you see. Okay. So we can actually go

37:38

and see, you know, like this kind of a thing. Let me see Germany is able to generate some data.

37:45

So show me, show me the last five years approximate.

37:55

We want to look at a slightly longer pattern as well.

37:58

Let's say the last 20 years approximate air conditioner,

38:05

air conditioner sales data and render the same data and render the same as a line.

38:15

What is this kind of chart called? It's called a line chart. X axis is a time. Y axis is some value. I want to also see seasonality clearly occurring, which shows, which shows the clear pattern of AC demand during summers and

38:45

less to low demand during winters. So maybe you can look at this one. Let us see. Let us see what it generates. And you will see the you will see the line chart beautifully coming up. Okay. We'll just wait for Germany to do it. It will do a very nice job. It will probably give you some data set and it will give you a nice line chart and you'll be able to see for yourself. So last 20 years data ahead. So there definitely fluctuations will happen. If you talk about COVID, let's say COVID was a time when a lot of people

39:15

conserving cash. I'm sure COVID also happened during summers, right? So that was around March April when it was a peak of COVID lockdown was happening. But yeah, I mean, a lot of people, people would not have gone out and spent a lot of money that time. There was a massive dip that happened. But I think this is a nice, this is a nice example. You can see. This is a nice example. You can take a look at it. Okay. And you can take a look at this one. So the 20 year macro trend, you can take a look at it. On an average, what is going on. On an average, it is spending upwards.

39:45

So if you look at the average pattern, the average pattern is going on. Okay? So, and this is the seasonal trend. So this is, this is peaking around, I think, May June. If you look at it, this is May June. It's a huge peak around May June. And then it is again dropping. Again, it is peaking around May June. This is the monthly sales of AC units. Again, it is dropping. And if you try to draw a line, this line will basically go somewhat like this. So the trend is increased because it is obvious.

40:15

is that, you know, as the years have increased, the country has become more developed, more and more people, people standard of living has increased. So previously in homes, maybe people who would have normally bought a fan, now they are buying an AC. So on an average, there is more sales of AC happening. So the trend is on an average positive, uptrend, positive trend, on an average. But within that, you are able to see there are seasonal fluctuations happening. So there are certain months when the AC sales is very low, and there are certain months when the AC sales is very low. And there are certain months when the AC sales is

40:45

is very high. That is the concept of sustainability. Okay, I hope everybody is aligned with this. That is the concept of what seasonality refers to. Now, moving on, coming to the concept of train test split. So I got another nice demo in my, in my slides also. I'm going to show that also so that everyone is aligned. This is another nice example. We can take on the capital. So this is the real world data. I think if you take a look at it, this is the real world data.

41:15

But this will be, this will be something how your data will look like for something like high stream saves or something, okay?

41:23

So you can see on an average, there's a, you know, there are lots of ups and downs and dips that are happening.

41:28

So if you look at the trend, on an average, the trend is going off.

41:31

If you look at the average trend, the trend is actually going up. If you look at this, the trend is going up.

41:35

But if you look at the seasonality, the seasonality is clearly visible. So the seasonality is very, very clearly visible. It is going somewhat like this.

41:42

It is clearly visible.

41:45

Sometimes it is going up, sometimes it is going down.

41:48

Now, moving on, very, very important.

41:52

We want to understand the concept of train test split.

41:56

Right. What is the concept of train test split?

41:58

We've been discussing this like all this file in our sessions.

42:04

Very, very important concept of time series data is the train test split has to be completely in

42:13

chronological order.

42:15

All this while, if you go back to our machine learning conversations within our classes,

42:19

we did so many exercises like supervised learning and all that we did so much, right?

42:23

So in all our exercises, the frame test split was random.

42:28

Go back to any data set we worked on any model that we built.

42:32

How did we go about it?

42:34

We took the data and we split the data into training and testing.

42:37

So we are saying a certain percentage of our data is part of frame data.

42:40

80% of data is trained.

42:42

And the remaining 20% of data is trained.

42:45

percent of data is test. That's how we went about it, right? So we are saying, okay, a certain

42:49

percentage of data, you know, 80% of our data is part of train data and the remaining 20% of the

42:56

data is part of test data. So the train test split process that we went through was completely,

43:00

was completely random, was completely random. But problem is in time series you cannot do it.

43:09

You cannot do that in time series. The reason is because why you cannot do that in time series is

43:13

because the moment you talk about time series data, I told you at the beginning of my class itself,

43:19

the time series is inherently the order matters.

43:22

If you look at time series data, inherently the order will matter.

43:27

Order matters.

43:27

And because the order matters, the print test plate also has to be in a certain order.

43:33

So, so if you think of a use case, let's say we've got January to October data, right?

43:40

As you can see on the screen.

43:41

So we have also got.

43:43

overall January to October data is what we are having.

43:50

And if you have the January to October data, the training data, 80% of my data will be definitely January to August.

43:59

Right? So 80% of my data will be definitely January to August.

44:04

And the remaining 20% of my data will be September, October.

44:08

That's the way how we can look at it. So 80% of my data will be January to August.

44:13

And the remaining 20% of my data would be September October.

44:19

Now, why are we doing it this way?

44:20

If you think about it conceptually, why are we doing it this way?

44:23

Because, again, conceptually, if you look at it,

44:30

we are training the model on 80% of our data.

44:37

That is from Jan to August.

44:40

I think it's very obvious we want to learn the patterns from January.

44:43

to August. What's going on between January to August? So we want to understand the

44:48

patterns. We want to really understand what is going on between January to August.

44:53

Understand the patterns. And based on whatever you, you know, whatever patterns you learn from

45:00

Jan to August, you want to use those patterns and do the predictions for September of October. That's

45:06

the test data, right? So the chronological order is obvious because, see, unless you know August data, you can't predict

45:12

September data is very obvious. Unless you know, you know, July and August data, you cannot

45:17

predict September October. So that has to be the test data. But this was not the case in our prior

45:23

exercises. You go back to the California housing prices, you go back to the, there's so many exercises

45:30

we have done, diabetes data set, cancer data set, credit default data set. None of the exercises, the train

45:36

test plate had to follow this order. Because we could have preying the data on some 80% of our

45:42

rows 80% of our patients and we're going to predict it on 20% of some other patients because

45:47

there was no time order. But here, you know, we have to depend on these time. So this is one more

45:53

thing that is very, very important in time series. Otherwise, as we see the demo, lot of things are

45:58

similar. The process of ML machine learning that we do is very, very similar. But these parts will

46:03

be different. These parts you will have to do differently in time series, okay? So please keep

46:07

this at the back of your mind. Now, moving on.

46:12

The chronological split is very, very important. Please keep this at the back of your mind. Okay. Now, now we will come to the concept of rolling window. This is a very interesting concept and I, so I'll do this in two phases. One, I will explain the concept through some of our materials through my notes. And then I will take you to a real stock market use case. And I keep referring back to stock markets because that's something everybody can relate to. So rolling windows is actually a very popular concept.

46:42

used in the stock markets.

46:46

Specifically, the concept that we are looking at right now is called a moving average.

46:51

Some of you listen into these money control and these investment analysts talking on these news channels.

46:59

They will often use, you know, the term moving average.

47:02

Okay.

47:03

Yes, yes, moving average.

47:05

Very real world, okay, it's something that is used a lot.

47:06

And we see what moving average is, why it is important and what exactly it is and how to do it in Python.

47:12

we'll cap it up with a demo.

47:15

First, let us understand what rolling average actually is.

47:20

Okay, let us see that.

47:23

All right. So, um, so.

47:30

So we can see the general concept of it.

47:36

We can just look at the definition then I will show the demo.

47:39

If you see, as I discussed already, the raw,

47:42

daily values, they jump up and down, right?

47:46

So the raw daily values, they will constantly move around.

47:50

They will jump up and down.

47:51

And it is what we refer to as very noisy.

47:54

So the raw daily values are basically very noisy.

47:57

They will jump up and down.

47:58

And it is very hard for a model to read.

48:01

Think of it that way.

48:03

So it is, it is very difficult to do any analysis using that.

48:07

Because the raw values will, you know, moving up and down.

48:11

So it is very difficult for a model to read.

48:12

a model to read it.

48:14

Rolling windows are basically used to smooth out the noise.

48:18

And I will discuss what it is.

48:21

Why it is smootening the noise and how it is used to create rich features from the recent

48:25

history.

48:26

This is also a very important candidate.

48:27

So whatever topic we are doing right now, this is used as a kind of a feature engineering method.

48:35

So let me see what it refers to, what it is.

48:39

So you have to go and, uh,

48:42

define a certain window size you will have to go back and define a certain window size

48:47

as you're working with the rolling window there is a certain window size that you

48:51

will have to consider and you will have to define that particular window size.

48:56

Okay, to define that window size.

49:00

And every day, look at the last end days and compute their average.

49:06

Drop the oldest day at the newest and repeat.

49:11

That is.

49:12

why the term rolling window is used okay so i have a demo i'll show this to all of you

49:16

what is going on we'll see that but the concept is very simple like all that we are doing is

49:22

every day look at the last 10 days if you look at a 30 day moving average or a 30 day rolling

49:28

average okay you look at the last 30 days data and find out what is the average you get one value

49:42

you drop it go to the next day take the average drop it go to the next day take the average

49:47

and that's the way how it works out the window rolls forward in time okay let me explain to you

49:55

i think it will be better if i explain to you so this diagram very nicely uh calculates it we're

50:02

looking at a window with equal to three actually it looks like two but that's okay so what we will do

50:10

right now to start with this we will go back and we will calculate a kind of a rolling

50:19

average what this rolling average is basically doing doing okay so let me show this

50:40

is doing and how we can hang through it i want to just quickly open up one of my uh one of my

50:46

one of my notes also just allow me a minute i have the code snippet also i wanted to

50:52

parallelly run the code snippet as well so that everyone's able to follow that also now okay

50:57

let me open that up parallelly this is all under the eighth june folder right so everything

51:06

is under the eighth june folder i've already uploaded that all right

51:10

now let us move on as you can see this is the initial part what we covered i think

51:17

just to just going to wrap this up since the order chronological order we talked about we talked about

51:22

we talked about trend seasonality this is the thing that we discussed right so this is the trend seasonality

51:26

idea now and we also talked about the concept that of why the chronological split is very very

51:34

important so in machine learning you must always split your data in this in this order to prevent leakage

51:39

it always has to be chronological now let's look at the concept of lags and rolling windows what

51:47

exactly rolling windows are what is the concept of a rolling window what exactly it refers to

51:54

what is it basically so first of all uh

52:09

here all of you take a look at this first we are discussing the concept of lag

52:22

okay what is lag let us see that what it is it is bringing it is bringing a past

52:29

value forward as a new column right it explicitly tells the model model here is exactly what

52:39

happened yesterday that means see if you're looking at today's sales a nice way we try to

52:46

demonstrate this is if you say this is t if this is time period t this is basically time period

52:52

t minus one what happened yesterday so that's the way how the lag concept is so important so we

53:03

can do that using the shift function in python very simple to do it you will see that in the code but

53:09

what is it telling you you're able to show what happened yesterday you can show what happened

53:14

two days back like that for example if you look at my current demo i think this will be very relevant

53:20

this is my overall sales data and with respect to my overall sales data i think the you are able

53:27

to see with respect to my overall sales data you're able to see what happened the previous day

53:34

what happened the previous day what happened the previous day what happened the previous day

53:39

and so and so forth.

53:44

So that is what we are able to understand.

53:49

So we are actually having the DF features data pane.

53:52

We're creating a new column called day of week.

53:55

And this is how we are doing like DF features lag one is nothing but sales shift one.

54:00

Okay.

54:00

So we are we are saying sales shift one.

54:04

That's the way how we are doing this.

54:06

Okay.

54:07

So this is a sales shift one.

54:09

So this value, if you take a look at it, this value, whatever you are able to see,

54:16

this is today's sales, right?

54:18

This is time period at zero.

54:20

This is today's sales.

54:22

And mind you, this is DF features, DF underscore features.

54:24

We are looking at the top 10 rows right now.

54:27

So you can ignore the first entry.

54:29

The first entry you can ignore.

54:30

That's the initial one that is taken.

54:33

But if you look at this one, if you look at 4.04, what is, what is?

54:39

What is 404 telling you?

54:41

So this is today's data.

54:42

Let's say this is like whatever time period, Monday, Wednesday, Wednesday, Wednesday, Wednesday, Wednesday, Thursday, Thursday, Friday.

54:49

And this is what you originally have.

54:52

This is the data that we originally have.

54:55

This is what we have added.

54:57

This was the original data, original time series data we had.

55:03

And now if you look at this original time series data,

55:06

we right now only have a sale.

55:09

column. So we only have a column which says that, hey, what is the, you know, the sales

55:15

at time period T? We are only tracking what is the sales at time period T. But it will also be

55:22

very important to track what is the sales at time period T minus 1. The T minus 1 will also be

55:28

important now. I not only want to know what is going on at T, but I also want to know what is

55:35

going on at T minus 1. That is the reason why in 5.

55:39

we use this shift function. And you can see this is the code that we used here.

55:44

We used a shift one function and we created a new column. We created a new column called lag 1.

55:50

And we used shift two and we created a new column called lag 2. That means you are saying, hey,

55:56

what was the sales? So another way to look at this would be, you're saying, hey, what was the sales one day back?

56:05

What are the sales, T minus 1? And this is telling you,

56:09

what is the sales, sir, T minus two? This is the overall sales and you can see T minus one.

56:14

That means, so today is time period one. So with respect to today, yesterday sales was 404.

56:20

So 404 value is coming. So with respect to today, yesterday sales was 212. 212.2 is coming.

56:26

So that means, that means, and that means very interesting, you know, when you're looking at this

56:31

row of data, let's say you're trying to solve a problem and you're looking at this row of data,

56:36

you are able to not only see what is the sale.

56:39

today, but you're also able to see what is the sales yesterday and what is the sales

56:43

two days back. Because the sales yesterday was 212, that is reflecting here, and the sales two days

56:49

back was 404, that is reflecting here. This is very, very useful, especially for stock markets

56:54

and all these kinds of things, because, you know, when you want to do a prediction, what is important

56:58

is, if you, you know, just to clarify the whole story to all of you, what I'm doing and why I'm even

57:05

talking about it, this pattern will matter.

57:09

Okay, this is sales, right? And forget about rolling mean for a minute.

57:15

Imagine you've got lag one, lag two, and there are multiple lags that are not just one or two.

57:19

There are like hundreds of lags you will have.

57:21

Lag one, lag two hoga, lag three, you might have all the way to lag 100.

57:26

You want to look at a hundred days worth of data and based on that you want to predict the price.

57:31

Now, what I'm getting at is guys, I said, this is lag, not long, by the way, because I think the handwriting seems like long.

57:37

This is lag.

57:39

lag three got, lag four, okay?

57:42

And it goes all the way to lag 100.

57:47

And what market analysts they do is, they go and calculate all these lags.

57:53

So if you think from a real world regression problem perspective,

58:00

this is you're your data here here here all this we have talked about.

58:04

These are your features.

58:06

This are your features.

58:07

So these are all your features.

58:09

And based on this, you are trying to predict sales.

58:12

That's, that's what it boils down to.

58:14

So this lag 1, lag 2, lag 3, lag 4.

58:18

This is, this entire thing is your input, right?

58:22

Make sense?

58:23

This entire thing is like your input X and this sales is like your output.

58:27

This is not going to ignore.

58:28

Day is relevant.

58:29

This is your output, y, right?

58:31

I think now the story will be clear to you.

58:33

Why it is so important?

58:34

When you think from a data frame perspective, what you are saying now is that, hey,

58:39

I want to look at the last one-day data, last two-day data, last three-day data.

58:43

I want to look at one day-pile-ca-sales-kits-kittan, two-day-pre-a-sales-kit-h

58:47

how-tri-day-day-per-sales, how-h, three-day-day-a-sales, how-h, up to 100-day-ka-sales.

58:51

So based on all these features, and based on today, what it is, we want to predict what is the

58:56

current sales or tomorrow sales, whatever.

59:00

So this is a big picture idea.

59:01

So using lag, this is a very, very useful way to do feature engineering.

59:07

You are actually trying to create new features.

59:09

from the existing features. So, we have one case sales follow. You know, you here

59:13

here here the original data is, original data in only it. Time was and sales

59:17

that's it. It's it. It's not. Time series data is. Time series data

59:20

is. Time will be sales or time, or weather, time will, time, stock price, or whatever it is.

59:25

The data will be only like this. That is good. Now, we are trying to engineer more features

59:30

out of it. To get more, because this is we can't prediction not. It's very simple, right?

59:35

Time sales have come here. No. But from this data sales have come. No. But from this data,

59:39

Okay, now we're what we're.

59:40

Now we're like,

59:42

but this your sales time period T.

59:44

So, okay. So sales time period T minus 1.

59:47

Sales time period T minus 2, but now.

59:49

Just lag 1, lag 1, lag 2, like that.

59:51

So these are these all become features.

59:53

My point of discussion here is to tell you that all of these eventually become features.

59:57

I think, as I neatly summarized here, this is how it all relates to in the real world context.

1:0:04

Okay.

1:0:05

Same thing for rolling mean also.

1:0:08

rolling mean is similar thing. This is also a kind of a feature. So lag actually

1:0:13

our notes. I'm just trying to do. I just wanted to discuss this with you. So, you know, we only

1:0:18

have covered rolling mean, but that's okay. I think we can briefly we have covered. I think. So

1:0:23

rolling mean is what? Rolling mean is basically, uh, it is, it is also another extra feature that we

1:0:28

are adding. So if you look at it, that's a data frame and we are adding a new feature called the rolling

1:0:33

mean. Rolling mean is another extra feature that we are adding in the process.

1:0:38

That is another extra feature that we're adding in the process, rolling mean head.

1:0:42

Okay, and you can take a look at it. What is the rolling mean feature?

1:0:46

Rolling mean feature is nothing but we are looking at the last seven data points and based on that we are calculating the average.

1:0:56

Okay, so we are looking at the last seven data points and based on that, what is the average with the last seven data points.

1:1:04

So that is how we internally calculate what is rolling.

1:1:08

mean, okay, so you know, what is the, uh, yeah, so the, so the, so the, so the, so actually,

1:1:19

you know, what we have done here is we've actually dropped the NA features.

1:1:22

So, so I think it might be a little confusing, but what I can do is, if I, if I just comment this

1:1:28

out, it's for comment can't, it's, you can't clearly see. Actually, I'm here here here, actually,

1:1:33

we're actually, who NA features for drop here. So I think you might be a little confused,

1:1:36

that's what is. So actually, this data is so I think this is easier to understand.

1:1:43

But NANs, your models, whatever, but that's the reason why before we do machine learning,

1:1:48

we always try to drop the NSA. So that is what I did in the code here. But I think this diagram

1:1:53

will help you understand this in a better way. Okay, it's it's a whole clear

1:1:57

what you're going to. This is a time period T is. Is it? You know, it's your time period T minus one.

1:2:04

I mean, if you're looking at today, if you look at today's data, with respect to today's data,

1:2:10

that is what happened one day back. One day back, it's a price. With respect to this data, one day back

1:2:15

to thine. That's why lag's the value nan. Okay, so this is how we are able to see. And rolling

1:2:21

mean, what got? Rolling mean, you're looking at the last seven data points.

1:2:24

It's like that. You're looking at this particular row. With respect to this row, you look at the last seven

1:2:31

sales values. One, two, three, four, five, six, seven, seven, including.

1:2:34

this. Including this, you look at the last seven sales values, and you find out the average.

1:2:39

Because that is what rolling mean is. So, calculated, Nikalte, we can do this. We can do the math here.

1:2:44

So, Garthi, Sarsat. So, I think, approximate, calculated. So we can calculate it. 207. You can see this one.

1:2:49

207 plus 207.45 plus 198.12.12 plus 170.11 plus 2.11 plus 223.

1:3:04

445 plus 197.28 plus 404.8 plus 404.8.

1:3:18

Okay, so this all data points the addition is divided by 7. And this is what we'll give you the rolling mean.

1:3:23

And you can look at the number. It is 2.45.5.3. Approximately he because that both my decimal points are considered

1:3:28

not but you get the idea. So all that we are doing is we are adding up all these values.

1:3:33

we are adding up all these values and we are dividing by 7.

1:3:36

So for this particular data record, the rolling mean, the rolling average is coming as 245.5.

1:3:44

Okay.

1:3:45

That's what next what? Next what? You're going to this particular data point. What is the rolling mean with respect to this particular data point?

1:3:53

The rolling mean will again take into account.

1:3:55

Where from average data? When I was looking at this row, it was taking the average for the last seven points.

1:4:01

When I look at this particular row,

1:4:03

it will take the average all the way from 198 to this.

1:4:07

So it will consider this point and it will look at the last like total seven rows

1:4:11

average later including that.

1:4:14

Total seven rows including that.

1:4:16

It is two partisans.

1:4:17

So rolling mean is also an extra feature that we have added.

1:4:21

So but again, there are nans that we are getting.

1:4:23

Here there are nan queue are because if you look at this, it's the rolling mean

1:4:25

not going to because we are in the sixth row.

1:4:28

And if you consider this sales value, one, two, three, four, five, six.

1:4:32

Only six.

1:4:33

sales values I'm getting.

1:4:34

Seven sales values are not.

1:4:36

That's not.

1:4:37

There is no seven sales value we have.

1:4:41

So that's why the rolling minute is starting from here.

1:4:42

And that's why we have here.

1:4:43

And that's the way, we have here on the code

1:4:45

so to drop the features.

1:4:47

So the idea would be that,

1:4:50

uh, nan,

1:4:51

not a number.

1:4:52

Man basically means,

1:4:53

uh, it is like a missing value.

1:4:57

So Python man stands for missing value, right?

1:4:59

Isn't it?

1:5:00

Nan stands for missing.

1:5:01

We're missing value.

1:5:03

So, but then this kind of thing will cause issues when you're building the models.

1:5:07

So we're doing the real world in, we basically drop the NAs.

1:5:11

So this is the more appropriate time series data that you will enter into.

1:5:15

So,

1:5:16

as I explained to you, this is how we have created new features.

1:5:21

Lag one, lag two, rolling mean.

1:5:23

So we have managed to create new features on the basis of our data.

1:5:27

We have a new features made on the basis of our data.

1:5:30

All of you are you going to see this.

1:5:33

That's what rolling average basically is.

1:5:39

And there's a lot more, there's some more concepts that I will talk about, what exactly

1:5:43

it is and how it is useful.

1:5:46

So lag too useful and everybody can relate to it.

1:5:48

Lag is useful because we are looking at what happened one time period back.

1:5:54

We are looking at what happened two time periods back, three time periods back,

1:5:57

four time periods back.

1:6:00

That is what we have seen.

1:6:03

So that is the lag feature, very useful.

1:6:06

It eventually becomes features, right?

1:6:09

Rolling mean also acts like a feature.

1:6:11

If you look at rolling mean, rolling mean also acts like a kind of a feature.

1:6:15

Rolling mean is also like a feature.

1:6:18

So lag is also a feature.

1:6:19

Rolling mean also acts like a kind of a feature.

1:6:24

So it's kind of an average that you're able to create.

1:6:29

Our dummy values are dumped to nan values.

1:6:31

Huh, huh.

1:6:33

No, I mean, when I say, Shiva, I think what you are trying to say is, are we dropping the nance.

1:6:38

Yes, we are dropping the nance.

1:6:40

Because those NA values are not useful, right?

1:6:43

And you cannot build models using that.

1:6:45

So our work is over.

1:6:46

We have managed to create the lag 1, lag 2 and rolling mean feature.

1:6:50

Once that is done, you drop the nance.

1:6:51

That's it.

1:6:52

This is the drop any function that you have seen in your Python classes.

1:6:54

Okay?

1:6:55

The simple drop any is what I'm using right for.

1:7:00

And now, what we will do.

1:7:03

We will go back and as I told you, we will go back and we will do the modeling.

1:7:07

I think I told you that these eventually become features.

1:7:11

And this is where it all boils down to.

1:7:14

Now we are using this and we are trying to do machine learning, which we will see.

1:7:19

Now, there is one more concept I want to talk about with respect to rolling mean.

1:7:22

So lag is something again we relate to, but something more about rolling mean.

1:7:26

What exactly rolling mean is?

1:7:29

It's okay conceptually we understood the window like I'm average.

1:7:33

Why are we doing that? And you here here

1:7:37

here on a core term, it is clearly saying that

1:7:41

we use rolling means to smooth the noise.

1:7:47

This part we discussed, this part is sorted.

1:7:49

This part is sorted. That you can use rolling mean to create a new feature.

1:7:53

That ultimately feature is being. But this kind of what does it mean to

1:7:57

say smooth out the noise? Let us see that. Why do we say that?

1:8:01

So if you think about it conceptually, what happens is, if you look at the last, I think, again, I can maybe go back to Germany and show, let me generate this, you'll get a better clarity.

1:8:21

Just give me a second.

1:8:31

Thank you.

1:9:01

I'm trying to create an interactive visual so that people are able to

1:9:21

to let's do it very interesting and you can see it's a very noisy data set.

1:9:25

So they've set up a noisy data set up a noisy data set. Imagine it has a daily sales figure

1:9:30

or a fluctuating temperature sensor, whatever. I mean, so, but with, you know, with,

1:9:35

so what is, what is basically doing is it is trying to, the time series data is very noisy.

1:9:41

We'll see that in a moment, it's coming up. And you will, and you will see, this is your data,

1:9:47

right? Everybody is able to see the data. It's very noisy. Can you see? So this is exactly

1:9:51

what you're able to observe right now. This is, this is the data right now. You can see it's very noisy.

1:9:56

Very noisy. This is the original data. Okay. And, and, you know, and, you know,

1:10:00

And what is going on? Look at this. This is what is happening in rolling average.

1:10:05

When you do rolling average, this is what is going on.

1:10:09

And the interesting part is if I increase my window size, look at this. Can you see? This is what I

1:10:14

wanted to show you. Really cool. When I did I want to increase here and look at it. It's smooths out.

1:10:19

Effect is smoothed out. Can you see? The effect is kind of smoothed out.

1:10:27

I don't know if I'm able to explain.

1:10:30

in this perfectly. What I can do is let me take a slightly bigger range.

1:10:32

So if I take window size equal to one, window size equal to one, window size equal to one is nothing

1:10:37

for the original data itself. Window size one, basically means that you have this particular

1:10:43

row or you have that window size one is like taking the point itself. So the smaller the window

1:10:51

size, you are taking the individual points. So you're back to the same noisy story. Data points

1:10:56

are going like this. It's the same noisy story that we discuss. Data points are like this.

1:11:00

points I'm looking. So if your window size is very small, you're, you know, you're like

1:11:06

considering individual points. So then you're looking at all these small, small fluctuations.

1:11:11

So you're going to understand the trend. What I'm getting at is we do rolling average to understand

1:11:16

the trend. Rolling average, meaning average. That's we're going to say, we're trying to, on an

1:11:21

average trend care. Now, if you increase the window size, now, if you increase the window size,

1:11:25

we're doing, very interesting. We're going to increase it. It's very interesting. We're

1:11:29

Windows size is increase? What does it mean? Moving average 40

1:11:36

means 40 day moving average? That means 40 day moving average. That means I want to look at the last

1:11:40

40 data points. I want to look at the last 40 data points and I want to go back and I want to

1:11:46

look at the last 40 data points and find out the average. We'll make a average point

1:11:51

take that 40s, then after 40 data points, one average we can start to see. You can

1:12:01

start to see that we're 40 data points average and plot it. Let me show the animation. This

1:12:06

observe it. Look at the number of fluctuations right now. If we're here we window size 2

1:12:12

you make you make you look at how little fluctuations are. Can you see? See the fluctuations? Look at the

1:12:18

fluctuations. As good as the individual points only. This is what I wanted to demonstrate. This is what I wanted to

1:12:21

demonstrate. Now we have this window size 40s are smooth out. You're plotting only the

1:12:28

40 day average is right now. You're getting a better understanding that by trend care. This is this is what

1:12:34

we started our session with today. We were talking about stock markets and why trend is important.

1:12:39

And you're able to see this trend. On an average, what is the pattern that is playing out.

1:12:44

I hope the animation will be helpful. And this is exactly what we are adding as a feature. So next

1:12:51

you're looking at a particular row and you're looking at the sales data. You are trying

1:12:55

to understand not only the sales data at that particular time period, but you're also trying to

1:13:00

understand. So you're not only trying to understand that, hey, what is the sales value at that particular

1:13:05

time period, but you're also looking at the T minus one sales value. You're also looking at the

1:13:10

T minus two sales value and you're also looking at the average, the rolling wheel. So, so I repeat again,

1:13:17

you're tracking the T minus one sales value, lag one.

1:13:21

you're tracking the t minus two sales value lag two and you're tracking the rolling average and this is giving an idea of the trend he okay seven days overall what is the trend and this is very very useful and as I told you in the larger context these will eventually become features and this is this will be part of my next conversation so we will you know which we'll circle back in a moment this is be part of my next conversation where we will go back and use all these as features and build a model okay and as I told you like you can see in stock

1:13:51

markets also this is this is so popular I mean so the concepts of 30 day moving average 200 day moving

1:13:57

average so they are very very common in stock markets okay up you here at 10 sex search for a stock

1:14:03

market so if you see in fact if you you have 30 day moving average type correct then you

1:14:07

type stocks but it is so popular moving average is so popular in stock markets that they are

1:14:14

used they are used to identify buying and selling opportunities because you want to understand

1:14:19

the long term and short term prints

1:14:20

if you want a long-term trend up window size

1:14:23

because the bigger the window size the more

1:14:27

smootening effects you're actually getting that's the intuition and you can see zero

1:14:32

there are there are a lot of charts you will find which tells you uh you know

1:14:40

different types of moving averages you're actually explained be here very nicely they've

1:14:43

explained a moving average also so this kind of technical

1:14:47

because they've gone into concepts like uh

1:14:50

you know markets and all but what i wanted to highlight in this example is that it is it is an

1:14:57

important thing that is used in the real world also moving averages are actually used in the

1:15:02

real world whatever we have seen here now what we will do we will use this entire context

1:15:09

and we will go back and build a linear regression model

1:15:12

now we go back our usual machine learning on this why we understood about time cities

1:15:18

we understood about the different features we are creating

1:15:20

So specifically we have two features

1:15:23

we created a lag feature and we also created a rolling window feature.

1:15:28

These were the two specific features that we created. So we created a lag, you know, a lag feature

1:15:34

and we also created a rolling window feature. These are the two features that we have

1:15:38

explicitly created here. Okay, now let us continue on and let us finally use all these as

1:15:46

inputs that I told you we will eventually use all these as the input and

1:15:50

access these are features you know are therefore so this is what we will do these are all my

1:15:55

features these are all my excess and based on these axes we will try to predict this

1:16:00

why that's the solution that we are going to solve so based on all these input

1:16:05

accesses we are trying to predict what is the sales why that's the way how we are going

1:16:09

for it okay so that is what we are going to be doing so so before i continue on everybody

1:16:17

think this is something i encourage everyone to like uh

1:16:20

do until here so i've already shared this code file with you so before i start with this section

1:16:26

number six all of you please open up the code file up some eight june folder my job please open up

1:16:31

your code file okay and please run the snippet until here

1:16:34

here so if you're all given to comfortably see the uh uh the code okay all of you please

1:16:41

run until here and then we will together to the hand down six six

1:16:45

am sure you just going to give you uh maybe five minutes just to run the thing until here okay

1:16:50

then we will see the next part all if you just execute until now

1:17:20

you know

1:17:50

you know

1:18:20

I'm

1:18:50

I'm

1:19:20

If you guys are all able to

1:19:32

you can just write a quick.

1:19:34

You can just write a quick yes on chat.

1:19:36

This is easy.

1:19:38

I mean, simple.

1:19:39

There's no data set we are loading.

1:19:40

Just taking a sample data set we are just taking a sample data out straightforward.

1:19:45

The focus is more on the concepts.

1:19:46

There's another data set that I will take up shortly.

1:19:49

So after the main.

1:19:50

concepts are out of the way. We will see another very interesting, a more real world air

1:19:55

passengers data. That will be the next part of my conversation. Just going to give you a few more minutes.

1:20:20

Thank you.

1:20:50

Thank you.

1:21:20

Thank you.

1:21:50

Thank you

1:22:20

Thank you

1:22:50

Thank you

1:23:20

Thank you

1:23:50

Thank you

1:24:20

Thank you

1:24:50

All right.

1:24:54

All right.

1:24:57

So now, I hope everyone

1:25:02

to the next

1:25:04

now we'll continue to the next phase and we'll actually

1:25:06

we'll actually build a model.

1:25:09

As I was discussing before,

1:25:11

the main objective of this

1:25:13

the main objective of this particular step was what?

1:25:15

The main objective of this particular step was we were able to create features.

1:25:19

Right?

1:25:20

Just to show you once again, this is our entire set of features we have managed to create.

1:25:25

Okay? And now we will take the data. We are separating what is the X and what is the Y. This is the actual modeling part. We will see.

1:25:34

And back to our all familiar machine learning territory. Nothing changes here. This part is very, very similar what we have discussed.

1:25:41

And we will do the train test split. And I told you, we will do a chronological split. Very important. And one of the ways you can do

1:25:50

do what this is we will use something called shuffle equal to false. Now, we did not do this before because the default of train test plate is always shuffle equal to true. Can you see? If I hover over over it, you see the train test plate

1:26:01

arguments and you can see that at the top shuffle is always equal to true. That is what we have been doing all this while. So whenever we were doing train test split, by default, it was shuffling. It was no particular order that has been maintained. But here we are explicitly saying for time series shuffle equal to false. So we are saying, hey, you know, like 80% of my data,

1:26:20

in that order is part of my training and the remaining 20% of my data in that order is part of my testing.

1:26:28

So 80% of my data in that order is part of my training and the remaining 20% of my data in that order

1:26:34

is part of my testing. That's the way to look at it overall.

1:26:46

And now on the basis of that, we will go back and build the model.

1:26:50

We have got X-Y. We have done the train test split. And now we are also going and dropping the day column, actually. The day column is not that useful. But the day column is what we are dropping because we anyways have the sales figures, the sales numbers we have already. And now here is linear regression. LR. Dot fixed X-ray and we are getting the score of linear regression model. You can clearly see linear regression is giving us 92% in training, 87% in testing. Not great, but we are getting a decent result.

1:27:20

And next, back to the machine learning ideas.

1:27:24

We are taking the same data and this time we are fitting gradient boosting regressor.

1:27:30

NST matters equal to 100.

1:27:31

NST matters now, now we know, now we have done that random forest module.

1:27:34

NST matters is the number of decision fees that are, there are, it's a hyper parameter.

1:27:39

So with gradient boosting is a more powerful model and for the same data, again, gb model.

1:27:44

Gb model dot fit, gb.gb.org, we're getting the train and test scores and we're getting a 94% accuracy.

1:27:50

So we're getting a better accuracy for gradient boosting.

1:27:53

And more important than that, what I wanted to clarify in this entire conversation is that

1:27:57

the machine learning approach remains very, very similar.

1:28:01

And you can see the, this is the pictorial representation that I've done.

1:28:05

So this whole thing is part of my train data.

1:28:07

And here, on the right inside, you can see the actual test data in black.

1:28:12

And you can see what the linear regression predicted and what the gradient boosting predicted.

1:28:18

I think here it is not that easily understanding.

1:28:20

but you can make out to some extent that, you know, the gradient boosting is actually the green.

1:28:25

The green is very close to the black because we saw that when we build the model with gradient boosting,

1:28:31

that gradient boosting model is able to forecast more accurately.

1:28:34

And forecasting always happens on test.

1:28:37

That's the whole idea, right?

1:28:38

We always fits the model on the train data.

1:28:40

And with whatever model we fit on the train data, you know, on the train data, that means the last 120 data points,

1:28:47

we want to use that to predict what will happen in the next 20 data points.

1:28:50

So we already know that ground proofs test data.

1:28:53

And on that, we are using gradient boosting to predict forecast and we are comparing.

1:28:57

So gradient boosting is giving us a higher test accuracy.

1:28:59

So you can see the predictions and the actuals are very close in gradient boosting.

1:29:03

Okay, you can see the linear regression is yellow.

1:29:05

Yellow is a lot of way off.

1:29:07

Can you see it's very peeking up, but the green and the black are kind of going in tandem.

1:29:12

So with gradient boosting, we're getting a much better result comparatively.

1:29:15

But we can make it even better.

1:29:17

So this is the business use case of what I wanted to.

1:29:20

where it all boils down books.

1:29:22

So create new features, build a model, try linear, tri-gradient boosting, and get the scores.

1:29:28

So this is back to the machine learning territory that we talk about.

1:29:31

And as I said, in the more real world scenario, we will not just have lag 1, lag 2,

1:29:35

and rolling mean 1.

1:29:37

There will be hundreds of features.

1:29:39

What you are seeing here, as I told you, they'll be like lag 1, lag 2, up to lag 100.

1:29:43

And rolling mean 30, rolling mean 50, there will be like 50 different rolling means that you will have.

1:29:48

So that is how we do it.

1:29:49

There will be so many.

1:29:50

features that we will be having in practice. So, but this is just to show you at a smaller

1:29:54

scheme how it looks like. Okay, I hope everybody is clear. Next up, what we will discuss

1:29:59

is we will discuss about different evaluation methods. We have already talked about it.

1:30:03

I think this is, so, so one thing about time series is very similar to regression.

1:30:08

Because ultimately, what are we trying to do? We are trying to predict a numerical value.

1:30:12

We are trying to predict a number. Right. So next data point, what that numerical sales will be.

1:30:17

Next data point, what that numerical stop price will be. They're trying to predict

1:30:20

the numerical value. So these are the evaluation, you know, methods that you have here.

1:30:25

What are the different evaluation methods? Okay. We will see that. And after this, we will see

1:30:30

another case study. I've got another very nice case study where I have done this whole thing on a different

1:30:35

data set. So those are the two things that we will see. But we can take a short break right now.

1:30:40

Okay. So we are at 918 and the clock. So we can take a quick 10 minutes break.

1:30:44

Circle back and we will complete the evaluation methods and then from there we'll go to another case study.

1:30:50

where we will use all these methods taken together. Okay. So guys, once again, all the

1:30:55

materials are in the 8th June folder. Okay, you can refer on to it. Okay? So let us take a break and I will

1:31:02

see you back after a 10 minutes break.

1:31:20

Thank you.

1:31:50

Thank you.

1:32:20

Thank you.

1:32:50

Thank you.

1:33:20

Thank you.

1:33:50

Thank you.

1:34:20

Thank you.

1:34:50

Thank you.

1:35:20

Thank you.

1:35:50

Thank you.

1:36:20

Thank you.

1:36:50

Thank you

1:37:20

Thank you

1:37:50

Thank you

1:38:20

Thank you

1:38:50

Thank you

1:39:20

Thank you

1:39:50

Thank you

1:47:50

Okay, welcome back all of you.

1:47:55

will continue on we'll continue on and we'll continue on and we will continue on and we will look at the

1:47:59

different ways how we can evaluate the model now.

1:48:02

So before the break we talked about different about different aspects of different aspects of how we can build the time series model.

1:48:10

So we talked about the concept of trend we talked about the concept of

1:48:15

of seasonality.

1:48:18

We also understood how to create additional features. So additional features were, we created, you know, the lag features. We also created the rolling average. We understood what is rolling average. And we also discussed the 30 day moving average, 200 day moving average. What is the benefit of it? The benefit is that they are able to reduce the, they're able to primarily reduce the overall

1:48:48

noise. So whatever internal fluctuations are happening in the data, those fluctuations reduce reduce.

1:48:57

So they're able to reduce the overall noise.

1:49:01

That's the intuition.

1:49:03

Now moving on, what are the different ways we can evaluate the model and we also finally went and built the models?

1:49:15

The evaluation metrics remain very similar.

1:49:17

very similar. So we have R squared. R squared obviously is the general evaluation

1:49:24

metric that we use for regression. But here we will also discuss something called MAPE. You've

1:49:31

already seen MAE and RMSE before. Now we will see something called MAPE. And MAPE stands

1:49:36

for mean absolute percentage error. So we use something called MAPE which stands for mean absolute

1:49:43

percentage error.

1:49:47

So, let us see what MAPE tells us and what is the broad idea behind MAPE.

1:49:58

So the official definition is nothing but it is the prediction error expressed as a percentage of the actual value rather than in absolute units.

1:50:12

All the other error metrics that we have discussed before in our regression modules.

1:50:17

they are always expressed as actuals but if you look at MAPE it is it is nothing but actual minus predicted divided by actual into 100 that is the formula for MAPE

1:50:36

so for example let's say on day one the actual sales is 100 I'm just giving an example right now let's say on day one the actual sales is equal to

1:50:47

100 but the predicted sense is coming out to be equal to 110 so the actual

1:50:53

sense is equal to 100 the predicted sense is coming out to be equal to 110 what is the error

1:50:58

percentage how do we calculate that it is actual minus predicted it is the modulus of that mind you

1:51:05

the sign does not matter it is the absolute value so this particular thing stands for modulus absolute

1:51:11

value so 100 minus 110 that is 10 by 100 into 100

1:51:17

10% there's a 10% error rate. So we are not trying to take the absolute value,

1:51:25

but we are looking at the percentage value. It is giving us a percentage comparison. Next day,

1:51:31

let's say the actual ground truth value for day two sales is 200. Imagine this is my test

1:51:40

data and whatever model we have built, that model is giving us 190 sales. So what is the

1:51:47

error well 200 minus 190 10 by this into 100 5% there's a 5% error so that's the way

1:51:55

how we can look at it obviously the higher the MAPE the more the error that is obvious and remember the

1:52:03

other things we we talked about already are there like for example R squared is the way to like typically

1:52:08

more the R squared lower the MAPE because more the R squared more accurate the model is so lower the errors will be so

1:52:16

so that pattern anyways holds through here also and you can compare the same thing for our

1:52:22

current exercise as well what we did for the linear regression model so here you know we are seeing

1:52:27

the the individual data point errors but what we do in reality is we do the average it is the

1:52:33

average of that that is mean you know absolute percentage error so we calculate the absolute

1:52:39

percentage error for the individual data points and then we take the average of that so here we

1:52:44

calculate it for this point for second point for third

1:52:46

point, then we take all the three and we average it out. So we get a single average value.

1:52:52

So we can say 7% means the predictions are off by 7%. So in our exercise, obviously with linear

1:53:02

regression, the MAPE is 9.67%. And with gradient boosting, obviously, we built a better model.

1:53:08

We saw that already. The R squared was higher and naturally the MAPE is lowered. So that is also something

1:53:14

that we can relate to.

1:53:16

So now what I will do is I'll go on to another exercise.

1:53:21

So this is pretty much the concepts that we have here over on.

1:53:25

And now we will go back and look at a couple more concepts.

1:53:33

And again, just wanted to summarize the conversation between M-A-E-R-M-M-M-A-C and M-A-P-E.

1:53:45

So M-A-P-E is.

1:53:46

is very, very good when you're comparing across multiple scales, right? I think this is just a small

1:53:52

summary that is given here. You can see. So MAE mean absolute error is when all errors are equally

1:53:58

important. But RMAC, if you remember, RMAC is basically squaring the error. So RMAC, the large

1:54:05

errors are typically more costly. I'm just trying to just trying to mention this. Again, we have seen

1:54:10

this before, don't want to confuse you. So today's main idea was MAPE, but you can actually

1:54:15

compare MAPE with the other metrics also. Okay, by and large, they will give you the same interpretation.

1:54:21

But as I said, with MAPE, you're able to compare across different scales, like especially for

1:54:26

time series, it works on very well. Because it is the percentage metric. These are not percentages,

1:54:32

but this is the percentage. So the units are removed. Units are not there. So that's why, you know,

1:54:36

we can use it to compare across different scales. That's the main thing. And now what I will do is,

1:54:43

I'll take you back to another, another very interesting case study we have here.

1:54:48

This is the air passenger case study that we have. Okay, we'll see that.

1:54:53

So let us see the air passenger's case study.

1:54:59

So you don't have to solve it. I've already solved it for you. Let me take you through it.

1:55:06

And related to that, I've also given a air passenger CSV dataset. I'll download that.

1:55:13

And this is my data set that we are able to see on the screen. Okay. I will quickly

1:55:20

upload the CSV file on my solution notebook. We'll quickly do that. This is the pretty old

1:55:30

data set. We are looking at the air passengers demand from January, 1949 to January, 1960.

1:55:39

So last six year, uh, 12 years worth of data.

1:55:43

is what we are tracking right now.

1:55:47

So that is the air passengers data that you have here.

1:55:53

So if you want to get a sense of this data sets, this is what it basically tells you.

1:55:59

It tells you the total number of passengers traveled on that particular month.

1:56:04

How many passengers traveled on that particular month?

1:56:08

So let me upload the dataset first. I will upload the air passengers.

1:56:13

data, CSV fine. Straight forward and we will load the data site. And first things,

1:56:21

first based on the concepts that we have studied, you can make out that this is a time series

1:56:26

data. Why is this a time series data? Because every row stands for a particular time period.

1:56:34

We are looking at January, 1949, February 1949, March 1949, and so and so forth. Every

1:56:40

row stands for a particular time period. Everybody is very.

1:56:43

me and we are also tracking the passenger demand the passenger demand is actually in

1:56:49

and in in 100,000 you might be wondering like only 112 people voted uh you know two flights that

1:56:55

here not off the store but yeah i mean it's like 112 000 118 000 132 000

1:57:02

129 000 okay it's in thousands but obviously the number is much smaller than what we have today

1:57:11

and if you look at your data set this is how you're

1:57:13

data looks now. This is a beautiful time series that I've plotted, a line chart that you

1:57:19

have plotted and you can see x-axis we have the time. So you have got data for different months,

1:57:28

right? This is like 1949, February, March, April, May, June, July, August, September,

1:57:33

October, November, December, and again, 1950, January, February, March, April, May, June,

1:57:39

July, August, October, November, December. And again, 1950, January, January, February, March, May, June, July, October,

1:57:43

again, 1951, which starts from here. Very interesting. You, you're, I think in this,

1:57:49

in this exercise, you're able to see all our ideas getting demonstrated very nicely.

1:57:54

First things, first, you're able to observe the concept of friend very nicely. We're able to see on an

1:57:59

average what is happening. You're able to clearly see, on an average, the air passengers, the air passenger

1:58:05

demand is increasing over time. As the month's progress, as time increases, you're able to see that the

1:58:12

the number of air passengers are are increasing over time. So the trend is on an average

1:58:17

positive. We are seeing a positive trend, you know, a higher trend. On an average, if you see,

1:58:24

it is increasing. On the same lines, there is seasonality, and that is the thing that we understand for

1:58:29

airline data. There's a very clear seasonality, even if you see, that typically, January, February,

1:58:36

March, April, May, June, July, August, September, October, November, December, December, December.

1:58:42

December, it falls drastically. So every time you're looking at this data, every time you go

1:58:48

all the way to December, it falls drastically. At least November, it falls drastically. November,

1:58:52

December or the period when it falls a lot. And the peak is usually around July August.

1:58:57

July August is when it's typically the peak. The highest airline demand is a seasonal pattern

1:59:04

across all the years. And if you look at it, it started all the way from 1949. You look at 955 data, 56 data,

1:59:11

57 data, all the years if you see, yeah, the fluctuations are a little different, but by and

1:59:18

is the same seasonal pattern you will see. There's a beautiful seasonality we are able to

1:59:23

see in the data. Now, moving on, I will, I will quickly go ahead and, take the, do the dummies right

1:59:40

now. Why am I doing this? Because we want to incorporate the months parts correctly. So,

1:59:47

that's my data set. So because the month is otherwise considered as January, February,

1:59:52

March, like that. It is a categorical column. So, uh, we have discussed something called

1:59:57

one hot encoding. All of you know. So January, February, we are creating dummy columns for those

2:0:02

months. That's it. Nothing new we have done. We already have this data. So that means, uh, we have the

2:0:08

time index. We have the number.

2:0:10

number of passengers. This is the general thing to be eventually drop this one, but the time

2:0:15

index will tell me, we'll go from one all the way to 144. And this is a month's, the dummy columns

2:0:23

that we have created. So I think this particular row corresponds to January. Next row corresponds to

2:0:27

February. February is one rest are all zero. Next row corresponds to March. This is a simple one hot

2:0:32

encoding or dummy encoding that we have done. We discussed this long back in our machine learning

2:0:37

sessions, data pre-processing sessions, if you remember.

2:0:40

Okay. So next up, what are we doing? Now we are doing the actual machine learning.

2:0:46

So we are dropping the passengers column. Everything else is part of my X and this is part of my Y.

2:0:53

Okay, everything else is part of my X and this is part of my Y. So frame test split and linear

2:1:00

regression. We're building the model and we are calculating the scores. So you can take a look at it.

2:1:06

Okay, I think I think this particular

2:1:10

date time we have not removed it actually. So we need to remove the date time. And once I

2:1:15

remove the date time, it should work. Just give me one second. The reason is because I actually

2:1:20

did not remove this particular part. Can you see? We did not actually remove this particular month

2:1:25

column. So I'll just use the Jeveny feature to correct that error. And you have to drop the month

2:1:30

column. So I'm not only going to drop the passenger's column, but we will also drop the month column. Why?

2:1:35

Because the month is already, the month information is already taken out. We don't. We

2:1:40

don't need this column. Okay, so it will fix it for me. And the rest of my code should run

2:1:44

absolutely fine. You can see. So yeah, the code is successful now. So with linear regression,

2:1:50

we are getting 95% train R squared and 62% test R squared. Not the best results I'm getting,

2:1:57

but I think we will take that. We will take this result. And next, what I will do, I will go and

2:2:03

plot it out. I will go and plot it out just to see what type of, you know, results we are getting

2:2:09

with linear regression. Okay. So the same way that we were doing this before. So here also we can,

2:2:14

we can go and plot it out just to, I think, understand, you know, what type of results we are getting

2:2:19

with linear regression. And obviously, we can now repeat using the gradient posting regressor also.

2:2:28

That's a that's true. Okay. Yeah. So I hope everybody's clear. Everybody's, you know,

2:2:34

got a sense of how we are, how we are approaching time series. So this is the simple linear

2:2:39

regression model we have done but if you want you can obviously go and do this using gradient

2:2:43

boasting so again what is the what is the what is the benefit what have we what have we done here we

2:2:48

have simply taken the data as it is there it is time month and these are the one hot

2:2:56

encoded columns that have created for the month okay and these are basically all my input

2:3:02

access and based on that we are trying to predict what is the output once just to clarify these are all my

2:3:08

input x this is all my Xs and based on that we are trying to predict the Y this you can

2:3:13

ignore this we have eventually dropped so that's that's how my that's how i'm formulating the

2:3:18

machine learning problem x and Y based on these Xs we are trying to predict this one okay i

2:3:26

hope everybody's clear and here we have done this with linear regression and next what you can do

2:3:33

you can absolutely use gradient boosting let me just try this with uh with gradient boosting

2:3:38

nothing will change i will keep the rest of the code as it is exactly the same i think

2:3:44

i have not imported the gradient boosting package let me see from sk learn dot ensemble import

2:3:51

gradient boosting uh gradient boosting regressor i will just go i think i just made a spelling mistake

2:3:59

ensemble it will be import gradient boosting regressor there it is okay that's it perfect

2:4:08

and now what i will do is uh i will instantiate uh gradient boosting

2:4:14

regressor and here uh rest of the part remains exactly the same nothing changes i'm

2:4:23

keeping the default model and you're able to see with gradient boosting what type of results we're

2:4:26

getting obviously you need to use nstimators nhtmater's uh hyper parameter needs to be used

2:4:31

but with a little bit of tuning you should be able to get uh uh uh uh uh recently

2:4:35

really good performance okay so that is the uh iteration the same way how we did last time

2:4:40

same way we can try it out here and we can see with gradient boosting uh you know what type of

2:4:44

results be on that video so this this this this ml part remains very very similar now that you

2:4:49

understand the crux of what it is the rest of the machine learning part remains very similar

2:4:54

and now you can add other features maybe maybe now the challenge would be that hey like okay we have

2:4:58

got time index we've got month and all that but can we go back and add uh lag features can we go back and

2:5:04

try to add some lag features you can do that maybe that could be the next exercise so now

2:5:08

you can you know the same way that we did in that last case study now you can additionally

2:5:14

create lag features okay so we've got passengers data and now you can additionally create lag

2:5:21

feature you can say okay i want to create a feature lag of one lag of two like that

2:5:28

so they will additionally become features in their in your dataset you can do that and and generally

2:5:33

these features will help you generally to build a better quality model so the overall

2:5:39

quality of your model will be better if you use these kinds of features generally the

2:5:44

quality of your model will be usually better so that's just one thing to keep in mind so overall

2:5:49

you will have a better quality model generally still okay fine guys everybody's with me

2:5:56

so this is pretty much about about the session today any questions i hope all of you follow

2:6:02

along what we talked about it was a it was a lighter session it was a lighter session

2:6:09

compared to the other topics which were very exhaustive but it was a lighter session comparatively

2:6:15

which allowed us more time to get into another case study and talk about it but most

2:6:20

importantly we wanted to give you an idea of time series what time series is so that all of you

2:6:26

are able to are introduced to a different philosophy a chronological philosophy in terms of how to work with

2:6:32

data okay all good any questions that is fun in time

2:6:40

everybody's clear so i've already uploaded the files here this is the solution

2:6:44

file and this is the demo file and also very interesting i've also given a couple of

2:6:49

resources something i absolutely encourage people to go through in your sessions

2:6:55

towards the end of my notebook if you see i've given you some gaggle

2:6:59

references in terms of some data sets

2:7:02

and the same way that i did this case study for you the air passengers one i will absolutely

2:7:07

highly recommend you if you can use a bit of jemini feel free feel free to use a bit of jemini if you

2:7:13

want but try to solve the problems so very interesting we're looking at a store a store

2:7:20

item demand forecasting challenge this was a challenge and the problems on it's to predict

2:7:28

three months of items sales at different stores and this could be so useful for uh

2:7:32

different companies right imagine you're a retail store and you want to i you know estimate

2:7:38

how many items will be required something that everybody's doing the uh your swiggy insta mart is

2:7:44

doing amazon is doing in their warehouses the same forecasting is a very real problem

2:7:49

because if you're not able to forecast correctly how do you know how much of stock to keep in your

2:7:53

inventory so very real problems so this is the interesting one

2:7:58

fly match time series data is an interesting one you can take a look at that also

2:8:02

this is the you're looking at deli data 2013 cellyk 2017 you're looking at deli's data

2:8:09

and you can you can see some interesting things coming out of this also so this is the

2:8:14

climate change data that we are looking at electric production time series predict electricity

2:8:19

consumption and then be a lot of very strong seasonality will be there in this data i think we can

2:8:24

understand if the electricity data may what will happen is there are certain uh months of the year

2:8:30

if you look at indian context only i think the summer months electricity uses that is highest there's

2:8:35

no doubt right like winter india typically people don't use heaters so other parts of the world

2:8:40

heaters are more common but here like okay summer aces are very normal so the electricity

2:8:46

consumption it shoots through the roof during uh summer season in our country okay so naturally

2:8:53

there'll be a very strong seasonality in the data on an average as a trend the electricity consumption has

2:8:59

increased over time electric production is also increased over time but you will clearly see a

2:9:04

seasonal trend there are certain months of the year when it is very high organic drops so that is

2:9:09

an interesting thing walmart sales forecasting the same retail store use case i mentioned

2:9:13

and again based on historical data this is with respect to the bitcoin asset but you can take

2:9:18

any other asset this is a very interesting data set you're looking at uh one minute interval

2:9:24

data or bitcoin so i'm sharing just with bitcoin but you can do this with any other financial

2:9:28

asset stock market hogea you can talk about mutual funds you can talk about gold you can talk about

2:9:34

real estate bitcoin so the same ideas will work out and this will be very you know very interesting

2:9:40

see if you can actually at least build a baseline model i'm not asking you to build a perfect model

2:9:47

that will predict everything correctly that's not the objective but at least use some of the

2:9:51

ideas from this session uh go back to the demo notebook that i shared with you and try to

2:9:56

build linear regression try to build gradient boosting the same data set you'll get a lot of

2:10:00

confidence okay and it's very simple it's a simple c sb find given to you and you can work through it okay

2:10:08

all right guys these are again references that i wanted to share with you and uh

2:10:12

that pretty much uh wraps up the session for today and today as i told you it's been a lighter

2:10:17

session comparatively so we talked about trend versus sensality that was the main

2:10:21

topic uh time aware splits why it is important to split the data in a chronology

2:10:26

order what is the relevance of that we use shuffle equal to faults if you remember

2:10:30

that was another important concept we talked about rolling windows and also

2:10:33

additionally i covered about rags lags so these are the additional features that we talked about right

2:10:38

what is rolling window what is lag why it is important and finally how do we evaluate time series

2:10:43

models okay so we also went a notch further and we build some time series

2:10:50

machine learning based regression models and we were able to finally also evaluate those

2:10:56

models what kind of accuracy in our squares we're getting so that's pretty much the contents

2:11:02

for the session okay guys uh so that will be all from my end thank you everybody so over to preck

2:11:12

who will carry on with your with your quiz and the multi meter quiz thank you everybody

2:11:20

Yeah, thank you, sir, for the lecture and thank you students for attending.

2:11:26

Now I will launch the feedback poll and then after that it will be the MENTimeter Quest.

2:11:35

So just give me a minute.

2:11:50

Okay, I'm sharing the Mentiator link here. Please join the Mentiator

2:12:08

quiz. I'm sharing the Mentiator quiz. I'm sharing the screen. Just give me two minutes. I'll start.

2:12:20

Thank you.

2:12:50

Hello. Yeah, okay. All right. Players please quickly. I am ending the poll.

2:13:09

Everyone has voted it seems. Okay, seven players, all right. I am going to start because I need to hurry.

2:13:20

All right.

2:13:24

Started the quiz.

2:13:27

What does seasonality represent?

2:13:31

So I'm in a bit of hurry, so I would appreciate if you guys like answer quickly today.

2:13:37

I mean usually you guys are very quick.

2:13:43

Let's go.

2:13:46

What does seasonality represent?

2:13:48

Pretty simple question.

2:13:50

Actually, covered by S.R. many times. I'm not expecting anyone to get this wrong.

2:13:57

Oh. So seasonality means repeating patterns. It does not mean long-term growth at all. So people who are like, if this was a guess, then all right. Okay. Let's see. All right.

2:14:20

Next question.

2:14:24

Starting. Okay.

2:14:32

Which metric gives percentage error?

2:14:38

So, I mean, this one is very easy. I'm not really everyone should be able to answer this.

2:14:45

The options make it.

2:14:49

it obvious almost.

2:14:51

So yeah.

2:15:03

All right.

2:15:07

Yeah.

2:15:08

So MAPE, that is the P.E stands for percentage. So that's why I said the options make it pretty obvious.

2:15:14

All right.

2:15:16

Moving on.

2:15:19

Okay, next question.

2:15:27

Uh, okay, seems you have lost a player. All right.

2:15:39

What happens if future rows enter training?

2:15:47

This is something.

2:15:48

This is something that we have seen many times in the past also.

2:15:51

It's an example of...

2:15:58

Harsh, don't worry, the poll is not for, like,

2:16:01

so don't worry about it.

2:16:03

Even if you don't mark the poll, it's fine.

2:16:06

I'm not, I can't release it again

2:16:09

because otherwise every, all the results will have to be redone.

2:16:14

And then some people have already left, so can't do it again.

2:16:17

can't do it again.

2:16:19

Maybe next time, okay?

2:16:21

Awesome. Most of you did get it correct.

2:16:23

Future leakage is the correct answer.

2:16:25

Yes, it is, it's not overfitting.

2:16:27

It is a leakage. It's a leakage problem.

2:16:29

Right?

2:16:30

We've seen it multiple times in the past.

2:16:36

All right, it seems further isn't back in the game.

2:16:41

Okay. Shake is leading.

2:16:46

leading

2:16:48

seven

2:16:51

I thought there were eight people.

2:16:55

Okay, fine, I'll just start.

2:16:58

Last two questions.

2:17:01

Which feature best captures recent volatility?

2:17:16

So, yeah, this is also something that Sir covered, actually.

2:17:33

I mean, he showed a demo with this.

2:17:37

So, yeah, recent volunteer.

2:17:45

recent volatility, right?

2:17:47

So it is the, uh, let me just actually confirm it.

2:17:51

One second.

2:17:53

I'm, I'm pretty sure it is a rolling standard.

2:17:57

Just give me one second.

2:18:02

Yeah, which features, best captures,

2:18:08

recent volatility is a rolling standard.

2:18:11

So, yeah, all right, no problem.

2:18:15

Last question of the day.

2:18:22

Okay, all right.

2:18:28

I think I got it.

2:18:29

Nice.

2:18:35

Okay, yeah, okay.

2:18:37

All right.

2:18:38

Last question of the day.

2:18:39

This one is related to lag, actually.

2:18:42

Why are lag features useful?

2:18:44

So these are lag features.

2:18:53

What are features useful for in general?

2:18:57

I think this is like, okay, yeah, people have already looked at all right.

2:19:11

Yep, they encode past behavior.

2:19:13

All right.

2:19:14

With that, the quiz is completed.

2:19:16

I think...

2:19:18

I'm not sure.

2:19:20

Probably Arnika has won this one.

2:19:22

Again.

2:19:24

Alright, yeah.

2:19:25

Congratulations, Arnika.

2:19:27

And with that, we are at the end of the session.

2:19:30

I will see you guys on Wednesday.

2:19:32

Have a good night.