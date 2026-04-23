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

Hi everyone, good evening. Well, welcome to all of you.

11:22

Welcome, sir.

11:25

We can start.

11:26

We will wait a couple of bills to get others, and then we can start.

11:30

Yeah, hi everyone.

11:32

Very good evening.

11:33

Thank you, Samia.

11:34

Hey, folks.

11:35

Am I audible to all of you?

11:39

So I guess the chat is not enabled.

11:42

Also, if you could make me host, then it would be good.

11:54

Folks, can you check if you are able to send a message now in the chat?

12:01

Is my screen visible to all of you?

12:13

So, I think chat is not able to all of you?

12:31

Okay, sure, Gora Vravitaja, we will enable the chat.

12:49

So may are you there?

13:01

one or two more minutes, we will enable the chat. And we'll start the class in a couple of minutes.

13:08

Let's wait for more people to join because today's session is going to be very important and

13:13

hands-on session. So let's wait for a minute or so.

13:20

Samya, are you there?

13:31

Folks, give me a second.

14:01

Thank you.

14:31

Thank you.

15:01

Thank you.

15:31

Thank you.

16:01

Hi, Hi, everyone, now, now the chat is able to be able to be able.

16:23

Okay, so, great.

16:26

So, let's get started with the discussion now, today's discussion now.

16:31

And today we are going to talk about how to implement vector search systems, right?

16:36

So, guys, in the last two classes, what all the things we have discussed?

16:40

Can you recall that?

16:43

What all the things we have discussed in last two classes?

16:48

We have discussed about vector embeddings, remember?

16:51

Absolutely correct, right?

16:52

If you see, in specifically in the last two or last three, four classes, we have been talking about

16:58

repetitively about databases, then we talked about.

17:01

vector embeddings, vector databases, et cetera, right?

17:04

So for example, let's say if you see, in the class on 13th of April, we talked about what are

17:09

embeddings, what is similarity, what are similarity search, different types of similarity

17:14

like cosine similarity, ukulean similarity, remember that?

17:17

correct?

17:18

That if you create a vector of a particular sentence of a particular data, and if you try to search,

17:26

you can say that, first of all, what do you do?

17:28

you create vector embeddings of input data, right?

17:33

Your knowledge base, correct?

17:34

Everything you convert into embeddings, you store those embeddings into vector database,

17:39

and whenever query comes in, what happens?

17:41

What do you do?

17:43

When a new query comes in, what do you do?

17:46

You convert that query into vector embedding, and then you perform vector search, correct?

17:51

So based on vector search, what do you do?

17:54

You try to find out the vectors which are very, very similar.

17:58

to the query vector, and then you return top five, top 10, similar kind of vectors.

18:04

Remember this discussion?

18:05

This kind of search is called as similarity search.

18:09

This kind of search can also be considered as vector search.

18:12

Is that point clear to all of you?

18:15

Correct.

18:15

And now, everyone, we know that if two vectors are quite similar to each other,

18:21

their embeddings will be close to each other or their embeddings will be far from each other.

18:26

If two vectors are,

18:28

close to each other, their embeddings will be close to each other.

18:32

Like, if two vectors are similar, their embeddings will be close, right?

18:36

That we understand from, okay, this is already written on the screen itself.

18:41

If two sentences have same meaning, same type of meaning, they will have close embeddings, close vectors.

18:48

Right?

18:49

And when we say everyone close vectors or far vectors, on what basis do we define the closeness of vectors,

18:56

whether two vectors are close or not close?

18:58

How do we measure the closeness that whether these two vectors are actually close or actually

19:04

far from each other based on the angle between the vectors or based on the distance between

19:09

the vectors?

19:10

If you see everyone, dog and puppy, these two are close vectors.

19:14

If they are close vectors, the angle between them is very less, right?

19:17

Dog and orange, these two things are completely different from each other.

19:22

So that's why you see that everyone, the angle is increasing.

19:26

So this is what we have discussed in the last.

19:28

to last class.

19:29

Then everyone in the last class, we talked about vector databases, correct?

19:34

Then we talked about vector databases, correct?

19:38

That we store all these embeddings into vector database, and then we can perform vector search

19:42

using these vector databases, using this vector database.

19:45

Is that clear to all of you or not?

19:49

Okay, everyone clear?

19:52

Now everyone let's talk about the implementation part today, right?

19:55

Today we are going to see the implementation behind these things, right?

19:58

So before we actually go to the implementation, everyone, we can say that, let's just

20:03

try to learn about vectors search a bit more, and then we will see the implementation in today's

20:08

class, right?

20:09

So first of all, everyone, we can say that, yeah, so let's see everyone the complete implementation

20:15

workflow.

20:16

End to end, what are we going to implement?

20:23

Let's try to understand step by step, then we will see the implementation.

20:26

End to end.

20:28

Workflow.

20:42

Folks, just give me a second, let me switch off the fan.

20:46

It is noising.

20:58

Yes. So let's see the complete implementation workflow.

21:08

What should be the first step?

21:09

If you want to search something from any database, what do you need first of all?

21:15

The first step.

21:18

If you want to search something from any database, what do you need?

21:24

Before even location, before even search criteria, what do you need?

21:27

You need data.

21:28

Correct?

21:29

Yes or no?

21:32

First of all, you'll have to store data inside the database.

21:35

Right?

21:36

So you have data.

21:38

Now is this data can be in what format?

21:41

This data can be in what format?

21:44

This data can be in documents format.

21:47

Correct?

21:49

Files format, text format, PDF format, any kind of format,

21:57

kind of format, right?

21:58

So there are a lot of systems out there which can support data in multiple, multiple formats.

22:03

Data can be in images format, data can be in video format, notes format, and whatnot.

22:08

Now the second step.

22:09

Once you have the data, now we will take quite simple example, which is easy to understand, easy

22:14

to implement, which is let's say we will take some files or some documents or some PDF.

22:19

Once you have the data, will you store this data as it is into the vector database?

22:25

Will you store this data as it is into the vector database?

22:32

Tell me.

22:33

No.

22:34

What you'll have to do now?

22:35

You will have to create embeddings, absolutely correct.

22:38

So the second step everyone is to create embeddings.

22:41

To create embeddings.

22:45

To create embeddings.

22:47

So first everyone, what do we do is convert each data item.

22:52

convert each data item into a numerical vector into a numerical vector into a numerical

23:06

vector right now everyone tell me or we can say that numerical vector or vector

23:17

better name is more technical name is vector embedding.

23:21

Now, Shantanu is saying that tokenize.

23:24

Now, guys, if you remember, I think I don't remember exactly, did we take this example or not, if

23:30

you're using any vector embedding model, let's say, for example, let's say there are a lot of models

23:35

out there, just like LLMs, there are different models as well to create embeddings.

23:39

In those models, you don't have to do the tokenization step manually.

23:42

They will automatically take care of tokenization internally.

23:45

So Shantanu is mentioning that, we will have to do the tokenization also, not really.

23:49

If you are using any embedding model.

23:51

They will automatically take care of tokenization. Sounds good. So you don't have

23:55

to worry about really, you don't have to really worry about the concept of tokenization. They

23:59

will automatically take care of. So convert each data item into a vector embedding.

24:05

Now this for these vector embeddings, there are a lot of things out there. You can use a lot of

24:11

models just like you have multiple LLM models, Open AI LLM model, there are multiple open sources

24:17

model also, Gemini, Claude and whatnot. Similarly, for LLM.

24:21

Every company provides a vector embedding model also. You can use some open source model,

24:26

right? You can download some model, you can use that locally, or simply you can also use a model

24:32

from Open AI also. So convert each data item into a vector embedding using some model. Is

24:39

that point clear at all of you? Everyone yes or no using some model.

24:46

Folks, is that point clear to all of you?

24:51

Okay, what is the third step?

24:56

Now we will store these embeddings into vector database.

25:02

They will automatically take care of, Shora.

25:04

See, if you are giving some embeddings, right?

25:06

So see, the point is, if you have to do a lot of customizations, then you will have to take care

25:12

of these things on your own.

25:13

For example, let's say if you want to do a lot of customization in the way of chunking, how do you chunk,

25:19

Then you'll have to do manually, then you might have to write a lot of code on your own.

25:24

But if you don't want to have a lot of complexity in your side, you can just directly use open

25:30

source, some open source or some third party models.

25:33

Now what you'll have to do is, you'll have to go through the documentation of these things

25:37

that how do they take care of, how do they create the embeddings of large documents?

25:41

How do they chunk?

25:42

If that approach is working for you, good enough.

25:45

If not, then we might have to implement these things on our own.

25:49

Okay, but technically a lot of times as a, like if you're building any project or if you're

25:55

building any small application, most of the times we don't do these things on our own.

25:59

Because once you start implementing these things manually, it will take a lot of time.

26:03

Makes sense, sure, yeah?

26:04

So most of the times we rely on third party systems.

26:07

Until or unless your company becomes very big that you can hire multiple people, a lot of people

26:11

can walk on that.

26:12

Okay?

26:14

Okay.

26:15

Absolutely.

26:17

Right.

26:17

So guys now, can I say that now once.

26:19

the embeddings are ready, we need to store these embeddings into vector database, vector

26:23

db. Now there are multiple types of vector db, we'll talk about it, right? So we can say that

26:29

store storage. Third part is storage. What is what is the meaning of storage?

26:35

Store. Store embeddings into vector

26:49

database. Okay? Now everyone, if you just store embeddings into vector database, is that

26:57

sufficient? If you just store these vectors into vector database, is that sufficient?

27:05

Answer is no. Because everyone see, if you just store vector embeddings, right? If you just store

27:12

vector embeddings, and then after, at the time of searching, when you find similar, when you

27:16

perform similarity search. Let's say for some query, right, for some query, you found

27:23

top three similar vectors. Now, will you return these vectors to the user, to the LLM? Do you think

27:29

so? Will you return these vectors to the user? No. Ultimately, what do we need? Corresponding to

27:36

these vectors, we want original text. Correct, everyone? That what is a text? Embedings are used

27:42

only for internal usage. User has nothing to do with embeddings. Correct.

27:46

So can as that, you need to store the original text and their corresponding embeddings.

27:54

Original text corresponding embeddings. So that if this embedding is the answer you want to return

27:59

for any search, then you will have to get the original text corresponding to that.

28:05

Then you will use this original text to generate the actual answer that you are going to return

28:09

to the end user. Everyone clear with this? Folks, yes or no? Correct. So what all the things

28:16

we need to store in the database, we need to store original text.

28:23

Original text. Then everyone, we need to store vector embedding for each text, for each file, each chunk,

28:31

each document, whatever. For each original text, we need to store their vector embeddings. Then everyone,

28:37

we need to store some kind of unique ID also. For each original text, for example, let's say,

28:43

in simple words, you can say that, to each document, we will assign a unique idea.

28:46

Otherwise, how will you uniquely identify each document in the system? Similarly, everyone,

28:52

in SQL database, do you assign a unique ID or a primary key to each user, each student,

28:57

each entity? Similarly, you might assign a unique ID to each document so that you can uniquely

29:03

or easily identify that. Also everyone, we will store some metadata, correct everyone? We will store some

29:11

metadata for each document. Why do we need to store metadata? And what do we mean exactly?

29:16

by metadata.

29:17

Metadata is like?

29:20

Metadata is like?

29:25

Meta data is like?

29:31

data about data.

29:34

Right?

29:35

In the last class I think we talked about metadata, right?

29:37

Did we talk about metadata?

29:39

Okay, I think in this class, if not, let me give you some brief understanding

29:50

about metadata. Okay, so this meta data is nothing but data about data. Now, there's a lot of times,

29:55

don't you think for each document, if you store some extra information, for example, let's say the category

30:02

of this document, when this document was added into the system, who added this document, this,

30:07

what is the summary of this document? Very small amount of data.

30:09

But if you have this data, then it can add a lot of value to your search system.

30:14

Correct, everyone? Meta data, the meaning of metadata is data about data.

30:18

So in the document, you have a lot of data.

30:20

Let's say for example, you have one document about the company policies about maybe let's say return.

30:25

For e-commerce website, let's say in one document you are storing companies return policies for any product.

30:32

Now if you store and you have thousands of such documents for different, different categories.

30:37

Now everyone tell me, if you do you do that you just,

30:39

just maintain small data, small metadata, that okay, what is the category of this document?

30:45

Now, if any query comes in and you can identify the category of the question, of that query,

30:50

now if you just, before even you perform the similarity search, if you can just filter the documents

30:57

based on the category. So don't be even out of thousands of documents, you might be able to filter

31:02

out, maybe 99% of the documents. That? Because if the category of the question, if the query belongs to,

31:09

Return policy. Now, do you really need to go to, let's say, Amazon Prime Video. Let's say, for example, Amazon is maintaining this database, that the policies related to Prime Video, policies related to Amazon Pay, policies related to something else, seller, etc, etc. Do you need to even go through those many documents?

31:28

If you just store the category, are you guys getting what I'm talking about? You can store some small metadata about each document so that you can even perform better search.

31:39

Now, is this metadata actually mandatory? Is this metadata actually mandatory? Not really, right? Even if you don't store, it is okay. But if you store this metadata, then definitely it can make your system much, much more efficient. How many if you're clear with this? There was one question, I think. I'm not able to find it now. Okay, anyways. Clear? Perfect. So these are the things, everyone, that we will store inside the vector database. Now, what are the different types of vector database, everyone?

32:09

Simply everyone, for relational databases. We have different types of relational databases like MySQL,

32:15

MSSQL, PostgreSQL, etc., etc. Similarly, vector databases are the databases which provides us

32:21

the capabilities of storing vector embeddings. Make sense? The capabilities of storing vector embeddings.

32:28

Now, there are different examples of vector databases, right? For example, let's say one of the most commonly used and

32:34

one of the most easiest to use is chroma db. Okay? Which you can simply insert.

32:39

install in your local machine and you can use it. There are other things also like pine cone,

32:43

etc. But we will use one of them, which is chroma database, chroma db. Is that point clear to all of you?

32:48

I will show you how to install chroma database using the libraries, how to use it via the code,

32:53

etc. Okay? Like we save genre, target audience, absolutely correct. For example, what could be

32:59

the metadata about a movie, the genre of the movie, the actors of the movies, right? Maybe different

33:04

subtitles, the category of the movie, right? When this movie was released, what is the duration?

33:09

of the movie, et cetera, et cetera. Make sense, everyone? Okay, will we store the structure

33:14

formats such as original text, vector embedding, unique ID? Kind of yes, Ramsey, but mostly all of these

33:19

things might be, will be handled by different type of databases in their own way. So what we will do

33:24

is we will create one kind of data structure, right? And in this one data structure, we will

33:28

give this document, right? Document as well as, as well as the metadata. And this document, for this

33:36

document we will create the embeddings then all of these things we will push to

33:40

chroma database to any vector database so internally it will automatically maintain that okay

33:45

this is the database or this is the document original text this is the metadata and this is the

33:51

vector embedding corresponding to this makes sense everyone okay the fourth step everyone is

34:00

query what the fourth step is

34:06

What is the meaning of query? Query means when user ask a question, correct? User asks a question, a query. Now, is to find the similar kind of answers for this particular query. Don't you think this query we should also convert into vector embedding? This query we should convert into vector embedding. Then we will perform the similarity search or vector search? Yes. So user ask a query and

34:36

And we convert this query, we convert this query, we convert this query into embedding into embedding, everyone clear?

34:58

is everyone clear with the fourth step as well?

35:02

Then the fifth step, everyone is everyone clear with the fourth step?

35:05

is perform similarity search or retrieval. Perform similarity search.

35:12

Right? So guys, in similarity search, what do we find out? We find perform, you can say that.

35:21

Search, perform search operation, search in vector database, search in vector database, and find out

35:35

top K, top 5, top 10, top 20, top 1, top 2, whatever. Top K, nearest neighbors.

36:05

the query embedding. Is that point clear to all of you?

36:20

All of you? Folks, these are the five steps that we perform in any vector database, entire

36:31

entire flow. How many if you're clear till this point of time?

36:36

So if I summarize what we have discussed. So initially we have data. Data we convert

36:43

into embeddings. Embedings, we store into database, store into vector dv, then we get a query.

37:00

query again we convert into embedding.

37:07

This embedding, using this embedding, we perform search operation, perform search operation.

37:29

And finally, everyone, return the answer, return the response.

37:40

Everyone clear? So how is top K related to search? Top K means what?

37:45

For example, let's say, if you have to find out the answer of any query. For example, if you have

37:50

any query, you have to return the answer. So how do you find out the answer for that particular query?

37:55

You find out the vector embeddings, which are very, very close to this.

37:59

Correct? There might be millions of embeddings you have, right? You might have millions

38:04

of embeddings. So you have to find out the embeddings which are closest to the query embedding.

38:09

But how many embeddings you need? Maybe three, maybe five, maybe seven, or maybe ten. Now,

38:15

once you have, let's say, you have decided that top five, you will find the closest five embeddings

38:21

with respect to the query embedding. Once you have the top five closest embeddings, you will

38:27

return these embeddings to the LLM, LLM will generate the answer using these embeddings

38:32

and return to the user. Is that point clear to all of you? It's about the retrieval

38:37

strategies, absolutely correct. Shandranu, is that point clear? Perfect. Which one would be

38:44

performance search for CRUD? Performance search operation. Performs search operation.

38:50

Performs search operation. Performs search operation means perform similarity search.

38:52

Once you have the query embedding, you need to find the similar kind of vector. You need to find the similar

38:56

kind of vectors, the nearest vectors for this vector embedding, right?

39:02

Makes sense? This is the whole idea of creating embeddings.

39:06

Performs search operation means perform similarity search via cosine similarity,

39:11

Euclidean similarity, whatever. Will we have something like tables in the relational database?

39:15

Not exactly tables, but yeah, what it does is it creates a slightly different structure internally.

39:20

We don't have to go in the details of how does vector database stores the data actually

39:24

in the database internally. But you can understand.

39:26

that it also creates some kind of structure where for each document you create, you store the original

39:32

text, you store the embeddings, and you store the metadata about the document. Now, these vector databases,

39:38

they are highly optimized for certain kind of operations. What these are certain kind of operations are

39:44

to find the closest vectors with respect to the given vector. No, no, no. How is that related,

39:53

Shantanun? Top K, top P, those are sampling.

39:56

approaches, right? Here you are trying to find out the nearest vectors, right? Maybe you can try to find out some

40:02

correlation that may be similar kind of thing, but these are slightly different things. These are

40:07

related to vector databases. Those are LLM operations, LLM parameters. Sounds good?

40:20

Folks, how many if you're clear? Guys, have we discussed this? Tell me, just really.

40:26

this line. Have we discussed this line at least 5 to 10 times? Tell me.

40:30

Absolutely. In which class did we learn about cosine similarity? Okay? Go to the class which

40:42

happened on 13th, 13th of April. Go to this class and here, here we talked about similarity.

40:49

Okay? Yeah. If you see, the vectors which are similar in meanings, they will be.

40:56

be close to each other. Close means they will be placed in the vector space. In the vector

41:02

space, they will be present together. They will be present near to each other, right? The vectors

41:07

with different meanings, right? They will be present far from each other. How do you measure the closeness

41:13

of two vectors with respect to the angles? If there are these two vectors, a dog vector and a puppy

41:20

vector, these are two very similar things. And that's why you see that both of these things are

41:24

present together, very, very close to each other. Because their angle is less. You can calculate

41:30

the angle. Internally, the systems are there, there are libraries, there are functionalities which

41:35

provides you this thing. You don't have to do this manually. But how does this work internally? You can

41:40

calculate the angle between them. If the angle is less, it means they are similar, they are close.

41:45

If the angle is very high, if the angle is very large, if you see this angle, this angle,

41:50

between dog and orange, these are completely unrelated.

41:54

things. Dog is an animal. Orange is a fruit. Orange is a color. These things are not at all

42:01

similar to each other. And that's why you see that dog vector and orange vector. They are very far from

42:07

each other. Is that point to all of you? Or you can also calculate, like, euclidean similarity. How do

42:16

you measure similarity? Two things. Distance and angle. Angle like this. And distance, you calculate via

42:22

are Euclidean distance, right? So, distance like this. Distance between these two

42:28

vectors is less, so they are similar. Distance between these two vectors are more, so they are not

42:33

very similar. Makes sense, everyone? How many if you are able to recall now?

42:44

Folks, yes, no, yes, no. Okay, very good.

42:52

Now everyone, let's talk about, so this is the entire flow. I hope everyone is very, very

42:57

clear with the entire flow. Now what we are going to do with, what we are going to start with,

43:02

the starting of development environment. Before I actually dive deep into the actual implementation,

43:09

I want all of you to be comfortable with what, actually, what internally what we are going to do,

43:15

right? So I just don't want to throw the names in the class that, okay, use this, use that,

43:20

install this. First, we should be very much clear with the idea that why, that what are we

43:24

using, why we are using. Now everyone, what we are going to do is, first let's talk about

43:29

development environment setup. Development environment setup. Development environment setup.

43:36

So basically we are talking about before we go into the implementation, I want to show you what

43:45

all the things do you need for implementation, development. Development means implementation.

43:50

So, okay, now, first of all, we are going to write code in Python, correct?

43:56

Correct or not? We will write code in Python.

43:59

First everyone, if you see, we will have the data. Assume that I will give you the data, okay?

44:05

Data is very easy thing to get. We will have some sample data. Makes sense, everyone?

44:12

Once we have the data, we need to convert that into embeddings. Correct or not? We need to convert that

44:18

into embeddings. Yes or no?

44:20

Now everyone, in the development environment, we need to create embeddings.

44:28

Now, these two embeddings, to create embeddings, there are multiple ways.

44:32

Let me show you two most popularly use ways.

44:35

One everyone is you can install a Python library called as sentence transformers.

44:41

Guys, now where I give the name of these libraries, please don't stick to only these libraries.

44:48

There might be hundreds of other libraries.

44:50

libraries. I'm giving you the names of most popularly used libraries. So there is one library called

44:55

a sentence transformers. So this library, everyone, gives you a way to create embeddings automatically.

45:04

Sounds good? So this library gives you a way to create embeddings automatically. Or everyone,

45:11

you can use, so using these models even, this is, you have to install this library in local and then it will work.

45:18

Obviously, if you want to use any Python library, will you have to install it in your local

45:23

environment, in your local laptop, and then you will be able to use it? Correct?

45:28

Correct?

45:29

First way. That you can install this library using Python, PIP3, install this library. I will

45:35

show you that way also and you can use it. Other way everyone is you can use some third-party library,

45:41

third-party API, like open-party library.

45:48

AI embedding model. Okay? So guys, open AI, I think in one of the classes I showed you

45:55

as well, right, open AI documentation. There is a large model, there is a small model. Remember

45:59

that? There is a small model of open AI and there is a large model by open AI. Small model

46:07

has how many dimensions? 1536. Large model has how many dimensions? Double of this,

46:12

3072. Okay? So you can use open AI models also. You can use open AI embeddings.

46:18

Third party like Open AI embedding models.

46:23

Now, any one of them we can use.

46:26

Which one do you want me to use?

46:27

Which one you are more interested in?

46:29

In seeing the demo?

46:30

Do you want me to show you this thing or this thing?

46:33

Second one, more practical.

46:36

This is more practical.

46:38

Because, guys, open AI gives you very, very realistic view.

46:42

Open AI gives you more realistic view.

46:45

No worries everyone, I will show you one of them.

46:47

I will show you one of them and second one I will add in the notes. You can take reference from there.

46:53

I will show you whatever is more practically used in the industry, in the class, in the life class, and other thing, right?

47:01

The counterpart, for example, let's say I will show you this thing. This I have already added in the notes.

47:06

So if you want to say this, you can refer the notes. No worries. Or anyway, I can show you this also.

47:11

The point is I have added both of these things in the notes. You can refer it from there.

47:17

Folks, yes or no?

47:20

So once you have the embeddings, everyone, now you need to store these embeddings into the database.

47:25

To store these embeddings into the database, what do you need?

47:29

To store these embeddings into the database, what do you need?

47:34

You need database.

47:36

Okay?

47:37

You need a vector database.

47:39

So guys, there are a lot of examples of vector database.

47:42

We will see one example which is most commonly used.

47:46

used, the name of this vector database is ChromaDB.

47:50

Okay?

47:51

So, ChromaDB, everyone, is one of the most widely used for local implementation.

47:57

Local implementation means everyone that we are not going to host this database on some cloud

48:03

server, on Amazon, Google, etc.

48:05

I want this database to be present in my local laptop, in my local machine.

48:09

So it is a good choice for local implementation.

48:13

Make sense?

48:16

Folks, CSNO, this is a good choice for local implementation.

48:31

For this everyone, you will have to install this chroma database in your laptop.

48:35

How?

48:36

I will show you that.

48:38

And then you can use it directly in your local machine.

48:41

Okay?

48:43

Fine.

48:46

So yes, Chroma database supports all the major operations, like you can add documents,

48:52

you can update documents, you can add embeddings, you can update embeddings, you can store,

48:57

you can say that, you can store metadata and whatnot.

49:00

All the common operations, all the important operations it supports.

49:04

Now I think we can get started.

49:05

Okay?

49:06

Yeah.

49:07

So could you please give some good examples of production-grade vector databases?

49:11

See, Chroma database is also a very good example of production grade databases.

49:15

For example, AWS,

49:16

provides its own vector database. I don't remember the name, but all the major cloud

49:21

providers, they provide their own vector databases, okay? So let me show you that.

49:27

Most common, there is one pine cone, there is one other as well, most common

49:35

vector databases for production.

49:44

Superbase also gives one of them.

49:46

right yeah so pine cone is one quadrant is one right open search is one mongo db atlas right

49:54

mongo db all of you know mongo db database all of you know mongo db database so mongo db database has its own

50:02

cloud called as atlas now mongo db also supports vector database so what happens everyone is like

50:08

when something becomes popular right when something becomes popular every company would

50:12

want to implement that functionality so that they can hire they can they can they can they can

50:16

have more customers right so now it is almost every system supports it right do you

50:22

remember everyone we had a demo of pg vector do you remember we had a demo of pg vector

50:30

in one of the classes that are not in your batch right uh pg vector is also one of the use cases of

50:36

a vector database is using postgres right that was a different uh class okay but how do you

50:44

you use pg vector how do you use uh chroma database same thing so these are some of the most

50:49

commonly used examples okay okay we are configuring to return top k results is is this nothing

50:57

but yes if n is nearest absolutely right so you can find uh top five top 10 so this is

51:04

k nearest neighbor search okay for optimization you can perform this approximately if you want

51:10

exact results you can perform accurately

51:14

okay one class per day and not even regularly okay uh like along with office work

51:26

it becomes very difficult to take even one class so i don't even take on an average one class

51:31

every day so sometimes i have one class sometimes i don't have okay so what happens everyone

51:38

is like for different courses the syllabuses are different agree for example now in this particular batch

51:43

this is the batch where we are focusing more on the agentic systems so there are

51:47

different batches in which different things are being taught right but if you see in this particular

51:53

course we are having a wide variety of topics covered is that concrete all of you

52:04

so we are going to use chroma database if everyone is clear we can start with the

52:08

implementation and one more thing you want that what we are going to build right now is that we will

52:12

create sample documents i will have these documents in the system i will give you

52:17

that then we will generate the embeddings stores them in chroma database then okay let me

52:22

write it down what are we going to implement okay first is we have sample documents then we have sample documents

52:42

then we generate embeddings then we store these embeddings into chroma db.

53:12

chroma db then everyone uh if once we get the query convert the query

53:20

the query into embedding

53:27

fifth is perform similarity search

53:42

this this is now we want to move to the code directly directly so what we have done to implement step by step

53:48

step everyone clear everyone clear okay so now everyone let's move to the code directly so what we have done

53:56

everyone is what i have done already is i have created one project with the name of vector

54:00

search okay i have created one sample project from with the name of vector search and in that i have

54:07

initialized a virtual environment how many if you know about virtual environment how many if you know about

54:16

virtual environment okay if not uh let me tell you that because virtual environment is like a as a

54:24

as a name such as virtual environment what can happen is that quite possible that in your

54:29

laptop you are running multiple python projects possible you are having multiple python

54:35

projects in your laptop now is it possible that for the same library for the same library one

54:40

project needs a different version other project needs a different version in the same laptop in the same

54:47

machine possible you need a different version of the same library in different projects

54:54

Now, how will you do that?

54:55

Let's say in one project you need X version, in other project you need Y version.

55:01

So how do you tackle this situation?

55:03

In one laptop, in one machine, you can have only one version of a particular library.

55:07

So how will you solve this problem?

55:10

You solve this problem by creating multiple virtual environments.

55:14

You can say that.

55:15

Very simply, you can understand that virtual environment is like a small computer, a small virtual

55:21

computer that you are creating within your computer.

55:24

Now inside that virtual computer, inside that virtual environment, you can install any kind

55:30

of dependency that will not interfere with other virtual environment.

55:34

So all the virtual environments are completely independent of each other.

55:38

So what you can do is, you can create one project, create a virtual environment inside

55:42

that project, create project 2, create another virtual environment inside that project.

55:46

Now what happens is these two projects are now completely individual, independent of each other.

55:51

You can go inside project one, install.

55:54

the X version of some dependency.

55:57

Now you can go to Project 2 and install the same dependency with a different version.

56:01

Now you can have two different versions of the same dependency or of the same library

56:06

in two different projects at the same time without conflicting, without interfering with each other.

56:12

Make sense everyone?

56:14

So you are saying that, you can see that you can create a virtual environment for a particular project

56:18

which is completely independent of other projects.

56:24

it takes space, obviously it will take space, but it will not take a very big amount of space.

56:28

Maybe few embis.

56:29

Now, ultimately it will depend on how many dependencies you're installing inside the virtual

56:34

environment.

56:36

Virtual environment itself is kind of a boundary only, a virtual boundary.

56:41

So when you buy a plot, what do you do?

56:43

You put a fencing so that no one can enter inside the boundary, right?

56:46

That is something like virtual environment.

56:48

So you have created a boundary outside this project.

56:51

That whatever is there inside this project will remain.

56:54

inside, right? And now you create another project. You create another boundary

56:58

outside that project. So these two projects are completely individual of each other,

57:02

completely independent of each other. How close I was when I mentioned create separate

57:08

files. Kind of same thing, not separate files. You can say that these are virtual things.

57:13

When you create a file, right, file is something which is present in the laptop.

57:18

These are virtual boundaries only. Okay? These are imaginary things.

57:24

Virtual environment, it is understood that you are creating a computer inside your computer.

57:29

But it is not actually something physical. It is just logical. Make sense?

57:34

Everyone clear? So how can you create a virtual environment?

57:39

How can you create a virtual environment? For example, this is the command.

57:54

I have already added these commands in the notes also, everyone. So you

58:01

can copy paste these commands from the chat also. So first command is to create a virtual environment

58:06

Python 3-M, V-E-N-V-N-V-N-B. And then you can activate the virtual environment using the second

58:12

command, source. Okay? So what I can do is, let me create, I have already created a virtual environment.

58:17

So I will create a file now in this system. File name is let's say, what do you say?

58:24

sample or vector underscore db.tty. Okay, this is our file. And here I can give this

58:33

in the comments, this thing. Is that point cleared all of you? Okay. Now what do you need

58:41

everyone is, first step is to install chroma DB. Okay? So what is the command to install

58:49

chroma DB? PIP3 install.

58:54

ChromaDB. Once you install this, it will take some time. Okay, I already have,

59:06

if you see, the requirement already satisfied. I already have this, uh, chroma d be installed in my

59:11

laptop. So that's why it is already there. It is just, uh, trying to update it, upgrade the

59:17

version. And that's fine.

59:24

Sometimes, RM, it's very important for you to visualize things in your mind.

59:29

Right? So for example, let's say what happens? Like if there is a hall, right? If there is a big,

59:34

you can say that a big building, right? How do you give individual spaces to every person?

59:40

You create separate rooms. You can consider that virtual environment is like that room.

59:46

Make sense?

59:50

Sometimes it's not practically possible to visualize everything.

59:54

on the laptop, right? On the system. Sometimes you'll have to visualize by understanding

1:0:00

in your mind that, okay, virtual environment is like a room that you are giving to every student

1:0:05

in the hostel. That is their personal space. Personal space, now that is completely independent

1:0:11

of other students' room. Can installation inside virtual environment available globally? No.

1:0:17

That particular virtual environment, whatever you install inside the virtual environment, that is

1:0:20

going to be there inside the virtual environment only.

1:0:24

Okay? Yes. If you want to use the same library in other virtual environment,

1:0:28

you'll have to install that again. Okay? Everyone clear? So how we have installed ChromaDB?

1:0:35

Okay? Okay. Folks, yes, yes or no? How difficult is it to say yes or no?

1:0:54

no. Understood? Perfect. Now I'm, I don't want to go ahead without taking a consent

1:1:00

from all of you. Otherwise, it might be difficult for you to catch up. Okay? Second thing,

1:1:04

everyone, that we need is we need to install the library to create embeddings. Now, to create

1:1:08

embeddings everyone, as I discussed, either we can use a transformers, right? We can use open AI API,

1:1:15

open AI, API, right? Open AI API. Or we can use sentence transformers.

1:1:24

library. Okay? Let me tell you one. So some of you were saying that, okay, we should

1:1:30

take this approach in the class or we should take this approach in the class. Let's do one thing. I

1:1:34

think we will have time. So let's take both approaches in the class. Sounds good. Let's take

1:1:39

both approaches in the class. So first, what I will do everyone is we will have to install this

1:1:43

sentence transformers library in our, in our virtual environment, in our project. So what we

1:1:48

will do, PIP3, install, sentence.

1:1:54

PIP3 install sentence transformers. Okay? Install this. It will take some time.

1:2:04

So it is already there in my system. Requirement already satisfied. Done. Now everyone, we will be able

1:2:09

to use both of these libraries in our virtual environment, in our project. So what we will do?

1:2:13

We will import chroma DB. ChromaDB, if you see it is available. And then from

1:2:19

sentence transformers, we will import the class which we are going to use to create embry.

1:2:24

which is called a sentence transformer, right? We will use this. Everyone, clear?

1:2:31

Okay? Now everyone, we are going to create sample data. Prepare sample data. Now, guys,

1:2:39

in order to create sample data, at least can I say that maybe at least five or six documents

1:2:45

should be, we should have of different, different categories so that we can check whether we are

1:2:50

getting the right answer or not. If you just have one document, two documents,

1:2:54

of the same category, you will obviously receive the same answer. But if you have let's say

1:2:59

at least maybe five or six documents, also they should have different kind of data, different categories

1:3:04

of data. Then only you will be able to realize that, okay, whether we are getting the correct

1:3:08

data in the output or not. For that anyone, so that we don't spend this time in the class, what I have

1:3:15

done is I have created this sample data of around five or six documents. Okay? Otherwise it will

1:3:20

take at least 15, 20 minutes to write this one by one. Let me. Let me. Let me.

1:3:24

Let me walk you through this data, what this sample data is all about, we have created a records.

1:3:29

Okay? This is the name of the data, records. And this is a list, correct? Correct. I go? The square

1:3:34

bracket, right? List. Inside this list, what we have is, we have one document. So, ID is document one,

1:3:41

doc one. And then we have the text. What is the text? Customer can return products within 30 days of

1:3:46

delivery. Is the first document create all of you? And then we have metadata. Meta data is another, you can say

1:3:53

that dictionary where we are defining the category of the data, that category of this

1:3:59

document is returns category, and source is, let's say, policy document. Let's say, this is coming

1:4:04

from a company's policy. Is the document one clear to all of you? Is the document one clear to all

1:4:10

of you? Simple, right? Very simple. It is nothing but a list and a vector, a list and a, a list and a

1:4:17

a JSON or a dictionary, nothing but. Then everyone, we have document to, document two, document.

1:4:23

2 may we have another document which is refunds are processed within 5 to 7 business days

1:4:29

after return is approved. Category of this document is returns again and source is policy.

1:4:36

Then another document 3. Now this is a different category. Orders above 499 are eligible

1:4:43

for free shipping. So this is document 3, category is shipping, source is FAQ, frequently asked

1:4:50

questions. Document 4, this is category account, sources, help center. You can receipt your

1:4:56

password from the account in the settings page, whatever, okay? Then express delivery, shipping,

1:5:01

FAQ. Then there is a payments document as well. So do you say that we have around, we have six

1:5:05

documents, two belongs to returns category, right? Two belongs to shipping category. One belongs to

1:5:12

to account category. One belongs to payment category. Is that one clear to all of you? Is that data

1:5:18

clear to all of you?

1:5:20

Okay?

1:5:22

Using sentence transformer, its data or these records into the vector database.

1:5:37

What do we need?

1:5:38

We need to create embeddings, right?

1:5:40

Create or we can say that, yeah, create embeddings.

1:5:50

convert documents into embeddings, correct, everyone?

1:5:59

Folks, yes, no? Now, before we convert documents into embeddings, we will have to decide the model,

1:6:06

model, or we can say that, we can, we will have to load the embedding model, which model we should

1:6:14

use for embedding. Okay? For that, everyone, we will use model, is equal to

1:6:20

Sentence transformer. We will use this class and we can use different models are there.

1:6:25

We can Google about it. One model is this. A small model which will be more efficient, we can

1:6:32

use this. This is one model that we can use directly, which is coming from sentence transformer.

1:6:37

Does that make sense to all of you? So this is the embedding model, which we are going to use

1:6:43

to convert our documents into embeddings. Is that point clear to all of you? Yes or no.

1:6:50

Okay? Now, do you remember that in just a second? Yeah. So now once you have these records, right? If you see, in the code only, you have these records. Now, do you need to create the embeddings of ID, text, or metadata? You need to create the embeddings of what part of the text.

1:7:19

what part of the input data, ID, text or metadata? Only text. Now can I say that everyone,

1:7:27

that from this records list, we should extract the text information separately, ID information separately,

1:7:36

and metadata information separately. Tell me yes, no. Take documents separately.

1:7:42

Correct? So what we can say that? The documents are what?

1:7:49

are nothing but create a list of from the records, get the item text.

1:7:59

Right? Text for record in records. In records. How many if you're able to understand this link?

1:8:11

So basically what we are doing is, if I write this in simple terms, it is for each record in record in

1:8:19

records list, what we should do is create a documents list, empty list, and we can say that

1:8:26

inside documents, please append every text, okay? You can say that, records say every record

1:8:34

to get the text component and add it inside the documents. So is this code and the above code

1:8:41

same everyone?

1:8:41

Now I think you should have this much of clarity on Python that the above code

1:8:52

and this code is same. So what you are doing is you are iterating over each document, each record

1:8:58

inside the records list. Records is nothing but what is each record? What is each record? Don't

1:9:04

you think each record is a dictionary? Each record is a dictionary? Get the text part of each record.

1:9:11

and add it inside a separate list. Now in this documents, everyone, in this documents list,

1:9:17

you just have the text part of each record, clear or not. Clear or not? Clear or not?

1:9:27

Right? Similarly, everyone, you will take IDs, you will take, you can say that metaDas. So you can

1:9:33

say that. Now for IDs, everyone, I will write the same code. Now I think it will make a lot of

1:9:41

sense to all of you now. And similarly, for meta data, I will write the same code that

1:9:46

meta data, metadatas is equal to this thing. Correct even? Similarly, we have documents, right? So

1:9:56

better if we understand this code. So that we have same type of code for all the three parts.

1:10:05

Everyone aligned till this point of time?

1:10:11

Now what do we need to do? Now we need to create embeddings. Okay? So document, let's

1:10:20

say document embeddings is equal to, we will use this model and we will call the function

1:10:29

call as encode. Encode is a function which will give you the embeddings. Now, out of these three

1:10:35

data's, documents, IDs, metadata, for what type of data do you want to create the embeddings?

1:10:41

For what type of data we need to create embeddings? We need to create embeddings of

1:11:06

create embeddings of documents only, right? We need to create embeddings for documents only.

1:11:12

Just a second. So we will pass documents here.

1:11:22

Documents. Then we want one thing that we need to do is that tell me that once you

1:11:29

create these documents, do you want to, do you want the model to create the embedding?

1:11:36

of all the documents inside this array, inside this list, because documents is a list,

1:11:41

right? Correct? And inside this document, you will have this part, first document, second document,

1:11:49

third document, fourth document, and so on, correct. So what is this documents? Don't

1:11:55

you think this document, this document's list is a list of documents where each element

1:12:02

inside this documents list contain a document itself?

1:12:06

the text itself. Tell me, yes, no? Correct? Now everyone, if you want to use

1:12:14

this sentence transformer and you want this model to behave that, okay, what you want to do? That

1:12:21

this is the document's list. What this model needs to do? What this model needs to do? It needs

1:12:26

to go to each and every element of the document in this list and create the embedding for that.

1:12:30

For that, everyone, you need to give one separate parameter, which is called as convert to

1:12:36

Numpai. This we need to give true. Now, do you remember that we had a class on NNPi long

1:12:41

back in the last module? Now, what is NUMPI? NUMPI is nothing but everyone. It makes it easier

1:12:49

to access to work on list. Makes sense? It provides you a lot of functionalities. What this

1:12:57

does everyone is that if you give convert to NUMPI is equal to true, whatever it is going

1:13:01

to encode, you will get the data in the form of NMPI. Simple.

1:13:05

Right? Numpai array. And once you have the Numpai array, you can convert this into list.

1:13:10

Is that point clear to all of you? So now everyone, after this right side, once you do this,

1:13:16

you will have a list of embeddings. So where everyone? This document embeddings, what it will

1:13:21

contain? First, it will contain the embedding of document 1, then it will contain the embedding of

1:13:27

document 2, something like this. For example, embedding of document 1, embedding of document 2, embedding of document 2,

1:13:32

embedding of document 3, embedding of document 5, 4, 5 and 6. This kind of list you will receive

1:13:39

in the output. So this will be your document embeddings. Have a look at it and tell me if this is

1:13:45

making sense to all of you or not. Now, now, some of you might be worried that, okay, Deepak, how will

1:13:55

I remember this? Do you need to remember this? No, you need to understand this. Always, if you take a reference from

1:14:02

any online documentation, chat, GPT, or wherever, you will get this code as it is.

1:14:07

But you should be having this confidence that you should be able to understand this.

1:14:10

What this is doing? It is just converting the document array into NUMPI so that basically

1:14:15

what NMPI does, right? NMPI gives you an easy way to work with list, right? Simple, right? NMPi

1:14:22

is not a rocket science. What NMPai gives you? NMPi gives you a lot of functionality to work on

1:14:26

arrays, right? You convert this documents into NMPi array, encode this, and code this, and find

1:14:32

finally you are converting that NAMPi array into list. This is the syntax that it follows.

1:14:38

Make sense? Yes, Ravitha, it is pretty scalable. Don't worry about it.

1:14:44

Makes sense? So guys, do you want to go through this code? Should we take a break right now? If it is

1:14:49

becoming overwhelming for some of you, should we take a break? Okay, so it's all like it's okay,

1:14:55

it's more than 9. It's we are ahead of 9 p.m. So let's take a break everyone. So it's almost 9-899. So let's

1:15:02

Let's take a break till 912, 12, 12 minutes, 920, 921. Let's meet around 920 or 921 and then we will

1:15:10

discuss further. So maybe I'm leaving this on the screen. You can have a look at it. Okay?

1:15:15

See you in 10 minutes ever.

1:15:32

Thank you.

1:16:02

Thank you.

1:16:32

Thank you.

1:17:02

Thank you.

1:17:32

Thank you.

1:18:02

Thank you.

1:18:32

Thank you

1:19:02

Thank you

1:19:32

Thank you

1:20:02

Thank you

1:20:32

Thank you

1:21:02

Thank you

1:21:32

Thank you

1:22:02

Thank you

1:22:32

Thank you

1:23:02

Thank you

1:23:32

Thank you

1:24:02

Thank you

1:24:32

Thank you

1:25:02

Thank you

1:28:32

Thank you

1:28:36

Hi

1:28:40

I'm

1:28:47

Hi,

1:28:49

I'm

1:28:50

I think there will be there will be

1:28:53

Hi everyone, I am I am I'm

1:29:04

I think there will be some class let me check with the schedule and I'll I'll check with the

1:29:07

let me check the schedule and I'll I'll I'll check and update okay I think mostly there should be some class. Okay? I think mostly there should be some class. I think we had one class.

1:29:14

I think we had one class on Claude right already.

1:29:17

Right.

1:29:21

You can refer that as well if you want

1:29:23

maybe in future also we might have some session right reach out to the support team

1:29:28

I think from the dashboard or from the email ID whatever works.

1:29:32

I'm using Python 3.1.2 running into issues installing Chrome RDB, failing to build Pandas

1:29:41

when getting requirements to build a wheel.

1:29:44

Did you create a new virtual environment?

1:29:46

Create a new project, create a new virtual environment, start from scratch.

1:29:49

Most probably it might be interfering with the existing dependencies, okay?

1:29:53

If you have done everything from scratch, still you are getting the issue, then I think you should copy paste this error to GPT and see what error it is all about.

1:30:02

I have never seen this error, so please check.

1:30:06

Okay, so should we start even that as of now, we have created the embeddings.

1:30:11

Now once we have created the embeddings, what should we do?

1:30:15

We should store these, store the embeddings.

1:30:23

into chroma db.

1:30:27

Store these embeddings into chroma db.

1:30:29

Before we store these embedings into chroma db, don't you think we need to create an instance,

1:30:34

create a client for chroma db?

1:30:37

How can you access chroma db, right?

1:30:39

As of now, you have just installed chroma db.

1:30:41

How will you use that?

1:30:43

So you can say that client is equal to chroma db that you have imported,

1:30:49

import chroma db, this one.

1:30:52

Chroma db.

1:30:53

dot persistent client and then everyone because you want a local chroma db you can give a path

1:31:02

simply like this quotes dot slash chroma store so i will show you that even like

1:31:11

chroma db or whatever chroma store whatever name you want to give when you give this dot slash

1:31:17

what it does is it will create a database in memory database a local database

1:31:22

with chroma db a chroma a local database using chroma db in the current location

1:31:29

when i say current location it means that in the same location where this file is because you are

1:31:35

giving dot slash dot slash dot slash means current folder and when we will run this code everyone

1:31:41

you will see that there will be a file or there will be a database that will get created with the name of

1:31:47

chroma db is that point clear to all of you yes or no

1:31:52

is that point clear to all of you yes or no okay now let's try to store them

1:32:02

right so what we will do client this client chroma dv client dot the function name is get get or create

1:32:18

collection i will talk about this what this function does first let's try to understand

1:32:22

what do we need to pass inside this just give any name to uh to this database let's say

1:32:29

we call it as uh let's say amazon or let's say uh maybe what we can say that let's say knowledge

1:32:41

vector db this is the name of the database makes sense everyone inside chroma db this is the

1:32:46

name that we are giving and then everyone another parameter that we need to give is called as

1:32:50

embedding function that we need to pass now now what this function does everyone

1:32:58

is that first of all if you see get or create collection inside one chroma database you can have

1:33:05

multiple collections right multiple parts for example let's say one collection you are storing for

1:33:10

one use case other collection you are storing for other use case and so on simply everyone in one

1:33:15

my SQL database can you have multiple tables you can have multiple tables right similarly here

1:33:20

Here also you can have multiple collections.

1:33:23

You can decide that, okay, let's say in one collection I will store one type of data, other collection

1:33:26

I will store for different use case, different type of data and so on.

1:33:29

So what we are doing is get or create collection.

1:33:32

What is the name of the collection?

1:33:33

This is the name of the collection.

1:33:35

Now this get or create as the name suggests, if there is already a collection with this name,

1:33:41

use that, get it and use it.

1:33:44

If there is not a collection with this name, then create a collection with this name.

1:33:50

Making sense?

1:33:50

If there is already a collection with this name, use it, if not create it.

1:33:56

Then everyone we are giving embedding function is equal to none.

1:33:59

Now everyone tell me, do I want chroma database to create the embeddings or we have already

1:34:06

created the embeddings?

1:34:08

Do I want, do we want, Chromea database to create the embeddings?

1:34:13

Answer is no, right?

1:34:14

We have already created the embeddings here.

1:34:17

So that's why we are giving embedding, embedding function is equal to none.

1:34:20

Because, everyone, Chroma database also gives you some ways to create embeddings internally.

1:34:26

But we don't want to use that.

1:34:27

We are using external way to create embeddings.

1:34:29

Make sense, everyone?

1:34:32

Does it make sense?

1:34:35

Okay.

1:34:36

Then everyone, what we do is, if you see, we have created a collection, we have the embeddings ready.

1:34:42

Now what we need to do, store this thing, okay?

1:34:47

Here we can see that, this is first we need to create a collection.

1:34:50

Create a collection.

1:34:51

And then everyone, we can see that.

1:34:54

Store the embeddings into collection.

1:34:57

Right?

1:34:58

So what we will do?

1:34:59

Collections.

1:35:04

Sorry.

1:35:06

Yeah.

1:35:07

Collection.

1:35:09

Then everyone, we do, what should we do?

1:35:13

Insert operation, right?

1:35:15

Collection dot insert.

1:35:17

Even if we don't mention about embedding function, will it

1:35:20

create an embedding audit's own by default. I think so. I think so. I will have to go through

1:35:25

the documentation, but better practices, good practices. Always if you want, if you don't

1:35:29

want Chroma database to not generate the embeddings, better to make it false. I don't know

1:35:35

the default behavior. We will have to check the documentation that what default behavior

1:35:39

it supports. But yeah, better if you pass none, if you don't want to use it. Okay. So guys,

1:35:45

inside a collection, what we will do, collection dot insert the embeddings now. Correct, you

1:35:49

one, that what all the things we want to insert? So, yes, there is no insert function here.

1:35:54

If you see, there is no insert function. There is a function called as absurd. Okay? I think insert

1:36:01

also is there, but absurd function is what absurd function is. Do you know what absurd function is?

1:36:09

Absert function stand for update plus insert. Now what this does everyone is, so for

1:36:15

for example, what upset function does is, if you're trying to

1:36:19

something. For example, let's see if you're trying to insert a particular document with some ID.

1:36:24

If you change something in that document with a particular ID, ID will not change, right? If you change some

1:36:31

content, some text inside the document. Now, if the document is already there, if you change something,

1:36:37

obviously the embedding will change, then if you again try to insert the document, updated document,

1:36:42

inside the CromaDB, what do you think? Should it insert it again or should you update the

1:36:47

existing document. Should it insert again or should it insert or should it update the

1:36:53

existing document? Obviously update it. Also everyone, if you're trying to insert a document with a

1:37:00

particular ID, if that ID does not exist in the collection, that ID does not exist in the database,

1:37:06

then it should insert. So can we say that everyone that if the ID, if you're trying to

1:37:12

insert a document with a particular ID, if the ID is already present in the database, it means that you're

1:37:17

to update something, then it should automatically update. Correct? If the ID is not present,

1:37:23

then it should insert. Yes, and everyone? So you should handle this scenario already, right? So first,

1:37:29

what you should do? Check the ID. If the ID is already present, call the insert function. If the

1:37:34

ID is not present, call the insert function. Make sense, everyone? ID present, update function,

1:37:39

ID not present, insert function. Yes or no. You will have to do this manually. But to avoid this,

1:37:47

this everyone, there is a function called as absurd. Most of the databases, they

1:37:51

provides you absurd function. What it will do? Whatever ID you will provide here, if you

1:37:55

see, there is an ID, whatever ID you will provide here, for example, you say that ID is

1:37:59

equal to some doc 1. It will check that if document 1 is already there, it is an update

1:38:05

operation, it will try to update, else it will insert. Is that point clear to all of you?

1:38:09

Yes or no. Okay? Now what do you need to do everyone is? Very simple. You can

1:38:17

Now, should we insert all the documents one by one?

1:38:20

Document one, document two, document three, document four, and so on.

1:38:23

Should we do that? You can do that. If you want, you can definitely do that.

1:38:26

You can do something like this, that for each record, right, for, let's say, I in the range of, I in the range of 0 to 6, right?

1:38:35

As of now, we have six documents. Okay.

1:38:38

Then you can say that collection dot insert, right? Insert. Then insert like this.

1:38:44

Is this a practical approach? If there are millions of.

1:38:47

of documents, will you write this code again and again? Obviously not. It is not a very good

1:38:53

approach. So everyone now, this collection also supports that you can, it allows you to insert multiple

1:38:59

documents, multiple embeddings in one function call. How you can provide like this, IDs.

1:39:08

So what are the IDs, everyone? IDs are, these are the IDs, right? Let's say, let's call them as

1:39:15

document IDs. Make sense everyone? Let's say document metadata. Right? So what are the

1:39:23

IDs, everyone? Ids are these IDs. So it gives you function like this, that provide the IDs,

1:39:31

doc IDs. Then you can say that documents, that is text is equal to where you have stored the documents

1:39:41

inside these documents. Right. Then everyone, you need to store the documents.

1:39:45

metadata. Metadata is equal to document metadatas. And then finally

1:39:52

everyone, you will store embeddings. Embedings. What is the name of the embeddings? Document embeddings.

1:40:00

So guys, what you do? You are providing arrays here. So what it does, everyone, it will iterate

1:40:05

automatically. So first ID, first document, first metadata, first means first index. So first index ID,

1:40:13

then first index's document, first index metadata, first index can embedding. They will be

1:40:18

inserted together. Then it will go to the second index. Second index key, ID, second index

1:40:23

document, second index's metadata, second index embedding. It will insert in one go. Getting the point.

1:40:29

So you don't have to write any for loop, anything like that. It will automatically insert all the

1:40:33

the documents, all the embeddings, all the metadata in one shot. Is this line also clear to all of you?

1:40:43

all of you. Okay? Now everyone, how do we verify that whether the data has been inserted

1:40:49

or not? How do we verify whether the data has been inserted or not? So first, everyone, what

1:40:54

you can do is you can simply print something, let's say, print, you can try to print the collection.

1:41:02

That how, what is a count inside the collection? How many records have been inserted? So you

1:41:07

can say that. Let's say something like this. Number of

1:41:13

number of, you can see that number of documents or number of records in collection.

1:41:23

Right? Then you can give comma, collection.com. Is that one clear to all of you? It will give you

1:41:31

total number of values inside the collection. Is that one clear to all of you? Yes or no?

1:41:37

Okay, we have not created this collection of that, right? Create this collection

1:41:45

is equal to this. Make sense? Okay, there is one more function everyone. Yeah, if you want

1:41:57

to store, if you want to print all the records, you can also print like this. Print, print like this. Print.

1:42:07

records in the in collection. You can print like this. There is a function

1:42:16

called as peak, comma, collection dot peak. Okay, if you call this function collection dot peak,

1:42:22

what it does is, it will give you the first record, then second record, then third record,

1:42:27

then fourth record and so on. Right. So now using these two things, we will be able to verify

1:42:32

that whether the data has been inserted inside the collection or not. How many if you're clear,

1:42:37

with the code as of now. So if I summarize what we have done is we have, we installed,

1:42:43

import ChromaDB, import this, then we have these records, then we loaded the model, then we extracted

1:42:51

the data, then we created the embeddings, created the client for ChromaDB, created a collection,

1:42:57

inserted the data inside the collection, and then we are trying to test, trying to verify whether

1:43:01

the data has been inserted or not. Now what we can do? We can clear the terminal and try to insert, try to

1:43:07

this code, right? We don't need a connection for vector database. If you see, this

1:43:13

is the connection only. There are different ways for every database to create the connection. This

1:43:19

is how the Chroma database gives you a way to create the connection, okay? Because this is a local

1:43:24

database, okay? So guys, let's try to run this code, Python 3 vector database.ty. Guys, give me

1:43:32

a thumbs up. If we should run this code. If everyone is comfortable, give me a thumbs

1:43:37

very good it will take few seconds of time because we are creating the

1:43:45

embeddings and embeddings will obviously be a slow process it will take few seconds okay let it

1:43:50

run okay let it run okay there is some error what is this error list indices must be integer

1:43:59

Okay.

1:44:01

But the problem here?

1:44:04

record a type error not string.

1:44:32

Okay, I think we need double, double quotes.

1:45:02

Let me check this. It is saying it should be integer. No, no, no, no, no,

1:45:11

so it is a, what do you see, records may.

1:45:32

Got it. So because if you see, records is a list. So records, if you want to go to first, yeah, actually, that's correct. So let me just verify this once.

1:46:02

Actually, this is the wrong way. I understood this. So you will have to iterate over the record and then record of record dot get zero, right? And then get text. Correct everyone? Because record is a list. So first you have to iterate in the list, then go to zero element in the list. From that, get the text, add it in the document, right?

1:46:30

Yes, no, everyone.

1:46:32

Then go to the, what do you see? The second, the first index, from the first index, get the text. Correct or not?

1:46:41

First integer and then, are you guys getting what I'm saying? Yes, two for loops. Not exactly, one for loop, but the way that we need to do is that if you see, records is a list, right?

1:46:54

So first we will need to go to this element. Then inside this, this is a dictionary. Every element inside the records list is a dictionary.

1:47:01

Records is not a dictionary. So go inside every element record, then get the text.

1:47:06

So I'm just trying to figure out the right way. Right? So this thing.

1:47:31

How many if you're clear with the error here?

1:47:37

At first, records is a list. First, we need to iterate over the list, every element in the list.

1:47:43

Every element inside the list is a dictionary. Then you will be able to access the dictionary.

1:47:48

Records directly is not a dictionary. Okay? Folks, yes, absolutely. Right.

1:48:01

If you see this records, right, we need to do this. That's it. My bad. That's it.

1:48:07

Right? We are going to every record. Then every record is a dictionary. Then we can do what? That record of text.

1:48:15

Makes sense, you know? That was a typo. Actually, thank you, Pila. You figured out that. I thought that we are already using records.

1:48:24

Clear. Right? So what we will do? Now we will try to run.

1:48:29

This single quotes, double quote, does not.

1:48:31

matter.

1:48:40

What is the problem now?

1:48:42

Collection.Opsert got an unexpected argument embedding.

1:48:46

Okay, then what is the name of the argument here?

1:48:48

The name of the argument?

1:48:49

Did I make any typo?

1:48:51

Embedding.

1:48:52

Embedings, not embedding.

1:48:54

This is embeddings.

1:48:56

Okay.

1:48:57

Yes.

1:48:58

Correct everyone?

1:49:00

Correct, everyone?

1:49:01

If you are giving IDs, documents, metadatas, you need to give embeddings, not single embedding,

1:49:09

list of embeddings.

1:49:10

Let it run.

1:49:12

Yeah.

1:49:13

Now if you see everyone, the embeddings are ready.

1:49:16

Is that point clear to all of you? Embedings are ready?

1:49:19

Yes or no?

1:49:21

Now what are we printing everyone?

1:49:22

First of all, if you see, number of records.

1:49:25

How many records do we have?

1:49:27

How many records do we have?

1:49:28

Six records.

1:49:29

Right?

1:49:30

Stored record in the collection.

1:49:32

See the first record.

1:49:33

First, everyone, we have IDs.

1:49:35

Ids are document 1, document 2, document 3, document 4 and so on.

1:49:40

Then everyone we have embeddings array, where we have 6 arrays, right?

1:49:45

So first embedding, then second embedding, third embedding, 4th, 5th, and 6th.

1:49:52

Correct, everyone?

1:49:54

Total, how many dimensions do we have?

1:49:58

do we have?

1:49:59

384 dimensions.

1:50:01

Each vector has 384 elements, and then everyone the original text.

1:50:06

And then everyone, we have metadata.

1:50:08

That what is the metadata for the first document?

1:50:12

Sources policy, category is written, second meta data, third document, third document, and so on.

1:50:17

Is the data type clear at all of you?

1:50:20

But yes, data is getting inserted absolutely fine in the database.

1:50:24

So as of now, our code is running fine.

1:50:28

point clear to all of you.

1:50:29

Okay.

1:50:30

Now everyone, let's say now we are getting the user query.

1:50:38

Now you see that now our application database is ready.

1:50:42

Now let's say everyone we are getting the user query like this.

1:50:45

Let's say user query.

1:50:46

Now let's say you want to, let's say user is asking query something related to refund.

1:50:51

Let's say the query something like this.

1:50:53

I want a refund or let's say I want to return my sugar.

1:50:57

my shoes and get my money back.

1:51:04

This is the user query.

1:51:06

Now guys, don't think these are the queries, these are the type of queries that we give to Amazon

1:51:10

or Sviggi or Zepto like that, right?

1:51:13

That I got a bad item, I got defective item, I got damaged product, I want my money back, correct?

1:51:24

In a very raw way.

1:51:26

Can I say one like convert this, convert the user query, convert the user query into

1:51:35

embedding?

1:51:36

Yes on everyone?

1:51:38

Convert the user query into embedding.

1:51:41

So let's say query embedding.

1:51:45

Now this query embedding, how will you do that?

1:51:48

Can I say that we will have to use the same model with which we created this embedding?

1:51:55

folks yes or no exactly copy paste and now this user query same thing right

1:52:02

this same thing now this user query is just one one thing because you are converting this

1:52:11

into list we can convert this like this right that this is a single string right we can

1:52:16

convert this into list like this make sense now we need to retrieve what

1:52:25

Or we can see that perform similarity search, similarity search.

1:52:33

Guys yes, no, perform similarity search.

1:52:37

So let's say result, results is equal to collection.

1:52:41

So there is a function called as query.

1:52:44

Inside this query, you can pass the query embedding, query embedding is equal to this.

1:52:49

And inside this query embedding, you need to give something called as end results.

1:52:53

That how many items do you?

1:52:55

you want in the result. You need one item, you need four items, like 10 nearest

1:52:59

items, two nearest items, one nearest item, and so on. So let's say everyone, we need three nearest

1:53:06

items. Is that concrete to all of you? We need three nearest items, correct? Then everyone,

1:53:13

you can try to print this, print, let's say, top three results with respect to user query

1:53:24

Okay, user query. Let's say first you try to, you print the user query, and then everyone

1:53:32

you say that user query, and then you say that, this, okay? After this, you print the results.

1:53:43

This is how you can do that. Is that point clear to all of you?

1:53:47

Okay, these results, everyone, these results, right, it will contain a lot of things. But to the user,

1:53:53

you will have to return only the documents, the text. I will show you how can you do that.

1:53:58

Okay, but is the idea clear to all of you? Okay, even if you don't want to do this, right?

1:54:04

Okay, top three results, forget about this. Let's make it very simple for all of you. Okay, forget about

1:54:09

this. That just print these three results. Top results. Does that make sense if you know?

1:54:21

Let's try to print.

1:54:23

Everyone clear till this point of time?

1:54:27

Everyone clears?

1:54:28

Okay. Now what we will do?

1:54:30

Clear the terminal and again try to them.

1:54:34

Let's see what you get in the results.

1:54:36

Then we will try to get the actual answer.

1:54:38

That what do you actually need?

1:54:40

Because the results will have a lot of data.

1:54:42

Okay.

1:54:43

Very good.

1:54:45

So finally you see that everyone.

1:54:48

Top three results.

1:54:50

Okay. So actually do one thing before this.

1:54:52

let's put some separator otherwise it is not very visible.

1:55:12

So if you see everyone, first you are getting document two.

1:55:17

Let's see what you are getting in document two.

1:55:20

Now the question is about, if you see the top three results, right?

1:55:21

If you see the question is about return, that I want to return my item, I want to return my product, and I want get my money back. I want to get my money back. In the entire sentence, have I used the term return, the term refund? Have we used the term refund in the in the query?

1:55:40

Answer is no, right? We have not used the word refund. But if you see the documents everyone, ideally what should we get? Can I said we should get the items which are

1:55:51

close to which are similar to return and refund.

1:55:55

Correct everyone?

1:55:56

Because user is talking about return and refund.

1:55:58

I want to return my product and get my money back.

1:56:01

So if you see everyone, the closest item, if you see the closest item is documented too.

1:56:06

Because it is containing the word return as well, containing the term refund as well.

1:56:15

Get my money back and refund. They are the same thing.

1:56:18

Getting the point.

1:56:19

We are getting the point.

1:56:20

document 2 as a closest answer. If you see, there is it? Yeah. We are getting

1:56:33

document 2 as the first answer. Getting the point. Top result is document 2. And do you

1:56:38

say that even? Document 2 is the highest matching item. The most similar item is document 2 only.

1:56:45

How many of you agree with this? Then second item.

1:56:50

that we are getting is document 1. Why document 1? Because document 1 is talking about return.

1:56:55

It is not talking about refund. That's why it is coming at position 2, not at position 1.

1:57:03

Then we are getting document 6. Because document 6 is talking about something related to payment.

1:57:08

Although it is not related, but still it is coming in the output because you are asking about top 3.

1:57:13

If you ask about top 6, obviously all 6 will come. Correct or not? Obviously all 6 will come.

1:57:19

Yes or no?

1:57:20

keep on increasing the number of items top 10, top 20, top 100, top infinite. Obviously the number

1:57:26

of items will keep on coming in the output. But if you want the exact output, that's why you need

1:57:31

the K value to be very, very precise, not very low, not very high. How many if you're able to

1:57:37

understand this fact that yes, similarity search is working absolutely fine. Now if you make the

1:57:43

value of n result is equal to 1, that you want top 1 result only. That give me the item, give me the document,

1:57:49

which is a maximum matching, most similar.

1:57:53

Now guys tell me, because there are only five or six documents we have, right, you can easily find

1:57:58

out that if the user is asking about that I want to return my shoes, please return my money,

1:58:03

please, please, I want my money back.

1:58:06

Out of these six documents, which is the document, which is maximum similar, which document

1:58:11

is the most similar answer, most similar document.

1:58:15

Document 6, here it is talking about payment, there is no concept.

1:58:19

of return here. There is no mention of return. There is no mention of return or refund

1:58:23

here in the document 5. In document 4, it is completely unmatched, right? Document 4 is talking

1:58:29

about password reset. Document 3 is talking about shipping. Document 2 is talking about refund. Refund

1:58:36

means money back and return also. And now if you execute the code with n value is equal to 1, it

1:58:43

means that you want the top 1 result only, the document which is maximum matching, you will only get

1:58:49

document 2. Getting the point, everyone. How many if you're getting that? How many

1:58:53

if you're understanding that similarity search is working absolutely fine? How many if you are

1:59:00

getting this point? There will be functions, Sharia, right? For example, if you see, it is, it might be

1:59:06

doing internally exact search. If you go through the documentations of ChromaDB, it will also

1:59:11

also give you other functions also, like query. There might be other functions also. Okay. Does metadata

1:59:18

play any role, I'll come to that. I'll come to that. Folks, how many of you are 100%

1:59:24

clear till this point of time? If yes, then we will move forward. I will show you one more thing.

1:59:30

Yes, at the end of the class, HP, I will share this link, share the code. Okay? Now everyone, let's

1:59:35

say, now let's say everyone, there is another query, the user query underscore 2, which is let's say, the query

1:59:43

something like this. Let's say, once you have placed an order, the query is something like

1:59:50

this, that how fast my order will arrive or how fast I will receive my order, something like this.

1:59:58

How fast my order will arrive. Or how fast my order will arrive. Or how fast I will receive my order.

2:0:08

Is the query clear to all of you? Is the query clear to all of you?

2:0:13

Okay. Now again everyone, what will we do? We will create the embedding.

2:0:21

Query embedding to change the query. That's it. And finally, everyone, we will

2:0:27

results to. Results to. And then everyone, we will see that query embedding to. We will change the query embedding. And then we will execute. And then we will execute. And finally, we will try to print results.

2:0:43

2. Or here we will see results. Let's print it. Let's comment it out. And then we

2:0:52

will print results 2. Okay. Now if you see everyone, I have changed the query. Now tell me everyone,

2:0:58

if I find top three answers, out of these six documents for this particular query, how fast I

2:1:05

will receive my order? What will be the answer? What will be the answer?

2:1:13

Which document is the maximum matching? Document 5.

2:1:20

Document 5. Correct? Express delivery usually right within 24 to 48 hours. Correct? And there is one more shipping, right? Yeah. Yes, no, everyone?

2:1:31

So if you are getting the top one answer, let's see if you're getting the top one answer, then you will only get document which number? Document 5. Correct? Doc 5. So now.

2:1:43

Execute this. You should get Document 5 as an answer, which is the nearest answer.

2:1:51

Then I will show you even more interesting thing.

2:1:54

Correct. Document 5 is coming. Let's make it Document 2. Let's see top two results. Now we want

2:2:01

document 5 will anyways be the will be in the answer. It will be the nearest answer. Now if I ask you that

2:2:08

out of other five documents, 1, 2, 3, 4 and 6.

2:2:13

What should be the next answer? What should be the other nearest answer?

2:2:19

After document 5, what will be the other nearest answer?

2:2:23

Which document is talking about shipping, delivery, arrival, etc?

2:2:29

Document 3. In this, everyone, are we using any word like fast, shipping, fast or arrive, etc? No.

2:2:39

Still, if you see from human logic, from our understanding, we can say that, it is very

2:2:43

similar, right? So let's see. I don't know whether document 3 will come in the answer or not.

2:2:48

Most probably it should come. Let's see. Let's verify. Now we are getting top two answers.

2:2:53

Okay? So document 5 should come and document 1 is coming. Document 1 is what? Document 1 is coming.

2:3:02

Because if you know, why document 1 is coming? Because it is talking about days.

2:3:06

It is talking about days. Because everyone here if you see, here it is talking about shipping. It is okay. But

2:3:12

But if you understand the similarity here, internally what embedding is calculating,

2:3:18

it is talking about rupees and it is talking about orders above this much value. Then they are

2:3:24

talking about free shipping. Here, the tenure is not mentioned when the order will be received. But

2:3:30

here even if you see, here we are talking about days. So internally inside the embeddings, it might

2:3:34

be recalculating that, okay? Document 1 is matching more than document 3. That's why,

2:3:42

1 is coming in the output. But anyways, I think this is making sense to all of you, right?

2:3:48

Does it make sense to all of you?

2:3:53

Correct. Now if you see document 1, although it is not a good idea, right? Ideally document 1 should not come in the answer.

2:4:00

Although it is coming, we cannot control that because might be this embedding model might not be accurate, might not be very good.

2:4:06

And that's why companies keep on improving their embedding models time to time.

2:4:09

But you can still try to improvise it, try to improve it.

2:4:11

try to improve it by putting some filters. What filters you can put is, you can put a

2:4:16

a wear clause. Where close we have already seen in SQL classes that we can put conditions.

2:4:20

Now let's tell me here, this query is talking about what? Can I say that this query is talking about

2:4:28

shipping? Can we say that? This query is talking about what? Talking about shipping. The category

2:4:35

shipping. So can I put that? Please find the result of this where the category

2:4:41

category is shipping. How many of you are getting this point?

2:4:48

Now don't you think even if you put filters, then it will make your query even more powerful.

2:4:54

Yes or no. It will even more, it will even make your query more powerful.

2:5:01

Right? So I think Mukul was talking about it. What is the use of metadata? This is the use of meta data.

2:5:06

Now if you put filter, that means even you are even neglecting, maybe.

2:5:11

maybe 99% of the documents. You're not even going through that. You're only focusing on the

2:5:16

documents which are belonging to the category shipping. Now clear the terminal, try to execute

2:5:22

the query, and then you'll see that now, you will only get the output in the, you will only get the response

2:5:27

in the result, the documents which belongs to the shipping category, not any other, not any other

2:5:32

thing. Now document 5 and 3 are coming. Is that one clear to all of you? Now document 1 is not coming,

2:5:37

even if it is matching more. But still, because you are filtering based on the category,

2:5:41

only shipping documents are coming. How many of you are able to understand this thing?

2:5:46

Okay? Now everyone, let's say, let's try to see one more thing, right? Then we will,

2:5:57

then we are done with the class. Just five more minutes. Let's say, everyone, we insert one more record, right?

2:6:02

Let's say, I already have that record ready so that we don't have to write. If I ask a question which is not there in the document, will it return null?

2:6:09

It will not return null because if you see there.

2:6:11

If it is not making, it is not doing exact match. If you talk about any random thing, let's

2:6:18

see if you talk about something like, let's say Iran versus USA, right? It is not matching to anything.

2:6:24

It is not related to anything. But still everyone, if you see, it is, you can say that, it is comparison-based

2:6:31

approach. It is not exact match. Now if you try to find a vector, right, if you try to find the

2:6:37

distances, similarity, and then you try to find out top K. The exact similarity will be

2:6:44

lesser, but still out of that also, if you try to find top K, something will come in the output.

2:6:50

Right, Vamsi? Something will come in the output. But if you want that, okay, if you want to remove

2:6:56

the non-matching things, then you can put a filter like category. Okay, it is a relative search.

2:7:02

Okay, it is a relative search. Okay, it is a relative search. Take it. Now, let's add a new record.

2:7:07

Let's say everyone, this is a new record we have, right? Document 7. And the text is canceled.

2:7:12

Orders are refunded to the original payment method. Okay? And the category of the document is payments and the

2:7:19

source is policy. Now what we need to do is we need to create an embedding of this document. How new, let's

2:7:26

say new embedding. New embedding is equal to model dot encode.

2:7:37

Then convert to numpi is equal to true. Dot tool list. Okay? Created a new embedding.

2:7:45

And now what we need to do, you know? Can I say this new embedding, we need to insert in the same

2:7:50

collection? Yes or no? This new embedding, we need to insert in the same collection. So what we

2:7:55

will do? Collection.comert. Collection dot absurd. What this absurd will do? It will try to match the

2:8:02

IDs, right? Let's say IDs is equal to what? What is the ID? We can say that new records,

2:8:07

let's say, we have to pass in this format, new records' ID part. This is the ID. Okay? Then everyone,

2:8:16

we have to pass documents. So, text, basically. So new record.

2:8:27

Text. Then metadata.

2:8:33

And then finally, everyone, embedding. And then embeddings.

2:8:37

is equal to embedding. Is that point clear to all of you? This is how we can insert

2:8:44

the new record, a new document, correct or not? So now what we can say everyone? Now we can try

2:8:52

to print, now we can try to print the data once again, right? So after this, yeah. Now after

2:9:00

inserting this one new record, everyone, how many records we should have? As of now, if you see,

2:9:05

there are total six records, right?

2:9:07

Total number of records, six. Now, how many records we should have?

2:9:14

Now, how many records we should have? Okay? So let's try to print. Let's try to execute.

2:9:32

Okay? Now finally even just see the number of records.

2:9:37

some, okay, we are getting some error. What is the error we are getting?

2:9:42

Hmm. Did I make any mistake? There must be some typo everyone.

2:10:07

Oh my bad. Guys, if you see this new embedding is already a list, right? So we are passing list inside list. So this is just new embedding.

2:10:23

I know? Just new embedding. This new embedding is already a list. Getting the point. So let's execute

2:10:32

execute this. Because if you see this new embedding, we are already converting this into the list, right? And I was

2:10:37

writing this in the square bracket. That was the error. Okay. Now do you see that even?

2:10:41

How many records do we have? Seven. Make sense? So update, absurd, insert operation also

2:10:47

working fine. Okay? Now what we should do? Now let's give another query. The another query is

2:10:53

slightly different. Let's say user query three. The user query three is that something like this,

2:11:00

let's say how will I get the refund? Okay? Okay.

2:11:07

like this. How will I get the refund? Is the query making sense for all of you?

2:11:10

You? How will I get the refund? Let me try to add one more sentence. How will I get the

2:11:21

refund for a cancelled order? Okay? Now everyone if you see, what is the seventh document? If

2:11:29

you see, cancelled orders, so obviously what I have tried to create the query in such a way that the

2:11:35

7th document should be the highest matching document, right? It should be the highest

2:11:40

matching document. So what I will do? I will again try to make the query. So get the results. Results

2:11:46

3. We will change this. So query embedding. First we will have to create the embedding of this.

2:11:56

query embedding, let copy paste.

2:12:04

Query embedding 3, model.ncode, query 3, convert to

2:12:09

numpy true and spine. Once we have the query embedding, what we will do?

2:12:15

We will pass this query embedding into the query function. Let's say we want top one result. Now,

2:12:20

do we want the category is equal to shipping? Do we want the category is equal to shipping? No.

2:12:26

Category should be payments, you know? Category should be payments.

2:12:33

Makes sense? Because we are talking about the payment here. We are talking about the refund.

2:12:40

And then everyone finally, what we're going to do is we will try to print the results.

2:12:46

Let's make it results three.

2:12:52

Everyone clear what changes we have done here.

2:12:56

Everyone clear what changes we have done here.

2:13:03

Okay? Pop it. See we are getting only one result. So document 7 obviously is the highest match.

2:13:17

Document 6 we are getting why we are getting 6? Why we are getting 6?

2:13:25

If your payment fails, try another card.

2:13:30

Guys, very strange, right? We are getting document 3. Document 6 as an answer.

2:13:36

We are talking about cancelled order. We are talking about refund.

2:13:40

Okay? And everyone, document 6 is what? Document 6 is talking about what?

2:13:45

It is talking about payment fails. Okay? So guys, somehow if you see, it is not a very good model.

2:13:53

Correct?

2:13:54

Make sense? Because the number of dimensions are only 384. Correct? Yes, it is talking

2:14:02

about cancellation, failure as the same thing, but this is a drawback. It is not a very good model then.

2:14:07

Right? And that's why everyone, the companies like Open AI, they use models with very high

2:14:14

number of dimensions. But I hope the thing is the idea making, I hope the idea is making

2:14:18

sense of you. Okay? If you make top two results, then obviously document 7 will 100%

2:14:24

come. Because everyone, one more thing, right, if you see in the results, right, distance

2:14:27

is also coming. That what is the distance between the query vector and this vector? So if you see the

2:14:33

query vector and the document 6, they had a distance of 1.4 and it is having a distance of 1.8.

2:14:40

Second is document 7 only. Make sense? I'm pretty sure, I'm 100% sure that if you try to change

2:14:48

the model from this small model, right? We are using very mini model. Which model we are

2:14:54

using this all mini lm this thing if you try to change the model to open a it will

2:14:59

100% give you document seven as an answer because it is nearest match makes

2:15:04

sense everyone yes or no because it is considering lesser number of dimensions into the

2:15:09

consideration right it is considering less number of dimensions only 384 but in reality

2:15:13

if you have more number of dimensions it will be more accurate but that does not matter what

2:15:18

is coming in the answer the idea should make sense that documents which are similar with

2:15:23

they will be close to each other. The documents which are not similar, they will be

2:15:26

far from each other. And on that basis, we will get the answer. Is that point clear to all of you?

2:15:32

Is the code making sense to all of you? Is the idea making sense to all of you?

2:15:41

Now folks, we don't have time now to show you the open AI model. I thought that, okay, I can show you

2:15:45

that. But what you can do is try to do two things as a homework. Try to use open AI.

2:15:53

I embedding model in place of sentence transformer.

2:16:01

Right? So everyone, the code is present in the nodes for your reference. Okay, you can refer that. I have already added a working code even if you copy paste, it will work. The only thing that you need to do is you need to give the API key. Then everyone, do one, do one thing you need to give the API key. Then everyone, do one thing.

2:16:23

also. I have shown you how to insert a new document. What you can do is just for practice

2:16:28

even so that you will be, you will get familiar with the code. Try to update an existing document

2:16:35

in the collection and then try to query. Does it make sense for all of you? These are the two

2:16:47

small homeworks for all of you. The code references are already present in the notes.

2:16:53

This is just for your practice. Is that point clear to all of you?

2:17:04

Folks, please let me know. Now what we want to do is we will upload the code to the GitHub.

2:17:13

We will create a new repository. Let's call it as vector.

2:17:22

repository.

2:17:52

Done. So this is the code link.

2:18:06

Sure. So this is the code link.

2:18:08

This is the code link. And let me also upload the nodes. Then I will share the link as well.

2:18:17

So guys, all the nodes for our batch present in this repository, agentic design batch.

2:18:22

Okay, I will upload the notes as well.

2:18:52

in this classroom. Folks now tell me how many of you enjoyed the discussion for today's

2:19:09

so maybe we can skip the quiz because we are already over time today we can skip the quiz. We can skip

2:19:14

the quiz. We can have the quiz in the next class. No worries. Now what is the action item on all of you? All of you

2:19:22

the class, very good. All of you understood very thing, very good. All of you watched the

2:19:27

lecture very, very carefully. Very good. What is the action item on you?

2:19:34

Tricky. Till the time you are not going to implement on your own, things will look tricky.

2:19:38

But trust me, if you understood the concepts in the previous two classes and today's class is just

2:19:43

a demo of it. So the base was formed in the last two classes. If someone is attending this class

2:19:50

directly, they will not understand it. If,

2:19:52

Someone is attending all the three classes last, two classes and today's class, they will understand it.

2:19:56

And they will be able to relate. Okay? Cool. So please do give it a try. Otherwise, it will

2:20:01

always be tricky for you. It will slightly be difficult for you. But once you give it

2:20:05

try, it will not be difficult. Still, if you want, if you get any doubt while implementation, a small

2:20:12

doubt, a big doubt, no worries, I'm there in the next class. Please feel free to ask any doubt in

2:20:18

the next class. Sounds good. Okay, okay? Perfect. So guys, now,

2:20:22

I'm launching the feedback poll now. Please take the poll and then we can end the class.

2:20:27

Please take the poll right now.

2:20:31

Folks, if you like the lecture, please take the poll accordingly. We are doing very good work.

2:20:36

Trust me, that the kind of content that we are going through, it's not very usual content, right?

2:20:42

And the kind of discussions that we are having. If you like the discussions, please, yeah, read accordingly.

2:20:48

I hope all of your liking discussion.

2:20:52

Why people are not able to fill the feedback poll? I can see 0% participation. Can you see the poll?

2:21:01

Okay, maybe it is not updating on my side.

2:21:22

Can you see the?

2:21:24

Yeah, I can see.

2:21:26

Okay, strange.

2:21:29

Please take a note once all the people fill the form, then we can end the poll.

2:21:38

Sure.

2:21:40

I think it is not getting updated on my side for some reason.

2:21:52

I don't know.

2:21:55

No, someone?

2:22:22

Thank you everyone.

2:22:36

It starts.

2:22:52

Yes. Okay. Thank you. Thank you. Everyone, have a good day. Take care.