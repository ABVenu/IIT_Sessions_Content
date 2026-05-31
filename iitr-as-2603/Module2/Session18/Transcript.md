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

Hi, Koppel, I'm Ame Audible.

6:20

Yes, you're audible.

6:23

Yeah, so Koper, I just wanted to let you know that if you can give me one or two minutes, I'll just let the students know.

6:32

Or I don't think so it is necessary because this is an IM session.

6:38

Yeah, it's okay.

6:39

You can carry on.

6:41

I'll not do any announcement.

6:43

Thank you.

6:44

Thanks.

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

Thank you.

9:50

Thank you.

10:20

Thank you.

10:50

Thank you.

11:20

Thank you.

11:50

Thank you.

12:20

Thank you

12:50

Thank you

13:20

Thank you

13:50

Thank you

14:20

Thank you

14:50

Thank you

15:20

Thank you

15:50

Thank you

16:20

Thank you

16:50

Thank you

17:20

Thank you

17:50

Thank you

23:50

Good evening,

23:54

Good evening, everybody,

23:57

Hi, all of all of you,

23:58

Hi, all of you,

23:59

Welcome to the session.

24:20

Just just

24:30

Just start in a minute.

24:32

Just start in a minute.

24:50

Thank you.

25:20

Thank you.

25:22

Thank you

25:25

Thank you

25:29

Thank you

25:33

Thank

25:36

You

25:37

Thank you.

25:39

Thank you.

25:41

Thank you.

26:11

Thank you.

26:41

Thank you.

27:11

Thank you.

27:41

Thank you.

28:11

Thank you.

28:41

All right, guys, so let's start on here.

28:45

And today's session is on, is pretty much a continuation from where we, you know, where we ended last session.

28:52

So last session we talked about regression and at this point in time, I think all of us, we are fairly comfortable with the overall workflow of machine learning.

29:03

So we all understand what is machine learning, how to take our data set, how to split our data into training data, testing data.

29:11

So we all understand those pieces very well right now.

29:14

And so last session was more about ridge regression, lasso regression.

29:19

We discussed about something called regularization.

29:22

But if the model becomes very overfit, then we regularize to reduce the power.

29:26

So we understood the idea of overfit model, underfit model, good fit model.

29:29

These are all the things we have discussed already.

29:32

And at this point in time, we are fairly comfortable in how to build a model.

29:36

We understand how to take our data, how to build a model and also how to evaluate a model.

29:40

So we have seen these things.

29:41

Now, all this while we have discussed these, you know, these things in the context of,

29:46

you know, what we refer to as a regression problem. In today's session, we are going to be

29:51

specifically discussing about classification. So this is the broad agenda of the session we will

29:56

do today. So we'll see how is classification different from regression. So what is classification

30:01

exactly? I think this goes back to our very first class if you remember. So we've already talked

30:05

quite a bit about regression versus classification. I will start the session by again quickly summarizing

30:11

the difference. Then we will specifically talk about what is logistic regression,

30:15

a very, very popular classification algorithm. Which is, like regression in, I started my

30:21

conversation with linear regression. So the equivalent of that in classification is called logistic

30:25

regression. So we will just discuss the very basic intuition of what it is. We will not get to the math

30:30

at all, but it is a very basic intuition that we will be discussing. That's why the term intuition is used

30:35

not the method on. We now get into the mathematics predictions. How do we build a model? How do we

30:40

do predictions. And you'll be surprised to see. That's why I say today's session I think

30:46

is comparatively a lot lighter, a lot easier, because all the bases are covered. Now we are trying

30:51

to learn a new topic. That's it. Like in whatever base we have discussed in machine learning,

30:55

that remains the same. So we all know how to take a data, how to, you know, how to go back and

31:00

split the data into training data, testing data. So we have seen those pieces already. So all that we

31:08

we are trying to do right now is we are talking about the, you know, the classification part

31:12

right now. That's the only thing that we are trying to do right now. So just the classification part

31:16

we are trying to talk about here. Okay, so we'll see decision threshold and we will also see how

31:20

to evaluate models. Same thing. The code will be absolutely the same. In fact, if you want me to just

31:26

do a rundown of the notebook, I can just take a quick 10 seconds to show you the syntax a little bit.

31:33

This actually our case study is last way. Now, look, syntax is exactly same to same.

31:38

There's no. Classification models.

31:41

That's for the way we are using SK learned. Like the regression algorithms we are using SK learn.

31:45

Classification also uses SK learned and you'll be surprised to see the code will be exactly the same.

31:49

Nothing changes. Only the conceptually there be some changes. We'll focus heavily on the concepts a little bit.

31:54

But then the code part is very similar.

31:56

Now, look, pipeline, min-max scalar, algorithm, there, dot fit, dot score, white rain accuracy,

32:01

white test accuracy. Same story. Nothing changes, actually. Some new intuitions will be seeing along the way.

32:08

So just to kind of summarize the discussion points for today, what we'll be covering.

32:12

So now with this, let's start on. Let's start on and let's get a little, let's understand what is classification.

32:18

What exactly do we mean by classification? And what is it? What is classification? How is it different from regression?

32:26

So most importantly, if you all remember, we have discussed this in our, in our very first session.

32:32

In regression, we are always trying to predict a continuous output.

32:36

What are we trying to do in regression?

32:38

The output that we are trying to predict is always a number.

32:41

We are always trying to predict a numerical output in regression.

32:44

The output is always a number.

32:46

That is what we are doing in regression.

32:47

So if you go back to the exercises we did last to last day, Monday, we were able to predict the housing price, California housing price, Kiar.

32:57

So we were able to predict the marks secured by students.

33:00

So in all these cases, the output was always numeric in nature.

33:04

So based on the features, we are trying to predict some kind of a numerical output.

33:08

So regression is more like where the output is a number.

33:11

Like what is the exact price of the housing rupees?

33:14

And there we discussed about R squared, R MAC, M-A-E, these kind of metrics we actually talked about.

33:19

This is what we discussed in regression.

33:21

Now, here me outfinsch.

33:24

Intuitively, how many regression how studied here.

33:27

Intuitively, regression was more like what is the line or plane or surface that best fits the points?

33:33

If you remember the conversation of regression that we did, so we have, we have, you know,

33:38

know, we are having a lot of data points.

33:39

You have your x-axis, or y-axis, hey, so we have to study here.

33:43

You've got x-axis, you've got x here, you've got y-here, you've got y-here, and all that you're trying

33:48

to do, you're trying to find out that there can be infinite number of lines that you can draw

33:54

in this two-dimensional mathematical space, right?

33:57

So in this two-dimensional mathematical space, you can draw infinite number of lines.

34:01

So out of all the infinite number of lines, we are trying to find out, we are trying to find out

34:05

what is the line or plane or surface.

34:08

that best fits the point. So the best fit is what we are trying to find out in a way.

34:13

So out of all the infinite number of lines that we can draw, what is that line that best

34:17

fits the points? This is our linear regression, what we discussed. So that is the idea of

34:21

regression that we already covered. Why am I talking about it? Because classification is more about

34:27

separation. I'm that intuitively simplification. What is the theoretical definition of classification?

34:33

Something we already done before. Theoretical definition is, you are trying to predict

34:38

something that is not a number.

34:40

Like you're looking at the features of a person and you're trying to predict whether the person will

34:45

have a disease yes or no. The output column is the output column is not a number. The output column is a category.

34:52

So is it yes? Is it no? Okay. So a credit card fraud detection is another great use case.

34:57

You are looking at the different features of a person. Let's like the transactions.

35:01

The person is doing different types of transactions and based on the different features of the person,

35:07

you are trying to predict whether the transaction is a fraud or not.

35:11

So fraud a column will you have to predict is that fraud column going to give you yes value?

35:19

Excuse me.

35:21

If you can see why.

35:27

Or is the fraud column going to give you no value?

35:30

Just like you your credit card. You go and swipe the card and real time the fraud detection is happening.

35:36

So based on the amount of the transaction, based on the time of the transaction, the merchant name, the model is trying to predict, is it a fraud? Is it not a fraud? That is what we are trying to do in fraud reduction. So the output, the output will be either yes or no. So that's the way how we can understand what we are trying to do in classification. So that is the intuitive understanding, I mean, the theoretical understanding. Conceptually, what is what is really going on in classification? What are we actually doing? So as I

36:06

say, regression is more about how much? Whereas in classification, it is more about which category.

36:12

So if I relate this to Maasai school use case, we've got a lot of student data, right, historical student data.

36:18

As I told you in the prior sessions, we were having these examples. So we are looking at the different

36:23

characteristics of the students, right? So what is their attendance, how much are they, how much marks are they scoring in the class and all that? How attentive are they? How engaged are they?

36:31

So based on all these factors, we are trying to predict how much marks is.

36:36

will get? Go hoagia regression problem. What could be a similar classification problem?

36:41

Where we are trying to predict whether you will pass or fail. So based on the features of the student,

36:46

based on your location, based on the amount of time you're spending on this, based on all these factors,

36:52

we are trying to predict, will you pass, will you fail? That is what you are trying to estimate.

36:56

You're trying to estimate, will you pass, will you fail? So pass or fail is the output that you're

37:01

time to predict. That is how we can look at a classification problem.

37:06

What could be some other examples of classification?

37:08

These are some other very nice examples of classification.

37:10

You can relate to it.

37:10

We have seen these in our first session.

37:13

Just that's banking may probably in a transaction we talked about.

37:15

Email, spam classification.

37:17

It's a very, very good use case.

37:19

So whatever mailboxes we are having today, based on the different attributes of the email,

37:24

we can predict whether the mail is a spam or the mail is not a spam.

37:28

You see, your mailboxes, use to take junk mail option are that, right?

37:31

All of you, all of you know, all of you have seen the junk mail option in Outlook and Gmail.

37:35

And you know what they are doing?

37:36

They're all using spam classification behind the scenes.

37:39

So email data maybe, the inboxes, they're all by default using something called spam classification.

37:46

They're by default using something called spam classification.

37:49

All if you can take on the table.

37:50

This is the sample one that I'm trying to show you right now.

37:53

Now, I've opened up my outlook in my system, and you can take a look at it.

37:58

This is like junk mail.

37:59

So you might be wondering, who is putting these mails in the junk mail folder?

38:03

You think I am going there and manually moving it?

38:05

No.

38:05

There's a machine learning model that is built in Outlook.

38:09

Microsoft has been made already.

38:11

The model is built into Outlook and the model is able to look at the emails that I'm receiving.

38:17

Every single email I'm receiving.

38:19

And it is classifying that key, is it?

38:21

So based on the features of the email, based on all those words and everything,

38:26

subject, word, what kind of content is there, it is driven to predict that, hey, is it a spam mail?

38:31

Is it a ham mail?

38:33

Spam will go to the junk folder.

38:35

Ham, H-A-M, hand, we'll go to the inbox.

38:38

So this is what is going on behind the scenes.

38:40

I hope everybody is aligned.

38:42

Another great use case that we are seeing getting used nowadays is employee resignation prediction.

38:48

Okay, so you're looking at the different characteristics of the employee,

38:52

and you're trying to predict will the employee pass or will the employee resign or not resign?

38:57

Okay, so can we estimate in advance whether a person will lead the job or not?

39:03

This could also be a very nice.

39:05

application we can look at. So based on the features of the person can be

39:08

estimate whether the person will leave the job or not, will the person resign or not,

39:13

yes or no. So the output that you are trying to predict will be either yes or no. So that is

39:19

another use case of classification we can look at. And finally, will the student pass or feel?

39:23

as you can see in all these cases, the output is not a number, it's a category. So this is how we

39:27

understand the intuition behind the classification problem. Okay. Now, what we are going to see right

39:33

now overall here is a specific type of classification which is called logistic regression.

39:42

So before I get to that, I'm going to go back and set a little bit of intuitive context

39:50

behind what classification really is. Just like we discussed about regression, best fit line.

39:56

Same way, let me give you another another way to think of a classification problem.

40:03

let us see that. So what I'll do, I'll take you back to this diagram, which I've already

40:08

created for you. Before I explain this to you, everybody just dedicate 30 seconds to just go through

40:17

it once. Yes, even if you don't understand anything, it's okay. Just just wanted everybody to just give it a

40:22

glance right now. Just give it a glance all of you.

40:33

Thank you.

41:03

everybody give it a glance please. And I'll just all of you take a glance please. I'll explain. And just to, yeah, so all of you take a minute. I'll explain.

41:33

Thank you.

42:03

Thank you.

42:33

Thank you.

43:03

So, guys, what we are looking at what we are looking at the, we are looking at the, we are looking at the, we are looking at the right now, we are, we are looking at the, uh, just to give you a little bit of context what we are, you know, what we are talking about here. We are looking at the

43:31

a typical self-driving car use case. So not quite literally, I mean, self-driving car

43:40

will be more advanced, but you can think of it like a self-driving car use case. So that is,

43:45

that is the intuition behind what we are seeing right now. Okay, so based on the features of the road

43:54

conditions. So based on the different, different features of the road conditions, we are trying to predict

44:01

what is the speed of the car going to be?

44:05

Now, look, this is the table is left-hand side in. This is where you will understand the story,

44:09

the big picture story. Steepness means how steep the road is.

44:15

Like, let's say if you're in a mountain road, the mountain road will typically be very steep, right?

44:21

So steepness is that, how steep is the road? And bumpiness means that how bumpy is the road?

44:28

Take it straightforward. We've got steepness and bumpiness. Steepness means. Steepness means how steepness means how steepness?

44:31

is the road and bumpiness means how bumpy is the road. And based on that, you are trying to

44:36

predict what is the speed of the car. So based on the steepness and the bumpiness of the road

44:43

conditions, we are trying to estimate what is the speed of the car. This is our problem. This is what we

44:50

are trying to solve. Okay. Now, look, speed, either slow or fast will. Everyone can see this.

44:56

So until here we are sorted. So the other story we know. This is our data is. This is your data,

45:00

X, Y combinations. You can use an algorithm. You will be able to build a model. Then this we understand

45:06

already. What I'm trying to do is I'm trying to give you the visual understanding of what is

45:12

classification. Visually, you how you can't look at this. Visually you have asked us to look at this one on

45:18

on the x-axis. X-axis in our steepness plot. So let's say steepness is the value within zero to one.

45:25

Zero, what's the beautiful steepness. One is one matter. One is very steep road. And bumpiness is the value

45:30

between zero and one. If zero is, then it's a good smooth road. And if one

45:34

there, then very bumpy road is. So whenever the road is

45:39

neither steep nor bumpy, if the steepness of value

45:42

be come and bumpiness the value be come. If you look at this area, all greens,

45:46

what the car is going fast. So if I plot this data, every single

45:51

row in the table is a dot in a scatter plot. And we are

45:55

coloring by the speed. So you're wondering, you're wondering, sir,

45:58

this color how are. So we are basically color.

46:00

by the speed. If you plot this data, you'll

46:04

you'll see that these all points here, this will all be like fast.

46:10

All the greens will come here. So when the steepness and bumpiness,

46:13

both are low, the car is going very fast. When the steepness and bumpiness

46:18

both are high, but the road is very steep and very bumpy or

46:21

either road both are very steep or the road both bumpy either the road is very steep or

46:27

the road is very bumpy, then also the car is going fast.

46:30

sorry, going slow.

46:32

Reds here.

46:34

So we just data drawed here. So what we are trying to do in classification is

46:40

we are trying to find out what is the line

46:43

that best separates the classes.

46:45

This is your red, this is your green.

46:48

You're going to say, sir, this points where from?

46:49

This points our data.

46:52

Machine learning, what are we trying to do in machine learning, guys.

46:55

We have lots and lots of X, Y combinations.

47:00

Input-output combinations you have.

47:02

Input, output is.

47:03

Input is steepness, bumpiness.

47:05

Output is speed.

47:06

Speed, meant to color.

47:07

So you have this data already, the greens and reds already have.

47:10

We've just put it to coordinate axis in plot to you.

47:13

You know, to give us, to show and to show me, to make sure the issue.

47:17

Now coming to the story, that classification, ma'am,

47:21

we're doing.

47:22

When we use an algorithm and when we build a model,

47:24

that model is what model is nothing but this kind of a line.

47:30

This is what you are trying to do in classification.

47:33

Now, you know, as we discussed about that regression exercise last week,

47:38

Y equal to MX plus C,

47:41

X axis, Y axis, coordinate axis, there are infinite number of lines you can drop,

47:45

line as it can be, like, how can't, it's like,

47:47

you can't, if you can go back, you can't,

47:49

there can be infinite number of lines you can drop.

47:52

See, I'm rotating the scale right now.

47:54

And what you are trying to do, out of all the infinite number of lines you can drop,

47:58

you are trying to find out what is that line.

48:00

that best separates the classes.

48:03

So, just you,

48:03

like you've made ruler here up,

48:05

turns out that this is the one that best separates the classes.

48:08

You can't here.

48:09

Here, this is, it's not right.

48:11

Herepah, here can't.

48:12

This, this is right?

48:13

This can't be.

48:15

This be right.

48:16

Because then you're not separating reds and greens

48:17

correctly.

48:18

Turns out that this is the best separation between the classes.

48:22

Okay?

48:22

And turns out, this is what is referred to as a decision boundary

48:25

or a decision surface.

48:28

This is what we are intuitively

48:29

trying to do in classifications.

48:32

The classification is about separating the classes.

48:35

You have herepah,

48:36

it's it there.

48:37

You have two classes.

48:40

Output, there are two classes.

48:42

Slow is a class.

48:43

Fast is a class.

48:45

Green one class is, red egg class.

48:47

All that you're trying to do

48:48

is you're trying to separate the two classes.

48:51

This we are trying to do in classification.

48:53

And this is the difference between regression and classification conceptually.

48:58

One definition we discussed on the first.

48:59

day of machine learning, that regression, numeric output and classification categorical output

49:04

that story is sorted.

49:06

Those story, everyone knows.

49:07

Now, this is the intuitive understanding.

49:09

Regression in, we are trying to find the best fit line.

49:12

We're trying to find the line that best fits the points.

49:15

What is the best fit?

49:16

Regression is all about trying to find the best fit, whereas classification is always about

49:20

trying to find the best separation.

49:21

You've got reds here, you've got greens here, and we are trying to find what is the line or plain

49:25

or surface that best separates the two classes.

49:28

That is what we are trying to do in classification.

49:29

So, regression is more about, you know, finding out what is the best fit line?

49:36

What is the line or surface that best pitch the points?

49:39

That is what we are doing in regression.

49:40

Whereas in classification, we are trying to find what is the line or plane or surface that best

49:45

separates the classes.

49:46

And that's your final end result, the model here.

49:49

This is a equation, this is a equation, it's just like we discussed the story in regression.

49:55

Here here, the classification will be the same kind of equation you'll be having.

49:58

But we will not get to the mathematical.

49:59

smart at all right now. But just to give you the intuition, so data, algorithm,

50:04

when we'll build a model, which will have an equation and that is also called a decision

50:11

boundary or a decision surface. That is the intuition behind what we are trying to do in classification.

50:16

We have here here here one term used here binary versus multi-class. Now multi-class is not a focus

50:21

area for today, but just to give you the intuition, binary is where there are two classes.

50:27

So we're example you to give you right now, whatever use case.

50:29

we have talked about so far, we are only two possible classes of output. That is what we refer

50:37

to as binary. So either it is slow or it is fast. Based on the mark secured by the student,

50:45

either you will predicted to be passed or predicted to be paid. Yeah, binary here. Either it is

50:50

this or it is this. That is what we refer to as binary. Whereas multi-class, it is more than two classes.

50:55

Binary is always two classes, multi-classes more than two classes. So that's one.

50:59

I mean, example of multi-class could be, let's say, you, you up, up, up here we

51:05

we are trying to predict the speed is either slow, or past. Either it is slow or it is fast.

51:10

Now, an example of multi-class would be, yeah, it is slow or it is medium or it is fast. That's

51:15

it, you can change it to multi-class at this. Now, I can say either it is slow or it is medium

51:19

or it is fast. That's to that way it becomes a multi-class classification. Another great example

51:23

of multi-class could be if I, if I relate this in the context of a disease use case.

51:29

disease prediction useless. So based on the features of the person, you are trying to predict

51:35

whether the person has, you know, low diabetes, medium diabetes, your high diabetes.

51:45

I'm just trying to, you know, classify diabetes into different categories. How severe

51:52

diabetes is? You know, I think, you know, some people have so extreme diabetes that they will have to take insulin.

51:59

and then there are other people for who insulin also doesn't want. So we are trying to

52:04

categorize. So can we look at the different indicators of the person and can we predict?

52:11

What level of severity is? What level of disease? What level of diabetes? Not just yes or no.

52:17

Not just a yes for prediction, but we are trying to predict what is the category of the disease.

52:23

Is it a level one diabetes? Is it a level two diabetes or is it a level three diabetes? Or is it a level four diabetes?

52:28

anything more than two is multi-class problem. But the story remains the same.

52:33

Nothing changes. Just keep this at the back of your mind, all of you. This is how we think through

52:37

classification. The SM classification is so such dedicated. I will dedicate another five to 10

52:45

minutes in the class more to talk a little bit more about some theory. And here, I will give you a little bit

52:52

for intuition in terms of how to think through classification, a little bit of math idea that we'll talk

52:58

about very intuitively and then we will go to the coding part. So that is how we will

53:03

paste it out. Now, moving on, as I was explaining, I'll come back to the diagram, you know,

53:17

one second for you. Look at us all of you. So, you have, you have, you have, you have, let's

53:28

for a minute that you have a problem and look at the left and side. Let's let's take a particular

53:34

classification problem, which we've already discussed here. So I'm just trying to take this

53:41

example here once again for you. You have x-axis? You have y-axis. X-axis. X-axis tells you how much

53:51

of this could be something like your attendance or your

53:58

or some kind of attendance or study hours.

54:03

You have your study hours have. And based on study hours, we are trying to predict whether you will pass or not.

54:16

So, so, data set, how is? Data set, what is? Data set? Could? Let me draw this out. You have a study hours

54:22

is okay? Now, while while I'm explaining this, all of you, please ignore the right-hand side.

54:28

part, all right? Just ignore it. I'll explain to you. This right

54:31

what is this S curve? What is the sigmoid curve? I'll take a minute to explain. Don't worry,

54:36

okay? So first let's understand the left inside part. Okay. Now,

54:42

study hours and we've got pass. This is your X and or you have a while. Now, study hours will take

54:51

different different values and pass to, or it will pass one or it will fail zero.

54:58

One matter pass yes. Zero, meant a pass no. This is how the data will look like, okay?

55:04

So this is another way you will typically see classification problems are framed. So oftentimes we don't

55:10

explicitly say pass is yes or no. We say pass, yeah, one is zero. I mean, but one is like saying,

55:16

yes, and zero is like saying, yeah, pass, no. So that's one way to convey it, okay? So just to clarify.

55:24

So one is like pass yes and zero is like, you know, how we say it is like. You know, how we say it is like.

55:28

That's one way to kind of look at it. Okay. Now, moving on, moving on, moving on. So if you try to plot this data,

55:46

first question is, can we solve it like a regression? Can we solve it like a regression? Can we solve it like a regression?

55:53

If you have regression in a regression, what will happen? You have to, what will happen? You have, you have, you

55:58

have a set of data points. Data points is something like, right? If you can see, you can take some

56:03

real values and check. If you're actual data, if you're, actual data, either pass or fail

56:09

nothing in between. The pass value point seven, not. Pass value point seven, not. Pass value point

56:13

four, not is. The actual data is, we have Masai's student's data. So we have data already

56:19

is. The man, how many can measure based on, let's say, you know, we'll have different engagement

56:24

metrics. Like, whatever data we can gather. One will be how much of class time you're

56:31

spending. Second will be how much time outside the classes you're spending. After the classes get

56:36

over, how much time you're going back to the platform. A platforms and recordings

56:39

are we can keep a track of that. Exercise time. All of those things we will use to estimate the

56:45

study hours. So study hours data we have for every student. And we will also know whether the

56:50

person passed on day, as an example. Now, pass fail itself is a very broad discussion, but we will

56:54

internally have some metrics. So this data we have

56:57

historical data for all the students. Now first thing is you want to plot this data.

57:02

If you're if you look somewhat like this, you agree.

57:05

Now, look, all these students study hours, if are more or less

57:12

come, then they did not pass. Zero. It's past value zero. So for all these guys,

57:17

pass value zero and for all these guys, pass value one hand. This is what your data looks like.

57:23

Now, if we try to solve this problem like a regression problem, what will happen?

57:30

What will happen behind the scenes? Behind the scenes, we are trying to do this.

57:35

We have discussed a regression story last week. Regression me, what do guys?

57:39

We are trying to find out what is the line or plane or mathematical surface that best? We are trying to find out what is the line or plane or mathematical surface that best? We are trying to find out what is the line or plane or

57:53

mathematical surface that best, that best fits the points.

57:59

That is what we are trying to do. Okay? So what is the, what is the line or

58:06

plane or mathematical surface that best fits the points? This is your best fit

58:12

got. You got your best fit. All of you are able to see. That is what you're able to see in terms of

58:17

the best fit. What is the issue with this? This issue can.

58:21

So, this issue is the issue here is that, if you want to go back and do a prediction using this,

58:34

man, if you can't study hour 100 or somebody's study hour 60 is, so model predict

58:40

predicts 0.6, right? If someone's study hour 20, model predict can't minus 3. Now, you cannot

58:47

pass the exam 1.73 times.

58:50

It's not?

58:52

If a study hour 90, then model predict will 1.7?

58:55

No, this is the reason why we cannot think through this kind of a regression thing.

59:02

Now, logically, you can't say, sir, this is regression.

59:06

One is zero, so it. Okay, it. No part. We're, we're data to scatter plot in like how I taught you last week.

59:12

And we will try to do that. Why, you can do that. Why? You can do that. Problem is this.

59:18

Even if you end up drawing that line,

59:20

you, you cannot have a value between 0 and 1.

59:27

Fasts value 0 and 1 between no one.

59:29

That's no matter of that.

59:31

If you're back any other than example, what we talked about in regression,

59:34

you take the last use case period on Monday, California housing price.

59:38

California housing price can be between 0 to 50, any number it can take.

59:41

Which any number can take.

59:42

Any number may say, 70.9, 20.999, 20.999, we are absolutely okay.

59:48

But, but pass the value will either be 0 or be 1.

59:52

Nothing in between.

59:54

That's the issue, guys.

59:55

Okay?

59:55

So, everyone's aligned.

59:57

Now, moving on, how do we solve the problem?

1:0:04

So this is to help you explain, that this is actually a classification problem.

1:0:09

You can't it.

1:0:12

So, solution what is?

1:0:13

This for we use something called a sigmoid function.

1:0:18

Intuitively I'm trying to explain.

1:0:20

This is where we use a sigmoid function.

1:0:21

Because we have this go best-fit lines as solved.

1:0:25

So we're going to singmoid function use and sigmoid function, what it basically does behind the scenes is,

1:0:30

it kind of takes that line and quite literally what you're able to, you know, see on the screens.

1:0:36

What it does, it quite literally does this.

1:0:40

I mean, it's clipping kind of, we call it clipping.

1:0:43

The edges have gone where the line goes both sides, it kind of clips it.

1:0:48

cliped here. This side be cliped and this type of shape. Now, you can again see,

1:0:55

ignore the internal mathematics behind it, but the most important thing is it squeezes the

1:1:02

predictions into a strict probability between 0 and 1. That is what the sigmoid function basically

1:1:09

does. And this is what is required for classification. We are not trying to predict the exact value of

1:1:15

pass. The pass value of 1.7.7 no.

1:1:18

So what we will do is, we will first do something like a linear regression.

1:1:24

That's-after, we go to a x-sigmae function-through what we can do is we can convert it into this

1:1:30

into this scale of 0-1. So it will basically take a strict probability values between 0 and 1.

1:1:38

So that is what the sigmoid function basically does, update system.

1:1:41

We are going from a raw score to a probability. That is what we do.

1:1:44

The mathematics is again not required. I'm repeating. Not required at all.

1:1:48

Even this is not required. I think we have actually put this in the diagram. So I'm just trying

1:1:52

to talk about it into a degree. But even this is actually not required from an implementation

1:1:56

perspective. You can't be but I'm still trying to take it through it a little bit. So all it does

1:2:03

is it goes and it shrinks the values in a scale between zero and one. So that's the way to look at it

1:2:09

overall. That's the way to look at it. Now, so now how do we, how do we kind of kind of

1:2:18

of complete the story with whatever we talked about so far. This was the internal

1:2:29

mechanics what we covered. This have an internal mechanics covered here all this while, right?

1:2:34

Regression. We cannot do it as regression. So use a sigmoid function and we cap the values between

1:2:39

0 and 1. Number two, we are actually trying to find out a probability. So sigmoid, what it does is,

1:2:47

what it does, it outputs a value between 0 and 1. And that we are we doing.

1:2:53

Ultimately based on the study hour, you have a pass

1:2:57

value chaiy and the past's the probability value that has to be between 0 and 1.

1:3:03

And now the probability can be a value in between.

1:3:07

That in between the value is.

1:3:09

The sigmoid is basically simply doing classification. It is helping you to the classification properly.

1:3:16

And it is output.

1:3:17

putting a probability. And now from here onwards, everything else that we will do in the class,

1:3:23

you can just remember this diagram. That sigmoid was just a small detour I wanted to do to help you

1:3:29

understand the inner mechanics to some extent. Now everything else will be based on this.

1:3:35

Now we have everything else about this respect. Again, coming back to the story, we have X,

1:3:40

we have Y. We are trying to find a line or plane a surface that best separates the classes.

1:3:47

This is your model. So when we use something like a logistic regression, which I'll demo

1:3:52

right now, logistic will do exactly this point. It will be able to separate the greens from the

1:3:58

edge. It will build a line or plane or surface that separates the two classes. This is your model

1:4:05

here. This is a decision boundary or decision surface. So based on the data, we are able to use

1:4:11

an algorithm and build a model. And now, very important guys, do both parts. Machine learning.

1:4:17

in the first part is dot fit. So dot fit we are able to build that line,

1:4:21

build that model, build that separation. Number two,

1:4:26

when we have our past a new data

1:4:27

then what will? Let us talk about that.

1:4:31

Naya data is. Steepness value point three is. Bumpiness

1:4:35

the value point four is. So point three is, point four

1:4:39

here. So let me just draw this out once again. So steepness value is

1:4:43

equal to, uh, steepness value is equal to point three.

1:4:47

bumpiness value is equal to point four.

1:4:49

This is new data. Which I have pointed out here.

1:4:52

Okay.

1:4:53

You can you. This is model.

1:4:54

Dot predict happening.

1:4:55

So next time our new data point is given.

1:4:58

That means I have already trained the cell driving car.

1:5:00

That cell driving car.

1:5:01

That self-driving car has everything.

1:5:04

He's steepness in how to go to this bumpiness

1:5:06

in case.

1:5:06

He's learned earlier. The model is already trained.

1:5:09

Now you are taking that model to production.

1:5:11

The self-driving car is on its own.

1:5:15

Now we've got it's on its own.

1:5:15

Now we've just go road in road to go.

1:5:16

So the moment it encounters a steepness value of point three and the bumpiness value of point four,

1:5:22

the car itself has to predict, based on whatever model is trained, what should be my speed?

1:5:30

So speed will be something like this.

1:5:32

This is your speed over.

1:5:33

So the model will predict fast.

1:5:35

That fast predict can.

1:5:37

Two things I'll say.

1:5:39

This we'll quote in detail in detail.

1:5:42

Dot fit model.

1:5:44

The equation dot predict say,

1:5:45

your class predicted.

1:5:47

And you can you see that most of the values here are greens and model will predict green.

1:5:51

I mean, fast.

1:5:51

And you're obvious.

1:5:52

If the steepness come and bumpiness come, the model fast predict can.

1:5:56

Number one.

1:5:57

Number two, number two, here is the important part.

1:6:01

In classification, in classification, we also find out, we not only predict

1:6:08

that the car will go fast, but we also try to find out the probability of the prediction.

1:6:14

The important thing is to find out the probability of the prediction.

1:6:25

So this one story is clear. Everybody understands this.

1:6:29

This we're in port on, then dot fit, which we already did before.

1:6:33

Train test, split, dot fit, model been made.

1:6:35

And this one thing how we make out?

1:6:37

Dot predict.

1:6:38

This story we have.

1:6:40

These two stories we know.

1:6:41

These two stories we know.

1:6:41

Dot fit what, dot predict, what?

1:6:42

Dot predict, what?

1:6:43

Then, now a value do? I will plug it into the model and find out what is the predicted value.

1:6:47

This story is the new story that we will learn today is dot predict, dot predict underscore proba.

1:6:58

Court in the case, just.

1:7:01

But intuitively, you'll it's how can't you?

1:7:03

Intuitively, you can't it as you can't based on the new value of X that is given,

1:7:10

what is the probability that the speed will be fast?

1:7:13

how confident are you that the speed be passed?

1:7:18

And his intuition here will be the, the closer the point is towards the separation line,

1:7:26

so that you're confident not, you're not.

1:7:28

So, you mean, here here, you look, point three and point four,

1:7:32

fast to have, but am I very confident that will be fast?

1:7:36

Maybe not. So predict proba's value, it's something close to a 50-50.

1:7:41

50-50 to not be, let's say, we are only like 60% confident it will be fast.

1:7:49

Rather, we have one example

1:7:51

if, mano, point where it would be here, let's say,

1:7:54

steepness's like 0.01, and bumpiness's the value is like 0.07.

1:7:58

I mean, data point here is here.

1:8:00

If point here were, then, then we are very confident, the garrie fasts.

1:8:04

It's there no doubt in it.

1:8:06

So here here here there are some points of red here, some are red here.

1:8:11

So neighbor room in the red points there.

1:8:13

So we are not very confident.

1:8:14

That's why the probability of fast is 60%.

1:8:18

But if I give you a new data point like this,

1:8:22

okay, steepness value 0.01, bumpiness the value 0.07.

1:8:26

And now you have to predict that what's speed what?

1:8:29

Fastly will still predict fast.

1:8:31

Now the interesting part is what is the probability of the prediction?

1:8:34

The probability of the prediction will be probably close to 97%.

1:8:40

97% or 99% whatever.

1:8:43

So that's one way to look at it.

1:8:44

So, Gurtak, so 100% be your own-the-line is always 50-50.

1:8:48

Always, always-al-50.

1:8:50

So theoretically, 100% will be like,

1:8:52

like, a-dum-so, the original-point

1:8:53

and then here your 100-pac-a-as-past-past-pac-pac-past-pac-pac-pac-us.

1:8:57

Somewhere, at one-downss,

1:8:58

where there both value is zero,

1:8:59

so here something like a hundred-h-h-h-h-h-h-h-h-h-h-h-h-h-h-h-h-h-h-h-h-h-h-h-----------------.

1:9:04

So just this is what, how I want everybody to think through classification.

1:9:10

Yeah.

1:9:11

Yeah, the further, see, the way to look at it is,

1:9:16

the closer you are to the line, because this is your separation is, right?

1:9:20

If you're like that the best fit, the line is a separator.

1:9:25

You have a red class.

1:9:26

You have a green class.

1:9:27

Line is separated.

1:9:29

The separator is used to find out whether it is red or green.

1:9:32

If your data point, if your data point,

1:9:34

If your predicted value, that line is a past, then you're not very confident.

1:9:38

That it can red be green be or green.

1:9:40

Line, there's a little this part here, then red it'll,

1:9:42

if it's right, so that's like 50-50.

1:9:45

So the closer you are to the line, 50-50 chance is.

1:9:48

And the further you're at this side, the further you're this side,

1:9:52

it'll be from 0 to 100.

1:9:53

Make sense?

1:9:56

Got it?

1:9:58

No, the same story.

1:9:59

Same story, good.

1:10:00

So, line, if a curve be heard, if a curve be heard,

1:10:02

if your curve be, if your curve be a, if your curve be

1:10:03

so concept remains the same.

1:10:05

Because the concept of decision boundary does not change.

1:10:07

This is the standard concept.

1:10:08

This is the standard concept.

1:10:09

Decision boundary, what is the separation between the classes?

1:10:13

So the concept remains exactly the same.

1:10:14

Nothing changes.

1:10:16

Okay, that's the time we're kind of curve-based

1:10:18

on tangent-like-am-local calculate.

1:10:20

But that's a different story.

1:10:21

That's the mathematical part.

1:10:22

But what you're saying is, to some extent, correct.

1:10:25

So we take a distance of the point from the line and decalculate.

1:10:29

But that's the mathematical part that is not required.

1:10:31

But the intuition, what you are saying is right.

1:10:33

Okay. Okay. Now, guys, let us go back to the, okay? Yeah, good. Now let's go back to the

1:10:43

implementation. Whatever we talked about in classification, let's see a small implementation.

1:10:49

And as I promised you in the beginning of the class, the code is exactly the same. Nothing

1:10:52

will be different in the code. Okay. So, so first what I will do, I will import the necessary

1:10:59

packages. And you can see the packages are all known to us majorly.

1:11:03

majorly the packages are known to us.

1:11:05

Train test split, we have seen SK learned linear model.

1:11:10

The only difference is we are importing something called logistic regression.

1:11:15

This is used for classification.

1:11:17

Min-max scalar we have already seen.

1:11:19

Make pipeline we have already seen.

1:11:20

Pipeline is used to combine multiple pre-processing steps together.

1:11:24

You can use the pipeline to go back and combine multiple pre-processing steps together.

1:11:29

So we've had last class in pipeline used to,

1:11:31

how win-macks, then, then, algorithm.

1:11:33

And finally, this is the new part we will see.

1:11:36

I mean, it's got theoretically discussed last to last week I recall.

1:11:42

I'm in this time of precision recall discussed. It was a long discussion.

1:11:45

You remember for Confucian matrix?

1:11:46

So, a quite long topic. I think last two last week. I think last week I covered.

1:11:52

Confucian matrix, precision, recall, f1 score. Same story.

1:11:55

That time I told you, when I was taking that session, I told you that guys, later in another class,

1:11:59

the same thing is talked about. So today is that class.

1:12:02

Today, we're back from the confusion matrix

1:12:04

which we've already in the class in detail

1:12:06

same story.

1:12:08

And here, we will see this in code.

1:12:10

Okay?

1:12:11

Now,

1:12:11

Confucian matrix, what is it, guys?

1:12:14

False negative, false, positive, true, negative, prove positive.

1:12:17

Yeah, that explanation I did.

1:12:19

I'll once again explain to you, don't worry.

1:12:21

Now, moving on, this is the sample data that I have given to you right now.

1:12:27

So you have study hours, you have sleep hours,

1:12:29

have distractions, and based on that,

1:12:32

you are trying to predict whether the person will pass or be.

1:12:35

So you need to predict, yeah, the result pass will, that is, result will be one, or result

1:12:40

zero, that means the person will fail.

1:12:43

This is your simple data.

1:12:45

Now, in a real world scenario, this data you have you available here.

1:12:48

Let's say we have done a survey at Maasai and we have got the data from the students.

1:12:51

You have got the data available here.

1:12:52

Study awards, team, problems, distractions, on that basis, you are trying to predict what the result

1:12:56

will do.

1:12:57

Result need be either one or result will be zero.

1:13:01

So data is there.

1:13:02

Now we will train a logistic regression model.

1:13:05

The story demands exactly the same.

1:13:07

How do we do this?

1:13:08

So we will simply segregate what is X and what is Y.

1:13:11

Is it a standard machine learning process now?

1:13:13

Nothing is different.

1:13:15

You have X what?

1:13:16

Study hour, sleep over, distraction.

1:13:18

All these three are part of your X.

1:13:21

This all are your X part.

1:13:23

And what is your Y?

1:13:24

Your Y is result.

1:13:25

So these three are your X part.

1:13:28

This is your Y's part.

1:13:30

Next, what do we do?

1:13:31

We do the train test plate.

1:13:33

This is the train test split story.

1:13:34

We've already seen that.

1:13:37

This is the part where we use the logistic regression algorithm.

1:13:40

We build the logistic regression model.

1:13:43

Intuitively, what is happening?

1:13:44

You are trying to fit that separation.

1:13:47

And finally, you're calculating what is the train score?

1:13:49

What is the test score?

1:13:50

This story remains exactly the same.

1:13:52

And by looking at this, we can say, if we have a decent model to start with it.

1:13:58

I'm the data here.

1:13:59

I'm the model made up.

1:14:00

And we're able to see that we have a model which is giving us 93, close to 94% brain accuracy,

1:14:10

close to 92.5% test accuracy.

1:14:12

So this is a decent, decent model, decently good fit model.

1:14:16

So can we make it better?

1:14:17

Yes, potentially.

1:14:18

This is exactly the part where you teeterate and try.

1:14:21

I mean, or try it kind of so that we can make it better.

1:14:23

And we talked about that story last session, overfitting, underfitting, good fit.

1:14:26

This is what we are starting out with.

1:14:28

We are getting a model, a baseline.

1:14:30

model, a basic model to start with. Can we make it better? Yes, we can try different methods.

1:14:34

We can try different algorithms. Okay. We will see a new algorithm in the next session,

1:14:39

your next classroom on Monday next week. We will see a new algorithm. So with that, probably we'll get a better

1:14:45

result. So it is an iterative way how we go and do machine governance. But using logistic, I'm getting

1:14:52

a decent model. Okay. Now, moving on, this part, we already know. Dot fit. And as I told you,

1:15:00

in the explanation a while back, how it makes a decision.

1:15:05

How do we calculate the predictions level?

1:15:08

So do two ways.

1:15:10

One is dot predict and second base dot predict program.

1:15:18

Okay, I will run the code for a minute for you. And as you can see,

1:15:21

when you call model dot predict, as I explained to you, it gives you hard zero or one.

1:15:28

It will give you the actual classes.

1:15:30

But you have surface to have, you know, you've got, you know, you're on the surface

1:15:35

kind of side. That's it. It's either predict zero or either predict one. That's it.

1:15:39

Either pass, or fail. Or slow or fast. That's it. Simple story.

1:15:45

But internally what are? It's just to understand to us. But internally what is happening. It is

1:15:50

always calculating a probability using predict proba. Now, this is the part that is a new thing that we are

1:15:56

studying in classification. This regression may not down.

1:16:00

Now, we'll say, sir, regression in prediction? Regression will only, you're doing a dot

1:16:06

fit, you're building a model, and you're saying dot predict to calculate by his new X, then predicted

1:16:12

y, that's it. Story ends there. In classification, the additionally, you can find out the probability

1:16:18

of the prediction. So, so we can find out the probability of the prediction. And please remember,

1:16:25

by default, if the probability of passing is greater than equal to 55,

1:16:30

The model confidently shouts the pass. So the 50% is the default threshold that is used.

1:16:38

So it's, so the prediction basically happens in two phases. If I have to just summarize the concept for you.

1:16:45

So you don't know phase phase may be okay. First phase, you're doing dot fit.

1:16:51

Dot fit's a model been here. Now, new data comes.

1:17:00

you will use dot predict proba you will use dot predict prova to calculate the probability of the predictions or other probability you will use dot predict proba to calculate the probability of the prediction if the probability of the prediction is more than a certain value excuse me guys if the probability is more than you know if the probability is more than a certain

1:17:30

value, then the model will predict this or the model will predict this.

1:17:35

So, sub-separalli, you will find out the prediction probability.

1:17:39

If it's 50% more, okay, let me write the story now.

1:17:42

If, if probability, I'll use prob, probability of pass is greater than 50%, then the model

1:17:58

will predict us, else the model will predict fail.

1:18:04

This is what is going on behind the scenes.

1:18:07

Behind the scenes are here.

1:18:08

This is a layer that we don't usually see.

1:18:11

We're in court in the court in, we just dot predict call, so we'll answer will show you in a minute.

1:18:16

But in case you're wondering, sir, what is behind the scenes.

1:18:19

Behind the scene, this is what is happening.

1:18:21

So we're both ways to show you to make.

1:18:23

Model been got, that story is over, trained test.

1:18:25

We have fit that best fit line.

1:18:27

That is over.

1:18:28

Now I will tell you that when I give you a new data, that means when I give you a test data,

1:18:33

now we'll test data, we'll give them probabilities calculate and I will show you that

1:18:38

whichever cases the probability is more than 50%, the model has predicted pass.

1:18:47

Let's say there is a particular student where the model predicted that his probability of pass

1:18:51

is more than 55%.

1:18:53

So model in a pass predictor.

1:18:57

And there is another student where.

1:18:58

the probability of passes, let's say, 46%, they're going on behind the sales.

1:19:06

Okay?

1:19:07

So this is the default behavior.

1:19:09

Please remember, this is what we call the default behavior.

1:19:12

I'm again highlighting this is bold, because it's default.

1:19:17

And default is the matter of what you can't.

1:19:21

And this is our next discussion will later later.

1:19:23

How to change this is what repercussions will.

1:19:25

We will come to that story.

1:19:27

I hope everybody is aligned.

1:19:28

And now, let me, let me take you to the code.

1:19:34

Model been here.

1:19:35

And now let me show you the results.

1:19:37

This your hard predictions and your prediction probabilities have.

1:19:41

And this is the data frame that I'm trying to generate for you.

1:19:43

I'm just showing you the actual result.

1:19:45

What is?

1:19:47

The probability of passing what is and hard prediction?

1:19:51

Let me show you.

1:19:53

I think we are showing the,

1:19:57

um,

1:19:57

five results are you can see some more if you want.

1:20:01

Here basically we're here.

1:20:02

Basically, we're 5th, but if you want to see some more,

1:20:04

we'll just take 10 to take.

1:20:06

So that you can see some more numbers.

1:20:10

You can see some more numbers.

1:20:10

I think, I think it's very easy to follow now.

1:20:13

So let me explain to you.

1:20:15

Remember, dot fit is over, motor is already built.

1:20:17

And given a new data point, given a new student's data,

1:20:22

the probability of passing,

1:20:23

this is your probability of pass, P pass.

1:20:27

The probability of pass, sorry, sorry, one second, what happened here?

1:20:34

Sorry.

1:20:36

This.

1:20:40

Ah.

1:20:44

You have got a probability of pass.

1:20:47

And you can see that whenever the probability of pass is 0.01.

1:20:51

0.01, what is the 1%.

1:20:52

Both come here.

1:20:54

This is like 1%.

1:20:55

The probability of pass is very low.

1:20:57

the model has predicted 0.

1:21:00

Just to clarify the story,

1:21:03

pass equal to, so this is like 1.

1:21:10

And fail is like 0, just to clarify.

1:21:12

Pass,

1:21:12

I mean fail, so 0.

1:21:14

So if the probability of pass is so low, 1%.

1:21:18

1.1%, so model has predicted a fail.

1:21:22

Or the probability of pass is 53%,

1:21:24

0.53%,

1:21:25

33%?

1:21:26

50%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%..

1:21:32

So behind the scenes, herep%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%..

1:21:49

Here here here, the model is very confident.

1:21:51

So, I mean, this student's, so much, maybe it is students,

1:21:55

sleep is very good, study hours is very good.

1:21:59

So the student is well rested.

1:22:01

So we are very confident the student will pass.

1:22:03

There's a 95.69% probability that person will pass.

1:22:07

So model has predicted pass.

1:22:09

So this probability is important because

1:22:11

this from it's not just, see,

1:22:14

hard prediction is not important.

1:22:17

Hard prediction, it's, you know,

1:22:18

it, you'll predicted value will be.

1:22:20

But in a classification problem,

1:22:23

what is also very important for us to know,

1:22:25

is how confident am I about the prediction?

1:22:28

Now, look at this guy, look at this guy.

1:22:32

Look at this guy.

1:22:33

This person has a 99.9.97% probability that person will pass.

1:22:40

There is like a 99.99.97% probability this person will pass.

1:22:46

So that makes me very confident. This guy is brilliant.

1:22:50

But now, you, up, up, up, this go to this case.

1:22:52

This is, on one hand, I give you this guy.

1:22:55

on one hand, I give you this guy.

1:22:57

Both are pass are.

1:22:58

This also pass are.

1:23:00

It's like, this person just got past the finish line.

1:23:04

So we've made it's got it in the finish line.

1:23:05

But, like, if you're really evaluating the students

1:23:09

based on their capability and potential,

1:23:12

you will look at the predic proba.

1:23:14

If you'll look at predic proba, then you'll look at

1:23:16

clearly see that the probability of passing

1:23:18

is much higher for this person.

1:23:20

I mean, this person is brilliant.

1:23:22

That's one way to look at it.

1:23:23

I hope everybody is with me overall.

1:23:28

So there are two new concepts we have studied.

1:23:30

We have seen something called predict proba.

1:23:32

We've seen something called predict.

1:23:34

Okay.

1:23:34

Remember, SK Learned default 50% here.

1:23:38

This is happening internally using SK learn.

1:23:41

You don't have to do anything.

1:23:42

If you look at the code once again,

1:23:44

I'm a dot fit here, model been madeaaaaer,

1:23:46

we're able to get.

1:23:49

And by default, based on the 50% threshold,

1:23:53

the predict function is automatically working here.

1:23:56

That is something that I wanted to clarify.

1:23:59

Okay.

1:24:00

Okay. And finally, the level four,

1:24:01

the last part of the story is where we are trying to basically find out where we went

1:24:09

from, okay?

1:24:10

Which other sessions where we failed and where is it that we actually went wrong.

1:24:13

So here we will talk about the concept of the confusion matrix and whatever we have

1:24:18

already seen, I'm going to recap that a little bit for you.

1:24:20

So we can see the confusion matrix.

1:24:21

This is the main, uh,

1:24:23

the last topic that is left out.

1:24:25

And after that, we will see some,

1:24:26

some end-to-end case studies and I'll keep sufficient time today for some case

1:24:30

studies so that we are able to use all these things in action today in the class.

1:24:33

Okay. So we can take a short break right now.

1:24:37

Okay, let us take a quick session break.

1:24:39

And after the break, I will ask, this is again, just to clarify,

1:24:42

Satyseme, same folder, same story, as we do for all classes.

1:24:45

I've uploaded the folder.

1:24:47

All the contents are here for you.

1:24:49

So everyone can refer on to this one.

1:24:51

So this is a demo.

1:24:53

P-Y-N-B-5 that I'm referring in the session right off.

1:24:56

Okay, so we can take a break and let's circle back after the break and we'll continue from here onwards.

1:25:23

Thank you.

1:25:53

Thank you.

1:26:23

Thank you.

1:26:53

Thank you.

1:27:23

Thank you.

1:27:53

Thank you.

1:28:23

Thank you.

1:28:53

Thank you.

1:29:23

Thank you.

1:29:53

Thank you.

1:30:23

Thank you.

1:30:53

Thank you.

1:31:23

Thank you.

1:31:53

Thank you

1:32:23

Thank you

1:32:53

Thank you

1:33:23

Thank you

1:33:53

Thank you

1:34:23

Thank you

1:34:53

Thank you

1:35:23

Thank you

1:35:53

Thank you

1:38:23

Hi,

1:38:26

So,

1:38:27

Before you

1:38:28

Before you

1:38:29

Just

1:38:30

Just

1:38:31

Just

1:38:32

We

1:38:33

We'll

1:38:34

We'll

1:38:35

We'll

1:38:36

We'll

1:38:37

We'll

1:38:38

We'll continue on

1:38:41

and

1:38:42

Before the break,

1:38:44

just to

1:38:45

summarize the story that we covered

1:38:46

We looked at how to

1:38:49

build the model

1:38:52

we looked at. We also understood the concept of predict proba.

1:38:56

That is something that is a little new what we do in classification.

1:39:01

So predict proba only classification

1:39:03

regression in

1:39:04

So we are able to basically take the data and we are able to predict, find out the probability of the

1:39:11

predictions.

1:39:12

So there we

1:39:14

there we understood the concept of what is predict roba.

1:39:20

So we covered that.

1:39:21

that and now we will try to understand what are the errors and what are the mistakes the model is making.

1:39:29

So we see this idea of Confucian matrix.

1:39:32

So and why why is Confucian matrix important?

1:39:36

If you relate to the discussion we had before in the last thing, one of the important things was we talked about the fact that

1:39:46

you can have a model that is very accurate.

1:39:49

Right?

1:39:50

You can have a model that.

1:39:51

that is very accurate, but how do you know where it is making mistakes?

1:39:56

What are the false positives? What are the false positives? So I want to know explicitly where the model is making mistakes.

1:40:01

So this model we've made that is giving us 92.5% accuracy.

1:40:06

I mean approximately seven and a half percent error it is making, right?

1:40:09

100 minus that is the error.

1:40:11

Where are mistakes going? I want to know that.

1:40:14

But what mistakes? What? Mistakes? What? Yeah, to model predicted pass, but actually fail?

1:40:19

or model predicted fail actually pass.

1:40:23

That is exactly what you are trying to understand in the Confucian matrix.

1:40:29

You are trying to explicitly understand where the model is making mistakes.

1:40:34

So that is what your Confucian matrix shows.

1:40:38

It shows exactly where our errors happened.

1:40:41

So how do we build the Confucian matrix?

1:40:46

We use the Confucian matrix function.

1:40:49

And we simply give the actuals and comma the predicted.

1:40:53

That's it.

1:40:55

Because the confusion matrix is a kind of an actual to predicted comparison.

1:40:59

It is a kind of an actual to predicted comparison.

1:41:02

So you basically plot the actuals along the rows.

1:41:07

You plot the predicted along the columns.

1:41:10

And this is how we understand the confusion matrix.

1:41:13

We have seen this in detail in the last session.

1:41:15

I'm just recapping this once again for you.

1:41:17

So model up a better.

1:41:19

model got fit the model made. This is the model you already, you know, created.

1:41:26

And along the, along the columns you plot, what are the predicted values?

1:41:31

Predicted zero, predicted one, that's your columns percha chalayae.

1:41:35

Actual zero, actual one, your rose may go, okay?

1:41:38

And if he predicted, zero, predicted one, your columns on to go.

1:41:42

Actual zero, actual one, your rose by chalaya. And this is how the ambition matrix looks like.

1:41:47

True negative means model predicted negative and the general convention that we use is

1:41:55

the general convention that we use is negative is always zero and positive is always one.

1:42:03

But of, this is your convention.

1:42:05

But whatever you are trying to predict is always considered to be a positive plus.

1:42:13

I can give you an example.

1:42:14

Just say mano bank here and the bank wants to build.

1:42:17

a model to predict credit card fraud.

1:42:20

He's what to predict?

1:42:21

He has to fraud predict kind of fraud.

1:42:22

So fraud is like a positive plus.

1:42:25

Bank doesn't want to predict not fraud.

1:42:26

Not fraud.

1:42:27

That's a good thing.

1:42:28

But you want to find out frauds.

1:42:30

So if you're having a conversation with the executives of the bank,

1:42:36

they want you to build a model to identify frauds.

1:42:40

We want to know which are the transactions are frauds.

1:42:43

That is how the conversation will go.

1:42:44

He will not be.

1:42:45

He'll not say, hey, hey, hey, hey, hey, can you build a model to identify?

1:42:47

identify not frauds.

1:42:48

I hope you're getting it, sir.

1:42:50

So whatever you're trying to predict is a positive class.

1:42:53

So bank's case, fraud positive class.

1:42:57

You can talk about the must high school.

1:43:00

Here we have our past positive class.

1:43:02

Because we want to identify who are the students who will pass.

1:43:06

Something like that, okay?

1:43:08

Spam positive class.

1:43:09

We want to identify which are the males are spam.

1:43:11

So that is the way how we can understand what is positive and what is negative.

1:43:15

So TN, Maltz.

1:43:16

that means true negative, model predicted negative.

1:43:20

Whatever is written on the right hand side, this is like what the model predicted.

1:43:24

So model predicted negative and the prediction is true.

1:43:27

Actual also negative.

1:43:28

So this is true negative.

1:43:30

Predicted negative actual also negative.

1:43:32

Predicted zero, action,

1:43:33

0.

1:43:34

What is true positive?

1:43:35

Same story.

1:43:36

Model predicted positive plus and the prediction is true.

1:43:40

But the model net positive predict here and the prediction is true.

1:43:45

Actually is also positive.

1:43:46

That is how.

1:43:46

we understand two positive.

1:43:48

So this is the correct predictions the model is making.

1:43:54

Now, what are the errors in the model?

1:43:56

The errors in the model are false negative and false positive respectively.

1:44:00

These are what we refer to as the errors in the model.

1:44:02

The mistakes the model is making.

1:44:04

So false positive is nothing but model predicted positive and the prediction is false.

1:44:11

That is what the meaning of false positive.

1:44:14

So model predicted positives.

1:44:16

and the prediction is false.

1:44:19

Who are your false positive?

1:44:23

So model,

1:44:24

model predicted positive and the prediction is false.

1:44:30

This is like a false alarm.

1:44:33

Agarap, if you're a fraud case as so, okay, it is like saying,

1:44:35

model predicted fraud, but actually it is not a fraud.

1:44:39

You know, you're falsely alarming the team that, okay, it is likely fraud.

1:44:43

You get false alerts on your mobile phone also, right?

1:44:45

False alerts.

1:44:46

that's, okay, this transaction might be a fraud or some fraud happened, but actually nothing happened.

1:44:55

Sometimes, you know, when you're accessing a public Wi-Fi,

1:44:58

you know, if you're airport in or any railway station in, go to public court spot correct,

1:45:04

your computer's anti-virus, that will be that, that's a threat detected.

1:45:08

That also, a great example of classification, by the way.

1:45:11

So, you know, all these antivirus softwares are also a great example of classification.

1:45:15

So based on what you're browsing, based on your Wi-Fi, and based on the website,

1:45:20

the model will predict how it's likely to be a threat.

1:45:22

Model-in-the-pred-model-per-the-but actually that threat not.

1:45:26

So false alarm, it's falsely warning you.

1:45:30

And false-negative is like sometimes very dangerous because

1:45:34

it's going to be model predicted negative.

1:45:38

Model predicted negative, but prediction is false.

1:45:40

Actually, it was positive.

1:45:41

I mean, predicted negative action positive.

1:45:43

That is sometimes dangerous.

1:45:45

think of this in the context of fraud.

1:45:47

But the model has predicted that fraud not, but actually that fraud is.

1:45:51

So a fraud gets missed out.

1:45:54

Fraud happened in reality, but the fraud actually got missed out.

1:45:59

That's one way to do that.

1:46:01

That is how we understand the meaning of false negative.

1:46:05

Disease prediction about we're going to do.

1:46:07

So model predicted you don't have a disease, but actually you do.

1:46:12

Very dangerous.

1:46:12

Because, you know, in reality, the person has.

1:46:15

a disease but the modern predicted you don't you miss out the fact that the

1:46:19

person actually has a disease these are some practical things I wanted to kind of share

1:46:25

with you and as I told you the industry context like how do you decide which is which is

1:46:31

better and and you know again it depends completely depends in some cases false positive is

1:46:37

bad in some cases false negative is bad it completely depends on the context there are a few

1:46:43

use cases I'm trying to share with you.

1:46:46

Okay.

1:46:47

Now, look, sending a severely sick patient home unchecked, catastrophic life-threatening error.

1:46:53

So if you're a medical case or disease prediction case as far as to go, false negative is unacceptable.

1:46:59

False negative is, this case may have a mist detection.

1:47:02

But the model predicted, you don't have a disease, but actually you do.

1:47:05

That is a very dangerous situation.

1:47:07

Unacceptable. So in a real world scenario, these are the metrics on the basis of which your

1:47:13

customers and clients will evaluate, that your model is good.

1:47:16

If you're, let's say, all these are dot fit, dot predict, and code may

1:47:20

go and finally, you have you have to result for it, customer to, customer will ask you,

1:47:25

that, boy, your model in, how many false negatives are, how many false positives are?

1:47:28

So if you, you're, if you're, you're saying, you're going to, you tell me how many

1:47:33

false negatives your model is giving me?

1:47:36

And you've said, if our model has two false negatives are, so that's a dangerous thing.

1:47:40

Hospital will never accept a model.

1:47:43

that is giving 20 false negatives.

1:47:44

Because that, the patient who you're going to go back and go to hospital to case

1:47:48

so 20 false negative means there are 20 times, 20 cases where the modern predicted

1:47:53

that man is sick, but actually they were sick.

1:47:57

That person can eventually come back and sue the hospital.

1:48:00

So false negative is dangerous.

1:48:01

But false positive is like something that always happens.

1:48:04

It is a false alarm.

1:48:06

So it is falsely telling a person they are sick.

1:48:09

That's not daily not.

1:48:11

And if you see in healthcare, it's a carcuit.

1:48:13

It's a lot of routine. If you go to a doctor to a hospital

1:48:17

go, you'll, you'll first test will give you.

1:48:20

So, that panel test is all.

1:48:23

Everybody in hospital in a hospital, you're admitted, so that's all by default

1:48:26

are. It is not that. So they are by default assuming the worst.

1:48:31

That is the way how doctors operate, majorly.

1:48:34

So doctors are by default assuming, that it's this can, this can, this can.

1:48:38

So doctors are already predicting that the person might have the disease.

1:48:41

I want to rule it out.

1:48:42

it is all it is like that.

1:48:44

So doctors are operating on the philosophy that we never want to miss anything.

1:48:48

So false negative should be zero, but false positive

1:48:50

is quite are.

1:48:52

So doctors just want to be absolute tissue.

1:48:54

I'll give an example.

1:48:55

If you're a blood test in hospital, if you're going to hospital in, so.

1:48:59

Final test in HIV tests, all.

1:49:01

Doctors want to rule out.

1:49:04

So normal blood tests and all if you do panel test CBC and maybe in hospitals, they will do

1:49:08

do those kinds of, you know, those kinds of tests also.

1:49:11

they want to rule out that you don't have any other transmission disease tests.

1:49:16

Okay?

1:49:16

So it is not that.

1:49:18

So they are suspecting you might have it.

1:49:20

So you, so, if you're, after he can't.

1:49:22

Because the doctor is already suspecting that you might have the disease.

1:49:28

I want to rule it out.

1:49:29

That's the way, you know, so two, tests to.

1:49:31

So that they are absolutely sure that, this is not there, this is not there, this is not there.

1:49:35

So now they're restricting that, now, they're restricting that,

1:49:36

yeah, a bit of the year for stuff.

1:49:38

Okay, so I hope you're clear.

1:49:39

So a lot of this depends on the business.

1:49:41

context.

1:49:42

Which error is important?

1:49:44

Which error we are going to give more preference to?

1:49:46

That depends on the business context.

1:49:49

Now you're in loan approval in.

1:49:52

False negative, I mean, rejecting a good customer.

1:49:55

Model predicted, the loan not going to.

1:49:57

But actually, the loan to give you.

1:49:59

But actually, the loan to know customer is a good customer.

1:50:00

You lose a good customer.

1:50:02

So there are different, different contexts in which this will matter.

1:50:07

So we will see a very real use case of this disease one.

1:50:10

We have a case study for that and we have another case study for finance.

1:50:14

You have finance and medical, both our case study here.

1:50:16

Real case studies are.

1:50:18

So we will see that and we will try to get some more context in this.

1:50:24

We'll see that.

1:50:26

Okay, I hope everybody's aligned.

1:50:27

And as I said, before the break, we talked about the threshold.

1:50:30

So threshold, the default threshold is always 50%.

1:50:33

Please give this at the back of your mind.

1:50:35

The default threshold is always 50%.

1:50:36

This is the default what happens in a scale.

1:50:39

If 50%, if it's the default,

1:50:39

if it's more than, then that pass predict will.

1:50:42

If it's a fail predict can.

1:50:44

Now, one thing that people typically ask, sir, can I change the threshold?

1:50:49

Yes, you can change it.

1:50:51

So model's a predict probae.

1:50:53

And then you can write an if-l statement.

1:50:55

You can do that if the predict proba is more than this, then I will predict this.

1:50:58

Else I will predict this.

1:51:00

But the dot predict function is by default based on 50%.

1:51:04

If the dot predict, if you use for it, then by default 50% based on.

1:51:08

But you can absolutely work.

1:51:09

with your own thresholds.

1:51:10

You can absolutely go back and pull it.

1:51:14

Okay.

1:51:14

Now, the question is, okay,

1:51:17

we, on what basis on threshold set kind of?

1:51:20

How's it.

1:51:20

So, threshold, trade off.

1:51:21

Threshold to default 50% is.

1:51:24

Dot fit model beena.

1:51:26

Dot, predict, proba.

1:51:27

Calculate the probabilities.

1:51:29

And based on the 50% threshold, model will predict,

1:51:32

either pass, or fail.

1:51:33

That is how the default predict function will work.

1:51:36

But, abe, you're up to defaults and not go to.

1:51:38

Now you're saying that sign.

1:51:39

I don't want to work with the default.

1:51:41

I want to use my own threshold.

1:51:44

So, you can set a threshold.

1:51:47

How can do you can have a lower threshold.

1:51:51

So, like, let's say at Masai, we want to be linear with our students.

1:51:56

So we can set a lower threshold, 30% probability of pass.

1:52:00

Even if the probability of pass is 30% model will predict fast.

1:52:04

Like that.

1:52:05

If we want to set a very strict threshold, let's say fast and fast.

1:52:09

fail is something based on placements or drives.

1:52:12

You know, let's say we are, I'll give an example.

1:52:14

Let's say these are, you know, this is the drive that we are doing for bulk recruiters.

1:52:18

So we want to identify, we want to give a more linear criteria for our students.

1:52:22

If the person is having a 35, more than 30% score, model will predict us.

1:52:28

That's bad set that drive in.

1:52:30

But here, let's say we are shortlisting people for companies like Google and other companies.

1:52:35

So they have a very stringent criteria.

1:52:37

So we want to be very sure the person is a good candidate.

1:52:39

So for us, we're criteria, more strict.

1:52:43

So how does the workflow look like?

1:52:45

Same story.

1:52:47

Let me just write this out.

1:52:48

Same story.

1:52:48

When we're we can it in code in the same thing.

1:52:51

We will say dot fit.

1:52:53

We will build the model.

1:52:56

Then we'll dot predict proba.

1:53:02

Dot predict proba.

1:53:03

We'll get probabilities.

1:53:04

Okay.

1:53:04

We'll have probabilities.

1:53:05

Then we'll not use dot predict.

1:53:08

Because remember, dot predict is.

1:53:09

working based on 50% threshold.

1:53:11

So, now we'll get, just we've got probabilities

1:53:13

now we have our

1:53:15

self-if-else statement taking.

1:53:17

Conditional if-selt statement, we'll

1:53:18

we'll write them.

1:53:19

We'll say, okay,

1:53:20

if the probability of

1:53:21

pass is more than

1:53:24

70%, then

1:53:26

model pass predict

1:53:28

or else

1:53:30

model fail predict correct.

1:53:33

I'm just trying to,

1:53:34

this is not the perfect syntax,

1:53:35

but I'm just trying to write it out,

1:53:36

just to show you.

1:53:37

This is how the flow will be.

1:53:38

So this is

1:53:40

to have a more strict metric.

1:53:42

And this

1:53:43

can't

1:53:43

many scenarios

1:53:43

are applicable

1:53:44

now.

1:53:46

Now, you

1:53:46

are fraud detection

1:53:47

in

1:53:47

even if you

1:53:49

have the slightest

1:53:51

of doubt

1:53:51

that the transaction

1:53:52

is fraud.

1:53:53

You have

1:53:53

pros

1:53:54

classified

1:53:54

to put

1:53:54

you.

1:53:55

You're

1:53:55

50%

1:53:56

weight

1:53:56

not

1:53:56

because

1:53:57

fraud is a big

1:53:58

deal.

1:53:59

If

1:53:59

if bank

1:54:00

bank

1:54:00

there's

1:54:00

if

1:54:01

this

1:54:02

transaction

1:54:02

fraud

1:54:03

so model

1:54:04

should ideally

1:54:04

predict

1:54:04

fraud.

1:54:06

Okay,

1:54:06

if I

1:54:07

if I,

1:54:07

this is

1:54:08

past fail

1:54:08

story

1:54:09

now if I

1:54:10

change the

1:54:11

same

1:54:11

story

1:54:11

for a

1:54:11

fraud

1:54:12

detection

1:54:12

in

1:54:12

that

1:54:14

case

1:54:15

threshold

1:54:16

has to be

1:54:16

extremely

1:54:16

very low

1:54:17

even

1:54:18

even

1:54:19

if

1:54:19

the model

1:54:22

has

1:54:22

predicted

1:54:22

a point

1:54:24

2%

1:54:25

probability

1:54:25

of fraud

1:54:25

you still

1:54:27

classify

1:54:27

that as a fraud

1:54:28

card

1:54:29

swipe

1:54:29

and the

1:54:30

model

1:54:30

has predicted

1:54:31

that based on

1:54:31

the

1:54:32

transaction

1:54:32

I think there's a

1:54:34

2% probability

1:54:35

of fraud

1:54:35

that is a very high probability

1:54:36

probability

1:54:37

you will not wait for that 50% thing, okay, got it.

1:54:41

So this is how based on the context,

1:54:42

based on your understanding of the domain,

1:54:45

your understanding,

1:54:48

your common sense,

1:54:48

say,

1:54:49

you have figured out of the right threshold.

1:54:52

Okay, I hope everybody's clear.

1:54:54

These are the concepts that we have here,

1:54:56

and I think

1:54:56

the code is the easiest part,

1:54:59

which is what I'm going to get into.

1:55:01

So this is all that we'll be,

1:55:02

we'll be seeing right now.

1:55:05

And just one thing,

1:55:06

one last thing I wanted to

1:55:07

clarify, just one last thing I wanted to clarify, when you're just one last thing I'm

1:55:11

to clarify, when you eventually see this in the code, you will see the code, you will see

1:55:15

the predic probe will typically give an output like this.

1:55:18

This, you'll

1:55:18

you'll output typically

1:55:19

this is

1:55:19

this way, we'll be seeing only the code from here.

1:55:23

Output you'll be typically

1:55:25

a

1:55:25

and whenever it comes this way, please remember, in Python, the default is this is always

1:55:30

this is always one.

1:55:31

This is always one.

1:55:32

This is always

1:55:32

before

1:55:33

when I was explaining Confucian matrix.

1:55:34

So always zero comes first, one comes later.

1:55:36

What's up negative plus, then positive plus.

1:55:38

Okay, please remember.

1:55:40

So, if predict proba gives this value,

1:55:43

this is the, okay, there is a 92% probability person passed.

1:55:47

But there's a 92% probability of fraud.

1:55:49

And if you use the predict function,

1:55:51

so predict is working on a 50% threshold.

1:55:53

So model has predicted past or problem.

1:55:56

You can just keep this at the back of your mind.

1:55:58

If you do predict proba, for a binary classification,

1:56:00

because today our discussion is focusing only on binary.

1:56:03

If it's multi-classes, then multiple answers will.

1:56:06

That is different.

1:56:06

I'm not getting to that today.

1:56:07

So today it is only binary.

1:56:09

If two classes, we'll have two values right now.

1:56:15

One, the probability of zero class, second, the probability of one class.

1:56:19

So that is how it looks like in context.

1:56:24

Okay.

1:56:26

Now, moving on, this is the use case that we will be doing right now.

1:56:30

It's a very interesting use case.

1:56:32

So all of you give it a glance.

1:56:34

We'll be seeing this right now.

1:56:36

This is the use case we will do.

1:56:40

Just give it a glance.

1:56:41

I think the general pipeline has been shared with you.

1:56:44

What exactly will be building?

1:56:45

And then we'll go to code may go and I'll show you the code how to do this.

1:56:48

Okay, we'll see that in the code.

1:56:51

Everybody give it a glance, please.

1:56:55

Just so that all of you know exactly what we are trying to solve here.

1:57:06

Thank you.

1:57:36

Thank you.

1:58:06

All right.

1:58:19

So this is the case that we are trying to solve that we are trying to solve guys that we are trying to solve guys.

1:58:36

So we are looking at the different features of a person's cancer cell sample, a cell sample.

1:58:45

So we have measured different different cell sample.

1:58:48

There are 30 features we have right now.

1:58:50

And based on that, this is the pre-processing pipeline we will do.

1:58:53

First, we'll scale kare.

1:58:55

Then we'll make model, then we'll make, then we'll make sure we'll see that.

1:59:00

Let's go to the notebook now.

1:59:01

Before that, this is the snippet I already discussed with you, Confucian matrix.

1:59:05

curve. We already saw this. And I hope everyone, everyone can relate to it, right?

1:59:11

So everyone is able to understand this. So this is the code for the Confucian matrix,

1:59:17

actual and predicted. Because Confucian matrix is always a plot between actual and predicted.

1:59:22

So when you're seeing this particular matrix, how do you, how do you understand this?

1:59:29

Remember, along the rows, we have the, along the rows, we have the, along the rows, we have the, uh, actuals.

1:59:39

Here we have actuals over along the rows, okay?

1:59:42

Yeah, your actuals will.

1:59:44

And along the columns, you have the predicted.

1:59:48

Yeah, your predicted over.

1:59:50

So, yeah, it's your 1.

1:59:52

Yeah, it's your 1. Okay.

1:59:53

So 01, 01, actual versus predicted comparison.

1:59:56

This is what we are trying to do over on, okay?

1:59:59

I hope everybody's aligned. So this is what it is 01. So this is how the story looks like.

2:0:05

So just to clarify, this is your true positive. This is your true negative. This is the correct

2:0:12

predictions the model is making. Okay. And this is your false positive because model predicted one

2:0:18

actually zero. Model predicted positive actually it is not. So false false alarm. And this is your

2:0:23

false negative. So this is this is false negative. Okay. So this is false negative. Okay. So this is. So this is

2:0:29

is how you, how you will do the confucian matrix in the code. Always remember,

2:0:33

the first zero is, then, then one will predicted column actual rows. Okay. Now moving on.

2:0:45

Now let's, now let's come to the actual implementation.

2:0:55

So this is what we are trying to do here. We are looking at the different,

2:0:59

we are looking at the different features of a person and we are trying to predict

2:1:09

whether the person is suffering from malignant cancer or the person is suffering from

2:1:15

benign cancer. That is what we are trying to do. And this is our implementation. All if you can

2:1:22

see. So this is our cancer data set. All if you can take a look at it. This is a very popular

2:1:29

set to you already, we already have it in SK learn. It's already available.

2:1:35

Okay. X. X. Y. Yeah. And train test plate. This is the general workflow. We have already seen that

2:1:44

before. And this is the pipeline. What is the benefit of the pipeline? We can add multiple pre-processing

2:1:50

step. A go. A go ahead to what each is. Dot fit, dot predict. Dot predict proba. There's nothing else.

2:1:56

But the only difference is we are able to use the pipeline.

2:1:59

First, we're scaling here.

2:2:01

Then, we are doing a pitch.

2:2:07

And finally, we are doing our score. If I run this, I'm getting 98% test accuracy.

2:2:13

So that is a very good sign. So we are able to get a model which is giving us an extremely high test accuracy.

2:2:19

So that is just what I wanted to show you.

2:2:23

You can, now, look at you how the model is doing. And this is how you can see the false negatives and

2:2:28

falls positive with respect to our data. Okay. So that's one way to look at it.

2:2:33

Now, the final exercise that I wanted to share with you is a more real world exercise. This is the easy

2:2:38

one. This is just to kind of show you from a quote perspective what we did. So subsep-prely we built

2:2:44

the model. We did dot fit. We are able to do dot predict. You can also do dot predict proba. Same

2:2:49

story, dot predict proba. The next exercise is on predict card detection. This is a Kaggle exercise.

2:2:57

I will straight away share the Kaggle link with all of you. So before I start with the

2:3:03

discussion, everybody, please give it a read once. Go to this link on Kaggle, everybody, and please

2:3:09

give it a read. Here here first, you have data to say what kind of data is given to us. Okay. And this is

2:3:15

data from a real Taiwanese bank. Okay. Data of real customers, their credit history, their bill

2:3:22

statements, all this was collected from real customers from a period of April to September.

2:3:27

2005. The data is anonymized. Real data need. But the customer's name address

2:3:32

that's not. But the data is real. And this is the data that we are taking right now. Okay.

2:3:39

My expectation from you guys will be just go through the data set once. Try to feel comfortable.

2:3:45

What is the problem we are trying to solve? Take five minutes all of you. Read through the

2:3:49

dataset. Try to understand your data properly. It's the most important part of machine learning is to

2:3:55

understand your data.

2:3:57

for so much so much more important. So that is what I want to dedicate some time.

2:4:00

All of you please take some time to understand your data.

2:4:02

That's after, we go to code solution in.

2:4:05

The code, the set, the template is very simple.

2:4:07

Same dot, dot predict, dot predict, proba, but we will see some other aspects in this particular workflow.

2:4:14

Everybody give it a read in the meantime.

2:4:27

Thank you.

2:4:57

Thank you.

2:5:27

Thank you.

2:5:57

Thank you.

2:6:27

Thank you.

2:6:57

Thank you.

2:7:27

Thank you.

2:7:57

Thank you

2:8:27

Thank you

2:8:57

Thank you

2:9:27

Thank you

2:9:57

Thank you

2:10:27

Thank you

2:10:34

You can, I hope everybody has managed to give it a read.

2:10:52

Very interesting data set.

2:10:54

We are looking at the different features of a person.

2:10:59

Every row stands for a person.

2:11:00

You can you have here on a data sample.

2:11:05

What I have actually done is in your drive, I've also uploaded the,

2:11:09

I've also gone ahead and uploaded the actual data set for you.

2:11:12

If you take a look at it, this is the UCI credit card data set.

2:11:15

I've made you download and you upload up to upload here.

2:11:18

So every row stands for a customer.

2:11:21

This is the historical data of the customers that you're able to see right now.

2:11:26

Each and every row stands for a customer.

2:11:29

And you're able to.

2:11:30

to see for every customer you're tracking, what is their credit limit?

2:11:33

What is the limit balance?

2:11:35

What is the sex of the customer, male, female, education level, what is the age of the customer?

2:11:44

Payment status, I mean, if the customer, let's say, delayed in certain months to pay,

2:11:50

his payment status here.

2:11:52

And this is actually how banks collect data.

2:11:55

Usually, two years, three years, to data, there's data right?

2:11:59

From a, from a data perspective.

2:12:00

are only looking at last six months data.

2:12:03

But banks will typically consider, at least up to last two years data to make decisions.

2:12:10

So here here all the 12 months or 24 months' status right?

2:12:15

This is the payment status?

2:12:17

This is the bill amount.

2:12:18

So bill amount one, bill amount two, bill amount three, have to bill amount six.

2:12:22

Because remember, April to September data, I think bill amount one corresponds to, let's see,

2:12:28

bill amount one, I think corresponds to September.

2:12:30

So September's bill amount is.

2:12:34

And April, the bill amount, it's, April, May, June, July, August, September.

2:12:40

And I'm going to say, sir, bill amount's from what can't tell you?

2:12:42

Bill amount's a pattern, I know.

2:12:44

Patterns, you know.

2:12:47

But now that's why why, that person was having,

2:12:50

I mean, the credit card in a bill, it was, last three months,

2:12:52

that the month, not went, that the one has used not.

2:12:55

Other interesting things, like,

2:12:57

uh, look at this one.

2:13:00

I'm just trying to find some high spending.

2:13:05

I'm just trying to find some numbers.

2:13:08

Look at this one, for example.

2:13:11

Here.

2:13:13

Achalachs, you have been both spent for the year.

2:13:16

Isn't, you know, this your April.

2:13:18

Okay.

2:13:19

Acha'clock in September, you've got this, so that is also a concern.

2:13:24

Right?

2:13:25

So that is something that the banks will look at, bill amount.

2:13:28

And finally, the payment amount.

2:13:30

Bill amount for the credit card, the bill generated.

2:13:33

I mean, at the end of the month, the end of the statement period,

2:13:35

credit card bill gets generated.

2:13:37

That's after you, how did pay?

2:13:39

That's how much thing is.

2:13:41

Some customers, what they will do?

2:13:42

Your credit card in $10,000 dollar-ca due, but you don't pay.

2:13:47

You're only minimum amount pay for you.

2:13:49

Just to wave out the fees and all that, you're only paying the minimum amount.

2:13:53

Baki, you're carrying forward to the next one.

2:13:56

That is not a good sign.

2:13:57

That is not a healthy sign.

2:13:58

So the banks will want to,

2:14:00

the pattern, that's the September in the bill, you know,

2:14:04

you've paid, how do you?

2:14:05

Paysa actually not that is a problem.

2:14:08

So the bank is looking at those kinds of factors.

2:14:11

Rather you have a customer, which has $1,000,000 in September

2:14:14

spent was, $21,000 last month,

2:14:16

but actually the customer actually paid also.

2:14:18

He said, he's got a more payed, yeah.

2:14:21

So this is why the payment amount is also important.

2:14:25

And based on that, finally, the last column is the default payment next month.

2:14:28

This is what we are trying to predict.

2:14:30

This is a very real-world use case.

2:14:33

Banks are also doing it nowadays.

2:14:34

Credit card companies are looking at your historical transaction data,

2:14:39

your last six months data based on how you're using the card,

2:14:42

how you're using the card, how it's how much amount, how much statement, how much

2:14:45

came up and based on that, we are trying to predict whether you will default,

2:14:49

whether you will not default.

2:14:52

It can be sometimes funny to think of.

2:14:55

It's not that it's not that customer in a card in a barred amount swipe up.

2:14:59

So banks want to prevent against that.

2:15:03

Like I'm telling you, April to September, your data is.

2:15:06

Okay?

2:15:07

You have April to September data.

2:15:09

So you are able to see the April to September data.

2:15:14

And

2:15:15

April to August, you've never spent

2:15:20

not September, you've spent a lot of money on September.

2:15:24

So that is the concern for the bank.

2:15:26

So the bank wants to look at your historical data to predict that will you

2:15:29

default, do you not default?

2:15:30

This is historical data.

2:15:31

This we have already available.

2:15:34

This customers, we've already

2:15:35

know, these people defaulted, these people did not default.

2:15:38

We want to build a machine learning model to study from this pattern.

2:15:42

They already have gone to past, we have.

2:15:44

We've got.

2:15:45

If a person defaulted, then, you know,

2:15:47

that's data, April to September data basis

2:15:50

on October in October, the man has what did?

2:15:52

We will know that.

2:15:53

That our historical data.

2:15:54

We will train the model based on that.

2:15:58

And as if any new customer,

2:15:59

they say you start using the credit card bank will real time predict every month the bank

2:16:04

will real time predict will the person default will the person default will the person default.

2:16:09

That's the real world use case we are discussing every every major card company is doing that.

2:16:14

Visa, MasterCard, MX, something for any credit card company and they are doing this.

2:16:18

Now let's come back to the solution.

2:16:22

So the understanding of the problem is very important.

2:16:24

You see how much time we spend on the understanding of the problem.

2:16:26

So real world may go up as a Kaggle, later system.

2:16:29

you need to understand the problem okay so this is what we are trying to do the goal is to

2:16:34

build a model to predict whether a customer will default on their credit card payment next month

2:16:37

that is what we are basically trying to do okay so all of you can just uh give it a glance what is the

2:16:44

blueprint what are we really trying to do everybody your tasks what is it that we are trying to achieve

2:16:49

same this but just give it a glance all of you take a minute

2:16:59

Thank you.

2:17:29

okay so you can you can actually see this one all of you will take the data

2:17:39

we'll separate the x we'll separate the y why is nothing but the default payment next month

2:17:43

train test fit karengi pipeline banay or model

2:17:46

you will see the accuracy and we will also build a confusion matrix okay so first things

2:17:52

first let me download the dataset this is already in your google drive so let me download the data

2:17:56

data. So I'm going to download that and I will put it on Collab. So I will upload the data

2:18:05

in Collab. Collab make upload the option. So whenever you want to upload this in your working

2:18:11

directory, this is the way how you can upload your data. We have seen this before. This is the way

2:18:16

how we are uploading the data. Next, what I will do, I will use read underscore CSV. I will load this into a

2:18:24

a data frame called demo. And this is how my data looks like. Or some redundant columns

2:18:28

dropped here, okay? This is my final data set. Now look at whatever data we worked on, this is my final

2:18:34

data set. Limit balance, age, pay zero, pay one, pay two. And finally, we are trying to predict the default

2:18:40

status. Okay, all if you're able to see this. Now, moving on, we are segregating the x and segregating the

2:18:47

Y. So we are dropping that output column. Everything else is part of my X and the output column. And the output column is part of my

2:18:52

while train test split. This is our pipeline. Today's focus is only logistic. So

2:18:58

first we're scaling. Why scaling? Because if you see, this is a very good use case for scaling

2:19:03

because the data is in different scales. You pay zero, age, look. Age is in a very different scale.

2:19:09

Limit balance for credit limit. If you're in India in any credit card, usually you're

2:19:13

usually you're 1,000, 5,000, 75,000, 1,000, 1,000, so the scale is very different.

2:19:19

And now, age is of a person maximum, it's, so it's, 100 to go to, 100 to, 10,000,000,

2:19:22

go right? So the scales are very different. Payment status. This is 0, 1, 2, 3,

2:19:28

it's the values. You can go. You can't see. It's already defined here. So the values

2:19:33

be either minus 1, 1, 1, 8, 9, maximum 9, values are. You. Now, you can see. The scales are very

2:19:40

different. And finally, bill amount or payment amounts are very high. So very, very important

2:19:46

use case for scaling. You should always scale your data in this number of scenarios. Then we are

2:19:51

building the model.

2:19:52

Baki, same to same here, dot fit, dot score. And we can see that the model is giving

2:19:57

us 80.9% accuracy. The baseline model. Behind the scenes, what did we do? We were able to find

2:20:06

a line or plane or surface that best separated the classes. Classes, what is the default, not default,

2:20:13

which are two classes. Okay. Now, very important. Is it a conversation I wanted to have with you.

2:20:19

If you look at the accuracy of the model, our model is the model.

2:20:22

80.9% accurate. If you look at the accuracy of the model,

2:20:27

ah, I mean, maybe it's a, it's a decent model, whatever. But how do you decide

2:20:35

whether it's a good model? Is accuracy the only indicator? No, it's not. Accuracy is only a part of

2:20:40

an indicator. So this is what I was mentioning before. So accuracy will not give you the entire

2:20:45

picture in terms of what is really happening. Accuracy will give you part of the picture. But accuracy

2:20:50

will not give you the complete picture in terms of what is.

2:20:52

really happening. So yes, the model on an average is giving you decent results.

2:20:58

But to get the complete picture of how the model is really doing, you will have to go back, get

2:21:04

the predicted values and find out the condition matrix. That is what we will do. That is what I will

2:21:09

show you. Rest, whatever we talked about conceptually, you can do predict proba. Prebara, we already

2:21:16

discussed here. First, the class 0 will come, then the class 1 will come. And in the context of our problem,

2:21:22

what is zero? One, what is default. This is what you are trying to predict.

2:21:28

Whatever we are trying to predict is the one plus and whatever, and the other one is the

2:21:32

zero plus. So these are the probability of defaults. So predict probability will give you the

2:21:40

probabilities. Next time we have a new customer. This customer has a 22% probability of default.

2:21:45

They are all less than 50. Tabdeco is zero z. But in a real world scenario,

2:21:51

I told you another thing, like threshold update.

2:21:56

In a real world scenario, you should never go with a 50% threshold.

2:22:02

Because even a 22% probability of default is very high, extremely high.

2:22:06

I mean, if you look at a real world banking context, if you're seeing a transaction, a customer,

2:22:11

and the model says, why, there is a 22% chance the customer might default next one,

2:22:16

what will you do? You immediately block the customer's card.

2:22:19

So 22% chance is a very high probability.

2:22:21

of default. The reason why the model predicted zero here is because it is working based

2:22:25

on a 50% pressure. Remember, so what we should do in practice in a real world scenario,

2:22:30

where we actually actually, we actually take the predict proba and we write our own

2:22:36

fail statement. So we will use our own thresholds. And usually banking context, maybe we'll set a threshold

2:22:41

close to 1%. Even if you're 1% likely to be a defaulter, I will still classify as a defaulter.

2:22:48

1% is also considered to be very high because we don't want to miss any

2:22:51

defaulters. No way. I don't want to miss any defaulters. Even if there is a slimy test

2:22:56

of possibility you might default, I will put you on the default category. I don't want to take

2:23:00

any risk. Otherwise, it's a financial loss for the bank. Default, what kind of? The bank

2:23:04

is the customer may, say, $2,000 swive and swiped and you're going to, credit card.

2:23:10

What, credit card? What, you're swiped. And then payment time comes, so you run away. And

2:23:16

that recovery, do it, do. So, you'll run away. But bank has lost money. Right. Bank has to write.

2:23:21

it of bank. So it's a financial loss for the bank. Okay, I got it. Everyone's

2:23:27

understanding. So try to always connect with the business context. That's the thing I always try to

2:23:33

encourage you in all these sessions. Always try to, so topics rea but always try to connect with the

2:23:38

real world, business context. How are things really happening? Okay. So that is the way how you should

2:23:43

always approach it. And things become very much fun once you learn that way. Okay. So dot fit,

2:23:50

dot predict to what? Dot predict. And then we can see the Confucian matrix.

2:23:54

And you can see the Confucian matrix right now. Look at this. This is what I wanted to share with you.

2:23:58

Look at this. The moment you look at the confusion matrix, you are able to see, you are able to see that this model is having 1.26 false negatives.

2:24:11

This model is giving you 1.026 false negatives. Can you see? So that means the accuracy of the model was 80%.

2:24:18

Accuracy 80% a, but the model is giving you 1.026 false negatives.

2:24:24

So although this is giving you only part of the picture, but once you see this in detail,

2:24:28

you are seeing there are so many false negatives. I think there are so many such cases where

2:24:32

model predicted you will not default, but actually you did. So this is a very, very poor quality model.

2:24:38

Okay, so this is the reason why Confucian matrix is very important. This is giving you a more granular

2:24:42

view in terms of what is really going on. So there are 1026 such cases where model

2:24:48

predicted zero, but actually it is one.

2:24:52

Everyone's aligned. And finally, the last part, and this is again something that's actually

2:24:56

part of a next week's topic. Finally, all along today, we have seen logistic. Just to complete the

2:25:04

story, what we have been discussing before as well, machine learning ma'am, kartea kya. Now, now we have

2:25:09

seen that logistics say it's not going to. We scale the data, we use the logistic model, but we are not

2:25:15

able to get a very good quality model. Accuracy is only coming in.

2:25:18

or false negative is very high. So what can we do? Can we try a different algorithm?

2:25:23

And that is exactly what I'm trying to do right now. I am trying to use a more powerful algorithm

2:25:28

called gradient boosting classifier. What is it you don't have to worry right now? That is not part

2:25:32

of my discussion for today. Next week we will see. So we are using a new algorithm called gradient

2:25:37

boosting classifier. And I will show you in code. It is very simple to implement it. So the thing

2:25:44

remains the same. You just import gradient boosting classifier from a different.

2:25:48

package. The pipeline same to same.

2:25:50

First, you have data scale

2:25:52

and then, now, now, now, now, this one of using logistic,

2:25:56

you're using gradient boosting for classification. It's a more powerful

2:25:59

model for classification. And the moment you do that, the moment you

2:26:02

build your pipeline, you are able to see accuracy has marginally

2:26:05

improved, but most importantly, your false negative

2:26:08

has marginally reduced.

2:26:10

A quite reduced for. 20% reduced your fault's negative.

2:26:12

And this is the iterative way how you do machine learning in the real world.

2:26:16

So real world, we have as a way.

2:26:18

We take a data set, we build a baseline model.

2:26:20

We start what kind of sports we are getting.

2:26:23

We see that. And then we try different, different iterations and we try to build a better and better

2:26:28

quality model. That's the way how we go about it.

2:26:31

We take a data set, we build a model, and then we try to build a better quality model.

2:26:36

So the moment I take gradient boosting and I try to build another model, you are able to see

2:26:41

I'm getting very good results.

2:26:43

So we can say that this is a better model than what we have before.

2:26:48

So this is the, this is the final thing that I wanted to share with you.

2:26:52

Okay.

2:26:54

Everybody's with me, clear, all of you?

2:26:56

Please let me know.

2:26:58

So we saw some more case studies today, but I think from a topic perspective, it was light.

2:27:03

So primarily there were three core ideas that we looked at in the session today.

2:27:09

So three core ideas as to kind of come to the key takeaways.

2:27:12

So, you know, these were the main takeaways from the session today.

2:27:15

We understood classification.

2:27:17

We understood.

2:27:18

So these are the broad ideas.

2:27:20

Like so what is classification?

2:27:22

What is binary? What is logstick?

2:27:24

Sygmoid. He intuitively. What is sigmoid?

2:27:27

He's zero to one.

2:27:29

Decision threshold.

2:27:30

You get threshold, how to adjust the threshold.

2:27:32

We saw that confusion matrix.

2:27:34

The recap confusion matrix, false negative, false positive, how to decide which one is important.

2:27:40

And then finally the standard pipeline of dot pit, dot predict, dot predict robot, these are the pieces.

2:27:46

Okay.

2:27:46

So comparatively, comparatively,

2:27:47

I think today we saw more case studies and two very interesting case studies.

2:27:53

We saw the breast cancer one and also some of the Kaggle case studies.

2:27:56

What I've also done in my notebook is I've also given you some other additional exercises, which

2:28:00

I really encourage people to go through.

2:28:04

Okay, so if you see in my notebook, I've given you a few of these use cases here.

2:28:09

So I've discussed this generally in the class, but if you see, these are some real data sets

2:28:13

where these things have been addressed.

2:28:15

So this credit card, real data is.

2:28:17

Predict transaction, fraud detection, like we have example I've talked about a couple of times,

2:28:23

but this is the ideal data set where they've taken data from European card holders and they are trying to predict whether the transaction is a fraud or not.

2:28:31

So same ideas you can use as we discussed in the session today.

2:28:34

This is another very interesting use case where we are trying to predict whether a customer will leave the network or stay with the network.

2:28:41

It is called customer churn. Churn, what you're just saying you're with Reliance Geo today.

2:28:45

And the same thing we discussed in the context of employee attrition.

2:28:53

Employee attrition, what I mean, employee, churn, meant love, employee, short and justra company going.

2:28:56

Customer churn, means, customer, short, and justra brand may go.

2:29:00

Idea is the same.

2:29:01

This is a very interesting machine-man in use case.

2:29:03

HRs can use it, companies can use it.

2:29:06

Because the cost of acquiring a customer is very high.

2:29:09

That customer to retain care, a discount do, 10% discount do,

2:29:12

new customer retainer, retain caro, that is still cheaper.

2:29:15

But to onboard a new customer is probably more expensive.

2:29:19

The same story applies in the HR domain also.

2:29:22

It's fine to retain the employees.

2:29:24

So bonus, it's just going to stay back in the company.

2:29:27

But to go through that entire recruitment life cycle, hire a person, do multiple rounds of interview,

2:29:33

best fit, evaluate for O.

2:29:34

So that is more possible.

2:29:36

So sometimes it's better we say to retain the person.

2:29:39

But how can HR use machine learning to predict what is the probability a person might leave?

2:29:45

And what is the probability our customer might churn?

2:29:48

Great use case.

2:29:48

And these are all real data sets I've shared with you.

2:29:50

So I encourage you, and this is exactly how the learning should happen.

2:29:54

So you come out of the sessions, go to some of these real-case studies,

2:29:58

and see how things are really done.

2:30:00

These are easy data sets.

2:30:01

If you see the data set, not very difficult, them.

2:30:03

Now look, customer ID, gender, partner, and you're simply trying

2:30:07

to predict whether the customer will chair or not churn.

2:30:10

Same tabular format where X low, Y, more even all, okay?

2:30:14

Hard disease.

2:30:15

prediction, something very similar to the cancer prediction we take today.

2:30:17

And finally, this is a bank marketing deficit.

2:30:20

These are some very nice five, very real world Kaggle case studies on classification

2:30:25

to help you connect the dots with respect to what we discussed in the class today.

2:30:29

You get something for your additional reference.

2:30:33

Okay, guys, I'm going to pause here for any questions you have at this point in time.

2:30:38

Any questions?

2:30:39

All of you followed?

2:30:40

Everyone understood the topics.

2:30:42

You want to ask me any questions right now?

2:30:45

Okay, thank you, thank you, Buma.

2:30:49

Udkar, yeah.

2:30:50

So others, others are all good.

2:30:52

Please let me know.

2:30:54

Clear is all, all concepts are clear.

2:31:01

All concepts are clear.

2:31:04

The walkthrough was clear.

2:31:06

Everything is all good, good to go.

2:31:08

Yeah.

2:31:09

I'm just going to pause for a minute here.

2:31:12

Once all of you confirm, we'll proceed.

2:31:14

we'll proceed. Okay. Thank you, Anjali. Okay, thank you, Herprits.

2:31:26

Others, let me know, guys. Thank you, Gurtig.

2:31:35

All right. So if there are no other, I take this time, yeah, yeah, sure, sure,

2:31:43

Sure, Koppel. I think you can, yeah, people are mostly clear.

2:31:47

Yeah, I was just trying to, you know, check if anybody have any questions.

2:31:49

Yeah.

2:31:50

So we'll just give it maybe 10 more, 30 more seconds and then I'll pass it over to you. Yeah, sure.

2:32:01

Meanwhile, I'm sharing the feedback on. They might like, like, fill up this.

2:32:08

Absolutely, yeah. Please take some time to fill up your feedbacks. In the meantime,

2:32:11

if you have any questions, you can ask me. And after this, we'll be.

2:32:13

we'll get to the, uh, the meter. I suppose the mantimeter should be fairly simple today.

2:32:20

So yeah. Okay. So polls are mine guys. Please fill it up. It was really an informative.

2:32:37

And after filling the phone, please fill it up. Opel, I think you're

2:32:43

voice is disconnecting, but it's going on and off. Yeah.

2:32:53

I think it will be better now.

2:32:55

Yeah, it's better. It's fine. Yes.

2:32:58

So great. So thank you so much, guys. I will take your leave at this point in time. A good night.

2:33:03

All the waste for the Menti meter. Yeah. Thank you. And over to you, Koppel.

2:33:07

Come here on this. Thank you so much. Okay. Sure. Yeah. Yeah.

2:33:13

So I'm sharing my screen.

2:33:43

I'm just pasting this code in the chat as well.

2:34:13

Okay. Hurry up guys. I can see only seven participants have joined right now.

2:34:43

All right. So let's get started.

2:34:54

So here is your first question.

2:35:05

Logistic regression is mainly for and the options.

2:35:10

And the options are Image editing, classification, data, storage, storage, storage, storage, or animation.

2:35:24

And the correct option is classification. Let's look at the scoreboard.

2:35:54

Which problem is an example of classification and the options are predicting house price, predicting temperature, predicting spam or not spam, or predicting salary.

2:36:04

And the correct option is predicting spam or not a spam.

2:36:20

Regression task.

2:36:24

Let's look at the scoreboard now. Buckle up for the third question.

2:36:39

In binary classification, how many classes are there and the options are? One, three, infinite, or two.

2:36:54

And the correct option is two. In binary classification, we have two classes.

2:37:09

Let's have a quick look at the leaderboard.

2:37:24

Moving on to the fourth question.

2:37:30

The sigma function converts values into, and the options are negative numbers, probabilities between 0 and 1,

2:37:38

large integers or text labels.

2:37:54

And the correct option is, probability is between 0 and 1.

2:37:59

Let's have a quick look on the leaderboard.

2:38:08

Moving on to the last question for the day.

2:38:15

Which option is true about regression and classification?

2:38:23

And the options are regression predicts continuous values, regression predicts categories, classification predicts continuous values or both are exactly the same.

2:38:53

predicts continuous values.

2:38:57

Let's have a look on the final scoreboard.

2:39:04

Congratulations, Sakura.

2:39:09

With that, let's stop here.