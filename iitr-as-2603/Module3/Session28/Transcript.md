0:00

Thank you.

0:01

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

Thank you.

4:02

Thank you.

4:32

Thank you.

5:02

Thank you.

5:32

Thank you

6:02

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

Thank you.

20:20

Thank you.

20:50

Hi guys.

20:54

Hi guys.

20:55

Sayan sir would be joining within maybe five minutes.

20:59

Please wait five minutes.

21:17

Sorry for the delay.

21:20

Thank you.

21:50

Thank you.

22:20

Thank you.

22:50

Thank you.

23:20

Thank you.

23:50

Thank you

24:20

Thank you

24:50

Hi, everybody, very good

24:57

very good evening all of you

25:01

we will be starting on here.

25:04

We will be starting on here.

25:20

Thank you.

25:50

So today.

25:57

So today we start off with a new topic guys and we'll be starting out with a new topic guys and we'll be getting into, we'll be starting out with a very, very interesting topic.

26:20

called Retrieval Augmented Generation.

26:22

So just to set the context what we have done and where we stand right now.

26:32

So let me quickly share my screen.

26:37

So we are currently in the we are currently in this particular module and here in this module

26:45

until now we have covered all the ideas with respect to what are API

26:50

and all those things. So we have talked about APIs, we have talked about the process of writing a prompt, how do we write a prompt.

26:58

So we looked at the concept of Olama, how to use open source models. We talked about that idea. What is the meaning of open source, how to call open source models.

27:09

And until now, we have a decent understanding of local and cloud-based models. That was also a focus area. We saw the pros and cons of each one of them.

27:18

And here we start out with a very, very, very.

27:20

Interesting session called rags. Now rags are broken down into four classes. We've got total four sessions on rags. Today will be a very introductory session. It will be a very basic introductory discussion to what rags are. There isn't much hands-on that we have today, but it will be a basic demo that I will show you how the rag thing is working without too much of code.

27:40

But then a big focus area of today's class will be the hands-on. We will see a lot of, sorry, a big focus area of today's class will be the concept. We will try to understand why rags.

27:50

because oftentimes when you learn a new topic, we should understand and appreciate why we are doing it, why we are learning something new, and that is what is going to be the main focus area for today.

28:01

We will try to understand first part will be why rags and the second part will be, we will look at some of the building blocks of a rag application.

28:09

And as I said, like, this will be covered over, you know, it will be covered over overall four sessions.

28:14

So we will see a basic introductory discussion of rags today.

28:17

So that is going to be the main focus area.

28:20

So now with this in mind, let's move on to our main content.

28:31

I will use some references of the content today because I think the materials are very nicely crafted

28:36

for today. So we'll use some of the general outline from here. Now, very interesting. If

28:43

you take a look at it, let's understand first of all,

28:50

some of the limitations, right? Why LLMs are not enough? Why large language models

28:56

generally are not enough, right? Remember, all these large language models are trained on public

29:02

internet data. Like when these models are trained, I have used a term before as well with all

29:07

of you that these models are trained on internet scale data and they are having a lot of pre-trained

29:13

knowledge, right? So these models are trained on a tremendous amount of internet scale data.

29:18

and they are having a tremendous amount of pre-trained understanding of things.

29:24

Pre-trained knowledge is what we call it, right? That means they know a lot of things.

29:31

So if you go and ask a question, if you go and ask some general questions to your large language models

29:38

about some specific events that happened, it may not be able to correctly answer.

29:47

Right?

29:48

So this is the.

29:48

general idea. So I think the best way to do it is for me to demonstrate this to you

29:53

what what this particular diagram is talking about. So I will go to my GROC platform for a minute.

30:01

This is the GROC platform, all of you can see. We have used this before as well. I'll go to the

30:05

playground and I will choose the Lama 70 billion versatile model as an example, right?

30:11

Now we have seen this system message, user message. We have seen this part. Let's say system

30:16

message is you are a helpful assistant. I'll just keep.

30:18

it basic you're a helpful assistant very general purpose

30:23

thing we are trying to build right now you're a helpful assistant and user

30:28

message would be system message is you're a helpful assistant that is what we are

30:32

doing and user message would be uh let's say i'll ask a question um so so um so you know let's ask a

30:44

general question right so we had this uh i'm sure many of you are watching

30:48

the FIFA World Cup right in the FIFA World Cup Germany got eliminated right it was a big upset

30:54

okay so many of the German fans were very unhappy let's ask this question why did Germany

31:01

get eliminated uh why did Germany get eliminated

31:10

against Paraguay in the FIFA 2026 World Cup

31:18

Now think about this question for a minute. Think about this question.

31:23

This question is GROC actually will not be able to answer. When I, when I run this in GROC will say,

31:30

since my knowledge cutoff is December 2023, I don't have the information about 2026 World Cup.

31:35

Nipa. So this is the challenge. Challenge number one, we will discuss another challenge also.

31:41

So challenge number one is all these large language models are only trained with data up to a certain point in time.

31:47

and that particular thing is called a knowledge cutoff that means when the Lama 3.3 model

31:54

was trained was time paying the entire data was collected latest as of December 2023 all the data was

32:01

collected by then and then that is how the Lama 3.370b model was actually trained it was trained on that

32:08

data it was trained on that real world data that's the intuition so the knowledge got

32:14

knowledge cutoff is December 2023 that's the intuition right now the thing is

32:26

definitely if you ask a question on a different date on the more recent dates it doesn't have

32:31

answered to that question right this is challenge number one so it will not be able to

32:35

answer real time questions for you challenge number two let me just do the minus let me discuss another

32:42

a challenge. I will take a very specific, imagine I want to ask a question about

32:49

a very sensitive company policy or something, okay? So I'm just, I'm just, you know,

32:57

giving like thinking, thinking, you know, generally. So I'm just taking an example of Siemens

33:03

as an example, right? So what is Siemens' latest latest HR policy which employees

33:12

are really liking. Okay? Give me the exact details. Along with the latest high

33:32

percentages. Now remember the question that you're asking right now, it is a very sensitive question.

33:39

means this kind of information will usually not be in the public domain. This company

33:44

memos in right? So when Siemens HR team will probably send a internal mail to all the company

33:49

employees, this is how it usually happens, right? If you ask, excuse me, if you ask a general question,

33:55

what is Siemens' latest HR policy which employees are? It will not be able to answer. Because the

34:01

Lama model again, when it was, when the knowledge cutout was collected back in December 2023,

34:07

it did not have general Siemens data. Like there were two.

34:09

problems. One is it doesn't have recent data that we already saw. Anyways, here it will not

34:13

have the Siemens recent data. And number two, it will not have access to, it will not have access

34:20

to Siemens internal confidential documentation. It will not have access to that. So it will

34:26

anyways not be able to answer this. So if I go and ask this question, you will see that the assistant

34:31

will say, I don't have access to real time or the ability to browse the internet

34:36

additionally and this is the important part. This we already discussed.

34:39

I don't have information about Siemens current HR policies. This is an important thing.

34:48

So if your use case is to get answers to questions about internal proprietary data,

34:59

your organization data, the team that you are working in, the project that you are working on,

35:04

if you're from the HR department, you might have some policies, you want to get some questions answered about that.

35:09

the normal language models will not help. And you're able to see that.

35:15

Because he's no no, it is not trained on that data. And that is exactly the first part of what we are

35:20

trying to highlight. The LLM, LLM doesn't know that. LLM doesn't know that. LLM has a general understanding,

35:27

but it doesn't know the current data and also data about private documents, but the company reports, strategy

35:33

documents, internal data, which is not part of the model training. It doesn't have access to that.

35:38

And the important thing is without your documents, the LLMs can be confidently wrong.

35:43

It can be confidently wrong. El LLMs will give the wrong answers.

35:48

So we have the, you know, we have the knowledge cutoff problem. We discuss that. We have the no private data

35:55

problem. Internal documents were never used in training. Right? And another problem that is there is

36:01

hallucination. Hallucination is again something we will keep seeing from time to time. Hallucination

36:05

basically means that the application gives an.

36:08

incorrect answer. So you ask a question. See, sometimes what happens is, you know,

36:13

even even we humans do it at times. So you are asked a question. Even if you don't know the answer

36:19

to the question, you might sometimes give a wrong answer. But you know, it's sometimes very

36:24

embarrassing to say, I don't know. So if you are asked a question, you will still try to answer that

36:29

question. You will try to attempt it. Okay, okay, let me answer it. Now attempt. So that's the,

36:34

that's the idea behind hallucination, right? That's the concept.

36:36

I hope everybody is aligned. That is the basic idea behind what hallucination basically refers to.

36:44

Now, these are the specific problems that we will solve in RAG. So first of all, I wanted to discuss

36:52

the problem. And now we will look at the solution. Rag is the solution. So rag is usually used in

36:58

scenarios where you want to use your company's internal. You want to basically get some

37:06

some questions answered about your company's internal confidential data.

37:12

Joe LLMs.

37:12

I cannot go and ask a LAMA model. I cannot go and ask a mistral model. I cannot even go and ask a

37:18

GPT model. Even if you have the API keys with you, you cannot even go and query a GPT model saying,

37:24

okay, please tell me Siemens' latest HR policy. It is not trained on that data.

37:28

These are real challenges. And this is exactly the problem that RAG is solving. Now, what is

37:34

right? How it is doing? All this we will discuss. But first of all,

37:36

we wanted to follow this problem solution approach.

37:39

So we know the problem. Problem what problem. Problem is RANG. And we will see what RAG is right now.

37:45

How is Rag? We will see. Now.

37:50

So the general idea is, if you see, what we are trying to do in RG is, you can take a look at it at a very high level.

38:01

I mean, the process is kind of explained in a lot of detail. And I told you, like, we will do this

38:06

our four classes, like not one sessions. I don't want to like overburden too much in one class,

38:11

but it will be four sessions we will have. But at a very high level, what are we doing?

38:14

What are we trying to do? So this is a, I think it's a very nice example that is taken here.

38:20

Very nice example. Imagine we are trying to take an open book exam. Okay? This open book exam.

38:27

So there is a library. There's a library. Library in there is a rank of books and neatly organized.

38:34

There's a librarian. There's a librarian also.

38:36

that is there and the librarian lady is the person who is responsible for stacking the books

38:44

in the right order here the history books will be there geography book will be there

38:48

computer science book will be there like that you know when we go to a library we see the books are

38:52

neatly stacked in different categories serial numbers indexes so this is one first part i wanted to

38:58

clarify the library this is a general analogy and later on you know once we understand this example

39:05

I will connect the dots and tell you what is this called in the in this rag.

39:10

So technically it's called a vector tb. So we'll see that later. So first we will have to have a very

39:14

good library. Library may all the books should be arranged in the right order so that if any

39:21

user wants to access a book they can easily find it. Ultimately finding is the most important thing

39:27

like informational knowledge is all around us today. If you look at the access to information, the access to

39:35

information that each one of us in this audience we have we have access to every information

39:39

but i think the biggest challenge is sometimes is getting things organized we need to get our

39:43

life organized that when we need something are we able to get it so we also need to build a library

39:48

in how makes all the digital clutter know like have a library now that is step number one have a

39:55

good library step number two when you are asked a question question that you are asked is explain

40:02

and transformer architecture. This is the question that is asked. What will happen?

40:07

This is what I told you. The language model doesn't know the answer.

40:10

Nei. Imagine you are taking an open book exam. Open book exam means the LLM is not supposed

40:16

to know anything. If LLM can LLM will answer from its pre-trained knowledge, but that's that's the whole

40:22

idea. That's what we are saying, right? The LLM doesn't have the answer to these questions. So next

40:27

time you're asked any question, the LLM will look up from the library. It will always take

40:31

take help. So in this kind of a system, it will always go and take help. I can, so it will say,

40:36

okay, you're asked a question, sorry, I cannot answer. I will take help from the library and then answer.

40:42

Asked another question, sorry, I cannot answer. I will take help from the library, then answer.

40:48

So next time you're asked this question, explain transformer architecture. You, you don't know anything.

40:53

You're blank. But you're very good reasoner. You can reason very well. You don't know anything. You're not

40:59

memorize anything, but you can reason very well. So you've got this question, explain

41:03

transformer architecture. What you will do? You will smartly go and ask the librarian.

41:08

Yeah, then you will go and search in the library. You will go and search in the library

41:15

through an assistant. You will have an assistant, let's say. And you will tell the assistant,

41:18

that, go and look and decide where the transformer book is there. Go fetch it for me.

41:25

the librarian gives the book to you and then you simply take the respective portions on the book

41:33

that much knowledge you need to have right you need to have that much intelligence at least when you

41:37

you get the book you should be able to copy the answer you know we have all done this in exams

41:41

but you should know what to copy also sometimes right so you should know which portions of the book to take

41:46

and you have to copy the answer and get it that is exactly what rags do at a high level so the so the

41:55

thing in this analogy is when you're asked a question, the person is not directly answering it.

42:03

That means the language model is not directly looking at the question and giving a response, no.

42:08

And I would say part of the reason is because the language model doesn't know the answer.

42:11

Nehapata. It's not trained on that data.

42:15

Now here I'm asking a general question to explain, but it's going to be a more sensitive question.

42:21

Let's say what is Seaman's HR policy? Let's explain the latest.

42:25

the language model doesn't know it so it will have to consult a library the library will have the

42:30

entire knowledge base now how the library is getting built and all that that's a different story

42:36

that's a much bigger story we'll see later on but the library for now is the complete document base

42:43

that's everything so you're not supposed to remember it you get the question go talk to the librarian

42:50

library will efficiently search okay you know based on whatever questions i and got uh let me find me

42:55

find out the similar books for cert and now from there you you figure out okay okay

42:59

i think these two three paragraphs will do for my answer what two three paragraphs you copy

43:04

and then you try to further streamline the answer from there that's it so that is basically

43:10

what rags are at a very high level right rag connects an lm to your knowledge base

43:18

it retrieves relevant documents adds them as context and generates accurate rounded answers

43:23

this is what is going on at a very high

43:25

level in a rag I think this diagram also is a follow on but here we have introduced some

43:30

more technical jargon which will probably make it a little bit more clearer what we are doing

43:36

on the extreme left hand side we have the knowledge base which is the library

43:40

I told you first of all building that library itself is very very important

43:44

technically that's another process altogether we will see later on in the further sessions

43:49

it will consist of books papers notes reports web pages up which it will be the complete knowledge base

43:55

so you have to build that library now next you are asked the question what is the

44:04

transformer architecture sorry explain transformer architecture that is the question you're

44:09

asked based on whatever question you're asked what will happen the retriever

44:14

will find the relevant information from your library right so i repeat again

44:19

based on whatever question you are asked the retriever will find the relevant information from your

44:25

So that means you are asked this question the retriever is who is the retriever,

44:31

the retriever is the librarian. So Librarian is your helper.

44:34

So, you're a question asked you, Librarian will go and retrieve the relevant information or the books from your

44:40

library. It will retrieve those relevant documents.

44:44

I mean that Transformer's three book

44:46

and then you'll put together. And this is the context, this is the information that is present

44:52

in the documents right now.

44:55

So now you see very interesting. The original question, the user input was explained

45:02

transformer architecture. But now that, but now what is happening is, but now what is happening is,

45:12

if you see, you have this question that you consult the librarian, the librarian returns those

45:20

documents to you, the document chunks to you, sections, portions of the documents, portions of the

45:24

of documents it returns to you. Three documents chunks you have. And this is basically the

45:31

new revised query for the LLM. This is what you will now use to answer your question. You are the LLM.

45:38

Think of it this way. I think that's the analogy. You are the large language model. I think that's

45:41

the way we will look at the analogy. So who is the LLM in this picture? The you, the person who is taking

45:48

the exam and who is the retriever the librarian? So you are the person taking the exam. If you are the

45:52

person taking the exam. If you are directly asked a question, here LLM is, so if you're

45:57

giving the user input directly, it cannot answer. Because I told you it doesn't have the internal

46:01

knowledge. So it will take the help from the librarian. Library will give the document chunks,

46:08

similar chunks, which can be used to give the answer. And, and now this is your revised prompt.

46:18

This is your revised prompt, what you're seeing. So what you're seeing on the screen is your revised prompt.

46:22

Okay? So now not only are you asking the question, explain, transform, and architecture,

46:30

but the LLM now also has access to the documents where to look up, look the answer from.

46:37

LLM is this person writing the exam.

46:39

Abhi, he has not only question, but he has that context information be here. Okay, whatever I need to

46:45

answer that question. You can see that. It's almost like you go to the exam, you see the question,

46:49

or left may you have some notes say. And you're writing the exam.

46:52

open book, who notes have exam. It's like that. Now that large language model, that brain

46:57

not only knows the question, but it also has the context. And based on that, is able to give the answer.

47:03

So generates the final answer using the provided context. The LLM was initially not able to generate

47:09

the answer just based on the question. Because no, no, no, and now the moment you

47:17

add the context, it is able to generate the answer.

47:22

And that is why the term retrieval augmented generation, why the term is getting used.

47:29

That means first you retrieve the relevant chunks, then you augment and based on that you generate.

47:37

And that's why the term retrieval augmented generation is what we are able to see.

47:42

And if you just take a look at it, rag again, retrieve, augment, generate. Retrieve means

47:46

you are retrieving the relevant knowledge, right? So you have the, uh, the question.

47:52

question question is asked you you you first you retrieve the relevant knowledge then you

47:58

augment the prompt initially the prompt was just the question explain the architecture

48:06

so first you retrieve the knowledge then you augment make the prompt bigger

48:11

a prompt here can you see it is like the revised question for the LLM you augment the

48:17

prompt make it bigger because you add the context now and based on that you generate a grounded answer

48:22

So that is why we call it retrieval augmented generation.

48:25

So all this while what we were doing in the sessions was normal generation.

48:29

Next time you go back to those use cases we worked on.

48:34

If you talk about that meeting summarizer use case, what did we do in that meeting

48:38

summarizer use case?

48:40

In the class notes file we did, right, at a basic level.

48:42

You know, I gave you a transcript and the language model was able to read through the transcript

48:50

and generate a summary of the transcript.

48:52

it was normal generation. So the LLM was able to directly see the user input

48:58

and based on the user input, the LLM was able to directly generate a response.

49:04

That is what the large language model was able to directly do. So what is rag then? You get the

49:11

question, you retrieve the relevant chunks and based on that, you get the final grounded answer.

49:16

That's the idea. That's the big picture idea. And now these are the things that we will see.

49:21

It's a long discussion. I don't.

49:22

told you it's four classes so we have obviously not going to do all this in one class but you know

49:26

i can see there'll be a lot of questions on this also but guys again just be patient we will see this in due

49:31

course but uh if we take everything today it'll be very very confusing it's a rag is spread over four to

49:36

five sessions actually it's five if you look at another session later in fact it's actually six

49:40

because there is one more class on rags we are doing later it spread over three weeks okay so we will

49:45

take it slow so these are the general analogies your books are your documents

49:52

your library or your catalog is like your umbedings and vector store we will see that just

49:57

remember the terms all of you for now your librarian is the retriever

50:02

reading before answering is nothing but the context and finally the this is the final generation

50:08

so this is the basic analogy of what we talked about in a rank i'm just going to repeat it once

50:14

again you're the llm this is the the human that you see on the picture is like the large language model

50:21

if it's asked a normal question it will not be able to answer because of the problems we already

50:26

cited so now given a question this human being this large language model will console the librarian

50:35

the librarian will retrieve the relevant chunks and it will give it to that llm now the llm has some

50:42

help now the large language model has access to the question and it also has access to the

50:48

the retrieved chunks those retrieved documents which can potentially help it answer that question

50:55

and this is the final revised prompt for the llm and based on that it will be able to generate

51:01

the answer and if i have to connect the dots back with your

51:08

semen's HR policy or any kind of company proprietary data all that story that we were

51:13

discussing i told you that the large language model this guy is not supposed to

51:18

to know if i ask the question please tell me about semen slated say hr policy and all that it will

51:22

not know that this guy will not have that answer to that question so next time you're you know you're

51:27

asking a question about a very internal company policy or something of that sort what will happen

51:34

based on the question this guy will go and consult the library and retrieve the top three

51:39

top four top five relevant chunks okay and get the answer so in fact what i'm getting at is that

51:47

semen's hr manual any company semence sogia mercedes cisco all the top companies in the world

51:54

every company will have our hr guidelines booklet any big company will have documentation right

51:59

hr in hr me what's what's how much of bonuses it's not as if one fine day people wake up and

52:05

decide no there's a very proper detailed guidelines that available and all that is text there are

52:10

text guidelines because these go through audits these goes to compliance reviews right there's a very

52:15

detailed amount of text text data the HR department will have. So all that must be first

52:21

organized in the library. And that's a massive discussion. Okay, I'm just trying to give you

52:27

the analogy. So the entire company's internal document data, text, it has to be first organized in the

52:35

library, indexed. It is like a database, you can't. Another thing I want to add, this is usually a very

52:42

secure on-premise database.

52:45

because you will never host your company's proprietary data somewhere else.

52:52

So this will be present within the company premises, within the company servers.

52:56

It is highly secure. So the library should be like a vault. The library is like a vault.

53:01

Like nobody should have access to it. There should be no external access to it. So the entire

53:05

company's confidential data, everything, text data, documents, PDFs, docs, whatever, all that has to be

53:12

part of that vault, the library. That's the first thing. And next time any kind of question

53:18

is asked, any kind of general question is asked, the LLM will not know the answer to that question,

53:23

but what we can do is the LLM can go and consult the librarian. Librarian will retrieve the

53:29

chunks from the vault. That vaults et sort of chunks retrieve karek and based on that LLM will answer.

53:35

So now it will be able to say, okay, what is Siemens HR thing? So that is the thing about what

53:41

rags are doing at a high level behind the scenes. Right? And Gurtig, just to answer

53:50

to your question, I think I already answered that. I already answered that. So absolutely. So

53:54

as I told you already, LLM, does it read our library? Yes, it does. It is reading our library

54:00

only for reading or retrieving, but it does not train itself on the library. It can never,

54:03

it doesn't a training access, okay? Very dangerous. LLMs will never be trained on the internal

54:09

on library data. Library is like a vault. I already told you. So LLMs can only read

54:14

and retrieve and access the information. LLMs will not be able to train on that, okay? Just to clarify.

54:20

And Arnica had asked a question sometime back how LLMs connect to RRAG. Arnika, that's a

54:24

that's a deeper discussion. I'll come to that. This is the analogy I'm talking about. How LLMs

54:28

connect Rack, we will see that. LLMs connect Rack. I think that like, I mean, I think the question

54:34

is not like proper LLM are a part of Rang. You can be coming to that. We are in the early stages right now.

54:39

So I think, I think what you meant is how LLMs connect to the library. I think that's what you meant.

54:45

Because rag, this whole thing is rag. I think what you meant is how LLMs connect to the library to

54:49

retrieve. We will see that. We will see that. We will see that just to clarify.

54:53

So, it's a setting. It's a setting. These are basically, when I show the code demos to you,

54:59

it's just one or two lines of code. Instructions. No, no instruction. So Arnica, if your question

55:05

is, is, is it a system message? No, it is not a system message. No. This is a instruction. No.

55:09

or steps here. It is not as if you have to write in English, no. Not like that. It is not part of your system message. It's a simple

55:15

module. So for all these demos going forward, we will use a Lank chain package. Lank chain. It is like one line of code.

55:22

There is a code for retriever. We use and you can retrieve it. It's very simple. Okay. Yeah, we will see that.

55:30

All right. Now, let's move on. And as we discussed, from a enterprise perspective, why are rags preferred?

55:39

Why do enterprises prefer that? Because main reason is basically privacy. The biggest reason

55:47

I would say is privacy. Because if you talk about the HR use case, the Siemens use case that I was talking

55:51

about, HR policy of use case. The company gets the best of both worlds, right? The company is able to

55:58

keep their confidential data, their private data on premise. On premise means on inside their company

56:04

servers. The company is able to maintain their own data in their company servers and like,

56:09

they are still able to get the answers to the questions. So that is the major benefit of the

56:14

the rag system that I will clarify. Okay. Now let's go to the next level. All this while it was an

56:21

analogy. From the library case of say I tried to explain to all of you. Now we will see the exact process

56:28

of the rag. What is going on inside the rack. So let us see that. Let us see that a bit more in detail.

56:35

So that everybody understands this. And this is where we will see the

56:39

the entire pipeline of the rag. What is going on inside the pipeline? Okay. Let us see that.

57:09

here for this one. But anyways, I'll just try to pause here for a minute. Allow all of you to

57:14

take two to three minutes to go through it once. Just give it a read once all of you.

57:39

Thank you.

58:09

Thank you.

58:39

Thank you.

59:09

Thank you.

59:39

everyone's everyone's aligned and i'll explain to you i'll explain to you what this is in the meantime to you what this is in the meantime i'll take up one of my other diagrams also to explain this in a better way

59:51

but just to give it a idea to all of you what we are doing so so subsep first we load the pdfs i told you like

59:58

in a typical enterprise you will have a lot of confidential data for the company so subsep first what will happen is

1:0:06

you will load the entire company's confidential data, PDFs, text, docs, everything here.

1:0:13

This is where you will load the data. Next what you will do is you will prepare. That means even Chang

1:0:18

can do embeddings, right? What is the, what is the thing?

1:0:21

In a way, preparation of the library. You have a library. So the first two steps is to prepare

1:0:29

the library. I told you have to take a lot of effort to build your library. So the library will contain

1:0:35

the entire company's document data. So you have to take all your documents and then you

1:0:41

have to chunk. Chunk means you're trying to divide that data into multiple smaller portions.

1:0:46

Okay. Like for example, imagine you have a 100 page PDF. So let's say you have a 100 page

1:0:55

PDF. So it is very difficult to process a 100 page PDF directly. 100 page PDF you cannot

1:1:03

directly process. So what you will do, you will take the 100 page PDF and you will divide

1:1:07

that 100 page PDF into multiple smaller sections. It is very difficult to process the 100 page

1:1:14

PDF. So what we will do, as I said, we will take the 100 page PDF and we will divide the 100 page PDF

1:1:20

into smaller sections. Smaller sections. Chota Chuta Chachers may divide currently.

1:1:24

That's what we will do. We will divide that into smaller sections. So and those sections are called chunks.

1:1:33

So one very simple example of a chunk could be, let's say, one chunk is one page.

1:1:39

That's the analogy we will take for today. Let's say one chunk is one page.

1:1:43

So your 100 page is PDF. It's a huge amount of data, but we will not be working and processing that massive amount of data.

1:1:54

So what we will instead do is we will divide that into smaller smaller chunks.

1:1:58

Where every chunk is one page. So you have as what you have got, so chunks will.

1:2:03

That's the intuition behind chunky. You're dividing that into smaller chunks.

1:2:08

But remember, 100 page PDF core, you have divided that into 100 chunks.

1:2:15

Each chunk is one page. But those chunks are still text, right?

1:2:20

If you go back and look at those chunks, those chunks are still text data. The chunks are still text data.

1:2:27

And I already told you machines don't understand text.

1:2:31

whenever any kind of processing happens in the machine, the processing will happen in a numeric

1:2:36

manner. So machines inherently don't understand text. So machines, the processing will happen

1:2:43

in a numeric manner. That's the idea. So we will have to take those chunks, those text chunks,

1:2:51

and convert them into chunk embeddings. Chunk embeddings. So these are some numbers. So these are

1:3:00

some numbers which represent the meaning of the chunk. Think of it that way.

1:3:06

Now, how it is done? These are not done by LLMs, but these are done by, let's say, some pre-trained

1:3:10

transformer models. There are already some predefined models which will do this work for you.

1:3:16

We will not be building the models. There are predefined models that we have which will do this.

1:3:20

They are called embedding models. So document a 100 page PDF. You create chunks.

1:3:26

You take each and every one of those chunks and you save them as embeddings.

1:3:30

You have got chunk 1. You generate the embeddings and store it. Chunk 2 generate

1:3:37

the embeddings. Chunk 3 generate the embeddings. And all this gets stored in what we call

1:3:44

a vector db. How do you store it? This is what we call a vector database. This entity where

1:3:51

the chunks and the embeddings are present, let me just maybe annotate it so that people

1:3:56

understand it better. This entity is called a vector DB. You have

1:4:00

a vector db. Maybe I'll just take a cylinder shape like a database. You have a database.

1:4:05

What is it called? It's called a vector db. In other words, this is like your library. You have

1:4:09

library. Okay? Just to clarify what I told you, 100 page PDF as an example. I'm saying every chunk

1:4:19

is one page to how many chunks? There are 100 chunks. There are 100 chunks we have. And remember,

1:4:25

every chunk is like a text. Machines will not understand text. So what you will have to do?

1:4:30

you will have to take each and every one of those chunks c1 c2 c3 up to c00 you will have to take each and

1:4:35

every one of those respective chunks and you will have to convert each and every one of those

1:4:41

respective chunks into what we refer to as chunk embeddings.

1:4:45

This your chunk embeddings. And eventually we will have to go and save it in the vector db.

1:4:51

Inside a vector db will be saving the respective chunks and their corresponding chunk embeddings.

1:4:55

This is what will be saved in the vector db. This is the first part of what i wanted to

1:5:00

clarified. This is the library preparation part. Now we come back to the other part.

1:5:07

And usually what happens is guys in enterprises this happens right at the very beginning of the

1:5:11

workflow. When you are starting a big rag project, this is the kind of thing that you will do right

1:5:15

at the beginning. You will take all your PDFs, you will take all your document data. You will do chunking,

1:5:21

you will do embedding, you will prepare your vector db. So this is the kind of thing that you will do

1:5:24

right at the beginning of the process. Now what will happen? Now, what will happen? Now,

1:5:30

we will come to the general retrieval process.

1:5:33

You are asked a question. This is what will typically happen, right?

1:5:36

User question is asked, but explain transform or architecture.

1:5:41

So language model will not directly know the answer.

1:5:44

If you are asked, if the user asks the question, that means some question is asked to the LLM.

1:5:48

Naturally, machines don't understand text.

1:5:53

This user question will also need to be converted to query embeddings.

1:5:58

It has to be converted to a bunch of

1:6:00

of numbers. So question could be

1:6:02

let's say explain transformer architecture. The user question is explain.

1:6:05

Explain. Explain

1:6:07

Explain.

1:6:16

And we can convert that question user query into query embeddings. Let's say query embeddings

1:6:22

is that point 1 2 minus 0.85.

1:6:27

0.3. Whatever. I'm just giving a very ballpark

1:6:30

understanding. And you can clearly see that this query embedding is very similar to this chunk.

1:6:35

And that is what we are doing in the retrieval. You are trying to retrieve the top K similar results.

1:6:42

You are trying to retrieve the top K similar results. That means whatever question is asked,

1:6:47

like I was discussing in that library analogy, you are asked a question, explain transformer

1:6:53

architecture. Your library end will go and retrieve only those books or only those sections where

1:7:00

that particular topic is talked about. And how does it know? Everything is happening

1:7:05

on the basis of embeddings. Because the embeddings are basically nothing but the representation

1:7:10

of the text. Machines will not understand the text directly. The embeddings are nothing

1:7:16

but the representation of the text. That's the way to look at it. Embedings are nothing but the

1:7:21

representation of the text. That's the intuition. So I repeat again, we have the PDFs, you do the

1:7:29

chunking you do the embedding you create the vector db vector db is the library every row stands for a

1:7:35

chunk we have got chunk one we have got chunk two we've got chunk three each and every row in the

1:7:39

vector db stands for a chunk and we are generating what we refer to as chunk embeddings

1:7:44

c1's embedding k2 embedding yeah hey c3 embedding what is it so we are trying to generate the

1:7:48

embeddings for every single chunk and that is what we call chunk embeddings and now we will do

1:7:55

retrieval next time when you're asked a question when a user asks the question

1:7:59

and explain transformer architecture you will convert that query into what we refer to as

1:8:05

query embedding we will take that original user query and convert that into query embedding

1:8:11

and now we will take that query embedding and effectively go and look up in the vector db.

1:8:16

Whatever vector db is there we'll go and look up in the vector db and find out what are the

1:8:20

top case similar chunks.

1:8:23

but to answer that question the question is represented by its query embedding to answer that question

1:8:29

can we go back and look up in my library or the vector db which are the chunks there are

1:8:34

hundred chunks mind you here there are 100 chunks which out of those 100 chunks are similar to the

1:8:40

question that is asked i will retrieve those top two or top three whatever the value of k is

1:8:46

okay and this is what is called the retrieved context yeah your retrieved context and now this becomes

1:8:52

your fresh augmented prompt i told you right so initially you were just asking the question now not only

1:8:56

you have the question you also have the retrieved context so this this entire thing together

1:9:03

is like your new uh user input and that you sent to the ln to give an answer get an answer

1:9:13

that's what rags are basically doing intuitively okay this is one more uh one more thing that we

1:9:20

are able to see documents prepare chunks embeddings you will save save in a vector DB

1:9:26

which is like a document index like a library this is the first one part right let me show

1:9:31

this also you have the pdf's hundred page pdf prepare chunks converted to embedings and create

1:9:38

the vector db this is usually the first part of the process or here herep retrieval

1:9:44

whenever the user question is asked you go and look up in the library which are the similar

1:9:49

chunks retrieve the top to relevant chunks and when llm will generate the answer based on that and

1:9:56

and hence the term retrieval augmented generation you first retrieve and then augment

1:10:01

and then you generate and this is again i repeat particularly useful for proprietary internal

1:10:06

confidential data uh steps one and two happens for every new query we ask for only one time

1:10:13

uh good question steps one and two will only happen one time one time three four five

1:10:19

every time new question is asked he'll go and search

1:10:22

retrieve correct answer every time but very good point one and two will only happen one

1:10:27

time usually one time see i'll tell you what vector database is a very special kind of

1:10:32

database just like you've got relational database artdbms hey up to my SQL you might have

1:10:36

studied a bit of SQL in your first module first module before me you were studying some something you

1:10:42

were doing right so you would have studied along with python for about my SQL you would have done

1:10:47

that is the rdbms relational database

1:10:49

management system vector databases are similar to that either be we go here also you have

1:10:56

documents you have you have text and you've got text embedding these are text chunks and there are

1:11:00

chunk embeddings so the same principles that you will use to maintain your relational database

1:11:06

you know you will oftentimes when new date records are added you will insert update delete drop

1:11:10

yes up chelterdraxing you will do so the process remains very similar to a vector db also so the regular

1:11:17

management will happen regular management will happen

1:11:20

that's say kutek there can be cases where semen's updates is hr policy so then there'll be

1:11:26

there'll be some modification joe chunks already he will modify

1:11:30

update or then they drop some clauses they drop some pages from this thing they

1:11:34

remove some information from their hr policies those time we will to delete so that regular

1:11:40

management will happen just like a relational database a normal tabula database right what we call it rdbms is what we

1:11:45

call it but we call it but

1:11:47

but yes i mean generally it's a one-time process okay hope that answers for you so take the

1:11:53

documents and this is the way how the llm will generate the answer i want to i want to uh

1:12:00

you know use one more analogy here let me uh take that up for everybody

1:12:17

this is another one of my simplest where i have diagrammetically

1:12:39

kind of explained what rags are hopefully should give you a very good intuition and understanding of

1:12:46

understanding of what rags are let me share this with the audience okay okay okay just

1:13:13

give me one minute guys it didn't get saved

1:13:43

i'll take some time to explain this in detail to all of you but before that all of you

1:13:48

take two three minutes just try to give it a glance once just give it a glance and i will repeat

1:13:53

the same rack process through this diagram this is a bit more detail because you here

1:13:57

i've actually broken down the pieces more neatly for you okay you'll probably get a better perspective

1:14:02

in this diagram everybody take two minutes please

1:14:13

I don't know

1:14:43

You know

1:15:13

Thank you.

1:15:43

Thank you.

1:16:13

Thank you.

1:16:43

Thank you.

1:17:13

Thank you.

1:17:43

Thank you.

1:18:13

Thank you.

1:18:43

Thank you.

1:19:13

Thank you.

1:19:43

Thank you

1:20:13

Okay, now, it is in action.

1:20:18

It is in action.

1:20:33

So let us see this in action, guys.

1:20:41

Just give me a second.

1:20:43

Thank you.

1:21:13

Thank you.

1:21:43

All right.

1:21:50

So what I will do.

1:21:52

So what I will do.

1:21:57

So let's consider the PDF that I'm going to let's consider the same use case of the 100 page PDF that I was discussing.

1:22:11

Let's let's just say this is the PDF which is spanning

1:22:13

overall 100 pages guys. This is that HR manual that we were talking about from a particular

1:22:20

company which is extremely confidential and naturally it is a huge amount of data so we will do some chunking.

1:22:26

And the policy that we are using right now is we are saying one chunk per page.

1:22:35

There are a lot of other ways to do chunking and chunking will be a separate topic.

1:22:38

We will actually get into chunking in detail in the next to next session.

1:22:42

We will see that in detail.

1:22:43

So we will create one chunk per page and the end result will be we will end up having 100 chunks, C1, C2, and it will go all the way up to C 100.

1:22:52

We will end up having 100 chunks.

1:22:54

But remember, these chunks are also chunks of text.

1:22:57

Whatever chunks you are able to see right now, they are also chunks of text.

1:23:00

So we will take each and every one of those chunks.

1:23:02

We will pass it through an embedding model.

1:23:08

We will pass all these chunks through an embedding model.

1:23:11

and they will eventually be stored in a vector database.

1:23:15

C1, C2, C3, all the way up to C100, all these chunks will eventually be stored in a vector database.

1:23:22

C1, C2, C3 up to C100.

1:23:25

And you will be having what we refer to as chunk embeddings.

1:23:28

Right, so as an example, let's say C1, the embeddings will be something like 0.1.2.

1:23:34

I'm just giving some very ballpark numbers right now.

1:23:37

Imagine C2's .1.1.2.

1:23:41

that is C2, and the same way we are looking at C100, which is going to be, let's say, 0.8.9.

1:23:48

So these are the respective chunks that you are able to see on the screen, okay?

1:23:52

So we have the 100 page PDF, we have done the chunking, we have got 100 chunks,

1:23:58

and now we are taking each and every one of those respective chunks.

1:24:02

We are using an embedding model, and this is what we are getting.

1:24:05

So every chunk, we are able to get each chunk embeddings.

1:24:09

C1, we are able to see its embedding.

1:24:11

C2, what are the embeddings, all the way up to dot C00 C00, what are the embeddings?

1:24:14

We are able to see that.

1:24:16

Now, when the user asks the question, the question the user is asking is, let's say as an, this is

1:24:21

the first part.

1:24:22

This is the usually got the first part.

1:24:23

And this is like your library.

1:24:24

I was giving the analogy of the library, ELAQa library here, the vector database.

1:24:28

It's just like any other kind of database, right?

1:24:30

And vector database is very, very good for storing unstructured forms of data.

1:24:34

Data that you cannot represent in rows and columns, tab tables, unstructured, like this is text.

1:24:38

Similarly, you can store pictures also.

1:24:40

Now, images be stored can also store pictures as embeddings, right?

1:24:45

Now, question would be, imagine I'm asking a general question.

1:24:53

How many leaves we get in a year?

1:25:04

So given this question, what you do is you end up?

1:25:08

And you end up getting what we refer to?

1:25:10

as query embeddings, right? Because remember, machines will not understand text. So if you're

1:25:14

looking at any kind of text data, the machine will convert that into what is referred to as query

1:25:18

embedding. You have a query embedding. The machine will convert that into query embedding and

1:25:26

it will send it to the retriever and the retriever will go back to the vector DB and retrieve the

1:25:31

top two, you know, similar chunks. Top two similar chunks.

1:25:36

Now, talk to is just an example I'm taking right now.

1:25:42

And the chunks it will retrieve, let's say, are C1 and C2.

1:25:45

It will retrieve C1 and C2. It will retrieve these two chunks.

1:25:48

Okay? So I repeat, coming to the retrieval part of the workflow, you ask a question, how many leaves

1:25:54

we get in a year? It will convert that query into the corresponding query embedding. And now,

1:26:01

the library will have to go and retrieve the information. It will go to the vector database,

1:26:05

where all the other chunks are there, it will go to the vector database and you are asking

1:26:09

the question, please tell me, you are asking the question that which are the top two similar

1:26:15

chunks? Which are the top two similar chunks? So you will retrieve those top two similar chunks,

1:26:21

C1, C2, Upka, top two similar chunks. You will retrieve those top two similar chunks. And this becomes

1:26:27

the retrieved context. And you can see right now, let's say the query embedding, let's say, is, I'm just

1:26:32

giving an example. Imagine the query embedding is coming as point.

1:26:35

1.2 and point to 2. You have your query embedding. This is the, these numbers somehow

1:26:43

represent the meaning of the question. Similarly, these numbers somehow represent the meaning of

1:26:47

this text. That's what embeddings are, right? So you can clearly see these numbers are similar to C1

1:26:51

and C2. Similar, distance formula here. There are other other mathematical ways to do this which we'll see

1:26:56

later, but it is going to be like a distance formula. So you retrieve C1 and C2 and this is what is called

1:27:01

the retrieved context. This is it called the retrieved context. We call it a retrieved context.

1:27:05

And now this is coming to the final LLM. So whatever we have seen so far, the story so far has

1:27:12

been what? The story so far has been you have a large language model, right? You ask a question,

1:27:18

you ask a query. Yeah, your system message hoag and you get a response. That has been the story so

1:27:24

far. We have done all our applications until now like this. We define a system message. Query is the user

1:27:30

message and you combine the two and you get a response. There'll be system obviously, right?

1:27:34

This is what we have talked about.

1:27:35

so far. Now what we are doing is not now you cannot directly ask that question to the LLM because

1:27:41

the LLM doesn't know. It doesn't have that context. Neipata what, what is in the HR thing. So now

1:27:46

what will happen is based on the question, we do all of this stuff to retrieve the context. So in addition

1:27:54

to the query, you will also have the retrieved context. You will also have the retrieved context.

1:28:05

and based on that, it will generate the response. So user asks the question, we are able to retrieve

1:28:15

the relevant context. Whatever context is there, we are able to retrieve the relevant context.

1:28:21

And this combination of query and context together is called the user message.

1:28:27

This your user message. So system message plus user message, we are able to get the assistant response.

1:28:33

That's what we are able to see. So system message plus.

1:28:35

the user message is nothing but the query plus the context and you get the response.

1:28:39

And hence the term retrieval augmented generation. It's not a normal generation. First you retrieve,

1:28:44

then you augment and then you generate. Right. I hope everybody is clear. And as I told you,

1:28:48

this is particularly useful for sensitive enterprise data. Sensitive enterprise data, because this

1:28:55

entire thing that you are seeing here, this will typically happen on premise inside the company servers.

1:29:02

Because this is very sensitive data. The vector DB will usually be hosted.

1:29:05

in the company servers. This will not go public.

1:29:08

Okay? So that is the way how we are able to ensure privacy and security in this particular context.

1:29:15

This is just one more analogy that I wanted to share with all of you.

1:29:21

So I hope with this example, you will get a very good perspective of what rags are, right? Both

1:29:27

the diagrams should give you a very good perspective of what rags, you know, what rags are and what they

1:29:31

are doing behind the scenes. And now we will be getting a very good perspective of what rags. And now we will be getting

1:29:35

into some of the other nuances, right? There are some other nuances that we have,

1:29:38

which we'll talk about. And we will see what they are. Okay. So we can take a break and

1:29:43

come back. Let us take a short break and come back. And after the break, we will discuss a few

1:29:48

other general concepts. And I will show you a very non-technical demo of what this is. Okay,

1:29:53

we'll see a very small non-technical demo of a rag system. So that is what we'll, what is the plan

1:29:59

after the break. Okay. So let's take a break and I'll see all of you back after the break.

1:30:05

Thank you.

1:30:35

Thank you.

1:31:05

Thank you.

1:31:35

Thank you.

1:32:05

Thank you.

1:32:35

Thank you.

1:33:05

Thank you.

1:33:35

Thank you

1:34:05

Thank you

1:34:35

Thank you

1:35:05

Thank you

1:35:35

Thank you

1:36:05

Thank you

1:36:35

Thank you

1:37:05

Thank you

1:37:35

Thank you

1:38:05

Thank you

1:41:35

Hi,

1:41:38

We will back, we'll back, we will come back.

1:41:49

we will continue we will continue on we will continue on.

1:41:51

So we will continue on.

1:41:52

So we went.

1:42:05

understood what what is the meaning of retrieval augmented generation, the rag pipeline.

1:42:11

So first we load the data, then we chunk it, we embedded and based on that we are going ahead and retrieving the information and generating the answers.

1:42:21

And that is what is referred to as retrieval augmented generation.

1:42:24

So we first looked at the problem and then we understood why rags are important and then we actually went through the process of the rack pipeline.

1:42:32

Actually, you will see each one of these things in a lot of detail.

1:42:34

of detail, lot of detail, as I told you know, the sessions that we have here,

1:42:40

each of the sessions will take you through the specifics, like if I have to just tell you at a very high level.

1:42:46

So we will see the very next session that will focus only on embeddings and vector search.

1:42:51

So today is just basic foundation, right?

1:42:53

next class will be only embeddings and vector search.

1:42:55

We will see what is embedding, what is vector search.

1:42:57

So we'll talk about that vector DB part in detail.

1:43:00

Next class will be getting into chunking and document preparation.

1:43:03

preparation like if you're asking if you're thinking that okay sir i will take the PDF and i will

1:43:08

generate chunks how it is happening so there's a separate class only for that and then we will see the

1:43:12

final retrieval and grounded generation the part where i'm saying that you ask a question and the

1:43:18

retriever will retrieve the top to relevant chunks and generate the answer so there's a separate

1:43:22

class only for that and then we will see the entire end to end rag use case actually in the very last

1:43:27

module like integrating rag so actually there are four more classes for rack so we are here right now

1:43:33

Now, with this in mind, let us go ahead and just to give an idea to you.

1:43:38

I've actually, you know, although we will see this in the next class, but just wanted to give an idea to you, what embeddings really are.

1:43:44

When we talk about embeddings, what they really are, because all this file, we are saying that, okay, you know, we take the document and we divide that into smaller chunks and we create chunk embeddings because machines don't understand text.

1:43:57

So what really are these embeddings? Just wanted to show you a small demonstration of that.

1:44:01

just a small demonstration of that.

1:44:04

So we are installing a package called sentence transformers and these are the kind of models that

1:44:09

we will use to generate the embeddings. Embedings are nothing but they are giving you the contextual

1:44:14

information of the thing. They are basically giving you the contextual information.

1:44:21

So embeddings are basically giving you the contextual information of that text. If it is a chunk,

1:44:26

what is the meaning of that chunk? If it is a query, what is the meaning of that query? It is giving you to some extent

1:44:30

the contextual information. So we will first pip install the sentence transformers library.

1:44:35

That's the first thing we are doing. Next, from sentence transformers import sentence transformer.

1:44:40

We are importing this particular module right now. And then we are instantiating sentence transformer.

1:44:46

This is the model that we are loading right now. And this is a very, very fast and widely used

1:44:52

for baseline semantic search. Okay, it is used for semantic search is a kind of similarity-based search,

1:44:58

right? That means you are searching based on the minimum.

1:45:00

of the document. That is what we have been doing in the RAG system all this file.

1:45:04

So the technical name that we use for it, we call it semantic search. That means, you are

1:45:10

semantic means the meaning. Semantic means meaning in a way. In English, semantic means meaning. So,

1:45:17

you are looking at the chunks, chunks of text and the embeddings are somehow telling you,

1:45:26

giving you the semantic meaning of that particular chunk.

1:45:30

So, next time I ask you a question, you are retrieving the similar chunks,

1:45:35

similar chunks based on the semantics, based on the embeddings. That is why it is called a semantic

1:45:39

search. Because that is how we are looking up. We are looking up based on the embeddings. We are not

1:45:43

looking up based on keywords. It is not as if we are seeing the question here. These are the keywords

1:45:47

that are there. So let me go to my library and see which of the. No, it is not a keyword-based

1:45:52

search. So based on the query, you go to the vector database and you look up what are the

1:45:58

similar chunks based on the semantics.

1:46:00

In fact, we are learning about VectorDB today, Google has been doing this for a long time.

1:46:06

Next time when you go to Google and in the search bar, when you type a query, Google has been known

1:46:11

to use a hybrid method for a long time.

1:46:13

Historically, if you go back decades, Google was traditionally using keyword-based search.

1:46:19

That is whatever you are typing on the Google search, whatever keywords are there, it will return

1:46:24

the respective URLs to you and the links to you which contain most of those keywords.

1:46:28

It was doing a keyword-based search majorly.

1:46:30

But later on, in the past few years, Google has been extensively using this kind of semantic search.

1:46:37

So now when you ask a question, it is not just doing a keyword-based search, but it is also giving

1:46:42

you links to other webpages based on the semantics, based on the actual nature of the content.

1:46:48

And the magic of that is all embeddings.

1:46:50

Google be made.

1:46:52

Every web page is like a chunk.

1:46:54

Every website index is like a chunk.

1:46:56

And what is Google doing?

1:46:57

It is looking at the initial HTML of the page, the initial content of the page.

1:47:00

and it is generating web page 1, embeddings of web page 2, embeddings for web page 3.

1:47:07

So next time you ask a question, it is also doing something like a semantic search.

1:47:11

It's actually a hybrid.

1:47:12

It is doing a lot more than that, but this is also a very big part of what they are doing.

1:47:17

Anyways, now let's see what these embeddings really are.

1:47:20

What are these embeddings?

1:47:21

Let us see a very basic demo of that.

1:47:23

So first time loading the sentence transformer model.

1:47:26

These are the three sentences.

1:47:27

We have the quick brown fogs jumps over the lazy dog, fast, dark colored form.

1:47:30

sleeps over a resting dog and python is a great programming language for AI in sentences

1:47:35

right and what we are doing we are saying model dot encode sentences that's it so we will do model

1:47:43

dot encode sentences and we will generate the three embeddings so for these three sentences we will

1:47:49

generate the three embeddings right now and i will simply print out the embeddings for you let us see

1:47:54

it will takes a while for the embeddings to get created but this is very small amount of text it will be quick

1:47:58

so first it will load the model we will first download the model locally locally means in our

1:48:03

system we will download the model we are doing that already we are downloading the mini lm

1:48:08

l6 v2 model and then we will take this uh you know these respective uh text and we are trying to convert

1:48:17

them into their respective embeddings so printing print print the sentence i will also print the

1:48:22

embedding shape that means uh how many numbers are created for every text and also finally i will

1:48:27

print the embedding the first five values because there'll be many numbers see how i'm downloading

1:48:33

this one it's a very small model i've got three sentences right now and for every sentence you can

1:48:37

see the mini lm l6 we do what it does is it takes every single text and it converts it into a

1:48:47

vector of 384 numbers that is what is doing behind the scenes now remember friends these numbers are

1:48:55

like we we humans we don't understand what these numbers are these numbers do not mean

1:49:01

anything to us we humans we do not understand what these numbers are but the machine is taking these

1:49:08

this particular text chunk and it is converting this text chunk into a sequence of 384 numbers

1:49:14

embeddings as we got it that is what it is doing behind the scenes it is taking that and it is

1:49:19

converting that into as i said a vector of 384 numbers

1:49:25

that's the big picture idea that's that's what is doing behind the scenes

1:49:29

and you can actually take a look at the first five values yeah your paella five numbers

1:49:34

you can also see the all three so these numbers as i say they make no sense to us

1:49:39

as humans they do not make any sense they do not have any say make any sense to us but for a machine

1:49:44

these numbers are very important because for a machine these numbers are demonstrating

1:49:49

for a machine these numbers are in a way demonstrating that okay they're giving you the meaning

1:49:53

of that sentence in a way

1:49:55

and that's the big picture idea so vector db in this

1:49:58

number stored here if you want to see the entire number i can just remove the this this five

1:50:03

here you can actually print out the entire embeddings right

1:50:06

you'll actually generate the entire set of numbers but obviously it's hard to see what

1:50:11

what what this means you know you can see so this is the entire text right now the quick

1:50:17

brown fox and these are the 384 numbers now look all 384 numbers that represent

1:50:22

that sentence these are all 384 numbers that

1:50:25

represent that sentence this is basically what embeddings are or this

1:50:28

pooha chees your vector tvs are stored on depending on the kind of embedding model you are

1:50:31

using right now i'm using the embedding model which is uh uh you know uh all mini lm l6 v2

1:50:37

there are other kinds of embedding models you can also use and you can google out

1:50:40

you can print go to that library and you can search

1:50:46

okay we can go back to that library and we can search what are the other kinds of

1:50:49

embedding models that are there the one that we are using is this thing sentence transformers

1:50:54

this thing but you can use a lot of other sentence transformers models also just click on it

1:50:58

click on this one and you will see a whole lot of other sentence transformer models these are a

1:51:03

whole lot of other sentence transformer models that you will see spaces models 127 such

1:51:08

options you have and you can choose any of them there's a jama model jama model jama is by google

1:51:14

there are bigger models out there there are specific embedding models for different domains

1:51:17

you can search different different models and you can try so these this is how you will take those

1:51:22

chunks and you will convert them into a vector of numbers which somehow tell you the

1:51:26

meaning of that text okay that is what is going on behind the scenes this is what embeddings

1:51:31

really are i have shared this code in the first july folder it's a very short demo for today

1:51:37

i just wanted to show you what embeddings are at a high level anyways embeddings will be a part of

1:51:41

the the next session also when we see uh you know each of the modules in a lot of detail

1:51:46

deal okay i hope everybody is clear what does its unit mean what do you mean what do you mean

1:51:54

good thing i i didn't understand your question what do you mean in the code carpe um

1:52:03

where where did you see it's please tell me i'm i'm here for you please tell me i'm i'm here for you please

1:52:16

excuse me loading weights where oh iterations per second

1:52:26

that means iterations per second each per second means iterations per second each per second

1:52:32

basically stands for uh you know iterations per second that is that is what is going on behind

1:52:37

the scenes okay huh it means it means iterations per se it just it's just a progress bar for

1:52:46

for speed you can think of it like how many loading steps the model completes each second

1:52:51

yeah because this is a model right you joe all mini lm l6 v2a it's a model you're loading that model

1:52:57

so while loading the model this many iterations you're completing per second just just just the progress

1:53:01

bar here okay yeah okay great let's move on and uh and finally the last part what i wanted to talk

1:53:11

just mention is that the aspect of grounding very important grounding grounding

1:53:16

means it is very important in a rag system that your answers are grounded in the context

1:53:22

your answers must be grounded in the context this is again the big picture idea retriever will

1:53:27

retrieve the relevant information same story we have talked about it multiple times already right

1:53:33

so you're asked a question go to the knowledge base get the information and the generator will go

1:53:38

and use that to generate the answer it is very important this is a very important line use only the use

1:53:46

only the retrieved notes to generate the answer very important if it is not there in the

1:53:53

notes don't make it up and say i don't know and this is called the grounding rule so when we build

1:54:00

rag systems down the line this will be a very important criteria

1:54:04

but if you're asked a question let's say if you're building a rag system for your uh

1:54:08

company's hr documents okay if you are asked questions specific to the hr domain you'll be able to answer

1:54:14

you will answer it accurately you should answer it accurately okay if you're asked

1:54:20

questions specific to the hr domain you should be able to answer accurately right but let's say if you're

1:54:24

asked asked a question on a slightly on a different domain a love domain if you're asked a question

1:54:29

then that's a problem okay so this is again something that you will have to keep in mind

1:54:34

if you're asked a question about the hr domain you should be able to generate the answer but if you're

1:54:39

if you're asked a question on a on a slightly different domain then you know that becomes a

1:54:44

problem so these are again some of the things that you will have to keep in mind okay so that's

1:54:50

the that's the basic context of what uh what rags bring to the

1:54:56

grounding the grounding root grounded rule must be grounded in the context okay

1:55:02

so whatever answer the language model is going to give the generator llm is going to give out

1:55:08

that answer must be from the context

1:55:09

it should not be outside the context only what you have retrieved from the library only that answer

1:55:15

you can give up nothing other than that let's see if you have a rag system and if you ask it

1:55:21

you know what is the weather they know because it is not there in the context and uh

1:55:27

good thing not necessarily are rags lLMs hosted locally not necessarily this

1:55:31

the one that i shared with you on chat that diagram if you remember excuse me the lLM layer

1:55:38

it is not necessary that the lLM has to be hosted on chat no not necessary

1:55:43

lLM can be cloud hosted also it has to be it can be local also in fact the vector db is usually

1:55:49

on premise that is always hosted locally the vector database because that is very

1:55:52

sensitive but the final processing can happen anywhere because imagine if you're using a gpt or a

1:55:57

paid model if you're using one of the close source models paid models then you have to keep

1:56:03

it on the cloud it has to be an API call right so that is uh one kind of arc

1:56:08

the other kind of architecture is yes i mean if security is absolutely paramount then you can host

1:56:14

it locally then you have to use open source allems okay yes that is that is a very good point

1:56:23

good thing good thing you're saying that okay uh sir what if the lLMs are taking a context as input

1:56:27

then we are sending some data outside but good tech let me tell you that is a very very very very very

1:56:31

small portion of your entire document base remember we are not attaching the entire document as context

1:56:37

it is a bit of a trade off and at the end of the day just like everything else it is a it is a

1:56:42

decision that we have to measure and take so your document your vector tb consists of everything

1:56:49

that is like your vault what vault say you're you're retrieving only a very few one or two chunks

1:56:55

and then you're sending it to the relm it's a very small minuscule fraction of your data

1:56:59

and sometimes companies are okay to take that hit it's a very minuscule faction but even there

1:57:04

i would say good think there are a lot of things we can do we can do mass

1:57:07

we can do redaction we can try to hide the personal details any sensitive information we can

1:57:12

mask those kinds of things can be done even before those chunks are sent across to the

1:57:17

lLM so yeah so those are two things i can tell you one is it's a very small amount of data

1:57:24

that you're sending out and second is obviously you can do some masking and if at all you're

1:57:30

absolutely concerned about security then you always have the option of open source models right

1:57:35

you can host it locally that anyways is there

1:57:37

but just like everything else is the you know it is like a trade-off as always it's a trade-off

1:57:43

like in terms of cost as well we were talking about this the other day open source models are nice to

1:57:48

talk about but then they are very costly because you have to procure your own hardware you have to

1:57:53

you know host these models locally it's very costly sometimes when you're starting out a

1:57:57

project shuru-sudu-sudu-s actually a lot cheaper to do API calls because you you know you the initial

1:58:03

cost the upfront costs are very high okay that's one way to look at it

1:58:07

see the analogy is almost like let's say today you want to start a company

1:58:12

if you're a company caridna what will you do will you go and uh buy hundred acres of land

1:58:18

where go where you get the money right i'm just giving an analogy so if you're starting a company

1:58:25

maybe it's a lot cheaper for you to rent a co-working space you will not own anything you will not

1:58:29

buy anything but you will only pay as you go you will maybe uh hire a co-working space rent a co-working space

1:58:36

rent a co-working space.

1:58:38

$15,000 rupee in a month.

1:58:40

Just have a bench, have a workstation.

1:58:42

You get a place to sit, you get a place to work.

1:58:45

So you have the infrastructure and you pay as you go.

1:58:49

That's the thing.

1:58:50

That's basically the cost-benefit analysis.

1:58:52

Okay.

1:58:53

Yeah.

1:58:57

Okay.

1:58:58

We will see a very small.

1:59:01

Excuse me.

1:59:04

A very small.

1:59:05

A very small.

1:59:06

demo right now and this is pretty much what I was you know what I wanted to show you a very small basic demo.

1:59:17

Eventually what we will do is as we get through the classes we will see the same demo using you

1:59:25

know using the code we will see that but for now I will use chat GPT to show you a very small

1:59:32

end to and drag demo and just to show you because you know the surprising thing is

1:59:36

that even chat gpt is using rags many of us we don't realize it but even chat gpt

1:59:40

internally is using using rags and hopefully through this demo you'll be able to see the thing in

1:59:46

action without any code but you will be able to relate to it some of the things that it is doing

1:59:51

behind the scenes okay let us see that so what i will do first of all i'll take my data right and i will take

1:59:58

a data set which eventually we will discuss later on we'll be taking this up in more detail in the

2:0:06

to next session even next session will be elementary rack topics i will cover we will

2:0:11

be covering as part of the module and then only the next session you will see a full-fledged comprehensive

2:0:15

demo but anyways let me go and show you the data set what kind of data set we are dealing with

2:0:24

right now so we have a Tesla financial report this is from the year ending 2023 December

2:0:33

Tesla financial report annual financial report is what we what we have right now

2:0:38

and this is the 130 page document imagine this kind of thing can be very useful for investors

2:0:44

investors or investment bankers people who are into trading they would like to know details about

2:0:52

the company how is the company doing and all that this is what happens in stock markets right you

2:0:56

invest money on companies then based on the company's financials and fundamentals they go up they go down

2:1:02

people buy sales shares all that so these could be this could be a very good rag use case

2:1:07

where i'm just sharing with you one um financial document but there could be several

2:1:13

tens of thousands of financial documents tesla might be having and you can literally uh

2:1:20

take this financial document and people can ask questions of this document and get answers that becomes

2:1:25

a rag use case right so what i will do i'll go to chat gpt and just to simulate the demo i will quickly

2:1:31

upload this particular document here let me upload the document here okay now uh

2:1:38

first i will run the query then i'll explain to you what is happening at a high level

2:1:42

let me run the query first then i'll explain to you what is going on at a high level so that you can

2:1:46

relate to that end to end a very low code no code end to end in terms of what is going on behind the

2:1:52

scenes let's see that and i will ask the question what is the annual revenue

2:2:01

what is the annual revenue excuse me in the year 2022 uh so very interesting if you see

2:2:12

what what is going on behind the scenes i'm going to i'm going to i'm going to uh

2:2:18

talk about this in a minute for a minute uh if chat gpt was processing your entire pdf file

2:2:25

think about it for a minute okay this is the free platform completely free chat gpt allows you to use it for

2:2:30

free if users were able to upload a massive PDF like what i have right now and if it was

2:2:36

taking that entire PDF as input then imagine the number of tokens that it has huge right

2:2:42

have you thought about it how is the language model because chat gpt internally is making an

2:2:47

API call i already told you that whatever you type here this is your user input whatever you type

2:2:54

and attach here is like your user input this user input is getting combined with chat gpt is hidden system

2:2:59

message and based on that it is giving the response the API call is happening behind

2:3:04

the scenes it is calling gpt models right now imagine the amount of token usage that will happen

2:3:10

massive so they are also doing a rag but they are doing something like an in-memory rag

2:3:16

that means what chat gpt is doing is the moment you upload a PDF they are internally creating a

2:3:22

kind of a vector db in that session in memory whatever i was talking about that vector db conceptually to all of

2:3:29

a while back this same vector db is getting created in memory in a more real world use case like

2:3:36

what we will see in our demos going forward we will create this physically in a database we will

2:3:42

it physically and stored in a file it will be persisted it will be saved but in the case of chat gpt

2:3:48

is not saved permanently you as a user you will not be able to see it but they are doing this in the

2:3:53

session in the current chat session so if you ask this question what will it do it will take the

2:3:59

pdf it will create chunks it will convert those chunks into embeddings it is creating a

2:4:04

vector dv in memory in the ramp of this thread and next time you ask this question it is going to that

2:4:10

vector db real time it is looking at the similar chunks and giving the answer it's a lot more

2:4:14

efficient way of doing things that's why when i click on send the prompt you will see

2:4:18

chat gpt will actually read from the document that means it is creating the chunks is going and doing the

2:4:22

retrieval right now it has retrieved the relevant chunks and it is giving you the answer based on that

2:4:28

so this is the way they are able to

2:4:29

to efficiently kind of do a in-memory rag this is the contextual understanding and you can

2:4:38

also see they have quoted the source from which source they have got the answer so this is to further

2:4:42

demonstrate they are doing a rag you can have multiple sources you can have five 10 different

2:4:45

sources so oftentimes it happens right you can upload five six pdfs and you can ask a question

2:4:52

and the answer to the question might come from only certain chunks right which are in certain

2:4:57

pdfs and and they will cite that PDF also chat gpt will also cite it that okay which

2:5:01

pdf i got the answer from even in a real rag system when we build it later on in our sessions when we do

2:5:07

it we will see the same thing there'll be citations we will actually cite the actual source where it is coming

2:5:11

from so this is just to give you a very nice miniature big picture demo in terms of what is going on

2:5:17

inside a rag so when we build our rags we will do exactly the same thing we will take a PDF we will create

2:5:22

a vector tv manually and then on the basis of that we will ask a question based on

2:5:27

that chunks will be retrieved and we will get the final answer like what we are seeing right now

2:5:32

and is it the right answer yes it is 81 000 462 you can validate it so 81 000

2:5:37

462 million chunks yes it is the correct answer it has given the correct answer right now

2:5:45

we will see this exact same demo in python later okay 2022 you can see next again 81 000

2:5:51

462 and the interesting part is the answer to that question when you ask the question

2:5:57

what is the annual revenue in the year 2022 very interesting the answer to that question is present

2:6:02

in so many different portions of the document is present here is present here is present here is present

2:6:05

here is present in all these four places so next time when i ask a particular question

2:6:11

and when i try to retrieve the chunks actually four chunks will be retreat all the four chunks

2:6:17

will be retrieved here because the answer to that question is somehow present in all these four sections

2:6:21

of the document and then we will be getting the you know the fine-tuned response from all these

2:6:26

chunks okay so this is just to give you a very miniature example and you can extend this in

2:6:31

any other platform like many of you in companies you're using co-pilot you're using uh

2:6:35

you're using uh other kinds of assistants and where they are all using rags in some way

2:6:41

whenever you upload anything and whenever you upload a document or anything when you

2:6:45

upload you are basically in a way that application behind the scenes is doing a rag

2:6:51

and today's discussion will give you some intuition and some and it will maybe broaden your

2:6:56

next time you're using chat gpd it will broaden your view and you will relate to it but remember i'm

2:7:00

repeating again it's not a it is not a physical you know use case it's not a physical database

2:7:06

that is created it's only a in-memory db yes uh-huh so uh what is that while researching

2:7:19

and you know very interesting talking about a legal domain there is actually a company called harvey

2:7:24

so you can actually read about a specific company called harvey harvey is also doing uh

2:7:28

exactly what you said okay harvey is actually a company that is that is specifically in this

2:7:34

particular domain they're doing exactly something that you said in the legal domain

2:7:38

there so so that is just one other thing i wanted to generally share but yes i think just to

2:7:43

read utkirk's question while researching case laws for any sort of legal problems gpt

2:7:48

often generates false cases or citations huh so uh utkars yeah good question because gpd

2:7:53

because gpt is a next token predictor not a legal database so without grounded retrieval

2:7:59

it can generate citations that look plausible but they don't actually exist so that is the thing

2:8:07

that is the thing because it is not explicitly trained on legal data right when the language

2:8:11

models were trained whatever public cases it could find it will be trained on basic public

2:8:15

data but otherwise specific citations and specific grounding it doesn't have

2:8:19

in legal work exact name sections citations matter so this is a classic use case of a rag

2:8:25

you need to do this over trusted case law sources and yeah that is you need to have a build

2:8:31

a very robust database of that and then do it but a normal llm and a gpt will not be very good in

2:8:38

giving you these kinds of things they will hallucinate because language models find it very

2:8:44

embarrassing to say i don't know you know it's like it's like a normal behavior no like if you're asked a

2:8:48

question usually people will say i people will never say i don't know they will still try to

2:8:51

answer lLMs are no different if you ask a question lLMs will usually never say i don't know

2:8:56

they will still try to answer they'll try to make up an answer but they will still answer

2:8:59

and that is exactly what you are saying it's how it's called hallucination

2:9:04

and and and this is the classic use case of rags once again rags can be used to reduce

2:9:08

hallucination huh huh the prompt will work to some extent not beyond the point of

2:9:18

it will work to some extent not beyond the point beyond the point if you ask for some specific

2:9:23

case detail that day on the day on what exactly happened why did the judge pronounce this

2:9:27

then you need access to judgment data got it you need exact access to case files to answer that question

2:9:34

that is what i meant and actually legal domain is an excellent use case for this generative way especially

2:9:42

in our country where you know we have so much of text data and all legal is a very good use case i would say

2:9:48

okay guys so uh that's pretty much all for today and just to summarize the conversation for

2:9:55

today today was the introductory rag session as i told you we have multiple sessions planned after

2:10:01

this so we looked at rags we understood what rags are we took a lot of time to

2:10:05

conceptually understand rags why we need rags we understood the entire retrieve generate

2:10:11

augment pipeline we understood what chunking and embedding are we in fact looked at all the components

2:10:18

at a very high level and finally like we looked at a very basic minimal rag demo a very low

2:10:23

code no code demo we saw just to show you an understanding of a rag and this exact tesla demo

2:10:28

what i will do we will see in a later time okay in actual code we will repeat that so just to

2:10:36

summarize this for all of you what we covered in the session any questions anybody has anything

2:10:40

that you want to know the embeddings file i've already uploaded in today's first july folder

2:10:45

you can do some small demos from there okay apart from that uh anybody wants to ask any questions

2:10:56

all clear guys okay okay okay great thank you guys thank you guys thank you everybody

2:11:10

once again uh yeah have a good day have a good night all of you and i will see you

2:11:15

all of you in the yeah in the next session thank you everybody and good night to all of

2:11:22

you uh in over to Pratap yeah thank you yeah thank you yeah am i audible

2:11:34

yes yes you audible Pratam yes okay okay okay okay yeah thank you so much sir for another amazing

2:11:40

lecture and okay okay so students i will release uh

2:11:45

the feedback poll now please fill the feedback poll make sure you fill the feedback poll

2:11:54

and once you're done with the feedback poll then and only then i will release the then i then i will

2:12:00

start the mintimeter course so students please make sure you fill the feedback poll

2:12:15

fill the second question as well how did you find today's lecture experience

2:12:19

the long answer i've noticed that many don't fill that

2:12:24

the website

2:12:25

um it will all

2:12:27

me that it is not

2:12:42

Okay, I am starting to share the screen.

2:13:12

All right, I am ending the poll now and we'll start with the metameter quiz momentarily.

2:13:29

So there are 16, I'm sorry, 15 attendees now, I'm hoping at least 10, I'm hoping at least 10 people join in the Mettometer quiz.

2:13:40

Okay, the poll is ended.

2:13:47

Guys, please join the Menti-meter quiz quickly.

2:13:54

I'll wait for one more minute.

2:14:03

Requesting students in attendance to join the Menti-meter quiz.

2:14:10

Can we get two more players? Okay, 30 seconds more?

2:14:40

All right. Fine. I'm starting the quiz now.

2:14:48

And so only eight people.

2:14:52

Alright. Here we go. Okay, nine. Great.

2:14:57

What is a knowledge cutoff limit?

2:15:03

So when you, when a LLM has a knowledge cutoff limit.

2:15:09

off. What is it limit?

2:15:11

CINLM has a knowledge cut off of October 2013 or 2015, whatever.

2:15:22

What is the thing that gets limited?

2:15:25

I think everyone will get this one, correct?

2:15:31

Oh, okay. Surprisingly, a lot of people didn't get this.

2:15:37

Okay.

2:15:38

Okay, so I'm actually surprised more people didn't get this than the ones who got.

2:15:45

So when a knowledge cutoff limit is there, it prevents or it limits the LLM's access to latest or private facts.

2:15:53

It is not searchable text pieces because there is no rag that we're including in this.

2:15:59

This is just a noise cutoff limit refers to purely LLM, it's an LLM parameter.

2:16:06

Purely LLM, it's not related to.

2:16:08

not related to RAG in any way. So there is no searchable text pieces in the first place.

2:16:12

And vector sizes, like, that's just a nonsense option. So I'm not sure why people have selected that, but okay.

2:16:20

See, I told you last time, the question this time will be a little tougher.

2:16:24

All right. I think last time the questions were a little too easy. So this time I've

2:16:34

made them slightly tougher, but I didn't expect.

2:16:38

so many of you to just guess and answer.

2:16:42

I think a lot of people are just guessing.

2:16:46

So made it difficult to guess actually.

2:16:51

Okay. What does an embedding represent?

2:16:54

An embedding. What does it represent?

2:16:58

Again, this one is definitely easy.

2:17:03

This one is definitely easy.

2:17:07

This one is definitely.

2:17:08

easy if you have paid attention in class.

2:17:12

Yeah, text, text meaning is number.

2:17:34

Yeah, text meaning is numbers great. So everyone got that correct at least.

2:17:37

All right.

2:17:47

All right.

2:17:49

Next question.

2:17:52

Oops.

2:17:58

Okay.

2:18:01

What is sent to the LLM after the retrieval step is done?

2:18:06

So if you remember in RAG there are three steps.

2:18:11

Retrieval, augmentation and then generation.

2:18:14

The generation is by the LLM, last step.

2:18:18

So, and augmentation is what the system does, basically.

2:18:24

So what goes to the LLM after data is retrieved?

2:18:30

So I have intentionally made the options difficult to guess.

2:18:35

So you have to guess.

2:18:36

think about it. Yes, the correct answer is retrieved text only. The text is the only thing that is

2:18:43

that is given to the LLM because LLMs work with context and inside context there is to be text.

2:18:50

It cannot work with vector databases or raw vector arrays or API keys and scores.

2:18:57

API keys and scores is a nonsense option in this case. So yeah.

2:19:06

Most of you got that correct, so that's great.

2:19:10

All right.

2:19:17

Last two questions.

2:19:20

What risk comes from tiny chunks?

2:19:31

So this is not something that sir has covered, but I want you guys to think about it.

2:19:35

when an LLM is getting data, retrieving data rather, if it is retrieving the data that is very, that has very tiny chunks.

2:19:47

So the data, there isn't even a complete sentence, let's think about it that way.

2:19:55

So the chunks are very small, like three, four word long.

2:20:01

What is the, what is going to happen?

2:20:04

Yes.

2:20:05

the key facts are loose surrounding context.

2:20:07

Because you need at least a complete sentence, right?

2:20:11

Or maybe not an entire complete sentence, maybe one sentence can have two, three facts.

2:20:16

But you need complete sentences at least.

2:20:19

So if you have very tiny chunks, then it becomes difficult to store all the relevant context,

2:20:27

surrounding context, right?

2:20:29

And they become too expensive to store is not really relevant to this question.

2:20:34

to this question. I mean, that's not, that's not the point why we are studying RG systems, right?

2:20:43

We don't care about if they are becoming, at least not at the moment.

2:20:49

We are not, we don't care about whether they become difficult to store or not.

2:20:53

So, all right.

2:20:55

Last question of the day.

2:21:04

Excuse me.

2:21:05

What causes a confident wrong RAG answer?

2:21:10

So you have an RAG system, but it is confidently giving you wrong answers.

2:21:16

What is the probable cause?

2:21:18

So again, the options are slightly confusing, but if you think about it logically, you'll get the correct answer.

2:21:33

All right. I think almost everyone will get this correct. Yes. Bad retrieval or weak grounding. Yes, that is the correct answer.

2:21:45

Using the closest chunk is not a reason because most likely cause of a wrong rag answer and confident wrong rag answer is that it's probably not able to access.

2:22:02

not able to access the database vectors only.

2:22:06

So that's why it is using the closest chunk is not relevant in this case.

2:22:12

All right.

2:22:15

Let's see.

2:22:20

I think, yeah, congratulations for Ender for winning this one.

2:22:29

And I will see

2:22:31

guys tomorrow for the tutorial session. Okay? Have a good night. Yeah, bye guys.