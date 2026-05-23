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

Thank you.

4:30

Thank you

5:00

Thank you

5:30

Thank you

5:32

Thank you

5:34

Thank you

5:36

Thank you

5:38

Thank you

5:40

Thank you

5:42

Thank you

5:44

Thank you

5:46

Thank you

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

Thank you.

9:48

Thank you.

10:18

Thank you

10:48

Thank you

11:18

Thank you

11:20

Thank you

11:22

Thank you

11:24

Thank you

11:26

Thank you

11:28

Thank you

11:30

Thank you

11:32

Thank you

11:34

Thank you

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

Thank you.

15:06

Thank you.

15:36

Thank you.

16:06

Thank you

16:36

Thank you

17:06

Thank you

17:08

Thank you

17:10

Thank you

17:12

Thank you

17:14

Thank you

17:16

Thank you

17:18

Thank you

17:20

Thank you

17:22

Thank you

17:24

Thank you.

17:54

Thank you.

18:24

Thank you.

18:54

Thank you.

19:24

Thank you.

19:54

Thank you.

20:24

Thank you.

20:54

Thank you.

21:24

Thank you.

21:54

Hi, everybody, good evening, uh, good evening all of you.

22:09

We will just get started here.

22:24

Thank you.

22:54

Thank you.

23:24

So, guys.

23:54

topic, linear regression, all this while we have been discussing quite a lot about, you know,

23:59

building machine learning models, right?

24:02

We talked about the machine learning workflow long time back in our introductory session.

24:08

And today, finally, we will be officially discussing our, you know, a discussion on machine learning.

24:18

So we'll actually start building, start building models in today's session and understand

24:24

what these models are, how to build the models. And specifically we will be discussing

24:29

about something called linear regression in the session today. So linear regression will be the

24:35

the main power, the main focus of our discussion today. That's what we'll be covering overall.

24:54

I will start the discussion with a small introduction to what, what regression is. So this is again, something that is known to us already. We already know at a high level what is regression. But I will still give you a very quick summary understanding of what regression is, kind of a recap of what we have already seen and what we have already discussed. So we'll, so we'll talk about that. And we'll, we'll, uh,

25:24

that learning from there. So overall, this is the main agenda of what we'll be covering

25:34

today just to give you a bit, bit of a basic idea in terms of what we will talk about today.

25:39

So this is the broad agenda, what we'll be discussing. So we'll look at the difference between what is

25:44

regression versus what is classification. We will talk about what is the meaning of regression. What is

25:49

the meaning of best fit line? What is the meaning of slope, intercept? So,

25:54

some basic elementary level mathematics. Next, we will do quite a bit of hands on

26:01

using linear regression. So I, so we'll, so we'll have a fair bit of hands on where we will use

26:05

collab. We will write Python code and we'll actually build the model. The model building we have

26:11

already seen before. It's not new. At a high level, we have already seen quite a bit of model building

26:16

before. We take a data, we do a train test plate. On the training data, we, we fit a model. On the

26:24

testing data, we evaluate a model or do predictions. So those broad concepts we are already

26:29

aware. Today we will try to put all those pieces together and we'll finally build a linear

26:35

regression model. Okay, although code wise we have already seen it at a high level, but we'll see

26:39

this in more detail today. Finally, we will talk about comparing the model to a baseline. We'll

26:46

discuss what is the concept of a baseline. This will be a bit of a new topic, overfitting, underfitting,

26:51

sort of a new topic over here. This we have not covered in detail before. I might have

26:56

I might have talked about it generally but not in detail, but we will cover what is the concept of

27:01

overfitting. And finally, we will discuss the concept of errors or residuals. Residules

27:07

what? Residuals mean errors. So this is nothing but how far is the actual values from the predicted

27:17

values. So that is how we define errors or residuals.

27:21

So errors or residuals can be, they can be used to define how far the actual values are,

27:30

how far are the actual values, how far are they from the predicted values?

27:35

That is what errors and residuals basically stand for. That's the intuition, okay?

27:40

So we'll talk about these topics today. That's to summarize the flow of the session today.

27:46

So what I want to do, I want to again start out with a very quick recap in terms of what

27:50

regression and classification are. So I, and once again, the contents of this session,

27:58

20th May, are already in the drive. You can already see this in the drive link. I've created the

28:03

folder. These are some of my contents. The Jupita notebook I'll be using. And there is something

28:08

more we will add along the way. All right.

28:20

So first things, I hope everybody, everybody remembers what is the difference between regression and classification. All of you, all of you recall that. Everybody remembers what is regression versus what is classification. So regression is that kind of machine learning where we are trying to predict a numeric output.

28:41

Your output was number that is how we define regression. So that is your sales prediction, stock price prediction. Yes, all regression problems there.

28:49

Right. So the output that you are trying to predict is a number. It's a numeric output that you are trying to predict. So that is how we define regression. Whereas classification is that kind of machine learning where the output is not a number. Whatever output you are trying to predict is not a numeric output. So you can talk about some examples where we are trying to identify. We are trying to predict what is the sales. What is the stock price of going to be next week?

29:19

what are the oil prices going to be what are the housing prices going to be what is the salary of the person based on their experience

29:25

in all these cases based on some x we are trying to predict some y so with this goes back to our very first class if you remember

29:33

regression versus classification so anytime we are trying to predict a numerical output it's a regression problem

29:37

anytime we are trying to predict a category it is classification so what could be some

29:44

examples of classification problems a very good example is spam classification so you're

29:50

looking at the contents of your email you're looking at the contents of your email

29:53

but of the real if you look at your Gmail outlook mailboxes and all this is exactly what's going

29:59

on behind the scenes so you're looking at the contents of the email and based on the contents of the email we are

30:05

trying to predict is it a is it a spam email or is it a not spam mail so based on the

30:12

contents of the email we are trying to predict excuse me we are trying to predict is it a spam or is it not a

30:19

spam so that is the specific problem we are trying to solve we are trying to predict is it a spam is it not a

30:24

spam based on the contents of the email so that is a classification problem either spam or not spam

30:31

another good example will be based on the features of a person based on your different

30:35

different diagnostic attributes,

30:38

your BP, your cholesterol, your body mass index, your weight, your age.

30:42

So based on all these factors, can we predict,

30:44

are you having a disease or are you not having a disease?

30:47

Yes or no.

30:49

So all these, you know, like personally I also use a Galaxy watch,

30:54

Galaxy watch ultra eye wear, okay?

30:56

So they have a fault detection feature.

30:58

Isn't a fault detection?

30:59

That Apple Watches maybe have.

31:01

Some of the Garmin watches maybe out.

31:03

That is a very good use case of machine learning.

31:04

fall detection how do you guys so these galaxy watches are fitted with many sensors

31:10

gyroscopic sensors are there and based on the features based on the value of the

31:18

sensors based on the orientation or here real time is real time they are capturing your

31:23

movements and all that so based on all of the features based on the input sensor data the

31:29

model is trying to predict did you fall did you not fall the real time fault detection that is

31:34

happening all the time in the galaxy watches, okay? And if the model detects a fall,

31:39

it they will automatically call up emergency surveys and all those kinds of things.

31:41

Okay, so you can see some practical examples how classification is getting used in practice.

31:48

Some other examples could be fraud detection, credit card fraud detection.

31:51

I'm ne the use case discussed here class in. So this is just to tell you the difference between

31:56

regression and classification. So now we are officially entering into ML, the model building phase.

32:01

So the first two sessions will focus on regression. I'll,

32:04

regression is a more regression session over next week and then we will get into

32:08

classification so now we will take our focus back to regression what is regression how are

32:14

we doing regression okay so as I told you so based on the features we are trying

32:20

to predict a numerical output another great example could be a taxi fair

32:25

prediction taxi fare prediction taxi fair prediction is also a very good example of a

32:28

regression problem so over Ola yes of yes of how is it happening how is it happening

32:34

so they are looking at the different features of the cab ride we are looking at the different

32:39

features of the you know of the booking and based on that we are trying to predict what is the

32:45

fair of the ride you're looking at the source destination the location all of this and we are

32:51

trying to predict what is the what is the fair of the right okay so these are all good examples

32:56

of a regression problem now we will get to understand a little bit more in detail about

33:04

what is going on behind the scenes

33:06

how is it all happening

33:09

okay and i hope all of you remember this terminology

33:12

this terminology should be very clear right x or y

33:15

x kx what is what is nothing but features

33:19

just remember this terminology all of you

33:21

x basically stands for features

33:23

and y

33:25

y basically stands for the target or the output

33:29

so based on the features

33:31

we are trying to predict what is the output

33:34

so this is a very nice use case of a housing price prediction problem

33:39

so based on the features of the house

33:42

we are looking at the number of bedrooms the area the age the parking

33:47

we are trying to predict what is the sale price of the house

33:52

yeah x is y hey this is your data

33:56

on the basis of this the model learns a pattern this is what we already talked

34:01

about based on your x y combinations

34:04

your historical data right whenever we are trying to build a machine learning model

34:09

this data initially whatever i'm giving you right now will be the historical data so based

34:15

on this x y combinations or based on this input output combinations you will use

34:21

some algorithm and based on that you will build a model you will use some algorithm based on

34:29

that algorithm you will end up building a model model is nothing but an equation a relationship we will

34:34

build and then next time there is a new value of x we will use that

34:41

relationship to predict what is the corresponding value of y I hope all of you

34:46

recall that from our prior machine learning classes right basic ML discussion so on

34:51

the training data on the training data we will learn the pattern we will learn the

34:57

relationship between y and x right it will be something like y equal to 2x plan plus 3x2

35:02

plus 5x 3 whatever

35:04

and we will see that in detail today we will learn that relationship model learns the

35:07

pattern you learn the model okay and after that on the new data given there is a new x given

35:15

there is a new house features of the house you will put that in the equation you will put that

35:21

new x in the equation and you will get the predicted point that's the intuition now we'll get a

35:29

little deeper and we'll try to understand exactly what linear

35:34

your regression is behind the scenes what are we doing behind the scenes and to explain

35:39

this in a better way i will take you back to my snippet here so all of you go back to my uh all

35:46

if you take a look at this for a minute okay so this this might look like a little bit of mathematics

35:52

but it is not very scary don't be scared with this i will explain to you in detail what is it but this

35:58

understanding is required you should know what is slope what is intercept so what we are getting

36:02

right now is the concept of straight line coordinate geometry jessy umne y

36:08

equal to mx plus c these kinds of concepts we have seen so that is what we are trying to go over

36:15

so before i continue on any further all of you take two minutes of your time and just glance through

36:22

whatever i'm showing on the screen right now this is like a class 9 10 mathematics concept something

36:27

we have studied back in our school days just take two minutes and glance through it once all of you

36:32

Thank you.

37:02

Thank you.

37:32

Thank you.

38:02

Thank you

38:32

Thank you

39:02

okay guys i hope everyone's everyone's everyone's gone through it so

39:11

what we are seeing on the screen right now what we are seeing on the screen right now okay i just

39:16

give another 30 seconds all of you if you're still going through it just try to read this part as well okay

39:21

look at this part slope intercept see if you can relate to this

39:25

this y equal to mx plus c something that most of you might have seen in your school days coordinate

39:32

so that's why i'm giving you some time to uh recall those concepts because that's all

39:39

what linear regression is based on there is nothing python code though we already have seen before

39:43

there is nothing new there and the only new part of our learning today will be this particular

39:48

equation this is the major new concept of you know that we are discussing today okay take

39:53

take another 30 seconds all of you try to recall the ideas then i will recap it for you

40:02

Thank you.

40:32

Thank you.

41:02

okay so guys what we are seeing on the screen on the screen is a straight line equation equation

41:25

so you can focus on this particular diagram and what i'll do is for explanation let me download this and that'll be easier

41:32

so i'll try to explain what is this the mathematical concept then we'll take it back to

41:39

python so we have x axis we have y axis and what you're seeing here this is like the straight

41:48

line equation and the equation of the straight line is given by y equal to mx plus c so there is

41:56

the x axis coordinate geometry there is the y axis coordinate geometry concept axis and this is the

42:02

a straight line that you are able to see the equation of the straight line is this so m is the

42:09

slope and m the slope is defined by delta y by delta x what is the meaning of slope guys

42:20

slope basically means that for every one unit increase in the value of x what is the

42:28

change in the value of y that is how we understand the meaning of the slope right

42:32

if your x increases if your x increases by one unit your y increases by what

42:42

it is almost like when you're climbing up a hill when you're going up a hill imagine these two

42:49

points right now point a to point b you have a line equation eh right so when you're going from

42:56

let me use my marker just one second guys let's say this is point a an anna and this is

43:02

is point b so if you're going from point a to point b if you're going like this so you're going

43:09

up that means what if you're traveling a certain distance horizontally if you're going this much

43:19

distance forward you are also going this much distance up a to b if you're moving it is like saying

43:28

you're moving a certain distance forward and a certain distance

43:32

up this is slope of slope meaning and this certain distance forward is given by

43:41

delta x delta means what is the what is the what is the change

43:50

so initially the value of x was this and this is the final value of x that's why we call it

43:56

x i and xf similarly initially the value of y was this

44:02

now the value of y is this y f so that is how we define what is delta x and what is delta y and what is

44:12

slope what is m slope it is delta y divided by delta x yeah your definition of slope

44:20

and finally there is something called y intercept see what is the meaning of y intercept

44:32

how far is that line the point where the line intersects the y axis how far is that from the

44:41

origin that is how we define the y intercept okay so we just now understood what the meaning

44:50

of this equation is whenever we see y equal to mx plus c we now understood what is the meaning of this

44:56

straight line equation what is the meaning of y equal to mx plus c m m stands for the slope

45:02

and slope can be positive slope can be negative right now whatever you're seeing on the screen

45:10

right now whatever you're seeing on the screen this is basically positive slope okay whatever

45:18

you are seeing on the screen right now this basically stands for positive slope and slope can be

45:25

negative also slope can go like this also this is negative slope that means for every one unit increase

45:32

in the value of xx3.

45:32

how much did you go down so that is how we understand the meaning of slope and c stands for

45:40

y intercept and if you combine these two pieces you will start getting these kinds of straight line

45:46

equations jessi you will get something like this y equal to 2x plus 3 so next time you see an

45:52

equation like this you should be able to relate it back to mx plus c which i explained

46:02

and you should understand that m is nothing but two and c is nothing but three slope is

46:10

nothing but that slope is nothing but two and intercept is nothing but three that's the way we

46:17

understand what is slope and what is intercepted okay so you have an example

46:21

two x plus three now look look at that that line the point where it intersects the y

46:28

axis how far is it from the origin and this i hope everybody remembers this is

46:32

back to your school days right class nine 10 we have

46:35

kied straight line geometry along with circles and all those geometric figures that you

46:40

studied so first first we studied straight lines then we then we then we went to

46:46

other kinds of geometric shapes right this is all part of your geometry

46:49

trigrometry concepts okay all right now

46:53

now this one example we've given minus 9x plus 7 okay what what what what is this

47:00

minus 9x plus 7 it's got case how can you understand this so the slope is minus 9

47:05

that means the the the line will look somewhat like this

47:09

a so it will look somewhat like this so you can think of it this way

47:18

let me draw this out there is x axis this is y axis this is y axis

47:23

there it is your that is your that is your minus 9x plus 7 so this 7 basically

47:31

stands for the y intercept the 7 stands for the y intercept basically

47:37

that's the intuition for what slope and intercept basically stands for

47:43

now moving on relating this concept to a real problem a real problem okay let us see

47:53

so i give you uh x y combinations back to the same story that we discussed in our

48:01

introductory machine learning class i give you xy combinations and we want to use some algorithm

48:09

and based on that we want to build a model so this story we all know right one two four five six

48:16

seven and i give you eight you have to predict what is the y this is the same story we have discussed

48:21

so based on the available data use some algorithm and build a model the model that you end up

48:32

building is a mathematical function y equal to x plus one yes that's a function over right so x

48:38

y combinations use some algorithm build a model the model is nothing but a mathematical function

48:45

and next time i give you a new value of x if i give you x is equal to 8

48:51

you can substitute x equal to eight here and you can predict y equal to nine here

48:59

this is the normal flow we have discussed now let us understand this geometrically

49:07

pictorial and visually what is happening so there is my x axis this my y axis

49:17

this is one comma two is this is one and there is two

49:25

you have four comma five okay i'm just giving an example so this is like your one comma two

49:36

this is like your four comma five and this is like your six comma seven

49:40

this is six and this seven see so basically what we have is

49:51

initially we have lots and lots of x y combinations

49:55

so we have this data to scatter plot represent

49:58

which training data is this one data is this data is

50:01

okay we've gotter plot represented

50:03

now what are we trying to do in linear regression

50:08

we are trying to find out the line

50:10

of best fit that is the geometric way how we are trying to solve the problem

50:18

this was just a conceptual thing that we discuss right but yeah how are we getting that y

50:24

equal to x plus one this is the geometric way we can visualize the problem we are not getting

50:30

to the algorithm level details here that's slowly not required here but the intuition is

50:35

important the mathematical intuition is important what we are trying to achieve so geometrically what we are

50:39

are trying to do we are trying to find what is the line that best fits the points

50:46

now if this is the two uh two dimensional coordinate space if we have

50:54

x axis y axis if we have this kind of this particular uh two dimensional coordinate space

51:02

if we have how many how many lines can you draw in this two dimensional coordinate space

51:09

you can theoretically draw infinite number of lines you can theoretically draw infinite number of lines

51:16

the straight lines can look like this like this like this like this there can be infinite number of

51:20

such lines you can draw right in this two-dimensional coordinate space

51:27

but out of all the infinite number of lines you can draw the line of best fit the line of best fit

51:35

will be this one it's not perfectly gone through all of it but it will actually go through all the points

51:39

and this is what we call the regression line and this equation is y equal to x plus one

51:48

this is a very easy problem that's why we are able to get a perfect fit but in real world it won't

51:53

be such a perfect fit so this is the pictorial view of how we do regression

51:57

you have data i repeat one two four five six seven a plot and

52:01

find out what is the line that best fits the points best fit so the straight line equation that best

52:09

the points is y equal to x plus one so its slope one is intercept one

52:14

whatever that's that we already saw this is what we get out of model training we train a model

52:20

on the data visually and model prediction at time

52:24

kha k'kka value eight so we have eight somewhere here now that you learn the pattern

52:31

you substitute that eight and see what is the corresponding value of five

52:36

oh nine so this is the way how we

52:39

how we visualize regression pictorially so this is the same story which i explained here

52:46

you can see we plot the points and we find what is the line of best fit

52:53

y equal to mx plus c where m is the slope c is the windercept and this is actually

52:58

something that you can also interpret

53:03

no data data is not always in numbers rnick because if data

53:07

numeric not is we already know how to handle it right if data number maybe

53:12

what can we do we can do encoding remember so we have learned some pre-processing techniques

53:18

you have if a categorical data be ho go so you

53:21

you can't you can't you see when you say data if you mean data is features features

53:30

so x will always be why will always be number x could be or

53:37

so why will always be numeric because that is what we studied in regression to start with

53:44

if you look at the main concept of regression the output is always numeric okay sure sure

53:53

we can take an example let us say let me open up a whiteboard for a minute okay let me give an

53:59

example let's do salary prediction for a minute before i digress to another topic

54:07

before i just want to make sure that this conversation is clear to all of you straight line

54:13

equation and how to visualize linear regression uh pictorially everyone is fine anybody wants me to

54:20

stay back repeat this one you're all okay please let me know on chat just this top part

54:30

everybody is clear with what we are trying to do fundamentally in linear regression at a basic level

54:37

so we have just studied the concept of what is the straight line equation

54:42

and we have also studied how we are trying to fit a best fit line that's it

54:46

but whatever we are doing conceptually before y equal to x plus 1 em

54:51

conceptually correct right we are just trying to you we are just trying to do it visually right now

55:07

just to give an example to you hernika what you asked imagine we are trying to do salary prediction

55:28

okay so based on the experience of a person and the

55:37

skills of a person we are trying to predict what is the salary of a person right

55:46

so you're your x1 here x2 and this your x2 and it makes sense so first of all conceptually

55:58

here regression problem here regression problem is because output the output salary is a number

56:07

if you look at the output salary output number see that's the most important thing how do you

56:13

classify something as regression or classification output basis so salary is numeric so that makes it a

56:19

regression problem but features to anything

56:22

if you can't be anything in my current scenario experience of a person can be too

56:28

this numeric but skills to do anything let's say this is python

56:37

experience is his skill java is the other man's six year experience

56:42

skills python are another person three years experience skills java

56:48

but can you do machine learning on this data may

56:53

can't right see output we are not concerned about output is a separate thing that is always

56:58

numeric right because for regression problem output is a number but this may not be a number

57:02

features can be anything else this go how can handle kertek what did we discuss

57:07

we will do encoding one hot encoding remember we discussed about this in our

57:12

classific pre-processing session last week so we will do categorical one-hot encoding

57:18

so kase karengen so we will go and take experience here

57:28

and we will create as many number of columns we will create as many columns we will create as many columns

57:37

as there are a number of unique values so we'll

57:42

python can a column

57:43

be i will call it skills python

57:48

and we'll call it skills python and we have

58:06

simply pre-processed our data that's it so again this is like your x-1

58:18

this is like your x-1 x2 this x3 and this is o guy this features

58:25

this is a target make sense so this is two python present so 1-0 this 5-0-1-6-6

58:36

1 0301 okay so all right now i hope you hope you are clear so when you say data is

58:46

always numeric huh output is always numeric but input may not be right now we can do machine

58:52

learning on this data okay clear it now back to the same to the same linear regression story

58:59

and you know you know this is actually linear regression using multiple variables what we

59:06

discussed was using a single variable how many discussed y equal to mx plus c

59:13

that was a general pattern there single x

59:17

but what happens if there are multiple xs same story will happen here okay so if i go

59:23

and build a model y will be equal to what m1 x1 plus m2

59:36

same story as many number of features are there the same linear equation continues

59:43

so this is the way to relate to it okay i hope it i hope it i hope you are clear okay

59:52

now moving on back to linear regression concepts so we have talked about what is linear regression

59:59

intuitively and we have also discussed the meaning of what is slope and what is intercept

1:0:04

one other way you can understand slope for one unit increase in x

1:0:13

what is the change in y see if i make this a slightly simpler problem

1:0:19

take an example let me just remove all this and i will make it simple

1:0:30

let's say this is what we have right now you're your your salary

1:0:36

experience and based on that you want to predict what is the salary

1:0:40

sorry salary will be the output you want to predict what is the salary

1:0:45

based on the experience x

1:0:52

so these are the patterns experience is two salaries let's say

1:0:57

i'm keeping it very simple right now let's say salary is equal to three

1:1:00

experience five is so salary 11.

1:1:02

Okay, let me give a different number.

1:1:04

Okay, two are, let's say, um, just give me one minute.

1:1:10

Two, two.

1:1:11

I'm just trying to calculate also manually.

1:1:13

Let's say I'll make it five.

1:1:14

Okay?

1:1:15

This I will make it 11.

1:1:17

This I will make it 13 and this I will make it 7.

1:1:20

Okay?

1:1:21

So I think everybody in the audience can understand the pattern.

1:1:24

Pattern to clear.

1:1:26

So if you go and take the data and build a model,

1:1:28

pattern what is?

1:1:29

What is?

1:1:30

is y equal to 2x plus 1.

1:1:32

This pattern is now it is not that we will do it manually.

1:1:36

Here manually not we will use a algorithm.

1:1:39

In Python we will come to that and we will build it.

1:1:42

This is the relationship.

1:1:44

Now the relationship is what is

1:1:47

if I change this with the actual variables.

1:1:50

This is what we are getting 2 times experience

1:1:53

plus 1.

1:1:55

Now the question is what is the meaning of this equation.

1:1:58

That is what we are trying to look at.

1:1:59

to look at and if you relate back to what we studied this two is nothing but the slope

1:2:05

and this one is nothing but the experience is nothing but the intercept this is in

1:2:12

the same form y equal to mx plus c right this is in the same form we are talking about

1:2:18

the question is how do you interpret the meaning of two and how do you interpret

1:2:24

the meaning of one

1:2:26

you?

1:2:27

what you know, this data is, this relationship, this equation is, okay, y equal to mx plus

1:2:34

c, straight line.

1:2:35

Now I want you guys to tell me what is the meaning of two and what is the meaning of one?

1:2:40

To a business user.

1:2:43

In a non-technical way, in a business oriented way, how will you explain this?

1:2:48

This is what is.

1:2:50

You have to explain the meaning of two and they explain of, explain the meaning of one.

1:2:57

Using the analogy of salary and experience, what does it mean?

1:3:27

I will just give it a minute for all of you to think over it.

1:3:43

We are just trying to understand what is the meaning of two and what is the meaning of one?

1:3:48

From a domain perspective, salary or experience in between

1:3:52

how can you interpret the meaning of two and one?

1:3:56

think about it.

1:4:26

Thank you.

1:4:56

Thank you.

1:5:26

Thank you

1:5:56

Now,

1:6:08

According to experience we interpret,

1:6:10

Okay, Prasat has also answered two means how much salary changes when experience increases.

1:6:15

Yes, yes, very good, very good, excellent Prasat, excellent, excellent, excellent.

1:6:20

Very good, very good.

1:6:22

So as Prasad rightly says, so as Prasad rightly says, see, as I say it,

1:6:26

this.

1:6:27

Right?

1:6:28

Where did we see this guys?

1:6:29

We saw this here.

1:6:31

If I take you back to my initial discussion, here we saw this.

1:6:36

Slope's what is the meaning of slope?

1:6:39

I know it's a little bit of math, a very basic level math we are seeing, but not very hard, right?

1:6:45

What is slope?

1:6:46

Slope is Mx plus C.

1:6:48

So, sorry, slope is del y by del x.

1:6:51

So slope tells you, as I explained, for every one,

1:6:56

one unit increase in x that means as you go one unit forward how much do you rise as you go one unit forward how much is y changing so it's like if you go from a to b that means you're going one unit forward how much how much are you rising or falling that is slope and same story if you relate to here slope is two that means for every one unit you go forward

1:7:25

You are rising two units.

1:7:28

And that forward?

1:7:30

What is?

1:7:31

Forward is, because now x-axis is experience.

1:7:35

If you want to pictorially see this,

1:7:38

if you want to pictorially see this,

1:7:40

this is your experience.

1:7:43

This is your experience.

1:7:44

This your salary.

1:7:46

Okay?

1:7:50

And this is what we have.

1:7:52

So, this is what we have.

1:7:54

So.

1:7:55

this is one.

1:7:57

So slope is defined by this.

1:8:03

For every one unit that your that your experience is going up.

1:8:09

How much are you rising?

1:8:13

So for every one year increase in experience,

1:8:19

the salary increases by two units on an average.

1:8:23

And what is one?

1:8:25

one is basically the salary of somebody who is having zero experience.

1:8:30

If a person has zero years experience, the salary of that person is equal to one.

1:8:36

So one is the baseline, the base salary.

1:8:38

Or one's basis of the salaries calculate.

1:8:41

So this is how you interpret the meaning of MNC.

1:8:47

Next time you're given any problem, you will take the data, build a model,

1:8:52

have a mathematical equation like this.

1:8:55

and the next step would be after you are able to get that mathematical equation

1:8:59

the other step will go to interpret that equation interpret the equation

1:9:04

basic salary is one that's right that's right shape interpret the equation that's the

1:9:09

equation that's the way you will have to go back and do it you will have to go back and

1:9:12

interpret the equation conceptually so so interpretation

1:9:16

so interpretation would be for every one unit increase in experience the

1:9:22

salary goes up by two units that is how you interpret

1:9:24

okay okay i hope everybody is clear this was pretty much the

1:9:36

excuse me the introductory ideas of regression that i wanted to talk about what regression

1:9:43

basically is what are we trying to do in regression and now we'll go back and try to do a very basic

1:9:54

a fit process in collab so we'll build a very basic regression model on

1:10:07

collab all right all if you can see my screen so this part is very basic I think

1:10:16

you will find this part very simple now initial part was a little bit of math but

1:10:19

it was required the maths was very minimal very basic level we saw but at two

1:10:24

that point mx plus c is required okay i want to just do a quick check with everybody all of

1:10:30

you are comfortable can you please tell me yeah mx plus c clear is up say

1:10:34

s up if i know if like i just want to make sure that everybody is comfortable clear

1:10:38

mx plus c let me know guys please let me know on chat if all of your absolutely clear then we'll

1:10:46

move on to the python code and i can assure you python code is very simple trust me one or two lines

1:10:50

of code you will have but the conceptual part is where i i

1:10:54

focused on a lot in the class today because that's the part that is the hardest code we have

1:10:58

already seen you'll find it very easy we'll see that now we'll go to the coding part now

1:11:05

clear everybody at all of you please respond some some some are pending just want to make sure

1:11:10

everybody's clear

1:11:24

okay thank you now moving on let us look at a very basic level one problem simple linear

1:11:34

regression using a single variable right so what are we trying to do i have curated a sample

1:11:41

data set where study hours have exam score here this is my data right now what you can see on the

1:11:48

screen right so here here we've trained test those of level one we have not

1:11:54

not done all that okay here i just wanted to show you the data so we have x we have y

1:12:03

and what is the business problem based on the number of hours that you're studying we want

1:12:09

to predict what your exam score will be so whatever data you're seeing on the screen

1:12:16

this is the historical data of let's say all students who are who are enrolled in massai school

1:12:22

because we will have the data right we will have everybody's data we will know for all the

1:12:29

students uh how many hours they are spending how many classes they're attending how many hours they're

1:12:36

engaging and based on that we will also know their scores so that is how we have plotted this data

1:12:42

initially so this is our historical data of existing students and what we are trying to do using this data

1:12:52

we are trying to find a line that best fits the points remember linear regression

1:12:58

what are we trying to do we are trying to find the line of best fit we are we are

1:13:01

best fit we can never have the perfect fit so the example we can never have the perfect fit

1:13:06

so the example we've made sure we're in the perfect fit that was real in never

1:13:10

never ever not now now now y equal to x plus one so that i must i make you

1:13:15

to explain to you but in practice your data points will never pass through the line all the points

1:13:21

will never pass through the line there'll always be some noise always be some randomness

1:13:27

to real world data will always be like this but at the same time what is the big picture idea

1:13:33

big picture idea what is this code in two line kind code is nothing i'll show the code in a minute

1:13:38

but big picture idea is if you if you're x mano it's why mano so the equation of the line is something

1:13:45

like this so i'm just randomly guess here here i'm just randomly guessing

1:13:51

this two unit is if you're going two units up uh forward i think you're moving up to 70

1:13:59

60 to 70 is going approximately i'm saying okay so much 15 by 2 7.5 i'm just guessing

1:14:07

the slope will be something like 7.5 i'm guessing don't worry about this okay yeah

1:14:12

you don't worry about this okay you don't worry i'm just guessing so this is this is broadly what the

1:14:17

equation of the line will be okay so if i go back and do linear regression

1:14:21

the equation of the best fit line will be somewhat like this or if i convert it to the study

1:14:28

hours and exam score story it'll be like hours i'm sorry uh score will be equal to

1:14:39

7.5 times hours plus 45 this your story

1:14:47

what it means guys so slow

1:14:51

is 7.5 that means for every one unit increase in the hours so for every one hour that you

1:15:00

study more if a one hour on an average you are getting 7.5 more marks so that is actually a lot

1:15:09

isn't it so we study hours so in the day limited up going to 10 hours say that i mean people

1:15:15

study for more than 10 also but we are keeping that as a cap so even if you study one hour more

1:15:19

that's a big deal

1:15:20

so that is a noticeable pattern one hour you can achieve a lot actually so on an average

1:15:26

we are able to say that for every one hour extra that you study for every one hour more that you

1:15:31

study you are getting on an average 7.5 more score and the baseline score is 45

1:15:37

if you're just saying like don't treat that as a but i'm just saying like you know this could be

1:15:43

could be that there's some places where there's a marking scheme even if you don't study anything

1:15:48

even if you don't study anything you can do guess

1:15:50

work exam in whatever you do you will still get 45 one of you imagine you know school

1:15:55

time we have those practicals right a theory exam in whatever you do doesn't matter practical

1:15:59

where people will still get 30 and pass 40 you will get and you will pass theory maybe doesn't matter

1:16:05

so that is like what it is no so even if you study nothing you will get 45 and for every one hour more

1:16:11

that you study you are getting 7.5 more much okay so the key concept the reason why i stressed on this

1:16:19

idea is interpretation interpretation interpretation this is

1:16:23

interpretation kind of both important so whatever equation you're getting equation

1:16:27

the equation to ban jayton in one line of four we will see that shortly okay

1:16:30

equations are interpret how you're important thing okay okay

1:16:33

so i will keep this i will keep this light visible i will keep this part visible and what

1:16:40

i will do now um just a minute guys let me see okay let me let me take you down

1:16:49

to the actual python code here it goes

1:16:55

this your linear regression is same story nothing to talk about and you can see the answers

1:17:00

are closely matching so i'm

1:17:02

this guess work here just many this 7.5 this guess work

1:17:05

but you see you're look back match

1:17:07

so what are we doing here we are segregating the data in python we have seen this

1:17:12

story already study hours x exam score y

1:17:15

okay train test split all familiar train test split

1:17:19

x train x test we are splitting the data into training and testing and here is where

1:17:26

we are using linear regression this is the part of the code where we are using linear regression

1:17:31

this is the part where we are using linear regression algorithm and this is coming from cycid

1:17:38

learn SK learn is the machine learning library in python

1:17:42

we've seen other other things used until now if you remember we were able to use uh train test

1:17:49

split from sk learned we were able to use the min-max scalar from sk learn

1:17:53

hana and today we are using something called linear regression from sk learn

1:17:58

this linear regression is the algorithm that is used to find that best fit line

1:18:03

that is what is used behind the scenes and we are focused on the python

1:18:06

implementation only we are seeing the python implementation that we're

1:18:10

visually we've seen that best fit line what is right and this is the python

1:18:14

interpretation of how it is happening so you use a linear regression

1:18:19

and remember we always fit on the train data you have your x-rain y-train you will do model

1:18:24

dot fit on x-rain y-train you will train the model and this is the coefficient and intercept of the

1:18:28

model so model equal to linear regression dot fit x-train comma y-train

1:18:35

you've got fit x-train comma y-train you learned the model and you find out

1:18:41

that model's coefficient what is intercept what you

1:18:44

look cof underscore is the code intercept underscore is the code whatever i

1:18:49

just a step back here here

1:18:51

what we've explained

1:18:52

best fit line by

1:18:54

this is the best fit line parameters

1:18:56

are now

1:18:57

model trained successfully

1:18:59

this is 7.87

1:19:01

so we can change the story here

1:19:03

because we have got exact

1:19:04

now

1:19:05

so here actually has 7.87

1:19:07

let me change the story this is going to be

1:19:10

7.87

1:19:12

this is going to be 7.87

1:19:13

this is 7.87

1:19:15

this is 7.87x plus

1:19:17

37.66

1:19:18

or here okay 7.87 hours plus 37.66.

1:19:27

Everyone is able to see that.

1:19:29

So what it means is and based on whatever equation we have learned, based on whatever model we have built,

1:19:37

we can now calculate the training score and the testing score.

1:19:40

This also we have studied before.

1:19:42

In our basic, in our basic machine learning session, we have

1:19:48

we have discussed what is training score and testing score.

1:19:50

What is the meaning of training score?

1:19:52

Training score means how well the model is doing on the training data.

1:19:56

And testing score means how well the model is performing on an unseen question paper.

1:20:01

So this is your training accuracy or testing accuracy.

1:20:05

So training accuracy

1:20:06

how well the model is performing on the training data?

1:20:09

Train data,

1:20:10

what the text book is.

1:20:11

Train data how is the model doing?

1:20:13

How is the model performing on the textbook?

1:20:16

That is how that is what is the

1:20:18

training score how is the model performing on the text book okay this is this is

1:20:24

the training score so sometimes what happens is after you study the concepts

1:20:29

you want to do revision so training score is like that revision accuracy

1:20:33

who revision can type how the model is performing on the train data but the

1:20:37

wapas see what textbook when you're revising how well you're doing that is 94% and testing

1:20:42

score means how well the model is scoring on the testing data x test y test on the

1:20:46

mock question paper okay so we have seen this code before and mock question paper it is doing 93

1:20:51

so we can say reasonably good quality model but we will get deeper into this in a way but right

1:20:59

now 94% training 93% testing we can say it's a decent model but we will see this in more detail

1:21:05

we will discuss this okay this is a decent model we are able to see and we have also

1:21:12

discuss the interpretation most importantly we have we have talked about the interpret

1:21:16

we understand what it means now the interpretation we have talked about

1:21:21

okay i hope everybody is clear everybody is conceptually clear about this thing now

1:21:27

there is another very interesting concept called residuals now what is the meaning of a residual

1:21:33

residual basically means what is the difference between and guys just to clarify

1:21:41

uh this is a like hours and score example that i gave you

1:21:46

you can also try to relate to a caggle exercise this is a very real world cagull problem

1:21:52

you you can see where the same salary kind of data is given to you not very hard right i mean

1:21:58

you can see how easily you can do these things now so you have data here let's say you're working

1:22:03

in a company and hr department in you gave you this experience is this salary

1:22:09

it's this experience it's this salary you can build a model right not very hard not very hard i think

1:22:14

this is given in month monthly salary you're your monthly salary

1:22:18

is your monthly salary data this is the historical data of all the

1:22:24

employees in the company so you can easily build a regression model using this data

1:22:27

so these external references i keep sharing in the code files now coming to

1:22:34

something about residuals residuals what is the meaning of residual is nothing but the

1:22:40

difference between the actual score and the predicted score why

1:22:44

actual minus y predicted is what is called the residual okay why actual minus y predicted

1:22:51

is what is called the residual excuse me that is what residuals uh basically mean okay now

1:23:02

let us understand this pictorially and visually what is going on take it let us understand

1:23:08

this pictorially residual is nothing but the difference between the

1:23:14

actual and the predicted so guys all of you remember all of you remember let me show you

1:23:22

visually if you see it visually it will make it uh you know it will make it a lot more clearer to

1:23:27

understand visually if you if you look okay so if you understand this visually this is

1:23:34

visually this is how we build the best fit line okay this data is and on this data

1:23:39

we were able to find the best fit line

1:23:42

this is our best fit line okay on this particular data there is the actually it

1:23:49

is 37.6 so we can uh we can actually start from here once again 37.6 sort of

1:23:56

it will go somewhat like this there is the best fit line okay all if you can see now

1:24:05

this is your equation is the equation of your equation of your best fit line

1:24:10

this is usually the predicted value right all the actual values are the actual data points i will

1:24:19

use a different color guys let me is a different color this is like your y a this is your y actual

1:24:26

he an a y actual and on the line you've got y predicted why predicted is always on the line

1:24:34

that means for a certain value of x what is the predicted value of y so recidual is nothing but

1:24:40

the difference between these two you're your residuals

1:24:45

the difference between these two is the residual you're your residual

1:24:48

sorry i think here you have been line draw here

1:24:51

let me just change it back to draw this is the residual

1:24:55

this is the residual here your residual here is the residual

1:24:59

this is the residual okay this is the residual

1:25:04

okay this is the residual here your residual

1:25:06

so the distance between the actual and the

1:25:10

the predicted on the line is what is called a residual. So I think I can show a slightly better

1:25:16

diagram. Google, there's some couple of nice diagrams we can relate to. Let me show you.

1:25:29

Just to show you pictorially what is this. Okay. You can't right. Pictorially

1:25:33

someajal, so very simple thing. Both simple thing. Not at all hard. And there are so many nice diagrams in Google.

1:25:39

I'm just trying to figure out which one to show you because all of them are very good.

1:25:43

All of them are very good. I think this one is a nice one. You can see this one. Here the concept is also very

1:25:49

nicely explained. So positive and negative care. Let's let's see that. Sorry. Uh, uh, uh, uh, look at this

1:26:01

all of you. This is your data. It's your data. X, X, X, X, S is. S. You find the best fit line. So this is

1:26:09

think what I was talking about. This is your actual data points. Y, why actuals? So if you

1:26:19

this point, okay. This is your ya. Why actual is. And it's your correct. And it's the

1:26:26

corresponding X. Mano, its x value is 7. 7 or 8. So for this X, what is the predicted

1:26:32

Y? Predicted Y? Predicted Y always line. So model will predict. This model will predict. This

1:26:37

This line may go. This is predicted. So this is what is called a residual. Residual is always the

1:26:43

difference between actual and predicted. So this is called a positive residual. The actual is more than

1:26:49

predicted. Here here. Now, look, actual here. This is the why actual. This is the why actual. And what

1:26:57

is the why predicted? Why predicted is on the line. So this distance between actual and predicted is called

1:27:03

the residual. Obviously the part of the starting example.

1:27:07

last in the first we discussed. All the points were on the line, here

1:27:11

there's zero residual. But in practical, real world scenario, residuals will never be zero. So

1:27:17

residuals from what can tell you? What do you know? Residuals are the quality of the model.

1:27:24

You can also identify which data points are not correctly predicted. There can be lot of

1:27:30

cases where we can see, yeah, these are able to estimate very well. This point seems to be very

1:27:37

different. I mean, here error could

1:27:39

is a

1:27:41

outlier. Maybe it's an outlier.

1:27:43

So we will investigate more.

1:27:46

This is where

1:27:47

residuals help.

1:27:49

Okay. So if I, if we come back to our current example,

1:27:52

you, look at it. If you

1:27:55

take a look at it, so

1:27:56

first we have, we have data.

1:27:59

Train test plate, we made model

1:28:00

all this we discussed, model. We have done.

1:28:03

And remember, we always fit the model

1:28:05

on the train data. And we always fit the model on the train data. And we

1:28:07

always go back and do prediction on the testing data same story right so we

1:28:12

will always go back and do dot predict on the testing data so on the X test we

1:28:17

are doing model dot predict on the X test okay and now we are creating a

1:28:24

data frame where we will compare the reality versus the prediction but

1:28:29

we will simply compare why a and Y P simple guys so residual

1:28:34

is nothing but actual minus predictive

1:28:37

and this

1:28:39

final data frame will look like this.

1:28:43

This is study hours, X,

1:28:46

this your actual score

1:28:47

YA, this your predicted score

1:28:50

what the line is predicting

1:28:52

what the straight line is predicting

1:28:55

and this is residual

1:28:56

the difference between actual and predicted.

1:29:00

And the important thing here is

1:29:02

is, this is important thing here is to

1:29:06

understand

1:29:06

how off we are from the actuals.

1:29:10

So you can identify, for example, look at this one.

1:29:14

You can see some cases where

1:29:16

the biggest mistake you can identify.

1:29:19

So there was actually a student who studied 7.7 hours.

1:29:23

The predicted was 98.36 marks.

1:29:28

Lekin his actual 10 marks. So we were off by 12 marks.

1:29:32

We've been off by 12 marks.

1:29:33

We've made 12 marks.

1:29:35

So that is a very, very big.

1:29:36

error. So these kinds of things we can

1:29:38

identify. That means

1:29:40

which are those data points where the model is

1:29:42

making the largest mistakes?

1:29:45

And if we can identify that properly,

1:29:47

we can do what we can,

1:29:48

we can fix fix can.

1:29:50

So we can, if we know,

1:29:52

the year's all cases in the model is not doing that well,

1:29:56

we'll fix can. So that is the main reason

1:29:58

for working with recidivals.

1:30:01

So the concept should be clear to all of you.

1:30:02

Everyone should be, you know,

1:30:04

very, very clear with the basic

1:30:06

idea. The concept should be clear.

1:30:36

So, we'll do another very interesting problem here.

1:30:53

And this time, what we will do is we will talk a little bit about,

1:30:57

we can fix it by doing residuals.

1:31:00

Akshat, residuals if fixed n'h, residuals, we are trying to understand the issue.

1:31:04

When we do residual, we are trying to understand the issue.

1:31:06

understand which are those data points where the maximum mistakes are getting made.

1:31:11

Fixed how can't. To fix, we need to go back and build a separate model.

1:31:16

Maybe we have to pre-process the data. For sure if that data was an outlier,

1:31:20

so whatever student we saw,

1:31:22

the student's prediction was coming so different.

1:31:25

It could for that student, you know,

1:31:28

could be was that student's data we got to

1:31:30

or that student's data we got out of.

1:31:32

Yeah, that student's other features that we've considered

1:31:34

not here. So it is very clearly a sign of an outlier.

1:31:39

So now we can fix it by handling that outlier.

1:31:44

Wapest from model

1:31:45

we'll make. Wapest the residual calculate

1:31:47

kareg and we should now observe that in the second try, the residuals would have reduced.

1:31:53

That is the idea. That is how we work towards it.

1:31:56

Okay?

1:31:57

So, understand.

1:32:04

So, guys, we can take a short break at this point in time.

1:32:09

Okay, 9.20.

1:32:10

So after the break, the agenda would be to walk you through.

1:32:14

So this was basically a simple linear regression where we are only one X and one Y.

1:32:20

One X is.

1:32:21

On the basis, you're trying to predict a Y.

1:32:23

After this, we will look at something called multiple linear regression,

1:32:27

where there are multiple Xs and based on that, you are trying to predict what is the Y.

1:32:32

And based on this, we will discuss.

1:32:34

The concept of overfitting and underfeiting.

1:32:37

Very important concept, overfitting, underfeiting or baseline concept and discuss

1:32:41

what is the baseline?

1:32:43

We will talk about the concept of a baseline.

1:32:45

So these are going to be the main discussion points after the break.

1:32:50

We'll do some exercises today after the break.

1:32:52

Majorly, it will be exercises on hands on we will do.

1:32:55

So I will see you back after the break.

1:32:57

Five minutes, ten minutes we can take and we can come back.

1:32:59

Okay, we'll resume.

1:33:04

Thank you.

1:33:34

Thank you.

1:34:04

Thank you.

1:34:34

Thank you.

1:35:04

Thank you.

1:35:34

Thank you.

1:36:04

Thank you.

1:36:34

Thank you.

1:37:04

Thank you.

1:37:34

Thank you.

1:38:04

Thank you.

1:38:34

Thank you

1:39:04

Thank you

1:39:34

Thank you

1:40:04

Thank you

1:40:34

Thank you

1:41:04

Thank you

1:41:34

Thank you

1:42:04

Thank you

1:42:34

Thank you

1:45:04

Okay, welcome back all of you.

1:45:08

We'll start on.

1:45:09

We'll start on.

1:45:11

And so far we have discussed on.

1:45:13

And so far we have discussed about the concept of the

1:45:15

of performing regression using a single variable.

1:45:20

And now we will first start our discuss this use case with a, you know, like in the real world

1:45:27

we never do predictions using a single X.

1:45:30

We always have more than one use case with a, you know, like in the real world if you look at it, we never do predictions using a single X.

1:45:31

We always have more than one inputs.

1:45:33

And the game.

1:45:34

great use case is this. In fact, this will be part of our, this will actually be part of our case study. So we will be seeing this shortly.

1:45:47

But in the real world, imagine we are trying to predict the price of a house. So the price of a house is impacted by multiple factors. So the price of the house is impacted by the square feet, but

1:46:04

the size of the house, the number of bedrooms, the age in years,

1:46:09

this your entire data right?

1:46:12

And if you want me to show the data frame,

1:46:15

this is how broadly the data frame will look like.

1:46:18

Let us see that.

1:46:19

This your real estate data.

1:46:21

So, this your real estate data, right?

1:46:24

All if you can take a look at this.

1:46:26

That's your real estate data.

1:46:28

And that is how a lot of real world data will be.

1:46:31

But the story demands the same.

1:46:33

The way we are going to do machine learning and modeling on this data will remain the same.

1:46:38

The concepts don't change.

1:46:40

This is your X1, this is your X2 or your X3.

1:46:43

At the end of the day, everything boils down to problem framing.

1:46:46

First machine learning session that we did right.

1:46:49

This is your inputs.

1:46:50

You have identified.

1:46:52

What are?

1:46:54

What are?

1:46:56

This inputs?

1:46:57

This output number.

1:46:59

We have to predict this based on these features.

1:47:01

That's it.

1:47:02

Straightforward.

1:47:03

That's the problem statement.

1:47:05

Next,

1:47:07

the same thing.

1:47:09

We just separate what is X, what is Y?

1:47:13

Train test split, same story.

1:47:16

And we do linear regression on this data.

1:47:21

Okay?

1:47:22

And we find out training score and testing score.

1:47:24

That's the concept.

1:47:26

So this is how we have learned something called multiple linear regression.

1:47:30

What do we call it?

1:47:32

We call it multiple linear regression.

1:47:33

Multiple linear regression means the prediction isn't just based on one input, but the prediction housing price is based on multiple inputs.

1:47:42

There are multiple features.

1:47:44

When multiple features use to predict the Y, we call it multiple linear regression.

1:47:50

So what is the other kind of regression called?

1:47:53

The simple one that we did.

1:47:55

And as you rightly says, we call it simple linear regression.

1:47:58

We call it simple linear.

1:48:00

Single name, by the way, we call it simple.

1:48:02

Simple linear.

1:48:03

regression. This we don't do much in practice. This is using one X, one X variable.

1:48:10

If you have a single feature, then simple linear regression

1:48:14

say it.

1:48:15

If you have multiple features, then multiple linear regression

1:48:18

So just keep this at the back of your mind on a few.

1:48:24

Now we'll come to the next concept.

1:48:26

First, we will do a case study.

1:48:29

And that case study basis we'll be discussing a very, very important.

1:48:32

A very important concept, overfitting, underfitting and good fit.

1:48:35

So, so first before we get any deeper, let us do this particular Kaggle case study.

1:48:41

You don't have to solve it. I have already shared with you the solution.

1:48:47

So, but the concept will be very, very interesting here.

1:48:51

And I'm pretty sure after we discuss this case study, you'll be able to relate to the concepts a lot better.

1:48:57

Now conceptually, you can't actually see how good.

1:49:00

So this is the California.

1:49:02

housing prices data set. It's a real data set. It is derived from the 1990 California census.

1:49:08

So 1990 in California state, a census

1:49:11

where this data set out. So first, before I start discussing the case study,

1:49:16

all of you go to the Kaggle website and give it a read.

1:49:21

See, my other objective is I want you to make, I want to make all of you very, very comfortable

1:49:26

to solve these kinds of exercises.

1:49:29

So these are all real exercises, right?

1:49:31

And companies are evaluating people based on Kaggle.

1:49:35

So you should be confident that, okay, we have learned the concept, we can do some normal class exercises.

1:49:41

And you can also go to places like Kaggle where, you know, a lot of enterprises and a lot of open source, other enthusiasts, other machine learning researchers, they share real data sets.

1:49:53

And on that also, you're able to solve the problems.

1:49:56

So that is how I, you know, I encourage everybody to study.

1:50:00

So definitely in the classes, we will keep doing these kinds of exercises.

1:50:04

But even when you're studying by yourself, try to go to Kaggle, try to explore different types of problems.

1:50:10

Using whatever methods I taught you, try to look up a similar use case, a similar data set based on your field of interest and try to build a model.

1:50:18

T.K.K.K.K.K.K. Okay, just that you have IPL's a data set in Kegel in. And IPL data set. You have something called IPL data set.

1:50:27

Very interesting. This is an IPL complete data set.

1:50:30

All the way from 2008 to 2025.

1:50:33

So you have data.

1:50:35

Now, you can go back and you have the entire ball by ball, match by match level data we have got.

1:50:42

Event name, batting team who are, bowling team what is the ball? Was it a four? Was it a six?

1:50:49

Okay, who was the batsman? So we have got like hundreds of features.

1:50:54

Non-striker, player out, reviewed, all this. And maybe one good use case could be you want to use. You want to use.

1:51:00

this data and build a and do a match prediction match prediction so based on the historical data

1:51:06

you want to look at whether a particular team will win or lose and IPL just a match

1:51:11

predictor. So these are some very good personal projects people can do right so I really

1:51:17

encourage people to work on these kinds of projects but look see one thing is you're studying the

1:51:22

topics you're learning the concepts with us right and the second thing is how can you

1:51:25

parallelly build up your resume so you say exercises you try to you try to

1:51:30

you know put it up on github you try to put it up on some social profile and then you can claim that yes

1:51:36

you know if if you're a fresher you cannot get experience this way but what you can do is you can claim that

1:51:41

you worked on similar problems and that will be a great great experience for you so people you can say that

1:51:46

this is what i worked on all right everybody please go to the uh

1:51:50

california housing prices data set take two minutes and go through the exercise all of you just read

1:51:55

through the problem read through the problem statement read through the context and

1:52:00

and please go through this data set understand the columns what are the columns that are

1:52:03

given at a very high level so take two to three minutes please a very big part of doing machine

1:52:09

learning is to understand your data it's a very very crucial phase so everybody give it a read

1:52:15

please then i will discuss the solution in all of you give it a read please

1:52:30

you know.

1:53:00

Thank you.

1:53:30

Thank you.

1:54:00

Thank you

1:54:30

Thank you

1:55:00

Thank you

1:55:30

Thank you

1:56:00

Thank you

1:56:30

Thank you

1:57:00

Thank you

1:57:30

Thank you

1:58:00

all

1:58:04

I hope you have

1:58:05

I hope you have

1:58:07

to go through the data.

1:58:10

I will go through the data.

1:58:14

I will walk you through it briefly.

1:58:15

I will walk you through it briefly.

1:58:29

What is it?

1:58:30

In case you are going through it just I'll give it a minute more and just read through this

1:58:35

point and if you scroll a little bit down you can see the descriptions of the columns are given here.

1:58:41

Columns what is what is the input what is the output.

1:58:46

Okay so we are trying to build a model to predict the median housing price based on all these features.

1:58:53

That is what we are trying to do and this could be very useful in the context of you know companies like magic bricks

1:58:59

99 acres, these kinds of companies which are, you know, looking to predict real estate prices.

1:59:06

So based on the features of the house, we can predict what is the price of the house.

1:59:13

Take us all of you just take a minute more.

1:59:29

Thank you.

1:59:59

Thank you.

2:0:29

Thank you.

2:0:59

okay

2:1:06

So,

2:1:07

we are looking at the house and the house and the features of the house are latitude,

2:1:14

the house are latitude, longitude.

2:1:29

the housing age, total rooms, total bedrooms, population, household and income.

2:1:37

And based on that, we are trying to predict what is the median housing value.

2:1:41

Actually, a district level data.

2:1:42

If you're you're a data go to look.

2:1:43

It's not exactly a housing level data.

2:1:46

It is actually data that is pertaining to houses found in a given California district.

2:1:54

So this understanding both important.

2:1:57

So if any problem when we are working, we should understand what is one row.

2:2:02

What is the meaning of each and every row?

2:2:05

Right?

2:2:06

What is the, you know, what is the meaning of each and every row?

2:2:12

That is the important thing.

2:2:13

So every row stands for one particular district in California.

2:2:18

So that is what we are having.

2:2:21

And this is a very popular data set.

2:2:24

So we are loading the data set directly from science.

2:2:27

it learned. So of course we can download the data and we can load it as a CSV.

2:2:31

But this data already available.

2:2:33

SK learned data sets, the data is already there.

2:2:36

So we are simply loading the data and we are separating what is X and what is Y.

2:2:42

That is the straightforward thing we have done first.

2:2:44

And now, look, same data is.

2:2:46

This is your input, income, housing age, rooms, bedrooms,

2:2:51

population, latitude, longitude.

2:2:54

Every row stands for a particular particular

2:2:57

district in California based on these features of the district you have

2:3:03

x1 x2 x3 x4 like that you want to predict what is the Y okay okay so this is the

2:3:08

problem we are trying to solve so first what are we doing

2:3:12

so first we are going ahead and building a linear regression model straight forward

2:3:16

so we know we have trained test lit here

2:3:20

that we've been in the min-max scale is actually a very very useful thing to be done here

2:3:24

why because if you if you're up here data go

2:3:27

you will observe that the data is in very very different scales.

2:3:31

So, so first, latitude, longitude, the latitude values are in minus 100.

2:3:38

You look here on average occupation 2.1, 2.2.2 is

2:3:42

is in thousands.

2:3:46

Median income is like in 1 to 10 range.

2:3:49

Average bedrooms are more be come.

2:3:51

Housing age is like in 10, 20, 30 is like that.

2:3:53

So the data is in very, very different scales.

2:3:57

And scaling why do we do what did I teach you?

2:4:02

We try to do scaling to ensure that all the features are given equal importance.

2:4:11

It's not that any feature

2:4:12

that feature's value is more, then it's more importance.

2:4:15

No.

2:4:16

So we try to bring all the features to the same scale.

2:4:21

We try to bring all the features to the same scale.

2:4:25

That is the whole idea where.

2:4:27

scaling actually comes in, right?

2:4:29

So we are doing min-max scalar.

2:4:31

Fit transform, transform, same story.

2:4:34

And we are building the model.

2:4:37

You can see, it takes a little time and we are getting this kind of an accuracy.

2:4:41

Now, there is something new I will teach you in the court part today.

2:4:45

If you here here, we'll look at it, we've made it manually

2:4:47

kind of manually done.

2:4:50

So, first we min-max scaleed, then then then

2:4:52

then, then, then, then, then, then, then, then, then,

2:4:53

again, linear regression, if you want to see this slightly better,

2:4:57

way, we can also go back and use a pipeline in SK learned.

2:5:01

A pipeline is actually a better way to bundle multiple steps together.

2:5:05

Okay?

2:5:06

So, so what we are doing, manually scaling the data and feeding it to the model takes multiple

2:5:12

steps and introduces the risk of data leakage.

2:5:18

You can take a look at it.

2:5:19

This is what we were doing before.

2:5:20

Minmax scalar, way fit transformed here.

2:5:23

Test per we transformed here.

2:5:25

Us k'a, model dot fit, linear,

2:5:27

integration in scale data. So it's a multiple steps we are doing, right? It's difficult.

2:5:31

So rather than that, we're a pipeline

2:5:33

are making. And in the pipeline, we are saying that first we will do

2:5:39

min-max scalar and second, we will do linear regression.

2:5:43

Simple, right? And this only min-max scalar can't mean, you can

2:5:46

do the main-max scalar, you can here, you can do the encoder, you can do scalar, you can do

2:5:50

simple imputer. Last class we have simple imputer discussed

2:5:53

that, you can have multiple steps in a pipeline.

2:5:57

This is a pipeline where you are defining what are the things we will do.

2:6:01

So, first we will do min-max killer,

2:6:03

then we will do linear regression.

2:6:05

So you are defining the steps in a pipeline.

2:6:07

Okay?

2:6:08

So pipeline defined again.

2:6:10

Next, you will simply say dot fit, X-ray and Y-train.

2:6:13

And you will say dot score, and you will get these results.

2:6:16

The answers will be exactly the same.

2:6:18

Now, look, here we have without pipeline here.

2:6:20

Here we have with pipeline here.

2:6:21

The answers are exactly the same.

2:6:24

But the code is much, much smaller.

2:6:26

hardly a few lines of code.

2:6:29

Okay.

2:6:30

Use case number two, like this next point that I want to talk about is

2:6:34

when you look at this data,

2:6:37

when you look at this data, when you

2:6:38

you're, when you're looking at,

2:6:40

ultimately, what are we trying to do in ML?

2:6:42

We have some data.

2:6:43

Like here here we have California data.

2:6:46

We are using some algorithm

2:6:48

and we are building a model.

2:6:50

Right?

2:6:50

That we're doing all this way.

2:6:53

Now, my question to all of you is,

2:6:56

let me hear some general answers.

2:6:58

My question to all of you is,

2:7:01

when you see training accuracy of 61%

2:7:03

and testing accuracy of 58%

2:7:06

what can you say?

2:7:09

What can you say about the quality of the model?

2:7:15

Very open-ended question.

2:7:17

What can you say about the quality of the model?

2:7:19

61% training, 58% testing.

2:7:24

What can you say about the quality of the model?

2:7:26

So, can we say it is good?

2:7:38

So, good be both relative

2:7:39

is a very relative concept.

2:7:43

So, well,

2:7:44

so, 97% be good not.

2:7:47

If your model accuracy 97% percent

2:7:48

is not, then people will ask the 99%

2:7:52

who are, so good is a relative concept.

2:7:55

Good is a relative concept.

2:7:55

Good is very, very.

2:7:56

But generally speaking,

2:8:01

I mean, moderate,

2:8:02

generally speaking, I think we all will agree

2:8:05

that this is not a good quality model.

2:8:07

I mean, it's said the better

2:8:08

can't.

2:8:10

58% test accuracy

2:8:12

what is?

2:8:13

That means when you go and evaluate this model on a test data,

2:8:17

when you go and evaluate this model on a test data,

2:8:17

when you a mock question paper solve

2:8:19

that mock question paper in you

2:8:21

have 58% answers correct.

2:8:24

That is not good, right?

2:8:25

We should try to.

2:8:26

make it better. Now what we are trying to do is we are trying to introduce some some new

2:8:34

terminology and more specifically I'm introducing the concepts of overfitting,

2:8:40

underfitting and good fit. Okay guys. While I talk about this thing. Everybody

2:8:48

give it a glance. I will again pause for two minutes. This will be the final concept in

2:8:53

the session. But everybody give it a glance please.

2:8:56

and and I will intentionally hide this portion so that you are not confused, okay?

2:9:03

Let me hide this portion so that people are not confused.

2:9:10

Okay, just give me one second.

2:9:17

Yeah, this one part I'm hide.

2:9:19

Okay, don't worry about this thing. Okay, it's go, don't worry.

2:9:26

I will hide this portion and I will also hide this portion.

2:9:32

Everybody take a minute, okay? Just take a minute. Just take a minute, glance through it once.

2:9:36

X axis go sumjo, Y axis go somejow. Look at underfitting, overfitting, good fit.

2:9:42

Tino terms go sumjo. Take a minute, I will discuss. Okay? Everybody. Just look at the screen,

2:9:47

all of you, for a minute.

2:9:49

What are we discussing right now?

2:9:51

Now we know how we know how to train test fit how it?

2:9:53

we know.

2:9:57

Free processing how it is?

2:9:59

Encoding, imputation, scaling.

2:10:03

We also know at a pipeline

2:10:04

how to build a linear regression model.

2:10:09

This continues in the next class, obviously.

2:10:11

But we know at a basic level how to build a model.

2:10:13

So what are we doing right now?

2:10:15

We have model to baned now.

2:10:16

Now we are discussing how to evaluate a model.

2:10:18

How do we evaluate that model?

2:10:21

What do we evaluate that model? Was the 61% or 58%

2:10:23

And Raya, that is what we are discussing. Model evaluation right now.

2:10:27

Okay?

2:10:28

Everybody, give it a glance for a minute.

2:10:53

Thank you.

2:11:23

Thank you.

2:11:53

Thank you.

2:12:23

Okay.

2:12:53

I will discuss this, but before I start my conversation,

2:12:57

Y axis, what is why is why axis?

2:12:59

What is y axis?

2:13:01

Why axis stands for error?

2:13:04

So error is basically nothing but inverse of accuracy.

2:13:09

If a model

2:13:11

10% error, that means it is 90% accurate.

2:13:16

Okay, you're building a model on some data

2:13:19

and you're getting 90% accuracy.

2:13:22

So 90% accuracy equivalence to is equivalent to 10% error.

2:13:27

Think of it that way.

2:13:30

Excuse me.

2:13:33

90% accuracy is equivalent to 10% error.

2:13:38

Okay.

2:13:40

So

2:13:42

Y axis is error.

2:13:45

Let's start with underfitting first.

2:13:47

Underfitting what is.

2:13:49

Underfit models are those models whose training

2:13:52

error and testing error are very high.

2:13:55

So training error or testing error are

2:13:57

high.

2:13:58

Meaning training accuracy or testing accuracy

2:14:01

both low.

2:14:03

That means whatever models you are building,

2:14:07

those models are giving very poor performance

2:14:11

on the training data also and on the testing data also.

2:14:16

Okay?

2:14:17

This is your underfeiting.

2:14:20

So whatever models you are building,

2:14:21

models you are building those models are giving very poor performance on the training data

2:14:28

as well as on the testing data that is what is referred to as underfeiting.

2:14:34

So it is like saying it is a very poor quality model.

2:14:38

Very poor quality.

2:14:40

You're using those patterns,

2:14:45

training data maybe we are getting a very poor result.

2:14:48

Testing data maybe we are getting a very poor result.

2:14:50

poor result. So it is a very poor quality model. That's the intuition of what underfitting refers to.

2:14:58

So you can train maybe if you go and evaluate your model on a textbook, you are getting a very low accuracy.

2:15:07

Even when you go and evaluate that model on a mock question paper, you get a very low accuracy.

2:15:13

It is a very poor quality model.

2:15:16

That's the intuition.

2:15:20

coming to overfitting. What is overfitting? What are we, so what is the idea behind overfitting?

2:15:28

Overfit models are those kinds of models whose train error is very low, but the corresponding

2:15:38

test error is very high. That is how we go back and define overfitting. So overfit models

2:15:45

are those kinds of models whose train error is very low.

2:15:50

And test error is very high.

2:15:52

You can it.

2:15:53

You can't alter accuracy as if you can't train accuracy high or test accuracy low.

2:15:59

That means on the textbook,

2:16:03

you're from where you're seeking,

2:16:06

if you try to revise, you are not making any mistakes.

2:16:11

You mean, you're, you're, you're not making any mistakes.

2:16:12

You mean, you, the textbook's things very well.

2:16:15

Whatever training data is given to you, you are able to learn that pattern very well.

2:16:20

But given an unseen test data, given an unseen test data,

2:16:29

given an unseen test data, when you're

2:16:31

new data, on that you're performing very poorly.

2:16:38

That your overfitting. Overfitting means like road learning.

2:16:41

Imagine you're studying a night before the exam.

2:16:45

So, what you're your topics,

2:16:47

you've got to do you have, you know, you're overfitting overfitting.

2:16:50

but whatever real questions are there, you're making mistakes.

2:16:57

So underfitting, you learn nothing.

2:17:00

You've got any other than you're not bad.

2:17:02

Textbook also bad. Mock question paper also bad.

2:17:05

And overfitting means, yeah, textbook too you remember very well.

2:17:09

Because you memorized it by heart.

2:17:11

But actual in you learned nothing because when some unseen questions are asked, you're failing.

2:17:16

So, both are bad.

2:17:19

What you're ultimately looking?

2:17:20

for is a good fit model. So good fit model is that model which has the lowest test

2:17:26

error. And this thing we're in machine learning. So today the focus was just on linear

2:17:31

regression, just on basic model building. But in practice, we'll

2:17:35

we'll show you. Although that is not in the course today, but I'll show you. Actually,

2:17:40

we're real in what we do. We take different, different, excuse me, we take different, different instances

2:17:46

of data. We build different different. We build different different.

2:17:50

different models, right?

2:17:52

We're linear regression model

2:17:53

we're, we're, we're allog, other models

2:17:55

and we try to choose that particular model

2:17:59

which gives the best results.

2:18:02

That is what we are broadly trying to do.

2:18:05

We are trying to build, we are trying to

2:18:07

finally, you know, choose that particular model.

2:18:12

We are trying to finally choose that particular model

2:18:14

which gives the best results.

2:18:17

Okay? And best results,

2:18:19

means the lowest test accuracy.

2:18:22

Whatever model we finally choose should give us the lowest test accuracy.

2:18:26

Test accuracy should be the lowest.

2:18:29

Okay. And that's the reason why I told you,

2:18:33

that's the reason why I told you, that good fit

2:18:34

no definition. So, it is very relative.

2:18:40

Okay? So, you can build a model and you can say the next model is more good fit

2:18:45

than the previous model. So all these three terms

2:18:48

underfitting, overfitting and good fit

2:18:50

are very, very relative.

2:18:53

If anybody asks you that please explain overfitting,

2:18:56

you generally explain to,

2:18:57

but if you a model

2:18:58

can you 100% say this an overfit model,

2:19:01

you can't say, you can't say,

2:19:04

yeah, you can't say, yeah, you can't say,

2:19:07

that this is more overfit,

2:19:08

this is more underfit,

2:19:10

yeah, this is more good fit.

2:19:11

You're model one or model two

2:19:13

compare and say whether it is relatively more

2:19:16

overfit,

2:19:18

more underfit, you are relatively more good fit.

2:19:21

So coming back to our story, whatever we were discussing,

2:19:26

this is,

2:19:28

this is generally can say,

2:19:29

that, well, this, this is an example of,

2:19:34

this is a, we are looking at a,

2:19:37

you know, a small example of what we call a underfit model.

2:19:42

How we're this to underfit model?

2:19:44

Generally underfit.

2:19:46

Okay, yeah, yeah.

2:19:48

It is a generally underfit model,

2:19:50

excuse me, because the training score

2:19:54

and the testing score both are low.

2:19:59

Can we make it better?

2:20:00

This is we make it better.

2:20:00

Yeah, he he's in machine learning in iteration one,

2:20:04

we've put a total data,

2:20:05

train test split,

2:20:06

we made, pipeline,

2:20:07

model,

2:20:08

all set,

2:20:09

61% and 58%.

2:20:11

Now what can I do?

2:20:14

A Aege we can go back and try to build a different

2:20:17

model.

2:20:18

We'll a example

2:20:20

how a new model

2:20:22

how a different model looks like.

2:20:24

So while I show this example,

2:20:26

you guys do not worry, don't worry about

2:20:28

this code.

2:20:29

So this we have not seen today, right?

2:20:31

But we will see this later on.

2:20:37

So gradient boosting regressor

2:20:38

name's a good algorithm.

2:20:40

Now, look, we're going to go,

2:20:41

we're doing what we're doing?

2:20:42

I have basically just copied and pasted this code.

2:20:45

I am simply going to replace linear regression

2:20:48

with a different algorithm called gradient boosting regressor.

2:20:52

This what is, please ignore.

2:20:54

This you have to know it.

2:20:55

We will see ensembles in the next to next week.

2:20:58

We will see.

2:20:59

For now you ignore it.

2:21:00

But this discussion is just to show you

2:21:02

the absolute fundamentals of machine learning that we have discussed.

2:21:06

What are the absolute fundamentals of machine learning?

2:21:09

You have data.

2:21:11

Data is nothing but X, X, Y, combination.

2:21:13

You have data on the data on uper

2:21:14

any algorithm,

2:21:15

and on the basis of that, you can build a model.

2:21:18

model.

2:21:19

This is your machine learning one-on-one concepts.

2:21:21

Now, if you remember, first we use linear regression.

2:21:25

Now we linear regression,

2:21:26

now we will keep everything else the same.

2:21:30

I will use something called gradient boosting regressor.

2:21:34

This is a other type of algorithm.

2:21:37

If you are intuitively,

2:21:39

if you're, sir, this is basically a non-linear model.

2:21:42

This is basically a non-linear model.

2:21:44

Like linear regression, what we do?

2:21:46

Linear regression is built a linear model.

2:21:48

but gradient boosting regressor builds a non-linear model.

2:21:51

So its accuracy can't.

2:21:53

If I have to show this in the code to all of you,

2:21:57

you can see very clearly the moment I do this

2:22:02

and when I hit enter, I will run the cell,

2:22:05

you will take a look at it that my training score

2:22:07

and my testing score both will significantly increase.

2:22:10

They have both significantly increased.

2:22:13

Can you see? Almost like magic.

2:22:15

Almost like magic.

2:22:17

So,

2:22:17

We have nothing changed

2:22:18

We have a new algorithm used

2:22:20

and we have managed to build a more good fit model.

2:22:24

This is what I meant in the last discussion.

2:22:26

So you're model one

2:22:28

you?

2:22:29

You're model two?

2:22:30

Excuse me guys.

2:22:32

And we can say that model two,

2:22:35

model two is more good fit than model one.

2:22:38

And more good fit

2:22:40

because

2:22:42

it is having a higher training accuracy

2:22:45

and it is having a higher testing.

2:22:46

And it is having a higher testing.

2:22:47

accuracy training data it is doing better and even on the testing data it is doing

2:22:52

better.

2:22:53

So that is the reason why we will say this is a more good fit model.

2:22:56

So this is the way how you build models in machine learning.

2:23:00

And Akshad has asked a question, uh, uh, uh, uh, uh,

2:23:05

okay, okay, great.

2:23:07

Uh, uh, correct, correct, correct.

2:23:09

Higher accuracy means lower error, correct.

2:23:11

Both are inverse.

2:23:13

And lower accuracy is higher error.

2:23:14

Exactly.

2:23:15

You, uh, you can't say, correct.

2:23:16

Right.

2:23:17

90% accuracy.

2:23:18

So you can't.

2:23:19

10% error.

2:23:20

Okay.

2:23:21

Okay.

2:23:22

Everybody is relating to this.

2:23:24

All of you.

2:23:25

Everybody is related to this.

2:23:26

So two important learnings here.

2:23:28

We have seen how to build a model.

2:23:30

And we have also discussed, very important.

2:23:32

We have discussed the concept of underfitting, overfitting and good fit.

2:23:36

Through this particular diagram.

2:23:38

Here there were other other things that was not relevant.

2:23:40

That's why I removed it.

2:23:42

But then the key idea should be clear.

2:23:44

Underfit.

2:23:45

What is?

2:23:46

fit?

2:23:47

Underfit means you learned nothing.

2:23:49

Training, testing, accuracy, both are

2:23:51

overfit means you learned training very well.

2:23:53

Or good fit is what we are aiming for.

2:23:54

Good fit models are those models which give you the highest performance on your test data.

2:24:02

All right.

2:24:16

And finally, the last of the ideas that I wanted to talk about right now is,

2:24:26

actually, this is an example.

2:24:28

We have given this in our notes and I wanted to share with you.

2:24:31

This actually does this very nicely.

2:24:33

This is also a very nice note which I wanted to share with you.

2:24:36

You look, here overfitting, underfitting,

2:24:38

underfitting, visually explained here.

2:24:40

Very nicely done, actually.

2:24:41

Very nicely done.

2:24:42

You can see.

2:24:43

This is your x-axis.

2:24:44

Okay?

2:24:45

You can it.

2:24:46

you can see

2:24:49

this is your

2:24:51

x-axis, y-axis are

2:24:53

based on the input we are trying to predict the output

2:24:56

underfit model in patterns

2:24:57

don't learn not are you see

2:24:59

this is the underfeit model

2:25:01

what are we trying to do in regression

2:25:03

we are trying to find

2:25:05

shake this is the thing

2:25:07

okay I think this diagram will make it very clear to you

2:25:11

this diagram will make it very clear to you

2:25:14

so underfitting means

2:25:15

you are not learned

2:25:16

the patterns at all.

2:25:17

You are not learning the patterns at all.

2:25:20

Okay?

2:25:21

So you are able to see that the line doesn't represent the patterns at all.

2:25:29

Overfitting means that whatever curve that you are building, we are able to perfectly fit

2:25:36

all the points.

2:25:37

We are able to perfectly fit all the points.

2:25:40

That is also bad because we are remembering sweet spot is this.

2:25:45

So this is the kind of model we are trying to build.

2:25:52

And the important thing here is what is referred to as generalization.

2:25:59

This is what we are mainly trying to do in machine running.

2:26:04

We have to generalize the things well.

2:26:09

We are not trying to exactly remember the pattern of the points.

2:26:14

here here here then it is like memorizing we don't want that too many this we don't

2:26:20

want that that's bad overfitting not required underfeiting you're not learning anything

2:26:24

that's also bad what we are looking for is the right generalization on an average

2:26:30

can I understand that by patterns can't so patterns are on an average like this

2:26:35

okay yes there are errors happening the the the curve is not perfectly going through

2:26:41

all the points agreed

2:26:43

there, some outliers, some outliers, there, residuals have, no problem, but we are able to broadly understand the patterns.

2:26:50

I hope this is clear.

2:26:51

Sheikh, I hope that answers your question.

2:26:52

Let me know, Sheikh, yeah, clear.

2:26:55

So generalizes well.

2:26:57

This generalizes well.

2:26:58

This is the pictorial way to understand what is overfitting, underfitting and good fit.

2:27:13

And the final idea that I wanted to clarify to all of you.

2:27:19

We have actually seen this before.

2:27:21

The final idea that I wanted to clarify to all of you here is the concept of a, the concept

2:27:27

of a baseline, what exactly a, what exactly a baseline basically is, right?

2:27:36

What exactly a baseline basically is, what is the meaning of a baseline?

2:27:39

So baseline basically stands for.

2:27:43

the average, what is the average performance?

2:27:49

That means if you do not build a model, on an average, what the results will be.

2:27:56

So I can take the same thing in my current example.

2:27:59

This your California housing data.

2:28:01

So, uh, what is a baseline model?

2:28:05

A baseline model is nothing but you take into account your entire why.

2:28:11

Why is nothing but the price?

2:28:13

You take the entire Y, this is your price, okay?

2:28:18

And, and you can take a look at this.

2:28:25

This sara Ys take all the Ys lay lo.

2:28:28

This is the average is, the average, y bar is, we mean,

2:28:31

we're, this is called a baseline model.

2:28:38

Okay, okay, it's kind of a baseline model.

2:28:40

Just I wanted to tell you what a baseline model is.

2:28:43

Otherwise, it's useless.

2:28:44

In practice, this has no relevance here.

2:28:47

You ultimately have to build a regression model to solve a real problem.

2:28:50

But just wanted to introduce to you so that, you know, in case you hear the term, you guys know what is baseline.

2:28:55

So baseline kind of meant to mean, it's an average.

2:28:58

But the average basis of we'll not work, right?

2:29:00

We have actually prediction.

2:29:02

We want to ultimately build a relationship between Y and the X's.

2:29:08

You will not find out the average.

2:29:11

And you will not say, okay.

2:29:13

On an average, the price will be this.

2:29:14

No.

2:29:15

But I want to look at the actual features of the house and predict what is the price of the house.

2:29:20

But just remember that a baseline model is nothing but the average.

2:29:24

This is the concept.

2:29:25

Otherwise, in practice, you will, you know, you will not be using this a lot.

2:29:29

Okay?

2:29:30

Shake, you want to see this in the code.

2:29:31

Yeah, code, no problem.

2:29:33

We here here here one two things, but that may not be so relevant.

2:29:37

But I can show you in the code.

2:29:38

Just you, you, you, you know, you're 80% or 78%.

2:29:41

Okay.

2:29:41

Let me do a couple of.

2:29:43

very interesting modifications right now.

2:29:46

You goad-wise ignore but conceptually you can look at it.

2:29:50

So, first, previous model comparison, this is a good fit.

2:29:53

This is a more good fit model.

2:29:56

Okay.

2:29:56

And what's that?

2:30:02

One second, I'll come to you.

2:30:04

So, you can actually go back and try to increase the estimators.

2:30:08

And as you will be able to see, you will be able to see.

2:30:11

you'll be able to see that the model will become more and more good fit.

2:30:18

You can take a look at it.

2:30:20

The model will become more and more good fit.

2:30:24

Now, 80, 78, and as you increase it,

2:30:29

this score barter jae,

2:30:31

and after a while, it might actually overfeit.

2:30:34

So this you will have to do and check, check.

2:30:36

So there's no easy way out.

2:30:37

We have to check this.

2:30:40

So, so it's no easy way out.

2:30:41

you increase the, if you increase the parameters too much and what these parameters are

2:30:45

again, we have not discussed.

2:30:46

We will see this in the next class.

2:30:48

But this is the intuition, that linear model's up underfeiting

2:30:51

is going to and the moment you use a different algorithm, a more powerful algorithm,

2:30:56

your better model was, but if you're much more jada, okay, then you go ahead, then

2:31:00

go overfit will.

2:31:02

That is the intuition.

2:31:04

It's still running right now.

2:31:05

And I think you will start to see some overfitting happening here.

2:31:09

Okay?

2:31:10

Yeah, actually, you want to ask me anything on that PDF.

2:31:11

right now what what you want to ask visual given in the PDF which one this one

2:31:18

which one what I explained here this one yet overfitting underfitting you want to

2:31:24

ask something please ask me what you want to ask what you want to ask to ask

2:31:29

to ask what you want to ask?

2:31:41

you can uh yeah so actually you want to ask something on this please let me know oh you want a

2:31:52

PDF this will be shared with you after every glass these notes are uploaded okay our team will

2:31:56

upload all these notes to you don't worry these are lecture notes say

2:32:00

these files to have up my end to share i i do some stuff i add some more things i share the code

2:32:06

files with you additional reference for sometimes we sometimes we use these are all our lecture notes

2:32:11

all this you will get don't worry okay by tomorrow only it will be uploaded

2:32:15

okay shake what i did here what i did here was i actually use n-stimators

2:32:24

thousand and i actually got 90% 83% you can you are able to see

2:32:32

this is a much better model 90% 83%

2:32:37

if you increase it even further

2:32:41

So actually it will take a lot of time.

2:32:43

you, you know, you've got it took a lot of time.

2:32:46

So I could have done it 10,000 to show you.

2:32:49

But you, you can estimate

2:32:49

can't you,

2:32:50

1,000 run to 20 seconds

2:32:52

so 10,000 in estimating it will take me

2:32:55

approximately 5, 10 minutes.

2:32:58

I'm not running this, but just to let you know,

2:33:00

intuitively, if you

2:33:01

this is 10,000 more

2:33:02

now you will start to see

2:33:05

that training score will start to increase,

2:33:08

it will start to become close to 99%

2:33:10

whereas testing will

2:33:11

start to drop, this 70%

2:33:14

you will start to see that pattern.

2:33:17

Okay, you can

2:33:18

you can run it later on, okay?

2:33:21

But then it was an improvement, right?

2:33:23

That's the important part.

2:33:24

Now, look, our linear regression is

2:33:26

this, gradient boosting,

2:33:28

baseline model I'm getting this,

2:33:30

at a very basic level I'm getting this,

2:33:33

okay?

2:33:35

78, 71, whatever number

2:33:37

77, 74, 74,

2:33:39

better than, better.

2:33:40

Better, and.

2:33:41

and I can improve that model further and further and further.

2:33:45

I'm able to improve that model further and further and further.

2:33:48

Again, do not worry what these things are,

2:33:50

but the idea is to tell you how we go about

2:33:53

building a better quality model

2:33:54

by trying different different parameters.

2:34:00

So, the final thing we did was this.

2:34:02

We actually built a basic gradient boosting model

2:34:06

or object safety compared to the previous model,

2:34:08

we had a higher training score and a higher testing score.

2:34:11

Take it?

2:34:12

Hello.

2:34:13

Guys, any questions?

2:34:15

I'm just going to open the floor for any questions.

2:34:17

If you have any questions, you can ask me.

2:34:19

So, anybody else wants to ask me any questions?

2:34:23

Any doubts, any doubts that you have

2:34:27

until now, whatever we have seen today in the class?

2:34:30

I hope everybody is clear.

2:34:32

Any questions?

2:34:33

I'll just go to pause for a few minutes here, for any questions.

2:34:36

So today what was the main focus?

2:34:51

The main focus area of the class was here.

2:34:55

We talked about, we just went ahead and looked at a very basic recap of what is regression.

2:35:03

We did a very basic regression.

2:35:05

Recap of what is regression.

2:35:06

regression. We already saw this in our problem framing class, but we had a very basic recap.

2:35:12

We had the intuition of linear regression, right? No formula nothing. No formula is required here,

2:35:19

but we had a very basic intuition. Best fit line, what is slope, what is intercept. We understood the

2:35:24

meanings of these terms. What is M? What is C? We also saw multiple linear regression, right? We also

2:35:30

understood what is fit and what is predict. We would train test split. How do we do that? How do we do that?

2:35:36

saw that we also at a basic level understood baseline and most

2:35:41

importantly overfitting and generalization okay we understood the meaning of what

2:35:46

is overfitting what is underfitting what is the good fit model and finally the

2:35:52

concept of residuals take these are things that will be covered later you can see

2:35:55

defer M a R M a R M S to a later session these are not part of today R squared and all will

2:36:00

be covered later in case some of you have studied kisar squared kya don't worry that will be

2:36:04

taken up later in fact the next session

2:36:06

we are covering ridge lasso r squared i will talk about that in detail in that session right but today the

2:36:12

the main idea the main idea of the session was to teach you at a fundamental level how to build a

2:36:18

linear regression model how do we build a linear regression model that was the main objective

2:36:23

okay any questions anybody else wants to ask me anything

2:36:31

so clear all of you are okay everyone's clear with the concepts

2:36:36

any final questions

2:36:40

okay thank you guys if there are no other questions i will uh pass it over to prattap for the

2:36:56

quiz and uh okay good night to all of you uh thank you thank you everybody i'll see in the next

2:37:03

session and we'll continue on with with

2:37:06

continue on with regression next session is also linear regression continued

2:37:11

so we'll see some more interesting ideas of linear regression in the next session all my

2:37:16

materials are already in the drive that you can access okay uh okay thank you good night guys

2:37:22

see you in the next class pritha over to you thank you yeah thank you sir for the lecture and thank you

2:37:30

students and today so i will be releasing the poll now

2:37:36

and after the poll is done you guys already know the drill once you complete the poll

2:37:44

join the menteometer quiz so i'm sending the link to a mentement request here

2:38:06

we have some interesting questions today so please join quickly

2:38:20

anyone who is not able to see the poll okay i think everyone is done all right

2:38:25

i'm ending the poll now everyone has voted all right guys please join we have

2:38:36

we have an interesting many meter quiz today only six people only seven

2:38:53

uh you can join using the link that i've given in the chat akshad

2:39:06

7 is like less than half the students here we have 15 students at least eight eight

2:39:15

nine students i would like okay uh in that case akshit just give me a second yeah join using

2:39:25

the QR code anyone who's uh who needs to join with the phone just join using the QR code say

2:39:32

done in the chat so i can just start

2:39:36

okay akshad if you are done scanning then just message in the chart

2:39:48

okay all right so i think we have oh okay great nine players fine let's start

2:39:59

okay anyone else who wants to join or uh anyone who wants to join or uh anyone who's trying

2:40:06

to join or do you want me to just start thumbs up if you want me to just start

2:40:13

okay all right first question why is predicting why is equal to one or two or three for junior

2:40:30

mid or senior not a regression problem

2:40:34

So remember we are we are predicting one, two, or three, which is continuous variables, right?

2:40:46

Why is that not a regression problem?

2:41:04

two represents median and media uh and senior right so this is i have just taken one

2:41:13

two and three as my notation notation so this is just a notation right the actual actual information is

2:41:21

junior media medium or senior right so it is a category junior is a category medium is a category

2:41:27

medium is a category i am denoting it or notating it using one two or three so intentionally

2:41:34

i have written this uh in a confusing way and asking you why is this not a regression problem

2:41:40

but then great job most of you guys did get it correct and obviously reaction regression cannot use

2:41:47

integers that is true that is true but that is not the main main thing here okay uh linear model

2:41:57

reject codes uh they don't yeah yeah they do they do they do

2:42:04

But then again, not the not the main point.

2:42:08

Alright, it seems everyone has gotten like the idea correct though.

2:42:13

Whoever has answered they have answered based on the idea they have gotten it correct.

2:42:18

All right. Next slide.

2:42:22

So it means everyone has understood regression to a good level.

2:42:29

Great.

2:42:33

Great.

2:42:35

What is the intercept in a predicted regression line?

2:42:40

Now just to clarify intercept, if you remember your coordinate geometry, you have the straight line in a slope intercept form.

2:42:54

Right?

2:42:55

So intercept was usually the C in y equals to mx plus c.

2:43:02

c was the intercept. So what does the intercept mean in a predicted regression line?

2:43:12

Yeah, yeah. Prediction when features are zero. Basically what it means is that you say for example y equals to mx plus c and if x is zero. So whatever the value of m will be that will be multiplied by zero, right? And plus c. So c is your intercept value. If you remember,

2:43:32

If you remember the example that Sir took for experience with respect to salary,

2:43:37

or sorry, salary with respect to experience,

2:43:40

the more experience a person has, their salary will increase.

2:43:45

But someone with zero experience will also have some salary, right?

2:43:49

So that was one in that example.

2:43:52

And that is why this is the correct answer.

2:43:55

Zero experience, but still there is some salary.

2:43:58

That is why prediction when features are zero is the correct answer.

2:44:01

answer. Okay. Distance from the training data is residuals or you can say error.

2:44:07

Distance from the training data. No. Distance from the training data is not something that is a valid answer.

2:44:17

Okay. This is always fun seeing the numbers go up.

2:44:30

All right.

2:44:37

Based on the behavior of residuals, remember, residuals are errors.

2:44:43

When is the predicted regression line reasonable?

2:44:47

When is the predicted regression line reasonable?

2:44:50

Reasonable.

2:44:52

So like the regression line is looking okay.

2:44:59

When does that happen?

2:45:15

Yeah, yeah.

2:45:16

So when residuals scatter around the line, that is when the predicted regression line is reasonable.

2:45:23

So for example, if there is, if Sir drew a line like this, and there are

2:45:29

there are residuals around like this, right?

2:45:33

So that is an example of a good regression line, reasonable regression line.

2:45:39

Get it?

2:45:41

All right.

2:45:43

When residuals form a curve is not, that is a different question actually in today session.

2:45:50

So actually what happens when residuals form a curve

2:45:57

a curve that is a question that I'm it will be that probably the next question or the last one.

2:46:05

But yeah.

2:46:09

Okay, yeah, it's the next question.

2:46:11

So when residuals are in a curve, like when you draw a scatter plot and you have the regression line

2:46:20

and then residuals are in a curve, what does that indicate, what does that suggest?

2:46:27

This one is a little difficult because it requires application of what Sores taught you.

2:46:42

But then, yeah, I'm sure.

2:46:45

Okay.

2:46:46

So I expected most of you would not get this correct.

2:46:49

And intentionally I wrote this option.

2:46:52

Linear model is not set up correctly with slope and bias.

2:46:56

I intentionally wrote that to confuse you guys.

2:47:00

The correct answer is that linear model is too simple to provide decent predictions.

2:47:04

See, what is happening here is if in a graph you have this XY graph and you have residuals like this, right?

2:47:13

Something like this, for example.

2:47:17

Okay? So the correct model, if you try to, if you try to do a linear regression, you will get something like this, right?

2:47:24

but a correct model would be more like this.

2:47:29

Get it?

2:47:31

So this is the correct model and oops,

2:47:35

this is the correct one and this is the incorrect one and this is the incorrect one.

2:47:39

So linear regression by definition because it is linear

2:47:45

is too simple to predict and provide decent predictions.

2:47:49

It's too simple to provide decent predictions.

2:47:51

And so even if you set up linear

2:47:54

model with slope M and bias A, however much you set it up, it is not going to be equal to a curve.

2:48:02

That is, if residuals are in a curve, then you need to use a curve model.

2:48:10

You can't use a linear regression model.

2:48:13

I hope everyone got that.

2:48:15

This is a rather interesting question and this will be covered more in detail in the next lectures.

2:48:21

So then it's an application of all.

2:48:24

what Sarah has thought today.

2:48:27

Oh, Arnica got that correct.

2:48:30

Awesome.

2:48:31

Alright, I think we've lost one player.

2:48:39

Anyways, I guess should be fine, right?

2:48:44

I should just start.

2:48:45

Thumbs up if you just want me to start.

2:48:48

Okay.

2:48:53

Okay.

2:48:54

One third of the people are saying yes.

2:48:58

All right.

2:48:59

If both train and test errors are very high, what's the situation?

2:49:06

This is an easy one.

2:49:10

The last one is an easy one.

2:49:13

Usually I try to keep the second last or the last one as the difficult ones.

2:49:20

So yeah.

2:49:23

I'm sure everyone would get this correct.

2:49:26

Ah, mostly everyone got a correct.

2:49:29

Okay, great.

2:49:30

If model is overfitting, right?

2:49:33

Remember guys, if model is overfitting, train error will be less.

2:49:37

Because the model is like, so a good example is,

2:49:41

the model is literally by-hearting or rote learning or mugging the entire textbook, word for word for word.

2:49:51

So if there is a, if there is a,

2:49:53

change in the word, like let's say there is a, instead of and there is some different word used,

2:49:58

or if in, there is some, some, any, any random change in the text without changing the meaning,

2:50:06

the model will not be able to identify it as the correct answer, right?

2:50:11

That is what overfitting is.

2:50:13

It is doing everything that is there in the train set, training set correctly.

2:50:19

All the, all the predictions in the train set are correct.

2:50:22

But then.

2:50:23

And in the test set, it fails horribly.

2:50:26

So that is overfitting.

2:50:27

Basically, it has memorized the training data and then in test data, it is not able to get the answers.

2:50:34

And this is obviously incorrect.

2:50:36

If it is exhibiting perfect generalization, how are the errors high?

2:50:40

The errors have to be low in both the cases, right, to exhibit generalization.

2:50:45

So yeah, let's sit.

2:50:53

All right, congratulations, Arnica.

2:51:00

You have one again.

2:51:02

I think on Monday also you only won.

2:51:05

So good job and good job to everyone who are tempted.

2:51:09

And yeah, I'll see you guys tomorrow in the tutorial session.

2:51:15

Okay, please keep your doubts ready.

2:51:19

And if you have any doubts, we'll have tried to

2:51:22

try to try to get them discussed at the start of the tutorial only. So that way if you guys

2:51:29

have to leave for some reason due to extension of tutorial timing, you can leave. Okay,

2:51:36

without and get your doubts all first. All right. With that, I will end the lecture now.

2:51:45

Thank you guys. Bye-bye. Have a good night.