0:00

Thank you.

0:30

Thank you.

1:00

Thank you.

1:30

Hi. Very good evening all of you. We will just be starting on. Good evening all of you. Just a few minutes we will start.

2:00

Thank you.

2:30

Thank you.

3:00

Yeah, yeah, sure, sure. I'm not speaking at this point in time. We'll just start in a minute.

3:30

No, I'm sure you are you sure very much on time. We are yet to start. We are yet to start? We are yet to start?

4:00

just starting in a minute. Yes. Welcome all of you. So today is our fourth session on rags

4:10

that we are doing just to establish the context in terms of, you know, what we will cover and what we are

4:18

going to be discussing for the day. So today will be our fourth session on rags where we will see the different aspects.

4:30

a little bit more detail and finally we'll talk about the final retrieval part of the workflow

4:36

in the session today. So just to establish the context, we're going to be, we're going to be exploring the

4:43

final part of our lecture. And in the final part of our lecture, we will, so so far we have seen

4:50

chunking, we have seen embedding, we have seen, so we have also explored the ideas around how

5:00

to create chunks, how to effectively create embeddings, how to create a vector DB.

5:07

So we have gone through all those pieces. And in today's session, we will get a little deeper and we will

5:14

talk about the final step in the puzzle, which is the retrieval part. If you remember, this is pretty much

5:19

what if what we have seen earlier, earlier we have seen the five-step rag workflow. So this is that

5:25

five-step rag workflow that five-step rag workflow that we have explored in detail.

5:28

So this is one of the things that we have seen and discussed in the class so far.

5:35

So the five-step rack workflow where first we ingest, ingest means the part where you load the data.

5:41

If you remember in our conversations, we have, you know, we have discussed with respect to the HR data set.

5:50

We have taken an HR PDF data set in our sessions.

5:53

So first thing, we are loading the HR data.

5:55

Second thing we are doing is we are effectively, so second thing after we load the HR data,

6:04

we are going ahead and, you know, we are converting the data into effectively chunks.

6:11

Because if we have a massive data set, which is spanning hundreds of pages, it is very difficult

6:17

to process the whole thing together. And also if you try to process the whole thing together,

6:21

give the entire thing as input, then there is no security. And also we talked about

6:25

the fact that there will be too many chunks that you will end up sending to the LLM, too many tokens.

6:30

That's why we never process the entire PDF in one go. What we do is we take the whole PDF or

6:36

whatever, whatever be the format of your text data. It can be a PDF, it can be a word document,

6:40

it can be a text file. So you take the entire, you take the entire document and you divide the document

6:48

into chunks. So that is what is happening in the data preparation stage. So first you ingest,

6:54

next you prepare and preparation part is where you do the chunking and you do the embedding that is the

6:59

preparation phase that we do we do chunk then we do embedding that's the preparation phase

7:05

because remember machines don't understand text you have to convert those chunks into

7:10

embeddings and then we save that in a vector db we save that in a vector dv so preparation part is where

7:19

you're also saving the whole thing in a vector dv remember we also talked about the metadata aspect that

7:24

where you you're going to save with some metadata last session we saw that and metadata is

7:28

basically for traceability and auditability for easier retrieval and then finally we'll define a retriever

7:36

there is step number three we'll define a retriever where you go back to the uh based on the query

7:41

you go back to the vector dv retrieve the relevant chunks and you generate the answer so this is the

7:49

part we will majorly focus on today retrieve augment and generate and generate so this is the part we will majorly

7:51

focus on today retrieve augment and generate so far we have built these parts in detail

7:56

and now we will focus primarily on this part we'll take the same tesla demo data set that we did

8:02

will be a very hands-on session i'll initially walk you through some theory after that we'll go back

8:06

to the hands-on and we will walk through how the retrieval can be done okay so that way we will be

8:12

working through it again primarily the core agenda would be to tune and run top k retrieval how do we

8:19

we define the top k how do we retrieve the top five similar chunks right in fact last

8:26

session only we saw that demo i have briefly shown you with lanchain how you can define a retriever

8:32

how you can define a rank chain retriever where you can go to the vector dv and retrieve the top five

8:38

similar chunks based on the similarity of the embeddings the query will have a corresponding

8:44

embedding you'll have a query embedding and you go to the vector dvd and try to retrieve all

8:49

those similar chunks which have similar embeddings so that is the top care retrieval that we

8:54

talked about right so we will do that we will build a context block so query context and

8:59

response and we will call grok and finally we will generate the answers so that's going to be the

9:04

final end to end production part that we'll see we have got a few more rag sessions towards

9:08

the end where we do some more advanced things but is that whole pipeline we will be seen and one

9:14

very important aspect that you know we saw this in the first session also is called

9:19

grounded generation why do we call it grounded generation guys is because you know the

9:23

generation that we are doing right now has to be grounded in the context that is a very

9:26

important part right so whatever uh answer the rag system is giving that answer has to be

9:34

grounded in the context so you ask a question from the vector dv you retrieve some chunks and you

9:39

get a response so whatever response you're getting from the vector db that response must be grounded

9:46

in the context and that is one very important aspect i want to

9:49

to you know clarify in the course of our conversation the response must be grounded in the

9:54

context so that is an important thing all right i think i think it will help if i take you back to

10:01

our slide which i believe we have seen it in a lot of detail already and i'm going to just take you

10:07

back to the same diagram again we saw this i think this is the third time we're seeing it and i've

10:12

i've actually written these things in the snippet so even last session i did that but i did not

10:17

share it with you today i've actually written these things down and this is the same analogy

10:22

which i've taken friends if you take a look at it i've taken the same analogy so before i start the

10:26

conversation like everyone can maybe take uh two to three minutes to just uh eye over it and i'm

10:33

sure everything will come back to you and today as i told you the focus will be on retrieval

10:38

creating the prompt and doing the grounded generation so we'll see these three sections

10:42

but all of you just give it a glance all of you and also relate back to the hr pdf example

10:47

that we took when we were explaining rags in the first session i talked about that 100 page hr pdf right

10:52

remember all of you so all this is nicely written here everyone take uh two minutes to go through

10:57

then i'll again explain to you okay and by the way this is all part of your 13 july folder

11:08

as always i'm creating folders for every day 13 july i've already uploaded the folder you can please

11:13

see this on the screen itself

11:17

you know.

11:47

You know,

12:17

You know

12:47

You know

13:17

I'm

13:47

Okay, I hope all of you are all of all of what we are going to

14:02

and I'm sure, as you're seeing this, a lot of what we saw in the lot of what we saw in the first three previous three rack sessions are all coming back.

14:11

I hope everyone is recollect some of those things just take another minute and I will once again

14:17

from there, we'll straight away come back to the practical.

14:47

You know,

15:17

You know

15:47

I'm

16:17

friends

16:47

here. So let's let's have a very quick recap of this thing

16:51

whatever we saw and whatever we have seen discussed so far.

16:54

So first let's say we have the HR PDF that you know all of you remember and imagine the PDF is having 100 pages, right?

17:01

And obviously you cannot process the entire document in one go. So what you do is something called chunking and you create one chunking.

17:07

And you do something called chunking and you create one chunk per page. So you do something called chunking and you end up creating one chunk per page. And after you do something called chunking and you end up creating one chunk per page. And after you do that you end up getting total 100

17:17

chunks, C1, C2, C3, C4, up to C hundred, you end up getting 100 chunks.

17:21

So every page is like a chunk and now you can take each and every individual chunk and you can pass it through an embedding model and you can generate the embeddings.

17:33

Right. So 100 pages, one chunk per page, you have total 100 chunks. Chunks are nothing but sections.

17:39

That is also text data. Machines will not understand text data.

17:43

So now you have to take those individual chunks, pass it through an embedding

17:47

model and end up getting the embeddings. So chunk one, you have certain embeddings, chunk two,

17:52

embeddings, chunk three, embeddings. So each and every chunk, we know what is the embeddings

17:57

with respect to each and every corresponding chunk. So C1, what are the embedding? C2, what are the embeddings,

18:01

C3, what are the embeddings? So we are able to understand what are the embeddings for each and every chunk.

18:07

And imagine this is how the numbers look like. So C1, embeddings are 0.1, the embeddings are

18:14

this thing, C3 is this thing, and so and so forth. You will also have some metadata as well

18:20

we are all about, right? So that's one other way to intuitively understand this. Okay, so these are the

18:25

chunks that we talked about. Okay. Yeah. So now, so that is the part where we take the data,

18:32

we do chunking, we create the chunks, we use an embedding model, and we store all this in the vector

18:38

DB. This entire thing will happen on premise. So just to just to clarify, just to clarify,

18:44

I think just to also answer your question shake, this entire process will happen on premise.

18:51

This complete process of taking the data, you know, creating the chunks, and then using the

18:59

embedding model, and then storing the whole thing in the vector dv, this complete thing will happen

19:04

on premise, which we have seen, right? Now, moving on. Next time when a user asks the question,

19:12

now this thing is completely safe, because as I told you,

19:14

you, this whole thing is, you know, happening completely on-premise in the company servers.

19:21

And next thing, what is happening is next time the user asks the question, imagine the user asks a question,

19:27

how do, how many leaves do we get in a year? It could be that, you know, you're trying to build an automated

19:32

HR assistant and, you know, you're asking a question, how many leaves do we get in a year? If you ask a

19:38

question, the corresponding query will also be converted into query embeddings. And let's,

19:44

say for this particular query, the query embeddings are 0.1.1. Let's say for this particular

19:50

question, the query embeddings are 0.1.1. And you have to understand, based on whatever question

19:58

that is getting asked, which of the chunks in the vector div best answer the question? That is what we are

20:04

trying to figure out. Right? So, based on whatever question is asked right now, which chunks in the vector

20:12

db are best used to answer the question. So, turns out the corresponding vector dv chunks

20:18

are c1 and c2. So based on whatever question is asked, the question that is getting asked is,

20:24

you know, this thing, this is the question that is getting asked. So based on whatever question is

20:28

asked, you go to the vector db and turns out the similar chunks. The similar chunks turn out to be

20:36

this thing, C1 and C2. The C1 and C2 are the chunks that we are getting in the process.

20:42

And that's the idea of how retrieval is happening.

20:47

Retrieval is the part where based on whatever question you ask, can we go back to that library where

20:52

all the content is present and can we find out those similar books where potentially the answer is

20:58

present? And that is what we call the context. And this is the K value that you will have to decide.

21:05

There is no such hard and fast rule that you have to retrieve the top two chunks or the top three chunks

21:10

or the top four chunks. But this is that exact K value that you will have to find out.

21:15

You will have to figure out what is the right value of K. Should I retrieve the top two chunks?

21:18

Should I retrieve the top three chunks? Should I retrieve the top three chunks? Should I retreat the top

21:20

four chunks? So you will have to iterate, try out different, different permutation combinations and

21:25

you will have to come up with the right value of K. What is the right value of K that or the right number

21:32

of chunks that I should retrieve? So that is something we will have to figure out. So we have

21:36

have retrieved the top two chunks you are able to see right now and that is what we call

21:41

the retreat context so those chunks that we retrieve that is what is referred to as the retreat

21:46

context the retreat context and that is how so we get the retreat context and that is how we will

21:53

call the LLN the large language model so that's the way how we will you know in a way call

21:59

the large language model to get the response okay so until here is fine we

22:06

ask the question retriever will retrieve the chunks which is nothing but the context this is the

22:10

context that you retrieve and now you will make the final lLM call right and this is what i was

22:16

mentioning all this while we you know until now before the rag session whatever we have seen is

22:22

we have a lm and we are just asking a question and getting a response this is how the structure

22:26

has been right normal generation you have an lm you ask a query is it a user input system message

22:33

and based on that you make the API call get an assistant response

22:36

right user message system message you make the API call and you get an assistant

22:42

response so that's the way normal generation happens okay so that's the way how I would say

22:48

normal generation happens this way and what we are seeing here is what is

22:54

referred to as retrieval augmented generation so what is retrieval augmented generation you ask

22:59

the question and based on the question you retrieve the relevant context so based on whatever

23:04

question is asked you retrieve the relevant context and based on that we get the answer

23:11

so so here the l llm API call is little different because you're giving more information and and why

23:17

is this important because see if you ask a general question about a company's proprietary data

23:23

the lLm is not having the pre-trained knowledge to answer that question that is one very

23:30

important concept we saw in the previous sessions the lLN doesn't know how to answer that

23:34

question it will not know that because if you just ask okay how many leaves do we get in a

23:39

year in this company the lLM is not inherently trained on that kind of data it will not know that

23:44

right it doesn't have the information for that to answer that question right lLM will not know that

23:49

so based on the question the language model cannot directly give the response because honestly

23:54

the language model doesn't even know but what if you can ask the question and based on the question

24:01

you can retrieve the context and now

24:04

you are giving both the query and the context as an input you are giving the query also as an input

24:09

you are giving the context also as an input and both are the inputs to the lLM and based on that you are getting the response

24:16

and that's the big picture idea of how the retrieval augmented generation is happening that's why we call

24:21

it retrieval augmented retrieval means the part where uh based on the question the content context is retreat

24:28

the chunks are retrieved retrieved retrieved retriever is retrieving the chunks that's that's a retrieval part right and then

24:33

augmented part is you're augmenting the prompt the prompt previously was just this system message user message

24:40

that's it story ends here user message was just the question now the prompt is system message will

24:46

anyways be there we have to customize a system message we will come to that but the user message consists

24:51

of the query and the context that's why we use the term augmented augmented augmented means we are augmenting

24:56

the prompt we had before was simple we just asked the question but now the prompt will consist

25:01

of the question and the context that's why i demonstrated this year that whatever retrieved

25:06

context is coming that retrieved context becomes the input to the llm along with the user query so the user

25:13

query and the context together make the user message obviously the rag will have its own system message

25:18

and based on that you will get a response so that's the way how retrieval augmented generation

25:23

happens right so we have seen several things in the previous sessions i don't want to repeat it entirely

25:29

but there are so many points where rags can go wrong i think uh one very important thing is that

25:36

obviously the responses have to be grounded in the context you ask a question whatever answer the

25:42

rag is giving it must be grounded in the context that is actually a very important uh

25:47

property of a rag system the answer cannot come from somewhere else very important

25:52

so so whatever question you're you know you're asking the answer to that question must be grounded in the context

25:58

must come from whatever context is given to do okay and in case you get an incorrect

26:04

response there can be so many reasons why the response is incorrect so in case you get an

26:09

incorrect response what you have to do so as part of the evaluation process you will have to go back

26:15

and you will have to figure out where it went wrong and there can be several points of failure

26:22

so many in fact last session we were getting a little deeper into chunking if you remember

26:26

but we talked about fixed size chunk there can be chunk size chunk overlaps how big a chunk

26:32

are you creating is it a very big chunk is it a small chunk and we talked about some of those cases

26:38

if a chunk is very big what is the problem if you have a very big chunk imagine the entire

26:43

pdf is part of one chunk then the whole point of rag is used this on the contrary if every

26:49

chunk is one character just a saturday session only we saw that right if every chunk is like a one character

26:55

then also it's bad because in each and every chunk is hardly having any meaning that way

27:03

so so chunk size chunking can be a problem if chunking is a problem everything downstream can go for a

27:08

cross number two the embedding model can be problematic there are so many different types of

27:16

embedding models out there remember in our sessions we used something called gtee large right

27:22

and all these embedding models friends this i have not mentioned before

27:25

all these embedding models are part of your part of a mt eb leader mode in case some of you

27:32

are curious that sir where can we see these embedding models all these embedding models are part of

27:37

this mt eb leaderboard you know what is the full form of mt eb

27:43

mt eb stands for massive text embedding leaderboard now it's not just for text data but it's

27:49

also for other forms of data as well it stands for massive text embedding leaderboard and interesting part

27:55

interesting part is it supports other languages also and you can go to the model section

27:59

and in the model section you can actually see the model that we used we use gtee large if you

28:04

remember we use gt e large and if you scroll down you will be able to find it gt e micro gttee large

28:09

zh and there is the model that we actually used this is the specific model which i used in my last

28:17

lanchain demo in fact we will see that again today and you can see what we actually did was we

28:23

took a text and what what is the what is an embedding model an embedding model is

28:27

different from an l l l lm will take an input and it will give a response text completion

28:32

whereas the embedding model is responsible for taking an input text and it will only

28:37

convert that into a sequence of numbers into embeddings that is what an

28:40

embedding model will do embedding model will just take that input text and it will simply

28:44

convert it into a numeric form or numeric embeddings that's what an

28:49

embedding model inherently does and in this particular

28:53

case we are taking the input and we are converting that into thousand to 24 dimensions

28:57

that means we are taking that entire text and we are converting that entire text into

29:01

1224 numbers that is what this specific embedding model is doing right now and so embedding models

29:07

can also be a problem what i know what i'm highlighting is that sometimes you might have to try out

29:13

different different embedding models and they will all work the same way the base idea is the same but

29:18

what is embedding fundamentally doing embedding is fundamentally

29:23

taking that text whatever be the text it is taking that text and it is converting that into a

29:27

numeric form and that numeric form to some extent conveys the context of that text so if the embedding is

29:34

done differently if the embedding model is somehow not able to uh you know represent the text

29:38

properly then you might have lost some of its meaning if the context the context should be well

29:43

represented those numbers those embeddings are representing the context of the text so if the

29:48

the embedding model itself is not a good one then it will not be able to

29:52

convert the text into the right set of numbers so i hope this is absolutely clear so embedding

29:58

model which is another point of failure the vector dv itself is another important thing that has to

30:03

be maintained metadata the search the search what kind of source source metadata you've used right

30:09

and finally coming to the query part remember the same embedding model you've used here have to be

30:14

used here also we talked about that in the previous session very important relevant to what we

30:18

are seeing today retrieval how many chunks are you retrieving this is also a very important point of

30:22

failure right and this could be any number of chunks you can retrieve one chunk

30:26

you can retrieve three chunks there are any number of chunks you can retrieve but the

30:30

number of chunks you retrieving is also a very very important factor and again the best

30:35

way to understand this thing is through extremities extreme analysis so think about

30:40

it this way what happens if you retrieve one chunk and second what happens if you

30:46

retrieve hundred chunks what happens if you have one chunk that

30:51

compared to what happens if you retrieve 100 chunks like that you can think in terms of

30:56

extremities they know the use case we are covering today in the class we are not focusing on multimodal

31:03

but what you say that can also happen that's a very good point so sneha asked a question

31:07

that sir what will happen with pictures so pictures are basically part of multi

31:12

model brand we'll actually have a session later when i will cover multimodal brand

31:16

but if you're asking me that sir like whatever demo we did and whatever Tesla

31:21

code i shared last session can it handle pictures no it cannot it is not meant for that it'll

31:27

will only accept text okay but can we work with pictures yes we can and just to give it a big

31:33

big picture idea image embeddings will happen the same way as text embeddings

31:40

images will be embedded the same way so the so the story remains very similar you you have the

31:46

entire period and from that the same way that you are getting text chunks you can also return

31:51

three image chunks let's see you have a particular page page number one in that page number

31:56

you've got four pictures so those four pictures are also extracted one two three

32:02

four and every image is encoded as a vector of numbers just like every page of text is

32:07

encoded as a vector of numbers similarly sneha every picture is encoded as a vector of numbers

32:12

and all these together gets stored in the vector view right i hope uh you're you're able to follow

32:17

right and you can take a look at it huh yeah so you can you can take a look at this

32:21

particular benchmark or you know what kind of tasks you have you can take a look at it and you can

32:26

actually compare we can actually compare with the modality uh to answer your question you can

32:30

actually search with image and you can actually see what kind of image embedding models we have

32:35

so it has image embedding models also by the way you can actually search for uh

32:39

specifically image embedding models so these are some models which will you know which will

32:43

exclusively do image embeddings you can you can search on the basis of that how they do you know

32:49

you can see cv just a distance of objects in the

32:51

image with similarity matching can i see this is exactly the kind of embedding models that will

32:56

be created here in a intuitively okay uh and there was one question by uh there was one question by

33:05

shake shake i missed your question that time let me answer that for you uh so i think uh

33:11

the technical term for that full on promise process is usually ingestion and indexing pipeline

33:16

or rack pipeline more specifically the part that chunks data reacts embeddings

33:21

and stores them in the vector degree is the indexing service and the part that finds relevant

33:26

results later is the retrieval or the retrieval layer i would say right got it so it's it's

33:33

it's not a uh like i mean uh yeah i mean the retrieval is not exactly like yeah so retrieval is

33:40

happening on premise because you ask a question and that retrieval will still happen on premise

33:46

because the API call we are doing only at the end right here if you see the API call we are only

33:50

doing here at the end everything that you're doing before that this is all happening inside

33:56

your company premises your data is safe and secure with the company so that's why i say

34:01

retrieval is also on premise shape i hope you are here right so you ask the question retrieve

34:08

the relevant chunks retrieve the top two chunks three chunks whatever and only then you make an

34:13

external API card right and guys just uh one other very important aspect i wanted to

34:20

clarify with respect to the number of chunks that you want to retrieve as i told you you must

34:26

always think in terms of extremities what happens if you retrieve the top uh one chunk versus what

34:34

happens if you retrieve the top hundred chunks so you have to think in terms of extremities

34:40

right so imagine the retriever is retrieving the top one chunk so if we retrieve the top one chunk

34:46

so if we retrieve the top one chunk what will happen then we have very limited information

34:58

in that case we will end up having very limited information right if see if i retrieve only

35:02

the top one chunk we will end up having very limited information i hope everybody is aligned we will

35:09

have a very limited amount of information here in that case because we are only getting one chunk

35:16

right so you ask the question maybe the answer to that question is spread over many

35:21

many pages i'm just giving an example here let's say leak policies can be discussed over multiple

35:26

pages right but if you at the retrieval part if you only retrieve top one chunk let's see you put a

35:31

criteria saying i want to get the most similar page in the answer that chunk may not contain

35:36

the entire answer so you are restricting the answer to the question you will not get the full answer to the

35:42

question because remember that is the context

35:46

that is eventually getting fed to the llm right so very low value of k is a problem you should

35:52

not take top one chunk and similarly you should not take top hundred chunks also because if we

35:57

say top hundred chunks or top thousand chunks then you're retrieving too much information and as i

36:03

told you the whole purpose of rags is repeated because if you're retrieving the top thousand

36:07

chunks you know imagine here uh you know i'm i have the pdf i've got hundred chunks my vector dps

36:14

hundred chants and retriever what do you do you're saying okay look at the question and retrieve the top

36:18

hundred chunks and what's the point of doing rag you know rag should like rag should limit the

36:24

answer you know rack should not be like you ask a question and i tell my librarian that go and get all

36:30

the books then i just search my answer from there and what's the point of using right so not i don't want

36:35

all the books i don't want only one book i want only the right number of books and this has to be tried

36:41

there's no one answer to that question this is a bit of a trial by error process you have to try

36:47

different different values of k and you have to see which particular k actually works

36:53

so that's the way how this part of the process will work out okay i hope everyone's

36:59

able to get a good sense and a very good understanding of how this is happening right as i

37:05

told you this is the final part of what we were discussing so you

37:11

ask the question you ask the specific question and you will have to decide the right value

37:15

of k so k equal to one is very bad it may be fast but it will it will it will it will effectively end

37:22

of missing many many of the aspects whereas if you take k equal to five it is more

37:30

context but risk of noise you are retrieving too much so the whole uh purpose of rags is

37:35

defeated so neither should k be very small nor should k be very large you should pick a value of

37:41

k somewhere in between and this has to be tried out there is no one answer to this question okay

37:45

it has to be tried out that is how you decide the top k chunks which top k chunks you want to retrieve

37:52

top k retriever it's often called top k retrieval the k value is an important one

37:58

and now on the basis of that you'll be building the final uh rag system you'll be building the

38:06

final rag prompt based on the metric so that's the way how the whole

38:11

pipeline will be working so let us go back to our uh case study that we did in the last session

38:19

that was on 11 july i'm just going to quickly open it up and we will run through that

38:30

and maybe if it's if it's easy for you i will try to uh load it in the same like folder itself

38:36

so 11 july was saturday we already had this session and we were able to run through uh the last part of

38:41

the code i'm going to take you to that snippet once again and just go over it in a bit of detail

38:47

okay let's see that's see that i'm going to open up the tesla demo file

39:11

okay, we'll just wait for the runtime to start.

39:41

upload the tesla annual reports dot zip file okay and remember i've also

40:04

connected to a t4 gp uq so when you're running the code at your end please connect to a t4 gp u

40:09

all this we saw and now this will take a while i'm going to install all the necessary

40:14

packages once again this will take a while let's just pause for a minute

40:39

you know

41:09

you know

41:39

Thank you.

42:09

Still loading, just going to another minute it will take.

42:39

Thank you.

43:09

Thank you.

43:39

Thank you.

44:09

Thank you.

44:39

All right. Now I think you can all take a look at it. The library is got installed. Everything is good. You know, set all set to go. Right. You can take a look at it. We need to restart the session. After this is completed, we will also.

45:09

need to kind of restart the session, which I will do right now. This is the way how I will restart the session. All of you can take out of it ahead. And now I will go ahead and import the necessary packages. First, we are setting the GROC API key. We've already seen that multiple times. So same way how we are importing GROC and setting the GROC API key. Next, we are importing the other necessary packages. And just to walk you through what these packages are French,

45:39

So we are looking at, you know, all our packages, all our utilities that are built inside Lanchine.

45:47

Okay. So all these utilities are built inside Lanchine.

45:49

So Lanchine is giving us all these functionalities.

45:52

And it's kind of, I would say, making life easy for us, right?

45:55

Lanchine is giving us all these functionalities and, as I said, it's kind of making life very, very easy for us, right?

46:00

So Lankchain is already giving us a utility for, you know, recursive tech splitting.

46:05

It is giving us a utility for loading the data from our data from our,

46:09

a PDF, PDF directly loaded. It is also giving us a utility for sentence transformers,

46:14

right? So you can take a sentence and try to generate embeddings. And finally, it is also giving us a

46:19

utility to create a chroma DB vector database, right? So this is the, you know, the four

46:24

utilities that we are using right from the Langein package. Okay, so right from the Lanktrain package,

46:31

we are, you know, we are able to see these utilities, okay, overall. So recursive character,

46:38

text glitter. So how we are taking the entire text and how it is, you know, the same thing

46:45

that we saw last time, last session, I think we've already seen this chunk overlap, chunk size,

46:50

just the fixed size chunking. We've got other kinds of chunking that we will see later, like semantic

46:54

chunker and all. So the line chain text glitter library will give us all those chunking algorithms.

47:00

The PDF directly loader, instead of that, there are other kinds of document loaders you can also

47:04

use, right? This is not the only kind of document loader. You can also use other kinds of document loader. You can also use other

47:08

kinds of document loaders. There is PDF loader, there is other kinds of document

47:13

folders you can also explode. There's so many actually, right? Sentence Transformers is for the

47:18

embedding model and this is for the chroma dv. Right. Let me run this code. The first part I think

47:23

we have already seen, I'm going to quickly go over it now. This we have seen several times,

47:27

even including the last session. I will load my PDF. I will do the chunking and we saw that my

47:33

data, my entire PDF file has overall 351 chunks. You should

47:38

this part takes a bit of time. Let us see. So the entire PDF consists of total 351 chunks,

47:48

which we'll see now. So there it is. 351 chunks are contained in the PDF. All of you can see right now.

47:56

Now moving on, we can see the chunks. Every document is like a chunk. We can see the page content.

48:02

That means what is the text of the chunk that is contained and what is the source and what is the page number?

48:08

So we have the chunk content and we also have the chunk metadata. That means for that particular

48:14

chunk what is the source? Where has the chunk come from? And also what is the page number where it is

48:20

present? So we can see the chunk source PDF and we can also see the chunk metadata. So both

48:27

the things we can kind of see. We can see the chunk source and we can also see the chunk

48:32

are the page number. And now we will go and do the vector DB creation. Vector database

48:39

we will do embedding model we will load right now. And based on that, we will be creating the vector database.

48:47

You can see this is the same GTE large model that I showed you a while back, right? And we are using

48:52

the Lanchine libraries that I already told you. So we don't have to go and manually define anything. Lanchine

48:57

is making it very easy for us. Even when we start with agent,

49:01

start with agents from the next session onwards. We'll be seeing a lot of these

49:06

lanchine libraries that will get used. Okay, it can make life very easy, especially from the coding

49:10

perspective. You don't have to write these things manually from scratch. All these things,

49:14

you can just import and just a few functions you are writing and all these operations will happen.

49:21

And this is the same way you should learn. You should not try to memorize these things. Even

49:24

from a learning perspective, we should try to understand these components. What is chunking doing? What is

49:29

embedding doing? And then you just remember, okay, you know, this is

49:31

this is how I can do chunking. That's it. So using the line chain, I can use this function.

49:35

I can do the chunking display. So that is how you should learn, not try to memorize these things. Okay.

49:41

Now, the vector DB creation is happening now. And after a while, you will see the Tesla

49:44

DB has been created. And now I will test my retriever. I will instantiate my retriever. You can see my

49:50

retriever we are instantiating right now. This is just for the basic level of testing. So we are saying

49:56

that I want to retrieve the top five similar chunks. This is just a

50:01

basic level of retriever testing that we are trying to do now. Okay, this is just a basic

50:07

level of retriever testing that we are trying to do right now. So based on the question, whatever

50:13

question is asked, we are trying to retrieve what are the top five similar chunks? So that's the

50:19

problem that we are trying to solve. So based on the question, what are the top five

50:22

similar chunks? That's what we are doing. So now, what is the annual revenue in the year

50:31

22. So if you ask this question, the retriever will retrieve the top five similar chunks

50:36

and these are the similar chunks you are able to see right now. So based on whatever question

50:41

is asked, you can see the retriever has retrieved the top five similar chunks. Okay,

50:47

based on whatever question is asked, the retriever has retrieved the top five, the retriever has

50:54

retrieved the top five similar chunks and these are the chunks we are able to see right now.

50:58

you've got retrieve chunk one retrieve chunk two retrieve chunk three retrieve chunk four and

51:02

retrieve chunk five so we've got the top five similar chunks as you're able to see on the

51:06

screen so based on whatever question is asked these are the top five similar chunks you're

51:11

able to see based on the semantics based on the embeddings it has retrieved this right from the

51:16

vector db got it so and i think very interesting i i actually showed this to you last session

51:22

also what is the annual revenue in 2020 if you go and take a look at it the answer to the question

51:28

be this right uh sorry not 94 uh the answer to the question would be this and the answer is

51:33

actually present in one of the chunks can you see it'll actually be present in the other chunks

51:37

also we have to manually go and start somewhere else also the 81 4662 will be there but yes indeed

51:42

uh the answer to that question is present in one of these chunks that means the context is

51:46

retrieved correctly and this is actually how a lot of evaluation happens like see how do we evaluate

51:51

a rag system like you can ask a question and the rag system will give a certain answer but how

51:58

do we know and how do we actually evaluate whether the rag system did what it was supposed to do

52:04

on what basis do we explicitly kind of evaluate by that so that is what the rag system is i would say

52:13

kind of supposed to do so very important very important how is the rag system expected to uh

52:21

look at a particular you know uh how is a rack system expected to look at a particular you know uh how is a rack system expected to

52:26

look at a particular question and based on that particular question how do you figure

52:31

out what are the right or chunks okay how do you figure out whether the right chunks are retrieved

52:37

correctly or not and that is what we are able to see so we can clearly see that yes based on whatever

52:42

question you are asking i am able to retrieve the correct chunk because the answer is contained in

52:49

this show so so this is an important thing you know i was remember i was talking about grounded generation

52:55

the generation must be grounded grounded generation very important so whatever answer

53:01

the rag is finally giving me that answer must be from the context you can see right now

53:08

grounded generation produces natural language output constrained by the supply context rather than model

53:15

memory alone what it means is if you ask a general question let's say if you ask the question how

53:19

many leaves the you know do you get in a year so if you're making a

53:25

LLM call only with that question the language model might try to answer that from its

53:32

own pre-trained knowledge the language model may not go back to the PDF and try to retrieve the chunks

53:38

from there so grounded generation is a very important aspect of a rag system because that is what

53:45

you want you want to ask the question and you want the answer to be retrieved based on that

53:50

so you will ask a question and the answer to the question you want to the question you want to

53:55

retrieve the answer from that so that is exactly how grounded generation will happen in the

54:00

real world right so that's that's that's one other important thing to keep in mind okay

54:07

anyways i hope everybody is aligned everybody's able to understand the concept of it that is

54:12

most important the concept is most important so we have tested our retriever and this part is also a

54:17

little redundant the reason i've again imported is because i want to show it as two sections

54:21

i told you last class also i actually framed this notebook in

54:25

two ways like first i wanted to cover this part this box okay document chunking embedding

54:31

vector dv i think this is sorted next i wanted to complete this box and this is what we are seeing

54:36

in the this part that's why i've done the import statement again fresh we are using the lama

54:42

3.370 billion versatile model sentence transformer and this is the same story that we have discussed

54:49

so far i'm again instantiating the retriever because in a real world what will happen you will only work on the

54:55

component the vector dv will usually be created so here i manually created the

55:00

vector dv because we are learning the concept but in a more real world scenario the vector dv will

55:06

already be created for you okay the vector db will already be created for you and you will

55:11

just be doing the retrieval pipeline you will ask the question the query embeddings will be created

55:18

you will go to the vector db retrieve the similar chunks and then get the answer and that is exactly

55:23

what we are seeing so we are again instantiating the retriever okay retrieve the top five

55:28

similar chunks and now here goes the rag system message this is the system message for my lab

55:36

now we are coming to the llm layer so we have managed to ask the question we have managed to retrieve

55:42

the relevant chunks and now we are in this layer we'll define this llm layer right now so everybody

55:47

give it a glance once just give it a read once we have all seen system messages so many times but first

55:53

time we are seeing the system message for a rag so everybody please give it a glance

56:00

it is pretty self-explanatory what it means but you can also read it at your end once

56:05

so that you understand exactly what it's doing

56:23

you know.

56:53

You know,

57:23

Thank you

57:53

Thank you

58:23

Okay, guys, I hope all if you are able to relate to it

58:37

relate to it.

58:39

And you can clearly see, you can clearly see, you can clearly see we have explained how the language model is supposed to work.

58:47

I think that's the whole idea of the language model is supposed to work.

58:50

clearly stated how the, you know, how the language model is effectively supposed to work.

59:20

So you're an assistant to our financial services firm who answers

59:30

user questions and annual reports.

59:31

You're giving a context here right now.

59:34

And you're seeing user input will have the context required by you to answer the user questions.

59:40

Because I told you whenever you are defining a system message, you have to be very clear that what inputs

59:44

need to be fed in the system message.

59:46

So you are explicitly stating that the user input will content.

59:50

in the context and the question. Both the question and the context should be part

59:55

of your user input. And we saw that, right? We already discussed that the LLM, the user input to

1:0:00

the LLM will contain the query and the context. The system message is just giving the overall idea

1:0:06

of how the language model should work. And that's why it is very important to state that in the system

1:0:12

message that while giving the user input, we will give the context with a delimiter hash, hash,

1:0:20

and we will also give the question with a delimiter hash hash question. So we are explicitly

1:0:28

stating that. Please answer the user questions only using the context provided in the input.

1:0:35

Very important. Do not mention anything about the context in your final answer. Your response

1:0:43

should only contain the answer to the question. So everyone can see the last two lines were

1:0:50

the last three lines were very important because this is where you are kind of absolutely

1:0:54

sealing the behavior of a rag system. So the grounded generation part is very nicely covered

1:1:00

here. So we are explicitly stating that answer the questions only using the context. So

1:1:06

so if you're asked the question, please don't, I mean, please don't kind of answer the question,

1:1:12

you know, generally based on anything. So please ask the question only on the basis of the context.

1:1:20

text. Don't use your own intelligence. That is the important part. Second, we are also saying if the answer is not found in the context, respond, I don't know. This is also a very important part. If the answer is not found in the context, please say, I don't know. So imagine you ask a question, you know, imagine you ask a question, you know, imagine you ask a question.

1:1:50

In the Tesla data set, whatever we have, you're asking a question, how many leaves I get in a year?

1:1:56

Now, that is not relevant, right?

1:1:59

If you ask a question in the Tesla data set about annual profit or revenues or whatever, it can be answered.

1:2:07

But if you ask a question, what is the leaves I get in a year, obviously that question cannot be answered.

1:2:14

Because based on whatever question you ask, the vector DB doesn't contain the answer.

1:2:17

it will not even be able to retrieve the relevant chunks, right?

1:2:21

So these are some very important things to be kept in mind.

1:2:26

Right? So this is a very, very important thing that you need to keep in mind and understand.

1:2:31

I hope everybody is aligned. So that's your system message. User message template will be like this.

1:2:38

You can see very clearly we're giving a delimiter. That is the concept of a delimiter.

1:2:42

Delimiter basically means it's like a separated kind of thing.

1:2:46

So we're giving a delimiter.

1:2:47

hash hash context and the context will follow. And we are also giving a demiliter

1:2:52

hash-h-h-h-h-h-h-h-h-h-h-h-question and the question will follow. This is the placeholder.

1:2:58

And now finally when I ask the question, what is the annual revenue in the year 2022?

1:3:04

This is the code we are using to retrieve the relevant chunks. And you can see five chunks are

1:3:08

retrieved. And now here is the final one. This is just a random one I did. Now if you ask the

1:3:13

question, what is the annual revenue in the year 2022? Let's see. Let's see.

1:3:17

we run this the retriever will retrieve the relevant chunks we already define the retriever a while

1:3:24

back we will say get relevant documents user input so whatever user input is given

1:3:31

it will get the relevant documents based on that and you might be wondering that sign

1:3:36

where are we doing the query embedding remember the query embedding is automatically happening

1:3:41

so the moment i write this code retriever dot get relevant documents this entire magic is happening

1:3:46

in one line of code. It is taking the query, converting that into numbers, doing the retrieval,

1:3:51

and giving in the chunks. The whole magic is happening with one line in one line. So based on the

1:3:56

input, I'm getting the relevant chunks. Now the relevant chunks will completely be in a text form,

1:4:02

right? So what we are doing, this is like a, you know, a Python program, list comprehension is what we

1:4:08

call it because it will basically be a list of documents we'll be having. So we are going

1:4:13

through all those list of documents and we are joining that into one massive text query.

1:4:16

So this is that entire context for the query we get. So whatever five chunks we repeat, we are taking

1:4:22

all those five chunks and we are building that complete context. And now finally, this is the last

1:4:28

part of the magic that we are doing. So role system system message. Remember Q&A system message

1:4:34

is the variable we already defined here. And role user, role user, user message.

1:4:43

dot format and we are giving the input and the context. So this is getting populated.

1:4:47

This entire thing is getting populated. It's a prompt template, right? So runtime, when you're

1:4:51

calling this, this will get populated. So we are populating the context with the context for the query.

1:4:56

This is actually the context and this is the user input, the question. And that's your complete

1:5:01

prompt for the LLM. So that prompt is nothing but what you will now use to make the API call

1:5:07

to the LNN. This is that whole prompt that we have curated. We can also print the prompt and show that to you.

1:5:13

And then inside a tri-except block. Try-Exap block is often very commonly used in these cases because

1:5:18

you don't want to run into exceptions, right? Even if exceptions happen, you don't want the

1:5:22

application to error out. Right. So very important, even if exceptions happens, you don't want the

1:5:28

application to error out. So we use try-ex-ex-ed block. And very common, I would say, you know,

1:5:35

so very common use cases of exceptions are what? Very common use cases of exceptions are

1:5:42

So very common exception use cases are, I would say, API errors. Many of you are using

1:5:52

LLMs. Many of you are doing client chat completions create. You're making an API call. Oftentimes, some of you might

1:5:57

have encountered, you know, oftentimes some of you might have encountered, you know, something like,

1:6:03

you know, think of it like, your model name is wrong, your API key is wrong. And these kinds of cases,

1:6:11

you know the try except block actually helps a lot anyways straightforward uh

1:6:15

thing temperature is zero very important for rack systems always try to keep temperature

1:6:20

zero because you want deterministic answers every time you ask the question the same question

1:6:25

should always yield the same answers so temperature should always be equal to zero

1:6:29

and this is the final response that you're getting and from that we're getting the prediction

1:6:33

so let me run the poll and you will see the answer will come out 81 462 million right this is that from

1:6:41

i think the prompt is not that visible so i can just print it because the print statement

1:6:44

what it does is it just goes and kind of the notebook implicit printing is a lot better when i just

1:6:49

use prompt like this i get implicit printing but if you use print in python it it prints this way

1:6:54

hard to read so if i'm using the notebook implicit printing you can see it in a nice see or you

1:6:59

can also use pretty print there is something called pretty print you can google out there's something

1:7:04

called pretty print in python there's a preprint package which will also go and print in a better way okay so this is

1:7:10

the nice way we are able to see the complete prompt what is that complete prompt

1:7:14

that we are using to make the API calls you can see role system message system system message

1:7:19

and role user we have the context and the question so both the context is given

1:7:27

and the question is given separated by a delimiter and this is how the LLM knows that okay

1:7:31

this is the question and this is the context it is almost like one of those reading

1:7:35

comprehension things that we used to do in our school days right like you're asked a question

1:7:40

first you have to read a paragraph and then you have to answer the question from those

1:7:43

paragraph so that's what we are able to kind of see on the screen okay i hope everybody's

1:7:49

able to understand this over all intuitively

1:8:10

so you are also able to check this in our thing and our thing and you know our thing and you can see

1:8:40

801,462 if i go and you know actually navigate over to my tesla pdf file i think we already

1:8:48

checked that we are indeed getting 481 4602 we were able to get the exact same answer here as well

1:8:56

all if you're able to see and that's the final piece of the retrieval uh pipeline that we wanted to show you

1:9:03

today right so we already know the vector dv so today the main thing was how you retrieve how you

1:9:08

you augment and how you generate and you can indeed see that this is coming very nicely in

1:9:12

fact i can ask a different question let me ask another question i'm going to copy these two cells

1:9:17

and let me let me let me ask another question you can also copy cells in jupiter right uh i can

1:9:28

ask what is the total annual revenue across this is a slightly harder question you can see

1:9:38

across both the years across both the years 2022 and 2023 and you can try out some other

1:9:45

kinds of queries also and this is actually a harder question because you're asking uh like it has to do

1:9:51

two things it has to first look at 2020 to find out what is its revenue then it has to look at

1:9:56

2023 find out what is its revenue and then based on that it has to go and you know kind of uh

1:10:02

it has to kind of go and do a summation right so i will ask this question we'll retrieve the chunks

1:10:08

and you will see that the correct answer is given this is actually very interesting i think

1:10:14

it could have been formatted in a better way again all this magic will happen in the system message

1:10:19

if you're not happy with the formatting because this is exactly how an end user will see the answer

1:10:23

maybe if you run it again it might give a better result uh this is the better one couple of iterations

1:10:29

will help definitely so you can definitely kind of format it and you can see the total annual

1:10:35

revenue across both the years is this this is well formatted and you and you and you can validate it the

1:10:41

answer is exactly this it has to look at 2022 find out what is its revenue and you can calculate

1:10:47

let me open up a calculator and check it is indeed 81.462 million means 81.46 billion

1:10:56

right thousand million makes it a billion so this much billion plus 96.77 billion so it had to look at the

1:11:04

document retrieve those relevant numbers and then it was doing a submission 178.23 and you will see

1:11:11

178.23 it has given me the exact answer this is what i meant by grounded generation it has not got this answer

1:11:19

from somewhere else it has got this answer from that video right i hope everybody's aligned you can

1:11:24

maybe try out a couple of samples queries also and guys yeah so we can take a break now let us take a break and

1:11:30

let us uh you know come back after the break and continue on the corner

1:11:34

so let's take a short break at this point in time we have pretty much completed the

1:11:40

Tesla flow and all this once again isn't the 13th July folder okay so let us take a break

1:11:45

and we'll continue on after the break

1:12:04

you know.

1:12:34

You know,

1:13:04

You know

1:13:34

I'm

1:14:04

I'm

1:14:34

I'm

1:15:04

I'm

1:15:34

I'm

1:16:04

I'm

1:16:34

I'm

1:16:36

I'm

1:17:04

Thank you.

1:17:34

Thank you.

1:18:04

Thank you.

1:18:34

Thank you.

1:19:04

Thank you.

1:19:34

Thank you.

1:20:04

Thank you.

1:20:34

Thank you.

1:21:04

Thank you.

1:21:34

Thank you

1:22:04

Thank you

1:22:34

Thank you

1:22:36

Thank you

1:22:38

Thank you

1:22:40

Thank you

1:22:42

Thank you

1:22:44

Thank you

1:22:46

Thank you

1:22:48

Thank you

1:22:50

Thank you

1:22:52

Thank you.

1:23:22

all right guys welcome back all of you we will continue on and what i intend to do is to take you through

1:23:35

one more small case study very similar to what we have done because the tesla one we already solved

1:23:40

and uh and so far you know i've been talking about hr hr so i thought why not take a uh a very similar

1:23:48

hr data set and show you in an example of rag which

1:23:52

respect to that data right so we'll see another very small mini case study and i think i think

1:23:58

based on whatever approaches we covered based on whatever concepts that we discussed i really

1:24:02

encourage everybody to go and you know use this in different uh

1:24:09

applications i would say right so you know you it's up to you now now it's up to you to implement i

1:24:14

would say so you know you can take any PDF file you can take any text data let's you're working

1:24:20

with a particular document data you're working with a particular document data you're working

1:24:22

with a particular text data this could be a great use case where you can take any kind of a

1:24:27

text data and you can build a rag based system on that and uh maybe you can talk about support

1:24:34

manuals i was discussing this use case also these could be some very nice uh

1:24:37

projects you can take up let's say tomorrow when you uh you know you have a

1:24:42

masonic ac right and normally what what we do whenever the ac uh like make some

1:24:49

problem or the washing machine has some issue what we do we call up we pick up the phone and we call

1:24:54

call customer support right so this is the product manuals pdf section that we have for

1:25:00

ac refrigerator washing machine and if you click on this we have the list of all the products

1:25:05

they're all pdfs by the way if i click on it is a user manual we all have user manuals right

1:25:09

so and and and and you can see this is the 40 page user manual for this particular brand

1:25:14

and it could be such a very nice use case for a rag system the next time you have some

1:25:19

query that okay what to do how to do you know like oftentimes we have questions know what each

1:25:23

thing does and what are these buttons what is cotton cotton equal easy care

1:25:28

yeah because we ask these questions but like maybe in the future you can and they don't have this

1:25:34

today but maybe in the future it's not for Panasonic to do web scraping go to each and every one of

1:25:41

these URLs and they're all URLs right if you hover over it they're all URLs HTTP in fact if you're

1:25:46

you're in chrome you can go to inspect and you can go to the and you can actually

1:25:53

extract these links you can easily see what these uh urls are can you see you can all see this one you can see

1:25:59

what the corresponding you know age references are here you can clearly see that content dam

1:26:06

panasonic can you see it's it's public you are so you know you can if you with a bit a little

1:26:11

bit of HTML knowledge you need to know a bit of HTML for that you can actually do something

1:26:15

called web scraping and from this website you can effectively scrape all the hundreds of

1:26:20

PDFs so we've got PDFs across across AC across refrigerator across the washing machine and

1:26:27

there are so many different brands and and easily the count will go into hundreds so maybe you can

1:26:33

build a take all the PDFs you can store all that in a vector DB and then you can simulate a kind

1:26:40

of a support assistant where if end users can ask a question it will go and hit the vector DB retrieve

1:26:45

the relevant answers and the rag system will give an answer based on that so whatever we have

1:26:51

seen in a very basic way with respect to Tesla DB you can effectively go and kind of extend

1:26:58

it to so many other use cases okay so let me quickly upload the other case study for you

1:27:10

this is the the HR one the final one that we will talk about for today let us

1:27:15

see oh you can absolutely heartbeat you can absolutely you can absolutely you can do that

1:27:35

see the in the in the language in the library we were using is five pdf directly loaded

1:27:39

look at the command we were using directly loaded now what it means is inside that directly directly

1:27:44

if there are multiple PDFs in the directory it will work right we are using something

1:27:51

called pi PDF directory loader so what it means is if there are multiple PDFs in the same folder

1:27:57

or in the same directory it will work that's one way to look at it okay yeah you can do that

1:28:05

directly loader will work in the same way okay now let me quickly share the other uh

1:28:14

file with all of you.

1:28:44

you it's not not a very big data set but just to give an idea we've been talking about that HR

1:28:49

example for a long time so i just thought let let's see the same rag workflow is exactly the same

1:28:53

nothing is different is exactly the same kind of pattern and workflow we are able to see on the screen

1:28:59

so the same uh kind of a rag workflow we you know we are seeing with respect to the HR data set

1:29:05

set is a smaller file it is only eight pages long and but you'll be able to see like that specific

1:29:11

thing i was talking about uh the grounded generation part all that we are

1:29:14

will be nicely you know nicely ensured nicely covered here actually that is very important because

1:29:20

if you ask a general HR question the language model might you know might use its own memory and try to

1:29:26

answer but okay i think there are this many leaves i think this is the salary and all that

1:29:30

no you know there's no room for i think you have to uh look at the context and you have to give me the

1:29:36

answer from the context that's why we call it grounded generation so that groundedness check is very

1:29:40

very important later on in the upcoming sessions i will actually talk about judges

1:29:44

how to evaluate but but you know but ensuring that your response is grounded is very very

1:29:49

important okay so let's go and uh run this now very important uh we need to ensure that we

1:29:57

delete the runtime the previous runtime because in collab you get a limit of using only

1:30:03

one gp u runtime at a time you can only start one gp u runtime right so we are doing that here

1:30:10

and i will also go ahead and uh

1:30:14

start this let me upload the PDF we will do this one

1:30:24

that's my oh i'm sorry i think i mistakenly uploaded tesla i will upload the uh you know

1:30:31

the this one this is a straightforward PDF file and once again same process i will

1:30:38

install the necessary packages it's a new runtime so again the same way it will take a while to install

1:30:44

And the same process you can actually see here.

1:31:14

Thank you.

1:31:44

Thank you

1:32:14

Thank you

1:32:44

Thank you

1:33:14

Okay, so it's still installing.

1:33:20

Yeah, this is wait for a minute minute.

1:33:23

And one more minute and one more thing.

1:33:27

And one more thing while this happens, I just wanted to maybe talk about it.

1:33:32

Another very important thing you need to take care of and maybe it's not so relevant in this session

1:33:36

because we have another two or three advanced classes on racks coming up in the next module.

1:33:41

We have some advanced sessions where we discuss this in more detail.

1:33:44

the latency. That is also very important because so far we have just talked about, you ask a question, we retrieve chunks, we get an answer.

1:33:51

Latency means that how quickly you are able to get your answer. I'm sure all of you have encountered this where you are chatting on a chat board or you're entering a URL on a website and on a browser, sorry. And, you know, you're waiting forever for, you know, for the website to open.

1:34:09

Other be request response.

1:34:10

You are you, what are the website in? You're going to link down here.

1:34:14

TPS something or it is making a call to the respective server and you're getting a response back.

1:34:21

Internet way is it chan't a website.

1:34:22

How's going to say.com. It's sending a request and you're getting a response back from Facebook.

1:34:27

But the point is latency is a very important factor.

1:34:32

Like Facebook.com is an application. Just say google.com is also an application.

1:34:37

Similarly, your rag is also an application. It is an application you are building for end users.

1:34:41

If you're making, your HR policy of Tesla to banasonic rag, whatever you're building, somebody will use it, right?

1:34:50

You have to think from that perspective, French.

1:34:53

So, their latency will also be a factor. And there are several factors that will contribute to the latency.

1:34:59

Go back to all those conversations we had, chunking over, embedding over it, how many chunks you're retrieving.

1:35:06

If you're retrieving too many chunks, then retrieval will take a lot of time, right?

1:35:10

If you're latency bargey.

1:35:12

It's always a trade-off.

1:35:14

So just like anything else in life, here also, it's trade-offs.

1:35:18

You cannot get the best of both worlds.

1:35:20

Now, it's not that you know, you can build an accurate solution and that will also be very, very fast.

1:35:25

Accuracy comes at a cost.

1:35:27

If you want to be 100% accurate and you want to be very correct, your applications will be slow.

1:35:34

So retrieval is a very important factor.

1:35:36

Like, if you're retrieving too many chunks, like if you go back to,

1:35:40

that initial conversation we were having here.

1:35:43

We were discussing about the value of K, right?

1:35:47

And that time I told you that K equal to one means you're retrieving only one.

1:35:51

But see, there is a trade off.

1:35:53

One aspect is that it is fast.

1:35:55

And this is the latency part.

1:35:57

This latency one of part.

1:35:59

So if you're only trying to take the one chunk,

1:36:03

the retrieval is super fast.

1:36:05

That's from here.

1:36:07

But it's accurate not.

1:36:08

Your question's answer not going to answer in one chance.

1:36:12

But if you go to K equal to, on the contrary, if you take K equal to 100, if you're trying to retrieve

1:36:18

100 chunks, 100 chunks you're trying to retrieve, there be problem.

1:36:22

Because 100 chunks might give you the answer to the question, but it will be very, very slow.

1:36:27

So you have to keep that particular trade-off in mind.

1:36:30

So whenever you are building rag systems or any application, any generative via application.

1:36:36

So you have to be cognizant and you have to remember.

1:36:38

Remember your end users, that he's going to use fun.

1:36:41

Now, like we're Panasonic's talking, imagine you're a customer, you've seen machine

1:36:45

machine carried, you, you've got some trouble are.

1:36:48

You have company had you a chat warded, an app gave.

1:36:51

Where you, you know, you're asking, you're asking for 10 seconds to answer to wait.

1:36:54

You're, I mean, see, this is normal human psychology, right?

1:36:58

I'm sure most of you, if you're opening up your mobile and you're opening some application,

1:37:03

you've got to type and it takes forever to answer.

1:37:06

So, do you?

1:37:06

Do you?

1:37:08

Even the current chat bots, like chat gpti got here, this jemini got a quick response, right?

1:37:17

So latency is a very important factor also.

1:37:20

So just keep that at the back of your mind, okay, guys?

1:37:23

Okay, okay?

1:37:24

Let's move on.

1:37:25

I think my libraries are installed, good to go, and I will restart the session.

1:37:31

And we will also pip install grog here.

1:37:36

I will load the file.

1:37:39

The file is already present here.

1:37:44

I will load the file and we will see the number of chunks present.

1:37:48

This is a very small file, unlike the Tesla one, which was huge.

1:37:51

Here, you know, we only have 58 chunks.

1:37:53

It's a very small data set.

1:37:55

So we are taking the PDF.

1:37:57

We are creating chunks.

1:37:59

And this is again to build that confidence.

1:38:01

You're going to see?

1:38:02

You're here at Tesla, we use here.

1:38:03

Why am I sharing this exercise with you?

1:38:05

is because I want to build the confidence that using one template you can solve for any kind of file.

1:38:11

You're here the template use caro.

1:38:13

Like we're in Tesla in the Nesla, we are seeing on another PDF.

1:38:19

Same way you take the same template and try to use on your own use case.

1:38:23

Now same way in our use case in.

1:38:25

So this is just to build that confidence.

1:38:26

I've used the same context and the same template.

1:38:30

So now we are creating the vector DV same process.

1:38:33

We are instantiating the retriever.

1:38:35

We are defining.

1:38:35

K equal to 5. I'm sticking to k equal to 5 for today. We will discuss evaluation in the

1:38:40

advanced session. And if you ask the question, let's say, what is the salary policy?

1:38:45

Updiko, the right chunks will be retrieved. It will retrieve the top five chunks based on whatever

1:38:50

question you're asking. If you're asking, what is the salary policy, so based on whatever

1:38:55

question you're asking, the model will retrieve the top five similar chunks. So the top five

1:39:00

similar chunks will be retrieved. So that's what will happen here.

1:39:03

So let's see. Usually the vector DB creation takes on time. That's where we are stuck right now.

1:39:10

You can scroll up and you can check. It's loading the embedding model. It is creating the vector dv. And there it is.

1:39:15

It has actually retrieved those five chunks. It's a very small document.

1:39:18

You can see that your chunks are also very small. I think in fact my chunk size is also very small.

1:39:23

There in Tesla, every chunk was 512 characters. 512.16. We have.

1:39:28

Now, look, here here on chunk size 64, because the document itself is very small.

1:39:32

So I've reduced my chunk size to create more chunks, more sections of the document.

1:39:37

So this is also an important factor.

1:39:39

You're, you think, sir, this chunks is this small.

1:39:42

We have created smaller chunks here.

1:39:45

And you can see, based on the question, we are able to see that indeed the answer is present in some of the chance.

1:39:50

Salary policy to have here. Here here here here be attracting new hires, you,

1:39:54

or some kind of policy related are.

1:39:56

Sufficient time should be spent with each employee.

1:39:58

So salary policy is related to remuneration benefits yourself.

1:40:01

So you can take a lot.

1:40:02

look at it. So now, same way. Now we will discuss the retrieval pipeline, same context,

1:40:09

the same template we are using. And in fact, even the rag Q&A message is similar, only

1:40:13

I've changed this part. There I was saying, you're a assistant to the Tesla. Here I'm saying

1:40:19

you're an assistant to the Nestle. So the template is very similar. And then you can add on top

1:40:22

of it. You can add and subtract on top of it. Okay. But again, it is to build the confidence

1:40:28

that you have kutkut. Same way, you're on our jasa caro. Yeah, but you can attach

1:40:32

for a PDF, your rag on that particular PDF data. Maybe you can take some personal documents

1:40:37

also. You might have some income tax periods. You might have some other kinds of PDFs. Bank statement

1:40:41

to go. That would be a bank statement. You take your transaction summary for the last one year.

1:40:49

Exile's a transaction summary. Bank statement. It's a big summary. And you'll be surprised the kind of

1:40:55

questions you can get answered. You take your bank statement for the last five, six years, or 10 years,

1:40:59

depending on how, you know, your banking really.

1:41:02

relationship with a bank. Bank statements and you can ask questions. And these are all some

1:41:07

amazing use cases of rags that can be implemented. Abhita, this has some one in India in. Because

1:41:12

they are also very sensitive, because transaction data in banks are all very sensitive. But you can

1:41:17

see the prospects. But the kitna scope. But I think part of the thing is the business, the leadership

1:41:22

approval also. So one is that banks mindset is very different. Indian customers are different. So

1:41:29

so, okay, banks are not too much. Banks are not too much.

1:41:32

about cutting-edge innovation. But I'm just saying that these are things that can be done.

1:41:37

Now, now that rag system, then how can use it? Who will use it? You and I, we know rag. But you talk

1:41:43

about the millions of other customers. So rag-ca-ca-ca-ca-ca-out-pott-a-pott-it-mall-you-mall-you-mall-

1:41:47

-n't-you-know-and. I'll give you another classic example of what I'm talking about. And, you know,

1:41:53

if you see Amazon, now Amazon to all use. Okay. Amazon, too, Amazon to save. Okay, Amazon,

1:42:00

so, well, banks, leave it. But Amazon is, everybody's using, right? And you'll be

1:42:04

surprised to see, like, I made a phone search here, Samsung S-26, right? Now,

1:42:08

look, I've looked, I've seen it, and if I scroll down, I don't know how many if you have seen this,

1:42:14

very little bit down, right? From page, right? You know, right? You're up here. This is a very good

1:42:21

use case of retrieval augmented generation Amazon is doing. Now, now, they'll say, sir,

1:42:25

he's, here here for who will use it? You tell me. Not, not many customers even,

1:42:30

care about all this? That product, will look, search

1:42:32

the keyword search, is it matching? Is it matching? Price in, budget

1:42:36

in, buy it, who will worry about asking Rufus AI questions and all this?

1:42:42

So I think sometimes, you know, you have to also look at the real world application of these things.

1:42:47

Kavikavik will be a great solution. You and I, we know it, but then from a business mindset,

1:42:52

if you look at Amazon, you know, the crores of customers, it is catering to, like, who

1:43:00

will use this. But it is actually doing a rag.

1:43:02

If you look, let's say, if I ask, what, can you tell me, you know, can you tell me something

1:43:09

about the battery of the phone? Is it good? What is happening?

1:43:18

Now, I'll say, sir, this vector DB how's being? Oh, in memory bunted. Vector DB is basically nothing

1:43:22

but you, the product description, it is effectively taking the entire description. The entire description, the

1:43:28

entire description, the technical specification, all these things are actually taken.

1:43:35

All these things are actually taken and based on that the answer is given. So your,

1:43:39

your, your, your, your, your, uh, text, the chunks are created based on all this display, connectivity,

1:43:46

all the details here. This case, based on your battery related information here. And now,

1:43:50

look, look, where we're, we're going to, basically a 4,300 millie amp will be.

1:43:55

100% it will come because it is doing retrieval augmented generation.

1:43:58

right? You can see this exact answer is coming. But it is a rag, right? It is based on a

1:44:02

question I asked, it is retrieving the relevant chunks from that particular description part,

1:44:07

and it is giving me the relevant answer. But then as I told you, like, how many people will even

1:44:11

use it or, even if you ask me personally, you know, I am so much deep in the field.

1:44:17

Now, now, now, now, maybe not. Maybe not. Maybe, maybe, unless they do something more,

1:44:24

just descriptive search, maybe doesn't search the use this. This is a, so on battery,

1:44:28

section, that's what I mean, five seconds, we'll put the perfect. If type

1:44:33

or you, ask, so you will be able to, you know, you'll read it yourself, right?

1:44:37

So maybe, maybe this can be built in a better way than just give out simple chat interface.

1:44:42

Okay. Okay. So, um, all right. So we did this part and now when I ask this question,

1:44:49

we are retrieving the relevant chunks and this is that final solutioning we are getting.

1:44:53

All if you can see. The same story that we discussed before. So you ask the question, we retrieve the

1:44:57

relevant chunks, you curate the prompt, and based on that, you get the answer, okay?

1:45:02

So this is the thing. And this kind of evaluation valet section, which I do not want to get into

1:45:06

right now. So you all the part may delete because you might be confused with this, okay? So this we

1:45:11

have not seen today. I will just remove it from my notes so that you don't get confused. So this

1:45:18

we will be seeing in more detail later on. But until now, this is the final story of where we are.

1:45:23

We have seen the entire rag pipeline starting with, you know,

1:45:27

taking the data, chunking, embedding, all the way to the retrieval part. Okay.

1:45:32

So we've seen that. Okay. Uh, all right, guys. So that's where we are right now. And as I say,

1:45:39

uh, yeah, the final part of what we did was an informal grounding check also. Like with rag,

1:45:45

without rag. Without rag, without rag, so normal LLN, what we discussed. So that's one of a part.

1:45:50

Okay. So yeah. So, and there is a more formal way to do it. So what we did majorly today was just, uh, you know,

1:45:57

informally, we went to the PDF and we were checking, is the annual revenue indeed 2020?

1:46:02

Is it totaling correct? Because the human evaluation we were doing. But some of you might be

1:46:06

confused, that sir, it's for manually caring or how can't do. So that is actually done using

1:46:10

specific rag evaluation techniques, which we will discuss. We will talk about something called

1:46:14

rag triad. That will be part of an advanced rag discussion that we will have later. Okay. Fine,

1:46:20

guys. So that's pretty much all that we have for today. So just to kind of summarize the contents,

1:46:27

We were able to see the top K retrieval.

1:46:30

We have understood the delimiter concept.

1:46:32

Delimiters, what delimiters are from a hash, hash, hash, hash, hush, question.

1:46:37

So how you're framing that.

1:46:39

Okay.

1:46:39

Generate answers that site which chunks supported each.

1:46:42

So it's basically a grounding of chunks retrieve.

1:46:45

You're asking the question.

1:46:46

You're getting the chunks.

1:46:47

And if you have the right metadata of those chunks, you will know that from where the chunks were retrieved from.

1:46:52

Okay, this is, I think, to some extent, related to what we have seen in the prior session with metadata.

1:46:57

And finally, complete a small end-to-end rags.

1:47:00

We have actually done two today, Tesla and the Nestle one.

1:47:03

So we have seen a very small mini case study where you were able to see a very real world

1:47:07

rag application using two cases. Okay. So, so that's all.

1:47:12

That will be all for today, guys. And next session is another very exciting session.

1:47:16

We are coming to it. We're going to be discussing about memory and control flow.

1:47:22

What is memory? We'll be seen. And we are slowly entering into agents from here.

1:47:27

So now that we have seen rags and LLMs and other things, so from here onwards,

1:47:31

we are entering into some deeper discussions on agents.

1:47:36

Agents will be a very new and exciting area we're entering into now.

1:47:39

Fine. So any questions, right? All of you have followed the class today, whatever we have done.

1:47:43

What is the purpose of delimiters? Herprete. Delimiters? Yeah, no? Delimiters are basically

1:47:48

this. So you're actually using it as kind of a separator. Otherwise, not?

1:47:55

this whole text. So you're just using it as a separate one. First question, next context.

1:48:01

See, how will the LLM understand, that question is, what's a context in? Because you're sending

1:48:05

the entire text in one go, right? Remember, when you're making an API called to a large language

1:48:10

model, a poor tech, so LLM can how can't tell what is the question and what is the context? I hope you're

1:48:17

with me. So that is why we are using delimiters. We are saying, okay, hey, you know, whenever you have

1:48:21

something starting with question, that's the question. And whenever you have something starting with

1:48:25

context. So that is all that we are saying. So this your user message is

1:48:29

template. When the final user message is getting framed, you will do it this thing. You will say

1:48:33

hash-h-h-h-h-h-h-h-h-h-h-ch-ch-question. And this is the thing that we go to the language.

1:48:40

So it will know that what is the context and what is the question.

1:48:44

Okay. Okay. Okay. Okay. Okay. Okay, guys. Fine. Thank you all of you. I'm, so. So if there

1:48:53

no questions. Thank you, everybody. Once again, have a good night. I will see you again on

1:48:58

Wednesday, usual time, and hand it over to Prata for the other things. Thank you, all of you. Take

1:49:04

care. Good night, everybody.

1:49:07

Yeah. Sorry, I think, sir, someone asked a question about multiple PDFs. Is that?

1:49:14

I answer. I answer. That was a question. Okay. You can do it. Yeah, I answered all you. Thank you.

1:49:19

Okay. Thank you. All right. Thank you. Thank you so much, sir.

1:49:23

Sohith, your hand is up. Is there something you want to ask?

1:49:30

Okay. All right. Yes, not. Okay. Guys, I'm releasing the feedback poll. Make sure you fill the feedback pool.

1:49:38

Rated 5 if you liked it. And yeah, once the feedback poll is done, we can start with the Menti Menter Quiz.

1:49:53

Almost half of you have voted till now. So I'll wait for a couple of minutes.

1:50:23

Still five people are left to vote. Please make sure you vote quickly so I can release the feedback poll.

1:50:53

Okay. Three people are left.

1:51:00

I've shared the links and the screen is also sharing.

1:51:14

Is there anyone who is not able to fill the feedback pool?

1:51:21

Guys.

1:51:23

Chat, is there anyone who's not able to fill the feedback poll?

1:51:32

Okay, all right. In that case, I'm going to end the poll now.

1:51:42

And we can start with a mandameter question.

1:51:53

All right. So I'll start with a Mentiometer quiz. I'm just waiting for more people to join in.

1:52:23

Not getting the link to join. Okay. Are you able to see the screen?

1:52:31

I've sent the link again in the chat. So okay. Anyone else having any issues?

1:52:53

So like out of 16 players, 16 attendees, only seven are in the quiz.

1:53:04

Okay, 15. Out of 15, only seven are there in the quiz. Can I get some more people?

1:53:11

Eight, okay. I'm hoping for 10. At least 10. At least 10.

1:53:22

I know you guys can hear me.

1:53:29

I know you guys can hear me.

1:53:32

Hmm.

1:53:37

All right, fine.

1:53:43

Um, in that case, I'll just start.

1:53:46

Shouldn't wait too long.

1:53:52

Okay. Anyone who wants to join, they can join later, I guess, send the link anyways.

1:54:00

All right. So the quiz is started. Which rag stage searches the chroma collection?

1:54:10

Fairly easy question. Which stage searches the chroma collection?

1:54:22

I hope you guys don't get confused.

1:54:26

It's really easy question actually.

1:54:29

Okay, yeah. The correct answer is retrieve.

1:54:44

Retrievel step is the one that searches for the search in the collection and then starts giving the answer.

1:54:51

Okay. Next question. Which value is passed to ChromaDB to control retrieval count? Now this one is a little difficult and it's specific to ChromaDB. So might be confusing, but it's kind of important for you guys to know this.

1:55:21

So this is a question.

1:55:26

You want to control the retrieval count.

1:55:29

So what is the name of the parameter that is passed to ChromaDB to do that?

1:55:37

Yeah. So the correct answer is end results.

1:55:45

It's okay. I understand a lot of you might not get this correct because it's not something that.

1:55:50

because it's not something that is not something you guys have practiced probably.

1:55:55

So once you guys practice it, you will all get the correct answer.

1:56:00

All right. The end results is the correct answer. The others are just like confusing.

1:56:08

So. Yeah. All right. Next question. Oh, we have more players. Awesome.

1:56:20

Which choice can increase retrieval and prompt processing latency?

1:56:28

So how what what is the what is something that you can do to increase the latency?

1:56:34

Increasing latency is bad by the way. So yeah.

1:56:40

I think everyone should be able to get this one correct.

1:56:49

this one correct oh okay i am a little surprised by raising k and lowering k so see raising

1:56:56

k means the number of chunks that you are retrieving right top k you will be retrieving the top k

1:57:05

chunks when k is equal to say three you are just retrieving top three chunks but if k is let's say

1:57:11

100 what's are covered in the example um during the class if k is 100 then you are retrieving 100 chunks so

1:57:18

obviously retrieval time is going to increase and prompt processing time is also going to increase

1:57:24

so the whole latency is going to increase right if the k is very high the latency increases that's

1:57:31

what sir was explaining and that is the correct answer okay lowering k is going to decrease the latency so

1:57:48

all right next question last two which distinguishes generate without drag

1:58:04

from rag answer so you have you have you have two functions generate without rag and a

1:58:11

function called drag answer now you've probably not seen these functions anymore anywhere so i want you to answer

1:58:18

common sense what could be the distinguishing factor based on the options it's fairly easy

1:58:28

actually if you just think about it you will everyone will get it yes so everyone uh okay most of you

1:58:36

did get it generate without rag clearly means it is not using any rag that means there is no

1:58:43

retrieve context and rag answer will be of course you are using rags so you have

1:58:48

to have some sort of context right the other options are just not valid uh this is the most

1:58:57

common sense correct option okay sometimes you need to guess the answer also if you don't know it

1:59:18

what is the main value of preserving chunk distance in retrieval output so chunk

1:59:28

chunk distance means whatever chunks we have retrieved they are distances why do we want to preserve

1:59:35

that when we are getting the value from chroma db when we are doing retrieval why do we

1:59:41

we want to preserve the distances the uh again options are options make the answer

1:59:50

kind of easy to guess yes uh so the correct answer is it supports relevance inspection

2:0:00

basically if you have multiple many chunks and you can see their distances you are able to

2:0:06

tell what is going to be the most relevant chunk how are the other chunks related to you

2:0:11

other all of that so this is useful for your interpretability okay that is why

2:0:20

this is this is the correct answer and this is the important question all right with that i think

2:0:27

we are done with the minty middle quiz yeah let's see okay ragster congratulations

2:0:41

and with that we are at the end of our session i will see you guys on wednesday

2:0:48

and yeah have a good night bye bye i'll end the 20 meter quiz now stop sharing okay all right