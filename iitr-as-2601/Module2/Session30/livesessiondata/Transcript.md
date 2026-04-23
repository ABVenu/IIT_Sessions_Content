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

8:56

Thank you

8:58

Thank you

9:05

Thank you.

9:06

Thank you.

9:08

You

9:09

I'm

9:10

I'm

9:12

you.

9:13

Thank you.

9:43

Thank you

9:45

Thank you

9:47

Thank you

9:49

Thank you

9:51

Thank you

9:53

Thank you

9:55

Thank

9:57

I

9:59

Thank you.

10:01

Thank you.

10:31

Thank you.

11:01

Thank you.

11:31

Hi, everybody, very good evening all of you.

12:01

Thank you.

12:31

Thank you.

13:01

So, folks, today, the agenda of today session is classification.

13:07

In the last session, we talked about the ideas and the concepts of regression.

13:15

And now we will get a little deeper into understanding the core concepts of classification, that is the that is what we'll be covering majorly in the session today.

13:31

I've already uploaded the session contents in the Google Drive, as always.

13:35

So you should be able to see all the session contents in your in your drive link.

13:45

And we'll start on with the flow as we go along.

13:52

Okay.

13:53

Yeah.

13:54

So we'll first do a little bit of a very basic recap.

14:01

And from there, we will be going on.

14:04

Yes, I can't shoot.

14:05

Yeah, we have, I think you are not there last plus.

14:08

Yeah, yeah.

14:08

So we have talked about that briefly.

14:12

RMAC and MAC are kind of error metrics, basically.

14:14

So when we are building models, it is not entirely required.

14:18

Just like we discussed, you know, like if you have a model that is 90% accurate or if a model has 90% R2, it is equivalent to having 10% error.

14:26

So they are mostly used for interpretation from an interpretation perspective.

14:31

They are not exactly required from a model building perspective.

14:34

Okay.

14:35

So next time you have to interpret the results they are useful.

14:47

All right.

14:48

So now we'll be getting into classification.

14:50

And everybody, just to summarize the core idea with respect to what classification is,

14:55

everybody remembers the very first machine learning session that we did and we talked.

15:00

and we talked about, you know, what is, what is ML, what is supervised learning,

15:05

what is regression, what is classification.

15:07

So regression is where we are trying to predict a numerical output.

15:11

The output that we are trying to predict is a number.

15:13

For example, the exercises we did in the previous sessions, we were trying to predict the housing

15:18

price, if you remember, California housing.

15:20

Then we looked at, we tried to predict what are the advertising sales, what will be the sales

15:25

of the company.

15:27

These were all examples of regression problems we did.

15:30

Okay. So we are trying to predict an output that is a number.

15:34

So the output is any continuous variable.

15:37

And the most important evaluation method is R squared. R squared is how we evaluated.

15:41

R squared is like an accuracy metric.

15:44

Coming to classification, we are trying to predict a categorical output, an output that is a category.

15:51

So these are things like use cases of classification problems would be,

15:56

you look at the transaction and you try to predict whether the transaction is,

16:00

genuine or fraud. I'm sure everybody has encountered this use case.

16:08

You swipe your credit card. You go to some outlet, some retail outlet and you swipe your credit card

16:14

and real time you get a message from the bank which says that sorry, the transaction got

16:19

declined. And you might be getting a call real time from the bank and, you know, they are trying

16:23

to authenticate the transaction real time. So that is a very good example of a classification problem.

16:29

So based on the first.

16:30

features of the transaction, you are trying to predict whether the transaction is genuine

16:35

or the transaction is fraudulent. That is the specific problem that we are trying to solve. So I repeat

16:40

again, based on the features of the transaction, we are effectively trying to estimate whether the

16:44

transaction is genuine or whether the transaction is fraudulent. So that is the particular problem

16:50

that we are trying to solve here. So output is either yes or no. Another example of classification

16:57

would be what are some other exercises of classification disease detection you look at

17:03

the features of a person and you try to predict whether the person is diabetic or not so the

17:09

output will be either yes or no in fact we will solve a similar case study in the class today

17:15

yeah pass and fail that is in fact the case study for today we can look at the students uh

17:20

data and based on the student's data uh you guys we can predict whether the student will pass or the student

17:25

will fail so the output is either yes or no pass or fail diabetes or not diabetes like that it's

17:31

not a number that we are trying to predict we talked about the loan example like there are many

17:37

applications in india which you know where you can just give your pan number and based on your pan number

17:42

they will effectively decide whether you're eligible for the loan or not right so that is also

17:49

a very good example of a classification problem so we are trying to predict is it loan yes or is it

17:53

loan no and very good absolutely spam or not spam is a great example we have seen

17:59

that example also before in the prior sessions where uh based on the different features of the email

18:03

you're looking at the different keywords of the email and based on the different keywords of the email

18:08

we are trying to predict is the mail spam or is the mail not spam

18:11

spam yes or spam no that's what we are trying to predict effectively so these are all examples

18:17

of what is referred to as classification problems right uh

18:23

head or tail like there has to be a there has to be a use case right so like what is the

18:29

use case around head or tail yeah so there has to be a business problem around it right so

18:34

see toss cannot be predicted right uh but look i i think you're talking about from that perspective

18:38

if you're saying that okay we will look at historical data and try to predict the toss result yeah

18:43

you can maybe think about it but uh that's not a that's not a real use case because i'll tell you no

18:49

matter what you predict at the end of the day uh like it's

18:53

is just a law of large numbers and mathematics every time you go to a coin toss

18:57

it is still a 50% probability of head and 50% probability of pain uh machine learning and predictive

19:02

analytics will not work in that particular problem because the results of a coin

19:06

cost are actually not impacted by anything results of our coin toss is completely probabilistic

19:14

very good very good very good use case by vinica defective or not defective very good very good

19:18

in fact that is uh that is something that that we are doing a lot in the quality

19:23

testing if you look at quality testing quality assessment is a great use case where we are

19:27

doing exactly what you're saying so how do we look at a particular you know elements that is getting

19:35

manufactured an object that is getting manufactured in the factory line and how do we use machine learning

19:40

to identify whether the product is defective or not and if you go back to the you know go back

19:47

to a period of time this is the process we have been doing majorly using uh rule-based techniques we have been

19:52

using rule-based techniques and a lot of other uh approaches we were using for solving

19:58

this problem today we are doing this using you know using machine learning how do we go back and

20:02

look at the you know different features of the of the of the product whatever product is getting

20:08

manufactured through the assembly line how do we go back and look at the different features of the product

20:12

and based on that how do we predict whether that product is defective or not defective

20:16

that is the specific problem that we are trying to solve so based on the features of the product

20:20

we are trying to predict defective or not defective good

20:22

very good use case it's not not as if every every imagine a product can be anything it

20:27

can be a coca-cola bottle also it can be something as simple as a coca-cola bottle also

20:32

there's a bottling plant where the the the cocoa is manufactured your rifa you're

20:37

filling it up you're you're bottling it you're bottling it you're sealing it that's the

20:41

that's the final packaged product you look at a complete car assembly plant like

20:47

every single aspect of the car is getting assembled there

20:52

how do you ensure that whatever final car is getting assembled or the final

20:57

cocoa bottle or the coca-cola can that is exactly as for the specifications what you expect it's an

21:03

extremely difficult problem have you have you wondered about it that when the uh when we see all

21:09

those marketing labels and they say that hey like this is a 500 millimeter of coke is present

21:15

have you ever wondered is it exactly 500 ml think about it have you ever wondered whether the

21:21

the coke is exactly 500 mm no i mean it's not possible it's not humanly possible to

21:26

measure every single bottle but have you ever wondered when you look at a medicine

21:32

medicines are also manufactured by machines today if you look at a machine

21:35

medicine there are so many different compositions of a medicine right like let's say for example

21:42

it contains 20 gram of sodium ascorbate there's a particular medicine

21:46

ingredients may both are a ingredients and have you ever wondered five m g hey two m g hey yes

21:51

who is measuring that the final packaged tablet that is getting

21:55

manufactured right into the strip you think somebody's actually

21:59

opening that strip and measuring the tablet no it's an extremely difficult

22:03

problem and that is exactly where machine learning helps i wanted to take a

22:07

moment to talk about it because this is a very real use case

22:09

front detection to abhikar we talked about it already yeah exactly so i hope everyone's

22:14

getting a idea about what classification is we've talked enough about it already in the

22:18

prior sessions already and today we'll get into some

22:21

methods how to do it and the best part the best part is the best part the best part is

22:25

the best part the best part is that the workflow will be exactly the same as regression

22:29

so today it will give us more time to get into a lot of hands-on and practicals we will do that

22:33

we'll do a lot of practicals today because whatever workflow we will do in classification

22:38

will be exactly the same take the whole data training data testing data you train the model on

22:45

train accuracy test accuracy overfitting under fitting

22:51

remember all those terminology we discussed everything remains the same the only new thing the only new

22:57

topic that we will basically cover is this thing called confusion matrix this is something we'll

23:03

come a little later in the class otherwise everything else that we do in classification

23:07

workflow same because it's the way x is y same is same is model model problem statement is not

23:15

not changing the ideas are very similar so that's the way how we are looking at it

23:21

yes ubrage unsupervised learning here in session in

23:25

session may i'm not taking up these questions so if you're having these general

23:28

questions i think arsita is there arsita can you also help the team also you can you can respond to

23:33

youbrage also so uh huh it is there it is uh at a basic level youbrage okay

23:40

the curriculum you can one post her

23:42

arsita is there in the class so she can take up all these you know queries uh you had another

23:47

question uh like how many weeks i think she can take up those questions so that way

23:51

we will not be distracted and as i clarified already this is not an ML course so ML

23:55

uml is basically at a level where we are trying to get you acquainted

24:01

what machine learning is that you

24:03

there are a lot of other things that's why we are not getting to the mathematical

24:08

details of these things so unsupervised we are touching upon it not into the depth of it right

24:12

now because the core we will still be genii that is what we are ultimately coming to

24:18

after a few more sessions we are straight away starting with generative AI

24:21

LLMs, Transformers, agentic AI, which is the most exciting part I'm sure everybody is waiting for.

24:26

Okay? Okay. Okay, let's go. Let's move on. Uh, so now let's come back and let's talk about a

24:43

let's talk about the decision pipeline, what we will be doing and I'm going to straight and

24:47

I'm going to straight and open up the notebook for all of you as well, family. Let me quickly. Let me

24:51

open up the notebook here. Is it a 21st April notebook? It's all shared with everybody.

24:57

You can absolutely refer to it parallelly on your screen. I think today, today you will find it a lot

25:05

more comfortable because you've already seen the workflow. So today I think it will be a lot more

25:10

comfortable for you. So let's see. So I will start with a very basic case study. And we'll

25:17

a bit complex case studies us going to because it gives us more time to get into some other

25:22

interesting things today. So we'll look at a lot more problem statements today and we will have some

25:27

general discussions on the problem statements, okay? Yeah. All right. So this is the specific

25:32

case study we'll take up today. Will the student pass or fail? That's what we will do. So I'm first

25:38

importing all the necessary libraries. Updak sacked your modules are all the standard modules,

25:43

Nampai Pandas. Pandas is used mainly for data manipulation working with tabular.

25:47

data. SK learn in all machine learning functionalities.

25:50

There's any algorithms, min-max scalar, accuracy, all of these are part of your

25:56

machine learning libraries. So all these are part of SK learn. Now, first question,

26:05

why linear regression fails for classification? So first,

26:08

first you have your question, sir, like, why can't we predict? Why can't we solve these

26:14

problems using linear regression? Okay, let's do one thing. Let's take one thing. Let's tell you.

26:17

a use case. Let's take a use case. Let me show the data to you first.

26:23

So let's say for a minute, this is your data set, okay? We have,

26:28

let me print the whole data,

26:30

all data, okay? Let's say we have the study hours, sleep hours, distractions,

26:36

and on the basis of that, you are trying to predict a result. That is your data set. So

26:41

your X, what is? We can model this into a typical machine learning problem. This

26:45

this is your x, and this is your x-y combination. You've already seen this before.

26:54

So all these three features, your input x, and this result of your output y

26:59

okay? Everybody is able to see. All these features are, you know, are your, are your x,

27:05

and this is basically your output y. So that's the way how we are able to look at it.

27:15

this is your x and there goes your output y that's the problem that we are trying to solve

27:22

this is your output why this is the output y that we uh that we have right now so based on the

27:28

x we are trying to predict the y just give me one second guys just give me one second please

27:45

Thank you.

28:15

Thank you.

28:45

Okay. So again, as we as I told you, we have the input X, and based on this, we are trying to predict the output Y. And the output Y, as you can see on the screen is basically a

29:07

kind of a number. It looks like a number. It looks like a number. It looks like a regression problem. You know,

29:12

on first glance, when you look at this, it feels like it's a regression problem.

29:15

If we are trying to predict a number, if you are trying to predict a numeric value.

29:19

So this number, it feels like it's a, you know, it feels like we are trying to predict a number,

29:23

but it's actually not a number. It is not like a numeric value that we are trying to predict.

29:29

So based on the features, we are trying to predict what is the output.

29:33

Output looks like a number, but it is actually not a number. It is actually not a number. This is not the

29:39

number that we are trying to predict. So now the question is, so, right?

29:45

if you think of it as a number, can we treat it like a number?

29:51

Why, we regression in this way can we do regression on it? Now, the idea is,

30:01

we can do it, right? We can regression can. But the problem with that approach will be,

30:06

if you do linear regression on this data, linear regression is the best fit line.

30:11

We've this thing last last in discussed. It's a best fit line.

30:15

And the model can predict any value on that line on a scale of minus to plus.

30:24

That cannot happen, right? In practice.

30:27

See, for example, we have this simplify. Let's say we have study hours or this is your result.

30:35

I'll try to simplify this for you.

30:37

Let's actually do this.

30:39

Okay, unless I show you, it won't be clear.

30:41

Let's do this. It will take hardly a minute.

30:43

This your x or your y is.

30:45

Okay? And you have trained to split here.

30:49

Exactly as what we've discussed, nothing is different.

30:52

All that I will do right now is I will do something called linear regression.

30:56

We have linear regression, right?

30:59

So all that I will, all that I will do right now is I will just go and do linear regression on this particular data.

31:08

I will just go and do linear regression on this particular data.

31:11

That we import here.

31:13

This is just to show you.

31:15

You have you to edit not to class in.

31:16

I'm just trying to show you this entire thing.

31:19

So if I were to do linear regression, we back-y-court change in here.

31:22

This is the beautiful thing about SK learn.

31:25

So when we use psychic learn, we, we this go back from this go back to change in.

31:30

So you can see this one in action.

31:33

We are getting a model.

31:34

63% train, 62% test.

31:36

That is not important.

31:39

Now the interesting part will be, so you.

31:41

Here here here, best fit line or best fit plane, whatever that is, right?

31:45

I'm not getting to that thing again, but you understand that's the best fit surface we are getting, linear surface.

31:51

Those stages are. First stages, we are building the model.

31:54

And second stage is, if I give you some new data, you can make predictions.

31:59

Now, the question is, the thing is that when you try to do model, your predict,

32:05

and when you try to, you know, do the prediction on the test data,

32:09

this is the interesting thing will.

32:11

do that, you know numbers look at.

32:15

So this predicted Y's values.

32:16

Now, we can be point 1-1-2.

32:18

See, our, our expectation is either 1 or 1 or 0-0-0.

32:21

Now, how 0-1-2?

32:23

How-1-2? How-0? How-1-2?

32:24

How-0-0? How-1-0? How-1-5? Can you believe it?

32:29

See, are you getting the intuition?

32:32

Again, forget about the math.

32:33

Match is over last week.

32:34

Forget about it.

32:35

I'm just trying to give you the intuition that,

32:39

how, which bias is a different thing?

32:40

That, I'm going.

32:41

I'm not getting to that here.

32:42

I'm just trying to give the intuition, that, why not it will?

32:45

you know, you can go.

32:46

You can code with nothing, no problem.

32:48

Because Python is seeing, that this is X, this Y, this is,

32:51

let's y' number, no problem.

32:53

Because Python is not intelligent.

32:54

Python is only going to do what you ask it to do.

32:57

So Python will actually build the model.

33:00

Linear regression takes the time.

33:02

But the final outputs will not make sense.

33:05

I'll give you the example, guys.

33:06

Here it is.

33:06

In front of you, this, look, minus point 0.05.

33:09

This is what is?

33:10

Can pass.

33:11

on fail value be minus 0.05.

33:14

It doesn't make sense, right?

33:15

Because it's a regression.

33:17

We've got it to

33:18

solve here.

33:20

So, output, what,

33:21

that's a continuous value

33:22

is.

33:24

But our problem statement

33:26

is, it's allowed

33:27

not.

33:28

You're all problems statements.

33:29

Defect, not defect.

33:31

Diabetes, not diabetes,

33:32

cancer, not cancer,

33:33

fraud, not fraud, not fraud,

33:34

spam, not spam.

33:35

We have that

33:36

either zero or one.

33:39

Either are the two values.

33:40

I cannot have anything in between.

33:41

So, nothing in between and my values cannot be less than zero, cannot be more than one.

33:49

There can't be zero or two or one over.

33:52

That is exactly my requirement right now.

33:55

Okay?

33:56

That's the use case.

33:58

Now, let's move on.

34:00

Let's continue on.

34:02

So now, what we will try to do, we'll try to go back and take the data.

34:08

So this is, this is what I actually explained here.

34:10

The model, this makes no sense.

34:13

You can't pass 1.73 times, right?

34:16

This not can't be a value.

34:19

We need a model that squeezes every prediction to be exactly between 0 and 1.

34:23

We need it.

34:24

Whatever predictions will, we just want two values.

34:27

Either 0 or 1 or 1.

34:29

And that is exactly where.

34:30

And this is only for mentioning in the class,

34:33

this is not the math we will not see.

34:35

This is exactly what logistic regression will do.

34:37

It's in the mathematical aspect called sigmoid function.

34:41

And that sigmoid function will do exactly that.

34:45

It will take those numbers.

34:46

It will take those numbers that we are creating.

34:49

Jovey numbers I'm create.

34:51

It will simply take those numeric values and that compresses to all.

34:55

Zero or one in between.

34:56

Just remember that at the back of your mind.

34:59

That is what logistic will do.

35:01

I will just show you the magic part here.

35:04

But us in under what is max.

35:06

It's a reference thing.

35:07

But you don't have to get into that.

35:09

Just remember the idea.

35:11

Linear regression, same.

35:13

Your values are going to be continuous.

35:16

This is not going to solve our problem.

35:18

So, what we're doing?

35:19

We'll logistic.

35:21

This is a classification algorithm.

35:24

If you go back to last week, last week we were sticking to linear regression or gradient boosting regressive.

35:29

They were regression algorithms.

35:32

Last week's what they were regression algorithms.

35:34

I mean, that we were able to solve regression problems.

35:36

When you have a classification problem, then you have this is all for it.

35:42

All that I changed is one line of code.

35:44

We've got to change in.

35:46

We have the train test split.

35:47

That's the X or Y.

35:49

X, your study hour, say, Y, your result.

35:51

Everything is same to same.

35:53

That's your model dot fit X train and Y train.

35:56

Same up the score.

35:58

I'll run the code.

36:00

That's your train or test accuracy.

36:02

Interpretation same to same.

36:04

Overfit, underfit, good fit.

36:05

We have seen all those pieces.

36:06

Right now, this seems like a good fit model.

36:09

Generally, good fit model.

36:10

But if you remember, we've discussed

36:11

the only way to interpret whether

36:14

something is truly overfit, underfeit or good fit is to evaluate it.

36:19

Is to evaluate subsequent iterations.

36:20

Now subsequent iterations evaluate for, that's the way to look at it.

36:25

Whether a model is overfit, whether a model is underfeit or good fit,

36:28

that of course, subsequent iteration from

36:30

that's the only way to look at a, you know, a kind of

36:34

look at it.

36:35

I hope everybody.

36:36

is aligned. Everybody is getting ourselves. Now,

36:41

uh, moving on guys, moving on.

36:48

So now, if I do model.

36:52

Now, the magic that logistic actually did.

36:56

When I use linear regression, what was all the values were in a different range.

37:01

It was continuous set of values that was getting.

37:04

This is what logistic has done.

37:05

Just remember.

37:06

So, what it is able to do, it is not giving as continuous values.

37:13

It is able to compress those values in a range either zero or one.

37:19

That is what logistic will behind these things do.

37:21

So obviously, we'll see how it. What are the other things around it we will see?

37:26

But I hope the core idea of ML is clear.

37:28

The core idea of machine learning, we discussed here.

37:31

Train test plate, take a data set, fit a model, find out the scores,

37:35

that thing, same to same.

37:36

Nothing changes you.

37:38

Age the process.

37:39

You're all the other algorithms try.

37:41

Other models, make, and compare it.

37:44

That is the same way how things basically work out.

37:47

So this is based on a very simple data set we will see and we will see some more concepts

37:50

around this.

37:51

And then we will go to at least two case studies we will do in the class today so that you get

37:55

a good amount of practice.

37:57

If you have concepts, comparatively come here.

37:58

So we want to take more time for practicals, which is actually what is more important.

38:02

So we want to do some more code in today's class.

38:06

Now, one thing I'd like, guys, regression for a different algorithms have.

38:15

Classification for a other algorithm.

38:17

Just keep that at the back of your mind.

38:19

And if you want to see, our focus area for now is only logistic regression.

38:27

Okay.

38:28

I'll you you give you one example so that you get a sense of it.

38:32

This we have our logistic we've done.

38:34

I'll just use a small comment right now.

38:36

say linear regression.

38:38

We have we used here.

38:41

Linear regression or one we've made gradient boosting regression.

38:49

These are the two things we discussed in the context of regression.

38:53

In the context of classification, our focus areas are now.

39:00

Logistic regression and

39:03

and.

39:06

boosting classifier. These are the two things that are relevant in the context of

39:10

classification. So we have logistic regression and gradient boosting

39:13

classifier. So

39:16

the regressor is the corresponding regression algorithms. Let me just go and

39:20

write another comment. These are all regression algorithms and there are

39:22

many more. Okay, or be regression algorithms for there are same to same

39:26

process and these are all classification algorithms.

39:33

So I know one confusing thing which people

39:36

usually tend to ask that if this classification

39:39

so we're here

39:40

regression kind of use you

39:42

are a mathematical aspect.

39:44

You don't think that is just how the name is.

39:48

And if you're trying to think a little deep

39:50

behind the scenes, the intuition here is that

39:53

the mathematics of logistic regression is based

39:56

to some extent on linear regression.

39:58

So the match, which is sort of regression's similar

40:00

that is best bit line, MC,

40:03

we're the same thing we're similarly

40:04

study, that we're just the term regression

40:06

but otherwise logistic regression

40:09

has nothing to do with regression.

40:11

This classification is important. So

40:12

this typically we're confused

40:14

beginners, so just keep this in the back of your mind.

40:16

Again, remember, guys, our objective is

40:18

problem solving. We want to be very comfortable

40:20

in implementing things. We have a problem

40:22

solve. Just problem solving

40:24

aspects of you. Just problem solving aspects

40:24

have, you just, you just, you just

40:25

problem solving aspects of you just. Now, all of

40:29

you are okay with this. Now,

40:31

a gradient posting

40:32

we're up. So,

40:34

logistic's how are? 93.8%

40:36

92.5%.

40:37

What can I do?

40:41

How's gradient boosting

40:42

can't? Well, just import the necessary package.

40:46

So package import is

40:47

first in the start

40:48

in the beginning. So we'll

40:51

a package import here.

40:52

This all you can help

40:53

can't. But again, you know, like

40:55

there's been many years I've been writing

40:58

these codes. So for me it is second nature.

41:00

but if you're doing it, honestly,

41:02

and I'm telling you myself that there

41:04

is no value in writing code.

41:05

Now the code we type are,

41:07

if you can it's

41:07

no value in writing code,

41:10

but it's okay.

41:11

So there is,

41:11

so writing the thing from scratch,

41:13

okay,

41:13

I mean,

41:13

it's a practice

41:14

you know,

41:16

but don't try to take

41:17

too much pressure on remembering syntax.

41:19

Okay, it's not a,

41:20

not a big thing.

41:22

Now, moving on,

41:23

I will use

41:24

gradient boosting classifier.

41:27

Now,

41:27

look,

41:27

code in which has changed

41:28

just changed the algorithm

41:30

and magic has happened.

41:31

100% accuracy

41:32

got so.

41:34

I need to tune some hyper parameters also.

41:36

So it's,

41:38

you can tune it and you can try to build a better quantity model.

41:41

This we have to iterate

41:42

and evaluate

41:42

and we have to see

41:44

where we are getting the best model.

41:46

You have to continue different,

41:47

different permutation combinations

41:49

and see where the model actually become better.

41:50

So a little improvement to

41:51

have been better.

41:52

You know,

41:53

we're talking about comparative improvement now.

41:56

We are all talking about comparative improvement.

41:58

I'm ultimately trying to build a model

42:00

which is comparatively better.

42:02

With a logistic model,

42:03

training was 903.

42:04

testing was 92.5.

42:06

Ultimately, what matters is testing accuracy.

42:09

Our mock question paper

42:10

how's results? That is ultimately what matters.

42:13

So train is 92.93.8 and testing is 92.5.

42:16

That is the accuracy that we are getting.

42:19

So training accuracy, it's not testing accuracy is 92.5.

42:22

That is what we are getting.

42:24

And after I use a gradient boosting classifier,

42:28

gradient boosting model, I'm getting a higher test accuracy.

42:31

Our test accuracy bergia here.

42:33

So we can.

42:34

say this is a better model than what we had before.

42:36

So concept is the same.

42:37

This is just I wanted to demonstrate to you

42:39

that what we've done last week in regression

42:41

in the same to same,

42:42

your classification.

42:44

So we'll what we'll say, this model is

42:46

comparatively more good fit than the previous model

42:48

because its test score is

42:49

a more. Test score is

42:51

it's more.

42:53

Okay?

42:55

This your notebook in

42:56

this I'm off the offer from share

42:58

don't worry, but

42:59

we've generally gradient

43:01

did all.

43:02

Only logistic is the focus area for today.

43:04

But this is just something I wanted to additionally show you.

43:07

Now, training the logistic regression model,

43:11

this we've already seen how we train the logistic regression model.

43:14

So we have already seen that.

43:15

I hope everybody is clear.

43:17

And now I wanted to share with you the next concept of

43:22

predict proba.

43:24

So so far, what are the key pieces that we have discussed?

43:27

We have fit discussed here.

43:30

Uh-huh.

43:30

Yubras, that is absolutely correct.

43:31

Second one has larger gap.

43:32

We have gap.

43:32

We don't measure not.

43:34

If you remember what I taught you,

43:36

we look at training improved

43:38

and testing been improved.

43:39

Both improved have.

43:40

So it is more good fit.

43:42

We're both improvement

43:43

based on the gap.

43:46

So training accuracy,

43:47

so training be better and testing

43:49

be better.

43:51

Always think from a human

43:52

amyerogy perspective.

43:53

You, you, up,

43:54

you, up, up,

43:54

you know, human being

43:55

as far as much.

43:56

If you prepared

43:57

if you've done,

43:58

so you have

43:59

your revision in,

44:00

so training score

44:01

more,

44:02

then what is,

44:03

then?

44:03

What is?

44:03

What is?

44:03

in the reading in

44:04

if you're a good

44:04

in revision

44:05

if you're a

44:05

good thing,

44:06

if I

44:07

asked you

44:07

something from

44:08

your

44:08

textbook,

44:08

you're

44:08

100%

44:09

answer

44:09

there's

44:09

a

44:09

good

44:10

nothing.

44:10

I'll

44:11

tell you

44:12

why it's

44:13

fine,

44:13

you

44:13

Raj.

44:13

because you

44:14

you're

44:14

you're

44:15

here to

44:15

here

44:17

you're very good.

44:18

Here you're

44:19

here you're very good.

44:20

you're

44:21

good.

44:22

So that is a

44:23

good thing, right?

44:24

So that is a good

44:25

we look at the improvement in both.

44:28

train

44:28

be

44:28

made and tests

44:28

be brought.

44:30

Actually,

44:30

if you're

44:31

if you're

44:31

if you're

44:31

things, if you're

44:33

people,

44:34

people, people,

44:34

say it's overfit

44:35

are,

44:35

that's wrong

44:36

actually.

44:37

We're not overfit

44:38

not

44:38

we're overfit.

44:38

The only criteria

44:40

all these

44:41

textbooks are keeping

44:42

100%

44:43

that is not how

44:44

actually, you know,

44:45

things in industry work.

44:47

Okay?

44:47

Overfitting is not a term.

44:49

That's what I taught you, right?

44:50

Yeah,

44:51

that's what I taught you, right?

44:51

Yeah,

44:51

I mean, look,

44:51

some,

44:52

where,

44:52

and I'm telling you,

44:54

you will see,

44:55

see this.

44:55

This books

44:56

in books

44:56

be

44:56

there's,

44:57

some YouTube

44:57

can give

44:58

that

44:58

be able to

44:58

say,

44:59

that is wrong

45:01

actually.

45:02

100% doesn't

45:03

just mean

45:03

overfitting.

45:04

And I'll

45:04

give me a

45:05

simple

45:05

analogy.

45:06

Your train

45:06

is 100

45:06

test 100

45:07

is?

45:07

Are you?

45:08

Are you

45:08

overfitting?

45:08

think about it.

45:10

How's,

45:11

so training

45:11

100% doesn't

45:12

mean

45:12

overfitting.

45:13

This is the

45:13

actually a mistake

45:14

that, you know,

45:14

people

45:15

usually make.

45:17

But, yeah, I'm

45:18

again

45:18

warning you,

45:19

that sometimes

45:19

sometimes

45:19

sometimes,

45:19

sometimes,

45:20

sometimes,

45:21

they sometimes,

45:23

they're not

45:24

it's a reality.

45:25

The company

45:25

interviewer

45:26

then it's not as if

45:28

they know

45:28

everything, right?

45:28

Sometimes they're

45:29

also making

45:29

mistakes.

45:30

And most of the

45:31

time they're making

45:31

mistakes.

45:32

Right?

45:32

There are also

45:33

people like

45:34

you and I only.

45:36

Okay.

45:37

So,

45:37

yeah,

45:37

so just be

45:39

careful when you're

45:39

answering it

45:40

to the interviewers

45:40

also at times, okay?

45:42

Yeah,

45:42

so this

45:43

good fit model

45:44

is, please remember.

45:45

And again, I repeat,

45:46

it is comparatively

45:47

more good fit

45:48

than the previous model.

45:49

So,

45:49

the first model

45:50

than comparatively

45:51

more good fit.

45:53

Right?

45:54

So,

45:54

what we've

45:55

what did

45:55

what did

45:55

we've got

45:56

did

45:56

we've got

45:57

we've got

45:57

predict

45:57

we're

45:58

we're

45:58

in a

45:59

new

45:59

thing

45:59

in classification

46:00

in

46:00

which

46:01

is

46:01

dot

46:01

predict

46:02

proba.

46:02

This is a

46:03

wonderful

46:03

thing.

46:05

So

46:05

Predic

46:05

proba is

46:06

what?

46:07

Let us

46:07

let us

46:08

understand

46:09

what is

46:09

this

46:09

predic proba.

46:12

Yes, yes, yes,

46:14

yes, yes, yes,

46:14

generally

46:15

it should

46:16

isn't it

46:19

logical.

46:19

Again, whenever

46:20

you're asking

46:20

this question

46:20

you're asking this question,

46:20

you're

46:21

should be,

46:23

you're

46:24

when you're preparing

46:24

something,

46:25

you're

46:26

preparing

46:26

so ideally your

46:28

test result

46:29

should be a little lower.

46:31

If if

46:31

high

46:31

it's a

46:32

different thing,

46:32

but usually

46:33

it's less

46:33

less

46:33

because your

46:35

performance on

46:36

your train is

46:37

usually better

46:38

than your test.

46:40

Because you

46:40

where you're

46:40

where you're

46:41

performance

46:42

always better

46:42

rather

46:43

compared to

46:44

a completely

46:45

unseen paper.

46:46

That's the logic

46:47

basic.

46:48

Again,

46:49

human analogy,

46:50

basic analogy based on

46:51

real world.

46:52

You're

46:52

you're just

46:53

examination

46:53

So what you're saying is right, generally, it's generally, it's, but then again, there are some stray cases where your test data can be different, that is okay.

47:10

And process time depends on data side.

47:12

How can be, no, that's a different question.

47:13

I'm not, see, big data is a different thing, actually, so that I'm not getting to that.

47:17

So big data is a different thing, but again, compute hardware is a different piece, absolutely.

47:22

I just wanted to clarify.

47:23

Definitely.

47:23

a big data, there are different ways to do it.

47:26

And you can think, I mean, like, what happens is, if you know PY Spark and all are there,

47:30

there are different frameworks are available.

47:32

But big data, if you're talking about Hadoop and all, distributed processing.

47:37

So we have other frameworks for that.

47:39

Psychic Learn is not the best framework for distributed processing.

47:41

So, clearly, we have things like PY Spark,

47:44

SPARC, MLLIB is a library.

47:45

You're all that different things, totally apart from the course.

47:49

But I just wanted to answer your question, okay?

47:50

Okay, okay. So let's move on.

47:56

We have taken the data, we have built the model, we have built the model, we've made model fit

47:59

and now we want to go back and do the prediction.

48:02

We want to do the dot predict.

48:06

This is our predicted probability of values.

48:08

Oh, sorry, we have gradient boosting here. That's the reason.

48:12

So let me go back and get back to logistic.

48:15

Go back to where we work.

48:16

Here there a lot of things we have tried to.

48:19

We'll go back to logistic.

48:20

and we'll use the logistic regression model for the problem.

48:24

So, you're your predict.

48:26

A Go ahead, we'll add one thing that is predict proba.

48:29

So what is Predict Proba?

48:31

Predict Proba will give you the probability of the predictions.

48:35

Okay?

48:35

So remember, this all thing tests data in.

48:39

So model.

48:40

Predict on X test when you do, you will get the predicted values.

48:43

You will get the predictions here.

48:45

What the model is predicting?

48:48

This where is it?

48:49

This is your Predict Proba's.

48:50

you are getting this from the predict problem the probability of the prediction

48:56

now this is new for classification this method we did not have for regression regression

49:01

regression we were just doing dot fit dot predict you find the line and given a new X you try to

49:06

predict that is all that we were doing in regression in classification what we are doing

49:12

we again build a surface and given a new X we are trying to predict what

49:17

we are actually trying to predict what we are actually trying to

49:20

predict what is the probability of the Y.

49:24

So that is a new thing that we are trying to do in classification.

49:26

In classification, we are in a way trying to predict what is the probability of the

49:30

so based on the X we are trying to estimate we are in a way trying to estimate what is

49:34

the probability of the Y. So that's the thing that we are trying to do in a typical

49:38

classification problem. So based on the value of X can be find out what is the what is the

49:43

probability of the white. What up here here you are able to see them as much. Okay.

49:50

So here we have a different data frame

49:55

but absolutely in a raw way,

49:59

if we're totally in a raw way,

50:03

let me write the code for you.

50:04

Exactly raw type of what are.

50:06

So that you get a better idea.

50:09

This is what happens.

50:10

Because this is simple code.

50:11

There's a lot of things here,

50:12

there's a table, etc.

50:13

So this is the simplest way to look at it.

50:16

Now, look at it.

50:16

Now what is going on here, guys.

50:19

it is returning two values, right?

50:22

You're getting two numbers right now.

50:23

And you know what these two numbers are?

50:25

These two numbers basically point,

50:26

basically are the two classes.

50:29

One of your zero plus

50:30

or one plus.

50:33

This is your zero plus.

50:34

This is your own plus.

50:36

And these are giving you the probability values.

50:38

Here you have probability is showing up.

50:40

Probabilities.

50:45

So you are able to see the probability of the zero plus

50:47

and you're also able to see the probability of the

50:49

plus. So based on the features, you're able to understand what is the probability of the,

50:55

you know, of the zero class and what is the probability of the one plus.

50:59

And what are these numbers right now?

51:01

These numbers are basically corresponding to the probability.

51:06

So 9.88 into 10 to the power minus 1.

51:10

What is the meaning of 9.88 into 10 to the power minus 1?

51:13

What is the meaning of that?

51:15

The is the matter of e minus 1,

51:18

but 10 to the power minus 1.

51:19

So the meaning of E minus 1, go got 10 to T power minus 1.

51:23

That is what E minus 1 actually refers to.

51:25

So 9.8 into 10 power minus 1 what is.

51:30

0.98.

51:32

And 0.98,

51:34

it means 98%.

51:35

So,

51:38

so what's what?

51:42

There is only a 1.1% probability that this person is only a 1.1% probability that this person is,

51:48

diabetic. Sorry, this person will pass.

51:53

Because one pass is zero fail here, right?

51:55

There's only a 1% probability the person might pass.

51:58

And, you know,

52:00

threshold is always 50%.

52:03

Default is psychic nerd.

52:05

Okay?

52:06

So, these two things

52:08

are all right.

52:09

So here's fit got.

52:10

Here to be it.

52:11

Here to everybody knows what's in what we are building the model.

52:15

Based on whatever model you have built,

52:18

you can this prediction based on whatever model you have built right now,

52:22

you can prediction

52:22

and you have a probability of predictions are

52:26

and all the way at the bottom you'll be able to get the predicted values.

52:30

You're here here.

52:31

Predicted value is the meaning of the zero predicted value?

52:35

Predicted value is what is the meaning of the zero?

52:35

What is the predicted value?

52:38

The predicted value is the model has predicted that it is not diabetic.

52:42

So that is the meaning of the zero predicted value.

52:46

So predicted value basically means the model is the model.

52:48

is not diabetic because the probability of diabetes was very low.

52:53

So because the probability of diabetes was very low.

52:55

Because the probability of diabetes was very low, we can say that model is not diabetic.

53:01

Now, the other one, there's a 53% probability of diabetes.

53:06

10 to the power minus 1,

53:08

that 0.53.

53:10

0.53% percent, so 53%

53:13

probability of 1 would be 53%.

53:16

It's probability of 1 is 53% which 50%

53:19

which is 50%

53:20

then model will predict diabetes.

53:24

So the first we're probability

53:26

we're going to internally and

53:28

it's based on the basis we predict

53:29

that they belong to.

53:32

Now you're getting. You know what?

53:33

You're seeing. And these

53:36

are all things is happening on the test data.

53:38

If you have, I'm that

53:39

be confused. I'm I'm that if you're looking at it.

53:40

This is your test data. If I just go and do ahead

53:43

if I just go and do ahead and that

53:45

show the top five goes, this we're doing.

53:47

And what are we doing?

53:48

We take the data, we build a model,

53:51

model been got.

53:52

Now you're new data

53:53

are you, that's it.

53:54

You're new data

53:55

on the new data, the test data

53:56

is, the mock question paper

53:57

is, that's it.

54:00

Everybody can relate to it.

54:02

So you're showing the X.

54:03

Let's, if this X were prediction

54:05

this is, if it's the probability

54:07

this is, for the third row,

54:10

probability 51% is.

54:13

If you're 51% is,

54:14

50% is.

54:15

That means, based on these features,

54:19

study hours,

54:20

it's enough, sleep hours,

54:21

it's, distraction,

54:22

if any student's

54:23

this data,

54:23

we know

54:23

we know that our model predict

54:26

that there's a 51% chance

54:28

that the person will pass.

54:30

Which is 50%

54:31

so the model has predicted

54:33

pass.

54:36

So that's the way

54:37

how it will work out.

54:37

Oh, I'm sorry, I'm sorry,

54:38

my mistake.

54:39

E minus 03 and sorry, my mistake.

54:42

So it's actually very low.

54:43

Sorry, yeah.

54:45

It's actually a nice.

54:45

99% probability the person will fail, actually.

54:48

So the model has predicted fail.

54:50

Okay?

54:51

Fifth's the record.

54:52

Here, pass, predict, why?

54:54

Because if a fifth one of record,

54:55

there is a 95.69% probability the person will pass.

55:00

Mottaphtap.

55:00

There's a very strong indication the person will pass.

55:05

So the probability is very high.

55:06

More than 50%, so model has predicted you will pass.

55:10

So key takeaway, the key summary of the conversation would be,

55:14

three things.

55:15

We first data on the model to fit

55:17

the other thing,

55:19

we try to find out the probabilities on the test data

55:25

on the test data.

55:26

First thing, we're train data

55:28

model to fit

55:28

do s'rater.

55:29

We try to test data predict proba

55:33

we try to find the probabilities of predictions on the test data.

55:36

That's the next thing that we do.

55:38

And the final thing is based on those probabilities,

55:40

we try to find out the predicted values on the test data.

55:43

So these are the three things that we try to do.

55:45

Okay. So first, we, you know, so, so once again, first thing, we go and do the dot fit.

55:54

We train the model. Second is we go and find the predicted probabilities.

55:58

We find the probability of the predictions.

56:00

Predict proba kerted. And the third thing we predict

56:03

are the three things that we go back and move over all.

56:11

Okay, I hope everybody is clear.

56:13

Here we have that same thing summarized here.

56:15

summarized here. But here actually, we have

56:18

actually, we have a different data frame

56:19

that's the way test, here. Here, actual results

56:21

are that's it. So, it's a bit confusing

56:23

is that. We've got it. We'll, we've got it.

56:26

And we'll share it. So simple, this is the way how you actually do it.

56:30

Now, one of the people's in the mind in the

56:32

this is binary.

56:34

Multi-class in what we'll go back in.

56:37

So we'll make a case study

56:38

that what happens for multi-class.

56:40

This is two classes, or,

56:41

either zero, or one.

56:43

If three classes, four classes,

56:44

if you're four classes, five classes, so what will?

56:47

You'll, five probabilities predict

56:48

and four probabilities predict

56:49

and three probabilities predict are.

56:52

This is binary, either zero or

56:53

or one.

56:53

All the use cases we are discussing,

56:55

because our content is that.

56:57

We'll next day in

56:58

we'll make a multi-class example

56:59

will give him.

56:59

So, the binary

57:01

is either zero or one, right?

57:03

So when we do predict proa,

57:05

you're only having two classes.

57:07

Yeah, the probability of zero

57:08

or the probability of one.

57:09

Yeah, that's a very good question.

57:10

Threshold change of what is.

57:12

We'll get to discuss.

57:13

We'll come back in the class in a moment.

57:14

We'll discuss that.

57:16

That's a different point.

57:17

We'll see that in a moment.

57:20

So predict, Proba and predict we have actually seen here.

57:25

Now, let's move on.

57:32

Okay, so discusses.

57:37

We can actually talk about it for a moment.

57:40

And we can actually change the probabilities also.

57:42

Um, threshold change can change, right?

57:44

See, this is what we discussed, right?

57:47

When you call model.

57:48

It gives you a hard zero or one.

57:51

That is what we discussed, right?

57:52

Now, when the predict call,

57:53

then you either zero a or one will.

57:56

Based on whatever use case we talked about now,

57:59

or pass or fail, right?

58:01

But internally, what is logistic doing?

58:03

It is calculating a probability

58:05

using the model.

58:06

That is what it is actually doing behind the scenes.

58:10

So internally behind the scenes,

58:12

logistic is actually calculating.

58:13

Logistic is actually calculating a predict.

58:14

predict proba method.

58:16

That is what logistic regression is internally doing.

58:19

It is calculating something called predict underscore proba.

58:22

That is what it is doing.

58:27

That is a very good, that is a very good question, Eubraj.

58:30

The prediction to know, so probability key important.

58:32

We'll talk about it.

58:34

Let me talk about that.

58:35

And that's what I'm coming to.

58:37

So internally, you're probability calculate.

58:40

And by default, the probability of passing is greater than 50%.

58:44

your 50% threshold by default.

58:49

If 50% than more probability, then model will predict that plus.

58:53

Whichever plus has a higher probability, most will predict

58:55

50% is the baseline.

58:58

So this is the internal way how logistics is working.

59:01

Now,

59:03

the problem is the probability of relevance.

59:06

What is the relevance?

59:06

Why we've been talking about it?

59:09

Why is probability important?

59:11

Let us discuss it.

59:12

Let us discuss the idea.

59:14

why it is important to talk about the concept of predict proba?

59:23

Why are we?

59:26

So now, you know, now, you know, this is this explain to you.

59:31

We have a note here on this.

59:34

So this is what we talked about, to summarize, right?

59:37

Left hand side, predict proba straight forward.

59:40

You have two values will be because we are focused on binary.

59:42

So, yeah, to zero, or so one, right?

59:45

This is the binary.

59:46

Yeah, I'm sorry.

59:48

Yeah, so zero or so one.

59:49

So model will predict what is the probability of fail and probability of pass?

59:54

One, matter of pass.

59:55

If 92% probability of pass, then model has predicted pass.

1:0:02

Simple.

1:0:04

That's the intuition.

1:0:07

So now,

1:0:12

If you think about it,

1:0:17

probability of the matter what is?

1:0:19

Probability important, why?

1:0:22

Because if you're you this one of reasoning

1:0:23

will go, the person who got 92% probability of pass,

1:0:30

that will be pass, that the person who got 51% probability of pass, that will be pass

1:0:31

will be pass, and the person who got 51% probability of pass, that be pass

1:0:39

right? You here here a value, you take it, you know, if it's a 51%

1:0:42

like, okay?

1:0:43

This is also possible, right?

1:0:47

possible?

1:0:48

Mani, we have, we made a student's record

1:0:49

and the model has predicted that the probability of pass is 51%

1:0:55

possible.

1:0:57

So 51% if it is 51% if it is

1:0:59

50% more, it's that he can't be fast.

1:1:03

So, yeah, that the model is giving the same prediction for both the people?

1:1:07

Because very clearly the student,

1:1:09

one is more deserving.

1:1:11

It's a pass on a more probability, so it's

1:1:13

a different thing. But it's just borderline

1:1:15

crossed it, then it's just a borderline

1:1:15

crossed it, then he's got to pass

1:1:17

show it.

1:1:19

So that's the thing.

1:1:21

So in high-stakes scenarios,

1:1:23

probabilities matter more than little.

1:1:26

Probability are important.

1:1:28

It is not important to just go back

1:1:29

and, you know, kind of,

1:1:31

just say, yeah, 50%

1:1:33

than more, then, okay, pass-carus,

1:1:35

no, okay, pass-carat-do, but

1:1:37

flag-be-go. That's the thing.

1:1:39

So, so the use case would be, I hope, you know,

1:1:43

Yubras, that was your question.

1:1:45

You know, you know,

1:1:45

so the use case would be,

1:1:49

if this second student,

1:1:51

okay, we, we're, we're,

1:1:52

we're, we're, we're going to,

1:1:52

we're not,

1:1:54

that's, as I told you, is,

1:1:56

is, is, is, is,

1:1:57

this, is, is, is, is, is,

1:1:59

so model will say,

1:2:01

okay, the person is pass.

1:2:04

But, but,

1:2:04

but you,

1:2:04

but you, if you're,

1:2:05

the probability of,

1:2:06

you'll see,

1:2:07

that you'll,

1:2:07

how confident,

1:2:09

we are about that class.

1:2:11

That's, you know, that's important.

1:2:13

So, okay, we will treat them differently.

1:2:15

This is important thing is.

1:2:17

So now you will get a better idea,

1:2:18

that, okay, this student is different.

1:2:22

You can take a other use case,

1:2:24

that you, uh,

1:2:25

could, you, uh,

1:2:25

could be,

1:2:26

you, you know,

1:2:27

let's say probability of default.

1:2:31

You're your one who is,

1:2:32

probability of default is,

1:2:34

I'm just giving a use case,

1:2:36

okay?

1:2:37

One person is,

1:2:39

probability of defaulting.

1:2:43

It's 90% probability of default.

1:2:46

So model to it's

1:2:47

defaulted is, okay?

1:2:49

And one person

1:2:51

is, you know, or let me put it

1:2:55

this way. Let me, let me say,

1:2:57

one man is, let's put it this way,

1:3:02

there's a person and there's a

1:3:04

90% probability that

1:3:06

the person will pay the loan.

1:3:09

You're basically looking at the features of the person,

1:3:14

what's income is,

1:3:15

where it's where it's,

1:3:15

what's the home,

1:3:16

what is,

1:3:16

dependent,

1:3:17

or single,

1:3:18

and based on that,

1:3:20

you're trying to predict

1:3:20

that the man's

1:3:21

he will the person pay back the loan?

1:3:22

The model is trying to predict

1:3:23

that will the person pay back the loan?

1:3:26

And this is a very common problem

1:3:27

that credit cards and industry is trying to solve, right?

1:3:30

Credit card be a one way

1:3:31

if you're a credit card in transaction

1:3:33

so you're,

1:3:34

so you're 40 days back

1:3:35

you pay for repay.

1:3:35

35, 45 days back payment cycle

1:3:37

in repay.

1:3:38

So it's a kind of

1:3:39

for loan.

1:3:40

A credit card

1:3:40

as any

1:3:41

the credit card

1:3:42

in the bank's

1:3:42

looking at your

1:3:43

historical data

1:3:43

and they are all

1:3:44

constantly trying to

1:3:45

solve this problem.

1:3:46

They're trying to

1:3:47

predict real time

1:3:48

that customer

1:3:49

pay or not.

1:3:50

Now you're

1:3:51

a credit card

1:3:51

like two

1:3:52

$2,5

1:3:52

and they're

1:3:53

a loss for the bank

1:3:54

right?

1:3:54

So they are

1:3:55

constantly trying to predict

1:3:56

that what is the

1:3:57

probability the person

1:3:57

will repay me.

1:3:59

So here

1:4:00

here a customer

1:4:00

who has 90%

1:4:01

probability

1:4:02

of repayment

1:4:02

that he will pay

1:4:04

pay will

1:4:04

so the model

1:4:05

made all good

1:4:06

customer is in good

1:4:07

standing.

1:4:07

If you

1:4:09

if you

1:4:09

50%

1:4:10

threshold

1:4:10

so

1:4:11

Pratik Proba

1:4:13

value

1:4:13

return

1:4:13

will return

1:4:13

0.9.

1:4:17

So the

1:4:18

probability

1:4:18

of payment

1:4:19

is 0.9

1:4:19

that is

1:4:20

what

1:4:20

predic proba will say

1:4:21

and your

1:4:23

bank will

1:4:23

classify

1:4:24

that

1:4:24

customer

1:4:24

good

1:4:25

is

1:4:25

one

1:4:27

more model

1:4:27

there

1:4:28

another

1:4:29

customer

1:4:29

probability

1:4:31

that the customer

1:4:32

will pay is

1:4:32

0.51

1:4:33

or bank

1:4:35

will still

1:4:35

classify good

1:4:36

see that is triple

1:4:38

good

1:4:39

are both

1:4:40

card

1:4:40

both

1:4:41

functioning

1:4:41

ray

1:4:41

no problem

1:4:42

because if you

1:4:43

if you

1:4:44

if you're

1:4:44

if you're

1:4:44

if you're

1:4:44

if you're

1:4:44

if you're

1:4:46

both

1:4:46

are

1:4:46

predicted

1:4:47

to pay

1:4:47

because

1:4:48

both are

1:4:49

predicted to pay

1:4:49

but the

1:4:51

first

1:4:51

customer is more

1:4:52

likely to pay

1:4:53

because it's

1:4:53

probability

1:4:53

of payment

1:4:54

is a

1:4:55

second customer

1:4:56

is the

1:4:56

border line

1:4:57

is

1:4:57

that

1:4:58

yeah

1:4:58

that

1:4:59

you're

1:5:00

you have

1:5:00

flag

1:5:00

so you can

1:5:01

flag

1:5:02

the transaction

1:5:02

flag the customer

1:5:03

and flag the customer

1:5:03

and

1:5:06

I'll give you one more

1:5:07

use case, one more

1:5:08

beautiful use case.

1:5:10

This use case is that

1:5:11

sometimes we can we

1:5:12

change

1:5:14

we can change

1:5:14

we

1:5:15

we can change

1:5:17

we can't

1:5:18

we

1:5:18

we can change

1:5:20

so that's the

1:5:23

interesting part

1:5:23

and as I told you

1:5:25

this is

1:5:26

effectively what I talked

1:5:27

about so far

1:5:28

default

1:5:29

0.5% decision threshold

1:5:31

if 50%

1:5:33

if it's side is

1:5:34

it is pass

1:5:34

50% of this side is to fail it

1:5:36

We talked about that.

1:5:38

Now here is the beautiful thing.

1:5:39

You can go,

1:5:41

you can go and effectively

1:5:43

you can change that threshold.

1:5:48

And I will talk about that for a minute.

1:5:49

You can actually go back and change that threshold also.

1:5:53

Yeah.

1:5:54

You can go back and change that threshold also.

1:5:57

You can change this threshold.

1:5:58

This is what we discussed.

1:6:01

Take the data, build a model.

1:6:03

And the model will predict

1:6:03

that probability of pass

1:6:05

and probability of fail.

1:6:06

and based on the 50% threshold model will predict something.

1:6:10

But you can't change

1:6:12

now business case

1:6:14

what is the threshold to change

1:6:16

what is the business case?

1:6:20

What is the business case?

1:6:25

We'll change that.

1:6:26

We'll just discuss

1:6:27

on this slide.

1:6:31

Okay?

1:6:32

This we have in the code

1:6:32

we're not going to

1:6:34

conceptually you're

1:6:34

so

1:6:36

50% default

1:6:38

is 50%

1:6:40

your default

1:6:40

now

1:6:42

you're

1:6:43

logically

1:6:44

say

1:6:44

if it's a weighing

1:6:46

balance

1:6:46

50% is default

1:6:47

so

1:6:47

zero or one

1:6:49

equally

1:6:49

go to

1:6:50

think about it

1:6:51

that way,

1:6:51

you know?

1:6:54

You're

1:6:54

both classes

1:6:55

pass or fail

1:6:55

equal weight is

1:6:56

okay?

1:6:57

So this

1:6:58

whole model

1:6:58

is up

1:6:59

model will predict

1:7:00

some probability

1:7:00

depending on the

1:7:01

student

1:7:01

what is the probability

1:7:03

of pass

1:7:04

if his pass

1:7:05

probability

1:7:05

then he will pass

1:7:06

will be

1:7:07

prediction

1:7:08

pass

1:7:08

if

1:7:09

if fail

1:7:09

probability

1:7:10

if fail

1:7:11

we talked

1:7:13

about

1:7:13

now here is

1:7:14

here is a

1:7:15

interesting

1:7:15

part

1:7:15

now

1:7:16

this is obvious

1:7:17

but we're just

1:7:17

just putting

1:7:18

a picture

1:7:18

around it

1:7:19

now the school

1:7:20

is becoming

1:7:20

very strict

1:7:21

school

1:7:22

is saying

1:7:23

okay

1:7:24

51%

1:7:24

be pass

1:7:25

they're

1:7:25

90%

1:7:26

pass

1:7:26

they're no that

1:7:26

cannot happen

1:7:27

if

1:7:28

if we're

1:7:28

if we're

1:7:28

if we're

1:7:29

if we're not

1:7:29

if we're

1:7:30

we're not

1:7:31

what we're going to

1:7:34

percentage are

1:7:34

the threshold is

1:7:36

nothing but a

1:7:37

passing

1:7:37

percentage

1:7:37

for us.

1:7:39

Yeah,

1:7:39

it's the

1:7:39

thing is

1:7:39

all

1:7:40

everything

1:7:42

will be

1:7:42

same

1:7:42

will

1:7:42

change

1:7:43

change

1:7:43

okay

1:7:44

you know

1:7:45

everything

1:7:46

will change

1:7:47

you take

1:7:48

the data

1:7:49

you build a

1:7:49

model

1:7:50

do the

1:7:50

dot fit

1:7:50

and for

1:7:52

every

1:7:52

test

1:7:53

row

1:7:54

you find the

1:7:55

predict

1:7:55

proba

1:7:55

predict proba

1:7:55

make out

1:7:56

probabilities

1:7:58

make out

1:7:58

you know

1:7:58

here

1:8:00

all same

1:8:01

the only changes

1:8:02

in the end end

1:8:03

end in

1:8:03

you will write an EFL statement.

1:8:07

You will write an EFEL statement to do the predictions.

1:8:10

So you're

1:8:11

you,

1:8:11

you know, you know, what you call?

1:8:16

I'm just going to give you a pseudo code.

1:8:17

I'm just going to give you a pseudo code to keep the thing simple.

1:8:21

So I'm just going to do a pseudo code for you.

1:8:23

So a normal predict proa, you know, you can't know, you know, you can't predict proba.

1:8:27

Model will use the default 50%.

1:8:31

Now what you can do?

1:8:32

Now what you can do, now,

1:8:33

you can go back and you can do this with respect to 70% threshold.

1:8:40

So you can say, now, change the threshold to 70% percent. And you will just write an

1:8:50

afl statement. I'm not doing that in detail, but you can do that later.

1:8:55

You can say that if, you'll say that if, if, if predict proba,

1:9:03

If predict, underscore, proba, is greater than 70%, then, predict, pass, else, predict,

1:9:23

mean, how about, this is, what I'm going to say?

1:9:27

Not difficult, right?

1:9:28

Simple's a thing.

1:9:29

Default is 50% is.

1:9:31

That is how SK learn is working.

1:9:32

That is K learn's.

1:9:33

If you're a default, if you directly dot predict method, then 50% is the threshold.

1:9:38

But here you can here you can't, same thing.

1:9:42

Take the data, do the fit, find the probabilities.

1:9:45

If it was 70% percent more than pass, if it, if it's 70% than

1:9:48

more, then fail.

1:9:50

In fact, based on our reasoning, this is the entry, model, it's actually fail

1:9:54

there. Here we're pass, because it's 50% up up on up.

1:9:58

But based on our logic, because it's 70% is, our model is fail.

1:10:03

This is the simple way we can write the pseudo code.

1:10:06

And if you come back to the slide again, if you see, 70% highly confident positive predictions, if you see.

1:10:14

So only when we are very confident the person will pass the pass the pass, otherwise, otherwise, if you want to be more generous,

1:10:22

I want to pass more people, then you can't do.

1:10:25

And this will apply for many, many different use cases.

1:10:28

We'll see some more use cases down the line.

1:10:31

Just say, money is a bank.

1:10:32

Okay, I'll give you a real.

1:10:33

example credit card fraud is a use case we talked about right now think about it you think

1:10:38

banks will use 50% threshold as a 49% chance of fraud day 49% probability of fraud is huge

1:10:46

in banking. You can imagine 49% chance of fraud what I'm like you can imagine 49% chance of fraud

1:10:51

what if you're doing 1000 crore worth of transactions so 500 kron to fraud may you understand

1:11:01

the probability math actually so

1:11:03

What I'm getting at is, same aspect.

1:11:08

You take the data, fit the model, and you are trying to calculate the prediction probabilities.

1:11:15

You are trying to calculate the prediction probabilities.

1:11:17

If your prediction probability is very much,

1:11:22

if your probability of fraud, very much higher than 50% up up, then fraud would becky percent

1:11:27

if up or more than fraud, then fraud may becky.

1:11:30

That's what the issue is.

1:11:33

So banks' case.

1:11:33

case in if I just slightly change the story, this is, if I just slightly change the story,

1:11:38

this is, if I just slightly change the story, if I say this is like,

1:11:45

like, like, like, like, like, like, like, like, not fraud, this is not fraud

1:11:48

part and this, right?

1:11:52

Mani, it, it's fraud detection.

1:11:53

Front one, and not fault zero is.

1:11:55

This threshold, it's just down here on here.

1:11:58

And this will be something like 01.

1:12:00

That's the bit more.

1:12:01

That's more than it.

1:12:03

0.01, well, well, it's, well, 1%.

1:12:05

In real world scenario, banks will have a threshold of 0.001,

1:12:10

because they cannot afford a single fraud.

1:12:13

A big bit more bad.

1:12:15

So, this threshold more come over.

1:12:17

You understand the math right now.

1:12:19

So, that's the same thing is.

1:12:21

Dot fate, dot predict, trauma.

1:12:22

And the pseudo-code is that.

1:12:24

If my probability, if my probability of fraud is greater than 0.0001,

1:12:31

Then we go and it's fraud classify

1:12:33

to, else we'll classify that as fraud only when the probability is more than 0.001.

1:12:45

So even the slightest chance of fraud will be classified as fraud.

1:12:50

If it's a good transaction, then it'll, well, it's probability of fraud come over.

1:12:53

Even the slightest chance of fraud, even the slightest problematic transaction unit,

1:12:59

let's say it's a genuine transaction.

1:13:01

So, in the sub-u-uped-uped your card, you used to,

1:13:03

credit card you have night to swipe.

1:13:05

So that is like a 0.001% probability of fraud,

1:13:08

but still, but the model will still classify that as fraud.

1:13:12

So see, the real-world use case that we'll change.

1:13:16

So classification problem, you'll always predict-pro-bah use

1:13:18

and you, you'll be probably, you'll make up your logic

1:13:21

use and you'll make it threshold to.

1:13:24

But, I mean, again, for the problem solving,

1:13:27

50% is good, but this is something I wanted to explain to you for your understanding.

1:13:31

that we are the thresholds for key change.

1:13:37

Okay, everybody's okay with me.

1:13:39

Do give me a quick confirmation on chat.

1:13:41

All of you are following along.

1:13:50

Let me know, guys.

1:13:55

We have one of course.

1:13:56

We have all of you are following along.

1:13:57

Do let me know.

1:14:00

Here's all clear.

1:14:01

It's a bit of a long concept.

1:14:03

This is a lot of this.

1:14:03

We'll come to before we're a practical

1:14:04

because this is a little conceptual

1:14:06

thing.

1:14:06

So we'll, we'll, we'll do a problem

1:14:09

and then we'll come back to this.

1:14:11

Clear is?

1:14:12

All of you're okay.

1:14:12

Let me know, guys.

1:14:15

Everybody's fine.

1:14:16

You want to take a five minutes

1:14:17

breather and come back?

1:14:19

Quick water break.

1:14:20

Be good.

1:14:21

Summer season has started, so

1:14:22

we should take some small break in between.

1:14:25

So let's take a small break.

1:14:26

Okay?

1:14:27

A short break, let's take a small break.

1:14:27

Let's circle back in five minutes.

1:14:30

Okay?

1:14:31

Thank you.

1:15:01

Thank you.

1:15:31

Thank you.

1:16:01

Thank you.

1:16:31

Thank you.

1:17:01

Thank you.

1:17:31

Thank you.

1:18:01

Thank you.

1:18:31

Thank you.

1:19:01

Thank you.

1:19:31

Thank you.

1:20:01

Thank you.

1:20:31

Okay.

1:21:01

Thank you.

1:21:31

Thank you.

1:22:01

Okay.

1:22:31

Okay.

1:23:01

Thank you

1:23:31

Hi, everybody, welcome back.

1:23:37

We'll start on here.

1:23:38

So we'll do a we'll do a case.

1:23:40

I think let's do a case study.

1:23:42

I think let's do a case study.

1:23:43

So whatever I talked about all this while,

1:23:45

a simple case study may apply so that so that will make you more confident.

1:23:49

And like as I told like today, like today, you know, we have some time to talk about a case study.

1:23:54

They want you to do that in the class.

1:23:56

So it will be, it will be fun.

1:23:57

So concepts on me a simple data set

1:24:01

us here. So far we have talked about this in a simple data set, if you see. And now what I want you to do,

1:24:09

see any thing is fit, predict, predict, predict prober. And

1:24:13

we go ahead and we go and then then future matrix can, then future matrix will. But right now,

1:24:17

the case study is where we want you to do this exact same credit default prediction. This is what

1:24:24

you will have to do right now. You will have to go and look at the features of a customer.

1:24:31

bank is customer and you have to predict whether they will default on their credit card next month.

1:24:38

This is the same use case I was discussing with you.

1:24:42

This is actually how banks do it.

1:24:43

Banks work exactly the same way.

1:24:45

Like, if you have a credit cards, not for issuing card.

1:24:49

Issuing card. Issuing card is a different workflow.

1:24:51

That's the card issue default prediction would.

1:24:54

This one is people who are already having the card.

1:24:56

You have card.

1:24:57

The bank is tracking your current payment history, billing amount.

1:25:00

you're how are you paying the repaying on time?

1:25:06

It is looking at all those factors and we will predict

1:25:10

what is the probability that you will default the card the next month.

1:25:16

One, it's defaulted. Zero, it means not default. It will. Simple.

1:25:20

So back to the same thing.

1:25:21

I mean, our problem statement in could change in coding.

1:25:24

There's a codeing in change not. Actually, it is hardly a 20 second exercise.

1:25:28

I mean, that's all over a half a second exercise. I mean,

1:25:30

so it is like hardly 20 seconds if you use the same template.

1:25:35

But it is to gain some confidence.

1:25:37

How's going?

1:25:38

Min-max scalar and logistic you use the same thing.

1:25:42

So this one thing you have to throw a little bit more than to do.

1:25:44

So what we did in the last California housing, you know.

1:25:47

Why do we do we do scaling?

1:25:48

We do scaling to make sure all the values are in the same scales.

1:25:53

So this is a very good use case for the current data set also.

1:25:56

Because other, other data points, other scales may be.

1:26:00

So we want to make sure that we want to convert everything to the same scale.

1:26:03

So we'll use the same thing we did last class in California housing.

1:26:07

Pipeline use case.

1:26:08

So we will use the pipeline.

1:26:10

First we min-maxed.

1:26:11

Then we'll logistic.

1:26:14

That's it.

1:26:15

That's it.

1:26:16

Simple use case we have right now.

1:26:18

We have it.

1:26:18

We have it solve right now.

1:26:20

And finally, you will have to do until here.

1:26:22

That's it.

1:26:23

Take the data.

1:26:24

Look at the data set.

1:26:25

Load the data.

1:26:27

X or Y separate.

1:26:28

Train test create.

1:26:28

Pipeline.

1:26:29

Bona.

1:26:30

build the model, dot fit, dot predict, dot predict, that's it.

1:26:34

This one of the thing, you know.

1:26:36

Confucian matrix is something I haven't talked about until now.

1:26:38

Just here to number four, you, you have to number five to bring.

1:26:42

And this is the data set that we are using from Kagan.

1:26:47

You can't data here from download can.

1:26:49

Or then we'll have to download and give you.

1:26:50

And you will have to build the model on this data.

1:26:53

Actually, let me share the data with you.

1:26:55

That will be better.

1:26:57

You know, have to create an account and all that.

1:26:59

So first, no need to do any, no need to do any.

1:27:00

thing.

1:27:01

First, you go to website in go.

1:27:03

Problem to say first.

1:27:05

Take five minutes, read the problem.

1:27:07

Then, then we'll model model.

1:27:10

Okay?

1:27:11

Coding is very simple.

1:27:12

Coding is the easiest thing.

1:27:13

You know, you know, that you know, that code in

1:27:15

it's not going to be the same thing.

1:27:16

You're the same thing, X, X, Y, train test, plate, dot fit, dot predict.

1:27:20

Same template is.

1:27:21

But the understanding of the problem will be very, very important going forward.

1:27:25

As you get deeper into solving real business problems,

1:27:28

the understanding of the domain is.

1:27:30

something that will matter or not.

1:27:32

And jitna, you're just like this type of competition problems

1:27:34

take more confidence you will get.

1:27:37

You have more confidence will get.

1:27:39

You know, that is the whole idea.

1:27:42

Like, you know, so take the class concept.

1:27:44

See, all class, we will not have the opportunity to take up these kinds of case studies.

1:27:48

But this is something you will have to do.

1:27:50

Because class can, a certain curriculum here we have to follow, right?

1:27:53

So we, I'll still try to take out as much time as I can to cover these things with you.

1:27:58

But you should have the dedication where you know, you, you know, you, you, you,

1:28:00

You take the concepts that we are discussing,

1:28:03

and you can't say,

1:28:04

you know, like, you know, like,

1:28:07

you have to a motivation from a, you know, like, you have to a motivation

1:28:09

from you, right?

1:28:10

So the same templates will be applied here.

1:28:13

Anyways, so we'll, we'll solve this today.

1:28:15

Everybody, please take five minutes to read the exercise first, then I'll guide you.

1:28:19

We'll, we'll, start, such, we'll, take five minutes all of you.

1:28:23

And we're, and we'll download and you'll share to.

1:28:25

Don't worry.

1:28:26

Don't have to download anything.

1:28:28

So we're here a folder and share together.

1:28:30

Thank you.

1:29:00

Thank you.

1:29:30

Thank you.

1:30:00

So, I'm the data, guys, guys, guys, guys, guys, everyone can't

1:30:15

I'm data we upload

1:30:19

guys.

1:30:20

Everyone can see that.

1:30:23

So, okay, you need the problem first.

1:30:26

Don't want to distract you.

1:30:27

But just to let you know, I've also uploaded the data set here.

1:30:31

This is your CSV file.

1:30:32

So you're first Kagle in problem.

1:30:34

Whatever problem I've already shared with you, you first take some time to read the problem.

1:30:37

Understand the problem.

1:30:39

There on data explained here what is the different fields right now.

1:30:43

Everything is beautifully explained.

1:30:45

So first problem, go to the 21st April folder,

1:30:49

now data set CSV to download caro, and then just go ahead and solve it exactly how it is given.

1:30:55

That's it.

1:30:56

This is all that is expected right now.

1:30:58

Okay.

1:30:59

Take five minutes all of you, something that I completely expect you guys to do in the class right now.

1:31:04

And then we will do the Confucian matrix topic arose.

1:31:06

This we'll come Confucian matrix apply.

1:31:15

Thank you.

1:31:17

Thank you.

1:31:47

Thank you.

1:32:17

Once people are done, take your time, I think your time, I think at least five 10 minutes I'm expecting.

1:32:35

As long, as far as you complete, please do let me know what is the train and test course you're getting.

1:32:39

That is the only expectation, okay?

1:32:41

Just let me know with logistic of our train or test accuracy kit now.

1:32:47

Thank you.

1:33:17

Thank you.

1:33:47

Thank you.

1:34:17

Thank you.

1:34:47

Thank you.

1:35:17

Thank you.

1:35:47

Thank you.

1:36:17

Thank you.

1:36:47

Hi, everybody, everybody has at least, everyone, everybody has at least read the problem, everybody has at least read the problem statement.

1:37:10

problem statement. I can just walk you through the problem statement once again.

1:37:15

So very nicely explained.

1:37:17

I think Kagal, I think Kagal, I've introduced here first.

1:37:20

It's a wonderful website where people, they share a lot of competitions and data sets.

1:37:27

There are lots of use cases here here.

1:37:30

A lot of real companies are also hosting competitions.

1:37:33

And now that we are starting to enter into these ML parts, you will start feeling a lot of confidence.

1:37:38

You will start feeling a lot of confidence.

1:37:38

You know, now look, these problems be.

1:37:40

There are a lot of different ways to solve it.

1:37:42

But even with a simple template that we discussed in the class, you can build a baseline model.

1:37:46

That is all we are targeting for now.

1:37:48

At least, how to take a data, how to craft it, how to build a model.

1:37:52

At least you should have that confidence.

1:37:53

That's the whole objective.

1:37:55

So what we have right now, we have got data from a real Taiwanese bank.

1:37:59

This Taiwanese bank and we have got information from 2005.

1:38:03

So April to September's data.

1:38:06

If you have a website, we have got information from April, 2005,

1:38:10

from September 2005, real customer data, but anonymized it.

1:38:14

You don't know the customer names.

1:38:16

Oftentimes, as information share care.

1:38:18

So data in little changes and customers' name

1:38:22

and customers' name and we're not sharing. This is a very small amount of data that is shared.

1:38:27

So what is the information that is given right now?

1:38:30

ID of the client, I mean, this your customer ID go jay.

1:38:33

Internet backing, HDFC, ICSA, like customer ID. It's a unique number to identify the customer.

1:38:38

limit balance, what are you?

1:38:42

How much of credit is given to you?

1:38:44

If you take a credit card in India, your credit limit is given to.

1:38:47

The default credit limit goes to give you.

1:38:49

That is what this refers to.

1:38:51

This is obvious education, marriage.

1:38:53

This is something to understand.

1:38:54

Each customer, a day married, single, education, male, he is, female,

1:38:58

you to understand.

1:38:59

Age is in years, what is.

1:39:01

And these are the payment statuses, repayment statuses.

1:39:03

This is very, very important.

1:39:05

And this is actually what banks do you.

1:39:06

You'll be surprised to know, banks access.

1:39:08

do this. Data as a track here. For every customer, there are, there are like hundreds

1:39:14

of columns that are tracked. You'll be surprised to know, even at a level of ICICA bank, they are doing

1:39:20

this. They have a very big data team that is sitting in Bombay. Mumbai in Mumbai in its main operations

1:39:24

and they are actually doing this world. Okay, they have a very big technology team that is sitting

1:39:29

and doing this world. So for every customer, they are, they are actually tracking, you know,

1:39:34

information like the payment statuses.

1:39:38

So, like here we have April-September data, so you, you know, for every customer,

1:39:42

we have information there will. These are the column names, if you're, if you data

1:39:46

look better than you'll better understand. If you're, if you're, if you're, if you look somewhat

1:39:50

like this. This, I've been uploaded already. Your data looks somewhat like this. Let me share

1:39:57

with you. This is your data set. You see I, credit card, CSB. And you can't, you can't

1:40:05

you can see you. Your information will be, one second, sorry, what happened to you.

1:40:15

Your information will be given somewhat like this. Every row is a customer and we are looking

1:40:20

at the different features of the customer. That's the way how we are able to look at it. And

1:40:25

this is your pay zero, pay one column. All right? The idea, so much. Limit balance we have discussed

1:40:30

here. These are education, marital status, age, these are the obvious columns. Okay.

1:40:35

Just understand what it is. Don't have to get too much into it. It is a lot of data, and it's a lot of data, actually.

1:40:41

There are 20, 30,000 rows of data.

1:40:43

a lot of data. A lot of data set up.

1:40:45

A bit, 700 rows of data set. This is a massive data set. Quite a big data set we are looking at right now.

1:40:52

Pay 0, pay 2, pay 3, pay 4, pay 5, pay 6. These are repayment statuses.

1:40:57

Every row is a customer. And these are the features of the customer. We are looking at the information of the customer.

1:41:03

These are all the features of the customer.

1:41:09

And these are the repayment status values that you are looking at right now.

1:41:12

These are all repayment status values.

1:41:16

So, like, pay zero is the repayment status as of September 2005.

1:41:22

So September 2005, in your repayment status, what is?

1:41:25

Okay.

1:41:27

August in your repayment status?

1:41:29

July, your repayment status

1:41:30

what is?

1:41:31

June in, what?

1:41:32

Okay?

1:41:33

May, in April, what is? Every month, we are tracking what your repayment status values are.

1:41:40

Next, the bill amount.

1:41:42

I mean, April from September, we are tracking only these six months.

1:41:46

But you're real one in front, how much data are. Because every month, credit card's statement

1:41:50

generated, right?

1:41:51

Credit card may, banks generate a statement every month.

1:41:54

Every month in every month, how much amount tracked? And this is actually the information that is

1:41:58

maintained.

1:41:59

For every customer, we are tracking, that every month in every month, how much amount?

1:42:03

maybe, I mean, two, three, years' data tracked.

1:42:06

But this is the trend and the pattern that we are trying to understand.

1:42:10

So, this is your April from April from September's billing amount of tracking, we

1:42:13

have made.

1:42:14

Now, you'll say, sir, what will?

1:42:16

The real world use case is what is it?

1:42:18

We're, why are we doing?

1:42:20

So, say, to do it from, they can't get them can't?

1:42:22

Billing amount we're track this only because,

1:42:24

because, I mean, it's obvious a trend, I'll, like, I'll give an example to you.

1:42:29

You, you, you know, you know, you know, you know, you know, look at this guy.

1:42:33

This card use not. It's a problem, right?

1:42:36

Now, if you have a customer, who has not incurred any bill amount for the last five months,

1:42:44

I'm for example, okay.

1:42:46

Imagine you have not incurred any bill amount.

1:42:48

You've never used in the last, uh, one of a year, all of a sudden this month,

1:42:53

you've had $9,000 swipe up. That is a red flag.

1:42:56

It's, it can't, no, lock, go ahead. What, you know, what's like, see, if you're a normal customer,

1:43:02

you'll be using the card, right?

1:43:03

Some kind of pattern will.

1:43:05

The man,

1:43:05

it will do it from,

1:43:06

or even OTP,

1:43:07

or $2,000, lounge access,

1:43:09

whatever.

1:43:10

But you have never used the card.

1:43:12

And bank will have the data for that.

1:43:14

You have not used the card.

1:43:15

Billing amount is showing as zero.

1:43:17

And all of a sudden,

1:43:18

now, now the RBI's rule

1:43:19

be able to, if you're not

1:43:20

if you're not used not,

1:43:20

then card gets deactivated.

1:43:21

That's a different thing.

1:43:22

But, like, actually, yeah, that's a rule also, by the way.

1:43:24

So 12, 12 months and all those is there.

1:43:27

But, but now the thing is that

1:43:29

if all of a sudden, one fine day,

1:43:31

one minute your transaction

1:43:33

was $9,000. That is a very

1:43:35

clear red pad.

1:43:37

If your billing amount is $9,000 for the last

1:43:39

month, then most likely the customer might

1:43:41

default. Or maybe you will have an operations

1:43:43

team, customer care to call call

1:43:45

and they will want to find out.

1:43:48

So these are all the processes

1:43:49

happening behind the scenes. And

1:43:51

this is not that you're asking to phone

1:43:53

customer care in, please unblock my card,

1:43:55

this stuff not can't. Oftentimes, the response

1:43:57

will be, sir, there's an operations team.

1:43:59

An operations team is your data science team sitting at the

1:44:01

back end.

1:44:02

Customer care is only going to answer questions

1:44:04

what they've been instructed to answer.

1:44:05

They have no idea of all this, right?

1:44:07

This is a simple blog that will be done on your card.

1:44:10

There is nothing you can do.

1:44:11

You have to do a mail channel.

1:44:12

You have to mail written.

1:44:14

So, if you're exceptional approval is given,

1:44:16

so you'll go, basically.

1:44:18

Or the exceptional approval is nothing but your threshold.

1:44:21

The threshold is what we discussed.

1:44:23

So some manager, some supervisor will have to exceptionally approve

1:44:27

that, okay, this customer is good.

1:44:28

They will look at somebody will manually examine your data.

1:44:31

We'll try to understand your case.

1:44:32

And then go and block it.

1:44:35

This is actually what happens.

1:44:38

Okay, so we're just

1:44:39

data explain to now.

1:44:40

Payment status,

1:44:41

and billing amount got, and this is also important.

1:44:45

This is also important.

1:44:46

This is a pattern, quite important

1:44:46

that, like, this your billing amount

1:44:49

or your payment amount.

1:44:50

It's how previous payment here.

1:44:51

Will amount is something, payment could.

1:44:53

This is the problem,

1:44:54

your billing amount.

1:44:55

Your billing amount had,

1:44:56

your billing amount had, $2,000, you paid,

1:44:57

payed, $500,000.

1:44:58

Why?

1:44:59

And, and if this trend,

1:45:01

it's a problem. So these are all things

1:45:05

that are being tracked for the customer.

1:45:07

And a lot of people doing that.

1:45:09

They revolving balance. It's a bad thing, but

1:45:12

people have this habit. It's a credit economy also.

1:45:15

Especially, like, in the younger generation

1:45:17

in our country, this trend is very much today.

1:45:20

So we are all like,

1:45:21

like, Western economies say credit.

1:45:24

So like we are getting to that kind of thing

1:45:26

because, you know, cost of living is increasing, whatever.

1:45:29

So the credit economy is there in a big way.

1:45:31

So, okay, so card, dues, people are not clearing and all that.

1:45:35

That is happening.

1:45:36

And banks are tracking that, actually.

1:45:38

Your billing amount is, but you have paid not paid.

1:45:41

Here here the billing amount has, one lakh of you.

1:45:42

You paid only 70,000.

1:45:44

So these are also getting tracked.

1:45:46

See, every row is a customer.

1:45:48

And the last column, which is your default payment next month.

1:45:51

This is your data that you have right now.

1:45:54

And the first thing is, from a real world perspective,

1:45:59

you want to understand.

1:45:59

So this is your historical data.

1:46:04

We have machine learning SACA, right?

1:46:05

Historical data.

1:46:06

You have some data already.

1:46:08

These are customers you already have.

1:46:10

This are in the system in

1:46:11

and you have.

1:46:12

You have it.

1:46:12

You have this data

1:46:13

know.

1:46:14

This we're not prediction

1:46:15

are, we are, we are already looking at

1:46:18

existing customers

1:46:20

April from September

1:46:21

data and they have

1:46:22

in October what did we know.

1:46:25

Understand it's very carefully, okay?

1:46:27

This is very careful. Okay?

1:46:27

Okay?

1:46:27

This April from September data

1:46:29

is, right? So April, September,

1:46:32

all patterns are.

1:46:33

And based on that, the output column,

1:46:35

it's color, okay?

1:46:36

This the output we need,

1:46:38

this is already known for all my customers.

1:46:41

This is already known for my historical data,

1:46:42

we already know this

1:46:44

for my existing customers.

1:46:47

That, okay, this particular customer

1:46:48

has defaulted,

1:46:49

this has defaulted,

1:46:50

this has default not.

1:46:52

That's it.

1:46:53

That is what I'm seeing.

1:46:55

So he's defaulted,

1:46:56

it, it's default not

1:46:57

it, it's defaulted,

1:46:57

it, it's not default not did.

1:46:58

We are able to see that pattern.

1:46:59

that basis we have model

1:47:01

so I just took some time

1:47:04

to explain the data to you.

1:47:05

But once you understand it,

1:47:07

we're going to do, that's it,

1:47:08

simple, you know.

1:47:10

C.S.B is shared with you.

1:47:11

Just take the data and build the model.

1:47:13

That's it.

1:47:13

I can guide you a little bit.

1:47:16

Alka say I can guide you just

1:47:17

one or two steps I can guide you.

1:47:19

So what I will do right now,

1:47:21

our data, let me share in my folder.

1:47:23

Just one second, go along a minute.

1:47:25

You can follow along with me.

1:47:26

You can follow along with me.

1:47:27

You can follow along with me.

1:47:29

But you will see the confidence you get, right?

1:47:33

That's the whole idea.

1:47:34

I mean, you'll get the confidence now.

1:47:38

Okay, we can actually solve some competition problems.

1:47:41

Now, we cannot be masters and exports in ML in just five days, right?

1:47:44

That's not expected.

1:47:46

That's unrealistic.

1:47:47

But the whole idea is to give me that confidence

1:47:49

that, that, we mean, we can't solve us.

1:47:52

But, but you're again, you're more than experiment

1:47:54

can, but it is just to give you that confidence.

1:47:57

Okay, so now,

1:47:59

So let's, let's take the data set right now.

1:48:03

You can, you can't as, as far as can do with us.

1:48:05

We can do along with me.

1:48:08

This is UCI credit, uh, UCI credit card.

1:48:11

That's, I'm sorry, let me just take the working directory.

1:48:15

This is important thing.

1:48:16

Working director, let me see that's set right now.

1:48:20

I hope you guys know it, right?

1:48:21

Working directly.

1:48:22

Kher, you're all right?

1:48:23

You're all right.

1:48:25

Uh, one thing, guys,

1:48:25

we're doing in collaboration.

1:48:26

Because most of you are doing on collab.

1:48:27

No point in confusing you, okay?

1:48:29

Let's go back to Collab because BS code may be a different thing.

1:48:33

Let's not, let's not get into this.

1:48:35

Let's go to Collab because everybody is doing on Collab.

1:48:38

It will make a light simple, okay?

1:48:40

So Collab, if you're if you're going to remember, your working directory is here.

1:48:44

Now, file here up upload here, okay?

1:48:47

Please keep that as the back of your mind.

1:48:48

You have to file here upload here.

1:48:50

You connect to the runtime and there is a small folder icon you will get,

1:48:55

and you simply upload your file here.

1:48:57

That's it.

1:48:59

So this UCI credit card CSV file is, you know here upload

1:49:05

that's it.

1:49:06

This is our folder, you can see.

1:49:08

And I will simply upload that UCI credit card CSV here.

1:49:12

That's it.

1:49:13

This is all that I have to do.

1:49:14

Or nothing to do.

1:49:15

That's it.

1:49:15

Once the file is uploaded,

1:49:17

now you can proceed along.

1:49:18

Connect, run time.

1:49:19

Connected to connect.

1:49:21

There's all right.

1:49:22

No problem.

1:49:23

Please run all this.

1:49:26

You can run all this.

1:49:29

And I can come all the way down.

1:49:32

And here we're just to add.

1:49:35

PD.

1:49:35

. read underscore CSV.

1:49:38

So here there's nothing to do

1:49:38

there.

1:49:39

Colab in, so in Collab in the collab in

1:49:40

so you can see I'm typing and it's able to

1:49:44

understand that probably I'm trying to read

1:49:46

UCI credit card CSV.

1:49:48

So there's nothing to do only, right?

1:49:49

In Collab.

1:49:51

So Gemini is too good.

1:49:52

It's just too good, actually.

1:49:55

Anyways, I'm not saying BS code is not good.

1:49:57

But we have there on extensions enable not able to.

1:49:59

So that's why I was not getting the assistance there.

1:50:02

So demo.

1:50:03

You can just quickly see the data.

1:50:05

Data what is my data set?

1:50:09

And just for simplicity, just bear with me on this one.

1:50:12

Again, we can get into the details that we

1:50:15

can get into the details, but just for the current data set,

1:50:17

please drop the sex education marriage columns.

1:50:19

This is drop and the reason is because

1:50:21

that real world use cases

1:50:23

may these columns can contribute bias.

1:50:27

So this is our understanding

1:50:29

things are no impact.

1:50:30

The concepts are all of the same.

1:50:31

But just for the example, I'm just saying

1:50:33

that you can drop these three columns.

1:50:35

ID to any way, you're drop

1:50:36

if you're ID say, so there is no relevance

1:50:39

for the ID column.

1:50:41

And what is the syntax for dropping?

1:50:44

Data frame.

1:50:44

Drop, what do you do?

1:50:46

X is equal to one.

1:50:48

X is equal to one is what you will do?

1:50:51

This is the first thing I will drop the ID column.

1:50:53

And again, what are the other columns I will drop?

1:50:56

This come list in list.

1:50:57

Okay, ID got here.

1:50:59

Next, sex got, marital status, what is that? Marriage?

1:51:07

And let me just give a comma.

1:51:11

And this is your last

1:51:13

I'm sorry, education and then marriage.

1:51:16

Okay, I mean, I mean,

1:51:16

maybe, any, any, order, you know, education and then comma marriage.

1:51:23

Okay, I'm just dropping these columns and trying to build the model,

1:51:25

that's it.

1:51:26

Okay?

1:51:26

This is your final data friend.

1:51:28

No, rocket science?

1:51:29

I'm just saying,

1:51:30

the ID hathed-do, because ID has nothing to do with the output.

1:51:32

Output, the default,

1:51:34

the customer defaulted or not going,

1:51:35

that's what do you know,

1:51:36

what's the idea to do?

1:51:38

So, and this is the problem is

1:51:40

that, like, let's gender,

1:51:41

now, if any male or

1:51:42

or female, what has that got to do

1:51:44

with a default thing?

1:51:46

So these kinds of columns can contribute

1:51:48

bias.

1:51:49

And believe it or not, there have been

1:51:50

lot of historical cases.

1:51:52

So, that's a

1:51:53

other thing is, but I can give you some

1:51:55

real case studies,

1:51:57

like J.P. Morgan. So J.P. Morgan had to, J.P. Morgan's credit model was found to be

1:52:04

biased against women, and they had to pay some $50 million to fine to, you know, like something of that sort.

1:52:12

You can ask you. You mean, you can actually read about it, you know, like there is a, so you can actually

1:52:20

see right now, J.P. Morgan has faced multiple lawsuits and regulatory complaints alleging gender and

1:52:25

racial bias against women, including

1:52:27

claims of care. It's a lot of HR. I was talking more about credit default

1:52:32

and loans. It was more from a more from a loan model. But yeah, I mean, there have been

1:52:40

documented cases like that. They've been documented cases where there was an album. Yeah,

1:52:44

you. Look at this. Very, very, very interesting. This is, this is the thing. Look at this.

1:52:51

A high earning woman would be denied a loan at a high rate not due to our finances.

1:52:57

earning high.

1:52:59

Finances don't know anything. But due to her gender bias data.

1:53:03

And this is a real issue that in 2009, US equal employment opportunity sued J.P. Morgan

1:53:09

alleging gender discrimination.

1:53:12

And like how these kinds of algorithmic biases happen.

1:53:18

And historical discrimination in lending, these all kinds of algorithmic biases happen. And historical discrimination in lending, these are issues.

1:53:22

So nowadays banks have adopted practices.

1:53:25

Nowadays, banks have adopted practices where they do not use these kinds of features.

1:53:30

We're like features on basis on loan aside not.

1:53:34

That they're male, female, he.

1:53:35

It's been married, it's not. We don't try to discriminate people on the basis of a pixie.

1:53:41

I mean, again, different societies are different, right?

1:53:44

If you go to European countries, there's marriage-caque-in-neying-in-neying-you-s-west-in-ne-he-you-S-me-me-

1:53:48

but if you go to some other countries, like, even if I take France.

1:53:54

I mean, I'm like, I mean, there's a country where there,

1:53:55

it's very open, right?

1:53:59

You look at the laws and the social laws of those countries.

1:54:01

So you're how, what is the point of these kinds of columns? Can you understand?

1:54:07

Especially if you're at MNC's social.

1:54:09

multinational banks, banks' operations across the world,

1:54:14

yeah, India society we can understand.

1:54:15

You can look at, I don't know, there can be patterns you can find out.

1:54:19

People who are single, people who are married, a patterns rea,

1:54:22

that's stability, whatever.

1:54:24

But you cannot take, if you're an MNC,

1:54:25

bank, you cannot take this model and run it in Europe.

1:54:28

Now, where France, Portugal, and this model will?

1:54:30

There, where there, single marriage, what concept is?

1:54:33

Make sense?

1:54:33

I mean, you have to understand, go to Middle East countries.

1:54:36

Like, it's very different in those places also, right?

1:54:38

So these are very real scenarios, and these are very sensitive issues.

1:54:41

So we usually try to avoid these kinds of, you know, features to build a model.

1:54:46

Okay?

1:54:47

This is a very long discussion.

1:54:48

For now, you please go and ignore these columns.

1:54:51

And then once this is done, what you can do?

1:54:54

You can go and please.

1:54:55

take this template.

1:54:59

Here from here we expect you, you can help you.

1:55:03

But from here onwards, I will expect people to do it, please.

1:55:07

So you please do it until here.

1:55:09

And then, all you have to do is, this one I will not ping you.

1:55:12

Okay, this one is expected that you will do.

1:55:14

That is, that is the thing.

1:55:15

I want everybody to contribute to this exercise.

1:55:18

Now you will have to take the data from here.

1:55:20

You have to here from here.

1:55:21

Now, what's to do it.

1:55:22

Now, do not do.

1:55:22

X, is Y, X, Y.

1:55:23

X, Y.

1:55:24

Take this.

1:55:25

thing, take the template from here.

1:55:29

You have your template already here.

1:55:31

You take the X, take the Y, separate it.

1:55:33

train test plate, logistic, bano, and then model.

1:55:35

That's it.

1:55:36

There's nothing to do here beyond this.

1:55:38

Only thing is up for pipeline ban on you.

1:55:39

That's the only thing that you will have to do.

1:55:43

Okay, I'm sure, like, if people have done it, you can let me know.

1:55:46

What is the train and test code you're getting?

1:55:48

Yeah, I think I've given people enough time.

1:55:51

Around 20, 25 minutes we have taken.

1:55:53

So that's okay.

1:55:54

Another 5, 10 minutes we can take.

1:55:55

And then,

1:55:55

we'll go to Confucian matrix.

1:56:00

Accuracy, 80.97%, Anjora's already pinged.

1:56:02

Anybody else?

1:56:03

Anybody else wants to let me know?

1:56:05

Just let me know the train accuracy, test accuracy.

1:56:08

FN, false negative, general, there's no.

1:56:09

No, we haven't said yet.

1:56:10

No, we haven't discussed Confucian matrix shortly.

1:56:14

But for now, you can just tell me what is the general scores you're getting.

1:56:17

What is the train accuracy you're getting and what is the test accuracy you're getting?

1:56:23

What is the train accuracy you're getting and what is the test accuracy you're getting?

1:56:24

getting and what is the test accuracy is going?

1:56:26

People can just try this out.

1:56:27

And please use this template.

1:56:29

You'll make your life easy for you.

1:56:32

I'll make your life easy for you.

1:56:33

Some, yeah, we up to pinged.

1:56:34

You're up, you can, just use the same template and do it.

1:56:39

Just change the column names at the top.

1:56:42

Oh, study hours distraction, huddered.

1:56:45

Incorporate our current data and just build it all with you.

1:56:49

Okay?

1:56:54

Thank you.

1:57:24

okay very good 80.9 3 80.9 percent okay okay okay thank you anjou

1:57:43

others everyone must do okay i have waited for everybody everyone must do this all if you please do

1:57:54

to try.

1:58:04

And there is a lot of depth in that accuracy numbers, okay?

1:58:09

I'll try, I'll cover that right at the end.

1:58:12

Okay, around 8.30 times, I'll cover, 10.30 times I'll cover that what?

1:58:15

we say here are 11s are, I'll come to that.

1:58:18

But upon out just the baseline model we are trying to build.

1:58:22

Okay, 80.9.

1:58:23

So it's a.

1:58:24

It's a reason of the good fit we can say.

1:58:26

So we can potentially try to make it better.

1:58:28

Anjur, what you can do is a gradient boosting like to, see if it's becoming better.

1:58:32

So, first, logistics said, this is what you're getting.

1:58:35

Then there.

1:58:35

Gradient boosting in again, you can check.

1:58:37

Are we getting a marginal improvement on this same dataset?

1:58:43

Others, what are you getting?

1:58:45

Let me know.

1:58:46

Let me wait for another five more minutes, max.

1:58:48

Then I will discuss.

1:58:54

Okay, very nice. Abhichita has reported in a different answer.

1:58:59

But different can be no problem, guys.

1:59:01

And the reason is because, uh, what is the thing due to privacy issue?

1:59:08

Oh, chat copy not?

1:59:10

Oh, I'm so sorry, guys.

1:59:13

Chat, how copy not copy not?

1:59:15

One second.

1:59:16

No, copy who are, I mean, I'm able to copy the chats from Zoom.

1:59:20

As a Mac man.

1:59:21

And the Macs, I don't think it's a zoom setting.

1:59:23

I don't think so, Amit.

1:59:27

Not it's not so sorry.

1:59:29

I think we're too sorry. I think we've too disabled here.

1:59:31

Let me see.

1:59:33

But I am able to copy.

1:59:34

I'm to copy.

1:59:34

I'm so copy can't.

1:59:35

You don't copy access.

1:59:37

This is new.

1:59:38

I'm not trying to go.

1:59:41

That's interesting.

1:59:42

So,

1:59:42

never any session in a chat copy.

1:59:45

No, not a single class.

1:59:47

What the?

1:59:49

Okay, okay.

1:59:50

Okay.

1:59:53

Okay, that's interesting.

1:59:55

I can check with the team later.

1:59:57

Yeah, I'm the, it's not a big issue.

1:59:59

Abh Kali, it's not a issue not.

2:0:01

But I can check that for the next class,

2:0:03

okay?

2:0:03

Yeah, I was not aware of this.

2:0:04

Thanks for letting me know.

2:0:06

Usually, chat copy should.

2:0:07

I think, uh,

2:0:10

okay, we'll see.

2:0:11

We'll see.

2:0:12

I'll check.

2:0:12

I'll check with the team later.

2:0:14

Like, I think there was be some host permissions,

2:0:17

okay?

2:0:17

Which host permission will,

2:0:18

that's for that for sure.

2:0:19

But we can check.

2:0:20

Don't worry.

2:0:21

We can check.

2:0:23

Yeah, I will, I will 100% get this sorted for you next class.

2:0:27

Okay.

2:0:27

Yeah.

2:0:29

Okay.

2:0:30

Ah,

2:0:30

how many options are.

2:0:31

Gimini in picture,

2:0:33

picture,

2:0:33

you,

2:0:33

you'll do you're just giving a workaround.

2:0:36

That's a better thing than chat rate.

2:0:39

Even if your sniffing tool doesn't work,

2:0:40

you take your phone out, take a Gemini snap.

2:0:43

Asked Gemini to convert that to text and we'll do everything for you.

2:0:46

Anyways, that's just a workaround.

2:0:48

Yeah, but that doesn't, that's not the solution for this.

2:0:50

I'll check with the team, okay?

2:0:51

Yeah.

2:0:53

Okay.

2:0:54

Okay.

2:0:55

I'll know this.

2:0:57

Okay.

2:0:58

Let's go.

2:1:05

Thank you.

2:1:35

Can we, okay, okay, okay, uh, okay, uh, okay, uh, guys, uh, we need to continue now, everybody, let me know,

2:1:54

Pranger has also pinged.

2:1:55

See, answers are a little different.

2:1:56

I'll tell you, I'll explain to you answers different few.

2:1:59

Answers different is.

2:2:00

Answers different is because people are taking different train test splits.

2:2:02

That's the reason flying a ready, okay?

2:2:04

So don't be worried about that.

2:2:05

So if you're taking a different train data test data, then answers different are

2:2:08

siky.

2:2:09

So don't worry about that.

2:2:10

It's not as if you're doing something wrong, okay?

2:2:12

So answers, people are different.

2:2:13

It doesn't mean you're doing it wrong.

2:2:14

Answers different just means that you're taking a different train data and test data.

2:2:18

Okay.

2:2:19

Others, let me, let me hear from more folks.

2:2:22

Come on, guys, this is a simple one, train test.

2:2:26

dot fit, dot score.

2:2:27

There's nothing to do in this exercise.

2:2:29

I'm expecting everybody to complete quickly.

2:2:32

We are looking to learn.

2:2:34

We are looking to learn Gen AI. We shouldn't be stuck on this, right?

2:2:37

This is solved thing, right?

2:2:39

30-40-second thing is.

2:2:41

So you should all be confident and complete, huh?

2:2:45

Okay, Tisha is saying same train test accuracy, okay?

2:2:50

Okay.

2:2:51

Tricia, just ensure that you're calculating train and test separately.

2:2:55

Because numbers are exactly same.

2:2:57

So just ensure that it is the same.

2:2:59

But I hope it is train and test separate only, right?

2:3:03

Okay, so I can also talk about it, guys.

2:3:10

So template will be very similar, as I told you.

2:3:13

Very similar template I will be taking right now.

2:3:16

So actually here our cancer in here, so there's already done.

2:3:20

So I'm going to take it from here.

2:3:22

Maybe simplify that a little bit for all of you.

2:3:26

First, we have to split the data into X and Y.

2:3:32

what is X and what is Y?

2:3:34

This is the same way we will do the template, right?

2:3:36

So X is what is.

2:3:42

So Gemini is already doing this for me.

2:3:44

See, I'm starting to type on Collab.

2:3:46

The moment I start typing on Collab, everything is happening.

2:3:49

So Demo. Drop, default payment text 1, X is equal to 1.

2:3:52

It is already giving me the code.

2:3:54

This go drop.

2:3:55

Baki, joe be columns that is actually my X.

2:3:58

And now you can say, what is Y?

2:4:00

Why is default payment next month?

2:4:02

Germany is doing that for me.

2:4:04

Then, train test lit and then we are doing the pipeline.

2:4:08

We already talked about what is pipeline.

2:4:10

So first I will do min-max scale and then I will do logistics.

2:4:14

First, I will scale my data between a zero to one scale.

2:4:18

Then we'll logistic are.

2:4:20

Anjur, it's a default one.

2:4:21

No, no, you're going to do your default.

2:4:23

It will come, it, or never, it depends on the port on.

2:4:26

That is, that is Gemini's intelligence.

2:4:28

You just enter to, so that is, that is a default one.

2:4:32

Sometimes it might come.

2:4:34

You can do one more thing.

2:4:35

You can actually try entering a comment.

2:4:37

You can comment enters can fit and fit a model.

2:4:41

You can try to try.

2:4:43

Comment say it can actually do a comment and hit enter.

2:4:47

Neither the best way to do it is obviously you can do generate with AI.

2:4:50

This is Germany with any ways open on the site, which I taught you last time.

2:4:55

So train test split, pipeline, dot fit.

2:4:58

This is your dot fit and your course had got got fit.

2:5:02

this looks too complex.

2:5:04

There's too much of this print and formatting and all that.

2:5:07

So if you want to remove the complexity,

2:5:10

okay.

2:5:10

All complexity remove, let's keep it simple.

2:5:13

Training accuracy.

2:5:16

And this is your test accuracy.

2:5:18

So Gemini will back will be our.

2:5:20

Okay, okay.

2:5:21

Okay, it's got.

2:5:21

Jemini has done everything for me.

2:5:23

Pipeline.

2:5:23

Dot score X-J-Jane into 100 or testing accuracy

2:5:27

had got pipeline.

2:5:27

Dot score, X-Test, Y-Tase into 100.

2:5:30

That's it.

2:5:31

Completed.

2:5:32

Okay.

2:5:34

Or 100 be up to, okay, if you want to show it, it's fine.

2:5:37

If you don't want to show it, just remove it.

2:5:39

You get the train and test data, train and test codes.

2:5:42

So let's build the model now, and you're getting 80.93% and 80.9% in value.

2:5:48

This is the baseline model that I'm getting right now using logistics.

2:5:52

This was the expectation that I had.

2:5:54

How much time did it takes?

2:5:56

So I did explain that by it took some time, but it's hardly 20 seconds, okay?

2:6:01

And now you can.

2:6:02

We can try out with a logistic model, with a different algorithm.

2:6:08

We have logistics from.

2:6:09

We can experiment the same thing using something called gradient boosting.

2:6:16

So this is we can do with gradient boosting.

2:6:18

So you can try it.

2:6:20

You can try now using a different algorithm what kind of results we are getting.

2:6:25

So this is the way how you will do it.

2:6:27

And you'll be surprised to know that no matter what problem you take up in the real world,

2:6:31

if you will be the real world problems you'll be following.

2:6:37

You have to identify X, what, Y, what are, fit, predict, and get the results.

2:6:42

Okay, so prediction. So prediction, how can we?

2:6:44

Now, now you're pipeline.

2:6:46

So, when you're pipeline so, what we do?

2:6:50

We do pipeline.

2:6:51

If directly modeled, then we do model.

2:6:53

So we do model.fit, model.

2:6:55

And if we're pipeline, we do pipeline.

2:6:56

We do pipeline. Fit, pipeline. Pideline.

2:6:59

predict. So here we will take make dot pipeline.

2:7:03

Do two things we've seen.

2:7:04

Predict proba. In the class, this was a learning right?

2:7:07

We did predict proba. So let's let's predict proba.

2:7:10

This was learning number one and learning number two was

2:7:15

dot predict. That's it.

2:7:19

So this is gone to look at last.

2:7:20

So this is what will. There are two classes we have zero class one class.

2:7:26

So we'll be able to find out that prediction probability.

2:7:29

What is what is?

2:7:30

Uh, uh, okay, actually, predict proa, direct object, you're not. That's a different issue, actually.

2:7:36

So this is directly you, you can't this. So you're directly, you're not like this in. So

2:7:39

it's, okay. So it's, it's actually a other type is. Sorry, sorry, sorry, my mistake. Actually,

2:7:44

directly, your predict function, predict, predict, predict, predict, predict, proa. So this,

2:7:49

this, this, you cannot directly do a predict, predict, uh, predict, predict, just to clarify.

2:7:53

So directly, uh, predict proga will actually not work. There's a, there's a different workaround

2:7:57

for it. Okay. So, so, what is, what is a, so what is a,

2:7:59

you can do. Okay, to this for, uh, up, pipeline aspects, okay, to get into the other aspect

2:8:06

for explaining that. Because this is the pipeline, right? So pipeline, so whenever you do this with

2:8:16

a pipeline, so directly this particular thing will not come, okay? If we want to scale just some

2:8:21

columns, then it doesn't work. I try, no, no, this is a way to do it, just to clarify. There is a way to do it.

2:8:25

There is a way to do it. So you can actually do it. So you can actually do.

2:8:29

If you want to scale only some columns, then you can take only that particular, uh, section of

2:8:33

columns and you can build the model. You can absolutely do that. You can only take that particular

2:8:37

section of columns and build the model. So you can absolutely do that.

2:8:43

But then you can, then you then you'll have to take the rest of the columns and you'll have to

2:8:48

concatenate it. But generally it is not a good practice. It is usually not a good practice just to clarify.

2:8:55

Okay, so just to clarify, it is usually not a very good practice. You will have to clarify. You will have to

2:8:59

If you want to do this thing, you usually want to go back and, like, you want to build it on the whole thing.

2:9:07

It's not a good practice to do it only on, uh, uh, uh, encoded columns are no, no, no, no, no, no, no,

2:9:15

encoded columns must not be scaled. So then the approach is that you encoded column's off. I think you

2:9:20

must have, you must have that categorical location encode key. So, okay, very good.

2:9:24

Now, you're encoded columns, it's not a lot of them. You know, uh, scaled column's it.

2:9:29

go up scale and then both of then last in concatenate for both.

2:9:34

Two loco last in you have concatenate that's the concept.

2:9:37

At the end of it all, you can catenate the two columns.

2:9:42

That is the idea.

2:9:44

And coded, keep it as it is.

2:9:47

Scale, the data is, keep it as it is.

2:9:49

That is the whole scale data.

2:9:50

And finally you go back and work this out.

2:9:54

That's the way to look at it.

2:9:59

So now we will go back and quickly, uh, see the predict proba part right now.

2:10:11

Predick proba, how we are actually getting the probability values you can see.

2:10:16

So X test, you can see right now, this is class zero and this is class one. So class zero is

2:10:22

class zero is basically the probability of default. And this is probability of, sorry, probability

2:10:27

of not default, probability of default. So for every customer we are able to see,

2:10:32

what is the probability the customer will default and what is the probability customer will not

2:10:35

default? So 22%, 50% to come here, so model has predicted zero.

2:10:42

16% 50% is the model has predicted zero. So you can see the issue of threshold.

2:10:47

If we're default thresholds say going, then what will happen here is,

2:10:52

all we're not defaulted classify can. But actually, it's a very big issue is. If this person,

2:10:57

is a 29% chance of default.

2:11:00

Then 29% chance of default is a big deal for the bank.

2:11:03

Mani, it's a credit card.

2:11:05

You know, person might actually run away with the money.

2:11:08

So 29% probability of default is extremely high.

2:11:11

That is a red flag.

2:11:13

But we're not classifying that person to be a default. So we are not classifying that person

2:11:16

to be a default.

2:11:17

And we're saying, okay, person will not default.

2:11:19

So please keep the card on.

2:11:20

Are you seeing the real issue now?

2:11:21

To threshold, you manage them here.

2:11:23

And now in these kinds of cases, what you can do?

2:11:25

You can modify the threshold.

2:11:27

You can write a set.

2:11:27

separate if else statement and you can say that if the predict proba is more than this, then it is

2:11:33

a default, else not default. So this is your concept.

2:11:38

Okay, so same to same. We take the data, we take the X, we take the Y, train test plate, build the pipeline, do the dot fit, do the predict, do the predict proffer.

2:11:47

So complete end to end what we saw.

2:11:50

Now we will come back to our final topic, which is Confucian matrix.

2:11:56

Confucian matrix is the way to evaluate.

2:11:57

the model. So what is Confucian matrix? It is the way to evaluate the model. We are trying

2:12:03

to evaluate the model. And before I discuss this with all of you, please give it a glance all of you.

2:12:12

This is where we have kind of very neatly simulated the idea of a Confucian matrix. So Confucian

2:12:18

matrix is a way to evaluate the model. A model to evaluate perfectly. We take the data, we do the fit.

2:12:27

in Y train, X test, Y test, we'll let them fit. And then we try to evaluate the model

2:12:35

on the test data. So Confucian matrix is useful for model evaluation. And please remember,

2:12:42

these are only applicable for classification. So, ah, we've made jove concerns discussed

2:12:47

everything is similar. Two core things. Not predict proa, probabilities are only applicable for classification

2:12:55

or for regression. And this particular thing,

2:12:57

is only applicable for classification or not for regression.

2:13:00

So here we are trying to understand how did the model perform.

2:13:06

Model, what we've made. So model made. So model in predict kind of what's, actual

2:13:10

something. Model in predict what's actual question. So how do we go back and predict how the model actually

2:13:15

performed? So that's the problem that we are particularly trying to solve.

2:13:20

Okay, so everybody please give it a glance, all of you.

2:13:24

Please check. Then we'll discuss.

2:13:27

Please check across. And just to clarify, what is negative and what is positive,

2:13:36

just each thing I'm about this. What is negative, what is positive? Whatever you are trying to predict.

2:13:41

Abhi, we have a credit default example here. So we can put a story and we can discuss with that only.

2:13:46

So we can say that, you know, we can, we can say that positive is nothing but default.

2:13:53

But one plus is actually default class.

2:13:55

which positive class is nothing but not default class, you can negative class. So one

2:14:02

you defaulted and zero must have you not defaulted. But the one means default is true. You defaulted.

2:14:10

And actual one matter of you defaulted. And here, you defaulted. And here,

2:14:14

you're not defaulted. Everybody please continue on now. Just give it a glance and I'll explain.

2:14:22

Free through, free through it all. Take some time.

2:14:25

to it.

2:14:55

Thank you.

2:15:25

Thank you.

2:15:55

Thank you.

2:16:25

I will come to that, I'll come to that. I'll come to that.

2:16:30

T.P. Let me explain. I'll take up your question. Once I explain, I'll take up your question. Okay. I'll take up your question.

2:16:34

Default and actually, I'll come to that. Hold on. Let me explain that. I'll take it up.

2:16:38

So first of all, guys, as I told you, first we take the data, we build the model. This is used for model evaluation.

2:16:45

All this while, we were covering only the concept of accuracy. We were only trying to discuss accuracy at a high level.

2:16:52

The accuracy care.

2:16:54

What is the number?

2:16:55

meaning of accuracy. That is what we were covering at a very high level. The model predicted

2:17:00

it now, actually itna, and that's how we understood the accuracy as a whole. Okay, so we looked

2:17:07

at accuracy as a whole. Now we are trying to understand what are the specific areas the model

2:17:12

is making mistakes in. So you can see there is something called true positive. What is true

2:17:18

positive? True positive means modern predicted positive actually is also positive.

2:17:25

So, so this is the way to understand true positive.

2:17:29

True positive to have a message that what's the model predicted.

2:17:34

So, subsequently, a Confucian matrix is.

2:17:37

Along the columns, you always have the predictions.

2:17:40

Along the rows, you always have the actuals.

2:17:43

Just keep this at the back of your mind.

2:17:45

Along the columns predicted, along the rows, you have actuals.

2:17:50

Okay?

2:17:52

So first things first, we have true positive.

2:17:55

Right?

2:17:55

model predicted positive and the reality was and the prediction is true.

2:18:05

That is the way to look at it.

2:18:06

I mean, the model predicted positive and the prediction was true.

2:18:12

So actually is also positive.

2:18:15

As I understand.

2:18:16

That's how much.

2:18:16

The model predicted positive and the prediction was true.

2:18:20

Because remember, this is something that you will prepare on the basis of your test.

2:18:25

data mock question paper. Whatever model you have built, you are going to

2:18:31

evaluate that particular model against the mock question paper. That is what you will do, right?

2:18:36

You are going to evaluate this particular model against your mock question paper. That is

2:18:40

what you will do. So now you will basically evaluate this particular model against your mock question

2:18:47

paper. That's the way how we will work it out.

2:18:55

So, model predicted positive and the prediction was true.

2:19:07

So, the actual is also positive.

2:19:09

So this is model predicted default actually also your default.

2:19:12

So all good.

2:19:14

What is true negative?

2:19:15

Model predicted negative.

2:19:17

And the prediction was true.

2:19:21

So that means model predicted you are not a default and actually also you are not a

2:19:25

defaulter. That is what we call a true negative case.

2:19:31

And these two taken together are what we refer to as correct predictions.

2:19:35

So TN and TP taken together are what is referred to as correct prediction.

2:19:38

The model is making correct predictions here.

2:19:41

If you combine TN and TP, this is what will tell you the total number of correct predictions.

2:19:48

So the overall number of correct predictions is nothing but true negatives plus true positives.

2:19:54

That is how we define the third.

2:19:55

total number of correct predictions.

2:19:57

How many true negatives plus how many true positives?

2:20:02

On along the diagonals is where the model is making mistakes.

2:20:07

This is where the alarm bells will start to ring because this is where the model is making

2:20:11

mistakes.

2:20:12

Whatever model we have built, when we are evaluating that model against the test data,

2:20:17

here are the mistakes that are meeting.

2:20:19

So we first, this is how can't say false negative,

2:20:21

I mean, model predicted negative and the prediction is false.

2:20:27

I mean actually a positive.

2:20:30

But the model predicted negative, but the prediction was false, actual was positive.

2:20:36

And you can see from the Confucian matrix perspective also, model predicted negative, but actually is positive.

2:20:44

And I'm sure you, you realize that false negative is a dangerous situation.

2:20:48

It's a missed reduction.

2:20:50

And if you talk about the I.

2:20:51

idea of a credit default prediction problem, the one that we discussed a while back.

2:20:56

This is a very, very dangerous situation.

2:20:57

Because false negative, the model has predicted person defaulted and not.

2:21:03

So bank has allowed it, but the person is actually a defaulted.

2:21:06

So you miss defaulting customers.

2:21:09

It's a big business loss for the bank.

2:21:11

So FN is very, very costly right now.

2:21:14

And this thing you have to business concept of itself as far as to

2:21:17

say that which error is costly, which is important to analyze.

2:21:21

So these things you will have to do from a business perspective.

2:21:24

You will have to use your own intelligence and you will have to figure out that which error is more costly.

2:21:28

So this case, my fn is very costly.

2:21:31

And what is FP?

2:21:32

Final one?

2:21:33

Model predicted positive and the prediction is false.

2:21:38

I mean negative prediction, actual negative.

2:21:40

But the model positive predict here, but actually one negative bias.

2:21:45

And this is like a false alarm, not a moderate default predict here, but actually more default

2:21:49

and negate.

2:21:49

But this is acceptable.

2:21:50

Right.

2:21:51

It happens all the.

2:21:51

time, right? False positive is like a false alarm.

2:21:53

If you're a credit default to as far as a transaction fraud case and so, it happens all the time, right?

2:21:58

This is like a safe guard.

2:22:01

I mean, it's a safe thing. It's also an error, but it's, it's better than FN.

2:22:05

FN is a very bad thing.

2:22:06

FN, M is a very bad thing. FN, what I mean, customer is actually a defaulter, but our system in us to lagging

2:22:12

not. That is an extremely dangerous situation.

2:22:15

FN is unacceptable.

2:22:17

But FP is okay.

2:22:20

FP's example.

2:22:21

case there will be, imagine, uh, uh, fatal for customer, maybe absolutely right,

2:22:26

you know, but FP is basically a very bad experience for the customer.

2:22:30

Mania, you go to the restaurant, you want to swipe your credit card.

2:22:33

Uh, a chance, you find the card is blocked. That is an FP case.

2:22:36

You want you, you, you're taking out your card to pay the restaurant bill, right?

2:22:40

You have such a high-end credit card or card work function not here. That is a false positive case.

2:22:44

So the bank somehow thought that you are, yes, the bank somehow thought that, okay, you are likely to be a

2:22:50

defaulter.

2:22:51

So the bank has proactively blocked your car, but you are actually a good customer.

2:22:56

Bank did a mistake for security card blocked here, but that is a impact on the customer experience.

2:23:03

So this can't be solutions.

2:23:05

Real world in the real world, what we'd do, the super premium cards are, so there are different, different models that these banks,

2:23:12

and all, they are built for different variants of credit cards.

2:23:15

This actually happens, you know, like, this is the way it actually is getting done.

2:23:21

Again, the workflow would be you take the data, you build the model, you evaluate the model.

2:23:25

You have overall accuracy.

2:23:27

That you'll see how the model is performing, like what we did here.

2:23:30

We got 80%, 81%, right?

2:23:32

That's after the Confucian matrix, look.

2:23:35

And Confucian matrix, you have to, you know, in a detail level in summary, how the model is performing.

2:23:40

Where is the model specifically making mistakes?

2:23:42

And what are our focus areas?

2:23:45

So, like, credit card industry for, FN is very, very costly.

2:23:48

We cannot afford false negatives.

2:23:51

So, and this is where the next set of our efforts will start.

2:23:55

So now we will try to do whatever it takes to reduce the number of false negatives.

2:24:00

So now we, we have to reduce the false negatives.

2:24:02

What can we do to reduce the, so what can be, what can we go back and do to, you know, reduce the number of false negatives?

2:24:10

That's the, that's the problem.

2:24:15

Uh-huh. Uh-huh. Very nice, very nice.

2:24:19

1079.

2:24:19

line. Hey, false negative is not false alarm. No, no, no, no, no, false negative is not false alarm.

2:24:24

Uh, that's the wrong. For false negative would be like, uh, this one. False alarm is this one,

2:24:29

actually. That's the false alarm. Uh, okay? False alarm means that you wrongly predicted that person

2:24:34

to be a default. False alarm will be FP here. Okay. Okay. Okay. Let's move on. Let us look at

2:24:45

the industry context. I hope everybody is clear. Everybody understood this and, uh, this is the,

2:24:49

structure of your confusion matrix. Again, I repeat, guys, this is only for binary.

2:24:54

Please do not be confused about multi-class. Multiclass. We've never discussed

2:24:57

not. I know some of you might have that question, that, sir,

2:25:00

now we're discussing. So, what if there are three or four more classes? So then what will

2:25:05

be? So, then something more will be. So right now, this is two cross two.

2:25:09

If you, if you're two-classes, if three classes, four classes, then confucian matrix

2:25:13

will be ready. What will happen, we will see. Okay, that we will discuss. This is only

2:25:17

only restricted to binary classification.

2:25:19

this current module. You will see multic. I'll show a use case later. So 0-1, 0-1. And if you just

2:25:26

quickly go back to the case studies we did already, first, the pass-fail-fail-va-go-gia. And if you see,

2:25:33

this is a simple way you can build a Confucian matrix. There it is. So you take the data,

2:25:39

you build the model, dot-fit-koro, you, dot-predictor. You get the predictions will get. You get

2:25:44

the predictions when you do dot-predict. And the confusion matrix is nothing but a plot between

2:25:49

actual and predicted. That's it. The Confucian matrix is nothing but a simple plot between

2:25:55

actual and predicted. That is what the Confucian matrix is. Actual to predicted comparison.

2:26:02

And the moment I do that, you see this is what we end up getting. Same story as we discussed before.

2:26:09

Yeah, because zero-ho-go-one-one-one-go-gia. False-negative. Same story. So we can do the Confucian matrix for

2:26:14

our current exercise also. No problem. Very simple. If you think all this code is too difficult,

2:26:19

we can write it from scratch just to you know make you more confident

2:26:24

this one we did right we did the whole thing from scratch right we did this we built the model we

2:26:30

calculated the scores all this we did and finally the last part i will show you how to

2:26:35

build the build the well if i write it this where jemini only will build it for me i don't think i

2:26:44

need to do anything but that's okay let's let's let let us allow jemini to do it for us so

2:26:49

pipeline hey dot predict x test we will do and we will get the predictions okay we will call

2:26:55

it predictions let's call it simple predictions and then this is nothing but predictions

2:26:59

and actuals there is the confusion matrix and we can display this on it we can actually

2:27:05

print it out we can print the confusion matrix okay everyone can see this this is our

2:27:11

confusion matrix and i think this is exactly what i think the uh we can't take actually uh

2:27:19

on chat something very similar we are getting so let us let us let us see this let's

2:27:25

quickly understand from this uh code as well what we are doing so we've got the uh test data

2:27:30

and on the test data we are doing the predictions and we have the uh we have the actuals

2:27:35

and the confusion matrix is nothing but a uh a comparison of the predicted values

2:27:39

with the actual values okay and if i just have to go and i show you exactly uh

2:27:44

what we did in the class today this is how we discussed right

2:27:49

all of you recall so there goes the predicted and there goes the actuals.

2:27:56

You have your predictions. Sorry.

2:27:59

Your predictions have your predictions are here.

2:28:08

Your actuals.

2:28:13

So this are the numbers, right? So this is your TP.

2:28:17

Pro positive.

2:28:18

This is your 01.

2:28:19

here for zero one right everyone's clear so model predicted zero actually zero two positive model

2:28:24

predicted uh sorry model model predicted one actually one two positive model predicted zero actually

2:28:29

zero two negative model predicted zero actually one false negative this is fn fn

2:28:36

fn means model predicted you will not default but actually will default so this is a very

2:28:42

dangerous situation so our model is actually very bad and you get the ideas you start to get the

2:28:47

idea now. Although accuracy was 80%, accuracy is actually not giving us a true picture.

2:28:53

Accuracy is not giving us a true picture. Now that we are seeing the confusion matrix, now we get a better

2:28:58

understanding as to where the model is actually failing. So the accuracy is, that

2:29:02

we're just seeing that we're all over all it is 80% accurate. But the moment you start

2:29:10

looking at false negative, you start to realize how dangerous this model is.

2:29:17

And everything has to be quantified. Machine learning, everything

2:29:20

you have to quantify. It's not that we've made the model

2:29:22

we've made, accuracy, we've seen 60% 70%.

2:29:25

What's the meaning? What's what actually happens in industry, you know?

2:29:30

Industry we actually try to estimate the value of a false negative.

2:29:34

We look at historical defaulted data and we see that on an average

2:29:37

how defaults are, per transaction, how defaults are.

2:29:40

If a customer defaulted, then on an average, how defaulted amount would.

2:29:44

I mean, if any, a $50,000 defaulted defaulted or $1,000 defaulted,000,000,000.

2:29:47

defaulted. So one false negative, that's a customer. So 1,00026 false negative,

2:29:53

that 1,00026 much customers we missed. But for the bank, they will estimate their revenue loss.

2:29:59

So there is a real, you know, business context. And machine learning is not just opening Python and

2:30:04

typing code. Machine learning is a lot about, you know, understanding the business, understanding

2:30:08

the context, the domain. Everything you have to be that business-related. That's false-negative,

2:30:14

actually business is a loss.

2:30:16

If it's a credit card, then it's a credit card for credit card for loss.

2:30:19

So you, that's the way, dollar value, rupee value, estimate.

2:30:23

That's the way how you should look at things going forward.

2:30:26

So next time you say, I got a model with 90% accuracy. It actually means nothing.

2:30:30

Ultimately, your errors, what is the matter is, what means what is, business meaning

2:30:34

that is what you need to present.

2:30:40

Okay, everybody. So this is the basic confusion matrix.

2:30:44

right now. And now we will, uh, once a second, where is that? And now this has to be improved,

2:30:50

right? This can be improved. Over time, we can improve. And this is exactly what I was talking about.

2:30:55

Age go. Go ahead and we're what we do, we're different, different algos use

2:30:58

and we different hyper parameters use. We're different models

2:31:01

and we try to make the, you know, make this process a little better. So this is what we try to do

2:31:07

over a period of time. As a mania, here here we're gradient boosting as an example. I'll just show you. This is just a

2:31:13

just the last part I'll try to show you. Just to just to iterate and and show you I can do a

2:31:17

gradient boosting classifier. We've already seen this right. And I will simply instantiate

2:31:24

gradient boosting here. And all that we are trying to do now is to see whether using gradient

2:31:29

boosting I can get a slightly better quality model. That is it. That is all that I'm trying to

2:31:33

demonstrate right now. So yeah, we have gradient boosting used to false negative for too. Let us see that

2:31:39

intuitively. Again, we need to iterate a little for this, but we can check it up at a basic level.

2:31:43

It's a little time will be because there are 30,000 rows of data. It's a massive data set.

2:31:47

It's a very, very big data set, but we can check it up.

2:31:51

So you will also start to get a feel of real ML. So this

2:31:54

even time looks a more, but you can see. Again, it's a basic demo.

2:31:57

This is a quite basic demo. But you're at a basic level,

2:32:00

that you compare to logistic, 80%, 80% gradient in that

2:32:04

there's a little improvement has. We can make it even better.

2:32:07

There's more improvement has. And also, particularly, if you

2:32:10

look, so a little reduction in. And this is exactly. And this is exactly.

2:32:13

is what we try to do in ML. We try to, you know, we try different algos and we try to, you know,

2:32:18

make a better model. And we're more better model by, or we're overal accuracy increase

2:32:23

or then, the important error say, it's reduced. And here on important error,

2:32:27

means false negative. That we've reduced. So, we're a lot of achievement. And this is actually

2:32:33

what we try to do, you know, because like, it is not just reducing 200 FNs. It is actually reducing

2:32:38

what? I told you, right? It is reducing our losses by 200 such defaulters.

2:32:43

Those were defaulted. Every defaulter is like a lack loss. The bank's incurs. It's a huge amount of money.

2:32:49

We're talking about crores that you've saved. So you've made this model

2:32:53

for bank for bank to manage to save crores of the piece. You see the real business repercussion,

2:32:58

actually, how these things actually help.

2:33:02

So final thing, this is the last piece that I will talk about, guys. Just some couple of use cases

2:33:07

where we talk about these false negatives, false positives. This industry context

2:33:12

what? We talked about false negative already. So loan approval for what

2:33:17

is? False negative, I mean, right? False negative, but a model predicted, you will not,

2:33:24

model predicted, like, the loan will not be approved. But actually, like, it's a good customer.

2:33:33

So false negative is that particular context. So disease screening maybe, you have

2:33:39

you know, disease winning, this is like diabetes prediction.

2:33:45

If you're about cancer detection, diabetes detection, this is a very good use case. So

2:33:51

model predicted that the person is not diabetic, false negative, but not diabetic or not cancer.

2:33:58

Model predicted you don't have cancer, but in reality you do. So sending a very sick patient

2:34:04

home unchecked, it's a catastrophic life-threatening error. We talked about it. So false negative is very

2:34:08

costly for medical diagnostics where you're trying to use machine learning to predict some

2:34:13

disease. But false, positive is actually okay. If you're a disease-wala use case, so FP is fine.

2:34:19

And FP happens all the time. Doctors often make guesses while treating a patient.

2:34:25

If you're a patient to treat, then guesswork is normal. Guesswork on. So doctor will try to predict

2:34:30

that maybe you have this disease. You have a shy-a-medical condition, shy-de-a-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-d-dise-ha.

2:34:35

. But in reality, you don't. So that is, happens.

2:34:38

but that is still okay. It's not a big deal.

2:34:42

False alarms is not a big deal, but FN is catastrophic.

2:34:45

But still, you might fall sick.

2:34:47

Galat test, diagnosis here.

2:34:51

So these are some applications. And again, your business context is dependent on.

2:34:55

Depending on different business context, you will have to see which one works, which one doesn't work.

2:35:00

And finally, we have, we have a last use case.

2:35:02

This is not like a very difficult problem.

2:35:06

So this is a simple sort of.

2:35:08

Cancer data set we have this go breaked. Same to same thing. Nothing is new here.

2:35:14

So we are trying to look at the different features of the person.

2:35:17

And we are trying to predict whether the person is suffering from cancer or not cancer.

2:35:22

So this basically your cancer data set. So we've got cancer data set. And you can't see how your data is

2:35:27

data is. This is now the data is given. It's a it's an in-built data set. And we have simply

2:35:34

separated what is the X and what is the Y.

2:35:37

So we are trying to.

2:35:38

to predict cancer, whether the person is suffering from benign or malignant cancer,

2:35:43

zero or one. That is what we are trying to do. And this is how we are building the model.

2:35:48

This is same thing. False, negative, false, positive in them. You can see it. You can see it last

2:35:51

time. Okay. Okay. Yeah. So this is pretty much what we have for today. And again, I think

2:35:58

multi-class quality thing I'm taking in the next session. But the whole objective of today's

2:36:03

session was to clarify the flow, kind of tell you how.

2:36:08

how similar the flow is compared to regression. Regression, as we did

2:36:12

dot fit, dot predict. Same thing. And two important new learnings.

2:36:20

One, the algorithm side, say, logistic and gradient boosting classifier, we have two things used

2:36:24

here. Second thing, dot predict proba, we've made a new thing. Dot predict proba,

2:36:29

and thresholds, 50% threshold concept. That is new for classification. And third thing that is new for

2:36:34

classification is confusion metrics. So these were the three key new learning.

2:36:38

in the class today. Okay, with respect to binary. Okay. So next session will continue on

2:36:44

with classification. We will continue on with classification. And obviously I will

2:36:47

look forward to take any questions. But I hope everybody understood all of you followed along.

2:36:52

Do let me know. Everybody followed it. Okay. And also make sure that you continue working on these

2:36:58

case studies, guys. This will be very good for your confidence. Okay. So I have uploaded the

2:37:04

revised file with all of you on the drive. You can take it from here.

2:37:08

So all the stuff is already done here. You can take it. Yeah.

2:37:18

Okay. Wonderful. Any questions anybody wants to ask? All good. We have the quiz today also. So Arsita,

2:37:27

if you want to conduct the quiz, you can. So in the meantime, I'm here. If people want to conduct, ask me some

2:37:32

questions, I can take it up as you're answering the quiz. I think the quiz will be easy today.

2:37:36

We'll probably follow because not many.

2:37:38

new things okay yeah so do let me know if there anybody anybody wants to ask any questions

2:37:43

then really thank you very much for the wonderful session students

2:37:51

we will continue with our quest today the poll is already like you can fill that in

2:38:01

we're completing only today that's very nice that's very nice actually

2:38:08

any questions guys as you can say that coding us not much focused

2:38:20

you've got interviews are changing in a big way you know we have to come out of that mindset

2:38:25

we will not believe how much change the industry is going through right now but honestly nobody

2:38:31

really knows what's coming our way nobody knows it's the reality if you're

2:38:35

you know what you can't say sir you're what we don't know how things are changing

2:38:40

right now like things are changing you know in in in manners like you will not believe so

2:38:47

interview to okay but i'm talking about the entire composition of a team the concept of jobs

2:38:52

how do you set up a project to project me can't care like so much drastic changes are happening today

2:39:00

the interviews are a very small part of the puzzle i would say and definitely that is changing

2:39:05

in a huge way because companies also realize right companies are see i i i think

2:39:12

what is actually getting tested in a huge way today is problem solving an IQ aptitude because you

2:39:19

can't build aptitude let's face it so companies are really trying to focus on that area because

2:39:25

aptitude have not built can't you see if you have a strong aptitude if you have a strong problem solving

2:39:32

you have three or four days you'll pick up all of you can relate to some of your friends

2:39:38

or that school kind of college kind of you can get better at it is not to discourage anybody

2:39:44

if we're going to slow go so we're somehow like to pick up but once you get into the group we are

2:39:49

actually good don't underestimate the human brain

2:39:51

yeah these people's innate abidities are there is no doubt about it but what i'm saying is

2:39:58

problem solving and aptitude is what companies are paying premium for today

2:40:02

I'll give you a simple analogy like this is not a new thing right up

2:40:06

they go to MBA graduates who are IAM's top tier colleges that graduate

2:40:10

they do JPMorgan Goldman Sachs and all these investment banks they hire at like what

2:40:16

80 lakh one dollar packages

2:40:18

who's what kind of iAT can't do

2:40:21

they can't do they know anything about it no they don't

2:40:25

but what they have is excellent aptitude you might have also heard

2:40:29

stories of lot of IAT people getting hired in investment banks what do they

2:40:32

they know about banking nothing but these guys are extremely sharp and they can pick up

2:40:36

things very quickly right i think that is basically what is happening in a big way in the

2:40:41

AI era also so if you're asking me for what is that one skill that you can actually work on in a

2:40:46

big way of course these are important things because these are employable skills these are

2:40:50

things that will help you get jobs 100 percent but what will really help you transition jobs and

2:40:56

to set you up for the future is your aptitude and your problem solving ability

2:41:00

to fast thinking, quick thinking,

2:41:03

something new things are,

2:41:04

kuttsa,

2:41:04

kuttsi if you see some concept,

2:41:08

you see some concept,

2:41:08

you've got to see some concept,

2:41:08

you've got to

2:41:09

how to do it. I think these are

2:41:11

absolutely irreplaceable skills.

2:41:14

No AI can replace

2:41:16

these kinds of skills. If you have these skills, you are

2:41:18

unbeatable in the market.

2:41:21

You have to look at it from that

2:41:22

perspective. Now to answer your

2:41:24

I'm confused about in an

2:41:28

agentic system developing. That's a very good

2:41:30

question, that's a very good question, Yubraaj,

2:41:31

ML's a role

2:41:33

because, see, again,

2:41:36

agents don't we've discussed

2:41:37

not, we're not

2:41:38

we can't

2:41:38

help from

2:41:39

the agent we'll

2:41:40

make the machine learning

2:41:41

can be one of the hands of the

2:41:43

agent.

2:41:44

What like agent

2:41:44

what is the agent

2:41:45

you know, you

2:41:46

might say basic introduction

2:41:47

in last Python

2:41:48

but agent is basically

2:41:50

like an autonomous system

2:41:51

that can do multiple things.

2:41:52

And now,

2:41:53

we're you

2:41:53

we're basically

2:41:54

basically we're

2:41:55

the credit default

2:41:56

kind of we can

2:41:57

actually build a credit default

2:41:58

agent.

2:42:00

That credit default agent

2:42:02

can do many, many things.

2:42:05

That customer

2:42:06

to mail can get sot.

2:42:08

That news can

2:42:08

know,

2:42:11

that,

2:42:12

uh,

2:42:14

they're both

2:42:14

things are

2:42:14

right?

2:42:16

Apart from that,

2:42:17

that agent can also go,

2:42:20

that agent can also go and

2:42:22

predict whether the customer

2:42:24

will default or not default.

2:42:27

So,

2:42:27

machine learning becomes one of the components

2:42:30

of the agent.

2:42:31

So now that you are seeing machine learning,

2:42:33

now that you studied machine learning

2:42:34

at a conceptual level,

2:42:36

so this agent's a part

2:42:38

can't.

2:42:39

It is not going to be

2:42:41

very much related to the agent thing

2:42:44

that we will be seen,

2:42:45

but now that you see,

2:42:46

now that you have seen

2:42:47

regression,

2:42:48

what is, classification

2:42:49

you will be able to incorporate

2:42:52

these things in our future discussions

2:42:54

on agents.

2:42:56

So, one is that this

2:42:57

a different tool

2:42:58

can be a credit default

2:42:59

tool to make a tool which an agent can use going forward.

2:43:04

You can,

2:43:04

you're a diabetes prediction

2:43:06

tool to do and that's a tool that an agent can use.

2:43:08

A tool is nothing,

2:43:09

but you have it to function in

2:43:10

wrap up and you can create a tool.

2:43:12

Makes sense, I'm going a little fast

2:43:13

to explain in your language.

2:43:16

One is the concept is

2:43:17

machine learning forms the base.

2:43:21

Because agency

2:43:22

agenti is based on LLM's, right?

2:43:24

Large language models,

2:43:25

which is based on deep learning.

2:43:26

And deep learning is based on machine learning.

2:43:28

So machine learning gives you the base.

2:43:29

So, again, these things are

2:43:31

all things to understand

2:43:31

this is a very good base for you, right?

2:43:33

Make sense?

2:43:36

So there are two aspects.

2:43:37

One is the concept and the other is, like,

2:43:39

like, yeah, absolutely, absolutely.

2:43:42

We'll help having an idea

2:43:44

what is going on in a, absolutely.

2:43:45

I mean, not an idea in part of the agent.

2:43:48

I would say, one,

2:43:50

the, one, what's in it's in there

2:43:50

a idea in the second day,

2:43:52

the agent to make you help help.

2:43:54

But yeah, we haven't,

2:43:55

but we haven't, we've not yet,

2:43:56

so it's technically called a tool.

2:43:58

So this, all,

2:43:59

these MLs can basically be tools in an agent.

2:44:02

You can you know, when we come to agents,

2:44:04

we will see that.

2:44:05

So we can use these as tools in an agent going forward.

2:44:10

Maybe they get deep.

2:44:12

Once again, fundamentals of ML,

2:44:15

you just need to know the basics.

2:44:17

Because that's a different agenda

2:44:18

go to then you're trying to become a machine learning developer.

2:44:21

We are not trying to become machine learning developers.

2:44:23

Our course is agentic AI.

2:44:25

So that agenda is different.

2:44:27

So right now our focus is agents.

2:44:28

ML is one part of it.

2:44:31

So ML is only one part of it.

2:44:32

So that's why we're just a basic level

2:44:34

for some of it.

2:44:35

If your focus is now,

2:44:37

Vinica, you're saying,

2:44:37

no, sir, I want to enter a company

2:44:39

where I want to only work on machine learning,

2:44:41

then definitely I would say

2:44:42

you need to get deeper into it.

2:44:44

But the focus of this course is not into ML in detail.

2:44:46

Focus is primarily into Gen AI,

2:44:49

agentic AI,

2:44:50

us-ke-related ML is we are discussing.

2:44:52

Okay?

2:44:53

There are two different roles.

2:44:54

There are two different roadmaps.

2:44:58

Okay, very nice.

2:45:05

So, yeah, I mean, sorry, I'm done, Arsit.

2:45:07

I'm so sorry.

2:45:07

Like, you can continue with the quiz.

2:45:10

No way.

2:45:10

I'll keep talking only if you don't stop me.

2:45:15

Please continue.

2:45:16

Yeah, I think I can share my screen.

2:45:18

Sorry.

2:45:19

Yeah.

2:45:21

Okay, students, let's start with the first question of the day.

2:45:28

What does classification predict?

2:45:34

Averages, numbers, graphs or categories.

2:45:58

Yes, that is correct.

2:46:07

Classification is used to predict categories.

2:46:11

Second question.

2:46:16

Logistic regression is mainly used for

2:46:19

measuring distance, sorting, sorting images,

2:46:24

finding equations, or predicting categories.

2:46:28

Yes, similar to the previous question, we know, logistic regression is a classification.

2:46:58

model, so it is used to predict categories.

2:47:02

Third question.

2:47:06

What is the sigmoid function output?

2:47:11

Only 0 or 1.

2:47:13

A probability like value, any integer, or a text label.

2:47:28

Yes, it is a probability-like value, which is between 0 and 1, but not only 0-1.

2:47:58

Fourth question, what is a common decision threshold?

2:48:06

0.9, 0.5, 1.5 or 0.1.1.

2:48:28

Yes, 0.5 is a common threshold, but like we saw today, it can be changed depending on our particular problem problem.

2:48:45

Final question of the day.

2:48:50

What is a true positive?

2:48:58

Right, through positives are correctly predicted positive values.

2:49:28

look at the final lead-up on now.

2:49:38

Avishkar has won the quiz for today.

2:49:42

Congratulations, Avishkar.

2:49:46

So with that, we end our quiz for today.

2:49:51

If we have any more questions, I think Schenzer can take over now.

2:49:57

Yeah, thank you.

2:49:58

so much, uh, yeah. I think we are good, nice, all good. Shall we close today?

2:50:07

Any other questions anybody has?

2:50:14

Okay. Okay. Good night. Good night, all of you. Let's meet again next session. The next session,

2:50:20

we will continue on. There's another continuing classification session we have. And we will

2:50:25

also specifically discuss a multi-class use case with you death class. Okay. Yeah.

2:50:28

Okay. Thank you, everybody. Good night, all of you.