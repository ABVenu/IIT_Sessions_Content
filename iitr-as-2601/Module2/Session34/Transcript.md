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

Thank you

4:59

Thank you.

5:01

Thank you.

5:31

Thank you.

6:01

Thank you.

6:31

Thank you.

7:01

Thank you.

7:31

Thank you.

8:01

Thank you.

8:31

Thank you

9:01

Thank you

9:31

Thank you

9:33

Thank you

9:35

Thank you

9:37

Thank you

9:39

Thank you

9:41

Thank you

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

9:58

Thank you.

10:00

Thank you.

10:30

Thank you.

11:00

Thank you.

11:30

Thank you.

12:00

Thank you.

12:30

Hello, everybody. Good evening all of you.

12:39

I was just waiting for everyone to join in. I think we can start.

12:44

Very good evening all of you.

13:00

Thank you.

13:30

Thank you.

14:00

Thank you.

14:30

Thank you.

15:00

Thank you.

15:30

So, folks, today we have a very interesting

15:43

and today we have a very interesting session and today's class is going to be, yeah, we have to start now.

15:49

So today, today we have a very interesting class and today we are starting out with an

15:55

an end-to-end case study kind of thing.

15:56

We have done that flow before, but every session has been.

16:00

more like discussing about different topics. And today one of the things that I will try to do

16:05

is to take you through a case study using a very familiar data set. So we'll take a data set that

16:12

is doable in a classroom setting. We will take that. We will go through all the steps. We'll go through

16:18

all the different steps that are there and we'll try to build a machine learning model. Try different

16:24

different algorithms and build a model. And there is one more

16:30

new thing that we will study. The model building phase, we are already okay. I think we have

16:35

already done. Sure, sure. I'll do that. Can I think I need to be. Yeah, I'm not a, I'm not a host.

16:46

One second. Can one of you make me the host? One second.

17:00

Ah, okay. I can't show I've enabled the chat for everyone. Great. Thank you. Yeah. So as I was

17:07

mentioning, so today's class will be more about where we take a real data set. We take a real data set and

17:13

we try to go ahead and we will be solving, building a machine learning model using that data set.

17:21

And we will try out different, different algorithms. So we'll start with classification. And I will keep it simple. I'll

17:27

start with logistic i'll take decision pre i'll take random forest we'll stick to the

17:32

algorithms that we have discussed so far i will not get into we'll not get into we'll not get into

17:36

something very different we have we'll see specifically in classification the algorithms we have

17:40

seen mainly logistic decision pre random forest these are the three things we will we will focus on

17:47

we will try different different different algorithms we will build different different

17:51

models and we will evaluate the models we will see how good the quality of the models are

17:56

that is number one what we will do and number two we will be getting into

18:02

a slightly new topic slightly new topic that is how to deploy the models and this is very interesting

18:08

because lot of you over the last yeah yeah yeah i can't you very good very good point that is

18:15

actually part of what i will discuss today very good that is part of what i will discuss today

18:19

c cd so mother we will not get very deep into it but i'll give an idea to you that is part of what i will

18:24

will cover today where we will discuss how to save the models and how to deploy the models deployment

18:29

is part of my coverage and i will also talk a little bit about model monitoring so far we have just

18:35

been focused on how do we do things in a jupita notebook the last two months you guys have been in

18:43

python and you spend the last one month with me and you know we have all been in a jupita notebook

18:48

that's where we're all our everything right but you might be wondering that sir we have been

18:54

a diabetes classification model loan classification model credit default model but

19:01

what we'll do we're going to do now real in real that's a question everybody will have

19:08

and that is exactly what i'll address today so one part of the session will be more like a

19:14

kind of a very very quick world win recap of what we have done that is the agenda for the class

19:18

mainly so we're we're we're we're we're we're using we're model going to we're

19:24

you know all know that we'll quickly will and the new thing that we will talk about is

19:29

the model we've made that we can't we can't what we can't how do we see how do we deploy

19:35

so that part only based on your request i'm doing that is not a big coverage area for the session

19:40

that content we don't have it as part of the session content but since you want to know i will

19:45

additionally talk about it okay i will additionally talk about how you can maybe

19:49

take that particular model that front end way web app can't make

19:53

you're application how can't so we will use a bit of jemini help so by the end of that

20:00

class each and every person should have a very real world overview

20:06

that all this while we're jupita notebook in that

20:09

ipynb file or you're you or whatever you're looking at the correct answer actually real

20:14

we're in facebook browse we we're some website type

20:17

and there ml there ml are so so whatever we're ml notebook

20:20

in that is the bridge that i'll try to build in the session today so that the entire

20:27

n2 and clarity is there okay so this is that two phases of the class first phase will be the model

20:32

development second phase will be the deployment we will see that what is that yeah to that is

20:39

i have to uh okay i think you mean to say garima you're you need to deploy a model right

20:45

you've made up and you've made you know what you'll deploy can't and just to let you know we'll use

20:49

so in case some of your curious key uh you know like how how we will be doing that so we'll be

20:56

mostly using something called radio okay let's move on uh and i will start on i will be sharing

21:03

this and just one other thing uh so uh yeah so before we start this is uh this is a

21:13

note from the team i think the the masai team they asked me to convey this to all of you and i would

21:19

like all of you to take take a moment to uh to share your feedback i think as part of the

21:24

as part of the as part of the last course at the session you know we have been doing this for the

21:28

last one month so please do take a moment to share your feedback for the course uh and obviously your

21:34

feedback is our team's motivation uh that's what keeps us going and it genuinely helps us understand

21:38

what's what's really going well so if you think that something's going well please to talk about it

21:44

and and obviously this is something that we can all use to enhance the learning experience

21:49

so and and so please all of you can take some time i think there's a link that you might have

21:54

received uh that's what the team convey to me so you just just take some time before we start the

21:59

session we can take two to three minutes time i can give all of you to um to just uh fill up your

22:06

feedback so arsita you can also maybe just help in case there is some link or somewhere where the team

22:11

has to go and fill up uh yeah yeah yeah thank you so i'll give all of you uh

22:19

two to three three minutes of time you guys can just take a moment and uh just take some

22:24

time to enter your feedback for the sessions out they are going and yeah in case you have

22:28

already done some of you you can just let us know on chat that you have completed and others if you

22:33

have not done just take three minutes of your time to fill it up and then we'll start on with the

22:37

contents of the session okay what's that uh account shoe i have uh oh yeah i will do that yeah i will do that

22:44

yeah actually maybe i'm a little on and off uh linked in akanshu okay now i will definitely

22:49

to that here take thank you thank you thank you uh so i'll just pause for a while once you all done

23:04

let us know and then we'll start

23:19

you know.

23:49

Thank you.

23:51

Thank you.

24:21

Thank you.

24:51

Thank you.

25:21

Thank you.

25:51

Thank you.

26:21

Thank you.

26:51

Thank you.

27:21

Thank you

27:51

Thank you

28:21

Sure.

28:28

Sure, sure, I will answer.

28:32

I will answer your questions.

28:49

I will answer your questions.

28:50

Thank you.

28:52

Thank you.

28:54

Thank you,

28:59

answer your question

29:04

we'll use

29:06

I'll keep it very basic.

29:19

I'll keep it very basic.

29:20

That is again not part of the content.

29:22

We are not curated the content around that.

29:24

Deployment actually I'm not

29:25

that we don't know that

29:27

will be an important thing for you guys

29:29

because so that you can get the very good end to and connect.

29:32

A lot of deployment that we will see,

29:34

even a country that is to do with your question on Docker also.

29:37

Docker, we'll talk about

29:39

so basically when we come to agency AI,

29:41

some of the ideas will be very similar there.

29:44

I will talk a little bit about Docker when I come to that portion of the course.

29:47

So the same way I will we will deploy models.

29:50

Deploying LLM applications will be very similar.

29:53

So we'll docker's a little bit of a little bit of a different topic.

29:57

So that will be a very different topic.

29:59

So, unfortunately, in today's class we will not take it up.

30:03

I will take it up.

30:04

I promise you I'll discuss about Docker, Kubernetes,

30:06

a theory I will discuss so that people have a good understanding.

30:09

But we'll leave it aside for today.

30:11

So we will stick to Gradio, Anjo to answer your question.

30:15

We'll use a very basic framework called Gradio.

30:18

So that's a very basic framework called Gradio.

30:19

So a different thing, but that we'll just use a bit of, I just wanted to show you the application,

30:26

that, everybody is able to do it and you're able to kind of get a big picture idea,

30:33

what is happening. That's the whole idea.

30:35

Then a Docker Kubernetes is not part of our thing right now. Don't worry.

30:40

Modeling too, we are all doing this already.

30:42

So and Ankhid, we are all using collab, right?

30:45

That's the reason why I'm encouraging Google Collap.

30:47

Even a big part of our

30:49

almost the entire course on AgenteCIA is also going to be done on collab.

30:53

So we strongly discourage you, discourage you from using your local machines.

30:56

Please don't use it.

30:57

For the learning purpose, stick to collab.

30:59

So, coi tension is fine, absolutely okay.

31:02

That's the way to look at it.

31:04

Is not?

31:07

Please stick to collab.

31:08

Don't get into all.

31:10

Okay.

31:15

I'm going to share this across with everybody.

31:17

So, and one more thing, Akanshu, just to answer your question, at a practical level, at a high level, yes.

31:24

As a developer, you don't need to get very deep into it.

31:28

Obviously, that's not the, testing is not something that you need to know at a very deep level, because testing a

31:34

a very different mindset that you require for testing.

31:38

So, machine learning development and machine learning testing are very different fields.

31:44

Concepts will be the same, right?

31:46

Right?

31:47

But again, testing is a very different piece.

31:49

Those by testing principles have.

31:51

I mean, I can talk about things like unit testing, integration testing, regression testing.

31:56

There is many types of testing, but that's a very different QA kind of a course that we are talking about.

32:01

So again, QA is a very different thing.

32:03

You don't need to get into that.

32:04

As a developer, your focus should be on model development.

32:07

You are not going to be a tester.

32:09

Huh, concepts, even if you talk about machine learning testing in real organizations, testers

32:15

testers also need to have the same kind of concepts.

32:19

Ideas should be very similar.

32:21

But you don't need to be like, you know, how do I say?

32:24

You don't need to be very good at it.

32:25

You don't need to really get very deep into the principles and understand it.

32:29

Because usually he will not be the person who has to, you know, who has to do the testing.

32:35

There'll be a completely different team who will usually do the, you know, the model testing.

32:40

That's one way to do that.

32:41

Okay.

32:45

certainly I think some of the, some of the basic principles, I agree, like something we'll be seeing as we go along.

32:51

As I said, a bit of doctor and all that I talk about, so who I'm thinking.

32:55

The principles remain the same.

32:57

So whatever we are talking about in ML, those things will remain very similar when we talk about

33:01

LLM and H&TKI.

33:03

So we'll get a lot of time that time, obviously.

33:06

Yeah, but as a as a as a machine learning engineer, as a machine learning developer, your work

33:14

primarily should be about A, taking the data, get it into a PANDA's data frame, just to draw

33:19

the connect at a high level, whatever you guys have done so far.

33:22

You data, you data lia, you've made, some of the things that you have talked about

33:29

is scaling, we scale the data, we transform the data, we transform discussed here, right?

33:35

How to normalize the data, convert your data into normal distributions, right?

33:38

And we talked about that.

33:39

We talked about why skewness is bad.

33:41

So all of these are feature engineering methods that we do.

33:43

And after that, you also visualize your data.

33:46

You've done a little bit of basic data visualization using Matt Plotley, Plotley,

33:50

our visualized kios, systograms, scatter plots.

33:54

We do correlation.

33:55

We do all of these things to find out, to understand our data in a better way.

34:01

And after that is done, what we do is we go ahead and we build models on our data.

34:08

We try different, different models.

34:10

We build model and we evaluate the models.

34:13

So that's the thing.

34:14

This is the work of developers.

34:16

And then we give it to the testing team.

34:18

They are the ones who will test it.

34:20

But testing in testing what is happening in testing?

34:23

If you ask me, what are we doing in testing?

34:25

Like, if you talk about testers, what are doing?

34:27

right?

34:27

If you're the model made, what is an object.

34:30

Right?

34:30

Now they are testing that model.

34:32

That hey, if I built a diabetes prediction model,

34:36

you relate back to some other classes, you know,

34:39

sometime back when we built, when we did something on diabetes prediction.

34:42

Now, now they're a model by, right?

34:43

Actually, case study is a cancer prediction use case.

34:47

So, mano, you have a model which can detect cancer, right?

34:52

Imagine you have built a model that is, that can detect cancer.

34:55

Okay, exactly. They will check for edge cases.

34:58

They will check for edge cases.

34:59

And guys, one request, can you all, like, set your chat to everyone?

35:03

So something I encourage, because, you know, that way what happens is,

35:06

everybody feels part of the class, because some of you ask really great questions,

35:10

but because you're only messaging to us,

35:13

So only we get to see, can't we? Only we get to see.

35:16

So just all of you, Anjorn has asked something.

35:19

Akanchu keeps asking very good questions also.

35:22

So just, just go and message to everyone.

35:24

So that everyone gets to know your questions also.

35:27

So, so, exactly.

35:30

So exactly, they will check for, they will check for edge cases.

35:34

But what you know, our model, how is that model performing?

35:38

How is that model performing with different test data.

35:43

If you have some test data on that, what model's performance?

35:48

Today, our main objective will be, we will build a model to predict cancer.

35:52

Based on some input access, we will predict, is it cancer, is it not cancer?

35:58

And a lot of this is happening in the real world.

36:00

If you ask me in the world of health care, this is a very big use case today.

36:05

Both very use case.

36:07

So this kind of thing is a very, is a very big thing today.

36:10

If you ask me, health care is a,

36:13

massive space today, if you ask me, where a lot of these predictive analytics models are getting used

36:19

to look at the different diagnostic features of a person.

36:23

Your blood pressure, your glucose level, any past medical history,

36:29

we are looking at all of these parameters and we are trying to predict.

36:33

This all inputs are okay.

36:34

This all inputs are and based on that, we are trying to predict what is the probability you will have

36:39

cancer or what is the probability you will have heart attack.

36:43

And this is a big thing that is happening.

36:45

If you look at most of the variables,

36:47

variables maybe, this classification is going to.

36:51

There are already reported studies that Samsung Galaxy Watch and Apple Watch are doing

36:56

where they are able to predict heart attacks.

36:59

That release has not been released.

37:01

I think the devices are still not incorporated it, but they are doing a lot more.

37:04

I personally use a Galaxy Watch Ultra.

37:07

Our watch in ECG is, fall monitoring.

37:11

have. Fall monitoring is, by the way, machine learning, right? And it was surprisingly

37:16

good, actually. What are they doing? How are they doing fall monitoring? How are

37:20

how are they doing galaxy watch detect can't whether you are falling or not? So they have gyroscopic

37:27

sensors. These are all your inputs. So based on all those Xs, they are trying to predict

37:33

did the fall happen? Yes or no. If fall was, then emergency contact, that's all over. And

37:40

And the rest of everything, all is real-time tracking.

37:43

Stress monitoring.

37:45

If my stress, like, session is, my session in stress,

37:48

so after the completing the two hours last, I'll go and check my mobile.

37:53

Stress is usually very high.

37:55

I'm always asking questions, answering questions.

37:57

So, okay, it's naturally expressed.

38:00

So, but the interesting part is, now the, now the variable devices,

38:04

what's what is, what's their stress, they're looking at,

38:06

their sleep, they are looking at your sleep data from yesterday.

38:10

They're looking at everything, your heart rate, everything, real time, at this very moment,

38:14

at this very second. And based on that, they are trying to predict,

38:18

what is the probability that half an hour after Sayan's heart attack will?

38:23

So that is actually happening.

38:25

But there are reported studies that is possible.

38:29

It's physical.

38:30

I mean, if somebody suffers from a heart attack, you actually get to know sometime in advance.

38:35

There are already reported studies on that.

38:36

So there are real use cases of this.

38:39

So when we talk about this.

38:40

about disease prediction, this is a very real use case.

38:43

And healthcare in health care,

38:44

there's quite analytics is not going to be. Right now, if you see,

38:47

a lot of, especially Western,

38:49

uh, uh, Western nations, if you see,

38:52

America, Europe, if you look at some of the hospitals

38:55

that are very advanced, very advanced. I mean, India is a different

38:59

ecosystem. There are a lot of good things here.

39:02

If you're up US, Europe, I also, I have a residency in Qatar,

39:07

I also, but if I have to visit a hospital in Qatar,

39:10

they have to have seven, eight minus, appointment in.

39:13

You have your up on the doctor,

39:14

there is no concept of just going and walking into a doctor

39:19

clinic. You can't do that.

39:21

Who is not as a doctor.

39:22

You have to take a eight months' before appointment and only then you can visit a doctor.

39:26

There are a lot of good things and bad things also.

39:28

But infrastructure-wise, they are very advanced.

39:30

They are already doing these kind of predictive analytics and all that I'm talking about.

39:35

Our here here on the challenge is, that data's challenge is.

39:37

That data collection takes and not.

39:39

If you go to the big chains, then this is actually happening.

39:42

If you go to the big chains, they are collecting the data, they will have data entry people.

39:47

Like, like you're in hospital in you admit, you're discharged.

39:50

There are people who are entering the data.

39:52

If someone who can't type and data in any enter

39:53

then, then how model will be?

39:56

Model building and machine learning is only possible if you have the data.

40:00

The biggest challenge is the ecosystem of collecting the right data.

40:04

That's the challenge.

40:06

Otherwise, software to all people have.

40:08

So, we're all seeing.

40:10

You guys are also studying.

40:11

What, what's the thing?

40:13

What's the big deal?

40:16

Nothing.

40:16

The biggest challenge that we see in ML is the collection of data.

40:22

That is the biggest challenge.

40:24

Now, data right?

40:25

So, everything is possible.

40:28

I'll give you another practical use case.

40:29

You look at CCTV.

40:32

Traffic monitoring has got.

40:34

We talk about these things, right?

40:36

You know, smart cities and.

40:38

optimizing traffic and all of these kinds of things.

40:40

If you'll see this stuff, so feasibility is there.

40:45

You can do.

40:46

Everything can't India.

40:48

The biggest challenge is the data, the ground level implementation.

40:52

You have to invest money.

40:55

You have to put the sensors.

40:56

You have to put the cameras.

40:58

If your sensors, camera, hardware,

41:00

everything is.

41:01

If you're collecting the data,

41:03

then predictive analytics is actually very easy.

41:07

But it's, it's.

41:08

requires a lot of money to install all these things, right?

41:10

The software part is very easy.

41:13

I'll give you a very practical use case.

41:16

We can look at an image data from an intersection

41:19

or we can look at sensor data.

41:22

Sensor's from a traffic movement

41:23

and real time we can plan

41:26

that here traffic jada

41:28

so you're diverting.

41:30

So these kinds of things can be done

41:31

and these are already happening in Western countries.

41:35

So this is short a Paisa, so they are doing it.

41:37

But what I'm getting,

41:38

that is it is not a it is not a software problem software and you know thing we

41:45

already have right so so if you if you take a look at it the software thing we already

41:51

have we are already able to build the model that kind of thing we are already able to

41:55

able to do but the important thing here is more about the the data challenge the data

42:04

challenge is the is the more difficult part how do we collect the data that's the

42:08

more difficult part, okay?

42:09

Sure not.

42:12

Just wanted to talk a little bit about it, general things.

42:14

Okay?

42:15

Yeah, yeah.

42:19

Sure, sure, sure.

42:21

And there's a lot to talk about.

42:23

It's never ending.

42:25

Okay, so it's a lot to talk about.

42:27

So yeah, I can't you.

42:28

Just to answer your question again, yes, we check for edge cases.

42:30

Like we build the model and we go back and check for edge cases.

42:34

Yes.

42:37

Aphotos of course.

42:38

There's everything is possible.

42:42

It's about ground level implementation.

42:44

I'll give you a simple use of it.

42:46

I honestly do not know.

42:47

I do not know why they are not, don't do it.

42:50

We talk so much about elections and we,

42:52

Bengal elections were, whatever happened.

42:55

I mean, some of the things you already are seeing in the news, right?

42:58

So the point is, you know, if people are all talking about data,

43:05

my thing is, ground level, it's kind of easy.

43:07

Now, people go, go, biometric device,

43:09

go. Everybody who goes to the polling

43:11

center will do the biometrics can, and if their

43:13

biometric is recorded, they get to both.

43:15

But if you actually see the ground level

43:17

implementation, the ground level

43:19

implementation is there is actually no concept of

43:21

biometric. People are going,

43:23

you're going, you

43:23

know, a Dhar card like that. Now, how are

43:25

how it is, you all know that

43:27

how it is, you all know that, right?

43:30

How documents are forced and all that, you guys know that

43:33

already. But how, so

43:35

at the end of the day, a lot of it boils

43:37

to implementation at the end of the way.

43:39

How you can, how you're implementing

43:40

these things, actually, at the ground level.

43:43

So, so

43:44

election commission can mandate everyone

43:47

next time who goes to vote.

43:49

Your biometric mandatory

43:50

is. All right thing is

43:52

it's all right. I'll give you a simple example.

43:56

Just say, if you, if you marry,

43:58

if you're married, if you're married certificate or

43:59

registry, you're going to, biometric

44:01

mandatory. I know, most of you are too, you know, too,

44:03

too young to marry. But

44:06

it's mandatory right nowadays.

44:09

You have to be biometric

44:10

then have to be. If you go to visa,

44:12

biometric then have to be. If you're traveling towards

44:14

so. So I don't know

44:16

why they don't do biometric in

44:17

exactly. Exactly. It's such a

44:20

no-brainer. Such a basic thing.

44:23

What is the issue? Logistics.

44:25

Now, what's the scanners? How's

44:26

how can't, how can't. It's

44:28

a good, this is the connection commission,

44:30

say, boy, chorro. A d'ar card low.

44:32

Verify.

44:32

Okay, one percent, two percent, point one percent

44:35

error.

44:36

And what back-end in what? Nobody knows. We don't know. Nobody knows.

44:41

That's another discussion. But, yeah, but it's so easy to

44:44

validate people based on Adhar and then, you know, kind of do a biometric.

44:48

Now, the bigger question is, now, that biometric data

44:50

is right? So everything boils down to data. If your data is correct,

44:53

if your back-end data is correct, then everything works smoothly.

44:57

And this is applicable for everything in life, be it

45:00

machine learning, be it, you know, generative AI.

45:03

So everything is possible, if your data is trustworthy.

45:06

Now, you say, sir, that the Adhar banai, that biometric did, that he forged.

45:12

If they're illegal out and Adar made, biometric did it.

45:15

What's kind of, that's fine. It's fine. How do you stop that? You can't stop that.

45:22

So the only way to stop that is go back to the data stage and then fix the data.

45:26

And even machine learning in this is, you know, even when we talk about model building, a lot of

45:30

this also happens. Many times we build a model and then we realize, okay,

45:35

we actually go back to the data gathering stage.

45:39

We go back right to the phase where we collected the data.

45:42

And then we go back and fix that.

45:44

Or, from back, we're back from data proper model to make.

45:46

This is the very practical thing we do.

45:48

That's why we say,

45:48

that model building is a very iterative process.

45:51

Now, data fixed you,

45:52

then the model

45:52

and then again model banai.

45:54

Excuse me,

45:55

again data go and fix

45:56

model made.

45:57

Right.

45:57

And the same way it basically works out.

46:01

It's a very iterative process.

46:02

Okay.

46:04

Yeah.

46:04

Yeah.

46:05

It's a very good question, a point that you raise.

46:10

Politic is Rajdip, it is too sensitive.

46:12

Industries like finance, these are very sensitive, actually.

46:15

So using face recognition for that is very sensitive,

46:18

so it is basically something that is practically possible.

46:25

Practically possible, and nowadays if you see many of the private banks,

46:32

Now, now, it is, it is basically bank, look.

46:34

ICISA bank.

46:35

American Express.

46:36

I'm not that thing, but I'm sure they are already implementing it.

46:40

It's very strong.

46:41

I mean, mostly the tech team said,

46:45

few of these private banks are very good.

46:47

I-Saysa bank technology team is very good.

46:49

Access Bank is very good, technology team.

46:51

And they are already having these voice recognition systems.

46:55

So the voice recognition system, you can just call up the bank and say,

46:59

hey, I want to talk about, you know, saving account.

47:03

I want to talk about credit card.

47:04

So based on what you're saying, you know, it will connect you to the corresponding agent.

47:08

So these things are at a high level happening.

47:10

But, yeah, I mean, doing a face scan is, is something that is also, you know, it's in the works.

47:22

I think basically fast KYC process already has.

47:26

I'm not 100% sure, but I think that is already there, which banks already are.

47:30

I'm not, I don't recall, but I've heard about it, the instant account open HOTI.

47:34

happens. But yeah, that's another thing. But I think it happens already.

47:38

Yeah, yeah, Garima, I will, I will come to that. I will come to that. Yes.

47:44

Actually, it can be part of what I've been discussed today. So let's move on.

47:53

Very nice to see some of these questions to do. That is also, that is also part of my

47:56

objective today. I wanted to also take up some general questions. So topic of hair is one part.

48:00

That's one discussion, but then I really wanted to give all of you some time for some

48:04

you and day questions also because every class is like we do a topic. We have an agenda.

48:09

But today is kind of very open. I will, you know, there's an agenda. We will complete that case study.

48:14

And then I really want to take some time with all of you on these generic questions.

48:18

So that's, that's the time that we will spend today. And Anjori had asked a question sometime back.

48:25

Very good question. Very good question. I think Garima's question is kind of related to that,

48:29

not entirely, but to some extent is related. Garima's question is related.

48:33

Garima's question is also on drift. So yes, that's normal. It's called data drift or concept drift.

48:39

So you keep the model up to date by monitoring real world performance. Okay. So machine learning

48:46

what are? If I have to give you a very broad idea of everybody has seen this for the last three weeks.

48:51

We're doing four weeks in fact. We have data. We have trained test made key.

48:57

Train in model, we made. Test in the model to evaluate here. Okay. Now, now, now, think, the development team

49:02

have whatever model you're building, which you're building, you're, excuse me,

49:08

you're building that model on the train data, right?

49:13

You have data. You have data. You are building the model on your training data. You're building the model on your

49:20

training data. And then you are, you are, you're, you're final model that you're building. Whatever

49:28

final model that you're building, that final model you're building, like, is stale data, right? That is a stale data.

49:37

Whatever final model that you're building is stale data or is on stale data. Let's say today I give

49:44

your data sale. You're, you're making some model in. You're saying, you're doing some model. Now,

49:49

you're doing a model to predict cancer, which is our case. You're making a model to predict cancer, which

49:56

that's our case is cancer. We have done this before. It's not something completing you.

50:02

So, you, you know, you know, and this is a very nice way to approach something. It's not as if

50:09

first thing, we're going to code file. We'll have to think. How do we work towards things? Okay, we have to

50:16

solution it. Okay. So, if you have to cancer system banning it. And this is how you think. You don't open up a file,

50:24

you don't open up an Excel, a CSV. You know,

50:26

So that's not how we do. We have to think. Okay, I have to build a hospital diagnosis system.

50:34

So use case what is? Hospital wants us to build an AI system. This is the use case. In fact, let me, let me ping this to use.

50:42

This is. So, the hospital. Hospital wants us to build a, a, uh, build an AI system that will predict whether a tumor is malignant or benign.

50:56

This is the problem that we are broadly trying to solve.

50:59

This is our case where we want to build a model to predict whether the tumor is malignant or benign.

51:06

Malignant, it is cancerous or benign?

51:11

Malignant, tumor means it is a, uh, it is dangerous. It can kill a person.

51:16

Binine meant to be safe.

51:17

But then we are classification. So hospital wants you to do that.

51:21

Because, the normal process is what? Normal process is.

51:26

you go there, you do a scan, you blood test,

51:30

everything, and based on that, there is a doctor,

51:33

there's a radiologist, there is a pathologist,

51:35

there's a panel of doctors.

51:39

Now, that's the hospital in, you go to a test,

51:42

scan, do, everything,

51:44

and two days after your report

51:45

and a report, what is the report?

51:49

Report is that, what is the report?

51:49

The report is that, your test results

51:51

is this is, this is, this is all your test results.

51:56

That is the data.

51:56

test results, it's not that doctor

51:59

are you, your blood pressure

52:01

what is your blood pressure.

52:04

Doctor not, not

52:04

but the doctor is a data.

52:07

Your data points,

52:08

look at the doctor is giving the final report.

52:11

That your tumor is,

52:13

that your tumor is,

52:13

how dangerous are?

52:15

Now, this process, if you see today,

52:18

is majorly handled,

52:19

is completely handled by a physical human being today.

52:23

One human being or a panel of human beings.

52:25

Go any hospital in go,

52:26

if any disease diagnosis,

52:27

then a doctor is a panel of doctors.

52:31

There are radiologists,

52:32

some radiologists,

52:33

there are, some other

52:34

specialist, a gynaecologist,

52:36

are gynaecologist. These are a panel of doctors.

52:38

If you go to a super speciality hospital,

52:39

a panel of doctors is deciding

52:41

that you can be a disease

52:42

can be.

52:44

So, hospital's what is?

52:45

The hospital is.

52:47

Now, hospital is, we're saying,

52:48

we're saying, we're not

52:48

we're not going to be it.

52:50

I don't want my doctors

52:52

to do all this words.

52:54

I will hire a team.

52:56

team of developers or software company,

52:57

we hire and that

52:59

he'll make an automatic AI system

53:01

will be, where patients

53:03

will, we'll have past test

53:04

and that test

53:06

basis, our AI system

53:07

will say, well, you have

53:09

cancer, you, your cancer,

53:10

or you're your cancer, or your tumor

53:11

or not?

53:14

There's no thing, no difference.

53:16

Here, doctors are,

53:18

you're telling, tumor malignant or benign.

53:20

Here, AI is

53:20

here, AI is tumor malignant or benign.

53:22

If you think from a big picture perspective,

53:24

we are doing classification.

53:26

We are trying to predict, is it malignant, is it benign?

53:28

Okay? That's the first thing.

53:30

Now, now,

53:30

now, you have to

53:31

how do you know how will the data come?

53:35

All this while we have been taking all this for granted.

53:38

Because I was sharing some CSV with you,

53:40

you were starting with answers file to data

53:42

available.

53:43

But now you have to solution

53:45

can't have a, imagine the hospital has approached you.

53:47

Hospital has come to you.

53:48

Hospital, you have to build

53:49

that whole system.

53:52

So how will?

53:54

If you are the machine-learning person,

53:56

how will you build this system?

53:58

You have got data

53:59

So to train a model,

54:02

you need lots and lots of data, right?

54:06

So data

54:06

how can't?

54:09

X, Y combination,

54:10

back to supervised learning.

54:11

We have done a lot of supervised learning already.

54:14

So in order to build a system

54:16

where you can predict

54:18

malignant or benign tumor,

54:21

you have got to

54:22

many x-y combinations

54:24

only have been able to.

54:25

That hey,

54:25

when the patterns are like this, malignant.

54:28

When the patterns are like this, benign.

54:30

When the patterns are like this, malignant.

54:32

Patterns like this, benign.

54:34

Patterns like this, benign.

54:36

So these are X, Y, combinations.

54:38

You need many, many such X, Y combinations.

54:42

Let's say the hospital is hiring me as consultant.

54:45

And this is a very common model.

54:47

A lot of hospitals also hire consultant.

54:48

Let's say they hire me as a consultant

54:50

and they say, I'll please build this for us.

54:52

So I need the data, right?

54:53

Now, data can't?

54:57

This is exactly what I was telling you guys,

54:59

that data infrastructure

55:00

should be.

55:01

Data to hospital

55:02

have been to be.

55:03

If data hospital

55:04

to have not,

55:06

no matter all that you learn,

55:07

all that I'm teaching you right now,

55:08

you don't know.

55:10

You're not going to be

55:10

no model not going.

55:12

All these are useless

55:13

if you don't get the hospital,

55:15

the hospital

55:16

who hospital is hire

55:16

for this work for,

55:17

if he has data

55:18

didn't,

55:19

you know,

55:19

that hospital's

55:20

there's nothing,

55:20

you're going to say,

55:21

sir,

55:22

you say,

55:22

you're saying,

55:23

what will we?

55:25

You have to give me the data.

55:27

You have to tell me,

55:28

you have to tell me,

55:28

you have to tell me,

55:29

you have to last

55:29

last two

55:29

years in

55:30

many people,

55:32

you know,

55:32

you know,

55:33

you know,

55:33

so that is how

55:36

I will have to

55:37

talk to the management.

55:38

I will have to say

55:39

that we need,

55:39

we need,

55:40

at least we,

55:41

need, at least we

55:42

need 2,000

55:43

patients' data

55:43

and data

55:45

and the data

55:45

in this format

55:46

we need, that we

55:46

need,

55:47

I will tell them,

55:49

I will tell them,

55:49

we'll in a tabular

55:50

form in,

55:51

this sort of,

55:52

like we have

55:53

you have

55:53

concept in class

55:54

in X1, X2, X3,

55:55

so patient's history

55:56

and what was the

55:59

final diagnosis?

56:00

What was the

56:00

malignant

56:01

was his malignant

56:01

was his

56:02

malignant was,

56:02

he was the

56:02

next row,

56:05

patient number

56:06

two,

56:06

his history,

56:07

X1,

56:07

X1, X2,

56:08

X3,

56:08

X, 4, X,

56:08

X, 5,

56:09

blood pressure,

56:09

cholesterol,

56:10

whatever is,

56:10

there,

56:10

and based on that,

56:12

his final diagnosis

56:13

was,

56:13

what was the

56:16

malignant, was the person

56:16

malignant,

56:17

was the person

56:18

blinded.

56:19

That is the way,

56:19

how I want my data.

56:21

And remember,

56:22

this data is the

56:22

is what the hospital has to

56:23

give you.

56:26

And this data

56:26

can't

56:26

you know

56:26

you can't

56:27

not happen

56:30

without

56:30

input,

56:31

output,

56:31

output

56:32

combination.

56:32

Now there are

56:33

a lot of

56:33

other

56:34

situations where

56:34

what happens is,

56:37

now that

56:37

happens is,

56:38

now that

56:39

might be

56:39

there may be

56:41

a hospital

56:42

is a new

56:42

hospital.

56:44

Now,

56:44

what will

56:44

if a

56:45

hospital

56:45

established

56:46

hospital is

56:46

there's

56:46

there's

56:46

there's

56:46

there's

56:48

already

56:48

systems,

56:49

there,

56:50

there has,

56:50

databases have,

56:52

where

56:53

it's normal, right,

56:54

patient application

56:55

form

56:55

is,

56:55

you go to any

56:56

any big

56:56

chain in

56:56

you go to

56:57

even if

56:57

if you're

56:58

if you're

56:58

simple

56:58

test

56:59

in a simple test

56:59

in a

56:59

hospital

57:00

in a

57:01

need.

57:01

We're

57:02

in India

57:03

in

57:03

there's

57:03

no

57:04

there

57:04

no

57:04

there's

57:05

no

57:05

you go

57:05

and

57:05

you

57:07

go and

57:07

and

57:07

get

57:07

but

57:08

in India

57:09

in India

57:09

if you

57:10

in

57:12

you go to a

57:12

hospital

57:12

you will

57:13

have to

57:13

fill up

57:13

information

57:14

you will have to

57:15

you will have to

57:16

pay just for

57:19

registration

57:19

and registration.

57:20

And registration

57:20

what is?

57:21

Your

57:21

detail

57:22

have your vitals are, everything, all your basic vitals, your name, your contact number, your age,

57:27

your weight, your height, your BMI, your, your,

57:30

your, your, your, that is what I meant by the data.

57:35

Then, after you, that's all

57:37

against you go back. So sometimes the hospitals will give me the data.

57:40

Other times, if hospital says, we're, we're new hospital, we have to, we have to, we have to,

57:44

we have to, we have to, we have to, we have to, we have to figure out a way to get the data from other

57:50

third party sources.

57:52

hospitals, there are more many changes.

57:55

Hospitals of other, you know,

57:58

other, uh, you know, uh,

57:59

you know, uh, there are a lot of players who are selling data also, you know, right?

58:03

You know, you can get data from other places and there are different privacy contracts and all.

58:08

Which data you can generate can't you.

58:10

You can create something.

58:12

Uh, another thing is very interesting is, you can sit with their panel of doctors,

58:16

the new hospital, you know,

58:17

you know, the data from the panel of doctors to,

58:18

you know data from label and make up.

58:20

you look at other patients, or then you give them a window of six months.

58:25

You'll tell, okay, we're immediately, we're not going to,

58:27

we're immediately, we'll do you, six months, we'll sit together.

58:29

We'll look at different patients to look, and we'll look at your doctors

58:33

how it's malignant or benign diagnose

58:37

I will note that data myself, and then we'll make it.

58:41

And that is a very common way how things happen in practice.

58:44

This is some of the questions you guys were also asking today, very beautifully related to today's

58:48

case study.

58:49

Look, the real in the model development

58:52

that's the use case, a hospital diagnosis,

58:55

this is not like a one-time process.

58:58

It's not like a one-time process. It's not that

58:58

the hospital has hired us, say, and you have a model

59:01

made, okay, data

59:02

data made, model been made, just, our

59:04

time's done. No.

59:06

Remember, especially in this

59:09

use case, if it's new hospital

59:11

then what will?

59:12

He has a very limited amount of data here. They have a very limited

59:15

amount of data. They have only, let's say, 20, 30,

59:19

rows of patients data they've got right now.

59:22

So what will happen in that case?

59:25

So I will start.

59:27

We'll start.

59:28

I say, not that I will just sit idle and do nothing.

59:30

I have to start.

59:31

I will build a basic model.

59:32

We'll make a basic model.

59:34

We'll make a basic model. We'll give us to hospital.

59:36

It will go.

59:37

Barabbard shall.

59:38

Then what I will do, every week,

59:40

every week, as new patients are getting added to the system,

59:44

I will have to retrain my model.

59:47

This process is what is called model retraining.

59:49

So just wanted to just mention this to all of you.

59:52

This is basically what is referred to as what is referred to as model retraining.

59:57

This particular process is called model retraining.

1:0:00

You take the data.

1:0:02

You take whatever, you know, a data is there and we, we try to retrain the model.

1:0:11

You see, every week, new patients will get added.

1:0:14

I'm usually weekly.

1:0:14

Weekly or fortnightly is a very common norm.

1:0:17

because you have taken the current X, Y combination, and based on that, you have built a model.

1:0:24

Now, you have made a model current data on.

1:0:27

But, one week back, the hospital in Naya patients add one.

1:0:31

You're getting new X, Y, patterns.

1:0:35

Now, your equation, your model you've made here, that model,

1:0:38

that model, do, two, two-hapte-prel prior model is.

1:0:43

You know, two weeks of the past, you've been a model made.

1:0:49

But, now the new patients add was, that your model in the model, that pattern, that thing is not

1:0:54

considered in the model.

1:0:56

So you have to constantly take those new intramental data and you have to retrain your model.

1:1:01

Model, what is what, why is a function of X, y, y, to the x squared equation is.

1:1:06

So that equation always change.

1:1:08

This is obvious, is not?

1:1:09

If X, Y, combinations, if the data is getting added, if more data,

1:1:13

data is coming, definitely your patterns will change.

1:1:16

And we will have to constantly reframe the model.

1:1:20

And this thing we're drifted in production.

1:1:23

This is the same thing, Anjor was asking sometime back and also what Garima was referring to.

1:1:28

This is basically what is referred to as model drift, a concept drift.

1:1:33

You know, the model made, that two-a-past-pre-per-model was model.

1:1:38

That was based on two weeks back of patient data, right?

1:1:41

That was your model is right now.

1:1:43

that model will not give you good performance.

1:1:47

You have to account for the current data.

1:1:50

Abhi two-haphtam, the patients add-hirt were, can I add it to my model?

1:1:54

The model should reflect that reality.

1:1:56

That is the intuition.

1:1:57

So, this retraining, we model retraining, we're model retraining,

1:2:00

we're new data add and back from model retrain.

1:2:03

So that's the thing.

1:2:06

Yeah, absolutely, absolutely.

1:2:08

That is definitely there.

1:2:09

And it's a process, Garima.

1:2:10

No model will be 100% correct.

1:2:13

Right?

1:2:15

Machine learning, one of the fundamental rules is machine learning will never be 100% accurate.

1:2:20

It will never be 100% accurate.

1:2:22

It will always be prone to errors or mistakes.

1:2:26

So that is part and parcel of what we have to accept.

1:2:28

Now it is more about my discussion with my hospital, because the hospital has hired me.

1:2:34

Hospital said, say,in, you have for our lily, a tumor detection system to make.

1:2:41

Now.

1:2:43

Now, I need to have an agreement with the hospital,

1:2:49

what is there acceptable accuracy?

1:2:52

We're just system being, hospital will have to agree that, okay, we are okay with 7% error.

1:2:58

It is not my decision.

1:2:59

All this while, we have been doing machine learning and we have been trying different models.

1:3:04

Which models 90% accurate, some 93% accurate, some 97% accurate.

1:3:09

Every time we are saying, okay, sir,

1:3:11

whatever best model is, we use can.

1:3:13

there, but the best model will never be 100% accurate.

1:3:17

That test data may be 97, 98% accurate it's in the area, not 100%.

1:3:21

That means you have to accept a 2% error.

1:3:23

Now, that 2% error, who is called?

1:3:26

Not your call, right?

1:3:27

It's the call of the people who are paying you.

1:3:29

That's the hospital who are hiring are, that is their decision.

1:3:34

That sign can be except 2% error.

1:3:37

I mean, so patients may say two patients won't, which we're prediction is wrong.

1:3:43

Now, you say, sir, this hospital can decide how will hospital decide their error rate?

1:3:51

And medical science may actually error rate 2% is very high.

1:3:54

You cannot afford that.

1:3:55

Like, if somebody's tumor has, so that is like somebody, the model incorrectly says benign or cancerous and that's a big deal.

1:4:08

So 1% is actually a very high error.

1:4:11

So you have to go below 1%.

1:4:13

And the baseline is always the human baseline.

1:4:17

If your hospital's in the positions, it's how much error are.

1:4:21

Because physicians be mistakes are already.

1:4:23

Physicians are also making mistakes.

1:4:25

So the baseline is always that baseline.

1:4:27

So usually we do, we'd do, we'd do 2,000 data points let out of 1,000 data points,

1:4:33

we say, okay, the hospital will evaluate.

1:4:35

The hospital's internal team will evaluate, that, okay, out of 1,000 data points,

1:4:40

I have sign on one hand, who has built a nice model,

1:4:42

and his model is 99% accuracy.

1:4:45

Let's, that's a 1% error is.

1:4:46

So if we're a thousand data points sign-ca model to do it,

1:4:51

then 10 errors will.

1:4:54

But that he,

1:4:55

if we're our doctors team to do this,

1:5:00

they're a hospital decide to.

1:5:01

The same thousand data points,

1:5:02

if I'm giving to my doctors,

1:5:05

so how are my doctors able to 100% do everything correctly?

1:5:09

That's not?

1:5:09

Doctors, be mistakes.

1:5:10

They're not?

1:5:12

That is how they take a call.

1:5:14

That is how the hospital will take a call.

1:5:16

They will take a call based on the error,

1:5:19

and they will also majorly take a call based on the cost.

1:5:23

Now, that he's the whole thing to do,

1:5:24

he has to panel of 10 doctors hire to.

1:5:26

That does doctor hire to the cost of,

1:5:29

compared to how much they are paying me 1%,

1:5:31

one person who's just that pay the money,

1:5:33

if I am giving them only 1% error,

1:5:36

and if the panel of doctors is also giving them 1% error,

1:5:40

and they're paying me 1 tenths the cost,

1:5:42

you tell them,

1:5:42

me from a management perspective, what will they do?

1:5:45

They will, of course, hire me.

1:5:47

Because they don't need the 10 doctors.

1:5:49

He's who does doctors,

1:5:49

they need a lot of them.

1:5:51

I am able to do all that.

1:5:53

One percent error doctor's

1:5:54

also. One percent error in

1:5:55

one percent error,

1:5:56

we're doing on the real data.

1:6:00

So, you'll see a hospital check

1:6:01

not with me.

1:6:02

We've made the model made it.

1:6:04

Now, hospital, when they are trying it live on their system.

1:6:07

Now, they're looking at,

1:6:08

that, okay, say,

1:6:09

okay, a percent error will be.

1:6:12

Our physicians,

1:6:12

all the same percent error are.

1:6:14

So, okay, I will choose sign because

1:6:16

I must have to hire these 10 doctors.

1:6:20

This is the way how management will take a decision.

1:6:22

In many other real world scenarios,

1:6:24

I'm just trying to give you one sense.

1:6:27

So this is about business decision.

1:6:29

That FP, what N, and what accuracy is.

1:6:31

This is our call not.

1:6:33

Conceptually, you please remember whatever I've taught you.

1:6:36

You have to build the model with the best accuracy.

1:6:39

Lowest false negative, right?

1:6:41

False negative, least only.

1:6:42

Because false negative, here

1:6:44

there's very dangerous things.

1:6:45

False negative,

1:6:46

model predicted you don't have cancer,

1:6:48

actually you do.

1:6:49

So these are concepts we have discussed.

1:6:51

But at the end of the day,

1:6:52

how much error is acceptable?

1:6:54

100% never will.

1:6:56

How much is acceptable?

1:6:57

That is a business decision.

1:6:58

It boils down to hard money.

1:7:01

It's all money.

1:7:02

It's on money.

1:7:04

If I am doing the same error

1:7:06

and the doctors are doing the same error,

1:7:08

who will keep?

1:7:09

If the money are less than,

1:7:10

if they're less than,

1:7:11

there are legal mandates.

1:7:14

In India, there are laws, obviously, like,

1:7:16

I don't think you will want to visit a hospital

1:7:18

where they are saying,

1:7:19

that's a report,

1:7:20

AI,

1:7:21

that's a different conversation.

1:7:24

I'm not getting to that,

1:7:25

but there are some legal mandates

1:7:27

and some law are, obviously,

1:7:29

but I'm just telling you from a practical sense

1:7:31

how enterprises are thinking nowadays.

1:7:33

Error is completely a business decision.

1:7:35

Okay?

1:7:36

Yeah.

1:7:38

Sure.

1:7:41

customer is the one who is giving me the work right now.

1:7:45

They are saying this is the work you have to do.

1:7:47

We have this is the data.

1:7:48

Those are all initial conversations that will happen.

1:7:51

That's then we'll connect.

1:7:52

I will sit with the hospital administration.

1:7:54

Hospital just are betting the systems.

1:7:56

Where where there is data has,

1:7:59

if he has a database,

1:8:00

you have SQL for right?

1:8:02

Hospital data where stored are you?

1:8:04

What is their problem?

1:8:06

What are we trying to solve?

1:8:07

Do they have the data?

1:8:08

These are all initial conversations I will have.

1:8:10

have.

1:8:11

Study the requirements.

1:8:12

Requirements from customers.

1:8:13

If data, if there are,

1:8:15

data not there, then how collect can we?

1:8:17

Acceptable accuracy.

1:8:19

We call it a baseline accuracy.

1:8:22

Baseline, I mean, we can't we can't

1:8:24

at least are you okay with a 95% accuracy to start with?

1:8:28

5% error start.

1:8:30

And then we will sign a contract and we will agree upon,

1:8:33

we'll, we'll take it, we'll take it

1:8:34

we'll take it over time.

1:8:36

So if I'm starting as a consultant,

1:8:38

we will say, okay, I will start,

1:8:39

I will start with 5% error and over a period of 5 months,

1:8:43

I'm us to 1% to take it.

1:8:45

So that is a commitment I give to a hospital.

1:8:47

So these are all conversations that will happen.

1:8:49

You can see there's a lot that is going beyond Python,

1:8:52

beyond just a code, beyond just taking a dot read CSV

1:8:55

and promoting the data building a model.

1:8:57

All this is a very small part of the thing.

1:8:59

Ultimately, a lot of the decisions are taken by business.

1:9:02

He will you tell you what you'll tell you.

1:9:04

We are just implementing this in Python.

1:9:06

That is one part.

1:9:07

But a large part of it is happening outside of this world.

1:9:09

purely business decision.

1:9:11

Cost benefit analysis, right?

1:9:14

Does doctor in hospital?

1:9:15

What's how cost is?

1:9:17

What benefit?

1:9:18

What is.

1:9:19

The way?

1:9:19

If our Python's a model,

1:9:22

same kind of,

1:9:23

as a 110th or 120th of the cost

1:9:25

so we're not to have this doctor in hospital.

1:9:28

Apart from the legal and ethical mandates,

1:9:30

that's a different conversation.

1:9:32

But apart from that mandate,

1:9:33

yeah, so do you say,

1:9:35

how enterprises will think,

1:9:36

not only for medical, but for most use cases.

1:9:38

where we are saying,

1:9:42

if an AI can automate this thing,

1:9:44

then where is the cost?

1:9:46

What is the cost?

1:9:46

What is the benefit?

1:9:47

These are things you have to evaluate.

1:9:50

Uh-huh.

1:9:53

Okay.

1:9:55

So those are challenges, see,

1:9:57

that's what I discussed.

1:9:58

Those are real challenges,

1:9:59

as I said already, right?

1:10:00

So, yeah, absolutely.

1:10:03

So that is become the data availability,

1:10:06

you know, interoperability problem.

1:10:07

That's obviously.

1:10:08

Model monitoring account is like,

1:10:11

whatever model we deploy,

1:10:13

so the models we're doing,

1:10:14

whatever models we deploy,

1:10:16

this hospital can say,

1:10:19

whatever model we are built,

1:10:22

right?

1:10:22

Whatever model we are built,

1:10:24

and we are trying to evaluate

1:10:27

how that model is performing in production.

1:10:31

Now, our use case is

1:10:32

cancer prediction.

1:10:34

So we've got data,

1:10:35

we made, model, we find out the best model.

1:10:38

All of you remember these things,

1:10:40

logistic, decision,

1:10:41

we, random forest,

1:10:42

three models we'll make.

1:10:44

That's two minute's work.

1:10:45

Basically, I'll show the code to you.

1:10:47

Two minute's a notebook is basically today.

1:10:49

That's why I'm taking the liberty of

1:10:50

conceptually talking about some of these things.

1:10:53

So, data, Leah, logistic, decision,

1:10:56

we will build three different models.

1:11:00

Okay, and we'll choose the best care.

1:11:02

Done.

1:11:03

Our 99% accuracy

1:11:06

is the customer requirement

1:11:08

satisfied

1:11:08

got it,

1:11:09

we're deployed

1:11:10

we're doing.

1:11:11

The application

1:11:12

made it.

1:11:13

Now,

1:11:15

that customer

1:11:15

hospital

1:11:16

in all this that I'm

1:11:18

doing is something

1:11:18

that I'm developing.

1:11:20

As a developer,

1:11:21

I'm doing all this.

1:11:23

But as

1:11:23

we've finalized

1:11:25

that this is the best

1:11:26

model,

1:11:27

I'm giving it to the

1:11:28

hospital.

1:11:29

That hospital

1:11:30

that hospital's application

1:11:31

run

1:11:31

to be.

1:11:34

That is where I have to

1:11:36

monitor the model in production.

1:11:38

I mean, how it is

1:11:39

executing in the hospital's

1:11:41

internal system.

1:11:42

Ab-tac-to-

1:11:43

I was only taking

1:11:44

train data,

1:11:45

test data in my

1:11:46

local environment and

1:11:48

I was evaluating.

1:11:49

By our train

1:11:50

and our test in

1:11:50

how the model is doing.

1:11:53

But when

1:11:54

the same model

1:11:55

has been deployed

1:11:57

on the hospital

1:11:58

website,

1:11:59

hospital application,

1:12:01

as and when

1:12:02

real patients are

1:12:03

coming, trickling in,

1:12:05

every day,

1:12:06

real patients are

1:12:07

it.

1:12:08

Those parameters

1:12:09

are captured

1:12:10

X1, X2,

1:12:11

X3,

1:12:11

X4, blood pressure,

1:12:12

all this stuff.

1:12:13

That model

1:12:14

predicting

1:12:14

that patient

1:12:15

cancer

1:12:16

prediction

1:12:17

what is

1:12:19

model monitoring.

1:12:21

You are

1:12:21

tracking it

1:12:22

live how

1:12:22

things are

1:12:23

getting predicted

1:12:24

in production.

1:12:26

And I'll give

1:12:26

an example to your

1:12:27

timeshu.

1:12:28

There's

1:12:28

your model

1:12:30

your model

1:12:31

a human loop is

1:12:33

always there.

1:12:34

Even in real world

1:12:35

scenario today.

1:12:36

Everything is not AI.

1:12:38

Definitely

1:12:38

AI is the first step.

1:12:40

Now here

1:12:40

here

1:12:40

here at the hospital

1:12:41

first

1:12:42

doctors

1:12:42

take.

1:12:43

The hospital

1:12:43

has decided

1:12:44

we need

1:12:44

10 doctors

1:12:45

need

1:12:45

need to

1:12:45

pay.

1:12:46

There's

1:12:47

there's

1:12:48

that we're

1:12:48

doing

1:12:48

that we

1:12:49

have

1:12:50

no

1:12:51

any

1:12:51

pay.

1:12:52

So 10

1:12:53

doctors you're

1:12:54

paying a lot

1:12:55

more

1:12:55

compared to

1:12:55

what you're

1:12:56

paying only

1:12:56

need.

1:12:57

So hospital

1:12:57

is decided,

1:12:58

we will hire

1:12:59

him and

1:12:59

we will do our

1:13:00

work.

1:13:00

But that

1:13:01

that will

1:13:02

release not

1:13:02

will release.

1:13:02

He's

1:13:03

maybe 9

1:13:03

released and

1:13:04

one

1:13:04

gave.

1:13:05

And that one

1:13:06

he

1:13:06

took

1:13:06

that one

1:13:07

he will

1:13:09

be the

1:13:10

human

1:13:10

evaluator.

1:13:13

Our

1:13:13

the models

1:13:14

predict

1:13:14

are the

1:13:15

doctor

1:13:15

that

1:13:15

he's

1:13:15

that

1:13:16

our model

1:13:17

really

1:13:17

is actually

1:13:17

called

1:13:20

human

1:13:20

evaluation.

1:13:22

Now if the

1:13:22

the

1:13:22

thing

1:13:22

AI

1:13:23

will be

1:13:23

so AI

1:13:24

so AI is

1:13:24

right

1:13:25

or

1:13:25

are

1:13:35

okay if I'm able to explain to you,

1:13:36

So my model when it is running on the production system,

1:13:41

as in when real patients are coming, it is predicting, is it,

1:13:45

is it malignant?

1:13:49

Model

1:13:50

predict

1:13:50

I'm predicting, I'm monitoring that,

1:13:53

that based on this model

1:13:54

has predicted benign,

1:13:55

the model has predicted malignant,

1:13:57

that tumor

1:13:57

is, tumor

1:13:58

there, tumor

1:13:58

and

1:13:59

we're also tracking,

1:14:01

that doctor

1:14:02

has feedback

1:14:02

did.

1:14:04

I mean,

1:14:05

my model has predicted

1:14:06

that,

1:14:07

he's,

1:14:08

the doctor

1:14:08

said,

1:14:09

he's not

1:14:09

that is

1:14:11

what I am tracking,

1:14:12

monitoring,

1:14:14

okay, my

1:14:14

model is

1:14:15

giving errors right

1:14:16

now.

1:14:17

Why are

1:14:17

it?

1:14:19

What's a record

1:14:19

in error

1:14:20

there?

1:14:21

What's a

1:14:21

record is,

1:14:22

where

1:14:23

my model

1:14:24

said,

1:14:24

but that

1:14:25

doctor, the

1:14:26

doctor who

1:14:27

was retained,

1:14:28

he's

1:14:28

more

1:14:28

saying,

1:14:29

he's more

1:14:29

more

1:14:30

being.

1:14:31

And this

1:14:31

how is?

1:14:32

Is it happening one of

1:14:34

cases?

1:14:35

it that over a period of time, over weeks, it is declining?

1:14:38

But the error

1:14:39

are going to go

1:14:39

then it's a concern.

1:14:41

If errors are increasing,

1:14:43

then that we're

1:14:43

going to say,

1:14:44

you know,

1:14:45

then I have to monitor.

1:14:47

I have to monitor the performance

1:14:49

of the model.

1:14:50

Make sense?

1:14:51

That is the concept of model

1:14:52

monitoring.

1:14:53

So whatever models you're building,

1:14:54

you're evaluating the

1:14:56

performance of the models

1:14:57

on the production system.

1:14:59

And the ideas are very similar.

1:15:00

Whatever we have discussed,

1:15:01

transfusion matrix,

1:15:02

same thing that we're going to do.

1:15:03

But there are real data

1:15:04

I'm doing.

1:15:05

Here, it's just train and test data.

1:15:08

All this that we have discussed is just from the developers point of view.

1:15:13

Large part what I've been talking about right now, all this, why, is mostly from a production

1:15:17

system point of me, how things will be in the big picture.

1:15:21

So you're

1:15:22

you're from, that, that's

1:15:24

in the hospital

1:15:24

use

1:15:26

there you're monitoring

1:15:28

that,

1:15:28

when you're real patients when are being,

1:15:30

your model is predicting

1:15:31

cancer or not cancer, right?

1:15:34

Yeah, that prediction is it?

1:15:38

It's predicting cancer.

1:15:39

But,

1:15:39

but a doctor

1:15:40

is,

1:15:40

that's a error.

1:15:43

That is what model monitoring is.

1:15:45

It's a very, very critical part of the machine learning

1:15:47

life cycle.

1:15:49

That's a very different thing altogether.

1:15:50

How we do it, all that is very different.

1:15:52

But I just wanted to give it a idea to you.

1:15:53

People should know what it is.

1:15:55

And many of these topics are very overlapping with agents and all that we will study.

1:15:58

Because,

1:15:59

because we have in machine learning in monitoring

1:16:02

and what we're monitoring

1:16:04

things very similar.

1:16:05

That's why I told you there's a lot of overlap.

1:16:07

When we're most of topics

1:16:08

can, then kind of

1:16:09

overlaps will, so we'll see some

1:16:12

more things there, okay?

1:16:14

And as I said, absolutely,

1:16:16

absolutely. So unseen data

1:16:17

don't need to, so definitely

1:16:19

production in the unseen data

1:16:20

will be and very much the whole idea

1:16:22

is based on X, you are trying to predict why.

1:16:25

So that's expected

1:16:25

is, you're ultimately

1:16:27

production in you will have

1:16:29

you will ultimately have

1:16:32

X1, X2, X3 and based on that you will

1:16:34

want to predict some Y. That is expected, right?

1:16:38

So you will have the input X's, and based on that,

1:16:40

you will predict the Y. So that,

1:16:41

that's unseal. But I think what I,

1:16:43

what you meant to say is,

1:16:46

sir, if patterns see unseen,

1:16:47

that's a lot of case that

1:16:50

we're not going to, so case that

1:16:50

we're not going to be trained

1:16:52

so that's a disaster. So that is your

1:16:56

skill as a data scientist, that is

1:16:58

your skill as a data scientist to ensure

1:16:59

that your training data is good,

1:17:02

that your training data is represented,

1:17:04

relative, that's still

1:17:06

so you will have to ensure that you take all

1:17:10

possible cases of data

1:17:11

and nothing is taken that is unseen.

1:17:17

Or this will

1:17:17

imagine, I'll give you a very practical

1:17:22

scenario, I'll give you a very similar scenario

1:17:24

I'll give you. Imagine

1:17:25

you, again, again, the same hospital use some

1:17:28

let's, okay? So the hospital's

1:17:30

the system has, you started working for the hospital,

1:17:33

hospital has data shared

1:17:35

and all the patient's age is

1:17:37

from zero to 70 years.

1:17:41

70-year-old

1:17:42

people to hospital

1:17:43

have data. These are people who

1:17:46

have consulted the hospital the last

1:17:47

one or two years. We have got

1:17:48

data. But all are up to 70 years, okay?

1:17:53

And we've made us up to

1:17:54

model, train, test, plate, whatever,

1:17:55

table appellant we've made,

1:17:57

application in deploy,

1:17:59

production in production, I'm doing

1:17:59

monitoring, all very good

1:18:01

doing. My model is

1:18:03

giving excellent answers. Whatever my

1:18:06

model is predicting, that evaluation

1:18:08

be barabar over how it.

1:18:09

His in-house physician is also agreeing,

1:18:11

that, okay, this tumor,

1:18:12

he's a bit tumor and it's agreed.

1:18:15

But now what happened, there's a person who comes

1:18:18

to the hospital, who is 95 years old,

1:18:20

which is 95 years old.

1:18:22

And this is very interesting.

1:18:24

Because 95 years old person's

1:18:26

data in our training

1:18:28

in our training may never.

1:18:29

And 95 years is the age where people

1:18:32

develop a lot of complications.

1:18:33

and my machine learning model was never trained on that.

1:18:39

My machine learning model,

1:18:40

the data is,

1:18:41

that was only having data from 0 to 70 years.

1:18:46

All right now.

1:18:48

Now, a chance, say, one day,

1:18:50

a person registers in the hospital, age, 95 years,

1:18:53

person named this, diabetes, this, cholesterol, this, this, this, this.

1:18:56

And my model has to predict,

1:18:57

that, he's cancer, he doesn't.

1:19:00

Model to give me, but my model will not answer.

1:19:01

But my model will not.

1:19:03

do a good job. Because there might be some hidden cases, some patterns which my model doesn't

1:19:07

understand right now.

1:19:08

That age bucket my model has never seen.

1:19:12

So, Garima, that's the answer to your question.

1:19:14

These cases where what we do in the real world,

1:19:18

I just wanted to give the scenario to all of you.

1:19:19

This scenario, this is very practical scenario.

1:19:22

Now, what will you do?

1:19:23

So you'll, you'll, so you'll, you'll, so you'll, obviously, you'll have to start?

1:19:27

Now, the hospital, we've got to contract

1:19:28

and then what do you?

1:19:29

If the hospital has zero to 70 years' data, we'll do, we'll do not do?

1:19:32

No, I have to,

1:19:33

start. A model, model was working fine until now.

1:19:37

Now, 95 years, Banda's data

1:19:39

so, now we have got, this is something wrong.

1:19:42

This is exactly what my model monitoring will come with the

1:19:45

timeshu was saying.

1:19:46

Now we'll monitor this is the very unseen kind of a use case.

1:19:51

My model has never seen that kind of a pattern.

1:19:53

This is a very old person.

1:19:55

It's kind of complications have, which I have not trained my model on.

1:20:00

So my model will still predict.

1:20:01

He will still predict, that he'll still predict,

1:20:02

that the banda cancern is, he or not.

1:20:03

He'll predict, yes, no, answer, to do.

1:20:05

Classification.

1:20:06

Everything is sorted.

1:20:07

But the answer will, that may not be something that I'm very confident about.

1:20:13

Evaluation, the human evaluation is, well, but it might be an incorrect answer.

1:20:19

Now, this is where, as a developer, I have to go back, I have to collect that data.

1:20:23

And I have to say, okay, this is a very new pattern that I saw.

1:20:26

Where there my prediction incorrect there, so we'll take, so we'll go.

1:20:32

And we artificially, four, five, or data points,

1:20:38

70 and 900-age group in create, we try to artificially create some more data with similar patterns.

1:20:49

So that I have more data of older people.

1:20:52

Yeah, to artificially via, or hospital consultation said, yeah, we'll put more data in that older age group.

1:20:56

So we'll put more data in that older age group.

1:21:00

And with that I will retrain my model.

1:21:02

then I will once again deploy it.

1:21:06

This is basically the big picture idea how things happen in cactus.

1:21:12

I hope that answers the question for you very much.

1:21:17

Sure.

1:21:32

Okay. Let's move on. Let me just share this with all of you. So a lot of interesting discussions today.

1:21:39

Always good. And this is again part of part of what I wanted to keep some time aside for today.

1:21:44

I wanted to keep some time aside to give you the big picture idea, how things happen, how things work.

1:21:50

Baki to simple. We will see the case study. We'll see the things, whatever we have discussed so far.

1:21:55

We'll see that now. Okay. Just a minute.

1:22:02

Thank you.

1:22:32

Thank you.

1:23:02

Thank you.

1:23:32

So you want to take a short break and come back.

1:23:50

I'm just going to take a short break and come back.

1:23:52

I'm just going to also share this case study in the drive.

1:23:55

So take a short break and see you back after the short break.

1:24:00

Take a short five minutes break and take a short break.

1:24:02

faculty. Yep. Okay.

1:24:32

Thank you.

1:25:02

Thank you.

1:25:32

Thank you.

1:26:02

Thank you.

1:26:32

Thank you.

1:27:02

Thank you.

1:27:32

Thank you.

1:28:02

Thank you.

1:28:32

Thank you.

1:29:02

Thank you.

1:29:32

Thank you.

1:30:02

Thank you

1:30:32

Thank you

1:31:02

Thank you.

1:31:32

Thank you

1:33:32

Thank you.

1:33:36

Hi.

1:33:39

Hi,

1:33:40

Hi,

1:33:42

Welcome back.

1:33:43

Welcome back.

1:34:02

Thank you.

1:34:32

Thank you.

1:35:02

Thank you.

1:35:32

Thank you.

1:36:02

Thank you.

1:36:32

I'm just sharing the

1:36:46

the particular the particular the particular the particular

1:36:49

with all the particular thing with all of the

1:36:53

everybody on the on the Google right. Everybody can navigate over to the the Google right.

1:36:56

Right.

1:36:57

That is in the fifth May folder.

1:36:59

All of you please navigate over to the on the Google Drive.

1:37:01

All of you please navigate over to the Google Drive.

1:37:02

5th May folder.

1:37:05

Yeah.

1:37:10

And they have uploaded the demo.

1:37:31

what IP by NB file, everybody can see.

1:37:46

Very basic.

1:37:49

Yeah, yeah, I've uploaded that.

1:37:50

All if you can see.

1:37:51

Here it goes.

1:37:53

Demo.

1:37:54

Type you by NB.

1:37:55

You don't have to solve it.

1:37:57

I've pretty much already solved certain portions of it which

1:38:00

of it, which we'll be doing right now. As I already started my discussion today, that it's going to be kind of very much related to whatever we have done until now. We'll go over the pieces once again. Yeah. Okay. You're able to see? Everybody's able to see the case study thing. Let me know, please. Okay, very nice. Very nice.

1:38:30

Okay, very good. Please open it up on Collap. Everybody can please do this and Collap. Let me also do it on Collap with it. No need to do it on BS code with a better system. I'm also opening up my Collap. We'll do the exercise here completely.

1:38:50

All right. So connect to the kernel, top right, connect to the runtime. That's the first thing we are doing. The first thing we are

1:39:00

to the runtime. Let us see that in action. So first thing we are, we are connecting to the runtime.

1:39:09

And now I will go ahead and import Pandas as PD, import NMPi as NP. We are loading that if necessary packages and we are loading the breast cancer data.

1:39:28

If you want to see the data set, if you want to just understand your data a little, you can see that.

1:39:34

You can see what your data consists of right now.

1:39:37

You have data go take a look at you data.

1:39:40

Anyways, this is coming as a kind of an array format, which is not that easily understandable.

1:39:47

But if you want to, if you want to see the data in a better way, you can go ahead and let me also use a bit of Gemini here.

1:39:56

Okay, I'll take set you up with a query query.

1:39:58

go. These are things everybody should be comfortable using right now. But I think even

1:40:04

without using this, you are able to see, right? You were able to see that we have got a predefined

1:40:08

data set. So the pre-built data set that we are loading. But I've seen that this data is not

1:40:15

returned as a, it is not returned as a data frame.

1:40:22

That we're going to print kind of the data frame case of print. It's not a data frame actually.

1:40:27

It is an internal file format.

1:40:28

But internally, it is taking the data from here.

1:40:31

When you see the cancer data site, it is loading the data from here.

1:40:34

Here from here from here. So if you want to study your data, you can't study your data. You

1:40:39

don't have to use much. This is just for your reference. This is a very popular data set.

1:40:45

We've in class maybe it is not in nothing new. Cancer, we've in class where basic level

1:40:51

discussed here. So quick picture idea is based on all these input features, we want to

1:40:58

There are total 32 variables we have.

1:41:02

And if you want to see the CSV, we have CSB.

1:41:04

We have CSB we have KV. We have you

1:41:05

have to help us share there's no problem.

1:41:09

Because here we are using a predefined data set.

1:41:12

I just wanted to make it easy for everybody.

1:41:13

No, you you have to have CSP load and do it. But that's okay.

1:41:16

Let me share that also with me so that everyone can see the data.

1:41:23

Is your

1:41:24

I've already uploaded this in the 5th May folder and I'll take you,

1:41:46

your data set in. This is how your data looks like.

1:41:50

ID column to care, you can drop it. You can drop the ID column too there. You can drop the ID column. It's not required.

1:41:54

So whatever we are trying to do, you can completely drop the ID column.

1:41:58

And these are the features we are talking about.

1:41:59

Radius, mean, texture, all these are the inputs.

1:42:02

These are all the inputs we have.

1:42:03

So every row stands for one person.

1:42:06

So 1% of cancer cells the features basis we are trying to predict.

1:42:10

Is the diagnosis benign or is the diagnosis malignant?

1:42:13

So that is the problem that we are trying to predict.

1:42:17

So based on the features of the person, we are trying to predict is the diagnosis benign or it's the diagnosis malignant.

1:42:24

Is it B or it's the diagnosis malignant?

1:42:24

is it empty. That is the problem that you are trying to solve. So benign

1:42:27

it's okay. It's a treatable form of cancer. For malignant, it is dangerous form of cancer.

1:42:32

That is your data set basically. Okay. So again, we'll take work

1:42:36

not to the actual solutioning. So you split your data, train test plate, whatever we

1:42:42

have talked about before, right? So this is test size 0.2. What is the meaning of test size

1:42:46

point two? That means 80% of your data is part of training and the remaining 20% is part of testing.

1:42:52

That is how we have managed to split our data.

1:42:54

Now we will now start our model building using pipelines or this is the way how we will be

1:43:02

we will be a kind of kind of proceeding right now over on. Okay, let us see. Let us continue on.

1:43:17

There is no particular reason, Sanghi Dato. So just a general one that you have taken. It's just a

1:43:23

a breast practice. There is no particular reason. But you can take anything. The point is

1:43:29

whatever random state you take is just this is very common seed value that you use. You know,

1:43:35

it is like, Sangha, it is like saying, he, uh, sir, we're NPQed. These are very good questions,

1:43:43

actually. You know, these are very good questions actually. Now, look, in four pandas as speedy Q are. There is no

1:43:47

reason. You can't it. And I'll, in fact, there's a very funny thing. Uh, there's,

1:43:53

what kind of people do they reverse it.

1:43:55

You can do import Pandas as NP or you put Numpai as PD.

1:43:58

You're confused. Because whenever you go to GitHub, you

1:44:02

you'll go to GitHub, you'll go and see some

1:44:05

quote snippets from online. Or Germany may have generated

1:44:08

this is not their typical practice.

1:44:11

So this is the general accepted practice.

1:44:13

That's the same way, if you ask me,

1:44:16

if you ask me, he, sir, we'll take. That is the general accepted practice.

1:44:20

You know, if you ask me, if you ask me, say, sir, we'll take it. That is the general accepted practice. Now

1:44:20

if any code Google caro. In fact, you're Gemini, GP.

1:44:23

say code generate that will be you usually 42 say they're going to that's the that's the

1:44:27

that's the intuition right now. Okay. Now. Now let's move on. So as we discussed, we have loaded our

1:44:40

data, training data, testing data. Yeah. And now what is that? Uh, absolutely, absolutely.

1:44:49

For normal tabula or data, you usually could circle before splitting.

1:44:53

Yes. Otherwise, training may get one pattern range and testing another, which can bias the accuracy.

1:44:59

Right? So in train test split, you can do shuffle equal to true.

1:45:03

Is that, you know, is the default, actually. So shuffle equal to true default. I can't you, I think you were there in my last class.

1:45:09

Last class, we have time series basic level in the. So shuffle equal to false

1:45:13

we particularly, because I discussed the chronological order, right? So here here, if you're

1:45:18

if you're in train test split by default, the default is always shuffle equal to true. Can you see?

1:45:23

is always equal to proof.

1:45:24

If you're not even if you're not by defaulted by default. So that is the reason why we do it.

1:45:28

We try to shuffle our data because we don't want the order to be maintained. That's the intuition.

1:45:33

There is nothing we have to do particular. That is part of the process.

1:45:37

Now next we are building the pipelines. So we have already seen this kind of a flow before.

1:45:42

So subse first we are scaling the data. Whatever data we have, we are scaling it.

1:45:46

And then we are going and instantiating the different types of models. So first we are,

1:45:52

instantiating the logistic model. Next, the decision tree model. Next, the random forest model.

1:45:58

Okay.

1:45:58

Scaling, then model. Scale, model, scale, model. That is what we are doing right now.

1:46:04

Okay? So this is the pipeline.

1:46:05

First, our data will. We'll, we'll scale kare. Then we'll, then we'll basically, model will. That's

1:46:13

the way how well, how we'll proceed. Basically. This is how we are doing the right now.

1:46:17

So first I define the pipeline and then I'm prime. Then I'm fitting the models.

1:46:22

separately. Or this classification problem. Because it's the classification problem,

1:46:26

we are trying out first using logistic regression. Second, we are trying something called

1:46:32

decision tree classica, which is slightly better. If you remember, decision trees, we are

1:46:35

building three like structure. And third, we are using something called random forest.

1:46:40

What is random forest? A random forest is the collection of many, many decisions, even better.

1:46:47

So logistic regression is a baseline model, very basic model. Second, we have decision tree,

1:46:51

which is slightly better, slightly better, because we are trying to build a slightly more

1:46:55

complex model. And finally, we've got random forest, which is a collection of many, many decision

1:47:00

piece, which is an even more complex model, even better. It'll give even better performance.

1:47:05

Okay? So we have herep, model. Dot fit. And this is the standard piece of code. Model. Dot

1:47:10

X-ray and why we are doing it. And finally, the last part is model evaluation. The same

1:47:15

template that we have used before. Okay. Model evaluation, we are doing separately for logistic.

1:47:21

Now, look, logistic pipeline what is the pipeline for logistic regression.

1:47:28

We have defined the pipeline. We have done pipeline. Dot fit. And now we are doing pipeline.

1:47:34

Dot, dot score. Dot train, X train, and pipeline. Dot, X, train, and pipeline. Dot, X, Y,

1:47:40

test, Y, test. Okay? Simple. We have seen the accuracy. So using a basic logistic model,

1:47:45

what is the key learning right now? We are getting 98% training accuracy, 97% test accuracy.

1:47:51

This is what me as a developer is getting as I am working with the hospital data.

1:47:58

Hospital did us, the same story I was talking about with you in the beginning of the class.

1:48:02

So I get my data from the hospital.

1:48:04

I'm a train test made, we made a model and I am seeing that using the logistic regression model,

1:48:09

I'm getting 97.37% test accuracy.

1:48:12

So our unseen data is, my unseen data, not hospital.

1:48:15

My unseen data, whatever data I have kept as fixed.

1:48:19

So I know what I have got results can.

1:48:21

The developer level to testing to do, I am seeing 97.37% accuracy.

1:48:28

That means I am getting around 2.5% errors. Now, I will have to run it with my hospital to

1:48:33

understand whether this is acceptable or not. Whether this is acceptable or not.

1:48:38

And we're going to this on this. Here I'm doing classification report, but I can also generate

1:48:43

a Confucian matrix. What is the code for the Confucian matrix? All of you know this, right?

1:48:47

What is the Confucian matrix? The code is. This is Germany. So you have here on a line. You

1:48:51

so confusion matrix will do everything for you.

1:48:57

It will do everything for you. You have a confusion matrix code. That's it. Or you can already

1:49:01

see that confusion matrix right now. Whatever logistic model that I built, dot fit

1:49:06

got, dot predicted. O'gay. And now, what are you trying to do? What are you trying to

1:49:13

evaluate? You are trying to compare the actual why with the predicted why. That is what you are trying to do.

1:49:19

So logistic regression, I'm getting a pretty decent model.

1:49:21

the reason is because my data is very strong.

1:49:25

So even with such a basic model, you're able to see a very good quality result because my data

1:49:29

is very strong. My data is very good quality.

1:49:32

This is every case in any go. And we have seen use cases before.

1:49:35

Now, you know, credit default case study.

1:49:36

We have that case study up to dig out. And that time with a logistic model, we were getting a very bad

1:49:41

result. Then when we did gradient boosting, decision trees, we got better results.

1:49:45

But here you're able to see, even with a simple logistic model, you're getting a very good accuracy.

1:49:50

This is a great indicator that your data,

1:49:51

quality is very good. Our quality of data actually. So that is the inference we are able to

1:49:57

we are able to, we are able to broadly, you know, make out right now. Okay. Everyone is able to see

1:50:05

this. So and Confucian matrix, all of you remember, right? So this is what is called false negative.

1:50:13

But I'm getting a very good accuracy. There are three mistakes I'm making and one false negative.

1:50:19

But there is only one such case where model predicted not cancer, but actually it's a cancer.

1:50:27

So only one such dangerous case is happening.

1:50:30

Or you know how it's happening in Python?

1:50:34

Python may actually zero or one. I told you already. The order is always zero and one.

1:50:39

So there is only one such case where model predicted not cancer, not tumor, but actually it's a cancer.

1:50:46

So this is predicted versus actual.

1:50:47

Rows in always always always predictors. So there was only one such case where

1:50:57

model predicted zero actually is one. That is what you're able to see on the screen. Model predicted

1:51:02

zero actually it is one. So this is what it is. And now you will have to evaluate, sit with your

1:51:07

hospital administration. They are the ones who will have to take a call and they will have to say,

1:51:12

that by he acceptable is. Because this is a serious case, right? If there is a serious case, right? If there is one, if there is one,

1:51:17

such case where the person is actually having cancer but you are missing out, is that acceptable.

1:51:26

Now, you have to evaluate kind of our internal physicians, how much mistakes they are making.

1:51:31

This is exactly what I was mentioning in that first one hour. I was talking about how you check.

1:51:35

This is not your call. It's not that developer, you sit and say, sir, is it fine? I am nobody to say.

1:51:41

You are nobody to judge. Is it fine? You can build the best, you can do the best you can do.

1:51:45

you? You'll best say that you can I take some better data? Can I use a different

1:51:51

algorithm? Can I try some other hyperparameters? We'll say better model

1:51:55

can make them. Those are all things that you can try which are in your control, which are under

1:51:59

your control. But is this acceptable? Is, you know, is 97.37% test accuracy acceptable? That is not

1:52:09

your call. That is your hospital administration by the whether this model is acceptable or not.

1:52:14

Okay. Let's move on. And we have also discussed at a very high level, without getting into the formulas. I won't get into formulas today. It's only application today. We have also discussed the idea of F1's code.

1:52:27

F1's course say we are able to understand class level accuracy. You are able to see the performance of each and every individual class.

1:52:33

Not only are you seeing the overall accuracy, but you can also see the performance of each and every individual class.

1:52:39

For you have a logistic rate is being fairly well.

1:52:41

iteration two. We have decision free pipeline

1:52:45

made. First we are again doing scaling and then we are

1:52:49

building a decision free model at a basic level. Without any

1:52:53

hyper parameters, remember we have also talked about hyper parameters. Just say

1:52:56

decision free may we have talked about depth. Random forest

1:52:59

we talked about n-stimators. But here we're not doing it. We're not doing it. We're just

1:53:03

baseline models done. So the very common strategy that we follow. We first

1:53:08

build a basic logistic, basic decision tree, basic.

1:53:11

basic random forest, then we're going. Now let us see what I'm getting with a basic decision

1:53:16

fee. So with a baseline decision tree model, I am getting an overfit model, 100% or 94%.

1:53:23

Okay? Okay. So here here you can. If you want to tweak it, you can. You can definitely

1:53:32

tweak it. And we know this. We know how, you know, how it will work in the context of a decision

1:53:36

to do. So how will it work? How will it work?

1:53:41

it. What I will do? I will just bring this code somewhere here. Just to show this to you.

1:53:50

No, what I mean to say, basically. You can see this one in action. Just at a very high level

1:53:59

wanted to show you. Again, I'm instantiating the pipeline, but only differences this time, I will use the

1:54:04

maximum underscore depth hyperparameter. And I will use maximum depth equal to one. Now, what is the

1:54:11

meaning of max depth equal to one. You know when I was discussing decision. We actually

1:54:15

explained the concept that time. And I told you when you use depth equal to one, you were getting a very

1:54:20

basic model. You are asking only one level of question. And as you increase the depth of the decision

1:54:27

p, you are asking more and more questions and you are building a more and more complex model.

1:54:33

So we are increasing the model complexity. You know, up? In the very initial phase of the first

1:54:41

I have told you that when max depth equal to one, we are building a very basic model,

1:54:47

we are underfeit model. If we run it, you know, you can you see? In fact, let me run the code

1:54:56

along with this right now. We can we see? In fact, let me run the code along with this right now.

1:54:58

We'll just run it. You see, here depth equal to one here. When we're model we're making, it's

1:55:03

an underfit model. Can you see?

1:55:05

train accuracy nearer down and tests be nearer down. This is underfitted.

1:55:08

data, so you're getting a very good result, right? You're getting 92%, 89% you think this is great.

1:55:15

But we have restricted the tree to only one level deep. We are not asking it enough questions.

1:55:23

It's a very basic tree. So we have reduced the complexity. This is called underfitting.

1:55:29

Underfitting much is a very basic model. So, first, so logistic. That's done.

1:55:34

of decision 3K under, you can tune these knobs. Remember hyperparameters?

1:55:41

Hyper parameters are the knobs that you can tune. So maximum depth is a kind of hyper parameter.

1:55:46

You can use to control the depth of my tree. So when I take depth equal to one, you are getting a very

1:55:51

basic model. And when you, as you increase the value of depth, object is all of you. As you increase the value

1:55:57

of depth, you are making the tree slightly better. Updivate for train, 92 head test 89 here. As I increase the

1:56:04

depth slightly. Now, look, these both are here. Rain became higher, test became higher. This is a

1:56:09

slightly better model. As I increase depth to three, what will happen? As I increase the depth to three,

1:56:16

train became slightly more, test becomes slightly more. Everyone is able to see, 97, 94

1:56:19

it's gone. And as I increase the depth, what is going. Again, train barred and test barred. So as I'm

1:56:25

increasing the depth, my model is becoming more and more complex.

1:56:30

And you'll have you going to point you back to the specific class. And you know, I'm going to point you back to the specific

1:56:34

where I talked about it. I think this was back in my classification, you know, case study.

1:56:42

The 8th April should be discussed. No, not, I'm not sure the case April to, we discussed.

1:56:49

No, not 1st April. Maybe bring it up for you. I talked about it on 14th April.

1:56:57

14th April. I talked about this model accuracy curve. Okay? Model accuracy curve. Okay. Model accuracy curve, if you

1:57:04

I have specifically discussed this diagram for you.

1:57:07

We have you said that if you're building a very simple model, it is an underfeit model.

1:57:11

That means when max depth one will, then it was simple model, underfit

1:57:15

over.

1:57:16

Our training accuracy or testing accuracy don't know.

1:57:21

And as you increase the value of depth, your model becomes more and more complex.

1:57:28

It's an extreme that overfit shall go.

1:57:31

At least your train will touch 100 tests will,

1:57:33

reduce and you are trying to find out what is that value in between. And this exact process

1:57:38

is what is referred to as hyper parameter tuning. I mean so we are trying to find we are trying to

1:57:42

find we are trying to find we are trying to do hyper parameter tuning. So we are trying

1:57:46

out different different values of depth. Decision PKK under we are trying out different different

1:57:50

different values of depth. Dept equal to one depth equal to two depth equal to three. So we are trying

1:57:56

out different different values of depth maximum depth and we are trying to find out what is the

1:58:00

best you know value of depth that we can go for so we are also trying out different

1:58:08

different values of maximum depth and we are trying to figure out what is the best value

1:58:14

of maximum depth that we can go for what is the best value that we can basically choose

1:58:20

if you're a depth so much like if depth is equal to 100 that means you are having a very

1:58:27

complex model and what will happen needless to say you overfit

1:58:30

now you look train accuracy is 100% test has reduced so this is overfitting two conflicts so

1:58:37

what is the right value we have to find it on that is something we have to evaluate and this

1:58:43

process is what is called hyper parameter tuning so the key takeaway the key takeaway was going

1:58:49

from underfitting to overfitting if you tune the value of the hyperparameters very less depth

1:58:54

under fit very high depth overfit somewhere in between good fit here we make

1:59:00

So we are trying logistic, we are trying decision-pick, different values of depth.

1:59:04

Third, we will try random forest, different values of LSD meters.

1:59:08

That same thing we'll make sure.

1:59:10

So this was just to explain to you.

1:59:12

I mean we can't go right now because we already saw this piece here.

1:59:16

I've got to distract away from the main pole.

1:59:19

Yeah, try can't you, and finally, I will explain the same story with respect to random forest.

1:59:27

I will explain the same story with respect to random forest.

1:59:30

So this is the baseline random forest model.

1:59:33

Now if I again try to tune the hyper parameter, what is the main hyperparameter inside random

1:59:38

forest?

1:59:39

We have something called n underscore estimators.

1:59:42

You have you got we have got n underscore estimators.

1:59:45

Same story here also.

1:59:46

N underscore estimators is used to control the estimator.

1:59:49

It is used to control the complexity of the model.

1:59:52

So again, this your model accuracy curve got got it.

1:59:55

If n estimators value is equal to one, model will be highly under thing.

1:59:59

very basic model.

2:0:01

And as we increase the value of estimators, the model will be highly over there.

2:0:05

Now, you can see, when I use, I have to write one more line of code.

2:0:07

Sorry, I could fit it.

2:0:09

Now, look, given it, it identified automatically that was missing.

2:0:13

It did that for me.

2:0:14

Anyways, now I'll run the code and you can clearly see this is underfitting.

2:0:19

Underfitting.

2:0:20

Training or testing, don't have.

2:0:21

Now, data is it's so good, I'm still getting a good model.

2:0:24

And as you increase the value of estimators, you can see,

2:0:26

the model is becoming better and better.

2:0:29

So my training and testing, I'm expecting both will increase.

2:0:33

Both will increase.

2:0:33

Now, look, like, NSTEMators re-creded, my training also increased already.

2:0:36

Testing, 95% went.

2:0:38

So NST meters is that particular knob that we try to tune.

2:0:41

Okay, so we have already seen this.

2:0:42

And what is random for us, if you all remember, it's a collection of decision please.

2:0:45

I mean, this is what it is.

2:0:47

And again, NSTMAT has been more than what will.

2:0:49

What will, guys?

2:0:50

If NSTMATES is too high, my modern will over 50%.

2:0:53

This is again a bad thing.

2:0:56

Okay.

2:0:56

Now, now the important thing is, guys,

2:0:59

Now the important concept that I wanted to clarify is you can build a matrix table, right?

2:1:03

So whatever we are discussing right now, you can of course build a matrix table.

2:1:10

So here, comparison to we are already talking about here, but to compare in a better way,

2:1:14

what you can do, you can go and build a metric table to see everything at once.

2:1:20

And we can easily spot overfitting in a better way.

2:1:24

So here you can here you can make a matrix table where you can see,

2:1:27

that we have logistic model, we made, decision tree, we have made, and random forest

2:1:31

we've made, and here you can make it much bigger in the real one, right?

2:1:35

You can, any, our hyperparameters, you can, uh, different parameters, can you.

2:1:40

So here I've only taken three models trying to show you, that with a logistic model, we are getting

2:1:44

this much performance, with a decision tree model, we are getting this much performance,

2:1:47

and with a random forest model, we are getting this much performance.

2:1:51

And, and now you can see that this is exactly where we will go back and use some.

2:1:57

something called the, you know, something called the Occam's Razor principle,

2:2:01

which is, which is that if a simple model performs almost identically to a complex model,

2:2:07

we prefer the simple one because it uses less memory and is less grown to overfitting.

2:2:12

This is a very, very important concept even in the real world.

2:2:16

Even in the real world, it is like saying that if you can get something done using lesser resources,

2:2:21

if come pay some money, come resources, simply if something goes, why complicate control?

2:2:27

If I can use a simple logistic model, logistic regression is very easy.

2:2:32

And it actually takes very less time to fit compared to a random forest.

2:2:37

You will remember some of the exercises you might have done.

2:2:41

Random forest usually takes time.

2:2:42

If our data very big, I remember giving you that case study on UCI credit card.

2:2:47

This is all very simple.

2:2:48

It's number of rows are quite common.

2:2:50

But the credit card data set in the data set in there were 20,000 rows I remember.

2:2:54

And I think it was taking a lot of time to fit.

2:2:56

So, some of the times these complex models will take a long time to train, long time to predict.

2:3:04

So if you can get something done with a simple, in a simple manner, why not?

2:3:08

And the best big part is, if you're here here accuracy, very interesting.

2:3:12

Look at this.

2:3:13

Actually, my logistics is performing better.

2:3:16

Forget about train and test.

2:3:17

This is overfitting we discussed already.

2:3:19

But if you just compare based on the accuracy, accuracy wise also logistic is better.

2:3:24

And part of that has to do with my.

2:3:26

my data itself, my data itself is very good.

2:3:28

And this is exactly the evaluation part and the model comparison part that you will do.

2:3:33

Okay, there is no right or wrong.

2:3:36

Okay, don't tell me that sir,

2:3:37

which one should I use.

2:3:39

It's completely up to you.

2:3:41

This is nothing to do with your customer.

2:3:42

It's not as if the hospital will tell you to use this or use that.

2:3:45

Nothing to do with that.

2:3:46

Hospitals will not tell you.

2:3:47

You will have to take a call and you will have to decide which model is better.

2:3:51

Should I use decision tree?

2:3:52

Should I use random forest?

2:3:53

You will have to take a call and you will have to say,

2:3:55

if I this, you know, this particular, you know, this particular model is called it.

2:4:00

So that is what you will have to, you will have to basically work towards.

2:4:04

You have to figure out.

2:4:05

You have to figure out, you have to go and figure out which model is comparatively, you know,

2:4:12

comparative to that.

2:4:13

Yeah, absolutely.

2:4:13

Everything is at the end of the day trial and error.

2:4:15

Yeah, I mean, obviously with some, with some guidelines and with some intelligence.

2:4:18

Not that we are randomly doing it.

2:4:20

This is we're randomly not doing it.

2:4:20

This is we're randomly not doing.

2:4:22

You have data and we, we methodically, we have,

2:4:25

like, decisionary layer, random forested.

2:4:27

We have principles right now we know the principles,

2:4:30

that overfitting, underfitting, what and underfitting what,

2:4:32

n-stimators, what, maximum depth, we know the principles.

2:4:35

And now we are working on the basis of those principles.

2:4:38

It is not a random trial by error, but if I take you back to my very first machine learning session,

2:4:43

machine learning itself is a process where we do not know the roots.

2:4:48

Right, if you go back to the, you know, the absolute principles of ML,

2:4:53

in ML in we do not know the roots.

2:4:55

So we do not know the rules in machine learning.

2:5:00

And because we don't know the rules, we will have to take lots and lots of data

2:5:04

and the machine will have to learn the rules based on our data.

2:5:10

Because we don't know the rules.

2:5:11

We don't know the rules.

2:5:12

So machine will have to learn the rules from the data.

2:5:15

So that is why the trial by error happens.

2:5:17

Because we have rules not.

2:5:19

If we have rules know what is the function,

2:5:22

then we could have used that equation.

2:5:24

But we don't know.

2:5:25

That's the reason why we are trying.

2:5:27

I mean, not know.

2:5:27

That's the logistics and it's better than.

2:5:29

We don't know.

2:5:31

That's the intuition.

2:5:32

Again, going back to the very first class that we did, if you remember all those

2:5:35

conversations, we had rule-based AI, machine-running-based.

2:5:38

If we had a rule-based, if we had a statement-lidded.

2:5:41

But we have rules not.

2:5:42

That's the concept.

2:5:45

So now, next thing.

2:5:46

As I told you, it's largely a recap in the initial phase.

2:5:49

This is the part where I'm again demonstrating the same thing that I explain, overfitting,

2:5:53

undercutting, I'm trying to demonstrate here.

2:5:55

Okay?

2:5:56

Or joe be the things we have made up,

2:5:58

this is the same thing you can repeat for a regression problem also.

2:6:01

So I remember even California housing,

2:6:03

we've seen, this is again, the same content I'm taking.

2:6:06

This is already part of our content.

2:6:08

So the same California housing data that I'm taking right now.

2:6:11

But again, just wanted to let you know that how you will try out different,

2:6:14

different models, how you will try out different hyperparameters

2:6:20

and how you will build the best model.

2:6:22

So same thing, I'm doing.

2:6:23

I'm first scaling my data.

2:6:24

So scaling, we are doing because we want to ensure that we bring all our data to the same

2:6:30

scales, okay?

2:6:31

We have overall 20 columns and we are trying to ensure we bring all the 20 columns to the same

2:6:37

scales.

2:6:39

Okay, so each of the 20 columns that we have right now, we are bringing each of the 20 columns to

2:6:43

the same scales.

2:6:44

That's the whole idea of scaling that we are, you know, kind of doing right now.

2:6:49

Okay, so all the 20 columns, we are basically bringing.

2:6:53

to the same scheme. That's the first thing. And then we are doing first step, we are doing

2:6:57

linear regression. Second step, we are doing random forest regressive. So this is how we are proceeding.

2:7:01

And let us build the baseline model.

2:7:05

California housing, you have to, it's taking a little time because the data is bigger.

2:7:09

This is exactly what I wanted to tell you, that random forest takes a lot of time to train.

2:7:13

If you can get something done in a simple way, if, if, if, uh, linear regression's a calm

2:7:18

chandering, you can use that. But here herephe, that's not going to. Last use case. You have,

2:7:22

logistic was better. Logistic was faster and was also giving me higher accuracy.

2:7:26

So nothing like it. Okay?

2:7:29

Faster model and also more accurate. So definitely I will use it.

2:7:31

And this principle's name of Oscombe Grazer.

2:7:35

Okay, we call it. What is it called? It is basically called if you see, this is a general term

2:7:41

that we kind of use right now. So we basically call it

2:7:45

Occam's Razor. Okay. So just have you know, we don't have to get very,

2:7:52

you know, very deep into it.

2:7:54

But I'll just remember what it's called, sorry, where did I go?

2:7:56

Yeah, this is the, this is the, this is the thing that we are using.

2:7:59

This is called, it's called, it's called the Occam's Razor, kind of a principle.

2:8:03

So out of his, first, first, first, he asks what it is, okay?

2:8:07

And you can, and you can basically read about it.

2:8:09

Occum's reason has nothing to do with MN.

2:8:11

It's more of a, it's more of a problem solving techniques.

2:8:14

If I was for Wikipedia by download it, that's what I was trying to do.

2:8:17

If you, if you put it on Wikipedia, it says, it's a, it's a, you know, it's a problem

2:8:22

solving technique that recommends searching for explanations constructed with the smallest

2:8:27

possible set of elements.

2:8:29

But the idea is like, when I'm trying to solve a problem, when any life in life in problem

2:8:35

solve, let's start with something simple.

2:8:38

Let's start with something simple.

2:8:40

Then we start to iterate, get into more complex, more complex, more time.

2:8:44

That is what is referred to as Occam's flavor.

2:8:47

So this thing, when we use in, this is where it all boils down to.

2:8:51

So if a simple.

2:8:52

logic performs almost identically to a complex model.

2:8:55

If logistic's working, if my business is fine with the accuracy that I'm getting,

2:8:59

just that's it. That's it. I will not go with a more complex model.

2:9:04

But moment you go to California housing, scenario change will.

2:9:08

Scenario change will. Here, the simple model, here the simple model struggles.

2:9:13

You look, linear regression's only 57% of code.

2:9:16

In the code, it's simple. That's the dot fit, that's the dot score.

2:9:20

This is something you guys are all comfortable.

2:9:22

Analysis is what we are focusing on in today.

2:9:24

If you're looking, if you look, you'll look, you'll take 57% or 59% of it.

2:9:29

So here here linear regression is a simple model.

2:9:32

It is fast, but it is struggling.

2:9:34

The California housing data set is very complex.

2:9:36

We have many, many features and there are many, many patterns in the housing data.

2:9:40

And it is unable to represent all the patterns accurately.

2:9:44

It is unable to represent all the patterns accurately.

2:9:46

So here here we're here when I'm using random forest, we are getting a much higher accuracy.

2:9:52

They go random for us, say, I'm getting 80%.

2:9:54

So very clearly, this is a great example where when I'm using a more complex model,

2:10:00

when I'm using a more complex nonlinear model, I'm getting a better quality result.

2:10:05

My patterns are represented much better.

2:10:07

That is the thing.

2:10:08

So simple linear model, say it was not working out, but the moment I use a more complex model,

2:10:13

a more nonlinear kind of a model, you know, we are getting a more accurate result.

2:10:19

This is another one of the scenario.

2:10:20

But ultimately, it boils down to.

2:10:22

the business problem.

2:10:24

You can, again, you have to put yourself in the shoes of the company that has hired you.

2:10:27

So the company you have to hire you, you have to think that, okay, you know, the real estate

2:10:33

company that has hired me to do the housing price prediction.

2:10:37

What kind of accuracy are they find with?

2:10:39

Because your, you're your, you're just being used in some real world application.

2:10:47

You know, that application we'll now we'll be, you'll be able to be able to be able to be able to

2:10:51

unknown. I'm coming to that right now. So you have to use it in some real application.

2:10:57

So where users can enter, what is the price at which I can sell my house, things like that.

2:11:04

So you obviously want a model that is accurate. You don't want somebody to guess a wrong answer,

2:11:09

right? So, yeah, so, you know, enough about the real world thing. Let me talk about it for a minute.

2:11:14

Because we've got a lot of thing about you. Let me talk about this for a minute. Let me show you, let me show you, what do

2:11:21

mean by this real world. Let me take a minute. Only when you see it, you will get a field.

2:11:26

Then I'm back to use there. That how it is, how it is done and how is radio built. So we have

2:11:33

time. I think the last half and I'm let me get towards this conversation now.

2:11:38

Ah, Anki, just to answer to your question, yes, that's inference latency or prediction time. And you can

2:11:43

measure it to doodramatically by capturing the time before and the time after predict. That's a very good

2:11:47

question. It is called prediction time. Do you. One is your, uh, uh, uh,

2:11:51

you know, uh, training time. Training time. That is happening during model training. That is what I'm doing

2:11:57

in my Jupita notebook. What you're asking is also a great question. That is basically something that

2:12:01

happens during model monitoring. Some of you ask me this question, that said,

2:12:05

model monitoring, ma'am, we are tracking how well the model is predicting. How's predicting

2:12:12

how? Second, unkey, what we do. We are also measuring exactly what you're saying. We are predicting

2:12:17

how fast it is giving the answers.

2:12:19

user may to enter the model dot predict

2:12:23

so we try to programatically do it and we are tracking

2:12:27

the time before and after

2:12:29

prediction so that's the way how it can be done so it's very simple you can just

2:12:33

before you run the dot predict function of system

2:12:35

time look time stand after dot predict you take the timestamp and you can find it out

2:12:39

if you can you can you can Google out a little

2:12:42

of Germany in this go down though you can do percentage

2:12:44

actually percentage percentage time you can use not single time yeah you can use something

2:12:48

called percentage percentage percentage time just do something called

2:12:52

percentage time if you if you run something called percentage

2:12:55

percentage time, that you can also run something called percentage time it

2:13:02

you can Google a little bit about these two things and you can this will

2:13:05

so you have cell in a cell. So you run it in a cell.

2:13:10

Cell in the show you add this code down, use a bit of Germany.

2:13:13

So if you're going to run it, you'll give you time will give you

2:13:16

it's not so much time it's going to do that. I hope that's like because I'm just still running

2:13:21

this code all if you can see.

2:13:24

Yeah very nice. And while this happens I'm going to talk about the other part which is basically

2:13:40

saving the model to a disk. As I've been as I've been discussing on this while you guys, even in the

2:13:45

current California housing case study,

2:13:46

if you see that all of what we have been doing, okay,

2:13:49

now here we have, we have tried linear regression,

2:13:55

we have tried random forest regressant,

2:13:57

and we have already

2:13:59

talked about that,

2:14:00

you can take nST matters,

2:14:03

and estimators for come

2:14:04

if you have,

2:14:04

we have talked about that.

2:14:07

And then we have to tune the hyperparameters, right?

2:14:09

You have to find out what is the best hyperparameter.

2:14:11

So on that I'm doing right now,

2:14:13

I'm taking three NST matter value.

2:14:15

50 layers,

2:14:16

we don't know, I'm just taking randomly.

2:14:19

See, see, three values, then go to go

2:14:21

it's just so I just wanted to take three values and demonstrate in the class.

2:14:25

So, now go to execute it.

2:14:26

It took a lot of time, by the way.

2:14:28

If you, if you counted, I think one and a half minutes to

2:14:30

go ahead.

2:14:31

There are one minute's run here.

2:14:33

And you hover over it.

2:14:35

Okay, it's a collab in, but more practically,

2:14:38

three minutes actually.

2:14:40

If you look, the cell took around the approximately three minutes to run.

2:14:45

Can you see?

2:14:46

But a better way to track it is percentage time that I showed you.

2:14:50

So three minutes, can you believe it?

2:14:51

Three minutes for just three hyperparameters.

2:14:53

But in practice, what you will do?

2:14:54

You'll check again.

2:14:56

Because you don't know, right,

2:14:57

that if it's a $50 or $100 or $200, I'm not know.

2:14:59

I don't know.

2:14:59

NST method value what will.

2:15:01

I don't know.

2:15:01

So you can already start to see how much time it takes.

2:15:04

Model training takes a lot of time.

2:15:06

Initially, the model development is, we'll try

2:15:09

linear try and random forest try

2:15:11

and random forest try to.

2:15:12

Random forest under hyper parameters

2:15:14

that try and we'll try and we'll tune

2:15:16

do and then we will find the best one.

2:15:18

So best one we are getting with NSTMAT as 200 and

2:15:23

we'll make them final model to make it.

2:15:26

So best here we can find a final model

2:15:27

that's the way how it basically works out.

2:15:30

Okay.

2:15:31

So best, so best joe is best,

2:15:34

this is, here like we'll make final model

2:15:35

that's the, that's the basic concept of this entire film.

2:15:42

So best pipeline is, I think we already talked about it.

2:15:45

The best pipeline is.

2:15:46

effectively the one that I'm building.

2:15:48

So as we've got,

2:15:50

that NST matters 200 is the best model,

2:15:52

what I will do?

2:15:53

This is what I'm able to do, right?

2:15:54

NST matters, one, two, see,

2:15:56

like how I was doing.

2:15:57

And now you figure out that,

2:15:58

chlo, NST matters 200 is the best one.

2:16:01

Okay, NST matters 200 is the best one.

2:16:03

So you'll, you know, you will go and build the,

2:16:07

you will go and build the best model.

2:16:11

That's what you will do, okay?

2:16:12

So now, let me go ahead.

2:16:16

Just a second, guys, Joblib housing model.

2:16:18

You have two files out of, okay?

2:16:21

Logistic was very large.

2:16:23

Okay, this is hospital, it or housing,

2:16:24

shall, okay.

2:16:25

So, so.

2:16:28

So, let's go ahead.

2:16:29

Hospital took, took, and what I will do now?

2:16:33

Just go look quickly to this one.

2:16:35

So, now, so best is 200, right?

2:16:37

So best is 200.

2:16:37

Now, what I will do?

2:16:39

I will construct the best random forest pipeline.

2:16:42

This we'll dump.

2:16:43

Okay, so the best random forest model model

2:16:44

what will be?

2:16:46

What is the best random chorus model going to be?

2:16:51

That is what I will basically train right now.

2:16:55

So let us see that.

2:17:10

So let us see that. Yeah. So I will take, I will write it from scratch.

2:17:14

So we're here here we'll say, best underscore RF underscore pipeline.

2:17:19

So I'll keep it simple.

2:17:20

So this is what I will do now.

2:17:22

Best underscore RF underscore pipeline.

2:17:24

All if you can see this one.

2:17:25

And I will say equal to, equal to random forest.

2:17:30

Random forest regressor.

2:17:32

And I will simply say in estimators.

2:17:33

Now, look, everybody has come here.

2:17:36

Something to do it.

2:17:36

I was actually about to type it.

2:17:39

So I'm trying to construct the best.

2:17:40

Now we have got that, that 200 is the best.

2:17:44

I will try different, different values.

2:17:45

We'll find that best care.

2:17:47

What best came, we'll make, we'll make final model.

2:17:50

That he came.

2:17:50

That's made already.

2:17:52

N-stimates do so low.

2:17:53

Random set 42-0.

2:17:55

A end-jobs equal to minus 1 is,

2:17:57

that we ignore can.

2:17:58

But that means that I will,

2:17:59

because random forest training takes a lot of time.

2:18:02

We've seen how much time.

2:18:03

So N-job is equal to minus-1.

2:18:05

The mean, you are using all the CPU course for training.

2:18:09

You're all the CPU course

2:18:10

and you're training.

2:18:11

That is what it basically means.

2:18:13

And then,

2:18:13

but you are trying to you're trying to train the final model.

2:18:17

That's the way how it's working out.

2:18:21

It's going to take a while.

2:18:22

You can see, again, some time will.

2:18:24

This is the thing I was talking about.

2:18:26

You can see.

2:18:28

Now, the important thing is, while it completes,

2:18:31

this thing is in my Python memory.

2:18:34

Now, this Google Cloud is, what is?

2:18:37

This is your virtual machine, which is something that is operating on the

2:18:43

So, this is Google machine, it we can't, but whatever it is, this thing that you are,

2:18:54

all these variables that you're creating in Python.

2:18:57

You're, all the variables are you're taking in Python.

2:18:57

Now, Python in the data, it's how are stored here?

2:19:02

This is all the thing is system's RAM may store up here.

2:19:05

Now, look, the system's RAM already 2.5 utilized over.

2:19:08

I mean, this all variables are living in my RAM.

2:19:11

The more objects you create, I mean, and the more objects you create, I mean,

2:19:13

And the more technical term I want to use in Python is object.

2:19:18

Whatever you have learned in Python, all objects are.

2:19:21

You have started Python's first class, integer, float, string, bowl,

2:19:25

four main data types, list, they, double, and dictionary, and, and what are?

2:19:30

List, double, dictionary, set, set, say.

2:19:33

These four other types are.

2:19:35

Okay, and, what?

2:19:36

I mean, these are main data structures, right?

2:19:39

And, again, we go, and we're going to,

2:19:40

model building, see, SK-Learned models,

2:19:42

got, the models you're making, this is actually a model.

2:19:47

This is a model, this is a model, this is a model, this is a object.

2:19:50

This are all objects.

2:19:52

Here, even when you go and do A equal to three,

2:19:56

when you say this, what you're storing three in a variable?

2:20:00

That is a, what a variable? A, it requires memory.

2:20:03

But that is actually stored in system's RAM.

2:20:06

So I can, you know, I can simulate a very nice demo for you.

2:20:12

you can say, you can save a, I take a time, so save a massive,

2:20:20

you know, you're, you're just, we're in Germany, okay,

2:20:23

if you're, okay, you're, okay,

2:20:25

a, save a list of,

2:20:28

you take around,

2:20:33

uh, or then you, then you'll, then you're

2:20:37

a number in array, save them, okay,

2:20:39

okay, mp.

2:20:39

Mp.P.A arrange, it's a Germany, it's a Germany, it's a,

2:20:41

exactly.

2:20:42

NP.A range, you can do it.

2:20:44

You can take NP.A range from one, two.

2:20:46

Now, type, just.

2:20:48

That's it.

2:20:49

You know?

2:20:50

Seriously.

2:20:51

Yeah, exactly.

2:20:52

That's what it is, right?

2:20:53

Now, what I'm trying to demonstrate is,

2:20:54

when you're this, what do you think it is using?

2:20:57

It is using your RAM?

2:20:58

Now, look at this number.

2:20:59

What is?

2:21:00

I've also lost track of it.

2:21:01

This 100,000, 1 million, 10 million.

2:21:03

You're 10 million numbers stored here.

2:21:05

Can you believe it?

2:21:06

Can you see how much of time,

2:21:07

memory it will take?

2:21:08

I'll reduce it a bit.

2:21:09

Okay, but number.

2:21:10

company, then still specialized,

2:21:12

it's a little space.

2:21:13

But it's still a space.

2:21:15

You see, this 2.6 gb ram is right now.

2:21:17

But if you try to store all these numbers,

2:21:20

that's where it's stored,

2:21:22

that's in the main memory,

2:21:24

store it.

2:21:25

Disc is not, hard disk.

2:21:26

Hard disk is different.

2:21:28

Hard disk is called the permanent storage.

2:21:30

Back to computer basics.

2:21:31

This is school level computer basics.

2:21:33

Hard disk,

2:21:34

you can store here.

2:21:35

You can store.

2:21:36

Now, you off, on,

2:21:37

and on it.

2:21:38

Movie, then there in hard disk.

2:21:39

movie you download

2:21:41

you, whatever you download

2:21:42

that's all your hard disk.

2:21:43

You have.

2:21:44

You're off and on it,

2:21:45

it is.

2:21:46

But this A variable is,

2:21:48

this A variable not

2:21:49

this is only the system

2:21:51

runtime of time.

2:21:53

So these are all stored in RAM.

2:21:55

That is the reason why

2:21:56

it's very expensive.

2:21:57

If you're a computer

2:21:58

going to go

2:21:59

that RAM,

2:22:00

so how price is how price

2:22:01

now?

2:22:02

Now, what?

2:22:03

How do you?

2:22:04

You have one TB's hard disk

2:22:05

hard disk?

2:22:06

You get $3,000?

2:22:07

You know,

2:22:08

where the 1 dB RAM?

2:22:09

1 TV RAM?

2:22:10

Does it?

2:22:11

No, it's not.

2:22:12

It's not.

2:22:13

It's cost to be lax.

2:22:14

Lacks.

2:22:15

Lacks.

2:22:16

So RAM is very costly because it is reason.

2:22:18

So disk is different.

2:22:21

Disc is permanent storage.

2:22:22

RAM is current, temporary storage.

2:22:25

We're in Python in

2:22:26

whatever you do

2:22:27

anything

2:22:29

everything.

2:22:30

Integer, float, string,

2:22:34

Boolean variable declared

2:22:36

list declared,

2:22:37

tuffel,

2:22:38

declare,

2:22:39

you know, dictionary, sets,

2:22:41

you,

2:22:42

you've made,

2:22:43

a plot clip,

2:22:44

or peltt, dot,

2:22:45

or so,

2:22:46

so,

2:22:47

you know,

2:22:48

that's what you are,

2:22:49

that you're,

2:22:50

it's all getting saved in the runtime.

2:22:53

Then we go and

2:22:55

we've,

2:22:56

last one month's machine running

2:22:57

you,

2:22:58

you're doing,

2:22:59

you're doing,

2:23:00

so model dot fit

2:23:01

we're,

2:23:02

we're what we're doing

2:23:03

we're making, it's an object,

2:23:04

it's an object,

2:23:05

it's a Python object,

2:23:06

so that is also getting stored in the RAM.

2:23:08

So when you're running

2:23:09

run this piece of code.

2:23:10

It will take a while,

2:23:11

but it is going to all get saved in the system RAM.

2:23:15

This system RAM may save

2:23:16

it.

2:23:17

Now this will take a lot of time.

2:23:18

Now,

2:23:19

look,

2:23:20

sorry, I will not do this.

2:23:21

Now,

2:23:22

you have 5.6

2:23:23

but I have a hunch

2:23:24

that will

2:23:25

crash.

2:23:26

I have a hunch that will be crash

2:23:27

because we

2:23:28

have 100 times

2:23:29

you're saying.

2:23:30

Can you see?

2:23:31

Look at this.

2:23:32

11.8,

2:23:33

now a collapse

2:23:34

that's actually,

2:23:35

yeah,

2:23:36

we need to do not,

2:23:37

but did you get the idea?

2:23:38

I want to just demonstrate this to me.

2:23:39

The code is simple.

2:23:41

3-0 added you.

2:23:42

You know,

2:23:43

what are we doing?

2:23:44

We are tremendously

2:23:47

increased the memory.

2:23:48

Can you see?

2:23:49

Got a flavor of it?

2:23:50

These are all variables

2:23:51

that are occupying the RAM.

2:23:53

Okay?

2:23:54

Now, why am I talking about this today?

2:23:55

Let me now come to the next part.

2:23:56

Why am we discussing all this?

2:23:58

Okay?

2:23:59

Now, we're going to run

2:24:01

here.

2:24:02

It's just like how a program works,

2:24:05

correct?

2:24:06

So everything is in the

2:24:07

exactly.

2:24:08

We'll be correct.

2:24:09

So RAM is a complete memory space for your application.

2:24:13

Your application is like the memory space.

2:24:15

That's the intuition.

2:24:16

Now, all you want to do is,

2:24:19

you want to just go back and make sure that you are saving this in the disk.

2:24:24

Because if you're in RAM in

2:24:26

if you're, like, if you're,

2:24:28

like a restarted,

2:24:29

this is like a restart,

2:24:31

all right,

2:24:33

back from from from from

2:24:35

from,

2:24:36

remember guys, I'm running every

2:24:38

I'm running everything from the beginning now.

2:24:40

This time will take three minutes.

2:24:43

Everything I'm running from the beginning.

2:24:45

All the variables are gone.

2:24:47

Now, how do I ensure I'm persisting this to the disk?

2:24:51

There are two very interesting things,

2:24:53

JobLib and Pickle.

2:24:55

Pickle is a way.

2:24:57

So there is something called JobLid, there is something called Pickle.

2:25:00

So what is the difference?

2:25:02

So JobLib is the native SK-Learned format.

2:25:05

JobLib is the native SK-Learned format.

2:25:07

learn format, whereas Pickle is the native Python format.

2:25:10

Both they work in the same way.

2:25:12

Similar way.

2:25:13

JobLib is generally a little faster.

2:25:16

If you want me to just share a small snippet

2:25:19

that you can share you.

2:25:21

I don't want you to memorize these things,

2:25:23

but if you're practical applications

2:25:25

to ask you,

2:25:26

so JobLip is actually generally something that is made for.

2:25:29

Let me just think that to all of you.

2:25:30

Here you have just a small image is.

2:25:33

There's an image copy not.

2:25:36

So.

2:25:38

Just a second.

2:26:06

Ah, you can take this one now.

2:26:11

Okay?

2:26:12

I'm not, of course, screenshot a message here.

2:26:14

So you can just use that to kind of visualize which one is better, but they all operate the same way.

2:26:20

Both of them operate the same way.

2:26:21

Just for the session perspective, what I'm doing right now, just for the, just for the session perspective, what we are trying to do is we are trying to use the job lib, you know, same facts, okay?

2:26:34

So Pickle also works the same way.

2:26:35

works the same way.

2:26:36

So job is faster.

2:26:37

So practically we'll prefer using job level.

2:26:40

So we have comparative notes you have shared here.

2:26:43

You can see.

2:26:44

So we are persisting disk.

2:26:46

Like you file save you,

2:26:47

okay,

2:26:48

as we've talked about,

2:26:49

you have a pipeline to make,

2:26:50

all right,

2:26:51

cut cut up,

2:26:52

it's been,

2:26:53

but the model is,

2:26:54

what model is,

2:26:55

that model is in your RAM.

2:26:57

If you're,

2:26:58

if you're restarted,

2:26:59

the model go,

2:27:00

so you want to save that with a disk.

2:27:02

That's the intuition.

2:27:03

You want to save that to the risk.

2:27:04

You want to save that to the risk.

2:27:05

So by, but right now, they only exist in the Jupyter notebook memory, that is RAM.

2:27:10

So to send them to our software engineers, to put into a real application, that's what we are trying to do.

2:27:15

When we're, when we're making

2:27:16

we,

2:27:17

this thing,

2:27:18

we need to our front-end development team to do that's a different team.

2:27:21

So we must save them to our hard disk as a file like using job.

2:27:25

Like we document, dot x, docels say,

2:27:27

Excel files, share, save for the notepad save,

2:27:30

we save some file, we save some file.

2:27:32

We save some file, we'll save it,

2:27:33

same thing.

2:27:34

Same thing.

2:27:35

So, we'll show you how to save it.

2:27:38

Okay, you can see you.

2:27:39

We'll delete it, so you'll better

2:27:42

understand this.

2:27:43

We've already been already made it.

2:27:45

So, once I do this, once I run this particular piece of code,

2:27:49

you'll see, this dot job live file will be created here.

2:27:53

So once I run this will take a while to run,

2:27:55

because first this will complete for it.

2:27:57

Okay, this is a very time will be.

2:27:59

Once this complete, once this code is successful,

2:28:01

whatever model I'm training, whatever dot fit I'm doing,

2:28:04

doing this dot fit's the model is.

2:28:06

Now, it's in RAM, it's from,

2:28:08

I'm doing joblib. dump,

2:28:10

and I'm writing it to this particular job-lib file.

2:28:13

Okay?

2:28:14

So this is your model.

2:28:16

This Python's model object.

2:28:18

That's it.

2:28:20

Now, look, here here,

2:28:21

file will be.

2:28:22

That's it.

2:28:23

And that's it.

2:28:24

There's nothing.

2:28:25

There is.

2:28:26

This is your job-lick file.

2:28:27

Okay,

2:28:28

now we can do.

2:28:29

We can we can,

2:28:30

we can take this prediction.

2:28:31

That's it.

2:28:32

That's it.

2:28:33

This is your job-liq file is.

2:28:34

completely a different machine in.

2:28:35

This dot job-lib file is.

2:28:37

So you can you can do a totally

2:28:38

a different machine in.

2:28:39

Here we're similate it.

2:28:40

So,

2:28:41

the first step, you are dot dump

2:28:43

this is something that you will do

2:28:45

on a development machine.

2:28:46

You take your data, train test

2:28:49

and you make model

2:28:50

and you are saving that in a dot job-lip file.

2:28:53

That's the first part that you do.

2:28:55

You are saving all that in a dot job-lip file.

2:28:57

Now once you have saved that, what you will do

2:28:59

is you can now go to a completely different server.

2:29:02

Okay, imagine this cell is

2:29:03

Imagine this cell is completely separate Python script

2:29:06

turning on a different server, in a different country,

2:29:08

where it's another in the country.

2:29:10

It doesn't need the training data anymore because

2:29:14

training to have got,

2:29:15

the model training we've done,

2:29:17

that whole logic here here

2:29:19

we've already,

2:29:21

that trained model has,

2:29:24

the dot fit and the final result

2:29:25

we already in this file in the file

2:29:27

all the metadata data is already stored here.

2:29:30

Now we have training data

2:29:32

not only what we will just

2:29:34

we will just load the dot job lip file

2:29:37

and start the prediction

2:29:38

so two steps are now

2:29:40

so this is the real world way how we do it

2:29:42

we do it

2:29:43

we all the entire thing in the file

2:29:44

we can simulate

2:29:46

so we'll model

2:29:48

make model,

2:29:49

we'll save and set

2:29:50

this our document

2:29:53

you know

2:29:54

now we're what we're

2:29:55

we're very interesting

2:29:56

we can you can

2:29:57

this is the interesting part

2:30:00

I am downloading this is

2:30:01

I'm downloading this is

2:30:02

this, now we're in this chat

2:30:03

to share this.

2:30:04

You guys can just run this script.

2:30:06

This is right.

2:30:07

You can't

2:30:08

take any data,

2:30:09

if I share this with,

2:30:11

let's say you guys are all

2:30:12

dispersed all across India,

2:30:13

there's,

2:30:14

so you're not going to

2:30:16

do you.

2:30:17

You've seen how much time

2:30:19

training in training in.

2:30:20

Model training can take a lot, I can take hours also.

2:30:22

So I have invested all the time.

2:30:24

We have trained

2:30:25

hours I have spent.

2:30:26

I have built the final model,

2:30:28

we have saved it,

2:30:29

and I'm simply going to share that with me.

2:30:31

I will simply

2:30:32

go and share that file with you.

2:30:34

Here we go.

2:30:34

Let's say you are part of my application team.

2:30:37

Ah, this is a very big file.

2:30:39

Sorry, so, so, so those are 70 MBA.

2:30:41

He may not go.

2:30:42

But anyways, see,

2:30:43

yeah,

2:30:43

yeah, you,

2:30:44

this is a big,

2:30:45

big,

2:30:46

okay.

2:30:47

Whatever.

2:30:51

Anyway,

2:30:52

so, I mean, it's a, it's a bit of a big file right now that you've got.

2:30:55

So, whatever.

2:30:57

So, whatever.

2:30:58

So, this is your, this is the complete package

2:31:01

that we have got right now.

2:31:02

And now,

2:31:02

what you can go back and do is you can take this,

2:31:04

you can go and take this, you can download this,

2:31:06

and you can simply use it for doing prediction.

2:31:08

So you're in your system in what

2:31:10

can do.

2:31:11

Imagine you're part of my application team,

2:31:13

you are our application team.

2:31:15

You have no.

2:31:16

You know,

2:31:17

you know,

2:31:18

that you know,

2:31:19

what reads, CSV,

2:31:20

we have anything.

2:31:21

You have just job leave

2:31:22

we're developer,

2:31:23

we have made

2:31:24

things,

2:31:25

and we've shared you,

2:31:26

the job with file,

2:31:27

there is model

2:31:28

model,

2:31:29

you are an application developer,

2:31:30

development person,

2:31:31

you are an application developer,

2:31:32

you know, you'll just

2:31:34

you just mean that you'll just

2:31:35

mean,

2:31:36

that's it,

2:31:37

that's it,

2:31:38

that's it,

2:31:39

that's it,

2:31:40

that's it,

2:31:41

so this is going to run

2:31:43

on a completely difference

2:31:44

under.

2:31:45

So here we'll simulate

2:31:46

joblift.

2:31:47

load,

2:31:48

new, new,

2:31:49

value, and modern dot predict,

2:31:50

just, it's just

2:31:51

in server.

2:31:52

No,

2:31:54

Docker is a different thing,

2:31:56

so that's a different thing,

2:31:57

so that's a different thing,

2:31:58

okay?

2:31:59

I, I, I promise to do,

2:32:00

I promise to docker, we'll cover

2:32:01

we'll,

2:32:02

okay?

2:32:03

So do Docker in today,

2:32:04

let's not go to Docker today,

2:32:05

but I will cover it later,

2:32:06

okay?

2:32:07

But yeah, application team must have

2:32:08

the required income, correct,

2:32:09

absolutely, you're right.

2:32:11

So if I'm, if I talk about it

2:32:16

from a slightly conceptual standpoint,

2:32:18

what we are,

2:32:20

what we are talking about here,

2:32:22

we can say that

2:32:24

the Python packages,

2:32:26

the package's version,

2:32:27

that will be very similar.

2:32:29

The packages, the packages, the versions are, that will be very similar.

2:32:32

So, if we have

2:32:33

SK Learned's particular version used,

2:32:35

that application also has to use the same Python version,

2:32:37

the same library, the same set-up,

2:32:39

that's your absolutely right.

2:32:41

So it's the better way that we can docker

2:32:43

exactly how it's a different conversation.

2:32:45

That's a different conversation.

2:32:47

When we're,

2:32:48

when we're agentic

2:32:49

then we'll, then we'll

2:32:51

that we'll get.

2:32:52

That's the big.

2:32:54

But this is the big picture idea how the deployment

2:32:56

actually happens.

2:32:57

When we talk about deployment, we use all

2:32:59

these fancy terms, C, I, C, C, C, D, D,F,

2:33:01

these are some fancy terms.

2:33:03

It's all fancy terms, okay.

2:33:04

But the big picture idea is.

2:33:05

What are, what is?

2:33:07

There are hundreds of jargons we'll find.

2:33:10

But, yeah, Docker and all are different tools that we have.

2:33:13

But this is the big picture idea.

2:33:15

You take a data set, you build a model,

2:33:17

you persist, you save,

2:33:19

download, download,

2:33:21

development, the application team

2:33:23

of it, share, and that team

2:33:24

that will make that, basically.

2:33:26

And now, finally,

2:33:28

and now finally,

2:33:29

So we have prediction Python strips here.

2:33:34

Now the thing is, can we go back and can we do the same thing?

2:33:40

Can we go back and can we do the same thing using an application?

2:33:44

And this is exactly where we are using something like a gradio.

2:33:47

So this is the part of the code that I want you not to worry about.

2:33:51

Please don't worry about the radio part because radio is a great of application development framework.

2:33:56

It is completely unrelated to our data.

2:33:58

unrelated to our topic. But I just wanted to give you a simulation. Again,

2:34:04

the first step is,

2:34:06

model made. Best model, I save the best model. I save the best model. And now I want to use that model for making prediction.

2:34:15

This is a scripted way I was doing the whole thing. Now I want to do the same thing using a radio application.

2:34:22

We're front-end, okay? Interactive UI is a very simple way to do it. And

2:34:27

And again, what I'm doing at the front end, I am loading the this thing.

2:34:34

So this is what my application team will do.

2:34:36

This is again not my work.

2:34:38

This is not the work of data scientists and ML people.

2:34:40

My work end it here.

2:34:42

My time here.

2:34:44

Take the data, try different models, build the best model.

2:34:48

As you've got a best model, you have it dumped.

2:34:51

You have it dumped. You have it dumped.

2:34:53

Job lib by save it.

2:34:55

And job lib we have shared with you.

2:34:56

So everyone in the class.

2:34:57

right now. You are, you, you guys are part of my front end application team.

2:35:03

Abbe from our come, my work is over. And now what you have to do? You are part of my application

2:35:11

team. So now you will have to go back and you will have to, you will have to use a front end.

2:35:19

You can use a front end application. You can build a front end. Better but streamlet we use

2:35:23

can. Which is. Stringlet is also, stream is actually better. But Gradyo, we prefer.

2:35:27

I think GradyO is simpler. Gradyo is a very popular standard for building web apps in machine

2:35:33

learning and JNI in particular. So, Gratio is actually a very easy framework. That of course,

2:35:38

streamlete, but Gradyo is actually a better framework. It's an easier framework to kind of work with.

2:35:45

They are both web application frameworks. But again, remember, I want to clarify, please remember,

2:35:53

this work will be done by the application development team.

2:35:55

job lip file we've sent you. Imagine you are part of my application development team.

2:36:02

You will take that file. And you go and you go and you go to this is a small simulation. I'm trying to

2:36:08

show you. You are this code to look up. And this code in at a high level, what are you doing? You were

2:36:13

accepting all these features. And based on that, you are doing modern.com. And now thanks return

2:36:17

and here here all web user interface interface, the sliders say, what value can turn can you?

2:36:23

What interface is. Please ignore this part.

2:36:25

want you to get into this right now. But the important thing is the application, which I want to share

2:36:30

with you. Application case how will. Let me show you. This is the public URL application. This is the

2:36:36

big picture overview that the team will build for me. This is how it all boils down to. Whatever

2:36:41

we have been discussing all this file, this is where it all boils down to. So we were doing all this

2:36:47

in a local Jupiter notebook. So we have a notebook. So we have a model made. But that model is what model

2:36:51

here. Yeah, what model?

2:36:53

Today we discussed here, you can actually go and save that model.

2:36:56

You have the module to dump here in a job lip file.

2:36:59

Joblib is faster.

2:37:01

There is another option called pickle.

2:37:02

Pickle is a little slower, but, you know, so that's, that's one way to look at it.

2:37:08

So you're able to store in a job lip file.

2:37:12

And now, using that job lift file, we are simply loading it and we are doing prediction.

2:37:20

This is the front end user interface.

2:37:21

are able to see. So this is exactly what your end users will do. When my end users are

2:37:26

using the application, this is what my end users will see. So imagine I'm building a website

2:37:31

or the website may, you've seen these of magic breaks 99 acres. Imagine you are trying

2:37:36

to sell a property. So I'm just giving an example. So you're trying to sell a house and

2:37:42

you're up, you choose that you have your income what is. Area of income what is. Housing age

2:37:47

is not the exact same use case, but I'm trying to give it a high level idea. If you want to sell

2:37:50

your house or sell your car. So this is how we can enter the details.

2:37:53

Website in. You can do it. Here, age, it's it. This is it. This is. Okay, so

2:37:59

this is numeric. So, all, we're all right? Average number of rooms are seven.

2:38:04

Let's go. Rooms are. Okay. Population, it's enough. Occupancy. Latitude, it's

2:38:09

longitude, it's. Here here, you have a map selection. Now, who, who's

2:38:13

latitude, longitude? If you ask me, my latitude, we don't know. We don't know. But you. But you,

2:38:17

you can make a map selection there. You can make the UI better.

2:38:20

interface, you can better. You, you can a map.

2:38:23

So, map, in the map, people select

2:38:24

could. That based, from, latitude, long,

2:38:26

automatically fill up. But that is not our work.

2:38:29

This is our work. This is our work. This is front-end development.

2:38:32

But what I wanted you to see is the big picture idea.

2:38:35

This is what is. You know,

2:38:38

you here values enter. Okay.

2:38:39

Values down, end-user values down.

2:38:42

Okay.

2:38:43

Submit down.

2:38:45

As he submitted is, what is?

2:38:47

This is your input X.

2:38:48

This is your input X. This is your input X.

2:38:50

Based on that entire input X, based on that,

2:38:53

based on that entire input X,

2:38:57

this is getting passed back to the,

2:38:59

this is, so whatever, whatever values you're entering,

2:39:02

just same way as in streambook,

2:39:04

whatever values you're entering,

2:39:05

a Python function column, these are all the input excess.

2:39:08

Model dot predict will happen.

2:39:10

The price will get calculated and the output will be returned back.

2:39:14

Or to return hold, who of the output,

2:39:16

the output radio text box may have.

2:39:18

So this is what is going on behind the scenes.

2:39:20

This is the magic that is happening now.

2:39:22

So when I hit submit,

2:39:23

observe this one, when I hit submit, what is happening?

2:39:27

Calculation will.

2:39:28

Then, then last, your output is it is.

2:39:29

There it is.

2:39:30

Here we'll get a little come,

2:39:33

we'll, we'll, we'll, it's a little bit better,

2:39:34

okay?

2:39:34

You can see, you can try to.

2:39:36

And obviously, if the locality

2:39:38

income is a lot, then housing price is

2:39:40

more, it's obvious.

2:39:41

I'm expecting my housing price to be higher now.

2:39:43

Now, if any estimate

2:39:44

if our housing price,

2:39:46

if we're, if we're,

2:39:46

if we're in this area to buy

2:39:48

if we're going to buy

2:39:48

this area to buy this price

2:39:49

will imagine you're building an application.

2:39:52

This is our application team

2:39:53

will be. So customer

2:39:55

will enter, he will submit

2:39:57

be, just as they submit mark it.

2:39:59

What happens? This is going to my model.

2:40:04

That model is

2:40:04

that model, which we've

2:40:06

made in job leave and save it,

2:40:07

there's going, there's a dot predict

2:40:09

will, why return it, and

2:40:11

why it will you display will.

2:40:12

You look, it going to go me, here he will display

2:40:15

here, you're going to. This is the big picture.

2:40:18

This is how it all stacks up.

2:40:19

you can. You can't. But again, I'm repeating this for

2:40:23

the next time. This is not our work. This is not a

2:40:25

machine learning or an agentic AI rule. You say

2:40:28

there's no relation to this is the front-end development rule. But

2:40:30

you have a big picture idea

2:40:32

even if you're talking to an application development person,

2:40:35

you have that you know what is my model? Where is my

2:40:38

model? You know, we were all this while, you know, we were all like

2:40:42

in a Jupiter. Now, sir, you know, we're

2:40:45

on Facebook. We're looking at some website in go. And I know. If you remember

2:40:48

in the very first session, I was talking about spini.com.

2:40:52

We have you a beautiful use case, the

2:40:53

spini.com, okay? So, at that time we

2:40:55

I had you explained to these things. So Spinney

2:40:57

there's an option where you can go and enter your car price.

2:41:01

The car number entered here.

2:41:04

You have a car number entered. Then you

2:41:06

click car price gate. So when you click

2:41:08

the car price, so when you click it, what is it?

2:41:10

What's how we've discussed

2:41:12

that, get your, I mean,

2:41:14

let's, you mean, uh,

2:41:15

California real estate price.

2:41:18

Same way you get.

2:41:18

at your car price.

2:41:19

Is there the same thing.

2:41:20

Now gari-ca details enter.

2:41:22

How many kilometers run,

2:41:23

how this,

2:41:23

how this,

2:41:23

this, you.

2:41:24

You enter and

2:41:26

model that predict is

2:41:27

happening and it is

2:41:28

estimated, it is

2:41:28

estimated, it is

2:41:28

estimate the car price for you.

2:41:30

That's a guarantee

2:41:30

so he's,

2:41:31

that you're saying, if you

2:41:33

want to buy you,

2:41:34

we'll buy this

2:41:35

price based on their

2:41:36

regression model,

2:41:37

that they have already

2:41:37

trained and deployed.

2:41:38

In some similar job

2:41:39

job leave, fine.

2:41:40

Job leave,

2:41:41

more we can find,

2:41:41

something like that,

2:41:42

okay?

2:41:43

So the only

2:41:44

difference is

2:41:44

real world in

2:41:45

we don't use

2:41:46

so Gradio is

2:41:47

very, very popular.

2:41:48

Very,

2:41:48

then I wanted to talk

2:41:49

about gradio is because

2:41:50

you can't

2:41:50

encounter

2:41:51

come up.

2:41:52

A good

2:41:52

we're going to

2:41:53

go

2:41:53

going to

2:41:53

see a lot of

2:41:53

,

2:41:53

we'll see

2:41:55

you will see

2:41:56

a lot of

2:41:56

of gradio

2:41:57

getting used

2:41:57

there

2:41:57

also in

2:41:58

practice.

2:41:59

Okay,

2:41:59

so that's the

2:42:00

that's the,

2:42:00

that's the,

2:42:02

that's the,

2:42:03

that's the,

2:42:04

intuition.

2:42:06

Okay?

2:42:06

Okay.

2:42:07

Ah,

2:42:09

yeah.

2:42:18

I hope everybody's, everybody's got a sense of this, all if you're absolutely clear.

2:42:40

Now, you're absolutely clear.

2:42:41

That could be a challenge for you.

2:42:43

You can see,

2:42:43

that's the big feature idea.

2:42:45

But the big picture idea is, is, is, is,

2:42:47

is if you can be a good application,

2:42:48

when you go and look at, let's say, Facebook, Facebook have

2:42:51

there are so many features that you have there.

2:42:54

Same idea, same way how it happens there also.

2:42:57

Facebook will be a sort of module where, you know, all, there are many, many predictions

2:43:03

happening in the real world.

2:43:04

When you look at a real application, there are thousands of these models that are built.

2:43:09

We're real world in the real world, one, that

2:43:12

can't, but multiple that can't.

2:43:14

You can't.

2:43:15

You know, jemina use for.

2:43:16

Here we have a radio,

2:43:17

you have made a radio.

2:43:18

Simple, straightforward.

2:43:19

You have here a cell select.

2:43:20

We have already ready to you share in our notebook.

2:43:24

Very simple.

2:43:25

Yeah, absolutely.

2:43:26

Create a code cell.

2:43:27

Generative day, do.

2:43:29

Stream rate the same thing using stream rate.

2:43:32

Build the same front-end interface

2:43:37

using stream-lid.

2:43:39

Using stream-lids.

2:43:42

Cheney.

2:43:43

Make it.

2:43:44

You can try.

2:43:45

This you already know.

2:43:47

That's why I'm not trying to.

2:43:48

get into it too much.

2:43:49

But, yeah, so stream rate pretty similar way.

2:43:51

Okay, overall.

2:43:52

Okay.

2:43:53

Okay.

2:43:54

I want to talk about it.

2:43:55

Amlops, one kind of, one second.

2:43:58

You can see joblit dot load housing model.

2:44:06

This is the way how you will build the streamlet application.

2:44:09

Very similar.

2:44:11

So the concept is that you.

2:44:12

You have the model you're saving the model.

2:44:15

This is the way how it works out.

2:44:17

it works out.

2:44:18

You are now loading the job-lib model and using that you want to do the predictions.

2:44:22

Now you want to load the job-leg model and using the job-lid model you want to do the predictions.

2:44:28

That's the way how it has to work out.

2:44:31

Okay, so stream-lidtap you have to install it.

2:44:33

Now, because streamlet is not installed.

2:44:34

So what you have to do is you have to install stream-lit.

2:44:37

That is the only thing that you will have to do.

2:44:40

So pip install streamlet.

2:44:43

If you clip install streamlet, so,

2:44:45

actually, actually, it will do it do.

2:44:46

I don't have to do anything, okay?

2:44:48

It will do everything for me.

2:44:50

So it's, I can solve it and if you do this, it will work out.

2:45:16

Okay.

2:45:23

Yeah, I can't show.

2:45:29

At a high level, I can't show, yeah, see, MLOx is basically, at a high level, I can talk about it.

2:45:45

See, at a high level, I can talk about it definitely.

2:45:46

important component that you do there.

2:45:48

A, after only only new thing.

2:45:50

Basically, when we come to MLOps, this is also part of it.

2:45:53

This is also part of ML operations, what you're doing.

2:45:56

Only thing is, MLOx in a tool we use a completely different tool itself.

2:46:00

So both of that is a different thing on together.

2:46:02

We use something called ML flow there, actually.

2:46:05

So there how we use something called ML flow, machine learning flow we use.

2:46:09

And the only thing conceptually that is happening there.

2:46:12

So we have a demo so it's actually very easy.

2:46:15

Since you're requesting, I can briefly talk about it, definitely.

2:46:19

So it's very easy, actually. It's not difficult at all.

2:46:22

So if you ask me, this is the most popular, this is the most popular platform, the most popular

2:46:28

library that we use for mastering the ML lifecycle.

2:46:32

So this is a practical library which we use for doing experiment, tracking, model management,

2:46:40

model deployment and all that.

2:46:42

What we have seen definitely is at a high level,

2:46:44

we made, saved him, saved it, job by saved, and deployed with radio save.

2:46:50

But what is a more organized way of doing it?

2:46:53

You're what you're asking, CICD, which is a very good question.

2:46:57

This is actually the way to do it.

2:46:58

But ML4 is a very different piece.

2:47:00

But at least at least at a basic level, you'll see one two snippets if you're trying, so you

2:47:05

you'll get out of it.

2:47:06

Very simple, actually.

2:47:07

It's very simple, okay.

2:47:09

It's very simple.

2:47:10

You look, Akancho, what you can do?

2:47:14

This is the way.

2:47:14

how you can train a model, right?

2:47:16

Trains as usual.

2:47:17

But you're only enabling logging.

2:47:21

You're only logging.

2:47:22

You're logging it.

2:47:24

Because in machine learning, what are we doing?

2:47:27

We are trying out so many different, different models, so many different hyperparameter combinations, right?

2:47:33

And what we have talked about is like scratching the surface, that we only a crisis,

2:47:38

we only a logistic model try here.

2:47:41

We only a random forest classifier try here.

2:47:43

But within that.

2:47:44

model, there can be thousands of hyperparameters, tens of thousands of different hyperparameters

2:47:48

you can have, right?

2:47:50

I think about it that way in practice.

2:47:52

There can be so many different, different, hundreds of different different permutation combinations

2:47:57

who exist can't see.

2:47:58

Look at it from a practical perspective.

2:48:00

This can happen, right?

2:48:02

So that is where you need a proper platform to manage all that.

2:48:05

And that is exactly where ML flow comes in.

2:48:08

So, there's nothing is.

2:48:09

So, there basically, you can here on a example, you can see.

2:48:14

They've got a very good documentation.

2:48:17

And if you want me to specifically, specifically talk about which tool to use, you can learn a little bit of ML flow.

2:48:24

ML flow again is very different.

2:48:25

This is not part of your thing also.

2:48:27

But this is a simple code to get you started.

2:48:31

If you're you, sir, how are you?

2:48:33

Just it's just that.

2:48:33

Amlflow import, dot SKL and auto log.

2:48:37

So whatever models you're building random forest, it's, there's auto logging,

2:48:40

that means a beautiful dashboard where you'll see where you'll see,

2:48:43

that is how it will happen behind the scenes.

2:48:48

And that's the best part about MLP.

2:48:50

So all of these things will be logged automatically.

2:48:52

Whatever you're doing, all of these things will be logged automatically.

2:48:56

So that's the intuition behind what ML flow takes to the table.

2:49:02

So you can you can also go back and understand, you know, the models that you're building and you can understand the, you know, what are the models, what are the hyperparameters.

2:49:13

this is all of everything.

2:49:15

And I think a good way to see this is to again go back to the documents, the documentation,

2:49:25

and just to explore the select event.

2:49:27

You can see.

2:49:28

Psychic Learned's two, three examples.

2:49:30

Sara, they know, sample data set to do.

2:49:32

Nodwine, they've done.

2:49:34

Breast cancer, we discussed it today.

2:49:36

You can here.

2:49:36

You can see here.

2:49:37

M&O, they used to.

2:49:39

They've used a bit of ML flow here.

2:49:42

Okay.

2:49:42

So you can try it out.

2:49:43

try it on to it. It's just, just logging.

2:49:45

You're, whatever you're trying,

2:49:48

a gradient boosting try kyrgya, logistic try here,

2:49:51

10 other models try

2:49:53

all logged. And he's important.

2:49:56

It's very important.

2:49:57

You'll think, sir, logging's what you mean?

2:49:59

I'll tell me what to do.

2:50:00

Things can get very messy.

2:50:02

Now if you'll ask, if you're a Jupiter notebook in,

2:50:05

sir, you've made, sir, you've struggled to give the answer.

2:50:08

Because it is not organized.

2:50:10

Jupiter is very messy.

2:50:11

We have, I'm in a notebook in that I could have tried,

2:50:13

different things.

2:50:14

You want to log it.

2:50:15

You want to manage it properly.

2:50:17

So from a developer perspective, it is very important.

2:50:20

And the second thing is that from a model management standpoint, it's very important.

2:50:25

It is very important from a model management standpoint.

2:50:29

So see, we can exclusively do a class on ML flow.

2:50:33

I'm happy to do that.

2:50:34

So your evaluation general dee.

2:50:36

So what I've been doing is I'll request the team to exclusively maybe we can do a class on MLQ.

2:50:41

So I can, I can, I can, I can just that.

2:50:43

ML flow is actually very, very popular, very common.

2:50:46

I will do that.

2:50:46

So I don't want to like, just like, like, do two minute-minute discussion I don't want to do.

2:50:50

But ML flow is a completely different thing.

2:50:52

But definitely, ML flow, your, ML flow, your email flow, your agent's maybe I go.

2:50:58

This is the same library that is even used in agentic AI.

2:51:04

So the same concept that applies in machine learning, the same ideas gets applied in agentic

2:51:08

AI also.

2:51:09

That's the intuition.

2:51:10

So, so I will keep a.

2:51:13

comprehensive discussion for that.

2:51:14

Don't worry.

2:51:15

But I hope the high-level idea is here.

2:51:18

Models, experiments can you.

2:51:21

You can log-carsathe.

2:51:23

And you can also save the models.

2:51:25

Whatever models you are building, you can also go and save the models.

2:51:28

That's the way how the whole thing will basically work out.

2:51:43

Yeah, absolutely, absolutely.

2:51:56

Jenkins is absolutely usable.

2:51:58

Now, CI-CD is this is more like the deployment part.

2:52:02

But Jenkins, it's an industry standard for CICD.

2:52:06

But that's another tool altogether.

2:52:08

Jenkins is another thing altogether.

2:52:09

There are many things.

2:52:10

It's something very different altogether.

2:52:13

See, that's what I said, that these are things that will be very common.

2:52:16

If you'll look, this is not only specific to machine learning.

2:52:19

It's not that this is only for machine learning.

2:52:21

These discussions, Genkin, Docker, this, ML flow, these are very common things even

2:52:27

when we get into agency here.

2:52:29

But the way that will.

2:52:31

So any which ways, these are part of the thing when we will see the agent deployment.

2:52:36

Anyways, we will continue talking about these things, right?

2:52:38

That's what I'm trying to say.

2:52:39

So the Jenkins is not only for machine learning.

2:52:41

Jenkins are Bellelans or agents.

2:52:43

can't be correct.

2:52:44

Jenkins is a very popular CICD too as well, just to clarify.

2:52:47

But it's a different problem.

2:52:49

ML flow is more from experiment tracking and way.

2:52:51

Whereas Jenkins automates the build, test and deployment pipeline.

2:52:54

So if you're talking about CICD,

2:52:56

that's for Jenkins said.

2:52:58

If you're talking about MLOps, which Akanshu mentioned initially,

2:53:01

that's for ML flow.

2:53:03

Two other things are.

2:53:04

And both you're machine learning for day be can't.

2:53:06

LLMs or agents can't do.

2:53:08

I just wanted to clarify what is used for what.

2:53:12

But what is it exactly?

2:53:13

Exactly, that we will see later.

2:53:14

I'll anyways have a discussion for that when we come to agents and amendments, okay?

2:53:17

That's why I did not want to just show one small board and all that.

2:53:21

But at least the big picture idea should be clear.

2:53:23

I hope everybody's working.

2:53:26

Chalo, okay, guys.

2:53:27

I think we'll keep it at this.

2:53:29

Okay, so I've already shared the notebook with you.

2:53:32

I think you have been the evaluation this weekend.

2:53:34

So next course we are starting out.

2:53:38

It will be a new module that we are starting out with, obviously.

2:53:40

That will be the one that we are all.

2:53:43

you know, waiting to learn.

2:53:45

That will be agents.

2:53:46

That's what we'll be starting out with.

2:53:49

So any other questions?

2:53:51

All is clear.

2:53:56

I hope I've shared the demo.

2:54:01

demo with everybody.

2:54:08

Yeah, I've shared this with, okay.

2:54:20

Yeah. So, yeah. So, gradient boosting will be used. See, see. See, again. See, again, again, see, again. See, again, again, it has to be tried out. You know, there is. See, see, again. See, again, it

2:54:29

has to be tried out. There is no one way to, like, you have to try out. The same way

2:54:35

that we tried out logistic and different, different models that we tried out, same way you have to try

2:54:41

out gradient boosting. Same way you have to compare.

2:54:44

You'll table, comparison for whichever model is giving the higher test accuracy, you will be using

2:54:48

that. That's the process. There is no, there is no guidebook saying, he is data, he is data to use

2:54:55

there is no guidebook that tells you that.

2:54:59

Okay, that's the process.

2:54:59

way how we. Model monitoring, again, Akanshu, this is

2:55:03

completely unrelated to course for, but since you're asking, I can talk about it.

2:55:06

Model monitoring, again, is something that you'll be doing using a completely different

2:55:09

library, only because you're asking, it is not part of your, part of your curriculum and all that.

2:55:14

This is, so, you can, so, you can't use this. There's a very popular package for

2:55:19

evidently. Evidently, you have searched. This is a very popular evaluation platform.

2:55:25

You can talk, this is, this is actually a very good way to evaluate your

2:55:29

your machine learning models. Particularly monitoring. Whatever conversations we

2:55:35

were having today, drift how to measure, this is where you're evidently will be used. Now, again,

2:55:41

I'm telling you that this is also not only for machine learning. This is a bit of your LLM's related

2:55:47

when we come to that conversation, we will eventually talk about this also. How to monitor.

2:55:51

ML specific we will not see, but we will be seeing evidently AI getting used for LLM monitoring.

2:55:56

The ideas remain the same.

2:55:57

You know, how is that application predicting on some new data?

2:56:02

Model what predict are you? Actuals what are we estimate those predictions? What is the model predicting

2:56:08

and what are the actions? That's the piece that we're talking about. That's the intuition.

2:56:14

So this is what evidently is about. You can see some resources. There are some guides that are available.

2:56:19

Very simple, not difficult at all. You can see some tutorials. So for example, if you want to see

2:56:26

the basic model monitoring, how to do. You can see some documentation for that.

2:56:34

This is the kind of dashports you will get, evaluate your model. So classification models can

2:56:38

condition matrix, one or data, okay. So whatever discussions we have had before. So the only good thing

2:56:43

about evidently is that it will go and give you some sample, some sample images, some sample

2:56:49

dashports that will do the thing automatically for you. That's the intuition. I hope it's clear. I hope it's clear.

2:56:56

Yeah, again, there's a, this, it's an entire universe, okay? The discussion goes on and on.

2:57:00

As I told you, yeah, but some of these things are very much common to machine learning as well as your LLMs and agents one.

2:57:12

Yeah.

2:57:15

Yeah.

2:57:20

One thing, one thing I would definitely suggest you guys, uh, Akanshu, particularly for you, some of the other folks.

2:57:26

If you think that you want me to talk about some other things,

2:57:29

okay, the classes, we have only certain courses, certain modules are there.

2:57:35

And, you know, we are restricted a little to those modules, but, but definitely, you know, I'm open.

2:57:40

I'm absolutely open to talk about it.

2:57:42

But one of the things that we are also trying to achieve is that you're also trying to stick to the times of it.

2:57:48

So our classes are we, we're trying to strictly stick to 10.30, 1040 types.

2:57:53

So you can definitely ask when you do a.

2:57:56

connect with Priyanka, your program manager.

2:57:58

You request, please, to do a class on ML flow.

2:58:00

And I'm happy to do it for me.

2:58:02

I'm happy to do it.

2:58:03

But my idea is I don't want to just rush into it.

2:58:06

But you're just, as you're asking, sir,

2:58:08

an example, even I feel bad.

2:58:09

Yeah, I'm just taking, but this one small sample I'm not about, but, you know,

2:58:14

if you want a class, you formally request after you,

2:58:16

I can do that for you.

2:58:18

And we can do a complete ML flow session.

2:58:20

We can do a complete evidently session.

2:58:22

So this is based on your request.

2:58:24

If you think that, you know, you want some.

2:58:26

session, an extra class, I can do it for you. No problem. No problem. Okay. But only thing is

2:58:31

that this is not a core part of your curriculum. So now we are, we are trying to go a little beyond

2:58:36

the curriculum and we are trying to do a session. So I'm alaqsek. If it's a request from you,

2:58:40

we can do it for you. No problem. But this is again not a poor part of your agentic or JNI

2:58:46

curriculum. Okay? Yeah.

2:58:56

Okay, great. People stayed back. Thank you. Once again, again, I'm trying to, one of the things I'm trying to do is trying to stick to the timings a little because, you know, I want to make sure that we also adhere to the timings a little.

2:59:07

So I'll try to, as we go along, I'll try to close this classes by 1040 and really so that, you know, everyone's comfortably able to have dinner and all that.

2:59:16

So just to keep everybody's interest in mind. But definitely some of these, you know, general, you know, general questions or,

2:59:25

that sometimes, and even I like to entertain all questions, it's just my style of teaching.

2:59:30

It's not that's just content, curriculum, there, that's why I say, you know, like, you know, like,

2:59:34

up evidently to have, but I give it the reference to you. ML flow is there. I give the reference,

2:59:39

but this is the thing. If you ask me, this is actually a two-hour topic. Now, I would love to teach you this,

2:59:46

but it is actually not the general thing. So these are little, if you want some coverage on that,

2:59:52

you can definitely request us. You can definitely ask us,

2:59:54

that's like, sir, a class for things. So we can plan some one, one extra class.

2:59:59

Us there's what, what's problem is. But one thing is that, that, the, uh,

3:0:04

this we have to make an ala extra session, correct. We will have to do a extra class for

3:0:08

some of these additional things, monitoring. So anyways, some agents pay similar things. It's

3:0:13

not as if when we come to Gen A.I. We'll, we'll definitely, you know, we'll definitely, you know,

3:0:19

keep talking about ML. We'll keep referring back to ML. Ideas to remain the same, right?

3:0:24

concepts remain the same. Doesn't matter. Yeah, yeah, yeah, yeah. Gen.

3:0:29

I think next week onwards, yes, next week onwards, the plan is the same. So I'll be handling

3:0:35

the Gen. AI for you, definitely. Yeah, that's why I say, that's why I say. When we keep talking about

3:0:39

Gen. AI, you know, we'll connect back to these same things that you're asking, and we will connect

3:0:44

back. Yeah, so as of now, that's the plan. So I'll be handling your Gen.

3:0:49

Chalo, thank you so much. Thank you so much. I will just quickly launch the poll for today.

3:0:54

I think Arshita is not there. Let me just check. Yeah. So all of you take some time to fill up your phone, everybody. And all the best again for your exam. I'm very sure exams you will all do well. Don't worry. Learning is a journey. I think it's not just about the exams that we should worry about. It's a journey. And I think the what matters is the overall learning, the holistic learning that you're getting, the end to and learning that you're getting.

3:1:24

So that's where you should really evaluate yourself on those parameters.

3:1:32

No, syntax, you think. Syntax you, you know, syntax you have to one or two things mentally work out

3:1:37

and have. What are? What is? Inport statement, train test plate, dot fit, dot score, train accuracy, test accuracy,

3:1:47

confucian matrix, Y test, why predicted, it was. Classification report function

3:1:53

have been. Yeah, yeah. And what? And what is? If you go with whatever we have seen in

3:2:03

ML so far, what else do you have? I've missed. I did what? Dot fit, dot score, was.

3:2:10

Classic Confucian underscore matrix function. Now you'll say, sir, you don't know, sir, you don't know?

3:2:15

I'm, you know, I'm, I mean, but now, I'm, I mean, what, there are, four, five, so functions are? Am I right?

3:2:23

I'm just saying it's not hard. I'm trying to make you confident. It's not hard. It's only, it's on six, seven functions.

3:2:28

So, so why are you demotivated? Six, seven functions are there.

3:2:34

Now, see, one way of teaching you is I can tell you, that, guys, you don't have to memorize.

3:2:40

Now, someage low, things, some of what, to do. Another way I can tell you is,

3:2:44

if you, if you know, if you add to do, then, that's it, seven, eight things only have to remember.

3:2:50

You have to remember. You, a template banal. I always suggest in my classes,

3:2:53

template to go to a template.

3:2:55

Today, the class we've made, you know, you can't, it's a template as far as template as

3:2:59

treat, okay, data, data, dot fit, dot score,

3:3:02

now our all ML's codes there,

3:3:05

that's kind of template

3:3:06

that's it,

3:3:07

there's, there's, there's. That's it. That's it. That's the way.

3:3:12

Okay.

3:3:15

Okay. Okay.

3:3:17

Let's, thank you, guys.

3:3:19

Oh, yeah, definitely, definitely.

3:3:20

You know notes, but maybe, maybe do it a smarter way.

3:3:23

Adjee. Manually not do. Use AI tools. You, you're all

3:3:26

snippets to Gemini to do, that

3:3:28

that will be you're going to you know. I'm just suggesting. You use some

3:3:31

smart ways of making notes. Notes be AI

3:3:34

can't. You have to do anything. Take my Jupiter notebook, put it on

3:3:37

Gemini and say generate notes for me.

3:3:39

I've made it. Sart line. You've got it.

3:3:42

This notebook is,

3:3:43

7-8 notebooks, put it on Gemini and say,

3:3:46

okay, look at all the codes that sir has shared and based on that

3:3:49

please share with me, generate the syntax.

3:3:53

generate the syntax on the basis of that.

3:3:57

Generate the main code snippets on the basis.

3:3:59

You can, it can go through all my notebook files,

3:4:04

the main four, five templates which I've shared.

3:4:07

And it can give you those main aspects,

3:4:10

key dots, dots paid, dots code,

3:4:11

confusion matrix, classification report,

3:4:13

there on overpitting, hyperbarometer tuning,

3:4:16

plus seven, eight things are there,

3:4:18

more question of there.

3:4:20

The approach will be the same over on.

3:4:23

And or hey, um, visualization may you might, uh,

3:4:27

visualization, so that's already done.

3:4:29

That's the Python module.

3:4:31

Simple, not much, right?

3:4:36

Yeah.

3:4:36

Chalo, okay.

3:4:37

Thank you guys.

3:4:37

Thank you all of you.

3:4:38

Uh, take care.

3:4:39

Have a good, have a good, have a good time.

3:4:41

Yeah.

3:4:41

Thank you.

3:4:42

Everybody.

3:4:51

Good night.

3:4:53

Good night. Take care, guys. Take care of you.

3:5:23

Thank you.