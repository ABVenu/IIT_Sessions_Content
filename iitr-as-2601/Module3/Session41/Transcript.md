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

Thank you

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

Thank you

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

Thank you

21:54

Thank you

22:24

Thank you

22:54

Thank you

22:56

Thank you

22:58

Thank you

23:00

Thank you

23:02

Thank you

23:04

Thank you

23:06

Thank you

23:08

Thank you

23:10

Thank you

23:12

Thank you.

23:42

Thank you.

24:12

Thank you.

24:42

Thank you.

25:12

Thank you.

25:42

Thank you.

26:12

Thank you.

26:42

Thank you.

27:12

Thank you

27:42

Thank you

28:12

Thank you

28:42

Thank you

28:44

Thank you

28:46

Thank you

28:48

Thank you

28:50

Thank you

28:52

Thank you

28:54

Thank you

28:56

Thank you

28:58

Thank you

29:00

Thank you.

29:30

Thank you.

30:00

Thank you.

30:30

Thank you.

31:00

Thank you.

31:30

Thank you.

32:00

Thank you.

32:30

Good.

32:34

Hi, everybody. Good evening.

32:36

Yeah, I was just waiting for everyone to join in. We'll just be starting.

32:55

Good evening.

32:59

Good evening all of you.

33:00

Thank you.

33:30

Thank you.

34:00

Thank you.

34:30

Thank you.

35:00

Thank you.

35:30

Thank you.

36:00

Thank you

36:30

Thank you

37:00

Thank you

37:04

Thank you.

37:07

Thank you.

37:30

Thank you

38:00

All right.

38:10

Good evening all of you

38:12

and today's

38:13

today's session will pretty much be the complete

38:16

the completion to the rag module that we've been doing since last week.

38:21

Just to very quickly summarize once again with our mind map where we are, you know, what we are doing and how we are starting out.

38:30

to it.

38:31

So the very last session, we just going to quickly bring up the mind map here for all of you.

38:40

So here is the mind map.

38:43

So after we covered Python and machine learning in detail.

38:47

So we are in the Generative AI module, the Gen.

38:49

A.

38:50

and Agents module.

38:51

And in the last session, in fact, the last three sessions, we have talked about the details of RAG.

38:56

So we have understood all the different components of a RRAG system except for the different components of RRAG system, except

39:00

last part. So we have seen how to take a data set, how to chunk the data, how to take

39:05

a data, how to create chunks. And then from those chunks, how we go back and create an embedding

39:12

model. We've also seen the aspect of how to create an embedding model, generate embeddings, and

39:19

then ultimately store those embeddings in a vector d. So chroma db part we also saw. And the second

39:25

part was how next time when the user asks the question, how we retrieve the information, how we retrieve the

39:29

information, how we retrieve the relevant chunks. And then on the basis of that, give it to

39:35

the LLN to get the final response. Okay. And that last part is what we are basically talking about

39:41

in detail in today's session. So today's session is all about the retrieval and the grounded generation

39:46

is what we are talking about. How do we do that final retrieval part? So until the last session,

39:51

it was all about vector DB. So take the data chunk, generate the embeddings, save in the vector db. We saw until

39:58

that part and today we will see next time the user asks the question how do we retrieve

40:02

retriever also we have seen we have we have we have understood we know what is

40:05

retrieving six chunks seven chunks we have seen that but we get into that in detail okay

40:10

and how do we finally do the final generation so this will this this this today's course will complete

40:15

the rag loop for all of us okay and a very very good use case we actually did a wonderful

40:19

use case in the session last session we actually took a Tesla document and we were able to

40:25

build a real world rag system on the basis of

40:28

the Tesla document. So that is how this particular session fits in the larger context.

40:34

So just to lay down some guidelines with respect to where we are and what we are trying to cover

40:41

in today session. Okay. So I'm going to take you back to the I'm going to take you back to the

40:48

module that we already did. So so I'm going to take you back to the same Tesla demo that we already

40:53

shared with you last session and I will run it through that.

40:58

but before that let me very quickly summarize the whole drag loop in my own words okay

41:04

but this will be a big part of our session today we'll go back to the same tesla pdf document we'll take

41:09

a complete end-to-end use case where we'll do all the stuff again uh you know from scratch and on the basis of

41:15

that we will go back and uh you know generate the the final retrieval results okay so now let me quickly

41:24

go back and share with you the complete rag loop and before i uh go any further i will encourage

41:43

everybody to just give it a glance once this is a very nice diagram where i've summarized everything we've

41:50

seen a lot of slides in our session but today i will keep it only one

41:53

slide only one slide which is this because this completely summarizes everything about rags

41:59

in one slide okay so everybody just take two minutes to glance through this once then i will discuss

42:06

it in my own words and then exactly on the basis of this i will go back and take you through that

42:10

case study the complete code aspect will be seen if all of you just please take a couple of

42:16

minutes just glance through this one

42:23

you know.

42:53

You know,

43:23

You know

43:53

and now

43:57

and now,

44:01

now,

44:02

what we are going to just,

44:23

another 30 seconds and please try to recall all the ideas we have been discussing since last week. That's my only thing just so that all if you are able to recap all that all that.

44:34

Just another 30 seconds and I'll start explaining this in my own words.

44:53

You know,

45:23

So, what I will do, first things first, let me take the example of a, of a HR use case, okay?

45:35

So we want to take a case study here and the case study that we will take up here.

45:39

Let me show all of you.

45:44

So we'll take a HR-oriented case study for this particular exercise, okay?

45:49

So imagine we have a company PDF manual.

45:52

H.R manual, okay? Let me just use a slightly bigger pen.

45:59

H.R. PDF manual. Spanning total 100 pages, okay?

46:06

So 100 pages is a manual. The company has a total overall PDF manual, which is spanning total overall 100 pages.

46:15

That is what we have right now. Now the whole idea is, what is the business use case. The company has a total, the

46:21

the business use case. The business use case is the company wants to build an automatic chatbot system for their employees.

46:29

Okay. It means, let's say, if you join a company, company's

46:34

there, right? So you might have time-to-time questions about the company.

46:39

How many leaves you get? Compensation, how you get?

46:42

Compensation, when you'll you'll get, when you'll get a bonus will, when you'll give,

46:46

what are the different roles you have? How do you progress from a developer to a manager?

46:50

of things are, you know, questions people will have. And actually, it's a very real use case.

46:57

We have, like, you've done a consulting work for a customer a few months back. We will, we actually

47:02

build this system also. A very common use case that enterprises are looking at. This is not the only

47:08

use case. There are so many use cases not right, but this is one of the use cases that I see is happening

47:13

a lot where support departments, HR departments, any of these kinds of departments, which are

47:20

which are document focused and very manual in nature and getting automated.

47:26

So HR department is also, except for the human factor.

47:28

The human factor is definitely there.

47:30

If you always want to see a human being, if you want to be a human being, you want to talk to a human being also.

47:36

but if you have some generic questions, this is one area where rags are shining a lot to do it.

47:41

is a very real use case, actually.

47:43

so imagine we have this entire set of manuals for the company that is there.

47:49

And if any employee in the company, if they ask a question, we should be able to retrieve

47:54

the information from that HR manual and generate it the answer.

47:59

That's the idea. So a chat type of interface been a company.

48:04

Every employee in the company can access that particular chat interface.

48:09

So if you go, you ask, how many leaves do we get in here?

48:13

So the moment you ask that question, the model will be able to generate a response.

48:17

Okay, you go and ask the question, how many, you go and ask the question, how many,

48:19

leaves do we what is the compensation policy, the highest compensation range in my role,

48:24

and the model should be able to generate the answer. So that is the kind of thing that we are trying

48:27

to simulate. So obviously, first thing is chunking. Chunking I've discussed here in the last session.

48:33

So chunking is where we try to divide the data into smaller parts. So we are just for the same example here,

48:40

we are saying, he one chunk is one page.

48:49

Just for the example, because we have already seen that there are different, different ways you can do chunking, right?

48:56

A fixed size chunk in, you can also do semantic chunking.

48:59

What is fixed size chunking?

49:00

Fixized chunking tells you that every 512 characters you want to create a chunk.

49:04

For semantic chunking, Hothaii, all the similar aspects of the document, they are all part of one chunk.

49:09

But the other, you have a massive HR PDF manual spanning 100 pages.

49:14

You go through that entire pages and wherever there are similar ideas, they are all placed in one chunk.

49:18

But just for the same thing, you have a massive.

49:19

simplicity for this demo, I am saying one chunk is one page.

49:22

If you have 100 pages have, C1, C2, C3, all the way up to 100 chunks, this is what you

49:28

have right now.

49:29

Now, next thing that we have to do is we will use an embedding model.

49:33

Now, your chunks been got, okay?

49:35

But what is the chunk?

49:36

A chunk is nothing but a section of text.

49:39

Okay, a chunk is nothing but a section of text.

49:42

Machines cannot understand text.

49:44

Inherently, machines cannot understand text.

49:47

So what we will do?

49:48

We will use an embedding.

49:49

model. And we will take each and every one of these respective chunks,

49:59

C1, C2, O'Gi, C3, all we have to see, 100, we will take each and every one of these

50:06

respective chunks, and we will generate the embeddings of these chunks. So we will take the whole

50:11

media, we will generate the chunks. Chunks are nothing but sections of the document.

50:15

100 chunks will make, we'll make each and every one.

50:19

one of these hundred chunks and we will generate embeddings of the chunks. We call them chunk

50:22

embeddings. And embedding models we, what we use are more transformer models use. We have done

50:28

this, even this section we have seen. And chunk embeddings, we upshot, remember we talked about

50:34

an upset operations. We're vector div in insert. In vector db in, vector dm in, so vector db, so

50:41

vector db will basically contain the chunk, the chunk ID, the chunk metadata, the chunk metadata. Metadata,

50:46

there's a bit of a lot of the chunk. Well, that from where from.

50:49

are you. You have chunk. Here your chunk text

50:52

if I could just add a few more words. This is the chunk text.

50:58

Some other information will be there. Chunk ID will be there. Chunk ID will be there. Chunk

51:02

chunk of text. And then you will also have information about the chunk metadata.

51:13

up? Meritator, I mean, one of the other way, that chunk of

51:21

documents are. That's a real world scenario, the kind of solutions that we usually build. It is

51:27

usually not from one PDF. We have multiple PDFs. Right? In the simplicity, here I'm showing only

51:32

one PDF file. Our use case today is for one PDF. But you can easily extend it for hundreds of

51:38

of PDF files. It is important to retain the merit data, that the chunk, that the chunk you are stored

51:43

correct which PDF file it is coming from, which text file it is coming from, which

51:47

doc file it is coming from. It can be anything. See, I am taking PDF doesn't mean that it is

51:51

always PDF. Any kind of text file. It can be text. It can be JSON. It can be HTML file. It can be

51:57

dot doc file. What document? It can be dot Excel file. Anything where you have got text data.

52:01

Anything. The chunk is coming from where. So that source will be there. You can metadata

52:05

source. Let me write it in itself. Next, we will have the chunk embeddings and every chunk will be a vector of

52:12

numbers. Let's say, mano C1-1. Point-1. I'm just giving some ballpuff numbers.

52:18

Just some example numbers I'm getting. C-2. Your point 1, point-point-1. And C-3

52:27

got some other. C-3 is a little bit more. Okay. Now, therefore, C-1 and C-2 seem to be very similar.

52:33

But C-3 is something very different. And then-backly chunks are. And C-100 seems to be again very

52:38

different. C-100 is a very different idea. Because so this is the embedding.

52:42

Embedings collectively tell you something about that particular text.

52:46

Because we have seen that also.

52:48

So, this is the final story up to the vector db part.

52:51

And the vector db part is actually managed by your separate guide.

52:55

The same way that, you know, we talk about relational databases.

52:58

Upper relational databases and you will typically have a person who will, you know, who will manage the relational database.

53:06

So similarly, there will be one person who will manage the vector db.

53:10

And here also there are a lot of questions people are.

53:12

People sometimes wonder, okay, sir, 100 pages document.

53:16

We've chunking, embedding, everything, and we are storing in the vector d.

53:20

But what if somebody, what if somebody, what if a new page gets added?

53:26

What if a new page gets on it?

53:29

What if a page gets deleted?

53:31

What do we do in those kinds of scenarios?

53:33

What if a, what if a new page gets added?

53:37

What if a, what is a page gets deleted?

53:41

How do we go back and handle?

53:42

And then those kinds of scenarios, we go back and effectively do the same kind of

53:50

insert, update, delete operations in the vector D. So those are again something we are not getting

53:54

into, but just so that you can relate back to your SQL module. You've made SQL key last to last

53:59

course in. Machine learning's first one post in Python key, if you remember there was a session on

54:05

SQL where you learned select start from, you know, select in, you have learned those SQL things.

54:10

So there is a insert statement.

54:12

update statement. So what I'm getting at is the same kind of methods that you use in a standard

54:17

relational database. You will apply the similar kind of strategies for a vector db also.

54:22

Here here you're up update here. Here here. You're here. You're up a update. All those operations

54:27

are also possible. But again, from a generative AI perspective and from a course perspective,

54:33

our focus is a retrieval path. We're only selected. Okay. Now, we will see the bottom pipeline now.

54:40

Top of the pipeline. Our top pipeline has our own.

54:42

Now, you have the next one pipeline taken here. Quarry, retriever, chunk and another.

54:46

Okay? Let us see. Now. So, what is the query? Quarry is the user question?

54:53

User Sama-cuhi. This is the end user. User. User, what? User? How many leaves do I get in a year? Let's see. How many leaves?

55:12

in a year. This is the query text that you are able to see on the screen, right?

55:23

And the whole idea is you get a query text and you will effectively use the same embedding model.

55:30

The same embedding model you'll be using. You can't the text. As I told you, machines don't understand text.

55:36

Machines for text are so much. So you have to take that entire text and convert that entire text. And convert that entire text.

55:42

into what we refer to as query embedding.

55:47

Yeah, a query embedding for. And just to give an example to you, query embedding values

55:52

what, what will be the values for query embedding? This will be something like, let's say, 0.1.1.

55:59

I'm just giving a very bonpuff number. It's an example number. So now,

56:04

you have a query kind of vector form available here. This is how the machine understands the query. The

56:09

semantic meaning of the query is present in these numbers.

56:12

So now, what will be here? This is the aspect we'll be doing now.

56:18

So now what you do? You have a vector dv. Okay? Vector dv is like a library.

56:22

This is, we have an analogy last to last class in. What is the vector? It's like a library.

56:26

Here you have all chunks. And user is asking this question.

56:32

The retriever will go back to the vector dv and retrieve the top two similar chunks.

56:36

Okay? Retreative the top to similar chunks.

56:42

How can it trip to? Well, it will basically do a similarity match.

56:47

It is like a distance formula. It's a similarity match.

56:49

Just for the demo exercise right now, you have there.

56:53

Quarry is 0.1.1. You tell me which of the chunks it is most similar to.

56:59

Just for the exercise here, we are able to see only four chunks, right?

57:03

Actually, 100 chunks are. But you see there. Here here four chunks visible.

57:06

So just by like looking at the numbers, I think you will agree with me that the most similar chunks are C1 and C2.

57:12

C1 and C2 are most similar to the query that is being asked.

57:18

What it means is, given the question that you are asking, user is asking a question, that

57:24

is asking a question that means given the question that you are asking, C1 and C2 are the most

57:30

appropriate answer.

57:32

The answer is mostly present in these relevant chunks.

57:38

So these are the top two chunks that you are actually extracted.

57:42

Is there be a CQA4. You will have to, you can, you can figure out top two, top three, top four.

57:47

I will have those conversations today. So what it is. But for now, we are keeping it to top two.

57:52

We are retrieving only the top two chunks, C1 and C2. And this is what is referred to as a retrieved context.

57:58

Isco how retrieved context get into? That means, user asked a question.

58:03

Based on the question, you go to the vector TV. You retrieve what are the top two similar chunks.

58:09

That means, in order to, enough to answer the.

58:12

that particular question, what sections of the document do I need? What all do I need to

58:19

answer that question? So in order to answer that question, the most similar portions I require are C1

58:25

and C2. Our answer is this two chunks in kind of here. So here, because these two chunks

58:32

most likely resemble the answer. And this is what is called the retreat context. Let me write it down.

58:38

This is your retrieved context.

58:44

Actually, this the retrieval is, rag in the retrieval-in-rtle-rack-me-the-retrieval-weller thing is this is

58:48

because we are retrieving the context.

58:51

The user is asking a question.

58:52

You go to the vector TV.

58:54

Vector TV is like your entire store database.

58:56

You retrieve what are the relevant chunks.

58:58

You retrieve the context.

59:00

And then you are making the final LLN policy.

59:03

This is the piece we will see today.

59:05

Baki, all the pieces we have seen majorly.

59:07

This is the final.

59:08

piece we are trying to add today. So today's class is basically completing this

59:12

loop. So here we're doing. Let us see that. Here we have final

59:17

prompt looking. And that prompt in what prompt in what

59:19

things would. Let's talk about that. Let us see that. So you will have your usual system message.

59:25

Remember all language models, LLMs, whenever you're making any API call, you will have to

59:30

write your own system message. And then you will have to give your own user message.

59:38

User message, what are the things that will go?

59:40

That will be there in the user message?

59:43

User message, you will have you.

59:46

In the user message, you will have your, let me just write it.

59:50

In the user message, it will be the combination of the original query.

59:58

Let me bring the original query.

1:0:00

There is the original query.

1:0:01

Yeah, your query.

1:0:02

The original query is coming from here.

1:0:07

There is the original query.

1:0:08

plus the retry context.

1:0:11

This taken together is what is called the user message.

1:0:15

I just wanted to highlight it in a proper way.

1:0:18

So the system message will be the LLM's own instructions.

1:0:23

You are explicitly highlighting its own instructions.

1:0:26

What the LLM can do, what the language model cannot do.

1:0:29

System message, you have a high level instructions.

1:0:31

We have all seen that, right?

1:0:32

Here on our constraints all that will be there in the system message.

1:0:36

And user message will consist of

1:0:38

User message will consist of the original query.

1:0:43

What is the original query and what is the retrieved context?

1:0:46

That is what the user message will consist of.

1:0:49

So what is the question you're asking?

1:0:51

What is the context you're retrieving?

1:0:53

And that whole thing will be part of your user message, basically.

1:0:56

That is the thing.

1:0:58

And this is how you will make the LLM API call and get the final response.

1:1:03

And now if you think about it,

1:1:04

if you think about it, how is RAC different?

1:1:07

The biggest thing is that?

1:1:08

You know, like we have talked about generation.

1:1:11

How is lag different?

1:1:13

Because in a normal scenario, what we would have done?

1:1:15

In a normal scenario, what we have done in the initial sessions?

1:1:20

Before we came to the right part.

1:1:22

If you remember, we were only doing this.

1:1:25

We were asking the query.

1:1:28

System message.

1:1:30

We have a user message.

1:1:31

Based on that we are getting the response.

1:1:34

So this is the story we were discussing until now.

1:1:37

Okay?

1:1:38

So we have a language model.

1:1:40

You will have a,

1:1:41

so you'll basically have a particular system message.

1:1:46

You will have a particular user message.

1:1:49

And based on that, you will make the API phone.

1:1:52

LLN will give the response.

1:1:54

This is the story we have discussed so far.

1:1:57

What is the story we are discussing now?

1:1:58

All this entire detail we have discussed.

1:2:00

If I have to summarize that, this is the normal generation.

1:2:03

Right.

1:2:04

If I just go and write it down, what you're seeing at the top is like a normal

1:2:07

generation.

1:2:09

This is like a normal generation.

1:2:13

Or I don't have to write about normal.

1:2:15

There's nothing called like, you know, just, just trying to use a general term.

1:2:19

You have a generation task here.

1:2:21

What do you see?

1:2:22

It's like a normal generation task.

1:2:24

You ask a, user asks a question.

1:2:26

Basically, if you remember, I'll give you a small use case.

1:2:29

If you remember my very first session, we discussed for LLMs, that was long back, a few weeks

1:2:34

back.

1:2:34

So we had discussed a use case on transcript,

1:2:37

meeting transcript summarization, then.

1:2:39

So question in your transcript and the response will be the summary.

1:2:44

So you have a system message, you will give a input and based on that, the response will be generated.

1:2:49

Use system, user assistant.

1:2:51

Same story.

1:2:51

Now, what are we doing differently in RAD?

1:2:53

Let me use a different one of these.

1:2:55

So in RAD, the story remains very similar.

1:2:58

Here here, you have your system message over.

1:3:01

Here on here, your user query would.

1:3:07

you have a retrieved context today.

1:3:11

User query and retrieve context.

1:3:13

This is what is different.

1:3:14

And these two taken together is like a user message.

1:3:17

Your sister message, that's not really remains the same.

1:3:19

User name.

1:3:20

User question is not getting processed by the LLM directly.

1:3:26

Based on the question, the context is retreated and together that becomes a user message.

1:3:31

And based on that, we are getting the response.

1:3:34

And this is what we are getting the response.

1:3:36

And this is what we call a retreat.

1:3:37

augmented generation because first we are retrieving the relevant chance.

1:3:42

We are augmenting the user message and based on that we are generation.

1:3:47

Just to kind of complete the whole story because sometimes people wonder, okay, sir, we are doing

1:3:52

something very different.

1:3:53

No, we are not doing something very different.

1:3:55

We have learned a lot of components here.

1:3:57

But if you look at the core of it, the core of it is just like a normal API call.

1:4:01

Uh, but just to get that context, there is a lot we are doing.

1:4:04

Lot we are doing chunking, vector DB.

1:4:07

retrieval, all that we are doing just to get the retreat context.

1:4:11

Yeah, here we have retrieved context.

1:4:14

User asks the question, you go and retrieve and you get the retreat context.

1:4:17

So now you ask the question, you pass the context and this taken together is like your user message level.

1:4:25

And that is why we call it retrieval.

1:4:26

First, you retrieve the context, augmented, you augment the user input.

1:4:31

Previously, it was only the question.

1:4:32

Now you give the question and the context.

1:4:34

You augment the user input and based on that you generate it.

1:4:37

That is by the term retrieval augmented generation.

1:4:42

I hope everybody's around.

1:4:43

Everybody is absolutely clear.

1:4:45

So just going to quickly go ahead and, you know, kind of save this.

1:4:49

And I want to just make sure everyone's able to, you know, like you have this with you.

1:4:54

Just give me one second.

1:4:57

Yeah, of first screenshot.

1:4:58

P.HLA will go to know.

1:5:01

What is that?

1:5:04

Ah, sorry.

1:5:05

Actually, sorry, I might have missed that question.

1:5:07

Okay, I'll take it up.

1:5:11

Actually, when I open up the snipping tool, your chat hide will just give me one second.

1:5:16

Let me go ahead and just cross shape.

1:5:19

This is visible.

1:5:23

Yeah, excellent.

1:5:24

Here we have made.

1:5:25

Here we've made, all the whole hour you summarized.

1:5:27

Okay.

1:5:29

What is that?

1:5:30

I noticed a chat agent in my company today.

1:5:32

I asked it.

1:5:33

It confirmed it is open AI L&M.

1:5:36

And Rag is also there.

1:5:37

No, absolutely.

1:5:38

Ankeh, that's a very good question.

1:5:39

You asked.

1:5:40

Actually, in enterprises, it's a quite normal.

1:5:43

You have confluence.

1:5:44

Confluence and jira, and jira is also an atlacian product.

1:5:48

Jira is also an atlacian product.

1:5:49

The idea is very similar.

1:5:50

Absolutely.

1:5:52

These are all rag systems.

1:5:53

Companies are all, like this is a very normal thing nowadays.

1:5:56

Companies are all investing in chatbots.

1:5:58

And those chatbots are basically rag systems on their own internal document base,

1:6:03

port base and all that.

1:6:05

Confluence had, jira had got.

1:6:07

If you might have a company wiki pages, let's say you might have a company wiki page,

1:6:11

so it's their documents will, right?

1:6:13

You might have hundreds of different internal code bases, okay?

1:6:18

Those key, so all of that will become part.

1:6:21

So whatever I'm explaining right now with respect to that PDF,

1:6:24

the starting way, the documents where we are taking a PDF.

1:6:27

We have an HR system racked.

1:6:29

You have any any system can make.

1:6:31

And this will be very, very good, especially in the enterprise context where, as I told you,

1:6:35

like Confluence, confidence is a place where,

1:6:37

it's like a knowledge base.

1:6:38

Let's say company's any of the things go,

1:6:41

you're up confluence to go and go and let's say your,

1:6:45

your company might be following certain types of coding standards,

1:6:49

coding guidelines.

1:6:50

If they be company's code, whatever code you have in the company,

1:6:54

you want to go back and save all of it in one place.

1:6:57

Okay, you want to save it.

1:6:59

Like what they say, can both take,

1:7:00

repository, code repository.

1:7:02

There is a term that we use called code repository.

1:7:04

Let's say money, you know, we are all writing all these.

1:7:07

Code, Jupyter notebooks, IPY, ND files.

1:7:09

We're in every class in you share.

1:7:11

Like companies in, you will write code.

1:7:13

Companies will write code, and you will write code according to the company's standards.

1:7:17

Companies have some standards.

1:7:19

You know, standards could be something like what kind of variable names you're using,

1:7:22

what kind of, you know, naming conventions you're using, right?

1:7:25

What kind of approaches you are using.

1:7:27

So company will have its own code basis.

1:7:29

So that entire code base, believe it or not, that entire code base is like your documents know.

1:7:35

So that's why I said this is not just.

1:7:37

a PDF file. This can also be a PY file. It be a Python script.

1:7:41

It can be a PDF in you. What are you? PDAF in you. PDAF in you're, right?

1:7:46

So text is text to your Python may be here. This can also be a PY file. This can also be a

1:7:52

a Jupyter notebook and IPYNV file. Whatever IPYNV file, this can be an exercise for you guys also.

1:7:59

Maybe you can try it out. You can take five Jupiter notebooks for a five Jupyter notebooks for a rag

1:8:02

very interesting use case actually. Okay. So you can go. So you can go. So you can go. So you can

1:8:07

you can basically have. You can basically have an IPY and B file also here.

1:8:14

This is an IPY and Bifile. Right? That's one way to be correct.

1:8:18

Yeah,

1:8:18

Bailch, absolutely. That is exactly the part of what we. So you've asked a question, sir, is there any way to

1:8:23

remove a document from the rag? Or,

1:8:25

you can do that. But you have to update your vector db.

1:8:29

You have to update your. If you have to update the document vector db in already better. This is back

1:8:33

to our relational database management concepts. Just say, you have to update.

1:8:37

and delete, here you can update and delete. But that has to happen with a separate process.

1:8:42

So you can absolutely do that. And usually, you know, you know, you guys what enterprises do,

1:8:47

companies in actually what? Companies may actually this is like a periodic operation.

1:8:52

Hey, Chad GPT, hey, Chad GPT is not a rag, by the way. Chad GPT is not a rag.

1:8:56

Chad GPT in chad GPT in some other. Hey, this is the, this is the complete. Chat GPD is just a simple

1:9:02

language model. It is not doing this kind of thing.

1:9:07

So that is something different.

1:9:10

Chat GPD in actually, Yugrat GPD is doing a normal generation.

1:9:13

You're asking you, chat GPD generate. I think a good way to relate to that would be.

1:9:18

Yeah, yeah, you can just go and ask a question and the system will generate the response.

1:9:24

Correct. From that perspective, we can say. From that perspective, we can say, you guys.

1:9:29

Correct. Correct. But there, you're up, up, up, update need. I get your point. I get your point.

1:9:36

So you've got your point. So, Yugraji said.

1:9:37

our chat gpt map document upload

1:9:39

so, how do it. In that case, I would still say to some extent it is building an in-memory

1:9:43

rag system. That is happening.

1:9:45

But there update not. If you have got to update

1:9:48

then you have, then you can't dobrage. Taking the same chat gpt, example,

1:9:52

you have to document had to do.

1:9:54

You have to manually that PDF remove

1:9:55

so that you can do in the vector db also.

1:10:03

In fact, you know, in fact, uh, you know, in fact, uh, like,

1:10:05

very interesting and I wanted to any and we change, sorry, um, can you just read, uh, you know, retried, like, what is that? Can you change documents easily without manual process? Hey, you have to involve yourself manually. You cannot automate this part. The vector DB creation is something you will have to go back and, uh, you will have to

1:10:35

to kind of manually do this part.

1:10:39

Okay? So, you have to manually

1:10:41

let's say, here you have some chunks. Let me give an example to you.

1:10:45

You have got C3, C4A, C5, you've got some chunks.

1:10:48

And now all of a sudden you realize, Yubraj, that the C3, C3, C4, C5 chunks

1:10:52

are old document, old data. That is old data, that is old data, stale data.

1:10:57

That is not a new. So you will have to manually do it.

1:11:00

That is not an automated process.

1:11:01

Here there's no command in Chrome A DV. There is no command we have to automatically do it.

1:11:05

You will have to manually do it. And again, Yuma, I will take you back to a normal relational

1:11:10

database management system. Now, now, you normal RDBMAS social. We don't have a automatic process,

1:11:16

right? Where there's somebody will have to manually see the record and do our update or delete

1:11:20

statement, right? So somebody will have to manually do it. There's no automated process.

1:11:26

But you asked a very nice question on the chat GPT part. I'm just going to take a moment in a while

1:11:31

to clarify that, that, that chat GPT in a chat gpt may what is. That's what you're going to do you.

1:11:35

documents and all. Something very similar is happening. I'll come to that in a while.

1:11:40

But that's also a very nice use case you gave. Okay? And yes, again, extending my conversation,

1:11:46

whatever I was mentioning, as I was telling you, this documents can be anything.

1:11:50

This code files be possible. You take five four files. You take five Jupiter notebooks here.

1:11:56

You take the five Jupiter notebooks. You do the chunking. You have the chunks. You save all those chunks in

1:12:02

the vector d. And now users can ask questions.

1:12:05

Users can go back and ask questions with respect to the code base. This is the entire company's

1:12:12

code base. Hasarro files over. Thousands of Jupyter notebooks you might be having. Jupiter files

1:12:17

here, Python files over, whatever. And now the employing the company can ask a question. This will be a

1:12:23

question. Let's say a developer asked the question that, hey, how do we do this? So now your rag application,

1:12:28

the internal company rag application can go and retrieve the relevant chunks from the vector TV and give the answer.

1:12:35

So in a real world use case, this is the kind of application that we are seeing companies are using a lot.

1:12:40

That he was also raising the same thing. You were saying, okay, in enterprises, they are doing this a lot.

1:12:46

They are building a rag on the internal company's code base. So that any developer who is building solutions in the company,

1:12:53

who quickly go and they can do that. In fact, many of you in this, in this audience, you're already working in companies.

1:13:01

Companies may co-pilot user. Right. Microsoft co-pilot is such a popular thing that.

1:13:05

that enterprises are using.

1:13:06

Co-pilot is also being something very similar.

1:13:09

Co-pilot may be your rag used for a bit. Something very similar.

1:13:13

You've made co-pilot in it whenever you are asking a question, it can actually go and refer back

1:13:18

to your, it can refer back to your entire code base.

1:13:21

Not only your current code, that's normal, you can ask a question, co-pilot your code generate

1:13:26

that is another thing. But what it does is, it also has the ability to reference to your company's

1:13:32

internal code base. So you, you can connect can't.

1:13:35

So co-pilot also will do something very similar.

1:13:38

So imagine you are right now in, so co-pilot is like a simple chat application.

1:13:42

What is co-pilot? It is Microsoft co-pilot is a chat application.

1:13:45

You go and look up in the vector dv. What are the similar chunks?

1:13:50

Okay. What are the similar portions of the code?

1:13:53

And based on that, you get the answer.

1:13:56

So there are so many applications, so many applications we have here.

1:14:01

Okay.

1:14:02

Okay.

1:14:05

And you're going to, again, Yulajad asked a very good question.

1:14:15

You know, I'm going to just go to take your, take your time here for a minute.

1:14:18

That's a very good point, actually.

1:14:20

So, you can't if I need a rag system as a customer in which I need to change the documents.

1:14:26

I need to change the documents rapidly after every use, right?

1:14:31

You have to, you have to understand that whatever we talked about here.

1:14:35

This was like a completely enterprise rag system.

1:14:38

Yeah, we have an enterprise rack system discussed here.

1:14:41

So in this enterprise rack system, this vector db will be massive.

1:14:45

This would be like a massive vector db.

1:14:48

So this is not from the customer perspective.

1:14:50

Ah, you talk GPD example later, I'll clarify that in a minute.

1:14:53

But this is like a complete enterprise rag system where the customer will should have ideally no access to it.

1:14:59

Vector DB is a very sensitive thing.

1:15:01

And vector db is usually will be massive.

1:15:03

It will be huge.

1:15:05

Now, it is not like a simple one PDF or two PDF on a thing.

1:15:08

We are talking about millions of PDF.

1:15:10

The company's entire document data will be stored in the vector D.

1:15:14

So this is a highly sensitive database, which customers and end users will not be given access to.

1:15:20

So 100% of your, and first of all, customers should not even know the vector DB idea.

1:15:27

Customers, the end users should see a simple chat application, a simple user interface.

1:15:34

End users should not.

1:15:35

should not have to concern about what is, you know, how should I update.

1:15:38

And that is not the end user's work.

1:15:40

That is completely a developer's work.

1:15:42

So right now also, whatever explanation I'm doing, this is from a developer perspective,

1:15:46

not from an end user perspective.

1:15:48

So end user, who, in my example today, the end user is the employee of the company.

1:15:54

That employee will be, that employee will ask, that, he will ask him,

1:15:56

that's what he's the same matter.

1:15:59

He has no, it no, it's no matter from where from where from, what, retrieve are.

1:16:03

So that means we, we'll ask, we, we'll ask.

1:16:06

We have a user interface, we'll, we'll answer will.

1:16:09

That's it.

1:16:09

Okay?

1:16:13

And just to clarify, what you can also do is, if you want to, as an end user, if you want to go back

1:16:19

and build that system, so a proper production rack system should have an admin upload panel

1:16:24

or an automated sync pipeline.

1:16:25

So document changes triggered.

1:16:27

So what you can do is, you can do is, you can, you, you can, you, you can, you can, but end users will

1:16:32

not have the control for it.

1:16:33

The developers will act to set it.

1:16:35

So, Chrome and DB may be, let's say you've got C1, C2, C3, up to C100, these chunks are coming

1:16:41

from certain documents, PDF files, text, file, from.

1:16:44

You have some other document upload here.

1:16:46

Yeah, that you can absolutely give end users the ability to that, that will be a separate

1:16:53

workflow.

1:16:54

That will be a separate workflow.

1:16:55

So if you're this example through relate to, this is like a question the employees will be asking,

1:17:01

but from the HR perspective,

1:17:03

you know, where HR, a more manual upload can.

1:17:07

That will be from the HR perspective.

1:17:08

That will be from the HR user interface will be able to be a user interface

1:17:11

and HR can be, here, he can't,

1:17:14

that this document we need, and this document

1:17:18

we have updated. So HR will be able to upload the fresh

1:17:20

PDFs.

1:17:21

And as he will HR, that PDF upload

1:17:23

again, it will be chunking

1:17:25

again, it will back in vector TV

1:17:27

and it's corresponding operations over.

1:17:28

If that chunk already exists are, then you can update it.

1:17:32

If that chunk is not exist,

1:17:33

you can delete it, you can insert it.

1:17:35

So that way you can go back and do it.

1:17:39

I hope that answers the question.

1:17:40

It's a very deep question you asked, Eubrach, but, yeah,

1:17:42

that's the H.R.

1:17:44

Ui.K. aspect, you can do it.

1:17:46

Okay?

1:17:57

And guys, you know, like, one very interesting thing, I want to clarify.

1:18:01

So one interesting thing I want to clarify.

1:18:03

I will answer that, guys.

1:18:06

Very good questions.

1:18:07

Latency and providers, I'll come to those things.

1:18:10

But just very quickly, something that is very relatable to all of you,

1:18:14

something that everybody in this class can relate to chat GPT.

1:18:18

I'm just going to come to that for a minute.

1:18:19

Just want to come to that for a minute.

1:18:21

And let me download that Tesla demo once again.

1:18:26

You'd be surprised to see that chat GPT

1:18:27

maybe a little rag-o-a-rug-o-o-r-rug-o-r-r-rug-o-r-r-r-rug-o-r-r-rug-r-r-rug-r.

1:18:28

But not in the level we have discussed.

1:18:30

That's a different thing.

1:18:32

But I just wanted to do.

1:18:33

to show you you can let me go back and go back and if you can, let me go back and

1:18:49

if you take a look at it, this is this is what chat GPT is doing, right?

1:18:54

You can upload the PDF and you can ask the question, what is the annual revenue.

1:19:01

If you remember, this is the same exercise we did.

1:19:03

the other day, right? You are asking the question around annual revenue. What is the annual

1:19:09

revenue in the year 2020? This? So we can go back and ask that question.

1:19:18

Excuse me. So what is the annual revenue? In the year. In the year. In the year.

1:19:27

So, you can't you go and ask this question. Very interesting. You'll be surprised to see what happens.

1:19:38

There's actually a rag that is going on behind the scenes. So chat GPT also, but although you are not,

1:19:44

this is not something we are built. So whatever I explained here, this is something we built from scratch.

1:19:49

Here we have our rag, and that is the deliberable by the end of the class. At the end of the class, we will be able to build something

1:19:57

like a chat dpity. We'll have you a same user interface

1:19:59

and make it. Same story that you are seeing here. The same story

1:20:03

how we can also do it. You're here. You upload

1:20:05

and you question, question, answer either.

1:20:08

Chat dpity, maybe, just how it's how it. So we looked at the

1:20:11

entire inner process. Here you have to

1:20:12

inner process, you know. You have the document

1:20:14

uploaded and asked, you, you'll ask, you, you'll get

1:20:16

something that every single person in the class is doing right now.

1:20:20

So all are all. But now we will have some

1:20:23

understanding that, by you know, when you're going to have

1:20:25

you're document there you, this is something like. So this is also kind of doing

1:20:30

something like a rat. So this is in a more detailed enterprise context we discuss, but this is

1:20:36

you know, you know, a more generic context which everybody is using today. So this is like a

1:20:41

persisted rag. This is a vector db is permanent. So company will invest a lot of money to create

1:20:48

the vector db. This will be a very, very big. And then users will ask questions and get the response.

1:20:53

But this is in the context of a more.

1:20:55

temporary application. This is just your chat session

1:20:58

for you. You have a chat gpti make a new chat session

1:21:02

should do you. You have documents upload for a one document does document

1:21:05

upload and you ask the question and you can see what it does. It reads the

1:21:09

document. Here he will be reading documents. Reading documents.

1:21:12

Reading documents. I mean that vector TV is in-memory

1:21:14

are.

1:21:14

Asked. Someal put. It's relevant chunk extract to answer. Okay. Now

1:21:19

look very interesting and it is also giving the context.

1:21:21

That way, the answer from context. So very interesting. You can see.

1:21:25

the sources. Sources, you can you show that

1:21:27

can you upload the files used to answer that question?

1:21:29

If you upload 10 files, this is the metadata by the way.

1:21:33

Can you see this is very interesting?

1:21:35

Because we are all using this thing every time.

1:21:38

But now you will get a clarity that we

1:21:40

we use this is actually doing a rag.

1:21:42

Most people don't realize, but this is actually like a rag.

1:21:45

So this is using what is referred to as

1:21:48

and you

1:21:49

chat GPT to ask,

1:21:51

does chat GPT do use in-memory rag?

1:21:54

drag, in-memory rags. It is kind of using something like in-memory, actually like in-memory vector db.

1:22:02

Sorry, I think I just, you know, it's called a in-memory vector db. It uses an in-memory vector db.

1:22:10

That means whenever you ask a question, internally what is going on inside chat, GPT, let me go and

1:22:16

complete the story. Same thing, same story is happening. You know, document here up note here on chat session

1:22:23

started.

1:22:24

Okay, you have document uploaded.

1:22:26

As you enter, whenever you hit enter, you know what is happening?

1:22:30

This is going.

1:22:31

Here here chunks are.

1:22:33

This is getting stored in the vector db.

1:22:36

Now the only difference in chat gpt is this vector db is very small.

1:22:40

What I explained to you is what you will do in an enterprise setting.

1:22:44

One time vector db you are going to be in an enterprise setting which will be massive.

1:22:48

Chat gpt in that is why I use the term.

1:22:50

This is the in-memory vector dv.

1:22:52

This is the in-memory vector db. That means this is going to exist in the RAM.

1:22:58

This is the time the application is running, it will be in-rame in-div be made.

1:23:03

Our use case we discussed here, vector db is stored in-memory vector db.

1:23:09

But here, it's called the in-memory vector db.

1:23:11

Only during the chat session, whatever documents you are uploaded

1:23:14

that basis of vector db are.

1:23:16

But the rest of the story remains exactly the same place.

1:23:20

This is your vector db been here.

1:23:21

here you have asked this is part of your user message.

1:23:24

This is part of your query.

1:23:26

If you relate to the pipeline that I discuss, you have a query here.

1:23:29

So then what you do?

1:23:30

You go back and retrieve the similar chunks.

1:23:32

You retrieve the...

1:23:35

You retrieve the chunks.

1:23:37

And then what's then what's going to?

1:23:39

Internally, this is the layer you're not able to see.

1:23:42

Okay?

1:23:43

Internally what is it doing?

1:23:44

Using that question and the retreat chunks, it is now passing it to the LLM.

1:23:49

LLM, what is it?

1:23:50

Open AI's GPT models it is passing it through and it is finally giving the response that you're able to see on this screen.

1:23:55

So this is like a beautiful application or whatever we are discussing at a much smaller scale.

1:24:00

Okay, so next time you're uploading any documents on chat GPT, Gemini, you should remember that they are also internally doing something like a rag in memory rack.

1:24:08

Okay?

1:24:09

Yeah.

1:24:10

Ah, absolutely. Absolutely. That is, this is very costly.

1:24:15

Hankit, that's a very good point you're raising.

1:24:17

This is very, very costly stuff.

1:24:19

Absolutely.

1:24:19

People are, I mean, no doubt AI infrastructure is such a costly deal.

1:24:26

It is very, very costly.

1:24:27

You're absolutely spot on.

1:24:29

That is why it is expensive, I would say, in a practical real world scenario.

1:24:32

But if I have to maybe touch base upon one technical term, they use massive distributed infrastructure.

1:24:40

They use massive distributed infrastructure, auto-scaling, load balancing, kersh, kashing, kashing

1:24:45

so those all, we are able to maintain the things in a better way.

1:24:49

Just to answer your question, okay?

1:24:55

Anjord, your question is a little deeper.

1:24:57

It is something to do with memory.

1:24:58

I will come back to that later.

1:24:59

Okay, I will drag wall a demo, I will answer your question.

1:25:03

You have asked a very nice question.

1:25:05

This is actually called memory.

1:25:06

So memory what is, I will answer that at the end for you, okay?

1:25:10

Just remind me in case I forget.

1:25:11

But just to clarify, the answer to your question is somewhere here.

1:25:16

So Anjore is asking, that, sir, when we ask, sir, when we ask,

1:25:18

some questions. It is, you know,

1:25:21

our memories have, right? So.

1:25:24

Now, look, you know, you're in chat GPD in settings. You will have something called

1:25:28

personalization. And here here

1:25:32

your, you know, memories. Let me see.

1:25:35

No, here. One second. General. They have removed in search.

1:25:39

Somewhere else they have put it, I think. Security. One second.

1:25:42

So they have a memories option. Let me just see. Data controls may

1:25:46

I don't know. Data controls in where if they put it? They've changed it very

1:25:51

recently actually. Um, personalization. Yeah, yeah, memories. Can you see? So you can actually

1:25:59

go to your chat GPT account or you can go to something called personalization or you have

1:26:03

memories right. So the memories will tell you everything about you. So very interesting. This is

1:26:09

this is the, this is like a memory context. So here here, maybe, could have to rag on.

1:26:16

Here here, to some extent, Anjur, something like a rag is happening.

1:26:21

You know, this is also very, very interesting.

1:26:24

Right. So this is also something like,

1:26:27

something like very, very interesting.

1:26:29

Here here,

1:26:29

here, a bit up to cut up to chat, GPT, maybe.

1:26:32

You can see how it is referencing the memories.

1:26:36

So, so I'll just give you a general thing.

1:26:38

And you look, you know, memories is like a complete file.

1:26:42

Okay, where you know, everything, you know,

1:26:45

everything, everything that you search, everything that you do.

1:26:50

Here, everything you're in here. So, so whatever you search in chat, GPT, and

1:26:57

everything, the entire magic, you're all embedding the magic is. The whole magic is basically

1:27:04

with respect to, you know, embeddings. So embeddings is basically like the

1:27:10

whole thing. Right. So that's what.

1:27:15

one way to look at it. So you can see very interesting. Some of my memories, I should

1:27:19

from show it's like, you know, whatever I've searched in chat GPT, ever since. So like, you know,

1:27:24

like you can see very interesting. I was, I think sometime back last year, I was planning a trip

1:27:28

to Ley. I visited Ladakh two times. Very nice place. So we're planning for a thing. So chat

1:27:33

GPT is that memory made. And you know, what is? And so oftentimes I ask questions about, you know,

1:27:39

like a lot of work I get. So maybe I was, you know, one day I was asking a question to chat GPT. How do I

1:27:44

manage my workload. He made a memory

1:27:46

this is an entire profile about me.

1:27:49

That okay, Sion feels

1:27:50

siren feels overwhelmed by the workload.

1:27:54

So I told you, I stay in Doha, right? So I was, I generally,

1:27:59

I do, I have a, I have a citizenship in Qatar.

1:28:02

So I'm pretty much a resident of Qatar. So right now I'm back in India to do the war.

1:28:07

But I still hold a resident ID there. So I keep asking questions.

1:28:10

Like so I'm working as a, you know, like I keep exploring opportunities in Doha also.

1:28:14

So I was asking some questions, what kind of other work opportunities I have there.

1:28:18

So this is another question I was asking.

1:28:20

So it has actually built a profile that, hey, I'm a data science consultant working in Doha.

1:28:24

So that's a profile beena. And in case you're wondering, what is going on behind the scenes,

1:28:28

you know, if you're asking this question, what is going on behind the scenes here,

1:28:35

every time you ask a question in chat GPT,

1:28:38

whenever we have chat GPT, what is happening behind the scenes is,

1:28:42

is every.

1:28:44

interaction, every chat session,

1:28:46

those embeddings have been made.

1:28:49

Every interaction, every chat session, the embeddings are getting creative.

1:28:53

Embedings are getting created.

1:28:54

So let's say, these are all the chats in chat, GPD.

1:28:58

You can all the chat save, you can opt to delete it also, but by default, all these chats

1:29:02

are getting saved.

1:29:04

Okay, all your chats are.

1:29:05

Let's say hundreds of chats you have in chat GPT, chat sessions.

1:29:09

And who are all the chat sessions, this is the interesting part.

1:29:12

those chat sessions,

1:29:14

you know, that your embeddings memories make.

1:29:17

So they pick up similar ideas across those chat sessions, embeddings.

1:29:21

The magic is again embeddings.

1:29:24

They take every chat thread,

1:29:25

it's kind of an embedding been made.

1:29:27

Is it like a chat embedding?

1:29:29

It will create embedding for chat number one.

1:29:34

Okay, it will create embedding for chat number two.

1:29:36

Embedding for chat number two.

1:29:38

So for every chat session, it will create the embeddings.

1:29:41

And those embeddings,

1:29:42

they make them make to give you intuitive understanding.

1:29:48

This is kind of like a database where it is story, a memory database that it is story.

1:29:53

So you can imagine, you have a memory database.

1:29:59

This is your memory database.

1:30:03

Think of it like a memory vector DB.

1:30:09

So this is a way, a vector DB is.

1:30:11

And every single thing.

1:30:12

of my saved memories that you see on the screen.

1:30:15

I'm just trying to intuitively explain.

1:30:17

This whole across all my chat GPT account, across all my chats,

1:30:21

we're memories, that okay, what is the profile about sign?

1:30:24

Sign is this, sign is this, sign is this.

1:30:27

You know, Sion asks questions like this.

1:30:28

So, it's a question about this.

1:30:29

He's about how about it.

1:30:31

Family kind of, it's, he is, he, he and where it.

1:30:34

and what does everything about me.

1:30:36

And that, um, against my chat, GPT account,

1:30:41

that memory vector div will be now you guys know what is vector d.

1:30:44

Now, look, look, in real one in the real one, so for every row will be like a memory,

1:30:49

and you will have the memory embeddings.

1:30:51

So, is planning a trip to lay with the intention of visiting monasteries, right?

1:30:55

Okay, you can see, okay, and you can see,

1:30:58

this memory of a embedding been here.

1:31:00

This memory two kind of embedding been made.

1:31:02

Memory three's embedding been.

1:31:03

So memory copy a vector db became.

1:31:07

And now you can relate to the story very nicely.

1:31:09

End user, what will do you.

1:31:11

These are, this is like you.

1:31:14

Okay, you.

1:31:15

You're chat GPT, I go.

1:31:16

You open a chat GPT.

1:31:20

You open a chat GPT.

1:31:20

You'll a screen will.

1:31:21

You're here.

1:31:21

You have a question, ask.

1:31:23

Here you enter, and you'll answer.

1:31:25

So you know what is going on?

1:31:26

Every time you ask anything in chat gpt, when you start a new chat session,

1:31:31

this is a beautiful part.

1:31:32

It actually goes on references your vector D.

1:31:35

That be, when you go, when you're a new chat session open up,

1:31:38

I'm sure many times you've observed, you've observed, you open a new chat session.

1:31:41

and you're a question GPT to chat gptt knows that hey hey sion this is what it is

1:31:46

hey Pratab this is what it is hey Ankit i think you are very stressed

1:31:50

you're, I'm, I think you should do this.

1:31:53

So sometimes you're also wondering, he's how is how does it know?

1:31:57

So because it is referencing from the long-term memory and that's the beautiful application

1:32:01

I think with respect to the rag thing that we're discussing.

1:32:03

So there's a lot rags's all right here.

1:32:06

So next time you ask the question, what is it doing?

1:32:09

It is going back to the memory web.

1:32:11

database. It is retrieving the relevant chunks. It is retrieving the, you know, the top two or the top

1:32:17

three chunks, something related to what we discussed. It is retrieving the relevant chunks. And on the

1:32:23

basis of that, it is giving the final response to me. So our question that is not just based on the

1:32:29

question that you're asking, but the answer to your question is also based on your memory.

1:32:34

But, you know, let's say if I go and ask the question, and okay, you know, I want to go and,

1:32:37

please suggest a good diet plan for me.

1:32:41

Let's say as an example.

1:32:43

If I go to chat GPT and I can just ask the question, please suggest the best diet plan for two.

1:32:47

I can show the live demo to you.

1:32:48

I don't know what it will say.

1:32:50

But if I go and ask the question, it will not just give a generic diet plan.

1:32:54

It will first look at that question.

1:32:56

It will go to the memory vector TV.

1:32:58

You know, that memory vector TV, he'll retrieve it.

1:33:02

He can't say, he's a diet plan to know, then we're going to sign a diet plan.

1:33:05

So we're current diet's the first diet's the first diet,

1:33:09

his workload, and it will give me a very tailored response saying,

1:33:13

okay, sion, you're working hard, you're having less sleep, whatever,

1:33:17

you're already working towards your health, all this stuff.

1:33:20

So we think you should do this.

1:33:22

It will give me a personalized answer.

1:33:25

I will not use the word training, Rajdip.

1:33:27

It is not training itself.

1:33:29

Because remember, chat GPT is internally using a model.

1:33:33

Model of our own control not.

1:33:35

But yeah, what you can say is, I think the more appropriate word to use,

1:33:39

Rajdip would be the vector DB is getting updated.

1:33:43

I think this is to some extent, Yubraj, your question, your question.

1:33:46

I think you are getting the context.

1:33:50

So this is how you can build that pipeline.

1:33:52

So users are asking the question, this in-memory vector DB, the memory vector DB is,

1:33:57

this is kind of getting updated.

1:33:59

So this is the, you know, very interesting application.

1:34:03

So people can try this, you know, I think not many of you might know there's a memory feature.

1:34:07

It's very sensitive.

1:34:09

If you search also.

1:34:09

such stuff, you know, like all the memories will be there.

1:34:11

You can see, you can't, what do you know, about?

1:34:15

And it's scale, actually, you know, like,

1:34:18

and this is just sad GPT.

1:34:20

You have Jemini's how much know about?

1:34:23

Because he has your Chrome data, your YouTube data,

1:34:26

your YouTube data, your map's data, your photo there,

1:34:28

everything. And they, and just imagine the scale at which

1:34:32

Gemini is building a memory about you.

1:34:34

So Jemini is not just building a memory about you based on what your,

1:34:37

what your chatting.

1:34:39

that's just one aspect.

1:34:42

Gemini is building an entire profile about you.

1:34:45

That's memory's vector TV has Germany to

1:34:47

that is building an entire profile about you based on everything.

1:34:51

You're where going, what are you, what are doing, what you are.

1:34:54

What photo upload are.

1:34:56

So that entire profile they're having about it.

1:34:58

It is very sensitive.

1:34:59

That's why, you know, some things are not allowed right now.

1:35:02

If you see maps data out, not allowed may have.

1:35:05

But theoretically, it is very scary what we are seeing today.

1:35:09

Okay.

1:35:39

All right.

1:35:44

So you can see, very interesting.

1:35:46

I just wanted to show you as normal demo.

1:35:48

I go and ask this question, how to control my workload.

1:35:50

I mean, you can take a look at it.

1:35:53

Like, you know, I'm only this question.

1:35:56

This is a new chat thread.

1:35:58

We're just a question how to control my workload.

1:36:01

And see what is going on.

1:36:02

It is going and picked it up from my long-term memory.

1:36:04

We have this chat thread in a question to puttie to Pitti.

1:36:07

We didn't know what I do.

1:36:09

What is my contract?

1:36:09

but it knows everything about me.

1:36:11

This is what I meant.

1:36:12

So the moment I ask this question,

1:36:13

I hope you're relating it to the rag idea that we discussed.

1:36:16

The moment I ask the question,

1:36:17

it is going back and looking up in my,

1:36:19

in my memory vector db.

1:36:22

It is able to go back and look up in my memory vector db.

1:36:26

Memory

1:36:26

vector db.

1:36:30

Pull the top five or the top top top 10 relevant chunks.

1:36:35

What are the relevant chunks is able to retrieve?

1:36:37

Yes, are a relevant chunks?

1:36:39

And based on that,

1:36:39

is the final answer we are getting.

1:36:41

So this is it again a very nice application of how we are actually doing this in the real world.

1:36:46

And enterprises,

1:36:48

this is the same thing is right.

1:36:53

You're right.

1:36:54

You will have to do it.

1:36:55

Correct.

1:36:56

Any update on in document in or up to us.

1:36:59

So somebody has to manually go and update it.

1:37:00

Correct.

1:37:01

That is, that is correct.

1:37:05

Once I get Chad GPT a picture of my group for class presentation.

1:37:09

And it will learn from that.

1:37:14

It's all part of the memory.

1:37:15

You've made one part of the picture share that,

1:37:17

that memory was.

1:37:18

And you know, the interesting part is,

1:37:20

again, the sessions right now is focusing on text,

1:37:22

but image can be embedding going to.

1:37:25

If you think, see, right now we are uploading a text, right?

1:37:29

We are discussing how the text is,

1:37:33

we are creating embeddings out of it.

1:37:35

But whenever you upload a picture,

1:37:36

the story remains the same,

1:37:37

that's been made the same.

1:37:38

That's been made sure.

1:37:39

remains very, very simple. Okay. Okay. Let's come back.

1:37:46

Great questions from everybody. Great questions from everybody. Let's come back.

1:37:51

Now, uh, what I will do, let's come back to the workflow once again. This is pretty much what we

1:37:57

talked about, right? Just wanted to stay on this for another 30 seconds to a minute before we come

1:38:07

to the end, you know, the, the hands on.

1:38:09

Let us see that.

1:38:39

and I was just going to go.

1:39:09

to the chat and just, just saw your question.

1:39:12

So no, it doesn't have to be organization specific, just to clarify.

1:39:16

So the LLM, the base LLM doesn't have to be organization specific.

1:39:20

Usually the organization specific part is only the data, the retriever layer, proms, permissions,

1:39:24

guardrails, but that does not have to be, you know, organization specific, just to clarify.

1:39:30

Okay.

1:39:34

And Bavik has asked a question, sir, how does rag work?

1:39:39

And that's actually.

1:39:39

a very good question, Bavik has asked, I think, how does rag work in low latency?

1:39:44

Latency is actually a very important aspect.

1:39:46

You see, all this while we are discussing, you ask the question, chunks are getting retrieved and

1:39:50

we get the final answer.

1:39:51

This process can be very slow.

1:39:52

So this whole process where you're asking the question, retrieving the relevant chunks and getting

1:39:56

the answer, this process can be very slow, real world in.

1:39:59

Okay?

1:40:00

So, so absolutely.

1:40:01

I mean, so this is something you will have to do.

1:40:04

It's a very good question.

1:40:05

So all those are parts of advanced aspects of rags, actually.

1:40:08

So, I, I, I, I, I, I,

1:40:09

I can briefly talk about it, but just to let you guys know, the team is also planning a master class on rag.

1:40:14

So rag, we are just focusing on text data for now, but there are so many other aspects we can do.

1:40:20

So I've also put across a word to the team.

1:40:22

So separately as part of rag, we'll, we'll also incorporate some of these ideas like

1:40:29

from caching, multimodal rag, and some of the things that Bavik is asking.

1:40:33

So how do we build advanced rag pipeline?

1:40:36

How do we make rag quick?

1:40:37

Because if you look at the screen in, this is something.

1:40:39

I think that is going to be very slow.

1:40:42

You ask the question, the vector div will be massive.

1:40:46

You know top two or top three chunks retreated for me,

1:40:48

very time had to.

1:40:50

And if you think from a real world scenario,

1:40:53

user has a question,

1:40:55

based on the question, you go back and hit the vector divay and retrieve the chunks.

1:41:01

You have to wait, right, until that retrieval part is complete,

1:41:04

answer will not know.

1:41:06

So that latency is a big deal.

1:41:08

Latency must have delay.

1:41:09

How much do you have to wait?

1:41:11

How do you make this retrieval part efficient?

1:41:13

Now, how can you efficient can you?

1:41:15

And that is another thing altogether.

1:41:16

It's a very detailed conversation.

1:41:18

If I have to maybe give you a couple of terminologies,

1:41:21

Bavik, I mean,

1:41:22

one is pre-computed document embedding some people do we do.

1:41:25

Prompt caching definitely helps also in that context.

1:41:28

Okay, but then there are a lot of other rag philosophies

1:41:30

we used to build advanced rag pipelines.

1:41:33

So that is something we will see in a separate conversation.

1:41:38

Okay?

1:41:38

you know, very nice questions.

1:41:39

Very nice.

1:41:42

Okay. Now we will go back and implement this entire thing in the context of our.

1:41:49

Uh, absolutely, absolutely.

1:41:50

Absolutely.

1:41:50

Absolutely.

1:41:51

Absolutely.

1:41:52

Absolutely.

1:41:53

Right.

1:41:54

It might be, he, he's kind of, he is.

1:41:55

He, he's doing.

1:41:55

He, he is a drag.

1:41:57

So you, like, type,

1:41:59

you're just type, like, chat are.

1:42:00

You here, there's your enterprise in enterprise in the memory

1:42:02

being a memory being.

1:42:04

Enterprise setup in memory being.

1:42:06

So it is personalized to your thing.

1:42:08

100%.

1:42:09

Cursor and these tools are using rag internally.

1:42:11

100% you're correct.

1:42:13

But in-memory is just to clarify in-memory right.

1:42:16

What we are discussing is the complete enterprise rag system,

1:42:19

which we're going to, but those IDs are using in-memory that, just like chat GPT.

1:42:26

Let's come back to the Tesla DV file right now.

1:42:30

I will once again share this as part of your folder.

1:42:32

The same thing we are doing.

1:42:33

Second June in, what we've uploaded here was, it's pretty much the same thing that we'll be seeing.

1:42:38

here. So let me go ahead and upload this. And. And also, Yubraj, I see your question. It's a very good question. You've asked a good question. You've got

1:43:04

sure is. The best part about RAG is also security. You ask a question

1:43:10

and you're only retrieving the relevant chunks. You're all the chunks retrieve not

1:43:14

are you. So your document is already safe. Right? It's a very good question. From a security standpoint,

1:43:22

rag is already safe because user asks the question and you're retrieving the top five relevant chunks.

1:43:28

You're just that chunks to externally bejured. So the LLM API call. Not everything. And even then there are

1:43:34

strategies that we use.

1:43:35

We're here on masking. Before we send the chunks, we can use. Got it? Make sense?

1:43:40

So even those strategies we can use. But absolutely, yeah, thorea, thorea bohote up leaped for. I take your point,

1:43:46

but that is probably 0,000, 0.01%. If you get the scale, right, if the vector div is so massive,

1:43:53

every time I user asks the question, a very small portion, a minuscule portion is potentially

1:43:59

getting leaped, but you can hide can by doing masking.

1:44:04

And if at all, you're absolutely paranoid about security, then you can do it on premise, which is what you originally see.

1:44:10

Because I'm just trying to give you both the dimensions.

1:44:12

Sometimes companies will have very strict, you know, uh, uh, uh, uh, uh, that may,

1:44:17

we're, no, we're, we'll do it on purpose. So then you can do it on premise.

1:44:21

Olama, you can use that.

1:44:23

Uh, yeah.

1:44:25

Masking, what, what is masking?

1:44:28

Masking, what, just as mano, you know, you're talking about confidential credit card information,

1:44:33

customer detail.

1:44:34

personal information, phone number, data, those kinds of stories, right?

1:44:38

So masking in a way basically stands for, you know, it is basically,

1:44:43

the chunks you're retreated for, see, I'll give a very practical use case, very practical

1:44:47

use case.

1:44:48

You know, let's say you're asking a general question about some credit card.

1:44:51

And the chunks retrieved are containing customer information.

1:44:54

So, when you're LLM to query are, that customer information will be masked.

1:44:58

So, right? So basically, the, those are advanced aspects, but

1:45:02

what we do is after the chunks are retrieved, we're here here on a more masking LLM use

1:45:08

so it will go and take the original chunks and it will generate the masked chunks.

1:45:14

Mask, I mean, mask, basically, means hide, hidden.

1:45:17

So you specifically find out from your chunks, which are those personal information that we have,

1:45:22

but you're hide, then, then us go to go and then that is another architectural strategy that we use.

1:45:32

very good questions very good questions from people okay um so i'm going to go ahead and

1:45:44

quickly connect to the runtime once again just give me one second guys you guys

1:45:51

you guys want to take a break and come back this is the demo that we will see now so we are oh yeah we are at

1:45:56

922 almost okay so five minutes get our water break this will be another uh 2025

1:46:02

minutes match to take a water break a lot of questions today i'm very happy to see people who are so

1:46:08

engaging today and it's a very interesting topic uh but a lot of a lot of great questions today

1:46:14

let's take a water break and come back to five minutes

1:46:32

you know.

1:47:02

Thank you.

1:47:32

Thank you.

1:48:02

Thank you

1:48:32

Thank you

1:49:02

Thank you

1:49:32

Thank you

1:50:02

Thank you

1:50:32

Thank you

1:51:02

Thank you

1:51:32

Thank you

1:52:02

Thank you

1:52:32

Thank you.

1:53:02

Thank you.

1:53:32

Okay.

1:54:02

Hi, folks, welcome back. We will continue on.

1:54:11

So, once again, first what I will do, I'll quickly load the Tesla file.

1:54:19

We already briefly talked about this before as well.

1:54:22

So I'm going to just continue on with the flow.

1:54:24

So here I've loaded the Tesla document.

1:54:26

If you remember, this is a, this is the real PDF file.

1:54:31

You have a real PDF.

1:54:32

file here. And what we want to do is we want to go back and this is a 130 page PDF. So the same

1:54:42

story that we discussed from this point. And I want to, uh, users should be able to ask any

1:54:50

questions from this document and they will get the responses based on exactly the rag pipeline

1:54:54

that we discussed. So whatever story I covered all this file theoretically, from this pay over a

1:55:00

whole racked. And primarily the session focus. And primarily the session focus.

1:55:02

the last part, the ragwara part. So we'll see that. Okay. So

1:55:08

bits and pieces we have talked about, but today we'll complete the whole story. Okay. So starting

1:55:12

one apart, let me quickly install the necessary packages. So PIP install. I will install the necessary

1:55:22

packages here.

1:55:32

popular orchestration library that is used for doing all these things. Like we have

1:55:37

been using retriever, we have been using chunking, we are talking about embedding models.

1:55:42

Yes, all in line chain package may available. It makes it very easy for you. Instead of writing

1:55:47

the base Python code from scratch in order to do each of these things, our blank chain can

1:55:52

methods say in one line of code you're able to achieve these things. Chroma db is the vector

1:55:57

TV. Sentence transformers is basically the embedding models. The transformer embedding models are

1:56:02

When you have those chunks, chunk one, chunk, two, chunk three,

1:56:06

those embeddings, how are you? We already talked about grog before.

1:56:09

You already know grog. Grok is the LLM that we are ultimately using.

1:56:13

Okay. And finally, we have the Tick token.

1:56:19

Okay. The Tick token is the tokenizer package that we have right now.

1:56:30

So the LLN part will be the GROC one. I hope every person.

1:56:32

Everybody remembers that. So when you go to Grog, console Grog, your API keys are and the same way you will have to do it here.

1:56:39

I'm just still running the code here. It's just wait for this. The PIP install takes a while to complete.

1:57:02

So just I think it could be because I think most likely it could be because

1:57:32

Python make you're probably exceeding the number of tokens could be.

1:57:38

Abh Gt, yes. I've not uploaded that. Don't worry. I'll do that. Right after the class I'll upload it. Okay.

1:57:43

Just allow me five to 10 minutes after the class. I'll upload it. Yes. Yeah, I'll do that. Yeah.

1:57:47

And she just, yeah, that's the only thing because Grog is a free thing, right?

1:57:51

See, all these LLMs are very, very costly. Oh, then it should not ideally. But the API might be hitting the

1:57:58

organization limit. That could be because when you're, it is.

1:58:02

counting against your organization quota. Yeah. So, so, uh, because the playground is different.

1:58:08

The playground is not exactly counted against that quota. If you're using APIs, APIs are counted against

1:58:13

that quota. So whatever Kurok's quotas that you're seeing, let's say 12,000 tokens per minute. I think it is

1:58:25

around, uh, open a equally. I think it is around 120,000 tokens per day. That is the limit. So that is the limit. So that is

1:58:32

sounded against the API usage. I know, I know, I know, I know, because the open AIs models

1:58:39

is very, very restricted. You might have, you might have exceeded that particular models limits.

1:58:47

Bucky models, you have not exceeded the limits. Only that particular model, you might have exceeded

1:58:50

the limits because you might be using it a lot. So Grog has many models, right? So that could be one of the

1:58:57

reasons. If you give it some cooling period, try after a few days, it might, maybe next, next,

1:59:02

day you can try. There is a monthly limit also. See, what am I talking about just to clarify

1:59:06

for the rest of the people? If you go to GROF, because GROF is a free provider, right? So if you

1:59:11

look at it, this is the limits that you have right now. 200,000 a day, 8,000 a minute, 30 request per

1:59:17

minute. So these are all the, you know, the typical limits that you have when you are using the API.

1:59:23

Okay, so just just keep this at the back of your mind and this is severely restricted. If you're using the

1:59:28

this is free. But, you know, like, again, it will be different for every model. And also,

1:59:34

it will be restricted. If you're using this a lot in your code, then it might happen that one particular

1:59:40

model you are not able to use anymore. But that is okay. You can use a different one. So this is,

1:59:46

this is a free account, right? So this will be a restriction that you will have. But obviously in a real world

1:59:51

scenario, when you're working on actual production setups, then you will have a paid account. You'll have a,

1:59:57

you have a proper API key and in that case these limits will not be there okay but i would still

2:0:04

say that grok is still amazing because it is one of the only platforms one of the very few platforms that you

2:0:09

have which is you know kind of uh which is kind of giving you this kind of reuse it nothing is

2:0:16

giving you this for free is what are the only platform that are giving it to you for free

2:0:27

clarify, don't worry. I know I'm importing those packages, but we're here on TikTok and use

2:0:31

just to clarify. Don't worry. You know, I know in the code I'm actually doing TikTok and but ultimately

2:0:38

we're not using that. We are not using that. Okay, you're right. So we are just installing the package,

2:0:44

but we're not using it. Okay. So after I install, I will go and restart the session. I will restart

2:0:51

the session. And next, let me go down. Remember, I've already uploaded the

2:0:57

Tesla annual reports fine. Let me run this now.

2:1:06

I am using open AI API API P, but that's okay. Don't have to worry because I have my own

2:1:09

personal keys, but you can use a GROC one. When I share the code with you, I will update it for GROC API.

2:1:14

T. Don't worry. The same thing will work fine. So let me, let's come down. And these are a different

2:1:21

library imports we are doing. Okay. You can see right now, I'm, uh, import. I'm, uh, import.

2:1:27

the recursive text data chunking for five PDF directly loaded to read the data, all these

2:1:33

the different things we are importing. And now here I will create the vector dv. The first part

2:1:38

is creating the vector dv. So we uploaded the zip file. Now first I unzip. This has the PDF

2:1:45

file inside it. You can see. And now I will do chunking. Same story we talked about last class.

2:1:49

I will quickly go over it. So you specify the directory. Holder location of specify for and then you do chunking.

2:1:57

How many chunks do we have? We have total 351 chunks. And here is the interesting part. I have only

2:2:05

one PDF inside this folder. You have a folder location. Right? You have a folder can

2:2:10

a folder in a thousand of PDFs. That is how you can extend this example using some of your own

2:2:15

stuff. So there are 351 chunks that we are able to see in this particular PDF. Every and now

2:2:22

next thing that I will do, I will take those chunks and I will create the vector dv. Okay. I will

2:2:27

use this particular embedding model even this we talked about before what is the embedding

2:2:32

model and then i will create the chunk embeddings you can see that this is the one line of

2:2:38

code we are giving the chunks we are giving the name of the embedding model and this is the

2:2:44

directory where that particular database will be created after this code run successfully the Tesla db

2:2:51

folder will be created and that will be my vector db okay so until now we are in this part upurwara part of

2:2:57

a PDF chunking embedding vector dv is still running now this part usually takes a

2:3:04

lot of time to run a lot of time and by the way when you're running this code at your end

2:3:08

this is not an error it gives a warning but it's not an error as long as your jupiter

2:3:13

notebook code is successfully executed it's not an error you can ignore this one so it takes a while

2:3:19

so here also it's a very small file only 130 pages but in a reality this this this process this

2:3:25

this vector dv creation in practice will take a lot of time but usually it can also

2:3:31

take days literally because you have one-time process in a real world scenario company is starting

2:3:38

an initiative they want to create a vector db you know so this will usually take a tremendous amount of

2:3:42

time in practice okay so now next what i will do i will instantiate the retriever

2:3:48

the retriever is where you are saying that hey i want to retrieve the top five similar chance

2:3:51

this is how you instantiate the retriever and you can specify the

2:3:55

value of k now couple of important things i want to clarify these are again see these are

2:4:00

things that again have to be tried out there is no one way to answer it but these are again things

2:4:04

that have to be tried out so how do you decide you know how do you decide like what is the right

2:4:10

value of k so in a way i would say if you take only k equal to one it is fast but it may miss

2:4:17

a second rule right so it might there might be cases where you miss out information

2:4:20

if you only retrieve one chunk it will be super fast you're using

2:4:25

less tokens but then you might miss out information and if you retrieve too many chunks

2:4:30

if you retrieve more context but risk of noise that is lot of irrelevant information might

2:4:37

also see if you go and look at our current context what is the annual revenue in the year 22

2:4:44

it is possible that you know you're retrieving a lot of context but much of that context is not

2:4:49

relevant because so very low value of k is bad very high value of k is bad and this is

2:4:55

the balanced value of k so the optimal value of k is equal to 3 k 3 4 and you of try

2:5:01

so we have to always figure out what is the the right number of chunks that we should be using

2:5:07

so it again has to be experimental there is no one way to answer it there is no one answer to this

2:5:12

question but you will have to experiment so for this particular demo i'm using k is equal to 5

2:5:18

so if i ask this question what is the annual revenue in the year 22 what will happen this is the

2:5:24

the query query embedding will happen and then you will go to the vector db and retrieve the top five

2:5:29

relevant chunks okay retriever similarity k equal to five and these are the top five chunks

2:5:35

now see if you when i ask this question what is the annual revenue in 2020

2:5:39

you you upka chunks retrieve chunk one consists of this

2:5:44

you your chunk number two is retrieve chunk two consists of this

2:5:48

retrieve chunk three consists of something like this now see the answer where there

2:5:53

here there is answer there so many numbers there somewhere here the answer is present but the

2:5:57

chunks are written the chunks are those sections of the document where potentially that question

2:6:02

is answered chunk four here is this chunk four okay and chunk five is this

2:6:11

and now now that i've retrieved my chunks now we will go to the next part we'll

2:6:14

now we'll now we'll take the bottom of the code in okay so let us see that okay let us see that

2:6:20

i will again this time i will load the vector d so first part was creating the vector dv and the second

2:6:27

part is i will load the vector dv so next time the user asks the question next time the user asks the

2:6:33

question i will now go back and define that entire rag q and day pipeline this is the new part

2:6:38

that we are seeing today okay the rag q and day what the l lm we what we're

2:6:42

what we're doing system message user message the system message will be this this is the

2:6:48

detailed system message for my rag all of you give it a glance please just give it a read all of me

2:6:54

just give it a read take take a minute give it a read please what is the system message for your

2:6:58

rag please give it a read on of you oh sorry sorry i think i went to the other screen yeah just

2:7:04

give it a read all of you the system message for your rag

2:7:18

you know.

2:7:48

Thank you.

2:8:18

Thank you

2:8:48

okay i hope everybody is with me and you can take a look at it and you can't

2:9:03

take a look at it and we are explicitly specifying in detail what is the system message by the way

2:9:09

where is the story coming this story is coming here if i just had to quickly go back to the

2:9:15

this beautiful screenshot that we walk through the entire

2:9:18

session this system message is this one that we are writing this LLM's system message

2:9:22

so we are explicitly saying that you're an assistant to our financial services firm who

2:9:27

answers user queries on annual reports okay user input will have the context required by you to answer

2:9:33

the user questions this context will begin with the token context these are delimiters that we provide

2:9:39

so we're explicitly specifying a delimiter so that the LLM understands that query what is

2:9:48

you that as part of my user message i should have the context also i should have the question

2:9:54

also so hash question or hash context just to clarify the user message of the LLM should have the

2:10:02

original question and it should also have the retreat context okay it should have the query and the

2:10:08

retreat context so we this whole whole LLM system message in

2:10:12

okay so do you so I'm explicitly telling the LLM that user input will

2:10:18

have the context required by you to answer the user question.

2:10:21

The context will begin with the token context is a delimiter and the context contains references

2:10:27

to the specific portions of a document and the question will begin with the token question.

2:10:33

So jlm will see that API call.

2:10:35

When LLM we'll see that API call, when LLM can have the user question also and it will have the

2:10:41

retrieve context also.

2:10:42

Exactly the same story that we discussed here.

2:10:44

So he has question be there, he has a question be there, he has a retreat contact

2:10:46

not really be able. And it's got what is exactly what I'm writing in the system message.

2:10:52

One very important aspect of a rag system is if the answer is not found in the context,

2:10:58

please say, I don't know. And you'll look here here

2:11:00

very interesting, very interesting. I will live demo this for you. I will live demo for you.

2:11:04

You're up here, you, you're here asking, if you weather what is the weather for tomorrow?

2:11:08

And the rag system will not give the answer.

2:11:10

That rag system answer not. If you ask it a general question about the weather, the rack system will not,

2:11:16

you know, it will not give you the accurate answer.

2:11:21

You can just give me one second.

2:11:22

I think I'm editing here.

2:11:26

So the RAC system will not give you the generic concept.

2:11:29

If you ask it the question, you know, if you ask it something that is not in the context, it will say,

2:11:34

I don't know.

2:11:35

Now, user message template will be this.

2:11:37

It will consist of the question and the context.

2:11:40

So what will the user message template consists of?

2:11:43

It will consist of the question and the context.

2:11:46

You are seen, the question will be or retrieve context rave context.

2:11:51

100%.

2:11:51

Grounding is always part of the prompt.

2:11:53

And that is one of the most important aspects of a rag system,

2:11:56

it has to be grounded in the context.

2:11:59

If you're asking, let's say, a Tesla-wola-a-a-a-a-rida use-case are, okay?

2:12:03

Now, you know, Tesla-related question.

2:12:05

You, ask, what are your revenue, profit, what is the company's guidance for the next five years?

2:12:10

That's right-bara-bara-jave-jave-jave-dave-you-bara.

2:12:11

But if you ask it a question, today, what is the weather in California?

2:12:15

That, hey, what is the weather in California?

2:12:16

like, I don't know.

2:12:17

You are asking a question about whether it is going to the vector dv

2:12:22

and it is trying to retrieve relevant chunks.

2:12:25

He doesn't get chunks in any way.

2:12:26

That context in any of the context in any of whether or not be able to answer that question.

2:12:31

Okay, this is a very, very important at a characteristic of rag.

2:12:34

So rags should always be grounded in the data.

2:12:39

Okay, so if you, now let's look at a complete story.

2:12:42

Is it a complete end-to-end story we are seeing on the screen?

2:12:45

So this is that complete story and this is beautiful.

2:12:48

You know, every time I see this, it just amazes me how wonderfully the system is working.

2:12:52

So I'm asking the question, what is the annual revenue in the year 22?

2:12:56

I'm asked, user input here here.

2:12:58

A code depot.

2:12:59

First, based on the user input, I'm retrieving the relevant chunks.

2:13:03

Okay?

2:13:04

I'm retrieving the relevant chunks.

2:13:07

This is your relevant document chunks.

2:13:09

And you take those relevant document chunks and you build that complete context.

2:13:12

You have a context.

2:13:14

Chunks too.

2:13:15

This whole chunks of text will.

2:13:16

That whole context I'm creating.

2:13:20

And now you frame that complete prompt.

2:13:23

LLM's prompt what is.

2:13:24

Role system, system message,

2:13:26

which we already defined here.

2:13:27

And role user, user message.

2:13:29

User message in two things,

2:13:31

context and user input.

2:13:33

Okay, we know the user message consists of two things.

2:13:36

Query and context.

2:13:38

System message, query and context.

2:13:39

So query and context.

2:13:43

Okay?

2:13:43

And then finally, you.

2:13:45

Do chat completions create?

2:13:47

Model equal to model name.

2:13:49

Here here your prompt came.

2:13:50

The prompt has defined you, and temperature equal to zero.

2:13:54

This is also a very important aspect of a rag.

2:13:56

Whenever you, when, because I told you that rag system should always be grounded in the context.

2:14:02

They should always give you factual information.

2:14:05

So I don't want a scenario that.

2:14:06

That we have a one bar runed, then a second time run it, then another answer will.

2:14:10

We don't want that.

2:14:11

We want every time the rag system to have the same answer.

2:14:13

To give the same answers.

2:14:15

So we are getting temperature equal to 0.

2:14:17

We should always say temperature equal to zero.

2:14:19

We should, they should be grounded in the context.

2:14:21

So if I go and run this, I'm getting an answer, 96.77 billion dollars.

2:14:26

And you can informally go and check.

2:14:29

You can informally go and check.

2:14:31

So we have already seen this story, but you can here on here per check.

2:14:33

Just to be absolutely sure that we are getting the right answer.

2:14:38

So, uh, 96.77, you know?

2:14:41

96.7.

2:14:42

Uh, 96.

2:14:42

uh, 966770.

2:14:47

Actually, you know, 96, uh, yeah, million may have my answer.

2:14:51

So let me just check it up.

2:14:53

I think it is in millions.

2:14:55

But you can see,

2:14:56

you can see, there are several places where this is mentioned.

2:14:59

There are several in 2020 through,

2:15:01

we recognized total revenues of 96.77 billion dollars.

2:15:06

Here here.

2:15:06

Here.

2:15:06

Okay.

2:15:08

And I let me give you another instance where it is coming.

2:15:11

For 96.7.7.

2:15:12

billion dollars here. Can you see?

2:15:14

Look at this. How cool this is.

2:15:16

966773.

2:15:17

I mean, 96773, there are so many aspects in the document where this is coming.

2:15:23

This is 9673 here here.

2:15:25

You can you see, that, boy, 20-203 revenue is this.

2:15:30

9-6773 here here.

2:15:31

This is in page number 51.

2:15:33

There are.

2:15:34

There are other, two-khi-chunk in.

2:15:35

9-7-7-3 here.

2:15:37

page number 57, where he are.

2:15:38

And 9-6-7-3 here.

2:15:41

Yeah. So based on the question you are asking, what is the annual revenue in

2:15:46

2023? The retriever is able to pull in information from all these chunks.

2:15:50

This whole chunk retrieved over. And interestingly, this 96.77B came here.

2:15:56

Jove, we have first you showed. So this is also very interesting. So it is able

2:16:04

to pull in information from all these five chunks. This is the retrieved context.

2:16:08

The user has asked asked. Contexts retrieved from all those five. Context retrieved from all those five.

2:16:11

chunks and based on that the LLM is acting as a refiner. LLM is giving me the refined response.

2:16:17

That question study is studying, that's all the retrieved chunks study are. And those

2:16:21

LLM is able to give it a refined, grounded answer. That's why the groundedness is a very

2:16:27

important past. Grounding is a very important concept of LLNN. Because you, the answer to that

2:16:33

question must be in the period. So if you're up, if you're not, if you're not, it will not work correctly.

2:16:39

So that is one important thing to keep in mind.

2:16:41

So let me just take you back to this aspect in a bit more detail. This is very interesting, actually.

2:16:48

Let me talk about it. And then the final story, what I will do. The final story, what I will do,

2:16:55

we'll, we're, we're going to a gradio interface in a, okay?

2:16:59

A radio interface in a, let us see that story. So we have already seen a bit of radio in our

2:17:04

ML session. So that time, we made models ban. And I told you, the radio is like a front-end user interface.

2:17:11

Like a web app you can.

2:17:12

So far it is like all in Jupiter notebook.

2:17:15

But what if I want to build a system,

2:17:18

where there a chat GPT type of interface we'll

2:17:20

make.

2:17:21

Because I told you in the class we will do that.

2:17:22

So this is that last part.

2:17:24

So we have this is that rag-we-we-we-we-welled-weather-

2:17:26

that thing is,

2:17:27

that we'll make a front-end interface

2:17:30

run-gain. So Gradio is again

2:17:31

not a, not a gen-AI-related aspect.

2:17:34

It is mostly into application development.

2:17:36

But just a little bit of code we will be seen.

2:17:39

So whatever we do, whatever we

2:17:41

did in the rag, all I did is I put it in a Python function. That's it. So Gradio is like that

2:17:45

piece only. So don't worry too much about this part. The same story. User asks the question.

2:17:51

Query, a argument, you retrieve the relevant chunks.

2:17:55

Us-based, you write the prompt, system message, user message, whatever story we have

2:17:58

discussed. And finally, based on that, here herepah your response here. Same thing, only thing is

2:18:04

you're a function in it's for down. And then based on Gradio, you do some gradio specific stuff.

2:18:08

I mean, you say, by, GR dot interface, just one line of code is very simple.

2:18:13

Gradio is a very, very simple way to quickly mock up, you know, proof of concept, POCs, kind of thing.

2:18:20

It is not a full pleasure application development framework.

2:18:24

Usually this will be done by your full stack development teams, right?

2:18:28

But this is a very nice way you can try out your demo.

2:18:30

So Gradio is very, very popular for experimentation purposes.

2:18:33

I'm just run. Let us run this thing.

2:18:37

Excuse me.

2:18:38

and you will see a public URL will come.

2:18:40

You'll have you, you may have a machine learning in a demo

2:18:43

showed at this paper. And now you can go back and click on that public URL

2:18:47

and you will see that very nice real world application that we just now built right now.

2:18:52

So this is what your end users will see.

2:18:54

End user can't know. This is what I was mentioning.

2:18:56

He was no idea not, that, what's no idea, that, what your vector divie is,

2:18:59

what is what is your end users will see.

2:19:02

End users will be able to ask the question.

2:19:04

That where, what is the annual revenue?

2:19:08

In the year 2022, end user will ask you.

2:19:12

And behind the scenes, the entire story is playing out.

2:19:15

You ask the question, you retrieve the top five relevant chunks, and you get the answer.

2:19:19

We're here here submit click.

2:19:21

The moment I hit submit, what is going to happen?

2:19:23

That's so that entire rag pipeline is working out now.

2:19:26

Look, Vector DB is a one-time process.

2:19:28

That's your been made.

2:19:29

Like we're in chat, GBT, I'm talking about.

2:19:31

Now, ask you, memory, from context retrieved, and answer are.

2:19:35

So same way, here here here, Vector DB back end in.

2:19:38

You know, if the context is retreated, and based on that, the LLM is giving you the final answer.

2:19:43

So that entire rag story, the whole thing is playing out right now.

2:19:47

And if you see, yeah, you can't, you can do it.

2:19:49

And you look, now, look, 8,000462 are here.

2:19:51

You know, you can't hear that this is the exact answer.

2:19:54

So I think, 81,462, if we're, if we're, uh, you can see we are getting 81,462.

2:20:02

And you can do this with any PDF.

2:20:03

You have got to bills, invoices, he will, insurance policies,

2:20:06

your resume will. You can be a nice personal project. You can be a nice personal project

2:20:10

you can, obviously your personal data will but you can be a nice try. You can be a nice try. You use

2:20:16

my same template. You, you have our PDFs to go up, you up, you up, you have a personal

2:20:24

assistant, you know, with you. You. You have bank statements on up on rack

2:20:28

back. You have, let's say, I say, bank, HDHC's statement's right. You're put a whole, a whole statement's

2:20:34

all the PDFs, four, five bank, PDF, Michelle, fund, statement.

2:20:38

The, very, very statements are right.

2:20:39

Now, put up PDF in, all the PDF in it.

2:20:42

Now, it's up on it. Great idea, right? I mean, you have a, now you can query.

2:20:47

And you can ask some in very interesting questions,

2:20:49

how much did I spend on food last year?

2:20:52

And you'll be surprised to see the answers.

2:20:54

You'll be surprised to see the answers that you're getting.

2:20:57

You can try out these personal projects, you know, based on what we are seeing.

2:21:03

No, no, no, you're going to.

2:21:04

I was just mentioning some personal projects that you can do.

2:21:07

You can build a rag on PD on your resume.

2:21:09

You can build a rag on insurance policies.

2:21:12

Aubri upro a drag per secur.

2:21:14

Okay?

2:21:15

And 2023 up.

2:21:17

Dusra, I try, okay?

2:21:18

2023.

2:21:19

And this is the same answer I'll be getting.

2:21:21

And now the most important part on the groundedness part.

2:21:24

If I ask the question, what is the weather?

2:21:27

What is the weather usually in Delhi?

2:21:30

Okay, during summers.

2:21:32

Now, if you see very interesting,

2:21:34

if it was a normal generation task, what would have happened?

2:21:40

You ask the question, LLM will see the user query and it will generate the answer.

2:21:45

That will be right.

2:21:47

It will tell, it usually very hot in suburbs.

2:21:49

So it will answer that question, okay?

2:21:51

Whatever.

2:21:52

But now, very interesting.

2:21:55

Now this is rag, right?

2:21:57

So what you will do in rag?

2:21:59

User asks the question.

2:22:01

It will go to the vector db.

2:22:03

The Tesla's vector DB.

2:22:04

We are in our use case, back end in the front end, the user interface we are able to see.

2:22:10

But back in the back end, it will go back to the vector db.

2:22:12

It will retrieve the relevant chunks.

2:22:14

Now, interesting part is, based on this particular question I'm asking,

2:22:18

that vector diva in this can't about this.

2:22:20

It's a Tesla report.

2:22:21

Here, here, here, Delhi, summer, or anything, there.

2:22:23

Chunks will not be retrieved here.

2:22:25

No relevant chunks will be there.

2:22:27

And so the LLM will say, I don't know.

2:22:29

And if you, if you are wondering, sir, this, this, this job why will give?

2:22:32

Because remember, in my rack, you are.

2:22:34

one day, I had explicitly mentioned in my system message, I had explicitly said, if the answer

2:22:39

is not found in the context, please say, I don't know.

2:22:41

So this is a very, very important character characteristic of RAC system.

2:22:45

So if you ask these kinds of questions, the system should say, I don't know.

2:22:49

This is just one thing I wanted to mention.

2:22:51

This is very interesting.

2:22:51

And you don't want it.

2:22:53

People will ask all sorts of questions.

2:22:55

Who don't know.

2:22:56

System should not, it's very important.

2:22:58

The system should not generate answers from its own memory.

2:23:02

So, you know, it's a LLN we are asking.

2:23:06

But the LLM should always answer questions from the context.

2:23:10

You can't ask, say, what is the capital?

2:23:12

Capital is all the capital of India.

2:23:13

Like, what is the capital of India?

2:23:15

You might be wondering,

2:23:15

if the capital can answer the question.

2:23:18

But no, it will not answer.

2:23:19

That's the whole idea.

2:23:20

It is not like you are directly passing this query to the LLM.

2:23:23

No.

2:23:24

Based on the question, we are first retrieving the relevant chunks.

2:23:27

So our Tesla PDF in India about India about

2:23:30

with any capital countries, nothing.

2:23:33

So when it goes to the document and tries to retrieve the relevant results, right,

2:23:38

it will not see relevant chunks.

2:23:40

It will not see relevant chunks.

2:23:42

And if I run the thing, I'm sure I will see, I don't know, which you are able to see right now.

2:23:46

It is running right now and it says, I don't know.

2:23:48

I'm sorry.

2:23:48

I mean, I don't have any information about India capital chunks in my PDF.

2:23:52

And this magic is basically happening here.

2:23:57

Okay.

2:24:00

And I just wanted to mention, this is again part of a thing that we will do later.

2:24:08

Hugging face is another conversation, which we're in regular sessions in too,

2:24:11

but certainly this is something I will,

2:24:14

see, there are so many advanced things also.

2:24:17

And what we will try to do is we'll try to identify something I've also shared.

2:24:22

Over and above our regular course, we will keep some sessions for that.

2:24:26

We'll extra classes in this up for that.

2:24:27

As a hugging face, you have you, you know,

2:24:29

so a push dikhae how you can we can plan some things on that definitely but that will be

2:24:35

very interesting. So this is the entire rag Q&A pipeline that everybody is able to see on the

2:24:41

screen. I hope all of you are able to understand the ideas. Happy video. So and the final part was

2:24:48

basically the evaluation, the Eval that we are doing. So the session contents I will be

2:24:57

uploading here, I will just take the, I will just take five to 10 minutes after the class

2:25:03

to do it, just allow me a little time. So I'm here. Herepiae up-the-the-this-law-fala-wola-ch

2:25:09

upload-the-the-only. The only thing I will do is, we'll be able to remove-per-the-grop-wale-th

2:25:15

thing. So you'll be able to refer to the contents under the 5th June folder. So for now,

2:25:19

I will quickly put the annual reports. This is what we have seen already.

2:25:27

And the final code file, I will just update that Open AI with GROC and I will share that

2:25:32

with you in the same 5th-June phone deck. But for now, you'll be able to see these two components,

2:25:36

okay? And again, just to summarize the entire conversation, we have seen, you know, we have gone over

2:25:43

the concept. This is again the same story we have been doing for two days, configure top retrieval,

2:25:49

how to decide the value of K, embeddings, vector search, all these things we have seen. Assemble the

2:25:54

retrieve chunk into a prompt with clear delimiters. Delimiters,

2:25:57

mottes, what type, hash user, hash context, you're you, how do you basically write that

2:26:04

prompt? System message, user message, and context. All that will come in the same two.

2:26:09

Okay? Very important. Generate answers that site, which chunks support each claim. So you can do

2:26:13

an informal grounding check.

2:26:15

Like, as our here here here answers are, what is the capital? We were able to do a manual check.

2:26:21

Okay, manual check. Okay, manual check and you can see what are the chunks that are

2:26:24

retrieved. Here we asked, based on whatever question I'm asking, informally, you can go and

2:26:29

check what the retrieve chunks are. And then you can trace it back to the metadata and say,

2:26:34

that, this is your chunk and this chunk of this chunk of this file from, this page number

2:26:38

are. So we can actually do, this is again from a debugging perspective. If any, you know,

2:26:44

kind of errors are happening, then you can go and do the debugging. And finally, build a complete

2:26:49

end-to-end drag script that ingest retrieves and answers. This is a small thing. But definitely, I will

2:26:54

encourage everybody to use my code snippet, which I'll just be sharing here,

2:26:57

use my code snippet and effectively maybe build a rag application on some of your own

2:27:02

personal use case. Okay. All right. Hope everybody's clear. Everyone's aligned with the rag part.

2:27:10

Okay. So a lot of, lot of interesting things today. And I think a lot of great questions,

2:27:16

chat, GPT, memories. Yes, all we make here. Okay. But code part is something you. I think,

2:27:23

just take a look at it. Just go through it. I think in the class, there is this entire code that we saw.

2:27:30

So if you go through it once, I think it's very simple. If you want me to recap it very broadly,

2:27:35

Ubrage, uh, code k' chunks, what are the modules? What are the modules?

2:27:40

Uh, modules, uh, summedo. First module was you load the PDF, five PDF loaded.

2:27:45

Okay, second module is chunking. This is how you should remember the code. Okay?

2:27:51

First module is you'll load the PDF. Second, you'll load the PDF.

2:27:53

module is chunk. Chunking. Third module is you are using sentence transformer and you're

2:27:59

creating the embedding. Vector DB create. This is the third module. Vector DB

2:28:03

is. This is the syntax. This you cannot, yes, you don't have to memorize. This is just a module. It's a

2:28:09

syntax that is there. So I will recommend you like don't try to buy heart it. But up modules

2:28:15

to say some load kia, chunking here. You have your embedding here. And after the embedding is done,

2:28:21

you define the retriever. K equal to

2:28:23

five top five chunks retrieve or retrieve or what is the retriever. And after that is done.

2:28:28

Now we go back and we define the, the rag system message, user message. Okay. And finally,

2:28:36

this is the whole the rag pipeline. Yeah, your prompt. Okay. So you can, you can go over. These are

2:28:43

these are the modules that you can remember in the code. If you refer to my notebook, some of the code aspects

2:28:50

will be a little redundant. But look, you'll look, you'll see what he import statement.

2:28:53

I might have used which is by the notebook looks a little longer. But I'm sure if

2:28:58

you just maybe take some time after the class and just walk through the code, you'll find it

2:29:03

absolutely simple. Okay, but you go through if you still have some doubts. I will get it clarified

2:29:08

for you next class. No worry. All the library is in land chain. Exactly. Everything is in

2:29:14

land chain. Langchain makes it very easy and Langchain is a high level framework. Sub-langchain

2:29:19

now. Now look, here we have retriever used here. Okay. Now, look. Here we have retriever used.

2:29:23

So you think, sir, the retriever from here. It is all coming from Langchain.

2:29:30

Lankchain. Lank chain, vector stores, import, chroma. And that chroma from our

2:29:34

other things are. Now, look, the retriever we defined here. That retriever is basically coming

2:29:39

from here. Chroma. Chroma. Okay. This all Lankchain library is here. So

2:29:49

Lankchain is a high-level library. When we're agents be carrying next module, we'll be using

2:29:52

lanchine extensively because lank chain makes it very easy for the development to happen.

2:29:57

It just makes it very simple for you to go. All right.

2:30:04

Thank you, everybody. I think that is pretty much all that we have for this session. And I hope

2:30:09

everybody is clear. Everybody got a full flavor of rags at this point in time,

2:30:14

whatever, you know. The agent is basically a different idea, Yograj. But I will take that up.

2:30:22

When we built agents, very interesting that you ask this question.

2:30:25

When we're agents back in the agent, rag will be like a tool in an agent.

2:30:30

If you're a larger agent, rag will be a part of it.

2:30:34

And then when we come to those conversations, we'll make one rag not make, we multiple rags

2:30:38

will make. So, it's again a slightly different concept right now.

2:30:43

We may not, but since you ask this question, so rag will become a tool in an agent.

2:30:47

That agent type tune will.

2:30:48

So, we've got a whole application case as I'm going forward.

2:30:54

The rag will basically become a tool going forward.

2:30:59

But you know, my radio is still running.

2:31:02

It will be very interesting.

2:31:03

You guys can try it out.

2:31:04

I don't know how far it will support the load.

2:31:06

But this is my link which I use today in the class.

2:31:08

You know, you want to go to that URL and try.

2:31:11

See, my Gradio server is still running.

2:31:14

So you can also go to the URL and you can type a couple of messages.

2:31:16

Now type for what is the annual revenue of Tesla.

2:31:18

Can you all confirm you're seeing the result?

2:31:21

And you can do that activity at the end.

2:31:24

You can see it's a very nice public URL.

2:31:26

It's not safe.

2:31:27

As I told you, it's for demos and POCs.

2:31:29

But this is like how you can quickly, you know, kind of mock up a,

2:31:33

mock up a real application.

2:31:34

You have a couple of one application

2:31:35

and a new URL to share.

2:31:39

And they can also try out.

2:31:40

Today, you can ask a question.

2:31:41

Here here you have upload option be desic.

2:31:42

We have that level to go.

2:31:45

But you can also maybe, you know, give an upload option.

2:31:48

You know, upload.

2:31:48

option though where users can upload a PDF and they can get answers.

2:31:51

That's enough for all those interesting things you can go back and do.

2:31:55

Anna?

2:31:56

Aya, Raji, did you get the answer?

2:31:58

Is it working?

2:32:04

Chalo, very nice. Excellent.

2:32:07

Okay, great. Thank you. Thank you guys.

2:32:09

You can take some time to try the link.

2:32:11

And in the meantime, I'll pass it on to Pratav.

2:32:13

Thank you, everybody.

2:32:14

Take the weekend.

2:32:16

Take the time that you get.

2:32:17

Try out the demos.

2:32:18

And I will see all of you once again in the next session.

2:32:22

Yeah.

2:32:22

Eubraj, over to, sorry, Prath, over to you.

2:32:25

Thank you.

2:32:27

Yeah, sir.

2:32:28

Okay.

2:32:29

All right.

2:32:30

Thanks again for another great lecture.

2:32:33

And thank you, students, for joining.

2:32:36

I will release the feedback poll now.

2:32:38

And post the feedback poll.

2:32:40

We'll have the Mendymeter session.

2:32:42

So the feedback poll is live now.

2:32:46

Please fill the feedback poll.

2:32:48

And once the feedback poll,

2:32:48

feedback poll is done. I will start the Menti meter quiz.

2:32:55

Yeah.

2:32:56

Okay.

2:33:18

So I've copied the link.

2:33:20

I have sent it in the chat to everyone.

2:33:23

I think there's one person who has not yet completed the poll.

2:33:29

So I'll wait for, I'll wait for a couple of seconds.

2:33:38

Maybe like 15 seconds.

2:33:40

And then we'll stop.

2:33:45

I'll end the poll and I'll start the MENTimeter course.

2:33:47

start the MENTIMENTR quiz. Okay.

2:33:55

Hope you don't find the quiz to be too difficult today.

2:33:58

I'm not sure the difficulty level you guys are used to because this is my first time as a panelist.

2:34:07

So with you guys.

2:34:09

All right.

2:34:10

Ending the poll now.

2:34:12

And we can start with the Mentimeter quiz.

2:34:16

So I have five questions.

2:34:17

I hope everyone is familiar with this. Can we have some more players?

2:34:24

Okay. Thumbs up in the Mendi-meter quiz if you want me to start with only these many people.

2:34:39

Oh, okay. It seems everyone is ready to go.

2:34:42

All right. If anyone wants to join, they can join in later, I guess. I have sent it.

2:34:47

Just sending the link again.

2:34:57

So yeah, why are context delimiters added to the prompt?

2:35:02

Whenever you are sending a prompt to the LLM or to a model,

2:35:10

wire context delimiters added.

2:35:12

Suppose this one will not be too difficult for everyone.

2:35:20

All right.

2:35:22

Yes.

2:35:24

So context delimators mark the boundaries of the user query because for an LLM all text is basically the same thing.

2:35:32

So it needs to be able to understand the user query.

2:35:35

What is the difference between a user query and something else?

2:35:39

Maybe the system prompt or whatever.

2:35:41

So yeah, great. All right.

2:35:47

Alright.

2:35:48

Okay, next question.

2:35:54

So there are like 13 people in the session.

2:36:08

Okay.

2:36:09

Okay, which rag stage finds the nearest stored chunks for a query?

2:36:14

So I have all the four stages of a rag.

2:36:18

Which stage finds the nearest stored chunks?

2:36:25

Again, pretty easy question actually.

2:36:30

Awesome. No one got it wrong.

2:36:33

Great. Great job.

2:36:35

Sayan Sir has mentioned in chat that you should.

2:36:38

that you should check your shared folder in about an hour.

2:36:45

Sansa they have the link, right?

2:36:49

If, okay, I think the answer is not.

2:36:52

All right.

2:36:53

I hope you guys have the link because I have not saved it.

2:36:57

If you want me to read, if you want me to get it from sir, just let me know.

2:37:03

Okay. All right.

2:37:05

Okay.

2:37:06

Okay.

2:37:07

Okay.

2:37:08

If anyone wants the link, they can just message in the chat and one of you guys can send it.

2:37:15

All right. Moving on. Next question. Okay. Three more questions to go. What is the key task in an informal grounding audit?

2:37:34

So when I, grounding audit basically means you are.

2:37:38

trying to ensure that all of the data in the vector DB is accurate.

2:37:47

So if you think about it, based on the options, you should be able to get the guess the correct answer.

2:37:59

All right, let's see.

2:38:02

Okay. Okay. All right. So yeah, fairly. It's a.

2:38:07

It's equally divided. That's interesting.

2:38:10

So the first thing that you would do, or rather this is, this is why it's a key task, is you would map each factual claim to a retrieved chunk.

2:38:18

Because, I mean, of course, removing low ranking chunks from the chroma DB is another task, but this is something that you would do second, right?

2:38:26

Usually.

2:38:27

The first thing is most important, which is mapping each chunk.

2:38:31

So that is why this is the correct answer, but people who have tried this one, not a,

2:38:36

one not a not very off of the mark okay so yeah good job guys. Not really off the mark. All right. Last two questions. I think this one might be a little tough tough. Okay. Yeah.

2:39:06

Let's see. Relevant chunks exist in the vector db of course, but the reply is generic from the LLM.

2:39:13

So what is the likeliest cause?

2:39:19

Okay, if you look at the options, I mean, it's pretty obvious actually.

2:39:23

But still, the understanding the reason is more important. Even if you don't get it right, it's fine.

2:39:33

All right, it seems everyone is voted.

2:39:36

would be oh okay um all right let's see the default top K value is three so um that would not

2:39:46

directly cause this basically the reply if the reply is generic then your LLM is most

2:39:53

likely that's why I said this is the most likely cause right if your LLM is not able to retrieve the

2:39:59

context or it's not able to just get to the vector DB at all that's that's the most likely cause right

2:40:05

default top K value three is probably it's a probable cause but then it is less likely than

2:40:11

like i mean first you would check if the power is on right before trying to solve a problem so

2:40:17

this is the thing all right but still still great job guys you guys are actually thinking

2:40:35

regardless of who wins you guys actually put in thought and effort in answering these

2:40:41

questions so again great joan what is the most dangerous grounding illusion in an r a g system

2:40:49

so yeah this might be a little difficult actually um but you have to understand what is like

2:40:58

what is something that is like that seems like grounding but it is not actually grounding

2:41:05

So you can think about it like the LLM is confidently giving an answer, but it is wrong.

2:41:19

Yes, fluent answers inheriting authority from nearby relevant context.

2:41:24

I am yeah, great job you guys, you've almost all got this correct.

2:41:29

Retrieved evidence increasing prompt length excessively.

2:41:32

So this is not.

2:41:35

exactly a grounding illusion i mean the evidence uh retrieved evidence will increase the

2:41:41

prompt length excessively it will cause issues in uh in an r a g it will increase your token size all of those

2:41:49

things but it is not going to give you a wrong answer exactly right but this if the nearby

2:41:58

if nearby context is completely different then it is very likely to give you confidently wrong

2:42:05

answers. Right? I hope you guys understand when I say an LLM will lie confidently.

2:42:12

So yeah, this is this is why this is a very good, very good thing to understand that your RAG

2:42:19

or vector vector database, chroma or whatever you're using, is having nicely separate, is having

2:42:28

nice separations between relevant contexts. Okay. Okay. All right.

2:42:35

Let's see. It seems like, okay. All right. So congratulations to Casper, whoever they are. Oh, Rajdeep. All right. Great. Congratulations. And everyone else, good job. You actually tried. And I mean, the lowest person is not on a zero. So you did well. Okay. Great job. All right. Guys. Guys, have a nice.

2:43:05

weekend and you will be treated by your existing TA in the next lecture. Okay.