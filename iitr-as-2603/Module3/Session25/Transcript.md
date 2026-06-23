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

Thank you

15:06

Thank you

15:36

Thank you

15:38

Thank you

15:40

Thank you

15:42

Thank you

15:44

Thank you

15:46

Thank you

15:48

Thank you

15:50

Thank you

15:52

Thank you

15:54

Thank you.

16:24

Thank you.

16:54

Thank you.

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

Thank you

20:24

Thank you

20:54

Thank you

20:56

Thank you

20:58

Thank you

21:00

Thank you

21:02

Thank you

21:04

Thank you

21:06

Thank you

21:08

Thank you

21:10

Thank you

21:12

Thank you.

21:42

Thank you.

22:12

Thank you.

22:42

Thank you.

23:12

Thank you.

23:42

Thank you.

24:12

Thank you.

24:42

Thank you.

25:12

Thank you

25:42

Thank you

26:12

Hi, everybody, very good evening all of you all of you

26:19

How is all of you doing?

26:25

How is all of you doing?

26:29

Good

26:30

Good evening.

26:31

Good evening guys.

26:41

Sorry for the little bit of thing. I'm just waiting for all to join it.

26:57

And the meantime I was also trying to start up the lab just a second.

27:11

Thank you.

27:41

Thank you.

28:11

Thank you.

28:41

Thank you.

29:11

Thank you

29:41

Thank you

30:11

Thank you

30:41

All right.

30:44

Hey guys.

30:45

Once again, very good evening to all of you.

30:47

And today we will be pretty much continuing our

30:50

our conversation from where we left off in the last session.

30:54

So we will be discussing and picking up our conversation with the aspects of prompt engineering.

31:01

We pretty much continue on from there onwards.

31:04

So just to take you back to the journey that we already completed until now.

31:10

So we have all done with

31:11

Python, we have done with machine learning, where we talked about the, you know, the important concepts in terms of how to build, moderates and everything.

31:19

And from there, we are in the current module right now.

31:21

And in the current module, we are talking about Genuity BI.

31:25

So we have started with Genvity BI.

31:27

We talked about the introduction.

31:29

Last session, last week, Thursday, we interacted,

31:34

sorry, Wednesday we interacted on the basics of prompt engineering.

31:38

Right.

31:39

So we talked about that session in a theoretical manner.

31:41

So we talked about system message, user message, zero shot for ROM, few short prompt, what are the different types of prompting techniques.

31:48

But it was, it was a session where we did not get into the code, and I told you that the next session will focus more on the Python port.

31:56

So today's session is more focused on that.

31:58

So today's session is, you know, basically the LLM in general for big designers.

32:03

And one aspect will be, we will be taking the same prompt engineering demos that we did in the last session.

32:10

and we'll see that in the Python context and we'll also discuss some very important concepts like context window what is tokens you know there's a saying that all these language models are extremely costly why why is it that they are so

32:24

what are the cost and questions for all these language models so these are the things we will talk about and of course I think the main value add from this session would be you will appreciate the the programmatic ways how we write prompts because

32:40

last session it was all in chat gpT we were doing the things but today we will actually see it in raw python how to do it

32:45

we'll write code and we'll also be we'll also try to understand some of the architectural patterns right what are the best practices and you know some of those other things we will be discussing and some of the other parameters of a prompt like temperature and all that we'll be discussing so that is generally going to be the overall agenda for the session today right now let me start the session

33:10

today with a bit of a very quick 30,000 feet overview or a kind of a recap in terms of what we did in the last

33:19

class. I'm going to just quickly open up the contents from here itself. So we did the session last on 17th June.

33:27

So I will open up the 17th June folder. Right. And if you remember, we we talked about the we talked about the foundations of we talked about. We talked about the foundations of we

33:40

about the foundations of what a prompt basically is so what are the things that what are the things

33:48

that goes on inside a prompt so what are the things that goes on inside a particular problem okay so what is it

33:56

that that that basically goes on inside a particular prompt so we have a system message we have a

34:03

user message and based on the system and user message we are trying to predict what is an assistant response

34:09

So this is the core idea that we covered on the session.

34:13

Everybody give it a glance, please, all of you.

34:17

So this is basically the format of how a prompt is written.

34:21

So we have a system message, system messages are high level instructions that you're giving to the

34:25

LLN where you're telling the LLM what to do, what not to do.

34:28

So these are the high level instructions that you're giving to the language model.

34:31

You are instructing the language model what to do and what not to do.

34:34

That is how we define the system message.

34:37

So this is where you will tell all,

34:38

all the behavior right so what the language model can do what it cannot do

34:42

well some safety features we were talking about last session so all that will be part of your

34:48

system message user message is the user input whatever the input the user is

34:53

providing more user input and finally we have the assistant message and I'm going to take you

34:59

back to that beautiful demonstration between the last class you know this was in the context

35:04

of a hospital administration assistant this is the assistant to the assistant to the hospital

35:08

to that the assistant is responsible for looking at the medical notes

35:15

so this assistant is responsible for looking at the medical loads and based on the medical notes this

35:23

assistant can uh i'm sorry so based on the medical loads so based on the uh the medical notes the

35:30

assistant can basically output and extract information like what is the age of the person what is the

35:37

diagnosis of the person what are the medical conditions of the person and so and so on

35:43

so based on the uh the text content of the medical notes we are trying to extract information

35:49

of you so that is one of the things that we are effectively trying to do so what is the

35:55

information that we are able to extract from the medical notes so that is the problem

35:59

that we are explicitly trying to solve so that is information extraction use case is what we

36:05

you know what we broadly talked about here now based on this let us look at a couple of

36:11

demo so this is the most important format of a problem that we started and based on that let us see

36:15

first time in the class i think we have done how many sessions we have done only two classes

36:22

on generative AI in the last week we just started with the ideas but today is the first session

36:28

where we will actually start to call APIs so we programmatically set things up today a lot of fun right

36:35

and you will need some time to do the setup with me right if you want to do with me

36:41

with me in the class you can do that right and uh people can people can do the setup and you can do

36:48

that basic setup with me today right everybody can do that okay so everybody can see the 22nd june

36:56

folder 22nd june folder i think sub kpass 22nd june folder is there you can go to your

37:01

google drive and there is a file called class node node node

37:05

type b by n d standard jupiter notebook and we have done these things in the classes before

37:11

everybody's aligned on that so first things first you will have to open up that file

37:17

everybody knows that how to open the jupiter notebook file okay open over here top right make

37:21

sure you're log you to pull up second thing very important this will be very new to what you

37:26

have done so far so far all of you observe this and i will highly recommend you you

37:32

can do the demo along with there is Pratap also who can guide you

37:35

along the way but this basic set up you do along with me see rest every class what i say is okay

37:40

you follow along with me you see the code you do it later but today's session i will tell you the

37:45

first 15 20 minutes up set up set up so you can do the rest of the things later on okay but the

37:53

basic setup you do along with me so that you will all be on the same track okay so first step go to 22nd

37:59

june please open up my class notes on ipy nb5 okay and make sure you're signed into google the same

38:05

kind of window ulyc okay i will pause for everybody step by step so everybody okay please i will

38:11

irritate you a little i will keep asking stupid questions but okay please forgive me but please

38:15

tell me if you're all done i will wait okay you will have to answer or chat once you are done

38:20

please let me with a yes on chat i just want to make sure everybody is able to do it along

38:26

okay if you miss out now then then back me problem would see because in a class setting we are all like

38:33

together so you can ask your questions

38:35

later on you guys might struggle okay they won may not be help and so i want to make sure everybody

38:41

is able to you know clearly set things up in the session itself okay thank you ayush thank you

38:45

heart print others are all okay i will wait for 17 responses in the chat all 17 of you

38:51

must respond okay

38:55

notebook open kallos up starting with everybody please open up your notebook

38:59

again next step um a okay and where is the folder i think just in case people do not have

39:05

the folder.

39:06

I'm directly folder link pinged so it'll be easy for you.

39:10

So that people can directly go to the folder.

39:14

This is the 22nd June folder where the contents are all shared.

39:19

You can directly open up the file from here.

39:22

Okay.

39:23

So you don't have to figure out where is the folder and all that.

39:25

So please open it up and make sure this is you're all here.

39:28

Okay, everyone please let me know.

39:31

I've got three responses.

39:33

Okay.

39:34

Okay.

39:35

thank you. Thank you.

39:37

Okay.

39:38

Okay.

39:39

Okay.

39:40

Okay.

39:41

Okay.

39:42

Okay.

39:43

Okay.

39:45

Okay.

39:46

Okay.

39:47

Okay.

39:48

Okay.

39:49

Yes.

39:50

Okay.

39:51

Prasah.

39:52

Thank you.

39:53

Okay.

39:54

Okay.

39:55

Okay.

39:56

Each of you have responded.

39:59

I'm just waiting for a few more.

40:03

Okay.

40:04

Thank you.

40:05

Thank you. Okay.

40:07

Okay.

40:09

Okay.

40:10

Others.

40:11

Okay.

40:12

I just wait for the rest of the folks for the people who are done.

40:29

Next thing you will have to do is go to grog.

40:32

Go to grog.

40:33

Go to grog.

40:34

And again, this is very interesting.

40:36

Grog.

40:37

What is it?

40:38

I will talk about that later.

40:39

Right now, we are just focusing on the setup.

40:41

Set up.

40:42

I will talk about all these things with you later.

40:44

So you have to go to console.grog.com.

40:47

Let me ping the link to all of you.

40:50

So Colab just open and let it be as it is.

40:53

Next you go to console.g.g.com.

40:56

Please log in with your Google account.

40:58

Please sign in with your Google account.

40:59

After you go to console.g.

41:01

You have to sign it.

41:03

You have to sign.

41:04

with your Google account.

41:06

And once you do that, you have to go to API case.

41:09

You can see a window.

41:11

Okay?

41:12

Google sign in kind of.

41:13

Simple, you can enter your email or then sign in with Google.

41:16

And you'll be able to see a window that looks somewhat like this.

41:19

Brock, like this.

41:20

Something like this.

41:21

Something like this.

41:23

On the top right, you should be signed in.

41:26

Now, what you need to do?

41:27

Go to API keys.

41:29

See, one time I will discuss, please follow this.

41:32

And then you can replicate it.

41:33

Okay.

41:34

seconds please see exactly what I'm showing you and then you can do it on collab and then finally

41:38

confirm to you.

41:40

Chalo.

41:41

Once you're there in Grog, console.g, go to API keys.

41:44

Okay.

41:45

And please create a new API key.

41:47

You go on create new API key.

41:50

You give any name.

41:51

You call it demo.

41:52

Set no expedition and you click submit.

41:55

Once you do that, an API key will show up.

41:59

API key is like a password.

42:01

It's like the kind of a password.

42:03

It's like a secret key.

42:04

you can you can use that key to access things.

42:07

We will see that what things they are.

42:09

Okay?

42:10

So, so first you create your key.

42:12

As a key

42:13

Then you can't, please copy that key.

42:15

Here here copy press.

42:16

Hit copy on this one.

42:18

Okay?

42:19

Here here copy and then go back to Pullab.

42:21

Observe very carefully what I'm showing.

42:23

Go back to Pallab.

42:25

Click on this secrets like option.

42:28

This secrets one option is to click

42:30

click and enter the

42:33

secret.

42:34

name as Grog underscore API underscore key and enter the secret value as this.

42:41

Whatever your secret value is.

42:43

Rest of the things you please ignore.

42:47

Okay.

42:48

Just go to console Grog, create API key, copy the API key and go back to secrets and just paste

42:55

it here.

42:56

That's it.

42:57

Straightfoam.

42:58

It's nice setup.

43:00

Rest I will come to the notebook execution.

43:03

But

43:04

I just want to make sure everybody is done until here.

43:07

So that this secret name and this secret is already saved here.

43:13

If you want to see, I think you can take a look at it.

43:16

This is that complete GROC API key.

43:19

So all I did, you can ignore the rest of the API keys.

43:22

You can forget about that.

43:23

That is my personal keys and all.

43:24

You can forget it.

43:25

But this one is the one I created through Brock.

43:27

So GROC,

43:28

the API you'll see.

43:29

Please come and paste that value here

43:31

and please give the name exactly as what I'm showing.

43:33

what I'm showing. So this is the end result of what we are trying to actually. This will hardly take 10 seconds.

43:38

So once people are done, please give me a quick final confirmation on chat.

43:46

Okay? Yeah, please do let me know because this will be a very important step for

43:52

not only module 3 but all module 4. So we want to make sure everybody is set up with crop.

43:57

Okay. We will just pause and myself and Katak can help whoever is done.

44:03

So please do let us know if you're all done until you're okay.

44:11

Take it.

44:12

Ayush, okay, thank you.

44:14

Others.

44:17

Just one small thing.

44:19

API key, you must, after you create, click on create,

44:23

ah, no, that's okay, that's okay.

44:26

All the keys will not be visible.

44:28

You don't have to worry.

44:29

See, initially when you open up your full app,

44:32

so, uh,

44:33

All the keys will not come, you know.

44:38

All the keys will not work.

44:40

That is okay.

44:41

You just have to add your own secret.

44:42

These are all my personal keys.

44:44

So you can think of it like Naranjana is Slack username password.

44:48

You don't have these other things created which is okay.

44:51

That is not required for you.

44:52

You only have to create GROC API.

44:54

Right? These are my personal keys.

44:57

You just have to click on add secret.

44:59

You have to add new secret

45:00

and you just have to add this secret.

45:02

These are my keys. You don't have to create.

45:03

to create the rest okay and this is a permanent thing after we set up

45:08

this is permanently stored in your Google account next time you open up

45:12

collapse it'll it will be there for lifetime as long as Google stays as a company

45:16

which I think it will be for the next 50 years okay it's okay everybody

45:22

okay wonderful thank you Niranjana Ananya Harbri Puma has done

45:26

a Yush has done five of five people have responded others others others

45:33

I will just pause for others.

45:36

So how about you?

45:38

Okay, do we?

45:43

Okay, do we, okay, okay, okay, keep.

45:48

Repeat steps up to creating API key, okay,

45:50

okay, no problem.

45:51

Handika, make sure after you create the API key,

45:53

you've copied it on the clipboard.

45:55

Because what is, I'll show it to you.

45:57

I'll show it to you.

45:58

Some of you might be doing it this way.

46:00

Some of you might be doing it this way and you hit submit.

46:02

You will hit submit.

46:03

You must make sure that you copy from here.

46:05

Like you create this is taking a while.

46:09

Just make sure you copy like this.

46:12

If you missed the copy here,

46:14

then you'll back from here.

46:16

Here from here, just to clarify.

46:18

This is usually a question people tend to ask.

46:22

It's usually a question people tend to ask, so you cannot copy from here.

46:25

So if that comes, what you have to do?

46:27

Just delete it and create it again.

46:29

Make sure you copy from that window.

46:31

Then you come back to the collab node.

46:32

to the collab notebook that you already have opened during the click on the secrets icon can you see secrets click on

46:38

the secrets click on and after you click on the secret cycle the name you will have to click on add new secret

46:46

you have to click on add new secret yes if i just maybe uh okay i hope you're okay with me

46:54

yeah so comfortable so uh collab maybe it will be maybe it will be easy if i'm

47:02

walk the steps like this okay go to pull uh click the key like ikel

47:11

secrets okay now add new secret okay

47:16

okay add new secret okay secret name secret name what

47:21

okay secret name will be grok underscore api underscore key

47:25

it's simple and uh secret value

47:29

here whatever your groc value is thinking whatever your rock API Cisco page that's it

47:37

this is this is what you will have to do right stick just wanted to list it out for every

47:42

done simple here okay good i'm just just going to wait for others just for another

47:51

minute or so practical is a big part of today's class we want to really make sure people are able to do the

47:58

ideas yeah so there is some amount of coverage that we have but majorly it is a very hands-on

48:03

session today so we want to drive these hands-on session uh second session also this week

48:09

is similar to this we will get deeper into APIs we'll get deeper into jason so it's a very

48:13

hands-on week that we have and nika where are you struggling what what is the doubt you have

48:19

can you list it out on chat can you just let us know on chat or you can ping a screenshot i think

48:26

you have an option to like post a screenshot or something on the chat or you can just

48:32

let me know where you're struggling and i can help you

48:35

and i can help you and uh and how about the rest of the people

48:51

can i get a confirmation from others

48:56

people who have not responded already okay good thing is done and others

49:04

that's okay people have already responded it's fine i'm not asking yeah just just the ones who

49:09

have not responded yet just want to make sure everybody is done

49:12

even if one person is left out i want to stay back for him so just want to make sure everybody's

49:17

done all good is it fine guys

49:26

shiva thank you and uh yeah question for arnica again like if you yeah i mean

49:32

yeah i mean uh uh sure yeah i don't mind yeah yeah if you can speak yeah we can we can talk no

49:51

so yeah i mean whatever is comfortable if you want to post on chat is okay if you want to talk it's okay

49:56

whichever way you're comfortable me please yeah i can hear you go on please

50:04

hello okay look okay

50:26

good to hear another voice everybody should try to come to the sessions once in a while

50:37

and just talk ask your question we can we can do these kinds of interactions once in a while

50:41

it's good i think it makes it interactive i know the classes generally are scheduled in a way where

50:47

i would say like in a webinar mode we don't usually allow permissions but if you have uh some general

50:55

questions like uh i think this is good this is good it's good to hear another you know

51:01

like the interactive way yeah okay uh yeah arnica i think we cannot hear you like you want to

51:09

is there anybody else pending pratham i think everybody has responded done right i think

51:17

few people may not have i think um oh you're done okay that's good that's good that's good

51:23

okay okay very nice okay okay okay okay okay okay okay

51:39

okay so um i think we are it's fine prath up i think maybe we can separately follow up with the

51:53

people who are not done i guess uh branchill has not responded you can check one by one

51:59

maybe you can just make one vatica that the vittica already yeah so people uh let me know let us know

52:06

know if you have not done uh just ping us uh me or Pratap separately we'll help you

52:11

okay the rest we are to carry on with the class okay uh but yeah the furringtar also i did not

52:17

hear chandani i've not heard from you guys so how about you guys what are you going to do you need

52:22

some help please let me know but otherwise i think mostly everybody has responded

52:27

here and also uh yeah okay do let me know okay i'll be here here for

52:36

you let's continue on for the ones who are done done okay thank you thank you yeah just

52:43

let's just make setting two or three of you who are not responded so we'll reach out to you again

52:47

if you still stuck please let us go please let me or breath out go okay now let's continue on

52:54

next thing you will have to do just the setup just to make sure everything is set up everything is good

52:58

to go right just to make sure that the uh the setup is good

53:03

is good oh this is actually on uh okay just give me one second

53:11

it's actually done with the opening i don't worry don't worry about this i just

53:33

Thank you.

54:03

I will just change one small thing in the code to make it aligned with Grog.

54:12

Right now I think I just saw it as done with respect to opening.

54:15

I don't worry, it is a very minor thing I will change, but don't worry about it guys.

54:18

So what we then fuse the others.

54:21

I will just make that modification and then I will update you, okay?

54:25

Just give me a second.

54:33

Thank you.

55:03

Thank you.

55:33

Thank you.

56:03

Thank you.

56:33

Thank you.

57:03

okay there's just a small

57:15

all good all good here and all good here and all that you will have to do now is uh you will just have to

57:19

do now is uh you will just have to quickly refresh the uh the drive link again so we are in 22nd june here

57:28

and so it's just a couple of modifications i did the file so all you do is all you do is

57:33

it's okay everything else you've done is already saved against your google account nothing

57:37

changes all that you will have to do right now is just go up to your uh just close whatever notebook

57:47

you have opened right now please hit a close go back to the google drive hit a refresh refresh refresh

57:55

so the file gets refreshed and just open up the glass notes file again simple simple okay just

58:03

just open up that class notes file a little that's simple rest all the story remains the

58:08

same you can click on your secrets and you can still see that whatever secret you added that remains

58:13

nothing changes all that you can do is you're just accessing a different notebook file a

58:18

so everybody please do that i repeat close whatever ipyynb you have refresh your google drive

58:25

and you can just open up whatever class notes the fresh glass notes which i've uploaded right

58:30

that's it okay this is how the setup will look like

58:33

okay after that the last thing that we will be doing the last thing that we will do is

58:39

just start the execution from here and i just want to make sure you're able to execute the code

58:45

don't worry about this code i will explain this to you so this is the first cell that you will

58:50

have to execute this is the first cell we are executing you can see this simple execution we are

58:58

doing this is the first cell we are executing

59:03

this is the way you execute a set in collab we have already seen this before after a while a tick

59:08

mark will come this is the first see can take a look at it and once you get once you get

59:31

once you do this you will see the this will execute successfully okay your secret

59:37

bina this will execute successfully run the next cell execute successfully this is the prom

59:44

structure whatever theory we talked about system user assistant let's explain this in a moment

59:49

system message user message and run this cell and see this response this is the end result

59:55

of the small hands on exercise we are trying to do the setup we are trying to do at the end of this

59:59

exercise you should be able to run this entire cell until here and see the output is coming

1:0:05

like this guys this is the same story we were discussing on uh wetness test session if you remember

1:0:10

this was that beautiful uh medical notes assistant we were trying to discuss right so imagine a doctor

1:0:16

will enter some medical notes and the language model will try to extract information out of it

1:0:21

so from that unstructured text data how do you read that unstructured text data and how you extract

1:0:26

contents out of it in a structured manner though i will give this particular thing as a system

1:0:31

message where you're describing the language model what to do what the language model has to do we are

1:0:36

clearly explicitly stating that okay you will be given medical loads and from that please extract

1:0:41

what is the age what is the gender what is the diagnosis what is the weight and what is the smoking so from

1:0:47

the medical notes you please extract all this information and this is the part where we are entering the

1:0:51

medical notes as input so the medical notes are entered as input here and based on that we are getting this

1:0:56

response okay so i will explain the rest of the code to you do not worry i will come back to that

1:1:01

conversation but this is a very simple way how we are programmatically doing exactly what we did

1:1:07

you know like in a very high level on witness test session so we are simply programmatically doing it

1:1:12

so system message up now string go yeah what were we doing in in in uh you know uh in in in in in in a

1:1:20

witness test session we were doing it this way we were using grok we were choosing the language

1:1:26

model 70 billion versatite you have my system message

1:1:29

here and this was my user message this is remember this is how we were doing on

1:1:33

Wednesday day right so this was my user message we have already seen this story in the last

1:1:37

session system message you're defining what the language model should do all the

1:1:41

you know aspects should be covered here you should tell what the model can do what it cannot

1:1:46

do what are the different safety aspects all that you have to specify here there is another very

1:1:51

important term that we use called guard rage like when certain types of questions are answered how will the

1:1:56

the model respond so all those things be part of your system message and medical notes will be the

1:2:02

user message this is the part when you're entering the user email so this is going to be the you know

1:2:07

the the the user message you can take a little bit okay everybody is able to uh

1:2:13

everybody is able to observe this is the user message now what is the corresponding code for this

1:2:18

this was the normal way we did it last session if you click on view code in grop this is exactly

1:2:23

what we wrote in the class today okay you can ignore this

1:2:26

the other things but this one template from grop import grok and what is grog exactly

1:2:33

grok is basically a provider of language models so grok is a place where all these language models are

1:2:39

posted because all these models are very big they require a lot of memory and computation to store

1:2:44

so we cannot download them in our own systems we cannot we don't our systems our laptops are not that

1:2:49

powerful just to give you some understanding a 70 billion parameter model it takes like a lot of gb

1:2:55

lot of gbs of space this model will take several hundreds of gigabytes of space we don't have

1:3:01

that much of gb of ram in our system so our machines are not capable of hosting these models

1:3:06

so that is why there are providers like grok these are infrastructure providers these providers

1:3:12

are hosting the models you can think of grog as one massive computer as an analogy you can think of grok as

1:3:19

one massive computer so grok is basically this massive computing infrastructure where also

1:3:25

these models are hosted we have the lama model we have the the the the lama model posted we have another

1:3:32

model posted we have another model posted so grog is basically that particular uh you know a very very

1:3:38

powerful super computer kind of thing it's a very powerful super computer kind of thing where all these

1:3:43

individual models are posted m1 m2 m3 m4 f5 are posted and what are we trying to do so grog

1:3:49

they have these all models it has enough ram it has a lot of ram imagine that this grok

1:3:55

computer has a tremendous amount of ram tremendous amount of processor and inside it all these

1:4:00

models are stored here there are stored and what are we trying to do we are trying to access these

1:4:06

models through an API that is what we are trying to do so programmatically we are trying to access

1:4:12

these models using an API so we are importing grok we are instantiating client equal to crop we are giving the

1:4:18

API key. API key, what kind of password? See, Grog is having these models, right,

1:4:24

but, but you need to access it, right? So whenever you are trying to access an external resource,

1:4:31

you require some kind of an API key. That is exactly what that API key basically stands for. It's a

1:4:37

kind of a password. See, let's say you want to go to facebook.com. A facebook.com to

1:4:41

like you have to log in with your user ID password. So think of it this way. Right? So you want to go to

1:4:47

to GROC, you want to access the Lama 70 billion parameter model from GROC and get a response.

1:4:54

See, in order to access that 70 billion parameter model from Grog, you will have to go and give an API

1:4:59

key to get access to that model. So that is basically what this entire thing is all about.

1:5:04

Okay? So you write the prompt, you write the prompt, whatever prompt we have got,

1:5:09

system message, user message, whatever story we talked about, we write the prompt, we give an API key,

1:5:15

we get access to GROP and here.

1:5:17

here we get a response back. So there are two important terminologies we are writing.

1:5:22

One is a prompt that you're giving as input. The GROC engine will do all the processing.

1:5:27

All the processing will happen in the GROC supercomputers, which we don't have to worry about. And we will

1:5:32

simply get the response back. And all that magic is happening in this piece of code.

1:5:36

Client chat completions create. This is the code. You just have to remember it. You just give the name

1:5:41

of the model. And messages make your entire template. This is basically the prompt.

1:5:47

Next time we talk about a prompt. The prompt is remember, role system system message and

1:5:51

role user user message. This combination is called the prompt. Okay. Pronged go

1:5:56

and temperature we will discuss in the next part of the session, what it is. Okay, we will come to

1:6:00

that later. So this is the most important part. Client chat completions create and you're getting

1:6:04

the completion. Okay. So this is what is going on. I think most importantly, this story is very,

1:6:09

very, very important. So first of all, what is this GROC? GROC is like a very, very powerful super

1:6:14

computer. You can think of it like a server. A lot of resource.

1:6:17

sources, lot of computation is available. And Grog is responsible for storing all these

1:6:22

models. M1, M2, M3, M4. All these are stored in Grog. Right? What are we doing? We are writing

1:6:29

a prompt. This is the prompt we have written system and user message. We use an API key.

1:6:35

API key is like a password. You use that password to access the models in Grog and you get a response.

1:6:41

Okay. So this is basically what is going on and programmatically, that's the same story we are talking about here.

1:6:47

Our notebook code take okay. Same thing we have done. We have basically copied the code

1:6:51

from there only. Grog equal to this client equal to Grog. So please instantiate the Grog client.

1:6:58

Set the API key from Collap. This is the way you're trying to take whatever secrets you created.

1:7:03

See, whatever Grog API key secret we created, we are using user data. Get. When I do that,

1:7:09

I'm basically getting the value of that secret. And whatever that is, you're assigning the API key.

1:7:15

So this particular code is where we are assigning the API key in GROC.

1:7:20

Okay, client equal to GROC is what we are doing.

1:7:22

You keep the name of your model, Lama, 70 billion, versatile, whatever model we used here.

1:7:27

And finally here, this is the story we talked about. System message, user message. This is the

1:7:32

triple quotes in Python, multi-line streak. And finally, client chat completions create.

1:7:37

Name of the model and prompt. You get a response. So you write the prompt and you get a response.

1:7:42

So this response is what we are able to see right.

1:7:45

Okay, so for the first time in our class, we have managed to do an API call

1:7:49

successfully using GROC.

1:7:52

Now you'll ask you, sir, GROC, a supercomputer, he's,

1:7:55

he has this memory, it's this computer, it's this costly

1:7:58

we are able to do it for free with a simple Google account, right?

1:8:02

That's also a very interesting thing. Remember, nothing comes for free in today's world.

1:8:07

AI compute is very, very costly, infrastructure is extremely costly.

1:8:11

See, even Grog is going to give you a lot of limits. The Lama,

1:8:15

model that we are using, these are the limits that are available right here.

1:8:18

So there are, so we will talk about some of these things today, also part of our coverage,

1:8:22

tokens, what are these things, we'll come to that. But you can see, uh, tokens, you can imagine

1:8:26

them as words as an example. So this is your limit. In a minute, you can only have 12,000 words,

1:8:32

maximum input, output, will again. In a day, only 1,000 requests can be made. In a minute, only 30

1:8:37

requests can be made. These are limits. So this is not indefinite.

1:8:41

Uh, infinitely used nike. Yes, rock is one of the only few providers.

1:8:45

which are giving for free rest all the providers you have to give some dollar top-ups and then

1:8:49

do it okay so i want to make sure the objective of the session right now from the last hands-on

1:8:55

we did like a while back you all set up the things i want to make sure everybody is able to run the

1:9:01

code until here so that you're able to see exactly the same answers if you have done any of the parts

1:9:08

incorrectly in the previous step you have error and make sure you run all the sales in order

1:9:13

that means to execute so please execute this cell

1:9:16

then then next cell and make sure that you're getting this answer in age 35

1:9:21

just ensure the information extraction is happening correctly the only difference is

1:9:25

are able to do this programmatically in the class today last session we were just you know

1:9:28

using the dashboard we were kind of getting submit and we were seeing the story here the same

1:9:33

story we are able to do it programmatically right now because this is what we want to do as developers

1:9:37

as developers i don't want to you know use this kind of an interface as developers i want to do the exact same

1:9:42

thing in a program you want to use python to do the same thing

1:9:46

which is exactly what we are getting okay i hope you can draw the connect with what we did on

1:9:51

witness day session okay people are able to do it until here please give me a confirmation

1:9:55

if a green tick mark is coming at the end of this particular say i will i will i will

1:10:00

will i will pause for a while about okay

1:10:12

be no guys and remember this is the updated class notes file okay so just make

1:10:20

sure you're executing are using the updated class notes file okay thank you shake okay others all good

1:10:33

okay okay thank you

1:10:37

we've got two responses so far just going to wait for the rest of you okay thank you or nika good thank you shima thank you shiva thank you iroh others

1:10:57

thank you a bit six of you responded that's good the first time the first time you actually called a language model

1:11:07

programmatically that's a take-out all this point we were just thinking

1:11:11

the language model what is the llm all that theory we've seen first time today we have

1:11:16

programmatically called the language model using a prompt we are writing a prompt we are

1:11:20

using an API we are accessing a language model all this while we have heard they are

1:11:24

massive models too many parameters oversized but today we are able to actually access

1:11:28

that programmatically and you're able to see the results okay others please let me know

1:11:37

we will wait a minute no problem we'll pause for a minute

1:12:07

okay thank you thank you thank you thank you good i'm just trying to ensure everybody is able to do it okay that's

1:12:37

i'm waiting just want to make sure everybody's uh you know talk to go okay thank you

1:12:46

thank you medical very nice very nice to see everyone same little like good good uh still some people

1:12:52

are respond left out uh there's sad how what you

1:13:00

experience experience some error prasad what is the error would you like to state most likely

1:13:05

API error is it a API error or make sure Prasat make sure that you're

1:13:13

running the cells in the same order and also can you confirm Prasad that it says Grog API key

1:13:19

or then do you see a different API what what what what what I just want to make sure you

1:13:24

you're accessing the same file that I'm using

1:13:28

Prasad can you confirm this is Grog API key or something else

1:13:33

Grog API key right okay very nice then that is

1:13:35

correct and Prasat can you also ensure all these cells are in the same order first you execute

1:13:40

this set then you execute this set most likely i have a sense maybe you might have you might have

1:13:46

missed this cell now check kharu yes and execute work in there is a cell here here this is very small

1:13:53

cell sometimes they get missed out make sure all these cells are executed and then you go and

1:14:00

execute these two cells and different okay total five cells you have to execute

1:14:05

And if you're still getting an error, Prasad, I would request you to just bring me the error message, okay?

1:14:11

How can I change the name to Grog Kvati? Hey, Gurtig, simple, just go here.

1:14:17

So how did you create the secret? But look like, uh, uh, ah, to change

1:14:21

not change. Yeah, yeah, you cannot change the key. He is very sensitive, right? You cannot change it.

1:14:27

Only option is up for delete. Uh huh, correct, correct, correct. Yes, there's no way to change it.

1:14:32

But I have a suggestion for you. I have a suggestion for you. What you can do.

1:14:35

You can unhide you can go back and you can go back and just copy the key.

1:14:42

This go copy the key.

1:14:44

Copy the key.

1:14:45

Then, add new secret.

1:14:46

Once say, give the name and just paste the value.

1:14:49

Okay, got it?

1:14:50

I think that will be a better way to do.

1:14:52

Let's a good point goes then.

1:14:54

You cannot change the key once you create it.

1:14:56

So just try it out.

1:14:58

And Prasad, just to, you know, just to quickly check with you also.

1:15:04

also if you are able to fix it.

1:15:09

And the rest of you, I think, as Prasap Pratav is also being like others, can you all confirm?

1:15:16

Anywhere, if you're stuck, you can please let us go.

1:15:21

Everyone is done, Chantani and system message not defined. Prasad, so clear it. You might have

1:15:28

missed this step.

1:15:30

This variable, right? You can execute not execute.

1:15:34

run. Also, if you can set your message to everyone, people can see your chat.

1:15:41

Others can also see what you're asking. So just change your chat settings to everyone.

1:15:47

But just to kind of clarify the fixed Prasat, this go.

1:15:49

Run. Please run this cell and please run the next cell.

1:15:55

Then you do this. And please confirm.

1:15:59

Okay. And others, how about Pranjel, Chantanthanii, Quarinter?

1:16:14

Okay, Pranjan. Okay, very nice. Good. Thank you for that.

1:16:17

Oh. Okay, good take is also now. Very nice. Very nice.

1:16:21

Very good. And, uh, no else. I think, uh, Sneva, have you all good with you? You

1:16:33

responded, too? I think you did not respond. So I wanted to check.

1:16:40

Sneh, how about it? Are you called up to it? Let us know. And Prasat, finally for you, like,

1:16:50

like, ah, it's done, good. Wonderful. And Prasar, I think if you're able to fix it,

1:16:55

please do let me know with a quick yes on chat that you fix it, okay? Yeah, it's working for you.

1:17:05

So, very nice. So people are all able to today, you're all able to, uh, good, excellent,

1:17:11

you're all able to call a language model today. So what is the story we discussed again? This entire thing

1:17:16

is like your prompt. This is the same thing we were doing, like in

1:17:20

the UI in the last session. I'm, we're manually doing on Wednesday day. And and everybody today

1:17:25

in the session, you are able to take that prompt. You are able to write that prompt. This

1:17:32

entire thing is like a prompt. Right? And you are able to use the GROC. But you are able to make a function

1:17:41

call. I'm just trying to give you analogy because everybody knows functions. It is like a function call

1:17:45

you're doing to GROC. GROC is this very powerful computer.

1:17:50

a lot of models which are stored in GROC, you are able to make that function called to GROC

1:17:55

and get a response back. And this is exactly what we are doing. Gline chat completions create. We are

1:18:01

sending the prompt and we are getting a response back. You have a response to R&. And this is the

1:18:07

thing that we are doing programmatically as developers. This is all that we will do for the remainder

1:18:12

of our course. Obviously the prompts will get more complicated and the applications will get more

1:18:18

complicated. But whenever we have to call a language model, this is the same story that we will be

1:18:23

following. Now, this can be something else. This may be Grog. This can be some other provider.

1:18:29

Now people often ask that, sir, this is GROC is not? GROC not, GROC not, which other provider

1:18:33

can. Absolutely. So GROC will host a certain type of models. If you go to GROC, you'll be able to

1:18:39

see these are these are all a certain class of models that GROC is hosting. So GROC is that very

1:18:44

powerful computer and GROC is hosting these models.

1:18:48

mostly they are open source models right and that's why they are giving it for free

1:18:52

a free may access can you right but the moment you go to some other platform let me give you that

1:19:00

that that particular demo also the moment you go to some other platform they say platform

1:19:05

open AI okay i will i will have the same story let me put the same story here as well let me put the

1:19:12

same story here so right now i'm in open AI platform

1:19:18

i'm using gpt 4.1 same story you're your system message here your user message is

1:19:25

same story nothing changes the only difference the only difference is that now we will be able to use

1:19:32

gpt models for your open aai platform so the so the reason i wanted to show this demo is because

1:19:39

this is the same application system message user message same application

1:19:43

but if you see the code you'll be surprised to see that the code remains

1:19:48

surprisingly very very simple. And this is one very important learning.

1:19:52

So whatever we do using the GROC, sessions we can use currently because that is something

1:19:58

everybody can access freely. But as you extend the conversation to other kinds of APIs,

1:20:04

they say some of you might want to access open AI models, some of you might want to access

1:20:08

anthropic models, some of you might might, you know, might want to access Gemini models, the interface

1:20:16

remains very very similar. Now, look, here we're open AI models access

1:20:20

are the only difference, and I repeat again, the only and only difference is you are saying client equal

1:20:26

to opening high. Here we're here I was saying client equal to croc. Can you see? I was saying client equal to

1:20:31

grok. And here I'm saying client equal to open AI. That is the only difference.

1:20:36

Bucky story same to save. Client chat completions create. Model equal to model name and message is

1:20:41

equal to this system system message, user user message. And you're getting the response back.

1:20:46

And this is the best part. And how is it different here? How is it different?

1:20:51

The only difference here is that you are taking this entire prompt. You are taking this entire prompt.

1:20:58

And now you are making a call to open AI's models.

1:21:05

So this is again that very powerful computer. It can be open AI, it can be grok. So now you realize what these things are.

1:21:12

These are basically servers. They're very, very powerful computers. So,

1:21:16

This is like the open AI platform, which is a very powerful computer. Think of it that way.

1:21:20

Ah, Azure be it can't. It's anything.

1:21:21

There can. Here on your cloud be. So in a way, in a way, if I have to give a more technical term,

1:21:30

these are called LLM providers. These are called LLM providers.

1:21:36

I'm could say to language model banning because it requires a lot of data, a lot of time to build

1:21:42

and train that language model from scratch. It is impossible to do it for.

1:21:46

a normal, you know, so there are many such providers which are hosting these language

1:21:51

models, right? These are the server providers. Like open AI is a provider. Open AI is a platform

1:21:57

a provider to. This chat gpti is not. Chat GPT is a different. But what I'm pinging right now to you

1:22:04

is actually an LNN provider. You write a firm, you access using an API key and you get a response. So

1:22:13

same story works on. Okay. So this is just one.

1:22:16

general concept I want to clarify. So the classes will happen on Brock, but that does not mean

1:22:20

it is, it is similar for other providers also. So here our platform, open AI and you have

1:22:25

any other model use can you. GPT 4.1, GPD 5.5. This is the latest of the models from open AI today,

1:22:30

GPD 5.5. But the story remains the same. The concept remains the same. Whatever concept

1:22:35

become, L&M, providers is the concept.

1:22:38

This is a platform, open AI. And another major enterprise which is in this space is cloud. And this is

1:22:45

Claude developer platform. This is cloud's developer platform. Which is very, very similar.

1:22:50

Here code a little bit, but very, very similar. Let us, let us take a look at the cloud platform.

1:22:58

Very, very similar. So how is it different? How is Anthropics platform different? Because it will

1:23:02

host only Anthropics models. Grok was hosting mostly open source models. Open AI was hosting

1:23:10

the GPD models, which is open AI's internal models. And Anthropic Claude,

1:23:15

Anthropic is hosting its own models. Like Claude Sonnet, Clod Opers. This is the company for Anthropic.

1:23:20

So after Open AI, Anthropic is the second most valuable company in the world today.

1:23:24

Like I think in the space of LLMs and language models, second most valuable startup in this big story.

1:23:31

And this is Anthropics developer platform. Story remains the same.

1:23:34

That is system message, that the user message. You have that code. You can see the code.

1:23:39

You can see the code. Where is the code? I think there's an option to find the code and get the code.

1:23:43

And you can take the code.

1:23:44

Here, there's a little bit, but here again, again,

1:23:47

the client equal to anthropic, API key, download. And you can just do, instead of client dot chat

1:23:52

completions create, here here client messages.

1:23:54

A little syntax change, but the idea remains the same across all the providers. So a key learning

1:23:59

from this session was, okay, whatever we saw in the last class, Pront, we know that.

1:24:04

Now that story, we are aware, you have a prompt you will give. You will give the name of your

1:24:09

model and you can call any LLA provider to get a response.

1:24:14

Okay, so that's the and what is the setup we have done in the class?

1:24:17

The setup we have done is with respect to Chrome.

1:24:21

Okay, I hope everybody is aligned with respect to what we did. And this is a small demo in terms

1:24:26

of what we discussed. Okay, I'm just trying to run a small dummy application. You don't have to,

1:24:29

you don't have to see this in detail, but this is just to kind of give you the big picture idea

1:24:33

of what we did in the last class. Okay, this is the small radio application I'm trying to create.

1:24:38

So all this while, what I was doing was I was programmatically showing you.

1:24:41

He, okay, system message here, user message here.

1:24:44

to answer as are that okay but in reality how will the application look like say when a when a

1:24:48

hospital is accessing that application how will the application and practice look like okay in practice

1:24:53

how will that application look like so that is exactly what this whole thing stands for okay so

1:24:58

so how will the application in practice look like so the application will be something that the

1:25:02

doctors will be using and this is exactly what they will be able to see this is exactly the

1:25:07

application that will run live in the hospital about doctor or the hospital assistant who is

1:25:14

who will be using the application.

1:25:16

They are users of the application.

1:25:18

They should not know what is the system message.

1:25:21

They should not even understand what is system message.

1:25:23

They are not supposed to know that.

1:25:24

System message is something that is supposed to be very, very sensitive.

1:25:27

It is supposed to be a very, very, you know, sensitive piece of information.

1:25:30

They are not supposed to know what is your system message.

1:25:32

But they will definitely know what, you know, they will definitely be able to enter the medical notes.

1:25:40

You have medical notes enter them.

1:25:42

And they will be able to get the response.

1:25:43

So the story remains very, very similar.

1:25:45

Okay, so you can see the big picture idea of how this application will work out.

1:25:49

So in the real world also, whenever you are building these applications,

1:25:52

system message will never be known.

1:25:54

This is the same story I was talking on Wednesday.

1:25:57

They say chat gptu-gpt is also a real application.

1:26:00

Chat-GPT what are you doing in stat GPD?

1:26:02

You're doing the same thing.

1:26:04

You are the end user.

1:26:04

You are only entering the user message.

1:26:06

You have your user message entered.

1:26:08

That's it.

1:26:08

Now, whatever you are entering, that is getting combined with the hidden system message.

1:26:13

the prompt. So user message, hidden system message is the prompt. And from that

1:26:19

you get the response when you hit enter. That is what is going on. Right. The same thing here also.

1:26:24

User is entering the user message. This is getting combined with the hidden system message.

1:26:30

Application company system message. Although system message, what we have defined. This is what we

1:26:35

have defined. So that whatever the doctors are typing, their user input is getting combined with

1:26:41

the system message of the application and based on that the response is

1:26:46

basically given up. So this is the way how you're able to see this. And in a real world scenario,

1:26:51

in a real world scenario, what happens is this output of one application usually becomes an input

1:26:56

to another application. So whatever this application is outputting, it is not just for seeing,

1:27:00

it's not just for display. Usually what happens is a great use case that we see that are

1:27:05

happening today. Like as we work with enterprises today is how you are able to tap into this

1:27:11

humongous amount of unstructured data, like text data, and how you're able to extract structured

1:27:17

information on. Here, classic use case. You're able to connect to that humongous amount of unstructured

1:27:22

data, whatever unstructured data you have, you have some text data with you. And from that text data,

1:27:28

you are trying to extract the information out of that particular text data. So that's the use case

1:27:32

with here. And then eventually you're able to save it back into a database.

1:27:37

Yeah, too, you can save it back in an Excel file or a CSV file, or you can save it back in a database.

1:27:41

You can save it back in a DB as well. Okay. You can hope this is absolutely clear.

1:27:46

All of you are absolutely aligned on this one. Maybe you can run this one. You can, you guys

1:27:51

can maybe take a moment and try this out. This is my radio. You're not able to run this code. The only

1:27:56

objective was I wanted to, wanted you to ensure the setup is ready. Now that the setup is ready,

1:28:01

but you can just use my gridio URL. Okay. And what is Gradio? We have this machine learning.

1:28:09

briefly it is just used for some small sample demos. Okay, machine learning also what happens is,

1:28:14

you know, we take the data, we build a model. You can, all this is in a Jupiter notebook, right? But how do you

1:28:19

demo that to end users? End users? End users who kind of what your application is doing. You go back

1:28:25

to all the use cases made it in regression, classification. How will end users for what your application is

1:28:29

really doing? So this is a nice way to build up a small demo of your application. You take it outside of that

1:28:38

that Jupiter environment and you create a small working URL or a link that you can share with your

1:28:44

managers with your clients to show them, hey, this is what I make it. So demo,

1:28:48

our very simple time. We have a system message, user message, we have a language model

1:28:53

called here, but we can't this client can't show you to the client. If I have to show something

1:29:01

to the client, we call it a POC, approve of concept. So we will go back and, you know, share a gradio you

1:29:07

want it. The same way I'm sharing with you.

1:29:08

I will share this link with the client and ask the client, hey, clients, these test my application.

1:29:12

So I've done it. This is the thing that we did.

1:29:17

Okay, I hope everybody is with me. Everybody is aligned on this and this is the next one.

1:29:22

Again, we are programmatically doing this. You can see user input. This is for another user.

1:29:27

And same way, same way, we are getting the response and here is the response I'm actually getting.

1:29:32

This is for another person. This is for Mr. Prishnaveni. Same system message, but I'm giving a different

1:29:38

user input. So when this particular user input is given, this is the information that is expected

1:29:43

of. Okay. Let us look at one more example. Information summer meeting summarization. We did this

1:29:48

use case last session also. I'm quickly taking it through it right now. So system message,

1:29:52

this is the system message. And you can see system message. We have clearly defined how the summarization

1:29:57

has to be done. And this is your user input. User input will contain the entire meeting transcript.

1:30:01

Let's say this is a two-hour session that we are doing in Zoom. So the complete transcript of this

1:30:06

two-hour session will be caught up my user info. We can another. We can another.

1:30:08

the basis of that i will get the uh the application response and you can take a look at it you can take a look at the

1:30:15

response whatever response i'm getting and this is that final summary summary response i'm getting

1:30:20

so meeting documentation and this is the whole summary of that meeting exactly the way you asked him

1:30:26

and this is actually very detailed because in the system message i'm clearly stating how i want a

1:30:30

summarization to be done you could have given a generic system list you could have asked okay please summarize

1:30:34

the meeting like this and all they can look you could have given a more generic

1:30:38

system message we are not doing that we're not giving a generic system message but we're

1:30:42

giving a very specific system message like one very serious so we're not giving a

1:30:47

generic system message we're giving a very specific system message that from this

1:30:50

transcript please extract this please extract this please extract this and based on that i

1:30:54

want you to do with a summary so that is how you're how you're stating this so this is that meeting

1:30:59

summarization uh you know use case that you're able to see again as i told you

1:31:07

these applications you can do this on gradio i'm again going to create a gradio you

1:31:12

are so that people can demo this application and you can again see this in practice

1:31:17

so this is how the application will look live if you're building it yourself so in the

1:31:21

back end we have done this tool we have used our system message we have you know used our

1:31:26

user message to demo this thing but this is how it will look like in the front name you can keep

1:31:31

any meeting transcript or our case in meeting transcript let's say it will be this user message

1:31:35

this is your user message is let me just give that entire user message

1:31:39

of transcript you're your user message okay so based on the user message i will enter

1:31:44

here we enter and we'll enter and we're two ways of

1:31:48

one could be that you you you know you manually enter the transcript the other use case

1:31:52

would be that this is entered or this is automatically coming from soon just as

1:31:58

zoom in what happens is whenever whatever i'm speaking or whatever anybody is speaking

1:32:02

it automatically gets transcribed the speech is automatically

1:32:05

converted to text so so this will automatically come from zone

1:32:14

soon there's an application that is already built in which will take this entire

1:32:18

meeting transcript and let's say if somebody presses the submit button

1:32:23

that summarization would say this is a nice POC or a proof of concept of what we

1:32:27

achieved here okay so this is basically what's going so system is not

1:32:32

showing up right now but that is all going on behind the scenes so

1:32:35

this is a small meeting summarizer application so you can enter your user message your user

1:32:40

input is getting combined with a hidden system message prompt and based on that prompt

1:32:48

you're uh you're you're you're making a llm call and you're getting a response

1:32:54

so this is what's going on behind this is where are you getting the output can you can you confirm

1:32:59

which place are you getting the outcome where are you getting the outcome where are you getting the output

1:33:05

in gradio okay but in gridio which which which part of gradio you're getting the output

1:33:13

can you tell me okay gradio first install have you installed gradio i think

1:33:17

pip install is there any gridio i think is already pre-instoned

1:33:21

okay gradio to chaly but ayush you need to tell me what is the error you're getting then i can

1:33:26

clarify is it is it in the first one the medical notes only are getting error or how's

1:33:35

okay so first in which grade you are getting the error and second is what is the error

1:33:41

you're getting just post that error message on chat i'll help you okay yeah that's the first one

1:33:45

okay so make our think of what is the error message you're getting

1:33:56

and i wanted to also also just clarify one small thing for everybody okay because this this

1:34:00

might be a mistake against i'm not saying this is the case but i'm saying it might be a mistake you might be a

1:34:04

a mistake you might be making they go here here this is system message and uh this is

1:34:07

system message here so just remember the same system message is getting reused in multiple

1:34:13

places so it is a variable name right so here here here umne put system message used here

1:34:18

and if you come all the way to the meeting note summarizer it's a different application but

1:34:23

here also i'm calling it the same variable system message so i'm just saying this could be a

1:34:27

possibility that you're running the previous cell or

1:34:30

back say you're executing this cell so that system message is getting overridden

1:34:34

so just make sure that if you're running radio you are running the cells in the same order

1:34:39

so you're you're need to execute then you come back at top you will get error that is just one

1:34:44

thing i want to clarify because the system message might be getting overwritten

1:34:48

that i know so i think that could be one of the reasons i wish okay now you

1:34:52

once check and uh since you already confirmed to me that you're here

1:34:56

where it is absolutely running fine until here one

1:35:00

first start for run all the cells in the beginning until here and then run the next cell i am

1:35:06

pretty sure you run k right okay most likely that's that's my hunch

1:35:11

okay okay okay okay let's move on so we have talked about the concept of the

1:35:19

the APIs and what it is now we will get a little deeper into a few prompt

1:35:23

parameters so all this wine what we've

1:35:26

we are doing we are basically just writing a prompt and in a way whatever we have done in

1:35:34

these last two demos we were writing zero short prompt okay zero shot prompt and they

1:35:38

write here only the prompt is given there are no specific examples i'm giving we talked about

1:35:45

zero short few short chain of thought last session so remember in zero short prompting there is no

1:35:49

additional information or no additional examples you give to the red net so this was a simple

1:35:54

application of zero shot prompting that we did you write the user message and you get a response

1:35:59

now what other prompt parameters do we have there are many prompt parameters out of which

1:36:04

there are two very very important parameters that we will talk about in the session today

1:36:09

one we have got something called maximum tokens so the parameter maximum tokens

1:36:15

refers to the maximum number of tokens that can be generated in the chat completion

1:36:19

and you're very important guys because if you don't limit the response of the large

1:36:26

language model if you limit not limit these models are very costly right they are very costly

1:36:34

so it is very important to limit the output and see what again just to kind of reiterate this entire

1:36:43

conversation goes back to tokens right so first of all what is a token of token have token what do you mean by a

1:36:48

a token is the smallest individual unit of a text so everything starts from here

1:36:57

basically what a token is a token is the smallest individual element of a text this is how

1:37:04

this is how language models are processing your prompts are proud to make those question

1:37:09

but it is not actually seeing that entire sentence or it is not seeing that entire question the way

1:37:15

you're asking it is not seeing that entire sentence it is not seeing that entire sentence

1:37:18

sentence or it is not seeing that entire question the way you're asking it is converting

1:37:24

that entire sentence or everything into the list of cookage and think of it this way

1:37:35

the most basic definition of a token could be like a word that's the most common thing but it

1:37:39

may not be like like for example uh i think this this this example is taken up very nicely

1:37:48

Un believable. Now I'll talk about Tokenization go

1:37:51

but again that is generally not in the scope but if I have to explain in a very brief way.

1:37:56

If I have the word unbelievable, I'm sorry, unbelievable.

1:38:07

Think about it. In the English language, this is one word.

1:38:10

This is one word, right? But what if I tell you that in the world of tokenization, if you're

1:38:17

you're trying to break it into tokens here three tokens in english it is only one word but in

1:38:22

tokens it is actually three tokens now it is a it is a internal concept

1:38:29

L&M's different language models will do tokenization in different ways

1:38:32

but these are the smallest individual elements of a text.

1:38:36

Motl here here tokens are an on a token

1:38:39

will believe a token will be able to

1:38:47

And you know, it's very interesting.

1:38:52

The reason because you can reuse these tokens in different contexts.

1:38:58

Now you are both un and able are different.

1:39:01

You know, it's between you're both of them.

1:39:05

Unmistakable.

1:39:07

Unimpeachable.

1:39:11

Un believable.

1:39:14

And what is?

1:39:17

And what is?

1:39:17

Unable, anything else? Can, two, three more examples.

1:39:25

Unable are so many words in English language you can see it.

1:39:29

Unthinkable. Think a token.

1:39:32

What are?

1:39:33

Unor able to have.

1:39:34

Beechp.

1:39:35

Think down.

1:39:36

See the idea?

1:39:37

So tokens are reusable.

1:39:38

We're machine.

1:39:39

We're making.

1:39:40

We're not doing.

1:39:41

We are not doing it.

1:39:42

We are not doing it.

1:39:43

Machine is doing it.

1:39:44

My responsibility was to explain to you the concept.

1:39:47

what is the intuition? But rest is they are doing internally.

1:39:50

We just have to know the concept.

1:39:52

We'll use one.

1:39:53

Unable.

1:39:54

Two token set.

1:39:55

And in the bidspey have some token down.

1:39:57

So any.

1:40:03

Unimaginable.

1:40:04

And unimaginable.

1:40:06

And unimaginable.

1:40:08

And what are?

1:40:09

Two more examples with un or even.

1:40:11

Okay.

1:40:14

I'm also, I'm also.

1:40:16

Unachievable.

1:40:17

One example.

1:40:19

Unachieved.

1:40:20

Yes, good.

1:40:21

There are three tokens.

1:40:23

There are achieved, able then.

1:40:25

One more example.

1:40:26

We have not covered.

1:40:28

One other quote else.

1:40:29

Come on.

1:40:34

Unavailable.

1:40:37

Unitable?

1:40:39

Unitable.

1:40:41

Is it a correct word?

1:40:43

I'm not 100% sure.

1:40:45

But.

1:40:46

Inedible.

1:40:47

It is un-eatable.

1:40:48

I think the right English word is inedible.

1:40:51

But that's okay.

1:40:52

There's more on the ones of the English.

1:40:54

So inedible, can't.

1:40:55

Unedible not.

1:40:56

But, yeah, unavailable is a good one.

1:40:58

Sure.

1:40:59

Very nice.

1:41:02

So, undoable.

1:41:03

It's absolutely.

1:41:05

So tokens are basically the smallest individual element of a text.

1:41:09

This is what you have to remember.

1:41:10

They may not be worked, but for the rest of our conversation.

1:41:15

And for pretty much.

1:41:16

us the rest of our modules.

1:41:18

Generally, we will assume token as words.

1:41:21

Generally.

1:41:22

This discussion was to tell you that tokens may not be words,

1:41:25

but just remember for our discussion for simplicity,

1:41:29

we will assume that one token is one known.

1:41:32

Yeah, how make assumption correctly.

1:41:34

Just keep this at the back of your mind.

1:41:36

But they may not.

1:41:39

Now, moving on, there are ways to count tokens.

1:41:45

This point.

1:41:46

what is very important, there are ways to count tokens.

1:41:48

And why is it an important idea to count tokens?

1:41:51

Why is it important?

1:41:53

So why is this, why is it important to count the tokens?

1:41:59

Because, see, there are two types of tokens, right?

1:42:07

What you're giving as input, a prompt, you're giving a prompt as input, right?

1:42:12

And remember what does the prompt consist of?

1:42:15

The prompt consists of system message, user message, that is your prompt, and you get a response.

1:42:21

So you're basically having two types of tokens.

1:42:24

One is the input token, one is the output token.

1:42:27

So one is the input token, whatever input token is going.

1:42:32

And the second is the output token.

1:42:35

This is the diagram I usually like to use to explain this.

1:42:38

So we have two different types of tokens that are coming here.

1:42:45

here, you can take a look at it. So the total token cost is like this.

1:42:50

Yeah, your request is nothing but the input, right? So this is nothing but the input prompt.

1:42:56

This is the prompt tokens. What, how, however big the input is, that is your prompt token.

1:43:01

System plus user combined. And this is the output response, the completion tokens, input output.

1:43:08

And it is very important to estimate the number of tokens here.

1:43:13

Prompt tokens, kiphton tokens.

1:43:15

because if your number of prompt tokens is large, if you have a large number of prompt tokens,

1:43:22

if you have a large number of prompt tokens, what will happen?

1:43:28

If you have a large number of input tokens, or if you have a large number of prompt tokens?

1:43:34

What will happen if you have a large number of prompt tokens?

1:43:36

That means, if the input is big, it will take a lot of time to process.

1:43:42

It will take a lot of compute to process.

1:43:44

process because I'm

1:43:46

doing it. We're prompt input

1:43:47

data. LNM is processing giving a response back.

1:43:50

That is what's going on. So if

1:43:52

your prompt tokens are large, if your system

1:43:54

and user message combined is very large,

1:43:56

if the number of words is very big,

1:43:58

if it's a massive prompt,

1:44:00

then be a huge cost.

1:44:02

Input where cost?

1:44:05

And if your response

1:44:06

is very big,

1:44:08

if whatever response

1:44:10

the language model is giving out, if the response

1:44:12

is very big, there'll be a completion token.

1:44:14

must and that is why it is very important to limit the number of too much

1:44:20

because if you don't limit i'll i'll give an example

1:44:23

imagine you're writing of font please write me a story

1:44:30

in infinite number of words i'm just saying like it will never have to know this

1:44:33

because of guardrails and safety parameters but what if you go to chat gpt and say

1:44:38

please write me a story in 20 000 punch it won't happen there will be safe cards actually

1:44:44

Because if you don't restrict the number of completion token,

1:44:47

you are having the language model generating a very massive amount of output.

1:44:53

This is the LLM in the middle. If you have a very big input, it will take a lot of money to process.

1:44:59

If you ask that NLM to generate a very big output, it will take a lot of money to process.

1:45:05

It will take a lot of money to process that. So both of these are very important

1:45:09

post the other account from input tokens output outputs, round token completion process.

1:45:14

Now you'll ask you, sir,

1:45:17

this cost is what is this cost? Let's talk about that.

1:45:24

Let's talk about that. Let's talk about them. And I will go straight to Open AI.

1:45:29

I will go straight to Open AI's pricing

1:45:32

parameters to give an idea. You don't have to memorize this. This is just for your knowledge purpose.

1:45:37

But just to give an idea to you, these are the current costs that you can see. Cache input is a different

1:45:44

thing you can ignore that for the time being update this is the uh gpt 5.2

1:45:49

monies update sat down input token cost is uh uh uh uh 1.75 dollar for million tokens all these are

1:45:57

basically in four million tokens or one million tokens you have been costing then that means for

1:46:04

one million words it is 1.75 now it looks small but one million words can get exhausted very fast

1:46:10

one million words definitely data not then and how

1:46:14

output is 14 dollars per million words output is always more costing look at gpt5.2

1:46:19

21 dollars per million tokens and this is 168 dollars per million tokens and some of

1:46:27

we might think he sir he can million tokens say this is like a lot billion words

1:46:30

where use or no well i'll tell you where use over like see so far we have just started our demos on

1:46:36

grog and very interestingly brok gives you a dashboard

1:46:39

now taskport to go now dashboard in taskport to go to usage but

1:46:44

users you go to use how much use these models you go to usage you go to

1:46:48

activity you go to usage and you go to uh activity and you go to uh activity and you here

1:46:52

here here check i think this is my activity here today look at the activity like i do a lot

1:46:59

of other okay and some trainings and maybe there was a training on this day i look out this is my

1:47:04

personal about so um our account say i was trying to use this many tokens this is in broad

1:47:10

100,000 are one user again. This is probably I've seen one week or two demos

1:47:14

Degov. You have my one week or June's users.

1:47:17

And this is these are very basic. This is not even production grade projects. This is very

1:47:21

basic demos I talked about. In fact you talk about today's demo.

1:47:24

All right. All right now.

1:47:26

Today, what I've seen. Simple. A medical nose extraction and one summarization. We have

1:47:31

already used up four and a half thousand tokens. Can you see input tokens, two and a half

1:47:34

thousand? Outputs one and seven thousand. Yes, everything is cracked. Everything is getting cracked.

1:47:40

Whenever you are, like, whatever API falls I made, everything is getting cracked.

1:47:45

If you go to the log section of GROC, today is 22nd June, right?

1:47:49

22nd June, in my Kya Kyaa Kyiya function falls clear.

1:47:51

You can see all the different parameters. That means when you made this particular call to the

1:47:58

grog model, how many input tokens you send and how many output tokens you got as output.

1:48:05

And also very interesting, there is another very interesting term for latency. What is latency?

1:48:10

Lentency stands for the time taken to complete the response.

1:48:13

Or this is important thing.

1:48:15

When you are building real applications, latency is also important.

1:48:18

See, it is like you go to Facebook.com.

1:48:20

You type the thing.

1:48:23

And it takes forever to respond.

1:48:25

So then the user experience will be bad, right?

1:48:27

Idea will be that we're going to type

1:48:30

and then that is what we expect.

1:48:32

But we don't expect.

1:48:33

But we don't expect we type something,

1:48:35

we hit enter and then it takes forever for the answer to come.

1:48:38

We don't want that.

1:48:39

We don't want that.

1:48:40

like that.

1:48:41

Latency should be as low as possible.

1:48:43

That takes a sector very interesting.

1:48:45

Sometimes the latency has been very low.

1:48:48

And sometimes the latency has been quite high.

1:48:51

And there can be multiple reasons for that.

1:48:53

There's not necessarily one reason.

1:48:56

But you can take a look at it.

1:48:57

The same number of tokens.

1:48:58

Here you see here.

1:48:59

Similar number of tokens.

1:49:01

Here here, latency is actually a little bit lower one.

1:49:03

Here latency is a lot more high.

1:49:05

Comparatively is 0.483.

1:49:07

But here the latency is almost 1 fourth.

1:49:09

you get a intuition on this.

1:49:11

So what I'm getting at is all of these things need to be considered.

1:49:15

It is not just that prompt here.

1:49:18

We have to write a good quality prompt.

1:49:20

Because the last class on Wednesday was more about time.

1:49:23

We were discussing how well you can write a problem.

1:49:25

Now zero shot for a few shot for examples.

1:49:28

If you can keep more examples, the model will do better.

1:49:30

We talked about all that story.

1:49:32

The same use case, I discussed the chain of thought.

1:49:35

We said, okay, if you can describe the instructions in a more detailed way, the model

1:49:39

we'll do even better. But hello guys, please remember, chain of thought comes at a post.

1:49:43

The moment you write a chain of thought wrong, it's very detailed.

1:49:47

Our input token barge. Processing post-verjaidantency be. Because of it not only is it

1:49:54

possibly to process both tokens, but it also takes time to process more profit. So now that

1:50:02

becomes a very fine and delicate balance of cost-benefit analysis. We call it cost-benefit analysis.

1:50:07

We're going to. No, it's no matter.

1:50:10

Okay, I'm willing to spend more, but am I really getting a benefit by writing a better prompt.

1:50:21

So things are the kind of conversations you have to make. Right?

1:50:26

That's a good question because Kourten, every time you're sending a new request.

1:50:30

When you're doing two client chat completions are, the other request is going to go.

1:50:34

If you have to use a more technical term, you have to be more technical term, you're going to say.

1:50:37

It's like an API caller. So every request is getting associated with a request ID.

1:50:42

Every time you do client dot chat completions. Create, take request ID generate. You're sending a request,

1:50:48

you're getting a response. So whenever you are running this code, this is the story goes thing, right?

1:50:53

Whenever you're running this code, client chat completions create, you are going to grow. You're making a request and you're getting a response.

1:51:00

Does it make sense? So that is what request ID basically stands from.

1:51:03

And the reason I wanted to show this to you is because I wanted to. I wanted to.

1:51:07

Help you appreciate that.

1:51:09

In real enterprises also, enterprises also want to see,

1:51:13

okay, how are my models, applications are calling the models? Where is it taking time?

1:51:18

Where is it taking time? Where there's a time? Why? Somebody will have been

1:51:22

investing in. Who? Who are you complaining? Why? Then somebody will investee here,

1:51:28

if there's, why, if we send, 7009 tokens? What percent as part of the 7009 token?

1:51:34

Here. Here, be similar token send you. Here, be similar token.

1:51:37

send you on. But here, it took more time. Why? These are the kind of questions you will

1:51:40

have to answer. Right? Make sense. I just wanted to show you this comparative view here.

1:51:46

So key learnings, we talked about latency and we talked about the costing part. Costing part is

1:51:51

very, very important. And what is the costliest model available? The costliest model. Just to give an

1:51:55

idea to you, the costliest model is from open AI, which is called the O1-4 model.

1:52:01

With unimaginable cost, that then, unimaginable cost. They go, see, sara.

1:52:07

Just to give an idea to you, 4.5,000, this, where did? 4.5,000 tokens majorly, approximately I'm talking about, right?

1:52:18

two, three more demo, so easily our 100,000 demos, 100,000 tokens will, right?

1:52:24

If I take the entire class as a whole, there are, like, 15 of you right now, 100,000 into 15.

1:52:30

100,000 into 15, now, if, just for 1.5 million, so we have already crossed a million tokens.

1:52:35

and like if for some reason we're not doing that but if for some reason we were using the gpt o1

1:52:40

flow model in a matter of one hour in the class they have so dollar card only are

1:52:46

just to give an idea to you how expensive these models can be this is 150 dollars per million

1:52:55

okay and all that it takes is you just have to go here and change

1:53:02

you have to go here and change you have to go here and change what and equal to

1:53:05

Model equal to O1 Pro.

1:53:07

O1 Pro, it'll go over.

1:53:09

But here not calling the Open AI API, but just to let you know.

1:53:13

But it's so easy to programmatically do these tools right well.

1:53:17

So very important aspect of the session was to talk about the pricing.

1:53:20

Please be aware of the pricing.

1:53:22

And it is very important to estimate your costs.

1:53:25

So writing a prompt is not just writing a good quality prompt,

1:53:29

but keeping account of the tokens.

1:53:31

It's not taking account of the tokens.

1:53:34

And that's, and that's.

1:53:35

one way to look at it.

1:53:36

What is the specific code that we use for it in case you're curious about it?

1:53:41

We use a specific thing called tokenizer.

1:53:44

So tick token is what we use.

1:53:46

So tick token is all of the ways how we basically program.

1:53:48

So tick to can use kirk and we're costing estimate person.

1:53:52

We can use the tick token package in Python.

1:53:55

You can, very simple, you can use a simple tick token package in Python.

1:53:59

And using the tick to get the tick token package in Python, you can estimate the number of

1:54:03

total.

1:54:04

how input tokens and so we can go back to all our demos we can go back to all

1:54:10

our demos here and let's say we have system message and user message and we can use a simple

1:54:16

tick token package to found the number of tokens.

1:54:18

Kikna input tokens and Kikna outtokens.

1:54:20

So we can do that.

1:54:22

So just keep this at the back of your bunch, but the platforms will do it for you.

1:54:26

I just wanted to clarify, you know, there are some demos that are shown here, but it's not like we don't

1:54:31

do it this way in practice.

1:54:32

In practice, you can't do it.

1:54:34

practice you can go back and use these kinds of end user interfaces like rock and you can use

1:54:39

these the logs and the usage things and you can keep a trap of the tokens.

1:54:43

Kikna token future.

1:54:44

If token usage here is right, but yeah, programmatically if you want to do it, just remember

1:54:49

there's a package from tick to get from a theoretical perspective.

1:54:52

Okay, so yeah, so as I told you, these are some aspects of billing, latency and length

1:54:58

straight off we talked about very important. So billing is an important factor. Latency is an important factor

1:55:03

and quality is an important factor but of just writing a rich system prompt is not enough

1:55:08

just writing giving few short demos is not done this is when you're focusing on quality

1:55:12

he both a problem we want to build an excellent problem okay very nice but please remember

1:55:19

more input tokens and longer output means more billing

1:55:23

you're accuracy a good quality good prompt but it will also take more time for

1:55:29

to read and write please keep that at the back of your mind so this trade off is what we want to

1:55:33

to discuss over. Next another very important thing is to talk about a concept called

1:55:41

context window. What is context window? Very easy concept. Context window refers to the maximum number

1:55:49

of tokens and LLM can process in one request. Your full input plus the model's generated output.

1:55:56

Please keep this at the back of your mind. What is the context window? Every language model has a

1:56:00

context window of its own. Even the modern

1:56:03

we are using right now lava 70 or billion versatine model it has a certain context

1:56:08

but what models the capacity is how much input to

1:56:12

the maximum number of tokens it can process input input input or output together

1:56:20

who's the context video of that's okay now processing power

1:56:24

back example they know but i think just to think from a you know from a human

1:56:29

analysis, right? So think of it this way. I have the human brain. Let's say this is my brain.

1:56:37

Okay. My brain has a certain capacity. So my brain's

1:56:41

context built. My brain can take a certain amount of input. My brain can take a certain amount of

1:56:48

input. And why if it is processing, it can give a certain amount of output. Now,

1:56:58

I cannot absorb a massive amount of information as input and

1:57:03

such that I cannot give out a massive amount of information output.

1:57:07

My context is limited. That's why we can talk about multitasking.

1:57:12

That's why we can talk about multitasking.

1:57:12

At the end of the end of the goal.

1:57:15

So that is the context with, at a time,

1:57:18

how input or how input,

1:57:19

such at a modern process, a human brain can process,

1:57:22

or the language model can process,

1:57:24

that's one way to become. That's the context. That's the one way to become.

1:57:27

That's the context.

1:57:28

and why is it important to talk about? Because, and if you ask me,

1:57:34

he sir, which models are the highest context windows? Gemini models are the highest context

1:57:40

language model. Anthropics, flawed models are the highest context windows today.

1:57:47

Close to a million tokens. But the open-eye models, surprisingly, have very low context.

1:57:54

Their context windows are up 128,000, 256,000.

1:57:58

So here we have some general examples

1:58:03

here we used to have in the older models. What we used to have in the older days,

1:58:07

right? So that's back in 2018, 2019, when the concept of language models were started

1:58:13

developed. The context window was very less. It was only 4 to 8,000 to us.

1:58:17

It was very small. It was very small. It was a small. It's like saying you have a very small

1:58:27

brain. If your brain, if your brain is

1:58:29

you, you know, if you're not

1:58:31

input in any way, if you've been

1:58:32

a problem, if you're doing something prompt, you'll

1:58:34

process in it. So, small language

1:58:37

models faint in that ability. They could not

1:58:39

process big and they could not generate big out.

1:58:42

That's a context window was limited.

1:58:45

And today, we are in the

1:58:46

we are in the world of long context

1:58:49

flagship models. Flagship models are all these

1:58:51

models we are having from open AI, the GPD models, the Gemini models, the Gemini

1:58:54

models, Anthropics, Glock,

1:58:57

models and they all have context window in the range of 200,000 to a million

1:59:01

million plus action in fact there are models with context windows above one million

1:59:07

for this benefit. The biggest benefit I would say the biggest benefit I would say is

1:59:14

if you have something with a long context window, you can attach a lot of information.

1:59:21

Everybody in this class has tried out, you go on to Germany and I'll just give you a simple example,

1:59:26

you guys have all gone to Gemini and Gemini allows you to attach files, a pile of person.

1:59:34

Have you ever wondered what is doing?

1:59:36

The more files you upload, the more pictures you upload, the bigger prompt you write.

1:59:40

This entire thing is part of an input.

1:59:44

Now,

1:59:45

now kushmi korea here, whatever you do, right? So if you take a look at it, just a second.

1:59:51

If you go and take a look at it, I'm just going to give you some, you know, general examples,

1:59:56

not make it cool at once but you.

1:59:57

But, you know, these files have been nothing right now, but I just attached three files for you.

2:0:02

You can you.

2:0:03

You can just remember, whatever files you attach and whatever stuff you write here,

2:0:08

this entire thing is part of your user message.

2:0:12

Gemini's limited.

2:0:14

Gemini is one of those problems with the highest context window.

2:0:18

It can process a massive amount of the

2:0:20

this whole context, this whole, your kind of a user message, in a way,

2:0:27

we will discuss some other ideas around it, but think of it like a user message.

2:0:32

But it allows you to attach all this, and then it sends all this to the analytical response.

2:0:36

We talked about this to the story, right?

2:0:40

Now the interesting part is,

2:0:43

you all of them say, some of you might have observed this also.

2:0:47

What if you take a massive file,

2:0:49

that you can try this exercise.

2:0:51

Today at the end of the class, you can try the exercise.

2:0:55

It will be a very interesting exercise to try.

2:1:00

You're a WhatsApp message for.

2:1:02

It isn't the exercise I want you to try.

2:1:03

Just to get out, you know, just so that you guys can build some context about context going to.

2:1:07

You're like somebody who will be chatting for some time.

2:1:10

You know, it can be a friend.

2:1:11

It can be your parents, whatever.

2:1:13

You have a few years of chat history data.

2:1:16

WhatsApp in you have export for you.

2:1:17

Transcript in.

2:1:18

go export to export. I think text file in export, in TXT file.

2:1:22

Okay, it's a TXT file will be massive.

2:1:26

When I said massive, it will be massive. Given that, let's say,

2:1:30

if you're talking to your parents, brother, friends, whatever.

2:1:32

It's all the years and a chat.

2:1:34

So, how many shares, how much text have.

2:1:38

It will be massive.

2:1:40

You'll be tokenizer, you'll probably get 10 million tokens.

2:1:43

That would be it.

2:1:45

Now, very interesting exercise.

2:1:47

you take the file here, attach on Gemini.

2:1:50

Attached on Gemini.

2:1:52

Germany,

2:1:53

if you're not going to rate,

2:1:55

and you, then you ask you,

2:1:56

let's say you attach this particular file.

2:1:58

Let's say you attach this particular file.

2:2:00

You, then, then, please tell me,

2:2:04

please tell me,

2:2:06

what are the common words I use in my

2:2:11

cat transgrade?

2:2:14

As an example, you know,

2:2:15

so, what, what's used?

2:2:17

You will get a message from Gemini.

2:2:20

At the end, what you'll process

2:2:21

you, you'll,

2:2:22

you'll, where Gemini says,

2:2:24

I am sorry, I may not be able to process the entire

2:2:27

you.

2:2:28

You'll answer you're going to give up,

2:2:30

but this chat transcript is so massive.

2:2:32

10 million of tokens,

2:2:34

how long chat history are you.

2:2:36

This TXT5 is so massive that

2:2:38

Gemini was not able to look at the entire TXT5.

2:2:41

Even something as powerful as Gemini,

2:2:44

Germany has 1 million

2:2:45

context will do. This TXT file is even bigger than now.

2:2:49

So they can't process it.

2:2:51

It's not even memory.

2:2:52

You know, you know,

2:2:53

you know, you know,

2:2:55

it's 20 million words in.

2:2:58

But those who are the one million

2:3:01

process, they cannot process the other.

2:3:03

They'll only process one million words.

2:3:05

You're giving it 20 million votes.

2:3:07

Can't process.

2:3:08

Basically trunk it.

2:3:10

What we call it is called force trunkish.

2:3:13

There is a small topic that we have added here.

2:3:14

I think.

2:3:15

it's just a general topic where it.

2:3:16

It's going to get forced truncation.

2:3:18

So basically, can you call it context overflow?

2:3:22

I just wanted to give you a real use case of this.

2:3:25

What is the real use case of context overflow or context froncation?

2:3:30

There's a lot of story that's case used here generally,

2:3:32

but it's the general concept.

2:3:34

If you give a very big context, if you give a very big problem

2:3:37

of very big user input,

2:3:38

just the chat example that I gave you,

2:3:41

the model will not complain, the model will not complain.

2:3:44

The model will not complain.

2:3:45

will not show a red error banner.

2:3:48

It simply cannot read it.

2:3:51

It will just drop.

2:3:53

So early or middle portions of the prompt that dropped

2:3:56

or compressed before generation.

2:3:57

That's why you will be surprised to see

2:4:01

that in that entire, you know, that WhatsApp chat transcript that you upload,

2:4:06

maybe in 2014, you've got chanted, that

2:4:09

2018 you did some chat, it will not come.

2:4:12

So in bits and pieces, some things would have been all the way.

2:4:14

that is actually very risky.

2:4:16

So it's very important to understand the meaning of context window.

2:4:19

What is context window?

2:4:20

And next time your outputs are not coming correctly.

2:4:23

So, you know, you're using a command like this,

2:4:26

but you're getting the outputs which you don't expect.

2:4:28

We'll have to question the context window.

2:4:30

Most likely you're entering a situation which is called context number.

2:4:34

So what is it called?

2:4:35

It's actually called context limit.

2:4:37

So it's like saying, it's quite literally the analogy that we are giving

2:4:40

is pages ripped out of the middle of the book.

2:4:43

Because I'm sorry, I can't remember.

2:4:44

Remember, you give the human brain 1,000 pages to remember.

2:4:47

I'm sorry, I will not.

2:4:48

I'll rip out some pages and remember .

2:4:50

So I can only process that much.

2:4:52

That's the, that's the context behind what is.

2:4:55

Context over flow and context and context trunk it from it.

2:4:59

I hope everybody's aligned.

2:5:01

And this is another way to track it is to tick to it.

2:5:04

You will use a tokenizer.

2:5:06

One way to track it is using tick token or tokenizer.

2:5:10

That's one way to look up.

2:5:14

Tick token and tokenizer is one way if you'd be able to do.

2:5:19

Okay. Now, just to come back to the story, I was discussing this with all of you before we went to that other discussion.

2:5:26

We were talking about the concept of max tokens. What is the meaning of max token?

2:5:31

Max token basically stands for the maximum number of tokens that can be generated in the chat.

2:5:38

And I think now at this point in time, everybody appreciates why this is important.

2:5:42

I hope all of you in the class now, every

2:5:44

why this is important because you are trying to restrict the size of your output.

2:5:49

If you don't restrict the size of your output, the completions will be too big.

2:5:55

And too much, if you don't put limit on your output, it would be a, it might be too possibly,

2:6:02

B, it might take two times. So that is why we use something called max underscore token and how does

2:6:07

the code look like the code is very simple. Use case is more like you're an assistant to a

2:6:12

marketing team for the gaming company, Razor.

2:6:14

So this is the system message where we are saying, hey, you know, we will give you

2:6:18

specifications of a laptop and based on the laptop specifications, you have to curate a marketing message.

2:6:23

That is what you will have to do.

2:6:25

So based on the specifications of your laptop, you will have to curate a kind of a marketing message.

2:6:29

Here you get the user input. User input is the specifications of your laptop.

2:6:34

And based on the specifications of your laptop, you will have to generate the marketing message,

2:6:37

and this is how the marketing message will basically do.

2:6:40

And you can see clearly in the code, we have simply done max underscore,

2:6:44

tokens equal to 1000. So we are saying max underscore completion underscore tokens with the

2:6:49

thousand. So we have restricted it. So this is the important thing about max

2:6:54

and it's very, very, very, very useful in real application. You will always want to restrict

2:6:59

the maximum size of the output, the language model will generate. So this is what we

2:7:05

refer to as a prompt parameter. The structure is the same. We still have client chat

2:7:10

completions create model equal to model name. Messages equal to this. We have this. We have this. We have

2:7:14

the same story. This is the prompt and this is the prompt parameter that we have given.

2:7:20

And finally, the other very, very important parameter that you are able to see on the screen

2:7:26

is something for temperature. So temperature is used to control the variability of the language

2:7:32

language. So what is temperature? Temperature is explicitly used to control the variability of the

2:7:40

of the large language bomb. So temperature is basically used to control. So temperature is basically used to control.

2:7:44

no time. So it kind of controls how how adventurous the model model is when

2:7:51

picking up the next goal. How, how with what probability the model is able to pick up the next

2:7:58

moving. And the important thing here is, the important thing here is, you can see creativity versus

2:8:06

consistency. Creativity versus consistency. So in a way, it is like saying if you set a very high

2:8:14

impression that let's say this is the use case again the same use case we were

2:8:17

discussing a while back you were an assistant to the marketing team for the gaming company

2:8:21

razor you were an assistant for the company raiser and you help the team to create advertising

2:8:26

content for the company okay you are assistant to the marketing team and you help the team to

2:8:32

create advertising content for the company that's what we have right now so that's my

2:8:36

system message and and on the basis of this particular system message

2:8:41

you have this particular user message and this is how the response will do

2:8:47

and you can see here we have given two prompt parameters just the rest of the code remains very

2:8:52

similar in fact the code here is very easy i think everyone's starting to feel a lot

2:8:56

comfortable with the code maybe now so remember we initiated client equal to grok before

2:9:01

who our subset by the API PEM has set here and now from the court perspective this

2:9:06

template remains the same every time so client's chat completions create you please give the name of your

2:9:10

model and you specify the system message you specify the user message and temperature

2:9:15

equal to this and max 2x equal to this and this is a great example where you are setting a very high

2:9:20

temperature okay and a high temperature basically means that you are trying to make your

2:9:26

model more creative more creative you're trying to make your model more creative every time the

2:9:33

model will generate different different answers every time the model will generate different

2:9:38

different, different answers and you can try this one.

2:9:40

I'll run it.

2:9:41

Now, look, here the answers

2:9:42

a little bit more than.

2:9:43

We're getting at 2.97 for the way we are

2:9:46

getting the answer is a little different, and I'm going to run

2:9:48

this code again, and you'll see that the pattern is very

2:9:50

different now.

2:9:51

Now, look, here here paying in at,

2:9:52

it's sophisticated design, advanced features,

2:9:55

some other are.

2:9:56

The formatting is also different, star, star, bullet point are there.

2:9:59

So every time I'm running this cell, the same cell I will run.

2:10:03

The same cell I will run every time.

2:10:04

I'm getting different, different answers every time.

2:10:06

And different means quite different.

2:10:07

Now, look, here here pattern

2:10:09

is. Here, pattern

2:10:11

are different. Every time I'm getting a different set of answers.

2:10:16

Here they're different. Here, there's a good question.

2:10:20

It's a little bit of a mathematical question what you're asking.

2:10:24

But basically, you'll think, you'll think, language models

2:10:26

in what are what are language models?

2:10:28

I think you might have done a professor session by a one of class.

2:10:31

So basically, there, there probably,

2:10:33

there might have told you.

2:10:35

In a language model, what happens is,

2:10:36

basically based on the prompt,

2:10:39

you're trying to predict the next token.

2:10:44

All language models are basically born.

2:10:47

All large language models are basically next word prediction agents.

2:10:51

This is fundamentally LLM 101.

2:10:55

Basics of LNM.

2:10:55

LNM in what is what is what is LLM?

2:10:59

I am giving you a sequence of words to take.

2:11:01

And on the basis of that entire sequence of words,

2:11:03

you are trying to predict that next word what is.

2:11:06

There are thousands of possible words.

2:11:10

Now here here, look, overall the experience was dash.

2:11:12

You can't do that.

2:11:14

Dash can be positive, can be negative, can be anything.

2:11:17

But what is the probability of this one?

2:11:19

See, we are looking at the entire sequence of words.

2:11:22

And based on the entire sequence of words,

2:11:24

you are trying to predict what is the probability of the next node.

2:11:27

That is the problem that you are trying to solve.

2:11:29

So based on the complete sequence of words,

2:11:31

we are trying to find out what is the probability of the next one.

2:11:35

And whatever is the problem?

2:11:36

We are trying to predict that particular world.

2:11:39

We are trying to estimate what is the probability of that particular next.

2:11:44

So that is what we are trying to do.

2:11:47

Okay?

2:11:52

What does creativity mean for probability?

2:11:54

So when we set a high temperature value,

2:11:57

you think what happens is that we assign more or less an equal probability for all the words.

2:12:01

But it is like saying,

2:12:03

that if you're here here here, mano,

2:12:04

of three possible words. So that means you're giving one third probability between each.

2:12:09

If you have a high temperature value, you're probably, you're mostly having equal probability

2:12:13

for all words. So any of the words can get seven. That is what is going on mathematical.

2:12:17

You can click in if you're having a low temperature value. So that is the story that is getting

2:12:21

laid out here. A got a temperature high here. That means any of the words can come next. And based on

2:12:27

that next word can be also random. Based on that next word is also random. So high probability

2:12:31

the randomness is just not what the probabilities are equal.

2:12:34

But every word that might come next will have equal probability.

2:12:37

So the three of them as to selectors. You run it again negative select,

2:12:41

or run it again positive select. But when you set a low temperature value,

2:12:46

when you set a temperature value, when you set a temperature value, when you reduce the temperature

2:12:49

value, it reduces variability in generation. That means the answers become more consistent.

2:12:55

And that is what we've put in the content, creativity versus consistency.

2:12:59

Temperature one,

2:13:00

like creating every time you get different answers because

2:13:04

and temperature is even consistent every time you get the same answer

2:13:08

and to answer your question again good thing when i set temperature equal to zero

2:13:13

it is like saying whichever word is having a higher probability will

2:13:17

come but of all the words will not have equal probability

2:13:21

the highest probability words will always happen

2:13:25

make sense are you getting the intuition

2:13:26

So this next level is Gourtec. Just for you, just for you, maybe if people are really

2:13:35

to explore, you know, there's a soft max activation function. So behind the scenes, what happens

2:13:41

is, you know, through the temperature when the soft max function is getting configured.

2:13:45

Softmax probability is generated. That is the mathematical way how it is happening behind the scenes.

2:13:49

I give you the intuition, but mathematically you have the soft max for more confirmed.

2:13:54

Yeah, that again goes into deep learning neural network. Which is,

2:13:56

is not required but the intuition is more important. So that's to summarize the

2:14:00

conversation, temperature equal to zero, you will get the same answers. Every time you run the code,

2:14:05

you will get the same answer or near similar answers, near similar answers.

2:14:09

I will get similar answers every time. I will not get different answers. I will get

2:14:15

different answers. I will get the same with the sleek design, black design, durable construction,

2:14:19

I get the same pattern about this item with this classic black design. So similar, near similar

2:14:24

answers i'll say that is due to internals of neural nets sort of parameter values are

2:14:30

changing but you can see it is broadly almost the same so you run in n number of times you

2:14:34

can get the same answer to that's the other okay i hope everybody is clear everybody's

2:14:41

aligned with this that is the concept of temperature and and here we have discussed about a very

2:14:47

important concept which is referred to as temperature and the max tokens this phone so max tokens is used to

2:14:54

control the number of tokens in the output.

2:14:57

Output, how many tokens we want to keep.

2:15:00

And through temperature, we are able to control the behavior of the other day.

2:15:06

So for very high temperatures, it becomes very chaotic, repetitive.

2:15:11

I think repetitive is not the right word.

2:15:14

Repetitive is not the right word. Sorry, I think this is not the right world. This is incorrect.

2:15:18

This will be chaotic. Chaotic, it will be very different.

2:15:20

Whereas a low value of temperature would mean that,

2:15:24

it is it is data managed that means it will give very similar or almost the same output

2:15:28

every time okay okay if you chat gpt

2:15:31

so sir chat gpt gpt

2:15:33

me care temperature used almost is something around 0.6.7

2:15:37

temperature is also a system level setting

2:15:39

no we will not be able to see when you're when you're going to chat gpt and you're

2:15:43

chatting with chat gpt or jemini these other applications

2:15:46

you will not be able to see what is the temperature value you will only type the user

2:15:50

message your user message is combined with the system message and based on that

2:15:54

the chat competitions create is happening you don't as a user you don't get to see the

2:15:58

temperature but there is a certain temperature that is that they are also isn't so they

2:16:01

they usually use a temperature somewhere around 0.6 to 0.7 that is the default

2:16:05

temperature settings of chat chepo so they are kind of giving you balanced uh

2:16:10

creativity because chat gpt in other

2:16:12

question or chat gpt is giving the same answer every time it becomes boring right you want it to be

2:16:16

a conversational so for these kinds of conversational assistance you want the outputs to be more

2:16:21

every time somebody asks a similar question you want the outputs to be given in a different way

2:16:27

so these are more creative in a way in that manner in that context i hope this is absolutely clear

2:16:34

called the concept so this is the temperature use case i think there's nothing to talk about here

2:16:41

we already discussed this use case very extensively so we are basically tried out different temperature

2:16:47

values so we are trying out temperature zero we're trying out temperature 0 we're trying out temperature 0 and we just

2:16:51

using the same client chat conditions we even getting the response so this is the same

2:16:56

the same thing you're basically trying out two different things that you're seeing

2:17:04

okay is it fine everybody's okay is it fine everybody's okay i just wanted to pause for any

2:17:15

questions if you have any anybody has any questions so this is pretty much uh what we wanted to

2:17:20

we wanted to cover in today session and uh i'll just wait for a while for any questions

2:17:26

if you have any at this point in time but the overall agenda of today's session was to talk about

2:17:31

the concept of what uh you know what token counts are why token counting is very very

2:17:38

important right so we talked about the ideas of token counts right uh relating into real cross

2:17:46

building latency uh input output lengths what these things really are so we talked

2:17:50

about that we understood the context of a context window what what is the context window uh

2:17:56

context window here and i and i really encourage you like the use case and the case study i

2:18:02

gave you please take a WhatsApp transcript today tomorrow you can do that example not a check

2:18:06

right of you know upload to a Gemini upload to a chat gpt and you would see how the information

2:18:12

is getting truncated so we understood what is the context window that is the maximum number of

2:18:17

tokens input plus output combined the n l and that process but what kind of its power is

2:18:22

capacity we talked about the concept of temperature trading 3pc versus consistency very

2:18:29

important temperature equal to zero means it is consistent it is the same answer temperature very high

2:18:35

it is creating it you get different answers the higher the temperature value the more the very

2:18:40

every time you run it you will get different answers and this is usually used in use cases where

2:18:46

you want more creative responses let's say you want to create a marketing article

2:18:50

you want to create an advertisement in these kinds of cases you want the higher

2:18:53

temperature value whereas in more uh you know applications of you know

2:18:57

know where you want factual information you want the lower temperature value

2:19:00

it can we also looked at the concept of uh context

2:19:03

context of a in a real conversational context we looked at what it is

2:19:09

what it is and you know and how do we find out when the context is getting

2:19:16

bracket and when the context is all and this is exactly something i want you to them you can try

2:19:20

with a real WhatsApp transcript real WhatsApp chat uh

2:19:24

programmatically you can't do that whole txt file transcript

2:19:28

you can put that as a user input right and you can do it programmatically also but i would suggest

2:19:33

you do it in a simple way in jerry night now you upload

2:19:36

and you ask a question and you will see for yourself how that entire uh

2:19:40

context the word is happening okay everybody's okay all of you're with me

2:19:45

okay i hope it was a helpful session a lot of learnings here and for the first time we were able to call

2:19:50

the grog model that we were able to see the grog platform okay and we will take this conversation

2:19:55

forward next session on wednesday we'll continue on and we'll get deeper into APIs

2:20:00

we'll get a little deeper into that that he's a response object here like some of you were

2:20:08

asking me that this is a response i'm getting but what is that response is the response

2:20:12

we were just printing this out but it's a lot of

2:20:15

lot deeper than that if you if you print

2:20:18

if you're print there's a lot going on inside it's a it's actually a response

2:20:22

jason looking at jason okay so we'll get a little deeper into that in the in the next

2:20:28

session and we will see this in no detail like how to work with these

2:20:32

APIs the different APIs that are there

2:20:34

today we're crop before the next session i'll talk about some other things as well

2:20:37

okay so very interesting conversations to follow

2:20:42

okay so any questions just going to wait for a minute anybody

2:20:45

else wants to ask me any questions today people were very interactive so it was great to see i

2:20:50

think the demos had problem so uh so if there are no questions we will do the metimeter

2:20:57

meter whiz and the cold but just maybe 30 more seconds if anybody wants to ask me to go

2:21:06

the contents are all part of the 22nd june folder as always i'm reading the folder

2:21:11

folder uh folder names for you same place i have uploaded the content because

2:21:15

okay i think uh if there are no questions uh kith up over to you i think you can you can

2:21:28

take over thank you thank you so much everybody and uh good nights to all of you i'll see you on

2:21:34

wednesday day again take care guys and i will look forward to hear from everybody on that exercise how

2:21:39

you're able to the way to go yeah thank you so much all right

2:21:45

yeah thank you sir for another lecture and we will start with the poll guys i am

2:22:00

uh okay just give me one second it seems i don't have

2:22:04

uh give me one second guys hold on

2:22:13

seems i'm not able to open the pool

2:22:15

let me okay all right uh guys i'm not able to open it

2:22:29

i can i can i you want me to launch it prata i i can i yeah yeah yeah yeah yeah please do

2:22:34

right right yeah i'm able to launch it guys you can fill it up please yes it was launched

2:22:41

sure thank you so much i i've launched it for all of you yeah okay yeah thank you okay

2:23:04

okay uh guys this is the time you're done with the pole we will start with the

2:23:20

mentimeter quiz so i'm just what's the difference between okayish and average

2:23:28

sorry about that can you explain uh gurtec what you mean okayish and average

2:23:34

in the in the poll oh uh it's a it's a okay it's just less than average i'll just say that um i'm not really sure

2:23:54

anyways um okay so the mantimeter quiz uh link is shared uh link is shared

2:24:04

and the screen is also sharing i will end the poll now it seems everyone is voted

2:24:18

uh so answer i think you will need to end the poll i'm not able to end it

2:24:22

no sure i will do that thank you thank you everyone yeah sure uh everyone has voted shall i

2:24:28

i think it's just 12 people were voted so yeah yeah so the 11 people are attended i think so okay fine

2:24:34

sure thank you okay all right all right in that case we can start the mantimeter quiz now

2:24:48

okay guys requesting you to please join so we have seven players okay okay anyone else who's want

2:25:00

to join we'll just wait for 30 seconds more

2:25:04

So at 22, 13 I'm going to start, 10.13.

2:25:08

Okay, 20 seconds left. Anyone left to join?

2:25:34

three two one okay so yeah what do llm

2:25:46

what do llm APIs commonly build by we're starting off with a very easy question i expect everyone to get it correct

2:26:04

Yep, great. Yeah, everyone got that correct.

2:26:11

GROC API key. Nice. All right. Next question. Which layer should hold stable rules. So layer in this

2:26:31

case means prompt layers. So which layer, which layer, which layer of the prompts

2:26:40

should hold stable rules. The rules that you don't want to change. But you want to

2:26:48

ensure that they don't change. Again, pretty easy question actually. Yep, everyone got

2:27:01

that one as well.

2:27:02

I think I need to explain.

2:27:10

Okay.

2:27:14

We're starting to get into a bit of a difficult question now.

2:27:19

Why are 10 weak examples risky?

2:27:26

Make sure you read the options carefully before you answer.

2:27:30

answer. We are giving 10 week examples to an LLM. What's the risk in that?

2:27:39

I think someone might be having network problems because, yeah. Someone is probably having network problems.

2:28:00

Okay. So yes, they crowd the context. 10 weak examples. If you just keep on giving it weak examples, you are crowding the context, right? You are consuming tokens and then what will end up happening is there will not be enough tokens for maybe the output. And it is going to take those weak examples and try to generalize based on that. So I think this was, I think this was pretty self-explanatory.

2:28:30

All right.

2:28:34

Last two questions, bit difficult, but you guys should be able to get through.

2:28:43

Which tasks need low temperature?

2:28:47

So low creativity.

2:28:50

Someone seems to have raised a hand.

2:28:54

Okay, I will take a look at that later.

2:28:59

Okay.

2:29:00

Which tasks need low temperature, guys. What is something that does not require creativity or requires less creativity?

2:29:10

Pretty easy, I would say.

2:29:15

Okay. Classification does not require creativity because it's either a yes or a no question or is it like 0, 1, 2, 3 question.

2:29:28

Right?

2:29:29

but taglines certainly require creativity.

2:29:34

I mean, utterly butterly delicious, Amul butter, something like that is not someone who isn't creative can come up with, right?

2:29:46

As an example.

2:29:48

So, yeah, this is obviously, this requires a lot of creativity, taglines, poetry, these things.

2:29:58

So, yeah, okay.

2:30:05

For the things that you require a lot of creativity, you need to keep the temperature high.

2:30:10

Temperature high equals more randomness equals more creativity.

2:30:15

Okay? I hope you guys understand that.

2:30:19

If you're confused by it, of course, let me know.

2:30:22

We'll take a look at that part again.

2:30:28

which output setting limits rambling.

2:30:31

So rambling means a lot of, a lot of talking,

2:30:35

unnecessarily going around and around the topic.

2:30:38

Like, people in engineering might be able to relate,

2:30:44

but like the way you write exam, write long answers in exams.

2:30:51

Taking the same point and twisting it and writing it in five different ways.

2:30:57

in five different ways.

2:30:58

You can consider that as rambling.

2:31:03

Yes.

2:31:04

So the correct answer is max tokens.

2:31:07

Max opens is what limits rambling.

2:31:10

Examples.

2:31:12

Examples is not an output setting.

2:31:14

It's something you give in the prompt, right?

2:31:19

It's something you will give in the prompt or in the context to the LLM.

2:31:25

The output setting, you can just.

2:31:26

You can just set max tokens to do something and the LLM will start to give answers very briefly, very short answers.

2:31:35

So that's what this is. All right.

2:31:44

All right.

2:31:49

Congrats me, I guess.

2:31:52

All right.

2:31:54

Thank you guys for attending.

2:31:55

attending I will see you guys on Wednesday. Have a good night. And if you guys have any

2:32:02

doubt, please raise them in the next session. And please try to be a bit more interactive,

2:32:09

especially when Sir is trying to take a practical session because practical sessions will help you more

2:32:18

with your exams and your understanding also. Okay? All right.

2:32:25

