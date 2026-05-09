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

Hi everyone.

12:40

Hi, everyone.

12:43

Welcome to the session.

12:46

Deportse will join in 5 to 10 minutes because we're meeting right now.

13:05

Stay tuned, let others join in starts.

13:35

Thank you.

14:05

Thank you.

14:35

Thank you.

15:05

Thank you.

15:35

Thank you.

16:05

Thank you

16:35

Thank you

17:05

Thank you

17:35

Thank you

18:05

Thank you

18:35

Thank you

18:39

Hi,

18:41

Welcome to all

18:42

Welcome to all

18:43

Welcome to all you

18:45

Welcome Deepak sir.

18:48

So we'll start in a couple of others

19:04

choice.

19:07

So you can start whenever you

19:34

Thank you

20:04

Thank you

20:34

Thank you

21:04

Thank

21:06

Thank you.

21:36

Thank you.

22:06

Thank you.

22:36

Thank you.

23:06

Thank you.

23:36

Hi everyone, very good evening.

23:43

Folks, am I audible to all of you?

23:47

Hi everyone, am I audible?

23:50

Okay, great. Very good evening everyone and welcome to the class.

23:58

Sorry for joining a bit late today.

24:01

I was involved in some discussion in my team.

24:05

Okay, and that started at around 6, 610.

24:10

It was supposed to get completed by 7 or 715, just one hour of discussion, but somehow it got extended.

24:18

Okay?

24:19

Yeah.

24:20

So I hope all of you are doing well.

24:25

And how many of you tried to implement a Rack system?

24:31

How many if you tried to implement Rack system?

24:34

Did you at least go through the code from the notes?

24:45

Did you at least go through the code in the notes?

24:49

Okay, great.

24:54

If you have not implemented it as of now, no worries.

24:58

Maybe take the weekend of time.

25:00

If you have, if you see like today's Wednesday, so,

25:04

this is the last class of this week, then you have Thursday, Friday, Saturday, Sunday.

25:07

So at least take these four days of time, try to implement a vector database, embeddings, use any

25:13

model, Gemini, GPT does not matter.

25:17

At least try to implement a very basic rag pipeline with all the steps as we did in the last

25:23

class.

25:24

Okay?

25:25

Maybe if you're not, if you don't get enough time to implement all the steps, advanced steps also

25:30

chunking, cleaning, etc.

25:32

Do not worry.

25:33

at least try to implement the basic Rack, first of all.

25:36

Okay.

25:37

So, folks, let's get started with today's discussion.

25:40

Is my screen visible to all of you?

25:45

Is my screen visible to all of you?

25:47

Okay, perfect.

25:48

So folks, today's class is going to be, haven't done the multiple file Rack.

25:51

No worries.

25:52

If you have implemented the simpler Rack system Pillar,

25:56

you can try to implement the advanced Rack over the weekend.

25:59

Okay?

26:00

Okay.

26:01

So, folks, in the last around three classes, we have talked about RAG, right?

26:07

And today's class is also based on Rack, right?

26:09

But the idea for today's class is going to be about evaluating and improving the Rack system.

26:17

How can we improve and evaluate that whether our Rag, whether our Rag application is working fine?

26:24

Is it giving us better responses?

26:25

Is it giving us good responses or not?

26:28

Okay.

26:28

How to evaluate?

26:29

talk about the quality of the Rack outcomes, right?

26:34

So how can you compare that the quality of output with Rack without Rack?

26:39

And what are the parameters we can take into consideration while evaluating and improving

26:44

the Rack system?

26:45

Is the I directly to all of you?

26:48

Okay.

26:49

So today's class is going to be more of a conceptual class in which we are going to talk about

26:53

different metrics, different terms, different terminologies associated with evaluation of Rack application.

26:59

How do you evaluate?

27:01

So rather than, instead of writing the code, rather than we are going to focus on the conceptual

27:06

things, right?

27:07

I think we have written a lot of code in the last two, three classes.

27:09

So let's focus on the ideas now.

27:12

Okay, so this in the previous class, you know that we built an e-commerce Rack customer support

27:17

agent which can answer queries related to return or refund or shipping or warranty, etc, etc.

27:24

Now, once you build a Rack application, that is one thing that you have done.

27:29

But in reality, a real Rack system comes from user feedbacks, right?

27:34

So you need to continuously evaluate the Rack system.

27:38

You need to continuously keep on asking the user feedbacks.

27:41

You might have some internal tools as well with which you keep on checking that what kind of quality

27:47

you are giving to the customer, what kind of quality answers you are giving to the customer.

27:51

So that you are continuously evaluating the outputs, you are constantly evaluating your RG

27:55

application, you are trying to improve it over the

27:59

period of time. So the goal of today's class is to understand how to test, how to evaluate,

28:07

and how to improve the Rack system more systematically. Does it make sense to all of you?

28:14

Does it make sense to all of you? Okay. So as I discussed, today's class is going to be more

28:19

of a, you can say that, a theoretical or a conceptual class, right? And because the coding part we have

28:25

already done in the previous class, right? So folks, rag application.

28:29

Do you think that Rag application is relatively very simple and straightforward to evaluate

28:34

that whether your Rag application is good or not good? Is it a binary answer? 01? Is it working? Is it not working?

28:40

Is it a very straightforward answer like 01? It is working or it is not working? Can you do like that?

28:48

Answer is no, right? For example, everyone, if you're solving a mathematical problem, so you are either correct or you are not correct? It is 0 or 1. It is a

28:59

binary solution. Either you will be able to solve the problem or you are not able to solve the problem.

29:03

That's it. But in Rack system, everyone, it's not about 0 or 1. Even if your Rack system is giving you

29:08

an answer to the user, still that does not mean that that is a correct answer. You cannot binary

29:15

or you cannot objectively evaluate that whether your Rack system is working or not working. It's not

29:20

working or not working. It's about the quality. And this quality is always subjective. Make sense,

29:26

everyone. There is no correct measure or there is no mathematical device or mathematical

29:31

representation that you can use to major quality. So that's why everyone, every company, every

29:37

team, every organization, they might have their own parameters on which they will evaluate their

29:43

rag application. All of you agree with this? All of you agree with this? And that's why everyone,

29:50

whenever you use any customer support agent from Sviggy, from Zomato, from Amazon, from Flipkart,

29:55

from any application out there, you might see a good amount of difference between the answers,

30:02

right, and as well as the kind of feedback they're collecting at the end of the, at the end of

30:07

the query. Once they resolve the query, then they ask you the feedback. Now, how they are asking

30:12

about the feedback, it also varies, right? So for example, in some of the applications, you might

30:16

have seen that. Some applications just take the objective feedback. Yes, no. Thumbs up, thumbs

30:21

down. Correct? Did you like the response? Did you not like the response? Simple.

30:25

Correct, everyone? Then at the same time, some other applications gives you some options,

30:30

right? Like, maybe first of all, you can give the rating, one, two, three, four, five. And based on

30:35

the rating, if you give, let's say, five star, they will show you different options. What did you like?

30:41

Did you like the time that, okay, how much time did we take to resolve the query? It was very short

30:46

period of time, right? Did we resolve your query very fast? Or was the query more, let's say, was

30:54

the answer, understand, understood, understandable to all of you, understandable to the customer,

30:58

right? Did the agent solve your query to the point, et cetera, et cetera. Then if you select

31:04

four star, the questions will change. If you select three stars, the questions will again change.

31:09

Have you observed that? Have you observed that? So guys, this is called us continuous evaluation.

31:16

Right. So even if let's say, Sviki, uh, customer support agent, they solved my query. But that does

31:23

not mean that they will be able to solve your query as well. Because they might have

31:27

thousands of policies about vegetarian food, non-vegetarian food, about branded restaurants like

31:32

McDonald's, McDonald's, Domino's, et cetera, et cetera, right? They might have different

31:37

policies for local restaurants. They might have policies for five-star restaurant. They might have

31:42

different policies for, let's say, different brands, right? For different area, for different people,

31:48

right? For different customers. Correct, even? There might be different, different policies.

31:53

is different rules and regulations for different scenarios, different timing,

31:57

right? Whether you are ordering a food on, let's say, 31st of December, there is a peak time, right?

32:02

31st of December, like, millions of people are ordering food from Svigizumato. Right? So that,

32:06

at that point of time, the policies might be different. Right? So that's why these systems

32:12

needs to be evaluated constantly. And it is not very objectively possible. It is not possible

32:17

objectively evaluate this thing. Yes or no? Right. So that's why everyone you must have seen on Svigy,

32:23

when you resolve the query, they ask you the feedback about the rating. First of all,

32:27

they ask you the rating, one to five. And then they ask you different questions. What did

32:31

you like? What did you not like? So this process is called as continuous evaluation. And

32:38

using these evaluation parameters, using these feedbacks, over the period of time, you will keep

32:44

on improving your rag application. Is the agenda for the class clear to all of you?

32:53

Is the agenda for the class cleared all of you?

32:59

Now guys, in RAG applications, can you simply say that okay, can you just, if let's say your

33:04

rag application is not behaving up to the mark? If you're not receiving a lot of five star

33:10

feedback from your customer, a lot of customers are complaining that the customer support agent was

33:15

not very helpful. It was not able to resolve my query or it took a lot of time, it took a long time

33:21

for the agent to understand the query, to resolve the query, and many other things.

33:26

Now, can you just dump all the blame to the large language model?

33:30

Because LLM is bad, right? That's why our application is not working fine.

33:35

Can you just blame, can you just put all the blame on the head of large language model?

33:41

Because LLM is not good. LLM is bad. That's why my RRAG application is also not behaving good.

33:49

Can we just put all the blame to LLLLR.

33:51

M. Actually, not really. Why everyone? Why can't we put all the blame to the LLM? Because

33:58

LLM just generates the answer based on the context that you are providing to them. Correct,

34:04

everyone? LLM just, you can say that, LLM just generates. If you remember everyone in Rack

34:12

application, there are two major components. One is retriever, one is generator. So generator

34:17

component comes at the end. So generator component, before even

34:21

generator component comes into the picture, you have already retrieved the context. You have

34:26

already retrieved the answer, right? Or the relevant chunks or the relevant document. Now you are

34:32

going to use these relevant chunks or relevant documents and you will pass these as a context to

34:38

the LLM and LLM will use this as a context to generate the answer. Now, if you like simple principle

34:45

in AI, garbage in garbage out. Folks, if your retrieval policy,

34:51

itself is not good. If your retriever itself is not behaving, is not retrieving the correct

34:56

documents. If your retriever itself is not very strong, right? If it is loosely following the

35:02

documents, if it is loosely fetching the documents, right, if it is not very strong algorithm

35:06

that you are using, you are not performing very, very particular search, not proper filtration,

35:13

not proper semantic search. Your embeddings are not very good. And because of that,

35:17

your similarity search is not very accurate, not very up to the

35:21

mark. Now, if you're not able to fetch, if you're not able to retrieve quality documents or

35:28

the right chunks or the documents and you are passing them to the LLM, that is not the problem

35:34

of LLM, LLM will only generate the answer based on the context that you are providing. If your context

35:40

itself is not up to the mark, is not relevant, then you cannot expect your answer to be 100% relevant

35:47

for the query. Are you guys getting this point?

35:49

So, if you have to control the quality of your rag application, which is the main component

35:56

that you need to make sure, right? Although everyone, all the components are equally important. But

36:01

if you have to choose one of them, that should be the most priority for all of you, for all of us

36:06

as a developer, to improve on priority. What is that component? What is that component that we

36:14

should improve on priority in a rag application? Which will actually continue.

36:19

control the real quality of your rag application. That is the

36:26

folks? That is what? That is a retriever. So retriever is the main component that we should focus upon. Are you guys getting this point?

36:49

run. Okay, so folks, a good quality rack system, right? What all the properties

36:56

it should have, right? So.

37:19

Yeah. Is my screen visible to all of you? So good qualities or you can say that.

37:34

Goal of a good drag system.

37:49

Right? What all the things should be there? First of all, everyone, answer should be accurate.

38:04

Accuracy is the first and the most important goal of any Rack system. For example, even, I think we are going to talk about a lot of such examples in today's class. But one very basic example is, let's say,

38:19

Let's say, when will I get my refund is one query, right?

38:24

When will I get my product delivered is another query?

38:28

If you see everyone, in both of these queries, they are very, very similar to each other.

38:32

And they are different as well in terms of context.

38:35

One is asking about the refund, other is asking about the shipment, the delivery of the product.

38:40

But the common part among both of these queries are when.

38:44

It means that in both of these queries, user is asking about the timeline, the ETA, estimated

38:48

time of arrival. When will I get my refund versus when will I get my shipment deliver?

38:54

Now, guys, if your RAC system is not performing up to the mark and it gets confused or up

39:00

because of some reason, it is creating both of these queries as a similar kind of queries. And in both

39:07

of these queries, it is using the same document, same chunk where the time is mentioned. It might

39:13

be related to refund or it might be related to shipment. Do you think that the answer will be

39:18

accurate in all the scenarios? If user is asking about the time, it is using the same document

39:24

for all the type of queries. Answer is no. So answer should be accurate in the in the first place.

39:30

Right? Other things will be taken later on. First of all, accuracy is the most important thing.

39:35

Right. Then your answer should be grounded. Tell me everyone, what is the meaning of grounded

39:40

that we saw in one of the classes?

39:48

What is the meaning of grounded? Your response should be grounded in nature.

39:59

This is also a very important property to have and also you should know the meaning of the word grounded response.

40:07

Referred to the knowledge base. It should be reliable. It should be accurate. It should be referring to something. Grounded means that even you should not give your response in air.

40:18

Right? Just like.

40:18

that okay that somewhere I read this right randomly right you should not try to give

40:24

some random references right because you read somewhere or your knowledge base already has something

40:30

no you should always be grounded it means that whatever you are giving the response as a response

40:36

whatever you are giving as a response it should have some base right it should have some document which

40:42

you can refer to for example it's a lot of times you must have seen that as per the policy and then

40:48

everyone in that some link is given or let's say some reference is given as per the

40:52

policy number 170 as per policy stated in the above document as per FAQ 17 this is the answer

41:00

when you give a more like when you give an answer with some reference it is called as a grounded

41:06

response because you're not trying to give the answer randomly you're trying to give the answer

41:11

based on some reliable sources that is the meaning of grounded response does it make sense for all of you

41:18

Does that make sense to all of you? Your answer should be complete.

41:22

Obviously, it should not be incomplete by the way, like 100%.

41:25

It should be, it should be, first of all, it should be safe as well.

41:31

Safe in the terms of everyone, you should never ever disclose some private company's information to the customer.

41:39

A lot of policy documents you cannot reveal to the customer. So you need to make sure that you are not revealing some private document or some private reference to the customer.

41:48

Right? And your response should always be up to date and it should be relevant.

41:54

These are the goals of a good rack system. Is that point cleared all of you?

42:01

These are the goals of a good rack system. Guys, please, please make sure that after the class,

42:07

whenever you get time, please go through the notes for today's class. I have added n number of

42:12

examples in today's notes, right? Because those examples are pretty big, right? Might not be

42:17

possible for us to go through all the examples. I will definitely go through good number of

42:22

examples in today's class. But even more than that, I have added more examples in the notes.

42:27

Please make sure that you go through that. Okay. So for example, even, let's say, yeah,

42:33

so let's say everyone, the policy says that returns are allowed within 30 days. Okay, let's say this is

42:38

what policy says. And the question is asked, and the user is asking about, can I return my product

42:43

after 20 days? Right. Now,

42:47

If you are giving the response as that no, the returns are only allowed within seven days.

42:54

Is this answer even correct? The policy says that you can return the product within 30 days.

43:00

But somehow you have some prior information. You have some cutoff date. Because of that, you have some

43:05

information. And you are just replying that, okay, you can just return the product within seven days.

43:10

But maybe let's say you have older information and the recent policies have been changed.

43:15

Right? So it is a wrong response altogether.

43:17

It means that you are not getting the answer from the latest policy documents.

43:22

Is that one clear to all of you?

43:28

Okay.

43:32

Folks, is that clear to all of you?

43:34

Okay. Then everyone, you might also give some hallucinated answer, right?

43:38

Let's take an example for that. What could be the hallucinated response?

43:45

Let's say, response. Let's say, the retrieved context is.

43:47

you got some context from the, from the knowledge base, from the vector database, that refund takes around 5 to 7 days.

43:55

Okay? Okay. Refund takes 5 to 7 days. This is the context. And your chat bot is answering that.

44:01

Refund takes 5 to 7 days. And customer also gets 100 rupees of coupon code for delay.

44:10

If the refund gets delayed, then you will get some coupon code as a compensation from the company.

44:17

Now, folks tell me, this coupon information is not at all present in the knowledge base, in the vector database.

44:24

But still, you are returning that. It means that your LLM is having some internal information because

44:31

everyone, some company might be giving some coupon. If the refund gets delayed, some company might not be given.

44:37

Assuming that, let's say if LLM has some prior information about some company and it is using that brain,

44:43

that okay, because that company gives the refund, that company gives some compensation of $100,000,

44:47

100 or some coupon code, if the refund gets delayed, this company might also be giving.

44:53

Is that the correct thing?

44:55

If LLM is trying to answer something based on its prior information, even if it is not mentioned in the document,

45:04

even if it is not mentioned in the policy document, this is called as hallucinated response,

45:09

that even if you don't know that particular thing, you're still giving that in the answer.

45:13

This is called as hallucinated response. Is that point clear to all of you?

45:17

Okay?

45:24

How much time is required?

45:29

I did not get it.

45:33

Then everyone, so these are different, different errors that you, like, these are different different things that you might face in terms of responses.

45:45

Now let's talk about everyone.

45:46

about everyone the evaluation framework of a Rack system that what should be the framework

45:51

that you can follow what framework you can follow in order to evaluate your Rack system.

46:11

Evaluation framework of Rack system.

46:16

So how can you evaluate the Rack application?

46:20

Okay.

46:22

So first of all, you should check was, were the documents or let's say, was the right documents or were the right documents or were the right documents retrieved?

46:46

was the right document retrieved now then you need to check that from this

46:59

right document because the document itself will have multiple chunks from the right

47:04

document was the right chunk retrieved

47:16

make sense to all of you? Was the final answer correct? Was the final response correct? And was the response grounded? And was the response grounded?

47:46

Okay, so maybe let's not write it such a big statements. First check, write

47:55

document retrieved, write chunk retrieved, final response was correct or not, and was the response

48:02

grounded. So these are four things everyone that you should definitely check. Definitely you

48:09

can add more parameters as well, right? What's the difference between chunk and document? See, there

48:16

is one document which you divide into multiple chunks. Correct? Make sense? So you

48:24

have a document and that document you have divided into multiple chunks. You can combine both of these

48:29

statements also. If the document is not very big, you might not be dividing that into chunks, quite

48:33

possible. Just give me a second item.

48:46

So in some of the systems, you might have divided the documents into chunks. In some of the systems, you might have divided the documents into chunks. In some of the systems, you might not.

49:16

have because it depends on what is your overall document size. If the documents are not

49:21

big enough, you might not have divided them into smaller chunks. Make sense, Chirac?

49:26

Chirac. Okay? Yes. So for correct even, now, these are the things that you need to check.

49:40

Now, what generally, what is the framework that we follow for follow? For follow,

49:46

this process, right? What is the step by step? Evaluation flow that we have. So first

49:51

of all, everyone, to evaluate this, right? First of all, everyone, like, there are two things that you

49:56

can do for evaluation. One is, you can do some testing in the backend, right? And based on the

50:03

customer feedback also, you can improve the system. Correct or not? So customer feedback,

50:08

like the user feedback, will come later on. But before even you, let's say, before even you launch

50:14

the Rack application to the customer.

50:16

Will you test on your side before even you launch that whether your system is actually working

50:21

or not? So we are talking about the first flow as of now. Later on, we will also talk about the second

50:27

flow. That once you have launched the application, then how will you improve the application

50:31

using customer feedback? So first everyone, what you do is you prepare, you prepare test questions.

50:46

You prepare test questions, right? Then you have some sample policy documents.

50:54

You have some sample policy documents. You have some sample policy documents. Then everyone, what

51:07

you do is, again, these sample policy documents, you, if you have to divide them into chunks, do that.

51:12

You have to create the embeddings, do that. You have to store them into vectors. You have to store them into

51:16

vector database, do that. Once you do all these operations, everyone, then comes, then you do

51:22

what? Then you give the user query. So we are not talking about that particular flow about the

51:30

embeddings, about the chunking process, etc., etc. And then everyone, this user query, you will give

51:36

the response based on the test questions and based, like, these test questions are already there.

51:41

You run the RAC system.

51:46

Because you already have some test questions like user queries, run RAG application.

51:57

And this RAG application, say, you will get the response.

52:08

Now folks, how will you evaluate this response?

52:12

Like, whether this response is correct or not.

52:15

If this response, if this response,

52:16

is correct, how much correct it is.

52:25

So what you can do everyone is, you can assign some score to this response, right?

52:31

Maybe let's say some score between 0 to 5, or let's say 1 to 5.

52:35

On a scale of 1 to 5.

52:37

Now it means that if this is, if this response is up to the mark,

52:41

you can give the score of 5, it is kind of a rating, 1 star, 2 star, 5 star, up to 5,

52:45

star up to 5 star. If this response is following certain criteria, how will you evaluate

52:52

those criteria will come to that. You can give, based on certain criteria, you can give some

52:57

rating to every response. Then you run this loop, let's say maybe 100 times. And 100 times

53:05

you will try to evaluate that how many times we are getting 5 star responses, how many times

53:10

we are getting 4 star, 3 star, 2 star and 1 star. Now everyone you will focus on

53:15

let's say 5 star, once you have got, let's say, maybe 70% 5 star, you are good enough.

53:19

But then you will try to focus on 1 star, 2 star, 3 star.

53:22

That how many times you are getting 1 star? Now you will try to evaluate into each and every run.

53:27

That okay, for this query, this is the response we have got and this is, this has been rated as 1 star

53:33

star response, right? What are the mistakes that we have done, whether we retrieved wrong

53:38

documents or was the answer generation took a lot of time? Or maybe the document itself is not

53:45

are not properly stored. Did the answer hallucinate? Did we, even if we did not have that

53:51

policy in the database, still our LLM or our system tried to answer that and that led to hallucination

53:59

and because of that, the answer was wrong and we got one or two star rating. Are you guys getting

54:04

the idea? You run some sample test cases, some sample test queries for 100 times and then

54:12

you try to evaluate that how many times you got very bad rate.

54:15

one or two star and then basis on that you will try to dig deeper into each and every

54:20

query that if you got one star or two star why did you get it what problem did you face

54:25

everyone clear for example everyone if you if you have a query like can i return my product

54:34

after 20 days which expected policy you should fetch from the system you have already

54:39

written that in the text data set that for this query this is the policy document that we should fetch

54:44

from the database then after the query is completed then you will check that did our system

54:50

actually fetch the correct document or not if yes maybe you will give four four or five star

54:56

if not if your system did not fetch the correct document from the database it means that it is

55:03

is going to get one or two star rating does it make sense to all of you

55:14

Folks, let me show you some sample data sets.

55:18

Okay? Let me see if I can copy paste that.

55:24

This is not the one. Let me take a screenshot.

55:44

This is how a sample data set can be created for a sample data set can be created for

56:14

evaluating the RAG applications.

56:17

Let's see.

56:20

See.

56:21

Folks, have a look at this, have a look at this screenshot and let me know if this kind of sample application, sample data set is making sense to all of you or not.

56:31

Just take one minute of time, try to go through this.

56:34

There are eight pointers. Read every pointer and let me know if this is making sense to all of you or not.

56:44

Making sense everyone?

57:02

First sample evaluation set is that if user is coming up with a query like, can I return my shoes after 15 days?

57:12

What policy document are?

57:13

policy document our system should follow. What it should retrieve? It should retrieve

57:19

a return policy document. Correct, everyone? It should retrieve a return policy document. And what is

57:26

the expected answer? That return is allowed within 30 days if unused and packing is intact,

57:32

original packing. Now if you're returning the, if you're fetching the same policy document,

57:37

that is return policy and you are giving a very very similar answer, your answer will be rated high.

57:43

maybe four or five right then everyone's second is can i return open personal care items

57:48

now you will go to return again return policy document open personal care items are not returnable

57:55

that in that return policy document you might have a section that how the return policy is applied on

58:01

different different items return policy on electronic item return policy on shoes return policy on

58:06

other items and personal care items also right how long does express shipping

58:13

Now you are expected, your system is expected to fetch the shipping document.

58:18

Folks, correct?

58:20

So this is how we create a sample data set for our use case, for evaluating the RAG application.

58:28

Okay? Should we move ahead now?

58:36

Now folks, the point is that how will you evaluate the retrieval quality?

58:42

It is very...

58:43

like straightforward to say for me as well, for you as well, that okay, we will assign one star,

58:48

two star, three star, four star or whatever.

58:50

But how will you do that?

58:52

It is not very straightforward, right?

58:53

It is not very easy for a system to identify that whether this response is four star or five star or one star.

59:00

Correct or not?

59:00

So you can evaluate your system or you can evaluate the retrieval in such a way.

59:06

You can divide them into multiple portions, right?

59:09

First, correct policy document.

59:11

If the policy is correct.

59:13

Then definitely even you cannot give one star or two star to that document, to that query, right?

59:19

To that response.

59:21

Correct?

59:22

Now, it means that at least the first step is clear to your system.

59:27

Your first, your system has clarified, your system has cleared the first step, which is retrieving the current, which is retrieving the correct document.

59:36

Then your system should be able to fetch the relevant information from that chunk or the document.

59:43

as well. Because if your document is quite big, and let's say your document, your

59:48

return policy document contains the return policy of multiple type of products. But you are

59:53

actually checking only the return policy of a particular type of product. So whether your system is able

59:58

to identify from the user query that user is asking for what type of product. If you have to do

1:0:05

some pre-processing before that, for example, it's a user is not specifically saying shoes here or personal

1:0:11

care items.

1:0:13

is just telling that, okay, can I return my recent order? Within, after 15 days.

1:0:19

Now, user has not mentioned that the recent order is about shoes or personal care items. So

1:0:24

don't do think even before you actually try to retrieve the document, you should actually make a database

1:0:30

call, make a call to the database, external tool, and check your order, check the order ID

1:0:36

from the query, fetch the order ID, and check the order status, right? Order details. That

1:0:43

in this particular order, what products did the user actually ordered? Correct or not?

1:0:49

What kind of products were ordered in this order? Then only you will be able to get the final

1:0:55

return policy, the correct return policy. So if you have to do some pre-processing before you actually

1:1:00

try to retrieve the document or retrieve the relevant information from the document, you should be

1:1:05

able to do that. Right. And then everyone, I think this is how you can give your

1:1:12

rating to the final retrieval. Final answer.

1:1:18

Okay, then I think, this is simple example, everyone, that you can use to evaluate or give rating to your

1:1:29

response retrieval, right? How? Let's see. Let me give you an example. Let me copy paste this

1:1:35

screenshot. Maybe on a scale of 012,12, right? If you can, let's see. Let me give you an example. Let me copy paste this screenshot.

1:1:36

maybe on a scale of 012, right? If you have 1 to 5, it might be very difficult for you

1:1:45

to give 5 different things. For simplicity, everyone, I have taken an example of only 3, 3 numbers,

1:1:51

0 1 2. If you have more parameters to evaluate, you can take 5 also 1 to 5 or 0 to 2, whatever works,

1:1:57

right? For simplicity, I have taken 02 to scale. If you use 0 to scale, 02 scale, 0 is score you will only give

1:2:05

if the content itself is irrelevant. If your system did not fetch the correct document

1:2:12

altogether, doesn't make sense to all of you? If the current, if the correct document itself was

1:2:18

not fetched, you will give score 0. Sounds good?

1:2:23

Score 1, it was relevant. It was not 100% irrelevant, but it was a bit of relevance,

1:2:30

but it might be missing some information. Right? Maybe let's say you are saying that, okay,

1:2:35

If there is a query like, okay, I will give you an example. Let's say, if user is asking

1:2:44

about the timelines for COD refund, if there was a order, which was cash on delivery, and user is

1:2:52

asking about the cash on delivery product refund, right? Then everyone you are saying that, okay,

1:2:58

you are giving the response that a refund will be processed within five to seven days. But everyone now,

1:3:04

you have not taken that COD into consideration. Because there might be different policies

1:3:10

for COD, for credit card, for debit card, for net banking, for Amazon pay also. Correct? Because

1:3:17

Amazon pay just take two, three hours for the refund. Credit card may take two to three days. But if you

1:3:23

have paid by a COD, it might take more time also because COD may you have, let's say you have paid

1:3:28

via cash. Right. Now, in order to get the refund, you might have to choose the bank also.

1:3:34

Are you getting this point? So you have just given a very general response. It is relevant,

1:3:41

but it is not having all the proper information. So then you can give score 1. And 2, obviously

1:3:48

everyone, it is correct, it is relevant, it is complete and it is grounded as well. Does it make

1:3:54

sense to all of you? Folks, is that clear to all of you. Now let me show you some examples.

1:4:04

Have a look at it. Take one minute of time, read these three examples and try to understand that if these ratings or these scores are making sense to all of you or not.

1:4:32

Again, everyone, these are also subjective. It's not like that. It is correct. It is not

1:4:37

correct. It is right. It is not right. So obviously, the rating system that you are going to use

1:4:42

initially, you will also keep on improving that over the period of time. So when you have more and

1:4:49

more people who will review that process, they will have their own suggestions. Maybe in some evaluation

1:4:57

process, evaluation flow, you might be missing some parameter. And someone suggests you that,

1:5:02

okay, this is the parameter that we're missing and then you try to add it. It will

1:5:05

definitely, it might make your system even more better for evaluation. So evaluation is also something

1:5:12

that we will keep on review over the period of time. And it will keep on getting improved again

1:5:17

and again. Right, everyone?

1:5:26

Okay, correct. Now we want, we will now move towards.

1:5:32

slightly more objective approach, which you can actually measure, right? Which you can actually

1:5:37

measure, which is retrieval metrics. You can also maintain some metrics on your side.

1:5:47

Right? Metrics are something that everyone that you are measuring, some number that you're

1:5:52

measuring, and basis on that you can take some decisions. First, metrics everyone, that we can maintain

1:5:59

is the precision metric.

1:6:02

What is the meaning of precision?

1:6:07

What is the meaning of precision?

1:6:15

Precision is how precise your output was. How relevant your output was.

1:6:21

Did you fetch correct document or not?

1:6:24

Did you retrieve correct chunk or not?

1:6:27

Correct heaven? That is what precision means, right?

1:6:30

Correct accuracy.

1:6:32

Precision is accuracy, correctness, right?

1:6:36

So precision simply means that, that out of retrieved documents, out of retrieved documents, how many are, how many are, how many are, how many, how many,

1:7:02

are actually relevant. Is this metric clear to all of you? How many of the

1:7:20

actually, how many of the retrieved documents are actually relevant? For example, everyone,

1:7:26

in some query, for some query, for some query, for some query,

1:7:32

you retrieved four documents, right? You retrieved four documents, but how many of them are

1:7:43

actually relevant?

1:7:48

Because see everyone, how do you retrieve these documents?

1:7:52

How the retrieval works based on similarity, right?

1:7:56

So if you're fetching, if you're fetching top four, right, it means that top four, it means that top

1:8:02

four similar documents. So top one will be the maximum similar, top two will be

1:8:08

slightly like second similar, third similar, four similar. But now tell me everyone, if you're asking

1:8:12

about refund, you are trying to find out top four documents for refund. But let's see if

1:8:18

only top two documents are talking about refund, but third and four document does not even contain

1:8:24

the word refund. But still they are coming in a similarity match because you have chosen top four.

1:8:30

Are you getting this point? Because you have

1:8:32

have given top four, it will give you four documents. But last two documents are

1:8:36

completely irrelevant. So now you see that everyone, let's say you fetched four documents, but only

1:8:42

two documents are actually relevant for the answer. So what is the precision, everyone?

1:8:49

What is the accuracy? What is the precision metric? It is two are usable. You are going to use

1:8:56

two out of total four. That is point five. Or in other words, you can say that.

1:9:02

It is 50% precise. What is the precision of this flow? 50%. How can you improve

1:9:09

the precision? How can you improve the precision? Retrieve less documents. That's

1:9:18

everyone, if you have only two relevant documents for refund, but still you are fetching four.

1:9:24

Don't you think the K value is pretty high here? We have discussed in the previous class also, right?

1:9:30

if K value is very high, you might get some irrelevant documents. If the K value is less,

1:9:35

you might end up losing some important documents. So it's very important for a developer,

1:9:40

for an AI engineer to find out the right value of K. So what should be the right value of K?

1:9:46

1, 2, 3, 4, 5, how much? Is there a concrete number that everyone in the world can use? Top 3, top 5,

1:9:53

top 2, top 1? No, it is not possible at all. Because everyone, it completely depends on what

1:9:59

and how your system is built up. If your system has a lot of documents and it has a lot of

1:10:07

documents for every, every category also, then maybe top four, top five might work. But if

1:10:15

your system has only few documents and your system has only one document per category, then more

1:10:24

than top one does not even make sense, right? I'm getting the point. Because even if you go to top

1:10:29

three, you might get two irrelevant documents and only one relevant document. So everyone

1:10:34

now, this top K value keeps on changing, keeps on varying based on the, based on, like, it keeps

1:10:40

on changing system to system. Sounds good to all of you. Right? So precision metric is very,

1:10:48

very important that we can check and it is relatively easier to check. Right. So guys, if you say,

1:10:54

if I give you one metric, you tell me if this is making sense to all of you.

1:10:59

If the precision is high, high, high precision means less noise. Is this making sense to all of you. High precision means less noise.

1:11:28

traffic light. A lot of people are honking. There's a lot of noise. But do you have anything

1:11:36

useful, any sound which is useful to you there? Everything is noise. Nothing is useful. It means that

1:11:43

everyone, if you have high precision, it means that more and more documents are relevant. Obviously, you will have

1:11:48

less noise because all the documents are relevant. More documents are relevant. Noise means irrelevant

1:11:55

documents very good Vishu Nat. Noise means something which is irrelevant.

1:12:25

Okay folks, so let's take a break at the moment and we will talk about the remaining

1:12:32

metrics after the break. So it's 901. Let's take a break of around 10 to 12 minutes. Let's meet

1:12:37

around 913, 914. And after the break, we will talk about the remaining metrics. Today's class is

1:12:42

very, you can say that just like this only. We will just talk about few things and because implementation

1:12:48

is mostly done. After the break, after the class, at the end of the class, around 10 p.m. If you have any

1:12:53

doubts related to implementation. That you can ask. Okay. So let's take a break

1:13:00

everyone and after the break we will talk about the remaining things. See you after the break now.

1:13:23

Thank you.

1:13:53

Thank you.

1:14:23

Thank you.

1:14:53

Thank you.

1:15:23

Thank you.

1:15:53

Thank you.

1:16:23

Thank you.

1:16:53

Thank you

1:17:23

Thank you

1:17:53

Thank you

1:18:23

Thank you

1:18:53

Thank you

1:19:23

Thank you

1:19:53

Thank you

1:20:23

Thank you

1:20:53

Thank you

1:26:23

Thank you

1:26:53

Hi, everyone. So let's

1:26:55

so let's continue our discussion.

1:26:57

the first metric that we discussed was the Precision metric that we discussed was the Precision metric, right?

1:27:01

Now another metric that comes into picture is recall metric.

1:27:03

Now another metric that comes into picture is recall metric.

1:27:23

Recall means what? No, it is not precision exactly. See, precision means what?

1:27:34

That how many we retrieved versus how many are relevant. For example, if you retrieved, out of four, out of four, two are relevant. Recall means

1:27:49

means that if there are ten lexicon

1:27:53

For example, if there are 10 relevant documents present in the system, how many of you,

1:28:00

how many of them you were able to retrieve?

1:28:04

It is slightly confusing.

1:28:06

Let me write it down.

1:28:08

Recall means out of all relevant documents, out of all the relevant documents, out of all the relevant documents,

1:28:18

out of all the relevant documents, how many did we retrieve?

1:28:36

Okay.

1:28:45

If you see everyone, for example, let's say,

1:28:47

example. Let's say there are four relevant documents are there are

1:29:17

let's say four relevant documents are there in the knowledge base.

1:29:29

Okay, so for example, there are four documents available with respect to refund, which are related to refund.

1:29:36

But how many we retrieved?

1:29:40

The number of retrieved are let's say two.

1:29:46

Right? So what is the policy everyone now? What is the recall number?

1:29:51

That we retrieved two documents, but we retrieved two relevant documents, but total there are four

1:30:00

relevant documents. So it is 0.5 again. Or let's say we retrieved three just to change the number

1:30:07

so that you don't get confused. We retrieved three documents, three relevant documents, but total

1:30:13

there are four relevant documents. So it is three by four.

1:30:16

which is 75 percent 0.75. Is that point clear to all of you? The value, the recall

1:30:27

metric, that how many we retrieved versus how many were actually available. Now everyone, let me

1:30:34

draw a very small comparison between precision and recall. So let's talk about precision,

1:30:46

versus recall. So what is precision versus recall? So what precision versus recall?

1:30:54

So what precision says? Now folks tell me, if you are following the precision metric,

1:31:03

what precision says? That out of retrieved chunks, if you retrieved, let's say,

1:31:09

10 documents, and out of 10 documents, four are, only four are relevant. It means that your

1:31:16

the precision is 40%. Correct? That you retrieved 10 documents, six of them are not useful.

1:31:22

Only four of them are useful. Making sense? So if you can improve the precision value,

1:31:30

what you're trying to improve? If you can improve from 50% to 100%, it means that what you're

1:31:38

trying to improve everyone? You are trying to improve irrelevant documents. Can we say that? You are trying

1:31:44

to improve or avoid irrelevant documents, correct? So precision means what? Avoid

1:31:51

irrelevant documents, correct or not?

1:32:05

Folks have a look at it and tell me if this is making sense to all of you or not? Precision simply means

1:32:11

that you are trying to avoid. If precision increases,

1:32:14

this irrelevant documents decreases. But everyone now, if you see recall,

1:32:24

although recall is also trying to avoid irrelevancy, but in a slightly different way. How, if you

1:32:29

see, let's say total there are four relevant documents present, but you are not able to retrieve

1:32:37

or you were not retrieving all of them. You are only retrieving two. It means that you are not

1:32:43

not retrieving two relevant documents, correct? Correct or not? If you increase recall number,

1:32:52

it means that you are trying to avoid missing the relevant documents. Can we say that? Recall means you

1:33:01

are trying to avoid that you don't miss any relevant document. Right? So avoid missing any relevant document.

1:33:13

Avoid missing.

1:33:43

Don't you think they are trying to achieve the same thing? That if you retrieved 100

1:33:48

documents, how many of them are relevant? First says that you are retrieving 100, maximum

1:33:55

should be relevant. Recall says that you are trying to retrieve all the relevant documents without

1:34:00

any miss. Have a look at it and tell me if this is making sense to all of you or not. All

1:34:06

of them, the goal is very, very, very similar that you want to try, you want to increase the relevancy.

1:34:13

Make sense everyone?

1:34:17

Then everyone, the other metric that comes into picture is top K recall.

1:34:27

Now folks, let's say if you are giving the value of K as 3, okay, as 3, the value of K as 3,

1:34:38

now is is it 100% possible that out of top 3,

1:34:43

documents, you might not be getting the, you might not be getting all the context. You

1:34:49

might not be getting all the relevant documents about the query, right? Because let's say you

1:34:52

have total five relevant documents, but you are only retrieving top three. What about the remaining

1:34:58

top two? What about the remaining two documents? They also have some context. So definitely you

1:35:04

can create an answer. You can generate an answer using top three. But do you think that that answer

1:35:08

will be complete or 100% true? That answer will be more grounded. That answer will be more grounded. That answer

1:35:13

will be 100% relevant? Maybe not. Because you are just generating the answer based on top 3.

1:35:18

But there is some context which is there in other two documents as well. So top K recall checks.

1:35:43

Correct answer appears.

1:35:50

within the top K retrieved documents or not documents or not.

1:36:20

Folks, yes or no?

1:36:27

For example, everyone, let's say if the query is, let's say if the query is, let's say, let me take a screenshot now.

1:36:38

This is coming from notes only. See if this is this example of top K recall is making sense or note.

1:36:53

Now, try to read the definition and then see.

1:37:03

The definition and then see the example. Tell me if it is making sense. Tell me if it is making sense

1:37:08

or not. First, read the definition, then see the example.

1:37:38

Tell me everyone, is the example clear and the definition clear now.

1:37:58

Very straightforward.

1:38:01

But as per semantic search, second result should come first.

1:38:08

as per semantic search. See, semantic search also depends on multiple factors.

1:38:14

Semantic search works on probability. Definitely you are saying that this particular result

1:38:21

should be the first answer. Absolutely correct. But is it a guarantee that it will it always

1:38:27

be the first answer? As of now, I have just returned a small, small things, right? Let's say

1:38:33

this is just the query. And the document can be very big. So when you perform, you perform

1:38:38

on similarity, the similarity gets performed on 100, 200 or 500 different factors.

1:38:44

Right. So you never know which will come at number one, which will come at number two.

1:38:49

Right. So you're only comparing COD, COD. But what if there are other hundred of factors which

1:38:54

are taking this document at the second number, this document at the first number? Because if you

1:38:59

remember, the semantic will have 1536 dimensions, embeddings, right? So every document, every query,

1:39:08

Chung will get converted into 100, 536 number of dimensions. Now, out of these many dimensions,

1:39:15

do you really, would you really get to know that what will take more priority, what will take less

1:39:20

priority? No, right? Like, even if let's say this document is slightly more similar than the query,

1:39:28

not because of COD, but other things also. Right? Why recall one said failed? Because it is a general

1:39:38

policy right? You are talking about COD. Because COD might be having completely different

1:39:42

refund policy. Right? COD you will have to fill a form, let's say, you will have to give your

1:39:47

bank details, then you will get the refund. Right. But if you have online payments, then the payment

1:39:53

will get transferred to your source account. It is very straightforward. But COD might have a completely

1:39:58

different route altogether. Right? Order of documents depends on the content in both of these

1:40:05

documents, absolutely correct. Right? And content.

1:40:08

means embeddings and embeddings will have thousands of parameters, thousands of dimensions.

1:40:14

It can change. Right. Okay. So then everyone, let's talk about the next thing, which is evaluate response

1:40:21

accuracy. Again, everyone, the response accuracy, I think we have already talked about it, that how will

1:40:31

you rate the response, how will you rate the response accuracy? Was it correct? Was it not? Was it

1:40:38

not correct? Was it like maybe 70% correct? So based on that, you can give some rating

1:40:43

on a scale of 1 to 5 or 0 to 2 or 0 to 3, whatever. That is something that we have already figured

1:40:49

out. For example, everyone, I have taken an example of 0 to 3 scoring. Okay? So, the topic is, let's say, evaluate.

1:41:08

response accuracy. So I'm giving you an example on a scale of 0 to 3.

1:41:24

Maybe this is a very simple, maybe a table, maybe a table that you can follow to score.

1:41:32

right so it can be 0 to 5 it can be 0 to 2 this is just an example okay zero means

1:41:42

completely wrong answer three means it is complete correct and fully grounded answer right

1:41:50

and now everyone let's take an example of this

1:42:02

as an example for this one this thing. So look at this table and then look at this

1:42:13

example table and then try to find out that how can we give the score.

1:42:32

Take one minute of time, take two minutes of time, try to go through all these examples

1:42:41

and then think, is the scoring criteria making sense to all of your node?

1:43:02

See, user is asking about that does the warranty covers the liquid damage?

1:43:09

Okay?

1:43:10

Policy says liquid damage is not covered.

1:43:12

Okay?

1:43:13

And if you give an answer that yes, warranty covers liquid damage, it is completely wrong.

1:43:18

Right?

1:43:18

Policy says that it is not supported.

1:43:20

You are saying it is supported.

1:43:22

Hallucination.

1:43:24

Nowhere this answer is coming from.

1:43:26

No one knows.

1:43:27

So it is score zero.

1:43:29

Second answer says that warranty does not

1:43:32

cover liquid damage up to the mark correct score three. Then you say that in the third

1:43:37

answer, no, warranty does not cover liquid damage, but you may get a free replacement. If you say

1:43:43

that it is partially correct, right? It is partially correct. It is saying that it does not cover

1:43:48

liquid damage, but from where it is coming from, you may get a free replacement. We don't

1:43:54

know. So it might be coming from different other document that might have some reference

1:43:59

of liquid damage. It might have other references.

1:44:02

of replacement, etc, etc. That's why we will have to, we need to investigate

1:44:07

that where this is coming from. If it is coming from some relevant source, you can give a

1:44:12

score of two. Otherwise, definitely it might be a score of zero or maybe one.

1:44:17

Why it is not score of zero? Because it has some context, some correctness. That is, it does

1:44:22

not cover liquid damage. I hope this makes sense to all of you guys. Again, these things

1:44:28

are very, very subjective. Make sense? These things are very subjective. It's not.

1:44:32

100% true or false. Okay, it is not 0 or 1. These things also keeps on improving over the

1:44:38

period of time. Okay? Then everyone, how will you detect hallucinations in the responses?

1:44:46

This is something interesting. Hallucinations we all know. Detect, how do we detect?

1:45:02

Detect hallucinations.

1:45:05

Hallucination in responses.

1:45:32

everyone, if your LLM, again, there is no strict criteria in which you can find out

1:45:36

that whether this answer is hallucinated or coming from some document. But there is some

1:45:41

approximate framework that you can follow in order to just guess whether it is a hallucination

1:45:47

or not. If your answer, if your system is giving you some claim, let's say maybe you will

1:45:56

get a coupon code or you will get a hundred rupees coupon code from somewhere on a refund delay.

1:46:02

That might be hallucination.

1:46:04

So whenever your LLM is trying to claim something, whenever your LLM seems to be overconfident,

1:46:12

whenever your LLM is trying to claim some timeline, which is wrong, then it is hallucination.

1:46:19

So how can you identify that?

1:46:21

You can try to highlight every claim that your LLM is trying to make, that your answer is trying to make, that your system is trying to make, that your system is trying to make.

1:46:30

Some claim, maybe related to timeline, related to payment, related to, let's say,

1:46:37

maybe coupon code, etc. And then you check that whether this claim is present in the retrieved

1:46:45

document or not, or this claim is supported by some data or not. If yes, okay, if not,

1:46:51

it is hallucination. Does it make sense to all of you? Okay?

1:47:00

Folks, clear? Again, there is no strict policy that I can give you, unfortunately,

1:47:07

that how can you detect hallucination? Okay? This is just hidden trial and over the period of time,

1:47:12

your system will improve in terms of hallucination. The system will do less and less

1:47:18

hallucination over the period of time. Next topic, everyone, is how can you improve grounding in your

1:47:25

response?

1:47:30

improve grounding in response.

1:47:47

So, what is grounding, everyone?

1:47:49

Grounding, we all know that.

1:47:51

Grounding means that the answer,

1:48:00

should be based only on the retrieved chunks or documents. It should not be coming from random places, right?

1:48:25

It should not be a random answer. Rather, it should be coming from some retrieved document.

1:48:30

Right? Or in other words, we can say that grounded answer means no random assumptions in the answer.

1:49:00

So how can you improve grounding in your response? So whenever you are trying to claim

1:49:07

something, for example, let's say refund will take five to seven days. Your payment will be credited

1:49:13

or let's say you will get your order within two days. So always try to quote something. Always

1:49:20

try to add some resources. Always try to cite something. For example, let's say as per are now,

1:49:25

a lot of times everyone, you might not be allowed or you might not be having to have a

1:49:30

the right of disclosing the policies 100%. So that is a different policy. That is a different

1:49:35

way altogether. But if you're allowed for example, then you can always say that, okay, as per the

1:49:40

refund policy, section 10, you will get the refund within five to seven working days. It means

1:49:47

that everyone, in future, if the, if the user comes back with some claim, you will be able to identify

1:49:53

that, okay, you made this, your system made this claim that refund will be processed or refund will not be processed, whatever.

1:50:00

on what basis? What was the ground of that response? What was the ground of that answer?

1:50:05

So that you will be able to go back and check that this is the policy, this is the section, this is

1:50:10

the page number that was referred while giving this answer. Are you guys getting this point?

1:50:15

So whenever you're trying to answer, try to give some response. I try to give some code

1:50:22

that this is coming from there. Is that point clear to all of you?

1:50:30

Okay, then everyone, you can also tune in order to improve the responses.

1:50:39

You can also tune top K number, top K parameter. What is the meaning of tuning, everyone?

1:50:56

What is the meaning of tuning? That how many? Like, tuning means that just like you adjust

1:51:03

the sound, right? The music, you just adjust it, right? When everything is perfect, right? Let's

1:51:09

say there are 10 controls. You are just trying to tune the volume in such a way that all these 10

1:51:14

10 things are working smoothly together. Similarly, everyone, top K value, there is no perfect answer

1:51:20

for that, top 3, top 5, top 10. You will have to keep on adjusting over the period of time.

1:51:26

and then you will realize that, okay, this particular value is working best for your use case.

1:51:31

Right? So maybe initially you will try with top, a low value. Eventually, you will keep on increasing.

1:51:36

And after a certain point of time, you start realizing that, okay, now the value is bit higher.

1:51:40

Let's say you start with three and you say that, okay, three is a bit lower. You go to four.

1:51:45

Four is giving you slightly better response. Because from three to four, you got better responses,

1:51:51

you say that let's try to improve two. Let's try to increase to five. Let's say five is also giving you the better response.

1:51:56

But then you go to six. Now, six has started giving you more irrelevant documents in the answer.

1:52:02

And that's why everyone you realize that, okay, maybe the five is the value that is going to work

1:52:06

better for you. So then why? That's why you tune. You have tuned to the top K value to be top

1:52:11

five value. Does it make sense for all of you? This is how you keep on adjusting these values

1:52:16

step by step. If the top K value is too low, system may miss some important context.

1:52:23

If the top K value is too high, system may retrieve some irrelevant document.

1:52:26

So generally everyone, three to four is the value that works best for most of the use cases.

1:52:32

Make sense?

1:52:34

Okay? Then everyone, other thing is that you can apply filtering.

1:52:41

Metadata filtering.

1:52:56

meta data filtering for better response.

1:53:10

For example, now for example, everyone tell me, is this idea clear to all of you?

1:53:15

That if you can perform a metadata filtering while retrieval, will it give you a better precision or

1:53:22

not? For example, everyone, let's say you have thousands of documents. And now, let's say,

1:53:26

the user query comes in for refund. Now, without any filter, what you do, you perform

1:53:32

similarity search and you got top five documents. Quite possible that the fifth document or the fourth

1:53:38

document, they might not be 100% related to refund. They might be related to something else, right? Top one,

1:53:44

top two document, they are good. But now everyone, let's say, if the user is specifically asking about

1:53:49

refund, do you even need to consider other documents in the retrieval? Do you even need to consider

1:53:56

other type of documents, other category of documents?

1:53:59

Maybe not.

1:54:00

So what you can do at the time of retrieval, before even you try to perform similarity search, you can

1:54:05

give the query in such a way, you can put a filter that I want to perform similarity search only

1:54:11

on refund documents.

1:54:14

So that other all the documents, if there are other documents like delivery, shipment, order

1:54:19

cancellation, etc., etc., all these documents you will not even consider.

1:54:23

you will only perform similarity search on filtered documents, on refund-related documents.

1:54:32

Now, don't you think even if you can perform such filtering, definitely everyone, the documents that

1:54:37

you are going to retrieve after filtering, they will be even more precise for better response

1:54:44

or precision, right? Because now you will be able to get even more precision.

1:54:51

Because you have even applied.

1:54:53

filtering before even you perform similarity search.

1:54:56

In the implementation class, I must have talked about this, right?

1:54:59

Last to last class.

1:55:01

When we implemented RAG earlier, in the last to last class, we must have talked about this.

1:55:07

That yes, you can perform filtering based on metadata for better precision.

1:55:15

Because now even if some document which is coming from shipment, which is matching with your query,

1:55:21

It will not even come into the retrieved documents because you have applied the filter

1:55:26

before that, right?

1:55:28

So definitely all the documents that you are going to get now, they will be related to refund and

1:55:32

that's why it will offer you, it will give you better precision quality.

1:55:36

Is that point clear to all of you?

1:55:37

Yes or no?

1:55:44

Folks, clear?

1:55:45

Okay.

1:55:46

Then just last topic, you can also improve.

1:55:51

prompt design for policy-based answers.

1:56:06

So guys, when we implemented RAG in last class and in the previous couple of classes as well,

1:56:12

did I show you the RAG prompt template?

1:56:19

Right?

1:56:19

Don't make up the answer.

1:56:21

give the answer based on the policy documents.

1:56:24

If the answer is not present in the policy documents, don't give the answer.

1:56:28

Just return, I don't know.

1:56:30

Okay, it is okay.

1:56:32

Always, it is better to give answer no rather than giving wrong answer.

1:56:38

Correct or not?

1:56:39

You can deny, right?

1:56:41

It's not always possible to give the answer always.

1:56:45

Say no.

1:56:46

That okay, I don't know the answer.

1:56:47

This is not present in the system.

1:56:49

Give your feedback.

1:56:50

We have noted down.

1:56:51

And we will, probably now you will give the feedback to the team and team will try to add that in the document.

1:56:59

Right.

1:57:00

So you can give some prompt template like this, right?

1:57:05

So let me give you, let me give you an example of both weak template as well as strong template.

1:57:17

Weak prompt and strong prompt.

1:57:21

See this, everyone.

1:57:29

If you just give this prompt to the LLM that answer this customer question, that's it.

1:57:35

Versus if you give this prompt, right?

1:57:38

You are a customer support agent for an e-commerce company.

1:57:41

Use only the policy context provided below.

1:57:44

You will provide the context.

1:57:46

And these are the rules that you're defining.

1:57:47

Don't make up policy details.

1:57:49

If the answer is not present as a context, say you,

1:57:51

do not have enough information, mention timelines, eligibility, et cetera, et cetera,

1:57:56

give proper answer.

1:57:57

Don't you think everyone, this prompt is definitely giving, is going to give you much better response

1:58:02

than the normal template, normal prompt.

1:58:06

Does it make sense, everyone?

1:58:15

Folks, is that point clear to all of you?

1:58:19

Okay, and then worse, one last thing, everyone.

1:58:21

that this evaluation process and improving process is a continuous loop.

1:58:30

You are never going to say that, okay, my Rack application is working 100% fine.

1:58:35

There is always a scope of improvement.

1:58:37

There is always something that might be missing.

1:58:39

New policies will get added.

1:58:41

Previous policies will be deleted.

1:58:43

New policies will be added.

1:58:44

New products will be added.

1:58:45

New type of users will be added.

1:58:48

Some policy documents might be unavailable, etc.

1:58:51

sector. You never know in the production systems what can change at what point of time.

1:58:56

So always, it is a continuous evaluation and improvement process. So you will have to

1:59:15

continuously do that, right? Internally, as well as externally. Externally, what? Take the user

1:59:20

feedback. So after.

1:59:21

every query, consider user feedback. Keep on maintaining that at some place and maybe

1:59:26

run the evaluation process every week or every day or every month. Whatever the cycle you

1:59:32

are choosing, whatever frequency you are choosing. For example, Amazon kind of system might be

1:59:36

running the feedback policy every two three days because they are getting a lot of feedback

1:59:40

every day. Because the user base is very big. Right? Sviki might be getting a lot of feedbacks

1:59:45

every day. So if you're getting enough number of feedbacks to be to act upon every day,

1:59:50

try to perform, try to run the process every two, three days or every week so that you can

1:59:55

keep on making your rag application, your customer support agent, your travel agent,

1:59:59

better every day. So it is a continuous process. It is not, it is never ending thing.

2:0:05

I hope this makes sense to all of you. The class is making sense, although the class was a bit

2:0:10

theoretical. I hope this makes sense to all of you. And we have talked about almost everything with

2:0:16

respect to rag everyone. Even if you go through any external

2:0:20

you say that external resource you will find out that we have covered each and everything

2:0:24

in detail in these i think three or four classes with respect to rack okay so we are done with the

2:0:30

class thank you so much i'm uploading the notes a bit shorter class today i hope you get this time

2:0:40

you enjoy this time so let me just upload the notes and then i will launch the feedback pool

2:0:50

has launched the feedback pool folks please take the feedback pool then we can then

2:0:56

feel free to drop off there is no quiz today because the class was a bit theoretical that's why

2:1:01

we will start having the quiz again from the next class

2:1:20

So guys, these are the notes for today's class. You can refer these notes, but most

2:1:31

probably like I would recommend you, I would suggest you to go through the notes, the printed or the type

2:1:38

notes that you must have got on your dashboard. Go through those notes, those are more detailed and more

2:1:43

examples with more examples. Okay. Thank you so much everyone. Have a good day. Take care. Bye

2:1:48

If you have taken the feedback poll, feel free to drop off.

2:1:50

If not, please take the feedback poll and then feel free to drop off. We are done with the class.

2:1:57

Thank you, thank you everyone. Have a good day. Take care and bye.

2:2:01

There are five, six people who have not taken the feedback poll. Please take it.

2:2:20

Folks, take the feedback poll. Just two three people are remaining. You are done.

2:2:50

Thank you so much everyone. Have a good day. Take care. Good night. Thank you, Samia. Take care and bye.

2:2:56

Thank you, sir. Thank you all. We'll have a tutorial tomorrow. So if you haven't done,