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

Thank you

13:46

Thank you

14:16

Thank you

14:18

Thank you

14:20

Thank you

14:22

Thank you

14:24

Thank you

14:26

Thank you

14:28

Thank you

14:30

Thank you

14:32

Thank you

14:34

Thank you

14:36

Thank you.

14:38

Thank you.

15:08

Thank you.

15:38

Thank you.

16:08

Thank you.

16:38

Thank you.

17:08

Thank you.

17:38

Thank you.

18:08

Thank you

18:38

Thank you

19:08

Thank you

19:10

Thank you

19:12

Thank you

19:14

Thank you

19:16

Thank you

19:18

Thank you

19:20

Thank you

19:22

Thank you

19:24

Thank you

19:26

Thank you

19:28

Thank you.

19:30

Thank you.

20:00

Thank you.

20:30

Thank you.

21:00

Good evening everybody. We just wait for everyone to join just starting out in a few minutes.

21:30

Thank you.

22:00

Thank you.

22:30

Thank you.

23:00

Thank you.

23:30

Thank you.

24:00

Okay.

24:04

Welcome to everybody.

24:17

Welcome to the session.

24:19

Welcome to the session. We will start on here.

24:30

Thank you.

25:00

Thank you.

25:30

All right, guys, just to quickly set the context, what we are trying to cover today and the overall agenda for the session today, just to walk you through it, what we are going to, what we are doing and how we are overall facing today's session.

25:48

I'll just quickly, you know, give you a brief on that.

25:53

So today, our agenda would be to get into pretty much rags.

26:00

We will go back to rags, whatever we discussed, and we will talk about some advanced aspects of rags in the session today.

26:06

That is the main agenda.

26:08

And this is what we have done so far.

26:11

So we have fairly familiar in the previous module.

26:14

We have gone through rags.

26:17

We have gone through the different tools.

26:19

We have built retrieval apps.

26:20

We have also built agent flows.

26:22

So that was the previous module.

26:23

And this current module until now, we have, the last session was a very interesting session on guardrails.

26:30

very important session where we understood what are the different challenges and safety challenges that large language models face.

26:38

So we talked about guardrails. We talked about how to protect against unsafe inputs.

26:43

And today's session is going to focus more on pretty much the similar ideas of rags. First thing,

26:51

I'm going to recap a little bit of rag for all of you. And then we will discuss a few other advanced concepts on rags.

26:58

When I say advanced concepts,

27:00

These are ideas like how to do chunking.

27:02

What are the different types of chunkers?

27:05

We will talk about metadata up, how to apply metadata filters, concepts around re-indexing.

27:12

Why do we need to do re-indexing?

27:14

And a very, very important aspect, which is how do we evaluate a Rags system?

27:19

All this while, even in the last module, we had four classes on Rags.

27:24

In fact, five, but all that we did was we took some data, we built a Rags system, and we got an

27:29

answer. You know, if you remember, we did that demo on the Tesla dataset, and, you know, we were

27:35

able to ask a question, like, for example, what is the annual revenue in the year 2024 or the year

27:42

2022, and we got an answer to the question. We were able to, like, you know, get an answer to the question

27:48

in a very general way. But who is going to evaluate with whatever answers we are getting are the

27:54

correct answers or not the correct answers? How are we going to evaluate whether the answers are

27:58

correct or not. That is a very, very important thing to keep in mind. And this is exactly

28:04

where the idea of evaluation will come in. So a big part of the session, I will also focus on

28:10

evaluation. Basically, how to make the Ragn answers traceable and reliable. How do I rely on a Rack

28:16

system? Whatever answers I'm getting, how do I rely on it? So this is being the core focus areas of the

28:21

session, what we will achieve out of today's class. Okay. Now, let us quickly go back to this

28:28

a very nice diagram that I shared with you. Right at the very beginning of my journey

28:34

of Rags, we did this if you remember long, long back, long time back, almost more than a month back

28:40

when we introduced our first class on Rags. We have seen this. And I will very quickly review this

28:46

for everybody, what it is. I will take up a similar use case, a very practical use case, and from

28:52

here we will go ahead. Okay. So what is retrieval augmented generation?

28:58

And what are we trying to do in a RAC system? This is the workflow. First, on the left

29:03

and side, you can see we are taking the documents. So right on the left and side, what we are doing

29:07

is we are taking all the documents. All the different documents we are considering here. And

29:12

then we are sending the documents into a chunker. A chankar will be responsible for taking the

29:18

PDF. It can be one PDF. It can be several PDFs. It can be several PDFs. It can be one

29:24

PDF or it can be several PDFs we can have. We can have a bunch of many, many PDFs.

29:30

So this particular chunker is responsible for taking the bunch of different different

29:34

PDFs and to create chunks. And there are different types of chunkers. I will talk a little bit more

29:41

about this chunker today. A couple of other methods I will talk about. So the analogy that we took up,

29:47

just I can take my marker to write this out again for you.

29:54

Just mark it on the screen for everybody to get a good understanding, right?

30:18

So we have the PDF. There is a PDF that we have the PDF that we have here.

30:23

imagine we have a 100 page PDF HR manual. This was the use case we took up in the last

30:28

session. We have an HR manual. A hundred page PDF is what we have here to start with. And we are

30:38

doing chunking. And the type of chunking that we are doing right now is, you know, we are saying that

30:43

every, every page is one chunk. We are saying one chunk is one page. So that means if it's a hundred

30:48

page PDF, how many chunks are we basically creating in the process? We are basically creating in the process?

30:51

We are basically creating total 100 chunks in the process. We have C1. We have C2. We have C3 and we go all the way up to C100.

31:00

So we have basically created overall 100 chunks in the process, C1, C2, C3 up to C100. And these chunks are nothing but, you know, sections of text. The chunk is nothing but a section of text. So C1 is a section of text. All the way up to the C100 is a section of text. So each of these chunks are basically nothing but different, different sections of text.

31:21

text. Now I told you that machines don't understand. Machines don't understand text. So what is the next thing

31:29

we do? We convert these chunks into embeddings. So there are embedding models that we use. We convert the

31:34

chunks into embeddings and all this eventually get stored in what we call a vector DB. A vector database is the

31:40

very special type of database where you would be storing the unstructured data. That means in this case,

31:47

you'll be storing the chunks and you'll be storing the respective embeddings. So you will sort, okay,

31:51

say C1 can be represented as a vector of this many numbers.

31:55

C2 can be represented as a vector of this many numbers and dot C100 can be represented as a vector of this many numbers.

32:01

So we are actually, you know, representing the chunks with respect to their embeddings.

32:06

Okay. And mind you, the vector DB is not just used for storing, you know, our text.

32:11

The vector DB can also be used for storing images. The idea is very, very similar.

32:16

And in our sessions, usually we have used something called a fixed size chunker.

32:19

If you remember the Tesla data set that we worked on, we used a fixed size chunker.

32:23

That means every 512 characters you want to create a chunk.

32:27

Next 512 characters, another chunk.

32:30

Next 512 characters another chunk.

32:32

So we have basically done the chunking in a very fixed size manner.

32:35

That has been the focus area so far.

32:37

I will talk about a few other types of chunking in a moment.

32:42

And part of today's class will also be about discussing the other loopholes that we have in the rag system.

32:47

Some other advanced mechanics we will talk about.

32:49

That is what we will see.

32:51

Okay.

32:51

So again, this is this, this initial part is going to be a one-time process.

32:56

The initial vector DB creation that the enterprises do will usually be a one-time process, right?

33:01

You take the entire PDFs, you do the chunking, you divide the PDF into different, different chunks.

33:07

If it's a 100-page PDF, you divide that into 100 chunks.

33:11

Every page is like a chunk.

33:12

Think of it that way.

33:13

So every page is like a chunk.

33:15

So you divide the entire PDF into 100 chunks.

33:18

C-1, C-2, C-3, C-3.

33:19

4 up to C-100. And then you take each and every one of the respective chunks. You take C-1,

33:24

C-2, C-3, C-4. You take each and every one of the respective chunks and you, you know, you save it as

33:31

embeddings. You take C-1 and you save the embeddings of the chunk one. You take C-2, you save the embeddings

33:37

of chunk 2. All the way up to, you take C-100 and you save the embeddings of C-100. So we take each

33:42

and every individual chunk and we are able to, you know, save the chunks in the form of the embedding format.

33:48

So this is the one-time process that we do. Now, what is the next thing that happens?

33:54

The next thing is users will ask the question. Imagine I ask a question, you know, what is the

34:00

leave policy in the company or how many leaves I get in the year, right?

34:06

What is the leave policy? Or let's just say, how many leaves I get in a year. That is the question you're asking.

34:12

So next time you ask the question, again, the question will also be in a string type of format, right?

34:16

Whenever you ask the question, the question will also come in a typical string type of format.

34:21

Again, machines don't understand the string particularly. So what will happen is you will take that

34:25

particular question and you will convert that into query embedding. So, so this is the question or the

34:32

query that you are asking in a string format. You will take that particular query in a string format

34:37

and you will convert that into query embedding. And then you will send it to the retriever and the retriever will

34:43

retrieve the top two similar chunks. The idea will be very, very simple.

34:46

So the retriever will once again do what? The retriever will take that particular query.

34:50

Whatever query is being, whatever question is being asked, the retriever will, you know, it will kind

34:57

of take that particular question. The retriever will take that particular question and it can retrieve

35:03

retrieve the top two or the top three similar chunks. That's what the retriever can go back and do.

35:08

Okay. So the idea is that you have a particular question or a query that you are asking. You go to the particular

35:13

vector DB and you find out whatever question.

35:16

is being asked which sections of the document or which chunks in the PDF

35:22

pertains to the question. Like if I want to know what is the lead policy in the company, I want

35:29

to semantically select only those chunks which potentially contain the answer. And that is what

35:34

we call the retrieved context. These are the retrieved context. Right? What is it? This is what is

35:40

the retrieved context. This is what we are able to retrieve from the vector DB. And this entire

35:46

thing becomes the input to the LLM. And that's why I say whatever we saw in the initial

35:50

parts of our session was, was like a normal generation. That means you ask the LLM a question.

35:58

This is the query. The query becomes a user message. LLM will have its own system message,

36:03

right? And on the basis of that, the language model generates a particular response. So this is how the

36:09

story has been so far. The language model is going to take a particular user query. User query is

36:15

query is like a question. And the LLM will also have a system message of its own. And

36:22

based on that, the language model is able to generate the response. That is the way how the process

36:27

has worked out so far. Okay, you ask the question, the LLM has a system message and based on that

36:33

it is able to generate the response. That is what we have seen and what we have discussed so far already.

36:38

Right? We have, so we are sorted on that particular part. Right. Now, what is different in a Rang? What is

36:45

different in a rag is that not only are you now giving the question. Because remember, the whole

36:49

idea of a rag is what? The language model is not supposed to know your question. It's not,

36:54

it doesn't know that. If you're asking a question about a very proprietary data or if you're

37:02

asking a question about a very business specific process, then the language model does not have the

37:08

answer to that question directly. It doesn't have the pre-trained knowledge of that task. Imagine you're

37:13

working for a company like C-V.

37:15

You're working for a company like Cisco, ABB.

37:19

So we are talking about engineering companies, automobile companies.

37:22

And all these companies will have a lot of intellectual property.

37:26

They will have a lot of confidential data on their different systems and their different components

37:32

and engines and all the equipments that they manufacture.

37:35

And this is not in the public domain.

37:37

It is not that you can go to Google and search for PDF and you will get something about

37:42

Siemens' latest, you know, equipment.

37:44

You will not find that.

37:45

online. And that is why these large language models, be it a GPT model or a Lama model,

37:52

what we have been using in Grok, these models are not trained on that data. If you directly

37:57

ask a question about that, it will not be able to answer. And that is exactly the big picture idea

38:01

of the Rags system. Rack systems come in very, very handy when you want to effectively retrieve information

38:07

from internal confidential data, public data that the language model itself doesn't work. So now you

38:13

cannot do this. You cannot just ask the question.

38:15

a response. You ask a question. You retrieve the context. And now the query and the context,

38:23

the query and the context, both will be part of the user message. So it is still a kind of

38:31

generation. The LLM will still have a system message of its own. We are still asking a question.

38:36

But along with the question, we are also retrieving the context. And now this entire thing is becoming

38:41

the user message for the large language model. And based on that, it is generating a response.

38:45

That's the way how you can think of how retrieval augmented generation happens.

38:49

So first you are retrieving, then you're augmenting, and then you're generating.

38:53

So that's the big picture idea behind what retrieval augmented generation is.

38:58

Right. I hope everybody's aligned.

38:59

Everybody's, everybody's clear with what the idea of a RAT system is.

39:04

This is what we have already seen before.

39:08

Now, what I want to talk about, I want to go a little deeper into it today, because that's part of what the class is for today, right?

39:15

going to go a little deeper into Rags and understand a lot of mechanics of Rags.

39:20

Guys, what are the points of failure? What are the different areas where you can go wrong?

39:25

When you talk about a Rags system, because we are talking about a company's internal data,

39:34

right? You're talking about a company's internal data. And if you want me to kind of,

39:41

maybe before I start with the rest of our conversation, let me just share this with you.

39:45

Just give me one second. Just give me one second.

39:51

Just give me one second.

40:15

Thank you.

40:45

Thank you.

41:15

Thank you.

41:45

Thank you.

42:15

Thank you.

42:45

Thank you.

43:15

So, guys, I'm going to take up a real, I'm going to take up a real use of the real use case for the Rack system to highlight this.

43:34

To highlight this in a, uh, uh, uh, in a better way to highlight this in a, uh, in a better way so that all of you get a sense of what, uh, what we are doing in the right.

43:42

Okay. Let us take this. Let us take this up. So this is actually a real, um, ABB user manual. Okay, I just, I just pulled it out from, uh, you know, this is actually not confidential. So just to let you know, I just wanted to give you the feel of it. Okay. It's not confidential. This is the real user manual. And, uh, what I will do is let me, let me also share this with you. It's a very nice case study. I've kind of walked you through it in the very same way.

44:12

that we discuss. AbB is one of the, is a very big engineering company based out of for Switzerland, okay?

44:18

So, uh, just wanted to take up this case study. So we recently did a small kind of technical workshop for this, for them, for their,

44:25

you know, their employees. I do a lot of these, some of these corporate workshops for different companies.

44:30

And this was actually the same kind of case study I took up there. So, and, and apparently this is something very similar to what they are also doing.

44:38

If you look at large engineering companies, they're also solving something very similar. They have a lot of

44:42

of, you know, manuals and all this and they are trying to build a rag assistant on the basis of

44:47

this data. Let me upload this for all of you. Let me upload this for all of you. Then I will take

44:52

you through it. And my point is you can relate to the Tesla demo. The Tesla demo, what we talked about

44:59

the idea is the same. Here you have a PDF manual. It can be in a PDF form. It can be a document form. It can be

45:05

in different, different file formats. And you can build a question answering system on this. And, and, you know,

45:11

what I say is, if you understand the idea of retrieval augmented generation,

45:17

you can literally automate the entire support landscape.

45:23

What I'm talking about is let's say if I go to Google and search Panasonic's product manuals.

45:27

Can you see? Look at it. This is Panasonic's product manuals.

45:31

AC's, refrigerator and a washing machine. You can just go there. This is India private

45:35

limited. In India, whatever washing machines are sold. Next time you don't have to pick up a phone

45:40

and call anything about the washing machine.

45:41

machine. Your chatbot will just type the question. It will look up in the manual,

45:46

give you the answer. Now, I'm suggesting it's something that everybody can do. It can be a very small

45:51

proof, POC kind of a small project you can do. Now, if I click on the washing machine,

45:56

your kitha, user machines, user manuals for all the different washing machines. So you can basically

46:03

do a little bit of web scraping. A web scraping. Automatically go to the individual links,

46:08

download the respective PDFs, approximately 1530 pages.

46:11

every PDF. And you can take all the PDFs in one folder and you can basically do everything

46:17

that we have talked about in the same day. So all the products of Panasonic, all the product

46:22

manuals, all this can be basically part of the, part of the documents, list of documents over.

46:30

You can do a chunking, right? You can do a chunking and you can find the chunks. Okay. And then you can

46:38

store in the vector TV. The vector DB will basically consist of information about all.

46:41

all your you know so next time from a application perspective next time when

46:48

users ask a question let's say your AC is not working or your TV is not working or something is

46:53

not working the very first thing we do is we call up customer care right that is usually the first

46:57

line of working we have but what this will ensure is that you can kind of completely get rid of that

47:02

so you can already start to see where the world is at it like the concept of product manuals and all

47:08

that we have will completely go over

47:09

So I mean, I'm thinking of the world where probably either the websites like Panasonic

47:16

will put up a small chatbot in their site.

47:19

Now chatbots have been there on for a while but maybe this will be like a rag-based chatbot

47:23

which every enterprise will do going forward.

47:26

Either it will be that or it will be integrated right within chat GPD.

47:28

Because chat GPT may integration for everything. You can go and ask in chat GPT.

47:33

Chat GPT will internally do a rag and give a response back.

47:36

You can see the use cases. There are so many and how how

47:39

maybe in a good way how it will be beneficial for users because oftentimes support as

47:45

you know the customer support is not able to answer questions properly right but then if you

47:51

have a rag assistant a rag chat bot this will 100% answered your questions

47:55

correctly so this could be some of the use cases basically okay now let me go back to

47:59

this particular demo what I was talking about initially so this is for ABB it's

48:05

actually a primary control firmware manual it's a very technical document and this is the

48:09

kind of thing that engineers will be working on, right? So the technicians at ABB will be

48:15

working on these things and they will face a lot of issues, sometimes some errors will come,

48:19

sometimes good logs may errors are and they want to know. They want instant support. We are talking

48:24

about business support. Like ABB's technicians will not call up customer care and all that like they expect

48:30

a proper business enterprise support, right? So can we build a rack system for the technicians at ABB?

48:36

where if in the engineers and the, you know, the floor managers, they face any issue,

48:43

if they face any issue in the particular product and the things, so can we give them answers to specific

48:48

answers to questions? And through this demo, I also wanted to highlight how important the accuracy of the thing

48:53

is. It is so important to be accurate.

48:56

I mean, see, it is not like a simple Tesla demo that I'm demoing in the class.

48:59

If it's okay, the wrong answer, I mean, you cannot afford a wrong answer here. This is a business

49:05

sensitive thing. If users are asking the question, it has to retrieve the correct

49:09

chunks and it has to give the answer. It is very important to have the right accuracy. And that is

49:14

the next phase I will talk about, the evaluation part. Okay, so quickly just to walk you through

49:17

the flow, quickly just to walk everybody through the flow so that we are all aligned. Okay. So just

49:23

just run this notebook briefly for all of you. I'll be a little quick on this one because we have

49:28

done this before. Just that I wanted to take up a different use case with you. Okay. So that you get

49:34

a good flavor of it and you're able to remember because we did lags quite a long time back.

49:39

So I'm going to upload the ABB demo file right now.

49:45

You have my APP demo go here.

49:53

And I will go ahead and install the necessary libraries. Let me quickly do that. Let us see.

50:04

Thank you.

50:34

this runs guys i wanted to okay let this execute first and then i'll show you

51:04

Thank you.

51:34

Thank you.

52:04

Thank you.

52:34

Thank you.

53:04

Thank you.

53:34

Thank you.

54:04

Thank you.

54:34

Thank you.

55:04

Thank you.

55:34

Thank you

56:04

Thank you

56:34

Thank you

57:04

Thank you

57:34

Thank you

58:04

So guys, the runtime I have restarted.

58:07

so the library the package installs basically basically take a lot of

58:10

take a lot of time just restarting just restarting the library the package installs basically take a lot of time just restarting the runtime here once again.

58:15

Let us see.

58:18

Initial Langchain packages take a tremendous amount of time.

58:21

So now it is set.

58:23

I will quickly instantiate the API key.

58:33

And this is basically the packages, all if you can see. Everybody has already seen this before.

58:41

So first part, what are we doing? First part, we are going ahead and we are downloading the PDF file. We are taking the PDF file.

58:50

This is that particular PDF file we are taking.

58:53

Oh, okay, sorry, my mistake. I took the ABB demo. I should have uploaded the PDF instead.

58:59

So first thing, what I should do is I have uploaded the PDF instead.

59:02

I will I will load the PDF file. I'll use the PDF load the PDF load the PDF file.

59:10

That's the first part and after that we will do chunking.

59:13

This is what I was mentioning.

59:14

So what we are actually doing is we are effectively using a recursive text splitter chunker.

59:20

This is like a fixed size chunking and we are saying every chunk is 512 characters in size.

59:25

So every 512 characters you are basically creating a chunk.

59:28

Every 512 characters is a chunk.

59:31

Two sort of 512 characters another chunk.

59:33

Another next 512 characters another chunk like that.

59:37

Okay.

59:38

So we are doing that and overall in this document we have got total a thousand or chunks.

59:44

We'll see that.

59:44

Okay.

59:44

Let us, let us complete the chunky.

59:47

So this is usually going to take a tremendous amount of time and this is the fixed size chunking that we are doing.

59:52

Just on the same lines, I want to also talk about another kind of chunking that is very common.

59:57

And it is quite popular, which is called semantic chunking.

1:0:00

Right?

1:0:01

What is semantic chunking?

1:0:04

See, guys, fixed size chunking, what is the problem?

1:0:06

Like, this is a very nice and a very basic approach, right?

1:0:11

Fixed size chunking is a very basic approach.

1:0:14

If you see, this is pretty much what fixed size chunking is, right?

1:0:16

You have got a text here.

1:0:18

And all that you're doing is you're saying, hey, the first 512 characters is chunk one.

1:0:22

The next 512 characters is chunk 2 and so and so forth.

1:0:26

So these are happening in contiguous sections, right?

1:0:29

But if you try to understand the meaning,

1:0:31

of a chunk? What is the chunk? A chunk is supposed to be a particular idea. A chunk is supposed to be a particular

1:0:37

idea, a chunk is supposed to be a particular section of the text that gives you some idea about

1:0:46

that text, right? It should be about a particular theme. But right now, it is not a theme-based chunking

1:0:52

we are doing. It's just a normal contiguous chunking we are doing. But wouldn't it be incredible?

1:0:59

If I can create these chunks on the basis of similar text, and that is what is referred to as semantic chunking.

1:1:07

So this is like a normal recursive text liter we used, right?

1:1:10

This is the recursive chunking we did.

1:1:13

A similar kind of chunking, a better way to do chunking will be called semantic chunking.

1:1:18

And all that we do in a semantic chunking is that we take the document, it's very nicely explained in this medium article.

1:1:24

Let me bring this link to all of you.

1:1:26

It is very nicely pinged here.

1:1:28

what we do is we take a particular document and we try to find out what are the different

1:1:33

different sentences in that document.

1:1:36

Sentences, how can try to find out the full stops.

1:1:40

Wherever you see a full stop is a sentence.

1:1:42

The first of full stop, another sentence.

1:1:43

The first of full stop another sentence.

1:1:45

So you can go through all the sentences that we have in the document.

1:1:50

And then out of all the sentences that you have, you can try to find out which are the similar

1:1:54

sentences.

1:1:55

Remember, guys, machines don't understand text.

1:1:58

After documents and sentences, there can be, there'll be like millions of sentences you will have.

1:2:03

It's a very, very computational intensive thing, by the way.

1:2:06

Let me tell you.

1:2:06

Semantic chunking is extremely computational intensive.

1:2:09

This is simple.

1:2:10

This may be time.

1:2:11

You could have seen it took some time.

1:2:13

I mean, it took at least 20, 30 seconds to still figure out the chunks.

1:2:18

It took some time, right?

1:2:19

It's not just.

1:2:20

But imagine the amount of time it will take for semantic chunking.

1:2:23

And this was a small document, hardly a few hundred pages.

1:2:25

That's a.

1:2:27

Semantic chunk will be much more.

1:2:28

costume. Okay. But it will be a lot richer and a much better way of chunking compared to

1:2:34

fixed size chunking, what we are doing before. Right. So here, you take the document,

1:2:38

divide that into six sentences. Is it a six sentences that you have? What's that?

1:2:46

Yeah. Divide the chunk into six sentences. And you take each and every one of the

1:2:53

respective sentences and you create embeddings. So sentence one, embedding, sentence one, embedding,

1:2:58

two embedding, sentence three embedding, sentence four embedding. What is an embedding? Embating is

1:3:03

going to tell you the meaning of that sentence. So sentence embedding will somehow tell you the

1:3:07

contextual or the semantic meaning of that sentence. So once I have those embeddings for all the

1:3:13

sentences in the document, now I will start to group the similar sentences together. And the group of all

1:3:22

the similar sentences will be part of a chunk. Group of another set of similar sentences will be part of another

1:3:27

chunk. Group of another set of sentences will be part of another chunk. The main

1:3:32

benefit of this approach would be that it is not continuous. Let's say you, you're talking about

1:3:40

leaves. You have your HR document. I was talking about the HR manual, right? HR PDF. And HR PDF will

1:3:47

consist of many themes, many ideas. It will talk about leaves, compensation policy, termination policy,

1:3:55

resignation policy, you know, joining policy, joining formality. There are hundreds of things,

1:4:01

pressures, experience, laterals, directors, across different roles,

1:4:05

what what happens, everything will be documented, right? Food policy, whatever. So when you create

1:4:13

the chance, and if you think about it, this won't be like one PDF, it'll be like thousands

1:4:19

of different PDFs or text files, the HR department will have, right? And if you do fix-size

1:4:25

chunking, what, what's saying ain't because if you look at a concept of leaves,

1:4:34

leaves can be talked about in a particular page, leaves can also be talked about in page number 70

1:4:40

and leaves can also be talked about in page number 90. So, allot, other leaves are talked about.

1:4:47

But the moment I do semantic chunking, the best part is that I will end up having one particular chunk

1:4:52

chunk where I only have information about leaves.

1:4:55

So here all sentences, what leaves-related sentences.

1:5:00

So this becomes a more efficient thing. So we are basically creating chunks based on different

1:5:04

themes. So initial part will be very costly. This will take a lot of time. And as I told you,

1:5:13

creating the embeddings and the chunking will take a lot of time. What is the benefit? You can question

1:5:17

me then, sign, why are we even doing this? What is the benefit? The main benefit is retrieval

1:5:21

quality. Because if your vector D.B quality is good. If you're a vector DB quality is good. If you're

1:5:25

chunks are good. If your chunks, every chunk is conveying different themes, if your chunks

1:5:30

are good, next time I ask any question, like, please tell me what is the leaf policy, I will be able

1:5:35

to very accurately retrieve the relevant chunk. And the other major benefit of semantic chunking

1:5:42

would be you can retrieve lesser number of chunks and answer questions. In a normal approach that we

1:5:49

discussed here, if you remember in the demo, we retrieved top five chunks. So we had to retrieve more

1:5:54

chance because if I'm asking about leaves, the answer can be present across multiple

1:5:58

pages, right? But if I am doing semantic chunking, my answer is present only in one chunk or two

1:6:05

chunks. So during the retrieval phase, I can retrieve lesser number of chunks. And I will still

1:6:12

get more accurate answers. So these are the benefits of semantic chunking. So semantic chunking is actually

1:6:17

a very, very popular industry standard. And you can see this is again very nicely highlighted. You

1:6:22

then all give it a glance. This is very nicely described semantic chunking here for

1:6:27

everybody, which I'll ping you on the chat as well. Updek sat you, all of you can see. And it

1:6:32

pretty much summarizes everything about semantic chunking. It involves taking the embeddings of every

1:6:37

sentence in the document, comparing the similarity of all the sentences with each other and then

1:6:42

grouping sentences with the similar embeddings together. You're just trying to group similar

1:6:46

sentences together out of millions and millions of sentences that you might be honest. You can imagine

1:6:51

and how much of computation is required for this to happen.

1:6:54

I just wanted to make you aware of what is semantic chunking.

1:6:56

But yes, as I told you, the computation is only during the initial.

1:7:01

No, no, no, no, Ali, there is no concept of overlap. There is no concept of overlap. Okay.

1:7:06

There is no concept of overlap. But then it will be more accurate. It's much more accurate

1:7:09

method. And also the best thing is that it will improve your retrieval quality.

1:7:13

In real world production use cases, we use this a lot. We use this a lot. And as I say,

1:7:19

it's a top not choice when the maintaining the semantic integrity is vital.

1:7:23

And the best thing is that you can, you can retrieve lesser number of chunks and still get answers to questions.

1:7:27

It's very simple to implement. If you want to see the implementation,

1:7:30

so recursive to have already here. This is already part of my code demo.

1:7:34

Recursive character text glitter, which I already showed you. But if you want to do semantic chunking,

1:7:38

the code is very simple. You can just scroll down in the same notebook. They have given a small example

1:7:43

for semantic chunking. This is what it is. There is semantic chunker, one line of code. That's it.

1:7:49

The same way, the same, uh, Langchain experimental text glitter is.

1:7:53

You're corrective.

1:7:53

You're going to say. So everything else will be very, very similar.

1:7:58

You go all the way up here.

1:7:59

If you remember the import, so whatever import I did, right?

1:8:03

Here I had a recursive character text glitter, right?

1:8:06

Langchain text glitter I had, right?

1:8:08

I had recursive. I can simply put semantic chunker right.

1:8:11

Here on semantic chunker you can actually put.

1:8:15

Okay.

1:8:17

So this is about semantic chunking that I want.

1:8:19

to discuss with on a few briefly. Anyways, coming back to the use case once again,

1:8:23

I have created the chunks and here onwards, everything will be the same, be semantic, be whatever.

1:8:29

So everything will be the same after this. Now we will create the vector db. This is a vector db

1:8:34

I'll be creating. I'll take the chunks and convert them into embeddings and I will create

1:8:38

the vector db. And then I will just quickly test my vector db right now. I will define the retriever.

1:8:45

I will instantiate and define the retriever right now that, okay, please retrieve it.

1:8:49

the top five similar chunks. Okay, I will instantiate and define the retriever.

1:8:53

Please, please define the top five. Please define the top five similar chunks.

1:9:00

I will instantiate and define the retriever right now.

1:9:19

Thank you.

1:9:49

You can see the amount of time it takes to create the chroma db because you've got all these chunks and it is trying to generate the embeddings and create the vector db.

1:9:58

This process usually will take a lot of time.

1:10:00

So there are so many points of failure.

1:10:01

This is the point of failure.

1:10:02

If you don't get your chunking right, then eventually, you know, this will be a very important factor.

1:10:08

So if at all you see that your rag system is not giving the right answers.

1:10:12

You have to question all this.

1:10:14

Maybe your chunking is not right.

1:10:15

Maybe go back to semantic chunk, but do the chunking differently.

1:10:17

Now chunks, keep, say, create. Second point of failure will be the embedding model.

1:10:22

Maybe the embedding model that you've used is not right. You need to use a more powerful embedding model.

1:10:27

Right. So the embedding model that we are using right now is GTE large. This is the one that is

1:10:32

responsible for taking those chunks and converting them into numbers. Now you can experiment with

1:10:38

different embedding models because that is what is taking that chunk of text and converting that into

1:10:45

numbers which is conveying the meaning of the text. So if that embedding model is a problem,

1:10:51

yeah, be a point of failure. I'm just trying to talk about the different points of failure.

1:10:55

The vector db itself is also a very important part. How you're managing it, how you're indexing it.

1:11:00

What kind of metadata you are putting there. So I'll talk a little bit about that in a while.

1:11:05

So you need to manage your vector db also corrective. So you can have a scenario where new

1:11:11

documents are getting uploaded. Some documents are getting removed. Some are getting updated.

1:11:15

So that vector DB will also be in a state of constant term.

1:11:18

Like some of the operations we saw in chroma DB before, absurd and all.

1:11:21

So similar way you will do it. So somebody, this is actually not going to be a core gen AI role,

1:11:25

but somebody will have to take care of that administration also.

1:11:28

Because if the vector DB is not maintained correctly, then everything downstream will be incorrect.

1:11:34

Now it's how many LLM is good and all that.

1:11:37

If the vector DB is not managed properly, if you're having stale data, if the data is not getting updated,

1:11:43

let's say, mano HR policy. And the HR policy is, and the HR policy.

1:11:45

Let's say, every week some new policies are coming and every week some new, some policies are getting

1:11:51

deprecated. Let's say, 10-year-year-year-old was H-R leave policy. So that already

1:11:56

company has it. But are you ensuring that you go back to the vector DB, find out those corresponding

1:12:02

chunks, and you remove it. So these are again things that you need to keep in mind. So this is another

1:12:06

point of failure. I'm just trying to talk about the different points of failure. All this while,

1:12:10

it was just about the language model land. But if your RAG system is giving a wrong answer to.

1:12:15

these are all the things you will have to question.

1:12:17

The quality of my chunking, the kind of embedding model I use, and how I'm managing my vector DB.

1:12:23

Another very important point is the retriever.

1:12:25

How many chunks you are trying to retrieve?

1:12:27

It's how much chunks have retrieved. Should you retrieve one chunk?

1:12:30

Should you retrieve 10 chunks?

1:12:31

That is also an important point to highlight.

1:12:33

Remember, guys, if you retrieve too many chunks, what is the issue?

1:12:38

What is the issue if you retrieve too many chunks?

1:12:40

If you retrieve too many chunks, then I think the whole purpose of rags is

1:12:44

like, you know, there's no point in doing rags anymore, right?

1:12:49

If you're retrieving, let's say, imagine you have a hundred page.

1:12:53

Yeah, API tokens, right, you brought.

1:12:55

Now if you say, okay, okay, so I will retrieve 110,000 chunks.

1:12:59

So, so rag is why do you can take that whole document as a context and you can give?

1:13:03

So we should not retrieve too many chunks and we should not retrieve too few chunks.

1:13:09

If you only retrieve one chunk, then also it's a problem.

1:13:12

Then you will not have enough information.

1:13:13

So it's a trade off.

1:13:14

Even that is a very, very important factor.

1:13:17

How many chunks you will retrieve?

1:13:18

What is the right number of chunks to retrieve?

1:13:20

And the interesting part is there is no answer to that question.

1:13:24

You will not know that.

1:13:25

Unless you evaluate.

1:13:27

I will teach you some evaluation method in a moment.

1:13:29

Okay, what, how to evaluate.

1:13:30

But unless you evaluate your right system,

1:13:32

up for not know how to tell you all these aspects that I'm talking about,

1:13:35

are you doing the chunking right?

1:13:37

Are you doing the embedding right?

1:13:39

Is your vector DB right?

1:13:40

Are you retrieving the right number of chunks?

1:13:43

None of this you will get to know.

1:13:44

unless you're evaluating the rag response.

1:13:47

So that is one of the most important things in anything I would say,

1:13:50

which we'll see how to do it.

1:13:53

Because, yeah, very important.

1:13:54

So you should have a very good idea how many chunks you're retrieving.

1:13:57

And as I told you, if here you're using a semantic chunker,

1:14:00

if you're doing semantic chunking, then you can retrieve lesser number of chunks.

1:14:04

Because those chunks that you're retrieving are high quality.

1:14:07

High quality chunks are retrieving.

1:14:09

So you can do with lesser number of chunks.

1:14:10

So most likely if you're asking some question,

1:14:13

the answer to the answer to the.

1:14:14

the question will be present in some of the chunks.

1:14:17

Okay, so in fewer chunks, it would be present.

1:14:19

Ah, that is right. That is right. That is right.

1:14:22

Absolutely, right, you're right. And once that is there, let me move on.

1:14:26

Let me move on with the code flow as well.

1:14:28

If you can, so yeah, to vector DB creation for go.

1:14:30

Retrieval, I will just quickly test. This is the very technical question I'm asking.

1:14:33

My ACS 880 drive just stripped with fault code 2310. What does this mean and what should I check?

1:14:40

This is the kind of question a technician at ABB will be asking from the ABB manual.

1:14:44

It's a very real world manual we have taken.

1:14:46

And you can see it will go to the vector dv and it will retrieve the top five chunks.

1:14:51

The top five chunks potentially where the answer is present.

1:14:54

So that is the way how it will do.

1:14:56

Next, I will now integrate this into the complete rag system.

1:15:02

Let us see that.

1:15:03

This is my rag, you and A.

1:15:04

You are an assistant who answers questions.

1:15:06

So your rag user message is context and question and this is the user input.

1:15:11

You delete the five document chunks and, and

1:15:14

if user asks this kind of a question, you will get the answer.

1:15:17

Yeah, your answer is. This rag system will generate the answer.

1:15:21

You can see it is, so next time I ask the question, how do I change motor control mode to

1:15:24

scalar on the ACS 880?

1:15:27

Now you'll have to go through the document and see.

1:15:30

But a rag system will go through that entire document, find out the relevant chunks, and it has

1:15:34

given me a very, very nice answer. Set the parameter of this to this.

1:15:38

That's it. This is the way how the rag system is working.

1:15:40

So this is the final part, which is the retrieval part.

1:15:43

So based on the question, retreat the context, and now the LLM will answer based on the context.

1:15:52

Ali, when I say it is costly, very good question, very good question.

1:15:55

Ali has a question.

1:15:56

I think others are not able to see your question.

1:15:59

Would you mind posting that to everyone, Alu?

1:16:01

You have asked a very good question.

1:16:03

Chat settings to everyone for post.

1:16:05

You have asked a very good question.

1:16:06

I just wanted everyone to see your question and then I will answer it.

1:16:10

I will but everyone to post for all of me.

1:16:13

Ali?

1:16:32

Okay. So I'll just post Ali's question for all of you. Okay. Okay. So I'll just post Ali's question for all of you. Okay. This is what Ali asked. Okay. Allie asked, okay. Okay. Okay. Anyway, I also posted parallelly.

1:16:42

Okay. So Ali has asked a very good question. He's saying, he said, sir, semantic chunking being, what is that?

1:16:50

costly? Yeah, costly. So what does it mean that it is costly? When I said semantic chunking is costly,

1:17:01

when I was explaining semantic chunking, I was telling you it is costly. When I say costly, I meant it is going to take a lot of time, not money.

1:17:08

Money and see, so what is.

1:17:12

What is semantic chunking? How are you doing it?

1:17:15

You first, you understand how are you doing it?

1:17:19

You are doing it on your local machine.

1:17:22

Chunking usually will completely happen on premise here.

1:17:27

There is no API calls and all that you are doing just to let you know.

1:17:31

Because this is with your very, very sensitive company data that you're doing it.

1:17:35

Right? You have a PDF or your sensitive document data.

1:17:38

You're, you're doing. You're your chunking car. You're on it. You're just on it's chunking car.

1:17:41

So semantic chunking is.

1:17:42

will also happen on this completely on premise in your company servers.

1:17:48

So, Ali, if you're asking, by money and cost, I mean to say, that token usage, answer is no.

1:17:55

Here, there's no LLM call.

1:17:56

No.

1:17:56

By the level.

1:17:58

Semantic chunking, if you want to say, it is basically happening through an embedding model.

1:18:04

The same way that we are using an embedding model to take a query and convert it into embeddings,

1:18:09

the idea of semantic chunking is exactly the same.

1:18:12

You are taking.

1:18:12

every single sentence, you're converting that to embeddings and then you're comparing similar sentences, right?

1:18:17

So at its code is an embedding model.

1:18:20

Or the embedding model can't where from are that embedding model is something that you're downloading

1:18:24

locally.

1:18:25

You are downloading locally.

1:18:26

They say, if you remember, this is what it is.

1:18:28

You have an embedding model.

1:18:29

The same kind of embedding model that you are downloading locally on your system, on your servers.

1:18:35

That is what is used to do the semantic chunk.

1:18:38

So when I say it will be costly, I meant it.

1:18:42

It will be costly on your server infrastructure because this is your server, right?

1:18:46

This is your company, your premises, not costly in terms of tokens, but costly in terms of your

1:18:51

computation, your resources and also the time.

1:18:53

I hope that answers.

1:18:55

But this will entirely happen on premise.

1:18:57

The vector db chunking, all this will happen on premise.

1:19:00

But remember, this is a one-time activity.

1:19:02

Yeah, one-time activity.

1:19:04

Obviously, there will be a maintenance that you will have to do, as I told you that if any

1:19:08

updates and changes happen to the original documents, you need to update your vector db,

1:19:12

there will be changes that will happen, but usually this will be one time.

1:19:16

Inference time, users will just ask a question.

1:19:19

That vector div be been made.

1:19:21

There's a retrieval-hung, answer will be something very similar to what you are demonstrating here.

1:19:26

What I wanted to demonstrate you here.

1:19:28

This is inference time.

1:19:29

So when we say inference-me, what is happening,

1:19:32

inference-me, this is something that will happen.

1:19:34

Like that Gradio example that we saw in the class, right?

1:19:37

Let me just run this finally for you.

1:19:42

you can see this one.

1:19:45

This is a small radio application that I'm building.

1:19:48

And this is the kind of thing that you are, uh, uh, uh, uh, what's that?

1:19:53

Uh, let me show. Let us see.

1:19:56

Goode gradio.

1:19:57

Can not import, you know, that's interesting.

1:20:12

We want to be one second place.

1:20:42

Thank you.

1:21:12

Thank you.

1:21:14

Thank you.

1:21:44

I think some of the run time actually

1:21:56

that's the reason why it's the reason why

1:21:58

it's not going to get installed most likely.

1:22:01

I'm just going to quickly uh,

1:22:04

restart the runtime and do the second.

1:22:05

Just a second, guys.

1:22:14

Ali, I hope that answers your question in the meantime.

1:22:24

I hope that is clear with you.

1:22:44

Thank you.

1:23:14

Thank you.

1:23:44

Thank you.

1:24:14

Thank you.

1:24:44

Thank you.

1:25:14

Thank you.

1:25:44

Thank you.

1:26:14

So one of the thing that

1:26:25

which I was which I was, which I was just trying to resolve here,

1:26:28

if you see, if you see, uh, just at the grade of our rest is all fine, rest is all the

1:26:34

all the normal thing that we have talked about.

1:26:35

I was just trying to execute this for you.

1:26:37

So Gradioca push library made there are some changes that happened actually.

1:26:40

So I was just trying to update the radio package.

1:26:42

This was working fine in.

1:26:43

fine in the last demo, which we did. We were just doing PIP install radio and it works.

1:26:47

So it turns out that there is some dependency issue that is happening right now. I'm just updating

1:26:54

that. And with that, hopefully, it should be working. But that's okay. I don't want to like get

1:26:59

a bit. It's just the final radio part that we have here. But I hope everybody, everybody at a high level,

1:27:05

you understood the big picture idea. So the radio part is nothing but that front end user interface,

1:27:10

where end user is asking a question and on the basis.

1:27:13

of that, the rack system will retrieve the chance and generate the answer.

1:27:17

And the important thing I wanted to highlight here is that when you talk about that final,

1:27:23

that final evaluation, that final thing, during inference, inference is actually quite fast.

1:27:30

So this entire thing is a one-time process, but when end user is asking a question,

1:27:35

you're retrieving chance and getting unanswered, that is usually a, like, that's going to be pretty fast fairly.

1:27:40

Right.

1:27:41

Now let's go on, let's move on here.

1:27:43

And what I will do now is I'll talk a little bit about the aspect of, I will talk a little bit about the aspect of, I will talk a little bit about the aspect of, okay? Just give me one minute because I'll be sharing this forward with you.

1:27:58

I don't want to mess it up. Let me just have the same gridio install. Okay.

1:28:05

Ah, okay. Ankit, um, embedding models are different from actual models.

1:28:11

correct. Yes. Not can be. It is different. It is different because the LLMs cannot be used as embedding models. Remember with that. Okay. So think of a topic. The normal large language models show he. The large language models cannot be used as embedding models. Okay. So that is just one thing to keep in mind. The normal LLMs cannot be used as embedding models.

1:28:37

Okay. Now let's come to the

1:28:40

let's quickly come back to the evaluation part. What I want to do is

1:28:54

come back to the evaluation part and talk about how the evaluation is happening, particularly here.

1:29:04

And let's understand the idea of evaluation. How do we evaluate a right system?

1:29:10

When we talk about a rag system, what are the different ways we can evaluate a rag system?

1:29:14

Because that's the most important part.

1:29:16

So, guys, there are two broad methods I'm showing you right now.

1:29:22

So this is pretty much what the rag has been. You ask a question, language model will, like, you give the question, you give the context and the element will give an answer.

1:29:31

This is pretty much the rag that we talked about. Now, how do we evaluate the response the rag is giving?

1:29:38

Turns out, there is another LLNLM.

1:29:40

that we will be using. This is what is called LLN as a judge. What is it? What is the term that we use right now? We call it LLM as a judge. It's a very, very common methodology that is used in practice. LLM as a judge that we used to evaluate a rag application. And there are two judges we will use right now. We will use a groundedness judge and we will use a relevance judge. These are the two judges that we are using right now. So again, the first language model is giving us.

1:30:10

the usual rag response. And there will be a second large language model that will act as a judge.

1:30:19

There will be a second large language model that will act as a judge. And there will be two judges we'll be having.

1:30:25

So for example, we will have a groundedness judge and we will have a relevant judge. Groundedness judge gone over.

1:30:33

Groundedness judge is that judge who will check is the response supported by the retrieved context.

1:30:40

That means whatever answer the rag application is giving, whatever answer the rag application is giving, the groundedness judge.

1:30:52

Groundedness for what is the amountedness? What does groundedness even mean?

1:30:57

Groundedness means that whatever answer we are getting is that answer supported by the retreated context.

1:31:07

That is what the groundedness judge will tell you.

1:31:10

whatever answer we are getting is that answer supported by the retrieved context.

1:31:21

And that is important, right? Because rag system's idea to the way. I, the answer to the question cannot come from anywhere else. The answer to the question must come from the retreat context. I think whatever PDF and whatever manuals are there, the answer to the question must come from. The answer to the question must not come from somewhere else.

1:31:40

So that is groundedness for you.

1:31:44

And relevance will be another judge. That mean, these, both of these will be LLMs, right?

1:31:49

That means here we will do our LLM call.

1:31:51

Yeah, an LLM hoga.

1:31:53

And I will write it, write a system message to evaluate how the first LLM performed.

1:31:58

It is almost like a competition, right?

1:31:59

Imagine you go to some competition, right?

1:32:02

A song competition, dance competition, you know, shark hang.

1:32:05

What happens is there is one performer who is performing, right?

1:32:10

And then there is a competition.

1:32:10

judge who is rating that performer on a scale of 1 to 5.

1:32:15

Yeah, idea of SIO. So the first language model will look at the user question and give a response.

1:32:23

But this, what is going to evaluate this guy? So there'll be a judge.

1:32:28

Two judges will be a ground and this judge. And second, there'll be a relevant judge.

1:32:34

Both LLM calls over. So the groundedness judge will check that whatever answer,

1:32:40

you gave, the first guy gave, is that answer coming from the manual?

1:32:46

Is that answer coming from the retreat context?

1:32:48

But the whatever PDF manual we gave you, is that answer coming from that.

1:32:52

And the relevance judge will check, will check is the response relevant to the query given the context.

1:32:59

That means, you know, it's like saying, if I ask you, what is the annual revenue of Tesla?

1:33:04

The answer should be revenue. The answer should not be profit.

1:33:07

If I ask you the question, what is the annual revenue of Tesla?

1:33:13

The answer should be revenue. The answer should not be profit.

1:33:17

The answer should be revenue. The answer should not be profit.

1:33:19

What is the annual revenue? It should be revenue. It should not be profit.

1:33:23

But the relevance will check that. Relevance will check is a response relevant to the query given the context.

1:33:28

So given the context, are we, you know, so, so I'm asking a question about revenue. Are you answering revenue?

1:33:34

I want you to answer it correctly.

1:33:37

So this is the concept of evaluation, right?

1:33:40

Groundedness and relevance.

1:33:41

Let us see the implementation right now.

1:33:43

How do we do it?

1:33:44

So this is the same demo that we have right now and this is the evaluation part.

1:33:48

See, let us now use the LLM as a judge method to check the quality of the rag system on two parameters, retriever and generation.

1:33:57

We illustrate this evaluation based on the answers generated to the question from the previous section.

1:34:03

That means the previous LLN, the main ragged LLLLLLLLLLLLN, the main RRAG,

1:34:07

whatever answers it gave, we will use the answers and we will send it to a judge.

1:34:13

In fact, then we will send it to two judges and the judges will give a rating.

1:34:18

There is one more important thing I wanted to highlight here.

1:34:21

Usually, the judge models will be more powerful than the original model.

1:34:27

Means the first LLL, imagine if it's a, you know, a slightly cheaper model.

1:34:32

If the first model is a slightly cheaper model, the judge models are supposed to be more

1:34:36

more extensive. That is just one other thing you will have to keep in mind, which is obvious, right?

1:34:43

I mean, imagine if you're going to some competition and there's a participant and all that, right?

1:34:46

So, so, so typically the judge model should be more extensive.

1:34:52

Okay, so the judge model should be, you know, think of it like they should be, they should be,

1:34:57

you know, comparatively much more, much more knowledgeable. The judge is supposed to be more knowledgeable and more

1:35:06

intelligent than the first LNM. So the judge model should be better models.

1:35:12

So now let us see the groundedness prompt. This is the groundedness rate our system message.

1:35:16

So what are we seeing right now? This is the groundedness LLM. And what is this is a system message for

1:35:22

the groundedness LLM. Right? So this is the groundedness LLM. So every LLM should have a system

1:35:28

message, right? The LLM call should have a system message. So this is how the system message will do.

1:35:33

You are tasked with rating AI generated.

1:35:36

answers to questions posed by users. So it is like, you know, even judges will have to be briefed, right?

1:35:41

Imagine if you are a judge going to evaluate some competition. You have to briefing

1:35:44

can't. Judge, just like, how will the judge know what to do, how to rate, what metrics and

1:35:51

what are the things to see? And our rating, what state scale, one star, what is five star what is. How do I rate

1:35:58

people? So judges will also have to be briefed, right? So the system message is like the briefing sheet for a

1:36:03

judge. Whatever the judge models are, who the judge model is, how will this groundedness

1:36:08

judge model rate this guy and how will the relevant judge model rate this guy? So this system

1:36:13

message is a briefing sheet for that. And this is a very popular approach which enterprises use

1:36:17

or not because it gives you a lot of control over how you want to configure it. A very important

1:36:23

template will be very very similar, but a very important part is this metric. The answer should only

1:36:29

should be derived only from the information provided in the context.

1:36:33

So you are you are explicitly briefing the judge. This is the system message of your judge.

1:36:38

You are explicitly briefing it. The answer to the question should be derived only from the information

1:36:45

present in the context. You are explicitly briefing it, explicitly specifying that right area.

1:36:53

I hope everybody is aligned on this. And you can see that how we have defined the ratings

1:36:58

right now. The metric is not followed at all and 5 star means the metric is followed completely.

1:37:02

that means the answer is completely coming from the context, which is exactly what the

1:37:06

grounded is such to devalued. You're second one, look, relevant judge. Relevance judge is the second

1:37:11

judge and the system message for the relevance is very, very similar. You are telling it that

1:37:17

by what you will have, you, what you will have, you, what to give you. In the input, the question

1:37:22

will begin with the question. You have a question via jae. You have a context yeah and you answer

1:37:27

give. These are the three things the judge will get.

1:37:29

judge will get the question, context and answer. I think a better diagram will be this one. I think

1:37:34

this will give you another far better idea what's going on. So you can see the first LLM is the normal

1:37:39

rag, right? User asks the question based on the retrieved context, you are generating the answer.

1:37:45

This is the first rack system, right? You can see the inputs are user message and this thing,

1:37:50

user query and context. The judge model will take the user input. It will take the retrieved context and it will

1:37:58

also take the generated response. It's what the judgment. Judge has to know. If you're

1:38:04

a judge, you know, who is evaluating something, case, who is just so everything. Just so everything. Just

1:38:07

just has to know, okay, what was the question that was asked? Tell me what contact was

1:38:12

retreat and also tell me what the other guy answered, what the first guy answered. Based on that,

1:38:17

I will give a quality score on 1 to 5. So this is what LNM as a judge concept basically stands for.

1:38:23

Okay? So now let us see. I will define my relevance rate and message. This is already part of

1:38:28

of your demo file. It's already have it. And this is the user message template,

1:38:32

question, question, question, and answer. And now I will ask this question. You can ask the specific

1:38:37

question right now. Let me go and ask the same question. How do I change the motor control

1:38:43

mode through scanner on the ACS 880? Because our manual ACS 880 guy, right? We have that ACS 880 manual

1:38:49

today. If I ask this specific question, let me ask this. It will retrieve the relevant chance.

1:38:56

A retriever is not defined. I think the same nonsense.

1:38:58

But I restarted the session, that's why.

1:39:02

Again, let me do that.

1:39:07

I'll just initialize the thing. Just quick to put me.

1:39:28

Thank you.

1:39:58

Thank you.

1:40:28

Just

1:40:35

Just give it a minute, guys. I'm just trying to run.

1:40:58

you're able to see the results. Okay. It's running up. Just trying to

1:41:03

reach start the session and then once again do it. So because of this error, I actually deleted

1:41:10

the runtime and did again. So that's why, you know, like none of these things were saved. That was the

1:41:16

problem. That's okay. No problem. We can just do it again. So here I will instantiate the retriever.

1:41:21

Rest is all fine. Rest I think it will work fine now. Now I ask the question. I can just quickly go ahead

1:41:26

and check the retrieve chunks.

1:41:28

is good. All is good now. So we can instantiate the model. It's all fine now. This is all

1:41:35

fine now. And the normal drag is working fine. Let's see. All is fine. So the client I will quickly

1:41:44

instantiate here. Client part was not done. And this is the normal drag response. So I can just run this

1:41:57

query and you'll be able to see based on the question, we are able to retrieve the chunks and

1:42:01

the first LLM is able to generate the response. So we saw that, right? Set parameter,

1:42:05

control, model, whatever it is. We have seen that. Now coming to the evaluation part. Okay,

1:42:10

groundedness system message, a relevant system message. This is the system message for the judge

1:42:16

model, which we are able to see. And now this is the user message template. There goes the user message

1:42:23

template. I will ask this question.

1:42:27

retrieve the relevant chunks and this is the prompt for your prompt for the grounded

1:42:34

not the first answer the rag answer and now this you will send to the judge the grounded this judge

1:42:41

and you can see the groundedness judge will evaluate it will it will it will go and evaluate it

1:42:46

the groundedness judge will go and evaluate it and it will give a response it will give a star rating

1:42:52

let us see that it will it's it has given a score of five star but so whatever original question

1:42:57

asked the ground and this judge actually evaluated it or what

1:43:01

the things that checked steps to evaluate against the metric you can see it

1:43:05

that actually did that entire thing step by step and it said okay the question asked how to

1:43:10

the motor control to that the context of retrieve here here and

1:43:15

based on that the judge is checking yes the answer is fully derived from the provided

1:43:19

context and directly answers the user question using only contextual information so i

1:43:25

I will give a five star. So the groundedness is giving me a five star.

1:43:28

Similarly, I will check the relevance.

1:43:31

Relevance just like the answer are check. Relevant judge is also giving me five star.

1:43:36

So that makes me very confident my rag application is working fine. So this is a very,

1:43:40

very important metric I wanted to talk about. Now this is in real world, it will not just be based on

1:43:45

a single question. You're evaluation. That means you will you will frame a series of

1:43:51

50 hundred different different questions across different topics.

1:43:54

and you will ask the RAG system to answer those 50 hundred different questions and then you

1:44:00

will ask the judge model, LLL as a judge model to, you know, give a rating for on the groundedness

1:44:06

parameter, give a rating on the relevance parameter. So 50 questions

1:44:10

relevance course are either, 50 questions got groundedness course is how grounded the responses were

1:44:16

and then you can take an average of that. So this is the way how in practice we go and, you know,

1:44:21

we go and evaluate the RAG application. We take an average.

1:44:24

average rating.

1:44:25

Ah, absolutely. Absolutely. This is not going to happen in query time.

1:44:28

Whatever I'm talking about, evaluation will happen during the development time.

1:44:32

This is happening during the development of the RAG application.

1:44:36

And this is exactly what will help you. Like for example, see, if I had got a low rating,

1:44:42

if I had got a lower score from a judge, that means this is something that I will use to further work on

1:44:48

my application. Maybe something was wrong.

1:44:51

Yeah, so chunking was wrong, yet to embedding was wrong, or I retrieving was wrong.

1:44:54

lesser chunks. So anything could have been wrong. So this is what I'm doing at the

1:44:59

development phase. So definitely it is one time during the development phase. While developing

1:45:04

the Rang application, while developing all these components, what chunking can. I was talking about

1:45:08

semantic. Now, now try to. Now, now fix size

1:45:11

number one, judge's rating check for. Second, you're semantic for. Chunking, you change the chunking

1:45:17

strategy. Do semantic. Then check the judge ratings. Whichever case the judge is rating more,

1:45:21

that will tell you, that will tell you, maybe that's second.

1:45:24

approach is better. So this other developer you will be doing. Okay. But definitely once you

1:45:29

have finalized the complete pipeline of Chunker, embedding model, all of these kinds of things,

1:45:35

once you have finalized the entire thing, during inference time, during actual users when they are

1:45:42

using it, judge is not getting used. Okay. They are judges used. I would say, say, I would not say

1:45:49

that judge is not getting used. I would rather say the judge is getting used in a very small sample of

1:45:54

responses. Very small sample of responses judges getting used. See, I mean, if you, if you see from

1:46:01

that scenario, even chat GPT, like if you go to chat GPT,

1:46:06

chat GPT, like we don't get to realize this, but have you ever wondered? Next time you ask a certain

1:46:13

question to chat GPT. You hit an enter and you get a response, right? So basically the story is like

1:46:21

you write a query and you get a response. But have you ever wondered who is evaluating

1:46:25

these responses? Have you ever wondered? Who is evaluating? How's evaluate it? If you think

1:46:32

somebody at Open AI is monitoring every single messages that billions of users across the world

1:46:37

are typing? There is a judge model that they are also using. They're using a different kind of

1:46:43

judge with their own system message. Our rag judge was different. We focused on, we focused on

1:46:48

grounded less and relevance as the criteria. Open AI can't have. So open AI, what they will

1:46:54

do? This is happening during runtime. Run time, billions of requests are being sent to chat GPD

1:47:01

every day. Open AI is taking a very small percentage of those requests. It's taking, let's say,

1:47:06

0.0001% of the different, different requests from different, different geographical regions across the

1:47:12

world. That's all right request lay right. It's taking all these query responses and it is sending it to a judge.

1:47:18

it is sending it to a judge LLN. There is one, not one judge, but there are several judges

1:47:25

which are evaluating the responses based on several parameters. So chat GPT's a

1:47:31

parameters. So because OpenEI also wants to know, how is the application doing? How are users liking it?

1:47:38

You know, based on certain questions is the application giving the kind of responses we expect.

1:47:43

Right? So that is how you will frame your judges. So just like here,

1:47:48

we had a groundedness judge and we had a relevant judge. Similarly, in the case of chat GPT,

1:47:53

you will have different, different judges. You will have a judge that will maybe, let's say,

1:47:57

evaluate the tone of the conversation, evaluate how correct the responses, all these kinds of things.

1:48:01

Because I hope the idea is clear. So judges are there everywhere, just that we don't get to see it.

1:48:08

So chat GPT is also using judge modage to evaluate the quality of the application. And you have to

1:48:14

be rating like a concept item. You know, all the responses will be rated on a score of

1:48:18

scale of one to five. And at the end of the week, they said a leadership team of

1:48:22

opening I will see, okay, how is our chat GPT application performing week on week?

1:48:27

Our judge's scores what is the average score we are getting across all the responses.

1:48:32

And that will give an idea to you how the chat GPT application is working.

1:48:35

The only thing is that he will not have one judges, you will have several judges.

1:48:39

Now, if you want to know in real world what is going on,

1:48:42

a more level in chat GPT in. You know, you know, here up, thumbs down,

1:48:46

like Ali has two responses.

1:48:48

So all that is also incorporated.

1:48:50

Some user feedback is also incorporated.

1:48:52

So, sometimes you get a response, user gets a particular response,

1:48:56

and you get a chance to either do thumbs up or thumbs down.

1:48:59

So that will be feedback to judge's.

1:49:01

And finally, there is a small section of responses that also goes to human evaluators.

1:49:06

Human evaluators are, human evaluators are, human evaluators, so maybe one workflow that they are using.

1:49:11

So maybe one workflow that they are using is, first, judge LLM will evaluate.

1:49:16

He'll rate on a scale of one to pie.

1:49:18

And whichever responses are rated one,

1:49:21

jove responses, one year two rated, that means the responses are bad.

1:49:25

This will actually be sent to a human expert.

1:49:27

Open AI will have human experts, real human beings that they will be hiring,

1:49:32

who will literally see the chat GPT queries.

1:49:35

They will see chat GPT in, people can see queries.

1:49:39

So obviously there'll be security and all, you know, like the personal information of the accountant,

1:49:44

the person who is having the account will be hidden.

1:49:46

But yes, human evaluators are.

1:49:48

are actually seeing whatever you are you are typing in chat GPD.

1:49:52

This is the kind of workflow that really happens.

1:49:56

So question, answer, judge model, rating kareg, wherever the ratings are one and two,

1:50:01

wherever the judge says, the first language model will generate the response,

1:50:05

which is what the chat gpt model is doing.

1:50:07

And the second, and the judge model is evaluating those responses.

1:50:11

Wherever the judge says, the rating one year two, I will send it to a human evaluator for further review.

1:50:16

So, human one, evaluator, go back, that, okay, I mean, chat, GPT response, how's it?

1:50:22

So this is the feedback that these human evaluators will now get to the open AI development team.

1:50:28

But then back from that chat GPT co versions change, they will try to make some improvements in the application.

1:50:34

Okay, I hope you got a big picture overview into how things really work.

1:50:38

Because I wanted to take some rag aspects and connect to the real world.

1:50:40

Many applications in the real world, they work like this.

1:50:43

They are all using these judge models, okay?

1:50:46

Did you all understand the judge part?

1:50:51

Everybody's clear.

1:50:52

Yubraj, are you clear?

1:50:55

Ali, are you clear?

1:50:56

During the workshop I tested by storing, is that answered,

1:50:59

Yuvraj?

1:50:59

I'm just reading that question now and compared it to actual answers.

1:51:03

Is it, is it?

1:51:04

No, that's, no, actual answers, you're not.

1:51:07

Yeah, I got what you're saying.

1:51:08

I got what you're saying.

1:51:09

But basically, that is a scenario, Yubraj, where you are doing a human evaluation.

1:51:14

What you are asking, what you are saying, there is like a.

1:51:16

human evaluation.

1:51:18

And that is something that you will do only in a very small fraction of responses.

1:51:22

You cannot do it all the time.

1:51:24

You know, that will be very costly.

1:51:25

It's very difficult to, whether it is as good as like taking some sample questions and

1:51:29

going and manually checking.

1:51:31

Ah, to some extent you can do, but you cannot like do it at scale.

1:51:35

So at scale, you will have to use a judge model.

1:51:38

And then as I told you, like, whichever cases, judges are getting wrong, you can do a human

1:51:41

evaluation there.

1:51:44

So that is a ground growth, what you're referring to you.

1:51:46

You have some test data, ground proof data.

1:51:49

If you have you have ground proof data not, then you have to ask you to ask you.

1:51:52

And Yubra, I want to highlight one more thing.

1:51:55

Remember, getting the ground proof data is very costly.

1:51:58

That costly be costly.

1:51:59

You need to spend time.

1:52:02

You need to spend time.

1:52:02

You have to spend time.

1:52:03

It is quite literally saying that, you know, you have to go to this PDF.

1:52:11

You have to actually frame a series of 20 question answers.

1:52:15

That needs time.

1:52:16

that is effort.

1:52:17

You have to have a human being read the document and that human being will frame question answer.

1:52:23

like teacher question answer, you have to go and ask you go to question answer.

1:52:28

That's a whole document per-up.

1:52:29

Now you're asking a question.

1:52:31

Something.

1:52:31

I mean, I struggle going.

1:52:33

I will give it to you guys.

1:52:35

You will see how difficult it is.

1:52:37

And that's how human evaluation happens.

1:52:39

Human evaluation happens the same way.

1:52:42

They will typically hire people who will do exactly this one.

1:52:44

They will read a complete PDF.

1:52:46

And they will.

1:52:46

frame question answers.

1:52:48

They will frame that you,

1:52:50

you know, you can't ask you, correct?

1:52:54

That's a workaround.

1:52:57

That's a workaround, of course.

1:52:59

So, yeah, but I hope the idea is clear.

1:53:01

In fact, just to extend the conversation,

1:53:04

there is one more very interesting thing that we use in the real world called a

1:53:07

rag triad.

1:53:09

We have two aspects are seen.

1:53:11

We have discussed two aspects today in the class,

1:53:13

groundedness and relevance.

1:53:14

But just sometimes in interviews, they also also.

1:53:16

ask you a third metric. Just remember,

1:53:18

it is called a rag triad.

1:53:20

So this your rag triad.

1:53:22

Very simple, very, very, very easy thing.

1:53:24

Okay? So, your query is.

1:53:26

Your context, your response.

1:53:28

User asks the question. You retreat the context.

1:53:30

You get the answer.

1:53:32

Right. So we have talked about these two parts.

1:53:34

We have talked about groundedness.

1:53:36

Groundedness means is the answer supported by the retreat context.

1:53:41

Whatever response the LLM is giving, the chatbot is giving.

1:53:43

Is it coming from the context?

1:53:46

And.

1:53:46

Relevance means is the answer relevant to the question that you're asking.

1:53:50

These two aspects we talked about.

1:53:52

The final thing that their triad is talking about is context relevance.

1:53:55

It basically closes the loop.

1:53:57

So we talked about this part,

1:53:58

but I'm going from context to response.

1:54:01

And we also talked about this part, going from query to response.

1:54:04

Now we are going from query to context.

1:54:06

That's it.

1:54:07

And this is also quite helpful.

1:54:08

This is very, very helpful if you want to understand the quality of your retrieval.

1:54:13

These are very important because I told you,

1:54:15

RAG applications, if it goes wrong, how do you know where it is going wrong?

1:54:21

It's simple.

1:54:23

Chunking, embedding, embedding, vector d'b, it's, it's got.

1:54:25

There's nothing.

1:54:26

You have our template follow up on,

1:54:27

any sort of PDF like anybody can build a rag system in a matter of seconds.

1:54:31

The biggest challenge is when you face issues, when you face mistakes.

1:54:35

Your judge, the wrong score is giving a lower score.

1:54:39

Groundedness judge is giving a lower score.

1:54:41

Now you have to question that, okay, why am I getting a lower score?

1:54:44

why is my RAC system not working?

1:54:46

And context relevance can be a very important metric.

1:54:49

Because what it tells you is, based on whatever question I'm asking,

1:54:52

am I retrieving the right context?

1:54:55

Is the right context even retreat?

1:54:56

If there is the problem then, then like nothing downstream will worth right.

1:55:01

Because everything is on context on dependent.

1:55:03

If your context is right, then your context not retrieved not, then what will be?

1:55:06

and there can be several reasons behind this.

1:55:09

This is why can't goys down to chunking, boils down to embedding,

1:55:14

all these things.

1:55:14

will have to be done.

1:55:16

And each of these will be separate judges.

1:55:18

This kind of a judge will, this is a different judge will, this is a different judge.

1:55:21

We focused on these two in the class, right?

1:55:23

We have both things in class in focus here.

1:55:25

And generally in many practical scenarios, what we have seen in projects is that if you take

1:55:30

care of these two parts, the third part is automatically covered.

1:55:33

That's why in my demo I showed you these two parts.

1:55:35

I made these two judges.

1:55:37

If you see my slides also, I actually have judges only for these two.

1:55:42

But then again, in sometimes in books and articles,

1:55:44

you will see rag triad, a third one metric be given.

1:55:47

But usually in practice, we have seen that if you're covering the grounding this part and if you're

1:55:53

covering the relevant spot, if you're covering the relevant spot, if you're going to do all right,

1:55:56

so right's the right thing that it has to be right.

1:56:00

Although it cannot be that this is right, so right, and this is also right, but this is wrong.

1:56:03

It cannot be.

1:56:04

It's a triad, right.

1:56:05

So it's just another way to look at it.

1:56:08

So you can add the third parameter also.

1:56:10

It's called the rag triad.

1:56:11

I'll share this link with all of me.

1:56:13

This is very, very useful.

1:56:14

And if this is helpful for all of you, I'll, yeah.

1:56:23

Let me just share this link with all of you.

1:56:34

No, no, you were just to clarify vector database, cahy modify.

1:56:38

Vector database is not getting modified.

1:56:40

Not at all, not at all.

1:56:42

Vector DB is not at all getting modified.

1:56:43

If that's what you're asking.

1:56:44

you're not touching the vector db.

1:56:47

Vector db how can't modify over?

1:56:53

GIT says modify.

1:56:54

What do you mean?

1:56:55

Gid, where's from?

1:56:57

Sorry, I think I'm losing the context to the question, you grudge.

1:57:01

How's I'm showing you the demo in my screen, right?

1:57:05

Where vector db is not getting modified.

1:57:07

You are asking the question.

1:57:09

You are retrieving the chunks.

1:57:10

And that's it.

1:57:11

Vector DB's no update not going to.

1:57:13

No update not going to.

1:57:14

If you're referring to some code you have done,

1:57:16

so I have to see what you did there.

1:57:18

So here, so you're retrieval time

1:57:20

in time, there's no modification

1:57:21

never, just to let you know.

1:57:23

Yeah, yeah, same thing.

1:57:25

Hankik, no part there.

1:57:26

Hankit, like semantic chunking is only impacting this layer.

1:57:30

You have to understand where the layers are coming.

1:57:32

Whatever we talked about, chunking, chunking is happening.

1:57:35

This is your whole rag application,

1:57:37

whatever story we talked about, the first four sessions last month.

1:57:40

This was all of this.

1:57:42

this is your whole rag

1:57:44

part, so semantic chunking

1:57:46

to here here.

1:57:47

That's the judge's saying.

1:57:48

Judge is coming after this.

1:57:51

This after this.

1:57:51

after this judge are all this rag story

1:57:54

that we did,

1:57:55

now the judge

1:57:55

said, did you do it right or not?

1:57:57

That's it.

1:57:58

So chunking is only one of the components

1:58:00

in the main rag application.

1:58:03

Got it?

1:58:03

So judge is after it.

1:58:04

Judges like a LLM.

1:58:05

Judges, think of judge as one more

1:58:07

language model.

1:58:09

Whatever response you're getting,

1:58:10

you're passing it through a judge

1:58:11

to get a score.

1:58:14

Got it?

1:58:25

And this is very, very important.

1:58:27

And just wanted to clarify,

1:58:29

evaluation is an extremely important component of building LLM applications.

1:58:33

Evaluation is absolutely important.

1:58:35

Because if you evaluate not,

1:58:36

you'll, you'll not know,

1:58:37

whether the application is working or not.

1:58:40

That is a very important thing to keep in mind.

1:58:41

Okay? Okay. Okay. Okay. Okay. Okay. Okay. Okay,

1:59:03

you're okay. Excuse me.

1:59:08

Okay.

1:59:08

Okay.

1:59:09

Okay.

1:59:10

Okay.

1:59:11

you're saying, Gid tracker shows M, sign in with Gere score, showing, and that can happen.

1:59:20

It usually doesn't mean that your embeddings are, like, I would say doesn't, doesn't usually mean

1:59:26

that your, you know, embeddings changed.

1:59:29

For assisted vector TPs often update, side files, while, journal, locks, SQL, like, metadata,

1:59:35

access time stamps, it has internal indexed state during reads.

1:59:39

So Git marks them as modified.

1:59:41

It's not that vector DB's contents change.

1:59:43

I would, I would say, I would say, a good way to think of it is that

1:59:48

what's sort of internal metadata change over, no, not that the file is changing.

1:59:53

The answer to your question is, to keep the persisted DB directly out of GIT with GIT ignored.

1:59:58

Now, get ignored those, okay?

2:0:00

Unless you are intentionally versioning database finds.

2:0:03

A vector DGyp.

2:0:04

That is the solution to your point.

2:0:08

Hello?

2:0:09

No, no, that change in here.

2:0:11

to let you know that is not getting modified but safe side you can do a gate ignore if you're

2:0:15

using version control okay okay okay let us move on so this was a very very important

2:0:25

concept which I talked about here over on let's continue on so yeah so broadly speaking we

2:0:34

talked about chunking we talked about different types of chunking fix-size semantic

2:0:40

chunking. Another very important part, as I told you, is the metadata part.

2:0:45

Metadata part is also very, very important. You need to understand. We have seen this

2:0:49

before as well, just to kind of summarize it. Whenever we are creating chunks, it is a good

2:0:53

idea to associate metadata with the chunks. Right? It is a good idea to associate metadata with the chunks.

2:1:02

Just say, for example, imagine you are asking a question. You are asking a question.

2:1:07

this particular question. Can I return a damaged laptop? Imagine you are asking

2:1:18

this question to the Amazon customer care. Amazon's customer care. There you're asking the question,

2:1:24

can I return a damaged laptop? So ideally, RAG workflow in what will happen? It will go to the vector

2:1:30

DB and it will retrieve all the relevant chunks. Right. Now what we are trying to do is we are saying,

2:1:35

can we make the retrieval more efficient?

2:1:39

Yeah, how more retrieval pipeline for more efficient

2:1:41

can we do that? Can we make the retrieval more efficient?

2:1:45

so that you don't, so that based on a question,

2:1:48

we don't have to go to the vector dv and retrieve the chunks.

2:1:52

See, because the vector dv will usually consist of several tens of thousands and

2:1:56

millions of chunks, right? Vector db is really huge.

2:1:59

So how can we make that retrieval process more efficient?

2:2:04

Because if you can make

2:2:05

make that retrieval efficient, you will get fast answers.

2:2:08

Not so what will be? User answer

2:2:09

question type and it will take a long time to retrieve the answers.

2:2:14

It will take a long time. Latency will increase.

2:2:16

These are all things you have to consider.

2:2:19

So your solution should not just be based on accuracy.

2:2:22

The last part, the discussion I talked about, groundedness, relevance, they are only

2:2:26

evaluating accuracy.

2:2:28

So, by the rag system, is it even giving the right answer?

2:2:31

First, you know, obviously, accurate to have.

2:2:34

If you're all right, if you're not sure, if you're not sure,

2:2:35

point. Second level, what you have to do is you have to work on the efficiency.

2:2:40

You have to work on reducing the latency. Is it speed? Is my application passed?

2:2:45

User has asked and they're waiting 15 seconds to get the answer. And nobody can use your app, right?

2:2:52

That's the ABB's technician has, he, who's got urgent help chaiy.

2:2:56

His system crashed, his machine fail, equipment fail is. And it's a very real engineering challenge

2:3:02

is right, that we are facing. So technician needs an urgent answer.

2:3:05

are they, it's a matter of, it's a matter of like life and debt sometimes, right?

2:3:11

So sometimes, like if you know seamens, companies like seamens, like they are basically

2:3:17

one of the biggest manufacturers of all these CT scan machines, MRI machines.

2:3:23

Now, any of the hospital, you know, seamans' equipment there, is, you know, seamens, this up,

2:3:27

is a engineering company, right? And a lot of the times, what will be city scan or MRI machine

2:3:32

may cause error. And you need instant help to this.

2:3:35

things because sometimes there are real patients who are inside and there are, there is real

2:3:39

operations which are going to do. Like, there are so many hospitals which are using Siemens

2:3:44

equipment today, right? So there is real world, right? Seamance is also a big provider of

2:3:51

signaling system. Indian rail may up that not right now, but if you look at European

2:3:58

rail, Siemens is a European company obviously, but if you look at European rail systems,

2:4:03

Siemens is completely taking care of the signal.

2:4:05

system. Infrastructure, track, signaling, poor house, people. So if there is any fault

2:4:10

somewhere, if any of the systems are not, the technicians or the railway engineers want instant

2:4:15

answers. There they cannot type something and they will not be waiting, B, second, T, second,

2:4:19

wait for air, no. Latency is a very important aspect. How do we improve the latency? How do we

2:4:25

make sure the rag is able to be fast responses? And usually, this, the rack system is slow usually because

2:4:34

it is going to the vector db and it is trying to retrieve the information from all the

2:4:39

chunks. You don't have to do that. You can associate matter it up.

2:4:44

Now we have merit to associate by associate. So it is, it is like saying, if I have to give

2:4:49

your example to you, it is like saying, let's say we have the vector db. You have a vector db.

2:4:54

Abidded. A bit of we are saying, this chunk 1, this chunk 1, this is chunk 2, this is chunk 100. These

2:4:59

are the embeddings. And we are retrieving based on the chunk embeddings. Now what I'm saying is, you can

2:5:04

also associate metadata. We have done this before. We have seen the exact demo before also,

2:5:10

right? Now we can associate metadata. And here here here

2:5:15

metadata down, let's say, year, 2001, 2002, got or not, 2010, something like that. You can give

2:5:23

more metadata, good up name, company name, whatever, file name. And now if the end user

2:5:29

asked the question, here here from your query are, right? Here from your query are, right? Question is, question,

2:5:34

is, okay, tell me, what are the details of 2022?

2:5:38

Okay, let's say the Tesla's question. What is the annual revenue?

2:5:42

What is the annual revenue in the year 2022? Right? This is the question I'm asking. So now the thing

2:5:48

is that you don't have to go to the entire vector db and look up. Because vector dp is massive.

2:5:53

Now you have to go to full vector TV in look up. It can happen in layers. So first you

2:5:58

can do a metadata level search. First you can do a metadata search. First, you can do a metadata search.

2:6:02

In earlier, it will search, okay, which are the chunks only for 2002? Let me get

2:6:08

only the chunks for 2002. These are only the 2002 chunks. Now, within these 2,022 chunks,

2:6:14

I will find out which are the similar chunks. So that is the way how it can speed up your retrieval.

2:6:22

Because otherwise, every time my user asks the question, it will go through all the vector

2:6:28

db and try to find out similar chunks. But it's not needed.

2:6:32

question is related to 2022 and revenue, then you're all the millions of other rows

2:6:39

in the vector TV don't even need to go to. So first let me use the metadata search to find out

2:6:45

which are those chunks, which are 10, 15 chunks which are relevant to the query. And within those

2:6:53

1015 chunks, let me find those are similar chunks. So that is the way we can do this. And

2:6:59

if you see the question here, we have actually given a small, uh,

2:7:02

in here. So these are some metadata fields, actually, you can see. So I asked the question,

2:7:09

I asked the question, can I return a damaged laptop? If I ask the question, can I return a damage

2:7:14

laptop? Now, look, metadata search in your example. Because I mentioned laptop, who

2:7:20

the back products will pick again. So it will apply the metadata filters, that's B2, active. It has

2:7:26

to be an active laptop. Right? So that's the idea. So filter like product,

2:7:32

equal to laptop and status equal to act. It makes retrieval cleaner. Now in that massive

2:7:37

vector DV, I have so many documents, that so many chunks. Out of all the chunks, I will

2:7:42

apply that filter. It's like a, think of it like a wear clause in SQL. And finally who

2:7:46

wear plus filter apply to. Let me out of those thousands of chunks in the vector dv, let me narrow

2:7:52

it down to 20 chunks. Let's say these has a chunks where my information could be there. And out of

2:7:58

those 20 chunks, I will now do a similarity search. So that is the big.

2:8:02

picture idea. That is the big picture idea of what medical level filtering is all about.

2:8:08

I hope everybody is absolutely clear. And very important, you will have to, please keep this at the

2:8:15

back of your mind. This is usually not a very core, it is usually not a very core generative AI task,

2:8:21

but you will have to go ahead and ensure that you are constantly re-chunking and re-indexing your vector

2:8:27

so then be just like we do this in a normal relational database you will have to make sure

2:8:35

that you are going ahead and you are going ahead and you are ensuring that you are

2:8:40

uh as and when the underlying documents are getting updated you are updating your vector

2:8:49

which if new documents are getting added you are adding chunks to the vector db if the

2:8:56

original documents are getting added you are adding chunks to the vector db. If the original documents are

2:8:57

being removed because his vector dv in reference remember vector dv will always have a reference

2:9:03

to the original document we have seen that in the prior session metadata may your reference

2:9:07

reference that he was chunks how are from which documents the chunks are so

2:9:11

if the underlying document removed then from the vector tv somebody will have to remove those chunks

2:9:17

so that is also a very important part re chunk re chunking and re indexing your vector tv but this is

2:9:23

usually part of an administration task but usually vector dv is so sensitive even

2:9:27

even if you're in a generative AI role in a company usually our vector db like the chances are

2:9:32

less that you will work directly on it right so okay team a come karek there'll be one administrator

2:9:39

person who will work on it uh with database level knowledge they will create the vector db or

2:9:45

that vector db up to access data so as a generative AI person as a person who is building a rack

2:9:51

system you can only connect to the vector db and get responses but the management of the vector db will

2:9:56

usually be a very very sensitive thing.

2:9:59

Ah.

2:10:03

The idea is the same,

2:10:04

like you're fixed chunking in store

2:10:07

you're storing metadata, page number.

2:10:09

Seventic in the fact that is.

2:10:11

That's the sentence,

2:10:13

some page number is,

2:10:14

that's reference no.

2:10:16

Page number will not be there,

2:10:18

but other metadata will be there.

2:10:19

There,

2:10:20

metadata's a context change

2:10:21

like topic.

2:10:23

So fixed size chunking in

2:10:24

just a topic

2:10:25

you cannot have a meditator like topic but semantics

2:10:28

there can be a meditator like topic i agree with page number will not be relevant

2:10:32

but a page number if you want to put you can still put it up as a

2:10:35

say you can't say okay i have a particular chunk

2:10:38

and that chunk is coming from page numbers one

2:10:40

comma three comma seven

2:10:42

you can have it

2:10:43

look a metadata

2:10:44

you can put whatever metadata you want

2:10:47

metadata is what metadata is what

2:10:49

metadata is nothing but information about your chunk

2:10:52

you are just sharing more information about your chunk

2:10:53

you are just sharing more information

2:10:55

about your chunk.

2:10:56

That chunk we can we tell something more about the chunk?

2:11:00

It can be a page number,

2:11:02

that chunk in which page number

2:11:03

that chunk is in original document

2:11:06

that chunk of the corresponding topic

2:11:08

because you can come down completely up to you

2:11:11

how you want to define the matter.

2:11:13

Okay? Okay. Okay.

2:11:15

okay guys uh any other questions any other questions some very very important and the very

2:11:26

key uh i would say learning from today's session was the grounding part evaluation very

2:11:32

important l lm as a judge very important and uh something that like no i want you to incorporate

2:11:39

in your demos going forward so llm as a judge very important okay okay okay okay

2:11:45

Any questions, anybody wants to ask me at this morning time?

2:12:03

Agent Subraj will be, again, uh, if you see a big part of what we have in this module, I, I, I, so this module was more about the, uh,

2:12:11

drag part, we were discussing some conceptual things, but if you see,

2:12:15

That is pretty much done now.

2:12:17

This is what we saw here again to summarize.

2:12:21

The other session, we will further see some more advanced fine-tuning things on drag.

2:12:27

And then the entire thing is on agents.

2:12:30

We will come to Langra.

2:12:31

So we have multiple sessions on Langra where we will discuss how to build multi-agent systems.

2:12:36

We saw a very simple example of single agent systems in the last, last month.

2:12:41

I'm react framework.

2:12:42

I will extend on that idea and we will learn.

2:12:45

And very interesting, like, so A Ageka, all the sessions are on agents here.

2:12:50

Right.

2:12:51

Yeah.

2:12:51

So we will see that.

2:12:52

And of course, after that we have agentic memory and patterns and all that we have parted.

2:12:56

Okay.

2:12:59

So just to summarize the ideas, guys, what we saw for today.

2:13:02

So we looked at metadata, uh, chunking, grounding checklist.

2:13:07

And the, I would say the most important part was this particular grounding checklist.

2:13:10

How do we go back and ensure that whatever applications you are building, the application, the

2:13:15

applications are basically the rag applications are actually grounded in the context.

2:13:19

So that is a very, very important thing. So, yeah, Ali is asking a question in current

2:13:24

session, we upload a PDF.

2:13:27

Huh. What do you mean, Ali? I didn't get your question. Actually.

2:13:33

Huh, metadata is something you will have to add a D. Okay. So you have to add an app. During chunking,

2:13:40

you will have to do it, basically. You can, you can, I would suggest you can refer back

2:13:45

If, you know, if you want to get some context on that, you can refer back to this particular session.

2:13:50

Where we talk exactly about that.

2:13:52

You just chunking while a class.

2:13:54

I actually talked about that metadata part in more detail here.

2:13:59

I think this class we did on rag, chunking and document preparation.

2:14:04

So you can refer back to that session, Ali.

2:14:09

And you can just review that once.

2:14:13

Where is that?

2:14:15

Yeah.

2:14:25

We actually saw that process how to...

2:14:29

Okay.

2:14:30

Okay.

2:14:31

Okay.

2:14:33

Okay.

2:14:34

Okay.

2:14:38

Good guys.

2:14:39

Any other questions?

2:14:40

I have saved the file for all of you.

2:14:44

Okay.

2:14:45

you can go to your folder 2nd July.

2:14:49

So 2nd July folder in your ABB demo file.

2:14:52

Already I have uploaded for you.

2:14:53

So please refer on to it, everybody.

2:14:57

And this is how I will encourage you to work on, take your own personal projects also.

2:15:02

You some use cases know in your enterprise, take some PDFs.

2:15:06

It could be something as simple as a resume.

2:15:08

It could be something as simple as a, you know,

2:15:10

some electricity bills upload.

2:15:12

Maybe you have some insurance policies.

2:15:14

You have health insurance.

2:15:15

Yeah, automobile insurance, something of that sort.

2:15:18

You take some of these things and you try to work on it.

2:15:21

Okay?

2:15:21

So that could be a good way how you can do it.

2:15:27

What do you mean?

2:15:31

Evaluation notes you're saying, Ali.

2:15:34

Yeah, yeah, yeah.

2:15:35

Take it. I'll do that.

2:15:36

I'll do that.

2:15:37

The one that I talked about today, right?

2:15:38

Yes, sure.

2:15:43

Okay.

2:15:45

So thank you, everybody.

2:15:46

Once again, yeah, over to Arshita.

2:15:57

Thank you, sir.

2:15:59

Students, I hope you all have tried executing today's code.

2:16:03

I have also launched the feedback poll.

2:16:06

Please fill that in as well.

2:16:08

Only some of you are left.

2:16:15

Thank you.

2:16:45

Thank you.

2:17:15

Okay, thank you everyone.

2:17:30

We got 100% participation in the polls.

2:17:33

So we will be closing the session now.

2:17:35

Thank you everyone.