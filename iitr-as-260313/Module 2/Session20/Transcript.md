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

Thank you.

5:00

Thank you

5:30

Thank you

6:00

Thank you

6:02

Thank you

6:04

Thank you

6:06

Thank you

6:08

Thank you

6:10

Thank you

6:12

Thank you

6:14

Thank you

6:16

Thank you

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

Thank you.

10:48

Thank you.

11:18

Thank you

11:48

Thank you

12:18

Thank you

12:20

Thank you

12:22

Thank you

12:24

Thank you

12:26

Thank you

12:28

Thank you

12:30

Thank you

12:32

Thank you

12:34

Thank you

12:41

Thank you.

13:11

Thank you.

13:41

Thank you.

14:11

Thank you.

14:41

Thank you.

15:11

Yeah, guys, can you hear me?

15:29

Is the voice clear to everyone?

15:31

The voice is clear to everyone?

15:36

The voice is clear, right?

15:38

Yeah, we get for everyone to join and then we can

15:41

chart.

15:48

Yeah, did you watch the recording of the last class that was there?

15:54

As everyone was through that part.

15:57

You will see this that today's class is implementation of last class.

16:02

So last class theory is very, very important.

16:05

Without that, it will be a little tricky for you to understand everything.

16:09

So yeah, my thing like if you have been

16:11

watch the theory, then you will be able to relate with almost everything that we are discussing.

16:41

We are at 1 minute we can wait and then we can start.

17:11

Let me quickly share my screen also.

17:14

So I think the screen is visible.

17:17

So this is a PPD that is there.

17:19

And today you will see a lot of food writing we will try to do.

17:22

So that part also we will see.

17:24

Let me just turn on the video also.

17:28

I think you will see me as well, right?

17:31

Can you see me?

17:33

Yes.

17:35

Yeah, I think we can get started then.

17:39

Let's start one by one and let's start one and let's see me.

17:40

one by one and let's try to discuss everything that we have for today.

17:44

So one by one, let's start.

17:45

So first of all, what we will try to do is we will try to actually see the Rack architecture part.

17:51

One by one, let's look into that.

17:53

All these theoretical part we have already seen.

17:55

And then we will start writing the program that is there.

17:58

You will see this that I've edited this repository.

18:01

In this repository, I'll push all the codes that we are writing today.

18:05

So you can copy paste form here in order to run that particular part.

18:09

Let me just share.

18:10

the link as well.

18:11

I've pasted the link in the chart also.

18:13

So you can see that particular part.

18:16

So yeah, let's try to go ahead to the part that we are having.

18:19

So we can see this that today we will try to build a Rack system for this support card that is there.

18:25

If you remember that yesterday we discussed in the last class we discussed about something called a support card.

18:31

That we need to build a proper chatbot, a Rack chatbot, which is able to understand what is there in the knowledge base of support card.

18:39

card and then answer different different questions that are there.

18:42

So today what we will trying to do is we will try to build a rag for an e-commerce platform.

18:47

That e-commerce platform here is shop cart that is there is there is

18:50

there is that idea clear.

18:52

That idea I think everyone is able to understand right?

18:55

That here you can see that inside shop cart there are multiple scenarios that we have.

19:01

The first scenario is related to the customer part.

19:04

The second scenario that we are having is related to support team.

19:08

The third scenario is that we are having is related to support team.

19:09

related to the business part the four scenario is related to the outside boundary that is there.

19:14

So if you try to see here this particular part, we can clearly see that all these things will be coming from some knowledge base that is present.

19:22

So that knowledge base or knowledge boundary will be coming from where it will be coming from the Rags system that we will be building.

19:30

So that part you remember right that how a rag works.

19:34

Correct.

19:35

This part you remember or not?

19:39

Guys, do you remember that? Yeah.

19:44

So one by one, let's try to see.

19:46

Like once I show you the data part, you will understand that, okay, inside this knowledge waste, everything is present.

19:52

And all the data that is present in knowledge ways, we will be storing that data.

19:56

We will convert that data into proper embedding.

19:59

Once the data is converted, whenever user is asking any particular question that is there,

20:04

we will answer it based on whatever data we have stored.

20:07

That particular part we will try to.

20:08

particular part we will try to do.

20:10

So yeah, let's try to see all these things that are there.

20:13

One by one first we can write the program.

20:15

Then we can understand what is the meaning of the program and all.

20:18

So you will see this that I will be using a lot of things here.

20:22

Like for a first, if you remember that there are three components in a Rack system.

20:26

Like first of all is a knowledge source that is there, the real data.

20:30

This real data I will be storing first of all in Python.

20:34

Once I store that, then we will try to store this data into Chrome

20:38

DB.

20:39

Inside this comma DB, once the data is getting stored right, it will be converted into embedding.

20:45

And for embedding, we will use some particular model that is there.

20:48

That particular model will be a BG model.

20:51

Do you remember, we talked about BG model, which is a free model that is there?

20:55

Do you remember that part?

20:57

Guys, do you remember about it or not?

21:01

So you remember right?

21:04

How our Rack actually works?

21:06

One by one, let's discuss that part.

21:07

discuss that part and then we can go ahead.

21:10

So probably here only let's try to discuss.

21:13

So we can see, first of all, we will have normal data, which is the raw data that we are having.

21:19

This raw data, it will be present where it will be present inside Python.

21:24

We will write a normal, we can say this is the raw data.

21:27

This raw data will be stored in something called as Python list.

21:31

I think you remember that, right?

21:33

Once we have this raw data, we will try to clean this data.

21:36

We will store this data.

21:37

this data properly. Once that particular part is done, what I'll try to do is I'll try to chunk this data

21:43

and I'll try to embed the data that is there.

21:46

So we will proceed to the next step that will be embedding.

21:49

For embedding, what we will be using, we will be using something called as a BG model.

21:54

What is this BG model?

21:56

BG model is a free model which is provided by a Beijing Artificial Intelligence Institute that is there.

22:03

There are multiple models that are present in BG, one by one we can see all.

22:06

by one we can see all of them like for example if you go here to this particular link

22:10

you can see here bg large model is present.

22:13

Same way we can find out a link for bg small model also.

22:17

This model will be used for converting into embedding part.

22:20

What is embedding?

22:21

Embedding is nothing but the sequence of numbers that we have.

22:26

So you will see this that this raw data,

22:28

it will look like something that we have written in English language.

22:32

Once we have this kind of data that is there,

22:34

then what we will try to do, we will convert

22:36

it into a list of numbers. That list of numbers will be nothing but embedding.

22:40

And then we will try to store all these list of numbers where we will store it into a

22:45

vector database that is present.

22:47

So you will see this, that all these numbers, they will be stored into a vector database,

22:52

which will be here, ChromaDB.

22:54

So you can see here this particular part, like the next step will be that we will store the data

22:59

in something called as a vector database.

23:02

And that particular vector database, what we will call it as,

23:05

we will call it as we will say this that this vector database is something called as groma db.

23:09

I think this part is also clear, right?

23:12

This part are you able to understand?

23:19

Guys, still here the first three steps are clear.

23:23

This type of component we can also call as ingestion component.

23:27

Ingestion means that we are trying to fill in the data that is there.

23:30

Once this ingestion component is done, we will go to the retrival part.

23:34

For retrieval,

23:35

we will make a proper strategy.

23:37

Once we have a proper strategy and we retrieve the data,

23:40

like once the retrial phase is done,

23:42

then what we will try to do is, we will try to,

23:45

we will try to send that data.

23:50

Let's say that user query is there.

23:52

I can say any user query comes up.

23:54

We will try to embed that user query.

23:56

I think you remember that what is embedding.

23:59

So we will embed the query.

24:02

Once we embed the query, we will try to find out the top key

24:05

that are there. I think you remember that what are top K results and all.

24:09

Once we have those top K results, then what we will try to do?

24:13

We can see this that we have top K results.

24:17

Once we have these top K results, then what we will try to do?

24:24

We will try to fill, like find out the top K results.

24:28

That will be done with the help of retrival strategy.

24:32

Like we will build some strategy that is there.

24:34

It could be.

24:35

depending upon anything, like we have a retrival scenario using which we figure out the top K results.

24:41

Then those results will be sent to what? It will be sent to a LLN.

24:45

So here I will be using what LLN. I will be using in today's last GROC LLM that is there.

24:50

So you will see this that GROC is another LLN which will be used to generate the final answer.

24:55

Whatever final answer in English language we want, we will try to generate it.

25:00

And that will be done with the help of LLM.

25:02

What will be the LLM? It will be GROC.

25:04

So this entire

25:05

component will be our what component this entire component will be the retribal component that is there and the other component that we are writing is the ingestion component I think both these components scenario you are able to understand right and this entire thing will make what this entire thing will make a rag system so we can say this entire thing is nothing but a wrap which is retrival augment generation

25:31

Tell here at this part are you able to understand?

25:40

Yes, right, GROQ, GROQ and GROK is different.

25:47

Guys, till here, this part is clear, right?

26:01

Guys, till here are you able to understand?

26:15

Any doubts anyone is having?

26:17

Still here are we good to go, right?

26:31

No, right, Rakesh, you can watch the theoretical part that is there.

26:41

That theoretical part you want to watch right?

26:46

Guys, still here are we good to go.

26:58

This is a very good to go.

26:59

This is a very good question. We have already studied our list, right? Did you miss that class?

27:07

Other people know, right? What is Python List?

27:29

see list is nothing but which is used to store the data that is there all the elements let's say if i want to store all the numbers then what thing i can use i can use a python list that is present right so let's start i think we can start with the project so one by one i'll try to give you all these commands and then we can see all other things that are there so yeah one by one we will see the right which chunking strategy and everything we will use depending upon the data we will choose that

27:56

harsall that part is clear right so let's try

27:59

first i'll go to my visual studio code i'll tell you all the commands i'll do some changes so that you are able to understand very easily so what i'll do is i'll just create a new folder which is project

28:13

and i'll even move like this particular project uh inside this so that multiple coding examples we have here rather than project i'll just rename it to coding examples i'll say these are the

28:27

a coding examples that are there inside these coding examples we have this vector search lab

28:36

here only i'll create another folder which will be let's write today's is this shop cart rag so i can just

28:44

say that let me rename it and i'll say i'll just create a new folder which is shop cart rag so you will see this

28:56

coding example this is the embedding one that we discussed and this is the other one that we are having

29:02

i think you can see my screen currently you don't have to do anything i'll show you all the things that are there

29:08

so let me just to push all the changes i'll just write a basic command to push all the changes

29:18

so that you can see on that particular link also push will happen once we have done this okay i did not

29:26

commit cap no i commit i'll just do git uh the start

29:56

so these are the commands that you can run if you remember in the last class we can first run

30:02

this command which is pip install chroma db do you remember i think those who have already

30:07

run it you don't have to run it again but if pip is not working then what is a command that we can use

30:12

we can use pip three so do you remember that already it will be installed so you don't have to worry

30:18

if you want to update the version then you can update the version but currently it is not required

30:24

we can see here that i can directly write here pip three i'll show you where you can

30:29

write the commands from i think you can see my screen right all these commands that i've written

30:35

one by one you can run them you can create a folder like this as i have created and then you can run

30:41

these commands that are there like these commands will be required in order to run the program program i'll

30:46

give you you just have to copy paste the entire program but before that you can either run with pip command or you can do

30:54

with pip three command that is there so one by one i'll quickly show you with pick three so we can see

31:00

here pip three install chroma db so this is already installed up since we will see

31:06

sentence transformers also will be installed up so i'll just say pick three install this this is also

31:14

installed groc might not be installed for you guys so you can run pip three install grog all all other commands you have

31:24

in the last class for me even grok is installed so you can see it is working so all of you

31:29

can open your visual studio can run this command either you can run pip install like either you

31:36

can run the pip one or you can run the pip three version whatever works for you is that part

31:41

clear these other things you remember right we installed it in the last class in order to run the program

31:48

do you remember that guys do you

31:54

remember that or not API key i'll tell you how to get API key and everything for

31:59

API key also let's try to discuss some steps that are there and then you can get your API key like

32:05

first what you can do is you need to go to this particular link which is grog.com i'm sharing the link

32:12

in the chat as well so you will have to create a account like how do you create account click on

32:18

free API key here it will ask you to sign in you can sign in with a google account

32:24

and once you sign in with a google account you should see you can sign in with the email also

32:29

once you do that you should see option of create API key can everyone open this particular link

32:34

which is groc.com i have shared the link in the chart are you able to open that

32:43

guys are you able to open it

32:45

are you able to create a account very quickly can you create account

32:54

this fits my chair also are you able to create account

33:03

so how you will create account just click on start building also it will open another tab and

33:07

you can create account or click on free API it will ask you to do a sign end and once you have

33:12

sign in can you see such a screen here

33:14

here no API key will come for you but for me so many API keys are coming

33:19

because I've created so many API keys but are you able to see that?

33:27

guys are you able to do that or not

33:35

how many have created a API key how do you create API key?

33:39

Like once you have created account click on create APIG and type in any name

33:44

you can type in any name like you can type here test let's say test class and just click on

33:51

submit your API key will be created up and then you can copy that API key also is everyone

33:56

able to do this mohith in the last class did you install everything necessary

34:01

did you install that particular part whatever we discussed python is installed in your

34:05

system or not is python installed

34:14

How many people are able to create an API key?

34:44

You have just copy it right now. We will use it later on. Everyone is able to create it, right?

34:56

Right? GROC, I think it will be downloaded in some time, so you don't have to worry.

35:04

ChromaDB and a sentence transformer, if you download it in the last class, you don't have to download it in this class.

35:14

So let's try to see here. You can see this that now I'll try to copy paste the program

35:22

one by one and then you guys can also copy paste and then once we run it, we will try to understand what

35:27

we are doing. You can see this that currently very simple program I am writing and we can even discuss

35:33

it that how this program is working. So what I'll do is I'll just write a program for everyone.

35:40

I'll create here another. You can write, give it the same name for

35:44

file. If you want a different name, you can give a different name also. I'll just give it a name as

35:50

rag.p.y. Okay. Now what I'll try to do is I'll paste it here. So you can see this that currently only

35:57

this much code I have written. Let's discuss about this code and then any name you can give to a API key.

36:03

Name is not any like issue. You can give it any particular name that is there. So you can see here

36:10

this particular part. Like if you try to see, I have written in this program.

36:14

what I'm trying to do. I'm trying to import sentence transformers, ChromaDB and GROC.

36:20

This is the entire data that we are having. Currently only I have written this data that

36:25

if I just press a backspace here, you will see it will go. Let me insert it. So currently this is a text

36:34

that unopened items may be returned within seven days of delivery. And if Shopcart, I think this text is

36:41

there. Other things we can write down. I'm not sure why they are not

36:44

written. Ideally, it should be generated up. Let me just generate it another time.

36:52

So you will see this that. We will try to write a complete knowledge base. Inside that particular

36:57

knowledge base, what I'll try to do, I'll try to give all the necessary documents that are there.

37:02

And then I'll tell here about the embedding model. So you can see we are specifying just the embedding model.

37:08

The embedding model here is BG. BG is the, if you remember, Beijing artificial intelligence.

37:14

Institute, right? They are giving us that free model that we can use for embedding.

37:19

For generation, I will be using Lama model that is there. How this Lama model I can use? So you can see

37:26

your program. It will be talking to GROC. GROC is a third party service, right? It's a external

37:32

service that is there. In order to do the talking with this Lama model, right? You need the API key.

37:38

That is why we created the API key that is there, because our program, it needs to talk with a third party service.

37:44

That third-party service will try to authenticate whether who is sending the request.

37:51

So how it will do that authentication? It will do that authentication with the help of API key. Is that part clear?

37:59

Currently, understand the concept that is there, right?

38:02

Purajan, are you able to understand the concept? Currently, you don't have to paste it anywhere.

38:06

Just keep it safe in a text file and then I'll tell you when to paste.

38:10

Guys, is the context clear to everyone? Is everyone able to want to,

38:14

understand this so in order to connect with grog we can see here that we need to use API

38:21

so the main idea is that currently in this data like this is nothing but the list data that we are

38:27

having i'll update this data also so you will see this that currently two models we are using

38:33

what are the two models the first model that we are having here is the bg model bg model bg model is used

38:39

for embedding purpose embedding means that all the english sentences that we are having

38:44

they will be converted into numbers that are there. Those things are done with the help of embedding model.

38:50

The next thing is that for generation, you are using Lama model. This Lama model, it will do the

38:56

generation that user has given this query. How do I reset my password? You will get the necessary

39:02

context from all the embeddings and everything. Generation or final answer will be generated with

39:09

the help of LLM. Who is the LLM here or who is the brain here? The brain is LMA model. The brain is Lama model.

39:14

you are connecting with that NAMA model, you are connecting it with the help of API key that is there.

39:19

Is that idea clear?

39:26

We need to import libraries that are there, right? That is why we are writing that Nupur. I think that part is

39:32

clear. We are importing everything that is necessary for the program. We will see OS and other things

39:37

also will be necessary. So that is why we are importing it. Is that idea clear?

39:44

Yes, right, GROC is a third-party application that will help us connect with Lama model.

39:55

Can you write the doubt in chat, Vareen?

39:59

Till then, let me just update this. Let me open and update the entire thing.

40:14

So I'll update the exact data that is there. So we can see the exact data will be this.

40:34

This is the exact data that we are having. I'll write actually like almost all the things that are there and then we can run it one by one.

40:42

so that properly you are able to understand. So you can see this that I have added the

40:48

necessary comments also. So you can see, first of all, like multiple things we can use.

40:54

Currently, list, dictionary and anything we are using. Like these will be used for different parts

40:59

in a program. Currently, even if I don't write this line, then also things will work. Later on, we can

41:04

import them. We are importing OS because the secret that is there. API key is like your password. It's

41:12

a secret that is present. You need to store it very carefully. I'll show you how we will

41:17

store that secret or API key that is there in the environment file. So in order to get that

41:23

from the environment file, we will be using OS here. ChromaDB is used to store all the embeddings

41:28

that are there. Sentence transformers, they will be used for the BG model and GROC will be used for the

41:34

LLM generation and everything, like for generating the necessary context with the help of

41:39

LLM. So you can see this that in shopcard, all this data is present, that this is a

41:44

textual data, that unopened items should be returned within seven days. This is one data. This is another

41:50

data that is present. This is another data that is present. This is another data that is present.

41:56

So you can see all this data is present. And this is an embedding model that we will be using. And this

42:01

is the generation model that is there. Till here, are you able to understand the program?

42:07

So this is the raw data that.

42:09

we are having. I'll push this much and then we can go to the next part. So you guys can create

42:14

a file, drag.p. And you can copy paste that particular part that is there. So I'll just write

42:20

here this. I'll commit it and I'll push it. So we can see here that once I do this, if I go ahead

42:28

to the next part, you can see here this thing that this content will get updated. So if I quickly open

42:34

here, we can see we have this coding example folder inside which, which

42:39

we have this rag.py in which this kind of code is written. So this file code you can copy

42:45

paste. Till now you don't have to run it. We will run it later on. Currently you can if you want,

42:51

you can copy paste till here this part. I'll paste you the entire code. Every time I will be updating

42:56

the code here only. So you can directly copy paste and run it once I tell you. The model name is

43:02

Lama model that is there. Lama model we are able to get it using GROC. Is that part clear?

43:09

So you can see here this part is clear. So you can see here that currently very basic program we have written. We can see here that basic setup of rag we have done. We have added the data part that is there. Once we add the data part, what do you think will be the next step? Like what do you think will be the next step?

43:39

we will define necessary functions and we will try to like store the data properly chunking and

43:45

embedding we will try to do so i'll directly paste the code of that and one by one we can discuss so you can see

43:51

multiple functions i have created this function will create the embedding model then this function will

43:58

set up chroma and everything like if you remember in the last class also we have seen that we were

44:03

creating a chroma store like if i show you here in this particular part do you remember this

44:08

chroma store got created so we are creating here the necessary chroma store so that all the

44:13

embeddings can be stored then we will encode all the documents like whatever documents we are having here

44:19

right currently all these documents are properly present so that is why no chunking we are doing

44:25

because currently they are present in chunk format only like if you read this you can see here that this is a

44:31

policy chunk that is there this is like return policy chunk this is shipping policy chunk this is

44:38

warranty policy chunk then this is refund policy chunk i'll show you a example where i have

44:44

real life data in that i have done chunking so that also i'll show you but currently you can see the

44:49

data that we are having is already chunked since the data that we are having is already chunked we just need

44:55

to embed that data how embedding we are doing we are doing it with the help of bg model that is there so we need

45:01

to call all these necessary functions once these functions are called then automatically embedding will

45:06

happen and we will see in our chroma store everything will be inserted so let me just call

45:11

all the necessary functions and then we can go to the next part this part of code this piece of code

45:16

are you able to understand that what it is trying to do

45:24

guys this code are you able to understand so one by one let's try to see a good example and then

45:30

understand so first of all what we will try to do we will try to write here this part

45:36

we will call the set of function that is there we will call here like i'll run here setup

45:43

chroma function that is there i can even write the entire program like i can just ask it to run

45:51

the set of function i think this is the set of function right then create embedding where it is called

45:56

is it called during this sentence or warmer embedding model name it should be called somewhere i'm

46:05

just checking that get or create correction so we can see here like first of all what

46:15

should we do we can like first we will try to do this thing we will create a chroma and everything

46:21

once we have created the chroma part then we will try to embed the function like we will do embedding

46:27

part and then we can do the printing part that is there so one by one let's think uh chroma part i have done

46:34

i'll create embedding model but i think it is just returning i'll directly call this here shop

46:42

policy embedding function is none let's directly call the index policy that is there and let's try to run and see

47:04

let me just run it for running part what i'll do is i'll just write here python

47:15

i'll go to that folder i think the folder is coding example so i'll just go there inside this folder i'll go to

47:23

the shopcart rag now i am in the correct folder now i can write python three and i can write ragd

47:31

dot p y so once i run it let's see it will take good amount of time to load embedding model and

47:36

everything and then we can see that part even main function as the things we can write we can even do it

47:42

with the help of clod also i'll show you how we can do it let me just fix that part i think model and everything

47:48

we need to pass the collection and everything we need to store and do it let me do it like i'll quickly write it with

47:56

clod what i'll do is i'll just open this i'll say that

48:01

uh we need to store all the embeddings in the

48:14

the embeddings in the chroma db.

48:31

let it do like i need to like i don't have much time to actually like fix and run all the functions that are there but what we can do is we can ask clod that update the program so that necessary functions are called up because one by one we can see first i need to set up the chroma db i need to store the collection that is there once that particular part is done we will pass it to the index fund function that is there so you can see this is a mean

49:01

function that it has written first we will create a model like once this particular model

49:06

is created then we can call the chroma db function that is there once that particular part is

49:13

done we will update the policy records and everything even for demonstration purpose we can print

49:19

everything i think it will try to print the count in everything later on we can print other things

49:24

also that are there so let's try that like let me just try running this

49:31

now i think it should be able to like run everything you can see that last time also

49:36

this same unauthenticated request was coming right it's a minor warning and we can see four

49:42

policies records are added and if i go here to this particular part i can see my chroma store is

49:48

also created so this means that everything is running up do you remember that how we can view all the

49:54

embeddings that are there what is the function that we can call in order to view all the embeddings

50:01

in order to view all the embedding what function we can call

50:07

peak function that was there right peak function we can call and we can see all the embeddings

50:12

also like if i want to just print a list of all the embeddings then i can even do that i can ask

50:18

laud or i can ask other ai tools that i have integrated and they will update the program and we can

50:24

call the necessary tools that are there currently till here this part you are able to understand

50:31

repeat the entire thing currently till what we have done so we can see here first of all what

50:36

we are trying to do is we are having some normal data this is just an example to show you that how

50:42

rack can work currently this is a data that we are having currently the data is already chunked

50:48

that is why chunking strategy we are not using i'll show you other project that i've created

50:52

we are chunking also we will do with the raw data do you remember that grow hddfc mutual fund

50:58

like do you remember that example that i showed you where the raw

51:01

data i showed you then i showed you the filter data then chunk data and then all the embeddings let's try

51:07

to see that example they are chunking we did so we can see that and then we can go ahead

51:15

let's do that particular part so if you see my other screen i'll zoom it a bit so we can see here that what

51:25

i did is like if we talk about first of all the data that we are having we can see this is a raw data

51:31

that is present in this you can see raw HTML pages are present then i cleaned that particular

51:37

data how did i clean it i wrote a basic python program in order to clean the data this is the

51:42

this is the clean data that is present up once we have the clean data what we will do is we will create

51:47

the necessary chunking chunking means that we will try to like chunk the particular data chunking

51:53

chunking means that divide the data into different different groups that are there and once we do

51:59

this particular part we can see here that chunking will be created like the data will be divided

52:04

into different different groups for all these chunking what we will try to do we will try to

52:08

do we will try to convert this data into numbers so you can see for each chunk we will have a

52:13

sequence of depending upon which embedding model we are using we will get some numbers that are

52:19

there all these numbers will have specific dimensions do you remember in the last class also if i

52:24

use any small model we will get 384 dimensions so you can see three

52:29

384 numbers are there all these numbers they will be stored into a vector db that particular

52:34

part we will do so here you can see in this particular part what is happening in this particular part

52:39

chunking is happening is this idea clear guys this thing are you able to understand

52:51

so in this part chunking we are doing in this particular part we can see this that we have written a program

52:58

which is doing the first component what is our first component the first component is this one

53:03

like if i go back to the google chrome you can see here this is a component i was telling you

53:09

about right that first we have raw data raw data is python list all these data that is stored here

53:15

right if you see in this particular program this part this is the list that we are having in which

53:21

everything we have stored in chunked format then we are doing the embedding for doing the embedding we are

53:26

first calling and creating the model then we are creating a chroma collection once

53:31

we do that we are encoding everything so we can even see the embeddings and everything once this part is

53:37

done we will go to the next component the next component will be the retrival component that is

53:42

present up is the idea clear guys till here the idea is clear to everyone

53:51

so i'll just push this code and everyone can try running the code as well so let me just open my terminal

53:56

i'll directly say get add star most probably i think this thing will not be

54:05

pushed git status we can see rag is updated i'll just configure my email i'll commit it and i'll

54:16

push it so you can see if you go to my git hub uh let's open that we can see here that this is a

54:24

the get up you can see this program is updated now you can copy paste this program and run it

54:30

and you will see this output the main output that you will see will be this one which is that index

54:36

like it will show you that four things are updated correct four things in the policy record

54:42

they are updated and their embeddings are created can you try copy pasting the program and running it

54:48

for running it how what things will be needed you will need here grok like you will need all the

54:54

things that i was mentioning here you will need grok you will need chroma db and sentence transformer

55:00

if pip command is not working use pip three command that is there correct guys still

55:10

here this part is clear in the main function here we are just creating a model right if you see here

55:16

in the main function part what we do let's try to see here in this part you can see this that what i do is like this is

55:24

like this is a main function like whenever you can see the name is main

55:28

whenever we run the program automatically it will go to the main function in main function

55:32

first of all we created a model this model is the bg model this is an encoding model that is there

55:38

it is not a llm it's an encoding model once we did it we created a chroma db

55:43

mean in the last class also you saw right that i was creating a chroma db here for creating a

55:49

chroma db what is a command name or what is a command we can see here that we are

55:54

using this persistent client and we are creating a chroma store inside that chroma store

55:59

we are creating a collection which is this after that once we have done that we are passing two

56:04

things we are passing the collection and the model so that it will extract all the documents this

56:10

code you remember right in the last class also we discussed this code two three times that it is just

56:16

a shortcut way to extract all the ides documents and the metadata it's like running a fall loop and then we are

56:23

writing it it will store all the IDs into proper list it will store all the textual data

56:28

and the metadata once that is done i am using encode function that encode function will convert all the

56:35

sentences into numbers once that particular part is done i am inserting it and you can see that

56:40

once insertion is done we are just printing this part correct is this thing clear guys

56:53

you need to install it right purajan you have to install everything that i told

57:06

if you don't install it then it will not work right we discussed it right that you need to install

57:12

all these things without installing these things it will not work apparently this part you can skip

57:17

but other things you have to install other people is everyone able to do it

57:23

other people are you able to do it are you able to run the program

57:30

yeah right that thing will come up soarshal that thing is correct

57:41

it will download it in a tish right what is the error you are getting what is the exact error

57:53

install API key right jen i told you you don't have to do that right now

58:01

Grog key it will take a time to install it right you need to give it time it depends upon your

58:05

network speed so did are you able to run three commands for a gen did you run that three

58:10

command did you run this particular command PIP 3 install grok is it installed or not

58:18

or PIP install grok did you install that

58:21

did you install sentence trust

58:23

and other things right three things are required did you install all three

58:32

all three we need to install right did you copy paste the program correctly

58:37

you'd have to delete the entire program and then copy paste from starting you need to delete

58:43

the entire program and copy paste check if hundred and six lines you are having or not

58:47

but what is the error it is coming so in the last class also right

58:55

we saw that a warning will come you have to ignore that warning right

59:00

i can run the program again and i can show you that part like if we write here python

59:05

three and we run this particular part so you will see this that

59:11

it will say that basic warning because we are not signing in into hugging face

59:17

that is there we are directly running it that is why that warning is coming this record

59:21

everyone is able to see right index four shopcard policy records

59:32

so you need to install python properly slope and other things that are there

59:36

other things whatever things you have not installed you need to install that

59:39

chroma db you need to install

59:44

so i'll give you the commands that are there like if you see here this particular commands

59:51

that are present these are the three commands the first command is pip install chroma db so

59:58

those who have not installed need to run either pip or you need to run it with pip three

1:0:04

these are the three commands you can try with these commands and let me know

1:0:09

you can either try with pip or try with pip three as i am pasting in the chat just

1:0:15

focus on the chat right now i am pasting the commands again one by one try either with pip

1:0:21

or with pip three it will work it will show you right like rakesh if you see my screen right

1:0:28

you can see here that if i run here pip three install groc it will say already satisfied so this

1:0:36

means that it is already installed if this thing is coming then you

1:0:39

are good to go

1:0:42

varen to you are not listening right in the class i guess i told you need to install grog

1:0:53

did you install grog properly it is clearly showing you the error also no module named grok so

1:1:00

did you install it properly did you install it in the correct environment that is there in windows

1:1:04

it will be installed in a specific environment and then you need to enable that environment

1:1:09

then only it will run.

1:1:20

Directly with pip also you can install.

1:1:23

How many people are able to run it?

1:1:25

Can you type in chart yes?

1:1:29

I'll tell you right,

1:1:30

Archie with the API we will do use that in the generator part that is there right?

1:1:39

at how many people are stuck can you write in chat now if you are stuck

1:2:09

Yes, right, Vareen. Did you run the last program Vareen?

1:2:19

Archer, that is correct.

1:2:21

After three command, you need to copy paste the program that is there, whatever program I have written.

1:2:27

You need to copy paste that program from GitHub, update it in any particular file, and then you need to write Python 3, whatever file name you have given.

1:2:36

That particular thing it is you need to do.

1:2:39

What error is coming?

1:2:46

Yeah, shan the blast class in the last class.

1:2:48

then you have not installed.

1:2:51

That is why it is failing.

1:2:53

Warning is coming. That is okay.

1:3:01

So with the also same error that

1:3:04

sentence transformer you have not installed.

1:3:07

unless and until you install it properly and other things, I think probably it will ask you to install. Yeah.

1:3:17

Other people are able to run it, right? We can see

1:3:21

Pratik, whatever file name you have given that thing you need to create, right?

1:3:28

If you write rag.p.y and if rag.p.y is not there, then it will not run.

1:3:33

And the command that also you have given, right, it's not the Python command.

1:3:36

not the Python command carefully and then do it if you are not able to do it right then what should I say like you need to be in a specific folder then only you can run it right else you won't be able to run it

1:3:50

so other people can try and towards the end we can discuss the other doubts that you are having now we will go to the next sequence of program so just focus on that particular part because you can run it later on also but yeah you need to watch last class recording and

1:4:06

and then only you will be able to see that part so you can see this that even if i update this program and i try to write this particular thing

1:4:14

that what i do is inside the main function i like here only i can do that i can even print the collection like whatever

1:4:25

collection is there we can even print the count of that collection and we can even see the embeddings and everything also so let's try that so that

1:4:33

so that you have a better understanding on how this will happen so let's try to run it again

1:4:38

and we can see the output and first see the output later on you guys can run it

1:4:46

so you can see now it has already created a vector database it has stored everything and we can

1:4:52

see all the documents are loaded up all the chunks are loaded up and all these are nothing but

1:4:57

embeddings that are there so these embeddings are four embeddings are there because four chunks were

1:5:03

and each embedding is of 384 size that is why because 384 dimensions are there

1:5:09

and you can even see all the documents and everything that is there so you this part is clear right that

1:5:15

four documents they are uploaded and their embeddings also we can see till here the output is clear

1:5:22

right to everyone output are you able to understand

1:5:33

yeah so we can see here this particular part let's try to see the next thing that is there

1:5:39

so yeah let's try with the next part so next thing what i'll do is i'll try to build a retrival

1:5:45

function that is there let's talk about that and let's understand the retrival function and then

1:5:50

we can go ahead so i'll just paste that and then later on we can modify the retrival part also

1:5:58

so you can see what i'm doing is i am passing a collection i am passing the

1:6:03

model i am passing a user query and then i will extract like whatever if i want to extract

1:6:10

two things i will try to extract two things that are there if i want top three things then i can

1:6:15

pass that also what it will do is it will try to query the it will try to embed the query let's say

1:6:23

user has given query related to refund policy then we will convert it into embedding

1:6:29

we will ask our chroma db that what are the top case sentences

1:6:33

that are matching related to that once we get that we will store that particular list once we

1:6:40

have that list we will return that list that okay if the sentence was related to passwords then we will get

1:6:47

all the things related to password once we have those things related to password we will return that list

1:6:53

that list along with user query will be sent to llm and llm will be using and generating the final

1:7:00

answer with that so if you see even this thing we did

1:7:03

it in the last class in the last class i like like like if you remember that i was able to find

1:7:10

out the top three ranks that are there and we were printing the ranks and the distances also so

1:7:16

you can check out that particular recording where the same thing we did currently also here same thing i'm

1:7:21

doing i am converting user query into a list of numbers once we have the list of numbers we are trying

1:7:27

to find out uh we are trying to find out what are the closest sentences related to that particular

1:7:33

number once we do that we are finding out and extracting the data that is there i think till

1:7:38

here we are good to go my screen is visible right clearly it's visible everyone can see my screen right

1:7:46

right yeah so you can see here this thing that we can ask claude only that let's try to update and call

1:7:58

everything in the main function so we can see this that uh we can

1:8:03

can call the retrival

1:8:08

so let it will

1:8:33

go to the next step so you can see currently what i'm trying to do currently i'm trying to do

1:8:38

this thing like if you see in this diagram that we are embedding the user query embedding the user query

1:8:44

embedding the user query means that whatever english sentence you are having we are trying to convert

1:8:49

that english sentence into sequence of numbers and we are extracting the top k matches how we are

1:8:55

extracting it we are extracting it with the help of a vector database that we have created here so

1:9:01

using this proper retrival we will do once we have done the retrieval part and we get the top

1:9:06

k results we will go to the next step which is a generator step that is there so this particular

1:9:11

step we will see currently we were seeing the code of this part that we convert the user query into

1:9:18

all the list of embeddings once we have done that we try to retrive the list from the vector database

1:9:24

once we have done this particular part we should be good to go so we can see this that uh let me just

1:9:30

open this part so we can see here that once we have done it will like it has even created a sample

1:9:36

query so if you see here i'll just close it we can see in the sample query that uh all the necessary

1:9:43

chunks are in like called and these are the top matches that are coming even the distance

1:9:49

and everything will get printed so let's try to run this program and we can see everything

1:9:54

this part currently if i want to remove i can just comment it also so that

1:10:00

and everything will be hidden but currently the sample query is that how many days i have to return

1:10:05

item so if you see the data we can see that this should be the matching one and other things also

1:10:12

can match we will see that particular part so yeah let's try to actually run it and see the output

1:10:17

and then we can see currently we are calling for two things you can call it for top three things

1:10:23

five things also whatever you feel like depending upon your retrival strategy you can call anything that is there

1:10:30

so you can see first the embeddings will be created then we will try to convert the

1:10:35

user query into sequence of numbers once we have those sequence of numbers then other things

1:10:40

we will try to do so yeah you can see this that the top k matches for this particular part is

1:10:48

unopened items may be returned within seven days opened or unused items are not eligible

1:10:55

unless they are defective refunds will be created this is the second match

1:11:00

that is having and you can see the distance also the first one is coming with this distance so

1:11:05

currently these are the top two matches that are there if i want to see top three matches i'll just

1:11:11

go here and i'll type here three if i type here three and then again i run the program you will see this

1:11:18

that top three matches it will show so let's try to see that part also and we can see top three matches

1:11:25

the third match will be having a lot of distance so you can see this match is

1:11:30

uh related to the delivery part and we can see that the distance is very very high so depending

1:11:35

upon how many matches you need generally top two three matches we will take all these matches

1:11:41

they will be sent along with a user query to that groc llm and groc llm will print a final user message

1:11:48

that part also we will see till here this output are you able to understand this particular scenario

1:11:55

is clear right user embed query that we have done and the return

1:12:00

tribal part this part are you able to understand or not so depending upon the data we will

1:12:13

take right rakesh we will generally take top three or top five that is there now llm is having

1:12:18

a brain right it understands that which context is actually matching with the scenario and what is not

1:12:24

matching so it will read the everything it will read the user query

1:12:30

it will read all the rants messages that you are having and then it will tell you that

1:12:34

which matches are actually closer other people are you able to understand this or not

1:12:41

guys are you able to understand this or not

1:13:00

let me just push this program and then we can go to the next part you guys can

1:13:08

run it like get status so we can see this program is changed i'll just add it i'll say update

1:13:17

content and i'll configure my email address and i'll just push it this configuration of

1:13:24

email address is not compulsory even without that also we can see like if i go here we can see like if i go here we

1:13:30

we can see i have updated so if you go to rag chatboard you can see this file is updated up

1:13:36

so you can see here that what i did is i created a policy i have created a index building part

1:13:42

where we are retrieving the data once we try to retry our data we are printing everything that part

1:13:48

is everyone able to understand in the like last 30 minutes i'll help you if you are not able to run it

1:13:56

don't worry you can probably share your screen and do it but

1:14:00

but remember what i'm saying just try to think and understand that you need to install three things

1:14:05

very properly grok then chroma dv sentence transformers these three things need to be

1:14:14

properly installed either in the environment in which you are running and then you need to create

1:14:18

a file listen this part very very carefully that inside a specific folder i have created a file rag

1:14:25

dot p.y and then i'm typing here python ragdotpy then only this program will run are you

1:14:32

able to understand this can you try installing everything and seeing like probably for you some

1:14:41

environment and all need to be created you can ask if you have any ai tool inside visual studio code

1:14:48

right you can ask that also to run the program it will run the necessary commands and do it

1:14:52

till here first of all the program is clear to everyone

1:14:56

program are you able to understand

1:15:03

you can copy paste and you can run the program also those who have installed

1:15:09

everything properly they will be able to run it how many people are able to run it

1:15:14

guys are you able to run it or not yeah right then run the program are you able to see the output

1:15:25

also how many people are able to run it and see the output we are great

1:15:31

yeah if top k matches are coming then you are good to go if top k matches are coming you are good to go

1:15:40

let's go to the next part let's try to see the next scenario that

1:15:44

we are having and then we can go to the next part that we are having yes right part you can do

1:15:50

that so you can see once we have done that in the next part what we will try to do

1:16:00

like in the next part we will call the generator part that is there we will try to generate

1:16:05

everything with the llm in order to generate everything with the llm what will be needed

1:16:09

api k will be needed so now api k will come into picture why why why

1:16:14

it will come now because you need to generate everything like and generation part is done

1:16:19

with the help of llm that is there correct that part are you able to understand

1:16:31

let me paste and update the generator code also and then we can see

1:16:44

shall tell you that how that program will run let me just fix it

1:17:14

i am updating the code and i'll tell you so are you aware of what is a dot env file so you can see this

1:17:22

that you need to connect with something called as grok if you see here that inside this grok once

1:17:28

you create your API key only one time it will show so next time if you have if you

1:17:33

forgot and now you did not copy the API key properly you can copy it again that

1:17:39

particular API key is like a password if i have your API key i can call

1:17:44

your grok so you don't have to share your API key with anyone and that API key we will keep

1:17:50

it safe in a dot env file that is there so you will see this that i will be creating another file

1:17:56

that is a dot env file inside which we will be saving the API key that is there so i'll show you that

1:18:03

particular part and then we can go ahead so you can create a API key and only one time it will be visible

1:18:09

like when you are creating it then only you can copy it like i'll just create it again

1:18:14

you can set it to no expiry like if you set it to no expiry it is good to go you don't

1:18:21

have to worry about anything you can just set it no expiry you can see apexe is visible i'll copy it

1:18:28

now once i am done copying i need to create it where i need to create it inside my like you need to

1:18:35

actually create it in your vs code near to that particular file that is there so if i show that particular part

1:18:43

let me just show you that part also and once like i'll show you that part but is everyone

1:18:49

able to create a new API that is there you might have to install other things also

1:19:00

like other things like import command also i'll tell you what you need to install API other people

1:19:06

are able to create and copy it

1:19:13

i think by mistake i edited the main function let me fix that also

1:19:33

you can share the screen after 930 and then we can do it but currently are you able to run the program

1:19:43

what is the error that is coming so everyone has to run this command i'll paste in the command

1:19:55

before that i'll try to update my API key and then i'll tell you the command also that you need to run

1:20:00

so one by one we will see all the necessary steps that are there and then we can talk about

1:20:11

so you can see here that what we need to do is we need to create a new file like all of you can create

1:20:19

this new file that is there you can see here where your rag dot p y is there right i'll create a dot env file

1:20:26

so you can see this file name i'm giving is dot enbb and b and b and i'll see this file name i'm giving is dot env and i

1:20:30

paste here groc API key and then i'll paste my API key whatever API you are having right

1:20:36

you can paste it you don't have to create this dot enbd example file that is there you don't have to do

1:20:42

that but i'll tell you that i'll even upload it on GitHub so that you understand the format

1:20:49

what you need to do is you need to create a file that file name will be what the file name will be

1:20:57

that file will be here only the name of the file will be dot

1:21:00

and inside that you can write groc API key i'll paste it in the chart also and then you need to

1:21:08

write your API key joe be whatever you have copied your API key right if you have not copied

1:21:15

it properly copy it again and then write it so you can see that particular part you need to do once

1:21:20

are you able to do that part till then i'll like push the program and everything else so that i can

1:21:27

like share with you also these things and then we can

1:21:30

see i'll tell you what are the necessary commands that you need to run so yeah let's do that

1:21:40

let's see what is getting added so we can see only these things are added up i'll try to add get

1:21:47

ignore also i'll try to add dot envd example file so this is an example file that i'm adding you

1:21:55

need to create a file similar to this you you need to create a file similar to this you want to this

1:22:00

this kind of file the name of the file will be dot env where you will write

1:22:06

the API key but it will be similar to this correct so even the steps are written there so you

1:22:12

can do that let me push all the steps over get up and then we can do it

1:22:22

so yeah let's push it so we can see here one by one if i go to my get up

1:22:30

like if you go to the get up part and just refresh here so multiple files will be created i think

1:22:37

pi caches should not be there i think we can even remove it i'll just remove it uh pie caches should

1:22:44

not be pushed but yeah you can see this kind of file you need to create in your rag dot p y also

1:22:50

the program should be updated up you can see that we are calling the client that is there and we can see

1:22:57

i'll update this prompt and everything i'll explain you all this part but before that what

1:23:03

is the thing that you need to do you need to update your API key similar to this particular file

1:23:09

which will be groc API key equal to and what you need to do you need to install other things

1:23:14

what are the things that you need to install let me share you another command and show you that part

1:23:20

so we can see the command will be pip installed dot env so everyone can run this

1:23:30

command either you can run it with pip 3 or you can run it with this then only your like program

1:23:38

will work later on so i'll show you how to even run that as well i have pasted that command in the chat

1:23:45

so you can see i'll just write for me pip does not work that is why i

1:23:50

you pip 3 and for me it is already installed so you guys can run pip 3 install python

1:23:57

env so that everything is stored in env file as well till here this part is clear

1:24:20

all here this part is clear this part is clear this part is everyone able to understand

1:24:50

other people is everyone able to do can you write in chat if you are able to create your dot env file

1:24:58

write in chat if you are currently program you don't have to run currently you don't have to run the

1:25:03

program you just have to create a dot env file are you able to do it

1:25:08

which is similar to dot env example file and your program is also updated right we will discuss

1:25:15

the program later on but currently i think this thing is clear

1:25:20

one is able to run this command dot env this command are you able to run you have to create

1:25:33

only env file you don't have to create the other files so yeah after this we will do the generation

1:25:40

step i think we can take a short break and then we will do the generation step and then the entire program

1:25:45

will be completed up so that but also we can see till here is everyone able to

1:25:50

follow whatever we are doing step four is clear right guys step four are you able to

1:25:59

understand later on other things also we can do but till here i think we are good to go right

1:26:11

but main thing is that currently your program latest one will not work because

1:26:16

for this part we need other things also so it can happen that it can fail let me try

1:26:24

if it is able to work or not then we can probably after the break we will discuss and study the

1:26:30

program in detail once we have studied the program then again we will try to run it but let's

1:26:36

see if the output is coming or not yeah so probably i think it will be working for other people

1:26:46

it is telling the grounded answer also like for example if the question is how many days

1:26:51

i can return so it is saying that you have seven calendar days to return an unopened item

1:26:57

and this answer is coming from grok correct right is this thing clear

1:27:05

this part are you able to understand so if you run it latest then probably it will come up

1:27:16

and you can try running it if you have done set up correctly if your env keys there or not

1:27:21

and these things are there then only it will work let me check if it is importing the API key or

1:27:27

not it is sending the prompt it is sending the context and it is calling the sample data

1:27:39

create glock client where is this function yeah so it is getting the API key correctly also and it is not

1:27:46

if you this error is coming that means your API key is not set correctly so if you see that

1:27:51

if you see this particular answer you are good to go

1:27:53

go

1:28:00

till here this thing is clear right i have already pushed the latest code for the retrival part the

1:28:09

the latest code is already present till on get up we will study this program but till till then you can't

1:28:13

study this program but till then you can run it with API and then later on some more

1:28:18

changes we will try to do you can see the program is up to date uh you can see these two

1:28:26

functions i've added but these two functions we will study after the break that is there

1:28:30

yeah i think we can take a short break and then we can see till here i think this part is clear

1:28:37

right we can have a short break and then after that we will study the program so i can keep our eight

1:28:43

let's break and then we can go ahead

1:29:13

you know

1:29:43

Thank you.

1:30:13

Thank you.

1:30:43

Thank you.

1:31:13

Thank you.

1:31:43

Thank you.

1:32:13

Thank you.

1:32:43

Thank you.

1:33:13

Thank you.

1:33:43

Thank you.

1:34:13

Thank you.

1:34:43

Thank you

1:35:13

Thank you

1:35:43

Thank you

1:35:45

Thank you

1:35:47

Thank you

1:35:49

Thank you

1:35:51

Thank you

1:35:53

Thank you

1:35:55

Thank you

1:35:57

Thank you

1:35:59

Thank you

1:36:01

Thank you.

1:36:31

Yeah guys, let's start with the next part. I think till here is, let's start with the next part.

1:37:01

Is everyone able to run? Did you try running the program?

1:37:12

Yeah, I think everyone is able to run. Right. If you are stuck with any issue, we can discuss that. Let's like try to wrap up almost everything that we are having. I think you can see me as well, right? Yeah. So let's start one by one. All the things that we are having. Let's try to discuss this program and then we can go ahead.

1:37:29

So you can see that currently what this program is doing. Let's talk about all the functions one by one and then we can go ahead.

1:37:37

So you can see this particular part, the starting part, is just all the chunks data.

1:37:42

Whatever data we are having in the program that is present in all these chunks.

1:37:46

These chunks are basically acting as a knowledge base and these chunks are getting converted into numbers, which are actually the embeddings.

1:37:54

So that particular part is done where you can see first we are creating an embedding model.

1:37:58

we are using that particular embedding model inside this particular part where you can see proper embedding and everything is done.

1:38:07

So I can just probably cut this and paste it at the start so that you have a proper understanding on how this program is working one by one.

1:38:17

So we can see here that first embedding model is created and then embedding is done.

1:38:23

Then what we are trying to do like before that you can see that we have written

1:38:28

this particular function. This particular function also, what it does is it actually creates a chroma div.

1:38:35

Like all these embeddings will be stored inside chroma div. So you can see that particular part is done here.

1:38:41

So you can see this all this code, right? The first part of the code.

1:38:45

This is doing everything related to the ingestion component. It is creating an embedding model that is taking the raw data or the chunk data that we are having.

1:38:54

And it is converting it into proper embedding and then it is storing it into a chrome.

1:38:58

database. So this particular part is happening. Once we see this particular part, then what we try to do is,

1:39:05

we try to retrive the data. So you can see this particular function will come up, which will do all the

1:39:11

retrival part. So I'll paste it after that. So we can see this is the retrival part. That once we have done

1:39:21

the chunking, we will try to retrive the data based on the user query. So if you see the main function,

1:39:26

first we load the model, we create.

1:39:28

a chroma dv. We store everything into the chroma db after the embeddings. Then we take a query.

1:39:34

We extract the chunks. We get the rank of the chunks that is there. Once we get that,

1:39:40

then we are creating a grog client. So you can see we create this particular grog client that is there.

1:39:46

How we are creating the grog client. We have imported groc library. This library can only be imported

1:39:52

if you have installed grog that is there. Once you install grog and you have imported and created a

1:39:58

GROC client. This client will get a API key. This API key is coming from the ENV file.

1:40:03

EnV file is which one. This is the ENV file. Inside which we can see API key is also present.

1:40:09

Once we do that particular part, we can see this that our GROC is integrated. Once that particular part

1:40:16

is done, we can see we are generating the grounded answer. So that particular answer is generated

1:40:22

with this particular function. Inside this function, I'll explain you what all thing is happening.

1:40:27

So one by one, let's paste this function above. And I'll push this program also so that proper flow you are able to see.

1:40:34

So you can see this particular function. First, it uses a prompt. This particular prompt is a system prompt.

1:40:41

We need to tell GROC right what to do. So whatever prompt we are sending to Grog, we are writing it in this particular function.

1:40:49

So you can see I'll just paste it here only. So now you can see the code is properly formatted. And we can see first, we are

1:40:57

extracting all the necessary chunks, like whatever ranks we got, we have extracted that and we are

1:41:03

storing it into this context block that is there. Then what we are trying to do, we are trying to say

1:41:10

that you are a shop cart support, customer support person. So here we are using all the techniques that

1:41:17

we studied in prompt engineering. Do you remember all the techniques that we studied in prompt engineering?

1:41:22

All these techniques we are using here and we are saying that answer to the

1:41:27

question using all the policies that we got below all and we have given some

1:41:34

rules that are there all the policies we are adding from this context block all the query we are

1:41:40

getting here and we need to tell the final answer in this format so this is a system

1:41:45

prompt that we have provided this particular prompt will be called with the help of this thing

1:41:53

like we will in order to call the model we are writing a function

1:41:57

that particular function what it will do is we will provide the model name we will

1:42:02

provide that you are a system and you are a support assistant that is there and then we will

1:42:07

pass in the prompt whatever prompt is generated in this particular part this prompt will

1:42:12

contain all the necessary instruction it will have the proper context where it is getting the

1:42:18

context the context is coming from the retrival part if you see this particular retrival thing that we

1:42:23

did right where we are retriving all the chunks so you

1:42:27

can see these chunks we are fine passing these particular chunks they will be going to the

1:42:33

prompt and once this prompt everything we have extracted properly from the chunking part

1:42:38

we are storing it into the context blog and then we are passing the user query and then it will

1:42:44

generate and once it has generated a proper response we are just printing it so this is what is

1:42:52

happening in this entire rack program i'll push the latest program also but same kind

1:42:57

of output it will generate like for example if i just write here python 3 rag

1:43:02

dot p y you will see this that same thing will happen is this thing clear this what are you able

1:43:09

to understand program are you able to relate from my end the voice is very clear right now

1:43:18

so you can hear me only can you hear me

1:43:27

not return right where we are writing this is not a user prompt here we are just calling

1:43:31

the model that is there we are passing two messages that we are just telling it that we are setting

1:43:37

up a particular context that is there once we set up a context then we say that okay this is a prompt

1:43:43

that is coming to you in this prompt you can see it will be reading everything in detail that particular

1:43:49

thing we are trying to do even i can write it with a tab spaces also i don't think it will cause any

1:43:55

issues but yeah we can write it like this also even that part works we can see output

1:44:01

is also coming up and this is the output that is there and if i just go here and i write here

1:44:07

python 3 rag dot p y you can see that it will run again and everything will be good to go i'll

1:44:13

just push the latest changes as well so that you can read and understand the program in a better way

1:44:18

so let me do that i'll just say git status i'll say git add

1:44:25

rack dot p y git commit update content and get push origin so now you can see a full program

1:44:33

with a specific flow i have written where we can see this particular part that you can see first we

1:44:40

have the data part then we have a embedding part that is there where we do everything with the embedding part

1:44:46

then we are doing the retrival part then we are creating a grog client then we are updating the prompt that is there

1:44:53

once we update the prompt we send a message to grok and once we have done that we can see our

1:44:59

entire rag is good to go so this exact diagram that is there right we have implemented and we are good

1:45:06

to go is this part clear this part is everyone able to understand this part are you able to understand

1:45:19

now more queries we can attach and we can do that like we can do that like we can

1:45:23

can write a lot of other things also like for example currently we can even just call the

1:45:29

llm also even that particular part we can do if i don't pass the prompt then to i think nothing will

1:45:34

happen so let me just see if we can add more prompts and everything

1:45:39

we can add more queries

1:45:47

i'll do directly the queries with the rag part so that particular part let me update

1:45:59

till here the program is clear to everyone right

1:46:17

we can even print the retrival chunks that are there

1:46:44

and see i am just trying to write a better program so that one more very good demo we can see

1:46:50

and then we are good to go like that is it from that class one more demo i'll show you very quickly

1:46:56

and then we can see till then if you are having any doubts can you write in chat so that we can see that part also

1:47:14

you know.

1:47:44

Thank you.

1:48:14

i am updating the program in the background and let's do that

1:48:31

let's do that till here let me know what you are having in the program that is there

1:48:44

we can even discuss it this flow you are able to understand right i'll just just zoom it a bit

1:48:50

so i think everyone understands this particular part that first we are loading the model once we can see we

1:48:58

have loaded the model we have done the embedding part collection part and everything we are running a sample

1:49:03

query we are extracting the top k matches that are there once we do that particular part we are generating the

1:49:09

answer with the help of this now one more thing that you need to see if you open

1:49:14

your grog.com right you can see here is a section of API key if you click here

1:49:21

dashboard and you click here last one hour can you see two API calls are there because two

1:49:27

times we have run the program it will take some time for you guys to reflect so you can if you are

1:49:32

seeing two blue pyramids like this right or triangle like this then you are good to go this means

1:49:38

that your grok is properly connected are you able to see that

1:49:44

are you able to see that or not like if you open grog dot com open grog dot com and click on free

1:49:53

API key where you see API key right click on dashboard and click on here in dashboard only

1:49:59

if you see uh last like if i just show you here just click on last one hour and refresh so if you

1:50:08

have run the program some minutes back then it will take like it will take good amount of time

1:50:14

for you guys reflecting me it will take 30 minutes so after 30 minutes you can open and you can

1:50:19

check if you have run the program it won't be empty it will show uh these kind of pyramids like i have

1:50:25

run it twice right that is why i can see it takes time to reflect it's like if i run it again right

1:50:31

more calls currently are not coming up so it will take like around one or two show you so you can even

1:50:37

see that particular part but is everyone able to see some call when you run it around 915

1:50:44

915 data i think some people can see those who have run the program and properly connected

1:50:50

with grog they will be able to see that part otherwise it won't be visible directly

1:51:03

guys still here are we good to go are you able to see can you open and try

1:51:12

so i've updated the program also

1:51:14

let me show you the output if everything is good to go then we can go ahead and we can see yeah

1:51:21

right whenever you run the program it will show the time of that only joe b you

1:51:25

every you ever run the run the program i have added here more queries and i have

1:51:33

like added a lot of things so let's try to see it so you can see here that currently what it will do is

1:51:44

it is printed like i have added a lot of things like one by one we can see so you can see

1:51:51

first what i did is i asked this particular question that uh how i can like how many days i can

1:51:58

return item so you can see this is the rank one the distance is getting printed or not like

1:52:05

currently you can see this is the distance that is coming this is the rank two sentence this is the rank

1:52:09

three sentence and this is the output that is coming then the next question is

1:52:14

i received my phone case yesterday how many days i have it to return it so you can see this

1:52:21

is the first matching one this is the second matching one and we can see you have six calendar days to

1:52:28

return it and this is a scenario that is final answer is coming same way you can see the next part also

1:52:34

will express shipping reach my address in a metro city by tomorrow so you can see that standard

1:52:42

delivery is matching the one then refund is matching and the final answer that is there that

1:52:48

according to the delivery policy we can see that it will take one or two days to print the output

1:52:54

then we can see another question i have asked my earphone stopped working after 10 months is the

1:52:59

repaired or not so you can see automatically this sentence is matching and it is generating a good enough

1:53:05

response that is there same way you can check it for the next sentence also will the refund

1:53:12

be via upi it is matching with this particular part and we can see the final answer is this

1:53:18

so i've added like multiple queries you guys can run this program you can see all the like all the

1:53:26

ranks and everything a lot of ranks and everything is getting printed so you can see with

1:53:30

every question i am printing proper rank and then i am printing the answer also so a lot of

1:53:37

things you can see i'll just push this program also and i think we are good to go

1:53:42

so i have just added that particular part i'll add here rag dot p y and i'll say get comment

1:53:50

update content and i'll push it because i have called it that way right rakesh if you see here

1:53:59

every time i'm calling top two ranks that are there when i was calling here i am calling top three so

1:54:05

if i want i can change it to again two then only top two results will come up that idea is clear right

1:54:11

you can change this number and do it right like currently i'll just update it to top two only

1:54:22

if you want top five that also you can see guys this program are you able to understand now you see

1:54:28

right that how our rag is working and how it is generating our data that part is clear

1:54:41

guys still here this part is clear can you see i've updated the program here also so all of you can refresh

1:55:01

here and you can see the latest program with multiple user queries i have added and you can see i've

1:55:08

you can see i have created one more function this function is this function will retrieve the

1:55:12

chunks it will print the retriving chunks also and it will print a final grounded answer also so

1:55:19

everything i've added here this chunk is just for printing thing like for printing you can see

1:55:25

beautiful output was coming up right here if you see if i just run it again you can see that

1:55:31

a lot of hashes and everything was coming up right it is just for that particular purpose so you guys

1:55:38

can even run it and like if your API key and other things are connected properly you should

1:55:42

be able to see it is the program clear to everyone is everyone able to understand the program

1:55:49

you can copy paste and run it and let me know if you can see this will be a very big output

1:55:54

but you can see multiple queries i have added that is why so much big output is coming

1:55:59

till here are we good to go

1:56:11

guys still here are we able to understand

1:56:17

is everyone able to understand this program how many people are able to run it and see such a big

1:56:22

big output are you able to do that so you can see this that so you can see this that

1:56:28

that this thing is coming up and you can see this example also correct right

1:56:39

yeah i think till here the rag part is here right in the next class let's talk about a little bit

1:56:45

theory and that revision also we will do for similarity search internally it is using

1:56:55

using cosine similarity right cosine similarity is only calculating the distance

1:57:00

correct that also we can configure you can write a function for that and you can override the function

1:57:07

also you can ask claude to change that particular part it will definitely change it you can set it to

1:57:12

anything like whatever mechanism you want you can do it currently the inbuilt chroma dp function

1:57:18

that is there it will use cosine similarity only to find out the latest sentences that are there

1:57:25

Is that part clear?

1:57:32

Guys, this thing everyone is able to understand.

1:57:35

So later on if you see whenever we are building a customized rag like this, right?

1:57:40

Even this project I can share, you guys can go through that particular project also.

1:57:44

This is a big project where I've used rag in a real life application.

1:57:49

So that also you can try and you can use it.

1:57:52

Let me just share you that part also.

1:57:55

you can see this that here i've done that like here that particular same rag i'm

1:58:06

showing you right same rag is present you can see other rag also like this is another rag that i

1:58:13

built so you can even see that but here everything is customized but that is a big enough project

1:58:18

probably if i make a video of that also i'll share you that much big project we cannot make in a single

1:58:25

class we need like around good like five eight classes that are there

1:58:32

yes right jatin that is correct i've shared you two links in which you can see big

1:58:37

rag demos are also present so you can even check that out

1:58:45

till here we are good to go right

1:58:55

Yes, right, no port that is correct.

1:59:07

Guys, still here is everyone able to understand the program

1:59:15

Because the embedding numbers can be different for you, right?

1:59:17

The queries like the number, it is storing, it depends upon the sentences, right?

1:59:23

That which embedding model it is using and how that is.

1:59:25

embedding model is generating the result so that embedding model can generate different

1:59:30

results for different people right like for you it will generate a different result for me it can

1:59:35

generate a different result even though the sentences are same because it's it's based on a prediction

1:59:41

model like it's predicting it understands some meaning of the sentences and then it's predicting everything

1:59:47

so it's not every time that you will get the same distances the distance can be different correct

1:59:52

I read the embedding model internally is using prediction mechanism right to understand the words like it is saying that king

2:0:01

for the numbers are queen can be different every time right that part are you able to understand up

2:0:08

other people are also able to understand right that every time it will not generate the same numbers

2:0:14

even though the sentences are same it's not 100% guarantees that the number will this thing

2:0:22

this part is clear is everyone able to understand the program right

2:0:40

is the program clear to everyone now how many people are stuck and like for you if let's say this thing is not working

2:0:52

whatever we discuss is clear right i have added the program i'll share you the detailed

2:0:57

program and working on get up also i am pushing that in the background but for how many people the

2:1:02

program is not working first of all how many people are able to understand the program

2:1:08

rather than the ppt you can use another file that i'm uploading and you can use that how many people

2:1:14

are still stuck can you raise your hand or probably let me know how many people have understood everything so

2:1:21

basic rag is clear right you can read the program and later on whenever you want

2:1:26

you can make similar function like this whenever required that particular thing you can do so yeah

2:1:32

even that particular part can be done up now those who are stuck did you install everything dot env

2:1:38

kroma db sentence transformer and other things did you install i am posting the notes of today's

2:1:46

class as well so first we can check that out and you can go through that there more

2:1:51

things I've added and those parts also you can read.

2:2:21

Let me push that also and then we can see.

2:2:51

so if you open the get up you can see here this particular part that that is uploaded up so we can see

2:2:59

section session 20 notes are also updated so you can directly open that you can read this

2:3:05

file and you can see everything that we have written related to the program along the diagram

2:3:09

is present so rakesh fatale it is clearly saying right that chroma dp is not installed you can

2:3:15

read there right no module name chroma db did you install chroma db

2:3:21

did you install that particular part share your screen i'll give you the necessary permissions

2:3:29

did you set up the environment environment have you set up yesterday the program was running

2:3:38

yesterday was the program running yeah right harchid you can set it up on your

2:3:50

personal laptop in office laptop it might be blocked

2:3:53

so yesterday maybe for yesterday i have said the environment but it was not uh running

2:4:03

share your screen

2:4:23

type here pep install just don't type here

2:4:33

right the hair to we don't have to run it

2:4:36

where run it in that terminal right there to run in that terminal

2:4:38

there type for pip install chroma d bha one bar

2:4:41

dv one

2:4:45

spelling is wrong

2:4:47

now one-one-three python three python three or pip-three or

2:5:03

python run go if pip-p-krre then you say python look like python pip-three

2:5:08

care you so that will be it so it will bep-three are both are

2:5:13

and python and that's the is about are python and that's the is about are you

2:5:16

Sir, so, what do you?

2:5:18

PIP three?

2:5:19

No, yeah,

2:5:20

yeah, first PIP three,

2:5:22

install

2:5:23

PIP three install

2:5:24

Cromadiv.

2:5:25

So that's right

2:5:27

you're doing.

2:5:28

You're the wrong.

2:5:29

You know,

2:5:30

you know?

2:5:31

Yes, sir.

2:5:32

You

2:5:34

now type

2:5:35

Python,

2:5:36

I think you're

2:5:37

there's a

2:5:38

type,

2:5:39

Python,

2:5:40

uh, space.

2:5:41

Now that

2:5:42

the file is,

2:5:43

Rack.

2:5:44

P.

2:5:45

Or, you know,

2:5:46

Enter

2:5:48

now.

2:5:50

Now,

2:5:51

see,

2:5:52

clearly he's

2:5:53

that it's

2:5:54

now

2:5:55

again,

2:5:56

now,

2:5:57

sentence transform are missing,

2:5:58

so sentence transformer

2:5:59

comment,

2:6:00

write.

2:6:01

one,

2:6:02

first,

2:6:03

PIP 3,

2:6:04

install,

2:6:05

and

2:6:07

write

2:6:08

sentence transformer.

2:6:09

I'm

2:6:10

you,

2:6:11

copy, paste,

2:6:12

give,

2:6:13

and give them.

2:6:15

And you

2:6:16

you

2:6:17

be

2:6:18

you

2:6:19

do

2:6:20

it.

2:6:21

it would

2:6:22

you

2:6:23

know,

2:6:24

you know,

2:6:25

one,

2:6:26

you know,

2:6:27

PIP and PIP

2:6:28

and PIP 3

2:6:29

do,

2:6:30

two

2:6:31

one of one

2:6:32

will go and

2:6:33

and then

2:6:34

then run

2:6:35

to run

2:6:36

two minutes in

2:6:37

run it.

2:6:38

You know

2:6:39

I'm

2:6:45

or you

2:6:46

or you

2:6:47

didn't

2:6:48

do

2:6:49

it.

2:6:50

No,

2:6:51

you

2:6:52

paste

2:6:53

and

2:6:54

enter

2:6:55

now

2:6:56

it's

2:6:57

now

2:6:58

it's

2:6:59

so it's

2:7:00

not

2:7:01

it's

2:7:02

this

2:7:03

Huging face installation

2:7:04

but I think

2:7:04

NAMPai

2:7:05

is

2:7:06

now install

2:7:06

to it

2:7:07

wait

2:7:07

and wait for what

2:7:08

and then

2:7:09

then you

2:7:10

then then B and B

2:7:11

B and B

2:7:12

I think it's installed

2:7:13

and B

2:7:14

command

2:7:14

and

2:7:15

you can

2:7:16

and

2:7:17

if you

2:7:18

and you

2:7:19

can't

2:7:20

run

2:7:21

and

2:7:22

let

2:7:23

run

2:7:24

other

2:7:25

other people

2:7:26

are you

2:7:27

able to

2:7:28

what is the

2:7:29

issue that if

2:7:30

you are

2:7:30

if these

2:7:32

things are not working

2:7:33

then just

2:7:34

run the

2:7:34

command properly

2:7:35

right

2:7:36

now.

2:7:37

Now you

2:7:37

look you

2:7:38

you're

2:7:39

you know

2:7:44

you're

2:7:45

same

2:7:46

you know

2:7:47

now

2:7:48

you're

2:7:49

you're

2:7:50

you're

2:7:51

so

2:7:52

we're

2:7:53

we're

2:7:54

we're

2:7:55

you're

2:7:56

you're

2:7:57

you're

2:7:58

and then

2:7:59

you're

2:8:00

you're

2:8:01

what you're

2:8:02

installed

2:8:03

here

2:8:04

here

2:8:05

here

2:8:06

you're

2:8:07

you're

2:8:08

you're

2:8:09

you're

2:8:14

Okay, you're

2:8:16

you're

2:8:17

you're

2:8:18

you're

2:8:19

you're

2:8:20

you're

2:8:21

or then you

2:8:22

or then you

2:8:23

you're

2:8:24

you're

2:8:25

you're using

2:8:26

okay

2:8:27

or we're

2:8:28

either we're

2:8:29

or we

2:8:30

or we're

2:8:31

or we

2:8:32

we're

2:8:33

we

2:8:34

we're

2:8:35

like Python, like

2:8:35

Python use

2:8:36

and PIP use

2:8:37

and this

2:8:37

this scenario

2:8:44

you

2:8:45

install

2:8:46

you're

2:8:47

I've

2:8:48

I've

2:8:49

have

2:8:50

that I've

2:8:51

can't

2:8:52

and then

2:8:53

then you

2:8:54

you can't

2:8:55

you can't

2:8:56

go

2:8:57

you can't

2:8:58

stop

2:8:58

you

2:8:59

don't

2:9:00

you

2:9:01

don't

2:9:02

then you

2:9:03

I'm

2:9:04

installed

2:9:05

you're

2:9:06

you're

2:9:07

you're

2:9:08

you're

2:9:09

you're

2:9:13

I'm

2:9:23

share

2:9:24

you

2:9:25

you have

2:9:26

you

2:9:27

share screen

2:9:28

screen

2:9:29

on

2:9:30

you

2:9:32

and

2:9:33

V

2:9:34

VAS code

2:9:37

go

2:9:38

Go

2:9:39

on

2:9:43

Now, now, now, now,

2:9:47

now, now, now,

2:9:48

now,

2:9:49

now

2:9:51

type

2:9:52

and then you

2:9:53

and just

2:9:54

Python and this

2:9:55

file.

2:9:56

Pyl.

2:9:57

this is

2:9:58

I think you're

2:9:59

in

2:10:00

this in

2:10:01

hide

2:10:03

click

2:10:04

just a

2:10:05

here.

2:10:06

clear type

2:10:06

here

2:10:13

just file

2:10:15

you

2:10:16

enter

2:10:17

you

2:10:18

you're

2:10:19

you're

2:10:20

you're

2:10:21

you're in

2:10:22

you're in

2:10:23

you're in

2:10:43

I don't know what are you going to do what you want to do?

2:10:58

What are you?

2:10:59

But you are not what going to do you?

2:11:07

I have installed chroma DB but it was not running the command right?

2:11:12

command right just open that agentic system design folder that is there

2:11:17

this is not the local disk C may have

2:11:33

this is not the correct folder

2:11:42

where is the folder now?

2:11:47

I'll share my screen in a minute.

2:11:51

Probably in the next class you can share because currently it's already 10

2:11:56

so yeah but you need to just understand that that you are not in that module folder

2:12:02

that module you need to go and then you need to run the command.

2:12:08

Currently your file is not opening. Are you getting my point?

2:12:11

that much too you should understand right like currently if you see that currently I am present in the shop rack share see my screen that see my screen first of all

2:12:27

Yes

2:12:29

I am present inside this shop card folder that is why I can write that program because inside it this rack dot file 5 is present so what I did is that you can write this CET

2:12:38

is present. So what I did is that you can write this C.

2:12:41

command right from cd you can go into the folder you need to type module one then you need to

2:12:46

type module two you need to go into the proper folder and then run the program getting my point

2:12:55

getting my point

2:12:59

otherwise it will not run right that is very very basic try that

2:13:05

in the next class we can see it's already 10 so in the next class we can see it's already 10 so in the next class we can see

2:13:11

other people also we can even schedule extra class you can request masai team to

2:13:14

schedule extra class where we can resolve the doubts related to that i think whatever

2:13:21

we discuss is clear to everyone right so man grakash patil you need to run grog command that is

2:13:28

there right did you install grog error is coming in program

2:13:34

did you install grok properly what error is coming

2:13:41

error not here.

2:13:42

So what doubt then?

2:13:44

We are importing here GROC, right?

2:13:58

Currently for free thing, like GROC is a free LLM, right?

2:14:02

You don't have to enter your credit card details.

2:14:05

That is why we are using GROC.

2:14:07

GROC from GROC from GROC to import

2:14:08

are doing it?

2:14:09

What is a doubt?

2:14:10

Like, what is a doubt here?

2:14:11

Rakesh, this is this?

2:14:14

Rakesh, this time you have you

2:14:17

Rakesh, this bar, if you have

2:14:32

not you've got to have it, then, then tell you.

2:14:35

PIP 3 and PIP

2:14:42

and PIP 2nd of 2nd of 2nd of 2nd of

2:14:44

share

2:14:45

one screen

2:14:47

1.

2:14:48

First, screen.

2:14:53

First type type

2:14:58

type here,

2:14:59

PIP type here,

2:15:00

PIP install GROC.

2:15:01

PIP install GROC.

2:15:05

Now he has installed

2:15:10

here, now.

2:15:11

Now, run with Python.

2:15:12

Now, now, run with Python.

2:15:13

Now, how?

2:15:28

How it's it?

2:15:32

You're not installed.

2:15:33

You're not?

2:15:34

are you

2:15:36

you?

2:15:37

You're like, you

2:15:38

can't

2:15:40

this one?

2:15:41

I think that I've got

2:15:42

I think that

2:15:43

you

2:15:44

did you?

2:15:45

No,

2:15:46

no,

2:15:47

here?

2:15:48

No, here.

2:15:49

So,

2:15:50

then, then

2:15:51

you can't

2:15:52

you?

2:15:53

What?

2:15:54

What?

2:15:55

What are?

2:15:56

So,

2:15:57

that?

2:15:58

So, then, then,

2:15:59

they're

2:16:04

Now you know

2:16:05

you

2:16:06

have

2:16:07

so that

2:16:08

it's not

2:16:09

so

2:16:10

you can't

2:16:11

see

2:16:12

okay

2:16:13

Okay,

2:16:14

okay, sir,

2:16:15

okay,

2:16:16

no problem.

2:16:18

Yeah,

2:16:20

Copel, I think you can take over, yeah.

2:16:22

Alright,

2:16:24

um,

2:16:25

I have just one

2:16:28

query.

2:16:29

We had a session on

2:16:31

this ChromaDB installation on last

2:16:33

last Tuesday.

2:16:34

And I'm not sure why you guys are not able to install these things today as well.

2:16:42

So can you please quickly write your issues here so that I can understand why you were not able to do that.

2:16:49

Because dedicated two hours were given for this thing.

2:17:03

So I can see only one response.

2:17:30

Last time you have installed from command prompt,

2:17:32

if you guys have already installed chroma db and

2:17:46

sentence transformers so why you are not like doing your experiments in that environment

2:17:54

why you were created new environment?

2:18:02

Okay, you're not from IT background, this program is not running in C.

2:18:32

Python is a programming language and PIP is a Python installer package that is used to install the libraries and packages.

2:19:02

All right.

2:19:09

Meanwhile, I'm releasing the poll and I'm looking for the issues as well.

2:19:16

I generally want to know what kind of issues you are facing so that we can like come up with a solution.

2:19:32

Usually when we start a project we need to create a folder.

2:19:51

It's good to avoid any kind of conflict.

2:19:55

I'm saying I installed Python again today.

2:20:02

Again getting three months.

2:20:07

Yeah, please stay back for a quiz. We have a short quiz.

2:20:25

So from different responses, I can like conclude that you guys are having multiple installations for Python.

2:20:45

And then you get path-related conflicts mostly. That is the main reason. And another one is the main reason. And another one is, you don't get, you don't get path-related conflicts mostly.

2:20:52

And another one is you don't get proper time to execute the command.

2:20:58

Okay.

2:20:59

I'll share these feedbacks to the team and then we can like have a proper solution to your queries.

2:21:22

Alright, so let's move forward with the short quiz.

2:21:29

To summarize what we have learned today, let me share my screen.

2:21:52

So you guys can either scan this QR code or just go to this website, given here,

2:22:09

www.minti.com, and enter this code. I'm posting this code in the chat as well.

2:22:22

Thank you.

2:22:52

All right.

2:23:22

So here's your first question.

2:23:29

What is a knowledge boundary and the options?

2:23:33

Internet connection is speed, topics the bot is allowed to use,

2:23:37

size of the database or number

2:23:52

The correct option is topics the bot is allowed to use.

2:24:22

Let's have a quick look on the scoreboard.

2:24:29

Get ready for the next question.

2:24:33

Which component finds relevant information and the options are?

2:24:39

Generator, retriever, customer or browser.

2:24:52

And the correct option is retriever.

2:25:07

Almost everyone has got this question right.

2:25:21

Let's move to the third question.

2:25:26

Which component writes the final answer and the options are?

2:25:30

Retriever, chroma, generator or metadata.

2:25:51

And the correct option is generator.

2:25:58

Let's move forward with the scoreboard.

2:26:19

Moving on to the fourth question.

2:26:20

What can be used as a retriever?

2:26:25

And the options are Python List, BG embeddings plus Chroma query, Excel or Metadata.

2:26:50

Everyone has got this question correct.

2:27:05

Yes, BG embeddings plus Chroma query can be used as a retriever.

2:27:20

Moving on to the fifth question, is vector search alone considered complete track?

2:27:36

And the options are yes, no, sometimes, or only for large datasets.

2:27:50

The correct option is no.

2:28:11

Vector search is not alone considered as a complete route.

2:28:15

We have seen that rack comprises of multiple steps.

2:28:19

So let's move on to the sixth question.

2:28:49

What should the generator use to answer questions?

2:28:54

And the options are random internet pages, only retrieve policy excerpts,

2:28:59

Wikipedia or social media posts.

2:29:19

And the correct option is only retrieve policy excerpts.

2:29:26

Let's have a quick look on the leaderboard now.

2:29:32

Moving on the second last question for the leaderboard now.

2:29:46

It is.

2:29:48

Y and LLM only baseline used.

2:29:52

And the options are to compare with Rag Answers to train the retriever to create embeddings to delete data.

2:30:16

And the correct option is to compare with rack answers.

2:30:30

Let's look at the leaderboard now.

2:30:46

moving to the final question for the day.

2:30:53

Which environment variable stores the GROC API key?

2:30:58

And the answers are open AI key, API secret, GROC API key or chroma key.

2:31:16

The correct option is Groke API key.

2:31:26

Let's see two bins today.

2:31:31

Congratulations, Mayut.

2:31:44

we have come to an end to two days session.

2:31:48

Sakshaam, do you want to comment anything or do you have any announcement to make?

2:32:14

Okay, so let's end today's session.

2:32:17

Good night, everyone. We'll meet tomorrow.

2:32:21

