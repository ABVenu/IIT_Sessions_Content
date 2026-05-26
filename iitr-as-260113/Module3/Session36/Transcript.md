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

Hi,

14:43

Hi, everyone.

15:06

Welcome to the session. Welcome people, sir.

15:10

We'll start in a couple of minutes in this channel.

15:16

Hope you had a great exam yesterday.

15:21

So you can start.

15:26

So you can start.

15:36

Thank you.

16:06

Thank you.

16:36

Hi, everyone, good evening.

16:47

We'll start in two three minutes.

16:49

Let's wait for more people to join and then we'll get started.

17:06

Thank you.

17:36

Thank you.

18:06

Thank you.

18:36

Thank you.

19:06

Thank you

19:36

Thank you

20:06

Thank you

20:36

Thank you.

20:40

Hi, everyone, uh, very good

20:46

Hi, everyone, uh, very good evening.

20:51

Hi, everyone, uh, very good evening.

20:56

Folks, uh, am I audible to all of you?

21:00

Am I audible to all of you?

21:06

Okay, great. Good evening everyone and welcome to the class.

21:10

Folks, I'll keep my camera off today.

21:12

I think there is some reflection from the from the back.

21:16

Okay.

21:17

So folks, welcome to the class and today we will be talking about

21:23

Langchain.

21:24

Okay.

21:25

In the last class, everyone, did we write some code for Langchain?

21:28

Do you remember?

21:30

Correct?

21:31

What did we do in the last class?

21:32

Could you recall?

21:33

Let me know.

21:35

What did we do in the last class?

21:42

Let's see how many of you remember that?

21:46

Did we build some Langchain applications?

21:56

Did we build some like couple of Langchain applications on Wednesday?

22:02

If yes, what applications did we build?

22:04

did we build?

22:05

Remember?

22:06

Let me show that to you.

22:08

Just a second, everyone.

22:10

Let me give you a quick recap.

22:12

Let me give you a quick recap.

22:16

Yeah.

22:17

So, Langchain, what is coming?

22:22

Okay.

22:24

So Langchain introduction?

22:27

Yeah.

22:31

So we had this discussion about Langchain and also we wrote some

22:34

code right? Correct, everyone. We did write some code as well. So on 20th of May.

22:44

And this is the code I can see. Same on 20th of May. Yep. Yeah. Can you see that everyone now?

23:00

In Langchain applications, we built Application 1. In this application everyone, everyone,

23:04

what did we, what did we do? If you look at this application, we implemented, we added

23:10

Langchain Open AI, and we imported Chat Open AI. Can all of you see my GitHub screen?

23:20

Right? Yeah. So we integrated, we imported Chat Open AI.

23:27

First of all, everyone, yeah, before using this, first we hardcoded the prompt, and then we used prompt

23:34

template. Remember? Then we used Prompt template. We imported Langchain OpenAI, this is what we installed. Then Langchain Core. From Langchain Core.Promts, we imported Prompt template. Then we created the client object. Client is equal to chat Open AI. We defined the model. Then if you remember, we also gave the Open AI key in the environment variable. Correct, everyone? Right? We gave the Open AI key in the environment variable. Then we defined the prompt template. Prompt template.

24:04

dot from template. So this is the prompt template that we have. So whatever variables we define everyone,

24:10

we do that via curly brackets. So any, anything that you define inside curly bracket, that acts like a

24:17

variable. Correct everyone? That acts like a variable or that acts like a placeholder. It means that while

24:24

invoking the API, while executing the code, you can give any value to that placeholder, to that variable.

24:30

So that you don't have to write the prompt again and again.

24:34

so that you can reuse the prompt.

24:36

Everyone, clear?

24:38

So that you can reuse the prompt.

24:40

Folks, clear?

24:41

Then everyone, we defined the prompt by giving the value of the variables, topic, audience, tone, and limit.

24:49

Okay?

24:50

Then we executed or invoked the API.

24:52

Then we printed the response.

24:54

Correct, everyone.

24:55

And then everyone, we also talked about Langchain expression language, L-C-E-L.

25:01

This is the main topic for...

25:04

Today's class. Today we will try to build some applications, a couple of applications

25:08

using Langchain expression language. So Langchain expression language, that is LCEL, allows us to

25:15

connect components with a pipeline, with the help of a pipeline. I'll show you that particular thing.

25:20

Then everyone, we built application to app2.py. And here everyone, we use the same prompt

25:25

template. And then we used everyone, something called a string output parser.

25:31

Correct?

25:31

then we use something called a string output parser, right?

25:36

We will use today as well, string output parser.

25:40

Without string output parser, everyone, model returns the complete response object.

25:43

Basically, that is a AI message.

25:45

I will define that today more formally, right?

25:48

And with string output parser, we just get the content in the form of string.

25:54

Everyone clear?

25:55

And this is how we define a expression language, L-C-E-L, Langchain, expression language.

26:01

So prompt will go to LLM, LLM will make the, LLM will generate the response, and the

26:09

generated response it will pass to output parser.

26:12

And then it will invoke the API and you will print the response.

26:16

Is everyone clear?

26:17

This is what we did in the last class.

26:21

Everyone aligned?

26:22

Very good.

26:23

Now, everyone today, what are we going to do?

26:25

Today, we will continue our discussion and we will implement few applications using

26:31

Lanchine expression language.

26:35

Okay?

26:36

So today's main agenda is going to be L-C-E-L-C-E-L-L, which is

26:47

is Lanchine expression language.

27:04

Okay.

27:08

Now, everyone, what flow we are going to build in today's class, the flow we are going to build in today's class.

27:12

The flow everyone is going to be very, very similar to what we have done already in the past.

27:16

We will have some input.

27:17

data, this input data, we will, using the input data, first of all, we will create

27:26

a prompt template.

27:28

Anywhere we will not use any hard-coded prompt that is not reusable.

27:32

So we will always use a prompt template.

27:35

So whatever input data is coming, we will pass it as variables inside prompt template.

27:40

The prompt, we will generate from the template.

27:43

We will pass to the chat model.

27:47

chat model and from chat model everyone whatever output we are going to get we will

27:53

pass it to output parser and from output parser everyone we will get the final response

28:00

we will get the final response this is going to be the complete workflow

28:08

everyone clear so langchain expression language L-C-E-L

28:17

What it does, it allows us, L-C-E-L allows us, allows us to compose, to compose the, to compose the, to compose the chain or pipeline using pipe operator.

28:47

using the PIP operator.

28:54

Everyone, clear?

28:56

So Lanchine allows us to compose the chain or pipeline using the pipe operator.

29:00

It means that even if you have to create a chain, you can simply do like this, that chain is equal to,

29:06

first you will have the prompt, you will generate the prompt using the template.

29:09

Prompt, everyone, you will pass it to model or LLM.

29:14

Okay?

29:15

And whatever output model is going to generate,

29:17

that you will pass to output parser.

29:20

Correct, everyone?

29:21

This is what we do.

29:22

So everyone, instead of writing in a complex way, you can simply do it via pipe symbol.

29:29

Okay?

29:30

So if you see on top of your enter tab, enter button, you will see that there is a pipe symbol.

29:38

Can you see that?

29:40

On top of your enter button in your laptop, in your keyboard.

29:45

Right?

29:45

So that is pipe symbol.

29:46

Right.

29:46

So this pipe symbol, right?

29:46

So this pipe symbol, everyone, you can use to create a pipeline, to create a chain.

29:54

Correct, everyone.

29:58

So should we start writing the very first code for today's class?

30:02

So everyone, now what are we going to do today is?

30:04

So in the last class, I showed you to how do we use LankChane, OpenAI?

30:11

Correct?

30:12

Did we make a call to OpenAI model, GPD 5.2?

30:16

So Lankchain gives you a library called as Lankchain underscore OpenAI that we imported

30:23

first of all, that we installed first of all, PIP, PIP3, install, Lanchine, open AI.

30:28

Then we import it and then we use it to make a call to open AI LLM models.

30:34

Remember?

30:41

Yes or no, everyone?

30:43

Today we are going to use, yes, we are going to use, so will, another model.

30:46

Okay?

30:48

So today everyone, what are we going to do is, today we are going to integrate.

30:53

So in the last class, we used Open AI.

30:55

Today, everyone, we are going to not use, we are not going to use Open AI, rather we are going

31:01

to integrate Lang Chain with O'Lama.

31:06

How many of you remember O'Lama?

31:10

So this is the new part in today's class.

31:16

What is?

31:16

O-Lama everyone? Can you tell me? What is O-Lama? We had a full class on

31:27

O-Lama, right? This is the class. Open source LLM provider, very good. So if you see

31:33

everyone, O-Lama is a tool that helps us run LLM locally and use them. Okay, it is kind of

31:42

a marketplace where multiple open source models are

31:46

present that you can download and that you can pull and use it in your own laptop.

31:52

Use it on your own architecture.

31:55

Correct, even?

31:55

And O-Lama, you can use either on cloud or you can use on local as well.

32:00

Generally, everyone, generally if you're using O-Lama, you will find out that mostly people uses O-Lama on local.

32:07

It means that using O-Lama, you download the models, right?

32:13

So what generally people does?

32:15

using O'Lama, download the model, whatever you want to use, depending on your

32:30

use case, depending on your configuration of the laptop, depending on your architecture, using

32:36

O Lama, download the model, and then run it on, run it on, run it on.

32:45

own architecture.

32:52

Okay?

32:53

Now everyone, this architecture part is provided by O-Lama also.

32:58

O-Lama also says that, okay, if, because I didn't see, if I'm a small company, right, if I run a

33:03

small company, if I download the model, which is free, which is free to use.

33:08

But everyone to run that model on machines, on servers, on CPUs, on GPUs, on GPUs,

33:14

Will I have to pay money for that?

33:17

Will I have to buy machines?

33:19

It is costly, right?

33:21

If you are running a decent model, a bigger model, you will have to spend money for that.

33:24

Also, everyone, it's not one-time thing.

33:26

It's not like that, okay, you buy the machine once and you can use them forever.

33:30

You will also have to keep on monitoring that.

33:34

You need a good number of people.

33:36

You need a complete DevOps team who can help you to run those models for a longer period of time.

33:42

Correct or not?

33:43

Folks clear?

33:44

And that's for everyone, you have the concept of cloud.

33:51

So Olamas says that, okay, if you are not able to run the architecture on your own, if you don't

33:56

have enough resources, if you cannot spend a lot of money beforehand, right?

34:01

Because if you are buying your own machines, you will have to pay upfront.

34:04

For example, let's say if there is some server, which is of, let's say, $5,000, right, you'll have

34:08

to spend that upfront.

34:09

Now, a lot of small companies might not have that kind of money upfront.

34:13

So what do they do?

34:13

They use cloud.

34:14

so now what do they do everyone they rent out the machines they take machines on rent

34:20

and then they can pay for the architecture pay for the machines on monthly basis just like a

34:26

bill is that point clear of you everyone clear okay but everyone now it's completely up to us

34:35

whether we want to use O Lama on local or cloud for testing purpose everyone it is 100% okay if we use on

34:42

local. Correct, everyone. Isn't it better to run Olama Cloud, we can use better

34:50

versions of that particular model? You can use the same versions on your own laptop as well. But if you

34:55

see, if you're running cloud, again, you'll have to spend money for that. Right? For example, let's say

34:59

just for testing, if you're using Olama Cloud, okay, Olama Cloud, or if you're using Open AI,

35:06

if you have already money in Open AI, for example, if you already have a subscription of OpenAIA or Gemini, do you

35:11

need to pay money to Olama cloud as well? Not really, right? If you just want for the testing

35:17

purpose, you can either use open AI or Gemini or OLAMA local or cloud does not matter. One of

35:24

them could be cloud. For example, let's say we have already seen, you can say that we have already seen

35:30

LLM's LLM via open AI. So don't you think open AI gives you LLM on cloud? Correct, because you are not

35:39

managing the infrastructure.

35:41

Right, so we have already seen that. Now, we can focus on the local part. If you're using O Lama, we can focus on local cloud. So anyways, we see that via open AI multiple times. But using open AI is very, very similar to using OLama cloud as well. Just the name is going to change in Langein, it is very, very similar. Okay? If you want, like, I can show you that as well. It's very straightforward. But in the previous one, we used one model for free.

36:11

was local. Okay, I was using the model from local. You mean the open AI model for free?

36:23

Are you saying that? We are using open AI model for free? OLama is free. OLama is free. OLama for

36:32

free. We did not use OLama cloud in the last class. Okay. We used OLama on local. So what did we do? We pulled the model. We downloaded the

36:41

in the laptop and then we used it. Okay? On local host. Remember that?

36:49

Just modeled out. Is it edge service we could recommend customer, we could recommend customer

36:54

Olama? Is it edge device? Is it for edge device? We could recommend customer Olamma?

37:06

Answer is yes. Okay. So Olamma takes care of all the architecture, every device. Okay? That is not a problem.

37:11

Yes, absolutely sure. We use some quen model locally in the Olama class. Do I need high

37:20

configuration GPU for Olam? Lama? Not really. See, Olama is a marketplace. Okay? So Olam is not a very

37:27

heavy process. So O'Lama gives you the support of hundreds of models. Hundreds of models. So you can

37:35

select the model based on your use case, based on your machine configuration, right?

37:41

So there are models which just needs 500 Mb of RAM, MB. Okay? And there are models which would need 100 gb of RAM.

37:50

So it is completely up to you, Shivam, which model do you want to use based on your configuration?

37:56

Now, whenever you are using O Lama for your project learning, for your learning or for any development project, I would always recommend you, don't go with model bigger than 1GB or 2GB of RAM maximum.

38:10

Okay.

38:11

like you will have to like your laptop will become slow right shivom but Olama gives you

38:17

models with very small RAM as well 300 400 mb okay and you can even go up to 100 gb 200 gb of

38:23

rap so we can go with very small models up to 1 gb it is good enough clear okay so let's start

38:33

uh the usage everyone let's start writing the code

38:38

everyone aligned till this point of time so now the agenda for the class is going

38:41

to be, we will be using, we will be integrating Olama, Langchain, Langchain,

38:47

language, output parsers, prompt template, all the things. Clear?

38:55

Okay. Perfect. So let's get started.

39:08

So folks, let me just.

39:11

Let me open the project. Let me share the code screen first.

39:41

Yes, everyone. So this is the project that we have on VS code, the Langraph application. And we can, we have two applications, App 1 and App 2. Okay. Let me also give you a quick recap of how did we use Olama? I think Olama code we wrote in

40:11

Where, e-commerce rag? Yes. Okay, in this. Remember? So,

40:19

So, e-commerce rag, we created a folder, we downloaded a model, then we created a model, we downloaded a model,

40:41

then we gave the API path, which is the local API path, local host. It means that the model is running on my local server, that is on my laptop. Then we gave the model name Quen 1.8B. Then we wrote the prompt. Then we gave the payload. Then we made the API call and then we printed the response. Okay. Then we wrote app to. App 2. What did we change? We are, I think, checking the, yes. Now if you see everyone, we are also, okay, did I show?

41:11

you the Olama Cloud as well. Yes, everyone? I think we have seen Olama Cloud as well. I forgot. Yeah, now I can remember at the end, we had a demo for Olama Cloud as well. Correct? So both the things we saw. Olama Local, Olama Cloud. Right? So any one of them we can use today as well in the exact same way. Okay? Yeah, actually I was not able to recall that yes, we did Olam Cloud as well. Perfect. Anyways.

41:41

Then it is good. Okay, now everyone, let's start writing the code for today's class. And we will go to Langchain application,

41:47

this folder, this project, and we will create a new application here, App 3.Pi.

41:54

Okay, third application for Langchain. So what are we going to build for this, everyone?

42:00

Again, we will follow the same approach. We will use the O-Lama base URL.

42:04

Okay. What was the base URL, everyone? So let me just copy paste that. So new window.

42:11

From that, that only everyone, I will open.

42:41

114.34 is the default port number slash API slash chat and Quinn 1.8b, we can use this.

42:49

Then everyone we have.

42:52

Base URL is okay. Model is this. Okay, we will give the base URL.

43:11

base URL. This is the base URL, everyone, till port number.

43:23

Okay. Perfect. Let me just set up everyone. Then I will explain step by step everything. And then the next thing that we have is, if you're using local, do we need the API key?

43:35

If you're using the local running model, do you need the API key?

43:41

No, API key would not be required. Okay? Then the next thing that we need is, now we can start writing the code.

44:11

Uh, okay. Okay. So we can start writing the code.

44:41

install langchain hyphen o llama install this already installed good enough uh pip3

44:50

install what else do we need uh we need lanchine core okay done and then we need i think i think that's

45:03

it okay so now everyone what we will do is we will import the things that from langchain underscore olama

45:11

import. So, folks, from here, we are going to import a model which is called us chat

45:18

O Lama. Okay, chat O Lama. It is a model that we, that we're going to use in the local. Okay, so

45:24

basically this is kind of a wrapper. Make sense? This is kind of a wrapper that we are going to use,

45:29

which will provide us the APIs for chatting with the O Lama model, which is running via O Lama.

45:35

Okay? The model could be anything behind this. Okay. Then everyone, from

45:40

from Langchain underscore core dot prompts import prompt template we will use the prompt

45:54

template okay and then we will also use from Langchain core dot outputs dot output's

46:10

So these three things we will import, okay? And then everyone, we will start writing the codes.

46:18

So the first thing that we need is everyone, we will build the chain. So we are writing the function,

46:23

define, build chain.

46:29

Build chain.

46:32

Now in this everyone, what do we need to do is we will build a very simple chain. What chain we will build a very simple chain? What chain we will build?

46:40

Just a comment. First we will have prompt template. From prompt template, we will pass to O Lama, that is a model. Chat O'Lama. And from O Lama, we will pass to output parser.

47:01

Output parser. Everyone clear? Is everyone clear with this chain? In fact, we are going to pass to string out.

47:10

Let me write the name as it is.

47:16

What to do if the model I want to use has no Lanchine library?

47:22

Generally, that does not happen. If you see all the major models that you use, OpenAI, Olam

47:28

or all the major LLM providers, they have libraries for most common frameworks like Lanchine.

47:37

Lankine is anyway by far the most popular one.

47:41

So you will find any model rarely which does not have the required libraries for Lankine.

47:48

Okay, generally that does not happen.

47:50

Because otherwise people will stop using that.

47:53

Why people would use that then?

47:57

Okay?

47:58

Take it.

47:59

Now everyone, we will write the prompt.

48:03

So, instead of writing the prompt from scratch,

48:06

Okay, in the last class, I think I showed you prompt template.

48:09

Now, today, let me show you a different template, which is chat prompt template, which is also

48:14

very, very similar even. The only thing that we have is prompt template can be a bit more generic.

48:20

Chat prompt template is generally used for chatting kind of use cases, right, when you want to have

48:26

one-to-one conversation. Rather than having some kind of agentic use case, if you just want to have a

48:31

chatting conversation or a chat or a simple conversation, then you can use chat prompt template, right?

48:35

very, very similar. Not much difference. Okay. Now, everyone, first, we will use the prompt,

48:41

we will build the prompt template. Okay. So let's write the code one by one instead of, yeah,

48:45

so prompt is equal to chat prompt template dot from, from template. If you see, we are,

48:54

we created, we use the prompt template as well in the exact same way, prompt template dot from

49:01

template. Okay, in the exact same way, we use this as well.

49:05

And then everyone, uh, we will define the prompt. And in the prompt everyone, actually

49:13

the prompt example that I have is a big, bigger one. So let me copy paste it. This is anyways, a simple

49:20

prompt. So look at this everyone. What we have? In this prompt, everyone, we are giving

49:30

an array, a list, right? If you see a list, in this list, we are passing two parameters, right?

49:35

the first parameter and the second parameter. Because everyone, in the conversation,

49:39

generally, there are two people. Now, what system responds? What is the role of the system and what

49:44

prompt we are giving to the system? That you are a beginner-friendly programming, beginner-friendly

49:48

programming instructor. And these are the rules that you need to follow. Make sense? And what we are

49:55

expecting from the human, from the user, that you are a human, and you can give prompt like this.

50:01

Explain this particular topic using a simple analogy from

50:05

this domain, from analogy domain, right? From this use case. Are you guys getting

50:11

this point? Now everyone in a chatting example or in a chat bot kind of a system, if you're building

50:17

a chatbot using Langchain, then there will always be two candidates. One will be the system

50:22

who is, what do you say, who is giving the responses? And one is the user who will, what do you say, who will

50:30

ask the questions. Correct everyone?

50:38

Folks clear.

50:42

Okay. Now folks, we will build the model. Okay. Now, this is building the prompt template. This is the first

50:48

thing. Let me put a comment here. Build, chat, prompt, template. Now, even the second thing is,

50:57

after this, we will build the model object. Now, how we are going to build the model object?

51:03

This is, we will build step by step. So, let's see, model is equal to chat O'Lama model. And here

51:11

everyone will have to pass few parameters. First, everyone, we will have to pass the model object.

51:17

Right? That, if you see everyone, chat O'Lama is a wrapper. Okay, let's call it as LLM. Okay,

51:22

chat O'Lama is a model, is a model wrapper. Using chat O'Lama, you can use

51:27

any model which is coming via Olama. So somewhere, everyone, you will have to define the model.

51:32

Where the model is coming from. Are you guys getting this point?

51:38

Right? So, for example, everyone, we already have this model running in my system. So we can use

51:42

directly this model name, right? That I want to use this particular model in my application, right?

51:48

Model is equal to model name. This model we want to use. Folks, clear?

51:54

Then just define the model. Then define the model. Then define the model. Then define the

51:57

the base URL that where that model is running. So guys, all of you agree that this is

52:02

the base URL and everyone, there is another parameter called as base URL, base underscore URL

52:08

is equal to this one. Correct. Everyone? This is the base URL. Where your model is running.

52:15

Now there comes a difference, everyone, that the URL can be the local host URL or it could be

52:21

the cloud URL. Clear everyone? It could be the local host URL. It could be the local host URL. It could be the

52:27

cloud URL as well. Whatever you are you are going to give, then you will be using

52:32

that particular service. Okay? Folks clear. Very good. Then everyone, you can define other

52:40

parameters. Again, these parameters are optional. Only these two parameters are required

52:44

parameters. If you are using everyone, if you are giving the base URL as, what do you say,

52:51

what is that called as cloud? If you are using the cloud, then you will have to provide the API key also.

52:57

Remember? Then you'll have to provide API key also. But in our case, everyone, because we are using

53:02

local host, API key is not required. Correct? API key is not required. Then everyone, we can

53:08

define some other parameters like temperature. Do you remember what is temperature, everyone?

53:16

Temperature? Between what was the temperature value? What was the range of temperature value?

53:27

0 to 2. Towards 2. Temperature value is very high. It means output will be very creative.

53:34

Temperature value is very less. It is very, very strict output. So we can give, if you want

53:41

anything, right, you can give temperature is equal to 1 or temperature is equal to 0. It does not matter.

53:45

I'm just showing you everyone that you can provide temperature value as well. You can control

53:50

how your model is going to behave. How your model should behave, you can define that here.

53:57

So generally everyone, temperature value is generally one.

53:59

When you want not very creative outputs as well as not very strict outputs.

54:05

Folks clear?

54:07

Okay.

54:08

Then you can give other parameters as well like number predict.

54:12

For example, if you want expected number of output words, or I think this is correctors,

54:18

how many words or how many tokens do you want in the output?

54:22

Approximately.

54:23

For example, if you say that 100, it means that you will have approximately 100 words.

54:27

in the output. Again, this is, this is not required. You can remove it. These are, only

54:33

these two things are actually required. It is like a token limit, yes, in the output value. So

54:39

this is how you build a model. Everyone clear? This is how you build a model. So everyone,

54:50

now if you see what we have done? We need three things, right? First, we need template. Have we created

54:57

the template? Have we created the template? Yes. Have we created the model? Yes.

55:04

Only thing is output parser now. Okay. Then you just need the output parser object. Parcer is

55:12

equal to string output parser. That's it. So now we have all the three required parameters.

55:18

What do you say? Prom template, model and parser. Now you can create a chain. Chain is equal to prompt template.

55:27

prompt, whatever name we have given, what name, what is the name? Prompt only. Then prompt

55:31

after pipe, pipe symbol, LLM, pipe symbol, parser. That's it. This is your

55:38

Langchain expression language. This is your L-C-E-L. Everyone getting this point?

55:51

This is your Langchain expression language.

55:55

Correct?

55:57

And everyone, if you see what this function is doing, this function is building the chain.

56:01

So after building the chain, we will return the chain.

56:06

Correct?

56:08

Folks, how many of you are 100% clear with this idea? That what we have done?

56:17

Just if you want to go through this once, you can go through.

56:21

First, we are building the prompt template, very, very similar syntax that we used in the last class.

56:25

Then we are building the element.

56:27

LM model. Then we are building the parser. Why we are returning the chain? Because in

56:31

future, we are going to use this method multiple times in multiple files, right? So that we don't

56:39

have to copy paste again and again. So what we can do, we can directly import this function from

56:44

App 3 and we can directly create a chain. Okay, Chira? Okay. Now we will create the chain.

56:51

Chain is equal to build chain. Okay. And now we will do chain.

56:57

Make sense, Chirap. Now, for example, let's say in future, I create App 4 as well.

57:03

Okay, app 4.p. Now, in app 4 as well, I want to build the similar kind of chain. I don't have to

57:08

copy paste the code again and again. What I can do from App 3, I can import build chain and I can simply do

57:15

chain is equal to build chain. Getting the point, Chirap, code reusability. That's why we are

57:21

returning chain here. Now, this function is completely interesting.

57:27

independent. Okay? Now everyone, we will invoke the chain. After invoking the to invoke the chain,

57:33

everyone, could you tell me what input parameters we need to pass to invoke the chain? Everything is

57:39

written in front of you. Please let me know. So the chain is basically passing the variables

57:45

as parameters to the variables defined it before it. Absolutely correct.

57:52

What parameters do we need to, in, uh, to, uh, to, uh, to, uh, what parameters to,

57:57

we need to pass to invoke the chain.

58:08

Only two parameters, topic and analogic, correct?

58:13

So, we can simply pass. And how do we pass these, these things in a simple JSON object?

58:27

topic is what do you want to explain? Let's say topic is, uh, langchain expression language

58:35

in language. This is what I want AI to explain me. And some real life example, analogy domain.

58:42

Maybe let's say everyone, analogy domain. So guys, you need to make sure that the variable names are

58:48

exactly similar. Analogy domain. Analogy domain is let's say maybe something in software engineering.

58:57

Okay. So you will get the result.

59:03

Now everyone, this result that you will get, in what format will you get this result?

59:09

In what format you will get this result?

59:12

You will get this result in the string format, right?

59:16

Because you are using an output parser. If you see, this chain will have three components.

59:21

It will have the prompt. It will have the model. It will have the parser.

59:25

So the output of one.

59:27

component will be passed as an input to the next component. And output of prompt will be

59:33

given to LLM. Output of LLM will be given to parser. And then we will finally print it. How many

59:40

if you are clear? If yes, we can start running the application. We can try to run the application.

59:46

Does the method name always should build chain? No, no, it can be whatever. This is just like

59:50

if you let's say, if you say that, build simple language.

59:57

simple chain using langchain expression language, whatever you want to give.

1:0:05

Okay?

1:0:06

This is your method that we are writing.

1:0:09

Okay?

1:0:10

Let me see.

1:0:14

Yeah.

1:0:15

Yeah.

1:0:15

Very good.

1:0:16

So let's try to write everyone, Python 3 and app 3.3.py.

1:0:20

So let's execute everyone.

1:0:22

There are some errors.

1:0:23

What are these errors?

1:0:26

Prompt.

1:0:27

Prompt in, okay. So I think prompt me, there is some syntax error. What is the syntax error?

1:0:33

Okay, you are closing. It is saying that expected string got list.

1:0:41

Okay.

1:0:57

I think everyone, I will have to check the syntax.

1:1:27

There is a small error in the syntax.

1:1:44

Let me just copy paste that on GPT.

1:1:46

And we should be able to identify that.

1:1:57

Somewhere I think extra bracket is there or let me analyze.

1:2:07

The issue is this from tablet expects one string template, not a list of chat messages.

1:2:24

Since you pass the list list this.

1:2:27

Okay, I think everyone we are using different, a wrong method here.

1:2:38

Not from template, it is from messages.

1:2:41

Okay.

1:2:42

So, folks, very simple.

1:2:44

I used a wrong method here.

1:2:47

It should be from messages.

1:2:49

Okay.

1:2:50

From template, use, from template expects one input.

1:2:55

Because you are using a change.

1:2:57

chat model, that's why you are passing messages. From messages expects two input

1:3:02

parameters. In fact, it expects a list. Okay. You can pass what a user is expecting, how

1:3:09

users should behave, and how model should behave. Make sense, everyone? So the error was

1:3:14

from messages function we need to use, not from template. Now we will execute the code again.

1:3:22

Now it should run fine.

1:3:27

Let's see. I think yes, it is running fine. Yes. Are we getting the response, everyone?

1:3:35

Are we getting the response? Yes. So imagine, in fact, let's try to learn this. This is the

1:3:40

explanation of Langchain expression language in the analogy of software development, software engineering.

1:3:45

Imagine a computer that is very powerful, yet it has limited storage and processing power compared to

1:3:51

other computers or supercomputers. In contrast, consider a smartphone that is designed to be compact and

1:3:56

lightweight, but it still has a larger screen size than most of the laptops.

1:4:02

And its processor, processing power and memory capacity are generally higher than those of traditional

1:4:07

desktop computers. In summary, the concept of Langchain, L-C-E-L, expression language in Langchene,

1:4:13

can be compared to a powerful laptop with limited storage and processing power and an advanced

1:4:20

smartphone with a larger screen size, higher processing power.

1:4:26

and more capacity.

1:4:27

Guys, honestly, tell me how many of you understood this.

1:4:31

Is it the correct analogy?

1:4:34

At least I don't, I don't find it very good.

1:4:38

I also did not get. That's why the reason is what?

1:4:42

We are using very bad model.

1:4:44

Remember, we are using this model and the size of this model was just 300, 400 mb.

1:4:51

Correct?

1:4:54

That is a reason.

1:4:56

What was the size of this model?

1:5:05

Olama list?

1:5:07

This was just 1 gb.

1:5:09

Okay, 1.1 gb.

1:5:14

Everyone, clear?

1:5:17

We can make the changes.

1:5:19

So, can you try to make the changes?

1:5:20

Or in the next example, we can make the changes.

1:5:23

Okay?

1:5:23

So, folks, if you want to use a better model, you can use a better model.

1:5:26

via cloud, via open AI, or you can download a bigger model in your laptop and you can use it.

1:5:33

But what is more important, everyone, the code is working fine.

1:5:36

Is the code making sense to all of you?

1:5:38

How to create a language?

1:5:39

How to create a language?

1:5:44

Why I'm not downloading any bigger model is there is a reason for that.

1:5:47

I have a MacBook.

1:5:48

It is quite decently powerful.

1:5:51

The reason is because I teach at multiple batches and I run multiple.

1:5:56

models and multiple things together, right?

1:5:59

In different, different batches, I give different demos.

1:6:02

And if I keep on downloading multiple things, then I think my laptop will die very soon.

1:6:06

And every time, it's very difficult for me to remember and delete the models after the class.

1:6:11

Okay? That's the reason. Because, see, you download 1GB model, you download 20 gb model.

1:6:16

Only the output is going to be different. But demo may, there will be no difference.

1:6:20

The code will remain exactly the same. You just have to change the name of the model.

1:6:24

Right. So we should focus more.

1:6:26

on the model, more on the demo. That's it. Okay. Folks, everyone clear with the code.

1:6:31

If yes, we can take a break and after the break, we will take the next example.

1:6:35

We'll take two more examples to make this concept super strong. Okay? Good. So we can take a break,

1:6:43

everyone. So it's 855. Let me push the code first of all. You can have a look at the code for two,

1:6:49

three minutes. And then we can, you can take a break.

1:6:56

Langton expression language.

1:7:16

This is a code for today's class. You can have a look at it. And we can have a break of five minutes. You can have a look at the code. Then 10 minutes, you can have a look at the code. Then 10 minutes, you can take a break. So let's meet around 9.

1:7:26

Okay. See you after the break.

1:7:56

Thank you.

1:8:26

Thank you.

1:8:56

Thank you.

1:9:26

Thank you.

1:9:56

Thank you.

1:10:26

Thank you.

1:10:56

Thank you.

1:11:26

Thank you

1:11:56

Thank you

1:12:26

Thank you

1:12:56

Thank you

1:13:26

Thank you

1:13:56

Thank you

1:14:26

Thank you

1:14:56

Thank you

1:15:26

Thank you

1:15:56

Thank you

1:23:56

Yeah,

1:24:00

Yeah, Hi, Hi,

1:24:01

Am I am I am I am I,

1:24:04

So,

1:24:05

So there is a question.

1:24:08

Can you

1:24:10

Can you

1:24:11

Why you have you have

1:24:25

mentioned, system and human in the prompt. See, it is a chat application, right? So in chat application, there will be two. There will be two parties. One will be the system who will basically that is the application who will give the answer and there is a human who will ask the question. So user will ask the question in this format and we are passing the input while calling the application while executing the application or while invoking the application. And this is the prompt that we will pass to the

1:24:54

This is the system prompt that we are passing to the system, make sense, Mukul?

1:24:59

This is, you can say that this is the system prompt.

1:25:02

Okay?

1:25:03

This is the default prompt.

1:25:06

That will go in every execution.

1:25:09

And this prompt, we will attach along with the system prompt.

1:25:15

Yes.

1:25:16

Vamsi asking another question, though it's out of context now, I have a question regarding the prompt size.

1:25:21

Is it a good practice to have the number of correctors define in each part of the part of the problem?

1:25:24

prompt with 3,000 characters, user context which is dynamic capped to a certain

1:25:30

limited number of characters. Because though character limit is more on Gemini, which I am using,

1:25:35

it is allowing some MBs of prompt though through the network. If the size is exceeded, there is

1:25:41

an error being thrown. Absolutely correct. But nowadays, that size is good enough. Okay. So you will

1:25:48

have multiple millions of characters. MB means multiple megabytes of data. So generally you don't

1:25:54

hit that limit very often, right?

1:25:58

Generally, we don't hit that limit very, very often.

1:26:01

Okay.

1:26:02

So if it is clear, everyone, should we start with the next example now?

1:26:09

Or next idea now?

1:26:13

Okay.

1:26:13

So, folks, I think we are good enough.

1:26:16

This we have understood.

1:26:24

Yeah. So let me just add this comment. What does string output parser does? Yeah. If you see, string output parser extracts text content from the model, such as AI message or AI message chunk and converts into a plain string. So whatever type of output you are getting,

1:26:53

string output parser converts the output into plain string.

1:26:58

Sounds good, everyone.

1:27:01

Okay?

1:27:02

Why we are using temperature?

1:27:03

Temperature controls creativity or randomness.

1:27:07

Okay?

1:27:12

Controls creativity or randomness.

1:27:23

Output generation. Okay.

1:27:25

Now the second part is everyone validating the chain across multiple inputs.

1:27:44

So let's start with the second code everyone, which is validating chain across multiple inputs.

1:27:48

and this, okay, actually let's call app three as, let's rename it as build chain,

1:27:58

yeah, build chain.

1:27:59

It is better naming convention.

1:28:01

And app four is, let's say,

1:28:07

validate chain.

1:28:07

Okay.

1:28:09

So first of all, everyone, in validate chain.

1:28:11

Dotpy, we will build, build the chain from build chain,

1:28:15

import, build chain using lang chain.

1:28:19

So let's build the chain first of all.

1:28:21

Okay?

1:28:22

We are building the chain.

1:28:24

And then what we're going to do is,

1:28:27

first we will define the function.

1:28:30

I'll explain step by step what we are trying to do.

1:28:33

First write a function is output valid or is valid response.

1:28:38

Is response valid, whatever?

1:28:40

Is response valid?

1:28:43

Valid.

1:28:44

This is a function I've really.

1:28:45

that we are going to write and this function will take the response in the input parameter.

1:28:54

Response is going to be of what type everyone?

1:28:58

Response is going to be of type string and what output we can expect from this function to return.

1:29:03

This function, okay, we'll define what output we can expect from this function to return.

1:29:08

Okay.

1:29:14

We can define this later.

1:29:15

Okay. This is a function. So what this function is going to do, let me write a comment here.

1:29:25

This function is going to validate, this function is going to validate, this function is going to validate, validates whether the response

1:29:45

the defined criteria or not? What is the defined criteria, everyone? These

1:29:56

are the defined criteria that we are doing. First of all, output should be string. Let's say

1:30:01

success criteria. So basically, we are just building a response validator, which will validate

1:30:09

the response before passing to the user. Okay? Not exactly bullion.

1:30:15

Mokal, it will be slightly different. I'll explain that first. Okay. First success criteria, everyone, that response should be string.

1:30:24

This is what exactly everyone, the production application does also.

1:30:28

A lot of production applications, they don't send you the response directly.

1:30:31

Because everyone, models can hallucinate. Models can always give you wrong output. Models can give you the output, which is not understandable.

1:30:38

In spite of giving good prompt, in spite of defining everything inside the prompt.

1:30:42

Everyone, clear?

1:30:43

Everyone aligned with this?

1:30:44

that models output can be ambiguous, can be hallucinated, and might not be very much user-friendly.

1:30:52

So always everyone, you validate the response before passing to the user. So how do you validate? Very simple

1:30:58

criteria, response should be string. First thing, then response should not be empty.

1:31:11

Response should be string. Response should not be empty.

1:31:14

And let's say everyone, maybe, how many bullet points do you need?

1:31:18

Let's say response should contain exactly five bullet points or three bullet points.

1:31:30

Okay?

1:31:31

Three bullet points.

1:31:33

Also, everyone, you can define this.

1:31:34

Let, let's say other things also, extra things.

1:31:37

That response should not be more than thousand correctors, right?

1:31:41

Or response should not be.

1:31:44

should not be too long. That's it.

1:31:50

Okay. Are these success criteria making sense to all of you?

1:31:56

Okay. Everyone clear? So guys, how can you check whether the response is string or not?

1:32:03

So guys, in Python, there is a function called as is instance. Okay? So you can simply check that

1:32:08

is instance. Response is not an.

1:32:14

instance of string, if this function is returning none, if not this, then it means that

1:32:21

response is not of string type. Is this point clear to all of you?

1:32:28

Response is not of string type. Okay? And everyone, you can also create one thing because you are

1:32:35

validating because there can be multiple type of errors your code can generate. You can create

1:32:40

an errors array, right? An empty array. And here.

1:32:44

you can return you can append errors dot append this type of error response

1:32:51

is not string everyone clear response is not a string and you can return and you can return here

1:33:05

what you can return first of all we are returning false we will return false we will return false

1:33:14

that is valid false and also we can return errors okay these are the two things that we will

1:33:20

return right that is response valid no and what errors we are getting is everyone getting

1:33:29

this point so everyone what is a return type we can define here what return type we can

1:33:35

define here could you tell me now let's see how many of you know python and just understands python

1:33:39

now what is this return type tell me

1:33:43

it is a first it is a bullion then it is a list of string list of string list of string

1:33:52

and it is a tuple of that correct everyone it is a tuple

1:33:59

tuple so you can define

1:34:02

tuple of string uh tuple of string uh tuple of bullion double and list of string and list of string

1:34:11

bullion and list of string this is the return type is everyone clear with this

1:34:23

that's why i was not defining this at the beginning so aren't these constraints a part of the

1:34:30

system prompt as well if you are not using them in the system prompt what is enforcing the success

1:34:34

criteria if not the lLM see this is just uh you can say that a second check okay if you see if you see

1:34:41

what we are defining in the system prompt in system prompt all of these things we are giving here

1:34:45

okay now see allens can still hallucinate even if you are using the latest model the probability

1:34:54

increases that it will follow your instructions it will give you the correct output but is it

1:34:59

guarantee it is written anywhere that lLM is going to give you the correct output answer is no that's why

1:35:04

every time we follow some kind of validation process and most of the times everyone validation happens

1:35:11

maybe in the background right maybe you and me cannot see that validation happening

1:35:16

in any application that might be happening in the background but happens okay so i'm just

1:35:21

telling you that if validation happens this is how we do that which last parts will

1:35:30

which last part is not clear the return type this is a do you know what is tuple in python

1:35:41

Do you know what is a tuple in Python?

1:35:46

Tuple is nothing but a set of values, right?

1:35:48

So if you see this is a tuple, tuple is a pair, okay?

1:35:53

Pair of what type?

1:35:54

First value is bullion, second value is list of string.

1:35:57

So it is a tuple of type bullion and the second value is list of string.

1:36:02

Second value is errors.

1:36:03

Errors may what we are doing?

1:36:05

We are adding a list.

1:36:07

In this list we are adding a string.

1:36:09

So errors is nothing.

1:36:11

but list of strings and this is a tuple where first value is bullion second value is

1:36:19

list of string tuple where first value is bullion second value is list of string makes sense for it

1:36:25

again everyone this is not a defined thing right this is what we are defining it is not a

1:36:30

hard-coded thing that you will have to use that only yes sure we can do that as well okay

1:36:36

this is the first thing everyone that we have checked that response should be string

1:36:40

then everyone what should we check that response is not empty how can you check response is

1:36:45

not empty should not be empty by checking the length uh very good but don't you think if

1:37:02

let's say response is something like this okay like this just spaces

1:37:08

response is if you if you look at the length it is not one or zero right it can be 10 20

1:37:17

anything but don't you think the response is still empty right so don't you think you should check the

1:37:22

length after you can say that stripping after removing all the extra spaces okay correct so you can

1:37:34

check if the response dot stream uh response

1:37:38

not strip after that if string is empty then you can print this thing then you can

1:37:43

append in the errors response is empty what do you think about this everyone

1:37:50

that after stripping you should check whether string is empty or not if yes then do that.

1:38:08

then everyone uh you can check this thing response should contain only exactly three bullet points

1:38:14

uh i'm skipping the code for this it is very simple python code we can write it later because

1:38:18

that is not related to anything related to a i or langchain etc response should contain

1:38:26

exactly three bullet points right try this on your own right to do okay try to do this then we can check everyone what

1:38:36

this is to do and then we can check response should not be too long uh maybe let's

1:38:41

everyone we can define uh maybe limit is 100 characters whatever limit you want to define

1:38:46

limit is you will have to define some limit right limit is 100 characters

1:38:52

again this is an example you can put whatever limit you want so first you'll have to create uh

1:38:57

you'll have to count uh maybe word count or the characters 100 characters will be two less maybe 100 words

1:39:04

this is good enough so everyone you can calculate the number of words words word count

1:39:10

how can you calculate the number of words so you can split the response

1:39:18

based on space right by default it is it splits based on the space operator then after split everyone

1:39:24

it gives you a list of words right remember that i think we have used that in the past also that split

1:39:31

function splits the string into a into list of words and then you can calculate the length

1:39:37

of this list this will give you the length of words correct number of words this will give you number

1:39:44

of words and we can simply say that if number of words if number of words if word count is greater than

1:39:51

hundred then we can simply do errors dot append response too long and in the bracket also you can add

1:39:59

more than 100 words correct everyone right folks clear

1:40:13

and uh we can return we can do this else else everyone what we can do is

1:40:23

is a response is not string and here we can return so you'll have to length of error

1:40:42

so here you are checking whether string or not fine then you are checking response should not be too

1:40:48

empty you are just appending that into the errors here also you are appending that into the errors so guys error

1:40:53

only be there can i say that if length of errors is equal to equal to zero then it is

1:41:02

then there will be no error or we can say that now finally what you should return if length of errors

1:41:11

is equal to equal to zero what does that mean everyone no error right correct neither this

1:41:17

executed nor this executed correct so you will return what you will return what you will return

1:41:23

response valid true and errors errors will be anyways empty else everyone you will

1:41:32

return false and errors or simply if you want to avoid all this hard work you can simply return

1:41:41

errors length of errors equals to equals to zero it will directly return a bullion and errors

1:41:48

how many if you're clear have a look at it simple python

1:41:53

code everyone nothing related to AI clear let me just walk you through once again

1:42:02

what we have done so we are creating an empty list of errors so guys if if the response is not string

1:42:09

then there is no point of checking further thing that's why we are returning from here only that

1:42:14

is a response valid false response is not valid and error may we are only returning one error response

1:42:20

is not string if response is string if this if condition is not executing you will come to

1:42:26

this if condition then you will check is response empty if yes then you will add in the errors then you will

1:42:32

calculate the number of words if word count is also greater than hundred you will also append that in the errors

1:42:37

now these are the two two things that you have checked then if there are no errors the length of errors will be zero

1:42:43

so you will return that true or false and the errors that you have created in the that you have added in the

1:42:50

everyone clear okay then everyone you can call these things with multiple

1:42:56

what do you say test cases right so you can have first of all you can create a chain or simply

1:43:05

you can do chain chain we have already created i guess

1:43:14

chain we have already created this is the chain and then everyone we can create a test case uh test case

1:43:20

equal to we can use the same thing topic is what do you say langchain expression language in

1:43:33

langchain and analogy domain what is the exact word which from here it is coming analogy domain

1:43:50

analogy domain is let's say software engineering software engineering okay this is one

1:44:01

test case everyone clear generally everyone you test across uh you give multiple test cases okay so for

1:44:10

now let's say you have just one test case you can instead of this also everyone you can create a list of

1:44:14

of test cases so this is the first test case similarly you can define another test case right

1:44:20

you can give another test case and so on and then you can iterate over these test cases

1:44:25

and check how many times your code is working fine how many times your code is not working fine

1:44:28

clear for now we are just testing across one test case we are testing for one test case

1:44:35

folks clear okay then everyone we will simply execute the code

1:44:43

response is equal to chain dot invoke chain dot invoke chain dot invoke me we will pass the test case

1:45:00

test case we will pass the test case and then everyone we will validate the response okay first print the response

1:45:09

then validated the response so let's say first we will get is valid

1:45:20

is valid is valid comma errors is equal to is response valid pass the response here correct ever

1:45:33

pass the response here and then everyone you will print this

1:45:39

particular thing if is valid is equal to true then simply you can print response

1:45:47

valid response else we will print errors we will print errors we are getting folks clear we will print let's say

1:46:09

invalid response okay okay so let's try to print this everyone

1:46:19

let's try to execute this code everyone clear with the execution so guys this is how we write the

1:46:23

test cases okay so as a developer it's very important to test your application okay so this

1:46:29

is the part of testing that we do as a developer for every application okay so python 3 validate chain

1:46:37

point so hopefully it should work fine yeah so i think it is running the code is running

1:46:44

let's see the output yeah now if you see everyone first of all we are getting the response yes we are getting the

1:46:51

response yes we are getting the response and then everyone it is a valid response okay it is a valid

1:47:00

response now what actually we can do is we can we can we can make this

1:47:07

a response too long if it is less than 10 characters right then if length of

1:47:37

if you see response too long this is error that we are getting are you guys getting

1:47:41

this point so guys this is what we do for monitoring and observability of our application that

1:47:48

how many times our application is working how many times it is not working as expected is everyone

1:47:53

here folks clear or not

1:48:07

okay perfect so that's it everyone this is main thing that we wanted to discuss

1:48:13

now let me write one just one definition of uh

1:48:19

okay guys one more thing so this is a basic observability system for response absolutely

1:48:27

group group that's correct and now everyone why we are doing this validation i think soarya asked

1:48:31

this question in the chat also that we are clearly giving all these instructions to the model right

1:48:39

explain concept clearly there should be three bullet points each bullet point should be short

1:48:44

it should not be very long do not add an introduction etc we can also put a limit here right

1:48:49

we can also put a limit here right but everyone the hard truth is lLM may not follow

1:48:57

lLM over the period of time everyone lLMs are becoming very smart they are they follow every instruction

1:49:02

but once in hundred times they may not follow the exact instructions every time correct everyone

1:49:13

so don't blindly follow lm every time it's very important to monitor to monitor

1:49:19

that's why it becomes very important to monitor the output monitor and test

1:49:32

the output generated by LLM constantly is that point clear to all of you?

1:49:49

okay so uh i have one more example even that is 100% same as the as the previous one

1:50:03

okay it is exactly similar so that example is mainly for the explanation of string output parser

1:50:09

that we have already understood so i will just write the definition of string output parser and and we are

1:50:13

done this was the agenda for the class okay so let me go to the notes

1:50:19

and i will show you that example as it is that is the same example for explaining the

1:50:25

string output parser is my ipid screen visible yeah so next topic is the topic was string output parser

1:50:41

but we have already learned output parser as a as a tool while writing the code but this is separate topic all

1:50:49

so we have not learned this as a separate topic okay so string output parser so guys

1:50:54

when we call the LLM through LLM or generally through any framework or in fact via API also

1:51:00

we don't get the output as a plain string correct so when we call LLM we do not get the output as a plain string correct so

1:51:19

we don't get the output as plain string.

1:51:33

Okay.

1:51:38

LM generally returns.

1:51:43

Is it possible to add loop to correct response and fix it possible to add loop to correct response and fix it possible to,

1:51:49

to regenerate the response absolutely yes it is possible in fact we will see that in the upcoming

1:51:53

classes okay cycles and loops okay generally uh that we do via human in the loop also that we are

1:52:00

executing is executing at this point of time we got the human feedback then we go back again and then

1:52:05

again we start from the a certain point again we iterate the process again we take the human feedback

1:52:10

if human feedback is not as expected again we go back again we process again we take the human feedback and

1:52:18

then if human feedback is let's say approved then we go ahead okay obviously everyone we

1:52:23

will have to put a limit on this execution we cannot do that infinitely otherwise our systems can

1:52:29

crash right Guru Pris obviously we can do that but it should be some limit on that there

1:52:34

should be some limit on that okay we will do that in the upcoming classes clear yeah so when we call

1:52:42

LLM we don't get the output as plain string as plain string as plain string LM often returns

1:52:48

or LM generally returns returns returns the response as complex objects as complex objects which

1:53:12

contains multiple parameters.

1:53:30

Multiple parameters.

1:53:32

So there are libraries like string output parser.

1:53:40

libraries like string output parser is a you can say that it is one of the simplest

1:53:46

output parser that extracts what it does it extracts the text it extracts the text it extracts the text

1:54:10

from the response object response object

1:54:17

response object and returns it as as a plain python string

1:54:35

everyone clear so if there are objects like a i message some streamed message etc there are

1:54:42

different type of objects depending on what l lm we are calling uh what model we are calling what

1:54:48

you can say that what framework we are using we are using lang chain lang graph etc

1:54:52

different models different frameworks may have different type of return type different response object return

1:54:58

type okay but there are always parsers like string output parser which can give you the data in the string

1:55:04

format okay and i think the usage of this we have already seen in the in the

1:55:16

in the code okay i think the exact same code i have written again in the notes as well okay no need

1:55:22

to copy paste that as well everyone clear till this point of time so this is what we wanted to discuss for today's class

1:55:34

So it is the most common and the simplest parser use in Langchain.

1:55:40

There are other parsers also.

1:55:43

It is the simplest.

1:56:04

okay so that's it for today's class everyone so uh i think uh we don't have

1:56:18

quiz for today's class and let me just check once everyone uh somewhere do we have the quiz for today's class

1:56:19

let me just check once everyone uh somewhere do we have the quiz for today's class

1:56:34

I think I missed it even. We missed it. We missed it. No worries. We will have the quiz in the next class. Okay.

1:56:51

Also everyone, uh, I have a question. Are we going to see the other frameworks as well like Google ADK, uh, Langraph, etc? Not all of them, but some of them, yes.

1:57:01

Okay? Some of them yes. Uh, sure, let me check.

1:57:04

check the exact curriculum, then I will let you know. I don't remember exactly, but I'll check.

1:57:12

Okay. So what we have covered from today's class, everyone, is this was the agenda for the class.

1:57:17

Let me just share my screen. Yeah. So as you can see, see on your screen, everyone, this was the agenda for

1:57:24

today's class, right? So did we create, uh, construct an isolated Python environment with Langchain,

1:57:30

Olam integration? Isolated Python, a Python environment means, can you can someone tell me?

1:57:34

what do we mean by isolated python environment virtual environment? Have we already

1:57:40

created virtual environment in last multiple classes? Have we already seen that? Create a virtual

1:57:45

environment? I have already added that in the notes in today's class as well. In case you want to

1:57:49

refer it, we have covered that. Apply secure project layout environment variable. Yes, secure project

1:57:54

layout everyone that never ever share your API key, secret key, if any sensitive information in the code.

1:58:01

Because when you commit the code, those sensitive information,

1:58:04

also gets committed on the code, along with the code, and anyone can access that on GitHub.

1:58:11

That's why we have already seen in the path that generally API key, etc., we added in the environment

1:58:16

variable. Okay? Absolutely. That we have already seen in multiple classes. Demonstrate correct model

1:58:25

binding using all chat Olama with credentials and endpoints. Yes, we have done that. Compose and execute

1:58:31

a langchain expression language pipeline, compiled, uh, combined.

1:58:34

defining template prompts chat model deterministic string output parsing all done and validate

1:58:41

validation also done okay validate the first chain uh behaves consistently across different input

1:58:47

parameters using defined success criteria so if these were the agenda for today's class and we

1:58:53

have successfully completed all of them everyone clear okay the support told me

1:58:59

a application security related content is added to the module end uh yes

1:59:04

I think that is there.

1:59:05

For example, guard rail, right, privacy policies, those are there.

1:59:09

I remember that.

1:59:10

In the next model, those are going to be there.

1:59:13

Yes.

1:59:15

So folks, everyone clear with all the points for today's class?

1:59:22

Pidentic you can use if you want to define the structure, if you want to validate the structure,

1:59:28

right, that whether this attribute is there or not, this object is correct or not, this data type is there or not.

1:59:33

for those kind of things, you can use pidentic.

1:59:37

Okay?

1:59:37

If you're constructing some object and you want that object to follow particular way or a particular

1:59:43

structure, then you can use pidentic.

1:59:46

Okay?

1:59:48

I don't think that how will you construct a response pidentic object?

1:59:51

Because response ideally should be a string.

1:59:54

And pidentic we use for objects.

1:59:57

Okay?

2:0:00

Yes.

2:0:00

So now everyone, I hope all of you

2:0:03

enjoyed the class. Now, I'm launching the feedback poll.

2:0:06

Please take the feedback pool and feel free to drop off.

2:0:09

Now, I think everyone, all of you might be, should be aware of that, that now the class timings have been changed to 8 to 10 p.m.

2:0:17

Are you guys aware of that?

2:0:19

Instead of 8 to 1030, now it is 8 to 10.

2:0:22

Yes?

2:0:24

Yeah, so we will be wrapping up the class by 10 p.m. I think some of the people, some people raise the concern that, okay, class is going a bit longer.

2:0:31

That's why we have.

2:0:33

we might increase the number of classes a bit.

2:0:35

I'm not sure about it.

2:0:36

But the class duration is now 8 to 10, 2 hours of class, not 2 and a half hour.

2:0:41

Okay?

2:0:42

I think that is good also.

2:0:43

Content we will try to cover in the same time.

2:0:45

Okay?

2:0:47

For example, today we will have, we had a complete 2 hours of content, not more, not less.

2:0:55

Folks, please take the feedback poll.

2:0:58

55% people have taken.

2:0:59

Please take the feedback pool.

2:1:01

Then we can end the class.

2:1:02

Today you have.

2:1:03

like half an hour more, maybe you can revise the content in that much of time.

2:1:08

Okay, utilize this time.

2:1:09

Generally, we used to end the class by 10, 20, 10, 10, 30.

2:1:12

So you have now 30, 40 minutes.

2:1:15

Okay?

2:1:15

Right to revise.

2:1:16

Thank you, everyone.

2:1:17

Thank you, so he'll.

2:1:33

Yes, I will see you in the next slide.

2:1:44

Feel free to drop off.

2:1:45

Thank you.

2:2:03

Thank you.

2:2:33

Thank you.