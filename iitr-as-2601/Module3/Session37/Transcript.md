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

9:53

Thank you.

9:55

Thank you.

10:25

Thank you.

10:55

Thank you.

11:25

Thank you.

11:55

Thank you.

12:25

Thank you.

12:55

Thank you.

13:25

Thank you

13:55

Thank you

14:25

Thank you

14:27

Thank you

14:29

Thank you

14:31

Thank you

14:33

Thank you

14:35

Thank you

14:37

Thank you

14:39

Thank you

14:41

Thank you

14:43

Thank you

14:45

Thank you

14:52

Thank you.

14:54

Thank you.

15:24

Thank you.

15:54

Thank you.

16:24

Thank you.

16:54

Thank you.

17:24

Thank you.

17:54

Thank you.

18:24

Thank you

18:54

Thank you

19:24

Thank you

19:26

Thank you

19:28

Thank you

19:30

Thank you

19:32

Thank you

19:34

Thank you

19:36

Thank you

19:38

Thank you

19:40

Thank you

19:42

Thank you

19:44

Thank you

19:46

Thank you.

19:48

Thank you.

20:18

Thank you.

20:48

Thank you.

21:18

Thank you.

21:48

Thank you.

22:18

Thank you.

22:48

Hi, everybody.

22:52

Hi, everybody. Good evening. We'll start on.

23:18

Hi. Good evening, everybody.

23:48

So today we have a very interesting session and it is kind of a kind of a follow on from what we discussed in the last session.

24:01

Last session we took some time to talk about the fundamentals of prompting how to write a zero short prompt, how to write a few short prompt.

24:12

We talked about that and this session we will get a little deeper into we'll kind of extend that

24:18

conversation. We'll talk about prompting. So we'll talk about that, but we will be seeing how we can use a bit of Python. We'll be using large language models using Python calls. And I will also introduce a few really cool API, some new things we will do. And there is also something called Olama that we will discuss. Right. So a lot of new things, a lot of new terms, but unlike the last session where we were primarily, you know, going to

24:48

chat GPT and Gemini interface and GROC interface and, you know, we were not coding anything.

24:55

Yes, we conceptually understood a lot of things, but we were not really coding anything.

24:59

So today's session will actually write a lot of code.

25:02

We'll do a lot of coding in this, in this particular sense. Okay?

25:05

So that's how we will pace it out. Okay.

25:10

All right. So now, with this in mind, let's, so the contents once again are part of your

25:18

Google Drive, same way as I upload always. Let me quickly go ahead and share my screen.

25:25

Just give me one minute, French. Yeah, here it is. Here it is. Here it is. All of you can see my screen.

25:33

All right. Yeah, yeah, yeah. You'll do that. I'll do that. I'll do that. I've done that. Yes, I've done that.

25:41

I don't know why the FDban modes gets disabled. But yeah, I've done that. Okay. Everyone can, you can chat with everything.

25:48

Okay. Yeah. Great. Great. So yeah, let's start on. And first things, first, what I would like you to do. You know, I'm going to straight

25:59

away jump into the different modules and all that that we have. We'll talk about the different types of things.

26:06

And we'll specifically talk about something called Olama in the session today. Right.

26:12

So what is a large language model by now? Everybody understands. We spent a lot of time discussing.

26:18

that what is LLMs and what is it? What is the prompt? So the large language model is basically that

26:23

that processing engine, that's that brain. It's that model that will take in some input and it will give some output. That is what the LLN basically is. So the LLM is basically that brain that takes in some input from and it generates some output response.

26:37

That is what the large language model basically is. That's what the LLF basically is. Okay. Now, the question is where is that LLM

26:47

going to resign. Now, I talked about two interesting, uh, interesting

26:56

scenarios in the before as well and I'm going to go ahead and give you a small analogy once

27:02

again to help you understand this a little better, right? So there is an option called a local

27:09

LLN and there is an option called a cloud LLN. So the large language model is a massive entity.

27:17

And now the question is where will the large language model really reside?

27:23

Where will it reside? Will that large language model reside in your current system, in your current hardware,

27:33

or will that large language model reside on the cloud? So where will that large language model actually reside?

27:40

That's what we are trying to understand. Okay. So if you look at

27:47

at it, there are two of these setups we will discuss here. And the analogy is almost like

27:52

food delivery. You know, if you want to, let's say, have chicken biryani. What are the two options you

27:59

have? Option number one is cloud delivery. But the concept of cloud kitchen. So you can just go to the

28:08

application, you can order, you pay for the service and you get it back. You don't have to do anything

28:13

at home. That is option number one. So all the heavy lifting is high.

28:17

happening in the kitchen. Somebody is preparing the food for you. Delivery person is going.

28:24

So khana up and they're giving it back to you. So that is a cloud model. And that is the same way how

28:30

cloud LLMs also operate. So this large language model is a massive model. It is a massive model like

28:39

GPD4, Gemini. We'll be using these things in our class today. These models are massive. And you need a lot of

28:45

memory to store it. And this thing we're

28:48

a lot of class in more actually saying, why am I saying you need a lot of

28:51

memory to store these models? We will see this in a better way today.

28:57

So what we are doing is we are taking these models and we are

29:01

storing them in the cloud.

29:04

You have, up, up, upne machine, store need to store

29:06

even if you have these models hosted on the cloud. And if somebody wants to

29:11

use it, they will have to access that model and get the

29:15

response back. Access the model, get the response back. Access the model, get the

29:19

response back. That's the intuition.

29:22

The other option is what we call a local LLM. Local LLM is like cooking at cooking at home.

29:30

If you want chicken biryani, you cannot order chicken biryani from somewhere. You cannot

29:35

order chicken biryani from somewhere. You don't have to, but you know, you can basically have a kitchen,

29:39

have a kitchen, you can procure all the ingredients, all the set up gas,

29:45

everything you can have and you can go back and effectively, you know, kind of do the entire

29:52

cooking at home. So that's the way how this whole thing will work out. Okay. So this is the

29:59

difference between cloud LLMs and local LLMs. So local cloud LLLLMs are where the LLM is hosted on

30:05

the cloud. Okay, there is a, there's a cloud where the, where the large language model is hosted. That is

30:11

what we refer to as cloud LLMs. And local LLNMs are basically

30:15

where local LLMs are basically where, you know, as I say, this is the kind of set up where,

30:21

you know, we can say that the LLMs are hosted locally. You're downloading it locally.

30:28

Okay?

30:28

I mean, the software, everything is in your own hardware.

30:32

Yeah, I wish that I would not say restrictions.

30:36

Ullta is. Local in the restriction there. Because local in to your hardware.

30:40

There is no restriction in how you want to use it. But yes, the restriction will be how powerful and

30:45

how fast you will get the responses. And we will do a live demo of this.

30:48

We're both of them. We'll do a live demo as we'll, so you answer

30:50

soon will be what I mean to say. So if your, if your machine is not that

30:54

powerful, if your, if your car RAM is, if you're at first GEP car RAM, then

30:57

you'll see a very slow response. And people who are on very high-end

31:03

machines, you will see an instant difference. You'll see an instant difference.

31:05

You'll see, you'll see it completely depends on the, on the

31:10

hardware capacity of your machine. Okay. So that is the

31:14

way to look at it. So this is the analogy. I hope everybody is clear. Cloud

31:19

LLMs, where the models are hosted in some other place, we will access them. And local

31:25

LLMs, where the models are hosted locally, we'll download khani, we'll upload kind of small models

31:31

because, you know, we cannot download a GPT4. It's used, is massive at that scale.

31:35

So we will be downloading smaller models and we will just see how we can do some simple demos

31:40

based on that. So don't know what are the difference. What are the different? What are the different?

31:44

references basically, right? So if you look at it, these are two broad scenarios we have right now.

31:51

We have local environment, we have cloud API. From a cost perspective, local, local environment is totally free.

31:58

There is zero free inference, zero cost is involved. And if you look at a cloud API, it is pay per token.

32:05

But now you have to pay. So based on usage, you will have to pay. That is the biggest advantage. Obviously, in our sessions, I will give you some

32:12

access to some free providers. So coffee free providers. So you can get a lot of demos done

32:19

for free. But generally, the cloud APIs are very expensive. Okay, because, so what happens is these models are

32:27

hosted somewhere else, right? And because these models are hosted somewhere else in some cloud

32:34

environment, what will happen is that it will be very costly because somebody else is managing. This is the

32:42

same example I told you for the chicken biryani. You have ordered

32:45

there. Maybe there. It's gas, it's rent, his

32:49

house, his house, his kitchen, set up. It's, who's? The pisa can't. You can't be. So you're

32:55

paying for the food. So similarly here, if you're using a cloud API, if you're using a large

32:59

language model that is living in the cloud, you have to pay them to. And that's how much is

33:04

pricing and all that we will see. But you'll have to pay for it. Right? But if you're local

33:07

you'll make? So inference is free. There is a one-time cost up

33:13

is, it's not that local free is. So free inference,

33:16

I mean, just birri-bri-bri-bri-bri-bri-bri-barnie-barned to

33:19

no kind of a kind of effort. That's just your effort.

33:22

But there is a capital investment.

33:24

You have a kitchen-barned, gas-lenaed, everything. It's more hassle.

33:28

But it's more restriction-free.

33:30

Right? Here, there's a restriction. You can't do. You have enough hardware.

33:34

No. So you can see hardware constraint bound by local RAM and CPU.

33:37

limit but access to massive GPU clusters.

33:40

Because in cloud where your model is

33:45

living somewhere else, it is living on some other computer,

33:49

that computer is very powerful

33:51

can't. But,

33:53

when we're in class in models we're

33:55

in our system in download

33:56

it will be very, it might be very slow.

33:59

So hardware constraint

33:59

is also a big factor.

34:02

Privacy is also a big factor. Privacy factor

34:03

is the idea, that is the thing

34:05

is when we download

34:08

locally, everything

34:09

is running on our own hardware.

34:12

Everything is running on our own hardware.

34:14

Everything is running on our own hardware. Everything is running

34:14

on our own machine.

34:16

So data stays on the device.

34:17

That is one thing you will have to keep in mind.

34:19

So the data, whatever data we are talking about,

34:21

that stays on the device. It stays on your device.

34:24

It doesn't go outside your device.

34:26

So Olama, that way is very, very safe.

34:28

The local environment is very safe.

34:30

Which is why we often say

34:31

that enterprises who are working on very sensitive

34:34

applications.

34:35

Both sensitive sectors

34:36

in your work

34:37

so this is a very preferred way of doing it.

34:40

But please remember, there is a lot

34:42

of investment you will have to

34:44

make in the hardware,

34:45

you have to make in the hardware. Yes,

34:45

you have to invest

34:46

have.

34:47

Yeah, yeah.

34:51

Yeah, ain't that strong

34:52

so correct.

34:53

You're right that is correct.

34:53

So we'll do that, we'll be demo

34:55

but I will give you smaller models.

34:58

You have all varieties of models.

35:00

You have all varieties of models.

35:00

You have 200 Mbbbbg's models.

35:02

5500 Mbc can.

35:03

I'm we'll do that every single person is able to run these models on your laptop.

35:08

So you'll be able to see.

35:09

You'll be able to see.

35:10

You can you can't see.

35:10

And some other remote computer.

35:16

That's one of a option.

35:17

He's pe to do something.

35:18

In fact, most of our demos will be on this.

35:21

I will follow this setup for majority of the course.

35:24

But today we want to give you a flavor of this.

35:27

And as you rightly said, it's not expected.

35:29

I mean, not only for you.

35:30

Even I don't have a, like, at least the session I'm taking right now.

35:33

So I have a GPU laptop in my home, but this one is a basic one.

35:40

This way, I cannot also download a 100 gp model.

35:43

It'll go.

35:43

It's not required also.

35:47

Now, now, now, you know, now.

35:48

The concept is important to understand.

35:49

It's a thing to look one again.

35:51

But it's not important to download a 100 gp model.

35:53

And it's useless.

35:54

I mean, I say that if you, see, it is like if you have an option,

35:57

if you have an option that these models are already present in some place,

36:02

you access to.

36:03

problem.

36:04

You have us to pay and access to them.

36:06

We are learning, right?

36:09

We are not exactly working in an enterprise setup, building enterprise solutions.

36:12

So if security, it's not a big issue not.

36:15

If privacy, it's not bad issue there, then it's okay.

36:18

Cloud is the best way to go about it, quickly build some POCs and all that.

36:22

So that's the reason I always prefer for students and all.

36:25

Cloud is the best way to go about it.

36:26

And I'll show you some really cool cloud platforms like GROC and hugging face and

36:31

Olamma that you can use for accessing these.

36:33

language models.

36:35

Abhikar, that minimum, there is no definition of that.

36:39

It depends on your use case.

36:41

There is no definition of minimum.

36:42

So it depends on what you want to run.

36:45

Now you say, sir, I want to run a llama 100 billion parameter model.

36:48

So for you have to have 100 gp RAMs.

36:50

Now, so GCP RAMs, what's laptop in?

36:51

No, you cannot provision this kind of hardware.

36:55

You can't, you have up, up, up their machine,

36:56

LLMs, not can't.

36:58

Yeah, but if you're asking me for a general configuration, Avishkar,

37:02

if you want to run.

37:03

LLMs with some basic thing.

37:07

I think 64 GB RAM.

37:09

It'll be okay.

37:14

Absolutely.

37:15

It will download from authentic three sources only.

37:17

Absolutely.

37:18

I'm authentic.

37:19

We'll tell you.

37:19

I'm why.

37:21

I'm why you're piloting things

37:22

of course, of course.

37:25

I will tell you, authentic sources only.

37:27

Olama is very authentic.

37:28

GROC is very authentic.

37:29

GROC is very authentic.

37:29

There are, see, like,

37:30

there are a lot of third party glings,

37:33

like, don't use all that.

37:35

Those are all like, absolutely.

37:37

But these will be absolute enterprise options

37:39

we'll be seen in the class, okay?

37:40

Yeah, don't worry.

37:41

Let's move on.

37:43

And to start our conversation, what I will do,

37:45

we will quickly download Olama.

37:48

So, first we'll set up

37:50

we'll, a local environment set up

37:52

for him. Okay?

37:54

Let us do that.

37:55

So, this will be a very

37:57

step-by-step hands-on class today.

37:59

Unlike the other sessions, today's class will be

38:01

very hands-on.

38:03

can go to olama.com.

38:06

Okay?

38:08

And you can just click on this link.

38:12

You can just click

38:12

on that.

38:15

You can just click on that. You go to the URL,

38:16

everybody, and please download it.

38:18

Okay, you're all right?

38:18

You can, you all right?

38:18

You can, everybody will also do along with you.

38:21

Everybody will do along with me.

38:23

This is the exercise.

38:25

This is the very hands-on session today.

38:26

So concept-wise is less,

38:29

practical is a lot more today.

38:31

So,

38:33

We want all of you to install.

38:34

We want you to run a model.

38:36

We want you to use a cloud.

38:38

Because the prompting,

38:39

whatever,

38:39

what we've discussed

38:40

that is sorted.

38:40

We have done all that.

38:41

So today is a very hands-on session.

38:43

It's like 80,

38:44

90% hands-on,

38:45

10% percent,

38:46

me talking.

38:47

So most of the class,

38:48

we will do hands-on today.

38:50

Okay?

38:50

So all of you please download this.

38:52

Now, look,

38:52

here here Mac, Linux,

38:53

there,

38:54

so you know what laptop

38:55

you'll know.

38:56

You guys will know

38:57

what operating system

38:58

you have tickets.

38:59

So your Jasa operating system

39:00

is, mostly I'm guessing

39:02

because Windows is

39:03

popular,

39:04

or Windows or Mac

39:05

or Mac

39:05

will, rarely

39:06

some Linux

39:06

will majorly.

39:08

So you

39:08

know,

39:08

you know,

39:09

so I will

39:11

also do it

39:11

parallel

39:11

so

39:12

you'll

39:13

also do it

39:13

download

39:13

is

39:13

okay.

39:14

So let's

39:15

be patient.

39:17

Let's be patient.

39:17

Let's be patient.

39:18

But I really

39:19

want you to do

39:19

it, okay?

39:19

Everybody,

39:20

please do it.

39:33

No, no, it's, it's the same.

39:49

I think just, yeah, if you, if you, if you're, so you want to see your windows or

39:54

whatever, I think it, it,

39:57

Linux is always lightweight from that perspective, but, but, but, but you can download

40:03

it.

40:03

You can you.

40:04

You can't

40:05

it.

40:06

There's no problem there.

40:07

Yeah.

40:11

So,

40:12

Ranjan, right?

40:14

Ranjan, if I can,

40:15

I hope I'm

40:16

pronoun

40:17

your name correctly.

40:18

Ranjan, absolutely.

40:19

This is a demo we are doing.

40:20

You can use other things also.

40:22

There are

40:23

many things are

40:24

there.

40:25

LM studio is another thing that is there.

40:27

Right, but this is

40:28

this is part of what we are

40:29

covering in the content.

40:30

But just like Olama,

40:31

there are other setups

40:32

other setups also available.

40:33

so you,

40:34

you can

40:35

a learning for

40:36

Okay?

40:37

Definitely.

40:38

Definitely.

40:39

Since you are using it already, you know what

40:40

Olama is already.

40:41

Which is great.

40:42

You can just write it out.

40:45

Olama is one of the most popular

40:48

most popular out there today as we speak.

41:02

So,

41:04

G.

41:06

2GP's download,

41:08

guys, so it

41:09

2GP download, guys, so it's a little

41:24

so it's time

41:27

I think it's got almost up.

41:29

Olama set up, eXE file

41:31

been here.

41:32

People who are on Windows,

41:33

you will see this, I'm demonstrating on Windows,

41:35

so people who are on Mac, you already know how to do it,

41:38

would, the same.

41:39

One way that you access a software,

41:41

download and install a software.

41:43

Same type, you download

41:44

I'm moving on, because my

41:46

now here,

41:47

let me click on the EXC file.

41:49

Now we'll set up.

41:50

We're set-up.

41:51

There's nothing.

41:52

Next, next, next, next, finish.

41:53

That's it.

41:54

Okay, then it's okay.

41:55

You know, no problem.

41:57

Yeah.

41:59

Same way you proceed with the installation.

42:01

I'm also doing it in front of you.

42:03

Okay.

42:04

This normal install.

42:05

It's not.

42:06

You're a pop-up in install.

42:07

It will click.

42:08

All go.

42:09

nothing you will have to do.

42:11

That's it.

42:12

People, please complete it.

42:14

And with this, you will get a flavor of some of the things.

42:17

You know, you might be wondering,

42:22

that, if you're going to,

42:23

so challenge, what is?

42:25

All this while in my classes, I was telling,

42:26

that all these models are very big.

42:28

That big of what is what?

42:30

Now, you know,

42:31

I was just telling you,

42:33

that's 4MB, 10, GB, but you will realize

42:36

why these models are so powerful and why

42:38

and why, like, they require so much of computation.

42:41

Your machine will not.

42:43

We'll make a demo, it will run very well,

42:45

and I'll show another demo very will say it will be very slow.

42:48

And you will instantly realize a difference between cloud

42:51

and local care.

42:53

Okay.

42:54

All of you do it.

42:56

I'll just give you two minutes of time, please.

43:02

I'll just pause until the time it's complete.

43:08

Thank you.

43:10

Thank you.

43:12

Thank you.

43:42

Okay, okay,

43:46

Okay, okay, Alu, are you good, that's okay,

43:49

it'll be a while, I know, it'll be good, that's okay, it'll take a while, I know, I know, it'll take a while.

44:07

It'll take a while.

44:08

No problem. Let it download.

44:09

It's 2GB.

44:11

So that's okay, no problem, but it's very important all of you do the demo.

44:15

As I told you, this is, this is given the most important part for today.

44:19

Everybody should be able to do it.

44:27

Set up maybe, it depends.

44:30

I am on a very powerful system.

44:32

Merey, it's time like it depends on what system you're on.

44:37

So it's actually quite slow.

44:39

Install might take five minutes.

44:40

take five minutes some of you take it that's okay we'll wait for a while

45:10

Thank you.

45:40

Thank you.

46:10

Thank you.

46:40

I hope everybody is

46:56

Ah, no, that's okay, that's okay, uh,

46:58

No, no, that's okay, that's okay, Kunal.

47:00

Don't worry, don't worry.

47:01

Take your time, take your time, take your time.

47:02

See, just because it happened fast for me doesn't happen, doesn't mean, that's okay, that's okay.

47:06

We have the time for all this today, don't worry.

47:08

As I've clearly said today,

47:09

I have clearly said today is a very hands-on session.

47:11

We want each one of you to do this along with me.

47:13

Okay?

47:14

That's okay.

47:15

Take your time.

47:16

But everybody must have Olamma downloaded.

47:17

Everybody must have Olamah Rani.

47:19

I will leave another five minutes if required.

47:22

It's okay.

47:23

Take your time. Take five minutes, okay?

47:25

Everybody should see a console like this come up

47:27

where there is Olamma, something like this.

47:29

Kuch, could start, okay?

47:31

That's it.

47:32

We will discuss other things, okay?

47:34

Don't worry.

47:36

All of you please install.

47:39

and once it is successfully installed,

47:43

we will start the discussion.

47:45

I'll just wait for another maximum.

47:47

Five minutes for everybody.

48:09

Thank you.

48:39

Olama is basically a platform.

48:43

So, Ali, just to answer your question in the meantime, what is Olam?

48:49

Olam is effectively a local runtime for large language models.

48:55

So I started my session today.

48:57

I started my session today with the two setups, right?

49:01

I hope you follow this, right?

49:03

This part of the discussion, I hope you followed, right?

49:05

Cloud or local.

49:08

is used for doing this.

49:11

So if I have to give you an analogy, Ali, Olama helps you build a kitchen at home, cooking at home.

49:17

That's what your whole set-up been a setup.

49:19

Think of Olama on the right-hand side.

49:21

But the Olama is like a platform that helps you implement local elements.

49:27

But you, you know, you can download

49:30

through the Olamma platform.

49:33

And you can run them from your machine.

49:36

Okay? Make sense, Ali.

49:38

Whereas in the cloud, you don't, you're not downloading anything.

49:42

You are only accessing a service and you're getting a response.

49:46

Just like ordering food.

49:48

Okay.

49:49

So Olama is like this.

49:51

That's why I told you it gives you more control and more security and those kinds of things.

49:55

Okay.

49:57

Okay.

49:57

Very good.

49:58

So, yeah, and just just wait for another four minutes for all of you to compete.

50:08

What is the inference?

50:19

Inference basically means, inference basically means prediction.

50:26

I'm an inference term previously used here.

50:28

I think even during machine learning, I have also used that term inference.

50:33

So, Ranjan, if you, if you remember, there are two parts of machine learning.

50:37

So, the part is what?

50:39

First part is you're using the data and you're building a model.

50:42

The first part is you are using some data and you're building a model.

50:47

You have data.

50:48

You have a algorithm used and model

50:50

that is the first part.

50:52

And once the model is built, once the model is trained,

50:55

the second part is you're using that trained model for doing predictions.

50:59

That we're inference.

51:01

When you're using a trained model for doing predictions,

51:04

that is what is referred to as inference.

51:07

Okay, I hope you're clear.

51:10

Is now?

51:16

And inference is not just for LLMs, right?

51:18

It is a general machine learning concept.

51:21

You have a model.

51:22

That time, we, we have machine learning models.

51:24

Here we have language models.

51:27

Models been made, right?

51:28

You are using that model to get answers.

51:33

I'm not even talking about Hugging face in the class right now.

51:36

Hanging Pes is talking about it.

51:38

We'll come to that.

51:38

I don't want to distract to Hugging Pace.

51:40

We'll come to that.

51:41

I'll explain Hanging Pace also.

51:43

We'll tell you that.

51:44

But let's not go to Hanging Pace right now.

51:46

I will explain Hanging Pace what.

51:49

Basically, there there's your models

51:50

have been made.

51:51

That's a cloud kind of provider.

51:54

But we will come to that later.

51:55

That is not the intent for today.

51:57

But since you ask that question,

52:01

Ranjan, Hanging Fess, what are what are.

52:03

Hanging Fess in the models been.

52:05

There were models available.

52:06

is available.

52:07

And you're just access

52:08

but what that is?

52:09

But what is?

52:09

How's demo we will discuss.

52:11

Don't worry.

52:12

Okay?

52:13

We will discuss that later.

52:14

Just two minutes more, guys.

52:16

For the Olama setup.

52:18

People who are done, please,

52:19

let me know.

52:20

Yes on chat.

52:21

Set up who are, please.

52:26

Nothing.

52:26

No,

52:26

do anything.

52:27

Don't worry.

52:28

Okay?

52:29

Thank you, Ranjin.

52:30

Yeah, no, I'll discuss.

52:31

I'll discuss everything.

52:32

Don't worry.

52:32

Don't do anything.

52:33

Just let me know with a quick, yes.

52:35

People were done.

52:36

Okay, okay, okay, okay, okay.

52:39

Okay, others, others let me know.

52:45

Everyone must do it, okay?

52:47

Everyone must do it.

52:49

Bucky classes, I don't, I don't push you so much

52:51

because those are concepts that are there.

52:54

But today's class is primarily hands-on.

52:56

This way, you have to be part of the hands-on.

53:00

That's the whole intent, okay?

53:02

And a lot of our LLM classes will be like that.

53:06

want you to do the practice, it will be very much driven like a boot camp where we want you to do

53:10

along with me. That's how it will, you know, it will be like, okay? Yeah. Okay, very good, very

53:15

good. Getting installed. Take your time, take your time. Take your time. No problem. Take it. That's okay.

53:23

Let's take, let's take a few minutes more.

53:36

Thank you.

54:06

Thank you.

54:36

Thank you.

55:06

Yeah, it'll be fine, don't worry, don't worry.

55:26

it'll be fine.

55:30

Error, it's a very, very simple install.

55:34

You ideally should not get an error.

55:36

It's a normal install that you're getting.

55:40

Error to need to be a normal install that you're getting.

55:44

If you can please paste the error message, I can, I can try to help you.

55:52

So then, then, then, then, then, then, then, then, then, then, that's a system with, you can, I can try to help you.

55:56

settings will then.

55:57

Because this is simple install.

55:59

See, normally in the time, you have to choose

56:01

folder,

56:02

to do this thing to do

56:04

do it. So, here, there

56:05

there's nothing

56:05

to do anything. Just, you

56:07

press it, it will go. So it

56:10

could be, it is interfering with some

56:12

other files in your system, could be.

56:16

If you can be, we still have time

56:18

right now. You if you're a

56:19

if you're a bit, if you're just

56:20

start and restart and get back back

56:21

back again, that will be great.

56:26

Is it? So, yeah. So I think your fan speed has increased

56:29

are, is that so?

56:30

You know, fan speed has been

56:31

got, yeah. Because I think

56:34

the, you know, you'll get a feel for it, obviously.

56:40

Yeah. Fan speed

56:41

will be a bit better. Now, when

56:42

models on and if you're,

56:43

more be, more be sort of intensive

56:46

over. I'm looking, we'll take

56:46

that how it's going.

56:48

Yuvraj, if you can, one

56:49

you can, one, you can, start

56:51

start and start and again, once

56:53

try it out, you can.

56:56

Ah, okay, okay,

56:59

okay, yeah, that's

57:00

correct, correct.

57:02

You're the requirement

57:02

are it, so you

57:03

you're going to

57:03

give you

57:04

need to do.

57:05

Yeah,

57:05

VC plus and DL

57:06

is okay,

57:07

they're stuck

57:07

are stuck

57:07

error to

57:08

it will give you

57:09

a link to

57:10

install it

57:10

so you

57:10

you'll click

57:11

to install

57:11

it,

57:13

you'll install

57:15

you know.

57:16

That could be

57:17

that's a good

57:17

point,

57:17

Angit, thanks

57:18

for mentioning.

57:20

Maybe,

57:21

uh,

57:21

Ankit, you can actually post that to everyone on chat.

57:25

Others can also see what you, what you said.

57:28

Yeah, so B, C, plus, plus,

57:29

something will be,

57:29

there's a message are

57:32

there.

57:32

Yeah.

57:46

That's, it's a message out.

57:48

it is, you know, you know,

57:50

your C,

57:51

drive or

57:51

there

57:52

your

57:52

space

57:54

there's

57:54

so that

57:55

is obvious

57:55

so

57:56

you

57:56

have

57:56

you

57:56

have

57:57

done

57:57

have

57:57

installed

57:57

have

57:58

, right.

58:27

you.

58:29

you.

58:30

You

58:31

you.

58:33

You

58:35

you.

58:37

You

58:38

You

58:40

You

58:42

Thank you.

59:12

Thank you, okay, okay, very good, very good.

59:36

Thank you, thank you, Sanita, good.

59:39

Others who are trying, I hope you are done.

59:42

please let you know the once you have completed once you've already pinged is fine

59:45

just the ones who are trying we're done let you know okay okay

59:51

okay very good very good

1:0:12

So now.

1:0:42

Now that you guys have already done this and just to clarify, this is the platform that we will be using to run the models.

1:0:49

Now that everybody has installed Olamma.

1:0:50

Now we look at the next step.

1:0:53

So, now, back any, you know, close to do.

1:0:55

Just close everything.

1:0:59

And now what we will do is we will go and use the CLI, the command line interface and we will be

1:1:06

accessing Olamo.

1:1:09

That is what we'll be doing.

1:1:10

So, okay, let's go.

1:1:10

So, okay, let's do Olamma.

1:1:12

whatever the application is coming, you can start it, right?

1:1:15

And here you'll be able to see, here you'll be able to see settings.

1:1:22

These are the settings.

1:1:24

Okay, normal settings are there.

1:1:27

And this is OLAMA account you can also create.

1:1:30

And this is the models location.

1:1:31

Up they're secure the location where the models are stored.

1:1:34

Can you see?

1:1:35

All this file I was, now I was mentioning that Olama is where you are trying to download the models

1:1:40

locally.

1:1:41

you know, you are the system in models store

1:1:42

and these are very, very big models.

1:1:45

So where you're download

1:1:46

you, this location in the models download

1:1:49

so see us are sign Olama.

1:1:51

So this is for me. You guys will have a different thing.

1:1:54

Okay?

1:1:54

Now, now moving on, what I will do,

1:1:57

I will go to new chat.

1:1:59

Everybody do this along with me.

1:2:00

You go to something called new chat.

1:2:03

And once we are here,

1:2:06

we want to start with a basic model.

1:2:09

go to new chat.

1:2:35

Everybody click on new chat.

1:2:39

download the models. Here

1:2:40

you're up models for download

1:2:41

can't.

1:2:42

and here

1:2:43

a model

1:2:44

is Jema4.

1:2:46

Olama.com

1:2:47

may go

1:2:47

and you can see

1:2:49

this is Jema4.

1:2:50

So these are all the

1:2:51

different different models

1:2:51

which are available.

1:2:52

If you click on Jema 4,

1:2:54

Jemma 4 comes in

1:2:54

many, many different versions.

1:2:57

Short-time mobile model

1:2:58

be out,

1:2:58

barren models be out

1:2:59

so that are different

1:3:00

different versions in which the

1:3:01

Gema 4 model is available.

1:3:04

Okay?

1:3:04

So you can take a look at it.

1:3:05

And this is your

1:3:06

coin 3.6

1:3:08

This is your Jemar 4.

1:3:09

port. So these are all the different

1:3:10

different types of models that we have

1:3:12

that we have here.

1:3:14

Okay?

1:3:14

Now, when you click on this,

1:3:18

when you send a message,

1:3:20

what will happen is the model will get downloaded.

1:3:22

So we'll make it more

1:3:23

actually way can.

1:3:24

We want to have some more control over the process.

1:3:26

So let us see how we can

1:3:27

how we can do this.

1:3:29

So this is just one interface I wanted to share with you.

1:3:32

The next interface that I want to do

1:3:34

do,

1:3:34

yeah, correct, correct.

1:3:35

Cloud sign is different.

1:3:38

That's a good question.

1:3:39

Okay, Cloud basically stands for the models

1:3:41

which are present in olama.com.

1:3:44

So olama.com may be

1:3:46

some cloud models are also hosted.

1:3:48

That's the cloud models are.

1:3:50

So to answer your question,

1:3:52

difference is that these models are,

1:3:54

you can download locally,

1:3:55

but these models are hosted on the cloud.

1:3:57

You're download not downloading.

1:3:59

That's the thing.

1:4:01

So Lama gives you basically both options.

1:4:03

See, I started by saying that

1:4:05

there are two options, like

1:4:06

cloud and local have.

1:4:09

We have actually two.

1:4:10

Olamma is mainly used for local LLMs,

1:4:12

but OLAMA has some element of cloud also.

1:4:15

But there are some models which are hosted on the cloud.

1:4:18

Some models are in the cloud.

1:4:20

You can't access to.

1:4:22

And some models you're installed and access

1:4:24

access to.

1:4:24

Okay?

1:4:25

So what I would like you to do,

1:4:27

you please start Windows PowerShell.

1:4:29

All of you.

1:4:30

Windows PowerShell.

1:4:32

All of you start Windows PowerShell, everybody.

1:4:34

So if you are Windows in,

1:4:35

then PowerShell should start PowerShell

1:4:36

start to do.

1:4:37

If you're at all of you,

1:4:38

this is a command from Mac

1:4:40

in the terminal in

1:4:41

go to your terminal, all of you.

1:4:44

And now that you guys have OLAMA installed,

1:4:46

what is the way to validate Olamma?

1:4:49

The way to validate Olama is

1:4:50

you can simply say Olamma

1:4:52

hyphen hyphen version.

1:4:55

You can simply say

1:4:56

Olama hyphen hyphen version.

1:4:59

Everybody can do this

1:5:00

and this way you can check,

1:5:02

you can validate that

1:5:03

yes, I have the right version of Olama.

1:5:06

Actually, that, you know,

1:5:08

you know, what we've seen

1:5:09

that was just for your knowledge.

1:5:12

That we're just for your knowledge.

1:5:12

That we're not doing.

1:5:13

That's a bachar thing.

1:5:14

That's a bit of a bitar

1:5:15

it.

1:5:15

It's not used

1:5:16

there.

1:5:17

Actually,

1:5:18

practically this is what is

1:5:19

important and

1:5:20

whatever we will see in

1:5:21

Jupiter and Kolaav will be important.

1:5:23

But that thing is

1:5:24

useless, actually.

1:5:25

I just wanted to show you

1:5:26

what it is.

1:5:28

Okay?

1:5:28

So all of you do

1:5:30

Olama hyphen hyphen

1:5:31

version and please see

1:5:33

if you're getting

1:5:33

version number this.

1:5:35

People who are on

1:5:36

Mac, you can use your terminal

1:5:37

and people who are on Windows

1:5:38

can use your power shell

1:5:39

or command prompt.

1:5:41

Same way it will work.

1:5:42

Okay?

1:5:42

This is your normal

1:5:43

power shell

1:5:43

is not.

1:5:47

This will give us

1:5:48

more control.

1:5:49

Now,

1:5:49

look,

1:5:49

here here

1:5:50

there's a lot

1:5:50

just to clarify,

1:5:53

if I go back

1:5:54

and show you this way,

1:5:55

here here

1:5:55

I only have these many

1:5:56

models.

1:5:56

We have other models

1:5:57

options in

1:5:58

we have.

1:5:58

We're fine

1:5:59

then if we're fine

1:5:59

so

1:5:59

there are limitations

1:6:03

you have to sign in

1:6:04

you have to sign in

1:6:04

all that.

1:6:05

This is just a thing.

1:6:06

But what you can do now?

1:6:09

But here

1:6:10

you will have to go back

1:6:12

and you can interact

1:6:15

with the thing more freely.

1:6:17

That's the intuition.

1:6:18

You can interact

1:6:19

with the thing more freely.

1:6:21

And the specific models

1:6:22

that I want to use

1:6:23

is a very, very popular model.

1:6:25

All of you would have

1:6:26

heard of the Gemma model.

1:6:29

So we can use

1:6:30

or then what we can do is for our demo.

1:6:34

But demo purpose

1:6:34

we can go back and use

1:6:36

a slightly different model

1:6:38

called Quain

1:6:39

Quint 2. And I think

1:6:42

I can assure you, even the

1:6:44

even the

1:6:44

most basic of laptops,

1:6:48

this one will go

1:6:48

this one to go. This one

1:6:50

is there. No issue

1:6:52

need to. Okay. Quent 2.5

1:6:54

I will quickly

1:6:55

have all of you

1:6:59

to install the

1:7:01

Quent 2.5.

1:7:04

0.5 billion parameter model.

1:7:06

is a model. Quen is a model. There are

1:7:08

many, many language models out there.

1:7:10

So, Coen is

1:7:12

one of these language models that are there.

1:7:14

Or when you go to the Olama

1:7:16

website, you'll see you, you can't, you can't

1:7:17

any model choose

1:7:18

can. Like, you have Coen 2.5

1:7:20

to select you. Here, you

1:7:22

see what are the different, different versions

1:7:24

of the model? And you can't see

1:7:26

see. You know? You know,

1:7:27

now? You know, I'm talking about.

1:7:30

It is, it is by a company called

1:7:31

Alibaba.

1:7:33

Chinese model, correct.

1:7:34

And you can see, it is point.

1:7:36

billion parameter. It's a very small model and its size

1:7:39

is only 300 mb. This is something everybody can work with.

1:7:43

It is not very powerful, not very powerful, but something that will easily

1:7:47

install in our system. And you can't difference

1:7:49

see can't. Quain's 300 mb

1:7:52

model and that same coin's 47 gb

1:7:56

model is. Now you choose which one you want to install.

1:7:59

Now remember, if you download

1:8:01

and run it, then you'll have this minimum RAM

1:8:04

need to be. And I'm, and even 8GB system in

1:8:08

this RAM, you know, it's all right? It's

1:8:09

so RAM to have all right? Now, 400 MB RAMs to

1:8:13

be able to be able to go. If you're Word document or Google Chrome

1:8:15

be, so 400, or 1GB use

1:8:17

Chrome in. This is all of all. But don't try to run this model

1:8:21

because your system will crash. Because 47GB

1:8:24

when you try to run, that whole 47 GB

1:8:27

RAM utilize can make. And this, I'll

1:8:30

me and this I'll make a real-time demo

1:8:31

will. Everybody can do the demo with me.

1:8:34

We'll real-time demo where you can see,

1:8:36

this is our system, this is our performance.

1:8:39

So here, you can see,

1:8:41

I'm utilizing 17 gb of RAM right now.

1:8:43

I'm utilizing 17 gb of RAM right now.

1:8:44

So I can afford to take a more powerful model.

1:8:48

I can do that.

1:8:49

Okay, I can do all that.

1:8:50

But then you have to also check

1:8:53

that your remaining memory is

1:8:54

Windows is 10,

1:8:56

20 gb can't.

1:8:57

Windows is actually very memory intensive.

1:9:00

So you will also need to go to your task manager and check.

1:9:03

You know?

1:9:04

If the task manager click

1:9:05

there on,

1:9:06

check how many utilized

1:9:07

on that on that basis

1:9:08

you can use the model.

1:9:09

But just for the class demo,

1:9:11

we will use the 0.5 billion parameter model.

1:9:13

Vinica, memory allocation still failed.

1:9:19

Oh, memory allocation failed.

1:9:22

What are you?

1:9:23

Like, your Olam installed, no?

1:9:26

You can follow along, no worry.

1:9:27

You can follow along, Vinica, no

1:9:29

but can,

1:9:31

can you help me understand a little?

1:9:33

until what point you have done?

1:9:35

I hope you have done until the

1:9:38

the Olama installation, right?

1:9:41

Olami installation, that you have done, right?

1:9:44

Okay, very good, very good.

1:9:47

Then what is the issue?

1:9:48

Power shell start here.

1:9:50

So this start to what are what are

1:9:52

you are typing Olam version?

1:9:54

Are you seeing C, Windows, System 32?

1:9:56

This is right?

1:10:01

Okay.

1:10:07

Okay.

1:10:08

Uh...

1:10:11

Uh...

1:10:16

What the message is giving?

1:10:21

Sorry.

1:10:22

I'm sorry.

1:10:23

I'm sorry.

1:10:24

What, that giving up?

1:10:25

What, that's the message is giving up?

1:10:26

I'm confused, actually.

1:10:28

That's interesting.

1:10:30

Okay.

1:10:31

For a minute, I thought you're giving up.

1:10:34

So, okay, so, so, uh, one second.

1:10:38

How do I check?

1:10:42

So maybe Arshita can help you a little bit with the installation part.

1:10:46

A one.

1:10:47

Can you just try in the command prompt once?

1:10:50

Can you try in the command prompt once?

1:10:53

You can try in the command prompt?

1:10:56

Command prompt, go and try it.

1:10:58

Same is.

1:10:59

Either we try can try to come in command prompt.

1:11:01

Go.

1:11:02

Look, the part is one.

1:11:04

Okay.

1:11:05

See, I'm telling you PowerShell.

1:11:08

PowerShell and this is the command prom by the way.

1:11:10

How do you launch command from, Vinica?

1:11:12

You can see my screen.

1:11:13

Command prompt start.

1:11:14

Just type COMMMA.

1:11:16

Windows in your command prompt.

1:11:17

Okay?

1:11:18

Here, same type.

1:11:19

Here you're command prompt.

1:11:21

Same thing.

1:11:22

You're here.

1:11:23

If here here,

1:11:24

if it's here here,

1:11:25

if it's going,

1:11:26

sorry,

1:11:27

this is my mistake.

1:11:28

It will be hyphen hyphen version.

1:11:30

This is same data, okay?

1:11:32

Please try and command prompt and check,

1:11:34

one.

1:11:35

If not, if you should do our system restart

1:11:37

and then it will work, okay?

1:11:39

Okay?

1:11:40

So now, coming back, I'll be using this particular model

1:11:43

and what is the code to download the model?

1:11:46

Now we'll download this

1:11:48

0.5 billion parameter.

1:11:50

So it's a very small model

1:11:51

and the code to download the model is this.

1:11:54

Okay, very nice, very nice.

1:11:56

Okay, so come on prompt on.

1:11:57

Okay.

1:11:58

Olam pool, this.

1:12:03

This is the code I wanted to run, all of you.

1:12:06

You have our screen is, everybody.

1:12:08

This is the code I want you to run.

1:12:10

So Colama pool is what is.

1:12:12

You are going to the Olama website.

1:12:14

The coin model we have you

1:12:16

you have to download you.

1:12:18

That's it.

1:12:19

See, this is a little download,

1:12:21

400 MB model is.

1:12:22

We are all downloading it right now.

1:12:24

And then we're going to use it.

1:12:26

Okay.

1:12:27

Okay, everybody please do it.

1:12:29

We'll have both things.

1:12:32

We'll, one Olama,

1:12:34

we can do,

1:12:35

and another one I will show you, you know, which

1:12:39

probably everybody may not be able to do,

1:12:41

because it will be a ram more used over.

1:12:43

Okay?

1:12:45

You can see the Olama model is getting downloaded

1:12:48

and this Olama model has been successfully downloaded right now.

1:12:51

So there are two specific commands we have seen.

1:12:53

One is version,

1:12:55

and one is Olama pool, where you're downloading.

1:12:56

where you're downloading a large language model.

1:12:58

And you can download any of the models.

1:13:00

There are hundreds of models available.

1:13:03

These are all open source models, free models.

1:13:05

They can go to go and go to it.

1:13:07

Like here, deep seek's a model.

1:13:09

Deepseek is also a Chinese company.

1:13:11

It's recently, four weeks already update

1:13:13

was, deep seek version four.

1:13:15

You can here.

1:13:16

These are all the different models.

1:13:17

These are all the different models that you have here.

1:13:21

This is the coin 3.5.

1:13:25

coin 3.5.

1:13:27

Look at this.

1:13:29

Look at these models.

1:13:31

These are all the models that you can download.

1:13:33

Can you see?

1:13:35

81 gb.

1:13:37

It's this big model.

1:13:39

81 gb.

1:13:41

Okay.

1:13:42

Anyways.

1:13:43

Now, next what we want to do.

1:13:45

We have talked about how do we go back and download the model.

1:13:49

And if you want to see the model,

1:13:51

now you have to see the model.

1:13:53

So let me take you to my

1:13:54

you to my drive.

1:13:56

I showed you, right, C.

1:13:57

This PC?

1:13:58

C.

1:13:59

Where are models?

1:14:00

See?

1:14:01

Users.

1:14:02

Cyan.

1:14:03

It's in Olam.

1:14:04

Olam.

1:14:05

There is Olam?

1:14:06

There is Olam?

1:14:08

There is Olam?

1:14:10

Everybody can navigate

1:14:12

to a similar folder location

1:14:14

in your system.

1:14:15

So it's all in your system

1:14:17

power.

1:14:18

It all depends on your system power.

1:14:20

Here, you see,

1:14:21

all models I will be there.

1:14:22

manifest in and then you will

1:14:24

these are these are

1:14:25

available.

1:14:26

So this is not human readable,

1:14:27

but the main thing that

1:14:29

the download was,

1:14:30

remember that when

1:14:31

that was that

1:14:32

how mb was

1:14:33

397,

1:14:34

you're approximately this 380 type

1:14:37

installed here.

1:14:39

This kb means

1:14:40

this Mb.

1:14:41

So this is the actual

1:14:43

this is the actual

1:14:45

model.

1:14:46

Okay?

1:14:47

This is the actual model.

1:14:49

Actually,

1:14:51

actually

1:14:52

That's a good question.

1:14:53

To some extent, the reason is because of the hardware, the underlying hardware, because

1:14:56

the underlying hardware is our own local hardware.

1:15:00

So the cloud models are running on better hardware.

1:15:02

So the same models can sometimes perform better on better hardware.

1:15:06

So that is just one other thing to keep in mind.

1:15:09

Okay.

1:15:10

All right.

1:15:11

Now, next what we will do, we will go back and run the model.

1:15:15

If you want to see what is the list of models available,

1:15:18

you can see what is the list of models available?

1:15:21

No, no, no problem, no problem.

1:15:25

And if you want to go and install another model, you can do that.

1:15:30

Just safe side, I will encourage people to install another model.

1:15:34

And you can run this command also, just safe side.

1:15:37

Just for fun, we can all do this one.

1:15:39

Olama pull.

1:15:40

Ola ma pull.

1:15:42

Or, yeah, this one, this one is optional.

1:15:46

Okay, people can do it.

1:15:48

People can do it. People might opt not to do it.

1:15:50

So, okay.

1:15:51

I'm not going to force you because this one is also small.

1:15:56

This one will be approximately, if you want me to show you,

1:16:01

if you said how big this model is, let me show you,

1:16:04

if you want me to show you how big this model is, I can show you.

1:16:07

This is the one billion parameter model.

1:16:10

This is the one billion parameter model.

1:16:13

This is size is about 1.3g.

1:16:15

So this is also small, reasonably small.

1:16:18

So we will, this is now pooled.

1:16:20

pooled.

1:16:21

This is going to download this.

1:16:23

Okay?

1:16:24

This go to download.

1:16:25

So 3.

1:16:26

So 3.2.

1:16:29

Sorry.

1:16:30

Excuse me.

1:16:35

Lama.

1:16:36

1 billion.

1:16:38

That's the model.

1:16:41

So let me run the code.

1:16:44

And Olama pool, this.

1:16:49

I will just make.

1:16:50

this to everybody.

1:16:52

So the end result would be what?

1:16:54

I would have two models that I would have downloaded.

1:16:57

One quen to and one is Lama.

1:16:59

Both we are now going to have the power of language models in my machine.

1:17:02

So we are now going to have the power of language models in my machine.

1:17:06

And we can do that.

1:17:08

But I will be restricted by the power.

1:17:11

Because we have that much hardware not.

1:17:13

I don't have that much of RAM, that much of GPU.

1:17:16

But we are just trying to see a small setup right now.

1:17:20

You know,

1:17:22

you know,

1:17:24

and

1:17:25

You know.

1:17:27

Thank you

1:17:57

Okay.

1:18:11

But at the end, but at the end of the process,

1:18:14

I will have both the models,

1:18:16

both the models that I have downloaded.

1:18:18

Or last May, once I've done this,

1:18:20

I can say something called Olamer list.

1:18:23

I can go and see something called Olamar list.

1:18:24

I can go and see something called Olamar list.

1:18:26

And just I'm Olamma list type

1:18:28

I can see the list of both the models

1:18:30

that I've downloaded, okay?

1:18:31

So the final command is Olamma list.

1:18:34

Okay, so people can do this.

1:18:36

So you can actually see,

1:18:38

whatever models you have downloaded in OLama,

1:18:41

locally, you can see the list of your models here up in.

1:18:44

So this one was a 397MB model

1:18:46

and this is the 8, 1.3GB model.

1:18:49

Okay, and now we will run one of the models

1:18:52

and we will do some basic prompting.

1:18:54

Whatever we were doing in the last session, you know,

1:18:56

we're getting instant answers.

1:19:00

Now you will get a real feel how these things look like

1:19:03

when you're doing in your own system.

1:19:04

Okay?

1:19:05

Yeah, Rajee, please go on.

1:19:06

Please go on.

1:19:07

What is your question?

1:19:07

Please.

1:19:12

Yeah, because it is a Chinese model, right?

1:19:17

Yeah, because it is a Chinese model, right?

1:19:21

Absolutely, absolutely.

1:19:23

See, the reason is because these Chinese models,

1:19:26

might have, what are language models?

1:19:28

Language models are basically, you know,

1:19:31

they are having a certain context about how things work,

1:19:34

the world and all that, right?

1:19:36

That's what large language models are, in a way, right?

1:19:39

All these language models are kind of based on that.

1:19:42

So the Deepseek model is already trained on lot of Chinese propaganda data.

1:19:47

So the inner knowledge of Deepseek is based on the Chinese propaganda data.

1:19:51

Imagine if a US government official is using Deepseek

1:19:54

and they're asking, okay, what happened in the world?

1:19:56

World Trade Center, whatever, you know.

1:19:58

So deep seek might actually give a response that, okay, it is controversial and maybe government

1:20:02

and all that, you know, had a hell, whatever.

1:20:04

So that's the thing.

1:20:05

That's the difference between using a Chinese model versus the US model.

1:20:08

So the Chinese, see, one part is the Chinese model is internally trained on majority of Chinese

1:20:13

specific data, right?

1:20:15

Whatever they are getting in their ecosystem.

1:20:18

That's the, yeah, probably Taiwan.

1:20:20

And this is a very, very good point, actually.

1:20:23

Very good point.

1:20:23

Now, you chat GPT to put you.

1:20:26

And see, this is again, a very good point.

1:20:28

You're here deep seek, we're just trying to try.

1:20:30

Right.

1:20:31

Deepseek's chat interface be there.

1:20:33

Deepseek's chat interface be here.

1:20:36

Okay, this is the chat.deepseek.com.

1:20:38

This has this is the chat.deepseek.com.

1:20:38

This is this is a chat interface also.

1:20:42

You can just go and ask a question about Taiwan to deep seek.

1:20:46

And you can ask a question about, you know, Taiwan to open air.

1:20:52

Now, both difference will go.

1:20:53

Because the language models are inherently trained differently based on how U.S.

1:20:59

East Taiwan versus how China sees Taiwan, based on the kind of data that they are grounded on.

1:21:04

Another very controversial issue is the status of Palestine.

1:21:08

There are many countries who officially Palestine, who recognize not.

1:21:13

But you'll be able to see some very interesting patterns that are coming out of this.

1:21:18

Or for that matter, even Iran.

1:21:20

You go and ask a question to deep seek about Iran, about the current.

1:21:23

U.S. Iran war and you go and ask the same question in chat, GPD.

1:21:27

You can't see.

1:21:29

I hope that answers, Raji for you.

1:21:32

Okay.

1:21:34

Now, moving on, everybody do Olama list.

1:21:37

And once you're done, we will run our very first,

1:21:41

you will run our very first interactive chat session.

1:21:45

Olama run, so two model we have now available.

1:21:49

Because we've done we've pulled and downloaded it.

1:21:51

Now we have the small model is, run to run it.

1:21:55

So that everybody in the class can do it.

1:21:58

Now, look, I've runed.

1:21:59

And as I've run it, class manager, sorry, I've done it.

1:22:02

Now, look, I've done.

1:22:03

Now, look, as I've got a little memory burned.

1:22:06

There can you see?

1:22:08

Yeah, you see?

1:22:08

Yeah, because there is hardly anything we are using.

1:22:12

So to see a noticeable increase, we have to have a bigger model.

1:22:14

But this one, that's why I said, everybody can do this in the class.

1:22:17

This is a very small model.

1:22:19

Okay, so all of you please run.

1:22:20

And the moment you say,

1:22:21

run, you will see this message. And here you can go and ask your questions.

1:22:28

Explain photosynthesis in two simple sentences for a class 8 student. If I hit enter,

1:22:34

you see here here print it was super fast. It was super fast. It was super fast you. Why was it super fast?

1:22:39

Because this is a very quick model. It is a very quick model. It is very quick model.

1:22:42

That's just super fast. If you want to see a slow response, we'll up to give them.

1:22:46

But that you don't do, because your system hang goes down. If you're not an, if you're on an A.m.

1:22:51

she don't do that. But yeah, this is so quick. So if you ask the question, what is the capital

1:22:55

of India? What is the capital of India? What is the capital of India?

1:23:03

Nelly. Simple. We can it's this last session-wala format. System message here.

1:23:08

User message is. Please tell me the sentiment, something like that, you know?

1:23:12

So please tell me the sentiment of the below review.

1:23:21

as positive or negative. Okay. And then I will say review. What is the review? The review is

1:23:33

I love the food. Okay. How quick it is? All right. Everyone's able to do it. Please try. Just want you to get a flavor of these two examples, all of you.

1:23:51

please try.

1:23:55

Download.

1:23:56

No problem. Take your time.

1:23:57

Take your time.

1:23:57

Download car. Run.

1:23:59

And just try a simple prompt.

1:24:01

I want you to see the response coming in your system.

1:24:05

Ah.

1:24:09

That's a little time lagging.

1:24:10

That's a little time lagging.

1:24:11

Allow it to.

1:24:13

Allow it to start, please.

1:24:21

Thank you.

1:24:51

Thank you.

1:25:21

Okay, okay.

1:25:25

Yeah, so this could be a different issue. I think.

1:25:30

Yeah, that is okay. That is okay. That is okay. Yeah, yeah. It says failed. Okay. But it's starting for you, Sanquita. Is it starting for you?

1:25:42

That's okay. See, that's okay. This is this is this is known. So I, part of the struggle is I wanted you to struggle.

1:25:48

Because we have our local system. Right. Things will get very.

1:25:51

smooth once I show you grog, so there's

1:25:53

something to do it.

1:25:54

We'll call

1:25:55

call and the answer

1:25:55

will say, this is, this is, this is,

1:25:58

because there are so many factors here.

1:26:00

You have your system

1:26:01

have, your system in, what is,

1:26:03

what software

1:26:03

hey, what

1:26:04

DG are, so

1:26:06

there. A lot of factors matter.

1:26:08

It's like installing any other software.

1:26:11

So that is, that is okay.

1:26:12

That is, I think that is part of the deal.

1:26:14

It's okay. It's okay. If it's

1:26:15

if it's not running perfectly, it's okay.

1:26:17

It's okay. We'll just follow along.

1:26:20

I wish our response is big is because because

1:26:21

you have not gone and controlled the prompt.

1:26:23

A prompt you just give

1:26:25

a good prompt. You're asking what is

1:26:27

the capital? And answer can be different.

1:26:30

Answer can be different. Because remember,

1:26:32

large language models are inherently

1:26:33

probability. I think

1:26:35

your question is more like, sir, you

1:26:37

you know, my answer is small.

1:26:39

My answer is small. My rather, why are you? Because remember

1:26:41

the same question, the same prompt

1:26:43

can give two different responses for the language

1:26:45

model. Right? So if I write a prompt and

1:26:49

if you write a prompt and if we both

1:26:51

use the same model. Even if we both

1:26:53

use the same model, the answers can be different

1:26:55

Abhishka. Please give this some noise.

1:26:59

That's okay. That's okay. You don't have to go and

1:27:01

ping this place. Okay? That's okay. Yeah.

1:27:04

Okay.

1:27:06

What is?

1:27:07

Kunal, I think, repeat

1:27:08

so it's not difficult

1:27:09

I'm sorry because I have to go through the whole

1:27:11

class again, again. So

1:27:13

what I can do is I can

1:27:15

quickly give you, okay,

1:27:17

Okay, alama, we're from from sure from from

1:27:19

how we're going to repeat

1:27:19

do you. So, first you download

1:27:23

broadly, Arshita is also helping. So number

1:27:25

one, you download. Okay, I'm

1:27:27

just, just 10 seconds. I think you can catch it.

1:27:30

You can catch it. I'm confident.

1:27:32

So, first, you have to download

1:27:33

you're download to, then you open a power shell,

1:27:38

power shell, Olama version,

1:27:40

then Olama pool. This is how you

1:27:42

take the model, okay? And after that, you go and do

1:27:45

Olama list. Olama list is how you go and see

1:27:47

the list is how you go and see the list of all the

1:27:48

models that are available. And finally, you go back and do Olama run.

1:27:53

Ola ma run off, you'll do, you'll do you are running that particular model.

1:27:58

Got it? And once you click on Olama Run,

1:28:00

you've got a point, and when you click on Olama run, you'll, you can't get a

1:28:02

and if you're just prompt here, you can't do normal prompting

1:28:04

can't, okay? I hope that clarifies for you.

1:28:18

Okay, very nice, very nice.

1:28:21

That is okay, that is okay.

1:28:23

And I'm telling you again, the same prompt can give different answers.

1:28:27

Probability thing is there, absolutely, okay?

1:28:29

Barabbat.

1:28:30

Because LLM is what?

1:28:31

The first thing, large language models is probabilistic.

1:28:34

You are looking at some input problem,

1:28:37

and based on that, you are trying to predict a response.

1:28:39

This is a deep learning model.

1:28:41

Behind the scenes, what is the LLM?

1:28:42

What is a large language model?

1:28:44

The large language model behind the scenes is basically a kind of a probabilistic,

1:28:48

engine. So the same problem, you're, see, we'll

1:28:51

we'll look at. We, we'll, same

1:28:52

same question, okay? Here, we'll

1:28:54

put it, we'll put it back, what is the capital of India?

1:28:56

We'll, we'll go. Now, look,

1:28:58

now, look, it's a little bit

1:28:59

kind of a little bit of way, look, here here

1:29:00

one line, right? Exactly, Ali is also reporting,

1:29:04

one line, now, look, me, look, me right? So the same

1:29:07

problem can give different answers. If you're

1:29:08

here there more came, okay?

1:29:10

Got it all of you? That's the intuition.

1:29:15

Okay, now, moving on?

1:29:17

Now moving on, let me just also show you another very interesting thing.

1:29:23

So here, a basic setup we've done,

1:29:26

Olama, local.

1:29:27

What is the benefit of this?

1:29:28

It is secure.

1:29:28

It is private.

1:29:30

Whatever prompts your writing, none of this is going to the internet.

1:29:33

And here is the best part.

1:29:34

Here is the best part, guys.

1:29:35

This runs without an internet connection.

1:29:39

This runs without an internet connection.

1:29:41

Abid to care, we are on a Zoom meeting, so we can't be internet ban not.

1:29:43

But if you even, after we end the class,

1:29:46

you have internet bunded,

1:29:48

you, you're not network to disconnect

1:29:49

go,

1:29:49

Olama will still run.

1:29:51

Because this is,

1:29:51

this model is right now

1:29:52

in your machine.

1:29:54

It is not like a chat GPT

1:29:55

or some other cloud provider,

1:29:57

where you have to

1:29:58

go to browser

1:29:58

go to, no,

1:30:00

you don't need any internet connection.

1:30:01

Okay, this is running

1:30:02

completely locally,

1:30:04

completely securely in your device.

1:30:06

And there is a term

1:30:06

that we use in the industry

1:30:08

called on-premise.

1:30:10

This is an on-premise model.

1:30:11

Exactly.

1:30:12

It holds the entire data

1:30:14

and all the parameters

1:30:15

within your system.

1:30:16

That's why it is secure. It is private.

1:30:19

So now what I want to do, just for the demo purpose,

1:30:22

yeah, you don't repeat much because this one will,

1:30:24

this one will be a massive one.

1:30:27

I know, so.

1:30:30

Abhhhhhhhhhhah, that's a very good question.

1:30:31

History, you mean, you can't,

1:30:33

but because this is completely under your control,

1:30:37

here history, way,

1:30:38

maintain, not.

1:30:40

Look, there's nothing

1:30:40

that's not that machine in the machine

1:30:41

is not.

1:30:42

PowerShell's all commands actually,

1:30:44

historically,

1:30:45

you can't really your OS level

1:30:47

may save but there are ways to get it out,

1:30:49

but there are ways to also remove it.

1:30:51

But that is the operating system level thing

1:30:53

that you need to get into.

1:30:54

To answer your question,

1:30:56

what history is saved

1:30:57

is, yes,

1:30:59

your system's every thing

1:31:00

save is saved. That is managed at an OS level.

1:31:03

Normal person cannot find it.

1:31:05

Like, Gemini, I'm chat history

1:31:06

here, that normal, anyone can't see that.

1:31:09

Normal a person cannot see that

1:31:10

because this will be at an OS level.

1:31:13

But yeah, if somebody wants to take an

1:31:14

go to the power cell level and they can figure out

1:31:16

what you call it. They can.

1:31:18

They can. You can also delete it.

1:31:21

There are ways to

1:31:22

store that.

1:31:25

Because you can, you know,

1:31:26

you know, you know,

1:31:28

storing the history is not only for, not just for

1:31:30

privacy.

1:31:31

One, privacy concern, that

1:31:32

that, sir, I've chated here, history could be stored

1:31:34

over. Second is

1:31:36

auditable. Auditing be important,

1:31:38

if, if, man, if you're

1:31:39

wrong, so who is responsible?

1:31:41

We need to go back and see, that,

1:31:42

that prompt what did you?

1:31:43

Just the case of it's a

1:31:44

the wrong answer

1:31:45

I'm a example.

1:31:47

Manu, you're using

1:31:48

a large language model

1:31:49

in a hospital setup.

1:31:50

Okay,

1:31:51

patient may

1:31:51

a question

1:31:52

the language model

1:31:53

is processing

1:31:54

and it answers,

1:31:55

it gives a response.

1:31:57

So patient asks the question,

1:31:58

the language model

1:31:59

will process,

1:31:59

and it will give a response.

1:32:01

So if you think

1:32:02

about that kind of a setup,

1:32:04

the patient asks the question

1:32:05

language model

1:32:05

process and gives a response.

1:32:07

If you look at that

1:32:08

particular kind of a setup,

1:32:12

if the LLM

1:32:13

gives a wrong answer.

1:32:15

Patient has a

1:32:16

question but

1:32:16

that model

1:32:17

has

1:32:17

the model

1:32:17

has

1:32:18

answered.

1:32:19

Like I

1:32:19

have

1:32:20

here

1:32:20

asked

1:32:20

what is the

1:32:20

capital of

1:32:21

New Delhi.

1:32:22

Or then

1:32:22

I'm

1:32:22

another

1:32:23

question

1:32:23

asked

1:32:23

that I'm

1:32:24

am having

1:32:24

fever.

1:32:26

I'm having

1:32:26

fever.

1:32:29

What kind

1:32:29

of

1:32:30

medications are

1:32:34

usually taken?

1:32:35

Okay.

1:32:36

So I

1:32:36

know I'm

1:32:37

I'm chatting

1:32:37

with a

1:32:38

I'm chatting to

1:32:38

a doctor

1:32:39

assistant.

1:32:40

I'm chatting

1:32:41

to a doctor

1:32:41

assistant.

1:32:42

So if I

1:32:43

if I

1:32:43

if I

1:32:43

So it is saying

1:32:45

that

1:32:46

is saying, you can also

1:32:49

see how slow it is.

1:32:50

You can also see how slow it is.

1:32:51

You can't

1:32:51

why these language

1:32:53

models are so slow

1:32:54

when you're running it locally.

1:32:55

So this

1:32:56

is wrong.

1:32:59

Auditability

1:32:59

for this history

1:33:00

maintain

1:33:00

is sure.

1:33:02

If you

1:33:02

if you're

1:33:02

asked,

1:33:03

you can't

1:33:05

go and

1:33:06

you have got to

1:33:06

look what

1:33:06

what

1:33:07

got done

1:33:07

what prompted

1:33:08

was to be

1:33:10

somebody has to be accountable.

1:33:11

So in

1:33:11

enterprise application

1:33:12

having the history is

1:33:13

very important.

1:33:13

history

1:33:14

is not that

1:33:15

we're

1:33:15

not that we're

1:33:16

not history

1:33:18

because of

1:33:18

auditability.

1:33:19

The company

1:33:20

genuinely

1:33:20

wants the

1:33:21

auditability

1:33:21

train that if

1:33:22

something goes wrong

1:33:23

if a customer

1:33:24

sues me

1:33:24

if a customer

1:33:25

if a

1:33:26

customer is a

1:33:26

wrong

1:33:27

then the customer

1:33:28

so

1:33:28

customer to legal

1:33:28

case

1:33:29

will be

1:33:29

how they say

1:33:30

how they say

1:33:30

what will be

1:33:30

what

1:33:32

will be what

1:33:33

what will the

1:33:33

what will the

1:33:34

court's and

1:33:34

investigators

1:33:34

look at

1:33:35

right,

1:33:35

got it?

1:33:36

So this is actually

1:33:36

a very

1:33:37

important thing to

1:33:37

keep in mind

1:33:38

Oh it was

1:33:42

history from

1:33:43

previous response

1:33:44

that we don't have to

1:33:45

that's a good

1:33:46

question

1:33:46

that's a good question.

1:33:47

Uh,

1:33:47

uh,

1:33:47

we'll manage

1:33:47

can't

1:33:48

manage

1:33:48

can't do that

1:33:49

we're

1:33:50

we're going

1:33:50

but this is

1:33:52

not the

1:33:52

exact chat interface

1:33:53

right,

1:33:53

this is just a

1:33:54

console.

1:33:55

So console

1:33:55

you're when

1:33:55

you're when

1:33:56

you're

1:33:56

so this is like

1:33:57

a single

1:33:58

turn

1:33:58

conversation,

1:34:00

single turn

1:34:00

conversation,

1:34:01

how you can't

1:34:02

we can't do

1:34:03

this is not the

1:34:04

best

1:34:05

place for it.

1:34:05

This is not the best

1:34:07

we're just

1:34:07

going forward

1:34:08

I will take you

1:34:09

to my

1:34:09

Jupiter

1:34:09

notebook.

1:34:10

So whatever you're

1:34:11

asking, it can be

1:34:12

done in the phone

1:34:12

absolutely.

1:34:13

you can have a history

1:34:15

key system, user,

1:34:17

uh,

1:34:18

like we

1:34:18

we've

1:34:18

last session in

1:34:19

the system message,

1:34:20

user message,

1:34:21

assistant response,

1:34:22

back

1:34:23

you've got

1:34:23

a user message

1:34:24

and then

1:34:25

what's

1:34:25

back in

1:34:26

the whole

1:34:27

context

1:34:27

next time you ask

1:34:28

another new

1:34:29

user message

1:34:30

that's after

1:34:30

response

1:34:31

had so all that

1:34:32

can be

1:34:32

minting.

1:34:34

Okay.

1:34:36

So I'll show you

1:34:36

one last

1:34:37

example so that

1:34:38

everyone's

1:34:39

clear.

1:34:39

I'll show you one last example.

1:34:39

So that everyone's clear.

1:34:39

I'll go back to the deep seek, the very first version model.

1:34:45

You don't have to do this, okay?

1:34:46

No need to do this one.

1:34:52

This is your deep seek R1 model

1:34:53

you can already start to see

1:34:55

how massive some of these models are.

1:34:57

4004GB.

1:34:58

This is,

1:34:58

but what we'll go

1:35:00

is this 9GB model.

1:35:03

This can we can you

1:35:03

can you

1:35:05

can show you.

1:35:05

This will be a small one.

1:35:08

So you don't have to do it.

1:35:09

You don't have to do it.

1:35:09

You don't have to do it.

1:35:09

You don't this one, if you want to load a 9GB model, it will straight away use

1:35:13

8GB of RAM.

1:35:14

Straightaway 9GB of RAM gone.

1:35:16

And if you're on Windows, if some of you are on 8GB machine,

1:35:19

so you'll instantly crash.

1:35:21

Zoon, boom, all can't do that.

1:35:23

Don't try to run this.

1:35:24

This is just something I'm trying to do in my system, just to show you.

1:35:28

So how do you exit?

1:35:29

So now here

1:35:30

prompt window

1:35:30

if you're from you can just click on escape.

1:35:34

You can just click on Control C.

1:35:36

You can just click on Control C.

1:35:36

You can just click on Control D.

1:35:39

click on Control D.

1:35:40

Okay?

1:35:41

Control D you can click C-T-R-L-D.

1:35:47

So actually, Ankit,

1:35:48

if I have to answer you very intuitively,

1:35:51

Ankit's question is,

1:35:52

sir, this billion parameters

1:35:54

are what is this?

1:35:55

What is the meaning of this?

1:35:56

Like you're a deep seek model

1:35:58

is a model.

1:35:59

Deepseek was, is basically a model

1:36:01

that is by the deep seek Chinese company.

1:36:04

And a very, very popular model.

1:36:06

Globally, this viral trend

1:36:08

was last year.

1:36:09

20, 25, January.

1:36:10

It was a viral trend last year.

1:36:12

It's a very, very popular model.

1:36:15

And if you take a look at it,

1:36:16

here there are many versions there.

1:36:18

You have a 1.5 billion model,

1:36:19

7 billion model, 8 billion model,

1:36:22

14 billion model,

1:36:23

32 billion model,

1:36:24

70 billion model.

1:36:25

So all these are different, different sizes

1:36:29

of the deep seek model.

1:36:30

One is deep seek model and the deep seek model

1:36:33

comes in different, different sizes.

1:36:35

It is a 1.5 billion size.

1:36:38

It is a 1.5 billion size.

1:36:39

There is a 8 billion size.

1:36:40

There is a 14 billion signs.

1:36:42

Or I'm trying to explain this intuitively.

1:36:45

It is kind of telling you the power and the memory of the model.

1:36:48

But the model make it kind of context.

1:36:50

How good is it?

1:36:51

How much information does it have?

1:36:53

So if you tell 671 billion parameters,

1:36:56

this is massive.

1:36:57

I mean this model is trained on a lot of data.

1:36:59

Yeah, exactly.

1:37:00

I think what you are saying,

1:37:01

features and trading data.

1:37:02

Exactly.

1:37:03

It's kind of like that.

1:37:04

I mean, this model is trained on a tremendous amount of data

1:37:06

and it has a tremendous amount of knowledge about the world.

1:37:09

Whereas this one is having a very limited view of the world.

1:37:13

Think of it that way.

1:37:14

If you asked,

1:37:15

if you know, India's capital is, Delhi,

1:37:16

this is all know.

1:37:18

You know, if you can't be asked,

1:37:19

if you know,

1:37:19

and all of them, all know,

1:37:21

okay?

1:37:22

So, this answer will give us.

1:37:24

But if you asked,

1:37:26

that you, please explain to me,

1:37:27

you know,

1:37:28

what is,

1:37:29

maybe you take a very core

1:37:31

generative AI topic,

1:37:32

which is very, very advanced.

1:37:34

You have asked,

1:37:35

please, please, please explain.

1:37:37

So that you'll not be able to.

1:37:39

you want to just follow through the chat.

1:37:45

I have already pinged these things.

1:37:47

I've already pinged these things.

1:37:48

You're just, just, just try it out.

1:37:53

A bit just go back, go up the chat.

1:37:54

I just now pinged to one of the folks.

1:37:58

Yeah.

1:38:00

You've done Olamapul do both type

1:38:01

over.

1:38:03

Olamapul will only be once, okay?

1:38:05

Now, moving on, let me use the next one.

1:38:08

And this one,

1:38:09

what I will do?

1:38:13

I will go ahead and

1:38:15

say Olama pool

1:38:16

deep seek R1 14 billion.

1:38:19

Okay, Olama pool, deep seek R1 14 billion.

1:38:22

And I will

1:38:22

download this model. First, I will

1:38:25

download this model. Don't have to do this.

1:38:27

This one, you guys, don't have to do it. This one, you guys don't have to do.

1:38:28

Okay, no problem, you can. Let me ping you. Let me think you. Don't worry.

1:38:31

Don't worry. Let me ping you. This is time

1:38:32

will be a little. No worries. You can do it.

1:38:35

So first, you, allama version

1:38:36

version check.

1:38:37

Okay.

1:38:38

Next, Olama Pursion.

1:38:39

pull. When you say Olama pull, Olama pull is the command to go and pull and download that

1:38:44

particular language model. And finally, you can do Ollama run. And Olama run is basically the command

1:38:50

to run the language model. Simple. So pull is to download the model and run is to run the model.

1:38:55

But then you're a model. And just say you run here, this prompt window will be. Here on the

1:39:00

prompt, you'll, you have answers to get. That's the thing. The best part is all this you are doing

1:39:04

in your own machine. Okay. So this is the final demo that I want to.

1:39:09

to show you. Then we go to some code examples. Where to see all the models.

1:39:20

Models are available in the directory where you have saved it. If you want to test, see the list of

1:39:26

the models up, you can write the command called Olama list. Olam list.

1:39:31

Olama list is what you can do. Okay.

1:39:40

Ah, that one, that one you can do in Olama.com.

1:39:43

This I've seen right. I already talked you through it, right?

1:39:46

This I already discussed.

1:39:48

Olama.com, you go.

1:39:49

Here up in models make click.

1:39:51

If you want to see the list of all the models, you can go to this particular website.

1:39:55

You can go to this particular website.

1:39:56

You can see.

1:39:57

All these models you can search, popular models,

1:40:00

which are the most popular model subjects.

1:40:01

Okay, but then be mindful of the size of the model.

1:40:06

Okay.

1:40:08

So, let is it take a while.

1:40:09

Let me download this.

1:40:31

So most importantly, a small model, whatever we used here, a small model was efficient and lightweight.

1:40:41

It could quickly do things.

1:40:42

A large model is demanding heavy.

1:40:45

So this is a very good example of a large model.

1:40:47

So it will be very, very slow to run.

1:40:50

Or that is exactly what I wanted to show you.

1:40:52

It will be very powerful.

1:40:54

The questions of answers, it will be accurately they are, but we'll be very, very slow to run.

1:40:58

Because it is a bigger model, 9gb in size.

1:41:01

So it is always a trade-off.

1:41:04

If you want a more accurate model, remember that model will generally take, you know, more time to execute.

1:41:17

Every time you will have to go back and kind of ask these kinds of questions.

1:41:23

You have to look at that trade-off, basically.

1:41:25

If you can get something done with the simple model, why not?

1:41:31

And I think there's a very nice analogy that I wanted to bring up.

1:41:39

There is a very nice analogy that you can, that you can look at with respect to how to think through this in a better way.

1:42:01

So these are three different types of categories we talked about.

1:42:05

Model weights.

1:42:07

Ultra light weight, this is the one that we are using.

1:42:10

Everybody in the class can run this model.

1:42:12

3-0 or 400 MB's model.

1:42:14

All made.

1:42:15

Extremely fast, minimal RAM requirement.

1:42:18

But limited multitask reasoning.

1:42:22

High hallucination risk.

1:42:24

That means it is a, there is a very high high chance that this model might give you wrong answers.

1:42:30

there is a very high chance the model might give you wrong answers.

1:42:35

So this is the problem with this ultra lightweight model.

1:42:41

This is a small or medium model.

1:42:45

And what you're seeing here is basically a heavy weight model.

1:42:53

Heavy weight model, which I'm now up to dikhaer, heavy weight model is basically the one where it is bigger, it is bigger.

1:43:00

But the most important thing is, you know, as I always like to say, how do you choose?

1:43:07

You see, here I'm trying to use a, I'm trying to download a Lama, a deep seek 14 billion parameter model.

1:43:15

So, you'll ask, sir, why do you?

1:43:18

Okay.

1:43:18

So I'm just keeping all the things with me.

1:43:21

Now, depending on the requirement, I will choose which model I have to use.

1:43:25

Other basic task, let's say I have to, let's say I have to, I want the model to answer,

1:43:29

that, what is the capital of India?

1:43:32

So capital of India answer to, can we have this?

1:43:36

Capital to say, anyone will say, he be able to, he'll be able to.

1:43:38

But it's the right right, right? If you look at the coin model, if I ask, what is the capital

1:43:42

of India? It was giving the correct answer. I don't need such a powerful model to answer what is

1:43:46

the capital of India. Okay. Sainath, you can coordinate with Arshita. Arshita will guide you with

1:43:51

the installation. We have already gone through these things. I think you can follow along.

1:43:55

I think you can follow along. Just follow along. So this is very easy. And I think after the

1:43:59

plus you can try again. Otherwise, if you again try to do the setup right now, so you might

1:44:04

miss out. So we are almost completing the Olama part now. So last five minute

1:44:09

so you just follow along this part. And then the coding part you can do together. We will do together.

1:44:16

So this part just ignored for now. Okay. Yeah.

1:44:24

Billion stands for the number of parameters, Swarthi.

1:44:29

So what is this billion? The billion stands for the number of parameters. How many parameters the model has?

1:44:35

That means, how good is it? Okay. So if a model has, let's say, 70 billion parameters

1:44:42

compared to 0.5 billion parameters. So this model, this on this

1:44:48

parameters jada. Parameders jada is what? Parameders is what? What? What? It's got knowledge

1:44:54

is a lot. Think of it that way. So this is all coming from machine learning.

1:44:59

right? We have got a tremendous amount of internet scale text data.

1:45:03

Internet for he's available. And based on that internet scale text data, we have managed to

1:45:09

train this model. So that's the way to look at it overall. So more the number of parameters,

1:45:16

more the knowledge, more the information, more the training. That's why more powerful.

1:45:22

But slower. It is like a truck. It took a lot of energy and lot of resources, a lot of money to build

1:45:29

the truck. Heavy. It's heavy. It's heavy. Having a lot of capacity and all that.

1:45:32

They can, it is slow, right? It is slow. Think of it that way. Okay. Okay. Ah. Absolutely.

1:45:41

People should prefer local elements. Subras, you answered it perfectly. People should prefer local

1:45:45

in lips if they're looking for privacy. We are almost done. One minute more left.

1:45:52

And once you start doing it, I think one of you are answering, one of you are mentioning. Your fan will start, fan speed in the laptop will start to

1:45:59

increased. That's how it's been using

1:46:00

because these models are actually very, very, very, very compute-intensive in practice.

1:46:29

Thank you.

1:46:59

Okay.

1:47:06

Thank you.

1:47:09

Okay.

1:47:29

Thank you.

1:47:59

It takes a while to load. I think the final thing is done. I think the final thing is done. So you can see my deep seek model is right now loaded in. And what I've got to show my deep seek model is right now loaded in. And what I wanted to show you the last one is my this thing. You can see right now. You can see right now I've got around 16, uh,

1:48:29

gp of RAM that is active. And look at this, look at this very interesting thing that will happen.

1:48:33

Now we'll what we'll do? I will just run the command, which is Olama, run, deep see.

1:48:40

Now we're what we're going to Olamma, run, deep C. Because see, this is just not just downloaded.

1:48:47

Here here there's only download here. But we've been it still load not yet, application not run

1:48:52

made it. The moment I run this code, you will start to see, you will start to see the amount of utilization, how it will increase.

1:48:59

look at 16 gb.

1:49:00

This is the more powerful model. The moment I run this, it's the more powerful model.

1:49:05

The moment I run this, you start to see my task manager.

1:49:09

Start to see the increase.

1:49:10

Look at this.

1:49:12

And at this point in time, if you're, if you, you might go out of RAM also, if you don't have enough

1:49:17

capacity, your system will end up.

1:49:20

So here here, from 16 to like 15 to go.

1:49:23

Look, the first 16th was 16th, now 25 to go.

1:49:25

Now GB used used.

1:49:28

Okay?

1:49:29

My model is now loaded. My computer is able to load that model.

1:49:33

And now I will go and ask the same kind of questions.

1:49:36

And you will be able to also see, very interesting.

1:49:40

You'll be able to also see that the system will, you know, up herepe,

1:49:43

see that processor speed, CPU, you can see. Very interesting.

1:49:47

The patterns and the clock cycles, you can all see that.

1:49:49

And now, look, when I ask the question, you will see how slowly it is responding.

1:49:53

Can you see? Look at this. Very interesting. Look at the speed.

1:49:57

It is very slow in response.

1:49:59

very slow.

1:50:03

Actually, deep seek is a reasoning model.

1:50:05

It is sinking before answering.

1:50:06

But it is not as super fast as what we were doing before.

1:50:09

This is a bigger model. It's a bigger model.

1:50:12

You can already start to see my CPU is already taking more thing.

1:50:17

Okay? Kaffy processing is a lot of cycles are getting used.

1:50:21

And this is just to, again, show you the compute and other things.

1:50:25

And you, you, if you'll go ahead, the system fullerum will get up.

1:50:29

So there's a lot of compute that is happening.

1:50:31

So local LLMs, they look cool.

1:50:33

So local, it's, it's a lot to listen to it.

1:50:35

But you'll, you'll know, you'll see, you'll, you'll see,

1:50:38

that you know, you can't get, that they've got,

1:50:40

that they're thinking over there. And see, how much time it is taking to generate the tokens.

1:50:46

Right? Tokens are basically those unique words, right?

1:50:50

You can see how much.

1:50:51

So the first model was it so fast. But this model is powerful.

1:50:55

Yes, it is powerful.

1:50:56

It will give you answers to questions in a better way.

1:50:59

But it will basically, like, it will be very slow.

1:51:04

And that's the reason why it is so costly.

1:51:07

So unless you have a very good hardware, unless you have a very powerful system,

1:51:11

which clouds and all, that's available, so like, yeah.

1:51:29

Yeah, that's a good question.

1:51:41

NPU is basically an Intel's a new one is that stands for, uh, uh, uh, that's, you're, that's a,

1:51:48

that's a, you are, basically, uh, that's, that, you're, basically.

1:51:59

It's a kind of a processing unit only.

1:52:10

It stands for neural processing unit.

1:52:12

They use, in case you're curious.

1:52:15

So this is a very new processor.

1:52:16

I think I have some Ultra 7, I think.

1:52:18

This is an ultra series in.

1:52:20

So they have a dedicated unit built into newer Intel processors.

1:52:23

So they are basically using AI to run different types of workloads.

1:52:28

Okay?

1:52:29

So here ho go and what I want to do is, uh, I mean, uh, you can also go back and remove a model.

1:52:36

So, so our, like, uh, lot of RAM will get utilized.

1:52:39

So what I will do is I'll quickly close Olam and I will quickly close the application.

1:52:44

And let's start on with the rest of the flow.

1:52:47

So all this was basically to talk about local models.

1:52:51

Now we will be accessing cloud models through an API key.

1:52:56

And for this part of my demo, I want everybody.

1:52:59

to go to this website called GROC.

1:53:02

Okay, everybody go to GROC.

1:53:04

So GROC in GROC we've said last time, right?

1:53:07

All of you were on GROC last time, last class.

1:53:10

You were able to write, right?

1:53:13

So this is what I showed you last time, console.org.

1:53:16

Today, we will be doing these demos in a programmatic way using API.

1:53:20

Only difference is,

1:53:21

today we're on this demos in Python.

1:53:24

Okay?

1:53:24

The same demos, we will be doing in Python.

1:53:26

So we are basically trying to see two flavors in the class.

1:53:29

Flavor number one, the local LLMs came.

1:53:31

We've got Olama, Olama to platform installed here.

1:53:34

We learned how to download the different, different models locally on our system.

1:53:39

Okay, and we were able to get that flavor.

1:53:41

And this is the other flavor we are trying to learn.

1:53:44

How we can use GROC, where all these models are already available.

1:53:47

This is your cloud, this your cloud kitchen.

1:53:50

You have to do you need, you, you want to order it, you, you'll get to download it.

1:53:54

You don't have to download it.

1:53:54

You just call using an API key and you will get an answer.

1:53:57

API used to you, you know, you have a basic idea.

1:54:02

We will once again see a lot of coding with respect to that.

1:54:05

All I want you to do right now is you please go to API key and you can click on create new API key.

1:54:11

And all of you can just go ahead and create a new API key.

1:54:14

That's all that you can do right now.

1:54:18

So go to console GROC.

1:54:21

You can go to console GROC and you can please create an API key, all of you.

1:54:27

Click on Create API key.

1:54:31

Give the name of the API key.

1:54:34

You can give no expiration.

1:54:36

Click on Submit.

1:54:37

If you submit, then you'll see if you can be able to make sure, this part is very important, guys.

1:54:42

Make sure all of you copy that API key.

1:54:45

That screen's not go to it.

1:54:46

It's going to, because if you go back from once you go to back from back.

1:54:49

You have to make sure you create the API key and whatever API gets created, please copy that API key.

1:54:55

it's copy.

1:54:56

Okay?

1:55:04

And parallelly, once you're done with this.

1:55:08

You guys can also parallelly go back to the 22nd May folder.

1:55:12

Today's session is.

1:55:12

As usual, I'm uploading all the class notes for the respective sessions.

1:55:16

Today's session is, we've made class notes.

1:55:18

Jupiter notebook has already uploaded.

1:55:21

Please go to that class notes file and will open to that notebook.

1:55:23

Okay, so.

1:55:25

Two things do, API key to make it, copy and copy it in a notepad in safe.

1:55:28

Okay, simple, a note pad in save.

1:55:30

The other, please open up the class notes file.

1:55:33

The class notes notebook.

1:55:37

Excuse me.

1:55:39

Please open up the class notes notebook.

1:55:47

So, Grock, you will have a lot of fun because this may there's

1:55:49

a lot of jamela need.

1:55:50

People were reporting, sir, error are, here, this is the system heat-hoeing.

1:55:54

So this is the best.

1:55:55

part about the cloud APIs, right?

1:55:57

The cost might be a little more.

1:55:59

This is a free tier.

1:56:00

We are using a free account right now.

1:56:01

Costing is definitely very high for these things.

1:56:04

But yeah, you will have a lot of fun.

1:56:07

And I will show you the relationship with other API providers also shortly.

1:56:12

Okay.

1:56:12

So once everybody has done these two things, please let me know.

1:56:18

Okay.

1:56:19

API key, create over.

1:56:22

After copy and noteper in noteper save kia.

1:56:24

And second.

1:56:25

you are all in the class notes file.

1:56:32

This is a critical step.

1:56:34

So before I talk about that critical step,

1:56:36

it's a little new thing that you have not seen.

1:56:40

So we will see that before I take you to that critical step in the brand zone.

1:56:45

I want to make sure everybody has a setup ready.

1:56:48

All set up is okay.

1:56:49

I mean, you have made it in notepad in the key,

1:56:52

or you are in collaboration right now.

1:56:54

You are seeing the exact same.

1:56:55

same screen that I am seeing right now.

1:56:59

Okay, everybody let me know.

1:57:01

Warnit has confirmed others.

1:57:05

Everybody has done right.

1:57:06

Please do, please do respond, guys.

1:57:09

So this will help me to track people are able to do it.

1:57:16

So this is totally different from olama.

1:57:18

Olama is over done with.

1:57:19

In case some of you, if you have missed Olama, don't worry.

1:57:22

This say Olamma's no other than any.

1:57:23

That discussion has finished.

1:57:25

So this is completely new we are doing.

1:57:28

So Kunal, even for you, I think you can,

1:57:30

you can carry on from here.

1:57:31

Tika Piaihani, say,

1:57:33

you can, no, not Kuna, I think sign out.

1:57:36

Sign out once you are, right, so you're asking.

1:57:38

You can, you can follow from here.

1:57:43

Done, others also please confirm.

1:57:45

I've only got four responses.

1:57:55

I got kicked out of Zoom Plus.

1:57:58

Who's the kick out of you?

1:58:01

I don't know.

1:58:04

Okay, you were able to catch up?

1:58:06

Chalo, okay, okay, okay, okay.

1:58:10

I think you can talk to Arshita.

1:58:12

Arshita, I mean, she can help you get admitted.

1:58:15

Maybe, yeah, just, just ping ushita separately.

1:58:19

And she will help you join the meeting.

1:58:21

Ali, just ping her separately.

1:58:24

Okay.

1:58:25

Okay, done, everybody?

1:58:29

Now coming to the very important part, very important part,

1:58:33

click on the key, click on the Collab Secrets, okay?

1:58:36

So the API key we've created in GROC in GROC

1:58:39

in this kind of a kind of type of password

1:58:41

is, okay, guys, this kind of a kind of a type of password

1:58:43

so you can use this password to connect to all the GROC models,

1:58:48

programmatically.

1:58:49

Now we have our Jupiter notebook

1:58:51

from GROC models programatically access

1:58:54

do this. Okay, if you remember in the, what's that?

1:59:00

Yeah. So if you, if you, if you, if you go and remember in the last session, I told you that

1:59:07

javid you have here on system message, user message as you're like to look. All our class,

1:59:10

we saw this in a nice way, right?

1:59:12

But you, you look, this one section we hide kept there. But in the moment you click on view

1:59:17

code, the moment you click on view code, you'll be able to sit up Python code. So whatever

1:59:22

we were doing here, this is all the same thing.

1:59:24

the code in part that we have seen. Very simple.

1:59:28

Code in the code in there. System message, you're a, you're a hospital assistant.

1:59:35

This is all that we will see now. Same exercises we will do here.

1:59:38

Okay? What, what demo we did? What demo? Did it? What demo? Tell me? This demo? This

1:59:43

message? This is this. Okay? Let's see. There's a system message. And what is the user message? And what is the

1:59:50

user message is nothing but the medical notes?

1:59:54

user message? Simple. You look here here

1:59:56

how populate it. That's it. This is all that we will do in Python in our Google,

2:0:02

Jupita notebook. So we will define system message. We will define user message. And we will

2:0:06

simply call Brockclined.completions create. And we'll

2:0:11

call this model to call this. This model can't call

2:0:13

because we don't have it downloaded locally. Now, this is Olama not. This is

2:0:18

something other. Because this is the 70 billion parameter model. It's a massive model.

2:0:21

Now here in 10 billion, we have it. You can imagine 70 billion I don't have, right? How do I access this? Well, the best part is GROC has it. So GROC is that particular cloud kitchen set up that we discussed. So GROC is basically this. This is your GROC is. So GROC to GROC to GROC to

2:0:42

GROC to GROC can't this model available and we will simply access this model from GROC using an API key.

2:0:48

This is the setup to look at. That's the intuition.

2:0:51

So let's what you will do? Go back to the notebook again,

2:0:57

from the first. Please click on the key button.

2:1:00

Click on the secrets button.

2:1:02

And here here here I have a lot of other secrets. You can ignore this.

2:1:09

For you, what you require is this.

2:1:11

This is your, this. This is your key's name.

2:1:16

Okay. And here here you, you know, you have a lot of other secrets. You can ignore this.

2:1:20

key of value is whatever you have copied from your notepad.

2:1:23

So whatever that GROF API key that you have that you guys have right now saved in your

2:1:28

notepad, that open

2:1:29

and here here here in Secrets in here, click on Add New Secret.

2:1:34

Click on Add New Secret.

2:1:35

Name will be GROP API key.

2:1:38

Name will be GROP underscore API underscore key.

2:1:41

And value will be you please paste whatever you didn't collared.

2:1:45

Sorry, whatever you have saved in your notepad.

2:1:47

Notepag in the job as you please go and paste that.

2:1:52

That's it.

2:2:17

Where do I just for secret for secrets. I just explained that I just explained that.

2:2:47

Sanga, this is what you have to do.

2:2:49

Just go and click on Add New Secret.

2:2:53

Click on the key button.

2:2:55

In Collap, can you see there's a key button?

2:2:58

This key button is what contains the secrets.

2:3:06

Okay, so please click on the key button.

2:3:09

And once you click on the key,

2:3:12

you please click on add new secret.

2:3:17

And once you do that, you please type GROC underscore API underscore key.

2:3:23

This your name. First, you have the name.

2:3:25

It is just like a variable name, right?

2:3:28

So this is just like a variable name.

2:3:29

It's a variable can name.

2:3:30

I can push be desksed to, okay.

2:3:31

But for simplicity, please give the name as GROF underscore API underscore key.

2:3:36

This must be the same name, please.

2:3:38

And the value will be the value, the actual API key value that you guys have saved on notepad.

2:3:47

the value will be the actual API key value that you guys have saved on notepad.

2:3:54

You have your notepad in the notepad in the API.

2:4:17

Okay, Sanjita, let me know if it is done.

2:4:29

No, no, you don't have to do anything, nothing.

2:4:32

Nothing is required.

2:4:33

My name, Abhshan, no.

2:4:35

Not required, not required.

2:4:41

Okay, that's it.

2:4:43

And once you're done, you will actually see this entry will be created.

2:4:46

GROP.

2:4:47

key and its value here here.

2:4:49

Whatever value you have, you'll, you'll, you'll, you're going.

2:4:51

This your GROC API key will be, and here up your value will go.

2:4:54

GSC underscore something.

2:4:56

Okay, you're here here here here, it's from start with, okay?

2:4:58

If you're api keys in go, your API key, be GASK to start with something like that.

2:5:03

So it will be like GROC API key, and this your value will.

2:5:06

So this is something everybody should do.

2:5:08

Baki, all ignore.

2:5:09

Only I want everybody to have this API key created.

2:5:12

That's it, in secret.

2:5:14

Okay?

2:5:14

Okay. Now once this is done, once this is done, now we will run the code.

2:5:24

Go back to the notebook.

2:5:31

And then we execute khani.

2:5:37

So first I will, first initially I've got all these commented lines, which I will leave out right now.

2:5:41

And this is the most important part of the code.

2:5:44

We are installing GROC, we're importing GROC,

2:5:48

we are taking the API key that we have just now set.

2:5:52

See, when I say user did not get API key,

2:5:54

that we are basically getting that API key.

2:5:56

Whatever API key I set here, we are fetching that API key.

2:6:02

Client equal to GROP, so basically we're this code copy paste.

2:6:06

I'm just trying to explain to you, but all we are doing is we are simply copying and pasting this code.

2:6:10

That's it.

2:6:10

That's it.

2:6:10

This is the client GROC here.

2:6:12

Client chat completions create.

2:6:13

System, this user here.

2:6:14

That's it.

2:6:16

So client equal to Brock, done, code executed.

2:6:20

Model name equal to Lama 3.3 versatile.

2:6:23

That is the name of the model I will use.

2:6:24

You can use any cloud in these are models.

2:6:27

You can choose can.

2:6:28

I am choosing this one.

2:6:30

Run.

2:6:31

And this your prompt structure was.

2:6:33

This story, we've seen in last class in the last class I already told you.

2:6:35

There is nothing new we are seeing today.

2:6:37

Same story.

2:6:38

We're just looking at the implementation.

2:6:40

System message, medical notes one thing.

2:6:44

We've seen the last time.

2:6:45

User input in medical notes.

2:6:47

And this is your client chat completions created.

2:6:51

Okay, this is the template code that we are seen.

2:6:54

Client dot chat completions create your function.

2:6:57

Which we have grog from, this is the same website where I have copied it from.

2:7:02

Messages, role system, system message and roll user user message.

2:7:08

Run the code and you can see the response.

2:7:10

So this is the part until which I want to ensure every.

2:7:14

is able to see the response.

2:7:15

And you'll be able to see the answer is super fast.

2:7:18

No more waiting, no more.

2:7:19

And it's in the 70 billion parameter model.

2:7:21

Can you believe it?

2:7:22

I was running only a 9 billion parameter deep seek and it was taking like what forever in my hardware.

2:7:27

Can you believe it?

2:7:28

This is 70 billion parameter model and the results are instant.

2:7:31

Fixer run.

2:7:32

Now they go run over.

2:7:33

Instant results.

2:7:35

Less than a second.

2:7:36

You can imagine, you can already start to imagine how powerful this GROC server is.

2:7:42

Compared to downloading it locally, how powerful this GROC server is.

2:7:42

Compared to downloading it locally, how power.

2:7:44

powerful this is actually.

2:7:46

In fact, ROC is one of the fastest inference platforms out there.

2:7:49

People, I will pause for a minute.

2:7:51

Let me know if all if you're able to execute.

2:7:53

In fact, we can take a short break also.

2:7:55

We missed the break for the class.

2:7:56

Let's take a five minutes break here.

2:7:58

You guys can in the meantime ensure you run the code and you see a small tick mark here.

2:8:04

Any mistakes, please ensure that your Brock API is created correctly.

2:8:08

All these things are done correctly.

2:8:10

The end result I'm expecting is a tick mark here and that you're able to see the result.

2:8:14

here. That's it. Only until here. The rest we will discuss. Okay. So this is ensuring

2:8:18

that you're able to call the GROC API. You're able to call a cloud model and you're able to get

2:8:23

a result. Okay. So let's take our break also in the meantime. I'll see you back in five minutes.

2:8:30

And you can, you guys can utilize this time out to, uh, to, to make sure your code is run.

2:8:44

Thank you.

2:9:14

Thank you.

2:9:44

Thank you.

2:10:14

Thank you.

2:10:44

Thank you.

2:11:14

Thank you.

2:11:44

Thank you.

2:12:14

Thank you

2:12:44

Thank you

2:13:14

Thank you

2:13:44

Thank you

2:14:14

Okay,

2:14:17

all,

2:14:18

all of it's back, all of all if you're back from the break all of the break, all of you're able to execute it.

2:14:32

All of you are able to execute it until here, let me know,

2:14:35

Rangel has message DS.

2:14:37

Others, please confirm.

2:14:38

Until you are you able to run.

2:14:41

If you're able to that this is the first and this is the first and this is the first and this is

2:14:44

going to be an important setup because this means you're able to call the GROC API

2:14:49

and you're able to get the results.

2:14:51

Super fast.

2:14:52

No hassles, no local install, nothing.

2:14:54

But that's the objective today.

2:14:56

I wanted to show you both the setups today.

2:14:58

The two setups of the setups of these things.

2:15:00

Code, both of the same.

2:15:01

We have local code to be same.

2:15:03

Now, local we've installed and we were running it in the power shell.

2:15:07

But you can you can code in Python, we can do that

2:15:09

we can't.

2:15:10

We can't.

2:15:11

We are using the cloud.

2:15:13

We were using the cloud.

2:15:14

The models are already available in GROC.

2:15:17

We were simply connecting to GROC using an API key.

2:15:20

A password type of a key, we were getting access to all the models that are there on GROC.

2:15:26

That's in the servers.

2:15:28

That's it.

2:15:29

So all the processing is happening here.

2:15:33

There's all the processing is happening here.

2:15:34

Which is why you can be on a very, very cheap machine.

2:15:38

You have a 4GP RAM.

2:15:40

You can run it.

2:15:41

You can run it.

2:15:42

You can't do it.

2:15:43

Processing no.

2:15:44

You're just sending a prompt.

2:15:46

That prompt GROC to gop to GROC to process it.

2:15:49

You're responsible.

2:15:50

So that is the best part about this is in the cloud model.

2:15:53

And this is the setup we will use all through the sessions here in general.

2:15:57

Because this will be quick, it will be super fast, and we will not like...

2:16:01

But it is important to be aware of OLAMA.

2:16:03

So OLAMA was more of an awareness class today.

2:16:06

But going forward, we're like API with this access to.

2:16:09

So that we are able to actually get things done.

2:16:11

It is very, very good.

2:16:12

very good. It's very, very fast.

2:16:14

Okay.

2:16:16

Others, come on, guys. Show of hands.

2:16:18

People have done.

2:16:20

Ah.

2:16:24

Okay, okay.

2:16:25

Okay, okay.

2:16:26

Okay.

2:16:27

Others are all done.

2:16:28

Everybody.

2:16:29

Let me know. Please ping.

2:16:30

Yes.

2:16:31

Done.

2:16:32

Everybody who are done.

2:16:33

Please let me know.

2:16:34

No, Sankitha is trying, okay.

2:16:36

Is it? Okay.

2:16:37

Fine.

2:16:38

Others.

2:16:39

So done.

2:16:41

Okay, good.

2:16:42

Okay, thank you, Adich.

2:16:50

Others.

2:16:52

Come on, guys.

2:16:53

There are 25 people.

2:16:55

I'm looking to see everybody answered.

2:16:57

Because this is all in the class today.

2:17:00

So we want to make sure everybody is able to run.

2:17:03

Okay, Ali is good.

2:17:05

Fine.

2:17:06

And you can see that when you guys were installing it,

2:17:09

there are these.

2:17:11

This is install here, it was making,

2:17:13

but here nothing.

2:17:14

That's the best thing about using a cloud provider.

2:17:16

You're just making a call

2:17:17

and all the processing is happening there,

2:17:19

you're getting the response.

2:17:21

This is the chosen way of doing things.

2:17:23

So, the run.

2:17:29

Run, you're running the cell.

2:17:32

This is just you're just executing

2:17:34

up from.

2:17:36

Just the code is.

2:17:37

Just the code is.

2:17:38

Nothing to change in the code.

2:17:39

You have a notebook.

2:17:41

You're able to see the notebook.

2:17:43

You're able to see the notebook.

2:17:45

You're just just here to execute here.

2:17:47

just here to execute.

2:17:48

That's it.

2:17:49

Only execute until here, Sangeka.

2:17:51

Just here to execute.

2:17:53

Take mark and you will be able to see this results.

2:17:57

But very important, your Brock API key must be added.

2:18:00

Okay? This must be added.

2:18:02

If you're done this part, then this is easy, right?

2:18:04

You just have to execute the sense until here.

2:18:07

And the most important part of the code is this.

2:18:09

client.shad completions.

2:18:11

Okay?

2:18:12

Model equal to model name.

2:18:14

This is a variable that we have you

2:18:15

have before initialized here.

2:18:17

You can give any variable name.

2:18:20

And messages is basically where we write the whole prompt.

2:18:23

The prompt that we have,

2:18:25

system message, user message,

2:18:27

the whole prompt that we have.

2:18:28

This is where we have the message is.

2:18:30

The system, role system,

2:18:32

this is the system message string

2:18:34

and role user, we have the whole user message string.

2:18:37

This is the whole system message string.

2:18:38

This is the whole system message string.

2:18:39

which is the whole user message stream.

2:18:41

And this is how we end up getting the response.

2:18:43

Okay.

2:18:44

Okay.

2:18:45

Okay. Now, moving on, guys. Let us go over this exercise again.

2:18:57

I think we talked about this already.

2:18:59

Last class, so I'm this go to take a look at it.

2:19:02

And if you take a look at it, this is the first of our demos that we saw, right?

2:19:08

we were able to see the flavor of that application.

2:19:12

And it's the big picture idea.

2:19:14

What you have?

2:19:15

System message is.

2:19:16

You have a user message.

2:19:17

System message is what defines the high level behavior of the application.

2:19:20

And user message is what?

2:19:22

User message is that user's input.

2:19:24

Okay?

2:19:25

And what I have done, this part you do not have to do.

2:19:27

Right?

2:19:28

But what I've done, you can actually see how we have gone ahead.

2:19:31

How we have basically gone ahead.

2:19:33

And we are now able to,

2:19:35

actually the formatting is not,

2:19:37

absolutely correct right now.

2:19:39

So, other models actually generate

2:19:41

this in different, different ways.

2:19:43

So I can just correct it once.

2:19:46

Okay, okay, it's important not important right now.

2:19:48

But what I wanted to basically show you is this part.

2:19:51

This example is where you'll be able to see that

2:19:54

from the unstructured data,

2:19:56

we are able to extract structured information

2:19:58

and then we can actually store it back in a database.

2:20:01

A table we can store it to.

2:20:03

And it's a very good practical application

2:20:05

of generative AI that a lot of enterprises.

2:20:07

are doing today.

2:20:08

Yeah, or medical notes were,

2:20:09

or something or text or customer complaints were.

2:20:11

Let's say you're calling up customer support.

2:20:13

After customer support, you're talking on the phone.

2:20:15

Now, talk to your phone page.

2:20:17

Your entire speech is getting transcribed.

2:20:19

It's getting converted to text.

2:20:20

Okay.

2:20:21

And from that text, we are getting these extracted information.

2:20:26

So we can actually, at the end of that entire customer conversation,

2:20:30

we can have details like, you know, who was the customer,

2:20:34

what was the customer name?

2:20:36

What was the customer name?

2:20:37

customer associate name,

2:20:38

the customer support side of,

2:20:40

what were the things that were talked about?

2:20:43

What were the terms that were used?

2:20:45

Now, some people are,

2:20:45

that they were,

2:20:46

that's all over,

2:20:48

it's all overlaughts

2:20:49

so that will be used.

2:20:52

Sentiment of the call,

2:20:53

that's a new structure in a way

2:20:54

and you can see how useful this will be

2:20:56

to measure the quality

2:20:58

of customer support.

2:21:00

This is the practical application.

2:21:01

And it's a actually

2:21:02

to explain to what I've done,

2:21:04

I've done a simple radio application.

2:21:06

this is a very small application that I'm trying to create.

2:21:11

I've seen it.

2:21:13

Same thing.

2:21:13

This is the gradeo man.

2:21:14

That's it.

2:21:15

Like, we have you,

2:21:16

we have you made up machine learning class

2:21:17

in LLM as an example.

2:21:19

Same story in LLM.

2:21:21

Same story.

2:21:21

So here we're we're doing code run

2:21:22

and we're here we made it's a gridio

2:21:24

application

2:21:25

made up and if you click on that URL,

2:21:27

you'll be able to see.

2:21:28

This you don't have to do the demo.

2:21:29

This I'm just trying to show you.

2:21:32

And here here this is your doctor's view

2:21:34

will be hospital

2:21:35

that's what he will be able.

2:21:37

He doesn't know

2:21:38

that system message

2:21:38

is how I was explaining

2:21:40

in the last session.

2:21:41

System message is

2:21:42

always confidential.

2:21:43

System message this guy

2:21:44

will not know.

2:21:45

The hospital person will not know.

2:21:46

Okay.

2:21:47

So this guy will know,

2:21:48

okay, somebody has built a

2:21:49

bot for me

2:21:50

and now I will simply enter

2:21:52

the user message.

2:21:53

I will simply enter the user message.

2:21:56

And if I hit enter,

2:21:57

I will get the assistant response.

2:21:59

This is the way.

2:22:00

Okay?

2:22:00

The other guy

2:22:01

another doctor has, what will

2:22:02

do that?

2:22:04

one medical notes enter

2:22:07

that other one

2:22:08

one medical note

2:22:09

enter

2:22:09

is your medical note

2:22:12

and you submit

2:22:14

this is the user message

2:22:15

doctor who's

2:22:17

doesn't know

2:22:17

user message

2:22:18

he will simply enter his notes

2:22:20

and he wants to see the answer

2:22:21

okay?

2:22:22

so system message is stored

2:22:24

behind the scenes

2:22:25

as you as you submit click

2:22:27

this that system message

2:22:29

is combined with this user message

2:22:31

and automatically

2:22:32

that client chat completions

2:22:33

create follow

2:22:34

is done and you're seeing the response back.

2:22:36

So that is what is going on behind the scenes.

2:22:38

So behind the scenes

2:22:39

what are?

2:22:40

Here here here

2:22:41

here Jason is.

2:22:42

His name is 45A

2:22:43

female

2:22:44

is his name Krishna Veni

2:22:45

and diagnosis null

2:22:46

weight is null

2:22:47

and weight has

2:22:48

not it's not.

2:22:48

Weight is not you're able to see.

2:22:53

So very interesting.

2:22:54

So that entire call is happening

2:22:55

behind the scenes.

2:22:56

So when you hit the submit button

2:22:57

so real in your website

2:22:59

has a website be the same

2:23:01

website be the same work

2:23:02

and you have some information

2:23:03

in order, you

2:23:04

you've entered click

2:23:04

you, you

2:23:05

submit click

2:23:06

so this is like

2:23:07

the user message.

2:23:08

This user message

2:23:09

combined

2:23:11

for system

2:23:11

with system message

2:23:13

with some system message

2:23:15

and based on that

2:23:17

the prompt is getting

2:23:18

formed.

2:23:19

Client dot chat completions

2:23:20

are create.

2:23:21

You're making the API call

2:23:22

and you're getting

2:23:23

the response back.

2:23:24

You have a response in.

2:23:26

So the, so here

2:23:27

we're not code not

2:23:28

but this is

2:23:29

exactly what is going on

2:23:30

behind the scenes.

2:23:32

When you're chat GPT

2:23:34

we use

2:23:34

are not,

2:23:35

same thing is happening

2:23:35

behind the scenes

2:23:36

in chat GPT.

2:23:37

So we're just

2:23:39

just chat gpt

2:23:40

use the right.

2:23:40

But now you

2:23:41

get a better idea

2:23:41

of what is going on.

2:23:42

Here here

2:23:43

here

2:23:43

here the API

2:23:43

call

2:23:43

is okay.

2:23:44

Now you

2:23:44

when you

2:23:45

when you're

2:23:46

what is

2:23:47

the capital

2:23:47

of

2:23:48

what is the capital of

2:23:50

India?

2:23:52

What is the capital

2:23:53

of India?

2:23:55

When you ask

2:23:55

that question,

2:23:56

what is the capital

2:23:57

of India

2:23:58

when you go back

2:23:58

and ask that question

2:23:59

so this is

2:24:01

like the user message

2:24:01

then you are combining that user message with what?

2:24:07

With some pre-saved system message.

2:24:12

We are combining that user message with some pre-saved system message.

2:24:19

ChatGPT's system message.

2:24:21

We have told the last class.

2:24:22

They didn't know,

2:24:23

but actually it's hidden

2:24:24

so you,

2:24:25

so you ever chat gpity in

2:24:26

and the moment you hit enter,

2:24:28

that is your user message

2:24:29

which gets combined with the hidden system message.

2:24:31

behind the scenes,

2:24:33

that problem

2:24:34

and using that prompt,

2:24:37

we do client chat

2:24:38

completions create

2:24:38

this will

2:24:41

internally call a LLM

2:24:42

which we're in

2:24:43

code in

2:24:43

right,

2:24:44

client or chat

2:24:44

completions create

2:24:45

the same groc

2:24:46

call

2:24:47

here he

2:24:47

he will

2:24:48

open AIA model

2:24:48

call

2:24:49

and he

2:24:50

will call

2:24:51

and if he

2:24:52

respond to

2:24:53

so that's the way

2:24:54

how it

2:24:54

works out

2:24:55

okay

2:24:56

and the code

2:24:57

is the same

2:24:57

now

2:24:58

you're surprised

2:24:59

you guys

2:25:00

you're surprised

2:25:00

you're going to

2:25:01

here we're

2:25:02

we're doing

2:25:02

we're doing

2:25:03

we're

2:25:03

we're doing that

2:25:03

client equal to

2:25:04

grog

2:25:04

I'm just

2:25:05

just saying

2:25:06

client equal to

2:25:06

grog

2:25:06

I'm just saying

2:25:08

we're just saying

2:25:08

client equal to

2:25:09

grog

2:25:09

we're using

2:25:10

we're

2:25:10

we're

2:25:11

we're

2:25:12

we don't

2:25:12

a little

2:25:13

en little snippet

2:25:13

so

2:25:14

here

2:25:14

so

2:25:15

this is

2:25:15

relevant

2:25:16

not

2:25:17

just so that you

2:25:19

got a

2:25:20

good learning

2:25:20

uh

2:25:21

these models

2:25:24

are so

2:25:24

costly

2:25:24

right

2:25:24

we don't

2:25:25

we don't give

2:25:25

you the keys

2:25:26

and all for this

2:25:26

so keys

2:25:28

ches

2:25:28

need actually

2:25:29

but just to

2:25:30

show you a small demo.

2:25:35

So

2:25:35

you can

2:25:37

see

2:25:38

we're

2:25:38

so Grog is basically

2:25:40

a platform

2:25:41

so similarly

2:25:42

Open AI

2:25:44

developer

2:25:44

platform

2:25:45

is what we

2:25:46

what we're

2:25:46

what we're

2:25:48

platform.

2:25:49

that is openAI.com

2:25:50

that is

2:25:51

developer

2:25:52

platform

2:25:52

you don't have to do this

2:25:53

this is just

2:25:54

something I'm trying

2:25:54

to show you

2:25:55

just like

2:25:56

just like GROX developer

2:25:57

platform

2:25:57

this is open AI is

2:25:58

developer platform

2:25:59

okay this is

2:26:00

platform.

2:26:01

OpenAI.com,

2:26:02

you can

2:26:02

you can't

2:26:02

API keys create

2:26:03

and here

2:26:04

here we can

2:26:04

create

2:26:05

create

2:26:05

everything

2:26:06

here

2:26:07

here there's

2:26:07

there's

2:26:07

there's

2:26:07

only

2:26:08

difference is

2:26:09

here

2:26:09

you can

2:26:10

you need

2:26:11

and

2:26:12

this

2:26:12

highly paid

2:26:12

model

2:26:12

and this

2:26:13

this

2:26:13

is available

2:26:14

not

2:26:14

available

2:26:18

that you can.

2:26:19

same code is.

2:26:19

you'll be

2:26:21

you'll be shocked

2:26:21

the code

2:26:22

is the same

2:26:22

client equal to

2:26:23

open AI

2:26:24

client chat

2:26:24

completion's created

2:26:25

same story

2:26:26

we can't

2:26:27

we'll be side by

2:26:28

and you'll be

2:26:29

surprised.

2:26:29

Okay, that's why I always stress.

2:26:31

Once the concepts are clear,

2:26:32

so it's very easy to implement it anywhere.

2:26:35

Okay.

2:26:35

Now,

2:26:35

you know,

2:26:35

here here

2:26:36

my personal

2:26:37

my

2:26:37

case has

2:26:38

I have my

2:26:40

Open AI API key.

2:26:41

Okay,

2:26:41

that is for my

2:26:42

word purpose

2:26:42

I,

2:26:43

you know,

2:26:43

we get a good

2:26:44

amount of keys

2:26:45

with us,

2:26:46

right?

2:26:46

This is my

2:26:46

Open AI API

2:26:47

key.

2:26:48

So what I'm doing,

2:26:49

I'm straight away

2:26:50

instantiating this

2:26:52

client equal to

2:26:54

open AI.

2:26:54

I'm using GPT 5.4 nano.

2:26:57

Okay,

2:26:57

GPT 5.4 nano use

2:26:58

I think they should still be

2:27:01

they should still be working.

2:27:03

If it's worth it,

2:27:04

then you can

2:27:04

you can't

2:27:04

you can't

2:27:05

no problem

2:27:05

no.

2:27:08

The code

2:27:08

to say but the

2:27:09

model is costly

2:27:10

right

2:27:10

because first of all

2:27:11

you have to

2:27:11

understand

2:27:11

you know

2:27:12

Rajde that this

2:27:13

model is very costly

2:27:14

it's a development

2:27:15

cost is research and

2:27:16

development cost

2:27:17

they?

2:27:18

They've made an open

2:27:19

idea?

2:27:19

Open A idea?

2:27:20

You have to hire

2:27:22

developers.

2:27:23

Each developer

2:27:24

for you have

2:27:24

to hire developers.

2:27:25

Each developer

2:27:28

and development they have invested

2:27:28

on, there are massive offices, and to train

2:27:31

these models, there is massive amount of compute.

2:27:33

You're

2:27:33

in the

2:27:33

building,

2:27:34

people

2:27:34

hire to hire

2:27:35

the cost

2:27:36

that's

2:27:36

the reason why

2:27:39

these models are

2:27:40

very costly.

2:27:41

Compared to that

2:27:42

open source models

2:27:42

are not that good.

2:27:44

You're not

2:27:44

that compare any

2:27:45

can't.

2:27:45

GPT 5.5 is another

2:27:46

level

2:27:47

ultimator.

2:27:47

Its intelligence

2:27:48

is different.

2:27:49

It is very good.

2:27:51

Okay?

2:27:51

And here I will use

2:27:53

5.4 nano.

2:27:54

We'll use

2:27:55

5.4 nano use

2:27:56

okay?

2:27:57

Same story.

2:27:58

Same story.

2:27:58

system message, user message,

2:28:00

and you look,

2:28:01

client chat competitions

2:28:02

create

2:28:02

same story.

2:28:04

Code,

2:28:04

went fine,

2:28:08

you can see,

2:28:08

and this is better.

2:28:10

You can see, and this is better.

2:28:10

You know,

2:28:10

you, you know,

2:28:12

look, this grog

2:28:13

is, this grok

2:28:14

is, this grog

2:28:15

this grok's response.

2:28:16

Leto,

2:28:16

here here to

2:28:16

here,

2:28:17

look, look,

2:28:18

here, look,

2:28:19

but if you go to the

2:28:21

next one,

2:28:23

very interesting,

2:28:24

if I,

2:28:24

if I,

2:28:24

if I run the next one,

2:28:26

you can you

2:28:28

here here

2:28:28

answers

2:28:28

if you go back

2:28:30

and do the

2:28:31

next one,

2:28:32

you will be

2:28:32

able to see

2:28:33

that most

2:28:33

likely the

2:28:34

other model

2:28:36

may not

2:28:37

get the best

2:28:37

response.

2:28:38

Yeah,

2:28:38

this is a

2:28:39

different one.

2:28:41

Don't worry

2:28:41

about this

2:28:41

one, guys.

2:28:44

We have

2:28:45

a other model

2:28:45

here

2:28:45

down here.

2:28:46

Okay?

2:28:49

In case you're

2:28:49

getting an

2:28:50

error there,

2:28:50

just let me go

2:28:51

and use

2:28:52

the same

2:28:52

Lama

2:28:53

versatile.

2:28:56

And what I basically wanted to show is this one.

2:29:09

Now, look,

2:29:09

same thing is,

2:29:11

this is the next medical notes.

2:29:14

And if you see,

2:29:14

I'm using a Lama model

2:29:15

using the GROC API

2:29:17

and I'm getting a slightly different kind of answer.

2:29:19

Can you see the answer is coming like this,

2:29:20

note are here?

2:29:21

All right, we need a.

2:29:22

We have done JSON

2:29:22

I need.

2:29:23

Now same thing.

2:29:24

I will run the same to same

2:29:26

code. I will run the same to same code in my, using my open AI model.

2:29:32

I'm GPD 5.4 use

2:29:33

is even better.

2:29:35

GPD 5.4 is even better.

2:29:37

5.4 is an even more costly model.

2:29:39

I'm using this go and you use

2:29:41

and look at the answer I will get.

2:29:43

Look at the answer I'm very beautiful, clean JSON.

2:29:46

You have different

2:29:46

here here

2:29:48

there's no, nonsense, none of that is there.

2:29:51

Here what's doing?

2:29:52

Here on, here on JSON,

2:29:53

there's justin,

2:29:53

you can clearly see the difference between

2:29:56

the models. Same prompt.

2:29:58

Everything is the same. Only the model is different.

2:30:02

That's it.

2:30:02

So, this is the difference between using open AI models versus other models.

2:30:05

Okay?

2:30:06

Or you've got pricing compared to.

2:30:07

The pricing will be very, very different for these models.

2:30:10

Basically, okay?

2:30:11

My objective to show this code is to tell you that the code is the same.

2:30:15

You can use, you can go back and use the GROC API,

2:30:18

which is the standard for our sessions.

2:30:20

You can go back and use the Open AI API.

2:30:22

The code will be very, very similar.

2:30:24

Client chat completions create.

2:30:25

Okay?

2:30:26

Now, somebody will say,

2:30:27

no, sir, we're doing this, sir, we're using.

2:30:29

We have anthropic to use.

2:30:30

Do you.

2:30:31

No problem.

2:30:31

Go to platform anthropic.

2:30:34

Platform anthropic.

2:30:36

Platform anthropic will have its own team,

2:30:38

cloud platform basically,

2:30:39

the platform is.

2:30:41

It's a different API keys.

2:30:42

Same thing, same story.

2:30:44

If you want to access cloud models,

2:30:45

cloud sonnet, you know, cloud offers,

2:30:47

if you want to use the anthropic suite of models,

2:30:50

then you will create anthropic APIs.

2:30:52

Okay, but these are free freeing.

2:30:54

These are very, very costly models.

2:30:56

You don't need it.

2:30:57

Enterprises in these are used.

2:30:59

But the concept is the same.

2:31:00

My idea is to clarify concept.

2:31:02

That's the same.

2:31:03

Here you can get an API P.

2:31:04

Here you can get an API P.

2:31:06

Okay?

2:31:07

And you can basically go and get an API Pee.

2:31:11

And here also you can go and try your prompt.

2:31:13

Now you have a prompt try to.

2:31:15

You can go and try your prompt.

2:31:17

Here you have your clod's all right.

2:31:19

As a lot of models are, like there were open AI models are all right?

2:31:21

Here there's clod's all the models.

2:31:22

Okay?

2:31:23

Anthropic models are landing.

2:31:24

And you'll be surprised to see

2:31:26

the quad.

2:31:26

code is very, very similar.

2:31:27

Here here here, client equal to anthropic.

2:31:30

There on the client equal to GROC, client equal to open AI.

2:31:33

Now we are looking at client equal to Anthropic.

2:31:35

These are the two biggest LLM providers in the markets today,

2:31:38

Open AI and Anthropic.

2:31:39

And here here, look, client messages create.

2:31:41

This is a difference.

2:31:42

There we have client chat completions create.

2:31:45

Here here, client messages create.

2:31:46

So here, these small differences will be there.

2:31:49

But GROC and Open AI are exactly the same.

2:31:51

But Anthropic is a little different.

2:31:52

But the concept is.

2:31:53

Here here messages, system message, user message.

2:31:56

same story. So once you learn these in one API, it will be very easy to replicate

2:32:00

in the other ATMs, right? So that's one way to leave it.

2:32:05

So let's complete the story here, guys. I think here all I'm doing is I'm just running

2:32:10

through the remainder of the snippets. This is our meeting transcription

2:32:14

use case. We already discussed this last session. And now you can do it using your GROC API.

2:32:20

Okay, you have GROC API use correct. Now, look, here here we have GPD models used

2:32:24

wherever you see the GPD models, I would request you.

2:32:27

Please go back and replace it with your with your drop specific models.

2:32:32

Okay, because the GPD models will will specifically not work here.

2:32:38

So this is the results I'm getting system system message user user message.

2:32:44

Same thing. Same concept we have talked about before.

2:32:48

Okay. All right. So this is pretty much about what I wanted to talk about from the API perspective, but rest of

2:32:54

it is the same thing, exactly the same thing we talked about last class,

2:32:57

few short prompting, zero shot prompting. The objective was to basically tell you

2:33:01

how to make an API call. The API called, what is the meaning of an API call? Okay. Now,

2:33:07

so we talked about cloud API. We talked about cloud API across different platforms. GROC

2:33:12

is open AI here. These all cases in, models are not, we are not downloading it. The models

2:33:19

are available in some cloud. We are simply accessing those models using an API key. And

2:33:24

And the other thing I'm what we've seen?

2:33:25

The other thing, we've seen Olama, and in Olama, what are we doing?

2:33:29

We are installing OLAMA locally.

2:33:31

We are downloading the models locally.

2:33:34

Pull and run with the two important things we studied.

2:33:36

First we pull, then we run.

2:33:38

And then we saw some interesting demos where we were able to run the models.

2:33:43

Now, if we have Olama, can I do it programmatically?

2:33:48

We can do it?

2:33:49

We can do that. And now what I will do?

2:33:52

I will show a small example.

2:33:54

of the code where you can do it that way.

2:33:57

So the code remains exactly the same.

2:33:59

Nothing changes.

2:34:00

You can see a small code snippet.

2:34:02

Exactly what I told you.

2:34:04

Client chat completions create whatever I have in my snippet here.

2:34:08

This is how your simple script will look like.

2:34:10

You really specify the name of your model, local model equal to this.

2:34:13

This is the way you will do it.

2:34:16

Okay. What were we doing in the Windows PowerShell?

2:34:19

Windows PowerShell.

2:34:20

We were actually directly downloading it.

2:34:24

Then we were running the model and we were typing the problem.

2:34:27

When 0.5 billion model we're doing, now what we are doing?

2:34:31

The same thing, we will go and do this programmatically.

2:34:34

Just like how I showed you with the cloud models.

2:34:36

We are writing some Python.

2:34:38

We are connecting to that model using an API key and we are getting a response.

2:34:43

Here here same story.

2:34:44

Here we model can't where there model cloud in.

2:34:48

GROC to GROC to go to GROC.

2:34:50

Client equal to GROC we did.

2:34:52

Client equal to GROC, I'm going to GROC.

2:34:54

Grog, give me your model.

2:34:56

I'm taking it.

2:34:57

That we're doing.

2:34:58

Here, here, here here, here, there's where there.

2:35:00

Here, Olama, that C, user sign, where they stay there.

2:35:03

So this is exactly what I'm doing.

2:35:05

So I'm going to that place where my models are stored.

2:35:08

And I'm writing the exact same thing.

2:35:10

Role system, system message, role user message, same story.

2:35:14

This will be like the system user message, we will have model equal to model name or response

2:35:18

you have here here.

2:35:19

Same code.

2:35:19

The same text remains very similar.

2:35:21

Just here here you'll chat.

2:35:22

You will not say client chat, competition.

2:35:24

create you will just say chat. That's it. So this is just a small change in the output.

2:35:29

So this is the thing. So this is just something you need to keep in mind that here, this is the way

2:35:35

how you can pythonically call these models in Olamma.

2:35:45

Of course, of course. Practical, you're just going to say, the terminal one was something I just wanted

2:35:49

to show you because you were first time we were thinking Ollama is here. Now that, that's, that's,

2:35:53

That way it is easy.

2:35:54

But still, I would say this is a hard way.

2:35:57

Because Grog is even better.

2:35:58

Because Olamas say, you if you're going, then this be slow, slow will be.

2:36:02

Speed will not vary.

2:36:03

Only thing is that this is the, this is the programmatic way of accessing your model.

2:36:08

See, again, the analogy that I want to take is that you are,

2:36:13

your models can either be on the cloud or your models can be locally.

2:36:19

If that model in cloud, then you're in the cloud, then you're going to connect

2:36:22

give a prom, get a response.

2:36:25

If that model local in, then you're local in local to connect

2:36:28

give a prom, get a response.

2:36:30

Story is same.

2:36:31

You have prom to give you response to you and have.

2:36:33

Story is the same.

2:36:35

Only difference is where is the processing happening.

2:36:37

If it's a cloud model, the processing is all happening in the cloud.

2:36:40

If it's a local model, the processing is happening in your system.

2:36:44

So in GROC case, we are just using the API key to access the models.

2:36:48

Whereas in YOLAMA, it's all running in our system.

2:36:51

So Olama is a cloud concept, which is there.

2:36:55

Just wanted to show you, like GROC that we did, so same way, OLAMA is cloud concept is.

2:37:00

So the only difference is, now look, here we're what we're doing?

2:37:03

Two ways. One is, my models are hosted locally.

2:37:08

And second is, as we've got GROC cloud discussed here, GROC is much, much more popular.

2:37:12

Just keep in mind, GROC is much more popular.

2:37:14

It's the fastest inference platform out there.

2:37:17

But OLAMA also has a similar kind of a cloud setup.

2:37:21

Okay?

2:37:21

only two points are changing.

2:37:23

The host will point to Olama.com.

2:37:25

That's what I told you.

2:37:28

So, the first of all,

2:37:28

you know,

2:37:29

go to go, where do you?

2:37:30

Where a model is where?

2:37:32

Is my model available on Olama.com?

2:37:35

Or is my model available local?

2:37:38

You're a host there.

2:37:39

That's it.

2:37:41

The rest of the code remains exactly the same.

2:37:44

Host equal to?

2:37:45

And this is the same story.

2:37:47

User message, system, system message,

2:37:49

same thing.

2:37:50

Nothing changes.

2:37:51

Okay, I would suggest you to follow my notebook.

2:37:54

This is just something I wanted to show you that Olama's local be here.

2:37:57

And Olama's a very small component of cloud be able to be.

2:38:01

Okay, you can think of it that way.

2:38:13

And there are different, different model types that are there in Olamas.

2:38:16

Just as we clarify, you can go back and we, we have got different different,

2:38:21

model types that are there in Olama and what are these different different

2:38:25

different model types that are there so we have got chat competition models we

2:38:29

have got image models we've got speech models and we've also got video based

2:38:34

models so these are different different types of models out there so I'm a

2:38:42

a term use which is called a modality modality. Modality

2:38:45

what is what is? Modality is what is modality.

2:38:47

Modality is what is that different modes of

2:38:51

data.

2:38:52

So you can see OLAVA's library is not only chat text, but I'm not just text-based models.

2:38:59

Majority of our initial part of the course will focus on only text-based model.

2:39:04

But OLAMA is not only for text.

2:39:06

Olamma in a lot of things can do.

2:39:08

So tags and model cards tell you the modality.

2:39:12

Modality means what are the other input outputs that the model supports.

2:39:17

The text, image, audio, video, all over kind of models.

2:39:21

So vision model is one that understands pictures, videos, okay.

2:39:26

Speech model is something that understands speech later.

2:39:29

You're saying, telling something to Gemini, and Gemini is understanding that and transcribing that.

2:39:34

So these are some different, different model modalities that you will get.

2:39:38

And you can go there.

2:39:38

These are some examples.

2:39:39

I wanted to just show you.

2:39:41

You can go to Olama.com search and you can actually search with different modalities.

2:39:48

Vision, tools, thinking.

2:39:50

Can you see very interesting?

2:39:50

These are some vision models.

2:39:52

You can click and you'll be able to see all the vision models available.

2:39:56

See, most of the models today are multi-modal.

2:39:59

We, we all LLMs use today, right now Gemma 4-5 is discussing.

2:40:02

So these are all multimodal.

2:40:04

Whenever you hear that a multi-modal,

2:40:06

multi-model is that multi-model.

2:40:07

Multi-model is that these models are not only good with text.

2:40:10

I mean, this text to do you ask a question, get an answer.

2:40:14

This text will be able to, but these models are very good in multi-modal visioning.

2:40:19

They are also very good in.

2:40:20

handling other forms of data.

2:40:23

They are very good in handling other types of data.

2:40:25

Multi-multible modes of data.

2:40:26

So that is the multimodal models that we are offering to.

2:40:29

So most of them, look at it, all of them.

2:40:32

But last,

2:40:33

each single any models I had,

2:40:35

20-25,

2:40:36

where many models are majorly are multi-models.

2:40:39

All of them.

2:40:40

Now, these all models, they go,

2:40:41

all multi-model.

2:40:42

I mean, they all inherently, and that is the reason why

2:40:44

when you,

2:40:47

not from a technical perspective,

2:40:49

but I'm talking about,

2:40:50

let's say in a Germany,

2:40:50

interface, when you go to Gemini

2:40:52

go to, you, you're on the document

2:40:53

can also upload

2:40:54

can, as you as

2:40:55

picture also upload

2:40:56

as with as

2:40:57

voice also voice

2:40:57

upload to,

2:40:58

that all

2:40:58

they can

2:41:00

basically process all

2:41:02

different forms of

2:41:02

inputs and it can

2:41:03

process all

2:41:04

different forms of outputs.

2:41:06

So that is the best

2:41:06

part.

2:41:07

You've asked a

2:41:07

question

2:41:08

for Germany,

2:41:08

it's all

2:41:09

a different

2:41:09

answer to get.

2:41:11

And in fact,

2:41:12

let me,

2:41:13

did I, did I,

2:41:13

did I talk about this Google Photos thing last time?

2:41:17

We've discussed

2:41:18

I don't recall it.

2:41:22

So I can show you a really cool, cool demo.

2:41:25

So I think I did not probably talk about this with you.

2:41:27

But I,

2:41:27

huh,

2:41:29

that's,

2:41:30

that's,

2:41:31

next class is.

2:41:32

Rack's not a new reference

2:41:33

is next class.

2:41:35

That is next session.

2:41:36

But what I was talking about in Germany,

2:41:38

this is the last thing I will talk about here.

2:41:40

So if you go and ask the question,

2:41:41

show me, show me the latest.

2:41:43

this is true multimodality in action,

2:41:48

through multi-modality.

2:41:49

Show me the latest,

2:41:50

show me all the

2:41:51

all my photos

2:41:55

of sunrise and sunset

2:41:58

that I have taken

2:42:01

from flights.

2:42:06

If I ask this kind of a question,

2:42:08

Gemini will automatically pull all my

2:42:11

answer from my, you know,

2:42:12

answer from my Google photos.

2:42:13

you photos connect

2:42:15

it will pull up the pictures

2:42:17

and it will answer.

2:42:18

This is a true multi-modal model.

2:42:20

I am writing something in text

2:42:21

but it is pulling out the pictures

2:42:23

and on that basis

2:42:25

I can ask you to generate something.

2:42:26

Now move it.

2:42:27

These are all pictures I have taken.

2:42:31

You don't believe?

2:42:32

You don't believe? As I say when I click on it,

2:42:33

it is opening my photos.

2:42:35

This is my picture.

2:42:36

Photos by sign.

2:42:37

Look at this.

2:42:38

These are my pictures.

2:42:39

And I am asking a question

2:42:41

and it is able to pull up the pictures

2:42:42

from my photos account.

2:42:43

And now I can say that use all this, use all this and generate the best, the best sunset picture.

2:42:58

Now it's generate to generate to be bolder.

2:43:01

Brown, like,

2:43:04

now we're going to generate to create to be able to.

2:43:06

Now this is true multimodality.

2:43:08

Now it will try to generate an image.

2:43:09

Now, look, this creation is.

2:43:10

Now, this creation is creating it now.

2:43:13

that is multi-modality.

2:43:15

You are giving the input in text.

2:43:19

I love to retrieve my photo's library.

2:43:21

Now I'm going to make it.

2:43:22

He's output-carra-a-picture.

2:43:24

And this is the real multi-modality inaction.

2:43:27

Okay?

2:43:28

Right?

2:43:31

This will take a while, but you can see that after a while

2:43:34

this is created.

2:43:36

This is nice.

2:43:37

I don't know.

2:43:38

You can see this is kind of combined everything.

2:43:41

This is kind of combined everything.

2:43:42

I don't know, he, this guy's hand came.

2:43:45

Maybe there, somebody's hand was there,

2:43:47

so they've been they've been made.

2:43:49

Very nice, actually.

2:43:51

And very scary.

2:43:52

You have Gemini use and you can actually do this.

2:43:54

You, you can actually do this.

2:43:57

You, you know, you're up to describe kind of,

2:43:57

yeah, boy, four, five photos,

2:43:58

like, take, and make it based on, and do you know,

2:44:01

and I say, but it's, there's a lot of crazy things people can do with it,

2:44:06

actually.

2:44:07

You know, so,

2:44:09

anyways, so this is something I wanted to show you

2:44:11

with respect to multimodality.

2:44:12

Or you have a voice be add can't.

2:44:14

You, now do you add can't do,

2:44:15

so that is the meaning of multimodality.

2:44:19

This is what multimodality means.

2:44:23

And finally, there is rags.

2:44:24

Rags are the next topic that is not relevant for today.

2:44:27

So rags are something we will be seen in the next session.

2:44:30

So rags are again a very, very interesting topic

2:44:32

that we'll be seen in the next session here on which.

2:44:36

So now, just to summarize the conversation, guys,

2:44:40

we have seen, we have seen a lot of things,

2:44:43

a lot of things today in terms of what LLMs are.

2:44:46

So we have spent our time today discussing about LLMs.

2:44:50

So how do we pull a like model?

2:44:53

We have seen some examples,

2:44:54

how we run a single prompt on the CLA.

2:44:57

Okay, we have talked about some of the benefits of using heavy models,

2:45:02

life models.

2:45:03

What are the tradeoffs?

2:45:04

Okay, we have written some short scripts, right?

2:45:06

And we have gone ahead and seen a lot of code

2:45:09

and the multi-modality in action.

2:45:12

This is again what we have seen with respect to open source satellite lens today, right?

2:45:16

And next session onwards will be a very exciting class.

2:45:19

That is tomorrow.

2:45:19

Tomorrow we are having the class.

2:45:21

Actually, I had fever, you know, two, three days back.

2:45:24

I was suffering from fever.

2:45:25

That's why I could not take the class.

2:45:28

So tomorrow, anyways, 3 to 5.30, we are meeting.

2:45:31

So very interesting class on lags.

2:45:33

Don't miss it, guys.

2:45:34

So, and here we will see some very, very interesting things also tomorrow.

2:45:38

Yeah.

2:45:38

So I will hand it over to, yeah, all right, all right.

2:45:47

Yes.

2:45:48

So then any questions, any questions anybody has at this point in time?

2:45:54

All good.

2:45:55

Everyone's clear with the concepts.

2:45:57

Anything else you want to ask me?

2:46:03

There'll be quiz.

2:46:05

No, there won't be any quiz today.

2:46:07

There won't be any quiz today, Gunal.

2:46:08

I think Arsita is not here.

2:46:10

Orsita will conduct the quiz on our TA session.

2:46:13

In the next plus, yeah, yeah.

2:46:15

Kalka time is 3 to 530A.

2:46:17

That's right, that's right, yes.

2:46:20

Yeah, absolutely.

2:46:21

You're right, absolutely.

2:46:24

In defense and all these industries, there is no question of cloud.

2:46:27

Cloud's no concept in any.

2:46:28

Because it is very sensitive.

2:46:30

So everything, everything is your local is.

2:46:33

And then you're all right?

2:46:35

And then you're not, you're not.

2:46:35

You can't connectivity in any can't.

2:46:37

Internet is not like,

2:46:38

You know, internet is not like,

2:46:40

I'm saying internet is always like worldwide.

2:46:42

No, internet must have network.

2:46:44

Even local internet is like internet.

2:46:46

That's disconnected.

2:46:48

Like as you said, combat aircrafts or stealth aircraft,

2:46:50

where you're completely cut off from the world.

2:46:52

How do you run a model in that isolated environment?

2:46:56

So this is your olama is a very nice way to think about it.

2:47:02

India, to make, I think there's a company called Sargum AI.

2:47:05

It is doing a lot of good work in the space.

2:47:07

So I think, I think.

2:47:08

I think they, it was also, uh, circumcish all right.

2:47:14

So Sargum AI.

2:47:15

Oh, sorry, Sarva may I was, I was actually in the wrong page.

2:47:20

Servam AI.

2:47:21

So this is actually one of the foremost companies in India that is working on

2:47:25

NM's.

2:47:27

You can read about it.

2:47:28

It also featured in the India AI summit in a lot of detail.

2:47:32

Okay.

2:47:32

So these are some companies that are doing a lot of good work in the space, I would say.

2:47:36

Yeah.

2:47:37

Certainly it requires a lot of, you know,

2:47:38

you know, interest and research and all that for this to really scale.

2:47:43

That be here.

2:47:44

That you have to look at it.

2:47:49

Yeah, yeah, correct, correct, absolutely.

2:47:53

No, so outdated, it depends.

2:47:56

Outdated, that's your knowledge cut off.

2:47:59

That, till what time the models were trained.

2:48:02

The models were trained latest at last month or last year.

2:48:05

It's your date right.

2:48:07

That anyways, you will have that input.

2:48:08

That's the cutoff date on.

2:48:11

I mean, yeah, so outdated like you're revised and go.

2:48:15

You're using a certain model.

2:48:16

If you think, yeah, this model is not getting,

2:48:19

so you'll a fresh model download and you're going.

2:48:21

That's the idea.

2:48:22

You know?

2:48:25

No, huge.

2:48:26

These are like super computers you're talking about.

2:48:30

Machines, what are the, how do you tell them?

2:48:33

This is like huge servers.

2:48:35

I'm like example.

2:48:36

I'm an example.

2:48:36

If you're going to example, if you go, if you're going to hospital,

2:48:38

or any big supermarket in you go,

2:48:41

you can you see a server room?

2:48:43

Usually it says respected access

2:48:44

or the movies in the movie. It is like that

2:48:47

a server room.

2:48:48

There's a lot of computers that are,

2:48:50

the computer, I mean, like, how do I explain?

2:48:54

They say, you know,

2:48:57

it's best if I show you a picture.

2:49:00

This is your server room

2:49:01

so it's a type of something

2:49:03

something.

2:49:04

And this type of thing.

2:49:06

And this hardware level is.

2:49:07

My company, I don't work. I also don't have expertise at this level.

2:49:13

This is, this is,

2:49:14

hardware can't be able to,

2:49:15

my expertise is,

2:49:17

we're up on LLM's go back.

2:49:19

My LLM is basically sitting on this.

2:49:22

What I mean,

2:49:22

what we were we discussed

2:49:23

in OLA, so,

2:49:25

this is your computer

2:49:27

have.

2:49:28

Our laptop is,

2:49:29

you're your computer

2:49:30

and your LLM is inside this.

2:49:33

And your Pytton is inside this.

2:49:33

And you're Python,

2:49:35

you'll here Python code

2:49:36

you know, he'll you, he'll

2:49:39

he'll here at API

2:49:40

call and he'll

2:49:41

answer to.

2:49:42

Sara processing here

2:49:43

would make sense?

2:49:45

No, so

2:49:45

spacecraft

2:49:46

it's the whole thing, right?

2:49:49

Spacecraft and,

2:49:50

you're saying,

2:49:51

you're saying,

2:49:51

you're saying,

2:49:51

you're talking,

2:49:52

you're,

2:49:53

this is a very

2:49:53

scale in

2:49:54

this is we're

2:49:55

very big scale

2:49:56

in this is

2:49:56

it's a

2:49:59

supercomputer, it's a

2:49:59

supercomputer,

2:50:00

Tesla has a

2:50:00

supercomputer sitting

2:50:01

in a very small chip.

2:50:04

Now,

2:50:05

now,

2:50:05

this is a,

2:50:06

This is at a different scale already I'm talking.

2:50:09

You're asking me the question about defense,

2:50:11

that's full defense

2:50:12

that's, if you're talking about

2:50:13

only one fighter jet

2:50:15

or one spacecraft,

2:50:16

there's a

2:50:17

small supercomputer

2:50:17

will be that

2:50:18

that's a big

2:50:18

that's a chip

2:50:19

that are in a chip,

2:50:20

that's a chip in

2:50:21

that's a chip.

2:50:23

You know?

2:50:23

Like Tesla car,

2:50:24

Tesla car will be a great example.

2:50:26

You're a YouTube video

2:50:26

go,

2:50:27

and search

2:50:28

Tesla, Tesla,

2:50:30

a semiconductor,

2:50:31

the end up

2:50:31

the GPUs use

2:50:32

that Tesla GPU,

2:50:33

I'm sure

2:50:34

some Google's

2:50:35

picture is

2:50:35

here here.

2:50:36

Tesla, car, GPU,

2:50:39

Tesla's in there

2:50:39

there are

2:50:39

there's

2:50:40

you can't

2:50:41

see how

2:50:42

there's

2:50:43

there's

2:50:43

where

2:50:43

there's

2:50:43

like

2:50:45

or

2:50:45

your Tesla

2:50:46

car

2:50:46

in

2:50:47

some

2:50:47

GPUs

2:50:48

that are

2:50:49

people who

2:50:50

do they

2:50:50

make

2:50:50

video who

2:50:50

made

2:50:50

they

2:50:50

made

2:50:51

I saw

2:50:52

a video

2:50:52

some

2:50:52

few days

2:50:53

back

2:50:53

where they

2:50:54

there was

2:50:55

a guy

2:50:55

he was a

2:50:57

guy

2:50:57

who

2:50:57

his

2:50:57

name

2:51:00

was Siraj Raval

2:51:01

So what this guy did? He revealed how to mine Bitcoin and Ethereum with the car's electric battery and GPU.

2:51:08

They made Tesla car's GPU

2:51:10

got

2:51:11

and they took

2:51:12

and they took

2:51:12

Bitcoin mine

2:51:13

started.

2:51:14

So basically

2:51:16

hardware

2:51:16

has in the car but is a small car

2:51:19

but is a small car.

2:51:19

But the chip is small, right?

2:51:21

chip is small, right?

2:51:23

I hope you are getting it.

2:51:24

It is possible.

2:51:25

It all depends on your use case, actually.

2:51:31

Yeah.

2:51:34

Yeah, absolutely.

2:51:35

Absolutely.

2:51:36

Yeah, you can do that.

2:51:39

Chalro, very nice, guys.

2:51:42

Chalo, good.

2:51:43

A bit of a new thing,

2:51:44

and I think we are slowly starting to come

2:51:45

to the more exciting parts of the course.

2:51:48

LLNs and agents are very exciting to also teach.

2:51:51

So,

2:51:51

I mean,

2:51:51

it's a

2:51:52

more funn't,

2:51:53

it's funn'

2:51:53

and

2:51:54

fun to,

2:51:55

I think,

2:51:55

and now rags would be very interesting.

2:51:59

So do join the class for everybody.

2:52:01

tomorrow.

2:52:02

People do do the demo.

2:52:03

Some of you, I think,

2:52:04

mostly everybody was doing

2:52:06

very good in the class,

2:52:07

but some of you, I think,

2:52:08

your Olamah

2:52:09

didn't go to the class

2:52:10

in, so do

2:52:10

make sure you do the demo

2:52:11

at the end.

2:52:13

Okay,

2:52:13

grog is simple

2:52:14

and all of all

2:52:15

which is great.

2:52:16

But Olamah part,

2:52:17

please make sure that

2:52:18

people who miss the class,

2:52:19

one recording

2:52:20

listen and one

2:52:21

back back.

2:52:22

You can again

2:52:22

ask me questions tomorrow.

2:52:23

No problem.

2:52:24

Okay, and I will see

2:52:26

all of you tomorrow.

2:52:27

Yeah, there's a poll

2:52:28

I will quickly launch

2:52:29

and the quiz

2:52:30

I think will happen with you next week.

2:52:33

So please take some time

2:52:34

to fill up your polls for the session

2:52:35

and that will be all for the class

2:52:38

after a little bit out.

2:52:41

Autopilot mode

2:52:42

you have asked,

2:52:43

I might have missed that.

2:52:46

Yeah, so

2:52:47

did it get answered for you?

2:52:49

Yeah, then you still have a question.

2:52:54

Please let me know.

2:53:00

And this is actually a very interesting part.

2:53:02

Defense is a very good point you take.

2:53:04

And this only defense

2:53:05

in finance in finance.

2:53:06

We've done banks for

2:53:06

banks for

2:53:07

I worked on a project for

2:53:09

Australia, New Zealand

2:53:09

Bank, A&Z Bank

2:53:10

and I did

2:53:11

do. So banks are very sensitive.

2:53:15

Banks may be cloud

2:53:16

cloud call

2:53:16

there's the

2:53:17

what we're talking about,

2:53:19

you send a prompt outside

2:53:20

or how to respond.

2:53:22

This is

2:53:23

concept in the banks

2:53:24

in the banks in

2:53:24

API keys.

2:53:25

When you talk about banks,

2:53:26

everything is on

2:53:28

on premise.

2:53:29

Everything is on premise.

2:53:30

Some of your local

2:53:31

in banks.

2:53:32

Health care company.

2:53:33

One other example is.

2:53:34

Health care.

2:53:35

I mean,

2:53:36

healthcare is sensitive data.

2:53:38

We're

2:53:38

we're sometimes

2:53:38

we're not sensitive

2:53:39

we're not.

2:53:39

I mean, we

2:53:40

think,

2:53:40

that's

2:53:41

that is actually

2:53:43

sensitive data.

2:53:43

If you're

2:53:44

Western countries

2:53:44

go to Western countries

2:53:44

go to

2:53:46

Westland

2:53:47

nations,

2:53:47

health care is

2:53:47

very sensitive.

2:53:49

Extremely confidential

2:53:50

data.

2:53:50

The patient's

2:53:51

what blood group

2:53:52

is, what

2:53:52

it is,

2:53:53

it is as good

2:53:54

as personal

2:53:55

private information.

2:53:56

So health care

2:53:57

companies also

2:53:57

never use

2:53:59

these kinds of

2:54:00

cloud providers.

2:54:00

They will always

2:54:01

want to create

2:54:02

local elements.

2:54:03

They're all

2:54:04

invests.

2:54:05

They're very

2:54:05

money.

2:54:05

They're in

2:54:06

their hardware

2:54:06

in

2:54:06

their servers

2:54:07

in

2:54:08

such servers in

2:54:08

I can

2:54:09

give you

2:54:09

names like

2:54:10

you take

2:54:10

any of the

2:54:11

major drug

2:54:11

manufacturers.

2:54:13

You're

2:54:13

you search

2:54:14

or Novotis

2:54:14

go.

2:54:15

Nobonautist

2:54:16

is a

2:54:17

massive

2:54:18

Denmark-based

2:54:18

company

2:54:19

whose

2:54:19

his

2:54:19

other

2:54:20

drug

2:54:22

as big

2:54:22

drugs

2:54:23

like drugs

2:54:23

medicine.

2:54:24

Drug

2:54:24

not

2:54:24

medicine

2:54:24

or drug

2:54:25

like medicine.

2:54:25

Not like medicine

2:54:27

with medicine

2:54:27

about.

2:54:28

So

2:54:28

so many pharmaceutical

2:54:30

companies

2:54:30

you know, Astra Zanica is a great company you can, you can read about, they're all investing on these

2:54:35

kinds of on-premise local solutions, actually, who are up their servers

2:54:40

because they, they can't

2:54:41

they're not

2:54:42

patient data is very confidential actually.

2:54:46

So,

2:54:46

so at least

2:54:49

is important thing.

2:54:50

Yeah,

2:54:50

that implementation in the classroom context

2:54:52

you're not

2:54:53

that you know, your systems and all

2:54:55

will have to have the capacity,

2:54:56

but at least the knowledge should be there.

2:54:58

So, you know, guys, I'm looking forward to see everybody tomorrow.

2:55:04

Tomorrow, please don't miss the class.

2:55:05

That's my request.

2:55:05

Because, look, like,

2:55:07

Rags is important thing.

2:55:08

So everybody must be there tomorrow in the class, okay?

2:55:11

Ah.

2:55:15

Okay, thank, thank you.

2:55:20

Sorry.

2:55:22

Thank you so much, guys.

2:55:23

Thank you, everybody.

2:55:25

I will see you tomorrow.

2:55:27

Okay?

2:55:27

Take care.

2:55:27

Take care all of you.

2:55:30

Can you please share the Google Drive link?

2:55:33

Yeah, yeah, sure.

2:55:35

Sure, I mean.

2:55:38

Drive link

2:55:39

I've already shared

2:55:40

but, um,

2:55:43

one minute.

2:55:46

Let me

2:55:46

let me share with you.

2:55:52

Please,

2:55:53

this is safe for a practice, because this is

2:55:54

important.

2:55:56

Yeah.

2:55:57

Yeah, yeah. Thank you. Of course, yes. So it is, it's showing error at my end.

2:56:10

Okay. I, I'm sharing. I'm sharing.

2:56:16

See, this is the main, this is the main drive link, Ali, that I'm maintaining for the whole cohort.

2:56:23

This can't all right? You can't all right?

2:56:26

So, you're all right? So, you're the main drive link.

2:56:27

link.

2:56:29

Today date 22 may.

2:56:30

You have 22nd of folder

2:56:31

you go.

2:56:31

You'll

2:56:32

all the content

2:56:32

just to

2:56:32

get you.

2:56:33

Okay?

2:56:35

22 in the folder

2:56:36

you'll

2:56:36

see you'll

2:56:36

see everything.

2:56:37

You know,

2:56:38

you'll see.

2:56:39

So, okay.

2:56:41

Okay.

2:56:46

Okay?

2:56:50

Thank you.

2:56:50

Thank you.

2:56:51

Thank you.

2:56:52

Have a good night.

2:56:54

Yeah.

2:56:54

Take care.

2:56:54

Bye, guys.

2:56:55

See you tomorrow.

2:56:56

All of you.