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

Thank you

5:20

Thank you.

5:50

Thank you.

6:20

Thank you.

6:50

Thank you.

7:20

Thank you.

7:50

Thank you.

8:20

Thank you.

8:50

Thank you.

9:20

Thank you

9:50

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

Thank you

10:38

Thank you

10:40

Thank you.

11:10

Thank you.

11:40

Thank you.

12:10

Hi everyone, very good morning, very good evening everyone.

12:23

Folks, am I audible to all of you?

12:28

Hi everyone, am I audible?

12:31

Okay, great.

12:32

So I think people are still joining in and a few people are asking for the Zoom link.

12:37

Okay, so Somiya has shared the Zoom.

12:39

has shared the Zoom link in the chat.

12:40

So please feel free to join.

12:42

And we'll start in maybe a few minutes.

12:45

Let's wait for more people to join.

12:46

People are still waiting for the link.

12:49

We'll start maybe in five minutes.

13:09

Thank you.

13:39

Thank you.

14:09

Thank you.

14:39

Thank you.

15:09

Thank you.

15:39

Thank you

16:09

Thank you

16:39

Thank you

17:09

Thank you

17:39

Thank you

18:09

Thank you

18:39

Thank you

19:09

Hi,

19:16

good evening,

19:17

and welcome,

19:18

can all of you

19:19

can all of you hear me and

19:21

see my screen

19:22

and see my screen

19:23

with my screen visible to all of you

19:26

Okay, great.

19:28

So guys, as you can see on the screen

19:30

today's

19:31

today's topic is going to be the RAG application.

19:33

Okay, so if you remember, we have already discussed

19:35

about RAG in the last module, right?

19:38

module, right?

19:39

Correct?

19:40

We had some discussion on RAG.

19:41

In fact, I think we built a simple RAG application also.

19:46

But today everyone, we are going to build the RAG application with the help of a framework.

19:50

Earlier we kind of built all of the RAG application via manual way.

19:55

But today we will see that the Lanchain way of implementing RAG application.

19:59

Makes sense, everyone?

20:01

Okay.

20:02

So we will implement RAG application using LangChain.

20:06

Okay, now, if you remember everyone, everyone, what is RAG application?

20:29

First of all, you tell me, let's say if you're building a simple board application.

20:36

If you're building a simple, maybe a chatbot for Swiggy, Zomatto, e-commerce, Amazon FlipCard, right?

20:42

So if you have a non-Rag-based application, it means that you have a simple LM-based application.

20:47

So there is an LLM which will answer your queries, right?

20:49

which will answer users' queries.

20:51

But LLMs are generally trained on public data, right?

20:55

So LLMs may not have the context of your company's internal policies, companies' internal data.

21:00

Correct, everyone?

21:01

LMs may not have their company's, like your company's internal data.

21:05

Now, if you're not your company's internal data.

21:06

you're building such a customer support agent, customer support chatbot, with only LLM,

21:12

then it will be able to answer general queries.

21:14

But it will not be able to answer the queries based on company's internal policies data.

21:19

Because that data has not been fed inside LM.

21:23

LLM is not aware of that.

21:24

Now the point comes in that can we give that data to LLM?

21:28

Now, we can do that.

21:29

We can do fine tuning, etc.

21:31

But in fine tuning or we'll come to that point also.

21:34

But everyone, if you're using some LLM like,

21:36

like Open AI, et cetera, you cannot feed data inside them, correct or not?

21:40

Because that data, that training process is a very, very big process, right?

21:44

So if you think about, let's say, you can train LLM, right?

21:48

You can train Open AI.

21:49

It is not possible for a company, in fact, an entire company to train an AI model like Open AI, right?

21:55

Because they are such a big models, right?

21:57

It will take months and months of time and millions of dollars of money to train those models, right?

22:02

A lot of resources are required.

22:03

Right.

22:03

So that's why training data is not possible.

22:06

And fine-tuning, you can say that.

22:07

Fine-tuning, we do only with small amount of data and just the behavior change.

22:12

In fine-tuning, we don't feed any data inside LLM.

22:15

Makes sense, everyone?

22:16

Then here comes the concept of Rack.

22:18

When you want your LLM to have the excess of, when you want your LLM to have the excess of your

22:24

internal company's data, policy's data, with the help of an external database.

22:28

So basically, you connect an external database with your chatbot, with your LLM,

22:33

and your LLM can access that external data.

22:36

database, like a vector database, whenever it requires to answer a query, which is based

22:41

on some internal policies information, based, it can identify, because LLMs have power of

22:46

reasoning, LLMs can identify who, like for this particular query, do they need to access vector

22:51

database or do they don't need?

22:54

If they don't need to access the vector database, they can directly answer the query from their

22:58

own understanding, right?

23:00

But if they need to access the internal company's data, right, they will go to vector database,

23:05

get the data from there, retrieve, right?

23:08

Retrieve the required information.

23:10

For example, if you're asking any question about maybe refund, return, shipping, cancellation,

23:15

etc.

23:16

You have already fed those data inside the vector database and you have stored them in form of

23:22

embeddings.

23:23

We'll talk about that.

23:24

Now, your LLM can make a call to the vector database, get the required policy information,

23:31

and retrieve the proper information, and then create a user-friendly answer.

23:35

We don't retrieve, we don't return the data as it is what we have retrieved, right?

23:40

We try to return the answer in a user-friendly way.

23:43

This is what RAG is, right?

23:45

LLMs are very powerful, right?

23:48

LLMs are very powerful, but LLMs have mainly two limitations, right?

23:51

First of all, what is Rag, everyone?

23:56

It stands for retrieval,

24:05

generation, retrieval, augmented generation.

24:09

Now, there are two main things that we need to understand here, the concept of retrieval,

24:13

that will retrieve the information, and we generate the answer based on the retrieved information.

24:17

So, these two are the main components.

24:20

Apart from that, there are other components also, that before retrieving, you will have to load the documents,

24:24

you will have to store the documents, you might have to split the document into multiple chunks,

24:28

right? And all these things we'll talk about that.

24:30

But once you load the documents, once you store the documents, then you retrieve the documents,

24:35

information and generate the correct answer basis on that.

24:38

Generate the user-friendly answer basis on that.

24:40

Now, LLMs are very powerful.

24:42

Do we all agree with this?

24:44

That LLMs are very powerful.

24:50

But mainly there are two limitations of that.

24:53

I do have a question for Rack with our previous Rack pipeline, we chunk embed and save into vector database

24:58

for the PDF file, but how do we process for audio and video kind of file?

25:01

See, audios and videos, if they are very big enough, then they can also be down,

25:05

they can also be stored in the form of chunks.

25:08

Okay?

25:08

In fact, for example, let's say how Netflix, how a company like Netflix or YouTube stores big videos,

25:16

do you think that if let's say there is a movie on Netflix, right, with that movie is of, let's say,

25:20

four hours of duration, in fact, one hour of duration, do you think that that one hour of movie

25:24

is stored inside Netflix in one, as a one unit?

25:28

Do you think so?

25:32

Answer is no, right?

25:33

answer is no because one hour of movies storing itself is a big trouble and now everyone

25:38

assume that a very simple idea that if you open Netflix right and if you click on that one movie

25:43

generally that movies those movies are very of very high quality when you click on the movie

25:48

it means that if that complete movie is stored as one unit right without any chunkification

25:53

then entire movie will be fetched in your mobile application now tell me everyone is that

25:58

like is that feasible that if I don't have very good internet connection and

26:03

most of the times, all seven, what do we do?

26:05

We click on the movie.

26:06

We watch first few minutes of the movie and if we don't like it, we don't watch further.

26:11

Correct?

26:12

Then if there are not, like there are chances that the person might not even watch the entire movie,

26:16

then why should we fetch the complete movie?

26:19

So that's why everyone there is a process of chunkification that goes internally.

26:22

Right?

26:22

So the movie gets divided into small, small chunks.

26:25

The basic idea could be, let's say one minute of each chunk.

26:28

Night, so internally Netflix also stores that data in the form of chunks.

26:32

And when you click on the movie,

26:33

the first chunk gets downloaded, then the second chunk gets fetched, then the third chunk,

26:38

then the fourth chunk, and so on.

26:40

So that you are constantly fetching the data.

26:42

You are not over-fetching the data that might not be required even.

26:46

If let's say your mobile device, fetches the complete one hour of or two-hour of, three-hour-off

26:51

movie in one-go.

26:53

First of all, it will be taking a lot of time because you are fetching such a big file over the

26:57

internet and it might not be required also.

26:59

So that's why at every place, whenever you have big files, that is always.

27:03

that always goes via chunkification, okay?

27:07

Whatever kind of system you think of, okay?

27:09

YouTube, Instagram, right, Netflix, Amazon Prime, in fact, rag-based systems also.

27:16

Okay?

27:17

Yeah.

27:18

So LLMs are very powerful.

27:21

Right?

27:22

But mainly there are two limitations.

27:33

or one limitation that we are not interested today, right, that we are not concerned about

27:45

today, which is the context window, correct?

27:48

Let's say, but there is, you can say that, there is one limitation.

27:52

Context window limitation that we are not, let's say that is a different topic altogether,

27:56

that rag does not solve the process of, or rag does not, I would say, in some way you can say that

28:03

rag also solves the way of, what do you say? What do you say? Limited to context window

28:10

also. But Rag is not a direct solution to context window. Correct, everyone? All of you remember,

28:15

what is context window? All of you remember, what is context window in LLN? How much amount of data

28:20

LLM can process in one request at a time. That is what is called as context window. So that is a different

28:25

problem statement. But the main limitation that LLMs have, that they have finite and they have

28:32

static knowledge source. They have static pre-trained information. That does not change

28:41

again and again. So for example, whatever, let's say whatever has happened in the world today,

28:48

LLMs are not aware of that. Does not matter how powerful it is. It might know everything in the

28:52

world, what has happened in the past. But it will not know what is going to happen, what is happening

28:56

today because they have static pre-trained knowledge. And that pre-trained knowledge is not

29:05

very easy to change every day. You cannot say that I will keep on training my model every day. Because

29:09

training a model itself is a very big process. Because you have to deal with trillions of bytes of data,

29:14

trillions of jibs of data. Makes sense, everyone? And that's why everyone, rag comes into picture.

29:19

When you want to get some company's policies data, that can change also. Correct. Also everyone?

29:26

Right? So policy.

29:26

can change more, maybe every day also. Some new policies can be added. Existing policies

29:31

can be removed. Existing policies can be updated and whatnot. Now, this data is not present

29:35

inside the Rack. Because Rag has, this information is not present inside the LLM. Because LLMs have

29:41

been trained on some static data. And these policies data, kind of a dynamic data, that can change

29:47

every day. That can change over the period of time. That's for everyone, RAC comes into the picture.

29:52

So what happens everyone, right? So Rag may, what you do is with LLLM.

29:56

Let's say this is your LLM powered application. So when the user asks, generally what happens?

30:01

A simple Rag application, a simple LLM powered application, you give a query to LLM and LLM gives you the answer.

30:08

Simple. But because we want to give external data source as well, you add a vector database here.

30:15

Now vector databases are the special type of databases which are meant to store embeddings.

30:21

Correct, everyone? Which are meant to store data in the form of embeddings. And why do we convert the data in the form of embeddings? And why do we convert the data in the form of embeddings?

30:26

everyone? Why do we convert the data in the form of embeddings? Why can't we store the data as it is? Why can't we store

30:33

the file as it is? Semantic search? Absolutely correct. Because semantic or similarity search. Because in

30:40

LLM powerbed applications, in any AI powered application, we don't rely on static or we don't rely on keyword

30:48

base search. We don't say that. That this is the exact word, search equals to equals to. No, that does not happen.

30:54

What happens in the LLM powered applications or chatbot?

30:56

it works on semantic search. It means that it tries to find the similar kind of meanings.

31:04

It tries to find the similar kind of meanings for the given query. Does that make sense to all of you?

31:09

And to perform similar kind of, to perform semantic search, to perform similarity search, you need to

31:15

store the data in the form of embeddings. So here everyone, you store the data in the form of embeddings.

31:22

So whenever the query comes in everyone, for example, let's say if you ask a query, let's say,

31:26

maybe if you ask the query, tell me something about Virad Koli. If you say that,

31:33

tell me something about Virad Koli. Does LLM needs to make a call to vector database for that? For

31:38

this kind of query? If you are asking, giving some data to LLM and asking that LLM to summarize this

31:45

document, summarize this data. For this kind of query, does LLM needs a vector database search? Does LLM

31:51

needs to perform a semantic search? Not really, right? When you are asking specifically about

31:56

return policy, refund policy, cancellation policy, then LLM makes a call.

32:02

Guys, I'm using the word LLM makes a call, but it's not the LLM who makes the call. It's the agent

32:07

who makes the call. So basically, our application makes a call to database, vector database,

32:12

performs similarity search using the embeddings, gets the desired information, and this information,

32:19

this policy data will be given to LLM, and LLM will use this information to create the final answer.

32:26

that we can return to the user in a user-friendly way. Is that point clear to all of you?

32:31

And then finally we return the answer back to the user. This is what the entire flow that we are

32:36

going to implement today. Right? Everyone clear? Is everyone clear? Okay. Now one more thing,

32:44

everyone, one small, different type of question. Can we do, can we perform or can we make our LLM

32:53

fine tune also along with having RAG application. Can we do fine tuning also along with

33:00

having vector database as well? If yes, tell me the use case. That if we can do that, if we can do that,

33:06

then what could be the use case for this? Yes, we can do that. Yes, we can do that.

33:15

Guys, fine tuning is just a small piece of information that you give to LM, some examples that you give

33:21

to LLM that what kind of answers you need to present. How do you need to present the answer?

33:26

So basically, it just represents how your company treats their customers, right? How, what kind

33:31

of tone you should have while giving the answers, right? And even if you don't need fine tuning all

33:36

the time, you can give, you can do that via prompt also, correct? If you can give some instructions

33:40

inside the prompt, then also it is okay. Then fine tuning may not be required at most of the cases.

33:46

Make sense?

33:46

No, Nisag, nisarg, fine-tuning is not a replacement of rag. Fine-tuning is not a replacement of rag.

33:57

Rag is still there. Because in, like, this data can be of, let's say, 100 gb-t. You can have very big amount of

34:02

data in Rack database, in vector database. That amount of data you cannot do with fine-tuning.

34:07

Fine-tuning itself is very costly process. Okay? So you cannot fine-tune a data, you cannot fine-tune an

34:13

an LLM on the entire vector database. If we have our own harness specific for a niche business,

34:20

then a journal LLM does not have, does not have like maybe an agent for Nuclifier. Absolutely correct.

34:25

Training on domain terminology to understand absolutely correct. Very good, very good.

34:28

Now, I hope everyone is clear. Now let me write down the typical rag flow. Then we will discuss different

34:33

components and then we are going to implement all of these components one after another.

34:37

So first, everyone, the user query comes in.

34:43

So there is a user query. This user query, we give to the retrievers, you can say that,

34:50

domain, retriever component. This user query, we give to retriever. Now this retriever can decide that

34:57

should this, like now inside retriever everyone, obviously you will have LLM as well. This retriever can

35:02

decide that do I need to make an LLM call or do I not need to make an LLM call? If LLM call is, let's

35:09

say, if we need to make a call to Rack, then it will make a call to Rack. That's a call.

35:13

is the vector database, get the data. So what retriever generally does? Retriever searches relevant

35:19

documents. Searches. Searches. Searches relevant documents. And then everyone, from this

35:38

relevant documents, what we do? We fetch relevant chunks. And these relevant chunks, we pass

35:43

to the LLM to generate the user-friendly answer, right? So what we do? Relevant

35:49

chunks are given to the LLM.

36:13

to generate the final answer. Is that point clear to all of you? Is that concrete

36:21

all of you? This is what we do, right? These are different components that we have. Okay, now

36:30

let's see different concepts or different terms that we are going to implement, different components

36:34

that we are going to implement. The first component, everyone, that we are going to implement is something

36:38

called us document loader.

36:43

This is called as document loader. Any guesses, what could be the task of document loader?

36:56

So document loader, as the name suggests, it loads the external data. So you might be having the data

37:01

in the form of text file, in the form of PDF file, in the form of some other format also. This document

37:08

loader just loads the data in the form of Langchain document objects. So LankChain document objects. So

37:13

chains supports something called as document objects. That makes easier to retrieve the data.

37:19

Chunking and indexing will also come shant through, but that will come later. First, you load the documents.

37:23

Then you chunkify the documents. Okay? So document loader, what it does? It reads the external data.

37:43

Read the external data and converts it into

38:13

Is that point clear to all of you?

38:18

Okay?

38:19

We will see this in implementation also everyone.

38:21

This is how you basically do that.

38:23

So let's say you create a document object.

38:25

Okay.

38:26

Inside this document object, you basically pass the content, page content.

38:31

What content you want to store inside this document, page content.

38:36

So here you pass the text basically.

38:39

And then everyone you can pass some metadata also.

38:41

Do you remember in that, in those,

38:43

rack classes. We discuss about metadata. We discuss about metadata. For example, when this document

38:51

was created, when this document was last updated, the name of the document, etc., etc.

38:55

Right? That metadata can just help you to filter out some extra, extra things. Okay? Is the document

39:01

loader clear to all of you? The first component, everyone? The first component is clear to all of you?

39:06

Okay. The second component, everyone, that comes into picture is text splitter.

39:13

I think this is self-explanatory as well. Text splitter. What does this, does everyone? Text splitter?

39:21

That it divides the document into chunks. Why can't we have the entire document? Because everyone, entire document, the bigger, if the documents are very big, then it is very, very, very difficult to, it is very, very difficult to process. It is very, very, very difficult to retrieve the relevant information from bigger documents. That's why we chunk or we split the document into smaller chunks.

39:43

Right? It is difficult.

39:45

It is difficult.

40:13

It is difficult to retrieve the data from bigger documents. It increases the latency. It increases the time.

40:19

It increases the processing power and so on. Right? So, that's why.

40:43

into smaller chunks. Is that point clear to all of you?

40:51

Into smaller chunks. Correct? So now everyone, Lanchain gives you a class. Lanchine gives you this

40:59

functionality automatically. You don't have to do that. If you remember in one of the classes,

41:02

we wrote the for loop, right? But from first word to let's say 500 word, this is the first chunk.

41:08

From 5001 to 1,000, this is the second chunk. Remember that? We did it manual.

41:13

correct or not? So you can define any way of chunkification of data. It can be static

41:19

chunking, fixed size chunking, cementic chunking and whatnot. But Lanchine gives you a class which is called

41:26

as, which is the name of the class is recursive, character, text, split up. The name is slightly bigger.

41:33

Recursive.

41:43

text splitter. So this is the class, everyone, which Lanschain gives us. Now, take it as an assignment, read about it. Okay? And tell me in the next class, what retrieval, what chunky, chunking logic does it use internally? Make sense? I can tell you right away, but make some effort. Spend five minutes of time, 10 minutes of time. Google about it, read about it. Okay? It is a default.

42:13

way of splitting the data into multiple chunks. Okay? And it automatically takes care of chunk

42:19

size, etc. Right? Now everyone, there are two parameters that we can control here, right? One is one,

42:23

one parameter is chunk size. Remember that? You can decide the chunk size if you're doing in a fixed

42:30

chunking. Okay? Let's say chunk size is maybe thousand. It means that every chunk will have

42:35

thousand words. Correct? But everyone, do you remember there was one problem that if you have a very big document

42:42

and if you divide them into individual chunks. Is it possible that, let's say, at the end,

42:47

let's say this is the document and you say that this is chunk one, this is chunk two. Let's say there

42:51

was some sentence started in chunk one and some part of that sentence goes into chunk two. Remember that?

43:01

So how can you control it? Obviously, when you cannot control it 100%, but how can you try to reduce it?

43:06

by the concept of chunk overlapping. That some part of the current chunk or some part of the current chunk or some part of

43:12

the previous chunk you can store in the next chunk, maybe 10% 20%, you can store in the next chunk.

43:18

So that next chunk will also have some context from the previous chunk. That parameter is called as chunk

43:23

overlap. That parameter is called as chunk overlapping. That parameter is called as chunk overlapping. Is that point clear to all of you?

43:38

Okay? So chunk size controls the chunk length.

43:42

Chunk overlap keeps some repeated content between adjacent chunks, which helps some

43:47

important information which has been splited across multiple chunks to maintain some context around

43:53

it in the next chunk as well. So that next chunk is not like, it is not at all aware of what is

43:57

going on. Is everyone clear with these concepts about text blater, chunking, chunking, chunk

44:05

chunk size, chunk overlap, and so on? Everyone, clear? Okay. Then the third, third, third,

44:12

component everyone that comes into picture is embeddings. I think we have done a lot of

44:19

discussion on embeddings. That every word, every word, every word gets converted into a list of numbers.

44:30

And what will be the size of this list, everyone? How many numbers will be there in

44:35

this list, this list, 100, 200, 500, etc?

44:42

It will depend on embedding model, right?

44:45

So guys, in today's class, we will use open AI embedding model.

44:55

Open AI embedding model.

44:57

Do you remember that there are two different embedding models that open AI provides?

45:03

Small and large.

45:08

Small gives you 1,536.

45:12

as a, you can say that size of the vector, size of one embedding, and large one gives us the

45:18

double of this, that is, 3,072. So any one of them we can use, right? Small also works absolutely

45:24

fine for most of the cases. Okay? Now, if you remember, there is one more thing, that's

45:31

similar vectors. Well, similar means, similar vector means, close meanings, similar meanings,

45:37

similar meanings, right? Can we say that close vectors?

45:42

Close vectors means similar meanings.

45:57

Correct? And if the vectors are far apart, if they are very far from each other, that means

46:03

they are less similar or they are not similar to each other. Correct or not everyone.

46:07

Okay? Then we have the concept of fourth component is, so as all of these components

46:13

we are going to implement, loader, splitter, embeddings, and then to store these embeddings,

46:20

we are going to have a vector database. Vector database is the database to store vector embeddings, right?

46:28

Vector database is allows us to store embeddings.

46:37

embeddings and performs and allows us to perform and you can say that allows similarity search.

46:45

Correct or not, you don't have to implement similarity search manually.

46:49

Vector database like ChromaDB provides us, allows similarity search. Is everyone clear with

47:00

this? Store embeddings and allows similarity search. Perfect. Then everyone, the example,

47:07

of vector database that we are going to use in our use case is chroma DB. So we will

47:11

use chroma DB. Previously also we have used chroma DB because chroma DB is one of the most

47:16

widely used database which can run locally and it can also persist data permanently. There is a functionality

47:22

with which we can persist the data as well. Okay? Then the fifth component, everyone, is the retriever component.

47:37

component. What this retriever component does? It takes the user query.

47:47

takes the user query and searches relevant chunks or relevant documents.

48:07

relevant documents, right? We will see that everyone how we are going to

48:16

implement this. So basically in the retriever also, the retriever component also is given by a

48:21

land chain. So we just have to invoke it, create the object of it and invoke it. Just like we

48:25

have implemented agents, this is how we do that. Now everyone, these are the components that we are going

48:30

to implement, right? The loader, splitter, embedding, database, and retriever. Now coming to the next

48:36

point everyone, that how we are going to have the complete flow of this land chain.

48:42

So guys, in Langchain rat, if you see the most common word in Langchain is chain, that you

48:47

define everything in the form of chain, right? And to create chain, what do we have? We have something

48:53

called as land chain expression language. Remember, in which you define component one, pipe symbol,

48:59

component two, pipe symbol, component three, pipe symbol, pipe symbol, four. So from component one, we will go to

49:04

to, from two, we will go to three, from three, we will go to four and so on. So this is how

49:08

we are going to create our land chain for RAG application also, right? How we are going to do everyone

49:13

is, first of all, we are going to have the retriever component. First of all, we want to retrieve the

49:19

documents. Then everyone, we want to, let's say, the next component we are going to have is some kind

49:25

of formatting of documents. We will see what is the meaning of formatting in some time, formatting

49:30

the documents, right? Then we are going to have, now it means that using these,

49:34

two things. You have retrieved the relevant documents or relevant chunks. Now these

49:38

relevant chunks, don't you think you need to pass to the LLM now to generate the final answer?

49:43

That you use these relevant chunks, use these relevant documents and generate the final answer?

49:47

Yes or no everyone? Correct? For that everyone, we write a prompt template. Correct? Because

49:56

to LLM we are going to pass a prompt. Okay? So whatever data we have fetched, we attach inside

50:01

the prompt and inside the prompt everyone, this is not.

50:04

a hard-coded prompt, we will use a prompt template for it. We have used multiple times.

50:09

So we have already given some instructions inside this template and whatever data we have added,

50:14

whatever data we have retrieved, we will add it inside the prompt and this prompt we will pass to the LLM.

50:21

Is that point clear to all of you? This data, this prompt, we will pass to the LLM and whatever data,

50:26

whatever answer, LLM will return, then we will pass it through the parser so that it returns the data in

50:33

the spring format. This is the complete chain we are going to develop in today's class.

50:39

Is that point clear to all of you? This is the entire chain we are going to implement in today's

50:46

class. Okay? Everyone clear? That's it about the theoretical part, the conceptual part. Now we can

50:53

directly start and we can directly start writing the code. We can directly start writing the implementation

50:58

now. Should we start the implementation now? If everyone is comfortable.

51:03

Okay. So everyone now let's get started. Can we not make the steps before retrieval?

51:11

Can we not make the steps before the retrieval in the chain? We can do that. See, it is a defined flow.

51:16

It is a general flow. But if you think that there is some other flow that could also work for your organization, that can also work.

51:22

Okay? So if you want to format the data first and then retrieve and then pass it to the LLM, then inside the prop, you can do that.

51:29

Okay? Perfectly fine.

51:30

So let's start the Visual Studio everyone.

51:37

So everyone, what we are going to do is we are going to do is we are going to open the folder of

51:41

land chain application, which is our land chain app.

51:49

Guardrails generally comes at the end. Okay.

51:54

And in fact, at prompt level also you can do the guard railing.

51:57

Okay, we will discuss guard railing at the end of the module.

51:59

Okay.

52:00

We will have.

52:00

classes on guardrails also. Okay. So now everyone, what we are going to do is let's close all the tabs

52:05

and let's create a new class or new file here, which is Lankchain rag dot PY. Now everyone,

52:14

there is one thing that we are going to implement first of all, which is like we will install all

52:19

the dependencies. Okay? So what all the dependencies will be required? PIP3, install, Lankchain,

52:28

land chain open AI, land chain community. This is the new dependency that we will be seeing

52:36

today, Lanchine community. Lankchain also gives you the support of Kroma, so Lanchine Kroma,

52:43

then Lankchain, text, splitter, and that's it. So if you see Lankchain, Langean, Lankchain,

52:55

and Lankchain community, Lankchain, Kroma, and Lankchain, text, splitters.

52:58

let's install all of them. Now everyone, what we are going to do is because this

53:09

is going to be very big code, right? We are going to have, we will see that. We'll see

53:13

that, I'm okay, but it's a use case of every dependency. We'll see that. Now, one point everyone

53:18

is that this complete code is going to be very big because we will have multiple things. We will

53:22

have, we will have document loaders, retrievers, splitters, embeddings, uh, vector

53:28

database, retrieval, and generation, and then, and multiple things, right, to load the documents

53:34

and whatnot. That's why everyone, what we are going to do is we are going to not write the entire

53:38

code in one class. If you want, you can do that. But what is the best practice, everyone, to split

53:43

the code into multiple files, correct or not? To split the code into multiple files. So that's

53:49

everyone, what we are going to do is, first we are going to create the file like this, which is to create

53:55

the corpus, right? To create, to load the documents, basically.

53:58

So, lankchain, rag. So all the rag files will be having this name, Langchain, rag,

54:05

sorry, rag, and let's say, create corpus. Create corpus means what, everyone? Corpus means database.

54:14

Or you can call it as database also, create db.py.

54:17

Create corpus.compo, create db.py, create db.py, same thing. So we are going to first create this file. Let it

54:22

install everyone. Just the last dependency is remaining, I guess.

54:28

Some of the dependencies are quite big, so it is taking time.

54:48

Okay, I think we can start writing the code. First, we need to create the corpus. From that,

54:52

for creating the corpus everyone, don't you think we need to store files, correct or not? We need to store files.

54:58

Yes or no? For that, everyone, we need the path library from Python. So we will use

55:05

path lip. From pathlib, we will import path. Right? To write the documents, to write the files at a

55:12

particular path. Okay. And everyone to store all the documents, what I will do is I will create, let's say,

55:16

one folder. And here I can do, let's say, all the rag documents. Okay? The name of the folder is,

55:22

let's say, all documents. Or, yeah, let's say doc you. All the documents are press.

55:28

here. So what is the path of this folder, everyone? Copy path. And if you see, this is the path.

55:34

Does it make sense to all of you? This is the path of this folder. So what we are going to do,

55:38

everyone, define a base directory. These are the variables that we are going to use again and again.

55:46

It is the base directory. It means that this is the directory or this is the folder where we are going to

55:50

store the documents. Is that point clear to all of you? Okay. I will give you one interesting idea also.

55:55

If you want to create this folder, right? You can delete this folder, let's say. And let's say

56:00

if you want to create inside land chain application, if you want to create this folder, you can

56:04

also do like this. That base directory dot mkDIR. Okay. And you can say that. MKDIR means make

56:12

directory, create directory. And you can give parents is equal to true. Okay. Create this.

56:19

Exist. Okay. If this exist already, it is okay. But if this exists already, it is okay. But if does

56:25

not exist, create this. Okay? If you are already creating this document folder here,

56:30

then you don't need this line. Okay? You can remove this line also. I can comment it out. Is that

56:36

concrete to all of you? Okay. Then everyone, we are going to create documents like this. Documents

56:43

is equal to. Now for now everyone, let's say assume that we are getting the documents in the form

56:49

of text format. Correct? Let's say we are going, we are getting return policy, refund policy, can

56:55

policy and multiple policies like this, maybe two, three policy documents.

56:59

But as of now, we are just getting them in the file format or in the textual format.

57:03

Now we want to load them. Now, as of now, these are normal files, normal text,

57:08

normal PDFs, normal documents. But don't you think we need to convert them into

57:12

land chain documents? Correct? So what we are going to do?

57:21

Let's say we have these policies.

57:25

pays this completely. So just a second, everyone. Let me copy this complete data part.

57:35

Yeah. If you see this entire data is there and look at this data. First we have, so this document,

57:43

everyone, this documents is nothing but a dictionary where you have the name of the file,

57:46

return policy dot MD, MD made background, then you have the return policy document, then you have

57:51

the refund policy document, then you have the refund policy document, then you have the shipping policy document.

57:54

So this is how you are getting the data. And there is one more, which is warranty policy.

57:58

And there is one more cancellation policy. Does it make sense for all of you?

58:01

Assume that this is how you are getting the data. Correct?

58:04

This is how you are getting the data. Now, what do you need to do everyone is, you need to store these

58:08

into the file. First, create the files for them. For file name. Now, honestly, everyone, I could have

58:14

skipped all this by giving all these documents in any format, right? I could have directly created files.

58:20

But just I want to show you that with Python, you can create files also.

58:23

So this is called us file handling concept in Python. How do you handle files? Correct?

58:30

So what do you can do? You can iterate through the file.

58:35

So there are two things that we will iterate through. File name and content. I iterate in

58:43

documents dictionary. So the key is file name, value is the content. Key is the file name, value is the content. Key is the file name, value is the content, right? In the dictionary.

58:51

right? Documents. Dotts. Okay? I iterate through all the items in the documents

58:57

dictionary. Take the file path. What is the file path, everyone? Don't you think file path is nothing

59:02

but the base directory? Base directory means go to documents and create inside the documents,

59:08

create a file with this name, return policy.md, refund policy.md, shipping policy.md and

59:15

so on, folks clear, slash file name. So now everyone, let's say, if the base directory,

59:21

is this. Okay?

59:27

Back to everyone, I think, even if you give only slash documents, that with the current directory.

59:34

Okay? So base directory takes the relative path from the current directory. And from the current

59:41

directory, where this current file is written, Lanchain, Rag, Create, Corpus. This file is

59:46

currently written in Langchain. So inside Langchain, you have just one more folder, which is

59:50

slash documents.

59:51

So what will be the file name, everyone?

59:53

slash documents slash return policy.md.

59:57

Slash documents slash refund policy.md. Is this first line cleared all of you?

1:0:01

And on this file path, everyone, what we're going to do is write text, file path.

1:0:06

Dot right underscore text. And we will do content. Content go. We will strip. If there are

1:0:13

any, let's say, extra spaces, we will remove it. And we will use the encoding.

1:0:20

Encoding is equal.

1:0:21

to UTF8. UTF8 is the encoding which we use for English language. Everyone clear

1:0:28

with these two lines of code. Everyone clear with these two lines of code.

1:0:37

Okay. And finally, let's say, that's it. We are done with this everyone. And now, let's see,

1:0:42

try to run this application. Run this code. Okay. So what you can do everyone is,

1:0:47

okay, let's do one thing everyone. Let's run all these things in one shed, in one shed.

1:0:51

Can you explain line number 84? 84 is just a file path. For example, let's say what is the

1:0:56

file, what file path you, like at what path you want to create the file inside documents.

1:1:01

So base directory, I have defined slash documents in the current folder slash documents slash

1:1:06

return policy.md. So this will be the one file that will be created. Right. So return policy.

1:1:11

dot MD and this content will be added in that file. Then the next file will be slash documents

1:1:17

slash refund policy.md and this content will be added in the, in the, in the, the,

1:1:21

file. Then the third policy will be, third file will be. Should it be the file name? Yes.

1:1:26

This will be the file name. The file, file, not really file name, file path. Okay, that we have created

1:1:32

a file at this path. If you see, file name is what? File name, if you give the complete file name,

1:1:37

that is nothing but the file path only. For example, if your file name is like, return policy.md,

1:1:44

this is your file name. But can you just access this file only with the name? No, right? You need to

1:1:51

where this file should is present. That's why generally when you access on, when you work

1:1:57

on the file system via code, you work with file path, that this file is present inside documents

1:2:02

folder, then return policy.md. This becomes a complete file name or complete file path. Make

1:2:08

sense? Is everyone clear? Okay. Then everyone, once we have assumed that, assume that for now,

1:2:16

this file or this complete code will generate four, five, five, file.

1:2:21

inside this document folder. Correct? I'm teaching you from scratch. I'm not telling you,

1:2:27

assume that the data is already there. I could have done that. We could have saved 15 minutes there.

1:2:32

But we should understand that we don't get data always in the desired format. We might get data in

1:2:39

the textual format, in the dictionary format. Now we need to convert that dictionary and we need to create

1:2:44

files out of it. And these two lines of code is creating those files. Correct? Now when we will run this

1:2:50

code, four, five files, return policy.md, refund policy.md,

1:2:56

cancellation policy.md, they will be created inside documents folder. Now, once you have these

1:3:00

files, everyone, don't you think you need to ingest these files inside Langchain? You need to load

1:3:06

these documents. As of now, you are, these are just simple files. Correct? These are just simple.

1:3:12

Dot MD files. Now you need to load these inside Langchain. For that, everyone,

1:3:17

we will create another file here, which we will call it as, let's say,

1:3:20

land chain, rag, all the rag code, every rag file will be starting with

1:3:25

landchain hyphen rack and ingest.py. Ingest means, ingesting means that, everyone, you are ingesting

1:3:32

the data inside document loader. You are loading the documents in Langchain. For that, everyone,

1:3:37

again, we will use PathLid because we need to read the data from files, import path, right? And

1:3:44

then everyone, from Langchain dot, Langchain underscore community, we will import document load.

1:3:50

loaders. If you see everyone, these document loaders are coming from Langchain community.

1:3:56

Is that point clear to all of you? I think Mukul, you were asking this, right? That why we are

1:3:59

importing, why we are downloading Langchain community? Because we want to use document loaders

1:4:04

and they comes from Langchain community. From Langchain community dot document loaders, we will

1:4:10

import. There is one thing called as directory loader and there is one thing called as text loader.

1:4:16

What is the use case of this? We will see. Then everyone, we will see.

1:4:20

Okay, there is one thing that I have missed everyone. Here, I got this wrong. You have to

1:4:29

define this in the form of path. Just cut this and path. That's it. Everyone clear? This is

1:4:36

the path that you have defined, the path object. Okay? Similarly, everyone, in In jest, we will

1:4:41

define the directory. That where we have to load the documents from, what is a path? Okay? The path is,

1:4:47

let's say the data directory or the file directory, policy directory.

1:4:50

Data directory is equal to path slash documents. Correct? All the documents are present

1:4:57

in this path. Now we will create a loader object, everyone. Loader is equal to directory

1:5:02

loader. And here we need to provide some parameters. What are these parameters? First of all,

1:5:07

provide the path. What is the path? In the string format, we will provide the data directory.

1:5:12

Again, everyone, you can directly provide this also. Does not matter. First, you are giving the path

1:5:18

that our data is present in this folder. At this path, please read the data from

1:5:22

this path. The first parameter is clear. Okay? Then everyone, you provide other parameter

1:5:31

which is called as globe. I'll talk about globe as well. That, what type of files do you want to read?

1:5:36

Now, inside this documents, everyone, let's say assume that. Assume that, assume that there are a lot of files

1:5:39

also present. But don't you think your policy data, your policy's documents are only present in dot MD

1:5:46

fold dot MD type of files. See, shipping policy dot MD. MD means markdown.

1:5:53

Right? Maybe it can be in text format. It can be in document format. It can be in PDF format. Okay.

1:5:58

So you want to read only the, only the dot MD files. For that, we will give the, the star star, star,

1:6:08

star means name of the file could be anything. Then slash after slash dot MD. This is the format.

1:6:16

that we use. So basically, dot MD means, this basically means that just read or just load

1:6:22

dot MD files. Does it make sense to all of you? This means just load dot MD files. Search for

1:6:29

MD files. That's correct. Just load dot MD files. Then coming to the next point, everyone,

1:6:36

what loader class we are going to use? We are going to use text loader. We are loading textual data,

1:6:42

not image data, not other type of data. There are other loaders also. But

1:6:46

now we are just loading the text data. Right, everyone? And then everyone, we have to

1:6:52

just provide the encoding. That what language you are using? Then you provide loader arguments,

1:6:58

KW arguments. And this, everyone, there are multiple things that you can provide here. We will only

1:7:03

use one of them, which is encoding is UTF8. Now everyone, if you see, there is nothing that you can

1:7:08

more do about the syntax here. You can just try to understand the syntax. Right. Directory loader, you are

1:7:16

creating a loader object which will read the data from this path. It will only read the

1:7:21

dot MD files. It will use the text loader functionality to load the text and it will load the data

1:7:27

in the UTF8 encoding format. Is everyone clear? Right? Is everyone clear with this loader object?

1:7:37

Now see everyone. Now I know some of you might be worried that Deepak how do I remember all

1:7:43

these things? Correct.

1:7:46

How do I remember all these things? It is impossible. I don't say it is difficult. It is impossible

1:7:50

to remember so many things. There are so many frameworks, so many libraries, and you have to do so

1:7:55

much of tasks, impossible to remember these many things. That's why everyone, you don't have to

1:7:59

remember these things. You just need to understand that how do you create a rag application

1:8:03

in Langchain? What is going to be the format? What is going to be the step-by-step process

1:8:09

of it? Then everyone, you can Google it about it. All of these things are clearly written on Langchain

1:8:14

documentation. Okay?

1:8:16

I also referred Langchain documentation before the class. It's not like that. I remember this

1:8:20

complete code. I can definitely tell you to scare all of you that I remember all this code. I have

1:8:25

used this 100 times. No, I don't put efforts in remembering the code. No one can do that and no one

1:8:30

should do that. Make sense, everyone? You should be able to understand the idea that what this document

1:8:35

loader does. And that also on a high level. That also on a high level, that document loader loads the data

1:8:41

from one place into Langchain. Okay? Now we will use this.

1:8:46

document loader, let's say this will return us documents. Let's say docs is equal to

1:8:51

loader dot load. It will load all the documents inside this docs variable. Now what do we need

1:8:57

to do everyone? Let's say we have got all the documents now. We have loaded all the documents

1:9:02

inside Lank Chain. Now we can directly use it for, we can directly use it for retrieving.

1:9:13

Correct or not everyone? We can directly use it.

1:9:16

for retrieving, correct? So two steps are done. What's two steps are done?

1:9:22

First step done was, what is the first step done, everyone? Let's say, the first step is,

1:9:30

created the documents, right? And the second step that we have implemented in this file is

1:9:39

loading the documents. Okay? Where we have stored it in, as of now, note.

1:9:46

As of now, we have not stored the documents inside the vector database. That step will

1:9:49

come later in some time. Okay? So as of now, assume that, I give you dot MD files. Now, from

1:9:56

these dot MD files, you have just created documents. Now these documents, you will load inside

1:10:00

land chain. Then you create embeddings. Then you store into vector database. Then it is ready

1:10:04

to use. So two, three steps are still remaining. Everyone clear? Two, three steps are still

1:10:10

remaining. Now, it's 901. Should we take a break so that you can see that. What happens if dog size

1:10:16

in GBs, can we load it in all single object? It is going to be difficult, but we split it.

1:10:21

As of now, the assumption is that we have one document is not big enough. But if one document itself

1:10:27

is big enough, you might have to, one file is big enough, then you load it into document, then you

1:10:31

split it. Right? We will do the chunkification also. Okay? But if you think that the document itself is,

1:10:38

let's say, maybe terabytes, then first you have to do that might be manually, that create these documents

1:10:43

into small pieces. Then you load them into the memory and then use them. Okay? Makes

1:10:51

sense? Do we load? No, no, no. See, everyone now tell me one very good question coming from

1:10:56

Mukul. Do we load the data always? Tell me, this data loading process and data, like creating the

1:11:04

files, do we have to do every time. This loading process or creating these files, this is just one-time

1:11:12

process. Once you create the documents, then you load the documents, then you convert them

1:11:18

into embeddings, store them into vector database. Now it is done. Now your documents are present in the

1:11:23

vector database. You don't have to do anything now. You can directly use them every time. Make

1:11:28

sense, Mukul? You can directly use them. Cool. Okay. So we can take a break now, everyone. It's

1:11:34

902. Let's take a break of maybe 12, 13 minutes. Let's need it 9. 9. And after the break, everyone,

1:11:40

we will start writing the remaining code.

1:11:42

Okay. Let's meet at 9.15 p.m. Sharp. Okay. If you want, I can push the code as well.

1:12:12

So your code is present at this location.

1:12:23

The name of the function is recursive, character, text, splitter.

1:12:30

Recursive, character, text, spliter.

1:12:31

Recursive, character, text.

1:12:35

We are going to use this text splitter.

1:12:38

Okay? See you in 10 minutes, everyone.

1:12:42

Thank you.

1:13:12

Thank you.

1:13:42

Thank you.

1:14:12

Thank you.

1:14:42

Thank you.

1:15:12

Thank you.

1:15:42

Thank you

1:16:12

Thank you

1:16:42

Thank you

1:17:12

Thank you

1:17:42

Thank you

1:18:12

Thank you

1:18:42

Thank you

1:19:12

Thank you

1:19:42

Thank you

1:24:42

Thank you

1:25:12

Hi everyone. Let's start.

1:25:15

So just one more thing everyone.

1:25:16

Let me just write it down one more point.

1:25:18

One more pointer here so that you can refer it later on one more pointer here so that you can refer it later on

1:25:21

that what directory loader does.

1:25:23

Directory loader loads multiple files from from the given path.

1:25:35

That whatever path you have given, it will load.

1:25:37

And what text loader does?

1:25:39

Inside this we have a text loader as well.

1:25:41

text loader reads the text data reads the text data, reads the text data from the loaded files, from the files.

1:25:54

Everyone clear till now?

1:25:57

Everyone clear till now?

1:26:00

Now folks, once we have loaded the dot data, now we need to what?

1:26:04

Now we need to do what?

1:26:05

Now we need to split the data.

1:26:07

Correct everyone?

1:26:08

Now we need to split the data into chunks.

1:26:10

split the documents.

1:26:12

We have loaded the documents now.

1:26:14

Split the law, split the documents into chunks.

1:26:19

And what is the process for this, everyone?

1:26:21

Splitting the data into chunks.

1:26:22

First, we need to create a text splitter object.

1:26:26

For text splitter object, everyone, we import recursive text splitter.

1:26:32

And this comes from from Lanchine underscore text

1:26:39

underscore splitters that we have installed today, import recursive text splitter.

1:26:46

And once you do that, everyone, recursive text splitter, and we have to pass few parameters here.

1:26:53

What do you think everyone, what parameters do we need to create, to split the data into chunks?

1:26:59

What parameters do we need to split the data?

1:27:02

First, we need the chunk size, absolutely correct.

1:27:04

Let's say the chunk size is maybe randomly you can take 500, 800,000, 5, 500,000, 5, 5.

1:27:09

maybe less, 1,000 might be more, so let's take a middle value, 800.

1:27:13

Right?

1:27:14

You can take whatever you want.

1:27:15

And then you need chunk overlap.

1:27:16

Chunk overlap is generally everyone between 10 to 20% of the chunk size.

1:27:20

So you can take maybe 15%, that is 15% of 800, which is 120.

1:27:25

This looks good.

1:27:26

Again, these are just assumed numbers.

1:27:28

You can take other things as well.

1:27:30

Is that point clear to all of you?

1:27:32

Okay.

1:27:35

There is one more parameter everyone that you need to add here.

1:27:38

Add start index is equal to.

1:27:39

true. So basically what it does everyone is that when you create chunks, for example,

1:27:43

there is a file and you have divided that file into 10 chunks.

1:27:46

Now how will you identify chunks?

1:27:48

Don't you think you should give some index or some index to the chunk, some number to the chunk?

1:27:52

This is a chunk one of this document, chunk two of this document, and so on.

1:27:56

This is what add start index does.

1:27:58

That adding the start index to each chunk.

1:28:00

Makes sense, everyone?

1:28:04

So once you do that everyone, now you can use this text splitter.

1:28:08

splitter, you can create chunks now, text splitter.

1:28:12

Dot chunk, split documents.

1:28:15

Split documents.

1:28:16

And here you can provide everyone the documents that you have loaded.

1:28:20

The documents that you have loaded just here.

1:28:23

Once you load all the documents, you create a text splitter object

1:28:27

and then you split the documents that you have loaded just right now.

1:28:31

Is that point clear to all of you?

1:28:33

Now everyone, just to identify that how many, maybe,

1:28:37

maybe you can say that how many documents you have.

1:28:42

You can print, let's say, total number of documents, original documents.

1:28:48

How many documents are there?

1:28:52

Let's say you can print length of documents, and you can use this formated string.

1:29:06

Similarly, you can print chunks also.

1:29:09

Generated chunks.

1:29:11

So at least you will get some idea that how many documents we had and how many chunks we have created.

1:29:16

Is that concrete all of you?

1:29:18

How many documents you had and how many chunks you have created?

1:29:22

Now if you want everyone, you can try to print the chunks also.

1:29:26

Try to try to print the chunks.

1:29:30

And if you try to print the chunks, you can see what chunks have been created.

1:29:34

Again, we can skip it, not required.

1:29:35

not required.

1:29:36

Everyone clear?

1:29:39

Now, as of now, have we stored these chunks into vector database?

1:29:45

Have we stored these chunks into vector database?

1:29:48

No.

1:29:49

Now let's do the next point, everyone.

1:29:50

Store these chunks into vector db.

1:29:56

For this everyone, we will have to install a few more things as well.

1:30:00

One is the from land chain, underscore chroma.

1:30:04

underscore chroma, import chroma db, right?

1:30:11

And because before storing the chunks into chroma db, what do we need to do?

1:30:16

We will have to create embeddings.

1:30:19

So from Lanchain OpenAI, we will import Open AI embedding models.

1:30:25

Correct everyone, this is the first time that we are using Open AI embeddings in Langchain, correct?

1:30:34

Now everyone, what you need to do is that you need to define the path, that where do you want

1:30:38

your chroma database to be there.

1:30:39

So you can define some chroma directory, chroma db directory, that is, let's say, you want

1:30:44

to create the chroma db directory in the same folder, which is let's say, chroma, chroma db.

1:30:52

I think everyone there is one mistake that we have done from the starting.

1:30:56

It should be not slash, it is just documents because it is in the current folder.

1:31:00

Okay?

1:31:01

If this does not work, we might have to change it, but ideally it should work.

1:31:04

And another is this document.

1:31:06

So this chroma db, so if you see everyone, data directory means where your data is present in documents

1:31:10

folder and chroma db will contain your chroma database, okay?

1:31:15

And then everyone, if you remember inside chroma database, do we create multiple collections?

1:31:21

Just like tables, right?

1:31:22

Just like tables in SQL database, you create multiple collections in chroma db.

1:31:27

For now, we are just going to create one collections and we can give the name as collection name

1:31:31

because we are going to use this maybe multiple times, that's why.

1:31:34

collection name is let's say maybe e-commerce underscore e-commerce underscore policy underscore docs.

1:31:42

So this is the collection name that we are going to use to store our chunks, to store our embeddings, policy docs.

1:31:50

Everyone clear?

1:31:53

Now, what is the process of storing this?

1:31:56

First, everyone, what do we do is if you are storing this data from scratch, we might have to clean the old database, clean old database.

1:32:04

Right? Again, it is an optional process. You might do that, you might not do that.

1:32:08

It does not matter. But clean old database. If there is any redundant data that might be cleaned.

1:32:12

Again, how can you do that? If, let's say, chroma DB, chroma directory already exist.

1:32:19

It means that this is already there. It means that some data might already be there. You can clean it.

1:32:23

And how can you clean it everyone? You can remove it. You can remove this directory and create it again.

1:32:29

For that, you want to create the directory. You want to remove the directory. For that, everyone, you import

1:32:34

a Python library called shuttle. Okay, import shuttle. And using this shuttle, everyone,

1:32:42

what do you do? Shuttle.RM tree. RM tree means remove. Pre means whatever data you have inside

1:32:48

this ChromaDB, maybe multiple folders, multiple collection, clean this data for now. Again,

1:32:54

everyone, it is an optional process. It is an optional step that I'm telling you. Okay? So shuttle.

1:32:59

Remove tree, which directory we want to remove? This directory, I want to remove. This directory I want to

1:33:04

move. Again, everyone, let me write it down that this is an optional step. Okay? If you want your data to be cleaned,

1:33:12

right, this is the optional step. Is everyone clear? Correct? And then everyone, you will have to use

1:33:19

some embedding model. And what embedding model we are going to use for it, just to give me a second.

1:33:25

Embedding model, I must have defined somewhere in the notes. Yeah. This is the text embedding three small.

1:33:32

Okay. This is the open AI embedding model that we are going to use. Okay. Is everyone

1:33:41

clear? If you want to store it inside, what do you say? Environment variable also, you can do that.

1:33:47

Okay? If you want to store this in environment variable, you can do that perfectly fine. Okay. But it is not

1:33:53

something that we want to hide it. It is okay. Then everyone, what do you need? You have loaded the

1:33:58

documents. You have splited the chunks. Now we just want the embedding model. This is the

1:34:02

embedding model that we have everyone. And finally, what we are going to do is, we are going to create

1:34:09

embeddings. Embedings is equal to open AI embedding model. And here we need to pass that what model we are

1:34:18

going to use, we are going to use this model. Open AI embedding model. And guys, honestly, you can

1:34:24

like no need to do this again and again. You can directly hard code it. Because this is what we are

1:34:29

going to use only once. Okay.

1:34:32

You can do this. You can do like this. So everyone, if you see, this is how we create a chat GPT object also, right? GPT object, LLM. But here we are creating the embedding object. Okay? Everyone clear? Is everyone clear? Now we will store this into vector database. So let's say vector store. And we will use chroma object. Inside this chroma object, we will just have to pass what data we want to store, what embedding model we want to use.

1:35:02

And which collection, inside which collection we want to store.

1:35:05

Three parameters. One is the collection name.

1:35:08

Collection name is the collection name that you have defined at the top.

1:35:12

Then embedding function is this embedding function that we are going to use.

1:35:15

Basically, the embedding model that we are going to use. And then everyone, where you want to store,

1:35:23

persist directory is equal to string. And there you provide chroma directory.

1:35:29

This chroma directory simply means that where you want to store.

1:35:32

store. So if you see everyone, first you are providing the collection name. Maybe you can think

1:35:37

in this way. This is my database, Croma directory. This is my database. Inside this database,

1:35:43

this is the name of the collection. And this embedding function I want to use to create embeddings

1:35:47

to store inside vector database. Everyone here. Does embedding model for audio, video, text

1:35:53

embedding, shows it for text. I think you'll have to Google about it. There are embedding models

1:35:58

for that also. I'll have to check that how exactly embedding works for audio, video, etc. But

1:36:02

there should be a way. Okay? OpenEi must be providing some models for that as well.

1:36:08

Is this clear even? So you have kind of created a chroma DB object. Okay. That where you want to

1:36:13

store, what collection you want to store and what embedding model you want to use. Now you just have

1:36:17

to tell what data you want to store. So vector database, vector store dot add documents.

1:36:23

And here you just have to provide. Now everyone tell me here you want to store documents.

1:36:27

Here you have to store documents or chunks. Tell me.

1:36:32

Inside vector database, you store chunks, right? And this everyone finally give you some chunk

1:36:38

IDs. How can you access it inside the vector database? How many if you're clear? Just have a look at it

1:36:43

everyone. Just maybe these five, six lines of code. Just look at this. If I summarize what we have

1:36:49

done, created the embeddings model, which embedding model we want to use using open eye embeddings

1:36:54

class from Lanchine. Then we created the Croma object where we have provided the directory, which

1:37:00

directory we are going to use, basically the chroma directory, the folder name, embedding function,

1:37:05

and the name of the collection. I think line number 52 is the easiest one. Once you have

1:37:14

created the chroma DB, you are just telling that what data you want to store inside this

1:37:19

chroma DB. We want to store these chunks. So add documents inside vector store, these chunks

1:37:24

we want to store. Make sense, Chira? That these chunks, I want to add inside vector store.

1:37:30

That is also one of the way. Okay, Mamcy? That is also other way.

1:37:39

Now, tell me how many if you're clear. So till this point of time, everyone, what we have done? We loaded the

1:37:44

documents. First, we created the files, loaded the documents, splited the documents, then created

1:37:50

the chunks. Splited the documents means created the chunks. Created the vector database.

1:37:55

Stored them, stored, basically defined all the variables, that this is the vector database folder,

1:38:00

This is the collection name and this is the embedding model, created the embedding model.

1:38:04

And finally, we are going to store these chunks. We are going to add these documents inside

1:38:08

vector database. Okay? Is everyone clear? Yes or no?

1:38:16

Folks, please let me know if this is clear. So as of now, what we have done? Again, everyone,

1:38:23

I have habit of repeating loading documents. After that, we have split into chunks.

1:38:30

Then create embeddings and store embeddings into chroma dB.

1:38:42

This is what we have done till now. Is everyone clear? Perfect. Now, finally thing, the final thing, everyone is?

1:38:52

Now, one last thing, everyone. Meta data is already there inside the, if you see, you're not giving it separately, but when

1:39:00

you are creating these files, right? When you are loading the documents here, you are having

1:39:04

some metadata also. I think we had some metadata creating the corpus.

1:39:15

Okay, as of now, there is no metadata, but if you want to add, you can add it later. Okay? I think

1:39:21

we have not added the metadata for now, but we can do that. Okay. Now, one last thing, everyone, that I think

1:39:26

that people might be having doubt in this persist directory. Now, this persist directory. Now, this persist

1:39:30

this stores the data locally. So what this does is this tells chroma db to

1:39:39

to chroma db to store vectors locally so that we can use later. So it is going to persist

1:39:49

locally. It is going to persist. It is going to save permanently so that we can reuse them

1:39:56

later. Is that point later all of you? So that we can

1:40:00

reuse them later. Persist means what? Save. Pursist means save. In which directory we want

1:40:05

to save? This directory. Clear, everyone? This is a complete process that we have implemented till

1:40:16

now. Just look at line number 56. These four steps we have implemented. Now everyone, we are going

1:40:21

to create the final rag application, Lanchine RAD. This application, basically, what this does is

1:40:27

it will read the data or it will load the chunks, load the data from ChromaDB and create

1:40:40

a retriever. So for this everyone, what we are going to use, from PathLIP, we will import

1:40:48

path from Lanchine because we would need, what do you say? We would need LM also from LAM chain also.

1:40:55

From Lanchine open AI, we will import chat open AI and open AI embeddings for similarity search

1:41:02

etc. Then, because we are going to use ChromaDB, from Lanchine, Chroma, Proma, import, Proma. These are the things

1:41:14

that we are going to use. So first, everyone, Open AI, API key, etc., that we'll have to store.

1:41:19

I will do that later. So we would need this Chroma directory and collection name.

1:41:25

These two things we would need. Obviously, to load the chunks, to use the chunks, we need the directory and the collection name. And we would need the embedding model. Because to perform similarity search, don't you think the embedding model will be required? Also, everyone, when the query comes in, when the query comes in, don't you think that query also you convert into embeddings and then you perform similarity search? Correct? To convert the query into embeddings, we will have to use the same model, right? We'll have to use the same model.

1:41:55

That's why we are again creating the embeddings object here.

1:41:58

Okay?

1:41:59

After that, everyone, we will again use vector underscore store is equal to what chroma database we are going to use?

1:42:06

Chroma. And again, everyone, this chroma database, these things we want to use.

1:42:12

Okay? This vector store just says that which chroma database you want to use.

1:42:16

There might be multiple chroma databases you might have, multiple collections you might have, that this vector store I want to use.

1:42:21

Now, finally, I will create a retriever.

1:42:25

As of now, everything is copy-pasted from the previous class, from the previous file.

1:42:30

Now we are going to create a final retriever. In the final retriever, everyone, create retriever

1:42:35

is equal to vector store. Dot, it automatically gives you a function called as retriever.

1:42:45

As underscore retriever. Now, I will explain the meaning of this, but mostly you will get from the

1:42:50

name itself, that now use this vector store as retriever.

1:42:54

getting the point, everyone.

1:42:56

Now you have to tell what kind of search you want to perform.

1:42:59

Do you remember that?

1:43:01

There is a similarity search and there are other kinds of searches also.

1:43:04

So I want to perform what type of search?

1:43:08

Search.

1:43:11

Search underscore type is equal to similarity, right?

1:43:18

And everyone, search.

1:43:23

I think this parameter.

1:43:24

may not be required actually. Let me check if it is a mandatory parameter.

1:43:35

So I think it is okay. So what kind of search? So we have created a retriever which will perform

1:43:42

similarity search. Is that point clear to all of you? Also everyone, while similarity search, let's

1:43:47

provide the parameter. What's the harm actually? While performing the similarity search,

1:43:51

what number do we want to maintain?

1:43:54

What number do we want to define?

1:43:56

Tell me that how many similarity searches you want to perform, right?

1:44:02

how top K, right?

1:44:04

Three, you want three similar, five similar, ten similar.

1:44:06

Remember that?

1:44:07

So that you define via this keyword call as search underscore KWRs.

1:44:16

Arguments, search arguments, which is, we will define k value is equal to, let's say, three.

1:44:23

Okay, everyone?

1:44:24

value is equal to three. It means that when you perform similarity search while retrieving

1:44:28

the document, give me top three choices, top three similar choices. And then everyone, we can

1:44:33

for now hard code a query here. Let's say query is the, let's say what is the, maybe return policy

1:44:40

or return window for electronics items. Electronics items. Is that point clear to all of you?

1:44:48

This is, let's say, my query. Is everyone clear? Now what I need to do. In land chain, now it

1:44:54

is very straightforward. You just have to invoke the retriever. Retriever.

1:45:00

Now see the magic now. This retriever, because if you see, this retriever is what? This retriever

1:45:05

is, you have added, you have created this retriever on vector store. And this vector store, everyone,

1:45:12

or automatically has the instance of database. It already knows where the documents or where the

1:45:17

chunks are stored, correct? Vector store already has all this information. And on top of that,

1:45:22

you have created a retriever and you have provided also what type of search you want to perform.

1:45:27

So on this retriever. Dot invoke, you will invoke this query, right? And then everyone, you will have

1:45:33

some output documents. It will give you top three similar documents. Top three similar chunks from

1:45:44

chroma div. How many of you are getting this line? How many of you are getting this line?

1:45:50

Now you can also print this everyone also. Let if you want to print that this is the query

1:45:56

and let's say how many documents we have retrieved. Print the user query and user query is this query.

1:46:09

And you can also print, let's say, retrieve documents and let's say how many documents you have retrieved documents and let's say how many documents you have retrieved.

1:46:20

you can have the curly bracket, length of docs, okay, and add formatting here.

1:46:30

This is what we have added. Is everyone clear? So now, if you want, you can print all the documents

1:46:36

also. That will take a lot of space. That's why I'm not doing that right now. But if you want, you can do that.

1:46:40

Okay? It's perfectly possible. Okay. Now, what do we want? Can I say that now? Everything is ready.

1:46:50

In the last class, in the last, when I say class, everyone, I mean this file.

1:46:55

In the last file, we have implemented all this process, correct?

1:46:59

So don't you think even, this is the pre-processing.

1:47:01

Before you use the rack system, you'll have to load, you'll have to split, you'll have to create embeddings,

1:47:06

you'll have to store them into vector database, correct?

1:47:08

Once this pre-processing is completed, then you do what?

1:47:11

Then you perform similarity search and get the desired data.

1:47:15

Now what is the final thing, everyone?

1:47:18

You just have to build the pipeline.

1:47:20

Correct? Build the pipeline. We should not send it manually to LLM, right?

1:47:25

Pila? We should not directly send it to LLM manually. What we should do now, everyone, is finally,

1:47:31

let's say, land chain, rag, app.py. This is the final application.py, everyone.

1:47:39

And here we are going to build landchain expression language, rag chain.

1:47:45

Okay? And this is going to be very simple, very straightforward.

1:47:50

PathLib, import path, from Lanchine, OpenAI, import chat, OpenEI, and OpenEI Embedings.

1:48:04

From Lanchine, Croma, import, import, Croma, DB, and we want Cromt template also, from Lanchine.

1:48:20

Lanchine underscore core dot prompts, import, chat prompt template. And I think we have

1:48:28

used chat prompt template multiple times. We are all aware of that now. And everyone, we want output

1:48:34

parser also now. A lot of things are required. Lanchine dot, core. Dot output parser, import,

1:48:44

STR output parser. We have used it already. And finally, to invoke, right, we would need Lankchain.

1:48:50

chain underscore 4. To run this chain, we would need. Dot runables, import, runable, pass

1:48:59

through. Okay. Now what we want everyone? We want the place of ChromaDB and collections, this thing.

1:49:10

Okay. And then everyone, we want the LLM model. Let's say LLM underscore model. We want to use GPT.

1:49:20

5.2 because now LM would be required. And then we would need the embedding model.

1:49:28

Okay, embedding model and LLM model we can anyways hard-coded, no worries. Okay.

1:49:35

So we will create the LLM now. LLM is chat OpenAI. Which model we are going to use?

1:49:41

We will use GPD-5.2 and temperature we can set to 0.0.0.

1:49:50

Okay, guys, all of these things we have already used in the past. Okay. And we will create the

1:49:56

embedding model. Embeding model, I have copied. Then we would need ChromaDB also.

1:50:07

Okay? ChromaDB. Then we would need retriever also.

1:50:16

In fact, everyone, there is one more thing that we can do actually.

1:50:20

Can you say that we can import this vector store and retriever and embedding model from this class?

1:50:29

Can we do that?

1:50:31

For example, instead of creating them again from Lankchain hyphen rag, right, we can import these things.

1:50:40

You can do that also. That is also absolutely fine. Okay. But now we will run them individually

1:50:44

so that you can understand well. Okay. I will run the first file, the second file, the third file and then fourth file.

1:50:50

Okay. So now assume that all of these file are completely individual from each

1:50:54

other. Okay. Now, final, everyone, what do we need to do now is we will write a prompt template.

1:51:02

Prompt is equal to chat prompt template. And we all know how to create a chat prompt template.

1:51:08

Chat prompt template. Dot from template. And we will have some prompt template.

1:51:14

Let me copy paste the prompt template.

1:51:20

Okay. Just one thing.

1:51:25

Chat prompt template. Yeah. This is a prompt template that we're going to use here.

1:51:33

Okay. Just look at this everyone. Very standard straightforward. You're a helpful customer support

1:51:40

assistant for an e-commerce company. Use only the retrieved context to answer the user's

1:51:44

question. If the answer is present in the context, answer clearly. If answer is not present in the context,

1:51:49

I don't, please say, I don't know, based on the provided documents, don't use

1:51:54

outside knowledge. Now everyone, as of now, we are just restricting it to use inside knowledge,

1:51:59

right? For example, generally everyone, what generally happens is, I will give you one practical

1:52:03

use case of this. If you go to Amazon chatbot, can you ask any random question that give me

1:52:09

some latest AI news? Explain me agentic AI, explain me hallucination. Can you ask any random

1:52:14

question? No. Because everyone, they have guided their models, please answer the questions.

1:52:19

if that is present in the documents. Don't answer any outside question.

1:52:23

Correct? This is also one type of guard railing.

1:52:26

Okay? This is also one type of guard railing that you are restricting your model to not answer any

1:52:31

random queries. Does it make sense to all of you? Right? Mention the source file wherever possible.

1:52:36

Keep the answer. Now everyone, you are passing the context here. This context is nothing but

1:52:40

the retrieved, the retrieved chunks. We will pass that context and we will pass the question.

1:52:46

Does it make sense to all of you? And finally, we will get the answer.

1:52:48

This is the prompt template that we have. Is everyone clear? Now, finally, build the rag

1:52:57

chain. Okay? In rag chain, we have already discussed in notes. What is a rag chain now?

1:53:05

Rag chain is equal to what all the things will be provided in the rack chain? First of all,

1:53:13

everyone, before even you start, you will have to provide the context. How will you get the context to

1:53:17

everyone? How will you get the context? Basically the retrieved context, right? Retrieved

1:53:24

chunks. You will get it from retriever, right? You will get it from retriever. Correct or not? Retriever

1:53:33

returns the chunks. Okay? And then everyone, you will have, these are the two parameters that

1:53:42

you need to pass. First is the context to the prompt template and the question, the user question.

1:53:47

question. Okay? Question is, let's say, you will get runnable pass-through. What is this? I'll

1:53:55

come to this. I'll come to this. I'll come to this point now. Now the next point, everyone, is that you pass

1:53:59

is that whatever context you have, whatever context you have, you need to pass this inside the problem.

1:54:05

Right? Then after the prompt, you pass it to LLM. After LLM, you pass it to string output parcel.

1:54:12

This is the chain that we have. This is the chain that we need to invoke. Is everyone clear?

1:54:17

Is this point clear to all of you?

1:54:27

Right? Now, coming to this runnable pass-through. Renewal pass-through simply means that Avumar. Now, I think

1:54:37

you can directly hard-cote the question here also. It is not required to use a runnable pass-through because

1:54:42

I'm just using it because Lancchain document is suggesting this to use. Renable pass-through,

1:54:47

simply means that pass the original question as it is.

1:54:58

This means pass the original question as it is.

1:55:02

This means pass the original question as it is as it is to the retriever.

1:55:14

This is the meaning of runable pass-through.

1:55:16

Okay.

1:55:17

Now is anything pending, we just need to invoke the chain.

1:55:21

And finally, to invoke the chain, everyone, what do we need?

1:55:25

Are we using embedding model here?

1:55:31

Embedding model for Embedding model, API key will be required, right?

1:55:35

But we are, okay, if you see, embedding model, we are not directly using it here.

1:55:40

Embedding model is just used for, no, actually in this class it is not required.

1:55:45

We can even remove it.

1:55:46

Okay.

1:55:47

And here, is it required?

1:55:49

No.

1:55:50

Actually, it is not required.

1:55:51

Okay, we can remove it also.

1:55:55

Okay, and finally, everyone, let's say we have a set of questions.

1:55:58

Let's say the first question that we have is,

1:56:02

let's say for now we are hard coding this, and we can use the same question.

1:56:12

This is the question that we have.

1:56:13

And now we just invoke the rag chain.

1:56:16

Finally, get it.

1:56:17

the final answer. Answer is equal to rag chain dot invoke dot invoke this question. Is that point

1:56:28

clear to all of you? And finally, we will print the answer. Everyone, clear? I know, I know everyone

1:56:39

everyone, there is a lot of code that we have written. But if you see, if you close your eyes and see the logic, first

1:56:44

you try to understand the logic, then these things will become.

1:56:47

very easy for you to understand. If you directly look at this, then it might be very complex.

1:56:50

But if you look at the step-by-step process, it's not that difficult. Now everyone, we are going to

1:56:54

we are going to execute these files one by one. Okay. So let's first of all, everyone, execute the first

1:57:01

file and let's call it as, let's say, step number one, right? For your easy understanding, I'm writing

1:57:06

step number one, you can check it. So first, I will execute Python 3, land chain, rag, create corpus.

1:57:15

Okay? Let's execute this again.

1:57:17

There is a file path which is a problem. What is the file path here? Base directory slash file path.

1:57:24

Sorry, file name. Okay, file name. This is a file name. The wrong variable we were using.

1:57:32

And if you see everyone, after this, do you see instantly all these MD files have been created inside

1:57:40

documents folder. Can you see that everyone?

1:57:44

All these MD files have been created successfully in the

1:57:47

the documents folder. Now tell me one thing, everyone. Before the class, I could have

1:57:52

created these files, right? Correct or not? I could have directly created these files,

1:57:56

right? So that you don't even have to write this create corpus code, right? This code, you don't

1:58:01

even have to write it. But I have just shown you how the real production grade application works.

1:58:06

In production grade applications, you don't get directly the files. You get textual data.

1:58:10

Those textual data, you need to write them into the files. This is the code that you use.

1:58:15

Okay? Then everyone here comes as step number two.

1:58:17

In step number two, what do we do? We do all this stuff. Load these documents, split these documents,

1:58:23

create embeddings of these documents, of chunks, and store them into vector database.

1:58:27

So this is basically the step number two.

1:58:30

Step, the file that you need to run in the second step, right? So Python 3, is the first step clear to all

1:58:37

of you? That it has loaded all the documents in the documents folder.

1:58:43

It has loaded all the documents in the documents folder. Simple. That is nothing, that has nothing to do

1:58:47

with RAG, AI, anything. Simple, code, which converted our dictionary into files,

1:58:52

simple. Then I need to run this land chain, hyphen, rag, hyphen, ingest.

1:58:59

Okay? Now, if you see everyone, it is taking some time, because it is loading the documents,

1:59:03

there is some error. OpenAI API key is missing, as expected. Let's go to platform.

1:59:17

create a new API key.

1:59:24

Sorry, demo key, copy the key, copy the key, and export, open AI, API, API underscore key is equal to do this and now, execute this.

1:59:44

Okay? It will take some time, everyone. If you see, original documents are five and chunks are

1:59:50

also five. Why so? Total documents are also five. And each document is divided into one chunk only. Why? Because of

1:59:58

chunk size. We have given the chunk size of 800. But if you see everyone, files are not that big, right?

2:0:04

Files are not, in fact, total 800 size, right? Maybe after the class, when you try this on your own,

2:0:10

what you can try is, you can try to give a lower chunk size, maybe 100, 200, right? Maybe 50.

2:0:14

Make sense, everyone? You can try to do that later. That is your assignment.

2:0:18

Everyone clear. The step now is also clear. Loaded the documents. And now after this step, everyone,

2:0:24

do you see that a chroma DB has been created? Earlier, it was not there. Can you see that? The

2:0:28

chroma DB has been created. And inside this, a collection has been created where you have these

2:0:33

some data, right? Here you have data in this folder. You might not be able to see the data

2:0:38

directly because it stores in the form of, what do you say, the embeddings. But if you see, the

2:0:43

DOM has been created successfully. Is this step also clear? Created the corpus, ingesting the files.

2:0:52

Now we can, we need to perform similarity search. Okay. Now, folks, what we have done is the rag application.

2:0:59

And in this one, once again, embeddings are there, vector store is there. Retriever is there. This is there. And

2:1:04

retrieve chunks are there. Okay. Now I think we don't even need to run this rag application. Rack. We can directly run this.

2:1:12

Right? Because now in this RAG app, right, just look at this RAG app. In this RAG app, what we have,

2:1:17

what we are using is, we are having an LLM model, we are having the embeddings, we are having the vector

2:1:23

database, we are having the retriever, we are having the prompt template, and we have created a chain.

2:1:28

Okay? And finally, we are just giving the query and invoking the chain. This is the final thing that

2:1:32

should get executed with RAG. Okay? Let's clear the terminal. And let's execute Python 3, Python 3,

2:1:40

Lanchine rag-app.py.

2:1:46

It is going to take some time because it is going to use LLM, it is going to use vector database,

2:1:51

okay, and it can throw some errors also.

2:1:54

In it takes, what is the problem here? What is the error?

2:1:57

Base model, in it takes one positional argument, but two were given. And where two were given?

2:2:03

Run.

2:2:10

What is the exact line failing, everyone? Line number 69.

2:2:18

169, 69 may, 169 in 169, you have the query.

2:2:26

Folks, what is the problem here?

2:2:36

Type error, base model.Init, takes one positional,

2:2:40

but two you have given. Where we have given two?

2:2:50

Exo-Athara. Like, this is the internal line. This line number is not in our file. Kishore, this is

2:2:56

coming from serializable.Py. It is internally executing something. Okay, above. Where you

2:3:03

have given? Question for Rack. Yes, this is the question for Rack. What is the problem in this?

2:3:10

Oh, okay, everyone, I think there is one comma missing, okay?

2:3:22

Because it might be taking that in the different way.

2:3:34

Folks, string output parser, this is the class actually, and we have to pass it.

2:3:38

And we have to pass it like this with bracket. I think it should work now.

2:3:44

These are small, small syntax mistakes, even, that you can make. Yeah, if you see everyone,

2:3:48

we are getting the answer. What answer we are getting? Electronics, that is headphones,

2:3:53

keyboards, smart watches, mobile accessories can be returned, can be returned only within

2:3:58

seven days of delivery. And what is the source, everyone? Do you see that? Source is also being added

2:4:03

that this is coming from return policy.md. Go to return policy.md, everyone. Go to return policy.md, everyone.

2:4:08

Go to go to documents, documents, return policy.md, and see, electronic items such as

2:4:15

this, this, this has seven days of return policy. Let's change it 70. First of all, do you see that

2:4:19

the rag application is working absolutely fine? Rag application is working absolutely fine.

2:4:25

Correct or not? Yes. Now there is one more problem that might, that might happen everyone.

2:4:29

If I change it to 70 here, will it change, will it take the changed value? Will it take the changed value?

2:4:37

No, why? Because everyone, these are raw documents. You have to convert these documents into

2:4:42

chunks, then embeddings, then stored into vector database, right? So you will have to ingest again,

2:4:46

absolutely correct. And that's the reason, everyone, that in ingest, first I am cleaning this. Can you

2:4:52

see that? That's why first we were cleaning this. That if there is some data already, which you might

2:4:57

want to clean, because earlier data might not be correct. Now, if you want to ingest the correct data,

2:5:02

clean the, delete the directory, and search it again. Now, what I can do everyone is, let's say in return

2:5:07

policy, you have electronics, products, etc. Let's ask a different question here. That might not be

2:5:12

present in the policy documents. For example, the question is, let's say, what is the return

2:5:17

window for baby items? Okay? Now, this baby item is not present in the rag, right? Let's see what

2:5:24

it does? How our rag application works? I don't know based on the provided documents.

2:5:31

The return policy for the return policy only specifies 10 days window for most of the products. But I

2:5:37

don't specifically know for baby items. Is our rag working absolutely fine? Is our rag

2:5:44

application working absolutely fine? This is what we wanted to discuss. I know we have a lot of code,

2:5:49

but everyone, I could have directly told, directly things, like, for example, it's a document loading. I

2:5:56

could have skipped. I could have directly given you the documents, correct? But that is not how

2:6:00

production application works. In production applications, you do everything from scratch. And this is how

2:6:04

every application works. Is everyone clear?

2:6:07

Is everyone clear? This is how exactly application, real time production grade application works.

2:6:15

Prompt is also working as well, right? Prompt is also working. Because in the prompt, we have given

2:6:19

clear instruction that if the answer is present in the context, answer clearly. If the answer is not

2:6:25

present, say, I don't know based on the provided documents. Also, mention the source file name wherever

2:6:31

possible. Do you see that when we are getting the answer, it is also attaching the source. This is called as citation.

2:6:37

sourcing. Remember in one of the classes, I think we discussed about this, right? Citation and

2:6:42

sources. When you add sources, when you add credible sources, everyone, with the answer that you are

2:6:47

giving, don't you think it increases the credibility of the answer? That now this is not a random

2:6:53

answer that system is generating. This answer is coming based on this source. Is everyone clear?

2:7:02

Is everyone clear? Folks, now see, at least I get very excited when I build these kind of

2:7:06

applications even 100 times. I have built this kind of application maybe at least 20 times,

2:7:11

15, 20 times. But whenever I see this, I get excited that yes, we have built something which is working

2:7:16

in the reality. So you should also have that curiosity that yes, this is how it is working. And now

2:7:23

try to do that on your own after the class. Maybe not today, at least over the weekend, try to implement on

2:7:29

your own. Okay. Then you will get a very clear idea about how step by step system works. Okay, we are done

2:7:35

And with the class, I am adding the code to GitHub, get add, get commit, land chain,

2:7:42

rag app, push.

2:7:49

With all the land chain, rag application is present at this link and notes also I will upload right away.

2:8:05

So guys, you will be able to find the notes at this link. Just try in one minute.

2:8:29

This is the link for notes for today's class.

2:8:35

Okay? Just click on this link after one, two minutes. You'll get it. I am from non-tech

2:8:42

background and coding part seems interesting, but when it comes to writing code, it becomes hard to

2:8:46

remember. You don't have to remember. That is what I'm emphasizing on for last three to four months

2:8:50

now. You don't have to remember. Shaik, if you are from a non-tech background and still coding is,

2:8:57

the coding seems interesting to you. That's a green flag, that you are in the right direction. Now,

2:9:02

what you have to do is you just have to follow the process. Now, even

2:9:05

after writing some code, let's see if you forget about this syntax, no worries, refer it.

2:9:10

The only thing that you need to remember is how this rack chain works. You know that,

2:9:14

this is the context that you have, that you are passing to prompt, creating the prompt template,

2:9:18

then passing to LLM, then passing to output parser to give the final output. If you understand this,

2:9:23

you don't have to remember this complete syntax. For example, I missed this bracket here.

2:9:27

Because I don't remember the syntax, right? If I would have remembered the syntax, I would have given this bracket

2:9:31

in the first step. Okay? You have to understand the flow of the application.

2:9:35

and how they are working, how most of the things are working internally, right? And that is

2:9:41

approach, that is the approach that we're taking in our classes also. We are not just going through

2:9:44

the code. We are not just going through the theory, both the things. In today's class also,

2:9:48

we spend 30, 40 minutes on understanding the concepts. And then we are building things.

2:9:52

This is the right way of learning any concept. Okay. Learn, build. Learn, build.

2:9:58

Okay. How to build anything without remembering? You don't have to see. When you build something,

2:10:04

then people sees that, okay, they will just focus on one screen and they don't refer it. Do you think

2:10:10

this is how anyone, any software engineer in the world works that they don't refer any document?

2:10:16

They don't refer anything? Stack overflow, chat, GPT, Gemini, etc. Do you think so? This is how

2:10:22

any software engineer works in the real world? Not at all. Everyone while writing the code, they refer

2:10:27

documentation. They refer different sources. But quite possible that if you build these applications

2:10:32

maybe five times, 10 times, every day, then you will start remembering these things.

2:10:38

But that is also not very, I would say very, not very appreciated.

2:10:41

Because till the time you will remember, some new thing will come up. Again, you'll have to refer that.

2:10:46

Makes sense, Pratius, Pratush. Okay? So don't try to remember these things. Maybe

2:10:52

try to write the code and you can feel free to refer the GitHub link. Feel free to refer. But

2:10:58

don't copy paste. There's a difference in referring and copy pasting.

2:11:02

If you're copy-pasting, it means you are not learning the step.

2:11:06

But when you are writing line by line, you might get stuck, refer it, then try to read about it.

2:11:11

That this line does what?

2:11:14

Then you will remember it that this is the logic.

2:11:17

Okay?

2:11:18

Within every time, within every time, it will first retrieve the document even when the query not needed.

2:11:23

It will try to retrieve because if you see, we have given the instruction in such a way that don't use outside knowledge.

2:11:30

Okay?

2:11:30

If you remove this, then it may use outside knowledge.

2:11:32

knowledge also. Okay. And if you see, first we have given this prompt here, use only the

2:11:39

retrieved context. Don't use anything else. Okay. If you want to modify the prompt in different way,

2:11:44

you can do that. Right, Chirac? Okay. Folks, how many if you enjoyed the class?

2:11:51

Topics are very interested. What I don't get is where real world I can use. These things will come,

2:11:55

don't worry. People are still figuring out. Companies are coming up with these works on a

2:11:59

a day basis, it will come to you. Okay. Cool. So, folks, I'm launching the feedback poll.

2:12:05

Please take the feedback poll and we are done with the class.

2:12:14

For guardrails, we can also have a rag-like workflow. When we run a local similarity search,

2:12:20

not a separate DB, to see if the query is relevant to the task, an urgent, an agent is meant for,

2:12:26

we rejected. Otherwise, do you like search guardrails?

2:12:29

Quite possible, but I have not seen a rag-based system because rag-based system is quite heavy.

2:12:35

Okay? And for guardrails also, if you're building a rack system, it will increase the cost,

2:12:39

resources, and efficiency of the system. It will improve, like it will affect the, you can say that,

2:12:46

efficiency of the system. It will be a bit heavy application. Okay, latency, absolutely correct.

2:12:54

Okay. Folks, please take the feedback poll. We are done with the class. Once you are done with

2:12:58

the feedback pool, feel free to drop off. Code I have uploaded, notes I have given in the chart.

2:13:03

You can refer it after the class. Thank you so much for attending the class, everyone. Have a good day.

2:13:07

Take care and bye-bye. Thank you. Thank you, everyone. Have you in the next class now on Wednesday.

2:13:28

Okay, I think we are done with the feedback poll from now. We can end the class.

2:13:46

Yes, sir. Thank you everyone. Thank you so much.