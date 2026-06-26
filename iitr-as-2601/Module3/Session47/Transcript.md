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

Hi everyone, I hope am I audible to all right?

5:54

Guys, you will be starting in next few more minutes.

5:57

I'll let other people to join and then we'll start.

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

Thank you.

9:50

Thank you.

10:20

Thank you.

10:50

Thank you.

11:20

Hi,

11:27

Good.

11:28

Good evening.

11:29

All of you all of you.

11:34

We are just starting on here.

11:35

We are just starting on here.

11:50

Today we will have a very interesting case study session on Rags.

11:57

So I'll just wait for a few more minutes and we will start all.

12:20

Thank you.

12:50

Thank you.

13:20

Thank you.

13:50

Thank you.

14:20

Thank you.

14:50

Hey,

14:54

Hey, good evening,

14:57

Good evening,

14:58

Good evening, everybody.

15:14

Good evening, everybody.

15:20

Thank you.

15:50

Okay, let's start on here and just to set the context, what will be where we are as, you know, so far in our journey and what we are going to be covering in the session today.

16:01

So just to give everybody a little bit of context here. So we have covered Python and machine learning in the first two modules. And today is actually one of the final sessions for our module three. And in the module three, we have seen quite a bit. We have been

16:20

introduced to generative AI. We've been introduced to what large language models are. We have discussed how to write prompts. What is system message? What is user message? What is the concept of retrieval augmented generation? We have four sessions on rags. We looked at the entire pipeline step by step. We had a very small introductory discussion on agents, the React framework. And we saw a few other related things like how to be version prompts and memory and all those related things. So today is more of a, I would say,

16:50

a very comprehensive end-to-end session which we have which we will be conducting a very case study oriented session. So there won't be any new concepts today.

17:03

But the overall agenda of today's session will be to talk about a complete end-to-end drag application.

17:11

So we will build an end-to-end drag application on a very real world data set. I'll give you some context on the dataset shortly.

17:18

And we will do everything.

17:20

that is there in the rag. After we summarize a bit of rag, we will do chunking, we'll do vector db, we will do retrieval, and we will do the final user interface creation, just like how we discussed in our Tesla demo case study. That is what we will be doing. And obviously, the real world use case for this, exactly the case study that we will take up today. A real world use case will be policy bots and support assistants. How do you automate customer support, if given a particular manual,

17:50

people can go and ask questions automatically to that assistant.

17:54

How can you automate that entire process?

17:56

That is the real business value of what we are trying to achieve in today's class.

18:00

And obviously, from here onwards, the next module is totally focused on agents.

18:05

So module three, we have, we had an introduction to agents, but module four is totally dedicated towards agents.

18:12

And we will get into agents in a lot deeper fashion in this fourth module.

18:18

Okay.

18:19

So that is what we are getting towards.

18:22

Now coming to the case study, what we are doing.

18:25

And we're going to be building a rag system on a very real data set.

18:33

But before I do any of this, I hope everybody remembers what rags are.

18:38

Just a very quick two minute walkthrough of what retrieval augmented generation is all about.

18:45

We have done this over several classes.

18:47

I'm sure everybody remembers it very well now.

18:49

So you will take a PDF, a massive PDF file you will take.

18:55

And the problem is that machines cannot process a massive PDF file.

19:00

If you have a text file, machines cannot, they cannot process that text file as it is.

19:06

It has to be broken down into sections or chunks, as we call it.

19:10

We have to take that massive PDF document and we have to use something called a chunker.

19:15

And we have to divide that entire PDF file into a set of chunks.

19:19

So that is what we will have to do. We will have to take that entire PDF file

19:24

and we'll have to divide that entire PDF file into chunks. The chunks are what we will be creating

19:29

here. Let's say 10 chunks, 15 chunks or whatever it is. And after the chunks are created,

19:37

we will save that in a vector dv because chunks are basically, there are different different ways we can

19:43

do chunking. And if you remember, we talked about fixed size chunking where you will give a particular

19:49

chunk size and you will say, hey, after every 512 characters, I want a chunk.

19:53

After the next 512 characters, you want a chunk, right? I hope everybody, you know, recall that.

19:59

In case you don't, let me bring up that, that beautiful visualization that we saw about chunking.

20:07

So we saw this, you know, beautiful visualization about chunking where you can decide a specific chunk size

20:14

and you can say, hey, given a particular text, how you want to chunk your data.

20:19

Every 512 characters, we have chunk 1.

20:21

Next 512 characters, chunk 2.

20:23

Next 512 characters, chunk 3.

20:26

So it is basically dividing the entire text into manageable sections.

20:32

You've got section 1, section 2, section 3, and so and so forth.

20:35

You're taking the full text data and you're dividing that into manageable sections.

20:38

So that is what we are able to do.

20:40

And that's the chunk size basically, chunks size 512.

20:42

Every 512 chunks you are trying to, sorry, every 512 characters, you're trying to create a chunk.

20:49

There can be other more advanced ways of chunking.

20:52

We had a basic discussion on semantic chunker.

20:56

Here we are chunking in a continuous manner.

21:00

So every 512 characters in a contiguous fashion, we are creating chunks.

21:06

But sometimes what happens is related ideas are grouped together.

21:10

So slightly more advanced ways of chunking will be semantic chunking, where similar ideas are part of a chunking.

21:18

But the core.

21:19

The core concept remains the same. The core concept is what is more important. The core concept is you take a massive PDF file spanning thousands of pages or you have multiple files in a directory spanning millions of pages cumulatively. How do you work with that data? You can't process that entire data together in one goes. You divide it into manageable sections. Machines don't understand text. You have to use an embedding model here. Convert it to a vector DB and stored it in a vector DB.

21:49

Now, what does the vector DB actually contain?

21:51

The vector DB consists of those respective chunk text.

21:54

It actually contains the respective chunk text.

21:56

If you remember, we had a complete session on chroma.

21:59

Chroma absurd operations we discussed.

22:01

So Chroma DB is that vector db that we saw in our sessions.

22:04

There are other vector dvies also that are there.

22:06

And they are just like any other database.

22:08

Only thing is that they are not storing data in a relational fashion.

22:12

They are storing data in a, you know, they are very, very useful for storing unstructured data.

22:17

They're not that good in storing structured data.

22:19

forms of data, but they are very good in storing, I would say, unstructured forms of data.

22:22

That's what vector db is really are.

22:25

Okay. So every row in the vector db stands for a particular chunk.

22:30

Okay, so each and every row in the vector db stands for a particular chunk. And what we are doing

22:36

is we are trying to, yeah, so every row stands for a particular chunk. And we are basically creating

22:43

the chunk embeddings. So for each and every chunk, we are trying to create what the, you know,

22:49

what the different chunk embeddings basically are.

22:52

So for every chunk, we are trying to convert that into the corresponding embeddings.

22:57

I think the main difference, Akanchu, is that if you look at ChromaDB, ChromaDB is completely open source.

23:03

And the biggest benefit of that is you can locally host it.

23:06

You can, you know, it's open source, so you can host it on your own infrastructure,

23:10

whereas Pinecone is more of a cloud managed database.

23:13

It is more of a managed instance.

23:15

So I would say it's kind of about it doesn't give you too much control.

23:18

And so, you know, if you look at pine cone, fine cone will not give you too much of control

23:23

in terms of what it can do and what it cannot do.

23:26

So pine cone is more of a, you know, more of a cloud managed instance I would, I would put it

23:31

else. Okay. Yeah. But yes, I mean, the features and capabilities are obviously, you know,

23:36

very, very similar to what chroma can do and all that. But yes, that's one way to look at it.

23:41

Okay. Let's continue on. I'll, I'll come back to some of these general questions in a moment.

23:46

I'll take, I'll keep time aside for advanced questions also.

23:50

Just, we just continue the flow and then we'll keep some time for the questions.

23:55

So take the PDF, do the chunking, create the chunks, store it in the vector div.

24:00

The vector div will contain the individual chunks and it will also contain the numeric embeddings for the chunks.

24:07

That is what the vector div will contain.

24:09

And another very interesting thing is that guys, remember I told you, vector TVs will not just contain, you know, vector devs will

24:16

not just contain your, your, your, uh, uh, text data. Vector DVs can also consist of,

24:23

they can also effectively consist of, uh, image data. Just like we are taking the text chunks

24:28

and converting that into embeddings, you can also take the respective image chunks, image one, image

24:33

two, and you can convert that into embeddings. So that is also possible with the vector D. Okay. So this is the

24:39

first phase of the journey where you take the document and you store the chunks and you store

24:44

the embeddings. That's the first part of the journey.

24:46

The second part of the journey is what happens during the retrieval phase.

24:51

So the, you know, when the time eventually comes to write the query and to do the retrieval, what happens then?

24:57

So during the retrieval phase, you ask the question, the retriever will go and hit the vector DB, retrieve the relevant chunks.

25:03

This is a similarity match that will happen.

25:05

So whatever question the user is asking will be converted to its embeddings.

25:10

Based on that, you will go to the vector DB, find out what are the relevant chunks, the top

25:16

two relevant chunks or the top five relevant chunks. You will find out how many relevant

25:19

chunks you want to retrieve. And that is also an important consideration. We talked about it. You cannot

25:26

retrieve. Let's say if you say K equal to one. Should I retrieve the top one chunk? If you only retrieve

25:31

one chunk, then that means you don't have enough information, right? You don't have too much in enough

25:36

context. If you're only retrieving one chunk, then you have got a very limited context. So we will not

25:41

retrieve only one chunk. At the same time, I will not retrieve 100 chunks. If you retrieve 100 chunks. If you retrieve

25:46

hundred chunks and the whole purpose of rags is repeated. The whole idea of rags is that, okay,

25:51

you only retrieve whatever context is required or whatever context is important. You don't retrieve the

25:57

entire context. Entire context means the whole PDF and all the chunks and all the pages that are

26:02

present inside it. That's not required. Right. So now, so you ask the question and you retrieve the

26:10

relevant chunks. Let's say the top five chunks and whatever you have, you retrieve that. And this

26:16

becomes the context for your large language model. So now the story becomes, you are,

26:24

you have the question, you have the question. That would be the input to the LLM. So previously we were

26:29

just based on the query, we were getting the response, a normal generation task. That's what we've

26:32

been doing with LLM so far, right? If you ignore this entire part to the left and side, all that we

26:38

were doing was user was asking a question and the language model was processing that and was giving

26:43

a response. That is what a normal

26:46

generation task was now what is happening is you ask the question, that's the query.

26:51

This is the retrieve context. That's what we call the retreated context. And both together

26:56

are now inputs to the LLLL. Obviously it will have a system message of its own. So you're not

27:02

only looking at the original question, but you're also looking at the retreat context and based on that

27:06

you're getting the answer. And then hence we call it retrieval augmented generation. It's not a

27:10

normal generation. It is a generation that is like it's retrieval. First you're retrieving and then

27:15

you're augmenting the generation process. You're making it better. So first you're

27:19

retrieving the relevant chance and then you're augmenting the generation. So that is why we call it retrieval

27:23

augmented generation. There are a lot of, a lot of interesting things that you will have to

27:30

take care of. I think we have done this in various ways in the course of our session. But there

27:39

are multiple points of failure. So rag systems can be very difficult to evaluate. Sometimes it can be

27:43

very hard to figure out what is going wrong and how to evaluate a rag system. It's very

27:47

important to know that. And it is so useful because it's so important because why do we do

27:55

rags? We do rags because we want to get answers to questions from our company proprietary data. We often

28:03

use the term grounding. If you remember grounding has been a term we have used in the sessions.

28:07

That means whatever answers we want to get to our questions must be grounded in the context.

28:13

So whatever the actual data is, it should be coming from there.

28:18

So that's why evaluation is very important. There can be multiple points of failure.

28:22

And that's why rags can be very difficult. The workflow seems very simple.

28:25

But there can be a lot of scenarios where rags can go wrong.

28:29

So few things will be definitely chunking. How you are doing the chunking?

28:33

Are you creating too many chunks, too few chunks? You will have to try out and test.

28:37

What kind of chunking are you doing?

28:41

What kind of embedding models are you using?

28:43

We used GTE large. If you remember in our Tesla demo, the exercise we did, we used a GTE large model.

28:50

But there are different, different embedding models you can also try out.

28:53

Embedding models are responsible for taking the chunk text and converting that into numerical embeddings.

28:58

So if your embedding model is not a good quality, the numerical embeddings will not be right.

29:03

Embedding models are responsible for that. They are responsible for taking the chunk text and converting that into numerical embeddings.

29:10

That's what your embedding models will do.

29:13

So that is another point of failure.

29:15

If you make the wrong choice, how well you're managing a vector DB.

29:20

Is your vector DB updated?

29:21

If some new documents are getting added, documents are getting removed, are you

29:25

updating your vector DB accurate, you know, is the administration team doing that correctly?

29:30

This is the same way that you update a relational database.

29:33

Let's say it's an orders database.

29:34

If new orders are getting created, you know, let's say somebody cancels an order,

29:39

orders getting deleted, whatever, you know, customer DB.

29:43

or employee database in an HR use case, a new employee is getting onboarded,

29:48

employees are getting fired, they're getting deleted from the database. Are you managing that

29:52

activity? That is also another point, point to highlight that will impact your RAC system efficiency.

30:00

We talked about three pointers, chunking, quality of chunking, second point is embedding,

30:05

third point is vector DB itself. And related to vector DB is also metadata. We had a conversation about

30:10

that also. Sometimes metadata can be very, very useful.

30:13

for retrieval.

30:14

Now, see, whenever you are trying to retrieve the relevant chunks, it is not only based on the question.

30:19

You are asking the question and we are retrieving the relevant chunks on the basis of your question.

30:24

That is the easy way we talked about.

30:26

The other dimension we also covered was, are you retrieving based on the right metadata?

30:30

So based on the question, I not only want to retrieve based on the question, but also based on the

30:34

metadata.

30:36

So that is also another factor.

30:39

Finally, the retrieval part, what is very important is how many chunks you are retrieving?

30:43

That is actually a very important factor.

30:46

Are you retrieving one chunk? Are you retrieving 10 chunks? Are you retrieving 50 chunks? Are you retrieving the optimum number of chunks?

30:51

If you retrieve two few chunks, it's a problem. If you retrieve too many chunks, it's a problem.

30:56

If you retrieve two few chunks, that means you hardly have any information.

31:01

So imagine it's a, it's a very broad question. Now, if it's a very broad question, the answer will be present across different portions of the document, right?

31:11

you know, imagine the Tesla use case that we had discussed.

31:16

It was a financial statement from the year ending 2023 December, right?

31:20

Now, if you ask a question, what is the future direction that Tesla is added as for the latest

31:26

financial reports?

31:27

Imagine that's a question I'm facing, I'm posing.

31:31

Now, that is not a, that is not a question that can be answered on the basis of a single page.

31:37

You can't retrieve one chunk and get the answer. No.

31:40

Tesla was like, I think if I remember, right around 400 pages, 360 some pages.

31:47

So maybe the answer to that question, which direction is Tesla?

31:50

It is present across multiple pages.

31:53

Maybe page number seven, there is something.

31:55

Page number 30, there is something.

31:57

And on page 130, right, my, page number 60, there is something.

32:01

Okay, Ali, sorry, there is a question.

32:02

What I'm trying to do is, I'm trying to go through my flow.

32:05

And then I think Akansu and you had to, I'm keeping those questions pending.

32:09

I will honor all the questions.

32:10

I'll take it up at the end. I'll keep a time for Q&A today. So just just just just

32:15

just just just just hold on to those questions for some time. We'll do it right at the

32:18

end. This will be easy. We'll complete the class and then I'll have enough time for questions

32:23

to them. So so the answer to the question will be present across different sections of the

32:31

document. Page seven may have. Page 12 kaipea. Page 157. Page 57 page, page

32:37

page 101 may have. So I cannot return.

32:40

a single chunk. I have to retrieve multiple chunks. If I here retrieve only one chunk,

32:45

I will not have the entire perspective. I will not have the entire context. So I need to retrieve enough

32:52

number of chunks. Enough. Enough can't mean that's not. Then that is useless. Then rag itself is

32:57

useless. The whole idea of retrieval augmented generation is can we make it more efficient. What are we

33:03

trying to do? Based on a question, I only want to retrieve what is required. But what is required does not

33:09

mean you retrieve all the chunks. Because if you retrieve all the chunks, what is the

33:12

problem? There are two problems. If you retrieve all the chunks, what are the two problems? Problem

33:17

number one, there'll be too many tokens you are passing to the LLM. It will be costly. So problem

33:23

number one, there are too many tokens. It will be costly. The context will be very, very big. So it will be

33:28

costly for the LLLM. Problem number two, you end up sending a lot of private confidential data

33:34

to the LLM. The language model will be an external API call, right? You're

33:39

you know, we are making a GROC API call or an open AI API call, whatever it is.

33:43

But you're sending that context outside. So that's why we will not retrieve too many chunks.

33:48

We'll only retrieve what is required. The minimum number of chunks will retrieve. So chunking and the

33:55

number of chunks you're retrieving is also a factor. Okay. So we talked about the kind of chunking

34:01

number one, embedding model number two, vector DB metadata number three. How many chunks are retrieving

34:08

number four points of failure we are discussing. Fifth and the final point of failure

34:13

will be finally the LNM itself. What kind of system message you have here? Have you curated

34:18

the system message correctly? Have you instructed the language model what to do? If something

34:23

goes wrong here, the response will be wrong. So you can clearly see why rags are difficult.

34:29

Rags are difficult because you can go wrong in any of these past phases. If any of the past phases

34:34

are wrong, your rag response will be wrong. And then you have to sit and debug where you

34:38

went wrong. That is by understanding this pipeline is very important. Okay. The templated demo

34:44

is easy, but this is oftentimes a very important interview question. They often ask you. They often ask you

34:49

that, okay, what are the points of failure? How do you debugate? What kind of things you do? So that's the

34:55

whole idea. Okay, the summary of Rags is clear to all of you. Moving on, the use case we are taking up today

35:01

is for a company called ABB. It's just a general enterprise that I'm taking right now.

35:08

It's a Swedish company. What is AVB? AAB is like a, it is a Swedish company.

35:14

Actually, it's a Swiss company, Swiss headquartered. And it operates in the field of electrification, automation.

35:23

It's an engineering company. Let's say this is a very core engineering company.

35:28

If you look at ABB the kind of work they do, they are a very core engineering company. They are doing a whole lot of stuff with respect to, you know, helping with

35:37

If you look at AI mode and just try to look at what ABB is doing. So they are basically specializing in electrification, auto motion. They, you know, they do a lot of robotics.

35:47

ABB is involved in creating a lot of robotics. So these are actually ABB robots that you will find in factory floors, right?

35:53

So this is the use case we have, ABB robots. You will find assembly lines and all. So they are doing a lot of that work. So this is the use case we have. We are taking a company called ABB.

36:02

And, uh, and we are trying to build a lot of. And we are trying to build a

36:07

RAD system on an original ABB manual. Right. So this is the manual that I've taken. And this is

36:18

this is available. It's not something that is very confidential right now. But we are trying to simulate a Rack. In a real world scenario, this document is something you will not see online.

36:29

But we are trying to simulate a rag system where we have ACS 880 primary control program firmware manual.

36:37

Okay. This is the.

36:37

kind of thing. I mean, again, this is a little technical. So you don't have to really know what is

36:42

firmware and all that. That is not the, that is not the objective of the class. Objective is to

36:45

talk about Ragn, not talk about ABB's business. But what I'm trying to simulate here is,

36:50

you can create a kind of a support assistant. So at ABB, one of the things that is very normal, because

37:00

ABB is into robotics and, you know, all these core engineering space. So they will have a very

37:07

dedicated support team, right? Oftentimes end users will have questions and I would say

37:12

the technicians who are working on these kind of systems, right? So you can see they will

37:18

let's say the robotics thing that we saw. Let's say that that AVP robotics arm is being used in

37:24

some automobile plant. Okay, maybe there's some company. Let's say Maruti. Maruti has purchased

37:31

ABB's robotic arms for for assembling their cars. And the robotic arm all of a sudden is

37:37

giving a red error signal. Why? What do we do?

37:42

So if you think from Maruti's assembly line, the assembly plant, the car assembly

37:48

planting Maruti, they are stuck right? Because ABB's arm is not working. What do they do?

37:53

Who do they ask? Like the traditional processes, you will call up the customer support and you

37:58

will talk to your dedicated support team. So they will have a different business support obviously.

38:03

Like it's not going to be like calling up bank customer care and waiting. No, obviously.

38:07

there'll be a relationship man. There will be a very high level, you know, engagement they'll be having.

38:12

You can make an instant phone call, get answers to questions. There'll be a dedicated L1, L2, L3 support

38:17

that will be there. Okay. What we are talking about now is can we completely automate this process

38:23

with a rag application? Okay. So that's the, that's the scenario we are discussing. So Marathi is

38:30

using ABBs, let's say, roboticams. It's working well, but all of a sudden it develops a defect.

38:36

what do Marathi do? What do the engineers in the car assembly plan do now?

38:43

So can we, can we build a system where whenever any kind of machine defects are coming, whenever any kind of

38:50

normal defects are coming, can we ask questions and get we immediately get answers to those

38:56

defects? That's one way to do that. So the ABB engineers have to ultimately figure out why

39:03

the robotic arm is not working. So they will have to investigate.

39:06

they will have to go through the, you know, let's say the manual, they will have to go through it.

39:10

They will have to figure out what's going wrong, what's not going wrong. All that has to happen.

39:15

But can we effectively automate this process where any end user can ask the question and it will go through

39:28

the entire manual and it will generate the answer on the basis of that. And what we are talking about

39:33

is not just from an ABP perspective, but we are talking about, like, everybody knows

39:39

this. Everybody already has seen how to build this kind of a system, but this is actually a very game

39:45

changing thing, you know. It's actually like very scary because we are talking about automation of

39:50

everything for that matter. Everything. Everything technically, you know, the whole support

39:56

landscape can get automated. I'm sure everybody has faced scenarios where

40:03

Maybe your television has a problem.

40:05

Refrigerator is having some problem.

40:06

A.C.

40:07

there's Amazon, you want to ask some quick questions about certain things.

40:11

And first thing we, you know, usually, let's say bank's some issue.

40:15

Credit card, you want to ask some questions.

40:16

And the first thing that comes to our mind is, okay, what is the customer care number?

40:20

Let me talk to them.

40:22

And the customer care is very inefficient across the board for a lot of reasons.

40:26

Okay.

40:29

And part of the reason probably is that they don't pay the folks much.

40:32

a Pasha and you go to the firm, come come. So there are a lot of reasons why maybe support is bad.

40:39

That's another reason. Now, can you technically and theoretically build an automation thing here?

40:49

Can you automate this entire thing? Not very hard to do. So theoretically, you can have, let's say,

40:59

Panasonic, taking its entire suite of consumer products, television, bridge,

41:06

AC, microwave, all electronic products. Take all the Panasonic manuals. And it's not very hard.

41:15

Panasonic's search for you. You'll find so many manuals. And they are publicly available. Product

41:19

manuals public. There is no rocket science about it. Product manuals are all public information.

41:24

Right? Panasonic Life Solutions India, washing machine in. If you have a Panasonic washing machine,

41:27

go. If you have a Panasonic washing machine, you've got user manuals for every single

41:30

washing machine. And now you tell me, how beautiful a drag use case will be seen. This, this is

41:37

what, what is meant by building stuff. This could be a case study you guys can do. This are

41:43

manuals low. Just focus on washing machines for the time being. Take, take all these manuals.

41:48

This is the PDF. This is the PDF. This is the PDF. They've got three PDF. Three PDF.

41:52

So it's a whole year. I know. 24 page of PDF. 25 page of PDF.

41:57

we're 18 page of PDFs. So take all these PDFs. They'll be probably across all the product lines.

42:04

There'll be, let's say, 100 PDFs. Take all the 100 PDFs and, let's say, put it into my demo template.

42:11

Whatever code we have shared, you can put it into the demo template and upka Panasonic rag ready.

42:16

So who are the users of the application? So end user will be more like a simple web interface.

42:23

You will go to Panasonic.com. There will be a text box.

42:27

You ask the question. You ask the question. What will happen? User query will go and hit the rag system and the rag system will look up the relevant chunks and give you the answer. Is it hard to do? Not at all. Do we have the technology for it? 100%. And as AI gets cheaper, well, maybe the only reason probably why you're not seeing this in action today is because let's put it this way the cost of AI is cheaper.

42:57

sorry, the cost of AI is more expensive than what it takes to hire a human being.

43:02

The day that economic advantage goes away.

43:06

I mean,

43:07

I mean, it's still cheaper today.

43:12

Comparatively cheaper today.

43:15

You know, let's say, now the call center in bed there.

43:16

But they are not paid a lot.

43:18

You know, you can do with it, right?

43:19

Maybe, maybe.

43:22

Mayna in $20,000 to give us to give.

43:24

If you are able to get the job done,

43:25

but okay, it's fine.

43:26

It's fine.

43:26

that's what control left mark.

43:27

That's what a lot of support agents are doing right now.

43:31

But the point is that,

43:33

that the money's $20,000 is not enough to build this rag system.

43:37

Because the tokens and all cost money.

43:39

And you have to also think from the end user's perspective,

43:43

the end user search can,

43:44

what kind of queries, building that entire rack pipeline,

43:48

hiring AI engineers.

43:50

So the people who will build this solution,

43:53

maybe Panasonic is realizing that,

43:55

like,

43:56

hiring those people for a year,

43:59

might as well I keep 10 people at my support paying them $20,000 a month.

44:04

Our work is going to.

44:06

So I think that's probably the only reason

44:08

why you're seeing all these things are not getting used.

44:11

But it's possible.

44:13

And, and guys, I encourage you to have this business view.

44:17

You know, learning should not be just,

44:18

you learn a topic.

44:20

Thik, perlia, rag is there.

44:21

So it's fine.

44:22

But these are the kind of things you have to tell in interviews.

44:26

You know, if, okay, so it's possible,

44:29

so companies, why not are not doing?

44:30

Companies are this for not because it's a cost advantage.

44:32

AI is very costly.

44:34

Setting up the infrastructure, hiring a team.

44:37

Rag, so, okay, but company cannot just do rag like a Jupyta notebook, right?

44:41

They have to build a team.

44:42

They have to hire people.

44:45

Now, you have to have a HR person.

44:47

People have a year's commitment to do CTC and if you do the numbers right now,

44:53

your team's CTC will be for four, five,

44:55

that. If you have a Gen AI development team, maybe if you've got 10 people in the team

45:00

approximately, you compare a CTC of 5-Pro with a CTC of, let's say, if you're, like,

45:06

if you're, like, if you're able to get something done.

45:10

Yeah, so that's, that's one viewpoint that I wanted to bring off. So whenever you're looking at any

45:16

of these AI solutions, always question, yeah, yeah, it's what do not doing. Because AI is

45:21

possible. That could be one factor. The other factor is obviously, to some extent, lethargy is there,

45:25

management buying is there.

45:28

And to some extent, it is just the attitude that, right?

45:31

But the, you know, people are happy, it's all this fine.

45:35

So that's another view point.

45:36

But I think that pattern is changing now.

45:39

So always keep questioning.

45:40

Always keep like questioning, okay, what?

45:43

Because we have all the technology for this today.

45:46

And they are doing it.

45:46

They're doing it in bits and pieces.

45:48

If you go to Amazon, if you go to Amazon,

45:50

Amazon is already doing it in bits and pieces.

45:52

If you look at a typical drag application,

45:55

So we can go to, let's say, I'm just going to give you a small example.

46:02

We've seen this before, I think, briefly I may I've discussed with you.

46:07

But we can see a small example.

46:08

Let's say I'm looking at a Samsung S26 5G phone as an example.

46:13

And if you can scroll down and Amazon has incorporated some aspects of rag.

46:18

Let's see, if you keep scrolling down, there is a section called Rupus AI.

46:21

You can ask Rufus for search reviews and question answers.

46:23

So I'll Sv's a question.

46:25

So they are doing a raguar.

46:27

Right?

46:27

But Amazon still as a customer care.

46:29

And that's going to have to keep it.

46:31

Because people still,

46:32

now people still, how people, how do people, how much do they say,

46:33

like, see, Panasonic, if you're, like, you know,

46:36

you and I, we are talking about it, so we know that.

46:38

But you have to also understand the normal average user.

46:42

Like, we are only like, what, point zero zero one percent of the population of India.

46:47

And it has nothing to do with being rich or poor.

46:49

Even some very wealthy people, they have probably zero IQ.

46:54

That's how much a little means.

46:55

how they make money. You know, you know.

46:58

So many people are probably wealthy, but they are probably zero IQ about tech.

47:02

Or IQ about anything for that matter.

47:04

They're probably the dumbest people who are sometimes, like, unfortunately rich in our country,

47:10

due to a lot of other means, right?

47:13

Now, the point is, he use can. That's the other use case.

47:18

You can build the solution.

47:20

Solution to be made. But who will be using it?

47:21

Like, you and I, people like, you and I can talk about it.

47:24

Because we know what is the thing.

47:25

You can go to Rufus AI and you can ask.

47:28

Now, your mind in the mind is the problem are,

47:31

that, hey, H-26's phone to buy,

47:34

how is the camera?

47:37

How is the camera?

47:39

What are people talking about it?

47:42

Yeah, we'll ask them, what are people talking about it?

47:44

What are people talking about it?

47:50

And we're, we understand that, we trust the AI for the,

47:55

for whatever it.

47:55

is right? But what will the average user do?

47:57

First, average user can't know that

47:59

there's Rupert's AI is not something that you see on the top, right?

48:04

Amazon won't do it.

48:05

Amazon will use their real estate for a lot of other stuff,

48:08

all marketing nonsense, but this is something that is way, way down, you can see.

48:12

Right?

48:13

So this is what it is, ultimately.

48:15

And you have to always keep asking, what is the business proposition?

48:20

Why is it not happening?

48:21

And who are the users, who are the end users?

48:24

So please,

48:25

keep asking these kinds of questions as you get into deeper projects and as you continue in your

48:30

journey, right? And yeah, this is the rag, by the way. What it is doing is, it is based on the question,

48:37

it is catching the relevant chunks from your reviews. It is fetching the relevant chunks

48:42

from your product description or whose case is, of course, answer video. This is what it is,

48:48

basically. Let's move on. Let's continue on. I hope everybody has the context right now. Just wanted to

48:53

take some time and brief you about what it is.

48:55

All this while in the classes, we have been just following a structure content.

48:58

So today is a little different.

48:59

It's a case study class.

49:00

So we have some more, you know, freedom to talk about many other things.

49:04

So that's why we wanted to use the time and tell you some other things also, like, you know,

49:09

how things actually work and the business context and all that.

49:12

That is also very important.

49:13

Okay.

49:14

So now moving on, let us come back to our demo.

49:18

This is the ABB use case.

49:20

We are once again taking up just to set the context.

49:22

So we will build the complete rag system.

49:25

where given the kind of question that engineers will ask, we will retrieve the relevant

49:32

chunks and give the answer.

49:34

So that complete end-to-end process starting right from reading the PDF file, creating

49:40

the vector DB, so that entire thing will be doing.

49:43

And the case study after today's session would be, today's the last module of this

49:47

module three, last session of module three.

49:50

And your case study would be to build a similar rag system for the Panasonic use case.

49:55

A Panasonicabana.

49:56

I may shan, I may shan, but you can, you know, this could be a great use case that people can

50:02

walk home.

50:04

Okay.

50:05

I will, I will ping everybody again next week.

50:07

And I would love to see one of you have a, let's say, a GitHub, like a GitHub thing ready.

50:16

Okay.

50:16

And, you know, maybe it's a little bit of a different topic, but I was watching this video.

50:24

this was a very nice video by, not exactly a video,

50:29

it was more of a speech that, that, uh,

50:33

Kunal Shah gave.

50:34

I think some of you might know Kunal Shah.

50:35

He was, he's the founder of thread.

50:39

And also very recently he has, like he has become the, uh, the head of WhatsApp.

50:47

Okay.

50:47

So this was a very nice video actually.

50:50

And, and, and what is this, what has this got to do with?

50:54

what I'm doing in the class right now?

50:57

What has this got to do with it?

51:01

So I asked you to build something and you must do it.

51:06

And I think you will get some inspiration from this video, right?

51:10

Like Kunal goes on to say that not something I am saying.

51:13

It was inspiring for me also because I think even I waste a lot of time personally.

51:18

All of us do.

51:19

And he's going on to say that typical Gen Z, most of you are the Gen Z crowd.

51:23

And I think it's important.

51:24

Because, you know, in this AI era, you have to be different from others.

51:28

There are hundreds of people who are wasting time doing frivolous things.

51:32

People are using AI for useless stuff.

51:35

They're photo, they're editing it, they're,

51:36

but how are you really using AI for productive things?

51:41

How are you building something?

51:42

Right?

51:43

Are you really taking the effort, using all the resources?

51:46

Are you really building things?

51:47

Like I've made Panasonic cashiered.

51:49

Now, a lot of you, most of you will,

51:51

you will, you will probably dose off.

51:52

Like, I'm just saying, are you,

51:54

really taking the initiative and actually going and doing it.

51:57

You know, you're going and doing it.

51:57

You know, it's like your regime in now.

52:00

Yeah, I'm made it.

52:01

This is our rag.

52:03

That's what I think Kunal talks about in this video.

52:05

Very nice, actually.

52:06

You know, how to, you can, you can kind of use it as a, you know,

52:10

kind of a very inspirational thing, actually.

52:12

I personally liked it.

52:13

You can hear out.

52:14

And there are a lot of other videos.

52:15

He don't a Raj Shiamani Kashar Shahar Shah Bhaj Kharbiya had been episode.

52:17

This also, I've been quite a good.

52:18

I mean it was a three-hour long video where he talks about success.

52:22

And I think, I think, uh,

52:24

A lot of you might relate to it because he's a typical non-IAT, non-IAM guy.

52:29

And when you see success stories like that, it is naturally inspiring.

52:32

So there's no, there's no big deal about a useless Ata Shambani talking about what he is,

52:38

because they are already like fairly wealthy.

52:41

But it's quite something when you have first generation entrepreneurs like Unal and, you know,

52:45

like some of our Indian startup, many of the Indian startup founders who have really worked hard.

52:51

And I think he's one guy who really.

52:54

personifies hard work.

52:55

So I think you will be inspired by this amount.

52:59

So he just has asked a question.

53:02

Is it possible to retrieve based on location rather than numbers?

53:07

She just, we usually don't do that.

53:10

The whole distance.

53:14

What do you mean?

53:18

You're saying this one?

53:20

He will retrieve the top, the top X percent of the top.

53:24

five chunks.

53:27

Ah, exactly. You're retrieving the top top three.

53:29

Correct. You're retrieving.

53:31

Why, you can do that.

53:31

You can absolutely retrieve based on a similarity threshold.

53:34

You can do that.

53:35

But top K, like, it is usually a bit more stable, I would say.

53:41

Because you will, like, let me give you the other thought she just.

53:46

How will you know that what threshold even take?

53:50

Maybe, maybe if you tell top three chunks or top four chance, it is more stable.

53:54

We have generally seen in application, that's the more widely used one.

53:57

But to answer your question, can you use a distance criteria?

54:00

Yes, you can.

54:01

That function itself has the argument where you can go and use it.

54:05

You can do that.

54:06

You can do that.

54:07

You know, if you put it inside Germany, you will get that answer.

54:10

You get that particular argument that you use.

54:12

You can do that.

54:12

Answer to your question is yes, you can.

54:14

Okay.

54:15

But generally, generally what we use is top K.

54:18

Top K is what is generally used.

54:19

Okay, yes.

54:22

So now,

54:24

Let us move on. Let us see this one in action.

54:28

So I think now we understand the context.

54:30

We understand what is to be done.

54:31

So let us see that entire workflow here over on.

54:42

So let me quickly go ahead and upload this one.

54:47

The ABB demo.

54:49

Is it the entire PDF file we will be uploading right now?

54:54

And this is again part of the 25th June folder.

54:56

As always, I have already uploaded the contents here for you, 25 June, which is today.

55:02

And next up, I'm going to go ahead and start the runtime just to ensure the runtime is correct.

55:07

Let me just validate it from the SD4 GPU.

55:10

I will install the necessary libraries.

55:13

This will take a wipe.

55:15

Let us do that.

55:16

This will take a wipe.

55:22

Arul, I can see your hand is also raised.

55:23

You want to ask.

55:24

something you can please ping me and please message on chat okay so it's installing okay okay no problem no problem

55:54

Thank you.

56:24

Thank you.

56:54

I mean, good question.

57:24

Next question is how to handle images and data.

57:26

I think while the packages are getting installed, I can talk a little bit about it.

57:31

So idea is the same.

57:32

You can use, you can effectively use different farcers.

57:37

So the biggest challenge commit in that case will be it is basically called multimodal data.

57:42

So here what happens is we have got the text.

57:45

So we are taking the data, we are creating the text chunks, and then we are creating text embeddings.

57:50

So what will happen with images is there are different liabilities you can use to separate the pictures.

57:54

So first you find those pictures and one of those libraries that you can explore

57:59

is something called PiMU PDF. You can use the PiMU PDF package to find out what the

58:06

relevant images are. And then what you do is just like we have discussed chunk embeddings. Every image

58:12

will be like a chunk and you can create image embeddings there. And just like we have got text embedding

58:17

models, you will also have image embedding models. So ultimately what you are storing in the vector

58:21

DB will remain the same. Ultimately the contents of your

58:24

vector to be you can think of it this way where you will basically have text chunks

58:28

and you might also have image chunks. Every every record is like a chunk. You can have text chunks

58:34

and you can have the embeddings for that. Similarly, you can also have an image chunk or an image itself

58:39

and have the embeddings for that. So both the ideas are possible. Now the thing is that how do you

58:47

go and separate the picture so that you can do using the Pymeo PDF library. You can explore that a little bit.

58:52

So there are some contents that you will be seeing that. Yes.

58:56

That's a very good question. If texts are present in the image, will it create embedding for that?

59:00

Well, in a way, it does OCR for that. It will do optical character recognition to extract the text from those pictures.

59:07

So let's say within the image, if there is some text that is present, then it will do OCR and it will extract that text out.

59:14

So that is again, the Pymeo PDF library will inherently do. Okay. Yes.

59:22

All right. So I think the runtime is now created. Let us restart the session.

59:31

And next, what we will do? We've already got the PDF file loaded. All of you remember that.

59:36

This is the part we are doing all the library imports we have seen before and we are instantiating the GROC client by setting the API key.

59:45

Once that is done, we will take the file, we will load the PDF file. This is the PDF file we are loading right now.

59:50

This is that same PDF file which I uploaded.

59:52

And this is the part we are doing the chunking. We have seen chunking before.

59:56

And we can see that there are total. The chunking is happening right now.

1:0:02

This is the chunking that is happening right now. All of you can see the code.

1:0:06

The same flow, exact same flow that we saw in the image.

1:0:15

And this is the initial part that takes a little time. Okay. We can see there are 1,034.

1:0:22

chunks we have right now. There are 134 chunks or there are 134 instances of those

1:0:31

texts that we have right now. And now based on that, we want to create a vector DB. I will use

1:0:37

this particular embedding model GTE large. I don't do there are different embedding models you can

1:0:41

also use. Specifically, I will take this embedding model and then I will take each and every chunk

1:0:46

and we will convert the chunks into their respective chunk embeddings. So first we will download that

1:0:52

embedding model, which is what we are doing right now. So first we will download that embedding model.

1:0:57

So, this is the model we are downloading right now. And we will go through each and every one of the

1:1:15

134 chunks and we will generate the chunk embeddings and store it in the vector TV. This is the part

1:1:20

where we are creating the vector TV. You can see.

1:1:22

So chroma from documents is the chroma DB that we are building. So from these chunks, give the chunks, give the embedding model, generate the chunk embeddings, and this is the name of the collection. This is the name of your database, basically. You're storing in this directory. That's the name of your database folder is created. And within that, your database collection is stored. Okay. So if we take a while, the vector DB creation usually takes some time. It will take a while to run. Let's wait for it.

1:1:52

Thank you.

1:2:22

Okay. And once this is done, we will go and quickly test the retriever. This is just a testing that we are doing. I will instantiate the retriever right now. So the retriever, we are trying to instantiate the retriever right now. So the retriever, we are trying to instantiate right now. So imagine I ask a question. This is a bit of a technical question I'm asking.

1:2:49

that my ACSAT drive just tripped with fault code 2310. What does this mean and what should I check? So this is a typical kind of question that engineers at ABB will be asking. Okay. So ABB is an engineering company and we are looking at a particular manual, a firmware manual for this particular product. You can see there's very technical things. Okay. So it's a very core engineering field and under normal circumstances, somebody will have to know this. Somebody will have to memorize it. You know, you'll have to like search through this.

1:3:19

is. But we are trying to now build a rag system where if I ask this question, if any kind of faults happen, if I ask this particular question, will the relevant chunks be retrieved? We are trying to test that. So the retriever will retrieve the top five relevant chunks and just to test what those relevant chunks really are. Okay. So these are a relevant chunk. So yes, my retriever is working. This is just a test we are doing. So yes, the retriever is working. Moving on. Now I will set the model name as

1:3:49

3.370 billion versatile. That is the name of the model. And this is the part where we will now load the chroma DB. This part is similar. And this is actually how the embeddings are stored. If you are curious, okay, you know, sign how are we actually storing the things? This is how it is stored. You can take a look at it. Chunk ID is this. The chunk content is this. And these are the chunk embeddings. Similarly, the next chunk ID is this. The chunk content is this. And this is the chunk embeddings. So there's the first 10 values of your embeddings. So this is the first 10 values of your embeddings. So this is what is contained in the vector.

1:4:19

DV. Now these numbers are like giving you the contextual information of your chunk. This is what is what the machine is doing. It is taking that entire text chunk and it is converting that into a bunch of numbers. And finally, we will do the Rack Q and day. So until now we talked about the part where we take the PDF, we create chunks and we create the chunk embeddings and we store in a vector DB. So that part is sorted. Now the vector DB is ready. And now we will simply query from the vector DB.

1:4:49

So that is what we'll be doing right now. So this is the general system message that we have already seen before.

1:4:56

Just like the Tesla one, we are seeing. You are an assistant who will answer user queries and APP manuals.

1:5:02

And you are also explicitly saying what will be given as input. So we will give you the question. And we will also give you the retrieve context that we can use to answer the question. So both we are going to give to give you as input. So what are the inputs we will be giving you? We will give you the original question. And we will also give you the

1:5:19

context that will be required to answer that question. So both the things we'll be giving you. So that is what you're able to, you know, see on the screen. So we'll be giving you the original question. And we'll also give you the retreat context that is required to answer that question. And this is how the user message template will look nice. If we contain the context and the question. And again, you can see, we'll see the full rag pipeline right now. So this is the original question the user is

1:5:49

asking my ACS 880 drive just stripped with a false code so and so. What should I check? And you know, this is just like you're

1:5:57

simulating a support assistant. Usually you will call up somebody and you will ask this question. But now, you know,

1:6:02

imagine the engineers at ABB already have a tablet. They have all been given a tablet on the floor and they can just go to

1:6:09

their tablet or they can go to the mobile phone. And this is actually happening, you know, because I know for

1:6:15

a fact ABB we have done some consulting engagements for them. So, you know, they are actually doing it. They are

1:6:19

they already have Abby chat board. They already have a particular built-in integrated application that is doing exactly this thing. So engineers can just open up that app. It can open up that application. They can ask that question and they can get an answer. So that's the big picture idea. So first we will retrieve. These are the retrieve chunks and then we'll compose the response. So this is that whole pipeline that you're able to see on the screen. So first the retriever will retrieve the relevant chunks based on the user input.

1:6:49

generate the context, curate the context or retrieve chunks are part of your context. So curate the context.

1:6:57

And now we will frame the prompt. So the prompt will consist of system system message, user, user message. This is what the whole prompt looks like.

1:7:06

So system, system message, user, user message, that's the whole prompt. Client chat completions create and we are in instant checking this thing.

1:7:12

So you can see right now, this is the answer to the question. So we ask the question, how do I change the model?

1:7:19

control mode to scalar on the ACSAP. What parameter is that? This is the question I'm asking. And this is the answer I'm getting. To change the motor control, you need to modify parameters. So and so neat and clean. Actually, this is the great use case where I was talking a little bit about how many chunks you should retreat. So this is a great use case where you do not need to retrieve too many chunks. Because the use case here is getting very specific.

1:7:49

grounded answers to questions. And if you look at engineers, engineers are not going to ask very broad-based questions.

1:7:56

Engineers will ask very specific focused questions. So based on a particular question, they will mostly be like one or two

1:8:04

parts of the document or the manual where that question is potentially present. So if you only retrieve a few

1:8:13

chunks, that should be fine. And another final thing about a rack system, if you all remember, I told you that

1:8:19

these RAG systems, if you do not know the answer, please say, I don't know.

1:8:24

This is a very, very important criteria. And what is this called? It's called groundedness.

1:8:29

So RAC systems should be grounded in the context. If you ask a question, if you go and ask a question

1:8:41

in that particular case, what will happen is, you know, if you ask a question that particular case, what will happen is, you know, if you ask a question,

1:8:49

that is not in the context. It is say, I don't know. So that's the way to look at it. Yes. It will be very similar,

1:8:55

that history one is very similar to what we have seen. So once you have the regular flow, history one, you just have to incorporate that while you go there. There's no difference there. So all you try to do now is. So here, what we are doing is a single turn, right? We are simply looking at a particular user question and you're getting a assistant response. Response has come. The only thing that you do in the history. The only thing that you do in the history. The only thing that

1:9:19

that you, you know, look at the history is now you're going to be saving that whole thing.

1:9:25

Okay? You're just going to be saving that whole thing. So that is how the whole thing will look like.

1:9:29

Otherwise, everything else will remain the same. Nothing else will change. So the entire code of the rag will remain the same.

1:9:49

you mentioned one URL which has system message defined and we can use it from there. I

1:9:53

did not understand the question actually. System message you have to define. There's no

1:9:57

like there's no URL for that. You have to write a system message display. It has to be a string

1:10:01

only. It has to be a string only. Okay. Otherwise what you need to do is URL. I think you are,

1:10:11

I think you are confusing this with your prompt versioning session. Right.

1:10:14

Ah, so prom versioning we up here. Here, you know, I'm trying to focus one on the rack part. But

1:10:19

have been from versioning perceptive. Like here what we are doing, um, it is we are just

1:10:24

defining the system message. And I'm, uh, you know, I'm, I'm, I'm hard coding this as a string right

1:10:29

now. I'm hard coding the system message as a, uh, as a string right now. If you see, this is my

1:10:34

system message. But you instead of doing it this way, you can sort it as a TXT file. You can create a

1:10:39

proms folder. How did we do it? We created a prompts folder, remember? And within the prompts folder,

1:10:43

we can say version one system. You can do that. Absolutely. So those learnings from the sessions where

1:10:49

still be there. Right. Here the focus is more on the rag part. That is more like what we are trying to

1:10:55

achieve. But yes, whatever other learnings we had, that will be there. That you will incorporate. That we will

1:11:00

incorporate. Okay. So few things about the prompt versioning, few things about, uh, uh, uh, unkate,

1:11:09

I think, uh, I think of Jason's they confused. Jason, Unquit was not that. Jason was basically the, uh, the schema.

1:11:17

schema schema was JSON. Jason is not the history. History was going as a day. Ha,

1:11:25

you can say that it's a station dictionary format, but initially we'll list Ksapsen stored that

1:11:29

they stored it like a list, okay. But internally, how you're right. I think key value pair

1:11:34

Jason Ksapsi you can think about it. Okay. Correct. You can incorporate that too. So all those things

1:11:41

you can absolutely incorporate. But we are seeing the general red flow. Okay. Now once

1:11:47

this is done. This is the answer to the question we are getting. We're getting the answer

1:11:52

to the question and now I want to test this application out. We want to go back and test this

1:11:59

application out. Let us see that. So we can absolutely go back and test the application out using

1:12:05

Gradio. What is Gradio? Gradio will help you create a small web app. A small web app you

1:12:12

will be getting. And in that application users can now go.

1:12:17

and ask the question and they can get a response. That is what Gradyo will do for you.

1:12:21

So you can see the most important thing in Gradyo is this particular function.

1:12:25

Rag QA a function. It will accept query as input.

1:12:30

Based on the query, you retrieve the relevant chunks.

1:12:34

Clear the context for the query. You combine all the relevant chunks and you get the context.

1:12:39

You have a context. And on the basis of that, you curate the whole prompt. This is the whole prompt that you are curating now.

1:12:45

This is that complete prompt that you're curating now. You can see.

1:12:50

System, system message, user message, and based on that, you're getting that response and you're

1:12:57

simply returning that prediction response. So this is how the radio application will be working.

1:13:03

We've already seen that. It's like that web interface where you click on it and you see that application

1:13:08

line. And what is it doing behind the scenes? It is basically doing this kind of a

1:13:15

a rest API call. We saw a little bit of rest APIs as well, right? All of you recall that

1:13:21

you're making an API request. You're getting a response back, right? All of you can see this one.

1:13:26

So this is the same thing. You send the query as input argument and the RAQ&A gets a response back. This is what is

1:13:35

going on behind the scenes. That is not an error, Abhiji. Abhiti you can ignore that. Even I got it. That is more

1:13:40

of a warning from the libraries. You can ignore it. As long as your cell shows.

1:13:45

that, you know, successful even ignore it together. So Gradio is live. I will say

1:13:53

g.r. interface. Let me launch it. So Gradio is live right now. And we'll be just going ahead

1:14:01

and testing that application. I will use the same query. The same query I used here for testing.

1:14:08

Let us use the same query.

1:14:15

So there goes the query. I'll be using it for testing.

1:14:18

So this is the grade you application we are able to see in the stream.

1:14:21

There is a small evaluation part. People who are doing it, you'll see this. This is this.

1:14:24

I have not talked about yet. This is something else. I'll briefly discuss it in a moment.

1:14:29

But you can go back and click on that URL and you can test the

1:14:34

the grade you application exactly how we have created. You can ask the question.

1:14:38

This is how the engineers at ABB will be using this application. They will have a

1:14:43

application or they will have some other mobile phone app, whatever. And they can ask the

1:14:47

question, and this is like the user message. And, you know, based on the user message, you are

1:14:52

retrieving the relevant chunks. And on the basis of that, you're getting the response.

1:14:58

So this is the way how it is working out. So Gradio is giving you a very beautiful way of

1:15:03

building a POC. But how early? I think that will be part of a future session. Yes, deployment we

1:15:08

will talk about. That is part of the sessions later. You can easily

1:15:13

take this one and you can easily go and deploy as a real application. You're already seeing an

1:15:17

application live on the screen. This is already a sample application that radio has created for you,

1:15:21

but you can absolutely package it and deploy it in a more robust way. What's that? In prompt

1:15:29

versioning, we can save it. Where do you keep that? We keep that here, right? If I take you back to

1:15:36

my prompt versioning session, no problem, no problem. From versioning, if you take a look at it,

1:15:43

Let's go back to our notes for a minute. You will be able to see that. It's beautifully described here. This is the way how you save it.

1:15:49

Hello? This is the way how you save it. Remember, you will be saving it like this. Your

1:15:53

Prong folder here. And in the prong folder, you'll be saving version 1, version 2, like this.

1:15:59

Got it, okay? This is just the TXT file. You'll be saving it just like a simple TXT file. Okay, or you can save it in the registry also. But this is one of the ways how we have seen it.

1:16:10

Okay. All right.

1:16:13

So now moving on, it's working. You know, so what is that reporting? What is that reporting? What do you mean? So this is all shared as part of the content, Ali. You're already seeing this as part of your content, right? Uh-huh. And now, all of you can try this out? Can you all try this out?

1:16:43

Just take a minute. Everybody Friday's out.

1:17:02

And maybe you can try it out. And maybe you can try a question or you can try a different kind of question. The question. The question that I used here was this one.

1:17:10

But you can try out something else.

1:17:12

Maybe if you ask the question, what is the weather?

1:17:16

What is the, what is the capital of India?

1:17:20

Like, you can see I'm asking a very general question.

1:17:23

And I'm, I mean, pretty sure the language model should be able to answer.

1:17:26

But it is actually not supposed to answer it.

1:17:30

This is what I meant by grounding.

1:17:32

Because remember, whenever you're asking a question, the LLM is not directly answering the question.

1:17:38

Based on the query, we are going back to the PDF.

1:17:41

We are retrieving.

1:17:42

the relevant chunks actually they are going back to the vector d b retrieving the

1:17:45

relevant chunks and then forminating the answer but if you look at what is the capital of

1:17:49

India my document has no reference to India and capitals and all that it's not a

1:17:53

geography book right it is a ABB manual so unfortunately the question that you are

1:17:59

asking you know it's well it's not supposed to know the answer but it'll be

1:18:03

interesting to see what what it says okay oh a lot of you are trying

1:18:12

a lot of you are trying together you can see it's stuck a lot of you are trying

1:18:17

together yeah yeah that's interesting good good that everyone's trying yeah but I

1:18:21

think it will take a lot of time otherwise yeah people can run it at your end you

1:18:24

can maybe I think a lot of you are together trying this because the radio is a

1:18:31

sample thing right so you can you can already start to see that real applications

1:18:35

will also suffer from this problem and now we of course

1:18:37

how much the real applications will also suffer from the same kind of problem right so

1:18:42

what is the capital of India.

1:18:46

It is like going to IRCTC and trying to book a ticket.

1:18:48

Sometimes when multiple people are trying to do the same thing,

1:18:51

the server will like crash and there'll be a lot of time it will take.

1:18:55

This is the same demo that we are seeing.

1:18:57

So Grady go back behind the scenes it is building an application server.

1:19:00

That server is over.

1:19:01

And whatever application you are seeing, this application is hosted on some server.

1:19:07

So because many of you are using it parallel.

1:19:09

Now we have linked share here.

1:19:10

So all sat together.

1:19:11

So now, look, here here slow will go.

1:19:13

So that is what is going on.

1:19:16

Now, look, I don't know, I don't know,

1:19:16

I'm going.

1:19:17

Now, capital of India, who's who knows that?

1:19:19

Everybody knows that.

1:19:20

But this is exactly how my Rack system is supposed to work.

1:19:24

Okay, because if you're asking any question that is not grounded in the context,

1:19:27

it will say, I don't know.

1:19:29

Uh, uh, uh, 100%, 100%, 100%.

1:19:33

100% gradio can be used in local also.

1:19:35

Now local maybe use can use it.

1:19:36

It will open up in your local host environment.

1:19:39

The problem is that, abid, the problem is that,

1:19:40

Now we did in, you know, in, uh, here we don't do it because here in Colab, uh,

1:19:46

you can't open up a browser locally.

1:19:49

That's the thing.

1:19:49

But if you're running this in your local BS code, you can absolutely do it.

1:19:53

Huh.

1:19:54

You can absolutely do it.

1:19:58

Absolutely.

1:20:01

I mean, there is not a lot you can do.

1:20:03

There is not a lot you can do because radio, this is the free thing that you are using right now.

1:20:08

I mean, uh, yeah.

1:20:10

So you need to build a more robust backend to make it work.

1:20:14

Like, this is just a free application we are trying us from a demo perspective.

1:20:19

And what is happening behind the scenes is,

1:20:20

you look, we, we're doing.

1:20:24

I mean, if you think about what we are doing, Amit, what are we really doing?

1:20:27

This server is running where?

1:20:29

You have to question that.

1:20:30

Where is this server running?

1:20:31

This application is, where is it actually hosted?

1:20:35

This run, where are you running?

1:20:36

You're running to run, I've told you to the link share.

1:20:37

Everyone is trying it.

1:20:38

But, you know, like,

1:20:40

Facebook.com.

1:20:41

That server run, exactly.

1:20:43

Collab in run on.

1:20:44

Collab is limited in hardware.

1:20:45

So you have to scale that hardware.

1:20:47

Exactly.

1:20:48

Like Facebook.com, Amazon.com.

1:20:50

It's what?

1:20:50

What are it?

1:20:50

Like, GitHub.com.

1:20:52

There's any link, docks.

1:20:53

Google.com.

1:20:54

What is it?

1:20:55

This is the website, right?

1:20:56

This is hosted on some server.

1:20:58

This is a web application hosted on some server.

1:21:00

It's a very powerful machine that is hosting this thing, right?

1:21:04

Hundreds and millions of people are able to simultaneously access.

1:21:08

But in unfortunately, in my demo,

1:21:10

Like, only in the class of 20 people we are struggling.

1:21:14

These 20 people are unable to simultaneously access.

1:21:17

Slow-hoda.

1:21:18

So this is the thing that we have to scale now.

1:21:20

We have to scale this infrastructure right now.

1:21:22

Because this is what we will have to do.

1:21:25

All right.

1:21:27

But again, this is used for sample, POCs and all that usually.

1:21:30

You will not be, you will not be using this in.

1:21:36

Another question that was related to this,

1:21:39

Ali was asking.

1:21:40

You know, Ali is asking, is stream-late better?

1:21:46

Yes, yes, stream-lit is definitely better.

1:21:48

Stream-lit is definitely better comparatively, I would say.

1:21:52

Stream-lit is comparatively a lot more, a lot better, and I would say it's more robust.

1:21:57

And it's, from a security perspective, stream-lit is also better.

1:22:00

So that's one way to look at it.

1:22:06

Okay.

1:22:10

Weishal has raised his hand.

1:22:14

Vishal, you want to ask something?

1:22:31

Okay, okay.

1:22:32

No questions?

1:22:32

Okay.

1:22:40

Again, as I explained, you know, there are some technical perspectives there.

1:22:44

Yeah, some technical perspectives are there.

1:22:46

So basically you have to run a load balancer.

1:22:48

You have to run load balancer.

1:22:49

You have to use kind of some infrastructure-related things, how you set up a server and all

1:22:53

that.

1:22:53

Those are, again, very different conversations, which will typically be done by infrastructure guide.

1:22:59

So, yeah, so front-end application, wherever you're hosting, you will have to use a load

1:23:04

balancer, and, you know, you'll have to keep your embeddings, vector dv, LLM inference, and separate

1:23:10

services. Use auto-scaling, things like auto-scaling is there, request queuing is there.

1:23:16

If multiple requests are there, request queuing hoga, caching hoga, and GPU workers will be used

1:23:21

for inference.

1:23:21

Kolap in already GPUs. So these kinds of things we'll be doing.

1:23:25

Infrastructure is not part of the sessions, Ali, but what we are doing is we are doing some

1:23:30

master classes on some advanced topics. So definitely some of these things we can talk about

1:23:37

in the masterclass. If you ask me in the curriculum, in infrastructure, a part of it,

1:23:40

It is not. We're not getting into. Because see, the whole idea of application development is a different stack all together. Like, what we are trying to see is, TK, you can use a Gradio and you can just build a front-end user interface. But full stack development is an entire beast all to go. Like, how do you build that application? How do you host? That is a very different tech stack altogether. It's a very different learning path altogether. I think at Masai, we actually, I think, if I'm not wrong, we actually have a complete course itself for it entirely. So Gradio is just giving

1:24:10

a very quick way of setting something up and deploying something. But this is a very different track altogether.

1:24:17

Usually a Gen AI person will not do this. Even if you're working in a big team, your work ends once you build a

1:24:25

ad pipeline. You will take that thing and somebody else and a different team member will be typically

1:24:31

building this front end user interface, the application part of it. And then there'll be another team member who will take care of the

1:24:40

server, the load balancer, some of the questions you were asking.

1:24:45

Amit was also asking like, who will take care of these, you know, things.

1:24:49

There's a separate infrastructure guy who will take care of it.

1:24:52

It's a completely server side alone you're talking about.

1:24:57

Ah. All right.

1:25:04

Absolutely. Absolutely. But React is not related to today's plus. But what you're saying is right.

1:25:09

tools and React are related. Yes. That's right. But there's not tools and React we are using today. Today is just Rag. It's just a rag recap that we are doing. Yes. Okay. Okay. Okay. Okay. Okay. Okay. Okay. I will encourage you to run this code once. Okay. And there's another very interesting conversation I'll be having with all of you. So so far we have talked about the recap of the rag. We have seen a very interesting use case. The title is a little different. Sorry. The title will be. The title is different here.

1:25:39

And next thing we will see, we'll have another interesting discussion on a related topic, how to evaluate a RAC system.

1:25:49

So far we have been discussing how to build a RAC system.

1:25:52

But now we will have a very small discussion.

1:25:56

Now this is not part of the curriculum, but I feel it is very important to discuss it because when you ask a question like this and we are getting this answer, who is going to evaluate whether this is right or wrong?

1:26:09

Have you ever questioned that? Like lot of you are using this UI, you're asking the question, you're getting some answer. But how do you know whether it is right or wrong? The evaluation is a very, very important criteria. In any LLM application, be it rags, be it agents, evaluation is one of the most important pieces. And the next phase of my discussion, now that we have built the full pleasured application as a small demo, we will see how to evaluate this application. It will be another small conversation we'll be having. Okay. So we can take.

1:26:39

a short break at this point in time. Let's come back and we will be discussing the evaluation piece.

1:26:45

In the meantime, guys, you can try to try to run it, please, try to execute it. I will keep my

1:26:50

co-lab instance running also. But please try to execute it. I think they should be working absolutely

1:26:55

fine for everybody. Okay. So I will see everybody back in Terminich.

1:27:09

Thank you.

1:27:39

Thank you.

1:28:09

Thank you.

1:28:39

Thank you.

1:29:09

Thank you.

1:29:39

Thank you.

1:30:09

Thank you.

1:30:39

Thank you

1:31:09

Thank you

1:31:39

Thank you

1:32:09

Thank you

1:32:39

Thank you

1:33:09

Thank you

1:33:39

Thank you

1:34:09

Thank you

1:34:39

Thank you

1:35:09

Thank you

1:35:39

Thank you

1:36:09

Thank you

1:36:39

Thank you

1:37:09

Okay

1:37:13

Okay,

1:37:17

Okay,

1:37:18

Welcome back

1:37:19

back,

1:37:20

Let's

1:37:21

Let's come back,

1:37:22

Yeah,

1:37:23

some of these are,

1:37:25

I think

1:37:26

I think

1:37:43

think it's not an error. It will, if you just restart your runtime, it should be fine. Okay, okay? So if you just take a look at it.

1:37:52

I'm getting the same thing, right? Can you see my code? You can see my screen also, right? I'm getting something similar. But this is okay. This is not a problem. I'm also getting

1:38:03

like it shows like an error. But it's okay. It's not an error exactly. Okay. Yeah, this is okay. You can ignore it. My code as it is will run fine. Okay. Make sure you install and then you

1:38:13

click on runtime and restart session. Yes, yes, yes, that's it. That's it. The code will run seamlessly. Yes.

1:38:21

Okay. So this is pretty much what we have for today. And this is one final bonus module, which I wanted to incorporate, which is effectively how to evaluate a Rack system. So, you know, all of you should know that. So I'm just going to introduce that idea to all of you. The evaluation part. It's very simple, very basic idea will be seen. And

1:38:43

what are the different methods and what are the different approaches that we use to evaluate a RAC system?

1:38:50

So I like to use this approach here.

1:38:53

We mainly look at two criteria to evaluate a RAC system.

1:38:58

One is groundedness and one is relevance, right?

1:39:02

So all this while we are sorted with asking a question, retrieving chunks, getting an answer.

1:39:08

We have seen enough demos of that already.

1:39:10

And we have understood enough use cases about that.

1:39:13

But it is very important, especially for an enterprise like ABB, because their technicians will be using the results of a RAC system to actually solve problems and all that. So it's very important to have the accuracy. So whatever answers we are getting, who is evaluating that. So that's where the judge will come in. So you can take a look at it. The LLM will look at the user query. It will look at the retrieve context and give a response. This is pretty much a Rack workflow workflow we have done.

1:39:43

And here we will use that response and pass it through one more language model.

1:39:50

There is one more LLM that we will pass it through.

1:39:55

Which will evaluate that response based on grounded tests.

1:39:59

So whatever answer the first LLM gave, the second LLM will evaluate that, okay, is that response supported by the retrieved context?

1:40:10

It is like you're asking another language model to check that, okay,

1:40:13

whatever answer was given, is that even supported by the retreated context?

1:40:16

That means, is that answer grounded in the context?

1:40:20

I want to make sure you're answering from the context and not from somewhere else.

1:40:24

The groundedness is a very important property of a rag and this is how we are evaluating it.

1:40:31

So if you are asking some question that is not in the context, if you say, I don't know.

1:40:35

So how do we evaluate that? So is the response supported by the retrieved context?

1:40:40

And second, we are looking at something called relevance.

1:40:43

relevance is saying is the response relevant to the query that is given to the query given to the query given to the context it is one more language model we'll be using here right now and this approach is often called LLM as a judge right?

1:41:00

So this is often referred to as LLM as a judge. So these are both LLM as a judge approaches we are using. This is also LLM as a judge.

1:41:13

Why do we call it LLM as a judge?

1:41:19

Because the first language model is looking at the question and giving an answer.

1:41:24

This is the same story we have talked about all through the class and pretty much the agenda of the module and the session.

1:41:31

Now, the another language model, another judge model, a second judge model will evaluate the response of the first model.

1:41:41

because somebody will have to be a gatekeeper, right?

1:41:44

It's like, you know, let's say you're doing some work.

1:41:46

Somebody will have to evaluate you.

1:41:47

Otherwise, what is the guarantee you're answering things correctly?

1:41:52

Right?

1:41:52

Somebody has to evaluate.

1:41:54

The first language model will give a response.

1:41:57

And the second language model will look at that response and rate that response on a groundedness parameter.

1:42:07

And rate that response on a relevance parameter.

1:42:11

And what are these things? Groundedness says is the response supported by the context and relevant says is the response relevant to the context query. Like let's say, if you look at the Tesla demo, you are asking the question, what is the annual revenue in 2023? Like the answer should also be revenue. Answer cannot be profit. If the question is, what is the annual revenue, the answer also has to be revenue. Answer cannot be profit. That's the way how we look at it.

1:42:41

Now obviously for the judge model, we will have, they will have a system message of their own.

1:42:46

The second LLM we will be using as a judge, they will have their own system message.

1:42:51

Just like the RAG LLM had a system message.

1:42:55

We wrote the system message, right?

1:42:57

Similarly, when we are building these LLMs, they will have a system message of their own.

1:43:03

Because ultimately, what is the end objective?

1:43:05

Ultimately, the end objective is I want a rating on a scale of 1 to 5.

1:43:09

I want the groundedness, judge to give a rating, that okay, how grounded the response is.

1:43:15

And I want the relevance just to give a rating, that okay, how relevant the responses.

1:43:21

I want two ratings. Now, in order to give the criteria for these ratings, I will have to write a

1:43:27

detailed system message here and a detailed system message here, which we will do, shall be.

1:43:35

Okay, and absolutely, she just, the judge will.

1:43:39

also have the RAG access. It will also have the retreat context and all that. We will see that.

1:43:42

I think the next diagram will clearly explain what you are saying. This is exactly how you can look at it.

1:43:48

This is what the second model will have. So the first LLM, you can see based on the user question,

1:43:54

A is the user question. You can see this one. A is the user question. And based on the retreated context,

1:44:00

you're getting the response. So the LLM one is basically the one that is looking at the question and the

1:44:05

context and giving the response. This is the story we've already seen so far.

1:44:09

This is the new part we are we are incorporating right now in the session.

1:44:14

This is LLM to as a judge.

1:44:18

This is the second LLM. It will have its own system message.

1:44:21

Remember, I will have to write a system message for this LLM.

1:44:25

And what is this LLN going to take as input?

1:44:27

It will take the original user question.

1:44:30

It will take the retrieve context and it will take the final answer that was given.

1:44:37

And based on that, it will come up with a quality score.

1:44:39

And this is the way how the judge model will be working.

1:44:42

It will evaluate the results of the first model.

1:44:45

That's a very good question.

1:44:46

I think,

1:44:47

Ali, in the development part of the workflow,

1:44:48

this is something that you will do on a small sample of test data.

1:44:51

Of course, you cannot do it for every single example because this will be costly.

1:44:55

Because the judge model is another LLN that you're using.

1:44:57

So usually the way you will do it is, you know,

1:44:59

you'll be doing it like, let's say, on a small sample of 20, 30 examples.

1:45:04

So you will handpick 10, 15 questions.

1:45:07

And on those 10, 15,

1:45:09

questions, you will run it through a judge and see what kind of scores you're getting.

1:45:12

So that is the approach that is usually used.

1:45:15

Okay. Yeah. So that is evaluation. Basically, it is like evaluation of how do we do

1:45:19

evaluation in the real world? Imagine you're a factory, you're manufacturing, you know,

1:45:24

you're manufacturing something like nuts and bolts and whatever, diameters, you know. How do we

1:45:34

evaluate that? How do you evaluate whether the factory is manufacturing things correctly? So the way

1:45:38

to evaluate that would be, you know, the way to evaluate that would be you have to go and

1:45:43

you don't, you don't evaluate every single nuts and goals that you're manufacturing. You take a small

1:45:48

sample of that, let's say, some 0.1% or 0.001% of the production that you're doing, and then you

1:45:55

do defect detection based on that. The same idea happens here. So you already built a rag application.

1:46:00

How do you evaluate whether your rag is working well or not? How does ABB do that? So let's say

1:46:05

here we already built a, you know, built a rag application.

1:46:08

application, how does ABB evaluate whether we built a correct RAD application or not?

1:46:11

So they will, they will curate a set of sample question answers. So let's like a sample question.

1:46:17

So like this, I will have 10, 15 sample questions I will curate. And based on that, I will, I will see how the

1:46:23

judge is able to, you know, ranking those responses. This is the way how we will do it. We'll take a

1:46:29

small sample. Okay. Now, so this is the thing. This is the idea of what the judge model is

1:46:38

use for, just to summarize the conversation again, the first LLM is responsible for giving

1:46:43

the RAG response. And the second LLM, we are using one more LLM to evaluate that output of the first

1:46:49

LLM. It is acting as a judge. Okay, there's another person, there's another gatekeeper that you're keeping

1:46:54

who will evaluate how the first person responded. And usually the second model is a more powerful

1:47:01

model. Now in our demo, we will not do that because we are using GROC. We are already using a 70 billion

1:47:06

parameter model. So we will stick to that.

1:47:08

we will stick to that, but then, but the way we will do it is we will use the same model

1:47:15

in our in our use case. Okay. So these are the two main parameters that you have, groundedness

1:47:20

and relevance. The groundedness says is the response supported by the retreat context. Relevance is,

1:47:28

is the response relevant to the query given the context? That means, you know, is the answer relevant

1:47:33

to the question? If you're asking a certain question is the answer related to that and groundedness

1:47:38

say, okay, whatever answer you're getting is that related to the context.

1:47:42

So just to kind of clarify, groundedness is looking at this part. This is groundedness. I'll call

1:47:50

it G. Is the response supported by the context? That is G. Groundedness is looking at these two things.

1:47:59

The relevance is looking at these two things. Okay, just to help you understand, relevance is looking at

1:48:04

these two things. That's relevant. And there's a third thing that usually gets talked

1:48:10

about. Like, we are generally in enterprise applications, we generally, we have seen these two

1:48:14

work fine. There's a third thing that usually gets talked about in books and articles. I think

1:48:18

I can't you answer to your question that Raga's is another like nonsense that people talk about. We

1:48:23

actually don't use it. Like, it's something that is generally taught in things, but, you know, in enterprise,

1:48:28

we usually build our own judges and I'll show you how to do that. But yeah, Raga's is a framework.

1:48:31

It's also a framework. And they talk about Rag tribe. And, and

1:48:34

And that is where they talk about the third aspect.

1:48:37

So we talked about, is the response supported by the query?

1:48:40

We talked about is the response supported by the context?

1:48:42

Groundedness got it. They add a third part here.

1:48:45

And this entire thing is called the Rack Trials.

1:48:48

Okay, you want to, you want to see a Google demo of that. We can see that.

1:48:51

So this is called a Ragt Rite.

1:48:54

Not very difficult. You can see this one.

1:48:56

Now that you understand the context is very simple. Very simple to relate to it.

1:49:01

This is a Ract Rite. Which is nothing in it.

1:49:03

So interviews in you ask about, right, what?

1:49:06

So what are?

1:49:07

What's not?

1:49:07

This right?

1:49:08

You can see this one.

1:49:09

So we already talked about groundedness.

1:49:12

We already talked about relevance.

1:49:14

These don't know.

1:49:14

The only, the only thing that you're incorporating is context relevance.

1:49:21

Is the question, is the retrieved context relevant to the query.

1:49:25

This one loop we closed here.

1:49:27

So this we talked about.

1:49:28

We talked about groundedness.

1:49:29

Is the answer based on the context?

1:49:33

We talked about this part, relevance.

1:49:36

That means is the response based on the query?

1:49:41

Now, the question, what's asking is, it based on the answer will, no?

1:49:44

This judge, he will evaluate it.

1:49:46

But here, I'm the third one judge,

1:49:48

do you know.

1:49:49

This is sort of theoretically, like, the frameworks have it, basically.

1:49:52

So it's not usually not required, because if these two are working well,

1:49:56

then this is definitely going to work well.

1:49:58

But yes, you can also look at something called context relevance.

1:50:01

But the whatever question you're asking is the context,

1:50:03

retrieved based on that.

1:50:05

This is used to sometimes evaluate the quality of your retrieval.

1:50:08

You asked.

1:50:09

The context retrieved is, are the chunks retrieved correctly?

1:50:13

Are you doing the right similarity match and retrieving the chunks?

1:50:15

So these three things, all these three things taken together will give us a very good understanding

1:50:21

of how my rag application is doing.

1:50:23

But I can't you to answer your question?

1:50:25

That Raga is the same thing.

1:50:27

Your Raghas in what is all library is made.

1:50:30

If you're installed Raghas for,

1:50:31

Python in import there.

1:50:32

And there is no.

1:50:32

Just a method is, that you can't do it.

1:50:35

But what we're not practical.

1:50:36

Like what we will see is a more comprehensive demo, how you can do it manually.

1:50:41

But yeah, Raga's will make this thing a lot easier.

1:50:44

You can just install a library and you can get it done.

1:50:46

Okay?

1:50:47

Yeah.

1:50:48

But idea is not to see Raga's because, you know, Raga's is, again, as I told you, not very practical.

1:50:58

In reality, what we do is we build our own judges because that gives you more control.

1:51:02

When you use predefined frameworks, Akanchu, what you have control limited

1:51:07

so in practice, what we do in industries, we try to build our own judges.

1:51:11

So Raga's in that control you have not.

1:51:13

So this is called a Ragt trial.

1:51:16

I hope all of you are clear with the concept.

1:51:19

The concept is how the response of the first LLM is evaluated by another element.

1:51:27

So we have groundedness evaluated, we have relevance evaluated here, and we have context relevance

1:51:32

is evaluated here. And now, let us go back to the ABB demo, whatever ABB demo we already

1:51:37

have discussed, and let us see the evaluation part of the thing here. Let us see it up. So

1:51:44

we here here here evaluation, how we are manually building the judge of Akansho. We're manually

1:51:50

how manually how we are doing the system message. You can see, you can't, you can't. You can't

1:51:56

this. This is just a library. You have it's going to import for or use this. This you cannot do in

1:52:01

brothers. But when we create our own judges, it gives you more control. So this is what we

1:52:07

prefer. So the groundedness judge is like the judge. So groundedness judge system message will

1:52:13

look somewhat like this. This is the template that I wanted to show you. You can see you are tasked with

1:52:19

rating AI generated answers. You can metric on what basis will you evaluate? Well, the answer should

1:52:25

be derived only from the information present in the context. Yeah, all know. Groundedness is nothing but

1:52:30

is the response supported by the context.

1:52:34

Answer, there's no other from here.

1:52:35

Answer context in the context. That is the metric of evaluation the judge will use.

1:52:41

And this is the evaluation criteria. On a scale of 1 to 5,

1:52:44

you have, you rate,

1:52:45

what the judge to bet you? And if it is not followed at all,

1:52:49

he's going to, if it is completely followed, his to 5 do.

1:52:52

So this is the evaluation criteria for the judge.

1:52:55

And these are some other instructions you can give to a judge.

1:52:58

And this is a very practical way how we do things. You know, we'll be, we'll try

1:53:00

always try to create our own judges instead of using some of these, you know,

1:53:04

predefined frameworks and all that, which are just libraries and functions. There are hundreds of

1:53:09

libraries. If you do a Google search as a library for everything today. Okay, but this is

1:53:13

what we do to retain more control. Okay. Similarly, we can also create a relevance

1:53:19

later system message. So same idea. And absolutely you can use a different LLM in the

1:53:27

evaluation code also. The reason why we are not doing this is

1:53:30

because we have Lama model. Lama is a good model. So we are sticking to that.

1:53:34

But typically this will be a, this will be a more powerful model.

1:53:37

Judge is always a more powerful model.

1:53:40

Because the same model is giving some answer.

1:53:43

Usi model to have rating. Rating should be done by a different guy.

1:53:47

Usually a more advanced model.

1:53:49

Rating should be a more advanced model. But for the demo purpose, we are keeping the same

1:53:52

rate of model. Okay. So grounded as judge. This is the relevance judge.

1:53:58

Similarly, we have the relevant system message.

1:53:59

and this is your user message template.

1:54:02

Judge, also is an LLM.

1:54:04

So LLM, if we have to again give the same story.

1:54:07

Story remains the same.

1:54:09

Judge is also a language model.

1:54:11

LLM2 is the judge, right?

1:54:12

Now, this judge's a system message

1:54:13

will.

1:54:14

It's a user message

1:54:15

is what?

1:54:16

It is the original user query,

1:54:19

the retreated context,

1:54:20

and the response that was given.

1:54:22

These three things you have to

1:54:23

give you.

1:54:24

How judge rating how will?

1:54:26

Judge to give us

1:54:27

that original question what asked?

1:54:29

Context retreated what was and response

1:54:32

what gave?

1:54:33

This is the three things

1:54:33

need to change.

1:54:35

Okay?

1:54:35

And on the basis of that judge will give a rating.

1:54:38

So you're here here

1:54:38

here here our user message template

1:54:40

question, context, query.

1:54:43

Run, we're.

1:54:44

The question is the way is.

1:54:45

How do I change the motor control mode to

1:54:46

scalar of this?

1:54:47

And then same story, the ragged pipeline

1:54:50

chunks retrieve,

1:54:51

retrieve, correct.

1:54:51

Response is a again.

1:54:53

And now this is the groundedness judge.

1:54:55

And this is the answer

1:54:57

the groundedness judge is giving.

1:54:59

us. You can see the groundedness

1:55:02

judge is telling me that

1:55:04

okay, the metric is followed

1:55:05

completely five star. That mean, whatever

1:55:07

question I asked, I got a response

1:55:09

and the metric is completely followed.

1:55:12

Relevant judge is saying, whatever

1:55:13

question I asked, I'm getting

1:55:15

five star, the metric is completely followed.

1:55:18

So we are successful.

1:55:19

Yeah, we have a question on. So this

1:55:21

judge is we have a question on. This

1:55:23

in the real world is done for multiple sets of

1:55:25

questions. You have automated can take

1:55:27

a list of 15 questions and you can

1:55:29

get a groundedness score.

1:55:31

Groundedness's how good. Relevance

1:55:33

and you can take an average.

1:55:36

And this enterprises can do

1:55:37

on a weekly basis, on a daily basis

1:55:40

to get a report that how is the ad application

1:55:41

working? Sometimes what happens is

1:55:43

the application deteriorates in quality.

1:55:45

But you can keep a track of these things here.

1:55:47

I hope everybody's

1:55:49

got us. This is a slightly bonus topic.

1:55:51

This was not originally part of the content,

1:55:53

but because evaluation actually

1:55:55

we will take it at a much later stage.

1:55:57

If you see the curriculum, we have

1:55:59

a much detailed discussion on evaluation

1:56:01

coming up later, but I felt

1:56:03

in rags it is important to know this, okay?

1:56:05

If we have an evaluation frameworks,

1:56:07

we will be seeing that here. And to some extent

1:56:09

this, you know, you're asking

1:56:11

to some extent, you know, here

1:56:12

we're talking about LLMs of

1:56:14

your Raghas and all that, but

1:56:15

but from a practical

1:56:17

real world perspective, as I

1:56:19

told you, it is

1:56:21

not that important.

1:56:25

All that is part of

1:56:26

later topics, okay? Cardways and all are part of later

1:56:29

topics. That is entirely coming in module 4.

1:56:33

I hope everybody

1:56:35

has the context of

1:56:37

what is, what is the

1:56:39

how do we evaluate a rag system?

1:56:43

So we have seen the whole context, how we

1:56:45

build the rag, how we take

1:56:47

a PDF, how we do chunking, how we

1:56:49

create the chunk embeddings,

1:56:51

how we store in a vector DB, and finally

1:56:53

how we are able to retrieve the relevant chunks and get the answer.

1:56:56

I hope that whole pipeline, that whole context is clear.

1:56:59

all the way down to evaluation.

1:57:01

Not only did we build a RAC system,

1:57:03

but the final piece of the puzzle is we saw how to

1:57:05

evaluate a RAC system on two

1:57:07

parameters, groundedness, and

1:57:09

relevance. And we actually saw a

1:57:11

third parameter, which is called

1:57:12

context relevant, which we haven't used

1:57:15

but this is actually called a RAC tribe.

1:57:18

Sometimes this is an interview question that

1:57:19

they ask you, they tell you what is a rag tribe.

1:57:21

So now you know what it is. So whatever

1:57:23

answer the Rags system

1:57:25

gave you, you are trying to evaluate that

1:57:27

answer on multiple parameters.

1:57:28

theme parameter may have evaluated the, okay?

1:57:31

So is the question supported by the,

1:57:34

is the response supported by the question?

1:57:37

Is the response supported by the context?

1:57:39

Is the context coming from the question?

1:57:41

So this is the aspects that the Rack pride is given.

1:57:45

Okay, this is a nice diagram.

1:57:47

Let me share this URL with you.

1:57:50

I will take up some questions with everybody,

1:57:53

but in the meantime, just to kind of close the general

1:57:57

agenda.

1:57:58

of what was planned for today.

1:58:00

And then I'll come back to you guys and take some questions.

1:58:03

So again, as we discussed it,

1:58:05

there's not any new learning.

1:58:07

New learning was the bonus learning.

1:58:08

That was an optional thing I just shared with all of you.

1:58:11

But the overall objective of today's session was,

1:58:14

you know, take a small document corpus.

1:58:16

We took a real document corpus here.

1:58:18

And we looked at the entire piece,

1:58:20

how we can, you know, load and chunk the documents,

1:58:22

how we can create embeddings,

1:58:23

how we are able to store in a vector div.

1:58:25

We recap those ideas.

1:58:26

We saw the small demo of that.

1:58:28

Okay, we saw that particular part.

1:58:31

We looked at how to configure retrieval,

1:58:33

how to create that LLM rag prompt.

1:58:36

We saw that.

1:58:37

And we also finally got grounded answers from retrieve chunks.

1:58:40

This is that final rag thing that we did.

1:58:42

You retrieve the chunks and you get that final grounded answer.

1:58:46

And finally, you package it as a simple, runable rag application.

1:58:49

Do you have the grade you or want to teach?

1:58:50

Yeah, and obviously the bonus part is an optional thing that I talked about,

1:58:53

which is the evaluation part.

1:58:55

The evaluation part is very, very important because remember,

1:58:57

no LLM applications, like none of it makes sense if you don't evaluate things

1:59:02

correctly.

1:59:03

So evaluation is a very, very important aspect of how people want it.

1:59:07

Okay, so this was the general agenda based on what we discussed today.

1:59:13

I'm just going to go back up and see if there are any questions if people have, and we will,

1:59:21

we will, our memory was, we talked about it in the last session.

1:59:26

So memory is again something that.

1:59:27

We didn't want to confuse too many things here.

1:59:29

So today was more of the rag aspect that we wanted to incorporate.

1:59:32

But now that you know it, that is an exercise for you, how you can incorporate it and how you can go back and build it yourself.

1:59:39

Tika, but we have seen that.

1:59:42

You can maybe go back to that same Tesla demo notebook that I shared with you.

1:59:48

You can look at that particular portion where we incorporate a short-term and long-term memory.

1:59:53

And that could be a small use case you can incorporate it.

1:59:56

You can try that out.

1:59:57

Yeah, yeah, so this checklist is something which is, I mean, this is an internal document, Amit.

2:0:05

I'm not sure if the link will be open.

2:0:07

It's not my document.

2:0:09

It's something the team shares with me.

2:0:11

I think it's an internal document.

2:0:13

So what I do is at the end of every session you might have seen, I show you this content, but

2:0:18

I don't think this link is accessible from outside.

2:0:22

I think this is an internal document.

2:0:24

If you go to Inconcment, I don't think it opens up.

2:0:26

I open it not open.

2:0:28

It's not a public, it's not an open access, okay?

2:0:33

Yeah, this is an internal document that only the Maasai team has.

2:0:37

But you have a curriculum to have, I think your content file is enough.

2:0:41

You don't need to worry.

2:0:43

Whatever we are seeing here is already part of your contents, but this is the internal document, basically.

2:0:50

Okay.

2:0:56

I just want to make sure I answer some of the questions.

2:1:03

I remember a couple of you asked me some questions in the beginning.

2:1:13

Just going to take five minutes for some questions.

2:1:20

You can actually use, yeah, production, I would not say there's not, there was one question by I can't show.

2:1:26

There's no one answer to that, obviously.

2:1:28

There are different types of vector DPs you can use.

2:1:30

Production-wise, I think if you look at Posgras, PG-Vector Ecota, it's very good, actually, I would say.

2:1:36

You can look up something called PG-Vector, which Post-GG-G-SQL gives you.

2:1:41

PimeCone is also a very good, fully managed database.

2:1:44

But, yeah, so you can see PG-Vector is a very practical choice.

2:1:48

I see Post-Gra, PG-Vector getting used a lot in enterprises today.

2:1:51

But the concepts remain the same.

2:1:53

The concepts remain the same.

2:1:56

That's one way to be correct.

2:1:57

Ali had asked a question, sir, Fais or Proma, which one is better?

2:2:00

That was Ali's question.

2:2:02

Ali had asked that question sometime back.

2:2:04

So, Ali, just to answer your question, FIS is better if you just want a raw vector search.

2:2:09

If you want speed, more control, if you want to quickly look up the information.

2:2:13

So FIS is better.

2:2:14

FIS stands for Facebook AI similarity search.

2:2:17

If you Google out FIS, so FIS stands for, you know, Facebook, AIS similarity search.

2:2:23

It is just used for that searching.

2:2:25

it is just used for the similarity matching.

2:2:27

It is not a core vector D.B.

2:2:29

It's not a persistent storage.

2:2:31

So it, let me put it this way, Ali.

2:2:35

FIS is just that index.

2:2:36

It is just the search.

2:2:38

But FIS is not giving you that database, physical database.

2:2:45

Like, vector divby in what?

2:2:46

You're here here here, Ali, you're actually building this stuff, right?

2:2:51

You're actually building a physical chroma DB.

2:2:54

You can actually see that.

2:2:55

D.B that we built.

2:2:56

So FIS is just the index.

2:3:00

But chroma is better for, like, it includes storage also.

2:3:03

So chroma includes storage also.

2:3:04

It includes metadata also.

2:3:06

If you remember the conversations we had around metadata,

2:3:08

Apsert, we've made up in the previous sessions, if you recall it.

2:3:12

That's one way to do that.

2:3:13

But as I say, for production teams, PG vector is one of the most widely used ones.

2:3:17

You can Google out something called PG vector.

2:3:20

I hope that answers the question for all purely.

2:3:25

Okay.

2:3:30

Amit, I think I answered that image embedding up.

2:3:32

And you can try out Phi Nu PDF.

2:3:34

Please try out Phi MU PDF.

2:3:36

That was one of your questions that you had at that time.

2:3:40

Yes.

2:3:43

All right.

2:3:55

A QDrent be here, I can't shoot.

2:3:57

But QDrent, honestly, personally, yeah, QDrent is also like PGVector and QDN both are actually quite popular.

2:4:04

If you ask me personally, like, I've, I've seen PG-Vector post-Gra use cases a lot more.

2:4:08

Because Post-Gra is a more full-fledged enterprise database.

2:4:11

So post-Gra-gra use cases are khan.

2:4:13

Another pattern that we are seeing in the industry today is that enterprises are like many traditional relational databases.

2:4:21

Like post-Gra SQL is also a traditional enterprise relationship.

2:4:25

and database management system, right?

2:4:26

So they are all increasingly incorporating vector search capabilities like PG vector has come.

2:4:32

So, yeah, so, you know, so that way, if PostGRoy is a bigger, PGVctors are more popular choice.

2:4:39

Because many enterprises were already using PostGGG, they're migrating to this now.

2:4:46

And Ankiata questions are, if I'm not wrong, both model and we'll have different, what do you mean both model will have different embedding?

2:4:55

I did not get that question.

2:4:56

What do you mean?

2:4:58

Please let me know.

2:4:59

Oh, yeah.

2:4:59

So, I mean, I think there was one question, Ali, absolutely, like, I'm very much reachable.

2:5:04

I think you have my LinkedIn also.

2:5:06

Yeah, I'm not that active right now.

2:5:09

Maybe the last few, but you can definitely message me.

2:5:12

I think some of you can definitely message me.

2:5:15

There I will be active.

2:5:17

Yes.

2:5:19

What is that?

2:5:21

We have, we use different models.

2:5:25

let's say.

2:5:26

No, that's okay, that is exactly what is required.

2:5:30

Ankit, I'm an example.

2:5:33

Let's say, Ankit, you're going to some competition.

2:5:35

You've done some competition. You've done something performed.

2:5:37

Song, hey, dance, whatever.

2:5:38

Let's take an example.

2:5:40

You have used your own embeddings for that.

2:5:43

Abbe, whatever you answered, whatever you responded, whatever you performed,

2:5:46

somebody has to evaluate you.

2:5:48

So the guy who evaluates you cannot have the same embeddings.

2:5:50

They will have to be more intelligent.

2:5:52

Judges will have to be more intelligent.

2:5:53

So, so that is the thing, right?

2:5:56

So that is a given.

2:5:57

Embeddings will be different for the models.

2:5:59

So your original LL and the judge LLN will be different.

2:6:03

That is okay.

2:6:04

So that's the intuition.

2:6:07

Okay.

2:6:09

Okay.

2:6:15

All right, guys.

2:6:16

So, yeah, so I think that pretty much you have your exam probably.

2:6:22

When is your exam?

2:6:23

Sunday?

2:6:23

or how is it when are we when are you having the module three exams?

2:6:36

Oh fifth july fifth july you have oh okay okay okay okay that is good that is good

2:6:43

that is good

2:6:47

oh okay wonderful so next we are starting out with uh

2:6:53

we are going to be starting out with the agentic systems that is what we will be doing

2:7:01

next step and that will be a much more deeper discussion on agents so far we have not really

2:7:08

gone into agents for this fight but now we'll be getting a little deeper into agents in the

2:7:14

next from the next session onwards and lots a lot of exciting things to come obviously

2:7:21

as another one and half months is a lot and a lot of exciting things to come obviously as another one and half months is

2:7:23

that we have left out.

2:7:26

And yeah, I think the team is also planning a lot of master classes.

2:7:30

We have a lot of other master class sessions that will also happen.

2:7:33

Because see, the curriculum is one part.

2:7:34

There is a certain thing that we have to stick to from the university standpoint.

2:7:39

But there's a lot of master classes that will happen.

2:7:42

Yes, yes, multi-agent will happen.

2:7:43

Abhijit, to answer your question.

2:7:45

Correct?

2:7:46

So a lot of exciting things are coming our way.

2:7:52

Right, right.

2:7:53

all right. So let's end here. I'm going to pass it over to

2:8:11

uh

2:8:13

uh yeah hi debu yes i'm going to pass it over to you

2:8:20

yeah thank you so much we went

2:8:24

we'll get into some other topics today

2:8:26

so yeah so i think we're pretty much on time and uh we can do the mente meter and

2:8:34

other things with you so and yeah sure sure uh thank you so much for the wonderful session sir so

2:8:41

So today we don't have any mintimated.

2:8:44

So since this is the walks off.

2:8:46

So I'll release the feedback poll everyone.

2:8:48

Please fill the feedback poll and then we can end up the session.