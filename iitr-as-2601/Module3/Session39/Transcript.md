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

Thank you.

13:00

Thank you.

13:30

Thank you

14:00

Thank you

14:30

Thank you

14:32

Thank you

14:34

Thank you

14:36

Thank you

14:38

Thank you

14:40

Thank you

14:42

Thank you

14:44

Thank you

14:46

Thank you

14:48

Thank you

14:50

Thank you

14:57

Thank you.

14:59

Thank you.

15:29

Thank you.

15:59

Thank you.

16:29

Thank you.

16:59

Thank you.

17:29

Thank you.

17:59

Thank you.

18:29

Thank you

18:59

Thank you

19:29

Thank you

19:31

Thank you

19:33

Thank you

19:35

Thank you

19:37

Thank you

19:39

Thank you

19:41

Thank you

19:43

Thank you

19:45

Thank you

19:47

Thank you

19:49

Thank you

19:56

Good evening everybody. Welcome to the session. We will be starting on here.

20:26

Good evening folks.

20:43

So today is a continuing session on rags. So rags are a series of four sessions that we have.

20:50

Last session, we looked at a very high level introduction to what rags are.

20:56

So Raguala pipeline, all of you recall from the last session.

21:00

And if you want to just go back to that once again, so this was basically the main part

21:05

of the pipeline that we covered in the last session, right?

21:08

So the main idea of Rags, we are effectively first ingesting our data, then we are

21:15

chunking and embedding the data, and then we are retrieving and searching the vectors, finding

21:20

the relevant chunks, and then we are pasting to the prompt and doing the LLN.

21:24

So today's session is focused primarily.

21:26

on these two, primarily on these two. How to do the embeddings? We saw a small demonstration

21:33

of that last session, if you remember. We used something called sentence transformer.

21:36

You'll know, last we, we've made a little demo decked. So that is, that is the one key idea we

21:42

will cover again today in detail. That hey, how do we actually take those, those pieces of text?

21:48

Now here on a PDF, so how do we generate the embeddings? We will see that. And the second aspect is,

21:56

we go and store it in a vector database. So what is this vector stored? So it's still related.

22:00

We will discuss a very specific kind of vector store called chroma. Chroma DB is what we will

22:05

discuss today. And we will discuss some specific functions with respect to chroma DB. So again,

22:10

the focus of the session is only on these two components today. And then the remainder we will take

22:14

up in the upcoming session, obviously. So we are doing drag in phases right now. Okay.

22:21

So again, what is the main agenda today? We will understand the concept of

22:26

of embeddings. We were able to do embeddings yesterday. We will once again see that today,

22:30

what embeddings are. What embeddings are? We will see that. How to store vectors in

22:34

chroma? It's how to store in chroma? It's how to store in. And what is the name of this

22:38

this vector database? It's called a vector db. Like SQL module when you guys studied, you

22:45

used a relational database. You use a relational database. You use a relational database, where you

22:49

you're stable store. There's rows, there on columns. So similarly, there is something called a

22:54

vector dv. And chroma is a kind of. And chroma is a kind of.

22:56

of a vector d. So we'll see. And finally, we will discuss this particular thing called

23:00

semantic search. So here we'll discuss what it actually means. Here

23:04

here a retrieval one thing will. Okay. So that's the focus area for today's session, mainly.

23:11

So first things first, without any further at all, let's, let's basically talk a little bit about

23:18

the embeddings part once again. So what are embeddings? When we talk about embeddings, what are they

23:23

exactly? What do embeddings even mean?

23:26

So embeddings are basically, it is basically a way, how machines are effectively representing data in a numeric format.

23:38

Okay, we are actually representing data in a numeric format. Because remember, right from the machine learning module, I told you that machines don't understand anything, which is not a number.

23:47

Machines only understand numeric data. If your text data, if you have

23:52

you have some other kind of data. Machines will not understand that. Machines will inherently only

23:56

understand numeric data. So if you have some other forms of data, the onus is on you to take that

24:01

data and convert that into a numeric form. That is what you will have to go back and do. You will have to

24:06

take that other forms of data. And the onus is on you to take the different, different forms of data

24:11

and to convert the different different forms of data into a structured numerical form. So that is

24:17

what this, the whole idea of embeddings basically.

24:22

are. Again, if you remember in my initial session, we were discussing transformers and all that,

24:28

we were covering in the very first class of LLMs, very first session of this module,

24:32

where we actually talked about that concept, word embeddings, and what is imported decoder, what is

24:37

transformer. So the key idea is whenever you look at any kind of text, you have to be up chat GPD,

24:43

even when you write a prompt, after chat GPD, you write a prompt, what is the weather, what is the, what will I

24:49

do tomorrow, whatever, you ask a question in chat GPD.

24:52

You have that text, you have that sentence, you type that sentence is.

24:56

But the moment, the machine processes that, what is happening?

25:00

You remember that beautiful article we discussed?

25:03

So we actually talked about this, and I wanted to show this to all of you because it was so nice,

25:08

it was such a nice, you know, demonstration that we did.

25:11

And I wanted to just kind of make sure everybody remembers that, okay?

25:14

So this is the Financial Times article that we covered.

25:18

So we went through the whole session covering this thing, okay?

25:21

And you know, what I talked about here?

25:24

We talked about word embeddings.

25:25

We talked about how machines understand words as a vector of numbers.

25:29

So the, the, the, first, the core idea is, that you have you, you have this sentence is.

25:34

Machine's to have the machine's past, the machine has the tokens.

25:37

The first thing, machines do you, they're all the sentence to go to tokens by divide.

25:41

Tokens, what kind of individual words are.

25:43

And then what they're, other words' vectors are.

25:46

We talked about word to vector.

25:48

So machines are able to convert these words into some kind of.

25:51

of a vector format.

25:52

Okay, so some kind of a vector format.

25:54

So there we talked about this kind of a concept.

25:56

Word vectors for that.

25:57

Just like work, it's a vector of numbers.

25:59

So just like, you know, machines are processing a particular word as a vector of numbers,

26:04

it can also similarly process a particular sentence as a vector of numbers.

26:09

And that is the basic concept of what embeddings, you know, basically related to.

26:13

That is the main idea of what embeddings, you know, really are.

26:17

I hope everyone's aligned with that, the concept.

26:21

This is again, I'm again stressing on this because it's such a nice demonstration.

26:25

You can say in case anybody forgot or anybody did not, you know, was not part of the session.

26:30

So just be aware, you know, whatever you're doing, these are all embeddings.

26:35

They're all converted behind the scenes into vectors of numbers.

26:38

So this is.

26:39

The next time you have a question, the embeddings, go back to my financial times article and just go over it.

26:45

Allak, other models.

26:47

What was the thing that we talked about in the?

26:51

in the last session, what are the different things that we talked about?

26:54

So embeddings are again a key concept.

26:56

And another very important thing I wanted to cover here is the concept of semantic.

27:02

Semantic. Semantic to mean, what do these embeddings really represent conceptually?

27:09

Okay.

27:10

These embeddings basically represent a kind of a kind of semantic meaning of the sentence.

27:21

You have a sentence?

27:22

You have a prompt.

27:24

You have a prompt.

27:25

You are looking at embeddings with respect to that sentence.

27:29

These embeddings basically represent the semantics of the sentence.

27:32

What is the semantic meaning of the sentence?

27:34

That is what the embeddings actually represent.

27:36

That is what the embedding actually represent.

27:38

That is the conceptual thing you should be clear.

27:40

The embeddings are what these numbers are?

27:42

These numbers are telling you something which is representative of that whole sentence.

27:46

Okay, that's the same way that we discussed about this word word.

27:49

These numbers are somehow telling you.

27:50

Numbers are somehow telling you the semantic meaning of the word.

27:53

Semantic.

27:54

The term that I'm using is called semantic.

27:56

Semantic. Semantic means.

27:58

What is the meaning?

27:58

What is the context of that word?

28:00

So similarly, what is the context of that sentence?

28:03

That's the way to understand the meaning of semantic.

28:07

So another thing I wanted to clarify is embeddings can come in different, different forms.

28:13

So the one that we used last session and the one that I'm using here,

28:16

so there are different different things that we have.

28:18

So if you remember, we use something called sentence.

28:20

and there are many, many embedding models out there.

28:23

If you want me to take you through one such website,

28:27

a website called MTEB, MTEB stands for a massive text embedding leaderboard.

28:34

Okay, this is it a beautiful website.

28:36

Let me ping this to all of you.

28:38

And here you will have a list of all the top embedding models out there.

28:43

For the session perspective, we are focusing on a few basic models,

28:46

but this is the entire repository of all the

28:50

open source embedding models out there.

28:54

And see, unlike large language models, LLMs, LLMs,

28:56

LLMs can't be paid but these models are usually free.

29:00

These are open source, these are open, completely free to use and all that.

29:04

That is one thing that you will have to keep in mind.

29:07

So these embedding models are usually free of cost and something that you can work with.

29:11

Okay, so you're able to see the NTP leader vote right now.

29:14

It takes a while to refresh. Let me just,

29:16

just start it.

29:19

And here, the reason I'm trying to demonstrate this to all of you is because if you see,

29:24

here we've made a small demo and if you see, let me just go back and this is the same demo that

29:29

we saw last session.

29:30

So I'm just trying to show you the embedding part.

29:32

So how text becomes a vector.

29:34

What are the phases?

29:35

First, you have raw text.

29:37

Then, then you know, what you're talkingize it.

29:39

Divide the text into unique tokens.

29:41

Then after it, embedding, then then, it's then then it's stored part is different.

29:45

We will discuss later.

29:46

But this is what we already did in the last session.

29:49

If you remember, we used a model.

29:51

We used a model called all LM, all mini L6V2.

29:56

This we have an example model in last session.

29:59

You can take any clue.

30:00

Okay, if you want to go back and see what is this model?

30:04

If you want to go back and see what is this model,

30:07

this model is, you know, actually this one.

30:10

This is the model.

30:12

Now, when I type this in Google,

30:14

your automatic is all mini LN.

30:17

So what is this?

30:18

It is a sentence translation.

30:19

former model, it maps sentences and paragraphs.

30:22

I mean, any text for, it maps it to a 3804 dimensional vector space.

30:28

That's it.

30:28

Now, these 384 numbers means nothing to us.

30:32

We have this kind of meaning but this is what I meant by the semantic context.

30:37

You're able to look at these 384 numbers as a whole,

30:41

and you're able to somehow understand what these sentences are.

30:44

You're able to get the contextual meaning.

30:46

The machine is able to understand.

30:48

From this three.

30:49

84 numbers, what is the contextual meaning of the sentence?

30:52

That sentence can't.

30:54

If I say, my name is Sion, it's a, it's a, it's a,

30:55

it's a sentence is a meaning. Now, you and I, we understand English.

30:59

Machine doesn't know English.

31:01

So machine can't know English, but if I say, my name is Shain,

31:06

we'll, we'll give it, machine, we'll, machine, it's in embeddings in convert

31:08

and it through machine to say, you know, whatever is, it's like machine's language.

31:13

Think of it that way.

31:15

Very easy to use it, that is, that is all I'm trying to show you.

31:18

Important thing is, important thing is,

31:18

this is 384 dimensional vector.

31:21

It's not that all will be 384 vector.

31:23

There can be some other embedding model.

31:25

In fact, you can click on sentence transformer.

31:28

This is your main library is.

31:30

And you can see, there are so many different different

31:32

sentence transformer models you will find.

31:35

There are many.

31:35

There are many such sentence transformer.

31:37

There are like 127 models.

31:39

Can you see?

31:39

There's so many.

31:41

So sentence transformers is the main package.

31:43

This we've done,

31:43

pip install sentence transformer.

31:45

All of you, this is the only video.

31:47

Import sentence transformer.

31:48

And there are so many.

31:50

These are all open source.

31:52

You can see, these are all state-of-the-art embedding models that you are able to select from here.

31:57

And you can see, there are so many.

31:59

You can choose any one of the models that you want.

32:01

And the one that we used was this one, all mini-LM.

32:03

We've used to L6V2.

32:05

Let me just cross-check.

32:07

I think we used L6V2.

32:09

Now, look, here here here L-12V-2.

32:11

Now, you're going to say, turns out this is very popular.

32:14

This is actually 33.3.4, this one.

32:18

You can actually take a look at this.

32:20

Now, LQLV2, what is?

32:21

L2LV2B2B2.

32:24

So there are different, different variants of these models.

32:26

You can.

32:26

You can look at this one.

32:31

All MP net base B1.

32:33

Now, this is actually a 768 dimensional vector.

32:37

It is not always 384.

32:38

Some models are even bigger.

32:40

Let's just keep this at the back of your mind.

32:42

You can view all 127 models.

32:45

You can see here.

32:46

And you can also sought by popularity and most.

32:48

likes, most downloads. And you can, it will give an idea to you.

32:51

The subse popular or subse liked models on saying.

32:54

And in fact, if I saw it by most likes, you can see the one that we used is actually one of

32:58

the best ones, one of the top ones.

33:00

All mini LN, LN, LCs, V2, is one of the top embedding models that is there on Hacking Face.

33:05

And there is no platform that is bigger than Hanging Face.

33:07

The A year I'm used here, or they said it is very, very popular.

33:10

These are some other models you can also explore.

33:13

So there are many such models that you have to.

33:16

And this is a slightly bigger leader about.

33:18

That's why it's taking a little time to refresh.

33:20

I'll just give it one more try.

33:23

You can this.

33:24

You can this way.

33:24

This demo we'll not show you.

33:26

But in the next session, I will actually show you a demo with this one.

33:31

So we're not in sessions may use for today.

33:33

But you just wanted to make you aware.

33:36

It takes a while to open, actually.

33:38

Let's see, once it opens up, I'll show you.

33:42

So, anyway, so this code execution is what we already saw last session.

33:46

You can see.

33:47

Sentence Transformer.

33:48

LMVC, I'm the model to loaded

33:50

the first.

33:51

What are we doing?

33:52

We have two sentences here.

33:54

Refunds are processed within five to seven business days.

33:56

And when did I get my refund?

33:58

Money back after returning the item.

34:00

I'm there two sentences here.

34:02

This is sentence A.

34:03

This is what we are calling it.

34:06

Python may, it's nothing but a simple string.

34:08

Anything that you put within double code,

34:10

that Python may string button.

34:11

So sentence A is a string and sentence B

34:14

is also a string.

34:15

That's it. We've got two sentences right now.

34:18

So all of us.

34:18

you're able to see. So. So this is like

34:22

the next thing what we will do,

34:24

this is our model. Just, just for our hugging face

34:27

from load here, download here. You

34:28

look, we literally download it. So,

34:32

how big model is? Actually, it's a

34:33

a quite small model. 90 mb model. Okay. So whenever you see

34:37

this model dot save tensors, this means that you're actually

34:39

downloading it. You have your system

34:41

in download for you. This is a fairly small model. You're

34:46

downloading that and then you're doing model.

34:48

dot input sentence A and model.

34:50

And model dot input sentence P.

34:51

And we're just on NUMPI in convert

34:52

Now, you?

34:53

Now, you're asking,

34:54

now, why convert

34:55

because remember,

34:56

machines process

34:57

numeric values very efficiently

35:00

in numerical Python,

35:01

numpy. So that's

35:02

in NUMPI arrays

35:02

make a good, because

35:04

this vector is nothing but a set of numbers,

35:06

right?

35:07

You have this vector

35:08

so I've done this code

35:09

run already.

35:10

So because I ran the code,

35:11

if I over over vector A,

35:13

you can see once again,

35:15

so I'm loading the model.

35:17

No, no,

35:17

no, KOLAB in models

35:18

not. Collab is just an

35:19

environment to run.

35:20

If you hover over it,

35:22

you're over it, you

35:22

you can see that

35:23

Vector A is a NUMPI array.

35:26

Vector B is a NUMPI array.

35:27

So we're we're

35:27

we're going to

35:27

convert

35:28

and finally

35:29

you can see

35:31

what is the length of Vector A?

35:33

What is the length of vector A?

35:34

This is the length of vector A.

35:36

384.

35:37

So this is a array

35:38

this is a NUMPI array

35:39

you're here

35:40

here we're here we're

35:40

here we're here we're

35:40

here we're here.

35:41

But you look,

35:42

now look it.

35:43

Vector A what is.

35:44

This is your vector A.

35:45

These numbers

35:45

mean nothing to the human

35:47

expert.

35:47

Now, human being

35:48

for these numbers

35:49

no means.

35:50

Now you'll

35:51

ask you, sir,

35:51

what is this

35:52

E minus 2?

35:53

E minus 2?

35:55

How do

35:55

it's how

35:55

how do we

35:55

interpret

35:56

in Python?

35:57

What do we

35:57

say?

35:58

Whenever you see

35:58

E minus 02,

36:00

it's the

36:00

meant

36:00

10 to D

36:01

2.

36:02

2.

36:02

E's means

36:03

just keep this

36:04

at the back of

36:04

your mind,

36:05

exponential.

36:06

So whenever

36:06

you see E,

36:07

next time you see

36:08

E in Python,

36:09

E's

36:09

means exponential,

36:10

I mean to the power.

36:11

So E minus 3

36:13

means 10 power minus 3.

36:14

So that means

36:15

this value

36:15

is minus 3.

36:16

It is minus

36:17

3.59 into 10 to the power minus 3.

36:20

8.44 into 10 power minus 2.

36:24

Okay?

36:24

1.16 into 10 power minus 2.

36:27

This is all these numbers are there.

36:32

But these numbers make no sense to the human expert.

36:35

Human being for

36:35

means, but all these numbers taken together.

36:39

How many such numbers?

36:40

All these 384 numbers collectively taken together.

36:44

It conveys the semantic meaning of the text.

36:46

It somehow

36:47

conveys that, that the vector A

36:48

is, vector A

36:49

we have,

36:50

we have,

36:50

you know,

36:50

the sentence A

36:51

it's somehow

36:52

conveys the meaning

36:53

of this particular

36:54

sentence.

36:55

So that's the beauty

36:56

of what,

36:56

you know,

36:58

what these

36:59

sentence are

36:59

betting is basically

37:00

relates to.

37:01

Okay, so again,

37:02

we are going back to

37:03

something that we talked

37:04

about in the very first

37:04

session.

37:05

I just wanted to connect

37:06

the dots with everybody

37:07

to that you know what it is.

37:08

So finally,

37:09

finally I think this load

37:09

was,

37:10

finally it was

37:11

there was.

37:13

No,

37:13

not just not just

37:13

not yet.

37:15

Actually,

37:15

there are many

37:16

there's why.

37:17

slightly different one.

37:19

This we have

37:19

this is something

37:21

just for your additional

37:22

reference to get.

37:23

Yeah, you can see it

37:24

consists of

37:25

100 plus

37:25

models.

37:26

Ah,

37:26

we load one.

37:27

Now,

37:27

this is the more

37:28

exhaustive.

37:28

This is much more

37:29

exhaustive.

37:30

And this is the

37:31

actual embedding

37:32

leaderboard.

37:33

Here there are

37:33

more big models.

37:34

Sentence Transformers is

37:35

usually limited to

37:36

300 vectors, 400

37:37

vectors,

37:39

1000 vectors.

37:40

But here

37:40

you have

37:40

you have

37:40

models

37:41

that you

37:42

embedding dimensions

37:43

look is

37:44

massive.

37:45

If I sort it,

37:46

if I sort it,

37:47

you'll basically have a model

37:48

called Grit LM

37:49

and what it does is

37:51

this is incredible.

37:52

It's actually taking

37:53

every,

37:55

you know,

37:56

every sentence and it's basically

37:57

converting that to a vector

37:58

of 32,000 768 numbers.

38:01

Can you believe it?

38:03

So the more

38:03

the number of dimensions

38:05

that reach up the context.

38:07

So,

38:07

yeah,

38:07

here here here's sort and ascending

38:09

can you,

38:10

you know,

38:10

you'll see everything

38:10

whatever we talked about,

38:12

right?

38:12

You have your very base,

38:14

you have very basic

38:15

models like

38:17

you know,

38:18

pub med,

38:18

but,

38:19

base embeddings.

38:21

So what it does is

38:21

it takes a particular

38:22

sentence and it

38:23

converts that to

38:23

64 numbers,

38:24

whatever we talk.

38:25

We have,

38:26

we have, our case,

38:27

in our case,

38:27

384

38:27

vector size

38:29

but here

38:29

here's all

38:30

models available.

38:32

And you've got

38:33

even some

38:34

massive models like

38:35

this one.

38:36

This is a huge

38:37

repository.

38:38

This is a

38:39

very big.

38:39

Obviously,

38:39

this is like,

38:41

this is massive.

38:42

You can see here

38:43

here here here here.

38:45

Huge list.

38:45

and it will give an idea to you in terms of what is it.

38:49

Just one second, clear sort.

38:51

I'm here

38:51

sort here

38:51

sort

38:52

and let me just do this one.

38:55

And you can actually get an idea

38:56

in terms of

38:57

what some of the biggest

38:58

models are.

38:59

This is your grid LM

38:59

or your open search

39:01

or your

39:01

your GTE

39:02

or your GTE

39:02

in fact,

39:03

we'll use

39:03

in class in.

39:05

So these are some of the

39:05

biggest

39:05

models out there.

39:06

And if you want to use them,

39:07

it's very simple,

39:08

very simple to use them.

39:09

You have it's

39:09

click

39:10

click

39:10

click on.

39:12

In other face

39:12

it is very simple

39:13

to use a model.

39:14

Just click on it.

39:15

And once you click

39:15

on it, you

39:16

you have

39:16

this type of

39:16

a page

39:17

like that

39:18

all LM

39:19

mini

39:19

page

39:20

had got a

39:20

page

39:21

just say use

39:22

the model

39:22

and just

39:23

click on

39:23

transformers.

39:24

that's

39:24

it.

39:24

nothing.

39:25

It's

39:25

simple, very

39:25

simple to

39:26

use the

39:26

model.

39:27

That's it.

39:27

So the way

39:27

we use it

39:28

is the same way.

39:29

That's it.

39:29

Just use

39:30

the model

39:30

and it will

39:31

be very, very

39:31

simple to

39:32

just use these

39:33

models over now.

39:35

Okay. You've got

39:35

another model

39:36

if you want to

39:37

use something

39:37

else.

39:38

You have this

39:38

try

39:39

try to.

39:40

GTE,

39:40

two.

39:41

use the model.

39:43

Now see,

39:43

sentence transformers

39:43

available

39:44

is a massive

39:45

model.

39:46

This is like a

39:47

model

39:47

which is taking

39:48

every

39:49

sentence and

39:50

converting that to

39:51

8,

39:51

960

39:51

vectors.

39:53

So this

39:53

I'm just checking

39:55

if I can

39:56

download this

39:56

1.5 billion

39:58

parameters

39:58

I think we can do it.

40:02

2 billion

40:02

parameter

40:03

must have

40:03

so we can try it

40:05

it out.

40:05

It will be fun right?

40:06

So you

40:07

your sentence

40:07

transformer

40:08

here.

40:09

Now look

40:09

here

40:09

here

40:09

very simple.

40:10

you

40:10

you know

40:10

you

40:11

see

40:11

and everyone

40:12

everyone's aligned

40:13

okay,

40:13

very simple

40:14

now

40:14

look like

40:14

we are now

40:16

loading this

40:16

model

40:16

and you can say

40:18

sentences

40:19

you can say

40:19

four sentences

40:20

and you can

40:21

simply say model

40:22

code

40:22

and what will

40:23

happen

40:23

it will go back

40:26

and it will

40:26

effectively

40:27

generate with the

40:28

and it will be

40:29

interesting

40:29

and this is actually

40:30

what we do

40:30

you know

40:31

in real world

40:31

scenario

40:32

now you

40:32

ask you

40:33

what you can't

40:33

what model

40:34

use

40:34

we'll

40:35

that we will come to

40:37

at a later

40:37

time

40:37

yeah,

40:38

exactly,

40:39

exactly, this is

40:40

exactly what I was

40:41

talking about

40:41

and Ali has asked a

40:42

perfect question.

40:44

Ali has asked a

40:44

question.

40:45

Ali, this is exactly

40:46

what we have to try.

40:48

We have to try

40:48

we have to try

40:48

very good question.

40:50

Now you'll say,

40:50

sir,

40:51

our course

40:52

we're our content

40:53

we're only

40:53

we're only

40:54

all mini

40:55

LM, L6

40:56

use

40:56

why do?

40:57

Because it's popular

40:58

just to explain

40:59

but your point is

41:00

very good.

41:00

It's many

41:01

many models available

41:01

thousands of

41:02

models are available

41:03

which

41:03

I'm trying to show you right now and it is so easy to use it.

41:06

So what you'll, in real world scenario,

41:08

you will keep trying different

41:09

different models and see which model

41:12

will generate the best embeddings for you.

41:14

This we have to try

41:14

and also what happens is

41:17

there are different types of evaluation methods.

41:20

When we get to the details of

41:21

RAC systems,

41:22

we'll evaluation discuss

41:23

from other models try

41:25

like we're machine learning

41:26

we were trying different

41:27

models and we will choose the one

41:29

that is giving us the best results.

41:31

So something very similar

41:32

we will follow even in this approach.

41:33

also. But we

41:35

some standards use

41:37

it. It's not that we randomly

41:38

try everything, but I just wanted to make

41:41

you all aware

41:43

that it is very easy to use this model.

41:46

Okay? You're up, up, up. You know, just code

41:47

take this code. It's nothing.

41:49

You know, just here just

41:50

this code. So the same demo that I did here,

41:53

all I will do,

41:55

all I will do, I can just

41:57

take the same code.

41:59

What I will do right now?

42:00

We'll just load it. That's it.

42:02

This is your sentence transformer.

42:03

The code is same. And after that,

42:05

all the same to same. I can literally copy

42:07

the entire code as it is.

42:10

Sentence-a-sentence be too already available.

42:12

This is not going to do.

42:13

We're just back code

42:15

up and copy-paste

42:16

is. Is there any difference between this and this?

42:19

Nothing, right?

42:20

Only difference is,

42:21

you know, we've made the model

42:21

and used here.

42:23

Okay, it's simple.

42:24

We're hugging paste

42:24

we just used and here

42:26

here here.

42:27

You can run and you can compare the results.

42:30

This is a little bit

42:30

model.

42:31

You can see that

42:32

you'll see that

42:32

look at the lab in users, okay?

42:35

That's not bad. But anyways,

42:36

you'll get an idea of the RAM usage.

42:39

RAM, there's a little used here.

42:41

And you can't see it is downloading.

42:42

Oh, wow, no, my mistake. I thought it'll be a smaller model.

42:48

My mistake. I thought it'll be a smaller model. My mistake.

42:49

We made, but you know, this is the nice demo.

42:53

It will allow us to actually show you the power of how big these models are.

42:57

The first one was very simple.

42:58

This is a 7 gp model is.

43:00

You can see how we're, you know,

43:01

how we model for load and download

43:03

it? Download, what are you? You're downloading

43:05

and it's a RAM in load

43:06

you. Now, look, look,

43:07

KOLAB's RAM

43:08

back. And if you try to download

43:11

too big a model,

43:12

COLAB might also crash

43:13

sometimes. This is something that you can

43:15

is very interesting to actually see.

43:17

This is local machine in download. And

43:19

for us right now, the local machine is

43:21

Collab. So, internet is

43:23

quite fast, no problem. But

43:24

okay, I hope that answers your question,

43:27

typically. Mostly it is about trying.

43:30

Second thing, to some extent.

43:31

you can also look at it.

43:32

This we have

43:33

here there are

43:34

many many metrics.

43:35

So,

43:35

so we have not seen

43:37

until now.

43:38

Eventually we will

43:39

see these things in

43:40

detail, but

43:40

here there are

43:41

many different benchmarks

43:42

there are a lot of

43:43

different benchmarks,

43:44

how different

43:45

models are performing

43:45

in different

43:46

different tasks.

43:47

So your business problem

43:48

what is it that

43:49

you are trying to solve?

43:50

Is it a classification

43:51

problem?

43:51

Is it a clustering problem?

43:53

Is it a

43:53

multi-level classification

43:54

problem?

43:55

Is it a fair classification problem?

43:56

So here here

43:56

look,

43:57

different scores

43:58

are.

43:58

So you can what

43:59

you can do?

44:00

You can do you

44:00

in descending order.

44:03

That means you want to choose that particular model,

44:05

which is giving me the best

44:06

classification scores.

44:08

Does it make sense?

44:08

I hope this is clear.

44:09

So this is another way you can go back and,

44:11

you can choose,

44:12

you know,

44:13

you can go back and choose the best model.

44:15

So this is the best,

44:16

this is the model with the highest

44:17

classification score.

44:19

If your use case classification

44:20

then you,

44:21

then you have a type of model

44:21

choose can set here.

44:23

So this is another way to decide

44:24

which model you want to use.

44:26

Okay?

44:27

So,

44:28

yeah,

44:29

so I think there's some issue.

44:30

I think I went out of memory or something.

44:32

So, okay, this is just to help you understand.

44:34

I'm not going to run this code.

44:35

So sort of out-of-memory

44:36

one thing is here.

44:37

Okay, that's why

44:38

Mini LM is the safest bed,

44:39

but this is a very, very big model.

44:41

But I just wanted to let you know

44:42

how easy it is to access it.

44:44

Okay?

44:45

Yeah.

44:47

Chalo has asked a question.

44:49

Sir, Olama the other day I installed

44:50

is not showing in my system.

44:53

No, no, no, no,

44:53

that's not anything.

44:54

You have to control panel

44:55

go and install can't.

44:56

Olama is 100% there.

44:58

If you, in fact,

44:59

if you type Olaama,

45:00

Sangita, Olama, will be,

45:02

it will be, I mean,

45:04

it could be some reason

45:05

you've been, shall uninstalled

45:06

or anything.

45:07

Two ways, you

45:08

you know,

45:09

number one.

45:10

Number two is

45:10

you, it's

45:11

you usually

45:13

shows up here.

45:14

If you click on that

45:15

task bar or

45:16

your, you

45:17

here on your

45:18

little, you know,

45:18

there's a little

45:18

oldama

45:19

icon

45:20

from, okay?

45:22

So you can see,

45:23

but it's not a big deal.

45:24

It's okay,

45:25

I mean,

45:25

it's not a big deal,

45:26

then, you're,

45:26

then you're not a big deal,

45:28

okay?

45:29

Waped off off.

45:30

Okay, that's great. That's great, that's great on it.

45:32

If it worked for you, that's amazing. That's amazing.

45:34

Yeah, so

45:34

that's a little constraint

45:35

so it works fine.

45:38

Now, moving on, guys.

45:40

So we have talked about

45:41

what is embeddings?

45:42

Okay, so now let's move on.

45:44

Let's come to the next phase of our conversation.

45:51

So basically,

45:51

idea

45:52

people have

45:53

you take the whole document,

45:55

you divide that document into chunks or sections.

45:58

Chute and different sections.

45:59

To divide,

45:59

and then

46:00

each and every chunk

46:02

you go back

46:03

and convert them to

46:03

embeddings.

46:04

You take each and every

46:05

chunk and you

46:06

convert them to

46:06

embedding.

46:07

Like we

46:07

our example

46:08

last session

46:08

did.

46:09

You take a

46:09

massive

46:10

PDF file

46:10

which is

46:11

having 100

46:11

pages.

46:12

That's not

46:13

massive

46:13

not a example

46:14

I'm

46:14

not a example.

46:14

100 pages

46:15

is not massive

46:15

actually.

46:16

But you take

46:17

a massive

46:17

PDF file

46:18

which is

46:18

spanning 100 pages.

46:20

100 page

46:20

of a page

46:20

page file

46:21

up.

46:22

Then then

46:22

next thing

46:22

what you do

46:23

you do,

46:23

you divide that

46:23

entire

46:24

PDF into

46:24

chunks.

46:25

Now chunks

46:25

to

46:25

divide one, chunk two

46:27

chunk three.

46:28

And you

46:28

can use a simple logic like every page is like a chunk, something like that. So, so chanx

46:34

chunks made. So saw text chunks

46:36

and now you take each and every chunk and you'd say model dot and model dot input.

46:40

Whatever we were saying, model dot input. So you take each and every one of those chunks and you

46:44

say dot in quote, dot input. So every chunks are your embeddings are

46:48

like chunk one embeddings are

46:50

here. Chunk two can embeddings are here. That's the idea. And

46:54

what is the next phase?

46:55

That is the next thing. That is the next thing. That is the next thing. I will talk.

46:58

about.

46:59

You can how it's how chroma dv in store can. I will show you.

47:02

This there's a code. I don't want anybody to get worried about the code.

47:06

Concept here. This is the main idea. And now whatever we will see is just some hands on, just some

47:11

code so that, you know, you'll get able. Just just one or two more concept pieces that we will be

47:17

seen. But the chroma db part, there will be some syntaxes. There'll be some code demos that we

47:21

will be seeing right now. But the core idea should be clear. You take the text and you convert the text

47:27

into, you know, a sequence of numbers. Okay. Now, moving on. How to search embedding model on

47:43

on hugging face? Me, this is nothing but, see, there are two ways you can do it, Ali. So number one,

47:49

you can actually go to this site. You can go to this side. This is the massive text embedding leaderboard.

47:55

You have a main leaderboard where all the top embedding model model.

47:57

are compared. And the second place where you can go is this place. This is the other place.

48:04

A sentence transformers type. So in fact, you just go to the sentence transformer section. And I already

48:10

ping that. I think I already ping that to you know. Let me just share that again with you.

48:19

Yeah, I already ping that to you. Just click on the link and you will see that.

48:23

I will link quickly for and that and that will answer your question. Just click on the link.

48:27

And you will see that model, okay? Just click on the link ones. And the second place

48:32

where you will see the list of all the models is this, sentence transformers. Up sentence transformers

48:37

make click on table. You can see the list of all the models. So this is the other place where

48:42

you will see the list of all the sentence transformers models. So please, uh, bookmark these two places.

48:48

Okay? So let's move on. And this is just two kind of, uh, uh, and this is just to kind of, uh, uh,

48:57

clarify this idea once again. We've already talked about it, but you can see that, you know, very broadly,

49:03

this is what we are doing behind the scenes. Very nice diagram is kind of clarifying this again for us.

49:07

You can see. So we are taking the raw text data and we are breaking the data into tokens.

49:12

That we have put some kind of text. Machines don't understand text. So machines are breaking

49:18

that text into tokens. There is some neural network behind the scenes which is converting that entire thing

49:24

into a vector of numbers. This he go on embeddings kettel. And

49:27

this is something that we will eventually store in a vector d. And then we'll compare

49:31

what is comparison we see later. But this is the core idea. So we'll tokenize

49:35

and we'll embed using our embedding models and then we will store it in the vector db. So that's

49:42

the basic idea. Okay. That's a general idea. Now moving on.

49:57

So that is, that is something that I wanted to clarify. The semantic concept is very, very important. Okay. Now, what I, what we will do now is we'll take a small example. And since we talked about vector databases,

50:27

There is another very interesting kind of a diagram that talks about the difference between a normal database and what is the vector database.

50:37

You can see this particular diagram that very nicely explains the idea in detail.

50:43

So everyone can just take a look at it.

50:45

All of you can take a look at it.

50:47

So basically on the left hand side is what you guys have done.

50:50

Left and side of the thing you've done.

50:52

We talked about relational database. I already mentioned that term.

50:55

Whatever we have generally seen and what?

50:57

Whatever we are generally used to see is a RDBMS, relational database management system.

51:03

Like your MySQL world benched.

51:05

Okay, this your data, this is your RDBMS is, okay?

51:09

So I have to just take a minute and show you what you are seeing on your screen right now is a RDBMS system.

51:15

Here here your data, here your table, there is something everybody in the class has seen.

51:20

You have a table say you can do select star.

51:22

So these statements, everybody is aware how to do it, right?

51:25

So you can do queries like select star from.

51:27

After data digs in table, where clause, you know, you guys have done this, right?

51:31

So this is like nice thing to analyze.

51:34

Okay, so where clause, in, where, select where, from, group, by, order by.

51:39

You guys have seen this.

51:40

This is like a relational database, okay?

51:42

Where data is stored as tables, rows and columns in a very structured manner.

51:47

Data structured, you know, the kind of data that we are mostly used to.

51:51

Now on the other hand, you have another kind of database called a relational vector database.

51:56

Okay.

51:57

So what is the good thing about working with relational database?

52:03

In relational database, you have a concept called exact match.

52:07

If we have to retrieve kind of, this is important thing, okay?

52:11

So we have a users table.

52:12

You can see the left-hand side demo.

52:14

Users' table.

52:15

Here, here four rows or a saw rows, or so any, I'm just showing the top four rows for you.

52:20

And you can see the rows are like this.

52:22

You've got user ID.

52:23

You have a user name, you have an email ID, you have a sign-up data.

52:27

Now, use case is.

52:29

Use case is that, by user ID 7 data need.

52:33

For whatever reason, you know, like management may query

52:37

or then, some reporting, some requirement.

52:40

Customer, could ask, that, by, my data do.

52:42

So what will you go back to your database.

52:45

You select start from the table where user ID equal to 7.

52:48

fetch that row.

52:49

User ID 7 have bob.

52:51

So, it's a row to roll out of the manager for do.

52:53

That's it.

52:54

This is a simple, exact match.

52:56

So SQL works primarily on the basis of that.

53:00

Whatever SQL you have done, whatever SQL course you have done using MySQL.

53:05

I think my SQL mostly you guys have used.

53:08

You know, so you have used exact match.

53:10

You have made exact match.

53:12

So if user ID 7 exactly match on,

53:16

then you go back to retrieve it.

53:17

No, not it were not.

53:18

Here there any approximate match or anything.

53:21

User ID 7 has, we need to be that.

53:23

We need to return to.

53:25

So let's start.

53:26

straightforward.

53:27

Right, everybody is aware of that.

53:29

Now, what is different in a vector d.

53:31

Now, what is different in a vector db?

53:32

Now, what is the diagram perfect?

53:35

But let me, uh, let me add my flavor to it.

53:40

It conveys the information, but I think it's not perfect.

53:43

But let me just add it.

53:46

Add a few things here.

53:48

Give me one second, myself.

53:50

So the time has got shortened from today.

53:55

day.

53:56

8 to 10 so we'll take a break around 9 and it's around 10.

54:00

So we go like 5, 10 minutes max 10 10.

54:03

Okay.

54:04

But we'll take a break around 9, another 10 minutes.

54:07

Okay, just to keep all of you aware.

54:10

Now, this is the vector degree.

54:17

Here we have chunks.

54:21

So chunks are, you have your C1 or your C2 is.

54:24

This story.

54:25

already discussed last session.

54:26

You may repeat.

54:27

I'm not going to, that we've already discussed

54:29

you take the whole PDF.

54:31

It's a page of PDF.

54:32

You have a PDF to divide in chunks.

54:34

Chunks are nothing but the sections.

54:36

And then you embed the chunks.

54:38

So, let me is a different color.

54:40

So chunk 1, something like 0.11, 0.12.

54:44

chunk 2.

54:45

Chunk 2.

54:46

2.

54:47

0.12, 0.13.

54:49

Chunk 3 had.

54:50

0.11.1.

54:52

0.13.

54:53

Okay.

54:54

chunk 4, something more.

54:55

Now, if you take a look at it, as I told you,

54:58

these numbers are giving you the semantic meaning of the document,

55:02

semantic meaning of the chunks.

55:03

For the chunk is what the chunk is.

55:05

These numbers are somehow conveying what the chunk means.

55:07

Now, think about it.

55:09

This is our relational database.

55:11

That was the story we were discussing, right?

55:13

Exact match you can do, exact lookup you can do.

55:16

You can do.

55:17

You need, same it.

55:19

Now, think about it.

55:21

How do you look up something in a vector database?

55:24

in a vector database.

55:25

Here,

55:26

here,

55:27

you can look-up

55:28

what you?

55:29

What do you?

55:30

Use case is what?

55:31

We talked about

55:34

retrieval augmented generation,

55:35

the whole pipeline in the last session.

55:38

One thing,

55:39

remember, guys.

55:40

What was the retrieval part of the workflow we discussed?

55:42

I'm going to take you back to that for a minute.

55:44

So the first part is clear.

55:46

The first part clear.

55:47

The first part is.

55:48

Text.

55:49

You have a PDF file.

55:50

That you,

55:51

you have,

55:52

sections,

55:53

it.

55:54

C1, C2 are the different chunks of the document.

55:56

Chunks go off embeddings in convert for.

55:58

Chunk one is this, chunk two is this, chunk three is this,

56:01

chunk four is this.

56:02

You convert that into embeddings,

56:04

and you store in the vector DV.

56:06

That's the first phase is over there.

56:08

Second phase is,

56:10

when user has a question,

56:13

you have to retrieve the similar chunks.

56:17

So let me show that workflow.

56:20

If the moment when users ask a question,

56:24

The moment when users ask a question, this is your user question,

56:28

I'm here here here, okay?

56:30

This is user query.

56:33

User query,

56:35

which you're you're using

56:36

this is user question.

56:38

So user has a question.

56:40

User question is, okay?

56:41

User question is that how many leaves do I get in a year?

56:45

How many leaves do I get in a year?

56:46

How many leaves do I get in a year?

56:53

This is the user question.

56:56

How many leaves do I get in the year?

56:57

This is what we are, you know, looking at behind the scenes.

57:01

So user has a question asked, how many leaves do I get in the year?

57:03

This is the query.

57:04

This is the prompt.

57:05

It's like a user is typing this in the chat.

57:09

Now, what machines?

57:10

To this is the same embedding

57:11

text, what, string, what is?

57:12

It's not so the same embedding model

57:15

will be used to convert this query into its corresponding embedding.

57:20

I'll give an example to you.

57:21

The corresponding embedding.

57:23

for this query will be something like, again, I'm just giving an example. I'm giving a ballpark number.

57:27

It will be something like 0.13, 0.13.1. And what you are seeing on the screen right now is a query

57:35

embedding. This we're what we're saying? This form query embedding. Okay. Not very difficult, right?

57:45

So user's question. User has asked. You know what machine? We don't know. We have

57:49

we have machine language to convert it. So machine has converted that into query embedding.

57:53

That means these, this set of two numbers tells you what is the semantic meaning of the user's query.

58:04

0.13.11.

58:06

This user's question.

58:08

Or our vector database, what is stored in the vector database?

58:12

Here we have chunk embeddings.

58:14

Okay?

58:14

Vector database in we have got chunk embeddings.

58:23

And all that you are trying to do, user has asked a question. You need to go back to the vector db and find out what my relevant chunks are.

58:36

That means, if your PDF document is, if you have, if there are like close to 100 chunks that you have right now,

58:47

I mean 100 sections of the document you have to have. You are trying to understand that.

58:53

To answer the user question, user's question, how many leaves do I get in a year?

58:58

You are trying to understand which portions of the PDF or which of the chunks can be used to answer that question.

59:06

That means, which of those chunks are most similar to the question that has been asked.

59:12

And this is your similarity search.

59:16

Yeah, here. I'll just add one more thing here. It is called semantic similarity search,

59:22

Vector semantic search.

59:23

Semantic, meaning, context.

59:27

This is the thing of your vector delete.

59:28

D.D.D.D.B.

59:29

So whereas in relational database, it is an exact lookup.

59:31

There is no concept of semantic lookup and all that.

59:34

Okay.

59:34

Because you can't do you.

59:36

If user ID's with us, it's up to do it.

59:38

No, if it's not, so no, I can't return.

59:40

Select is already operating, where it was operating based on an exact match.

59:44

That's it.

59:45

And here it is working based on a similarity match.

59:49

User is asking a question.

59:50

Convert that into query embedding.

59:52

And you want to find out that which of the chunks are most similar to the user query based on their embedding values.

1:0:00

So query embedding over 0.13.11.

1:0:03

That is what conveys the query embeddings for you.

1:0:06

And chunk embeddings are, look.

1:0:07

And you can ask the question that, okay, based on whatever question the user has asked,

1:0:11

please find out what the top three chunks are.

1:0:15

Konsa that top three or four or five chunks are, which are most similar to the user query.

1:0:22

Uh-huh. So, uh, uh, and, and, and, and, and very interesting, I think,

1:0:29

answer what answer is? Can you tell me based on whatever values are given?

1:0:33

Your query embedding is, you tell me out of C-1, C-2, C-3, C-4,

1:0:37

what's the most similar chunks of you see? Tell me, guys.

1:0:41

No, Anj, Anj, the keyword, like, you, I mean, I get it up.

1:0:46

Like, you, like, you're, like, you can't, I see where you're coming from.

1:0:49

You can't, but that is not the accurate way of doing it.

1:0:52

this. I'm saying the top three. You have to retrieve the top three. Let me

1:0:55

is a different color. You just tell me the top three. Just tell me the top three

1:0:59

similar chunks. I wanted to tell me what are the top three similar chunks based on.

1:1:05

You have to retrieve it. If you go back to the rag discussion that we did, you have to

1:1:10

retrieve the top three similar chunks. Okay. Okay. Anjur, I hope that is clear. Keyword search

1:1:14

to what your thing will limited and it may not be very accurate. Or

1:1:18

no, I'll tell you, I'll answer you a question.

1:1:22

that you asked, how many leaves do I get in a year?

1:1:27

So, it's not necessary that document on the word

1:1:30

will be. Now, the PDF

1:1:31

text there, there's like, okay, the person is entitled to seven holidays.

1:1:36

There, leaves term is used there. You know, how many leaves do I get in a year?

1:1:40

But the document there, contented, you know, employees get seven holidays.

1:1:45

But semantically, they are still similar.

1:1:47

I hope I'm able to answer. So keyword match, by the up,

1:1:49

now, okay?

1:1:51

Got it?

1:1:52

Exactly. It's more convenient. That's right. Yes. It predicts this can be. This can be. This may be. Exactly.

1:1:59

So I hope everyone's with me. C1, C2, C3.

1:2:02

Okay. So similar chunks what are? Similar things are? C1, c2, comma, c3. So based on whatever

1:2:12

question the user is asking, the query embeddings are this. 0.13.11.

1:2:17

Yeah, your query embeddings are. The query embeddings are 0.13.11. These are the query embeddings.

1:2:22

That means, this is the way we are able to convert the query into a numerical form.

1:2:27

That your numerical representation of the query, which gives you the contextual meaning of the user question.

1:2:32

The user has asked, and now you're going back to the vector db, where all your chunks are stored.

1:2:38

And you're asking, if this user has asked, can I go back to my vector db and find out, what are the top three chunks that are similar to the question that is asked?

1:2:47

That's it.

1:2:48

Please retrieve the top three chunks.

1:2:52

that are similar to the question the user asked.

1:2:56

Similar in terms of what?

1:2:58

Now, I'm going to say, sir, similar in terms of what?

1:3:00

Semantic similarity.

1:3:01

Similar in terms of semantic, similar in terms of semantic, similar in terms of meaning.

1:3:06

And here here here, so I've got to do this,

1:3:09

no calculation here but I just used basic intuition.

1:3:12

You know, the values are 0.13.11.

1:3:15

And here the values are 0.11.1.

1:3:17

0.1.2.

1:3:17

That's similar.

1:3:18

0.13.1.

1:3:19

is similar.

1:3:20

C1 is very close.

1:3:22

query embedding is C2 is also very close.

1:3:25

Query embedding is this.

1:3:27

That means chunk one, chunk, two, chank three, which page one, page two, page three is basically as an example.

1:3:33

These three pages approximately contain the answer.

1:3:37

Approximately contain the answer.

1:3:40

Okay, so because they are very close.

1:3:41

That's the way to look at it.

1:3:44

Yeah, so that we're defined kind.

1:3:46

That's the distance formula from, for it.

1:3:48

Because we are saying top three similar chunks.

1:3:50

Similar, what?

1:3:51

Similar, what?

1:3:51

Similar based on the distance.

1:3:53

You're choosing similarity based on distance.

1:3:55

You have this query embedding and this chunk embedding.

1:3:59

So how are we saying that?

1:4:01

How are we saying that?

1:4:02

How are we saying that, okay, query embedding 0.13.11 is similar to this.

1:4:06

Distance, distance formula we are actually doing.

1:4:09

Okay, so we are actually using things like Euclidean distance,

1:4:12

which you have your time distance between two points and a coordinate axis.

1:4:16

You know, you can't even distance.

1:4:17

You can't even decalcedent.

1:4:19

Okay, so I hope that clarifies.

1:4:20

It will never be exactly the same.

1:4:21

The query of the embeddings, based on that, you are trying to find out what are the similar,

1:4:26

what are the closest chunk embeddings based on distance.

1:4:31

Okay, Amit, let me know.

1:4:33

Is it clear?

1:4:34

How do you decide which chunk to pick?

1:4:37

This is how you decide which chunk to pick based on the distance, how close it is to the query embedding.

1:4:42

And we here here here, I want to take the top three similar chunks.

1:4:46

This is up to me.

1:4:46

This is what we have to decide top three, top four.

1:4:49

That's a related date.

1:4:49

But for now I'm saying top three.

1:4:51

So moment I say top three similar chunks am I do, so what will it do?

1:4:55

It will take the query embedding and it will find out the distance of the query embedding with all the chunk embeddings.

1:5:01

It will find out the distance of the query embedding with all the chunk embedding.

1:5:05

All the chunk embeddings are our distance calculate.

1:5:07

Okay.

1:5:08

And based on that, it will return those chunk embeddings, those three chunk embeddings where the distance is the least.

1:5:14

Distance least, what's the same similar time.

1:5:17

Okay?

1:5:18

Does it make sense?

1:5:19

I hope you are clear.

1:5:21

Let, now, which one will it choose least distance one?

1:5:31

No, the top three, two, three only choose.

1:5:34

Three only choose.

1:5:35

That, that's, you know, that you'll calculate.

1:5:37

I think here here you're going to calculate for it.

1:5:39

Okay, so I think, I mean, if you want to work through the mathematics, I can take you through it,

1:5:44

no problem.

1:5:45

I can take you to it to it.

1:5:46

If you want to work through the math, we'll make you a example, okay.

1:5:49

I think you'll be clear.

1:5:50

Okay.

1:5:51

Here we'll show you, this is your X1, this is your hidden dimension one, this is your hidden dimension two.

1:5:57

Okay, so your query embedded, point one, so point one, so point one-three is the ex-coordinate.

1:6:03

This is your like point-13 is, right? So, once a second, let me just write it down.

1:6:08

This is your point-13 or your point-11, okay? So this your query is embedded. I'll say Q, query.

1:6:13

So we'll call it, okay? This is your query here. This is your query. And let me write it this way.

1:6:19

here. That is, this value 0.13. It's, its value 0.11. It's. And here

1:6:27

C1, C2, C3, we can get. Okay. Yeah, so those are the, those are the distance metrics.

1:6:32

Garima, I'm not in this session. I'm not getting into the details of those metrics right now,

1:6:36

but I'm just giving the intuition. Yeah, but what you are, what you are saying is right. What you're

1:6:40

saying is right. So C1, C1, 0.1, 0.12. So 0.11 and 0.12. So C1. So C1, 0.1. So C1, 0.1. So C1,

1:6:47

1.1 around here. And point 1.2 is here. Okay. So you can

1:6:53

how you can represent it. So I'm just trying to make it easy for everybody.

1:6:58

This is C1. Okay. So, so you have a point

1:7:01

1-1 got. And it's your point 1-1. And it's your point 1-2. Okay.

1:7:07

So you can see, distance calculated.

1:7:10

If we're going to say, C-1 and Q-based distance make out. So, Amit,

1:7:14

C-1 or Q-in between between distance.

1:7:17

How do you calculate?

1:7:18

Root over?

1:7:19

This formula, you know.

1:7:20

Route over X2 minus X1 whole square plus Y2 minus 51 whole square.

1:7:24

I'm not trying to scare the others, but just to answer your question, Amit.

1:7:27

What you can do?

1:7:28

So, right?

1:7:28

So, way, you can do?

1:7:30

Or be, or other distances are.

1:7:32

So simple.

1:7:33

The best part about converting text into a numeric vector is,

1:7:39

all of a sudden, you can visualize that in a coordinate space.

1:7:43

All of a sudden, this text query is, how many leaves do I get in a year?

1:7:46

Like you've been number in number, and this is the best part about embeddings,

1:7:50

you can actually represent this in our coordinate space.

1:7:53

Now, you can look, that, yeah, this is a query, this is your chunk 1.

1:7:57

chunk 2, we'll put in, chunk 2.

1:7:58

chunk 2. Where are? Chunk 2? Where are?

1:7:59

chunk 2? Here here.

1:8:00

chunk 2 will be. 0.12, this is 0.12, and 0.13.

1:8:09

This is your chunk 2.

1:8:10

and chunk 2. And chunk 3, 0.11, 0.11.13.

1:8:14

chunk 2.

1:8:16

So 1.1.1.3.

1:8:18

These three chunks are. And chunk 4, where will be?

1:8:20

0.4, 0.8.9?

1:8:21

Chunk 4, it will be here.

1:8:23

C4 will be massive.

1:8:24

It will be 0.8.9. It will be very big.

1:8:27

So, you can see,

1:8:27

that the query here is.

1:8:29

So, user has the question

1:8:31

this question.

1:8:32

The user's the context is,

1:8:34

which of the chunks are most similar to the user query?

1:8:38

You can simply do a distance formula.

1:8:40

That query with the query with

1:8:41

all chunks of distance

1:8:42

we choose those top chunks

1:8:45

where the distance.

1:8:46

is the least. I hope this is now pictorially clear to you, Amit, what is going on behind

1:8:51

the scenes. Okay. And, uh, okay? And this is basically the retrieval part of what we do in a,

1:9:05

in a typical drag system. Okay. So just to summarize the conversation, there are two main, there are two key

1:9:11

takeaways from this conversation. We talked about exact match. You on our DVMS in this

1:9:15

and, uh,

1:9:18

johm,

1:9:19

chroma db is the vector database.

1:9:22

Vector database we are doing a similarity search.

1:9:25

We are doing a semantic search, a semantic match.

1:9:28

So exact match for a normal database,

1:9:30

whereas a semantic search for a vector database.

1:9:34

Vector database in we are trying to find out the similar chunks.

1:9:36

So similar,

1:9:37

similar chunks is what we are basically trying to find out.

1:9:40

So based on a particular chunk, based on a particular question,

1:9:43

what are the similar chunks that,

1:9:45

that answer the question in the best possible way.

1:9:48

So similarity basis, if we apply to two things.

1:9:51

So now, this one line be both actually

1:9:53

written to the most similar items,

1:9:57

nearest neighbors, based on meaning in the vector space,

1:10:00

which I have explained to.

1:10:01

So query is.

1:10:03

Chunk one, chunk two, chank three,

1:10:04

this is.

1:10:05

So based on the query,

1:10:06

what are the nearest chunks,

1:10:07

which means similar to the question that you're asking?

1:10:10

So that is the way how we understand the concept of ritual.

1:10:15

Okay, I hope everyone's aligned.

1:10:18

Next, what we will do?

1:10:19

We will actually look at some cold.

1:10:22

So we will be using chroma all through in our sessions.

1:10:24

But if you're, if you basically are looking for two other, a few other examples,

1:10:30

these are a few other examples that we have here.

1:10:32

We have chroma, we have FICE, just for you to be aware.

1:10:35

We have something called PG vector, PG vector ACOR, vector DTB

1:10:39

inside Postgres SQL.

1:10:40

And there is another very, very popular option called pine cone.

1:10:44

Okay.

1:10:45

So this is just for your information, FineCone.

1:10:47

Fine Cone is an enterprise managed vector database.

1:10:51

The thing is the concept same in.

1:10:53

You have, document chunks low,

1:10:55

you can convert it, and you have those database in store.

1:10:58

So the most popular option that we are going to be using is called ChromaDB,

1:11:01

which is what we'll be using in our demos also right now.

1:11:04

So now we'll be seeing how these labs are right now.

1:11:10

We'll see that.

1:11:11

So first we will see this entire pipeline in action.

1:11:15

Now, you can see whatever pipeline will be seen.

1:11:17

So whatever we'll be seeing in the lab right now.

1:11:19

So this whole pipeline we'll be right now.

1:11:22

All of you can just give it a glance, everybody.

1:11:24

Just give it a glance.

1:11:26

What is the pipeline we will do right now?

1:11:27

Very simple.

1:11:28

We've actually already talked about every single part of it.

1:11:32

Sir, again, Mahmad.

1:11:34

Yeah, sir, Ali, which, what do you want me to clarify?

1:11:37

What do you want me to repeat?

1:11:37

Please tell me.

1:11:40

What do you want me to repeat?

1:11:41

Please tell me.

1:11:42

I just explained.

1:11:43

No, Kroma is just a name.

1:11:46

Kroma is just a name.

1:11:47

What is chroma DB?

1:11:48

Kroma DB is a kind of a vector database.

1:11:50

So this thing we've explained here.

1:11:52

Like, my SQL.

1:11:54

MySQL is a relational database.

1:11:56

Where you can write, select, start from all these kinds of queries.

1:11:59

So here you can table store can.

1:12:02

Tables in rows and columns.

1:12:03

This is what we're saying?

1:12:04

This form relational database can't.

1:12:07

So let me just type it out for you.

1:12:09

So we call it a relational DB.

1:12:13

Similarly, we have something called a vector db, where we can store vectors.

1:12:18

This we'll store where we can store where we can store if you, if you're data folia chunks

1:12:20

divide it, so we can store it in a vector database.

1:12:26

That is what a vector database basically stands for.

1:12:30

So you can basically store this entire thing in a vector database.

1:12:34

So and these are examples of vector dps, chroma, fies. These are examples of vector dps.

1:12:39

So what is chroma db?

1:12:41

chroma db is nothing but an example of a vector to levels.

1:12:46

Okay.

1:12:46

Are you with me, Ali?

1:12:53

Okay?

1:12:54

So all of you, please, please give it a glance, everybody.

1:12:58

Just give it a glance.

1:12:59

This is the pipeline we'll be seeing now.

1:13:02

Is it a pipeline we'll see in action?

1:13:07

And from here onwards, it will be hands on, we will do, okay?

1:13:11

And you can see the code is already uploaded.

1:13:15

As always, 26 May.

1:13:17

The content is here.

1:13:18

Very simple.

1:13:19

This is just one notebook file we have got right now.

1:13:21

And as I told you, we are breaking up the rag into multiple sessions.

1:13:24

So this is another layer we are adding.

1:13:26

And eventually in the next two sessions will complete the whole rack pipeline.

1:13:29

Then you will see the whole thing in action.

1:13:32

Okay, so we are again breaking.

1:13:33

This is only partial code I've shared with you, relevant to our class today, but you would use.

1:13:36

But slowly we are seeing the rag thing adding up.

1:13:40

All right.

1:13:41

file for today also. Okay. You guys want to take a short break. We can break for

1:13:46

five minutes. It's nine, nine to on the clock. So we can break for five minutes. And after we come

1:13:51

back, we'll be seeing the six step pipeline. The chroma lab is what we will be exploring

1:13:57

after the break. Okay. So this is what we'll be seeing. I will present this in the screen so that

1:14:02

people can give it a glance. And this is what we can see in detail after the break.

1:14:11

Thank you.

1:14:41

Thank you.

1:15:11

Thank you.

1:15:41

Thank you.

1:16:11

Thank you.

1:16:41

Thank you.

1:17:11

Thank you.

1:17:41

Thank you.

1:18:11

Thank you.

1:18:41

Thank you.

1:19:11

Thank you

1:19:41

Thank you

1:20:11

Thank you

1:20:41

Thank you

1:21:11

Thank you

1:21:41

Thank you

1:22:11

Thank you

1:22:41

Thank you

1:23:11

Thank you

1:23:41

Thank you

1:25:11

Yes,

1:25:14

welcome back.

1:25:15

here we come back.

1:25:16

Thank you

1:25:46

So.

1:25:50

So now.

1:26:16

how to prepare the chunks. So I will prepare some quick chunks here with

1:26:21

with ID and metadata and metadata from chunks from chunks

1:26:24

from chunks

1:26:25

Then we'll

1:26:26

then we're embed

1:26:27

chunk embed and chunk embeding

1:26:28

the exact workflow that we talked about.

1:26:30

Next what we will do.

1:26:32

We will go back and store it in a chroma DB.

1:26:35

So we will use an absurd function.

1:26:37

Absert function is what we will use to store in the chroma db.

1:26:39

So that is what we will be

1:26:41

doing in the code.

1:26:43

Then we'll count

1:26:44

we'll verify.

1:26:45

So we will

1:26:46

we'll verify

1:26:47

how many records got added.

1:26:50

We will see that.

1:26:51

Right?

1:26:52

Next, we will do the embedding for the query.

1:26:54

query embedding

1:26:55

going to

1:26:56

then I will write a query to find the top

1:26:59

nearest vectors, whatever I explained here.

1:27:01

Here we have top three here.

1:27:03

So here we have same thing

1:27:04

take the top three.

1:27:06

And finally we will read and interpret the results.

1:27:08

So this is all we will see right now

1:27:11

and part of the demonstration lab right now.

1:27:14

okay?

1:27:15

let us see this in action.

1:27:16

Let us see this in action. Okay. Now. So the data that we will take right now is going to be in the context of a e-commerce support knowledge base. Okay. So this is the use case we are considering right now. So you have a, we have a typical e-commer support kind of a scenario. We have a typical e-commerce support kind of a scenario where e-com support is

1:27:46

So e-com support support, we have got, you know, information about, like, customers will ask a question.

1:27:53

And on its basis, the support assistant will give an answer.

1:27:56

So customer has a question,

1:27:57

how do you order is this delay, why will be delivered,

1:28:01

free shipping, or not?

1:28:02

These are a typical kind of questions you might have for Amazon, right?

1:28:05

If you want to buy something, let's say you're trying to buy a big television from Amazon.

1:28:09

You have a mind in a question, what warranty is, what is.

1:28:12

So this is like a typical e-comber support knowledge base that we are trying to.

1:28:16

user will ask a question and based on the question, the chatbot will retrieve the most similar answers.

1:28:26

That is the thing. That is the big picture idea. Okay. Now, so what we have done right now is

1:28:34

I have simulated the data. So as I told you, we are not doing a full scale rag in the session today.

1:28:41

We have a session break here in multiple parts. Imagine we have a massive.

1:28:46

PDF manual. So company has, so Amazon has a very, very big PDF manual.

1:28:58

Amazon has a very, very big PDF manual, which consists of information about this whole data.

1:29:06

So the massive PDF manual that Amazon also has. Let's take that context here.

1:29:11

So now, now, now, in the PDF in imagine there are thousands of pages we have.

1:29:16

So we have what did? We have taken that entire PDF manual, and we have divided

1:29:23

that entire PDF manual into chunks. And in my demonstration right now, we have this chunks

1:29:29

we have this chunks to simulate here. Actually, here here in the code in PDF not

1:29:33

given a PDF, because we are seeing a small drag example here, not a full one. So we

1:29:38

have only five chunks you have given. We have put a full PDF in this class in, we are seeing in the upcoming

1:29:44

session. But we have only from there from

1:29:46

chunks, five sections of text up to the end.

1:29:50

You can think that you, page number four may have, page number six

1:29:53

page number seven. So this is that the five chunks I've given to you.

1:29:57

So what are chunks? Chunks? Chunks are basically nothing but it's like ideas.

1:30:03

You've got one idea per row. There are five chunks right now. So there are like five ideas

1:30:07

that you have right now. So customers can return products within 30% or really.

1:30:11

This is an idea. This is a chunk. It's a answer. It's.

1:30:14

refunds are processed within five to seven business dates.

1:30:17

Orders above this are this. This is another chunk.

1:30:20

Okay. This is one more chunk. So text is clear.

1:30:24

Everyone knows what is the text.

1:30:26

ID is a identifier.

1:30:29

Like, your ID in SQL in your customer, ID, employee ID.

1:30:32

Like, this is a chunk ID. And this is the very, very good indicator.

1:30:36

That you, when you're you're in data in database in store

1:30:38

kind of, you have used in, you are working with different types of tables.

1:30:42

you want to store a customer table.

1:30:46

Customer table, you're stored for it.

1:30:47

So, that's for it.

1:30:47

So similarly, here also you require something called a chunk ID.

1:30:53

You have you need, you need a chunk ID. You need to chunk ID.

1:30:53

You need a chunk ID. You need a chunk ID. And you require a metric route, which is category

1:30:58

shipping, category account, category returns. So, instead of for the metadata return.

1:31:02

So you need to have the ID for the chunk.

1:31:06

Chunk. What is the unique identifier for the chunk? That is number one.

1:31:09

You need to have what is the chunk text?

1:31:11

Chunk text.

1:31:11

Chunk's text what is the text?

1:31:12

That is number two and number three, you are having some additional metadata.

1:31:17

Metadata means it is some additional information about the data.

1:31:22

Metadata means that's meant that what?

1:31:23

Some additional information about the data.

1:31:26

Means, this chunk is telling you something about shipping.

1:31:33

This is metadata, it's some additional information.

1:31:35

It's a category is shipping.

1:31:38

I mean, if any shipping-related

1:31:40

question, then this answer is.

1:31:42

This chunk is, its metadata category is account.

1:31:47

Account-related information.

1:31:49

This chunk is, its metadata category is shipping.

1:31:53

This chunk is, its metadata category is returns.

1:31:56

The refunds process is.

1:31:57

This is a product returned,

1:31:59

and this is a product returned,

1:32:00

and this is your chunk text and its corresponding metadata category is returns.

1:32:05

So this is what I wanted to clarify.

1:32:08

So don't be scared with this thing.

1:32:09

This is simple Python dictionary.

1:32:11

This is your ID, chunk to identifyer,

1:32:15

chunk of chunk text and chunk of merit data.

1:32:17

As I told you, in a real world scenario,

1:32:20

this thing you, you're in a real world scenario,

1:32:21

you'll make this one class for the session content today,

1:32:26

we are trying to divide it into a smaller thing for you.

1:32:29

So I have given you these five sections.

1:32:31

In a real world scenario, this is 5,000

1:32:35

will be that many number of chunks.

1:32:38

See, if you take a real PDF,

1:32:41

if you break that PDF into multiple sections,

1:32:43

they'll be like the PDF itself will be so big,

1:32:46

you will have tens of thousands of chunks.

1:32:48

So if you can understand the idea today with five chunks,

1:32:51

in the next session, you can understand the idea with 10 million chunks.

1:32:55

That is the idea.

1:32:57

So everyone is clear, everyone is clear with this thing.

1:33:00

I will save this.

1:33:02

This we have sampled data for prepared.

1:33:04

Number two, we will create a persistent client.

1:33:07

This we will create a persistent client.

1:33:08

This we'll come a chroma collection.

1:33:10

Okay?

1:33:11

Collection is a kind of a database.

1:33:13

This is a kind of a database.

1:33:15

This is a SQL table.

1:33:17

And this is to store our embedings.

1:33:20

That's it.

1:33:21

Rest, it is just code. There is nothing much to talk about.

1:33:23

So Chroma's module installed not.

1:33:25

The reason is because we have not run this code.

1:33:28

Excuse me.

1:33:30

You will have to pip install actually.

1:33:31

So subsets start, I should do not even.

1:33:34

Let me pip install. One second.

1:33:37

It actually session restarted in the beach in.

1:33:40

Whenever it restarted.

1:33:41

you need to actually disconnect together.

1:33:43

Let me install chroma db and sentence transformer.

1:33:48

Remember chroma db is the vector db and sentence transformer is the package that we are using to create embeddings.

1:33:54

Embedings generate to sentence transformers.

1:33:57

Okay.

1:33:58

Next.

1:33:59

So I'm going to go back and run this code now.

1:34:06

You already saw the five chunks which I have simulated for you.

1:34:09

And then what we'll, we'll create a chroma database collection.

1:34:15

And you are calling it support knowledge base.

1:34:18

This collection name is just like a table.

1:34:20

It means.

1:34:21

This is what it means.

1:34:23

This we have an analogy here.

1:34:25

Like you have SQL in a SQL database,

1:34:27

you have a table in it,

1:34:29

similarly, you're your chroma database,

1:34:31

it's in there you're a table in.

1:34:32

So table's a another name is collection.

1:34:34

When you say create collection,

1:34:36

you're creating a collection name called support knowledge base.

1:34:38

That means the name of your table is.

1:34:39

support knowledge base.

1:34:40

It's in there's all the embedding stored.

1:34:42

Embedings of these five chunks.

1:34:45

Now we will use the absurd method.

1:34:48

Now we will add data to the chroma collection.

1:34:51

Now our chroma db is

1:34:53

Db is.

1:34:54

If you're in a club in this,

1:34:56

if you're in a club here,

1:34:57

this is there is just there.

1:34:59

This is a db is just here.

1:35:00

This we are data downing.

1:35:02

Okay,

1:35:03

it's right.

1:35:04

It is called chroma store.

1:35:06

Okay?

1:35:07

This is the, this is the chroma store.

1:35:08

This is the, this is the,

1:35:09

called Chroma store.

1:35:10

And within that, we have the collection name called

1:35:12

Support Knowledge Base.

1:35:13

Collection is nothing but a table.

1:35:15

We have a table.

1:35:16

We have a table we have

1:35:18

five chunks store

1:35:20

store,

1:35:21

its metadata store it,

1:35:22

and its metadata store

1:35:23

and its corresponding embedding store.

1:35:26

That's the thing.

1:35:27

You can visualize it just like a sql table.

1:35:30

It's nothing.

1:35:32

Very simple.

1:35:33

So what I will do?

1:35:35

We must generate vectors for our documents.

1:35:37

Documents,

1:35:38

which are five chunks are.

1:35:39

the exact same sentence transformer model

1:35:41

before writing them in the database.

1:35:43

Straight forward, so the model we have loaded

1:35:45

we have already seen.

1:35:47

And here we are isolating the documents, IDs and metadata.

1:35:51

That's it.

1:35:52

This is your documents, you have your IDs,

1:35:55

you have your metadata, these the five chunks are

1:35:57

its documents, its, this is

1:36:00

text, this is, it is, and it's corresponding metadata

1:36:04

you are isolate

1:36:06

and you are simply using model.

1:36:08

dot encode documents.

1:36:11

You're encoding the documents part.

1:36:13

That's your document embedding's got

1:36:15

and this is the main function that we are using.

1:36:18

Upsert.

1:36:19

Upsert writes all the four parallel lists.

1:36:22

If I run the code,

1:36:24

unless I run the code, you will not follow.

1:36:26

If I run the code,

1:36:27

we basically, what we did,

1:36:29

we up up up.

1:36:31

You look, you know,

1:36:32

if I search IDs right now,

1:36:34

if I print IDs,

1:36:35

this is your 5 IDs are.

1:36:37

Doc 1, doc 2, doc 3, dock 2, do.

1:36:38

five.

1:36:39

This is.

1:36:40

This is.

1:36:41

All of you have with me.

1:36:42

Next, look.

1:36:43

So, we have you,

1:36:44

we have you,

1:36:45

we have a five IDs for separate

1:36:47

here.

1:36:48

You have here here,

1:36:49

this is your 5 metadata

1:36:50

is.

1:36:51

If I just see what I have done in the metadata

1:36:54

part of the code,

1:36:55

I have simply separated the 5 method.

1:36:57

We have a list made.

1:36:58

These are the list of the IDs,

1:37:00

the list of the metadata,

1:37:02

and finally the list of the documents,

1:37:04

the document texts.

1:37:06

So if I just go and run this part of the code,

1:37:08

this is nothing but the list of the document texts.

1:37:11

Okay?

1:37:12

This is the list of the text.

1:37:13

Document in the text.

1:37:14

This is the list of the text.

1:37:16

And we're on that we're encoding

1:37:17

now.

1:37:18

What is the code I'm writing?

1:37:19

I'm saying model.

1:37:20

Endcode documents.

1:37:22

It means these

1:37:23

individually one-by-one documents

1:37:25

embedding for.

1:37:26

Five documents,

1:37:27

five documents chunks,

1:37:28

it's embeddings,

1:37:30

and chunk

1:37:31

we'll make

1:37:32

make.

1:37:33

That's it.

1:37:34

straightforward.

1:37:35

This is all that we are doing right now.

1:37:37

And on.

1:37:38

What I will do, moment I use the absurd function,

1:37:41

that's all automatically stored

1:37:43

we'll.

1:37:44

We will verify what is stored right now.

1:37:46

Look, actually this is

1:37:48

actually syntax.

1:37:50

I'm just trying my best to explain to you what the syntax is doing,

1:37:52

but otherwise it is just syntax.

1:37:54

Simple syntax.

1:37:56

You have five chunks and you will simply use the absurd function.

1:37:59

You give the ID, you give the document,

1:38:01

you give the metadata, and you give the embeddings.

1:38:04

Okay?

1:38:06

So ID or

1:38:07

matter is optional.

1:38:09

It can not be, but documents will be definitely though.

1:38:13

Okay, and once the

1:38:15

Upsert is complete,

1:38:17

Upsert, it's a way,

1:38:19

it basically adds rows.

1:38:21

Think of it that way.

1:38:23

You can verify that there are total five rows

1:38:25

that were added in my vector Dube.

1:38:27

Vector D. In other words, in other words,

1:38:29

the collection we've made,

1:38:31

the collection by the name of support knowledge base,

1:38:34

there under five records added.

1:38:36

Now you have to see what?

1:38:38

What is that collection that we are referring to?

1:38:42

I'm seeing that a couple of you have raised and Remover has raised hand and

1:38:46

like sign us raised and you guys have any question, sorry.

1:38:51

You have raised and please please do ping me.

1:38:54

Please do message me.

1:38:55

Please do let me know on chat.

1:38:56

Remove one if you have a question and sign out if you have a question.

1:38:59

Please do let me know on chat.

1:39:01

Please do let me know on chat.

1:39:05

Um, actually, Anki is actually something that is not a very core JNI work.

1:39:12

That's why the data ingestion is,

1:39:14

that's how can be it.

1:39:15

It can be a PDF be,

1:39:16

document be, whatever.

1:39:18

So here we've only simulated here.

1:39:20

Now you'll say, sir, this data

1:39:21

can't, say,

1:39:22

can't any from,

1:39:23

you can't,

1:39:24

your data from PDF's from,

1:39:25

worddocs or

1:39:26

HTML website, web scraping

1:39:28

and can come

1:39:29

text file,

1:39:30

can,

1:39:31

and you're absolutely right.

1:39:32

And you're absolutely right,

1:39:33

this is the data engineering task, completely.

1:39:34

task completely.

1:39:35

It is typically not a Gen.

1:39:36

A.I task.

1:39:37

Your separate teams,

1:39:38

will,

1:39:39

data engineers will,

1:39:40

who will be made and

1:39:41

it will be given to you by data engineers.

1:39:42

Yeah, it will,

1:39:43

it will be given to you by data engineers.

1:39:45

Yeah, it will, it will, absolutely.

1:39:48

Jason be,

1:39:49

it will be.

1:39:50

It will be.

1:39:51

And it will take that, 100%.

1:39:54

This is the process of

1:39:56

taking the document or

1:39:59

we are not talking about one PDF.

1:40:01

Again, see, today's session I'm, you know,

1:40:03

I'm, you know, I have a limit, I cannot talk about everything because

1:40:07

we have a limit on the, we have two other classes on BRAG.

1:40:10

So, we'll you'll show you, exactly,

1:40:12

our use case is, I'mkech, we'll

1:40:14

how you can take multiple PDFs and you can actually build a system.

1:40:18

And that will be in our demo.

1:40:20

And it will take time, you will realize.

1:40:22

You can take a, you can take a folder with 50 PDFs,

1:40:26

50,000, but 100,000 pages will be there.

1:40:30

Now, you can take,

1:40:31

chunking in the time time.

1:40:32

time.

1:40:33

And it will take time.

1:40:34

It will take time.

1:40:35

You're absolutely too time.

1:40:36

Okay?

1:40:37

Okay.

1:40:38

Okay?

1:40:39

Yeah.

1:40:40

So,

1:40:42

our HTML in text,

1:40:44

basically, what are we talking about?

1:40:46

Here we are saying,

1:40:48

you have a PDF document

1:40:51

right?

1:40:52

You have a PDF document.

1:40:54

This you have a PDF document

1:40:56

that is spanning overall 100 pages.

1:41:00

And what you are doing is you're effectively

1:41:01

you're effectively dividing that entire document into the respective chunks.

1:41:06

Five chunks in five chunks

1:41:07

you've divided it.

1:41:08

That's the full document is, the full PDF of your document

1:41:11

have you,

1:41:12

you've got it,

1:41:13

so chunks are nothing but text.

1:41:16

Now, text PDFs can be

1:41:18

can come from,

1:41:19

text documents,

1:41:21

text and HTML can't,

1:41:22

they'll give an example to you.

1:41:24

Let us look at this, you know,

1:41:27

hugging face website only.

1:41:29

This is hugging face website.

1:41:30

This is a website.

1:41:31

If you right click on inspect,

1:41:33

if you right click on inspect,

1:41:34

if you click on inspect,

1:41:36

you go to the website's HTML content digs.

1:41:39

This is the HTML of the page.

1:41:42

Can you see?

1:41:43

Whatever you are seeing on the browser, this is nothing but HTML.

1:41:46

So this is what I meant by taking the data from HTML.

1:41:50

You have this website's data

1:41:52

can't. Ultimately,

1:41:54

this is typically not a genuine one.

1:41:56

So HTML is not something that's a different thing altogether.

1:41:59

But you're getting it right.

1:42:00

Like this is, Sangita.

1:42:02

This, this text is what is?

1:42:04

This, look.

1:42:05

Can you see?

1:42:06

In the following, you will find modules tuned.

1:42:08

If I expand this for you,

1:42:10

you will find modules tuned.

1:42:12

If I expand this for you,

1:42:14

you, if I expand the paragraph,

1:42:16

this in your here,

1:42:18

it will be here.

1:42:20

Right?

1:42:22

You know?

1:42:23

Can you see?

1:42:25

Can you see this?

1:42:26

In the following, you will find models

1:42:28

used for text.

1:42:29

So basically,

1:42:30

what you can do is you can literally go to any web page.

1:42:33

And if you know the hypertext markup language, HTML,

1:42:37

you can

1:42:38

HTML, you can write from website

1:42:40

data can take.

1:42:41

And what is that technique called?

1:42:44

That technique is called web scraping.

1:42:46

That is another thing altogether.

1:42:48

You can go to any web page

1:42:50

and you can fetch the information from a website.

1:42:53

And that's your chunk

1:42:54

being.

1:42:55

Now, this website is,

1:42:57

you're a chunk,

1:42:58

this is a chunk,

1:42:59

okay?

1:43:00

My point is that all of these can be chunks.

1:43:02

So we have simulated the demo right now

1:43:04

where I've already given you the five chunks.

1:43:06

But it can any of any of chunk one, chunk two, chunk three

1:43:09

chunk, chunk four, chunk five.

1:43:11

Chunks' corresponding IDs

1:43:13

and its corresponding merit data is here.

1:43:16

Next, what I've done,

1:43:18

I've created the Chroma database,

1:43:20

I've created the Chroma collection name,

1:43:21

which is the table name,

1:43:23

and I have basically went ahead

1:43:25

and done the embeddings for each and every respective chunk.

1:43:29

Chunk one, what is the embedding

1:43:30

chunk two, what is the embedding,

1:43:32

chunk three, what is the embedding,

1:43:34

all the five chunks are we have done the embeddings for those five chunks

1:43:39

and you can take a sneak peek into what those chunks really are,

1:43:42

what it contains right now.

1:43:44

Now, you'll see what I've been talking about on this file.

1:43:47

This is what is contained inside the chroma dp.

1:43:51

This is your chroma dp in the content.

1:43:53

Very simple, very simple.

1:43:55

So we basically,

1:43:57

what stored is in it in?

1:43:59

Documents.

1:44:00

is nothing but the list of these five chunks, chunk one, chunk two, chunk three, chunk four, chunk five.

1:44:04

Now, you see, there five chunks you have you

1:44:06

have stored, separated by comma,

1:44:09

okay?

1:44:10

That's five chunks' corresponding chunk embedding store.

1:44:15

This is, if I had to show you in a proper way,

1:44:18

this is embedding for chunk one,

1:44:20

here end here.

1:44:21

This is your array.

1:44:22

This is the embeddings for chunk one, comma,

1:44:25

embeddings for chunk two, embeddings for chunk three,

1:44:28

embeddings for chunk four, embeddings for chunk one,

1:44:29

embeddings for chunk one,

1:44:30

chunk fine.

1:44:31

Okay?

1:44:32

It's clear.

1:44:33

Everybody is clear.

1:44:34

Remember, each of these are vectors of 384 numbers.

1:44:37

Because we are taking each and every chunk and we are converting that to a vector of 384 numbers.

1:44:43

Because we have that mini, that LMV6 model, right?

1:44:47

Right?

1:44:48

Ids go and metadata, straight forward.

1:44:52

This is your chroma div in under.

1:44:54

Very simple, right.

1:44:56

Very simple.

1:44:57

So we've, vector divi been made.

1:44:59

chunks, embedding, and we have also seen what is actually contained in the vector dv.

1:45:06

So this is your vector ddb in this content will.

1:45:10

Okay? This is what is contained inside.

1:45:12

And now the last phase is where we will retrieve the data with similarity search.

1:45:19

Okay? So taking you back to the use case once again, whatever I explained, you know, before the break,

1:45:23

we have, distance formula, explained to you know,

1:45:26

use case what is?

1:45:27

E-commerce support bot is.

1:45:28

There are five questions.

1:45:30

There are.

1:45:32

Customers can return products or 5,000 processes.

1:45:34

This is like the Amazon manual.

1:45:36

You can't, this is an Amazon manual

1:45:39

is a miniature version.

1:45:41

This is like the Amazon manual right now that you are able to see.

1:45:44

Okay.

1:45:45

Now, when a user asks a question,

1:45:47

I want to return my shoes and get my money back.

1:45:51

Okay.

1:45:53

User to ask this question.

1:45:54

User will what will?

1:45:55

He will go to Amazon in the chatbot

1:45:57

bat bot and he will question

1:45:59

I want to return my shoes and get my money back.

1:46:02

He will simply go and he or she will go there and type

1:46:05

type and enter.

1:46:06

What will.

1:46:07

This is what is called the query.

1:46:10

This is your query.

1:46:12

This is your query.

1:46:14

This concept is very important.

1:46:15

Code is,

1:46:17

two line of code,

1:46:18

collab,

1:46:19

Gemini is.

1:46:20

I think the coding part is the easiest part.

1:46:22

But the concept once it is clear,

1:46:24

you will never forget it ever again.

1:46:26

Like the concept clear

1:46:27

you can never be able if you remember with my examples.

1:46:30

So this is your query.

1:46:32

Okay, this is your query.

1:46:35

End user

1:46:36

this is a question in Amazon's website.

1:46:39

So query is this, right?

1:46:42

Remember, machines don't understand this.

1:46:44

So machines will convert that into what?

1:46:47

query embedding.

1:46:49

You will do the same model.

1:46:51

You will do the same model.

1:46:53

code, which we're here here here here

1:46:55

model.

1:46:56

This is my query.

1:46:57

I want to return my shoes and get my money back.

1:47:00

So we are doing model.

1:47:01

The same embedding model I'm using,

1:47:04

you know, V6, version 6 model

1:47:08

model generally are.

1:47:09

We are using the same mini LM model.

1:47:11

And we are effectively doing model.

1:47:14

And we are creating query embedding.

1:47:16

So we are creating query embedding.

1:47:20

query embedding created.

1:47:27

Next, what I will do?

1:47:30

I will go back and I will now, based on the user questions,

1:47:35

remember, we already discussed right?

1:47:38

Remember, we already have a vector db, right?

1:47:41

Vector db is.

1:47:42

Vector db.

1:47:43

There are our five chunks

1:47:45

C1, C2, C3, C4, C5, C5.

1:47:49

C-fine.

1:47:50

It's corresponding IDs,

1:47:51

and it's corresponding text and its corresponding embeddings are.

1:47:54

Now, all that we have to do is, you all remember, right?

1:47:56

We are going to go and to the vector DB and retrieve,

1:48:00

we're going to retrieve the top three similar chunks.

1:48:04

Which of our five EPECUs do you think will be the closest mathematical match?

1:48:08

This is the user.

1:48:10

The user has the question

1:48:12

that I want to return my shoes and get my money back.

1:48:15

That the five chunks are,

1:48:16

the five of Amazon manuals of chunk is,

1:48:19

that five chunks may say which of the chunks answer this question the best possible way?

1:48:23

Why?

1:48:24

to do it.

1:48:25

If the user to answer then, so based on the user question,

1:48:28

based on the context of the user question, based on the embedding,

1:48:31

based on the context of the user question,

1:48:33

can we find out what the similar chunks are?

1:48:36

And that is what we are trying to retrieve using this part of the code.

1:48:40

Now, look, the concept and the code is beautifully related.

1:48:43

So we'll say collection.

1:48:45

Query, query Embedding 1.

1:48:48

This is your query is a query is.

1:48:49

and please get me the top three results by meaning.

1:48:53

What is that?

1:48:55

When semantics search in the vector table,

1:48:57

no, no, no, no, that metadata, actually, it's not 100% mandatory.

1:49:01

No, no, that is a slightly advanced concept, Tunkin.

1:49:05

So if you asked, I can, I can, yeah.

1:49:08

So basically it is used for some amount of,

1:49:11

some amount of, like, hybrid search.

1:49:14

You can exact search be and semantic search

1:49:17

can.

1:49:18

For that for that for metadata use.

1:49:19

Otherwise, this demo for me need to be needed to

1:49:21

just to clarify.

1:49:23

And indexing and all are internally done, Garima.

1:49:25

That is also internally done.

1:49:27

During retrieval, ChromaDB uses indexing,

1:49:30

yeah, that internally you can do.

1:49:32

So vector database, this is the management of a vector DB

1:49:38

is very similar to how

1:49:40

is very similar to how a normal database system is managed.

1:49:44

You're all indexing,

1:49:46

everything, everything.

1:49:47

Because retrieval is a very expensive operation.

1:49:49

Look, here there are five chunks.

1:49:51

It can be 5 million chunks.

1:49:53

So can you imagine how time-consuming that operation will be?

1:49:58

You have a query vector.

1:50:00

You have a query vector.

1:50:02

And you go to that 5 million values compare to

1:50:05

that kind of close is.

1:50:07

And then you have to 3 retrieve it.

1:50:09

It's an extremely difficult, extremely time-consuming operation.

1:50:13

And computer science, we say,

1:50:14

sorting is the most complex operation.

1:50:18

So this is going to take a lot of time.

1:50:21

Anyways, so we will return the top three results.

1:50:24

That means based on the query embedding,

1:50:27

we'll try to find out which are the top three chunk embeddings.

1:50:31

Okay?

1:50:32

And Ali, two lists,

1:50:35

two lists is just converting to a list.

1:50:37

Two list is just converting it to a list.

1:50:40

They say 2 underscore numbai

1:50:42

is 2 underscore pundas.

1:50:43

2 underscore list.

1:50:44

Two list is just converting it to a list, okay?

1:50:47

Yeah.

1:50:48

Okay, so this is the same thing we have demonstrated right now.

1:50:51

Okay?

1:50:52

So, so we'll go.

1:50:53

And we'll show you that results what is.

1:50:56

I think I want to return my shoes and get my money back.

1:50:59

So this answer is obvious.

1:51:01

What will?

1:51:02

But let's see.

1:51:03

Very interesting.

1:51:04

You can take a look at it.

1:51:05

You can take a look at it.

1:51:06

You can see.

1:51:07

If you ask this question, I want to return my shoes and get my money back.

1:51:11

So the closest match, the rank one, the closest match is,

1:51:14

document number two, chunk number two.

1:51:16

That means refunds are processed within five to seven.

1:51:18

talking days.

1:51:19

So the banda is, I want to get my money back.

1:51:21

Now, the money will, but it usually takes this much time.

1:51:23

See, semantically, the system understands that based on the user question, the nearest

1:51:29

matches this answer.

1:51:30

This is beautiful, actually.

1:51:31

And this is very powerful stuff.

1:51:33

Once you put this in the context of a larger system, this is extremely powerful stuff.

1:51:37

I'm here here a very small demo, that

1:51:40

five sample chunks like you can actually start to see.

1:51:43

Customers can return products within 30 days of delivery.

1:51:47

This is not that related.

1:51:49

Actually, this is not that related.

1:51:52

An order sub of your 4, 9, 10,000, qualify for free.

1:51:54

Shipping is not a question in.

1:51:56

So if customer is the closest match is basically this.

1:52:01

You can see this one.

1:52:03

And you can see this one.

1:52:04

And you can see this one.

1:52:05

Now here results equal to 1,

1:52:06

you, your closest match will get.

1:52:08

You, you see, closest match will.

1:52:10

Actually, we need the closest match.

1:52:11

Actually, we need the first answer.

1:52:13

We need.

1:52:14

I only want one top answer.

1:52:16

And you can actually start to see.

1:52:17

what that top answer is.

1:52:19

So based on the user query,

1:52:20

can you go back and look at all the five chunks

1:52:22

and get me what is the top chunk?

1:52:24

Top one chunk of the end results

1:52:26

can control can control and this is the top chunk.

1:52:29

Okay?

1:52:30

And you can see index zero, best semantic match

1:52:33

and distance, the lower it is, the closer it is.

1:52:36

Or distance,

1:52:37

I have you explained in coordinate axis,

1:52:39

distance.

1:52:40

How far is the query embedding from the chunk embedding?

1:52:43

So the closer is the distance,

1:52:45

the more similar it is.

1:52:46

the most similar it is.

1:52:48

Best case is.

1:52:49

Best case is that query embedding or chunk embedding

1:52:52

and chunk embedding, that's same to same.

1:52:53

That will never exactly match.

1:52:55

But they can be very similar.

1:52:58

So remember, the lower the distance, the closer it is.

1:53:03

That is one way to look at it in two to two.

1:53:07

So let us try a completely different topic to see if it correctly pulls up.

1:53:13

This is fun actually.

1:53:15

Actually, the other example, how do I change my login password?

1:53:18

So it's an account-related question.

1:53:20

So I think logically people remember there were five chunks I had.

1:53:25

Again, I'm telling you, I'm repeating again,

1:53:27

I'm repeating again.

1:53:28

I have this demo for five chunks here.

1:53:30

But no need in a real world scenario,

1:53:32

which we'll, we'll look at the two sessions we'll

1:53:34

we'll take a PDF file

1:53:36

we'll show this whole thing.

1:53:38

Same-to-s-s-support-support-to-support-support-support use that we'll

1:53:40

take the PDF file.

1:53:41

Okay?

1:53:42

So if I say, how do I change my login password?

1:53:44

password we will say model dot input and you can see again i'm going to retrieve the top one result and

1:53:51

based on the user question the top retrieved result is you can reset your password from the account

1:53:58

settings page well well this is amazing this is amazing so you can uh so

1:54:03

you're change kind of change

1:54:06

uh how do i i i have forgot my i have forgotten i have forgotten i have forgotten

1:54:14

my, yeah, I can try anything.

1:54:17

You know,

1:54:18

it's not that we have these demos

1:54:20

made, but no,

1:54:21

this works like magic.

1:54:25

This works like magic actually.

1:54:26

It's literally it works like magic.

1:54:27

You can take any sentence

1:54:28

and the machine will

1:54:30

internally, semantically

1:54:32

find out the embeddings of that sentence

1:54:34

and that those numbers

1:54:36

somehow tell you something about the sentence.

1:54:39

And those related answers

1:54:41

what are you? You can't tell you, you

1:54:41

what I've forgotten my login password.

1:54:44

Ideally,

1:54:46

its context or its context same.

1:54:48

So I should get the same answer.

1:54:51

If what we are discussing is aligned to all of you,

1:54:54

I should get the same answer.

1:54:55

Okay?

1:54:56

I'm getting the same answer.

1:54:58

So query embedding is.

1:55:00

Five chunk embeddings have.

1:55:02

Based on this question,

1:55:03

model has figured out what is the best answer.

1:55:06

Okay?

1:55:07

Everyone's clear.

1:55:09

Some other question?

1:55:10

Somebody, try out a sample query.

1:55:14

Try out a sample query.

1:55:14

Okay, we can do a

1:55:17

we can do a fun exercise.

1:55:19

So, so we can do one, again, one other, we have

1:55:23

you have five categories, right?

1:55:24

Customers, this, this,

1:55:26

you have five categories.

1:55:27

This basis,

1:55:28

on one other question you want the chatbot,

1:55:31

you want to ask to the chatbot?

1:55:33

See, this is also very important,

1:55:37

model testing.

1:55:38

Amazon, when your chatbot

1:55:39

deploy in the real world,

1:55:41

Amazon has to know

1:55:42

that,

1:55:43

you know,

1:55:44

if you can say, then you will never build a real world application without testing.

1:55:51

So what we are doing right now is basically testing.

1:55:54

In a very small scale, we have an application

1:55:55

and we are basically doing something called testing, that's it.

1:55:59

So can somebody give me a sample query?

1:56:01

Multilingual, there are other, other models that are, you know,

1:56:05

so you need to choose the right kind of model for that.

1:56:10

This model is not the best multilingual model, I would say.

1:56:13

If you're Hindi about talking to,

1:56:15

this model, India, like, can't.

1:56:17

Basic token support they have, but, you know,

1:56:20

only if you use a multilingual model.

1:56:23

This all mini-LM we use here, this is only for English.

1:56:26

This all mini-LM, L6V2, is mainly good for English.

1:56:29

But if you're looking for multilingual support

1:56:32

for languages like Hindi, Bengali,

1:56:34

then you will have to use a different embedding model.

1:56:36

Everything depends on the embedding model.

1:56:38

All the magic is with respect to the, you know,

1:56:42

you know the embedding model okay so you can use some multilingual models so if you if you

1:56:50

want some examples from me, I have some

1:56:52

you can try these two.

1:56:54

Now sentence transformers Google for and you can maybe try some of these options.

1:57:00

These are multilingual models that perform better.

1:57:02

Whatever tokens you have, even if you have tokens in other languages,

1:57:06

language specific models are.

1:57:08

So it all depends on the embeddings.

1:57:09

Now if you can't text do.

1:57:11

Okay, computer accept it.

1:57:12

The computer has everything is.

1:57:14

But they can't embedding fix and they can't.

1:57:16

Because he doesn't know that tokens.

1:57:18

Okay.

1:57:19

Make sense.

1:57:20

Order more than 499 and express delivery.

1:57:24

So again, as I said, very good, very good.

1:57:27

Excellent question, Unkid.

1:57:29

Let's try Unkid's question.

1:57:31

Garima has also asked a question.

1:57:33

So first let me go for Unkid's question.

1:57:35

Ankeet, I asked, asked,

1:57:37

Okay, Unkech has only asked to host and panel.

1:57:40

By the way, I'm just typing.

1:57:41

question.

1:57:42

Anki's question is this.

1:57:43

Order is more than 4-910 express delivery.

1:57:46

So the answer to that question should be this.

1:57:48

I am expecting the machine to give this answer.

1:57:51

If we asked the machine should answer this.

1:57:54

Okay?

1:57:55

So let us see if my system is working.

1:57:58

System is working.

1:57:59

The system is coming or not, let's see.

1:58:02

Let us see.

1:58:04

So this, this is sample demos.

1:58:08

So this is a sample demos.

1:58:09

I'll try to create some space

1:58:12

so that people are clear that these are from sample demos we are doing.

1:58:17

So let me quickly copy Unkid's query.

1:58:21

And here it is,

1:58:24

Hairly worry,

1:58:27

here, okay?

1:58:29

This is your user query.

1:58:32

Let's run the code and you'll be able to see

1:58:34

model has answered.

1:58:37

That means based on the query, the query,

1:58:38

the query embedding.

1:58:39

The similar chunk embedding is basically this.

1:58:42

So here it's retrieved answer to say.

1:58:44

Okay.

1:58:45

Correct.

1:58:46

I want to change my login credential.

1:58:47

So Garima, this is again very similar to the,

1:58:49

very similar to the password one.

1:58:51

Absolutely.

1:58:52

So if you ask this question,

1:58:53

I want to change my login credentials.

1:58:55

If I go and ask this question,

1:58:57

okay, the model will go and give this answer.

1:59:00

You can reset it from the account settings page.

1:59:03

Okay?

1:59:04

This is the way how it will basically work out.

1:59:06

And this is very interesting.

1:59:08

This is the other thing.

1:59:09

we have, you know, we've kind of seen in real world scenarios and chatpots and all that.

1:59:13

And most of us are pretty amazed at times.

1:59:15

And you can see, we have here we did that.

1:59:17

We have there we did that, that we did, that we did,

1:59:19

we have spelling mistake here,

1:59:21

Jaunpushka.

1:59:22

I want to change my login.

1:59:24

Yeah, I want to change.

1:59:27

Now, now, look, here we have

1:59:28

grammar be wronged, spelling,

1:59:30

and you'll be surprised to see.

1:59:32

You'll be surprised to see the machine is still

1:59:35

contextually giving the same answers.

1:59:37

That's the magic of embedding.

1:59:39

That is what, and that is the reason why even when you make mistakes, spelling mistakes in chat GPT,

1:59:44

you know, guys, it is not as if chat GPT is correcting it.

1:59:48

It correct not, everything is based on embeddings.

1:59:51

Because internally, when it's the process, that all, those numbers in convert

1:59:55

so even when you type some incorrect things like, I want change, grammar,

1:59:59

grammar is not, spelling mistake is not, I want to change my login.

2:0:03

See, if you're all of everything, then it's a different thing.

2:0:07

But here, it's just to understand.

2:0:08

I mean it understood intuitively, I want to change my,

2:0:11

well, that the keywords like,

2:0:13

that's all the magic is about embeddings.

2:0:16

It is looking at the embeddings and it is still able to figure out,

2:0:19

that similar things.

2:0:22

What do you mean?

2:0:24

What about prime member?

2:0:26

Ah, is that a, is that a question, Razzie?

2:0:29

You want to ask that?

2:0:30

You want me to ask that?

2:0:31

What about prime?

2:0:32

I didn't get that.

2:0:33

So is that your question?

2:0:35

Is that the chatbot's question?

2:0:37

So I, I, I, I.

2:0:38

I missed the context.

2:0:41

Prime?

2:0:42

Prime is there.

2:0:43

I think, you know?

2:0:45

Yes, what is it?

2:0:47

I'm sorry, I missed that.

2:0:48

You want me to ask this to the chatbot?

2:0:50

I think Prime is not.

2:0:52

Prime is not.

2:0:53

That's very interesting, actually.

2:0:55

Prime is not there.

2:0:57

And just for people, Rajdip is asking,

2:1:00

what about Prime member then?

2:1:02

So Rajdip is asking a very, very interesting.

2:1:05

Rajiv has actually an error condition of question

2:1:07

question, which is my next topic is.

2:1:09

Very good.

2:1:10

So Rajit has a general question

2:1:11

asked, what about prime member then?

2:1:13

Yeah, exactly.

2:1:15

Amit, your question is exactly what

2:1:17

Rajdip is asking.

2:1:19

So he asked a question,

2:1:21

exactly.

2:1:22

Okay, if we ask irrelevant questions, exactly.

2:1:25

See, the way this system is going to handle it is,

2:1:29

it is, it is still written answers.

2:1:31

But this is what actually my next topic was about,

2:1:35

when ranking looks wrong.

2:1:36

wrong.

2:1:38

You will ask, that he will

2:1:40

ask you, but the distance will be extremely high for this.

2:1:42

It is still returning the chunks, right?

2:1:44

It is still returning the chunks, right?

2:1:48

Now here, I didn't actually, but you

2:1:50

distance here print can't. The distance will be very high.

2:1:54

It will still return the top match.

2:1:56

Because what is it returning? It is returning the top match.

2:1:59

You have, you have questions.

2:2:01

You have five chunks.

2:2:03

Those five chunks were, whichever chunk is the closest.

2:2:05

the closest. That will be returned.

2:2:08

Closes, it can be very far away, but still it is the nearest match.

2:2:11

It is still be returned.

2:2:13

So very good question.

2:2:15

A lot of times what will happen, if a user asks the question about something,

2:2:20

we don't have in our database.

2:2:22

Vector databases don't reply, I don't know.

2:2:25

This option is.

2:2:26

Vector databases cannot reply, I don't know.

2:2:29

They return the mathematically closest vector even if it is completely

2:2:34

it is completely unhelpful. So here I've explained this part.

2:2:37

If you ask a query,

2:2:40

and that query doesn't have a matching chunk or doesn't even,

2:2:44

it's not even related to the chunk,

2:2:46

so what can do it?

2:2:47

It is still written to the...

2:2:49

I mean, I think Rajleaf still asked a relevant question.

2:2:53

So I'm here here here

2:2:54

if you say, if you say,

2:2:57

when did man land on the moon?

2:3:01

I mean, if you look at it, my question,

2:3:03

If you look at it, my question, the vector div will not complain.

2:3:07

But my query embedding, it is trying to see what is the, you know,

2:3:11

what is the closest jump embedding?

2:3:13

The closest, that's the closest to be,

2:3:15

this closest state.

2:3:16

You know,

2:3:17

how much retrieve, it will,

2:3:18

but then you can, you have to see that.

2:3:20

Sometimes these will not make any sense.

2:3:23

So, so the, so the, the onus is on you.

2:3:28

The on you.

2:3:30

The onus is on you.

2:3:31

The responsibility is on you.

2:3:32

it is on you.

2:3:33

When we come to the next session, when we come to the next session,

2:3:36

when we come to the next session,

2:3:40

the owners will be on you to ensure that you handle these specific cases.

2:3:44

You have to handle these specific cases.

2:3:46

Ideally, user's a question,

2:3:48

users do all the way of questions.

2:3:50

You have to ensure, you will have to test your application,

2:3:53

and you will have to ensure that if a user asks the question

2:3:57

that is not present in my, you know, a relevant chunks,

2:4:01

then the system should answer.

2:4:02

I don't know.

2:4:03

But the vector db, whatever is the topic for today,

2:4:06

the vector db as such will not answer, I don't know.

2:4:08

Vector db, your similar chance will return.

2:4:11

Okay?

2:4:12

Okay?

2:4:13

Yeah.

2:4:14

You can't, you can't.

2:4:16

You can this condition

2:4:17

correct.

2:4:18

Absolutely.

2:4:19

But again, Karima, a very good point you raise.

2:4:22

But the thing is,

2:4:23

but the fact is,

2:4:24

vector db internally not, but you

2:4:25

you can,

2:4:26

application there, I'm,

2:4:27

your own own own logic,

2:4:28

you can do.

2:4:29

So, basically,

2:4:30

I think, people are

2:4:32

wondering what I'm saying. So you can actually write your own logic.

2:4:35

You can say if the similarity value is greater than this,

2:4:38

if it is less than this,

2:4:40

then we go back we return

2:4:41

again.

2:4:42

If similarity value

2:4:43

very,

2:4:44

um,

2:4:45

I don't know.

2:4:46

So that is the thing.

2:4:47

So that is the thing.

2:4:50

So very interesting, but this is something we wanted to kind of

2:4:55

break it up in a small section for you to help you understand.

2:4:59

Okay.

2:5:02

Excuse me.

2:5:17

So this is another very nice diagram,

2:5:20

which I've curated.

2:5:22

So these are only something that we only curate as part of the content team.

2:5:27

So we have given this diagram for you.

2:5:28

Very interesting.

2:5:29

Whatever I've explained to you,

2:5:30

but I think sometimes it just helps when you see

2:5:32

these beautiful visuals.

2:5:34

The visuals are very nicely curated.

2:5:36

You can look at it.

2:5:37

This is also very nicely done.

2:5:38

Top-K results ranking are how we can.

2:5:40

So whatever I explained to you, very beautifully

2:5:43

is summarized in this particular diagram.

2:5:45

So you have a user query.

2:5:47

It is.

2:5:48

This is your documents collection.

2:5:50

It's a PDF.

2:5:52

And if you see these are all the chunks that you have right now,

2:5:55

document once they take a document N.

2:5:57

So you send it to the retriever.

2:5:59

User query, retriever.

2:6:01

And you find you find it.

2:6:02

out what are the relevant chunks.

2:6:05

So what we do is we take the chunk embedding,

2:6:08

a query embedding, and we compare with the chunk embedding,

2:6:10

and we find out similarity scores.

2:6:12

And whichever similarity sports are the highest,

2:6:15

0.9 to 0.87.

2:6:17

We will pick up the top 5 documents

2:6:19

whose similarity scores are the highest

2:6:23

and we will retrieve those top 5 documents.

2:6:26

So that's the way how we will go about it.

2:6:31

I hope everybody is clear.

2:6:33

So this is pretty much, it's a very easy session that way, comparatively.

2:6:36

So this was the key takeaways from today, basically.

2:6:40

So I think, you know, I think straightforward, basically.

2:6:43

So ChromaDB and embedding is the main agenda for today.

2:6:47

And as I said, we have broken down the session into multiple phases.

2:6:51

So I think this is pretty much what we are seeing here.

2:6:54

Ankit has asked a question.

2:6:55

I will quickly take up Ankit's question.

2:6:58

Sir, grounding thing will never be.

2:7:01

part of what is that?

2:7:04

We'll never be part of vector db processing.

2:7:08

It will always return the result.

2:7:11

And can't say, yeah, yeah, yeah,

2:7:12

vector db may go, correct.

2:7:13

That's basically right.

2:7:15

A vector dv only returns the nearest matches.

2:7:17

I don't know come from the application project.

2:7:20

Correct.

2:7:20

Vector db never never will say, I don't know.

2:7:22

Vector db will always give it a similar match.

2:7:25

Very question.

2:7:26

Question, what?

2:7:27

Vector db said, you're saying,

2:7:28

you're saying, b, five similar chunks return.

2:7:31

vector db there.

2:7:32

Now, that chunks, that's, that's application's logic,

2:7:35

that you're you want to show to you?

2:7:37

Vector db will return the chunks to you.

2:7:39

Now it is up to you whether those chunks are similar,

2:7:42

that you are similar, that you're using the user to do you.

2:7:44

Okay, got it?

2:7:48

Both that answers your question, okay?

2:7:53

Great, great.

2:7:55

I will take up some questions.

2:7:56

We have time for some questions here.

2:7:58

But just to summarize the conversation, guys.

2:8:01

Again, as I said, it was a very easy session today.

2:8:04

So we only had majorly the four areas to understand embeddings.

2:8:08

We understood how to create embeddings for a sample.

2:8:11

This is we've seen in the last session maybe for some embedding demo.

2:8:14

But the main agenda for today was embeddings and how to create the embeddings.

2:8:18

We also saw how to store vectors in chroma.

2:8:21

Chroma is the main thing that we are using for the session and the curriculum.

2:8:25

And also finally, run a top case semantic search query.

2:8:28

So we were able to ask a question.

2:8:31

and we were able to retrieve the top three at the top five similar results.

2:8:35

So these were the main discussion points for the session.

2:8:38

And this very beautifully follows through in the next session.

2:8:42

Aglajo class is, you can take a look at it.

2:8:48

Okay, I think this is, yeah, we will see this.

2:8:52

You see the next session, which is again, very interesting.

2:8:55

You can take a look at it.

2:8:56

We are in the embedding vector search.

2:8:58

The other session will be on chunking.

2:9:00

So we are.

2:9:01

We have two more classes on Rags left down.

2:9:03

And in these two sessions, we will get into a little bit more in detail.

2:9:06

Here we have we will be seen.

2:9:11

So we'll actually load a document.

2:9:12

We'll do the chunking.

2:9:14

So the first part, we'll today we have you made sample chunks.

2:9:19

So we'll more detail in the next class.

2:9:22

That chunking up how are you?

2:9:24

Today we're chunks manually gave you.

2:9:25

Five chunks.

2:9:26

But next session will be more about that document preparation.

2:9:30

People were asking, like,

2:9:31

are, is a data engineering task too.

2:9:33

That is what we will see.

2:9:34

And finally, the last session will be about a complete rag bike line.

2:9:38

So this is, this is how we will be seeing these pieces.

2:9:41

Okay.

2:9:43

So I think, I think, see, Ankit, just to clarify, do not confuse it with the larger machine learning piece.

2:9:50

Machine learning is, again, a very different thing, what we have seen in the last course.

2:9:54

So these are not very much related to ML.

2:9:58

These are completely different generative AI topics.

2:10:00

Don't confuse if it's supervised or unsupervised.

2:10:03

It's neither.

2:10:04

It's neither.

2:10:05

If your question is, is it just, is it supervised?

2:10:08

Is it unsupervised?

2:10:09

I would say it is neither.

2:10:10

It is neither.

2:10:11

It is our Gen.

2:10:11

A.I.

2:10:12

topics.

2:10:13

You know, you don't really, got it?

2:10:15

Okay.

2:10:15

Don't confuse with what piece he saw in the last course.

2:10:19

Okay.

2:10:22

All right.

2:10:23

Great.

2:10:23

Any other questions, guys?

2:10:25

Any other questions?

2:10:27

I hope all of you are clear.

2:10:29

the contents for the session are already uploaded.

2:10:32

This is the demo file that we saw.

2:10:34

And these session notes, this is something that I have curated with the content team.

2:10:39

So these session notes is something, it will be uploaded to your, to your LMS by tomorrow.

2:10:44

Okay?

2:10:44

So by tomorrow, you should be able to see this in your learning material.

2:10:47

Okay?

2:10:49

Great.

2:10:49

Excellent.

2:10:50

Thank you.

2:10:51

Thank you, all of you.

2:10:52

In that case, I will hand it over to Arshita.

2:10:54

And good night, all of you.

2:10:57

We are having an early closure.

2:10:59

good on time yeah so I think it would have been conveyed to you that we have

2:11:04

advanced the session timings a little so some sessions might go till a little

2:11:09

no but I think again we'll try our best to you know take up do the classes on time

2:11:15

start on time and on time but yeah I think so we also adjusted the curriculum

2:11:21

significantly based on that we've added more classes okay so so don't think

2:11:27

that, you know, because the classes are like small, so we have added many sessions.

2:11:31

We've added more sessions also.

2:11:33

So, uh, so, uh, I gave we have many sessions added.

2:11:36

So instead of, I think, I think what we felt was, instead of having very long classes,

2:11:41

I remember in the initial phases, I think I used to do till 11 and like, it used to be very long.

2:11:47

But then what we realized was, that let's not have very long sessions.

2:11:51

Let's not have very long sessions.

2:11:52

So we, uh, we, the three-hant-hour class is, we, we're just to do it, we're going to split

2:11:56

currently. So upcoming contents, what we have done is we have split it into multiple sessions.

2:12:00

So we'll have multiple shorter sessions instead of having a one view session.

2:12:05

Okay. And we also realize that people were not getting time to have dinner and all that. So I think,

2:12:09

I think keeping your interest in mind, we have, we have really tried to redesign, you know,

2:12:15

our experience here. Yeah. Thank you so much, guys. I will handle it over to Arsita and take care

2:12:21

on of you. Good night. I'll see you in the next session.

2:12:26

What's that?

2:12:29

Oh, okay, sure. Yeah. So I will enable the poll, guys.

2:12:35

Yeah, sure. Sure. Sure. I'll launch. Yeah, I'll launch the phone.

2:12:40

Call if you can just take a moment to fill up the feedback phone. And after that, Arsita will conduct the

2:12:46

minty meter quiz for you, okay? Okay.

2:12:53

Thank you very much, sir, for the wonderful session.

2:12:56

Thank you for the 90 meter quiz. You can use this code to join in.

2:13:04

We will start in about two or three minutes once you are done with the pool.

2:13:26

Thank you.

2:13:56

Thank you.

2:14:26

Thank you.

2:14:56

Thank you.

2:15:26

All right, let's start with the quiz.

2:15:34

Here is the first.

2:15:56

Semantic vectors, SQL tables, word counts or audio files.

2:16:26

What does a higher similarity score usually mean?

2:16:33

Less relevant, slower query, more similar, more similar, or bigger file size?

2:16:56

more similar, right? It is kind of the same thing.

2:17:26

Yes, everyone is correct.

2:17:34

We read about chroma today.

2:17:38

Fourth question.

2:17:42

What is semantic search?

2:17:47

What is semantic search looking for?

2:17:53

exact spelling only, meaning based matches or random results.

2:18:23

Final question of the day?

2:18:36

What does top K search return?

2:18:41

The newest chunks, the top matching chunks, all stored chunks, or the longest chunks.

2:18:53

Correct. It is the top matching chunks. Let's look at the leader board now.