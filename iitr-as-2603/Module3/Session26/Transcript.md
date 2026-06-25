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

Hello, everybody, very good evening to all of you.

13:06

Hi, good evening everybody.

13:13

Just wait for a minute and we will kick off.

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

Thank you.

16:36

Good.

17:06

of you have joined in already.

17:36

Thank you.

18:06

Thank you.

18:36

Thank you

19:06

Thank you

19:36

All right, guys, yeah.

19:43

So everybody has mostly joined in here.

19:47

So we will be starting on.

19:49

And today we'll be getting on with a very different session, very, very different kind of session we'll be having on

19:59

on API's and JSON and something that is a little bit bit Python oriented, but you will also get a

20:06

flavor. It's a very important topic and we will see how the dots connect as we go along.

20:11

So just to walk everybody through the journey that we have done until now. So we are after we completed

20:18

module one and module two on Python and machine learning, in the current module on Generative AI,

20:25

we have, we have only got started. We've only got started. We started with LLM behavior. We talked

20:32

about how to write a prompt. We discussed a few different.

20:36

different types of prompting techniques, what is zero shot prompting, what is few shot prompting.

20:40

So we had a discussion on that. And we are also fairly comfortable from the last session in terms of how to write a prompt programmatically.

20:48

So we used a thing called GROC.

20:51

GROC is basically like this massive gigantic computing infrastructure. It's like an inference platform.

20:58

It's like a platform that has all the large language models inside it.

21:03

Open source once, think of it that way.

21:05

There are other providers.

21:06

also we saw. So GROP was one of these free providers that are available. And we were able to use an API key and send the prompt to GROC and get a response back.

21:16

Okay. And actually today's session is very closely associated with that. You know, in fact, what we did. So a large part of what we did, what we are going to do today is very much related to what we already have been doing for a couple of sessions here. Right. So if you look at that particular function that we are going to do today,

21:35

that we wrote, client dot chat, completions, not create, the very fact that we are sending a prompt to GROG and we are getting a response back from GROP, that is a big part of what today's session is also about. So by the time we connect, we complete the class, we'll be able to get a much better understanding of what an API call is. I might have used this term a couple of times that we are making a GROC API call. We are making an API call to GROC. And we will see this in a lot more detail what that actually

22:05

is. In a very simple term, you can think of it like a function call. We are calling the GROC.

22:10

GROC is doing something for me and is giving the response back to me. That's exactly what was

22:15

happening, right? So we were we were writing a prompt. We were writing either a zero shot prompt

22:18

of a few shot prompt or a chain of thought prompt. We were writing the prompts in different,

22:22

different ways. And what was happening is you're making a request to GROC. You're making a call to GROC.

22:30

GROC is doing some processing and it is sending the response back to you. That is what was

22:35

happening, you know, behind the scenes. That's one way to look at it overall.

22:40

Okay. I hope everybody, everybody has got a good feel in terms of what, you know, what it is

22:48

overall. And obviously, this is what we'll see in detail, specifically something called rest.

22:52

Rest API we will discuss. We'll talk about the different HTTP status codes. We have not

22:57

encountered these problems yet, but we will see some simulations today. And we will also understand

23:02

a little bit more about JSON. You might have seen a bit

23:05

of JSON in your Python sessions, something that you did in the very initial part of your

23:09

course. You might have seen some part of it, but we will review that again. We will see what

23:13

JSON is. And again, it is extremely important because this is something that you'll be using

23:21

all through in your journey. This concept of an API call is very, very important. How you make

23:27

an API call, what is the format of an API call. And that is what his entire module is about.

23:32

Now, let's move on. Let's completely get started here over on. And first of all, let us

23:42

understand what is an API and why do we need APIs? If you think about it, why do we require

23:51

APIs? So, in the last session, the previous couple of sessions, last and the previous

23:58

session, we've been writing simple prompts, right?

24:00

you can write a system message, you can write a user message, and we have been through

24:05

that journey, how you can write a prompt, how you can, you know, do certain things using a prompt.

24:11

So we have talked about that part already. Okay. Now, a system message cannot give you

24:18

live information, right? So if you think about it from a very practical perspective, a system message

24:27

cannot give you the live information.

24:30

about whether it cannot give you the live information about other things. So these,

24:35

these things a system message cannot do. Okay. So it cannot tell you what is today's

24:41

courier location. Let's say you want to know what is your order status. You place an order with Amazon

24:45

and you want to know what is your, you know, what is your current order status. So you cannot do

24:51

that kind of thing using a system message. Because system message will not have access

24:57

to the current database or the current details.

25:00

And this is exactly where APIs become very, very important.

25:07

So let me give you one more thought process to help you think about this a little better.

25:15

Okay. And maybe the best way to do it is using using a live example. So this will not be a big part of today's class.

25:23

We will see this in more detail later. That's why I've got Gemini opened on the site to show you this really cool example.

25:29

But we'll see this later.

25:30

everybody knows Gemina is a language model. I think that's what we understand until now, right?

25:38

Gemini is a language model. Just like we have got GPD is a language model.

25:42

Gemini is also a language model. But what you are seeing here on the screen, this is nothing but an

25:47

application. This application consists of a language model. So we can ask a question, right? This is

25:53

what we have talked about before. What is the capital of India? You can ask for a simple prompt.

25:58

And you can hit enter. Let me use a normal.

26:00

3.5 modeled. And what is what is going on behind the scenes? If you, if you, if you, if you

26:07

look at it, what is what is exactly going on behind the scenes when you, when you say, when you ask this

26:11

question, you are effectively writing the user message. The user message is getting

26:18

combined with the hidden system message. As we have discussed before, every application has a hidden

26:24

system message. Gemini, the creators of Gemini,

26:30

application, not Gemini model. Gemini has two names. Gemini is an app also.

26:35

Gemini is a model language model also. So I'm talking about the creators of the Gemini application.

26:39

So the creators of the Gemini app, what you're seeing, they have created some system message.

26:44

So that system message will combine with this user message. Because remember, system plus user is

26:49

what makes a prompt. And based on that, we will make the API call and get a response. So this

26:54

is basically how the story is adding up. So you take the user message. Gemini application internally,

27:00

has a hidden system message. This is my pen. Use my pen here. So Gemini application

27:06

internally will have its, you know, we'll have a certain system message. So you will combine that

27:13

system message with the user message and this is what the prompt is. And internally behind

27:19

the scenes, you're making a call to the Gemini model. We are not doing anything. The Google services

27:25

are doing all this. They're making an API call and we'll get a little deeper into that today.

27:29

What is it? But this is an API call.

27:30

Right. In simple terms, you can think of it like a function call. You're making an API call or a function call to the Gemini model. And the Gemini model is giving a response back. So what does the code look like here? The code is something very similar to client dot chat completions. Something similar to that. I'm not saying it's exactly the same. We use GROC in the last session, but here we will be in Germany. But all this is hidden from our view, right? If you see, none of this we are able to see. We are only asking the question and all this.

28:00

this magic is happening behind the scenes. The API call, using the model, everything is happening behind the scenes, right? And if you hit enter,

28:08

you will see how the Gemini will give the response. This is something we already know. Right? I want to clarify one thing, friends. See, it's refining the

28:16

response on that stuff it is doing. Now, very important. How do you think Germany has answered this question?

28:25

Did it need to refer to any external sources or some other public information to answer the question?

28:30

No. See, I like to take a very good, you know, I like to think of language models as the human brain. We have, we have 19 people in the class, 19 of you in the session right now. So every person, every student in the class is like a LLM. That is the analogy I like to take. So imagine every single person in the classes like a LLM, a Gemini model. If I ask you the question, what is the capital of India? How will you answer it?

29:00

You will go back to your pre-trained knowledge.

29:03

Whatever you have learned, whatever, whatever training you have undergone for the last 30, 40 years of your life,

29:10

all that is in your head, in your brain.

29:13

That is what is referred to as pre-trained knowledge.

29:16

Even for a large language model, LLM, there is a pre-trained knowledge or memory.

29:21

All that information that you have accumulated over the years, all that is the pre-trained knowledge of the model.

29:27

So whenever I ask you a question, you are using that pre-trained knowledge to answer.

29:30

that question. Right? I hope everybody's aligned. It is not using any external services

29:37

or tools. And language models will do this very well. If you go back to all the use cases we did in

29:43

the last plus also, you know, if I remember a few use cases we did, we did, we did that beautiful example

29:48

of information extraction from medical notes, right? So the language model inherently understands how to look

29:54

at medical notes and how to find age, diagnosis, weight. We did that example on.

30:00

meeting. The language model inherently understands how to look at the transcript of a meeting

30:06

and how to find the summary of the meeting. It knows that. It already has the knowledge. It doesn't have

30:11

to look up some external sources. It doesn't have to go to some websites, some U.RNs to look it up. No.

30:16

It is answering the questions from its preterm understanding.

30:20

And finally, the last session, we did temperature. We also had this demo on create a marketing

30:26

advertisement for a gaming company Razor, if you remember. We are asking a

30:30

language model to create a marketing advertisement, right? There also, it doesn't have to look up

30:36

anywhere. It just has enough context to do it itself. So, so all these kinds of questions, the language

30:44

model is able to understand, is able to answer directly from its pre-trained knowledge. But what if I

30:50

ask the question, what is the closing price of nifty today? Think about it.

31:00

If I ask this kind of a question, now, very interesting, the Gemini application can answer

31:08

beautifully. However, the Gemini language model cannot answer this question.

31:15

The Gemini language model cannot answer this question. And I think instead of demoing this in

31:21

Gemini, if I go back to the GROC platform as well, because, see, ultimately, Gemini is an application.

31:26

Gemini will work absolutely fine. If you go and ask, what is the closing price of Nifty today,

31:30

Gemini can answer. How will it answer? Because it will do a web search. See, it will

31:35

actually search. If you look at this part, it will actually search pinpointing closing price. It

31:39

will actually search online. Searching the web. This is the part I wanted to highlight,

31:43

searching the web and is giving the answer live from the website. So it is not answering the

31:49

question based on his pre-trained knowledge because you want a real-time information.

31:55

It is answering the question by searching the information from the web.

32:00

So, this is the native ability that we want to build.

32:03

Now, Gemini is already a built-in application, right?

32:06

But we are trying, we are going to in the future build these capabilities.

32:12

Now, you might ask me that, sir, what is happening here behind the scenes?

32:16

Well, it is making an API call.

32:18

And that exact API call is what we'll talk about today.

32:20

So all this while is just to kind of, you know, to help you appreciate and understand what that API call

32:30

basically is. Okay. Now, uh, if you go to GROC, if you go to GROC, if you go to GROC

32:39

playground, and if I ask the same query, now we did this in the last class, right, 70 billion

32:43

parameter model, we are fairly comfortable with GROC now. The story is the same. You ask this

32:48

question, please, Alon. Please ask this question to GROF. Okay, let's say it's a generic system message.

32:53

I'll give a very generic system message. You're a helpful assistant.

32:57

Helpful assistant. It's actually optional.

33:00

Who can answer questions? Who can answer questions? So, this is the thing that you're asking.

33:09

And let's see, this is the question you're asking right now. Any guesses what Grog will tell us?

33:14

So, Grog will tell us that, sorry, I cannot answer. I'm a large language model. I don't have

33:19

real time information to the current market data. My training data only goes up to a certain point in time.

33:26

And you know, this is actually often called the knowledge cutoff.

33:30

There is a technical term that we use for it. We call it, let me, let me ping this term to all of you.

33:36

We call it knowledge cutoff. Every language model has a knowledge cutoff. That means knowledge cutoff basically refers to until what point in time the language model has all the information. That is what point in time the language model has all the information.

33:52

That is what is referred to as a knowledge cutoff.

33:56

So unfortunately today, this this Lama's

34:00

7.3.370 billion versatile model, whatever we are using right now, this particular

34:05

Lama, you know, 70 billion parameter language model. It is a LLM, which was trained latest as

34:14

of data which, you know, several years old. I think it's a year, one and a half years back,

34:20

it was released. And it has data latest as of then. It doesn't know what happened in Nifty

34:25

today. It is not there in the pre-trained knowledge. To answer that question,

34:30

we have to build the capability. We have to build the capability. And moving to answer your

34:37

question, Mohammed, you are absolutely right. Perplexity is working just like Gemini as an application.

34:44

Remember, I told you that this is not a language model. Gemini is an apt. Perplexity is also an

34:50

apt. They're working the same way. But Lama 3.370 billion is a language model. So language models

34:59

cannot answer real-time questions. This is the capability we have to build. We have to build that

35:04

search capability. And you can actually ask a follow-up question. You know, you can ask a follow-up

35:09

question. What is your knowledge cut-off? You can ask it. Let's see what it answers. What is your knowledge

35:15

cut-off? If you ask this question to the Grog model, let us see what GROC has to say. If you ask

35:23

this kind of a question, let us see. So GROC will say, my knowledge cut-off is currently December 2023.

35:28

Can you see? That means the GROC model, this particular model, Lama, whatever model we have taken, the latest training data that this model has is latest as of December 2023. That means anything that happened before December 2023, this model doesn't know. Sorry, anything that happened after December 2023, you know, I would say it doesn't know. It doesn't know because the training cutoff is December 2023. That's one way to look at it.

35:57

But yes, as I said, if you have recent data, if you want to look at weather data, some real-time data,

36:03

language models cannot answer because language models do not have access to real-time data.

36:07

They only have data up to the knowledge cut-off.

36:10

Right? I hope everybody is clear. Right. So, I think if you look at it, look at this one. Okay,

36:16

there is this is this one way to look at it. Okay.

36:19

Now, this is just one small demo I wanted to show all of you. Let's go back to Germany again.

36:25

So what is Germany doing?

36:26

When you ask this kind of a question, Gemini is able to figure out, the application is intelligent enough to figure out.

36:35

Should I use my own internal memory, pre-trained knowledge, or should I go and do a search?

36:44

Or should I go and use another capability? What is our other capability? Let me show you.

36:49

People might have already seen this, but let me show you the other capability.

36:53

Show me the top.

36:54

show me the top promotion emails I have received.

37:08

I'm again asking, writing a user message.

37:10

User message will get combined with system message and if we give the answer.

37:14

If you take a look at it, this is also not something their language model will, it will connect.

37:17

This is interesting, connecting, connecting to what connecting to personal context.

37:22

That means it is connecting to the workspace.

37:24

And it will actually give me answers to, you know, a real, like, you know, a real, real, real promotion mails have actually received.

37:34

Real promotion mails have actually received.

37:38

So it has taken it up right from my email.

37:42

What did it do?

37:44

Can a language model answer this question?

37:46

So what if I go and put this in the grog?

37:49

You think it will be able to answer?

37:51

May, right?

37:52

This is that concept I really.

37:54

wanted to build today, right? If you go and ask this question, can it answer? Can it answer? I'm

37:58

sorry, it cannot. It says, I'm a language model. Please. I only have knowledge until what you taught

38:04

to me. I don't have ability to access your personal email account or Italy specific mails. I cannot

38:08

do that. I'm sorry. I don't have that access. So this is a language model. All large language models

38:13

are like this. They are only going to answer questions based on their pre-trained knowledge.

38:18

How do you make them powerful? How do you make them do things that these guys can do?

38:24

So, so this is not just a language model.

38:28

This is the LLM plus external tools.

38:32

So next time you think of Gemini, Gemini is much, much more than a LLM.

38:38

Because it can connect to a lot of external services.

38:41

So here it is able to connect to my Gmail.

38:43

Here it is able to connect to Google search.

38:46

And even a whole lot of other things and it will be able to answer questions.

38:50

Even I can ask a question.

38:52

Show me the, uh,

38:54

Show me the latest PPD which I presented.

38:58

This is actually a very hard question, right?

39:01

It's a very hard question.

39:03

So it will actually go back to my Google workspace because I've got workspace linked up.

39:08

And for these things to work, what you need to do is you need to go and explicitly, you know, give permissions.

39:13

So go to settings and there's an option called personal intelligence.

39:18

And if you click on personal intelligence, you need to click on connected apps.

39:21

And in connected apps, you have to give Gemini permissions to access.

39:24

your workspace. If you have given Germany permissions to access your workspace, then it will be

39:28

able to answer all these questions for you. Yeah. Oh, this is so incredible. They've added some

39:33

few more actually. I think the last few days they've added photos was not there before. So they actually

39:38

added and they took it out. So now I can see there's Google photos as well, which is incredible. I'll show

39:43

you a cool demo of that as well. There's search services. That means when next time you, when you're

39:50

asking a question, you're not just asking the question to just a dumb language model.

39:54

But you're asking a question to a very powerful application, which is able to connect to external services.

40:00

And this is exactly what we do using APIs.

40:04

That's the key takeaway of our session today. I wanted to show you this demo and then we will be seeing the, you know, the smaller chunks, demos that we have in our content.

40:12

This is the big picture idea. I hope everybody can relate to it.

40:16

So how has Google built this? Google has basically created these APIs.

40:21

And it allows us to connect to, let's say, G, G,

40:24

email, calendar, Google keep, book, search services, Google photos, YouTube, right?

40:30

And very interesting. You need personalized insights about your discover YouTube videos.

40:36

Google business profile you can connect. This is a very recent addition, right? You can also connect to

40:41

Google flights, Google hotels, classroom, Canva. This is so cool. So cool. Amazing. Amazing. So we can go back to the, we can go back to the, we can go back to the

40:54

interface again. And let me ask one final question. So, let's say I want to ask the question.

41:00

Show me that, show me the, show me the, show me all my personal photos, which I have clicked

41:11

from the flight showing mountains during, uh, during sunrise or sunset. I'm just giving a

41:24

example. You know, I like to take a lot of photos generally. Now, very interesting. If, you know, if I go and ask this question to a large language model, again, it will tell me the same thing. I don't have access. But what is Gemini? It is not just an LLM. It is LLM plus APIs. It is able to connect to external services. If you, if I do this, remember, I've got it connected to my Google photos also. It will actually real time go back to my Google photos. I wanted to show you this part particularly. See how it will actually connect to photos, personal context. It's actually doing a lot of work. And so the very recent intuition Google has done.

41:54

They've actually included and taken it away to do some security things and they've again put it back now.

41:59

You can literally have a photos library of tens on thousands of photos and you can see.

42:03

And look at this. It has actually given me some live pictures from my real photos.

42:07

It's even took the date. So I traveled in Ley Ladakh and in 2018. It's a long time back, but I traveled to

42:13

lay. I took some nice pictures from there and it's actually able to show it. How do you think it did that?

42:18

Because it was, it's not just a language model which is able to do it. Language model, you ask a question. It will give a answer

42:24

back in text, English text. But this is not just an LLM in action. This is where you ask

42:29

a question. The LLM is using some other external service to call the Google Photos. It's like a

42:35

function call, right? You are asking, please show me the top mountain photos, Sunside, sunset. And then

42:40

the model is making a kind of an API call or a function call. Think of an API call like a function call.

42:48

So Germany is now making a function call. It is making an API call or a function call to some other

42:53

external photos service. And it is saying, okay, please give me those science photos to me.

42:59

That photos is a separate application. Gemini is a separate application. Photos is a separate

43:02

application. Obviously there is photos.com is a separate application. Gemini.com is a separate

43:07

application. So here Gemini is trying to talk to photos. Gemini is saying, Gemini is making a call to

43:13

photos person, the two separate entities. Gemini is talking to photos and saying, hey, you know, we have

43:20

cyan here and cyan wants to see the sunrise, sunset photos. Please give it to me and

43:26

it's retrieving it from photos. And that is that request and response mechanism that we are

43:32

talking about today. Gemini is making a request to photos and it's getting the response back from

43:36

photos. And this is what we are able to see. And it's really cool. I mean, so today the functional capabilities

43:42

are amazing. You can literally ask, textual questions on Gemini and you can get incredible responses

43:48

on the basis of that. Okay. That's one way to look at.

43:50

it. Okay. So now moving on, let us see. Let us get going. And I hope everybody has

44:03

a very good understanding of the context right now. So now with this in mind, let's move on. Let's get

44:09

going. Okay. What is that if we provide Lama the API to access? It will show, huh,

44:16

absolutely, absolutely. But that is exactly what we will try to build during agents. We have not

44:22

come to agents yet, but this is that exact functionality you can also build. So Gemini is like a finished

44:27

application. But, you know, like, especially when we come to agents, we will be able to build exactly

44:34

those kinds of functionalities. So we'll be able to build those kinds of functionalities. Yeah. All right. Now,

44:41

let's come back to the flow of the session today. Now, so as I do.

44:46

you if you want to get this kind of live information, we will have to use an API. An API is

44:52

nothing but a function call. A more formal definition of an API is what? It is a contract

44:57

between two software components. It defines what request may be sent and what response

45:02

will be returned. Simple, straightforward. You know, imagine you've got Google Gemini on one hand,

45:08

Google Photos on one hand. Gemini is talking to photos, requesting some photos and photos is sending their response back.

45:15

That is you send a request. You're sending a request. Please give me sunrise, sunset photos and you get the response back. You actually get those photos. That's it. That's what an AP. It's like a contract. So we are making an API call. That means we are making a function call. That's the way to think of an API. That's one way to look at it. It's just to kind of explain to you what an API actually is. What does it even mean? API is like an interface. It's like an interface that is acting as a connection between the two entities. You have got.

45:45

Google Gemini, you've got Google Photos. We want to establish a connection between both of them so that they can talk to each other.

45:52

If Gemini wants to get some photos from here, okay, I want to create a medium of interaction.

45:58

That's one way to look at it. Right. Now, there are two important components here. There is something called request and there is something called response.

46:06

Now we are actually getting a little deeper into what an API call actually refers to. What are the things that are happening in an API call?

46:14

Okay. Again, a simple.

46:15

way to think of an API call is like a function call. What are the things that are happening? Do you send a request, you get a response back? Okay? Now, there are four main components of a typical request. So there are four main components of a typical request. One is there is a URL. You are basically the, you know, the website that you'll be accessing. And we will see this in our demo today. We will see exactly what this is. Okay. So it is a URL or an endpoint. This is like the URL where the survey.

46:45

is located. Okay. And HTTP method is basically going to be either a get or a post. So there are two

46:53

types of HTTP methods you have. There is a get method which is used for reading and there is a post method

46:58

which is used for creating. Right. So in our case, in the demos that we have discussed so far,

47:04

our concern is mostly with the get method. The post method is not relevant for now. Majorly it's

47:09

the get method because we are trying to fetch some information. And what were the three

47:15

specific demos we saw in our Germany. We were able to make a request and fetch some

47:22

information from search. Number one. Number two, we were able to make an API request and

47:28

fetch some information from Gmail, Google mail. Number two. So you saw my Google mail promotional

47:34

mails. And number three, we were able to make an API request and get some information from my

47:39

Google photos. You were able to see that third example also. So HTTP method basically stands for

47:45

the action. What is the action we are talking about? Is it a read action? Is it something

47:50

we are trying to get some information, a read action, or a right action, or a post or right action?

47:55

Heathers basically refer to some kind of an authentication mechanism, authorization mechanism,

48:01

API keys and all will be there. And Params is basically some other additional data that you want to

48:06

send. Like let's say a use case that we will talk about at a basic level in today's session would

48:11

be, at least to start with. I've got a lot of demos today, interesting demos today.

48:15

The basic one that I will show you is you want to fetch the weather information from a particular place.

48:22

Now, as I told you, a language model cannot do it. So we will use an external service.

48:27

We will use an external service. So we will use this kind of a service. We'll make an API call. We'll send a request, a get request.

48:35

Go to that particular service. Specify the latitude, longitude, which place, whether you want to get. Let's say Delhi is whether I want to get.

48:43

So send the latitude, longitude, and get the response back.

48:48

You make a request, you make a function call and you get the response back.

48:51

That's a simple way to think of an API con is like a typical function call.

48:55

You call the function, you know, you call the function, you send a request and you get a response back,

48:59

return value of the function.

49:01

That's one way to think about it. Okay.

49:03

The request part consists of these four sections.

49:06

Response part will basically consist of these two things.

49:11

Very important. We have something called the status code.

49:13

And we also have something called the body. What is the body of the response?

49:19

Status code will basically tell you, you know, whether the, you know, the request was successfully passed or successfully processed.

49:27

And that is what the status board will be. And the body will be whatever the body of the response is.

49:31

That's one way to look at it. Okay, just to summarize the conversation. I hope everybody's aligned.

49:36

Okay, I'm just trying to take you through some theory. And then we will see these things gradually step by step.

49:39

So next time, remember API, we talked about what is an API. API.

49:43

like a medium, it's like an interface. It's like a medium. It's like a medium. It's like an

49:48

interface. I want to establish a medium of communication between two parties. Gemini party, Photos party.

49:55

API is the medium. Okay? API request response. One person will send a request. Another person

50:02

will give a response. Straight forward. And these are the different components of your API request.

50:07

This is the way how you will typically do it. Specify the URL. Specify the method.

50:13

Get is going to be the main agenda for this session. We'll use get.

50:17

Headers will be some kind of authorization that will be required. See, everything will not be free.

50:21

Today's class will majorly focus on the free APIs because API, some of them can be very costly.

50:26

Right. For example, if you ask me, sir, I want to do search. So for doing search, you cannot do it for free.

50:32

You have to create, have an API key and then you have to access it. I can show you some demos on that also if you want.

50:36

But some of them are free. Like if you want to access this one, this is completely free.

50:40

You don't have to use any kind of, you know, this.

50:43

kind of thing for this. You can directly go to API.oponmeteo.com and you can directly,

50:49

you know, access the information from here. You know, it's a straightforward API that you have.

50:54

You can actually click on this site. Okay. And you'll be able to kind of fetch the information

51:00

from here. Okay. So some of them are actually completely free of cost.

51:06

But otherwise, you have to create an API key and then you have to access it. That's why the

51:09

authorization that it is there. Now, so moving on, so moving on,

51:13

all. Another very important terminology that is usually used is called rest. So when we talk about

51:21

APIs in the world of web applications and web development, the term that we usually use is

51:30

called rest API. You might have heard that term called rest API. Everybody will say rest API.

51:36

So we don't just say API. We always say something called rest API. But the story remains the same.

51:42

Nothing changes. So rest stands for representational state transfer.

51:48

Rest. Everything else, the story we discuss remains the same. Everything else. So it's like think of an

51:53

API like a restaurant waiter. You order from the menu, you send the request and the waiter brings the

51:58

food gives a response straight away. What do you do when you go to the restaurant? You're talking to the

52:03

waiter. It's like a medium. You are party number one, the customer and waiter is the party number two.

52:08

So you're you're making a request to the waiter. Waiter, I want this particular food.

52:12

waiter will process and get the response back. That's it. Straight forward. And what is the,

52:18

what kind of medium do the web APIs follow? They follow rest. Okay. So rest API is a term that we will

52:23

use going forward. Again, as I told you, you just have to specify the specific URL. You have to specify the

52:32

the specific URL and you also have to specify the, you know, the action that you want to take.

52:39

And as I told you, the focus for our session will be get, not post.

52:42

So get is where you want to fetch some information. So whatever we were doing in the class today,

52:47

it was always the get method. Okay, the get is what we are focused on. So today's lab will be on the

52:52

get. Read live weather data without changing the server. We want to just read the data. We want to go

52:57

to that particular URL. Okay. I want to send a rest API request to that particular URL and fetch

53:04

the weather information from there as a response, request response, fetch. That is what a get is for.

53:11

Right? And this is the way you.

53:12

you will typically do it in rest time. So you'll do it this way. If you just take a look at it.

53:17

Let's say list orders. You want to list what are the orders that are there. So we will do it this way.

53:22

Get orders. If you want to list one particular order, this is this is what you will do. You say get

53:27

and you will locate that order and give that name of that resource. It can be a URL also.

53:33

H2TPS a big URL you can also have it. Okay. If you want to place an order, this is the part we will

53:38

will not see in the session, but just a demo. If you want to place an order, that means you are trying to

53:42

make an update you are either trying to insert update or delete so whenever it comes to either

53:49

insert update or delete you will use a post method that's one way to look at it you will use a kind of a

53:54

a kind of a post a post is where you're trying to make a change to the state okay but that is

54:01

usually not going to be a thing we will cover here but we will see that at a later time here okay now

54:09

so as i say this is effectively and

54:12

we have seen what is an API. We have seen what is the rest API and what goes on in a typical

54:19

rest API request response mechanism. So request means that you're sending a rest API

54:25

request. You're using a get statement to send a rest API request. You're giving the URL

54:30

and you are also giving the other details and you're sending a request and the API is giving a response

54:38

back to you. That's one way to look at it. Okay.

54:42

Now, request part is done.

54:47

Response part, as I told you, there are two aspects of the response.

54:50

What are the two aspects in the response?

54:52

The two aspects in the response are, sorry, where was that?

54:56

Yeah, the two aspects in the response are status code and status body and response body.

55:01

I think body is very obvious.

55:03

Body is basically what response we are getting.

55:06

That is what the body stands for.

55:08

And if you take a look at the, if you take a look at the, if you take a look,

55:12

at the status code. Status code will basically tell you what is the code, the response code.

55:19

And this is very interesting. You know, we have not seen these issues in Grok yet. I'll try to

55:23

simulate some interesting demos for you. So, so you'll appreciate this a little better.

55:29

So, um, what kind of codes could there be possible, right? So let's say, as I told you,

55:37

the Gemini example, or let's talk about the restaurant waiter example. You go to the restaurant

55:42

you know your entity number one take a let me use a bit of a bit of a market so people can

55:49

appreciate better this is like me I'm person number one and there is the waiter right this is person

55:55

number two this is the waiter and API is that medium okay API is like that medium in between

56:03

how do you talk so as a customer I'll use a different color please I I will place a request

56:08

that get me chicken biriani you wait a waiter

56:12

have. Now waiter can know if the waiter will send a response back.

56:18

Okay.

56:19

That okay, sir, I will get it for you.

56:21

Or then he'll error that he'll ask you. I'm sorry, I cannot give you the code.

56:26

So, so the response that you get will contain two things.

56:29

It will contain the code.

56:30

It will contain the status code.

56:32

So waiter's a status code right.

56:34

And waiter's a message.

56:36

They will effectively be.

56:42

Now, now the status code in this case could be what?

56:50

The status code in this case could be effectively, it could either be a success or it could be a failure.

56:55

Like if you see any kind of status code coming up like to XX, it is like a success error code.

57:03

It is like a success error code.

57:07

But anything apart from 200, only 200 is like okay.

57:11

whether get succeeded.

57:13

That means you were able to successfully connect to the weather API get a response.

57:17

You were able to successfully connect to search get a response.

57:20

You were able to successfully connect to Gmail get a response.

57:23

Jemini was able to successfully talk to the Google Photos and get a response.

57:27

That is like error code 200.

57:30

But, but anything else is an error.

57:34

And there can be different, different types of errors possible.

57:37

You don't have to memorize it, but just, you know, this is by and large what you will usually see.

57:41

We'll try to simulate some of them today.

57:44

There can be an unauthorized error code.

57:47

Very common.

57:49

You will be able to see that with respect to, you know, with respect to GROC.

57:55

Unauthorized, but somewhere there's an invalid error key or something that you have.

57:59

4.04 stands for typo in the API path.

58:03

Like whatever API that URL that you're giving, if there is a typo there.

58:07

Let's a Gemini wants to access the photo services and Gemini is giving the wrong path.

58:11

So 4.0 for error code is common.

58:14

Rate limit is another kind of error code.

58:17

This is usually something that happens when there are too many calls that you're making.

58:23

Even that GROC was a kind of an API call, right?

58:25

I mean, now that we have talked about a bit of API, what would we be doing in the last class?

58:30

We were saying client dot chat, dot completions.

58:39

Dot create, right?

58:41

Even this is what we were doing in the last class?

58:43

But what were we really, what were we really doing?

58:48

What were we really doing when I say client chat completions create conceptually?

58:51

We are actually sending an API request.

58:54

We are actually making an API call there also.

58:56

The story remains the same.

58:57

So whenever you do client chat completions create, what are you actually doing?

59:01

You're taking that entire prompt.

59:05

You're taking that entire prompt system user message along with the parameters, everything.

59:09

You're taking that entire prompt.

59:11

And you're going ahead and on the basis of on the basis of that, on the basis of the

59:20

entire prompt, you are sending a request.

59:24

I'm sorry, you are sending a request.

59:30

You're sending an API request, a GROP API request.

59:34

And when you're making that GROC API request, remember, we made a API request to a very particular place.

59:41

Now, we did not have to do all that because Python took care of all those details for us.

59:45

But that is exactly what the API request was.

59:48

So behind the scenes, we were already doing these things.

59:51

But we did not quite get into it in the last session.

59:54

But that is what today's class is for.

59:55

But we were already doing this.

59:57

We are taking that entire input.

59:59

We are sending a request to GROC.

1:0:00

GROC is like our waiter.

1:0:02

GROC is like our waiter.

1:0:04

It is that other service that we have.

1:0:06

And based on that, GROC was sending a response back to us.

1:0:10

This is the story that was playing on.

1:0:11

And now that particular GROC response, given it was successful, and in all our cases in the past session, we had successful responses, if you take a look at it.

1:0:22

So, we were getting error code 200.

1:0:28

We were getting 200 error code.

1:0:31

But it could be that if your API key was not correct, let's say you are making the client chat completion screen and you're giving a wrong API key.

1:0:38

You will get 4.01 status code.

1:0:40

So, some of you, some of you reported it last class.

1:0:45

Last class we were doing the demo.

1:0:46

Some of you were actually reporting, sir, I'm getting an error.

1:0:49

And if you go back to those error messages, you will see the kind of errors you were getting.

1:0:53

You will see that error right at the end of your cell, it shows error and it also shows the code of the error.

1:0:59

And you will usually see a very common error that people were reporting was 4.01.

1:1:04

4.1 is a very common error.

1:1:06

Either you have not named your model correctly or you have not given your API key correctly.

1:1:10

because if you want to send a request to GROC, you cannot just do it for free.

1:1:15

You have to use an API key.

1:1:17

That is that authorization header I was talking about.

1:1:21

Right?

1:1:21

I hope everything is still clear to all of you now.

1:1:25

But there can be other kinds of errors also.

1:1:26

They can be like 4-04-0.4-8.

1:1:29

There can be 4-29 error.

1:1:31

This is a very interesting one because remember, I told you GROC is a free service.

1:1:35

GROC is giving us the service for free.

1:1:37

So it is absolutely possible if you use it too much.

1:1:39

If you use it too much, I mean, some of you might have encountered that you're using GROC too much for your practice.

1:1:45

You will encounter 429 error, rate limit error.

1:1:49

Or even worse, sometimes the GROC server will be unavailable.

1:1:52

You are trying to make an API call and that service is not available.

1:1:55

The server is down.

1:1:57

Right?

1:1:58

Let's say Gemini wants to talk to Google Photos and for some reason Google Photos server itself is down.

1:2:04

The machine is crashed.

1:2:05

It will give me 500 error.

1:2:08

It is just like you're trying to.

1:2:09

to do a ticket booking in IRCTC and IRCTC website is down.

1:2:13

The server is down.

1:2:14

500 error.

1:2:16

So these are different, different types of error ports that we get.

1:2:20

So it is very important to also understand the kind of error ports we are getting.

1:2:24

Right, just so that everybody is able to fund it.

1:2:27

And if you want to see this, I can show you a small demo of that 429 error.

1:2:30

I told you this last class as well.

1:2:32

You can go to GROC.

1:2:33

We already set up GROC last session.

1:2:35

Go to Dashboard.

1:2:36

Go to logs and you will see some examples of 429 errors here.

1:2:39

Can you see?

1:2:40

First of all, this is error 400.

1:2:42

This is that error code 400 I was talking about.

1:2:44

This is the incorrect.

1:2:45

So I'm sending an incorrect model name.

1:2:47

And if you want to see some rate limiting errors, this is rate limiting error code 429.

1:2:50

Can you see?

1:2:51

This is that error code.

1:2:52

These are all 200.

1:2:53

200 means succeeded.

1:2:54

Every time you're making an API call on GROC, the demos we did last session, every time you do that,

1:3:00

every single request is stored here.

1:3:02

Whenever you say client.chatcompletions.

1:3:04

Create using your GROC account, using your specific API key, the GROC account,

1:3:09

GROC account that you have created, it is all, it will all be logged here.

1:3:13

Dashboard and logs, it will all be logged here.

1:3:14

You can also take a look at it.

1:3:16

I think your last demo was on, I think, when did we do it?

1:3:21

20, 22nd June, right?

1:3:22

So you can see 22nd June you did some demos in the class.

1:3:26

Everybody will be able to say error code 200 because all your demos succeeded.

1:3:30

So you got a success, you know, response.

1:3:33

You can actually see that in GROC.

1:3:36

But sometimes you might encounter four to nine rate limit.

1:3:39

Why? Because this was a different session I was doing for a different audience and we were doing a very heavy usage of tokens.

1:3:46

So either my input prompt was very big or I was trying to generate a very big output response and I was exceeding the tokens.

1:3:57

And you might ask me, sir, why are you exceeding tokens?

1:3:59

Because remember, these models are freely given to us and there is a token limit that is given to us.

1:4:03

Otherwise, these are very costly. How can Grog give it to you for free permanently, right?

1:4:07

So there are limitations that they have imposed.

1:4:08

only 12,000 tokens a minute you can apply.

1:4:11

You can use.

1:4:13

In a minute you're crossing 12,000 tokens, then you have to wait, rate limit exceeding.

1:4:19

Okay.

1:4:20

If in a minute you're doing more than 30 requests, there are 30 chat completions, not create

1:4:27

requests you're making.

1:4:30

There are 30 API requests you're making to GROC.

1:4:33

Well, if you will not allow more than 30, the limit is 30.

1:4:38

And I think the story here is something like, if I have to give you an example, if a lot of people are trying to book IRCTC tickets at the same time, I think we have all seen, even income taxes websites crash at times, right?

1:4:51

So last day before filing deadline, income taxes, you will see that, you know, so last day overall, before the filing deadline happens, many people are trying to file their income taxes together.

1:5:08

So multiple people are trying to file their income taxes together.

1:5:11

So what happens is there are multiple requests you are making at the same time.

1:5:15

Multiple people are trying to make requests at the same time and the server crashes.

1:5:19

So these kinds of things happen basically.

1:5:22

So these are the limits which are basically imposed.

1:5:24

All if you can take a look at it's okay.

1:5:26

So from the response perspective, there are two important things.

1:5:28

One is the status code and only if the status code is successful, what do we do?

1:5:34

Only if the status code is successful, we then go back to the body of the response.

1:5:38

the body of the response because the response consists of two things, the status code and the response body.

1:5:44

And now we will get a little deeper into understanding what that response body basically is all about.

1:5:52

So we have seen APIs. Specifically, we have seen rest APIs. We understood what is an API call,

1:5:58

which is nothing but you send a request and you get a response. That is what an API call is.

1:6:04

Right? That's what an API call is. You send a request and you get a response. That's an API call.

1:6:08

And the final thing that we have seen is the idea of what are the different components of the request and what are the different components of your response?

1:6:19

These are the things we have seen.

1:6:21

Now, let's get a little deeper into another very interesting thing called Jason.

1:6:28

What is what is Jason exactly? What does what does Jason even refers to?

1:6:33

So Jason, the full form stands for JavaScript object.

1:6:38

Notation. Very interesting. The term JavaScript actually gets used, but, you know, it has nothing to do with JavaScript, the language. So that is something I wanted to clarify. So a lot of people. So, yeah, so Jason, the full form is JavaScript object notation. Let me just, ping all of you.

1:6:55

Gurtig has asked a question. Gurtig, there is no statistics and probability in today's topic. There is zero mathematics related to today's topic. We are only seeing applications and APIs. There is, there is, there is no relationship with statistics and probability.

1:7:08

not even remotely with respect to what we are seeing here. Okay. I just wanted to clarify. Yeah.

1:7:15

Okay. If it's a general question I can answer, if you, if LLM wise, you're asking an answer, but if you're saying, sir, if APIs and

1:7:21

Jason and all this, is there any statistics there, there is none. This is just general concepts we are seeing. Okay.

1:7:27

There's no math that is going on behind the scenes. Yes. Okay.

1:7:38

JavaScript object notation, JavaScript object notation. This is what is called. This is the full form of JSON. And as I told you, it isn't tied to Java or JavaScript. It is not that. So what is Jason? It is a universal text format. It is a universal text format that is very, very useful for transmitting structured data between systems. This is what Jason. Jason is one of the most popular file formats used in web.

1:8:08

today. Whenever we talk about the internet, anytime you are going to a website, you're clicking a form,

1:8:16

you're hitting submit, or you're filling up a form, you're, you're doing anything on a website or a web page.

1:8:21

You're basically working with Jason behind the scenes. We don't get to see that, but I mean, it is, it is related to,

1:8:30

you know, I would say, yeah, so you're you're actually transmitting the data in a way. That is what it is. Okay.

1:8:36

So if you, if you relate back to once again, what we discussed here, if you relate back to once again what we discussed here, we have, you know, we have, let's say, a system number one, which is effectively the Gemini example that we talked about today.

1:8:51

We've got Germany.

1:8:52

This is one person, and we have got Google photos. This is the other person, right? This is the same example we have taken before.

1:8:59

Okay. We've got the photos person. We've got the search person.

1:9:04

And we also got the Gmail person. Okay, each of these are three different separate services. These are three separate applications. And the Gemini guy wants to talk to it. How does Gemini talk to it? You cannot just directly talk. You have to talk in some language. We eat English or so API is that language with that interface. It is creating that interface of communication. That interface of communication is what is referred to as rest API. Okay. And what are we doing?

1:9:34

So Gemini will basically send a request. It will send a request and it will get a response back.

1:9:40

So, and this entire mechanism of conversation usually happens in a JSON.

1:9:46

This usually happens in a JSON. You're sending a request in JSON and you're getting a response back in JSON.

1:9:52

So JSON is a very, very important file format for transmitting data between systems.

1:9:58

So whenever we are making API calls, be it a request we are sending, beat a response we are getting,

1:10:03

and JSON is the, you know, is basically what is used behind the scenes.

1:10:09

Okay. Similarly, it is, it is, it is, you know, accessing the search service using JSON.

1:10:14

And similarly, even Gmail it is, you know, doing isn't JSON. So that's the way how it is

1:10:18

intuitively working out behind the scenes. Okay. Now, what exactly is Jason? It is very similar to

1:10:26

a Python dictionary. So the structure of our JSON is very, very similar to a Python dictionary.

1:10:31

Very, very similar to a Python dictionary. This is very, very similar to a Python dictionary. This is very

1:10:33

basically what what the JSON looks like.

1:10:37

You can take a look at the screen.

1:10:38

This is, this is effectively what the JSON, you know, Jason looks like.

1:10:43

So name, or I think you can relate to it.

1:10:45

This is exactly something very, very similar to what we talked about in a Python dictionary.

1:10:49

So, so Jason is exactly very, very similar in form and structure to a Python dictionary.

1:10:55

Okay, and which is the reason why it is very easy to load a JSON into Python and vice versa.

1:11:03

So parsing is very easy. So if you already have a JSON, it is very easy to load that

1:11:11

JSON into a Python dictionary. And we can use something called JSON.

1:11:15

dot loads or response dot JSON. So both of these things can be done. And what we can do is we can

1:11:20

take a JSON and we can convert it to a Python dictionary. So let's say on the left hand side,

1:11:25

we have a complete JSON string. And I'll show a demo of this also in a moment. So let's say on

1:11:31

the left hand side, we have a complete JSON string. It is one.

1:11:33

big text file. So that JSON string is like one big text file you've got right now. So let's say on the left hand side you have this, you know, this one massive, you know, a Python string that you have on the string. And I'm sorry, I'm sorry, Jason string. Sorry, Jason string. You have a string basically, whatever. It's like an STR in Python. You can have this massive JSON string which is there on the left hand side. And all you can do is you can go ahead and

1:12:03

load it in Python as a Python dictionary. So that's the piece we are trying to talk about. You can take a JSON string and you can load it in Python like a Python dictionary. It is interchangeable. The format is interchangeable in a way. Okay. So Jason to dictionary and dictionary back to Python. Okay. So guys, yeah. So this will be shared with you

1:12:23

tomorrow. Okay. So we'll upload this in the notes tomorrow because I have this and I have some of my code notes as well which we shared. So we collate all of it and we will share in the materials tomorrow. Okay.

1:12:33

And this is another sample response that you'll be getting. You can see. So when we make the API call to the weather API, I told you, request response, the communication will happen in JSON. So when you send an API request, you're sending some JSON there. And when you get the output response, you're getting some JSON back. Because JSON is that, you know, that mode of transfer. It's like that mode of communication. Think of it back a way. And this is how a typical response will look like. It looks like a string, but you can load it into Python like a dictionary. And you can load it into Python like a dictionary. And

1:13:03

you can parse the information from here. And I'm sure everybody is with me that, you know, if you want to know what is the

1:13:09

temperature from this particular, you know, JSON that you are able to see. What is the temperature from this Jason? This is actually a JSON. I can save it at a JSON file, a dot JSON file. I'll show you that demo in a moment. But what you can also do is you can effectively load this into a Python dictionary, right? So I can basically load this into a Python dictionary. And I can effectively

1:13:32

I can effectively extract the temperature information out of that. Okay. So it is like data of current. So this is the key and this is the value. All of you remember dictionaries from your Python sessions, right? So dictionaries have key value pairs. Okay. There is a key and this is the corresponding value. Curly braces, there is a key and there is a corresponding value. So dictionaries will have these kinds of key value pairs. Similarly, JSON also follows the same structure.

1:14:02

You have a particular key. You point to that particular key and you get that entire value. And now within that value, you're again pointing to the temperature key and you're getting this value. 34.2 is what you will end up getting back. That's the way to look at it overall. What a typical JSON file is. So you can absolutely, you can absolutely, you know, save this as a JSON file. So whatever you're able to see on the screen, this is effectively what a JSON is. You can absolutely save it as a, you know, as a simple, simple, you know,

1:14:32

Jason. So let me show you, I think, very, very simple demo so that, you know, people appreciate this neatly. So all of you understand it nicely. So what I will do, I'll just create a small file for JSON. Demo.Json. Give me one second. And everybody can see this. This is what my JSON file will contain. Can you see my file name? My file name is demo.J. This is all it is. This is all that

1:15:02

JSON file looks like. So you can have a file which is called demo.jason. I'm actually saving this in Notepad also. You can see. And this is exactly what your JSON file will contain. It follows the exact same structure of a dictionary. That's your JSON file. Okay. So you can take this JSON file and let's say if I move it to Collab. So can I move my JSON file to Collab. Yes, I can. Let me do that for you. I will just upload this file on Collab for a minute.

1:15:32

And I will show you how to read this JSON file. Very simple way to do it. There it is. This is a simple way how you can load the JSON file. Can you see demo dot JSON is my file? And if you click on it, this is what the JSON looks like. So right now, we just talking about what is Jason. That's it.

1:15:47

Jason is a typical. Think of it like a file format. Just like we've got TXT, we've got other kinds of file formats, doc file, Excel file. Jason is a kind of file format. Very easy, very simple way to transmit information in the web request and response.

1:16:02

JSON is. So we have this JSON file. Can we load the JSON file? Yes, we can. We can absolutely load this JSON file as a Python dictionary. Right? So we have got demo. JSON. So we can easily load this file as a Python dictionary. So we can we can come here. So in fact, I can I can ask Gemini to do it. I can say load the demo dot JSON file as a Python dictionary. And you will see that it will use a very simple syntax. It will use something called JSON.

1:16:32

This is quite literally how you will do it. You will use something called jason. Dot loads.

1:16:38

And it will automatically convert this JSON to a Python dictionary. And you can see that. You'll see the code.

1:16:43

Very simple. Just one or two lines of code you can see that will come up. Okay. Can you see all of you?

1:16:47

You can see with open demo.json. So we are opening the demo.jason file. We are reading the contents. And we are saying JSON. Dot load. And we are loading the content. And we are loading the contents here.

1:16:59

Okay. You can take a look at it. There it is. And what is this.

1:17:02

What is this demo data? What is this exactly? What is this demo data? What is the type of demo data? What is the type of demo data in Python? Demo data is basically a dict type. Okay. I think everybody can appreciate this now. It is actually a Python dictionary.

1:17:17

So what is the key takeaway from our session? The key takeaway from our session here, this very simple discussion is that, okay, a JSON is just like a Python dictionary. It's interchangeable. If you have a JSON file, you can read it into a dictionary. And if you have a dictionary, you can write it back to a JSON.

1:17:32

both ways. So I repeat again, if you have a JSON, you can read it into a dictionary, a Python dictionary. And then you can obviously do some processing. Like, you know, because this is a dictionary, you can say demo underscore data. And I told you like current, you can access with this key. Just like how we have discussed dictionary indexing, right? I think we have talked about dictionary indexing in our Python sessions. You have seen that already. So we are able to access the current key. We're getting this value. And, and within that value, you want to access the temperature key. The temperature.

1:18:02

the temperature. What is that? Let me just copy that temperature 2M key. And with that, you will get the specific value. There it is. You will get the temperature value. So this is the way how you can basically take a JSON, read it, convert to a dictionary and parse it. Okay. In a way, there is another term that we use. We call it parsing adjacent. And the other way around is also correct. Other way around is also true. What is the other way round? The other way around is where, you know, you already have a

1:18:32

a Python dictionary and you can write it back to a JSON. This is the other way around. So we have talked about both the variants. Variant number one, you have a JSON string or you have a JSON file, whatever it is. You can use JSON. Load to load it into a dictionary. You can convert it to a Python dictionary. And the other way round is also possible where you already have a dictionary and you want to convert it back to a JSON string, a JSON pine. You can say jason.comfs.

1:19:00

So jason. load jason.dum. You can remember. Okay. We will see some more demos on this now.

1:19:08

Okay. I hope everybody's aligned and everybody is absolutely clear with respect to what a rest API is and what a JSON basically is. Okay.

1:19:18

So let us see this now. Let us see a small demo with this particular concept now.

1:19:25

So you can take a look at this one. Similar demo I'm trying to show all of you. So built in module.

1:19:30

and this is my JSON string that I've got right now. So I'm just trying to simulate a sample response, right? So what I'm doing right now, I'm trying to simulate a sample response. In the real world, in the real world, how will this happen? Imagine there is a separate orders platform. Right? There is a separate orders tracking platform. You are sending a request and the orders tracking platform is sending a response back to you. Imagine for a minute, this is exactly how the orders tracking platform is sending a response back to you.

1:20:00

that is what the API is all about, right?

1:20:03

You send a request that, hey, please give me the status.

1:20:06

Sometimes it happens, right?

1:20:07

In chat, you're chatting with the Swigi agent and you say, please give me the status of, you know,

1:20:11

when I will get the order, whatever, right?

1:20:13

So the, so this is what is going on behind the same.

1:20:16

So you, so you send the request and, and that particular service sends the response back to you.

1:20:23

Okay, so the response will always come back in a JSON.

1:20:26

And now, as I told you, this is like, this is a string I've got, right?

1:20:29

usually we'll get a string. All these platforms, if you get a string, raw JSON arrives as

1:20:37

one long text string. And now you can simply say JSON dot loads and you can convert this to a

1:20:45

Python dictionary. And that's the beautiful part. It'll be done the code. What is that parcel? That parcel

1:20:51

is nothing but a Python dictionary. You want to see that? Let me just show you the type of this. What is the

1:20:57

type of parcel. Parcel is nothing but a Python dictionary. You can take a look at this.

1:21:03

So we have managed to call a Rest API, get a response as a JSON, convert that JSON to a Python

1:21:12

dictionary, and we're able to scrape some information out of it. That's a beautiful thing.

1:21:19

Now this is a very simple kind of a JSON demo we are seeing. As we get a little deeper in the next set of demos, I'll try to

1:21:27

take this simple JSON that we are getting back and we'll put this back in our prompt

1:21:33

and make a GROC API call. So we'll basically be doing two separate API calls. So one, we will do a normal

1:21:38

API call, get a JSON back. And with that JSON that I'm getting back, I'll make a GROC API call

1:21:44

and again get a response back, LLM response back. So that is the flavor we'll be discussing. Okay,

1:21:50

so that step number one we saw. So we talked about jason. Dot load, how you can take a string and

1:21:56

convert it back to a dictionary.

1:21:57

And similarly, this is the other way around writing JSON where you can take a dictionary

1:22:02

and write it back to a string. The story remains the same. Imagine this is the Python dictionary

1:22:06

you have. So this is like a dictionary in Python, right? Curly braces. So now you can take that

1:22:11

and you can do something called jason.d dumps and this will convert it back to a JSON string. That's

1:22:17

it. It's just the other way around. Okay, but for our discussion today, the focus will be more on the

1:22:22

first part. The focus is not on the second part. Naturely the focus is on the first part where

1:22:27

you know, when we are building AI agents, usually the focus is on the first part,

1:22:31

where you're typically making a rest API call to some service, be it a search surveys,

1:22:37

a Porto service, whatever. You're making a rest API call to some service. You're getting a JSON

1:22:42

response back in Python, because Python is your code interface, right? You're making a rest API call.

1:22:48

You're getting a JSON response back. And now using that particular JSON response, you are trying to parse it.

1:22:54

You're trying to get some information out of it.

1:22:56

So that's what.

1:22:57

PR prime to see here. Okay. Now, now we will see the full lab. We will see the complete interface

1:23:03

here. We'll see a very nice, you know, example where you can go back and effectively we'll call a weather

1:23:10

API. This is that same weather API that we discussed, like API.meteo. We will see that example

1:23:16

where you can call a weather API, get some information back as a JSON, parse that JSON, build a prompt,

1:23:22

and then make a GROC API call. So we'll see this one example. And I will also show you a few other

1:23:27

API related examples, some very cool hands-on examples where you'll be exposed to other

1:23:33

kinds of API. There are hundreds of different, different APIs you can have, but for the

1:23:37

session, I've taken some free APIs which you can call without creating keys and accounts and

1:23:42

all that, because some of these are chart services. So these are some free APIs that are there,

1:23:46

which you can easily call and you can get some practice. Okay. So we can take a short break right now,

1:23:52

right? Let's take a five minutes break and we'll circle back and we will see the rest of the

1:23:57

but in the rest of the part will be mostly the implementation we will discuss. So we'll see the implementation. And in the implementation, we will see the full collegiate example as we discussed here. Okay. Yeah. So I will see all of you back after a, after a short break.

1:24:27

Thank you.

1:24:57

Thank you.

1:25:27

Thank you.

1:25:57

Thank you.

1:26:27

Thank you.

1:26:57

Thank you.

1:27:27

Thank you.

1:27:57

Thank you

1:28:27

Thank you

1:28:57

Thank you

1:29:27

Thank you

1:29:57

Thank you

1:30:27

Thank you

1:30:57

Thank you

1:31:27

Thank you

1:31:57

Okay, welcome back everybody.

1:32:00

all of your back all of your back.

1:32:03

so we'll continue on the back.

1:32:04

So we'll continue on and we will continue on and we will see the full pledged example in terms of how

1:32:08

of how you know things are adding up.

1:32:11

Let us see that here.

1:32:12

So before we went for the break, we talked about what is an API, what is a rest API and we saw that

1:32:19

and we saw that beautiful example in Germany.

1:32:21

What it means to do an API call, like there is a request and there is a response.

1:32:26

is a response. So what goes on in a get request? We are focusing only on the get request right now. And we also talked about the get response. And the response we talked about these kinds of error codes. A few error codes we talked about, like 200 error code. And the specific error codes we talked about were the error

1:32:45

these were the error codes we will see are four not one like APIP error. You will see 429 is a very common error we will see, which is a rate limit error. And we will try to simulate some of these error. And we will try to simulate some of these errors.

1:32:56

in today's session right now. Okay. And now we also talked about the concept of JSON. Jason is a very common file format.

1:33:03

Okay. Jason is a, you know, it's a very, very common file format we actually saw. Okay. And you send a request and you get a JSON back.

1:33:16

And there were two other important methods we discussed. One is JSON. Loads, which you can use to read a JSON into a Python dictionary.

1:33:24

and we also talked about jason.dums, which you can use to write something back to a JSON file.

1:33:31

Now let us see this comprehensive example of how to map JSON fields into LLM prompt variables.

1:33:39

Let us see that concept here. Right. So as you can see, fetching the data is half the job done.

1:33:48

Okay, so fetching the data is only half the job done. And what are we what are we talking about?

1:33:52

right. So let's say, let's go back to this demo, right? Let's let me show you this first. Okay. So we have this setup here. And what I will do is I will basically use this URL, API.O.com V1.4. I don't worry. This is not to remember. It's just a service that is already available. So I will give the city name. I will give the city latitude, city longitude and the timeout. And I will basically set up the parameters for the query. And this is how we

1:34:22

do a get request in Python. So how do we do a get request in Python? We use the standard request library. It is a syntax. Okay. So how do you do that rest? What, you know, we were seeing rest syntax a while back G, T, get, but that's not how you do in Python. Python makes it very simple. In Python, you can simply use a request library to execute the get requests. You can use the request library to execute the get requests. You can say request.

1:34:52

And after you do request. Get, you can enter the URL. You can enter the parameters. What are the parameters? And based on that, you will get a response. It is that request response story that we talked about.

1:35:05

Finally, we are also checking what is the status code of our response. And if our status code is equal to zero, we are saying response.

1:35:16

dot JSON. Look at this part very important. I told you already that what you end up getting will be like a typical JSON string. It's not a Python dictionary. What what you're getting here is like a typical string. The API, the service will return a JSON string back to you. This string, you will convert it to a dictionary. You will parse the JSON string and convert it to a Python dictionary, whether data is a Python dictionary. And that is what we'll be observing. And if I run this, this is a

1:35:46

is what you will all get. Take a look at it. Getting the weather data for Delhi, it has actually run successfully. It went to that service. So from my

1:35:54

Google Collab, we are making a rest API call to that API.mito, whatever that is. We're getting a response back. We're getting a response back. And you want to see that response object, guys. That response code, error code is 200. 200 means successful.

1:36:12

And what is that response? You want to see that response? This is that raw JSON.

1:36:16

data. We're actually printing that raw JSON data. This is that raw JSON data that is fetched. You can see there is so much information. But we don't need so much information, right? That's what we were discussing. So this is the raw JSON data that is fetched. I told you how you can convert it to a dictionary. How we can further parse it. Because when we are getting this data back in Python, we want to parse it in a dictionary format. So that we talked about JSON.js, right? But the other aspect is we don't need all this. I just

1:36:46

want to know what is the temperature in Delhi, right? I just pass the parameters, Delhi, latitude, longitude. It giving me the entire thing for Delhi. But I don't need that. I don't need so much information. I don't need elevation and all that. This is a lot of data, right? And this is exactly what this next thing is about. How do we map the JSON fields into LLM prom variables? So fetching the data is only half the job. But we don't need so much information, right? So copy only the three lines that matter. We don't need everything. We just need temperature, weather code and latitude, longitude. That's it.

1:37:16

that's the only story. So we will call the weather API. We will get a response. Live JSON response we are getting. We talked about that. We are loading this in a Python dictionary. We talked about that.

1:37:27

Because this, this entity, what is, what is this entity? If I just run a print statement here, print type of weather underscore data. Hello, guys. What is this weather underscore data? That weather underscore data is a dictionary. Hello? I told you, right? That's a dictionary. It is a type dict in Python.

1:37:45

You can easily parse it as we talked about, right? So now the question is, do you don't need all this, right?

1:37:52

So I'm calling the weather API. I'm getting a whole lot of information, but I only need to extract the city.

1:37:58

I only need to extract the temperature and I only need to extract the weather description. Do we know how to do it? Yes, we do. Because now we have a dictionary and we can easily extract those relevant items.

1:38:11

If I ask you, how do I extract the temperature? Well, not very difficult.

1:38:15

from this dictionary access current and from this current access temperature. That's it. You can access the weather code also. You can access the latitude, longitude. We've already seen that.

1:38:27

So that is what this is about. So, and this is again, why is this important? Because when you eventually take that data and give it back to the LML, you want your prompt to be as efficient as possible. Because this is the big picture, you know, objective that we,

1:38:45

are trying to achieve. You know, we want to get the live weather data from the API,

1:38:51

okay, get the live Delhi weather data, extract the information from here in a JSON, and then eventually take that

1:38:59

live data and send it to a prompt and ask for advice whether how we should do our outdoor setup for some

1:39:05

event. So let's say there's a tech fest that is happening and we want to get the live data for

1:39:10

Delhi and we want the language model to tell us whether how the setup will be.

1:39:15

So, so whatever information you are getting from here, we will map it into relevant variables, which we are doing right now.

1:39:23

You can see. So we do not feed the raw JSON to the LLM. We don't do that because if I'm feeding the raw JSON to the LLM, there'll be too many tokens.

1:39:32

There are like thousands of tokens we will have. We don't need that. We will only need the specific, take only the specific fields we require.

1:39:41

Right. And then we will navigate that.

1:39:45

JSON dictionary, whatever dictionary we got, we'll navigate that. We will extract what is the

1:39:50

current weather code, information, temperature and all that. We will do that. We will extract that

1:39:57

information. So from that massive dictionary and JSON that was retrieved. And again, I'm calling

1:40:02

dictionary and JSON interchangeably because as I told you, you can easily load a JSON as a dictionary.

1:40:08

So dictionary and JSON, I'm using the terms interchangeably. So you can basically go and from that

1:40:15

massive dictionary or JSON that you have, we are simply extracting this information.

1:40:20

This is all we require. City, temperature, weather code and description. And now we will go and build

1:40:26

the downstream LLM prompt. This is that final prompt that we'll be building. And here we will give

1:40:33

the name of the event. And this is that final LLM prompts that we are building. Can you see? It is more

1:40:38

dynamic now. It is no longer a static prompt. It is a more dynamic prompt. And you can see, you are a campus event

1:40:43

assistant use only the live weather facts below do not invent temperature or

1:40:50

conditions. So don't make any guesses. Okay, Delhi is usually hot. Delhi is usually cold in winters.

1:40:54

Please don't guess any information. Use only the live weather facts below. Reply in under 80 words.

1:41:01

Okay. Event name is this. City is what is already coming from the variable city. What is variable city?

1:41:08

Variable city is nothing but Delhi. It is it is it is it is it is it is passing that Jason dictionary.

1:41:12

right? Life temperature is variable's temperature. It's parsing the JSON dictionary. I told you already. And conditions is

1:41:18

variable with the description. This is the information that you're giving in the prompt. And task is advice whether

1:41:23

whether outdoor setup should continue or move partially indoors. So this is your entire prompt that you are

1:41:30

asking to the LLLN. And if I run this code, this is how that complete prompt looks like. Okay. This is that

1:41:37

complete prompt for the large language model. And this is exactly what you will now,

1:41:42

used to make a groc API call. You will now use that to make, excuse me, you're going to use

1:41:49

that to now make a grog API call and get a response. I hope the story is clear. Okay. So how did we get

1:41:56

this information was from another API call? We made an API call to a weather service. We got this information.

1:42:02

We have put all that in the prompt. And now that we have the complete prompt, we make a grok call.

1:42:07

This is like a user message, right? This entire thing is like a user prompt. This demo, we don't have

1:42:12

system prompt. System prompt is optional. We don't have a system prompt here. It's just a user prompt we have

1:42:16

right now. So now you will take that entire user message, make a GROC API call and get a response. That is how the

1:42:23

whole thing boils down to. Right. And if, and if you want to see that entire exercise, well, here is what we are doing.

1:42:30

Take a look at it. As I told you, there is no system message we are put here. It's optional. Right. So now I have

1:42:34

the LLM underscore prompt. The LLM prompt is there. This is that whole LLM prompt. All this information I got from

1:42:40

that weather API service that I called, right? And now this is that LLM prompt and back

1:42:44

to the GROC world. Back to the GROC world, guys. You're making GROC client chat, chat

1:42:50

competitions create. This is one more API. So this is even simpler. You don't have to say request.

1:42:55

not get and all that anymore. Brock makes it even more easy. But behind the scenes, it is the same story

1:42:59

that we discussed. You're sending data as a JSON. You're getting the data back as a JSON request

1:43:04

response. So GROC is also doing the same thing. Not only GROC, every LLM provider that you have, be it,

1:43:09

platform open AI B, Anthropic D, Gemini. Whenever you're making API calls, they are all

1:43:16

doing the same thing. Data is fundamentally exchanged as a JSON kind of a format. This one everybody

1:43:22

can relate to. You're giving the model name, messages, temperature equal to points to and max tokens

1:43:27

equal to 150. You're trying to limit the number of output tokens. And this is that final response

1:43:32

you're able to get. And you'll be able to see the final response that we're getting is taking a while

1:43:39

because it's sending the data to GROC. And GROC's final response is, okay, hey, continue

1:43:42

with outdoor setup, as the clear sky indicates, no rain. However, considering providing shade and

1:43:48

hydration for attendees due to high temperature of 33.7 degrees Celsius. And this is, I think,

1:43:52

we are taking the real data from Delhi today. Okay, this is real time. This is real time. I mean,

1:43:57

again, the thing might vary, but I think Delhi is around this temperature. We're taking

1:44:00

real much of live as in as of now. As of now, we are taking the data, the Delhi temperature.

1:44:05

And if you go to Google, I think it will be like something around that only. Delhi's temperature

1:44:09

you right now, I plot, I've got whatever. So the services can differ, but approximately

1:44:13

it's around 34 degrees Celsius is taking. So this is, this is live data that you are using,

1:44:17

and you're able to, you know, fetch the live data, use that in the prompt, make an API

1:44:24

call to grow up and get a response. So this is exactly how we will do things going forward and how we

1:44:29

can build many advanced services going forward. So just here here here a simple API call we did

1:44:34

to a weather service, you can make that API call to any kind of service imaginable.

1:44:39

Which Bho. Stop markets. Let's say you want to build a trading agent. Imagine a trading

1:44:45

agent you want to build. You can make an API call to a trading agent. Okay, I have that demo also. Let us see that.

1:44:51

Okay. We can we can take similar demos in many other real world use cases. And here I've got five other very

1:44:59

interesting demos. Free of cost, you don't have to do API setups and all. That is very easy. No need to. It's freely available.

1:45:05

So e-commerce, financial markets, global forex.

1:45:09

We've seen some examples across the board. Let's say this is like another very simple example of

1:45:14

a e-commerce retail agent. It's like a fake store. Fake store. Imagine there is a retail store.

1:45:20

Now, the idea is if you ask some questions, that, this product is, I want to order this product. What happens?

1:45:27

Let's see you're a customer and you want to order a phone or you want to order seven packets of milk from Swigy Instamart.

1:45:32

What are you going to do? See, everything that you are seeing on the app, the app, the app, the app is the app,

1:45:39

behind the scenes, this magic is only happening.

1:45:42

This is all developer stuff.

1:45:43

But ultimately behind the scenes, what are?

1:45:46

When do you get to see that Swigi mainstamark in out of stock? How do you know that?

1:45:50

Well, how is it happening?

1:45:52

Because constantly that application is making API calls to the backend database,

1:45:56

your backend applications.

1:45:57

Swigy's order's application there.

1:46:00

So they also are maintaining some kind of a, a backend.

1:46:05

Swiki has a kind of an application which is,

1:46:09

And they are also making API calls.

1:46:10

Think of it that way.

1:46:12

So the Swiggy application is making an API call to that service.

1:46:16

And it is getting a response back about the, about the status.

1:46:21

About the status.

1:46:22

That okay, how many products are there?

1:46:24

How many items are there?

1:46:26

Is it available?

1:46:27

Is it out of stock?

1:46:28

All that information is coming from the APIs.

1:46:32

So APIs are all used, you know, behind the scenes.

1:46:36

Right?

1:46:38

Yeah.

1:46:39

When I ask, Gurteg has a question.

1:46:41

When I ask something to Gemini or chat GPT request is processed on their servers.

1:46:45

Yeah, you're sending a JSON.

1:46:47

Look, Gurteg, we are not doing anything.

1:46:51

Our just text input, text output, but all the magic that is going on behind the scenes is JSON.

1:46:57

That is actually, that is actually all the magic that is going on behind the scenes.

1:47:02

If you're building your own applications, then you'll be actually seeing that parsing happening.

1:47:07

But all that is hitting.

1:47:09

from us. All that is hidden from our view. See, that's why I told you, this response

1:47:13

object that you are getting. Let me, let me show you this response object. See, all this while in our

1:47:17

classes, what, what were we doing? You know, you're making a GROC API call and you're getting a

1:47:22

completion response, right? This response is. This response. We're, we're going to see the

1:47:29

full response. You want to see the full response. Hello, guys. Let's see the full response

1:47:33

for a minute, right? This is the full response. You will be able to see. Completions. Why?

1:47:39

Sorry, it's completion. This is actually the full JSON response that you're getting.

1:47:44

This is that full JSON response that you're getting. This is exactly how it is returned back.

1:47:49

This is actually that complete response. This is that complete JSON response. And all that we are doing is we are simply parsing that response.

1:47:59

Completions. Dot choices, zero dot message. content. Those response, me say content of the response. I want to only see that.

1:48:05

And that is what we've been using as a template all this file.

1:48:07

nobody questioned that time, but today we realize it. Today we understand what it is. You're sending a, behind the

1:48:13

scenes, you're sending a request as a JSON, getting our response as a JSON, but all that is hidden from our view.

1:48:19

Because Python is doing all that magic.

1:48:21

Now, you'll put you, sir, here on Jason, how they're saying? That is what Python is handling for us. That is what this client chat

1:48:27

completion is create is doing for us. We are not having to manually do it. And if you're using the base

1:48:33

Python library, the base Python library, just a request.org get was.

1:48:37

This is where you are manually passing the params.

1:48:40

Here, here also you are making an API call.

1:48:46

Chat completions create, you're also making an API call, but this is more high level.

1:48:49

This is the easier library to use.

1:48:52

I hope this is clear.

1:48:55

Now, let us let us see.

1:48:57

Come back to that fake store API use case once again, what we are doing.

1:49:01

So we are fetching the live product data for a particular product, which is number five.

1:49:04

Let's say some user has asked a question is that product.

1:49:07

available on the shelves or not available, whatever it is. So store URL is given.

1:49:12

Same story request response. You are sending a request, request or get. You're giving the

1:49:17

URL. You send the request and you get a response of the JSON. This is the product data JSON response

1:49:23

that you will get. And we are parsing that JSON response and you are converting this to a dictionary.

1:49:29

Product data will actually be a dictionary. And now we are simply parsing the information from

1:49:33

that dictionary. A lot of information will be returned here. If you want,

1:49:37

to see what all is returned. Let me print that for you. Let me print the product

1:49:41

underscore data for you. Let me show you. I'll just use a print statement here just to show you.

1:49:47

The complete product data returned from the API, from the API request, rest API request.

1:49:59

Basically, technically we are calling it a rest API request. This is the whole product data,

1:50:03

the entire product dictionary that is returned back. Out of that, you only want this.

1:50:07

information. So let let us see what all is returned back. This entire thing is

1:50:12

returned back. Public sector. There's so much. There's so much. We have the product ID. We have the

1:50:16

product title. We have the product price. Description. We have the category. We have the image

1:50:24

also. Product's image. It's so interesting. Rating be. Customer has kind of rating be a count

1:50:31

be here. It now available. And I think now you can relate to it. Behind the scenes data

1:50:36

is safe. It's able to see. Whatever you're basically seeing this on be. You're actually

1:50:41

seeing the title. You're seeing the image. This is all getting picked up from here. So all the magic

1:50:46

is happening this way. So you're fetching the product, right? And based on that, you're building the

1:50:54

prompt. You're accessing only whatever information is required from that product that you fetched.

1:50:59

And now you're building the prompt. You're a highly.

1:51:01

persuasive professional e-commerce sales agent. So please write a short, punchy sales pitch

1:51:05

under 50 words convincing the user to buy this highly rated product today. So whatever

1:51:11

product you have fetched, you please write a marketing pitch for that. And see how dynamic this is.

1:51:17

Depending on whatever product ID you give, it will automatically fetch that particular product.

1:51:22

That product basis, he will prom-based and that prompt-based on grok response day. I hope everybody's

1:51:29

aligned. Because these are placeholders.

1:51:31

A put. And let us take a look at it. For product ID 5, you're getting this thing.

1:51:35

Elevate your style with this stunning 4.6 rated product, John Hardy, Brace, let him. Then you can

1:51:39

see this. Now, his ID number change. Number 6, you will see, I'll get a different thing. I'm getting

1:51:45

a different product, which is, I think, some satisfaction, whatever that is. This is a rating

1:51:49

is a little bit more. But you can see elevate your style with our this, rated this, solid, gold,

1:51:54

pitite, micro, micropave, I don't know what that means. So, uh, but, but, but, but

1:52:01

whatever. It's a random fake data, by the way. Luxurias, durable time date. But,

1:52:05

but the idea is important, what we are, you know, what we are doing. Okay, let me change it back

1:52:10

to five. There is another very interesting use case. This is actually accessing data from a live

1:52:15

Forex and Trade Advisor, the Forex website. Yaka stock markets may be. There are many such

1:52:20

stock APIs as well. If you want to maybe do something after the class for your, for your practice,

1:52:26

this is actually a very, very popular API for stock markets, Alpha Vantage. So we are

1:52:31

talking so much about APIs today, you know, like, money control can be API

1:52:37

have multiple, money control is such a popular, you know, a website, you know, like in our country,

1:52:44

India. Money control also exposes an API. You can see this one. Money Control API is there.

1:52:51

their third party APIs are available. You can scrape live data, but this is the very, very popular

1:52:56

one. You can get a free API key and you can similarly get information about stocks from here.

1:53:01

But we are simulating a simple demo. This is a simple demo where you're connecting to

1:53:06

a API.prangporter. And what are we trying to do? We are trying to get the live exchange rate of

1:53:12

US dollar and Indian rupee. And based on that, our LLM will act as an international trade advisor.

1:53:19

So the objective is that I want to go to that API call, make an API call, get the live

1:53:25

USDA INR exchange rate. Usd INR exchange rate. And based on that, the language model will give some advisory

1:53:30

information. So USD INR, you know, you know, the USD INR's latest 94.29. So

1:53:36

sort of, excuse me, a little sort of improved was very high sometime back during the Iran war.

1:53:45

But I think now it has dipped quite a bit. Rupi is, has improved quite a bit over the last

1:53:50

few weeks. Okay. Now that the peace deal will be signed. So now what we are doing is we are making

1:53:58

our requests to the 4X. We're getting a response. Same story. Jason to dictionary

1:54:03

convert Kyi up. Building the prompt. Based on that, we are building the prompt. And this is

1:54:08

that final thing that we want to do. Right of 50 story executive advisory to a U.S.-based client,

1:54:14

should they hedge their currency this based on this rate? So it's a little technical. You need to know

1:54:19

forex and currencies and all that. But I think at a high level, it is like saying that, as you

1:54:24

just as you have stocks carry such as currencies be carriages. A lot of people buy,

1:54:28

So it's like saying, okay, I will buy 100 shares of reliance. And it is like saying,

1:54:34

I will buy 100 US dollars. Like so, and you will hedge that.

1:54:38

I mean, that push go hold. So that next time when rupee again falls, you will sell it. That's the

1:54:44

idea. So just the stock price barred. So again, the technicality doesn't matter, but the use case

1:54:49

matters here. Again, you can see we are fetching the real data. You can here

1:54:54

print you can actually print the 4x data whatever is retrieved here. This is very interesting.

1:54:59

You can actually see whatever information is retrieved.

1:55:02

There are a lot is one. Base is USD. Date is this and INR is 94.67. These are real time.

1:55:08

There are real time. So different APIs can give for a fluctuation. But you can see it's almost real time.

1:55:16

Okay. So data is. So it can, I think it takes it at certain intervals. So our intervals

1:55:21

So Google is completely real time. It is giving it a completely real time, but this is

1:55:26

giving you at some fixed intervals. It is almost similar only, 94.67 objects and this rate will

1:55:31

also vary. And based on that, you are getting this particular response on the LLM. Okay. So there are

1:55:38

two such API calls were making you. You want to see a small, you know, example of an error.

1:55:44

I wanted to simulate an error for you. Just to, just to simulate an error for you. So versatile

1:55:50

the name change. Let me simulate an error for you. And this is a error code 404 error.

1:55:56

This is what I was talking about. So story remains the same. You are sending a request to the grok.

1:56:00

You're getting a response back. But you can see that I'm I gave a different model name. So a wrong model

1:56:07

name triggers a 404 error. This is like what a response error code basically stands for. Okay, just

1:56:13

wanted to simulate this for you. And another kind of error that people usually reported a lot in the last session was

1:56:19

this are API key not are. API key. So API key issue is basically like if you know, so what about that API key one? So the API key also, if you give a wrong API key, you will get a error code as well. The same way you can simulate that. I've got one last example, which is with respect to GitHub API. You can take a look at this also. This is also very interesting. The GitHub API, you can take a look at it.

1:56:49

And if you take a look at it, what we are doing is we are connecting to the official GitHub API.

1:56:55

GitHub gives your official API to you free. And you can connect to any repository, any report, any code repository.

1:57:01

GitHub in people basically use GitHub to post their code.

1:57:07

You have some code, even this course, let's say. We also have a GitHub repository at Maasai.

1:57:12

We upload all our contents there and we maintain all our contents there. So we also have a GitHub repository, which is

1:57:19

openly shared. So GitHub is very, very popular across the world. And even for all of

1:57:24

you students, one of the things that we recommend is have a good GitHub repository, have a good

1:57:30

GitHub profile. Because, you know, tomorrow when you go for interviews, people will ask you what

1:57:34

you have done. And then you don't have to tell what you did. You can actually show. Like, so the

1:57:40

traditional way of using resumes is gone. So resume is useless today. For resume, to do chat

1:57:47

GPT may be. Now, two lines litiged all, all resume been made. So companies have also realized

1:57:52

that, that the resume is very easy to create. The resume in

1:57:56

no effort not. But that's got a bit of effort

1:57:59

like that. So we are seeing a lot of enterprises going back to traditional modes of hiring today.

1:58:04

Because AI has made things so easy nowadays that you, that during evaluation, we really want

1:58:11

to find people who are putting that extra effort. You're how to find for them? You're going to find for

1:58:16

you know, interviews are also changing and this is one of the ways like try to build projects,

1:58:22

try to, because there are also people will argue that project be too. There are also people will argue,

1:58:26

that project be to chat GPT in Germany, I made, Jmini, I said, but

1:58:30

okay, effort to look right. You're still, somebody has to still run that code.

1:58:36

Guys, yeah, remember, generating the code is easy.

1:58:41

Is it? Generating the code is easy, but to execute that code is another matter altogether.

1:58:46

Code run be on. Gemini, you guys are using it all this while.

1:58:50

Gemini is not a guarantee that it will generate perfect code for you.

1:58:53

No, Germany will often make mistakes.

1:58:56

So many times Germany makes mistakes.

1:58:58

There's no guarantee generally Germany will give you correct code.

1:59:00

But now the important thing is how you're able to generate that code.

1:59:04

Yes, feel free to use AI tools, generate that code and then build an application,

1:59:09

build a small application.

1:59:10

Like today we saw some so interesting cases.

1:59:12

Let's say, uh, up a pick application banow it.

1:59:14

Something like that.

1:59:15

So let's say we did that stock market wall of things,

1:59:19

for X's what basis where you can build a small application

1:59:23

and you can build a small like a demo, a small proof of concept.

1:59:27

And this could be a nice takeaway from the class.

1:59:29

This is how I really will encourage all the students to go ahead.

1:59:34

Like whenever you have every session, there'll be some takeaways.

1:59:37

Those basis where you create a GitHub repository, okay, with your ID.

1:59:43

And then by the time you complete, you will have,

1:59:45

like 10, 15 ready projects.

1:59:47

The next time anybody asks you, what is your resume?

1:59:50

Your resume is your GitHub repository.

1:59:52

All the things you've done now, okay?

1:59:54

Yeah.

1:59:55

So this is what basically a GitHub repo is.

1:59:58

And you can go to, let's say, Facebook React.

2:0:01

Facebook React is one of these GitHub repos that are there.

2:0:04

You can see this one.

2:0:06

So Facebook React is one of these GitHub repos that are there.

2:0:10

Okay.

2:0:11

And we want to connect to that particular, you know, GitHub repo.

2:0:14

And we want to extract some.

2:0:15

information out of it. That is what we want to do. So same story. We will basically

2:0:20

make the request, API request to the GitHub, get a JSON response back. And I want to show you

2:0:27

what that Gid JSON response is. It will be a massive response. A lot of information will be there.

2:0:32

I don't need all that information because there'll be too many tokens. I only want to extract the name,

2:0:37

the Stargazers count.

2:0:39

But there are a lot of concepts around that. I don't want to get to GitHub session right now.

2:0:44

but how much stars, say, and all that you can crack.

2:0:47

Basically, how many people have rated and all that.

2:0:49

How many force count?

2:0:50

What is the language?

2:0:51

And you want to only fetch this information.

2:0:53

Okay?

2:0:54

And now this is,

2:0:55

after you fetch that information based on that, you're writing a prompt.

2:0:59

Okay, you are evaluating technology stacks for a new enterprise project.

2:1:03

Write a 50 word executive summary concluding whether this technology has enough community support.

2:1:08

So based on all the information like count and forks and all that,

2:1:11

force is also a very popular one,

2:1:12

so 885 forks says.

2:1:14

I mean, a lot of people are using it and all that.

2:1:17

So, okay, let me pull the information.

2:1:19

You can't see, this is all that GitHub is giving back so much, so much.

2:1:23

ID, node ID, okay?

2:1:26

Avatar URL, there's so much.

2:1:29

I mean, we don't have to get into all this, follower URL, start URL, subscriptions, URL, there's so much, right?

2:1:35

All these are URLs.

2:1:36

Then there's then after user view, description here.

2:1:39

Okay, if you keep scrolling, GitHub has returned so many things.

2:1:43

So many things.

2:1:44

Go all the way to the right and here you will start to see those numbers.

2:1:47

Can you see forks dig re?

2:1:49

51065, open issues, watchers, default branch.

2:1:54

So this is basically what APIs are.

2:1:56

Abdek Sakthi.

2:1:56

There's so much information we are getting back.

2:1:58

We don't need all that.

2:1:59

Forse that dictionary, get only what you require.

2:2:02

Put it in a prompt and get the response.

2:2:05

So this is how you can really build connected systems now.

2:2:07

Now the story becomes, you know, starts becoming very, very interesting.

2:2:11

Okay, so whatever we have seen in the class today, Abdecki, Sakti.

2:2:13

So we made an API call.

2:2:16

We got some response.

2:2:17

We're building the prompt.

2:2:19

We are making another API call.

2:2:21

We get some response.

2:2:22

And we take that response.

2:2:24

We make another API call.

2:2:25

So this is how we are able to build a very, very connected system over all.

2:2:30

Okay, I hope the general concept is absolutely clear with everybody,

2:2:33

whatever we achieved here.

2:2:36

Okay.

2:2:38

So, yeah, that is pretty much what we have here for today.

2:2:42

This was the final demo.

2:2:43

And all the.

2:2:43

contents are part of your Google Drive under the 24th June folder French.

2:2:48

Everything is part of the Google Drive under the 24th June folder.

2:2:52

And this is to summarize whatever we discussed in the session today.

2:2:56

We talked about REST APIs. We talked about APIs.

2:2:59

We talked about how client applications communicate with REST APIs.

2:3:03

Through a lot of real world examples, we saw that.

2:3:06

We understood how to read and write JSON.

2:3:09

JSON. Dot load gogear.

2:3:11

JSON.com.

2:3:12

Jason. Dot load is to read.

2:3:13

JSON.Dump is to write.

2:3:15

We talked about that.

2:3:16

We talked about executing a get request.

2:3:19

Get request library in Python.

2:3:21

Say how case you?

2:3:22

We saw the request or get function.

2:3:25

And we were also able to connect the dots with the grok request that we are doing.

2:3:29

And finally, we were able to map JSON fields into variables.

2:3:32

Why are we doing the last thing?

2:3:34

We are doing the last thing because, as I told you, a typical JSON response that you're getting really huge.

2:3:40

It's a last one of GitHub where I showed you.

2:3:41

Like this, easily like a million, like, like,

2:3:43

100,000 tokens will be there.

2:3:45

That's not that. I mean, the information I need is only a few things.

2:3:49

Like how many folks, how many followers, how many stars, that's it.

2:3:52

I don't need so many other things.

2:3:54

So only fetch what is required and map it to a prompt.

2:3:57

So these were the key takeaways from the session for today.

2:4:01

Okay?

2:4:02

Yeah.

2:4:03

Okay, everybody followed.

2:4:05

All of you clear.

2:4:06

So this will be all for today.

2:4:08

Any questions, anybody wants to ask me?

2:4:10

The contents are all here.

2:4:12

So you will see the,

2:4:13

a lot of interesting demos we had here.

2:4:16

And maybe one exercise and activity for everybody would be, you know,

2:4:20

how you can maybe think of some other APIs.

2:4:24

I say Indian stock market like API search through.

2:4:26

This could be an activity for you.

2:4:27

So today I showed you the USD-I-NR-Forex-Q-Q-A-Pi.

2:4:31

But I've given you some APIs examples here.

2:4:33

So maybe your activity will be, you can use a bit of Google and you can search a stock market

2:4:38

API, NIFTI-Kai API search for, and maybe get the latest information about.

2:4:43

Indian stocks, stocks to information patch, maybe that could be an activity you can do.

2:4:47

So you can build an API call where you're fetching the live stock prices for some stocks,

2:4:54

and based on that, you want to do some activities.

2:4:56

So this could be a very simple exercise you can do after this class.

2:5:08

What do you mean, credibility of the API?

2:5:10

Part of that is to kind of go back.

2:5:13

and, you know, you need to go back and, like, whether it's official API or not, like,

2:5:19

yeah, that's, some part of it is basically Google.

2:5:22

Like, you can ask me, sir, how do you know this?

2:5:24

This we have got, I know it, a little bit of search also I did.

2:5:28

So you cannot remember and memorize it.

2:5:30

So one part is you need to search.

2:5:32

You need to know what is provided.

2:5:34

Like, stock markets' the API, you know, how can't tell you.

2:5:37

No, no, how.

2:5:38

You have to search, Google search, Google search, search for, chat GPT, me search for.

2:5:41

And second part of your question.

2:5:43

and Gourteg is a credibility.

2:5:44

Credibility, to some extent, will be based on the official sources.

2:5:48

That's, well, way, so there's no, answer no, but, like, you know,

2:5:51

just you know, if you ask you, sir, is this credible?

2:5:54

Answer is no, it is not.

2:5:55

It's a free API.

2:5:56

So free API, the free API, never credible not.

2:5:58

Because it's there could be some issues or something.

2:6:00

I don't know.

2:6:01

Maybe it might respond with something else and, you know, you're sending data somewhere

2:6:06

where it's not secure.

2:6:09

So it's not that credible.

2:6:11

It's great for a demo, it's great to understand.

2:6:12

is not that credible.

2:6:13

So credibility, so you have to use the paid sources.

2:6:16

So lot of that will come back to the official documentations and what kind of security

2:6:21

they are using, community usage, what is the community talking about it.

2:6:24

So all those things will happen.

2:6:25

But a lot of this will be research, basically.

2:6:29

Take a good thing.

2:6:30

These are the free APIs.

2:6:31

So free APIs will be like, you know, just for learning purpose, just for demo purpose.

2:6:39

Okay, great.

2:6:40

Any other questions, guys?

2:6:41

I hope everybody followed the class today.

2:6:52

Okay.

2:6:53

Okay, great.

2:6:54

If there are no other questions, thank you.

2:6:56

Okay, yeah, what's that?

2:6:58

Okay, yeah.

2:6:59

So thank you, everybody.

2:7:00

Thank you, all of you.

2:7:01

Once again.

2:7:01

I'll pass it over to Pratak for taking the session forward.

2:7:05

Sheikh, you have raised your hand.

2:7:06

Do you want to ask something to me?

2:7:08

I can take up the questions in the,

2:7:11

meantime. Yes. And I think in the meantime, Pratap, you can launch the phone and you can get

2:7:17

started with the other activities. Yeah, Shakey won't you want to ask something. I'm here.

2:7:21

Yeah. All right, sir. Thank you so much. I will start the poll. If anyone has any questions,

2:7:28

you guys can ask. Sir, I'm here. If you want to ask me anything. Yeah. Oh, I thought Shaiky wanted to

2:7:34

ask because your hand was raised. Tiki. Perfect. Perfect.

2:7:38

Go-lo. T'i. Okay. Okay. Okay. Okay.

2:7:41

Thank you guys. Thank you so much, all of you. And I will see you in the next session.

2:7:46

Okay. Good night, everybody.

2:7:50

All right. Good night, sir. And students, the poll is up. Please make sure to vote.

2:7:58

Once you have voted, we can start with the Mentimeter quiz.

2:8:11

There are four, four, five students left. Please make sure you vote.

2:8:41

Is there anyone who's not able to see the pole?

2:9:11

4 people have not answered.

2:9:15

All right.

2:9:22

Okay. Chandini is not able to see the poll.

2:9:32

All right. I'll just, I'll try to report this.

2:9:36

Some people are not able to see the poll. Okay. In that case. All right. I'll just, I'll try to report this. Seems some people are not able to see the poll. Okay. Okay. All right. In that

2:9:41

Uh, okay. All right. Seems everyone has voted whoever is here.

2:9:46

Um. Okay. We can start with the Menti meter quiz in that case.

2:9:53

All right.

2:9:57

So students please join the Menti meter quiz.

2:10:03

I can see only five players so.

2:10:11

Okay, yeah, 13 of 13 are voted. All right. I am ending the poll now.

2:10:18

Okay. All right. Great. Anyone else who wants to join?

2:10:41

I'll wait for two more minutes or maybe one minute.

2:10:51

Okay, no, I'll wait for two minutes and students, please join the Mentimeter request.

2:10:57

So I am looking for around seven or eight players at least.

2:11:02

Yeah, Gourthik, you have your hand up.

2:11:11

Okay, no mind.

2:11:18

Yeah, yeah, that's okay.

2:11:21

30 seconds more I'm waiting, students.

2:11:26

You know, you can join the Menti meter quiz and it's fine if you don't score at the top, right?

2:11:38

So the effort, the effort, the...

2:11:40

the attempt matters. That's the more important part.

2:11:48

And I mean it's anonymous, so it doesn't really matter.

2:11:58

Alright, fine. I am going to start the Menti MENT request then.

2:12:04

Okay.

2:12:10

Alright, first question.

2:12:16

Which status code means okay?

2:12:20

Which status code means okay?

2:12:35

Just give me a second.

2:12:39

All right.

2:12:40

Okay, move on. Next question.

2:12:56

Um, what is the...

2:13:01

Yeah, okay.

2:13:09

Adjacent object maps to which Python type?

2:13:18

So in Python you have different, different...

2:13:22

Wow, that was fast.

2:13:24

Yeah?

2:13:26

Yeah.

2:13:27

I mean, okay, fair enough.

2:13:29

I did expect this question to be very easy for you guys.

2:13:33

So, um, okay, all right.

2:13:37

The last three questions are not going to be so easy though.

2:13:44

So let's see.

2:13:49

With status code means rate limit.

2:13:52

Now this is something you guys have already run into a couple of times.

2:13:57

So...

2:13:59

Okay.

2:14:01

I think everyone will get that correct as well.

2:14:04

Okay.

2:14:05

Wow.

2:14:06

Wow.

2:14:07

You guys are on a roll today tonight.

2:14:11

Everyone is getting everything correct.

2:14:14

Let's see, maybe the last question will be enough to create some gap.

2:14:28

Last two questions.

2:14:32

Jason.

2:14:33

Dot load S converts what?

2:14:36

Again, pretty simple question.

2:14:43

This is, so the way to read this is JSON.

2:14:48

Not JSON.

2:14:50

Not.

2:14:51

It is JSON.

2:14:52

.

2:14:53

When you read it as JSON.

2:14:55

Dot load S, you get a very good hint of what is going on.

2:15:05

Yes.

2:15:06

So load S stands for string.

2:15:09

So you are loading a string to JSON.

2:15:14

So that's a very good way to read it.

2:15:17

Instead of reading as loads, you say load S.

2:15:21

And read or there will be also JSON.

2:15:25

dot read.

2:15:26

There is JSON.

2:15:27

.

2:15:28

So that is also similar to that.

2:15:31

Status to body is not correct.

2:15:34

Status will be something like 200 or

2:15:35

like 200 or 400 and you can't convert that to body.

2:15:39

That's completely wrong.

2:15:42

All right.

2:15:47

We have one more question left.

2:15:51

This one is slightly difficult.

2:15:57

I think most of you should get it.

2:16:01

If the API code is 200 and 10,

2:16:05

temperature is 28 degrees Celsius.

2:16:07

But the LLM still says it's 40 degrees Celsius.

2:16:10

What is the most likely failure?

2:16:13

This one is a little difficult.

2:16:16

Read the options carefully and understand.

2:16:19

Why?

2:16:21

Like, find out the correct answer.

2:16:25

The options are also tricky in this one.

2:16:31

So, yeah.

2:16:34

Okay, I am guessing most of you will be...

2:16:39

Oh.

2:16:40

Oh, interesting.

2:16:43

Okay.

2:16:44

So I expected you guys to get confused between JSON syntax and generation grounding.

2:16:52

But it seems you guys are confused between the rest endpoint and generation grounding.

2:16:58

So generation grounding is correct because the temperature is 28 degrees Celsius, but the

2:17:03

but the LLM is saying 40 degrees Celsius.

2:17:05

That means LLM is probably hallucinating.

2:17:08

Right.

2:17:09

The rest endpoint is not a problem because API code is 200.

2:17:14

So if the API code is 200, that means the rest endpoint is working properly and

2:17:20

you're getting the correct data, 28 degrees Celsius.

2:17:24

But the LLM is not able to read this data or it is even if it is reading it's not,

2:17:30

it's ignoring it, something like that is going on.

2:17:32

on.

2:17:33

Right?

2:17:34

That is why this is the correct answer, Generation Grounding.

2:17:38

Rest endpoint is not an option.

2:17:40

I mean, it should be a easy elimination.

2:17:44

The more difficult to eliminate option is JSON syntax, actually.

2:17:50

Jason syntax, why is it difficult to eliminate?

2:17:54

Because your JSON, if your JSON that you're reading inside the LLM is expecting

2:18:02

something else then it is a possible problem but usually that is not going to happen

2:18:08

what is usually going to happen if the API code is 200 right that means your JSON syntax is

2:18:13

also correct because what happens is if so for example if you are if you're talking to a

2:18:18

weather API right and it is expecting latitude and nonitude but instead you give it

2:18:25

the name of a city for example okay so the syntax there is incorrect and so what you will

2:18:32

get is not a 200 code it will be some some error code that you will be getting in return.

2:18:39

So that is why JSON syntax is not not going to be the correct answer in this case also.

2:18:46

This is something I expected most of you to select.

2:18:49

That's why this was the more confusing option but it seems you guys are not sure about the

2:18:54

rest endpoint itself.

2:18:55

So fair enough, we will try to cover these things in the tutorial that has

2:19:02

happens probably in the next week regardless.

2:19:06

Guys, I would advise you to take your doubts and raise them in a tutorial session.

2:19:13

Even if it is today's session, you can raise those doubts in tomorrow's tutorial also.

2:19:20

So if I have time, I'll cover it.

2:19:22

I mean, I'll try to cover it as best as I can.

2:19:25

Okay. All right, with that, we are at the end of the session.

2:19:30

Let's see.

2:19:31

Interesting.

2:19:38

All right, congratulations, Sneha.

2:19:42

Yeah, Sneha is here.

2:19:45

Okay.

2:19:46

All right.

2:19:47

With that, we can end the session now.

2:19:49

Good night, guys.

2:19:51

Thank you so much for attending.

2:19:52

I will see you guys tomorrow in the tutorial session.

2:19:56

Okay.

2:19:57

Bye-bye.

2:19:58

Have a good night.