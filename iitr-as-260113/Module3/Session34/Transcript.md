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

Hi, everyone, very good evening to all of you, uh, welcome to the first session of module three.

14:27

Hope you had a very good exam yesterday.

14:31

We'll start in a couple of minutes.

14:34

Welcome Deepak sir.

14:35

Let others join.

15:05

Thank you.

15:35

Thank you.

16:05

Thank you.

16:35

Thank you.

17:05

Thank you.

17:35

Thank you.

18:05

Thank you.

18:35

Thank you.

19:05

Thank you

19:35

Thank you

20:05

Hi,

20:12

Hi, everyone.

20:13

Hi, everyone.

20:15

Hi, everyone, very good evening.

20:35

Folks, am I audible to all of you?

20:39

Hi, everyone, am I audible?

20:44

Okay, great. Good evening everyone and welcome to the class.

20:51

So today we have the new module starting up, right?

20:56

So this is module number three, right?

20:59

This is module number three, correct?

21:03

Great.

21:04

And with the new module

21:05

and everyone, we'll be starting with the first topic, which is running LLMs locally via OLAM. Okay? We'll be talking about that.

21:14

Right? So today's topic is going to be that how can we run LLMs locally with the help of OLama?

21:23

OLama, what is this tool all about? What functionalities does it provide us, right? We will be talking about that.

21:31

Just one quick disclaimer, everyone.

21:35

Today, I have a bit of fever for last two days, like from Saturday, Sunday, right?

21:43

I'm on heavy medication. I have already taken medication. So please bear with me.

21:48

If you just see some disturbance, I might be having a few small, small breaks in between, right?

21:56

Just for like a few seconds, just to, I hope you get it.

22:00

Right? So please bear with me.

22:02

Right?

22:04

Yeah.

22:05

having all the discussion, just bear with me for today's class, right? Hopefully by Wednesday's class, I'll be fine. Okay? Yeah, I did not want to leave the class because today's topic is not that difficult, everyone, and the content is also not too much, right? Olam is relatively easier topic, right? You just need to understand a few constructs about OLama, and it is very, very similar to how you call open AI APIs, right? The only thing that is going to, that is going to be different is that how do you make a comment?

22:35

all, right? The concepts are not at all different. Concepts are absolutely the same, right? Some part of coding is going to change. So that's why I thought that, okay, let's do the class. Let's take the class. Okay. Yeah. Thank you. Thank you, everyone. Okay. So let's get started with Olamma. Okay. So first of all, everyone, as of now, in our applications, have we already used LLMs? Have we already used LLMs?

23:02

tell me. Absolutely yes, like 100 times, right? The tens of times we have already used. And LLMs stand for large language models.

23:14

Large language models. So, folks, how we have used LLMs as of now. Can you tell you? How we have used LLMs as of now?

23:29

in our previous classes, how we have used them.

23:35

When I say how we have used them, I meant where they were running and how we were able to talk to them.

23:41

Absolutely correct via API call. Okay? Via API call. So folks, we have already used LMs from OpenAI.

23:53

Okay. We have already used LMs from OpenAI, Gemini.

23:59

or Claude? Right? So if all of these LLMs are the pro-prioritry software, right,

24:09

these are the softwares, these are the LLMs owned by a different company. And they are not freely available.

24:15

It's not like that. You can download them in your machine. You can directly use them, right? It's not like

24:20

that. If you want to use Gemini or Claude or OpenAI, you'll have to properly create an account on these platforms.

24:27

For example, let's say Open AI. Go to open AI. Go to open AI.

24:29

Go to chat gpte, whatever is the website, platform.com. Create an account. After creating

24:36

an account, you will get the API key. That API key is like your username password, right? That

24:41

API key is like the unique identity about the user. Whether you have money in your account or not,

24:47

whether you have subscription or not, that everything will be identified via API key. For example,

24:53

let's say everyone, if I'm trying to use GPT 5.5.2 or GPD 5.5, I think the latest version,

24:59

is 5.5 now. If I'm trying to use GPD 5.5 via API call from my Python script,

25:07

right, and if I give my API key. Now, this model, this GPD 5.5, is not a free model that everyone

25:15

can use. This is a paid model. For this, you need to have the premium subscription from chat GPD,

25:21

from OpenEI. Now, guys, how, when I make an API call, how open AI will identify whether this user is

25:27

eligible for this particular model usage or not? How GPT will check? How open I will check that?

25:39

Tell me via API key. Correct, everyone? So what you do, everyone, is, so basically what happens,

25:49

when you set API key, so there are like two, three ways in which you can set the API key. So, for example, when you

25:54

create the client, when you create the client, you do.

25:57

something like this, client is equal to open AI. So from, first of all, you will have to

26:04

install open AI. It is like open AI gives you the software development kit SDK for every language,

26:11

for every technology. For example, you can use open AI in Python, Java, C, C++, etc. Right? Whatever

26:17

language you want to use in, you will have to check, you will have to import it. You will have to

26:21

install it. Right. And once you install it, everyone, you can create. For example, if I take an example of

26:26

Python, you create a client object for open AI, client is equal to open AI. And then

26:33

here everyone, you do what? Here you provide the API key. Correct or not? Here you provide the API key.

26:41

Yes or no? Now everyone, if you provide API key here, then what it will do? Then it will be

26:51

exposed to the code base, right? It will be visible in your code base. Right? Anyone can see this.

26:56

that. If you upload your code base on GitHub, then everyone can see that. So instead of that,

27:01

everyone, what do we do? So, instead of passing the API key, right, at inside the function,

27:09

manually, what you do is, we set the API key, set API key in environment variable.

27:19

That is the best way. In environment variable.

27:24

Folks, yes or no? So folks, when you set this inside the environment variable, right? For example, in Mac operating system or Linux operating system, the command is export. Okay? So export. Now, one thing to note here everyone is, let me write it down. Open AI API key is equal to something. Right? You give the API key here.

27:54

When you run this command on your terminal, this API key is set as your environment variable

28:01

in your laptop. Now, first of all, everyone, when you set it as an environment variable, and after that,

28:06

when you create an object of open AI client, you don't have to pass it here. No need to pass it here.

28:13

When you create an open AI object, open AI client object, it will automatically check. Do you have

28:19

the variable value, value of this variable set? Now, one thing that you,

28:24

which is very, very important here, everyone, is that you need to make sure that the name of this variable is exactly the same.

28:29

For example, if you change the name of the variable, then OpenEI client, OpenI object, this function will not be able to recognize whether you have given the value of this API key variable or not.

28:40

Makes sense to all of you?

28:45

So, you can set the value of this variable and OpenEI object, while creating the object of OpenA, it will automatically read the value.

28:52

Now, everyone, after this, after this, you can set the value of this variable.

28:53

After that, whenever you make a call using this object, client dot, what was the API name, client dot responses dot, this responses dot create, right?

29:09

Whatever API call you will make here, model, etc., all the input parameters you will pass.

29:15

Whatever API call you will make, this API key will automatically go inside this request.

29:20

You don't have to pass it again and again.

29:22

Why? Because this client has that API key value embedded. Does that make sense to all of you?

29:28

This client object has that value already embedded inside it. Correct? Make sense, everyone?

29:37

Right? Then everyone, whether you are able to, whether you are eligible to make this request or not, do you have, for example, let's say if you're trying to make a, like here you are passing the model, which is the paid model.

29:49

Right? So how GPT will check, how OpenA will check that?

29:52

whether you are eligible for that usage of the model or not. Because you are passing the API key,

29:57

it is kind of a token, kind of a, you can say that, a role number or an ID. Right? So open AI key,

30:03

open AI, what will do? It will go to the database and it will check. First of all, it will check that

30:08

whether this API key is a valid, valid key or not. Then everyone, then it will check that, does this

30:14

API key has a paid subscription or not? Then it will check that whether this API key has the value present in the amount or not.

30:22

Like some amount present or not, if that is a paid API. Are you guys getting this point?

30:26

So it will check all the things and then it will tell you whether this excess is present or not.

30:31

Sounds good, everyone.

30:34

Folks clear. So guys, all of these models, all of these models, right? And a lot of other models also,

30:40

Facebook model, et cetera, et cetera, meta also gives you a lot of models.

30:43

OpenAI, Gemini, Claude, Grog, et cetera, et cetera. All of these are, all of these are proprietary models.

30:51

These are not freely available models for using these models.

30:55

You'll have to create an account. You'll have to set the API key and then you will be able to use them.

31:00

And even now, one more important thing is, when you use OpenAI or when you use Gemini or anything like that,

31:07

you are accessing them via API request, via API request, via API call.

31:14

Correct?

31:15

Now everyone, when you make API call, where these models are running, where these models are running, where these

31:21

models are running. Where these models are running, so you are able to access them via

31:28

internet. If you don't have internet, will you be able to call Open AI API? No, right? So what

31:37

you do? You have your laptop, right? You are running some code here, and this code is triggering

31:44

an API request.

31:51

This code is triggering an API request and the request goes to some data center, some cloud.

31:58

That cloud can be present in US, Singapore, Australia. You never know that.

32:03

What these companies does everyone is, for example, let's say if you talk about Open AI, definitely

32:07

they will have one major data center in US, right? Let's say maybe in Seattle or let's say in California.

32:13

They will have one major, biggest data center. But everyone now, Open AI is such a big company that

32:19

everyone in the world, every part of the world, people from every part of the world,

32:24

they are using open AI. If they have only servers, if they have the servers only in one part

32:31

of the world, let's say in US, do you think that they will be able to serve such a big traffic?

32:37

Do you think so? Right? For example, everyone, let's say this is the entire world map, right? I am

32:44

sitting here in India and they have data center here. Now everyone, if my request, from

32:49

from my laptop sitting in Delhi, if the request goes to very, very far away, somewhere

32:54

in US, then server will get the request, server will process the request, and then server will

33:00

send the response back.

33:02

This is request.

33:03

Guys, just give me a second.

33:07

Just give me a second.

33:19

then server will process the request and then server will give the response back.

33:23

Don't you think even it is going to take a lot of time, right? Because everyone, what happens is

33:28

latency. The time taken by the request, that is latency, is directly proportional to, directly

33:35

proportional to the distance. The request is traveling. If the distance increases everyone,

33:43

don't you think every request will be very, very slow? Correct or not? Request will be very, very slow.

33:49

And everyone, obviously, if the requests are slow, right?

33:51

If you are taking, let's say, if it is taking two minutes for a simple response to come,

33:56

do you think that people will prefer Open AI or any platform for that matter?

34:02

Do you think so? Absolutely not.

34:04

So, that's the reason, everyone, that all of these major companies, right?

34:09

They don't have data centers running only in one part of the world.

34:12

What do they do?

34:13

They copy their servers.

34:15

They place their servers in different parts of the world.

34:18

They will play.

34:19

servers in multiple at multiple locations in US, at multiple locations in India, for example

34:24

Mumbai, Chennai, Delhi, etc. They will place multiple servers in Singapore, China, etc.,

34:30

etc. So that if I am sitting in Delhi, my request need not to go to US. My request will go to

34:36

my nearest data center, right? That their server will automatically identify that where the nearest data

34:41

center is present. Are you guys getting this point? Right? Now everyone,

34:49

the request goes to some cloud. And this is what is called as cloud. Cloud is a imaginary

34:53

thing which is distributed across the world, right? You don't know, you, you really don't know exactly

34:58

where that request is actually going as a user. As a company, definitely, you know that. Where we are

35:05

serving the requests from. But as a user, you have very limited understanding of that, right? Because they

35:10

have a lot of internal tools, because they will, for example, let's say if I am sitting in Delhi,

35:14

my request might be served by the data center present in Delhi. If you are nearby Mumbai,

35:18

your request will be served by the nearest data center present nearby Mumbai.

35:22

So how do they identify? They identify with the help of IP address, your internet service provider.

35:28

That where this user is actually located. Makes sense, everyone? And they will find out the nearest

35:32

data center and they will serve your request because if your request is traveling lesser distance,

35:38

obviously your request will be faster. You will get response very fast. Sounds good, everyone.

35:42

So you get the response, you make the request. Your request goes to the data center.

35:47

This data center, everyone.

35:48

If using VPN, then it is a tricky thing. For example, if I'm using VPN of some different

35:53

country, then the request will go there. For example, even now, this actually happens.

36:00

For example, let's say a lot of people does what? If, let's say there is some movie, which is not

36:04

released in India, but that is released in, let's say, Australia. So what do they do via Netflix?

36:09

You connect Australia VPN on your laptop and then you go to Netflix. And then you will be able

36:14

to watch that movie. Because everyone, then Netflix will assume.

36:18

that your request is coming from Australia server or Australia's internet, Australia's IP address.

36:25

VPN is a way to fool these companies.

36:29

Makes sense, everyone?

36:30

A lot of websites which are not accessible in India.

36:33

If you use a VPN, you can access those websites.

36:36

Make sense, everyone?

36:39

Okay.

36:40

I'm talking about other 99.99% of the scenarios that your request goes to the cloud.

36:46

Now, guys, cloud is everywhere in the world.

36:50

Your request goes to the cloud and then you get the response back.

36:54

Are you guys getting this point? Yes or no.

36:58

This is when everyone, we are using LLM models from third party providers, which are paid models.

37:06

Everyone, clear?

37:07

But everyone now, there is another way also.

37:10

There is other way also that you can run models locally also.

37:16

Now there is a very big point that I'm going to claim now that we can also run

37:22

large language models locally.

37:32

Is that point clear to all of you?

37:34

We can also run LLMs locally.

37:36

But everyone, does that mean that you can run open AI locally?

37:42

Can you run open AI locally?

37:45

Can you run open AI locally?

37:46

Claude locally? No. If these models are not available to download, how can you run them

37:53

locally? To run a model locally, you will have to download that, right? You will have to download

38:01

the model. But everyone, if something is not available to download, if they are private models,

38:06

right, they are running on cloud, they are running on open AI servers, they are not allowing you to

38:11

download. So how can you use it? So guys, you can only use LLMs locally, which are freely available.

38:16

to download. These are called as open source models. Are you guys getting this point?

38:21

These are called as open source models. So, guys, in today's class, I will literally show you by downloading

38:26

a model in my laptop. You can also do that very, very easily. It's just like you'll have to execute

38:31

two, three commands and you'll be able to do that. Very, very easy part of work. Once we download the

38:38

model locally, it is running on my hard disk. It is sitting on my hard disk. It is running on my hard disk. It is running

38:42

on my RAM by my CPU. It is that.

38:46

simple straightforward process. Are you guys getting this point? But everyone, this thing is

38:51

very, very important that we cannot randomly run every and any model locally. That model

38:57

should be freely available. That model should be open source. Now, what is O-Lama now? O-Lama is a tool

39:05

that gives you the functionality to download these models and to use these models in your local

39:12

machine. For example, everyone, it is kind of a marketplace. For

39:16

example, even let's say think of Amazon, right? Or think of, maybe, think of Amazon.

39:21

Okay? Now, guys, what Amazon has done? Can I say that Amazon has brought thousands or millions of

39:27

world's sellers together? Correct? Even if today I want to sell any item. I can list my

39:34

company on Amazon and I can start selling the items. This is what Amazon has done. For example,

39:39

even now, if you have, let's say, 100 different models, let's say 100 different models, which are

39:45

freely available. Now, everyone, if you want to use those models, don't you think you'll have to

39:49

identify, first of all, you'll have to understand the documentation, that how this model I can use,

39:54

how can I use this model, how can I use that model? Then every model might have different way of

39:59

usage, every model might have different way of downloading, etc, etc, right? So it will be very

40:05

difficult, it will be very inconvenient for a normal user to understand the functionality, way of

40:12

downloading, and the usage of every individual model.

40:15

one by one. Correct? What O Lama does? O Lama is like Amazon. So O Lama brings

40:23

support of hundreds of open source models together and now instead of talking to these models

40:30

individually, you can talk to O Lama. You can tell O Lama that hey O Lama, I have, I want to use this

40:38

model and this model you have on your platform. So please download, I want to download this model

40:43

on my laptop, please allow me to do that. Please do that for me. So I will talk to O Lama and

40:50

O Lama will automatically take care of internal handling. Makes sense everyone? O Lama will

40:55

automatically take care of internal handling. Is that point clear to all of you? I'll come to that,

41:00

Shiva. I think it is just majority of a company's difference. I don't think there is a big difference

41:07

in them, but I'll still check that. Then it's mainly MCP of, you can think of that. Absolutely. What

41:13

saying that it is kind of MCP. Very, very similar to that, it is bringing the support of

41:18

multiple models together. Similarly, everyone, what MCP does? MCP, did we have lectures on MCP? Not

41:24

really, right? I think I taught that in a different batch, not in this batch. We will have, I think, a few

41:29

sessions on MCP as well. If you know, it is good. If you don't know, it is okay. We will have that

41:33

in the future. MCP brings the support of multiple external tools together. That instead of talking

41:39

to different tools via agents one by one, you can talk to them via MCP. So that if tomorrow

41:45

you want to change from one tool to another tool, you don't have to do a lot of changes,

41:49

right? You can just ask MCP to do so. Every complexity, every hidden complexity will be taken

41:55

care by MCP itself. Any minimum, I will come to that. Any minimum hardware required to run it locally.

42:01

Absolutely yes, 100% yes. It will be having a lot of hardware requirements. Now everyone,

42:06

there are models. I will talk about them in detail in some time.

42:09

Right. Very, very similar to that, Chira. But Olam is even more popular and there are some

42:15

differences between them. So folks now, coming to the hardware requirement, I will show you that

42:20

on the website also. There are few LLM models, there are few large language models that you can download

42:26

and use even if you have one Gb of RAM and some models can go up to 32 GB of RAM. For example, my laptop,

42:34

the MacBook that I'm currently using, that has 16 GB of RAM. Right? Definitely one. I need to have

42:39

I cannot download a model which will have, let's say, which would need 32 gb of RAM.

42:45

Makes sense, everyone?

42:48

You can say that different tools, right?

42:50

Different ways. That's it.

42:55

Both of these are different, different platforms.

42:57

Nothing more than that.

42:59

Folks, clear?

43:00

So definitely even every model will have different requirements, different number of parameters, different size.

43:04

For example, even my laptop has currently 256 gb of RAM.

43:08

Now, if I.

43:09

try to download Open AI. Do you think that Open AI has only open AI can sit in 250

43:14

gb of RAM? 2506 gb of hard disk, not RAM. If I have a laptop of MacBook of this much of RAM, then

43:23

that's a different story altogether, right? This is hard disk. This is a hard disk. Open AI must be taking,

43:31

I would say, let me check, size of...

43:39

latest gPT model.

43:46

GPT model.

43:48

Yeah.

43:50

So, opening has released.

43:51

Frontier model, GPD 5.5, like other advanced such as GPD 40, etc.

43:56

Does not publicly disclose, but expectedly it will have...

44:09

Exact parameters are unknown.

44:39

Folks, I think it is having 80 gb of GPU. It is not even like hard disk, GPU.

44:47

80 gb of GPU and even this is 04 Mini.

44:51

Like the hardware requirement is insane.

44:59

1 trillion bytes, which is around 0.7 tb, 700 gb.

45:05

So it will have like multiple terabytes of hard disk.

45:08

And then hundreds of.

45:09

GBs of RAM. Okay. So now let's come to Olamma, everyone. And let's come to everyone.

45:15

That tell me one point here. I will talk about all these things when we will go through the

45:19

OLAMA documentation. Tell me everyone that if I can use open AI or if I can use very advanced

45:26

LLM models on cloud like open A.E like cloud, etc. Why do we need to run LLM models, large language

45:33

models on local? Why do you think so?

45:39

What could be the major reasons that why, like what could be the requirement here?

46:09

local elements.

46:13

Okay, so guys, we will talk about some of the advantages, disadvantages, but all of these are going

46:19

to be relative terms. Now everyone, if you are running on your local machine, right, here we are going

46:24

to run on my machine, but think of as a company, right? Let's say maybe Masai company. Now, if I want

46:29

to, if let's say as a company, Masai wants to run a model locally, definitely when they will not

46:34

be running on one laptop, they will be running on multiple PCs, right? Still everyone, don't

46:38

think they will have to analyze that what cost they will have to pay for using, let's say,

46:44

open AI model and what cost do they need to pay if they are running some open source model on

46:50

their servers, correct? So always you will have to, you and also you cannot just compare basis on

46:58

the cost. If something is cheap, but that is not fulfilling your requirement, then there is no point

47:03

of it, right? Correct, everyone? Let's say if something is, let's say you have to pay $10,

47:08

and for something you have to pay $100, right? So you see that it is 10 times cheaper.

47:13

Good enough, very good. But everyone, if this particular thing is not even fulfilling a requirement,

47:17

you do you think this is not of any use, right? Correct or not? This is not of any use. So you

47:23

will have to see the utility, we'll have to see the availability, you'll have to see the usage and then

47:28

cost. Cost is not the only factor. There are a lot of other factors that comes into picture by

47:34

deciding which LLM to use, when to use, and should we use on local servers or should

47:40

we use on cloud, right? So the first thing that comes everyone is the most important thing is

47:44

privacy. Could you explain that security and privacy? That's for companies running large language

47:54

models on their own servers, how it can enhance security and privacy. What do you think about this?

48:04

So if a company wants to use some application on their local data, for example,

48:18

companies' policies information, there is some, let's say, finance company, there is some banking institute,

48:23

if they want to use Open AI, if they want to use some LLM model on their private information,

48:31

private data, don't think even if they are using Open AI.

48:34

or any model running on the cloud, they will have to share their data with them.

48:39

Right? Via requests, you are sending their data. And whatever data you are sending to Open AI

48:44

or anything, they are definitely going to store your data. Right. So guys, if you're not okay with

48:49

sharing your very, very confidential data with third party companies, obviously the only way

48:56

is running LLMs locally. Correct, ever? The only way is to run LMs locally. This is one very

49:03

important factor, before even cost, before even anything else, security and privacy is the most

49:08

important thing. Correct? Then everyone, cost control, cost can be one factor, but everyone cost,

49:15

for example, but we can use VectorDB using LLM via IPA. You cannot store everything on VectorDB.

49:23

For example, you want to train your model, you want to fine tune the large language model on your data.

49:31

Then what? Make sense?

49:33

Right? Fine-tuning means that LLM needs to know that information. And if LLM needs

49:39

to know that information, that information will go to Open AI and OpenAI will save that information.

49:44

That is technically, maybe the company might not be okay with sharing the information with the

49:50

Open AI servers. Makes sense? Second thing is cost. Now cost is a very, very relative thing.

49:56

Now everyone, we say that, okay, if you are using OpenAI, if we are using Cloud, then you will have

50:01

to pay the internet cost because you are making the remote.

50:03

More importantly, everyone, you'll have to get the subscription and you will have to pay per token.

50:09

Correct, ever? You will get limited number of tokens and for every extra token, you'll have to pay extra.

50:15

Correct, everyone? So that's why everyone's open AI, cloud, etc. They are very costly models if you're using at a very big scale.

50:21

Then everyone, you say that, okay, if they are very costly, let's use local LLMs. But everyone now, if you're using local LMs, don't you think there, the hardware requirement comes in?

50:32

Because you're not going to run local models in air.

50:35

You need infrastructure for that.

50:38

If not, see, if you're using OpenAI, who is taking care of the servers?

50:43

Who is taking care of the hardware? Who is taking care of the infrastructure?

50:51

Who is going to take care of the infrastructure in OpenA? OpenA. OpenA. That's why it is costly.

50:56

But everyone, if you are using local model, then you will be the one who will have to take care of the infrastructure.

51:02

you'll have to either buy the machines or you'll have to get the machines from AWS, etc.

51:06

Right? Don't you think even you'll have to pay the money for that?

51:09

Buying the machines, renting the machines. Also, you'll have to manage that also.

51:13

Management is also very difficult because your data is sitting on the server, how will you manage the data?

51:19

You need DevOps people, you need infrastructure people, you will have to hire people and those people will be

51:25

managing the data. That is also going to be the cost factor. So guys, after all these things, what

51:31

companies basically does. They don't go with one conclusion at the beginning. Because really

51:36

at the beginning, you really don't know how complex things are going to become in the future,

51:42

how much cost we are going to incur, et cetera, et cetera. So what, for example, let's say what company

51:46

might be doing, if let's say I have my company and we are using Open AI today, right? We have OpenEI

51:51

today. And let's say as a company, I will analyze that how much money we are paying to OpenEI, good enough.

51:57

Then everyone, I will, if I think that, okay, the money that we are paying to Open AI is big.

52:01

then everyone we will start analyzing that should we move to some different

52:05

LLM model instead of opening if even if that money is going out of the budget then we

52:10

will start analyzing the requirement of what if we start running a model locally for that

52:16

again we will also have to analyze that how much infrastructure going cost is going to happen

52:20

right after that again we will try for some time and some lot of times every everyone what happens

52:25

is even after trying locally the cost will be even very high not only cost everyone they

52:31

the headache of maintaining so much data, maintaining so many API calls, scaling the

52:37

infrastructure is going to be very, very difficult. You'll have to hire more and more,

52:41

more and more people to scale the systems, right? But everyone, if you're using OpenE,

52:45

OpenEII will automatically take care of that. Right. So, guys, final conclusion will be based

52:49

on multiple factors, right? Can we use infrastructure as a service using open eyes to tackle it?

52:55

Yes, you can do that, absolutely correct. You can get the infrastructure from, from Amazon.

52:59

You can get machines from Amazon.

53:01

You can get machines from Microsoft, right? But for that also you'll have to pay money.

53:07

LLM might be free. You might be using some open source LLM. LLM might be free. But running that is not

53:13

free. If you are running that LLM on some machine, you will have to pay for that machine. And if your usage is

53:20

very high, you'll have to buy a lot of machines. A lot of infrastructure will be required.

53:25

And you'll have to pay for that. And everyone, you will have to have, you need to have a lot of people who are going to manage.

53:31

this infrastructure. Which machine is up, which machine is not up. Which machine is running,

53:35

which machine is not running. Which machine is overconsumed? Which machine is less consumed?

53:39

How many machines do we need? How many? Like, are we not consuming more machines? Are we consuming

53:43

less machines? So a lot of things goes in. Are you guys getting this point?

53:48

Is Open AI enterprise versions ensure privacy and security, like data is not stored and shared over

53:53

the cloud? There might be different different policies, but as far as I know, for a normal user,

53:58

they store the data. Right? It is very simple.

54:01

definitely you can clear the data, right? I can go to the settings and I can clear the data,

54:06

but definitely they are going to store the data. But for different enterprise plans, they might

54:11

have different, you can say the different plans or different security layers that are we going to store

54:17

your data or like we are going to store your data in a separate server, right? As soon as the user

54:22

will ask, we can delete the data. There might be different, different, you can say that terms and

54:26

conditions, but you cannot guarantee that, right? But when you are running LL

54:31

on local, then you'll have 100% safety and security that my data is not going outside

54:35

my organization. Now, think about a banking application, think about a stock market application,

54:40

think about a very, very critical, let's say, the biggest hedge fund of the world. If that data

54:48

gets leaked, right, for any reason, right, then it can bring like, it can have a impact of billions

54:55

of dollars in a day. Right. But that's why everyone, these kind of companies, they have very, very

54:59

strict policy about their data. That data should not go out of the system at any cost.

55:04

They are okay to compromise the quality. They are okay to compromise whatever. But the data

55:08

should not go out of the system. Makes sense, Roger? It depends. It depends company to company.

55:15

It depends policy to policy and so on. Okay? Then everyone, third reason could be offline development.

55:23

So, guys, if your LLM is running locally, don't you think everyone, it is going to be relatively

55:28

faster than making an API call? It is going to be relatively faster than making an API

55:34

call? Absolutely yes. So guys, these are some of the factors because of which local deployment,

55:43

local LLM might be useful. And one thing which is very, very important is one, which is for building

55:48

some kind of learning project for your college, for your job, for your resume, etc. For learning

55:53

purpose, local LLMs are very good. As a student, you need not to pay anything.

55:58

run a very, like take a very small model, run on your local, and you are good to go.

56:04

You can build a very small project with your LLM model.

56:08

You can give a demo also in your college, etc.

56:10

Right?

56:11

Now let's talk about O-Lama.

56:15

That what is O-Lama now?

56:17

Local LNB, we all understand.

56:20

How to run, we will see.

56:21

Now, what is O-Lama?

56:23

O-Lama is a tool.

56:26

It is a tool.

56:28

O Lama is a tool.

56:42

That helps, that helps us run.

56:50

LLMs.

56:58

use them and use them. Makes sense, everyone?

57:09

if you see everyone?

57:10

LM is a tool that helps us run LLMs locally and use them. Sounds good.

57:16

Right? Now everyone O Lama also, like OLama also gives you two ways.

57:23

Right? So with OLama, for example, let's say, with OLama you want to use some open source LM.

57:28

Okay, that is free.

57:30

LLM is free.

57:31

That is built by some open source company.

57:33

But everyone, Olamma gives you both the ways.

57:37

Right?

57:38

OLama you can use on local or on cloud.

57:46

Now you say that okay, I don't want to pay for LLM.

57:52

I will use open source LLM via OLAMA, but at the same time I don't want to take the

57:58

the headache of maintaining the infrastructure.

58:02

Are you guys getting this point?

58:03

I don't want to take the headache of maintaining the infrastructure.

58:06

Then I can use that.

58:08

Hey, O Lama, I want to use some open source but via your cloud.

58:12

So it gives you both the functionalities.

58:14

Sounds good to all of you.

58:15

So in this case, everyone, if you go with O Lama with cloud,

58:18

right, you don't have to pay for tokens, etc.

58:21

Right?

58:22

You just have to pay for the infrastructure.

58:24

Whether you are running O Lama on one machine, on 10 machines, you'll

58:28

have to pay accordingly. But when you are using chat GPT, you are paying for LLM as well,

58:34

you are paying for infrastructure as well. You are paying for overall package. But when you're using

58:39

OLama with cloud, open source model with cloud, then cloud will be taken care by OLama company.

58:45

LLM will be free. You'll have to pay for the machines. You'll have to pay for the

58:49

infra or hardware. Is that point to all of you? Is that point here to all of you?

58:58

So guys, when you are using, when you run a LLM locally, you can say that while running while running an LLM locally via O LLM locally.

59:28

Right, we can say that while running LRM locally.

59:33

What OLama does?

59:35

Olamah behaves like a, it behaves like a,

59:52

running on our machine.

1:0:03

So folks, what happens if you have this, your laptop, right?

1:0:08

Let's say this is your Python project, okay? This is your Python application.

1:0:15

Right? And inside your Python application, what do you want to do? You want to do, let's say, let's say, let's say,

1:0:22

you have downloaded O Lama, right? So what O Lama does everyone? You have downloaded some LLM,

1:0:28

which is running on your local. So guys, now via your Python application, you want to use this LLM

1:0:34

model. Don't you think this is also going to act like an API request? The only difference is everyone.

1:0:39

This is not an external API request. Here you are making an external API request. You need internet

1:0:45

for that. Here everyone what is happening? It is an internal API request which is going just from one

1:0:50

application to another application within the same machine. Does it make sense to all of you?

1:0:56

Right. So you can assume that this is also acting like a small AI server running on your laptop,

1:1:03

running on your machine. Right. So guys, when you run LLM, when you run LLM via O Lama, it also runs

1:1:10

on a local host, right? Do you remember that the fast API server was running on some local host in my laptop,

1:1:15

in our laptop? Right. So guys, guys, similarly.

1:1:20

Similarly, O Lama also run on local host, HTP, colon, slash, slash, local host. Then port number.

1:1:29

Port number is, this is the default port number, 11434 slash API slash chat. So if you want to have

1:1:36

a chat with OLLM model, you can make an API call, pass the prompt, it will give you the response

1:1:42

back. So from this API, you can make a call to this address and you will get the response back.

1:1:48

Does that make sense to all of you? Yes.

1:1:50

or no? Does that make sense to all of you? Yes or no. Now, let's try to install

1:1:59

O Lama. So folks, what I will do is, I will show you from the beginning. I already have O Lama downloaded,

1:2:06

but I will still show you the complete way. Just give me a second.

1:2:20

So, folks, this is the, what do you say? This is the definition, this is the home page of Olama. If you go to Olama.com, you will see this. And these are the models that are available freely, right? So what you can, first of all, what you can, what you should do is you should create an account on Olama, go and create an account. And then what you do is you install this, right? And where is the installation?

1:2:50

download. Go to download and you can choose your operating system and you can download.

1:2:59

Either you can run this command on your terminal, it will download or you can download from here.

1:3:03

Makes sense, everyone? And once you download everyone, once you download it, it will be like few, what do you say?

1:3:09

Few MB only. I already have installed. You can download it. Everyone understood? And once you download it and then you double click on the application, just follow the steps.

1:3:17

install, install, install, agree, and once you install it, go to the terminal,

1:3:22

and how will you check whether you have successfully downloaded O-Lama or not, whether it is successfully

1:3:27

installed or not, go to your terminal and just execute the command O-Lama-V-V-V, it will tell you

1:3:33

the version, right? If it is telling you the version successfully, it means that it is downloaded.

1:3:38

Makes sense, everyone? It is downloaded, right? And then everyone, you can also run this command

1:3:43

O-Lama, right? Then everyone, once you do this, if you see, it has opened the terminal.

1:3:47

interactive terminal with which you can use it, right?

1:3:51

So you can use O-Lama, you can use Claude, desktop via O-Lama cloud.

1:3:55

There are different ways.

1:3:56

What we are going to do is, we are going to chat with the model.

1:3:59

Just click on this, then you can select the models.

1:4:02

These models are recommended that you can use.

1:4:04

Are you guys getting this point?

1:4:06

For now, we will close it.

1:4:09

Is that point clear to all of you?

1:4:11

This is how you can download it.

1:4:13

Very simple, very straightforward.

1:4:17

Okay. Once you download that, everyone, then how can you download the model?

1:4:27

Then everyone, if you want to download any model, you can do Olama, run, and give the model name,

1:4:35

the name of the model. Let me just take this model name. For example, everyone, if you go to the models,

1:4:41

then you can select these models. And then everyone, you can also see the size of the models. For example,

1:4:46

if you, let's say, click on this model, Deepseek V4 Pro, if you click on this model,

1:4:52

you see that how much is the size of the model?

1:5:00

How much RAM is required?

1:5:03

Size is not given here.

1:5:04

But if you see, this model is 1.6 trillion parameters.

1:5:08

It is a very big model.

1:5:09

Definitely.

1:5:10

My laptop might not be able to run this particular model.

1:5:13

So maybe we will go back and let's say we will go with this.

1:5:16

Q1 3.6. And yes, if you see this model has different versions, right?

1:5:23

Q1 has different versions and it is telling you how much size is required. Right? If you see

1:5:29

24GB, 17GB, 31 Gb, 55 GB. Do you think that everyone this much data is like for testing?

1:5:40

Should we download such a big model?

1:5:42

not real, not worth it, right? It will take a lot of space. My laptop will become

1:5:49

slow. It will start getting hanged up, right? Not worth it. So, you can go with these small

1:5:55

models, everyone. I think Q1. Yeah, these are very small model, right? If you see, Q1. Yeah, these are very small model.

1:6:10

Right? If you see Q1, 2.5, this model, this is just 3.2 gb. This is good enough. We can use it. Okay. And then you can use this one also. Quen. And they are also even very small models. If you see how much data it is going to use, just 395 mb. That is like less than half a gb of data.

1:6:30

Right? This is just 1.1 gb. I think 1.1 gb should be fine. Is everyone clear?

1:6:36

Now tell me everyone. There are like here if you search, right, you will.

1:6:40

even be able to find a model with 100 gb of RAM requirement, right? So if you go to, if you search

1:6:45

and then, let's say, for example, if you go to some image model, some vision model, some video

1:6:50

model, you might be able to find some model, which is very, very strong, which is very, very powerful.

1:6:55

It might be having a requirement of 100 gb of RAM. Definitely you can use that versus you have a model

1:7:01

with just one gb of requirement. What is going to be the difference between 1GB model and 100 gb model?

1:7:10

What is going to be the difference between a 1gb model versus a 100 gb model?

1:7:16

Obviously, the number of parameters, right?

1:7:18

The number of parameters on which that particular model has been trained upon.

1:7:22

More number of parameters, it means that it has more information from the world, from the universe.

1:7:28

Definitely, it will be better, it will be able to perform better.

1:7:31

It will be able to give you better answers.

1:7:33

Right.

1:7:33

So everyone, obviously, if you're going with smaller models, you'll have to compromise on the quality.

1:7:39

Make sense, everyone?

1:7:40

So, for local testing, for learning purpose, it is okay.

1:7:44

Makes sense, everyone?

1:7:46

Okay?

1:7:48

Now everyone, if you don't want to see, you can download these models also, or you can also interact with these models via terminal also.

1:7:57

I will also show you how to download these models, how to pull these models.

1:8:01

But if you directly give, let's say for example, if I take, if I copy the name, and if I do, Olamar run this model.

1:8:09

And if I press enter, you see that, it is also downloading, it is pulling.

1:8:15

If you see everyone, yeah, it is downloading 1.1GB, right?

1:8:19

So there are different ways in which you can run interactive, you can run online also.

1:8:22

I will show you that also.

1:8:24

But if you see, it is downloading this model.

1:8:26

Makes sense, everyone?

1:8:27

We will use this model.

1:8:28

This is good in.

1:8:29

1GB is good enough.

1:8:35

Okay, let it download, everyone.

1:8:39

One more thing, everyone, that don't you think if you have a model running locally, then you can actually go inside the model's information and change something?

1:8:52

You can play around with that.

1:8:54

Right?

1:8:56

Correct?

1:8:58

Actually, you can do that.

1:9:00

You can do that.

1:9:01

I will show you that this model is getting downloaded in my hard disk.

1:9:04

I can go inside the model.

1:9:06

I can delete something.

1:9:07

I can edit something.

1:9:08

I can add some more information.

1:9:09

This is nothing but kind of a fine tuning, that you are fine tuning the model.

1:9:15

You are giving your own information on top of what it already knows.

1:9:19

If you see it has downloaded and then it is trying to install some related things and it has

1:9:25

verifying, it has verified, writing manifest and success.

1:9:29

The model is downloaded successfully.

1:9:39

Yeah, now you see where it is asking a message.

1:9:44

It is asking a prompt.

1:9:45

I can write a prompt here, send a message.

1:9:48

For example, let's say explain the difference between, let's say, tell me, please tell me, if I should use open AI model or some

1:10:09

local model via Olam right let's say if everyone if I'm asking this question

1:10:15

I press enter is this request going outside my system is this request going outside my

1:10:24

system absolutely not this request is served by the model which is running on my

1:10:30

local machine is that point clear to all of you this request is served by the server by

1:10:36

the LLM model running on my machine right and everyone if you

1:10:39

you see, the request, the response is also good enough, right?

1:10:41

It's not very bad, right?

1:10:44

It is telling you that whether you should use open AI model or local depends on several factors.

1:10:49

Performance, availability, cost, right?

1:10:52

However, it is essential to keep in mind the performance of open AI model might be impacted by

1:10:56

various factors such as availability, etc. You can read about it.

1:11:00

So, first of all, is everyone clear how to install Olamma, how to run a model?

1:11:05

Make sense?

1:11:07

So you can go to this link.

1:11:09

You can go to this link and search for any model.

1:11:14

So folks, we can take a break at this moment.

1:11:16

It's exactly 9 p.m. sharp.

1:11:18

Let's take a break at this moment.

1:11:21

Now what do you need to do is take 5 minutes of time,

1:11:24

download Olama, install it and try to run your first model.

1:11:27

It could be very small.

1:11:29

Don't try to run a very big model.

1:11:30

Try to, even if you're okay, even I'm okay with if you run this model.

1:11:35

Just 3, 400 mb.

1:11:37

It is good enough.

1:11:38

For testing, it is good enough.

1:11:39

It might not give you very good response.

1:11:42

It might not be very good with reasoning, complexity, etc.

1:11:45

But we are okay with that.

1:11:47

So let's take a break everyone.

1:11:48

So let's take around 12 to 13 or maybe 15 minutes of break.

1:11:51

Take 5 minutes of time to install and download Olama.

1:11:54

And then we will try to see after the break,

1:11:56

how can we integrate this with our Python script, Python code,

1:11:59

Python application.

1:12:00

Okay?

1:12:01

So let's take a break right now.

1:12:02

See you after the break again.

1:12:09

Thank you.

1:12:11

Thank you.

1:12:41

Thank you.

1:13:11

Thank you.

1:13:41

Thank you

1:14:11

Thank you

1:14:41

Thank you

1:15:11

Thank you

1:15:41

Thank you

1:16:11

Thank you

1:16:41

Thank you

1:17:11

Thank you

1:17:41

Thank

1:17:43

Thank you.

1:18:13

Thank you.

1:18:43

Thank you.

1:19:13

Thank you.

1:19:43

Thank you.

1:20:13

Thank you.

1:20:43

Thank you.

1:21:13

Thank you.

1:21:43

Thank you

1:22:13

Thank you

1:22:43

Thank you

1:22:45

Thank you

1:22:47

Thank you

1:22:49

Thank you

1:22:51

Thank you

1:22:53

Thank you

1:22:55

Thank you

1:22:57

Thank you

1:22:59

Thank you

1:23:01

Thank you.

1:23:31

Thank you.

1:24:01

Thank you.

1:24:31

Thank you.

1:25:01

Thank you.

1:25:31

Thank you.

1:26:01

Thank you.

1:26:31

Thank you.

1:27:01

Thank you

1:27:31

Hi everyone.

1:27:37

So folks, let's see some other commands as well.

1:27:41

So the model, if you want to install a model, if you want to run a model, the command is Olama run.

1:27:47

Now if you want to see all the models that you have installed via Olama, you can have a command, you can run the command called as Olama list.

1:27:58

It will list down all the downloaded models.

1:28:00

models.

1:28:01

If you see, as of now, we have one model which we have just downloaded.

1:28:05

Because earlier when I downloaded a few models, it was taking more space in my laptop, I removed

1:28:09

those models.

1:28:10

Sounds good.

1:28:11

Because in day-to-day life, I don't need these models in my local laptop, correct, in my laptop.

1:28:16

So after the class, typically if I feel that there is a lag in the performance, I just remove

1:28:21

them.

1:28:22

If you want to remove any model from your system, what you can do is the command is Olamma, RM,

1:28:30

and give the ID or give the name.

1:28:33

Okay?

1:28:34

Olama hyphen give the name.

1:28:35

It will remove the model from your laptop.

1:28:37

Sounds good?

1:28:38

Maybe I will show you that.

1:28:40

Also when there is a command called Olamma PS.

1:28:42

Anyone has used PS command in MacBook,

1:28:46

Windows, etc?

1:28:48

Anyone has used PS command, not for OLama in general?

1:28:52

Running processes, absolutely right.

1:28:57

If you want to see the processes running in your laptop,

1:28:59

is running in your laptop, you use PS command, right? If you want to use the processes or the models

1:29:05

which are running via Olamma, you can use Olamas and it will show all the running models, right?

1:29:12

If you see everyone, as of now, there is no running model. Make sense?

1:29:18

Everyone clear? There is no running model. The model, this model is downloaded, but it is not

1:29:23

running at the moment. Make sense, everyone? Okay. Now for example, Evel, if you're running

1:29:29

any model, if you're downloading any model, what all the things, does it, like, does it impacts in your laptop?

1:29:39

Hardware consumed by a model in laptop?

1:29:59

disk? Tell me, does it consume your hard disk? Yes. Does it consumes your CPU?

1:30:10

Coors of the CPU? Yes. Does it consume your GPU? Your laptop's GPU? Yes. Ram? Yes. Battery. Right, obviously. And so it will also consume your bandwidth.

1:30:29

No, what is the bandwidth?

1:30:36

Anyone knows, anyone can tell me what is the meaning of bandwidth? Disc bandwidth?

1:30:41

Disc bandwidth is like kind of how much data you can transfer from your RAM to hard disk, hard disk to RAM,

1:30:47

CPU, GPU, like overall data transfer within your laptop.

1:30:51

Via internal, like within the laptop, right? It might, it might transfer the data outside the laptop also.

1:30:58

But majorly, when we look at the systems running locally, we'll look at the data transfer that can happen per second within the laptop.

1:31:07

Right? So, guys, if you are running a model locally, don't you think it will transfer data from hard disk to RAM, RAM to hard disk, et cetera?

1:31:14

Because everyone typically what happens, every application that you download, right? For example, if you look at this model, right?

1:31:20

If you see, I downloaded this model, the size of this model is 1.1 GB. But is this model running right now?

1:31:26

Is this model running right now? No. So this model is not running right now.

1:31:33

Right? For example, if you install Facebook in your laptop, in your mobile phone, if you install any application,

1:31:38

you are not running that application. But still, is that application sitting in your hard disk?

1:31:45

Is that application sitting in your hard disk? Yes. So it is consuming hard disk. But as soon as you click on that

1:31:51

application, you touch on that application, that application starts running. So what operating system does is,

1:31:56

system picks up that process, picks up that application from the hard disk and put it inside

1:32:01

the RAM. Because who has the responsibility of running applications inside your hardware,

1:32:07

inside your laptop, mobile phone, etc? It is a CPU and GPU. But CPU, GPU cannot talk to your

1:32:13

hard disk. Anyone can tell me the reason for that? CPU or GPU cannot run an application

1:32:22

via the hard disk from the hard disk in your laptop. Or even in your mobile.

1:32:26

phone. Because anyone would like to take a guess, any, anything, any thought process,

1:32:35

any guesses, that why CPU cannot run an application directly from the hard disk? Exactly,

1:32:41

speed. Because everyone's CPU's speed, what is the CPU speed? It is generally in gigabits,

1:32:47

like, what is that? The frequency is gigahertz. Right? You might have seen, right,

1:32:51

that if you buy a laptop on Amazon, if you buy a laptop on Amazon, if you buy a laptop on Amazon,

1:32:56

for example, let's say, if you buy a laptop on Amazon, right, you will see that the size,

1:33:04

what do you see, CPU's frequency, right? Open any laptop? You will see that.

1:33:18

CPU, CPU, CPU. Let me show you number of course. Yeah. If you see, processor is G99,

1:33:26

some processor, octa core, these many cores are there, and the frequency, 2.2 gigahertz,

1:33:33

right? 2.2 gigahertz. What is gigahertz? Giga means 10 wrist for 9. Hurds is the

1:33:39

is the unit of frequency, one by second, right? One by time. It means that this gives us, if you see,

1:33:48

which runs up to 2.2 gigahertz. This is the maximum speed of the CPU, of the core.

1:33:56

It means that it can run 2.2 into 10 raised to power 9 operations per second. Hurds means

1:34:03

per second. So it can perform 2.2 billion operations per second. So this is the typical speed of

1:34:09

a laptop, of the CPU. And if you see this is a very normal range laptop, just 28,000. If you buy

1:34:17

a very high-end laptop, that might have a speed of like 10 gigahertz, 20 gigahertz, right? It

1:34:23

means that your CPU can perform billions of operations per second.

1:34:26

second. But your hard disk cannot do that kind of operations per second. Getting the point.

1:34:31

So that's why there is a very big difference, 1,000 times, 10,000 times, 1 lakh times. Speed difference

1:34:37

between the CPU and the hard disk. That's why what CPU does is CPU gives the instruction to operating

1:34:43

system. For example, Mac operating system. For example, Windows operating system. That hey, operating

1:34:48

system, I want to run this application. And then what operating system does?

1:34:52

Operating system pick up that application and put it inside a right.

1:34:56

RAM. And RAM is very fast. Ram is very fast. Now CPU can directly talk to RAM. And that's

1:35:02

if you have more RAM, along with the hard disk. If you have more RAM in your device, in your hardware,

1:35:08

then definitely you will be able to run more number of applications. And that is a reason,

1:35:12

everyone, that you might have seen multiple times that if you buy a device with 4GB of RAM, with 8GB

1:35:18

RAM, if you keep on opening more and more number of applications, after a certain point of time,

1:35:23

your device starts hanging. Because there is no device, there is no more space in the RAM.

1:35:30

That's why what operating system will try to do, it will start picking up the applications from

1:35:36

the RAM. And that's why there will be a slowness in the system. Right? Applications will start hanging. Is

1:35:42

the idea clear to all of you? Is the idea clear to all of you? Yes or no. Okay. Folks, yes, sir.

1:35:53

Okay, folks, so considering all these things, everyone, that we will maybe run a small model on locally.

1:36:23

I give any question to this? And it is giving me some response. Can I blindly trust the response

1:36:29

of this model? Can I say that, okay, this model is always going to give us the good response? No.

1:36:35

Because if we have small models, small model can hallucinate. There is a very high possibility.

1:36:42

It might hallucinate because it does not have proper context. And because of that, it will start,

1:36:49

yeah, I have just written this. Small model can hallucinate it. Because it does not have a lot of

1:36:53

of context and after certain amount of time, it can start hallucinating. So please don't trust

1:36:58

on the responses given by small model. Sounds good to all of you. Everyone clear? Okay. Now everyone,

1:37:08

what we're going to do is we will start writing the code in Python by, and we will see that how can

1:37:14

we use the Python script? How can we write a Python script which will use the local model instead

1:37:20

of using open AI. Have we returned the Python code in the past, in the previous

1:37:25

classes, which will call Open AI APIs? Have we already done that multiple times? Have we

1:37:32

already called Open AI APIs multiple times in the past? Yes. Today we will see how can we call

1:37:37

an open source model running locally via Python code. Okay? Sorry. So what we can do?

1:37:46

Let's open Visual Studio. Open some folder.

1:37:50

So what we can do everyone is, so we can use this one only, e-commerce rack, and inside this everyone, we can create another folder, let's say, local LLM model, or local LM, yeah, local LM, right?

1:38:18

And inside this everyone, we will write up.

1:38:20

code, we will write a file called app.p.m. Okay, we will write a code

1:38:25

called file called app.p. Okay. Now first of all, everyone, we will have to install a few things.

1:38:31

Okay. So let's go to the terminal. So what, first of all, what we need to do?

1:38:37

First of all, what should we need to do? What do we need to do? If you want to install few things

1:38:41

in local LLN, what should we do? Go to local LN.

1:38:50

Should we install a virtual environment?

1:38:58

Correct.

1:38:59

Python 3-M-V-E-N-V-V-E-N-V.

1:39:04

Correct?

1:39:06

And then everyone, what we will do?

1:39:08

Activate now.

1:39:10

Source V-E-N-V-V-B-Activator.

1:39:16

Okay, done.

1:39:17

And if you see, virtual environment has been installed.

1:39:19

So what?

1:39:20

Do we need to do now, everyone? We need to install a few things. First, we need to install

1:39:24

either one. So, folks, will we have to make a, will we have to make a HTTP request from

1:39:33

Python code, from Python application to local LLM model? Will we have to make a HTTP call?

1:39:41

Yes, we will have to make an HTTP call. So, folks, there is a model, there is a module in

1:39:45

Python, which is called as request module.

1:39:49

Requests module.

1:39:50

We will have to import or we will have to, first of all, install this model.

1:39:54

Now, one question that you should ask here is that Deepak, we did not install this module when

1:40:00

we used Open AI.

1:40:02

Then why do we need to do this now?

1:40:04

There also we were making API calls.

1:40:06

Here also we are making API calls.

1:40:08

Then what is the difference?

1:40:10

Can someone tell me now?

1:40:15

It's part of OpenAE? Okay. Think about it. While calling Open AI APIs via Python code, did we install request module? Did we install request module?

1:40:30

Answer is no. Absolutely correct, everyone. At that point of time, everyone, we were creating

1:40:37

an Open AI client. Client is equal to OpenAI. And via that client object, client.

1:40:42

to request. We were making HTTP call. So internally everyone, the client

1:40:47

of OpenEI, the client object of OpenEI was taking care of this HTTP part. Are you guys

1:40:53

getting this point? It was taking care of that request part. It was automatically making

1:40:58

HTTP call. But now everyone, because we are coming at lower level. Now we are even, now we are

1:41:05

running our own model. Now we are making a call to our own model. Then we will have to take care of

1:41:10

HTTP call as well.

1:41:12

Are you always getting this point? Are you guys getting this point? Why can't we use

1:41:17

fast API? We can do that. But for if you see, if you're using fast API, then you are building our

1:41:21

own server. Here we are not building our own server. Rather, we are just writing a simple

1:41:26

Python script to make a call. You can do that via fast API also. But fast API probably will

1:41:32

be maybe an advanced step, right? That you are building your own server and then that server

1:41:37

is making a call to local LLM. And this is, you can say that this is just a simple Python script.

1:41:42

simple Python application which is making a call. Are you guys getting this point that why we are

1:41:47

installing this request module? And if you see everyone, we have successfully installed the request

1:41:52

module. Folks clear. Okay. Now what we, what we will do everyone is we will make a, we will start

1:42:03

running the module. O-Lama run this model. Now if you see this model. Now if you see,

1:42:12

everyone, when I initially ran this command, O Lama Run, and the name of the model,

1:42:19

when we initially did that, do you see that, it started pulling the model? Pulling the model. Pulling

1:42:23

the model means downloading the model. It started pulling the model. But when I ran this command

1:42:28

right now, did it pull the model now? No, it did not pull the model? Why? Because it automatically

1:42:37

checked that the model is already there. Folks, is that point clear to all of you? Because the

1:42:42

model is now what we're going to do everyone is now we will start writing the code.

1:42:46

First we will import request, import request, and then everyone we will give the O-Lama host.

1:42:54

That where that O-Lama server will run by default, it will run on HTTP,

1:43:01

slash-slash, local host, colon, port number. There is 1-14-34. And then we will give the model name.

1:43:09

And what is the model name, everyone? Let me copy paste the model name.

1:43:12

sorry is that point clear to all of you okay and then everyone we can give some

1:43:22

prompt prompt is like let's say please tell the advantages or please compare the

1:43:34

LLM models or LLMs running locally or running locally or

1:43:42

a simple problem. Let's say explain rest API in a beginner friendly way.

1:43:55

Okay, bro? A very, very simple prompt. Sounds good. Okay? And now everyone, what we will do is we will get the response.

1:44:06

Response is equal to request. Post. So guys, we will have to make a post.

1:44:12

post API call. Now, guys, when you make a post API call, I will explain this in some time.

1:44:19

First, let's try to make an API call. Post, when do we make a post? Right? So can you tell me,

1:44:26

if you remember, we discussed about HTTP methods, right? HTTP methods, get put,

1:44:35

a patch, get put, post, and delete. Put and patch are the same thing. Same thing is update.

1:44:42

Post we use for creation of the resource, right?

1:44:46

For creation of the response.

1:44:48

So, folks, you can think in this way that, Olama gives us a way to make a post call.

1:44:52

Why? Because it is, you think in this way that it is creating a response object.

1:44:57

Okay? It is creating a response object.

1:45:00

And then what do we need to do everyone is? First, we need to make an API call, right?

1:45:04

We need to give the path and path is what, everyone?

1:45:07

Olamah host, basically this is the path. Okay. You can say that API path also, you can define.

1:45:12

If you don't want to do that big task, right, path is slash API slash chat, right?

1:45:22

You can do like this.

1:45:23

So you directly, you can give the API path here.

1:45:26

Are you guys getting this point?

1:45:27

You can directly give the API path here.

1:45:30

Slash API slash chat.

1:45:32

Folks clear?

1:45:35

11434 slash API slash chat.

1:45:38

Right?

1:45:40

Then everyone, you will have to pass.

1:45:42

the request body. Do you remember that? We might have discussed this point that for post

1:45:49

request you need to pass the request body because when you create a response, you need to pass

1:45:53

a complete request body in the input. So let's create the request body. That is also called

1:46:01

as payload everyone. You can call it as request body or you can call it as payload. Let's create

1:46:06

a payload. Payload is nothing but a JSON object that will contain all the input parameter.

1:46:12

in one object, in one JSON object, that you want to pass to the, in the API call.

1:46:21

Right?

1:46:22

So what do you think, everyone, inside the payload, what API parameters or what input parameters

1:46:27

should we pass?

1:46:28

Just think about it.

1:46:33

What input parameters should we pass?

1:46:36

Very good.

1:46:37

First of all, we should pass the model.

1:46:39

Model is equal to.

1:46:42

model is equal to model name. Correct. What is the second thing? Then we pass

1:46:50

messages. Then we pass messages not equal to column. Messages may, what do we pass everyone? First

1:47:00

of all, we pass the rule. Again, everyone, rule is a, you say that role is a, not a mandatory

1:47:08

parameter, it is an optional parameter. So you can say that you're acting like a user,

1:47:12

because you are just trying to communicate, you are just trying to make a call to the chat API.

1:47:17

You can make, you can define some role as well. For example, if you want to use some role prompting,

1:47:22

let's say act like a software engineer and then give this answer. Act like a doctor, give this answer.

1:47:26

We have already seen that in the prompt engineering, right? So for now, we are just defining the role

1:47:31

and then we are giving the content. Content means the prompt. Here you define the prompt.

1:47:36

Sounds good, everyone.

1:47:39

And then everyone, the another parameter that you need to pass is.

1:47:42

Next is stream. I will talk about stream in some time.

1:47:47

Stream is, for example, false for now. Is that point clear to all of you?

1:47:51

Stream value is false for now. We will talk about stream in some time.

1:47:55

Okay? We will come back to stream. Is everyone clear with this? Yes or no.

1:48:05

This is how we create the input object, the request body.

1:48:12

request body, right? And this everyone, we pass as it is in the JSON filter, right,

1:48:18

or the JSON input. And then everyone, there is one more parameter that you can pass, which is optional,

1:48:24

which is called as timeout. Time out means that everyone, that how much time it should wait, right?

1:48:30

For example, you can give that in the seconds, that 120 seconds, or let's say maybe 60 seconds.

1:48:36

That if you don't get the response within 60 seconds, just make the request time out. Over

1:48:42

internet, everyone, over some websites, some applications. Sometimes, have you come across

1:48:46

this timeout error that your request was timed out? Because everyone would happen sometimes

1:48:52

when you make a request, at that point of time, let's say the server was not available, and your

1:48:56

request was waiting, right? If your request keeps on waiting, keeps on waiting, keeps on waiting,

1:49:01

and the server does not have any timeout set, then your request might be waiting for infinite time.

1:49:06

You never get a response back. So always, what do you do is, when you take care of these things, right?

1:49:11

Now, why don't we do that on the OpenAI? OpenA might have their default timeout.

1:49:16

You can change it, but definitely they will have some default timeout.

1:49:19

Maybe let's say 120 seconds.

1:49:20

That if you don't get the response within two minutes or 120 seconds, then you automatically get the response back with the error code timeout.

1:49:28

But here everyone, you'll have to set it manually because you are the server.

1:49:32

Now you are maintaining the server.

1:49:33

You are the owner now.

1:49:35

Are you guys getting this point?

1:49:36

Otherwise, if your server is not responding, then your server might be waiting for info.

1:49:41

finite time. Are you guys getting this point? Yes or no? And then finally,

1:49:46

everyone, what do we do? From this response, we get the data back, let's say output back. Response.

1:49:53

D. JSON. This complete, whatever response we are getting, convert that in the JSON and print that

1:50:00

in the output. Are you guys getting this point? Yes or no. Are you guys getting this point? Yes.

1:50:11

Folks, how many if you're clear with the code?

1:50:15

Okay, now what we want to do?

1:50:18

Clear the terminal.

1:50:20

Python 3, app.py.py.

1:50:24

role is user? Oh, sorry, sorry, sorry, sorry. This is also in the chess.

1:50:46

Right? Yeah. So now if you see, well, it is making a call. Let's wait for the response.

1:50:54

Why we hear it? Yeah, you can remove it. Right? You can remove it. This is not required.

1:51:01

Okay. Now do you see that everyone? This is the complete response that we are getting. That in the

1:51:05

complete response object, we are getting the model that we are using, right? Getting the point. We are

1:51:10

using the local model that we have already installed. Right. This response was created at 18th of May.

1:51:16

This is the time. Right. Then everyone, what message? What message we are getting? Yeah. Rest.

1:51:24

state transfer is an architectural style, etc. This is the complete response that

1:51:30

we are getting from here to here. Is that point clearly to all of you? Yes or no? Correct? Correct? This is a complete

1:51:41

response that we are getting out in the output. Okay. Then everyone, it is also giving some other

1:51:48

parameters that we technically don't need most of the time. If you just want to get the content,

1:51:53

if you just want to get the content, where did you get the O Lama host path? This is from the

1:52:01

the official documentation. If you go to the official documentation, you will be able to find out

1:52:05

that how to run. For example, if you go to download and when you download it, you go to the documentation,

1:52:11

it will tell you. Okay, if you go to the documentation,

1:52:14

quick start, download, run, and here you will see that after launching, etc. This is, this is

1:52:23

is the path. Okay, slash API slash chat. Correct, pillar? Okay? Okay. Yeah. Yeah. So folks,

1:52:35

now if you just need the content, what you can simply do is that from this response, from this

1:52:42

complete response output, just give me from the, first of all, go inside the message, and inside the message, just

1:52:52

give me the content. Content, that's it. Okay, now clear and make a call. It will just

1:53:02

give you the output. Getting the point of your, this is the complete response that we are getting

1:53:09

from our local LN. How many if you are clear with this yes or no? So folks, let's try to understand

1:53:18

this step by step. Right? So this is the API path.

1:53:22

Right? That we are getting from the documentation. This is a model everyone. Now if you change the model,

1:53:28

for example, let's say if I change the model to, let's say there is some other model as well that we can check.

1:53:34

For example, this is also a valid model, right? Let's give this name of the model. And then let's try to

1:53:40

make an API call. Do you think that I will be able to use it?

1:53:52

No, right? Now if you see even output is coming as empty. Okay? Because now if you see that

1:53:58

message is not there in the output. Now, as of now, the message is, the error is not properly handled.

1:54:03

But now if you show the output here, you'll see that output itself is not there. In the output, what

1:54:10

we are getting? Error, that model not found. Correctable? The error, what error is we are getting

1:54:15

modern, this particular model not found. Okay? We will also see how to handle errors. I will show

1:54:20

you that in some time.

1:54:22

Okay. Also everyone now, one more thing that if you see the model is currently running, let's stop the model.

1:54:29

If you see, I have suspended it, I have stopped the model. And then everyone, what I will do, I will go to the original model.

1:54:52

the original model and now let's try to run this. The model is not running at this

1:55:00

this moment. Yeah, model is not running. Okay, it might be giving the response. Is it giving

1:55:08

the response? Yes, it is giving the response. I think it is giving the cash response or it might

1:55:15

be running in the background. Okay, the model is running actually. Okay. The model is running actually.

1:55:22

Okay. This model is running. Even if you stop it, it was running. So how can you kill the model? How can you stop the model?

1:55:33

What is the command for that?

1:55:52

Okay. The model has been killed, I guess. Let me check. Not really. Let me just check.

1:56:22

Olama stop. Okay, it has stopped the model. And now if you try to make an API call, let's see what it will give you.

1:56:52

It is still running. Why? And how? No, no, it is still running. Why it has not stopped here?

1:57:22

Yeah, now it is stopped. Okay, now it is stop. I think it takes some time. That's why. Now it is stopped. And now if you try to make an API call, it is still running.

1:57:52

What it does everyone is, uh, internally is doing something, some optimization that even if the model is not running, right? It is running the model.

1:58:02

Okay. So if you see earlier, we were not getting any model running after making the IPA call, it is starting the model and then it is making a request.

1:58:11

Okay.

1:58:13

Even not on the RAM, it can like, it can like ultimately who is going to run operating system. So operating system can pick up the model and run it.

1:58:20

Right? Makes us. I'm also surprised that this kind of thing is there. So it is running the model and then using it. Okay. So it is not waiting for us to run. Are you guys getting the idea? Maybe we can close the connection from our application. What do you mean by closing the connection? What do you mean by closing the connection? What changes do you want me to do?

1:58:50

Close request.

1:58:56

Definitely. Then it will not be able to talk. Correct. But if the connection is opened, but even if the model is not running in your laptop, still it can start the model.

1:59:04

Right? Still it is able to start the model. Okay. Now everyone coming to the next point that what all the things are there, the only thing that you need to, so line by line, let's try to understand, API path, we understand, model name we understand, prompt we understand.

1:59:20

All of these things we understand. How we make a request, this also we understand, correct?

1:59:24

The only thing that we need to understand is this stream. This stream value is equal to force. Can you tell me what do you understand by the term called stream is equal to false?

1:59:50

Ask any question. Explain. Explain me about rest API in a beginner friendly way. Same prompt. Now just observe exactly, right? All of you are correct in the chat. Just let's press the enter and see how the response is coming. Do you see that? The request, the response that you are getting, it is streaming. It is coming. It is coming token by token.

2:0:20

is coming word by word. Do you see that? It is writing on the fly. Correct, everyone?

2:0:26

This is called a streaming. Streaming is something like Behanah, flowing. The output that you are getting from

2:0:32

chat, GPT, you don't you think the output is actually streaming step by step, token by token, word by word.

2:0:38

Correct or not? Correct? This is one way. Another way could be what? That if you make stream is equal to false, then what model will do?

2:0:49

model will generate the complete response and then it will give it you in one shot.

2:0:54

If you make stream is equal to true, then it will keep on giving you the response continuously.

2:0:59

That will get typed, that will come to your, that will come as a response, character by character,

2:1:05

token by token, word by word. Is the meaning of stream making sense to all of you?

2:1:13

is the meaning of stream making sense to all of you? Now everyone, let's try to do one thing.

2:1:19

Let's make stream is equal to true.

2:1:24

Okay? Let's make stream is equal to true and let's try to print the output now.

2:1:43

What is the problem here?

2:1:49

response.Jol.

2:1:55

Extra data line to column 1.

2:2:02

Why this error is coming?

2:2:07

Okay, there might be a different way if you want to have stream is equal to true.

2:2:11

Okay, I'll check it.

2:2:12

Okay, but if you make stream is equal to false, you might have to pass some special parameter as well.

2:2:19

Are we getting output for stream is equal to false?

2:2:24

Let's see.

2:2:25

Yeah, we are getting it.

2:2:27

Okay.

2:2:28

So what is stream is equal to false?

2:2:30

Stream is equal to false means that return the full response in one go, in one shot.

2:2:42

Right?

2:2:43

Not token by token.

2:2:48

token streaming with it.

2:2:51

Not token by token streaming.

2:2:54

Is that point clear to all of you?

2:2:56

Yes or more.

2:2:59

Is that point clear to all of you?

2:3:01

Okay.

2:3:02

Now everyone, there is another way as well in which you can use O-Lama,

2:3:06

which is O-Lama Cloud.

2:3:09

So you can use O-Lama with cloud as well.

2:3:11

It is going to be extremely, extremely, like,

2:3:14

absolutely same, extremely simple, just like this.

2:3:17

What do you need to do everyone is?

2:3:18

like O-Lama Cloud is as good as using open-air.

2:3:23

It is very, very similar.

2:3:24

Just small differences.

2:3:26

First, everyone, what you'll have to do is if you want to use O-Lama Cloud API,

2:3:29

you will have to create an account at O-Lama.

2:3:31

Once you create an account at O-Lama, you will get the API key.

2:3:34

For example, if you go to O-Lama, and then if you go to your account,

2:3:38

settings, keys, you will get the API key, right?

2:3:44

Once you get the API key, everyone, set it in the environment variable.

2:3:47

Let's do that.

2:3:48

Let's do that.

2:3:49

Okay?

2:3:50

Let's say API key is 18th of May.

2:3:54

Generate the API key.

2:3:55

Once you get the API key, let's create another application here.

2:4:01

Tap 2.p.

2:4:07

And what we're going to do is, first we need to set the environment variable, export OAPI key.

2:4:17

API key is equal to this.

2:4:20

Set the API key.

2:4:22

Once you set this everyone, we again import request.

2:4:33

Then again we need to give these two things.

2:4:37

Okay.

2:4:42

Then API key is done.

2:4:46

Then again, we can.

2:4:47

can copy the prompt. Let's say we have the same prompt. Again, we give the model, the payload.

2:4:54

The payload is absolutely similar. It is exactly the similar thing, everyone. We give the model name,

2:5:00

model name, whatever. Message is same and streaming is false. And then what we need to do,

2:5:08

everyone, is this is something different that we need to do, that we need to pass the API in the API key,

2:5:14

in the header. Okay? So you create a header

2:5:17

object, which is also type of a JSON. And in this header, everyone, you set the authorization

2:5:22

tag. Authorization. And in this authorization, everyone, you give the token bearer token. Beer

2:5:28

is a type of token, and then you give the API key. Okay? So what you can do, everyone,

2:5:33

is basically what you would do is in Open AI, because Open AI, you are paying for it,

2:5:39

it is giving you slightly more functionalities. But in Olam, everyone, you will have to read the

2:5:44

open AI, you will have to read the API key in the open AI.

2:5:47

code how let's see so what do you do you import another module called as operating

2:5:51

system OS right and from the operating system you can read the value of API key

2:5:56

okay so what you can do here is API key is equal to operating system dot

2:6:02

environment variable environment dot get and give the name of the variable

2:6:07

which is this variable O Lama API key makes us everyone Olamma API key sounds good

2:6:13

and this API key everyone you pass it as a parameter

2:6:17

in authorization header API key. Is this point clear to all of you?

2:6:24

Okay. And folks, just to check this, you can also check like this. If API key is not set, if not API key, then you can raise a value error.

2:6:47

Like, can you elaborate the question?

2:6:54

You, is your question that why do we need Olam API key?

2:6:57

Is your question this, that why we need Olam API key?

2:7:02

Yes, no.

2:7:16

No response is coming.

2:7:19

OLama API key, let's say, key, not set.

2:7:25

You can raise this value error.

2:7:28

We are downloading the model.

2:7:30

So if you see, I am giving you a different way that we are trying to make a call to open AI, OLama

2:7:36

Cloud.

2:7:37

So we have already seen how to make call to local model.

2:7:41

Here we are seeing that how we are making a call to open AI, sorry, again again, I'm using open

2:7:46

O-Lama Cloud, right? I'm telling you both the ways.

2:7:50

First we saw running open O-Lama model locally and then using it.

2:7:55

For that, you don't need API key.

2:7:58

If you're using O-Lama cloud model that is running on O-Lama, then you would need API key.

2:8:04

So this is the second file, app 2.

2:8:07

Okay, so let me put a comment here.

2:8:10

So in this app, in this code, okay, we are

2:8:16

using O-Lama Cloud.

2:8:21

Okay?

2:8:22

That's why for that, we would need O-Lama API.

2:8:30

Makes sense?

2:8:33

Does it make sense to all of you?

2:8:36

Oh, yes.

2:8:38

Now that would not need, that would not be running on local host,

2:8:41

that would be running on O-Lama.com.

2:8:45

Okay.

2:8:46

That would be running on O-Lama.com.

2:8:49

Correct.

2:8:50

Everyone, clear?

2:8:53

Because now, if you see from here, it is clear, that it is running on cloud.

2:8:57

Okay?

2:8:58

And finally, everyone, we will make the call in the exact same way.

2:9:00

Just make the call.

2:9:03

Request.

2:9:05

Response is equal to request.

2:9:07

Request.

2:9:08

API path.

2:9:09

API path is this.

2:9:10

Olama.com slash API slash chat.

2:9:13

Then JSON.

2:9:14

Now everyone, along with JSON.

2:9:15

everyone, along with JSON, now you need to pass headers also.

2:9:18

Headers is equal to header.

2:9:21

Is that point clear to all of you?

2:9:23

Now you need to pass authorization header also.

2:9:26

And inside the header, you are passing the API key.

2:9:28

How many of you are clear with this?

2:9:30

So we can use other LLMs as well, absolutely yes.

2:9:33

So with Olam, you can use any LLM.

2:9:35

I will show you that.

2:9:36

And finally, everyone, after you get the data, after you get the output,

2:9:40

response.

2:9:41

Dot JSON, okay?

2:9:43

You can print

2:9:44

Output of message and then content.

2:9:53

Is that point clear to all of you?

2:9:55

Yes or no?

2:10:02

Folks clear.

2:10:04

Have a look at it and tell me.

2:10:07

So let's try to make a call everyone.

2:10:10

So let's try to run Python 3, App 2.

2:10:13

PY. Can we generate the output using stream?

2:10:16

I'll have to check that.

2:10:17

So we can definitely do that.

2:10:18

It will not be a very difficult thing.

2:10:20

I'll have to check that.

2:10:21

It might need some extra parameter.

2:10:22

Okay?

2:10:23

I can check that.

2:10:26

So let's try to run this everyone and let's see.

2:10:29

What is a problem here?

2:10:31

Output message content?

2:10:34

The response we are getting.

2:10:42

method not allowed.

2:10:52

Why method not allowed?

2:10:54

Need to set up the API key.

2:10:56

We did set it right.

2:10:58

Export, O Lama, we set it.

2:11:00

This is the API key.

2:11:04

We set the API key.

2:11:06

Export O Lama API key.

2:11:08

Is the name different?

2:11:10

Oh, Lama, just a second.

2:11:15

API underscore key.

2:11:18

We have the key.

2:11:20

Okay.

2:11:21

And we are getting the API key.

2:11:23

API key is equal to this.

2:11:25

Let's try to print it, everyone.

2:11:26

Whether API key is coming correctly or?

2:11:28

Method not allow.

2:11:31

Why?

2:11:33

API key is correctly coming, right?

2:11:35

This is the correct API key.

2:11:38

Yeah, correct API key.

2:11:39

It is giving us method not allowed.

2:11:46

Let me check.

2:11:47

and getting this error while calling Olam

2:12:05

API Cloud API.

2:12:08

Post method.

2:12:16

Oh, correct, correct. It should be HTTPS.

2:12:21

Okay?

2:12:22

Correct.

2:12:23

Chimmy, that's correct.

2:12:25

And also on chat GPT also I got the same result.

2:12:28

Okay.

2:12:29

What could be the possible errors?

2:12:31

Thank you.

2:12:32

Okay, let's try to make.

2:12:34

Okay, now the model not found.

2:12:37

Okay, now I think we will have to use

2:12:45

It's not a cloud model. Let me check which is the cloud model.

2:12:52

It's not a cloud model.

2:13:06

Cloud API does not include the model at all.

2:13:11

That's correct.

2:13:12

Okay.

2:13:13

So instead of Q1.1.8B.

2:13:14

Let me use this particular model.

2:13:17

So I'm just searching on chat GPT, everyone.

2:13:19

So GPT is giving us this model.

2:13:22

Okay?

2:13:23

So folks, some of the models, they are very basic.

2:13:25

And if you see, this was the most basic model, just 1GB.

2:13:28

This does not even give you these APIs, the cloud APIs, okay?

2:13:32

Because these are very small, very, very, very specific to local use case, right?

2:13:37

That's right.

2:13:39

So now I have changed the model.

2:13:40

Let's try to make a call now.

2:13:43

model not found. Okay, this is also not working. This is the model that, that was suggested by Chad GPD.

2:13:50

Okay.

2:13:52

Q1 3.5 is a cloud model. Okay, let me check. Go to models.

2:14:10

Q1.

2:14:12

is a family of open source multi model that delivers exceptionally utility and performance.

2:14:21

Okay, yeah, if you see a run, this is cloud model.

2:14:27

Okay, this is cloud model.

2:14:29

Cloud is there.

2:14:30

But now everyone, if I search for which model we were using initially, this model, right?

2:14:36

Let me search for this model.

2:14:39

Then it will tell us.

2:14:41

This is also 3.5 is cloud. If I search for this.

2:14:53

F is 7, Q12. This is QN2 is not cloud model. So 3.5 is a cloud model. So we can use, let's say, this model. Okay, let's copy this model.

2:15:04

Copy paste.

2:15:10

Let's check.

2:15:12

Okay, this model is also not found.

2:15:17

Okay, this model is also not found.

2:15:25

Okay, this is also not working. Why so?

2:15:33

For making cloud request.

2:15:39

request.

2:15:52

Local host, okay, pull.

2:15:55

You do not need to manually run beforehand the API usage, but the model for hosted cloud endpoint,

2:16:03

end point.

2:16:04

Is the API key valid for some particular time?

2:16:06

No, no, API key is just fresh, right?

2:16:08

API key?

2:16:09

is not old.

2:16:10

API, you will not have any problem.

2:16:12

No local pull needed?

2:16:27

Okay, is the API different everyone?

2:16:31

HTTP, column.

2:16:34

Okay, folks, let me check the API.

2:16:38

No, no, API slash API slash chat only.

2:16:48

Cloud.

2:16:52

Okay, running cloud models, sign in to run a cloud model, open the terminal and run.

2:17:01

OLAVA cloud models requires an accountant there.

2:17:07

First, pull a cloud model, so it can be accessed.

2:17:14

Okay, let's follow this thing, everyone.

2:17:18

Export is done.

2:17:26

Client is done.

2:17:28

Okay, I think this should not be required.

2:17:39

H.TPSolama.com.

2:17:51

Beer plus the token, that's correct.

2:17:57

Post.

2:18:09

Guys, there is some difference in the...

2:18:16

Okay, okay, okay, okay, okay, so once we have pulled the model, got it.

2:18:23

So I think everyone from the documentation, it is visible that this is the open source open model,

2:18:30

GPT OSS, open source, 120B cloud.

2:18:35

So it is telling us to pull the model and then use this model.

2:18:38

use this model. So here let's try to change the model. It is just the model problem, not

2:18:44

anything else. The request is absolutely correct. Now I think we are getting the response.

2:18:54

Okay, so you just have to figure out that which model is actually available that you can call. First

2:18:59

you'll have to just, you just have to tell the local O Lama to pull that model. So it is not downloading

2:19:05

the model, rather just it is allowing the model to call.

2:19:08

via API request. Okay, now if you see everyone, it is making a call to this model.

2:19:12

But everyone, if you see, we have not installed this model. Okay, if I go to this, Olamas list.

2:19:21

Okay, but is it running locally? Yeah, it is not running locally. Does it make sense to all of you?

2:19:28

It is not running locally. And if you see everyone here, if you see this model is also not downloaded locally, right?

2:19:34

This is just a way to local Ollama to

2:19:38

know that which cloud model we are using. If you see that size is null, there is no size.

2:19:43

Okay? Are you guys getting this point? Are you guys getting this point? So whichever open source

2:19:50

model on the cloud that you want to use, you just have to kind of make an entry for that in the Olamal

2:19:56

local and then you will be able to use it. And now if you see even, we are able to get the response.

2:20:02

Getting the point of you. Folks, so now we have seen that how to make.

2:20:08

make a call in the local machine, how to make a call on the cloud machine. Is everyone clear with both of these things?

2:20:15

Okay. Now folks, there is one very good thing just going one step ahead. I have added some extra code in the nodes to switch from local model to the cloud model.

2:20:37

just by very small change.

2:20:39

Okay?

2:20:40

So what you can see in the notes is that I have added a very small piece of code.

2:20:45

That you can add, for example, let's say here if you see, there are two different ways in which you are making a call.

2:20:52

A local call and the cloud call.

2:20:56

So can you combine both of these codes and maybe take some another variable which is called as mode?

2:21:03

So mode can be the value of these codes?

2:21:06

can be the value of the mode can be local or cloud.

2:21:10

So based on this, you can decide that if mode is equal to equal to local, then make a local call.

2:21:22

Make a local model call.

2:21:26

Else make a cloud model call.

2:21:33

Now guys, this is your homework.

2:21:35

Will you be able to call?

2:21:36

combine both of these files and just with simple defense condition.

2:21:42

Will you be able to do so?

2:21:43

For your reference, I have added the code in the notes.

2:21:52

Okay?

2:21:53

Now everyone, if you go through one last thing of the of today's class, if you go through the models available on O-Lama,

2:22:00

it does not, if O-Lama is free, if O-Lama gives you open source models,

2:22:05

open source models, if Olama allows you to download the models, that clearly does not mean that Olama just has simple models.

2:22:13

If you select for, let's say, thinking, it will give you the models which are very, very good for thinking use case, right?

2:22:20

Some reasoning, some complex use cases.

2:22:23

If you look at, for example, this Nemotron, right?

2:22:25

This Nemtron is a NVIDia Nimodon 3, nano-Omini, is a multi-model.

2:22:30

Anyone can tell me the multi-model?

2:22:32

What is the definition of multi-model?

2:22:34

Sorry.

2:22:35

this multi-model, large language model.

2:22:38

What is the meaning of multi-model?

2:22:40

Multi-model means that the model which can work with text, audio, video, images, etc.

2:22:48

Make sense?

2:22:49

Some models are only text models.

2:22:51

For example, if you see that Cuban 2, if you see that all of these are very simple models and they are just text models.

2:22:58

Make sense everyone?

2:22:59

You can just give the input in the form of text.

2:23:02

But if you look at this complex model, first of all look at the size.

2:23:04

of all look at the size. It is 28 gb. And what does it support text and image? If you go

2:23:11

to even bigger models, it can even support videos, it can even support vision, right? If you look

2:23:20

at the vision, then let's say, I think if you go to mistral medium or even the

2:23:26

Gemini text and image, okay? I think can we see, can we see, can we see,

2:23:34

can't be sought out. There are few models, everyone, which are very big. Deepseek,

2:23:41

OCR, they might be very big models. Okay, 6, 7 gb. But yeah, I hope you understand that Olama,

2:23:47

if Olamai is free, it is giving you open source model, that clearly does not mean that. It just contains

2:23:51

very simple models. It is having very big models as well. If you go to Lama 3.2, it is having 90 billion.

2:23:58

Okay? Just look at this, 55GB. It is a pretty big model.

2:24:04

It has models even for terabytes of RAM, okay, terabytes of usage.

2:24:11

Is that point clear to all of you? Okay. So O-Lama gives you models for text, image, audio, video,

2:24:20

files, PDF, and whatnot. Okay? So you just have to get the right model. It can even give you

2:24:26

models to write the code as well. Okay. So for example, if you go to this and if you put a filter of code,

2:24:32

Okay, models and some code models.

2:24:38

Code Lama, right?

2:24:39

They are very big models.

2:24:41

Code models like 39GB.

2:24:44

Code Lama, 70 billion parameters.

2:24:47

Books, clear or not?

2:24:50

Large language model that can use text prompt to generate and discuss code.

2:24:55

Folks, yes or no?

2:25:01

Folks, this is what?

2:25:02

we want you to discuss in today's class. Okay, let me push the code first of all.

2:25:16

Then everyone, so this is the link of the code.

2:25:25

Just one assignment for today's class, everyone, please make sure that you try to write both the applications,

2:25:31

local as well.

2:25:32

and cloud as well, and trying to combine both of the code with the help of if-help

2:25:36

conditions.

2:25:37

Rest everything we have done in the class.

2:25:39

Okay?

2:25:40

This is the code link, everyone.

2:25:41

I will also upload the notes and just wait for a few seconds.

2:25:44

We will also have the quiz.

2:26:02

So guys, these are the notes for today's class.

2:26:16

Can you check if you are able to access these notes?

2:26:19

And now let's go to the quiz.

2:26:32

So, folks, please join the quiz.

2:26:47

Please check in a minute, Sandhya, you should be able to access because it takes some time to render the page.

2:26:59

Folks, please join the quiz.

2:27:02

or by the link that I've given in the chat.

2:27:32

Okay. Join the quiz, everyone. Join the quiz. Shall we start?

2:27:51

Everyone, if you have not joined, please join soon. We are just starting with the quiz.

2:27:56

Okay, let's start. Here is the first question, everyone.

2:28:02

command to use if Olamah is installed.

2:28:32

it tells you the version second question if you have this command olama run and some model

2:28:46

what does this command do

2:29:02

Okay, almost all of you got it right, runs the model. Correct.

2:29:09

Third question.

2:29:12

Which command shows the list of the list of locally downloaded models? I think we have used

2:29:31

10 like multiple times today. Olam list. Correct. Very good.

2:30:01

related to today's class. It is from the previous classes. Embedings.

2:30:06

Last question, everyone. Here we go. Fifth question.

2:30:31

It is used for images. Okay. Good. So guys, let's see the final leaderboard. Who is at the top?

2:30:51

Vote Gott. Who is who is this guy? Vote goat?

2:30:55

pillar. Great. Okay. That's it everyone for today's class. I hope all of you enjoyed the class.

2:31:04

And folks, let's just quickly mark down what all the topics we have covered today from the actual

2:31:10

agenda. Okay? So let's mark it down.

2:31:18

So understand and run locally. Install Olama. Pull a light local model.

2:31:25

should avoid pulling heavy models. Obviously, RAM, hard disk and whatnot. Okay.

2:31:31

And then everyone, we have described trade-offs, very big model, small model. Obviously, we know that.

2:31:37

We discuss that. Script to run APIs, done. Create Olam account done.

2:31:46

Host setting done. And API key. Localite model with cloud, done. Done. List the main things

2:31:52

Olama can do chat, text generation, embeddings, etc. It can also do embeddings, audio

2:31:58

generation, video generation and whatnot, right? Main models through Olamma. So we have discussed

2:32:04

like few models. There are like hundreds of models available for different, different use cases,

2:32:08

right? And we have the Python script ready, which is working for both. So if you see in the

2:32:14

agenda, we have either local or cloud, but we have discussed both of them. Okay? So if we discuss one of

2:32:21

them also, it is okay. But we have discussed both of them. Now you just try to write both of

2:32:25

them on your room. So we have successfully completed all the agenda items for the class.

2:32:30

Okay. That's it, everyone. Now we will launch the feedback pool. Please take the feedback pool if you

2:32:36

like the class today. And then we will end the class. Thank you so much for attending the class, everyone.

2:32:41

Have a good day. I hope I was able to take the class in the, in the full energy.

2:32:46

Despite being very, very unwell today, I hope you like the session.

2:32:51

everyone have a good day thank you have a good day and take care good night

2:32:56

I hope you like the session thank you bye bye yeah so I think by Wednesday I'll be

2:33:04

fine I'll be I'll be I'll be in the full stand once again thank you thank you everyone

2:33:11

thank you okay thank you everyone we drop off now we can drop off thank you so much and bye bye

2:33:21

Thank you everyone. Thank you very much, sir. We'll meet again Wednesday.