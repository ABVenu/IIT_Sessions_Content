0:00

Thank you.

0:30

Thank you.

1:00

Hi, everybody, very good evening, all of you, we will just be starting on here.

1:30

Thank you.

2:00

Thank you.

2:30

Thank you.

3:00

Thank you.

3:30

Give me one second, guys, I'm just trying to give me one second, guys, I'm just trying to share my screen. Just give me one second, please.

4:00

Okay.

4:07

Hmm.

4:12

Hmm.

4:30

Thank you.

5:00

Thank you.

5:30

Excuse me.

5:42

Excuse me.

6:00

Hmm.

6:30

Thank you.

7:00

Okay, guys, welcome all of you once again to the session.

7:04

I hope everybody is doing good.

7:06

So we'll continue to start on and I'm going to quickly start out with a very basic mind map in terms of where we are in the session, what is today's session about, what is the context of today's session.

7:20

And this is something that we have, we are trying to do in a very new way.

7:25

It's a new initiative that we have started.

7:26

So every class, each of you can connect the dots.

7:30

with respect to what we did in the last class, what we are doing in the next class, and how this connects with the overall course and some real world use cases of it.

7:41

So it's a very basic, this will again be shared with all of you in, you know, as part of your, as part of your course materials later on, but just wanted to walk all of you through it.

7:51

So the previous module obviously was Python foundations.

7:54

This is what you did already and you learned code Python, Pandas, SQL.

8:00

other things and from that we entered into the the foundational module. This is what we covered

8:06

and this is the current module we are in wherein we have talked about the fundamentals of machine learning.

8:13

Okay, the fundamentals of machine learning. What is it about building a model? How do we split the data?

8:18

Some very basic data preparation stuff we talked about. And we also talked about something

8:22

called linear regression, lasso and ridge regression we looked at, regularized models. And we also covered

8:28

our very first classification algorithm called logistic regression in the last session,

8:33

along with a detailed discussion on the confusion matrix. We spent a lot of time on this and we understood,

8:40

you know, what exactly is a confusion matrix, what is the context of false positive, false negative,

8:46

what kind of mistakes it makes. So we talked about that in detail. And right now,

8:51

as we stand, right now we are all very, very comfortable in terms of how to build a model. How do we take a data?

8:57

how do we build a model? We are all very, very comfortable with that particular part right now.

9:03

Current session, this particular class is about, is kind of following on from where we

9:08

left off in the last session. And today we will talk about something called decision trees and

9:11

random forests. So we are moving beyond one model and very interesting. Once I start talking

9:16

about decision trees, you will realize what this means. This is also very much, you know,

9:21

we will discuss it in the context of classification, but today's algorithm can also be used for

9:26

for regression. Just keep this at the back of your mind. But again, the session is

9:30

focused on classification. So we are continuing on with classification. Everything that we

9:35

covered in the last session, everything remains the same. The only thing is that we are

9:38

covering a different algorithm called decision trees. That's it. Nothing changes. The same.

9:44

dot fit, dot predict, train test plate, overfitting, underfeiting, good fit, train accuracy,

9:50

test accuracy, nothing changes. Everything remains the same. We'll just give you some

9:54

intuition behind decision tree. Again, remember,

9:56

but this is not a math session. We won't be getting into the internals of the algorithm.

10:00

We will intuitively give you the concept of decision trees. Okay. And how does this relate to the

10:06

overall, you know, overall next module? Next module is where we start on with the very, very interesting

10:15

generative AI part, module 3. And after that, in the next module, we will talk about agentic

10:20

systems. So this is the learning part that we have got here. And obviously all of what we are covering

10:25

will be very relevant for what you will do going forward. When you go to Gen AI, you will

10:29

relate to what model building is, although the topics are not very much connected,

10:33

but still the fundamental concepts that you're learning here will definitely be useful there. For

10:38

example, Confucian matrix, even when we build rags, agents and all those things when we come to

10:44

in module 3 and module 4, when we talk about those topics, you will realize that there are many,

10:49

many commonalities between these two modules actually. Okay. And this is the, um, and this is the,

10:55

you know, this is the course, course value. This is what is the overall value add for this

11:00

course. And obviously, uh, from a real world perspective, like what, what is the, what is the key

11:06

real life use case for what we're going to be building today? Well, I think we have already talked

11:10

about enough real world use cases of classification, but I'm just trying to like some general examples

11:15

are given here like loan rules, spam filters and all these kinds of things. I think we have talked

11:19

about this in detail already. You guys already know what this is, right? Writing, picking the right metric.

11:24

What does this mean? It means. It means.

11:25

okay which error is more costly is false negative more costly false positive more costly and all

11:29

that so that is basically what this is about okay again it's a very small initiative that you have

11:33

started uh you know where the first five minutes or first three four minutes we just walk you

11:39

through this thing and then we'll proceed along okay yeah now let's start on let's jump into

11:46

decision trees and start on with our uh decision tree lecture

11:55

all right so in the previous session folks you learned how to build a

12:06

logistic regression model obviously and you know we have we have seen how to build

12:10

classification now today we will learn a slightly different algorithm called a decision

12:14

tree now what what is a decision tree exactly doing behind the scenes what does the decision

12:19

tree really do and to help you understand this in a better way i'm going to take you to a

12:24

a to a very interesting diagram let me take you back to a very interesting diagram which

12:30

will help us understand this in a better way what decision trees really are basically and to

12:48

understand this in a better way i will take the context of loan prediction

12:54

right so so let's take the context of a loan approval problem all of you can see the screen

13:03

and so before i start the conversation everybody give it a glance once all of you just give it a

13:09

read once what are the things that are required when we are trying to approve a loan for a person

13:15

i think this is the use case we have covered before also when we talk about classification

13:20

let's say today you apply for a loan in a bank this you have a bank you have a bank you have a bank

13:24

and you're applying for a loan in some bank right what kind of what kind of methods is the bank

13:32

using what kind of methods is the bank using to predict whether the loan should be granted to you

13:39

or the loan should not be granted to you so the bank is looking at all your historical data they're

13:45

looking at your credit history your credit limit your last few months transaction details the bank

13:52

is looking at your last few months payment history so the bank is looking at all that information

13:58

and based on that the bank is deciding whether to go and grant you the loan or not and this happens

14:05

in many of the many of the applications also nowadays if you look at many of the applications nowadays

14:12

you know we have many of these online applications uh apps where you can just go enter your

14:17

pan number in india the pan number is linked with everything right so if you give your pan number your pan number

14:21

your pan number is linked with everything so from the pan number everything is fetched

14:25

basically so the information about your credit limit and all you know all your bank accounts is

14:29

automatically fetched okay nowadays there are also apps where different banks are starting

14:35

these apps nowadays i say say a bank has it hdfc has started something called smart wealth these are

14:40

like aggregators third party aggregators where uh the bank has partnered with a firm and if you

14:46

just enter your pan number uh you know so within i say say bank or within hdfcc bank or within hdfc bank

14:51

all your other bank's details will be singularly aggregated okay anyway so what i'm getting at

14:58

here is how does the bank decide whether to grant loan to you so these are the kind of questions

15:06

that need to be asked right so it is it is a typical machine learning problem all of you can relate to

15:12

it so we've got the employment status we look at the overall uh um um

15:21

you know we look at the employment status we look at the overall uh retirement status you know is the

15:26

person retired is the person not retired so we look at the retirement status and uh we look at

15:33

annual income of the person right and does he have any dependents he or she have any dependents

15:38

that's also an important factor sometimes if you have dependents dependence

15:41

dependence when let's say kids or you know senior citizens like parents you're looking after then it's

15:47

a problem i mean that means your expenses are very high you know if you're uh you're uh you're uh you're

15:51

if you have dependents and all of a sudden your expenses are high and then maybe the probability of

15:55

you being able to repay the loan will be in question because banks want to give the loan

15:59

knowing that you will repay on what basis is the bank deciding should i give loan to this person

16:03

so the bank is trying to understand your repayment capability if your repayment capability is high

16:08

then the bank will approve the loan so there's a lot of machine learning going on behind the scenes

16:12

and it's very similar to that credit default prediction we have done here also there will be

16:16

historical data historically we will know uh you know various

16:21

historical loans that were like granted customers like this you granted the loan and this customer

16:27

repaid the loan but then you have another example you historically there's another customer to whom

16:32

you granted the loan but the customer did not repay the loan so you will learn on the basis of

16:37

that that these kinds of customers they repay the loan these kinds of customers they did not repay

16:43

the loan and based on that you're trying to build a machine learning model to predict whether the person

16:49

will pay to repay the loan next time you apply

16:51

for a loan in a bank or in some other app you know there are so many apps nowadays where

16:55

you can just type your pan number and apply for a loan when starting from as as small as 10 15 000

17:03

you can you can apply the loan the models are basically calculating a it's a classification

17:09

problem that is being solved so they are trying to predict what is the probability that you will

17:15

what is the probability that you will be you will repay the loan and if your probability of repayment is high

17:20

then the bank will approve the loan but the important thing is these are the features so in

17:25

order to answer that question these are the kind of you know these are the kind of features i require

17:29

features middle of inputs so we need to know employment status retirement history and all that

17:35

these series of questions can be organized in a hierarchical structure i'm trying to tell you the

17:39

intuition behind what a decision tree is so the final thing that will be created

17:44

will be something like this this is that final decision tree like structure that you can see

17:49

the decision tree is nothing but a flow chart think of it that way so before i

17:52

talk about it any further all of you give it a glance please just give it a glance all of you

17:57

what is it just give it a glance all of you

18:19

you know.

18:49

you take a look at it. You see it is basically it is basically it is basically structured like it is basically structured like a flowchart.

19:19

Yes, yes.

19:24

It is structured like a flow chart, a flow chart kind of a diagram.

19:28

And this is the end result of what is getting created.

19:32

So if you try to think of what we are trying to do here, we have the data, okay?

19:37

We have the data and we will be using an algorithm called decision tree.

19:45

We have the data.

19:47

We will use an algorithm called decision tree.

19:49

We will use an algorithm called decision tree here.

19:53

Okay?

19:54

This is a decision once again.

19:55

Sorry, I think the screen went out.

19:58

We will use an algorithm called decision tree.

20:01

I'll say dt.

20:02

dot fit.

20:03

Dot fit I will do.

20:05

And based on that, what I will do, I'll end up building a model.

20:08

This is back to the fundamentals we learned in our machine learning introduction session, right?

20:12

So data algorithm model turns out that today, the name of the algorithm is called decision free.

20:17

That's it.

20:18

We are using a decision.

20:19

tree algorithm to build a model and this model is, we will take a tree like structure.

20:27

It will take a tree like structure.

20:29

So the end result of what we are getting, by using a decision tree on our data, we are

20:35

able to generate that particular tree like structure.

20:39

That's the model.

20:40

So what you are seeing right now, this is the result of this.

20:44

So we have historical data.

20:45

We will have a lot of historical data just as I was explaining.

20:49

Customers like this repaid the loan.

20:51

Customers like this did not repay the loan and all.

20:53

This is the X, Y combinations you will have.

20:55

You will fit a decision tree and the end result will be this tree.

20:58

The model of the tree that you will get.

20:59

And this is that example model or tree that you're able to see on the screen.

21:03

This is the example model or the tree that you're able to see on the screen.

21:06

And this is the end result of what you're getting.

21:08

It's the result of dot fit.

21:10

Right.

21:11

And this is going to give you an idea as to how the model thinks.

21:15

Okay, this is the dot fit part, not the dot predict.

21:17

I'll talk about the dot predict part in a moment.

21:19

Okay.

21:19

So you can actually start to see very interesting.

21:21

So first, you're asking a question, is the person employed?

21:25

Right?

21:25

Is the person employed?

21:27

If yes, then ask the next question.

21:30

What is the customer's age?

21:31

Is it less than this?

21:31

Is it more than this?

21:33

If it is less than this, ask the next question.

21:35

What is the annual income of the customer?

21:37

Is it high?

21:37

Is it low?

21:38

If the annual income is high, then approve the loan.

21:40

If the annual income is low, then ask another question.

21:43

Does the person have dependents?

21:44

And based on that you use?

21:45

So this is the way how the prediction happens in a decision pre.

21:48

So what you are seeing?

21:49

on the screen, this is actually getting built when you're using the decision-free algorithm,

21:54

which I will just be coding in the session in a moment.

21:58

This is the final thing that will get built.

22:00

Yeah, your can be made-upon-a-pura.

22:02

And then what you can do, you can go back and do predictions on the basis of that.

22:07

You can go back and do predictions.

22:09

So, for example, let me use a different color.

22:13

For example, this is model.

22:15

This is model.com prediction we will be doing.

22:18

And for prediction, we will be doing.

22:19

purpose, let's say, let's say I'm saying the employed is, these are the values I'm giving you,

22:25

okay? And I will, I will ask you to answer it. Employed, the value is equal to yes. Okay.

22:33

Customers age, let's say, is equal to 42. Okay. Forty two. Okay. Forty-two is customer's age. And

22:49

um low okay. And dependence is no. So this is the way how we have done things so far, right?

23:05

So you take the data, you build a model and next time I give you a new value of X.

23:10

You have your X new. Okay?

23:12

When you have a new input, so using that input, you can do a dot predict. That's the way how we have learned machine learning so far, right? You take

23:19

the data, you build a model. It turns out today the model is nothing but the decision tree.

23:25

Data is a model but now, which is the decision tree. This is what you're able to build behind the

23:29

scenes. And next, what you can do, using that decision tree, you can do the prediction. Whatever

23:33

tree you're built right now, using, using that, you can do the prediction. So given a new person,

23:41

given the records for a new person, if I know they're employed, value, the age, the income and the

23:46

dependents, I can predict whether that person should be a,

23:49

do for the loan or not. And it's very, very, very interesting. And you can, you can literally go

23:55

through the tree and understand exactly how it's happening. So far in our sessions, if you relate to the

24:01

linear regression and logistic also, we just saw dot predict. But I've got, we're that time

24:06

we've got, we're saying, well, it's what's going to say, right, what is going to. You can actually see

24:11

through the decision tree and understand exactly what is going on. That is why we say the decision

24:15

tree is one of the most explainable algorithms, explainable. It is very explainable. It is very

24:19

You can literally understand how the machine is thinking.

24:24

When you're new data, look, one, it's the data is,

24:27

the algorithm fit, and the model been

24:28

one, one, it's there to go-gia.

24:31

This model, the decision tree model, or this tree is, this is a complete white box.

24:36

But that it's like, you can really understand exactly what's going on here.

24:40

So next time when a new customer applies, next time when a new data comes,

24:43

you can completely see the flow of the data through the decision tree.

24:47

You can see the flow of the data through the decision tree. You can see the flow of the data through

24:49

the decision tree to understand exactly why the model predict something.

24:54

It is no longer a black box. And that is the biggest advantage of a decision tree.

24:59

So, chalo, here here here, X new, so model dot predict, how will. I will come to that,

25:03

I will come to that, I will come to that. Don't worry. I will talk about that if he fails, I'll come to that.

25:07

So, so abe, up here here here. How's, how flow can. Let's take a look at it.

25:12

So first, you're asking the question, is the person employed? Huh? Yeah, yeah,

25:16

here's from here. This side's the guy. Next, you're asking the question, what is the customer's

25:19

age 42, so that's less than 55 is.

25:22

Well, this is a question-wale.

25:24

Here, you're asking, what, customer's age, what is?

25:26

Less than 55 or more than 55.

25:28

So, this value is, it less than

25:29

than, then, so you here from.

25:31

Okay, this side.

25:32

It's like a flow chart.

25:33

I mean, every node you're asking a question.

25:35

Is it this? Is it this?

25:37

If this is here, we are, if it's true, then here.

25:40

Okay? That's it. Simple, no?

25:41

Simple.

25:42

Next, next, here here here came, income.

25:44

Income, what is, it's low, so,

25:45

the side, this side, this side, this.

25:47

This side, this side.

25:47

Here's it, right?

25:49

And next, what is the thing?

25:51

You're asking, has dependents?

25:53

Has dependents?

25:53

Yes or no?

25:54

Yes, the person does not have dependents.

25:56

Sorry, no, the person does not have dependence.

25:58

So, the answer to the question will be, yes, the person will be approved for the loan.

26:05

So next time, you give a new data and you do model.

26:09

Dot predict, what will happen?

26:11

Next time you give a new data and you do model.

26:13

Dot predict, what's going to happen?

26:15

You've got to literally traverse through the entire decision tree.

26:18

You're going to start from the root node.

26:19

the top, you're going to traverse through the entire decision tree.

26:22

At every node, you will keep asking questions.

26:24

You will traverse through the entire decision tree.

26:27

And you will come all the way down to the bottom leaf node.

26:30

And where you go to the answer will.

26:31

And the best part about a decision tree is that you know exactly what is going on.

26:35

You have full of the case how it's going.

26:38

Look, you're a real world situation.

26:40

Imagine you're a customer.

26:41

You've got to bank to go to loan for.

26:44

So bank said, you, bong, he can't be, you can't pay you.

26:47

So we'll you just sit and go back and, you know, go back.

26:49

And no, you will, you will, you will, you will, you, you, you, you, you, you will, you, you, you, you will not just accept it.

26:55

So the bank is liable to explain to you.

26:58

So policies on the, protocols, it should be the bank is able to explain to the customer that this is the reason why we cannot give the loan to you.

27:05

It should not be a black box.

27:07

India may regulations, it's not.

27:09

Here, bank may be there, bank they bought there, you. You cannot argue.

27:12

You go to the bank, loan reject, what do you? What can you do?

27:15

But if you go back to Europe, Europe has a very stringent regulation.

27:19

called GDPR.

27:20

GDPR stands for general data protection regulation.

27:28

General data protection regulation.

27:30

And in Europe, it is actually mandatory for banks.

27:34

Whenever you are asking any, if a customer goes and asked the question,

27:38

why I did not get the, you know, get the loan, then what will happen?

27:43

You can go back and explicitly ask the bank.

27:48

Ask the bank.

27:49

to go back and give this answer.

27:51

That's the way to look at it.

27:52

So the bank is liable to give the answer.

27:54

And again, in these kinds of scenarios, you can see, you can understand that the decision tree

28:00

will be very, very helpful in that context.

28:02

Because decision tree, you can't exactly why the bank took the decision.

28:06

Customer age, yeah, income it's, dependence here, you're traversing to the whole tree.

28:11

Because this is the concept of a decision with a big picture idea.

28:14

Data, we will use the algorithm, we will build a model.

28:17

The model apparently takes the shape of a.

28:19

tree which is like a flow chart okay this is the model dot fit yeah

28:23

your tree will be and when you next time you give a new data this is the

28:26

prediction that will happen where you're simply traversing through the tree now

28:31

the very interesting part is I'm going to take up Gourtex question right now

28:34

that he's what is what is what is going to be here?

28:36

Gertek Poochak is what is different.

28:39

Very good question actually because many of you if you're seeing this

28:43

you, you, if you're seeing this, you, that you say, sir, sir, this is ifel's

28:45

so machine learning, what point is and very good question.

28:49

I'm going to take you back to the discussion we had, you know,

28:53

you know, first day, first class of machine learning.

28:56

Yeah, I'm in starting me you

28:59

classed classed rule-based AI or machine learning based AI.

29:04

Is, right?

29:05

Yeah, yeah, so you know, if-else statement had to rule-based AI.

29:10

So, Gurthek, if-al's, if-else statement,

29:14

you're not, then the responsibility will be on you.

29:19

to figure out all the permutation combination.

29:22

You have to study

29:23

you have to figure out

29:25

if these kinds of patterns are true,

29:29

the person might default on the loan.

29:30

If these kinds of patterns are true,

29:32

you have to write lots and lots of EFL statements, right?

29:34

Remember those conversations we had long back.

29:37

We will be, I think this is almost more than a month back.

29:39

First class of machine learning, right?

29:42

So we talked about

29:44

writing all those manual if-else rules from scratch.

29:48

That is.

29:49

is very tedious, that is very time-consuming, right?

29:52

So that is where you are writing an if-else from scratch.

29:56

You, you as the user, you as the customer, you are writing it.

30:01

You are the end-user, you are writing it.

30:03

So you have to study the system, you have to write all the if-else rules.

30:06

You have to write all the if-else rules.

30:07

You know, but here.

30:10

Here-per-if-else, we're not looking.

30:13

Here-per-if-else, the machine is writing.

30:16

And that's the biggest difference between rule-based AI.

30:18

By rule-based AI is where we humans write the rules.

30:20

So we are writing our e-fells, right?

30:22

Like we've made example that time of operating system.

30:25

Now, you know, we have examples of air-conditioner.

30:29

Or then, something like a mobile phone.

30:33

We have the operating system on the mobile phone.

30:35

If mobile phone battery 15% down, then battery saver would.

30:38

So this is the e-fells we have written.

30:41

But what is different in machine learning?

30:43

In machine learning, we are not explicitly writing rules.

30:47

Because the patterns are so.

30:48

complex. There are so many infinite number of ways people can

30:52

default on a loan, people may not default on the loan.

30:55

How many, kind of conditions are so many infinite number of conditions

30:59

that we cannot write if else rules.

31:01

We can't write if we can't.

31:02

We do machine learning. We ask the machine to write the rules.

31:06

I say, I cannot give the EFEL's rules.

31:09

So machine go, you EFEL's rule.

31:11

And decision tree is a great example of that.

31:13

All through the classes, we're doing.

31:15

We're doing the machine was learning the rules.

31:17

But only.

31:18

The only thing is that here here here,

31:20

machine upna up and machine up and make the data, you fit the decision to the algorithm.

31:25

Now, algorithm in the other, some, which is not the scope of the class,

31:28

which is not, we will not get into entropy, informed, but a lot of things are happening there.

31:34

But if you, if you see what's going on is from the data, once you fit the algorithm,

31:41

this rules are getting learned.

31:42

So here we have a one term up to use to, okay, this is your rules.

31:46

this rules are actually learned.

31:49

And this are the if-else rules.

31:51

So the machine is coming up with the E-FELS rules.

31:54

So, you know, and that tree map you're all right.

31:57

You are able to see beautifully what those E-FELS rules are, what, you know, how the data is propagating.

32:03

So this is the biggest difference.

32:05

In rule-based, we are writing the rules in decision-free,

32:08

the machine is looking at the data and the machine is able to automatically come up with if-else set of

32:16

rules, right?

32:18

So you're going to say, sir, this E-FELS is.

32:20

But if it, but if-will-if-alls, is.

32:22

So, diagrammatically,

32:24

things are very easy to.

32:25

That's the way, I have you made up a picture

32:26

but you tell me, can you convert this into an EFELS rule?

32:30

I'm going to, you know, I will not do this in detail because it will take a lot of time.

32:35

I will use a shortcut.

32:37

Shortcut, what is, guys?

32:39

I will take a snipping tool.

32:41

You see, it's beautiful actually, you know.

32:43

It's a beautiful thing.

32:44

So I will just go and, uh, I will just go and, uh, uh,

32:45

I will just go and take a snippet.

32:47

This go to Gemini in.

32:50

Okay?

32:51

This is your...

32:54

Oh, where is copy?

32:57

Let's see.

32:58

Let us see exactly what if else rules are getting created here.

33:03

Just a second, guys, huh?

33:09

What happened?

33:15

So, I'm here and you can take a look at it.

33:17

Here we, this go here we'll tell that please convert this flow chart into a corresponding if else, if,

33:30

if, elif, else in Python, with all the nesting, with all the nesting as required.

33:42

No functions.

33:45

Keep it simple, only if else, okay?

33:49

So, Kutnik, I think, I think, your question to answer will be.

33:53

But you can take a look at it.

33:54

Very interesting.

33:56

Sorry, just one second.

33:58

I just wanted to show this to all of you.

34:01

This flow chart is, flow chart, so I made up to make it, so I've got it picture

34:04

but actually that flow chart is nothing but a set of if else rules.

34:08

So that is exactly what the machine is generating.

34:10

That's the best part.

34:12

So, so it internals when we will now, we will now straight away get to the,

34:15

application part, okay? Now, let us see.

34:19

And you can, and this is the, this is the, this is, huh, exactly.

34:22

Huh, exactly.

34:23

ML algorithms, learn patterns from data to make predictions.

34:25

Exactly.

34:26

You can't take a look at this.

34:27

Now, this doesn't look that difficult, but, uh, so man et

34:31

this is basically taking some simple variables.

34:34

This is now ignore.

34:35

Your focus area should be here.

34:37

Your focus area should be here.

34:38

Your focus area should be here.

34:40

This flow chart's decision logic.

34:40

Okay, okay?

34:40

Not very hard, right?

34:42

Not very hard.

34:43

If you take a look at it.

34:43

If L.F.

34:45

LIF, how nested L-siff, see?

34:48

So that entire nodes of the tree, those are nested L-siff here here.

34:52

You can take a look at it.

34:53

So, whatever I showed you there, so this is that entire part of the nested L-S-S-A block.

34:59

Okay, so this is the big picture idea of what we are, what we are learning here today.

35:03

Okay?

35:04

And that's what decision tree is really hard.

35:07

All right. Excellent.

35:09

Now let's move on.

35:11

So this is again pretty much the same stuff.

35:13

and just from a, just from a terminology perspective, just some of the important terms to clarify,

35:19

there is something called the root node, there is something called the branch.

35:22

Branch, branch, what's your path is, okay?

35:25

That we're branched, okay?

35:26

So, root node is basically this.

35:28

The sure in the show-mey-s-s-s-sha-saw-poo-you-who-route-node-ho-h out-h.

35:30

And these are the internal nodes.

35:33

Internal nodes are basically the intermediate nodes that are coming in between.

35:36

Nodes, I mean, where the part where you're asking the questions.

35:41

And leaf node is where the final answer.

35:43

the final prediction happens.

35:44

You have your leaf nodes.

35:45

Okay?

35:46

Depth of the tree is how many question layers.

35:48

Basically, how many levels deep you're going?

35:52

Basically, we're doing.

35:53

Basically, we're doing, guys, here.

35:55

We're, we're asking,

35:57

nested if else rules.

35:58

What are decision trees?

35:59

Decision trees are nothing but nested,

36:01

if else rules from root to leaf.

36:03

But you've already,

36:04

how it's if else is.

36:06

So, we're what are here.

36:08

We are asking questions of the data, right?

36:10

Isn't it?

36:11

If you see from the root node,

36:13

all the way to the internal nodes,

36:17

we are asking questions of our data.

36:20

Given any new data,

36:22

we are starting from the root node,

36:23

we are asking a question,

36:24

if that'sai-ho-to-d-d-d-d-d-d-dus-ra question,

36:26

that-so-h-h-h-h-d-dus-ra question,

36:27

so we are continuing to ask

36:30

different, different questions of the data

36:32

to get to the answers.

36:34

So that is exactly how we can think of

36:36

the context of the depth.

36:38

Depth of how many question layers,

36:41

how many question layers we are having?

36:42

So, you know, if you look at the depth of the decision tree here,

36:46

its depth, it's how depth, it's depth two.

36:48

It's a depth to start.

36:51

You're root's at depth one,

36:52

one level deep, second level deep.

36:54

Yeah, this is the decision tree which is two levels deep.

36:57

That is the way to look at it.

36:58

This is a decision tree that is two levels deep.

37:01

Right?

37:03

So, the terminology should be clear.

37:05

Root node we have discussed.

37:07

Branch we have discussed.

37:08

Branch, we have discussed.

37:12

question, you're asking,

37:13

if it true, or it's true not?

37:16

Then, you're branching.

37:18

Either this side or this side, that is the branch.

37:20

Leave, internal node, leaf node, leaf node, and depth.

37:23

That's the way to look at it.

37:24

This is the concept.

37:25

And just keep this at the back of your mind.

37:27

Just like how we discussed in our

37:29

ridge and lasso regression session.

37:32

We made last week,

37:35

ridge and lasso regression session

37:36

did.

37:37

There we have a hyper parameter alpha discussed

37:40

you.

37:40

You know, you know, I may this term be used

37:42

what was called hyperparameter.

37:43

And I told you that it is like a tuning knob.

37:46

Now, you know, that you add to a tuning knob.

37:48

So I had you said that,

37:49

like you alpha value come to go.

37:51

It will overfit.

37:52

If you increase the alpha, it will underfit.

37:55

So every algorithm, even decision tree,

37:58

this can be a tuning knob.

38:00

Like in that regularization session,

38:03

we had discussed the concept of alpha.

38:06

Now alpha go through the model will become something.

38:09

If you increase the alpha, the model will become something.

38:12

in terms of good fit, overfit, underfeit, right?

38:14

So similarly, even for a decision tree,

38:17

there is the particular hyper parameter that we have called maximum depth.

38:20

So we have a max depth hyperparameter

38:22

and which we can control,

38:24

which we can use to control the depth of the tree.

38:27

So we can decide how big the tree will be.

38:30

Yeah, your decision tree is two levels deep.

38:31

And just remember all of you.

38:33

If you go and, you know, it,

38:36

so there is a particular hyper parameter called maximum depth.

38:39

On the decision tree code kare.

38:41

So we will.

38:42

go back and learn about this maximum depth.

38:44

We'll use this is that hyper parameter.

38:46

This is that knob.

38:47

This is your tuning knob.

38:49

You can it.

38:49

You can't it, it's more than.

38:52

Maximum depth's minimum value one.

38:54

So what is maximum depth basically?

38:56

I think it's very obvious.

38:57

Maximum depth limits.

38:58

How many questions are allowed to be asked?

39:01

How many questions you can ask, basically.

39:03

What now you can't get to level deep go.

39:06

And obviously, you can think, if your maximum depth is equal to one hour,

39:09

we'll show you.

39:10

We'll demo in demo, okay?

39:11

We'll demo and try.

39:13

If you say maximum depth equal to one, that is a very basic decision tree.

39:17

Depth equal to one is a very basic decision tree.

39:19

You know, you can think of it like a very underfit tree.

39:22

But depth one, much like, you have only one level deep.

39:26

That's it.

39:27

But I mean, you're not asking.

39:29

It's like saying, if you don't even ask the right questions, how will even get to the answer?

39:35

You know how can't how can't even get to the answer?

39:38

If you don't even ask questions.

39:41

You have to continue asking questions.

39:44

You have to continue asking questions.

39:48

So if you limit your maximum depth to one,

39:50

if maximum depth to one, if maximum depth to it's so

39:53

that you're not asking you'll get a highly underfit model.

39:57

Underfitting, that means a useless model.

39:59

The model will not be accurate.

40:01

Number two, point number two, if your maximum depth is very big, very large,

40:06

you have a maximum depth to 100%

40:08

that means you have,

40:10

you're trying to go very deep and you're trying to ask all sorts of questions

40:17

and based on that you're trying to decide then that is also bad.

40:22

If maximum depth go both barra diya, what would be overfitting?

40:26

Okay?

40:26

Both come underfitting, very overfitting.

40:30

Beech in you will have a good fit.

40:32

The same story that we have been discussing before.

40:34

So this is the hyper parameter called maximum deck that we'll be using here.

40:38

And this is a key no.

40:40

for generalization.

40:43

Okay, so to generalize the model, because this is what we are trying to do in machine learning, right?

40:46

Other model, if the model is not at all learning, that is bad.

40:50

If the model is learning too well, that is also bad.

40:52

So the key idea is generalization.

40:54

We want to build a model that generalizes very well.

40:57

Okay, that's the concept.

40:58

Now, to help you understand this a little better, let me go back to my snippet.

41:09

Just just.

41:10

Just give me one minute, guys. I'm just going to quickly go and open this.

41:20

I will first explain to you. And you know, the best part is, guys, the best part is,

41:24

the best part is, we can actually go and plot it in Python also.

41:29

It's very nice, actually.

41:30

Whatever I explained all this while, I'm literally, you know, notebook in car and think how it's

41:33

plot it. It's really cool.

41:35

Okay.

41:36

So just allow me a minute.

41:37

I'm just going to make a couple of edits here.

41:39

Just give me one minute.

41:40

Oh.

42:10

Thank you.

42:40

Thank you.

43:10

Thank you.

43:40

Thank you.

44:10

Thank you.

44:40

Thank you.

45:10

So,

45:13

So, guys.

45:14

So, guys,

45:17

what we have to the.

45:40

this thing. And I have a simple data set. We have seen this data set before also.

45:45

Same data set as we discussed last time. So I'll start my explanation with a simple data set. So we

45:52

pass fail wala change. Then we'll come to a more real world problem shortly. Okay? So what does the

45:59

data set tell you? Based on the study hours, sleep hours and distractions, we are trying to predict

46:05

whether the person will pass or fail. So we are looking at the study hour.

46:09

sleep hours and destruction. And we are trying to predict whether the person will pass or fail.

46:14

It's a classification problem. The person will either pass or the person will will, will, will, will, we will fail.

46:19

Dono may say, okay? That classification problem here.

46:23

It's a kind of classification problem. So based on the features you are trying to predict whether the, you know,

46:28

whether the person will pass or fail, as you can take a look at it.

46:33

Okay. Okay. Now, moving on.

46:39

This is the part where we are training the decision tree model.

46:49

Updek, Saktio. And this is exactly the code I use for the decision tree. The concept remains exactly the same.

46:55

Dictionary classifier, max depth 3. Dot fit, dot score, same story. Nothing changes.

47:03

So the only thing is that you can see, you here on when I say maximum depth equal to one, I can either say maximum depth equal to.

47:09

to 1. But if you increase the maximum depth, what will happen? If you make your maximum

47:14

depth very high, what will happen? The model will overfeit. This is overfitting. So, if we don't stop them,

47:21

they will ask 100 questions until they perfectly memorize every single student. That is the,

47:26

that is the intuition behind overfitting. What's like, if you're up depth to it. The tree will look,

47:33

the decision tree will look very, very big. This is something like. This is a so. This is a

47:38

very big. Not trying to show the whole thing, but it will be very big. At every node,

47:42

you will be seeing certain types of questions getting asked. So this is the intuition behind maximum

47:47

depth. After the maximum depth, you'll make 100 kore. Your tree will be like this. You'll continue

47:52

asking questions, continue asking questions and it will be a highly overfit model.

47:57

Overfitting the matter. That means on the training data, whatever data is given to you, the machine

48:02

will learn the patterns very well. But when you're giving some unseen new data, the model will perform very

48:07

poorly. So that is the intuition behind what overfitting refers to. So this is what will happen

48:13

in the context of overfitting. Okay? That's how we can look at the whole thing. What is the other

48:20

extreme? Do you see say maximum depth equal to one. Maximum depth equal to one.

48:26

Maximum depth equal to one, you're making it only one level deep. You're making it only one level

48:29

deep. This is. This may what is. It's what you're asking. So rendering, right? But you can take a look at it.

48:37

When you say maximum depth equal to 1, you are, so you

48:41

this one thing, you know, this pay, some other

48:43

things are going to confuse you guys, but

48:45

your, your focus should be only on this part.

48:48

Now, you ignore it. Samples,

48:50

number of rows are. And this one of

48:52

ignore it, okay?

48:55

This one thing ignore.

48:56

And here here, just look at this part.

48:57

What is the final output?

48:59

Okay?

49:00

Just ignore the, the value part here.

49:04

Like, it's split, basically.

49:07

So what is important is based on the question, these rules are constructed by the tree.

49:12

Your tree are being made. This is how the tree is getting formed.

49:15

So at the algorithm stage itself, you're limit

49:18

can't, I want a tree that is only up to one level deep.

49:23

But when you say maximum depth equal to one,

49:24

you've constraineded regularization, right?

49:28

You've constrained it a lot.

49:30

You're only allowing it to ask only one question, one level of question.

49:33

So it is not a very good model.

49:36

So you need to find.

49:37

out what is the right value of max depth or easy process go what is the term that we use

49:41

here guys I had I had mentioned this term before as well we call it hyper parameter

49:46

tuning is called hyper parameter tuning. We try to tune the value of the hyper parameter

49:51

and we try to find out the best hyper parameter value. So let's let us agree at something close to

49:56

three if we say maximum depth equal to three three k a

49:59

we will probably end up seeing a better quality model something like that okay again this is

50:04

is the very small data set we'll get a better idea in the upcoming problem.

50:07

problem. When I say maximum depth equal to three, let's look at the tree. Let's look at the decision

50:12

free how it looks like. This is how my decision tree will look like for max depth equal to three.

50:18

Now, look exactly how I explain. This we'll see, it's a simple one. Depth equal to three. Maximum

50:23

depth is equal to three. Depth one, depth two, depth three. That's three levels of questions you're

50:28

asking. This automatically bunder. And and the nodes are basically about the features.

50:34

Now, features, look. Data in study hours, sleep hours, there are distractions,

50:39

right? But output, pass or fail. So leaf node will always have the output.

50:42

Yeah, or pass or fail. And you're traversing through the notes.

50:46

All this root node and the intermediate nodes, you're asking questions of your data.

50:50

I mean, questions of your features.

50:52

That study hours come, distractions come,

50:54

have, sleep hours, jada, or whatever is. Based on that, you're actually answering.

50:58

So this is the way how we can think through a decision tree. And this is the way to write.

51:02

And the rest of the story is very similar.

51:04

started my session by saying, you know, from a implementation and practical perspective,

51:09

nothing changes. Same train test split, same dot fit, dot predict, dot score, nothing changes.

51:14

So only key takeaway until now, whatever we, we learned, we looked at the intuition behind another

51:22

algorithm called a decision tree where we are basically, the machine is basically creating a set

51:28

of rules. It is building a tree and is building a flow chart kind of structure.

51:32

And the prediction is happening based on that.

51:34

this is what we saw. Okay, but the implementation of that's the way to look at it.

51:39

Now, let's continue on.

51:41

The next thing that we will talk about is a, is related to decision tree and this is this is actually

52:02

called random forest.

52:04

is random forest. The random forest stands for wisdom of the crowd.

52:09

Okay. Let me give you some analogy. Let me give you some context behind what we are discussing here.

52:14

Okay. What are we even talking about here? What are we talking about here?

52:17

Okay. So, um, what we have done so far is like a single model.

52:25

I'm now abit up a single model. Right. If you see, whatever we have done so far, whatever we have

52:30

built so far is a single model. We have built one single model on the entire, uh,

52:34

data. Okay? Now, sometimes it can so happen that whatever model you have built,

52:44

that model is highly biased. Oh, can't. You're, you're taking the whole data and you're building a

52:49

single model. On the entire data, you are building a single model. You're building a single model.

52:54

You're building one single model on the entire data. Now, it can absolutely happen that whatever

52:59

model you built, there is a possibility that that that model might become biased.

53:04

But that model is already biased. That is the, that is the thing that we are talking about here.

53:10

And, and that exactly is what the, you know, the, the idea is when it comes to building a collection of many, many decision trees.

53:25

So you can see that a single tree can be, is good, but it can be biased due to how it is getting formed.

53:32

So why not we create multiple trees?

53:33

And this is what a random forest is. So in short, there is a particular term that we use called an

53:39

ensemble model. Okay, so ensemble can't what? Ensemble can't what is. It is a collection, basically.

53:47

Ensemble stands for collection. So, I'm going to give you another, you know, simple analogy to help you

53:53

relate to it. Let's say you, you know, you are in a company.

53:59

Any of company in a company, so, what if any company may any decision lia so, what is it basically one

54:03

person's decision. It is never one person's decision, right? If you, if you're trying to do

54:07

decision making in a company, it is never one person's decision. It is basically a collective

54:12

decision of a group of people. It is basically a collective decision of a group of people. A group of

54:17

people together have to decide or to vote. And even something as simple as let's say, where you want to go

54:21

for a team lunch. So, so the manager of the team says, hey, we want to go to this place.

54:28

So that is a different thing. But usually there'll be a vote and there'll be some, you know, there'll be

54:33

some resolution, you know, let's say seven people will vote, we'll go to this place and three

54:37

people vote we go to this place. So the majority is considered. So this way we can remove the biases.

54:44

If you ask only one person to answer which place they will go, they will be biased. So instead of doing

54:51

that, you are asking a group as a whole. Any kind of company decision making happens this way. And

54:56

there are so many other real world applications. Like if you look at a jury, whenever you're looking at very

55:02

important cases.

55:06

Okay, whenever you look at

55:09

these important cases and all, right?

55:14

So there also what will happen?

55:16

There's never one single judge who will decide the outcome of a case.

55:21

Because a single judge can be biased.

55:23

That's to bias in a case.

55:25

But it's never the decision of one single judge.

55:30

It is always a decision of a group of judges.

55:32

So let's say judge one will say, banda guilty, judge two will say banda guilty and judge three will say

55:37

a person is not guilty. So two people say guilty, one person says not guilty, they'll be a vote.

55:43

The jury is a very common concept, right? Even Supreme Court where, you know, when, uh, there's a

55:47

jury, right? So it's not just like one judge who is deciding. Sometimes for very important cases,

55:52

there's a jury that sits. And in fact, this another very good example I can think of is

55:57

who can think of is, who can be can be can't caropati. If you look at KBC.

56:02

asked you. And let's say, you don't know the answer to the question.

56:08

So, what do you can phone a friend?

56:10

Now, phone of rent, what if the other person knows the answer, he'll be, but, you know,

56:14

let's say, what if the question is on some topic that the person doesn't know?

56:17

He doesn't know. He doesn't know. He doesn't know. So audience poll always works.

56:21

If you historically study and if you have read about it, so, audience poll in what

56:26

is, that? Let's say there are 100 people sitting in the show.

56:30

Now, nobody's a superhuman. They're all average people.

56:32

like you and me. We are all average people, right? We're not super humans, right? So we are all like,

56:37

so it is like saying that none of us in this class know everything.

56:42

If you're, if you're, I'm working on it, but maybe I'm very bad in history.

56:48

If you're all, sir, what 18, 19 in what happened? No, no, what happened? And I, yeah,

56:53

all the same, we'd like this person, this war started in dash. We had to remember. Memorize

56:59

So, but the point is if you do audience poll, the interesting part is,

57:07

one person will not know everything. Every person is average.

57:11

He's this thing a good, this thing, this thing, it's this thing, it's a good

57:13

and this thing, it's a thing, what's a thing, such a part, everybody's an average person.

57:17

But the wonderful thing about audience poll is majority vote, wisdom of the crowd.

57:22

The way, the word, the way, the word. And this is actually a very studied mathematical concept.

57:28

But this is a joke-wale thing not.

57:29

I mean, yeah, this is a lot of, uh, lot of, lot of, lot of mathematics around it as well.

57:37

You can read about it.

57:38

It's pay, coffee researched here, wisdom of the crowd, and there are a lot of models around this also.

57:43

There are reasons why it works.

57:44

I'm not going to get into that.

57:46

But averaging works beautifully.

57:49

You know, some person can be right, some person can be wrong, but the group as a whole is almost

57:53

always right.

57:55

Maybe I'll give a great example for this cohort as a whole.

57:58

You know, there are 23 people.

57:59

There are actually many more people in the cohort.

58:00

Some people, sometimes they are attending.

58:02

But mostly there are a lot of people in the cohort.

58:05

And different people can have different opinions, right?

58:08

But the majority as a group is a very powerful indicator.

58:12

The majority as a group, your voice is a very powerful indicator.

58:16

So again, we are looking at wisdom of the crowd.

58:19

What is the crowd saying?

58:20

What is the group as a whole saying?

58:22

I hope you are, because see, again, again, again, if you're a cohort aspect

58:27

if you're going to link kind of different people kind of different opinions, right?

58:31

They say person one say, sir, this say, sir, this a say, caro, person two says, sir, this a

58:35

caro, person three, sir, sir, you say, but the group as a whole is a very powerful indicator

58:39

for us, wisdom of the crowd, because that's an important thing.

58:43

And this is related to what we call an ensemble model.

58:46

Okay, so much, everybody's able to relate to it.

58:49

And you can, and you can read about it.

58:51

Audience poll is almost never wrong.

58:53

Ha, it might be very close at times, but very rarely audience poll has gone.

58:57

gone wrong.

58:58

Chit many KPC's what had.

59:00

Usually, audience poll doesn't go wrong because of the wisdom of the crowd effect.

59:04

Okay?

59:05

Now, how does this relate to what we have discussed so far?

59:09

So, where are we right now, guys?

59:11

Tordaer a bit earlier, we made a decision tree.

59:13

We took the data, we used some algorithm.

59:15

And on that basis, machine made a tree-like structure

59:18

we built a decision tree model, which is looking like a flow chart.

59:24

And we told that that tree is like a flow chart.

59:26

And we told that that tree is like a.

59:27

single model, that biased can.

59:30

Now we are discussing, we're not we will build a forest of trees, and that is called

59:35

the random forest.

59:37

That's the intuition.

59:38

This is the thing.

59:39

And there's a very simple.

59:40

The mechanics of it is a little different.

59:42

That we how we have to give you some intuition.

59:45

We have to give you some intuition.

59:47

We have every tree to make a different data.

59:47

So you have got a full data.

59:48

You're all data from a tree being.

59:50

So random forest in intuitively, if you are curious to know, that we, sir, we're trying to

59:53

here.

59:57

So if you have some rows, tree one, you have a little data,

1:0:01

tree two, two, a little different data do you.

1:0:03

Tree three, three, a different data.

1:0:04

So you're trying to train the trees in different ways.

1:0:07

So we're getting many, many decision please.

1:0:09

Okay?

1:0:10

What is the tuning knob?

1:0:12

Very important.

1:0:13

Most important tuning knob in random forest is called N underscore estimators.

1:0:17

This is your tuning knob.

1:0:19

Okay?

1:0:19

And N estimators tells you how many trees we have in the forest.

1:0:25

Here on two, two.

1:0:27

Examples from layer.

1:0:29

Example number one, we are taking, you can see we are, we are considering two examples right now.

1:0:36

Example one, we are considering n-stimators equal to one.

1:0:40

And example two, we are considering, example two, we are considering n-stimators is equal to 100.

1:0:47

N-stimates equal to one means we have a random forest with a single decision tree.

1:0:52

That is the meaning of an estimators equal to one.

1:0:54

That means we have a random forest with a single decision tree.

1:0:57

A key tree is.

1:0:58

So, that is the only model.

1:1:00

That then ensemble concept is useless.

1:1:03

Then it's anyways a useless thing.

1:1:05

It's not a good thing, right?

1:1:09

And on the contrary, we have an estimate as equal to 100.

1:1:14

Too many estimators overfitting.

1:1:17

100 tree forest.

1:1:19

That's the intuition.

1:1:20

So this is the way how you can look at the overfit and underfeit part for a decision tree.

1:1:25

So just keep this in the back.

1:1:27

of your mind.

1:1:27

So overfitting, like, if I have to just summarize the conversation for you,

1:1:32

let me just take a minute and summarize the conversation for you.

1:1:35

So for decision tree, what happens is, in fact, you know, we can go back to our first June.

1:1:47

One second.

1:1:48

This was, I think, back in 27th May, you know, 2017 or 29 to me upload here.

1:1:52

29 comment upload.

1:1:54

Just give me one second.

1:1:55

No, sorry, not this one.

1:1:57

Um, not this one, the day prior, 20th.

1:2:02

Huh, this one.

1:2:03

If you remember this diagram and uploaded it.

1:2:05

Yeah, but I'll be better because the connect will be very clear to you.

1:2:10

This is, this is the model accuracy curve, overfitting, underfitting good fit.

1:2:13

This is all we are doing in ML.

1:2:14

Okay.

1:2:15

You know, kithen every, could be, a algorithm lay low, regression low, classification low.

1:2:19

This is the same story we've been discussing for the last one month.

1:2:22

Basically, in different, different ways.

1:2:23

So, we are ultimately trying to build the best model.

1:2:25

that we are right right?

1:2:27

So for a decision tree,

1:2:29

yeah, your maximum depth, okay?

1:2:32

So, if the depth is, if the depth is, if the depth is very high,

1:2:39

depth is very high, the model will overfit.

1:2:43

Very high depth.

1:2:44

Overfit overfid over.

1:2:46

And as you reduce the depth, that knob is, as you reduce the depth,

1:2:50

you get depth equal to one.

1:2:52

You underfeit.

1:2:53

And you have to find what is the depth in between.

1:2:55

Depth one is underfeited, depth, or more overfit.

1:2:58

It's the beach of value.

1:3:00

You have that you need to know, okay?

1:3:02

Coming to the story of n-stimators, I don't have space here, so I'm up on up on,

1:3:06

okay, now you'll understand.

1:3:08

N-stimators.

1:3:10

N-stimators.

1:3:13

Same way, if N-stimators is very high,

1:3:17

the model will be a highly highly over-fit model.

1:3:18

That means, N-stimators high is what is, what is, what is?

1:3:21

That means, in that forest, that forest, that forest is comprised of many,

1:3:25

many trees.

1:3:27

I mean, that the committee is,

1:3:28

which basis on decision lay go,

1:3:30

the committee has too many people.

1:3:32

That means it's a very complex model.

1:3:34

Overfit.

1:3:35

Too detailed.

1:3:36

Not good.

1:3:37

And on the contrary, what was the other extreme we looked at?

1:3:41

If N-stimate is equal to 1.

1:3:42

1.1.

1:3:44

If N-stimate as equal to 1, under-fit.

1:3:47

What does it mean?

1:3:48

N-stimate is equal to 1 means it's a dummy model.

1:3:51

Dummy model.

1:3:53

So N-stimator is equal to 1 means you only have,

1:3:55

like the whole random forest has only a single decision tree.

1:4:00

That is an estimate is equal to one.

1:4:01

So the forest has only a single tree.

1:4:04

So this is the way how you can, you know, get towards a good fit kind of a zone.

1:4:08

So on one hand, we have underfit.

1:4:10

On the other hand, we have overfit.

1:4:12

We are trying to find out what is the good, what is the good fit model.

1:4:15

And now we will see some practicals.

1:4:17

We'll see some applications.

1:4:19

And the key learnings until now were depth and an estimators.

1:4:23

So these two things to understand to understand.

1:4:25

We have to go through the structure.

1:4:27

We have to go through the flow chart.

1:4:29

We have to understand what forest starts.

1:4:30

I hope now everybody is able to get a sense, get the intuition key.

1:4:34

Chishin'h.

1:4:35

But remember, I'm going to repeat again, guys.

1:4:38

The story remains exactly the same.

1:4:40

Nothing changes here.

1:4:42

Baki, you're up your.

1:4:43

Ackh, upke, up-fate, dot-predict, dot confusion matrix.

1:4:47

Nothing changes.

1:4:49

False negative, false, false positive.

1:4:50

All these things remain very, very similar.

1:4:52

Okay.

1:4:53

Now, this is one.

1:4:55

more thing that I want to talk about with respect to random forest.

1:4:59

This is, this is the, one of the best things about random forest.

1:5:03

That is that they can help you find the feature importance.

1:5:07

Because just keep this at the back of your mind.

1:5:09

So whenever you work with something called a random forest,

1:5:12

and this is another very nice, you know, pictorial depiction of what is happening,

1:5:16

updakes that you.

1:5:16

This is actually what happens.

1:5:18

So there are four decision trees that you're creating.

1:5:21

So this is like an estimate is equal to four.

1:5:23

Because you're upchar trees are you.

1:5:24

But the committee in charge trees.

1:5:25

And an estimate is equal to 4.

1:5:28

So 3-1 will do some prediction.

1:5:29

3-1 will say, yeah, person is diabetic.

1:5:31

3-2 will say person is diabetic.

1:5:33

You know, 3-3 will say person is diabetic.

1:5:36

And 3-4 will say person is not diabetic.

1:5:38

So majority vote will be.

1:5:40

Team-logue is a diabetic-year.

1:5:42

4th person, 1 person is saying not diabetic.

1:5:45

So the model will predict diabetic.

1:5:47

That's the way to look at.

1:5:48

This is a very nice pictorial depiction of what is going on inside a random forest.

1:5:53

Now, as I was mentioning,

1:5:54

a very, very important idea of random forest is something called feature importance.

1:6:00

Just keep this at the back of your mind.

1:6:04

It is able to automatically figure out which features are the most important for making decisions.

1:6:13

So this is a very, very important aspect of a random forest.

1:6:16

So for example, whatever we did here until now, you can't see what we did here until now, whatever we did here until now,

1:6:22

we have to data set data set already have we already talked about it.

1:6:27

So we have got study hours, sleep hours, and distractions.

1:6:30

So we can build a model and now we can study the feature importance.

1:6:35

So we can actually study that, hey, what is the percentage importance for the study hours feature?

1:6:40

What is the percentage importance for the distractions feature?

1:6:43

And what is the percentage importance for the sleep hours feature?

1:6:46

How important are these respective features?

1:6:47

How important is the study hours feature?

1:6:50

How important is the distractions feature?

1:6:52

and how important is the sleep hours teacher.

1:6:56

And based on the context of my data,

1:6:58

you can clearly see that study hours is actually

1:7:02

one of the most important features.

1:7:04

It is 74% important.

1:7:06

Study hours is 74% important.

1:7:08

That means it is one of the most important,

1:7:10

one of the more important features.

1:7:11

And you will ask me that, sir,

1:7:13

what is the benefit of it?

1:7:16

Benefit to clear.

1:7:18

Because this is the single most important thing

1:7:20

we are trying to do in ML.

1:7:21

Machine learning, ma'am,

1:7:22

what are we trying to do in ML?

1:7:25

We are ultimately trying to build,

1:7:26

take features which are important for the prediction, right?

1:7:30

We are ultimately trying to figure out which of the inputs

1:7:34

are good predictors of the output.

1:7:37

That is what we are ultimately trying to do.

1:7:39

Which of the inputs or features are good predictors of the output?

1:7:42

That's the ultimate problem that we are trying to solve.

1:7:45

Okay, so you have to see that study hours is a good feature.

1:7:49

You have a, if you have a data set may,

1:7:50

so features, 50 features.

1:7:53

So, feature importance, you can

1:7:54

make out of which is the most important feature?

1:7:56

And then using that feature, you can go back and build the model.

1:8:00

Because I told you, before as well,

1:8:02

not all the features will, you know, will be important.

1:8:07

Some features will be important, some features will not be important.

1:8:10

We are trying to figure out which of the features are more important.

1:8:13

And we will keep only those features and build a model.

1:8:16

Joe features important not, that we'll motted them.

1:8:19

And that is it.

1:8:20

iterative way we will have to proceed.

1:8:22

Now, let us see one more example.

1:8:25

So this is the, this is the disease one, just a sample disease prediction we are actually doing.

1:8:29

You can see, I think this is a story we have already seen before.

1:8:32

So I'm just trying to kind of simulate this once again for you.

1:8:35

Yeah, your cancer prediction, disease prediction while I use case.

1:8:38

And once again, we are building a, a kind of a decision free classifier.

1:8:42

Same way, dot fit, dot predict, up the exact you know, we are taking the data, we are doing a dot fit,

1:8:48

dot predict and based on that we are getting this.

1:8:50

particular thing, all of you are able to see. And the reason I'm doing this example is because

1:8:56

I wanted to basically tell you the intuition behind what exactly is a, you know, is a kind of a

1:9:03

confusion matrix. Okay? So Confucian matrix to humne, bohout detail in discuss here already.

1:9:08

So today again, I'm trying to give you some, some sense on this confusion matrix part.

1:9:12

Okay? So we're going to see this here. So I think we can take a short, very quick break right now.

1:9:17

And after the break, we will come back and look at.

1:9:20

this example once again, level three onwards.

1:9:22

Okay, this we'll take.

1:9:24

Rare disease problem.

1:9:26

So the interesting learning here will be that accuracy both high, but then if you look at the false

1:9:32

negatives, it will be very high.

1:9:33

So this is the accuracy issue.

1:9:36

And we will see what is precision recall F1 score.

1:9:38

We have seen this before.

1:9:40

Confucian matrix, but we'll back see this repeat.

1:9:42

And in the context of that, we will understand like another metric called ROC, AUC.

1:9:48

Okay?

1:9:48

And finally, we will incorporate this.

1:9:50

into a real world case study on breast cancer.

1:9:53

This is a simple case study we will be doing.

1:9:55

So same way we will take the data, we'll build the model.

1:9:59

And here we're up, other models banay and we will compare the models, okay?

1:10:04

Don't do case studies going to this.

1:10:06

It'll be totally demo based from here onwards.

1:10:08

T, okay?

1:10:10

So guys, we can take a break and come back.

1:10:13

So the notebook for the session is uploaded already under the respective folder.

1:10:19

So we are already in first June.

1:10:20

So we can find the Jupita notebook for the session uploaded under this particular place.

1:10:25

Take it.

1:10:26

So everyone can take it from here, please.

1:10:28

Okay. So I will see you back after five minutes then.

1:10:50

Thank you.

1:11:20

Thank you.

1:11:50

Thank you.

1:12:20

Thank you.

1:12:50

Thank you.

1:13:20

Thank you.

1:13:50

Thank you

1:14:20

Thank you

1:14:50

Thank you

1:15:20

Thank you

1:15:50

Thank you

1:16:20

Thank you

1:16:50

Thank you

1:17:20

Thank you

1:17:50

Thank you

1:18:20

Thank you

1:18:50

Thank you

1:19:20

Okay,

1:19:24

So we'll come back.

1:19:25

So we'll continue on

1:19:27

So we'll continue on.

1:19:28

All right.

1:19:30

All right.

1:19:32

So let us go back to our use case.

1:19:34

Let us go back to our use case.

1:19:38

I'm going to continue on from the

1:19:40

from this particular use case.

1:19:42

The you know, the patient disease

1:19:45

use case here if you see and what all that all that we are doing

1:19:48

all that we are doing in this particular problem is

1:19:49

particular problem is we have simulated some data.

1:19:54

So we are looking at the different features of the person, health metric one, health metric two.

1:19:58

They don't know features.

1:19:59

And based on the different, these two features of the person, we are trying to predict the status.

1:20:05

But the way is the person having a disease is the person not having a disease.

1:20:08

So status will basically tell you, you know, whether the person is having a disease or not.

1:20:13

So that is the problem that we are trying to solve.

1:20:15

So we are trying to predict based on the features of the

1:20:19

person, whether the person is having a disease or the person is not having a disease.

1:20:26

That is what we are trying to do here.

1:20:28

Specifically.

1:20:29

Okay.

1:20:30

Now, so this is a simulated data.

1:20:34

So as you can clearly see, we have got health metric 1, health metric 2 and status is the data set we have right now.

1:20:40

So I'm this to simulate here and we are simulating the predictions also.

1:20:46

Okay?

1:20:47

So we are first trying to build a very

1:20:49

basic decision tree model which is we call it a shallow model or a very lazy model.

1:20:54

But you are why are keeping maximum depth equal to 1?

1:21:01

I just wanted to show you what what's really happening when maximum depth is equal to 1.

1:21:07

So we will do the dot fit x comma y same story and we will also go back into the dot predict.

1:21:15

We will get the predictions.

1:21:19

And finally, based on that, we will calculate the accuracy.

1:21:21

So accuracy calculation is two things.

1:21:23

Whatever we have done so far, we can do model dot score,

1:21:28

but we can also use this particular function.

1:21:30

Now model dot score we use can use this function also.

1:21:33

Both ways the score function will work.

1:21:37

And what we wanted to demonstrate through this exercise is that

1:21:41

decision tree we've made.

1:21:43

Accuracy is coming out to be very high.

1:21:46

Accuracy is coming out to be 99%.

1:21:48

But the moment you look at the Confucian matrix, you will get the issue, what is going on.

1:21:53

So let me, let me take a minute and talk about it. What is, what is going on right now.

1:22:00

Okay.

1:22:01

Okay.

1:22:02

You have the data set is.

1:22:04

Sapset, whatever data set you have, that data is highly imbalanced.

1:22:07

That data is highly imbalanced.

1:22:10

So we have created a heavily imbalanced data

1:22:13

which will simulate how things in the real world will be.

1:22:17

world will be.

1:22:18

If you in real world,

1:22:19

if you're doing that,

1:22:21

then you have a heavily imbalanced data

1:22:24

will be.

1:22:25

I mean, out of every 100 patients, let's say,

1:22:29

90 of them will have a disease

1:22:32

and 10 will not have a disease.

1:22:35

I'm sorry.

1:22:36

90 will not have a disease and 10 will have a disease.

1:22:40

So sick low is,

1:22:42

see if you,

1:22:44

I'm just giving an example.

1:22:46

You go to a shopping mall.

1:22:47

There are healthy people you see around.

1:22:49

At least what you are seeing around is healthy, right?

1:22:51

People are walking and they're roaming around.

1:22:54

So, what will go?

1:22:55

So what you'll,

1:22:56

you're,

1:22:57

you're going to surveyed,

1:22:58

there are,

1:22:59

majority is a majority.

1:23:01

Majority will be,

1:23:02

majority will go,

1:23:03

you will see only one or two people will be sick.

1:23:05

Most will not be sick.

1:23:07

Most will not be sick.

1:23:09

That is what we referred to as in-balanced data.

1:23:11

We have already discussed

1:23:12

same story.

1:23:13

If you remember, they are all connected modules.

1:23:15

If you remember, we cover something called Smote,

1:23:17

long time.

1:23:17

back, data pre-processing time,

1:23:19

it's all connected.

1:23:21

It's called an imbalanced data.

1:23:23

Imbalanced data,

1:23:24

there are

1:23:26

lot of examples of one particular class,

1:23:30

but very few examples of another class.

1:23:33

That is what you're able to see right now.

1:23:35

Now,

1:23:37

this problem here,

1:23:38

you know,

1:23:39

if you make any model

1:23:41

let us train a basic model.

1:23:43

And this is the basic model, right?

1:23:45

It's a very basic one.

1:23:46

Decision tree with max depth one.

1:23:47

I told you, Max Step 1, underfit.

1:23:49

If you, if you'll be better,

1:23:51

but this is horrible model.

1:23:53

We'll train a basic model.

1:23:55

Problem here is that when you train a basic model,

1:23:58

what it will do is it will predict everybody to be healthy.

1:24:01

It is like, you know,

1:24:04

so what you are able to see here

1:24:08

is the Y actuals.

1:24:10

This side, whatever you are seeing are the actuals.

1:24:14

This side, whatever you are seeing are the actuals.

1:24:16

This side, whatever you are seeing are the actuals.

1:24:17

and whatever you have here will be the predicted.

1:24:24

Whatever comes here will be the predicted.

1:24:27

Or after the model,

1:24:30

whatever model you end up building on your data,

1:24:34

right guys, whatever model you end up building on your data,

1:24:38

whatever model that you have built,

1:24:40

that model

1:24:43

is predicting everybody to be healthy.

1:24:46

everybody to be healthy.

1:24:48

1,000 people are all 1,000 that model is predicting to be healthy.

1:24:52

We can imagine the example, it's like,

1:24:55

you're going to doctor to go to,

1:24:57

doctor, a,

1:24:59

some thought process,

1:25:00

who's going to be healthy, healthy, healthy, healthy, healthy.

1:25:03

So what will happen?

1:25:05

How accurate do you think the model is right now?

1:25:07

Actuals 990 healthy 10, 10, 6,

1:25:10

predicted thousand healthy.

1:25:13

What is, what are we trying to do in ML?

1:25:15

How accuracy?

1:25:16

We are trying to do actual to predicted comparison.

1:25:20

So accuracy, how did?

1:25:22

99% did not?

1:25:24

But do you think the doctor is a good doctor?

1:25:27

No, that doctor is just

1:25:30

doing random guessing.

1:25:32

Doctor is playing safe.

1:25:34

If he's sick not to say

1:25:36

if there's going to go wrong if

1:25:38

someone if you can ask them,

1:25:39

that doctor is just a random dummy doctor.

1:25:42

Doctor is predicting everybody to be healthy.

1:25:44

But he's all healthy predict

1:25:45

healthy predict,

1:25:46

it's,

1:25:47

then he's accuracy is 99% accuracy.

1:25:49

And this is

1:25:50

because of imbalanced data.

1:25:51

So that's why accuracy is a

1:25:53

problem, the danger of accuracy.

1:25:55

You should never rely on accuracy.

1:25:57

We have you when we were

1:25:59

discussing Confucian matrix for the first time.

1:26:01

I taught you this concept then.

1:26:03

There also I had a similar use case I discussed.

1:26:06

I told you that don't blindly follow accuracy.

1:26:09

Same thing here.

1:26:11

Because accuracy is 99%

1:26:13

actually this is,

1:26:14

actual here, model is predicting

1:26:16

all healthy, so accuracy the 99%

1:26:18

but what we want here is

1:26:21

what is the class level accuracy.

1:26:25

I don't want to know the individual accuracy

1:26:27

that overall accuracy is

1:26:30

overall accuracy

1:26:32

fine 99% is the overall accuracy that we are getting.

1:26:35

But what we really want to understand right now is the class level accuracy.

1:26:39

What we really want to understand is the class level accuracy.

1:26:42

That means more specifically we want to understand

1:26:43

More specifically, we want to understand what is the accuracy for each and every individual class.

1:26:48

For each and every individual class, what is the accuracy?

1:26:50

What is the accuracy?

1:26:52

We want to find out what is the accuracy for each and every individual class.

1:26:57

That is what we have to find out here.

1:26:59

So what is the class level accuracy?

1:27:01

How do we do that? Let us see.

1:27:02

Even more important, we will calculate the Confucian matrix here.

1:27:05

Confucian matrix we draw.

1:27:07

So we will repeat not we have discussed it before as well.

1:27:10

But just to

1:27:12

just so that everybody is clear with the story.

1:27:16

I've already done Confucian matrix two times.

1:27:19

So today is actually the third time we are discussing it.

1:27:23

But everybody knows it, everybody remembers it, I'm sure.

1:27:25

So this is exactly what your Confucian matrix looks like.

1:27:29

Everybody remembers it.

1:27:30

So you plot your actuals along the rows.

1:27:34

You plot your predicted along the columns.

1:27:36

Columns to have predicted.

1:27:37

And this is how it looks like.

1:27:40

0101.0.0.0 means not.

1:27:42

disease. One means you have a disease.

1:27:44

Actual 0 you don't have a disease.

1:27:46

Actual one, you have a disease.

1:27:48

And based on that we have TN, Tp, FN, FN, FN, FN, FP,

1:27:50

like that.

1:27:51

So TN is true negative, TP is true positive.

1:27:53

FN is false negative. FP is false positive.

1:27:56

We are able to see that.

1:27:58

So how do we understand the meaning of true positive?

1:28:02

What is true positive?

1:28:04

True positive means model predicted positive

1:28:06

and the actual is also positive.

1:28:08

But the model predicted,

1:28:10

you have a disease.

1:28:12

actually also you have a disease.

1:28:13

True negative matter, model predicted you don't have a disease,

1:28:16

actually also you don't have a disease.

1:28:18

False positive means model predicted you have a disease, but in reality you don't.

1:28:22

And false negative means model predicted you don't have a disease in reality you do.

1:28:27

So that's the way how we understand the Confucian matrix.

1:28:30

And if you remember, with respect to the Confucian matrix,

1:28:33

we are actually discussed two other very important pillars.

1:28:37

So two other very important pillars we are covered were precision and recall.

1:28:41

and recall.

1:28:42

Long back.

1:28:43

So when I was, if I just had to share my screen with you, the other one.

1:28:48

If you all recall, this one we had very briefly talked about that time.

1:28:54

So I showed you my Confucian matrix diagram.

1:28:57

And that time I'd explained to you what is T NTP, F and FNFP.

1:29:03

And I'd also explained to you what is precision and what is recall.

1:29:06

So what is precision?

1:29:08

Precision is the ability to correctly predict how,

1:29:11

well you are able to predict something, that is how we go back and define the meaning of precision.

1:29:16

And recall tells you how well you're able to detect something.

1:29:20

So precision is the ability to correctly predict, whereas recall is the ability to correctly detect.

1:29:26

Precision again tells you that, and the best part is that you can do it in a class-wise basis.

1:29:32

Accuracies is overall.

1:29:34

What we were discussing so far, TN plus TP by total.

1:29:36

Overall number of correct predictions by total number of predictions.

1:29:39

That is accuracy.

1:29:41

But what you can now start to do is, as I told you, overall is not important anymore.

1:29:48

Because overall the 99% are are because of my imbalance class problem, right?

1:29:53

But what is important right now is, how is the model performing for each and every individual class?

1:30:00

Here here, there are two classes.

1:30:02

Two types of outputs are.

1:30:04

Either disease have or disease not.

1:30:07

So now for the disease class, how is the model doing?

1:30:11

That is my main objective.

1:30:13

My main objective is to identify how well is my model able to detect and predict diseases.

1:30:19

So I want to know what is the precision and recall of my one class.

1:30:23

What is the ability to correctly predict?

1:30:26

That means if you look at the formula,

1:30:30

I just try to break it up and explain.

1:30:33

35 by 46,

1:30:35

out of 46 predicted values,

1:30:40

46 people you are predicting.

1:30:41

to have a disease out of which 35 are correctly predicted.

1:30:46

So how well you are able to predict and recall tells you how well you're able to detect.

1:30:52

Out of 55 actual ones, how many you're able to correctly detect.

1:30:57

So that's precision and recall for you.

1:30:59

So in simple terms, again, the formulas on all are just given for reference, you can, but what is

1:31:04

important is the big picture idea.

1:31:08

Big picture idea is their class level accuracies.

1:31:11

So precision and recall are both telling you how well the model is performing with respect to their one class.

1:31:18

One, one is saying how well you're able to predict the disease.

1:31:23

And the other is how well you're able to detect the disease.

1:31:26

If someone's actually disease, are you able to catch it.

1:31:31

So both these metrics are important.

1:31:33

So both of them to make them make one metric use called F1 score,

1:31:37

which is nothing but some kind of an average of precision and recall.

1:31:40

Actually, technically speaking, it is the,

1:31:41

the harmonic mean. So this is what we refer to as F1's code. And by combining this,

1:31:47

you end up getting this kind of a classification report.

1:31:50

Up your could say like. Classification report. So Confucian matrix will look like this.

1:31:57

And classification report will look like this. Here you'll be able to see the two different

1:32:01

classes right now. Class 0, class 1 up. Okay? Because it's a binary classification, remember. That's

1:32:07

why we are getting two classes. And you will also be able to see the, uh, the precision for the

1:32:11

classes, the recall for the classes, the F1 score for the classes and the support.

1:32:15

Support can matter of rows. How many data points do we have?

1:32:19

Means for the zero class, we have 99 points and for the one class, we have 55 points.

1:32:25

We are able to see zero class make it kind of data points. And one class make it data points.

1:32:29

We are able to track that. So 99 points for the zero class and 55 points for the one class.

1:32:34

We are able to see that. That's the intuition.

1:32:39

So this is giving you the class level accuracy.

1:32:41

And going forward, whatever we are doing, we will be concerned primarily about the F1 score.

1:32:46

Because F1 score we have both of combined and look at the overall accuracy.

1:32:51

Next time, the workflow will be you take a data, you fit a model, you build a model and you calculate the accuracy.

1:32:57

Tick, Moth score, dot score, train accuracy, test accuracy, whatever we've been discussing.

1:33:02

Now the new learning is that that accuracy is not the best metric.

1:33:05

So now we will rely on F1 score rather.

1:33:08

And you can see, at a high level, if you observe you can see that the F1 score for the

1:33:19

one class is actually lower. Zero class is higher, one class is lower. That means the disease

1:33:24

class is, the model is not doing that well. It will be the same for our case as well. And if you

1:33:29

want to go back to the story, what we discussed, same story is. It's the same story. It's

1:33:33

I don't know if you can't even if you can manually it's going, accuracy 99%

1:33:38

is TN plus TP by total. But the moment you start to look at the classification report,

1:33:44

if you're going to if classification report, then I've here here here here. If you're

1:33:49

here here, if you're made it. If you're classification report here here, the classification report

1:33:54

will tell you that it's a, you know, the real, the true quality of the model you'll be able to

1:33:59

get to see. Okay? Just a second, guys.

1:34:03

RF, we have here here.

1:34:07

Just give me one second, please.

1:34:14

Oh, because we're here actually

1:34:15

the other one classification report by, I care, whatever. Let me, let me print the classification

1:34:20

report for this one. So people already know the classification report.

1:34:24

So, this pay him on this. This we're on this. Okay, classification report. And you can take a look at it.

1:34:28

Very simple. The code is straightforward. So, yeah, Confucian matrix's a code is.

1:34:31

actual comma predicted and this is classification report actual comma predicted. And if you take

1:34:36

a look at it, let me run the code. This your Confucian matrix is. Accuracy is on 89%

1:34:41

whatever we discussed. But moment you look at the classification report, you will start to realize how

1:34:45

horrible this model is. So one class is, one class, much of the disease-wala class.

1:34:51

What disease-wala class may have the model is doing very, very poorly. In the disease class,

1:34:56

you can see the model is doing very, very poorly. So the model is giving a 0% precision.

1:35:01

0% recall and 0% F1 score for the disease class.

1:35:06

Disease class when the model is doing extremely poorly.

1:35:09

So 0% precision, 0% recall and 0% F1 score.

1:35:13

So the model is performing very, very poorly here.

1:35:16

Okay. So this is a poor quality model or false negative B does say. Does false negative say.

1:35:20

That means there are 10 such cases where model predicted, not, you know, disease, but actually having a disease.

1:35:26

So that's what we're able to see here right now overall.

1:35:28

And this is the overall idea behind what.

1:35:31

the concept of Confucian matrix basically is, okay?

1:35:37

What the concept of, you know, Confucian matrix basically is here overall.

1:35:44

Turns out there is one more kind of metric that we can also use.

1:35:49

Definitely the F1 score and, you know, is one metric, as I told you.

1:35:54

Instead of relying on accuracy, a better way to represent this will be by looking at the classification report.

1:36:00

So classification report can we can F1 score.

1:36:03

But F1 score itself is calculated mathematically based on precision recall,

1:36:08

which are in turn having FP, FN, these kinds of computations,

1:36:12

which I explained to you.

1:36:13

F1 score is a good metric going forward.

1:36:16

Another metric that we will use quite frequently going forward is something called ROC, AUC.

1:36:21

You can just keep this at the back of your mind.

1:36:24

So ROC AUC is referred to as area under the curve.

1:36:27

So there is a specific metric called AUC that we'll.

1:36:30

we use, area under the curve, or AUC metric basis, maybe a model to evaluate

1:36:36

it is a better metric.

1:36:39

And what you're able to see in this particular demo is you are able to see how the, you know,

1:36:44

the random forest is having a higher AUC than a decision tree.

1:36:46

And we know that, of course.

1:36:48

I mean, compared to an individual tree, compared to an individual tree, the forest will definitely

1:36:52

be better.

1:36:54

So that's what we can already relate to.

1:36:55

The random forest will definitely give you a better result than an individual decision tree.

1:37:00

And that is exactly what we are able to see on the screen.

1:37:02

Okay.

1:37:02

So the random forest is giving you a better result compared to an individual decision tree.

1:37:07

Okay.

1:37:07

So the new learning here is that accuracy is not a good metric.

1:37:12

We should not trust accuracy.

1:37:14

We will rather use F1's course and or another similar metric is called AUC or area under the curve.

1:37:21

Just remember that.

1:37:22

Okay.

1:37:22

So just keep this at the back of your mind.

1:37:24

You can, this copy derivation is coming from precision recall.

1:37:27

So whatever precision recall, I, uh, I, uh, I, I,

1:37:30

produced a while back to you.

1:37:31

So this particular AUC is also kind of derived from the same logic.

1:37:36

Okay.

1:37:36

So from a practical perspective, you need to just remember what, uh, what AUC is and how to use AUC.

1:37:41

So the usage of AUC is much, much more important.

1:37:45

Okay.

1:37:50

Although, exactly, like, that's what, that's what, uh, you know, I explained here could take.

1:37:54

So if you take a look at it back to, you know, back to the, uh, the prediction and detection

1:37:59

well, if you're, prediction is basically, uh, you know, along the predicted values are coming

1:38:05

along the columns and the actual values are coming along the rows, right?

1:38:09

So when I say precision, so that is again back to the formula.

1:38:12

So I just just just just trying to explain the formula a little bit what, what it is.

1:38:15

Okay, it's not needed for the class, but I'll again repeat for you, no problem.

1:38:18

So basically, uh, precision tells you how well you're able to predict once.

1:38:24

Out of 46 once, 35 are correctly predicted.

1:38:27

That is how we define precision.

1:38:29

So precision tells you how well you are able to correctly predict something.

1:38:32

Out of 46 ones, you're able to correctly predict 35 of them. If you look at the column total,

1:38:38

Gurteg, you're able to see we've got 46 once we are predicting, out of which 35 are correct.

1:38:43

So the precision is nothing but 35 by 46. Okay? What is recalled?

1:38:50

Recall tells you, recall is like a row total. Recall.

1:38:53

Recall, Dekrake, okay, how many actual disease people you've got?

1:38:56

there are actually 55 disease people.

1:39:01

So out of actually 55 disease people, we are seeing, there are overall 55 disease people we have got.

1:39:08

So out of overall 55 disease people, 35 we are able to accurately detect.

1:39:14

That is how we define recall.

1:39:17

Okay?

1:39:18

So 20 we are missing.

1:39:20

So that is how we can see precision report.

1:39:22

Actually, the formula is.

1:39:24

But then, yeah, I just try to explain to you.

1:39:26

that's what intuition? But when actual in use, you, you will just look at this

1:39:32

classification report and see what the class level accuracy is. This is called the class level accuracy.

1:39:39

So so far we were looking at the overall accuracy. Dot score. But now we will look at the class level

1:39:43

accuracy. He's zero class may how is the model doing? One class may how is the model doing?

1:39:48

Ah, exactly. It is, it is comparing the reality with prediction. Exactly. You're right. Absolutely. That is

1:39:53

what is doing.

1:39:56

And similarly another similar metric is called AUC.

1:39:59

AUC say, you know, you know, how it is, how it is, how the model is actually doing.

1:40:05

Okay.

1:40:10

All right. Now, moving on.

1:40:13

We will, we will try to put this into a larger use case.

1:40:16

And just to clarify, you know, precision, recall, uh, F1 score and ROC, AUC, all these four things.

1:40:26

Okay.

1:40:26

all these four things that we, you know, that we talked about here.

1:40:30

All these, you know, all these four things that we, that we explicitly talked about here, if you

1:40:36

see, all these four things will have the concept of, you know, 0 to 100%.

1:40:44

They will all range from, you know, a 0% all the way to 100%.

1:40:49

Okay.

1:40:49

So, so they will all range from 0% and they will all go all the way to 100%.

1:40:55

So that's one way to.

1:40:56

look at it. Okay, so they will range from 0 to 100%.

1:41:00

Just keep this at the back of your mind, all of you.

1:41:06

So that means the higher the value, the better it is.

1:41:08

Your accuracy, the higher it is, the better it is.

1:41:11

Precision recall the higher it is, better it is. F1 score, the higher it is better it is.

1:41:14

And same for ROC, AUC. Okay, the higher it is the better it is. Intuitively, what does it tell you?

1:41:20

Intuitively, all these metrics are telling you how well we are able to separate the classes.

1:41:25

Back to the story we did.

1:41:26

discussed in the very first classification session if you remember. So regression,

1:41:30

we are trying to find the best fit line. How will it fits the points? Classification, we are

1:41:35

trying to separate the classes. So even the AUC metric, what we are trying to do, the higher

1:41:39

the AUC value, the better we are able to separate the classes. Okay? So just keep this at the back

1:41:44

of your mind. This is a better kind of accuracy. So this is a real world case study now. This is the easiest

1:41:50

part because now we know the templates, we know everything. So we'll just try to put it together and

1:41:55

and show you how the comparisons basically work out.

1:41:59

So let us take a look at it. All of you can see, this is the breast cancer data.

1:42:05

So if you've got a data set, different different features of the person,

1:42:12

X, and based on that, we are trying to predict Y. So Y may be that,

1:42:16

does the person have cancer, does the person not have cancer? Yes or no.

1:42:20

Well, this type of data you have got, okay? So, so first, what are you doing? You are doing a train test,

1:42:24

split. You're splitting the data into x-ray and x-train x-tests, and then first thing,

1:42:29

we are building a decision-tree classifier. This is the baseline model that we are building. Dot

1:42:35

fate, dot predict, okay? We are finding out the score, dot score, accuracy, confusion matrix

1:42:42

classification report. You have a decision tree. And second, what are we doing? We are using a random

1:42:46

forest. And the idea is random forest is the better model. So an estimate as equal to 100. What does it mean?

1:42:53

it means it is a collection of 100 decision trees. This means it is the collection of

1:42:57

hundred decision trees and estimate is 100. So same thing, fit the model, do predictions. Dot score

1:43:06

calculate the accuracy and then finally create the Confucian matrix classification report and also

1:43:11

the feature importance. Feature importance. Feature importance, you have got out of all the features,

1:43:17

which are the most important features. Now when I run this, you will be able to see very

1:43:23

interesting expected, that decision tree accuracy is 94, random forest is better.

1:43:29

Accuracy wise, it is better. And even if you look at the other metrics,

1:43:34

the class level accuracy, now F1 score, look. Dono metrics in random forest is ahead. So this is to,

1:43:40

again, to further highlight the concept of ensembles and wisdom of the crowd that I was discussing,

1:43:46

instead of a single tree, when you build a collection of many, many decision trees, the model is always

1:43:51

better. And you can see here. There are three false negatives. Here

1:43:55

here only one false negative. So definitely, incrementally, this is the better quality model.

1:44:00

And this is the way how we do machine learning in practice. So we try one model. We see what

1:44:04

results we are getting. We try another model. We see what results we are getting. And that is how we

1:44:08

propagate. Okay. And finally, what you are seeing here is the feature importance.

1:44:12

You have 30 features. One message you can find out which particular feature is better.

1:44:17

Okay. So feature importance of deck sacked. This is a slightly better way.

1:44:21

I have visualized the feature importance for you. You can take a look at it out of all the 30 features,

1:44:26

which of the features are more important. The feature importance is the thing that we are looking at.

1:44:32

And random for us will give you that feature importance. Next, UCI credit card CSV. Yeah,

1:44:39

we've seen already. I think this we did. As far as I remember, I think this one we did last week.

1:44:47

Already, same story. You have in logistics made there, 27th Meiko. U.C.

1:44:51

credit card. Same story. Same data set we are taking right now. Let us see.

1:44:57

That's a subset by the data load can't just a second, guys.

1:45:05

But what I wanted to do is is the comparative analysis. Now that you know a lot of things.

1:45:10

We can compare in a better way. What is going on.

1:45:15

So let me quickly upload the dataset here.

1:45:21

I'm going to quickly upload the UCI data.

1:45:27

Oh, didn't get uploaded now. Just one second, guys.

1:45:51

All right, I'm going to load the data set here once again.

1:45:55

We know the story already. I'm not repeating it. So we are loading the data. We are splitting the data X, X, Y, train test plate.

1:46:01

So iteration one, we are trying a logistic regression. This is something we did exactly in the last class, if you remember.

1:46:07

We did logistic in the last session. So a model banaray. Dot fit, dot predict, get the predicted values.

1:46:13

Dot score, calculate the train accuracy, test accuracy, and generate the confusion matrix. So we have done this part already.

1:46:20

Okay. Next, what are we doing? Next, we are going ahead and,

1:46:25

so we are able to clearly see. This is a great demo. We are able to clearly see that

1:46:31

the accuracy seems to be very high. Very high. Very high. It's decent. Sevent 77, 78% accuracy we are

1:46:41

getting. But the practical thing I wanted to share with you in this class is,

1:46:47

Dekho, accuracy is coming out to be high. But the moment you take a lot,

1:46:50

look at your F1 scores, you are getting a very low value. Look at this. So the moment you take

1:46:59

a look at your classification report, the moment you take a look at your zero class and one class

1:47:05

particularly, you take a look at your zero class, you take a look at your one class. So the moment you take

1:47:11

a look at your zero class and one class, you are able to see that the scores are extremely low.

1:47:20

So, for the one class, the model is performing very, very poorly.

1:47:27

You can, you can see that.

1:47:30

Okay. So the model is performing very poorly.

1:47:35

Next, what are we doing?

1:47:43

Next, we are fitting a decisionary classifier.

1:47:48

Next, we will do a decisionary classifier.

1:47:50

I will fit a decisionary model and it will instantly fix the problem.

1:47:58

What are we doing? Decisionary classifier, maximum depth equal to three.

1:48:02

You can one be can try this out.

1:48:06

As you increase the value of depth, you can see you, the model will become more and more overfit.

1:48:12

This might take a long time to run.

1:48:14

This is exactly what I showed you in the concept so far.

1:48:17

Now you, you, you, you can see this code in.

1:48:20

So the model that you are able to get is highly, highly overfit.

1:48:25

So we are trying to find out what is the optimal depth of the tree.

1:48:28

So let's say with a three decision tree, we will build the model.

1:48:31

But most importantly, the objective is the comparative understanding today.

1:48:35

So comparatively, when we build the logistic last week, you're getting a high accuracy,

1:48:39

like in the scores are very bad.

1:48:41

Very basic model.

1:48:45

Very basic model.

1:48:47

Now when you go back and look at the

1:48:49

decision tree maximum depth equal to three when you're getting when you're building the

1:48:56

decision tree with maximum depth equal to three you are getting a much better quality model

1:49:03

accuracy is also high and most importantly the metrics are also high

1:49:08

so previously for logistic it was all 0 percent the disease class was doing very poorly

1:49:13

here here it's better incrementally the decision tree is giving us a better

1:49:16

that's the learning.

1:49:19

Number three, final point, random forest, even better.

1:49:25

That's the comparative piece I wanted to clarify today.

1:49:28

You do random forest, and estimators 100.

1:49:30

Accuracy is slightly higher comparatively.

1:49:33

And most importantly, F1's scores are slightly higher.

1:49:37

You have tuned to here here.

1:49:38

Random forest, the NSTMators have taken 100.

1:49:40

But usually you will see random forest will give you better quality results.

1:49:44

Okay, so this is a comparative way how we will have to apply.

1:49:46

approach machine learning. You take the data, try different different algos, build different

1:49:50

different models, calculate the accuracy, not just accuracy, but also look at the precisions, recalls,

1:49:56

F1 scores for the respective classes, and that is the way how you cumulatively compare, which model

1:50:03

is better? Is the logistic better? Is the decision tree better? Is the random forest better?

1:50:08

And just one final note I wanted to clarify for everybody. Please remember this at the back

1:50:12

of your mind that whatever we have discussed so far, random forest.

1:50:16

have discussed random forest in the context of classification, but please remember, the same

1:50:22

random forest can also be used for regression. So we have discussed random forest in the context of

1:50:27

classification, but the same random forest can also be used for regression. That is again not the main focal

1:50:35

point, but just wanted to add a small note on that. So whatever we have discussed is this,

1:50:41

right? SKL ensemble, import random forest classification.

1:50:46

This is what we have discussed. You can also import a random forest regressor. The story remains

1:50:54

exactly the same. Nothing changes. The same for decision trees also. So, decision tree or

1:50:59

random forest, whatever we saw today, decision pre, I mean, as a import the right?

1:51:10

So you can see decision tree classifier. Decisionary regressive. So both of these algorithms that we saw,

1:51:16

today can be used for classification as well for regression as well. So if you go back to

1:51:21

our California housing exercise, our advertising exercise, and many of those regression

1:51:26

exercises that we started our sessions with in linear regression and all, you can go back and

1:51:30

solve those same problems using random forest and it will actually get better quality results.

1:51:34

Just keep this at the back of your mind. In the modules, we don't have this because, you know,

1:51:38

ML is not the focus for these sessions. We are eventually going to go to Gen.

1:51:41

I in another few sessions from now, but just something to make you aware. The, the deal

1:51:46

these algorithms are kind of playing both roles. Okay, but from the module perspective,

1:51:50

we are focusing only on classification. So random forests and decision tree only from a

1:51:54

classification perspective. Okay, guys, I hope everybody is clear. So I think a lot of things were

1:52:02

known to us. So it was a more practical oriented session that I wanted to do where we wanted

1:52:08

to see some executions and all that. I hope everyone is aligned. Everybody's clear

1:52:12

with respect to whatever we, whatever we studied today. Okay.

1:52:16

And just wanted to summarize the core concepts that we covered in the session today.

1:52:21

Decision trees, what decision trees are the intuition?

1:52:24

What is the intuition behind that rule-based thing?

1:52:27

We talked about that in detail.

1:52:29

We talked about random forest. What is this concept of ensembles?

1:52:32

What is the meaning of ensembles? We covered that today, right?

1:52:36

Ensembles, hey, what does it mean to combine? What does it mean to vote?

1:52:39

What are the evaluation metrics? I think this is the third class we are talking about it.

1:52:42

First time we did this fighting backwards there in Smote, I remember.

1:52:45

So, there we talked about confusion matrix for the first time.

1:52:49

So, we discussed precision recall then. Then, and again, we talked about it last week.

1:52:53

Today is the third class we are talking about evaluation metrics with a bit more detail.

1:52:57

Specifically, the focus was more on precision recall f1 score.

1:53:01

And finally, the intuition behind what is ROC?

1:53:03

ROC is again, just like an accuracy metric, but better.

1:53:06

Accuracy is an overall metric. ROC will give you kind of an overall idea how the model is doing a more robust metric.

1:53:13

Just like accuracy, we saw it is.

1:53:15

Influence by imbalance, other imbalance data accuracy doesn't work, but RUC is a much better metric.

1:53:23

I hope everybody is clear. Any questions, guys. I hope all of you are aligned with what we discussed today.

1:53:29

And the next session, obviously, we will be getting into unsupervised. So we are slowly coming into some more interesting things now.

1:53:36

Okay. Yeah, yeah. Yeah, all good. Everybody is fine. Everybody's clear. Do let me know.

1:53:45

So, we are consciously trying to, we are consciously trying to keep a track of the time nowadays.

1:53:53

I think something that works well for everybody.

1:53:58

So generally we are for trying to wrap up the sessions a little early, sharp around 10, 10, 10, 15.

1:54:05

And at the same time, we have also increased more sessions.

1:54:09

So that instead of doing everything in one class, we are trying to break it across multiple sessions.

1:54:15

Okay. So because I think it gets a little late for you guys also. So that is a change that we have done in the recent classes. I think you can see that. So yes. So I will be ending my lecture right now. And at this point in time, I'll be passing it over to Pratab. And I once again wanted to thank all of you for being a part of my class and being so interactive as always. Thank you all of you. Good night to you. And I will see you all again on Wednesday day. Okay. Thank you. Take care. And I'll Pratab over to you.

1:54:45

thank you so much yeah thank you sir as always and guys i'm going to release the feedback poll now you already know the drill

1:54:54

answer the feedback poll and then after like i after a couple of minutes i will start the many minutes okay so just give me two minutes

1:55:08

until that point you can fill out the feedback form

1:55:15

Okay, I hope the feedback form is launched. Okay, yeah.

1:55:45

Okay.

1:56:15

in 90 meter. Give me a minute.

1:56:45

All right.

1:56:58

Alright, where is the okay, yeah.

1:57:02

All right.

1:57:03

Guys, I am going to release the Mentimeter quiz now.

1:57:06

And we can start presentation.

1:57:12

One second.

1:57:19

Cancel that, share.

1:57:22

Okay.

1:57:24

Share.

1:57:25

All right.

1:57:27

My screen should be visible.

1:57:30

Oh, I want the fifth question already.

1:57:33

Okay.

1:57:34

Start presentation.

1:57:38

Full screen.

1:57:40

Copy link.

1:57:41

All right.

1:57:43

Guys, join the Ventimeter quiz.

1:57:45

There are some, there are I think two people have still not voted in the feedback poll.

1:57:50

If you guys are not able to see the feedback poll, let me know and I will close it.

1:57:55

Is there anyone who is not able to vote on the feedback poll?

1:58:07

Guys, Chad, anyone?

1:58:15

Okay, in that case, I will close the feedback poll in 20 seconds.

1:58:21

Until that point, you can join the Mentimeter because I think we'll have a good session today.

1:58:33

A lot of people joining in.

1:58:37

Only 8 players?

1:58:44

Okay, 10. Good. All right. The feedback poll is being closed in 5 seconds.

1:58:53

And I'm closing it now. All right.

1:59:01

We'll start with the Menti meter quiz. The questions are relatively easy.

1:59:07

based on the class modes.

1:59:09

So let's see if you get them all right.

1:59:12

So which part of a decision tree returns the final class?

1:59:28

So this is like basically which is the part of the decision tree returns the final class?

1:59:36

part of the decision tree which gives you the final output.

1:59:39

Right? It's pretty easy to actually answer.

1:59:42

If you think about it. Yeah, leaf note.

1:59:45

So the leaf is going to give you the final answer.

1:59:47

Root is not going to give you the answer because that is the first comparison or question that

1:59:52

the this thing asks, decision tree asks.

1:59:56

Branch is irrelevant.

1:59:58

So.

2:0:06

All right, moving on.

2:0:22

Precision answers which question?

2:0:24

So when we are dealing with precision, what exactly are we measuring?

2:0:35

I think this one will everyone will get it correct.

2:0:49

Oh, okay.

2:0:52

Most of you did get it correct.

2:0:53

So great.

2:0:54

Yeah.

2:0:55

Precision means out of the predicted corrects, how many were actually correct?

2:1:00

Okay.

2:1:01

So this is something that you guys will need to practice.

2:1:04

It is.

2:1:05

I understand it is not exactly easy, but it is something that once you practice questions related to precision recall, accuracy, F1 score, R2, all of those things, you will start to get a better idea of it.

2:1:25

It's something, these things you will have to build an intuition on.

2:1:28

It will take it, it will take time, but you'll be able to do it.

2:1:34

to do it. It's not very difficult. You just have to practice a bit.

2:1:39

It seems we have lost two players. Okay. All right. All right. What is the random forest

2:1:56

is? Feature importance is summarize. So basically what is what is what do you do when you do when you do?

2:2:04

random forest is as has the feature importance.

2:2:18

This one might be a little, might be a little difficult. Then yeah. Okay, that's

2:2:33

Awesome. Most of you did get it correct. So yeah, I'm impressed.

2:2:38

Yeah, it's basically useful split contributions average across the trees.

2:2:43

That is how the random forest gets the wisdom of the crown.

2:2:49

Okay. So great job, you guys.

2:3:03

It's a little conceptually heavy, random forest and decision trees. But it's okay.

2:3:11

Once you guys read it once more, like after the lecture, you go through the notes, you'll be able

2:3:17

to understand it much better. Especially with all the examples, Cyancer has covered.

2:3:24

I think I've lost one more player. Guys, thumbs up in the chat if you want me to just start.

2:3:30

We have two questions left.

2:3:33

Okay, all right. We have the level player, I think.

2:3:44

A deep tree scores well on train, but poorly on euros. What is the likely issue?

2:3:49

It's something that is very easy. I'm sure you guys have all understood why this happens.

2:3:56

And I mean, even if you haven't, it's very easy to get an intuition on.

2:4:02

intuition on yeah seems everyone has voted quickly yes the answer is overfitting

2:4:11

basically the deep tree has understood has practically byhearted all of the examples in

2:4:17

the training set and that is why it is getting a very high score on train but it is

2:4:22

fitting very poorly on euros so same logic as the last few lectures for linear and

2:4:28

logistic regression also if the training training training

2:4:32

training accuracy is very high and test accuracy is low then it's probably an

2:4:38

overfit yeah so great great job you guys underfitting a low recall is not going to be

2:4:45

correct underfitting is if something is underfitting firstly a deep tree will very likely not

2:4:52

underfeit it is not going it's going to be very difficult for a deep tree to underfeit

2:4:56

and secondly if it's underfitting the train accuracy and test accuracy both will be very

2:5:02

low because underfitting means it's not able to pick up the pattern only.

2:5:07

So yeah.

2:5:09

Last question of the day.

2:5:32

okay all right last question what is max depth limit in a decision

2:5:42

again relatively easy question to answer what does maximum depth limit in a decision tree

2:5:57

oh okay some people still got what what does maximum depth mean in a decision tree I'm I'm assuming everyone will be getting this answer correct

2:5:57

oh okay some people still got it wrong but great job

2:6:02

most of you did get correct yes that means number of question layers so if you remember

2:6:07

a decision tree is like a flow chart and each each layer in the flow chart is like a question

2:6:14

so that is the number of that is the number of question layers and as the layers keep on increasing

2:6:20

that is the depth of the tree that keeps on increasing so that's the correct answer number of

2:6:25

features number of training rows these are not a number of output classes these are not valid answers

2:6:32

okay so yeah it's it's it's great that majority of you guys got all the answers

2:6:38

correct still we have like a pretty decent split between all the options oh arnica great uh

2:6:48

congratulations again all right um with that we are at the end of the session so i am going to

2:6:57

end the poll i'm sorry end the mintimeter quiz and i will see you guys on