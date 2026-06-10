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

4:59

Thank you.

5:01

Thank you.

5:31

Thank you.

6:01

Thank you.

6:31

Thank you.

7:01

Thank you.

7:31

Thank you.

8:01

Thank you.

8:31

Thank you

9:01

Thank you

9:31

Thank you

9:33

Thank you

9:35

Thank you

9:37

Thank you

9:39

Thank you

9:41

Thank you

9:43

Thank you

9:45

Thank you

9:47

Thank you

9:49

Thank you

9:51

Thank you

9:58

Thank you.

10:00

Thank you.

10:30

Thank you.

11:00

Thank you.

11:30

Thank you.

12:00

Thank you.

12:30

Thank you.

13:00

Thank you.

13:30

Thank you

14:00

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

Thank you

14:44

Thank you

14:46

Thank you

14:48

Thank you

14:50

Thank you

14:57

Thank you.

14:59

Thank you.

15:29

Thank you.

15:59

Thank you.

16:29

Thank you.

16:59

Thank you.

17:29

Thank you.

17:59

Thank you.

18:29

Thank you

18:59

Thank you

19:29

Thank you

19:33

Welcome to the session, everybody, we will be starting on here.

19:36

And today we will be starting on here.

19:52

And today we will continue on from the last demo that we discussed.

19:58

Just to add a little bit of context in terms of where we are.

20:09

So this module, we are in the generative AI module and the last session until now, we have covered quite a bit about Gen.

20:18

A.I. We have talked about a lot of conceptual aspects of the generative AI part so far.

20:25

So we understand about what language.

20:28

which models are how to make API calls. So we have also explored, you know, about rags.

20:34

The last four classes were completely about retrieval augmented generation. So we talked about rags

20:39

in detail. And, and today's session is a continuation of that, the same Tesla demo that

20:46

will be seeing. The only difference is we will add memory to it.

20:50

In the last class, if you remember, we did not have any memory. So it was like a single turn

20:54

conversation. It was like a single turn conversation, right? So where,

20:58

we just ask a question, get a response. That's it. It had no memory. Again, you ask a question,

21:02

get a response. It had no memory. But today's session, we are trying to do a value ad. What is the

21:07

value add of today's session? We are trying to build memory in the rag system. That means you can do

21:12

multi-turn conversations. The important term to remember is multi-term conversations. You can ask a

21:17

question, get a response. Again, ask a question, get a response and so on so forth. And once again, the

21:24

real world use case is you are trying to build a solution.

21:28

that recalls earlier messages. You're able to remember what happened before. You are able to

21:33

remember what happened before. So these are the multi-term conversation that you're trying to create.

21:38

That's the big picture idea where we are right now. And obviously from here, from this module,

21:42

after a few more courses that are left out, we'll be moving on to another very, very exciting

21:46

module on agents. We will see that. Okay. So let's jump in and let's talk about what and how to build

21:53

memory in a rag system. But before that, I think it will be interesting to, you know,

21:58

just to take you through the overall template that we have already seen so far,

22:02

and just just maybe take a few minutes to recap this. Everybody knows this already. We have seen

22:06

this in detail. But just to very quickly summarize the core idea of a rag system, we can do that

22:13

for everybody. So let me quickly summarize the core ideas of a rag system here for all of you.

22:28

All of you remember this particular diagram. I'm just going to

22:53

maybe I encourage everybody to just kind of recall some of the ideas that we have already

22:58

scene. See if you're able to recall this. Just take a minute all of you from this one.

23:04

And I can recap this and we'll get to the memory part straight away from here.

23:28

Thank you.

23:58

Thank you.

24:28

So, as you can see, guys, exactly, what we call it? Okay. I hope all of you

24:55

recall it's what we talked about last.

24:58

We first do the chunking. We take the PDF and we chunk it into multiple pieces. These are

25:03

a different chunks that we create. And we use something called fixed size chunking, if you remember.

25:08

So every 512 characters we are creating a chunk. Okay, so we have a 130 page document and we are

25:13

dividing that into multiple chunks. But remember, all these chunks are pages. The chunks are ultimately

25:18

text. Machines don't understand text. So we will have to take these individual chunks and we will have to

25:24

convert these individual chunks into their respective embeddings.

25:28

Okay. So we will have to take these, you know, these individual chunks and we will have to convert these individual chunks into their respective embeddings, chunk embeddings, and we will store it in the vector dv. Right. So that's the way how we will approach it. So we'll take the document. We'll divide that into chunks and save the chunk embeddings in the vector TV. So that is the first part of what we did. Okay. And just to take you through that journey once again, because we'll see the same notebook today with some more.

25:58

additions. Okay.

26:04

We will see the same notebook with some more additions today. I think the same notebook with some more additions today.

26:28

So here I have installed the necessary packages. And here I will go ahead and take my GROC API key. So what you're seeing right now is the is the GROC API key that we are considering. We're importing the necessary libraries, whatever necessary libraries we have importing that. And this is the part where we are unzipping the Tesla file. If you remember, we had that zip file. We are unzipping that and then we are doing chunking. Now why is chunking done?

26:58

is done to ensure that you're not having a huge amount of a bulky PDF, but you're dividing

27:03

that into many, many manageable portions. That is the reason why we are doing chunky. So we are

27:11

referring back to that particular file, which is present inside the Tesla annual reports folder using

27:17

something called file PDF directly loaded. Now, this is not the only way to load the data. We can also

27:22

use other document loaders, right? And what is the library that is making,

27:28

all these things possible. What is the library that is making all this is the library?

27:32

library. So Lankton is a very, library that is a library that is making all of these individual

27:38

possible. So this is the library that we are using, which is making all of these fundamental

27:44

possible. Okay? So you can look at it. We are doing the chunking and in this entire Tesla PDF file,

27:51

we are having total 351 chunks. 3.51 chunks is what we are having right now. Next, after the chunking part

27:57

is done. We are using a sentence transformer model. A GTE large model is what we are using

28:04

right now. This is the embedding model that we are using. Okay. And this is that transformer model

28:10

that will be used to take that particular chunk, that chunk of text. It will be used to convert that

28:16

chunk of text into a sequence of numbers. Embeddings because the chunk is nothing but text. The text

28:22

machines will not be able to understand that. So what you will have to do is you will have to use a

28:27

separate embedding model to take that text chunk and convert that into a sequence of numbers.

28:31

That is what the embedding models will do. And then on the basis of that, we are creating the vector d.

28:36

So at the end of this process, what we are getting is a chroma dv. Next step, what we do is we

28:42

define a retriever. So until here, the vector DB part is complete. So this is the Tesla DB that we have

28:47

created. Right? What is the next phase? What is the next thing we do? Next thing is we ask a question

28:52

and we have to define the retriever object. The retriever is another module that we have to add in here.

28:57

So when the user asks any question, like we asked what is the annual revenue of Tesla in the year 2020, what was the number?

29:05

The retriever has to go and look up in the vector TV. What are the similar chunks? So we will have to instantiate the retriever, right?

29:12

So we will have to go and instantiate the retriever. And in the retriever object, we will have to go and explicitly, we will have to go and explicitly define how many chunks you want to retrieve.

29:24

So we want to retrieve the top one chunk or top two chunks.

29:27

for top three chunks. So that is what we have to define. Okay. So we will define the retriever object

29:31

so that we know that when the user asks the question, how many similar chunks we want to eventually

29:38

retrieve. Okay. So that when the, you know, when the user eventually asked the question, when the user

29:44

eventually asked the question, we should know how many similar chunks we want to eventually retrieve.

29:48

So we want to retrieve the top 10 chunks, 20 chunks, 30 chunks or whatever. Right? So that is the thing.

29:54

So this is the workflow we will see now. Vector DB is already ready.

29:57

Now we will ask a question and retriever should be able to retrieve the top five chunks or the top three chunks, whatever that is. Okay? Let us see that. Let us see that. So here is the retriever object that we are instantiating. You can see. Similarity k equal to five. And when you ask the question, what is the annual revenue in the year 2022? This is the question I'm asking. Let me run this from here because the vector DPC creation usually is very time consuming. So once this is done from here, I can run the code. Yeah. So when

30:27

I ask the question, what is the annual revenue in the year 22? You can see the top five chunks which are retrieved.

30:33

Okay. So based on that question that I'm asking, based on the query that I'm asking, the retriever object went back to the vector DD and it found out what are those top five chunks, chunk one, chunk two, what are those top five chunks, which are matching the content of the question?

30:49

Because that is how it's supposed to be, right? We talked about that library example. You don't want, you don't want to have that whole PDF.

30:54

depending on whatever question I'm asking, I want to retrieve those top five relevant chunks.

31:00

Those chunks are where potentially the answer is present. So I will ask a question. The query is

31:05

where the question will be there. And in those chunks, potentially the answer is there. So based on the

31:10

question, please retrieve the top five chunks. Chunk one, chunk two. You scroll down, you have chunk three.

31:16

Scroll down. You've got chunk four, chunk four and scroll down, you've got chunk five. And scroll down,

31:20

you've got chunk five. Is it the top five chunks that you are able to retrieve? And you have chunk three.

31:24

And now this was the single turn Q&A, rat Q&A that we did last time.

31:28

So until here we are sorted. I think until here, everybody related to it. So we have the vector DB,

31:33

ask the question, retrieve the top three chunks. And now, now this is what you will send as the context

31:39

to the large language model. So, so the final LLM call, what are the things that you will have?

31:44

You will have the system message. So the language model, you will have to define this prompt

31:49

in the proper format, the LLM format, we already understand, system, user,

31:54

system message and user message both has to be there. And what is the user message?

31:59

System message, we will be writing ourselves. We will have to write a very detailed system message

32:02

where we are explicitly, you know, giving the instructions in terms of what this, you know,

32:08

a system is supposed to do. Okay. And the user message will be nothing but the original question.

32:14

User message will be nothing but the original question and the retreat context. So both of

32:19

these things taken together is what we call the user message.

32:24

Okay.

32:24

So system message is the overall high level instructions and user message is nothing but

32:28

the original question the user asked plus the context that was retrieved. And that is why we call

32:34

it retrieval augmented generation. It's not a normal generation. Normal generation is where you

32:38

just ask the question and you get an answer. That is how we define normal generation. Retrieval

32:43

augmented generation is where user asks the question. Based on that question, you know, we are

32:50

retrieving the top five or the top 10 similar chunks. And based on that, the

32:54

response is formulated right so this is the story that we looked at until the last session right if you all

33:00

remember but remember the problem is that this is a single turn baseline so this will work absolutely fine

33:06

i'm using the llama versatile model that's my system message right that's my system message and you can

33:12

take a look at it on the basis of that we are able to i will enter the question let's say what is the

33:19

annual revenue in 2022 i'll ask the question so the retriever will be

33:24

retrieve the top five relevant chunks. I will define the context. This is the context,

33:30

and this is how I formulate my entire prompt. So the prompt will consist of the system message,

33:35

whatever Q and a system message I actually instantiated here. This is my detailed system message.

33:41

So role system message and role user. This is the keyword. Role user. And role user,

33:49

and this is where you write the entire user message. The user message should consist of the

33:53

the question and the retreat context. So both the question and the retrieve context

33:58

should be present in the user message. So this is how the whole prompt is formulated. And you can now

34:03

do the client chat completions create with that and you can see the results coming out. So obviously

34:08

this will get the correct answer. What is the annual revenue in 2022? And the answer to that question

34:13

will be 81,462 million dollars. You can see this. Now what is the issue with this approach? Like so far

34:20

we have we have seen until here now the main issue with this approach is if you see

34:26

this is a thing that we have done without memory this is the one-shot rack system which is built

34:33

without memory right you can of course go and run this and you will get an answer then again you say but

34:38

it has no context of what you asked before if you remember that radio chat interface that we did

34:44

i'll once again show that to you okay i'll once again show that interface to you the system is not able to

34:50

remember what you did before if i only ask the question 2023 it will not get the right answer let

34:55

let me show you like if i go and ask the question i will not give any context annual revenue whatever

35:01

nothing i will just ask the question 2023 if i ask this kind of a question if the user input is this

35:07

do you think the context will be retrieved correctly no you can it is giving the wrong answer can you see when i say

35:11

2023 it is giving 13.26 billion dollar it is not the right answer the 23 annual revenue is not this

35:18

even if i ask the question 2022 it will not give the correct answer but this is what that

35:23

multi-turn conversation i want right imagine if the user asks a follow-up question this system has no

35:30

way of remembering what you asked before if you ask the entire thing at the time it will remember

35:35

it will give the correct answer it will give the correct answer no problem here it will give the correct

35:41

answer but it will not have memory for example revenue in 2020 you get the answer but what if you ask

35:47

a follow up question in the same chat interface what if you ask and in 2020 what about

35:52

2020 it forgets the context it will not be able to remember what you asked before so this thing

35:58

based on our solution this thing will be treated as as a as a completely new user query okay so it is

36:04

like it is like if you know if i take you back to the uh to my to my diagram here it is like you are

36:11

asking a completely new user query which is and in

36:17

2020 but there is a lot of rich context right it's not that you are just randomly uh

36:23

you know asking this question just a second and in it is not a random question there is a context

36:31

first you got the answer for 2022 now you're asking 2022 but in a single turn uh you know a

36:38

one short rag system that we did so far you are asking the question the more the retriever

36:42

will retrieve the relevant chunks and give the answer but the question is not rich

36:47

is not rich enough right now it is a very very open-ended very broad question you're asking

36:52

what what do i want to know about 2023 i'm not specified but do is it revenue is it profit what is

36:57

how do i know that so this will be treated like an isolated question it's a separate question

37:03

and so you will get the wrong answer because based on this question you will retreat the chunks

37:09

and different different chunks will be retrieved maybe revenue for 2023 will be retrieved

37:14

profit for 2020 2023 will be retrieved right uh other kinds of costs for 2023

37:21

will be retreat expenditure for 2023 will be retreat so many things will be retreat for 2023

37:27

but it doesn't know i'm not specified what i am asked and based on that the nm will give a very

37:31

incorrect response so in a real world scenario it is very very important to build memory

37:38

so that when we complete the session today the history should bold the 20m

37:44

2022 revenue turn so now in the second phase if i go and ask this question and in 2023 what is

37:51

going to happen the model should uh actually give the correct answer it should have some way of remembering

37:56

okay you know this is the context in 2023 okay so you can see so that's the way how

38:04

we are going to be able to successfully build a multi so i have actually done the demo here at the end

38:08

you can see it's a small console application this is how it will work out right you can see i ask the question

38:13

what is the revenue in 2022 i get the correct answer this is the story we have already seen so

38:18

far right so 181 000 462 million dollars right you can see this is me you so i ask the question

38:24

what is the revenue in 2022 i asked this question i get the correct answer then i ask another

38:30

follow up question how about 2023 you saw already when i asked how about i i was i was not getting

38:37

the correct answer a while back single turn rack by the time we complete the story here multi-turn

38:43

when i ask this question how about 2023 it somehow understands the context that what i

38:49

asked before it remembers that context it knows i'm talking about revenue so this will not be treated

38:55

like an isolated question it is not a individual question this will be treated like a question as part

39:00

of a follow-up conversation so the assistant the nlm already understands that okay you know previously

39:06

you wanted to know about revenues in 2022 and now you are asking questions about revenue in 2020 so when you

39:12

ask that question the you know the retriever is really you know are giving this specific answer

39:18

96773 it is the correct answer and that's the way how you know these systems are flourishing in

39:24

in fact even if you go and ask this question like you know 20 204 please it will actually give this

39:30

kind of results okay you can see this is the this is the intuition of what this system will do okay so

39:36

now there are different different ways you can build memory now we will do the session we will paste the session in a certain

39:42

but there are different ways and different contexts in which you know a memory can be

39:47

instantiated you can have short-term memory you can also have long-term memory so short-term memory

39:52

is basically the running chat history for the current session so what is short-term memory

39:56

it is the running chat history for the current session and this is primarily what we

40:00

will be you know doing in this lab this session will be focusing on short-term memory and

40:06

what are we going to do in a short-term memory what you know what are we talking about here we simply

40:12

use a python list there are two flavors of demos i'll show you the first flavor is i will

40:18

you know i will use uh uh something like a python list and the second demo i'll show a jason pipe

40:23

this is the short term memory context i'll be explaining to you so short term memory context

40:29

is very useful for the current chat session okay like like how i was explaining in in my

40:35

this is like one conversation thread you ask a question there's a chat assistant that you open you ask a

40:40

question get a response again you ask a question get a response again you ask a question get a

40:42

this is like one chat session one chat session like that's how we chat with chat gpt i

40:47

i mean everybody would have heard that right chat gpt maybe same thing is happening you ask a question

40:52

how is the weather i know you see how is the weather in delhi delhi how is the weather

40:58

this is the bridge in these applications also right and you get an answer so user message assistant

41:04

response user asks the question assistant gives a response okay now if you go and ask the question

41:10

is it usually how are things usually around winters if you ask this question

41:24

now see this is not treated like an isolated mess question this is exactly what i'm talking about

41:31

so inside chat gpt also they have built this kind of a system they built this kind of a short term

41:36

memory context right so chat gpt also has built this kind of a short term memory context right so chat gpt also has built this kind of a short

41:40

memory where in this particular chat session whatever you're asking so if i ask this

41:44

question chat gpt will inherently understand i'm asking about deli because delhi

41:48

delhi's about how is that in delhi right now and if you ask the question how are the winters

41:53

usually if you know that i'm asking this specifically about deli if you're asking about deli

41:57

i do not say this but it knows this del because the the short term context is written so in this chat

42:03

session that is what we are talking about the short term memory the running chat history for the current

42:07

session now what about long-term memory what is the relevance of long-term memory long-term memory

42:13

is not that essential for today's session but long-term memory is something very similar to your

42:18

chat gpti-t if you remember i had mentioned this uh you know an earlier session we have got chat gpt

42:24

memories so chat gpt memories are an excellent example of long-term memory so this is like the

42:29

you know what we were discussing before that whenever you're chatting with chat gpt you ask a

42:34

question get a response ask a question get a response so uh

42:37

you know so whatever you're asking and whatever kind of questions uh you're asking in chat gpt

42:42

uh chat gpt always stores a memory of that conversation it always stores a summary of that

42:48

conversation this isn't the long-term memory and it is stored as a vector db so this is what

42:53

long-term memory basically stands for the short-term memory is always in the current session the current

42:58

chat session this is what we will build in our uh this is what we will build in our session today

43:03

we'll build that particular short-term memory context in the session today today

43:07

and long-term memory is where you take that entire chat session whatever chat session you

43:13

went through you take that entire chat session you kind of summarize that whole chat session

43:17

let's say you you know the chat session lasted 10 15 turns what is a turn a turn is like user assistant

43:24

user assistant is that so one user assistant is one turn then another user assistant second third

43:31

like that okay so uh you take that entire conversation history that lasted 10 15

43:37

turns and you and that is how you kind of save the memory

43:41

that's that's that's that's one way to see we are not doing any

43:45

of sankeitha like memory uh memory here you know here you know here in

43:51

i'm just showing you like that you are not going to be able to build anything in chat g

43:55

because so chat gp t may already internally is happening but we are just trying to take an

43:59

example that whatever we are trying to do uh some inside the chat gpt you're

44:04

you're already able to see that in action but we have your chat session um

44:07

short term chat okay you asked a question

44:10

you asked after after

44:12

said follow up question

44:13

so in this current chat context

44:16

it understands what you're affecting

44:17

this short term memory and i just wanted to explain

44:21

what is long term memory long term memory is

44:23

implemented like this in chat typically who memories

44:25

so that is how it stores a complete profile about me

44:29

across all your chats whatever you have asked historically

44:32

that profile been and typically that is stored in a database

44:36

database and user profile this is what chat gpt does and so chat gpt in

44:40

chat gpti may a vector db banjata a database profile

44:43

and i think i showed you like if you see my memory some of my memories

44:47

so it has actually built a profile about me based on how what i search how i search so

44:51

personalization you can see reference memories it has actually built a you know

44:56

built a memory about me right so this is you know this is the context that's built about

45:00

overall okay okay

45:06

uh so ankit uh ankit to answer your question long-term memory basically means the

45:16

uh memory right correct correct absolutely absolutely i think you are you're you're on the right

45:21

so internally internally chat gpt can't the memories

45:25

that actually a vector db in store is correct you're absolutely right that is what it's

45:28

referring to correct but chat gpt i'm just giving an example okay so you know you cannot do

45:34

anything here this is the built-in application but

45:36

if you want to build something in your own application then you'll be doing it this way okay

45:41

so you'll be uh correct getting the same in-memory rag voila cheech which i discussed in a prior

45:46

session it is similar to that okay now let's come back let's come back to this so again the

45:52

the context of the class is focusing on short-term memory long-term we will circle back at a later time

45:56

not for today's class but i just wanted to discuss what it is so that people know the difference so

46:01

whatever we will see today it is only restricted to our current chat session okay

46:06

now now what do we mean by a conversation history from history

46:12

maintained as a current short-term memory may have

46:15

now the question is okay fine we will maintain history but who history

46:19

what are we going to have in the history well very simple uh

46:25

we all know the we all know the format of a prompt user message assistant message

46:30

and system message okay if you look at it in the correct order and final system

46:34

then user-fit assistant system message first then user assistant user assistant

46:41

like that it goes right so system message are the hidden rules user message is the analyst whatever

46:48

as an analyst whatever question you are asking and assistant response is what the assistant responded

46:54

that that so very important this is how you will maintain the conversation history

47:04

right so you will have to uh see this kind of kind of like this is how we will

47:09

maintain the history using a simple list in python so quite literally we will use a

47:15

simple list in python or one list use

47:18

that we can use because if you so if i go and maybe just copy this particular

47:23

uh code chunk and if i just share this with all of you okay i'll just call it general because

47:31

these are these are things that you know you don't have to like execute as part of the larger

47:35

context just just for some general demos i'm trying to show you yeah your history list is okay

47:40

this is just a small example how the history will be created okay in a smaller way so history is the

47:46

list in python okay and what you do first you will have a system message

47:51

so system message you're right role system message will be there and then you will say okay

47:58

role user and content is the user message and role assistant and the content will be this

48:08

okay yeah your assistance response i'm just trying to simulate this manually right now

48:13

but when i build the complete solution you will see that this will be

48:16

eventually done by the system so this is how you will have to append

48:20

we'll make history list

48:21

and we'll list in the list in the list in the system user assistant user assistant user

48:28

assistant like that will happen and at the end of it on you will be able to see what that

48:32

history uh what that conversation history looks like if i run that code if i run that

48:38

code you will see this is how that whole you know how that whole history object kind of

48:42

looks like that history object completely looks somewhat like this

48:45

you're all user user assistant

48:48

role user assistant and and

48:50

and there up up there a system over there

48:51

there's system here

48:52

okay so we can maybe ask jemini to uh

48:55

put our system message also here okay so we can say that okay

48:59

in this uh in this

49:04

in this history in this history uh

49:06

equal to uh list

49:10

please start by appending a

49:15

system message basic one so just to kind of kind of kind of show you how it is okay

49:25

that's a very good question okay that's a very good question how whato whato uh very good

49:30

question so that is very important so that's the reason why it is uh you know uh it's extremely

49:34

important that you uh you go ahead and ensure the uh you know you're you're actually

49:40

having uh some kind of a persistence model persistence model persistence i will talk about that also

49:45

so you're your list you're you can absolutely go and persist it in a jason file so that

49:50

that memory is stored somewhere because whenever you're doing in a list what is

49:54

happening is it is stored only in the session it is in the runtime but if

49:58

if a collab banded for some reason it crashes you will not be able to get it back so that's why

50:03

another recommended approach is instead of storing in a list in python you actually save it into a

50:07

jason file now then file in it's okay that's been hallucination is a general problem um okay that is a

50:14

a general problem obviously okay so let me done this uh q and day system message so system message

50:21

i can just hard code it i don't no need to just uh write it here so let me just hard code it

50:28

just a second guys system message will be you are a basic assistant okay i'm just

50:32

trying to kind of simulate a demo you are a basic assistant your your system message

50:37

okay what's that not able to see questions posted

50:41

ha ha yeah so when you're asking a question can you please in the chat can you go ahead

50:45

and just uh message everyone so very good questions everyone's asking so please message

50:51

everyone okay okay so okay so you're you're you're clear you're clear okay do let me know okay

50:58

just just ask your questions to everyone okay so other participants will also feel engaged

51:02

so when you ask questions everyone can see so just uh in your chat sitting when you're sending the message

51:07

please send to everyone okay so everyone will be able to see we will also be able to see

51:11

okay so now uh so let me run this history equal to list you're able to see

51:20

this you're an empty list first empty list we'll start

51:23

system system message you're a basic assistant and these are a user

51:29

you will ask a question and assistant will generate an answer here

51:32

i'm simulating this for you but in reality the assistant will generate this answer okay

51:37

again next follow up user asks the question assistant will generate an answer okay

51:43

i can ask one more final uh history up in after turn three so yeah to care jemini

51:49

cari think if i run the code jemini should be able to figure out what i'm asking let us see if

51:54

is able to figure out so i will say after turn three okay after turn three let us see if it's able to do

52:03

it i will i will say after turn three let us see if it's able to repeat after turn three

52:08

okay it's not even to actually if i need to just type a couple of clicks so user uh append

52:15

i will just quickly keep with that and i will enter a roll

52:21

roll and okay now it's able to figure out you can i will just correct it a little bit here

52:26

for all of you can i'll just correct it little bit here so i will just append the user message because this

52:33

assistant response we will we will want to say so then uh here i will ask what about uh

52:38

what about 2024 people what about 2024 and here guys let's say i'm getting a ballpark answer

52:45

i'm just going to you know just going to go ahead and let's say uh let's say the answer is coming

52:52

up to be teslas annual when it's um i'm just giving an answer let's say 16.77 whatever

52:59

86.7 so i'm just giving an example so this is how the history will be

53:03

maintained going forward can you see this is exactly when i i'm just wanted to break it up because

53:08

what we will see is a complete code solution so my objective is to just break it up and show you what we

53:13

are trying to achieve so first first a empty list lengen when we

53:16

we'll obviously have a system message for the rag

53:21

ragg's a system message raga and then user asks the question assistant gives a response

53:28

okay us after user asks another follow-up question assistant gives a response

53:33

This is your context. Again, user asked the question and just wanted to show you what that

53:39

complete conversation context looks like. This is your complete conversation context right now.

53:45

Now the interesting part is when you imagine you're in this, this phase right now, okay,

53:51

it is like, uh, just to give you the idea to you, you, you when you the radio

53:56

demo will you, this your chat interface will right?

54:00

Before you asked, some questions and the assistant

54:03

has an answer, this is user, this is, user,

54:06

user, they could some questions and assistant

54:07

did answer via. As say, you ask the

54:11

question here, you know, model gives the answer here.

54:13

You ask the question here, model gives the answer here.

54:16

Two, two such iterations have happened.

54:19

And now you are asking the question, what about,

54:24

what about 2024?

54:27

You can just find to help you visualize this a bit of.

54:29

When you ask this question, when you hit the enter, what will happen?

54:34

What will happen?

54:34

You're making the API call.

54:37

Wapashe, it's a rag going.

54:38

Now, here is the interesting part.

54:40

Abh, when rag is

54:41

this is not the only user message that is getting fast.

54:45

The entire conversational context is getting fast.

54:49

Okay?

54:50

So this whole conversational context is getting passed to the rag system.

54:54

You get the answer to the system.

54:55

So system, user assistant, user assistant, the whole context is getting past.

54:59

This is that complete prompt. Just to clarify the only. So this is what is meant by the history context.

55:07

Okay, I hope everyone is clear. We will be seeing this, you know, a little. And obviously, what is a

55:13

very common mistake sending only the latest message to the model? We will not do that because

55:17

we will be going and updating the history. After turn one, we will append. After turn two, we will append.

55:24

Whenever the assistant generates an answer, we will append it back to the list.

55:28

Okay, user will ask a question.

55:29

Assistant will give a response. Whenever we get that user assistant pair, we will append it back to the list.

55:35

Here we say user asks the question. Assistant gives a response. Whenever that happens, we will append it back to the risk. And that is how we maintain the context.

55:44

Okay. So you can see history is a Python list. It is easy to grow, save and need on. That's what we have here. So this is how the whole story will play out. You ask a question, get a response.

55:56

And when you ask a follow-up question, this whole thing is there in the context.

55:59

this whole thing is in the context. So now what is happening?

56:03

Now, let's say you have to answer this. So this whole thing

56:07

your kind of a kind of a user message has to, okay? So you go back to the RAC system

56:11

and you pull the retrieve chunks from the VEVector TV based on this entire user query.

56:16

Now the user query used over, this is your complete user message.

56:20

User message is not just and in 2020.

56:23

Now user message will be the complete context.

56:25

Yeah, your whole context lo. With that entire context, you go back to the vector.

56:29

TV, look up the relevant chunks, and get the answer. So that is the benefit of

56:33

this particular conversational context. Now, this is the other thing that I was talking about.

56:41

In memory, lists vanish when you close the notebook. Right? What I was talking to Ankehah

56:49

a while back. So abe, this is a workable solution. You know, this will get the job done. So it's a

56:55

nice way to understand the idea of it. This is a problem.

56:59

Look, this is co-lab. We've been talking about collab for so long.

57:02

But the moment I close the session, if you're a browser close

57:05

or if you run time, if you disconnect

57:09

here here if you disconnect the runtime,

57:13

whatever variables you have in the memory will go away, right?

57:17

So now, now, history equal to something we are able to see.

57:20

You're, come, and come, come, class in a collab open and you, type print history.

57:24

It will not remember, hey, history. How is how is it? No, this is in memory.

57:27

I think this is.

57:29

Only this list is existing only within this session.

57:34

Only within this runtime. It is in memory, RAM.

57:36

This is right now in your RAM.

57:40

So it is like, let's say, I open up a notepad.

57:42

We have a notepad open here.

57:44

And note pad open up, you know, I have some text

57:47

here. You can see, you can.

57:49

I've seen it. I've seen it.

57:51

Let me just start with up.

57:53

Hi, guys.

57:55

We are doing rag session today.

57:58

you have I'm like to type here.

58:00

Where is it?

58:01

Where is it right now?

58:03

It is in the notepad application.

58:04

It is in my RAM.

58:06

So this is saved in my RAM.

58:08

So if I shut down my system and come back, will I see the message?

58:12

You know, notepad right?

58:13

There's no, no, save kind of.

58:15

I need to go and save it, right?

58:16

This is what we do.

58:17

If I try to go back, it says, do you want to save it?

58:19

I'll save it.

58:21

Right?

58:22

So same thing.

58:23

If you look at a list in Python, these are all in-memory things.

58:27

They are not.

58:28

saved. So we have to go and persist.

58:32

What is the meaning of persist?

58:34

Persist basically means you want to save this to a file and you want to reload it on the next round.

58:43

So change what is nothing different compared to what we have talked about here.

58:50

The story remains the same. The only difference is that we are trying to use a JSON file instead

58:55

of a list.

58:56

That's it.

58:58

List to be in fact, simple, simply demo we'll list in day.

59:03

But you can extend this and use a JSON file instead.

59:06

Jason file is nothing but a file that you will create, okay, a file that you will create.

59:12

And in that particular file, you'll be storing the user message assistant response,

59:17

user message assistant response so that it is there even after your session disc alerts.

59:22

That JSON file is there even after your session disconnects.

59:26

You can say it is, so that's the that's the whole.

59:28

context. And this one way of this can't. So you can a Tesla chat history

59:34

or JSON file. Okay. And what you can go back and do is you can effectively first you can dump the

59:41

history at every conversation turn up history go dump the same way that I was appending to the

59:48

Python list. Here we can, here we can go back and dump the history to the JSON file or load

59:55

kind of time I can load the history from the JSON file.

59:58

and we can print it out.

59:59

So that's the way how it works out.

1:0:01

So jason.

1:0:01

Dot dump is used to write the list to a text file and jason.

1:0:05

Dot load is kind of reading it back.

1:0:07

So here I didn't have to do it.

1:0:08

I was just appending to the list.

1:0:10

I was just retrieving the list and printing.

1:0:12

So this is like appending and this was like printing.

1:0:14

The same story we can do with a JSON file.

1:0:17

Okay.

1:0:17

So if you want, we can see a small demo with Gemini.

1:0:20

So replicate the exact same.

1:0:24

Replicate the exact same.

1:0:27

concept as the previous two cells, this time, I want to save history not in a list, not in a list, not in a list, but in a JSON file.

1:0:57

So what was the thing that we looked at here?

1:0:59

We looked at JSON. Load and JSON. Dot dump.

1:1:02

Okay, so use JSON. Dot dump to write to it and JSON dot load to retrieve it and print it.

1:1:17

Okay, that's it.

1:1:18

Straightforward.

1:1:18

I think everyone's able to understand what we are trying to achieve.

1:1:21

So same story, whatever we did here, here here here, here we're just for JSON in here.

1:1:26

And you'll see when I run this code successfully, you'll be able to see that a JSON file will be created on my left-hand side.

1:1:34

Okay, this is different.

1:1:35

Don't worry.

1:1:36

This is a different file.

1:1:36

This is the different file.

1:1:40

But this is exactly how it will look like.

1:1:43

I think the code looks a little complicated.

1:1:48

So it's not very difficult.

1:1:49

If you know, you know, that history backer to do it's a little bit better.

1:1:54

But you can take a look at it.

1:1:56

Maybe I can run it through the code.

1:1:59

Okay, you can see we are using dev load history from JSON and depth save history from JSON.

1:2:04

In fact, I can try to simplify this code also if I want. Let's say, I'll simplify the code.

1:2:12

Just one second.

1:2:19

There are too many functions and all they're using.

1:2:25

Just show the.

1:2:26

basic functionality.

1:2:30

As you come into the advanced modules, you can also see that I'm encouraging the use of Gemini a lot here.

1:2:36

Gemini does not mean that Gemini is within Collap.

1:2:38

So please use this.

1:2:39

It will make you very effective in getting things done.

1:2:42

Because for the same thing, I'm not going back to Gemini or Chad GPD copying something,

1:2:46

pasting it back.

1:2:47

I'm doing all this within the Gemini inside Collap.

1:2:50

It is really incredible.

1:2:51

It will help you get a lot of these things.

1:2:54

Okay.

1:2:56

I think I mistake indeed or remove this.

1:3:00

I did a cancel by mistake.

1:3:02

Let me run this once again.

1:3:05

I will remove the function concepts.

1:3:07

So we can keep it, keep it very basic.

1:3:22

So this is the, I think this is the very simple.

1:3:26

Jason context that we are seeing right now.

1:3:28

All you want to see it to see.

1:3:29

Okay.

1:3:31

This is one second.

1:3:36

Okay.

1:3:37

You can, this is the history of basic history demo dot JSON file.

1:3:42

So demonstrating basic JSON save and load feature.

1:3:45

So we have a sample history.

1:3:46

So user asks the question.

1:3:48

You're a basic assistant.

1:3:49

And this is the user message and this is the assistant response.

1:3:53

So your list may have the story remains the same.

1:3:56

I have list so right now right now if you if you take a look at it

1:4:04

if you take a look at it system user assistant is there right now overall right and

1:4:10

this is the whole list that you that you have here same story as we discussed here

1:4:15

okay history is equal to a list you're offending the the things to the history list right

1:4:21

now so this part remains the same even when we see the complete drag application

1:4:26

user asks the question, assistant gives a response.

1:4:28

So list up history up and I'm not saying list will not be there.

1:4:33

And then periodically what you can do.

1:4:35

Apo list go you take that list.

1:4:37

Sample history is the list.

1:4:38

You take that list and you dump it into the JSON file.

1:4:42

So JSON dot dumps sample history.

1:4:45

Okay, JSON dot dumps sample history.

1:4:48

You're basically dumping this into the JSON file.

1:4:54

Okay.

1:4:54

And and what you are doing?

1:4:58

You can see.

1:4:59

WIT open, open the JSON file in right mode.

1:5:03

This is the path of the JSON file that we will be creating.

1:5:05

You open the file in right mode and you're saying JSON dot dump sample history.

1:5:11

That's it.

1:5:11

So history is safe to the JSON file.

1:5:13

So this part is where we are simply saving the history.

1:5:15

And this part is where we are loading the history.

1:5:18

So first part is you're taking the entire conversational context and you're saving it to the history.

1:5:23

And then what's after we are simply.

1:5:24

loading the history and printing it out.

1:5:26

So if I just run the code,

1:5:28

you know, this is like my file system.

1:5:30

Okay.

1:5:31

So here we don't have anything called,

1:5:33

you know,

1:5:34

we don't have anything called basic history demo or JSON.

1:5:37

So when we're run it,

1:5:38

you see, basic history demo or JSON can you see?

1:5:41

Basic History demo or JSON is scripted.

1:5:43

So I've demonstrated here how to,

1:5:45

how we have managed to retrieve the.

1:5:47

And if you want to see the JSON, I can download it for you.

1:5:50

I can show it to you,

1:5:51

that this is exactly what I meant.

1:5:53

This is exactly what I meant.

1:5:54

So this is what I meant by persistence.

1:5:57

If we're going to call out of my session,

1:6:03

the list will be deleted, but this JSON will be read.

1:6:06

So in the next session or in the same continuing session,

1:6:10

for whatever reason is the system shuts down.

1:6:11

I can always load it back.

1:6:13

So this is what I meant by persistence.

1:6:15

Persistence, you're persisting this in a, in the disk.

1:6:18

Now, now this may it's put in a disk.

1:6:20

And if you want to see the content,

1:6:21

we'll open it, you'll give it.

1:6:23

you can open it up in a notepad and you can see the contents of the jason.

1:6:30

So this is your jason content is.

1:6:33

Can you see, guys?

1:6:34

This your basic history, demote, or jason, whatever story we talked about.

1:6:37

You can it go to collab maybe open there's nothing actually.

1:6:40

I've done-loaded up to you, but you can it up to collab in even open to.

1:6:43

And you can see, basic history, demo, dot jason consists of this.

1:6:47

So we are beautifully persistent in the data right now.

1:6:49

That is what we have done.

1:6:50

I hope the concept is absolutely clear to you.

1:6:53

what it is. The story is the same.

1:6:55

List on stored on JSON based. So I just wanted to show you both the players.

1:7:01

Remember, in both the cases, you are doing short-term memory.

1:7:04

If long-term memory, then you're going to do that data-wise make.

1:7:09

I agree with you. I agree with you.

1:7:11

And you know, there is a reason why we give you the code-wala thing.

1:7:14

I know, see, and you see the reality of how things are.

1:7:19

If you ask me, even in my personal experience, when you go for interviews,

1:7:22

sometimes interviews do focus on some code.

1:7:26

That they'll ask you, what functions, what are how are doing?

1:7:29

So not hard, right?

1:7:30

I mean, see, we are using Gemini, but it's not very difficult.

1:7:33

You have to remember some things, obviously.

1:7:37

See, there is one thing that in order to get into the organization, they will ask you questions.

1:7:42

If you're in company, he will actually be using all this.

1:7:46

Because every enterprise today is making use of co-pilot, Claude, and all these things.

1:7:49

And I'm sure, a lot of your working professionals, you know it.

1:7:52

better than me, you already know it.

1:7:54

But that is, that is just how things are.

1:7:56

I know it, it's probably, but the reason why we are encouraging you to kind of get into the habit of

1:8:06

remembering some, you know, concepts is, you know, it is, you know, it is, it is, it is, it is, it is kind of, it is kind of to,

1:8:19

to help you know, to help you in those, in those interviews.

1:8:22

settings. Because there, you know, interview

1:8:24

to ask, that, sir, re-care, what

1:8:26

code, like, you know, everyone, even that guy knows it.

1:8:30

That you know, that you're using. That is useless.

1:8:33

Even that person himself may not be able to write what you are writing.

1:8:36

That, he will be able to write it. And that is the reality.

1:8:39

You know, it's the reality. But you have to push

1:8:41

not have you. So entry level, these are, these are differentiators.

1:8:45

So why do companies do it then? You know, it is like, these are like success

1:8:48

differentiators. Maybe you can correlate it back to

1:8:52

some hardworking tendencies,

1:8:55

that, right, he's got, he's got codes

1:8:56

know, so this guy might have put some effort

1:8:59

compared to a guy who is just using genome to code.

1:9:03

So that's, he's just using genome to code. So this is like a

1:9:06

filter criteria. You know, you can this is like a filter criteria.

1:9:07

You can you know, so this is a very efficient way to get

1:9:11

a lot of things done.

1:9:13

Now you have to strategize your learning in a certain way.

1:9:17

So one strategy is that, from the interview perspective,

1:9:20

you're going to sort of, you know,

1:9:22

you have a filter criteria. Now, how is Bhaweig different from 100 other people?

1:9:27

This is the criteria. So you're a little bit,

1:9:30

you're going to. You're doing. You're two line of python dig

1:9:32

away, history methods.

1:9:34

What Germany said is, that, he can't do

1:9:36

that, that's not can't do. If you give it, that person will know nothing.

1:9:40

He has variable even

1:9:41

not, he, equal to 5 print, or anything. So

1:9:43

the interviewer's seen in there, it will just be able to

1:9:45

say in the same way to understand. And the guys are very liberal, you know.

1:9:48

Sorry, the guys are very linear.

1:9:50

Lineant.

1:9:52

So it's not that if you get stuck on something,

1:9:54

they will absolutely penalize you or something.

1:9:56

They will understand.

1:9:57

If somebody is good enough in coding and somebody is

1:9:59

an architect level person who is doing this day in day out,

1:10:02

you're asking you, then you'll say it's in

1:10:04

the same way to say, he can't be able to know that.

1:10:07

So that is the whole idea.

1:10:08

It is purely a filtered criteria.

1:10:10

So one approach is for your interviews, definitely.

1:10:13

You're both code.

1:10:14

You're a little, memorize,

1:10:16

I know it doesn't make sense.

1:10:18

It doesn't make sense and I'm totally with you.

1:10:20

But the reason we are done.

1:10:22

doing this is only from the interview for us.

1:10:24

This companies just say it is like back to our CBCAC class stay and ICAC.

1:10:29

And now, now, what, history, what, what, what, what,

1:10:31

what's history in what, what happened, who came, who were, who king,

1:10:34

who, who, Raja, Rani, what?

1:10:36

What is it?

1:10:37

If you look at today's context of Chad, GPT, how does it help?

1:10:40

If 1814 in what, or what, or 1970, what?

1:10:43

Does it make any sense?

1:10:44

So, yeah, I mean, maybe, you know, we built some context about India, geography.

1:10:49

Some things are important.

1:10:50

But maybe something important,

1:10:52

We didn't have to memorize so many things.

1:10:54

But we still had to pass in the exam.

1:10:56

I've also studied, I've also studied history, you know, geography, chemistry, all these in my case.

1:11:02

So we all have gone through that process.

1:11:04

And, you know, before our engineering, college exams, we have all gone through the process.

1:11:09

There are some subjects.

1:11:10

We know, it's useless, it.

1:11:11

That no point there, but that still, you know, you're the first day,

1:11:15

and you know, you know, that you know, that you have, you know, that you know,

1:11:16

because companies in this is so we are, we are just following their standards, basically.

1:11:21

That's the reality.

1:11:25

I hope it will change and I think I am very optimistic it will change.

1:11:28

AI is leading to that change.

1:11:30

Because it's say assessments are more scientific.

1:11:34

But right now, to be very honest with you, companies don't have the best filter criteria.

1:11:40

It's many people have, there are so many applicants.

1:11:42

How do companies differentiate one person from the other?

1:11:46

And AI in it's a fraud going to.

1:11:47

Because how many people do what do you do?

1:11:49

You know, what do you know, do it's not.

1:11:51

So, how do you differentiate?

1:11:55

So these are the ways to differentiate.

1:11:56

We go back to the basics.

1:11:57

Like the CBSC-V-S-E-Wall that was.

1:12:00

So the government had a very nice, you know, they had a good noble thought.

1:12:03

Okay, you're, you're like, you're like, but whatever,

1:12:06

that's probably, that's probably frauding.

1:12:07

So they go back to the basics.

1:12:08

Back-to-bas, you know, tell, pen and paper.

1:12:10

That's, now, you know, now you'll, you'll be surprised to know a lot of companies do that.

1:12:15

That pen and paper exams try out there.

1:12:17

No code, that's nothing, you know, in pen and paper in.

1:12:19

And what's read-in-in-paper-in-paper.

1:12:21

What's going to be, it's a blank paper.

1:12:23

So, immediate filter out.

1:12:26

So it's very easy for the companies.

1:12:27

You know, you get 50 people lined up for a walk-in interview.

1:12:36

50 people, let's a blank sheet of paper, say,

1:12:39

or program, look.

1:12:40

50% of 49, not will write.

1:12:42

One man, let's, let's say, there's some in the syntax in garr,

1:12:44

there's something, something to write them,

1:12:46

some to, a algorithm, link to,

1:12:47

at, at least, if I ask people in the class,

1:12:49

that, let's a porridge loop,

1:12:50

that you'll be, but believe it or not,

1:12:53

most people,

1:12:54

he's for Forish Loo,

1:12:55

but at least at Masai,

1:12:58

that is not what we are having.

1:12:59

You know, we have prepared you in a way,

1:13:01

that's a time, say,

1:13:01

that you're, you're going.

1:13:03

It's a differentiating filter criteria, right?

1:13:08

Chalo, very nice questions.

1:13:10

Okay?

1:13:12

Yeah.

1:13:13

So let's move on.

1:13:18

I hope everybody's clear.

1:13:19

So this was the context of the JSON.

1:13:20

While it is not that important for the class today,

1:13:22

but I just wanted to take you through it,

1:13:24

so that everyone knows it.

1:13:26

This is we append, after every few terms.

1:13:27

So this is the context behind what is persistence.

1:13:30

So we've seen two flavors in session in.

1:13:32

The first flavor we have discussed is,

1:13:35

yeah, the first flavor we have discussed is,

1:13:38

you know, where we are saving the whole thing in a list.

1:13:41

We're conversation history to list

1:13:43

and the second flavor we have discussed

1:13:45

is how we are saving the conversation history

1:13:47

to a Jason pipe.

1:13:49

Okay, we'll jump kreysm.

1:13:50

Every time the user asks the question and the assistant gives a response.

1:13:54

Every time we get that user assistant fair, we'll just go to jason and dump

1:13:58

and then.

1:13:59

And then after next, when session, we'll, we'll use it.

1:14:03

That's what.

1:14:04

So this is how we are looking at the workflow.

1:14:09

Okay.

1:14:14

And next, as I said, in the, in the multi-turn follow up, what are we going to do?

1:14:19

We are going to basically.

1:14:20

You can see right now, we are going to simply build the query from the history plus the new message.

1:14:28

So that is basically how the whole thing is going to happen.

1:14:31

So when we are going to eventually build that entire rag module, as I told you,

1:14:36

what is going to be different here?

1:14:39

Multi-term in what different here?

1:14:40

This user query will now contain the history.

1:14:44

If I have to show you here, so previously I was asking a question,

1:14:50

and we were retrieving the question.

1:14:50

relevant chunks just on the basis of the question.

1:14:53

There's nothing to same to same thing.

1:14:55

Now, you'll ask you, that will not just be the question.

1:14:59

It will be the history plus the query.

1:15:03

This whole thing is a resultant query.

1:15:06

It's just a lot.

1:15:07

You'll just enter.

1:15:09

Query enter.

1:15:10

You will combine that with the entire history.

1:15:14

History, matter, user assistant, user assistant.

1:15:16

As it, you know, all the question as far as far as the whole your history

1:15:19

user assistant user history.

1:15:22

So this whole thing is basically your combined user message.

1:15:27

And on the basis of that, you go and retrieve the relevant chance and you get in the ad and certain.

1:15:32

That is it.

1:15:32

Nothing will change.

1:15:33

It is just a small change that we will do in the rag workflow.

1:15:37

But you can see conceptually, it's all the same.

1:15:41

Straight forward.

1:15:42

So we already talked about how to maintain the history.

1:15:45

This we can do using a list.

1:15:46

This we can do using a JSON file.

1:15:48

So for simplicity, we'll list as far as to explain

1:15:52

in the code.

1:15:54

Jason, we've made a demo we've given.

1:15:55

Both flavors we'll discusses.

1:15:57

But list is so easy to relate to.

1:15:59

You can see.

1:16:00

So this is our past a list will.

1:16:01

You are simply appending that query, user question, and this is your new combined query.

1:16:06

So this basis, you'll look up on.

1:16:08

Retreat the chunks and get the answer.

1:16:10

So even if you ask the question, how about 20, 23,

1:16:13

so he knows, it's based on, that relevant chunks, get the retrieved about.

1:16:16

So that's the, okay?

1:16:17

So that's the, uh,

1:16:18

That's the idea.

1:16:33

That's the idea.

1:16:35

It's persisted, Anke, I get it.

1:16:36

That's, well, that, well, that, well, that's, you know, that's your same concept.

1:16:41

Chat GPT, Japan, you, you can any, you can't, you can't, any, any, any, any, chat

1:16:44

trade predate, open to.

1:16:45

Same idea, no.

1:16:46

Your, your history is, that your user profile.

1:16:48

same thing, you can't say, so same thing, not only co-pilot,

1:16:53

but even if you're chat GPT in here, so here, like, our Germany in many

1:16:57

many chats are, our chat in GPD in many chats.

1:17:00

Okay, so chats in, when I go to my chat history, so same story, like, chat history is same story.

1:17:06

Okay, same story, so here here we're, we're the same thing, so you can, you can go back to this

1:17:12

chat thread, I can go back to this chat, daily weather update, I'm, we've seen, you can see, I can

1:17:16

open up the chat thread.

1:17:18

So the moment I do that, now, now, internally, its management is different, how they are doing it.

1:17:23

So, web application is a different framework point together that they are using.

1:17:26

But moment I load this, and the moment I start typing, back to the same basics,

1:17:32

this is our history here, okay?

1:17:34

So the same idea gets applied.

1:17:36

So now, if we're after, if we're going to, it is appended to the history, and based on that, LNM is called.

1:17:43

Okay, so the idea is the same.

1:17:46

Okay, so now, guys, guys.

1:17:48

we will come to the, come to the demo.

1:17:55

So we've already here to look at the, in terms of how to build a single turn rack.

1:18:00

So we already build this one.

1:18:02

And now, whatever we have discussed, we will now incorporate memory in the code.

1:18:06

So we will look at the portion now, how to incorporate memory in the code.

1:18:11

So we'll see that.

1:18:13

Hello.

1:18:14

You guys want to take a short break and come back?

1:18:15

We can take a five to 10 minutes break and come back.

1:18:18

After the break, we will see this part.

1:18:20

And guys, all the contents are part of your 9th June folder.

1:18:24

So Tesla annual reports and Tesla enhanced.

1:18:27

So this is the 9th June folder where the contents are uploaded.

1:18:30

So we'll circle back into the break.

1:18:31

And whatever concepts we have been discussing on this way,

1:18:35

we will incorporate all these concepts from here onwards.

1:18:38

Okay, this is our our here here here here.

1:18:40

So these are the few course snippets and we discuss in post.

1:18:43

Okay.

1:18:44

See you back in now.

1:18:48

Thank you.

1:19:18

Thank you.

1:19:48

Thank you.

1:20:18

Thank you.

1:20:48

Thank you.

1:21:18

Thank you.

1:21:48

Thank you.

1:22:18

Thank you.

1:22:48

Thank you.

1:23:18

Thank you.

1:23:48

Thank you.

1:24:18

Thank you.

1:24:48

Thank you.

1:25:18

Thank you

1:25:48

Thank you

1:26:18

Thank you

1:26:48

Thank you

1:27:18

Thank you

1:27:48

Thank you

1:28:18

Thank you

1:28:48

Thank you

1:29:18

folks.

1:29:25

folks.

1:29:26

Welcome back.

1:29:27

Welcome back.

1:29:28

Let's

1:29:29

Let's continue on

1:29:30

Let's continue on

1:29:32

let's continue on from, from, you know, from from, you know, from from, you know,

1:29:48

where we stopped and now we'll incorporate the memory.

1:29:51

Whatever we talked about, we'll try to integrate this into our Tesla Rack application and build a complete full pledged application here.

1:29:59

So let us see that.

1:30:03

So first we will instantiate this conversation history list, right?

1:30:08

So this is what we will do right now.

1:30:10

Role equal to system and content equal to system message.

1:30:14

Now what is the Q&A system message.

1:30:17

the Q&A system message I already had here. This is a normal Rack system message.

1:30:22

So we are going to eventually build the conversation history. So first thing I have in the history is

1:30:26

nothing but the system message. That is the first thing I have here. So this is what we have

1:30:35

done. Memory initialized and current state of the conversation history is system, you are

1:30:42

an assistant to a financial services user firm who answers user queries on.

1:30:47

annual reports. And this is the, I mean, the complete message. I mean, so we are

1:30:51

only printing the first, you know, few characters. You can see that right now. Okay. So this is

1:30:56

the complete message in the conversation history that we have right now. Okay. All of you are

1:31:01

able to see that. Now what I will do, user asks a specific question. You can user will ask a question.

1:31:09

Let's say the user query is, this is the variable. User query is what is the annual revenue in the year

1:31:15

the 22. So this is what the user is asking. And based on that user query, what will

1:31:21

we do? We talked about that. The single turn rag that we discussed, if you remember, we will use

1:31:25

a retriever, retrieve the relevant chunks, build the context. And this is that entire user message

1:31:32

context that we are having. So what is the user message for a rag? It is the original question

1:31:39

and the retreat context. So the user message will consist of the original user query one.

1:31:45

and the retrieved context. This is the user message. And this is something we will add

1:31:54

back to the conversation history. Very interesting. A conversation history already had the

1:31:59

system message. And whatever the user asked, based on that, we retrieve the chance.

1:32:07

We have the user message now and we will append it back to the conversation history.

1:32:13

And this conversation.

1:32:15

conversation history that we are having, this becomes the input to the LLL. The prompts that we will write to the LLN. So what does the language model see now? It sees the system message. It sees the user message. And based on that the language model will give an assistant response. And whatever answer one is coming, if you see, whatever answer one is also eventually added back to the conversation context. So that conversation

1:32:45

history initially started with just a system message. Then the conversation history

1:32:49

had the user message, append user message. And then finally the conversation history, we are appending the

1:32:55

assistant message. The same story we were discussing before. So we are, we just trying to put this

1:33:00

into a beautiful, you know, flow right now. So that is what we have done. And I think you can see this

1:33:07

one, you know, so we can take a look at this. This is how the whole system will work out right now. This is the

1:33:13

real thing that is getting retrieved. I'm running the code here. You can see the user asks,

1:33:17

what is the annual revenue in 2022. And it will retrieve the context and the assistant answer is this.

1:33:23

This is the normal thing. But what is the, how is the, what is the current state of conversation

1:33:27

history? The conversation history previously was this. And now the current state of

1:33:32

conversation history after the single turn, one turn has completed. You asked a question, you got a

1:33:36

response. And after this single turn, the conversation history consists of this. This is what

1:33:42

it consists of system, system message, user, user message, assistant assistant response.

1:33:47

That is what it consists of. Now we will see the second term. You can remember the conversation

1:33:53

history is already saved in a list. If you want, you can repeat the same story with a JSON file. I

1:34:01

already showed you that piece. The lists are not permanently saved in the disk, right? So you can do

1:34:06

the same thing with a JSON file as well, as I told you. Right now, next I will initiate turn to

1:34:12

the user asks the follow up question. And what about the year 2023? And notice we did not mention

1:34:23

revenue explicitly. Now this is user query two. Because the story remains the same. Based on the user query,

1:34:30

you retrieve the relevant chunks, build that user message. What is that second turn user message for the

1:34:36

system? It will be the context and the query. And we are appending that to the conversation history again.

1:34:42

The conversation history already had system user assistant from the previous term.

1:34:46

And now in the new turn, we are appending this new user message to the conversation history.

1:34:52

And here is the interesting part. Here is the interesting part. When you're making that second

1:34:57

drag fault, here is the interesting part. You are passing conversation history as the front.

1:35:03

That's the interesting thing. That's the really interesting part. So now you have the system message.

1:35:08

user one, assistant one, just for simplicity. And you also have user message

1:35:15

too. Because remember, I have, by now, I have already appended user message to my conversation

1:35:24

history. This entire thing becomes the prompt to the response to. So now when the LLM is

1:35:31

seen, you know, when the language model is seen that prompt, it is seeing, okay, what happened

1:35:37

before and what is my current user message? Now the user is asking this question and based

1:35:43

on that we are retrieving the relevant chunks. So that is the way how it is able to, you know,

1:35:49

understand this particular context. We're able to build this memory. Okay? So, so the language model

1:35:57

has, you know, has the intuition, it has the context in terms of what is happening. We get the answer.

1:36:02

You can see we are getting the answer right now. We're getting the response.

1:36:07

This is the answer to we are, we are getting back and we are appending it back to the

1:36:13

conversation context. We are appending the answer back in the conversation context. And here, just for

1:36:19

simplicity, we are trying to show, we are trying to show how the, how the response looks like. You

1:36:25

can take a look at it. This is now the whole conversation context is getting built now. System, user

1:36:30

assistant, user assistant and so and so and so forth. So that's how the whole context is getting

1:36:36

things. The LLM remembers the whole context. It remembers the entire entire context

1:36:42

overall. Okay. Now, we will quickly go and instantiate this in using radio. And absolutely,

1:36:52

I think, Uncle, that's a very good point that you raise. So will the tokens not get exhausted

1:36:57

if we do this, you know, when that is a, that is a serious constraint, obviously. The token, you know, but,

1:37:04

but one of those strategies.

1:37:06

that we use, if you ask me that, sir, in real world, what do we do? What do we do in the real world

1:37:11

so that the tokens are not exhausted? In the real world, what we do is we try to, you know,

1:37:16

we try to effectively, you know, kind of, one of the ways how we do it is we try to effectively

1:37:22

summarize, keep summarizing it. So let's say, you know, if you have this entire conversation history

1:37:30

right now, let's say if you have this entire conversation history right now, what we will do is, we will do is,

1:37:36

will not just keep appending to the conversation history, but after every four, five

1:37:40

turns, what we do is we take that entire history, we pass it to another LLM, and we summarize that

1:37:47

history. So if the entire conversation history is, let's say, 20, 30,000 tokens, we can summarize

1:37:52

and compress that into only 500 tokens. So summarization is a, is a very important thing that we keep

1:37:58

doing along the process. So that is one way we can, we can manage the token limits. But remember,

1:38:03

of multi-turn conversations, the token limits are usually going to be high. Otherwise, have you,

1:38:08

have you imagine, can you imagine in chat GPT, you ask a question, get a response. Again, ask a

1:38:12

question, get a response. It's so big. If every time you're passing that entire context, it is so big,

1:38:17

the chat GPT also does that summarize it. So, you know, we think as if the whole thing is getting

1:38:21

passed, but the whole thing is not getting past. Only the summary of this is getting past.

1:38:26

Okay, Ankit, I hope you're clear. Does that question get answered? Yeah.

1:38:33

Okay, thank you. Now, coming to the radio part, the radio part remains the same. Nothing is different here.

1:38:40

Only thing we are doing is we are, you know, we are putting the whole story together. You know, that's what we are doing.

1:38:48

So we are defining the rack Q&A function. Inside that Q&A function, we are passing the message.

1:38:55

And this is what it is. Same thing. Whatever I was explaining this, you know, in a simple way, now we have put this whole thing inside radio.

1:39:03

inside function. So because it is in my functions, it might look a little complicated, but it's not. It's very

1:39:08

straightforward. You can see we are passing the message. So first, based on the user message, user message is getting

1:39:15

passed from here, right? User message is getting passed from here. So based on the user message,

1:39:21

you are, you are effectively, you are effectively retrieving the relevant chunks and you are framing the

1:39:30

user message, which is the original question and the retreat context.

1:39:37

Now what you are doing? You are appending to the messages list. So role system,

1:39:44

even they rack system message. And this is the for each loop. Okay. And you are continuing to

1:39:49

append. Okay. You're continuing to append here. User is this and assistant is this. Okay. You're

1:39:56

appending this. Okay. Okay. And this is that whole.

1:40:00

user message that you're having. And finally, this is that LLM call that we're making

1:40:05

inside a try except block. So why are we using a try except block in Python? What is the reason?

1:40:09

You might have seen this a couple of times I have done this in my sessions. Like, in fact,

1:40:14

in your Python sessions, you might have seen error handling to some extent. The reason is because

1:40:19

if for any reason, if for any reason that the API gives any problem, if I get an error in this

1:40:28

particular block for any particular reason, the application will not error on.

1:40:33

Application can't be any number of reasons. It could be, it could be, let's say you went out of

1:40:39

tokens or you are using the GROC API, GROC is down. Okay, or you exhausted the limits,

1:40:44

the free limits, the free T or whatever. So you're doing a client chat completion's create and for

1:40:50

whatever reason that code gave an error or the input format was not in the right way or whatever. So even if

1:40:58

get an error, the application will not error out. It will go to the accept block. It will

1:41:03

simply print out that error message for you. So that is the basic error handling that we are

1:41:08

incorporating here. And then you're returning the prediction. And let us see. So all I did was I just

1:41:13

put this into the Gradio. That's it. So whatever I explained here, this is the main part. Here,

1:41:17

I just put it into the radio interface. Gradio is something I don't, I think before also I've mentioned,

1:41:21

don't try to get into the gradio part. It is just for small demos and POCs. We are using it. But

1:41:27

the actual front-end development port is something that will be done by a typical application

1:41:32

development team. So this is a very different skill set. Like building the front-end is a very

1:41:36

different skill set. Usually, you know, people use HTML, JavaScript, CSS, these kinds of

1:41:42

skill sets are used. And the very broad technical course category for this is the full stack development

1:41:47

course. Masai also has a full-stack development course where we actually teach you how to create

1:41:51

applications or applications. Okay. So Gradio is just like a, you know, just like streamlet. I think in your

1:41:57

Python sessions, you have done streamlit. So Gradua is something very similar to streamlit.

1:42:01

It is a framework in Python that is used to create these kinds of simple web applications.

1:42:06

Very useful for these POCs or demos kind of thing. Now, we can see the demo here right now. So

1:42:12

what is the annual revenue? What is the annual revenue in the year? In the year

1:42:22

what? 2020, we can ask the question and we're expecting the assistant will generate

1:42:30

the correct answer. Okay, so this is what we are able to see. So based on the question, we are

1:42:34

indeed able to see the correct answer. Okay. So we can again, now the best part is that we can again

1:42:39

ask a follow of conversation. And even if I ask a follow of conversation, this entire history

1:42:43

would be taken and based on that the, you know, the response will be given. That's the basic idea

1:42:49

of his assistant. The next demo, what I have done,

1:42:52

I have done the exact same thing, but this time I have, you know, built it using the JSON. I have used a JSON configuration. And there are a few other things I've done. A couple of other things that I've also done, which I haven't talked about. Okay. So we have seen that two-turn follow-up activity right now, how we are able to query the Tesla thing. The final piece of the puzzle that I'm talking about right now is loop termination. Very important. See, otherwise, what will happen if you see this particular interface right now. How many, how many, how many, uh,

1:43:22

are we going to go, right? You ask a question, get an answer, ask a question, get an answer, ask the question, get an answer. It's infinite, right? It keeps going on and on and on and on. But as you keep going on and on and on, the conversation history builds. So the applications will become very demanding, right? So you must have a exit condition, a stopping condition. Just like, you know, if you in Python classes, you would have, you would have learned about something for each loop, wild loops, right? And remember when you discuss four.

1:43:52

for each and while loop. You must have discussed something called a break, a break condition, break and continue. That's the same idea. How do you break out of the loop? If a certain condition is satisfied, how do you break out of the loop? I don't want the loop to run infinite loop. You know, like, how do I put it? In Python, for example, this is an infinite loop, right? If I say while of true, if you do this, I mean, I'm not going to run the code, but if I do this, my code, you know, the collab will crash, actually. Because if you say while true,

1:44:22

it will continue running. It will not stop. The cell will continue executing. But how do I put an exit condition? How do I ensure the thread actually stops? And that is an important aspect of what we are covering here. How do we give those stop rules? So, and this is applicable in many cases, right? If you think of an ATM machine, you try three times and if you three incorrect attempts and the machine will say, okay, I'm sorry, you try again tomorrow. There are explicit exit conditions everywhere.

1:44:52

If you look at many real world scenarios, there are exit conditions that are used everywhere.

1:44:56

You try to log into your internet banking.

1:44:59

If you, I think two, three times, if you give the wrong password, the system locks you all for 24 hours and 48 hours.

1:45:05

It asks you to call customer care.

1:45:07

Is there exit conditions, actually.

1:45:09

So same way, I should have some kind of a condition here also.

1:45:12

The user should not be able to indefinitely ask a question, get an answer, ask it.

1:45:16

No, but there should be some exit conditions.

1:45:18

Right? How do we do that? How do we go out with it? Let's see.

1:45:22

So we can go and use something called max steps, right?

1:45:29

Or we can explicitly write a logic where if the user types, quit, exit and stop, the loop will automatically break out.

1:45:40

So this is the logic which I've incorporated in my current demo.

1:45:44

So I have basically used two flavors right now.

1:45:47

One, I have incorporated the concept of max steps, which I'll show you.

1:45:52

I'll show you how, what code have written.

1:45:54

So one, I have incorporated the concept of max steps.

1:45:58

The max steps concept have incorporated.

1:46:01

And second is I've incorporated the concept of stop words.

1:46:06

That means I'm explicitly saying if you, if the user enters exit, tweet and stop, the application, the rag application will stop.

1:46:14

So you can see that here, if I enter exit tweet and stop, automatically the assistant will respond.

1:46:18

Thank you for chatting with you.

1:46:19

It will no longer go and do a rag look up.

1:46:22

So in all these cases that we go and do a rag look up.

1:46:25

But the moment I enter, exit and do it and stop, it come out of it.

1:46:29

come out of it. That's the intuition that I wanted to build here.

1:46:32

three new things that we are doing in this particular code.

1:46:36

be the final piece, what we are covering for today.

1:46:39

Max steps, how many maximum number of turns I want?

1:46:42

That is a hard stop.

1:46:43

It is like you ask a question, get an answer.

1:46:45

Again, ask a question, get an answer, ask a question, get an answer, ask a.

1:46:47

So there are total five such turns that we will do, hard stop.

1:46:50

After five turns, it will auto disconnect.

1:46:52

Okay?

1:46:53

Number two, we are allowing the user to give a condition.

1:46:58

Okay?

1:46:59

You specify whether you want to stop or not.

1:47:01

So the stopwatch, explicit stopwatch you have given.

1:47:06

And so these are two new things we are doing.

1:47:07

And finally, the third new thing we are doing is we are using a JSON filing stop.

1:47:11

We are not using a missed append, but we are instead persisting the conversation history in a JSON file.

1:47:17

That is how we are going about it.

1:47:18

Right?

1:47:18

I think I already have a conversation history.

1:47:21

So just for simplicity.

1:47:22

of the demo, what I will do is I'll delete the file, and I'm going to recreate it once

1:47:26

a second.

1:47:26

So I don't have a conversational history file right now.

1:47:28

I will create the history file, and I will keep appending to that JSON file instead.

1:47:33

The same way I was explaining, I'll simply integrate this in the code right now.

1:47:37

So first, I think we can run the application and show you what kind of results we are getting.

1:47:43

And this is the console application.

1:47:44

I'm not done this in Gradio.

1:47:45

This will run directly in my notebook, but you can obviously build a Gradio application also.

1:47:50

So this is what we are at.

1:47:52

explicitly are trying to do right now in this particular piece.

1:47:58

So now, moving on, let us go back to my console application.

1:48:02

You can ask the question, what is the, what is the annual revenue in the year?

1:48:09

What is the annual revenue in the year 2022?

1:48:12

You can ask this question.

1:48:13

And based on that, you can actually see the assistant gives an answer, $81,662 million.

1:48:19

The assistant is able to give the correct answer.

1:48:21

Okay, if you ask the question, how about 2023, how about 2023, the assistant will again give the correct answer,

1:48:29

96, 77, 7, 7.7, 3 million euros.

1:48:31

I'm not explicitly saying 20, but it remembers the context in this next call.

1:48:37

It is looking at this, it is going back to the, it is taking the entire conversation history.

1:48:42

It is going back to the vector DB, retrieving the relevant chunks and then giving me the answer.

1:48:47

And I'm getting the correct answer right here.

1:48:49

You can see that.

1:48:50

Okay? How?

1:48:51

about I don't have to say how about. I'm just saying 2024. Very vague question.

1:48:57

Even if I ask this question, ideally, yeah, I think it kind of messed up probably.

1:49:03

2024, I don't remember, do we have the data? Maybe we have to check that. But I think it kind of messed up.

1:49:10

Yeah, I think it did correct 10,000 close to that. But we have to check that. Whatever. I think I could

1:49:14

have asked it in a more eloquent way. But you can see if I ask the, even if I ask this kind of a question,

1:49:19

assistant is able to respond. So this is, this is, and now I think part of it will be about going and

1:49:24

tweaking the system message. Honestly, if you see my system message, system message is the same

1:49:28

system message I have used, but we can go back and tweak the system message to ensure that we are getting

1:49:33

more stable results. Okay, so these are a few tries we are doing. What if I say, what is the weather

1:49:37

in Delhi? What do you think the answer will be, guys? What do you think the answer will be? If I ask

1:49:42

this question, what is the weather in Delhi, what is the answer I'll be getting?

1:49:48

Anybody wants to answer?

1:49:49

What do you think I'll get? It's a rag system. Remember? This is our last week's concept we studied. What do you think I'll get? Will the rag give an answer? Exactly. I'd say, I don't know. She was excellent. It should say I don't know because it's taking that question. It's going to the vector DB, trying to retrieve the relevant chunks, but there are no chunks it is able to see about whether. It doesn't have any information about whether. Doesn't know. Okay. All good. Brilliant. And now what I will do? I'm

1:50:19

So if I run up to the fifth step, it will anyways close. But what I will do, I will use my stop words. One of my stop words is exit. If you remember, exit with the stopword. And if I hit exit, if I, if the user types exit, this is what I meant. In the chat interface, you type exit. And when you type exit, what will happen? The assistant will go. The loop will stop. The cell actually stop. The cell stopped. It came out of the loop. It broke out of the loop. All this while the cell was executing. The moment I hit exit.

1:50:49

The assistant responded exiting chat goodbye and the cell stopped. The chat session will end. That's what it means.

1:50:58

Okay. So this is the big picture idea how we, you know, how we design, you know, real applications.

1:51:03

I hope everyone's got a very nice big picture idea into what is going on. Right. Okay. So this is the final piece of what I wanted to talk about with all of you.

1:51:15

I hope everybody's clear. And finally, the last part and I'm with the, there was.

1:51:19

some questions people, people had, and a lot of you are curious, like, okay, Sian, how does this really work?

1:51:25

I think now you will relate to it. Now, this, I'm going to warn you. This is something outside the

1:51:29

session, and I just wanted to, like, spend the last five minutes giving you a very short sneak peek

1:51:34

into, you know, how this entire chat deputy architecture is working at a very high level. Can we skip the

1:51:40

rack processing or what is that? In the fourth step, can we skip the rack processing step? Or once we

1:51:45

use rag each time, it has to pass through the rack thing. No, you have to do. You have to do it. You have to

1:51:49

the right thing right okay okay sorry sorry you're you're talking about that part

1:51:54

sorry let me show the code uh yeah we can see that we can see that we can see that don't worry

1:51:59

you can see initially what we have done so this is the conversation history you can see so first we are

1:52:05

loading the conversation history if the jason is present jason dot load and if it is not in history

1:52:12

so we are you know we are we are inserting the system message they're loading the history

1:52:16

this is the safe conversation history we are doing jason dot dump

1:52:19

this is the same story i explained before jason load and jason down and this is where you are

1:52:26

giving a turn count remember on the maximum number of steps is five you're giving the turn count

1:52:31

okay and this is the condition that we have given so you know if the user input is in

1:52:38

stop words we are using a break condition so within the wild loop here is in a break this is

1:52:43

what i meant by the exit condition this is how that whenever i'm entering something which is present

1:52:47

within those stop words list okay whenever i'm entering any of these words it is it is it is

1:52:52

satisfying this criteria okay so that is what is going on behind the scenes okay and to answer your

1:52:59

question unkith in the fourth step can we skip the rag processing uh unfortunately remember

1:53:06

you have to still go through the rag because uh it will it will still go back to the uh the vector db

1:53:13

it will retrieve the relevant chunks and then the l lm will take a call whether it is uh uh

1:53:17

a relevant chunk or not a relevant chunk but huh i mean your point is absolutely valid maybe one another

1:53:23

additional logic that you can put is so if you ask me uh based on my code what have i done uh

1:53:28

based on my code i have not incorporated that i you know every query that you write eventually hits a

1:53:33

just to clarify that is my code logic only if you type only if you type if the user input is within

1:53:40

those top words it is it will break out of the loop any other user input you're hitting the rag

1:53:44

getting the response just to clarify but you're you're hitting the rank getting the response just to clarify but you

1:53:47

you have a very good suggestion you are saying sir i want to go and if a user asks this kind of a question

1:53:53

uh what you can do is you can now say you can now put another additional classifier loop

1:54:05

if you remember we have this is the classification l lm that we can have and the classification

1:54:10

llm will classify the query either as a general query or as a rag query or as a rag query

1:54:16

right unkid i hope that answers the question so if the classification llm classifies the query as a

1:54:22

general query it will go a normal generation generation response it will not hit the rag

1:54:28

otherwise it will do the rag so in that case if you go and ask this question what is the weather

1:54:32

in delhi the classification l lm will say it is a general query and it will give the generity answer

1:54:37

if you ask this kind of a question uh give me the answer for 2023 it hit the rag so you can

1:54:42

you can build it by including one more classification lm in the architecture

1:54:46

okay i hope that answers your query and click yes you will have to do it yourself

1:54:53

correct absolutely you'll have to design that logic everything will be the same only thing is

1:54:56

you will have to design this part the next time i user asked the question because see right now there

1:55:00

is no filter whatever user query is getting asked you are using that user query and hitting the

1:55:05

relevant chunks you can see they're straight away retrieving relevant documents with the user input

1:55:09

but now you can put a layer when the user asks the question we'll first classify is that a relevant

1:55:13

question only if it's a relevant question then we'll hit the

1:55:16

right else we will not you can use your own if else classification logic to handle that

1:55:21

that is something you will have to create no built-in way of doing that okay all right

1:55:27

we are just about in the back end of the session and i just wanted to maybe uh

1:55:31

just a quick two minutes i want to take here so uh what is actually going on inside a chat gpt

1:55:36

and oftentimes you know when you ask questions like uh you know for example if you go and ask uh

1:55:44

like you know so general questions you you might see the chat gpt somehow remembers it from

1:55:50

memory what you're asking right and i just wanted to demonstrate that to you let's say if i ask

1:55:54

a question how do i plan my work how do i uh plan my work more effectively and if i ask this kind of

1:56:02

a question what is going on behind the scenes so i am asking a question and based on that question you know

1:56:08

chat gpt will give a response it is not a normal generation that is happening it will first go and look up

1:56:14

from my memory long-term memory so chat gpt is memory maintaining two types of memory remember one is the

1:56:19

long-term memory which i showed you and second is the short-term memory that is the chat history okay

1:56:24

there are two memories it is basically maintaining moment i go and ask a question it is going and hitting

1:56:29

my long-term memory see it is saying remembering can you see says remembering it is kind of you know

1:56:34

it is kind of going and saying remembering okay it is it is it is remembering what all it knows and you can also

1:56:42

also look at the thought process can you see clarifying workloads and all of these kinds of

1:56:46

you know uh uh uh things and on overall you can see very very you know uh

1:56:52

interesting things you know it actually gives you a whole whole past chats and everything yeah

1:56:58

this is this is incredible how it's working and and i think i think just to uh just to clarify you ask

1:57:05

a question first thing that happens is there's a vector db and in that vector db this is

1:57:12

where the entire long-term memory is stored okay so think of it like memory one memory two

1:57:21

memory three just like how i showed you that entire embeddings are stored here so based on whatever

1:57:27

question you are asking it is also doing a something similar to a retrieval-oriented

1:57:31

generation just that we are not seeing that it's all happening behind the scenes but this is exactly

1:57:35

what is going on inside chat gpt this is the beautiful integration of whatever we have talked about in the

1:57:39

the class you ask a question and first it is retrieving from your long-term memory it is

1:57:45

retrieving the relevant chunks that you know based on this question what are the relevant chunks and based on

1:57:49

that it is giving me a generated answer and now coming to the short-term memory i can ask a

1:57:54

follow-up question i can ask a follow-up question i can ask a follow-up question and this follow-up question

1:57:58

will be part of my short-term memory so now it has the entire context of what i asked and in that

1:58:03

conversation thread now that whole thing will follow up just like the tesla demo that we did okay so just

1:58:08

just keep in mind that you know you know very real world application like a chat dpt how

1:58:13

both these memories are playing up but long term we will see at a later date when we come to agents

1:58:17

we will we will discuss how to build this in more detail but not right now but today we have seen a

1:58:22

very good flavor of what short-term memory is how to uh do the whole thing in a chat

1:58:28

conversational context and basically how all this uh you know ties to the big picture program

1:58:35

okay okay fine guys everybody's

1:58:38

clear all of you have a complete perspective of what is a rag now i hope everybody has like

1:58:44

clarity because you know the interesting part is we see these things on a day-to-day basis and

1:58:48

once you you know once you start to uh go into the depth of it you know and try to understand

1:58:54

it becomes very impressive you know so how it is managing memory so yeah and that's a good

1:59:01

question ideally it should not it's a free account that chat gpt is giving you i think you're

1:59:05

talking about chat gpt or the normal vector review so that is something you will

1:59:08

provision it accordingly so naturally you will you will provision it in a way where your

1:59:12

vector db does not eat a limit so you will have to provision it you will have to

1:59:16

constantly increase the capacity here this is the free account so chat gp open a i is

1:59:21

investing a lot of money to keep the service free for us so yes and and and one of the

1:59:25

ways how they are managing is the memory so they are continuing to summarize the things

1:59:28

remember they're not storing the entire chat they're not storing the entire history

1:59:31

but they're they're only storing a few tokens if you see my entire memory you open up your own

1:59:37

don't add gpt account is your memory what are the memories you have you only have few lines right

1:59:41

few tokens there is not much that is anyways getting used up okay okay great everyone's clear

1:59:48

others are all fine thank you rajid uh unkkaid has also asked lots of questions today uh

1:59:54

so others are all good let me hear from everybody everyone's followed the class today

2:0:07

okay all good guys i i think you should all feel confident about building the next chat gpt

2:0:16

at least you get an idea the chat gpt is not functioning in any different way so it should make you

2:0:22

confident in terms of how to build your own personal uh application with some memory you know it

2:0:27

can be a personal project and i always encourage like how you take these learnings forward and

2:0:31

how you do something on your as a side project as a personal project and please

2:0:37

please try to do that plan i think now you're all into the third module uh okay so please

2:0:41

try to think of some personal projects you know maybe uh take some interesting ideas and see hey

2:0:47

how can i use these uh snippets and notebooks that i'm sharing and how can you use this for some

2:0:53

personal projects something you know could be anything maybe uh you take your bank statements

2:0:58

and do something or you take your resumes and do something or you you have let's say you have a whole lot

2:1:04

of different documents in your system you've got resumes you

2:1:07

you've got income taxes you've got gst returns you've got health insurance reports

2:1:13

so many hundreds of pdfs you might see in your system build a rag application

2:1:17

intelligent rag application with memory and that's a great personal project that you can

2:1:21

uh showcase to your interviewers when you go okay okay uh that will be all from my end

2:1:28

thank you uh ev what what is that uh okay yeah okay okay thank you uh

2:1:35

okay thank you uh arsita over to you

2:1:37

and thank you guys uh good night to everybody uh and i'll see all of you in the next session

2:1:43

next session is very exciting we'll be getting into agents and just to kind of summarize

2:1:47

what we did uh just to again summarize what we discussed in the session today uh

2:1:51

so we were able to understand the concepts of what is memory what is short-term memory

2:1:57

versus what is long-term memory we were able to understand that we were able to

2:2:01

persist and reload conversation history across turns so we understood the concept of

2:2:07

Jason we also understood in long-term memory how we saved in a database so we saw that

2:2:11

idea uh loop termination conditions we use something called stop words max count we talked about

2:2:17

that and basically this was more like a a python centric concept a try

2:2:21

except block how you effectively if any mistakes are made this is not a gen a lLN

2:2:26

concept it's more like you know if there are any uh errors that the

2:2:31

API call makes the application doesn't error out but it basically goes and uh you know

2:2:37

kind of uh displays that error message overall so it is more like that try except

2:2:42

block that we looked at in position okay uh what's that what's that is some sort of

2:2:54

ha ha ha ha unkith absolutely history summarized what i meant is ha ha ha that code

2:2:58

on the code on that right so what it means is what it means is if you want me to show you a small

2:3:05

sample here they say manu you

2:3:07

let's say this is the history so imagine at any point in time you have a history so what i meant is

2:3:12

at every point in time you will keep a track after every four turns or five turns or you keep a

2:3:18

token counter you a token counter or a token counter or that token counter me track

2:3:21

how many tokens have we exhausted so the moment you exhaust a certain number of tokens what you do

2:3:26

you do your poor message do you pass it to one more large language model and you summarize it

2:3:37

text so system message and your summarized a context again that is the way how you do it

2:3:43

and you will have to manually keep a track okay this is something you will have to manually do

2:3:48

and this is a very common practice because if you think of chat gpte

2:3:55

chat gpte where there are you chat gpte you trade increases

2:3:59

some limit so like any imports not in chat gpt so can you imagine how long that conversation

2:4:04

context will be and this is free case open eI data how costly it will be for them to maintain

2:4:09

so this is something that they are doing in a big way

2:4:12

your gifes your first chat history has user assistant user that

2:4:16

that the whole summarized context in your new user message

2:4:21

and they keep doing that they use a token counter they're probably saying 500 000

2:4:26

token after every 500 tokens you summarize next 500 token you summarize so the entire message

2:4:32

should be max to max 500 tokens this is how you can you know maintain the

2:4:37

action

2:4:40

thank you guys once again okay i hope it's clear okay great so that so the contents are here

2:4:49

everybody can refer to it 9th june and yeah thank you guys good night good night to everybody

2:4:54

and over to our shiva yeah thank you thank you very much for the wonderful session students

2:5:02

the feedback poll is live also we will take a few minutes here to

2:5:07

run the code that was demonstrated today so you can go to the drive that is shared with all of the

2:5:14

resources you can open up the co-lab notebook and you can try running the code for yourself

2:5:21

and once you're done with this activity you can confirm in the chat box that you're done

2:5:37

you know.

2:6:07

Thank you.

2:6:09

Thank you.

2:6:39

Thank you.

2:7:09

Thank you.

2:7:39

Thank you.

2:8:09

Thank you.

2:8:39

Thank you.

2:9:09

All right, students, we will end the session here.

2:9:16

