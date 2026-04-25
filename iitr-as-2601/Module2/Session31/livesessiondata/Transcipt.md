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

Thank you.

11:46

Thank you.

12:16

Thank you.

12:46

Thank you.

13:16

Hi, everybody. A very good evening. We'll just start in a minute and a few minutes.

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

Thank you.

16:46

Thanks, good evening once again.

16:51

Let's start on here.

16:52

Hope everyone joined in and we will be kicking off today's session on decision on decision trees and random forests.

17:00

It's a continuation from where we closed in the last session.

17:04

It is very much related to what we discussed and what we covered in the last session.

17:09

The today session is very much a continuation of that.

17:16

Hi. Good evening. Good evening.

17:46

Thank you.

18:16

Thank you.

18:23

Thank you.

18:46

I've uploaded all the session contents in the 23rd FF folder. Everything is here. So today, as I said, it's very much a continuation from where we left off. And also we'll be looking at, you know, we'll be looking at a few other interesting concepts, which are very much related. There won't be too many new things we'll be discussing, but we want to do a lot of demos, a lot of practicals to further consolidate our understanding of classification following on from the last session.

19:16

So last session, we discussed about something called logistic regression, if you all recall, and we covered the whole pipeline once again, take the whole data, split the data into training and testing, build your models on trained data, and evaluate your models on test data.

19:31

And there was one other very interesting thing that we learned called the Confucian matrix.

19:35

So today we will further discuss about that Confucian matrix in more detail.

19:39

So last session, we just covered something called true positive, true negative, false positive, false negative.

19:45

falls negative. Today we will be getting a little deeper into that. I'll once again recap that and we'll see things like

19:50

precision, recall, f1 score, what are the other ways to evaluate models? And that's why the, you know, the name of the

19:57

session is classification metrics. We'll give a lot of importance to different types of metrics out there. And very

20:03

broadly speaking, the general agenda of the session is on, is on something called decision freeze and random

20:10

for us from an algorithm perspective. Just like last session, we, uh,

20:15

you know, we discuss something called logistic regression.

20:19

Today is majorly on, on decision, prison, random forests.

20:24

All right.

20:25

We're going to be starting on with the same use case that we did last time.

20:29

I will, so I will take the same demo as what we, uh, what we took up last time.

20:35

It's the same use case.

20:35

We have the student data.

20:36

Just for the understanding of the concept, we will start with this demo.

20:39

And then as we, as we get going towards the, uh, you know, towards us later,

20:43

later parts of the session, I will take up a case study and we will do the same way

20:48

how we did last time. We'll keep some time for the case studies or that people get some time

20:52

to practice the ideas that we studied today. That's the thing. Okay. Now first things first,

20:57

what is a, what are we trying to do in machine learning? I hope everybody remembers that idea.

21:03

All of you recall it from my very first session. So what is the poor idea of what we are

21:09

trying to do in MN? So we have lots and lots of X, X, X, Y combinations. We have lots of

21:13

lots and lots of inputs, lots and lots of inputs. So we have, we have lots and lots of input,

21:17

output or X, Y combinations, uh, with us. And what we are trying to do is, we are trying to, uh,

21:24

use the data, whatever data we have, we are trying to take the data, use some algorithm and build

21:29

model. So that's the crux of what we are trying to do in LEMM. So we have lots and lots of input

21:34

output combinations or X, and the crux of machine learning is we are trying to take the data, uh, use an

21:42

algorithm and build a model.

21:43

that is what we are trying to do okay the the rules are what we are trying to learn if you

21:49

remember so this happened last week it happened this week so we are we are trying to build

21:55

the model dot week we are trying to learn the rules learn that equation and dot predict we are

21:59

trying to predict to the prediction another important learning last session was predict

22:03

we'll use all of this today why am i talking about this now because decision-free the concept of rules

22:10

becomes very interesting there this is the first of the thing

22:13

we will be seeing again we are not entering into the math at all but i'll try to

22:17

intuitively explain what a decision tree is for you right so in a decision tree here also we are learning

22:24

the rules and turns out these rules are very much like uh you know visually if or else statement

22:30

it's kind of like a flow chart that we will see we'll come to that we'll come to that in a moment

22:36

so as we as we get going let's let's let's take up a small case study imagine we are trying to do

22:43

imagine we are trying to build a model to predict loan so let's say this is the use case we have

22:51

right now all if you give it a read once please just give it a read and we will then we'll discuss

22:56

just take a take a couple of minutes give it a read

22:58

Thank you.

23:28

Thank you.

23:58

we are trying to build a model to predict whether a customer should be

24:13

a loan or not right we have talked about this use case before last time also when you were discussing

24:17

classification and all these loan applications that are there right all these loan applications that are there

24:22

right all these loan applications that are there when you try to apply for a loan these are

24:26

loan these are the questions that they will ask you they will ask you these questions

24:29

that so how does the bank decide whether to grant you a loan or not if you think about it how

24:34

what are the factors on the basis of which the bank will decide whether you should be granted a loan

24:39

so you so it can be achieved by knowing answers to all these questions right they will first of all

24:47

they will ask you about your employment i hope everybody everybody is aligned on that so employment is a very

24:52

important thing they will ask you whether you're employed or not right right

24:56

are you employed are you not employed that's the first thing they will ask you are you

25:00

need a nearing retirement because if you're nearing retirement then probably your you know your your your

25:05

likelihood of repaying the loan reduces what is your annual income income is obviously a very

25:11

important criteria if you're earning more than you're a good customer if you're not earning more

25:15

then you're not a good customer you're a risky customer so these are the kind of questions that

25:21

need to be answered to help

25:26

the bank decide that hey should i give load to the customer or not does he have any

25:32

dependents you have dependents what is your age if you're young it's something if you're old is

25:38

something if you're old and not earning that's all other things so also permutation

25:42

combinations they will look at and finally what's your credit score in the Indian

25:47

context it's your civil score if you give you a pan number all those details are

25:50

automatically coming out that's the reason why you fill up a form right it's a very

25:54

important form it there's a lot of background verification that happens in loans

25:58

if one part is the sales people will call you and say sorry you want a loan you want a loan you

26:02

want a loan they will ask you hundred things and that's one part but remember miss

26:08

selling is one thing selling a loan is one thing but for a loan to be approved is a

26:12

completely independent back-end process the the salespeople are not going to you know

26:17

approve your loan just to let you know the other ones who will only do sell the product and that's it

26:22

it is their target meet.

26:23

It's just.

26:25

So,

26:25

go to go and then they are not the ones who are actually responsible for all this.

26:31

It is a separate, very robust back-end pipeline that is built on the basis of which it

26:35

decided whether you should be even granted a loan or not.

26:40

Now, what we can try to do is we can try to arrange these series of questions in a hierarchical structure

26:46

something like this and this is the flow chart that the banks are looking at when you're coming to a loan

26:52

approval and before i talk about it you just want to just just just give it a glance all of you

26:58

and this is exactly what we are what a decision to is i'll come to that term in a moment but all

27:02

if you just give it a glance just give it a glance what is happening some of the features i name

27:07

how how that workflow is playing out let's give it a glance everything

27:22

see we start right at the top is employed it's called a root node and every node

27:30

is where we take a decision but there

27:34

a question is asked are you employed if yes go this side if no go this side

27:39

yeah here another question gets asked what is your credit score is it low go this side

27:46

is it low go this side if it's high go the side another question gets asked what is the consumer's age

27:52

if it is more than 55 go this side if it is less than 55 go this side so these are the things

27:58

that are actually happening right now this is how we are actually able to frame the rules so you have the

28:05

data from the data the bank will need to come up with this kind of a flow chart structure

28:12

the bank will need to come up with this kind of a flow chart structure and on the basis of this kind

28:17

of a flow chart structured you can effectively take any customer and try to predict whether

28:25

that customer should be given that loan or not now the thing is that your question will be okay

28:32

how do we come to this flow chart structure this is generated this is actually what the

28:38

machine learning rules create so if you have to if i put a story around it imagine this is your data

28:47

we have studied before we will use some algorithm and this is also exactly what we'll

28:53

do discuss and do in today session so the algorithm that we'll be using will be a decision tree

28:59

and this is exactly the part where we will use something like dt dt dot fit we will use a decision

29:13

tree model we'll build a model and remember if you all

29:17

recall it from my discussions a model is nothing but the rules or a mathematical function

29:23

right and and and turns out in the case of a decision tree this can also be called something like a

29:31

tree this is what is learned so this is not something we are creating mind you this is not something

29:38

we are manually handcrafting i already told you in my first session initially that writing

29:44

these rules for a loan approval workflow will be very complex

29:47

there are so many permutation combinations right somebody's credit score is something

29:51

somebody is old somebody is young somebody is dependent there are so many infinite

29:56

number of combinations now how is it even possible for me to know that okay if this is

30:00

true else if this is true then this else is too many if else conditions right remember

30:05

if else statements we talked about rule based so this is what is we learned by the decision

30:12

this is the excellent example where those if else

30:17

rules i will write down for you those if else rules are learned in other words

30:26

this flow chart is learned this is your model and this is actually that is getting

30:34

created behind the scenes it's just one line of code be right i'll come to the code in a moment

30:38

but big picture idea you have lots and lots of x y combinations

30:43

you you fit the decision tree you do the duty dot fit you build the model and that model is

30:50

basically this tree so this is what the machine is learning on the basis of your data how that's a

30:57

separate part that is something that's that you do not need right now but the intuition of the

31:02

learning should be clear the end result is end result is if else rules

31:07

from the data use an algorithm build the model and the and this is the tree that you end up

31:12

building in the process

31:13

and if you see the tree at every note this is called the root node these are different

31:19

different terminologies we can use we can call this a root note root node is the starting node these

31:24

are called the intermediate notes the internal nodes these are nodes were notes in nodes

31:28

make decisions leave you ask a question if it is true though this side if it is false

31:33

for this side like that notes they're questions push it root node internal nodes or here the end

31:39

there on leaf notes is where nothing else happens to you all right and these are

31:43

are called branches decision branches generally speak so that's the way how it is working

31:50

are we doing it no the machine is doing from the data this if else route is learned and if you think

31:57

about it this is if else you're conditional statement right you can can you not write in if else out

32:02

of it you can write so first you are asking the question if your employer necessary

32:08

if you're asking what is your credit code if this then do this else do this then do this then

32:13

else what is the customer age less than 25 if it is this then do this else if it is

32:18

this entire thing is a very complex set of if else rules that are learned you are not creating it

32:25

but from the data that is learned now let me continue the conversation this is one part of the

32:32

puzzle so we have just now discussed the puzzle which is model dot fit now after the model

32:38

is trained what is the workflow we have discussed then fellow d t dot

32:43

there are two parts of ML right first part is building the model training the model

32:48

on the train data and the second part is based on whatever rules or whatever model is learned

32:54

in this particular case based on whatever tree is learned you will go and do some prediction on some

32:59

unseen test data so there'll be some unseen test data and on that unseen test data you will have to do

33:04

some prediction that's the way how it will work out so now we can take a new customer we can

33:11

effectively take a new customer or we can take a new student or whatever we can take a new person

33:15

and put prospective customer somebody who has applied for the loan so now we can take a new customer

33:22

and we can give the different details of the customer and based on that we can predict will

33:27

will the customer be granted the loan or not granted the loan that is how the detail that predict will

33:31

happen so dot fit is where the flow chart is learned the if else rules are learned or dot predict

33:37

predict what would what predict in dot predict on what predict on dot predict on

33:39

dot predict you can't you know let's say you are you know let's say we have an

33:46

example of a person a new person who has applied for the loan okay and we can a

33:51

example we can't we can't this case we have an example

33:55

we can't so new data will now data could something

33:58

color change and let's say a new data looks somewhat like this is employed

34:03

the new data is his employed yes is a

34:10

banda employed he okay age age how is feeling of the loan application form

34:18

his age money is 46 he can up age 46

34:21

again uh one second actually this can be a question i can ask you so if you like to

34:28

properly otherwise people will not understand my handwriting so employed

34:33

employed will be is yes age

34:40

age was 46

34:43

again uh income

34:46

i'm writing short form okay

34:50

you can't understand like this is income here

34:52

income corresponds to here annual income so it's the same thing right

34:56

income had uh low

34:57

and dependence had

35:01

dependents,

35:03

you know, parents

35:05

these are called dependents right?

35:06

A non-earning member

35:07

you have to take care of somebody.

35:09

What dependence is it?

35:11

So why is dependence important from a loan perspective?

35:14

Because if you have too many dependents,

35:15

maybe your income power is less.

35:18

Because you're spending too much money on people who are not earning

35:21

you have to look after your parents, kids like that.

35:23

So you don't have enough disposable income.

35:27

You have got dependents?

35:28

You have got dependents.

35:28

or dependents

35:32

no.

35:36

So my question to all of you is

35:37

data

35:39

algorithm

35:41

flow chart

35:43

free been here. This is the decision tree in front of you right now.

35:48

And based on whatever tree is learned,

35:49

whatever if else rules are learned,

35:51

if a new customer applies for the loan,

35:53

what will the predicted result be?

35:55

Question for everybody.

35:56

Prediction what will?

35:58

Take a moment, think through it.

36:00

You are simply traversing through the tree.

36:02

Prediction in you, what you will.

36:04

Whatever tree is learned, you will simply traverse through that.

36:06

You up from up from check it.

36:07

Okay, this is, yes, hey, here.

36:09

Now, this, say, no, here.

36:11

We're here.

36:11

Now, yes, say, no, here.

36:12

here.

36:13

Here.

36:13

So, you're going to traverse

36:14

and then the other leap note will,

36:16

that will answer will.

36:17

Okay?

36:18

I will wait for two minutes.

36:19

Allow everybody some time.

36:21

And you, look,

36:22

this has happened.

36:23

Intuitive.

36:26

Everybody, let me know what the answer will be.

36:28

What will be the predicted value?

36:30

Should the person be given the loan or will the person not be given them?

36:38

Okay, Ravahy's the Ravika the answer.

36:39

Others?

36:55

Good.

36:55

Let me hear from everybody.

36:58

All of you, use your, use your, you know, concept.

37:04

Okay, okay.

37:05

Mabik is corrected, okay?

37:09

Approve been approved.

37:09

Okay, okay.

37:11

No, no,

37:12

way,

37:12

we say,

37:12

we say,

37:13

you have to go through the tree structure.

37:16

But don't use logic.

37:17

See,

37:18

that's not that we are reasoning

37:19

what should.

37:20

What are not,

37:21

what should or not?

37:21

What should or not?

37:22

What will.

37:22

We are not, okay,

37:23

just to clarify,

37:24

see, I'm not asking a general question.

37:26

I'm,

37:26

we're not asking,

37:27

that if customer's data

37:28

if it's data

37:28

so what's going to happen,

37:28

then what is just

37:30

saying, what is actually

37:31

going to happen based on my data?

37:34

Okay, just to clarify.

37:35

It's a method

37:35

you have to first

37:36

you have to start

37:37

there's a flow chart,

37:38

it's like a,

37:39

this is like an e-fell statement.

37:41

So you're like,

37:42

yeah,

37:42

you, you,

37:43

you're just,

37:44

yeah,

37:45

no,

37:46

no, I'm not,

37:47

I'm not,

37:47

I'm not answering you, Bhaweck,

37:48

I'm answering Ishit, actually.

37:50

Ishit has answered

37:50

as his income is low.

37:52

I think you guys are all

37:52

pinging to hosts and panelists,

37:54

not everyone.

37:55

What is the reason?

37:56

What is the reason?

37:56

Your everyone's enable

37:57

not?

37:58

Can you can chat with

37:59

attendance and chat with host.

38:01

Okay, I'm so sorry.

38:02

Your host has enabled

38:02

so I'm so I'm

38:03

enabled

38:04

so I'm,

38:04

for some reason

38:05

does not enable

38:06

it.

38:08

Okay, okay.

38:08

Can you guys

38:09

ping everyone?

38:10

Because that makes a session

38:11

more lively.

38:12

You will feel like

38:13

you're just chatting with me.

38:15

You can actually

38:16

talk to others also.

38:17

It's fun.

38:18

It's fun too.

38:19

I don't know why.

38:20

I think in every class it gets

38:21

disabled for some reason.

38:23

I will have to check

38:24

with the team works

38:24

how to enable it.

38:26

Okay,

38:27

right.

38:27

Now it's all right.

38:27

Everyone.

38:29

Okay.

38:29

Ishit,

38:30

you've got

38:30

I think you answered

38:32

that as the

38:33

income is low,

38:34

it should be,

38:35

but like,

38:36

okay,

38:38

but you have to traverse

38:39

to that free and answer, okay?

38:42

Yeah.

38:43

Others, let me hear from everybody.

38:47

All of you.

38:49

So,

38:49

the first part clear is,

38:50

data,

38:51

algorithm.

38:51

You have a tree

38:52

if else statements.

38:53

This is the

38:54

connected set of if and statements,

38:55

right?

38:56

And now...

38:57

Actually, this is a way a technique.

39:03

This is a little time

39:04

will be,

39:05

but I think we are all smart people, right?

39:09

So, well,

39:10

okay,

39:11

we'll go back,

39:12

then we'll

39:13

show you

39:14

something interesting.

39:15

So first,

39:16

all of you do this one,

39:17

then I'll show you something interesting.

39:18

We will get a loan, okay.

39:19

We will get a loan, okay.

39:23

Sangita also says get.

39:25

Sanghita, you answered,

39:26

definitely while back.

39:27

While back.

39:28

You've corrected it.

39:29

Is it?

39:30

Okay.

39:31

Okay.

39:32

Okay.

39:33

Everyone clear.

39:34

Get the loan,

39:36

very nice.

39:38

So,

39:39

so now,

39:40

when new data

39:41

we're from

39:42

start from

39:43

root note.

39:44

What is happening in the root node?

39:45

What is happening in the root node?

39:46

You're asking, is employed, right?

39:49

So the person,

39:51

now,

39:52

application form,

39:53

okay,

39:54

the concept,

39:55

person will fill up the application form.

39:56

For application form, as

39:57

data entered,

39:58

it's based,

39:59

you will go and do that entire workflow.

40:01

So is the person employed?

40:03

Yes, the person is.

40:04

What is the customer's age 46?

40:06

So 46, let's say you're 46 more than 55.

40:10

Less than 55?

40:11

So it's sort of going.

40:12

Okay?

40:13

So, so it's sort of going.

40:15

Let me simplify this.

40:17

One second.

40:18

One second, guys.

40:20

So 46 will go this side.

40:23

It is less than 55.

40:25

is less than 55.

40:26

Now,

40:27

go and here in this internal note,

40:28

what is the annual income?

40:29

Income low or high a

40:31

man?

40:32

If you are,

40:33

if you're going,

40:34

if you're going to

40:35

see how I'm traversing the tree.

40:37

And then

40:38

the dependence is or not?

40:39

No,

40:40

if there's this side,

40:41

no,

40:42

we will approve the loan,

40:44

the person will get the note.

40:45

This is the result of dot predict.

40:47

When you're dot predict

40:48

in Python,

40:49

you will realize how simple the process becomes.

40:51

This is.

40:52

This is.

40:53

There is.

40:54

Nothing.

40:55

is split, dot fit, dot score.

40:57

Same to same, it,

40:58

it's not.

40:59

Same thing, you will take the last two days back

41:01

of code and you can copy paste.

41:02

Only thing you can use decision fee.

41:04

Some new learnings will be there.

41:06

And dot predict, this is the concept that is happening.

41:08

This is actually what is going on behind the scenes.

41:10

Okay, that's the basic idea.

41:13

Everyone is clear what is going on inside a decision fee.

41:17

Now, small thing,

41:19

you know,

41:20

here we have,

41:21

here,

41:22

if else rules are being.

41:24

This is actually a series of if else rule.

41:25

ephels do.

41:26

So, this is visually we can understand.

41:28

This is actually easy to understand.

41:30

But internally behind the scenes, the machine is kind of thinking in terms of a big series of ephel statement.

41:36

So just so that it is easy for you to remember, easy for you to understand.

41:40

We can, we can a ephels generate.

41:42

It will be too much to write it.

41:45

So what I can do is I can take a snipping tool.

41:47

Now, let's a snippet bina.

41:49

Let's take a snippet.

41:50

Go to Gemini.

41:52

Let's go to Gemini.

41:54

Let's go to Gemini.

41:55

And I will just create a small snipping tool on the basis of this.

42:02

Okay.

42:03

Just as simple.

42:06

So I'm in my Gemini right now.

42:21

So I'm in my Gemini right now.

42:23

And what I will do is I'll say that consider

42:25

this, consider this decision free.

42:30

Consider this decision fee.

42:32

Just to show you how the EFELs will look like enclosed in the image.

42:37

Please generate the corresponding

42:44

if else rules corresponding to the

42:50

corresponding to the decision fee.

42:54

I'm Python in

42:57

because internally

42:58

the rules

42:59

are different sort of

43:00

that

43:01

necessarily stored not

43:02

so that you can relate to it very nicely

43:04

that you can relate to it very nicely

43:05

that the decision free

43:06

we have explained to

43:07

data fit

43:08

the rules were created by the model

43:12

so that if else rules are

43:14

this was a visual representation

43:16

but you can actually try to

43:17

you know you can actually try to see from the code

43:19

that actual representation

43:21

so it's quite complex

43:22

but I'm not very complex

43:23

but I think you guys

43:24

now you have

43:25

you've got it,

43:26

you know, that you can't

43:27

see what

43:28

we're,

43:29

first we're starting

43:30

we're at

43:32

I think it's hard to show you

43:33

both the things,

43:34

but you can understand,

43:36

you can understand, right?

43:37

So,

43:38

look at our employment status

43:39

if not employed,

43:41

first are you employed

43:42

and then

43:43

nested if else,

43:44

credit score, and this is how it is happening.

43:46

Okay, clear, all of you,

43:47

three levels of nesting are there.

43:49

So this is what is actually

43:50

this is actually

43:51

what is going on behind the scenes.

43:53

You guys can check.

43:54

check this out, okay?

43:55

You can.

43:56

You can't.

43:57

You can't.

43:58

You can't.

43:59

You can't.

44:00

We can you snippet here

44:01

be pinged, okay?

44:02

Okay?

44:03

Okay, here there's not.

44:04

No problem.

44:06

I can, uh, yeah, yeah, exactly.

44:10

You can actually, you can actually do that.

44:13

Let, let me, let me share this image

44:14

together.

44:15

Let me share this image with you.

44:17

That's.

44:18

You also,

44:19

you can,

44:20

you can,

44:21

you can see that.

44:23

It's a nice,

44:24

this one actually.

44:25

Okay, let's go.

44:26

Let's move on.

44:27

Now what we will do?

44:28

Now we have seen the basic idea of a decision

44:32

P.

44:33

Now code layer.

44:34

Let us go back to the coding there and understand

44:36

this code in how do it.

44:38

So, Python to connect you.

44:40

First, I have done all my library imports.

44:43

Let's just allow me one minute once.

44:45

If you start first, let me restart from the input.

44:50

Ah, yeah, that is there, of course, yes.

44:52

I'll quickly restart my kernel.

44:59

Here you observe, you,

45:00

you have code not going to,

45:01

where you code can have to

45:02

I will myself tell you, go back to the notebook.

45:04

Right now, you can just follow along.

45:06

Initially, this is a theoretical,

45:07

we'll understand.

45:08

Okay, so.

45:09

So, first,

45:10

this we have,

45:11

thinking in terms of rules,

45:12

we discussed that concept,

45:13

and we understood that

45:15

it is not an equation, it is instead

45:17

like asking questions of your data.

45:19

If you're conceptually

45:21

conceptually,

45:22

I explained here.

45:23

So in a decision tree, what are we actually doing?

45:27

What are we actually doing inside a decision tree?

45:30

We are asking lots and lots of different questions of our data.

45:35

We are asking lots and lots of different questions of our data.

45:39

We are asking questions of our data and we are getting to the answers.

45:44

So we have to understand that

45:46

is the final answer that I want to get.

45:49

In order to answer that question, I'm asking lots and

45:52

lots of questions of my data and I'm trying to navigate to the answer.

45:55

That's the way how I'm achieving this.

45:57

Okay?

45:58

So what we're achieving here here.

45:59

Now, you can't.

46:00

Okay?

46:01

What's that?

46:09

Okay.

46:11

So these are the three, these are the important

46:15

terminology we have right now with respect to decision piece that we have here.

46:19

So root node, we have something called a root node.

46:21

something called a root node.

46:22

Root node is basically nothing but the topmost.

46:24

We already discussed this guys, root, internal node, leaf node, just summarizing this thing for

46:28

everybody.

46:29

And now we will come back to our, to our famous data set.

46:34

We've already seen this last session, right?

46:36

This is a simple data set we are taking right now.

46:38

So we are looking at the study hours, we are looking at the sleep hours and the distractions,

46:43

and based on that we are trying to predict whether the person will pass or pay.

46:47

That's the problem that we are trying to solve.

46:50

So study hours, sleep hours, distractions.

46:52

These are the three features we have,

46:54

and we are trying to predict pass or fail.

46:57

Okay, I hope everybody remembers, this is the classification problem.

47:00

Don't go by this, this is not a number.

47:02

Sometimes people get confused.

47:04

People are confused, sir, this number is.

47:06

One is, no, but I explained to you last session.

47:10

Remember, you can solve it like regression.

47:12

There is no problem.

47:13

You can do linear regression also, but what is the problem?

47:16

Problem here will be given a new data point,

47:20

So predictions will sometimes the predictions can be more than one or less than zero.

47:24

That's possible not.

47:26

So you will not solve it like a regression problem.

47:28

This is the classification problem.

47:30

The one and zero is not a number.

47:32

The one and zero correspond to two categories.

47:34

One matter of pass and zero matter pay.

47:37

That's the way to look at it.

47:38

Okay, so oftentimes when you're solving classification problems also,

47:41

the labels can be numerically encoded like this.

47:44

Okay, let's go.

47:45

Okay, we're back back.

47:45

We're data, x, y combinations, everything is set, and now we will train the decision free.

47:50

whatever decision tree we spent time understanding here, we took some time to understand

47:54

a decision free, this is what we saw.

47:56

Now we will see how we can build this decision free.

47:58

I'm quote, we'll see how to build this decision free.

48:02

Now, so very simple.

48:07

We are simply importing.

48:08

So this is a data already and this is the part where we instantiate the decision tree classifier

48:13

and we define something called maximum debt.

48:18

Okay, we define something called maximum depth.

48:20

And also just one small thing I wanted to clarify, there is something called random state that you will add to reduce the, to remove the randomness in the, you know, the overall thing.

48:32

So wherever there is randomness involved, if you remember, I had explained random state during brain test state also.

48:37

The same way, you will always use a random state for decision fee also.

48:41

Just generally always use it. Whenever, you know, you get an option, always use random state.

48:45

So that every time you don't get different answers.

48:48

But what is more important than that,

48:50

is something called this depth.

48:52

So depth, if you remember the thing I taught you here, what did I show you here, guys?

48:58

I showed you the concept of decision free.

49:01

And here also, we have a decision tree of depth three.

49:04

Depth one, depth two.

49:05

Actually, this is a depth four.

49:06

I'm sorry.

49:07

This is actually depth four, what you're seeing on the screen.

49:10

So we are looking at a decision tree right now.

49:13

Depth one, depth two, depth three, depth four.

49:18

So we have a decision tree maximum.

49:20

minimum four levels deep.

49:22

And that's the concept we are trying to, you know, get at.

49:24

This is what I was telling you, you know, you know, you have the data and you're trying to learn the rules from your data.

49:31

And the tree is basically that structure that you're trying to learn from your data effectively.

49:37

You're asking questions of your data.

49:39

And you can set the depth of your decision fee.

49:43

And you can limit the number of questions that way.

49:47

Now, look, this is the depth one maybe limit can.

49:50

But the question come, put you can also increase the depth of your tree.

49:55

I think it will be better if I show you here in my code itself.

49:58

So here I'm saying maxed script equal to three.

50:00

I will build a model.

50:01

Nothing to explain here.

50:02

This is same thing.

50:03

You have all part.

50:04

Train, test, accuracy, everything we know now.

50:07

So this seems to be a reasonably good quality model.

50:10

95% training, 93% testing.

50:13

But can we make it better?

50:16

100% yes.

50:16

I always told you that model comparison is always comparative.

50:20

There is nothing called best fit model.

50:22

You can always make it better until and unless you get 100% test accuracy, you will always keep trying.

50:28

So this is a baseline model.

50:29

And just to help you visualize it, this is how the visualization of the decision tree looks like.

50:36

This is how it is basically adding up.

50:37

So whatever I was showing you, you know, as a demo, this is basically how it boils down to it.

50:42

And you can see beautifully.

50:44

This is my data, right?

50:45

Study hours, say, sleep hours, say, distraction, see the decision tree, all of you, look at the decision tree and see how.

50:50

how it has curated the decision.

50:52

It is asking different, different questions of my data.

50:56

It is asking different, different questions of my data that, hey, what are the, is the study hours less than 0.46?

51:03

Is the study hours less than this?

51:05

Is the distractions less than this?

51:08

Is the study hours more than this?

51:10

Is the sleep hours less than this?

51:12

And if these, these conditions are satisfied, then end may jaque, fail, pass, fail, pass for that.

51:19

Now just one small small.

51:20

thing, guys, which I will request you to ignore. I wanted to remove it from the diagram,

51:24

but I did not at the end, but just remove, just ignore the samples part.

51:28

This is a little mathematical, it you don't need.

51:30

The other what we'll see. We'll just across all these things, please ignore the samples part.

51:37

So just ignore the samples part.

51:40

Samples, what? Samples mean how many data points are getting split, basically?

51:42

So you have to know right now. Just remove the samples.

51:46

So from the data, you're asking different, different questions. If they're, you're asking different questions,

51:49

if this, then do this, else if this, then do this.

51:52

And remember, by default in Python,

51:55

this convention is always going to be true and right side is always going to be false.

52:01

That is the basic convention that happens in Python.

52:04

So the left side is always generally equal to true and the right side is generally always equal to false.

52:10

That's the way how it works out.

52:13

So left side is true and right side is false.

52:15

Again, left side true, right side falls.

52:17

Left side true, right side false.

52:18

That's the way how it is.

52:19

going to happen fusion, right? All right. Excellent. Now, if you want to see how the

52:26

maximum depth of one looks like, how you'll show them. If you remember, guys, we have discussed

52:31

this in our very first class in machine learning. This one and this maximum depth is actually called

52:37

a hyper parameter. Yeah, you know, we have got into the demo demo. We have not got into the depth

52:44

of it before, but we have discussed in the initial session that this is the tuning knob that we are trying to

52:49

Every machine learning algorithm has that knob, right?

52:52

And this is one of those knobs that we are trying to put you.

52:55

Either we'll it will come or it, or it's just to do it, and by modifying that knob,

52:59

we can basically, you know, change the quality of the model.

53:03

Okay, we can try different, different values of depth.

53:06

We can take one, let's take, depth two, like, seth, depth three, let's say.

53:09

You can try different, different values of depth, and we can build a better quality model.

53:14

So we have here here here here, and as we have depth two, yeah, and as we have, we've changed

53:18

it. This is two level of tree. Can you see? We've only two level

53:23

of questions here. So first time asking, how study hour is? Then, we're asking, how study hours

53:25

is less than, that? Then we're asking, study hours less than, it's, true

53:30

is this side, or past, it, or false it, this side. Please remember,

53:33

convention, true this side, and false this side. And end result is, what is? End result

53:37

what is. The end result is, the end result is, you are your, fail, fail, pass, is. This is your end

53:44

product. This is the way to interpret the decision.

53:48

steps you ignore this, you need. In intermediate steps, you're just this

53:51

condition, exactly how I explain my other demo, okay? And final step

53:57

you have you seen, you here. You know, either pass or failer, that's the way to

54:02

look at it. Okay. And now, so you can relate to the whole thing. Like, dot fit

54:08

say, we are able to build the tree, we're able to build that e-fell's roots, and then

54:12

give her a new record, we can do dot-pidding. This is the, this is the big picture idea,

54:15

whatever we talked about in the class.

54:18

Okay, okay?

54:19

Maximum depth, we can three can, four, can, ten, can't.

54:22

No problem.

54:25

But what will? If I increase my maximum depth too much, what will? If I, if I ask too many

54:30

questions, if I make my tree too complex, what will happen? We will end up getting something called

54:34

overfitting. Right? So please remember, please remember, decision trees are highly prone to overfitting.

54:40

If we don't stop them, they will ask too many questions.

54:44

What I mean? What? The whole level on. If this, okay, what happened?

54:48

what you're employed?

54:49

How are? How are dependents? How? How is studying? It is continuing to ask questions of your data

54:56

and it is trying to split your data and get to the answer. That is what it is internally doing.

55:02

So if you allow the tree to keep growing, if you don't keep a limit on maximum depth,

55:06

that will go and be going, barter and this will lead to something called overfitting, which is actually happening right in.

55:13

Now, look, training has increased a lot. We've, we've, we've, we've depth 10, kind.

55:16

10 is a lot of. We'll see. We're in America. Very interesting. But testing has actually

55:22

reduced. And if you see the decision tree right now, you, you can see this 10 depth of decision

55:27

feature. Very interesting. That 10% not has, it's a different cause. But you can see how the tree

55:33

has actually grown. So 1, 2, 3, 4, 5, 6, 7, 7. Or 7 is the reason. It's a

55:39

one mathematical reason is because that's a different issue. That we're not going to

55:45

that's a different issue. That we're not going to. But, but, but, but what I wanted to, so we're

55:50

to, so we can't take 10 pay not because the reason is because, that's, because of that

55:54

other, we've already got the perfect splits. That's the idea. But you can see. This is

55:58

where I've done a max depth equal to 7. But the first level, second level, third level, fourth level,

56:05

fifth, six, seven. So seven levels deep. But definitely, highly overhead. Highly overhead. High

56:09

So, two extremes are. This highly underfit. This is. This is

56:13

this, you're not. This is only one level. It's. I mean,

56:16

only one question. If you're asking, answer, that's not

56:20

not. People have to ask questions. If you want to get to the answer, you have to

56:24

ask better quality questions. You can't just ask, how much study hour

56:27

is. Studying less than four to fail or, or not, it'll pass. This is a

56:31

wrong thing. Howly, study hour's from what? No, no, it's

56:34

not? The person, how is it? The person can be very intelligent and they can

56:39

study less hour, that will be passed. So this is not a very good quality model.

56:43

This is you, you know, you'll see you know what you can't. Right? So, depth one be

56:47

bad. F1, you mean, you're all right? And on the contrary, he be

56:52

a bad. Depth 10 be bad. So you're trying to find out what is the optimal depth in between.

56:59

So this, so this particular process, what is this thing called? This process is what is this

57:03

thing called? This process is what is referred to as high-per-parameter tuning. So,

57:09

this is we try different, different values of maximum depth and we actually try to find out

57:14

what is the ideal value of maximum. I'm tune. We're we, we're depth one, two,

57:19

we take, two, three, we take, four, we're. We're, we're allaract trees

57:22

and we try to find out which particular decision, which particular model is giving us the highest

57:27

test accuracy. This is we're saying, last week, logistic, baner it. Random forest,

57:31

make, two, three models, and we were trying to find out which is the best one.

57:36

That's the same thing. Same thing.

57:39

No, no, no, no, seven is the maximum depth only for this case I'm trying to show you.

57:43

Theoretically, Yubra is maximum depth of no limit. You can't, 10,000, 10 million

57:46

be more than, but that practically not

57:48

not be that big, but there is no theoretical limit on maximum depth.

57:52

Okay, if you have a huge data set tens of millions of rows, it's, both depth, right?

57:58

So maximum depth is an integer you can enter any value theoretically.

58:02

And whatever we are discussing right now, this the max depth I'm discuss

58:05

this is just tree for it. This is for logistic for not.

58:09

We have logistic regression Tuesday, discussed there, where did?

58:13

The maximum depth is the concept only for decision-p.

58:16

Because in decision tree, I'm here, this, this one of the thing is, this one of the structure I'm,

58:20

I'm showing, the rules, if else, me, it's just free in.

58:23

This, it's not. This is logistic in the equation.

58:26

Right?

58:27

So, that's the difference.

58:28

Data, algorithm, model.

58:30

Now, model equation be or model three, be able to be.

58:33

So, these are two different types of models.

58:36

Logistic is a different model.

58:37

Last week, linear regression is a different model.

58:39

type of model. Decision tree is a different model.

58:42

Decision tree, rules are able to create rules from your data. That's the thing.

58:49

So here, here if you're like, you're like, so I think once we come to the bigger case studies,

58:56

you'll give you to difference clear. I get it. You're, you know, here here data is this

59:00

small. I mean, this is sample data we've made just for the demonstration. That's why you're

59:05

probably checking, that, okay, depth, four, or five, or five, your, you're probably checking, you're,

59:09

but you will see a phenomenal change.

59:11

If you're the same thing, if that breast cancer data

59:13

or diabetes data, you'll, you'll

59:15

clear results will. We'll do it. We will later it and we will check.

59:20

But please remember, guys, this is called a hyperparameter.

59:23

This is the depth is, we're called hyperparameter.

59:25

We can tune the value of that hyperparameter.

59:30

Now, now, we have a tree

59:31

made. This is the tree that we are getting.

59:35

Now, we have a tree on prediction

59:36

we already discussed this example, but this is something you

59:39

will have to do. You have to do. You have to do. Now, you

59:41

let you'll give you.

59:43

Study hour six, study hour six, study hour six,

59:47

sleep time seven and

59:49

distractions one. You will have to tell me

59:52

what is the predicted value, guys.

59:58

You will have to tell me what is

59:59

the predicted value?

1:0:01

A predicted value about him to.

1:0:06

Yeah.

1:0:09

This is what you will have to do.

1:0:14

I'm sorry, let me should have notes after you.

1:0:17

So I ping you the new student's data.

1:0:21

New students data I've pined.

1:0:23

What kind of, what is it's what you're going to be?

1:0:25

This is what going to be based on the new students data.

1:0:35

Yeah, to pass or fail, that's my question.

1:0:38

And guys, please remember.

1:0:39

So I'm back from saying,

1:0:40

Python in,

1:0:41

in the left side in true,

1:0:43

right side in false.

1:0:44

I'll click it down.

1:0:45

So that is easy for you guys,

1:0:46

okay?

1:0:47

This true,

1:0:47

it's false.

1:0:48

Always, okay?

1:0:51

This true,

1:0:51

it false.

1:0:53

It's always like this.

1:0:56

True false.

1:0:59

True false.

1:1:01

And true false.

1:1:02

That's the way how it is.

1:1:09

So, I'm all right.

1:1:28

Flow, we're all right,

1:1:29

we've got to dot fit,

1:1:31

tree,

1:1:31

we've been made, tree dick, right.

1:1:32

The rule chart we are able to see,

1:1:35

and given a new customer record we are.

1:1:37

So this is a brilliant, brilliant, brilliant.

1:1:39

model and decision freeze, this is one of the reasons why they are very popular.

1:1:42

Decision tree is it's really popular.

1:1:44

Because we are able to visualize and we are able to explain the model.

1:1:49

I mean, we just

1:1:51

we're just about you're being

1:1:52

but we are not able to exactly see

1:1:55

that this is what thing is here.

1:1:56

It's a very complex equation,

1:1:58

but decision pre's this is one of the reasons why they're extremely popular.

1:2:02

If what the machine is learning,

1:2:04

you are able to clearly see.

1:2:05

You're visually looking.

1:2:07

And that is why there is another term

1:2:09

that we use right now, I'm us to explainable

1:2:11

we say that these models are highly explainable.

1:2:15

What I mean, you know, you're

1:2:15

you know,

1:2:17

if some issues happen, you can exactly say,

1:2:22

that because this, this, this, that's why I predicted past.

1:2:25

Because this, this is, that's why I predicted fail.

1:2:28

So if you're, you know, if you're

1:2:29

failed to make any false, positive, or false, negative,

1:2:32

or false, negative, a wrong prediction

1:2:33

who said, let's say, you know,

1:2:36

you, you've, you know, you've got to,

1:2:38

and failed predict did.

1:2:39

that person can't actually ask you,

1:2:43

yes, sir, on what basis you said,

1:2:45

I'm predicted to be a failure.

1:2:47

That person can challenge you.

1:2:48

You have, like, which basis in him to fail,

1:2:51

right?

1:2:51

Now, here you're saying,

1:2:52

you know, that there's a man past.

1:2:53

Now, there's another other man can be

1:2:54

who's got, we, we've failed predict,

1:2:57

that person can come back and ask us, right?

1:2:59

He's, sir, why am I failing?

1:3:00

Then you have a free, like, structure to explain.

1:3:03

This is actually very popular,

1:3:05

it's an extremely, one of the most popular models

1:3:08

that are used in industry today.

1:3:09

for the same reason, because they are highly explainable.

1:3:13

When back in,

1:3:15

then companies will have an option to come back to you and say that,

1:3:18

hey, you know why?

1:3:19

This is, we're this, so we've no, we've got paid.

1:3:21

Because, as, ha, ha, so we've made you fail

1:3:23

because like this, this, I'm predicting you to be diabetes.

1:3:27

So, next time we are solving any model,

1:3:29

so decision piece, this is one of the biggest advantages of using decision piece,

1:3:32

because they are, they are,

1:3:34

it's pictorially visualized.

1:3:35

Okay?

1:3:36

So, example, we'll go ahead.

1:3:39

So, no, so classification is generic concept.

1:3:45

Like, you know, classification,

1:3:47

other algorithms say we can't.

1:3:49

This is a one way to classification to do

1:3:50

how.

1:3:54

Yeah, yeah, yeah.

1:3:57

Yeah, yeah.

1:3:59

So, but let's, let's go over it.

1:4:00

Let me explain to all of you once again.

1:4:02

So, first, where is that?

1:4:09

I use the red color to explain this to all of you.

1:4:11

First, study hour six is.

1:4:16

Very good question, Yubraaj, by the alga Excel.

1:4:18

That's that we're machine learning.

1:4:20

Or not we're machine learning,

1:4:21

why we're going, or rule-based AI,

1:4:23

go back to the first class that we discussed.

1:4:25

The first class is.

1:4:26

What we discussed?

1:4:27

Yeah, the rules we're making, or machine,

1:4:29

right?

1:4:30

So if I write the rules myself,

1:4:32

we can make them, we can write,

1:4:34

you know, you have function

1:4:36

and you've made a function,

1:4:36

you've made, if-l statement,

1:4:37

it takes, then, then, else, this, else, this, else, this, else,

1:4:40

if, you, you can't, but that is the rule-based AI system,

1:4:45

right?

1:4:45

right? Why do we call it machine learning?

1:4:48

Because the machine is learning the rules from the data.

1:4:51

And decision trees are a beautiful example of that.

1:4:54

Because data say, you're not doing flow chart

1:4:57

you're not, you're not, model algorithm

1:4:59

is, right? So, and flow chart can't, the rules are not something

1:5:03

that we humans are creating.

1:5:05

And you, you know, and you can, and you can't,

1:5:05

and you can understand how complex.

1:5:07

basis there are much mathematics, which we're not going to.

1:5:10

This can't even, there are many math layers.

1:5:12

But you can't understand, why rules are complex?

1:5:16

This rule, who will somebody write this rule?

1:5:19

Study hour less than 4.26?

1:5:21

Who can't look? No human can do this, right?

1:5:24

Now, human being, back, what will think?

1:5:26

4.26 or 2.7%?

1:5:27

in what are different? You will generally write a rule,

1:5:30

that if this is then, but look at it.

1:5:33

A study hour greater than equal to 4.892.

1:5:36

These machines make.

1:5:37

It's impossible for humans to create these rules.

1:5:40

How can how can't find out of this basis

1:5:42

separation will?

1:5:44

Okay, so this is machine-generated rules.

1:5:47

Okay. So now,

1:5:50

prediction, we're studying our 6. So, is 6

1:5:53

less than equal to 4.26?

1:5:55

No, 6 is more, false, so this

1:5:57

sort of go this.

1:5:59

6, I mean, we'll go to this side.

1:6:03

Next, sleep hour equal to 7 is.

1:6:06

Is it less than equal to 2?

1:6:07

this? No, it is not. This turn up. And finally,

1:6:12

distraction is equal to one. Is it less than equal to this? Yes, it is.

1:6:15

This time go ahead. And you can see the reserve will be passed. As all of you rightly predicted.

1:6:21

And this is obvious thing. I mean, this is the man is, he or she is studying more.

1:6:27

Sleep hours is also. See, sleep hour is actually very interesting.

1:6:31

I think data in sleep hour's not relevance here. But here. But, yeah, the person is,

1:6:37

studying a lot of hours, sleeping also well, and also like distractions are the

1:6:42

obviously pass. So the model is able to predict the process, you can see. And here

1:6:50

here we have, uh, uh, then, uh, uh, diagramatically, yeah, dot fit was model been

1:6:57

and, uh, here here you can do the dot predict. And what is the model predicting? And what is the

1:7:03

the model predicting? Pars. We have, um, we, the diagram from the diagram.

1:7:07

model be that predicted. And finally, we'll last thing

1:7:12

will, okay? This a little complex

1:7:13

can, but I'll still go ahead and explain.

1:7:15

A little complex

1:7:16

can. But I'll still go ahead and explain. Just one last thing.

1:7:19

Okay. So, one second, guys.

1:7:23

Now, you can

1:7:24

here here. Here we've explained

1:7:26

here. We've seen here.

1:7:27

Okay? All of you saw it here.

1:7:34

Okay.

1:7:34

Last thing, I will talk

1:7:37

what, predict proba?

1:7:40

Predict proba, what you think? What are you?

1:7:43

Predict proba what? What are you?

1:7:45

Historical, based on the data, we build a model.

1:7:48

The data we're we're trying. And

1:7:50

the new data, given a new data, we either do dot predict and then dot predict proba.

1:7:55

Right? We learned it into his day. We said that, that we can find out the probability of the

1:8:00

prediction. And if probability of prediction, if probability of prediction, 50% thresholds

1:8:04

more than one predict or then zero predict

1:8:07

we discuss that concept. Now you have to tell me what is the

1:8:11

predict prova. Now, answer to make,

1:8:12

you have to tell me conceptually predict proba

1:8:16

what is. I'm here to explain that for this demo, but you have to tell me.

1:8:19

Conceptually, you have to tell me, conceptually, what are you

1:8:20

think? What do you think? I can give you a small

1:8:28

hint, you have to use this value thing to answer that question.

1:8:32

You have to look at this value and sample to look at it.

1:8:37

Okay?

1:8:38

So here, you have samples or value to look at it.

1:8:41

So answer, predict proba.

1:8:43

So given that new student,

1:8:45

you have a new student, you have a new student's

1:8:46

a new student, right?

1:8:48

Given a new student, data,

1:8:50

you have to predict can be that

1:8:51

pass or fail?

1:8:52

Now you have to tell me

1:8:54

what is the probability of the prediction?

1:8:58

You have to predict proba calculate

1:9:00

to calculate

1:9:01

number one, and then you

1:9:03

then you guys already did this part.

1:9:07

You've already did this part.

1:9:08

You've already done.

1:9:09

But remember, the machine in sequence

1:9:13

alike.

1:9:14

The machine's first predict proba calculated

1:9:16

and then probability,

1:9:18

prediction calculated, right?

1:9:20

So you have to tell me this part.

1:9:22

What the predict probability?

1:9:24

So you guys have already guessed this part, right?

1:9:27

You all have this correct guess

1:9:28

this correct guess.

1:9:29

Predict answer passed.

1:9:30

Well, it's done, this is sorted.

1:9:32

And pass is one.

1:9:33

One plus.

1:9:34

Past is one, fail,

1:9:36

means 0.

1:9:37

Bhabic says 165 by 166, excellent Bavik.

1:9:40

That is the answer.

1:9:42

This is your answer is.

1:9:43

This predict proba answer is.

1:9:44

Very nice.

1:9:46

Because this

1:9:48

the value 1 comma 165 is

1:9:50

what is?

1:9:51

What is?

1:9:52

What is?

1:9:53

You have taken the data, you have traversed

1:9:56

through all the nodes.

1:9:57

This final node in

1:9:59

there is a final load.

1:10:00

one customer who has failed,

1:10:02

the whole data message, there is only

1:10:04

one person who has failed and 165 are passed.

1:10:07

So the probability of a person

1:10:09

passing, this by default

1:10:12

zero class and this by default one class.

1:10:14

We have you

1:10:15

have to,

1:10:16

whenever it comes to Python, convention is always

1:10:18

left side, right side one.

1:10:20

Always.

1:10:22

So, prediq proba in

1:10:24

we have you had,

1:10:25

left side, right side one, always.

1:10:27

So same thing is happening here.

1:10:28

When you're predict proba

1:10:29

proba, so probability of pass is

1:10:31

165 by 166.

1:10:33

Total 166 rows are here

1:10:35

so probability of pass it's

1:10:37

that is the way to calculate.

1:10:38

And you can

1:10:39

this is such a high number as Bhabik has

1:10:41

rightly pin.

1:10:42

This 99.4%

1:10:44

close to 99%

1:10:45

that is more

1:10:47

that model is predicted pass.

1:10:49

Okay?

1:10:50

So we're

1:10:51

so we're a little bit

1:10:52

deep in here

1:10:53

so we don't have to get into all this

1:10:55

but I hope

1:10:56

but decision is important

1:10:57

so we've got

1:10:58

all the detail in here.

1:10:59

But I hope everybody is clear.

1:11:01

All clear.

1:11:02

Last one calculation we've

1:11:03

we've made

1:11:04

165 by 166.

1:11:06

Okay?

1:11:07

And you know the interesting part is

1:11:12

this

1:11:13

you've done here

1:11:14

you can clearly here

1:11:16

look at this.

1:11:17

This is the answer.

1:11:21

Predick Proba.

1:11:23

When I do Predic Proba,

1:11:24

I'm getting two probabilities

1:11:26

and you want to calculate,

1:11:27

you want to calculate, you want to

1:11:28

check. You can check

1:11:30

you, guys.

1:11:32

If you do 165 by 166,

1:11:35

you will get exactly this answer.

1:11:37

You'll get exactly this answer.

1:11:38

Now, let me see all of you?

1:11:41

Can you see all of you?

1:11:45

Same to same probability.

1:11:47

This is what you're getting.

1:11:49

So this predict proba

1:11:50

we just in last class

1:11:51

just like that

1:11:52

something that is a probability

1:11:53

here.

1:11:54

But today you're able to get a lot deeper

1:11:55

and understand that is what

1:11:56

probability.

1:11:57

How is calculated is.

1:11:58

under.

1:11:59

Okay?

1:12:00

So again, dot fit, build the tree, build the flow chart, learn the rules.

1:12:04

And the new data,

1:12:06

then, that new data to

1:12:08

that new data to traverse

1:12:09

like you guys have done.

1:12:11

Come all the bit to the leaf node.

1:12:13

Leap node,

1:12:14

look at the total 166 rows,

1:12:16

how are,

1:12:17

how many rows are,

1:12:18

and how many of fail,

1:12:19

and on its basis,

1:12:20

probability of prediction

1:12:22

and then.

1:12:23

And the probability

1:12:24

if probability is

1:12:25

than more than

1:12:26

if it is,

1:12:27

if it is here.

1:12:28

on 50% default threshold.

1:12:30

If you if you're

1:12:31

50% percent

1:12:32

if you can't

1:12:33

you can't

1:12:34

change the threshold

1:12:35

we'll

1:12:36

we'll change

1:12:37

it.

1:12:38

Is it okay?

1:12:39

Everybody's with me?

1:12:40

Yeah.

1:12:41

This is 99.39%

1:12:43

and I'll just like

1:12:44

once again take you back to

1:12:45

the diagram again

1:12:46

just so that everyone's clear.

1:12:47

Okay.

1:12:48

Okay, guys.

1:12:57

Come on.

1:12:58

Do let me know.

1:12:59

Confirm.

1:13:00

All clear.

1:13:01

Bawak is the only person who pink.

1:13:02

Others are all okay, right?

1:13:03

How are it?

1:13:04

That's all okay.

1:13:05

I'll go on.

1:13:06

If you're all okay, I'll go on.

1:13:08

All.

1:13:22

All of you

1:13:25

All of you?

1:13:27

All of you?

1:13:29

Clear?

1:13:33

Everybody?

1:13:34

Out of total, 166 rows,

1:13:37

one.

1:13:38

165 are predicted to be passed.

1:13:40

This is your 165.

1:13:42

Okay?

1:13:43

Just in case you are wondering, numbers

1:13:44

where are from?

1:13:45

165 by 166.

1:13:46

This is your head.

1:13:48

Okay?

1:13:49

This one,

1:13:50

part.

1:13:51

Just the last part what I discussed is a little,

1:13:53

you know, deep.

1:13:54

So that's why I'm just cross-checking again with all of you.

1:13:56

So pass,

1:13:58

all of you are sorted.

1:13:59

This is all of you are sorted.

1:14:00

But this part was a little dicey, I think.

1:14:02

Little tricky.

1:14:04

So again, same process is.

1:14:05

you're traversing.

1:14:07

You reach the leap node.

1:14:08

And the leap node,

1:14:09

and you're check that you're,

1:14:10

okay,

1:14:11

so out of total 166 rows,

1:14:13

out of total 166,

1:14:15

how is this?

1:14:17

So 165 out of 160 pass.

1:14:20

That's it.

1:14:21

If you were here,

1:14:23

if you,

1:14:24

if you traversed here,

1:14:25

then,

1:14:26

probability of pass,

1:14:27

10 by 20 would.

1:14:28

If you traverse

1:14:29

here,

1:14:30

then, the probability of pass

1:14:31

how would?

1:14:32

3 by 15 would.

1:14:33

Because this is,

1:14:34

12 is failed, 3 is passed.

1:14:35

01.

1:14:36

Okay, clear.

1:14:37

All of you.

1:14:38

And that's all of you.

1:14:39

And that's the

1:14:42

thing we've in the code

1:14:43

made.

1:14:44

Whatever I explained to you in concept,

1:14:45

the same thing we have implemented in code.

1:14:47

So code,

1:14:48

there's nothing to say

1:14:49

it's not.

1:14:50

It's actually

1:14:51

there's actually,

1:14:52

there's not.

1:14:53

So that's why I took some time to explain

1:14:54

the ideas behind it.

1:14:55

So code is simple.

1:14:56

Predic Proba and predict

1:14:57

exactly what we discussed last session.

1:14:58

There is nothing to talk about this.

1:15:00

Okay?

1:15:01

Same to same concept.

1:15:05

Okay. So moving on, we will get to the idea of something called a random forest.

1:15:11

We have a decision trees discussed here.

1:15:14

And decision trees in decision trees

1:15:15

what are effectively building one tree on the whole data.

1:15:20

We have the entire data and in that entire data we are building a tree.

1:15:24

Right.

1:15:25

Now, remember, to understand random forest,

1:15:31

we will take a small analogy.

1:15:33

Okay, we have a simple example.

1:15:35

analogy. Now, imagine you're the, you're the CEO of a company.

1:15:42

You're a company's a company CEO and you have a very decision

1:15:45

to make a very decision and you are the person who has been given the ownership to take that

1:15:52

decision. So, if it is only your call, if you're the only person making the decision,

1:16:01

then a bias is a bias.

1:16:03

You know, you have a preference case off the decision,

1:16:07

you have some money, like, people can get biased, right?

1:16:12

So that is why companies have boards.

1:16:15

Company in the board of directors are not.

1:16:17

So, any important vote in Tata may,

1:16:19

how big, some boat, which he shuffled were after,

1:16:22

you might have heard after written Tata's dead.

1:16:24

They were, like they were a fight.

1:16:26

So it's a big deal.

1:16:27

Tata is a big group in India, right?

1:16:29

Now, one one of one man was,

1:16:31

that we can do that.

1:16:31

Nobody can do that.

1:16:32

There is a vote that has.

1:16:33

happens. So all important decisions should always happen through voting.

1:16:46

It could be something as simple as you know, you want to go out for a team lunch.

1:16:51

Like many of you are working in companies, some of you are not.

1:16:54

When you're companies join work join, so there, so there always

1:16:58

have some of these are things. Some team party will and lunch, or

1:17:01

like to here to eat,

1:17:03

but what happens here to eat?

1:17:05

But what happens, usually?

1:17:06

Teams in what are, a voting.

1:17:09

There's team in 10 people.

1:17:11

Seven people will say, I'm here to go.

1:17:13

Two, we'll go here to, one will say, here to go.

1:17:15

So, who's going to?

1:17:16

The majority.

1:17:19

So this is a very important idea that I'm getting at.

1:17:22

And usually the majority always is a good decision.

1:17:27

If one people think, we're like we're saying,

1:17:29

but 100 people think it, it's not,

1:17:31

maybe they're right.

1:17:33

Let me give you another great example.

1:17:35

Who will be Kornuropathy?

1:17:36

I'm sure everybody has seen like two.

1:17:39

If you know, there's something called audience poll.

1:17:41

There's audience poll.

1:17:42

Actually, this is a very mathematical concept.

1:17:45

We're not going to go to much show you some part of it.

1:17:48

But I'm trying to give the intuition to you,

1:17:50

that what is it.

1:17:51

It's a beautiful concept.

1:17:52

If you want to study about it,

1:17:53

if you want to study about it,

1:17:55

there's a lot of maths done around it actually.

1:17:58

So the audience poll are, who can be able to korepati in.

1:18:01

So,

1:18:02

the question is asked.

1:18:06

Now, phone a friend is one.

1:18:08

You have a friend, one, you know,

1:18:08

if you one of the one of the one can't do.

1:18:10

So that's not a good

1:18:11

not really.

1:18:12

Now, a man can say,

1:18:13

he'll say, yeah.

1:18:15

He can answer.

1:18:17

But if he doesn't, then he doesn't,

1:18:18

then he doesn't.

1:18:19

Because if anyone

1:18:20

people who don't know

1:18:21

not, then he's,

1:18:22

if there's a question

1:18:24

then you're asking to somebody

1:18:26

who's a doctor.

1:18:27

He's probably not quite

1:18:27

not know.

1:18:29

But audience poll,

1:18:31

Now, you know,

1:18:33

that is correct.

1:18:36

But then if you look at audience poll,

1:18:41

audience poll is almost always correct.

1:18:44

Audience poll is almost always correct.

1:18:48

See, because we are not saying audience is very intelligent.

1:18:50

The audience in the audience who are not like some super humans or something.

1:18:54

They are all normal, average people like you or me.

1:18:56

And one say two, two, three people will ask,

1:18:58

that some day's capital is that they don't know.

1:19:00

I think an average people.

1:19:01

We don't know.

1:19:02

We're average people.

1:19:05

But you'd be surprised to know

1:19:06

that 1,000 average people coming together,

1:19:08

the decisions are always correct.

1:19:10

It's a fact, it's a mathematical reality.

1:19:13

So this, this is

1:19:14

proved in KBC in,

1:19:16

that audience poll is usually almost always correct.

1:19:20

Always.

1:19:21

Look, audience poll,

1:19:22

there's a big audience,

1:19:23

there are, 100 people, okay?

1:19:25

There's a question.

1:19:25

So if a very difficult question

1:19:28

if a very difficult question be,

1:19:30

even difficult question be,

1:19:31

Even then, it is proven,

1:19:32

it's data as far as it's

1:19:34

seen that the audience police usually correct.

1:19:37

It's not that they're experts who

1:19:38

sit, so many people who will

1:19:40

give a, which option B

1:19:42

and option C will vote correctly.

1:19:46

That is the idea of wisdom of the crowd.

1:19:49

Wisdom of the crowd is a beautiful match

1:19:50

concept. You can read about it. You can study about it.

1:19:52

You can learn it. You can learn it. And this applies

1:19:55

in so many disciplines in the real world also.

1:19:57

So real world, this is

1:19:58

this is in committees and boards may use

1:20:00

it's a big resolution

1:20:01

is, you know?

1:20:02

Now, like, you know,

1:20:03

like, you know,

1:20:03

the Iran's negotiations

1:20:05

are not that

1:20:06

Donald Trump's

1:20:06

mind there, so

1:20:07

could do anything

1:20:07

do it.

1:20:07

So it's not

1:20:08

not

1:20:09

run by one

1:20:11

person.

1:20:11

There's a board,

1:20:12

there's a cabinet,

1:20:12

there's a,

1:20:13

there's a, the Congress,

1:20:14

right?

1:20:14

What is the U.S.

1:20:15

Congress?

1:20:16

Now, Congress,

1:20:17

upro, upro,

1:20:17

before,

1:20:17

president impeached

1:20:18

there's all

1:20:19

everything.

1:20:20

We all

1:20:21

things

1:20:22

we all need, but

1:20:22

there is so much going on

1:20:24

behind the scene

1:20:24

that nobody even

1:20:25

knows, right?

1:20:26

There's so much that is going on.

1:20:27

There's so much, it's

1:20:28

not one person

1:20:29

decision or anything.

1:20:30

It is a resolution.

1:20:31

It's a board.

1:20:32

There are 100 people,

1:20:34

thousands of people

1:20:34

who are voting on some

1:20:36

activities, right?

1:20:37

So this is

1:20:37

a lot in practice.

1:20:39

I'll give you one more,

1:20:40

one last example of this.

1:20:41

Which is a great example.

1:20:43

Jury.

1:20:44

Any major court case

1:20:46

is a jury.

1:20:48

So in court

1:20:49

on it.

1:20:49

So in court on it.

1:20:50

There's a lot of hearing.

1:20:51

There's a lot of

1:20:53

last year we,

1:20:54

which, you do

1:20:56

anyway.

1:20:57

So there's a jury.

1:20:58

There's a jury that we

1:20:59

will be there, right?

1:21:01

So

1:21:01

some controversial

1:21:04

that central government

1:21:05

decisions on

1:21:06

there's

1:21:07

over there's

1:21:08

over there's

1:21:08

many, you know,

1:21:09

the voting

1:21:09

on the states

1:21:10

so whatever.

1:21:12

So whatever. So there's a

1:21:12

jury.

1:21:13

It is not like

1:21:13

one person's decision

1:21:14

that the chief justice

1:21:15

said,

1:21:15

ah,

1:21:15

man,

1:21:16

they're jury

1:21:17

were,

1:21:17

they'd,

1:21:17

three, four judges

1:21:19

juries,

1:21:19

jury,

1:21:19

they'd,

1:21:21

every judges

1:21:22

independently decide

1:21:22

decide.

1:21:23

Judge one

1:21:24

said,

1:21:24

yes, yes.

1:21:25

Judge two

1:21:25

said yes,

1:21:26

judge three said yes.

1:21:27

Se said yes.

1:21:27

Seven judges

1:21:28

said yes.

1:21:28

Yes,

1:21:29

they know

1:21:29

said.

1:21:30

Majority

1:21:31

what is

1:21:31

that's

1:21:33

all in our

1:21:33

non-sab

1:21:33

in

1:21:33

so the

1:21:35

point

1:21:35

is that

1:21:36

this is

1:21:38

the

1:21:38

concept of

1:21:39

wisdom

1:21:39

out of

1:21:39

the crowd

1:21:40

right

1:21:42

and this is

1:21:43

exactly the

1:21:44

issue

1:21:44

with a

1:21:45

decision

1:21:45

fee

1:21:45

if you

1:21:47

were brilliant

1:21:47

all

1:21:48

okay

1:21:48

but

1:21:49

it was

1:21:49

one

1:21:49

model

1:21:50

the decision

1:21:52

decision

1:21:52

because

1:21:52

basically

1:21:53

only one

1:21:53

model

1:21:53

one model

1:21:54

we

1:21:54

make

1:21:54

one

1:21:59

As I told you, a single decision fee is good, but it can be biased because of reasons I discussed.

1:22:06

So now the thing is that we'll make any decision piece.

1:22:09

What if we created many decision pieces?

1:22:12

I'm a,

1:22:12

we'll make a

1:22:12

decision

1:22:13

make a decision

1:22:13

we can't.

1:22:15

We'll

1:22:15

build a board

1:22:17

and

1:22:18

I will create many decision

1:22:19

piece

1:22:20

and make them to a vote.

1:22:23

And that is what we call an ensemble model.

1:22:26

This is to English in ensemble

1:22:27

group.

1:22:28

Ensemble vote.

1:22:28

Ensemble is.

1:22:29

is a group or collection.

1:22:31

So we are basically not building one model, but we are building a connection of models.

1:22:36

And this

1:22:37

thing, this is the forest of trees

1:22:38

is this is random forest

1:22:40

is called.

1:22:41

Today we're

1:22:42

first

1:22:42

we're telling what you.

1:22:44

You know,

1:22:44

maybe we used

1:22:46

in the first class

1:22:47

or we

1:22:47

we're

1:22:48

we're

1:22:49

we're gladium boosting

1:22:49

random forest

1:22:50

just

1:22:50

look and

1:22:52

that

1:22:52

that time I just

1:22:54

told you

1:22:54

that

1:22:54

this is very good.

1:22:56

This is a good model.

1:22:57

So

1:22:57

today you are you

1:22:58

that you know, you know, you know, you know,

1:23:01

you know,

1:23:01

you know,

1:23:02

you know,

1:23:02

regression class

1:23:03

we have

1:23:03

some gradient boosting or

1:23:04

random forest,

1:23:05

we used

1:23:06

we used

1:23:06

that.

1:23:06

We've said that

1:23:07

it's

1:23:08

accuracy

1:23:08

were being

1:23:08

I was able to

1:23:10

tell you that

1:23:11

accuracy is increasing.

1:23:12

That California

1:23:13

way, you

1:23:14

know,

1:23:14

we know,

1:23:14

we know,

1:23:14

the moment I

1:23:16

use gradient boosting

1:23:17

accuracy

1:23:18

that's

1:23:18

barred.

1:23:19

But what

1:23:19

is that

1:23:20

random forest

1:23:21

thing,

1:23:21

gradient boosting

1:23:22

they're all

1:23:22

ensemble models,

1:23:23

they're all

1:23:24

all

1:23:24

collection of many

1:23:24

models taken together.

1:23:26

That's the concept.

1:23:28

Okay, so tree and many, many trees taken together is a forest.

1:23:35

Now, coming to the code, coming to the implementation.

1:23:37

Implementation,

1:23:38

so

1:23:38

implementation is very simple.

1:23:44

But important hyperparameter is

1:23:46

an

1:23:46

underscore estimator.

1:23:47

Now you're

1:23:48

saying,

1:23:48

that you've already used

1:23:51

in the previous sessions.

1:23:53

This n underscore

1:23:54

estimators is controlling

1:23:56

how many trees you have in the forest

1:23:58

forest.

1:23:58

So, your board

1:24:00

your committee

1:24:02

committee is,

1:24:04

how many

1:24:07

trees you're having in that

1:24:08

forest?

1:24:08

So here I'm,

1:24:09

so I'm trying out

1:24:10

three different variations

1:24:12

of decision trees right now.

1:24:13

A decision tree with

1:24:14

estimate is equal to one.

1:24:16

One other decision with

1:24:17

estimate is equal to 100.

1:24:19

Another with estimate is equal to this.

1:24:20

So we can just try two of them.

1:24:21

And we can try out different

1:24:23

different estimators and build different

1:24:24

different models and we can see

1:24:25

which one is better.

1:24:27

And just like we discussed for a

1:24:28

decision P.

1:24:30

Decision P.

1:24:30

In decision tree, in hyper parameter, what are?

1:24:33

Decision tree in hyper parameter is basically the maximum depth.

1:24:41

Max depth is the hyper parameter for a decision P.

1:24:44

So we can control the maximum depth of the decision P.

1:24:47

And by controlling the maximum depth of the decision P, we can, so that is the hyper parameter.

1:24:53

The maximum depth of the decision P is a hyper parameter.

1:24:56

So we can control the depth of the decision P.

1:24:58

increase, decrease, decrease, underfit, overfit overfit and we can find the good fit.

1:25:04

So, similarly, what is the hyper parameter for a random forest classifier?

1:25:11

Joki, collection of many, many free z.

1:25:13

Now, hyper parameter for a random forest classifier is n estimators.

1:25:18

It is n estimators.

1:25:21

That is the hyper parameter for a random forest classifier.

1:25:24

So n estimators is the hyper parameter.

1:25:26

And how are the values impacted by these guys?

1:25:29

Values, how are the values?

1:25:30

How's impact here?

1:25:32

So, n-stimators, if one head or, model will be highly underfeit.

1:25:36

If n-stimators one-head, the model will be highly underfeit.

1:25:40

If n-stimates increases, model will become highly-overfitting.

1:25:44

And you are trying to find out what is the right value in between.

1:25:47

So that is the thing.

1:25:49

Okay.

1:25:51

So that is the way.

1:25:52

And this you have to try out.

1:25:55

This is like a hyper-trial.

1:25:56

parameter, you will have to try out different, different values and see which one works.

1:26:00

But generally, random forest will always give you better answers.

1:26:03

Always better answers.

1:26:05

And you're going to ask to answer your question.

1:26:07

To answer your question, let me tell me.

1:26:09

Let me, let me clarify, you know, to answer your question,

1:26:13

when you're making a decision, the process in which you created the decision people.

1:26:18

Just to explain to you intuitively, if you look at this tree that I will.

1:26:22

Now, look at here here we are giving study awards a lot of reference.

1:26:24

Can you see?

1:26:26

We are giving us a lot of reference.

1:26:26

a lot of preference to study hours.

1:26:29

I mean, the way that is again a different thing altogether.

1:26:33

It's a related thing, it's a related thing, it's a different way to make it.

1:26:38

But when you created this one particular decision, we made a certain sample of data

1:26:43

and made a tree, right?

1:26:46

So here there are some rules are.

1:26:49

But it can be that some features are given more preference.

1:26:52

I mean, here here we can we have study hours to do a lot more preference.

1:26:55

I mean, the first first hour, we're the first study hour basis in.

1:26:59

If you think about it, that may not be correct.

1:27:02

We're giving too much importance to study hour.

1:27:05

We've got our first root node in study hour,

1:27:07

that's the study hour more than this side, study hour more to this.

1:27:10

But that is not fair.

1:27:12

Why don't we ask something on sleep?

1:27:13

Why don't we ask, if you know, if your distractions are less than this?

1:27:18

So that is the idea.

1:27:20

That is why I meant that decision piece can be biased.

1:27:22

You know, is?

1:27:25

You know, you're in?

1:27:28

So then what we do is, we do is we take a little bit of data and we're

1:27:32

a different tree and we're a different tree.

1:27:33

Then we're a different tree.

1:27:35

We're a lot of many pieces make.

1:27:36

Like you're here here, this is very detailed.

1:27:39

Here we're not going, but.

1:27:40

So, like this is, NST matters 100.

1:27:43

Here we're 100 different decision trees

1:27:44

make.

1:27:45

We're so decisionaries being here.

1:27:48

And so decisionaries

1:27:49

make that, we are trying to do a prediction.

1:27:52

Okay, if you're, if you're pictorially

1:27:55

to look at, what,

1:27:56

what are here here behind the scenes,

1:27:59

at a very high level,

1:28:01

pictorially, if you want to just explore

1:28:03

and see, I can show you.

1:28:06

You can show you.

1:28:09

You have your, uh, you're here here here.

1:28:14

So this has come all the way down.

1:28:18

And if you see, this is the end result of what we try to make.

1:28:22

end result.

1:28:23

End result is what we are trying to do here.

1:28:26

So, you're allah, other training sets are

1:28:28

making.

1:28:29

Okay?

1:28:30

So you're here a little intuition here.

1:28:32

Again, we're not getting to the depth of the algorithm,

1:28:34

but just to give an intuition.

1:28:36

So you're trying to basically take the data,

1:28:38

and you're trying to kind of split the data in different different ways.

1:28:41

You're a little bit data

1:28:42

later.

1:28:43

We use a different data and we're

1:28:45

and we're a lot of trees make.

1:28:47

Here, there's a tree,

1:28:48

there's a other here,

1:28:49

here a tree,

1:28:50

here here, let's sleep hours first.

1:28:51

Here,

1:28:52

here here,

1:28:54

study hours root node go.

1:28:55

So we are trying to create different, different trees.

1:28:57

All right trees,

1:28:58

and then final prediction will.

1:29:01

Final prediction,

1:29:02

let's say person one, pass,

1:29:04

person two,

1:29:05

pass, person three,

1:29:06

so majority will pass.

1:29:08

That's the way how the predictions are made.

1:29:10

And that is the reason why random forest model is

1:29:12

generally more,

1:29:14

generally more accurate.

1:29:17

That's the intuition.

1:29:22

Just one last thing, just one last thing, remember,

1:29:26

because random forest asks many, many questions,

1:29:30

these models can automatically figure out which features are important for making decision.

1:29:34

That is also an important factor.

1:29:36

So random forest in a built-in concept called feature importance.

1:29:40

Just keep that at the back of your mind.

1:29:43

Okay, so here we have code just to make sure that you are creating a bar chart.

1:29:47

But if you find this code too confusing,

1:29:50

if you're very much more,

1:29:51

a lot more long code is.

1:29:53

So all that I did was I just did this.

1:29:55

Actually, we just did this.

1:29:56

Actually, this is actually, this code is a line

1:29:58

is.

1:29:59

You have a little longer

1:30:00

because you have created bar chart, added colors,

1:30:02

and hunt, a little of formatting to make it easy for you.

1:30:05

Okay, but actually it is the model.

1:30:07

The model dot feature underscore importance is underscore.

1:30:10

Here you have to feature importance

1:30:12

see here.

1:30:13

So exactly in the order in which the features

1:30:15

are coming in your training data.

1:30:17

Training data,

1:30:18

what is the first in the data

1:30:20

study over sleep hour distraction exactly in that order

1:30:24

study our sleep hour distraction exactly the order

1:30:28

they have us order in

1:30:30

you will be able to see the feature importance values

1:30:33

that means this particular feature is

1:30:38

74% important this is 13% important

1:30:41

and this is 12% important so this is also very important

1:30:44

so by building the model you can also tell

1:30:47

you can not only build the model itself but

1:30:49

but you know this form in the model in

1:30:51

which feature is considered more important.

1:30:54

So you can see study hours is actually given much more important.

1:30:57

Now, so now what we will do,

1:31:01

we'll get to the next phase of our conversation

1:31:04

and again I'll keep aside some time for the demo also.

1:31:07

Just to clarify, we will see that as well.

1:31:09

But now to come back to the conversation,

1:31:11

we will understand why accuracy is not enough.

1:31:15

See all this file we have been discussing only about accuracy.

1:31:18

Okay, you want to take a short.

1:31:19

break guys you want to take a quick break

1:31:21

wait session i think 920

1:31:23

so we can take a break

1:31:25

let's take a break and come back and after the break we will discuss

1:31:28

about accuracy

1:31:29

this is the related thing compared to what you have discussed before

1:31:32

accuracy precision recall

1:31:34

or some case studies kind of for some

1:31:36

we'll try to do some case studies and give you some data sets and you can solve it

1:31:39

that is going to be the plan after the break

1:31:41

let's take a short break and meet back after

1:31:43

after five minutes

1:31:49

You know.

1:32:19

You know,

1:32:49

You know,

1:33:19

I'm

1:33:49

I'm

1:34:19

I'm

1:34:21

I'm

1:34:23

I'm

1:34:25

you

1:34:53

I'm

1:34:55

you

1:35:23

I'm

1:35:25

you

1:35:53

I'm

1:35:55

you

1:36:23

I'm

1:36:25

you

1:36:53

I'm

1:36:55

you

1:37:23

I'm

1:37:25

I'm

1:37:53

I'm

1:37:55

you

1:38:23

I'm

1:38:25

I'm

1:38:53

I'm

1:38:55

you

1:38:57

I'm

1:38:59

I'm

1:39:01

I'm

1:39:05

I'm

1:39:09

I'm

1:39:13

I'm

1:39:17

I'm

1:39:21

I

1:39:26

I

1:39:31

Thank you.

1:39:33

Thank you.

1:40:03

Hi, folks, welcome back. So we'll continue on now.

1:40:27

So before the break, we looked at the, we looked at two other, two other algorithms primarily. So continue

1:40:33

on from logistic regression, we looked at something called, something called decision

1:40:38

trees and we looked at something called random policies for the two specific algorithms we

1:40:43

we explored. But the process is again the same. We have the data, train test plate,

1:40:48

dot pit, dot score, dot predict, dot predict proba. Same thing is. No difference

1:40:52

now we will look at another very interesting concept. So we also, we already saw Confucian

1:41:00

metrics. Now I'll start the conversation from there. We will recap a

1:41:03

little bit of that and we'll go to a slightly different data set for a minute, okay?

1:41:12

So imagine we are trying to predict a disease, okay? We are trying to predict a rare disease.

1:41:17

So we have some data with us right now, but we'll we'll show what data we have right now. So this

1:41:22

our data set is. So imagine that as for my data set, let me just show the data set to you first.

1:41:29

We are some data set here. DF underscore disease is my data.

1:41:33

So let's say for a minute, DF underscore disease is my data.

1:41:37

Right? I'm keeping it very simple right now. And this is my data set. And you can see.

1:41:48

So you can clearly see that these are the two input Xs. Health metric one, health metric two.

1:41:56

Health metric two, it's a simulated data. It's a sample data that I'm giving you right now.

1:41:59

Health metric one, might like, mean, your blood pressure, or health.

1:42:03

ultimately to some other things.

1:42:05

Let me have your cholesterol.

1:42:07

So based on the blood pressure and cholesterol, you are trying to predict whether the person has

1:42:11

some disease or not has some disease.

1:42:13

So status one, means disease is.

1:42:14

Status one, means, it's not.

1:42:16

This is very similar to that cancer example we did.

1:42:19

Don't do it.

1:42:21

Which day, we did.

1:42:21

We did this thing here.

1:42:22

There were many features there.

1:42:24

On the basis, you are to predict that the man's cancer is or not.

1:42:27

That's it.

1:42:29

Yeah, it's the disease prediction.

1:42:32

But whenever you look at any.

1:42:33

kind of disease prediction problem.

1:42:36

The thing is that most people will be healthy, right?

1:42:42

If you're this data set be, most people will be healthy on only 10 are sick.

1:42:47

Actual data maybe if you look, most people will be healthy and only 10 will be sick, right.

1:42:52

That is the thing.

1:42:53

We've made this total breakdown.

1:42:54

This is our data set.

1:42:56

Health metric.

1:42:56

We've only head lia.

1:42:58

If you're poor data, the status is that, there are 990 zeros.

1:43:03

Most of them are, most of them are.

1:43:03

zero and there are only 10 ones.

1:43:07

That means as part of my training data, whatever training data I have right now,

1:43:12

there are 990 people who do not have a disease and there are only 10 people who have a disease.

1:43:17

This is the nature of my data right now.

1:43:20

Okay?

1:43:21

This to have I assume for a minute.

1:43:24

Now, what if I build a model?

1:43:29

Imagine for a minute that.

1:43:33

we are taking this data and we're ahead decision tree set.

1:43:38

Now, look what have I done?

1:43:39

This is my data set.

1:43:41

And now I will build a decision pre model on this data.

1:43:45

This is our data.

1:43:47

Same thing.

1:43:48

We're decision tree model.

1:43:50

Model dot fit X comma y.

1:43:53

We have model made.

1:43:54

And based on that model, I will try to do some predictions.

1:43:59

So, what will happen?

1:44:02

So, if my.

1:44:03

If my model is giving 99% accuracy,

1:44:10

my model is right now giving 99% accuracy,

1:44:13

what can you say?

1:44:15

Can you say that you've got a very good quality model?

1:44:20

So that is what we did until now, right?

1:44:22

Until now, that is the only thing we discussed.

1:44:25

Now, our only understanding was that, okay,

1:44:27

if accuracy more got got got to, okay, if accuracy got a bad model,

1:44:32

accuracy is a very good model.

1:44:35

That has been our understanding so far, right?

1:44:39

But you have to understand to be that dummy model.

1:44:43

This model is not doing a good job.

1:44:45

I mean, if I take some time to explain to you further,

1:44:52

this are your actuals, right?

1:44:55

This actuals, there are 990s.

1:45:00

These are all 0,000, these are 0,000, we can,

1:45:02

keep writing. There are 990s that zeros we have. And there are 10 ones.

1:45:07

You have a actual set. But what if you are building a dummy model?

1:45:14

I'm a example. Here we're here. Here we're an example. We're making a dummy model. So,

1:45:19

our data this is the actual data that is given to you. But what if on the basis of this particular

1:45:28

data you are building a dummy model.

1:45:32

Dummy model, meant a fake doctor.

1:45:35

That dummy doctor is.

1:45:36

If any other person who will say, you have a bachar not, your disease, not.

1:45:40

So predictions what will be doctor's?

1:45:42

For a minute, some way.

1:45:44

If you go to our doctor today and the doctor always says,

1:45:48

your locality doctor always says you don't have a disease.

1:45:51

So they'll all not disease mark it.

1:45:55

The doctor will mark everybody to not have a disease, right?

1:45:57

That is what will happen.

1:45:58

So all the prediction is zero.

1:46:01

Because that dummy model.

1:46:02

That doctor is actually not looking at the data and doing a correct prediction.

1:46:07

That is a zero mark right?

1:46:09

That is the problem.

1:46:11

But what is the accuracy going to be?

1:46:13

That accuracy can't.

1:46:14

Accuracy is that he 99% is.

1:46:17

Because you, you know, you check

1:46:18

there are 990 zeros and 10 ones, right?

1:46:24

If you if you're in math

1:46:25

all are predicted to be zeros.

1:46:28

Doctor has all said zeroed.

1:46:31

So how it's correct.

1:46:32

predictions were accuracy.

1:46:34

Accuracy is what?

1:46:34

Accuracy is out of total number of predictions.

1:46:38

Accuracy,

1:46:38

means out of total number of prediction.

1:46:40

I mean, total the 1,000 pros are.

1:46:43

It's not correct.

1:46:44

10 is incorrect because these are all marked as 0.

1:46:48

But the 990 actual 0s are

1:46:51

that's all predictions are matched

1:46:52

so there are 990 predicted,

1:46:54

which are actually correct.

1:46:55

So 99% accuracy are not?

1:46:58

Now you look,

1:46:59

now, we have kind of,

1:47:02

This is like model fraud.

1:47:04

It's like model fraud.

1:47:05

It's like a fraud only, right?

1:47:06

You are, you are trying to build a dummy model

1:47:09

and just to give me or showing that,

1:47:10

okay, you know, I've got a great model,

1:47:11

99% accuracy.

1:47:13

That is not correct.

1:47:15

So the key learning right now is that accuracy

1:47:18

is cannot be the sole indicator of evaluating a model.

1:47:23

Accuracy is, we can't understand

1:47:24

we can't understand.

1:47:25

I hope everybody is clear.

1:47:29

Now, what else is,

1:47:31

else can be used.

1:47:33

Here, what you can go back and do is,

1:47:36

you can go and start to use the concept of

1:47:40

the Confucian matrix.

1:47:45

Confucian matrix

1:47:47

last week,

1:47:49

a Tuesday discussed

1:47:51

discussed.

1:47:52

If you're a Confucian matrix

1:47:54

will make the Confucian matrix will look exactly like this.

1:47:57

The Confucian matrix will look exactly like this.

1:47:59

The Confucian matrix will look exactly like this.

1:48:01

And you know, this is exactly what the confusion matrix they look like.

1:48:06

And if I just, you know, convey the story once again to you here.

1:48:09

You can see you.

1:48:10

Same to same story.

1:48:13

Actual data here here, 990 zeros, 10, once.

1:48:16

Predictions, dummy doctor have.

1:48:18

Sara zeros predicted.

1:48:19

Doctor doesn't want to take a risk.

1:48:21

Because he also, he knows that most people will not have cancer.

1:48:23

He doesn't take any of cancer,

1:48:25

he will be, he will be able to say,

1:48:26

he'll say,

1:48:27

he's not, 90% accurate,

1:48:29

but once you do.

1:48:30

But once you do.

1:48:31

the Confucian matrix.

1:48:32

Confucian matrix.

1:48:33

What is?

1:48:34

Everybody remembers, right?

1:48:35

Confucian matrix is a plot between actual and predicted.

1:48:39

Okay?

1:48:40

So, columns in your predictions are

1:48:45

your predictions, right?

1:48:47

Predictions, zero, predictions one.

1:48:50

And row, your actuals are actuals.

1:48:53

So actual one.

1:48:56

So columns in you have prediction zero, prediction one.

1:48:59

So row, you have actual, actual one.

1:49:00

0, actual 1. And now you get a true idea as to what is really happening.

1:49:05

We have already discussed last week, Tuesday.

1:49:08

So you can see the row totals.

1:49:10

There are 990 actual 0s.

1:49:13

And there are 10 actual ones, guys.

1:49:16

This is all right?

1:49:17

We have discussed.

1:49:18

Row totals, what are?

1:49:19

What total zeros are?

1:49:21

This is sorted.

1:49:22

This is sorted.

1:49:23

We have already seen.

1:49:24

Right?

1:49:25

And now,

1:49:26

column totals in you clearly

1:49:28

clearly, the model is that is making 1,000 0 predictions and 01 predictions.

1:49:35

No one prediction.

1:49:36

The model is not making a single 1 prediction.

1:49:39

And that Confucian matrix is proving that.

1:49:42

Accuracy is not.

1:49:43

Accuracy is not 99% were

1:49:45

because accuracy, but the moment you look at the Confucian matrix,

1:49:48

you're getting a clear idea that the predictions

1:49:51

column is the one column is completely zero.

1:49:56

But whatever model you build is not making a

1:49:57

you build is not making a single one prediction.

1:50:00

That is number one.

1:50:01

Number two, number two,

1:50:03

number two, here we're another color add

1:50:05

this is your false negative.

1:50:08

You have you discussed false negative last time.

1:50:11

False negative is a scenario where model predicted

1:50:14

you do not have a disease,

1:50:17

but actually you have a disease.

1:50:18

It's a dangerous scenario.

1:50:20

Thus false negative is dangerous.

1:50:22

So we cannot afford that.

1:50:24

We have to make it zero.

1:50:25

So there are 10 such cases that.

1:50:26

There are 10 such cases where model in predict that

1:50:28

it was 0,

1:50:29

because it was 0 predict that, but there are 10 such cases

1:50:31

are 0 predicted, but actually it's 1.

1:50:33

That is unacceptable.

1:50:34

That also needs to be reduced.

1:50:36

So the two issues are here.

1:50:37

So the moment you start looking at the Confucian matrix,

1:50:39

you will get a clear idea as to what is going wrong in the model.

1:50:43

So very important takeaway from this particular concession,

1:50:46

accuracy cannot be trusted.

1:50:48

And Confucian matrix should be used.

1:50:51

This is what we'll be getting into right now

1:50:54

as a new topic right now.

1:50:55

topic right now.

1:50:56

This is we know.

1:50:57

We just a revisit for example

1:50:59

of the Confucian matrix can use can use

1:51:01

can.

1:51:02

We go and we'll go and

1:51:04

here we will learn about another related thing called

1:51:08

the classification report.

1:51:10

So we're going to go to classification report.

1:51:12

Okay, so let us take a look at that.

1:51:15

So what is the classification report?

1:51:18

Let us see that.

1:51:22

So, first, at a high level, we'll see that.

1:51:24

we can you, on the same data, we can

1:51:27

on the same data,

1:51:29

when we build the Confucian matrix,

1:51:34

this is what I'm getting,

1:51:36

or on the same data you can also do something called the classification report.

1:51:39

So that you can also do that

1:51:40

can't, that you can't.

1:51:42

Now, first let us understand the theory,

1:51:44

that precision, recall, and what is what are

1:51:46

what are these metrics?

1:51:48

What these metrics actually are?

1:51:50

So this is a theoretical.

1:51:51

So let us understand what is the concept behind it.

1:51:53

the concept behind it okay just allow me a minute guys we will take a moment

1:52:00

and try to understand what is the concept behind these things

1:52:23

This is again to help you recall the Confucian matrix.

1:52:26

I'm sure everybody's done this already,

1:52:28

but I'm just trying to, because this is related to the Confucian matrix.

1:52:30

I'm just up to this slide open so that you are able to remember what we discussed already.

1:52:35

So this is your Confucian matrix is.

1:52:36

All of you recall just from last plus.

1:52:38

Predicted 0, predicted 1, actual 0, actual 1.

1:52:41

This is your true negative, true positive, false negative, false positive.

1:52:45

This is a wonderful way to evaluate your model.

1:52:47

Your model made, dot fit you did, and now you are doing dot predict.

1:52:51

And you're not just, you're not just,

1:52:53

not just looking at the accuracy of the model because now we know accuracy cannot be trusted.

1:52:58

If your dummy model is, if the model always predicts not disease, so accuracy

1:53:03

you need to look at the Confucian matrix to get a clear understanding

1:53:07

that what is exactly going on in the model.

1:53:09

And these are all model evaluation metrics.

1:53:12

It is done.

1:53:13

You have the data, you've already built the model.

1:53:15

You've made tree, you've made, our rules, made.

1:53:17

Then after, this is all about model evaluation.

1:53:20

Accuracy, training, testing, store go go.

1:53:23

matrix, the classification report are all evaluation metrics.

1:53:28

The model been made, that we're now in test in evaluate.

1:53:32

Okay.

1:53:33

There are two primary pillars we will be discussing right now.

1:53:37

So one is called precision, one is called recall.

1:53:40

And it's related we'll be discussing something called an F1 score.

1:53:43

So that is what we'll be seeing right now.

1:53:45

So, quare, one on one there is formula is.

1:53:47

I mean, we're, we can you, we can tell us how we can't tell us what, but you

1:53:51

we don't have to memorize the formula, but there is a formula,

1:53:56

but you don't have to memorize it.

1:53:57

We'll have you, we'll have interpretation, we'll give them, but this formula is.

1:54:01

This is a precision formula is, this is the way how we calculate these things.

1:54:06

So Confucian matrix, I've already discussed last week, Tuesday, you already know what is TN,

1:54:11

what is TP, what is F and what is F, you already saw that.

1:54:14

I repeat again, guys, please remember, it's binary for.

1:54:18

All this is for binary.

1:54:20

Multicast of we promised.

1:54:21

we'll do that that is something we will do today.

1:54:25

That is multi-class but this is all for binary.

1:54:27

The content doesn't get into multi-class.

1:54:29

We'll give you one.

1:54:31

This is all binary, either zero or one,

1:54:33

or zero or one.

1:54:35

Now that you know this, on the basis of that,

1:54:38

you can calculate can.

1:54:39

You're precision recon to calculate can.

1:54:42

So this is the way to make a record.

1:54:45

Now, if you don't want the formula-oriented way,

1:54:48

here we have our Niput's explained to just to make it easy for you to understand,

1:54:54

but you can't ignore it can't if you're not comfortable.

1:54:58

So,

1:55:00

first here here we've explained

1:55:01

that in the context of diabetes data,

1:55:04

not diabetes, diabetes, diabetes case

1:55:05

explained here.

1:55:06

This is our Confucian matrix, you can see here.

1:55:09

Predicted 0, predicted 1, actual 1, actual 1,

1:55:12

same to same T, N, P, P, P, P, P, P, P, P, P, P, P, P, P, F and F,

1:55:14

whatever I explained to you, we have, same to same T, here.

1:55:17

Okay?

1:55:18

How many we'll our slide in explain

1:55:20

that we'll explain, what we're

1:55:21

what is what is, what is

1:55:24

from here, conceptual, what things.

1:55:26

Okay, so this is what I will explain to here.

1:55:28

This is all right, all right?

1:55:30

Now, now, first, accuracy is what is,

1:55:33

accuracy is nothing but TN plus T2 by total.

1:55:35

So how many correct negatives?

1:55:37

How many correct positive by total?

1:55:40

So whatever accuracy we have been discussing all this fight,

1:55:43

it's any of the problems

1:55:45

ever we used the term accuracy,

1:55:47

what is accuracy exactly exactly?

1:55:48

exactly accuracy is nothing but the number of true negatives plus number of

1:55:53

two positives divided by totally that is the way how we understand the meaning of accuracy

1:55:58

so overall how many two negatives plus how many total true positives divided by

1:56:04

total so that's the way how we understand the meaning of accuracy

1:56:07

you're your accuracy here. Now,

1:56:11

Age, we're precisioned. Precision of one plus what does it mean? It means. It means

1:56:18

means how well the model is able to predict.

1:56:21

That's how well how well is the model able to predict?

1:56:26

So if you look at the one class right now, there are total 46 predicted ones.

1:56:31

If you look at the one class right now, there are total 46 predicted ones.

1:56:37

And out of 46 predicted ones, 35 of them are correctly predicted.

1:56:47

Column total what is?

1:56:50

Let's look at first.

1:56:51

Precision is defined as 45 by 35 by 46.

1:56:55

The formula, which we've seen in the slide in that slide, that one way to do it.

1:56:59

You can memorize one way to do it. You say, you memorize it. Other way, you

1:57:02

you can, you know, it's conceptually summed.

1:57:03

So, precision is nothing but 35 by 46, column total.

1:57:08

What's what? You look at the one column.

1:57:12

If they're predicted, it's predicted, it's predicted diabetes are.

1:57:17

There are total 46 diabetes predictions we are making.

1:57:21

And out of total 46 diabetes predictions we are making,

1:57:25

35 of those predictions are correct.

1:57:29

Out of total 46 diabetes predictions we are making,

1:57:33

35 of those predictions are correct.

1:57:37

That means the precision.

1:57:38

How precise are we in predicting diabetes?

1:57:42

I'm net 46 diabetic predicted.

1:57:45

I'm let's to 46 disease predict car did.

1:57:47

row or column total level. But out of that, how many are correctly predicted?

1:57:53

That your precision is. How precise are? How precise are in our position?

1:57:59

Okay. And recall is what? So it's, so it's kind of? You know, it's a

1:58:02

kind of recall kind of? You know, it's a reason to say you. How, how precise are you?

1:58:08

And recall had the ability to detect correctly. That out of 55 actual number of diabetic people,

1:58:17

Out of 55 actual number of disease people, in the whole data said there are 55

1:58:23

disease people. So row total got. So out of actually 55 disease people,

1:58:29

you have after, how many? How many were you able to catch?

1:58:35

So 35 out of those 55 people you were actually able to catch.

1:58:39

This is your report.

1:58:42

Okay, so precisioned over 35 by 46. Out of 46, 35 of them,

1:58:47

are, our, that is, precision. And recall what got? Recall got, 35 by 55. So,

1:58:54

yeah, it was a row total. So out of 55 actual diabetic, just the actual diabetic cases have

1:59:01

our, 55 actual disease, loch, one of those, our model has how much correctly captured

1:59:07

here. 35, it was able to correctly capture. So that is the way how we understand the meaning

1:59:13

of recall. So this is precision, this is recall.

1:59:17

Similarly, we can zero class for, so usually zero for here

1:59:22

here, but we can't, because the concept is the same.

1:59:25

So zero for the same thing.

1:59:28

So if you're going to it, so same thing is.

1:59:30

Precision of zero class,

1:59:31

I mean out of 108 predicted zeros, how many are correctly predicted?

1:59:36

So 88 are correctly predicted.

1:59:38

And out of 99 actual zeros, how many are correctly detected?

1:59:43

So this many are actually detected.

1:59:44

So this is actually detected. So this is, kind of less common.

1:59:47

So one plus is focus. We can see precision of one plus and recall of one plus.

1:59:53

And precision means how well you're able to predict correctly and recall means how well you're

1:59:58

able to detect correctly.

2:0:00

But out of 46 predicted ones, you've got four 26 ones predicted here. Out of 46 predicted ones,

2:0:07

how many were you able to correctly predict? You were able to correctly predict 35 of them.

2:0:13

So out of 46, once that you predicted, 35 of them are correctly predicted.

2:0:17

That is the precision. How precise are you? And out of 55 detected ones, this many are

2:0:25

correctly detected. It's the detection default. That's okay. So, but then turns out the precision

2:0:34

we call, uh, uh, uh, go allot-alach change was okay? And that's the reason. Because, uh, FP,

2:0:40

fn, if you increase, so we need some balance, right? So we need some balance, right? So, so,

2:0:47

The balance there is what is referred to something called an f1 score.

2:0:55

You just, you don't have to like get into the details of it.

2:0:59

So it is kind of like an average.

2:1:02

It is kind of like an average of precision or recall.

2:1:04

As we're arithmetic mean a plus b by two.

2:1:08

Like a thing is called harmonic mean, so that's a commonic mean. So that's your f1 score.

2:1:12

So key learning, we have learned precision. We have learned recall. We have learned

2:1:15

So workflow, what now? Data has, you made model

2:1:19

you've made up. Dots to fit

2:1:22

model, model been got, dot score,

2:1:24

accuracy over. There, so clear, it, it's sorted

2:1:26

and then. Conficion matrix

2:1:27

got, we discussed that on Tuesday.

2:1:30

Confucian matrix has been sorted.

2:1:32

Here until we've been made. Now, we are discussing.

2:1:35

Now, we are discussing, now

2:1:35

here from, how can we find out

2:1:38

what is precision, what is recall, what is

2:1:39

effort? That's our name. That's all.

2:1:42

That's all. Nothing.

2:1:44

Simple. So precision is.

2:1:45

nothing but how well we are able to predict?

2:1:48

Column total, you can

2:1:49

see, actually, this formula is.

2:1:52

So I'm just trying to explain that

2:1:53

that you're how you can't

2:1:55

actually say, actually, actually, it's a formula

2:1:57

is that TP by TP plus LP.

2:1:59

This formula is.

2:2:00

But you can remember it this way,

2:2:02

that out of 46 predicted

2:2:03

once, 35 are correctly predicted.

2:2:06

How precise are you? How well you are able

2:2:08

to predict? So that your precision

2:2:09

had, recall had got.

2:2:11

Out of 55, actual ones,

2:2:13

35 are correctly predicted, detected.

2:2:15

It's how good detect

2:2:17

and F-1 score is like the average of it.

2:2:20

And this is our classification report

2:2:23

in. This is the magical thing about the classification report.

2:2:27

This is up manually

2:2:28

nothing to do. That's why I told you,

2:2:29

interpretation is all it matters.

2:2:31

So this concept for we have you

2:2:33

but ultimately, in the real world,

2:2:36

you just have your data

2:2:37

will just have to create the Confucian matrix.

2:2:41

You have to make Confucian matrix.

2:2:42

You have confucian matrix

2:2:42

and make classification report

2:2:43

and all the classes have,

2:2:45

that classes of F-1 score, and

2:2:47

and all ignore them.

2:2:48

Just look at the F-1 sports,

2:2:50

look at the individual classes,

2:2:52

look at the F-1 scores, and see which class has a higher F-1 score.

2:2:56

So here you can see the

2:2:58

the class one is, the disease class is,

2:2:59

that's a F-1 score is

2:3:00

my model, to some extent,

2:3:04

is unable to predict diseases correctly.

2:3:07

So here we have improvement to do.

2:3:10

So two classes are,

2:3:11

and so I often say this is the class level accuracy.

2:3:14

The overall accuracy

2:3:15

that is the overall accuracy.

2:3:16

What is the overall accuracy of the whole thing?

2:3:19

That is called the overall accuracy.

2:3:20

Pura model's overall accuracy.

2:3:22

But what you are seeing right now,

2:3:23

this is called the class level of accuracy.

2:3:25

So for each and every individual class,

2:3:27

zero class, one class,

2:3:28

what is the performance of each and every individual class?

2:3:31

The disease class, how is it performing?

2:3:33

69% accurate.

2:3:35

Zero class, how is it performing?

2:3:37

85% accurate.

2:3:39

So F1 score is nothing but the class level accuracy.

2:3:42

That's one way you can interpret this.

2:3:45

So, okay, everybody's with me.

2:3:53

This is just a summary of what I talked about.

2:3:55

I think you can just maybe look at it for a minute exactly what I talked about.

2:4:00

So all the alarms we raised, how many were real?

2:4:02

So how precise are we in the prediction?

2:4:05

How precise are we?

2:4:06

And we call, of all the actual events that happened,

2:4:08

of all the actual diseases, how many did we catch?

2:4:11

Whatever model we did we build,

2:4:13

how many of the actual diabetic people is it actually actually?

2:4:15

that's the important thing that we discussed about. And what is the compromise?

2:4:19

What is the ultimate compromise? F1 score?

2:4:21

F1 score's from your balance. Instead of looking at precision recon, you can look at F1 score

2:4:26

and an F1 score is like a balance of both precision recall.

2:4:29

But if your F1 score is more, then both are. That's why I say that is the ultimate metric

2:4:34

and this is like your class level accuracy. So going forward, we will never look at the overall accuracy.

2:4:39

Now we're going to overall accuracy, now we'll go ahead, only F1 score

2:4:43

look at the class of F1 score, what is, the whole classes of F1 score, if

2:4:47

if a model of classes, F1 score are actually, then we will say that's a good quality model.

2:4:52

Because we will never trust accuracy.

2:4:54

So key learnings, never trust accuracy.

2:4:56

If dummy model, then accuracy is more accuracy, so we should always trust these metrics.

2:5:01

Either confusion matrix, or classification report.

2:5:04

So these are two things that we'll see.

2:5:07

Now coming to the code, is the implement.

2:5:09

This presentation is simple. If you want to know, sir, it's how to make it? All that

2:5:14

we do is we use this particular function. That's it. This is our classification report

2:5:18

is our two things, two learnings have our. So first learning is we discussed

2:5:23

confusion matrix, which we've already last session in, right? So Confucian matrix we can do.

2:5:30

Why test or RF predictions for confucian matrix. Right? This is simple. And now. And now,

2:5:39

Now, the next learning we had was classification report.

2:5:41

So exactly, as we have our slide in you

2:5:45

saw, same to same thing, we have here from here, so same to same,

2:5:49

same to same interpretation.

2:5:51

You take the data, build the model, dot predict, get the predictions.

2:5:54

And Confucian matrix is a comparison of the actual why and the predicted why.

2:6:00

And the classification report is also the argument should be the actual why and the predicted one.

2:6:05

There you have classification report takes into it.

2:6:08

So this is the way.

2:6:09

a past fail problem. So you have here

2:6:10

there. This is actually a very good model. This model is very good.

2:6:15

This is a simple data set. We'll go. So this is zero class and this is one class.

2:6:21

two classes are we have. So you can see how they can't.

2:6:23

So you know, two classes' performance is a good performance. So this is a very good thing.

2:6:29

So my model is doing very well for both the classes. The past failed be past class also. It is doing

2:6:36

very well. And feel plus also it is worth your own.

2:6:39

That's to me how it is working.

2:6:41

What about our dummy one?

2:6:43

Dummy for this one, Confucian matrix.

2:6:47

Let us see you guys.

2:6:48

The dummy model for those for us for

2:6:50

a classification report for, okay?

2:6:53

So this will be interesting to see.

2:6:55

It's for a classification report

2:6:58

then you'll be so much in the same

2:7:00

exactly what the issue was.

2:7:02

Here we're a classification report

2:7:07

you can.

2:7:08

You can see what we'll make a classification report.

2:7:09

This is your Confucian matrix and now you look at the classification report.

2:7:13

You can see, accuracy is a worthless metric.

2:7:16

But the moment you start looking at class level accuracy,

2:7:19

you see if one class, it's accuracy,

2:7:22

f1 score is very very low, 0%.

2:7:24

So the model is worthless.

2:7:27

Both ways you can interpret.

2:7:29

You have confusion matrix even

2:7:30

that there is no one predictions.

2:7:32

You have classification report

2:7:34

may be here and see that

2:7:36

one class performance,

2:7:38

F1 score. Forget about other.

2:7:39

Only look at the f1 score, it is 0%.

2:7:41

That means this model is performing very poorly for the diabetes loss.

2:7:45

So that's the inference that we can make out right now.

2:7:48

Okay. Over on, I hope absolutely everyone is clear.

2:7:51

Everybody is absolutely clear.

2:7:53

So precision, recall, X, X, Y score. That's the key level.

2:7:57

Okay, all of you, let me know.

2:8:00

Let me know.

2:8:02

All clear, everybody. What is precision?

2:8:05

What is recall? What is F1's four?

2:8:08

understood the idea of the dummy example, the takeaways, the medical data set that I took,

2:8:14

why accuracy is not good, why we should use something else, why confucian matrix, and most importantly,

2:8:20

why classification report.

2:8:22

Okay?

2:8:23

So this is a little mathematical that, but if you want to ignore that, you can.

2:8:28

Ultimately, you need to remember it's a formula.

2:8:30

I just went ahead here and just tried to explain the formula.

2:8:33

But again, you're important interpretation.

2:8:36

Interpretation, you have to know.

2:8:38

When you look at the classification report, you should understand that zero class, this is the performance, 1 class is the performance.

2:8:44

How well is the model performing for the 0 plus and how well is the model performing for the 1 plus?

2:8:49

So the performance aspect should be clear.

2:8:51

How well is the model performing for the 0 class and how well is the model performing for the 1 plus?

2:8:56

So that part should be very well.

2:9:08

Now, finally, we'll look at something called ROC, AUC.

2:9:21

ROC, AUC.

2:9:26

Yeah, we'll back in, so it will be a lot of concepts will be.

2:9:29

We're going to go back and use the same implementation.

2:9:35

So we've done cancer to do, on the decisionary and random forest, okay?

2:9:41

That we'll decision tree or random forest and then we'll do that classification report

2:9:45

and confucian matrix, all the thing will, okay?

2:9:48

We can see that.

2:9:50

So let us see that implementation.

2:9:52

Let us see that quick implementation here.

2:10:05

I will just go and copy this part from here.

2:10:11

This is the case study I will take up right now.

2:10:14

You have this.

2:10:15

You have this load cancer data.

2:10:21

So we had last week discussed what is the cancer data and

2:10:25

X med, Y, train test, plate we did.

2:10:31

All of you recall this.

2:10:32

This is the cancer data we did in the last session.

2:10:34

And all,

2:10:35

I'm trying to do is I'm trying to build two things.

2:10:38

I iteration one, we'll make decision tree

2:10:39

and interdation two,

2:10:41

we'll make a random forest and we'll compare

2:10:43

to them. What is our main learning from today?

2:10:45

If you're you looking, the main learning from today,

2:10:48

one part of the learning was

2:10:50

that we, we're decision free in basic model

2:10:54

we've explained. First, we've explained

2:10:55

that's the first part we talked about.

2:10:58

We went through the process of understanding

2:11:00

what is the decision free.

2:11:01

That's the thing that we looked at.

2:11:03

So if you remove all

2:11:05

the details of all that we talked about.

2:11:07

If we just go back and remove all those details

2:11:09

for a minute, we just talked about

2:11:11

the structure of a decision tree. That's it.

2:11:13

We've never said that's what I'm then we talked about

2:11:17

the concept of this particular hyperparameter.

2:11:20

I'm not saying if you don't control the depth of the tree.

2:11:23

If your depth grows, depth is the hyper parameter, right?

2:11:25

Maximum depth.

2:11:27

Depth can be one, depth can be two, depth can be three.

2:11:29

You can take different, different values of depth.

2:11:31

Or you have different, different values of depth change

2:11:33

and that depth is what we call the hyperparameter.

2:11:38

That's a perfect model

2:11:39

to make you.

2:11:40

If you don't limit the tree, if you allow the tree to grow too much, too deep,

2:11:47

so you'll do you will end up getting an overfit model.

2:11:50

95% training, 88% testing.

2:11:53

So it is going to be a overfit model.

2:11:55

But now the objective is to go back and,

2:11:58

objective is to go back and effectively

2:12:00

prune the text.

2:12:03

Prune the depth, you are trying to reduce the depth of the tree.

2:12:09

Now, depth to come to.

2:12:10

Jada come down, then it will be underfit.

2:12:12

So now we are trying to find what is the best fit model.

2:12:15

That's the idea.

2:12:15

So this is the concept that we talked about with respect to a decision fee.

2:12:19

Conceptually, that we're here here.

2:12:21

We have, we're at the first decision.

2:12:22

And then we said, okay, a single tree is not good.

2:12:25

So what if we take many, many, many such trees, many, many decision trees in a forest?

2:12:31

So we'll make, many, many trees of forest.

2:12:33

and with that, we will actually get an even better quality model.

2:12:37

So what he's the thing I'm here on here.

2:12:39

Okay?

2:12:40

So let us see.

2:12:41

Let me just go and do this thing.

2:12:45

I'm this to come up to make it little easy.

2:12:47

So that I want you guys to also do this with me.

2:12:50

So you guys to also do this with me.

2:12:51

So you're just, let me just open it up in collab.

2:13:03

Kunal has a question.

2:13:16

Kunal, I didn't understand your question actually.

2:13:19

If you, like, if you're in general questions about practice classes, if you want some guidance

2:13:24

or want to ask something, please ask me.

2:13:25

I am happy to help you.

2:13:27

Like, you want some help in how to study or what do you want?

2:13:30

Or is it something with to do with other classes?

2:13:33

So you can just maybe rephrase your question.

2:13:36

I can help you answer.

2:13:38

We also, we know here if there's any other general questions you have.

2:13:40

Yeah, yeah.

2:13:41

In the meantime, I can help you answer.

2:13:44

Okay.

2:13:44

In the meantime, I can go back to my collab.

2:13:56

Same thing, code, same to same to say, no problem.

2:14:00

Collab is always the best for the practice part because we have Jemini

2:14:03

our hands, we don't have to waste time on small things.

2:14:06

We have your cancer, we made a baseline

2:14:08

made. Okay.

2:14:09

So now we're what we're doing?

2:14:10

Uh, some things we have here

2:14:11

here we'll have here.

2:14:13

No need to do all this.

2:14:15

Okay.

2:14:15

So now that we know the concepts,

2:14:16

um, what can't do here on here.

2:14:18

I will simply go ahead and,

2:14:20

uh, I will simply go ahead and, I will simply go ahead and

2:14:24

and remove this part.

2:14:30

Remove this part.

2:14:33

Okay?

2:14:33

that's it. And this is how I will be model. Okay.

2:14:37

And here on here we have just Confucian matrix.

2:14:40

Add to thing.

2:14:42

Yeah, don't worry.

2:14:43

We have confusion matrix add here here.

2:14:48

And if you, if you write the code, uh,

2:14:50

Pritia of Germany will already guess, already guess, yeah, what you are about to type.

2:14:55

So we want to, so we have built a decision tree model.

2:14:58

Model can name had met underscore DP.

2:15:00

Med stands for medical, medical decision tree or, uh,

2:15:03

we have generated the predictions and we want to compare the tests with the

2:15:07

actuals or the app tests with the actuals and same way here we have built a random

2:15:11

for us we are expecting random for us to give a much better accuracy so I'm accuracy

2:15:15

we check karsakar but we are not doing that you're not just looking at the accuracy

2:15:19

I'm score be car saque you know model dot score also we can use but we are not doing that

2:15:24

we are only looking at the Confucian matrix and the classification report to compare

2:15:29

the quality of the model so iteration one hundred decision three

2:15:32

made or iteration two, we have a random forest made.

2:15:35

So here we have we can't confucian matrix code add

2:15:37

let us see we'll add the Confucian matrix code here also.

2:15:41

Jemini is smart enough to understand if I la one step in my Confucian matrix add

2:15:45

here, so most likely here also we'll be doing the same thing.

2:15:48

So let's run the code and you can see this is the result I'm getting.

2:15:53

And I think you can see a clear improvement, a clear improvement, okay?

2:15:57

So people are able to see a clear improvement what we are getting with a random forest.

2:16:01

A little bit more, you'll, you'll, you'll, you'll see a little improvement

2:16:04

is there, so overall accuracy also, also,

2:16:11

this is overall accuracy is, okay?

2:16:13

So this, I'm now I'm print and

2:16:15

this, I'm, I'm print and

2:16:17

what we are actually getting right now, guys.

2:16:20

So, uh, here we're print

2:16:21

here we're, okay, so you can't,

2:16:22

so you can't put a whole thing

2:16:23

so print, so print, testing accuracy,

2:16:27

beautiful, you know, so the results are coming very nicely to,

2:16:31

demo.

2:16:34

This is, you know, we don't need so much, too much of details.

2:16:40

We just need to print out the accuracy.

2:16:43

Just got it.

2:16:44

And then after, here, I will print out the test accuracy for random forest.

2:16:48

That's it.

2:16:48

Just before the, this, I will print out random forest test accuracy.

2:16:54

That's okay.

2:16:57

Okay, okay?

2:16:57

Okay, okay?

2:16:58

Okay, okay?

2:16:59

Okay, now.

2:17:00

Okay, is already guessing.

2:17:01

what I'm about to type.

2:17:01

Are you seeing by real time?

2:17:03

We're typing, and we're guessing,

2:17:03

we're guessing, that's going to,

2:17:04

okay, this is what,

2:17:05

sign, decision tree,

2:17:06

you did it,

2:17:07

so random course in the

2:17:07

that's why

2:17:09

Collab is a wonderful

2:17:10

environment.

2:17:10

Sometimes we're

2:17:11

sometimes we're in class

2:17:11

we're in

2:17:12

but this is a great

2:17:13

environment, okay?

2:17:14

You'll here

2:17:15

here here.

2:17:16

You will enjoy it

2:17:17

and I think

2:17:17

coding is a breeze here.

2:17:19

Okay?

2:17:21

And you can

2:17:21

see, guys,

2:17:22

this round off

2:17:23

so

2:17:24

we've the decision

2:17:24

made,

2:17:25

the test accuracy

2:17:26

is 94.

2:17:27

74.73

2:17:27

percent.

2:17:29

Learning number one,

2:17:30

we discussed.

2:17:31

tree-based model

2:17:31

is good,

2:17:32

it's good.

2:17:33

Logistics.

2:17:33

We can make

2:17:34

it.

2:17:35

So the accuracy

2:17:36

that's the accuracy

2:17:36

will be in the

2:17:37

decision tree

2:17:37

in a little

2:17:37

better

2:17:38

will be the

2:17:40

basic model

2:17:40

tree in

2:17:41

and

2:17:42

random forest

2:17:42

more better

2:17:43

are better.

2:17:44

99.

2:17:44

46.49%

2:17:45

brilliant.

2:17:47

Learning number two

2:17:48

was,

2:17:48

learning number two

2:17:49

was that

2:17:49

accuracy cannot be

2:17:51

trusted.

2:17:52

So what

2:17:52

we should

2:17:53

trust the

2:17:54

Confucian matrix.

2:17:54

We should trust a

2:17:55

confusion matrix.

2:17:55

We made

2:17:56

for tree for

2:17:57

and random forest

2:17:57

for us.

2:17:58

We made

2:17:59

two models for

2:17:59

two models for

2:17:59

we made and

2:18:00

both models

2:18:00

for we

2:18:01

made

2:18:01

classification

2:18:02

report

2:18:02

made.

2:18:03

There's

2:18:04

our learning

2:18:04

learning

2:18:04

what are

2:18:05

learning what is

2:18:06

false

2:18:08

negative

2:18:08

beautiful.

2:18:09

Decisionary

2:18:10

model

2:18:10

when we

2:18:10

made

2:18:11

false negative

2:18:11

three

2:18:12

there are

2:18:12

three

2:18:13

false

2:18:13

negatives I'm

2:18:14

getting

2:18:14

how many false

2:18:16

negatives I'm

2:18:17

getting on the data

2:18:17

three

2:18:17

I mean there are

2:18:18

total three

2:18:19

such cases

2:18:20

where model

2:18:21

predicted

2:18:22

you do not

2:18:23

have the

2:18:24

cancer

2:18:25

but actually

2:18:25

you do

2:18:26

which is

2:18:27

very dangerous

2:18:28

there are

2:18:30

three cases where model predicted you don't have cancer but actually you do.

2:18:34

But the moment you built a random forest, we're able to see there is one such case where

2:18:39

model predicted you don't have cancer but actually you do.

2:18:42

So we have managed to reduce our false negative.

2:18:44

So we are not trusting inaccuracy, but we have managed to reduce our false negative.

2:18:49

Number one, this learning number is.

2:18:52

The second thing is that if you're classification report

2:18:54

so we're our F1 score

2:18:56

two classes are born.

2:18:58

If you're a zero class or one class

2:19:00

look at you, as I told you,

2:19:01

this

2:19:02

all ignore, okay?

2:19:03

This everything. Just look at the F1

2:19:06

score. F1 score is like the class

2:19:08

level accuracy. If you're F1

2:19:10

score, look at zero class 93

2:19:12

1 class 96, this is

2:19:13

it's nothing wrong. But

2:19:15

remember comparative, can we make it

2:19:18

better? So when we take an ensemble of decision

2:19:21

tree, which is a stronger model, when you take

2:19:24

a collection of many decision trees, which is a stronger

2:19:26

model, you are able to get

2:19:27

a higher F1 score for zero.

2:19:30

class and a higher F1 score for one class.

2:19:33

Zero class,

2:19:33

95% are it.

2:19:35

One class's probably 97% of it.

2:19:37

We're getting a higher F1 score for zero plus also,

2:19:39

a higher F1 score for plus also.

2:19:41

That is what we're able to do.

2:19:43

Okay?

2:19:44

I hope everybody is clear right now.

2:19:45

So we're getting our overall end-to-end accuracy,

2:19:48

confusion matrix, FP, FN,

2:19:50

or F-1 score basis

2:19:52

we're able to beautifully interpret.

2:19:53

So going forward, key takeaway,

2:19:55

always look at F-1 score.

2:19:57

This is our binary for.

2:19:58

When you are,

2:19:58

when you're a binary for.

2:20:00

If you're going,

2:20:00

so the classes

2:20:02

will be,

2:20:02

that the classes will

2:20:03

create

2:20:03

we will see

2:20:04

that all the

2:20:05

classes are F1 score

2:20:06

is you'll be

2:20:07

able to

2:20:08

evaluate it that

2:20:08

way.

2:20:09

We'll be able

2:20:09

to see

2:20:09

that, okay,

2:20:10

class one

2:20:10

F1 score

2:20:11

it's,

2:20:11

you'll be able

2:20:13

to see that back

2:20:14

way.

2:20:14

So that's the

2:20:15

beautiful inference

2:20:16

you can go

2:20:16

back and do.

2:20:18

Okay?

2:20:18

And other

2:20:19

other learning was

2:20:20

that

2:20:20

what we're

2:20:20

here

2:20:21

remember,

2:20:22

it also has

2:20:23

something

2:20:23

called feature

2:20:24

importance.

2:20:24

We discussed

2:20:25

that already.

2:20:26

So feature

2:20:26

importance,

2:20:27

here we're

2:20:28

there we're

2:20:28

many things

2:20:29

are doing,

2:20:29

but

2:20:29

that's

2:20:30

that's

2:20:30

nothing

2:20:30

thing

2:20:30

you have

2:20:31

you have

2:20:31

model

2:20:32

made

2:20:34

RF

2:20:34

is nothing but

2:20:36

med underscore

2:20:37

RF

2:20:38

right at the

2:20:40

very end you

2:20:40

come and you

2:20:41

just

2:20:41

print out

2:20:42

this

2:20:43

dot

2:20:44

feature

2:20:45

importance is

2:20:46

that's it.

2:20:47

It's just

2:20:48

your feature

2:20:48

importance

2:20:49

are.

2:20:50

So all

2:20:50

features

2:20:51

individual

2:20:51

importance

2:20:52

values are

2:20:52

so code

2:20:53

actually one

2:20:54

line

2:20:54

but actually

2:20:55

you can't

2:20:55

you can't

2:20:56

see if you

2:20:56

see what

2:20:57

feature related

2:20:57

so

2:20:58

that's the

2:20:58

so that

2:20:59

we tried to create a data frame or data frame we wanted to show you which

2:21:05

feature is how much important and then we wanted to plot a bar chart to show you

2:21:09

that's the most important features

2:21:10

and this is important I hope everybody is aligned that this is important

2:21:15

because you have to understand that your model you've made which features are actually important

2:21:20

out of all the features, top five features

2:21:23

so interpretability

2:21:24

can are very good things.

2:21:25

So whatever we discussed broadly today starting with decision piece, so

2:21:29

from a, from a model interpretability perspective, it is very good.

2:21:33

So we're

2:21:33

what tree

2:21:34

we're seeing how are,

2:21:35

how's predictions

2:21:36

are

2:21:36

and most importantly

2:21:38

like which are the most important

2:21:41

predictors of the output that also

2:21:42

we're able to understand.

2:21:47

So

2:21:48

we're here

2:21:49

our last

2:21:50

example

2:21:51

so cancer we made

2:21:52

credit default

2:21:53

we can load that

2:21:54

data set also

2:21:55

we can't share

2:21:56

we can see that that's another very

2:21:58

we can see that's another very interesting

2:21:59

use case. So this was

2:22:01

today is 23rd April.

2:22:03

So 21st April, April

2:22:04

we've uploaded

2:22:04

that you see I credit card.

2:22:08

No, no,

2:22:08

UBRAG heat map we use

2:22:10

not usually

2:22:10

classification for

2:22:11

heat map is usually for

2:22:13

regression.

2:22:14

So correlation heat map is

2:22:15

only for regression.

2:22:16

So heat map, we're actually

2:22:18

here up, you have to

2:22:18

see what you've seen.

2:22:19

But if you've

2:22:19

if you've made,

2:22:20

but if you've done

2:22:20

that is only for regression

2:22:23

because heat map is used

2:22:24

to find out

2:22:25

the

2:22:26

the relationship between two

2:22:29

numerical variables.

2:22:30

Categories

2:22:31

in which

2:22:31

it's in

2:22:33

input and output

2:22:33

that's not

2:22:34

I hope

2:22:36

I'm able to

2:22:36

explain to you.

2:22:39

No, no, no,

2:22:41

no,

2:22:41

no,

2:22:41

but even,

2:22:41

not,

2:22:42

important feature

2:22:43

is that

2:22:44

you're trying to

2:22:45

find important

2:22:46

feature

2:22:46

is what is.

2:22:48

You are trying to

2:22:48

find out which are the

2:22:50

important

2:22:50

features for predicting

2:22:51

the output.

2:22:53

I mean,

2:22:53

you have

2:22:53

you have to

2:22:53

create

2:22:54

input and output

2:22:55

in the input and output

2:22:55

in.

2:22:57

So that

2:22:57

actually is wrong.

2:22:58

We're not.

2:22:59

You can

2:22:59

some code

2:22:59

and you can

2:23:00

you can

2:23:00

you

2:23:01

can't,

2:23:01

you know,

2:23:02

like,

2:23:02

that's

2:23:02

there's

2:23:03

not,

2:23:04

if you want,

2:23:05

we'll

2:23:05

we'll

2:23:05

make you

2:23:06

here

2:23:06

here.

2:23:07

You know,

2:23:08

but I'm

2:23:09

telling you that is

2:23:10

wrong,

2:23:10

that is not the

2:23:10

right way to

2:23:11

do it.

2:23:12

See,

2:23:12

this is your

2:23:12

data is,

2:23:13

you're saying

2:23:14

is fine.

2:23:15

You're

2:23:16

what you're

2:23:16

doing?

2:23:17

What you're,

2:23:17

your data frame

2:23:18

is,

2:23:18

okay?

2:23:20

What Ubraj

2:23:20

is saying is

2:23:21

that,

2:23:21

that,

2:23:21

sir,

2:23:21

DF students

2:23:22

do we have

2:23:22

DF students

2:23:25

do

2:23:25

DF students

2:23:25

do

2:23:26

core

2:23:27

we're

2:23:28

okay,

2:23:28

these two of us

2:23:29

in Germany

2:23:30

but

2:23:30

whatever I'm

2:23:31

typing the

2:23:31

code

2:23:31

I think

2:23:32

heat map is

2:23:33

not imported

2:23:33

so we will

2:23:34

do

2:23:34

SMS

2:23:35

dot heat map

2:23:35

or

2:23:36

you are not

2:23:37

equal to

2:23:37

true

2:23:37

okay

2:23:39

okay

2:23:39

done

2:23:40

right

2:23:41

S&S is not

2:23:42

imported

2:23:42

IP is

2:23:42

okay

2:23:42

S&S is

2:23:44

import

2:23:44

okay

2:23:44

but what I'm

2:23:46

getting at

2:23:46

is this is

2:23:47

not

2:23:47

the right

2:23:49

approach you know

2:23:50

because

2:23:50

because

2:23:51

this is not the

2:23:52

number

2:23:52

not

2:23:52

this is not a

2:23:54

pass or fail is not a numeric variable

2:23:55

right

2:23:55

make sense

2:23:56

or in

2:23:58

last

2:23:59

practice is

2:23:59

oh okay

2:24:00

okay

2:24:00

no no problem

2:24:01

but I'm saying

2:24:02

that this is not

2:24:03

a numeric feature

2:24:03

that's the reason

2:24:04

actually

2:24:04

yeah

2:24:05

sometimes

2:24:06

your value

2:24:06

same

2:24:06

hajah

2:24:07

time

2:24:07

I think

2:24:08

intuitively it might

2:24:09

come out to be the same

2:24:09

but

2:24:10

you should never

2:24:11

treat

2:24:11

this pass and

2:24:12

fail like a number

2:24:12

just to

2:24:13

clarify

2:24:13

you will

2:24:14

intuitively get the same

2:24:15

answer

2:24:15

sometimes

2:24:15

but this is not

2:24:17

the right way

2:24:17

to

2:24:17

see the

2:24:18

relationship

2:24:18

okay

2:24:22

Here you look,

2:24:22

intuitively

2:24:23

answers

2:24:23

that's

2:24:24

you're here

2:24:24

here on

2:24:25

that's

2:24:25

that's

2:24:25

but he's

2:24:26

but he's

2:24:26

mathematically

2:24:26

what he's

2:24:27

what he's

2:24:28

doing what

2:24:28

is

2:24:29

how he's

2:24:29

what he's

2:24:29

is

2:24:30

finding out

2:24:31

the relationship

2:24:31

between

2:24:32

X and Y

2:24:32

what is

2:24:33

they're

2:24:34

and they're

2:24:34

and

2:24:35

they're

2:24:35

and

2:24:35

Python is dumb right

2:24:36

and

2:24:37

Python is

2:24:37

number

2:24:38

right?

2:24:38

Because if you

2:24:39

if you

2:24:41

this data frame

2:24:42

look that is

2:24:42

actually not a

2:24:43

number

2:24:43

that is actually not a

2:24:43

category

2:24:43

so

2:24:44

so the heatmap

2:24:45

idea is

2:24:46

incorrect in this

2:24:46

so

2:24:47

so that we

2:24:48

we do we

2:24:48

we do

2:24:49

we feature

2:24:50

importance

2:24:51

we feature importance

2:24:51

We feature

2:24:52

importance

2:24:52

is a

2:24:52

different thing

2:24:53

is

2:24:53

its mathematics

2:24:54

completely

2:24:55

are

2:24:55

so mathematical

2:24:56

layer is very

2:24:57

different

2:24:57

so we're

2:24:58

not going to

2:24:58

that's the

2:25:00

machine learning

2:25:01

math but in case you're

2:25:02

wondering

2:25:02

that sir

2:25:02

this is

2:25:03

this is

2:25:04

what we're

2:25:04

we're

2:25:05

we're

2:25:05

we're

2:25:06

we're

2:25:07

not correlation

2:25:07

and no

2:25:08

just to

2:25:09

clarify you

2:25:10

if

2:25:10

if you're actually

2:25:10

if you're

2:25:11

if you're

2:25:11

if you're

2:25:12

if you're

2:25:12

if you're

2:25:14

that this feature

2:25:14

importance

2:25:14

point 740 is it

2:25:15

is it correlation

2:25:16

it is not

2:25:17

because our

2:25:17

correlation

2:25:17

078

2:25:18

remember

2:25:19

this is a

2:25:20

another thing is

2:25:21

straight

2:25:21

directly

2:25:21

make

2:25:21

okay

2:25:22

I hope that

2:25:22

makes

2:25:23

sense.

2:25:25

Yeah,

2:25:25

regression

2:25:25

makes sense

2:25:26

you're right.

2:25:27

Regression

2:25:27

in

2:25:27

we're right.

2:25:28

Regression in

2:25:28

we're

2:25:29

okay.

2:25:33

So I have

2:25:34

uploaded this

2:25:34

data set here

2:25:35

for everybody

2:25:35

is a very good

2:25:38

question.

2:25:39

So 24th

2:25:40

23

2:25:40

apron

2:25:41

there's here

2:25:41

we're here

2:25:41

we're not.

2:25:42

We'll

2:25:43

we'll

2:25:43

we'll

2:25:43

we'll

2:25:43

give

2:25:43

then

2:25:44

this is simple

2:25:45

that we

2:25:45

we just

2:25:45

we just

2:25:45

we just

2:25:46

we can do

2:25:46

so

2:25:48

so

2:25:51

So whatever we did, whatever we talked about, so credit card

2:25:54

data set, we can actually go and do this.

2:26:01

What is that?

2:26:04

Could you know?

2:26:06

No, so suasini, see, my thing is that

2:26:08

don't, don't burden yourself.

2:26:10

Don't burden yourself too much.

2:26:14

Don't burden yourself too many things.

2:26:16

Whatever I'm talking about,

2:26:17

the detail at which I'm discussing, that is more than enough.

2:26:21

Too many topics is not read.

2:26:23

Whatever content I'm sharing is more than enough.

2:26:26

There are many books, there are many references, there are many articles, I can suggest to you.

2:26:31

But the whole objective of this boot camp is to ensure that you are comfortably able to face with the program.

2:26:36

The program, the curriculum and the content we have and what we are doing in the classes is more than enough for the practical perspective.

2:26:43

Now, Auehya, absolutely what you're right is there.

2:26:46

That is their key references on ML.

2:26:49

That depends on the amount of time.

2:26:51

that you have. If you have enough time available, then certainly there are books you can read.

2:26:55

There are other that you can go to. But sometimes, you know, it can also overwhelm you. If you do too

2:27:00

much, it can overwhelm you because you will also have a lot of other work you're doing in the day.

2:27:04

And then it might actually demotivate you, I was not able to achieve this. I'm parnipa.

2:27:11

So that's why I say, guys, just relax, come to the classes with an empty mind.

2:27:16

Two and half hours, you know, make it a time well spent, feel confident, feel motivated.

2:27:21

So, what things we're sharing, what we're sharing, what things we're doing,

2:27:24

that's the way, you go to implement for.

2:27:26

Isn't it?

2:27:27

Our resources, you go, you know, you're going to Kagle, I go,

2:27:29

you're two similar problems solve.

2:27:31

That's it.

2:27:31

That is my resource.

2:27:32

I will not ask you to go to YouTube because there's too much of useless people sitting there

2:27:36

talking about bunch of useless stuff.

2:27:38

So don't go to YouTube and listen to all that nonsense.

2:27:41

So that is one thing.

2:27:42

Don't go to Google.

2:27:43

Don't go to any of the website.

2:27:45

Because a half-a-a-a-i-genrated content there.

2:27:48

Right?

2:27:48

So mostly it is all this.

2:27:49

So don't get into.

2:27:50

Don't try.

2:27:51

to, you know, burden yourself with too much of topics and too much of content what you're

2:27:55

hearing around.

2:27:56

But just stick to what we are discussing.

2:27:57

Stick to what we are discussing here.

2:28:00

As, Anki, that comes with practice.

2:28:02

To be honest with you,

2:28:03

there's a bit more practice from, if you'll ask you, you would have seen,

2:28:06

that we're just type are.

2:28:07

But if you ask me, is it required?

2:28:09

Maybe it's not.

2:28:10

It's not.

2:28:11

It's a process.

2:28:12

It's a practice.

2:28:13

It's a practice in a way.

2:28:14

Do you have you?

2:28:16

Do you have to remember?

2:28:17

Who is asking you to remember the syntax?

2:28:18

Who is asking you to remember memorized syntax?

2:28:21

Nobody is encouraging you to memorize syntax.

2:28:23

Nobody.

2:28:25

Syntaxes are you for you memorize them.

2:28:27

Right?

2:28:28

You know?

2:28:30

Yeah. Yeah.

2:28:30

Ah, you should know that.

2:28:30

See, if you're going,

2:28:31

that, see, if you're going, sir,

2:28:32

correlation, what is?

2:28:33

Something should come directly.

2:28:35

You have got to start.

2:28:36

Correlation is dot-con.

2:28:38

You should know,

2:28:39

that, yeah, this is how to be,

2:28:40

this is, it.

2:28:41

This is.

2:28:42

But you don't have to memorize the syntax,

2:28:44

okay?

2:28:47

See, and the brain has a

2:28:49

wonderful ability to,

2:28:51

adapt.

2:28:51

It will be over time it will come.

2:28:53

You have to be confident about yourself.

2:28:55

You over time,

2:28:56

are you know,

2:28:58

you know,

2:28:58

you know,

2:28:59

writing the code in collab is different

2:29:02

from going to Germany

2:29:03

and copy-pesting everything.

2:29:04

That's,

2:29:05

that's not going

2:29:05

much learning me

2:29:06

is.

2:29:07

I know, I know some,

2:29:08

a lot of people

2:29:09

who, what will,

2:29:10

the problem statement

2:29:11

take,

2:29:11

they'll go to Germany,

2:29:12

take the whole code

2:29:13

and that's it's a runness

2:29:14

all for.

2:29:14

That is useless.

2:29:16

That is useless.

2:29:17

That is useless.

2:29:17

Yeah.

2:29:17

If you're approaching

2:29:19

the problem,

2:29:20

then it's fine.

2:29:21

Use my templates.

2:29:21

That's why I'm sharing the templates with you.

2:29:23

Our template use code.

2:29:24

So now,

2:29:26

and it's a process.

2:29:29

It's a process.

2:29:30

I mean, again, see,

2:29:31

machine learning,

2:29:31

this is something that we are getting started.

2:29:33

It's a process.

2:29:33

Many of you might be doing this for the first time.

2:29:35

It's a process where you have to,

2:29:37

you know,

2:29:37

feel confident in time.

2:29:38

It's like.

2:29:40

Okay.

2:29:43

So now,

2:29:44

moving on.

2:29:46

Kunal,

2:29:46

you've asked a question,

2:29:47

I'll come to that as again,

2:29:49

a bit of a different one.

2:29:50

I'll,

2:29:51

Just stay back.

2:29:51

I'll take up your question to Rathik.

2:29:53

I'll take up your question also.

2:29:54

So now, moving on,

2:29:57

UCI credit card,

2:29:58

let's,

2:29:58

we already solved here last time.

2:30:00

So I will not ask you to again do it.

2:30:02

So this we already discussed last time.

2:30:04

So Hulka's from us, we'll tell us this.

2:30:07

So we will take the UCI predict card data set.

2:30:11

So what I will do,

2:30:12

I will take demo.

2:30:14

And I will do PD.

2:30:16

Read and, this is CSB.

2:30:21

And I will just quickly

2:30:23

load the UCI credit card.

2:30:27

T.S.B.

2:30:28

Now, look, this is what I made.

2:30:31

Now,

2:30:31

look,

2:30:32

this is auto-complete

2:30:33

is.

2:30:34

But it's the

2:30:34

mean,

2:30:35

do I not know the syntax?

2:30:37

I know the syntax.

2:30:38

But we have to do

2:30:39

not do the syntax.

2:30:39

What is more important is

2:30:42

what is more important is

2:30:42

that the Gemini

2:30:43

generate is,

2:30:45

if you see this,

2:30:47

that you

2:30:47

see this, you

2:30:47

see,

2:30:48

if you tell me

2:30:49

that, sir,

2:30:50

we're

2:30:50

that's the problem

2:30:52

now you are,

2:30:53

now you

2:30:53

say,

2:30:54

you say, sir,

2:30:54

what is,

2:30:55

what is an issue,

2:30:56

then it's an issue,

2:30:56

then it's a problem.

2:30:57

If you can,

2:30:58

pandas,

2:30:58

you've

2:30:58

got,

2:31:00

it's a

2:31:00

so much

2:31:01

you know,

2:31:01

it's a thing

2:31:02

what might be

2:31:04

happening.

2:31:05

But it's okay.

2:31:07

If you, let's say,

2:31:07

display method,

2:31:08

you know,

2:31:08

you know,

2:31:08

maybe you might

2:31:09

have been

2:31:09

that's okay.

2:31:10

So absolutely

2:31:12

it's true.

2:31:12

So absolutely

2:31:12

it feels free to

2:31:13

use auto

2:31:13

compute.

2:31:14

It's there

2:31:14

no problem

2:31:15

is.

2:31:16

In fact, in

2:31:17

today's world,

2:31:17

if you are writing

2:31:18

from scratch,

2:31:19

it's a problem,

2:31:20

you have to

2:31:22

change with the times.

2:31:23

Right.

2:31:23

Nobody will,

2:31:23

I'll ask you to

2:31:24

memorize these kind of

2:31:25

things.

2:31:25

Okay,

2:31:26

actually.

2:31:26

So now,

2:31:28

pt.

2:31:29

reed cc.

2:31:30

This is our

2:31:30

data set.

2:31:31

So,

2:31:32

first we're

2:31:32

we're trying

2:31:33

train test

2:31:33

we're same way.

2:31:35

Okay.

2:31:35

So let me go

2:31:36

and take the data.

2:31:39

and we will split

2:31:40

demo,

2:31:40

data frame

2:31:43

into train and test.

2:31:47

okay?

2:31:47

let's do that.

2:31:48

this.

2:31:48

this train test

2:31:50

will go

2:31:51

it will

2:31:51

it will do the whole thing.

2:31:54

I think it will do the whole thing.

2:31:54

I think it will do the whole thing.

2:31:56

the train test fit

2:31:56

this whole.

2:31:58

Okay.

2:31:58

This he'll be

2:31:59

over on.

2:32:00

Okay.

2:32:00

Anyways, I can test

2:32:01

take the initial code from here.

2:32:03

Okay.

2:32:06

You already did this part to some extent.

2:32:08

Let me take this part.

2:32:10

The whole thing.

2:32:16

You can say, what is your X?

2:32:19

What is your Y?

2:32:20

You can specify your X and Y.

2:32:22

Or remember, I think we also dropped some other columns, right?

2:32:25

I forgot to do that.

2:32:26

that actually.

2:32:27

So I'm a demo dot dropped the other.

2:32:28

I think last time we dropped some columns right.

2:32:31

We got dropped ID.

2:32:33

Then we dropped sex, education.

2:32:42

Education or marriage.

2:32:46

So ID, sex, education, marriage.

2:32:48

I mean, these are all columns dropped here.

2:32:51

Okay.

2:32:52

And access is equal to one.

2:32:54

Tax is equal to one means I'm dropping along.

2:32:56

the columns and that's it.

2:33:01

This is my final data frame that we have right now.

2:33:03

We already talked about this in the last class, right?

2:33:05

A again, we're what?

2:33:06

X will be demo dot drop.

2:33:13

default payment next month.

2:33:16

Yeah, we're just trying to do it again so that you build that.

2:33:19

You know, you're feeling confident about the flow.

2:33:22

So here we drop.

2:33:23

The other features are part of my X.

2:33:25

And this is.

2:33:26

part of my Y.

2:33:27

Okay, this is our X or its Y.

2:33:28

So that's it.

2:33:29

Simple.

2:33:30

Okay.

2:33:31

And now what I will do?

2:33:32

Now I will simply go into the train test.

2:33:35

Now I will simply go and to the train test split.

2:33:39

Okay.

2:33:42

Yeah, so you're either you do it and do it as a say you can.

2:33:44

Or then if you don't want to do any of this,

2:33:47

you, you open to side in.

2:33:48

That's it.

2:33:49

Data we set up.

2:33:50

We're going to do it.

2:33:51

We've got to do it.

2:33:51

Jemini open up.

2:33:52

We have.

2:33:53

And now just go and type.

2:33:56

So split the data into X-Train, Y-Train.

2:34:02

You're here here to the variables too, the variables too,

2:34:05

or maybe what kind of what kind of what kind of what kind of what kind of explanation for

2:34:08

other other variables here.

2:34:11

Here you're made RF, here here here X-Train M, X-Test-M,

2:34:14

X. So it's a little confusing

2:34:15

is right.

2:34:17

So this becomes a little confusing at times, right?

2:34:20

So that is the idea.

2:34:23

So now, split the data into.

2:34:26

X-rain, Y, X test, Y test, and build logistic regression model, build, logistic regression model,

2:34:34

build logistic regression model, build logistic regression model, and find accuracy and confusion accuracy and confusion matrix and classification report.

2:34:54

Compare with decision P.

2:34:55

So first we'll do it.

2:34:57

And you're here here.

2:34:58

You look, you know, you're learning, what will.

2:35:00

This is exactly the thing that we discussed in our session.

2:35:05

This code here here out will.

2:35:06

And you can see, here here, this is multiple cells I add to.

2:35:10

No, no, no.

2:35:11

Let's accept and run.

2:35:15

So very interesting.

2:35:18

Let me show you right now.

2:35:20

We, this, okay, leave, leave, we have to do it.

2:35:22

So don't worry about this right now.

2:35:24

If you show you.

2:35:25

this is what I wanted to show you.

2:35:33

Now, look, logistic been here.

2:35:34

Same data set.

2:35:35

So, sometimes, here here data, I'm just, it's not, it's not,

2:35:39

it's not comment so you're like, you're like, as if the code is very complex.

2:35:42

The code is not actually.

2:35:43

So I'll remove all this.

2:35:44

Let me just go and remove all this.

2:35:46

This is a very simple piece of code.

2:35:48

But the comments are too much.

2:35:49

So that's why the code looks very long.

2:35:52

Let me do, let me remove all this.

2:35:54

and let me build the model.

2:35:56

Okay.

2:35:57

Apply the way, we'll look at it.

2:35:59

Now, look, now, look,

2:36:01

and finally,

2:36:02

this our predictions are.

2:36:03

You can't see,

2:36:04

dot fit,

2:36:06

dot predict,

2:36:06

it's our full flow.

2:36:07

This is the entire flow.

2:36:09

Dot predict what we,

2:36:10

we're doing, dot score

2:36:10

and dot score.

2:36:11

And dot score be simple.

2:36:15

Here here too much,

2:36:16

a lot code leaked

2:36:17

so we here we here

2:36:17

here only test accuracy

2:36:18

we'll take out.

2:36:19

That's it.

2:36:20

This is our score

2:36:20

and here our logistic regression,

2:36:23

classification report.

2:36:24

So, classification report, what will?

2:36:26

This will.

2:36:27

And Confucian matrix,

2:36:27

what will?

2:36:28

That's it.

2:36:29

This is the simple way how we can do this.

2:36:31

This is a whole thing

2:36:32

in a cell in.

2:36:33

It's not going to do.

2:36:35

So,

2:36:35

so many,

2:36:35

so many,

2:36:36

it's a lot of

2:36:37

things, you know?

2:36:38

This is all the

2:36:38

line in one line

2:36:39

is the important

2:36:41

learning.

2:36:42

This is actually

2:36:43

the whole class's

2:36:43

takeaway.

2:36:44

You know,

2:36:44

this, the credit

2:36:47

data set that we did

2:36:48

last session.

2:36:49

Okay, so

2:36:50

we here here

2:36:50

test,

2:36:50

train accuracy,

2:36:51

print,

2:36:52

okay?

2:36:52

So test,

2:36:53

you can only,

2:36:53

then train be printed.

2:36:54

So train accuracy, we printed

2:36:57

right, right?

2:36:59

The train accuracy

2:37:00

we print

2:37:00

and there goes the train accuracy.

2:37:03

And now this is the

2:37:04

important learning from the

2:37:05

class.

2:37:06

So accuracy is very high.

2:37:08

If accuracy

2:37:08

if you go to,

2:37:09

it's, you know,

2:37:10

it's basically like a

2:37:11

good fit model.

2:37:14

But actually it's not.

2:37:15

Look at the column.

2:37:17

Look at the F1's code.

2:37:18

That's the key takeaway.

2:37:19

This was a real world use case

2:37:20

we did last session,

2:37:20

right?

2:37:21

Updick sector,

2:37:22

credit defaults data statement.

2:37:23

There are 30,000.

2:37:24

customers,

2:37:24

Abdek satio,

2:37:25

accuracy is 78%

2:37:26

but my model is performing

2:37:28

very poorly for the

2:37:30

one class.

2:37:30

One class

2:37:31

must have default

2:37:32

class.

2:37:32

So for the default

2:37:33

class particularly,

2:37:35

my model has performed

2:37:36

very poorly.

2:37:36

My model is unable

2:37:37

to classify defaulters.

2:37:39

Or if you

2:37:40

look at the column,

2:37:41

Abdeiqsatio,

2:37:42

that this entire column

2:37:43

is zero.

2:37:44

There are no

2:37:45

default predictions

2:37:46

my model is doing.

2:37:47

My model is only doing

2:37:48

not default predictions.

2:37:50

My model is not doing

2:37:51

any default predictions.

2:37:52

That's the other inference

2:37:53

we are able to make right off.

2:37:55

Okay?

2:37:56

Now,

2:37:56

now we're going.

2:37:57

Same thing

2:37:58

we'll decision tree

2:37:59

make.

2:38:00

So this is the

2:38:00

iterative way

2:38:01

how we do

2:38:01

machine running.

2:38:03

Now we know

2:38:03

the whole thing,

2:38:04

right?

2:38:04

Now we know the whole thing, right?

2:38:04

Now we have

2:38:04

iteratively

2:38:04

same to same.

2:38:06

Nothing will change

2:38:07

in the code.

2:38:08

We'll just

2:38:08

logistic

2:38:08

just a decision tree

2:38:09

to make it.

2:38:10

This is exactly

2:38:11

how we iterate and we check.

2:38:14

This is your

2:38:14

maximum depth

2:38:15

here.

2:38:16

We've discussed

2:38:17

maximum depth already.

2:38:18

You know,

2:38:18

for example,

2:38:19

three value.

2:38:20

Okay.

2:38:21

We'll just

2:38:21

we'll make.

2:38:22

And you can see

2:38:23

Comparatively, this is a better quality model.

2:38:26

Look at this, guys.

2:38:26

Accuracy

2:38:27

and F-144

2:38:28

1 plus has been

2:38:29

this is a better quality

2:38:31

model incrementally

2:38:32

than what we had before.

2:38:34

This is

2:38:34

we're trying to

2:38:35

and here

2:38:36

here you can

2:38:36

beautifully check

2:38:37

can't,

2:38:38

if you

2:38:38

if you've

2:38:38

decisionity

2:38:39

depth 1

2:38:39

so 1 is not a good

2:38:41

model,

2:38:42

it will

2:38:42

this underfit

2:38:43

and you

2:38:44

and if you

2:38:44

if you're

2:38:45

overfitted

2:38:46

So, so both are

2:38:48

and this is

2:38:49

and this is bad.

2:38:50

You're letting the tree grow

2:38:53

too much.

2:38:54

You're not putting any

2:38:55

controls on the tree.

2:38:56

Too many questions.

2:38:57

So model overfitt

2:38:58

got overfitt

2:38:58

okay,

2:38:59

this is bad.

2:39:00

This is bad.

2:39:01

So you have to find out

2:39:02

somewhere like an optimal

2:39:04

tip.

2:39:04

And it's kind of

2:39:05

there's kind of learning number two

2:39:07

and finally

2:39:08

what was the last thing?

2:39:09

The last thing

2:39:10

we talked about was

2:39:11

random forest.

2:39:13

So code

2:39:13

what is?

2:39:13

Code is just

2:39:15

only cell.

2:39:15

Goad.

2:39:16

Go ahead.

2:39:16

plot,

2:39:17

this formating

2:39:18

and your code

2:39:19

bar

2:39:19

but actually the

2:39:20

template is

2:39:21

just this only.

2:39:22

That's why I wanted

2:39:22

to do this

2:39:23

in front of you

2:39:23

so I just wanted to

2:39:24

make you feel

2:39:25

a bit

2:39:25

confident.

2:39:26

So random forest

2:39:27

and random forest.

2:39:28

And random forest's

2:39:29

hyper parameter

2:39:29

is an

2:39:30

estimators,

2:39:30

right?

2:39:31

N estimators

2:39:32

equal to

2:39:32

100.

2:39:33

I'll just take

2:39:34

a default

2:39:34

estimators,

2:39:35

build the model.

2:39:36

Same to same.

2:39:37

I'm only changing

2:39:38

the algorithm

2:39:38

and

2:39:40

you can see

2:39:42

what we are getting.

2:39:43

Yeah,

2:39:43

URAs, that's a good

2:39:44

question.

2:39:44

You can use

2:39:45

can use.

2:39:46

Actually it's a good

2:39:46

use case.

2:39:47

Here on the imbalance

2:39:48

there's a little

2:39:48

so you can use

2:39:50

use it

2:39:50

you can.

2:39:51

You first smote

2:39:51

then then

2:39:52

you can

2:39:52

you can do it.

2:39:53

So it's a

2:39:53

incremental

2:39:54

improvement

2:39:54

you'll

2:39:54

get a very

2:39:55

good

2:39:55

point that you

2:39:56

raise.

2:39:56

So if you

2:39:57

apply smote

2:39:57

and if you do

2:39:58

this,

2:39:58

you will

2:39:58

actually get an

2:39:59

improvement.

2:40:00

Okay?

2:40:01

And you can

2:40:01

see guys

2:40:02

we are getting

2:40:03

this code

2:40:04

tweak

2:40:04

you have to tweak

2:40:05

the model

2:40:06

and if you

2:40:06

tweak the model

2:40:07

you will get a

2:40:07

better

2:40:07

performance.

2:40:09

So generally

2:40:09

randomly random

2:40:10

forest will

2:40:10

give you

2:40:11

better accuracy

2:40:12

than

2:40:12

decision piece.

2:40:15

Okay, so

2:40:15

this is the

2:40:15

so

2:40:16

Confucian matrix and F1 score.

2:40:19

F1 score is like our new accuracy.

2:40:21

Go ahead

2:40:21

go any

2:40:22

any of you ask

2:40:23

how is the model

2:40:24

performing

2:40:24

and you will use

2:40:25

F1 score.

2:40:26

And coming to

2:40:26

UBra's question,

2:40:27

why did

2:40:27

Yuvrage

2:40:28

mentioned

2:40:28

class imbalance?

2:40:29

Why is

2:40:29

UBrash

2:40:30

talking about

2:40:30

class imbalance?

2:40:31

Because

2:40:31

see, support.

2:40:32

support

2:40:32

means what

2:40:33

is?

2:40:34

Support

2:40:34

means how many

2:40:35

records do we

2:40:36

have?

2:40:37

So how many

2:40:38

number of

2:40:38

zeros do we have

2:40:39

and how many

2:40:40

number of

2:40:41

ones do we have?

2:40:41

In the

2:40:42

whole data

2:40:42

set how many

2:40:43

zeros do we

2:40:43

have,

2:40:44

how many ones to be?

2:40:45

That is the

2:40:45

intuition

2:40:46

behind support.

2:40:46

So,

2:40:48

the whole data

2:40:48

out of total

2:40:50

6,000 rows of

2:40:51

data that we have

2:40:52

right now,

2:40:53

you're able to

2:40:53

see there

2:40:53

are total

2:40:54

4, 6, 8,

2:40:54

7,

2:40:55

0s and there

2:40:56

are

2:40:56

13, 13,

2:40:57

1s.

2:40:58

So overall

2:40:58

data

2:40:58

in it's

2:40:59

there,

2:41:00

it's

2:41:00

ones

2:41:00

and so

2:41:02

support is

2:41:03

telling you

2:41:03

how many

2:41:03

actual

2:41:04

number of

2:41:04

records we

2:41:05

have

2:41:05

right now.

2:41:06

So this is

2:41:06

what is

2:41:08

meant by

2:41:08

class

2:41:08

in balance.

2:41:09

We have

2:41:09

discussed

2:41:09

class

2:41:09

imbalance before

2:41:10

and if you

2:41:11

remember

2:41:12

sometimes

2:41:13

class imbalance

2:41:14

also plays a role.

2:41:16

Sometimes

2:41:16

this particular class imbalance also plays a role in the overall aspect of your, you know,

2:41:22

aspect of your, you know, your accuracy, your performance, your performance.

2:41:28

Because we have a lot of examples of class zero, but very few examples of class one.

2:41:34

Because class one's examples

2:41:35

very common. When you end up building a model, the model does not seem to perform that well on

2:41:41

class one.

2:41:42

This go, this go overcome

2:41:43

kind of smote use.

2:41:45

So if you're smart use.

2:41:46

and make it's a whole better process.

2:41:49

This all you can.

2:41:51

Like, like for example,

2:41:52

now we have iteration

2:41:53

what did?

2:41:54

Now we have logistic,

2:41:55

decision free,

2:41:56

and random forested.

2:41:57

We've only

2:41:57

algorithms changed and

2:41:59

do you're saying

2:42:01

smart.

2:42:01

Now you're saying smart.

2:42:01

Now you're saying smart.

2:42:01

Now, look,

2:42:01

you're just

2:42:02

there's just

2:42:02

there's just

2:42:03

bad.

2:42:04

Okay?

2:42:05

So you can what

2:42:05

can you?

2:42:06

Very simple.

2:42:07

You generate

2:42:08

and you can say

2:42:09

now

2:42:10

just like the

2:42:13

previous cell

2:42:16

where I did

2:42:17

logistic regression

2:42:20

please

2:42:23

generate a

2:42:26

pipeline

2:42:27

using

2:42:30

smote plus

2:42:32

we'll make pipeline

2:42:33

we're playing.

2:42:34

First we we'd

2:42:34

we'd say

2:42:35

we'd say

2:42:37

smote plus something.

2:42:38

That's it.

2:42:39

This is our pipeline

2:42:39

would.

2:42:40

Smort means

2:42:41

oversampling.

2:42:42

We have got very

2:42:43

less number of examples

2:42:44

of defaulters.

2:42:45

Right?

2:42:46

So you

2:42:46

artificially

2:42:47

de falters

2:42:47

increase

2:42:48

and then

2:42:48

model

2:42:49

will be

2:42:49

you can do that.

2:42:50

We can

2:42:50

we can

2:42:50

we're just

2:42:52

as an example.

2:42:53

So smooth

2:42:54

plus

2:42:54

logistic regression

2:42:55

and

2:42:55

and

2:42:57

keep the

2:42:59

rest of

2:43:02

the

2:43:02

ideas

2:43:04

exactly similar

2:43:07

to

2:43:07

the

2:43:10

cell.

2:43:12

So we can

2:43:13

we make,

2:43:13

do all this.

2:43:13

We do all

2:43:15

this in one sale.

2:43:20

So let's see.

2:43:22

So this smote's

2:43:22

we are

2:43:24

expecting that once we use a smote

2:43:25

our

2:43:26

our F1 score is

2:43:27

a little

2:43:28

improvement

2:43:28

so we'll tweak

2:43:29

if it

2:43:29

doesn't

2:43:31

make it.

2:43:32

But you can

2:43:32

see the code is

2:43:33

very simple.

2:43:34

Pipeline

2:43:34

is the first

2:43:34

smote

2:43:35

smote.

2:43:35

Smot A

2:43:36

meant

2:43:36

synthetic

2:43:37

minority

2:43:37

oversampling

2:43:38

technique.

2:43:39

It's called

2:43:39

synthetic

2:43:40

minority

2:43:40

oversampling

2:43:41

technique.

2:43:41

You see the top

2:43:42

pop up up

2:43:43

are you.

2:43:43

Over sampling

2:43:44

means if you have

2:43:45

less number of examples of a particular class,

2:43:48

we can synthetically

2:43:48

us

2:43:49

can't make that is what

2:43:50

Smote

2:43:50

basically stands for.

2:43:52

The same to same is

2:43:53

a pipeline

2:43:54

ban down,

2:43:54

dot fit

2:43:54

predictions

2:43:55

predictions

2:43:55

and accuracy

2:43:57

make out

2:43:57

confucianmatic

2:43:58

classification

2:43:58

report

2:43:59

nothing changes

2:44:00

same to same

2:44:01

thing is

2:44:01

nothing

2:44:02

we're

2:44:03

we're

2:44:03

we're

2:44:03

comparatively

2:44:04

analyze

2:44:04

things.

2:44:06

So you

2:44:06

might be

2:44:07

actually shocked

2:44:08

you might be actually shocked

2:44:08

you

2:44:09

like you

2:44:10

thought you

2:44:10

thought

2:44:10

you're

2:44:11

like sir,

2:44:11

you're

2:44:13

what you're

2:44:13

how you're

2:44:13

how you're

2:44:13

how you're

2:44:15

78%

2:44:16

is our 57%

2:44:16

is

2:44:16

right or

2:44:17

not?

2:44:18

But then the

2:44:18

interesting part is

2:44:19

look at the

2:44:20

beautiful thing

2:44:21

this

2:44:22

43%

2:44:22

this is what actually

2:44:24

matter.

2:44:25

Now this is what actually matter.

2:44:26

Now this 70%

2:44:27

in the 70%

2:44:28

what will I get

2:44:30

for 78%

2:44:31

if the model

2:44:33

model is

2:44:34

defaulty

2:44:34

prediction

2:44:34

then bank

2:44:35

is loss

2:44:36

is not?

2:44:37

Bank

2:44:37

did model

2:44:38

make you.

2:44:39

Defulters

2:44:39

identify

2:44:39

to identify

2:44:39

to

2:44:40

now.

2:44:41

Now whatever

2:44:41

model you have built,

2:44:42

this model is

2:44:43

unable to

2:44:44

identify any default

2:44:44

that.

2:44:46

That data

2:44:46

data scientists

2:44:47

made,

2:44:47

and gone and

2:44:48

the accuracy

2:44:49

78% left the

2:44:50

company.

2:44:50

I'm just kidding.

2:44:52

So,

2:44:52

it's

2:44:52

got to

2:44:52

okay.

2:44:53

But then actually

2:44:54

what he did is

2:44:55

useless.

2:44:55

He has

2:44:56

been to

2:44:56

a dummy model.

2:44:57

So that model is

2:44:58

not doing

2:44:59

what it is

2:45:00

supposed to do.

2:45:01

It is

2:45:01

performing very poorly

2:45:03

for the

2:45:04

class that matters.

2:45:05

So,

2:45:06

you've smote

2:45:06

you,

2:45:08

you

2:45:08

did a

2:45:09

accuracy

2:45:09

but you are

2:45:11

doing well

2:45:12

where it

2:45:12

actually matters.

2:45:14

This is the

2:45:14

increment and

2:45:15

improvement

2:45:15

I want to

2:45:16

show.

2:45:16

We're

2:45:16

actually machine learning

2:45:17

in practice,

2:45:19

we keep trying.

2:45:20

That's why it's a lengthy process.

2:45:22

You'll

2:45:22

say it's a lengthy process.

2:45:24

You'll say, sir, data has dot fit, and all

2:45:24

it's been

2:45:24

so you know the second

2:45:25

work.

2:45:26

But this is exactly the thing

2:45:27

that takes time.

2:45:29

You will keep on trying

2:45:30

different iterations of data,

2:45:32

other models

2:45:32

will make different parameters

2:45:34

tune and this is how you get

2:45:36

towards the best thing.

2:45:38

Make sense?

2:45:39

This is just a implementation

2:45:40

I wanted to share with you.

2:45:42

A last thing is

2:45:43

that's not difficult

2:45:44

and that's why I didn't want to

2:45:45

focus too much on that

2:45:46

generally, which is effectively

2:45:48

what is your

2:45:50

AUC.

2:45:54

Just remember,

2:45:55

so we have

2:45:56

all metrics, accuracy,

2:45:58

precision,

2:45:59

there,

2:46:00

f-1s4,

2:46:00

a confusion matrix we've discussed in detail.

2:46:02

Just one last addition

2:46:04

to the whole thing

2:46:05

is something called

2:46:07

area under the curve.

2:46:08

It's mathematics you

2:46:09

do not need the

2:46:11

mathematics behind it.

2:46:12

Just remember,

2:46:13

just like accuracy,

2:46:15

just like f-1-4.

2:46:16

F-1-Pur.

2:46:16

Like we've made

2:46:17

that new accuracy

2:46:18

is a good metric.

2:46:19

AUC is like also

2:46:21

something like an F1 score.

2:46:22

It will give you an overall idea

2:46:24

about how well the model is doing.

2:46:26

It is better than accuracy.

2:46:28

So,

2:46:28

like accuracy is not a good metric

2:46:30

I told you.

2:46:31

Accuracy is sometimes,

2:46:33

you know,

2:46:34

susceptible to bias.

2:46:36

So F1 score is a better quality metric.

2:46:38

So we can evaluate

2:46:41

the quality of the model.

2:46:42

Okay?

2:46:43

So we've here

2:46:43

evaluate

2:46:44

something called AU.

2:46:46

AUC stands for area under the curve and you can see that the decision P

2:46:51

AUC is coming as 97.9% whereas the random forest

2:46:54

AUC is coming as 9.991%

2:46:57

Okay, so AUC you can use a AUC function

2:47:02

and you can calculate area under the product.

2:47:04

So this accuracy type of a concept.

2:47:06

If you're going to generally

2:47:08

see what you mean it is AUC, it evaluates how well the model

2:47:14

separates the two classes, that's it.

2:47:16

See, the classification map, what do?

2:47:18

Classification in classes, conceptually, right?

2:47:21

We're classes separate

2:47:22

how well are we able to separate disease from not disease?

2:47:26

Depault us from not default.

2:47:28

We're the prediction correct.

2:47:29

How can predict can we are able to separate.

2:47:31

We are able to separate.

2:47:33

So that we are able to predict better.

2:47:34

So AUC is giving an idea

2:47:36

of how well we are able to separate.

2:47:38

Separate.

2:47:39

That, then, that's the same F1s 4 type of metric.

2:47:43

It's a formula in the same false negative

2:47:45

positive.

2:47:46

everything is ultimately based on that confusion matrix.

2:47:50

But it is another kind of formula.

2:47:51

As we have f-pons form described, a formula is.

2:47:53

Similarly, AUC's probably a formula.

2:47:56

But it's interpretation is more important.

2:47:58

You do not have to memorize that our formula content will be we have not given you.

2:48:02

So if you have AUC of 0.5, it is a very bad.

2:48:06

So the higher the AUC, the better it is.

2:48:09

One AUC is the best.

2:48:10

Like accuracy one is the best, AUC one is the best.

2:48:12

So these all metrics are, AUC, accuracy, accuracy,

2:48:16

precision, recall, f1s, all of these, the highest value is equal to 1.

2:48:21

So you should always aim for the highest value.

2:48:24

Asi we compare them.

2:48:26

So just keep this at the back of your mind.

2:48:29

Okay?

2:48:29

And again, final thing is basically threshold.

2:48:32

On threshold setting, we discussed here last week.

2:48:35

Please remember, default always 0.5 put.

2:48:37

So you have to threshold size set.

2:48:40

Whenever you are trying to set the threshold,

2:48:42

you will have to set the thresholds in the right way.

2:48:44

So set the thresholds in such a way.

2:48:46

that you are able to get the best model and so that you're able to get the best

2:48:51

f1 scores primarily okay that other of the model that threshold up to set

2:48:56

you set up to set up to set the parameters it will get impacted so you need to set

2:49:01

the threshold in the right way that is the other way

2:49:04

that is the other idea

2:49:06

any questions guys

2:49:16

So this we have saved got here.

2:49:21

So just in case you guys are also referring back.

2:49:24

So whatever I did that towards the end, I've actually saved that no output.

2:49:27

So this all the EA.

2:49:28

So the UCI credit card one that I did.

2:49:31

I think this was a nice one.

2:49:32

We were able to do these four last things.

2:49:35

We did logistic here.

2:49:36

Logistic plus floater,

2:49:38

random forested, decisionry,

2:49:40

and we've made the four things of actually compared here.

2:49:42

So I've added that part at the end.

2:49:44

You can see that comparative flow.

2:49:45

Okay.

2:49:46

In this basis, there are a case studies I will encourage you to do.

2:49:49

This is the way where your learning will get solidified.

2:49:53

People were asking me,

2:49:54

sir, how do you implement these are these things,

2:49:57

how are we are going to solve case studies.

2:50:01

You need to get better at, you know,

2:50:03

different case studies you do, you try to get better at it.

2:50:06

You go to Kaggle, you pick up some data sets.

2:50:09

Like we have discussed here,

2:50:11

you have in Kaggle,

2:50:12

you go, different data sets take.

2:50:13

And that is how you will get the confidence.

2:50:15

You get the confidence to work.

2:50:16

work on, you know, different problems.

2:50:19

Okay, like in the last session,

2:50:21

I have shared with you in the last session,

2:50:25

you know, the notebook that I shared,

2:50:28

where we have a lot of exercises

2:50:30

I think that's the way to implement.

2:50:33

You can, if you go back to the last session notebook,

2:50:36

21st April, you go,

2:50:40

we have actually this in class in

2:50:42

but we have you referenced links

2:50:44

that is what you do.

2:50:45

That is what you do.

2:50:46

what I really encourage you to do.

2:50:48

You go back to,

2:50:50

you go back to these.

2:50:52

Look at this.

2:50:53

These are wonderful use cases.

2:50:54

This is credit card product detection.

2:50:56

These are all real data sets.

2:50:58

Telecom customer churn.

2:50:59

Customer churn is a very important use case.

2:51:01

Companies are doing it.

2:51:02

They are looking at,

2:51:03

this is a real world telecom data.

2:51:05

We have this is a real world telecom data.

2:51:06

We have these links up.

2:51:08

This is the way to solve it.

2:51:09

You have these data set look.

2:51:10

Tegel in.

2:51:11

Okay,

2:51:12

your data has given

2:51:13

Okay, customer ID,

2:51:14

gender, senior citizen,

2:51:15

partner, dependents.

2:51:16

This is all information and based on that,

2:51:18

you have to predict

2:51:19

that you will the customer churn or will the customer not churn?

2:51:22

That is what you will have to do.

2:51:24

So based on the different features of the customer,

2:51:26

we will have to predict with the customer churn or will not churn.

2:51:30

This is the big thing.

2:51:31

Telecom companies are doing it.

2:51:32

They are trying to estimate what is the probability that customers will churn

2:51:37

based on the features.

2:51:38

Credit card fraud.

2:51:39

They've discussed this.

2:51:41

These are very real data sets.

2:51:43

This is like 13,000 votes say.

2:51:45

It's a lot set in.

2:51:47

It's actually, data set contains transactions made by credit cards.

2:51:50

September, 2013, by European card.

2:51:52

This is real data.

2:51:53

Actually, what do?

2:51:54

Many times, the community comes together,

2:51:57

they're anonymized.

2:51:58

The customer names, customer numbers,

2:52:00

it's just actually real data.

2:52:03

So you're real data for credit card for detection.

2:52:05

But the thing is the x, that is,

2:52:07

the way is, the train test plate,

2:52:09

you can,

2:52:10

you can all the last chart,

2:52:11

that code template, make,

2:52:12

all disease prediction.

2:52:14

We have discussed already.

2:52:15

Like you have diabetes, cancer detection

2:52:17

that is your heart disease prediction.

2:52:19

Now, look, same to same problem is.

2:52:21

X, Y, that problem framing mindset that we built in the initial classes,

2:52:24

right?

2:52:25

HR analytics.

2:52:26

This is a very interesting use case.

2:52:27

We are trying to predict whether the person will leave the company.

2:52:30

You're looking at the different features of the company.

2:52:32

Now, look, here here on data set you are

2:52:34

age, business travel, daily rate, department,

2:52:37

what's department in,

2:52:39

how last compensation was,

2:52:42

how bonus made,

2:52:43

who's manager is.

2:52:44

Based on all of that.

2:52:45

that you can basically predict.

2:52:46

Will the person leave the company?

2:52:48

Will the person not leave the company?

2:52:49

Like, customer in churn

2:52:51

churn,

2:52:52

churn, means will you leave Gio and go to Airtel?

2:52:54

That customer,

2:52:55

will you leave one company and go to another company?

2:52:58

Similarly, companies may attrition credit.

2:53:01

Attrition, will you leave one company?

2:53:03

And finally, the last one was bank marketing.

2:53:07

This is also very interesting.

2:53:08

This is a marketing data set.

2:53:09

They say,

2:53:10

banks' the phone will say,

2:53:11

you want to take a personal loan,

2:53:12

credit card,

2:53:13

you want to take a personal loan,

2:53:14

credit card.

2:53:15

This is a great use case.

2:53:17

This is a marketing use case.

2:53:18

It's a very nice classification data set.

2:53:22

We are looking at the different features of the customer.

2:53:24

You have customer to study

2:53:26

and based on that, you try to predict

2:53:28

that the customer actually in the product

2:53:31

is not.

2:53:32

This classification.

2:53:33

Ultimately, X is Y is.

2:53:35

What is X?

2:53:36

X is basically nothing but the features of the customer.

2:53:38

We are tracking different different features of the customer.

2:53:41

You have,

2:53:42

how time customer care agents have talked

2:53:43

to,

2:53:44

how time in website and went

2:53:45

where we are tracking how much time you spend on the site.

2:53:47

We are looking at all your features.

2:53:49

And based on that, we are trying to predict that,

2:53:51

hey, are you buying the product or are you not buying the product?

2:53:54

We are trying to predict, will you buy the product,

2:53:56

will you not buy the product?

2:53:58

And this is so useful.

2:53:59

You know, I'm sure people have heard of, you've got these calls

2:54:03

one of time from some of these companies,

2:54:05

they will ask you, sir, you want to take a connection,

2:54:07

you want to take a bank account, you want to take a loan,

2:54:09

credit card, some phone, but can we build a machine learning model,

2:54:12

but can we build a machine learning model to predict

2:54:15

What is the likelihood the customer might take it?

2:54:17

Okay?

2:54:18

What is the likelihood the customer might actually take the load?

2:54:21

What is the likelihood the customer might file the product?

2:54:24

And can be target customer better?

2:54:26

Online in it's a quite.

2:54:27

Our physical channels to have this not yet.

2:54:30

But online advertising, online targeting happens entirely based on this approach.

2:54:34

We are looking at your online profile,

2:54:37

your input, your behavioural profiles, your what you're clicking,

2:54:41

your cookies and all that.

2:54:42

That's how Facebook and all these companies do.

2:54:44

And based on.

2:54:45

that we are trying to predict what is the likelihood sign will buy that product.

2:54:49

If sign is likely to buy that product, I will show that on science home pitch,

2:54:52

something by that.

2:54:53

So I say, I see your YouTube marketing, Facebook marketing, basically.

2:54:57

This is the idea.

2:54:59

Because this is your, this is your practice section.

2:55:02

This is how I encourage you to use some of the learning.

2:55:05

Because in class, as I've said before,

2:55:07

we have time limited, I wish we had more time for the classes,

2:55:10

but this is what it is.

2:55:12

Limited time here that way.

2:55:14

whatever we are able to do, we try to do as much case studies we can.

2:55:18

And I try to give some extra case studies.

2:55:20

But then this is where you will have to travel.

2:55:22

You will have to take some time.

2:55:23

You will have to, you know, venture into different data sets.

2:55:27

The whole idea is to make you feel comfortable.

2:55:30

That we, the world is not very different.

2:55:33

You go to Kaggle's four problems of data set update.

2:55:37

It is so simple.

2:55:38

It is not difficult at all.

2:55:40

But the only thing is you have to sit and practice.

2:55:42

You have to put your effort and you have to do.

2:55:43

You have to put your effort and you have to do it.

2:55:44

And if you just think that, okay, I will do, then it will not.

2:55:48

You can actually have the motivation and actually go and

2:55:51

go and.

2:55:52

Okay.

2:55:53

Yeah.

2:55:54

Okay.

2:55:55

So, okay.

2:55:58

I think any other, any other questions?

2:56:05

I will pass it over to Vinot.

2:56:08

We know, I think you can take over.

2:56:10

I think that folks are no other questions.

2:56:13

We can.

2:56:14

You have to, you have the quiz or something?

2:56:16

You want to do?

2:56:17

Yeah.

2:56:18

Is we not there?

2:56:20

Ah, okay, okay.

2:56:23

Yeah.

2:56:24

Yubraj has asked the question, is this is the same way we will be building?

2:56:27

This is the same way we will be building.

2:56:30

Actually, I'm not the way how we do,

2:56:33

things in agents.

2:56:34

Agent building is some,

2:56:39

a slightly different kind of piece to clarify.

2:56:42

Agent building is a different piece entirely.

2:56:44

We don't build agents in the same way, just to plan it.

2:56:47

Okay?

2:56:48

Yeah, yeah.

2:56:49

Because agents' concept is a little different.

2:56:51

We're not getting to that right now,

2:56:53

but agents we're a different thing,

2:56:55

because that's already been already built.

2:56:57

Language models are already built.

2:56:59

The concepts are similar.

2:57:00

You'll be able to relate to it.

2:57:01

Train data, test data,

2:57:02

the concept of test data will be very similar.

2:57:04

When we agents are,

2:57:06

we're going to Confucian matrix will be very similar.

2:57:08

Classification report will be very similar.

2:57:10

There are many things similar

2:57:11

but,

2:57:12

yeah, you'll be logistic use not.

2:57:13

You will be very similar.

2:57:14

random forest use going to be.

2:57:15

Because you have a other model seems.

2:57:17

But concepts will be very similar.

2:57:19

Things your are you that's the idea.

2:57:21

Okay? That's the idea.

2:57:23

Okay?

2:57:24

Eugraj, is it fine? Convinced?

2:57:27

No, no, no.

2:57:30

Train test split also will happen.

2:57:32

That will be over.

2:57:33

But there.

2:57:34

We have not discussed that here.

2:57:35

But yeah, if you're asking me,

2:57:36

because train test fit,

2:57:37

yeah.

2:57:38

Yeah, yeah.

2:57:39

There we have split data data.

2:57:41

Absolutely.

2:57:42

Absolutely.

2:57:43

But we have some time to go there.

2:57:44

If you're asking, sir, do we train the, split the data?

2:57:46

Yes, we do.

2:57:47

We do.

2:57:48

Absolutely.

2:57:50

All right.

2:57:52

All, yeah.

2:58:00

Connected it, definitely.

2:58:02

See, whatever we are talking about here in the classes,

2:58:04

they're all connected.

2:58:05

At the end of the day, they're all connected.

2:58:07

All connected.

2:58:08

This is not completely disconnected.

2:58:11

ML is to some extent disconnected.

2:58:13

M.

2:58:14

related, but they are very much connected.

2:58:16

Agents are very much connected.

2:58:17

You will be related to the same ideas.

2:58:19

Training data, testing data, accuracy.

2:58:21

Same ideas are used there.

2:58:23

Connected.

2:58:24

So guys, please this go through.

2:58:28

The last part was very interesting what we did.

2:58:31

And I really encourage you.

2:58:33

You are, please implement it.

2:58:34

Okay?

2:58:35

If you have to jemini use kind of,

2:58:36

but try to implement these ideas.

2:58:38

That is something I will really encourage on YouTube.

2:58:41

Okay.

2:58:42

At least the weekend.

2:58:43

The weekend is coming.

2:58:44

You're getting some time.

2:58:45

Today is Thursday.

2:58:46

We're getting two days, Saturday, Sunday.

2:58:48

We're meeting again on Tuesday.

2:58:50

So, you know, I would love to hear from at least some of you folks.

2:58:54

You should come back next class and tell me that,

2:58:56

sir, yes, out of these five, we solved one problem.

2:58:59

That could be a nice challenge we can do, no?

2:59:02

Yeah.

2:59:03

So next class, you should come back and say, yes, I actually solve this.

2:59:07

Okay.

2:59:09

Great.

2:59:10

Alright, guys.

2:59:13

Thank you. I think that's all we have for today.

2:59:15

You can take some time, fill up your polls, please.

2:59:17

And, yeah.

2:59:19

Vinot, I think, is Vinod there?

2:59:21

Yeah, yeah.

2:59:22

Yes, I am.

2:59:23

Okay, okay. Yeah.

2:59:24

So thank you.

2:59:25

Yeah.

2:59:26

I just want to share the Mendi-meter quiz now.

2:59:28

Ah, sure, sure.

2:59:29

Please, please.

2:59:30

Yeah, please.

2:59:31

Yeah.

2:59:33

I'm sorry, I think you keep late.

2:59:36

Yeah.

2:59:37

I will just stop sharing.

2:59:43

Okay. Thank you.

3:0:13

Thank you.

3:0:43

please scan the QR code and join the Mentimeter quiz.

3:1:13

Thank you.

3:1:43

Okay, let us start the quiz now.

3:1:57

So these are the quiz rules.

3:2:00

We'll have 15 seconds to give your answer.

3:2:13

Thank you.

3:2:43

Thank you.

3:3:13

Thank you

3:3:43

Thank you

3:4:13

Thank you

3:4:43

Thank you

3:5:13

Thank you

3:5:43

Thank you

3:6:13

That's all from my

3:6:23

Thank you,

3:6:24

Thank you, thank you, thank you,

3:6:27

Thank you,

3:6:28

Thank you,