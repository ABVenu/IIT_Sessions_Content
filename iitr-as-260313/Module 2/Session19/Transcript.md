0:00

Recording in progress.

0:30

Thank you.

1:00

Thank you.

1:30

Thank you.

2:00

Thank you.

2:30

Can you hear me now? I think the voice is clear, right?

2:34

Yes, Afsham, you are audible now.

2:37

Yeah, so yeah, I think we can get started.

2:40

So let's start with today's class.

2:42

What we will try to do is we will try to learn about rag.

2:45

I think the screen is also visible.

2:47

So yeah, one by one we will start.

2:49

Like it will be a continuation of whatever we studied in the last class.

2:53

Those things only we will try to do.

2:55

So yeah, one by one we can get started.

2:57

So let's start with the first part that we are having.

2:59

that we are having. So we can see here this particular part that like what is the problem with

3:04

LLMs like that part we need to understand and once we understand that particular part

3:09

then only we will be able to understand that wire rag is required. So one by one let's try to

3:15

see this like let's say that we are having this kind of assistant that is there. I'll just quickly

3:21

share the other screen and let's talk about this diagram. So we can see here that whenever we have

3:27

this kind of scenario let's face this screen short there so we can see here

3:38

this particular part that let's say that we are having a a shopping assistant that is there

3:45

this particular shopping assistant what it can do is it is able to answer questions related to

3:51

return shipping warranty refund that is there but you can see this that is that is that

3:57

in order to get the correct information lLM should be having that correct information

4:01

that is there right but lLMs like for example if i talk about gbt 5.5 clod opus 4.6 and other

4:10

models that are there you will see this that these models they will not be able to answer

4:16

this information about your shopping card that you are building why because they will not be

4:21

having the correct information that is there is this point clear that if i talk about chat

4:27

or gpddd 5.5 or i talk about any other model let's say claude opus 4.6 and other models

4:34

that are there whenever we have these kind of models they will not be having the correct information

4:39

that is present like for example we can see any particular information they will not be having

4:45

the realistic information that is there in order to have them realistic information what we need to do

4:51

is we need to use the rag so you will see this that what rag what

4:57

problem rag is trying to solve we can see this that lLMs all the lLMs that we talk about

5:03

all these lLMs they are very good with generating the data they can generate the data that is present

5:10

but if i need this particular part like if i need rag then what i need is we can see this that we are

5:16

having some lLm in this lLm it will be combined with proper knowledge base how we will get that knowledge

5:23

base we will provide that particular knowledge base this knowledge base this knowledge

5:27

base can be anything it can be pdf it can be url it can be any API that could get the

5:35

data or from anywhere the data can come from so you can see the main part you need to understand is

5:41

that how rag is built rag is built on this particular part that you use a llm to generate a proper

5:48

answer but the context of the answer you are getting from a knowledge base and what is that knowledge

5:54

base this particular knowledge basis what thing this knowledge basis is

6:00

the context that we try to provide is that idea clear is this everyone able to understand

6:08

this particular point that this particular knowledge base it is acting as what it is acting as the

6:14

context that is there so we can see this that this context how it will get it will get it will get it from

6:20

different different data that we will try to provide and that data we will store in

6:24

which format we will be storing all this data in which format we will be storing

6:29

that in embedding format is that idea clear this idea is everyone able to understand that this

6:35

knowledge base which is acting as a context and this thing will be happening with the help of what

6:41

this will be happening with the help of embedding start are there so all the data that we are having

6:46

we will try to store it in the embedding format this part is every one able to understand i'm not that

6:53

well today so that is why i'm speaking a little bit low and won't be able to turn on the camera

6:58

yesterday only i got discharged from the hospital so yeah one by one we can discuss uh

7:05

till here this part is clear this part is everyone able to understand

7:15

till here this part the first thing is clear right that what is a problem that llm is having lm can

7:23

incorrect data LLM they can hallucinate also like for example sometimes whenever you are

7:28

writing code LLM can automatically generate any code which is not existing because it does not

7:35

know whether the proper function or a method already exist or not it just assumes and gives you

7:41

the data that particular assumption makes LLM insufficient that is there this thing are you able to

7:48

understand like in companies when we go LLM might not be aware of any

7:53

particular incident any particular new email any particular new feature that you are building

7:58

since LLM is not aware of that particular part its knowledge is insufficient in nature it can

8:04

generate any particular answer that is there is that idea clear this idea are you able to understand

8:17

correct right so let's try to understand this particular part

8:23

that how we will try to fill this particular knowledge gap that is there the first thing

8:28

that we will do is we will try to provide what we will do is we will try to provide static knowledge

8:35

Static knowledge means that you provide necessary PDFs and everything that is there now like you can

8:43

see this right that like basically that LLMs it has limited knowledge if you talk about GPD 5.5 which is

8:51

one of the best models of open AI

8:53

it has data till 2024 only it does not have realistic data in order to get the

8:59

realistic data what it uses is it uses LLM only like it uses internet search and it calls and gets

9:06

the latest information it is internally using tool search or it is using something called

9:12

as agentic rack that we will study later on but I think currently the idea is clear

9:17

that the main gap in LLM is that they are having

9:23

set of knowledge they are aware of only static data that is present up the second thing is

9:28

that they don't have any particular like they don't know the complete context they don't know

9:35

they don't know whether a feature is existing or not they don't know whether a library is

9:39

existing or not they don't have any particular knowledge related to that part since they don't

9:44

have that that is why they will generate any incorrect answer like for example if you ask

9:49

LLM that what is a life insurance of this

9:53

policy if it does not know right it will automatically generate some

9:57

useless answer that is there so these kind of things makes it inaccurate so in order

10:02

to increase the accuracy what we are using we are using something called as

10:07

drag is that idea clear like for example if chat gpd is not aware about any

10:12

insurance then it can give you this kind of answer that the payment of that particular

10:17

insurance will be done in 24 to 48 months but that information might be incorrect

10:23

why because that information that it is having is limited to when it was trained after it

10:29

if there is any particular modification then it will not have the latest data if i today go to

10:35

any particular grow mutual fund i think everyone here is aware of mutual funds right so if you go

10:41

to any particular mutual fund you will see this that every day the price of the mutual fund is changing

10:46

since every day the price of the mutual fund changes up lms they will not be aware of what is the

10:52

the latest price in order to get the latest price they use that internet search tool

10:56

and then answer it so if you ask chart gbd what is the latest price by its training

11:02

data it does not know the latest price by internet search call it is able to get the

11:06

latest price that is there is that idea clear this part is everyone able to understand

11:12

guys this part are you able to understand

11:20

if i asked at gp tp tpkach that what is the price of this particular mutual fund then with

11:35

its training data it does not know because when it was trained it was 2024 year now the price

11:42

of 2026 right it will not have the latest data that is there in order to get the latest

11:47

data it will make an internet search call that is there it will use that internet search tool and then

11:53

get the data is that idea clear so it has to make that internet search tool that is there and yes right

12:02

it will use internet search tool it will get the latest price and once it gets the latest data it will

12:09

generate the answer from the latest data that is present up correct yes muskan

12:20

malay i think till here this part is clear right other people is everyone able to

12:24

understand this particular part guys still here this part is clear

12:33

that what is the main problem with l lm that part you are able to understand right

12:39

purjan did you join the class late what i told i just told right it will refer internet

12:54

it can make a internet search call that means the same thing right i think till here

13:00

this part is clear to everyone correct it uses tool calling warine that

13:09

is called as mcb it uses mcp search that is there and then it calls different different

13:15

tools that are present internally does not use selenium i think that part is clear

13:24

so we can see here this particular part that now what is the scenario we can see here this

13:30

particular part uh one by one let's try to see this we can see here that llms they don't understand

13:39

understand a lot of things the main problem is that if you ask lm it will tell you with

13:44

full confidence that this answer is correct but ideally it will be wrong so that is a main

13:50

scenario that since lm is inaccurate it is not having the complete information it cannot be trusted

13:57

like if you ask it any particular thing like i was giving you an example of insurance policy that

14:03

is there it might not know the complete information regarding the insurance policy

14:09

but it will tell you the answer in that particular way that it will look like that the

14:13

answer is correct so you can see this that l lm can be confident but it might not be correct

14:19

that is a main thing we need to understand that in a lot of cases whenever it is giving incorrect answers

14:26

it can be very very confident on that particular part so since we don't have to like we cannot trust

14:35

a llm directly that whether it is giving a correct information on

14:39

not so in order to gather the complete information or in order to make lm more

14:44

accurate what we use is we provided the knowledge base that is there so that is why if you

14:50

see why rag was born rag was born for this particular part that LLM can generate

14:57

any data it can generate inaccurate data since it can generate inaccurate data we can see this

15:03

particular part that we don't know whether the data is accurate or not so what

15:09

we try to do is whenever we use rag what is the approach that we try to follow we try to

15:15

follow this kind of approach that whenever we are asking anything with LLM right we will write a

15:21

prompt whatever prompt we give to LLM what it is called us do you guys remember

15:27

whenever we are writing any prompt here for our application that we are building that

15:31

form this called us what

15:39

system prompt right so we can see this that whenever we are writing that system

15:59

prompt right what we will try to do we will try to do it in this particular way that that that particular

16:04

prompt will be like it will be a full prompt but we will enter this thing

16:08

that answer this query the query will be given by the user so you will see there will be a user query

16:16

whatever user query has asked and we will provide the context and context will be what

16:22

whatever data we are fetching is that part clear till here this part are you able to understand

16:38

till here this part is clear right so you will see that that system prompt will contain

16:43

a lot of things it will contain that you are a let's say a strong recommendation service

16:48

and you need to answer this particular query which user is asking and the context is coming from

16:53

where whatever data our rag is able to fetch that particular thing will act as a context i think

17:00

this idea is clear so this will be the kind of system prompt that we will be writing up

17:06

correct

17:07

i think this thing is also clear it is yes we are just putting one constraints

17:12

that use this particular context to answer that query so this is acting as a constraint part only in

17:18

the prompt this prompt we will be writing in our a i application or the rag that we will be

17:26

building so since it is written inside our rag right what it will be it will be the system prompt

17:32

is that part clear whatever query user is writing that particular thing can be called as a

17:37

user prompt that is there is this thing clear

17:44

guys this thing are you able to understand

17:51

rag will use what thing rag will use all the necessary embeddings that are there

17:56

all these embeddings they are stored in a chroma db so all these chroma dbs

18:00

what do you think are the example of long-term memory or short-term memory

18:07

long-term memory right i think that thing is clear now who asked it richu

18:17

till here this thing is clear right so let's try to understand that what is grounding and one

18:23

by one let's try to discuss this particular part so we can see here that what we need to do

18:29

let's understand it with the help of this diagram only i'll just copy this diagram and see if i can

18:36

paste it quickly

18:37

so we can see here this particular part that one by one let's try to see we can see

18:57

here that whenever the question whatever question user is asking whatever question user is asking

19:03

we will take that particular question question question let's say the user is asking let's say the user is asking question

19:07

questions related to any particular life insurance that is there or any particular policy that it has

19:13

asked so what we will do is we will try to find out the necessary policy chunks that are present

19:19

this necessary chunks means that let's say you bought a 25 year policy from lic now automatically once

19:29

this question is asked by the user that what is a tenure of this particular policy that is there so we will

19:35

in our rack system we will try to find out the necessary policy that is present

19:41

once that is done then what we will try to do is we will try to find out some evidence that is there

19:47

so let's understand that what is the evidence this evidence is nothing but whatever

19:53

question user has asked right we retrieve the policy chunks and then we validate whether what user has

20:00

asked and the chunks that we are having are they having necessary evidence

20:05

in for the question or not like sometimes it can happen right that the user is

20:11

asking about resetting your password and in your data nothing is there regarding resetting your

20:17

password then what will happen then what will happen we will see this that it will not work

20:25

right so in those cases we will just return that our rat chat board is not aware of that particular

20:31

information that is why what we are saying is we are saying that we are saying that

20:35

we will try to constrain the model output with the external factual answer that factual

20:42

answer should actually contain the data if that data is not present right then it does not make any

20:49

particular sense kuki this can happen right that your data was related to all the lic policies

20:55

and user is asking it related to password management then your rack cannot answer it so the main thing

21:03

is that we will try to search for a proper evidence in the prompt and then

21:08

llm will try to generate a proper answer that is there we will check that answer also we will check

21:14

that whether the answer is correct it matches with the proper like it answers the query properly

21:21

with the help of correct context or not and once that answer the query then we will try to like give the

21:28

final output to the user so this kind of verification we will try to do so this kind of verification we will try to do so

21:33

grounding is nothing but the verification that we are doing that llm has found out the

21:39

answer from necessary sources and not generated itself the main idea the main thing that you need to

21:46

remember is l lm is very good with generation of data so sometimes it can generate a lot of answers

21:54

which are inaccurate so in order to validate whether an llm has generated the answer properly or not

22:00

we are trying to evaluate the model answer whether that particular thing is correct or not

22:06

is that idea clear this idea are you able to understand

22:16

guys this thing is clear or not clear other people what's the scenario

22:30

this will be automated right once llm has generated the answer

22:39

then we will try to do other things correct then we will try to verify the answer

22:45

we can build a ii agent that will figure out the answer is that thing clear

23:00

till here this part is clear so i'll just focus on the current class once that is there

23:16

guys still here this part is clear right so we will write we will do a final verification

23:26

that is there that particular verification that we are doing right

23:30

that verification is called as what that particular verification is called as grounding is this

23:35

thing clear or not clear we will verify whether model has found out the correct answers or not

23:44

rather than generated it if let's say that if we were asking anything related to lic policy it can

23:50

generate the answer using lic policy right we will write a check whether that particular

23:56

information which model is giving is actually present or not

24:00

so that there is no guessing work there is hundred percent

24:04

correctness that is there is this thing clear

24:11

guys still here this part is clear

24:17

we will check it right we will write a program in order to check that

24:24

so let's see that how we will try to do it in drag apart and then we can go any doubts that you are

24:30

having to the last session right once let's complete this session and then we can discuss it

24:34

so don't worry on that part so one by one let's try to see this particular part we can see here

24:40

this thing that first of all let's understand that what is having in rag apart so if you remember

24:47

i'll just show you from a diagram only that how our rag is working if you remember we have already

24:52

studied about all these diagrams that are there so from this diagram we can clearly understand that what

24:58

track will try to do i think you remember this diagram right we drew this particular diagram

25:05

so let's say that user is writing any particular query like if you see here on this particular part

25:10

you can see this that user has given a query i want to reset my password okay this is the query of user

25:17

that is there now this query will be converted into list of embedding starter there embedding is nothing

25:24

but a sequence of numbers we will try to match where in our data

25:28

these numbers are present we will search that okay here embeddings are of food delivery

25:33

here the embeddings are of tech support here the embeddings are of password reset so you will

25:39

see the numbers that are written here right these numbers point 1.5.8 these numbers

25:45

they will try to match with which numbers they will match with these particular numbers that are

25:49

there and once we are able to get a match then we will try to return the answer is that idea clear

25:58

this idea are you able to understand this entire thing is called as rag what is

26:08

the meaning of rag now let's understand the r in rag so r in rag stands for the retrieval

26:15

part that user has given query okay this query is converted into the sequence of numbers that you can see here

26:23

now what you are doing is you want to retrive that what is a data associated

26:28

with this like what is the actual step of password and not correct so we are

26:34

retrieving from where we are retrieving from vector database that we are having so that is

26:39

why we have retrieval part now what is the meaning of augmented augmented in rag

26:45

means that whatever user query asks right what you are trying to do you are trying to embed

26:52

that particular query or you are trying to augment that particular query with this thing so if you see this

26:58

right whatever query user has asked what we are doing is we are saying that that particular

27:04

query it will be combined with the context that is there so we are doing augment augmentation means

27:11

jodana we are trying to augment the query with the necessary context that we are trying to find out once we

27:19

find out that then what we will do is we will try to generate the final answer so that is called as

27:25

generation so the main thing that you need to understand with the rag part is the first

27:30

thing rag may r stands for retrieval what we are redriving what do you think we are retrieving

27:39

what do you think we are retrieving we are retrieving we are retrieving the proper data or we can say the

27:47

context from where we are retrieving we are retrieving it from the vector database correct and how we are

27:54

retriving we are saying that whatever user query is there that particular user query is converted

28:00

into math number which numbers are like this and once you get all these numbers that are present

28:06

we can see this that uh these numbers that are there all these numbers that you are having we will

28:14

search in the original data where these numbers are present and once you are able to find out top k

28:20

results you remember in the last class we talked about rank one rank

28:24

two rank three we will get what we will get our main thing what is our main thing the

28:29

main thing will be the context part that is there so once we get the context all these things are

28:35

happening in the retrival part now what is the meaning of a in rag a in rag stands for augmentation

28:47

or we can say augment part what is the meaning of augment means augment means joining what you are trying to

28:53

join guys what we are joining we are joining user query is joined with what it is joined with

29:02

what it is joined with a necessary context that we got g stands for generation what is a

29:08

meaning of generation that llm will generate final answer is this part clear this part are you able

29:18

to understand guys is this part clear

29:23

not clear so it's retrieval augmented generation that stands for rag

29:32

these three terms are clear to everyone right

29:38

guys still here this three part is clear so we can see this that in retrival part now this data

29:48

can be coming from anywhere it's not hundred percent compulsory that data will come from you

29:53

and everything it can come from anywhere this data can be coming from what this data can

29:59

come from something like let's try to see the data can come from something like pdf it can come from

30:07

something like url it can come from some files it can come from some database it can come from anywhere so

30:16

that general retrieval part that we are getting right it can be from anywhere i think this idea is also clear

30:23

yeah right we can discuss that rjoo till here this part is clear this part is

30:32

everyone able to understand yes right punkaj that is correct

30:40

are data will be present the actual data that we are training will be coming from pdf url only

30:46

right you remember that diagram that we studied in the last class if you see this particular part

30:53

let's see so you need to remember this thing right that whatever data we are getting

31:00

okay that particular data what we are doing is we will scrape the data once scraping is done

31:07

we will clean the data then we will chunk the data then we will get embedding then what we

31:12

will do with this embedding we will store all these embedding into a vector db this part do you

31:18

remember last two three classes same thing only we have studied right

31:23

this part are you able to understand so we can see this like one by one let's talk

31:36

about the next thing that we are having so we can see here this particular part that this is

31:41

a flow of rag one by one i'll repeat the flow same flow we have already discussed it i'll just

31:47

try to copy paste this diagram one more time so that we can easily do it and then we can do

31:53

so yeah so let's try to see this particular diagram we can see this that first of all,

32:17

this is the retribal component that we are talking about in retribal component you can clearly

32:23

see that first we will try to retrive the query that is there like whatever user query has come

32:29

we will try to retrieve the necessary information this retrival will happen using what it will happen

32:35

using vector database only we have already seen right that actual embeddings they are stored where

32:41

they are stored in vector database from vector database we will get but vector database how vector database

32:47

will get the data it will have the original data right so you remember right there is something called

32:52

as a ingestion component what is the meaning of ingestion component that whatever normal

32:58

data you are having you will clean the data you will normalize the data you will chunk the data

33:02

then you will create that embedding correct so that embedding is stored where that particular

33:07

embedding is stored inside the vector database once we redrive the embeddings that till that thing will

33:13

act as a context that is there that particular context along with the user query so this thing and this

33:20

thing both the things will be combined and they will generate the answer once they

33:25

have generated the answer it's not 100% guaranteed that that answer will be correct so what we

33:30

will do is we will try to do some validation that validation thing is called as grounding and then

33:36

what we will do is we will try to generate the final answer to the user is that part clear

33:41

this diagram are you able to understand

33:50

Guys, till here the spot is clear.

34:20

In real world we will only store it right, we will write a schedule review that will always update the data.

34:27

That part we have already discussed about right.

34:31

So I can repeat this part in Malay but we have discussed it like two three times in last two three classes.

34:37

So you can see how the retribal part and rag is working.

34:40

The first thing is that user will write any message.

34:43

I'll write here example also.

34:45

So you can see this particular example as well.

34:48

So let's try.

34:49

So let's try to write it down.

34:51

And in the last class also if you remember the same part we have seen that first of all, user will be writing any particular query.

34:59

Let's say the user query is, how do I reset my password?

35:06

Okay, this is the user query. What is the first thing?

35:09

We will try to convert that user query into what?

35:12

User query will be converted into something called as embedding.

35:16

How these embedding will look like, they will look like this.

35:18

like this.

35:19

They will look something like this.

35:24

Okay.

35:25

Now once we have these embeddings, what we will try to do?

35:28

If embedding is empty, then we will tell user that we don't have a context of this particular

35:33

part.

35:34

We will directly tell the customer or the user that we don't know about it.

35:38

Let's say your data is about life insurance.

35:41

But user is asking about swimming.

35:43

Then we will tell that it does not know.

35:45

Correct.

35:46

That thing is clear.

35:47

that thing is here.

35:48

Right.

35:49

So you can see then we will use these embeddings to retrive the data.

35:54

So that particular retrive part we will do using what?

35:57

We will do it using vector database.

35:59

Once we do that particular part, we will get the necessary context.

36:04

We will combine the context with the user query that is written above.

36:07

And we will pass to the LLM for generation.

36:10

This is the flow, right?

36:13

What thing is not clear in this flow?

36:15

In last class also the same flow we have seen, right?

36:17

Do you remember the program of the last class where we were seeing the output?

36:24

Do you remember that part?

36:26

Guys, still here, this thing is clear?

36:32

This part is clear to everyone, right?

36:38

Context plus query will be written with the help of system prompt.

36:46

So you will be written.

36:47

you will see context query and everything will be written it is already added right shan in this particular part i've already added that so if you check here all the ppds and everything is added up right i updated here in the get up section also till session 18 i fixed that particular bug that you were having so it till session 18 it is added up even the program also is added up here and all the ppts are also added up you can check it here

37:17

Correct, right? I think the flow is clear to everyone. Is everyone able to understand the flow?

37:26

Guys, flow is clear to everyone.

37:35

Let's try to go to the next part. So you can always see that this is the same minor program that I have written.

37:43

So one by one, let's try to see that program also.

37:46

And then we can go ahead. It's similar to whatever program we wrote in the last class, right?

37:51

Let's even see that.

37:58

Currently, you will see that this program won't run because other functions are not implemented here.

38:04

If you see here vector search and all these functions are not implemented, but what this program is telling you about, this program is telling you about that how a rag will work.

38:14

like for example if you see here you can see here this particular part right that user question is coming we are trying to search that particular query inside our vector database and we will get the relevant chunks that okay these are the top three queries which are matching with the user query once we get that particular part we will build some kind of prompt this prompt will be system prompt that you are a shop card assistant answer using the policies this policies is

38:44

is the chunks that are there and we are providing the customer question and then

38:48

LLM will generate.

38:49

So this prompt you are able to understand that how we will write this kind of prompt.

38:54

Is this part clear?

39:14

Now, and the flow is also clear, right?

39:17

Joby user question is whatever user question we are getting, what we are trying to do is we are trying to search that particular user question in the embeddings.

39:25

Embedings say we will get the relevant chunks that is there.

39:28

Once we get the chunks, we will try to do what thing?

39:31

We will try to write a prompt.

39:33

That prompt building will be that whatever product we are building, right?

39:37

We will try to take that particular prompt, we will combine it with the necessary chunks.

39:43

we will add the user question and then we will ask LLM to generate it.

39:48

Is this part clear?

39:50

Like what thing is not clear?

39:52

This though we have already seen in the like last class also.

39:57

We will see that rare like Nidesh, what we will do?

40:01

We will see that particular part.

40:04

Prompt here will be the system prompt that we are writing right?

40:06

So currently we are building a rag chartboard for something like Amazon.

40:11

So this shop card is nothing but similar.

40:13

to Amazon only. So the main idea is that this shop card people will ask questions

40:18

related to different, different policies that are there. Now, if LLM generates inaccurate policies,

40:25

then customer will be confused, right? So in order to prevent that particular part,

40:29

what we are doing. We are saying this particular thing that you get the data from the relevant

40:35

chunk and then you answer the customer question. So in the prompt, what we have added, we have added

40:41

the necessary chunks that are there and the question part. And then we are asking

40:45

LLM to generate. What is not clear in this program?

40:51

Guys, what is not clear here? This part is everyone able to understand?

41:00

Guys, are you able to understand it or not understanding?

41:05

D-Rash, now you are able to other people, is everyone able to understand the flow, right? This flow.

41:11

we have seen like multiple times now. This flow is clear. Like, till now, you should

41:16

remember the flow, right? I guess.

41:28

So yeah, let's try to go to the next part that we are having. We can see here that what will happen

41:33

between grounded response and not grounded response. So now next part we will try to see to see.

41:41

here I think this part is clear. So let's try to understand that what will happen in this

41:45

grounding scenario. So let's see like let me just increase this diagram and paste that diagram

41:51

there.

42:11

Yeah. So let's start and discuss about this thing. So we can see this that, let's say, if user is asking this kind of question, that how many days it will take to return a opened phone case that is there. Let's say user purchased a phone case. And now user wants to return that particular phone case. Now user is asking this question. How many days is asking this question, how many

42:41

he should in how many days he can like return the phone case. So if I just give

42:47

response from LLM, let's say that we have one scenario where directly LLM is telling. Now

42:53

LLM will directly say that you can return in 15 to 30 days. Do you think this answer is fine?

42:59

This answer is not fine, right? Why? Because for Amazon, for Flipcard, for E card, for everything,

43:07

the answer will be different. And this is very vague answer that.

43:11

is there. There is no source. There is no platform. There is nothing. This kind of answer we don't

43:17

want. We want a good answer. So how we can get a good answer? We need what is the exact policy

43:24

of shop cut? We need to find out that what is the exact data that it has related to refund policy.

43:33

Once we find out that particular part, we will try to give a proper answer that is there.

43:38

Once the answer is generated, we will search again.

43:41

that is this present in the data or not that semantic search also we will do if you

43:46

remember do you remember the meaning of semantic search

43:52

guys do you remember the meaning of semantic search

43:58

whenever we want to find out the meaning right then we use what we use semantic search that is

44:03

there so we are searching with the context that is present up so we can see here this particular part

44:09

that what we need to do is we need to find out that whether the answer

44:17

LLM that is giving that unopened items within seven days of delivery can be

44:23

returned is that thing already present in the data or not is that meaning present in the

44:28

data or not if it is present we will show that response to customer but if data is not

44:33

present we will say that we are not aware of that I think that idea is also clear correct

44:39

guys till here this part is clear

44:49

here this part is clear right so you can see right so you can see the tone is same but

45:09

particular thing is giving the correct answer that is there so every time what we want

45:14

is we want these kind of correct answers that are present that is the main idea

45:21

till here any doubts anyone is having this thing everyone is able to understand right so you

45:26

can see other examples also if i ask other questions like this let's say that i ask a

45:31

question here that what will be the shipping like will it arrive tomorrow or not it can say this

45:38

that usually next day delivery that thing is completely wrong right because it depends upon

45:44

platform to platform amazon might have different rules flip card might have different

45:49

rules blanket or swigie might have different rules so that is why we need proper data so for all

45:56

these platforms different different data we will try to provide based on that data it will try to answer

46:02

questions in a better way the same thing you need to understand that if we are writing

46:08

phones dead in 10 months are they covered or not so again if it says two year warranty but

46:14

it's not again compulsory it depends upon platform to platform i think this idea is clear right

46:21

that every ungrounded response ungrounded means that you directly generate fake information from

46:28

l l lm can generate fake information and tell you you will never identify whether that is correct or not

46:34

is that idea clear

46:38

guys is the idea clear to everyone

46:46

till here everyone is able to understand right that why

46:51

this thing they will like these kind of responses are not good now the next thing that we need to

46:57

see is that how we will judge it is similar to hallucination only right that it is generating

47:02

the answer on its own so that's a scenario

47:08

so we can see here let's try to go to the next part that is present let's talk about that

47:15

we can see here that how we can know that whether the answer is good or not so let's say that

47:23

if it is telling like first thing is evidence that whatever answer llm is generating if we

47:29

feel that that particular answer has something which is mentioned about policy and everything

47:35

then it can be correct but it's not guarantee

47:38

guaranteed like you can see here if you see all these responses usually often typically

47:44

they all indicate we like general meaning they are giving vague answers and they are trying

47:51

to generalize the output that is there this kind of general output can never be trusted so that is why

47:58

what we are trying to do is we are trying to look for the evidence that is there that whether

48:04

a complete data information like for example the policy number the

48:08

policy version are these things present or not then if it specifically is answering like

48:15

if it tells some specific shop cart number or any policy number or condition then that means it is correct

48:21

like sometimes lm can generate correct answer also based on internet search tool like currently if i

48:28

asked r gpd that what is a price of gold or what is the price of silver it will make a google search call

48:34

it will get the data it will instantly convert that

48:38

particular data into embedding and then tell me the result also this kind of thing it can do

48:42

so it is using something called as a genetic rag that we will see later on but the idea is clear

48:49

right that all these chart applications like chart gpd gemma cloud they are able to answer real

48:55

time data irrespective of they are not trained on real time data is they are able to make a internet

49:01

search tool call that is there it can call any tool it's not internet they can call any other tool also and

49:08

the data. They can even if they have the access to database of your company, they will call your

49:13

database tool and get the required information from there as well. Is this thing clear?

49:38

there or not using those things only we can identify so that is why we can see this that

49:44

every time we cannot trust these lLMs for asking very specific questions that are there

49:49

since asking these questions if you see like whenever we see this particular part that

49:57

like whenever we see that general answer it is giving right in those cases directly trusting on

50:04

lLM we will not do and that is why rag was born all these

50:08

tadbots nowadays they are internally using rag system even chat gpd and all other things

50:13

they are also using rag so that's a main scenario i think till here this part is clear right

50:21

till here this part is everyone able to understand

50:38

part that we are having so we can see this that how rag will use vector search we have

50:45

already seen this part i can again show you that particular example and we can talk about it so let's

50:51

talk about it do you remember the last class program that we discussed

50:57

do you remember the output of that and everything i'll just open that particular part and we can talk

51:08

about that also.

51:38

that we wrote one by one let's try to see this part so if you see here once the program

51:47

run is completed what we can see we can see here from the starting that these are the

51:51

documents that you are having so currently do you remember that here six documents were

51:56

there i think everyone can see this particular part right that six documents were there so what

52:02

happens in the ingestion component ingestion means you are trying to fill your vector database

52:07

initially and this part is running before this part is running offline

52:12

offline means when user is not giving the query also right then also this particular part will

52:18

run and what this can you hear me now is the voice clear hello yes you're audible

52:30

yeah so we can see here this particular part that this is the data that we are having

52:37

And inside this particular data, all these docs that are present.

52:42

All these docs are nothing but embedding starter there.

52:45

Embedding they are representing meaning, meaning of these sentences like this sentence has this particular meaning.

52:52

Then we can see this particular sentence, it has this particular meaning that is there.

52:58

Then we can see this sentence, it has this particular meaning.

53:02

So same way all these meanings are stored.

53:04

Now if I ask a question, let's say that I ask this.

53:07

particular question that i want to get my money back correct so if you see the embedding

53:13

very carefully just see this that this sentence is i want to return my shoes and get my money

53:20

back now focus here focus on these numbers can you see the number is minus 0.065 can you see

53:28

minus 0.064 here if you see the second number is minus 0.135 can you see the second number is minus 0.135 can you see

53:37

see it's very near to minus 0.17. The second number is very very close to this particular

53:45

number. Same way if you see the last value is minus 0.111. If you see the last number here,

53:53

it's like minus 0.5. That is there, right? That is why if you see it is matching with doc 2.

54:02

Because the doc 2 if I print the embedding of doc particular 2, it is

54:07

will be very, very close to this particular part. That is why the distance is bare minimum.

54:13

Then a little bit more distance is there for this particular part. So if the query was I want

54:18

to return my shoes, then we are able to find out the matching dogs that are there. Is that idea

54:24

clear to everyone? This kind of thing is called as vector searching where we are trying to find

54:29

out sentences which have similar meaning. Like for example, this sentence was related to return part.

54:36

That is why all the sentences which are related to the return part, they are getting printed.

54:42

Is that idea clear?

55:01

Guys, still here?

55:06

Everyone is able to understand this, right?

55:11

Are currently I have not, currently I have not printed all these embeddings, right? Currently, here I have printed one. That is why 384 numbers are coming up.

55:21

Ideally in this also 384 numbers are present, right? But they are not printed. You can see dot dot dot here. Is that part clear?

55:31

That part, are you able to understand?

55:36

So this kind of thing is called as vector search. Now what are your doubts related to this program?

55:41

Since at the start of the class also, some people were asking doubts in this program.

55:46

What is a doubt you were having in this program?

55:50

Like see, Visual Studio code, if you are not able to set up those kind of doubts you can discuss on Friday or you can like set up from a YouTube video program what you are not able to get or you can raise a ticket from our side team and they will resolve that particular doubt that why you are not.

56:06

not able to install. At the end, we can see what is the issue with your installation part, but like, what's a scenario?

56:14

Like other doubts, anyone having any doubts in this program that we discussed in the last class?

56:36

Okay. I think the idea is clear. So yeah, let's try to go back here. So we can see this that rag uses this entire same concept in order to retrive. Like if we see this particular diagram that I was showing you, right? So here you can see the retribal part, context part that we are getting. All these things we have already seen by writing that program. Only the generation part will require a LLM call. So that we will try to do LLM call that is there. For LLM call, we will need something.

57:06

called us API key that also we will talk about in the next class but you can see the first

57:10

three steps which are related to query, re drive and context that thing are happening using this part.

57:18

I think this part is also clear right this part are you able to understand

57:36

So, Mali, we discussed that right, that different embedding models are there which are generating the embedding and the mathematics part. If you want, you can study about that. Correct. But in the classes, we will not be doing that part.

57:57

So yeah, let's try to see that how your vector search will be building. Let's talk about this diagram. This is the same diagram that I was talking about.

58:06

if you remember i was speaking a term called as ingestion let's talk about how this ingestion

58:11

component on how everything will be working so i'll just to delete this i'll just copy this diagram there

58:19

and let's talk about that

58:22

so once we discuss this diagram then we can go to the next part let me just face this diagram here

58:36

So we can see here this particular part that first of all there is something called this index building this index building is happening offline can you tell me the steps that are involved here like if you remember that the in this also multiple steps are involved what is the first step that whatever original data you are having let's say you have PDF data URL data that data will be scraped what is a process scraped like we can see this is that we will try to

59:06

fetch the data that is there and once we are able to fetch the data properly this is the first step

59:12

that all the PDF URL and all the database you will fetch the data once you fetch the data what you will

59:18

use is you will try to clean that particular data this thing is also called as what

59:25

this thing is also called as normalization that you try to store only that much information

59:31

that is required i'll give you a demo of that also

59:36

once you normalize the data then what we will try to do we can see here the third step the third step is that once you have done it you will use chunking chunking means breaking the data into small groups

59:56

once you break the data into small groups then what you will use you will generate the embeddings and once those embeddings are generated by any embedding model the fifth step will be

1:0:06

that you will try to store all these embeddings and where you will store these

1:0:11

embeddings you will store these embeddings in a vector database so these five steps they are happening

1:0:17

where all these five steps are happening inside this index building part and this is running offline so

1:0:24

that your rack can work so every day you can set a scheduler or you can set an alarm kind of thing

1:0:31

which will get the latest data that is there it will first clean the data

1:0:36

once the cleaning part is done it will chunk the data then it will create embeddings

1:0:41

and then it will store the embeddings into vector database is this part clear this part is everyone

1:0:48

able to understand guys this part are you able to understand this part are you able to understand

1:0:57

this diagram is clearly visible on the screen right abyshek if you have any doubt you can write in chat

1:1:06

correct so once we see this particular part then what we will try to do

1:1:13

so why every day very good question so why every day we will do let's say that if you are

1:1:19

building a rag for mutual fund then you know right that every day unless and until there is a

1:1:25

holiday the prices of the stocks will get updated like the mutual fund every day generally

1:1:30

they get updated unless and until there is some holiday so that is why every day it should run and get

1:1:35

get the latest data otherwise it will get the older data that is there right

1:1:40

is that but also clear

1:1:48

where is this part are you able to understand

1:1:55

i showed you that other thing like do you remember the grow thing that i showed you

1:2:00

do you remember that example of ingestion component i'll show you once again so if you

1:2:10

focus on my screen right now you can see this that this is a this is what this is raw data so can you

1:2:18

see that raw data is so much now out of this raw data is everything useful the answer is no

1:2:25

everything is not useful so what we will do is we will clean the data we will store only that much

1:2:30

information that is required by us once we clean the data and once we have extracted

1:2:36

proper information we will create chunk we will create different different chunk like we will

1:2:42

divide this particular data into many groups so you can see this is how the grouping is happening and this

1:2:48

is the chunk data once we have the chunk data what we will do is we will try to store all these chunks into

1:2:55

embedding embeddings are nothing but these numbers that you can see currently on my screen can you see here

1:3:00

all these numbers that are there so all these numbers are what all these numbers are

1:3:05

different different embeddings each of these embeddings is 384 numbers which is representing the

1:3:11

meaning of the chunk is that part clear is the first component clear to everyone this thing

1:3:19

is called as a ingestion component are you able to understand the ingestion component

1:3:30

guys are you able to understand it or not it is like the same thing right

1:3:37

that we downloaded it is just for a real life project that thing i showed you in the last class

1:3:43

was very small project right this is a real life project that is there

1:4:00

you guys still here this part is clear

1:4:15

ingestion is the entire component that is there ingestion has multiple components like all these

1:4:21

components that have written in orange color right they are part of ingestion is that part clear

1:4:26

here all these things right all these things that i'm writing here this is

1:4:32

ingestion correct

1:4:41

every time we will get the real data right so that is why if you remember i was talking about

1:4:48

this scheduler is like a alarm that is there every day the scheduler will run and what

1:4:54

scheduler will try to do this scheduler will always trigger the ingestion component so that we have

1:5:00

the latest data that is there this part are you able to understand this is a rag of like a complete

1:5:07

application that i was building so you can see every day there will be something called as a scheduler

1:5:12

scheduler you can understand right it's like you can schedule your alarm that is there same way we can see this

1:5:18

that we can schedule that every day you wake up at 10 a m you skis

1:5:24

the latest data that is there once you scrape the latest data you try to clean that particular

1:5:30

data that is present up once you have done the cleaning part you chunk the data and then you store

1:5:36

the embeddings and all is that part cleared

1:5:41

are we have already scrape the data it's legal you are usuf we are just using it for education

1:5:48

purpose right i am not predicting which stock to invest i am just telling the price of that stock

1:5:54

this thing is clear or not clear till here guys this part are you able to understand

1:6:02

this much ingestion component is clear scheduler is also clear right other people

1:6:10

what's the scenario

1:6:14

now what do you think will happen in retribal component what we will try to do we will try to do we will

1:6:23

retrive based on the user query if you remember we have already discussed the steps i'll

1:6:29

write the steps very quickly whatever user query we have that particular user query is converted

1:6:34

into embedding once we have that embedding what we will do we will search the embedding

1:6:41

where inside the vector database and once we get the embedding in the vector database then we will

1:6:49

set up the necessary context that what are the sentences which

1:6:53

are having similar meaning so setting up context means find data which has similar meaning

1:7:03

with user query this is this will happen in the retrival part once you have the retrival part then

1:7:10

what we will do in llm part what do you think we will do inside llm we have the data like we have

1:7:18

the context we have the user query we will write a good prompt

1:7:23

so that particular prompt will be the system prompt inside that system prompt three things

1:7:29

we will add we will add the context we will have the query and whatever extra information that prompt

1:7:35

needs we will add that correct so you can see this that context very all these things will be added up

1:7:44

and once we add that particular part what we will try to do we will try to do

1:7:53

we will see this particular part that particular thing will be sent to llm and llm will do

1:8:01

what it will do generation i think this diagram is now clear right this diagram are you able to

1:8:09

understand i think the diagram is clear right yes generally for normal policy and all it will not be

1:8:22

be required if data is not getting updated every day then scheduler is not required

1:8:26

but if your data is getting updated every one hour every two hour every day then scheduler will be

1:8:32

required right that also archid we can do it we can even build it for 10 000

1:8:40

urals or 1 million URLs for every URL we will store like 10 15 amount of data points that

1:8:47

are there right it will take 10 minutes only to run at max currently like for

1:8:52

for five six urals it runs in 10 second is that idea clear

1:9:00

guys this diagram are you able to understand or not understanding

1:9:07

is everyone able to understand the diagram part

1:9:16

let's go to the i think yeah till here only let's do it then brayette

1:9:21

Bray travel part is online why because whenever user is asking a query that time it is running

1:9:27

right this is happening in the background so if you see here this entire part that i'm talking about

1:9:33

right this entire part is happening in the background this is happening when user query is coming that

1:9:39

is why we call it as online online means jub user ne kuched then you do it that thing is called as

1:9:45

online whatever is happening automatically that thing is called us offline is that meaning clear

1:9:51

yes right shubam that is correct it is reading that pdf understanding that

1:9:59

pdf and then whenever you are asking question it is getting from that pdf so same rag thing it is doing

1:10:21

still here this part is clear

1:10:51

already discussed it right that how it does semantic search it uses vector

1:10:55

database to do the semantic search that is there right inside that it uses cosine similarity

1:11:00

and we studied about index n and also in the last class so those things are only happening right

1:11:07

do you remember that part let's have a short break and then we can discuss we can have a short break

1:11:15

and then we can continue with the next part let me write it let me just start the

1:11:21

timer eight minutes break we can keep

1:11:51

you know.

1:12:21

You know,

1:12:51

You know

1:13:21

I'm

1:13:51

I'm

1:14:21

I'm

1:14:51

I'm

1:15:21

I'm

1:15:51

I'm

1:16:21

I'm

1:16:23

you

1:16:51

Thank you.

1:17:21

Thank you.

1:17:51

Thank you.

1:18:21

Thank you.

1:18:51

Thank you.

1:19:21

Yeah, we are still here. I think we are good to go, right? This idea is everyone able to understand.

1:19:51

insert the LLM, then also it will be sent to LLM, right?

1:19:57

Yes, right?

1:19:58

So Dhanu, that is correct.

1:20:00

I think till here, this part is clear to everyone, right?

1:20:04

Are you able to hear me?

1:20:09

Let's try to go to the next part that we are having.

1:20:12

So one by one, we can discuss the other things that we have here and then we can go.

1:20:16

So you can see this, that there can be some scenarios where we don't.

1:20:21

don't have the chunking data. So let's talk about those scenarios as well using this diagram that I've wasted here.

1:20:28

So let's see this particular diagram and then we can talk about. So you can see this that there can be some cases, right, where the data is not existing.

1:20:37

In those cases, what we will do. So let's talk about that thing. So we can see here this particular part.

1:20:45

One by Walnut stock. So you can see here that the retrival part,

1:20:51

it depends on both the things.

1:20:53

Like sometimes this scenario can happen that we can get a wrong chunk.

1:20:58

Even this thing is possible that you get a wrong chunk of data.

1:21:01

There is one more scenario that you don't have the data.

1:21:05

You don't have a relevant chunk that is there.

1:21:08

Sometimes even this thing is possible that you have the chunk, but we ignore it.

1:21:13

So these three scenarios are possible.

1:21:16

Like for example, let's one by one see examples of these part as well.

1:21:20

Like let's say that you are searching for refund, but your chunk that is coming is related to shipment that is there.

1:21:29

In those cases, you are having an incorrect chunk.

1:21:32

Let's say that you are searching for password, but inside your data there is nothing related to password.

1:21:38

So you will encounter this scenario where there is no relevant chunk that is there.

1:21:42

Then the next scenario is you get the right chunk, but there is like the query such that that

1:21:49

you are not able to, LLM is not able to understand that particular chunk and it ignores that chunk that is there.

1:21:57

In those case, what we can do is, any idea like how we can do it.

1:22:05

In those cases, we will see that if any of these things happen, right?

1:22:10

Like, you will see this, that we cannot do anything with a rag part.

1:22:14

Because if data is not there, just if we are getting some incorrect chunk,

1:22:19

then what thing we can do?

1:22:21

We can change our embedding strategy, retrieval strategy, or chunking strategy that is there, so that we get proper chunk.

1:22:28

In no relevant chunk, we cannot do anything because if data is not there about password, how can our model answer?

1:22:36

Model will never be able to answer.

1:22:38

Like, for example, if I have data related to life insurance policies that are there, and if I ask

1:22:45

questions related to AI courses, then it will never answer.

1:22:49

So in those cases, nothing we can do.

1:22:52

In this case, if right chunk is getting ignored, we can fix in the prompt.

1:22:56

So we will see this that we can fix the prompt, uh, which is given to LLM,

1:23:00

or we can switch to better models that are there.

1:23:03

Those things can be done up, but in this case, so nothing we can do.

1:23:07

In this case, we can do something that we can change our chunking strategy.

1:23:11

We can change our embedding strategy.

1:23:12

We can change our retribal strategy that is there.

1:23:15

So one by one, let's talk about all these scenarios and let's see this.

1:23:19

this particular part i think the previous slide is also clear right this slide are you able to

1:23:24

understand guys this thing is clear wrong chunk no relevant chunk and right chunk

1:23:32

i think this part you are able to understand right yes let's go to the next part that we are

1:23:45

are having so we can see here this particular part let's go to the next thing and let's talk

1:23:50

about that there are different different applications that we can see for rag so a lot of

1:23:55

applications are there that part we will talk about i'll just thrown this a little bit

1:24:00

it decrease the size of this as well so we can see that a lot of like a lot lot of applications

1:24:08

are there let me just fix this at a lot of places in real

1:24:15

life rag is getting used let's talk about those real life scenarios so we can see here

1:24:22

first of all we have support bot starter there where rack can be used up so let's talk about

1:24:27

that so we can see here first of all that whenever you'd see swigi chartboard amazon

1:24:36

chart board flip card chart board mintra chartboard and all these places to

1:24:40

retrive the policies and latest question starter there what we can use

1:24:45

we can use rag chatbot why in companies also rag chatbot can be used because

1:24:50

every time different different policies in a company changed so whenever they are changing we can use

1:24:55

these kind of chatbots that are there is that idea clear

1:25:02

guys this thing is clear or not clear now the next thing that we need to remember that whenever

1:25:13

let's say that you want to figure out any documents

1:25:15

let's say that today you go inside a company and you get into any particular

1:25:20

team that is there and you need to understand every information about that team let's

1:25:25

say that you get placed into any company and you are new to that team you need to

1:25:30

understand everything so you can build a rag chatboard so that anyone can be

1:25:36

onboarded about everything like for example rather than reading the doc

1:25:41

if they have any particular question they can type to a rag chartboard and that

1:25:45

particular chatbot can answer all those questions that are there is that

1:25:49

idea clear guys this idea are you able to understand

1:25:54

you could have done this idea though is clear right today you are learning a i you

1:26:06

could have done is you could have done this particular part that you could have done this particular

1:26:11

part that you could have like an asked question with a

1:26:15

chatbot that what is rag what is agentic a i and all these things and then it will answer

1:26:20

it so we can see rather than reading pdf and documentation we can build a rag chatboard that can

1:26:26

answer it correct same way for retrieving any notes anything that is there you can use a rag

1:26:32

chartboard that will give you proper answer so that you don't have to dig dive into the notes you can build

1:26:37

a rag chat about out of all these notes that i'm sharing even this is possible that let's say that

1:26:43

you want to study that you have any question any doubt then it can use the necessary

1:26:48

information that is present and all these things and then can answer it is that part also clear

1:26:57

this part also are you able to understand correct so even this particular thing can be done

1:27:09

the next thing is that we are having a genetic workflow so we can see this that we are having a genetic workflow so we can see this

1:27:13

we can use a lot of agents like for example if you see a chat gpd chat gpd if you

1:27:20

ask what is the price of this particular stock price that is there internally it uses rag only how

1:27:26

it uses rag it makes an internet search call it search this entire web page whatever you are

1:27:31

asking it gets that data and once it gets the data then it tells you the exact price that is

1:27:37

there so internally it is using internal like in internet search

1:27:43

it fetches the data it builds a rag and then it answers up your question properly so only

1:27:50

thing is that that thing is possible with the help of agentic rag so agentic rag also we will study

1:27:55

as we go on into the later part of the course there we will study about agentic rag and all

1:28:00

i think till here this part is clear right this part are you able to understand

1:28:13

if you provide a proper link where data is present then it will give correct answer

1:28:17

only if you directly ask it the price then it will not give but if you give a u rl also

1:28:21

right then it will search and give you the correct answer

1:28:24

reju that part is clear right even you can build uh like if you are aware of upsc right

1:28:32

you can even build a rack chartboard for upsc thing and all correct is that part clear

1:28:43

let's go to the next part that we are having so we can see here this particular

1:28:51

part let's see that what are the different different limitations of the rag so first of all is

1:28:57

that rag reduces the hallucination like it will provide accurate answers that is there

1:29:03

but due to these issues like if you see all these issues that are there right that i was talking about

1:29:10

that sometimes wrong chunk we get sometimes

1:29:13

irrelevant chunk we get sometimes there is no relevant chunk that is there sometimes the right

1:29:19

chunk is getting ignored due to all these issues it is 99.5% correct but 0.05% it is

1:29:28

sometimes wrong also so this main idea that we need to remember that it's not 100% like it's not

1:29:35

100% correct it's like 99% correct but there is a 1% chance that it can give error also due to incorrect

1:29:43

chunk due to not finding out the relevant chunk due to ignoring the right chunk that is there

1:29:50

now you can see this that every time like if you are building a rag then you need to remember that

1:29:57

you need to clean the database also you need to remove the useless embeddings also let's say that every day

1:30:03

you are building a rag which is telling stock prices then the previous embeddings need to be cleaned up

1:30:10

because all these previous embeddings are useless let's say that today you are giving

1:30:15

one PDF for training rack next day you update that PDF so the earlier embedings that are there

1:30:21

they need to be removed so that is again a headache task that whatever useless information you have

1:30:28

have right you need to remove it is this thing clear that part are you able to understand

1:30:35

the next point is that retrival in generation they have to be properly tested

1:30:40

like for example every time if validation we are not doing on a lot of scenarios

1:30:45

right it will give incorrect answers that are there so this kind of validation we should always do

1:30:51

i think this idea is also clear guys this thing is clear and the next thing is that rag

1:31:00

needs to be maintained up maintained up means that whenever the policy is changing whenever new

1:31:05

information is coming what we need to do is we need to do is we need to

1:31:10

update the context or the information that is present in rack if i don't do that

1:31:16

it will continue to work on the older things that are there so that is why you can see operational

1:31:22

work is required operational work means people have to work on that rag and update the latest

1:31:28

data that is there is that part clear guys this thing are you able to understand

1:31:40

I see.

1:31:44

I was saying here that I was saying here that

1:32:10

the rag is tough to maintain tough to maintain but every day there has to be a

1:32:16

scheduler that needs to be triggered right like if i show you a demo of that particular part

1:32:21

you can see this that what will happen like for example if you go to this milestone two that is

1:32:27

there let's open that milestone two part so we can see here this particular part in this part if you

1:32:34

try to see you can see every day our scheduler runs up which every day at 915 istt

1:32:40

it runs up and it updates the information that is there every day it wakes up and it runs

1:32:46

and updates the information otherwise my rag will be older so it updates the information with the

1:32:52

latest details that is there so this kind of maintenance work someone has to do currently i've

1:32:57

automated that also that get up automates everything for me that every day get up runs the workflow

1:33:04

workflow i don't have to do anything but someone has to look into whether the data is getting updated

1:33:09

it properly or not every day currently i've written the program correctly so every day it runs up

1:33:13

so not a big issue but you can see that some day it fails then i will have older data that is there

1:33:21

so this is one problem with rag that operational works need to be done the second thing is that testing

1:33:27

you need to do if you don't test the retrival and the generation categories that are there then what will happen

1:33:32

is that uh what will what it will try to do is it will give some wrong answers

1:33:39

it will probably be using some strategy that is not working like the chunking strategy

1:33:44

that it is using or the embedding strategy or the retrival strategy that might not be correct

1:33:49

so that is one thing the next thing is that outdated pdfs that you see like every time data

1:33:55

has to be cleaned up properly right if you don't clean up that particular data then correct

1:34:01

answer you will not get i think that part is also clear

1:34:09

and it is guaranteed right that every time correct answers it will not be getting

1:34:14

like 100% correct answers we cannot guarantee that's another scenario

1:34:21

i think till here we are good

1:34:39

you guys still here this part is clear right

1:34:58

i think if you remember in today's class what we have done is we have done is we have discussed the theory part

1:35:09

you will see what we will do we will try to just implement like next two three classes

1:35:14

will be implementation of rag that we will be doing is that idea clear

1:35:39

tell you here this thing is clear

1:36:09

like currently in the last class we implemented this program where we were doing

1:36:13

basic embedding in the next class we will implement the entire rag similar to this now what are the

1:36:19

doubts that you have from the last class i think this thing is clear right till then i'll push the

1:36:25

notes of this particular class also let me just do that very quickly and then we can see

1:36:39

guys whatever we discuss that part you are able to understand goreng what is the

1:36:53

doubt you are having can you type in chat same with vinegar other people are you able

1:37:00

to understand whatever we discussed let me paste the today's notes that are there today's notes that are there

1:37:09

and

1:37:11

you know,

1:37:13

Did you watch the last class recording?

1:37:43

Did you guys try watching the last last recording that is there?

1:38:13

Other people, did you watch it or not?

1:38:20

I've just pushed the changes here, like if you refresh this particular page, let me check.

1:38:43

Do you see session 19 is coming up or not?

1:38:48

Session 19 by mistake, I think it is coming where let me add it properly.

1:39:13

You can see session 19 that right? You can see here all the notes whatever we are having are available here. I have pushed that whatever we discussed in the PPD is present. So you can

1:39:43

read it from this particular part also. I'll just change this repo and tomorrow will

1:39:47

make it better as well. Yeah. Other people, I think whatever we discuss is clear to everyone,

1:39:54

right? Guys, still here, this part is clear. I'll just to update this also. These PDFs,

1:40:07

these PPDs everyone is having.

1:40:13

Guys, how many of you are stuck with visual studio code setup and not able to do visual studio code setup? Can you type in chart?

1:40:21

How many of you are not able to do that?

1:40:24

Pankaj, can you share your screen? Let's see if you can share your screen. Did you try properly?

1:40:35

Can you share your screen? Other people, what's the scenario? How many people are able to run the program?

1:40:40

Can you share your screen, Pankaj?

1:40:50

Aray, pro you don't have to do, right?

1:40:52

Janani, without pro also, it will work.

1:40:54

Pankaj, can you share your screen?

1:40:58

Yeah, now it is visible.

1:40:59

What is the error that is coming?

1:41:09

You are on mute.

1:41:10

FYI. Do you know how to open a file or a folder here? Did you download that particular file, first of all?

1:41:17

Do you know how? Just click on file?

1:41:20

File. File on file? The file is looking at top, top. Top. Top left.

1:41:27

Right, left on left up. Look on, file. Click on new file. New file. Clicked on new file.

1:41:33

Clicked on. Now, click on, and, you type, type, type, here, file. File. Pyye.

1:41:40

Enter.

1:41:45

And this save to where you have to save it.

1:41:49

Desktop. Save it. Just create file.

1:41:52

Clicked.

1:41:56

File. P.W.

1:41:57

Now, the code, get up the link that I gave to, that code, get up the link that I had given.

1:42:01

Get up link you have?

1:42:06

Open that GitHub link.

1:42:10

Oh, my, my, my, man.

1:42:13

Here, click on vector.

1:42:17

The vector one, click on, scroll down.

1:42:19

Scroll down.

1:42:20

Scroll down.

1:42:21

Vector search lab.

1:42:25

Vector search lab.

1:42:27

Vector search lab

1:42:28

Click on.

1:42:30

Click on file.

1:42:35

Copy button

1:42:37

here.

1:42:40

copy and paste there.

1:42:43

Control V is it.

1:42:47

Pased.

1:42:48

How will it?

1:42:49

How do you?

1:42:50

How do it?

1:42:51

Terminal to open.

1:42:52

Terminal button, look.

1:42:53

The terminal button, look.

1:42:54

It's the terminal button, here.

1:42:56

Here, here from new terminal click.

1:42:58

Python installed.

1:43:01

We discussed it right, Gora, Gora,

1:43:04

in the last class.

1:43:06

Did you watch that?

1:43:07

Rest and continue.

1:43:09

Trust and continue.

1:43:14

Python installed.

1:43:15

Just type here Python 3.

1:43:19

Like Python 3, if there are there, then

1:43:22

now if it's a terminal, then.

1:43:24

Power shell is not.

1:43:29

Your laptop is slow.

1:43:31

Gohrab, did you check the recording of the last class?

1:43:37

We discussed it, right?

1:43:38

That how this is working.

1:43:39

It is just right. We are writing a for loop to extract the text ID and metadata there.

1:43:44

That particular thing we are doing.

1:43:46

Click on new terminal once more. Let's see if the terminal is opening or not.

1:43:50

Click on Terminal.

1:43:52

Terminal.

1:43:53

Click on new terminal.

1:43:56

Wait, click there.

1:43:59

Here, here here.

1:44:00

Ah, it's a terminal.

1:44:01

See, Users.

1:44:02

Look.

1:44:03

Look, look.

1:44:04

Near to the direction.

1:44:06

Left.

1:44:07

Left to look.

1:44:08

Right.

1:44:09

yeah, what did you.

1:44:11

Yeah, here from here,

1:44:12

run.

1:44:13

If Python installed,

1:44:14

and the other library you've installed

1:44:16

did you?

1:44:17

Sentence, Transformer, and all

1:44:19

all.

1:44:21

Terminal on click

1:44:23

there.

1:44:24

If you're run

1:44:25

on the button to be run

1:44:26

you're going to

1:44:28

run

1:44:29

on the other terminal

1:44:30

on.

1:44:31

Then, then,

1:44:32

then, then,

1:44:33

then,

1:44:39

it's also the same thing, right?

1:44:44

It's just another way of writing it got off.

1:44:47

Both are doing the same thing only.

1:44:50

Where it's going to run

1:44:53

already it is running.

1:44:55

It is saying, right?

1:44:56

The other terminal if you'll click

1:44:57

click on,

1:44:58

the terminal

1:44:59

click on the power shell right.

1:45:00

Click on it.

1:45:02

Here,

1:45:04

type if you're,

1:45:05

type if,

1:45:06

type,

1:45:07

Python 3,

1:45:08

file.

1:45:09

I, space,

1:45:10

can't

1:45:11

Python 3.

1:45:12

Python

1:45:16

the spelling

1:45:20

and

1:45:21

in the

1:45:22

last life class,

1:45:23

you'll

1:45:24

see how to

1:45:25

how to run

1:45:26

can

1:45:27

how to run

1:45:28

it?

1:45:30

That

1:45:31

so I was

1:45:33

correct.

1:45:34

Uh,

1:45:36

basically,

1:45:37

Saksh, I was

1:45:38

trying to do that.

1:45:39

But the last

1:45:40

what is

1:45:41

that

1:45:42

it was

1:45:43

you

1:45:44

have

1:45:45

installed in laptop

1:45:46

Yeah,

1:45:47

and

1:45:48

everything is installed.

1:45:49

And

1:45:50

uh,

1:45:51

the outputs

1:45:52

you know

1:45:53

update

1:45:54

this

1:45:55

this program stuck

1:45:56

or

1:45:57

this program

1:45:58

or

1:45:59

it's

1:46:00

or it's installed

1:46:01

properly,

1:46:02

the

1:46:03

visual studio update

1:46:04

and then

1:46:05

you

1:46:09

he

1:46:10

you are

1:46:11

you

1:46:12

and

1:46:13

it's

1:46:14

just

1:46:15

I will

1:46:16

I will

1:46:17

I will try to

1:46:18

and

1:46:19

and then

1:46:20

that

1:46:21

uh...

1:46:23

uh, install

1:46:24

success

1:46:25

message was

1:46:26

but when

1:46:27

that

1:46:28

that

1:46:29

two terminals

1:46:30

that were

1:46:31

they were

1:46:32

they were

1:46:33

I was

1:46:34

uh,

1:46:35

uh,

1:46:39

now

1:46:40

that

1:46:41

update

1:46:42

and

1:46:43

uh...

1:46:44

uh...

1:46:45

uh...

1:46:47

If you're

1:46:48

if you're

1:46:49

if you're

1:46:50

then you're

1:46:51

after you

1:46:52

start

1:46:53

you're

1:46:54

start

1:46:55

and then

1:46:56

you're

1:46:57

start

1:46:58

you're

1:46:59

that you're

1:47:00

you're

1:47:01

if you're

1:47:02

if you're

1:47:03

if you're

1:47:09

this

1:47:10

that

1:47:11

then

1:47:12

then

1:47:13

then

1:47:14

next class in

1:47:15

we're

1:47:16

okay

1:47:17

okay

1:47:18

yeah

1:47:19

go on Riju what is a doubt you are having?

1:47:21

Riju

1:47:23

Riju

1:47:24

what is

1:47:25

doubt is?

1:47:26

Hello,

1:47:28

can you

1:47:29

hear me?

1:47:30

Mm-hmm

1:47:31

Yeah

1:47:32

Saksam

1:47:33

actually

1:47:34

just wanted to

1:47:35

understand the

1:47:37

whole scenario

1:47:38

I mean as a

1:47:40

as a

1:47:40

wholesome picture

1:47:41

so we are using

1:47:43

rag basically

1:47:44

in order to

1:47:46

have the grounded

1:47:46

output that I understood

1:47:48

and we are using

1:47:49

the vector DV

1:47:50

in order to

1:47:51

store the embeddings

1:47:52

basically of

1:47:53

some information

1:47:55

right

1:47:55

now I mean my first

1:47:58

question is

1:47:59

when should we use

1:48:00

rag and when should we use

1:48:02

these

1:48:02

particular

1:48:03

I mean from the

1:48:05

from the embeddings

1:48:06

of the vector database

1:48:07

when should we

1:48:08

So rag is

1:48:09

nothing but

1:48:11

using everything

1:48:12

right

1:48:12

rag is

1:48:13

retrival

1:48:14

augment generation

1:48:15

the retrival part

1:48:16

uses

1:48:16

vector db and embedding

1:48:18

so

1:48:18

rack in the

1:48:19

back in

1:48:20

the

1:48:21

part

1:48:21

that's

1:48:22

we're

1:48:22

we're not

1:48:23

we're

1:48:23

we're

1:48:24

we're

1:48:25

we're going to

1:48:25

we're

1:48:25

we're doing

1:48:25

we're

1:48:27

we're going to

1:48:27

we're

1:48:28

okay

1:48:28

okay

1:48:29

okay

1:48:29

okay

1:48:30

other

1:48:30

thing is like

1:48:31

in the real

1:48:33

real life

1:48:33

scenario

1:48:34

so you're

1:48:35

our

1:48:36

my LLM

1:48:37

is

1:48:38

every LLM

1:48:38

, we

1:48:38

from

1:48:39

we'll

1:48:39

we're

1:48:40

the unit

1:48:40

can't

1:48:41

connect

1:48:41

and we're

1:48:41

correct

1:48:41

that we're

1:48:42

talked

1:48:43

that we're

1:48:44

talking yeah we're

1:48:45

in the

1:48:45

so

1:48:46

we're

1:48:46

we're able to

1:48:47

shortly

1:48:47

now we're

1:48:48

super

1:48:49

we're

1:48:50

maybe we're

1:48:50

they'll

1:48:50

we're

1:48:51

this model

1:48:51

uh

1:48:52

there's

1:48:52

there

1:48:53

we're

1:48:54

there can

1:48:55

we can connect

1:48:55

we can't

1:48:56

create

1:48:56

and different

1:48:57

other

1:48:57

things

1:48:57

so we know

1:48:58

and we

1:48:58

we're

1:48:58

and we

1:48:58

we're

1:48:59

and we're

1:49:00

and we're

1:49:02

and

1:49:02

what I mean

1:49:02

whether

1:49:03

okee

1:49:04

connect we

1:49:04

connect to

1:49:05

and when

1:49:06

uh

1:49:07

this tools

1:49:07

connect

1:49:08

VectorDB

1:49:09

always

1:49:09

connected

1:49:10

that

1:49:10

will be connected

1:49:11

that's

1:49:11

we're going to

1:49:13

go back and

1:49:13

we're

1:49:13

like we

1:49:14

if we're

1:49:15

a third-party

1:49:15

application

1:49:15

tool to

1:49:16

connect

1:49:16

let's say

1:49:17

we need

1:49:18

any, let's say

1:49:18

we need

1:49:19

or Figma

1:49:20

or Figma

1:49:20

design

1:49:21

to then

1:49:22

we're doing

1:49:23

we're doing

1:49:23

we're

1:49:23

we're

1:49:25

directly up new

1:49:25

cursor or

1:49:27

then H.RGPT

1:49:28

clod

1:49:29

these up

1:49:29

they're just

1:49:31

they're just

1:49:31

they're just

1:49:31

they're

1:49:31

so they're

1:49:31

so they're

1:49:33

saying MCP

1:49:35

which is model

1:49:36

context protocol

1:49:36

so we

1:49:37

we'll

1:49:37

we'll

1:49:37

we'll be

1:49:38

we'll be

1:49:38

we're

1:49:39

okay

1:49:40

okay okay

1:49:41

okay

1:49:41

okay

1:49:41

because I

1:49:42

actually

1:49:42

I'm actually

1:49:42

I'm

1:49:43

I'm

1:49:44

I'm trying to

1:49:45

we're

1:49:46

we're

1:49:46

we're

1:49:46

maintain

1:49:46

we're

1:49:47

we're

1:49:48

every day

1:49:49

probably we'll be

1:49:50

using any

1:49:50

scheduler or

1:49:51

something

1:49:52

maybe that could

1:49:53

be anything

1:49:54

but that could be

1:49:54

there

1:49:56

there's information

1:49:57

and

1:49:57

there's lag

1:49:58

there's like

1:49:58

you're

1:49:58

like you're

1:49:59

that you're

1:49:59

being a day

1:50:00

daily

1:50:00

run failed

1:50:01

so then

1:50:02

then...

1:50:03

but we're

1:50:03

we can we can't

1:50:03

we can't make

1:50:04

a script

1:50:04

can't check

1:50:05

that check

1:50:05

that will

1:50:06

that script

1:50:06

right

1:50:07

or

1:50:07

it's a

1:50:08

re-try

1:50:08

that's

1:50:08

I can't

1:50:09

I'm

1:50:09

that's

1:50:09

I'm

1:50:10

can't

1:50:10

get a

1:50:11

and then

1:50:11

they're

1:50:12

correct,

1:50:12

correct,

1:50:13

correct,

1:50:13

correct,

1:50:13

correct,

1:50:14

correct,

1:50:14

and

1:50:15

another

1:50:16

last thing is

1:50:17

that's

1:50:17

that means, that

1:50:19

means a

1:50:20

thing is my

1:50:21

just I'm

1:50:22

confirming from your

1:50:23

end,

1:50:24

that means

1:50:25

that means that

1:50:25

means that

1:50:26

I'm in the system

1:50:27

information

1:50:29

that I can

1:50:29

like,

1:50:30

like,

1:50:30

let let's a database

1:50:32

data data.

1:50:32

Suppose I'm maintaining

1:50:33

some oracle

1:50:34

so I'm maintaining some Oracle, so

1:50:35

that we're

1:50:36

that we can

1:50:37

convert

1:50:38

and it

1:50:39

can't

1:50:39

and

1:50:39

daily

1:50:40

the database

1:50:41

update

1:50:41

insert

1:50:42

and everything

1:50:42

and

1:50:43

after at the

1:50:43

day end I

1:50:44

can

1:50:44

schedule a

1:50:45

script

1:50:45

which will

1:50:45

maybe

1:50:46

shell script or

1:50:46

something

1:50:46

anything

1:50:47

correct

1:50:48

and

1:50:48

then we'll

1:50:49

get

1:50:49

and then we will

1:50:51

connect

1:50:51

our agent

1:50:52

to

1:50:52

retrieve and

1:50:54

I mean apply the

1:50:55

whole rack

1:50:55

process over

1:50:56

the vector database

1:50:57

and then

1:50:59

also in order

1:51:00

to generate

1:51:00

suppose I want to

1:51:01

generate a report

1:51:02

so maybe I can

1:51:03

connect to any

1:51:04

of the tabloo or

1:51:05

something like that

1:51:06

I mean I'm just

1:51:06

giving

1:51:07

example

1:51:07

maybe not

1:51:08

but

1:51:09

that agent

1:51:10

we'll connect

1:51:11

or then

1:51:11

then you

1:51:12

then you

1:51:12

you're

1:51:13

what you're

1:51:13

that

1:51:14

you're

1:51:14

then it will

1:51:17

take the data

1:51:18

from the

1:51:18

vector DB

1:51:18

and it will

1:51:19

use that

1:51:19

external

1:51:20

to generate the

1:51:21

report

1:51:21

is it

1:51:22

correct

1:51:22

we will

1:51:23

see that I'm talking

1:51:24

right

1:51:24

yes

1:51:25

yes

1:51:25

correct

1:51:25

thank you

1:51:27

thank you

1:51:28

thank you very

1:51:28

much

1:51:28

yeah

1:51:29

okay okay

1:51:30

okay

1:51:30

okay then

1:51:32

yeah

1:51:32

okay then I think

1:51:33

okay then I think

1:51:33

okay then I think Opel you can

1:51:34

take over

1:51:35

and in the next

1:51:36

class guys we will try to implement the same thing like this is the theoretical part that we have discussed

1:51:41

in the next class we will begin with the implementation part so probably basic program we will try to write down and we will understand that how we are writing that kind of program that is there so yeah that will be the main agenda in the next class and that thing we can do yeah i think opal you can take over

1:52:04

all right yeah so yep so let's move on to the next section

1:52:10

I'm releasing the feedback poll meanwhile if anyone has any

1:52:18

question to me they can ask regarding previous classes or anything else

1:52:34

Besides, I have one announcement to make, tomorrow is a class on ChromaDB installation and any other type of backlog installation or code related issues if you are facing, please come up with them.

1:53:04

We'll be discussing. So tomorrow will be two hours class from 8 to 10.

1:53:34

Thank you.

1:54:04

All right. We'll have a quick. We'll have a quick quiz. We'll have a quick quiz.

1:54:34

Let me share my screen.

1:55:04

here or just go to www.minti.com and enter this code given here. I'm posting this code in the chat as well.

1:55:34

All right, so let's get started.

1:56:04

an answer to make answers longer, to improve internet speed or to remove embeddings.

1:56:11

Yes, the correct

1:56:28

is used to retrieve the correct option is used to retrieve relevant information.

1:56:32

for generating an answer. Let's have a quick look on the leaderboard.

1:57:02

The very.

1:57:32

Here is your third question. What is grounding?

1:57:46

And the options are supporting answers with factual evidence, storing data in a database, compressing documents.

1:58:02

The correct option is supporting answers with factual evidence.

1:58:15

Let's look at the leaderboard now.

1:58:32

In RAG, which component finds relevant chunks?

1:58:39

And the options are generator, retriever, encoder or prompt.

1:59:02

The correct option is retriever.

1:59:12

Here is a leaderboard after this question.

1:59:17

Let's move on to the question.

1:59:25

which component converts with three parts into a natural language reply.

1:59:33

And the options are retriever, database, generator, chunker.

1:59:55

And the correct option is generator.

2:0:02

Let's have a look at a quick leader goal.

2:0:10

Get ready for the 6 question.

2:0:23

What does top K vector search return?

2:0:29

And the options are the longest documents.

2:0:31

The K nearest meaning matches.

2:0:34

The oldest document or the random documents.

2:0:39

And the correct option is it returns the K nearest meaning matches.

2:0:54

Let's have a quick look on the scoreboard.

2:1:09

Get ready for the seventh question?

2:1:13

Which of the following is an example of a knowledge base?

2:1:19

And the options are a keyboard, policies and FAQs, a monitor and operating system.

2:1:38

The correct option is policies and FAQs.

2:1:48

Here is a leaderboard after 7th question.

2:1:54

And finally, let's move on to the last question.

2:2:08

Complete the Rathflow, query, retrieve, dash, generate.

2:2:15

The options are train, embed, context, deploy.

2:2:38

The correct option is context.

2:2:53

Let's look at the final leader.

2:2:59

Congratulations, Mahi.

2:3:04

With that, we have come to you.

2:3:07

We have come to an end to today's session.

2:3:09

Let's meet tomorrow.

2:3:12

Till then.