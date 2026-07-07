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

Thank you

20:24

Thank you

20:54

Thank you

20:56

Thank you

20:58

Thank you

21:00

Thank you

21:02

Thank you

21:04

Thank you

21:06

Thank you

21:08

Thank you

21:10

Thank you

21:12

Thank you.

21:42

Good morning. Good evening everybody. Good evening. We will just be starting on in a few minutes.

21:56

Wait for all to join in. Just a few minutes we'll start.

22:12

Thank you.

22:42

Okay.

23:12

Good evening, guys.

23:42

Thank you.

24:12

All right, folks. Let's start on. Let's begin the session here. And so just to just to take you through what we have done so far and how we have based our session so far.

24:34

So we are currently in the current module until the previous session we have discussed about

24:42

about rags. That was the very last session that we did. We walked through the process of what rags are and overall in this module until now we have covered the concepts of how to write a prompt, how to make an API call. We have discussed about the general ecosystem, you know, what is a closed model, what is an open source model. How do we use Olama? There was a session we had an Olamma. We talked about Olamma, how to use it. We talked about the concept.

25:12

concept of JSON API call. What is an API call? So we went over, you know, these kinds of concepts. And the last session was specifically related to the rag foundations. We saw the entire life cycle of a retrieval augmented generation. I will very quickly recap that also for you. Because I told you this is the second session of rags. We have another two more sessions on rags. It is done over four classes. So today is our second session on rags. And today the focus will be on embeddings and vector search.

25:42

we already know this from last week. I know. We already saw this idea in the last session. But we will once again go over it. We will once again see this in a bit more detail. And we will specifically focus on the vector DB part a little bit more in detail in today session. So that is the main objective. Right. So that is what we will try to do. And overall, I think after we understand this well, we will be able to figure out how we are able to store the chance in a vector DB. What are the embeddings and all that we'll be able to see.

26:12

And obviously, after we complete this, the upcoming modules, we have rags, agents, it continues. And the next module, we have agentic systems that we will see in much more detail.

26:22

This is just to give you a very, very brief mental mind map in terms of where we stand in the classes so far.

26:29

Now, going back to the rag discussion that we had in the last session, so before I start on with today's flow, I wanted to very quickly summarize all that we saw.

26:42

in last week session in terms of what retrieval augmented generation is and some of the basic ideas behind it. Let us see that in action.

27:07

And all of you remember, this was the main. This was the main.

27:12

diagram that I used as a reference for the session. And I'm going to very quickly walk you through

27:17

this particular diagram and context in terms of what rags are. What is the workflow of a rag?

27:23

Okay. So all of you give it a glance once. I'm sure everybody is able to remember it. We talked about

27:28

those beautiful analogies of the library and all that. I won't repeat that entire thing, but I think

27:32

this diagram pretty much summarizes everything that we talked about in that two hour session

27:37

last week. Okay. So all of you just take one minute.

27:42

to absorb this, maybe recall some of the concepts that we did and I'll again repeat this

27:47

for you. And then we will start with our mistake. Okay. Yes. Can you share the Google Drive link

27:53

please? Mahmad, I think this is the, yeah, there's a cohort link we have so that I shared long

28:01

back. Yeah, can one of you share our cohort link like 2603? I can I can do that no problem.

28:09

This is the yeah, this is the cohort.

28:12

link I think. I think this is the right one. You can use this one, please. So this is the entire

28:20

2603 batch. Whatever I've done, all the classes that have taken, organized by dates, everything is

28:25

present in this thing. And today we are in 6th of July. So 6th of July, you will see this one. This is the

28:35

demo file which we will cover shortly, right? Okay, yeah, sure. All right, everybody please

28:41

So, please, yeah, I'm just going to give it a minute for all of you.

28:44

Please take a minute. I will again take you through it.

29:11

Thank you.

29:41

So it all.

30:11

concept of, it all started with the concept of a document and we talked about this,

30:16

this beautiful use case of a, let's say, an HR PDF files. Imagine we are starting out with a

30:23

HR PDF file, or an HR document that is spanning overall 100 pages. So let's say that

30:35

H.R. PDF pages. And the first thing that you do is spanning, you, you,

30:40

load that PDF and you do chunking. Why we do chunking? Because it's very hard to process

30:48

the entire file in one book. And remember, it's not always that we are talking about one file.

30:53

We are talking about several tens of thousands of files. Right. So just to clarify, it's not just

30:59

that we are talking about a single file. In reality, there could be several tens of thousands

31:04

of files we can, you know, we are talking about. So it's very hard to process the entire data

31:10

in one go. So what we do instead is we go and do a chunking. So we take the data and

31:17

we divide the data into chunks. Okay. So here also you can see we take the entire data and we

31:24

divide the data into chunks. We divide the PDF into chunks. And we can apply different different types

31:28

of chunking techniques. And the specific type of chunking technique that we are using right now is

31:35

let's say page wise chunking. And it's up to you. Like we can debate about

31:40

what is the best way to do it and all that. That's up to you. We can, there are many different

31:44

ways we can do chunking. So yeah, but the specific type of chunking here, let's say we are doing

31:48

is page wise chunking. So every page is like a chunk. Okay. So C1, C2 and C00. As we come to the hands

31:57

on, we will discuss other kinds of chunkers also later on. But this is just for an analogy I do. So every

32:02

chunk is like a page. And the chunks basically consists of text. You have taken that massive amount of

32:07

PDF data spanning 100 pages and you have broken it into 100 sections, 100 small chunks.

32:15

But remember, machines do not process text. Machines don't understand text data. So what has to

32:21

happen is you need to take this chunks and you need to eventually convert these chunks into what

32:26

is called embeddings. So we need to create what we refer to as chunk embeddings. So we have to take the

32:31

documents. We have to convert them into corresponding chunks and then take each and every one of those

32:37

corresponding chunks and convert them into embeddings. So we will have chunk one.

32:45

What are the embeddings for chunk one? Chunk two, what are the embeddings for chunk two?

32:49

Chunk three, what are the embeddings for chunk two? So we look at each and every one of the

32:52

respective chunks and we'll try to find out what are the embeddings that we have for each and every one of

33:00

those respective chunks. Okay. So the embeddings and this is an embedding model that we will use for this

33:04

purpose. Because machines don't understand text. You have to take the text.

33:07

you have to convert it into numbers, right? And these are the embeddings that we look at.

33:11

We had a very small demo we did last session if you remember of that embeddings. There's an

33:15

embeddings file I shared with you. And all that you are trying to do is you're saying, hey, we have got

33:20

C1 and C1 is nothing but 0.11. What is C2? C2 is nothing but 0.13.1. Like that. As an example,

33:28

I'm just saying this is how you can think to it. So we have each and every respective chunk,

33:33

which is nothing but a chunk of text. We have each and every chunk. And now we are able to represent

33:37

each and every chunk as a sequence and the vector of numbers. So chunk one is a vector of

33:42

these many numbers. Chunk two is a vector of this many numbers. Chunk three is a vector of this many

33:47

numbers. And we are able to understand those respective chunks and, you know, and the chunk embeddings

33:53

we are able to also kind of relate to. So that's the way how we go and create the vector db. All

33:59

if we can see the vector db that we create, this is how we create the vector db. And now when the

34:04

user asks the question, this is a question the user will be asking.

34:07

When the user goes and asks the question, the retriever will go and retrieve the top two or the top three relevant chunks.

34:14

That is what the retriever will do. Right. So now user will ask a question. Imagine the question that

34:19

you're asking is, you know, how many leaves do we get in a year?

34:30

How many leaves do we get in a year? If you ask this particular question, this particular query will be converted into its respective query embeddings.

34:37

So we will go back and convert this particular query into its respective query embeddings.

34:44

And based on that, we will do a similarity search.

34:47

We will see a small demo of this today. So now you have the vector db where all the chunks are

34:53

stored as a bunch of numbers. And you have the original question which is converted into its

34:59

embeddings. And you are doing a retrieval. You are doing a similarity search. So based on that question

35:05

and its corresponding embeddings. You are now going to the vector db and you are trying to find out what are the top three similar chunks that you're getting. So you're trying to figure out that okay, what are the top three similar chunks we are trying to figure out. So based on the question that is asked, you go and look up in the vector db and you try to find out what are the top three similar chunks. What are the top three chunks we are getting? Top three chunks which are similar.

35:35

And now that is what you eventually feed to the large language model.

35:40

So those top three chunks is what you eventually feed to the large language model to go and generate a response.

35:48

So that's the way how the rag is working out.

35:50

It's a kind of generation, right? And this was the biggest, you know, difference that we talked about.

35:57

Like if you look at what we have seen so far, you have an LLM, you are asking a question.

36:02

That means you're writing a prompt, you're asking a query.

36:05

The user asks the question and the LLM generates a normal response.

36:08

This is the story we have been doing all this while.

36:11

This is something we have talked about already multiple times.

36:14

You write a query, the language model processes it, and it gives a response.

36:18

Now, the thing is that in, when it comes to internal data, proprietary data for the enterprise,

36:26

when it comes to proprietary data for the enterprise, doing this thing is very difficult.

36:33

doing this thing is extremely difficult, almost impossible.

36:38

So, and that's where I would say we have the concept of, you know, we have the, so yeah, doing this thing is very, very difficult in a real scenario.

36:48

Okay, in a real enterprise scenario, getting this done is very hard, right?

36:51

So in that particular case, because the LLN doesn't have any, any context about the HR related queries.

37:00

If you go and ask a normal question, how many leaves I get in a year, the language model doesn't have the pre-trained knowledge.

37:07

He doesn't know that.

37:08

So it cannot answer that question directly.

37:10

It needs something else.

37:12

And that's something else is what is called the context.

37:14

And that's what retrieval augmented generation is.

37:17

This is the normal generation.

37:18

So here, based on the question, you please retrieve the corresponding context.

37:23

This is what we will be talked about all this file.

37:25

So go to the vector TV, find out the relevant chunks.

37:27

You retrieve the context.

37:29

Based on the query, you retrieve the,

37:30

the relevant context and that entire thing, this entire thing becomes a user message for the large language model.

37:37

So that entire thing becomes the user message for the large language model and based on that you can generate a response.

37:43

So that's the way how we can understand how retrieval augmented generation is happening.

37:46

You retrieve, you augment the prompt and then you generate the results. Okay, extremely good, extremely

37:52

popular technique, extremely powerful and, and, you know, a very, very important thing that you will be doing as part of your

38:00

And that's why we have dedicated four classes for that.

38:03

Now, moving on, let's come back to the flow and let's continue on with our conversation.

38:10

And let's focus our conversation back to, you know, this concept of embeddings and vectors and similarities and all that.

38:20

Okay, let's see that.

38:21

So just to very quickly clarify the core ideas that we're going to.

38:30

ideas that we will discuss today. These are the four core ideas that we will discuss today in the

38:35

session just to walk you through it. We will understand what embeddings are at a very high level.

38:40

We'll try to understand what embeddings are, how to calculate similarity scores. We will see that

38:44

idea. We will also create embeddings for sample sentences using a standard library. The second point

38:50

we already covered last session. We will revisit that once again. The very last demo, if you remember,

38:54

we actually did that. We used an embedding model. So I gave sentences and we were able to generate sentence

38:59

embeddings. I will once again review that for you. We will finally store the vectors in a chroma dp.

39:04

This is the part where we will take those embeddings and we will stay within a chroma data,

39:09

Chroma DB. Chroma DB is a vector D. Chroma is a vector database. Okay. There are different,

39:15

different vector databases out there. The one that we are seeing in our session is Chrome. It's open

39:19

source. But is this the only one? No. There are other vector databases also out there. Okay. If you're

39:24

using any of the cloud platforms, the cloud has their own flavor of vector databases. Right.

39:29

the one that we are seeing, as I told you, once again, is chroma. But it does not mean this is the only

39:34

vector db out there. You have, you know, you have pyes, your pine cone. Fine cone is also a very,

39:40

very popular vector database. It's a cloud-based vector database. We have something called PG vector.

39:45

PG vector is by Postgres SQL. So that is also available. So there are many vector databases

39:51

out there. But the one that is very simple, easy to use, and also very popular is what is called

39:56

chroma. So that is what we are teaching you in as part of the session. But if you,

39:59

If you understand one product, you'll be able to understand other products also.

40:02

Ideas remain the same. See, it is, it is no different from, like, when you did that SQL module,

40:08

I think you had an SQL module, so as part of the curriculum, you know, we had an SQL module long back.

40:14

You did SQL, right? Everybody did SQL. This was long back. You looked at some basic examples of select

40:19

queries, you know, you looked at some how to join different tables, inner join, outer join. You did all this, right.

40:25

Now think about it. What is SQL? SQL is where you are, uh,

40:29

writing a query, structured query language, and that is being executed on some relational database.

40:38

Now, that database can be anything, right? There are many, many relational database management systems out there.

40:45

So I can, I can show you, I've got MySQL in my system. I think, not sure if you use this, but MySQL is one of the

40:52

examples, right? But you can similarly use SQL server. You can use Oracle. But what I'm getting at is,

40:58

the concept remains the same.

40:59

The concept does not change, right? So the concept does not change it on. Right? So I think I gave a wrong password.

41:08

So you can see, uh, uh, uh, I think I get, uh, what was my password? I forgot. Ah, finally I remember. So what you are

41:23

able to see right now is this is my MySQL. I use it as a, you know, general thing for, for mostly for trainings, not a production DB, obviously.

41:29

So I have some databases here you can see. But why am I opening this? What am I trying to show you? What I'm trying to show you is it my SQL is one company, right? There's one company called MySQL, which has this product called Wordbench. But the core idea of writing a select query doesn't change, right? I can still go back and select thousand rows. I can select top thousand rows. I can select first name, last name, select start. This particular syntax will not change, right? If you go from MySQL to some other database product, if you go to SQL,

41:59

server. If you go to Oracle, this is the SQL fundamentally will not change. Yes, the query will run on a different database. You have to

42:06

write that as to select query on a different database product. Maybe SQL server will have something called SQL

42:12

server management studio. If you use Oracle, Oracle will have its own interface. Right. So similarly for vector db is also,

42:19

if you understand the ideas behind chroma, if you know what is chroma, you can easily relate to other vector

42:24

databases. And finally, we will see the run top case semantic search and inspect retrieve chunks for

42:29

relevant. So, so, so the focus will be on this part. We will talk about this part. The embedding part

42:37

today, the chunking part we will not see today. Chunking is the next session actually. So we will,

42:41

we will see the embedding part, how you are creating the chunk embeddings, storing that in the vector db and the

42:47

retrieval part, how you are retrieving the relevant chunks. So in the pipeline, these are the aspects we are

42:51

talking about. Okay, I want to clarify, we are not going to see this aspect today. This is going to be

42:55

part of the upcoming session. Okay. Now, let's move on.

42:59

Let's move on.

43:01

Give me one minute guys, huh? Just give me one second.

43:29

Thank you.

43:59

So, first of all, what is the meaning of embeddings? We saw this briefly, you know, in the last session, basically, the concept here is related to how machines understand words, right? How do machines understand words? And the concept is very much related to that.

44:29

Okay. This is not a new concept. This concept runs a long way back. And I can take a little bit of digression to talk about that idea as well. How this concept of embedding is actually originated. Okay. So this all originated by from Google, basically. This was back in the year 2013. When Google came up with the word two-back model model.

44:59

Right? You can see this is Google's word two-weck model. So this is when the concept of embeddings really started coming out.

45:10

And what Google did was they looked at different words and they were able to represent these words as a vector.

45:18

That means as a sequence of numbers. So in a way, these numbers were somehow conveying what is the meaning of the word.

45:24

Because see, machines will not understand language the way you and I, we do, right? If I tell you the word sky,

45:29

Now, if you think of the word sky, there are 100 things that you will probably

45:34

relates to with respect to the word sky, isn't it? But the machine doesn't understand sky that

45:41

way? For the machine, the word sky is nothing but a sequence of 10 numbers. Sky is nothing but

45:48

a sequence of 10 numbers. That is what Sky refers to in a way. Right? That's the idea. So

45:54

and you can see the word two-back tool takes a word as input and produce.

45:59

as word vectors as output. It's going to produce the word vectors, basically. This is

46:05

the vector representation of words. And the interesting part is those numbers convey the meaning

46:13

of the word. That's the powerful thing. Now, the internals are very different. We're not going to get

46:17

into that as related to deep learning. But just to let you know this, this happened way back in 2013,

46:24

where we were able to represent words as numbers. Let me show you one more very interesting.

46:29

And because this was done, all of a sudden, I'm going to show you this beautiful example,

46:35

all of a sudden, we were able to solve mathematical equations using words. Can you see? This is

46:41

like a kind of a mathematical equation. So let me write it down. I think you can relate to it. So we

46:47

are saying Paris minus France and this thing, right? So we can basically say, you know, yeah. So Paris

46:59

to France is Rome to Italy? Like what is to Italy? That's the question we are asking. So it is like

47:05

saying, okay, is Paris is to France, then what is to Italy? So if I can figure out a way to represent

47:11

these words as vectors, then we can literally solve mathematical equations with words. And this

47:19

was a fascinating thing that we started discovering back in 2013. And, you know, we were able to

47:27

find relationships between genders, king plus man equal to queen plus woman. We were able to

47:32

find synonyms, anthonyms, cities which are similar, words which are similar. And these things

47:39

are possible using word to make. Because every word now has a series of numbers that are attached to

47:44

it. And from word embeddings, we can relate to the concept of sentence embeddings also. Let me show

47:52

you one more very interesting visualization to help you relate to this matter. So we have

47:57

this beautiful visualization. I want to bring it up for you. Look at this all of you.

48:06

Some of this is with respect to PCA and debaity reduction and all these kinds of things,

48:10

but I think you can, you can see this one. This is that word today. Very interesting. And you can,

48:19

you can, you can see that the word embeddings. There are 702.99. That means there are 71,091,000. That means there are

48:26

7,0291 words that you see here. Every word is a vector of 200 numbers. If I take any word here, if you look at the word right now, this is the word Oleg, sky view. Let's say there is a word called sky view. That point is sky view. You can also zoom in, you know, you can zoom into this word also. So there is a word called sky view. I can, I can, I can, oh, sorry, I lost that. Where is it? Yeah. It's very small. Yeah. Yeah, this is that sky view. You can see I can zoom into that.

48:56

word sky view. Yeah, sorry. Yeah, whatever, you know, it's, yeah, whatever, sky view. So now, uh, this word is a vector of 200 numbers. And,

49:11

and those 200 numbers somehow convey what is the meaning of that word sky view. Now you'll ask me that, sir,

49:17

how is it happening? Now, that's the internal, but very briefly I can tell you that, see, one of the things we talked about these

49:24

models is that they are trained on a tremendous amount of internet scale data.

49:28

So when you train these models on so much of open source internet data, imagine the word sky view. The

49:37

word sky view would have been used in so many places, right? The sky view, like, there can be so

49:43

many sentences or words you can, you can maybe build with respect to the word sky view. You know,

49:49

it's like one single word in a way. So, so what are the different?

49:54

context and what are the different scenarios where the word sky view can be effectively used?

50:01

So many. I mean, you can talk about a sky view restaurant or it can be used as a noun.

50:08

Okay. And there are so many ways that this word can be used. We can look at other words also, coenzymes,

50:14

right? You have other words like glial and all this stuff. And the best part is that if I go and,

50:20

we are basically done PCA here, because obviously I cannot represent 200,

50:24

dimension. So we've done PCA to show only the top three dimensions. And if I search for

50:30

similar words, let's say if I search for Saturn, very interesting, you'll be able to see the words

50:35

which are similar to Saturn. And this was an incredible discovery back then. So because we are able to

50:41

represent every word as a vector of numbers, all of a sudden, we can now plot these words in a coordinate

50:47

space. So we can plot Saturn. We can plot, you know, like Europa. Europa is one of the

50:54

moons of Jupiter. It's a planet, it's a celestial body, right? It's a moon of Jupiter, but

51:01

Jupiter only right. Jupiter or Saturn maybe. I think Jupiter, Jupiter only. It's a Jupiter's moon.

51:06

Titan is Titan is basically Saturn's moon. One of Saturn's moon's moon is Titan. It's huge. It's a very,

51:13

very big moon, massive. Okay. And space probe. You can see all these are similar to Saturn. So Saturn is related to

51:21

space and very interesting. When I compare Saturn's word embeddings with all the other

51:27

word embeddings, we are able to see all these are similar words. This was an incredible discovery.

51:31

We were able to make back that time. And as I told you, friends, sentences or what we refer to as

51:37

chunks, chunks are nothing but text. They are sentences, right? They're chunks. They're composed

51:43

of words. Just like words can have embeddings. Just like we have word embeddings. Similarly, we can have

51:51

chunk embeddings because chunks are comprised of words. You know, if you have five words

51:56

and each of the five words have embeddings, you can combine those five words and you can create a

52:01

sentence or a chunk embedding. That's one other way you can work through it. So that's the basic idea

52:07

behind what sentence embedding means. Okay, so what is the meaning of sentence embeddings? I hope that particular

52:14

part is absolutely clear to one of you, the concept behind what embeddings are. So this is just to kind of

52:20

clarify how the text becomes embedding. This is the internal process neural network is

52:24

involved in it. So for example, if you have the raw text, this is the big picture idea of what is going

52:28

on. You can see the steps right now, raw text. We do something called tokenization. What is tokenization?

52:34

tokenization is the process of taking the raw text data and we are trying to convert that raw text

52:40

data into, you know, into a list of unique tokens. That is what is referred to as tokenization.

52:47

I repeat again, we take the raw text data.

52:50

and we convert that raw text data into a list of unique tokens, and that is what is called tokenization.

52:56

Tokens are nothing but, you know, unique words basically.

52:59

So the quick brown fox jumps over the lazy dog, so this is an example.

53:05

Tokens may be words, may not be words.

53:09

Usually tokens are effectively like reusable chunks of text.

53:14

Okay, so if you ask me in practice, what happens is different models.

53:20

have different types of tokens. The tokenization is really not in our controls, although we are

53:24

seeing the theory behind tokenization, but it's not in our control. We cannot manually do it. So

53:30

and what have we done in the demo so far? You just write a prompt. You write a prompt, you make an

53:35

API call and the API gives a response back. So tokenization is not something we are manually doing.

53:40

tokenization happens at the model end. Just just before the model is about to process the data,

53:46

you are giving the input text. This has to be tokenized.

53:50

And this is what goes as input to the embedding model.

53:53

Okay. So that is, it is kind of a pre-processing step, you can say, which, which is done, you know, by the model.

53:59

And then the model will obviously take each and every of the respective words and convert up to embeddings and you have the entire sentence embedding.

54:05

That's the intuitive understanding behind how sentence embeddings are created.

54:09

Okay. That's the idea. I hope the idea. I hope the concept is clear to all of you. Okay. And this was, this was one of the sample examples we saw in the last.

54:20

This was the, this was the exact preview, you know, demo that we saw last session if you remember. We used a sentence transformer.

54:27

If you go to my content 6th, June 9, I think last we met on, we did the class on,

54:34

Wednesday only date. We did the class on 1st July. If I go to my first July session, you can see this was the file I shared, embeddings. IPYNB.

54:43

And let's open it up. You will see the exact same snippet. Whatever you are seeing right now on the screen, the exact same thing we covered here.

54:49

we were able to see an embedding model we were able to install sentence transformers and we downloaded

54:55

this particular model there are different different embedding models that are there and and we tried out

55:01

with a few sentences and based on these sentences the embedding model was able to take those sentences

55:07

and it was able to generate the embeddings for those sentences okay and this is very interesting you can

55:12

see that given this particular sentence or the text we are trying to convert that into a vector of 384 numbers

55:19

Right. So we are trying to take that particular sentence or text and we are trying to convert

55:24

that particular sentence or text into a vector of 384 numbers. We are doing that. And we are only seeing

55:28

the first five values. So what we are seeing on the screen right now are the, you know, are the first

55:35

five values. We are able to see the first five values on the, um, you know, the screen right now.

55:40

Okay. So this is also we are taking the entire sentence or text and we are converting that to a

55:45

vector of 384 numbers. And finally again, we are taking the

55:49

entire sentence or text and you're again converting that into a vector of 384 numbers.

55:52

So this is what we are able to do right now overall. So we saw this idea in the last session,

55:59

the sentence and bedding spot. I hope everyone's aligned. Everyone's clear. Now, what is the

56:06

meaning of semantic similarity? What is semantic similarity? This is in fact one of the things

56:11

that we are trying to do, isn't it? And this will be, this is what is relevant in the context of

56:19

retrieval particularly, which is what retrieval is doing. So let's say we have, we've got the chunks now.

56:27

We've got chunk one, chunk two, chunk three. And we know how to generate the embeddings. Imagine,

56:32

you know, I give you the chunks and you're able to convert those chunks into the vectors. And in the

56:36

chroma dv, you'll be storing the vectors. We will see that demo also shortly. I will show you exactly

56:40

how that's done also. But then the retrieval part, what are we trying to do? We are asking a question and

56:49

Based on the question, we are trying to find out what are the similar chunks, which relate to the question.

56:55

So the question will have a certain embedding. So you go back to the vector db and you retrieve what are the

56:59

similar chunks. What are the top three, top five similar chunks which relate to the question.

57:05

And how are we doing that? We are evaluating that based on semantic similarity. We are evaluating that based on

57:11

semantic similarity. Semantic similarity is how we are using. It measures how close the two texts are in meaning.

57:17

So semantic similarity measures how close the two texts are in meaning.

57:22

How close they are semantically. Semantically how close they are. So I'll give an example to you.

57:32

Let's say if I say the weather is cloudy tomorrow because it's monsoons in our country.

57:39

It's cloudy everywhere, right? Most parts of the country, you know, monsoons are arriving, right?

57:44

So now let's say, uh, one of the sentences I, I give you is it will be cloudy

57:53

tomorrow or let's say the weather is cloudy tomorrow. And the other another sentence I'm giving you is

58:00

okay, uh, there is no sun in the sky and it might rain. Another sentence I give you is,

58:07

there are a lot of clouds in the sky. Another sentence I can give is it's cloudy and

58:14

windy today. So in all these four sentences, if you think about it, there are four different

58:19

sentences. And if I take each of these four different sentences and if I generate their embeddings,

58:27

embeddings will be similar. Because those embeddings are telling you what, they're telling you the

58:32

context. Context is nothing but the meaning, the semantic meaning. Semantic means what is the meaning,

58:38

what is the meaning, what is the context of the sentence? In all these four sentences, the story is the same.

58:44

that it is cloudy and there is no sun in the sky. That's it. This is the context.

58:49

So that is how we measure semantic similarity based on the embeddings. Once you have the

58:55

embeddings, now we can apply a distance formula on those embeddings and we can find out what is the

59:03

semantic similarity. If you want me to give you a very brief, you know, example of this, I can do that.

59:12

just to just so that you understand it in a better way, let me take my third. So imagine we have

59:19

we have document one, okay, we have document one. So as I say, like this is exactly what I was

59:27

talking about. Reset password and recover account access are close. They're similar sentence. There's

59:32

similar ideas, right? But weather forecast is something that is different. This is very different. Okay. That's

59:37

the idea of anyways. Now imagine we have a,

59:42

you know, document one, or since we are talking about rags, I will talk about chunk one.

59:49

Let's say we have got chunk one. And chunk one, the embeddings are 0.1, 0.1, 0.2.

59:59

And chunk 2, the thing is 0.11, 0.1.1.1. And chunk 2. And chunk 3, it is, let's say,

1:0:07

0.7, 0.8. I understand this very carefully. This is the,

1:0:12

embeddings of each of the chunks. And these embeddings are somehow telling you what is the

1:0:17

meaning of the chunk. In reality, the embeddings will be several hundreds of dimensions,

1:0:20

but I'm just taking it simply put two. I want to also clarify these embeddings. It's not,

1:0:27

it's not interpretable by a human being. If you ask me, sir, please tell me what is 0.7 and 0.8.

1:0:33

Nobody can tell me. We don't know. We don't know. We don't know. We don't know what those numbers are.

1:0:37

At a deeper level, they are neurons in a neural network. They're hidden features. But we don't know what

1:0:42

these numbers means. But yes, collectively these numbers are telling you what the sentence

1:0:47

means or what the chunk means. And now here is the best part. You can go and plot it. This is exactly

1:0:52

what I was showing you in that beautiful tensor flow projector, which I pinged on chat. Now you can

1:0:58

go and plot it, guys. You can say, hey, C1 and C2 will be here. I use a different color. So C1 and C2

1:1:04

will be here. There goes your C1.

1:1:08

T1 will be 0.1. 0.1. 0.1. 0.2. That's C1. And we have C2.

1:1:19

C2. C2 is also very close. And C2 will be 0.11 and 0.21. And 0.21. You have C2.

1:1:28

Okay. And finally, we will have C3.

1:1:34

C3 got 0.7.8.

1:1:38

You got 0.7.8.

1:1:44

The C3.

1:1:47

You can.

1:1:49

I think I don't have to tell you much.

1:1:51

You can understand already what I'm probably about to say.

1:1:54

That now that you are able to plot these chunks in a coordinate axis, you can easily understand that

1:2:00

the chunks are very similar.

1:2:03

Maybe they're talking about the same thing.

1:2:04

Maybe they are both talking about H.R. Leaves.

1:2:07

They are both talking about leaves, leave policy.

1:2:10

Whereas C3 is talking about compensation policy because they're talking about a different thing on together.

1:2:16

So this is how we can measure similarity.

1:2:19

Similarity is an important idea.

1:2:20

Once you have the embeddings, once you have plotted the data, what we have right now, now we can find out the distance between these two values.

1:2:29

And there are different, different distance formulas we can use.

1:2:32

That becomes a mathematical part.

1:2:34

So you can use an equilibrium distance.

1:2:36

You can use a cosine distance.

1:2:37

Cosine distance is usually more preferred.

1:2:40

Okay.

1:2:40

So all that we are now trying to do is we are trying to find.

1:2:43

This is back to our school level mathematics, right?

1:2:46

School level mathematics.

1:2:47

There are two coordinates data points that we have.

1:2:50

And you have to find out what is the distance between these two?

1:2:54

We can all do that, right?

1:2:54

X2 minus X1 whole square plus Y2 minus 5 and whole square.

1:2:57

I think you can relate to it.

1:2:59

This is one of the distance formulas, right?

1:3:01

Similarly, if you see these two are very close, distance formula wise,

1:3:04

but these two are very far away.

1:3:06

Okay.

1:3:06

So that is how we are now all of a sudden able to use embeddings to say that which sentences are similar

1:3:12

and which are not similar.

1:3:14

So that's the beauty of, you know, sentence embeddings and chunk embeddings,

1:3:19

what we talked about here.

1:3:21

Okay.

1:3:23

Now.

1:3:25

And obviously, I think you can relate to it.

1:3:28

Keyword-based search and similarity search are two very different things.

1:3:32

Keyword-based search is basically if you ask me,

1:3:34

how things used to happen historically.

1:3:38

Even Google search, a large part of Google search,

1:3:41

how it used to happen was keyword-based historically.

1:3:44

A long, long time back, the time when we were in school and college

1:3:47

and we were using Google, Google was using basic keyword-based search.

1:3:51

But if you look at a large part of how the Google search happens today,

1:3:54

it is semantic search completely.

1:3:56

A lot of things that you see nowadays are semantic search.

1:3:59

Semantic search means you search based on meanings.

1:4:02

You're not searching, you're not just searching.

1:4:04

based on, like you type something and, and, you know, we had all these things like

1:4:09

SEO, search engine optimization.

1:4:11

This was a huge field.

1:4:12

You know, Google search entire people made their careers out of Google search.

1:4:15

How do you list yourself high on Google?

1:4:19

There are a lot of experts who will be, you know, there's so many YouTube videos you can watch.

1:4:23

And they will tell you that, okay, use these keywords, use these keywords so that you rank up.

1:4:27

Right?

1:4:28

So keyword-based search was a real thing.

1:4:30

So if you use certain keywords in your search and if the corresponding webpages under

1:4:34

the URLs also contain the keywords. Your search, your webpage will come higher up.

1:4:39

But what is happening nowadays, especially the last few years, one or two years, particularly,

1:4:46

I would say, is the embedding-based search, semantic search. At a high level, you can think of

1:4:54

it like every single web page. I will call it web page one, webpage two, web page three. Imagine

1:5:00

there are like millions and millions and millions and millions of web pages. I'm just putting

1:5:04

a number, 10-2-2-6, whatever. Every single web page is basically stored as embeddings.

1:5:09

Think of it that way. So when I say web page, I mean to say the entire HTML content of the page.

1:5:15

The whole HTML content of the page, everything. Everything is basically stored as embeddings.

1:5:20

So web page one embeddings are, web page two embeddings here. Web page three is also like embedding,

1:5:25

something like that. Okay. Whatever. Every web page is like embedding. The next time you are in Google

1:5:29

search, you are in Google search and you ask a question. This is the same retrieval engine that is playing.

1:5:34

Whatever story we discussed in RAG, the same retrieval engine is used for similar kind of retrieval engine Google is also using.

1:5:41

Actually, Google users hybrid search. If I honestly tell you, Google users variations of different, different search.

1:5:46

Semantic search is one of it, but they use hybrids. Sometimes they also do it based on keywords.

1:5:51

So sometimes there are certain types of queries where keywords are more important. So they will use keywords to find out which are those links, which contain those keywords the most.

1:5:58

But a major part of how they are doing it is semantic search. So based on the query,

1:6:03

they are converting the query into query embeddings and then they are going to the vector db.

1:6:09

The vector database is consisting of the list of all web pages and their embeddings.

1:6:14

Think of it that way. That's what the vector DB for Google will look like.

1:6:17

Okay. And they are now based on the question the user asked, they are going to the vector DB and they are

1:6:22

retrieving the top 10 similar pages, web pages. And that is what they will show you in the search results.

1:6:27

So they're actually finding out, okay, based on whatever question you asked, we think this web page is very

1:6:33

similar to that and textually, semantically, and that's a very powerful thing, right?

1:6:40

In fact, if you look at some next generation search engines today, like perplexity,

1:6:45

okay, Google, to take Google be AI mode here, stuff, or all that, but if you look at perplexity,

1:6:50

if you look at perplexity, if you look at perplexity, perplexity is doing the same thing, right?

1:6:53

So if I continue with my Google, so if I go back and show you this thing,

1:7:03

what I name perplexity, Google started. I don't know what.

1:7:10

Google has to do with perplexity.

1:7:12

Because normally what happens is in your phone, you say, okay, Google, right?

1:7:17

Now Google, first, chalooed. But I think for some reason, when I said perplexity, my phone,

1:7:24

Google got started. I don't know why it happened.

1:7:27

Anyways.

1:7:29

So, yeah, where is it?

1:7:33

is that free plan or great, you know?

1:7:38

Oh, okay, fine.

1:7:40

Sure, yeah.

1:7:40

So what we can do is, uh, if I, you know, if I go and ask, this is again, very interesting.

1:7:45

Let's say if I, uh, so let's say the, the war situation, you want to know more about, yeah,

1:7:52

FIFA World Cup, okay, what's the latest in the FIFA World Cup?

1:7:54

Okay, now's the World Cup time, right?

1:7:56

What is the latest in the FIFA World Cup?

1:8:00

If you want to know what is the latest that is going on right now?

1:8:03

So what used to happen before was, you know, if you look at traditional search,

1:8:07

what, you know, if you look at traditional search, what, you know, what, what Google used to traditionally do, guys.

1:8:15

Traditionally, Google what can't do?

1:8:17

Google will basically give you, okay, just a second, I'll, I'll, you know, so if I go to, so if I go to Google and ask this question,

1:8:27

I, I, I went to Google home page, and I'm asking the question, what is the latest in the FIFA World Top?

1:8:33

If I go and ask this question, now it way, AI mode will give you, uh, exactly the semantic

1:8:40

search thing that I was talking about, right?

1:8:42

But now if you go and do a normal Google search, you up to top me digger AI overview.

1:8:47

And what it is basically trying to do is it is trying to summarize the information from

1:8:51

multiple sites and give you a summarized response.

1:8:54

This is the beautiful application of the retrieval semantic thing that I was talking about.

1:8:58

So, so historically Google used to do this, right?

1:9:01

You ask a particular question.

1:9:03

and Google is really taking you back to FIFA.com, all the relevant websites where those

1:9:08

keywords are potentially coming out strong. So they are doing that hybrid search. But what they are

1:9:13

also doing now is they are looking at the query. They are trying to find out what are the similar

1:9:19

embeddings from those web pages, which of the websites have similar embeddings.

1:9:25

Abidding here here Al Jazeera a year, Al Jazeera a year, India Today came here. Which are the websites

1:9:30

which have similar embeddings? And they are trying to scrape the information.

1:9:33

from that and they are giving you a summarized response.

1:9:36

This is all. How cool is that? And you can see this your answer up kaya, whatever answer you got

1:9:43

in AI overview, you are able to see when I click on show all, you can also see all the

1:9:47

websites that were used to answer that question. Now this is what Google is already doing. Google was

1:9:53

actually a late entrant. The company does this even better is perplexity. If I go and do this

1:9:58

in perplexity, perplexity is forplexity. They were one of the pioneers of this kind of

1:10:03

of search. Google actually implemented this AI mode a lot later. Google was more of a late

1:10:08

entrance to it. But perplexity was already doing it before Google. This is one of the reasons

1:10:12

why perplexity became popular. So their tagline was that, okay, how you can search better than

1:10:20

Google. So Google was not even doing this when perplexity started to implement this.

1:10:26

So they were one of the pioneers in this kind of search, right? You asked a question and what

1:10:30

perplexity does? Perplexity.

1:10:32

you can't you have a general links, but perplexity is a classic example of

1:10:37

semantic search. You can see, you ask a question and perplexity is retrieving the

1:10:44

similar, you know, web pages or the similar content based on semantic search and it's summarizing

1:10:52

the answer and it is answering the question. Google in here it is giving links. But perplexity

1:10:58

is not giving links. Perplexity is actually answering the question. What? We're

1:11:01

you're asking the answer. And what's even better is you can ask follow-up questions.

1:11:06

You can ask follow-up questions. You know, how did Norway versus England potter filing get

1:11:09

scheduled? If you want to know, let's say, Norway-England-Kut-ho-day, okay? How is

1:11:13

M-Bap? Like, who are the top players right now? Okay, you can actually ask these kinds of questions,

1:11:20

okay? Yeah. Okay. So Embabape, Messi and Haland are all tied on seven goals.

1:11:28

You can see this one. Okay.

1:11:31

Anyways, I hope everyone's clear. Perplexity, I'm sure all of you are using, right? Everyone knows this. I just wanted to relate the ideas to, you know, things that we all use on a day-to-day basis. You can see that whatever rag we are discussing, there are so many places where we are already doing rag. Just that we don't realize it, actually. Now, we are not doing, actually, the companies are doing. But we are using their solutions. We are using search. We are using perplexity. Okay, there are so many places where rags are getting used, actually. The same retrieval concept is getting used. Okay. Perplexities are

1:12:01

Classic example of rag. It is doing that exact rag idea that we discussed. You ask a question. It is retrieving similar chunks and the language model is giving a summarized response. Classic example of rag. Okay.

1:12:13

Okay. Let's move on, guys. Now coming to vector databases, I think we already have discussed this. I'm going to go a little quick on this one. And as I told you, vector databases, they store embedding vectors and support similarities. The same story. We are just, you know, going round and down and talking about the same thing.

1:12:30

So let us move on. So this is what we refer to as exact match. What you guys have done in your SQL course, you are running a select start from users where user ID equal to seven. This is what we know. This is like a normal, you know, SQL search we are doing. And this is a similarity based vector search. Exactly what I showed you a while back in that coordinate axis. So story. If you take each and every word or if you take, excuse me, each and every, you know, sentence, you can represent.

1:13:00

and those sentences in the coordinate space and you can find out that similarity distance.

1:13:05

Okay. So that's the way how you can do it. All right. So the chroma lab we will be seeing right now and we will see

1:13:12

these six step pipeline. We will collect and upload the raw content. We need normalized, extract,

1:13:17

extract insights, generate the content, validate the quality and publish. Okay. So this is the general thing

1:13:24

that we will be seeing. So let us go back. Let us see the chroma DB example here.

1:13:30

Okay. So we'll see that chroma example, how and what we can do inside chroma. And that's the, that's going to be the, you know, the next part of our conversation, specifically on the vector DB part. So we talked about embedding. Now we have chunks. We have managed to create embeddings. We understood what the embeddings mean. We understood what semantic search and semantic similarity means. We saw those pieces. And now we are going to store those embedding in the vector TV.

1:13:58

So we are getting into the chroma part.

1:14:00

up right now. So let us see. Now from here onwards, I'm going to go back to my notebook. I'm going to go back to my notebook and

1:14:07

that we also set things up in my notebook. So PIP install ChromaDB. This is the package we are using.

1:14:18

And I will also PIP install sentence transformers. This is we are using for the embedding models. You remember we did

1:14:24

this last week. So these are the two main packages we are installing right now. I'm doing it in front of you.

1:14:30

All right.

1:14:45

All right. Now, from here onwards what I will do. I'll go ahead and go ahead and

1:15:00

Let me restart the runtime. Always a good idea to restart the session. And now this is the

1:15:06

embedding part. I think we already talked about this part. So this is just the same code we ran last time. We're just

1:15:11

running this again. So I'm taking loading the particular sentence transformer model. I'm taking two

1:15:16

samples sentences. These are two sample sentences I've taken. And I'm just trying to create the two

1:15:21

vectors for these two sentences. That's it. Very basic. We're just trying to take two sample sentences.

1:15:25

And then we are trying to create, you know, vectors for those two sentences. You can see how it looks

1:15:29

slide. Okay. So we're just saying model dot input. You can see we are not doing any tokenization

1:15:35

nothing. All this is happening internally. We are not doing anything. Okay. So, so we're just giving that

1:15:40

entire input and it's happening automatically. So we're seeing the first five vectors. Okay. It's downloading the

1:15:47

model. We're using a very basic lightweight model. And we can see the first five numbers for this

1:15:54

vector vector we already saw this last time. Now,

1:15:59

This is, we are taking a very small example for this use case. We're considering

1:16:07

an e-commerce support, think of it like an e-commerce support knowledge base.

1:16:12

We'll take an e-commerce support knowledge base we'll be taking. And there are five frequently

1:16:19

asked questions that we will be, you know, we will be considering. Okay, in a real world, what will happen

1:16:26

is when we will come to the more advanced sessions.

1:16:29

especially starting from next to next session. We will take a real PDF. We take a complete full

1:16:35

PDF and we will see the rag. But we are still in the introductory class, a second session only. So we are

1:16:40

not taking a full PDF, but we are simulating a document. That's it. So we are just saying, okay,

1:16:46

this is a document one. This is a document two. This is a document three. So we are just simulating the

1:16:49

chunks right now. In reality, you will take a PDF and you will create the chunks. But as I told you,

1:16:55

the chunker is not something we are seeing today. Chunker will be part of the chunker is something. The chunker is something

1:16:59

we will see in the next session. I think the very next session is about chunking.

1:17:03

The very next class is about chunking and document preparation. That's coming this.

1:17:09

I think, no, but this is not meeting. I think that's coming Saturday. So we will see chunking

1:17:14

actually. So then we will see that entire PDF in practice. How do we chunk? How do we do the whole

1:17:20

thing? But today as a small demo, we are only considering each and every document. We are we are simulating

1:17:29

those chunks? We are saying, hey, this is chunk one, this is chunk two. This chunk three

1:17:32

is chunk four, chunk five. And this is the text in the chunk. This is the text contained in the

1:17:38

chunk. So normal FAQ, customers can return products within 30 days. Refunds are processed within

1:17:45

five to seven business days. You can think of it like a knowledge base. A customer care in

1:17:49

what you have, you call on, you, ask, you. The man or the guy or girl that is sitting there,

1:17:56

they will look at a particular, uh, a FAQ

1:17:59

he has a, so I'm just saying, like, you know, they will have a rule book as well,

1:18:04

which they will refer to.

1:18:06

Do you ask a question? They refer to the document and they answer.

1:18:09

That's the big picture idea.

1:18:10

How we're going to do. So I'm just saying that, okay, let's say these are the answers to questions.

1:18:17

This is that rule book. There are five rules that I've given. There'll be thousands and thousands

1:18:22

of rules, but I'm just saying there are five rules.

1:18:24

Five policies in them have been.

1:18:26

Okay, orders above 499 qualify for free shipping. You can reset your password and

1:18:30

express delivery arrive within 24 to 48 hours, simple. So this is basically how we are

1:18:36

simulating one chroma row. Now, chroma db, what we will store? We will store the chunks. I

1:18:44

already told you. And what is that, what is the chunk? The chunk is basically this. This is every

1:18:49

row is like a chunk right now. This will be stored in chroma db.

1:18:56

I.D. I'm in. Important. Text, it's

1:18:59

important. That's the actual content. And the third thing, very important. We haven't seen

1:19:05

this before. Metadata. What is metadata, guys? Metadata basically means data about data.

1:19:12

We have information about the chunk. The text chunk is what we have, right? But can we extract some more

1:19:20

information about that chunk? Just for better search.

1:19:26

We can some more information about it. So that is basically the metadata aspect that is coming out.

1:19:34

So can we get some more information about that specific chunk? That is where the metadata part will

1:19:39

coming. How do we get a little bit more information about that respective chunk? That is where

1:19:46

the metadata part will come in. So you have this particular chunk. Customers can return products

1:19:51

within the 30 years of delivery. So metadata will say category returns.

1:19:56

So what is the corresponding category? This query falls under the returns category.

1:20:01

Next chunk is this. This particular query falls under the returns category. This particular query

1:20:08

falls under the shipping category. This particular query falls under the account category. And this

1:20:15

particular query falls under the shipping category. So this is merit card.

1:20:20

So your data in Chrome TV in store is. Chroma TV in ID, text will, merit data, and

1:20:26

betting is right. Now you will ask me, sir, metadata, what is the benefit of storing that?

1:20:31

Right? Because you can search better.

1:20:35

Aqa query is only related to account, then you can do a normal. It's almost like the sequel where clause.

1:20:44

You can literally say wear category equal to account select only those rows.

1:20:48

So imagine there are total five rows in my vector DB right now. Five rows, but all the five chunks are not about

1:20:55

account right. So we can further streamline the search. We don't have to go to every

1:21:00

single, you know, chunk and figure out the similarity. So I can straight away say, okay,

1:21:08

get me only those chunks relevant to account. Okay, account related question. Let's say,

1:21:12

sometimes it happens, right? You go and call up customer care and the first question they ask you is,

1:21:16

please tell us, how can we help you? Now, you know, I would say, uh, so, you know, I would say,

1:21:22

a, yeah, yeah, absolutely, good, good, take, 100%.

1:21:25

That you can use the LLM for that also.

1:21:29

You can use LLM be used to, but you will do it yourself.

1:21:32

Meta data is completely under your control, okay?

1:21:34

Completely under your control.

1:21:36

Now, uh, customer care will ask you, please let us know why you're calling us.

1:21:44

Now, you'll say, okay, I'm calling about my returns.

1:21:47

Second, someone will be, no, I'm calling about my account, my account got locked.

1:21:50

So, the other one, I want to know when my order will get shipped.

1:21:56

Chotha, no, I want to return my product.

1:21:59

Tabetally, person, has not come to pick up my item, my return date maximum is exceeding.

1:22:05

See, these are all queries, whenever you are asking the question to customer support,

1:22:10

that agent is automatically evaluating his category, what is the category?

1:22:13

So customer has asked the question, what is the category of that question?

1:22:18

Or other customers, let's say, I'm the customer.

1:22:20

the question my account got locked, please unlock it.

1:22:23

So the model is deciding it's a account related question.

1:22:27

So what kind of? It will go to the vector db and it has to answer, right?

1:22:31

Based on my question, it has to look up the answer from the vector database.

1:22:35

But the vector database, it hasn't have to go through all this.

1:22:38

All the chunks it doesn't have to see.

1:22:39

It will now that it has identified my question is related to account, it will only pull up

1:22:44

those chunks which are related to account.

1:22:48

Account related to those 10, 15 chunks.

1:22:50

retrieve that. And from those 10, 15 chunks, you can, you see whether it can answer science

1:22:54

question. So that's the basic idea of why metadata is so important. It helps you in efficiency.

1:23:01

Okay, just understand this at a broad level for now, but I think once you see the whole pipeline,

1:23:05

it will become a lot clearer. Okay. So this is where we are right now. We have the,

1:23:10

just to summarize, we have five documents, but the five chunks we have manually created.

1:23:15

And you're also able to see the information about the chunks here.

1:23:18

Next, we will create the chroma client and we will store the embeddings.

1:23:23

So this is the next phase we will see.

1:23:24

Okay.

1:23:25

Guys, if you want to take a short break, let's take a short break.

1:23:28

Otherwise, this, this demo will continue now.

1:23:30

This is going to continue now.

1:23:33

And this is basically pretty much what we will do till the end.

1:23:37

Right.

1:23:37

So let us, let us take a short break.

1:23:40

Okay.

1:23:41

Take a water break for five to 10 minutes.

1:23:44

And I will see you back after the break and we'll continue from the same notebook.

1:23:48

Okay.

1:23:48

dot then.

1:23:49

Sure.

1:24:18

Thank you.

1:24:48

Thank you.

1:25:18

Thank you.

1:25:48

Thank you.

1:26:18

Thank you.

1:26:48

Thank you.

1:27:18

Thank you.

1:27:48

Thank you.

1:28:18

Thank you.

1:28:48

Thank you.

1:29:18

Thank you.

1:29:48

Thank you.

1:30:18

Thank you.

1:30:48

Thank you.

1:31:18

Thank you.

1:31:48

Okay.

1:32:18

Start on here. Just in a minute just in a minute.

1:32:48

All

1:32:52

All right.

1:32:55

All right.

1:33:18

from where we, where we closed before the break.

1:33:22

So guys, let's continue on.

1:33:24

So we were able to, we were seeing the Chrome RDB demo right now.

1:33:27

That's the focus area for the next 20 to 25 minutes to happen now, whatever we have left out.

1:33:34

And we were able to see the embeddings.

1:33:36

We saw how the embeddings are getting created.

1:33:38

We understood what are sentence embeddings, what is the meaning of embeddings.

1:33:41

We took a lot of time to understand that.

1:33:43

Conceptually, we saw some interesting visualizations also.

1:33:47

And you were able to take some examples of embeddings and similarity search with respect to Google search, perplexity.

1:33:55

We saw some examples there.

1:33:57

And now we are looking at ChromaDV. Right.

1:34:00

So we have taken five, we have created five sample chunks right now.

1:34:05

All of you are able to see that.

1:34:07

We have got chunk one, chunk two, chunk three.

1:34:09

So there are five sample chunks that we have created right now.

1:34:14

So every row is a chunk and we are also able to see the chunk text.

1:34:20

So this ID is document one, document two, document three.

1:34:24

Every row is like a chunk.

1:34:26

And we are also able to see the corresponding chunk text.

1:34:28

This is the corresponding chunk text you are able to see.

1:34:31

And we have also associated some metadata data data with it.

1:34:33

So in a way we have, you know, we have basically created these five sample chunks right now.

1:34:40

We have associated with the ID.

1:34:42

We have associated with the chunk text.

1:34:44

and we've also assisted in the metadata.

1:34:45

What is the metadata with respect to the child?

1:34:47

Okay.

1:34:48

Now we will create the chroma client and the collection.

1:34:51

We will create the chroma database.

1:34:54

Okay, let's see that to store our embeddings.

1:34:57

How do we do that?

1:34:58

Let's see that.

1:34:59

How do we exactly do that?

1:35:01

Okay.

1:35:01

This is nothing but the code basically what we have seen.

1:35:04

So first you import chroma DB.

1:35:07

You import something called preprint,

1:35:09

P print.

1:35:10

P print basically stands for pretty print.

1:35:13

Okay, so preprint stands for pretty print.

1:35:14

for, you know, pretty print basically.

1:35:18

It's a Python's Pretty printer.

1:35:20

And it's kind of like a formatting thing,

1:35:22

you know, you have normal print statement.

1:35:24

So Pretty print actually goes and formats the data

1:35:28

in a nice way so it makes it more readable, basically.

1:35:30

So you can read the outputs better.

1:35:32

And we'll see that how it is getting used, right?

1:35:35

Next, we are, you know, instantiating the part.

1:35:40

This is where I want to store my chroma DB.

1:35:42

Okay, so Chrome.

1:35:43

So CromaDB dot persistent client,

1:35:45

we are giving the parts where we want to store it.

1:35:48

So after a while, we will see that here,

1:35:50

the chroma DB will get created.

1:35:52

So this is the path where we want to store it.

1:35:53

The persist, persist means we want to persist the disk.

1:35:57

Ultimately, our database will reside in a disk.

1:36:02

Jubei database, if you guys, just say I may my SQL will be.

1:36:05

My SQ is also stored in some hard disk.

1:36:08

It is not like in the RAM.

1:36:10

That means here, J. J.J.J.J.J.J.J.J.J.J.J.

1:36:13

down if I come back to the session tomorrow day after, it should persist.

1:36:18

So that's the idea behind this particular thing, okay?

1:36:22

Next, we are saying client dot get or create collection.

1:36:25

We are creating the collection where the embeddings will be stored as the collection.

1:36:30

The collection is like a sequel table.

1:36:32

Okay, so collection is like a sequel table where the embeddings will be stored.

1:36:35

This is just like like what we discussed in our, in our examples, right?

1:36:40

So collection is like a sequel table.

1:36:42

So much of every row will be.

1:36:43

chunk or your chunk text will here here chunk embeddings will.

1:36:47

Chunk text will chunk, chunk embeddings will.

1:36:49

So that is basically the collection.

1:36:51

Okay.

1:36:51

So you will give the name of your collection and you will also, you know, give the embeddings.

1:36:57

Next, we will add our data to the chroma collection.

1:37:01

Let us see.

1:37:01

This is what we have done.

1:37:02

So collection count is zero.

1:37:03

So this is what we have here.

1:37:05

This is before absurd.

1:37:07

So we have not done any insert right on.

1:37:09

Abidtak still we have just created this.

1:37:11

So we have simply created the thing.

1:37:13

So right now, where are we?

1:37:15

We have simply created it.

1:37:17

You simply created the collection.

1:37:18

That's it.

1:37:19

But nothing is inserted yet here as of now.

1:37:22

Now we will add the data to the chroma collection.

1:37:26

Now, our table is the table made, the support knowledge base,

1:37:29

the collection name or the SQL table that I created.

1:37:32

Now we will add data to it.

1:37:34

Here data down the five chunks that we have.

1:37:37

This joe five chunks we manually created here,

1:37:41

these five chunks we will insert.

1:37:43

to the chroma D.E.

1:37:45

Now, it will insert the five chunks of vector

1:37:48

going to make and we will insert those vectors in the chroma DV,

1:37:52

the chroma collection that we have created here.

1:37:54

So we must generate vectors for our documents using the same sentence transformer model

1:37:59

and then write them to the database.

1:38:02

Okay, so sentence transformer load.

1:38:04

No problem.

1:38:05

And here I am basically extracting the documents.

1:38:09

I'm extracting the IDs and I'm extracting the metadata.

1:38:12

This is.

1:38:13

straightforward Python syntax effectively.

1:38:17

All of you are able to see that.

1:38:18

This is where we are extracting the documents,

1:38:21

the IDs and the metadata,

1:38:23

and we are doing model.n.

1:38:27

Documents, because our idea metadata is okay,

1:38:30

that is separate.

1:38:31

But our objective is to embed what?

1:38:33

Create embedings for the documents.

1:38:35

Documents, what's up the text here.

1:38:38

Whatever is the text content here,

1:38:40

that is what we want to ultimately create the embeddings for.

1:38:43

So,

1:38:43

we are saying model dot encode documents and these are the document embeddings.

1:38:50

So five documents that document embedding been.

1:38:52

Basically, five chunks of chunk embedding been.

1:38:54

Next, what I will do, I will simply say collection.

1:38:57

What is collection?

1:38:58

Collection is this one.

1:38:59

Remember, collection.

1:39:00

Collection is this one. Remember, collection.

1:39:00

Collection is here.

1:39:03

And now I am saying collection.

1:39:05

Dot absurd.

1:39:05

Upsert is like an insert.

1:39:07

You know, absurd is just another way to say insert in PromaDB.

1:39:10

So you're trying to insert rows into a table.

1:39:12

Just if it's a SQL query, you will say, you will say insert.

1:39:16

So upset is like insert or update.

1:39:19

So it's like either it inserts or it updates, but that's okay.

1:39:22

That's why we call it upsert.

1:39:24

Okay, so upset Q has.

1:39:26

Upsert means either it will insert or update.

1:39:28

So up stands for, up stands for the update part and cert stands for the insert part.

1:39:35

Think of it that way.

1:39:35

But again, update is not what we are seeing in today session.

1:39:38

So it is only for the inserting part we are using it for today.

1:39:41

Okay.

1:39:41

So you will specify.

1:39:42

the IDs. There are five IDs. You specify the five document chunks. You specify the

1:39:47

five metadata and you specify the five embeddings. Straight forward, nothing. So this

1:39:53

your TV will be the table, the table is very simple. You will have an ID column. Think of it

1:39:59

that way. Like visualize it. You have a ID. You will have a document column. Document column will

1:40:05

contain your document chunks, the chunk texts. You will have a metadata column. The metadata column. The

1:40:11

The meditator column will contain what is the merit data for that particular chunk or finally you will have an embeddings column.

1:40:17

Yeah, embeddings will contain what are the, you know, the numeric embeddings for those chunks.

1:40:22

So if there'll be five rows in that particular collection, the SQL table up and this is what is stored in that chroma reading.

1:40:29

Okay, this is what you're doing with this particular statement. You're inserting the five rows here.

1:40:33

Five rows you're inserting here with the document chunks and the embeddings.

1:40:37

Okay, all that magic is happening in this simple line of code. Let us see that.

1:40:41

I will run the code. This usually takes a little time. It's a very small data set. So it is quick. But this is the part that usually takes a tremendous amount of time. Because you're taking the embedding model. You're going to every single chunk and you're creating the chunk embeddings. So this usually takes a little bit of time. And finally, we can verify what is stored. We can go back and verify what is stored here. You can peek into it. So never demo a search without confirming the ad operation work, which is very important.

1:41:09

you are inserting something.

1:41:14

So obviously, I want to know, I want to validate that yes, my DB looks good.

1:41:19

Whatever five chunks are there, I want to see that is there.

1:41:23

So let us peek into the DB.

1:41:25

Peak carengen.

1:41:26

And quite literally, his function can name is the name of the function.

1:41:32

Everything is done through the collection.

1:41:33

Collection is that table, right?

1:41:36

So collection in data data data.

1:41:38

absurd here. And now I'm into collection. Dot peak. Simple. Now collection has five

1:41:44

records. There are five rows in the collection. And peak. Sample, this is how you are able to see

1:41:51

the data. When you say collection dot peak, this is how we are able to see the data in a dictionary

1:41:56

like format. We are now able to store the data in a dictionary like format. And you can see exactly

1:42:02

what I was talking about. Like we've got documents, embeddings, IDs, metadata, the exact way how we

1:42:08

talk about it. Same way. It is a kind of a dictionary like structure. Okay. Yeah, this is how it is,

1:42:15

the data is stored in Proma, not in a Python dictionary. But this is only the rendering. What you're

1:42:18

seeing is just for the display. But in Proma, it is stored in a different way, obviously, okay? Yeah, this is only for the rendering.

1:42:24

So yes, indeed, we are able to see the five documents. One, two, three, four, five. We are also able to see the embeddings,

1:42:33

patch embeddings behind. You're also able to see the five IDs. And you're also able to see the five. And you're also able to see

1:42:38

five metadata. Okay? Metadata in all the other things. We'll have a separate class on

1:42:43

metadata later also. That is also part of the session later. But if you're asking, sir, what else can be part of

1:42:49

my metadata? File names can have. You can have file names. You can have page numbers. Sometimes when you have a

1:42:56

tremendous amount of data, like in the next class, when we start talking about real PDF documents, real

1:43:02

document loaders, how you take a data from a real file. That time, I would.

1:43:08

When I'm creating my chunks, imagine there is a PDF file spanning 10,000 pages.

1:43:13

This is our page of PDF. And if I'm trying to create chunks from that PDF, there'll be so many chunks that will be created.

1:43:19

But ultimately, I want to maintain reference to my page numbers.

1:43:23

I want to know keyword chunk, which document it is from, which dot PDF file it is from.

1:43:28

I want the file name and I also want the page number.

1:43:31

So oftentimes the metadata will also contain the file name, the file source, page number, other references.

1:43:38

So these kinds of things are also quite common.

1:43:41

So we are done with chroma DB. And finally, we will now retrieve the data with similarity search.

1:43:48

So finally, now we will retrieve the data with similarity search. So we have taken the data.

1:43:53

We have taken those five chunks. We've created embeddings. We have managed to effectively, you know, go back and we have, we have, we have gone ahead and we have, we have, we have gone ahead.

1:44:05

and we have stored the data in the collection, all that we have done.

1:44:10

And now it is time for us to retrieve, now it is time for us to retrieve the information.

1:44:16

You can retrieve the information.

1:44:18

How do we retrieve using similarity search?

1:44:20

If you want to do an exact look up, you can also do it, but we will be doing a retrieve on the basis of

1:44:26

similarity search specifically.

1:44:29

That's how we will be doing it.

1:44:31

Okay.

1:44:32

So let us see that.

1:44:33

Let us see the query for that.

1:44:35

And we will use something.

1:44:35

called collection.

1:44:37

Collection of copy, we've seen syntaxes today.

1:44:41

We have seen collection that upsert to insert the records.

1:44:44

We have seen collection that peak to see what is going on inside it.

1:44:47

And finally, retrieval to time we will do collection.

1:44:50

Dot query.

1:44:51

This is the retrieval engine that we'll be seen right now.

1:44:54

Okay.

1:44:54

So let us see the code here, what we are trying to do.

1:44:57

So predict the top match.

1:45:00

If the user asks, I want to return my shoes and get my money back,

1:45:04

user's question.

1:45:05

This user has a user calls of customer care and user is asking this particular question.

1:45:12

I want to return my shoes and get my money back.

1:45:15

This is your question.

1:45:16

So based on that, the chatbot should be able to return the right answer to you.

1:45:21

So based on whatever question you are asking, can we retrieve the similar chunks and give you the answer?

1:45:25

So which of our five FAQs do you think will be the closest mathematical match?

1:45:29

What's our closest match is?

1:45:31

This is our closest match.

1:45:31

This is simple.

1:45:33

So you can create your query.

1:45:34

So you can create your query embedding.

1:45:35

Same story, same rag story we have discussed.

1:45:37

So you have the original user question.

1:45:39

Convert that to query embedding.

1:45:41

Use the same embedding model and generate the embeddings for that.

1:45:44

And then you do a similarity search.

1:45:45

Go to the vector db.

1:45:47

Look at all those five chunk of embeddings and see which chunk embeddings are similar.

1:45:51

And that the same kind of your question's answer.

1:45:54

Okay.

1:45:55

So simple, you can see, I want to return my shoes and get my money back.

1:45:59

So first I will use model.

1:46:00

Model.

1:46:01

Model is the same model that I downloaded a while back.

1:46:04

User query go do.

1:46:05

converted to query embedding.

1:46:07

Your query embedding here.

1:46:08

And very important, must be the same model as the document ingest.

1:46:12

So whatever model I used in ChromaDB, this has to be the same model.

1:46:16

This is the same model that mini max model that I used here.

1:46:18

You have a model there, which we already loaded right now.

1:46:22

And we are using that same model to generate query embedding.

1:46:25

Okay?

1:46:25

Age there is very simple, nothing to talk about.

1:46:28

Collection.com queries are syntax.

1:46:30

You specify the query embedding.

1:46:32

And it will go to that collection.

1:46:33

Collection, that massive table where the first.

1:46:35

five chunks and weddings are already stored.

1:46:37

It will find out the top result, top three, methods, top one matches, whatever you want.

1:46:43

Okay, and this is the results that will be returned.

1:46:45

And here you are just printing out.

1:46:46

This is just the printout that we are doing right now.

1:46:49

Okay, you up here up here.

1:46:50

Run and you'll be able to see.

1:46:52

In fact, you can actually return top three also.

1:46:54

Like, top three return, you can return top three.

1:46:58

And if you can return three, and if you say three, you'll be able to see the top three similar chance.

1:47:02

So I want to return by shoes here query.

1:47:03

And the top matches are.

1:47:05

this one, okay.

1:47:08

You know, refunds are processed within five to seven business days.

1:47:13

This is the closest one.

1:47:14

It is a distance of 1.17.

1:47:16

Next one is customers can return products within 30 days, 1.17.

1:47:19

And then, see, I mean, we can debate and discuss, sir, I think this is not answering the question.

1:47:25

But we answer to our objective for this current exercise is not to answer.

1:47:29

We are only talking about retrieval, that's it.

1:47:32

Answering the question is going to come in the next session.

1:47:35

Ultimately, answer.

1:47:35

how we're doing? But today's objective is only decreasing.

1:47:39

Your whatever is there in your vector d. And that is a very important aspect of rag.

1:47:45

If you, if you remember what we saw in the last session, we discussed a very important concept

1:47:49

called grounding. Your answer must be grounded in the context. So when a user asks a question,

1:47:54

that question, the LLM cannot invent that answer.

1:47:58

Abhi, you ask me to return my shoes and get my money back. I can invent an answer. I can

1:48:03

try to give a general answer. I'm general answer.

1:48:05

Okay, but I don't want to give a general answer. Right? I don't want to give a general

1:48:10

answer right now. I want to go back and, uh, effectively go back to the vector TV and find out

1:48:16

what are the similar chunks related to the question. Okay, so this is a similar chunk. This is a similar

1:48:21

chunk and this is the similar chunk and this is the similar chunk. That's the thing. And here on this

1:48:25

basis rank order may have come. So this is the closest chunks, basically. This is the collection

1:48:30

that query syntax up here using. Okay. And we can try another one very interesting.

1:48:35

interesting. I repeat again, this should be from the chunks which are already in the vector

1:48:40

D. If you've got some sort of a question, which is relevant in

1:48:44

then that's a problem. That's a problem, obviously. I have forgotten my password. So very

1:48:49

interesting. It's something to do with account. Some of me. I've forgotten my passport. So again,

1:48:54

the model, you will generate the query embedding for that. And now you want to retreat the top

1:48:59

similarity, similarity search. You want to get the top one result. You can do that. You can do that.

1:49:05

Very simple.

1:49:06

Now look. And quite interestingly, you are able to see retrieve that answer.

1:49:10

It's giving the right answer. You can reset your password from the account setting. So, okay,

1:49:14

the question is about. But remember, the answer is coming exactly from the chunks. It is not

1:49:20

inventing an answer. That's what I mean by grounded. It's a grounded generation.

1:49:25

You're retrieving the chunks and is grounded in the context. It's not, it's not trying to, you know,

1:49:29

give you something else. So it's, so based on the question, it is only retrieving what is there in the

1:49:33

vector degree.

1:49:34

And then after, our generation over which is the next thing in the next class, next to next class, in fact, we can see that later.

1:49:42

And finally, the last use case I've given is the when ranking can go wrong, very interesting.

1:49:47

This is the last kind of an edge case which I've given. So when ranking can go wrong.

1:49:51

That's up, you're a completely irrelevant question. Okay. So what happens if a user asks a question about something we don't have in our database?

1:50:01

What if a user asks the question we don't have in our database? What if a user asks the question we don't have in our?

1:50:04

database? Vector databases don't reply. I don't know. They just return the mathematically

1:50:09

closest vector even if it's completely unhelpful. So again, based on whatever concept we have studied,

1:50:17

you ask the question and we are trying to retrieve what are the relevant chunks or who closest chunks

1:50:24

return? Whether it is related or not, it doesn't matter. It is only going to look at the mathematical closeness.

1:50:34

embeddings are the closest. Even if they are far away, out of that top one consa,

1:50:40

that is he going to return. And you can see this one. Can I pay with my UPI? Story remains the same.

1:50:45

You take the question, please convert that into query embeddings. And now you will do

1:50:49

collection. query and you want to fetch the top one result. That is what the code means.

1:50:54

Run and I'm getting the answer. Look at this one. Orders above this. So here related

1:51:00

is not. We have nothing. We don't. We don't have nothing. We don't.

1:51:04

have any payment effect cues. Our payment related information in here. If you remember the five

1:51:08

chunks which I had, there was nothing to do with payments. There was account related thing.

1:51:12

There were returns related thing. There were returns related to things. But there is nothing with

1:51:17

to payments. If a user is asking the question, it is giving you, it is giving you a similar

1:51:22

chunk, the most similar chunk. The closest vector. But it is nowhere related to. But maybe you can

1:51:30

say UPI has something to do with payments or rupee has something to do with.

1:51:34

with payment. So it probably thought it is similar. So closest vector match, okay,

1:51:38

answer. So this is the basic idea. So oftentimes this validation is also very important.

1:51:44

After I asked, are the chunks like what is very important, especially from a support context is,

1:51:51

does your FAQ? This is the classic case of an FAQ manual, right? Does your FAQ contain all possible

1:51:57

sets of question answers? So the great way to test your application. You can actually have the users,

1:52:02

ask some completely unrelated questions and see how the how you know how the

1:52:07

retriever is happening are we able to retrieve the exact number of chunks on the basis of this that's

1:52:12

actually a very important factor that's a very important factor basically

1:52:16

okay i hope everyone's aligned everybody is able to relate to it yeah all right um

1:52:32

So simple. There is nothing much. I think once the core ideas are clear.

1:52:39

Simple. Not much. And just one small thing I wanted to clarify. You just remember, it's not going to be so

1:52:44

relevant for now, but just remember, get versus query. I'm a demo in a query. Query is what is used

1:52:51

for similarity search. But in case you want to do an exact look up, which you can't ever

1:52:54

never never want to do an exact look up. But just in case you want to look up exactly. But just in case you

1:53:01

want to look up exactly by the ID. They say, Mano, you want to find out what is ID number one.

1:53:06

You want to find out what is ID number seven. So you can use the get method. That is, it's an exact

1:53:10

look up, which in practice we never do. We don't do an exact look up in a normal DB. But just remember,

1:53:15

there's a method that is there. There is a get method. There's a query method. Just for your, you know,

1:53:20

just for remembering. Okay. Yes. So it is using, you can question that key sir,

1:53:25

sir, should be this for key, get ca what use case? If an administration tasks, so admin, there'll be a data

1:53:31

database admin, they might want to fetch by ID. They want to evaluate.

1:53:34

There's some chunk in a report here. So the administrators will want to see,

1:53:40

that chunk in the chunk in the chunk. So they want to take that chunk ID and they will

1:53:43

want to retrieve based on the chunk ID. And then they want to see, okay, what is there in the chunk.

1:53:49

So basically for checking the metadata, for debugging, a error handling, some other administration

1:53:55

issues. So that is where the get method would be useful. But for the normal semantic retrieval,

1:54:00

it's all query, whatever we have seen in my demo. Just wanted to mention this on the side,

1:54:04

okay? Just keep this at the back of your mind all of me. Okay. This is actually one more

1:54:13

nice visualization that is summarizing everything we have seen so far. Beautiful visualization.

1:54:18

But therefore, you have a user question. Useer asks the question. The retriever will retrieve the top

1:54:24

relevant chunks. You know, you're getting a scoring function. Scoring function will find a similarity.

1:54:29

and whichever documents are the most similar, the most similar. Point 92 is the similarity match.

1:54:35

Your sub's similar. That is what is written. So document 8 is most similar. Document 3 is most similar. Document 15 is

1:54:41

more similar. Document 2 is more similar and document 27 is more similar. So these are the top five similar

1:54:47

documents which are retrieved. Document but the chunks which are retrieved. So this is just another visualization

1:54:52

on whatever we have seen so far. Okay. All right, guys. I hope everybody is.

1:54:59

with me and this is pretty much the all that we have for today's session.

1:55:04

And what comes next? What comes next? As I said, we have two more sessions on rags that are coming up.

1:55:09

So this is only the part of the session where the main focus was on embeddings and vector DB. And we have two more

1:55:18

sessions on rags coming up. And the very next session, we will talk about chunking and document

1:55:23

preparation. We'll talk about the chunking, but in more detail.

1:55:25

Today, we'll make chunks to manually create here. Next session, very next session that we have.

1:55:31

We will actually take a real PDF and we will create chunks. How we will create chunks. We will see

1:55:36

the chunks size, overlap, how do we go back and take those chunks and save in the vector Db? We will see

1:55:42

that. And finally, the last session will be the complete pipeline. We will take a real PDF.

1:55:48

We will do the chunking. We will do the vector DB. We will do the rate. We will do the redacted. We will do the

1:55:55

and have the language model generate the answer. So retrieval part will be the focus

1:56:00

for that next session. And finally we come to agents. So these are the next things that we'll be

1:56:05

seeing. Okay. So just wanted to summarize the contents for the session today, whatever we saw. Okay.

1:56:12

I think it was a comparatively lighter session because many of the ideas we were, we were aware of.

1:56:18

So hope everyone was able to follow. So we saw embeddings. We discussed embeddings in a lot of detail today.

1:56:24

We understood how to create embeddings.

1:56:25

This was already covered in the last session briefly, but we saw this today in detail.

1:56:30

We saw how to store vectors in chroma. How to store. We saw the absurd operation. How to create

1:56:36

the chunk embeddings and how to store them in the chroma db. We saw that. And finally, we saw how to run a top

1:56:42

k semantic search. So how do we do a semantic search? And what was the main query? We saw. We saw.

1:56:47

Dot query. Collections. query. So yeah hogea collections. Dot up sort. You gogear collections.

1:56:52

So I hope everyone was able to follow. Yeah. So any questions? All of you are able to

1:56:58

relate to it. Everybody. The code is also saved here. You can please reference it. This is the

1:57:09

1st July folder. Sorry, the 6th July folder is already saved in your drive. Everyone can please

1:57:15

refer to it. Okay. So any questions, guys, all good. You are all able to follow.

1:57:22

Do let me know.

1:57:52

So yeah, so thank you. I'll pass it over to Pratap. Pratap, we'll continue with the

1:57:57

Tementi-meter quiz. And so all of you can take some time to do it. And yeah, so thank you. Thank you,

1:58:05

guys. Thank you everybody once again. I'll see all of you in the next session. And thank you everybody.

1:58:10

Yeah. Thank you, sir, for another interesting lecture on the first half of retrieval.

1:58:19

I think people have already very much convinced on

1:58:22

like what it is your thought and that is where they don't have any questions.

1:58:26

Yeah, yeah.

1:58:27

You don't share.

1:58:28

All right.

1:58:29

Okay.

1:58:30

So students, I'm releasing the feedback poll and you guys can answer that.

1:58:34

Once the feedback poll is completed, then I will start the Mendemeter quiz.

1:58:39

Okay.

1:58:40

So the feedback poll should be live now.

1:58:52

Okay. Students, please make sure you answer the feedback poll.

1:59:08

Meanwhile, I'll start the presentation for the mintimeter quiz.

1:59:22

Okay, all right. It seems everyone has voted. Great. Students, if possible, you can also write the law. How did you find today's lecture experience? Second question. Because I've noticed many people don't answer that.

1:59:52

I'll wait for one more minute.

2:0:22

All right.

2:0:52

else who's joining if there are five players only then i will start okay i'm ending

2:1:00

the poll now if anyone is still answering just let me know

2:1:05

all right the poll is

2:1:14

The poll is entered. Students please join the Mentiator quiz. Only five people.

2:1:21

There are like 10 of you here right now.

2:1:28

Seems many of you are not interested in the Mentiator quiz.

2:1:37

They're like 14, 15 people in class and now. Now there are only 10 people left.

2:1:44

All right, fine, six players I guess I'll start.

2:1:51

Good luck.

2:1:56

Which tool stores and searches vectors in the lab?

2:2:03

So in the lab as in this class.

2:2:06

Which tool did you see for storing and searching vectors?

2:2:14

Everyone will get this right, I'm sure. Yeah. So the correct answer is chroma DP.

2:2:44

chunks and queries. So what will you use to encode stored chunks and queries?

2:2:51

This is slightly difficult I guess. I mean it shouldn't be really pretty easy answer

2:3:06

actually if you paid attention. Okay so yeah the correct answer is same

2:3:13

embedding model, it's not the same document ID. Document ID is not relevant

2:3:18

in this situation where you're encoding. Okay?

2:3:23

encoding will be done using the embedding model. All right.

2:3:43

What does lower distance usually mean in chroma?

2:3:51

When you're talking of, when you're talking in chroma, when you say lower distance between a vector, between two vectors, sorry.

2:4:02

What does that mean?

2:4:04

I think everyone would get this.

2:4:06

Oh.

2:4:09

Okay, I'm a little surprised by it.

2:4:12

Okay.

2:4:13

That three of you did get it wrong. Okay. When you are talking about chroma, when you're talking vectors in ChromaDB, it means distances between the two vectors is less. That means the two vectors are closely related. So like the distance between, say, for example, a man and a king would be.

2:4:43

less than say, for example, a man and a woman, right?

2:4:48

That's what it usually means in terms of vector.

2:4:53

So, yeah, lower distance means their meaning is closer.

2:5:13

questions left. I think they are easy. I don't remember exactly. Oh yeah. Okay. Which

2:5:22

chroma query argument is was used in this lab in the class a lot. So which was

2:5:32

the chroma query argument, which we used? So this one is a little specific little tough, but

2:5:43

I think the next one will be a lot easier. Yeah, the next one is a lot easier.

2:5:48

Right.

2:5:49

Okay. So the query argument that we used was query embeddings mainly.

2:6:02

We did not use any of these actually. Query texts were document include IDs.

2:6:08

So Sir was teaching primarily about query embeddings.

2:6:12

in this lecture. Okay. So all right, this one, this one was a little tricky though, to be very honest. All right. Nice. Last question. Why can a UPI question still return? Why can a UPI question still return

2:6:42

a shipping FAQ. This is something sir covered almost towards the end. Like last 10 minutes, I think.

2:6:56

Last 10 minutes, they sir kind of covered it. So, and I tried to make the option a little easier, but then, yeah. Yes. So, so UPI is

2:7:12

related to payment and payment is usually related to something shipping. So that is why it is

2:7:18

most likely to return the nearest available vector. UPA does not mean delivery. UPS means delivery.

2:7:27

UPS means delivery. I think the UPS is a delivery service. So that can also be one reason why,

2:7:33

because UPS and UPI are like only one letter difference. So they might be closer and they might be

2:7:42

semantically similar also. Yeah. So both the logic is kind of applicable. But all right.

2:7:53

Great job to everyone. It's great you attempted it.

2:8:01

And yeah, junkinator. Okay. Congrats. All right. With that, with that, we are at the end of the

2:8:12

I will see you guys on Thursday, I think. Thursday is when our, when the tutorial session is there. And then on Saturday, Saturdays, lecture is there, I think. So, yeah. You guys will have, like, fun for two days now. All right. Have a good rest of the week. I'll see you guys soon. Bye-bye. Good night.