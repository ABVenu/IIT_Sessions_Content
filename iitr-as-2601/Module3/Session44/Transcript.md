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

10:24

Thank you

10:54

Thank you

10:56

Thank you

10:58

Thank you

11:00

Thank you

11:02

Thank you

11:04

Thank you

11:06

Thank you

11:08

Thank you

11:10

Thank you.

11:40

Hi, Arshtha, we'll wait for other two minutes before we start.

11:59

Sure, sir.

12:01

Thank you.

12:10

Thank you.

12:40

Thank you.

13:10

Thank you.

13:40

Thank you.

14:10

I hope my screen is visible.

14:17

Yep.

14:20

So can anyone put me on the message box in that my screen is visible?

14:27

Yes, it is visible.

14:29

Okay, thank you.

14:32

So today is a session for LLM internals for designers, right?

14:37

So very interesting stuff.

14:39

It's very interesting.

14:42

So before we go further, before we see the agenda, right, let us try to understand how this

14:51

this topic today session, which is the overall curriculum.

14:56

For example, right, today we are talking about the RLM Interim for Designs.

15:00

So today we will talk about the intuition behind and the actual stuff happens between the context, the context

15:09

limits, what do you mean by tokens, and how the context limit affect us when we are using

15:14

our elements for our daily work, right? And then we will introduce the concepts called temperature,

15:23

feed, and the truncation that happens because of the context limit.

15:29

So these are the today's topics that we are going to cover and this will improve, this will

15:36

connect it to your overall agentic systems.

15:38

agentic systems.

15:39

In the sense that when you build an application, you're using Langraph and then use guard

15:45

rights, right?

15:46

You will get to know, like this will help you to understand the basic limitations of the context

15:52

windows and then design according to the limitation of the context windows.

15:58

So the context window, we will see that it is a limitation of LLN system.

16:02

So if you know the limitation of something, then you know how to use it or make you level

16:08

it, right? So this is what we, that's why these study limitations phenomena, right?

16:14

So that's where the chapter, today's topic will fit in.

16:20

And then the most important stuff with this fourth path is that once you know what the limitation is,

16:26

see, everything is a budget, right?

16:28

So everyone else has a lot of dreams with any budget and all those things.

16:34

But we tend to go back, take a step back back.

16:38

step back and then we work on our dreams and all those things based on the budget, right?

16:44

So the budget is not a restriction impact, but this is a guiding principle which will use it

16:51

so that we can build our LLM based applications.

16:56

Okay?

16:57

In a way where we do reach the user with the goal.

17:05

At the meantime, we will work with the system.

17:07

will work with the system and then tune it according to its limitations, right?

17:12

And then most importantly, in the real life, right?

17:16

This shows that, see, as you know, right, today,

17:20

one of the major bills that the companies that are adopting AI

17:26

is with the usage with respect to the elements.

17:30

So you could see a lot of things that are happening

17:33

and you see some reports talking about the how the

17:37

licensing is tied with context window.

17:40

So that's a reason this session, this topic becomes extremely valuable in your journey towards

17:48

So this is not only affect the system, it will affect your financial bills as well.

17:55

So this is where we are going with us to the topic.

17:59

And as you told, right?

18:02

So here today, our goal is to learn about the internals from the internet from the

18:07

design perspective.

18:08

In the sense that if you can see the context window, it's nothing but a kind of a tiffin box,

18:15

right?

18:16

You have different compartments and then each compartment you hold some amount of volume.

18:22

And you cannot, unfortunately, you cannot carry anything beyond that tipon box capacity,

18:28

right?

18:29

So the whole idea is even this restriction, how can I write my query

18:37

and all those things, right?

18:38

So before even writing similar queries, we first understand what does this limitation mean,

18:45

not only from the theoretical perspective, but from the system perspective, which is very much important,

18:51

right?

18:52

So basically, as we know, right, an application talks about a rack chance, where we use it for

19:00

ground day, and then generally we have the chart tree, right, if you go and open up charge

19:06

or germinate by and it has a historical conversation between us and that machine, right?

19:13

And then we have a lot based on the tools that we use.

19:18

And then this, all those collectively, uh, boils down to the context window,

19:23

which is nothing but fixed at storage, like our different box.

19:26

Right.

19:27

So today, for algorithm is very clear.

19:31

So we want to know, understand the tokens with respect to the building.

19:35

with respect to the building, latency, and the prompt length.

19:39

So it's all connected to the context change, right?

19:42

So the next question would be like, we want to understand how the context limits shape the

19:49

RAD, memory and Asian design choices.

19:53

And then we'll see how, like, what will be the effect with different values of temperature

20:00

and seed, if seed is available, where we can trade off.

20:04

trade off. This is like I understand the design, you know, right?

20:08

And you, like, once if I go, it's similar to the design here that what we have, right?

20:13

If I take a two wheeler, right?

20:15

So if I want to reach my destination quickly, then probably I would go with the highest speed.

20:26

If I want to have the better mileage, I would go at around 40 kilometers per hour speed, which is 40 to 45 is the

20:33

45 is the sweet spot, right?

20:35

Where I could have my maximum fuel, efficient fuel burning and I will get a better mileage.

20:43

But not every time we tend to go with the ideal 45, right?

20:48

So sometimes what I mean is that we are getting hurry and we try to go fast beyond that.

20:54

Once we go that, yeah, we might reach earlier, but does not imply that we are efficient with us with the fuel message, right?

21:02

the same time, right? You go slower, slower before even 30, if you try to go saying that

21:09

a slow, lower speed, does not guarantee you feel better feel consumption, right?

21:16

So the thing is, that is my choice. And that choice exactly happens with respect to the consistency and creativity.

21:24

And we see this temperature and sees as a kind of knox for that.

21:29

And then next thing is we want to see.

21:31

want to see, what to predict, when the context is truncated or overloaded in mighty certain agendas, we'll look into it.

21:39

Okay. So these are the four agenda for today. So any questions?

22:01

Yes, do you have any questions on this agenda?

22:08

Okay. If not, let us go. Yeah, thank you. So, see, my goal is to know, and see,

22:20

see, the, see, understanding the big picture or waiting to know what we are going to learn.

22:26

That is the biggest motivation that will help us to follow the path.

22:30

And I hope you guys have Google collab installed and can access. Yes or no?

22:41

Here. Yes, right? So we are going to do some small exercises as we go further. As we some couple of activities.

22:54

So just get your Google ready.

22:59

ready and then what you can do is that you can, in the meantime, right, I will, I want you guys to, oh sorry, I.

23:11

So I want you, you guys to get the GROC.

23:17

Okay. I hope you guys have the GROC API key set. Okay.

23:29

send them a post a link on the chat box about how to set the GROC link, GROC API key, so that when we start doing activities, they can just easily, if people who have not already configured, right, can use them. Okay.

23:47

Sure, sir, I'll do that.

23:49

Yes, thank you. So let's come back. If you are set, it is fine, good.

23:59

So the question is, the biggest question is, why designers need LLN terms?

24:06

Right?

24:07

See, LLMs, say, already LLMs looks very, very technical from the common, from the point of your ingenious itself.

24:18

So from a designer perspective who don't have the technical background,

24:23

it looks like why I need to bother to learn these stuff, right?

24:27

So the whole idea is very simple, right?

24:30

We are not talking about you, about how to, how the, trying the model, LLM models and all those things.

24:39

We are talking about how you can use this, right?

24:44

Even when you are going to use the LLM, right, it is better to know, understand how it was.

24:49

So basically, when we talk about the internets, right?

24:54

So we are talking about the measurements, right?

24:56

So we are talking about the measure.

24:57

behavioral behaviors of the language model.

24:59

So just understand those.

25:02

Let's try to go a little deeper here.

25:05

So measurable behaviors of language models.

25:08

Because all, you see, now everyone is writing or implementing the language-based applications, right?

25:17

It makes our life super-incerect.

25:20

Most of the time it goes at such a system by itself.

25:24

So it is making our life.

25:26

It is making our life much easier.

25:28

So the thing is that when, but it comes with a cost.

25:31

To understand its cost, we know to know how it works from the 10,000 feet.

25:36

That's more than else, right?

25:37

I'm not asking you guys to understand, okay, how the tokens will be built and all those things.

25:42

But as I like to understand what do we mean by these basic ideas, like tokens, context window size,

25:50

randomness and latency with respect to the LLBs.

25:54

Okay?

25:55

So that, when.

25:56

we develop applications if we could build the so that that affects the cost

26:03

evident user experience okay so for that reason it is important to understand those

26:09

terms and the technical jargon without oversimplifying it and also at the same time

26:17

without going to be technical approach okay so this is the whole goal of this

26:22

session okay so it is similar to right

26:26

So when I tell LLM model, it's like a different box, as I told you earlier, right?

26:30

So you can see, right, it has a, when I write the prompts, right, it consists of the chat.

26:36

They basically have with my LLM, it consists of instructions, PDF churns, it has a chat history and everything.

26:44

So it's all neatly, like neatly put it in a box, right, as a different compartments, right?

26:52

So what happens is that the question would be like,

26:56

All the things happen with that opens, right?

27:00

The next question is that whenever, let us take a simple example.

27:04

So, you see, if I take the different box example, right, I cannot put more than its capacity, right?

27:14

So it is either it will spillover or I will not put it, I am not able to put it inside the open box.

27:21

Similarly, right, let us take a simple example. We are all having a, I have a, I will be able to put it, I'm not able to put it inside the open box.

27:25

I have traveled on the metro trains, right?

27:28

So whenever there is an maximum capacity, right?

27:30

So what happens is that we generally don't enter when it's at the full capacity, right?

27:37

So what happens is that we just stop?

27:39

So this we call it and trancheation.

27:41

Like, for example, when the model, the token, the model capacity with respect to the token context

27:47

limit is being reached, right?

27:50

It cannot take more tokens and at the same time it becomes like,

27:55

unresponsive and all those things happens.

27:59

And that state, where it cannot take a more token, right, is we call them truncation.

28:05

So generally, what happens is that for that reason, what we do is, we take only, in the rag, right,

28:14

we take only top three choices, will not take top 10 choices.

28:18

Because the more choices that you put, right, what happens is that, it will unnecessarily add too much noise

28:24

it to the model, but instantly if I add only under, if I have only three chance,

28:29

what happens is that the models become less and it can fit within the context window.

28:36

Otherwise, what happens is that the more, see, generally what we think, right,

28:39

intuitively, having more information is better, but from the system perspective, it is not

28:46

the case. So having a lot of information will not only add the noise to the LMS, but it also

28:53

quickly ease up my context window size, okay?

28:58

So generally what happens is that what we, so the reason, what we do, we actually, we go

29:03

and persist the chat history file so that we will store the whole history

29:08

separately as a persistent, and the persistence is nothing but storing on the disk.

29:13

The space is, we call it as persistent, right?

29:17

So, and then generally we will have the agent trace,

29:23

a verbose mode so that the thoughts are sent back into the loop and finally we will keep the

29:30

temperature as zero this implies that we want to have very less randomness okay so generally what

29:38

happens is that people think that okay LLM is like a Google drive and then whatever the chat in the

29:43

chat box I will keep on adding the PDF and I will add text files and all those things

29:49

let it analyze and come back so that you want to work so LLM is

29:53

not like Google Drive or any cloud storage. LLM is a model. You give the data,

30:01

instruction, it can be either instruction, either it can be image and videos, right? You give it,

30:08

it will understand and it will get back to you rather than storing. So don't try to save the,

30:14

you use LLMs as the storage space. So the question would be, right, if I, so looking at this

30:22

limitations right then actually the question comes to us is that how much I need to pack in

30:26

the request right so that's an important thing right so how much I need to pack and at the same

30:35

time generally what happens is that you might have seen you keep on uh typing and suddenly

30:44

the LLM coming up with different answers which is not related to what you have been chatting

30:49

over a while right so these are

30:52

things happen and the question is that how we can handle it and just where we go deeper here.

30:58

Okay, so clear about the motivation for the uh for knowing the LLM internals?

31:08

Yes or no?

31:14

So in simple work today we will learn how we can reduce the cost when using LLM's yes and for that

31:19

we need to understand what how the cost will do.

31:22

like as well, right? So then only you will know how to reduce it. So the question would be,

31:29

what do you invite tokens as well as once, right? We all converse in English. So my point is

31:38

like answer, can you explain the second point again? The second point is very simple. In order to reduce

31:43

the cost, right, you should know where the cost is inter, right? Where are the avenues, where I'm

31:52

I'm introducing the cost. Then only I can think of reducing this. So in the previous slide,

31:59

right? So which one? Sir, can you extend second point again? Which one if you can, is the second

32:06

point again? Which one if you can, like, is it like the core design question or?

32:14

Ah, persistent chart history file. So what is my persistent chart history file is nothing but

32:21

persistence is nothing but storing something on the disk. Your USB or your already

32:27

is right, that's a persistent storage. So I store the chats on the my disk. See, let us take a simple

32:34

example of your WhatsApp backup, right? Where does this WhatsApp backup goes? It goes to your Google

32:40

Drive. So whatever the chart that you had with your friend, right, that will be saved and uploaded to the

32:45

Google Drive, which acts as a persistence. So this is what we are talking about. You store

32:50

somewhere there rather than the LNA. That's what we mean to say persisted chat. Okay.

32:58

So now let us say to understand what do you mean by token and words. See when we speak, it is worse.

33:04

We will not tell that it's tokens, right? So whatever we speak, communicate with others is nothing but

33:11

words, right? It's not tokens. Okay. So what is a token? We have a token. We have from

33:20

the perspective of LLM, a token is the smallest unit and LLM briefs and generates.

33:28

So it's the smallest unit. Which is the smallest unit in our language? Can you don't tell

33:36

me? I need answer. So here I got another question. If we mention a persistent file that

33:45

will increase token forms, no. The persistent file, I will start.

33:50

store somewhere outside my LLN. So it won't be increasing the LLN because I'm not storing

33:57

inside LNN. Okay. So what is the smallest unit with respect to? What is the smallest unit that

34:13

we have in our language? Can you even tell me?

34:20

Not one.

34:35

Later are alphabets. Alphabets, right? If I take English, it is like A, B, T, is my smallest unit.

34:50

Those are my smallest unit, right? So similarly, when we talk about LLM, tokens are these small

35:03

elements. Okay, it is similar to the letters in our vocabulary. Letters are alphableness. Okay? So

35:12

whenever we talk about the tokens, right? So it is like it can be a whole word. It can become a part of word.

35:20

It can actually be punctuation or it can be space.

35:23

And if there is no, see, one thing is very clear.

35:27

It is, there is no general rule that the token should be only alchabets.

35:32

It can consist of punctuations and all this stuff.

35:35

It depends on the encoding scheme that is you have used.

35:38

The model is used.

35:40

Okay.

35:42

So a simple way, this is right?

35:49

So the token.

35:50

is a smallest unit, right?

35:53

In the, like, see, when we go to any shop, right, we see, rice or beef, we just not go and just pull a handpull and tell that, okay, I need only a handful, right?

36:07

So this is not the way it has, it will be sold, right?

36:15

It will have the package, packaged into 50 grams, 100 grams.

36:20

200 or something like that, you have the smallest package and you take it, right?

36:24

So this is what the token is.

36:26

So don't confuse token with the words that we speak in English.

36:31

Don't confuse yourself with the tokens with words.

36:35

It is similar to the words in the sense that it can be a single alphabet or a group of alphabets.

36:43

Okay.

36:44

Apart from that, there is no similarity between token and words.

36:47

And in our case, general the words, the word,

36:50

have meaning. In the tokens, it does not have any meaning. Okay.

36:56

So let us take very simple, right? So when you tell, namaste, how are you, right? For us,

37:02

it is four words. For, but for the API, it is not forward. Okay. So you think that when

37:10

you're sending a prompt, right? Namaste, how are you to the, to the, to the, to the, to the LLM. But it would

37:19

it will not count it as a four, it would count it as a six to eight basically, right?

37:24

We'll see, the thing is that APA billing happens with the number of the tokens rather than the

37:30

words. So be clear about that. Right. So whenever there is the English word, right? Short English word

37:36

will generally will have a mapping of one to one, right, in the sense that hollow will be mapped to hello.

37:42

But there are some words where you have a prefix and suffix. In that case, the tokenizer might

37:47

might remove the prefix or suffix. We'll see that. We'll see that simple example in other

37:54

few minutes. And when I have an India and English mix as well, right? So generally it will have the

38:01

lot number of tokens rather than the words. See, if you see here, right, we have call meeting

38:07

has time pa anna please. Danyahu. But it is only three plus three, it's seven, eight, right?

38:15

If I take a punctuation test, 10 words. But as a token, it is not 10. It will be more than that. Okay? So be careful. The tokens are not your words. And generally, what happens is that? When you talk about even in English, right? Approximately four characters is one token in English.

38:41

Okay. So that's not a...

38:45

For example, right, cat is one token and AM is also one token.

38:51

Sir, token includes special characters too, not necessarily depends. So it all depends on the encoding.

38:59

So what happens is that many types. You see, whenever there is a long URL or something, it will be tokenized. In the sense, it is straight.

39:09

So generally what happens is that, sir, do we count?

39:15

new lines of sources in tokens. See, it is not, you cannot go and count the tokens just like that. So you have an encoding scheme, right? Every, every model has the encoding scheme. And based on that encoding scheme, the text is converted to the tokens. Okay. And based on those tokens, you are built. And if the encoding does not create a new line,

39:45

or spaces, it won't be considered. It is highly dependent on the encoding scheme, right?

39:52

For example, right, how do you write Hindi in English? Either you use, there are a lot of translations, right?

40:02

I trams and all those things, like kakha, right? We add X extra, right? So it all depends on that. It all depends on the encoding scheme, right?

40:15

So generally what happens is that, say, the billing happens, as I told you, with the token, the input token and output token.

40:25

And what happens, higher the token, higher the latency.

40:29

Latency in the sense that it takes down more time to generate, right?

40:33

So generally what happens is that prompt lengths, whenever the prompt length is higher, you have to trim the instructions.

40:43

And you have to cap the change size.

40:45

What happens is that, generally people think that, okay, shalla, my own 40 page PDF, and then let the groc, germinate, summarize it.

40:57

So when you just upload one PDF, right, so internally what happens is that, if you count the number of tokens with respect to that PDF, okay?

41:07

So it divides that into chance, basically change and tokens, basically divides into tokens, basically divides into tokens.

41:15

and then it will use. So you will be built based on tokens, how your PDF file is

41:20

divided as a tokens rather than the 40 pages, okay? Be clear about that. And the problem with that is

41:27

once you have 40 pages or 100 pages, you are filling the context window as well. So not only it is

41:34

affecting billing, it is also affecting the context window. So in a simple sense, right? How much I can see

41:43

through my eyes depends on the distance of the distance of my eye power, right?

41:51

So that limitation is always there. Even though I can see all the things with my eyes, I cannot go and

41:57

see what is there clearly after certain possible distance, right? So this is how it is. So you go and

42:06

add your, if you go back to the example of Tiffenbox, right? If you add a lot of stuff, then you get

42:12

very less room for other stuff. So you should not go and upload PDF pages and all those

42:20

things. Okay. So generally people might say, okay, these like generally models are running on

42:30

the GPU side. Why should I think the slowness? The slowness happens because you have given

42:38

a lot of tokens. So what happens is that the model.

42:42

has to understand your tokens and it has to generate the token sequential. So that's a reason you feel that it is taking a lot of time. So at the end of the day, it is like, if I take, if you tell you in a very simple sentence, right, if we go for a trekking or something or if you want to travel, right, will you put a lot of baggie, a lot of items in your backpack or you keep only the required one and then go ahead with your travel plan? If you go with the

43:12

for the later, right, you will have a pleasant journey. Otherwise, you end up spending a lot of time on the former case, right? So managing those things. So that's the idea. Okay. So let us look into how the tokens are generated. Let me share this video. So I hope you guys can see this. So in the meantime, let me copy.

43:42

page this step for you guys so that you can also run on your on your

44:12

What we are doing here, very simple.

44:19

Let me copy it and then.

44:24

Okay.

44:27

I hope you guys are the, I have opened the Google collab, right?

44:34

So please do run with me, execute the,

44:38

can you send the whole file?

44:41

I think it has a whole file.

44:42

other stuff as well. At the end of the session, I can send it. But nonetheless, you can just copy paste like this in your Google Cloud. It should work properly. Okay. So what I'm doing is, what I'm doing is I'm just importing a Tick token library, which will help me to understand the token usage, okay? Not token usage. How the tokenization works. So basically what we are doing is that we are doing is that we have

45:12

we are using an encoding scheme like called cl 100k underscore base this is one of the charge gpt encoding. So you can have different encoding as well. So we ask what we are doing is we are specifying the encoding here. And then once that is done, we are just giving this sample from. The sample company is very simple. You are an annual report assistant for Acme Corp. Answer only from the context below, right? They even give over. So this is my sample prompt. You can write anything.

45:42

And the question is that next we have to understand what is my token count, right?

45:47

So how many tokens it has, right? I just what I do is I take this sample prompt and I do the encoding.

45:54

And once I do the encoding, the encoding function will return me the set of token IDs.

46:00

Right. So, and then I will just bring how many tokens it has.

46:04

See?

46:07

Right? It computed. So it seems that it has 54 encoding.

46:11

64 tokens and I just took that county here, right? And then what I do is what are the

46:19

token and then see if I if I use it 40, right? If I take how many words are there, let's take a simple

46:27

example of Google Doc. On me.

46:41

So here I just do that. And then if I choose, select it and I'll just word count, right? So this is showing me 36. This is showing me 36 word count. Okay? But my tokens is shown as 64. Right? Now you understand why it is like, it is, like,

47:10

You understand that token, we were, we are telling that a cool token is not equal to

47:16

win a words because of this reason. Okay. So these are the things would look like.

47:23

Any questions on this? I cannot copy page. Yeah. So it is not one-neous-to-one ratio. You are

47:31

correct. It can be more ever. It all depends on the encoding. That we wanted to let you know.

47:40

So can we quickly make an activity? So in the prompt, right, I have put it as a context on question, right? What was the revenue work in 2023? Can you add another one question and run?

48:10

See, how many of you could run the program? Just put SR no on your chat box.

48:25

You're able to run, right? So can you make some small change on the question and then try to see, run it? And did you find the one is to one as well?

48:40

See, I will share it after the class. Okay. So what I have done is I have...

49:10

So see here we are using the tictoker to get to know about the tokens, right?

49:19

How the token will work?

49:22

Yes or no?

49:27

What about the sentence?

49:30

for my... See, you can do it. See, here, what happens is that? With a sentence, see, I could understand that is your S-Burt model, right? So we are not talking about the expert model, right? So we are not talking about the expert model. We are talking about here with the LLNs. What we are doing?

50:00

here is we use TikTok token because we can get the same, the encoding that is supported by chat GPT.

50:07

Okay, so that's the reason we use TikTok.

50:10

You can get into the any encoding, but make sure that the encoding is compatible with the

50:16

the elements that you are going to use. Okay.

50:23

So I will upload, I will share it after some demo at the end.

50:30

because somehow there was some issue that I fixed it by hard coding my API key.

50:36

So I will remove it and then I will share it.

50:39

And the meantime, it should be easy for you guys.

50:44

So the next question is,

50:46

till now we were talking about context window, context limits, right?

50:49

Let us try to understand the real facts.

50:51

What do you mean by the context window?

50:53

So the context window is the maximum number of tokens and LLM can

51:00

process in one forward first, right?

51:04

It is similar to how much we can eat, right?

51:08

If I take it one piece, like at one point, right?

51:13

How many number of chunks of cake I can eat?

51:17

Right?

51:18

So that's my context window, right?

51:20

That's my limitation.

51:21

I cannot let us say that I cannot eat more than

51:24

three pieces of cake or I cannot eat more than four scoop of ice cream.

51:29

So something.

51:30

like that, right? So there is a limitation. So it is a limitation with respect to tokens,

51:35

how many maximum of tokens the LLM can process in one forward pass. That includes the system

51:44

text and the user messages, the prop that we give and the results that we get back from the LLM.

51:50

And then you ask to retrieve some documents, whatever things that it does, everything, right?

51:56

The whole thing includes, calls this a context window.

51:59

window. So if you can see, right, in the, it's a desk. That's it. So what is the desk space?

52:10

Right? How much things that you can keep it on your table, right?

52:14

Higher the, like, higher the size, higher the number of tokens, lesser the size, this is a number of tokens.

52:22

This is what it is, right? So this is the idea behind the context window.

52:28

What are the things that's the part of context window, the system instructions,

52:33

or systems or instructions that we give, right?

52:36

We tell, right?

52:37

You see the previously, right?

52:39

We wrote a sample prompt statement.

52:41

You are an annual report of the standard.

52:44

So we are telling explicitly what is your role.

52:47

And then we write some guard rights as well, right?

52:50

Those are part of the system or instructions.

52:54

Then your user messages. What is that?

52:57

What is that?

52:58

what was the revenue grown, right?

53:00

And then retrieved documents, context from PDF, web bar or database.

53:04

Here what we did?

53:05

Context start, context, saying that one has the source ID, something like that.

53:11

It includes those retrieved documents.

53:14

Here we have simulated it by manually giving some data in between context start and context stand,

53:21

and then what are the two results, right?

53:23

And then we get the replay, right?

53:26

So the whole those crystal.

53:27

Those stars will be constrained within the desk, right?

53:31

The single desk, that's my context window.

53:34

Right?

53:35

So this is the important stuff.

53:37

So generally what happens when you limit?

53:40

So truncation happens.

53:42

What is truncation? You just cut it.

53:45

Simple.

53:46

The old parts will go off.

53:49

Or it will not take your input.

53:52

There are the only two possibilities.

53:54

Either you throw off

53:56

you forget it or you stop responding it in the, from the model perspective.

54:02

What is forgetting?

54:03

The previous conversion, the model has with you, the stop or the model will not respond.

54:10

So this is what it is a truncation with rejection, right?

54:13

So generally, why this understanding context limit makes sense?

54:18

Because generally what happens is that when we have more tokens, we have to pay more,

54:25

more and the speed is less.

54:27

So once you lose the context, what happens is that?

54:31

It does not remember, right?

54:34

So as a result, you keep on, you will be back to square one

54:39

when you ask a lot of questions, right?

54:42

Because it could not, it cannot remember what it has to reply.

54:46

So it will give you the similar answer once again, right?

54:50

So that is extremely frustrating.

54:52

So it is, and as a result, you will be able to answer.

54:54

And as a result, your reliability drops and your user experience also drops.

55:00

So for that reason, you need to understand this context limit.

55:05

Okay?

55:06

So as a designer, what you can do?

55:08

You can trim, reduce the instruction, and then limit the street turns,

55:14

and then you have to control this.

55:15

That's one reason why I told you, right?

55:17

Don't upload bigger PAP files into the LLM.

55:21

It can read it, but the problem is it has, it will have,

55:23

it has, it will quickly work on the, quickly, it will reach the context window side.

55:29

So you can simply do a simple example, right?

55:32

You take a PDF and then give it to TikTok kind of library and you can,

55:36

you can see how many tokens it will be, right?

55:39

So generally what happens is that, you keep only what it matter,

55:44

similar to what we do decluttering, right?

55:46

So the more you put, it looks more messy, right?

55:50

You decilter it.

55:51

So that looks tidy.

55:52

So this is the...

55:53

designer things that you need to think about with respect to the context limits and context window.

55:59

Let us take a simple example here, right?

56:01

So let us take even more deeper visualization, which actually talks about, let us say that I have a

56:09

10,000, 8,000 context window. That implies that I am allowed to take, I can, at any point of time,

56:17

I can work with 8,000 tokens, sorry, 8,000 tokens, right?

56:23

So what happens is that? It's beautifully described as a user jar, right?

56:28

You put your user question and you put your instructions and whatever the room,

56:35

that the space that you get in the bottle after putting all this stuff, right?

56:39

This is exactly you have the space so that you will get the answer, right?

56:48

If the answer overclose it, then probably you can actually.

56:52

probably you cannot store it, right? So that's a reason. The only way to get a better answer for my question is to reduce the tool of chatistry, right? Changes and all those things.

57:05

See, user question and system, see, system rules, sometime I have to, I cannot do anything, right?

57:12

I want the prospective persona to be there, which is when LLM is behaving.

57:18

And then user question, I can repraise the

57:22

But the rat change, yes, retrieve only the chunk that is really required.

57:28

So what happens is that we think that, okay, having more information is better.

57:34

But unfortunately, it is not true.

57:38

You need to have the quality information in the sense that you give the agent what it is required, right?

57:47

The meaningful and good information, then the quality will be better.

57:51

Otherwise, you just give, instead of three chance, right, you can, it will also get into hallucination mode, right?

57:59

And then don't give the, all the, whatever that you are stored, just leave it to it saying that all nice day.

58:07

See, that looks cool, but unfortunately, that will add noise to the model, right?

58:13

And this is the one reason why it is very important to understand this context window.

58:20

So it is similar to the crime, right?

58:22

So if my compartment is full, nobody can enter and, and you have to wait till people, sufficient, but people get on from the compartment.

58:32

So this is the reason, right?

58:35

So it is like similar to, like, packing something in your backpack so that your travel becomes memorable, right?

58:43

The whole goal of you is to do a travel, right?

58:47

which is more memorable, but you should not end up only managing your backpack during your travel.

58:55

So that should be, you see, anyway, you have to manage it.

58:57

But the question is, you should not end up doing that as a main task instead of, instead of concentrating on your goal.

59:07

So I do have a question, I got question here.

59:10

Does GPTR plot try to limit their output tokens or they generate as far as input token?

59:17

See, does GPT or plot right to limit their output tokens are generated as well as the input token?

59:24

See, the way it is generates, right?

59:27

It all depends on the model it has been trained on, right?

59:31

So at the end of the day, it's a probabilistic machine, right?

59:35

It generates a token sequentially and cloud model and the GPD model both have been trained differently, right?

59:45

So cloud does awesome with us through the coding, but GPT response very good then you want to write something and then more comprehensive.

59:55

So it all depends on the model behavior and they don't have any care that any output should be this many tokens and are not.

1:0:04

It cannot be possible because it's a model that has learned it, right?

1:0:09

So even the creators don't have any kind of, the model creators don't have any kind of, the model creators don't have any kind of

1:0:15

role in it. The only one thing what you can do is that you can be explicitly

1:0:20

say that let me make sure that it is less than some 400 or 400 tokens or something like that.

1:0:28

You should write it as exclusively in the prompt. I hope I answered your question.

1:0:45

So what is the implications when we have the context of it?

1:0:51

So from the rag inflation, as I told you, right?

1:0:55

So the chunk size all compete, see, top k chunk size and metadata are all complete for the same window, right?

1:1:02

So let us say one thing, the year, what was it take away here?

1:1:08

So if I have a 8K total window, right, both input and output share the same box, right?

1:1:14

So if you have a prompt of 7,000 tokens, but you end up only getting, only remaining

1:1:21

1,000 tokens, even though think about it, 7,000 tokens will have at least 3,000, 4,000

1:1:28

tokens, a number of planes, but unfortunately, it won't happen, right?

1:1:33

So you will be cut up at 1,000 tokens.

1:1:37

And what happens with respect to the rag in education, they say, when you push a lot of information,

1:1:44

like instead of top KS 3, you put top 10, you think you are tempted to use that.

1:1:51

What happens is that?

1:1:52

The older data will be timely pushed up for making room into the new chart, okay?

1:1:59

So what happens is that another important issue happens to respect to the memory.

1:2:05

What happens?

1:2:06

So loading all, what it does, it will load everything and it makes.

1:2:14

the whole information will be pushed out right so what is for the agent the agent will take a lot of time to generate okay because at the each each model what happens is that it will think it will take it will think it will act and then it will observe right so when you push a lot of stuff your latest it becomes too heavy so what you have to do is generally right you take uh you apply filter

1:2:44

and take only the change that is required and then append it instead of appending everything, right?

1:2:50

So what you do is you start with small.

1:2:53

So basically we call it as a produce of disclosure pattern where you take with the start with the small and try to incremently increase the small and try to incrementally increase the small, if you are satisfied with the small, then stop there.

1:3:07

If not try to increase the complexity or add the information in a small.

1:3:14

quantity so that you will get the model will not get lost, right?

1:3:19

So this is the most important stuff with respect to the handling the context window limit, okay?

1:3:30

See, you can think about it in even more simpler way, saying that I have a shared cubicle, right?

1:3:38

I have shared cubicle with me and my friend, right?

1:3:43

So what happens?

1:3:44

me to think about it i am the input and your friend is and my friend is an output then both of us share the desk run if i keep on

1:3:56

that he gets the space to put his things right so things from that perspective it is nothing but your shared

1:4:03

workspace okay we can view like this the input and output as a shared workplace and then you have to put

1:4:10

what is the only which is required and get get the things out okay this is

1:4:14

I hope this is clear.

1:4:28

So why the, how this context limits the rag design?

1:4:35

See, let us take very simple example, right?

1:4:37

When we go to the prime, right, so see, if I go to the IRC, see, if I go to the prime station, what

1:4:44

So if I want to know about some specific trains, will I go and look into each train or I just

1:4:51

go to the search box and try to find only the required trains in my route?

1:4:58

Which one you will prefer?

1:4:59

Obviously the second one, right?

1:5:01

Why should I get into all the mess of getting into the thousands of train that is running in India for that day?

1:5:09

Instead what I will do is, I will go and check it out what are the...

1:5:13

whatever the train that is running between the my preferred route and I just look into it and make a decision.

1:5:21

That's exactly the context window does, right?

1:5:25

So it limits your view but it will not stop you from using it.

1:5:29

So that's the same thing, okay?

1:5:32

So generally what happens that we will think that we don't have a lot of space.

1:5:38

Then the thing is, what happens is that you have to that you have to have a lot of space.

1:5:42

you have to carefully look into those kind of stuff, right?

1:5:46

What we have discussed in previous.

1:5:48

So it is always a design choice, right?

1:5:50

So should I be relevant or should I be more coverage, right?

1:5:55

So what is that?

1:6:00

So let us say, if I take the top three result in Rang, that will be more relevant.

1:6:06

If I take top five, it will have more coverage, right?

1:6:11

But it comes with a couple.

1:6:12

cost. If I take top 10 also, it will have a lot of coverage. But it comes in the cost.

1:6:18

What is that? It will add noise and then it will quickly eat up my context window, right?

1:6:25

And then what happens is that more chance? What happens? It flows, right? Why? It takes

1:6:33

time because it has to process. It has to understand. It has to generate. But lesser number of checks, it happens faster.

1:6:41

faster, right? And then the cost as well, right? More tokens you get, you get a higher cost. But more is not better every time.

1:6:51

Okay. So these are the things generally you need to take care. And whenever you do it, right? So let us say, that simple example would be like, if I go with the intuition, say, we all know, right? We have the libraries in our institutes. We have libraries at home, generally.

1:7:11

What we do, every day, if we want to need something, right? For example, quickly I want to know about the design guidelines or something, right? I will not run through and get all the 10 books and then put it, right? I will not read the all that in books. What I will do, I will pick the one or two and I will look only to the two or three pages in that. I just look at the index and wherever the topic is there, I just quickly go and read it. I will not read the entire book.

1:7:41

That's exactly what we are talking about, right? So it looks like, okay, it is tempted to see that, okay, the book might cover each and every aspect. So, but we are tracing only the score and then incorporating there so that we will, our rag will not be constrained with the context limit. Okay? So this is the idea here we are talking about.

1:8:04

So basically, don't think that context limit is above and, uh,

1:8:11

how can I go with that? So you think that is a boundary, right? So that boundary helps you to understand the design choices and that will help you make your, tuning your applications better.

1:8:24

So what happens? These are the things, right? So generally, uh, the design choices would be like the keep when you, when you have this in the rag knob, right? Top K, what is it top content that you have to look into it. Don't go.

1:8:41

uh beyond five obviously uh because uh if if window is tight fine but uh if you if you think that okay still you have a space uh try to

1:8:53

incrementally do that otherwise uh don't do that and the chunks are right smaller chunks are there but but may if you go with the largest

1:9:06

what happens is that there will be more local context, but make sure that the chance are diverse.

1:9:12

Okay, diverse is nothing but more variety, right? So generally, right, de limiter will also have the

1:9:19

overheads. Like when I, when I write my rag, right, at the end of the data, the rag will also write

1:9:23

this context and this context is also counted as token because it is an LLM, right? LLM has to know that.

1:9:29

So that's exactly what we are going to here. So a context start and delimiter like space,

1:9:36

and your punctuation also considered tokens, right?

1:9:43

So everything, citation, everything, keep it short.

1:9:47

Okay?

1:9:48

So these are the things.

1:9:49

You should be very careful.

1:9:52

So don't be under impression that, okay,

1:9:55

charge you p.

1:9:57

No, it also pointed towards functions for your

1:10:03

tokens, okay?

1:10:05

Okay.

1:10:06

So there is a difference between grounding and stuffing. What is stuff? You put a lot of irrelevant stuff, that is a stopping. You put relevant stuff, sorry, relevant exchange, that is grounding, okay?

1:10:20

So I do got the question here. How does it handle when it is searching the web? See, it's the web and the search, the results will be presented to the model and the model and the model will parse and do the stuff.

1:10:36

Search is entirely different. See, if you are, if you are, let me tell you, what happens is that, if I take the Germany or charge, if it, when you use a web address, right, it will have a back, it will have a thread that will go and touch that.

1:10:52

And then it will, it will, it will, it will, it will implicitly use in your token generation.

1:11:00

So giving link will not affect your much. But the link,

1:11:06

what you are going to give us a web will be considered as a token and the content in that web, it will not be considered as a token, okay?

1:11:17

It might use, it might say the only one thing is that it might get some part, read it and all those things and get, get its token and all those things.

1:11:25

So that will be implicitly will be there, but it will not be exactly like that. Okay.

1:11:36

Let us try to understand some simple program here.

1:12:06

I hope you can see this now.

1:12:13

Okay.

1:12:15

So what we have done is we have written, we are simulating the chunks over here.

1:12:22

So here the retrieve tokens, what I have written is this right, okay?

1:12:28

So we just added the retrieve tokens, okay?

1:12:33

So let me paste this.

1:12:35

And then what we do is we wrote the token, how to come?

1:12:47

See, this is a maximum context tokens is right?

1:12:50

This is the budget that is.

1:12:52

See, we are stimulating it.

1:12:53

Okay.

1:12:54

Not exactly.

1:12:55

So what are the instructions?

1:12:56

What I am telling is answer only from my, from the context.

1:13:00

And if you missing say don't know, you don't know, right?

1:13:03

So this is my instructions.

1:13:04

my instructions. So if you remember, right, we were talking about the context

1:13:08

view of the instructions and what is the context tokens. So we are setting ourselves

1:13:13

as a six hundred. Okay. And this is a formatting the chain. So and then we are building

1:13:21

the context block. So if you see this context block, right, it's very interesting. So

1:13:27

here what we are doing is we are taking each chat. Okay. And we are measure

1:13:34

how many tokens are there in this chunk? Okay. So what are the chunks that I'm going to give here? Here I have four chunks. I take each chunk and then I would count how many tokens are there in each chunk. And I'm keeping track. I'm calculating like how much I have used it. And initially the user will be zero. And I will keep on increasing it till I am able to build until unless.

1:14:03

I reach maximum tokens, right? Otherwise, what happens? If my, if I reach maximum, then I will not be able to write it. So this is my constraint that I have picked up, right? So let us try to run this. It's pretty straightforward because we are simulating it. So this is my retrieved chunk. I count. I count to the token.

1:14:33

previously using the same as the tick token. So I'm just formatting for the printing here and the context block, right?

1:14:44

Here, when you run this, you get a context block. And then if you run this, right?

1:14:51

What happens? You change included is four and the context tokens is 74 and the full prompt tokens. So what is my total token here?

1:15:03

What is my equal tokens? It is 111 plus 74 plus 4.

1:15:33

Right? So my full prompt takes around 11. Sorry. Okay. Sorry. Uh huh. My, my bad. So it is 11, right? The full prompt is instruction, context, context, block and question. With the 110, right? Let us say that what happens if I change the maximum tokens to 100.

1:16:03

We'll run this once again, right? Right? And then when once I run it, what it happens is that? It will use, it will use, it will, see, what happens is that once I have that once I have that budget right?

1:16:33

It will use the, until the budget after that it remains the, it will dimmer the chance.

1:16:40

So this is what the things happens when you have the context. Okay?

1:16:45

So let us go back and try to understand.

1:16:52

Yeah, probably, yes. That is your other activity. So that will go into it a little after a little few other activity. So that will go into it a little, after a little few minutes.

1:17:03

So now, let us come back here. So, so generally, so generally, how this context,

1:17:33

the memory and the agent looks. So short-term memory is nothing but is the conversation

1:17:41

of the scratch pad text included in the current API request. So if you see the, see your

1:17:50

prompts, right? So there's a scratch pad and the conversation that we could see. You can see the

1:17:56

whole thread, right? That's my shorter memory. So similar to our phone gallery, right? Our phone gallery can

1:18:01

hold 500 photos. But when I send a email, I cannot attach all those them. I can only

1:18:09

all of them. I can only send a handful of them. Right. So the model sees only what we attach.

1:18:20

Right. So this is what the short term memory talks about. Right. So it is a contest limit that

1:18:28

decide what these models will remember.

1:18:31

So that's a reason we suggest to have a JSON or a persistent storage where you keep everything for the remembering. See, for example, right? If you take this example, so everything what we have in the disk will be maintained, right? So then what we do is sometimes we have only the summary, right? For example, if I take an Excel sheet, I maintain, what is status and all

1:19:01

those things, but the physical file will be somewhere there, right? So the model sees only what it can see

1:19:09

in that context window. So this is the important stuff. So generally what happens is that,

1:19:17

generally the loop. So what happens is that when you have this kind of stuff, the major thing is, the context

1:19:29

window is always not limited, right? It is only limited and we use the disk memory

1:19:37

for the unlimited. And now not only this memory, right, you can use it in the cloud as well,

1:19:42

which is theoretically used you an unlimited. So what happens is that whenever there is a context

1:19:49

limit, right, it will stop the request from going beyond this window. So generally what happens

1:19:58

these are two things that will be there when we develop a production based agent. One is the loop control. The other one is the context limit. Why we need to have the loop control?

1:20:13

Very simple. See, LLMs, the agents will think and it will keep on thinking and it or it will be keep on, keep on running, right? So for that, stopping that,

1:20:28

we want to have the loop control. The problem with the loop control is it will lead to the

1:20:32

infinite cycle where it will be only in this thinking mode. But with the context limit also,

1:20:38

right, stop the request going beyond this, right? So what happens is that you need to

1:20:45

integrate the, when you are building the applications, right? You need to think about a couple of

1:20:53

things like the multi-term chat, right? So what happens is that?

1:20:58

For the, you have to, we'll come back to the multi-term in few slides and then the scratch pad is nothing but whatever the thoughts, whatever the questions that we have used and we have given the prompt and how it has resigned and then it has appended.

1:21:18

So the scratch pad is from the perspective of agent, okay? And then whatever the tools are but what we have, right, it also contributes to the

1:21:28

context limit, right? So this rag and memory will also affect the shared budget.

1:21:36

So the next question is, let us see how can we stimulate this context limit, okay?

1:21:43

The things will become very clear. So here what I have done is we have a four messages.

1:21:51

Like, we are, we want to, we'll send only the maximum as a four messages.

1:21:58

let me change the model the content that we have okay so let me copy

1:22:04

paste this and I hope you guys can send it okay so what we do is a we have a

1:22:16

window correct what this window does see see see whatever

1:22:28

Whatever the messages that you keep on adding, right, you will look into the window and then whatever it is out, right, it will be dropped.

1:22:37

Holder messages will not reach the model, right? Because I have restricted it to magazines of code, right?

1:22:45

I can see only the latest code messages here. And then here, right?

1:22:58

What happens?

1:23:05

This is the dropper messages.

1:23:11

And this is actually we are just calculating what are the dropper messages, right?

1:23:21

So basically what we are doing is that we are sending the messages.

1:23:26

See here, right? We are having a, we are calling the windowed history and I'm giving the full history. The full history as how many messages?

1:23:35

Three, seven messages, right?

1:23:42

Seven messages. What I do is I will allow only maximum messages, four. And what the message is, what message is sent?

1:23:52

So the older messages are dropped.

1:23:55

the model can only see the last four, right? So if you see here, right?

1:24:01

So the messages sent to model are four, which are those assistant content, 815B per report,

1:24:12

add in to 153, 90% growth and automatic margin frame, right? So you can see the last four messages are sought, are sent, and there are dropped out.

1:24:23

The older ones are dropped.

1:24:24

this is out that how the context windows limit your model. Okay. Any questions on this?

1:24:54

See, here we are similar. So I got a question saying that, sir, instead of the older one, why don't we prefer to write the latest methods?

1:25:03

See, we are dropping, see, the agent is dropping the older message. See, you can think about it, right?

1:25:12

So you are, see, the new content is coming in, the old contents are sent away. So this is what it is.

1:25:19

It is, you see, it is by default.

1:25:24

But these are the things work in the real models. So we are not, we don't have any idea, like any way to tell the model to keep, like,

1:25:35

this is a behavior, right? So model see the only the things that is there between this context window. So anything that is beyond the context window, it is pushed out.

1:25:54

So we'll come back. And we can, yeah, so we can look into the temperature, determism and see, what you mean by temperature?

1:26:24

What is the journalism and the non determism? Can anyone tell me? Can anyone tell me, what?

1:26:54

Yes, are you there?

1:27:06

Ah, kind of, but not exactly.

1:27:23

One plus one is two, right?

1:27:30

If you write in any language, it is the same, right?

1:27:36

So that is a deterministic.

1:27:37

So every time you get the same output.

1:27:41

Okay, whatever the program, see, let us say that I create a, uh, um, I create a, uh, um, I create

1:27:47

a certification system where you have a user, where you have a user.

1:27:53

and the username and a password. Every time I write my password, I have the user name, right?

1:28:00

If I write the username and password, what happens? It will check and if it is right, it will

1:28:06

let us take a simple example, right? Instead of that, I have my face of indication, right? So the same

1:28:13

face, sometimes if I just shave my beard and go, right? So sometimes it will, uh, uh, uh, so sometimes it will, uh, uh,

1:28:23

accept me as a legit user or sometimes it might not. It gets confused, right? Because

1:28:30

it could not make the decision. So sometimes it will allow, sometimes it will not allow. So that is

1:28:34

a high level of unpredictability. So that's where it is a non-determinism. Okay. So it is a more

1:28:40

informal way. But the thing is what is, uh, what is why determinism makes sense here?

1:28:53

We need determinism.

1:29:17

There is a two things, right? Ittermism and non-determism.

1:29:23

every time it is predictable, right? So for example, I go and I do math, right? One plus

1:29:32

one is two, no matter what, right? So, and then I take the addition. So if you repeat the same

1:29:40

operation on two, two variables, right? So let's say two numbers. That addition will be

1:29:48

a, there is a large, right? So basically what happens is that when we talk about the internet,

1:29:53

the output is same. The behavior is same. Consistent. The consistent behavior is called as determinism. What is non-determism? You will have a behavior, but that is not consistent every time, right? So for example, in a cricket, right? So if a bowler, if a fast bowler actually throw, like, throws a ball, right? So like ball, basically when he's bowling, right?

1:30:23

One ball will be exactly on the stems, the other one will be a bad ball and it might be wide, right?

1:30:31

You cannot predict how the, what will be the next ball, right?

1:30:36

It all depends at that moment, how, based on the dynamics of the, how the bowler has bowled the ball, right?

1:30:44

But what about the writing your questions, right?

1:30:54

You know the syllabus and after knowing syllabus, you know the previous question paper, and you know the previous question paper, and you know what sort of questions that you are going to get.

1:31:03

The what sort of questions that you are going to get is my deterministic, right?

1:31:06

So let us say that most of the time nowadays people give the model question paper and, and most of the questions will be like that.

1:31:13

and you will not get questions which is out of your syllable, right?

1:31:17

If you get similar to that, that's a non-intermuseum, right?

1:31:20

You don't know that, right?

1:31:22

So you would have never expected it.

1:31:24

So that's what the non-evalmism is.

1:31:27

So determinism is very important because when you see the LLM, right, you go and test it.

1:31:33

Every time you ask something, same thing, it, the, there will be variation of the answer, a little variation.

1:31:42

And the reason is, it is a token generation, which is a probability at the end of the day, it is fine.

1:31:48

But the problem becomes very tough when you design an application based on that.

1:31:53

Let us assume that the LLM generates some message.

1:31:59

And in next, for the same problem, it gives different one, little different.

1:32:05

So then won't you think that's a problem?

1:32:09

See, for example, right?

1:32:10

my program of user authentication will fail only if I give the wrong password, all right?

1:32:19

If I use the right password, no matter what, it will allow me.

1:32:22

With respect to when you have the LLMs, right, that's not the case.

1:32:27

There is the difference in behavior.

1:32:29

How do we control that, making, reducing the randomness, and that's where we come up with a

1:32:36

temperature.

1:32:38

When you set the temperature as zero,

1:32:40

it is nearly determined.

1:32:43

Most likely you will get the same output from your LLN.

1:32:48

Okay.

1:32:48

So if it is within 0.2 to 0.5, it will be a slight variation.

1:32:54

Still, it will be professional.

1:32:56

And more than 0.7 to, if it is between 0.7 to 1, it will have a lot of variance.

1:33:04

And the variations will look good when you have a, when you need a more creative stuff, right?

1:33:10

So if you want to.

1:33:10

to become more creative and want to brainstorm new ideas, right?

1:33:15

In that case, you will ask the temperature to be at one.

1:33:19

But more than one is not recommended in the experiments.

1:33:23

So the determinism helps in a lot of stuff because it makes the behavior of LNM predictable, right?

1:33:32

So that's one reason why we set this kind of temperature, right?

1:33:39

So what happens when you have at the low temperature, it picks the most likely work.

1:33:45

So which is very likely among the set of possible tokens.

1:33:48

When you have a medium temperature, you allow it to pick only the few alternatives.

1:33:54

When you have higher temperature, you are allowing it to pick up the things and it will throw you surprises.

1:34:01

So this is what it is.

1:34:02

And the other thing is we will have the sometimes what happens is that we will have a cheat.

1:34:07

Why we need to say it?

1:34:09

The reason is you use the LLM to generate some data sets.

1:34:13

Let me use the example.

1:34:15

Every time you generate the prompt or you run it, right?

1:34:19

Basically if you are in testing, you might be knowing, right?

1:34:22

So what happens when we do the testing, we generate the data and we run repeated, right?

1:34:28

So the same thing we do repeatedly with a different test case.

1:34:32

So for example, if I am building an application that takes user,

1:34:38

name and password.

1:34:40

I will give, in my test case, I will give the valid user name with a valid password,

1:34:46

valid user name with an invalid password.

1:34:48

When I, when I do the system, these are my test cases.

1:34:54

What happens if the LLM generates one set of output and when I, in the next case, it will go and change the other set?

1:35:05

So what happens is that?

1:35:07

It is extremely difficult when we have, when we are debugging it, right?

1:35:13

When you rise the issues, you need to go and check in the code.

1:35:16

If you cannot reproduce, how we are going to check it, right?

1:35:21

So for that reason to forcefully make the determinism de-use speed.

1:35:28

So the random sampling becomes reproducible for the text.

1:35:33

See, anything when you are, when you build any application, right?

1:35:36

any application, it has to go to the testing.

1:35:38

For the testing, when you have the machine learning-based applications, especially with LLMs, right?

1:35:43

You need to have the seed if it is available.

1:35:46

So that it generates the, so that it generates that you required data in a reproducible manner.

1:35:56

If you cannot reproduce it, it is very hard and nearly impossible to do the testing.

1:36:02

So that's the reason this temperature and the seed control the difference.

1:36:05

control the determinism of LLM.

1:36:07

See, at the end of the day, LR and LLM are non-deterministic in nature.

1:36:13

Right? Just think about it. After this class, you can go and use the chart GPD.

1:36:19

So you give a one-page text and ask it to summarize.

1:36:25

It will do the summarization. Ask it once again, do the same page page.

1:36:34

page content and ask it once again, it will generate not the same answer, it will generate a different, a little different.

1:36:44

That's what the non-determinism we are talking about.

1:36:46

This is a very important concept in LLM and please let me know if you have any questions.

1:36:53

I can wait for two minutes here so that we are very clear when you go further.

1:37:04

Sir, no.

1:37:22

So as I told you earlier, right, the temperature is zero.

1:37:27

It is the same answer every time.

1:37:29

Perfect for the rag and policy boards.

1:37:32

So when you want to have the creative.

1:37:33

want to have the creative and brainstorming, right?

1:37:35

It is like trying to hit every ball, right?

1:37:38

So sometimes it makes sense.

1:37:40

Sometimes it won't make sense.

1:37:42

So basically when you have a higher temperature,

1:37:46

you will see sometimes hallucinations.

1:37:50

Okay?

1:37:51

The chances of hallucinations are pretty higher.

1:37:54

I hope you guys know about alacination, okay?

1:37:58

And sometimes what happens is that you can create a beautiful variations with higher

1:38:02

with higher temperatures.

1:38:03

So the lower temperature is like a board exam key, answer key, right?

1:38:08

So this is what it is.

1:38:13

The seed we use it for the, yes, the temperature selection may vary domain to domain.

1:38:22

See, that's the beauty of the machine learning now, right?

1:38:27

So based on that is, see, everything is a curable parameters most of the time.

1:38:31

It gives you creative independence, design independence.

1:38:34

But you should be thoughtful of using it.

1:38:38

So that's the reason, right?

1:38:40

Now we see a lot of AI getting into the creative mode, right?

1:38:46

So this is the one reason why you can turn off the norms according to your domain.

1:39:00

So quickly I have a quick activity for you guys here, right?

1:39:07

So for the refund quality, lookup order tool and test you with a CM generator, right?

1:39:13

What are the things, whether you are going to use the temperature as zero or you use a fixed

1:39:20

see?

1:39:21

Can you put your answer from the chat box?

1:39:29

0 for the refund policy, yes, right?

1:39:38

So if you become, if you have a temperature, higher temperature for 0.9 for the refund policy,

1:39:46

obviously the customers, you will lose the customers and get into legal troubles, right?

1:39:50

So that's the reason it should be the low one, right?

1:39:58

Yeah, festival can be more creative, yes?

1:40:05

Lookup can be point three as well for the tool planning because it can generate to more tools.

1:40:13

Okay?

1:40:14

Yeah, obviously.

1:40:18

SMS generator can be more creative, right?

1:40:22

Getting into images, logos and all those things.

1:40:27

Let us go back.

1:40:32

What happens when we have a multi-term agent?

1:40:36

And before that, let us try to understand what is the multi-term agent?

1:40:43

This is nothing but the repeated cycle of model call.

1:40:49

You repeatedly call the model, you execute some tools, and then you once again call the model.

1:40:56

Right?

1:40:57

until you stop the condition.

1:40:59

Right?

1:41:00

So this is what multi-term agent looping.

1:41:03

So what is this?

1:41:07

What is this?

1:41:08

In a real, in a simple word.

1:41:10

What happens is that each we have a race happens in multiple laps.

1:41:15

First lap, every lap,

1:41:18

the runner carries a heavier backpack, right?

1:41:23

because I have used the tokens.

1:41:26

See, the token.

1:41:27

The token is something about my billing costs, right?

1:41:31

So the basic idea what we are talking about is that I have a model.

1:41:35

And then I would go and repeat a cycle.

1:41:39

I will execute something and I will go back and give that one to the model, right?

1:41:43

So this is what it is.

1:41:45

It is like a race where the every time the runner, after each lap,

1:41:51

if backpack feels heavier because of token usage, right?

1:41:55

simple, simpler, right?

1:41:56

things right so the auto rickshaw negotiation right if you if you if you if you go and here and there you make multiple wrongs right so what happens if he you might you might have negotiated for the few few wrongs right so generally what happens is that as you know right he thinks if he thinks that you get to know that your requirement he would also try to negotiate better with you

1:42:26

in the sense that he will also having the demand, right?

1:42:29

So for that, you will, what happens is that for every round?

1:42:35

Just say you have to go to multiple paths, multiple places using the same auto rickshaw in multiple rounds.

1:42:42

What happens, you go, you would have negotiated and you go in the first round and then you go to the second round.

1:42:50

And each time what happens is that he will have to try to observe everything.

1:42:55

And suddenly he tells that, okay, he forgets that, okay, your whole conversation, your previous conversation, what happens?

1:43:04

You have to renegotiate and you become confused and you become confused.

1:43:08

So that's the problem that we have when we have the multi-term agent.

1:43:14

So what you have to do?

1:43:20

What we do?

1:43:22

So this is a typical one, right?

1:43:23

We call the model first where you call the plan.

1:43:25

model for the plan. Let us take a simple example, right?

1:43:31

What, you see, typically everyone of us, most of us know how to book flights, right?

1:43:36

Let us say I want to, I wish to develop, use LLM for the model, right? The model goes and plans

1:43:43

with the vacation, whether about the place. What I do? And I will, and I will ask it to do that.

1:43:53

It basically does a search. And it comes back.

1:43:55

back and shows me the plan. What I tell, I tell some strangers and I will tell them.

1:44:00

And it will once again go. It will look into the plan. It will, it will refinish plan and then

1:44:07

come back to me. And finally I tell, okay, go ahead and book. What happens in that case?

1:44:12

When it goes to booking, you know, right, the flight as a very, the flight booking is a very little

1:44:19

window. Right? So what if the agent is not able to successfully do that, then booking,

1:44:25

then what happens? Most of the time, what happens is it? You might have consumed the context

1:44:30

window, like tokens. What happens? Once again, you along the back square one, right? So this is

1:44:38

what it happens. How do we add it? How do we modify this randomness? Right? So the first one,

1:44:46

you need to have the initial plan. So generally, in the initial plan, the token, this is

1:44:55

moderate, okay? It is not high. The reason is you, you write the question and you wrote the history instructions, everything is fine. But the random

1:45:07

is you should have the temperature as very less. You should not have the highest temperature. Otherwise, you end up with the wrong two choice. Other thing is after you do the search. So generally, the web pages will be high and it has to pass and it will consume some token.

1:45:25

And you have to, and as a result, it might paraphrase or it might alternate, right?

1:45:32

That will be an high risk. And then whatever happens is that you generally use Python-based

1:45:39

tools to do some work on this media, on this, and then you will have a medium token risk, right?

1:45:47

So the final answer, right? So for arriving at final answer, it has to include all those.

1:45:55

three stages that's where the the token risk is higher because it has to it

1:46:01

would have already consumed all those things right so that's a reason you should be extremely

1:46:06

careful when you do this multi-term okay so if the temperature is high you see there's a

1:46:15

very less very high randomness and you might figure it out that why the agent is behaving like this

1:46:21

So this is the more, this will be a problematic and more step is not better.

1:46:32

So basically when we talk about Python, we are talking about the interactive command and

1:46:38

execution, right, or using other tools in conjunction. So don't plan to have a lot of steps

1:46:45

when you are designing the multi-term agent tools. You can quickly run into the token

1:46:51

is the prompt will grow very fast, okay? And there will be a randomness if you have

1:46:58

not set the temperature properly. So generally what happens as they use the end user, that

1:47:05

it would have forgotten the constraints or it will give you the contradictory answer or it will surround

1:47:15

stops, right? And many times if it goes to the hallucination, say, if it is a simple,

1:47:21

Simple task, it is fine, but think about booking in an airline, right?

1:47:25

You might have given your credit card, details and all those things.

1:47:29

If it allocates and it gives the wrong numbers, then that's the real issues, right?

1:47:35

So even when you have the model loop, your context window, use the real budget, right?

1:47:42

So try to make a decision on you need a stable working.

1:47:51

or a creativity, right? Don't try to mix everything. So if you try to mix the journalism and

1:47:57

the randomness, creativity, you have a lot of things. Okay? So if something is not happening,

1:48:06

stop early and don't expect for the perfect memory. What you can do is as the prompt goes on,

1:48:14

you keep on stopping the, keep on adding the persistent storage, right?

1:48:21

So what are my practical implications?

1:48:28

Does one request include RAG and history tools?

1:48:35

So what are the things?

1:48:39

So what are the typical practical implication that before as a for a designer playbook?

1:48:46

And see, you see.

1:48:51

Whenever you are writing the prompt, the first question that we have to ask is when I'm going to write a prom?

1:48:57

Does that include the RAG student tools?

1:49:00

If it requires, then I have a window risk.

1:49:05

What you have to do, you have to think about the token budget and you have to do it accordingly, right?

1:49:12

So today's models will have different, different models have different concept of token budget.

1:49:20

So basically context limit.

1:49:21

So based on that planet. So don't jump and try to put everything in place.

1:49:28

And if the tool observations have greater than 500 tokens, once again, your multi-term look is at the risk.

1:49:35

So you would summarize the summarize before you read from, okay?

1:49:40

And you want to have the answers much match the policy wording.

1:49:46

So if you want that, then you have to set your temperature.

1:49:50

and you have to add the seed, right? Temperatures zero.

1:49:53

Bill will make LLM to push towards the determinism, but it won't guarantee.

1:50:00

So that's why reason you have to add seed in your test.

1:50:03

Okay.

1:50:04

So if the session turns 20, then there is a higher risk that it will be tanketed.

1:50:10

So you summarize and then summarize the memory gracefully.

1:50:15

Persistence it, keep it in a persistent storage storage and use it.

1:50:19

in the subsequent prompts so that you will not lose any information, right?

1:50:26

So if users are built per message, then it will be too cost.

1:50:32

So basically, whenever you are doing prompting, make sure that you know the estimated injection,

1:50:38

right?

1:50:39

So generally, right?

1:50:40

So basically for the system instructions have coronary tokens.

1:50:43

For chat history, generally, 200.

1:50:47

So in this way, you can.

1:50:48

you can have some sufficient space, right?

1:50:52

So whenever you are, so when you're doing this step, right?

1:51:01

So testing, you pick the good prompts, expected, define the expected strings, and then re-change,

1:51:08

and see how it is changing.

1:51:10

And before we go next, like, go with the key takeaway, let us take away, let us see some demos, right?

1:51:17

demos right let us say to understand few other examples right so what I have done is

1:51:25

I've installed the groc right so here I have installed the groc here we will

1:51:33

see the prompt quickly right we want to demo give the demo with respect to

1:51:40

how the low temperature higher temperature works okay so what I have done in one

1:51:46

sentence explain why over the air software objects matter for electrical vehicles.

1:51:51

This is my prompt, right? I'll just take this prompt and I run with the low temperature,

1:51:59

okay? The low temperature is zero here. If you see here, so minimize the random token choices.

1:52:04

And here I have taken the creative version where I have put it as a temperature 8, right?

1:52:10

If you see here, right, I'm just printing three times, running it three times. If you see here, what?

1:52:16

What is the things I'm getting?

1:52:18

See, over the year, summary updates matter for value because they are gainable manufacturers

1:52:23

to remote physics issues, improve performance, add new features, enhancing the overall

1:52:29

training experience, reducing the need for physical recalls, right?

1:52:33

So the first one and second one, a little different, right?

1:52:37

But second and third, stay.

1:52:39

Yes or no?

1:52:41

What about creativity with temperature?

1:52:46

as 0.8, fixed issues, improve performance, fixed issues, and think about these things, right?

1:52:57

It talks about physical visits dealership, which was not the case here, right? So these are the

1:53:07

difference. Can anyone tell me, can even tell me the prompt for the, can even give me a prompt?

1:53:15

I can run it for you. And the meantime I can run this high temperature as 1 and quickly run 1.2. And then quickly run through this.

1:53:30

This

1:53:45

requiring owners to physically visit a dealer ship or service center.

1:53:49

So these are the things work when you change the temperature.

1:53:53

Okay.

1:53:55

What I have used to do they drop.

1:54:03

So basically what happens is that the temperature is a knob, right?

1:54:06

Most likely and less likely.

1:54:08

The higher likely would lead to me to the stability of the same answer and a lower likely will

1:54:14

likely will reduce me will be more creative. So any questions on this? Can even give me one

1:54:22

prompt which I can run here with the prompt?

1:54:29

Let me, I did not create anything. In one sentence, explain, hello,

1:54:44

screen emission. So explain LLM. That could be better, right?

1:54:49

Right? Right? So let me run this. Okay, let me change. I'll change my prompt. Low temperature, higher temperature.

1:55:09

See, what is LLM? A L&M. A large requirement is a type of hot-reaching engine design design design.

1:55:14

to process and understand human language, generating human like text based on patterns in the sense.

1:55:20

In the second and third, I am getting the same, right? What about this when I am creative?

1:55:30

See, human like text based on the vast amounts of data it was trying on.

1:55:37

Generating text based on vast amounts of training data and complex algorithms.

1:55:42

Understand human language by learning patterns and there is to be in vast amounts of text data, enabling it to generate Pooharanan context to success. See how the things change when you change the temperature. All three, see, are different here, a little bit different. See, semantically it is similar, but if you see the third one here, right, is a combination of these two answers. So that's the one reason why you should be extremely careful.

1:56:12

when you are using the LLH.

1:56:17

Okay?

1:56:18

So finally, right?

1:56:20

So these are my end-to-end depressed autonomy, right?

1:56:25

So you have a typical RAD memory agent call.

1:56:28

So generally you need to have the system rules chunk,

1:56:31

chat history, and the scratch pad, right?

1:56:34

So where the agent reasoning starts and all those things.

1:56:38

And then finally you will have some answer for your

1:56:42

budget. So this is how you have to plan it. So basically what happens is that for a safety reason, right? So you need to keep at least 10 to 15% for the safety reason. So that you can address the variability and the price. So the key talk away. So tokens are the billing units, billing and capacity units unlike words. It is not words, right?

1:57:12

So context windows are the shared desk.

1:57:15

You should be very conscious of using it and temperature and speed are the knobs that will help you to achieve the design choice between being creative or deterring them.

1:57:30

And when you have a multi-term agent, they multiply your spoken and brand on the space.

1:57:36

So you should be extremely careful.

1:57:38

So designers should better agents when they,

1:57:42

budget the tokens. So it is extremely important to budget the tokens. And as I told you, right,

1:57:47

but knowing the context limit, context window limit is a bounded that will help you to design it,

1:57:53

right? So this is what it is, right? Treat every prompt as a finite token budget. Every prompt

1:57:59

is a one that you are going to incur, right? So nothing is spring. Even though there are

1:58:05

free models and all those things, right? But nothing is free. Right. So this is the takeaway. So

1:58:12

So in order to build applications, it's extremely important to control the randomness for the consistent and golden answers.

1:58:20

And this governing becomes even more important because LLMs can help say it.

1:58:25

See, if you are, if you see previously, right, what is the LLM, right?

1:58:29

When I made the temperature as 1.2, you could see the third answer was the kind of combination of answer 1 and answer 2.

1:58:38

So my honest advice is, please understand.

1:58:42

Not only the prompt, understand the output as well, along with the contest window to deliver the best applications.

1:58:51

Okay, without any surprises.

1:58:54

Ashthita, I am open for the questions.

1:59:00

Sure, sir.

1:59:01

Students, if you have any questions, please raise your hands, or you can type in the chat books.

1:59:12

So in the meantime, I can share it the, uh, the, uh, this one as well. Okay. Let me stop this day. I can share the, I can share the notebook. The only one thing is that I would be removing the grog key.

1:59:42

I just keep it this empty. Please paste your drop key.

2:0:12

So, there is a, like, uh, isha is, um, kit, is asking for the, uh, is asking for the, the, so, you have raised his hand.

2:0:35

So, guys, I have uploaded in one more.

2:0:42

So in the meantime, right, I have put it on the wormhole.

2:0:48

Please download it within an hour, okay?

2:0:52

Whether it will be deleted.

2:0:54

You have to add your drop key, okay?

2:0:57

That's it.

2:0:58

That's all the thing works fine.

2:1:01

Sir, the grounding thing is always part of the system from.

2:1:04

Also, when we limit the token, we must never omit the system prompts ever.

2:1:08

See, generally for the system from,

2:1:12

See, the grounding from is always, uh, grounding is always recommended because Eleanorz alacinies.

2:1:20

Okay.

2:1:24

So, see, when you are having the customer facing issues, right?

2:1:27

So facing with the things.

2:1:30

So as you know, is Eleon's is more genetic in nature.

2:1:33

You need a rag kind of stuff or grounding is extremely necessary.

2:1:37

That's the reason it should be a cropped up the system from.

2:1:40

Because it's the whole system, right?

2:1:42

The output, we are considering the LLM as a whole system.

2:1:45

So that's why isn't it should be a part of the grounding.

2:1:51

So don't ever omit the system from.

2:1:55

Yes.

2:2:00

So, Ashthita, can you unmute Ankit?

2:2:04

Yes, Ankhith, you are able to unmute yourself now.

2:2:08

I have added you to the panel.

2:2:10

Please unmute and ask you.

2:2:11

ask your question.

2:2:12

I have already asked my question via the chat window.

2:2:18

Okay, got it.

2:2:20

Thank you, sir. Thank you, Arshedananam for this.

2:2:23

Yeah.

2:2:24

And, sir, what PDF?

2:2:26

I don't understand, Muhammad.

2:2:29

I don't understand your question.

2:2:34

I don't understand your question.

2:2:41

Oh, notes video, right? Probably.

2:3:11

I will share it. I think it. I think there is a small problem.

2:3:41

I'll share with the team.

2:3:45

Sir, if this context history is maintained for session, see, the context is, the history is the whole thing that you get it for the trend that you start.

2:3:54

It is nothing to do with your session, right?

2:3:57

When you start karma thing, right, it will automatically create a window, right?

2:4:01

And that's what we mean to say the context window.

2:4:11

You could, when you open your chativity, right?

2:4:18

It has a stretch, right?

2:4:20

So the first question will be there and then you will subsequently start asking the questions, right?

2:4:25

So that, the whole conversation will make into the context.

2:4:28

See, from the user perspective, for us, it doesn't make much difference.

2:4:33

But think about it, that kind of plot and all those things that we are using to build a code, right?

2:4:40

it writes the code and that itself is a lot of tokens. So there the context window is just runs like this.

2:5:10

In the meantime, let me show you

2:5:40

So we have covered these stuff, right?

2:5:45

Configure temperature, user visible effects, right?

2:5:48

So this is done.

2:5:50

Okay.

2:5:58

So make sure that you download, you will download the, you should download within one hour,

2:6:04

otherwise it will be deleted, okay.

2:6:10

I think it's a bit of a bit of a bit of a bit.

2:6:15

And so,

2:6:17

it's a,

2:6:18

one,

2:6:19

it's,

2:6:20

it's,

2:6:21

it's,

2:6:22

so,

2:6:23

and,

2:6:24

so,

2:6:25

and,

2:6:26

it's,

2:6:27

I'm,

2:6:28

I don't know,

2:6:29

I don't know,

2:6:30

I think,

2:6:31

and

2:6:32

I'm a bit of a bit of a

2:6:34

I'm going to be

2:6:35

I'm going to be

2:6:37

and so that's

2:6:39

I'm,

2:6:40

the same,

2:6:41

and I'm

2:6:42

a bit of

2:6:44

so,

2:6:45

and so,

2:6:46

and

2:6:47

and

2:6:48

So I can leave, can I leave Vastita now?

2:7:10

I don't think there are any more questions.

2:7:13

So we can wrap up.

2:7:15

Yeah, thank you.