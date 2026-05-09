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

Thank you.

13:06

Thank you.

13:36

Thank you.

14:06

Thank you.

14:36

Hi, everyone.

14:40

Hi, everyone, very good evening.

14:42

Am I audible to all of you?

14:44

Pratius, can you please make me host or co-host?

15:04

I'm not able to send a message?

15:05

I'm not able to send message to everyone.

15:08

Yeah, thank you.

15:11

Okay, I think people are still joining in.

15:13

The strength is very less.

15:15

So let's wait for maybe two to three more minutes,

15:18

and then we'll get started.

15:20

Strength is almost half of even less than

15:24

less than half of the usual strength.

15:26

Let's wait for two more minutes, then we'll start.

15:35

Thank you.

16:05

Thank you.

16:35

Thank you.

17:05

Thank you.

17:35

Thank you

18:05

Thank you

18:35

Thank you

19:05

Thank you

19:35

Thank you

20:05

Hi,

20:14

very good evening.

20:15

folks,

20:16

folks,

20:19

am I audible to all of you all of you

20:20

all of you?

20:22

Hi, everyone.

20:24

Am I audible to all of you?

20:27

Okay, great.

20:28

Good evening.

20:29

Welcome to the session.

20:32

Maybe because of Saturday, the strength is unfortunately still

20:35

bit on the lower side, but no worries. Let's get started. Okay. Now everyone, in the last class, if you remember, we discussed about the retrieval strategies. Remember, we discussed about the retrieval strategies. Can you just help me in a quick recall of what all the retrieval strategies did we discuss in the last class? Can you just help me recall what all the retrieval strategies did we discuss in the last class?

21:05

Similarity search?

21:12

Just give me a second.

21:35

Yes, the first one was similarity search, which is in fact the most common one. But in similarity search, everyone, there was a bit of limitation of what was a limitation of similarity search, that it will always sometimes it can also lead to redundant outputs, right?

21:51

Because every time it will keep on giving you the top five or top 10 nearest vectors, right? And after some point of time, you will realize that, okay, it has started giving you redundant answers, repetitive answers.

22:05

That's why everyone, we have another approach. We discussed another approach, which was MMR.

22:09

Maximal marginal relevance, right? In this, we make some changes in the strategy, how we pick up the nearest vectors, and we add some more diversity.

22:21

Okay? Then everyone, the third one is the hybrid approach, right? And hybrid approach made, what do we do? We have some kind of combination of similarity search and exact match, right? So if you have, if you find out the similarity,

22:35

you find out the mix off, if you make the, if you take both of these things into

22:40

into picture, that is similarity as well as well as keyword search, that makes your hybrid search.

22:46

Is that point cleared all of you? Is that point clear to all of you? Is that point clear to all

22:51

of you? Okay. Now everyone, we will start with today's discussion now. In the, in the previous

22:57

class, we came across few things. For example, let's say, we discussed about one thing,

23:02

which is query reformulation, right? Remember that? Reformulate unclear queries. Sometimes

23:09

queries can be unclear. We might have to reformulate them. We might have to expand those queries. So

23:16

that concept is query expansion and reformulation. We will talk about that. Then everyone, we used

23:23

this term called a citations. What are these citations? Let's talk about them. So these are the things

23:28

that we are going to talk about in today's class, right? So first everyone we are going to talk about is,

23:32

query expansion and reformulation.

23:42

First, let's talk about query expansion. Now, what is the meaning of query expansion? Any guesses?

23:51

What is the meaning of query expansion? Any guesses? Expanding the query, but

24:02

Sometimes everyone, the query might be a bit unclear. If you add some extra words inside the query,

24:08

that might make it more readable, more understandable. Correct? Ever? So expansion simply means

24:15

that expanding the query.

24:32

adding extra related words to the query to the query to the query to the query.

25:02

to make it more readable and more understandable. Make sense? This is a simple meaning of query

25:07

expansion. On the other side, everyone, there is another concept called as query reformulation.

25:16

What is the meaning of query reformulation?

25:27

Query and prompter saying yes. When we say query, it means that you are giving input to the user,

25:32

to the LLM or prompt to the LLM. Now, re-formulation, everyone, you see that, re-formulate.

25:40

Rewrite the query into more clear form. So it means that, everyone, you are not only adding extra

25:47

words, rather you are writing the complete query from scratch, rewriting the complete query. Rewriting,

26:02

to make it more clear. Is that point clear to all of you? To make it more clear, right?

26:11

What can be the example for this, everyone? Let's say, let's say if you give a query like this,

26:17

what about the refund? What about the refund? Now, this query might not be very clear to the system,

26:26

to the AI application. So you can reformulate the query into that the user is asking about, like,

26:32

what is the process of refund and the timelines, something like this, right? So here even

26:38

you are not very clear that are you talking about the refund process? Are you talking about the

26:44

refund timeline? Or are you checking about the refund status? It means that whether you have already

26:49

raised the refund request and you are trying to check the status for that. Do you see that? It is

26:55

a bit unclear query, a bit ambiguous query? Correct? Here it is not getting, you're not getting proper idea.

27:02

what you are talking about about the refund, right? Are you trying to check the status of the refund?

27:06

Are you trying to check the timelines of the refund and whatnot? Right? So you can rewrite the query.

27:12

Right? Now, can we use expansion and reformulation together?

27:25

Typically, yes. Okay? We can. Can we use, now one question is, can we use, can we use, can we use,

27:32

LLM to expand the query and reformulate the query? Can LLM help here?

27:41

Answer is yes. Right? So what we can do everyone? We can, in fact, we can do this without the LLM also.

27:47

But if you want to use LLM also for extension or reformulation, you can do that also. Okay? Now let's

27:53

move to the next topic, everyone, which is handling multi-term conversations. Okay, these two are very simple topics.

27:59

Let's move to the next topic, which is multi-term conversations. Any guesses? What about, any

28:07

guesses about, any guesses about multi-term conversations?

28:29

User asking follow-up questions? Absolutely correct. Now, because how many times

28:37

you have made, you have interacted with any AI application, be it Chad GPT, be it Gemini,

28:44

be it Claude, or be it any customer support agent of any application, of any company.

28:51

How many times you have interacted with them and you just had one question in the conversation?

28:59

Only one question. That you ask the question, they gave you the answer, done.

29:04

Rarely. Correct? Rarely, it is going to happen that the conversation will only have one question.

29:10

Can I say that, conversation will have multiple follow-up questions?

29:17

Any conversation,

29:29

Any conversation generally have.

29:59

multiple follow-up questions correct so for example everyone let's say if you ask a question like

30:08

what is the what about the refund right let's say if you're having a conversation about the refund

30:13

let's say you say you say that okay maybe refund or return period what is the return period right and

30:18

then chatbot answers that okay returns are allowed within 10 days within 15 days right and then

30:24

then you say that okay what about the damaged items what if I get a damage item by when I can return that

30:29

and so on. Now, you can have multiple follow-up questions. Now, why do you think,

30:35

like, do you think that that the multi-term conversations, it means that when you have multiple

30:40

follow-up questions, these type of questions, these type of conversations may be a bit difficult

30:47

to handle from the RAG perspective. What do you think about it? Do you think about this, that maybe maybe

30:59

try to understand, try to think these multi-turn conversations, when you have multiple follow-up

31:06

questions, these type of questions, these type of conversations can be a bit difficult from the

31:13

the Rack perspective, right? So we can say that everyone, that obviously follow-up questions.

31:29

depend on earlier context. Yes, everyone, like all of you understand that these

31:39

conversations are going to be difficult from the RAC perspective. Because everyone, see, if

31:45

you ask one question, right, if you ask one question, you will get the answer. Let's say you are

31:50

getting this answer, you are getting this answer from Rack. Now you ask another follow-up question.

31:54

Now to get the answer of this question, you will have to, like, the answer, the answer, you will have to, like,

31:59

answer will be dependent on the previous, the answer of the second question will be dependent

32:03

on the answer of the previous question, as well as you might have to check with Rag again. Again,

32:09

you get the answer. Again, the third follow-up question, it will be dependent on the previous answer,

32:15

again, even the previous answer, and then you have to check with the Rack. Getting the point. So

32:19

all of these conversations, all of these questions are not independent. They are dependent

32:24

on the previous answers and the previous questions. So you will have to keep a track of

32:29

of them, what answer did you give, what document did you fetch, what chunk did you

32:34

follow, etc, et cetera, et cetera. And again, you'll have to check with Rags. Are you guys getting

32:38

this point? Right? So all of you understand this point that, see, in the simple rag, in the last

32:45

to last class, when we talked about basic Rag pipeline, we saw that, you get the query, you get the

32:51

question. What do we do? We convert this question into embeddings, embeddings, right? We check the

32:58

similar embeddings and then we return the answer. Now, in the simple Rag pipeline, do we even

33:04

consider that this query is already dependent upon the previous answer that we gave or the previous

33:12

question that we got? Did we even consider this thing? Did we even consider this thing in the

33:17

simple Rag application? Answer is no. We did not even talk about it, right? We, in the simple

33:23

rag application, we consider every question or every query as an independent query.

33:29

Remember that? Yes, or no, everyone? In Simple Rack, we did not consider that. But in advanced

33:36

rag, in advanced applications, everyone, don't you think for every query, you need to consider

33:41

the conversation history as well? Not just the current query, right? So we can say that,

33:48

advanced rag, advanced drag, let me write it down, then it will make more sense,

33:59

advanced rag, retrieval strategies, advanced Rack, advanced Rack, Rattrieval Strategies, Advanced Rack,

34:18

the conversation history must consider the conversation history, must consider the conversation history, not just the current query. Is this point

34:40

clear, Anjou? That you cannot consider every query as independent query. Rather,

34:48

every query, if that is coming in a conversation, you need to consider the previous conversation

34:53

history as well. What kind of answers we have given, what kind of documents we have referred,

34:57

etc, etc. Right? Right. Let's talk about everyone, different strategies to handle

35:04

multi-turn conversations.

35:10

Strategies to handle.

35:14

To handle.

35:17

multi-turn conversations.

35:34

Okay.

35:35

First, everyone is the first strategy, the simplest is, the simplest strategy is called as conversation.

35:47

Conversation aware, re-formulation.

36:03

Okay? Conversation aware, query, re-formulation.

36:10

Right? What is the meaning of that? Let me write down this. That it simply says that we should rewrite,

36:17

rewrite the users, rewrite the user's message or message, a query, whatever, rewrite the user's message,

36:40

using conversation history.

36:52

How many if you're able to understand this point?

37:00

Read the user's message into a stand-alone query using conversation history.

37:06

It means that everyone, let's see if you are having a conversation, there is a question. There is a question.

37:10

Right? Let's say you asked a question, you got the answer. You asked a question, you got the answer. You asked the question, you got the answer. Now, let's say this is the conversation which is already going on. Now, if you ask a new question here, let's say this is the new question. Now, how will you make sure that the system, when you type this new question, when you send this new question, system will be able to understand that, okay? This new question is not completely independent. Whatever answer we are going to give of this question, it is dependent on these.

37:40

previous conversation history, previous conversation messages, getting the point?

37:46

So this particular question, how will you give the answer of this question, is dependent on the previous

37:51

conversation history? How will you find out that? Now, one thing everyone that you can do is, as soon as user sends this

37:57

query, you can rewrite the query, right? So you are maintaining some part of conversation history in the

38:03

backend. So what do you can do? You can rewrite the query with the conversation history. Right? It means that when you

38:10

send this query to the system. Before sending the query to the system, you will automatically

38:15

attach the complete conversation history in this query and you are going to rewrite or reformulate

38:21

the query once again. Getting the point? Okay? For example, everyone, let's see if the user, if the user asks,

38:29

what is the return period, bot says that 15 days. And then you ask that, what about damaged items?

38:36

Now, this, what about damaged items? It is not very clear, right? If you just say what about

38:41

damaged items, are you, if you just consider this query as independent query, will you be able

38:46

to understand the context behind it? Will you be able to understand the context what about damaged

38:51

items? Answer is no. Because what about damaged items is dependent on the conversation history.

38:57

So what are you going to do? As soon as you send what about damaged items, your system should be able

39:01

to add the context from the previous history that, okay, here user is talking about.

39:06

the return period of damaged items. Is that point clear to all of you? This is one of

39:13

the most effective query. This is one of the most effective way of handling multi-turn queries.

39:20

But everyone, there is a small disadvantage here. What is the disadvantage? There is a small

39:26

problem here. What is that problem? Absolutely correct. Mukta has raised a very good point.

39:35

don't you think, everyone, if you keep on adding the conversation history to the query again and

39:40

again, don't you think it will increase the limit of context window, it will breach the context window,

39:45

it will consume more number of tokens. Obviously, the cost will also increase. Does it make

39:50

sense to all of you? The cost will increase. Okay? Let's come to the second approach everyone,

39:55

the second strategy, which is called as, let's compare, let's understand all of these strategies.

40:02

Then we'll talk about the comparison as well. That you can maintain at one.

40:05

commonplace for every user, you can maintain conversation memory. Conversation

40:16

memory. So guys, have you seen that generally? Generally what happens? Let me give you

40:22

an analogy. And I'm pretty sure after that analogy, you will be able to relate on Swiggy, Zomato,

40:28

Zepto, etc. At one given point of time, how many conversations you can have active.

40:35

how many active conversations you can have at a time on most of these platforms?

40:45

Folks tell me, on most of these platforms, how many active conversations you can have at a time?

40:55

Guys, how many different chat windows you can have at a time? Only one. Have you noticed that?

41:05

At a time, you can have one chat window, right?

41:08

So what do you do? Let's say, for example, if you place an order, you go to chatbot, you go to

41:12

help center, support center, you click on that, you have a conversation.

41:17

Now, once the query, once the conversation is completed, you give the feedback.

41:23

Till that point of time, once you give the feedback or the executive ends the conversation,

41:28

that conversation is gone.

41:30

Right? So that conversation is gone now. When you reach out to them again, a new conversation. A new

41:35

will be started. Now, quite possible that in the first conversation, if the support system,

41:41

if the support, if the system is raising a ticket, and they say that, okay, please come back to us

41:46

after three days and we will check your issue internally. You can check the status after three days.

41:51

Now, what they will do? When you come back to them after three days, they will check from the database,

41:55

what issue did you raise from the memory? This is what is called as conversation memory. So what do

42:01

do they do? Depending on the context, depending on the use case.

42:04

applications can maintain the conversation memory where they can maintain the data about the

42:10

conversation. What issue did you raise? What questions did you ask? What responses did they

42:15

give, etc. So in conversation memory, everyone, what does these applications does? These

42:22

applications stores topics, topic of the conversation.

42:34

messages and answers of the previous conversations.

43:04

conversation memory? The conversation memory, example could be, for example, let's say,

43:09

what is the topic of the conversation? Sometimes everyone on some of the platforms, you must have

43:13

seen, right, that before you start the conversation, they ask you to select the topic or

43:17

the type of the query that you want to raise, return, refund, etc., etc., right? Damaged

43:24

item, wrong item, etc. Right? So they store the topic of the topic of conversation, conversation,

43:32

topic, something like this. Conversation topic, let's say you are talking about

43:48

return, right? Then they also store the product type for what type of product you have raised

43:57

the query, electronics, right?

44:02

And multiple things like this. So that everyone, now, if you ask a new question, if this

44:09

particular information is already maintained, for example, even let's say you ask a question, get

44:14

the answer. Ask a question, get the answer. So all of these things are being stored in the memory,

44:18

in this format. Now, if you ask a new question, what about the damaged items? As I gave you the

44:23

example, don't think, everyone, before giving the answer, we can check in the memory that what you

44:28

are talking about? Damaged items, you're talking about the return period of the damaged items.

44:32

right? And the product is electronics. So you can check the policies related to the return policy,

44:38

return policy of electronic items. If electronics item is damaged, what is a return policy? This is how

44:45

you can use. Is that point clear to all of you? Okay? Another way, everyone, is topic tracking.

44:57

If you see, as of now, we have seen three different strategies, conversation aware.

45:02

Maint conversation memory. And the third way is your topic tracking.

45:13

Now, what is the meaning of topic tracking? This means everyone, let me write it down first, that we delete if the user

45:32

Just a second. Return policy, refund policy, cancellation.

45:54

Okay, got it. So, actually, there are two things which are very similar to each other, I'll let you know.

46:02

So delete if the user is continuing the same topic or switching it to a new topic.

46:29

Now, what is the meaning of this? Let's see. Let's see everyone, the example for this is, let's say, if you give a question, let's say what is the refund policy? Let's say the query is, what is a refund policy?

46:50

Now, if you ask another question, let's say you got the answer for this. After that, you ask another question. What about cancellation?

46:59

What about cancellation? Now, are both of these things similar to each other?

47:15

Whether you are asking about refund policy, refund you will only get if you cancel the item or you return the item, right?

47:21

If you ask another question about what about return? Right. So return, cancellation, refund policy, they are related.

47:27

So these are same topic, right? These two conversations or these two messages belongs to

47:35

the same topic. But let's say everyone suddenly, if you ask after some time, let's say if you ask another

47:41

question and the question is something like this, I am getting some login error. Now you are, you

47:57

started asking about login error, that you are getting some error while you are trying

48:02

to log in. Are these, is this question related to the previous topic? No. So everyone, what

48:10

happens is, if the topic changes, you can probably move, you can switch the topic. And when you

48:17

switch the topic, you can maintain a new conversation memory. How? Let me give you an example. Without

48:22

example, it will not be clear. Right. So let's say everyone, let me just write it here, that same

48:27

type of topics, right? So here you will see that after this, it is a different topic

48:38

all together. Okay, it is a different topic. Now let me give you an example. Let's see if you're

48:45

talking, if you're having a conversation with e-commerce chatbot like Amazon, right? And let's say the

48:52

question that you ask is, can I return the phone after 10 days? Okay?

48:57

The question is, can we, can I return the phone after 10 days? Now, BOT says that yes.

49:03

If it is within 15 days of return window, you can return it. And then the user says that, what if it is

49:11

damaged? Getting the point? First question did you, what question did you ask the first question?

49:18

First question was, can I return the phone after 10 days? Bot says, yes, you can return if it is in the

49:24

refund window, if it is in the return window of 15 days.

49:27

So is 10 less than 15?

49:29

Answer is yes. It means you can return.

49:31

Then the user asks, what if the phone is damaged? What if it is damaged?

49:36

If the user asks, what if it is damaged, how the bot will understand that what user is

49:43

referring to? If it is damaged? Getting the point?

49:49

Getting the point? It means that everyone now, if bot is maintaining some kind of bot is tracking a topic

49:57

for this particular conversation, the topic is return, right? The topic will be assigned

50:03

to the query when you start a conversation. Correct, everyone? So at the start of the conversation,

50:08

bot will decide that, okay, in this particular query, user is talking about return policy.

50:14

So user is talking about return. And in the first message also, you will fetch the order

50:18

details, you will talk about, like you will get the order details or you will get the product details

50:23

that user is asking. So now the bot will understand that, okay, the topic of the conversation,

50:27

is return policy. Product type is, let's say, phone. Based on that, what will be able

50:34

to understand that if user is asking about what if it is damaged, it means that user is talking

50:39

about the return policy of the phone in case it is damaged. Now, from this understanding, you might

50:44

think that it is very, very similar to the memory part. Correct, everyone? It is very, very similar

50:51

to memory part. Correct? Answer is yes, it is very, very similar to memory part. But everyone, what happens

50:56

is in memory, you might maintain a lot more information, but in third approach, which is topic

51:03

tracking, you maintain slightly lesser information. In memory, you can maintain a lot of information

51:11

about the conversation, about the user, about the product and whatnot. But in the third approach,

51:16

in the topic tracking, you mostly maintain or you mostly track only the topic. Is that point clear

51:22

to all of you? Yes or no.

51:26

Okay, perfect. Now let's move to the final part, everyone. Here we will talk about that.

51:33

What are the common mistakes that we make in multi-turn conversations?

51:56

Right? Okay. What if the user switches the topic and gets back to the old topic? If it is

52:04

getting back to the old topic, then the topic is not in the tracking list as of now. So that's why

52:10

you must have seen that. Whenever you start, whenever you start asking the question, let's say the

52:15

conversation gets completed. And now you go back to the old conversation, or let's say you raise,

52:20

you start a new conversation and you've started asking about the new conversation. So what

52:23

the bot will have to do, either the manual user,

52:26

human being or the bot, they will have to go to the previous conversation completely. And that

52:32

takes time. Right? So topic tracking, memory, etc. They are for the active conversations. Make sense.

52:38

But ultimately, if you see, even if you go to Amazon chatbot or let's say Sviki chatbot, you will be

52:42

able to see the messages that you sent one year back. So ultimately, everything is going to get stored

52:47

in the database. But if you store everything inside the database, will you be able to fetch that efficiently

52:52

at the time of active conversation? No. Right. So after.

52:56

some time, once the conversation gets completed, you stop tracking that particular topic and

53:01

the complete conversation gets dumped into the database. Now, if in future the user comes back and

53:07

ask the questions about the previous conversation, generally it does not happen. If it happens,

53:11

then you'll have to go to database, fetch the older conversation, read messages, try to understand the

53:16

context. This is a relatively slower process. But this will only happen if you stop the current conversation.

53:23

If the user completes the conversation, then the topic tracking gets deleted.

53:30

Makes sense? Anjum Bashwra-Dip, same answer. Sometimes we change the topic. They start from the beginning

53:35

and given options. So that's why what happens is only topic tracking is not, is not used in production

53:42

applications. Along with topic tracking, what happens is we use memory as well. Right? Because if you just track

53:49

the topic, you will not be able to build efficient systems. Right. You need a

53:53

much more information about the conversation. That's why we use a complete memory.

53:58

Okay? Perfect. Now let's move to the next topic, everyone. That is some common mistakes that we make,

54:03

that generally people make in implementing multi-term conversations. What generally we do,

54:09

everyone, most of the systems, that they retrieve the messages, retrieve answers.

54:23

only based on recent messages. Recent messages or recent message. Do you think

54:37

that everyone, is it going to give you a very good system? Is it going to give you a very good response?

54:44

Answer is no. Sometimes we end up not maintaining complete conversation context.

54:53

not maintaining because of memory constraints. Conversations, conversation context.

55:07

For example, even if you're having a conversation with the bot and that conversation went very long,

55:13

let's say you are having a conversation and some issue is very complex, they are not able to resolve,

55:17

and you are having, you have exchanged hundreds of messages. Now, let's say the bot is maintaining a memory

55:22

in which it is maintaining the conversation context. But let's say everyone, obviously,

55:27

this memory will have some limit. Now, if you keep on having a conversation for a very long time now,

55:32

don't you think you might, let's say, the memory is full? Now, the new message, if you want to

55:38

put inside the memory, you will have to remove the older messages, right? Because of limited memory.

55:43

And because of this, everyone, if you remove the older messages, after some point of time,

55:47

you will see that, you will end up losing the context of the memory, context of the conversation.

55:52

you will not know what happened, like from where the conversation started, right?

55:58

What was the root of the conversation? Okay.

56:03

Okay. Another mistake that we make everyone, as we disperse in the first approach, that if you rewrite

56:09

the complete query, if you rewrite the complete query, by adding the complete conversation history in

56:15

the prompt, in the query, don't you think it will unnecessarily increase the prompt every time

56:19

with every query. Correct? So, if we pass, passing, entire conversation history,

56:49

This is, these are the common mistakes that we make while implementing multi-turn conversation.

56:55

Is that point clear to all of you?

56:59

Okay. Now let's talk about the next topic, everyone. Then we will go for a break and then we will

57:03

discuss further. The next topic everyone is citing and so, citation and source tracking.

57:19

This is relatively a very simple topic, right?

57:23

I think we all understand what is the meaning of citation, what is the meaning of source tracking.

57:27

So this goal as follows that in many, you can say that AI applications or rack systems,

57:33

especially if those rag applications are working for enterprise level, working for, let's say,

57:39

if people are paying for that particular, let's say if you're having a paid subscription of chat,

57:45

GPT, paid subscription of Claude, etc.

57:48

Right?

57:49

Or you are having.

57:49

some kind of application which is being used by people for research, for laws, for some kind

57:56

of, some kind of, you can say that, some kind of important work, right? It is not a very normal

58:01

work. Either people are paying you to use your application or people are using your application

58:06

for some critical use case, healthcare, laws, legal activities, etc., etc. Whenever you give

58:13

any answer, it is very important for you to make a quote that, okay,

58:19

This information, what is the source of this information?

58:22

Otherwise, that particular information will not be very much credible.

58:26

Correct, everyone, for example, if you're using chat GPD for some legal advice, for some financial advice,

58:31

for some kind of research advice, right, it gives you some answer, and you follow that blindly.

58:38

If you follow that blindly, now you are gone, right?

58:42

Now something has gone very bad.

58:44

It means that everyone now, chat GPD, now there is no point for you or there is no point for

58:49

charge GPT to claim that, okay, where this information is coming from? Correct everyone?

58:55

Right? What was the source of this information? Right? If you follow the advises given by any

59:00

AI application blindly, it can lead to harmful effects. Make sense, everyone? That's why it is very,

59:07

very important for any AI application, specifically if you are paying for it, if you are using that

59:13

for critical use cases like healthcare or legal activities, etc., etc., education, right? It's

59:19

very important for any AI application to cite the sources. This is the information that

59:24

I am getting from this particular source. If you want to read more about it, you can refer this

59:28

particular documentation. Also, even by the way, on any AI application, there is a small

59:33

disclaimer written somewhere on the screen, on chat GPT also, on Gemini also, that the information

59:38

given by GPT might not be 100% true. Please verify before using it, before following it. Have you

59:43

seen that? This disclaimer, at every place, this is written on every application, right? So,

59:49

you should always make sure that where the information is coming from, which document or chunk

59:54

we used to give the answer, right? Whether the answer can be verified. If you're claiming

59:59

something, right, the user should be able to, user should be able to verify that information, right?

1:0:06

This particular, everyone, this particular approach is called as citation, right? When you are citing

1:0:10

any particular source, right, if you are giving any answer, even where it is, use cautiously,

1:0:16

absolutely correct. Right? If you're giving, if you're getting any response,

1:0:19

on the bottom right corner of that response, there are sources mentioned, right? You must have

1:0:24

notice that, right? This particular approach is called as, this particular use case is called as citation

1:0:30

and source tracking, right? So, guys, citation improves what? Transparency, trust, credibility,

1:0:37

you can say that, explainability and whatnot, right? Okay, everyone, source tracking, everyone,

1:0:43

source tracking means each retrieved answer or each retrieved chunk, should

1:0:49

carry metadata. Again, everyone, citation may you tell the sources, source tracking is

1:0:55

slightly more granular part of this if you add more information, right? So citation may, although

1:1:01

it is, they are very, very, like, related to each other, but citation may you just give the

1:1:05

source name. Source tracking may, you might give more information that, okay, this particular

1:1:09

answer is coming from this document, this line number, this is the URL, this is the website, etc,

1:1:13

etc. But at the end of the day, both of these things are very, very similar.

1:1:19

Okay? Now, what are the different type of citations you can have? You can have multiple

1:1:24

levels of citation. First level of citation is document level citation.

1:1:29

Document level citation.

1:1:34

Document level citation. Second is everyone. Section level citation. Section level citation.

1:1:45

Section level citation.

1:1:48

Now, what are the meaning of this? Document level citations, everyone, you just refer the document.

1:1:55

Let's say according to as per this document, as per this website, right? You are having a broad level, right?

1:2:03

Now, everyone, let's say if there is a document of 1,000 pages, and you say that, okay, as per this

1:2:08

document, I am giving you this answer. Okay, it is definitely better than nothing.

1:2:14

But still, don't you think document level citation might not be very true?

1:2:18

or very good because you might have to go through the entire document to find out that.

1:2:23

Section level, everyone, you just say that, okay, as per this document, section 1.8, this is the answer.

1:2:30

So you are going a bit more specific, right?

1:2:33

Then everyone, you can do line level citation, right?

1:2:36

You can even refer the line as per this document, this section, line number 120, this is the answer.

1:2:42

Make sense, everyone?

1:2:43

You can have page level citation also.

1:2:47

Okay?

1:2:47

page level citation. You can have inline citation. You can refer the line as well.

1:2:53

I hope this makes sense to all of you, right?

1:2:57

Trying to be more and more, more and more specific every time.

1:3:01

Sounds good. Tell me yes or no everyone.

1:3:07

Everyone clear? These are very basic things. Okay.

1:3:10

Okay. Now we can take a break, everyone.

1:3:13

Okay? Like Wikipedia is editable, not trustworthy.

1:3:17

level, kind of yes. Okay. So let's take a break, everyone. Now it's 853, 854. Let's

1:3:24

beat at 906, 906, 907. If I say it or that in the fifth term, how does the AI know what I'm

1:3:34

talking about in the first term, right? Does it reread the whole chat every time? It maintains

1:3:39

a conversation memory. In the conversation memory, it maintains the topic, it maintains the product type.

1:3:44

It also maintains the product. That, okay, you are talking about, let's say, elect,

1:3:47

the category is electronics and you're talking about iPhone 17, right? Now when you say that in this

1:3:53

conversation, even in the 10th question, you say that, okay, I want to return it. Now, this it will be

1:3:59

referred via this conversation history. That, okay, this it is referring to some electronics item.

1:4:03

What electronic item, iPhone 17? Makes sense more? Yeah. So, yes, it's almost 855. Let's meet around

1:4:11

907, 908, right? Let's have around 10 to 12 minutes of break. And then after the break, we will start

1:4:16

with the next set of discussions. See you in 10, 12 minutes, everyone.

1:4:46

Thank you.

1:5:16

Thank you.

1:5:46

Thank you.

1:6:16

Thank you.

1:6:46

Thank you.

1:7:16

Thank you.

1:7:46

Thank you.

1:8:16

Thank you.

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

1:13:16

Thank you.

1:13:46

Thank you.

1:14:16

Thank you.

1:14:46

Thank you.

1:15:16

Thank you.

1:15:46

Thank you.

1:16:16

Thank you.

1:16:46

Hi, everyone.

1:16:50

Hi, everyone.

1:16:55

I'm audible.

1:17:16

Okay. Now let's get started everyone with the next topic, which is something called as

1:17:25

Semantic chunking.

1:17:28

Do you remember the process of chunking everyone?

1:17:30

What is the process of chunking, everyone?

1:17:39

What is the process of chunking? Can you recall?

1:17:43

Sources are always clear with AI.

1:17:45

clear with AI or they might hallucinate in citations.

1:17:49

Chances are very less.

1:17:50

Anjum, they are pretty much clear.

1:17:53

Because AI knows, like the system knows where they are,

1:17:57

fetching the data from.

1:18:01

So let's talk about everyone's semantic chunking.

1:18:05

So what is the meaning of chunking?

1:18:07

dividing the, dividing a larger document or

1:18:11

splitting the larger document into small component

1:18:15

for efficient or effective, you can see that retrieval, right?

1:18:22

Plating.

1:18:40

Larger document.

1:18:45

for efficient retrieval and retrieval and you can see that, managing or processing, you can see that.

1:19:08

Now everyone, what is the default way of chunking?

1:19:12

Generally, what approach do we follow to chunk?

1:19:14

chunk? What is a traditional approach? What is the traditional approach?

1:19:21

What is the traditional approach? Fixed size, right? So fixed size chunking is most popularly used.

1:19:31

But do you think that if you want fixed size chunking is a very good approach to chunk some critical

1:19:37

documents?

1:19:42

Answer is no.

1:19:44

Not a very good approach to chunk.

1:19:49

Not a very good approach.

1:19:51

But still, everyone, a lot of people, lot of companies still follow fixed-size chunking.

1:19:57

Why? Because everyone, it might not give you best performance, best retrieval, best answers.

1:20:04

But still, it is the advantage of this is everyone, it is easy to implement.

1:20:09

Correct?

1:20:11

Still people follow this because,

1:20:14

it is easy to implement. Now, guys, if you are implementing some AI application where you don't

1:20:20

you don't need a lot of, let's say, you are not working on some critical use case. You are building

1:20:25

a simple application, let's say even you're building a simple project. Now for implementing a

1:20:30

simple project, do you need very accurate answers, very high quality answers? Answer is no.

1:20:36

If you don't need very accurate, very high quality answers, then you can go with fixed size chunking

1:20:41

because it is very easy to implement and it can give you decent answers.

1:20:44

If not very high quality.

1:20:47

But symmetric, but fixed-size chunking is not a very good approach for good applications,

1:20:53

production level applications, which are used by real people.

1:20:56

And if people are paying you money to use your application, definitely fixed-size chunking

1:21:01

is not going to be a good idea.

1:21:02

Because if you blindly divide a document into chunks, right, let's say first 500 words, next 500 words,

1:21:10

next 500 words, quite possible that the semantic meaning.

1:21:14

you will end up losing.

1:21:16

Correct, everyone?

1:21:17

Some part of a particular document, some part of a particular sentence might go in chunk one.

1:21:23

Some part can go in chunk one. Some part can go in chunk two.

1:21:25

Right?

1:21:25

So what semantic chunking does?

1:21:38

Semantic chunking tries to split.

1:21:44

tries to split text based on the meaning.

1:22:14

a logical section, a logical section, a logical text.

1:22:40

Is the definition?

1:22:41

Is the definition clear to all of you?

1:22:43

Not really, Mukta.

1:22:45

We will have to write a different set of algorithms to do the semantic chunking or any type of chunking.

1:22:51

Is that point clear to all of you?

1:22:53

So semantic chunking is create chunks based on the meaning, not randomly, or not just any random type of chunking or fixed size of chunking.

1:23:04

So if you're creating semantic chunking, what will be the advantage?

1:23:13

Can I say that it will lead to better retrieval qualities.

1:23:20

Better retrieval of queries.

1:23:26

Of queries.

1:23:29

Of answers.

1:23:30

Is that point clear to all of you?

1:23:33

Folks, yes or no?

1:23:35

Generally not.

1:23:37

Okay, okay, Anjou?

1:23:40

Okay.

1:23:41

Because everyone, at the end of the day, the retreat

1:23:43

quality completely depends on the chunk quality.

1:23:48

If your chunk contains better data, your retrieval quality will be good.

1:23:52

If your chunk does not contain good data, your retrieval quality will be bad.

1:23:56

Make sense, everyone?

1:23:59

Okay, let's see how does semantic chunking works?

1:24:13

How does semantic chunking works?

1:24:27

Now first everyone, what do we do is, I'm just writing a high level overview of that how can you implement

1:24:34

the semantic chunking?

1:24:36

Let's try to understand step by step.

1:24:37

First, everyone, what do you do is we split the document.

1:24:43

split the document.

1:24:50

Split the document first into parts based on, let's say topics or paragraphs.

1:25:11

Just by looking at the document, do you, will you be able to understand the complete

1:25:15

semantic of the document?

1:25:16

Do you think so?

1:25:17

That you will be able to understand the complete semantic of the document just by looking at it.

1:25:21

That okay, these parts are connected to each other.

1:25:23

So they should go to one chunk, this part should go to that chunk and so on.

1:25:27

And so what do you do, everyone?

1:25:28

To understand the document better, first you divide that document based on the topics.

1:25:33

If let's say that particular document has headings, right?

1:25:36

Let's say this is the heading, then this paragraph, this paragraph, this paragraph, and so on.

1:25:41

So what do you try to do?

1:25:42

You try to divide the document first based on what you can see in front of your eyes.

1:25:47

That is, based on paragraphs and topics.

1:25:50

But is it possible that everyone, that paragraph can be related to each other?

1:25:54

For example, let's say this paragraph, this paragraph, this paragraph.

1:25:56

Now you say that, okay, this chunk, this is one chunk, this is another chunk.

1:26:00

But what if everyone, these two paragraphs are very, very close to each other, right?

1:26:05

If these two paragraphs are very, very close to each other, don't you think then in that case,

1:26:08

the semantic chunking that you have performed is not a very very,

1:26:11

very good, is not, like, is not up to the mark?

1:26:15

Right?

1:26:16

So, for example, this is one paragraph.

1:26:18

This is one paragraph, right?

1:26:20

If you just say that, okay, if you divide the document based on paragraph, right?

1:26:24

So you say that, okay, this is chunk one, this is chunk two.

1:26:26

Now, as of now, you have just divided the document based on the paragraphs.

1:26:31

But what if everyone, both of these paragraphs are connected to each other, they are related to each other,

1:26:36

they are very close to each other.

1:26:38

If both of these paragraphs are very close to each other, don't you think,

1:26:41

Ideally, they should be part of one chunk.

1:26:43

Ideally, they should be part of one chunk, right?

1:26:46

So now it means that if you don't create one chunk of these two paragraphs,

1:26:51

it means that your semantic chunking is not up to the mark.

1:26:56

Yes or no.

1:26:57

So what you can do, everyone, is how can you find out that, that whether these chunks that you have created,

1:27:02

right, let's say chunk one, some paragraph here, some paragraph here, this is chunk one,

1:27:06

this is chunk one, this is chunk two.

1:27:07

How can you find out that whether both of these paragraphs should be present?

1:27:11

in other chunks, individual chunks, or they should be present in one single chunk.

1:27:17

Can you find the embedding and then compare?

1:27:21

Yes or no? So what you can do everyone is, you can create the embeddings of these chunks.

1:27:41

of these chunks or these parts of the documents, then compare the embeddings.

1:27:56

So which embeddings should we compare? Don't you think we should just compare the embeddings of

1:28:01

neighboring chunks, adjacent chunks? Correct? This part, this part. Compare them. If they are very

1:28:09

similar, don't create multiple chunks?

1:28:11

Club them. Yes or no? Merge them. If they are very similar. So compare the embeddings of adjacent chunks, right?

1:28:41

for semantics, whether the meanings are same or not, for semantics. And then everyone,

1:28:48

the fourth is, the fourth approach is, if you can see that, merge the chunks when,

1:28:55

merge the chunks when merge the chunks if they are similar. If they have closed vector embeddings.

1:29:11

If they have closed embeddings, is that point clear to all of you? Yes or no. This is how you do

1:29:23

semantic chunking. Have a look at it and try to understand. Now, obviously, everyone, is this a bit

1:29:32

difficult, time-consuming, a complex process to do on bigger documents? What do you think about it? Is this definitely a bit

1:29:41

difficult time-consuming effort to create semantic chunks of a bigger document? Obviously,

1:29:48

yes. But if you want to have better retrieval quality of your answers, right? Better retrieval quality

1:29:55

of your application, definitely you'll have to spend efforts in terms of time, in terms of complexity,

1:30:01

in terms of resources, right? So is the process clear to all of you? If yes, let me know,

1:30:06

we can move to the next idea now.

1:30:11

Okay, I have given one example in the document, everyone, in the notes. You can refer that example for better understanding, right? So let's say the example is something like this. Let's say you are building a customer support chatbot for an e-commerce platform, the very simple, very straightforward example that we have been taking for long time now. And which contains different articles, let's say there is one long article, which contains different sections for order cancellation, order return, refund timelines, return eligibility, return eligibility.

1:30:41

damaged items, wallet, refund, credit card refund, etc, etc.

1:30:46

Right? Now, everyone, with fixed size chunking, what can happen?

1:30:51

Let's say if there is one document which contains all the, all the information about different,

1:30:56

different, different, different, you can say that, different, different, topics, refund, return,

1:31:04

cancellation, damage product, refund policy, wallet refund, refund, credit card, refund, etc., etc.

1:31:10

Now, if you process, if you process this document via fixed size chunking, what can happen?

1:31:20

With fixed size chunking, is it possible that some part of return can go to refund? Some part of return can go to refund. Some part of refund can go to refund. Some part of refund can go to maybe, let's say, damaged product. Some part of damaged product can go to cancellation and whatnot, right?

1:31:38

something can go, anything can go anywhere, right?

1:31:42

That means, everyone, if you ask a question, you might not be able to get a very good answer, obviously,

1:31:47

because you will fetch the chunk which is completely, which is very close to your query,

1:31:53

but that chunk might not contain all the information.

1:31:55

That chunk might contain only some information because some information might have gone to the previous chunk or the next chunk.

1:32:02

Correct, everyone?

1:32:04

Make sense?

1:32:05

So ideally what we should do.

1:32:06

In semantic chunking, everyone, don't you think we should try to chunk based on the topic?

1:32:11

That, okay, all the information related to order cancellation should be present inside one chunk.

1:32:16

All the information related to refund should be present in one chunk.

1:32:20

All the information related to return will be present in one chunk.

1:32:24

In that case, everyone, if you are asking any question about return, you just have to fetch one chunk

1:32:29

and you will fetch that entire chunk.

1:32:32

Now that particular chunk contains each and every information.

1:32:36

about the return that you are asking about.

1:32:39

It will be easier for you to give the answer.

1:32:42

Is that point clear to all of you?

1:32:43

Yes or no.

1:32:48

Okay?

1:32:49

Obviously, well, it is very good thing.

1:32:51

Semantic chunking is obviously a very, very better approach, right?

1:32:55

That can make chunks huge.

1:32:57

Answer is this. That can make chunks huge.

1:32:59

And also, if let's say after semantic chunking, if you think that,

1:33:03

some of the chunks are becoming very big, then you can put a threshold.

1:33:06

that okay after semantic chunking if any chunk is going beyond then beyond a particular threshold

1:33:12

then you divide it further okay bashworthy after semantic chunking you can do that as well okay okay

1:33:20

okay what are the limitations of semantic chunking

1:33:36

limitations of semantic chunking.

1:34:06

Complex pre-processing. What is the meaning of pre-processing?

1:34:15

Pre-processing? Pre-processing means that basically everyone, that whatever you are doing before processing

1:34:27

the query. So you can say that everyone if you think that pre-processing simply means that we are referring

1:34:33

to semantic chunking. Because cementing chunking chunking is the

1:34:36

the process that you follow before processing the query. So can we say that?

1:34:39

This is a complex process, right? Complex process. Right? Cost. Cost can increase because of resources.

1:34:54

Also everyone, it will take time. Time will increase. Also everyone, some chunks can be bigger.

1:35:03

Correct or not?

1:35:04

some chunks can become huge. So you will have to take care of that as well accordingly.

1:35:12

Some chunks can become huge. Is that point clear to all of you? Yes or no.

1:35:25

Okay. Now let's talk about everyone the next and a very, very important topic, which is called as

1:35:34

hierarchical indexing strategies. What is the meaning of hierarchical indexing

1:36:00

indexing? Let me first explain that the term is not very

1:36:04

like very self-understood that you will be able to get the meaning only from the term itself.

1:36:09

Let me try to explain. What hierarchical indexing says that I want that we can try to maintain. So

1:36:15

first of all, what is indexing? Forget about hierarchical. What is indexing? What is the meaning

1:36:23

of term indexing? Indexing means organizing the data in such a way so that you can retrieve it

1:36:34

Correct? Faster retrieval. Folks, yes or no? Maintaining some information

1:36:45

at some place so that you can fetch the data faster. You can make the retrieval faster. What

1:36:52

is the meaning of heretical indexing? Heretical indexing simply means that is one. If you can organize

1:37:04

organizing data at multiple levels. Organizing data at multiple levels from, you can say that, from high level summaries

1:37:31

to more granular summaries.

1:37:44

From high level

1:37:48

level, summaries.

1:38:01

to more granular level summaries. Now what is the meaning of this? Let's try to understand this.

1:38:13

Okay? Absolutely correct. Maintaining multiple layers of information, right? So let me try to explain this.

1:38:25

definition, right? So we can see that instead of, instead of storing, only one list of chunks,

1:38:55

the relationships as. What relationships? Like relationship between chunk and document? That this chunk is coming from this document.

1:39:14

Relation between chunk and section, chunk and subsection, that this chunk belong to this document, this

1:39:25

section, this topic, and whatnot. Paragraph, topic, and so on. Kind of parent-child

1:39:34

relation, absolutely. Paragraph or topic and so on. Now, guess tell me, if you are fetching a

1:39:42

particular chunk and that chunk is completely individual, right? Let's say you fetch the chunk,

1:39:48

because after chunking process, the documents have been splited into individual chunks. Let's say one

1:39:54

document has been divided into 100 chunks. Now, when you try to retrieve the answer, you go

1:39:59

to vector embeddings, you go to vector database, you compare the embeddings, and you fetch a chunk

1:40:03

which is closest to the query embedding. Once you fetch the chunk, do you really know that this chunk

1:40:11

belongs to which document, what is the context about it, what information does it contain,

1:40:15

which paragraph it belongs to, which section it belongs to, etc, etc. Answer is wrong, right?

1:40:20

If you don't maintain that information, by default, that chunk becomes a completely individual.

1:40:24

unit. It means that even now, if let's say you think about this, if you are building

1:40:29

an advanced rack system, if you say that, okay, this chunk is completely individual. If you

1:40:35

want to maintain, if you want to fetch, if you want to retrieve, some more information apart from

1:40:40

that chunk, where will you refer? You don't have any reference. Getting the point? If you don't

1:40:47

maintain the relationship that this chunk belongs to that document, this chunk contains the

1:40:52

information about this section, this belongs to that subsection, this chunk belongs to

1:40:56

that paragraph and so on. So, for better retrieval options, for better retrieval strategies,

1:41:02

in fact, faster retrieval strategies also, what you can do is you can maintain the, you can maintain the

1:41:08

relationship between the chunk and these things. How many if you are getting a very, very high

1:41:14

level overview, that okay, even after dividing the document into chunks, you're not making them

1:41:19

completely independent, completely different from each other.

1:41:22

what essentially you are doing is you are making them still related to each other.

1:41:27

You still be, you will still be able to find out that this chunk is related to that document.

1:41:32

This chunk is related to that topic. This chunk is related to that subtopic or subsection and

1:41:38

whatnot. Metadata. You can say that kind of metadata. Right. In slightly more detail.

1:41:44

Right. So you can say that everyone. What this relationship allows you to do. Can I say that this

1:41:49

relation, this allows.

1:41:52

This allows retrieval to begin, begin broadly, and then we can go in depth

1:42:22

if required.

1:42:26

Is that point cleared all of you? As I discussed everyone, first you fetch the chunk. But if you want more

1:42:32

information that this chunk, let's say because everyone, like any kind of chunk that you do, no type

1:42:38

of chunking is 100% perfect. Even if you do semantic chunking, right? Semantic chunking will also be

1:42:43

not 100% perfect. If user wants more answer, more in-depth, in detail answer, if you fetch a particular

1:42:49

chunk, some information is present before that, some information.

1:42:52

is present after that, how will you go in detail, in depth, right? If this chunk contains the

1:42:57

hierarchical information, hierarchical means everyone, parent-child relation, tree kind of structure,

1:43:02

that this is a document, this document is divided into these chunks. This kind of relation is called

1:43:07

as hierarchical, heretical relation. If you maintain the hierarchical relation, will you be able

1:43:13

to go in-depth if required? If user wants to have in-depth answer, in-detail answer, you will still

1:43:19

be able to iterate. You will still be able to traverse.

1:43:22

Is that point clear to all of you?

1:43:24

You can go back to parent, you can go back to child and whatnot, right?

1:43:29

So why is hierarchical indexing important?

1:43:42

Can I say that everyone?

1:43:46

If I tell you one problem statement first of all, or not problem statement, let me try to quote something.

1:43:52

If you have flat chunk, flat chunk, what is the meaning of flat chunks?

1:44:00

It means that in the chunks you are not maintaining the hierarchical information, correct?

1:44:05

If you are not maintaining any hierarchical information inside chunks.

1:44:08

So you can say that flat chunk retrieval, flat chunk retrieval, flat chunk retrieval has these common

1:44:22

has common problems. What are these common problems? The problems are something like this.

1:44:31

Can I say that? Search or let's say small chunks. If you have very small chunks, does it improve?

1:44:52

If you have very small chunks, will it improve your search quality?

1:45:00

Will it improve your search quality?

1:45:04

Answer is no.

1:45:06

Not search quality, but can I say that everyone, the small chunks may improve your, you can say that?

1:45:12

Your, you can say that precision.

1:45:15

Now, what is the meaning of precision, everyone, that if you have very big chunks,

1:45:18

don't you think big chunks may contain a lot of information?

1:45:22

But small chunk, if you are creating very small chunks, if it has some meaning, right?

1:45:27

Or maybe let me try to put it in a different way. Otherwise, it might get confusing. What I'm trying

1:45:31

to convey is that small chunks can improve your search precision. What is the meaning of precision,

1:45:37

everyone? That if you have a very small chunk, you know that it is going to contain the answer accurately.

1:45:47

Right? But if you have very big chunk, it might contain some extra information also.

1:45:52

Because if everyone, what happens is whenever you fetch a chunk, you fetch after fetching

1:45:56

the chunk, after retrieval the chunk, you send those chunks to LLM. So LLM will be using

1:46:02

those chunks to generate the answer. Correct? Correct. If you send a very big chunk to LLM,

1:46:09

what will happen? That very big chunk has the answer that you need. But it might have more information

1:46:15

also. So don't you think the answer will not be very, very precise? It will be a good answer. It will be an

1:46:21

accurate answer, but it will not be very to the point answer. Correct? It might contain other

1:46:26

information as well, correct. But if you have a smaller chunk, given that, that small chunk is

1:46:32

semantically correct, that is not incorrect. You have a relatively smaller chunk, but that chunk

1:46:38

contains all the information that you need. Don't think in that case, the small chunk can give you very

1:46:45

precise answer. Correct answer, correct everyone? Are you guys getting this point? That's what I was thinking

1:46:50

that how do you, how do I explain that particular thing to you? But at the same time,

1:46:54

the large chunks, right? Large chunks can do what? If you have very big chunk, correct? Then you will get

1:47:03

the answer, but that answer will be slightly more in-depth, could be, it could be in-depth, or it could be

1:47:09

slightly more complete, because you will be able to add some more background, some more, you can say

1:47:16

that, some more information inside that answer. Correct? So don't you think, if you know,

1:47:20

everyone in short terms. Can I say that? If you have, if you want accurate answer, as well as you

1:47:28

want a good depth also, a good background also. You don't want only to the point answer. At the same

1:47:36

time, you want accurate answers also. So what you can do everyone is, you can try to create the chunks

1:47:40

in such a way that chunks are not very small, not very big. What you can do is that you have the chunks.

1:47:47

If you want, if the user wants more in-depth answer, then you should be able to go to

1:47:53

the other chunks as well if required. Can we say that?

1:47:58

Correct. Assume that everyone. Let's say you have fixed-size chunking and you are not maintaining

1:48:02

any hierarchical indexing. It means that whatever chunk you are getting, you have that chunk only.

1:48:07

You cannot go to previous chunk, next chunk, etc. Because there is no context, there is no indexing,

1:48:12

there is no hierarchical relationship. Now in that case, everyone, if the chunk is very small, you will

1:48:17

more precise answer. If the chunk is very big, then you will get more broad answer. But don't

1:48:22

you think even, both of them might not be very good. You want accuracy, but at the same time,

1:48:28

you want some depth also, some explanation also, some background also. You just don't want one word

1:48:35

answer. You want some more explanation, some more background. In that case, everyone, if you have

1:48:41

a decent level of chunk size, but along with that, if you maintain hierarchical indexing, if you maintain

1:48:47

the information about the document, then don't you think you will be able to fetch

1:48:51

more information in case if it is required using the indexing process, using the hierarchical

1:48:57

index. Getting the point, if you want more information about the document, you can go to that.

1:49:03

Right. So that's why let me not write it down. Otherwise, it will take a lot of time as well,

1:49:08

and it will be a slightly more confusing. I hope the idea makes sense all of it. So let me

1:49:14

explain this one more time that what we do.

1:49:17

We try to retrieve not very big chunks. We try to retrieve smaller or an average or a decent

1:49:23

size of chunks. And what we want is we want to fetch specific chunks. Correct? You don't want

1:49:31

a lot of chunks in the answer, in the retrieval. You want specific chunks. Why specific chunks? Because

1:49:36

specific chunks will give you accuracy. Right. But everyone, if you want to attach more information,

1:49:41

if you want to attach some parent information, some other chunks information, some other document

1:49:47

information, then you need hierarchical indexing. Is that point clear to all of you? So

1:49:51

hierarchical indexing can help you to construct better answers with the current chunk. Are you guys getting

1:49:57

this point? For in-depth answer thing to work, we will need to connect with smaller chunks to hierarchal

1:50:01

indexing. Absolutely correct. Right? You cannot have very small chunks. You cannot have very big chunks.

1:50:07

But you will have decent size of chunks. You will retrieve specific chunks. But whenever you want

1:50:12

to reconstruct, whenever you want to construct better answers, you want some background.

1:50:17

you can fetch the document level information also from hierarchical indexing. How many

1:50:21

if you're clear? Keeping chunk size to small and using hierarchical approach will give explained answers.

1:50:27

Absolutely correct. Not too small also, Anjum. They should be decent. It should, the chunk size

1:50:32

should never be too small. It should never be too large. Okay? So let's talk about different

1:50:39

strategies, everyone, of hierarchical indexing.

1:50:43

Right?

1:50:47

different strategies for hierarchal indexing. First, everyone is

1:50:53

is parent-child, parent-child, territory.

1:51:04

What is the strategy, everyone?

1:51:07

This strategy, one. This strategy simply says that, store,

1:51:17

smaller chunks in vector database and store smaller chunks in vector database and

1:51:42

store smaller chunks in vector database and each smaller chunks.

1:51:46

bigger chunks or document. It means that even now if you see that if you want

1:51:56

precise answers, you can just go to chunk, smaller chunk and get the answer. But if you want

1:52:02

in-depth answer, if you want background information, then you can refer the bigger chunk or the

1:52:07

document. This is only if you want. Correct everyone? Only if you want. It is not a mandatory thing. It is not

1:52:14

a force thing. Is that point clear to all of you?

1:52:16

So what you can do at the time of query, you can retrieve these smaller chunks, right? If you want, you can go to their parent to retrieve more information. This is one approach. This is one strategy. Another strategy could be everyone. This is called as summary to detail retrieval.

1:52:46

Summary to detail retrieval. What is the meaning of that? You can create summaries, everyone.

1:53:01

Create summaries of documents. You can create some sections, some important sections. You can identify that.

1:53:16

and index these summaries with chunks. I think this is also self-explanatory, right?

1:53:37

With chunks. So what do you can do, everyone? Do the chunking process as you do. But along with chunking process, you have also indexed.

1:53:46

you have done is at the time of pre-processing, when you are creating chunks, you have also

1:53:50

a summary of entire document also, depending on what kind of approach do we have, what kind of document

1:53:56

do we have, what works best for your use case. Let's assume that in a very simple way. You have created

1:54:01

a complete summary of the entire document. And you have stored that at one place. Now with each chunk,

1:54:08

you have stored the index to that document. Document summary. Now when you fetch the document,

1:54:13

you can generate the answer from that particular chunk. But if you want more information,

1:54:18

then instead of going through the entire document or other chunks, because if you're going through the

1:54:24

entire document or if you're going through the entire chunks, it can take more time. So what you can do is

1:54:29

you can go through the summary of the document. So that if you want to construct the answer, if you want

1:54:33

to have more information, then you don't have to go through the entire document. Rather, you can

1:54:39

get that information from the summary of the document.

1:54:43

Is that point clear to all of you?

1:54:51

Makes sense? How will it summarize? We can summarize using LLM also, right? Anjum, we can summarize

1:54:57

the document using LLM.

1:54:59

Okay. Third strategy, which is even more interesting, right? Which is even more interesting,

1:55:04

which is called, that is called as recursive retrieval. Try to guess. Would you try to guess this?

1:55:13

retrieval? Would you try to guess what this recursive retrieval means?

1:55:20

A repetition, can you please elaborate?

1:55:26

Folks, try to understand from the perspective of

1:55:40

of hierarchical index. Recursive means what? When you repeat, right, repeat something,

1:55:49

right? Let me give you some example of recursive. For example, Avion, how many if you know

1:55:53

that, how many if you know a Fibonaki series? Do you know Fibonaki series? Do you know Fibonaki

1:56:00

series? What is Fibonaki series?

1:56:10

2, then 3, then 5, then 8, then 13.

1:56:15

It means that if you have to get the new number, right?

1:56:19

If you have to get the new number, the new number, the new number is nothing but the addition of last two numbers.

1:56:24

So it will be 23, 13 plus 8, 23.

1:56:27

Then the new number will be add of these two numbers.

1:56:30

Add last two numbers, 34, okay?

1:56:33

Then add these two numbers 34 plus 21, which is 55 and so on.

1:56:37

This is Fibonacian, right?

1:56:39

Now this is,

1:56:40

is this a repetitive process?

1:56:42

Is this a repetitive process?

1:56:45

This is, this problem can be solved using recursion, right?

1:56:49

So for example, everyone, if you don't know the Fibonaki series,

1:56:52

no one knows the Fibonaga series.

1:56:54

If I directly tell you that tell me Fibonaki of 100,

1:56:57

tell me 100th Fibonacci number, right?

1:57:00

If you have to solve this recursively, using recursive approach, what do you can do?

1:57:04

That's okay.

1:57:05

If I have to find out the 100th Fibonacci number, understand.

1:57:09

To find 100th Fibonacci number, understand.

1:57:10

100s Fibonacci number, what do you need?

1:57:12

100th Fibonacci number is sum of 99th Fibonaki number and 98 Fibonaki number, correct?

1:57:19

No?

1:57:20

Yes or no?

1:57:21

Now to find 99th Fibonacci number, you need 98th Fibonaki number and 97th Fibonacci number.

1:57:29

So do you say that even to solve one problem, you have to solve another problem.

1:57:34

To solve this problem, you have to solve another problem.

1:57:37

To solve 97, you need to solve 90.

1:57:39

solve 98, you need to solve 97. To solve 97, you need to solve 96 and so. So you'll

1:57:45

have to keep on going till 1. Is that point cleared all of you? This is what recursive is.

1:57:51

Similarly, everyone, the recursive retrieval means what? Recursive retrieval simply means that

1:57:56

whatever node or whatever chunk you have retrieved, can that chunk give you the reference of other chunk?

1:58:04

Parent chunk, right? For example, let's say you are dividing a

1:58:09

document into multiple levels. You have a bigger document. That bigger document is divided into

1:58:14

multiple topics. Inside the topic, you have multiple paragraphs. Inside the paragraph, you have

1:58:18

sections and whatnot. You have multiple hierarchies. Now, if you find out a very small chunk and you want

1:58:24

to reach out to the document, from the smaller chunk, you will not directly be able to reach through

1:58:28

the document. So what do you'll have to do? From that chunk, you will go to the topic. From the topic,

1:58:33

you will go to the, let's say, a bigger topic. From that bigger topic, you will go to the section. From that

1:58:39

section you will be able to reach to the document. Is the complete process making sense to all

1:58:43

of you? Step by step, retrieval, right? Step by step or recursive retrieval. Make sense?

1:58:50

So one chunk refers to another chunk, another chunk refers to another chunk and so on. Is that point clear

1:58:56

to all of you? So for example, everyone, a financial report, right? Let me give you an example for this

1:59:00

because it is slightly different approach. Let's say there is a financial report. That financial report

1:59:05

contains multiple hierarchies. There is complete report.

1:59:09

Inside that report, you have revenue section, then you have geographic revenue,

1:59:14

then you have product revenue, then you have profit, then you have cash flows and whatnot.

1:59:18

Now if you want to ask any question, that question refers to a particular chunk, but that chunk

1:59:23

will only contain very, very specific information. But you don't want only specific information,

1:59:27

you want to add more context to your answer. So you might have to go to the parent chunk which will

1:59:32

contain more information. If you want to add more depth inside the answer, you will go to its parent,

1:59:37

You will go to its parent and finally you will go to the parent document, the entire document.

1:59:43

Is that point clear to all of you? Tell me yes or no.

1:59:50

Okay. Now let's talk about everyone. Just one more thing, everyone, just just, just one thing.

1:59:54

What do I need to do? Just a second. I need to put the charger.

2:0:02

Things are like, there are, these things are endless, right? You can learn whatever you want.

2:0:07

So never coming things.

2:0:12

Okay. But it will be lengthy and complex. Obviously, yes. It will be lengthy and complex. But this you will

2:0:17

only be using if you want a very good in-depth answer. Make sense, Anjou? Okay. Now let's talk

2:0:25

about everyone. Financial use case, right? Now when you are giving an answer related to finances,

2:0:31

you cannot just give one word answer. You need to add a lot of information about the context. That context,

2:0:37

context you might get to the, you might get from the parent, its parent, its parent and so on.

2:0:42

You might have to go to multiple levels, multiple levels one by one, one by one by one, to get in-depth answer.

2:0:49

Okay? Okay. So let's talk about everyone. Benefits of hierarchal indexing.

2:0:54

Benefits of.

2:1:07

hierarchical indexing. Tell me everyone. What are the benefits of heretical indexing?

2:1:23

The best benefit of hierarchical indexing everyone is, can I say that better completeness of the

2:1:30

context? That's it. Better context.

2:1:37

If you just take the answer from the chunk, it might not be, it might be the correct

2:1:43

answer. I'm not saying that it will be wrong, but it might not be very complete. If you want

2:1:49

complete answers, in-depth answers, more precise answers, more background information, then you need

2:1:55

to follow hierarchical indexing. Is that concrete all of you? This is the only benefit that I would

2:2:01

like to recall, right? There are other benefits as well, everyone. But all the other benefits will

2:2:07

will be related to this. Okay. But at the same time, everyone, if it is good, if it is a good

2:2:13

approach, everything comes at a cost, correct? Do you get anything for free in today's world? Do we

2:2:20

get anything for free in today's world? Absolutely not, right? You'll have to pay something. What are

2:2:26

the challenges for this? Challenges of hierarchal indexing. As Anjum mentioned, it is going to take cost.

2:2:37

complex and time consume. Okay. Give definition of recursive. Okay, let me write down

2:2:55

the definition of recursive. I have forgot to write. But anyways, all these definitions are

2:2:59

completely written in the nodes, but still let me write it down here as well. Right?

2:3:07

A retrieved chunk, a retrieved chunk, can point to some other point to some other chunk or section.

2:3:37

And it can further point to, it can further point to, correct to, correct?

2:4:00

Correct? Okay, there might be multiple levels.

2:4:05

So, this is it everyone. Now the other topic that we wanted, that we, that we, that we have everyone is, I don't think we should start this topic. The topic name is multi-model rag. Okay. If I take this topic, it will take at least maybe 20 to 30 minutes. I think yes.

2:4:35

So guys, this topic and one more topic we will cover in a separate class, okay? I think we would need one extra class on rack to complete. Let me check with the team, right? We will see after this completion, Mukta. Okay. So let's do one thing, everyone. We will take one more class on rack. Let me check with the team when we can have that. In fact, in the next week also, we have all the four, we have three classes, Tuesday, Thursday, Saturday. Let me check with the team when we can accommodate that, okay?

2:5:05

No worries. I think we are done with the class. If you have any doubt, you can ask. Otherwise, first, we can launch the poll. Before we launch the poll, how many of you are understanding the rag concepts from last three classes? I think we have spent now six hours on learning rack. From next class. Next class, metham. How many of you are understanding rag? Guys, we will have one implementation class also, don't worry. So most of these concepts, we will see in the implementation as well.

2:5:35

okay. So these concepts will be more practical to see in action after these in-depth understanding, right? So let me launch

2:5:44

the feedback poll everyone. And after that, we can end the class. So guys, let's take the feedback poll and then we can end the class.

2:5:54

Thank you so much. Have a good day. Take care. Good night. Have a good weekend.

2:6:00

Feel free to, I would say, after thinking about 10 to 5 to 5.

2:6:05

10 minutes, Anjum, try to feel free to Google about it. Okay. It is okay. Once you Google

2:6:11

about the answers, then you will be able to understand that what kind of answers you can write it

2:6:16

right now. Okay. Does the AI agent get slower as the conversation gets slower? As a conversation gets

2:6:20

longer? Absolutely, yes. Does the AI agent gets slower if the conversation gets longer and longer?

2:6:26

Because it has more text to process, answer is yes. On top of that, you can do some optimizations

2:6:31

using caching, using, what do you say, maintaining something in the memory and so on. That's

2:6:37

it. Okay. But if you don't do any extra processing, does it become slower? Absolutely, yes. It will,

2:6:43

it will become slower. I think two, three people have not filled the feedback poll. Please do that.

2:6:51

And we can end the class then. Thank you, everyone. Have a good day. Take care. Good night. See you on Tuesday now.

2:6:58

Pratish, do we have the, what do you say?

2:7:01

The tutorial session for this batch in this week?

2:7:06

Yeah, yesterday we have completed the tutorial session.

2:7:09

Tutorial Friday go out.

2:7:12

Yes.

2:7:12

Okay, okay, got it. In the next week also, the tutorial is on Friday?

2:7:16

Yes. Basically, you are going to take sessions on Saturday. So, tutorial session has been

2:7:20

there in Friday 8 p.m. basically.

2:7:23

Friday 8 p.m.

2:7:24

Okay, one tutorial session per week, yeah.

2:7:27

Okay, got it. Thank you.