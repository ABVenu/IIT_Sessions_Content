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

Thank you.

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

Thank you

16:36

Thank you

17:06

Thank you

17:08

Thank you

17:10

Thank you

17:12

Thank you

17:14

Thank you

17:16

Thank you

17:18

Thank you

17:20

Thank you

17:22

Thank you

17:24

Thank you.

17:54

Thank you.

18:24

Thank you.

18:54

Thank you.

19:24

Thank you.

19:54

Hi, everybody, welcome all of you to the session. We will just be starting on.

20:24

Thank you.

20:54

Thank you.

21:24

Thank you.

21:54

Thank you.

22:24

All right, guys, welcome all of you, once again to the session.

22:38

So today we have a very interesting session and as part of today's session we'll be talking

22:45

about a very interesting example with respect to multi-modal models.

22:51

It will be a little different from what we have done also.

22:54

a comparatively easier session I would say. So it's a it's a comparatively easier session

22:59

and we will specifically focus on multi-modal models.

23:10

Now coming back to the, so coming to the general mind map in terms of what we will do and what we have done so far just to give you a little bit of

23:24

text. This is where we are right now. And so we have talked about, so we have talked

23:31

about the, the concepts of rags. We have talked about the concepts of agents at a conceptual level.

23:39

Even last session, we had a very interesting demo where we looked at the e-commerce agent.

23:45

In fact, that that agentic rag demo that we saw. Okay. So we were able to look at a broad

23:54

Shortly speaking, we looked at rags, we looked at agents, we looked at tools and the current

23:59

module until the last session, we have looked at various advanced metrics to measure retrieval

24:06

quality. And we have also discussed a few advanced aspects with respect to rags.

24:13

So now in the current session, we're going to be exploring multi-modal pipelines specifically with

24:18

respect to speech and vision data. Speech will be the main focus from the demo perspective.

24:22

and by the end of the session, at the end of the session, we will be able to connect

24:28

the dots with respect to not just how you build large language models dealing with text,

24:35

but we will also be able to understand how these models are also able to integrate audio data.

24:42

So first time we'll be actually talking about speech data. Speech data we have not really

24:46

seen in the sessions before. So in this particular session, we will also explore the ideas around speech data.

24:52

So how these language models are working and how they, how they handle speech data.

25:01

So that's the focus area that we'll have you.

25:06

And by the time we complete, we should be able to build assistants that listen,

25:09

summarize and speak, which is really cool. All this while we did, we have built assistance.

25:14

We have actually done quite a lot of interesting demos. But if you again look at the conversation

25:19

we had until now, it was mostly about building assistance,

25:22

which are taking in some kind of text input and based on that they are generating

25:27

some kind of text response it has just been i would say broadly uh text in text out kind of

25:32

systems right that's what lLMs are doing right if you look at large language models whatever we

25:36

have seen and discussed so far large language models are effectively nothing but you're giving a

25:43

specific prompt as input you're giving a specific prompt as input and based on that some processing is

25:48

happening and it is generating some kind of a completion as a response.

25:52

so it is taking a text input and it is giving a text response that is fundamentally what large

25:56

language models are doing but how can we incorporate other forms of data and that is the big focus

26:03

area like you know not just with respect to um not just with respect to text kind of data but can

26:12

we look at other forms of data particularly which can handle images which can handle text and those

26:18

kinds of things okay those are effectively other languages well i mean

26:22

So, Ali, just to clarify, to answer your question, the approach will not change, right?

26:27

Even if you talk about building models with respect to other languages, the concepts will not

26:32

change, right?

26:33

So if you if you look at the large language models, all the large language models we have even

26:39

today, if you look at the GPT models, even the GROC models that we used in our sessions, the Lama

26:44

model that we used, they are already trained on other languages as well, by the way.

26:49

It is not that the GROC model is, the Lama model is only trained.

26:52

on English, no. It understands other kinds of tokens also. Now the thing is that, yes,

26:58

there are some specialized models which are trained particularly on the other forms of languages.

27:04

So, there are some special, you know, specialized models which are trained on other languages

27:11

like, as you say, Arabic, Kurdou, these kinds of languages. But obviously that is going to be a different

27:17

conversation. But yeah, but there are specialized models. And what is different about these models?

27:22

So, you know, the different thing about these models is that the Arabic and Urdu, all these models, what they do is they are explicitly trained on, they are explicitly trained on only those kinds of tokens.

27:35

They are explicitly trained on only those kinds of tokens.

27:40

Not just the English tokens, but they are also specifically trained on, I would say, the so-called Arabic tokens.

27:51

And that's one.

27:52

way to look at it. So yes, there are, there are many, there are many Arabic LLMs that we have

27:56

and, like, an Arabic is actually a very popular language also. It's a very, very popular language. And

28:02

there are, there are a lot of good Arabic alums like JAS, ALAM, ASGPT, No, you can, you can look at,

28:10

you can explore some of these examples. Okay. So if you are interested. So there are many of

28:15

these kinds of language specific LLMs you will find. Not that, not that the, not that the,

28:22

Lama models or the GPD models don't understand the Arabic language. No, they are also trained

28:26

on the Arabic language that are basically. But then, yes, there are many subtleties in the language,

28:33

there are many specifics in the language that the general purpose LLMs will not be able to

28:37

pick up. All these, you know, American companies like the Open AI Anthropic and all, they are

28:43

mostly focused on English tokens, right? And at the end of the day, LLMs, the model is ultimately based

28:49

on tokens. What kind of characters and what kind of tokens have you seen? What kind of world?

28:52

words have you seen? So, if you're able to build a model specifically on the Arabic language

28:58

or specifically on the Spanish language or specifically on the English language. So that means

29:05

those models understand those specific morphology, idioms, dialects, the cultural context much better.

29:14

General purpose, everybody will understand. But the specific models will understand those aspects

29:19

much better. Language specific models, okay?

29:22

So, yes, so there are a lot of Indic languages also. There are a lot of Indic languages,

29:27

Indian languages, and all these kinds of LLMs you will also find. Like, if you look at Indic

29:32

Indic languages, there is Sarvum, there is also Croutrim. Crut Trim is that particular, you know,

29:40

thing by OLA, the OLA company, you know, CrutTrim AI. So these are some things which are

29:48

specializing in Indic languages. There are Chinese, Chinese models.

29:52

that are there, like when the Japanese models that are there, okay, and there are multi-modal,

29:57

multilingual models also that we have. No, no, no, that is fine. That is just the,

30:03

I think this is just the language specific aspect that I wanted to answer for you. But the embedding

30:07

model concept will also be very, very similar. So I would say, I would say, yes, there are language

30:15

specific embedding models also that we have, just to clarify. So just like we have got different

30:20

LLMs for different languages. There are also different embedding models that you have for different

30:24

languages. So if you go to this website, I think I introduced this in the initial part of my session.

30:30

I talked about multi-MTEB, right? It is a multilingual text embedding leader boat, okay, benchmark.

30:40

So you can see this one. This is, this is actually a text embedding kind of a benchmark and you've got

30:46

across the languages, right? I hope this answers your question.

30:50

and Ali, what you initially are. So you can see there are Chinese embedding models,

30:53

there are Indic embedding models, there are German embedding models. I mean these, these are not

30:57

LLMs. Embedding models are responsible for what? They are responsible for taking a text and

31:02

generating a sequence of numbers, embeddings, for saving in a vector db for comparison purpose,

31:07

for semantic similarity purposes, whatever. So because different languages will have different

31:13

nuances, you have different embedding models for those languages also. So there are so many language

31:19

which specific things you have there are more if you see the open source places there are

31:23

more examples you'll be able to find okay let me ping this link once again to all of you

31:31

okay great questions to start with yes now let's move on uh

31:38

and there is one more very interesting thing i wanted to talk about maybe this is also

31:44

on a slightly different note uh kind of related to some of the conversations i was having last

31:49

you know last session with all of you so i wanted to very quickly talk about that before i

31:54

get on with this one because this will be a quick example that we will do it will be a easy lighter

31:57

thing so this is that one other thing i wanted to talk about is with respect to uh

32:02

the parsing see guys if you remember the uh the whole pipeline of a rag whatever we talked

32:11

about with respect to a rag if you talk about that whole rag pipeline whatever we discussed

32:17

we take the document we do the chunking we divide the data

32:19

into multiple chunks and then we do the embeddings we save it in a vector db and then from that we do

32:25

do retrieval so that's the way how we look at a typical uh you know rack-based workflow

32:30

which we have all seen which we have all discussed in the session we are all you know we're all

32:34

aware of that at a fundamental level now the thing is uh if you look at it from this perspective

32:41

if the parsing is the very very important part because what if your pdf consists of

32:51

other forms of data i want to just briefly touch upon that okay although multi-modal is something

32:55

we will you know we are seeing here as well but something for you to explore

33:01

the general demos are simple you can absolutely go and take a pdf you can retrieve similar

33:06

chunks and you can go and uh do the retrieval and we have done several demos of that we've done several demos of that we

33:11

with that abb manual use case also where you had a real abb technical manual

33:16

and we were able to look up information and get answers we saw that as well but the point is

33:21

whatever uh approach we use was just a text loader if you remember we use something called

33:29

langchain pi pdf loader all if you remember that pie pdf loader that means it will simply

33:35

accept the pdf file and it will simply read the text contents from my pdf file that is what that thing will do

33:41

it will just you know take that pdf file and it will simply go back and accept the contents

33:47

from my pdf file it will simply go back and accept the contents from my just scrape and read

33:53

the contents from my pdf file that's what the model will do but that's what the model is doing

33:58

behind the scenes fundamentally right so now the question is if you take a look at it so now the

34:11

how do we parse the data and turns out there are multiple uh multiple interesting

34:18

document parsing software that are there now you can do it manually but manually can be very hard right

34:25

and i'm talking about pdfs which content pictures you you would have seen examples of

34:30

pdf which contains text examples of pdf which content pictures examples of pdf which contain images

34:36

or some tables and how do you make sure that we are actually loading the data correctly there

34:41

and for this we used document parsing tools even before chunking so the rest of our rag

34:49

workflow whatever we talked about nothing changes so we chunk we embed we save in a vector tb retrieval

34:54

retrieval retrieve chunks all that is the same now even before we start doing the chunking the part

35:00

where we are reading the pdf or parsing the pdf we are trying to understand the contents

35:06

parse means we are trying to understand the contents that that are present that is a difficult thing

35:11

because as i told you in a real world pdf you can contain uh it can contain images

35:16

it can contain tables it can contain charts and how do you go back and solve it like especially

35:21

scientific papers technical documentation you know invoices invoices we have it's not just text

35:27

invoices have a lot of structure to it insurance claims health care forms if you see there's a lot

35:34

of images and all that you will be seeing so this is these are approaches that we use for

35:39

taking the data and transforming them into a i ready data so lama index and lama parts

35:46

also gives a free tier let me ping this to all of you you can explore it definitely

35:52

you can definitely explore it and you can see this one so they give you some free credits for

35:59

you to practice which is great for a demo and you can try this out you can try this out later on

36:04

how lama index can be used okay let me just quickly uh connect this

36:09

just give me one minute let's put this thing back on

36:26

just yeah you're very similar to that you can access to an API

36:56

yeah so as i was mentioning uh

37:11

so this is the lama parts platform and yes as i just said you can access to an API you can see

37:16

there's a section called API keys and uh the llama parts is again it's a proprietary software

37:21

it's like a model and it's not a large language model it's a kind of a model that they're using

37:26

and these are models like i would say things like detection models object

37:30

detection models and all this that are built in so you don't have to download it and do all the heavy

37:34

lifting but you can connect to lama parts through the API key and you can see the free plan

37:40

usage is this thing this is the free plan usage ali you have a certain free tier i would say

37:44

enough for learning and you can go and use the free tier this is how the code snippet will

37:50

look like you can take a look at it this is how simple the approach will be you can connect to lama cloud

37:55

if you are if you are doing with python this is how the code snippet for parsing and extraction

38:00

will look like you can just import lama cloud in python and you can give your API key the same way

38:04

we have used groc API key instantiator client the story remains the same only thing is that the

38:09

code snippet changes and the code is also given here await that is you get the file

38:13

object id tier all this you specify and end result you end up getting the overall this thing

38:20

you can actually try this as well very interesting so there's a there's a there's a there's a trial

38:25

mode that you also get which is quite cool you can take some sample documents let's say i can take

38:29

a uh catastrophe report or i can take a kind of uh head statistics or a clinical study

38:38

clinical studies are also uh extremely rich in you know text extremely rich in different types of

38:44

images you'll have some tables you'll have some pictures can you see a picture a flow chart is there

38:49

so so yeah so this kind of clinical studies are very rich in this kind of data there's not just text what i'm

38:55

i'm trying to highlight here is not just text kind of data because if you take a look at this uh

38:59

look at this all of you see here i can select the text this is very important this is what we

39:03

are doing when i was uh using pi pdf loaded in my rag session i was able to select the text

39:09

it was selectable text but the moment you look at a real pdf like this oftentimes your text will not

39:14

be selectable oftentimes your text will not be selectable can you see i i can go to the other one

39:20

so we have this uh so we can take one more uh this thing so we can take one more uh this thing so we can take one more this thing so

39:25

can remove this file let's take uh something else it's a semiconductor report our component

39:31

data sheet this is a very interesting one component data sheet it has lots of pictures this is a typical

39:36

equipment rag kind of a use case we were doing the other session right abb use case we were taking

39:42

and you can see right now this is how it will be there'll be there'll be lot of images there's a chart

39:45

there's a table there's some text and the interesting part is you cannot read the data from here

39:51

so although this is text we can see but we cannot

39:55

select it so it is not text exactly so we have to use something called oCR or optical character

40:01

recognition to extract that text and that is exactly what lama parts will do for you you can build

40:05

your own methods for doing it but this is just one of the approaches i wanted to share

40:09

and you can see very interesting how it has extracted the jason so the code behind the scenes is this

40:14

this is the code that they have written behind the scenes and the results are this so this is like a

40:18

preview like so given this kind of a pdf let's say this is the pdf or the jpg whatever file you upload

40:24

this is the fan data sheet.p whatever right so given this particular pdf see how we have managed to

40:30

extract five images from that pdf and it has automatically done created the chunks and done the

40:37

embeddings for you this is something that we talked about right every images will be like a chunk

40:42

so given the pdf this is the image this is that logo can you see i is that logo this is also the image this is

40:48

also one of the images it has extracted so behind the scenes what is it doing in case you're wondering behind the

40:54

since it is going and using object detection and it is trying to uh you know it was it was trying

40:59

to locate where are the images in the pdf and it was trying to go back and uh retrieve it

41:07

by pdf was only for text okay so in line with our multimodal session i'm just trying to give you

41:12

an idea how you work with other forms of data that's it is only for other forms of data what if your

41:17

pdf has pictures if i if you were using pi pdf it will completely skip pictures it will not give an error

41:22

error will not come it will still work but it will completely skip the images that is how we looked at right

41:28

so if it's a if it's a normal pi pdf loader that you used it will completely skip the pictures

41:35

right that's the thing i talked about and this is the graph it has actually taken the picture of this

41:40

picture of this picture of this picture of the table the layout model has been used this is the

41:43

embedding model you can take a look at the embeddings right so all this we're able to spot right

41:52

this is a hard one hard one so for for parsing what you're seeing on this mean there is no one

41:57

approach for doing it early and parsing is actually very hard so otherwise rest of the things fit

42:02

nicely into the pipeline even then there are a lot of things which needs to be done but parsing is the

42:06

first step usually the focus was on text so that's why we work with text parsers but if you have

42:12

other forms of data then you will use these kinds of approaches right yeah yeah all right now uh

42:20

and you can see the jason you can see the

42:22

the tables and other things xllas the pdf file you can also so all and the text obviously the

42:28

text that is free you can also check it up okay so the data is actually given out in this manner

42:33

over all okay not really unk it so uh as i say chunking so once you have taken the

42:39

pdf and once you have extracted so what will happen if i have to uh you know give you a very

42:44

very simple understanding of it you will basically end up getting pictures and every picture

42:50

will be like a chunk so if you think of a if you think of a multi-modal rag kind of a use case

42:57

if you think of a multi-modal rag kind of a use case every uh every image will be like a chunk

43:04

and every text chunk will always be there so we already talked about that so we will end up

43:09

creating text chunks and we will end up creating image chunks so text chunks we already know

43:14

you take the entire PDF you read the text out of it you create chunks and every picture that you

43:19

you extract is also like a chunk and now the only thing is that anchet the same way that we create

43:24

chunk embeddings we will also create image embeddings we will take those chunks and we will create

43:31

embeddings similarly we will take the pictures and we will create embeddings so the vector dp

43:36

will contain both right makes sense i hope the idea is clear okay and this if you want to do it

43:43

open source because i told you lama parts is not free up to a limit it is definitely free

43:49

if you want to do this in a in an open source manner you can explore something called

43:55

pi mu PDF just explore this library this is a very very good library that is used for open

44:01

source parsing if you want to do something very similar to uh llama parts is giving you

44:08

very similar capabilities just that you want to do it in an open source manner there is a

44:13

python library called pi mu pdf you can install it and you can work with it just an option i want to do

44:19

now let's move on let's come back to the contents of our session okay so multimodal

44:25

pipelines we will look at speech and uh this thing and this is the primary end result that we

44:31

will try to build here this is a very interesting one so we will map a multimodal pipeline

44:39

so we will take a real audio transcript so let's say a typical customer care conversation

44:46

is an audio transcript right a typical customer care conversation will be like an audio

44:51

transcript so we'll take a real audio transcript and from that audio transcript that is speech data

44:56

we will do speech to text we'll take that speech data and convert that to text we'll get the complete

45:02

transcript from the transcript we will basically do the summarization and from the summarized

45:07

transcript we will convert it back to speech so we will see that whole end to end to end pipeline

45:11

and in a way the objective would be to create a you know a summary a summarized version of

45:20

a let's say a call center assistant so next time you make a call to call center you are also talking

45:27

in english or you're talking in some language so you're you're talking in speech data you're saying

45:33

something on audio and when you say something on audio that that is first transcribed to text so speech to

45:41

and then based on the transcription it is creating the summary but the summary is also

45:47

in text so from that summary it is translating it back to speech so i am saying something in uh

45:55

speech audio data and the machine is replying back in audio data the final loop and that's the

46:04

end result of what we are trying to build what is multimodal guys we have we have we have we have

46:11

have used this term multiple times before as well and so far all our labs everything we have

46:18

focused on text right everything has been on text we are doing text in text out you give a text input

46:24

you generate a text output that's what the story has been so far so in multimodal systems they can

46:30

accept or produce one more than one type of data exactly it can have different modes for input and output

46:39

it can handle text it can handle audio it can handle images it can handle video video is nothing

46:45

but a picture and that's what multimodal systems basically are now if you think about it conceptually

46:52

conceptually for multimodal systems if you look at it uh conceptually

46:58

everything that the machine processes or everything that the large language model processes

47:05

will need to be converted back to numbers everything that the lLM process

47:09

will have to be eventually converted back to numbers that is one important thing that we

47:13

have to keep in mind so everything the lLM processes will have to be converted back to numbers

47:17

so whether it's a text data whether it's an audio data whether it's an image data whether it's an

47:21

image data remember we will have to convert each of these data formats into numeric form

47:26

we will have to take the text data convert it to numbers we will have to take the audio

47:29

data convert to numbers and we will have to take the image data and convert that to numbers

47:33

we will have to take each and every form of data and the machine will internally convert it to an embedding form

47:39

because that is how the neural that is how the lm will internally process okay so for us definitely

47:45

that's something that we don't have to worry but just wanted to let you know that behind the

47:49

scenes when a language model is processing anything this is taking you back to our very first

47:53

session when i was talking about ellips i was telling you that you give a prompt as input

47:58

you get a you know text responses output so that is what we see all this file we are seeing

48:03

that okay you're giving our text input and you're getting a text output but that is actually not

48:07

happening internally internally that entire text is getting converted to tokens embeddings a whole bunch

48:14

of numbers numeric computations are happening and based on that actually a set of numbers are given out

48:19

and those set of numbers are converted back to the output so the prompt is converted to a set of

48:24

numbers all the processing is happening here in the network and a set of numbers is generated

48:30

and that set of numbers is is basically converted back to the english completion response that is what we end

48:37

are seeing i just wanted to clarify this part so you know even though we talk about multimodal

48:43

and we will uh you know all these models like you take pictures you video text whatever

48:49

you know they're able to inherently work with all these different modes of data but please remember

48:54

inherently they are all using embedding models okay all right so this is the general uh

49:01

concept behind what multimodal stands for and this is the pipeline that we will be building once again

49:07

so all of you please give it a glance okay everybody please give it a glance what is the

49:11

final pipeline will be building just give it a read all of you

49:37

and also the main part the main part part what the main part what is the main part what is the

50:07

that flow that we'll follow just give it a glance all of you then i will once again

50:11

pick up the conversation just give it a glance just give it a glance what we are doing here okay

50:37

you know.

51:07

and just to pictorially represent exactly what we are seeing and as i as i told you like we are

51:12

going to take a sample audio file in this particular part of the conversation we will take a sample

51:17

audio file it will be kind of a voice note that is exactly what we will do right and we will use the

51:24

we will use a speech to text model this is called st t is called a speech to text model this is a separate

51:32

model as i told you all this file we have focused only on this

51:37

but today we are using two other models today we will be using a speech to text model to take

51:42

that sample audio convert that into a transcript so we will go back and convert a sample audio

51:52

file into a transcript

52:07

yeah that will actually be a great case study like i think yeah i mean uh yeah okay

52:16

so we will take the sample audio file uh into a transcript into a transcript and then from the

52:24

transcript this this could be a big transcript right this could be a big transcript and the transcript

52:30

and the transcript will be like several thousands and thousands of words long depending on how big the

52:35

conversation was and from that transcript you can go back and use a

52:39

uh use a language model to summarize the transcript this is where the l lm will be involved

52:46

so first part st tt model to go from audio to transcript second time second model we will use a

52:51

llm to take the transcript and generate a summary so from the transcript we will create a summary

52:58

and finally we will use a text to speech model to take that summary whatever generated some so this will be a

53:03

a normal lm right you'll give a system message to the lm saying that okay given a particular

53:08

transcript please create a summary and we have seen these demos we have we have seen enough of

53:11

basic llm demos already this will be a normal uh system message that you will put in a large

53:17

language model you will say okay given a particular transcript please create a summary and in whatever

53:21

form of format you want if you want your summary to contain certain things you can explicitly state that

53:27

all that you can do right and based on whatever summary is generated we will go and convert that generated

53:33

that generated summary text to speech so we call it a tts and this will create the audio

53:38

file so text to speech is what we will create so this will create the audio file back

53:44

so that's the way how the whole thing will work out intuitively so again sample audio file speech to

53:50

text get the transcript transcript to summary and summary is the text text to speech but these are the

53:56

three specific models that we are using just to summarize this is a again a very nice summary of what we'll be

54:02

doing uh i'll just pause you up for a minute all of you please give it a glance

54:06

it's a pictorial way you can get a sense of what we are trying to achieve okay all of you please

54:12

give it a glance

54:32

and you know vishal has asked a very nice question

54:52

bishal is saying sir in masai also there is a i summary and a i tutor

54:57

actually this is a very good question in fact yes a i summary works in very similar way

55:00

so uh what the team also after every lecture what they are doing is they are looking at

55:05

everything that i'm saying and see the entire zoom recording is happening right so zoom already

55:10

internally has a feature so the masai platform already has this integrated they're doing exactly

55:14

the way we are talking about yes that's a great great connect that you got to there we shall

55:19

yes that's exactly what they do or i would say very similar to what they do i wouldn't say exactly

55:23

because there are some other custom components that masai is also using but yes absolutely

55:28

whatever i'm saying whatever exactly the wording i'm using the whole transcript is getting recorded

55:34

and from that entire so it is doing speech to text that is something zoom is doing the massai is not

55:38

doing that we are using a zoom platform we are paying for zoom right so zoom is doing that stttttt

55:43

zoom is doing because we are paying the zoom subscription so zoom is doing that speech to text we get our

55:50

transcription and from that transcription masai is using its own logic to generate a summary zoom also gives a summary

55:55

but we are having our own summaries and you know so yeah that's a good use case

56:05

okay there are many other use cases related to this i'll come to those conversations but yeah

56:10

let's just go through this first yeah everybody we did

56:25

you know.

56:55

Thank you.

57:25

All right, hope all of you have gone through it.

57:40

And Ankit, good question.

57:42

Ankit has asked a question, sir, where will Rick rag fit in the pipeline?

57:46

Well, Unkith, it depends on how you want to customize it? Well, of course it can fit. If you want it to fit,

57:51

it can fit. If you want it to fit, it can also fit. So, Unkith, one, one, you know, one good good, you know, one good

57:55

application of rag here could be let's say, you know, I will take the same example of,

58:03

I will take the same example of, let's say, the Maasai lecture recordings that Vichal was raising.

58:11

So it could be a great use case. So let's say whatever I'm saying in the session, that is my voice,

58:16

right? So I have my voice data and the speech to text model that is present in Zoom is converting that

58:21

to a transcript. So until that part, we are sorted. Let's let's leave out this part. Let's let's leave out this part.

58:25

let's let's leave out this part entirely so so until here we have done the transcription part so

58:31

at this point in time from whatever i've spoken in the class the entire transcription has been done let's say

58:37

this is where we are right now okay the transcription is ready now what you can do let's say masai is giving

58:43

you a feature where you can do question answering on the platform based on whatever i've taught you

58:50

this could be a great application you can potentially build or rather we can potentially build

58:55

right so students when they go to each of the recordings like let's say you've got

58:59

session number one from last week another session we did last week two sessions every week

59:04

right so let's see you go to one of the sessions so what will happen is there'll be a vector db and

59:12

the vector db will basically contain all the transcripts right so first part of the pipeline would be

59:18

from the speech data to the transcription save all these transcripts in the vector db

59:25

so basically against every single meeting all the transcripts will be saved as embeddings right

59:31

so everything will be saved as embeddings here so everyone can relate to it and now masai can

59:38

build a small user interface where people can ask a question and they can get an answer this is

59:46

just like whether rag use case will fit in an kith asked a question unkith i hope it clarifies this

59:51

will be a beautiful example of rag so we are able to do speech to text and

59:55

and then uh you know you can go against the go to that particular recording and you can you can use a

1:0:01

q and day feature which we can potentially build i don't think we have this but you can potentially

1:0:05

build that feature where uh you can ask a question and if you ask a specific question this will

1:0:11

not just give a general answer but this particular rag system will go and look up in the vector db

1:0:17

find out what are the similar chunks from what i discussed in the class because this is my transcript

1:0:23

data right my transcript data has been embedded

1:0:25

so based on whatever question you ask in the platform it will go to the vector d we retrieve

1:0:30

the relevant chunks and that is the answer based on what i taught you not something external to

1:0:34

what i taught you make sense so i hope you can connect the dots now

1:0:43

okay okay very nice so you can see now this is this is exactly what i wanted you guys to do

1:0:49

there's so many nice there's so many nice use cases that came up today and this is exactly what we want you to do

1:0:55

we want you to think through these use cases so next time you come across these new topics how do you

1:0:59

think through use cases things that you're using on a day to day basis and this is so nice okay

1:1:05

everyone is able to connect all right hope you've gone through it just just take another minute here

1:1:10

and then we'll continue on take another minute here all of you

1:1:25

you know.

1:1:27

Thank you.

1:1:57

Thank you.

1:2:27

All right.

1:2:57

this i think everyone's okay with the with the with the flow i hope all all is good to go

1:3:02

so from the speech we go to text summarize the text to speech and then the spoken summary this is what

1:3:08

we are basically trying to do here and you can also see where vision fits in so where is the

1:3:13

aspect where the vision models basically fit in so vision models also fit in the same pipeline

1:3:18

you can see this one so you can actually take a a particular photo or a screenshot and we can use vision based

1:3:25

models that will generate a short description of that image so ultimately we are converting

1:3:30

it back to text and then we are processing it just like a text data so so that is how it's happening

1:3:36

so whether it's audio data whether it is text data we're ultimately converting it back to text and we are

1:3:41

processing it you can see that so that is all that multimodal is referring to okay so we are so even if it's

1:3:46

a vision kind of data so even if it's a picture if you upload a picture uh the vision-based models will

1:3:52

basically do image captioning and beyond that

1:3:55

obviously so the model first converts the visual context into embedings or an extracted text

1:4:00

description and then processes it's just like any other input that's the idea ideal thing okay and

1:4:06

you can see this is going to happen parallelly so vision is a separate parallel input okay so it is

1:4:11

like a separate input so if you have if you upload a picture so speech will be one kind of input

1:4:15

definitely so this is what we talked about like you take the speech converted to text and

1:4:20

all that will happen that's is text data and similarly you take the picture and the vision models will go and

1:4:25

convert that texture you know that that that particular picture also into description okay you can see

1:4:30

from the the vision model will interpret the visual content whatever picture you uploaded and it will

1:4:35

generate a description a vision description look and this will be the structured information

1:4:41

that we'll be able to generate from the image for example you can see here i upload a

1:4:45

photo or share an image of this particular thing this is the image that i share and this particular

1:4:51

vision model will be able to analyze that picture and it'll be able to figure out what is the

1:4:56

exact text content that is coming out of that picture so that is the way how this uh this particular

1:5:01

thing will work out and this is what we are in you know generally seen we'll be using grog all through

1:5:07

so grog has all these capabilities built in uh speech to text there are many models we can use

1:5:12

but we'll stick to the grog whisper model so uh grok has a whisper model whisper model

1:5:17

whisper is by opening eye and it's an open source model unlike other opening i

1:5:21

models which are paid and which are not available for free uh whisper model is open source

1:5:27

you can use it and we will use the grog API to access the whisper model and get the results

1:5:32

it will be just like through an API key you can also do it locally but we will just make an

1:5:37

API call and do the thing okay uh summarization will be the grog chat model so we have

1:5:44

already seen grog chat we can also try olama cloud we saw olama in the last session we understand olama as well

1:5:50

we know how to use olama so same thing but we will stick to grok and finally for text to speech

1:5:56

we will use something called gttts so what is gtts gtts gttt stands for uh google text to speech

1:6:02

so google text two speech is also an open source model that we have right so that's what

1:6:07

we will do right now so we will use all the cloud services for these models so the speech models

1:6:11

and the vision models we will be using hosted a i models

1:6:15

hosted AI models completely right just to clarify and this is again completely up to you i mean

1:6:23

it's it's up to you how you want to drive it there's no one particular reason why you will do it this way or

1:6:29

whatever so you can do it locally also you can take the speech models you can do it locally you can take

1:6:34

the vision models you can do it locally but remember the local thing will take more

1:6:39

so you keep the setup lightweight this is the this is the setup we will be using we will use the cloud hosted

1:6:45

models speech models will be cloud in the cloud uh the grop model will be in the cloud and our local

1:6:51

laptop will only be used for the sample files that's it you take your sample files you use an

1:6:55

API key let's say we will upload a sample audio we will use an API key to access the speech model

1:7:01

from that audio we will do the transcription STT speech to text and from the transcription we will

1:7:07

generate the summary that again will happen on the cloud so from the audio you will generate the summary

1:7:12

all that in the cloud and once that happens uh it will send it will send it

1:7:19

you know that transcript that text and it'll convert it's

1:7:22

to speech again in the cloud so this also google text to speech service also happens so

1:7:26

like again completely no API keys required it's a separate service

1:7:30

it's not happening locally it's a separate service but you don't need to uh

1:7:34

but you don't need an API key for that google gives you a very very liberal

1:7:38

free tier for the text to speech gtts okay this is referred to as

1:7:42

refer to as gtt as google text to speech so that is how we will see this thing in action

1:7:50

all right let us uh now come to the demo i will quickly uh take you through the detailed demo here

1:7:57

how this will work out so let us see this

1:8:12

you know.

1:8:42

Okay.

1:9:12

all right so guys uh let's

1:9:23

i'll be taking you through this one here um just give me one second i'm just going to open up the notebook

1:9:31

and we will walk through this one quickly uh we'll walk through this one quickly

1:9:35

all right it's a simple one and the interesting part would be uh i will share with you one

1:9:41

sample uh you know recording through the mp3 file and i'll encourage you to maybe use uh

1:9:47

maybe some other sample if you can so that will also be a good thing so let us see a demo on a on a

1:9:51

on a simple sample and then it'll be interesting if you can take any other uh mp3 file you can take some

1:9:57

other recording and you can try to run the same uh script using one of your mp3 audio files so that is

1:10:04

one of the things that we will try to attempt okay all right so first things first

1:10:09

i will import install all the necessary packages so let us go ahead and install the necessary

1:10:13

packages here pip install grok pip install grok grog gtttts is that google takes to speech

1:10:24

let us see that i will also restart the runtime

1:10:34

do is we will also download a few of the sample files a few sample files are given so these

1:10:40

are the locations where the sample files are kept you can actually go to this location i'll

1:10:45

follow the link and if you you you can see this is i think it's not it's not audible so let me just

1:10:52

share my computer sound and show show yeah you can you can see uh okay not this one uh you can actually

1:11:04

hmm yeah yeah you can see this one guys so you can see

1:11:14

so these are a this is a sample audio file that we have already given we can take another

1:11:19

audio file as well right so you can take that hello this is what it is just hear out very carefully

1:11:26

hello this is a short campus update the library is open until 10 p.m.

1:11:34

carry your student id so simple i mean you just let me just play this once again

1:11:40

hello this is a short campus update the library is open until 10 p.m. please carry your student

1:11:48

id okay so very interesting i mean it's a simple one it's a very simple uh 10 second audio message

1:11:54

and we have kept it small to make sure that there's not too much of tokens and processing that we

1:12:00

burn through uh because it isn't the free grog service anyways so that's what's what

1:12:04

we have taken here and uh we are going to load that particular data and we're going to download

1:12:10

that particular data here you can see samples equal to this is like a dictionary we are creating

1:12:14

and we are giving the file name and we are going to say request dot get URL for each loop

1:12:20

so for every item we're going to go to that URL and we're going to get request or get is how you can

1:12:26

kind of you know let's just say if you have a if you have a link you can basically go and download it

1:12:31

that's one way to look at it yeah unkid i did not understand your question if you just

1:12:38

maybe you said it was i did not understand if you can ask me again i can answer for you okay yeah

1:12:43

just please if you can refresh your question okay okay so so request dot gate will download

1:12:49

the files for me let us take a look at it so whatever files we have we are just downloading that

1:12:56

and if i refresh it oh it was audible now okay fine fine okay so yeah i'm

1:13:01

that okay and now uh you can take a look at it this is my sample audio file the mp3

1:13:12

the transcript is not required because anyways we will generate the transcript so you don't

1:13:16

need to worry about this one this one you can kind of ignore i think uh yeah this one i think i think i

1:13:22

can ignore it because this i don't require right now because anyways this will be generated and also

1:13:27

the image you can ignore for now the image is where the vision model will come in but you can

1:13:31

ignore it for now okay so what i will first do i will import the instantiate the grog

1:13:39

API key okay let us see this client equal to grok we've already seen this ecosystem before

1:13:46

so this is that simple client equal to grog that we have done and now on the basis of that what i

1:13:52

will do i will simply generate the transcription i will simply use the model to generate the

1:13:58

transcription so if you take a look at it what we have done we have installed

1:14:01

the packages we have instanti key the grog API key right and this is the sample file that we are

1:14:08

using this is that speech to text that we will do on this sample audio file okay that's what it is

1:14:14

so we'll take the mp3 file and based on that we will go and uh you know iterate the transcript that's the

1:14:22

idea okay and this is a simple way how the uh the the speech to text will be working what is it

1:14:27

technically called as i as i told you once again it's called speech to text speech two text is what is

1:14:31

for uh speech to text is what is responsible for taking the spoken audio and converting

1:14:38

that into a written text that is what speech to text will do and in fact even your youtube auto

1:14:43

captions are doing this if you say this is a good example youtube auto captions are also doing the same

1:14:47

thing so uh see normally there are there are multiple ways that creators used to add captions before

1:14:54

sometimes creators used to manually do it but if you uh look at many of the current uh like most

1:15:01

on the current videos and everything that you've seen youtube today is auto captions

1:15:06

because a i is so advanced today that automatic captions just work fine if you go back and

1:15:11

maybe have seen these demos maybe even the youtube platform six seven years back

1:15:16

we had auto captions then also but it was not that accurate you can clearly see how

1:15:20

accurately auto captioning happens today it's again a great example of speech to text so real

1:15:25

time when the video is playing real time based on the audio data based on the speech based on the audio data

1:15:31

we are trying to find out what is the text so that is what is happening in youtube auto captions

1:15:36

basically okay and and and this could be a great use case for uh you know this could be actually

1:15:43

a great use case for a youtube summary kind of a use case also right so not very hard to do that

1:15:49

now based on this pipeline that i discussed you can technically listen into any uh

1:15:55

audio like it could be a youtube video as well which from the sound bites whatever audio that you can

1:16:00

get you can take that youtube audio and you can extract the text out of it and from that you

1:16:06

can summarize so what you can do is you can build a complete youtube video summarization pipeline

1:16:13

that could be a very practical application of what you can potentially build so whatever we

1:16:17

are talking about here you can build a youtube uh video summarization pipeline so take the

1:16:25

load the video data extract the audio part out of it because we are only concerned about what is

1:16:30

what is being said in the video because the captions are generated only based on the speech

1:16:35

not about the images the image content is not needed so based on whatever it's talked about

1:16:40

in the video the speech we do speech to text we get the complete transcript of the video

1:16:47

and from that entire transcript we can run a summarization or maybe even a question answered

1:16:52

once you have that entire youtube video transcript you can literally do question answering

1:16:58

that could be a very interesting thing maybe youtube should give us the service no not

1:17:03

very hard for them to do it so every video will already have the transcripts the embeddings

1:17:07

the content everything put in so maybe the next level youtube feature will be where they give you

1:17:11

a search or they give you a question answering uh you know ability but people can ask

1:17:16

questions about the video and based on whatever question you ask the chunks will be retrieved

1:17:22

and the answers will be given back that could be a great use case so based on whatever questions

1:17:28

you are asking the relevant chunks will be retrieved and the response will be given

1:17:34

that could be a great application of you know how this can be used in the youtube context

1:17:42

in fact we will see a small demo another very interesting demo in a moment

1:17:46

so that's about the uh this thing and obviously whatever transcript you get

1:17:53

whatever uh transcript you get you need to go back and also compare the transcript

1:17:58

you need to do a quality check of your transcript very important and you can ask me that okay

1:18:03

how do we do it so when we do speech true text we will get a transcript right so how do we go back

1:18:07

and do a quality text a quality check of our transcript how do we do that so we can go back and use a

1:18:12

judge model we can use an llm as a judge model to uh do a quality check there'll be some amount of

1:18:17

human evaluation also but a judge model can also be used there okay and this is how we will do the

1:18:23

speech to text with grok everyone can see this is how we can go back and do this with grok

1:18:27

so grog API key all this we have done and we will use the whisper model you can see the code right

1:18:32

now we've already loaded the file the path is here poor sample audio file is already here

1:18:39

and we will uh uh you know we have already instantiated the grog client before and we will simply say

1:18:45

client equal client. audio transcriptions. create that's it it's just client audio transcriptions

1:18:51

create is what we are doing so previously we were doing client chat completions create now we are doing

1:18:56

client audio completions create that's it and the file is nothing but the audio file

1:19:01

audio file is nothing but the uh the uh the file that i already initialized model name whisper large

1:19:06

v3 this is that this is that this is that uh you know uh s tt model

1:19:10

whisper large can you see this is specifically for uh audio and when i click on this

1:19:15

model you see this is client audio transcriptions create that's it this is all that is required

1:19:20

this is specifically for uh audio transcription okay so do that and finally response format

1:19:26

to text so you get the complete result back you'll say results dot strip get the transcript

1:19:31

and this is the complete transcript we will enter getting and then we can save that transcript

1:19:38

we can also go back and save that transcript so that's the way how this entire code base will

1:19:42

work okay let us see this one in action how we can do this so you can see i've just

1:19:52

simplify this whole thing here so again uh uh the

1:19:56

deaf speech to text i'm creating a separate function for speech to text it will take the

1:20:00

path as input path means the path where the audio file is stored we will give the path as input

1:20:09

we will do paths dot open rb read the audio file read it as audio file

1:20:15

and then we will use client. audio transcription. create give the audio mp3 file as input

1:20:21

this is the model response format is text and return results. Strip so we are simply defining

1:20:26

this can do it individually this is where the whole pipeline we have we have we have

1:20:31

we have done but i can just show it individually to all of you how the things look like so this is

1:20:36

just that just that particular function that i've created right now you can see

1:20:41

just that particular function which i've created let me run the code it is a speech to text

1:20:46

function that's it next what i will do i will simply go ahead and give the audio path

1:20:52

and i will call that speech to text function that's it we are doing it in phases that's it

1:20:56

simple straightforward i'm just trying to run it step by step there it is this is how the code

1:21:00

will look like if i run the code you will be able to see the transcript is coming out beautifully

1:21:06

can you see so it has actually gone ahead and uh taken that mp3 file whatever mp3 file which i

1:21:13

played for you a while back right this is that file i played for you this one just listen into this

1:21:18

all of you hello this is a short campus update the library is open until 10 p mpm please

1:21:26

carry your student id it listened to this entire audio and it and and and this particular

1:21:33

whisper model was able to generate the result transcript it worked nicely and it's could be a big

1:21:39

conversation also doesn't have to be just 10 seconds it can be big so more the bigger the conversation

1:21:44

bigger the number of tokens right so the whisper model is working beautifully and from this

1:21:50

transcript now we will feed it to the summarization model okay uh we can take a short break right now let's

1:21:56

take a break and come back ali you asked a question sometimes we use grog API and sometimes

1:22:00

client open not really not really greg ali so sometimes whenever i might have used it in my code snippets

1:22:05

that was just the a different provider you can stick to grok you can stick to grok okay absolutely

1:22:13

you can stick to grog absolutely absolutely whatever uh and sometimes you might be seeing

1:22:18

in my code also i might have used to open a i API the code does not change grok and opening eye the

1:22:22

code is similar the only thing that will change is right at the beginning your

1:22:26

saying client equal to grok you will just say client equal to open ai rest of the

1:22:29

code will remain very very similar so you can absolutely use the open aai APIs too only

1:22:35

differences as you rightly said cost involved because open a API API is not free you will have to pay for

1:22:39

it okay so and ali to answer to your question also makes no difference is the same so at least

1:22:45

from a usage perspective is the same but definitely there are differences in terms of how the models

1:22:49

will work open ais models are more advanced they are better that's why they charge you but the way we are thinking

1:22:55

we are thinking the implementation the demos nothing will change the code will work exactly

1:23:00

the same way got it you will just have to use client equal to open a i and use an open a i specific

1:23:05

model like for grok we were mostly using lama 70 billion versatile and all that but for open

1:23:11

a i you will use gpt models and all that sometimes you would have seen in my code snippets i've used

1:23:15

open a i and all that you had to do in in those code snippets but just replace my code and instead

1:23:20

of open a i API key use grok API key that's it that's all and it'll run

1:23:25

all right okay guys uh does it add any value if we use open a i or cloud uh i would rather

1:23:37

say anthropic because open a i is a company anthropic is also a company so let's say

1:23:41

open a i models versus anthropic models i would say uh mainly in model quality i would say

1:23:46

open a i and cloud would give better reasoning summarization quality instruction following

1:23:52

they will give more reasonable outputs abjit so definitely this

1:23:55

that is there i would i would certainly say that there's a reason why they are paid

1:24:00

models because there's definitely slightly better reasoning abilities they have

1:24:05

grog is more for speed and cost efficiency if your if your comparison is between uh

1:24:11

with respect to speed and cost efficiency then we will go for grok because grok is

1:24:15

mind you it's not using the paid models grok is using open source models so that's where

1:24:19

the cost is lesser they're only charging you the deep hosting cost like the infrastructure cost

1:24:24

they're not charging you anything for the model because the model is anyways free

1:24:29

makes sense and uh the second party answer to the question a widget will be it boils down to

1:24:34

benchmarks at the end of the day it boils down to benchmarks so different large language models

1:24:41

how do you compare the different benchmarks of the lm it's all boils down to benchmarks

1:24:48

so benchmarks need to be looked at and if you remember there was a particular thing called deep eval

1:24:52

which i might have that time shown and these are all the different available benchmarks that

1:24:57

lLMs have very interesting everyone can take a look at it very important this is in fact how you

1:25:02

evaluate language models so how do i know like whether a gpt model will do well a jemini model will do

1:25:08

well nobody knows that unless you see how those models have performed across different benchmarks

1:25:14

so for example there is a mmlu benchmark for uh you know multilingual language understanding reasoning benchmark

1:25:20

how how how well the models are able to reason there is a human eval benchmark

1:25:27

there's a truth cool qa benchmark okay there's a squad benchmark for testing the models reasoning

1:25:33

capability comprehension capabilities right so their hellaswog is there for common sense reasoning

1:25:41

so there are so many different different benchmarks for different different tasks

1:25:45

you can see there's math qa math qa is primarily for you know uh

1:25:50

you know like math's word problems like mathematical problems particularly so these kinds of

1:25:59

these kinds of these kinds of benchmarks we have here right you can take a look at it is also

1:26:03

swee benchmark for software engineering code related things okay and this is how you can evaluate

1:26:11

how different language models stand and where different language models stand based on different

1:26:15

benchmarks right makes sense so that is how you can take a calling even in big

1:26:20

projects when you are trying to take a decision okay should i use model a versus

1:26:24

should i use model b now here in the session obviously we are using grok but next time your clients

1:26:29

are asking you that okay please tell us which model should be used you will have to go back to the

1:26:33

benchmarks and evaluate one way to do it would be the benchmark second way to do it will be to go back

1:26:39

to the evaluation data and see how evaluate your models and see how well they're doing

1:26:45

that's the way you will have to do it okay all right so guys uh yeah let us uh yeah let us

1:26:50

just take a break and come back i'll complete the rest of the flow after the break okay let's take a short

1:26:55

break and i'll see you back after the break

1:27:20

I don't know

1:27:50

you know

1:28:20

you know

1:28:50

I'm

1:29:20

I'm

1:29:50

I'm

1:30:20

I'm

1:30:50

I'm

1:31:20

I'm

1:31:50

I'm

1:31:52

Thank you.

1:32:22

Thank you.

1:32:52

Thank you.

1:33:22

Thank you.

1:33:52

Thank you.

1:34:22

Thank you.

1:34:52

Thank you.

1:35:22

Thank you.

1:35:52

Thank you.

1:36:22

Thank you

1:36:52

Thank you

1:37:22

Thank you

1:37:24

Thank you

1:37:26

Thank you

1:37:28

Thank you

1:37:30

Thank you

1:37:32

Thank you

1:37:34

Thank you

1:37:36

Thank you

1:37:38

Thank you

1:37:40

Thank you.

1:38:10

Thank you.

1:38:40

Thank you.

1:39:10

Thank you.

1:39:40

Thank you.

1:40:10

Thank you.

1:40:40

Thank you.

1:41:10

So we'll continue on guys. I hope everyone's here. So we'll quickly continue on with the rest of the flow. So let us. So we have we have done the speech transcription part. So we were able to take the audio and we were able to convert that into that.

1:41:39

the transcript. Now moving on. The next phase that we will do is we will take that particular transcript and we will try to summarize the transcript. So summarization is what we will do using the basic GROC API call. If you remember, we have just created the transcript here right now. And this is stored in the transcript variable. Right. It is now stored in the transcript variable. And now all that we will do is we will take that particular transcript, which is going to be just like our

1:42:09

user message. Now we will feed it to a LLM. The transcript will be just like our user message.

1:42:15

we will have a certain system message and we will do an API call. So that's the way how this thing will work out.

1:42:21

You can see the GROC API key. We're instantiating the GROC client. The path we are also giving.

1:42:29

Where the transcript will be is saved. And we are making the API call to get the response.

1:42:36

And it's that complete flow. I mean, if you take a look at that complete flow, this is a

1:42:39

that complete flow. So first part we have gone ahead and created the transcript. This is that same,

1:42:47

you know, deaf transcript function that I talked about, right? Speech to text. So from the speech,

1:42:52

you get the text. That's the first function. And second function is the deaf summarized function.

1:42:56

And the deaf summarized function will take the transcript as input and it will curate this prompt.

1:43:01

We will, we will curate this prompt. And based on that client chat completions create, generate the response.

1:43:08

Okay, this is a summarized function. And if you see the summarized function,

1:43:12

we will call the summarized function like this. Summurize of transcript. What was returned in the

1:43:16

previous step, that we will give us input to the next step and we will show the summary.

1:43:22

And finally, the last function that we have is the text to speech function. So whatever transcript

1:43:28

summary that we end up getting, so whatever transcript summary that we end up getting, we'll take

1:43:33

that particular transcript summary. And from that transcript summary, we will generate

1:43:38

the speech the audio so we are basically doing text to audio text to speech this is the last part

1:43:44

and this is for this we are using the g tts it's a open source of free library and text equal to

1:43:52

speakable and we are just sending that particular transcript and we will we will get our audio

1:43:57

response back so that is the way how the thing will work out you can see the uh the three

1:44:02

functions i created here and this is the order in which we are executing the functions first

1:44:06

is the uh speech to text function we are getting the transcript back second is the uh the summarize

1:44:12

function we are getting the summary back and finally we are spending the summary to the text to speech

1:44:19

function and we are getting the uh the output uh the output audio file back and the output audio

1:44:27

file will be nothing but somebody spoken okay so that's the way how this entire thing is

1:44:32

basically working out if you take a look at it i have done the complete flow here

1:44:36

let us take a look at you can use any audio uh you know input here for that matter so we have taken

1:44:43

the speech to text summarize function and the text to speech function and this is a complete pipeline

1:44:49

i already have uploaded the files here you can run this so running the speech pipeline we got

1:44:55

the transcript from the transcript we got the summary and summary you can also do in different ways

1:45:00

like this completely depends on your system message how what kind of a system message you have used for the

1:45:05

the summarization what kind of an explicit system message you have used if you've used a

1:45:10

system message where you said okay in the summary i want this this this to be there i want this to be there

1:45:13

i want this to be there then the summarization will be done accordingly so the summarization

1:45:18

completely depends on what kind of criteria you are specified that's one way to look at it

1:45:24

yeah exactly so the uh you know i would i would say that instead of one llm so far what we have

1:45:30

done we have actually used three models today okay yeah and finally the the

1:45:35

the summary is saved in a spoken language and this is spoken summary dot mp3 this is the

1:45:40

file that we get got back this is the file that we got back

1:45:47

no summary is the normal lLM task uh ubrage right so first we have the transcript i think until here

1:45:52

you got it from the original audio we got the transcript and now from the transcript

1:45:59

whatever transcript you have that is the input to the lm that is going to be the input to the lLM

1:46:05

right and the llm will generate a response a summary response that's it this is a summarization

1:46:10

task so this is like like this is normally like a simple text in text out kind of thing

1:46:15

that we have been doing for so many days right you are giving a particular text as input

1:46:20

and you're getting a particular text as output so here the uh the thing that you're giving as input

1:46:25

is the transcript you're giving a transcript as input and you're getting a particular summary as the

1:46:30

output that is that is the summarization part you brush okay

1:46:35

you're with me this is the normal lLM okay and finally from that summary we are getting the spoken

1:46:40

mp3 format tTS text to speech from that summary text we're giving the summary as input and from that

1:46:46

summary we want a i to read it out we want to convert that to speech using the google model and if you just

1:46:52

go here you can actually hear the spoken summary as well and you will see the spoken summary will be a

1:46:57

complete replica of what is written here just that in you know in the default manner okay let's

1:47:03

Let's listen into this one.

1:47:08

Let's a spoken summary. Let's listen in.

1:47:11

Here are three short bullet points summarizing the transcript.

1:47:15

The library is open until 10 p.m. The library is open on campus. Students need to carry their

1:47:22

student ID. Well, it's a simple example, but you get an idea that how we are able to

1:47:28

like integrate this whole thing into a solution. And if you think about it, potentially you can

1:47:33

revolutionize customer support customer support can happen in a very different way right next time

1:47:37

you're talking to a customer care executive you are asking your question in audio and the audio

1:47:42

is getting transcribed into text everything about the audio conversation is getting transcribed into text

1:47:47

and uh next time there will not be any human agent let's say if there's an AI agent the

1:47:54

AI agent will reason and answer to you and that answer will also convert it we converted back to speech

1:47:59

so that could be one very good use case yeah and i think eventually all these systems

1:48:10

if you see the audio part will be a great thing in many systems that we have because yeah as you as you

1:48:14

rightly said unkey writing text is very frustrating like instead of typing instead of somebody typing

1:48:18

can we use a speech two text kind of model to do it for us that could be a great implementation even for rags

1:48:23

systems you can use that microphone button so in your applications you can use a microphone button so for

1:48:28

so instead of people having to manually type you can have a simple speech to text kind of

1:48:33

thing so so have the transcription based on that uh do the rag get a response back and the response

1:48:38

can also be read out to the human export so this could be a very interesting use case okay yes

1:48:58

all right uh you've just asked a question does chat gpt also works like that do they store

1:49:09

broadly similar i would say voice input is typically transcribed or converted into internal

1:49:13

representations that's right uvraj they process by a model and they have spoken back with text to speech

1:49:18

correct absolutely if you're looking at the live audio what they are doing that live thing that's what

1:49:22

they do but it does not automatically summarize every voice query summarization only happens if the product

1:49:28

or prompt ask for it and storage depends on the platforms privacy settings and retention

1:49:33

policy because remember chat gpt is not our application chat gpt is an opening eyes application

1:49:37

so it completely depends on many aspects of how they've implemented it but yeah broadly it is very

1:49:41

similar i would say right i was talking about that notebook lm use case this is also a wonderful

1:49:47

thing and i i had discussed this long back in my initial sessions if you remember and this is also a

1:49:53

classic example of multiple things happening together i would say right you have uh

1:49:58

uh you have rags happening you have the speech to text happening you have that youtube

1:50:03

subscription that i was talking that is happening so that could be a great use case of what this is

1:50:08

right uh yeah so just wanted to show you a small final case study based on this

1:50:14

which you can relate to yes but uh uncle that's right but only at the llm stage not the speech to

1:50:18

text stage that's right only at the llm stage okay after audio becomes text or after rag retriever

1:50:24

you can use the same groundedness and output format instructions for summarization okay yes

1:50:28

all right okay moving on uh let us take a small you know kind of a use case based on

1:50:46

on whatever i talked about overall in the class so the final use case we can take a um let's see

1:50:58

so, for example, let's say we have this, uh, like, like, uh, like, uh, like, uh,

1:51:28

uh um so we can take some you know some kind of uh some kind of uh some kind of

1:51:40

some kind of video some kind of speech kind of thing uh to our kind of a speech we can consider

1:51:48

right so let's say i will consider um um

1:51:58

this is a nice one this is actually a kind of uh one and half hour video that uh by kunal Shah

1:52:06

it's a nice kind of you know uh tips and tricks here shared about how to grow yourself and

1:52:14

all that nice nice video overall and just to kind of uh you know just share the link with all of you

1:52:18

and what i will do is i'll go back to notebook lm so imagine the great use case could be you

1:52:22

don't have time to see the video right you don't have time to see the video and this you can integrate

1:52:26

in many uh platforms like based on exactly what we talked about today so what you can basically

1:52:31

do is you can give it a notebook elm right i can create a new notebook and you can give that youtube

1:52:35

URL notebook element is doing something very similar to this you can paste that youtube link

1:52:40

exactly how i'm doing and notebook will automatically read the transcript of the video because every

1:52:44

youtube video is transcribed it is actually reading the youtube it's actually reading everything the entire

1:52:49

transcript of it and it is basically creating a vector db in memory vector db that is basically what is going on this

1:52:56

entire uh youtube video in fact all the sources notebook allows you to add multiple sources

1:53:01

all these sources are basically saved in a vector db you can add a youtube video as a source you can

1:53:07

add a document as a source you can add a pdf as a source all the text that you're getting so in the

1:53:12

case of the youtube video it is again going back and doing uh you know something like uh

1:53:20

audio data you're not concerned with the images here you're only concerned with the audio and every

1:53:24

video is transcribed right if we go to youtube if you see every video if you click on the more

1:53:30

you should be able to see uh the transcript for every video show transcript and this can be easily

1:53:34

script there are tools and there are python libraries to which you can uh like it's open source

1:53:39

right it's it's it's there for like you can also watch youtube in guest mode you don't need

1:53:43

any authentication to get the transcripts of the videos you can scrape it out and literally uh this is

1:53:48

like the speech to text that youtube is automatically doing so notebook lm is already

1:53:53

taking that entire transcript and it is effectively taking that transcript and saving it in a vector db

1:53:58

and next time here is the beautiful part you can go back and ask questions of your data of your video

1:54:03

so this is what i was trying to say so you can uh like you can actually ask questions what are the key

1:54:10

what are the key insights shared by shah shared by kunal and based on the question we will hit

1:54:18

the vector db retrieve the relevant chunks and we will get the answer from that entire one and a half of our video

1:54:23

so you can see our real world application where we are integrating several things and when

1:54:27

maybe instead of just giving a text response you can go and integrate that into a uh a google

1:54:32

text to speech model and that text can be converted back to speech and we can get a response back

1:54:37

so you can see this one very interesting okay and there are several other features that they also

1:54:42

have like audio overviews video overviews are again very similar to the thing that we talked about

1:54:48

is again that speech to text or text to speech the same kind of models are getting used

1:54:52

so here from the text and AI is reading it out for you so audio overview is a great example

1:54:58

of that so so so the entire uh you know kind of a video is summarized for you right you

1:55:04

so you can actually say summarize the video let's say for example

1:55:09

based on the entire transcript of the video we can summarize the video exactly like how we

1:55:13

did the demo today right you can think of this kind of a use case and then what we can do is from

1:55:18

the summary of the video we want to convert that entire text summary into a speech

1:55:22

into an audio and that is exactly what audio overview is in a way so there are some more

1:55:28

other ideas in audio overview but you can but broadly that is what it means you're taking the

1:55:32

entire summary and you're making an AI delete so it takes to speech right so this is

1:55:38

some very nice ways i wanted to connect the dots back with uh real world tools that we have

1:55:45

and we are all using where you can now slowly start to connect the pieces right all right

1:55:52

uh not directly request dot get works for a direct file URL

1:56:03

but a youtube link is a web page it is not a raw video uh

1:56:07

sorry uh okay it's not it's not a it's not a it's not a raw video or a transcript file for youtube

1:56:11

i would suggest that you can explore tools like this you can just go and google out these tools

1:56:17

just go and google out these tools if you want some python libraries to scrape youtube audio or videos or videos

1:56:22

just google out these tools y t d lp by tube are quite popular right and if you're

1:56:27

explicitly looking for uh youtube transcripts this is a particularly good tool to get youtube

1:56:33

transcripts just search for youtube hyphen transcript underscore api you know you can

1:56:39

search for transcripts on youtube okay uh sorry uh this is a python based methods we have yes

1:56:45

yeah uh-huh not very difficult uh-huh absolutely not very hard i mean if you take the

1:56:53

text la rag use case what are we doing you're asking our text question you're getting a text

1:56:57

text response you can take that text response and you can convert it back to a speech you just

1:57:02

have to add a google uh text to speech layer at the end that's it so whatever that google tts that we

1:57:09

did here in the demo today we did a the final part we did was a google tts right text to speech just

1:57:15

add this part whatever final rag response you're getting you just add this thing overall

1:57:20

right makes sense you can do that of course yeah uh i would say antigravity is more of a

1:57:30

developer focused IDE a little different little different not very different we are both

1:57:34

coding environments uh ali but yeah colab is more of a notebook environment for running python code

1:57:40

but i would say that uh you know yeah anti gravity is more of a developer focused

1:57:45

i yeah it's a little bit more developer focus but otherwise they work very similarly

1:57:50

they're also you have jupiter notebooks and all that similar thing yes will it make it a multi-modal

1:57:56

rag uh well uh i would say to some extent yes to some extent yes uh yeah to some extent

1:58:04

because you're actually uh generating something in audio format yeah if you're building the full pipeline

1:58:09

it'll formulate a kind of a multimodal rag correct yes that's right that's right that's right

1:58:15

and then you can also incorporate that with some of the other things i was talking about

1:58:19

in the beginning of the session you can use lama parts you can have your pds which can also

1:58:23

contain pictures but yes i mean towards the output side if you're converting it back to speech

1:58:27

and then definitely that you can call it a multimodal rag yes okay

1:58:34

fine guys uh yeah a lot of interesting things today we talked about uh i have already

1:58:38

uploaded the files in the 9th july folder there is a 9th july folder there is a 9th july folder

1:58:45

we have right now and that's what we have here and yali that's a good point exactly

1:58:53

so collab is that way it's a very good collab already is pre-installed with many libraries

1:58:57

antigravity is not because antigravity is something you're locally downloading it is just like a

1:59:01

vs code think of it that way that's why i say it's more developer focused you'll have to

1:59:05

install all the libraries everything manually so colab is more beginner friendly especially when

1:59:10

people like you you're all learning i would say collab is great to start with as you get more and more

1:59:14

comfortable you can go to the code editors okay that's the way how the learning should be i would

1:59:19

still say stick to collab stick to collab for now be comfortable with the learning then go to other

1:59:24

co-reditors okay that's the approach we should follow all right wonderful

1:59:44

i'm going to quickly just summarize the contents what we talked about we were able to build a

1:59:48

multimodal pipeline uh audio text in giving the audio as input getting the summary getting the

1:59:56

audio output this was the entire uh multimodal pipeline that we built and uh i will uh and from that we

2:0:05

were able to run a speech to text and check the transcript quality so basic check we will do

2:0:12

second we will summarize the transcript we will summarize the transcript the third thing we

2:0:18

talked about and finally we were able to take that transcript and do a text to speech the fourth thing

2:0:23

we did okay this was a very basic example of a multimodal pipeline that was the plan for today we also

2:0:28

looked at some other very interesting things the in the initial part of our session we talked about

2:0:32

particularly llama parts something that you guys can try out and uh this is what we will have for today

2:0:39

okay fine guys uh you can please uh

2:0:42

navigate over to the 9th july folder for you know just to go over the notebook once again okay

2:0:50

any questions i hope everybody has followed the contents for today any questions you have please let me know

2:1:12

yeah yeah it is again pre-built models umbrage it's basically just the pre-built

2:1:26

models we are using they are also for image we have models available the same way that you are

2:1:31

using models for this you you have image models as well again image is not a big part of the

2:1:35

conversation here but uh is mostly with respect to speech we did but even for images you will have models

2:1:41

unfortunately grog does not have image models right image models you will have to is

2:1:45

mostly you will have to download locally and then do it right so that's why you cannot do the demos

2:1:50

readily in grog for images it doesn't have any image you're ready models but yeah the idea is same

2:1:55

you can go to hugging face and you can try out like for example uvraj you can go to hugging face and you

2:1:59

can try out image captioning models okay you can try out uh you can check image captioning models in hugging

2:2:05

face yeah yeah behind the scenes abishka that's how they are doing it that's how they're doing it you can try

2:2:10

out some image captioning models from hugging face okay so this is a bit of a manual thing but the idea is again

2:2:16

very very similar i would say yes all right uh do they use cnn for image processing yeah bichkar i

2:2:29

think i answered that well you know uh in a way yes in a way yes if you understand cn cn cn cn stand for

2:2:34

convolution or neural networks that is what they internally use but again many of the see even for that matter the pi mu

2:2:40

of library abhikar if you remember what i talked about there also we are just using the library we are

2:2:46

just using the package right but you know behind the scenes they are actually using cnnnn they're

2:2:50

actually using object detection and trying to do it they're actually using object detection and

2:2:55

trying to do it that way that's the intuition

2:2:57

okay great all right uh yeah so thank you guys thank you so much all of you take

2:3:14

care everybody um yeah yeah thank you all of you i will pass it over to ars

2:3:27

sure sir students the feedback poll is already live please fill that in

2:3:39

also please attempt running the code that was shared for today's class as for the quizzes

2:3:46

ali we stopped because we were seeing very less participation but we can continue on certain classes

2:3:57

next week we can have a quiz after a source session

2:4:27

Thank you.

2:4:57

All right guys, thank you for attending this session.

2:5:01

We will meet again tomorrow for the TA session and next week for the instructor session.