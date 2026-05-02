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

Hi,

10:36

Hi, everyone

10:40

very good

10:41

Good evening

10:42

Good evening

10:44

So,

10:46

so am I audible to all of you

11:01

to all of you?

11:02

Hi, everyone, I'm

11:06

Audible.

11:07

I think somewhere the chat is not enabled.

11:10

Could you do that?

11:12

Yeah, I think the host access is to the coordinator.

11:18

I have given the access now.

11:21

Yeah, I have given the access now.

11:23

Yeah.

11:24

Chat must be enabled now.

11:26

Yeah.

11:27

Thank you.

11:28

Panko.

11:29

I have done that.

11:30

A very good evening to all of you.

11:31

to all of you. And welcome to the class. And in this particular session, we are going to talk about the rag architecture.

11:38

So in the last class, we had a quick, not quick, actually in-depth discussion on what a rag is, right?

11:45

Introduction to Rack. And in this particular class, we are going to actually build the actual Rack system.

11:52

Okay? We will go through all the steps that we need to take in order to build a Rack system and we will see the demo.

11:59

So let's wait for maybe.

12:00

for maybe three to four minutes, we will start around six or seven, eight, six, eight, seven.

12:06

It's much better. Actually, what happened is over the weekend I was traveling. Because of that,

12:12

I had a bit of fatigue, and on Monday I was working. And because of that, I was having some mild

12:20

fever and a bit of headache. That's why I was not able to take the class. Okay, now it's much better.

12:26

Thank you so much for asking everyone. So let's wait for two, three minutes, and then we'll get it.

12:30

get started. Okay? We'll start around 8687. Yeah, it's very hot outside. Please take care of that.

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

Hi, so, so welcome back, so welcome back and let's get started, uh, with the topic for today, uh, with the topic for today's class, right?

15:51

In the last class, right? So the last class, if you remember, we discussed about. So the last class was all about introduction to

16:00

correct everyone? All of you remember that? Introduction to RAG. What all the things

16:06

did we discussed in this particular class? Let's walk, let's walk through that. So in introduction to

16:12

rag everyone, first of all, we discussed the problem of hallucination. Remember that? We discussed the

16:19

problem of hallucination because obviously every LLM model or every large language model has some cutoff

16:25

data. Okay, so they will not have the latest information. What is happening?

16:30

around the world, what is happening in the world right now. Because they have been trained

16:34

up to a particular date. If you ask any question from the LLM after that particular date and if

16:40

LLM is just giving the answer based on their knowledge, that whatever they have been trained upon,

16:46

obviously they will give the wrong answer, correct everyone? Obviously they will give the wrong

16:50

answer if they just try to give the answer based on what they already know. Yes or no?

17:00

Correct? This particular process, when LLM does not know the context, when they do

17:06

not know the answer, but still they try to generate the answer, based on whatever understanding

17:11

they have, that problem is called as hallucination. Obviously, everyone, hallucination is not

17:16

desirable. You do not want hallucinate, like your LLM to hallucinate. You don't want a hallucination

17:23

problem in your system. Now, in order to remove or in order to reduce hallucination, what can you do?

17:30

You can add external source of information, right? The external source of information can be

17:34

added in the terms of internet, can be added in terms of books, documents, PDFs, etc, etc.

17:40

Correct, everyone? So, hallucination is not desirable. We need to try. We should try to reduce

17:47

the hallucination as much as possible, right? So LLMs are very powerful, but they have limited knowledge.

17:53

They do not have all the knowledge of the world. They do have a lot of knowledge about the world,

17:58

but up to a particular date.

18:00

Whatever has happened after that date till today, they do not know about it. That problem

18:05

is called us hallucination. Limitations, everyone? Static knowledge. They do not have access to the

18:10

private policy documents of any company. Now, if you're building a customer support agent

18:14

for your company today and you decide to use some LLM model, let's say, GPT 5.4 or some Gemini

18:20

model, et cetera, they are very powerful model. They have a lot of data on which they have been

18:25

trained upon. But still, they do not have the access to your.

18:30

private policy documents of your company. If some user is asking about the refund policy,

18:35

some user is asking about some other question about your policy, about your company, they will not

18:40

be able to answer because they do not know about it. If LLM is not having sufficient data about

18:44

question, why don't it say, I don't have the answer for it? You can do that. In fact, see,

18:51

first of all, if LLM does this particular thing that, okay, we do not know that, that is also not a good

18:56

option. Either when you are saying that I do not know the answer or you try to give the wrong answer.

19:02

Both of them are not a good approach. None of them is good approach. Right, Vishuana? They can definitely

19:08

if you have encrypted, if you have encoded the LLM in such a way, if you have written the code in such a way,

19:14

they can also deny that, okay, we do not know the answer for that. Okay? But the point is that when

19:20

LLM knows, when LN do not know the answer, they really don't know that they do not know the answer.

19:26

The point is that LLM works on probability, right? LLM works on probability. Now if you're trying

19:33

to search for something for which LLM does not know about it, if you are searching something,

19:38

LLM has zero information. The point is the amount of data on which LLM has been trained upon. That

19:44

is insane. So even if you search something on which LLM, like about which LLM does not know, even if

19:51

you search about that particular thing, still you will be able to find something. Even the

19:56

probability is less. Getting the point. So there will not be anything that you cannot find

20:01

inside the LLM. Maybe it might be an older information. It might be a new information. It might

20:05

be a high probability. It might be a low probability. Makes sense, Vishana? So the point is that

20:11

even if LLM does not know about the question that you're asking, it might be able to find out something

20:17

inside the LLM, inside the brain, inside the data, maybe with a much lower probability. And then

20:23

LLM will try to use that. Make sense?

20:26

that will lead to hallucination. Because once you have that kind of data, trillions of parameters,

20:32

you will be able to find some match. The probability will be less. That is a different topic

20:36

altogether. That is a different point altogether. But still you will be able to find something. Can't

20:41

we still keep a probability cutoff? You can do that. Absolutely you can do that. But again,

20:45

if you do the cutoff, if you do the probability cutoff, if the probability is very less. Still,

20:50

if you see it might, what probability you will take, 0.1 or let's say even lesser.

20:56

But in that case, your LLM will have to deny the answer. That, okay, I do not know the answer.

21:01

That is also not a very good option to have, right? Definitely, it might be a better solution than

21:06

hallucination, but still, it is not the best one. Right? In this case, if you deny the answer,

21:14

you can stop the hallucination, right? You can stop the hallucination, but still, it is not justified.

21:21

That nowadays, with so much powerful applications, with so much, with so much powerful applications, with so

21:26

many powerful AI agents, you are just denying it that, okay, I do not know the answer. That is also

21:31

not a very good option. In case, if I ask something, in case, if I ask something, what happens

21:37

after 1,000 years, which data is not available, what happens here? Again, works on probability. If you see that,

21:43

okay, let's say what will happen to the human species or, let's say, after 1,000 years. Now, based

21:51

on a lot of books, based on researches, based on research papers, it will try to find out the human

21:55

system that how it is going to evolve over the period of next thousand years. If it has some data,

22:04

if it has some research papers, it might be able to find out that. And it might not be able

22:10

to give you the exact answer. It can find out if there are, if there are any studies which are

22:15

available publicly that your LLM can check and based on that, it might be able to give you the

22:20

answer. Make sense?

22:25

Then everyone, we talked about limitations of LLM, static knowledge, they do not have

22:32

the access to your company's private policy documents, and hallucination is one limitation. Grounded

22:37

AI system. Grounded AI system, this term is quite important, right? Model's response should not

22:43

be based on external, unreliable, right? Uh, sorry, models response should be based on external,

22:51

verifiable, and reliable information. Then only you say that, that, that, that,

22:55

information, that answer is a grounded answer. Grounded means you have verified that answer.

23:01

You are not just trying to hallucinate. It is not a hallucinated answer. It is the answer which is

23:06

coming from based, which is based on some resource. It can be external, it can be internal,

23:11

but it should be a reliable resource. Then everyone, we talked about rag, retrieval,

23:17

augmented generation. There are two components which are very, very important in this term rag,

23:21

retrieval and generation. First, you retrieve the data. Now, instead of

23:25

only relying on the knowledge of LLM, right, the data on which LLM has been trained upon,

23:31

you try to add extra source of information. That can be in the form of database, that can be in the

23:37

form of internet, that can be in the form of documents, that can be in the form of books, etc, etc.

23:42

You give extra source of information to the LLM and what LLM can do? If they do not know the answer,

23:49

they will use this source of information, source of, you can say that knowledge source,

23:54

let's say policy documents of your company. They will go through the policy documents,

23:58

there might be thousands of policy documents, they will try to find out the best one,

24:02

maybe top one, top two, top three, based on, again, what type of search? What type of search

24:09

we perform in RAC systems?

24:18

Semantic search, similarity search, based on the user query, you get the query, you get the query,

24:23

you convert that query into embedding. Your documents have already been converted into the

24:28

form of embeddings. After that, after converting them into embeddings, you have stored them into the

24:32

database. What type of database? Vector database. So there are a lot of examples of vector database. One

24:38

of the example we are going to see in today's class in the implementation. When the user query

24:43

comes in, you convert the query into embeddings. Then with this query embedding, you try to find out

24:49

the nearest embedding in the vector database with the help of similarity.

24:53

search. Now, how to find the similar vector or the nearest vector that we already know from the

24:58

previous classes, like cosine similarity or Euclidean distance similarity. Remember that? That you

25:04

can perform similarity based on cosine similarity or Euclidean similarity, distance similarity. Once you do

25:10

that, everyone, for example, it's say you got one document, right? Or let's say first of all,

25:14

you were trying to find out the similar documents. Now, if in similar documents, can I say that

25:18

you can decide how many similar documents you want to find out? Top one, top two, top five,

25:23

top 10, right? Correct, everyone? And after that, using these top K documents, top one, top

25:30

top two, top three, using these K documents, you will try to find out the, you will try to generate a

25:35

relevant answer that you can return to the user. Is that point clear to all of you? Correct? So you

25:42

will try to find out the top five or top three most similar documents, right? So guys, I have already

25:49

returned the steps. You can go through that. You can revise the notes after the class once again.

25:53

So RAC combines the combination of retrieval of relevant information from the sources and generation.

26:00

There are two words which are very important, retrieval and generation.

26:03

So RAC combines retrieval of relevant information from sources and generation of responses in natural language.

26:09

This is very important.

26:11

Once you retrieve the documents from the sources, from the knowledge source,

26:15

should you return those documents as it is to the client, to the user?

26:19

That okay, this is the policy document, just go through it and find out your answer.

26:23

Does it happen like that?

26:30

No. You find the relevant source, you find the relevant document, then you give the context,

26:37

you give this information to the LLM. And to the LLM, you have already given some prompt that,

26:42

hey, LLM, consider yourself as a good support system of this company. Please be very, very polite

26:49

to the customers and try to give the answer based on this context. And you can ask you can

26:53

all this information in the prompt. What kind of prompt you can write? I will show you

26:57

in today's class. But is the idea clear to all of you? So whatever information you have retrieved

27:01

in the form of documents from the knowledge database, you will give that information to the LLM

27:07

along with some prompt and your LLM will generate the final answer that you will return to the user.

27:12

If you see, this is called as Generation Step. Absolutely Adita, it is called a system prompt. I'll

27:17

talk about it. We'll talk about it in some time. I will give you the demo as well. Are you guys

27:23

getting this point? Folks, yes, no. It is very important, right? So see, that's why I'm

27:30

giving you a quick walkthrough instead of just starting from today's class. Because today's class is

27:34

also based on the yesterday's class, like the last class. So instead of answering only from the

27:40

knowledge it has internally, the data it has been trained upon, system is answering using

27:45

other source of information, which is more reliable. Rag helps to solve some of the

27:50

limitations of only LLM. Grounding. We all know that. What is the Rack flow? You get the query.

27:58

You convert the query into embeddings. And before that, everyone, you have already stored the data in the

28:02

form of embeddings in the vector database. This is a pre-processing step. So if you have thousands of

28:08

policy documents, before even you start using the Rack system, you have already converted those

28:14

documents into chunks. The process of chunking we'll talk about today. Because a document can be very

28:20

big. So instead of storing the entire document as one entity, you can divide the document

28:26

into small, small pieces. Each piece is called as chunk. So you divide the document into chunks. For

28:30

example, let's say there is one document which is of thousand pages. Thousand pages at one place

28:35

is a very big thing, right? It will be very difficult for you to find out, to search. So what

28:39

you can do? Maybe let's say you can decide that okay, I will create one chunk of 10 pages. So

28:44

there is a document of 1,000 pages, 1 chunk, 10 pages. So total there will be 100 pages. Sounds good?

28:50

100 chunks, right? So now you create the embedding of each chunk separately and store that

28:55

into the vector database. Now it will be easier for you to search and perform any kind of operation.

29:01

Does it make sense to all of you? Right? So you have the query. Now once you have stored all the data

29:07

into the vector database, you have the query, you convert the query into embedding, then you perform similarity

29:13

search, right? And then everyone you provide the context to the LM and LLM will generate and generate the response

29:19

that you can directly return to the customer. Is that one clear to all of you?

29:26

Okay. So this table withdrawal, you can refer that. And guys, this is what we discussed in the last

29:31

class. Okay. So this is the entire flow. First, you have a lot of documents. First, you have a lot of

29:37

documents. You split these documents into small chunks, right? So that you can store them more

29:43

efficiently. You create the embedding of each chunk individually. Store them into the vector data

29:49

all the documents split it into chunks, create the embedding of each chunk, store these

29:55

embeddings into the database. Once you have stored these embeddings into the database, you will get

30:00

the user query, create the embedding of the user query, perform similarity search. You will retrieve

30:06

the relevant chunks, the chunks which are matching, which are similar to the user query. You do that.

30:12

Pass this to LLM along with the prompt. You have already set a prompt internally. How? We'll see that

30:17

in today's class. Using the prompt and the context or the right chunks that you have

30:23

retrieved, LLM will generate the answer and return to the customer. This is the entire flow that we saw

30:30

in the last class. Now, you will realize that after having this 10 to 12 minutes of revision,

30:36

today's class will become even more interesting and even more understandable. Everyone clear

30:41

till this point of time? Yes or no. Okay? So guys, now, in today's class, now, in today's class,

30:47

the agenda is going to like more of a hands on. We are going to build a system, right?

30:52

So the agenda is implementing a rag-based application. Okay? So we are going to implement to

31:06

implement a rag.

31:21

Now, what are we going to take an example? A very good, a very standard example, a very practical

31:27

example, everyone. So we are going to build a support agent for an e-commerce company.

31:36

support agent for an e-commerce company like Amazon.

31:45

E-commerce company like Amazon. Is the example clear to all of you?

31:49

So let's see we are going to build a chat system, a chat support agent for an e-commerce company like Amazon.

31:55

Now, tell me everyone, if you're building a support agent and if you're using some LLM internally,

32:03

right, let's say, for example, let's say they are using open AI LLM,

32:06

or they are using Google Gemini LLM or some open source, any LLM that you're using.

32:13

So in order to give more reliable answers, for example, if you ask a question around, let's say,

32:17

can I return a product up to 20 days? I ordered this item, can I return this now?

32:22

When will I get my refund? Now for all of these queries, do you think that any LLM in the world can give

32:28

the answer of these queries precisely? When will I get my refund? Can I return this product after 20 days?

32:34

after 10 days? No, these are the policies which are company-specific. Amazon may have their

32:39

own policies. Flipcard may have their own policies. Masi may have their own policies, right? So these

32:44

are the things that you cannot generalize. So what you need to do everyone is that along with having an

32:49

LLM, you need to provide the company policy documents to the LLM that LLM can use, that your AI application

32:57

can use whenever any query comes in. Is that point clear to all of you? Whenever any query comes in, you should

33:03

provide the company policy documents that your system can use, right? So we can say that

33:08

instead of allowing, so instead of allowing an LLM,

33:33

to answer the questions, to answer the queries only based on the knowledge,

34:03

We will provide it with the company policy policy documents that

34:18

companies

34:19

policy documents that LN can refer

34:29

refer

34:33

that LLM can refer to generate more reliable and better answers.

35:03

So, guys, when we talk about the policy documents, right?

35:06

So in this case, can you give me some examples, like what kind of policy documents you might need to provide

35:11

to the LLM, to the AI application for an e-commerce company?

35:18

Can I say that there can be policy documents with respect to return policy? That what are the

35:23

policies, what are the terms and conditions for returning a product? Return policy, return policy, refund policy.

35:33

a warranty policy, about the product warranty, right? Maybe let's say

35:39

shipping policy, and so on. So there might be thousands of such documents that you need to provide

35:46

to the system in order to give more reliable answers. Sounds good, everyone.

35:53

Take it. So guys, what we are going to do is we are going to spend maybe around next, it's 830,

35:58

around 30, 40 minutes on learning the architecture. That what are we going to do, how we are going to do,

36:03

and why we are going to do. And then we will see the implementation. So we have,

36:06

like, I have designed the class in such a way that it is going to be around 60% implementation,

36:12

40% conceptual think. Wouldn't it be better to train the LLM with the policy data instead of it

36:17

having to fetch every time whenever the question is asked? First of all, it's a right thought process.

36:22

So that particular process is called as fine-tuning. We will have a good number of classes on

36:26

fine-tuning as well. Is the question clear to all of you, first of all? That wouldn't it be better

36:30

to train the LLM with the policy data instead of it answering to fetch every time

36:36

whenever the question is asked. So instead of every time checking the database about the policy

36:41

documents, what that word question is asked, and based on that, fetch the corresponding policy,

36:48

the respective policy, why can't we just train the LLM? First of all, the thought process is absolutely

36:54

correct. This process of training the LLM on your custom information is, is a lot of the thought process is,

37:00

is called as what? It is called as fine-tuning, right? So the process of fine-tuning

37:06

is what, everyone? Let me give you a brief understanding of fine-tuning, just in a few minutes,

37:12

because fine-tuning is itself a big topic. We will cover fine-tuning as well in our classes.

37:17

Fine-tuning means that even that you already have an L-LM and you are trying to train the LLM,

37:23

or you are trying to feed some extra information inside the LLM, which is specific to your use case.

37:28

Make sense, everyone? Which is specific to your use case. Now tell me everyone, if you

37:34

have an LLM and you can train that LLM based on the company's policy documents, will that LLM

37:41

be smart enough now to give the relevant answers about the return policy, about the refund policy,

37:48

about the shipping policy, about the warranty policy? Answer is yes. Because you have fed

37:53

that information inside the LLM. You have trained now the LLM based.

37:58

on that information. It is the correct process. But everyone, fine-tuning is a very, very expensive

38:04

process. Because first of all, everyone, when you have an LLM, right? First of all, can you fine

38:11

tune an LLM which is running on some other server? No, right? So you should have your own

38:18

LLM in that case, right? For example, let's say you are using some open source or you are using some extra

38:23

model for that you are paying the money that is running at some location. Now, in order to

38:28

fine-tune that. Now, whenever you fine-tune any system, basically what happens is, like,

38:33

for example, let's say everyone, if you give me, if you give any extra information to the LLM,

38:39

which is having trillions of parameters right now, which have been trained on trillions of

38:44

data parameters. If you give more information to the LLM, what happens is inside the neural

38:50

networks, right? If you know about it, good. If you don't, it is okay. What happens, everyone,

38:55

is entire structure changes. Okay? It's.

38:58

It's not like that, you can just add extra information inside the LLM. Because everyone, for example,

39:02

if you're adding extra information about, let's say, human tendency or human behavior,

39:07

don't you think everyone, whatever is related in the world about human understanding inside the

39:13

LLM, everything needs to update it? Because you don't know what is going to be similar to the

39:19

information that you have inserted. Correct? So what happens is out of trillions of parameters,

39:23

a lot of data changes, the weight changes, the information changes, the similarity,

39:28

changes. The embeddings changes. That's for everyone, whenever you fine tune any model,

39:32

it is an ultra expensive process. Because you need to go inside the machine, go inside the

39:37

LLM and change the information at every place. Entire network changes. It is a hell expensive

39:46

process. Are you guys getting this point? Absolutely. Each and every node in the neural network

39:52

changes. And when you do that, it is expensive. It is not expensive. It is ultra expensive.

39:58

You might have to spend millions of dollars just to train a bigger model. I am assuming that

40:03

if you have a bigger model, right, you will have to spend a big amount of money, big amount

40:07

of resources. That's why fine-tuning is not something that every company can afford and every

40:12

company can do that very, very, very frequently. So for example, let's say you have a policy

40:16

documents. Now ultimately, policy documents are created by some people. So the support

40:21

people, there is a separate company, there is a separate team for that. If they make any mistake, if you

40:26

you have already trained your LLM on the existing policy documents and after one day,

40:32

you realize that there is some mistake in the policy document, then again you'll have to fine

40:36

tune. But now the fine tuning is even going to be more expensive. Getting the point, everyone.

40:42

So whenever you fine tune, the neural network changes. It's an expensive process. Sounds good.

40:48

But yes, actually it's a good point that you understood that point. If you're only using LM

40:52

for a niche use case, might as well make SLM as we have a few

40:56

parameters either way. If you do that, then LLM might not be able to give you better responses.

41:02

Okay, absolutely correct. If you have a very, very specific use case, for example, let's say if you're

41:07

building a system for Masai, Masai has a very simple use case. First of all, a simple use case of

41:13

education technology. There are let's say maybe 10, 20, 30 courses. At a point of time, how many people

41:18

might be there? Few thousand people. The scale is not very, very high. There is a decent scale.

41:23

But it is not as compared to Amazon or Flipcard or OpenEye.

41:26

Right. You can do that. But again, when you do that, even LLM fine tuning still be very expensive.

41:34

Right. Because see, the process of the term expensive also has a relative meaning.

41:40

Something which is expensive for me might not be expensive for someone else. Right. Make sense?

41:46

So that's why in terms of relativeness, right, in terms of relative expensiveness, it will still be an expensive process for a company like Maasai to train their own LLM or

41:56

to build their own LL. So that's why always it's better to have an external database.

42:02

Because external database, you can update anything, you want to remove a document, you want to

42:05

update a document, you want to create a new document, or you want to, let's say, you want to read

42:10

a document. The credit operations will be relatively simpler. Makes sense, sure. And that's why,

42:16

yes, coming to your question as well, does a company like Maasai needs to have the latest model

42:22

of open AI for their chat support system like GPD 5.4? That is ultra expensive.

42:26

No. A very simple AI model will work for these kind of simple use cases.

42:36

Okay. You will have to analyze that. If that is cheaper, then definitely we can go with that.

42:42

Drag is one solution. It's not like that. There are no other solutions existing.

42:46

Fine tuning is training LLM for the first time. No. Fine tuning is not training the LLM for the

42:51

first time. Fine tuning is updating. LLM is already there. You are adding more information to

42:56

LLM which is specific to your use case. Yes, Mokul, for smaller, not everyone is going to use

43:03

the GPT latest model. Not everyone is going to use the Claude latest model. So you are going to use

43:09

the model based on your use case, based on your budget. Makes sense? Folks, everyone clear? So what is

43:21

the problem statement we have that we are going to solve in today's class, right? So imagine that

43:25

there is an e-commerce company which has many customers, right? And the questions are

43:30

coming like, can I return a product after 20 days? How long, when will I get my refund? How long my

43:36

refund will take? When will I get my product? If there is any question regarding warranty, does

43:44

warranty covers accidental damage? Right? So, guys, a normal LLM can answer these questions based

43:52

on general assumptions, right? But if you want company specific, policy specific answers from the

43:58

LLM, you will have to add external source of information, which is policy, which are policy documents.

44:04

Make sense? So all these things I've already added in the notes, you can go through that, right? So

44:09

the core idea of Rags do not depend only on the LLM's trained information, LLM's memory, give the LLM

44:17

the right context before asking the answer, before asking the question.

44:22

So, okay, okay. Now everyone, okay. Now let's come to the generator part and the retriever part, right?

44:37

So guys, in the rack, the full form that we already know, rack stands for retrieval augmented generation.

44:52

interval, augmented generation.

45:02

If you see everyone, these are the two components which are very, very important for Rack,

45:06

retrieval and generation. So guys, you can divide your Rack application. When you implement, you

45:11

can divide your Rack application into multiple components. One component is the retriever component.

45:19

Now guys, as the name suggests, what?

45:22

what would be the task of the retriever component? What would be the task

45:28

of the retriever part inside the Rack application? Retrieve the data. Right? Absolutely correct.

45:37

And then everyone there will be a generator. There will be a generator which will generate

45:45

the final answer. Right? So guys, can I say that the task of retriever is going to be what? On a high level.

45:52

It will get the user query. It will convert the user query into embedding, a vector

45:57

embedding. Now for creating a vector embedding, do we need to write the code manually from scratch?

46:05

Do we need to create the text into embeddings manually? No. There are a lot of models present

46:10

out there. So for example, we can simply use Open AICA small model, which will give us the vector

46:15

embeddings in a good way. And it has good number of dimensions also. You get the query from the

46:22

you convert the query into embeddings using using some embedding model. Then before the

46:28

retriever everyone, can we simply assume that we have already stored our documents into vector database

46:34

in the form of embeddings? Correct? We have already stored our documents or policy documents

46:41

in that vector database in the form of embeddings. Now can I say that, to store the vector embeddings

46:46

into the database of the policy documents, you need to use the same.

46:51

embedding model for query as well. Correct? So you should use the same embedding model

46:58

for storing the vectors into the database as well as converting the query into embeddings. So you

47:05

have already prepared the database. So whenever query comes in, convert into embedding. Now

47:09

perform similarity search. That, okay, this is the query embedding. Give us the top 10 or top

47:16

top five nearest or similar documents, similar documents for this query.

47:21

You get, let's say, three documents. Now, guys, we will also talk about the top K documents. Should we have only one document? Should we have like top K? What should be the value of K?

47:30

1, 3, 5, 10 what? Should we fetch very less number of documents? Should we fetch very high number of documents? We'll talk about it. Once you have the documents, this is the task of retriever. Can we say that? The task of retriever is to retrieve the relevant documents from the vector database. Is that idea clear to all of you?

47:51

The task of the retriever is to fetch relevant documents from the database.

47:57

Then comes the part of generator. Once you have the relevant documents from the database, you give

48:02

those relevant documents to the LLM to generate the answer. That LLM would also need some prompt that

48:09

hey LLM please consider yourself as a customer support agent for Amazon. Use these documents to

48:15

generate the answer. You will have to write some system prompt. What will see that? That is the task of

48:20

generator.

48:21

So, Retriever comes first to retrieve the corresponding right set of documents. Then comes the generator to use these documents and generate the final answer.

48:31

Make sense everyone? So simply we can write this flow in such a way that you get a user query.

48:40

Right? This user query everyone will be given to Retriever.

48:47

Now, guys, I'm not writing all the individual steps.

48:51

because that we are going to see in the code. Retrieval will convert into embeddings,

48:55

perform similarity search, et cetera, et cetera, relevant, get top five documents, top three documents.

49:01

That is the task of retriever. Make sense everyone? Retriever will do all of these things.

49:06

After that, everyone, retrieval, whatever documents we have retrieved, right, those are called as

49:12

relevant document. So can I say that, retrieval will give us, retriever will give us relevant documents.

49:20

Yes or.

49:21

everyone. These relevant documents, everyone, you will give to the next component

49:29

which is generator. Folks, yes, no? Which is, which is generator. Now, what is the core part

49:42

of generator? Tell me, what is the core part of generator? Inside generator component, generator is just

49:49

one logical thing, right? Inside generator, who is working as generator? Who is generating?

49:53

It is what? LLM, right? It is LLM. Right? And finally everyone, LLM, will give you the final response.

50:08

This is the final thing that we are going to implement in today's class. Everyone, clear?

50:19

Okay? Now let's talk about everyone. The main components of Rack system.

50:41

And what are we going to implement in today's class? What all the components we are going to implement in today's class? What all the components we are going to see one by one?

50:47

First of all, everyone, we have the knowledge source. Correct? The knowledge source. In the form of, generally, it can be in the form of documents, it can be in the form of PDF, it can be in the form of images, it can be in the form of anything, right? So generally, you can say that. In our case, knowledge source is going to be policy documents.

51:14

So everything we are going to see from our example point of view, right? That what are we going to implement?

51:23

These policy documents, everyone, these knowledge sources, can is that you will convert into chunks.

51:31

Yes or no, everyone? Second component is chunk.

51:37

Folks yes or no? Why chunking is important?

51:44

If your documents are very small, let's say one page document, just one page each document.

51:49

Do you need to convert that one pager document into chunks individually?

51:54

Further?

51:57

Not really, not required, right?

51:58

So generally, everyone, the chunking process, you perform for large documents.

52:05

So what do you do?

52:14

are splited into chunks for better for better processing and searching.

52:44

species of information absolutely correct. That's correct. Okay?

52:49

Then everyone, the next component that we can think of is embeddings. Everyone knows about embeddings.

52:55

Numerical representation of data. List of numbers, numerical representation in a vector space of n

53:05

dimension, 10, 20, 100, 500, any number of dimensions. Then everyone we are going to use vector database.

53:14

knows about vector database also. We have seen the implementation as well. Correct?

53:18

So these are the things that we are going to implement and obviously everyone, we are going

53:26

to have an LLM as a brain of our application which will generate the final answer. Now everyone, let's

53:35

talk about the retriever component. The first thing that we are going to implement in this example.

53:40

So retriever component is the component which is actually

53:44

responsible right in fact yeah so retriever component is the component which is

53:51

responsible for retrieving the relevant chunks relevant documents correct then generator is

54:10

nothing but LRM. Okay. So I think everyone, we are done and now we can start

54:24

the implementation. So these are the components that we are going to implement. So we are going to

54:28

have a knowledge source. We are going to have chunks. We are going to have embeddings. We are going to

54:33

to have vector database. We are going to have a retriever and we are going to have a generator.

54:36

Everyone clear? If yes, we can start.

54:40

with the implementation. So do you want to go through this document before

54:47

we start the implementation so that we can complete the implementation in one stretch without any break?

54:51

So instead of having a break after maybe 10 minutes, 15 minutes, we can have a break right now.

54:57

So that the entire implementation we can complete in one stretch without any break in between.

55:03

Okay? So let's have a break everyone. So I'm sharing this document with all of you. In fact, let me share

55:09

is the previous document which is in fact having more information. Okay?

55:20

Let me share the link with all of you. You can revise and after the break we will start with the

55:24

implementation. So folks, it's 846. So let's meet around 10, 12 minutes after the break, after the

55:39

So it's around like 8, 5, 8, 5.59. So let's meet at 9 p.m. Sharp. Then we'll have around

55:45

1 hour, 1 hour, 10 minutes to complete the implementation. Okay? Can you share both? Sure.

56:09

Okay.

56:39

Thank you.

57:09

Thank you.

57:39

Thank you.

58:09

Thank you.

58:39

Thank you.

59:09

Thank you.

59:39

Thank you.

1:0:09

Thank you.

1:0:39

Thank you.

1:1:09

Thank you.

1:1:39

Thank you.

1:2:09

Thank you.

1:2:39

Thank you.

1:3:09

Thank you.

1:3:39

Thank you.

1:4:09

Thank you.

1:4:39

Thank you.

1:5:09

Thank you

1:5:39

Thank you

1:6:09

Thank you

1:6:39

Thank you

1:7:09

Thank you

1:7:39

Thank you

1:8:09

Thank you.

1:8:39

Thank you.

1:9:09

Thank you.

1:9:39

Hi everyone.

1:9:54

So what we are going to do?

1:9:56

Let's start our Visual Studio.

1:9:58

And we are going to create a new project.

1:10:02

So let's say open a folder.

1:10:07

So we'll create a new folder.

1:10:08

folder.

1:10:09

And let's give the name of the folder as e-commerce rag application.

1:10:15

Okay?

1:10:16

So let's open this.

1:10:18

Okay.

1:10:19

So what we're going to do, everyone?

1:10:21

We will create, we have created new new project.

1:10:25

Then we will go to the terminal.

1:10:28

Open the terminal.

1:10:29

Yeah.

1:10:34

And

1:10:38

Yes, yes, Aditha, we are going to do that only.

1:10:42

We are going to use OpenEI as embedding model.

1:10:44

Python 3, and we are going to create a virtual environment.

1:10:48

I think we have talked about virtual environment in the past, right?

1:10:51

All of you are aware of that.

1:10:53

Create a VNV.

1:10:55

And just we need to activate it, source VENV slash bin slash activate it.

1:11:03

Now if you see, our new virtual environment has been created and we are going to install all

1:11:08

dependencies. So first of all everyone, we need to install PIP3 install open AI, install

1:11:15

OpenAI, let it install. Done, then install PIP3, install ChromaDB. So guys, we are going

1:11:27

to use ChromaDB as a vector database. Let's install that. Okay. So it will take just a few

1:11:37

seconds.

1:11:38

Done.

1:11:41

Okay.

1:11:42

And then everyone, what we are going to do is we are going to create a new file which is called as, let's

1:11:46

call it as e-commerce rag.p.py.

1:11:52

Okay.

1:11:56

So from this everyone, we will install, we will import OpenEI from Open AI import, open AI, okay?

1:12:06

Then we will import Chrome.

1:12:07

ChromaDB. Okay. Everyone clear till this point of time. Okay. Now everyone, we will

1:12:18

have to create, let's say for example, if you want to use open AI small embedding model. So we

1:12:25

will have to create a client for open AI, right? So we will create open AI client. Now to create

1:12:32

the open AI client, we will use this constructor or use this function called as open AI. So open

1:12:37

provides you this function. But everyone, this, to create an open AI, see, is open AI freely

1:12:44

available to use? Is open AI freely available to use? No. It is not free. Right? You'll have to pay for

1:12:51

that. Now, if you're using open AI, right, you are creating a client for it. And using this

1:12:57

client, you will make API calls. You will use some AI model from open AI. You'll have to pay for it.

1:13:03

For that, you need to create an account on chat GPT. You will have to create an account on open AI,

1:13:07

platform and you will have to create a secret key or API key that you'll have to

1:13:13

set here. So for example, if you see this function, Open AI, accepts an input parameter called

1:13:21

as API underscore key. So what you need to do is, for example, let me show that to you. Go to your

1:13:29

Open AI platform, log into that, just let me log into my account. I have. I have,

1:13:37

some balance present in available in my open AI account. If you look at this, this is the open

1:13:42

AI account. I have around $4 remaining. That is more than sufficient for now. What we will do is

1:13:48

everyone, you will go to API keys. Here, everyone, you will have to create a new API key or new secret

1:13:55

key, create it, and give any name to the secret key. So for example, let's say e-commerce,

1:14:02

e-commerce rag demo. Any name you can give and create a secret key. So this secret key is

1:14:11

associated with your account. So you will have to give the secret key here. So API key is equal to this.

1:14:17

Now OpenAI will allow you, will allow you, will allow you to use your account from the code. Is I

1:14:24

declared all of you? Now in this way, Open AI will allow you to use the account, the open AI APIs from your code.

1:14:32

But don't you think, everyone, if I give the API key like this, anyone can copy paste it from my code.

1:14:38

For example, if I upload this code on GitHub, anyone can use it?

1:14:42

Yes, sure, obviously I will hide it. Anyone can copy paste it. It means that if you can copy paste my key,

1:14:48

right? You can make API calls to my account from my account and obviously it will burn my tokens, right?

1:14:55

It will use my balance. That's why everyone, whenever you recharge, you put any amount in your open AI platform,

1:15:02

in your open AI account, always, there is an option of auto pay, right? That if balance goes

1:15:09

less than $1, again, add $10. Always disable that. Just one hack. Also, even if you have

1:15:17

limited balance or unlimited balance, does not matter. You should not expose your API K like this.

1:15:22

Everyone clear? You should not expose your API key like this. So there are different ways for

1:15:28

that. One simple way, at least that I prefer, set API key as a.

1:15:32

environment variable, right? What are environment variables? Environment variables are your

1:15:36

machine level variables. So what I can do everyone is I can export, I can, in the terminal, I can use

1:15:42

a variable, open AI underscore API underscore key. Please note that the variable name should be seen.

1:15:48

OpenAI underscore API underscore key. If you do that, give comma, double quotes, copy paste,

1:15:56

paste the API key, then double quotes. Enter. If you do that everyone, you have stored.

1:16:02

a variable with the name, OpenEI underscore API underscore key, with this value.

1:16:09

Now you don't have to provide API key inside your code.

1:16:12

Now when you're going to create the Open AI object, a client, it will automatically check.

1:16:18

First, it will check that have you provided the API key inside the function.

1:16:22

If yes, good enough. If not, if not, then it will check that, have you set any environment

1:16:27

variable with this name. Okay, if you have used this name properly, correct?

1:16:32

it will automatically use this file. Now everyone tell me if even if I'm going to commit

1:16:37

this code on GitHub, still, will my API key be exposed now? Will my API key be exposed now?

1:16:45

Answer is no, right? Because this API key I am not putting in my code. This API key is present

1:16:49

in my laptop. And obviously you guys cannot access my laptop. So what I am going to do everyone

1:16:55

is I'm going to create a environment variable and use like this. Now obviously after the class,

1:17:00

what I'm going to do is, even if you are very smart and you say that, okay, you can type it

1:17:05

after the class by pausing the recording. What I'm going to do is after the class, I'm going to

1:17:10

delete this. Does it make sense to all of you? Okay? Anyways, is the idea clear? So this is how

1:17:17

we can create an open AI, a client. Okay? Then everyone, we will define that what embedding model

1:17:23

we are going to use. Let's say, I am going to use Gemini key? Absolutely yes.

1:17:30

You can use any model here. OpenA is just one example. Embedding model. What model we can use?

1:17:36

So we will use, so for example, go to documentations, go to API docs, go to embeddings, vector embeddings, and here, search the model, this model, small model we are going to use.

1:17:55

So this is the model that we are going to use. Then everyone, what LLM model we are going to use.

1:17:59

Let's say everyone we will use the LLA model of GPT-5.4. Does it make sense for all of you?

1:18:06

The latest model. Sounds good? Okay. The first step. This is the first step, everyone,

1:18:13

setting up all the variables. Right? First is creating an open AI client. Okay? The second step.

1:18:23

Second step is creating or defining, defining, embedding and LLM model. Sounds good? Then the third step, everyone.

1:18:45

Third step is, now we have to do what? Now we need to create, create policy documents.

1:18:52

or sample policy documents. Now, for our use case, like, one thing is that you

1:18:58

can do is everyone is you can create actual documents of thousands of pages. For that, it will take

1:19:04

a lot of time. So what I have done is, obviously with the help of AI, I have generated some sample

1:19:10

policy documents. Let me copy paste them right here. So these are the policy documents that we can

1:19:16

use directly. Just look at it, everyone. There is, if you see policy documents, it is a list

1:19:22

It is a list. Inside this list, there are multiple documents. This is document one.

1:19:26

This is document two. This is document three. This is document four. There are total four, five,

1:19:32

five documents. Sounds good. And in each document, everyone, what we have stored is the idea of

1:19:37

the document, return policy one. Then there is some text of the document. Then there is some metadata.

1:19:43

Metadata, we all know the data about data. Some extra information that you want to store

1:19:47

about the document. For example, category of the document, type of the document,

1:19:52

who created this document, when this document was created, etc, etc, right?

1:19:56

So for example, categories, returns, right?

1:20:00

Sources, return policy.

1:20:02

Other than we can do that as well.

1:20:03

We can explore that.

1:20:04

We can have PDFs also.

1:20:05

We can have text files also.

1:20:07

Simply for now, we are having simple a list of documents in the code itself.

1:20:12

So that it will not take a lot of time to parse and read the documents.

1:20:17

Otherwise, it will take a lot of time as well for us to write the code.

1:20:22

Because the whole idea is to look at the retrieval augmented generation flow.

1:20:28

The retriever should be working. The generator should be working.

1:20:30

That should be the main idea for the session.

1:20:34

Are you guys getting the idea? So this is the first document.

1:20:37

Then it is a, first of all, it is a return policy document, then we have the refund policy document,

1:20:41

then we have the shipping policy document, then we have the warranty policy document, and then we

1:20:45

have the cancellation policy document.

1:20:47

Everyone clear? Give me a thumbs up.

1:20:52

Then, folks, what we are going to do is, this is the third step.

1:20:57

Then everyone, we are going to write the four step, which is create embeddings.

1:21:03

Create embeddings.

1:21:04

Now, obviously, everyone, we will use the open AI model to generate the embeddings.

1:21:08

So for that, we will write a function, let's say, define, create embeddings.

1:21:18

And this embedding, everyone, this function, what this is going to take?

1:21:22

Can we also give DB call like SQL directly as a part of document?

1:21:27

Generally not.

1:21:28

I don't think, right, that you will provide a DB call.

1:21:32

You, if you have something in the database or some external source, download it and then provide it to the,

1:21:37

then use it as a policy document.

1:21:39

It would be easier.

1:21:41

Okay, because ultimately that particular thing you'll have to store in the database.

1:21:44

Okay?

1:21:46

Okay. Okay. So guys, here you will get the text.

1:21:48

So for example, everyone, we are writing this function in such a way that

1:21:51

this text we will provide in the form of, let's say, list of, let's say, maybe list of string.

1:22:03

What is, why we are doing that?

1:22:05

I will just let's just let you know in some time.

1:22:06

For this, everyone, you will have to import, you'll have to import from typing module, import

1:22:13

list, and dictionary.

1:22:19

So this is the list of string.

1:22:21

And what this is going to return everyone is, we are going to create, if you see, for example,

1:22:32

everyone, let's say the input is going to be something like this, list, okay, list of string.

1:22:37

For example, this string, then another string, then another string, and so on.

1:22:43

If you provide this type of list to the create embedding function, function, can I say,

1:22:48

it will, it should create the embedding of this string.

1:22:50

it should create the embedding of this string.

1:22:53

It should create the embedding of this string.

1:22:55

Correct?

1:22:56

It will have three embeddings of one, one embedding of each string.

1:23:01

Now, everyone, what is one embedding?

1:23:02

It is a list of floating point numbers, right?

1:23:06

So, do you think the output of this is going to be a list inside a list.

1:23:11

A list contains list like this, 1.2, 0.9, 0.6.

1:23:18

Then, and so on. Okay? Then another list similar to this. Another list of embeddings.

1:23:26

Is that point clear to all of you? So what is going to be the output of this function?

1:23:30

The output of this function is going to be a list and a list of floating point numbers.

1:23:36

How many if you're getting this point?

1:23:41

List of list of float. Okay. And then let's start the implementation. So this create embedding function,

1:23:47

function will take a list of string in the input. I will tell you how and why. It returns

1:23:53

a list of list of embeddings, right? You can say that a list of vector embeddings because every

1:23:59

embedding is a list of floating point number. Right. Now everyone to convert this, to convert anything inside

1:24:07

embedding, we will use open AI client. So let's say we will use open AI, open AI client. Dot responses,

1:24:14

is dot embeddings, dot create. Then everyone, we will provide that what model we are

1:24:19

using. Model is equal to what? Model is equal to what? The embedding model. Correct everyone? The embedding

1:24:27

model. Is that concrete to all of you? And the input text of what text you want to generate the

1:24:36

embedding. So input is equal to the text. So folks, what happens is that this input function,

1:24:43

this input parameter of this open AI API expects a list of string. Make sense? So if you

1:24:51

have a list of strings, so what you can do everyone is you can create the embedding of each string in just

1:24:58

one function call. What this create embedding function does is, it will consider this text as a list of

1:25:04

string. It will automatically iterate through each string one by one in a loop, then it creates the

1:25:09

embedding and as a response it returns list of embeddings. Is that point clear to all of you?

1:25:19

Is that point clear to all of you? It will return the list of embeddings of each string of the entire

1:25:25

input. So once you have the embeddings everyone, what you can do? Embedings is equal to. See, in this

1:25:34

response everyone, what we have is we have responses, response dot data. So what we can do, we can do, we

1:25:39

you can iterate through each response. Okay, so maybe you can write in this way, for each,

1:25:46

let's say, responses for each, for each item in responses, what we can do?

1:25:57

Responses. Dot data. Inside responses, you have data and in that data, you have a list of

1:26:04

embeddings. You iterate through each embedding and what are you going to do?

1:26:09

Because even these responses will have a lot of other things also.

1:26:13

I think we have seen in the past also that when you call any model, it returns you a lot of data.

1:26:20

So out of all the data, what do you need?

1:26:22

You just need the embeddings.

1:26:24

So what do you do, you create an embeddings as an empty array, right?

1:26:29

And iterating through each item, you simply do embeddings dot append item.

1:26:34

Is that point clear to all of you?

1:26:38

Simple.

1:26:39

Okay? Now, instead of writing these three lines of code, can you just do this as well? Let me know if you understand Python up to this level. So let's say item dot embedding for each item in responses dot data.

1:27:09

Tell me, and here also we need to do item. Embedding.

1:27:16

Tell me everyone, these three lines and this line, they are absolutely same.

1:27:28

Can you just identify that whether they are same or not?

1:27:32

Can you just confirm?

1:27:34

Ultimately what we are doing?

1:27:36

We are just iterating over responses.

1:27:38

dot data through each item, we are just getting the embedding out of it, storing that in a list.

1:27:44

And finally we will return this list of embeddings, return embeddings.

1:27:48

This is what we are going to do.

1:27:51

How many if you're clear with this function?

1:27:54

Kind of simple Python, nothing to do with AI, RAG, open AI, nothing.

1:27:58

Simple Python.

1:27:59

Plain Python.

1:28:00

Okay?

1:28:02

Now everyone coming to the next function, once you have created the embeddings, now guys, one thing to

1:28:08

note here is maybe inherently I'm trying to use all the best coding practices here

1:28:15

as much as at least what I know. If you see, I have used a variable here embedding model.

1:28:22

Can you tell me why? Why I cannot, why I just didn't write this string as it is here?

1:28:29

We can do that. Why we are not doing that? What is the benefit that you are creating a global

1:28:36

variable at the file level, right? And you are defining this variable, text embedding

1:28:42

three small at that place. Reusability, absolutely correct. If you see everyone, let's say if you are using

1:28:49

this model at 10 different places in your code, let's say you are using this model, you are using this

1:28:54

value, text embedding three small at 10, 20 places in your code. Now everyone, tomorrow, if you want

1:29:01

to change this model, let's say from small, you want to go to large model. You want to use a big model.

1:29:06

large model. Don't you think if you're using directly this variable name at all the places,

1:29:10

you'll have to go to all the places and make it from small to large, right? Make it small to large,

1:29:16

change small to large at 20 places. Now, because, don't you think it is, first of all, a cumbersome

1:29:23

process. It is a difficult thing to do in a bigger code basis, in big code basis. Also, everyone,

1:29:28

this kind of approach is prone to errors. It is quite possible that you might end up making some

1:29:35

mistake. Why? For example, let's say at 20 places you want to migrate from small to large.

1:29:40

But what if everyone, you forgot to do that, you forget to do that at two places out of 20?

1:29:45

It means that at 18 places you changed, two places you did not change. So again, a wrong thing, right?

1:29:52

But if you're using a variable and if you're using, if you're changing it from small to large,

1:29:57

you just change it at one place. So wherever you are using this variable, they will start using the updated model.

1:30:05

Correct everyone, they will start using the updated model.

1:30:08

Folks, yes or no?

1:30:09

So that's why it's always better to use variables as much as possible if you have clear understanding.

1:30:15

Getting the point.

1:30:18

Getting the point.

1:30:20

Perfect.

1:30:21

And everyone also, if you see, I'm writing the things inside small, small functions so that you can reuse them.

1:30:27

First function is to create embeddings.

1:30:29

Second function is to set up vector data way.

1:30:33

Set up.

1:30:35

vector db and everyone for vector db we are going to use chroma db i hope all of you remember

1:30:40

chroma db all of you remember chroma db okay so let's do that define setup vector db right no input

1:30:55

parameter required we will simply do chroma client is equal to chroma db dot persist

1:31:05

client and guys, you can give the path here, path is equal to dot slash chroma underscore

1:31:13

policy underscore DB dot, yeah, just db.

1:31:18

Make sense everyone?

1:31:19

So why we are giving dot slash?

1:31:20

Because we want to create this chroma policy database in the same folder, right, in the same

1:31:28

directive, at the same path.

1:31:30

If you want to give other path, you can give the entire path here.

1:31:34

And then everyone.

1:31:35

when we create a collection, remember that collection, kind of a table inside ChromaDB.

1:31:41

Right?

1:31:42

Chroma client dot get or create, get or create collection.

1:31:47

Then you give the name of the collection.

1:31:50

Name of the collection is, let's say, policy documents, e-commerce, whatever name you want,

1:31:57

e-commerce policy, documents, or collection.

1:32:03

Okay.

1:32:03

And then everyone, you give some metadata.

1:32:14

I think this is also good enough.

1:32:16

Apart from that, you don't need anything else.

1:32:18

But if you want to give other things, you can provide that, right?

1:32:22

But I think you can just, I think in the last class also we did not give anything.

1:32:25

Just let me check.

1:32:27

I think where did we write the code?

1:32:28

Book Summurizer, a React agent.

1:32:33

No, this is not R code.

1:32:43

Python vector search.

1:32:46

Yeah.

1:32:53

Embedding function none.

1:32:56

Yeah.

1:32:57

It is an optional parameter.

1:32:59

Even if you don't do that, it is okay.

1:33:03

Is everyone clear till this point of time?

1:33:15

Creating a client, creating a collection.

1:33:18

And finally everyone, this function will return the collection.

1:33:22

Okay?

1:33:23

So as of now, have you stored anything inside this vector database?

1:33:26

Or you have just set up.

1:33:33

We have just set up.

1:33:38

Then everyone, we will write the retriever component.

1:33:41

Sixth step is retriever component.

1:33:48

Now what we're going to do in retriever component, let's see.

1:33:53

Define, retrieve policy content.

1:34:02

Now to retrieve.

1:34:03

policy content everyone, what do you need? What do you need? Do you need the user query?

1:34:15

In the form of thing? Correct. Obviously, right? If you are asking a query about refund, so you

1:34:23

should have the query. So based on the query only, you will find the relevant documents. So first you

1:34:27

should have the query. Then you should have the collection. What is collection, everyone?

1:34:31

where you should search, huh? Which collection you should search? Correct, everyone?

1:34:39

Then everyone, there is another parameter that we are passing here, which is top K. Okay? Which is

1:34:45

top K. Now, what is the meaning of top K, everyone? So you should provide an integer here

1:34:49

that how many top nearest documents you want to retrieve? Top 10, top five, top three, top one,

1:34:57

whatever. Now everyone, this can be a default parameter.

1:35:01

that user can choose that should they, do they want to fetch five relevant documents,

1:35:07

10 relevant documents, 100 relevant documents or whatever. If they don't provide, by default,

1:35:13

we will fetch three top three relevant documents. Does that make sense to all of you? Top three

1:35:20

relevant documents. Make sense? And finally everyone, what this is going to return? Any guesses?

1:35:27

What this is going to return?

1:35:31

Let's see. Okay, this is a tricky part. I will let you know.

1:35:38

Okay, text, string, I'll tell you. Don't worry. Okay? I will tell you.

1:35:46

So let's put a question mark. Okay? So first everyone, we are getting the query. First

1:35:55

Can I say that, convert the query into embedding? Query embedding.

1:36:01

So we can see that query underscore embedding. Now you see that everyone, we can directly

1:36:08

call this function create embeddings. We can directly call this function. You don't have to

1:36:12

do this kind of work again and again, again and again, correct everyone? So what do you can

1:36:18

do? Create embeddings. But in this create embeddings everyone, we have to pass a list of string.

1:36:25

We have to pass a list of string. But we just have one query. So we need to pass this query in

1:36:30

the form of array, in the form of list, in the form of list, right? Query. Everyone clear?

1:36:35

Okay. Folks, yes, so? Also everyone, if you see, we are passing a list of string,

1:36:47

what this query embeddings will return? It will also return a list of string, list of embeddings.

1:36:52

But inside that list of embeddings, you will just have one embedding. Because in the string, in the input, you just

1:36:59

have one string. So you just get the first element of the list, right? Because you want the exact

1:37:04

embedding, not the list of embeddings now. You know? Getting the point, just getting the element from

1:37:09

the array. And then everyone, you get the result. How will you get the result by performing similarity

1:37:15

search? Perform or semantic search or similarity search. Okay. So how do we do that? We all

1:37:26

have seen that particular thing. So collection dot query.

1:37:29

In collection. query, what do we do? What do we do? Query is in list. Can you please repeat?

1:37:38

Query is in list. Because this create embedding functions is expecting a list of string.

1:37:48

Right, Aditha? So for example, let's say you have to pass ABC. But it is not expecting ABC. It is

1:37:55

expecting a list. So instead of passing ABC, you do that, you pass ABC. You pass ABC. You pass ABC.

1:37:59

inside a list. Simple. Right? This is what we are doing. Also, why this zero? Because if you are passing

1:38:06

this as a list of string, it will also return a list of embedding, right? It will also return

1:38:11

Pratius, a list of embeddings. But if you see, there is only one item in the list. So don't

1:38:16

you think list of embedding will also have one item? List of embeddings will also have one item. So

1:38:21

you are fetching that item. Make sense? Because now you will have exact embedding, not list

1:38:27

of embeddings. Because you will use this embedding.

1:38:29

in the query now, in the similarity search now. Makes sense?

1:38:33

But query has a number of words. We are considering one query as one word, one sentence.

1:38:51

Okay, we are not finding the embedding of each word again and again, like individually. We are every query, it might be having 10 words.

1:38:59

So we are considering one query does not matter whether it has 10 words, 100 words.

1:39:04

Query is query. So that entire query will be considered as one entity.

1:39:11

Okay? So if see, if one query has 10 words. So you are thinking in this way that every word will

1:39:18

have its own embedding. It means that for one query, you will have 10 embeddings. Let's say when I'm

1:39:24

going to get my refund. When I am going to get my refund. So let's say there are eight or 10 words,

1:39:28

8 to 10 words. So will you find the embedding of each word individually? What, when I am going

1:39:34

to get my refund? Does that make sense? So this entire query is one entity, right? So you will

1:39:42

find the embedding of this entire query in one go. Okay? Yeah. So then everyone, what we are going

1:39:54

to do? In the result collection dot query, it means that you are performing a

1:39:58

a similarity search on this collection where you have stored the vector data in you have

1:40:03

stored the embeddings. What do you do? You provide the query embeddings. Query embeddings is

1:40:07

equal to what? Whatever this query embedding is, because this query embedding is again expecting

1:40:13

a list. So you can provide this query embedding. Then after providing the query embedding,

1:40:19

you need to provide how many results do you need? N underscore results. Top K, top 1, top 2, how much?

1:40:27

top K. And then everyone, it includes, uh, actually I forgot the syntax. Let me just

1:40:34

open the vector search function. Yeah, if you see IDs, then documents, uh, not

1:40:43

collection dot absurd, query. Where is query up? Embeddings and end results. Okay, that's it.

1:40:49

Only two functions are required. Okay, only two parameters are required. The query embeddings and the

1:40:55

how many results do you want? I think we have already seen this particular concept,

1:41:00

so you already are aware of that. So nothing else. Is the function call making sense to all of you?

1:41:05

This is what similarity search is that. Folks, yes or no? Okay? After this everyone, you

1:41:17

have the results. In this results, everyone, let's say if the top K value is three, if the top K value,

1:41:24

K values are top K values three. Can I said in this results, there will be total three documents.

1:41:35

Right? Total there will be three documents here. How many documents? Three documents. Now,

1:41:39

from these three documents, what do we want? We want, let's say, top three documents may fetch all the things.

1:41:46

Documents. Then we will have, let's say, the metadata of the documents, right? Then we will have the

1:41:52

distance of the documents also. Why?

1:41:54

we are going to use this. Let's talk about it. We will see that. So results may, results of, results may there will be documents. So you are getting the top document. This is the top, the first document.

1:42:11

You can say that. Okay, I'll have to, I think I'll have to print it out. Okay. So what you can think of

1:42:17

everyone is that inside the results, you will have the documents, okay? And then

1:42:28

you will have the metadata. I'm just trying to visualize the structure of this results part.

1:42:47

How we are, how we were using there.

1:43:06

Just one second, everyone. So we are getting the result and result may, we were just printing the result. And when we were just printing the result. And when we were printing the results, it was giving us.

1:43:17

Results and score 3. It was giving us documents, metadatas, and the distances also.

1:43:25

I can recall that now. Okay. So I think, okay, let's do one thing. Let's do one thing.

1:43:34

For now, let's directly return the results. Okay.

1:43:42

Okay. Let's directly return the results. Is the function making sense to all of you? If there is any

1:43:47

change, I will do that in some time. Is the function clear to all of you? How we are

1:43:53

retrieving the relevant policy documents. Okay? Then everyone, we are building the prompt. Let's

1:44:17

Okay.

1:44:32

And this result will be what?

1:44:38

Let's remove this as well. So it is returning this. Okay, fine. And the seventh step is. Now everyone, once we have retrieved the relevant components, now we need to write a prompt, a system prompt that we will give to LLM along with these documents, correct everyone? That LM will use to generate the final response, right?

1:45:08

that LLM will use to generate the final response, correct?

1:45:12

So let's write the prompt for that. Let's say build system prompt.

1:45:17

Or let's say build the prompt. Build prompt. Are you guys getting this point?

1:45:22

Build prompt. And in this everyone, what we will get? We will get the user query.

1:45:28

Right? And we will get the retrieved, uh, retrieved documents.

1:45:38

Okay. In fact, everyone, in fact, what we can actually do is, in order to make it even better,

1:45:44

if you see from these documents, in these results, right, in fact, everyone, for simplicity, let me do one

1:45:51

thing. For better my understanding as well, for your understanding as well, I've actually forgot the

1:45:57

actual structure of the results. Let's actually verify that. Let's try to run this code. Remember this

1:46:02

code? Right? In one of the classes in implementing vector database, we wrote this code, right?

1:46:08

Let's try to run this code and let's see that what exactly result we are getting when we are running the similarity search.

1:46:17

Right? So what we will do, Python 3 vector db.p.py. So let's do that and I think we should be able to get a decent result.

1:46:38

Guys, let's make everything while this is not working.

1:47:08

Actually, let's make it three.

1:47:26

So we are returning, we are retrieving top three documents.

1:47:38

Yeah, if you see everyone, in the results, we are getting, first we are getting, so if you see we are getting a dictionary, right?

1:47:44

Right? We are getting a dictionary in which we have IDs of the documents which are being retrieved.

1:47:49

Then we have the embeddings. Then we have the documents. Correct everyone? In the documents, we have all the list of list.

1:47:57

Getting the point? Books, please participate in the discussion. In the result, in the results, we have results is what? It is a dictionary.

1:48:07

Inside the dictionary, we have documents. And inside the documents, what is this? It is a list. And inside the list, there are, there is each document. Okay? So if you see, there is this document, refunds are processed within five to seven days. Then there is another document. Customers can return the product like this. Then if your payment is like this and so on, right? So you have a list of list. Okay, good enough. Then everyone, we have URIs, not required, included.

1:48:37

what we have included, we are getting metadatas, documents, and distances.

1:48:42

Then everyone, if you see, we are getting metadata also, that source of the first document is policy,

1:48:47

category is return. For the second, for the second, what do you say?

1:48:51

For the second document, category is returns, sources, policy. Third document and fourth document,

1:48:57

like, and so on. Right. So it is like, if you see, it is also a list of list. Right? So first document is what?

1:49:04

Refunds are processed. So for that, the policy is,

1:49:07

this thing, right? Source is policy and so on. Then the distance of each document, are you guys

1:49:12

getting the return structure now? That what we are getting in the result when we perform

1:49:16

similarity search? What do we want? We just want these documents for now. If we get the documents,

1:49:23

will we be able to read, will we be able to generate the answer? Will we be able to generate the answer?

1:49:29

Answer is yes. How? Let's see. From the results, everyone, if you have to get the results from the

1:49:36

results. Can I say results made? Get the documents? And this is a list, everyone.

1:49:45

From this list, right? This is the structure of the results. Right, Chirac? Because what can happen is

1:49:53

you can perform multiple searches. You can give multiple queries. So these are the documents.

1:49:59

Actually, a very good question. If you see why we are having a list of list. Okay? So if I, so if I

1:50:06

copy paste this. This is the document structure in the result. Let me copy paste that.

1:50:16

If you see everyone, now, are you able to see the document structure? The result structure? So results may say, get the documents. But that document, everyone, if you see, there is a list of list. And there is only one item in the list. Inside the list, there is only one item, there is only one item.

1:50:36

Can someone tell me why?

1:50:39

That all the documents are present at in one list? Why?

1:50:45

Because there is only one query. If you give multiple queries, can I say that you can create

1:50:50

another list of top K documents of the next query? Document 10, document 2, and document 5,

1:51:00

for example. So this will be the response of second query. Similarly, there can be response

1:51:05

of other query, an another list, another list. Now everyone tell me, if you are giving

1:51:11

just one query inside the list of list, you will just have one element, right? So don't you think

1:51:17

everyone, from the results, from the results, just get the documents, it will give you list of list.

1:51:24

But because you know that, you have just given one query, can you just get the first element of the

1:51:29

list? So you will get the list of documents, that is, you will get this particular element.

1:51:33

you will get the list of documents for this query, top K documents for this query. Is that point

1:51:39

clear to all of you? Is that point clear to all of you? Now this is this is basic Python. This

1:51:46

is just simple list, dictionary, nothing else. Okay? Perfect. That's why everyone, revision

1:51:53

is very important. I have done this thing at least 20, 25 times. Still, I forget about it. So it means

1:51:59

it means that even if you're learning this for the very first time and you're implementing this for the first time, it's quite possible that

1:52:03

you might end up forgetting this. That does not mean you do not know about it. That means that you

1:52:08

forgot the syntax. You forgot the structure. It is completely okay. Feel free to Google about it.

1:52:14

Feel free to understand from the previous resources. It is okay. How can we give multiple queries? You can

1:52:20

give list of queries. How can you give multiple queries? So for example, if you like this part, right,

1:52:26

it expects a list of queries. Okay. So what is query embedding? If you see, it is a list.

1:52:32

Okay, inside that list, you might have one element, you might have 10 elements.

1:52:37

Right, Aditha? So let's open the, let's open our current project.

1:52:44

You know? So if you see, this is a list. So you can have, let's say, for example, you have multiple

1:52:48

queries. Query embedding 1. Query embedding 2. And so on. For now, you just have one query.

1:52:57

Take it. Now everyone, you will get list. So you will get the

1:53:02

results from the results, what I want is we would want to return the documents only, right?

1:53:09

For now, we are skipping the distances, meta, let's say, assume that we don't need it.

1:53:13

We just need the documents, right? So how can you do that? Results? Fetch the documents from the

1:53:19

results. Just give the 0th element. How many if you're 100% clear with this idea?

1:53:25

Results, documents, and 0. Okay?

1:53:32

Similarly, everyone, this is what I was trying to write. So you can fetch the documents like this.

1:53:37

Similarly, if you want to fetch the metadatas. Similarly, you can fetch the metadata of each document also.

1:53:43

Results, metadatas, meta-datas, meta-data's, meta-data's,

1:53:53

will you get the metadata like this?

1:53:57

Tell me, will you get the metadata like this? Yes, you will get it? But for now, you don't know.

1:54:02

need it. For now, we just need to return the list of documents. Okay, you just need to return

1:54:08

this. I hope everyone is crystal clear with this. Okay. Then everyone we are writing a prompt. We are

1:54:18

writing a prompt. Now, let's start building the prompt. So first of all, you are getting

1:54:27

the query. Then you are getting the retrieved documents that you are retrieving from the, the

1:54:32

the database. And then what we need to do everyone is we need to write the prompt. How we need to write

1:54:36

the prompt? Prompt is very big that I have already figured out. So what I'm going to do everyone is

1:54:41

I'm just going to copy-paste it instead of writing it from scratch. So let me paste it here.

1:54:53

Just look at the prompt. If you see prompt is you are a helpful, you are a helpful customer support agent

1:54:58

for an e-commerce company. Which kind of prompting takes?

1:55:02

technique we are using here. We are returning results, right? We are returning

1:55:13

documents. Pravi Teja, we are returning documents. How we are returning documents?

1:55:18

Inside the results, we have documents that is returning a list. From that we are returning the

1:55:25

we are getting the answer or the result of the first query, this query, right? So the, the

1:55:32

documents for first query will be present at 0th index. The documents for the second

1:55:36

query will be present at first index because list is 0 based indexing. So that's why we just

1:55:41

have one query. So answer will be present at 0th index. Get all the documents for all the queries

1:55:48

because you just have one query, get the documents related to 0th query. Or the 0th index.

1:55:55

We are using role-based prompting here and answer the customer's questions using

1:56:02

only, if you see only policy context provided below, right? So you are providing

1:56:08

the context and you are instructing LLM that, okay, if user is giving you a query, you have

1:56:14

to use only the policy retrieved policy documents to give the answer. So do not make up policy

1:56:23

details. Don't try to create, don't try to generate your own policy details because LLMs have

1:56:28

the capability of generating the data, but don't do that here.

1:56:32

If answer is not present in the context, you need to say this, right? Now everyone, if

1:56:36

user is asking something, now quite possible that that is, that information is not available

1:56:41

in your policy documents also. So you will have to simply deny that, okay, I do not have

1:56:46

that information. Keep the answer simple, clear, customer friendly, mention important

1:56:50

conditions or exceptions if they are present in the context. Is this prompt making sense to all

1:56:55

of you? Is this prompt making sense to all of you? But for that, everyone, we need to provide

1:57:01

the context also. That what is the context? Context is the retrieved documents that you

1:57:06

have fetched from the vector database. Is that point clear to all of you? Folks, yes or no? Okay? For that,

1:57:18

what you can do? Can you simply iterate over policy documents? So, for example, you are getting

1:57:27

the retrieved document, right? So you can go through each document for document for document.

1:57:31

in retrieved documents, right? You're getting in the retrieved documents and

1:57:39

in the context. Context, you can initialize here. And simply you can say that context.

1:57:49

Now, now guys, tell me, if you're adding all the documents, right? So you can simply keep on

1:57:58

appending it. Okay? So you can simply do that. Context.

1:58:01

plus equals to document. So you will keep on appending all the documents that you

1:58:06

have fetched, document one, document two, document three. But don't you think everyone, like,

1:58:11

there is no separation here. How the system will understand that, okay, this is document one,

1:58:15

this is document two, this is document three, correct or not? Right? So what can you do is,

1:58:26

what you can do is, so you can simply say like this, that okay, maybe you can

1:58:31

can also have some index, some index or or or, okay, what I'm trying to do is,

1:58:42

let's say length or number of documents, number of, you can have some delimiter also, but

1:58:54

better what I'm trying to do is, length of retrieved documents. So you can have range,

1:59:01

from 0 to length number of retrieved documents. Okay, from 0 to let's say there are three documents.

1:59:07

So you will go from 0 to 0 to 012. So you will simply say that for from, for index. Okay. So you'll say that document is equal to retrieved documents. It is a list.

1:59:31

a list. Yes? So give me the document at the 0th index, right? And you'll say

1:59:38

that context plus equals to, let's say this is policy document one.

2:0:01

and policy document 1. And then you will simply add the document here. Are you guys getting

2:0:13

this point? What I have done? I know. I've just added a delimiter. That this is policy document 1. And

2:0:19

after that everyone, you can add a new line so that all these policy documents you will add after each

2:0:25

line. Policy document 1, the text of that, then policy document 2, text of that, new line.

2:0:31

policy document 3. So these are the three documents that you have retrieved.

2:0:35

So can I said now, context will have all the information that you have retrieved from vector database.

2:0:41

Are you guys getting this point? Right? So you can add the context here and query as it is what you are

2:0:47

getting from the user. There is no change in the query. You are not even touching the query. And this

2:0:52

is the final prompt that you are returning from the returning. Returning prompt.

2:1:01

So this prompt you are building. Building prompt to the for the L-LM.

2:1:13

Folks tell me how many if you're getting this point, generate the answer. Have a look at it and tell

2:1:19

me. It might look like that we are writing a lot of code, but if you see it is not a lot of code.

2:1:25

Does the context structure matter? No, it does not matter. Ultimately, L-LM is smart enough, it will be able to see,

2:1:31

That's why a good LLM is required here.

2:1:33

Redshaw because it will be able to understand the context, that, okay, what you are providing in the context.

2:1:38

Because you are giving that, use the context.

2:1:40

So from that, LLM will be able to understand that, okay, user is providing three documents in the context,

2:1:45

policy document one, policy document two, policy document three.

2:1:51

Folks, are you guys getting this point?

2:1:54

Okay? And then everyone finally, we will write a function.

2:1:58

That will be, what is the number?

2:2:01

8, step number 8. Generate the final risk answer using the context. Okay, so what we can

2:2:13

do? Generate answer. To generate the answer, what do we need? Obviously, we need the query,

2:2:24

we need the query and we need the query and we need the chunks.

2:2:31

we need the chunks right everyone so first of all write the prompt we will call the function

2:2:39

directly to write the prompt build a prompt query and retrieve chunks retrieve documents

2:2:49

correct everyone now can we said give this prompt now if you see what is the logic here

2:2:56

see the logic you are trying to build the prompt you will call the function building the prompt

2:3:00

inside building the prompt, you are passing the retrieved documents.

2:3:05

Using this retrieved documents, you are creating a prompt that you will pass to the LLM, right?

2:3:10

Correct table. Now, call the LLM with the prompt.

2:3:13

To call the LLM, we have the open AI client. So we can say that response equals to openAI client.

2:3:21

client dot, client.Responses. Create. So you will write the model here, which model we are going to use.

2:3:29

the LLM model, right? And the query and the prompt. Okay. So you can say that.

2:3:35

The input prompt. Input is prompt. Is that point clear to all of you?

2:3:44

Make sense. And finally everyone, you will return response. Dot output text. What response

2:3:51

you are getting. Is that point clear to all of you? Now the only thing that we need to make sure is to get this

2:3:58

retrieved documents by calling the function.

2:4:03

Folks, yes or no?

2:4:06

Right? Now finally, everyone, the final flow, get the answer? The 9th step or

2:4:17

or resolve the user query with rag. So let's say we have a function defined

2:4:32

answer with rag.

2:4:38

Because I will show you answer without rag also. Right. So we will have a query.

2:4:47

Okay, query, string. Then we can also pass collection that we would need. And we would

2:4:54

need the top K element that how many elements do we need? Top K, it is going to be an integer and

2:4:59

the default value can be three. Okay? So first of all, everyone, if you want to answer with

2:5:06

rag, what do you need to do? Can is that, first of all, retrieve the chunks, retrieve the documents,

2:5:14

retrieved documents? For that, do you have a separate function to call? To retrieve

2:5:22

the documents? Yes, retrieve policy content. See? Retrieve policy content. Pass the query,

2:5:32

collection, and top K. Once you have retrieved the documents, what you can do? You can just get the answer.

2:5:44

or final result is equal to a final answer is equal to generate answer, correct?

2:5:58

Generate answer, pass the query, pass the query and retrieve documents. How many if you're getting this point? And you can return the answer.

2:6:07

Okay. So what you're doing in generating answer, you are building the prompt, calling the

2:6:15

LLM, generating the answer, everyone clear to this point of time now? As of now? The only thing that

2:6:23

that is missing here is what? The only thing that we have not done as of now is we have not stored these

2:6:34

documents right as of now. Correct? Calling the setup, we have not set up,

2:6:41

so we have not called this function, right? We have just implemented the function. Create embeddings,

2:6:46

set up vector database. So what we can finally do everyone is we can write a main function, right? So that

2:6:53

we can directly use, define a main function in which first of all, we will set up the vector database.

2:6:58

Correct everyone, we will set up the vector database. And apart from setting up the vector database, and apart from

2:7:03

setting up the vector database, we will have to store the data, we will have to, what do you say?

2:7:08

All these policy documents, right? Don't you think we need to store these policy documents

2:7:13

into the database, correct or not? We need to store these policy documents into the database.

2:7:21

For that, what we can do? What was the function? Absert function, right? Okay, so we have these

2:7:30

policy documents. So either we can write the code here or we can write a separate function

2:7:36

for that. Retrieve policy content, set of vector database. Yeah. So let's say everyone we have

2:7:42

defined store, store documents in vector dv. Correct. Correct.

2:8:00

For this, you need to pass the documents here. And what could be the type of documents?

2:8:05

If you see the type of documents is nothing but list of dictionary.

2:8:10

Correct, everyone? Even if you don't pass the type, it is okay. Right? We will call the absurd function.

2:8:16

Now for this, everyone, we will get all of these IDs, first of all the documents. So you see that, we have for each policy document in policy documents.

2:8:30

iterate over it and we can simply say that we have the IDs array, empty array. Again,

2:8:38

a simple Python code, IDs dot append, and policy document or this document. So we will get

2:8:50

each document and document may say get the ID. Then we will get the text. Then we will get the metadata.

2:8:55

Although we don't need this kind of information a lot, but document.

2:9:00

get the ID. Are you guys getting this point? So this is how we can get the ID. So if you don't

2:9:06

want to write these three lines of code, you can simply do like this. Idies is equal to what?

2:9:11

Write a list and doc ID. Document. Document may say ID. For each document.

2:9:30

documents. Are you guys getting this point? We can get the IDs like this. Similarly,

2:9:41

we can get the text like this. We won't only text. We don't want ID for now. We don't want any

2:9:46

other metadata. We are just writing a very simple code here. Text. Similarly, we can fetch the metadata

2:9:54

is here. We don't want it for now, but I'm just letting you know in case we want to do some modifications here.

2:10:00

get the metadata data like this. So once we have all of these things, right? Ultimately, we are not

2:10:05

doing anything, getting the ID, getting the text, getting the metadata, right? So guys, in future,

2:10:11

if you want to use for filtering purpose, you can use metadata. Remember that? In the vector search

2:10:18

class, I showed you that you can use metadata for filtering. Okay? So you can create the embeddings

2:10:25

now. Embedings made. So should I create the embedding of IDs or text or metadata?

2:10:30

us. For what, we should create the IDs. Can we do these in set up vector database

2:10:38

functions? If you see, it's a separate thing. First, we are just creating the vector database

2:10:42

and this step, we are storing the documents inside vector database. If you want, you can do that.

2:10:46

There is no hard and fast rule as such, but if you see, these are two different things. First,

2:10:51

we are creating the database, then inserting the data inside the database. So in this function,

2:10:55

we are actually storing the data. So that's why I have separated it out.

2:10:58

You know? So guys, now we need to create embeddings. We should create embeddings of text or IDs or

2:11:06

metadata. Of what? Only text, right? Folks, yes or no. And finally, we will store these embeddings

2:11:17

into database like this collection. We have the collection and how do we get the collection here?

2:11:28

the collection here. Okay. And collection dot absurd. Okay. Remember absurd, update,

2:11:38

plus insert. We can pass IDs. We can pass metadatas. We can pass metadatas. We can pass

2:11:49

documents, that's it. Documents or text, let's call it as documents only, better

2:12:00

name. Anyone has any doubt? And obviously, their corresponding embeddings, that's it. This is how we

2:12:12

can store the data inside the vector database. Is that point clear to all of you? So in fact,

2:12:17

everyone, let me change the steps here. One, one, two, three. Four is creating the embeddings.

2:12:22

Fifth is setting up the vector database. And then sixth step is, six step is store documents inside

2:12:32

in vector DB. Okay? Then we have step number seven, step number seven, eight, nine, and

2:12:47

Okay?

2:12:48

I think a very long process everyone, right?

2:12:52

I hope everyone is clear till this point of time.

2:12:55

Right? And in the main function, everyone, first we will set up the vector database.

2:12:59

After setting up the vector database, what we're going to do?

2:13:02

After setting up the vector database, what are we going to do?

2:13:05

After setting up the vector database, what are we going to do?

2:13:17

After setting up the vector database, we should create a collection.

2:13:27

Okay, it should, okay, setting up a vector database, it is returning the collection, right?

2:13:34

Okay, got it. I got confused. So it is returning the collection. Why we are not storing that collection?

2:13:39

Then after setting up, we should store the data inside the vector database.

2:13:44

For that, we will call the store function.

2:13:47

store documents in vector database. For that, we need to pass the collection. We need to pass the documents.

2:13:53

Okay, we need to pass the policy documents. In fact, policy documents.

2:13:57

Okay, policy documents, they are nothing but what do you say?

2:14:02

Guys, one thing, I made a small, we can make a change here.

2:14:07

Do you really need to pass these policy documents here?

2:14:10

Tell me. No, right? It is a, it is a global variable. Can't we directly use like this? Getting the point.

2:14:16

Getting the point. We can directly use like this, right? Why we need to even pass it?

2:14:20

It makes sense because they are defined globally. We don't even need to pass that.

2:14:26

Okay? We can make this better change and we can just pass collection.

2:14:31

How many of you are clear with this? So, till this point of time, we have created the database and stored the vector data,

2:14:37

stored the documents inside vector database. Then everyone, it means that our pre-processing is ready, correct?

2:14:45

Pre-processing is ready. Our database is ready. Now we will get a sample query from the user. Let's say sample or let's say user query.

2:14:54

User query is let's say, when will I get my refund?

2:15:01

Okay? When will I get my refund for? Yeah, that's it. When will I get my refund?

2:15:09

Is that point clear to all of you? This is the user query.

2:15:13

Folks, yes or no?

2:15:16

And everyone, we can simply get the answer by doing what?

2:15:19

By calling answer with Rack.

2:15:22

Answer with Rack.

2:15:23

What do we need to do?

2:15:25

Simple.

2:15:26

Pass the user query, pass the collection, pass the top K value.

2:15:31

And even if you don't provide it, it is okay because you are just giving the default value 3.

2:15:36

Is that point clear to all of you?

2:15:37

That's it.

2:15:38

And finally you can print the answer.

2:15:41

Okay?

2:15:42

You can say that.

2:15:43

Answer with Rag is this.

2:15:53

Is that point clear to all of you?

2:15:55

This is answer with Rack.

2:15:59

Folks.

2:16:00

Now everyone, for your better understanding, I'm doing one more thing.

2:16:04

I am writing one more function here.

2:16:07

Define answer without Rack.

2:16:12

So that you can compare, right?

2:16:14

That with Rack, what answer you are getting?

2:16:16

Without Rack, what answer you are getting?

2:16:19

What we should do in answer without Rack?

2:16:21

Can you tell me?

2:16:24

What we should do in answer without Rack?

2:16:26

You will get the query?

2:16:31

Just call LLM, right?

2:16:33

Call LLM to get the answer?

2:16:35

Absolutely.

2:16:38

Just call the LLM, don't pass the collection.

2:16:40

Don't perform similarity search.

2:16:42

Correct?

2:16:43

So simply what do?

2:16:44

Response is equal to OpenAI Client.

2:16:47

.oponA client, dot responses, dot create, dot create.

2:16:53

And what we need to do?

2:16:54

Pass the model, LLM model, then prompt or would you say the input?

2:17:02

What is the input?

2:17:05

Can you pass the input query as it is to the user, to the LLM?

2:17:08

That this is the query, and finally return the response.

2:17:12

Return response dot output text.

2:17:17

Are you guys getting this point?

2:17:20

So what you can do everyone?

2:17:22

Answer with Rag.

2:17:23

First, try to find out, okay?

2:17:26

Answer with.

2:17:27

Only user quid.

2:17:42

Now you can compare that what kind of answer you are getting with or without Rack.

2:17:56

Is that point clear to all of you?

2:17:59

Folks, yes or no?

2:18:04

Okay.

2:18:09

And now everyone, because we are just, we are just.

2:18:11

We are just, we have just written this code live.

2:18:14

Definitely there might be some small, small errors.

2:18:17

Would you want to try this on your own once, this code, and try to run on your own?

2:18:22

You just have to do Python 3, run this file, ecommerce rag.t.p.

2:18:26

Will you try that?

2:18:28

In the second, we need to update the answer variable.

2:18:30

Thank you.

2:18:31

These kind of errors will be there.

2:18:33

Okay, these kind of typos or some syntax errors can be there.

2:18:37

Okay, what about the API key?

2:18:39

For that, you'll have to create your own.

2:18:40

Okay?

2:18:41

Guys, what you can do is you can create an open AI account.

2:18:45

Just put maybe $1, $100, just put $1.00, it is okay.

2:18:49

Or if you don't want to do that, you can use the sentence transformers, right?

2:18:53

Remember that?

2:18:54

the sentence transformers API that I showed you in the last class.

2:18:57

You can do that also, right?

2:18:58

Or you can use some open source, LLM like Olama, like from Olam, you can use that, anyone

2:19:03

of them.

2:19:04

Now it is your homework to try this code.

2:19:08

I think, okay, the minimum is $5, so you'll have to add this.

2:19:10

minimum $5. Don't have to use OpenA, it is okay.

2:19:13

You can use the sentence transformer API that we seen in the last class.

2:19:18

Now guys, it is your homework now to try to run this code.

2:19:23

Mostly it will be running, there might be small changes here and there, some small typos,

2:19:28

some syntax errors can be there in this code.

2:19:31

But mostly it will run as it is.

2:19:34

How many if you are clear with the entire flow?

2:19:36

I would just need your five more minutes, then we will end the class.

2:19:40

Everyone clear with the entire flow of the application.

2:19:43

Flow is more important.

2:19:44

Even if you give this code to Claude to GPT, if there is any error, it will, and you can figure

2:19:50

it out, like what is a mistake?

2:19:52

But flow is more important, right?

2:19:55

Flow is very clear, very good.

2:19:56

Now everyone, one last thing for today's class.

2:19:59

We can experiment one more thing about top K.

2:20:04

What do you think?

2:20:05

The value of top K, should it be very less like one?

2:20:09

Should it be medium value?

2:20:10

value like 3, 4, 5, or should it be very high, like 10, 20, 30?

2:20:14

What do you think about it?

2:20:17

Ideally, it should be very less, it should be moderate, or it should be very high.

2:20:21

What do you think about it?

2:20:22

And first of all, are you able to visualize that obviously yes, that with the change in the top

2:20:28

K value, the type of output that you are getting will obviously change.

2:20:34

Understand this point?

2:20:38

Right.

2:20:39

Guys, if you're giving top K value.

2:20:40

value is equal to 1. What does that mean that you are generating or you are getting the exact

2:20:45

answer, the best match, the most similar answer? Correct? If you give top K value is equal to

2:20:51

one, it means that you are just trying to find out only one, the nearest, the most nearest, the most

2:20:56

similar chunk or the most similar document. If you give top 5, you are matching, you are getting top

2:21:02

five chunks. If you give top only one, if you give the K value to be very less, don't you think

2:21:09

one you might end up missing the context because you are just relying on one answer one answer

2:21:16

that might be the most similar but that might not have all the information right based on the

2:21:22

user query it is the most similar but it might not have all the information getting the point

2:21:28

correct for example if you come to your query uh if you give me your query if you're asking some

2:21:33

question now i know the best answer for your question so let's say masai allots me that particular

2:21:39

class or that particular query. I give you that answer. But does it mean that I will be having

2:21:44

all the information about that topic? Not really. Because Masai thinks that I know I will be the

2:21:50

best person to answer that query. But quite possible that before answering the query, if we refer three

2:21:55

different people, then we will be able to give better context to the answer. Similarly, if you give the

2:22:01

top K value to be very high, then you will have a lot of noise also. Correct? Then it might add a lot of noise.

2:22:08

So generally everyone that's why you keep the K value to be a bit moderate. Now what is the

2:22:13

meaning of moderate? Around 3, around 4. Not very high, not very less. Does that make

2:22:18

sense for all of you? Should it depend on the size of DB like 10% of the chunks? It can also

2:22:24

depend, absolutely correct. Now generally let's say for example if you have 1,000 documents. Now out of

2:22:29

1,000 documents, 1% could be good enough. Right? You will retrieve top 1% documents. Let's say 10 documents.

2:22:35

Fine. Make sense?

2:22:38

So generally what you do is you experiment with the top K value.

2:22:43

Okay?

2:22:44

Let's say you have, let's say Open AI is using this model.

2:22:48

They have 1 billion users, 100 croix users in the world, for example.

2:22:52

What they can do is for few people, they can experiment with the top K values equal to 3.

2:22:57

Then they can ask the feedback.

2:22:58

This is what chat GPT also does, right?

2:23:01

It gives you two answers.

2:23:02

They need to ask your feedback. Which one is better?

2:23:05

Which one is more relevant for you?

2:23:07

Based on that.

2:23:08

they come up with the, based on these experimentations, they decide what is working best for what kind of users?

2:23:15

Okay, everyone? For different users also, for different kind of users also, the type of retrieval policy

2:23:24

can change. What type of documents, what kind of data works best for what kind of users? Does that

2:23:30

make sense to all of you? Okay, that's it for today's class everyone. I'm going to

2:23:38

upload this code on GitHub. Please stay with the class just for two more minutes.

2:23:45

I will create a new repository.

2:23:52

So let's say this is e-commerce.

2:24:08

Thank you.

2:24:38

Okay. Just one second, Ravi. So I think yes. Because Monday go, we did not have the class. So we will have class on Wednesday, that is today. And we will have class on Friday. Is that okay with all of you? So instead of Monday Wednesday, only for this week, we will have class on Wednesday and Friday. Is that okay with all of you? So instead of Monday, Wednesday, Wednesday, only for this week, we will have class on Wednesday and Friday. So team will also let you know,

2:25:08

I will ask the team, they will update you. And we will have the next class on Friday. From next week onwards, we will have the regular schedule, only Monday, Wednesday. Okay?

2:25:16

Okay. So let me also do this one thing, upload the notes as well.

2:25:23

Tomorrow what? What are you saying tomorrow? So you are saying that we should have the class tomorrow? No, no, no. We should not leave the schedule. We will stick to the schedule because our batch is also like Monday, Wednesday, Friday, right?

2:25:38

Tutorial is planned for tomorrow.

2:25:47

Okay, fine. Let me upload the notes as well.

2:26:08

So guys, I have uploaded the notes. So these are the notes for today's class.

2:26:29

Masai team will plan that, so all the topics they will plan. Don't worry.

2:26:38

the same thing. Nitish, what you can expect is you can expect a communication from the team

2:26:42

by tomorrow. I will talk to the team by tomorrow morning and they will update you. Okay, old

2:26:48

repository, which old repository? All the notes are present here in this repository, right? If you go

2:26:54

to agentic design batch, all the notes are present here for all the classes. Okay? And if you're talking

2:27:00

about the repository for vector search, that will be present here. Okay, this is the code for

2:27:08

vector search that we were referring into this class. Okay. So guys, all of you

2:27:14

enjoyed the class. All of you understood the session. So sorry for taking 20 more minutes from

2:27:20

your time. Okay. But I hope you all enjoyed the class. So now I'm launching the feedback poll. Please

2:27:25

take the feedback pool and feel free to drop off. I'm not taking the quiz today because we are already

2:27:30

late. We will include the questions in the next class. Okay. And the poll is in front of you. Please take

2:27:38

the pool and we can drop off now. Take the pool and feel free to leave it, leave the class.

2:27:43

Thank you everyone. Have a good day. Take care and bye bye. There are different, different

2:27:51

repositories now. There is not a single repository. For different projects, there are different

2:27:54

repositories. You can refer this. All the repositories are present on my GitHub link. So on this account.

2:28:08

So folks, please take the feedback pool and we can end the class then.

2:28:16

Thank you so much, sir. Thank you everyone for joining.

2:28:24

Hope you had a wonderful session. We'll meet tomorrow to resolve your doubts on whatever we'll have learned last week.

2:28:34

So I'll suggest you to attend the

