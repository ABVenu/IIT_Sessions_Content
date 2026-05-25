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

Thank you.

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

Thank you

9:48

Thank you

10:18

Thank you

10:20

Thank you

10:22

Thank you

10:24

Thank you

10:26

Thank you

10:28

Thank you

10:30

Thank you

10:32

Thank you

10:34

Thank you

10:36

Thank you.

11:06

Thank you.

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

Thank you

15:06

Thank you

15:36

Thank you

15:38

Thank you

15:40

Thank you

15:42

Thank you

15:44

Thank you

15:46

Thank you

15:48

Thank you

15:50

Thank you

15:52

Thank you

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

Thank you.

18:54

Thank you.

19:24

Thank you.

19:54

Hi, welcome all of you. We'll be starting on.

19:59

I was waiting to allow everyone to join in.

20:07

Let's just take a minute forward and we'll start.

20:24

Thank you.

20:54

Thank you.

21:24

No, Akanshu, that is not the agenda for today. They will eventually be covered guardrails is a separate topic altogether that we will do later.

21:49

But today's agenda will be about rags, retrieval augmented generation, starter class.

21:54

We have multiple sessions on racks, and I'm starting with that. Yes, I'll just start with it.

21:59

But that's a separate class. Guard Brains and Responsibly, I have a separate session towards the end.

22:05

So we will talk about it later.

22:24

Thank you.

22:54

Thank you.

23:24

Thank you.

23:54

All right.

24:10

Once, once again, once again, I just go to start on here, and all of what we'll just go to start on here and all of you can, and all of you can see my street.

24:19

So this is pretty much going to be the agenda of what we will start on here and all of you can see my street. So this is pretty much going to be the agenda of what we will

24:24

be covering in today's session.

24:54

So we'll talk about rags today. Rags are a very, very interesting, interesting topic that we are, that we are going to be discussing in today's session.

25:02

And it is not just one class we are doing on Rags. Rags will be done over multiple sessions.

25:08

So today is only the first class on Rags that we are doing, but Rags is done over four sessions, I think next week, next to next week.

25:17

Also, we'll continue on with Rags.

25:20

So today is the starter session, the starter, the starter introductory.

25:24

Last one, rags we are doing. And, and here, we will try to learn the big picture.

25:31

So today's session is more about the big picture. It will give you the big picture idea

25:34

in terms of what, what, what rags are. And we will see absolute very basics today.

25:40

Like the whole, the whole rag pipeline we will see. And the complete full rag applications we will

25:51

discussed only in the upcoming sessions. Okay. So in the upcoming sessions, we will

25:55

talk about that.

25:57

So these are the broad agenda of the agenda of what we will cover. So first we'll understand why

26:15

rights. When we are learning a new topic, first we have to.

26:21

First, we have to go and understand why rags are important.

26:29

That's the first part. Next, we will obviously understand rags. We'll understand the big picture

26:33

idea behind what rags and retrieval augmented generation really are. So we will see that what

26:40

rags really are and what they bring to the table. We will understand the different components

26:45

of a rag. So what is retrieval, what is augmented, what is generation, what these things

26:51

are we will discuss. And then we will see a very small manual demonstration with and without

26:57

context, what it is we will discuss. But I want to clarify today, we will not see full drag app.

27:02

Bragg app is, as I say, it is built over four sessions. It's only the first of the four classes

27:07

on drags we are doing. But today will just be a very manual demonstration we will discuss.

27:12

We will see a very small demo today in terms of how to convert input text into embeddings.

27:18

Okay, that's what we will be discussing. And then obviously,

27:21

these will be taken up in the upcoming classes.

27:23

So this is the kind of the starter class we are doing today.

27:27

Okay. And as I already clarified, the safety and responsible AI is not part of putting it.

27:32

So this is the RAC specific discussion that we are doing today.

27:37

All right. Now, moving on.

27:51

Arshita, can you please answer these questions regarding the topics? I think you can also help this, I think, or contribute a question. You can, please answer.

28:21

Thank you.

28:51

Thank you.

29:21

Hardy, to answer your question, yes, I think yesterday we just covered about

29:32

about LLM API calls.

29:34

But see, again, I, I, one thing is that you must be, like, there is always a continuity.

29:40

So, well, like, will you get this topic?

29:42

I don't know if I can answer that, but obviously it's a continuing session.

29:46

There will be some portions of yesterday that we'll be using today.

29:48

So I would suggest, I think the conceptual.

29:51

part you can definitely get it. Majority of the concept today, one, one and a half

29:55

hours will be the concept. So that you will definitely understand. But the part when we come to the

30:01

coding part that, for that, I think yesterday's relevance will be required. Okay. Yeah. Okay. Now.

30:21

So first of all, what are large language models? What are large language models?

30:51

the meaning of LLMs, what are large language models? Let us understand that in Dutively.

30:55

So we already talked quite a bit about the context of what a LLM is. And if you remember,

31:01

LLM is basically trained on a huge amount of public text data up to a particular knowledge cutoff.

31:07

The important term that we are using is something called a knowledge cutoff. So a large language

31:10

model is trained on a tremendous amount of text data up to a public knowledge cutoff. Okay. And at

31:17

answer time, it predicts the likely works. That is basically what the

31:21

large language model is, NLM is. And we have already spent time discussing LLM so we can relate

31:25

to that. So you take a tremendous amount of data, you train the model so that it understands

31:33

the patterns and the context from all your data. So the model has learned the entire context from your data.

31:38

That's what we refer to as model training. And during prediction, during inference time, the language

31:45

model will predict the answers. So given a particular sequence of words, the language model will predict

31:50

what is the next word, the next word, and the next word, and so and so forth.

31:54

Okay. So we have the training data. We train the language model on the train data. That is what

32:00

is referred to as model training. Okay. So on the training data, we train the language model. Okay.

32:05

And then given we give some new data, given we give some new data, we will go back and use that

32:13

particular language model for making predictions. So we'll try to predict what is the next word,

32:17

what is the next word, what is the next word at

32:20

so forth so that's the way how it basically looks at now let's first understand the uh the context you

32:28

okay so so this is again the the l ln that we are talking about uh it is trained on public internet data

32:35

and this is a very very important thing which is called knowledge cut off right now what is this

32:40

knowledge cut off i'll give you a very small uh a very small example what i mean by this

32:46

what i mean by this particular term okay so let us see that

32:50

let us see that i'll open up my chat gpt for a moment

32:57

to demonstrate is in a better way okay now if you take a look at this

33:16

okay now if we take a look at this all if you can observe this

33:30

or let's go to grog because you've already used grog before so i'm going to go to grog here

33:46

right the system message is you are a general assistant who can answer

33:59

general queries so i'm keeping it very see i'm keeping it very uh very high level so i'm

34:07

keeping the overall uh message part very high level the system message you're a general assistant

34:13

who can answer general questions

34:16

that's the system message would be let's say i'm so the user message would be

34:21

what is the so what is the system message is this and what is the user message would be

34:30

let's say who want the recent kerala or let's say tamil natu

34:46

assembly elections right so very interesting we are able to uh we have actually asked a

34:56

question if you take a look at it now the now we all know the answer who won the recent

35:02

tamilana elections but very interesting we are using a language model called llama 3.3

35:07

so we are using a llama 3.3 versatile model this is the open source model and we have used

35:12

grok in the last week of class when we were introducing LLMs we were just

35:16

this kind of thing system user all that we have seen right now very interesting when you run this

35:21

query you will realize the language model will say the recent tamil natu elections but one

35:28

when held in this and dmka party won the elections very interesting it says 2021

35:37

2026 data on but it doesn't have the data that is what i meant by the knowledge cut on all

35:42

these large language models they are trained on a data up to a particular point in

35:46

time that never real data not only up to a particular point in time these language

35:51

models are trained on that on the data so all these other lms are trained on on a particular

35:56

amount of data latest as of let's say 20 204 2025 whatever okay and then these models are

36:03

released so when we ask these models questions like in this case when i write the system message

36:09

when i write a user message when i ask when i when i ask questions in a certain way right when i go and

36:14

ask these models questions in a certain way these models will respond in a different

36:20

when i ask these models questions in a certain way these models will respond based on their

36:25

knowledge cutoff based on whatever prior knowledge they have they will not be able to give generic

36:31

like yeah they won't be able to give absolute up-to-date answers but they will be able to give

36:37

they will be able to give uh like answers to the questions yeah exactly chat gptie all

36:44

that gpt also behaves the same correct now very interesting if i just change the query

36:50

and if i say who won the 2026 Tamil natu hasm relations

36:56

now we'll update today 26 now we'll see something very interesting will happen

36:59

now it says i am not aware of the current information and my knowledge cutoff is

37:05

December 23 this is what the knowledge cutoff is so knowledge cutoff

37:10

The Lama model that you are able to see on the screen,

37:15

now the GROC in GROC in this model is trained latest as of December 20203 data.

37:21

That's after the data is trained not trained this model has been trained only

37:25

latest as of December 2030 data and so sorry i don't have real time information for the most

37:31

accurate is checked with a different source. So you can repeat the same story with a different model

37:36

If you want to try a different model, you can try, no problem.

37:43

You can try, no problem.

37:44

coin 32p try, submit.

37:46

And look, this cutoff is all right.

37:48

It's, it's, you can see you, it is away.

37:52

So this is also very interesting.

37:56

Let me check the current date.

37:58

Now his current date is different.

38:00

You can see very interesting.

38:02

Now for that particular coin language model, it's a different

38:06

kind of framed it, he has knowledge cutoff not directly.

38:08

But you can understand its knowledge cutoff

38:10

October 2023 is.

38:12

Because for the language model quail,

38:14

when it was trained,

38:16

its context in the current,

38:17

it's October 2023 is.

38:19

He's, you know, we've got to October 2023

38:21

is our information.

38:23

You're going to, you know,

38:24

you're going to be.

38:26

And you can't.

38:27

And you can back from

38:28

what is the

38:29

what is the knowledge cutoff of the

38:35

model?

38:36

What is the knowledge cutoff for the, for this particular coin model, you can, you can take a look at it.

38:43

And you can see the knowledge cutoff for this particular point model is this.

38:46

That's quite one way to be correct.

38:48

Yes.

38:49

That is an agent, actually.

38:52

ChatGPT is not the intent of the conversation.

38:54

ChatGPT is different.

38:55

But ChatGPT's current knowledge was there because it is basically using Internet search.

39:01

But if you're using the normal large language models, then that is not for the computer current.

39:05

is not going to be the correct answer.

39:07

Okay?

39:08

Yeah.

39:09

So that's a good question.

39:10

If this question in chat GPT in, then answer is right.

39:12

If you're in Germany in, then answer is right.

39:15

Because remember, they are having the most up-to-date information.

39:18

Because they're going to internet search use.

39:20

Chat GPD is not a large language model.

39:23

And to understand about chat GPDs, we have to cover another two months of sessions to understand

39:27

agents.

39:28

So chat GPD is actually an agent.

39:30

Just to clarify.

39:32

So agent is a lot more than what we are.

39:34

than what we are seeing right now.

39:36

But just to clarify, in case people are running these queries in chat, GPT and Gemini,

39:41

and wondering that there's right answer there.

39:43

There's the latest data.

39:44

He can look at.

39:45

Why don't you know?

39:46

You know, very interesting.

39:50

I can search the information here.

39:52

What is the closing?

39:55

What is the census closing price today?

40:00

Now you have question here.

40:02

This is this question here.

40:03

Now, let's do Lama.

40:04

Okay.

40:05

You.

40:06

Now, look at this.

40:07

I am not able to provide real-time information.

40:08

That's not.

40:09

Look at this.

40:10

I am not able to provide real-time information.

40:11

He doesn't know that.

40:12

Because of the current information, today's what is the correct information?

40:14

Today's what?

40:15

He doesn't know that.

40:16

But if you go and ask the same question to...

40:19

If you go and ask the same question to chat GPD,

40:22

if you go and ask the exact same question that what is the closing census price today,

40:28

you will be able to see this will give you the correct answer.

40:30

Because this is doing internet search.

40:31

Searching the web.

40:32

Can you see?

40:33

that is not just using a language model it is searching rather simple so this is something else don't confuse with chat gpd we are right now completely focused on the l l lm model so chat gp t is something else you're not going to talk about gpd at all for here here all those are

40:49

models that we are using right now so all these language models that we are talking about they all have a knowledge cutoff they only know only up to that point okay now so naturally if you ask me from a practical context okay so naturally if you ask me from a practical context okay so a

41:03

one example we know knowledge cut off we understand okay now let us ask a slightly different question

41:09

so a one so let's say uh question we'll putt up so let's say uh question we'll

41:15

we do the sien and know how to build how to build uh okay interesting one okay

41:27

okay we're a scenario say so that's what we're trying to try to try to do so this is to further read

41:33

force the concept of knowledge cutoff.

41:34

What is what?

41:35

Knowledge cutoff of what means?

41:36

One of we have you

41:37

we've got it.

41:38

Recent information.

41:39

Okay.

41:40

So,

41:41

uh,

41:42

does I know,

41:44

uh,

41:45

uh,

41:47

open source

41:49

ellips,

41:50

open source models

41:51

and has he built

41:54

air gap

41:58

systems

42:00

in his experience?

42:02

in his experience.

42:05

So very interesting.

42:06

So it is asking a question.

42:08

Now that LLF

42:09

how you know,

42:10

you know,

42:11

the language model is a generic language model, right?

42:15

Now this is trained on Internet-scale data.

42:17

It is trained on all of Wikipedia, Internet scale data,

42:20

public data,

42:21

it's trained there.

42:22

So now if you go and ask this question,

42:24

he's what can do?

42:26

Sorry, I don't have any information about a person.

42:29

See, I'm not a popular celebrity or something.

42:31

something.

42:32

You can this question if Elon Musk asks, he'll,

42:33

but the Lama model is not trained on my data.

42:35

He's not trained on my data.

42:37

He doesn't know that.

42:38

He doesn't know that, right?

42:39

However, I can tell you that it is giving a generic answer.

42:42

So what I'm getting at is,

42:45

if you ask any specific question,

42:48

if you ask any specific question,

42:53

this LLM is

42:55

answer

42:56

without the context.

42:59

And here here, context,

43:00

context,

43:01

resume.

43:02

If you're my resume attach to you

43:04

or you're the

43:05

answer.

43:06

If you don't attach my resume,

43:07

it cannot give the answer.

43:09

That is what I further mean by the context.

43:12

So if you ask a generic question,

43:14

that will, that will

43:16

answer will

43:17

answer.

43:18

Okay, the LLMs can be, without our documents,

43:21

the LLMs can be confidently wrong.

43:23

That is exactly what I wanted to show you here.

43:26

So if you,

43:27

if we have our resume

43:28

and if we don't

43:29

ask,

43:30

let us, I know about open source models.

43:32

So, yeah, that experience and skills

43:34

they're asking.

43:35

LLM can't know.

43:36

But if I go ahead and attach my resume,

43:40

if I add my company knowledge,

43:42

if I add my resume, then it will be able to get the correct answer.

43:45

So the important concept that I'm getting at is without context and with context.

43:50

When you're LLM to ask you

43:52

ask you,

43:53

you're not going to

43:54

those specific answers

43:56

not can't give you.

43:58

Now, let us go and

44:00

repeat the same thing in a slightly different way.

44:04

So my resume is I can just quickly take my resume.

44:09

Just give me one minute.

44:11

I'll just open it up, paste it and show all of you.

44:30

Thank you.

45:00

Now we'll what we'll do?

45:06

We have our resume is, we have it, we'll

45:10

basically copy my entire resume text.

45:14

We'll copy my resume text

45:16

we'll copy here here.

45:17

So this is my entire

45:21

resume text.

45:22

I've got it.

45:23

This is my entire resume text.

45:24

This is a whole two-page resume here.

45:26

This is a full page resume.

45:28

And what I will go back and do.

45:29

And what I will go back and do,

45:30

Now I will come back to Grog and say that you are a general assistant who answers general questions, general queries.

45:37

Okay.

45:38

And then system message we're going based on some context.

45:42

Based on some context.

45:44

And we further going, you will be, you will be given a question

45:54

starting with question

45:58

question.

45:59

And you will be given, you will be given the context.

46:03

You'll be given the context.

46:21

Starting with hash context.

46:25

context

46:27

Use the context to answer the question.

46:34

Okay?

46:35

Everyone is able to get a feed for it.

46:37

And here what I'll do exactly what I explained to you.

46:41

Okay?

46:42

Here exactly how I explain to I'll do the whole thing.

46:44

So now I will go back and I will go ahead and

46:49

here I will go ahead and say this is the question.

46:55

This is your question?

46:56

Remember starting with hash hash question.

46:59

This is.

47:00

Okay?

47:01

And this your context.

47:03

This is your context.

47:04

Context will be very big.

47:06

Context is a quite big.

47:08

Context is a big.

47:09

Context in our context is.

47:10

This is our whole context is.

47:12

You're our entire context.

47:13

If we'll start, if we're

47:15

our context and our question,

47:17

everything is,

47:18

context be and question be.

47:19

The whole thing is there.

47:20

And now here we go and

47:22

and now here I can go back and finally ask the question.

47:29

Let us see.

47:30

Okay, let us see.

47:32

Okay, here a system message

47:36

here here user message.

47:39

User message in.

47:40

You're two things.

47:41

Context is and question and

47:44

what final user message.

47:46

Sorry, this basis we'll answer

47:48

So there it is system message, user message.

47:51

And user message contains the question and the context.

47:55

Now if I ask, you can see,

47:57

you can look at this.

47:59

Good, right?

48:00

There is the, this is actually what rags are.

48:02

I wanted to just do a small, you know,

48:05

simulation to help you understand that rags in that

48:07

what are.

48:08

So, you can see if we can't,

48:10

you can't ask you,

48:11

so you can't get in chat GPT in

48:13

he could be what experience.

48:15

Chat GPT in,

48:16

here you're normal questions

48:18

you know,

48:19

how can't tell you?

48:20

No, no.

48:21

sign, what?

48:22

Now, this is very different.

48:24

This is different.

48:25

It's the concept is a different.

48:26

You're, you ask, how, how

48:29

answer it?

48:30

Because chat GPT has something on memory.

48:33

I don't know how many if you know,

48:35

as more you go and query,

48:38

the more you go and query all these GPD systems and all that,

48:42

so chat GPD has already built a profile about me.

48:45

And you can see this.

48:47

Some of you do not know this.

48:48

You can actually go to settings.

48:50

You can actually go to settings.

48:51

in settings, and if you go to settings,

48:53

you have here personalization and if you scroll down, there is something called memory.

48:58

This is all the memory in memory

48:59

stored in.

49:00

So every time you chat with chat, GPD, that's all the conversation in memory

49:03

store.

49:04

So it builds a complete profile about yourself.

49:06

But anyways, just to come back to the

49:09

conversation, if you ask a generic question,

49:12

the language models will not be able to answer,

49:15

but if you are giving the context,

49:18

if you are giving the context,

49:19

if you are giving the context,

49:20

then if you are giving the context,

49:21

it will be able to answer.

49:22

So that is the concept that I want to cover.

49:24

No knowledge cut off.

49:25

Okay?

49:26

Yeah.

49:27

So internal documents should be there in part of my pen.

49:28

If you can give the internal data,

49:30

if you resume attached,

49:32

if you're up confidential documents attach to do,

49:35

if you context in providing to provide

49:36

then the LLM will be able to give a very accurate answer

49:39

based on exactly what you lost.

49:41

Okay?

49:42

Now, and just as I explained to you,

49:44

only if you give it the text,

49:46

paste, upload, retrieve with rag,

49:48

otherwise it will guess from general patterns.

49:50

Okay?

49:51

Now we are finally entering into what Rags really are, okay?

49:55

Now we are finally entering into what Rags really are.

50:00

So Rack basically stands for retrieval augmented generation.

50:04

So what is it basically?

50:07

It is a pattern where a system searches an external knowledge base

50:12

retrieves the relevant text, adds it to the ground, and then the LLN generates the answer.

50:18

Okay.

50:19

So before I get to this, let me just talk about.

50:21

this a little bit more.

50:23

Okay, let me just talk about this a little bit more.

50:25

Let's be more.

50:26

Then it will be clear.

50:28

One more questions questions, okay?

50:30

Okay, this is everyone's clear.

50:32

One more small question is, okay?

50:34

So what I will do?

50:36

You are a general assistant, again, question, font text, answers,

50:42

all will.

50:44

Now, I will ask a question

50:48

from a very confidential document.

50:50

confidential document.

50:52

So imagine, I'm just, I'm just generally giving the analogy here.

51:00

So imagine my resume is a very confidential document.

51:04

Yeah, if I have to take a more, you know, if I have to take a more practical example, I can,

51:12

I can do that for you, just give me one minute.

51:17

We can take a small example.

51:19

where we take a massive document here.

51:49

Thank you.

51:51

Thank you.

52:21

So I'm just going to show you a sample BDF.

52:51

Thank you.

53:21

If you take a look at it.

53:25

I've got a look at it.

53:41

I've got a Tesla annual financial reports data here.

53:45

Again, the objective is to simulate something.

53:50

This is a Tesla report, financial report.

53:52

It's a real data, right?

53:54

This was a Tesla report that was filed in December,

53:58

2023 fiscal Europe.

54:00

It's the real Tesla incorporated data.

54:02

And this is a massive PDF file.

54:04

Here's a 130 page data.

54:06

Real data, real Tesla guidance.

54:09

Why am I showing you this?

54:12

My point is to tell you that in the real world,

54:15

this kind of data will be very confidential.

54:18

This is very confidential data.

54:19

There's a very confidential data.

54:20

Now, I am, let's say, playing the role of a investment advisor.

54:22

What you're doing, this is a very confidential data.

54:23

Right?

54:24

Now, I am, let's say, playing the role of a investment advisor.

54:27

And all that, let's say,

54:29

playing the role of a investment advisory services.

54:34

You call up the bank, you call up it investment advisor.

54:40

That you'll you give you, sir, you can do, that,

54:43

and all that.

54:44

And oftentimes these people will need, you know,

54:48

you know, they get answers to questions, real cost.

54:54

Post any questions, right?

54:56

Also, that's actual questions, right?

54:57

And they've got answers to growth portions of growth costs.

55:00

That's the intention, right?

55:02

So how do you do that?

55:05

How can I go back and use this particular data set

55:09

to get answers to this question?

55:11

So, let's say one sample question will be,

55:15

what is the annual derivative of Tesla in the level?

55:17

in the year 2020.

55:19

So, again, this Tesla is a public company, so we are reported to photo.

55:25

You can put a story.

55:27

If you have a private industry company,

55:29

okay, a Tesla company is in New York,

55:31

American stock, etc.

55:32

there's a trading and then.

55:34

Tesla public can declare.

55:35

But, okay, you're a small startup.

55:37

Do you?

55:38

Do you have a small startup?

55:39

Do you?

55:40

No, right.

55:41

You work on a matter.

55:42

You've got paid.

55:44

You've got paid.

55:45

how much expenses, problems, how many people are.

55:49

You don't have to take it.

55:50

You do you have a public credit.

55:52

So imagine for a minute that this is a document from a private respect.

55:57

A private history,

55:59

there's a presentation, a PDF of where,

56:02

private, how to update,

56:04

and yet you want to use a large language model to access this information.

56:10

If you have this information,

56:11

if you do this document from any question,

56:13

how do you?

56:14

So the document,

56:15

if you want to ask some questions from your particular document data,

56:25

if you have to do, then what you will have to do?

56:31

You will have to go back and explicitly, explicitly,

56:33

explicitly upload the documents.

56:35

You have to upload the documents.

56:38

Otherwise, the model will not be able to answer appropriately.

56:41

And yeah, I think momentarily 30 seconds it was, it will back.

56:44

So what I was talking about.

56:45

telling was, look, Tesla is a public company.

56:47

Tesla is a publicly listed company.

56:49

But what if you take the example of a private company?

56:52

You, for a minute, assume, they,

56:55

that this is the private company,

56:57

this is a privately listed company.

56:59

So if private company is,

57:00

then it's data you'll not get online.

57:02

You can internet in the internet

57:03

data not will not be.

57:05

Because this private company is.

57:08

But yet, what you want to do,

57:10

you want a large language model to answer questions on this data.

57:14

The idea would be, that we'll be, that we'll be, that question, answers look at,

57:21

and that's the way how it will work out.

57:25

So how?

57:26

How? How? How? How? How?

57:27

How?

57:28

How?

57:29

Two ways, we're two ways.

57:31

And again, I'm telling you guys, Tesla is public company.

57:34

So, man, it's a private company's data, okay?

57:36

And, look, here we have already answers

57:38

have. I already know, that it's 81,

57:40

000 port 62,

57:41

something is.

57:42

Now, this is how it is, what are it, don't worry.

57:44

That I'm going to know.

57:46

So that's why I'm showing you.

57:48

So this is the actual annual revenue of Tesla in the year 2020.

57:54

This is the number, okay?

57:56

Now what I will do, I will just go and for a minute,

58:00

we'll copy to, okay?

58:02

Exactly how I told you,

58:05

question, context, the whole story has been discussed.

58:08

This is copy it will.

58:10

Okay, without copy it, it will not be.

58:12

Okay?

58:13

So we'll copy.

58:14

Same way, right?

58:16

You'll have to copy the whole thing.

58:18

This is the whole thing.

58:19

This is the whole context.

58:21

You can't understand it.

58:22

Context.

58:23

This is also copy it.

58:24

But one more page copy can,

58:28

in reality, it will be several,

58:30

all the thousands of pages you will have to give us context.

58:33

Here, let's go,

58:35

here, let's say,

58:36

I've, for simplicity,

58:37

one or two pages,

58:38

okay?

58:39

What I will do?

58:40

I will go back to my GROC and I will say,

58:44

that the context here is.

58:47

Context here, this is,

58:49

this is the full context.

58:50

I have the page copied here,

58:52

and here your question is.

58:55

Question is, what is the question is,

58:59

if you just take a look at it,

59:01

question is, what is the

59:03

annual revenue of Tesla in the

59:09

in the

59:10

year in the year 2020.

59:14

Now, this is again what I have been explaining all this why.

59:20

If you're your general

59:22

question, if you just go and if we had asked this question

59:26

generally without giving the context,

59:29

it will not know the answer.

59:31

He will not know the answer.

59:32

He will, he's not the answer

59:33

because he has no information.

59:36

Imagine for a minute, it's a private company.

59:38

If private company, then

59:39

then you can't have.

59:40

So he will guess.

59:41

But if you can give the context and

59:43

and if you can give the context and

59:44

if you, if you hit the submit button,

59:48

ah, right?

59:49

So you, you can't,

59:50

we get it, it's not 100% correct, but 81,000 4662.

59:54

Can you see?

59:55

And you're getting it?

59:56

So answer is right or not?

59:58

We can agree that

1:0:00

it's not formatted perfectly?

1:0:02

It's not formatted perfectly.

1:0:03

You, look.

1:0:05

Okay?

1:0:06

Clear it?

1:0:07

This is rag.

1:0:08

This is the concept.

1:0:09

This is what is meant.

1:0:10

bite and we have you proved

1:0:12

that answer is 8,00462

1:0:14

because I already showed you that table.

1:0:16

We have you

1:0:17

that table.

1:0:18

We have you, we have table

1:0:20

and we have the table in

1:0:22

that table in it,

1:0:24

that answer is 81,462 have.

1:0:27

This revenue is 2020

1:0:29

So the moment I give this entire

1:0:32

document as a context,

1:0:34

the whole page we copy

1:0:35

and here on context

1:0:36

if we'll put up

1:0:37

and if we're based on

1:0:39

then we'll question

1:0:40

we'll ask

1:0:41

if we're questions

1:0:42

if we're

1:0:43

question

1:0:44

and this is

1:0:46

our question

1:0:47

if I ask a question

1:0:48

the model has given

1:0:49

the correct answer

1:0:50

and that's the magic of

1:0:52

what

1:0:53

what providing the context is

1:0:55

now let me pause

1:0:57

problem.

1:0:58

It's the problem

1:0:59

then you

1:1:00

then you'll say

1:1:01

so all, so

1:1:02

then what's all right

1:1:03

what is

1:1:04

if any

1:1:05

if any document

1:1:06

if we're like we

1:1:07

copy and paste

1:1:08

then

1:1:09

so

1:1:10

this is all

1:1:11

the question

1:1:12

should be

1:1:13

that

1:1:14

this is

1:1:15

if you're

1:1:16

if context is something we can

1:1:16

anyways

1:1:17

take from my

1:1:18

PDF

1:1:19

I can copy and I can paste

1:1:20

it

1:1:21

then problem's all right

1:1:23

now

1:1:24

we can

1:1:25

we can't

1:1:26

we can't

1:1:27

we can't

1:1:28

problem is

1:1:29

that

1:1:30

whenever you're calling a

1:1:31

large language model

1:1:32

using an API

1:1:33

what we were

1:1:34

doing yesterday

1:1:35

yesterday we were using the

1:1:36

using the ROC API, right?

1:1:38

When you are

1:1:39

information,

1:1:40

you're publicly

1:1:41

sending outside

1:1:42

the network.

1:1:43

So imagine you're a private

1:1:45

listed company,

1:1:46

you're not publicly listed,

1:1:48

you're a private company

1:1:49

or a startup

1:1:50

your financial document

1:1:52

my resume is around very personal information.

1:1:55

So

1:1:57

and if you want to

1:2:00

use an NLM to answer questions

1:2:03

based on your document

1:2:05

so in this case we have

1:2:06

are using Lama 3.3 model to answer questions based on our document.

1:2:10

It's all

1:2:11

the system message you've

1:2:12

did,

1:2:13

user message you're

1:2:14

there

1:2:15

already sorted.

1:2:16

You know, you know the part where I have a problem.

1:2:20

The part where I have a problem is this

1:2:22

part.

1:2:23

This we have a problem.

1:2:25

This will not be just two pages.

1:2:27

This will be the entire document.

1:2:29

I'm talking about several thousands of pages.

1:2:32

So two problems.

1:2:34

Two problems.

1:2:35

The problem is.

1:2:36

this whole information is,

1:2:38

this whole information

1:2:40

I'm online

1:2:41

are being

1:2:42

because only then the API call is happening, right?

1:2:45

You are passing.

1:2:47

What are you doing?

1:2:48

When you're writing a prompt, what are you doing?

1:2:50

Back to last week's conversation.

1:2:52

Last week, what we've seen

1:2:53

you?

1:2:54

You're system message,

1:2:55

and based on that,

1:2:56

an API call is getting made.

1:2:58

That's what we did, right?

1:3:00

Yesterday in the class we did

1:3:01

what we did.

1:3:02

We created API key.

1:3:04

We created API key.

1:3:05

We made system message,

1:3:06

based on that, we made an LLM call.

1:3:08

We have function called.

1:3:10

Client chat completions create.

1:3:12

Grog's model called, and answer

1:3:14

gave. But

1:3:16

how can call? What?

1:3:18

What is what? You're sending the data outside the network.

1:3:21

And that is a very sensitive thing.

1:3:23

So privacy is a huge issue.

1:3:26

Data security is a huge issue.

1:3:28

In real enterprise application is a big problem.

1:3:31

If if any personal data

1:3:32

if you're like, sir,

1:3:33

what is, sir,

1:3:34

you're going to do,

1:3:35

this is your chat in.

1:3:36

so what you have to do?

1:3:38

Chat GPD in go, do.

1:3:39

But we're in class

1:3:40

chat GPD not are

1:3:42

not.

1:3:43

It's important to know the difference,

1:3:45

okay,

1:3:46

you know,

1:3:47

you can,

1:3:48

that we can't

1:3:49

that we can't

1:3:50

upload it,

1:3:51

but can you imagine a company

1:3:53

doing this in chat GPD?

1:3:54

Who will,

1:3:55

not?

1:3:56

It's a confidential data.

1:3:58

But,

1:3:59

yeah,

1:4:00

if I ask a question, will it answer,

1:4:01

it will answer?

1:4:02

Because the whole document is treated

1:4:04

as a context.

1:4:05

Whatever you are

1:4:06

uploading right now, this entire document is treated at the context.

1:4:10

I'm just trying to show you in different, different flavors.

1:4:13

I'm trying to explain to you

1:4:15

when you give the context,

1:4:17

when you are giving the context,

1:4:21

it will give the exact answers.

1:4:22

$81,062 million dollars

1:4:25

based on the document.

1:4:27

Problem number one,

1:4:28

data privacy, security,

1:4:29

because you're in network

1:4:30

you're using this

1:4:32

or you're just like this

1:4:33

or you're just like,

1:4:34

system user,

1:4:35

you're, you're,

1:4:36

Number two,

1:4:37

more big problem.

1:4:38

Or the more problem is

1:4:39

that if your document is massive,

1:4:43

here here,

1:4:44

you know,

1:4:45

it's 1, 130 pages is big,

1:4:47

but 130 page is not that big.

1:4:49

130 pages is relatively small,

1:4:51

relatively small document.

1:4:53

But what if you have a document which is several,

1:4:55

you know, millions of pages,

1:4:57

and this is not a document

1:4:58

in the company,

1:4:59

there will have thousands of PDFs in the company.

1:5:01

You will have thousands of PDF files in the company.

1:5:04

And imagine if I have to upload all these PDFs

1:5:06

files, that's first possibly not

1:5:08

and the other very, very important term that I want to mention

1:5:12

is a term that is referred to as a context window.

1:5:15

Context window.

1:5:18

Context window.

1:5:20

This is LLM, this is X actually, this is X,

1:5:23

this is X.

1:5:24

It may be LLM say, they have something called a context window.

1:5:28

Or LLM what is something that takes the input and it gives an output.

1:5:33

So,

1:5:35

the M

1:5:36

maximum size of your input is what is referred to as a context window.

1:5:40

So, input is that

1:5:42

the input is much more than

1:5:44

even if you have a context window limitation.

1:5:46

I mean you have a language model

1:5:48

which is only having a context window up to

1:5:51

1 million tokens or 1 billion tokens.

1:5:54

You can't that more tokens

1:5:56

that.

1:5:57

Now that's the more document not attach

1:5:59

and that is the reason why in Chad GPT and Gemini

1:6:02

now,

1:6:03

now go to Gemini

1:6:04

there is a maximum limitation up to 10 documents.

1:6:06

Now, you know,

1:6:07

upload even if you can't

1:6:08

at a time,

1:6:09

I'm process not

1:6:10

so two practical limitations

1:6:12

have

1:6:13

number one,

1:6:14

data privacy is an issue

1:6:15

and number two,

1:6:16

the context window is an issue.

1:6:17

Whatever

1:6:18

document you are sending across,

1:6:20

whatever document you're uploading,

1:6:22

if that document

1:6:24

big,

1:6:25

not?

1:6:26

If that the document

1:6:27

both big,

1:6:28

so then

1:6:29

it will

1:6:30

be too big for the

1:6:32

input layer to handle.

1:6:34

This LLM's

1:6:35

context window is the maximum size of the input it can handle.

1:6:40

And if your document or documents that you're uploading is too big,

1:6:44

then that process in

1:6:45

can't

1:6:46

so these are the real world challenges that I want to highlight to

1:6:49

really world challenges.

1:6:52

Now coming back to the question,

1:6:54

this is the reason why we are studying RAG.

1:6:58

So RAG in the

1:6:59

two problems solved

1:7:00

at the same time I can answer questions based on context.

1:7:04

So coming back to what we discussed,

1:7:06

story's same will be

1:7:08

this.

1:7:09

This your system message,

1:7:10

this is a question

1:7:12

we'll, we'll give context,

1:7:13

it is like, you know, it is those

1:7:16

reading comprehension questions which we used to

1:7:18

solve when we were, you know, when we were young,

1:7:20

when we were young, we used to solve those

1:7:23

those reading comprehension questions, right?

1:7:25

You're giving a particular paragraph,

1:7:27

a paragraph you give you a paragraph,

1:7:29

and then we ask us questions

1:7:31

question questions, that,

1:7:32

you know, this is, that, is, that,

1:7:33

this is.

1:7:34

So we tend to ask you questions on the basis of that.

1:7:37

So that is the same thing.

1:7:38

Same idea we are discussing.

1:7:39

It's kind of like those

1:7:41

so-called reading comprehension questions we are talking.

1:7:44

The question be thinking, context be

1:7:46

and that's based on our answer can.

1:7:49

So the answer to the question has to be based on the context.

1:7:52

That's the way how it has to work out.

1:7:54

Okay.

1:8:04

So now moving on.

1:8:19

Finally, we're moving out to the right definition.

1:8:22

We've got a kind of conceptual things about

1:8:24

so now it will be easy.

1:8:26

So retrieval augmented generation is what it is called.

1:8:29

It is a normal generation.

1:8:31

You know,

1:8:32

so first you know,

1:8:33

you know,

1:8:34

augmented what?

1:8:35

So we are trying to understand what retrieval augmented basically means.

1:8:38

What is the meaning of retrieval and augmented?

1:8:40

Okay?

1:8:41

So normal generation, we understand.

1:8:43

Normal generation,

1:8:44

you ask a question, get an answer.

1:8:46

That is what is referred to as normal generation.

1:8:48

You ask a question, and based on that, you get an answer.

1:8:50

That is what is referred to as normal generation.

1:8:53

Now, what is retrieval augmented generation?

1:8:57

You're from something retrieved and then you generate.

1:9:00

That is what is referred to as retrieval-movemented generation.

1:9:03

Now, let us start.

1:9:04

take a very simple analogy, which is very nicely explained here also, which I want to show you.

1:9:09

Let us see that.

1:9:11

So in RAG, the system searches an external knowledge base, retrieves relevant text, adds it to the prompt,

1:9:22

and then the LLM generates the answer using that material.

1:9:27

So if I have to just use a little bit of analogy, the system searches an external

1:9:34

knowledge base retrieves the relevant context. Context retrieves it.

1:9:39

Okay?

1:9:40

So text, we'll take it.

1:9:42

Retrieves the relevant context, C-O-N context.

1:9:45

So it looks up in the knowledge base, retrieves the relevant context.

1:9:52

Adds it to the prompt.

1:9:54

Now, prompt in system message be and user message be.

1:9:57

So prompt will contain the system message also and the user message also.

1:10:01

That context will be context.

1:10:03

Okay?

1:10:04

retrieved and context on prompt and based on that we are generating the answer.

1:10:09

So simple words, search first, then speed.

1:10:14

Okay, that's the way to look at it.

1:10:16

This is the simple way to understand what we are doing in a rag.

1:10:19

Abbe to what we are doing in a rag.

1:10:21

We assume that we're assuming that we're going to be context already we're going to

1:10:24

take.

1:10:25

This is your rag system more correctly.

1:10:28

Because we talked about why that's

1:10:31

because data privacy, context window limited.

1:10:33

Context window limitation, it's a big document to, we'll upload not

1:10:36

can't.

1:10:37

So solution, what is?

1:10:39

Rag solution.

1:10:40

You have a very big external knowledge base.

1:10:43

You have a massive external knowledge base, okay?

1:10:46

There's a massive external knowledge base that you have right now.

1:10:49

So what we will do?

1:10:51

So the external knowledge base is like a library.

1:10:54

Okay?

1:10:55

What I'll do is, let me complete the flow, then I'll take up the questions.

1:10:58

Okay?

1:10:59

Let me complete the flow, then I'll take up the questions.

1:11:01

Okay?

1:11:02

So we will go and go and go.

1:11:03

search the documents from this external knowledge base.

1:11:07

Here the library here, all the documents are tagged.

1:11:10

We're supposed to send us.

1:11:13

Once the question is asked, the system will search an external knowledge base.

1:11:20

That system go and search here search

1:11:22

here.

1:11:23

This is an open book exam is going to.

1:11:25

Explain the transformer architecture.

1:11:27

You're asked you.

1:11:28

You don't know.

1:11:29

Not literally.

1:11:30

You're intelligent, but let's say you don't memorize these things.

1:11:32

you don't memorize these things.

1:11:33

Let's say you don't memorize.

1:11:34

That's what transformer?

1:11:35

I'm just.

1:11:36

I have to look up.

1:11:37

Open book exam.

1:11:38

So, go, okay.

1:11:39

Go ahead.

1:11:40

So you're asked a question.

1:11:42

What you will do?

1:11:44

You will now start to think.

1:11:46

Okay.

1:11:47

Search.

1:11:48

This our whole bookshelf is nothing but the knowledge base.

1:11:51

There go and search.

1:11:52

System searches an external knowledge base.

1:11:54

Retrieves the relevant context.

1:11:57

Relevant the books are,

1:11:59

retrieve them.

1:12:00

drift and then you generate the

1:12:02

and then you generate the answer.

1:12:04

That is what RAG is.

1:12:06

So the biggest thing about RAG is, it connects an

1:12:09

LLM to your knowledge base.

1:12:12

It was just a normal language model.

1:12:15

It was just a normal language model.

1:12:18

Now the best thing about RAG is that you are giving

1:12:21

your language model ability to connect to your knowledge base.

1:12:26

Your knowledge base is

1:12:28

on that system can directly connect to you.

1:12:29

can directly connect to that's the idea okay there's a lot of text here which is very neatly

1:12:35

explained so i'm going to just maybe pause for a minute here to allow everybody to read through

1:12:41

it once just give it a read once often just read through it once this part then i will explain

1:12:47

and you're just to answer to your question no it is not trained on data

1:12:51

it is not trained on them all of you just give it a glance once just give it a glance once just give it a glance

1:12:59

Here we're here we're here we're

1:13:01

we're going to

1:13:03

exactly how the the rag setup is happening.

1:13:06

The same thing we are basically explaining

1:13:08

one second, okay, same thing.

1:13:11

Everybody give it a glance piece.

1:13:14

Everybody give it a long piece.

1:13:29

Thank you.

1:13:31

Thank you.

1:14:01

Thank you.

1:14:31

Thank you

1:15:01

Thank you

1:15:03

Thank you

1:15:31

Thank you

1:15:33

You

1:15:35

Thank you

1:15:37

You

1:16:05

So that's a good

1:16:12

So that's a good

1:16:17

that's a good question.

1:16:19

Does rag have a limit on the text it can handle like context window

1:16:23

uh,

1:16:24

of course, of course.

1:16:26

So ultimately whatever input you're giving to the

1:16:29

input you're giving to the rag.

1:16:31

The important thing is that it is that it is retrieving the relevant

1:16:34

the relevant

1:16:35

text, that's not

1:16:37

So if I have to give you

1:16:39

a small analogy, Yuvraj,

1:16:41

this whole

1:16:43

my bookshelf, the library

1:16:45

the entire library will be, let's say

1:16:47

thousands and thousands of words,

1:16:49

billions of words,

1:16:51

so I am not going and

1:16:53

I am not going and fetching the entire thing.

1:16:56

I'm going and only fetching the relevant thing that I require.

1:17:00

Question

1:17:01

question was asked, that question answer

1:17:03

to answer to the information

1:17:04

you need, that's

1:17:06

we're going to retrieve

1:17:07

and that is exactly

1:17:10

what the LLMAs. You can see.

1:17:12

So if I just tweak the system message a little better,

1:17:16

it will be like this.

1:17:17

You have an assistant who can answer general questions based on some

1:17:20

retrieved context.

1:17:22

We'll here here retrieved add

1:17:24

you will be given a question starting with question

1:17:27

and you will be given the retrieved context

1:17:29

starting with context.

1:17:33

Starting with context.

1:17:34

use the retrieved context

1:17:36

to answer the question.

1:17:39

Tuba as I think this is clear to you.

1:17:41

So you, when you

1:17:42

when we're going to retrieve

1:17:44

that ultimately part of the prompting

1:17:46

so the same limitations apply here also,

1:17:50

as Archita has also rightly explained here.

1:17:52

So you can actually see,

1:17:54

you can actually see this whole your context part

1:17:57

right? Yeah.

1:18:00

Okay.

1:18:01

And same same thing for you also, I can't sure, right?

1:18:03

also are not sure, right? So you can see obviously they'll be cost effective. Why they'll be cost

1:18:07

defective? Because you know, so whatever, uh, you're not having to process all the tokens

1:18:13

thing. All the tokens are not being used up right now. You're only retrieving the relevant

1:18:21

information and based on the relevant information the answer is given out. So sara tokens use

1:18:26

not only right? That's the reason. That's the intuition. Why because, uh, why they are cost defective?

1:18:31

Option.

1:18:32

Option?

1:18:33

The other option is?

1:18:34

This is the LLM.

1:18:35

This is the LLM.

1:18:36

This is the LLM.

1:18:38

It's a large language model.

1:18:40

Okay.

1:18:41

Question,

1:18:42

and language has to think.

1:18:44

The model is going to search.

1:18:46

You read.

1:18:47

Context is retrieved and the language model is answering based on the context.

1:18:51

That's the way to look at it.

1:18:54

Okay?

1:18:55

That's the way to look at it.

1:18:56

But the other option is

1:18:58

question is.

1:18:59

You retrieve the entire context.

1:19:01

context, jitnabhi books here available here you retrieve the whole context and based on that you answer.

1:19:06

So if you are able to, if you are answering the question based on the entire

1:19:10

context, the entire retrieved context, do you are answering the question based on the entire retrieved context,

1:19:17

that will be very, very costly, right? That will be very, very costly.

1:19:23

So definitely from that perspective, rag systems are very, very cost effective.

1:19:30

Exactly.

1:19:31

Exactly.

1:19:32

So, the LLM is used, right?

1:19:37

It is also LLM.

1:19:38

No, it is also LLM is not, it is also LLM is.

1:19:41

Our entire discussion, that's why I told you.

1:19:44

I've, this is here here here is a rag.

1:19:46

This is the manual version of Rag upgraded for you.

1:19:49

Rag is this is the way.

1:19:50

So ultimately, LLM is there, YUFRAG.

1:19:52

This is the large language mark.

1:19:54

If you look at the flow of the session today, what did we do?

1:19:57

First, we have asked,

1:19:58

what is the annual revenue of Tesla in this year?

1:20:00

of Tesla in this year, right?

1:20:02

Okay?

1:20:03

This question.

1:20:04

This answer not can't.

1:20:05

Now what am I doing?

1:20:06

I am asking the question, and based on the question,

1:20:09

I'm also giving the context.

1:20:11

So question or context, we have given the context.

1:20:13

So the first part of what you said is absolutely correct.

1:20:15

It will first look at the prong.

1:20:17

It will search for the context.

1:20:18

He will search for the context.

1:20:19

He will retrieve it.

1:20:22

And that's in the pronged,

1:20:23

and that's the whole prompt will.

1:20:25

That's why I explain this to you.

1:20:27

That's why I explain this to you.

1:20:29

See, searches.

1:20:30

So let's retrieve the relevant context, adds to the prompt,

1:20:33

that's the prong, it will be.

1:20:35

Okay?

1:20:36

System message, user message, context, that's a prong,

1:20:38

then the NLM generation answer.

1:20:40

So LLM is right, got it.

1:20:42

I hope that is clear.

1:20:44

Okay, very nice.

1:20:46

All of you got some time to read through this also.

1:20:48

I think this is straightforward.

1:20:50

People have read through it.

1:20:51

So I've demonstrated, like, everyone can see.

1:20:54

This is your knowledge base.

1:20:55

This is your knowledge base.

1:20:56

First time, retrieve the top documents.

1:21:00

context to the pront and this will be how it will be.

1:21:02

Okay?

1:21:03

So I've similarly, you have pronged

1:21:04

used the following context to answer the question.

1:21:07

Document 1, document 2, document 3,

1:21:09

what you've retrieved is your context.

1:21:11

This is your question and based on that,

1:21:13

LLM will answer the question.

1:21:14

This is pretty much the summary of what rags are.

1:21:18

So the first thing is what is

1:21:20

retrieved relevant knowledge.

1:21:21

Retriever will find the relevant information.

1:21:24

Second part is augment the prompt.

1:21:26

So instead of just asking the question,

1:21:28

the first we were only asking the question.

1:21:29

the question. So now, over and above the question, you also give the context. You

1:21:35

augment the prompt, you make the prompt richer. And then finally, you generate the answer.

1:21:40

Generator. So retriever is, augmenter and generator. These are the three components

1:21:46

about it.

1:21:59

Now, let's continue on.

1:22:16

Let's continue the conversation forward.

1:22:19

Let's see some other ideas around what rags are.

1:22:22

I hope everybody is clear with the term rag, retrieval augmented generation.

1:22:27

And why is different from normal generation?

1:22:28

normal generation.

1:22:29

So, first we retrieve, search the information,

1:22:32

prompt to augment,

1:22:33

so question is,

1:22:35

context, and based on that, I'm generating the answer.

1:22:37

And this is the way to remember what I talked about.

1:22:39

If you want, I can print out that system message for you.

1:22:43

You guys can try this out.

1:22:45

We'll demo, okay?

1:22:46

So by the time I close the class, we will do a detailed demo.

1:22:49

So your system message is something like

1:22:51

So you're explicitly stating,

1:22:53

I will give you a question,

1:22:55

you retrieve the answer, and that's how it will.

1:22:58

I'll retrieve the context and based on that, you please answer the question.

1:23:01

So when you're in practice in practice,

1:23:04

then you, you'll,

1:23:05

you're going forward, okay?

1:23:07

Now, moving on,

1:23:11

this is the five-step,

1:23:13

Rack flow, and we will only see the concept in today's class.

1:23:15

As I told you, there is no practicals.

1:23:17

There's only a very small amount of practical we will see today.

1:23:20

And so this is we will see in the upcoming sessions,

1:23:23

starting from next week.

1:23:25

Next week, we will go demos taking on this.

1:23:27

But today, we will only see.

1:23:28

only see the conceptualized work. What is the concept of the right? So these are the five broad steps that we have, ingest, prepare, retrieve, augment, and generate.

1:23:37

So three, four, five, we know what is, but

1:23:40

that before ingest and prepare. These are the two other things we are adding in.

1:23:43

Okay, so before I explain to you, everybody just give it a glance once.

1:23:48

Everybody give it a glance.

1:23:58

everybody please give it a glance the picture is very very self-explanatory. So that's why I'm keeping time for all of you to go through the diagram so that you understand it. Then I will add my explanation.

1:24:28

So the same thing is the same retrieve or generate.

1:24:35

So the same thing is being conveyed in different different ways in these materials.

1:24:39

Just to that view, you are absolutely clear and it reinforces the idea in a better way,

1:24:43

that is all of you, just take two minutes.

1:24:58

Thank you.

1:25:28

Thank you.

1:25:58

Thank you.

1:26:28

Thank you.

1:26:58

Thank you.

1:27:28

Thank you

1:27:58

Okay, guys.

1:28:10

So I think

1:28:12

So I think fairly.

1:28:14

So I think fairly, fairly self-expertating what is going on here.

1:28:20

So let me explain this to what is going on here. So let me explain this to all of you, what are the things we are doing right now.

1:28:24

So first step is basically loading the PDF.

1:28:27

So as I've the Tesla financial report you have to

1:28:30

you.

1:28:31

First you have to load it.

1:28:32

This is the pipeline.

1:28:33

We're in the code in the next class.

1:28:35

So today I'm trying to explain to you.

1:28:37

And here I was trying to explain to you in a conceptual way,

1:28:41

that we're how we are.

1:28:43

But here, this is the actual code thing we will do next week.

1:28:46

So first thing we will go ahead and we will load the PDF

1:28:50

ingest data ingestion,

1:28:52

data loading.

1:28:54

And this is actually

1:28:56

something that will usually be very deep.

1:29:01

And it's many challenges going.

1:29:03

And some of the challenges will be that

1:29:06

in real world, the PDF data,

1:29:09

that data text may be

1:29:10

can be, numbers may be

1:29:11

or images,

1:29:13

so this is going to be a very challenging part.

1:29:17

Next, number two,

1:29:19

prepare the data, chunk and embed.

1:29:23

So let's say if you upload

1:29:26

a particular data, right?

1:29:28

Let's go ahead and say that you upload a particular data.

1:29:32

And a PDF file that is spanning total 100 pages.

1:29:37

Okay, your PDF file is spanning overall 100 pages.

1:29:43

Right?

1:29:45

Now, now the thing is that

1:29:48

what is the concept of chunking?

1:29:51

What do we mean by chunking?

1:29:53

Chunking basically means that

1:29:55

you are taking this entire document and I told you that if you take that entire PDF

1:30:02

or if you take all the PDFs together,

1:30:05

if you have all the PDFs together,

1:30:08

what will happen is that if you take all the PDFs together,

1:30:13

what will happen is that you will easily go above the number of tokens.

1:30:17

Your context window breached your context window will easily breach.

1:30:22

So then what we do is we do divide and conquer.

1:30:24

Divide and conquer, ma'am, what we take one big document and we divide that into smaller chunks.

1:30:31

That's your chunking and embedding.

1:30:33

Very simple.

1:30:34

Actually, these are those one, one step so we have combined.

1:30:38

So first part, what we do is we take each and every,

1:30:42

let me take a pen and try to do this.

1:30:46

If I take a pen, it will be better.

1:30:48

And verdict to answer your question, we'll rock in rock.

1:30:51

Just not today.

1:30:52

Just not today.

1:30:53

Just not today.

1:30:54

to talk about demo.

1:30:55

This is 4 class put out.

1:30:56

Okay?

1:30:57

So all of next week, next to next week is rag.

1:30:59

So I don't, because if we do everything in today's class, then it will be too much exhaustive.

1:31:03

Okay?

1:31:04

So we have enough time dedicated.

1:31:06

But yes, to answer your question, we will be doing the whole thing in crop only.

1:31:09

Don't worry.

1:31:10

Okay?

1:31:11

Okay?

1:31:12

Give me one minute, guys.

1:31:16

Yeah, absolutely.

1:31:17

You're right.

1:31:18

You are right.

1:31:19

You are right.

1:31:20

Embating is like n40.

1:31:21

Perfect.

1:31:22

So we take each and everything.

1:31:23

So we take each and every page and we say each chunk is one page.

1:31:38

We are example.

1:31:39

It may be, may not be.

1:31:42

Now, it may be that one chunk is one page.

1:31:45

It may be one chunk is multiple pages.

1:31:47

So this depend, just to clarify, it is dependent.

1:31:50

Not like going to be a straightforward thing.

1:31:52

thing?

1:31:53

But I'm just saying one chunk is one page based on what we have right now.

1:31:57

So we have a massive PDF.

1:31:58

One PDF will, a thousand PDFs will.

1:32:00

Just many PDFs in your data, you know.

1:32:02

Do chunking.

1:32:04

And we are saying one chunk is one page.

1:32:06

So if you have 100 pages, the end of the end result,

1:32:09

what will?

1:32:10

You have a hundred chunks.

1:32:12

Okay.

1:32:13

Your documents are sections are.

1:32:14

That page one, a chunk is.

1:32:15

Page one chunk.

1:32:16

Page one chunk is.

1:32:17

Chunk.

1:32:18

You're not looking at one massive document.

1:32:21

You are rather looking at.

1:32:22

portions of the document.

1:32:24

So you have a C1, C2, C3, and we go all the way up to C100.

1:32:31

Okay?

1:32:32

So you have different, different chunks are there right now.

1:32:35

Now, next part is embed.

1:32:38

We have chunk and embeds.

1:32:40

So, first, load chunk and embed.

1:32:43

Embedding is what is.

1:32:45

You are taking each and every one of those respective chunks.

1:32:48

Chunks are nothing but sections of the document.

1:32:51

page numbers and whatever. You're taking those pages. You're taking the sections of the document and you're converting them into embeddings.

1:32:58

Okay? You're taking the documents and you're converting them to embedings.

1:33:03

This is how much? Let's take a little bit of time and discuss this.

1:33:08

See guys, one thing I have maintained right from the beginning is that even if we were discussing about machine learning is

1:33:16

machines don't understand non-numeric data.

1:33:21

If you're string do, categorical data do they, machines can't understand

1:33:27

and this we discussed right back in our time when we were doing one hot encoding, if you remember, I dot you.

1:33:35

Because all of these internal mathematics is based on some algorithms and some equations and all that.

1:33:43

Right?

1:33:44

So now the thing is that, if you have any text data here, okay?

1:33:50

text data. If you look at the same story that we are, we've been talking about all this

1:33:55

while, you have an LLM, you're giving a particular prompt, and based on that particular prompt,

1:34:05

you're getting a response. If you do it this way, basically, this prompt is just basically text, right?

1:34:12

This prompt, this is nothing but text data. It's texty. Now, if you ask a text question,

1:34:19

question, LLM to what can't understand?

1:34:24

He doesn't know, no, no, I don't know.

1:34:26

Machine only understands numbers.

1:34:30

So this is very much like the encoding that we were discussing in our machine learning session.

1:34:36

Related to that, something very similar to encoding we were discussing.

1:34:41

And we're in this in what we take that text and we convert that text into a sequence of numbers.

1:34:48

of numbers.

1:34:50

I'm a numeric memory moment we convert to take.

1:34:53

So, whenever you're next time, any prompt,

1:34:56

you know,

1:34:58

you're asking what is the weather tomorrow,

1:35:00

like we have a question asked,

1:35:02

that does Sion have skills in

1:35:04

air gap, generative AI systems and all,

1:35:07

you know, these kinds of things.

1:35:09

For humans, it is English.

1:35:11

But when you're sending that prompt through the large language model,

1:35:16

that language model,

1:35:17

don't know that English is.

1:35:19

You have to take that particular,

1:35:21

so you have to take that English prompt

1:35:24

and you have to, and internally it has to be converted into

1:35:27

some kind of an embedding, machine-readable form.

1:35:31

And that is exactly what the concept of embeddings basically are.

1:35:35

These embeddings are not understood by a human being.

1:35:37

This humans can't understand.

1:35:39

As you, you see, here here, C1, C-2, C-3, C-100, chunks

1:35:42

chunks are nothing but sections of text.

1:35:46

Text, prompt.

1:35:47

anything can say we are here.

1:35:49

Here we're prompt pulled.

1:35:50

I mean, if you ask a question,

1:35:53

what is the weather?

1:35:57

So, we're for English.

1:35:59

English question is, right?

1:36:01

But in behind the scenes, what is happening is that

1:36:03

this, this question is basically

1:36:05

converted into prompt embeddings, which is nothing but 0.11, 0.12.

1:36:10

These are the prompt embeddings with respect to the question.

1:36:14

So prompt and it's corresponding embeddings are 0.11.1.

1:36:16

Point 1.

1:36:17

So these are the numeric representation of the prompt.

1:36:22

That's what you're able to see on this screen right now.

1:36:24

Numeric representation of the prompt.

1:36:26

That's the idea.

1:36:28

Now, moving on, now moving on, what we can do.

1:36:33

We can move back and, you know, yeah, sorry.

1:36:37

This is the numeric representation of the prompt.

1:36:39

We are able to see.

1:36:40

Okay, question, question, answer.

1:36:42

We'll talk about this one, right?

1:36:44

So that's the part we saw.

1:36:46

solve, right? Now, moving on,

1:36:50

same way is happening here also.

1:36:55

Now, if you ask me, sir, what does 1.1 and 0.12 mean?

1:37:00

What do these two things actually mean?

1:37:02

What is the meaning of 0.11? What is the meaning of 0.1?

1:37:05

That is open-ended.

1:37:07

That is not interpretable.

1:37:09

That is not interpretable.

1:37:11

Okay.

1:37:12

So there is your C1.

1:37:14

There is your C2.

1:37:15

There is a C2. There's a C3.

1:37:18

All the way it goes up to, there's a C-100.

1:37:21

So each and every chunk we have.

1:37:24

And for each and every corresponding chunk, we can also see what are the chunk embedded?

1:37:27

You can see what are the number.

1:37:29

These numbers are not having any meaning to the human being.

1:37:33

These numbers have no means.

1:37:35

And if you want to understand this is a little bit more in detail.

1:37:39

These numbers are generated by a neural network.

1:37:41

A neural network use, you have numbers to generate

1:37:44

Right? But conceptually, conceptually, this is basically your, what we refer to as, what is this thing?

1:37:56

This is basically what we refer to as chunk embeddings.

1:37:59

You take the data, you divide the data into multiple chunks, C1, C2, C3, so and so forth.

1:38:05

And you take each and every chunk and you convert them into a vector of numbers.

1:38:09

So these embeddings, these embeddings, these embeddings,

1:38:14

These embeddings, let me write it down.

1:38:22

So individually the numbers make no sense, but collectively these embeddings are giving you.

1:38:29

They are giving you the contextual meaning of the chunk.

1:38:44

Collectively, these embeddings are giving you what is the contextual meaning of the chunk.

1:38:49

That is what these chunk embeddings are giving.

1:38:52

They're telling you what is the contextual meaning of the chunk.

1:38:56

So individually, those embeddings mean nothing, the numbers mean nothing.

1:39:00

But you are able to understand what is the contextual meaning of the chunk.

1:39:07

That's one way to look at this whole thing.

1:39:12

So that's one way to understand.

1:39:14

the whole thing overall.

1:39:17

So just to repeat again, ingestion has been, PDFs for loaded in the system in.

1:39:23

We have done the chunking, we have converted the PDF into different chunks, 100 chunks,

1:39:28

C1, C2, C3, up to C00.

1:39:31

And we have also converted those chunks into a pettings.

1:39:35

Next, what you will do, this is the part we will to retrieve augmented.

1:39:39

Three, four, five, them done already discussed here in detail.

1:39:42

But you can see the summary.

1:39:43

Very nicely given here.

1:39:44

So the user will ask a question.

1:39:47

User will ask you, and this chunks are, guys,

1:39:50

this is a vector database store in.

1:39:53

So PDF, we have,

1:39:56

So PDF here,

1:39:57

every chunk is one page.

1:40:00

As an example, chunks,

1:40:01

there are some other be other can that we will again see next class.

1:40:04

What are the types of chunking?

1:40:06

Now you'll say, if it's just page-wise

1:40:08

or some character-wise it is.

1:40:10

We will see all that.

1:40:11

But for now, to understand the concept,

1:40:13

chunk, we are divided.

1:40:14

dividing the document into smaller sections.

1:40:16

So here on page-wise chunking considered.

1:40:18

So how many chunks do we have right now?

1:40:20

We have total 100 chunks.

1:40:22

Or each and every chunk, we have also converted them to their respective endings.

1:40:27

So chunk 1's embeddings here is chunk 2 embeddings are this.

1:40:30

Chunk 3 embeddings are this.

1:40:32

But not all the way to chunk, 100 embeddings are this.

1:40:35

So we have converted each and every chunk into their corresponding embeddings.

1:40:40

So chunk 1, chunk 2, chunk 3, chunk 100.

1:40:42

So these are the corresponding embeddings

1:40:44

it has better the chunks. That's the way how we are able to get it.

1:40:48

And finally, finally, you will go and save all this. You will go and save all this.

1:40:55

Save all this.

1:41:00

Save the chunks and they are embeddings.

1:41:12

in a vector database

1:41:23

You have SQL here.

1:41:25

Everybody has done SQL in this class.

1:41:27

In SQL, you are all used my SQL, relational database, tables,

1:41:31

column, row, select star.

1:41:34

You guys have got a basic flavor of that.

1:41:36

So vector database is a special kind of database.

1:41:38

It is not a relational database where your tables are now there.

1:41:41

So vector.

1:41:42

database is a special kind of database where your data is stored like this.

1:41:46

Yeah, your database will.

1:41:48

Okay?

1:41:50

And here your chunks will.

1:41:52

C1, C2, C3, like that, all the way up to C hundred.

1:41:57

These are all the chunks here are stored over.

1:41:59

And these into the numerical embedding for those chunks.

1:42:02

As say, manu, this point one, point one, point one, two, it is.

1:42:05

This point one, point one, t is.

1:42:08

Like that.

1:42:09

So these numbers mean nothing, but it tells you what is the contextual meaning.

1:42:11

what is the contextual meaning of the concept?

1:42:13

What the concept?

1:42:14

What the statement, that, the chunk,

1:42:16

there the text is, the context is,

1:42:18

that's one way to be correct.

1:42:20

Yeah.

1:42:21

Yeah.

1:42:22

You're correct.

1:42:23

You're absolutely correct.

1:42:25

Absolutely correct.

1:42:26

That is correct.

1:42:27

Until now.

1:42:28

Until now, what we have discussed, step one and step two,

1:42:30

what you said is absolutely correct.

1:42:32

Okay?

1:42:33

Now, now, what we are,

1:42:34

now we have got all our chunks

1:42:38

safely stored in a vector DV.

1:42:40

this is a vector db, okay?

1:42:42

And believe it or not, guys,

1:42:48

we're just,

1:42:49

we're talking about,

1:42:50

we're discussing,

1:42:51

believe it or not, its code is like one line,

1:42:53

one or two lines,

1:42:54

there's no,

1:42:55

that's why the coding part is the easiest for it,

1:42:57

who will see, okay?

1:42:59

So now we have got all the chunks

1:43:01

and all they are corresponding embeddings stored in the vector dv.

1:43:04

Vector in vector dv in

1:43:05

it's stored,

1:43:06

chunks be stored

1:43:07

and its corresponding embeddings be stored

1:43:09

in the vector Dibu.

1:43:10

Now, what we will do?

1:43:12

We will go and do something for a retrieval.

1:43:15

Now we will go back and do something for a retrieval.

1:43:18

And here we will ask a user question.

1:43:21

As part of retrieval, what we will do?

1:43:23

We will go and ask a user question.

1:43:26

Search in the vector store, find out the similar charts,

1:43:32

and add it to the context.

1:43:35

Exactly what we were discussing before.

1:43:37

So retrieval what we do?

1:43:39

we find the chunks closest to the user question.

1:43:42

Or this is how it will discuss next class.

1:43:44

Next session, that is the plan.

1:43:46

Mathematically how it's done.

1:43:48

But the concept is,

1:43:49

here here here, the user will ask the question,

1:43:52

that what is the transformer architecture, whatever.

1:43:54

And then you go and look up in the vector store,

1:43:57

whatever vector db we have.

1:44:00

So, if you want me to go, let's say, one level of detail,

1:44:04

I can do that, no problem.

1:44:05

I can do that.

1:44:06

Let me go one level of detail.

1:44:07

So user will ask the question.

1:44:09

User questions.

1:44:10

So, let us take a story.

1:44:13

Let us say this is the, you know, this is the ITR manual.

1:44:16

This is your HR manual, okay?

1:44:19

It is part of a company.

1:44:26

Company's a HR department, it's a manual is.

1:44:29

Manual in manual, in all guidelines,

1:44:31

but HR policies are guidelines.

1:44:33

People might have questions like,

1:44:35

how many leaves I get in here,

1:44:36

a year, how bonus will, how compensation will.

1:44:39

So all these kinds of questions are taken up in the HR manual.

1:44:42

Okay.

1:44:43

So we have taken the PDF, 100 pages, chunking here,

1:44:47

chunk embeddings generated here.

1:44:49

For each of the chunks, we have created embeddings.

1:44:51

And we have saved all that in a vector team.

1:44:53

That, okay, until now, story is complete.

1:44:55

Now, coming to the user query.

1:44:58

User query, what is?

1:45:01

User query is, how many leaves?

1:45:06

How many leaves we get in a year?

1:45:21

Just to read this out, the query, the user will ask a question.

1:45:25

How many leaves we get in a year?

1:45:29

Again, understand which context, without context is the part

1:45:32

this is the question you, you're asking,

1:45:35

the answer to that question will be in the HR documentation.

1:45:39

That's the answer not?

1:45:41

Answer not?

1:45:42

Answer, there are there.

1:45:44

So you ask a question, how many leaves we get in here?

1:45:47

The answer to that question will be in the user documentation.

1:45:52

I repeat again, the answer to this question will be in the user documentation.

1:45:56

So we will simply go to the user documentation and we will fetch the answer to the question.

1:46:01

That's it. Okay.

1:46:03

The answer to the question.

1:46:04

Okay.

1:46:05

How many leaves we get in a year?

1:46:07

So this is how to retreat the information?

1:46:10

So subse pre-first, the query is, the prompt.

1:46:13

I already told you whenever you write a question,

1:46:15

machines don't understand the text.

1:46:17

You will have to go and convert that into what we refer to as query embedding.

1:46:21

Query embedding, you take the original user query

1:46:24

and you convert that entire user query into what we refer to as query embedding.

1:46:28

That's the way how we go back and do it.

1:46:31

You take the original user query and you convert that

1:46:34

you convert that original user query into what is referred to as query embody.

1:46:40

You take the individual query and convert it into a sequence of numbers, query embedding, basically.

1:46:46

Now, you take the query embedding, let's say, I'll take an example.

1:46:53

Here you have an example case of C layer.

1:46:55

I can also specify the numbers accurately so that you can understand.

1:47:00

Let's say C1 is a different color.

1:47:03

is 0.1.2.

1:47:07

C2 is 0.11.1.

1:47:12

And C3 is 0.8.9.

1:47:18

And C100 is 0.7.8.

1:47:22

So we have some sample numbers here.

1:47:25

So I'm just saying these are the corresponding embeddings for these respective charts.

1:47:30

As an example.

1:47:31

We can how we will that we'll tell you.

1:47:34

We can make them.

1:47:35

We can't make them.

1:47:37

And we can see that what embeddings are we can see that also, what those embeddings are actually.

1:47:44

So what we have done, we have taken the chance and we have stored that in a vector degree.

1:47:51

Now when the user asks the question, that the user's query is that we'll be in embedding in embedding.

1:47:56

Embedding, we are taking the text and you're trying to encode that in a certain way.

1:48:00

certain way. So query encoding embedding kithna how?

1:48:05

Yeah, B manu, something like 0.1.

1:48:08

So now, that is the corresponding query embedding that you are getting.

1:48:24

So now the question is based on the query embedding, based on the query embedding, based on whatever query embedding

1:48:30

that you are able to see. You will go back and look up in the vector TV and you will find out,

1:48:35

you will try to find out what the corresponding chunk embeddings actually are.

1:48:39

So based on whatever query embedding you're seeing, you want to find out what are the similar

1:48:42

query chunk embeddings. What are the similar chunks that can help you answer that question?

1:48:48

That's the concept of question.

1:48:50

Question is the query here.

1:48:51

How many leaves we get in a year?

1:48:55

That is the user query you are even to see.

1:48:57

So based on that particular user query that,

1:49:00

we're able to see on this pane. You go and look up in the vector d. You go and look up in the corresponding

1:49:08

vector db and you try to find out what the similar chunks actually are. So you go and look up in

1:49:16

the in the corresponding vector db and you try to find out what the similar chunks are. Which

1:49:23

are those chunks where the things are matching, the embeddings are actually matching? What are the similar

1:49:29

chunks from the vector team. So that is what you're trying to find out.

1:49:33

So what you're going to do?

1:49:35

You go and look up in your vector tibing. You go and look up in your vector tibing.

1:49:40

You, all these chunks check out of those hundred chunks, which are those chunks?

1:49:46

Or chunks, much of the pages, documents, the parts.

1:49:49

Which of those chunks of the PDF?

1:49:52

Who are the chunks are very similar to the question that is asked?

1:49:56

So you can now, now,

1:49:58

Now do a vector source search. You can find out the top K results and we can retrieve those

1:50:07

chunks. This is your retrieved context. Just for simplicity. In my retrieved context, I basically

1:50:15

have C1 and C2. Because you can see that as for the example I've taken, my query embedding

1:50:22

that is only 0.11.1.2. But my chunk embedding is basically which of the chunks it is similar to.

1:50:28

you can see that it is similar to only c1 and c2 distance formula so we can say that hey

1:50:36

based on whatever question i'm asking we have the question i'm asking him we

1:50:38

the question of the similar answers

1:50:42

how are they?

1:50:43

That's the answer possibly c1 or c2 say either

1:50:46

so this is my retrieved context

1:50:48

so what you're seeing here this is my retrieved context

1:50:51

c1 and c2 is my retrieved context

1:50:54

so you have two is my retrieved context

1:50:56

so you have two things right now

1:50:58

As we have you have something called, you have something called this thing, you have

1:51:05

something called this thing, you have here

1:51:08

basically the system instruction, as we have you

1:51:11

have a prompt,

1:51:12

the retreat context or a user query.

1:51:14

This will be a complete prompt.

1:51:16

This is exactly what we wrote a while file.

1:51:18

We have you in GROC in GROC in the

1:51:20

I had a system message

1:51:22

so the whole prompt is this is a system message

1:51:24

will be very explicitly state that the system to

1:51:27

like it will have a question it will have a context and based on that can get the answer

1:51:32

so that is a system message.

1:51:34

You have to give the retrieved context

1:51:36

that the whole context you've retrieved here, C1, C2.

1:51:39

Question basis, this is a similar chunk

1:51:41

that the full context retrieved was,

1:51:43

that you'll have the context

1:51:46

and the original user query.

1:51:48

These three things will call the prompt.

1:51:51

And based on that,

1:51:52

prompt, you will go and call the LLM.

1:51:55

You'll make the LM API call.

1:51:56

maybe I call and it will get the answer.

1:51:58

So benefit is what?

1:52:00

Benefit is the benefit is that it with context

1:52:01

here.

1:52:02

Now we're not only,

1:52:04

this is the first thing not.

1:52:05

You can't say,

1:52:06

good guys.

1:52:07

This one was the first

1:52:08

the prompt only consisted of system and user.

1:52:11

System is normal instruction and user

1:52:13

message is like,

1:52:14

hey, what is the annual revenue of this company?

1:52:16

So, LLM is not know.

1:52:18

If you've only this prompt

1:52:19

if you've only this prompt linked

1:52:20

LLN will not know,

1:52:21

it has context not without context

1:52:23

without context here.

1:52:24

So only difference you have done is

1:52:25

we have done is,

1:52:26

about me.

1:52:27

That's it.

1:52:28

Now we have instruction

1:52:29

did, context,

1:52:30

asked,

1:52:31

all of all of everything

1:52:32

and based on that it is responding.

1:52:34

And what is the benefit of the RAG pipeline?

1:52:37

RAG is helping you to retrieve their context.

1:52:40

So that is why it is cheaper.

1:52:42

So instead of uploading the, instead of giving a massive context,

1:52:45

the whole context I'm not doing.

1:52:47

So privacy was maintained and you're also able to keep it economical.

1:52:51

It is you're only passing what is required as students.

1:52:56

So that is the whole idea of operates.

1:52:58

This is the basic idea.

1:52:59

So top K is what is related to this kind of function.

1:53:02

Updix sacked your vector store is, you know, this is, we are retrieving the top K results.

1:53:07

Top K, for our question we are saying top two.

1:53:11

Again, there are many, many different paradigms for how many we want to retrieve.

1:53:15

But here top K, based on whatever question you are asking,

1:53:19

we are trying to retreat the top two similar chance.

1:53:23

And Archit has also explained this in a very detailed way.

1:53:25

length is in a very detailed way.

1:53:28

But as top P is a lot of a model level more thing, something else.

1:53:34

Okay.

1:53:35

So if top K is the subset of this is what top K means.

1:53:37

But otherwise, NLR level also is a different thing.

1:53:41

Ah, that's a very good question, Ankit.

1:53:43

It has to, it has, it will be, it's the closest match.

1:53:46

Closer match.

1:53:47

Top K in top K.

1:53:48

Top K in mode, which are the top two chunks which are closest to my query and wedding.

1:53:54

Close this match.

1:53:55

Exactly how match?

1:53:56

Exactly.

1:53:57

Can you match?

1:53:58

Can you ask you?

1:53:59

The context of the question will never match what is there in the pinch.

1:54:04

So embeddings are always contextual in nature.

1:54:08

You asked a question, you asked a particular question, and then you are converting your prompt into embeddings.

1:54:15

You ask a particular question and then you are basically converting your prompt into what is referred to as embeddings.

1:54:22

You are converting in embeddings.

1:54:24

convert.

1:54:25

Exactly.

1:54:26

You are converting that entire prompt into embeddings.

1:54:30

And these embeddings are basically what is telling you the contextual meaning of the problem, the chunk.

1:54:37

The chunk.

1:54:38

The text is, the text is basically, what is the contextual meaning of those chunks?

1:54:44

That is what the contextual meaning of those chunks.

1:54:46

That is what the embeddings basically contain.

1:54:49

So if you're asking a question,

1:54:51

question in question about questions.

1:54:53

question is what is the contextual meaning of the question?

1:54:58

So you are trying to find out the question is the question is what's similar chunks?

1:55:03

So best match, closest match.

1:55:07

That we will see later how to select is part of the next week discussion.

1:55:12

Then we're going to look at it.

1:55:13

We're programatically, but that is for a later discussion.

1:55:16

Okay.

1:55:17

For now, just conceptually, we are trying to understand that it's okay.

1:55:21

But K can value 2b or 2b or 2b.

1:55:22

can be 3b or 4b or can.

1:55:24

So when we come to the coding part, we will see how that is happening.

1:55:27

Okay?

1:55:28

That we'll get.

1:55:29

We'll try to see this.

1:55:31

We'll try to see this.

1:55:32

That is right, Sanghita.

1:55:37

You have summarized it very nice.

1:55:42

Correct.

1:55:44

That is right.

1:55:45

So this is the 5-step rag pipeline, which I wanted to take all of you through overall.

1:55:50

So I have this is a more diagram.

1:55:51

more diagram which you know I find it very useful so that it you know let me share that also with you so that everyone understands it

1:55:59

it a nice pictorial representation of rag

1:56:11

this is our another diagram in there.

1:56:14

Very nice intuitive understanding.

1:56:16

This is a little more visually changes in what we are going to do.

1:56:20

Okay.

1:56:21

So again, there on the textbook wall of what whatever.

1:56:25

Ingestion.

1:56:26

That's the part where you're taking the PDF.

1:56:29

It can be one PDF.

1:56:30

It can be several thousands of PDFs.

1:56:32

You're looting the entire document of the PDFs here right now.

1:56:38

Next is you're going ahead and chunking it.

1:56:41

You're taking the entire document and dividing that into 100 chunks, C1, C2, C00.

1:56:46

So chants divide it.

1:56:48

And then you're taking each and every one of the chunks.

1:56:50

one of the chunks and you're converting them into

1:56:53

embeddings, chunk embeddings.

1:56:55

So here vector TV is here.

1:56:57

This is the first part.

1:56:59

Document,

1:57:00

then, then it's in chunks divide

1:57:01

and then you based on embeddings.

1:57:03

So all this is the vector TV.

1:57:06

Next workflow, here to come.

1:57:08

Next workflow, what we are doing,

1:57:09

we are starting with the quail.

1:57:11

Question asked, the user has asked

1:57:12

question question to embedding in embedding

1:57:14

convert the retriever goes to the vector TV,

1:57:17

retrieves the top to similar chunks,

1:57:19

okay, and then.

1:57:20

then it is passed as a context to the LLM and based on the relevant to the answer.

1:57:24

So LLM has now what are the things the LLM has?

1:57:29

LLM has the original user question.

1:57:31

Original question, right?

1:57:33

This is the original user question the LLM has.

1:57:38

Original user query.

1:57:41

This is the retrieved context.

1:57:50

And when you go back and combine the two things together, you end up getting what is called the user message.

1:57:58

So we combine the user message with the system message to get the panelists.

1:58:08

That's the way how we go about it.

1:58:10

Okay.

1:58:11

So we ask the user question and based on the user question we retrieve what are the similar chunks.

1:58:16

We retrieve the context.

1:58:17

Based on the user question, we retrieve the context.

1:58:19

Retreat the context.

1:58:20

retrieve context higher and based on that we get the response.

1:58:24

So that's the whole idea of rags are multi notes.

1:58:28

Okay? Yeah, yeah, Sangita. See, majorly it is all our notes.

1:58:34

So the rag notes are very nice. This, this, our team will upload it tomorrow only. Don't worry.

1:58:40

It's from a massage tool notes only, what I'm talking about.

1:58:43

Okay, because it's very nicely documented today. So that's why I'm referring and I'm sharing this from the notes itself.

1:58:49

Okay.

1:58:50

Yeah. This will be shared with you in your LMS by tomorrow.

1:58:54

Yeah. Also a doubt first four steps of rank are different from LLM and the last is LLN technology used to be.

1:59:00

Absolutely, absolutely. Absolutely.

1:59:01

First four step in no LLM using not. Your absolutely right.

1:59:04

You're absolutely right.

1:59:06

Ingest, prepare, ingest, prepare. Ingest,

1:59:10

here. You're absolutely right.

1:59:13

LLM is only coming at the end. Absolutely.

1:59:16

Absolutely.

1:59:17

Okay.

1:59:18

Okay.

1:59:19

Okay.

1:59:20

Very good questions, guys. This is another particular understanding.

1:59:25

Documents, repair chunks and beddings, vector db.

1:59:28

Then what's what the user asks the question. You look up the similar chunks and get the answer.

1:59:34

This is just one more way to understand how it is happening.

1:59:41

So the important term that I wanted to clarify again is retrieval augmented generation, retrieval or generation.

1:59:47

But a penny, we are retrieving. The retrieving the retriever

1:59:50

finds the information and a generator is the element that writes the answer.

1:59:54

That's it. Retrieval or generation. These are the two things that you will have to keep in mind.

1:59:58

And one other very, very important thing. This is another thing you can see. Find the relevant

2:0:03

information of knowledge sources. Retriever's work. So what's going to be. As a like an open book

2:0:08

example, you're asked a question. The retriever's job is to go back to the relevant information

2:0:14

knowledge sources. Go through all the knowledge sources and find out the relevant information.

2:0:19

okay so you have the all the knowledge sources so from all the knowledge sources you find out the relevant information

2:0:27

the retriever will only do that you can retriever will only do that and finally the generator what will

2:0:34

do the generator will go and use all the notes to write and generate a clear accurate answer that is what

2:0:40

the generator will do but the retriever will find the relevant information and the generator will generate

2:0:46

very accurate answer. That is what the generator will do. That's the idea behind what

2:0:51

rags really are. So two important components. Retriever are generated. Obviously,

2:0:58

augmentation was the part that we talked about. And there's one more important thing I want to clarify.

2:1:03

This is called grounding. Grounding. Grounding means means that use only the retrieve notes to generate the

2:1:08

answer. Don't make it up. This is one more important concept of rag.

2:1:14

But, manu, go back to that exercise where I gave that PDF.

2:1:19

I mean the PDF up to you do some time back, right?

2:1:21

So, if you go back to that PDF and think back to that exercise once again, I uploaded a PDF.

2:1:29

And I asked the question, that what is the annual revenue in the year 2022?

2:1:39

I'm me that question, right? And if you think about it,

2:1:44

The objective of a rag system should be look up from the document and answer questions

2:1:51

from the document. I do not want the NLM to use his own intelligence to answer the question.

2:1:58

I will ask you one question. You have a question. You can't just go ahead and search

2:2:04

you, you, you, you, you're retrieve for open book exam,

2:2:06

the question asked you, you go and search, retrieve, what you need, and then

2:2:10

question answer to. So the answer must be grounded in the answer.

2:2:14

the retrieved context.

2:2:16

The context of the information is, your answer to be that is also very, very important thing about grounding.

2:2:21

So please keep that at the back of your mind.

2:2:24

So the answer must be based on the retrieves content.

2:2:31

Exactly.

2:2:31

Very good question.

2:2:33

We will do grounding exactly in the system problem.

2:2:35

And we'll just do this kind of this way to do.

2:2:37

Okay, we'll give it this live demonstration.

2:2:40

This go this way to show.

2:2:40

So if the answer, I'll tell you.

2:2:44

about okay if the answer to the question is not is not present in the

2:2:54

the retreat conflict please stay I don't know

2:3:14

This is a very, very important thing that I wanted to talk about.

2:3:18

Okay.

2:3:21

One more time, repeat.

2:3:22

Okay, no problem.

2:3:23

See, what we discussed here is basically, uh, two things are, right?

2:3:26

We are talking about the concept of retrieval and generator.

2:3:30

So, okay.

2:3:30

Can we take a break and come back?

2:3:32

It's basically, uh, ah, five, five.

2:3:35

Almost fine.

2:3:35

Okay, leave it.

2:3:36

We can take a short break in another two minutes.

2:3:39

So, uh, yeah, Sanquita, just to repeat this once again for you.

2:3:42

So we basically have a retriever.

2:3:44

Retriever's responsibility is what?

2:3:47

You ask the question.

2:3:49

The retriever will retrieve the relevant information from all the knowledge sources.

2:3:54

That is what the retriever will do.

2:3:57

And then generator will generate the answer.

2:4:00

I hope you're clear with that.

2:4:02

Now, grounding can what is the meaning of grounding?

2:4:05

Grounding means that your answer must be grounded in the notes.

2:4:12

Whatever information we are retrieving,

2:4:14

whatever information we are retrieving, your answer must be from the retreat content.

2:4:20

Your answer must not be like a generic answer.

2:4:23

The answer to the question should be from the retrieved context.

2:4:27

That's the way to the problem.

2:4:27

So the answer to the question must be from the retreat context.

2:4:31

That's the basic idea.

2:4:34

So, okay, so, because, Sankitha, I think you can relate to this one in a better way.

2:4:39

Abdiqo, you have a system message, take it.

2:4:42

So I'm explicitly stated.

2:4:44

in the system message that your question will start with question and the retrieved context

2:4:49

will start with context and we are explicitly saying please use the retrieved context to answer

2:4:54

the question and we are also saying this is the last one very very important point the last point

2:4:59

we are explicitly saying that if the answer to the question is not present in the retrieved context

2:5:04

please say I don't know okay I hope this is clear to you Sangita does it make sense

2:5:09

to mother manu here here we have here our whole context that Tesla financial report

2:5:14

okay, got it?

2:5:15

Now this is very interesting.

2:5:16

This whole context is, okay?

2:5:17

And now I will say, now I will say, for the question, sort of funny over,

2:5:21

okay, when, you know, when did, when, oh, sorry, edit

2:5:25

to edit kind of, okay, when did man first land on the moon?

2:5:29

Isn't, right?

2:5:30

Now, now, you know, okay?

2:5:33

When did man first, just, you know, man in sort of biased, right?

2:5:40

First man is land to, but let's say, when did, did, humans first, first.

2:5:44

humans first land on the moon, okay?

2:5:48

Human's first land on the moon.

2:5:50

Now, very interesting, if you look at this one,

2:5:54

you think, what are you?

2:5:55

What are you? So, very clearly,

2:5:58

the question is,

2:6:01

context is,

2:6:01

and context in this way,

2:6:03

answer to say, I don't know.

2:6:05

Exactly.

2:6:05

Exactly.

2:6:06

That answer will.

2:6:06

That answer will.

2:6:08

Finger crossed, I hope.

2:6:09

Okay, yeah, one second.

2:6:12

Answer will, I don't know.

2:6:14

Okay?

2:6:15

Yes, yes.

2:6:17

Okay, very good.

2:6:18

Hallucination is a technical term.

2:6:20

You've got a little advanced term used.

2:6:21

But you're absolutely right.

2:6:23

Grounding is the way to reduce hallucination.

2:6:25

You're right.

2:6:26

So we are able to get answers which are grounded in the context.

2:6:29

So, look, now you're, now,

2:6:30

you're asking, when did humans first land on the moon?

2:6:33

This is basic question, is, right?

2:6:34

We're able to answer.

2:6:37

It will be able to answer.

2:6:39

But what you are explicitly saying,

2:6:41

your application should use only the concept.

2:6:44

context to answer the question.

2:6:46

So when you go and ask this question, it says, I don't know.

2:6:49

I'm sorry, whatever context you gave me, boss, I don't have the answer in that context.

2:6:53

This is the concept of grounding.

2:6:56

I hope you are clear, everybody.

2:6:57

And I think, uh, uh, I hope you're also clear, right?

2:7:02

This this should clarify.

2:7:03

This is, this is exactly what you were, what you meant, I think, again, this, this part.

2:7:09

Gotcha.

2:7:10

So now, moving on.

2:7:12

Let us continue on.

2:7:14

So this is with context without context of cheese.

2:7:16

We've already defined what is with context and without context.

2:7:19

Let us move on.

2:7:20

Now there is another interesting part, which is called rag versus fine tuning.

2:7:24

At a very basic level, what is the difference between the tool, let us see that.

2:7:29

What is the concept behind this?

2:7:32

So rag, fine tuning is basically at a very high level.

2:7:36

At a very high level, what we are doing?

2:7:39

We are explicitly going back and trying to change the model itself.

2:7:44

It means, we have a GPD, we have a language model, Lama 3.3, 70 billion versatile model.

2:7:53

So when do you find you me?

2:7:55

So, and I also explained to you, at the beginning of the class, I also explained to you,

2:7:58

that whenever you talk to a large language model, whenever you talk about the large language model,

2:8:04

that particular large language model is trained on a tremendous amount of data.

2:8:08

That particular LLM is basically trained on a tremendous amount of data.

2:8:14

and it has a lot of knowledge and context with respect to its own data.

2:8:23

It has a lot of knowledge and context with respect to its own data.

2:8:27

It already knows a lot.

2:8:29

So that is what this Lama 3.370 billion versatile model is.

2:8:33

It has a lot of knowledge and context over all of its own data.

2:8:36

That's a thing.

2:8:37

Now, fine tuning is what is.

2:8:41

Fine tuning is what is?

2:8:43

what I mean it is, you know, your company has some other data.

2:8:46

You have your company's data.

2:8:48

You can look at that company's data to be,

2:8:51

this is usually very costly, we rarely do it.

2:8:55

We rarely do it.

2:8:56

Even the biggest of companies, they rarely do it.

2:8:59

Because there are two reasons.

2:9:01

A, it is very, very costly, and B, it is extremely,

2:9:05

you know, security-wise, it's a big risk.

2:9:08

So I for open AI platform to go.

2:9:10

This is platform.

2:9:11

This is platform.com.

2:9:12

So same story.

2:9:13

Like we discussed in CROC in CROC report.

2:9:18

So here also you have a chat interface.

2:9:20

And you can absolutely go and have system message, user message.

2:9:25

You can choose different models.

2:9:26

So same story.

2:9:27

Okay, this I made in class in class explained here.

2:9:29

And if you go to code, you can, you know, chat completion screen.

2:9:33

Same way it will happen, right?

2:9:35

And if you scroll a bit down,

2:9:36

here here your fine-tuning option will be.

2:9:40

Unless they've removed it.

2:9:42

So they have a fine-tuning section here.

2:9:49

Let me see.

2:9:51

They might have put in a different place.

2:9:55

Yeah.

2:9:56

Yeah, here.

2:9:57

Or maybe it is actually taken away from my phone.

2:10:01

Just a second.

2:10:03

See, you can see, you can't,

2:10:05

momentarily, he came here.

2:10:08

Can he see?

2:10:09

He came and then.

2:10:10

Then there is a reason.

2:10:12

There's a reason behind that, because we have our credits

2:10:15

not that could be one of the reasons.

2:10:17

If you just observe,

2:10:19

I'm a page to refresh here.

2:10:21

For a second, it will come and then it will go away.

2:10:23

Look at the left and side.

2:10:25

It will come in the second.

2:10:26

Here.

2:10:27

And then the intuition here is that

2:10:31

maybe they have shifted it somewhere in page.

2:10:33

Maybe they have shifted it somewhere in page.

2:10:35

No, there will be a bit.

2:10:37

I mean limits.

2:10:42

No, they actually become very restrictive right now.

2:10:48

Anyways, that's a different thing.

2:10:49

So fine-tuning basically you can do on these kinds of platforms and what, and the idea is that you can take any model.

2:10:54

You can take all these, Lama, all these models you can take.

2:10:58

You can take, the models already putty models take, you can't take up.

2:11:01

You can't putty models, and you can't data from data from models back to fine-tune

2:11:05

person. That is the concept of fine-tuning, basically.

2:11:08

And just keep this at the back of your mind. Fine-tuning is something we will be,

2:11:12

we will not be very concerned about, but just keep this at the back of your mind.

2:11:17

So you're able to kind of completely modify this particular model with respect to your own data.

2:11:24

But rag, we're not doing.

2:11:26

Rag in the model not touch not.

2:11:28

So that's the reason why the topic is called rag versus fine-tuning.

2:11:31

Because we're fine-tuning in what we have the knowledge.

2:11:34

We have the knowledge and we are basically training the entire thing.

2:11:37

We are basically like, if you look at it, we are kind of training the entire thing on our, on our own data.

2:11:46

We have GPD model here.

2:11:48

We have Gemini model.

2:11:49

We have Lama 3.70 billion model.

2:11:54

We are simply using that model.

2:11:56

We are adding a CSV pipe. We're adding our own data.

2:11:59

And based on that, we are retraining it.

2:12:01

And we're going to retrain it.

2:12:03

so that it understands our data.

2:12:05

So that it's knowledge we were discussing about knowledge cut off and all, right?

2:12:09

That current knowledge reflects my data.

2:12:13

So we're making it in the model we are baking it in.

2:12:15

We are baking it right into the model.

2:12:17

But in RAD, what we are doing is,

2:12:19

we're not touching.

2:12:21

The model is the same LLM is.

2:12:23

When we talked about retrieval augmented generation,

2:12:25

this LLM part is only coming at the end.

2:12:28

So here we are using external document to get the answer.

2:12:31

But that external document is not direct.

2:12:32

But that external document is not direct.

2:12:33

directly baked into the LLM.

2:12:34

is a separate entity.

2:12:36

What in doing?

2:12:37

What we do?

2:12:38

We need to do this thing is really

2:12:39

need.

2:12:40

Fine training is actually easy.

2:12:41

Fine training,

2:12:42

we're going to be,

2:12:43

okay,

2:12:44

whatever,

2:12:45

whatever, 100,000,

2:12:46

BDF,

2:12:47

we are,

2:12:48

we're all knowledge

2:12:49

in LLM can

2:12:50

ask

2:12:51

this question

2:12:52

and answer

2:12:53

it.

2:12:54

It sounds easy, but it is very,

2:12:55

very, very, very,

2:12:56

costly, number one,

2:12:57

and number two is

2:12:58

it is already exposing

2:12:59

your sensitive

2:13:00

sensitive data to the internet.

2:13:02

Because you

2:13:03

need to give

2:13:04

for people.

2:13:05

If you have a confidential data

2:13:06

and you

2:13:07

have LLM to train

2:13:08

then you,

2:13:09

that is

2:13:10

very costly,

2:13:11

I should,

2:13:12

the platform open A&AA

2:13:13

and upload

2:13:14

so that is the reason we never do it,

2:13:15

but that is why

2:13:17

Rags are a better solution.

2:13:18

So we

2:13:19

we have that

2:13:20

the

2:13:21

exact

2:13:22

ingest,

2:13:23

repair,

2:13:24

retrieve,

2:13:25

augment and

2:13:26

then finally

2:13:27

the end up

2:13:28

because that's

2:13:30

the introduction.

2:13:33

You

2:13:35

and

2:13:36

and

2:13:37

and

2:13:39

you

2:13:40

and

2:13:41

and

2:13:43

you

2:13:44

and

2:13:45

So

2:13:47

so

2:13:49

you

2:13:50

So

2:13:57

so

2:13:58

where we

2:13:59

we use

2:14:00

in

2:14:02

so

2:14:04

so

2:14:05

in

2:14:06

So where did we

2:14:14

we use

2:14:15

in real world

2:14:16

instead of rag?

2:14:17

No, so real world

2:14:18

may

2:14:18

pintening will be used in cases where I would say

2:14:21

you know, in scenarios

2:14:24

are not true where we want the model to like, we want the model to like,

2:14:29

let's see.

2:14:30

Sometimes it is more like rags are also very, you want.

2:14:34

So, so.

2:14:35

So the behavior itself is very different.

2:14:38

You can think of it that way.

2:14:40

So if it's just external knowledge, then you can use a RAC system to pull the relevant

2:14:44

terms and you can get answers to the questions based on that.

2:14:47

So it will solve most of the problems for you.

2:14:50

But pine tuning can use over.

2:14:52

Pine tuning will be used in cases where you have a particular model and you want to

2:14:58

to inherently change the model itself.

2:15:04

You want to bake that.

2:15:05

knowledge in the model extends.

2:15:06

So that inherently and natively, that model is a different model.

2:15:11

So let's say something like you want to change the tone of the model.

2:15:14

Now tone change

2:15:15

change the behavior change

2:15:17

you want that model to adopt a different

2:15:21

persona, a different personality.

2:15:24

So most of cases, fine-tuning actually works are very handy.

2:15:28

Rag is good enough for a simple knowledge retrieval.

2:15:31

If knowledge-retrieble object in, then

2:15:33

fine-tuning not.

2:15:34

Because I can ask a question.

2:15:35

retrieve the information, augment the prom, get the answer.

2:15:38

Whatever we talked about until today.

2:15:39

We cannot.

2:15:41

I hope we are aligned.

2:15:43

Okay?

2:15:49

So, yeah, so that's, that's contrary.

2:15:51

Fine-tuning and model training are two different things.

2:15:53

Yeah, that's a good question, Ankit.

2:15:55

They are related things.

2:15:57

When fine-tuning-gare-ho, then behind-the-scenes, you are also training a model.

2:16:01

Although that is something we will not be doing here, because, as I told you, we don't need.

2:16:05

to do fine-tuning, okay? Here, uh, later on from up to

2:16:09

you, two demos, we'll give it with open-source models, how to do it.

2:16:12

But obviously we cannot do that as a demo because model fine-tuning takes a

2:16:16

tremendous amount of computation. Even in Collab may, it will crash. Because Collab

2:16:21

doesn't have that much of GPU and memory for you do all these things. Okay. But fine-tuning

2:16:27

and model training are related things. Because you'll fine-tune how you can't,

2:16:30

you? Now, fine-tuned model to train and do, not? They'll, then how can't do?

2:16:33

You have, let me know, a Lama 3.70 billion model, which in GROC in already available.

2:16:38

And it's is the same model that was trained back in December, 2023?

2:16:42

I told you, right? Knowledge cutoff.

2:16:44

You have a model. Now you want to fine-tune that model.

2:16:46

You have to tune that model. You have how do you?

2:16:49

Your tuning, I mean, you, you'll take that the model, you'll take the rock-wola model, you'll

2:16:52

add, and then you'll do that you're training

2:16:55

fit, input-out-combination, train the model. So that's the same idea.

2:17:01

Five-tuning and model training are related things. There are similar thoughts.

2:17:03

not different. Okay, I hope this is clear. And now, from here onwards, we will be getting

2:17:09

into the, and again, as I say, like today we will be stopping at embeddings. And I will show you a small

2:17:15

demo how to create embeddings. So this kind of show how to create embeddings. You have embeddings

2:17:20

want to make, and then finally, this is what comes to the next class. Okay, I won't get too much

2:17:28

into this right now, because this is what will happen in the next session. So today it is just this.

2:17:31

you have a particular text.

2:17:33

You have embedding model used and you can, you can't make vectors

2:17:36

okay?

2:17:38

Next class we'll look at this

2:17:40

how we can see how to find the top

2:17:44

three or top two and finally

2:17:46

using that how we can augment the norm and how we can get the answer.

2:17:50

And now we will see a small example of how that

2:17:52

embedding vector is created.

2:17:54

That vector how they're how to look at it?

2:17:55

That's a short example demo.

2:17:57

But these are the things that are coming.

2:17:59

So this is all the same rag thing

2:18:00

what we discuss, expect, chunk, same idea, just that we will see this in a small demo later on.

2:18:25

Okay. Gunal, can we check the base code? Can we download, can we check the base code? If we download this

2:18:29

100 gb LLM can we check its base board?

2:18:36

Yeah, so at a basic level,

2:18:38

at a very basic level, you can see that. At a very basic level,

2:18:41

you're looking at a very basic level, open source models.

2:18:44

LLMs are open source models. You can go to Huggins and you can absolutely check.

2:18:48

There are many of these so-called models that you have in Huggins face where you can check the source

2:18:53

book. You can take the source model. But it has to be an open source model.

2:18:56

You can check the base board, but of course,

2:18:59

move not can't, 100 gdd LLM, you'll.m, you know, we talked about that yesterday,

2:19:04

you know, but a check-chick-chekers. The port-hugging place available can. You know,

2:19:08

you can't go. And, uh, yeah, Ankit, just to answer your question,

2:19:16

uh, uh, uh, uh, chunking as we're not just to clarify. I, I told you that chunking is actually planned for

2:19:21

tomorrow, you know? I will show you that. This is the plan for tomorrow.

2:19:25

So, because there's so many interconnected topics. They call on rack. This is what I was talking about.

2:19:29

RAC to both, we've divided in many classes we have divided the Rags in room.

2:19:36

Today, we are only in Rack foundations.

2:19:38

This is only today's class.

2:19:40

Then we will come to Vector Search.

2:19:42

That we'll back see.

2:19:44

Embatings what, what are, the Vectors, same story.

2:19:46

That's after, we go to chunking

2:19:47

So we have a separate class for that.

2:19:49

So I don't want to just rush and show you chunging.

2:19:51

You have a complete class only for chunking.

2:19:53

Then then we'll chunking

2:19:54

do it, retrieval, okay? So, so this

2:19:57

all things are. I think there was a question of, can't you at ask, hallucinations and all?

2:20:00

That's a separate class.

2:20:02

Okay, so this is our whole our flow.

2:20:04

That's our class.

2:20:05

So Rags are basically, there are three more classes where we will see the complete Rack demos in these three

2:20:10

classes.

2:20:12

Okay, just to clarify.

2:20:14

Okay.

2:20:15

Hugging face is basically, you know, Jha.

2:20:19

Hugging face is basically a kind of a, kind of open source.

2:20:24

platform you can say open closed platform i think i might have named it a couple of times and

2:20:32

you can see it's open source platform where a lot of companies are there a lot of models are available

2:20:38

because you get to you here if you search by deep seek you will be able to see that different

2:20:44

companies are are present in having days it is like agam i would say it's very much like cago that is

2:20:49

right that is right that is right up over you nailed it right it's exactly like that

2:20:54

later later that's the plan but later to this right okay so let us see our final

2:21:05

demo i'm just going to show you a final demo around the what it is

2:21:24

last lecture content hugging face ecosystem okay

2:21:37

okay a little so a hugging press discussion

2:21:39

but we have to check that

2:21:42

now then hey we will be talking about it no one and even if it's not there maybe later on

2:21:46

not today's session but we have enough number of classes we can as i told you we can add one or two

2:21:50

classes later we can have a separate discussion about absolutely we can have a separate discussion on

2:21:53

absolutely we'll see we'll see okay guys uh just give me a minute

2:22:06

other

2:22:12

all clear concept clear again the hands on

2:22:15

there's just a line code is actually it's very simple okay i think you will get a real

2:22:20

flow of rag once i show you the complete uh end to end to end quote so that's going to happen

2:22:25

over the next two sessions but just want to make sure the concept of rag is absolutely clear

2:22:29

so i hope everybody's alike with the basic concept so you know so any questions people have

2:22:36

in the concept i know idea clear enough what rag is and again i think the most

2:22:41

important slide was this the most important slide of the name was this in js prepare

2:22:46

re-augment generate this should be absolutely clear okay okay okay just give me one minute guys

2:22:55

i'm okay so because my code in code in full rag here so i want to just uh you know

2:23:01

trim those sections and i want to only show the part that is relevant

2:23:06

only the relevant part I want to show you.

2:23:36

Thank you.

2:24:06

Thank you.

2:24:36

Thank you.

2:25:06

Thank you.

2:25:36

Thank you.

2:26:06

So guys, what I've done is I've got a very simple piece of code for you.

2:26:10

I don't want to make it too complex here but this is a very basic code where I will share with you how to generate embeddings and I will call it

2:26:19

embeddings and I will call it Embedings.

2:26:21

This is the last part of today and basically what we have done is we are using a specific

2:26:28

in case particular package called Sentence Transformers Ticket.

2:26:33

So this is how we will be creating embeddings.

2:26:36

We can take any text, any chunk, any prompt, which we can take, any text kind of data we can take.

2:26:43

We can pass it.

2:26:45

And that model is the model that is what basically embedding's the concept stands for.

2:26:51

So first we install the package embeddings and next we go and we use sentence transformer.

2:26:58

What are we doing right now?

2:27:01

We are using a model called All Mini LNH6 is a very very popular model.

2:27:05

It's a very popular model.

2:27:06

for these kinds of word and beddings and all that.

2:27:11

It's a very popular model.

2:27:13

So we are loading that particular model.

2:27:16

And in case you are wondering that, sir,

2:27:20

how is it?

2:27:21

Where is it?

2:27:22

The model is how are from?

2:27:24

That's the hugging face there.

2:27:26

Okay.

2:27:27

You're hugging face.

2:27:28

You go and you can actually see

2:27:31

sentence transformer all mini LMN6B2.

2:27:34

This is the same one that I'm using right now.

2:27:35

that I'm using right now.

2:27:36

You can click and you'll be able to see more details about that model.

2:27:41

You can see it map sentences to a 384 dimensional vector space.

2:27:45

What, here what?

2:27:46

Here what is behind the scenes is?

2:27:47

It takes every text.

2:27:49

It takes every sentence.

2:27:50

It takes every chunk.

2:27:51

And from that it generates 384 numbers.

2:27:54

That's how powerful it is.

2:27:55

Very, very interesting.

2:27:57

It's not the only one.

2:27:58

There are many other such embedding models that you have.

2:28:01

And this is very easy to do it.

2:28:03

And it also gives you a small help in terms of how it.

2:28:04

help in terms of how to use it.

2:28:06

You go use the model.

2:28:07

How can use it?

2:28:08

This is exactly how I'm related.

2:28:10

Okay?

2:28:11

You can.

2:28:12

You can this sample code link.

2:28:13

So, yeah, this is simple.

2:28:15

It's there.

2:28:16

So, from sentence transformer, import sentence.

2:28:19

We have sentence transformer to import

2:28:21

we have the model to load

2:28:22

here here,

2:28:23

model, so load it,

2:28:24

download.

2:28:25

And then I give some sample sentences.

2:28:28

This is a happy person, happy dog,

2:28:30

happy person,

2:28:31

and then I say, model.

2:28:33

Endport sentences.

2:28:34

I'm writing a command saying model.

2:28:35

You're the model.

2:28:36

Please import these sentences and I will get the embeddings.

2:28:40

That's it.

2:28:41

Simple.

2:28:42

Straight forward.

2:28:43

And you can do this for all other models as well.

2:28:44

This is not the only model.

2:28:45

There are many other models which are these kinds of transformer models.

2:28:49

Okay.

2:28:50

So just to show the code to all of you.

2:28:52

So we are again, same thing.

2:28:53

We have some sentences here.

2:28:55

We are saying model.

2:28:56

And here I can demonstrate the embeddings and all this morning.

2:28:59

You can go load and you can take a look at it.

2:29:03

So that quick.

2:29:04

If brown fox jumps over the lazy dog, and we are only showing the first five values of the vector, because there are 384 numbers in the vector.

2:29:13

So all that we can only show you the top five values.

2:29:17

Okay?

2:29:18

And you can also say the embedding shape is 384.

2:29:20

Which I had already told you, it is taking this entire text,

2:29:23

and it is trying to represent that text as 384 numbers.

2:29:26

Now those numbers mean nothing to the human being.

2:29:29

Now, I'm going to ask what number is,

2:29:31

what number is.

2:29:32

I don't know.

2:29:33

I don't know what that number is.

2:29:34

But all the numbers taken together, all those 3 84 numbers together are conveying something about the text.

2:29:41

Okay?

2:29:42

The same thing for the second one, the same thing for the third one.

2:29:44

So this is what is giving you a contextual information about your text.

2:29:48

So here, I only 3 simple sentences,

2:29:51

but in practice what will happen is you will take the entire PDF.

2:29:55

You will divide those PDFs into chunks.

2:29:57

And now you can imagine that these are like your chunks.

2:30:00

Yeah, C1, C2, C3 will.

2:30:02

Chunky, we'll next class.

2:30:03

they can get and then you'll be able to convert these chunks into the corresponding embeddings.

2:30:07

So this is one of the ways how you can work.

2:30:09

And this code I have uploaded in your in your driver's menu.

2:30:13

So this is the very, very popular way how you can generate embeddings.

2:30:17

So this is already uploaded in your right.

2:30:19

So people can just take maybe it will hardly take you two minutes.

2:30:22

You can go to the 23rd May folder, just go there and execute it.

2:30:26

Just execute it.

2:30:27

This is very simple.

2:30:28

Possibly the simplest demo in all the two months we have been doing classes.

2:30:32

we have been doing classes.

2:30:33

This is the easiest demo today.

2:30:35

Easiest demo.

2:30:36

Right?

2:30:37

Just have the text and generate the embodies.

2:30:39

Yeah.

2:30:40

Range of those numbers will be usually from 0 to 1.

2:30:43

Yeah, correct.

2:30:44

Minus to 1 plus 1.

2:30:46

Usually.

2:30:47

It will normalize.

2:30:48

Correct.

2:30:49

Usually it is in that range.

2:30:51

Actually, it depends on the model how this train, but usually it is in that range.

2:30:57

Yeah.

2:31:00

You can you can actually go and go and see multiple models.

2:31:07

Like there is something called bird, there's something called Roberta.

2:31:10

There are many other models that you also have.

2:31:13

Anyway, so all of you please run this and after you are able to successfully execute this code,

2:31:18

Embedings on IP by NP by NP, please write me a quick yes on chat.

2:31:25

Yeah, yeah, yeah, yeah.

2:31:27

Ankit, that's a, that is not a foolish question.

2:31:29

You have a very good question.

2:31:30

You want to post that question on for everyone.

2:31:33

So everyone can see what a good question you asked.

2:31:36

It's a good question.

2:31:38

And the answer to the question is yes, you are correct.

2:31:40

The UI embedding Algo must match the NLM embedding angle.

2:31:45

Yes, yes.

2:31:47

I think what you mean to say is this thing.

2:31:50

What you mean to say is this thing.

2:31:52

So whatever models are used to create this embeddings, chunk embeddings,

2:31:56

the same models must be used to create the query embedding.

2:31:59

query embedding.

2:32:00

Right?

2:32:01

Right.

2:32:02

UI, the chunk embedding.

2:32:03

I think you're referring to the chunk embedding.

2:32:05

So user asks the question, use UI.

2:32:08

User asked the question.

2:32:09

Here here the query embedding code is the right term is called query embedding.

2:32:13

Whatever embedding model I'm using to take the question and convert that to numbers, the chunks

2:32:18

must go to the exact same embedding model.

2:32:20

So this embedding model that is present here and this embedding model have to be exactly the same.

2:32:26

Correct.

2:32:27

You are right there.

2:32:29

Okay, guys, let me know, please, if you are able to run this code, please,

2:32:38

this is the 23rd May folder.

2:32:40

All good.

2:32:59

Okay, execute all right. Okay, very good. Very good.

2:33:08

Hardy is done. Others are all done. Please confirm to me.

2:33:12

And there are multiple places how the embeddings can be done.

2:33:18

So hugging places are very, very popular resource.

2:33:21

This is what we will do in practice most of the time.

2:33:23

Just wanted to let you know.

2:33:24

But just be aware that the embedding models are,

2:33:27

they can.

2:33:28

They can also many other places.

2:33:29

Like, OLAMA may be available,

2:33:31

open AI may be available.

2:33:33

So embedding models are available in multiple places.

2:33:35

So don't be confused if you see some code

2:33:37

that here, here from Ovalama, here from there,

2:33:39

here from there.

2:33:40

So I personally think HuggingFace is the simplest code.

2:33:42

It's just simple code are anywhere.

2:33:44

You're just importing a library, loading the model,

2:33:47

and that's it.

2:33:48

Simple way to do it.

2:33:49

Okay?

2:33:50

So just wanted to let you know.

2:33:51

Hugging face is a very practical way we do these things also.

2:33:54

So stick to Hugging face.

2:33:56

Very simple.

2:33:57

to use the code and this is how we'll implement drags also going following.

2:34:01

Okay, others are all done.

2:34:04

The code is executing.

2:34:06

And just for a small exercise,

2:34:08

you can you can here a PDF

2:34:11

instead of taking three sentences,

2:34:13

you can actually take a complete PDF.

2:34:16

You can actually take a big document.

2:34:18

That you can a different demo can.

2:34:20

Okay, okay.

2:34:22

So next session, we will be meeting

2:34:25

and we will be talking more about

2:34:26

more about the concept of chunking.

2:34:31

Chunking is the plan for the next session.

2:34:34

As I told you, we'll get into the details of chunking.

2:34:38

And after that, we will see vector search embeddings,

2:34:42

and then finally the complete track pipeline with me looking at.

2:34:46

And this is where we'll answer some of these questions like top care retrieval.

2:34:49

One of you are asking,

2:34:50

is our top care, what is how to be?

2:34:53

So this is where we will see how you can take different

2:34:56

different values of K and how we can adjust.

2:34:58

But most importantly, the key objective of today's sessions

2:35:03

were to talk about what Rags basically are.

2:35:07

So understand the concept of Rags.

2:35:09

This is the most important part, I would say.

2:35:11

The most important part of Rack, Kertek Uhead.

2:35:14

So we went through with context, without context.

2:35:16

We talked about the privacy issue.

2:35:18

We talked about the cost aspects.

2:35:20

We talked about why enterprises do Rags from a

2:35:24

from an efficient,

2:35:26

perspective we can do from a cost perspective

2:35:29

from a privacy perspective.

2:35:31

And then we looked at analogies.

2:35:33

We looked at the five-step workflow.

2:35:35

All of you recall that five-step work flow.

2:35:36

All of you recall that five-step work,

2:35:37

we ingest, prepare, re-argment, generate.

2:35:40

We talked about the concept of grounding.

2:35:43

Grounding.

2:35:44

So grounding is what kind of what in brain language?

2:35:46

So the answer to the questions must be grounded in the facts.

2:35:49

And then also we looked at some examples of

2:35:52

with context, without context we talked about.

2:35:54

And finally, we also look at

2:35:55

we also looked at a small example of how to convert text

2:36:00

into embedding's, you know.

2:36:02

And this is where we are using Olama,

2:36:04

but I would highly recommend you not to.

2:36:06

If you're not to,

2:36:07

you know,

2:36:08

so Olamma is easy, there's nothing

2:36:09

this is not.

2:36:10

This materials you can

2:36:11

care care about.

2:36:12

But Olama, personally, you know,

2:36:14

I think it looks a little complicated.

2:36:16

You don't have to.

2:36:17

Like, if there's an easy way to do it,

2:36:18

you can go and use a big place.

2:36:20

But they're all doing the same thing.

2:36:22

Here here, you look,

2:36:23

you look at a quote embed,

2:36:24

Olaman also.

2:36:25

has embedding models available.

2:36:27

Embed model's name.

2:36:28

Normic embed text, whatever.

2:36:29

You can just pulling a sample,

2:36:31

embedding model from Olam.

2:36:33

Same way.

2:36:34

Then you're giving three sample sentences.

2:36:36

And then then you're saying embed.

2:36:38

That's it.

2:36:39

So same way, we are just calling in a different way.

2:36:41

That's it.

2:36:42

But hugging face is more popular.

2:36:43

So you can stick to hugging face what I taught you.

2:36:46

So this is the embedding generation part.

2:36:49

And finally, we will be like,

2:36:51

we will see this in the next class.

2:36:53

Obviously in the upcoming sessions,

2:36:54

how retrieval.

2:36:55

and all these things happen.

2:36:57

Okay.

2:36:58

Okay, guys.

2:36:59

Thank you.

2:37:00

Thank you so much.

2:37:01

Is it free?

2:37:02

And API will be exhausted control?

2:37:03

What do you mean?

2:37:04

What is free?

2:37:05

What is free?

2:37:06

This is free?

2:37:07

There's no API we use for this, by the way.

2:37:10

This is the Python package.

2:37:12

API we used in grog in grog in.

2:37:15

So grog in the rate limits.

2:37:16

That we'll back in next class

2:37:18

back from.

2:37:19

Usage limits on it.

2:37:21

But this,

2:37:22

there is a little usage limits.

2:37:23

This is the Python package.

2:37:24

You are.

2:37:25

If you have this port installed

2:37:27

you, this port in your system

2:37:29

run here,

2:37:30

this package is installed in

2:37:32

you're installing this package.

2:37:34

Are you with me?

2:37:35

Yeah.

2:37:36

Okay, okay, guys, thank you so much.

2:37:39

Amazing.

2:37:40

I think the great to again get started with rags and agents

2:37:44

all over again.

2:37:45

So I will pass it over to Arshita.

2:37:47

We have the quiz.

2:37:48

So Arshita over to you.

2:37:49

And thank you once again.

2:37:50

Yes, have a great evening.

2:37:51

We meet again

2:37:53

once again.

2:37:54

uh

2:37:56

umcith is asking

2:37:58

more guys

2:37:59

okay okay

2:38:00

I'm reply to

2:38:01

I'm reply to you on chat

2:38:02

okay

2:38:03

yeah

2:38:04

okay

2:38:05

who is

2:38:08

uh

2:38:10

well

2:38:11

yeah

2:38:12

thank you very much

2:38:14

so we will not have

2:38:15

the 90 meter quest for today

2:38:17

but I am launching

2:38:18

the feedback poll

2:38:20

so please do

2:38:21

fill that in before leaving the session

2:38:23

RACDB are considered on premise.

2:38:27

So let me in the meantime answer

2:38:29

Ankit's question.

2:38:31

Yeah, that's a

2:38:33

good question,

2:38:35

Ankit, very good question.

2:38:37

So first, Ankit, we are preserving,

2:38:39

we are not passing all the chance, okay?

2:38:41

Couple of things enterprises do in real world.

2:38:43

We do masking.

2:38:45

So we don't put a data

2:38:46

we basically do something about a pasting.

2:38:49

Okay.

2:38:50

So we go back and do

2:38:52

So we go back and do something called the masking.

2:38:54

So we mask the information.

2:38:56

That's one way we are able to implement it.

2:38:59

Okay?

2:39:00

So masking

2:39:02

we are able to implement it.

2:39:04

Second,

2:39:05

we are able to ensure that

2:39:08

we are able to ensure that

2:39:11

you're not passing the entire data.

2:39:14

If you have a huge document

2:39:16

which is spanning thousands of chunks,

2:39:19

thousands of pages,

2:39:20

our entire data can't.

2:39:22

So any way,

2:39:22

up a small portion of data measurement, right?

2:39:24

So that is one more way to look at it.

2:39:27

So that way you're preventing it, right?

2:39:29

So the entire organization data is not getting sent anyways.

2:39:37

Does it make sense?

2:39:52

Okay. Thank you. Thank you. Okay.

2:39:55

These vector db use cubes too.

2:40:05

Ah, that's internals.

2:40:07

We are actually talking about the internals.

2:40:10

So Proma dv is there.

2:40:12

The different types of vector dbys that are there.

2:40:25

But in that case, LLMs must be able to,

2:40:42

absolutely. That is true. That is true.

2:40:44

LLMs will be able to unmask also.

2:40:48

Correct.

2:40:48

That is true.

2:40:51

Yeah.

2:40:55

Okay. Any other questions, guys?

2:41:25

Thank you.