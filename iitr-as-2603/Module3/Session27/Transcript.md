0:00

By the start, you're putting them in the

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

Thank you.

5:00

Thank you

5:30

Thank you

6:00

Thank you

6:30

Thank you

6:32

Thank you

6:34

Thank you

6:36

Thank you

6:38

Thank you

6:40

Thank you

6:42

Thank you

6:44

Thank you.

7:14

Thank you.

7:44

Thank you.

8:14

Thank you.

8:44

Thank you.

9:14

Thank you.

9:44

Thank you.

10:14

Thank you.

10:44

Thank you.

11:14

Thank you

11:44

Thank you

12:14

Thank you

12:16

Thank you

12:18

Thank you

12:20

Thank you

12:22

Thank you

12:24

Thank you

12:26

Thank you

12:28

Thank you

12:30

Thank you

12:32

Thank you.

13:02

Thank you.

13:32

Thank you.

14:02

Thank you.

14:32

Thank you.

15:02

Thank you.

15:32

Thank you.

16:02

Thank you.

16:32

Thank you.

17:02

Thank you

17:32

Thank you

18:02

Thank you

18:04

Thank you

18:06

Thank you

18:08

Thank you

18:10

Thank you

18:12

Thank you

18:14

Thank you

18:16

Thank you

18:18

Thank you

18:20

Thank you.

18:50

Thank you.

19:20

Thank you.

19:50

Hi, everybody. Good evening all of you. We will start on here.

20:20

Thank you.

20:50

Thank you.

21:20

Thank you.

21:50

Thank you.

22:20

Thank you.

22:50

All right.

22:54

All right, folks, once again, uh,

22:57

welcome all of you to the session and we will start on.

23:16

And today the agenda would be to talk about.

23:19

talk about open source models, that is going to be the main agenda of the session today.

23:24

So we'll be covering about open source models and the related ideas around that.

23:31

So so far we have primarily if you go back to the session that we have conducted so far,

23:38

we have in our main focus has been on the GROC API.

23:44

We have been mainly using the GROC API where you know we have a cloud platform.

23:49

and we are using the GROC API. That has been the main focus so far.

23:52

So today the entire session will focus on the idea of local LLMs, how we can use a local model,

24:06

and that is what we'll be seeing. I will take you through something called Olama and I will walk

24:14

you through the steps, how we can install Ollama, how we can use Ollama to

24:18

take a local LLM. What are some of the considerations that we should, you know, keep in mind

24:25

when it comes to local models versus other kinds of models? What are the things to keep in mind?

24:30

So we will have a discussion on that. And that is what we will do. Again, it will be a very practical

24:35

session, but yes, there will be a lot of conceptual things that I will cover. I will cover a lot of

24:40

conceptual things in what in terms of what, you know, these kinds of models are, what they bring to

24:44

the table and all. So we'll be seeing quite a bit of that.

24:48

Okay, let me quickly share my screen with all of you. So that everybody is able to see this.

24:59

Just a second. Here it goes. So, this is pretty much what we will be doing for the session,

25:09

open source. Now guys, just to take you back to the conversation the conversation that we had in the very

25:17

initial phases of our module. We all understand what are large language models. LLMs are

25:23

these massive models where you can give some input prompt and the language models will generate some

25:31

output response. There are these massive models that will take some input and generate some output.

25:36

We've already seen that. And there were primarily two different categories of models that we have

25:44

have, right? On one hand, you have the typical open source. You are the typical paid

25:51

providers. When it comes to the paid providers, we have, you know, we have the GPT models, the Gemini

25:59

models. These are a typical paid providers that you have, right? So for example, if you go

26:07

to platform open AI, you can access all the open AI, you can access all the old.

26:14

open AI models through the API key. You can do that. You can go to platform open AI and you will have

26:21

access to all the open AI models from here, right? So open AI is a paid provider. And they will charge you

26:30

for their models. These are not open source models. There is no way you can download a GPT model or this thing,

26:35

right? The same applies for anthropic cloud models. The same applies for Google Gemini models. And these are

26:44

models which are available only through API access.

26:51

So one question people might have is that what is the, what is the value at that, you know,

27:02

it brings to the table? So when we are using these kinds of the paid providers are, do we get any

27:09

benefits? Answer is yes, you do. Yes, you do. Whenever you're using the paid providers, we do get

27:13

some benefits. So first of all, they are better quality models. They are trained on more

27:18

data. And these models actually score very highly on the performance benchmarks. That is one

27:28

more thing to keep in mind. Right? And I think everybody should understand the concept of

27:36

benchmarks. See, next time you are asked a question that, uh, which models?

27:43

is better. Right? In our sessions, the main focus has been the GROC models. But let us face it.

27:51

If you're working in a real enterprise, you will be working with many of these other providers also,

27:56

right? The concepts will remain the same. None of the concepts will change. The same client chat

28:02

completions create. That story remains the same. Nothing changes. In fact, if I take you back to,

28:07

you know, one of the GPT models and if you see the code, the code is the same. The story remains the same.

28:12

nothing changes, right? In fact, the APIs will remain very, very similar.

28:17

You just have to change client equal to GROC and make it client equal to open AI. That is the only thing

28:24

that will happen. Otherwise, all the ideas that we have talked about will remain the same. And within the

28:31

messages, you will actually write your prompt. So that will be like role system, system message,

28:35

role user user message. That will also be the same. So, one part of what I'm trying to cover is,

28:42

that this is very platform agnostic. It doesn't matter which kind of API provider you're using,

28:48

which model you are using. The way you are calling the APIs is very, very similar. Right.

28:56

So then what are the differences? How do you choose which model is better and how do you make those choices?

29:01

Well, there are different benchmarks available. So what happens is in the world of large language models.

29:07

There are, there are many, many benchmarks that you have. So there is something called the MMLU benchmark.

29:12

MMLU benchmark stands for the massive multilingual understanding benchmark.

29:16

It is a very, very popular benchmark that is used for, you know, evaluating the

29:21

the reasoning ability of language models. Let me open this link to all for all of you, just to show you

29:27

what this thing is. I'm just going to open this link for everybody.

29:32

Just so that everybody understands what this benchmark is. So this is the MMLU benchmark.

29:36

You can also Google out and you can check, okay. You can actually Google out and you can check this.

29:40

this is the MMLU stands for massive multilingual understanding and these are standardized

29:45

benchmark designed to evaluate the intelligence factual knowledge and problem solving

29:49

abilities of LLMs these are the kind of benchmarks that you will use in practice to evaluate the

29:56

quality of your language model and remember you will you will have these discussions many times

30:03

in your team in your projects with your customers and they will ask you that please tell

30:06

me tell us why did you use a particular model and see until up and

30:10

until now in the course we are not talking about costs because you don't have to bear any

30:14

costs right all these APIs we are using is a free API but in a real project when you the

30:19

moment you are using the open AI platform or other kinds of API providers you have to pay for

30:24

it there will be a real cost involved and whenever the costing aspects come in then your clients

30:32

and your customers will ask you that please tell us why did you choose model a compared to model

30:36

B if both the models are giving reasonably similar answers

30:40

then why will the customer pay 10 times more cost because all these models are charging you based

30:46

on tokens right i told you i talked about it token cost right there's an input token cost there's

30:50

an output token cost so the more powerful the model the more the cost so these are some

30:56

robust benchmarks on the basis of which you can you can evaluate you can evaluate the large language

31:03

models right you've got mmlu benchmark you've got swee benchmark right if i have to give you a couple of

31:09

important benchmarks no i can i can kind of

31:10

of go on and on but there is mMLU which stands for multilingual uh language understanding

31:16

benchmark you can see and you can you can take a look at it what is the benchmark basically what is

31:20

the meaning of a benchmark a benchmark basically means that it is like a question paper think of a

31:25

benchmark like a question paper so there are like 57 distinct subjects spanning stem

31:31

humanity social sciences professional fields law ethics all that it's like a question paper

31:36

and next time whenever any large language model is released there

31:40

they will have to solve that question paper it is quite literally uh let's say that i design a

31:46

question paper and i will evaluate you like how at masai we conduct examinations for students right

31:51

so we will design an examination with multiple choice format and each one of you in this class

31:55

will have to take that exam and you can see that these questions are given in an mcq format

32:00

designed to mimic human style examinations and you will go and ask these questions to your

32:06

LLMs. So on one hand you have a Gemini model sitting on one desk. You've got a GPT model

32:13

sitting on one desk and you've got a the Anthropic Cloud model sitting on one desk and quite

32:18

literally they take the exam. Like when I say take the exam, I mean you're basically giving the

32:22

questions as input and you're seeing what responses they generate. This is actually how LLM

32:26

evaluation happens, you know. And there are like you can see the latest benchmark what it is

32:33

and you can take a look at it. You can kind of

32:36

go and take a look at the you know the rankings and other things you can you can see right

32:42

you can if you want to go a little deeper and understand what this benchmark is you can see you can

32:47

and this is a comprehensive list of all available tasks like you can see high school

32:51

european history business ethics clinical knowledge this is just for your information you don't

32:55

have to memorize it but it's important to know right it's important to know these are all the available

33:00

benchmarks remember i was telling you what are the benchmark these are all benchmarks

33:03

so next time you have this question that sir please tell me which model is better which

33:08

you have to look at these benchmarks you cannot just say oh you know your gpt model is better because

33:13

i think i like it you like it based on what you know we are not like we have to give answers back by data

33:19

when you say data this is data so you have a i'm going a little bit beyond the curriculum right now because

33:26

these are some things i feel you should know we don't have it explicitly covered here but i think

33:30

i wanted to actually talk about it because we are we have met

33:33

quite some progress into lLMs and we are using different lLMs and i'm taking the liberty of

33:39

getting into this because today is actually very simple open source models is just a very simple

33:43

demo we have so i wanted to take the remainder of the time and you know talk about some of these things

33:47

so that you know what is it and and and you know the moment you start venturing into different

33:53

different types of language models this question will come now we have seen grog models most of you

33:58

in the class you're using lama 70 billion model uh some of you might be

34:03

using open a i gpt models some of you are using cloud models and this question will arise

34:08

that how do i take a call i can see the cost differences cost comparison we can do because

34:13

it is already published opening i will tell you that how much they are charging for the gpt model

34:17

but how do you how can you really gauge the performance differences so it is very

34:22

important that you understand these benchmarks so you can go to this particular site i can i think

34:27

i can ping this to all of you and you can take a look at it just for fun you can maybe understand more about

34:33

how they do it how they evaluate so there are like a series of questions on virology

34:37

econometrics college computer science high school biology you can just get an understanding

34:41

like how these things are framed these are like

34:44

general questions 57 different subjects very broad and you're really testing the language

34:51

model on all sorts of capabilities i don't think any human being in the class in

34:56

i don't know if there's any human being in the world who knows everything this well so you're

35:00

basically evaluating the language model based on every single aspect

35:03

so which is like incredible okay so this is one kind of benchmark helaswag is another benchmark

35:09

it is designed to evaluate language models uh common sense reasoning through sentence

35:14

completion tasks these are all like you know question papers you can think of okay then there is

35:19

a helaswag is also good then you know bbhs is also quite good this is again a general knowledge and reasoning

35:25

benchmark it's called big bench hard right it consists comprises 23 challenging big bench tasks where

35:32

prior model evaluations have not outperform the average human raters and you can see some of these

35:38

questions you can actually take a look at some of these general kinds of questions like bullion

35:41

expressions you know this is the kind of uh uh questions that we used to solve in our college and school

35:48

days no like these are a typical iat kind of questions that they will be asking and like humans have not

35:54

performed that well so they are trying to see how lLMs are doing and this is how they will rate

35:59

another very very popular uh you know benchmark in this space is uh a r

36:02

rc is also the irc is not listed herec is actually very good

36:07

a rc is also a reasoning benchmark it consists of 8 000 multiple choice questions from science

36:12

exams from grades three to nine we have all taken these exams but you're you're

36:16

you're basically evaluating the language model on it how how well it performs

36:21

so this is based on general knowledge reasoning right general reasoning general

36:24

understanding specifically you know with respect to math there is a there are two specific

36:31

benchmarks which are extremely popular this is one of the best benchmarks out there this is

36:35

called g s m 8k you don't have to remember it okay i have any way ping the link you can use it for your

36:40

reference okay and you can see there are like 1,319 grade school math world world problems

36:47

so very interesting you can actually see and if you want to see some other kinds of

36:51

questions you can read the papers the original papers are also listed here this is the original

36:56

pdf like where they actually list out the kind of questions that they have given

37:01

it's a big one but you don't have to like you can see you can see you can actually kind of

37:06

take a look at it you know you can take a look at it like um it doesn't look very difficult but

37:13

i think you you you get the idea right you you get the idea what type of what type of questions are

37:18

there this is the data set variety is there difficulty level is given to you so you can actually

37:23

take a look at it in in case people are interested in reading these are fairly like

37:27

detailed things we are discussing here but just in case if you're curious you can see what kind of

37:31

kind of questions are there and how we are evaluating the models okay this

37:34

take mrs limb milk sir cows twice a day well it's actually quite advanced even a normal

37:41

human being you and i if i asked you to solve it up pen and paper

37:44

you'll have to remember right there's so many computations to be done like twice a day

37:50

okay yesterday morning she got 68 gallons of milk okay in the evening she got this money

37:55

morning she got 18 fewer after selling some gallons left with only 24 gallons how much was a

38:01

the revenue if the gallon cost 3.5 so you have to do quite a bit can you see so these are

38:06

the kind of questions on which you're evaluating language models a correct answer

38:10

you will ask the llm to solve it you will see what the language model is predicting

38:17

not only that you will also see its reasoning it's just like how a how a teacher will correct you

38:23

and and based on that the ratings are given so this is like another very very popular

38:27

benchmark the gsm and there is something called math Q&A

38:30

math QA is also a very very good benchmark it's a large-scale

38:34

benchmark you can see English word problems are given this is on probability

38:39

geometry and much broader domain is there one very very popular

38:46

benchmark with respect to code which is what we are all doing right code

38:51

code specific benchmark the code there is something called

38:54

this human evil human evil is very popular for code

39:00

Human benchmark is a data set designed to evaluate an LLM's code generation capabilities.

39:06

And this completely depends on your application.

39:08

If your application is more into the coding front, let's say you want to,

39:12

you're a tester in a company, a lot of people working in the development team and

39:17

you know software development, you are going to use language models to write test cases.

39:24

So then how do you decide,

39:25

that what do you use can't?

39:27

Baki so all of it, prompt, write a system, user, all that's true.

39:30

we are discussing but how do you at least make that first baseline choice

39:33

that let's start with this model so these are a kind of benchmarks you will actually rely on

39:37

otherwise you know it is like a it is like an ocean there are like thousands of

39:42

models if you come if you include open source there's an entire universe out there and

39:47

today i will show you a moment i introduce olama to you you will realize that like there are

39:51

so thousands of models you can theoretically use how will you choose which one is better

39:56

so this is the human eval benchmark that you have you can take a look at it

40:00

Another very interesting benchmark is called truthful QA.

40:06

This is very interesting for evaluating truthfulness and safety.

40:10

So this assesses accuracy of language model in answering questions truthfully, very interesting.

40:16

So, you know, I mean, it's like you can read about it.

40:21

The questions target common misconceptions that some humans would falsely answer

40:27

due to false belief or misconception.

40:30

And this could be like, you know, a very interesting question could be, like, nutrition

40:36

how you know, but now,

40:37

you're a nutrition question, we'll ask you, maybe, maybe we have a misconception about something,

40:42

that egg may cause disease, like if I ask you that, okay, does egg cause cancer?

40:47

I'm just giving an example. Maybe a human expert might say, hey, yes, it does,

40:50

because that's their misconception, that's their belief. It's not grounded on facts.

40:56

But this data set is primarily checking the truthfulness.

41:00

this is also an important thing.

41:02

If you want to build an application that is going to give users answers to factual questions,

41:09

be it health, be it nutrition on a broad range of topics.

41:12

So truthful Q&Deka benchmark is also important.

41:16

Right?

41:16

So this is a very, very popular data set for that.

41:19

Squad is also very, squad or drop, don't know.

41:21

Squad and drop are very good for reading comprehensions, reading and Q question answering.

41:26

This is a general reading comprehension capabilities, right?

41:28

Like, what do you say?

41:31

You know, we have all done these kinds of reading comprehension questions in our school days, right?

41:38

I remember we started this maybe, I don't know, five, six, class five, six,

41:43

we're going to give it a small paragraph, and after the paragraph, there'll be like two or three questions,

41:49

and they will, it'll ask you, okay, in this paragraph, what was talked about?

41:54

They will ask you some questions, okay, what happened on this day, fill in the blanks,

41:58

reading comprehension. So they are testing primarily on the model's language understanding

42:03

capabilities. There's no other knowledge that we are testing. And reading comprehension is a very

42:08

different capability. And if you take a look at it, all these benchmarks are testing slightly different

42:15

capabilities of the models. Just reading comprehension carnekele. You don't need to know too much about

42:19

history, geography, economics. You have to have good comprehension ability.

42:24

Joe paragraphs somewhere can we read that paragraph. Can I understand what is being conveyed and can I

42:28

answer questions based on that. So it's very different skill, right? And same is the drop data set.

42:33

You can see the drop, sorry, the drop benchmark is also very similar.

42:36

Evaluate languages advanced reasoning capabilities through complex question answering, just like

42:41

reading comprehension. And finally, there is the agent and tool use, which we haven't talked about

42:48

in detail, but there is something called tool bench. Toolbench is there. So these are some of the

42:52

general benchmarks that are there, I would say. Right. So just to kind of kind of,

42:58

summarize. This is what I wanted to summarize for all of you. I've got this small notes,

43:03

which, you know, these are some of the things I covered. But you can just make a note of it. Like,

43:07

this is exhaustive. You don't have everything listed here on DPVL. DPVL focuses on the most common

43:11

ones. But this is a very exhaustive set of benchmarks that you have across different tasks. Okay.

43:19

And one very nice link I wanted to share with you, which you can use to reference. This is

43:28

this one very interesting and it gives you a

43:32

it gives you a list of different different language models you know

43:35

you can actually get a very nice visualization of different language models and all

43:39

okay so yeah you can actually read about it this particular thing about different

43:46

models and all that up you have paper sat there so this is the thing okay

43:50

let me ping this link to all of you now

43:58

Moving on. So these are all important things to be kept in mind, right?

44:04

Whenever we are accessing models, whenever we are using a GPD model, whenever we are using an

44:08

anthropic cloud model, whenever we are using a Gemini model, these are all things that we have to

44:13

keep in mind. These are all paid providers. You have to pay for the API and then you can get

44:18

access to the model. What was GROC? GROC is also a cloud platform. Here also we were getting

44:26

the models. Here here be GROC, we did not have to download anything. So we just took an API

44:31

key for free and up to a certain token usage we are using it. This is what we have done in our

44:35

session so far, right? We are using GROC. So what are these platforms? These platforms are like,

44:43

think of it like they are massive servers. They are like massive computing infrastructures or massive

44:49

servers, wherever a server say. And inside that, these models are downloaded and hosted.

44:56

It means inside the GROC, you can think of GROC as like, you can think of GROC as something

45:02

like this. This is like GROQ. This is what we have been using all this Y. And you can see GROC has

45:11

the Lama models hosted inside it. It has the, it has the Cuen models hosted inside it. So all

45:21

these models are hosted inside GROC. And it's, and these, and these, and these,

45:26

These models are massive. Like for example, the 70 billion parameter model that you're seeing

45:31

on the screen. I already told you, I introduced this briefly in the first session, I told you at a very

45:38

high level that the number of parameters tells you something about the complexity of the model.

45:44

The model in the model that much of complexity the model has, right? The more the number of

45:50

parameters, the more the complexity. We have seen that, right? So generally a model with more number of parameters is

45:56

usually more complex. So 70 billion parameter model is usually very powerful. And it is,

46:01

it is worth 70 gb in size. Just to load that model, you will require 70 gigs of RAM. And I'll demo this

46:07

live in the class today. When I come to Olamma, I'm just coming to that conversation now. But I feel this

46:12

context setting is very important because all this while we are using GROC and I wanted to build this perspective

46:17

so that people appreciate why it is so difficult to do this locally. All these platforms are charging you,

46:26

Actually, GROC will also charge you, but a GROC is giving you free up to a limit.

46:30

But these platforms are spending a tremendous amount of money to keep the hardware running.

46:35

It's the machine. You have to keep the machine running. There is cooling involved.

46:40

The machines get heated up. So Peter to throw it. It'll heat over. Imagine these servers,

46:45

they are like hundreds and gigabytes of RAM and GPUs that are running. Imagine the amount of money

46:51

that is spent on cooling. Amount of money spent on networking, physical infrastructure. It goes into

46:56

millions and billions of dollars right so somebody has to pay for it we are getting the

47:00

convenience our convenience we are simply taking an API key from grok and open AI and we are making an

47:07

API call getting a response request response the story is the API thing that we talked about last

47:11

session last session is all about API right request response you you you in the prompt you send a

47:17

rest API request you get a JSON response back that's it that's it we are not having to worry about you know

47:22

where it is hosted and what is the machine is the machine is the machine uh going

47:26

down will they be a downtime tomorrow.

47:28

tomorrow.

47:28

That is not our worry.

47:31

All that these companies are taking care.

47:33

They are infrastructure providers.

47:36

Right?

47:37

That is one thing to be kept in mind.

47:40

Now, the important thing is

47:42

what is the concern with these platforms?

47:49

So one thing we are talking about is these platforms.

47:53

And they make life easy.

47:56

Because we are getting the convenience.

48:01

You can make an API call and you get a response.

48:03

It's fast.

48:04

And it's also cheap.

48:07

But the pay as you go.

48:08

It's like pay as you go.

48:12

A good example I can give you with let's say Netflix.

48:15

If I give you two options,

48:18

that download the entire library.

48:21

I mean, okay, if you want to watch a movie,

48:24

you have $50,000.

48:25

Give me $50,000.

48:26

50,000 rupees, I'll give you the entire library.

48:29

That is option number one.

48:30

Option number two is you pay

48:32

$199 per month subscription in Netflix.

48:36

My name is 200 rupees.

48:38

And Netflix will, you can watch whatever as you want

48:39

as how you want.

48:41

Subscription based.

48:43

You're not downloading anything.

48:44

It's on the cloud.

48:46

So it's convenience, right?

48:47

I don't have to go through the hassle of paying

48:50

so much of money upfront

48:51

and downloading it in my system.

48:55

All the movies in my system.

48:56

system because it's the hassle.

48:58

So many files, how do I manage?

49:00

I have to take care of the whole thing.

49:01

And that too, I'm making such a high upfront investment.

49:05

Not a good model.

49:07

What is the better model?

49:08

I'll pay Netflix as in when I use it, subscription-based.

49:12

API concept, whatever we talked about, GROC and all,

49:16

they are also like a subscription-based model.

49:19

As much you're using it, you are paying them.

49:21

If you're using more tokens, you're paying them more.

49:23

If you're not using the API,

49:25

okay, you're not paying any.

49:26

think. Fair enough. So this feels like a very convenient option. Now the question is,

49:33

why are we then talking about open source models? So our class as a Q

49:39

so all this is great. I'm talking about paid models, convenient option. Then why are we even

49:46

having this session? This session can't what? Open source model. Why are we talking about it?

49:50

Anybody? So definitely, there has to be some limitation of the paid providers.

49:56

open AI.

49:58

There has to be some limitation of the

50:01

API calls, right?

50:03

What is the limitation of an API call?

50:06

Anybody?

50:07

So far we are talking about the benefits.

50:10

Convenience. No upfront cost.

50:12

No hassle of hardware infrastructure.

50:15

That's all who's a headache.

50:17

I will just pay for the API, make a request, get a response.

50:20

That's it.

50:21

I save money. I save money. I save, I have convenience.

50:24

All is great.

50:26

So then what is the limitation of a typical API code?

50:31

Anybody.

50:34

Okay. Okay. Connection and data privacy?

50:37

Yes. Very good point.

50:42

Connection is a good point. Connection maybe, it's a pointer.

50:45

Maybe if you're looking at very, uh, extremely mission critical applications where you cannot afford

50:56

even a millisecond of delay, then connection is a good pointer good thing.

51:00

I think you're talking about from that perspective.

51:01

We're talking about edge AI, but the devices that are deployed on the, uh, AI that is deployed

51:07

on the devices.

51:08

If you look at use cases like self-driving cars and all.

51:12

You know, cell driving cards.

51:13

You know, cell driving cars, what is the Tesla got.

51:15

Tesla is not making an API call.

51:18

Tesla is not making an API call.

51:20

All the Tesla cars, all the cell grabbing cards.

51:23

The decisions are happening in literally, uh, microseconduble.

51:26

and nanoseconds. That is how quickly you have to make decisions. You know,

51:31

the models will have to make decisions that fast. And the moment you make an API call,

51:36

there is a certain amount of latency. We have talked about it, right? Latency. If you,

51:42

if you go to GROC also, you can see the logs and you will see there's a certain thing called latency.

51:48

What is latency guys? Latency means the amount of time you, it takes to get a response. So you're sending a

51:55

a JSON request and you get a JSON response back. That entire cycle time is what we call

52:00

latency. And there is bound to be a delay. The fastest of the fastest platforms, there will be a delay.

52:08

And the more tokens you're sending, the more your input tokens, that means it's taking more time

52:14

to get sent because you're going to network. You're getting sending in a network, right?

52:18

Understand that. Your open AI servers, your GROC servers are

52:25

are they are not in the same premises. Your open AI and GROC servers are in a completely

52:30

different network. They are like in USA. I am sitting here in India. You're all in India, right? And the GROC

52:37

server and the open AI servers are in America. So my, when I make an API call, API call,

52:43

I'm taking that prompt, that JSON and I'm sending a request, rest API call. That entire JSON

52:49

is sent from India to America. That's quite literally that's happening on the network.

52:53

where you are not that is so that it's making that entire trip the processing is happening on

53:00

america server because model is there and it is sending the jason response back from america

53:04

back to india that is what's going on so there's a lot of latency involved you can see that round

53:10

trip is going to take a lot of time now one second two second you may not appreciate it the more

53:18

the bigger your tokens the more your tokens the more your tokens the like you will actually start to

53:23

feel that impact, especially for mission critical applications. I told you cell driving cars.

53:28

Self driving cars, look. It is all on-premise. We use a term called on-premise. What is the

53:33

meaning of on-premise? On-premise basically means that everything is hosted on the device. Everything

53:38

is hosted inside the Tesla cars. His GPU is there. His models are also hosted there. All the processing

53:45

happens on device. So one aspect is the latency. And the second aspect as Gourtheg has also nice.

53:53

mentioned is data privacy. Privacy is a huge thing.

54:00

See, so far for our demos, we are not that concerned about privacy because we are trying to learn

54:03

the topics, right? But if you look at it from a

54:08

financial company or a health care company, if you look at it from that perspective.

54:17

Now, these enterprises are dealing with very confidential data.

54:22

Very confidential data.

54:23

Financial clients are dealing with, financial companies are dealing with customers' credit card data.

54:29

Customers bank account data. Customers personal data.

54:33

Banks have everything to know banks. Banks to find out of you. Everything has to be known. Everything has to be known.

54:39

In fact, banks, banks will, ideally know more about you than any other business.

54:44

Because banks have, it comes to money, right? Like, banks will know more about you than any other business out there.

54:51

Because it's about money.

54:52

next time you want to take a loan, banks will take every other, every information about you.

54:56

Everything. Validated and third party very verified. That is a very confidential amount of data.

55:02

Remember, when you're making the API call, let's say you're the bank.

55:06

Okay, you're the bank. Let's say you are ICICI bank. So if you are ICICA bank, one second, guys,

55:12

where is my cursor? If you're ICICI bank, you're a data scientist working at ICA bank.

55:21

okay. This is your VS code. You're doing all the development in your VS code.

55:27

IPYNB file, joe, right? And this guy, the developer at ICACA bank, he or she writes a prompt, right?

55:35

He or she writes a prompt and they are making an API call. The moment they do that, the moment they do an API call,

55:41

remember, they are sending that entire prompt outside the ICICA bank servers.

55:46

That bank is out of bank. It's that actually, that data is actually going to

55:51

American servers, open AI, and then they are getting the response back. So that is a huge breach of

55:56

privacy. So security is a massive issue. Whenever we are talking about paid models, this is a very

56:01

important thing you have to keep in mind. Security. Security is to some extent limited.

56:08

Okay, so security goes for a toss. So there are solutions around that. Just say, I can, I can show

56:21

you instead of talking about it, I can show you. So there are, there are solutions about

56:26

solutions around it. So just say we can actually use Azure.

56:31

Now, I'm, sir, sir, I'm open AI trust. Because open AI is a startup company. It's not even

56:37

a publicly listed company. And I was nothing is out in the public domain. It's still a private

56:42

company. It's a startup. It's a startup. So it's one of the world's most valuable startup, but it's still

56:46

a startup, right? So the question is how do you trust it? How do you trust it? How do you trust a company that

56:51

not publicly listed. And we are talking about normal humans, right? Look at enterprises.

56:56

There are companies which are bigger than the valuation of open AI. We're talking about massive gigantic

57:01

companies up Pepsi low, Coca-Cola low. You look at these massive behemots uniliver. These are massive

57:07

FMCG companies. Look at their valuations. You look at Walmart. They are massive companies, right?

57:15

What is opening I compared to them? Right? Nothing. So why will these companies?

57:21

companies trust open AI. Why will Walmart send their data to open AI servers?

57:25

So what is the alternative? Cloud platforms come in. You go to cloud. Now again, I don't, I want to make it a very broad

57:34

discussion so that people know a lot of things today. Microsoft Azure is basically a cloud platform.

57:40

Inside that you have something called foundry. Inside Microsoft Azure, there is something called

57:45

foundry. And if you go inside foundry, let me see if it opens up.

57:51

I had this resource created. I wanted to show you. Just briefly I wanted to show you.

57:56

Huh, it comes up nicely. When you go inside Foundry, you will actually be able to

58:03

use the models inside Azure. You don't have to make an API called directly to Open AI.

58:11

But whatever we were doing so far, you know, we were actually, like for example, let's say, I want to

58:16

use a GPT, you know, GPT for model, GPT for Omni model.

58:19

one option is that I will have to do client equal to open AI and I will use open AI's API keys.

58:27

So like this, I'm sending my data to open AI servers. Security goes for a toss.

58:33

Open AI can't data go in network. But what is the other option?

58:40

The other option is, just give me one second. I wanted to show this to all of you.

58:47

Some sign-in issue, I think.

58:49

Ha, yeah. The other option is, I can go to Microsoft Foundry and I have an extensive list of models.

59:01

There is nothing that it doesn't have. So, what I'm getting at is companies trust cloud more.

59:09

If you're a Walmart, so we have done engagements with Walmart. Actually, Walmart uses Microsoft Azure in a big way.

59:16

Walmart uses Azure in a big way.

59:19

they will trust Azure.

59:21

So what will their generative AI developers and all that do?

59:25

They will not directly call the open AI API.

59:27

This use not.

59:28

But they will basically create a deployment on Azure.

59:32

They will basically deploy a model on Azure.

59:34

There is everything.

59:35

There's nothing you don't have.

59:37

You've got GPT models.

59:38

You've got deep seek models, open source models.

59:42

All this is there.

59:44

And the best part is they are all hosted on Azure.

59:46

Azure is like an infrastructure.

59:47

It's a cloud, right?

59:49

So again, the convenience angle is coming in.

59:51

But Azure is giving you that balance of privacy also to some extent.

59:55

It's a balance of privacy.

59:57

Again, I'm not saying it's completely secure.

59:59

Here also the Azure instance can be hosted somewhere.

1:0:02

But maybe this is hosted in America.

1:0:05

This is not exactly hosted in here in the same premises.

1:0:08

If you're ICICA bank, like whatever models you're using even on Azure is not whole, but it's

1:0:13

still safer because, you know, there's a trust associated with Azure.

1:0:17

And there are a lot of enterprises which are already on Azure.

1:0:19

So they find it easier to use the models on Azure.

1:0:23

And I wanted to let you know, again, something I was covering in the discussion before,

1:0:30

the way you call, the way you call the models is exactly the same.

1:0:37

Kuch for a difference.

1:0:38

Okay.

1:0:38

Now, foundry's home in let me show you here.

1:0:41

Now, look, look, you take a look at it.

1:0:44

I've deployed a GPD 5.4 nano model.

1:0:48

And you get a similar playground.

1:0:49

No, there's no further.

1:0:51

This is our open AI's playground.

1:0:53

System message, user message, I can write all this.

1:0:55

This is my Azure GPT playground.

1:0:58

This is, so what I've done is I've deployed a GPT model.

1:1:01

That means this GPT model is present inside Azure.

1:1:03

And I can ask a question.

1:1:05

You are an AI assistant helps to find information.

1:1:07

Okay.

1:1:07

Or be both sort of things.

1:1:08

These things we don't know right now.

1:1:10

Tools and all we will discuss later on.

1:1:12

These are agent related things.

1:1:13

You have ignored.

1:1:14

This is system message.

1:1:15

And this is user message.

1:1:17

What is the?

1:1:19

whether usually in India.

1:1:22

This is your question is.

1:1:23

This is your user message.

1:1:26

You see, the assistant's answer will.

1:1:28

And the best part is, you know, the best part is, I wanted to show the code to all of you.

1:1:33

When you see the code, there is an option.

1:1:37

The moment you see the code, if you look at the code, this is call model.

1:1:41

If you click on call model, you'll look on call model, you'll see code digger.

1:1:44

Just observe this for a minute.

1:1:46

I will copy the code.

1:1:47

I will copy the code.

1:1:49

show the code to all of you.

1:1:52

Yeah.

1:1:54

One second.

1:1:57

Here it goes.

1:1:58

This is the code.

1:2:00

This is the code.

1:2:02

Can you see?

1:2:03

Very similar.

1:2:05

Very similar.

1:2:07

It's almost like what we have been doing all this while.

1:2:10

Nothing changes.

1:2:14

You can see.

1:2:15

Import open AI.

1:2:17

It is using the same open AI.

1:2:19

API.

1:2:20

Just we're open AI API here use here.

1:2:22

We are using the same open AI API here.

1:2:23

Right?

1:2:24

And we are using something called client responses create.

1:2:28

It's similar to chat completions.

1:2:30

And you can see the only thing is that we're giving Azure specific things.

1:2:33

Azure endpoint, Azure API.

1:2:35

And this is the thing.

1:2:37

Okay?

1:2:38

This is the thing.

1:2:39

What is the capital of France?

1:2:40

The idea remains the same.

1:2:42

So this is what it is basically.

1:2:44

Enterprises are effectively more confident.

1:2:47

More confident.

1:2:48

More confident.

1:2:49

I would say on this thing.

1:2:52

So, this is just something all of you should, all of you should know, okay?

1:2:56

Now, so just to come back to our conversation,

1:3:00

why are we talking about, sorry, let me open up the notes.

1:3:05

Just to come back to our conversation, why are we talking about open source models?

1:3:10

Why local LLMs?

1:3:12

Local LLMs because they are safe.

1:3:16

Here, in a cloud LLM, what we are doing, we are sending.

1:3:19

the prompt. This is the story I talked about so far. You're sending the prompt. And as you send

1:3:25

the prompt, it is sent to a LLM, sorry, it is sent to a GROC, an open AI platform, Azure platform,

1:3:37

like I'm here on here on here on Azure platform. All that is happening. And based on that,

1:3:41

you're getting a response. That's what's going on. And there are multiple good things about it.

1:3:48

What are the good things we talked about?

1:3:49

already, convenience, all that. But remember you're paying per token cost. Sometimes the cost

1:3:55

can also be high. Sometimes the cost can also be high. The benefits are as follows. Access powerful

1:4:03

models, no local hardware, pay per usage, subscription based. But the disadvantage is this. Data goes to remote servers.

1:4:14

On the right hand side, we have local LLM. You run the model locally on your machine.

1:4:19

It sounds nice, but then as I told you, you have to have to have a very, very powerful

1:4:31

infrastructure to keep it running. What are the benefits, many? No per token cost. You no longer

1:4:39

have to pay a per token cost. But you might think as if you're saving money, but at a very small scale,

1:4:47

you will see that the headache is far too much. Because you still have to buy that hardware

1:4:52

or upfront investment you have to do. It works offline. It works even without an internet connection.

1:4:58

Maximum privacy. Maximum privacy, but you get full control over your data. These are some of

1:5:04

the benefits of using local LLMs. And a very popular platform for using local LLMs is Olamma. And we will

1:5:12

see that. And we will see the process of downloading Olamma. I will show you how this is. How

1:5:17

this is we will see. So just keep this at the back of your mind what is cloud versus what is

1:5:23

local. So wanted to take some time to explain the differences. I hope everyone is clear. So there is

1:5:32

Olamma for you. You can go to Olamma download. You can download Olamma. I've already done it for you

1:5:37

because it's a big download. It's a big download. It takes a while to download this 1.3, 1.4 gb download is

1:5:44

there. And it's a very simple installation.

1:5:47

Next, next, next, simple install is there.

1:5:50

And after you do this, what you do is, you validate whether Olamma is installed or not.

1:5:56

Let us do that.

1:5:58

Let us validate whether Olamma is installed or not.

1:6:01

So what I will do, I will come to my Windows PowerShell and I will type Olama version.

1:6:08

This is a quick way to check the Olama services running.

1:6:11

If you're on a Windows machine, you can go to the bottom right and you can actually see that

1:6:15

in the task part that symbol is coming. This is actually a different screen I have. So

1:6:21

usually you will see this here. Just here you will see those icons, right? All the applications

1:6:27

which are running, you will see Olama. There's a small, like the typical Olama icon will come. You'll see

1:6:31

an icon like this. That means the Windows service is running. It's like a window service.

1:6:37

Startup tray in, you know, Windows service. Okay. What else you can do? You can do something called

1:6:44

Olama list will list out all the models that you have downloaded.

1:6:52

All the models that you have downloaded will be part of the Olama list.

1:6:57

All the models that you have downloaded will be part of the Olama list.

1:7:03

Now in my session, I have already downloaded one model. I will download another model and show you.

1:7:08

So I've a basic model downloaded downloaded. What is that? When 2.5, it's only a point.

1:7:14

5 billion parameter model or approximately up they accept you that if it's a 0.5 billion, it's

1:7:21

roughly 0.5 gb that is the rough scale. So 0.5 billion, it's like saying 1 billion is to 1 gb.

1:7:29

Think of it. That is a rough approximate scale of the size. So if you have a model which is let's say

1:7:34

500 billion parameter, it's approximately 500 gb. That is Olamas's approximate scale. Now you will ask me

1:7:43

me, sir, how are models available? What? How do we know that? Well, you can go to

1:7:48

olama.com. You can please go to olama.com and you can go to the model section. And the model section

1:7:55

will give you an idea about all the available models that are there. All the available open source

1:8:01

models are there. And guys, let me again repeat. This is completely open source models. These are

1:8:07

freely downloadable. You can download can download in the Ollama platform and you can work with it.

1:8:13

show you some demos on that as well right now. So all the major Chinese models are there.

1:8:17

Just a minimax. Minimax is a very popular Chinese model. Kimi, Kimi is a by Moonshot AI.

1:8:25

This is a Chinese company. So Kimi K2.7, very good model. These are Gemma 4 is by Google. Google usually is known for the Gemini models. Gemini paid models. You can only access Gemini using an API.

1:8:39

Gemma 4 is Google's open source equivalent. This is more like a community service.

1:8:47

You know, it is like, how do I say? This is like corporate social responsibility.

1:8:51

All the big companies, they will also have some open source models.

1:8:54

Kuch publicly that is that. These are not at the same capability as Gemini, but they are decent.

1:9:00

They are good models. Okay. So Jemma is that. Quain is another open source model by Ali Papa.

1:9:06

I'm talking about some of the popular names here. There are hundreds.

1:9:09

But these are some of the more popular ones. This is NVDA's Nemotron. This is also like it's, it's actually like a very new one.

1:9:17

NVDA is also getting deep into the space. Nemotron 3 you can look up. Okay.

1:9:23

And Minimax we talked about. And obviously the deep seek, where is deep seek? If you scroll down, you will have the deep seek family of models. This is deep seek version 4. It was released two months back. It is an absolute amazing model. But it is massive.

1:9:37

If you look at deep seek, it's massive. Mistral.

1:9:39

Mistral AI is a French company. This is Mistral's flagship model.

1:9:43

Mistral 3.5. And if you come a little bit down, you will see Lama 4.

1:9:50

Lama is also there. And very interesting. GPT OSS is open AI's open weights model.

1:9:55

Open AI is again known for the GPT models, right? The GPT models, you have to access.

1:10:01

You have to access the GPT models using an API, right? There is no way you can download it. But open AI gives you

1:10:09

gives you another set of open source models that you can access freely. And that is GPT OSS.

1:10:16

You can access it through Olama. So whatever open source models are there in the universe, all the open source

1:10:21

models you will find in Olamma. Plus minor some things because, you know, Olamma adds it later on.

1:10:27

First it comes in the original model page, then comes in Olam. Olam is a separate company. But yeah,

1:10:32

majorly you will find all the models available here. Okay. So that's that. And I was talking about deep C.

1:10:39

you can go to any one of the models let's say if you click on deep seek version four pro you will

1:10:44

find for each of these models there are different different versions there are many many versions of

1:10:47

these models available there is a deep seek version four and you can take a look at it the models

1:10:54

what are the models we have all these you'll be able to us see okay the one that in the class right now

1:11:01

is uh where is that just a second where was my model uh yeah the one

1:11:09

that I downloaded in fact is Quen 2.5. Quen 2.5 upna model. Let me show you that particular model.

1:11:16

Our focus area, Quen 2.5. This is my model. And let me open it up.

1:11:25

This is our model 0.5p. And you can see this was this is not new. This was updated a year back.

1:11:31

One year is too longer time in today's world. I think so much that has changed. Quen has already released 3.5.

1:11:36

But that's okay. It's good enough for a demo. It's a very small model.

1:11:39

so it will take a very less amount of space and the whole idea of please remember we are all

1:11:45

working on our laptops so these models are not supposed to run it's not meant to be run on laptops but then

1:11:53

yes if you absolutely want to if you absolutely want to if you absolutely want to try if you absolutely

1:11:57

want to demo these are options that are given to you but as i as i said something that gets the job

1:12:01

done but love you don't need it's see it's like saying um

1:12:09

a very powerful language model is like a brilliant guy, a really super high IQ guy.

1:12:14

No, we need. We have two plus two.

1:12:18

Now super brilliant man like what can do? You ask a class 10 guy or you ask a

1:12:23

absolutely brilliant super high IQ guy, that's the two plus two.

1:12:26

The job will be. So a lot depends on the kind of problem that you're trying to solve.

1:12:31

Sometimes even the simplest of models will give the same results.

1:12:35

It is not that if you use a very powerful model answer,

1:12:38

something else will. No, an analogy is simple. If it's a very simple task, then anybody can solve it.

1:12:46

At the end of the day, it depends on evaluation, the benchmarks that I was talking about. You have to

1:12:50

evaluate based on the benchmarks. And that's a very long discussion. I just wanted to make you aware,

1:12:55

but that's a very long thing that you have to explore and you have to see and a large part of it is based on

1:12:59

projects, okay, but just something to be aware of. So Quen's a kaffi varieties, variants. There is 0.5 billion, there is 1.5 billion,

1:13:06

there is even a 72 billion parameter model. Guess what will be the size of this?

1:13:11

Kittan size will be? Here the size limits are given to you. Approximately 47 Gb. Massive. There's no way

1:13:17

we can download it. We can download it. If I try to do it, my windows will crash. I have, I have how much of

1:13:23

available RAM? I think I have, uh, let me see. Um, where is that? Sorry. I think I have. I think I have. I

1:13:36

got around around 16 gb of available ram. I don't have GPU on this machine. So 16

1:13:45

gb in 10 gb model up to 9 I can definitely use but not up to 32. Right. So that's that's one way

1:13:53

to look at it. That is a good question good take. Not necessarily. Other Vram here. But even

1:14:01

if you don't have it, they will run on community hardware. If you have it, it will be faster. But it is not

1:14:06

it is Olama doesn't mandate that you have to use GPUs. It's not mandated. Okay.

1:14:11

Yeah, that is just one thing to keep in mind. All right. Now, uh, okay, moving on.

1:14:25

As I told you, I've already downloaded the coin 2.5 billion parameter model. And what I wanted to do is,

1:14:33

I wanted to download another model in the class just to show you a small demo.

1:14:36

model. Okay, deep seek. Deep seek. Okay. Deep seek. Okay.

1:14:41

Deep seek. Let's go to deep seek. And I will go back to the very first version of deep seek that was

1:14:46

released. Deep seek version one. Sorry, yeah, deep seek R one. The reasoning model. This is what was

1:14:52

released. If I remember the date right, this was January 2025. Last year, 2025 when deep seek was

1:15:00

launched. It says updated 12 months back. Update, I mean, update, but deep seek was officially launched in

1:15:05

the first version of Deepseek officially released in January 2025. If you remember. And I will

1:15:13

take this model, 5.2 gb. This will go. 5.2 gb in machine in. I will take this model. It's quite a

1:15:20

decent model. And maybe I can even try this one, 9GB. No, I'll not try because I'm on videos on

1:15:27

Zoom. It will take a lot of space. But okay, I'll try this one. And what I will do is, what is the

1:15:31

command to download it? How to download it? You will have to do, let me copy this

1:15:35

model. Let me copy this. This all the commands there are. Don't worry. All this is given to you

1:15:41

in our notes, which we'll share. So Olama list, I showed you Olama list. And the one that we will do

1:15:47

right now is we'll do Olama pull. We'll pull. We'll say Olama pull. Ola ma pull is to download the model.

1:15:52

Olam is to run the model. That's it. So what we will do right now is Olam. Ola ma pull.

1:16:05

And remember, I've already copied that deep seek model.

1:16:09

This is what I will do. It will take a while to download.

1:16:14

Okay? It'll take a while to download. Oh my God. It's going to take this much time?

1:16:22

No, I think it should be fast. Let's see. Ah, yeah, it's not this is weak. Yeah, it'll

1:16:30

download. And this is just process.

1:16:35

I wanted to share with you how the how to download a life on premise. I'm doing it on my local

1:16:42

machine. Yeah, Colap's no scene. Whatever I'm showing you.

1:16:48

Up today.

1:16:50

Clearly on my BS code I'm showing you today. The idea is the same. Concepts we are the same.

1:16:54

Client chat completions create. Nothing will change. But I wanted to show you all these demos

1:17:01

local and cloud both on BS code. Just to give you one more flavor.

1:17:05

okay so guys uh we can take a short break take a take a tea break water break

1:17:16

i think it'll take five minutes for it to get downloaded let's take a short tea break and let's

1:17:21

circle back and we'll continue on okay i'll keep my screen on so yeah let's take it and come back

1:17:27

after the break we'll continue on with olama we will discuss how to call that model how to go to my

1:17:35

how to configure how to use so far we are just taking the model but how do we use it

1:17:42

and we will also discuss a few other related concepts like olama cloud and all that you will see that okay

1:17:46

all right so let's take a short break and

1:18:05

you know.

1:18:35

You know,

1:19:05

You know

1:19:35

I'm

1:20:05

I'm

1:20:35

I'm

1:21:05

I'm

1:21:35

I'm

1:22:05

I'm

1:22:35

I'm

1:23:05

I'm

1:23:07

Thank you.

1:23:37

Thank you.

1:24:07

Thank you.

1:24:37

Thank you.

1:25:07

Thank you.

1:25:37

Thank you.

1:26:07

Okay, guys, welcome back all of you.

1:26:24

Yeah, so you can actually see that it's still continuing on.

1:26:30

That's okay, no problem.

1:26:31

I think I'll continue on and let us see.

1:26:35

Let us see.

1:26:36

I'll allow this model to

1:26:37

like get downloaded. So we will see. And in the meantime, you know, we can continue on with

1:26:44

our our demos, our discussion. So none of that changes, but this is the model that is getting

1:26:49

downloaded already. So let us see. Let's wait for that to happen. And let me in the meantime

1:26:57

continue on to the other discussions. How do we use the model? So it's not a problem.

1:27:07

We already have a model. That's why I wanted to keep it downloaded. I knew we will learn into these issues.

1:27:11

Sometimes the speed will reduce increased. You can see it's gone back to 1.7 MbPS. It's more on the Olama server.

1:27:17

server. There's no issue with my connection. My connection is absolutely fine. So,

1:27:21

you think, sir, this speed can come here. Basically because there are thousands of people who are trying to access the model, something to do with the availability of the server. So all that is also there.

1:27:33

So yeah, anyways. Now, let us continue.

1:27:37

on. Yeah, I will, I will come on video in case it still creates a problem. Let me know.

1:27:45

Yeah. But I think because I'm downloading, maybe the video might start a little. But as long as you guys can hear me, fine, it's okay.

1:27:52

So, let's continue on. So now the question is, all these are the different, different models that we have, right? I think from a theory perspective, as I discussed, this Olama pull.

1:28:07

So what we are doing right now is Olama pull.

1:28:09

That we'll run again. We have not run the model as of now.

1:28:13

We have only, we have only done Olamma pull.

1:28:16

But we have not run the model. So the next step that we will do is we will do Olama run.

1:28:20

We'll next step we'll do. And this is the broad way you can compare.

1:28:24

Right. So you can compare a 0.5 billion parameter model, one billion parameter model, which is slightly more powerful.

1:28:32

This is slightly more powerful. But remember, more powerful models will have, will require more

1:28:37

am. Okay, so this is a very broad difference between a small and a large model. I think

1:28:42

we have talked enough about it. If you have a very small model, yes, it gets the job done. It's cheaper.

1:28:47

It's easier to store. If you want to run it locally with what we are, you know, primarily what is

1:28:53

the agenda for our session, local models. So smaller models are easier. Just like 0.5 billion model run. It's

1:28:59

very simple. You know, it's easy to download, easy to run and very fast. The biggest thing will be

1:29:04

latency, fast speed. Even on my machine, it will be very fast.

1:29:07

Very fast. See, I don't have GPU, right? My system, I don't have GPU. I, so it's, so this is a, you know, I have a Zen book duo. Okay. So this is like I don't have a GPU. It's integrated graphics basically. But yeah, I mean, it's a fairly good processor. Ultra 7 and also is a very good processor. But yeah, the GPU is just shared. But my point is, you can take a look at it. You can compare that when I

1:29:36

when I load the model, when I, so what am I, what am I basically doing here? I'm downloading the model.

1:29:44

I'm basically downloading the model. If you see, that is what's going on. I'm basically downloading the model.

1:29:48

Now, after the model gets downloaded, after the model gets downloaded, after the model gets downloaded, I will use this model.

1:29:58

Same story. There, Open AI was hosting that platform where I was sending the prompt processing was happening, was happening.

1:30:06

here and I was getting a response. So what matters now is where is the processing happening? Processing will

1:30:12

happen on my local host. Local host means my system. So now you send the prompt, system message, user message. The processing

1:30:21

will happen on your local host machine and then the response will be sent. That's what I'm talking about.

1:30:26

You know processing here, the processing time will be a lot less for small models. So that is one important thing to run.

1:30:35

fast inference.

1:30:37

Yeah, look, fast inference.

1:30:39

Like, it's a 0.5 billion parameter, what I will be demoing to you.

1:30:43

It will be super fast.

1:30:44

I will send the prompt.

1:30:45

I'll instantly get the answer.

1:30:47

Even though I don't have a very powerful machine, it's not powerful by modern standards.

1:30:51

Nothing.

1:30:51

My system is nothing compared to modern standards.

1:30:55

So fast inference.

1:30:56

And large models, it will be very slow.

1:30:59

And hopefully I'll demo this to you.

1:31:02

But the one that I am downloading is a large,

1:31:04

I'm a fairly large model.

1:31:08

Billion parameter model that is like, it's fairly good big.

1:31:11

It's more than 10 more than 10 times.

1:31:13

Yeah, 0.5 billion and 8 billion.

1:31:15

It's more than 10 times. It's more than 10 times actually.

1:31:18

It's a big model, huge model.

1:31:19

Comparatively, 10 times the size.

1:31:21

We will, we will demonstrate that.

1:31:23

So, um, let us see how to do this.

1:31:29

How to, how to, how to, uh, call Olamma from Python.

1:31:34

Right?

1:31:34

We will see how.

1:31:34

to call Olamma from Python. I'll just show the code. Then I think after this

1:31:37

completes I'll demo the whole suite to you. I will go to my local Vs code. I've already got a folder

1:31:43

created today. And here, I have demo.op. IP by NB. I'll do this all on Vs code today. I will

1:31:50

open up my Vs code and everyone can see that you all worked on Vs code. I know for a long time we have

1:32:00

not used it, but we come back to it again. We'll see this again today.

1:32:04

This is a simple way you can call the Olama model that is installed locally in your system.

1:32:13

Now, you look at the code and tell me, is it anything different that we have learned?

1:32:20

And I wanted to show you how strikingly similar it is.

1:32:23

It's the same thing. It's the same thing.

1:32:25

Only difference is, we here client equal to GROC, we are doing client equal to open AI.

1:32:30

Because Olama, OLAMA APIs are compatible with open AI.

1:32:34

That is one great thing. And, you know, many providers, many companies are making their APIs compatible with Open AI.

1:32:42

Because Open AI is one of the pioneers. A lot of companies have a lot of legacy code, which is similar to opening eye.

1:32:51

And I, what I'm saying, guys, if you're not following, if you're just, if you click on the code section, look at this, client chat completion's create.

1:33:04

can you see? Even GROC follows the open AI standard.

1:33:09

Whatever we have been doing in GROC, was the code any different? If I go to the playground,

1:33:14

all that we have been discussing so far if you click on the view code, OE client, chant

1:33:18

completions create. Nothing changes. The same open AI standard. What I'm saying is even Olama

1:33:24

follows that same standard. Olama also follows that exact same standard. All you do is you say client

1:33:30

equal to open AI. You specify what is the, uh, you specify what is the, uh,

1:33:34

the port number and the server where the, where the Olam model is hosted on.

1:33:40

So this is local host. Local host means my machine. This is, this is my machine. This is my machine.

1:33:46

This is where OLA, the model is hosted. And you will say client chat completions create,

1:33:51

model equal to model name. Whatever model is already downloaded. It will automatically read that.

1:33:57

So in in GROC, we had to say model equal to Lama versatile, whatever, right? Here we will say model equal to

1:34:03

whatever we have downloaded. Joe we have downloaded only that I can use. And right now,

1:34:07

if you remember, in my Olama list, my downloaded model is only this one. After I download this,

1:34:13

I will show this demo also. So right now, I will specify this on my downloaded model.

1:34:19

Message is equal to role user role system. That story remains the same. So the point is to tell you

1:34:25

that it runs the exact same way. But there is nothing new to teach you here. This is the same thing.

1:34:29

The same story we have discussed all this file. The new addition is that, okay, we install something.

1:34:33

something locally and Olama is running on a certain port number.

1:34:36

Because Olama is a service. It's an application that you installed.

1:34:41

Whenever you install any application on Windows, it runs on some port number. So this is the

1:34:45

port number by default where it is running. Or you can you can check all the applications running

1:34:51

on the port numbers and you will be seeing this is the Olam application. This is the default.

1:34:55

And this is all that you have to do. So I already pre-executed the code and you are able to see

1:35:00

when I pre-executed the code you are able to see that this is able to see that this is

1:35:03

is the response I get which is fairly fast the same thing I can do using this method

1:35:12

also this is this is another way we can do the same thing this is a similar kind of code we can

1:35:16

write just to clarify this is a similar kind of code we can write just wanted to let you

1:35:20

know the code remains very very similar the similar kind of code we can write here also

1:35:25

very similar okay so uh so uh

1:35:33

yeah so here it is a slightly different i mean it looks a little different but you can just take a

1:35:38

look at the code here all if you can see uh so i can run the code because my Olama service is

1:35:43

already running although this is getting downloaded this we are this we are downloading

1:35:47

right now although we are downloading this but uh like the Olama service is still active

1:35:51

right so I can still I can still program programmatically invoke the model I can use from Olam

1:35:59

import chat this is a slightly different way we are doing it the code looks a little different I'm

1:36:03

to show this also but i i don't personally prefer this i don't prefer this because the code

1:36:08

looks a little different if you see this code this looks like okay something a little different in the

1:36:12

syntax this is native olama syntax i i don't prefer this but i just shown this to you but what i prefer

1:36:17

is this the second one that i showed you this is that all familiar chat completion's API so you can

1:36:22

literally take all the code snippets which i shared with you all the code snippets until now

1:36:27

wherever we have used groc API uh you know instead of grok client equal to grok you make it client equal to open a i

1:36:33

this go and just change the name of the model after you download open uh so all the demos

1:36:38

you can literally do in your vS code today okay and you can run the code you can see the results i'm getting

1:36:43

i'm connecting to the uh olama model which i've already downloaded user message here

1:36:47

system message i've not given if you can give that also and this is the response i'm getting super

1:36:51

fast right how much time did it take super fast yeah we can still debate on the latency i think that we

1:36:55

can still debate yes you can still say no sir i think it took some time but yes as i told you like

1:37:00

this is something that you have to like the more powerful your machine you know it will it will run

1:37:05

faster but you can take a look at it right this is how we can call open source models the next

1:37:11

discussion i wanted to have with you and this is still downloading okay after this completes

1:37:15

this will be the last demo i will show you how the you know the performance of the deep seek model

1:37:19

like that is a little slow and all i will show that to you okay you will get a feel for it

1:37:23

latency party will be seen okay now the next part of my discussion i want to focus on

1:37:32

something called a dot env files so this is what we covered we talked about calling olama from python

1:37:36

we looked at that thing how do we call a local model from python using the same chat

1:37:41

completion's uh API okay so we talked about that and also just to clarify there is also something

1:37:46

called olama cloud okay so there is something called olama cloud also that you have

1:37:51

what is olama cloud oama cloud also that you have what is olama cloud

1:37:52

allama cloud is just like grok so now what we have talked about is there is an inference provider

1:38:02

called grok this is this is what we have generally talked about in our sessions this free

1:38:06

platform where you can sign in you can create an API key we can do chat

1:38:11

completions create and we can access it this is what we have talked about Olama cloud

1:38:16

is exactly the same thing there is zero difference so Olamma gives you two flavors

1:38:20

one you can download the models locally like what i'm showing you right now this is the

1:38:50

yeah so uh yeah i think it just slows down a little at times that's okay

1:39:04

so olama cloud is exactly the same as grok there is absolutely zero difference between what is olama cloud

1:39:11

and grok so grok was this platform which was hosting all these open source models and we can create an

1:39:17

API key we can connect get a response the story remains the same for olama

1:39:20

cloud olama cloud maybe you can you can you can sign into olama just say i have signed in

1:39:24

you can you can go to olama dot com you can sign in same way you can go there and you can access

1:39:32

olama cloud exactly the same way okay you can access olama cloud exactly the same way you can see

1:39:38

start local scale with cloud so it gives you both the flavors so olama gives you both the flavors

1:39:43

olama says okay we give you a local option we can download it locally you can download your

1:39:48

models locally okay so that is something you can do and we also give you something called

1:39:53

olama cloud and with the cloud what you can do you can like have an API key and now you don't

1:39:59

have to worry about hosting the models locally downloading it like the same trouble that we are

1:40:04

facing it takes an amount of time to download it is using a pima system RAM and and don't forget

1:40:11

about the machine heating up all these language models are taking are are doing a tremendous amount

1:40:15

of processing we don't get to realize it like in all these classes that we have done all that you're

1:40:23

doing is tk you're sending a prompt you're making a API call and you're getting a response

1:40:30

you are not appreciating the processing that is going on and and do you realize now up

1:40:36

here just wanted to make you aware we are talking about a seven billion

1:40:41

eight billion parameter model it is already taking five gb of RAM

1:40:45

what were we using in our grok all through the classes 70 billion can you estimate the amount of

1:40:50

gb ram it is taking imagine how much of heat will be produced when you're running this even on a single

1:40:56

request i mean if some of you have played games on your laptops and PCs you will typically

1:41:02

hear that fan speed and you know those are real things when you're you know uh

1:41:06

using large language models on your laptops it's also a lot of fun i mean i have i have a separate

1:41:12

PC where i do this word development work this is a more um portable PC i use but yeah but that's

1:41:20

another thing you if you have a workstation it's it's a lot of fun but coming back to our discussion

1:41:28

olama cloud you can access it from here you can go to olama dot com that is the same uh link that i gave you can go to

1:41:41

olama.com and you can go to something called API keys you can create an API key you can

1:41:46

go to settings and you can absolutely create API keys up here API keys create

1:41:51

API keys create and all the models that are available locally are also majorly available on the

1:41:59

cloud most of the models are there on the cloud also who you can go to the model section it is listed

1:42:04

that which are available locally which are on the cloud so if you want only the cloud models

1:42:08

all these are anyways free to download all the models you can download

1:42:11

you can download. Olama at its code is a local platform. The story that we are discussing

1:42:17

today. This is local primarily. The cloud is one part of it. If you want a cloud variant, if you want to

1:42:25

access only the cloud model, like GROC in GROC has selected only a list of models it has hosted.

1:42:33

Because these are very costly right. Each of these models are hundreds of GPs in size GROC

1:42:37

now host everything. It will go bankrupt right. So similarly OLAMA also it cannot host

1:42:41

host all the models. It has selected some of the most popular models.

1:42:44

Like Mini Max Kaliya, Gemma 4 by Google, Quain by Alibaba. It has taken some of these more popular

1:42:51

models. You will have DeepSeek version 4, very popular model. GPT OSS by Open AI. This is open

1:42:56

AI is an open source model. It has taken some of these popular models and it has hosted it

1:43:00

locally. Hosted it on the cloud. Now, look, here here cloud. How do you access it? Very simple.

1:43:07

Very similar to Rock. No difference client chat completions create. The

1:43:11

story remains the same. I will show the code to you. The only thing is that you have to go to

1:43:15

settings and you have to API key to be same way. You have to create the API key. Go to the key

1:43:22

section you have to basically create the key. You have to create the API key. Same way you have to do it.

1:43:28

Right. And once you have the API key, you can work with it. Okay. That is that is the way. That is

1:43:34

basically what Olama Cloud is just like rock. Now,

1:43:41

The next thing that I want to discuss in my class is, I want to talk about a concept of a dot ENV file.

1:43:48

This is something very different and we have not seen this before. If you remember in all our sessions,

1:43:56

we have primarily talked about, we have primarily talked about this, what you call, the secrets,

1:44:07

Collab Secrets. That was in the Cloud Collab.

1:44:11

that we're looking at, okay? Let me give you a slightly different flavor today.

1:44:16

What I will do, I will have an ENV file today, okay? I will create an ENV file today. I will create a

1:44:24

sample dummy folder to show you the ENV setup and all that that I will do. Okay, so I will create an ENV

1:44:29

file today. And an ENV file will look somewhat like this. You will do new. You will just create a text file.

1:44:41

And you will call it dot ENV. This is quite literally how an ENV file looks like.

1:44:46

That's it. You will just enter it like this. Dot ENV. And this is what an that's it. That's it. It's a text file.

1:44:56

Now question is, sir, this can't the rake. What do I keep inside it? Okay. Let's come to that. You will go there and you will store your GROC API key.

1:45:05

Open with notepad. I will store my GROC underscore API underscore K.

1:45:11

key. Everybody remembers we were doing this in Collab Secrets. So whatever we were doing in Collab Secrets,

1:45:16

that becomes my ENB filing local. Because I told you, today's class is entirely on BS code. I'm doing it

1:45:22

everything locally today. So whatever we were, because see, like some of you might say, okay, sir, why don't you,

1:45:30

why don't you save the API keys on the notebook itself? Because then that is not confidential, right? If I have to

1:45:35

give you the class perspective, see, all these are free of course. I know, but.

1:45:41

If I give you the class perspective, I'm taking a session with you.

1:45:44

Now, we're what we're going?

1:45:45

Now, if I put my API keys on the Jupita notebook, all those keys ends up getting shared, right?

1:45:54

And the same happens with customers also, clients also, projects also.

1:45:58

If your project has some API keys and if you share that with your team and all, that becomes a problem.

1:46:03

That's a password, right? And it's a very costly resources, right?

1:46:07

So, you know what you know, who is using how it is getting used? It's very costly.

1:46:11

So you, so this is a standard way to store any kind of environment variables, configuration

1:46:20

files, passwords, any kind of credentials and all, we use ENV files for that.

1:46:27

Just like how we were doing it in Collap Secrets, this is like your ENV file.

1:46:31

There are other ways to do it like JSON files and config files, but this is a standard we are seeing

1:46:35

in this class today, ENV. And how will you do it? You will just go to your grok.

1:46:40

You know, GROP in everybody created the API key.

1:46:43

You can take it from Collab Secrets. I can give you one workaround.

1:46:46

What you can do is you can go to Collab.

1:46:48

Collab in Secrets, go to go to Collab in Secrets, go, it to copy and then down it.

1:46:51

Okay, so you can take it from your Collab secrets.

1:46:54

So GROP in the whole not be.

1:46:55

It will be something like GSC, something like this.

1:46:57

This, you have to type it out.

1:47:01

You have to type it out.

1:47:01

This GSC, something, something, W, H, whatever that stuff will be.

1:47:04

Okay, so much of your API key.

1:47:06

Okay, so much of your API key for GROC.

1:47:09

Done.

1:47:10

it. Similarly, you will also create Olama underscore API underscore key. The story remains the same.

1:47:19

This we can co-lab in fact, in a collab maybe we've been made. In fact, here in

1:47:22

call it. Idea remains the same. I told you the same way that I'm calling GROC using an API

1:47:28

key, I will also call Olama using an API key. Remember Olama cloud. If Olamma local

1:47:34

there is no API key, you require. API key is only to access Olama Cloud.

1:47:40

Because local you are anyways downloading it locally and using it, right?

1:47:43

This is only to access Olama, the models which are on the Olama cloud.

1:47:47

API keys are only for cloud access.

1:47:50

GROC is hosting the models. You want to access that.

1:47:53

Olama cloud is hosting the models. You want to access those cloud models.

1:47:58

If your Olama models are already downloaded, like what we are trying to do is still downloading.

1:48:02

If it's already downloaded, then you don't have to do anything.

1:48:05

Which, no, that's the idea.

1:48:09

Okay?

1:48:10

All right. So anyways, this is how we will create the ENV file. I hope everybody is clear.

1:48:20

Once that is done, you go back to the VS code and this is what you will have to do.

1:48:27

Now look here, this is our working directory. I will just go ahead and open up the working directory.

1:48:33

You have our working directory. And in that working directory, I have my ENV file.

1:48:37

The same ENV file which I created. I just created one more.

1:48:40

and here, I, this is how it looks like.

1:48:45

You will have to use this command, load underscore dot env.

1:48:52

But remember, you have to do pip install.

1:48:54

.env first.

1:48:56

Okay, so there are a couple of pip installs you will have to do.

1:48:59

And this is the main command.

1:49:01

Load underscore.

1:49:02

.

1:49:03

Moment you do that, in your current working directory, whatever is the ENV file will be automatically loaded.

1:49:09

And there is the ENV file will be automatically loaded.

1:49:10

it is client equal to GROC. All this while we've been doing GROC API calls using our

1:49:15

collab. This is the first time we are doing a GROC API call using BS code.

1:49:20

Anything changes? No, nothing changes. Story remains the same. We just run.

1:49:24

There's no change. See this all of you. Okay? Running. No problem.

1:49:33

Oh, ANV may go. GROC API key fetched answer. Let me run it again. Can you see? Same way.

1:49:40

This is calling the GROC model. Lama, 70 billion versatile.

1:49:44

Obviously, I cannot download this model in my laptop.

1:49:47

Our $10 billion is download now.

1:49:50

70 billion what will show you?

1:49:52

Right.

1:49:53

But you can see, I don't have to worry about all this powerful model.

1:49:59

It's hosted in GROC.

1:50:01

The main takeaway is that here we are not, we are saving the GROC API key in the ENV file.

1:50:08

I'm not exposing the API key.

1:50:10

There you can say API underscore key equal to, you can do that.

1:50:14

You can do that. You can, you can, you can, you can, you can, you can do that, but then this is the other way to look at it. Okay, yeah.

1:50:23

But it, you know, it will not be confidential. That's one way to look at it. That's the reason why we don't do it.

1:50:28

Hi, I mean, Gurtig, absolutely, you can use JSON file, YAML file. A. JASANX is there. Dot INI is another way to do it.

1:50:36

Okay, dot ENV is just popular because it's the simplest key equal to value format.

1:50:40

If you ask me, sir, why is it so popular?

1:50:43

Because it follows just like a simple key equal to value format.

1:50:46

Now, JSON will, then you have you, you know, it's like, it's just like people's preference.

1:50:54

You can do it with a JSON also. You can do it with the JSON also.

1:50:57

You can do it with the JSON also. You can do it with the JSON also. You can't just, you know, it's what it is.

1:51:02

I mean, it's just a equal to format, say, it's what it's. But you, so oftentimes YAML files are also used.

1:51:07

Often times JSON is also used.

1:51:09

the concept remains the same.

1:51:11

Ultimately, this is like a key value.

1:51:13

Your, like, secret name or secret value is, that key is your key, it, that idea is the concept is important.

1:51:20

Whichever way you store it is, even, is a very popular format, usually.

1:51:25

Okay, and this is how the code looks like. I hope everybody is aligned.

1:51:28

Everybody is able to see. This is very, very familiar code.

1:51:31

Everything is familiar. The only new thing we are adding in the code is this. That is it.

1:51:34

There is nothing else that is new in the code.

1:51:37

Or this pooh-upata, we all.

1:51:39

Second demo I will show you.

1:51:41

Just I told you, GROC is very similar to Olama Cloud.

1:51:46

And, uh, we allama's local demo we already saw.

1:51:50

Olamas local demo was also the same.

1:51:51

Nothing, right?

1:51:52

I downloaded my model and I was, I'm pointing to the Olama where the model is downloaded, the port number.

1:52:00

And I'm simply using the same client chat completions create.

1:52:03

Same story.

1:52:05

And now the final option.

1:52:08

We have seen all.

1:52:09

the flavors today, right? And the final flavor is Olam Cloud.

1:52:13

Olama Cloud to call can. Let us see that.

1:52:16

Guys, let me just close my video. I wanted to show you this demo before the class ends.

1:52:19

I don't know why it's stuck. Let me see if I can, just give me one second.

1:52:23

Yeah. It was stucky-y-o-gia.

1:52:28

I guess.

1:52:31

Just give me one second.

1:52:39

Ah, yeah, my internet connection is very good.

1:52:42

Yeah, it's nice, definitely a server issue at Olamma's end.

1:52:46

Yeah, I was just cross-checking that.

1:52:50

Okay, I think that's okay.

1:52:56

So moving on, the final demo that we will see is, the final demo that we will see is Olama Cloud.

1:53:03

Like I told you, I already created the Ollama API key, Olama key we created key we created. I created

1:53:09

and now same way I will do dot ENV and from that dot ENV file I will get the

1:53:15

Olama API key and the same way I can use client equal to open AI well syntax and you can do it.

1:53:21

I was using the same client equal to open AI here.

1:53:24

Now look here here here client equal to grog because I was calling the GROC model and here I was

1:53:29

doing client equal to open AI because I was calling the Olama local model, Olama local

1:53:34

be client equal to open a say we were doing base URL API key and Olamma cloud cloud also

1:53:39

so I'm using the same client equal to open AI API key base URL story remains the same.

1:53:44

Or API key, how's how are it? Am I hard coding?

1:53:45

You can hardcode it also, mind you, it's a string.

1:53:50

But we are saying OS dot get ENV, get ENV,

1:53:54

get ENV, meant the environment variable you have loaded, because we have done dot ENV, right?

1:53:58

We have loading the ENV file and whatever ENV file we have loaded, we are getting that

1:54:03

ENV file, get ENV, get that and fetch the OLMA API value from there.

1:54:09

That's string. Remember, we saved the string there.

1:54:13

We said OLAMA API equal to. So we are fetching that value.

1:54:17

That is how I'm instantiating the client. And this is the same story.

1:54:21

Nothing to talk about here. Client chat completions create, model equal to messages.

1:54:26

You know, I can run the code because I already have it set up. I can run the code. I can show you.

1:54:30

Same way we run it. Look, VS code may. It's going to OLAMA. It's making the call.

1:54:35

It's giving a response back to me, request response. This is not running locally.

1:54:39

It's locally not going.

1:54:41

So we have seen both the flavors today.

1:54:43

This is your cloud model.

1:54:45

Cloud made the API call, give a response.

1:54:48

And this is, OLAMA gives you a free tier.

1:54:51

You might be wondering, is it the same as GROC?

1:54:53

Yeah, it's very similar to GROC.

1:54:55

But it's kind of your free tier, a free tier.

1:54:58

So you can see its usage, how you usage, how it resets in two hours.

1:55:03

And it gives you reasonable capabilities.

1:55:05

Just like Grog, this is also fairly good.

1:55:07

Fairly good.

1:55:08

And it's very new, actually.

1:55:09

Actually, Olamas cloud platform is fairly new.

1:55:13

GROC has been there for a longer time.

1:55:16

That's why in the classes, in the sessions, we started with majorly GROC,

1:55:19

because GROC is more renowned and much faster, actually.

1:55:22

Honestly, if you ask me, GROC is faster.

1:55:23

It's better.

1:55:25

I think the answer was in front of you.

1:55:28

Answer, up in front of you.

1:55:30

I was running a 70 billion parameter model.

1:55:33

Now count it.

1:55:33

Same query, same system message, same user message, okay?

1:55:38

Look at the amount of time.

1:55:39

I took to get a response.

1:55:40

And this is only a 20 billion parameter model.

1:55:43

It's one third the size.

1:55:45

And same prompt and CD amount of time it took to give a response.

1:55:49

And you can compare.

1:55:50

Now check it.

1:55:52

1, 2, 3. 3.

1:55:54

Now, 10 seconds in under answer.

1:55:56

Okay, you can see Grog is renowned for its speed.

1:55:59

That's latency for you.

1:56:01

And you can do the same thing here.

1:56:02

1, 2, 3, 4, 5, 6, 6.

1:56:09

7, 8, 9, 10, 10, the second.

1:56:16

The answer is in front of you.

1:56:17

So, Olamma is much slower.

1:56:19

So, GROC is in fact renowned for its speed.

1:56:20

If you Google out a little bit of GROC,

1:56:23

GROC is one of the fastest inference platforms out there.

1:56:26

A much more powerful model, it took less than three seconds to give me the answer,

1:56:31

whereas Olamma took 10 seconds.

1:56:32

So these are some things you need to be aware of.

1:56:34

I'm not saying you need to know everything in detail,

1:56:36

but these are things you should have to consider.

1:56:38

When you're building real solutions, you will have to consider these things also.

1:56:41

The same model, we're paying, but what are we getting for it?

1:56:45

What are we getting for the model that we are buying and whatever we are choosing?

1:56:50

Benchmarks was one aspect.

1:56:52

Cloud was one aspect that we talked about.

1:56:55

When to consider what?

1:56:57

When to consider local.

1:56:58

So these are all very, very important things you will have to keep in mind.

1:57:04

Okay.

1:57:06

Okay, guys, I think.

1:57:08

Let us go back to the discussion. I think, yeah, this is pretty much what we have today overall.

1:57:21

And again, the main agenda for the session as I talked about today was about, we started the conversation today with respect to the concept of what is, what is the concept of benchmarks.

1:57:38

compare different models because there are so many local models. There are so many open source

1:57:41

LLMs that we have. So we talked about that particular concept. How do we compare? What are the different

1:57:48

benchmarks that are there? That was a bit of a different topic. It's not in the contents, but that's

1:57:53

something we talked about. Very important to know that. Then we went into cloud models and local models

1:57:58

comparison. When to use local, when to use cloud. We talked about pros and cons. The main consideration for

1:58:06

for us today for using the cloud models was what? What was the main consideration?

1:58:10

The main consideration for using the cloud models was we wanted to. So the, so the main thing was that

1:58:15

we wanted something which is, we wanted something which is secure. So that when you're sending

1:58:22

a prompt, when you're making an API call, it stays secure in my platform. So security was a big

1:58:28

aspect. So we looked at Olamma. We looked at installation. We, you know, I'm still trying to,

1:58:36

download this, but thankfully I already had another model downloaded. So I was able to show you

1:58:39

a demo. But this is a real challenge. You will also have to try it out in your home and it will take

1:58:44

time to download the models. Okay. So we talked about Olamma, how to download, how to pull,

1:58:49

how to run the models in Python. We saw the programmatic chat completion from Python.

1:58:56

And most importantly, we saw what is Olamma Cloud. Just as we discussed GROC. We also saw

1:59:01

OLAMA Cloud and we were also able to store the credentials using an ENV file.

1:59:06

So using an ENV file, we were able to store the credentials. So that is another thing that we did.

1:59:11

And just remember, this is just from a theoretical perspective, because we have not discussed Git and all

1:59:16

that. Git is not part of our thing right now. But just remember, like the ENV file is, you can, of course,

1:59:22

save your credentials in an ENV file, but when you're actually checking this into a code repository,

1:59:28

you will use Git ignore. When you do Git ignore, automatically ENV files are ignored.

1:59:32

So Gurtt-Gaast question that question, sir, why is ENV file preferred?

1:59:36

So that is one of the other reasons. So when you're using some of these, so you can explicitly

1:59:42

like add it, okay? So you're, so, so you can actually ignore the ENV files as well. So EnV gives

1:59:49

you a nice standard where it, you know, it can be ignored. So when you're actually uploading it on the

1:59:55

code repositories, you can ignore those things. You don't want to upload. It's like saying you don't

1:59:59

want to upload your ENV files on GitHub. You want to upload the rest of your code, everything, but the

2:0:03

the ENV you will not upload. So some of the automatic code repository platforms and all that you

2:0:10

have, they will take care of that. Okay. Yeah. It is commonly ignored basically. Okay. So if you add ENV2

2:0:20

dot Git ignore, it will usually ignore it. Okay, but that's a different conversation. So just be aware of that.

2:0:27

Okay. So this is pretty much what we talked about. I hope everybody's clear. Any questions anybody wants to ask me.

2:0:33

as part of today's session. Next session, we start off with a very interesting topic.

2:0:39

I think it's called rags retrieval augmented generation. Very, very exciting topic. We will see what rags are

2:0:45

and that's going to be our next discussion. We will see rags in detail what rags are and what retrieval

2:0:51

augmented generation is. And there'll be a series of sessions. Rag is not only one class.

2:0:56

We will have a series of multiple rag sessions. We are starting on rags on this session. So

2:1:04

this is the complete rag. One, two, three, four. So it makes you realize rag is so important.

2:1:09

So rag continues all the way until next to next week. So it is good in phases. So there's a lot of

2:1:15

things to talk about. We'll do it in phases. So we will see basics of rag, how to do

2:1:21

chunking, all that. So this is going to happen in phases in the classes. Okay. All right, guys.

2:1:29

I so hoped I would be able to show you the thing, but it is still going on. So that's okay. Not a,

2:1:33

not a thing. I will have Olama in my system. I think when we start the session next class, first thing,

2:1:38

I will show you this deep seek thing. I will have it in my system. Okay. But I think this will still take

2:1:43

some time to download. All right. Thank you so much, all of you. Any questions? Let's take another few minutes.

2:1:50

if you want to ask me anything. Anybody wants to ask me any questions?

2:2:07

All clear. Everybody was able to follow all that we covered today. Yeah. A lot of conceptual things,

2:2:15

lot of project-based things and I hope everybody got a good sense of what we covered.

2:2:20

about anything else you would like to ask anybody? Anything based on your work and your projects,

2:2:25

right? I think it depends on your GPU. How much GPU you have good take. So

2:2:34

how much parameter, you have to do a rough estimate. The model size will be displayed on

2:2:39

Olamma. When you go to Olamma, the model size will be displayed. You, like if seven billion

2:2:44

parameter model, how much size it will take will be displayed. A seven billion model is often four to

2:2:48

5GB. You have to look at after Windows is available. Windows itself takes so much of

2:2:53

memory, right? You have to see how much of V-Ram, GPU RAM is available. So,

2:2:57

on that basis, you have to estimate. You have to keep some two, three, GB RAM extra. That's the

2:3:02

that's the way to, you will have to do it. It's an estimation task. There's no like exact thing,

2:3:06

but it's a thumb rule, you know, you have, you know, yeah.

2:3:15

But basically whatever free capacity you have, you have to check that. Okay.

2:3:18

Okay, yes. Mostly it is the RAM. The processor will kind of impact the speed of the processing,

2:3:24

but mostly you need to have it in the memory. For the computations to happen, RAM,

2:3:27

I'm going to computer science basics, but it's like you have to hold that in the memory first.

2:3:33

Ultimately, where there storage has to be there. Processing is the next thing, obviously.

2:3:38

Processor will impact the speed of the computations, primarily. How many, like, like, like,

2:3:42

like, like, just like, 1.6 gigahertz. My machine has a very, very good processor, Ultra 7. Ultra 7 is the good one.

2:3:48

Now, Ultra 9, I'm not sure beyond Ultra 9 what has come.

2:3:52

When I purchased my Zen book, there was Ultra 9 also.

2:3:54

Right, so Ultra 7 is a good one. And I get a 3.6, 3.5 G8 Z thing.

2:4:03

So processor speed, clock speed also matters.

2:4:07

Okay. But ultimately, from a model perspective, how much your hardware can store, that is completely on the RAM.

2:4:18

Okay. Any other questions? And there are a few other things also good thing.

2:4:28

I did not want to get into all that today, but there is something called model quantization. Are there

2:4:33

ways to make things more efficient? Yes, there is something called quantization. So you can take the same

2:4:38

deep seek model and you can make it smaller. You can take a quantized version of the model.

2:4:43

There are a lot of those things also that matter. Those are things we will see in fine tuning later on.

2:4:48

but yeah. Is it okay? Yeah, okay? Okay. Any other questions?

2:4:59

Gurtega, I'll solve the questions today. Others, I hope, you are all clear.

2:5:06

Okay, so, uh, uh,

2:5:10

now, look, look, class is going to be, now speed pickup. But that's okay. This, this, I can show you, uh, next class.

2:5:18

Okay, thank you guys, uh, like, uh, yeah. So over to you, Pratap. Thank you. Yeah.

2:5:28

Yeah, sir. Thank you so much for another amazing lecture and especially thank you for covering the part of

2:5:35

benchmarks in detail. So yeah, yeah, thank you. All right. Uh, students, I will be releasing

2:5:42

the feedback goal now. And I have your mente-meter quiz as well. So, yeah.

2:5:48

Let's launch the feedback poll. Okay. The feedback pool should be live now. Please make sure you fill it.

2:6:01

Please make sure you fill the feedback poll. Once the feedback poll is done and I see that everyone is voted, then I will start the minty-meter course.

2:6:18

Okay, it seems everyone has voted.

2:6:32

Students, I've noticed that you guys don't feel the long answer. I mean, not everyone writes the long answer as well.

2:6:40

So if you can do that, that will be great. I will start the Mentimeter quiz now.

2:6:48

If possible, you can fill out the long answer as well. That would be appreciated.

2:7:18

All right, I will start in about 15 seconds.

2:7:24

So please join till that point.

2:7:48

You can also go to mente.com and just enter this code.

2:7:54

I'll also, you can also do that.

2:7:58

So Gurtig has his hand up.

2:8:05

Is there something you wanted to ask.

2:8:08

Okay, no problem.

2:8:11

Okay, no problem.

2:8:14

Okay.

2:8:16

Okay.

2:8:17

Fine.

2:8:18

I'll start seven players. Oh, someone dropped. Okay. All right, let's go.

2:8:31

Which command checks whether O-Lama is installed? So some of these questions are a little difficult, but they are mostly based on common sense. So let's see if you guys get it.

2:8:48

Yes, that's the correct answer, Olama version.

2:8:53

If you get an output out of that, then that means Olamma is installed.

2:9:16

Which command downloads model weights?

2:9:18

So this is something sir tried.

2:9:20

What was the command that sir used to download model weights from Olamma?

2:9:26

All right? Fairly simple, I feel.

2:9:32

Yes, the correct answer is actually Olamma pull because that downloads the model weights.

2:9:38

Olamar run or Olamas serve are for running the model actually.

2:9:43

So these two commands are used for running the model.

2:9:45

the model. Okay. Good job. Okay. Next question. Which file should never be committed. So out of these files, which file should never be committed. So out of these files, which file should never

2:10:15

go to a Git repo or rather it's fine if it goes to the Git repo but it should not go onto a public server basically.

2:10:25

What is a critical file here?

2:10:27

I think everyone will get that correct?

2:10:30

Yes, it's the ENV file.

2:10:32

EnV file contains all your API keys which you pay for.

2:10:36

So whoever has your API keys is basically having your credit card.

2:10:45

You pay for the tokens, but someone else will be using them.

2:10:49

You never know.

2:10:51

It's a very big risk.

2:10:53

All right.

2:10:55

Last two questions.

2:11:01

Why is local inference more private than cloud inference?

2:11:05

I think this one is a very easy question also.

2:11:11

Okay, maybe I would, I thought I put

2:11:15

difficult questions in this one. Maybe this was not the one. Okay. Oh, I forgot to close the poll.

2:11:23

Sorry, ending the poll now. I hope everyone was focused on the metameter quiz anyways.

2:11:34

So yeah, yeah, prompt stay on the left. That's the correct answer. I don't know why it took some of you guys very long to answer that.

2:11:45

All right.

2:11:47

Last question.

2:11:55

Which pair best captures local versus cloud tradeoff?

2:12:02

So the options are Git versus Python,

2:12:04

CLI versus comments, privacy versus stronger reasoning and JSON versus Mountaine.

2:12:09

Okay.

2:12:11

Yeah, okay.

2:12:12

I should have given you guys a little more tougher questions.

2:12:14

questions. Now that I read it, it's like, okay, this is too easy. Next time I'll give you tough questions then.

2:12:27

Okay, this is, this is quite easy guys. Come on. Yeah. Okay.

2:12:36

Huh? But okay. Okay. Sorry, I'm a little surprised. Um, look.

2:12:44

Local versus cloud trade off in terms of LLMs, right?

2:12:46

We have the, based on the topic that we have discussed in the class so far,

2:12:51

what is the, what is the, what is the comparison between local versus cloud?

2:12:58

So locals have better privacy and clouds have stronger reasoning.

2:13:03

Right?

2:13:04

Guys, I am getting confused.

2:13:08

Why did you guys click on these options, Git versus Python, JSON versus Markdown?

2:13:13

versus Markdown. What is that? I'm very confused. Local versus cloud, right?

2:13:22

Privacy versus stronger reasoning, obviously, because cloud models give you very high.

2:13:28

Okay, Gurtig is saying the voters were hallucinating. All right. But yeah, basically, the local model will give you a stronger privacy, obviously. But there is a very, very, very

2:13:43

good chance that it is not going to be able to give you stronger reasoning.

2:13:46

Right, you can't, GPD 5.5 and Claude Opus, I think, I don't know, 4.8 or something is there.

2:13:56

The myth, mythos, fable, all of those models.

2:13:59

You can't get the same kind of reasoning on a local model.

2:14:03

At least not at, not in today's date.

2:14:07

Maybe three, four years down the line, maybe you can.

2:14:10

Maybe next year you could, but right now that's not possible.

2:14:13

So, yeah, this is the correct answer.

2:14:17

Alright.

2:14:18

By the way, in the tutorial, maybe I'll try to show you guys like local models running and Gourteg, I'll try to answer your question.

2:14:34

But again, as Sir mentioned that it involves complicated terms like quantization and effective parameters and all those things.

2:14:43

things.

2:14:44

So it will be a difficult thing.

2:14:48

Okay, if you are aware of those things, then great.

2:14:52

Then I can just directly show you a demo without explaining too much in detail because otherwise

2:14:58

others will be getting confused.

2:15:02

And also there are tools available that are like that basically check your systems specs

2:15:10

and suggest models.

2:15:12

So that is one thing. Also, there is one more thing which is it's called offloading, CPU, GPU, GPU offloading.

2:15:25

So the idea is that since the whole model maybe the whole model is not able to fit in your GPU.

2:15:33

So you offload some of the non-working parts of that model from GPU RAM into your GPU.

2:15:42

CPU RAM.

2:15:43

Okay?

2:15:44

And this is something that is possible only with MOE type models.

2:15:48

So there are different different types of models.

2:15:51

And mainly there are two types of models that we are typically look into, which are dense models

2:15:57

and mixture of experts.

2:15:59

So mixture of expert models is what you can use this offloading trick on.

2:16:05

And when you do that, you can get like pretty decent size models on low RAM, as a lot.

2:16:12

as in low video RAM and pretty decent speed.

2:16:17

Not very high speed.

2:16:18

You will obviously not be able to compete with something like GPD5.5, but you can get decent speeds.

2:16:28

It feels like a toy.

2:16:30

TurboQuant is a different thing altogether.

2:16:33

TurboQuant has nothing to do with offloading or offloading or a mixture of experts or anything like

2:16:40

that.

2:16:41

VerboCont is a way to quantize.

2:16:43

So quantization is something that is a very big topic actually and needs to be covered like how needs

2:16:51

to have like a whole lecture dedicated for it.

2:16:54

I don't know if you guys will have it but maybe maybe once your course ends if you're very

2:17:00

curious about it, you can ask me on email and I'll try to explain it too.

2:17:06

Okay.

2:17:08

Not at the moment though because you guys should.

2:17:11

should focus on what is being taught right now in the course okay all right

2:17:16

with that I think I have I have talked a little over the time limit as usual so

2:17:23

congratulations to I I don't know how to say this and I will be ending the session okay

2:17:32

thank you guys for joining ah okay okay her priest is asking 16 Gb RAM 16 GBM is

2:17:41

video RAM or is it system RAM? Should I install it deep seek 8b model?

2:17:48

Deep seek 8b system RAM. System RAM would be too slow for any decent model, like for any decent

2:18:00

speed. So if you install anything on your system RAM, you can get it to run, but the speed will

2:18:08

be very slow because CPU is not meant to

2:18:11

for the type of computation that a GPU can do and system RAM is is difficult not difficult

2:18:23

it system RAM is a how do I say this system RAM cannot talk to GPU directly right so

2:18:33

because system RAM can't talk to GPU directly it will have to go through many layers and that will

2:18:41

slow it down 3066 gb mobile what are my options this is something that you

2:18:49

guys will need to have to run a particular tool I'll try to find the name of that tool but

2:18:54

basically that tool will look into your PC specs and identify which models you can

2:18:59

run obviously with mixture of experts and offloading there are more options many more options

2:19:06

but it's and it's actually very difficult for me to

2:19:11

just suggest models like that because every day there is a new model coming out pretty

2:19:17

much every day so yeah you guys will need to understand how to do the research and then do it yourself

2:19:26

unfortunately i'm sorry uh in any case i think i'll close the session now i don't want it to

2:19:35

get too over the time okay bye guys have a good night