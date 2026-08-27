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

4:54

Thank you.

4:56

Thank you.

5:26

Thank you.

5:56

Thank you.

6:26

Thank you.

6:56

Thank you.

7:26

Thank you.

7:56

Thank you.

8:26

Thank you

8:56

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

Thank you

9:46

Thank you

9:48

Thank you.

9:50

Thank you.

10:20

Thank you.

10:50

Thank you.

11:20

Thank you.

11:50

Thank you.

12:20

Thank you.

12:50

Thank you.

13:20

Thank you

13:50

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

Thank you

14:38

Thank you

14:40

Thank you

14:42

Thank you.

14:44

Thank you.

15:14

Thank you.

15:44

Thank you.

16:14

Thank you.

16:44

Thank you.

17:14

Thank you.

17:44

Thank you.

18:14

Thank you

18:44

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

Thank you

19:30

Thank you

19:32

Thank you

19:34

Thank you

19:36

Thank you.

19:38

Thank you.

20:08

Thank you.

20:38

Thank you.

21:08

Thank you.

21:38

Thank you.

22:08

Thank you.

22:38

Thank you.

23:08

Thank you

23:38

Thank you

24:08

Thank you.

24:15

Hi, Hi, everybody. Very good evening all of you. We will start on here.

24:38

Thank you.

25:08

Thank you.

25:38

Thank you.

26:08

Thank you.

26:38

Thank you

26:41

Thank you

26:45

Okay.

26:49

Okay.

26:52

Hi,

26:54

Hi,

26:55

Hi, everybody.

26:59

Let me just

27:00

Let me just quickly

27:14

please share my screen and we'll get started here.

27:17

And today, today is a very interesting session.

27:19

And today's session, what we will do is,

27:22

it will be kind of an intersection of the rags and agents what we'll be looking at.

27:27

All this while across all our sessions, we have discussed about, I think we've done a lot

27:33

of rag-specific discussions and we by now understand the ideas of rags very well.

27:40

So today, the first part of the session, the way we will paste the class is,

27:44

the initial part of the session, we will talk about some fundamental aspects of rags.

27:52

We'll just try to recap a little bit of basic rag initial part.

27:55

We will talk about some evaluation metrics as well with respect to rags.

27:59

And then from there, we will connect rags with agents and we will discuss something called an agentic rag today.

28:05

So that will be the major new learning in the session along with some other related rag concepts,

28:09

some advanced rag concepts I will also cover.

28:11

So that will be the main agenda of the session.

28:14

So before getting started, let us quickly go ahead and talk about the workflow of retrieval augmented generation.

28:23

What is the workflow that we have discussed so far?

28:26

Okay, we have done this over several sessions and just wanted to take you through this diagram once again.

28:30

All of you must be remembering this very well by now.

28:33

So first things, first, what we do is we take a document.

28:36

The document can be a PDF file and a document file, whatever be the nature of your document.

28:41

First, you take that entire documentation.

28:44

You divide the document into multiple chunks. We talked about that, how you take the document

28:48

and how you divide the document into multiple, multiple chunks. You get chunks and then you store

28:54

those chunks in the vector dv. Because remember, machines cannot process text. So whatever

29:00

chunks you get, it needs to be converted to embeddings, and you need to store all that in the

29:04

vector dv. So the vector dv, so the vector dv will basically consist of your individual chunks,

29:09

the chunk rows it will contain, and it will also contain the embeddings with respect to the chunks.

29:14

Okay, repeat again, the vector db will basically contain the, excuse me, the individual chunks.

29:20

It will contain the individual chunks and it will also contain what are the, what are the specific embeddings that we are getting with respect to the chunks.

29:28

That is what the vector db, you know, will fundamentally contain.

29:31

So we talked about that as well. We saw that as well in detail, right? And this is the initial part,

29:36

what will happen during the, during the vector db creation. And now, if you, if you

29:44

you, during the retrieval part, the querying part, what will happen is if anybody asks

29:48

the question, you retrieve the relevant chunks, right? This is the retrieved context and based on that,

29:52

the LLM will generate the answer. So why do we call it retrieval, retrieval, retrieval augmented

29:57

generation? Because usually, you know, in normal use cases, what we have done, you ask a question

30:03

and based on that, the LLM gives the response. Like you straight away feed the query and based on that

30:08

the language model will generate the response. But we discussed about some of the limitations of this

30:12

approach. We said, okay.

30:14

This is how, this is not the best way to go about it. Okay. And why did we say that?

30:19

Because, okay, so what if, what if your question is related to proprietary data, confidential data,

30:26

that the language model is not explicitly trained on? What if the large language model is not

30:31

explicitly trained on proprietary data, confidential data? It doesn't know the pattern specific to that

30:36

kind of data. So if the language model is not explicitly trained on that kind of data, what you will do?

30:41

So in that case, you ask the question.

30:44

you retrieve the relevant chunks. You will feel both of them as the context and based

30:50

on that you generate a response. So this is the way how the large language model will basically

30:54

work out. So you ask a question. So the query will go as an input. Based on the query, you

30:58

retrieve the relevant chunks, right? So based on whatever question you're asking, you will go and

31:03

retrieve the relevant chunks from the vector db. Both will be the input to the LLL. You'll make

31:08

the API call with respect to that and based on that, you will generate a response. So that is how the

31:13

a workflow is happening. So we talked about this in detail and we were able to use

31:19

Langchain. If you remember in the Tesla demo, we were able to use Langchain. Langchain gave us the

31:23

libraries for doing all these things. And then we also had conversations around some of last session

31:32

particularly. We also had a conversation around evaluation. That was also a major part of our discussion

31:36

where we discussed about how to evaluate the rag pipeline. So not only is, is it important to

31:41

build the rag, but it is also very, very important to ensure that whether your system is giving

31:47

the right answers or not. And if you remember, we talked about the rag right, I'm again highlighting

31:51

this because this was, this is I would say, one of the most important aspects. How do you know whether

31:57

your rag is working on, whatever pipeline you built? And there are so many variables from them. I mean,

32:03

if you look at this pipeline, there are many variables. You know, we have chunking. There are different

32:08

types of chunkers available. There are different types of chunkers available. There are different types of

32:11

of embedding models that you can use. There are different types of retrievers you can use.

32:17

You can also decide how many chunks you want to retrieve. There are so many parameters to configure.

32:21

Even when you talk about chunking, fixed size chunking, if you remember there is something

32:25

called chunk size, chunk overlap, how do you decide those values? How do you know what values to use there?

32:31

How do you configure those parameters? And the only way to do that is if I am evaluating my rag

32:38

right until the end and if I'm figuring out how to

32:41

my rag pipeline is actually working? And there are different ways of doing that.

32:46

I will show you some fundamental ways of doing that. But in the last session, we talked about a very

32:51

robust approach, which is referred to as LLM as a judge. That means whatever final response the

32:58

language model is giving you, you will use that and you will pass it through a judge model. You will pass

33:04

that particular response to a judge model. You can see this is the context what we talked about.

33:08

You ask the user question. Based on the user question, you retrieve the context and based on that, the first LLN will generate the response.

33:15

Right. Again, I repeat, you have the user query. Based on the user query, you will find the retrieved context.

33:22

And based on that, the large language model will generate the response. That's the way how we looked at things so far.

33:28

Right. So question, context and response. The first LLM will do that. And the second LLM, so whatever response you're getting, the second LLM will be responsible for taking that particular

33:38

and it is going to act as a judge. It's almost like how you have a judge in a particular

33:46

competition. You will ask the judge to, you know, go and, you know, go and effectively evaluate the judge.

33:56

Right? So sorry, Ali. There were only two slides I used. Just in case I missed that, I will do it right away for you. Thanks for

34:07

reminding me, I will do that right away for you, just so that I don't forget again, okay?

34:12

Because I thought in the prior session, I uploaded one of my slides, but no, no worries, I will do that

34:16

right away for this.

34:18

This is a PPP here. Session four, we discussed here. And I will also, I will also share this one.

34:26

Here here. Here the diagram was, I, yeah, I've been shared here. But that's okay. I'll once again

34:31

put it as part of today's folder itself, okay? Let me do that quickly. Let me do that quickly.

34:37

So I will download the PPD. And both of them will be part of your 7th July folder, which is today.

34:45

So you can go to your cohort folder. These two no, I've made cohort folder in order. It'll be a very

34:52

nice summary in terms of all that we are talking about today. Just done that once again for you.

34:57

And these bachy joan we'll come to that conversation. After a little bit of summary and recap,

35:03

we will come to the very, very interesting case study today. So that's the main.

35:07

attraction for the session. You know, we're going to see that. We're going to see that case study. Okay. So I hope everybody remembers this. Everybody is able to relate to it. Again, I'm repeating this because it's so important. And this was only one

35:17

class where we talked about this concept. So I hope all of you remember the evaluation part. So whatever response, the first language model is giving, you will evaluate that response with respect to groundedness and relevance. So whatever answer the first LLM is giving, you will evaluate that response with respect to groundedness and relevance. And these

35:37

will be two different judges. So there's one judge that will evaluate based on groundedness is the response

35:43

supported by the retreat context. Very important. Like whatever answer the language model is giving, that answer must

35:49

come from the context. The answer must not come from like some random place and all that. So the answer must come from

35:55

the retreat context. That's the first thing we have to figure out. And the second is the relevant judge. The relevance

36:00

judge will say, okay, is the response relevant to the question that is getting asked? Because whatever the rag model, the

36:07

response the rag model gives you, is that answer relevant to the question that is getting asked.

36:11

So that is the relevance judge.

36:13

Okay, so we also talked about the rag triad. And this is how the other diagram looks like. What are the

36:19

inputs the judge will be taking in? You can see this one as well. The first LLM is the, the first large

36:25

language model, the normal LLM. It will take the, so the normal LLM will be responsible for, I would say,

36:32

you know, taking the user query, taking the context and based on that generating the rest of

36:37

the first language model will do that. It will take the user question. It will

36:42

retrieve the context and based on that, it will generate the response. That's what the first LLM will do.

36:46

The first LLM will be responsible for that response generation. And the second LLM, the judge model,

36:52

will take the user query as input. It will take the retreat context as input. And based on that,

36:57

it will also take the response as input because the judge also needs to know that, hey, if this was

37:01

the question, what was the answer that was given, it will take all those things as input. And based on

37:06

that it will come up with a quality score. It will come up with a roundedness score and

37:10

it will come up with a relevance score. It will come up with a kind of a quality score on a scale of

37:14

one to five, one being the lowest and five being the highest. So this is how judge is very,

37:19

very important. And judge comes in very handy when there is no ground truth. So, and usually it's a more

37:24

powerful model. The judge model is usually supposed to be a more powerful model. For example, if you're

37:30

using a GPT 5.4 mini model for the normal LLM, the judge should be ideally a more powerful model. Because

37:36

the judge should have more context. They should never be the same model. Mind you, LLM1 and LLM2

37:40

should not be the same model. So the first language model is giving the answer and you're asking

37:45

the same guy to evaluate, that's not the right thing. It'll be biased. So in order to ensure that the

37:53

result is, the evaluation is objective. You want the first language model to generate the response

37:58

and you want the second language model to effectively rate that response. A second and a different and a different

38:04

and the more powerful language model will rate that response. It's like a teacher.

38:08

Let's say, you know, you're all students. Like, let's say I'm the teacher. I'm just saying,

38:13

at least I know something more than you, probably. So I'm the teacher. So I am LLM 2. Think of it that way.

38:19

So you will do the exam. You will, LLM 1 will write the exam, generate some answers. And LLM 2 is me.

38:25

I am the judge. I will rate your answers. I will evaluate your answers like that. Okay. So if I ask you

38:30

only to answer and you only to rate, everybody will rate themselves five star.

38:34

everybody will be so that's the idea right so you should never use the same model as the judge

38:39

okay just the concept see whenever you think of these ideas know i i would say always think with

38:45

respect to analogies it can make make it very simple always think of real world analogies see okay

38:50

this is how you look at LLM is nothing but like a human brain it's like a human being think of it that

38:55

way okay so LLN 1 is one is one person who is generating the answers and LLN 2 is another person

39:01

another guy who is acting as a judge think of it that way okay

39:04

And the final part of the conversation we looked at was the idea of the rag triad.

39:11

We actually looked at this particular diagram. This was a beautiful diagram we saw last session.

39:19

And here we introduced one more important method, if you remember. So we already covered groundedness.

39:24

Groundedness is a very important property of a rag system. Groundedness, in fact, is an extremely

39:28

important property of a rag system, I would say. And on top of that, we also covered something.

39:34

called relevance. And groundedness, why is it important? Because it is important for the

39:38

Rags system, the answer should be grounded in the context. The answer should not be some generic

39:43

answers that you are giving. The answers must be grounded in the context. That is why the groundedness is

39:48

such an important criteria. So you ask the question, retrieve the context and you generate the response.

39:55

Whatever response you're getting, whatever answer you're getting should be based on the context.

40:00

The answer should not be based on something else. It should be based on the context. And that's

40:04

groundedness and the relevance tells you that whatever answer to the question you are getting,

40:09

that should be based on the question query that is asked, that is answer relevance. And finally,

40:13

the other thing that we have here is something called context relevance. What is context relevance?

40:19

Based on the query, are we retrieving the right context? That is the other aspect. Based on whatever

40:26

question that is getting asked, are we even retrieving the right kind of context?

40:31

Are we retrieving the right context? Is the retrieving the right context? Is the retrieved context

40:34

relevant to the query. Okay. And this is actually very important, especially while you

40:39

are trying to evaluate the performance of a rag system, I would say. If you're looking at the

40:43

performance of a rag system, these things are actually very, very important. So this retrieval

40:47

thing is very, very important. You want to know that whether the right kind of chunks are retrieved,

40:52

whether the right information is retrieved. So that is actually very important. Because if any

40:57

issue happens in the rag, usually the flaw will be in the retriever, usually. Maybe it will be in the retriever.

41:03

Maybe based on the question, the right information was not written. So that's why the

41:08

context relevance metric is a very important score. And this is going to be another judge model.

41:14

Right. And this will be another judge model, which will look at the question. It will look at the

41:19

retrieved context, whatever context or chunks we were able to retrieve. And based on that, this particular

41:24

judge model will be able to, in a way, arrive at a kind of a score. Arrive at a kind of a score or

41:31

kind of a rating on a scale of 1 to 5 in terms of how the, you know, how the pipeline

41:39

actually is performing. So that's the way to, you know, look at this entire thing, rag, right?

41:45

Okay. Now, as I told you, friends, there are several avenues where rags can go wrong. There are

41:52

several aspects that are there. And one of the things that we can definitely do is we can, you know,

42:00

we can go back and do very basic level of checks, right? For example, if you see here in this demo,

42:06

very simple, very simple check we are basically doing. I've given you five document IDs. As an example,

42:14

we're just simulating a, simulating a very, very small demo here. So imagine I've given you as an example,

42:20

five document IDs, document one, document two, document three, document four, document five. In a real

42:25

world scenario, this will be chance. And we already saw that story. We already saw how you can take a

42:30

massive PDF, how you can divide that PDF into chunks. And then you can create embeddings and

42:36

saving vector TV. So this is like chunks. Imagine these are the five chunks we have. We're

42:40

simulating a kind of a real world example of a hostel notice board with five pinned policies.

42:46

Think of it that way. So hostel notice board. So hostel has different policies around different

42:51

things, attendance, late submission, library, more hostel mess refund, whatever, Wi-Fi access. The different,

42:58

you know, policies are there.

43:00

So there is a notice board and every row is like one chunk. This is the context.

43:07

And what is the objective that we are trying to, what is our objective right now? We are trying

43:14

to build a simple question answering system. Okay, I think at the level of what we have

43:19

discussing, this seems very simple. I'm just trying to give you some new ideas here. But this is a

43:25

very simple use case, right? So we have five chunks. In a real vector DB, there'll be,

43:30

thousands of chunks, but we are just simulating five chunks right now, five chunks. And next time

43:36

a student asked the question, the, we will retreat the relevant chunks from our vector db and generate

43:42

the answers. That is a big picture idea of what we are trying to achieve. Okay? So you can see right

43:46

now, this is how we can generate, we can go and create the mini corpus. Simple. We are simulating

43:52

this. As I told you, in a real world, you will not be manually giving the text, but here to simulate

43:57

the demo, I'm manually creating the text.

44:00

So corpus equal to we are having a list, document ID, title, text, same to same,

44:06

whatever we have here. These are the chunks we are actually creating. So we created five chunks

44:10

right now. And now the important part is evaluation. Right? Build questions. So, and so we are

44:21

going to build questions or evaluation questions, kind of a human evaluation we are trying to do.

44:26

So what we talked about a while back was, what we talked about a while back was evaluation

44:33

by a judge. That is definitely a very, very good approach, right? Where you try to measure

44:41

roundedness, you try to measure relevance, you try to measure context relevance. So you use

44:46

another LLM to evaluate the results on the basis of these parameters. Here we are talking about,

44:52

how can we do a round of human evaluation?

44:56

or let's just say more static keyword based evaluation okay so and it's important to frame

45:04

the evaluation questions have some evaluation data have some evaluation see when we are talking about

45:10

evaluating the rag how will you evaluate the rag you to frame the questions also somebody will have to

45:14

manually come up with that test data set yes data set means how will you test the model whatever

45:20

rag pipeline you're built i want to know how the rag pipeline is doing that means what somebody will

45:25

have to frame a sample question and somebody will have to evaluate okay whether that sample

45:30

question is leading to the right answer so that is what we are talking about the eval part right

45:36

and here for the purposes of the demo we are just saying an evaluation item is not only a question

45:42

it also names which document should support the answer so here we are keeping it only limited

45:49

to the question and the retreat chunks that's it

45:55

So user will ask a question.

45:56

Us to frame somebody will have to define that.

45:59

It's like an evaluation question.

46:01

Please frame the question.

46:02

And also please frame what is the respective chunk

46:05

that will answer that question.

46:07

This is the ground proof.

46:08

Evaluation, evaluation, that is your data.

46:11

You have to specify, okay, this is how I'm expecting the thing to be.

46:15

Test set, and then when the rag finally starts working

46:20

and when the rag finally retrieves the chunks

46:23

and gives the answer, you will check.

46:25

Rack's output is that matching your expected output.

46:31

So that is where we are trying to do that evaluation.

46:34

So this is evaluation using ground truth.

46:37

So whatever evaluation you are seeing on the screen right now,

46:39

this is evaluation we are effectively doing with respect to the ground truth.

46:43

There is some amount of ground truth that we are having.

46:46

So and just to give an idea to you, this is how my sample evaluation set looks like.

46:53

When it comes to the judge model,

46:55

there is no ground proof.

46:57

Judge-val model in what is what is.

46:59

As I told you, LLM as a judge, simple approach.

47:02

You are simply, you know, taking the question.

47:07

You are taking the retrieved context,

47:09

the context retrieved and you are taking the answer.

47:11

That's it.

47:12

Answer, what the first LLM answer did.

47:14

Correct or not, no, no.

47:16

You are simply, judge is only responsible for rating it.

47:19

So here there is no ground proof.

47:22

In the LLM as a judge approach, there is no ground truth we have.

47:25

We are not saying.

47:25

saying, okay, you know, answer this is a comparison we are doing.

47:30

The judge is using its own intelligence to figure out,

47:33

okay, question was this, context was this, answer is this,

47:37

the predicted answer, the generated answer was this,

47:39

whose basis score what are.

47:42

But what we are seeing in this particular flow is

47:45

we are actually creating a sample evaluation data.

47:49

It is like, you see, we have done SK learned machine learning, right?

47:51

It is like a test data set.

47:53

It's a supervised learning where we have done,

47:54

train test split. It is like a test data.

47:58

Test data, we have the actual answers.

48:01

Means based on these inputs, we are expecting these exact outputs.

48:05

We know the actual wise. Think of it like the actual vise.

48:10

We know the actual wise.

48:12

Abi model will predict some why and we can simply compare predicted with actuals.

48:16

That is all that we are trying to do there.

48:18

It is not much of an additional learning.

48:20

That's why we will keep this discussion short and we will get into some other influence.

48:24

things in the course of our session.

48:26

So let us see a sample evaluation set right now.

48:30

A sample evaluation set.

48:31

And one other very important thing I wanted to clarify.

48:36

Whatever evaluation thing, questions that you see right now,

48:39

these have to be created by domain exports.

48:42

So you need domain experts who have to go and curate these kinds of questions.

48:46

Somebody will have to go and curate these kinds of questions.

48:49

Somebody who understands the domain, who understands the business,

48:52

they will have to go ahead and they will have to curate these kinds of questions.

48:54

So, so if the question is like this, the expected document, it will retrieve is this.

49:02

This is what we call the test data.

49:06

We are actual answer many are we are only going to the chunk part.

49:09

As I told you, here our evaluation is only restricted to you ask a question and you want to see

49:15

whether the right chunk is retrieved.

49:16

So our focus right now is a manual context, context, relevance evaluation.

49:23

So this is.

49:24

Just like this story we are discussing, right?

49:26

So based on the query, did you retrieve the right context?

49:29

Whatever we were discussing with respect to the rag triad, context relevance, that is the same thing that we are talking about here.

49:36

We are just giving the ground truth question answers right now.

49:40

So based on the question, the expected document we want to retrieve is this.

49:44

Based on the next question, the expected document we want to retrieve is this.

49:49

Based on the next question, the expected documents that we will retrieve is this.

49:52

and we can validate that.

49:56

So what is the minimum attendance required?

49:58

Now look at notice boat in the question is this.

50:00

You tell me from the notice board, which document you think is the best chunk that you should retreat for the answer.

50:07

So question is based on minimum attendance required, right?

50:12

So if you look at document ID is chunk ID, right?

50:15

Yes.

50:16

If you look at the chunks, obviously based on that particular question, what is the minimum.

50:21

question, what is the minimum attendance required?

50:24

I can, I can ping this to all of you.

50:27

What is the minimum attendance required?

50:29

If you look at this question, the most relevant chunk is the first one, right?

50:33

Related to attendance policy, this chunk will be retrieved.

50:36

So if this kind of a question gets asked, that is my test data, mind you, test data.

50:42

Okay, other question here is, if the input X is this, if the question is this, the

50:46

retrieve chunk should be this.

50:48

So retrieve chunk what is?

50:49

Retrip chunk should be D1.

50:51

And that is exactly what I've done.

50:53

If the question is like this, the retrieve chunk should be D1.

50:57

And then what we will do is in the real world scenario, when the finally the rag pipeline is working,

51:04

you will see how the rag is retrieving.

51:06

So this is your expected retrieval manually.

51:08

A human export will look at the data and they will manually see.

51:12

Okay, based on this question, it should retrieve this chunk.

51:15

And now you can, you will see how the rag system is working.

51:18

So is the rag system actually retrieving that?

51:21

chunk. So that is the way how you will go about it. Right. Can I submit an assignment

51:26

one day late? Again, you're framing a sample question. These are like sample question answers we are

51:31

framing. It's just like a like you're creating a question paper. You want to see, okay, if this

51:37

kind of a question is asked, I want to see whether my rag is going to retrieve this particular

51:41

chunk. So in order to answer this question, can I submit an assignment one day later? Yeah,

51:45

assignment related question. So naturally the answer will come from documents too. Late submission

51:50

and policy related chunk. So D2 will be retrieved. So based on this sample question,

51:54

you can see the expected document ID or the expected chunk ID that will be retrieved this

51:59

D2. Okay, we are keeping it very simple in this demo, but in reality there can be multiple chunks also.

52:06

Evaluation data set in multiple chunks be host. Just to clarify. Is the library open on Sunday?

52:12

You're talking about open, close hours and running hours and all that. So based on this question,

52:19

what is the expected chunk feature?

52:20

it here we are saying D3 and indeed it is D3 because D3 is talking about library

52:25

hours. Okay. Next question, how do I get a MES fee refund? D4 and D4 is indeed talking about

52:34

mess fee refunds. And finally, if somebody asks a question, can a guest use campus Wi-Fi? Normal question.

52:41

A lot of people have questions about Wi-Fi key and whatever. You know, this is just one kind of question,

52:45

but you can ask some other question. You can ask some question, KTK, the speed is not good and the fast

52:50

it is not working, whatever. Whatever be the question related to Wi-Fi, the model will

52:55

retrieve the chunks on the basis from from D-5, Wi-Fi access. That's the way how it will basically

53:01

work out. And now, finally, we are going ahead and we are also defining one more question, which is not present

53:09

in any of the chunks. That is also a very good practice. Like we should always go and give one more question

53:14

that is not matching anything. Now, we want to test the behavior of the Rack system. If you ask the question,

53:20

that is not there in any of the chunks. The expected answer should be none. And that is,

53:26

again, we will have to evaluate that, okay, what, you know, we expect that none of the chunks are giving the right

53:31

answer. Actually, this room rent related thing we don't have. So the ground truth, the test data means

53:35

that, okay, there is no chunks that are going to answer this question. And now when the rag pipeline

53:40

eventually works, I will see what chunks are retrieved and I will match, okay, like, is it matching these

53:46

expected document items? If they are, then I will say that, okay, I have a, I have a decent.

53:50

and bragging. So there are two levels of evaluation we are talking about. One is a kind of a semi-manual

53:56

evaluation, what we are doing here. This is also equally important. As a human expert, you want to see

54:01

that, okay, if this is the question, this is the expected retrieved results, is it matching what actually

54:06

is happening? Okay. So this is also important. And the LLM as a judge approach is also important. That's a more

54:12

automated evaluation. Because every time the Rack gives an answer, the judge will be able to rate it. How well is

54:19

the rag doing. Okay. So that is that's a more automated kind of process. Okay.

54:25

Okay. All right. So, um, okay. With this in mind, yeah. So, uh, Anki has asked a question, sir,

54:38

usually we retrieve top three to five chunks. How will this be handled on the basis of rank?

54:42

Ankit, then you evaluate as a ranked list, not as a single chunk, I would say. If the correct chunk

54:47

appears anywhere in the top three or top five that counts as, let's say, a hit. Think of it like a

54:51

hit. Apeg hit percent. If it appears higher rank one is better than rank three, you can use some

54:57

kind of weightages, actually. And I would say if multiple chunks are relevant and you compare the whole

55:02

return set with the expected relevant set. Okay. So yeah, there's no, there's no fixed rule for these

55:11

things, but it's all at the end of the race up to you. What kind of computations you are defining?

55:17

So let's say expected there are five chunks, okay, and the rag is actually returning three out of five. You can decide a hit rate.

55:24

Apeg heat rate decide the 60% hit rate. So we are expecting five chunks, but out of five chunks, three are matching.

55:32

Three are matching. So yeah, it didn't completely fail. Three out of those five are matching. So 60% is the hit rate. Think of it that way.

55:39

So you can design your own metrics. You can also do a weighted kind of a metric. Right.

55:47

I would say Avishkar, it depends on like, yeah, not not like compulsory, but I would say if you ask me,

55:52

the judge process is much more relevant, much more important. And this is also equally important

55:57

in cases where you want a human expert to come in, a human evaluation to happen. Because sometimes

56:02

judges can give you wrong answers also, because judges are also an automated LLM that is doing the rating.

56:07

So sometimes if you see some kind of discrepancies in the judge results, then these kinds of things will come in.

56:13

Right. But I would say if you are asking me about a real world rag pipeline,

56:17

you will stick to the judge.

56:18

Whatever I taught you in the last session, you will stick to the judge.

56:21

You will stick to this method.

56:22

This is a very, very popular method, but a rack, right, is what is used industry by,

56:26

industry by everybody, everybody does rags this way, right?

56:29

You use a judge model to, you know, evaluate the response based on these metrics.

56:34

And if you see some discrepancies, let's say, you see some discrepancies, you know,

56:39

you're getting a groundedness score which is very low, but you don't believe it.

56:42

You don't believe, okay, how can the groundedness be this low?

56:44

So the judge is telling the groundedness is one start.

56:47

relevance is one star, but that's not believable.

56:49

So then you go back and use these kinds of human evaluations.

56:52

It's a process, I would say.

56:53

It's completely up to you how you design the application.

56:56

Right?

56:57

That's why we just wanted to educate you that this also exists.

57:00

But this is a very manual process, right,

57:02

where somebody has to manually curate the questions and the expected results.

57:07

And then you're comparing, you know, but judge was not the case.

57:10

Judge was completely automated.

57:13

Okay, Avishkar, I hope that answers your question.

57:15

Yeah.

57:15

Anket, how about you?

57:17

Yeah, all good.

57:18

Okay?

57:21

Yeah, but I want to clarify again, there is no hard formula.

57:24

Once again, it's completely up to you of Kasa formula.

57:27

Okay, you can do a weighted, you know, thing and completely up to you, okay?

57:31

Anyways, as I told you, this is an optional process that you will use, okay?

57:35

So, okay, let's move on.

57:47

I think this is what I was basically trying to say.

58:02

So you have the question ID.

58:03

Imagine there is a question ID, and this is how the typical rag application will work, right?

58:09

So based on a particular question question, you use a retriever,

58:12

retrieve the relevant chunks, and the relevant chunks you end up getting is this.

58:16

But the expected chunk that we expect is this.

58:18

You know, isn't it?

58:19

I told you that evaluation set we have.

58:21

So then this is a hit.

58:21

It's correct because we are expecting this particular chunk and it is retrieving.

58:26

It is retrieving that.

58:27

It is retrieving that particular chunk.

58:29

And now you can look at the order.

58:31

Which order in which order did it retrieve?

58:34

So not only is retrieval important.

58:36

We are also going to focus on the order.

58:37

What is the order of retrieval?

58:39

What is the most similar chunk?

58:40

So based on this particular question, if you tell me that yes, this is the most similar chunk,

58:45

then yes.

58:46

very good. Indeed, this is the most similar chunk and this is also the expected

58:50

chunk. So perfect it. Perfect. 100% accuracy. The rag is working well.

58:56

Whereas if you come to the second question, second one of question, let's say there is some question I

59:00

asked, but the actual rag is retrieving D5, D3, D1. It is retrieving three completely different

59:06

chunks, but the expected result is D2. So you can see how the semi-automated evaluation is

59:11

helping us. So we can instantly say that, okay, this is not in the expect,

59:16

retrieved documents. So it is a complete miss. So the rag is not working as expected.

59:21

We are expecting the rag to retrieve D2, but it did not retrieve D2 at all.

59:26

Third one case, again, it's a perfect match. D3 is retrieved.

59:30

Fourth one case, again, complete miss. Fifth one case, again, perfect match. You can say, this is the way

59:34

how you can kind of do the evaluation in a simple way. Yes, she just has asked a very good question.

59:42

She just, in fact, that is effectively a very good question.

59:46

you asked here. So the question by Shidush is that, okay, what do we do if the rag is not giving

59:52

us the kind of answers that we expect? What do we, what do we basically do if the rag is not giving us

59:57

the kind of questions that we are, that we expect you to answer? So a couple of things, I think I can

1:0:04

summarize this entire conversation for you in the same pipeline. And how will you know that your

1:0:10

that your rag is not doing well? What are the, what are the methods to know that? Number one,

1:0:16

the way to know that is number one, the method that you will use to know that your rag is not giving you the right results is your judge.

1:0:27

The judge scores will be less. Groundedness, relevance, both the scores will be low.

1:0:32

And the second way you will know is the human evaluation that we talked about.

1:0:37

What do you do now? Let's say your retrieval scores and your rag judge scores are coming out to be low.

1:0:43

So one of the things that you can do is you can do something called same.

1:0:46

semantic chunk. That is actually a very, very popular approach. We can do something

1:0:51

called semantic chunking. We can change the type of chunker that we want to use. Until now, what we did

1:0:58

changes first, we use normal fixed size chunking. Fixed size chunking is what we used, right?

1:1:03

This is a slightly advanced thing. In fixed size chunking, what we did was we are trying to effectively

1:1:10

look at the every 512 characters and we are creating a lot.

1:1:16

a chunk. Next 512 characters chunk. So every 512 characters we are creating

1:1:23

a chunk. This chunk is, one chunk, one chunk, right? Make sense. So they are contiguous chunks we are

1:1:29

creating. I tell you the problem with that approach. In fact, there is a beautiful article on

1:1:36

medium.com that talks about this exact same thing. There is a beautiful article that talks about this exact same thing.

1:1:42

There is a beautiful article that talks about this exact same thing. What is

1:1:47

semantic chunk? What is the idea behind semantic chunking? Let us see that. This is the idea. This is

1:1:52

the thing behind semantic chunking. What is going on? You can take a look at it. So what we talked

1:2:00

about initially in our Tesla demo was fixed size chunking. Let me bring this link to all of you.

1:2:05

It's a very nice article. Very nice article. In fixed size chunking, this is the most common and

1:2:12

straightforward approach to chunking. All of you recall this, right? We did this fixed size

1:2:15

chunking. We will see that. That is also another factor. I will summarize that. Don't worry. I'll

1:2:20

summarize that. And here, all that we are doing is we are saying every 512 characters you are building

1:2:26

a chunk. Every 512 characters, you are building a chunk. That's it. That's what we are doing,

1:2:30

basically. And this is very similar. This is very similar to what we talked about here. If you

1:2:36

remember, this was that analogy that we took. This was that beautiful diagram that we looked at. Now,

1:2:41

what is the problem here? Imagine you go back to the HR use case that we discuss,

1:2:49

right? Imagine you are trying to build a chatbot for an HR domain and you have an HR PDF file of

1:2:56

the company's HR policies around leaves, compensation, XYZ factors and all that. So if you do a normal

1:3:03

fixed size chunking, every 512 characters you are trying to create a chunk. Well, I mean, different ideas will come in

1:3:11

different chunks, right? Or the same idea can come across different chunks. You know,

1:3:15

imagine we have a massive PDF HR manual. Okay, imagine if we have a massive PDF HR manual consisting

1:3:21

of 100 pages, right? Now, you tell me, concepts about leave, let's say some kind of policies

1:3:31

around leave. Now, leave will not necessarily be only in one or two pages. Leave can be spread across multiple

1:3:36

pages. Let's say, uh, you.

1:3:41

regarding freshers. The company can have fresher policies. So fresher policy

1:3:45

is talked about in page number one. Okay. Page number one, they are talking about fresher's

1:3:50

leave. Page number five, they are talking about lateral employees' leave, people with

1:3:55

some experience. You know, page number 50, they are talking about leaves for people who have

1:4:01

sometimes people who have resigned, they've sent their resignation or they've applied for resignation.

1:4:08

What's what? Like, you're serving your notice period in the company.

1:4:12

Usually people are like, oh, resign

1:4:14

paper downed, and then all the leave used. But companies have strict policies around that.

1:4:19

They also know, he last 30 days nobody will work.

1:4:22

Kuch star may care. But my thing is that, okay, page number one,

1:4:27

there's something about leave is talked about.

1:4:29

Page number five, something about leave is talked about.

1:4:31

Page number 50, something about leave is talked about.

1:4:33

So we are seeing all these different aspects that are there.

1:4:37

different aspects of leaves that are talked about in all these pages. You can see.

1:4:42

You can dot or dot. If you look at page number 100, page number 100, something about leave is talked

1:4:47

about this time for directors. Absolute executives in the company. Their leaves policies are actually

1:4:52

very stringent. A director cannot just vanish. You know, they cannot say. So, yeah, I mean,

1:4:56

it's actually very stringent for them. So these are a leaf thing. Now think about it. If you do

1:5:02

a normal fixed size chunking, if you try to create chunks based on the number,

1:5:07

of characters. Like, what will happen is there will be different, different sections of

1:5:14

the document where the chunks will be there.

1:5:18

But I mean, if I give the analogy, every page is like a chunk.

1:5:22

You have a chunk one, or your chunk is five, or your chunk 50 here. And there is a chunk

1:5:27

100 somewhere. And all these four chunks talk something about leave. Think about it. Now,

1:5:32

imagine if a user asks the question, if a user asks the question about some,

1:5:37

some kind of leave policy. User is asking a question, am I eligible for leave or not?

1:5:42

Something like that. Okay, user is asking a question, am I eligible for leave or not?

1:5:46

Or what kind of leave policies are there in the company, in the organization?

1:5:50

The user is asking a straightforward question.

1:5:53

Excuse me, if the user is asking a straightforward question, what will happen?

1:5:57

You go to the vector DB and you will look up the similar chunks and you will retrieve all these four chunks, right?

1:6:02

Because all these four chunks are talking about leave.

1:6:04

You have asked a leave related question, right? But all the four.

1:6:07

chunks will be retrieved because they are talking about leaves. So all is good.

1:6:11

Everybody is happy. We all know this, right? There's nothing new that I talked about. But I'll

1:6:16

tell you the problem with this approach. This is all fine. What is the problem with this approach?

1:6:20

The problem with this approach is that based on a question, we had to retrieve four chunks

1:6:26

just to get the answer to the question. It will work. There is no problem. As I told you,

1:6:32

this is a straightforward baseline approach. What that medium article also says, right?

1:6:37

So you are asking the question and you are retrieving the four chunks.

1:6:42

Now those four chunks are talking about leaves. So no problem. Your question will be answered.

1:6:46

The problem is that you are retrieving too many chunks.

1:6:50

And too many chunks means there is too many tokens, too much of data, security issue. All that

1:6:56

will go to the LLM. That's the problem. If you're using normal fixed size chunking, like this chunk size

1:7:03

chunk over lab, this stuff that we talked about, character spliter, recursive character,

1:7:07

a text maker, the demo that we did primarily in the class. This is the limitation of this

1:7:11

technique. So these are the kind of things that you will have to get deeper into to improve

1:7:17

the rag system, she did. Okay, I hope this idea was clear to you. So first we have to identify

1:7:23

what is the problem. The problem is if a user asks the question about leave, in order to answer

1:7:29

that question, I have to retrieve all the four chunks. Now can I use a method?

1:7:37

using which I can retrieve lesser number of chunks. Now I don't want to retrieve all the four chunks.

1:7:43

Let's say I do not want to retrieve all the four chunks? So do I have a method that is available

1:7:48

which I can use to retrieve only a certain number of chunks, less number of chunks, what I can do.

1:7:58

So that is exactly what semantic chunking refers to. So in semantic chunking, what we do is

1:8:04

you can see. This is very nicely described here. The semantic chunking approach is very

1:8:09

nicely described here. It involves taking the embeddings of every sentence in the document,

1:8:16

comparing the similarity of all the sentences with each other, and then grouping the sentences

1:8:21

with the most similar embeddings together. So in semantic chunking, the chunks are not created

1:8:28

based on every 512 characters, no. So you have the entire

1:8:33

you know, PDF manual, as I will take the same HR manual that I was talking about

1:8:39

a while back, you have the entire 100 page PDF, the HR PDF that we have. And the chunks are not

1:8:47

just based on every 512 contiguous characters, no. But what you are now trying to do is you are not

1:8:53

trying to go back and see this 100 page PDF, this 100 page PDF. You find out all the sentences

1:9:01

in the PDF.

1:9:03

Let's just say this particular PDF has 10,000 sentences. I'm just giving an example.

1:9:08

We have sentence one. I will just call it a sentence one, S1, all the way up to S 10,000. There

1:9:14

are 10,000 sentences in this PDF. Sentences mean separated by pullstop. All of you can relate to

1:9:19

that kind sentences. The 10,000 sentences in the PDF we have, right? Now the interesting thing would be

1:9:25

we are going to group the sentences together. Sentences will contain text, right?

1:9:33

Machines don't understand text. So just like we discussed in chunk embedding, you use an embedding model to generate embeddings for your chunks. Similarly, you will use an embedding model to generate embeddings for your sentences. So sentence one, you will create what are the embeddings. Sentence 2, you will create what are the embeddings. So you will create the embeddings for each and every individual sentence. Compare the similarity of all the sentence.

1:10:03

with each other with respect to embeddings and then group sentences with the most similar embeddings together.

1:10:09

And that's the magic of semantic chunk. So what you will end up getting is something really, really beautiful.

1:10:16

You will end up getting, let's say, sentence one, sentence seven, sentence 50, sentence 50, sentence 50, sentence 42, all of these sentences will be part of one chunk.

1:10:30

Yeah, the first chunk of the first chunk of all these.

1:10:33

sentences are now grouped up in one chunk. Second chunk in more similar sentence. And the

1:10:38

best thing about this approach is that similar ideas are present in the chunks now. Like we were talking

1:10:45

about leave in the last use case. Last use case. You asked a question about leave. So all the chunks had to

1:10:51

be retrieved in different different sections of the period. Now here here here here this chunk is entirely

1:10:57

talking about leave only. Now you have got chunks which are based on topics.

1:11:01

It's all costly. But the cost is the initial cost that you're paying. You have to pay a cost if you want to improve retrieval quality, right? So definitely it is extremely costly. Extremely costly initially and it will take a lot of time. You do a normal fixed size chunking. The chunking will happen very fast.

1:11:19

Tesla's demo we had chunking came. It was super fast. It got done in like what, nine, ten seconds. The second in ten seconds. The second in a ten second in.

1:11:27

130 page of PDF. You are same to same code used. I'm

1:11:31

encouraging you. Same to same code use. It will take more time. Semantic chunking is

1:11:37

guaranteed to take more time. It will take much more time comparatively. That is one of the things to keep

1:11:42

in mind. But what is the benefit? It is a more accurate approach. And it is a very practical industry-based

1:11:49

approach we use usually. Because now every chunk is not just based on, okay, first five, 12 characters,

1:11:55

this chunk-he. Next is this chunk. No. But now every chunk is based on a idea, based on a topic.

1:12:01

So, okay, first chunk is about leaves.

1:12:04

Second chunk is about money, compensation.

1:12:07

Third chunk is about this.

1:12:08

Four chunk is about this.

1:12:09

So, half a different topics.

1:12:12

Irrespective of from which page the sentence is fetched from.

1:12:14

This sentence can be from page one.

1:12:16

This sentence can be from page seven.

1:12:18

This sentence can be from page 50.

1:12:20

The sentences are taken across all the pages in the PDF and similar sentences are grouped together.

1:12:25

And it's a very powerful approach.

1:12:26

Because abe jake, when user asks the question, the user will go and ask a question,

1:12:30

and how many leaves I get in a year, you don't need to retrieve four chunks.

1:12:35

You can only retrieve a single chunk.

1:12:37

Because this chunk in the sara leaf-related so one.

1:12:41

So what is the major benefit of semantic chunking?

1:12:44

The major benefit of semantic chunking is that if you apply a semantic chunker,

1:12:50

if you apply a semantic chunker, you can retrieve lesser number of chunks.

1:12:55

Okay?

1:12:55

So if you apply a semantic chunker, you can retrieve lesser number of chunks.

1:12:59

And if you retrieve a semantic chunker, you can retrieve lesser number of chunks. And if you retrieve

1:13:00

lesser number of chunks, what is the benefit? Because now you can, you are sending lesser number

1:13:05

of chunks to the LLM. So privacy part come here because you're you're sending less data to the LLM.

1:13:12

Second, the input tokens also reduce. So input tokens become okay. So in the inference side,

1:13:21

when users are asking real questions, post time pay you're retrieving lesser chunks. So that way

1:13:25

the running costs become low. So Ankit, I hope you're understanding the part.

1:13:30

initial upfront cost is very high.

1:13:32

Because here here chunking will be very costly.

1:13:34

When I say costly, it will take a lot of computation.

1:13:37

So initial one-time process your chelago.

1:13:39

During development time, the chunking will be fairly costly.

1:13:42

But after you build that rag pipeline, during inference, because remember, when end

1:13:47

users are using the application, those time,

1:13:49

vector d'b is made.

1:13:51

Every time you're not creating the vector db.

1:13:53

So this is the one-time costly process.

1:13:55

This part will be costly.

1:13:56

Here you have semantic chunking.

1:13:58

So it will take a lot of time.

1:13:59

You take the sentences.

1:14:00

create embeddings, group them into similar chunks.

1:14:04

The rest of the story remains the same.

1:14:06

Once you have the chunks, you create embeddings, store in the vector db one-time process.

1:14:09

This will be very costly due to semantic chunking.

1:14:12

But after this is done, after this is done, the vector db is ready.

1:14:16

Vector db ready.

1:14:17

So during the inference part, when the end user is asking questions,

1:14:20

you can do with only one or two chunks.

1:14:23

One or two chunks in your answer will be.

1:14:25

You can retrieve lesser number of chunks and the quality of retriever will also be good.

1:14:29

I hope that answers the question.

1:14:30

like, yeah, so what are the benefits specifically?

1:14:35

And Ali has asked a question, if a PDF has a lot of information about one topic and very

1:14:40

less information about other ones, then the chunks will mismatch dramatically.

1:14:45

No, so Ali, like that is the nature of my data itself, right?

1:14:48

So that is okay, because I am trying to create chunks based on whatever data is there in the

1:14:53

PDFs.

1:14:54

But yeah, you're right, absolutely.

1:14:56

Semantic chunking can produce uneven chunk sizes.

1:14:58

You're right, absolutely.

1:14:59

That's right.

1:15:00

say that's right. Absolutely. What you are saying, I absolutely agree with you. So if you're

1:15:04

saying that chunk sizes can be uneven, absolutely. That is normal because it follows the data's meaning,

1:15:09

not a fixed length. In practice, you add guardrails up. It's going to manage to make. What you can do

1:15:14

is have guardrails use for mint tokens, match tokens. You can merge tiny chunks. So what we do is

1:15:21

our first level semantic chunking caro, Ali. And after that, what you can see is, it's a very good question,

1:15:26

actually, by Ali. And if you see that there are certain chunks, which are

1:15:30

very big because let's say there is a like one of my chunks is talking about leaves

1:15:35

a lot and there are certain other chunks is like very small. So there are some strategies we use.

1:15:40

Okay, we merge them. Many tiny chunks we try to merge them together. They say you find this

1:15:44

is miscellaneous topic. So merge can use. So similar chunks we merge them. And if you see very

1:15:50

oversized chunks, we go back and like we split it. So that is one of the things that we go back

1:15:56

and do. Okay, so either we merge it or we split it and we try to balance it out a little.

1:16:00

So that is a very iterative approach. There is no one guideline that we use for that.

1:16:05

Whatever, whatever with the ratio, this is the way you will do it. You will either merge or you will actually or split. Either way you will do it.

1:16:12

Okay. Okay.

1:16:30

And so we talked about the chunking part. Very important. And all this.

1:16:36

Yeah, this is the manual process. This is the manual process. Yeah. This is the manual process.

1:16:41

So you'll have to keep a track of it and you will have to do this. This is the manual process.

1:16:44

Normal semantic chanker's code up. You have very simple. In our session, we already saw the,

1:16:51

we already saw the recursive character text glitter code. This is we know. Very simple.

1:16:55

Chung size, chunk overlap. We already saw this one. Very simple. Right. Even semantic

1:17:00

Chunker is also very simple. Okay, you can, in the same link that I ping you of medium, you can see the

1:17:05

semantic chunker code is also simple. See, now that you know, the ideas is very easy to implement it.

1:17:09

See the, it's just one or two lines of code. They are modules, they are blocks now.

1:17:12

Now, you can use this code can't semantic chunk in person. Yeah. But then after the chunks are created,

1:17:19

this part will be, have to be done manually. The processing part is manual. Okay. When to merge, when to

1:17:24

split. So you have to look at. You have to see the similarities threshold. You have to see the similarity threshold.

1:17:30

to see the size of the chunks, how many tokens are there in every chunk. And based on that,

1:17:34

you will have to take a call to which chunks you want to merge, what threshold we want to merge.

1:17:40

The appraband we want to merge. That's the next level. Yeah. Okay. So now, uh, coming back to the

1:17:49

idea. So what else we can do? So first thing we can go back and do, uh, first thing we can go back

1:17:55

and do chunking. We can adjust a type of chunker.

1:17:59

The second thing that we can do is we can go and also change the embedding model.

1:18:04

We also have the embedding model. We can also go and modify the embedding model.

1:18:08

So we used, I think, GTE large for our sessions, but we can explicitly go and use something

1:18:15

called embedding model, different embedding models. Because sometimes if you use a more powerful

1:18:20

embedding model, that will give you better retrieval results. So a more powerful embedding model

1:18:26

will actually work well. So sometimes that will impact.

1:18:29

And second base, as I told you, controlling the number of chunks.

1:18:33

So adjusting that value of k, did you take k equal to one?

1:18:36

Should you take k equal to seven, K equal to 10?

1:18:38

How many chunks you want to retreat?

1:18:39

So even that is an important factor.

1:18:41

So adjusting the value of K is also a very, very important factor.

1:18:45

So all these things will impact the, I would say, the quality of your response,

1:18:50

the quality of your generation.

1:18:52

Okay, so these are some very, very interesting aspects of the right.

1:18:55

And what I will do is, in fact, you know, in fact, we have the,

1:18:58

multi-modal session that is coming up in the next class.

1:19:01

I will, in that session, I will also give you another, just a related thing.

1:19:06

I will also give you another very interesting demo of a multimodal rag.

1:19:08

I'll show that to you because that is the session on multimodal.

1:19:11

So I will show you how a multimodal rag is done.

1:19:14

Okay, so we will see that.

1:19:15

Now, let us continue on.

1:19:17

So all this file was to give you the context of rags and some advanced aspects of rags,

1:19:23

what you change, how you change the different parameters, right?

1:19:27

So, let's say that top K.

1:19:28

These are all the variables you will work with top key, how you try different, different values of

1:19:32

just like how we were doing, how we were doing this in the context of, you know, in the context

1:19:39

of machine learning, hyperparameter.

1:19:41

There is no way to know what value will work, but you will have to try out different, different

1:19:45

values and check.

1:19:46

You will have to try out different different values and check which particular number will work.

1:19:51

And what was the new learning in this class?

1:19:54

We saw that if you use semantic chunky, you can use a less, you can use a smaller value of

1:19:58

you can absolutely use a smaller value of K if you do semantic chunking.

1:20:02

So choosing the value of K is a factor.

1:20:04

Choosing the type of chunker is a factor, right?

1:20:07

The chunk parameters are a factor.

1:20:09

If you're using fixed size chunking, what is the chunk overlap, what is the chunk size?

1:20:13

These are a factor.

1:20:14

These are things that you will have to try out.

1:20:16

You will have to manually try out these factors and see what actually works.

1:20:19

So comparing those chunk settings, what kind of chunk is working.

1:20:23

So small chunks, medium chunks, have all other combinations look.

1:20:26

Here I've taken some, we have taken some, we have taken.

1:20:28

some random combinations and evaluated.

1:20:30

In reality, you will use a for each loop.

1:20:32

I'm just going to manually as in a way to do it.

1:20:34

We will use a for each loop.

1:20:35

But this is just to tell you, but there is no way to know what will actually work unless you do it.

1:20:40

You will do your chunking.

1:20:41

You will do the different things.

1:20:43

And then at the end of it on, you will use a judge model to evaluate.

1:20:47

So change the chunker, use a judge model.

1:20:49

Change the embedding model.

1:20:50

Use a judge.

1:20:52

Change the number of chunks are retrieving, use a judge.

1:20:55

So at every point of the pipeline, you are.

1:20:58

you are making some changes, you are changing the application, you're trying to make it better,

1:21:02

and you use a judge to evaluate, okay, did the scores improve?

1:21:06

Did the relevance and groundedness judge improve the scores or the scores improve?

1:21:11

Okay, so this is the way how you will have to usually go about the whole.

1:21:15

Okay. Okay.

1:21:22

Now, guys, as I told you, what I will do here is I will try to connect the dots with whatever we have,

1:21:28

have seen so far and we will try to connect the dots with respect to an agentic rag.

1:21:33

Okay, so we'll try to incorporate this particular rag as an agent.

1:21:38

And part of this is related back to a session we did long back and I think it will be good

1:21:44

to kind of give you a very, very small summary of that session because I know agents is

1:21:50

something we did a long back.

1:21:51

We have seen a few demos on agents after that, but we have, you know, we have seen this sometime.

1:21:57

Just give me one second, guys.

1:21:58

So just allow me one second.

1:22:01

I try to clarify PFC.

1:22:02

Just give me one second.

1:22:28

Thank you.

1:22:58

Yeah, I was trying to just locate the, look at the session where I actually covered this with all of you.

1:23:08

And I think you can see 11 June was the session.

1:23:11

And we did this very interesting case study using the Python data frame agent.

1:23:17

You remember the search, the server API I talked about.

1:23:20

And I'm using that as a reference.

1:23:23

And I will just take five minutes to recap it.

1:23:26

And then we will see a very interesting.

1:23:28

use case of an agentic rag. So all this while we have spent several sessions

1:23:33

understanding what is a rag. Today we took some time in the first half of the session to

1:23:38

talk about some advanced aspects of rags. What kind of things we can do to improve the accuracy

1:23:44

of a rag. And now let us integrate this rag as part of an agent what we have seen. Okay, so this is

1:23:51

the next phase of our conversation. And I will just quickly review this agent concept to you. And

1:23:58

From that, we will, you know, we will be seeing how to do an agentic ride.

1:24:02

Okay.

1:24:02

That is what we will be discussing.

1:24:04

Okay.

1:24:04

So let us take a short break right now.

1:24:06

We can take a session break here.

1:24:08

Then after the break, we will come back and we will build a very interesting chatbot.

1:24:12

So that's the objective of our class.

1:24:14

So by the time I complete the session, I will demo a real chatbot for you.

1:24:18

I will demo a real chatbot which will go and effectively, you know, kind of, you know,

1:24:24

kind of answer questions from your database.

1:24:28

it will answer questions from your rag system. So that is the end thing that we are trying to achieve.

1:24:33

Okay. Yeah. What is that? So Ankit has asked a question. So let's say we have in-house

1:24:39

LLN that we and we got a revised HR policy. And we got a in-house LLLM. You have an in-house

1:24:47

what is that? You have an in-house LLM and you got a revised HR policy. Should we train the model or the

1:24:53

rag way would be the good way. Well, I mean, when you say in-house LLLLLLM,

1:24:58

you're saying that. So I would say rag is usually the better choice, not retraining. I think you're

1:25:03

referring to retraining. So rag is usually the better choice because retraining, if you're talking

1:25:08

about fine-tuning the model, I think that's what you're referring to. You're talking about fine-tuning.

1:25:12

Fine-tuning is very costly. Fine-tuning is very costly, but rags are definitely the better choice.

1:25:17

It's faster, cheaper, easy to update, keeps the ground, all his answers grounded. So fine-tuning

1:25:22

is really the last resort. When we talk about the flow, usually we say fine-tuning is the last resort. That's the

1:25:27

last thing we do. Okay. So that's one way to look at it. Yeah. Maintaining is the last thing we do.

1:25:34

So stick to rights. Okay. Yes. Okay. All right. All right.

1:25:42

Okay. Abishkar, I'll take it up for you. It's a bit of a big query. I'll take it up with you. Okay. I'll reply to you. Okay. I'll reply to you. Okay. Okay. Okay. Let's take a

1:25:49

I'll see you back after the break. Okay. Yes.

1:26:19

Thank you.

1:26:49

Thank you.

1:27:19

Thank you.

1:27:49

Thank you.

1:28:19

Thank you.

1:28:49

Thank you.

1:29:19

Thank you.

1:29:49

Thank you.

1:30:19

Thank you.

1:30:49

Thank you.

1:31:19

Thank you.

1:31:49

Thank you.

1:32:19

Okay.

1:32:49

Thank you.

1:33:19

Okay.

1:33:49

Okay.

1:34:19

Okay.

1:34:49

Okay.

1:35:19

Okay.

1:35:49

Okay.

1:36:19

Okay.

1:36:49

Okay.

1:37:19

Okay.

1:37:49

Okay.

1:38:19

Okay.

1:38:49

Okay.

1:39:19

All.

1:39:23

All, welcome back, welcome back all of all of you, all of you, and we'll

1:39:29

We'll welcome back all of all of you.

1:39:33

All right, welcome back all of you and we'll continue on and we'll continue on. And as I told you, we'll, we'll, we'll continue on with the final part of our discussion on on on on on on this particular of agentic

1:39:49

So let us see that in action.

1:40:19

So now, guys, I hope everybody understands the basic idea of agents from the last session.

1:40:33

I'm not going to spend too much time on this, but just to very quickly review what agents basically are.

1:40:38

It's been a while since we last discussed this 11 June is when we talked about it.

1:40:42

I hope all of you remember it to some extent.

1:40:44

So agents are nothing but LLN plus tools, right?

1:40:47

Agents are very automated entities. They are completely automated entities which are not only able to think, but they are also able to do things.

1:40:57

So all this while we have been interacting only with the LLM, right, large language model, where you ask a question, you give a certain query and the LLM things and gives a response.

1:41:08

Now on top of that, we are giving it ability to do things.

1:41:12

So not only can a language model look at a query, think and answer, but the language model can also.

1:41:17

do things to external tools. So we are giving it access to external tools. And if you

1:41:23

recall the demo that we did in our, the last session, we did that surper search and we, I think

1:41:30

we used Python Ripple plus surper search. We did that agentic demo. This was that specific demo that

1:41:37

we saw in the last session. So it is like a manager worker analogy we also talked about. The LLM is like

1:41:42

the manager and the tools are like the workers. So the manager will get a request. LLM will get a

1:41:47

a request and the LLM will think. The LNM is the person that is responsible for thinking.

1:41:51

How do I solve the problem? In order to solve this problem, what are the different tools I have to use?

1:41:56

Should I give it to tool number one? Should I give it to tool number two? Should I give it to

1:42:00

tool number three? In order to solve this particular problem, which tool I need to give that particular

1:42:04

task to. That is the first of the things that we have to figure out. And after that, the

1:42:11

React framework will basically kick it. We talked about that React framework also in the session.

1:42:17

Okay. So LLM plus tools is the combination which makes an agent. Okay. So first is the language model. That is the main thinking engine. So based on whatever questions are asked, the language model will be the will be responsible for the thought process, what to do, how to do, how to solve the problem. The entire orchestration of the workflow, what are the things involved. All that the large language model will be doing. And the external tools are responsible for getting the things done.

1:42:45

they will say, okay, you know, I want to, you know, in order to solve this problem first, assign this to tool number one, assign this to tool number one, assign this to two number two, right? And it should also know what each tool is capable of. So every tool, what it is capable of, it should, it should also know that, okay? So it should also have a very good understanding and, excuse me, in terms of each tool is capable of doing, okay? That's one way to look at it. Okay. All right, all right. Now, uh, if you see,

1:43:15

This was the demo that we saw. Everybody remembers that. We created a Langchain agent in the last session. This was that beautiful demo that we discussed.

1:43:27

And if you see, take a look at it. This is that Langchain tool that we created, agent that we created. And this is how we are doing the agent right now.

1:43:39

Agent is nothing but LLM. What is the agent? It is the LLM plus the tools plus the prompt. The react.

1:43:45

From all of you recall that. And these are the two tools that we defined in the last session. So we had a search tool. The search tool will be responsible for, uh, uh, so going to the internet server and searching the results and the rebel tool will be responsible for running Python queries. So all of a sudden the language model is not just able to think, but is also able to get things done through these tools. So and we saw this beautiful example where, uh, you know, based on the question, imagine you are asking a question, what is the, the,

1:44:15

you know, what is the closing stock price of nifty? If you're asking a normal question, if you're asking a normal question, it will go and figure out based on the question, what's tool to use. So this is the question that is related to the search. You don't need to do any computation. So based on whatever question is asked, it will figure out which tool it has to use. It has figured out, yes, I have to use the surper search tool. So it uses the tool and does the computations. So that's the way how we are able to see how it is.

1:44:45

the, uh, the React agent is working. This was that entire conversation of React agents we had in the

1:44:51

last session. Okay, all of you remember that, I hope, okay?

1:44:55

Just wanted to review a little bit of this for you. Now, what we are trying to achieve in this

1:45:00

session, uh, what are we trying to achieve in this session? This is 7 July. I've uploaded the

1:45:04

templates for all of you. Today we will see a very similar kind of React agent. We'll see a very similar

1:45:11

kind of thing. And this is going to be a more full-fledged chatbot that I will try to

1:45:15

create for you. And the concept will be exactly how we discussed agents in the last

1:45:21

class. You will have a large language model. You will have external tools. And given the kind of

1:45:28

question, the LLM or the manager will decide which worker or which tool to allocate the task to

1:45:33

and that worker or the tool will get the job done. So all of a sudden our LLMs are capable of

1:45:40

of doing things through those external tools. And today we will discuss two specific.

1:45:45

I will talk about a database tool. I will talk about a rag tool. So without any further,

1:45:50

let me just start the exercise. Let me at least start the implementation. And then I will keep explaining

1:45:56

this as we go along. Okay. And I intend to show the complete end result also to you. So by the time

1:46:03

we complete the conversation, I will show you a real working chatbot how this chatbot is actually

1:46:09

interacting. So you'll see this beautiful like implementation of React framework.

1:46:15

And how rags fit into all this. All this file, you know, we have seen rags in a very isolated way.

1:46:20

So today for the first time, we will see rag as part of a real chatbot and a rag as part of an agent.

1:46:26

We will see how that integrates, the integration part we are actually back to see here. Okay. All right.

1:46:31

So first things first, there are a few library imports and all that are needed to be done. I intend to

1:46:37

show this demo live. So that's why I will just quickly go ahead and let me download these necessary

1:46:45

documents and I will upload them here.

1:47:15

Okay. Great. So there's requirements.t. I'll first take some time to install the requirements.t. This will take a while. All the pip installs are present here. What is the requirements. TXT file? It typically consists of all the installs. Instead of doing pip install, the separate packages, what we do is we keep all the package names in the requirement. TXT file. It is a best practice. So, so that we don't have to separately do pipinstalls. So we keep all the package names in the requirement. TXD file. It is a best practice. So, so that we don't have to separately do pip installs. So we keep all the

1:47:45

files in requirements.t. It is a normal text file, which we created in notepad, and I simply run this

1:47:51

command, pip install, requirements, that's it. This is a simple way to do it. All right, all the packages are

1:47:57

correctly installed now. I will restart the session. Always a good idea. After you install the packages,

1:48:04

you should restart your session. And now I will go and import the necessary packages. Okay, let me import the

1:48:09

necessary libraries. And first things first, I will create our SQL tool, right? So,

1:48:15

So before that, I wanted to clarify that we have a particular database called ECOMDB that is given to us.

1:48:24

So let me show you what is contained in that database. This is the SQL database that is already given.

1:48:29

You guys already did a bit of SQL before in the first module. So running select queries, running all this.

1:48:35

You've got a database, a very basic database that is given to us. So let us take a moment to first explore what is there in the ecom.com.

1:48:43

Let us see. So two.

1:48:44

So two things are given to us. And in fact, three things. First, I uploaded the requirements TXT for the packages.

1:48:50

Second, I have the database given to me. And third, I have the vector database given to me. In case you are

1:48:55

wondering, what is this policy docks. The policy docks. Zip is nothing but the vector db. Okay,

1:49:01

if I open it up, we will see it's a SQL like Proma DB. So inside the policy docs, we have the vector

1:49:07

DB. So the vector DB part is already created for you. This is what will happen in a real world rag

1:49:12

application. So what we were seeing in the demos was like the complete pipeline. You take the

1:49:17

documents, you build the vector db and then, but in a real world scenario, the vector db will

1:49:22

already be ready. Somebody would have already built that vector db for you. It's already there. It's like

1:49:27

a database that's already available. And that's what we have made available for you as a small

1:49:31

demo here. So that vector db is already there. On that, you will do retrieval. That is the pipeline

1:49:37

we will see you. So in this code, we will only build the retrieval pipeline.

1:49:42

Right. So two important things. One is we will try to, you know, first thing, we will try to go and build a particular pipeline that will read some contents from a database. And second, we will try to build a pipeline that will read the contents from a vector D. So both the pipelines we will try to do it. How can we get vector DB file like that? Well, really nothing. It's just a just a vector DB. If you go back to. If you go back to

1:50:12

the Tesla DB, what we created, you can simply zip it. That's it. We have only zipped it, by the way. That's

1:50:18

it. It's only a zip file. Otherwise, the contents inside are what are automatically created.

1:50:23

You can refer back to my Tesla demo, what we did when we were discussing the class on Rags. There

1:50:30

also we created Tesla DB. And if you, if you opened up that database, you can see the structure will be

1:50:35

exactly the same. It will be automatically created this way only. Only thing is we have zipped it. That's it. Only thing is

1:50:41

a dot zip. That's it. Okay. Okay. Now let me quickly explore what is contained in the

1:50:47

ecom. You can see this is my database location. I've given the location as ecom db. And I'm just

1:50:54

checking the database schema just to understand what type of data is present inside ecom db.

1:50:59

Everybody can see this one. This is the kind of information that is present inside ecomdb. All

1:51:04

if you can take a look at it. So we have customers information. Okay, this is typically like the kind of an

1:51:10

order tracking database, right?

1:51:11

something like an e-commerce company like Amazon, how they will, you know, how they will track orders and, you know, kind of things like that.

1:51:18

So it's a typical order tracking kind of database that we have right now, where you have information about orders, you have information about customers, you have information about invoices, and things like that. Okay.

1:51:32

So I repeat again, we have information about orders, you have information about customers, have information about invoices.

1:51:38

You can see this is the customer level details, Michael Smith, email, phone.

1:51:41

all that. We have invoice level details, right? This are the invoice level details.

1:51:45

What was the invoice? What you purchase? What was the amount? All that kind of stuff.

1:51:49

Invoice level details are also there, right? We have the orders level information, who purchased,

1:51:55

what was purchased, when it was purchased, all that we have. We also have information about products.

1:52:00

What is the product? What is the, you know, value of the product, all that. A refund information.

1:52:06

And finally, we have information about shipping. Okay, so the shipping information, we also have

1:52:11

information about shipping basically. Okay, so. So, so this is basically what is contained in the,

1:52:18

uh, uh, contained in the, uh, contained in the, or ecom.com. Dv.

1:52:21

Important to understand the structure of the data. So we have the data and we are also

1:52:25

seeing the structure of our data. I hope everyone's align. So we know all the different tables we have,

1:52:30

and we can also see the, uh, you know, the kind of content inside the, uh, the content inside the

1:52:36

respective tables. Everybody can is able to observe that. Okay. Now, next up, uh, this is

1:52:41

important because down the line, you know, when we query the things, we will be seeing how

1:52:45

it is done. That's what is there in ecom d. And our objective is to go and, uh, build a particular

1:52:53

agent which will, uh, using which we can access information from our database, right? Our

1:53:02

objective is to build a particular agent that will be able to access the information from the particular database. That is

1:53:11

what we are trying to do. Okay. And you can see that we have written a very detailed

1:53:16

kind of a very detailed kind of a system message. So we are saying that, okay, this is the agent

1:53:22

that is going to be responsible for, you know, taking the query in English, almost like you will

1:53:32

ask a question in English. And this agent will be responsible for translating that query into SQL.

1:53:38

Well, in case you're wondering, sir, how are we doing that? We are not going to do that manually. We will use a predefined agent called create SQL agent, which is already available in land chain, right? Just remember. So we are not trying to do this manually. We are already using a land chain, predefined library for doing this. That's it. So just, just to clarify, give it a big picture overview. So we have a ecom DB. And this SQL agent is a predefined agent. I can ask questions in English. And this agent will go to the database.

1:54:08

Write the corresponding SQL query and retrieve the results for me.

1:54:14

Really cool. And we'll see a demo of that. How it happens. Okay. So SQL agent is already built in.

1:54:19

What are we seeing here? We will see the rag agent. We will build that manually. So this is the SQL agent that is already created built in.

1:54:26

Write the question in English and get the answers, like get the query converted to SQL and get the answers. That's the first part.

1:54:36

And this is the built in agent that we have. And let us see.

1:54:38

Let us see how that, we're going to see a small demo of that agent here in action. Let us see that.

1:54:46

Let us see a small demo of that SQL agent how it's working. So I have the system message. And see, very clear criteria are given. Do not make any DML statements to the database.

1:54:57

Very important because, you know, we had this session on injection attacks a while back a few days back. We talked about responsibility. I got ways.

1:55:04

So system message has to be very difficult. You know, users can say, okay, please drop this table.

1:55:08

Please drop this database. Now, if you give a command like that, the corresponding SQL will be generated.

1:55:14

But we, the responsibility and the on us is on us to make sure that we do not generate these kinds of SQL queries.

1:55:21

So only run select queries. Please do not generate any kind of insert, update or delete related queries.

1:55:27

So we are very, very clear that we don't want to generate and repeat any kind of insert, update or delete related queries.

1:55:33

That is the important thing to keep in mind.

1:55:36

And as I told you, all these guardrails will have to be part.

1:55:38

of my all these all these guard drills will have to be part of my uh explicitly uh part of my

1:55:46

system message okay system message system message is where i will specify every single

1:55:52

aspect of the guardrails now um you cannot i think that's the whole idea you know i mean like

1:56:00

i think uh the whole idea is you know uh what if user tries to override but that is exactly

1:56:06

where the injection attacks will kick in

1:56:08

And even if the user tries to override, I would say,

1:56:11

that's exactly where the injection attacks will kick in, right?

1:56:13

So we should be able to identify in cases where the user is trying to override.

1:56:19

But that's the whole idea of your system message.

1:56:21

That's the whole idea of these kind of messages.

1:56:24

So it will not be entertained.

1:56:25

If user query tries to do it, if user query explicitly says that, okay,

1:56:29

please have dropped, then it will give an error.

1:56:31

The response will be that it will say, I cannot do that like that.

1:56:34

It will be detected. If you're adding these kinds of guardrails,

1:56:37

if you're adding some of guardrails that we're

1:56:38

about in the prior session, you know, if you remember input sanitization,

1:56:41

output sanitization, some of those things that we saw. If you're doing all of that, then definitely

1:56:46

it will be honored, okay. Okay, let me test it out. Let me test out this particular tool here,

1:56:51

how it's working. Only thing is when you run the demo, you try to change it to Brock,

1:56:57

that's it. That's the only thing that you device can do at your end. I will create the SQL agent

1:57:02

right now. You can see I'm creating the SQL agent. And very important, I will, I will go and convert this

1:57:08

SQL agent into a tool, a tool, because our, so that our top level agent can use it.

1:57:14

Because we are not done, we are not just trying to create a SQL agent. We are trying to

1:57:18

ultimately create a chat agent, right? So, so SQL agent is a built-in function. We are not doing

1:57:24

anything here. It's a built-in function that we are using, but now we will try to convert this into a tool.

1:57:30

Okay, this is the, this is how we are trying to convert this into a tool. And this is a simple

1:57:35

a pythonic way we are trying to do it. This is like the standard way how you will create tools

1:57:42

in Lanchine. Why do you need a tool? Because remember, an agent is nothing but LLM plus tools.

1:57:49

If you don't create a tool, then your top level agent cannot use it. So we are trying to create a tool

1:57:55

out of it. So we already defined the agent, which is create SQL agent. And this is like a simple

1:58:01

function, which will accept user input. It will generate the prediction.

1:58:05

and we are simply wrapping it as a tool. Let me define that tool. And now we have the

1:58:11

SQL tool that is created. This is the syntax. It's just syntax we are seen. And now if you ask the

1:58:16

question, did Michael Smith place an order? It will automatically go that we are just trying to check if that

1:58:21

tool is working. It will go to that DB. It will retrieve the information and it will generate the answer

1:58:26

to the question. See how I just asked a question in natural language. I just asked a question in

1:58:31

natural language and see how on the basis of that question, see how incredibly it was able

1:58:36

to go back and it was able to figure out, it was able to figure out on the basis of this, it was able

1:58:45

to figure out what is the corresponding SQL query that can be used to answer that question.

1:58:50

So we were able to find out the exact SQL query, which we were able to use to answer that question.

1:58:58

So the SQL query, we were able to get an output. And if you were able to, you were able to get an output.

1:59:01

want to validate it in fact michael smith if you see michael smith has placed two orders

1:59:05

this is that michael smith customer and if you scroll all the way back up uh when i was showing

1:59:10

the schema to you if you remember we do have a customer called michael smith and michael smith

1:59:13

and michael smith did place two orders there were two orders michael smith actually placed

1:59:17

so this is correct whatever information we got is correct and it has used some of its own internal

1:59:22

tools if you're if you're wondering that sir it is using sql db query did i create it no i did not create it

1:59:28

it's a predefined tool i already told you that create SQL agent is something that is a predefined agent

1:59:33

it is using its own tools right so the only new learning here was i simply wrapped it as a tool

1:59:40

going forward also whenever we create tools in lanchain whenever we create tools for agents we will

1:59:46

simply wrap it as a tool we will create a simple python function we will say okay this is the

1:59:51

input it will take this is the output it will give and we will simply wrap it as a tool and then the

1:59:56

top level agent we will use it as a tool that's it this is the way how we will simply use it

2:0:01

now this is the most important part we'll use a rag tool right so all this while we already have a

2:0:06

vector db that is there right now i will simply do the retrieval part of the pipeline here i will load

2:0:13

the embedding model gt e large we all know this i will simply load the vector db this is the part

2:0:18

where i'm loading the vector db i'm simply loading the vector db mind you the vector db is already

2:0:24

created it's already available you'll simply point the

2:0:26

point to the location of your vector db and we are simply loading the vector db that's it okay

2:0:31

that's all we are doing and now here is the rag system message that's it only the retrieval

2:0:36

pipeline we are seeing right now this part is all known to us i'm not going to go over it once again

2:0:40

we all know how to do the rag user message of the rag will contain the context and the question

2:0:44

i'm going to quickly zoom through it and this is my retriever and based on that what i will go back and do i will

2:0:50

now wrap this entire thing as a tool this is the new learning that i wanted to incorporate it right

2:0:55

because remember whenever you are trying to build an agent you know all this file we have done

2:0:59

rags like how we have actually created separate cells and you know but now we are wrapping this entire

2:1:04

thing in one function see the name of the function is def rag

2:1:09

defrag it will accept user input as an input argument it will do all of this this is like a do

2:1:15

dock string a dock string is like a description of a function it is describing what the function will do

2:1:20

what it will accept as input and what it will accept as output and this is the tool

2:1:24

the tool is the worker and this description is very important because this description is the

2:1:30

description of the worker the description of the tool and i already told you the analogy the tool

2:1:35

descriptions are very important because this is how the lm will decide which tool to call given a particular

2:1:41

question how will the language model know which tool to call the description is actually a very very

2:1:45

important factor how the language model will take a call and how the language model can basically

2:1:50

take a decision which you know which specific tool to call that's one way to look at it

2:1:54

That's the idea.

2:1:57

Okay, so you can see that this is the rack tool.

2:2:00

Once again, this is the function.

2:2:01

It is accepting, you know, the user input.

2:2:05

This is accepting this particular, you know, user input you are able to see.

2:2:09

And based on this particular user input, we are able to see that it is doing this particular

2:2:15

processing.

2:2:16

It is retrieving the relevant chunks, retriever dot invoke we are doing.

2:2:20

So based on the particular input, it is retrieving the, it is retrieving the relevant

2:2:24

seven chunks and it is creating the context list and we are feeding this into the prompt

2:2:31

of the rag system message and user input and context and based on that we are getting the

2:2:36

response the response and the response is something we are returning that's a straightforward we are

2:2:40

simply that is what the function is doing it is taking the input it is going to the vector dv

2:2:46

retrieving and giving the response that's what the function is doing and we are simply wrapping it as a

2:2:50

tool that's what i said creating our rag tool that's it because this is now what a top

2:2:54

level agent can use it okay so so same story about the rag only difference is now we are incorporating

2:3:00

this as a tool this is just the syntax okay don't worry about this this is how it is done okay so whenever

2:3:05

you know we are going to this is like an agentic rag now so now we will integrate this rag with a top level

2:3:11

agent we will see how to do that so so far we have created two tools we have created a if you remember

2:3:16

we have created a SQL tool there's an SQL tool that means this guy is responsible for going to my

2:3:22

ecomdb and getting answers to questions and there is also a rag tool which i created and this guy is responsible

2:3:28

for going to my vector database and getting answers to questions now you can ask me sir what is the

2:3:34

difference what is the difference between these two data sets well ecomdb will typically

2:3:38

consists of typical order information customer information okay imagine you go to amazon customer

2:3:43

support now you might have some questions about typical you know order related questions refund related

2:3:48

questions imagine let's say you ordered a product and you're not like you want to

2:3:52

to know when will it arrive things like that you want to get some typical information about your

2:3:56

account history and all those kinds of things so for that the ecom d will be there and we are having the

2:4:03

the uh the vector dv and the vector dv is basically basically responsible for giving us uh you know

2:4:11

answers to typical policy related questions if you let's say if you want to know what is the

2:4:16

you know refund policy for electronics what is the refund policy for this and so typical policy

2:4:20

see the limited questions will be answered with respect to the vector degree.

2:4:24

So that's one way to look at it.

2:4:50

okay so let's move on and i've created three other and let's let's test out the tool right now let's test

2:4:55

out the rag tool i will simply say ragd invoke imagine i asked the question what is the ram on the

2:5:01

mobile phone it is based on the query we are going and looking up in the vector db we are retrieving

2:5:06

the chunks and the rag is giving the answer so this is how we are testing the rag tool you can see

2:5:09

even the source is being given out right so beautiful application of rag if i ask another question

2:5:15

list all the keyboards available for syl i'm only testing the tool right now and see it is again going back to the

2:5:20

the vector dv retrieving the context and giving me the results so the rag tool is working

2:5:24

absolutely fine and we are building a few other tools right now imagine let's say uh we are

2:5:29

going to color after the end of the conversation we're going to collect some feedback from the customer

2:5:33

so we are creating another tool to register feedback similarly we are creating another tool to

2:5:37

defer to a human let's say sometimes we say we say okay please connect me to a human export we're creating

2:5:42

another tool for that and we're creating one final tool for uh orders delivered so we are creating three

2:5:47

other additional tools but these are only miscellamias don't worry too much about these

2:5:52

tools the main focus was on two tools the rag tool and the squel tool that was the main focus

2:5:57

area now what i will do is now that i have the tools created i will go back and create the i will

2:6:03

go back and create these are the five tools that we have so we have the rag tool which will retrieve

2:6:08

relevant information from the vector db and answer questions with respect to general policies

2:6:13

we have created the rag tool the rag tool will get this thing done we have the sq tool the sq tool

2:6:17

the sql tool will be responsible for uh you know uh getting answers to you know related

2:6:23

questions about order status invoices shipping information let's see you want to know when will

2:6:27

by order get shipped something like that you know all for that the skewell tool is there

2:6:32

and there are three other additional tools which i have created and this is now where i will

2:6:36

incorporate my react agent this is where i will build my react agent and i think we have discussed

2:6:40

react agents already in that last plimo 11 june same story i have the list of five tools this time

2:6:47

i have a sq tool i have a rag tool remember i have incorporated rag as a tool that was the

2:6:52

main learning from this session how i can take the rag as a tool the other things are you know

2:6:57

not very related to what we have seen but the rag tool was the biggest takeaway so we have

2:7:02

we have incorporated the rag as a tool that an agent can now use okay so we wrapped it as a function

2:7:08

we wrapped it as the tool so these are a list of five tools that we have and this is the agent and what is

2:7:12

the agent remember guys it is llm plus tools plus prompt the prompt is that that

2:7:17

system message that you have written okay and now we can go and chat with the agent

2:7:23

this is the uh the chat we can instantiate right now and you can see just wanted to show you a small

2:7:28

demo how the uh the agent is going to work right now if you ask the question hey how can i help you

2:7:33

i can say okay i want to know i want to get information about my uh about my orders you want to uh

2:7:44

let's see let's see what the chatbot will say the chatbot will enter and say sure i can

2:7:50

help you with that please could you provide me with your customer ID or email address okay email address

2:7:54

i don't remember so i will use one of the dummy email addresses of michael smith i will go back to my

2:7:59

schema and see michael smith what because this is how the data is stored in the database right in a real

2:8:04

world you will know your email address obviously but here this is the customer so i just want to make

2:8:08

make sure i'm using the right email address for the real customer so let me go back and i will enter uh

2:8:14

email address of michael smith there it is all right very good michael smith's information i've

2:8:20

provided and it will tell me the sequel tool is automatically called look at this how cool is this

2:8:24

remember i've created a sql tool right and based on whatever information i've created the sql tool was

2:8:30

automatically called because i want what did i say i want to get information about my audits so the

2:8:34

agent understood the language model understood what i want and it was able to like give me a beautiful

2:8:41

response it called the corresponding tool and it was able to tell me that hey michael smith

2:8:46

you you you know you ordered these two products you ordered these two products well amazing amazing

2:8:51

thank you so much thank you so much thank you so much nothing else well great amazing so now i have you know

2:9:04

i am glad if you are any other question see very interesting i just said i just say thank you so much

2:9:10

nothing else and the moment i did that the moment i did that it automatically called the register

2:9:16

feedback tool can you see so based on whatever message i'm doing in the chat board the the l lm is

2:9:21

able to figure out what tool to call something very similar to what we saw in that last demo so that is

2:9:26

that llm's intelligence we have we have five tools remember and there is a registered feedback tool so it was

2:9:32

able to understand it was able to understand uh what i wrote it was able to understand my sentiment was

2:9:38

positive and it automatically recorded my feedback as assistant was helpful and rating

2:9:44

is fine it so it is not like like sometimes we have applications where you ask the customer

2:9:49

to rate but this is amazing where somebody writes on chat okay thank you so much it was great

2:9:53

we don't have to ask the customer again to give a rating so this is like a registered feedback

2:9:57

tool which is automatically rating it which is quite cool uh i can ask thank you well i can say please

2:10:03

please transfer me to a human agent transfer me to a human

2:10:07

transfer me to a supervisor if you ask this question well very interesting again based on

2:10:13

whatever uh query you're entering it will figure out the language model will figure out which tool to call

2:10:18

because remember the lm is the manager the manager will figure out okay based on whatever

2:10:22

question the client is asking i you know i have to figure out which worker i have to assign

2:10:27

it to i have a list of five workers and it will automatically call the defer to human tool can you see very

2:10:33

so i asked this question transfer to a supervisor and it automatically called the defer to human

2:10:38

well amazing and it says i have forwarded your concern to a supervisor they will be in depth shortly well thank you

2:10:46

i wanted to get some information about policies now tell me the refund policy and the last part of the conversation

2:11:02

you know you can you can go back and try this out if you call the rag tool so this is

2:11:06

effectively how i wanted to show you the flow okay the overall flow how the thing is basically working

2:11:13

and i did a keyboard interrupt basically that's the only thing right and you can see the feedback

2:11:17

log that is actually recorded here so this is that last feedback that assistant but this is the one

2:11:21

that got recorded now okay assistant okay this is that this is actually again a very uh

2:11:26

like a comprehensive use case how you'll be using rags in the real one right so we have seen rags

2:11:32

but in real world what will happen is you will have multiple rags now here you got a flavor of

2:11:39

you know let's say one agent we built one complete e-commerce agent you know which had

2:11:44

total five tools if you look at this particular thing we had total five tools but in a more real world

2:11:49

scenario you might have multiple rag tools like not only will you connect to one vector database

2:11:55

you might have rag tool one you might have rag tool two rag tool three rack tool four

2:11:59

rack tool five each of these different different rag tools we'll talk to different

2:12:05

different different different vectors which are corresponding to different different

2:12:07

aspects vector db one is talking is concerned about refunds vector db two is concerned about

2:12:13

customers vector db three is concerned about policies vector db four is concerned about finances

2:12:18

because there are different departments in the company right if there are different

2:12:21

departments in the company you cannot aggregate the entire data in one place you cannot do that

2:12:25

because there are security issues and everything so this is a very real world scenario

2:12:29

you will actually have different vector dbs and you will have to create different

2:12:32

rag pipelines on different vector dbs the same way that we saw this simple rag work node where you

2:12:40

connected to a vector db to retrieve information you will do this with other rag tunes also

2:12:44

okay so and and you can see how how beautiful the setup will look like now now you can have the

2:12:50

llm and the llm will now be connected to multiple tools rag tool one

2:12:54

rag tool two rag tool two rag tool three rag tool four rag tool five along with the four

2:12:58

are the tools that we have so these are all the tools or as we gave the analogy in the last

2:13:04

class the hands and legs the limbs of the other than the next time you ask a question to the language

2:13:09

model the language model will not only think what to do not only think and answer it will think and it will

2:13:16

delegate that task to the respective tools which will get the job done and this is exactly what we saw in

2:13:21

this comprehensive demo in a chat one okay i hope this gave you some idea in terms of how you

2:13:26

integrate rags or how you integrate some of these things into a larger agentic

2:13:31

use case okay and and and this is what we call agentic rag there's a term that we will often

2:13:39

here called agentic rag so this is actually what agentic rag is so you are integrating

2:13:43

rag as part of an agent so simple thing that we did was we just did that own whole rag as a

2:13:49

function if this accept user input and generate the response as the output return that is all the

2:13:56

we leave here okay so yeah i hope all of you uh follow the demo any questions any questions uh

2:14:03

like anybody buys okay uh she just are asked a question is it possible to update rag while

2:14:09

we execute like a sequel is it possible to update that as i think you're talking about

2:14:16

not like sequel row updates i would say you update the vector d v sheges i think what you mean

2:14:21

to say is can we update the vector d i think that's the more specific question i think what you

2:14:25

you meant to ask yes you can do that i think we talked about the chroma upcert you remember

2:14:30

absurd absurd absurd upcert operation dot absurd upcert is what absurd

2:14:33

absurd means update and insert whenever new documents are added you can update it in chroma db

2:14:38

when uh you can insert in chroma db whenever any document chunks are updated you can

2:14:42

update in chroma dv with respect to the chunk ideas you can do that absolutely so you know uh

2:14:48

insert update deletes are supported absolutely that is that is going to be something that you will

2:14:53

have to define how frequently you want to do that operation

2:14:55

you want to do it weekly you want to do it fortnightly so that that will happen separately

2:15:00

that is a vector db related operation it will not impact your rag pipeline the rack pipeline

2:15:06

will happen on a you know on a different database but at the same time

2:15:09

parallelly you update a different version of a database is it like your you know she just uh

2:15:14

it's like it's like for example like development staging production so the rag pipeline

2:15:19

what we are using will be connected to a production vector db but the part where you make your

2:15:24

changes will be a staging or a development vector d makes sense yeah yeah yeah

2:15:33

yeah huh huh you oh you meant to say like that uh yeah yeah that's a great idea probably yes

2:15:38

yes maybe you can create an agentic system for that correct maybe that's a great idea maybe you can

2:15:44

ask queries and let the language model figure out how to update it you can create a tool for that yes yes

2:15:48

potentially you can do that yes that would be a good thought yeah okay guys

2:15:54

uh any other questions any other questions

2:15:57

i hope all of you followed it i hope this relates because all

2:16:02

because all i thought i wanted to take up a you know slightly more uh you know a

2:16:06

comprehensive use case because all this while we were doing like just a normal

2:16:10

rag you know we're just creating cells in a notebook and creating a normal

2:16:14

rack so i wanted to show you this this comprehensive demo how it all integrates

2:16:18

together right because we are anyways coming to lang graph in the next week onwards

2:16:22

multi-agent systems which is a very exciting

2:16:24

topic and once we come to Lang graph this demo will be very helpful for you and once again

2:16:29

review this in the next class next week demo i will once again take a similar use case with you

2:16:36

and we will see how you know the same thing can be used in the context of a multi-agent system

2:16:42

we will see that yeah okay um yeah so i would say you know mahmad um yeah so i would say you know mahmad uh

2:16:54

definitely so i think it's about practice i think it's you give it some time i think one of the

2:17:00

things is that definitely uh concepts are the very first thing and you have to understand

2:17:05

that most of you are learning these things for the first time so obviously it's easy to say that

2:17:11

we want to build something but you know but let's be let's be a little easy on ourselves all of us

2:17:18

like let's not push ourselves like beyond the point it's okay i think you don't have to absolutely

2:17:24

implement everything from the get go all the time so give it some time give it a few months okay

2:17:29

so uh understand the concepts understand the ideas right so maybe parallelly keep preparing for

2:17:36

interviews so that you know the ideas well you know the concepts well and it's a process you know it's a

2:17:41

process give it a few months and you will figure out case studies you will figure out applications

2:17:49

and as i say it's a process it won't it won't come in one or two days you have to

2:17:54

you have to build that discipline you know uh read through different different articles keep

2:17:59

reading keep exploring right so concepts and what i'm teaching is one part so how do we use

2:18:05

those learnings how do you go to these blogs like i pinged you a medium dot com link uh you know

2:18:10

you have something called towards data science that's another very nice uh towards data science

2:18:15

is also something very nice you can actually look at these kinds of you know uh websites and this is

2:18:21

very good for learning i would say so it's a process as i say it's not

2:18:24

like a it's not like there is there's no quick solution to this problem that you have to implement

2:18:29

something today but i would say that it's a process where uh be be be be you know like be be light on

2:18:38

yourself don't be too rigid and don't be too uh like hard on yourself so be easy on yourself

2:18:44

okay so it's fine give it give yourself time give yourself a few months four to six months

2:18:49

of time where you uh tell yourself that okay you will

2:18:54

master all the concepts you'll study all the things well and then you will you will you'll

2:18:58

you'll parallelly build enough context of everything that's happening so as i said it's not like

2:19:05

it's not like a it's not like a quick solution right for example if i ask you to build a model to

2:19:09

identify microbes in space like can you can't do that right obviously oh we need to study

2:19:13

but but let's say for example for example you already have studied the article

2:19:18

so tomorrow if somebody asks you a question well you know hey i read this article so i can connect

2:19:23

so a lot of learning is about that learning is about that only it's a process it's a long process

2:19:27

it's a very very long process where uh you know the more you learn the more do you study the more

2:19:34

you learn from different sources right you try to connect the dots and the human brain has a

2:19:39

wonderful way of connecting the dots so it's a process it's a process that will take time okay yes

2:19:44

but as i said most important part of the process is don't be too hard on yourself so be easy on

2:19:51

yourself okay that's one part

2:19:53

i know like one guidance is that okay you know we have to push ourselves every single day

2:19:57

and all that but that's okay there's a limit to that obviously sometimes even if you push yourself

2:20:01

every day it doesn't guarantee success right but it's okay sometimes when you're you know

2:20:06

when you take things slowly when you take things uh uh and sometimes you have to just believe

2:20:12

that you have a lot of time left in life that you all of you are so young right now so it's okay

2:20:17

i mean you don't have to like absolutely do something in the next one year so take it give it give it a

2:20:23

give it a fair runway give it a fair amount of time let's say a six months to a year and that's okay

2:20:28

that's okay i know a lot of people who have you know who who have probably uh like within a span

2:20:33

of one year they they have become very successful but after that they have lost the momentum

2:20:38

because of whatever x number x y z reasons or family and all this and you know life will burden

2:20:43

you at times but i think much of much of the learning is not only dependent on what you learn in the

2:20:50

class but much of your learning will also depend on how you how you uh what you're doing in the rest

2:20:56

of your life which also matters actually you know so learning and rags and gen ai is only a very

2:21:01

small part of our lives so you have to let's just say you have to figure out the other aspects of the

2:21:06

life plan and give yourself a sufficient runway enough number enough amount of time

2:21:13

it's okay you know companies come and go interviews come and go some will get selected some will not

2:21:18

get selected but you have to know it's not the end of the world okay it is never the end of the

2:21:23

world i think there are a lot of opportunities that are there i think it's something where

2:21:28

we need to be all optimistic that's the way i would put it okay yes but as i say i mean just

2:21:34

the summary of the conversation would be that there are no shortcuts i mean you have to give it enough

2:21:39

time you have to work hard you have to keep reading you have to be disciplined that you need to

2:21:44

over and above the sessions we are doing how you can read from other kinds of sources how you can

2:21:48

can try to assimilate more information from different different sources and then like

2:21:53

within six months to one year you will yours and feel confident okay that's the way to be

2:21:58

there all right um okay guys uh well uh well uh i have shared the contents with all of you

2:22:08

under the 7th july folder everybody please do try it out and then one more thing uh

2:22:15

please one if you're doing the demo please change the open

2:22:18

open AI key with the groc API that's the only other change that i would like you to make okay so

2:22:25

some of my demos i have used open AI keys so just change it to groc API key exactly how we did

2:22:30

here exactly how i did here just use that same snippet use the groc API key and the same to same

2:22:36

demo will work exactly how i showed you you can try this out after the plus okay yeah all right guys

2:22:42

thank you everybody that is all from my end uh yeah thank you everybody i will see everybody i will see

2:22:48

you next session next session we will do multimodal very interesting we have something called

2:22:53

multimodal models that are coming up in the next class we will see vision-based models text-based

2:22:58

models so far our conversation has been only limited to language the next session we will talk about speech

2:23:04

we'll talk about audio so we'll talk about multimodal models what all exists there okay so that's how we will

2:23:09

we will face it out okay yeah so thank you everybody this

2:23:18

you know.

2:23:48

Oh.

2:23:53

Oh.

2:24:18

Thank you.