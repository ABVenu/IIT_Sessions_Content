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

Hi, everybody, very good evening, all of you just start on here, a few minutes.

11:40

I hope all of you are starting out with a good exam.

11:42

Yep.

11:43

So we are starting out with a.

11:46

a new topic and I will just wait for a few more minutes to allow everyone to join it here.

12:16

Thank you.

12:46

Thank you.

13:16

Thank you.

13:46

Thank you.

14:16

Thank you.

14:46

Thank you.

15:16

Thank you.

15:46

Thank you.

16:16

Hi,

16:20

Good evening.

16:21

Hi, good evening all of you all of you.

16:34

Good evening all of you.

16:46

Thank you.

17:16

Thank you.

17:46

All right. Hey, guys.

17:55

So let's start on.

17:55

I was just waiting to check if people join in because today will be a very, very new session.

18:02

And, you know, I just wanted to ensure everyone's everyone's in the class.

18:07

And one of the thing that we are also trying to, you know, very actively do in the classes now is we are trying to stick to the timings in a big way.

18:16

So I think I want to ensure we start on time, we end on the time limits.

18:19

So, you know, yeah, so my request is, like, all of you please do, like, please do, like, try to join on time because, yeah, especially for the people who are early, I really feel bad because I, I'm, you know, I'm trying to keep, I'm making you guys, but also trying to understand how the others who join, you know, are able to also catch up.

18:41

But let us strictly stick to the time days, okay?

18:43

So 8 o'clock, if we join, we have enough time to cover up.

18:46

we should absolutely be done by, you know, kind of by 10, 20, easily we can wrap it up.

18:54

And then our Shita will have some time to do with the 20 meter.

18:56

So, yeah, but all of you, please, you try to join by 8 o'clock every day.

19:00

Okay, that's my request, everybody.

19:04

Okay, so let's start on.

19:08

We start off with the most exciting part of the course.

19:10

I'm sure this is what most of you, all of you have been waiting for, obviously.

19:14

LLMs and large language models. And today is our very first session. And just to clarify the

19:22

agenda of what we'll be doing at a very high level, I think the topics don't reflect everything we

19:27

will do. We'll do a lot more than what is listed out here. So we'll talk about what are the pitfalls

19:33

of classic machine learning. So so far we've been discussing about classic ML. The last entire one month

19:38

was based on that. So we'll talk about what are the pitfalls of classic ML. And here we'll introduce a very new

19:44

kind of idea called deep learning. We will see that. We'll talk about large language models.

19:48

We'll talk about something called transformers because LLMs are all based on transformers.

19:52

A lot of jargons we will discuss here. So today will be a very concept heavy session.

19:56

You have to put it that way. And from there, we'll talk about tokens and also probabilistic text

20:01

generations. These are the general subtopics, but obviously we'll see a lot more than this.

20:05

I have a lot of animations, a lot of demos that I have for you. But yeah, not not code demos.

20:09

So the code demos will majorly start from, uh,

20:14

Thursday onwards. We'll get into prompt engineering. Beautiful topic. We'll see a lot of

20:19

cool demos there. But today will be very, very conceptual. A lot of jargons we will discuss and we really

20:26

want to introduce you to the world of what LLMs really are. Okay, before we start getting to the

20:31

quote. Yes, we'll see a little bit of basic hands on for around 5, 10 minutes we will discuss.

20:36

Okay. Yeah. So what I will do is I will take you back to the very first class that we did on

20:44

30th March machine learning. If you remember, this was almost a month and a half back. And I had

20:51

used this diagram with all of you that time. And one of the things I mentioned was, what goes on into

20:58

machine learning? How do you go and build a model? Right. So you have some data. Data is nothing but

21:04

the input, output, or X, Y combinations. We are using some algorithm and based on that we're building a model.

21:09

That is pretty much what we covered and discussed so far. Right. Now,

21:14

If you remember all through the course we discussed about different, different types of algorithms, we can try different, different types of machine learning algorithms and we can build different different different types of machine learning models.

21:24

And then we compare and we find out which model gives the best results. We talked about that. Right. So now, what if we deal with a specific type of data that is very complex? What if we deal with data that is not in a structured format?

21:41

Because in the entire one month that we spent.

21:44

And also in the entire, mostly the Python module that you spent, you had mostly dealt with data which is in a tabular format.

21:52

Like beautiful table, rows and columns. You know, we've been working with data frames all along.

21:59

But my point is, what if you have data that you cannot represent in a data frame format?

22:04

So if I, and that's the piece that we are, you know, we are talking about here. Okay, just give me one second. I have my contents also that I have.

22:14

Shared between just a second.

22:20

Yeah. So what if what if you do not have data in a structured format, right? So all this file structured format. Right. So all this file is structured format. We, you know, we talked about housing price prediction. So we have data in a structured format based on the area, rooms, location, you want to predict the price. All this is great. All this is sorted. So they thrive on.

22:43

data which is in a structured format and all that stuff.

22:47

But how do you work with data which is unstructured? Like, for example, language data, or image data for that matter.

22:54

Images are not the scope of discourse. But if you talk about the world of computer vision, which is

22:59

dealing with pictures and videos, if you deal with the world of audio data, speech data, like how we talk to Google Gemini and Amazon and Alexa, how do you store that in a table?

23:09

Or how do you store text in a table? How do you do that, like language?

23:13

Language does not fit into a table, right? If you say, please reschedule my meeting tomorrow.

23:17

Imagine you're writing a mail and you're saying, please reschedule my meeting tomorrow. How do you store this in a table?

23:23

So these are where classical ML fails. These are the kind of scenarios that classical machine learning cannot solve.

23:31

We have not learned these methods as of now. And that's the first thing I wanted to talk about.

23:35

When are we talking about deep learning? The concept is still the same. You still have data. You still use an algorithm. You still build a model. Those ideas do not change.

23:43

But if the data itself is very complex, if the data is unstructured, especially aligning this with our course, if it is a text kind of data, then we need to use a different set of models to handle it. And this is exactly where deep learning actually comes in. Deep learning and neural networks actually come in. So what is deep learning? What is the term called deep learning? It's not something very different. So deep learning is just a very specific way we are learning the

24:13

patterns from our data. We already talked about machine learning. That's why you can see I've always been writing ML slash

24:18

DL. That time I did not talk about DL. Today I'm saying that DL stands for deep learning. You have the data. You have the input, output

24:25

combinations. You are using a specific algorithm. You are using a specific algorithm, which is, it could be a machine learning

24:34

or a deep learning algorithm and based on that, you're building a model. So general thumb room would be if it is a structured data, you will go and use a machine running algorithm.

24:41

and if it is an unstructured data, you will go back and use the deep learning algorithm.

24:45

But the ideas are all the same training data, testing data, overfitting, underfitting, good fit,

24:50

whatever we have talked to them. Regression, classification, everything remains the same.

24:54

Nothing changes. The only thing is in deep learning, we use a different set of algorithms and those algorithms

25:01

are referred to as neural networks. And I will discuss more about what neural networks are.

25:06

One thing I already warned you, people who are joining the class now, that today's session

25:11

will be full of jargons. We will learn a lot of different, different jargons and go slow,

25:16

and very conceptual, a lot of analogies we'll take, but there'll be a lot of terms that you will

25:19

clear. First of it is deep learning. So deep learning is a special way of doing machine learning. It is an

25:25

advanced way of doing machine learning. In there be the way. Data you have x-y combinations. You're

25:31

using some algorithm and you're building a model. The only thing is in deep learning, you are learning more

25:36

advanced patterns of the data. You are learning deeper patterns of the data. That's even a deep learning

25:41

which is now. So let's understand how is it different? What are we talking about? What is this

25:46

thing called a neuron? What is this thing called a neural network? So let us let us talk a little bit

25:51

more of that. And I think the, and what I want to do here is, I want to take you back and

25:58

to this particular diagram. The term neuron is not new by the way. The term neuron is not new. The term neuron is not new. The term neuron was coined back in the 19,

26:11

50s by a person named Frank Rusen Black. He was the person who coined the term neuron.

26:18

And this is basically what the structure of a neuron looks like. Please do not worry.

26:23

These pay these are equations and all that I've written here. It's back to kind of simplify

26:27

this a little bit for you guys. I have anyways uploaded this diagram for you. But I just wanted

26:32

to simplify this for all of you a little bit so that everyone understands this. If I have to simplify this

26:37

a little bit for all of you. A neuron is a, it's like a very simple, uh, computational unit.

26:45

I think you guys can understand it. Okay, okay. Let me try. I think you will all follow. I'm confident

26:51

to you will all follow it. It looks complex, but I'm, I'm, I'm confident to you will all follow. Okay.

26:55

So a neuron is a computational unit. This is that, this, this, this, this circle. This is the neuron.

27:01

It takes in inputs X1, X2. We multiply that input by the weights W1, W1, W. W.

27:07

we add a bias and we get an output wire.

27:11

This is your neuron. And the equation of a neuron or a perceptron, these are two terms that we use.

27:17

The equation of a neuron or a perceptron is given by this particular formula.

27:21

W1 times X1 plus W2 2 times X2 plus bias B.

27:29

Yeah. So, yeah, Ali, we are actually, yeah, so Ali, we are actually just trying to recap

27:37

a little bit of deep learning. We are starting out with deep learning. So what we are doing

27:41

is we are just, we just started around 10 minutes back. So we're just, we're just talking about

27:45

deep learning and neural networks, what it is, right? Yep. Okay. So no problem, no problem.

27:54

So all that I covered until now, Ali, the part that you missed, you know, all that I'm talking,

27:59

all that I covered was that deep learning is a is a more advanced form of machine. That's it. Deep learning

28:06

is a more advanced from a machine learning.

28:08

You have data and you will use some algorithm and you will build a model.

28:12

So deep learning is a more advanced for machine learning.

28:14

That's what we talked about here.

28:16

Okay. So here it goes.

28:18

All of you are able to see here.

28:20

So it all starts with a concept of a neuron or a perceptron.

28:23

This is just a standard terminology that I'm discussing.

28:26

What is this?

28:27

You know, neuron is here.

28:28

A neuron is basically a computational unit.

28:31

Right?

28:33

So a neuron is basically a

28:35

a computational unit that takes in multiple inputs, X1, X2.

28:40

We multiply those inputs by the weights W1, W2.

28:45

We add a bias and we get an output Y.

28:48

Or you see, that the formula is, y equal to WX plus V, isn't it strikingly similar to Y equal to MX plus C?

28:56

That is exactly what I've written here.

28:57

So I wanted to just tell you that whatever we are learning right now, this concept of a neuron

29:02

or a perceptron that we are seeing today for the first time.

29:05

this is nothing but a simple linear model.

29:08

This is very, very similar to a linear model.

29:10

Now, yeah, we did this class, I think, almost a month back.

29:13

We discussed linear regression.

29:14

And when we started the session, we took a similar example, like X1, X2, and then Y.

29:19

So we have lots and lots of input, output combinations.

29:22

And on the basis of that, you're trying to build a model.

29:24

Or that's the model equation is, that model equation, which is all of you recall that, right?

29:30

So Y equal to M1 times X1 plus M2 times X2 plus C.

29:35

So this is how we learned the equation of a model.

29:38

Neuron may be the same to same thing.

29:41

So next time you're thinking of a neuron or a perceptron, think of it like a linear regression model,

29:46

just for your simplicity purpose.

29:48

Only thing is, just one small disclaimer for everybody.

29:51

Here we're M1 slope, here here we're here we this to weight W1 k.

29:55

First, it's just not, you know, here we're M2 slope k here here we're w2 weight.

30:00

And whatever we call it Y intercept C, we call it Biosk.

30:03

That's it.

30:03

This is the only thing you will have to remember.

30:05

from here on. And we will see more applications as we go along.

30:08

So neuron or a perceptron was invented in 1956 by Frank Bruzenblatt.

30:14

It was a massive discovery.

30:16

So yes, indeed, it is very, very similar to linear regression.

30:21

And this is exactly what that computational unit was capable of doing.

30:26

Yeah, your computational unit is.

30:27

It used to take multiple inputs, X1, X2, X3, X4.

30:30

Baki be inputs.

30:31

Here we have two inputs here. You multiply those inputs with the weights.

30:35

this is like your slope, weights, W1, X1, because W2, you add the bias and based on that,

30:41

you get the output wide.

30:43

This is your simple concept of a neuron.

30:46

All of you, I hope you are able to relate to it.

30:49

So Rousan Black started with the idea of a neurons or perceptron.

30:52

And then we started realizing just like how we discussed decision pre and random forest.

30:59

You'll have you, when I was doing my machine learning classes, I explained decision pre to you.

31:04

And then I told you that, okay, we introduced the concept of ensemble models, right?

31:10

Everyone remembers ensemble, like a jury.

31:14

Instead of having one single model, you can have a collection of many, many models.

31:19

So, if you take a collection of many, many models together, you actually get a very powerful model overall.

31:28

If you take a collection of many, many models together, you get a very powerful model overall.

31:32

That's an ensemble.

31:33

The same idea of.

31:34

we can associate for a decision fee.

31:36

You can have a single decision fee.

31:38

That's your accuracy,

31:39

but if you take an ensemble or a group of many, many decision trees together,

31:46

what do we call it? What is a group of decision fees called?

31:50

Question for everybody.

31:51

What is a group of decision case called?

31:53

N-estimateds equal to, what is that called?

31:57

Random forest.

31:58

Forest is a collection of trees.

32:00

Yeah, very good.

32:00

Random forest is a collection of trees.

32:03

And generally,

32:04

random forest will give you a better accuracy.

32:07

So similarly, a single neuron or a single perceptron will give you a certain accuracy.

32:12

But if I take a group of many, many perceptrons tacked together,

32:18

a perceptron, yeah, usk upon a corley, us over a cornea.

32:21

So when you stack multiple such perceptrons, one on top of each other,

32:26

you end up getting a very powerful network called multi-layer perceptron.

32:31

And this is exactly what is called a neuron network.

32:34

So if anybody asks you that, hey, what is a neural network at its core?

32:38

What neural network is it all starts with a basic linear model.

32:42

It all starts with a fundamental entity called a neuron.

32:45

Neuron's a everything.

32:47

And the neuron term is, that be biology's associated.

32:51

Neuron is also like a nerve cell.

32:52

In the human body, a nerve cell is called a neuron.

32:55

So the term neuron is also borrowed from the world of biology.

33:00

How fascinating that is.

33:01

A lot of early experiments, a lot of, a lot of,

33:03

a lot of research in the early days was borrowed from biology because scientists were fascinated

33:09

with human beings, how human beings function, how we think, how the brain functions.

33:15

So this is why we call it an artificial neuron.

33:20

Anyways, so a neuron is a very basic model, a very basic linear model, just like your Y equal to

33:25

MX plus C, WX plus B. This is the neuron. But when you take many, many such neurons and stack

33:31

many such neurons together or you stack many such perceptrons together ensemble in.

33:36

So you get a more powerful model and that is what we call a multi-layer perceptron or a neural network.

33:43

This is your neuron network.

33:46

And again, we're more back here.

33:48

In fact, very interesting, so this is our curriculum in here.

33:51

But just to show you, just so that people are clear, just to show you, if you if you

33:55

you're psychic learn by search for, now, you look, you see, psychic learn will be MLP classifier

33:59

and MLP regressor.

34:01

So SK Learn maybe this is available there.

34:04

But again, we have not, we are not seen this.

34:06

This is not part of our ML thing, but just wanted to let you know.

34:09

The SK Learn maybe its package is available here.

34:12

Okay.

34:12

So this is the first part of my conversation to introduce what is a neuron and what is a neuron.

34:17

Now, let's take the conversation forward.

34:19

And what I wanted to do, I'm still trying to figure out the best way to do this with you.

34:24

I had a small video actually.

34:26

Let's see if I can kind of figure out a way to

34:30

leave this video for you.

34:33

I think here the sound sharing doesn't work.

34:37

Just a second.

34:44

So what I'll do, guys, I'll try.

34:49

If you're not saying, nothing like it.

34:53

But I'll give it a try anyways.

34:54

I think it will be audible.

34:55

So I've got a pretty decent speaker.

34:58

And because zoom my direct sharing.

35:00

actually. So I'm only trying my best to play the video for you.

35:03

Because here it's a webinar more.

35:05

So the sound sharing here are blocked.

35:07

So I'll try.

35:09

I'll play the video for you.

35:10

If you're able to hear it's fine, nothing like it.

35:12

If you're not able to, you can watch it at your end also.

35:14

No problem.

35:15

But anyways, I'll play it for you.

35:16

It's a small seven minute introduction to neural networks.

35:19

Very nice, very non-technical introduction.

35:21

So I will play this video.

35:22

And on the basis of this, I will explain to you very briefly, what is the neuron,

35:26

what is a neural network, and what deep learning is?

35:28

What is?

35:30

hidden layers, what neurons are?

35:31

And how is deep learning fundamentally different from what you guys have been doing for the last

35:35

one month?

35:36

Okay, so we'll do it.

35:38

And this from this, we'll have connection

35:39

going to, what is large language model?

35:42

Because if you're you not, you know, if you're not related to that thing.

35:46

Because it's all a connect and that, that, that connect is what I'm trying to build in

35:50

today's class.

35:51

Okay, one, two, three, four.

35:53

The connection I'm built by the time we close today.

35:55

Okay, so, so again, let me play this video for you.

35:58

Okay, all of you listening.

36:00

me a small, like, thumbs up, and yes, on chat, if you're all able to hear.

36:03

Fine, okay?

36:04

Let me play.

36:05

I'll play it.

36:06

I'll place my headphone very close.

36:13

The terms deep learning and neuro-network are used almost as a change of the AI, and even though

36:23

they're three, the machine learning, there's also a bit of a bit of hype and pretty mystique about them.

36:29

This video will demystify deep learning so that you have a sense of what deep learning and your land works really off.

36:37

Let's use an example from demand predation.

36:40

Let's say you run a website that serves t-shirts and you want to know based on how you press the t-shirts,

36:48

how many new it is you expect to sell, how many t-shirts you expect to sell.

36:52

You might then create a divest set like this where the hard-pressed t-shirt

36:57

goes out to demand.

36:59

So, I'm going to the straight lines of this data, showing that as the price goes up, the demand goes down.

37:07

Now, demand can never go to go to go zero.

37:10

So maybe you say that the demand will fatten up at zero.

37:14

And beyond a certain point, you expect you don't pay much less than to buy any T-shirts.

37:20

It turns out this dream line is maybe the simplest possible neural network.

37:27

you have as input the price A, and you wanted to output the estimated demand B.

37:36

So the way you withdraw with your network is that the price would be input to this little round thing here.

37:48

This little round thing outputs the estimated demand.

37:53

And the technology of AI, this little round thing here, this little round thing here,

37:57

is called a neuron.

38:00

Sometimes it's called artificial neuron.

38:03

And all it does is compute this blue colon that I've drawn here on the left.

38:11

This is maybe the simplest possible neural network with a single artificial neuron that just inputs the price and opens the ESME to do it.

38:21

If you think of this orange circle, this artificial neuron, as a single artificial neuron that has,

38:27

A little network network.

38:29

All to the new network is

38:31

in technology technology,

38:33

so you get a big power of a network network network.

38:39

Let's look at a different network.

38:42

Suppose that instead of no price of the t-shirts,

38:47

you also have the shipping costs that the customers

38:52

will have to pay to get the t-shirts.

38:55

Maybe you spend more than the t-shirts.

38:56

Maybe you spend more.

38:57

and you can also be the t-shirt on the thick,

39:04

you know, expensive cotton, or a much cheaper, more likely to make the team.

39:10

These are some of the factors that you think will affect the depended tissues.

39:16

Let's see what you're in place in them.

39:20

You know, because it's care about the quality of the team.

39:25

So, let's say,

39:26

Let's say you have a good

39:29

and draw this one in the

39:31

whose job it is to estimate the affordability

39:36

of the t-shirts

39:38

because of the

39:40

and so it is the function

39:44

of the dress and shows

39:46

that are chicken costs.

39:47

And moving on your duty

39:49

t-shirts is always

39:52

consumers

39:56

So the main thing that we have to be your property.

40:03

So let me draw here as a certain piece of official mirror-on that inputs your marketing,

40:09

how she spends on property, and outputs

40:13

how long away are consumers of your t-shirts.

40:18

Finally, the perceived quality of your product is so effective a lot.

40:23

And you can see,

40:25

would be effective on property

40:28

the policy

40:29

tries to convince people

40:31

this is like a policy teacher

40:32

and sometimes the price

40:34

something also affects

40:37

perceived quality

40:38

something to draw here

40:40

a third artificial law

40:42

that inputs

40:44

price

40:45

property

40:46

to you

40:47

and tries to estimate

40:49

the perceived

40:51

quality

40:55

I think it all

40:57

I'm taking on

41:03

on

41:04

the former

41:05

opportunity

41:06

because of

41:07

you can then

41:09

on the

41:10

here

41:11

that

41:12

takes as input

41:13

these

41:14

actors

41:15

and purpose

41:16

de estimated

41:18

to them

41:19

so this

41:20

is a new network

41:22

and this

41:25

it puts that's the input A to the output B to the output B to the

41:35

input B to the output A to be.

41:40

This is a very small network

41:43

with just full artificial neurons.

41:46

In practice, their networks used to make

41:49

much much much more can.

41:50

Thousands, tens of thousands, or even much much much more than that.

41:54

Not.

41:55

Disturbance is there. Is it nice? Because I tried to, no, I was thinking, but I didn't want to interrupt.

42:03

So, yeah, so I think, I'm not sure why disturbance actually. Let me check. Yeah, you know, I was seeing, but I didn't want to interrupt the flow. So, just a second.

42:21

Okay, no, no, anyways, I think I can, I can share this with you. The only thing is that the zone.

42:25

Zoom restricts me from playing the computer audio. That would have been the best thing. But this is actually a Coursera, very nice Andrew NG's, you know, material.

42:34

Anyways, let me, let me discuss this with you because most of you would have seen quite a bit of the video already.

42:41

I think that's okay. No problem. I'll discuss with you. Don't worry. So basically, Andrew started out with, Andrew started out with the concept of a demand prediction. This is the gist of what

42:55

Andrew talked about in the video. So, imagine, we are, you know, we have the price. Based on the price, we are trying to predict, what is the estimated demand to the product.

43:13

So this is like a typical neuron use case. So we have the price, which is the input, and based on that, we have to predict the demand, which is the output.

43:22

So based on the price input, we will have to predict the demand output.

43:25

that's the way how we'll be modeling this and that's what the neuron that's what we call the neuron

43:29

the neuron will take this input price x and based on that it will predict the output y that is a demand

43:34

why based on the input price x it will predict the output uh demand which is the y that's pretty

43:41

much what we discussed already now now let's complicate the problem a little okay uh now what

43:51

if there are total four features what if there are total four features we have the price we have the

43:57

shipping cost we have the marketing we have the material and these are like x1 x2 x3 x4 these are the

44:06

four features we um you know we have right now these are the four features we um we have right now

44:14

and now we are trying to go back and excuse me

44:21

and now we are trying to go back and predict what is the output demand based on this we are trying

44:30

to predict what is the output demand there it goes so here it is it is sorry

44:39

here it is here it is and based on that we are trying to predict output why

44:47

which is the demand okay i hope everybody is clear everybody is everybody

44:51

aligned on this now again i repeat this is just we are we are changing the problem right now

44:57

we are saying based on the input excess the price shipping cost marketing material we are

45:01

trying to predict the output demand and this is also possible we have done these kinds of problems in our

45:05

machine learning journey and this is also like a typical regression problem i think you can all

45:09

relate to it it's a demand prediction that means it's a regression problem right we can all relate to it

45:13

that one right now now let's let's let's let's let's continue on so think about it first

45:21

a minute think about it when we were doing machine learning we followed this process

45:27

called data cleaning feature engineering and i was repeatedly telling you that

45:32

whenever you try to build the best model uh data preparation is very important you must have the right

45:38

data and even if you don't have the right data you will have to oftentimes perform different

45:43

types of transformations and create the right data so you have to ultimately use

45:51

those inputs or xes which are good predictors of the output so what are those input

45:58

features which are good predictors of the output of demand output y that is what we are trying

46:06

to find out if you think about it the demand of a product is it really related to price

46:14

and shipping cost is price and shipping cost a very good predictor of demand

46:19

we can debate about it right so think about it if a price of a product increases does that always is that the

46:29

factor that causes the reduction of demand maybe maybe not a product of man know you

46:40

phone carid the phone price barred yeah so phone price barreda so customers will buy less

46:46

so demand to come will be we're not debate

46:49

that but the price if increased go we're not debating that what i'm debating is

46:55

you the demand fall is is the price the actual cause of it maybe not so i can also say

47:06

because the price of the phone increases that leads to the consumer sentiment here

47:15

there a more hidden feature called consumer sentiment the consumer sentiment got impacted

47:23

and that is why they are buying less that is why the demand is impact so what i'm getting at here

47:27

is the original inputs do not have a direct relationship with the output and that is exactly

47:36

what we were trying to do you know what we are trying to do in deep learning we are trying to find out

47:39

what those hidden intermediate features are what those deeper features are and that's why we

47:45

a deep learning you've got a little video they've got the gist of it what andrew

47:49

was trying to talk about but anyways i'll repeat the whole thing don't worry but uh part of what

47:54

andrew was telling that time was that these original features they cannot directly predict the

47:59

demand you're model you'll model to be model but it's accuracy

48:03

that's not enough no price increase if the demand will reduce but

48:07

its correlation will his relationship maybe price increase on as some other factors change

48:13

going to and if we'll get a much better accuracy because they are the true predictors

48:19

of demand and that is exactly what you know what andrew was showing in the next part of his video

48:25

now he started to say okay based on these original four inputs these are the derived features

48:31

we are creating affordability awareness perceived quality and based on that we are trying

48:37

to predict the demand this your model will be made you so these are these are

48:43

this is what we call a hidden layer in a neural as well so yeah your input layer

48:47

okay this is your input layer let me write it down so there goes your input layer there goes your

48:53

input layer there goes your output layer this is like nothing but your x1 x2 excuse to x3 x4 these

49:04

are the input x is this is the output y and these are the hidden features what you are

49:10

seeing here is like the hidden layer that's a hidden

49:13

layer that you are able to see on the screen and this is like your h1h2 and h3 that that's

49:20

what you're able to observe right now h1 x2 h3 have three hidden neurons you're able to observe

49:24

that means the concept here is nothing but based on the the input a input layer neurons that

49:31

you're able to see based on x1 x2 x3 x4 these are the four input layer neurons you're able to see

49:36

so based on this x1 x2 x3 x4 the four input layer neurons that you're able to see we are able to see we're

49:43

are able to derive the hidden layer neurons, H1, H2, H3.

49:49

These are three hidden layer neurons we are able to derive.

49:52

And based on that, we are able to get the output wine.

49:55

And turns out, this is exactly what I was talking about.

49:58

It turns out that these original exits, from this we are deriving this H1.

50:03

You know, affordability, what are you?

50:05

Price or shipping costs.

50:07

I mean, if price or shipping cost product's product, it's a affordability come

50:10

here. This feature is a hidden feature.

50:13

It's a new.

50:15

It's all the both of combined and been made.

50:18

So, turns out affordability is a new feature we have created.

50:21

Just like feature engineering, from the existing features, you are creating new features.

50:26

So you have a new feature and you're on this kind of basis on demand predict

50:30

so your model better would.

50:32

This is a more feature.

50:34

Awareness is how we've made?

50:35

Marketing awareness has awareness.

50:36

I'm, this is what I was talking about.

50:42

Price shipping costs are company specific features.

50:44

Company price set per seet.

50:45

Company shipping costs set up.

50:47

But,

50:48

yeah, product aware, affordable is?

50:52

Are customers aware?

50:54

How are they perceiving their quality?

50:55

I mean, it's how they're quality?

50:56

Like, if you have iPhone and Samsung's comparison.

51:00

Or iPhone and OnePlus plus compare to,

51:03

then there's comparison is not?

51:04

What compare to them?

51:05

Apple iPhone is way above the stack.

51:08

Samsung Galaxy Ultra phones are way above the stack.

51:10

They are very, very good in terms of quality and build and whatever.

51:14

So perceived quality is how are people perceiving?

51:17

So we have managed to create these hidden features,

51:20

customer level features based on the original set of features.

51:24

Here you deep learning can.

51:27

So next time when we think of deep learning,

51:29

now see, perceive quality is a feature that is derived from price, marketing or material.

51:35

And this is obvious.

51:35

like, if you know, Apple's a comparison, if price is

51:37

the price, then people will like, yeah,

51:39

it's so it's a good, you know,

51:40

I mean, general human psychology.

51:42

If you're in free, then you'll like,

51:43

yeah, free kind of, so, that's value

51:45

not. But if you think the price is more,

51:47

the Apple's price is more, then you

51:49

think, yeah, it's something to

51:49

have it. So, marketing also is a factor.

51:53

So more the marketing, more the perceived quality.

51:55

Perceived quality, I mean, how are people perceiving?

51:57

Its quality can how are people pursuing?

51:57

It's the quality, if the company

51:59

marketing in more, then you'll

52:01

like, yeah, it's a good.

52:03

If you're going to be a good,

52:04

if it's a good, so, so this,

52:04

So all these three things combined is creating the perceived quality feature.

52:08

And based on that, we are getting predicting the demand.

52:11

Now, here is a really interesting thing about deep learning.

52:13

Why we call it deep learning?

52:15

Now, the really interesting thing that Andrew was talking about at the very end was,

52:20

these features are something we don't create.

52:26

Yeah, I was just trying to do it to explain to you.

52:28

But these affordability, awareness, perceived quality,

52:31

yeah, manually, they're not making.

52:33

These are making.

52:34

last machine learning course, we're manually doing everything.

52:39

But this process is now automated completely in deep learning.

52:42

You're when deep learning in deep learning, this process is completely automated.

52:47

So the feature engineering part is totally automated in deep learning.

52:51

You just give the machine lots of Xs, lots of Y's what Andrew was explaining towards the end.

52:55

You just give the machine lots of input output combinations, X, Y combinations.

52:59

And it is the job of the machine to figure out the most accurate represent.

53:04

from the input text to the output line.

53:07

So this is something the machine will learn.

53:11

You're not going to be awareness, a conceived quality, whatever.

53:14

You will not go to create these features manually.

53:16

So it is the machine's responsibility to learn deeper features from the original set of features.

53:23

Original set of features.

53:24

From the original set of features,

53:27

it is the responsibility of the network to combine these original features and to learn the deeper features.

53:33

Like your deep learning.

53:35

This is exactly what deep learning is.

53:37

How do we learn deeper features from the original set of features?

53:41

And that's why the term deep learning gets used.

53:43

There's no rocket science is same to same, X, X, Y, supervised learning.

53:47

All the difference.

53:49

The biggest difference is that here, the machine is learning the intermediate set of deeper features.

53:53

And this only one layer, it's just a hidden layer.

53:56

In reality, neural networks can span.

53:59

This is what he was talking about in the last part.

54:01

Neural networks can span several hundreds and thousands.

54:03

of hidden layers.

54:05

Thousands.

54:06

Thousands are.

54:07

Tens of thousands.

54:08

So, input layer, output layer.

54:10

Output layer.

54:11

Here, we know.

54:11

There can be like thousands and thousands of hidden layers in between.

54:16

And that's what makes neural networks like really, really incredible.

54:20

And that's why they are able to like, and if you're conceptually thought of,

54:25

there are features that we are able to discover that the human mind would not even a thought of.

54:31

You know, maybe not even thought of.

54:32

will be that, yeah, it's a whole set.

54:34

So, we're having, when we are thinking,

54:38

that, what we're thinking, that, what, it's input, this output,

54:39

so we have to, we have to make, this, but we're going to make.

54:42

But deep learning in, you're making these features

54:45

that you're making, which you're making a machine

54:47

such feature being, which humans would not even have thought of,

54:50

that, yeah, that's how, that's how we're getting the idea of what I'm not.

54:54

That's why we call it deep learning.

54:55

That's why we're going to be a concept, I'm not.

54:57

Whereas, where these hidden features are mentioned in,

55:00

Suha said, hidden features are.

55:02

Just to clarify the terminology, this your input is?

55:05

I will repeat this once again for you, okay?

55:07

This your input layer, this your output layer, okay?

55:10

This is your hidden layer.

55:13

So I've been using the term hidden hidden for so long.

55:17

Huh?

55:18

Yeah, no, hidden layer in these are all neurons.

55:20

Correct, exactly.

55:21

They're all neurons, right?

55:22

This neurons are, correct.

55:25

So hidden layer.

55:29

And these are the hidden neurons.

55:32

right, H1, H2, H2, H2.

55:34

In this example, we have three hidden levels.

55:36

But the rest are you up on you.

55:37

You can't, you can't set up,

55:39

you're both set up, you can't,

55:40

that one hidden layer, we'll take.

55:43

So this is something that you will have to clear.

55:45

Okay, when you're deep learning models

55:46

to make, this is your responsibility to design

55:49

how you want to design the hidden layer.

55:51

Okay?

55:52

Is it clear?

55:53

So Asini, I hope you're fine.

55:54

And, Wernit, all good?

55:56

And, clear?

55:57

Let me know?

55:58

Let me know.

56:01

Okay?

56:02

Uh, okay.

56:04

And hidden Q can't, because he doesn't know.

56:07

Machine is deriving these features from the, from the data.

56:10

That's why we call them hidden features.

56:11

Okay?

56:12

Now I have another final one, final demo, which is also very interesting.

56:16

So this pay some images.

56:17

So actually, in course, but what I thought is like,

56:22

an intro is important to you.

56:23

Today's force is actually completely on LLMs,

56:25

but the important thing is production is important for you.

56:28

So that people have a big picture idea of deep,

56:32

what is it?

56:33

So it's just to give you a flavor of deep learning.

56:36

That's it.

56:37

Otherwise, we're not getting into deep learning and all that.

56:39

But yes, it's just to give you a flavor and we'll straighter.

56:41

We go to LLMs and transformers from here on this.

56:43

Okay, so that's the objectives.

56:45

Now, let's move on.

56:49

This is one more video, very interesting.

56:53

So Andrew is trying to explain here is,

56:57

let's say we have a picture and we are trying to do image recognition.

57:01

to do image recognition.

57:02

Okay, image classification and we are very practical example.

57:08

We've seen many practical examples.

57:11

So one of the practical examples is, if you remember,

57:14

we've this example before we discussed

57:16

when we started our course, right?

57:19

I discussed about this example in Google photo, right?

57:21

That time I explained to you that this machine learning based,

57:24

there are rule based, all of you remember, right,

57:26

we are not hard coding the rules.

57:28

At that time we had it was machine learning,

57:30

Today I will make a small correction and I will call it a more advanced version of machine learning called deep learning.

57:36

Actually, you're machine learning.

57:38

So if you're thinking, machine learning is like a super set.

57:41

This is the easy way to remember.

57:43

Machine learning is like a super set.

57:45

Deep learning is under a specialized subset.

57:48

So ultimately this is machine learning.

57:50

Machine is learning the rules from the data.

57:52

You're showing it lots and lots of examples and the machine is learning the patterns.

57:55

That is machine learning, right?

57:57

So deep learning is a specialized subset within it.

58:00

It is learning deeper features from the data.

58:03

So anything to do with unstructured images and all.

58:05

So next time you upload a picture,

58:07

how can't know that the elephant is deep learning is happening.

58:10

It's image classification.

58:11

So let's see a small example that how it is.

58:14

So this picture is.

58:16

Same story.

58:17

Same story.

58:18

You pass that picture through.

58:19

Look, picture is very complex.

58:21

When we talk about images,

58:23

then images is a different side topic.

58:25

But maybe at a very high level I can talk about it.

58:28

When we look at any picture,

58:29

Now, look, this is a number 3.

58:31

Now, you make it in paint.

58:33

You, you know,

58:34

JPG file in store,

58:35

PNG style in store,

58:36

or anything.

58:37

So this is a image file in store

58:39

right?

58:40

But guys, very interesting.

58:42

If you zoom it to zoom

58:44

into the picture, can you start to see?

58:46

You can you start to see?

58:47

You can you see?

58:48

This is exactly what machines start to see

58:51

when they process pictures.

58:53

Machines are not seeing an image like an image.

58:55

Images are very complex.

58:57

I can click a high radio.

58:59

resolution colored image of myself.

59:01

If my picture maybe zoomed in,

59:03

you can see these very small, small square boxes.

59:05

Can you see these very small, small squares?

59:07

These pixels are here.

59:09

As see, images can understand can't.

59:12

So images you cannot directly classify.

59:14

So what is going on behind the scenes is,

59:16

we take that picture, we pass it through,

59:19

we pass it through many, many hidden layers.

59:23

And based on that, we try to predict the output.

59:25

Whatever story we discussed in the last video,

59:28

if you relate it here, this is your input layer.

59:31

This is your output layer.

59:34

This is your input layer.

59:36

And these are all the hidden layers.

59:39

I want to clarify the story remains the same.

59:45

This is the gist I want people to get.

59:47

What is deep learning? Why we call it deep learning?

59:49

What is hidden neurons? What are these guys doing?

59:52

What are these hidden layers even doing?

59:55

Well, the hidden layer is looking at the original picture.

59:57

the original picture and it is deriving new features out of it.

1:0:02

So picture in the shape, the facial features what is the nose, how is the eye, features

1:0:09

how is the lighting condition.

1:0:12

So all each of these neurons are extracting features from this image.

1:0:16

Hidden features from this image.

1:0:18

Humans can't.

1:0:20

That's what deep learning excels.

1:0:22

Right?

1:0:23

And if you want to get an idea about what some of those features are,

1:0:26

take some of those features, what they are.

1:0:29

Because the first layer is able to learn basic features,

1:0:32

diagonals, vertical lines, horizontal lines,

1:0:35

basic features.

1:0:37

The second hidden layer is able to learn some more advanced features.

1:0:40

It's able to make out eyes, nose, ears, and all that.

1:0:43

And the third hidden layer is able to make out entire faces.

1:0:46

And this is basically the crux of what we are trying to do in deep learning.

1:0:50

Just to give you a very big picture overview,

1:0:52

by deep learning here.

1:0:54

No, no, no, no, no.

1:0:56

Do we have hidden layer data handy in form of?

1:0:59

No, no, hidden layer is derived from, as I told you,

1:1:01

the hidden data is derived from the original picture, original features.

1:1:05

Right?

1:1:06

Again, Suasini, I think I'll take you back to the original video,

1:1:09

because this video will be difficult to relate to.

1:1:12

I think this is what we talked about all this while.

1:1:14

So from the original features, you understood this, right?

1:1:17

Let me pause here.

1:1:18

Price, shipping, cost, marketing, material.

1:1:20

These are the original input.

1:1:22

Right?

1:1:23

On the basis of the original input.

1:1:24

we are deriving the hidden features.

1:1:26

Clear?

1:1:27

So that answers your question.

1:1:28

Where is the hidden data derived from?

1:1:30

From the original feature only?

1:1:31

That's it.

1:1:32

It can be one hidden there.

1:1:33

It can be multiple hidden threads.

1:1:35

They are all derived from the original data.

1:1:37

And the machine is made.

1:1:38

The best part, it is automated.

1:1:40

We are not doing it.

1:1:41

The machine is actually doing it automatically.

1:1:43

Because this is just to show you.

1:1:45

But this is a completely different topic.

1:1:47

This is actually on computer vision, which is not part of a thing.

1:1:50

But I just wanted to show you so that you have a big picture idea

1:1:53

that neural networks here.

1:1:54

So in image you're able to derive the different features of the image and based on that you're trying to finally classify the output.

1:2:04

Okay, everybody is fine.

1:2:06

Okay, this is the very basic contextual understanding in terms of what neurons are and what hidden layers basically are.

1:2:15

I hope everybody is absolutely cleared with this particular idea of.

1:2:22

Now let's move on.

1:2:23

This is pretty much how it looks like in practice.

1:2:29

As I told you, as explained to all of you, you've got input layer.

1:2:32

Input layer could be pictures or text or whatever.

1:2:34

Could be what's going to do.

1:2:35

Absolutely.

1:2:38

Any example, you can take any example.

1:2:41

You can take anything.

1:2:42

You can take any image data, image classification, though,

1:2:45

because our content is on text.

1:2:47

So I'm going to move on to text data right now.

1:2:48

When we're text data about the same idea you can do that.

1:2:51

Right.

1:2:52

let's say we have a particular, let's take the example of Google, Google News, right?

1:3:00

So Google News is looking at lots and lots of news stories and based on that they are trying to predict, you know, is it what category the news story corresponds to?

1:3:08

A new story is it, that basis of that category is it finance, is it technology, is it politics and so and so and so forth.

1:3:15

So that is also done using what we refer to as hidden layers. So you have input, input here, the text is.

1:3:22

So text for directly, you cannot do you cannot say, is it, is it, is it, a, uh, a politics, news story, is it?

1:3:29

So you can't directly process text data, we discuss that.

1:3:32

So what you'll do?

1:3:33

Now, now, you'll, now, deep learning through.

1:3:35

So from that original text, you are extracting many, many hidden features.

1:3:40

What words used were, what words used were, what words can't be able to, and based on that you're trying to predict now.

1:3:46

I can't get a little deeper into this in terms of text a while later, but I hope right now, the, uh, the, the, uh, the, the agent

1:3:52

is just to clarify what, what deep learning is.

1:3:57

How is it different from machine learning?

1:3:59

I hope everybody's aligned on that part.

1:4:01

Hidden layer, what is hidden neurons? The terminology should be absolutely clear to what is it.

1:4:07

What is it? What are we doing here overall?

1:4:10

Okay. Now, let's continue on.

1:4:19

And just to also kind of clarify, these are some of, these are some of

1:4:22

of the problems, these are some of the problems that we, that classical ML actually faces,

1:4:29

right? I was talking about classical ML and these are again some of the problems at classical

1:4:33

ML faces like the feature engineering problem. You need features. So, what if it's a more

1:4:40

complex problem? If problem complex, if it's unstructured data, like images, text, so classical

1:4:46

machine running say that we're not able to, which we've made last one month said, you want to solve a problem.

1:4:50

you want a neural network to learn deeper features from your data.

1:4:56

From your original data, you want to learn deeper features, number one.

1:4:59

Number two, other text data hoga, particularly with respect to text,

1:5:05

another problem that you will face is that different words will have different meanings.

1:5:11

This is also a classical problem.

1:5:13

Now, look, imagine you use a particular sentence called I went to the bank.

1:5:18

Okay?

1:5:19

If you say I went to the bank.

1:5:20

Now, the word bank can mean different things, right?

1:5:25

So word bank can refer to a financial institution, where pasha rakeo.

1:5:29

The word bank can also refer to a river edge.

1:5:33

That's the intuition.

1:5:35

So this is the other thing I wanted to clarify that the word ambiguity is also true.

1:5:41

And normal machine learning, whatever we have done so far, that will not help you resolve this.

1:5:47

That will not help you resolve this particular problem.

1:5:49

And this is exactly.

1:5:50

where deep learning, deep learning works very, very well.

1:5:55

And that is exactly what we will be getting into.

1:5:58

So these are the problems of classical element.

1:6:01

We talked about deep learning.

1:6:03

And this is exactly what deep learning will help you solve.

1:6:05

We're more animations used to make it a little easy for you.

1:6:08

But this is one of the major problems.

1:6:10

The word's meaning what do we understand the meaning of the word?

1:6:13

If a bank here, what does that bank refer to?

1:6:16

How are these chat, GPD and all so intelligent?

1:6:19

Now, if you question kind of context, you know,

1:6:22

so classical ML cannot help, but what is going on behind the scenes is deep learning.

1:6:27

Okay?

1:6:27

You're your question that is going through thousands and thousands of layers of neurons

1:6:32

before you get that answer.

1:6:34

That is actually what's going on behind the scenes.

1:6:36

And that's the basic, that's the big picture idea of what neural networks really are.

1:6:42

Okay?

1:6:44

Okay.

1:6:45

Now, let's continue on.

1:6:49

And what I want to do here is, and I basically have this particular, you know, very nice, very nice animation.

1:6:57

One of my favorite animations and I think for the next 20 minutes to half an hour, I'll be pretty much using this animation.

1:7:06

It's a really, really beautiful animation.

1:7:08

So guys, I'll bring the link to you, but you, but you this side-sat-sat-sat-sat-so-munt-d-de-cafac-conceptual.

1:7:12

There's a lot of concepts here here mentioned here and don't try to click on it and follow at your end.

1:7:18

So just follow.

1:7:19

how I'm explaining the topic, and then when it's required, I'll tell you, I'll tell you

1:7:24

when you need to go and do it more than you.

1:7:27

But for now, please follow the way how I'm explaining to you.

1:7:30

But it is one of the best animations that I personally, it's not my creation.

1:7:34

That's why I quoted financial times for it.

1:7:36

It's wonderful.

1:7:37

I have, you know, one of my favorite visualizations for large language models and transformers.

1:7:44

Really, really good.

1:7:45

I think you will, you will really enjoy this once we are done with our discussion.

1:7:49

But before I start with this part, is everybody convinced about what is deep learning?

1:7:55

Clear, all of you can connect the dots, that ML was and this deep learning.

1:8:00

Everyone is okay.

1:8:02

Let me know, please, on chat.

1:8:04

Clear, guys, all of you.

1:8:07

Difference clear.

1:8:08

What is what is clear?

1:8:11

Deep learning, our topic not yet, guys, but I still wanted to make an effort and just show you what is it.

1:8:16

Deep learning our content in here, actually.

1:8:18

We're not getting into.

1:8:19

deep learning, okay, but still you should know a little bit of it. So, okay, clear, all of you.

1:8:24

All of you.

1:8:34

Thank you. Thank you. Great. Okay. Let's move on. So now, uh, what I will do.

1:8:45

Let's say, let's say, let's, let's, let's, let's understand.

1:8:49

this step by step, okay? Let's understand this step by step. And before I, uh, before I get a

1:8:55

little deeper into this, uh, let's, let's, let's understand, uh, you know, this thing,

1:9:03

keep it. We go to work by train, okay? So imagine we have this particular sentence. We go to work

1:9:08

by train, okay? Okay. Now, to write text, large language models must first translate words into a language

1:9:19

that they understand. So, yeah, LLMC is something we have not introduced yet. So you

1:9:24

you can it's just so much can't, machine, machine must first translate words into a language

1:9:29

that they understand. Because machine can't work in the word

1:9:31

in the way we have to say. This we've got to say, that we've got to say, that's all the first

1:9:34

first thing, that you know, that's all right? But, but, but, but, but

1:9:42

if some text data has, it, machine can't understand, machines cannot understand,

1:9:46

machines only understand binary. So we need to

1:9:49

first figure out a way to store it in a format that machine can understand.

1:9:54

Okay, let's see. So, so first

1:9:57

first thing that we do is we, and the first thing that we do is we, a block of words is broken into

1:10:04

tokens, and tokens are basic units that can be encoded.

1:10:10

You know, they're encoding be, seeked, you know, word, one out encoding day. It's something similar

1:10:16

to that.

1:10:16

So, tokens often represent fractions of words, but we will turn each full word into a token.

1:10:24

So whatever assumption we are making right now is every word is a token.

1:10:29

That's a very default assumption.

1:10:30

So, sometimes other be more be able, but right now, tokens are basically nothing but the smallest

1:10:35

individual element of a word.

1:10:39

It's a block.

1:10:40

Each word is like a token.

1:10:41

token, means a group, one unit.

1:10:44

So one word, a unit.

1:10:45

So there are how many word, a unit.

1:10:46

many tokens right now, there are six tokens. That's it.

1:10:49

But it's a other way to be. Okay. Now, moving on. And this is again a technical term that

1:10:56

you can remember. So tokenization is like a technical term. It is the basic unit of text. It can be a

1:11:03

complete word. It can be a part of a word. It can be a punctuation mark. But imagine, if our sentence

1:11:09

something like, I'm just giving an example. If our sentence asa would, right? So let's say we have

1:11:13

this and I have a semicolon. If we have a semicolon, so my tokens would have been,

1:11:19

my tokens would have been semicolon would also would have been a token.

1:11:23

Semi-coron be a token just to clarify. So tokens can be in it. But for simplicity, I am saying

1:11:29

one token is one word. That's it. That is what we are starting the discussion with. Now,

1:11:38

these are the building blocks basically. This is another very nice demo I wanted to show you.

1:11:42

You can see. Very interesting. You can see this one. The unbelievable power of

1:11:52

tokenization. You can clearly see an is a separate token. Believe, able, power of tokenization.

1:12:01

So this is a rule. So don't worry too much about it. Kasea how are internally. But different

1:12:07

models will have different rules of being the tokenization. But at the most,

1:12:12

basic level, at the most basic level, every word is a token. That's the way how we

1:12:18

understand it conceptually. Okay. Now, moving on. Now we have broken this into tokens. All good.

1:12:30

Now, in order to grasp a words meaning, work in our example, the LLM first observes it in context

1:12:38

using enormous sets of training data. Taking note.

1:12:42

of nearby words. These data sets are based on collating text published on the internet

1:12:49

with new LLMs trained using billions of words. Our sentence is, we go to work by train. My focus

1:12:56

word is work. Now, work what is work? How is the machine able to understand the contextual

1:13:03

meaning of a word? That's how much of a word? Because you, many times you might have heard that

1:13:11

when these large language models are trained, these large language models are trained on a

1:13:15

tremendous amount of data, internet scale data. These LLMs are trained on a tremendous amount of

1:13:22

internet scale data. And in this internet scale data, basically I'm talking about the entire Wikipedia,

1:13:28

entire Google News, whatever. Then I'm like, you know, we can talk about trillions and zillions of

1:13:32

text it is trained on. Now, go to your GPT being, chat GPD is being. This is very expensive, very

1:13:38

costly, very time-presuming. And when you do that, you do that.

1:13:41

that, you think, this word work is. I'm just only one example

1:13:46

But there can be so many thousands and thousands of different ways how a particular word is

1:13:55

used internally, right? There can be thousands and thousands of ways how a particular word

1:14:02

is internally used, right? That's intuition. That's what we're talking about. They can be

1:14:08

there can be thousands and thousands of ways how a specific word is getting.

1:14:11

boost.

1:14:14

This is your example. This is what we are basically, you know, kind of talking about intuitively.

1:14:23

Right. I hope everyone's aligned on this. Now, moving on. So what are those thousands of words?

1:14:29

Let us see an example. Now, look at this. I went into work yesterday morning. How much work is

1:14:34

project? Down to, downtown to work. Roof at work as a, he's hard work and effort. He can analyze work related to

1:14:41

Now, there's some examples in different contexts in different contexts.

1:14:47

There are so many infinite number of ways what the word work can be used.

1:14:51

On machine, yes, all the examples go through kirkke, it is trying to understand that the

1:14:56

word's what kind of what's what kind of.

1:14:58

Streamlined our work, for her work are admirable, friend from work, live.

1:15:02

See, see how it is doing that? This is exactly what it is doing.

1:15:06

It is, and the most important thing is, it is taking a note of nearby words.

1:15:10

how is that word work used in the context of the nearby words?

1:15:17

And that is what I really wanted to want for us to focus on.

1:15:21

We are looking at a specific word.

1:15:25

We are looking at a specific word in the context of other words.

1:15:32

That's a very important thing, friends.

1:15:34

I repeat again, we are looking at a specific word.

1:15:37

Here also we are looking at a specific word.

1:15:40

in the context of other words.

1:15:45

We are looking at a specific word here in the context of other words.

1:15:52

And that's the basic idea. That's a basic thing that we're able to relate to right now.

1:16:00

Okay, so what is the, um, what is the, how is that word used? How is that word specifically used?

1:16:10

in the context of all these other words.

1:16:15

And based on that, eventually we end up with a huge set of words found alongside the word work in the training data

1:16:20

as well as those that were not found nearby.

1:16:23

Now, look, if you're looking at, if you're looking, then nearby,

1:16:26

now, what's words with work use are.

1:16:29

That nearby words is.

1:16:31

This is the best thing.

1:16:32

This is the context.

1:16:34

Next time anybody tells you about context.

1:16:36

Any of your context of what kind of context can talk about,

1:16:38

this is context of context.

1:16:40

what do you mean by context? Context, what is context? What is context?

1:16:46

When we talk about context, what is context? This is exactly what context is. This is exactly what

1:16:53

context refers to. That's what we are getting in a way. So this is exactly what the context

1:17:00

refers to. I hope everybody's aligned with this. And this is the final thing that people get.

1:17:08

eventually, we end up with a huge set of words found alongside work in the training data

1:17:14

as well as those that weren't found near it.

1:17:19

We end up with a huge set of words found alongside training data as well as those that weren't found near it.

1:17:25

This is the thing that we end up with, huge set of words.

1:17:30

And as the model processes the set of words, it produces a set of words, it produces a vector or a list of words

1:17:37

and adjust it. And this vector is known as a word embedding.

1:17:44

You see, go home word embedding care. This is the first step to understanding large language models.

1:17:52

So yeah, internally, hurry. Again, I think you don't worry about how internally this is happening,

1:17:57

but at a big picture idea is what I'm trying to get at. So the machine understands how that particular

1:18:05

word is used in the context of all the words.

1:18:09

And once it understands how a particular word is used in the context of all the words,

1:18:14

how that word is getting used along with other words, the context.

1:18:17

Once it understands that context, it tries to, it uses a neural network.

1:18:24

It uses a neural network.

1:18:26

The neural network used to, it is trying to learn a specific vector.

1:18:33

This is your end result is.

1:18:34

The final end result is a vector and this vector is known as a word embedding.

1:18:42

This is your word vector.

1:18:44

So next time you talk about a word work, a word work is nothing but 0.35.

1:18:50

0.19.1.15.0.08.25 like that.

1:18:54

Now you'll say, sir, this is what this is what we started the demo with.

1:18:59

We've clearly said that, guys, machines don't understand text.

1:19:02

If you can put text data input machine to it, it's not much machines only understand numbers.

1:19:09

And this is the way how we convert text into a numeric form.

1:19:15

Now, you know, you can't a, you can't, sir, this is how it how it's going to at a high level.

1:19:21

So at a high level, I'm saying, right?

1:19:22

You are passing that input through a massive neural network.

1:19:27

We have seen neural networks what it is, right?

1:19:30

You're passing it through a massive neural network.

1:19:32

this output will. So imagine if you if you pass the word work,

1:19:38

if you're, if you input, the output will be this vector of numbers.

1:19:44

Like, 0.35.0.29.

1:19:49

This your output would be. Point 35.0.29.

1:19:54

Excuse me, 0.1.5.0.08.

1:20:02

This is the final output. So based on the input word that is worth, we pass that input through a neural network,

1:20:12

a bunch of hidden layers and all that. We pass that through the hidden thing. And based on that,

1:20:18

we're getting that particular word vector. That's the end result that we ended up getting over us.

1:20:22

This is the big picture idea. Okay? Or this we only one word to explain to you.

1:20:27

Whatever we did here was with respect to a single word work.

1:20:30

I'm work applications. How is the word work used in so many different sentences? But you can do this for the billions of other words that we have. Not billions. Sorry, you don't have billion words. But then whatever. We can easily 100,000 millions to go. So you're growing this for each of those 100,000 words in the English dictionary.

1:20:48

Okay. So you can imagine how many permutation combinations and how big that processing will be. But the end result is, you know, you're going to be. And this is what is referred to as, you know, and this is what is referred to as, you know,

1:21:00

word vectors, word embedding, word embedding. This was a, this was a very pivotal thing.

1:21:06

And if you ask me, guys, this is not a new thing. This is not a new thing. In fact,

1:21:11

in fact, Google was the company that created this particular word embedding based model. Just give me one

1:21:21

second, guys. Google was the company that created this word embedding model for the first time. This was back in

1:21:30

2013. So whatever I just took some time to explain to you, this the word vector

1:21:35

we have explained here, all this while, that we can a word go, we can a vector to

1:21:39

represent can't. This was originally invented by Google back in 2013. This is nothing new.

1:21:46

This was invented more than 10 years back. This was a fascinating concept. And what I'm again trying

1:21:51

to do is I'm trying to build the basis for you. So first, we discuss neural network, which can process

1:21:57

text data. Second, we are discussing word embedding.

1:22:00

word to vector.

1:22:01

Now you'll say, sir, it's how it's made.

1:22:04

This was built using a neural network.

1:22:08

So words say, some vectors

1:22:10

make out. And if you want an even better

1:22:13

visualization, I can share that with you.

1:22:17

If you want an even better visualization, I can share that with you.

1:22:22

So we have this very nice one.

1:22:25

TensorFlow projector. Here you

1:22:27

here you can visualize can. So big picture idea is clear. Big picture idea is basically this.

1:22:35

This your big picture idea. All of you can see this one.

1:22:39

Now we're, we're only word vectors

1:22:41

about. This is the big picture idea. When you do word embedding, you will get something like this.

1:22:47

A man, a lion. So lion is something we can understand. But machine

1:22:51

this is to understand. Machine to what? Machine can't. Machine can't. The machine

1:22:53

can't what lion, the tiger, sometimes. Machines will understand these words.

1:22:57

the vector of numbers. Machine

1:22:59

can't just number. So that

1:23:01

that's not that lion, that lion, that means

1:23:03

that point one, point one, point one.

1:23:05

Point, point one. This is basically word in between. You're

1:23:11

representing that word in a vector format. How is this vector coming?

1:23:14

This vector is generated by a neural network. Neural network. Neural

1:23:17

Network's here. And then the best part is that

1:23:21

what you can do, you can represent this data in our coordinate plane.

1:23:24

Now, you can't coordinate x-axis, y-axis in

1:23:27

and this was back in 2030,

1:23:30

the first time that humans were able to

1:23:32

represent words in a mathematical way.

1:23:34

This is before we didn't. This is something

1:23:37

and it's fascinating, no, like

1:23:38

humans were so advanced and we had so much advanced technology,

1:23:41

but we had no mechanism of doing that.

1:23:45

But starting 2013,

1:23:47

starting with this Google's model,

1:23:49

as Google has it opened-source

1:23:50

I think, I'm mapping here, you know,

1:23:53

you know, like Google has it opened source

1:23:55

did it, they open source this word to back model.

1:23:57

First time, we were able to represent every

1:24:00

world on this particular coordinate space.

1:24:03

Now, look, you're, this lion is 0.11.

1:24:06

So lion here.

1:24:09

So this is F1.

1:24:11

0.11 and F2.2.

1:24:13

Okay, guys, let me connect the story back to deep learning.

1:24:16

This F1 and F2, you know, they're hidden features.

1:24:19

So if you're, I think this may

1:24:20

there's a little confusion can be, but I'll clarify that also for you.

1:24:23

So internally behind the scenes, what are going to?

1:24:27

You have a word lion and you can think of it like a hidden feature.

1:24:32

These two hidden features are.

1:24:33

You have one, H1, H2, and these two hidden features

1:24:35

value point one is, and point one-two.

1:24:40

So this is your word embedding.

1:24:42

Neural network is getting used behind the scenes.

1:24:45

Okay, just to clarify it.

1:24:46

And now you are able to plot it.

1:24:48

This word lion is, this point one-one is its value

1:24:50

and point-one-two is value.

1:24:52

This is the tiger is point one is the value.

1:24:55

0.11 is it value. And the best part is that

1:24:59

you can you can start to find synonyms antonyms of your data.

1:25:03

Now synonyms antonyms can make them.

1:25:05

Now, these are words which are very similar.

1:25:08

All these words are very similar.

1:25:09

Lion, cat, tiger, all similar. And the word plane is very different.

1:25:13

So words like lion, catch, tiger are very similar.

1:25:15

And words like plane are very different.

1:25:17

Now, this is so a represent can't.

1:25:19

That's the beauty of, you know, how.

1:25:22

we, how we go back and get word embedance.

1:25:25

And now with this analogy, I think you'll be fascinated by looking at this one.

1:25:32

Let me think the link to one of you.

1:25:34

So what I wanted to show you are a couple of, this is again a Google project kind of thing.

1:25:41

This is also quite old.

1:25:42

It's not, not new at all.

1:25:44

So, Dek Satyo, again, we have a particular word.

1:25:49

And if I search for words,

1:25:51

every dot is like a word.

1:25:53

Every dot is like a word.

1:25:54

Now, look, this is a word.

1:25:56

This word.

1:25:57

And you have represented these worlds in a three-dimensional space.

1:26:01

So we have basically taken every word,

1:26:05

just like how we discuss the word,

1:26:07

and we have kind of represented that word,

1:26:10

the vector of numbers.

1:26:12

And because every word is a number,

1:26:16

that we have coordinate axis represent present.

1:26:19

That's what we did.

1:26:20

We have,

1:26:20

we did.

1:26:21

actually we did here. But here if I search for the word, I'll give an example to you.

1:26:27

If I search for the word piano, very impressed you. If I search for the word piano,

1:26:33

you will start to see, you will start to see words very similar to piano.

1:26:38

The piano, after representation, and you are able to see words very similar to that.

1:26:42

You say organ, keyboard, synthesizer, melanchor, trumpet, flute, bass, and you can understand.

1:26:47

Like, these are all musical instruments.

1:26:49

So, so somehow, the machine has understood that context in which the word piano is used.

1:26:57

Because this all training has trained it on billions of text data.

1:27:02

It is seeing, like I explained to you here, they're seeing, okay, what are the different ways

1:27:07

piano is getting used?

1:27:08

How are piano used are used are.

1:27:10

It is able to see, okay, the word piano is getting used in this context.

1:27:14

So these are musical instruments, these are composers.

1:27:17

Here there's a composer. Here there, there's a composer.

1:27:17

There are a composer.

1:27:19

Mozart was a composer. Where is it? Now, there's something. Yeah, you can see Beethoven. Can you see?

1:27:27

Beethoven? Now, now, now, Beethoven case after, look, said to. Or some, um,

1:27:32

there's, here here. Here, look, Beethoven, here. Here, look, Beethoven, has got. Mozart

1:27:37

, is right? Very interesting, right? Yeah. See, all these are part of the same cluster.

1:27:44

Can you see, very beautiful, right? Now, actually, this go through D in, it's more better.

1:27:49

I think it's more better. So, I'm sorry, guys, I think something not messed up.

1:28:12

So, yeah, no, I said, so you know, I said a hundred and all points and, you can see, very interesting.

1:28:17

Here here here, all these are music and instruments. These are all.

1:28:19

composers, genres, all these are coming similar.

1:28:24

Ankit, absolutely. New word, ah, absolutely. That's what, what's going, obviously.

1:28:27

New word is getting added, so you can't. Yeah, absolutely.

1:28:31

Okay, I hope this idea is absolutely clear to all of you. So we talked about what is

1:28:34

word embedding. Word embedding, heck yeah. This was a fascinating discovery back in

1:28:39

2013 by Google. Google was the first company that came out with this. And now that we

1:28:47

understand word embedding, now that we know how to

1:28:49

represent word as a vector of numbers. We can also represent entire sentences as a vector

1:28:57

of numbers. Yes, I'm word embedding can represent every word as a vector of numbers. We can also

1:29:04

represent every sentence as a vector of numbers. Some sentence embedding be can. You might be wondering,

1:29:10

that sir, how can't. So, okay, example, let's take example. Then you. Then you're relate to okay. So

1:29:17

all this file, we talked about this with respect to the word work, right? So, let's say for a minute,

1:29:23

the word work is a vector of two numbers, okay? 0.1, 0.2. This two number is, okay? Let me write it

1:29:33

this way. Point 1, 0.2. It's a vector of two numbers. Similarly, the word 2 is a vector of two numbers.

1:29:41

0.01, 0.02. Everyone is able to relate to it. This is word embedding that we discussed.

1:29:47

As we've made word worth for it's time since you explained here,

1:29:50

similarly, we will do this process with all the words.

1:29:53

Jit many words are, all the words, you can't all the words

1:29:55

of all the words, you can't make, and overall the sentence

1:29:58

are, you, you can average and sentence vector

1:30:00

can't make. And that was a very powerful angle.

1:30:04

Individual word vector is okay. I can understand that

1:30:06

word, in what context in. Can I understand their individual word embedding?

1:30:12

And now the best part was that, I was able to

1:30:15

look at that whole sense.

1:30:17

sentence as a whole can understand that the sentence

1:30:21

so all of a sudden we were able to represent that sentence as 0.07.1.

1:30:27

Now this again means nothing to the human being.

1:30:29

Now we have you said you don't understand, right?

1:30:33

We understand language, English. But machines will understand this very

1:30:36

way. The same way I talked about word embedding.

1:30:40

You can represent words in a coordinate space.

1:30:43

Sentence embedding or document embeddings. You are all of a sudden able to represent

1:30:46

entire sentences on a body next phase. And all sorts of interesting things started

1:30:51

happening now. You can find clusters of similar news stories, clusters of similar sentences,

1:30:56

and all that stuff. Just like I was discussing clusters of similar words,

1:31:00

say piano, Beethoven, keyboard, synthesizer. Similarly, you know, with sentence and bidding,

1:31:06

we are able to get clusters of similar sentences. That's the idea. And this was a very,

1:31:12

very powerful discovery that was made that time. Okay. So let's connect the dots back.

1:31:16

So you have your word here. We talked about word embedding.

1:31:21

And you can see a word embedding can have hundreds of values.

1:31:25

Each representing a different aspect of a word's meaning, I told you already, right?

1:31:29

You can have hundreds of values.

1:31:31

Okay? Just as you describe a house-wise characteristics,

1:31:36

the values in an embedding quantify a word's linguistic features.

1:31:41

So what's context is what? It's the matter.

1:31:43

What's the matter. I mentioned to you, right?

1:31:46

from the beginning that this is generated by the hidden layers of a neural network.

1:31:51

And this is what I say. Just as you might describe a house, that

1:31:53

the house, like, the home's characteristics,

1:31:54

where location, bedroom, bathroom,

1:31:56

here we are trying to find the inner meaning of a world.

1:32:00

Inner meaning, but what is the hidden meaning of that world?

1:32:02

The word work is, what's the meaning? The hidden layers are describing these things.

1:32:07

So this is the intuition.

1:32:12

And this is like a vector of, we can say this is like a vector of 20 numbers.

1:32:16

Is it like 0.1, 0.2, 0.3, like that.

1:32:18

It's a random example that we have taken right now.

1:32:21

Okay? And you can here here you can see.

1:32:23

The way these characteristics are derived means we do not know exactly what each value represents.

1:32:30

As I told you, now, deep learning in hidden layer of the matter,

1:32:32

what I explained in the first demo, Andrew's demo.

1:32:37

Okay, no know.

1:32:37

We don't know. We've got that affordability, awareness, perceived quality.

1:32:40

We've initially example here.

1:32:41

But actually, what's not.

1:32:43

Actually, the machine is trying to come up with those hidden features.

1:32:46

That's just a mathematical formula.

1:32:49

So, it's what's the matter of that we don't know.

1:32:51

But words are expected to be used in comparable ways.

1:32:55

Words which are you, which expect to be used in comparable ways,

1:33:00

often have similar looking embeddings.

1:33:03

This is exactly what I explained a while back,

1:33:05

piano, Beethoven, synthesizer, like that.

1:33:07

Same idea.

1:33:10

Now, you can you can't see here.

1:33:12

Sea or ocean are really similar.

1:33:14

This is the same story I talked about here.

1:33:15

Same story.

1:33:16

like lion, cat, tiger are very similar, whereas plane is very different.

1:33:21

Same story here.

1:33:22

If you're a word embedding case of us see if you're see and ocean are two different things, right?

1:33:28

See and ocean are two different things.

1:33:30

Lekin, if you're embedding case up to compare to see, see,

1:33:33

the word embeddings for sea and the word embeddings for ocean seem to be very similar.

1:33:38

So we can say they are contextually very similar.

1:33:41

The word embedding for football and the word embedding for soccer are very similar.

1:33:45

So we can say they are contextual.

1:33:46

very similar. They mean the same thing.

1:33:49

But if you might be saying,

1:33:52

you might be saying, how can't understand they're similar because we are comparing the scales.

1:33:56

This is a heat map. You have seen, right? You have seen, right? So we are putting a scale.

1:34:02

We are saying if it is zero, if the number is zero, it is blue. If the number is one, it is red.

1:34:07

So we're we're just in scale in. So this would be something like, what, point seven

1:34:11

this point seven, this point one, this 0.1, this, this 0.9

1:34:17

how it's such a, this. This is how the numbers would be.

1:34:23

If you compare the numbers of sea and if you compare the numbers of ocean in a similar way,

1:34:27

it's quite similar. That's what I'm getting at.

1:34:33

So even if we do a typo, how can they fetch the correct contact most of the time?

1:34:36

Let's say, let's say word key, word is it the same thing.

1:34:40

Yeah, word and word is something very different.

1:34:43

Work and word is something very different.

1:34:46

So we will see that.

1:34:47

We will see that.

1:34:48

But if you make a mistake, if you say,

1:34:50

work, you're in a word, you say, word-embeding will be very different.

1:34:55

Right now, we're just talking about word-embeding,

1:34:56

that word-embeding of what?

1:34:59

Okay?

1:34:59

You have a, you have a sentence.

1:35:02

First, we're the sentence how we're,

1:35:04

we're basically seeing this journey right now.

1:35:05

Yes, we are basically seeing this journey right now.

1:35:08

Machines individual sentences,

1:35:09

I don't know what you can't know. Machines

1:35:11

to full sentence

1:35:13

to understand, if you're

1:35:15

asking us as far as we're asking,

1:35:17

that we, sir, we're

1:35:18

we, we're just the prompt

1:35:18

in chat GPT, let's say you ask a question,

1:35:22

what is the temperature today?

1:35:23

This is a very long sentence, right?

1:35:25

So this sentence has individual words in it.

1:35:27

What is the temperature today?

1:35:29

That sentence in that sentence

1:35:29

can't be quite individual words

1:35:31

be you, you can't.

1:35:33

So machines are not processing the sentence first.

1:35:35

Machines are processing the individual words first.

1:35:38

Now, what,

1:35:39

the embedding what is east

1:35:40

embedding what? Da'a embedding

1:35:42

what? Temperature to embedding

1:35:44

what? Today's embedding what? So we are looking

1:35:47

at each and every of the individual

1:35:48

words that we have.

1:35:52

And based on that, we are trying to work.

1:35:54

So that is how we are

1:35:56

kind of looking at the whole thing.

1:36:02

Okay.

1:36:09

Okay, Uncle, I hope that clarifies.

1:36:18

So word and work will have the same, you know, different embeddings.

1:36:23

So basically, you know,

1:36:26

so word-ca embedding

1:36:27

so the prompt you're writing in chat, GPD,

1:36:29

whatever prompt you're writing in chat, GPT,

1:36:31

whatever question you're asking in chat dpt,

1:36:33

you would take sentence in.

1:36:35

But the key takeaway of the conversation should be,

1:36:38

everybody should understand.

1:36:39

and to a sentence's vector

1:36:40

what is I think that we should all make too.

1:36:43

Because then we've

1:36:44

we've been word embedding discussed

1:36:45

that the word work is nothing but a vector.

1:36:48

But you're just

1:36:48

sentence that sentence is also a vector.

1:36:51

You're just chat GPD in a prompt

1:36:53

when I go to chat GPT and when I start

1:36:55

typing this, I'm going to chat GPD

1:36:57

and I'm typing something.

1:36:58

I'm going to chat GPT and I'm typing something.

1:36:59

I think what is the

1:36:59

what is the weather tomorrow?

1:37:03

When I type this thing,

1:37:05

you know, what are you?

1:37:05

What are GPT is reading English?

1:37:07

No, chat GPT doesn't go English.

1:37:09

He has no English

1:37:09

not yet.

1:37:10

So internally what is going on.

1:37:12

This is exactly what is going on

1:37:14

internally.

1:37:14

You're all the entire thing

1:37:17

is getting converted to tokens.

1:37:18

What is the whether tomorrow

1:37:20

five tokens are?

1:37:21

We're basic assumption

1:37:22

that every word is a token.

1:37:24

There can be other forms of tokenization

1:37:25

we will discuss later.

1:37:26

But right now, every word is a token.

1:37:28

So five tokens are and

1:37:29

every word's individual embeddings

1:37:31

are you can.

1:37:33

So we talked about word embedding.

1:37:34

Every word you can convert

1:37:37

to a vector of numbers.

1:37:38

So this entire

1:37:39

sentence, we can convert it to a vector of numbers.

1:37:42

So this sentence embedded

1:37:42

so basically whatever we are typing in English right now,

1:37:45

this whole thing we're in English

1:37:46

type is, it's basically value

1:37:48

is 0.11, 0.22.

1:37:52

Okay, I'm just giving a very broad example.

1:37:54

So this is your internally chat GPT

1:37:56

can enter chart. And if you're

1:37:57

if you're asking, sir, big picture idea

1:37:59

what is that? Now,

1:38:00

that's what are, okay?

1:38:01

So internally, when you're

1:38:03

you're here here per

1:38:04

so chat GPT is converting this

1:38:07

into a vector,

1:38:07

this is getting processed through a neural network.

1:38:13

A neural network is

1:38:14

that, what's processing.

1:38:16

And based on that, it is giving a response back.

1:38:19

That is what you're seeing in English.

1:38:20

Out-put are you.

1:38:21

But behind the scenes, this is all right.

1:38:24

So what is getting sent is in a numeric form

1:38:26

as sentence embeddings, word embeddings,

1:38:29

and neural network is taking that input.

1:38:33

It is extracting the hidden features,

1:38:35

whatever I explain.

1:38:36

That sentence,

1:38:37

the word is the inner meaning

1:38:39

what's context, all that is being

1:38:41

fetched and based on that you're getting

1:38:43

the response back.

1:38:44

So that is a big picture idea

1:38:46

how it is working behind the stage.

1:38:49

Okay, I'll further clarify this in more detail.

1:38:52

Let's move on.

1:38:55

As I discussed, a pair of words like

1:38:57

C and lotion, for example,

1:38:59

may not be used in identical context, but they're similar.

1:39:01

The ideas are very, very similar.

1:39:04

So we have already discussed here.

1:39:06

This is the same thing I tried to explain.

1:39:07

through that beautiful tens of flow projector demo.

1:39:10

I'm the piano one up to explain here.

1:39:12

The same thing we are trying to show here.

1:39:13

You can try to form clusters of similar words.

1:39:15

Now, look, bus, train, or car is quite similar.

1:39:18

They are all used in the same context.

1:39:21

And our college, school and work are similar.

1:39:23

Walk, swim, ran are similar.

1:39:25

Okay, these are very, very similar words we are able to see.

1:39:29

That's intuition.

1:39:31

Now, all this is great.

1:39:34

All this is amazing.

1:39:36

But now,

1:39:37

We're going to go to the next phase.

1:39:39

Okay.

1:39:40

Oh, but this alone is not what makes large language model so clever.

1:39:47

Yeah, so, okay.

1:39:48

Words are.

1:39:48

It's a number in, word embedding.

1:39:51

Sentence we've made vector in.

1:39:52

And something's going to do.

1:39:53

But what's what are going to see a little bit more.

1:39:57

Intuitively, some jargon's we will introduce,

1:40:00

and we will see what the transformer architecture exactly is.

1:40:03

Transformer is what is what we'll see.

1:40:07

So this is very nice time.

1:40:10

But what else do we have that makes LLM so clever.

1:40:14

What unlocked their abilities to parse and write as fluently as they do today is a tool

1:40:21

called the transformer, which radically sped up and augmented how computers understood language.

1:40:28

Now, I want to warn you on one thing.

1:40:32

Principles, same here.

1:40:33

Either be your token say, either be your word embedding going to, same thing.

1:40:36

Same to same thing.

1:40:37

But what else is happening? I'll show you. I'll show you intuitively here.

1:40:43

There's something more, something more over and above what we discussed.

1:40:46

Okay. Now here is the interesting thing.

1:40:48

Transformers process the entire sequence at once.

1:40:53

Yeah, part by part analyze not.

1:40:54

Abidak, what we were doing is that we were saying,

1:40:57

huh, that you have a sentence. We will go to work.

1:41:00

Why we're discussing are right? And we were doing it part by part.

1:41:04

We have, us kind of embedding.

1:41:05

We have embedding. We are.

1:41:07

We were looking at the words individually, right?

1:41:10

We were looking at the words individually.

1:41:11

That, bro, work-the-word embedding what?

1:41:14

V-Q-W-W-E-C-W-E-Wod embedding what.

1:41:17

Find out the individual word vectors and then create a sentence vector.

1:41:22

That is what we were doing.

1:41:24

But in Transformer, the thing that got revolutionized is, it processes the entire sequence all at once.

1:41:31

That whole sequence, that is what transformers do.

1:41:36

And this allows us to.

1:41:37

capture the context a lot better.

1:41:39

And that is exactly what I'll be talking about in the next phase of my discussions.

1:41:42

I will talk about transformers, transformers, how they led to large language models.

1:41:47

Every large language model is fundamentally based on transformer.

1:41:51

And from that, we will see a small example of a large language model in action.

1:41:55

This is the general agenda.

1:41:56

But you guys want to take a small break.

1:41:58

We've been going on for a long time.

1:41:59

So 9.30 on the clock, take five minutes, all of you.

1:42:02

So a lot of jargons and all we are discussing, I know.

1:42:04

So take a breather.

1:42:06

Five minutes, we'll take a breather.

1:42:07

come back, okay? Yeah. Take some water. Five minutes break and we come back. Okay. Yeah.

1:42:37

Thank you.

1:43:07

Thank you.

1:43:37

Thank you.

1:44:07

Thank you.

1:44:37

Thank you.

1:45:07

Thank you.

1:45:37

Thank you.

1:46:07

Thank you.

1:46:37

Thank you.

1:47:07

Thank you.

1:47:37

Thank you.

1:48:07

Okay.

1:48:14

Okay.

1:48:16

Okay.

1:48:17

Welcome back.

1:48:37

In a minute.

1:49:07

Okay. So we talked about, so now we'll start our conversation with the

1:49:21

with the idea of the idea of the transformer, what it is the idea of the transformer, what it is and how it is different.

1:49:28

So we talked about word embeddings.

1:49:29

We talked about looking at the words individually and from that we are getting the sentence embedding.

1:49:35

So what the idea clear.

1:49:37

Now the question is, transformers will not process those words individually.

1:49:43

Transformers will process the words together.

1:49:46

Okay?

1:49:47

A key concept of the transformer is something called attention or you see attention say it is able to look at all the words together over on.

1:49:54

So for example, if you have a particular sentence, I have no interest in politics.

1:50:00

We were taking each and every word out and we were analyzing that word separately.

1:50:05

if I have the word embedding, no, no, interest, what you are combining it.

1:50:12

But in transformer, what we are doing is it is it is parallelly, it looks at each token.

1:50:17

How many tokens? There are six tokens, right? Six words, six tokens. On an average, generally. I mean,

1:50:21

again, tokenization can vary. But here we are saying, okay, one word is each token. In the simple demo,

1:50:27

we are seeing. Okay. So self-attention looks at each token and decides which others are most important in

1:50:35

understanding its meaning. So you are looking at the word no and you're looking at the relationship

1:50:41

of the word no with all the other words in the sentence. So it is looking at the sentence,

1:50:49

looking at a particular word and trying to understand how is that word related to the other words

1:50:54

in the sentence. And that's the intuition of what self-attention is basically doing. So the transformer

1:51:02

are computes all the words in the sentence at the same time.

1:51:07

Just you have, look, here it is looking at the word I.

1:51:09

I can say I'll do one of them for you, okay, so that you can relate to it.

1:51:13

Okay. So we can see that, you know, we are doing the connection from I to have, I to know,

1:51:19

I to interest, I to in, or I to politics.

1:51:23

Some of that relationship's summarized.

1:51:25

Okay, and guys.

1:51:26

Similarly, I'm trying to understand what is the relationship of have to I, have to know,

1:51:32

have to interest, have to in, or have to what I'm getting at. So we are trying to understand

1:51:38

the relationship of each and every word with respect to the other words. Yeah, we're

1:51:43

not looking at the word individually with respect to the entire vocabulary of words. But here

1:51:48

we are looking at the words in the same sentence. Okay, and this is exactly where the context gets

1:51:53

a lot strong. So capturing this context gives LLM's far more sophisticated capabilities to parse

1:52:00

language. And in this example, you can see assessing the whole sentence at once means that

1:52:06

transformer assessing the whole sentence at once. This is what we were discussing.

1:52:11

We're alack say word-wise ne'am word. We are looking at the word and we are trying to understand

1:52:16

the relationship of that word with respect to all the words in the sentence. Or sara words

1:52:21

that each part. So assessing the whole sentence at once means the transformer is able to understand that

1:52:29

interest is being used as a noun to explain an individual's take on politics.

1:52:34

Here here interest of the matter of much more. Whereas if I use this in a different context,

1:52:39

if we're looking at the bank's interest rate rises. If we tweak the sentence, then the word

1:52:45

interest is now used in a financial sense. And this is the beautiful thing that transformers are

1:52:50

able to achieve.

1:52:52

Age concept is the same thing. If you're

1:52:54

if you're going to high level in the same thing. Concept is the same thing. Concept is basically the same thing.

1:52:59

You are looking at a sentence and this sentence is ultimately nothing but a vector.

1:53:03

0.11.1.2. Everything boils down to this.

1:53:08

But this is what transformers are particularly doing. They're processing the entire sentence together.

1:53:15

They are trying to understand the relationship of every word with the neighboring words.

1:53:19

The end result is this thing. 0.11.1.2.

1:53:24

Of course, sentence vector will jay. So next time you write a prompt in chat GPT.

1:53:27

If you're in a prompt link what is the weather tomorrow.

1:53:30

The same thing I explained to you.

1:53:31

This is the same story.

1:53:34

But the processing is different.

1:53:36

Then normal technique we have a different word's separate process

1:53:39

but here you are processing every word with respect to the other words

1:53:43

and you're getting that entire embedding.

1:53:44

But the end result is the same.

1:53:45

End result is that this whole sentence can embedding

1:53:48

go to point one point or something like that.

1:53:50

This is the whole sentence embedding that you're getting something of that sort.

1:53:55

I hope the clarity is there.

1:53:57

And if we combine the sentences, this is the best part.

1:54:00

This is the best part where transformers really excel.

1:54:03

And this is one area where the normal word embedding models used to create a problem.

1:54:09

But if same word sentence may use in different context, the model is still able to recognize the correct meaning of each word.

1:54:18

Thanks to the attention, it gives the accompanying text.

1:54:21

This is the first limitation there.

1:54:23

2013 where when the original word embedding model, we were looking at individual,

1:54:27

individual words.

1:54:28

If you're like, then interest of embedding same,

1:54:30

the interest of the same over.

1:54:32

That was a problem, right?

1:54:33

But now, even if you use both the words,

1:54:36

the same word in the same sentence,

1:54:38

both the meaning is different.

1:54:40

The first use of interest, it is this and in that are most attended.

1:54:45

You can see this is.

1:54:46

I have no interest.

1:54:46

I mean, you have no interest.

1:54:48

And the second interest is basically the financial institution.

1:54:51

They're two completely different contexts.

1:54:54

The functionality is critical.

1:54:57

Without it, words that can, so this is the word to back part, as I told you.

1:55:02

So interest, the enthusiasm, encouragement, similar words, or interest.

1:55:06

Oh, your profits, dividends, you know, rising interest will relate to this.

1:55:09

That is where the embedding part will come up.

1:55:12

I hope everyone's getting the idea in terms of what,

1:55:17

what transformers are, what word embeddings are, and how we eventually take a prompt

1:55:22

and basically, you know, convert that prompt into a vector of numbers.

1:55:25

That's the basic.

1:55:26

And this is, this is.

1:55:27

we can keep going on. The article keeps going on, but I think this is going to be more advanced

1:55:31

going forward. So the capability goes beyond words, like interest, that have multiple meanings.

1:55:37

Now, this is an example. The dog chewed the bone because it was hungry. He cannot. The dog

1:55:42

chewed the bone because it was hungry. This is your example. So, yeah, we have to transformers

1:55:47

process can. And, you know, you can, the end result could be, the whole sentence will give you a vector of

1:55:52

numbers. Okay, that is the thing that will happen. Now, in the following sentence,

1:55:57

Self-attention, though whatever transformer thing, is able to calculate that it is most likely

1:56:03

referring to dog.

1:56:04

What the word is the word? It's the most likely referring to dog. It's able to understand that.

1:56:10

More context have. Because remember, we are trying to learn the relationship of every word.

1:56:16

With every other word. It-kees-kees-as-was, it-ke-hungary, it-ke-ke-ke-se-be-because, because-it-ke-ke-ke-sard-bone,

1:56:21

it-it-case-sad-huh? So this will, it-a-ha-ha-ha-ha-ha-ha-ha-ha-ha-ha-ha-ha-ha-ha-ha-ha.

1:56:27

Now what I will do?

1:56:30

If we alter the sentence, swapping hungry for delicious, the model, the model is able to recalculate it.

1:56:41

And now what is the dog chewed the bone because it was delicious.

1:56:44

Ab-eat-a-a-eat-a-a-me-a-it-a-mot-me-a-a-h. So this is very interesting, nah?

1:56:48

The dog chewed the bone because it was hungry.

1:56:52

What we did? We just hungry to replace here? It's incredible, right?

1:56:56

Just one bone.

1:56:57

I replaced and its whole context changed.

1:56:59

The word, eat now refers to something else.

1:57:02

Here, it means dog. I hope all agree.

1:57:05

Nobody will debate on English, right?

1:57:06

It's all hungry.

1:57:08

Now, dog's a book like, then we chewed the bone, right?

1:57:10

everyone's able to relate to it.

1:57:11

But, observe this, observe the flow all of you.

1:57:15

Now, we'll just do it again, we'll delicious for it.

1:57:16

That's it.

1:57:17

I will simply replace hungry with delicious.

1:57:20

Simple.

1:57:21

Now, look, just.

1:57:21

Just one word changed one.

1:57:23

The dog chewed the bone because it was delicious.

1:57:27

Now, what is?

1:57:28

Eat, what the dog was delicious?

1:57:29

No, because the bone was delicious, right?

1:57:31

It was able to understand the context of the word with respect to the other word.

1:57:36

But the end result is what is?

1:57:37

just we're just about all this.

1:57:40

The end result would be that entire sentence can still be represented as a vector format like this.

1:57:48

Because, you know, machines will not understand all that we are discussing.

1:57:51

We're saying, we're saying, it's cute, it delicious.

1:57:54

Machines will not for that.

1:57:54

Machines will just understand that.

1:57:56

Okay.

1:57:56

It's the way how machines would understand it.

1:58:01

You will not see all this.

1:58:04

You will see applications, real application.

1:58:06

But this is the inner details of what is going on at a high level.

1:58:09

So that at least people can connect the dots.

1:58:10

How is it happening behind the scenes?

1:58:14

And you can see the benefits of self-attention for language processing increase.

1:58:19

The more you scale things up.

1:58:21

It allows LLMs to take context from beyond sentence boundaries,

1:58:25

giving the model a greater understanding of how and when of what is used.

1:58:30

This is very interesting.

1:58:31

And if you see, this is exactly what I was mentioning before,

1:58:33

that you're training this on like billions and billions of text data.

1:58:37

And once you do that, once you start to show it, many, many examples of eat, chew, bone,

1:58:41

it tries to understand context and it tries to understand that,

1:58:45

the dog chewed the bone because it was delicious.

1:58:47

And more, like, you know, like, you know,

1:58:53

you know, abu bone chew, you know, you, you, you, you, you associate the things about the dog.

1:59:01

The dog chewed the bone.

1:59:02

It had a red collar.

1:59:04

It was his owner's best friend.

1:59:06

It loved playing pitch.

1:59:08

It ate dinner at six minutes.

1:59:09

The dog-related or be relationships learn for probably.

1:59:13

And that's the interesting thing.

1:59:14

Oh, absolutely, I see it.

1:59:15

The concept applies for other languages also.

1:59:17

If you look at Hindi language and all that, Germany supports multiple languages today also, right?

1:59:22

So the same idea applies.

1:59:24

Everything is based on associations.

1:59:27

I started my session today with associations, you know, like the word piano.

1:59:31

The word piano is related to all these.

1:59:32

This is what it is.

1:59:33

It's association something like.

1:59:36

Like an Apple mobile and an Apple product.

1:59:39

Exactly, exactly.

1:59:39

Don't know.

1:59:40

Alachshida.

1:59:41

Correct.

1:59:41

Just like the bank example where I talked about.

1:59:43

Bank riverbank be hosta, bank, bank financial institution.

1:59:45

It is learning the context ultimately.

1:59:48

It's learning the context.

1:59:49

Like an end result?

1:59:50

What is the end result?

1:59:51

End result is basically, the end result is basically this thing.

1:59:57

Okay.

1:59:58

So if I talk about the overall end result of what we are achieving,

2:0:04

let's go back to chat GPD.

2:0:07

The end result would be this.

2:0:08

You're having a particular prompt.

2:0:11

This is what is called a prompt typically.

2:0:13

Whatever input you're giving is typically called a prompt or an input.

2:0:17

That prompt is going to get process.

2:0:19

But remember, the prompt is text data.

2:0:21

Machines don't understand X data.

2:0:23

So he internally what can't do?

2:0:25

ChatGPT in there.

2:0:26

Go internally,

2:0:27

it's up on top attention.

2:0:29

All this, it will do.

2:0:29

Transformers will be working behind the scenes.

2:0:32

All that is happening behind the scenes.

2:0:34

They will convert this entire sentence into a vector form.

2:0:39

And this and on the basis of that, I will get my response back.

2:0:44

So this is how it is working behind the scenes.

2:0:47

So next time you think of a large language model and slowly I will transition

2:0:51

you know, into the concept of a large language model.

2:0:54

What is a large language model?

2:0:57

An LLM.

2:0:58

And an LLM.

2:1:01

So a large language model is basically what?

2:1:04

We have a sequence of data.

2:1:06

And on the basis of this entire sequence of data,

2:1:10

we are trying to predict something.

2:1:12

We are trying to predict some output.

2:1:13

And that is what a large language model is in here.

2:1:15

So we also have a particular sequence of data.

2:1:18

And on the basis of that particular sequence of data,

2:1:20

sequence of data. This is what we are actually doing.

2:1:24

And this is basically like a very small kind of a, you can think of it like a very small historical,

2:1:32

historical timeline that you can think of. So word to back came out in 2013, right?

2:1:39

So this is the part where we started understanding the meaning of words, the context of words,

2:1:46

some words go individually so much prior. Then 2014, we had neural networks.

2:1:50

RNNs are a kind of a neural network.

2:1:52

So this was an old concept.

2:1:53

We don't use it today that much tickets.

2:1:56

So it was, neural networks were also used to process text, what we discussed briefly.

2:2:00

And then the more modern approach in 2017, the Transformers paper was written.

2:2:06

So 2017, a very, very famous paper was written.

2:2:09

If you want me to give you the reference to that, this was actually the paper that was written.

2:2:15

So again, these are deeply technical concepts, but just in case some of your curious,

2:2:20

can read about it. This was the original paper on Transformers. And this is, I would say,

2:2:25

it will easily rate as one of the most, one of the most fascinating discoveries of human,

2:2:30

humankind. Okay. So without Transformers, we will not be where we are today. This was one of

2:2:36

the most, the most revolutionary papers written. It was originally published and submitted on

2:2:43

2017, and 2017 is when Transformers were born. Okay, so Transformers when this very special type of

2:2:50

a neural network that were able to look at the entire collection of words, whatever

2:2:57

sentence you are giving, it was able to process this entire collection of words,

2:3:02

and it was able to understand this entire collection of words in a form of numbers. It was

2:3:07

able to convert that into a numeric vector. And then from Transformers, we ended up into the world

2:3:15

of LNMs and large language models. It is an LLMs evolved from Transformers. Okay?

2:3:20

So all the large language models that we have and the fascinating thing is even GPT.

2:3:25

And GPT's a full form, you know, GPT is a type of a language model.

2:3:31

GPT stands for generative, pre-trained transformer.

2:3:35

So whatever I took all this time to explain, this GPT model,

2:3:41

starting with the GPT model, GPT model was first released back in 2018.

2:3:45

So 2018, there were two fascinating models that

2:3:50

released that timeline I did not give here but 2018 is when open a i released

2:3:56

gpt gpt version one that time gpt version one ron launched

2:4:01

and google launched something called b e rt the birth model both were transformer-based

2:4:08

model. Now that 2018 open a.mai, nobody knew open a i know i didn't know either

2:4:15

i didn't know either. I was not working that actively in deep learning space that

2:4:18

generative is based at that time.

2:4:20

Only the last four, five years, we've been very actively researching.

2:4:23

2018 was too early.

2:4:25

Too early, honestly, like, I was also very young back then, you know.

2:4:29

Yeah, so that was like too early.

2:4:30

I was working on deep learning, computer vision, that kind of work, but not in generative way.

2:4:34

It's very new that time.

2:4:35

Okay.

2:4:36

And the interesting part is this was based on transformers.

2:4:41

Generative, pre-trained, transformer.

2:4:42

And this is in version one.

2:4:46

You know, today what do we have to do we have to date?

2:4:48

guys. What do we have today? So today we have the latest and the latest versions of chat

2:4:53

gpt. So today's version of chat gpt may be. Right, you can, you can, so even in today's

2:5:00

version of chat gp2, whatever version of chat gpt you have today, even in today's version of chat gpt,

2:5:05

we call it gpt or generative free train transformer. I will take you to the open AI platform for

2:5:12

a minute just to show you, just to show you. So it was a transformer base model back then and it

2:5:18

it continues to be a transformer-based model even today.

2:5:21

So we have the latest GPT 5.5 model today.

2:5:23

This is the latest one.

2:5:25

Latest one.

2:5:26

Here here.

2:5:26

It was called GPT back in version 1.

2:5:30

It was called GPD back in version 5.5.

2:5:32

And it is still based on the same transformer architecture,

2:5:35

which is nothing but a neural network working behind the scenes.

2:5:39

Now going forward,

2:5:40

Age Javan we're regarding these topics.

2:5:43

You don't need to, you know, get into any of these theoretical things and all that.

2:5:48

But you should all have a, I would say, a very broad understanding of the whole stack.

2:5:53

You know, you know, we're getting to any of our demos and case studies and whatever.

2:5:59

You're writing a prompt.

2:6:03

That prompt is typically in input.

2:6:06

And that prompt is getting sent through some black box.

2:6:09

Something going to.

2:6:10

Detail in detail, you know, you're just about what you're going to.

2:6:12

We spend a lot of time discussing all that.

2:6:15

But now you know that.

2:6:16

Now you know that prompt is getting converted to our vector.

2:6:18

of numbers that prompt is getting converted to embeddings 0.1, 0.2, 0.5. And you can decide

2:6:26

how many numbers you want here. Okay. The prompt is getting converted to embeddings. This is getting

2:6:30

passed through a very, very deep neural network, very, very deep neural network. And based on that,

2:6:36

you're getting the output response. That's what transformers are doing. Text in, text out. Okay.

2:6:41

And what are large language models? What are LLMs? LLMs are also transformers. LLMs. LLMs are

2:6:48

also transformers. They are transformer-based architectures. Okay. Now, let us see this one.

2:6:54

Now, why do we call it a large language model? What is it? Transformer, okay. But what are we doing?

2:6:58

LLM in a large language model? Why is it called a model? You see, there is a certain amount of

2:7:06

prediction involved. There's a certain amount of prediction that we are trying to do. Okay? So,

2:7:11

see what? The financial times is dash. Okay? At least. At it's simply. At it's simply.

2:7:18

At its simplest, the model's aim is now to predict the next word in a sequence and do this

2:7:26

repeatedly until the output is completed. So this is a very probabilistic model. It may be large

2:7:32

language models and starting with the GPT version 1 all the way to the GPT version 5 model that you get

2:7:37

today. All these LLMs that you see today, they are extremely probabilistic in nature. You're looking

2:7:43

at a sequence of words and based on that sequence of word you're trying to predict the next to.

2:7:48

next word. Next word. So here we have the financial times is dash. So as an example, to do this,

2:7:59

the model gives a probability score to each token. This is, if I have to give you an example,

2:8:03

this is like your predict prober. And I'm a classification here. So we've discussed in classification

2:8:07

has the concept of predict prober, all of you have discussed, right? So what are we doing in

2:8:12

classification? There also we have a sequence of different different, you know,

2:8:18

We have a sequence of different, different words. And based on that, we are trying

2:8:25

to predict features of a person. Let's a diabetes example. We have the features of a person. And based on

2:8:33

the features of a person, we are trying to predict, will the person, is the person suffering from

2:8:37

diabetes or is the person not suffering from diabetes? We discuss predict proa. So a probability

2:8:42

a probability basis we are assigning.

2:8:44

Other we are doing that we are finding out what is the probability of. We are finding out what is the probability

2:8:48

diabetes 60%. If 50% up up, then model was predicting diabetes yes.

2:8:54

If it's 50% is below, model was predicting diabetes no. So ultimately, if was calculating a

2:8:58

probability score, same thing happens here also. When you have a, when you give a sentence,

2:9:04

the financial time says, this sentence is, he's the way story. You have a prompt linked

2:9:09

the, okay? So if you want me to explain, this is, yeah, the financial time says, okay,

2:9:16

I'm here. Same thing. Same story. The financial times is, same thing. So this is

2:9:22

exactly what we refer to as a prompt. We're here just here just here

2:9:26

leave and leave it. So, this prompt is. If we enter

2:9:30

then what will, this entire thing will get processed. tokenization

2:9:34

will go. There go to tokens per

2:9:36

convert over. That poor sentence per vector

2:9:39

going to, point one, point two, point three, whatever. That is how machine will understand

2:9:43

that the sentence of the sentence of what is. And then, right? And based.

2:9:46

On that, it will now predict the other word can. It will try to predict what is the next

2:9:52

word. This is how it will work out. It will try to predict what is the next word. So there are,

2:9:58

there are potentially thousands of words in the English vocabulary. So it will give a probability

2:10:05

score to each token. And whichever word has the highest probability score, you can see here

2:10:10

here. This probability timeline, it's, I mean, it's numeric that is. So you, you can see, you can't

2:10:16

here here, this is zero and this one. The more yellow it is, the probability is closer to

2:10:22

zero. And the more red it is the probability is closer to one. So here here

2:10:26

there probably probability could point nine five type of. Whereas here

2:10:30

here here, it can be something like close to, um, well,

2:10:34

like, point three or point two, something. It'll add up to 100 actually. We have to adjust the number

2:10:39

so you can get it. So this is the higher probability. So the model will predict what? Here

2:10:44

model can predict what? Here the model will predict. The model will predict.

2:10:46

about because about is having the highest probability. So it, and so model

2:10:51

model they about predict here. So first the financial times is about predict here.

2:10:55

Now just he about predict here. Abh, again, it's going to next word predict

2:10:57

can't again. There'll be like thousands of words to choose from. So now, yeah, the

2:11:02

financial times is about. Now looking at these five words, you have to predict what is the next

2:11:07

word. The financial times is about. Looking at those five word by next word, yeah. Next

2:11:11

word here. And it keeps going on and on and on until it is happy with a

2:11:16

text that produced about economics. It will continue predicting and podcast and this,

2:11:22

this and this and it will continue doing this until it's got the perfect answer. And then there are some

2:11:28

more optimized ways of doing this also. And this is exactly what chat GPD also does.

2:11:32

Chat GPT also starts generating a token of text. And what is going on behind the scenes

2:11:40

now we understand, now we appreciate. Those tokens are getting generated because

2:11:45

given a particular input, we are trying to predict. We are trying to predict what is the

2:11:53

probability of each and every word in the output. So financial times is, and when I hit enter,

2:11:58

when I send the prompt, it is trying to predict what that next sequence of words will.

2:12:03

Okay, are they called commonly known as leading newspaper like this, like this, like this.

2:12:07

So this is the way how it's actually happening. So you see how when I do something in chat,

2:12:12

GPD, like tell me more. When I type something,

2:12:15

this is our input. And based on it, it's just completion.

2:12:19

So we'll check text completion. When I hit enter, it is just completing word by word,

2:12:24

word by word, phrase by phrase. It's just complete. Based on that entire sequence is

2:12:28

continuously trying to predict the next word, the next word, the next word, the next word, the next word,

2:12:32

it's going so fast that you're not able to relate to, but that's actually what's going on behind

2:12:36

the same. This is exactly how a large language model, which is nothing but a transformer is fundamentally

2:12:43

operating. This is the concept.

2:12:45

thing. A lot of jargons we have seen today, but

2:12:48

we're going to go,

2:12:49

we'll, today we don't have much of hands-on.

2:12:53

From a little bit of hand-on, but the objective

2:12:56

was to clarify these jargons.

2:12:58

All these jargons are,

2:13:00

you know, are very, very important.

2:13:01

What are all these jargons? And the token part is very important.

2:13:04

The token-wala thing is just to

2:13:07

just to, excuse me, relate to this, all of you.

2:13:11

Okay.

2:13:13

So the

2:13:14

excuse me, the token part is very, very important.

2:13:18

We can use a particular package called tick token.

2:13:22

If you want, I can show you a small hands-on on that also.

2:13:25

You can count can't.

2:13:27

So, I'm to simplicity for you, I told you that every word is one token, but not necessarily.

2:13:31

Not necessary.

2:13:32

Different language models will have different types of tokenization, how they do it.

2:13:38

They will have their own ways of doing tokenization.

2:13:41

But you can relate to that.

2:13:44

So our different, different models will have, you know,

2:13:47

different, different ways how they do tokenization.

2:13:50

But if you want to remember, on an average, it is usually 0.75 words.

2:13:54

Now, why is it important to talk about tokens,

2:13:57

conceptually?

2:13:59

Why is it important?

2:14:01

Because this, what we're doing in chat GPT in, right?

2:14:04

This is exactly not, I mean,

2:14:06

it's free here, chat GPT, the free version.

2:14:08

Like, actually, I have a go version.

2:14:11

Whatever, it's, chat GPT is giving a lot for,

2:14:14

free. And this costs money, right? When you write a prompt, when you ask a question,

2:14:19

what is the weather in India, usually this May to July, everybody saying there'll be a lot of

2:14:30

monsoon this time. The temperance will be lower. That's what they are saying. Typically,

2:14:35

North India, I think it will be lower comparatively. But whatever, if I ask this question,

2:14:39

you know, if I ask this question, what are, what am I?

2:14:44

What are doing? How many tokens are there? This is costly stuff, guys.

2:14:48

You're you, what tokens are? Based on our analogy, one, two, three, four, five, six,

2:14:54

seven, eight, nine, ten, eleven, twelve. Functuation, an act. So, there's a lot. As an example,

2:14:59

as an example, okay, tokenization another way to be. But it internally

2:15:02

is all right. So, this is all right? So, this is getting, going to a neural network. This is getting,

2:15:07

going to a neural network. Now we have it, okay? We have this, we have this is black box. Okay.

2:15:10

Now we have this, let's assume this is the black box.

2:15:14

So this is getting passed to a neural network and it's based on the response. This is all that

2:15:18

is happening. The response, we've seen. So probability-wise, next word, next word, next word, but

2:15:24

all over. Simple, you give a from, under, and you got a response. This is costly stuff. Okay?

2:15:33

This neural network, if you give a very big input, if your number of tokens

2:15:37

you have a neural network to process in a problem. We need a lot of cost and computation

2:15:43

to process your input. You know, two things. Input token is here. And output token is important. You have to

2:15:49

keep both in mind. Okay. So please keep in mind the number of input tokens and also the number of

2:15:57

output tokens. And most of the platforms will typically charge you. Chad GPT be charged. Yeah, chat GPT free

2:16:06

it. As Amit is also saying, 20 dollar cursor, only provides 5 million token. It's the

2:16:10

meaning. You can't use it. Five million might sound very big, but actually it's not big. It's

2:16:16

very small. Five million. Five million is used. That GPT and all are actually in losses. You know,

2:16:22

if you look at Open AI, if you look at their profitability, they are running in losses.

2:16:26

They are highly loss making. One of the most, you know, huh, yeah, basically, highly loss making.

2:16:33

Because this is costly stuff. The more.

2:16:36

tokens, the bigger your question, if your input token is a lot, if your question

2:16:40

is the neural network has to spend more time and more compute to process it.

2:16:46

Jada neurons will be that for somemage to. Because if your input is 100 words long, think about all

2:16:54

that I discussed. Every word association you're trying to understand with all the words.

2:16:57

If your input is it's just a lot, then computation kithn't how much? You're trying to understand

2:17:02

every word with respect to every other word. Can you understand? So it would be very, very competitive.

2:17:06

intensive. And that is the reason why typically these these companies, they charge you,

2:17:13

they charge you based on the token usage. You know, you're just that tokens use

2:17:16

you have to cost to give up. So, okay, this all we'll back in. Anyways, next class onwards,

2:17:22

prompt engineering have our hair. And I will get a little deeper into what that is. But just remember

2:17:26

the API cost all of you. There's a tremendous amount of cost that you will have to pay if you're not

2:17:31

careful. So, there's a lot of cost so you can't here. You can just keep this at the back of you. You can just keep this at the

2:17:35

back of your mind if you just wanted to mention this specific thing on this API cost.

2:17:42

Okay. And different, you know, language models will have something called context window. This is the

2:17:49

next thing I want to clarify. Context window is what? Context window is what? Context window

2:17:52

means capability and capacity of a language model. It's capacity what is. Now, language model is nothing

2:17:58

but the large language model is the ultimate transformer architect, the ultimate neural network.

2:18:04

Okay, so this is what we discussed all this while, right?

2:18:08

Now, look, our input prompt here.

2:18:11

We have an input prompt.

2:18:13

Okay.

2:18:15

You have an input prompt.

2:18:19

And you're sending that input prompt to a large language model.

2:18:23

And based on that you're getting an output response.

2:18:25

That is what we are doing right now.

2:18:27

Input prompt.

2:18:28

You're sending it to LLM getting a response.

2:18:30

This LLM is basically a neural network.

2:18:32

That is what we discussed.

2:18:33

This is a neural network.

2:18:34

Internally, it's a neural network.

2:18:36

Now, how's how it, what's a different thing.

2:18:38

All that is out of the way.

2:18:40

That's a theory.

2:18:40

Right?

2:18:41

But ultimately, this is a big picture idea.

2:18:43

There can be different, different LLMs.

2:18:45

This is an example of a LLM.

2:18:47

GPT version 4 is an example of an LLM.

2:18:51

Gemini is an example of an by a different company called Google.

2:18:55

If you're an anthropic company in,

2:18:57

anthropic name of a company.

2:18:59

They have a different LLM called cloud.

2:19:02

There are many, many different

2:19:03

LLMs that we haven't.

2:19:04

Again, in the upcoming sessions, we'll get deeper into the names and terminology.

2:19:07

Some, we'll discuss going to about so things.

2:19:10

But different LLMs have different, different, different context windows.

2:19:14

Because ultimately, yeah, what is.

2:19:17

And this is a neural network.

2:19:18

That's what we discussed, right?

2:19:20

So different LLMs have different, different context window.

2:19:23

If you look at the GPT 3.5 model,

2:19:25

which in exactly in December 20,

2:19:30

December 22 is when GPT 3.5 was released.

2:19:33

Okay, this model, this was the base model behind chat GPT.

2:19:38

People who have seen chat GPT's growth.

2:19:41

Chad GPT originally came in December 22.

2:19:44

2002 December 2,0202 December to chat GPT released were and chat GPT that time was based on the GPT 3.5 model.

2:19:50

The maximum number of tokens, the GPT 3.15 model could handle is 4096 tokens.

2:19:57

It's very less actually.

2:19:58

You mean, you can't even more input day.

2:20:01

That's the better model handle not.

2:20:03

and see the progress that happened.

2:20:06

This 3.5 version.

2:20:09

Then GPT4 came.

2:20:11

Then GPT4 Omni came.

2:20:12

Today we have more advanced versions of GPT.

2:20:15

GPT4 straight away 128,000 tokens.

2:20:19

That is,

2:20:19

it's this long input that process can.

2:20:22

Obviously,

2:20:22

pay not free.

2:20:24

This is not free.

2:20:24

It's you have to pay for it, obviously.

2:20:26

But this is the concept.

2:20:28

And Gemini is even better.

2:20:29

Gemini typically is 1 million, 1 million tokens.

2:20:33

So,

2:20:33

Context window is the absolute maximum number of tokens and LLM can process in a single call.

2:20:40

But if you input prompt, when you input day, how much can it process?

2:20:47

That is what is called the context window.

2:20:49

I hope it's absolutely clear to all of you, what context window technically refers to the large language model.

2:20:55

And this is what we already discussed, like, how we are ultimately, it's a very probabilistic model.

2:21:00

Whatever we have been discussing is like a probability based.

2:21:02

a probabilistic model is based on a particular sequence of text you are trying to predict the next word

2:21:08

but then if you're if you're happy type

2:21:09

So it's a happy birthday probably is more likely and I don't know I'm just just going to go and maybe type out in chat GPT for a minute

2:21:19

My birthday is

2:21:24

Next week example my birthday is not next week by the way. I'm just saying my birthday is

2:21:30

tomorrow.

2:21:32

So we're happy to end up.

2:21:34

Now very interesting.

2:21:35

Now, now, you're happy here, so happy

2:21:38

after what will?

2:21:39

If we're going, if we're going to enter this is the contextual thing.

2:21:42

Now, happy can come with any word.

2:21:43

Happy birthday, happy anniversary, happy whatever,

2:21:46

you know, could be.

2:21:48

So the model will assign probabilities for each and every word

2:21:51

and contextually, most likely it might predict happy birthday.

2:21:55

So most likely, so happy birthday.

2:21:57

Happy birthday.

2:21:58

That birthday.

2:21:58

That birthday predict, anniversary predict not yet.

2:22:00

context there. Okay, my birthday is tomorrow. Make sense? So it's a probabilistic model that is going on behind the sense. You can see this. You can see this final action.

2:22:09

Okay, guys, I hope everybody's with you. Everybody's. Now, the final piece that I will do, we have got just

2:22:15

one or two very small, you know, very small demos that I wanted to clarify for all of you.

2:22:20

What is the demo? And this is, this is, this is again, the, you know, the basic, the complete LLM pipeline that I wanted to clarify for you.

2:22:29

whatever we've been discussing on this file, a lot of jargons we have talked about.

2:22:32

I think this diagram very nicely summarizes all this we have seen today.

2:22:36

Here you can see.

2:22:37

We give a raw prompt, raw prompt, one of the text here, to chat, GPTM, I enter, that is the raw prompt we are giving.

2:22:43

And the first part we are tokenizing, tokenizing is the part where we take that entire text,

2:22:48

and we are breaking it into a list of unique tokens, a list of unique words we are breaking into.

2:22:54

Next, we are checking the capacity limit.

2:22:58

What's that?

2:22:59

you know, advanced words, Ali, that's what I'm meaning.

2:23:09

What I'm meaning is, we're using some new technical words use.

2:23:14

There, so many, new terms we used.

2:23:16

So, so we're saying jargon, that's what I'm referring to as jargon.

2:23:19

That's what I'm referring to as jargon.

2:23:21

So, that's how many new terms we use. So, that's how we're going to overall jargon, okay?

2:23:23

Okay.

2:23:26

So this prompt is nothing but the text.

2:23:28

So we're first tokenization

2:23:31

so we are breaking the prompt into words.

2:23:36

Then we're looking at how big the

2:23:39

how many tokens are there.

2:23:42

The whole text is, how many tokens are there?

2:23:46

That we're in context window kept.

2:23:48

The number of tokens in a prompt is called the context window.

2:23:51

Sorry, the number of tokens in a prompt,

2:23:53

we will change.

2:23:53

So it's it within the context window?

2:23:57

I mean, you know, you've made it too million page's input.

2:24:01

Huge, so obviously it can't process.

2:24:04

Next, what is happening?

2:24:05

After the context window check, you're sending it to the transformer model.

2:24:09

This is the neural network.

2:24:11

This is your neural network, lots of hidden layers and all that.

2:24:14

Those basis, the model will calculate probabilities.

2:24:17

All the words of probabilities calculate for them and based on that it will predict the

2:24:20

generated text.

2:24:22

This is an entire operational pipeline.

2:24:23

These are the four aspects that we have discussed so far.

2:24:26

Tokens, every word is a token, could be something else.

2:24:29

Context, what is the context, what is the context, window,

2:24:31

what of the memory, how can remember can't, and the transformer.

2:24:35

Temperature is a last thing, which we're talking.

2:24:37

Here we actually, I'll show this to you, the final thing, I'll show this to you, what is temperature.

2:24:43

Okay, but these are the three main pieces that I want to talk about here.

2:24:46

What these pieces basically are overall.

2:24:49

Okay, all right, now let's, let's see a small demo here.

2:24:53

I have around 10 minutes, 10, max 10 minutes I will take for all of you, okay?

2:24:59

And I'll do a small demo so that people, people can see.

2:25:03

Because today is not a demo session, actually.

2:25:05

Today is more of a conceptual session.

2:25:07

From demo session, next session is totally demo.

2:25:10

We have.

2:25:11

But anyways, we can do a small, simple conceptual thing here.

2:25:16

And what I will do right now is,

2:25:18

I will take you to a platform.

2:25:23

called GROC. So to explain this in a better way.

2:25:28

A GROC we'll. So GROC is very, very good.

2:25:33

So for now, you can just, you know, see what I'm doing.

2:25:37

Then you're back in, you can practice to. Anyways, next class, we'll see your detail in.

2:25:43

But what we have right now, you can see is this. Is this. Right?

2:25:51

We have a user message, which is a prompt. Here we'll prompt clicking.

2:25:55

Just to give an example to you. We'll give a prompt.

2:25:58

Please ignore system.

2:25:59

System is some other thing. We'll back in back. But right now, we will just write a simple prompt.

2:26:04

Okay, we'll write a simple prompt. This is a simple prompt that we'll be writing.

2:26:09

And I will, and let's say I will ask the question.

2:26:14

Okay. I'll ask a simple question.

2:26:17

In terms of

2:26:18

write a one sentence description of the style. I'll give an example. Like this is a very broad

2:26:27

kind of a thing. So you're first first, sir, this is, sir, this is like a GROC

2:26:31

what is like a platform where there are many, many language models out there. Again, I'll

2:26:36

talk more about it later in the next class, but just for now, my objective is just to show a small

2:26:41

demo. Here here, like we can use a GPT model, Gemini model, these are all paid models. You have to

2:26:48

pay money for that. You can't use it. That's what I told you. If you want to use

2:26:53

a large language model, you, you're not use it. But GROC is a free platform. Here

2:27:00

you, you can create a free in free, with some limits obviously. And all these open source

2:27:05

models are available in GROC. Open AI's all paid models are. GPD is a paid model. Gemina is a paid model.

2:27:13

Cloud is a paid model. You can't access it for free. You have to credit card can't add to. But this is a

2:27:18

pre-platform and is good enough for practice, good enough for learning. So you can see some

2:27:22

limits are there obviously. Now, look, here here Lama is a very, very popular model. Lama is a model

2:27:29

by Meta Facebook. Facebook's parent company. This is the one that we'll be using for most of

2:27:33

our class. And you can see we have a limit of 12,000 tokens for manage. Good enough, right? 12,000

2:27:39

tokens is enough free, free. This is more than enough. So we have chosen this particular model,

2:27:46

LLN and we've written this particular prompt. So I hope the story is clear.

2:27:50

I'm a prompt. This prompt will go to this particular language model.

2:27:54

Here here all processing, everything is everything. And output may have some response

2:27:57

to make. That is the thing. Now, here, the interesting part that I want to cover is

2:28:03

we will quickly discuss the concept of temperature. So temperature can basically control

2:28:11

the randomness of the generation. Okay. What do large language?

2:28:16

models basically do. LLMs are looking at some input and based on that they are able to

2:28:23

predict some output. Based on the input, they are processing and they're predicting some output. They're

2:28:27

generating some output. The temperature parameter can be used to control exactly the variability

2:28:34

of your output. The randomness can be controlled using temperature. Temperature. So we can use

2:28:41

the temperature parameter. So I'm here here I will just use the slider.

2:28:46

And I can take it all the way down to the ground.

2:28:48

How many things set can set up.

2:28:51

This is the important thing.

2:28:52

I was discussing.

2:28:53

See, if you don't limit it, your cost can shoot up drastically.

2:28:57

Yeah, grog is free platform.

2:28:58

But you can see, if you

2:28:59

if you're tokens for restrict

2:29:00

not, output, input to our

2:29:02

hand in-input, how long, how big a question I ask,

2:29:05

but output to

2:29:06

restrict it?

2:29:07

Whatever LLM response is there,

2:29:09

that you'll, how you'll respond

2:29:10

can. See, two important things, guys,

2:29:12

okay.

2:29:12

The input-input, we're right now this is actually called a prompt.

2:29:16

And whatever response we end up getting,

2:29:19

that is called a completion.

2:29:20

Input is nothing but a prompt.

2:29:22

That is the other word we are using.

2:29:23

And the response or the output is called a completion,

2:29:26

completion tokens.

2:29:27

So this is how we can control the number of response

2:29:29

or completion coquence.

2:29:30

You can directly control,

2:29:32

you can talk to the large language model,

2:29:34

and you can restrict,

2:29:35

that we're 2024 to go.

2:29:37

That's then then after not going.

2:29:38

So you're restricted to limit,

2:29:39

your cost.

2:29:41

So, as I'm a temperance is zeroed,

2:29:43

very interesting.

2:29:44

You can see,

2:29:45

when I run this,

2:29:46

multiple times.

2:29:48

When I run this multiple times,

2:29:50

if you're doing it, if you run

2:29:52

run, now,

2:29:53

now, now look,

2:29:53

this statement is the sky is a vast

2:29:56

ever-changing canvas of colors and texture.

2:29:58

You can't,

2:29:58

you know,

2:29:58

you go,

2:30:00

you can it is exactly the same.

2:30:03

Can you see?

2:30:03

This is what I wanted to clarify.

2:30:05

When you say temperature is zero,

2:30:08

model probabilistic

2:30:09

is sorted.

2:30:09

We all agree the model is probabilistic.

2:30:12

But you can already

2:30:13

already see,

2:30:15

the tooltip is

2:30:16

coming out, controls randomness

2:30:18

of the generation.

2:30:20

Because this is a completely

2:30:22

probabilistic process.

2:30:23

I discussed already.

2:30:24

When you enter a prompt,

2:30:25

when you enter an input,

2:30:27

the model is trying to predict

2:30:28

the probability of the next word,

2:30:30

next word, next word, next world.

2:30:32

That's poor a sequence in a probability

2:30:33

may generate.

2:30:36

Temperature just as zero

2:30:37

to, you,

2:30:38

you're probably control to.

2:30:39

This can't the mathematics

2:30:40

which we are not getting into,

2:30:42

but when you reduce the temperature to zero,

2:30:44

you are literally controlling that probability.

2:30:46

Right? So, so when you make the temperature zero,

2:30:49

the response will stay fixed on the time.

2:30:52

You can give it a read,

2:30:53

grays of cloudy days, whatever.

2:30:55

And then again, it will be exactly the same.

2:30:58

We'll pull no further.

2:31:00

Exactly the same.

2:31:00

We'll just run it.

2:31:02

Every time you run this, submit car,

2:31:04

what is what is going?

2:31:05

This input is getting fast to the LLM.

2:31:08

Temperature setting is zero and the response is getting fast back.

2:31:11

Submit do it.

2:31:13

So today's class, I'm keeping it basic.

2:31:16

The other class, when we'll actually show you the code.

2:31:19

We'll this code in Python.

2:31:21

So, there's nothing in the code.

2:31:25

This is very easy stuff.

2:31:27

We'll write in Python when we come back on Thursday.

2:31:29

Okay?

2:31:29

Chat completions create,

2:31:31

groc use.

2:31:32

We'll Python may directly

2:31:33

copy-pace.

2:31:34

So whatever we are able to do

2:31:38

in this UI right now, in this dashboard,

2:31:41

we'll just we're in Python going forward.

2:31:43

So this is the intuition of temperature.

2:31:45

If you make,

2:31:46

temperature zero, there is no variability.

2:31:48

And if you make temperature equal to two,

2:31:51

if you're when temperature to

2:31:51

you, when you're very ability will increase.

2:31:55

Now see this one, all of you,

2:31:56

the sky is a vast ever changing, whatever.

2:31:58

When you're increased

2:31:59

see what will happen.

2:32:01

Look at this.

2:32:02

This will be something different.

2:32:03

Here here here.

2:32:04

Callidoscope came.

2:32:05

Look, this was not.

2:32:06

It was not.

2:32:07

Now, you again, you again.

2:32:08

Again, you again.

2:32:09

Some other will come.

2:32:11

Some other.

2:32:12

There are.

2:32:12

A bit kaleidoscope not.

2:32:13

Look, the mesperating palette of colors.

2:32:14

There are.

2:32:16

I hope everyone's aligned.

2:32:18

Everyone's with me.

2:32:18

So the more you increase the temperature,

2:32:20

the more you increase the temperature,

2:32:23

you can see it's a completely different sentence again.

2:32:26

Number of words be increased over.

2:32:27

I hope everyone's aligned on this.

2:32:29

So this is basically what temperature is used to control.

2:32:33

Now, look, here here here some more came.

2:32:34

Clouds, sun, moon, starts.

2:32:36

Now, the general thing is that temperature

2:32:38

from variability can change.

2:32:41

Yeah.

2:32:43

All right.

2:32:46

So, guys, any questions, any questions, anybody?

2:32:50

Any questions that you want to ask me at this point in time?

2:32:54

Any doubts, any questions that you want to ask me.

2:32:56

I want to keep some time aside for doubt clearing.

2:32:58

One more term is called hallucination.

2:33:00

Hallucination term, we'll be in detail in discuss.

2:33:03

But just at a very high level.

2:33:05

Uh-huh.

2:33:05

Yeah, so you're not.

2:33:06

Temperature is basically nothing, but it is used to control the variability of the generation.

2:33:11

Now, you can, I'm hovering my cursor on the thing.

2:33:14

Now see, Sartio.

2:33:16

It controls the randomness of the output.

2:33:19

So temperature basically controls what is the randomness of the output.

2:33:22

How random the output basically is.

2:33:24

That is what temperature is.

2:33:26

Temperature controls the randomness of the output.

2:33:29

Okay?

2:33:30

If you're a temperature zeroed, response,

2:33:32

that's not random.

2:33:33

So you're okay?

2:33:34

This is what I explained to you.

2:33:36

If you want me, I can you again see, I can't see.

2:33:38

Temperature we have zeroed.

2:33:40

We're the same thing.

2:33:41

You write the prompt.

2:33:43

You hit, submit.

2:33:44

This entire input gets sent to the LLA.

2:33:46

And the response gets sent back.

2:33:48

When your temperature is zero, you will get the same response all the time.

2:33:52

Yeah, exactly, Anjou.

2:33:53

That is what you are.

2:33:54

Now, look, brilliant, whites of gray, cloudy sky.

2:33:57

You know?

2:33:57

When you get temperature zero, your response will always be the same.

2:34:02

Always be the same.

2:34:04

Always be the same.

2:34:05

Okay?

2:34:05

Think of it that way.

2:34:07

Okay?

2:34:08

Yeah, you have, like a seed value.

2:34:12

You can remember it that way.

2:34:13

It's like a seed value.

2:34:14

Because if you set it, that way, it's like a seed value.

2:34:14

Because if you set it, that same.

2:34:16

to same right.

2:34:17

So we'll, so we're in detail in detail.

2:34:19

GROC, I just wanted to be, I just wanted you to show at a very basic level.

2:34:23

But, yeah, we'll see GROC all through the force, don't worry.

2:34:28

I will teach you in detail, API keys, how set.

2:34:31

Today, I just wanted to show you.

2:34:33

Just, you know, share the GROC link.

2:34:37

I'm just sharing it with you, Ankeh, but, yeah, but you

2:34:41

setting.

2:34:42

I'll discuss this with you in the next class.

2:34:45

what's going to do because you might get confused if you try to see it by yourself.

2:34:49

But anyways, I'm being delayed to you.

2:34:51

Sure.

2:34:52

And there is one last term that I wanted to use called hallucination.

2:34:59

Or hallucination is again a very, you know, very interesting topic actually.

2:35:06

So, hallucination a term used.

2:35:10

Which is like, anybody knows what is hallucination?

2:35:14

Let me hear from.

2:35:15

the audience. Who knows what is hallucination?

2:35:17

Okay, Rajdip has a question.

2:35:19

Sir, if interlink the prompt to English and Hindi both in the same time.

2:35:21

You can do that. Absolutely.

2:35:23

If the model is capable of understanding both the tokens together,

2:35:27

absolutely you can.

2:35:29

Absolutely you can.

2:35:31

If the model is inherently capable of understanding those tokens.

2:35:35

So Rajdip, everything boils down to tokenization.

2:35:37

Now here in India in, we have an India-specific LLM, right?

2:35:42

We have an India-specific LLM called

2:35:44

called this what you call Servum AI, right?

2:35:48

So Servum AI is able to understand natively.

2:35:52

If you see Servum AI, they also have language models.

2:35:55

But their language models is specific to India.

2:35:59

So they will understand the India tokens very well.

2:36:02

Right? Make sense.

2:36:05

So everything boils down to tokens.

2:36:08

Whatever you are typing, whatever you are talking,

2:36:10

everything is ultimately broken down into unique words and converted to tokens.

2:36:13

and converted to tokens.

2:36:15

Even if you say something in Hindi,

2:36:17

I know, so I don't know if this will work perfectly.

2:36:20

Start speaking.

2:36:22

You know, you see what's the cart recovery.

2:36:27

So try.

2:36:28

We can actually updates are good.

2:36:30

They're very interesting.

2:36:32

I think the problem is that my

2:36:36

like I think

2:36:38

give permission

2:36:41

while visiting the site.

2:36:42

But yeah.

2:36:43

this is very interesting. You can try out the surrogles.

2:36:45

I'm going to say.

2:36:47

Yeah.

2:36:48

Absolutely.

2:36:49

Yeah.

2:36:50

What is.

2:36:51

What is?

2:36:52

What are?

2:36:53

Can you see, guys?

2:36:56

It's not.

2:36:57

I can you see, guys?

2:36:58

He's not in what I'm what I'm going.

2:37:01

You're about to hear me, right?

2:37:04

Here, right?

2:37:05

It's pausing also.

2:37:07

It's pausing also as I'm talking.

2:37:08

Can you see?

2:37:10

You're able to hear?

2:37:12

Are you able to hear?

2:37:14

Do you?

2:37:15

Don't I did it?

2:37:16

Yes.

2:37:17

I didn't hear you clearly now.

2:37:18

My apologies for the confusion earlier.

2:37:20

I was asking if you'd be interested in hearing about the special limited time deal

2:37:24

or the eye making left in your...

2:37:26

No, no, no, no, no, no, I'm not interested in any of that nonsense.

2:37:29

I have to get back to my class, thank you.

2:37:32

I understand if you're busy, but this is a really great...

2:37:37

You see what happened there?

2:37:39

I just wanted to open this up and show you.

2:37:41

up and show you. Everything burns down to tokens, you know?

2:37:43

ServerMaya is amazing. I think you guys can go to the site.

2:37:46

So basically, I was, you know, I was talking in Hindi. I was talking in English.

2:37:51

And server may I understand 22 languages?

2:37:54

This is the model. This is the one that was a big thing in our India

2:38:00

AI summit that happened this year, no?

2:38:04

This is our homegrown company.

2:38:06

Very nice, very nice actually. You can look it. See, everything is tokens.

2:38:10

is tokens. Whatever you have, everything is getting converted to tokens.

2:38:14

You.

2:38:15

You're in English in.

2:38:16

Hindi in it.

2:38:17

Do you do it.

2:38:18

And this is very nice.

2:38:19

Okay.

2:38:20

Great.

2:38:21

Chalo, guys.

2:38:23

Thank you.

2:38:24

That will be all.

2:38:26

Any other questions?

2:38:27

Maybe just a minute more.

2:38:28

Before I pass it over to Arshita for the for the Menti meter.

2:38:33

Any other question?

2:38:34

I'm sorry.

2:38:35

Ayshwarya had a couple of questions.

2:38:36

Sorry.

2:38:37

It means that when

2:38:39

Yeah, yeah, exactly, exactly.

2:38:42

I'll take it up in the next class, but hallucination exactly.

2:38:45

What you're saying is correct.

2:38:47

Oftentimes what happens is, see, because all these models are probabilistic, right?

2:38:50

All these models are probabilistic.

2:38:52

Everything you're trying to create in a probabilistic way.

2:38:56

And because you're trying to create everything in a probabilistic way,

2:39:00

what happens, oftentimes when you ask a question,

2:39:04

the language model oftentimes generates a fictitious answer.

2:39:08

And we have seen a lot of use cases, particularly in legal domain and a lot of police investigations and lawyers and judges.

2:39:17

So when they were using these kinds of large language models, right?

2:39:21

They were facing a lot of problems.

2:39:23

So, mania, what lawyer's what is?

2:39:25

Lawyer, when he's a case arguing, he'll look up, that here,

2:39:28

yeah, man, 1950s in what are going to.

2:39:30

And let's say you will go and ask Chad GPD, what happened in 1956.

2:39:34

And Chad GPT said that in 1956 in 1956,

2:39:37

A has B murder, but it might so happen that A was not even born that time.

2:39:42

So, what murder can do?

2:39:43

So I'm just saying that there are a lot of such cases where Chad GPT will give you and these language

2:39:48

models will give you wrong information.

2:39:50

They will hallucinate and they will, right, right, and they will basically generate a wrong answer.

2:40:01

Okay, so I'm very confidently they will give a wrong answer and that is effectively what

2:40:05

hallucination reference to.

2:40:06

And you have seen a lot.

2:40:07

lot of cases. It's very scary at times, you know. It's very scary at times. Like you,

2:40:12

I think there was this, there was this particular, especially, I would say, a lot of these,

2:40:19

lot of these personalities are at least, politicians and movie actresses and all. I was reading about

2:40:24

this post. I forgot, this was a US senator, I think. Yeah, US senator or US congressman's a

2:40:30

story. And this person said that when people were asking about her on chat, GPT,

2:40:37

or some other language model. It was giving all sorts of rubbish stuff about her.

2:40:41

It was hallucinating. When you are asking a question in a certain way, the model was generating a wrong answer.

2:40:49

I mean, you can ask a question about some person. Okay. What do you think of science? I mean, now it doesn't know me,

2:40:54

obviously, because I'm not that famous. But if you ask it about a different famous personality,

2:41:00

maybe what do you say about this person, a, chat GPT can sometimes manufacture an answer. And that is what is called hallucination.

2:41:05

It's a long topic. We will see that later, but just wanted to share with you the core idea

2:41:10

based on the question. But we will see that. Great. It means when we are getting random output,

2:41:18

when LLM doesn't know correct answer, exactly, exactly. Ashwari has already answered. Correct. Very nice.

2:41:24

Yeah. Very good. Exactly. We'll see. We'll see that in more detail later. Correct.

2:41:30

Sure. Great. I think we are just in the session closing time now, 1030.

2:41:35

any other questions. So people can also take some time to fill up the polls, please. And I'm here for some

2:41:41

questions in the meantime. You can, you can please ask me whatever you want to ask. And I'm,

2:41:46

I'm happy to take up some questions. Next session will be totally hands on. I will talk about the

2:41:52

groc setup, suppose they can get, but this was very important. The context is very important,

2:41:58

especially for interviews and all if you go, people will ask you. Like, so this context is very, very important.

2:42:05

whatever we discussed today. So to the overall theoretical ideas that we learned today,

2:42:10

very, very important. So I would really like all of you to maybe recap it once. Okay. Yeah.

2:42:16

So any questions? Any more questions you have?

2:42:32

So Prontme, most of the spellings are wrong?

2:42:35

So, absolutely. Absolutely. And that will also work out very nice. You know, exactly. Very good

2:42:40

question, even if that happens. So Ankeith has a question. I think others are not able to see.

2:42:44

Anke's question is, prompt in most of the spellings wrong. If you have a prompt

2:42:47

and prompt is not exactly correct. They know, they're not exactly not. Oftentimes, uh, uh,

2:42:53

that will pick up. Absolutely. It will correct. It has an auto correction capability also. It will correct

2:42:58

the prompts as well. Yes. And this is all the magic of transformers. Everything is the magic of transformers

2:43:04

something like the transformers joe. Yeah. Movie name is mercy. Oh, I didn't

2:43:11

hear about that. What is that Rajee? Is that a, is that a movie on LLMs or what is it? I've not,

2:43:16

I've not, I've not heard about it. What is that exactly?

2:43:28

Or maybe it's the kind of a kind of a judge that is using a large language model probably, huh?

2:43:34

Okay. Okay. Okay. Yeah. And it's actually a very interesting case, you know, since we are talking about legal domain, I wanted to give you a real use case today. There's actually a company called Harvey. U.S. Met is a company called Harvey. It's a very, very popular large language model. You know, this is the company called Harvey. Very, very popular in this space. And they are actually doing this. You can imagine how important, you know, how important this process is. It is very important for you to

2:44:04

to get it right. You cannot just, you cannot just hallucinate, you cannot go wrong.

2:44:08

Now, you're not the wrong. Yes, we agree that based on some input, you're trying to predict the next

2:44:13

word, the next word, but you cannot afford to go wrong. That is what I want to clarify.

2:44:18

Yes, these are real use cases. These are actually getting used in U.S. courts. Indian courts may

2:44:22

legally allow not yet. There are a lot of other Supreme Court guidelines and all. So Indian ports where

2:44:27

technology used like this is not, like there are a lot of legalities there. But in U.S. courts, European courts,

2:44:33

this is actually getting used. A lot of AI is getting used. And also if you think of it as a national

2:44:38

good, good can it be a try, no? So many pending cases are there up there in the country. So if you're

2:44:43

able to use AI and if you're able to fast track many of the days, it's good for the nation also,

2:44:49

right? That way. Yeah. So this is also a very nice use case I wanted to kind of mention to all of you.

2:45:03

Any other questions, guys?

2:45:33

Okay.

2:45:37

Hello, thank you then, guys. If there are no other questions, great. Thank you, all of you. And again,

2:45:43

my, you know, my request to all of you would be, you know, per humble, humble request, please,

2:45:48

all of you join on time from next class. I really, I want to try my best to make sure we close

2:45:54

the classes on time as well. Five, ten minutes here and there is okay. But that's why we are

2:45:59

really looking to stick to the timings. Everybody, please join on time.

2:46:03

Shar, eight o'clock, we will start the classes, right?

2:46:05

So, okay, but I think 801802 is fine, but everybody please be on time, okay?

2:46:10

So today also, I don't like to start early because everybody, because new topic

2:46:15

then, so if we'll start out and that also I don't like, I want everybody to follow the classes

2:46:21

nicely. That's my personal thing. But also the thing is that, you know, the team keeps telling

2:46:25

me to some of you get very late in the classes also, I think. So just try to come early.

2:46:31

We'll start the class early. We'll start the class early.

2:46:33

So if we start the class early, you know, we can end it early on. So we can stick to the

2:46:37

timings. And obviously, if required, we can always extend, we can have an extra class. Those things

2:46:42

are there. But at least the timings, let's start on time. That's my humble request to you.

2:46:47

Jolo, thank you everybody. Next session will be on, on prompt engineering. And we will be

2:46:55

doing that in the next class. Thank you. Thank you. Thank you, everybody. So thank you,