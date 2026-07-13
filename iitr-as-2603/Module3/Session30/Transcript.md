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

Thank you.

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

Thank you.

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

Hi, good evening, all of you.

13:07

We're just starting in two minutes.

13:09

Let's wait for others to join in.

13:12

Just two minutes, we will start, okay?

13:13

Yeah.

13:36

Thank you.

14:06

Thank you.

14:36

Thank you.

15:06

Thank you.

15:36

Thank you.

16:06

Thank you.

16:36

All right. Hi, guys.

16:43

Once again, let's begin the session.

16:47

So, everyone's mostly joined in.

16:50

And just to very quickly walk you through the context, what we covered and what we have been through so far, let us go and quickly do a recap in terms of the journey.

17:06

So this is where we stand in our entire discussion.

17:13

So we are in the current module until the previous session, we have talked about the fundamentals of RAG.

17:20

We've talked about the idea of what is the rag pipeline.

17:25

We went through the RAG pipeline.

17:26

We also looked at the fundamental aspect of how we go ahead and build a RAG workflow

17:36

If you remember the very first day session, we looked at taking the data, creating chunks from the chunks, we are trying to create an embedding model.

17:46

From the embedding model, we are going and creating the vector DB, embeddings, and then during the retrieval part, we are going back to the vector DB, retrieving the relevant chunks and getting the results.

18:01

So this was the RAG workflow that we briefly explored in the last session.

18:06

And we particularly talked about two specific things.

18:10

In the last few sessions, we just looked at the foundations and after that, we looked at embeddings and vector search.

18:16

So this particular session focused more on what the process of embedding generation was.

18:21

What is, so we looked at some chroma DB specific operations, the absurd operation we looked at.

18:27

What if you add a document junk?

18:29

How do you update that in the chroma DB?

18:31

So this was what it is.

18:32

And today's session will be more focused on the chunking document preparation.

18:36

at a basic level. And from there, I will also take you through the complete RAG pipeline.

18:42

So there is one more RAG session that is coming up, the very next class. And in that particular

18:47

rag session, we can see that entire rag flow, the grounded generation. So this is where the

18:53

retrieval part will happen. But as a precursor to that session, while I end today, I will take a real

18:59

PDF data. Because all this file, you know, we were taking, we were dealing with primarily just some sample

19:05

text and we were trying to build an application based on that. But today I will take a real

19:09

PDF file. We will take the PDF. We will do the chunking. We will create the document chunks. We

19:15

will do the embeddings. We will create the embeddings and we will store that in the vector DB.

19:21

So until that entire thing, what we have talked about in the class so far, we will do that on a real

19:25

PDF file. And after that story is over, I will show you that entire RAG pipeline. So that is how we will

19:31

paste it out. Okay. So this is the main agenda. So the initial part of the

19:35

we will focus on the just some of the theoretical nuances we will talk about. So we'll

19:40

kind of recap the rack concepts, what the rack concept is. We'll first start with a basic

19:45

recap. Then we will talk about chunking. We'll talk about metadata. We'll talk about the ChromeRDB

19:49

once again. And finally, we'll take a real world PDF file and see the entire RAG pipeline

19:55

with that, except for the last part, because the last part is coming in the next session. All right.

20:01

All right. Now, French, let's move on. I'm going to quickly

20:05

open up my the diagram that we used last time. Let me quickly open it up.

20:35

If you all remember this, you know, this wonderful diagram that we explored in our very first

20:46

RAC session, I'm going to take a moment and summarize this to everybody once again. I hope all

20:50

of you remember this by heart now. We've gone over it a few times. First session, we did it again.

20:55

I think the second session also I briefly recapped it. It's the third time I'm recapping it right now.

21:00

So I expect after this class, you should all be, you should all absolutely memorize this particular.

21:05

workflow of what is going on inside a retrieval augmented generation, right?

21:09

So, but I'll be brief here because I don't want the like just five, 10 minutes we will take on this

21:15

one. So friends, it all started with normal generation. Normal generation was what? You have a

21:20

large language model and you are asking it a question and you're getting a response. So whatever we

21:26

talked about here was normal generation. Right? I repeat again, you are asking a question. So normal generation

21:32

was more like you're asking a question. So there is a query that you're giving as input.

21:37

And based on the query input, the LLM is processing a response. So that is the normal generation

21:42

that we explore. Okay. So you're giving a query as input and the LLM is processing the query. And

21:48

based on that, the language model is generating a response. That is what is referred to as a normal

21:52

generation task. Now, what if we are talking about proprietary data? Many of you working in

21:58

enterprises, you're working with let's say your projects, your companies and.

22:02

many companies will have their own proprietary data. Like if you talk about companies like,

22:08

you know, let's talk about Siemens. So Siemens is a major manufacturer of like the healthcare

22:15

ring of Siemens. You'll find a manufacturing CT scan MRI machines all across the world in hospitals.

22:21

And it is their intellectual property. Even in India, if you go to any of the major hospitals

22:27

and all, you will find Siemens equipment present there. Right. Now that is their IP.

22:32

right? And remember, these are extremely complex pieces of machinery. If you look

22:38

at an MRI machine, an MRI machine can cost crores. It's not like even lax it's gross. And

22:45

why is it important to talk about it? Because these machines will have extremely complex operating

22:54

manuals. If I'm focusing on Siemens as a company, these machines will have extremely complex

23:00

operating manuals.

23:02

And if you face an issue, you will not call your regular support person and say, you know,

23:06

it's not like operating a TV or a microwave and a washing machine. So it's very, very specific

23:11

and very customized, very technical support that you're looking at. And you have to understand these MRI

23:16

machine to be operated by healthcare professionals, doctors, radiologists. If they come across any

23:22

errors in the machine, they have to talk to the right spots and handle it. We are discussing,

23:28

can we build a AI assistant that can do that job?

23:32

So next time a hospital is operating one of Siemens MRI machine and the MRI machine

23:40

and the MRI machine is giving some problem. Can we build a kind of a chatbot interface for the

23:46

doctors and the radiologists where they can go and they can ask a question and this chatbot

23:53

will consult the manual and retrieve the answer.

24:00

And this chatbot will consult the manual and retrieve the answer. And this chatbot will consult the manual.

24:02

and it will retrieve the answer. That is a retrieval augmented generation that we are talking about.

24:06

And this is particularly relevant for company protected IP data. It's particularly relevant for

24:14

company protected intellectual property IP oriented data. Because here we are talking about

24:19

Siemens manual. See, if you ask a normal query to the LLM, imagine you're talking about a GPT model. We're

24:26

talking about a Gemini model. Let's say we are talking about one of these kinds of models.

24:30

So if you talk about a, uh, uh, uh,

24:32

a normal query. Imagine you ask a very customized query.

24:36

Can I do this or how do I resolve this error? You're giving a particular error log and asking the

24:41

language model to generate a response. This could be a GPT model or a GROC model, whatever,

24:45

whatever providers we have been using so far. Remember, this LLM is not trained on

24:50

cement specific data. If you just ask the language model a question that, hey, I'm getting this error,

24:56

how do I resolve it? I'm sorry, I don't know. I was never trained on that. And how would it be? Because

25:01

remember that that that Siemens MRI equipment manual is very confidential. It is not in the

25:08

public domain. It is not like a PDF you can go down download normally. No. So only the customers

25:13

who have spent crores of rupees and bought that MRI machine, the hospitals, only they will have

25:19

the dedicated support for that manual. And, and obviously even some parts of that will be protected. There

25:25

are a lot of proprietary things that Siemens will not even disclose. Like there are certain error

25:30

codes and all that only their technicians will know. That is completely company protected

25:33

data. And for these kinds of scenarios, a normal LLM cannot resolve it. And again, I'm repeating

25:41

guys, see, many of these, all this course, what we are doing is we are going through a lot of case

25:45

studies and all. You will get a good hang of things, obviously. I'm very confident of that. But what

25:50

I really want people to be good at is how do you frame a problem? Next time you come across a similar

25:54

scenario. How do you frame a problem? How do you identify a use case? That, okay, you know, you're working

25:59

in a company and how do you identify, okay, this is how I should solve this problem, this is how

26:03

I should solve this problem, and so and so forth. How do we frame the problem? That's a very important

26:07

aspect. So again, company protected, IP protected data, normal generation task will not work. So

26:15

we need something called retrieval augmented generation. You ask a question. The language model will not

26:20

directly be able to give the answer. So based on the question, we retrieve the context from the manuals.

26:26

We retrieve the context and based on that the language model,

26:29

can answer. That's why we call it retrieval augmented generation. Right. Now, coming back to the

26:34

right pipeline, I'll be very quick here because this we have already seen before. So we take a PDF,

26:38

whatever, this will be a Siemens manual. We can take a real Siemens manual PDF. We can take.

26:43

Second step we can do chunking because remember that PDF file is very big. You can have one PDF. You can

26:48

have several hundreds and thousands of PDFs. You can have thousands of PDFs also. So we can take the

26:53

entire PDF document. We can divide the entire PDF document into, you know, into relevant chunks.

26:59

So chunks are nothing but different, I would say different sections, different, you know, pieces of the document we are taking.

27:07

So we take the entire document, the PDF data, and we divide the entire PDF into chunks.

27:12

So chunks are basically nothing but section. So we can basically say one chunk is one page.

27:17

Imagine if you have a PDF file which is spanning total 100 pages. And if you do chunking, you're actually dividing that entire PDF into 100 chunks.

27:25

So every chunk is one page, C1, C2, C3, C4, up to C100.

27:29

So you are dividing the entire PDF into, you know, 100 chunks.

27:35

And every chunk, you will pass it through an embedding model.

27:38

You will each and every chunk you will pass it through an embedding model.

27:41

And you will save that in the vector d.

27:43

Because chunk is nothing but their text.

27:46

Machines cannot understand text, right?

27:48

We have seen that.

27:49

We have seen that machines inherently cannot understand text data.

27:53

So you will have to take those relevant chunks, whatever you bought.

27:57

Pass it through an embedding model.

27:59

there are separate embedding models that we have.

28:01

If you remember in the last session, we used a mini max, a mini LM model, right?

28:05

LM model we used.

28:07

These are embedding models that will take that text and it will convert that text into a sequence of numbers, vector embeddings.

28:15

Okay?

28:16

And that is what we will store in a vector db.

28:19

So a vector database is a special kind of database which will be used for storing this kind of unstructured data.

28:25

If you have text data, if you have got image data,

28:27

the vector database will be very, very good in storing this kind of unstructured data.

28:32

You can take each and every one of your text chunks and you can store that in the vector dv.

28:36

So every chunk will be stored in terms of its embeddings.

28:41

Chunk one, embeddings, chunk two, embeddings, chunk two, embeddings, chunk three, embeddings, chunk four,

28:45

embeddings.

28:45

So each and every chunk we will be storing their respective embeddings.

28:49

That's the way how we will work through with friends.

28:51

So this is usually the first part of the process.

28:54

Right.

28:54

We have kind of been through this.

28:57

And I'll talk a little bit more about these specific aspects, the chunking aspect a little bit more in detail.

29:02

But it will come to that conversation.

29:05

And in the last session, we also saw the chroma DB, if you remember, we saw the chroma vector database.

29:10

There are other vector database also that we have specifically, we explored the chroma vector database in the last session.

29:17

And this is usually the first part.

29:20

But then definitely this will be managed and administered just like a normal database system.

29:27

there will be administrators who will constantly monitor this vector db.

29:32

If some new documents are getting added, you have to add those records.

29:38

And what if, let's say some, some policies updated, let's say Siemens manual,

29:45

Siemens updates something in the document.

29:48

So you have to go and locate that corresponding chunk and update the embeddings.

29:53

So these are part of the absurd operations.

29:55

If you remember, we saw that absurd operations.

29:57

as well. And oftentimes, you will also might have to delete the chunks. So this will be a

30:03

continuing process. Step number one. Step number two is the retrieval pipeline where next time

30:10

when the user asks the query, and as I told you, the query will not directly hit the RLM. So based on

30:16

the query, the query will also be converted to its relevant embeddings. Because that's all that the machine

30:22

understands. The machine doesn't understand anything else. The machine only understands, you know,

30:26

text in the form of its embeddings. So based on the query, we will once again convert that

30:31

query into its relevant embeddings. And then we will pass it through the retriever and the retriever

30:37

will go to the vector DB and it will retrieve the top three relevant chunks. And that top value can

30:42

also vary depending on the use cases. We will talk more about that shortly. So again, based on the question,

30:49

we go to the retriever and the retriever will go to the vector DB and retrieve the relevant chunks. So that's the

30:55

how the whole flow will happen. I repeat again, you next time when you ask the question,

31:02

you go to the retriever and the retriever will hit the vector DV and it will retrieve the top

31:08

three or top two similar chunks. So in a way, we are saying that, hey, based on whatever question the

31:16

end user is asking, can we go back to my vector database, which is a consolidated, you know,

31:21

list of all my document chunks and everything. So based on whatever question is asked, can be

31:25

go back to the vector degree and can we find out which of the chunks are similar to the question

31:29

that is asked? And that's partly what we are trying to do, right? That's partly what we are

31:34

trying to do. So based on whatever, you know, a question is asked, we want to understand which

31:38

chunks or which sections of the document are helping us to answer that question. That is what we

31:43

are trying to do. So based on the question that is asked, which chunks or which documents are

31:47

kind of helping us answer that question. That is what we are retrieving. And that is what we call the

31:52

retreat context. And this is now what we say.

31:55

send to the element. And so coming back to the story that I was discussing, so you are giving

32:00

the entire query as input to the LLN. Based on the query, this entire thing that we talked about

32:06

is giving the retrieved context. So based on the question, we are fetching the retreat context. And you can

32:13

decide that. You can decide the value of K. Like some of you might wonder at Schein, how do I decide what

32:19

is the value of K? And this is a long conversation. Like this is something we will see as part of

32:22

advanced rag later on, not right away. But you can decide.

32:25

you can take k equal to two you can take k equal to three so they can be a you know varying

32:30

degree in which you can take your k right so and if i have to maybe give you a little bit of thought on

32:35

that one if you retrieve two few chunks then you have very less information think of it that way so this is

32:44

just to help you understand the two extreme cases so so one extreme case could be you retrieve only

32:49

one chunk if you retrieve only one chunk what will happen that means based on the question you're only

32:54

retrieving one portion of the answer but maybe one is too restrictive maybe your answer

32:59

is not even covered in that one chunk so maybe the lLM the final response you end up getting

33:06

when not very accurate that is extreme case number one extreme case number two what if you

33:12

retrieve 10,000 chunks then the whole purpose of rags is defeated the whole purpose of rags is what

33:19

you have a document and you create small sections based on a question you retrieve what section

33:24

is relevant and then but here we are retrieving everything imagine the original document

33:29

itself is 10 000 chunks and when you're retrieving you're retrieving all 10 000 chunks

33:35

and what is the point of right you might as well have given the whole document as a user input right

33:40

makes sense these are two extreme cases to understand so you have to find out a value in between

33:45

now how to find that is part of a later conversation but i just wanted to give you these two

33:49

schools of thought what happens when you retrieve only one chunk and what happens if you

33:58

retrieve all the chunks and there is one more problem friends when you when you go and retrieve

34:04

all the chunks sometimes it's a security issue as well because here we are retrieving all 10,000

34:10

chunks and if you're retrieving all 10,000 chunks you're giving that as a context to the lLM

34:15

mind you're actually sending company data external

34:19

outside that is also a problem you have to be mindful of that you are actually sending

34:25

company data outside when you're doing that so sometimes retrieving too many chunks is costly

34:32

and also it is a security issue but definitely it will give you higher accuracy

34:38

and on the contrary retrieving two few chunks has its own set of problems as we discussed so you

34:42

have to find out a value in between okay anyways that's the vector dvy part we talked about you

34:49

a question retrieve the chunks that's a retreat context and ln will take both as input and give it the

34:54

answer this specific part we will focus on them in the next session how is that retrieval

34:59

happening particularly we will see in the next class but today we will see a very comprehensive demo

35:04

as i told you where we take a pdf we will do the chunking we will create the embedding we will create the

35:09

vector dv as a live demo and then finally i will show you the retrieval part also so until here i will

35:15

will show you entirely in today's plus end to end demo we will see that

35:19

now let's discuss a little bit more theory prints and you know a little bit more theory in

35:26

terms of some chunking properties and other things and then we will get into the hands on

35:30

that's the time all right so now i think uh yeah same story as we discussed i think uh

35:38

in different ways we have explained it just just another diagram so you know the more you see things

35:42

the more you visualize the more you're able to maybe retain things the brain has a wonderful way of

35:47

learning from pictures so here is another

35:49

similar explanation given to you the first you load the pdf or any kind of text data see i i'm

35:55

going to say it's only pdf text data can be anything text can be pdf text can be document text can be jason

36:00

even jason is a kind of text data right so it can be anything so you load the data you do a chunking

36:07

you do a kind of chunking and i will talk about different types of chunking what kind of chunkings are

36:12

available we chunk the data divide that into similar uh different chunks or different sections

36:19

second third thing that you basically very important what you must do is you

36:23

you must add metadata again we saw this briefly in the last class you must add some metadata

36:28

to identify those chunks okay you must you must add some little bit basic metadata

36:34

for identifying the chunks at least something like a page number source id and this will be

36:40

particularly important uh in scenarios where you are retrieving information from several

36:46

hundreds of documents it's not just one pdf but

36:49

PDF but there are several hundreds of PDFs and what if you are trying to retrieve

36:53

information from several hundreds of PDFs if in reality you are trying to retrieve the

36:58

information from several hundreds of PDFs you will need to you know create the metadata for that

37:04

because when the retrieval finally happens based on the question when you retrieve the relevant chunks

37:08

you should know that which PDF that chunk got retrieved from so that so based on the question

37:15

you got the you got chunk two chunks per retreat you should know okay chunk one came from this

37:19

PDF and chunk who came from this PDF you should know that anyway so that's the basic

37:25

chunking and metadata thing that we already saw in the last class but i think you should understand why

37:29

meditra is important and and and i think the important part is this thing attach metadata

37:37

to every chunk for traceability i think the important part is important part is traceability you want to

37:42

trace it back right you want to trace it back why it is important why it is important why do we need to add metadata to

37:49

the chunk is not just take the PDF and divide that into different sections no but you should

37:53

add metadata so that metadata is what metadata basically means data about data more information about the

38:00

data metadata okay so that means whatever text chunk you have can we add some more information about it

38:07

and we say okay which which page number it is from which source file it is from

38:11

even going down to which topic it is from which category it is from it can help for better traceability

38:17

next time you retrieve chunks this can help in evaluation and it can help in debugging

38:23

one very uh important issue for rag systems is rag systems give incorrect results

38:30

and oftentimes it boils down to the fact that the chunks are not retrieved correctly

38:35

i mean if you look at it uh if you look at this particular pipeline users ask a question

38:40

you retrieve the chunks from the vector dv if the retrieval fails then the final answer will be

38:46

be incorrect so so ensuring that the retrieval happens correctly is very important

38:53

so what if you are retrieving wrong chunks how will you even know that because now when those

39:00

based on the question when you're retrieving those seven eight chunks from the vector dv you will

39:05

you will know that hey this chunk corresponds to this file this chunk corresponds to this thing and you

39:09

know that so that traceability is important so that you can do the error handling later on you can do the

39:14

are debugging later on maybe your users will come back to you some user is asking a

39:19

question and the rag system is giving some wrong answer so that user will come back to you and you're

39:24

liable to explain sometimes there are serious legal issues also there are there are contractual things

39:30

and whether the company is bound to explain that okay i ask this question how can you give an

39:34

answer like this so you have to then go and have a traceability and auditing and logs in your

39:41

organization where you can tell that okay you know this is the reason why you

39:44

this answer came the time you cannot say okay i don't know idea what chunks are and

39:48

all that no so that's traceability part is very important right i hope everyone's

39:52

understanding why that is important after the chunking is done same story embedding

39:57

model this is that mini lm vectors that we created last time and then finally we will go

40:01

and store it in the vector duty right so this part we have already seen overall okay guys uh

40:08

now moving on let us go back why chunking matters we can

40:14

do this in two phases right we're going to first talk about chunking and i think before all this

40:20

theory i think uh i like to look at things very visually so that it helps this is a simple way you can

40:26

understand chunking right everybody can uh look at the screen it's a very simple way you can understand

40:32

what chunking is doing i'll take a character split a kind of chunk i will create chunks every

40:39

512 characters so every 512 characters i will create a chunk

40:44

so that is what we are doing right now okay guys every 512 characters i will create a chunk

40:51

so first 512 characters that's one chunk next chunk next chunk so every 512 characters we are

40:57

going and creating a chunk you can see that so that's chunk one that's chunk two so this

41:03

is a simple visual way to understand what is chunking and what kind of chunking i'll be doing

41:08

we are doing a very simple fixed size chunking so the kind of chunking that we are seeing here

41:12

is what is called a fixed size chunk so fixed size chunking is the most common

41:19

strategy in rag pipelines there are other kinds of chunking also but we will see that yes what do

41:27

mean chunking well arnica chunking concept is okay right you're just dividing chunk into sections

41:31

chunking chunking chunking means what chunking means that you're taking our entire text data

41:36

and you're dividing that entire text data into different sections means imagine urnica you have

41:42

have this you have this text you have this text here you all that you're doing is you want to

41:48

divide that entire text into manageable smaller sections like what we call divide and conquer

41:55

that's chunky chunk you're trying to create it into smaller blocks so jess

42:01

we have that case study uh last uh last maybe saw that demo if you remember hr pdf we had

42:06

hundred pages 100 pages is too much to manage it's huge so then we've

42:11

what did what we've done? We said, hey, you know, we will take one, uh, one

42:15

pages, one chunk. Shake, we will talk about it. Don't worry. Over luck. I'll not discuss that.

42:22

Finally, so chunking is nothing but, uh, it's nothing but every, you are dividing that text

42:29

into smaller pieces. Every 512 characters, we have a chunk. This is chunk one, first chunk. This is

42:37

second chunk. This is third chunk and so and so forth. Every five 12 characters.

42:41

we have a child there is something about overlap so we can give an overlap of 16 and you can

42:48

visually see what is going on when i give a when i give this particular set in okay i will

42:54

pause for everybody just give it a glance all of you just give it a glance everybody

43:01

remember i've set a overlap of 16 here

43:11

Thank you.

43:41

and as you can clearly see every 512 characters we have a chunk so the first 512 characters we have a chunk

43:52

and this is the overlap zone what is the meaning of overlap that means these characters are

43:59

present in chunk one also are present in chunk two also right so these characters that you see

44:08

they are present in the first chunk also they are present in the second chunk also

44:17

so they're acting as a kind of a bridge so so starting from here until here we have the

44:24

first 512 characters chunk one chunk two actually starts from here

44:32

here here is next 512 characters chunk two chunk three starts from here

44:38

starts from here from here all the way to here is chunky makes sense this is what chunk

44:44

overlap is that zone where characters are present in both the chunks and you might wonder okay

44:53

so why is it important why do we need to have the overlap overlaps are very useful let's say where uh

44:58

you ask a question and the answer to the question is somehow present in both the sections

45:04

what if the answer to the question whatever uh

45:08

answer to the question you have the answer to the question is basically present in both the

45:15

sections that's one way to look at it okay the answer to the question is effectively present

45:22

in both the sections that's one way to look at it so now let's talk a little bit more about

45:30

these strategies what to do when to use all that okay fine uh so andika i hope you're okay

45:36

with chunk shake overlap i hope is fine with you yeah so why chunking matters

45:44

chunking splits long text into segments basically okay it is splitting long text into segments

45:50

and that's the whole idea of what what why we are trying to do chunking what what

45:56

chunking basically stands for now let us see that let us look at the idea here overall right

46:02

as i told you why chunking matters okay so so uh chunking is important

46:13

because what is the alternative alternative okay you will have to take the whole file and

46:19

then create a vector that is too big right so you need to create the right

46:25

size of the chunks okay what am i what am i trying to say okay i think let me go

46:32

to the diagram that will make it easy first first things first what we what we are

46:37

discussing right now is something called fixed size character splitter with overlap it is the most

46:42

common strategy so we discussed about something called chunk size we discussed about something

46:46

about something from overlap pictorially we saw that it is the most basic concept of shanku

46:53

in fact strategy number three was just a concept it is not it is not used in practice

46:59

this is the exact same thing with which i explained your rank for the

47:02

so we said okay each pdf page is just one chunk so it was just a way to explain to you but in

47:07

practice we don't do it we don't do it this way in practice we always do like pick size character

47:12

wise how chunking but it was just kind of like a way to explain to you there are other kinds of

47:18

chunking also which i will talk about later but this is again again a pictorial view of how the thing

47:24

looks like you can see so every 512 characters we have a chunk on in this case you can see you know

47:31

every 500 characters we have a chunk with an overlap of 75 characters

47:35

then next chunk then next chunk then next chunk

47:38

then next chunk so that's the way how we are going about it now please

47:43

understand two extreme cases the best way to know this is to do two extreme cases

47:48

let's talk about it first extreme case can i do chunk size equal to one

47:53

you can't no problem you can't you look at it you

47:59

if you take a look at it this is useless right completely useless okay

48:04

i have got uh overall two six five eight characters so two six five eight chunks

48:09

be been there no problem but think about

48:12

embeddings what you will save in the vector db because vector db because vector

48:18

db in what i will save i will save i will save each and every character each and every chunk chunk one

48:23

chunk to usy's embeddings we'll store

48:25

and most importantly

48:28

this chunks are what is the logical meaning of the chunks

48:31

chunks should be different sections of your text

48:34

different sections of the text which actually

48:38

mean something if you tell me that every character

48:41

is a chunk then what

48:43

means nothing right this is useless

48:47

never have a very small chunk size

48:48

if you have a very small chunk size and i'm not only saying with respect to

48:53

to one and i'm talking about small chunk size even if you have a chunk size of five five is also

48:57

very small you're able to hardly express any idea in only five characters even if you take a chunk

49:03

size of 50 50 is also not good 50 is hardly a sentence

49:08

chung should convey some basic idea at least a few sentences or a few paragraphs it should be

49:16

so that's why usual best practice we use is 512 512 more or less if you look at an average

49:21

English sentence so 512 is a good number to look for

49:26

so two extreme cases i talked about chunk size should not be very small and the same time

49:30

chunk size should not be very large now you'll ask me sir what is the problem in being large

49:36

what problem is i'll tell you what the problem is i have a chunk size which is 10 000

49:43

so the entire document is only one chunk

49:46

his problem what is this problem here is if you tell me that the

49:51

entire document is one chunk if the entire pdf is one chunk then then then

49:56

then raggy why are we even discussing rag right right you don't need any vector dbs

50:01

and all that for that right so so that means if you're saying the whole document is one chunk

50:07

that means the entire information of the document is present in a single chunk

50:12

so i have too much information present in one section

50:16

so that is the other extreme case chunk size one there is hardly any information in a chunk

50:21

and chunk size 10 000 there is too much information present in the chunk so we have to find

50:29

out a number in between and this is something you will have to play with you will have to try out different

50:34

different values iterate and then see what is the right chunk size you're getting okay so we'll

50:40

see that we'll see the evaluation bit later on but i hope you're everybody appreciates the

50:45

concept what chunk size means what is the basic idea behind chunk size what happens when it's a

50:49

a very small chunk very small chunk one of the losers context i told you so you can see when i

50:55

so so so when the chunk size is very small you hardly have any context there's no context you

51:00

have on the contrary when the you know when the chunk size is too large there are there are

51:06

blurry embeddings and very few chunks you have imagine we have a chunk size of 10 000 characters

51:14

so 10 000 character month of the entire document is one chunk so the final embedding

51:19

that you end up getting will not be very appropriate that you give a very average

51:24

idea of the whole document that's the problem so that's why we will look at a sweet spot of

51:32

512 and 16 we are looking at a chunk size of around 512 and the overlap of luckily 15

51:40

overlap so that is the kind of a sweet spot you're using okay i hope everybody is aligned

51:47

everybody is getting an understanding of what is this concept of a fixed size chunking

51:55

whatever we pictorially so that's why i say pictorially if you understood this this is a visual

52:00

way you're able to see what uh chunk overlap and all this is

52:06

what is the significance of chunk overlap so rich yeah a good question this is what i

52:12

explained already why chunk overlap why overlap so we do

52:17

chunk overlap

52:19

chunks repeats characters from the end at the start of the chunk

52:23

think of it like a shared margin

52:28

it's like a shared margin right i think i think i think another

52:36

another very nice way to think of it in the real world i think the example is very

52:41

nicely given so that's for you a newspaper repeats the last line at the top of the next column

52:47

i'm not saying it it always happens but let's just say it does that it becomes easier to

52:53

recall and recollect so when you're reading the newspaper imagine you're turning the page

52:58

so so so let's say every chunk is one page you're reading the newspaper last

53:02

whatever line is getting used okay let's say there's a sentence that you're that is completing

53:08

at the end

53:09

what is happening what is happening is happening is you're starting with another sentence in the next page

53:17

so the chunk overlap is acting as a kind of a bridge and as i told you here also

53:24

if you see if i give a chunk overlap of 16 what if the answer is present here

53:32

see if you don't have an overlap what will happen you ask a question and only this section

53:39

is retrieved but very important this is a continuing sentence right can you see

53:47

this is obviously true that the returns are for imagine you ask the question and only the chunk

53:52

one is retrieved but chunk one to continue here this sentence continues

53:57

returns for performance and superlinear in business maybe this portion could also have been

54:01

relevant i don't know maybe this kind of some relevance could be so that is why overlap will ensure

54:07

that uh okay based on the question you think this part is similar but because of the overlap

54:12

might be this chunk will also get picked out so don't chunk pick up

54:16

retrieval of time too does it make sense so much am i able to explain to you what what it is it's

54:22

kind of a bridge to ensure that uh both the chunks are somehow retrieved

54:29

you know let's say you're looking at the newspaper you ask a question and the answer to your

54:33

question is present in both the pages of the newspaper if i maybe visually show it to you this is

54:38

this is this is newspaper page number one right not for you know what this is

54:43

how sports's a pifa world cup okay so you're talking about who will win the world cup all that

54:47

okay let's say we are talking about that now if you're reading the page number one of the newspaper

54:53

sports story this is a big article somebody is written an article article the last paragraph

54:57

and it is continuing from here right think of it this way now let's say you ask the question

55:02

this is the typical retrieval workflow i'm discussing but the answer to the question let's say is coming

55:07

from some portion of the first page the last portion of the page the answer is present here

55:13

now if you don't do chunk of chunk overlapped the answer only this chunk will be picked up but remember

55:19

this particular line is continuing here also so what the question is the answer here

55:26

to some extent here from here so if you do a chunk overlap what will happen both the chunks will

55:33

be retrieved so you will get a better retrieval performance that's the way to make it

55:39

rest of it is the syntax best practices i can i can explain that way but this

55:43

is to just help you relate to it why we do it in general this is the best practice we always

55:48

use chunk over now there's no ifs and but we always use it but this is the concept we just looked at

55:53

what the concept is and we also talked about the chunk size part how do you decide the right

55:58

chunk size okay 512 is a good thing to start with okay this is a very small uh

56:07

example of the metadata part that we looked at if you all remember right we talked about the metadata part

56:12

and so what we are doing is we are creating a small sample corpus so we are taking some sample

56:17

entries this is just a very sample text we are creating and this is the way how we are attaching

56:22

the metadata we are manually at the associating the metadata this is how it looks like we saw this in the

56:29

last demo but this is just to kind of further tell you that when you create your chunks in practice

56:33

this is the kind of metadata you should attach you should tell which source that particular chunk

56:37

came from and you should also specify which page number it came from and we will see this exact

56:43

same thing in our real world pdf demo in a while from now i will show you i will show you i will

56:47

show you this but this is just to show you like again a small snippet of how it will it will be done okay

56:53

everyone can relate to it okay now moving on um why do we require metadata data

57:07

why do we require metadata thing we mentioned that before as well metadata is required for traceability

57:15

metadata is primarily required for traceability especially source ID page number

57:21

and you can have some additional metadata also like your category these kinds of things

57:26

this is primarily used for traceability because next time when a user asks the question

57:35

the answer to the question will come from there and you should know

57:37

which chunks are retreat for the answer so that's why the concept of metadata is very

57:43

very important okay i hope everybody has the overall broad idea we take the data we do the chunking

57:52

fixed size chunking is what we are sticking to right now and finally we will save the you know we will

57:59

go back and save the documents the corresponding metadata and also the corresponding embeddings

58:05

so that's the way how we will do it okay so if you want to see a small demo we can we

58:10

can take a look at a small demo where i'm kind of applying these things in action

58:17

so quick one we will see that let us see i will show you two sets of demos today one a very

58:24

basic workflow and second is a more real world tesla demo which i discussed with you i'll take a real

58:29

pdf and i'll demo that for you okay so both the demos we will see the first part is just a

58:33

a standard thing that we have seen before let me connect to the runtime and quickly connect

58:40

to the runtime here and here i will create the sample corpus exactly what i explained to you right

58:45

so i'll create a sample corpus with some text and i will just specify the source id so here the source

58:51

id is this particular file the returns policy text file page number zero and for this particular chunk

58:58

the source id is shipping policy text file and page number zero so you're able to see the

59:03

two chunks that we have created we have created two dummy chunks right now and uh

59:08

which two dummy metadata right so that's what we have effectively uh you know gone ahead and done

59:14

over all there's two dummy document purposes we've said sorry not chunks i i would say uh

59:20

two dummy document purposes we have created in reality this will be like two files

59:24

massive files okay from this we will create the chunks okay so uh so we have already uh written a

59:32

two sample snippets and here just to clarify i don't want you to like

59:36

uh confused with the snippet the snippet what we are seeing is a very manual

59:41

pythonic way we are doing it but just in the very next demo i will show you a much simpler way to

59:46

write the code so you can completely ignore the coding part here uh the coding part i will show in a

59:51

much better way in the next demo where you will see it is a lot easier and why does it become a lot

59:56

easier because specifically we will use the langchain library for doing these operations here it is a very

1:0:02

manual way we are doing it now look here here we are creating a function called

1:0:05

deaf chunk text we are manually doing it so we are starting a counter we are taking the length

1:0:09

of the text we are checking you know and we are creating chunks manually but obviously this is not

1:0:13

the best way to do it so we will be seeing the lang chain

1:0:16

likely where all this will be done in a single line of code okay but this is just for the

1:0:21

discussion purpose i've kept it so first you define the chunk and second is you create

1:0:25

chunks from the corpus so these two functions i'm defined currently can let us see that

1:0:32

oh sample corpus is not defined sorry because i did not run this tool let's run this now

1:0:37

and you'll be able to see at the end of the process we are able to get total eight chunks

1:0:42

okay so just to clarify again this is my document number one

1:0:46

that's the metadata here is document number two we also have it's more metadata and all that we have

1:0:52

done is from these two documents we've created total eight chunks total eight chunks

1:0:56

you can take a sample uh these are the chunks we have created right now and we're just

1:1:01

reviewing one of the sample chunks okay so chunks zero id this is the sample chunk that we have seen

1:1:09

okay just in case you're wondering what is present inside chunks zero chunks chunks is the complete

1:1:15

list of chunks right you can see in case you're wondering that sign what is chunks you can see

1:1:21

chunks is completely this end it is list of dictionaries right here are your chunks there are total

1:1:25

eight chunks that we have created from these two documents and you can see the chunks right now simple

1:1:30

so you can see this is like one chunk this entire chunk is like a dictionary

1:1:36

jason this is the second chunk and within the chunk what are the different key value pairs that you

1:1:43

have right now you have id of the chunk you have the text of the chunk you have the text of the chunk

1:1:47

you have the metadata of the chunk okay the page number the chunk index this is the way how we

1:1:53

are able to look at it and this is very interesting guys because you can see right now

1:1:57

how beautifully we have done this remember we had two documents

1:2:00

right main main so main we had only two documents we had a we had a return policy dot t

1:2:09

document and we have a shipping policy dot txt document if you remember right at the beginning i

1:2:14

demoed this with only two documents two documents are our

1:2:17

or this say we see the chunks that got created for this particular document metadata right

1:2:24

this particular document this is my first chunk chunk chunk index zero for the same document

1:2:30

this is our second chunk number one index one now look page number zero

1:2:34

because a key page a document so first chunk from this document is this second chunk from the same

1:2:39

document is this third chunk from the same document is this and from the same document the fourth

1:2:44

chunk is this so from the returns policy dot txt document i have managed to create four chunks and you

1:2:52

can also see that is why the metadata is so important when you look at metadata uh you can get to see that hey

1:2:58

what is the source id which file that chunk came from what is the page number what is the

1:3:02

chunk index it gives you a lot of clarity and also the id will tell you like return policy

1:3:07

dot txt you can see p0 c0 p0 p0 meant of page number c0 meant of chunk index one so this chunk

1:3:14

corresponds to the this particular file and it also corresponds to this particular chunk id same way

1:3:19

this is your four chunks create and this is the fifth six seventh and eight chunks right from

1:3:23

which is actually coming from the shipping policy txt so this is how we have done

1:3:28

the chunking right now after the chunking is over and why traceability matters you can see

1:3:32

the file name tells you which document is answered in answered the query this is also sometimes

1:3:37

important for auditability and you know purposes compliance purposes you know if you're building

1:3:42

a uh a real world chatbot for the enterprise you will want to know at which uh chunk

1:3:47

actually answered my question okay you will want to know which document answered your query

1:3:53

okay i hope everybody's aligned now this is very important friends metadata is not

1:3:58

embedded as vectors i just wanted to clarify this so this so this the metadata is only for your

1:4:02

own reference here's vector div in store it's like a normal database only right vector tv

1:4:08

you will store it but you will not embeddings will only happen for the text section right so whatever

1:4:15

chunk you have these are the properties of your chunk you have the chunk id which is there for

1:4:20

reference you have the chunk metadata this is this is the only thing that will get embedded so you will take the

1:4:27

text pass it through the embedding model and generate the embeddings others are maintained as it is okay

1:4:35

and once that is done we will now persist the chunks in chroma we will we will we will

1:4:40

persist the chunks in uh chroma we will do that and you can see we are going to create a new

1:4:47

collection for these chunks we will save those chunks we are using the sentence transformer model

1:4:53

all mini lm l6 v2 right and we will do chrome

1:4:57

Upsert. Upsert is the operation that we learned last time last session we already saw the

1:5:01

chroma vector db and we use Upsert to insert data into the chroma db so we are doing the exact

1:5:06

same thing here same story same thing but just that we are doing this in a slightly typical way

1:5:11

so what are the things we will insert in the chroma dd we will insert ID we will insert

1:5:15

documents we will insert metadata so we have ID to already have chunk IDs this is the thing

1:5:22

so we already have the chunks right so we have the ID we have the documents

1:5:27

documents are nothing but the text itself and we also have the metadata metadata

1:5:31

metadata is nothing but this section and remember we will use the embedding model so we already

1:5:38

have the model so we say model. We will use the embedding model to convert our

1:5:43

documents into embeddings and finally here is the chroma absurd command

1:5:47

simple you're inserting the id document metadata embeddings straightforward and this will take a

1:5:53

while to run it's a small document but even then the embedding does take a little time

1:5:57

it will be quick it will be quick but it will load the model it will load the model

1:6:04

and then it will do the embedding and you'll be able to see the results here

1:6:11

sometimes it gets a little slow for various reasons let's see

1:6:17

so it gets downloaded you can see there's a small mini lm model i'm downloading

1:6:21

i'm creating the chance and i mean and i'm doing the upshot operation and chroma d okay and you can

1:6:27

also go and take a sneak peek into uh you know what some of your chunks are

1:6:31

objects that's a row slot in policy chunks is eight there are eight rows we have saved in the

1:6:36

vector div and you can also take a look at the uh the collection that peak collection

1:6:40

that peak come up you are peek into the chroma dp and seeing what contents are

1:6:43

present inside the same story so whatever we saw the same format we saw same story will be played out

1:6:49

here update set your peak sample documents you can see the documents right now

1:6:53

this is exactly how information is there in the chroma dddd you have the list

1:6:57

of documents you get documents but chunks basically when i say documents i need to say

1:7:02

there are eight chunks we have so all the eight chunks will be stored in the documents list

1:7:05

documents taken list of eight eight chunks we have we have the list of eight embeddings

1:7:12

these are all embedding number one embedding number two embedding number three you can like that

1:7:18

these are all these of IDs there are total eight IDs we will have and finally we have total

1:7:23

eight main instances of meta made metadata we have

1:7:27

this is the same way this is the way how we are maintaining things in the chroma db

1:7:31

and finally the last part is we can verify the storage and we can run a semantic search

1:7:36

semantic search means you are asking a question and you want to see whether the answer is retrieved

1:7:40

accurately or not so based on whatever question you are asking you you want to go to the vector db

1:7:47

whatever vector db we have traded now you want to retrieve the relevant chunks and you want to figure out

1:7:51

whether the the right information is retrieved or not so that's the way how we want to go back and

1:7:57

do it that's the idea all right and you can try this out this is the simple one that we

1:8:06

are using is that final part uh you know like a simple semantic check that we are doing here so we

1:8:13

can go and ask the question and the question we are asking is how many days do i have to return a

1:8:18

product so based on the question we will have to first create query embedding all if you can see

1:8:24

because uh you know machines don't understand text machines inherently do not understand

1:8:29

text so based on the question okay so machines inherently will not understand text right so

1:8:36

based on the question we will go and create the uh query embodies based on the question we will

1:8:43

create the query embedding and then we are saying uh collections not query then we are saying

1:8:50

collections dot query query embeddings and getting the results you're basically patching the top

1:8:56

three results from the vector data based on whatever question you asked your question

1:9:01

a how many days do i have to return a product so based on whatever question you asked you can see

1:9:06

the top retreat chunk the top retreat chunk is this yeah your your top retreat chunk is the

1:9:13

lowest so whatever question you ask turns out turns out whatever question you asked the

1:9:20

bank one chunk that was returned there are total eight chunks right it went to the vector db it

1:9:25

retrieved the the top chunk or who's a top chunk here you can see what content is of the chunk

1:9:32

okay and you can see i think it answers the question correctly and the best part is

1:9:37

your chunks retrieve all right this is only the retrieval part we see this is not the complete rag part

1:9:42

this is only the part where user asking a question it goes to the vector db and it simply

1:9:46

retrieves the chunk for you it retrieves the three chunks for you it is simply

1:9:50

retrieve that retrieving the top three similar chunks for you and the best part is you can

1:9:55

now see you can now place the chunks back to where they came from so that is the best part up here

1:10:00

there you see what the source id is what index it is this is very very good for debugging purpose

1:10:06

so this is the part of the rack pipeline where we are stopping right now so so we have

1:10:11

seen uh taking the document doing the chunking big size chunking we have explored recursive

1:10:17

we have seen creating the vector dp and find

1:10:20

based on the question you're asking you're retrieving the certain number of chance and now we will

1:10:25

replicate this because this is again we have you know we have kind of taken a uh a sample dummy data

1:10:30

but what i want to do is uh i want to take a real world use case today on the tesla

1:10:35

dataset and i want to show you the exact set of steps all over again okay and let me just

1:10:40

quickly take you through uh finally what we are trying to build here this is actually the tesla annual

1:10:49

reports folder which i've already shared with you it's a zip file by the way guys this is

1:10:55

all part of your 11 july folder as i always do i've uploaded all the contents here everyone can please

1:11:00

take a look at it i managed to download kiae and you

1:11:03

if you want to just quickly explore what type of data i have this is the actual real

1:11:08

tesla 130 page financial report this is what real world will be like real world will be not like i

1:11:14

create two list and do all that that's that's nonsense right real world will be like this

1:11:19

Real world is where you have PDFs, you've got 10, 15 PDFs and you're building a real

1:11:23

rag system based on this live data.

1:11:25

So that is exactly what I want to simulate it.

1:11:27

The concepts are important. The concepts are exactly what I talked about.

1:11:30

So all those are important for the concept building. But this is how we are going to implement

1:11:34

this whole thing in practice. Okay. So we will take the PDF. We will divide this entire thing

1:11:39

into chunks. I'm thinking they can say character chunk, you know, chunking can be done.

1:11:44

And we will use the lanchine libraries all through. And you will see how simple the code will look

1:11:49

flight from here onwards. So we will create the vector d and then we will finally show a retrieval

1:11:54

operation. If I ask a question, what kind of chunks are retrieved? We will see a final retrieval

1:11:59

operation at the end. So this is the end result of what we are trying to achieve. And in fact,

1:12:03

we will do this exercise shortly. Okay. Yeah. So we can take a short session break and let's come

1:12:09

back after the break. And after the break, this is the case study. We will discuss. It's a quick one,

1:12:14

15, 20 minutes we will discuss and it is close. That's the plan. Okay. All right. So I'll see

1:12:19

all of you back after a short break and I will see you back after the break.

1:12:49

Thank you.

1:13:19

Thank you.

1:13:49

Thank you.

1:14:19

Thank you.

1:14:49

Thank you

1:15:19

Thank you

1:15:49

Thank you

1:16:19

Thank you

1:16:49

Thank you

1:17:19

Thank you

1:17:49

Thank you

1:18:19

Thank you

1:18:49

Thank you

1:19:19

Thank you

1:19:49

Thank you

1:20:19

Thank you.

1:20:49

Thank you.

1:21:19

Thank you.

1:21:49

Thank you.

1:22:19

Thank you.

1:22:49

Folks, welcome back.

1:23:19

And we will start on with this particular case study.

1:23:23

As you can see, we have the 130 page Tesla, Tesla financial document, and this could be a very good use case for analysts, particularly, right?

1:23:36

Imagine if you're an analyst with an investment bank or if you're an investment analyst, customers will oftentimes ask questions, right?

1:23:45

Customers will oftentimes ask questions of the data.

1:23:48

And they will want to know different, different things like, okay, what was Tesla's report last year, what was Tesla's profit in 2023, things like that.

1:23:57

And this is a small retrieval augmented engine that we want to build where if users ask any question, we should be able to retrieve the information and generate the answers.

1:24:08

That is the big picture idea of what we are going to build right now.

1:24:11

So I will straight away come back to the case study, the document here.

1:24:15

I will go to Collab and run this for you. This is already in the 11 July folder.

1:24:22

I've uploaded everything. The first part of the demo I've already run today. This was using very sample data, kind of what we did for the first two sessions.

1:24:30

So this is the more comprehensive Tesla demo that we are seeing today and also the next session we will repeat this idea.

1:24:36

Okay. Now, let me quickly connect to the runtime.

1:24:45

We'll go ahead and do a pip install. First things first, we will install the necessary packages. This will usually take a while. And you can see we are installing all the necessary packages. Tick token is a package to do the token counting.

1:25:15

This is a tokenizer package. We can use it to count the tokens.

1:25:18

Phi PDF is a package that we are using to load the data from a PDF.

1:25:23

So you'll use something called Pi PDF to extract contents from a PDF file.

1:25:28

So this is ultimately a PDF file. So Pi PDF is used for that.

1:25:31

And this is the main Lanchine library that we will use for the orchestration tasks.

1:25:36

So all the different components that we talked about here, chunker, document loader, embedding model, retriever,

1:25:42

retriever, everything, the land chain will provide us. We will not have to write the code

1:25:47

manually for any of this thing. If you remember in the last demo, you know, I was actually writing the

1:25:53

code manually for creating the chunks and all that. It was, it was quite big. It was close to 20,

1:25:58

30 lines of Python code we were writing. And now that we use the langchain libraries in this demo,

1:26:03

you'll see the code is just one line, one line of code and, you know, we will be able to do the chunking.

1:26:09

One line of code, we can do the embedding. It will be a lot simpler. So,

1:26:12

Lanchine is the high level library that gives us all these helper functions when it comes to

1:26:18

rags and agents and a large part of agents that we will discuss from here onwards to the next module.

1:26:23

We will be using a lot of Lanchine functions going forward.

1:26:27

ChromaDB is the VectorDB and Sentence Transformers is the library that we are using for the embedding

1:26:31

models. And GROC and Open AI, we already know what they are. They are AI inference platforms.

1:26:36

Okay. All right. So let me run this. I'm still installing this. It'll take a while. It will still

1:26:40

take a while. Let's see this one in action.

1:26:42

then.

1:26:56

The initial Papan stall will take a while.

1:27:07

Just just another few minutes we will give.

1:27:12

Thank you.

1:27:42

Thank you.

1:28:12

Thank you.

1:28:42

Thank you.

1:29:12

Thank you.

1:29:42

Thank you.

1:30:12

Okay. Now, very important once the libraries are installed, all if you

1:30:23

all of you can please go and restart the runtime, restart session. So that is very important after

1:30:28

the installation is completed and I will restart the session. You can see my session is restarting

1:30:33

now. And now I will go and import. Okay, so please ignore these other messages. These are all warnings.

1:30:38

You can ignore them. After the restart is done, I will quickly go and import.

1:30:42

I'm using my GROC API key. Client equal to GROC. Same story. We've already done these things.

1:30:48

And I will also import the other very, very important packages.

1:30:52

So these are all the lank chain related packages which I'm importing. And you can see this is what I was

1:30:56

referring to. I was doing the chunking and splitting manually in the code a while back. And this is the

1:31:01

land chain helper, you know, package we are importing called recursive character text splitter.

1:31:07

I will only give two arguments on the chunking will automatically happen. We are also using

1:31:12

PDF directory loader to load the data from the PDF. We are using sentence transformer to

1:31:17

for the embedding model and we are finally using lanchain vector stores for the chroma DB.

1:31:24

So first things first, I have already uploaded the zip file. I will quickly unzip the data. You can see

1:31:30

I'm unzipping the Tesla zip file and the folder is now created here. And within that folder,

1:31:35

you will see the Tesla PDF file is also present. All right. Now next I will do chunking. Let us look at a

1:31:42

code for chunking. We have seen all the theory already. I'm not going to repeat that again,

1:31:46

but all that we are doing is we are using the command recursive character text meter. I promise

1:31:53

you it will be one line of code and it is actually one line of code. I've broken in into four

1:31:57

lines just but if you just see this is actually a single line of code. The recursive character

1:32:02

text liter from tick token encoder encoding name chunk size equal to this chunk over that

1:32:06

equal to this is a default option but these two are the most important thing to look for. Okay. So you are going to

1:32:11

the chunk based on 512 is chunk size and this is the overlap. And that's it. You can do the

1:32:16

chunking and you can see how many chunks are getting created. Okay, this will usually take a while

1:32:21

depending on how big your document is. It is taking the real Tesla PDF data that we already

1:32:27

showed you and on that it is trying to create the chunks right now. And at the end of this process

1:32:31

you'll be able to see that has total 351 chunks. We have total 351 chunks right now. If you want to see

1:32:38

those 351 chunks, you can take a look at it.

1:32:41

you can take a look at some of those chunks if you want because you can take a look at

1:32:46

maybe you know some of those chunks if you want maybe you can look at the i can run the whole

1:32:52

command and like all these chunks are printed out you can see these are the chunks right now and

1:32:56

very interesting you can see the default metadata is already added here this is what i was saying

1:33:01

i did not have to manually do it the langchain library automatically added the method

1:33:05

but you can of course manually also do it you can see it contains the page content

1:33:09

page content but the actual text whatever text is present here okay then it contains the metadata

1:33:15

which contains the source the source means what is the source file and it also contains what is the

1:33:19

page number if you can see it a very real world feel of how the chunking is done okay so this one

1:33:23

chunk and you can see what file it is from the same pdf file and page number is 125 you can see

1:33:29

page number 125 say you can you see you can get a real world feel of world that i was talking about like

1:33:35

metadata appraisability and all that see how helpful it will be you'll be able to be you'll be able to

1:33:39

like see sometimes also it will very useful for references oftentimes when you're in like when you

1:33:44

have to give citations users ask a question and when you retrieve information oftentimes you should

1:33:49

say which page number you got it from so for those times of citations also it's very useful

1:33:53

uh to have the medical okay yeah it's created by lanchine only that's what i was telling you

1:33:59

because you see what we've done we just did pdafloader dot load is that's it that's it

1:34:06

that's it langchain did it internally unlike the last demo we were doing manually

1:34:11

lank chain did the entire thing automatically but you can customize these options there

1:34:15

okay all right all right next up so where are we right now pdf lia chunking kia chunks

1:34:23

been here story is completed until here now from the chunks we will create embeddings and save in the

1:34:28

vector db okay let us see the vector dp creation part now so first i will load the gttee large model

1:34:34

okay in the last demo we loaded the mini lm model here we are loading the gt e large model

1:34:40

so that is the embedding model that we will load right now so let me quickly load the gt e large

1:34:47

model and using the gt e large model we will create the embeddings so the code is again

1:34:54

straightforward chroma from documents you give the name of the chunks you specify the embedding

1:34:58

model you specify the collection name and you also specify the directly where you want the vector database to be

1:35:04

created and you can see after a while it's actually downloading the model right now it's

1:35:08

quite a big one and and you can see after a while the tesla database will be created

1:35:12

so this is the warning you can please ignore the errors okay because as long as a tick mark

1:35:17

comes the code ran successfully these are only warnings please don't be uh please don't be

1:35:22

worried about those warnings is still running usually the vector db will take a long time to create

1:35:28

and it also uses up uh gp u ramp but here it should be fairly straightforward

1:35:34

so now we can confidently say yes my vector db is created and now what i will do is i will

1:35:40

show you the retrieval functionality okay so we are here right now vector db is created every row is a

1:35:46

chunk and we have saved the chunk embeddings completed and now i want to show you a sample

1:35:50

query we have instantiated the retriever this is also a default langchain thing so we did not

1:35:56

have to manually do it we have instantiature to the retriever and we are explicitly specifying that i

1:36:00

want to retrieve the top pipe similar chunks okay so we are saying vector

1:36:04

dot persisted dot as retriever we are saying search type equal to similarity and we are saying

1:36:09

that hey i want to retrieve the top five similar chunks so we are explicitly uh based on a particular

1:36:15

question we want to retrieve what the top five similar chunks actually are so that is what we are

1:36:21

going to do so based on whatever question we have let's say we are asking the question what is the

1:36:27

annual revenue in the year 2022 so based on the question that we are asking uh you know these are the top five

1:36:34

similar chunks that you have right now okay you can see this one so vector store persisted

1:36:40

dot similarity search query k equal to five and you here here here chunks

1:36:44

see what are the chunks between okay so this is the thing so based on whatever question you ask

1:36:50

are all lank chain libraries okay you don't have to worry it's just basic syntax that's

1:36:54

only one line of code every module is one line of code we've

1:36:57

chunking we've imbedding we've vector db creation we've retrieval we've retrieval we're retrieval

1:37:03

retrieval the first level second level we will see in the next class i will show a small demo but

1:37:07

that is for the next month until here we have seen retrieval you're going to the vector dv and you're

1:37:12

finding the relevant chunks uh you know the top a few chunks now i'll say sir like

1:37:19

so this is the normal you know retrieval that is happening and you can see retrieve chunk one

1:37:24

you have your retrieve chunk one here you have a retrieve chunk two you can actually see what

1:37:28

chunks are retrieved right now so which chunks were retrieved so based on whatever question you're asking

1:37:33

you'll be able to see that this answer to the question that what is the annual revenue in

1:37:37

2022 is somehow answered in these terms what like here here

1:37:41

you'll hear you have to you'll get up here from here and we will see that

1:37:45

just to just as an example the answer to this question you

1:37:48

are you guys you add to what is the annual revenue in 2020

1:37:52

the answer to this question the answer to this question is actually present

1:37:58

somewhere here you're a 81 000462 this is the actual answer to the question i want you to the

1:38:02

actual answer to the question i want you to

1:38:03

to remember this for a minute, because this is a chunk in a chunk number, chunk number two

1:38:11

retrieve all.

1:38:13

So this is the actual answer that we will be getting later on.

1:38:16

Abhito, you ask a question and you're getting all the chunks, all the top five chunks.

1:38:19

Now, from these top five chunks, from these context, the LLM will give the final answer.

1:38:25

OM last way.

1:38:27

So, so far, where are we?

1:38:29

We asked a question, retriever, retrieve the top five chunks.

1:38:33

And this is the retreat context.

1:38:36

So now based on the question and the retrieved context, retreat context for both questions.

1:38:41

We don't need all that.

1:38:42

We just need to know annual revenue, those are bides.

1:38:44

So based on the question and the context, the LLM will give me a refined answer.

1:38:49

And that answer will be 8,000462, which I will demonstrate for you.

1:38:53

Okay, we will see that.

1:38:56

So we have seen the first part of the flow.

1:38:58

And now on the same notebook, let me do that last part.

1:39:02

And the retrieval part, as I told you.

1:39:03

will be part of the next session.

1:39:04

We will see this in more detail in the next class.

1:39:07

Until here, we are only focusing on this.

1:39:09

And this retrieval you will see in the next class.

1:39:10

But then we will just show you the working demo how it is going to work.

1:39:14

So that you see the whole thing in practice.

1:39:19

So again, I mean, I don't want to confuse you with RAC Q&A and all that right now.

1:39:24

But just the final retrieval part I wanted to show you.

1:39:27

Now, you see what the final retrieval how going?

1:39:30

What is the annual revenue in the year 2020?

1:39:32

Coming back to the final.

1:39:33

story, this user's a question. Based on the question, we will say retriever dot

1:39:38

get relevant documents. We will retrieve the relevant chunks. Everybody knows that.

1:39:42

Because vector dp already been here. Until here, the story is over. We already went through

1:39:46

this in detail. Now, user asks the question. This is your question. User asked the question.

1:39:51

Based on the question, we will retrieve the relevant document chunks, top five.

1:39:56

Top five document chunks, we'll retrieve it.

1:39:58

We are using a python dot join function and we're creating the whole context.

1:40:03

the complete context. So based on whatever question you're asking, we are retrieving the

1:40:09

context and that is what you're able to see on the code. And on the basis of this, on the basis of this

1:40:15

thing, you can see the final LLM will take the query and the context as input. The final LLM is taking

1:40:23

the query and the context as input. You have a query here. Your query is user question and the context

1:40:28

as input to generate a response. Now this part I will, we will once again see in the next session and

1:40:33

detail, but just to show you the entire flow, I wanted to show you this answer.

1:40:38

Beautiful, 81,462 million dollars. This is exactly the answer that we were expecting,

1:40:43

and this is exactly the answer that we are getting. And if you want to validate that,

1:40:48

you up herepah, you go. You're herepe 80,000462 search for. This is a massive document. I'm here

1:40:53

search for you, to you'll get to get you. Now, look, guys, the annual revenue of Tesla in the year

1:40:59

22 is indeed 81,462. And actually,

1:41:03

actually there are four pages where this is there. This page number 39 maybe, 81, 462, you know?

1:41:09

This is your page number 51.51 maybe he has. This is also there in page number 57, 81,462. It is also there in page number 94, 81,462.

1:41:21

So somehow based on the question, we were able to retrieve all the relevant chunks, or let's just say, all the pages where potentially this answer is there.

1:41:28

And finally, the last part, the LLM has given me a refined response.

1:41:33

The LLM could not have answered it itself. If it is a confidential information, which is not in the public domain, the LLM will not know. It's a confidential report. Let's say LLM will not know that. So then you're asking the question. You're also giving it the context on the basis of that the LLM is giving the answer. And that's the big picture idea of what Rags are. But the final piece of the puzzle, the generation part we will see in the next session. That is the, we saw we rags are divided into four classes. We are in

1:42:03

only the third session today. Today the main focus was how to take the PDF, how to note the PDF, how to do chunking,

1:42:11

different types of chunking we saw, importance of metadata we saw, how to store that in the vector d. And finally, based on the query, how we are retrieving the chunks.

1:42:19

So we have seen the main flow until here. And the last part was just to demo that to you. But this particular flow,

1:42:26

how they are getting the response, will be the focus of the next session, which is the coming Monday.

1:42:31

Okay, I hope everybody got the flow. You can ask another question. Let's try another question. Let's try another question. You can say, what is the annual revenue in the year 20203? I've tried to try. So let's see if the rag is able to give the answer. Okay, 96.77 billion dollars. It's actually correct. Now, look, check here here. The 2020, $26.77 billion dollars. It's correct. Now they go, 96.77 billion.

1:43:01

$96.77 billion.

1:43:04

So it is given the correct answer. Okay. Yeah. I hope everybody is clear. Everybody, you know, kind of got a flavor of what, what, you know, rags are doing.

1:43:15

Is it clear, thanks? All of you are with me. Everybody's with me. Any questions? Any questions?

1:43:22

And you can see, you can kind of, you can kind of see how helpful this can be for enterprises. We are working in any company.

1:43:29

if you're if you're looking at any enterprise when you're working with, you know, massive PDF data, this, this approach can be, can be so, so helpful in practice.

1:43:39

So this approach can be so helpful in practice, I would say.

1:43:45

How to check if it is answering complex questions. What do you mean? What do you mean?

1:43:59

How do I check if it is answering complex questions?

1:44:07

Well, I mean, are you saying, Suraj, if it's answering complex questions correctly?

1:44:12

Well, you need to do evaluation for that.

1:44:14

Evaluation is one more thing I will talk about later. We will see in the later session. How is

1:44:17

evaluation done?

1:44:18

What I mean, our focus is we are asking a question. We are looking at the answer and then we are manually

1:44:24

checking that the answer is right. But I think if you're, if your question,

1:44:29

is more like, sir, how do I know that whatever is getting answered? Is it a correct answer?

1:44:34

There is another evaluation part that we do that we will see in the next discussion. What is evaluation? Okay.

1:44:40

Perfect, can you explain again what libraries we import and which library is for which function?

1:44:44

Okay, I think I went through that already, but I'll explain it once again for you. Okay. So these are the

1:44:49

packages we are importing. Okay, straightforward. So JSON is just to, we are not actually using JSON.

1:44:56

So this JSON or TikTokan, we're used not using. So in fact, I can remove it.

1:44:59

We have import, you have used in a way.

1:45:03

So tick token is a package that is used for tokenization, right?

1:45:06

So you can use it for token counting.

1:45:09

JSON is the package that we are using to interact with the JSON.

1:45:11

Because remember, perfect, everything that we are doing in the world of analogies with

1:45:15

respect to JSON's. You're sending a JSON request, you're getting a JSON response back.

1:45:19

Right? If you remember that conversation we had on APIs, everything is like a RES API call, right?

1:45:24

So justly Jason will be useful for us. But again, in this four snippet, I'm us to use not

1:45:28

do it. So you have to, no, no, no, no point. We have we have done here.

1:45:32

Panta's is the library that we are using for data manipulation. You've been, you've gone through that.

1:45:36

From the land chain perspective, these four main things are our have. Recursive character,

1:45:41

text liter number one for chunking. This is used to load the data from the PDF fine. We are using

1:45:48

some land chain document loaders to do it. And you can use other kinds of document loaders also.

1:45:53

You have other document loaders also. Like you can have Excel loader, you can have text loaders.

1:45:58

You can have data in other kinds of files, who's probably loaded. So, this is the PDF loader we are using.

1:46:03

Number three is the embedding models. Langchain, we are trying to use sentence transformer for the embedding models.

1:46:11

And number four, we are importing chroma for the chroma degree. So these are giving you a high level helper functions to work with these four modules.

1:46:19

You can make sense, her piece? Yeah.

1:46:23

Ernikah, like, was that a question you had? Like, inventory data must not have?

1:46:28

I didn't understand what, like, you can ask me.

1:46:31

Like, I missed your question, actually. Yes.

1:46:36

Okay. Everybody's clear. And as I was mentioning, like, before that, I was mentioning, this could be very

1:46:42

useful for your enterprise. Maybe people who are working in companies, your companies will already

1:46:47

have a tremendous amount of, you know, document data. And I think you can, you can already start

1:46:52

to appreciate how useful it would be, how useful it would be if you can take your PDF, if you

1:46:57

can build a rag system and people can just ask questions and they can get answers out

1:47:01

of it. Any kind of data, it could be very useful. Right? And I think, like, yeah, I mean,

1:47:07

Arnika, if you're referring to inventory data, huh, you can kind of also replicate something

1:47:11

very similar in inventory data also. You can, uh, like, let's say you're a store manager.

1:47:19

Imagine you want to do this at a, uh, a global level for a company like Walmart. Now,

1:47:25

Walmart for Walmart to do. So a store. So, uh, a store.

1:47:27

store manager can ask questions about inventory because that's a very important thing.

1:47:31

You want to know the, you want to know, you want to know how much, how much stock you have left for a

1:47:38

particular product.

1:47:39

What if it's got an item, it's got, what kind of item, it's got an item, it's got an item up in store

1:47:42

may have. It could be a great use case.

1:47:44

Store managers want instant answers to those questions.

1:47:47

So the rag system can be very useful for that.

1:47:49

Exactly.

1:47:49

So you can, they can ask a question.

1:47:51

I thought, you can think of it like a tablet, a tablet, a type of set up data.

1:47:55

There up made there, a app, you know, where the app, where the question,

1:47:57

this could be a great use case in, in that scenario as well.

1:48:01

And you can extend it, obviously, yes.

1:48:05

Okay, everybody's clear.

1:48:07

So all the contents are part of your 11 July folder, right, guys.

1:48:11

Everybody can please, please pick up the contents from the 11 July folder.

1:48:17

Okay, fine.

1:48:18

So, I'm sure all of you are clear.

1:48:21

So it was, it was, I think, again, a continuing session on rags that we did, and just to

1:48:27

walk you through the, the contents that we discussed for today.

1:48:31

So we looked at a use case of how we were able to load the PDF documents into, in memory,

1:48:38

we were able to load the PDF, we were able to apply chunking strategies.

1:48:42

We understood what is fixed size.

1:48:43

We'll back in other kinds of chunkers also.

1:48:48

In case, some of you are wondering, that fixed size is too, and I agree with you.

1:48:52

Fix size is only the start.

1:48:53

Fix size is only, we are creating chunks based on, you know,

1:48:57

contiguous characters. Every 512 characters, a chunk, but that's not appropriate

1:49:01

so what else do we have? You will see that. Our advanced ragby are. We will discuss something

1:49:06

for semantic chunking. We have other kinds of chunkers also. But we have seen a basic

1:49:11

fixed-size chunking today. And we also understood the concept of metadata. This is kind of related

1:49:18

to the last session also. And finally, we were able to purchase the documents to the vector store.

1:49:22

And also, in addition to that, we were able to complete the session with a, uh, with a,

1:49:27

beautiful end-to-end demo with a real PDF file, right? All right. So thank you guys. That will

1:49:33

be all from my end, uh, what we have covered for today. And I will look forward to all of you on Monday.

1:49:39

And Monday, we will have our final rag session. Final rag, what's like basic rack.

1:49:42

That's after advanced rag we have. If you look at our curriculum, we have some advanced rack sessions

1:49:47

also in the agentic module. So yeah, so our four sessions of basic rag we talked about here. And we are

1:49:53

doing another rag here. This agent build workshop.

1:49:57

there's this is the fifth session on rag that will come after a few weeks.

1:50:02

And after that, when we come into agents, this is where we will see advanced rag. So these two

1:50:07

sessions are particularly about advanced rags. This is where I will talk about other forms of chunking,

1:50:13

other forms of embedding or what can do. So a lot of interesting conversations. So rag is actually

1:50:18

this important. You can see, already start to see we are, we are having a lot of content on rag in our

1:50:22

curriculum. And we will actually do it. We see a lot of companies doing it in the real world.

1:50:27

Okay. Okay. Okay. Thank you. Okay, all of you guys. And I wanted to thank all of you for joining on a weekend. I hope it was time well spent for all of you. And I'll hand it over to Pratap. Thank you all of you. I'll see you on Monday.

1:50:42

Yeah. Thank you, sir. I am sure you have already vetted their appetite for advanced drag. Like, they're already very excited, I'm sure.

1:50:52

So, all right.

1:50:55

Guys, I am releasing the feedback poll.

1:50:57

please make sure you fill it in and also fill the second question as well. How did you find

1:51:04

today's lecture experience? Because I've noticed many of you just fill in the answers like the multiple

1:51:11

choice ones and then you don't fill in the second one. So please do that.

1:51:19

Yeah. Once this is done, once I notice that everyone is done, I will start the Menti meter quiz.

1:51:27

Okay.

1:51:57

everyone has answered. Okay, nay, a couple of you are still left.

1:52:04

So okay, all right. I will release the millimeter and screen sharing. Should be on. Okay.

1:52:27

feedback poll. Let me know if anyone is left. I can wait for a minute or two.

1:52:57

So the poll is ended. We're starting with the mental quiz.

1:53:07

7, 8. I thought there were nine players.

1:53:14

I just saw nine at the bottom there. That's right.

1:53:18

Okay. All right. Anyways. I think I'll start.

1:53:25

So a couple of easy questions.

1:53:27

Actually, mostly easy questions. Good luck.

1:53:34

What does an embedding primarily represent? Easy question, actually.

1:53:42

What does an embedding primarily represent? A vector embedding.

1:53:57

Why are people down voting?

1:54:01

I just saw someone say thumbs down.

1:54:05

I'm just wondering why.

1:54:08

Okay.

1:54:12

Yes. The correct answer is semantic meaning as coordinates.

1:54:16

So most of you, okay, it's pretty well divided actually, but the correct answer is semantic meaning as coordinates.

1:54:24

So when you say an embedding primarily,

1:54:27

it represent, right? A vector embedding. You would have the meaning as well, right? So for example,

1:54:34

a man plus ruler would be equal to king. So you can do that in vector embedding. You can do that

1:54:43

with embeddings because the meaning is represented with the words, right? Or a female or a woman

1:54:49

with ruler would be a queen or a princess, something like that. Right? That is, that is why this is the

1:54:56

correct answer. Okay? So understand why it is the correct answer. All right.

1:55:06

Actually, you did not expect only three people to get this right. So I'm sure the other questions

1:55:13

are a little easier. Okay. Which model is used in the class?

1:55:26

So in our class for embedding.

1:55:29

This one is a fairly easy answer.

1:55:32

If you guys paid attention, you would get it very quickly.

1:55:37

I think most of you got it.

1:55:42

Yep. Everyone is voted.

1:55:46

Yes. So, okay. Yeah. It's not text embedding. This is some different model. I'm not even sure if it is a model or not.

1:55:53

But yeah, the model that we have used, even

1:55:56

tutorials so far in all of the lectures, it is all mini Lm L6v2. So you don't have to remember

1:56:02

the whole thing. You just have to remember that this is, we are using mini LM. Even

1:56:06

sir mentioned it today. So yeah.

1:56:26

Why should one idea usually be stored per chunk? This is related to chunking.

1:56:38

Okay, if you look at the options, it's kind of, kind of obvious. If you look at the options, and I mean, obviously, and I mean, obviously, you have to take the previous question also in mind.

1:56:53

So the previous question, the answer.

1:56:56

and then if you think about the options, should get it.

1:56:59

It's pretty easy, actually.

1:57:01

Yep.

1:57:02

Everyone got that correct.

1:57:03

Great.

1:57:04

Improve the semantic focus during retrieval.

1:57:07

Yes.

1:57:12

Awesome.

1:57:18

All right.

1:57:26

What is the strongest reason to inspect top K documents manually?

1:57:35

So I'm sure you guys know what are top K documents.

1:57:39

The retrieval system is going to give out some documents to the LLM.

1:57:44

Those will be the top K documents.

1:57:46

What is the strongest reason to inspect them manually?

1:57:54

What could be a problem?

1:57:55

could be a problem if it if you don't inspect it so it did actually cover

1:58:01

it related to interpretability yes so vector distances are relative and may

1:58:09

itry one supported topics that is correct if you remember last in the last class

1:58:14

we had a question about UPI and shipping right so even if we're asking

1:58:21

question about UPI the model is giving the answer about shipping

1:58:25

because it doesn't, it may not have the correct data.

1:58:28

So this is, this is why this is like very important.

1:58:31

You need to know what are the top care documents that are being retrieved.

1:58:36

Because the LLM is obviously very much likely to make mistakes.

1:58:42

I mean, it can make mistakes sometimes.

1:58:47

All right.

1:58:48

Last question.

1:58:51

And then we are done for the day.

1:58:55

You guys can find a list.

1:58:55

enjoy a Saturday night, hopefully Sunday.

1:58:59

With chunking strategy is most likely to improve semantic retrieval quality.

1:59:04

This is regarding chunking strategy.

1:59:08

I'm sure sir covered this in some detail.

1:59:15

So, okay, yeah, this is slightly difficult, but

1:59:20

you should be able to get it.

1:59:25

Yeah, okay, so great.

1:59:33

Most of you did get it correct.

1:59:34

Create focus chunks with limited overlap and one main idea.

1:59:37

If you remember two, three questions ago, we discussed what should be the main property of a, like,

1:59:43

what is the thing that we want a chunk to contain?

1:59:47

So that is one main idea.

1:59:49

And that was the options as well, right?

1:59:51

So, yeah, this is the correct answer.

1:59:54

Split text at fixed characters.

1:59:55

without overlap. This is not true because sometimes we need overlap. That is also something

2:0:00

so explained. It helps in identifying related information. So we need overlap for that sometimes.

2:0:09

And use different embedding models for different chunks. That is absolutely wrong because if

2:0:16

you use different embedding models, you will have different, different embedding relations, which

2:0:20

means your distances will be meaningless. Retrieval will also be meaningless.

2:0:25

So, yeah, don't do that.

2:0:32

All right, I think SSR, whoever they are, congratulations.

2:0:40

Yeah, okay. So with that, we are at the end of the session.

2:0:44

Thank you so much for attending.

2:0:46

Have a nice weekend.

2:0:48

Try to enjoy whatever is left of it.

2:0:51

And I will see you guys on Monday.

2:0:52

Okay.

2:0:53

Bye-bye.

2:0:53

Have a good night.