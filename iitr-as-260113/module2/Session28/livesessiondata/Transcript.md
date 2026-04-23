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

Hi, everyone.

9:22

Hi, everyone, very good evening.

9:26

Hi, everyone, very good evening.

9:45

So am I audible to all of you?

9:48

Okay, so guys, we'll start in two, three minutes.

9:53

Let's wait for more people to join and then we'll get started.

10:18

Thank you.

10:48

Thank you.

11:18

Thank you.

11:48

Thank you.

12:18

Thank you

12:48

Hi,

12:52

Thank you.

13:18

Okay, great. Good evening everyone and welcome to the class.

13:28

I hope all of you have revised the previous

13:31

the previous content that we discussed on vector databases as well as embeddings,

13:38

vector embeddings, similarity search and like the related content, right?

13:43

I hope all of you have done some revision of that.

13:47

Is that correct?

13:48

All of you understood it very, very well.

13:55

Okay?

13:56

Very good.

13:57

So guys, now, today we are going to start with a new topic, which is RAG.

14:00

How many of you have at least heard about RAG?

14:03

You might not be knowing what RAG is, but you might have seen, there are very high chances that you might

14:10

have seen the term RAG.

14:12

It is so popular, right?

14:15

Rag term is very, very popular with the evolvement of AIE

14:18

with the advancement in the AI. And now, in the last, I would say a couple of years,

14:25

AI has become one of the most powerful tool to build things. And in that, everyone, RAG is,

14:32

I would say, one of the most common thing. One is agentic AI, agents, and RAG, vector databases.

14:39

These are four or five terms which everyone talks about. And there are a lot of companies,

14:44

there are a lot of startups which have been built around these problems.

14:48

statements which are solving the problem statements of memory, databases, RAG, and so on, right?

14:54

So RAG is a very, very powerful tool that almost all the applications are implementing nowadays,

15:01

or at least they are thinking in the same direction. So today we are going to talk about what RAG is.

15:07

But everyone, we are going to follow a slightly different approach to understand RAG.

15:12

Because see, RAG is a solution to some problem. Now, if I directly tell you what RAG is,

15:18

without telling you the problem statement first, I don't think that will be a very good approach

15:23

of understanding what RAG is, right? Correct? If you are understanding some kind of solution,

15:30

first you should understand the pain point, right? What is the pain point? What used to happen

15:35

before this solution? What will happen if you don't follow this solution? What is a problem

15:40

statement? What will happen to our AI applications if you don't follow the RAG approach? Right?

15:46

That is what we are going to start with.

15:48

Right? Everyone clear with the agenda? First, we will spend a few minutes on understanding

15:53

the core of the problem statement, right? That is, I would say, that is the best way to learn any

15:58

technology out there. First, try to start with the problem statement and then eventually see the

16:03

solutions. And finally, everyone, you will be able to build the solution on your own. Right? So let's

16:08

start with what is a problem statement. Before even we start with the problem statement,

16:12

first you tell me, what is the brain? Like, what acts like a brain?

16:18

for any AI application. What is something that is there in all the AI applications? It is

16:24

LLM. Right? It is LLM. Now what every AI application essentially does? Right? So guys,

16:31

can I say that every AI application internally it will have LLM. Correct or not? Every AI application

16:38

internally will have some sort of LLM. It can be Open AI LLM, it can be Gemini, it can be some open source,

16:44

anything. What a user does?

16:48

User makes a query and LLM will try to generate an answer, right?

16:54

LLM will try to generate an answer. You mean agentic any AI application, right?

16:59

Agentic AI, chat GPT, or any other AI application, even if a simple Generative AI application,

17:06

Divi, Agentic AI is advanced version of generative AI, right?

17:11

Agentic AI means that you are trying to do some actions also.

17:14

Generative AI means that you are just generating the text, generating the information.

17:18

information, generating the data. Make sense? See, that is a different field.

17:24

So see, what happens is AI is a very big field. Now, if you are building any generative AI application,

17:31

then it would definitely have LLM, right? AI has a lot of other things as well, right? A simple

17:36

machine learning model, other things, right, they might not need LLM. When we are talking about

17:40

our AI application, the common AI applications that we are building nowadays, that means we are

17:45

trying to talk about, we are actually, we are trying to mention about.

17:48

Generative AI application. That is the most common way of implementing AI applications

17:53

nowadays, to reach to like maximum number of people. Okay. So what LLM does everyone? A user gives

17:59

a query to the LLM and what LLM does? LLM will try to process this particular query, right? Query

18:05

is nothing but the prompt. LLM will try to process the prompt and based on all the information

18:12

it has, right? Can I say that LLM has humongous amount of information, almost

18:17

everything which is present on internet is present inside LLM. Correct or not? Yes and

18:25

you go on? So LLM is what? LLM has been trained on, right? So first of all, every LLM, it is a pre-trained

18:32

model. Now guys, when you are using any LLM, do you need to train it again and again? Do you need to

18:38

train it on your own? Do you need to train this on your own? No, it is a pre-trained model.

18:46

Right? So for example, let's say if you're using GPT, the latest model of GPD 5.4, right?

18:52

So what this pre-trained model does everyone is, it is trained on huge amount of

19:16

Internet data. Now, guys, one thing that I would like to mention here is that I have

19:22

written here internet data. It means that everyone, do you think that any common LLM, right, any

19:29

LLM, how to make LLM? It's a very big tedious process. If you are a company like OpenEI,

19:34

then you can build your own LLM, right? So it takes millions of dollars, in fact, billions of dollars

19:39

in today's world to build a good LN. Okay? It has a lot of, lot of technology running internally as well

19:45

there's a lot of hardware. A lot of resources are required. You will have to hire not AI

19:50

engineers. I would say you will have to, you need to hire AI researchers like scientists. These

19:55

people are actually scientists. They are not ingenious. Engineerses can build stuff, right? And AI researchers,

20:02

right, if you talk about open AI, meta, etc, they are paying millions of dollars to their

20:07

AI researchers. Have you seen that news? I think I've talked about that in the past also. Right, the kind

20:12

of salaries that they are getting, they are getting like millions of dollars of

20:15

of salaries. These are the people that you, these are the kind of people that you need in order

20:20

to build your own LLM. It's a very, very long process. It is not something that you can build

20:25

in just few days. Okay, anyways, right? So guys, LLM has been trained on huge amount of internet

20:31

data. It means that everyone, every LLM, right, has been trained on publicly available data. For

20:38

example, I have my own company or let's say Massai School, right? So let's say there is a company

20:42

called Masai School, right? Or if you have your own company, do you think that any LLM model,

20:49

any large language model, be it open AI, Gemini, Claude, et cetera, et cetera, have they been trained

20:56

on Masai school's database? If let's say Masai school has a lot of policies, right, refund policy, student

21:02

policy, exam policy, attendance policy, instructor policy, mentor policy, etc, etc. There are a lot of

21:08

policy documents that they have internally. Do you think that any LLM model,

21:12

can access these private information, access these private policy documents, and they can

21:18

be trained on this information. Do you think so? Technically not, right? Assuming that Masai school is not

21:26

making these documents public. So if obviously any company will not make their private documents

21:31

public, if those documents are not publicly available, any LLM model will not be trained on this

21:36

information. Everyone clear? So these LLMs, right, any LLM is trained on huge amount of data.

21:42

But what type of data, internet data, the data which is publicly available.

21:47

So when you give a prompt, what LLM does?

21:49

LLM will process the prompt and it will give you the response.

21:53

It will give you the response.

21:55

This is what a simple, generative AI application does.

21:59

Is that going to all of you?

22:02

Is that going to all of you?

22:03

This is what a simple generative AI application does.

22:06

But everyone tell me, can I said every LLM has some cutoff data.

22:12

Correct or not? Every LLM has some cutoff date. Now what is the meaning of cutoff date

22:18

everyone? For example, let's say assume that GPT 5.4, right? You can see the release date of GPT 5.4.

22:25

So this particular model or any particular model has been trained on the internet data till that

22:31

point of time, till that particular day. For example, assume that the cutoff date of this LLM model, whatever

22:38

model you are using, let's say the cutoff date was, for example, let's say 30 first, the cutoff date of this LLM model,

22:42

31st of March, 2026. This is the cutoff date. It means that on this particular date,

22:50

this particular model was released for public usage. Now, everyone today is 22nd of April. Now,

22:57

if you ask any question about the event, about the thing which has happened after 31st of March

23:04

till today, let's say, for example, if you talk about the latest news about Iran versus USA war for

23:11

today. Do you think that this particular LLM has that information already? Do you think so?

23:18

That LLM does, does LLM have that information? That what is going on in the latest, like what is

23:25

the latest status of the US versus Iran war? Answer is no. Now what LM will do then? If LM does

23:32

not have that information, what LLM will do now? Fetched from Internet. Fetch from Internet.

23:41

but assume that you have not integrated internet, right?

23:45

So guys, do you see that all of you got the answer?

23:48

That is the absolutely correct answer, right?

23:50

That it will search on the internet.

23:52

But don't you think even this is an extra step, right?

23:54

The chat GPTA application, or let's say you are using chat GPD.

23:58

So chat GPT, open AI engineers, they will have to integrate internet, right?

24:03

what they will have to do internally, they will have to write the code that, okay, if some information

24:07

we do not have, then please make an internet call.

24:10

But assume that everyone, as of normal.

24:11

Now we are building a simple application.

24:13

Internet has not been integrated yet.

24:15

There is no integration to internet.

24:17

That means your LLM cannot make internet call, cannot make external call.

24:21

So can I say that everyone, your LLM will try to guess.

24:24

This is what we also do in the exam also, right?

24:28

Correct.

24:29

Absolutely sure.

24:30

What LLM can do, in fact, first step is either LLM can refuse.

24:35

Simple it can refuse that, okay, sorry, I don't know this answer.

24:38

Correct?

24:40

Folks, yes or no?

24:41

LLM, first option is LLN can simply refuse to give the answer that, okay, sorry, I don't know this answer.

24:46

Please check somewhere else.

24:47

I don't know about it.

24:48

But is this a good way?

24:51

Is this a good way to build your application?

24:53

Absolutely not.

24:54

So what you can do everyone is, assuming that you have not integrated internet as of now.

24:59

Other way that LLM can take is, LLM will try to generate an answer, right?

25:04

This is exactly what we try to do in exams also.

25:07

For example, let's say you are giving some exam.

25:09

Now you have read a lot of things, right?

25:10

you have read, let's say, 90% of the syllabus.

25:13

Now, if you get any question from the syllabus that you have already studied, you will be able to give

25:18

a very confident answer, correct?

25:21

You will be able to generate an answer by very high confidence.

25:24

Yes or no?

25:25

That okay, this is something I have studied and I know this.

25:28

I can generate a very good answer for this, correct?

25:32

But everyone, a lot of times what happens is that we get a question for which we do not know

25:37

anything.

25:39

Most of the times happens, this happens right?

25:40

that we have got a question for which we have not studied anything.

25:46

We don't even know a single character for that particular answer.

25:50

Now, there are two ways.

25:52

Either you reject that question, you leave that question completely empty.

25:56

But if you don't generally, if we have time, do we do that?

25:59

If that exam is very important, that is a board exam, that is some competitive exam.

26:04

Do you leave that question empty?

26:06

No.

26:07

Because if you leave that question empty, you will get for sure zero marks.

26:10

What do you try to do?

26:12

You try to guess.

26:13

You try to guess and you try to write, you try to generate the best possible answer based on the

26:20

understanding that you have.

26:23

Correct?

26:23

Based on the understanding that you have, you try to generate the best possible answer.

26:27

It may be wrong.

26:28

It may be somewhat right, but it might not be, it will not be very high confidence answer.

26:33

This particular process in the concept of LLM is called as hallucination.

26:40

Is that point clear to?

26:40

all of you. This is called as hallucination. What LLM tries to do, if LLM does not

26:48

know any particular concept, it will try to give you some random answer. It will try to generate

26:53

the answer based on its understanding. It may be correct. It may not be 100% correct, but still

26:59

it will try to give you because if it does not give you the answer, that is a worst thing.

27:03

So just to avoid the worst thing, it will try to still give you an answer. Maybe wrong.

27:07

Maybe not 100% correct. That particular process is called as hallucination.

27:10

Is that all of you?

27:17

Correct?

27:18

Now, everyone, do you think that having hallucination in generative AI applications or agenetic AI

27:25

application is a good thing. That if your AI application hallucinates, if it tries to give you

27:31

the answer, even if it is not aware of that, do you think that it is a very good idea?

27:37

Answer is not at all.

27:39

So, guys, all of you understand this point that.

27:40

ideally, we should try to reduce hallucinations.

27:44

Hallucinations are not recommended or not desirable.

27:50

Nobody wants any model to hallucinate.

27:53

Not desirable.

27:55

Okay?

27:56

So try to reduce hallucination as much as possible.

28:10

as much as possible.

28:18

How many if you're clear with this?

28:20

Try to reduce hallucination as much as possible.

28:22

How can you reduce hallucination, everyone?

28:25

How can you reduce hallucination?

28:27

If I don't know something and you are asking me that question, I should study about it.

28:34

You should give me some source.

28:35

Correct?

28:36

You should have some source, right?

28:38

For example, as all of you, like some of you, like some of you,

28:40

mentioned that if you ask about the latest news on Iran-USA war from your model, if your

28:47

model does not know that information, then your model should check with the internet, check on

28:52

internet, right?

28:53

So don't you think, everyone, if your model does not know any answer, it is searching on the web.

28:58

So you must have seen on chat, GPD, searching on the web icon, right?

29:02

Have you seen that?

29:03

That if you ask any questions, for some questions, it checks on the internet, it searches on the

29:07

web, for some questions, it does not.

29:09

Obviously, everyone, if it involves some checking some extra information from internet,

29:14

it will check on the internet.

29:16

Else, it will try to generate the answer based on its understanding.

29:20

As of now, is everyone clear till this point of time?

29:24

So this, LLMs are very good at what?

29:28

LLMs are very good at generation of the text.

29:31

If it just has to generate, given that it already has the context of that question.

29:36

LMs are very powerful, right?

29:39

Right?

29:39

So can I said every one, we can say that LLM, LLMs are very powerful.

29:53

LLMs are very powerful, but can I say they have limited knowledge.

30:00

They cannot have all the knowledge of the world, right?

30:03

They have limited.

30:09

knowledge. How many of you are clear with this? LLMs are very powerful, but they have

30:17

limited knowledge. Now, when I say limited knowledge, everyone, there is a small star here. There is a small

30:22

catch. There is a small condition here. When I say limited knowledge, everyone, that means that

30:26

LMs cannot have every information in the world. For example, even, let's say if you are building

30:30

your own chat support agent, right? For example, let's see you are building a chat support agent

30:35

for a company like Zviggy, Amazon, Zepto, etc. Now, everyone, you are building, you are building your

30:39

using, you're building a AI agent or you are building a chatbot agent, which can

30:45

automatically resolve the queries of the people, of the users without, without any human intervention.

30:52

It can process the refund, it can initiate the refund, it can call the delivery guy, it can tell you

30:57

the status of the order, if there is any issue with the order, it can let you know, it can call

31:01

the restaurant, etc, etc. Some basic operations it should be able to do without any human intervention.

31:06

Clear? Okay? Now, don't you think.

31:09

want to give the answer to the user, you should have some LLM. Definitely Svigi will be using

31:15

some sort of LLN. They can use Open AI, they can use Gemini, they can use some open source,

31:20

they can have their own LLM also. They will have some LLM. But everyone, do you think that that particular

31:25

LLM will have the information about the internal SwayE policy documents when to process the refund,

31:31

when not to process the refund, when to, let's say, when to cancel the order, when not to cancel the order,

31:38

when to call delivery guy, when not to call delivery guy, when not to call.

31:39

delivery right? When to call restaurant, when not to call. All of these policies, everyone,

31:44

don't you think they are very, very private to Sviggy? They are very, very limited to Svigy. They are

31:48

not present publicly available. They are not publicly available, right? Or let's say you're

31:53

building some chatbot, chat agent for American Express, some banking application. So they have

31:59

some internal documents. Now to, in order to resolve user queries, don't you think the chat agent,

32:05

that is the LLM, should have the access to these tools? When should be processed?

32:09

the refund? What are the conditions for order return? What are the conditions for

32:14

refund and whatnot? Are you guys getting this point? So that particular agent should be able to

32:20

access these internal policy documents. Assume that everyone, there are no internal policy documents.

32:26

Let's say Sviki built a chatbot using Open AI LLM model. Now if you ask any question

32:32

about the refund policy of Svigy, assuming that it is not publicly available, this data is not

32:36

publicly available. This is not publicly available. This is internal to Sviki. Now, do you ask you?

32:39

Do you think that Open AI LLM does not matter how powerful it is? Will it be able to give

32:45

you a very, very accurate answer that why and how does, like what are the policies, what are the

32:52

what are the conditions for getting a refund from Svig? In what cases you get the refund from Svig.

32:57

Do you think so? Does not matter how powerful your LLM is. Will it be able to give an accurate

33:02

answer for this query if it does not have the access to internal Sviggy documents?

33:09

How many few are clear till this point of time?

33:16

Yes, it will not be able to give the answer.

33:18

Most of the times, everyone, let me give you another example.

33:21

A lot of times you ask me a query about attendance, PSP, exam, etc.

33:26

If I have that answer, if I know that, I give you the answer.

33:29

Otherwise, what I tell you that, okay, please check with the support team.

33:32

I don't know this answer.

33:33

Or what I can do is, everyone, if Masai team gives me the access to all their

33:39

internal documents, all the policies. If you ask me a question, if I know the answer, I'll

33:43

directly give you. If I don't know the answer, I can check that. I can check that database,

33:48

all the policy documents that Masai team has shared with me. Getting the point? This is what

33:54

exactly we are talking about. Everyone clear? This is exactly what we are talking about. This

34:00

thing is called as rag. I will talk about in some time. Don't worry about it. I have not even

34:05

talked about the full form of rack. We'll come to that. As of now, we're just building the

34:09

fundamental. Even with context from RAP, it came to know the policies and generate

34:15

text. How can we enforce these policies in its response? That is something that we will have to use

34:19

LLM for that. I'll come to that. So once you retrieve the documents, once you get the documents,

34:25

then the corresponding document in which let's say the user is asking about the refund. You will

34:30

fetch the refund document from the policies, from the documents. Then you give that document to the

34:35

LLM, then LLM will analyze the document, and then it will try to give the answer in this

34:39

way that, okay, the refund is eligible, the refund is eligible, you are not eligible for refund because

34:45

of this reason, or you're eligible for, you're eligible for refund for this reason. You'll have to

34:51

decide that with the help of, again, you'll have to apply some brain using LLM. So guys,

34:55

can I say that LLMs are always, always do have some limitations, right? So let me write down some

35:02

limitations of LLM.

35:16

Folks, how many if you're clear till this point of time?

35:20

We are just trying to understand the fundamentals for now.

35:22

Please interrupt me at any point of time because I can guarantee you kind of, right?

35:28

We are learning these in the best possible way.

35:31

At least up to best of my knowledge, best of my way of teaching, please try to understand

35:37

all the things in complete depth. Most probably you will not find this kind of in-depth content

35:42

easily on the internet. So please utilize this understanding very, very wisely. Utilize this time

35:48

very wisely. Feel free to ask any doubt. Okay. What are the limitations of LLM? That why do we even

35:54

need to add external data source policy documents, some extra source of information with LLM?

36:01

despite being, despite of the fact that LLM already has humongous amount of information.

36:08

They have trillions of parameters. Correct, everyone?

36:11

Because everyone, one thing that we need to understand is that LMs have static knowledge.

36:18

Correct or not?

36:23

LLMs have static knowledge.

36:25

Now, what is the meaning of static knowledge?

36:27

Because of cutoff data.

36:29

Now, for example, let's say if the LLM.

36:31

that you are using, if that was launched on 31st of March 26, this is a cutoff date.

36:38

Now, if you are using this LLM on 22nd of April, it does not have the information about the

36:44

events that have happened during this period. Now, you can say that, Ovi-Dipak, why can't we

36:48

give this information to LLM every day? For one day, we will give every information to LLM

36:54

for this, for new day. Whatever has happened today, we will give that information today. What will

37:00

happen tomorrow, we will give that information to LLM tomorrow. Can we do that? Yes, we can do

37:05

that. But do you think that everyone training, this is this process is called as training.

37:09

You are training the LLM. Do you think that training the LM is just a very simple thing that you can

37:15

do on everyday basis? Do you think so? The training is something like you can do every day,

37:21

forget about it. Training is something that you can not do even a day, even a week, even a month.

37:26

You cannot train this kind of bigger model with.

37:30

billions of parameters, trillions of parameters. Even if you add one text, one word,

37:35

or let's say one sentence or one document inside the LLM, it will affect trillions of parameters.

37:41

Trillions, right? Correct, everyone. It will affect trillions of parameters. It is not at all

37:48

possible. It is extremely costly. And that's why everyone, every few months you get a new LLM

37:55

model because it takes months and months of time, which are headed by

37:59

like high quality engineers, like best engineers of the world and best GPUs, best CPUs of

38:07

the world. Then it takes months and months of time for any company to launch their new LLM model.

38:13

They have static knowledge because that knowledge will not change over the period of time.

38:18

So if something changes after the cutoff date, LLM will not have that information. Policies can change.

38:25

For example, stock price can change. IPL, if let's say IPL is going on right now,

38:29

IPL statistics can change. What is the point of every team? What is the table looking

38:34

like right now? How the table is looking like, looking right now? It will keep on changing.

38:39

So LLM will not have that context. Make sense? Also everyone, LLM does not have access to private

38:49

information to any company. Does not have access.

38:59

Private policy documents.

39:10

Folks, yes or no? If you're building your own chatbot agent today, you are for your own company,

39:16

now you are the only person in the company, for example, who has the access to the policy documents

39:21

internal, which are very, very confidential, right? No one knows about that. So LLM will also be not aware

39:26

of that. If you want LLM to generate the answer for based on the answer.

39:29

the policy documents, you will have to share with that. LLM will not have the access to that.

39:34

Makes sense, everyone?

39:37

Right? LLMs can hallucinate.

39:42

Hallucination is also one limitation, right?

39:46

If it does not have any particular information, it can try to give you any random answer. This is

39:51

called as hallucination. Make sense, everyone?

39:59

Okay, so hallucination, so these are the limitations of LLM, right?

40:05

So why hallucination happens?

40:08

Hallucination usually happens when the model does not actually know the answer, and it tries to fabricate

40:14

the answer based on the existing information.

40:17

Make sense?

40:19

Okay, now let's finally move to the other thing, which is something called as grounded AI system.

40:29

Okay? Before we actually understand the definition of RAG, there is something, there is a term called

40:36

as grounded AI systems. Anyone would like to guess the meaning of grounded systems?

40:59

Kind of yes.

41:01

Guys, can I say that? Like, okay, if I tell you that there is a model which looks very good, right?

41:07

which looks very good and it will always give you the answer.

41:10

Forget about whether it is correct, whether it is accurate, whether it is coming from verified sources,

41:15

forget about it. But it will always give you the answer. It is guaranteed.

41:19

Do you think that that model will sustain for very long time in the market?

41:22

If it is giving you answer without even any verification, do you think so? That model will sustain in

41:29

market for very long time? No, right? Models should be able to give you, not only the

41:38

answer, but they should be able to give you the answers which are more accurate, which are more

41:44

reliable, right? Is that one clear all of you? So grounded AI systems means that that models response

41:59

response should be based on external external or verifiable, reliable, reliable information.

42:29

and not only on memory. Not only. Models response should be based on external,

42:41

verifiable, reliable information and not only on internal memory.

42:50

Correct, even? It means that model should not only depend on the information what it already

42:54

has. It should not only depend on the pre-trained information. It should not always give you

42:59

the answer based on the pre-trained information. It should be able to give

43:03

you the answer if required. It should be able to give you the answer based on some external

43:08

source, some documentation, some official documentation. For example, everyone, if you ask any

43:12

question from chat GPT based on, let's say, related to Amazon, related to Swiggy, then it will not

43:17

hallucinate. What it will try to do, it will tell you, right, if you're using paid model. I think

43:22

it shows you now in the free model as well. It shows you that, okay, I'm checking internal Amazon policy documents.

43:28

Obviously, everyone, it can only check the data which is publicly available.

43:32

So it will go through all the terms and conditions. It will go through all the frequently asked questions.

43:37

Then it will try to generate an answer. And then it will also give you a source that I am giving you the answer based on this information.

43:44

Have you seen that? Then it becomes more reliable source. Is that not clear to all of you?

43:53

Right? So guys, now tell me, if you have an

43:58

AI application, which hallucinates, which hallucinates, is that, can that be considered

44:06

as a grounded AI system? Can that be considered as a grounded AI system? If a system can hallucinate,

44:14

if a system hallucinates, that is not a grounded AI system. Grounded AI system means that even

44:20

that you have integrated external data sources, it can be internet, it can be whatever source that you need

44:24

to, that you need to go through, that you need to refer.

44:27

then you are giving the answer based on the verified information, reliable information.

44:33

That is what is the meaning of grounded AI system.

44:36

And guys, whatever we have discussed in last almost 30 minutes, all of these things are solved

44:42

using something called as RAG.

44:46

So RAG is the way in which you use some external source.

44:52

It can be internet, it can be books, it can be policy documents, it can be something else, whatever

44:57

internal source of information that you are putting in, that, okay, that LLM can use in

45:02

order to generate the answer, that LLMs can retrieve the information that you have embedded,

45:07

that you have added, and LLM can use that information, the retrieved information, and it can

45:13

generate the answer based on that, so that it does not hallucinate, so that you can reduce

45:17

hallucination. That particular concept is called as R-A-G-G-G-R-A-G-R-R-A-G-R-R-F. The rack full-form

45:22

everyone is something like this. The full-form of rag is what? Retrieval.

45:27

Augmented generation. Retrieval augmented generation.

45:41

So does low sampling probability and low temperature also weigh to make model grounded?

45:48

If you see, you can say that, those are the parameters that contains the, that decides the output.

45:57

But if, let's say, if LLM does not have the information, right, if LLM is trying to generate

46:02

the answer without having any context, that is what hallucination means.

46:07

Low sampling and low, like basically the sampling parameter and you can say that, sampling

46:14

and temperature parameters, they are there to control the type of the output that you want.

46:20

They don't have direct or indirect, I would say they don't have direct control on hallucination.

46:24

Because hallucination will happen when you don't.

46:27

have the context. And still you are trying to generate the answer. But you can still

46:31

use the sampling parameter or temperature parameter even if you have that context.

46:37

Makes sense? Even if you know the answer, then you can also, then you can still control sampling

46:41

and temperature parameters. So slightly different things. Make sense? But sampling and

46:48

temperature cannot be used to control hallucination. Everyone clear till this point of time?

46:57

So, all the things that we have seen in last 30, 40 minutes, they are solved via RAG.

47:01

Now, what is RAG, everyone?

47:04

So, let me write down a few terms, a few things, and then it will make more sense to all of you.

47:08

So, guys, RAG is an approach.

47:10

Rag is, it is an approach.

47:27

where the system takes the user query, AI application takes the user query,

47:39

takes the user query, retrieves the information, retrieves the information, retrieves the information from

47:57

external knowledge sources, right? Then everyone, once you have got the information,

48:11

should you return this information as it is to the user? Let's say if you're checking about the

48:16

refund policy on Amazon chatbot, Amazon chatbot checked the refund policy document. Should

48:22

it return the document as it is to you? No. Then, again, LLM will come in to you.

48:27

to picture now, you return this information. You give this information, whatever you

48:31

have retrieved from the external sources, from the database, you give this information to LLM. Then

48:38

LLM will apply their mind and then they will try to generate the answer that we can return to

48:44

the user. Right? So we can provide this information. Provide this information to the LLM for context, provide

48:57

information to the LLM as context. And then, then everyone, what LLM will do?

49:18

LLM gets this information, then LLM generates the answer.

49:27

using the retrieved context.

49:41

Is that point clear to all of you? Yes or no?

49:49

Will this information also be converted into embeddings? I'll come to that.

49:57

Guys, please go through these four steps one by one and let me know if it is making sense.

50:02

Take 30 seconds of time.

50:04

30 seconds or one minute of time.

50:07

Just read these four steps right now and let me know if the flow is making sense to all of you.

50:13

And I hope it will make sense because we have already studied a lot of things about AI in the past.

50:27

Now, for example, everyone, let's say you are interacting with Amazon chatbot agent and you are asking some information about order, return.

50:39

Can I return the order? Can I get the refund, etc, etc. Once you ask a question, what chatbot agent will do?

50:46

Agent will try to find the relevant documents for this query. You are asking about return. What type of product you have ordered? Let's say you are asking about the return of an electronic item. Let's say iPhone.

50:57

you want to return an iPhone, right? Or let's say you got a damaged product. Something like that you are

51:02

talking about. And then agent talks to the, talks to the LLM that, okay, do you have this information? No.

51:08

If you don't have this information, then the agent will try to interact this, get this information, retrieve this

51:16

information from the policy documents. Assume that you have stored the policy documents at some place.

51:22

Now your agent will go to that place, go to that database where you have stored the policy documents.

51:26

Now, don't you think it will have to like, there are thousands of documents. How will you find out that which document is the maximum, like which document is related maximum to your query, to the user's query? Let's say user is asking about return or refund. There might be thousands of documents, right? So you'll have to find the closest document which is matching with the user's query. How do you perform the closest search or similarity search based on what understanding, based on what

51:56

idea, you perform similarity search, vector embeddings. Correct or not, everyone? It means that all the documents you

52:04

have converted into embeddings, correct everyone? All the, all the documents you have converted into embeddings and those embeddings, you have

52:12

stored at some place. What is going to be that place? We know that from the last class. See, we know that from the last class, right?

52:25

In vector database.

52:26

For example, in the last class, we saw an example of ChromaDB. You can store all these documents into ChromaDB, and then you, when the user comes in, user ask a query, you convert the user query also into embedding.

52:38

Then you try to convert, then you try to find the nearest embedding. Correct, even, then you try to find out the nearest embedding.

52:45

Based on the embedding, you try to find out the relevant document. Give that document to the LLM.

52:50

LLM will get the information, generate the answer, return to the user.

52:55

Don't you think this is something that we have.

52:56

already built in the last class. Very, very similar thing. Now we are just going one step ahead.

53:02

Yes or no? This thing we have already built in the last class. And in the last two or three

53:06

classes, we have been studied very, very similar things. If you see this, we have learned already, right?

53:13

So in one of the classes, we have also talked about, right? In one of the classes, did we also talk about,

53:26

chunking process. That document gets divided into multiple chunks. We'll see that,

53:37

no worries, right? We'll see that. Okay, there is one question. Let me go through that. When we say LM

53:43

generated the answer using the retrieved context, in this case, LLM's roles is only to convert the embeddings.

53:48

No, see, once you have the embeddings, you compare those embeddings, then you based on those embeddings,

53:54

you try to find the closest embeddings. For that closest embedding, you have the document

53:58

already. Once you get the document, you give that document or chunk to the, that information

54:03

to the LLM. Then LLM will use that information and then kind of it will sugarcoat it. Because you cannot

54:09

just throw the answer, the policy document to the user. You will have to say that, okay? Hey,

54:15

let's say, hey, Divya, as per the policy, this is the information so that you are not eligible for

54:21

because the policy says refund is only eligible for within seven days, something like that.

54:28

So what LLM is doing? LLM is just sugar-coating. The policy, it is just trying to convert the actual

54:34

information into the type of information that you can return to the user. Because you cannot just

54:39

directly throw the information as it is to the user. You'll have to sugarcoat it. You'll have to

54:44

return that in a user-friendly. If the documents gets updated, should we update the vector database

54:49

with some badge of, yes. We do this.

54:51

that. We do that. The internal memory of an LLM is stored in a vector database? No, that is a different

54:57

thing. Vector database is different thing. So LM stores their information separately. See, you can see

55:03

that LLM is a different thing. Vector database is a different thing. Will LLM convert the text inside the document

55:09

as embedding? No, it is not the task of LLM. If you see, if you remember the last class, in the last

55:14

class, when we created a vector database, we used another model, right? Text embedding model. Correct?

55:21

So for example, let's say open AI gives the small model, large model. So these are the different

55:26

models that you can use to convert the data into embeddings. How many if you're clear till this

55:30

point of time? Yes or no? Right? Folks, let me know if it is making sense. Okay, now everyone,

55:43

let's come back to the definition of RAG, retrieval augmented generation. So guys, RAG is built up of

55:51

three terms, retrieval, augmented, and generation. If you just understand the meaning of two terms,

55:56

retrieval and generation, you are done. Retrieval means you retrieve the information. Using the retrieved

56:02

information, you generate the answer. So let me write it down in a very simple way that

56:09

how does, like what is the simple definition of rag? What rag does? Rag does? Rag.

56:21

Rag combines, Rack combines, retrieval of relevant information from

56:51

external sources. First, it combines the retrieval process, retrieval of relevant information

56:59

from external sources and generates. And generation of generation of response, generation of responses,

57:21

You can say that natural language.

57:24

Language that user can understand easily or naturally. Can you explain on the embedding conversion?

57:33

Who does this now? In the last class, did we convert, did we see this? See, this is what we have seen in the last class.

57:41

Convert each data item into embedding using some model. What this model can be? In the last class, did we use some model?

57:50

Correct? Remember that sentence transformer, right? We used sentence transformer to

57:56

convert it. Right? So what happens is, for example, you have a policy document, right? In fact,

58:02

just a second, let me show that to you. Let me open Visual Studio.

58:11

Yeah, this is our project, right? VectorDB, vector search.

58:16

Guys, remember this project, right? Let me build

58:20

on Monday, just one day back, two days back, correct? If you see this code vector DB,

58:26

right? You have these documents, you have to store these documents into vector database. So,

58:34

if you see, we are using some model. It can be this model. It can be some open AI text embedding model.

58:43

Did I show you this model also? Test text embedding model. There are two models, small model.

58:50

Small model generates 1536 dimensions, right?

58:55

Large model.

58:58

T072 dimensions. So you can use any of these models.

59:10

You can use any of these models. There are also hundreds of models present out there.

59:15

You can use any one of the model to convert vector into, to convert document or any data.

59:19

or any data into embeddings and then you store those embeddings into database.

59:24

Which type of database?

59:26

Vector database. Makes sense, Divya?

59:28

This is what we have already seen in the last class.

59:31

Folks, yes or no?

59:33

Okay? For your reference, everyone, please go through this.

59:37

Right? First we have, first we have the data.

59:42

Then we convert this data into embeddings.

59:45

Then we store these embeddings into database.

59:47

Then we have the user query.

59:48

the user query, then we convert this user query into embeddings.

59:52

Then we perform similarity search.

59:54

This is the user query.

59:56

Then try to find out the nearest vector, the closest vector, top 3, top 5, top 10, with respect to the query

1:0:03

vector.

1:0:04

Then you find out that and then finally you give one of those answers.

1:0:08

Then you try to generate the answer using LLN.

1:0:11

If you see exactly what we have done.

1:0:14

Will vector database also have embeddings about the previous human feedback for it?

1:0:17

is human feedback for responses. It depends whether you have incorporated that or not.

1:0:21

Definitely it can have. But you will have to implement that separately.

1:0:25

Right, Vamsi? But your point is absolutely valid. Can it have? Yes, it can have.

1:0:30

Everyone clear?

1:0:35

So guys, if you see whatever we are talking about RAG, whatever we are talking about in today's class,

1:0:42

that is some part of it is already coming from the previous knowledge that we have already seen in the previous classes, right?

1:0:47

The last few sessions, they are kind of interconnected.

1:0:50

They are all talking about internally vectors, embeddings, vector databases.

1:0:55

In today's class also, we are again going to talk about vector databases in slightly different perspective.

1:0:59

Right?

1:1:00

So if everyone is clear, we can have a break right now.

1:1:03

And after the break, we will dive deep into the understanding of what RAG is.

1:1:07

What are the different components of RAG?

1:1:09

Okay.

1:1:10

So, yeah, then just one more thing.

1:1:13

Let me just complete the definition.

1:1:15

RAC combines retrieval of relevant information.

1:1:17

from external sources and generation of responses in natural language.

1:1:22

So retrieval and generation. Retrieval and generation.

1:1:27

Make sense? So we can say that one more thing. So instead of answering only from

1:1:47

memory.

1:1:48

So instead of answering only from memory, memory means everyone the pre-trained information,

1:1:58

right?

1:1:59

So instead of answering only from memory, the model answers, the system answers, from, from,

1:2:17

external sources as well, external evidences as well.

1:2:23

Everyone clear till now? Is this definition clear?

1:2:27

Okay?

1:2:30

Okay?

1:2:31

Okay.

1:2:32

So guys, now I'm sharing the link with all of you of today's class notes.

1:2:36

In case you want to go through this, we can have a break now.

1:2:40

Okay, we can go for a break right now.

1:2:46

And after the break, we will talk about the remaining content.

1:2:51

So these are the notes for today's class.

1:2:53

Live notes for today's class, okay?

1:2:56

So as it's 858 almost, let's meet at around 9, 10, 9, 11.

1:3:00

Okay?

1:3:01

Let's have around 10 to 12 minutes of break.

1:3:03

Please get a brief idea about what we have discussed, then we'll talk about the remaining things.

1:3:08

What is our LLM training pattern, how to choose LLM that suits your needs?

1:3:13

I think we have already talked about it, but always.

1:3:16

right? In the previous classes, we have talked about it in a brief. But if you see, this will keep on changing.

1:3:22

The model which suits your requirement, which is not very expensive, which is, for example, let's say, if you're

1:3:27

solving some kind of complex problems, then you need very high quality models. If you are solving simple

1:3:32

problems, then you need simpler models, depending on the cost as well. If you're using very, very complex

1:3:37

models, it will be very, they will be very expensive. Now you need to decide that whether you are ready

1:3:41

to spend that kind of money or not, right? So in fact, you can use some LLM to find

1:3:46

out which LLM will be best suited for your use case. Tell your use case, try to compare,

1:3:50

and then you'll try to get one final answer that, okay, we can use this particular model, which

1:3:55

is going to give us decent answers in decent cost. Because cost is also very important factor

1:4:00

while deciding the right model. If you choose a very, very costly model, it is not going to work

1:4:05

for very long time. Okay? Okay, so guys, it's nine. Let's meet around 912.

1:4:16

Thank you.

1:4:46

Thank you.

1:5:16

Thank you.

1:5:46

Thank you.

1:6:16

Thank you.

1:6:46

Thank you

1:7:16

Thank you

1:7:46

Thank you

1:8:16

Thank you

1:8:46

Thank you

1:9:16

Thank you

1:9:46

Thank you

1:10:16

Thank you

1:10:46

Thank you

1:11:16

Thank you

1:11:46

Thank you

1:12:16

Thank you

1:12:46

Thank you

1:17:16

Okay, Hi, everyone, am I am I am I am I am I am I am able.

1:17:30

Okay.

1:17:31

Okay.

1:17:32

Okay. Now let's get started with the next

1:17:34

Okay.

1:17:35

Now let's get started with the next discussion, everyone, that is what?

1:17:46

pipeline is nothing but what are the different steps involved, etc, etc, right?

1:17:50

So guys, can I say that rag solves or rag helps or rag helps solve, helps solve the limitations of

1:18:08

of plane LLN?

1:18:09

Can we say that?

1:18:14

Hallucination.

1:18:15

Rag helps solve the main limitations of plane LLM.

1:18:22

Rags helps solve the main limitations in the application.

1:18:40

Make sense, everyone?

1:18:43

So yes, without RAG, can is that your model answers from the pre-trained general information

1:18:49

it already has?

1:18:51

Correct or not?

1:18:52

Without RAG, your model just tries to answer based on the general pre-trained information it has.

1:18:59

But as soon as you integrate RAG, it means that you're trying to be more specific, more trustworthy,

1:19:05

right?

1:19:05

and your answers are going to be more reliable.

1:19:08

Does that make sense, everyone?

1:19:13

Now, I think grounding also makes sense to all of you.

1:19:22

So what is the meaning of grounding in RAG applications?

1:19:27

So guess, do you think that Rack applications will try to invent the answer?

1:19:34

In inventing the answer means that they do not know the answer, they will just try to write whatever

1:19:37

they want, they will try to invent a new answer.

1:19:40

Inventing the answer means hallucination.

1:19:42

In Rack.

1:19:43

application, do you think that you expect the answers to be invented from the model?

1:19:51

Answer is no, right? In RAG applications, rag applications are more grounded. It means that

1:19:58

they give you the data, they give you the answer which are more specific, more reliable and more

1:20:03

trustworthy. Make sense, everyone? Okay. For example, everyone, let's take an example.

1:20:13

The example is as follows. Let's say if you are having a, in your companies as well, do

1:20:18

you have some internal chatbot? In your companies as well, do you have some internal chatbot?

1:20:24

For example, everyone, let's say if I take my example at Microsoft, like Microsoft is a very big

1:20:30

company. There are like millions of employees, at least I think millions of employees should be there

1:20:34

across the world. Now there are a lot of policies, right? Different, first of all, in India itself,

1:20:40

there are thousands of people who are working at Microsoft.

1:20:42

different, different domains, engineering domains, support, technology, AI, then vendor,

1:20:49

and whatnot. Similarly, there are, like, Microsoft is there in hundreds of countries. All of you

1:20:55

understand that, there are a lot of policies which are present at Microsoft for different, different

1:21:00

countries, different, different type of jobs, different different type of people, male, female,

1:21:06

et cetera, et cetera, and whatnot. There might be thousands of policy documents, correct or not?

1:21:11

Right? So, at Microsoft. So, at Microsoft.

1:21:12

Microsoft everyone, we have a support agent, a chat support agent, which I think the name is,

1:21:18

I think, ask HR. The portal name is ask HR. It means that if you want to ask anything from the

1:21:24

HR, you can go to that chatbot and you can ask your query. So based on your information, based on your

1:21:30

prompt, it will try to fetch the answer. Make sense, everyone? It will try to retrieve the document

1:21:35

based on your name, based on your country, based on the type of profile you are in. For example,

1:21:42

if I'm a software engineer, I might have different policies. If you are a different,

1:21:46

if you're from different domain, if you're working in different team, different country,

1:21:51

different domain, then you might have different set of policies. Agree or not?

1:21:56

Agree or not? Correct or not, everyone. Now what I can do is, I can go to that chat support agent,

1:22:01

and let's say if I ask a question in the Microsoft chatbot agent, that let's say, if I ask any

1:22:09

question related to my leaves, right? That, hey, hey,

1:22:12

ask catch-off, please tell me the number of leaves that I have and how many leaves, let's say,

1:22:18

I can transfer to next year. Let's see if I ask this question. So can I say that even that chat support

1:22:25

agent will have to retrieve the policy documents? It will have to retrieve the policy documents which

1:22:31

talks about leaves, right? Then it will also have to fetch. Now, there might be hundreds of documents

1:22:37

which talks about leaves, right? But if I'm working in India, can I said,

1:22:42

Indian leave policy might be different from US, might be different from Canada, might be different

1:22:46

from China, etc, etc. So it will have to fetch based on my location. Let's say it will fetch

1:22:50

Indian leave policy and the document says something, let's say an employee in India gets total

1:22:56

20 leaves and they can carry forward up to 12 leaves to the next year. Something like that. This is

1:23:01

the document that we retrieve. Now, then it gives me the answer, but it does not give me the answer

1:23:07

as it is. It will have to fabricate the answer. It will have to sugar.

1:23:12

quote the answer that, okay, as per the policy document, now everyone tell me, a lot of times

1:23:16

you must have seen that, it will try to add the source as well. If that document can be shared

1:23:21

publicly with me, if that document is not confidential, if that document can be shared, that link can

1:23:26

be shared, then the chatbot can give you more reliable answer. And most of the times,

1:23:31

everyone, if I'm giving you some information, and if I give you some source, that, okay, I am taking

1:23:36

this information from this source, don't you think I will sound more reliable, more confident, more

1:23:41

trustworthy, correct? Because I'm giving you the source, right? That's why everyone,

1:23:46

the chatbot agent will tell you that, okay, as per this policy, there is a link. The leaf policy

1:23:51

says that you get 20 leaves per year and you can carry forward up to 12 leaves to the next year.

1:23:57

This is how the rag system works. Are you guys getting this point? This is how, this is what grounding

1:24:03

means that it is not trying to hallucinate. It is not trying to give you some unreliable answer.

1:24:10

It is trying to be as reliable as possible because it is giving you the source as well.

1:24:15

It is telling you that as per the policy, as per Microsoft India policy, this is the information.

1:24:22

Are you guys getting the meaning of grounding here?

1:24:26

Grounding means when you're giving, when you're trying to be more reliable, when you're adding the information,

1:24:31

getting the point? Right? So what grounding does?

1:24:35

Guys, if your application is more grounded, can I say it reduces hallucination?

1:24:40

It reduces hallucinations. Tell me how no? Correct?

1:24:49

More reliable answers. More reliable, accurate? More reliable, accurate and trustworthy answer, because it is adding source.

1:25:07

Because everyone, most of the times what happens, right?

1:25:14

If you make any mistake, right?

1:25:16

And let's say if you are, let's say if you go to Amazon and you say that, okay, this is the product

1:25:20

I want to return and please give me the refund.

1:25:22

And they say that, okay, refund is not eligible for this particular item.

1:25:27

Then the only thing, even then the first thing that you ask is that where it is written, correct?

1:25:31

Is this mentioned somewhere?

1:25:33

Right? Was it told to me at the time of purchasing this?

1:25:37

Right?

1:25:37

If you buy and if you go to some shop and buy something, and then if you want to return that

1:25:43

particular thing, they say that, okay, it is not returnable. Don't you think you ask this first

1:25:47

question that was why this was not told to me at the time of buying the item? Correct, everyone?

1:25:52

because if they tell you with the source that, okay, if they write in their shop that, okay,

1:25:58

this item cannot be returned, then it is more trustworthy. You will not cross-question that.

1:26:03

Are you guys getting this point?

1:26:07

Right? And grounding also makes, makes easier, makes it easier to get it easier to get the source of the information.

1:26:37

Right? Okay. So if this is clear, everyone, we can move to the next part now.

1:26:46

Everyone clear with this? Should we move to the next part?

1:26:53

Okay. Now everyone, let's see, rag flow. How does a rag application works? What are the different

1:26:59

steps involved in a rag flow? Okay. The basic rag flow, everyone, is you get a query.

1:27:07

Okay. You get a query. For example, the example that I give you, if you are using

1:27:14

chat support agent of Microsoft, you give the query that, okay, tell me the leave policy, or how many

1:27:20

leaves I can transfer to next year. Something like that. Now, if you give the query, can I say that

1:27:26

the rag application should convert this into embeddings? Convert.

1:27:37

the query into vector embedding into embedding, folks, yes or no? Convert the query

1:27:50

into vector embedding. No. Folks, any doubt in this? Everyone clear, yes or no?

1:28:01

Then based on this vector embedding, you perform similarity search. Now, okay, similarity

1:28:07

search you will perform with what?

1:28:10

Guys, don't you think before you are actually getting the query, we are assuming that you have

1:28:14

already stored all the documents in the vector database already, after converting them into

1:28:20

embeddings. Correct? So we can say that. Let's say there is one assumption. Assumption is what? We have

1:28:29

already stored.

1:28:37

data in the form of embeddings. We have already stored data in the form of embeddings in the form of embeddings.

1:29:07

query. You convert the query into embedding. Performs similarity search. Similarity search

1:29:12

means try to find the nearest vector, maybe top three, top five vectors. And then everyone, from

1:29:18

those vectors, you will get the corresponding vector. You will get the corresponding documents. And once

1:29:23

you get the corresponding documents, what you're going to do? Provide the closest documents or

1:29:32

provide the context to the LLM. The documents to the LLM. The documents to the LM. Context.

1:29:37

to LLM. LLM will generate the answer. Generate and return the response.

1:29:50

This is a very simple example of a very, very basic rag pipeline, rag flow. How does everything

1:29:59

works one by one? Is that point clear to all of you?

1:30:07

Slightly different anagraph, we'll talk about that as well in the upcoming classes, okay?

1:30:14

Okay?

1:30:19

Okay. Perfect. Now let's compare just few things everyone. Before we go actually into the details of,

1:30:28

let's say everyone you have, let's try to write this in this way. I will give you the question. You'll have to tell me how

1:30:37

does that work in both of these type of applications? For example, you have LLM only application

1:30:43

and you have Rag application. Makes sense everyone? There is a LLM only application and let's say

1:30:54

there is a Rack based application. What is going to be the difference between them, by the way?

1:31:00

If there is an application with only LM and there is a rag based application.

1:31:07

What is going to be the difference between them?

1:31:12

Rag-based LLM will have some external source of information, right?

1:31:18

Rag will have some external source of information.

1:31:20

It can be internet, it can be vector database, it can be something else also.

1:31:24

Makes sense?

1:31:25

Absolutely divya, absolutely correct.

1:31:27

All of you can only have static data.

1:31:29

Very good. All of you are correct.

1:31:30

Limited hallucinations, very good.

1:31:32

Now if I ask you, I will give you some questions and you will have to tell me, right?

1:31:35

The first question, let's say something like this.

1:31:40

What is the knowledge source source for LLM based application?

1:32:01

It is only going to be pre-trained information, right?

1:32:05

Only pre-trained memory, right?

1:32:10

Only pre-trained memory.

1:32:26

Then in Rag everyone, Kammas is that you will have pre-trained memory plus external source.

1:32:40

Correct everyone?

1:32:42

Okay?

1:32:44

Then everyone's second question.

1:32:50

How much both of these applications will have access to

1:32:58

latest information in the world?

1:33:00

Will LLM have all the access to the latest information in the world?

1:33:05

Usually no.

1:33:07

Generally not.

1:33:09

Usually not.

1:33:10

usually no.

1:33:11

Right?

1:33:12

And in RAG, can you have latest information?

1:33:15

Yes.

1:33:16

If everyone, if you keep on updating your knowledge base, right?

1:33:20

If you keep on updating your knowledge source, external source.

1:33:23

What if your external source is internet?

1:33:26

If your external source is internet, it means that your application will have internally all the

1:33:31

access to the latest information of the word, everything in the world.

1:33:34

Correct or not?

1:33:39

Right?

1:33:40

access to private information.

1:33:42

Access to private information.

1:33:44

Do you think that LLM only application will have access to private information?

1:34:02

No.

1:34:03

Usually, no.

1:34:04

Not usually, actually no only.

1:34:06

Correct?

1:34:08

Rack based, can they have?

1:34:09

Can they have?

1:34:10

Yes, they can have.

1:34:11

Okay?

1:34:12

So does this internet access tool in Clod, charge, GPD, basically a rag workflow?

1:34:17

Yes.

1:34:18

Right?

1:34:19

Can be considered like a rag application.

1:34:21

Can be considered like a rag workflow.

1:34:23

Okay?

1:34:24

Yes.

1:34:25

Next question.

1:34:27

What about hallucination risk?

1:34:30

What about risk of hallucination?

1:34:34

What about risk of hallucination?

1:34:36

What is the risk of hallucination in LLM only application?

1:34:39

High. There is a high risk. Correct or not everyone? High risk, right? What is the risk of hallucination

1:34:52

in a rag-based application? Very low. Guys, in rag-based application also, can hallucination happen? In a rag-based application also, can hallucination happen? Yes. It can happen, right? If that

1:35:09

information is not available. Absolutely correct. Very good. The information that user is looking for, if that information is unfortunately not available in your vector database, obviously then your LLN will try to again try to invent the answer. Okay?

1:35:25

So these are the few differences between these different type of applications. I hope this makes sense to all of you. This table is clear to all of you.

1:35:39

Okay, okay? Now let's talk about everyone. The next topic, which is how do we integrate vector database with RAG? Let's connect RAG with vector database, RAG plus vector DB. Okay? I think by this time, if everyone clear with the

1:36:09

of vector database in rag application? Yes, because all the rag-based applications, rag-based applications, rag-based applications, to store,

1:36:39

and retrieve information. Correct, everyone? Right, everyone? But everyone, when you retrieve the information, I think we have already talked about this particular thing that can we do exact search, exact match, or we need to perform, or we need to perform.

1:37:09

some kind of similarity search.

1:37:15

This is generally not followed. Similarity search is more followed. But if you remember the last

1:37:24

class discussion, don't you think everyone, if you want better answers, more accurate answers, sometimes you

1:37:30

combine both. Remember that? Sometimes you combine both. That, for example, if you want the documents for

1:37:39

policy, particular use case, let's say, return policy. Or for example, let's say

1:37:43

the Microsoft example that we took, let's say you want the documents which are related to leaves.

1:37:48

Now, out of thousands of documents, first what you can do is you can filter out the documents

1:37:52

based on the category. Let's say leave policy. Correct, everyone? So out of thousands of documents,

1:37:58

you might neglect. Based on the filtering logic, you might be able to neglect or remove

1:38:04

99% of the documents. Correct. Absolutely correct. Based on the metadata, you might.

1:38:09

you can perform some exact search, not 100% exact search, but based on the metadata,

1:38:13

you can perform some exact match, exact search, so that you will be able to neglect a lot of unnecessary

1:38:19

search. Then once you have the set of information based on the metadata filtering, then you can

1:38:26

perform similarity search. That out of these 100 documents after filtering, which is the most

1:38:32

relevant document for our use case. Is that point clear to all of you? Yes or no.

1:38:39

Okay. Then everyone, I think you can see that similarity search and this, we can say

1:38:48

that just one note here that modern applications, modern AI applications, uses combination of

1:39:09

combination of exact match and similarity search. Modern AI applications uses combination match and similarity search.

1:39:39

Correct, everyone?

1:39:41

Okay, now everyone, everyone, do we need to discuss similarity search once again?

1:39:54

That vector search or similarity search converts text into numerical representations or vector embeddings,

1:40:00

then vector embeddings captures the semantic meaning, right?

1:40:04

In fact, let me copy this thing in the notes instead of, because this is something, a small

1:40:09

part which is actually repetitive, right? Which we have already seen.

1:40:13

Why it is not getting copied? It is not getting pasted actually.

1:40:32

Okay, no worries. Let me try to read that out.

1:40:39

Yeah, nobody's. So, just let me know if you get any doubt in this particular

1:40:45

discussion, that vector search converts the text or the data or the query into numerical representations.

1:40:52

These are called as embeddings. These embeddings captures the semantic meaning of the sentence.

1:40:57

Then we compare these embeddings of the user queries, basically the user query embeddings,

1:41:02

and the embeddings of the stored documents to find the nearest search, to find the nearest search, to find the

1:41:09

nearest documents which are matching with the user embedding or the user query embedding.

1:41:13

Makes sense, everyone?

1:41:16

Correct?

1:41:18

Right?

1:41:19

Then everyone, everyone clear with this, right?

1:41:21

That what happens in similarity search?

1:41:24

We have talked about this multiple times, right?

1:41:27

Now everyone comes that why vector search is useful?

1:41:30

Because it captures the semantic meaning.

1:41:33

And I think we have talked about n number of times that why semantic search is important.

1:41:37

Why can't, in the AI applications, we can't.

1:41:39

search based on exact match because we need to capture the meaning.

1:41:43

No user in the world can give you exact word to word sentence every time.

1:41:47

So instead of relying on exact search, exact sentences, exact words, right, exact, you can say that

1:41:55

exact meaning, you need to work on the semantics. Is that point clear to all of you?

1:42:09

Okay, now everyone, let's talk about that, how the vector search also works.

1:42:16

Now everyone, let's say you have documents.

1:42:22

Let's say policy documents.

1:42:24

Now we are talking about that how you are going to store these policy documents into, how you

1:42:31

are going to store these policy documents into vector database.

1:42:34

Just one thing everyone, let me just check one thing, embeddings, we talked about

1:42:39

embeddings. Yes. Okay. Then in the next class, we talked about introduction to

1:42:45

vector databases. Perfect. Okay. And then we saw the implementation of implementing the vector

1:42:54

databases. Perfect. And then here we are talking about the next class, which is rare. Okay.

1:43:00

So, guys, you have documents. Now tell me everyone, we need to store these documents into vector databases,

1:43:06

into some database. Can we store these documents?

1:43:09

as it is into the vector database? Can we store these documents as it is, as a PDF file,

1:43:16

as a text file, etc? In the vector database, no. You can do that in some type of database,

1:43:21

but don't you think even if you store the entire document as it is without converting into embedding,

1:43:27

don't you think search will be very complex? Because one document can be very big, and there can be

1:43:33

thousands of documents you might have. You might have thousands of such documents. So first, what

1:43:38

everyone, what happens everyone is we need to convert the document into embeddings.

1:43:42

But tell me everyone, if you convert every document into embeddings and you know what embeddings are,

1:43:48

embeddings are nothing but vectors, list of numbers. That we can use some model to convert any

1:43:54

sentence, any text into embeddings, a list of numbers or a vector of numbers. But tell me everyone,

1:44:00

if a document contains thousands of pages, don't you think it might be very unoptimized to convert

1:44:07

entire document into one embedding. To convert entire document into embedding in one

1:44:15

shot. Don't think it might be slightly unoptimant, because document is very big, right? For example,

1:44:22

everyone, if there is a book, this book has thousands of pages. Now, if there is no

1:44:27

bifurification in the book, there is no page number, let's say there is no paragraphs, there are no

1:44:32

topics, there are no chapters, right? Don't you think it will be very difficult for you to read that

1:44:37

book, right? There are thousands of pages in the book. There is no bifurcation. There is no

1:44:42

topic. There is no paragraph. There is no segregation. There is no chapter. How will you read

1:44:47

that book? Similarly, everyone, if you store the entire document as one embedding, it might not

1:44:53

be very optimized way. So what happens everyone is, first, your system will divide or split the document

1:45:01

into chunks. Split into chunks. Now, guys, it is completely optional.

1:45:07

step, right? It is not a mandatory step. But if you split the document into small, small

1:45:11

chunks, just in the same way, if you have a book of thousands of pages, you don't have only

1:45:16

one section in the book. You divide that book into multiple sections, multiple chapters.

1:45:20

On an average, let's say, there are 1,000 pages in the book. Every chapter will have approximately

1:45:26

20 pages. So there will be total 50 chapters. Makes sense, everyone? Now it will be very easy

1:45:30

for you to understand that, okay, every day I will read one chapter. Make sense? So, you divide the

1:45:37

document into multiple small, small chunks. In very simple way, what you can do is, let's say

1:45:42

there is a document with thousands of pages. You can say that, okay, I will have each chunk

1:45:47

as thousand words. Every chunk will have thousand words. This is the logic in which I'm dividing

1:45:53

the document. Obviously, there are multiple other logics as well. We will not discuss all those logics in

1:45:59

detail. Those are different topics altogether. But I hope you understand the logic. The only logic

1:46:04

that we need to understand is that storing the entire document at one place, and if you convert

1:46:10

that into one embedding, it might not be very optimized approach. So what do you do? You divide that

1:46:15

document into small, small chunks, depending on some logic, and then you create the embeddings of each

1:46:20

chunks. Do we not convert every token into a distinct embedding? That will come later, right? So first

1:46:26

you do what? You have a lot of lines, complete document. You have created small parts. You can say that, you have

1:46:33

divided this document into chunks, chapter, topic, let's say chunk one, chunk two,

1:46:39

chapter two, chapter two, chapter three and so on. Now you go to each and every chunk,

1:46:43

then you create embeddings. And while creating embeddings, you create tokens, right? You can say

1:46:48

that. Third step is create embeddings of each chunk. Make sense, Chirac? So while you will

1:46:56

create, while you create the embeddings, then the topic of, then the idea of tokenization comes into

1:47:02

picture. After creating embeddings, everyone, you store these embeddings into vector database.

1:47:08

Store in vector database. After vector database, everyone, you get the user query. Again, convert

1:47:21

embeddings, create embeddings of user query. Then perform similarity search. After similarity search,

1:47:32

everyone, you will get some chunks which are matching with the user query. Top three chunks,

1:47:37

top five chunks, top 10 chunks. Correct or not? Correct? Then you retrieve those chunks,

1:47:44

which chunks, the chunks which are matching with the user query? Right? Retrieve the similar

1:47:52

chunks. And after retrieving the chunks, everyone, you pass to LLM. Pass to LLM.

1:48:02

Is that point clear to all of you? This is how the entire flow works. And using these chunks, you generate the answer and you return the answer.

1:48:32

One question which I might have missed, how to determine we need to look into LM or we need to look into vector database.

1:48:38

So generally what happens is your LLMs are smart enough, right?

1:48:42

Like, what you can do is you can have, first of all, your LLM can tell you that, do we have that information?

1:48:48

Do I not have that information? Or if you're building a chatbot, a chatbot kind of thing, then if you are getting, you can have some kind of first layer that can decide the database to call.

1:49:00

They can decide that we need to call the vector database.

1:49:02

If you're getting any query related to refund, return, policies, etc, etc, etc, you can have some bracket that, okay, if we are getting some queries like this, then we will go to vector data.

1:49:13

Make sense? We'll see that. We'll see that in the implementation in the next class, in the next to next class.

1:49:20

Okay, how many if you're clear till this point of night?

1:49:30

Now everyone, after this.

1:49:32

point, I have given a very detailed example. For example, we took the example of Microsoft chatbot in the class.

1:49:40

Similar to that, very, very similar, slightly different example I have added in the notes. That is a very

1:49:44

detailed example. Please go through that example after the class, maybe today or tomorrow. Then you'll get

1:49:50

very good understanding even further. Is it more optimized to retrieve relevant information for every query

1:49:55

or is it better if we let the LM decide? It is better if we get the query, if we get, if we get,

1:50:02

we retrieve for every query, right? Because it is okay, because the vector databases are there

1:50:07

in the system, right? If you are having a vector database, then it is better to use it. The reason

1:50:12

is because if you are getting an answer from vector database, it is always going to be more reliable,

1:50:17

more trustworthy. It is going to give you more accurate answer. It is not going to hallucinate.

1:50:22

Okay, let me actually just walk you through the example. The question, the example that I've added

1:50:27

is enterprise knowledge assistant, right? So for example, everyone, let's say,

1:50:32

Enterprise means any company like Microsoft, if you have a chatbot for them, there might

1:50:36

be a lot of documents. Now, how will you use these documents and how will you build a rag application

1:50:41

based on this? I have added that example. Very, very similar what we took in the class.

1:50:46

Right? So we don't have to write that in the notes in the class right now. I have already added that

1:50:51

in the notes. Please go through that. Everyone clear till this point of time. And then I think,

1:50:57

yeah. Now coming to the last point for today's class, everyone. And hopefully,

1:51:02

we will be able to end the class before time today. The last part. That how RAG is used

1:51:11

in agentic systems. Because everyone, at the end of the day, we are in the course of agentic

1:51:17

AI. So we should always, we should only learn the things. We should try to learn the things

1:51:22

which are related to agentic AI in some or other way. Now the point is that we are learning

1:51:28

rag. But is rag really relevant for agentic AI applications? What do you think about it?

1:51:35

If you're building some agentic AI application, do you think that rag is required there?

1:51:42

What do you think about it?

1:51:47

100% I would say. In fact, agentic AI is one of the best way, is one of the most, I would say,

1:51:55

most crucial part where rags should be used.

1:51:58

Because if you don't use RAD, you never know when your LLM will start hallucination.

1:52:04

Correct? For example, everyone, at Microsoft, this enterprise chatbot only, Microsoft chatbot

1:52:10

only, now if you're making it in an agentic AI way that you can not only get the information,

1:52:15

but you can take actions also. For example, apply the leaves, transfer the leaves, cancel the leave,

1:52:21

apply for reimbursement, cancel the reimbursement, etc., etc. It means that you are converting

1:52:26

that simple chatbot into an agent.

1:52:28

AI application. It means that actions will come later. Agents will come later.

1:52:33

Agent are the one who takes the action. Correct? First they think, then they take the actions.

1:52:39

Now everyone tell me if the thinking part, that is taken care by the vector database or the rag,

1:52:45

if the thinking part itself is wrong, can you expect your actions to be accurate?

1:52:52

Tell me, if you're thinking in the wrong direction, if you are hallucinating even before taking the actions,

1:52:58

How can we expect our actions to be more accurate? Are you guys getting what I'm,

1:53:03

what example we are discussing? That agents are made to take decisions. But before taking the

1:53:10

decisions, they need to think, they need to generate the answer, they need to think what to do,

1:53:15

what agent to call, what actions to take. Now, how to decide what actions to take?

1:53:20

Using RAG. If you are using RAG, you will be able to take better decisions.

1:53:24

You will be able to take more reliable, more trustworthy, more accurate decisions.

1:53:28

Is that point clear to all of you? Yes or no? So is RAG required in agentic AI applications?

1:53:35

100% yes. Is everyone clear till this point of time? Yes or no?

1:53:41

Folks, yes or no?

1:53:58

agentic flow using rag. Agentic flow with, or let's say, let's talk about first,

1:54:10

agentic flow, right? So what happens in agentic flow? There is some goal. Correct everyone? You

1:54:18

decide the goal. Then agent, agent, agent gets the information.

1:54:28

Or you can say that. First, what was the loop for agent? Perceive, reason and act, right? Perceive. Remember that? Then reason and act. Typically, these are the three steps of any agent. Right? So first, everyone, agent perceives the information, perceive the goal. Agent.

1:54:58

perceives. Now, everyone, for reasoning, don't you think agent needs the information?

1:55:06

For thinking about the action, what action to decide, what action to take, we need the information.

1:55:14

Now, guys, if we are just relying on LLM to take the, to get the information, it can hallucinate.

1:55:19

So, guys, to get the information, to decide, you need LLM as well as rag. Or LLM as well as well as

1:55:28

external source of information for more accurate decisions, external source. Is that

1:55:36

concrete to all of you? Right? And finally everyone, you take the decision, you take the action.

1:55:43

So if you see, perceive, reason and app. But if you use external sources and LN together

1:55:53

to take the information, your accuracy, your decisions will be more accurate.

1:55:58

Folks, everyone clear? Yes or no? Okay. Now, tell me everyone, in any AI application, whether it is an agentic AI application or a simple generative AI application, is retrieval quality very important. I think this is one subtopic that we have to touch. We already know that, right? Nobody is going to say that, okay, retrieval quality is not important. Anybody, anybody is in the favor of that retrieval quality is not very important.

1:56:28

No, right? Retrieval quality is definitely very, very important. So we need to make sure that whatever

1:56:34

information that we are retrieving, that should be reliable, that should be accurate, and that should

1:56:40

be, you can say that trustworthy, with sources. If you can add more sources to the information, definitely

1:56:46

it is going to add more trust from the user. That's it for today's class. How many few enjoyed the

1:56:51

class? I think in the last class I took 10, 15 minutes more, right? I think the last class we ended at

1:56:58

around 10, 15, 10, 20. So now I think we have ended the class. We are done with the class

1:57:03

10 minutes earlier today. Okay. Perfect. So guys, now, we have got the information about RAG. Now,

1:57:09

in the upcoming classes, we will also see the implementation of Rack systems. Okay. That's it for today's

1:57:14

class, everyone. Now we are going to have the quiz for today's class and then we will end the class.

1:57:19

Okay? Just give me a second, everyone.

1:57:21

First, let's mark whether we have covered all the topics or not. Okay? Can everyone see my screen?

1:57:34

Yeah. So how LLM generates the response? We know that. We have covered that. We have covered that.

1:57:51

limitations of LLM, limited data, static information, hallucination, etc. Then we talked

1:57:58

about problem of hallucination, why it is a bad thing. What about grounded systems? What is the

1:58:04

meaning of grounding? Introduction to RAC. Yes, we have covered that. Then understand the concept

1:58:11

of grounding in RAC, that how does RAC solve the problem of grounding? In fact, how does RAC gives

1:58:17

us the grounding approach? High-level flow. We know that.

1:58:21

What are the different steps involved?

1:58:24

Then we saw the table for LLM versus Rag-based responses.

1:58:28

Connect Ragt to Vector Databases. We understand how we are going to have the vector databases

1:58:34

which are going to connect with Rag applications in order to give better responses.

1:58:40

Here, we are not talking about the implementation, only the conceptual part.

1:58:43

Implementation we will see in the upcoming class.

1:58:45

Then real world use case of Microsoft chatbot agent.

1:58:49

Understand the role of Rag in agent.

1:58:51

systems, we just discussed that. And why retrieval quality is important? Because everything

1:58:56

is dependent on retrieval quality. If your retrieval quality is not good, we cannot expect the agents

1:59:02

to behave in the right way. Let's say for example, if you're building an agent to, let's say,

1:59:08

for example, let's say to book flights. And if you're getting the, if you're retrieving the wrong

1:59:12

information about the flights, you cannot expect the flight booking to be correct. As simple as

1:59:17

that. Okay. That's it. Now we are going to have the quiz everyone.

1:59:21

Okay, I got logged out from the Menti meter.

1:59:24

Folks, just give me a second. Let me log into Menti meter.

1:59:32

Where are the credentials?

1:59:51

Folks, just give me a second.

2:0:02

Yeah, got it. I think we have time today.

2:0:21

Folks, all of you, the quiz.

2:0:51

Yeah. So guys, here is the quiz. Please join via the QR code. Or you can join via the link

2:1:00

or you can go to MentiMeter.com and enter this code. Any one of the way should work. So please

2:1:06

join the quiz. We will have simple five questions and then we will end the class. That's it.

2:1:21

Just a few more seconds, then we'll start.

2:1:51

Okay. So guys, here is the first question. What is Hallucination in

2:2:21

Simple, guys, see, all of you guys, see, all of you got it right?

2:2:51

What does retrieval part in RAG do?

2:3:21

All of you got it right? Very good, very good, 100%.

2:3:31

Third question.

2:3:51

different from an LLM based answer, LM only answer.

2:4:21

Based, it is always going to be based on the context. Okay? Perfect.

2:4:28

Fourth question.

2:4:51

Why can rag reduce hallucinations?

2:4:56

It gives the context.

2:5:09

Very good. All of you got it right.

2:5:12

Very good.

2:5:13

And here we go, everyone.

2:5:17

The last question for today's class, which is.

2:5:20

Like this. What is a vector database mainly used for in RAD?

2:5:50

Storing and searching embeddings efficiently. That's it.

2:6:04

So let's see the final leaderboard even.

2:6:06

Most of the questions were answered by all of you in the right and correctly.

2:6:11

So it is going to be very close.

2:6:13

Yeah.

2:6:14

If you see everyone, first four, five people, in fact, five, six people, everyone, everyone is at 48.

2:6:20

800 something. They are very close. Right? So who is the Latin? Who is this guy?

2:6:27

Pilla. Okay. Cool. Thank you so much everyone. Have a good day. That's it for today's

2:6:32

today. Now we are going to launch the feedback poll. Just like all of you participated in the quiz,

2:6:37

most of you, please participate in the feedback poll as well with the high energy. Then we can end the class.

2:6:43

Thank you. Have a good day. Take care. Good night and take care.

2:6:46

And see you in the next class now.

2:6:48

Till then, take care.

2:6:49

Take care. Bye-bye. See you.

2:6:51

Have a good day, everyone. Good night.

2:6:53

Done. Thank you. Thank you. Thank you, everyone. Take care. Bye-bye. We can end the class from you.

2:7:09

Yes, sir. Thank you, sir. Thank you, everyone.

2:7:19

