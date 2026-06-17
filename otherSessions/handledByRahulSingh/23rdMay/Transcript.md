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

Thank you.

5:30

Thank you

6:00

Thank you

6:30

Thank you

6:32

Thank you

6:34

Thank you

6:36

Thank you

6:38

Thank you

6:40

Thank you

6:42

Thank you

6:44

Thank you

6:46

Thank you.

7:16

Thank you.

7:46

Thank you.

8:16

Thank you.

8:46

Thank you.

9:16

Thank you.

9:46

Thank you.

10:16

Thank you.

10:46

Thank you.

11:16

Thank you.

11:46

Thank you.

12:16

Thank you

12:46

Thank you

13:16

Thank you

13:18

Thank you

13:20

Thank you

13:22

Thank you

13:24

Thank you

13:26

Thank you

13:28

Thank you

13:30

Thank you

13:32

Thank you.

14:02

Thank you.

14:32

Thank you.

15:02

Thank you.

15:32

Thank you.

16:02

Thank you.

16:32

Thank you.

17:02

Thank you.

17:32

Thank you.

18:02

Thank you.

18:32

Thank you.

19:02

Thank you

19:32

Thank you

20:02

Thank you

20:04

Thank you

20:06

Thank you

20:08

Thank you

20:10

Thank you

20:12

Thank you

20:14

Thank you

20:16

Thank you

20:18

Thank you.

20:48

Thank you.

21:18

Thank you.

21:48

Thank you.

22:18

Thank you.

22:48

Thank you.

23:18

Thank you.

23:48

Thank you.

24:18

Thank you.

24:48

Thank you.

25:18

Thank you.

25:48

Thank you

26:18

Thank you

26:48

Thank you

26:50

Thank you

26:52

Thank you

26:54

Thank you

26:56

Thank you

26:58

Thank you

27:00

Thank you

27:02

Thank you

27:04

Thank you.

27:34

Thank you.

28:04

Thank you.

28:34

Thank you.

29:04

Hello, hello, hello, good evening all.

29:34

So here we are and this is the class that we are having today, Advanced AI Topics.

29:44

Monday will be from a session delivery plan, Monday is going to be the concept last class and Saturday is your final review of Capstone.

30:04

different rag between normal LLM and RAG, foundations of RAG, the building blocks yesterday which was your retrieval, your query, collation, top K, top P parameters, and storage, tokenization, the six building blocks.

30:28

How do you adjust the chunk size, the different chunking strategies, and how to write an effective

30:33

prompt so that it can do exact word match, semantic word match.

30:38

And if there is something incorrect, if a incorrect token is picked up, then how do you kind

30:46

of pick the matrix, which is accuracy and recall, right?

30:51

So this is your session 30.

30:53

I'll just add here, session 29, just add the deck also here.

31:03

We'll cover concepts of MCP, what MCP is, what MCP servers are, what these SLM, small language models, and device-based LLMs, and then we'll look at token optimization, LLMOps,

31:33

A2A protocol. Some of these concepts also will cover. So yeah, thank you so much for joining.

31:44

Yes, so Ruppesha, we will have demos today. This is the status. I am waiting for Rishab Jane

31:55

to confirm finance. Okay, so this is also Project 5. I think these students have already given the first

32:02

round of demo. And we will do these demos today. So we will do that after we complete

32:11

the class so that students who don't need to sit back for demo. It's voluntary, right? I don't want

32:17

everyone to sit back for the entire demos. So yeah, I will do that at the end of the class for these

32:23

one, two, three, four, five, six, six students. Does that work? Okay, great.

32:32

I'll just give one or two more minutes for other students to join. In the meanwhile, let me.

33:02

Thank you.

33:32

Okay, I would also want to show you one ideal submission template. Do you want to see how your

33:41

final submission should look like? What all should you include? Like what?

33:46

What?

33:47

Okay, I'll show that to you so that you all understand what it is.

33:55

Yes. Yes, if you have doubts how to connect.

34:01

Loveable to Supabase, we can discuss that when you do your demo Rupesha.

34:08

So this is one of the submissions, right? If you see the person, I'll first play the video.

34:18

If you see the notion page, the problem statement, project photo, there.

34:28

Resume Analyzer, the tool, the tool, the front end is there.

34:31

The JSON file for backend is also there.

34:34

Right? But let me first show you the video and then I'll come back and

34:40

this is how your loom video should look like. Let me know if you are able to hear the sound. I'll just play this.

34:48

Hello everyone. I am Watsul Panery and this is my project submission for Capstone project.

34:55

Are you able to see this? Are you able to hear the sound?

35:00

Can you confirm? Okay. Okay, good. So this is an ideal format of how your video should look like. I'm just sharing it and I'll give this document also for you to verify, right? How it should explain everything. So let me just play this.

35:18

So let's dive into it. So this is the front end of the site and as you can see, it's very simple. First thing, what we need to do is a best job

35:30

description here. So as you can see, I have pasted a job description here. And the next step is to upload a file here.

35:38

So as we were told, it should take multiple resumes. So here I am uploading three resumes at a time.

35:46

See, as you can see, I have uploaded the three resumes and it will take it one by one. While this is being analyzed, let's check our workflow.

35:58

So the first part of the workflow is intake and extraction. The workflow kicks

36:05

off with the web book. As soon as the resumes is submitted, the system triggers a loop process

36:13

of the files. We use dedicated extraction node to pull the row text from the PDF, which is then fed

36:21

to the Google Gemini agent. This is done to clean up the data and normalize the candidate info

36:27

to a clean structured format. The next step is AI intelligent. The resume analyze

36:33

AI agent. The agent evaluates the candidate against our specific job requirements. It doesn't

36:40

just look for the keyword. It understands the context. Once the analysis is done, the data

36:47

is merged and log directly into the Google Sheets. The logic accent. Finally, the route makes

36:53

the decision based on the AI recommendation.

36:57

If they aren't fit, a polite rejection mail is sent to a Gmail.

37:03

If they are top-tier candidate, it automatically drops an interview, invite, and creates a Google

37:11

calendar event.

37:14

As you can see, the front end is updated with the scores and it also shows the meeting schedule.

37:26

So now let's see.

37:27

move to the slides.

37:32

Welcome to Recruit AY, agentic intelligence for modern hiring. We're removing the gravity from high volume recruitment with our anti-gravity philosophy and AI first architecture.

37:43

Meet Sarah, founder and TA manager.

37:45

So this is just the walkthrough of slides. I will share this document with you so that you can also

37:51

follow this template. Ideally, this is just the bare minimum that you need to have,

38:03

which is what is the problem that you are solving, which how did you define the problem?

38:08

If you have created some wire frames before actually building the into end-to-end product,

38:12

you can attach those wire frames also like screenshots of your project. And if you have the

38:20

have the front-end link, the backend link, the deck, the presentation that you have to make,

38:27

and your five-minute video link. In one single document, all of those can be submitted. I've shared this

38:33

with all of you. I'll just put this in the chat. And I will also put this in our topic coverage tracker

38:40

so that all of you have it handy. So ideal project.

38:50

So you don't need to do this right away because as we have discussed, we are in this week.

39:02

Next week you'll be doing your final demos on 30th May and some of you will also be doing this

39:07

today. So once this is done, you have one more full week to improvise, make it better and then

39:13

so that you are in the top tier of your batch, right? And I know some of you have done some really,

39:18

really good work. So you can pick all

39:20

of that by 7th June whatever your final template is record a video of that and then

39:25

submit the jason file for back end the lovable or whatever if you have used front end on

39:32

replate or cursor frontend link of that and the github link that will be learning on Monday to host the

39:38

entire project right so you have timeline till 7th of June any any questions on this before

39:44

we start with our content for today is this clear

39:50

Is this clear what needs to be done?

40:01

So you can just record the video Swati and then you can download the code repository

40:10

and push it on GitHub, the link to GitHub you can share.

40:20

Soaring will be done on, I'll just read the questions also. I am doing it on anti-gravity

40:27

local host. How will I show the link? You have to push the code to GitHub and then you can share

40:31

that link. That was a question from Satimayshari. We don't have to show or present the project.

40:37

That is not correct. On 30th of May, which is the Saturday, your final review will be there

40:46

where you will be given, each of you will be given seven to eight minutes. You will need to do the final

40:50

presentation so that and the idea of doing that presentation is even if you don't

40:55

if you are not able to submit on time or any part of your project is missing we would

41:00

have validated that and will give scoring here itself right on on these submissions I have

41:07

multiple workflows so I have to put each one yes either you can put all individually them or

41:13

what you can do is you can create two folders on your GitHub one is front end one is back end in

41:19

back-end you can have all those individual workflows added and you can give that link

41:23

harshavasti any other questions these are very good questions very relevant questions

41:31

avnish that is not possible like um the question is rag-based capstone project should get extra time

41:42

as we are still learning how to create rag that is not fair because

41:49

the other students we had given a choice of independence where you could have picked anything

41:54

like the concept was clear so i don't want at this point of time to randomize the time

42:01

we had shared this timeline five weeks four weeks back and there was an alignment and that's

42:05

why we did that entire session together in rag if i have to go back actually

42:11

we did rag with defy and i was showing you yesterday and d5 was already done here to build a rag

42:18

sorry i think i got stuck so defy we had already done

42:29

rag here so it was already completed uh that's an unfair ask at this point of time to stretch the

42:35

timelines we had i'd already given five weeks of timeline can i deploy it on versal yes hars you can

42:42

you can deploy it on vursal also any other questions from anyone

43:12

is this again uh i will share the outline or the template that was given to you

43:23

as part of this curriculum just calling this out up front we have done things a lot of things

43:32

which are outside your provided curriculum we have covered everything that is there in the

43:39

curriculum this today's session is one of

43:42

that where the topic are more advanced than what was promised on the curriculum itself

43:49

and i am doing this because i think the sense of maturity and uh the projects that you have created

43:56

it's very evident that you are AI first and you understand a lot of concepts that wise you are

44:02

able to build it these concepts are technical and therefore people is my internet unstable i don't know it

44:11

might be unstable i'll just turn off my video i because i can see one less bar on

44:17

this uh if you can confirm if you're able to hear me and see like see the deck properly now

44:27

okay so yeah this these are advanced topics and i am doing this out of goodwill that i

44:34

really want you all to learn and these are most of these topics are going to be very influential

44:41

probably in next two two and a half three years and you'll find as we discuss them

44:49

these are some of the technologies which are very very nascent at this point of time so when you learn

44:56

them our with all of them i have also given free high quality certification from good companies

45:03

like deep deep learning AI learning co and vdia microsoft google i have given certifications also so

45:10

so we'll be covering five topics any of these topics that you find interesting

45:15

saying hey this is something really cool and i would want to learn more about this please try to

45:21

spend some time and get those certifications done because what we are doing today is probably

45:25

a one zero one but if you want to go in depth and go to a 200 250 level you can

45:30

definitely pick them up as well right so with that let's get started and these are also the

45:38

topics which have come from your inputs in the first week of this module where i had asked

45:44

what are the things that you want to learn llmops token optimization cost model context protocol

45:51

these were the topics that you recommended and that's why i'm trying to cover them today

45:56

we'll go through these after each topic we'll take Q&A as well so that you understand what

46:01

exactly this means and how it works right so let's start with this first one

46:08

which is called model context protocol m cp this is a concept which was launched in

46:15

2024 by anthropic model context protocol if i had to define it in one line it is the USB

46:25

type c port for all the llm models what does that mean today you can ask a chat gptia

46:33

jemini or a perplexity that hey can you order food for me

46:38

it will not order the food it will ask you hey these are the items that you should

46:43

order go to zumato go to sui and order the food or if you are doing your financial analysis

46:50

and you say hey why don't you go ahead and place these uh investments for me on

46:56

zero da it will not be able to access the zero the tool because when we looked at

47:03

n8 and when we looked at uh make dot com also there are only

47:08

certain large big tech companies whose connectors are available connectors as in

47:13

you could connect gmail node you can you could connect the slack you could connect uh

47:19

probably or whatsapp and all of those right but if i have to take up my daily tasks is it

47:24

possible for me to add these tools to my llm and that is where the concept of mc comes

47:34

model context protocol any tool that i use

47:38

use i might be using swigi i might be using hot star i might be using spotify can

47:43

there be an endpoint provided by these companies that can directly integrate with my l lm and i can

47:50

use it effortlessly that is what an mcp is to give you an example i think zomato has launched its mcp

48:08

okay good so this has zumato mcp this is how it looks like i can also show you the

48:28

zero the mcp let's see the zero the mcp server this is the first company which gave

48:38

the mcp let me stop sharing and show you how its setup is done just give me one second

48:49

so this mcp setup does not work with the web browser version of clod or llm or your chat gpt and

49:01

jemni you will need to have the desktop version right so let me share my entire screen you will need to

49:07

let me know when the entire screen is visible is my entire screen visible

49:17

is my entire screen visible okay so see what are the instructions that they have given all

49:27

of them give very simple instructions go add this command mcp servers in your

49:33

developer config of cloud cloud desktop so i

49:37

my cloud desktop it's loading it says go to get started i'll just log this in and i'll share again

50:07

Okay. So, so my cloud desktop is ready, I'll go to settings, I'll go to settings.

50:37

settings in this it has connectors which you can directly connect or you go to developer

50:45

settings and in this you can have edit config this is the file the instructions that it says go

50:51

to your developer's left side bar and click on edit config and add these lines any mcp that you

50:58

want to add i don't have the zumato mcp added at this point of time let's try adding this

51:07

So open cloud, go to developer, go to edit config, and in the developer config, add the following instructions. Let's add this.

51:17

So, Zomato, let's click on this file and click on edit config.

51:31

This is the file. Let's open this up.

51:37

So you see all these MCP servers are already there, kite, which is by Zeroda.

51:45

If I show you the instructions of Zeroda, this is the command that needs to be added.

51:51

And then there is weather, there is playwright, there is Microsoft MCP playwright which is used

51:58

for testing.

51:59

All of these are already added.

52:01

I have to go ahead and add.

52:05

zoom to MCP.

52:12

This is your Zomato MCP added.

52:18

Save this and close this config file.

52:24

Right now if I go to my chat, if I see my tools, right, you can see there is

52:35

I think my screen is coming on top, so I'll let's track that aside.

52:48

So you see Microsoft is there, playwright is there, whether MCP is there, right?

52:54

If I want to add more tools from MCP, I'll just close this and restart it.

53:04

There is a question from Swati, why are we adding this?

53:07

For me to access these tools, for me to access my ZOMATO or my Zero Da or my Grow on all

53:14

of these LLM models, like we were orchestrating on NA10 or on Make, the easiest way is these

53:21

MCP servers.

53:23

You can add these MCPs.

53:25

With MCP, it's like an API call, what is an API?

53:28

It's like, hey, I am giving you an endpoint.

53:30

You can hit that endpoint and you can get all the functionalities or features.

53:34

teachers for me, right? Does that answer your question, Swati?

53:43

So yeah, let me just quit this. Let's launch Claude again.

54:04

Yes, that is what I'm trying to do, Saurav.

54:11

So Saurav is asking software adding, can I order food through Claude?

54:16

Let's try.

54:19

Let's see, do you...

54:22

Okay, so see, ZOMATO is now added.

54:25

It is asking me give the permission as soon as I logged in.

54:28

Are you able to see my Zomato screen?

54:34

Can you confirm? Because I'm sharing my entire skins, I'm just...

54:39

Are you able to access? Are you able to see my screen? Okay, I'll give access. Let me give my phone number.

54:48

Send OTP. Let's verify.

54:52

Okay.

54:53

Okay, this is the OTP which is...

55:03

which is not very safe but yeah let's try this okay authentication

55:12

successful redirecting back to the application this is done

55:18

server disconnected for troubleshooting Zomato MCP let's see do you have access to

55:27

Zomato tools

55:33

No, I don't have access to Zomito tools for Zomato related task.

55:37

Right?

55:38

Let's see what happened there.

55:41

Skills connectors.

55:44

Kite is there.

55:45

So my Zeroda is already attached.

55:47

But somehow the Zomato one did not get added.

55:52

Let's see.

55:53

Can you access my portfolio on Zerada?

56:02

So it says I have access, right?

56:12

It says turn on the settings.

56:16

And now it will ask me to log in and it will get the results.

56:21

So I can

56:24

Key Tools allow always.

56:29

And it says that you are

56:32

I'm giving you the link but interacting with zero the via AI is at your own risk right

56:39

if I go and click the link it will ask me to log in

56:44

once I give the login credentials I'll just because this is personal information

56:51

I'll just log this in and share the screen again

57:02

So it is this login is successful.

57:19

Let me share my entire screen again.

57:23

Tell me the stocks that I hold and this is a dummy account.

57:29

So let's see if it is able to pull that data or not.

57:31

Okay. So it says get holdings. This is an API endpoint that zero that exposes through their MCP server. You can just click always allow and it will be able to get your data. These are your holdings and these are your price. Current prices. Right. And that's it. You can ask it. Idea, stock. What is the Pandar.

58:01

fundamentals against what I hold. This is one of the dummy stocks that I'm just holding to get an insight on this idea.

58:10

And you can place your positions from here.

58:14

This is your average buying price, your current price, what is your intake and your fundamentals and all your analysis can happen here itself.

58:21

So this is the advantage of MCP and this is going to be the future of LLM based commerce.

58:29

Most of the applications pretty soon will start launching. I don't know if this one that we were trying from Zero Da is actually validated by Zero Da or not.

58:39

Zero Da sorry is validated. Zomato, I don't know if it is validated or not.

58:59

I already did this.

59:12

I don't know if this person is actually legit not let's say.

59:29

Let's give instructions.

59:37

MCP server, Zomatto.

59:40

Let's look at the configuration again.

59:43

Let's go to settings.

59:59

So command is MPX and the endpoint is MCP servers Zomato dot MCP.

1:0:08

MCP remote.

1:0:13

This looks fairly right. I don't know if what happened there.

1:0:22

Let's try to restart.

1:0:28

After the authentication, it should have been able to set up.

1:0:41

Let's see in the tools.

1:0:58

We have...

1:1:12

Okay.

1:1:13

This looks like it's not setting it up.

1:1:28

I'll set this up and I can walk you through this because I'm also trying this for the first time.

1:1:33

I don't know if this is validated and this is actually provided by ZOMAT or created by some AI enthusiasts.

1:1:40

Yeah, it is asking for permission.

1:1:43

It is also...

1:1:48

I'll just check if the SMS is actually coming from Zomato or not.

1:1:56

It is coming from Zomato.

1:1:57

This is where it is failing. I think the callback is not happening.

1:2:12

I could not attach the MCP server.

1:2:24

What is the error?

1:2:26

Server.

1:2:27

Let's click on view logs.

1:2:37

Server connected and successfully set up, but then authorization also worked.

1:2:47

Authorization required.

1:2:49

Okay, the server callback is failing because it's trying to hit local host.

1:2:56

Okay.

1:2:57

idea. Now, let me stop this. You don't want to train this. Most, if you go to MCP marketplace, right? A lot of companies, they have this portal where they have MCP market. Almost all companies have provided their MCP servers here, like 11 Labs, Firecrawl, browser base, Unity, Excel, right? If you look at the biggest

1:3:27

provide us from Microsoft also.

1:3:32

Microsoft 365, right?

1:3:36

Microsoft Playwright, Microsoft Docs, Microsoft 365, Core, Exchange,

1:3:40

Microsoft to-do, Microsoft Fabric.

1:3:43

All these are provided as,

1:3:46

so if you want to use Microsoft Teams via one of these LLMs,

1:3:50

right, it provides you those functionalities and it gives you the instruction,

1:3:54

how can you set it up?

1:3:55

Mostly the setup instructions are very,

1:3:56

up instructions are very similar, exactly like this, MCP server, name, and then the end point

1:4:03

that you need to hit. This is kind of the future or this is the kind of technology where a lot

1:4:11

of providers are setting up their MCP servers. How to create an MCP server, how to publish

1:4:17

it so that anyone else can use it?

1:4:19

Okay, there is a question. Will it help us in trading? Also, is it same?

1:4:26

to share your personal info with AI. It's definitely not safe because it tells you that, hey, you are doing this at your own risk.

1:4:33

But then this is going to be futuristic because think about it, right?

1:4:38

Today we use so many of these tools and we do the planning with LLMs, but we do the execution on those individual tools.

1:4:47

We would love to operate our Excel, our SBA, you know app, our Zeroda, our Zomato, our Uber, all of that through LLM.

1:4:55

You are chatting, you are doing your

1:4:56

regular work with chat GPT and you want to book your Uber. You would want Uber to provide you with that MCP server that you can connect and book it from there, right? So that's why it's an evolving technology. Today it is stateful. In future, there is a lot which is happening on MCP and that's why I wanted to cover it for you. You can attach your MCP servers of Notion, Zeroda, Mero, Lovable. All their MCP servers are available. You can directly, once integrated, you can then

1:5:26

And I think, Talley, I don't know, Swati, but if it is, I would love to see something from Talley, Angel 1, all of these companies as well, right?

1:5:36

We can imagine how powerful it will be if they come up with their MCP servers.

1:5:40

I, in fact, know the head of product in Talley, if you want to connect or touch base with him.

1:5:48

We should, and he was one of the learners of my AI course. So he is the head of product at Talley.

1:5:56

So he's the GPM at Talley.

1:6:03

He's been there for 15, 20, okay, 21 years.

1:6:06

Almost the head of India.

1:6:08

You can connect with him and check with him if they are internally trying out the MCP servers for Tally.

1:6:13

And if you can get early access to try it out.

1:6:16

It's a fantastic, I thought that you have, Swati.

1:6:19

So, yeah, same is with Angel 1.

1:6:22

You can touch with touch base with,

1:6:26

uh, Sakshi Mangwani. She is one of my mentee. Uh, she's working with Angel 1.

1:6:31

If you want to just check if they are building something on the MCP or not, Ruppesha.

1:6:37

Okay. Is this clear? Any questions on this? So this is like an endpoint creation. How it works.

1:6:45

It wraps your existing API, your existing endpoint or your existing applications.

1:6:50

Gives a specific instruction that can be integrated into the config file of LLMs. And

1:6:56

And on that LLM, then whenever you give a login, and every time you end the session,

1:7:02

you start a new session, it will ask you to log in and verify.

1:7:05

So, yeah, and then it directly interacts on your behalf with that app.

1:7:17

Can I add both make.com and internet and workflow to my system?

1:7:20

Yes, you can do that. Yeah, they can both work in parallel.

1:7:25

So it's built.

1:7:26

for defining tools and endpoints. Okay, quick recap, MCP server is a USB type C port

1:7:37

which allows any external tools, application, softwares to connect with LLMs. What we were

1:7:43

trying to show right now is the MCP server of Zeroda, which you could connect and you can start

1:7:48

sending messages and start interacting. Right. To set up your MCP server, you need to

1:7:54

define a standard schema, how to create MCP server and if you want to do deep dive, I have

1:7:59

added this deep learning AI course. It's very easy. It's slightly technical. It's for people

1:8:07

who understand coding. It's for them. If you want to create your own MCP servers, the capstone

1:8:13

projects that you are building, if you want to expose them as MCP servers, this is like a half an

1:8:18

hour course. You can do this and another one hour you can probably complete setting data.

1:8:24

Right. And in this deck itself, all the courses of all the topics that I'm going to cover for advanced AI are already available.

1:8:36

Okay. What do you track for setting up of MCP? How many times was it able to successfully call the MCP and set it up? Like the failure rate of Zomato was 100%. Two times we tried calling it. The tool success rate was zero. Right. How much time does it?

1:8:54

take to give the response from zero, like that is your latency.

1:8:58

And how grounded is the response in the actual data? Is it actually getting the data or is it fabricating

1:9:02

some of the data? And if there are any permission violations or if there are any data breach, what

1:9:11

Ruppesha was saying, then how do you identify that? If there is someone else who's trying to access

1:9:16

your login, like using Zomatok MCB server, somebody is trying to place my order, sorry,

1:9:23

is trying to place orders on my behalf, right? How do you track that? Like permission violations,

1:9:29

those are some of the metrics that you need to keep in mind while you think of MCPs.

1:9:37

Is this concept clear?

1:9:49

I've given you the instructions of setting up your MCPs. And, you've given you the instructions of setting up your MCPs and,

1:9:53

this deck also to cover. Yeah, you can set up a few MCP servers to start off with

1:10:01

Swati and then go through this course and try understanding how do you create your own MCP servers.

1:10:08

I think that will get you to more clarity.

1:10:23

You have showed how to do on AI tools. How will we do it on our website?

1:10:39

This course, if you go through it, you'll be able to understand. Like your endpoints of your applications,

1:10:43

once published, how can you convert them to MCPs? On N8 and also you can do it in a very standard format.

1:10:53

drop MCP configurations. Okay. This is slightly easier concept, but more prominent,

1:11:10

which you will start seeing a lot pervasive with the next versions of iPhone and the one that was

1:11:17

released two days back, the Google Pixel phone. The concept of LLMs being online.

1:11:23

or the concept of LLMs being hosted centrally and then we trying to access it is not scalable.

1:11:33

Why is it not scalable?

1:11:34

Because it needs a lot of data centers, a lot of compute and a lot of GPUs, which a common person cannot have.

1:11:41

Part 1. Part 2, people are very conscious and scared about their data getting leaked to

1:11:53

LLMs and their privacy being breached. That is where the concept of edge or on-devise

1:11:58

SLMs, small language models is coming into picture and this is growing very fast. Like Apple,

1:12:06

Qualcomm and Google are investing heavily in making your LLMs or SLMs available on your mobile devices.

1:12:14

Going forward, you will not work on LLMs, which is large language models. Going forward,

1:12:18

we'll work on on-device SLMs, which is small language model. What is a small language model? What is a small

1:12:23

language model. A small language model is something that works on your device,

1:12:29

creates the tokens and personalization, stores it on your device, and gives you personalized

1:12:35

experiences with the power of an LLM, but conceptualized on whatever you do in your daily life.

1:12:43

How does it work? Let me give you some examples. So Google Pixel, Apple's iPhone,

1:12:51

Snapchat lenses, Tesla's car.

1:12:53

and now Mahindra Naini is also doing that in India. All of them come in with inbuilt

1:12:59

SLMs. And these SLM's small language models are trained on the specific use cases. Like

1:13:07

a Tesla autopilot or a Mahindra 90 will only be trained to look on driving patterns, road sign

1:13:15

detection, auto maneuvering, self-parking, um, what is cruise mode.

1:13:23

Autopilot mode. These are just the six functions. It does not need to be a generalized

1:13:28

LLM. It's a very specific SLM. If you have not watched Google I.U. 2026, I'll just show you that.

1:13:36

Please spend some time. It's a 2-hour video. But please.

1:13:53

And you might have observed all the icons after Google I.O have changed of all the Google products.

1:14:02

All of them have changed. There is this CNETA summary video. Not this guy. I don't think it's...

1:14:23

that they only talk about what is changing with Google Pixel and the new phone that is coming out.

1:14:28

Right? And you can watch this as a summary video to start off by learning what all new capabilities

1:14:33

Google is launching. Right. Most of them are going towards on-device SLMs, where the sensitivity of the user data, their health, their voice, their photos, they never leave the device.

1:14:48

The LLMs are faster because they don't need internet.

1:14:53

One of the biggest limitations of today's LLM says that they work on internet.

1:14:58

But if they are on your device, then you never need to be connected to the internet.

1:15:02

And it reduces the energy cost that is needed to run LLMs to train them and to fine tune them.

1:15:10

You will end up paying that 50,000 or 90,000, 1 lakh in case of an iPhone to get up your own SLM,

1:15:18

which is on-device thing. And this is also a regulatory push from G.

1:15:23

GDPR, HIPA guidelines of US, GDPR of Europe, where they might be in future limiting the use of, a lot of companies also do that.

1:15:33

Companies say, hey, we will not allow an LLM usage in our company, but individuals can carry their own SLMs on their device.

1:15:41

This is the second technology that I wanted to at least cover for you.

1:15:45

So if anyone of you is wanting to invest or is looking to upgrade a phone in the next one, one and a half for two years,

1:15:53

try to focus or try to get on-devise SLM phone.

1:16:01

Because you'll really see the power of everything that you are today doing YLMs personalized on your use case

1:16:07

and then start training that SLM according to your own use cases.

1:16:12

So that's the second technology, not a lot of hands-on for us to do.

1:16:16

But I have again added a course if you just want to understand how the future chips of Colcom and VDR.

1:16:23

getting made for why on device and how these models work and how the deployment of these models is and how these are faster and better on energy consumption and on speed than your normal LLMs, right?

1:16:37

So this is the second concept just for you to know, nothing hands on or nothing for you to try.

1:16:44

But if you do wish to upgrade to a device type, this is the future of AI, one of the future, bigger future aspects of AI.

1:16:53

This is the one where I want to spend maximum time on in the class today, which is token optimizations.

1:17:02

So we have looked at tokens and we have used a lot of LLMs.

1:17:11

Like I was saying yesterday, the tokens are there at input, output, and processing all the three layers.

1:17:21

There are certain ways and there are certain.

1:17:23

applications that you should know on how you can optimize for those token costs and token utilization.

1:17:32

Right? And that is what I'm going to cover today. But, okay, before I get there, any questions on this on-devise, SLMs or how they are probably better than large language models and where they fit into our daily lives.

1:17:53

Just be aware about the things which are happening around you.

1:17:58

I think you'll be fascinated by seeing how this industry is evolving because the maturity or the growth of LLMs is done.

1:18:06

It's now more about SLM and use case specific on device SLMs.

1:18:16

Any questions on this? Is this clear?

1:18:23

Yep. You can watch the video and you can just complete the training so that you can, if you want to go deep, you can get that understanding. Yeah. Sure.

1:18:41

Okay. Okay, clear. Good. Let's talk about this. How can you reduce your token usage or token?

1:18:53

optimization. What are all the techniques that you know today? We have learned a lot of them.

1:18:58

One of them was in your make or in your n-8-10, you can limit the token output count, like a hyper-parameter.

1:19:06

Right? That was one thing. What else can you do? What are the techniques that you know for token optimizations?

1:19:23

How do you optimize for tokens?

1:19:24

Okay, rather than giving the entire long prompts, just give the keywords that are important

1:19:32

to take actions. Fantastic, Avnish. What else?

1:19:39

Use keywords and short forms. What else?

1:19:53

which consume less tokens. So choice of model is one thing that you can infer and

1:19:59

you can only choose those models which solve your problem and talk in the format that with minimal

1:20:06

tokens it can solve your problem like GBT Forum meaning great Sauravacharya. So one is rather than giving

1:20:13

long-form prompts, cut the prompt short, only give the relevant prompt which is called prompt pruning.

1:20:21

Second one is choose an LLL.

1:20:23

model which uses which uses and optimizes for less tokens by its nature, which

1:20:29

is given by Sauravacharya. Third one is what Faisal says that before you send your prompt,

1:20:36

you can rephrase or optimize your prompt from using another low-end LLM model, right? So optimizing

1:20:45

your prompt, what else? All of this that you are telling me is on input. What can you do on processing

1:20:50

and output?

1:20:53

Okay, change the context window after the few conversations

1:21:06

or update the context window after conversations. How do you do that, Amnish? How can you change the

1:21:13

context window? Again, writing optimized prompts is specifically writing optimized prompts is, specifically

1:21:22

writing optimized prompts is something that only impacts the input layer, not the output

1:21:28

layer. How do you optimize the processing and output?

1:21:31

These are very good ideas, by the way. Like, just keep making notes of this because these are also

1:21:42

important from your application when you build and when you make, you should take all these into consideration.

1:21:52

Optimized prompts. Okay. Let me get into this, right?

1:22:04

AI products don't fail because AI is not able to add value.

1:22:09

AI product failed because they are too expensive to scale. When more users start using your product, more

1:22:15

more tokens get burnt. Microsoft started saying, hey, everyone in Microsoft should

1:22:19

And yes, not using LLM for everything that needs input. It can directly come from

1:22:26

a basic rule-based check also. Don't always rely only on LLMs. That's a fantastic example, Mirage.

1:22:35

Microsoft initially started by saying all employees can use unlimited number of tokens

1:22:40

and can use how much ever clod they want. End of February, the bill that came, Microsoft stopped,

1:22:48

said, okay, stop. We are abusively using the tokens. And those of you who use Claude

1:22:54

might have seen Claude exhausts its limit like this. It burns tokens like anything, right?

1:23:02

So how to optimize this? So that personalization is not lost. Quality of responses is not lost

1:23:10

and it is accurate. Yes, fantastic fessel. Rag is a brilliant use case of how to retrieve relevant

1:23:16

information rather than getting everything from LLMs itself. Right?

1:23:24

We will talk about this from three angles. Let me. I think I have link of also this. Yeah. This is an architect of Google. I think they have removed his blog.

1:23:46

I have a snip of this, right?

1:24:00

So whatever you can call out, right?

1:24:02

Saurav Acharya is saying select smart models.

1:24:05

Aggregate your responses, don't take everything from LLMs only, which is what Mirad said, right?

1:24:11

change the context window and prune your prune your prong.

1:24:16

before sending it to LLM, what Faisal said. All of these techniques are valid. Let's talk about some of these techniques.

1:24:24

First one is prompt pruning. Before sending a prompt to the final LLM, you can use a low-cost

1:24:30

LLM to reduce the prompt or make only the keyword so that the action and the task is relevant.

1:24:37

That is called prompt pruning. You prune the prompt or you cut the corners of the prompt.

1:24:45

Second one is token.

1:24:46

Caching is if I know someone talks about the same tokens every time. Like let's take an example of Faisal. Faisal always talks about constructions and operations and maybe optimization of operations. Because I know that these are the common keywords or tokens that Faisal uses, I can store them and I can augment that with the prompt without Faisal asking.

1:25:16

them every time and I can build that in the in-memory context that Avnish was speaking about.

1:25:24

Third one that not a lot of you thought was model routing. So some of your queries can go to GPT 1.5. Some of them can go to GPT 1.5. Some of them can go to GPT 5.

1:25:36

Some of them can go to GPT 5.2. In Microsoft or in large companies, most of the queries that you ask, because on chat GPT,

1:25:46

don't know in behind the screens what chat GPD is using. Is it using GPD 5.2 or is it using GPD 2.5?

1:25:53

Which is cheaper? GPD 2 or GPD 5, which is cheaper?

1:25:58

GPD 2, okay?

1:26:03

2, 2. So if GPT 2 can give you good answers, why would you take your queries to GPT 5?

1:26:11

Your user don't care, right? Which one are you using?

1:26:16

to give the output. So you can route your query saying try solving it with GPD 2 if it is related

1:26:24

to payments, cashbacks, discount, order status. You can take it to GPD 5 if it is an escalation.

1:26:31

And you can take it to GPD 5 if it is an investment related decision. This is a very important

1:26:36

technique to get more value, 90% of the queries getting resolved.

1:26:46

by a lower end model and only 10% query is going to the higher end model. This reduces

1:26:54

the cost of processing. Token caching, prompt pruning is on the input layer. Processing pay

1:27:00

if you want to optimize, you can do model routing. I'll also cover the fourth one, which is batching

1:27:07

and streaming. Rather than giving the entire output and giving the entire answer to the user, try giving

1:27:16

them batches or stream of data and see if they are happy with smaller answers also.

1:27:22

If the user is satisfied with small batch answers, you don't need to burn your output tokens.

1:27:26

You can just do that sample batching. Over time, try with your audience what works for them,

1:27:31

and you can optimize for your tokens there also.

1:27:38

Then comes quantization. This is a machine learning or a data science experts role.

1:27:46

But kind of important for you to know if I am working in a particular domain, let's say Swati works in a sports business, right? Sports and sports equipment business. She does not need to use the entire LLM or SLM as it is provided by Chad GPT or Gemini. She needs to only pick those tokens, those weights and parameters which are relevant to her industry.

1:28:16

which is sports equipment.

1:28:18

So she can deploy a data scientist and say quantize this model only for this space,

1:28:24

like quantize this model only for healthcare,

1:28:27

or quantize this model for only finance, pick only those tokens and those keywords,

1:28:31

and give me a smaller model that can run faster.

1:28:35

That is what SLM creation is. That is what Servanum is doing in India.

1:28:41

They are quantizing the model for Indian languages.

1:28:45

Rather than saying,

1:28:46

we'll use everything that is there in GPT, we will quantize it.

1:28:50

And that is what deep seek also did.

1:28:52

Deepseek said, hey, we will find out the use cases that are mostly asked.

1:28:56

We will quantize it or we will filter it out according to those five or six use cases only.

1:29:06

Then other two things that you can think about what, again, Fassel said, is you can build your own rag and try to redirect most of your queries, internal company

1:29:16

queries via a rag.

1:29:17

One more thing that you can do about optimizing your processing in input and output

1:29:26

is you can give the fine tuning instructions in a way saying that only process if necessary.

1:29:33

Just this one line.

1:29:35

Another line can be process and refine only if the user asks for.

1:29:42

Apply reasoning only for the first level of understanding.

1:29:45

Don't apply reasoning.

1:29:46

to counter question.

1:29:48

These fine-tuning instructions make sure that the model does not keep looking for the best answer.

1:29:54

Generally what happens with Claude Opus and Claude Sonet is it iterates three or four times before it can give the right answer.

1:30:03

So you don't need to do that.

1:30:05

You can say, hey, only iterate once to get the answer.

1:30:08

Don't validate your answer again and again.

1:30:11

Do not cross-reference your answer until the user asks you to do it.

1:30:16

And then what I think Sauravacharya said, picking, and we had done that class, right, picking the right LLM models which fits into your per million token cost.

1:30:32

That is a very good exercise and it's a very big exercise for your own use cases.

1:30:38

Before starting by the choice of models, spend time and filter out which are the models which suit my best

1:30:46

case and then try to pick it up.

1:30:55

So these are all the techniques.

1:30:57

On the input prompting, you can do keyword-based filtering, you can do prompt pruning and

1:31:02

you can do token caching.

1:31:04

And you can also cache the most frequently asked responses.

1:31:08

So if the user is asking them same query multiple times,

1:31:11

you can also store their responses in their cache.

1:31:13

This is the input one.

1:31:15

On the processing, what you can do?

1:31:18

You can fine tune the instructions.

1:31:20

You can do quantization.

1:31:22

You can build your own rag.

1:31:25

You can do model routing.

1:31:27

On the processing part.

1:31:29

And what can you do on the output part?

1:31:32

You can do batching streaming.

1:31:34

You can, batching and streaming.

1:31:36

You can control the output hyper parameter of tokens.

1:31:39

How many outputs are to be given?

1:31:42

You can do sampling where you show user small

1:31:45

and if they like those small responses, you can stick to that.

1:31:48

Are these good techniques?

1:31:49

Are these good to know?

1:31:51

Any questions on these?

1:31:53

Any questions on these?

1:31:55

And you have all built applications.

1:31:59

And you have all built applications.

1:32:03

So I think you are, you should be able to apply all of these.

1:32:07

These are not very difficult considering you understand the entire ecosystem

1:32:12

of prompts now.

1:32:15

So how to add this into our applications?

1:32:26

That's a question.

1:32:27

I want to take that upright.

1:32:31

Saving or token prompts, you can, in your LLM or in your lovable itself,

1:32:35

you can tell it, hey, look at the user queries and store the keyword so that tokens are optimized.

1:32:40

Prompt pruning also, you can say whenever a user asks a query, prune the query, prune the

1:32:44

a query prune the prompt so that the token optimization is minimal and then take it forward.

1:32:51

And for model routing, when you are running and make.com or an innate and workflow, try to use two models.

1:33:01

Let's say GPD 2.5 and Gemini 2.5 and Gemini 3 or use Gemini 1.5 and Gemini 3.

1:33:08

And if the responses are of both good quality, then you don't really need to go for the latest one.

1:33:13

I hope that answers your question.

1:33:17

These are some examples how you can try your prompt optimization.

1:33:21

In the agent, you can say maximum token output count should be 500 per response, 2,000, 5,000.

1:33:28

And see which gives you a better response.

1:33:30

If 500 is giving you good response, you don't even need to go to 2,000.

1:33:35

Does that answer your question?

1:33:43

Okay, there is one large question. Can we say it in this way?

1:33:50

If we need information about something that is historical or already existing, even a chat GPD2 can provide that information.

1:33:59

And if there has been some any advancement related to it, that can be more advanced models.

1:34:05

Yes, that is right fuzzle.

1:34:07

So you can think it of it in that way precisely.

1:34:13

What are the token measures?

1:34:43

in mind let me just put this in full screen how many dollars are you paying for per

1:34:52

million tokens so launch this for a smaller audience let's say you launch it for

1:34:57

are you able to see my screen still

1:35:01

okay rather than launching it for a hundred thousand users in one go

1:35:12

Just launch it for 10 users and see how much token cost is coming and then extrapolate it to whatever your user base is before you actually make the final decision and do a product rollout.

1:35:25

How much average tokens are getting burned to answer one user query?

1:35:30

This number should always be in top of mind.

1:35:32

Any AI first company asks for this fundamentally, like when I also interview companies or people ask me, okay, you own Excel copilot.

1:35:41

own Excel copilot. For Excel co-pilot to resolve a query, how much average

1:35:46

tokens get burnt. And average tokens clearly in terms of input, processing and output, all three.

1:35:57

Then what is your cash hit rate? How much times the response is coming from the LLM versus

1:36:05

how many times is the response directly going from the cache? If you have 20 or 30 percent

1:36:11

responses directly going from your cache. That means you have a good caching strategy.

1:36:16

You are not wasting your LLMs. What are the number of requests that it can serve per minute or

1:36:22

per second in parallel, which is called a throughput? Number of requests of how many hundreds or thousands

1:36:30

of millions of users or does it break? Like what happened with Gipley? When every all Indians

1:36:34

started creating Gipley images, nowadays there is this new trend of a cartoon, your own cartoon being on,

1:36:40

on your image all over, right? How many requests is it able to create concurrently?

1:36:46

These are your performance measures which show are you optimizing for tokens or not?

1:37:03

Okay. Any questions on this part? On token optimizations? I'll just repeat because it's kind of

1:37:10

Kind of important and it's also one of the favorite questions in interview.

1:37:15

How do you optimize tokens across the three stages?

1:37:18

Input, output and processing.

1:37:22

So on the input, you can do prompt pruning where you can prune the prune the prompt and before sending you can make it smaller.

1:37:28

You can do keyword mapping where you store your keywords.

1:37:32

You can do caching of its responses input and output and you can have a smaller model to refine the prompt.

1:37:40

On the processing, you can select the model and do model routing.

1:37:46

Your model selection becomes important.

1:37:49

You can, on the model routing, you can also do your quantization, where you narrow it down and you bring it lower.

1:37:59

You can fine tune your instructions and you can apply a rag.

1:38:04

That's the fourth one.

1:38:06

On the output, you can do batching, you can do streaming, you can control your heart.

1:38:10

hyper parameter of token size and you can also do sampling where you show user

1:38:15

smaller answers if it works out well for them.

1:38:19

Any questions so far?

1:38:40

questions? Is it clear? Okay. We'll come to this, but before that I just want you all to run this prompt for me.

1:39:10

Let me share this with all of you.

1:39:19

Can I have one of you?

1:39:24

Can I have one of you volunteer please?

1:39:40

Okay.

1:40:10

is very precise in cloud where as gp t the big output it is just because they have

1:40:15

set the model to give output using minimum tokens yes mirage that's the configuration that they have set

1:40:21

up

1:40:22

okay the question that was set up

1:40:31

okay the question that was there was

1:40:34

from mirage since your panelists you can also see it when i give a prompt to the chat

1:40:40

the output is very long versus in clod it is very brief this is the

1:40:46

configuration that they have set up in clod so that is what i was explaining yes clod ideally

1:40:53

gives you concise outputs but the tokens that is burns on processing is much higher

1:40:57

that is what i was explaining can you share your screen and run the prompt library that i just

1:41:05

shared

1:41:10

Just go to chat GPT or Claude anyone and just run this prompt.

1:41:40

product designer.

1:41:55

That's it, yeah, copy till this till here.

1:42:00

Yeah.

1:42:02

Go to your lovable.

1:42:05

Just go to your lovable.

1:42:06

Directly let's try to run this in lovable.

1:42:08

Your lovable credits are exhausted, right?

1:42:09

are exhausted right?

1:42:10

Yeah, I cannot use lovable.

1:42:12

Oh, okay.

1:42:13

Anyone else who has lovable credits?

1:42:16

Who can volunteer?

1:42:18

Or you can try this in replet also,

1:42:24

replit or bolt dot new or cursor, anything is fine.

1:42:29

Okay, Rithu, I'll also invite you.

1:42:36

You can run the same prompt.

1:42:38

In any of that also, bold or new or?

1:42:46

Click on this.

1:42:50

Yeah, just paste that prompt here and run it.

1:42:53

Rithu, can you copy that prompt and run it in lovable for us?

1:42:58

Yes, I can. Shall I share my screen first?

1:43:06

Yeah.

1:43:07

I think Swati is.

1:43:08

already done this so we'll stop sharing for Swath. You can share it. Yeah.

1:43:38

paste it.

1:43:53

I'll just explain you the concept while this gets generated for Ritu and Swati.

1:43:59

Every company has an operations team and I'm sure most of you have already experienced this.

1:44:05

So think about an Ola.

1:44:07

Okay.

1:44:08

OLA will have a few people who are sitting in their Bangalore office.

1:44:12

They will have a very large monitor which will have an entire India map.

1:44:16

And it will show them where are the rides coming from?

1:44:20

Which part of Delhi, which part of Hyderabad is getting good rides, where the bookings are coming.

1:44:25

And if there is a particular area where the demand is very high, but if the supply is very low,

1:44:29

these operations team can quickly direct drivers saying,

1:44:33

yeah, don't stay in Bandra, go to probably Dada because Dada, the demand.

1:44:38

is very high but the supply is very low. And they can give incentive to those drivers.

1:44:43

Similarly, if think about Zomato, there is a particular city in which all of a sudden there

1:44:52

are a lot of one star, two star ratings coming in or there is a particular restaurant where

1:44:55

one star two star ratings start getting high. The operations team will sit and look at that

1:45:01

and quickly inform the leadership saying that, oh, something is going wrong. I'll give you my personal

1:45:06

experience. So when Mintra we were working,

1:45:08

I had written a code which went into production and it started breaking American

1:45:14

Express credit card payments. Like no credit card payments are going on. After two days

1:45:18

our operations teams came back and said credit card payments numbers are good, but one type

1:45:23

of credit card is not working which is American Express. And we could quickly debug, see what

1:45:29

happened, who had written the code, revert it and make it correct. That is the role of an operations

1:45:36

team.

1:45:38

Are you with me? Is that, does that make sense?

1:45:46

Correct. Now, what does LLM or AI operations look like?

1:45:53

It's called LLM ops or it's called AI ops. It's a very, very, very fast growing field.

1:45:59

Companies are making LLM applications. Companies are using AI. But how do they monitor if their

1:46:05

AI applications are working fine or not?

1:46:07

What are the metrics that they should be looking at? And if any of that metrics drop,

1:46:12

can they get automatic emails and notification? That is what is LLM operations. Like your business

1:46:20

operations, LLM operations is looking for everything that is happening on your LLM application

1:46:26

and proactively monitoring them. How does it work? They also have these dashboards. The dashboard

1:46:34

that the prompt library that I have given you is to create that type of dashboard.

1:46:41

Like what the large MNCs like Microsoft, Amazon, Google, what dashboards do they look at? What does

1:46:50

our dashboard of Microsoft M365 copilot looks like? That is what I've shared with you on the

1:46:55

screen. And this is a ready to use prompt in your companies or in your AI applications if you want to check

1:47:03

how your LLMs are performing. If anything is breaking, how do you evaluate that?

1:47:08

That is what it is going to create for you. So whenever it is ready for Rithu, you or Swati and

1:47:13

others also, if it is ready for you, you can share the link in the chat. We can quickly look at that.

1:47:20

Is the concept clear of LLMOps?

1:47:28

Let me know Ritu and Swati whenever your dashboard is ready. I'll come back and quickly share the

1:47:33

Gold is asking for money.

1:47:36

Oh, try on Replit?

1:47:39

I created another account on Lovibu.

1:47:42

And I'm trying on that.

1:47:45

So generally, while this completes for Swati and Rithu,

1:47:51

LLMOPs comprises of prompt lifecycle.

1:47:55

How many prompts are being asked?

1:47:57

What are the A and B flavors of prompt?

1:47:59

If a user is given A and B, which is the one that users are picking?

1:48:02

How many prompts are getting answers?

1:48:04

How many prompts are recommend follow-up recommendations are being taken up?

1:48:08

How many times the user is accepting those recommendations?

1:48:11

Right?

1:48:12

What is the rating of evaluations?

1:48:16

Are the evaluation saying that the responses are polite, safe, not harmful?

1:48:20

Is there any hallucination?

1:48:22

How much is the citation rate?

1:48:24

They also have a view like in Microsoft as soon as we enter the office.

1:48:29

The first screen that we see is

1:48:31

in which parts of the world and which type of prompts are being used to jailbreak or do adversarial prompting or how many attacks are we seeing every day?

1:48:40

So that dashboard is also created, right?

1:48:44

What is your token count?

1:48:47

What is your success rate, failure rate, and how many concepts or model drifts are being detected?

1:48:54

When was the last model deployed?

1:48:56

Which model is most actively being used?

1:48:59

Is it Claude?

1:49:00

Is it Gemini?

1:49:01

And if there is any complexity in resolving problems, what are the bottlenecks?

1:49:08

All of this data is available in one single dashboard.

1:49:12

You can toggle between the views.

1:49:14

And that is the role of your LLM ops team.

1:49:17

That is what they do.

1:49:19

Okay, it's ready for Rithu.

1:49:21

Rithu can you share your screen and show us?

1:49:24

See, so what it does is, can you publish this?

1:49:31

Click on Continue.

1:49:45

So it has Dashboard, Product Matrix, Business Matrix, Technical Metrix, Prompt Explorer,

1:49:52

everything.

1:49:53

All your views are.

1:49:54

there in this one single dashboard, click on publish.

1:49:57

Yeah.

1:50:01

What should we check?

1:50:19

How can we check this?

1:50:21

Yeah.

1:50:22

So, so I'm waiting for it to publish.

1:50:23

and then we can see it on the last screen.

1:50:25

Yeah, it is published.

1:50:27

Okay.

1:50:28

It is published in case.

1:50:44

Copy that URL and open that URL and open it in a new tab.

1:50:51

Yeah.

1:50:52

So whichever LLM model you are using, just give it some random name.

1:51:04

Like, let's say, finance application for LLM, something like that.

1:51:09

Yes, it consumes.

1:51:20

Yes, it consumes all the data file.

1:51:21

Fessel.

1:51:22

Once you give your API key and I'll show you like you can copy the same in the application context

1:51:28

also.

1:51:31

So if you see this Fessel, it asks you which model do you use?

1:51:35

Do you use Open A, do you use chat GPT and you can give your API key here.

1:51:39

Just select any drop down, select the LLM provider.

1:51:42

You can have Gemini, Claude, whatever model you use.

1:51:46

You give your API key.

1:51:47

Just give some random API key.

1:51:48

I've just set up at a sample account.

1:51:50

X Y, Y, Y, Y.

1:51:51

just type X, Y, Z.

1:51:53

Yeah, it will validate your API key.

1:51:56

If it is only validated, it will take you to the next screen.

1:51:59

Just click on validate API key.

1:52:01

It's not validating.

1:52:02

You need to give a right API key, right?

1:52:06

So go to your Gemini and give your API key.

1:52:09

A.I. Studio.

1:52:11

Yeah, Google AI Studio.

1:52:14

I'll give you the link.

1:52:21

This is the link, AISstudio.gov.com.

1:52:51

Just click on Create API.

1:53:11

You copy this.

1:53:14

Go to your LLM dashboard.

1:53:18

Select that is open.

1:53:19

No, no, wait, wait, wait, wait.

1:53:20

Wait, wait.

1:53:21

Select the above one.

1:53:22

It's not open here.

1:53:23

It's GPD, Gemini.

1:53:24

Yeah.

1:53:25

Yes, now validate.

1:53:26

It's not Pro.

1:53:27

So it's validated.

1:53:28

The API is validated.

1:53:29

Now if you see, it will show you everything around your API usage.

1:53:33

This is just sample data.

1:53:35

This is just sample data.

1:53:39

It's of course not.

1:53:40

You have used 1.28 million.

1:53:43

How many successful responses?

1:53:44

What is your latency, estimated cost?

1:53:47

All this is stimulated.

1:53:48

It's not real.

1:53:49

It's written.

1:53:50

it is real it is real. Like your million usage, your successful response rate, it's real.

1:53:55

Where it is simulated, it is simulated. Click on product matrix.

1:54:00

Now click on see what are all the prompts that you have asked? How much time did it take?

1:54:12

What is your success measure? What is your average satisfaction? All of these are simulated.

1:54:16

These are not real. Once you start using it, all of this will become real data.

1:54:19

will become real data. Again, click on business matrix. How many users converted? How many you are using GPT4? How many are using Gemini? How much is cost per one request?

1:54:34

So this grounds the click on Prompt Explorer. It will also show you how many prompts, what prompts your users are asking, how many tokens are getting burnt. Did the user get a successful response? Or it failed?

1:54:49

or it gave an error. This is an LLM ops dashboard.

1:54:53

All your business, all your product, all your prompt level data gets captured and stored here.

1:55:01

And this becomes a report out of success for your product teams, your business teams, so on and so forth.

1:55:12

Is this clear?

1:55:19

Yes, you can create similar dashboard for your co-pilot as well.

1:55:27

Okay.

1:55:28

So, like, how do we use it in day-to-day life or when to use it?

1:55:35

So this is every day your team, let's say you have an application which you have launched to your end users.

1:55:41

Every day in the morning or in the evening, your team will come and see how is your application behaving?

1:55:47

How are the users? What are the prompts that the users are asking?

1:55:53

What is the response rate? What are the token built rate per request?

1:55:57

What is the cost that you will end up burning?

1:55:59

So you don't see surprises. You can see all your transactions in one single place.

1:56:08

You can add as many APIs as you want FASL.

1:56:11

You can add APIs of GPT, Cloud, Gemini, whichever your users are using and it

1:56:17

all get populated here. Is this clear? Like this will be for applications which are

1:56:33

are using LLMs, right? Yes, that's why it's called LLM ops, LLM operations.

1:56:47

Data is taken from your API access directly, Swati.

1:56:51

Because your API, everything is getting tracked.

1:56:56

That's why you get your API key and you integrate it and you validate it.

1:57:00

Because you're billing, you're costing your token usage, all of that will end of the day happen

1:57:06

with API only, right?

1:57:14

Yes, these are the prompts which you will you will ask on that.

1:57:17

at API, it will get automatically logged.

1:57:19

Right now, the prompt that we've given is just giving samples so that we don't expose real data.

1:57:24

But these would be your users or your prompts.

1:57:29

It will give the data for the entire profile fessel.

1:57:32

It will not just give for one particular API.

1:57:34

It will give data of your entire application, how much ever LLM models you use.

1:57:39

So can you go to the technical matrix ones or business matrix?

1:57:43

See, it will show you latency percentiles by different

1:57:47

Models, if you see at the top, FASL, all models, GPD 4, GPD 3.5, Gemini.

1:57:52

If you click on those tabs, it will show you for that specific models also.

1:57:55

Just click on that Rithu ones on the top right, yeah.

1:57:59

See, it will give you the matrix for that specific model.

1:58:02

It will have filters like that.

1:58:07

Who are the end user of this?

1:58:09

There is always a LLM operations team with Sitz and the users are also the business, the engineers, the

1:58:17

product managers.

1:58:18

So think of yourself being an AI engineer.

1:58:20

One fine morning you come and say, oh, Gemini 3.5 responses are very low.

1:58:25

Or you say, Gemini is getting a large dissatisfaction rate.

1:58:29

What do you do?

1:58:30

This is answering Sheila's Basinette question.

1:58:33

Who are the users of this?

1:58:34

You are an engineer.

1:58:35

You have created an application using Gemini 3.5.

1:58:38

One fine morning you come and say, see, oh, all the users are just giving thumbs down.

1:58:43

What do you do?

1:58:45

Where will you go and check the information?

1:58:46

go and check the information? How will you check the information? What is your source of truth?

1:58:52

This is your source of truth. This will allow you to filter, get all your data, all your prompts,

1:58:59

all your user queries in one single place. You are a product manager and you have just upgraded

1:59:06

to GPD 5.2 because that's the latest model and you find that fancy and you've uploaded it.

1:59:11

Next day you come and see token usage has gone high from let's say 1.5.5.

1:59:16

million to 3 million. Where will you see that data? How will you see that prompt?

1:59:20

How much tokens are getting exhausted? This is the place. What is the average response size?

1:59:25

This dashboard gives you that view. So it is like your ECG of your applications heart.

1:59:37

Is it clear? The LLM ops use case?

1:59:46

Please confirm.

1:59:58

So what I'll do now is I'll send Swati and Rito back to attendees.

2:0:03

And we will also launch the feedback form

2:0:09

because we will now spend the rest 25, 30 minutes on product demos.

2:0:14

So those who want to and from a session.

2:0:15

to and from a session perspective that is what I wanted to cover today. LLM Ops, right? Your

2:0:22

token optimization on device LLMs, SLMs, MCP servers, right? So you can stay back. First

2:0:30

of all, let me know how many of you are there to... Okay, I'll let you complete the feedback. I think you are still giving your feedback.

2:0:38

So complete your feedback and then we'll see how many are there who are wanting to present their work today.

2:0:44

work today.

2:0:51

Can people confirm in the chat?

2:1:10

How many of you are wanting to present your work to doubt out of these people?

2:1:14

Puse Cauchel is there present present. Okay, who else? I just want to optimize for the time.

2:1:44

Rithu will also present.

2:1:56

So who will be remaining?

2:1:58

Sheila is not able to present?

2:2:01

Yes, I have written your project to Aditya Chandra.

2:2:04

Will you be presenting today?

2:2:06

Aditya Chandra?

2:2:14

Okay. So let's start. I think there are only three students who will be presenting today.

2:2:23

Others, if you have given your feedback and if you don't have any other questions, you can feel free to drop.

2:2:32

It is fantastic to see all of you. Do all of this and thank you for the amazing feedback.

2:2:38

Finstream AI. Okay, Swati's project name is Finstream AI.

2:2:43

I'll just share the screen again if you just want to.

2:2:54

Just validate your project names before dropping off.

2:3:00

And these three students, Ruppesha, Piyush and Rithu, if you are ready to present and if you have given your feedback, just type in the chat ready and I can invite you on the screen to share, start sharing and start presenting.

2:3:12

Okay.

2:3:19

So.

2:3:42

Thank you.

2:4:12

So we'll do like this.

2:4:14

Oh, it's not working out well.

2:4:21

Okay.

2:4:22

Piyush, you can go first and then Rithu and then Rupaisha.

2:4:26

A list.

2:4:29

Invite you one by one.

2:4:33

I hope you have given your feedback already because I think the feedback will close.

2:4:42

Yeah, others can feel free to drop. It's Ritu Yush and Rupesha.

2:5:12

Piyush, you can start presenting.

2:5:19

Or Ruppesha.

2:5:24

Okay, I think Puyush is back.

2:5:31

Okay, I can see Pooish's screen.

2:5:34

Yeah, Piyush, you can see it.

2:5:36

Rithu to present, you'll need to accept be promoted as panel.

2:5:41

be promoted as panlist.

2:5:45

Yeah.

2:5:48

So minus project five.

2:5:51

I have made a bank IQ tool.

2:5:56

I have used the level as rent-end and Defi as the backend.

2:6:02

And I tried Superbase, but Superbase is not updating right now.

2:6:08

But my database is getting captured in.

2:6:10

in level only.

2:6:12

Okay.

2:6:13

So it's a simple chatbot right now.

2:6:16

So I'm logging in.

2:6:19

So basically my problem statement here is

2:6:32

current account is a very typical product for banks.

2:6:37

One.

2:6:38

Second thing is there are

2:6:39

there are continuous change in regulatory guidelines from RBI.

2:6:43

Third thing is there is a huge attration at a branch level.

2:6:48

So attractions are at around 40 to 50%.

2:6:52

So although we are getting training to the people in the front line,

2:6:57

but still after two three months, half of the team is gone.

2:7:01

And for this, we have to keep a back-in team of around 870 people

2:7:06

who in turn

2:7:08

assist our frontline team on various

2:7:12

categories of current accounts.

2:7:15

So although we have chatbot,

2:7:18

but I want to add some additional functional functional

2:7:21

functional functionalities in that.

2:7:22

I've made chatbot this is my basic one.

2:7:24

Going forward, I want to add a

2:7:27

rack tool in this

2:7:30

in which whenever there is a new

2:7:33

circular which has been circulated by RBI,

2:7:38

here here you can directly

2:7:40

customer,

2:7:41

customer,

2:7:42

the front line team,

2:7:44

they can click on that

2:7:45

if you want to check online,

2:7:47

they can click on that and

2:7:48

they can get the

2:7:50

current circular or current

2:7:52

guidelines which are

2:7:54

come in recently.

2:7:57

So like this.

2:7:59

In this,

2:8:00

there's what I've got here,

2:8:01

here,

2:8:02

the scheme codes are here here

2:8:03

there are

2:8:08

This is the chat window.

2:8:11

This is the chat window.

2:8:13

It's some of your sample questions

2:8:15

up here.

2:8:16

Just like if I click on this.

2:8:18

And these are for any particular product type or these are for any product?

2:8:28

For current account only.

2:8:30

Only for current account, okay.

2:8:33

Good.

2:8:34

So I asked what is the revised non-mendentance charges for business classic CA from October

2:8:38

25.

2:8:39

This has me all of the entire

2:8:40

and then if I want to see the references,

2:8:43

I can see references too.

2:8:45

Nice.

2:8:47

And where is the rack getting stored for this?

2:8:51

Indy5.

2:8:54

So in Dify

2:9:00

I made a user input,

2:9:01

not a digital element and answer.

2:9:04

Okay.

2:9:05

And if I'm a user input

2:9:07

If I go to this,

2:9:09

I go to this

2:9:11

cloud

2:9:13

So,

2:9:15

so

2:9:16

you know,

2:9:17

so

2:9:20

you have

2:9:21

in this

2:9:22

chat history,

2:9:23

I've

2:9:24

I've been

2:9:25

here

2:9:27

just

2:9:28

I've just

2:9:29

just

2:9:30

only

2:9:31

only one user is

2:9:32

here.

2:9:37

Chats are getting logged.

2:9:38

Can you show me what are all the data sources?

2:9:40

How is that getting dynamically populated?

2:9:42

A knowledge retriever.

2:10:03

Kolo?

2:10:04

Knowledge.

2:10:05

So these are four documents which I have uploaded.

2:10:06

Okay.

2:10:07

These are manually uploaded

2:10:08

at this point of time.

2:10:09

Yes.

2:10:10

This is the master direction.

2:10:11

These are terms and conditions,

2:10:12

FAQ on master direction on K.

2:10:14

and then

2:10:16

Access Bank's document is.

2:10:18

Although

2:10:20

If I'm

2:10:21

access bank's documents

2:10:22

out

2:10:23

so I'm

2:10:24

publicly

2:10:25

level

2:10:26

that I have

2:10:27

there are many more things

2:10:28

which we can add into

2:10:29

into this

2:10:30

but when I

2:10:31

when I'll implement

2:10:32

in my organization

2:10:33

that will be much more robust.

2:10:35

Of course.

2:10:36

So you can all

2:10:37

have a pipeline set up where you hit the end point of RBI and auto fetch it.

2:10:41

But right now it's for MVP, this is fine.

2:10:44

There is one question.

2:10:48

Just a super base in your database

2:10:50

that's progress as well

2:10:51

but

2:10:52

this in here

2:10:55

here we're using

2:10:56

we're lavable

2:10:57

in this in

2:10:58

it's a

2:11:00

SQL or only?

2:11:01

SQL is it's a SQL database only,

2:11:03

it's a wrapper of Superbase only.

2:11:06

Okay, okay.

2:11:07

Got it.

2:11:08

It's a lovable wrapper of Supabas.

2:11:10

You got it.

2:11:11

Okay.

2:11:12

Okay.

2:11:13

Okay.

2:11:14

So this is great.

2:11:15

I think very sleek to use, very simple to use.

2:11:18

Well, integrated.

2:11:19

And I think you're the first one who has used

2:11:21

if I

2:11:22

back and front end on this to attach it.

2:11:25

I like it.

2:11:27

Thanks for sharing this.

2:11:28

And it is very consistent with AccessBank's theme also.

2:11:30

So good.

2:11:31

And one thing more.

2:11:32

If I'm

2:11:33

what I don't know

2:11:35

so it answers,

2:11:36

that please connect with your bank

2:11:39

RM to get this information.

2:11:41

It's not that

2:11:42

he will

2:11:43

hallucinate.

2:11:44

And that's a very important

2:11:46

or a valid use case of

2:11:49

rag right.

2:11:51

It should not hallucinate.

2:11:54

Like I think it's in

2:11:55

current chats

2:11:56

may

2:11:57

sure, Faisal.

2:11:58

If you want to drop off, you can drop off.

2:12:00

Have a good weekend.

2:12:01

We'll meet on Monday.

2:12:03

Avnish, I'm hoping you are all

2:12:05

ready for the Monday session to present the Codex and GitHub-Wala work.

2:12:12

Great.

2:12:21

That was there in the

2:12:24

super-based conversations only, no.

2:12:27

This specific information is not uploaded in the Access Bank documents.

2:12:30

Please check or connect with your relationship managers.

2:12:33

Nice.

2:12:34

Good.

2:12:35

Good. It's grounded in factual checks.

2:12:39

So this was all from my side.

2:12:43

Any more suggestions?

2:12:44

In which I can do you can record for demo for this is good.

2:12:48

I would request two more things.

2:12:50

One is you can have a D5

2:12:52

another workflow which auto fetches from RBA's end point.

2:12:55

You'll need to figure out that

2:12:57

it was just current account related information or contract

2:12:59

if current account related to it,

2:13:01

so how to download it?

2:13:02

That can be one automation that you can set up.

2:13:04

set up,

2:13:06

that automatically RBA

2:13:08

if any new circular release

2:13:09

then it can

2:13:10

add it to your defy database.

2:13:12

That can be one improvement, right?

2:13:14

And second improvement can be, but

2:13:17

that's when you implement internally.

2:13:20

This should also sync from the

2:13:24

user's current account history.

2:13:26

The user has

2:13:30

seeking from user current account history.

2:13:32

I've got it.

2:13:33

that's all of my chat history

2:13:35

No, no, this chat history.

2:13:37

The account history,

2:13:39

that's what transactions you have in

2:13:40

your current account in,

2:13:41

or your credit, or your debit line

2:13:43

on top of the tip can say,

2:13:46

that this is your recommendations are.

2:13:48

Make sense?

2:13:51

Got it.

2:13:53

Makes sense.

2:13:54

That's all for my say.

2:13:59

Awesome.

2:14:00

Thank you. Thanks,

2:14:01

Puyush.

2:14:02

or Ruppesha can start sharing.

2:14:05

Okay.

2:14:06

Okay.

2:14:07

We can see your screen.

2:14:09

I think.

2:14:11

Okay, we can see your screen with you too.

2:14:13

Pugh, I have marked you in the tracker as presented and ready to be submitted.

2:14:33

You can check the status.

2:14:35

Yeah.

2:14:37

So.

2:14:39

This is the problem I tried to solve.

2:14:42

This is for one-man army kind of stuff.

2:14:46

The people, one person who is handling everything on his or her business.

2:14:51

This is for them.

2:14:52

They can be especially therapists, service provider or coaching or consultant.

2:14:56

In the start of their business, they usually are the one-person team.

2:15:00

So this is.

2:15:02

And how I try to achieve the work space safety gate

2:15:06

at the start when they want to,

2:15:08

they want to like log in for the first time or create an account, they have to share some code, some invite code.

2:15:17

Then only they can get it.

2:15:21

So this is my app.

2:15:25

So if I sign out.

2:15:28

Yeah.

2:15:29

So we can create a new account.

2:15:31

We need to add a code here.

2:15:35

This is the account.

2:15:37

I added the form.

2:15:38

I have got password here also.

2:15:42

Then we get in.

2:15:44

So this is for the CRM, the general data of this.

2:15:49

This is the CRM pipeline.

2:15:51

Then they can also create some content for social media and they can also add their, do their bookkeeping stuff.

2:15:59

So everything in one app.

2:16:01

Nice.

2:16:03

Yeah.

2:16:04

So when they add any database.

2:16:07

So in the phase one, either they can share the link with the patient or they can fill this form.

2:16:15

Right?

2:16:16

And in the phase two, I'll try to integrate this form in their website or their Facebook or their Insta

2:16:22

where the patient themselves can fill the form.

2:16:25

And it is here.

2:16:27

After that, it is editable.

2:16:30

Any form that is here that can be edited.

2:16:34

the data is also visible on their dashboard.

2:16:41

This is in the board form.

2:16:43

They can shift the boards from one stage to another easily.

2:16:48

It is also in the table form when they want to either edit any data or delete any data.

2:16:55

So that can also be achieved.

2:16:57

For deleting, I have to do a lot of things.

2:17:00

The WhatsApp is also there.

2:17:03

So when I'm a lot of things.

2:17:04

never it takes me to the app and I don't know why it's taking me to this.

2:17:15

Okay.

2:17:16

Then I can also, this number may be, it may say that this is not on WhatsApp.

2:17:22

Otherwise I can, like this was the message.

2:17:26

Following up our conversation, do you have few minutes this way?

2:17:31

So this is.

2:17:33

This is.

2:17:34

This is the CRM. What I want to achieve more, which is like tags I can add when I am editing.

2:17:44

But I would also like to filter these via tags.

2:17:49

I would like to add the tags and filter this via tags in because I am expecting that one day it will be 1,000 people's database.

2:17:58

Then how this. So this is my next step.

2:18:01

I have also added that they can download it as CSW.

2:18:03

it as CSV and they can do whatever they want to do with it.

2:18:07

Maybe they want to give it to their marketing agency or for some data things.

2:18:12

So this can be also downloaded as CSV.

2:18:16

So this is the CRM.

2:18:18

Now for make, just give me.

2:18:22

So how I can add this, although this is not foolproof, but I tried.

2:18:27

So make.

2:18:33

Anything else.

2:19:03

basic the CRM should be able to achieve. So when we added this.

2:19:08

So it also changes.

2:19:20

When we try to add the WhatsApp, this

2:19:24

So, yesterday I tried all this, that's why it is saying one day.

2:19:27

Otherwise it will say just now or within 24 hours.

2:19:33

The link.

2:19:34

Yes.

2:19:35

No, this is very, very good.

2:19:36

I think a few things only you have done.

2:19:38

I have not seen any other project.

2:19:39

One is WhatsApp integration.

2:19:40

The second one is the referral base login.

2:19:43

And the third one is this table view versus row view.

2:19:46

So very, very good work.

2:19:47

I think very mature product.

2:19:49

I have a couple of feedbacks.

2:19:50

One of them is with the dark theme also keep light theme because people with

2:19:55

Yes.

2:20:00

Like color or visibility, disability, disability, eye,

2:20:03

can really suffer.

2:20:05

That is one.

2:20:06

The second feedback that I have is,

2:20:09

can you show me how the invoice upload is running automatically extract file?

2:20:13

Can we run that?

2:20:15

Yes.

2:20:17

Okay.

2:20:18

And also the database, what all you are storing in the database?

2:20:21

Yes.

2:20:22

So databases, one, the dynamic database is in this one,

2:20:27

it is here in Cloud.

2:20:32

So, I'm in.

2:20:33

I added the cloud but then lovable does not allow me to like disconnect this.

2:20:41

That's fine.

2:20:42

I just want to check what our tables it is creating.

2:20:45

So one is this basic CRM table that you have seen.

2:20:48

It has ID.

2:20:50

And in this also I want to add because it is saying therapist.

2:20:57

If you see the business profile, it will say therapist coach consultant.

2:21:02

But I may have two to three.

2:21:03

three therapists or four consultants.

2:21:06

So in that case, I would like to filter this as per that.

2:21:10

So I will add this, like the basic ID with which somebody is logging in.

2:21:17

So this thing is crucial I will add in the next just coming step.

2:21:23

Because here I have added like two therapists, but if I filter by therapist, I don't know

2:21:28

which therapist has added which data.

2:21:30

Tagging and filtering is easy to implement.

2:21:33

I think that should be straightforward for you to do.

2:21:35

So this is then this is for a leisure for the accounting purpose.

2:21:45

I tried with one to two accounts and these are all the profiles.

2:21:52

This is I don't know what.

2:21:54

Brand voice this is I have not added anything. This is for the content.

2:21:58

So, so first let's complete the front.

2:22:03

front end then I'll come to the database.

2:22:08

So this is here for the CRM, most of part.

2:22:14

To make this the saved records, we can like search here and it will have only six records.

2:22:21

After that we can search by elements, patient, history or tags, etc.

2:22:26

but it won't be like messy.

2:22:31

So if we have like have more than that.

2:22:32

more than like it has six records only but in the database we have many records.

2:22:37

So that's what I'm saying.

2:22:39

So it won't be messy here, the first thing.

2:22:43

And in the content, I have added a gem, I have created a gem and added it here.

2:22:51

So if I add like this, some, these are band stuff, this is what I want.

2:23:02

I have added the themes also.

2:23:05

We can add general or we can add some themes.

2:23:08

Like for the therapist, it is Mental Health Awareness Month,

2:23:11

but they may choose not to post mental health in May.

2:23:17

So it is something like this.

2:23:20

What is powering the gem engine?

2:23:25

Yeah, I'm telling you.

2:23:28

So this is habits.

2:23:29

So when I say generate,

2:23:32

Taylor brand content, it's say content is copied, pasted to the gem tab.

2:23:38

So if I go here, I can add my brand guidelines here in the gem.

2:23:43

This gem is created.

2:23:45

So for this and this can be copied also.

2:23:50

All the brand guidelines can sit here.

2:23:53

This is profile set up, one-time profile set up.

2:23:55

The person can set up their profile and they don't have to do this again and again.

2:24:02

And then they can create, for example, this, what we have copied from there.

2:24:11

If we go and create an Instagram or create a blog.

2:24:21

This is a reminder, Janet Metzen.

2:24:25

So here it is.

2:24:28

This is...

2:24:32

So it will create a blog in this.

2:24:38

For the general thing, I have added some guidelines which are like AI-proof guidelines, don't use

2:24:45

this kind of words, don't use this kind of word, like Unleash, etc., etc.

2:24:49

So I have added one full page of guardrails or don't do kind of guidelines.

2:24:56

And in this way...

2:24:57

Can we see that guideline also?

2:24:58

I feel bad for the eight people who have dropped off from the class.

2:25:01

This is just very powerful.

2:25:02

phones.

2:25:03

This is a reminder.

2:25:04

Okay, the gem I have created in my pro account here we can see.

2:25:11

This is a reminder.

2:25:13

Janet...

2:25:14

Alexa, stop.

2:25:32

These are the guidelines.

2:25:34

Okay, sorry.

2:25:47

This is how I set up first profile, like here.

2:25:53

Where I can see the guidelines that I have added to create this gem.

2:26:01

So it will say just ask setting up my profile and...

2:26:08

You can edit it, you can click on the left side button, edit and it will give you the guidelines.

2:26:13

That's okay.

2:26:14

Yeah, it should be here.

2:26:17

Yeah, here.

2:26:19

These are the instructions.

2:26:21

Not this is one time simple, zero AI test drop.

2:26:25

So I have these no AI words, no AI words, no fake words.

2:26:29

So I have this.

2:26:30

So I have this.

2:26:31

I've added these guidelines.

2:26:34

So this gem can be used and create the person can create the content.

2:26:39

In future we can add other things also like image creation or video creation.

2:26:45

But right now this is.

2:26:48

And yes, wait, sorry, I think it is not refreshed.

2:26:56

I have added the content calendar because when I was doing this, I saw that, yes.

2:27:01

Yes, after this it was not useful, it was saying Instagram also.

2:27:06

So I added this content calendar.

2:27:08

The person can add the calendar here, like they can see what we have posted about.

2:27:15

It can be at previous month also, next month also.

2:27:18

So they can have their content calendar here only in their dashboard.

2:27:22

And this is schedule, you can schedule this, pre-shedule this?

2:27:25

No, this is not attached right now to any Facebook or Instagram, but yes, I can choose that

2:27:30

whether it is planned, posted or schedule.

2:27:32

Like it can be my to-doist or task master kind of thing, like how I can do this.

2:27:39

But yes, in future, we can add this to the Instagram account or LinkedIn account where

2:27:45

we want to post it or schedule and it can directly schedule like we do in Kenba or something.

2:27:51

But this is for the phase two.

2:27:52

Right now we just want to add like what we have posted so that we don't keep running out of ideas

2:27:59

or we don't post the same thing.

2:28:00

twice or thrice a month.

2:28:02

So it will have a database for us.

2:28:04

But this is all manual.

2:28:05

Nothing here is.

2:28:07

You can attach this.

2:28:08

I think that should not be a big effort.

2:28:09

Yeah, that should not be a big problem.

2:28:11

But yes, in second.

2:28:12

I will attach a calendar view as well as because it took the table view,

2:28:17

but I wanted to attach a calendar view so that I can see the calendar

2:28:21

like monthly calendar view and then this automations.

2:28:26

This is.

2:28:29

This is.

2:28:30

This is what I wanted to see.

2:28:34

Can you upload a PDF and?

2:28:36

Yes.

2:28:37

So for example, credit, say I got 500 from Rehka as a follow-up fee.

2:28:51

This is client session.

2:28:53

Whether GST is applicable or not I can add, then commit, it will come.

2:28:59

So.

2:29:00

So when I pasted some text here, it takes the very correct information.

2:29:06

But when I added a PNG or PDF, it is not taking that much, like it is accepting, but amount

2:29:14

is sometime wrong.

2:29:15

So I have to check right now.

2:29:17

So this thing has to be improved a lot.

2:29:20

OCR text.

2:29:23

But if I add something here, for example, 300 at 3.

2:29:30

Starbucks for coffee tabit.

2:29:37

So process with AI accountant.

2:29:41

This.

2:29:43

So it is taking.

2:29:45

And then this.

2:29:47

Enter a valid.

2:29:55

Okay.

2:29:56

Sorry.

2:29:57

It is taken.

2:29:59

So this thing needs slight work but otherwise manual entries are taking

2:30:10

it's taking well and we can again delete at GST or this.

2:30:16

So this is now where I am struggling is one is, is this good for presentation or shall I add

2:30:26

or delete something else?

2:30:27

No, this is good.

2:30:28

I think this is very good.

2:30:29

very well executed.

2:30:31

Okay.

2:30:32

I don't know it will take the data.

2:30:40

Yes.

2:30:45

So if there is any data, it will send in Gmail also.

2:30:48

So this therapist one is complete.

2:30:51

It will create a super base row.

2:30:53

So if we add a new account, then it will create.

2:30:58

So this must have this.

2:30:59

created a row right now which is the date today.

2:31:04

Okay, let's try with another.

2:31:09

So we can add something.

2:31:12

It will, it never takes the same name.

2:31:15

If I repeat the then.

2:31:29

This, it has come here.

2:31:35

Why doesn't you take the same name?

2:31:37

Because there is already an existing record.

2:31:39

Yeah, so it takes the ID.

2:31:41

So if I like process the old data in this.

2:31:44

It is a unique identity.

2:31:45

Yeah, so it is a unique ID.

2:31:47

So it doesn't take the same, if I like process the same data,

2:31:51

I process the same data, when it says run once and use existing data.

2:31:58

So it won't run.

2:31:59

it won't, it will say this the operation then error.

2:32:05

So then it won't send the Gmail again and again.

2:32:10

So right now I have to add the problem is this is if the super base is acting very well as

2:32:16

an external thing but when I am doing something in my database in the dashboard, then

2:32:23

lavable dashboard is updating.

2:32:26

For example, if somebody is in

2:32:29

discovery and then it goes to treatment then this this dashboard is updating.

2:32:34

But this one is not updating at that time.

2:32:37

It is only creating one row pipeline stage once added it is not changing dynamically.

2:32:44

The reason for that is it is added to the external agent and not directly to the

2:32:50

dashboard.

2:32:52

Yeah, database because I have added already cloud and if I have not added then I could have done this.

2:32:59

But right now it is not able to do this.

2:33:03

Because both it's conflicting between the two databases.

2:33:06

Yes, yes, yes.

2:33:07

So like just for the examination point of view, I have added and created this so that you can see

2:33:13

because here it is taking the webbook data like as it is, but then I have to add JSON so that it can create a data structure.

2:33:23

Like otherwise it was taking name, email, everything in one row.

2:33:28

Yeah.

2:33:29

Then I have to add a router for all three and then this.

2:33:33

But the thing is it is not directly connected to this intake form.

2:33:39

So it is not dynamically changes.

2:33:42

Yeah, I can understand because there are two instances of super base.

2:33:46

We can try to resolve that.

2:33:48

I think if you once you add the filters and your OCR starts working, then you can solve for this.

2:33:51

Otherwise it's okay for presenting it in this level.

2:33:54

Okay.

2:33:56

So I have also decided what will be the phase two of all three.

2:33:58

is two of all three so that I can also share in the presentation.

2:34:03

Any suggestions?

2:34:04

Is this like front end, back end or database or it will be only considered the front end because

2:34:09

everything is on this database here.

2:34:11

Everything is here.

2:34:12

Both will be considered.

2:34:13

That is not a problem.

2:34:14

Okay.

2:34:15

Okay.

2:34:16

Okay.

2:34:17

Okay.

2:34:18

Thank you.

2:34:19

Any feedback?

2:34:20

Yeah.

2:34:21

One is the light theme and the other one is that OCR working.

2:34:25

That should be fine.

2:34:26

There is some text which is overflowing.

2:34:27

flowing but that is okay like not immediately.

2:34:31

Okay, okay, perfect.

2:34:33

Okay.

2:34:34

Thank you.

2:34:35

Thanks.

2:34:36

Okay, over to you, Rupesha.

2:34:39

Sorry to keep you waiting.

2:34:40

I know it's very late.

2:34:41

No worries.

2:34:43

Even I don't have my full product ready.

2:34:45

I just have my front end ready as of now,

2:34:48

but the front end is able to solve some problems without any documentation as well.

2:34:55

Let me.

2:34:56

Let me share my screen.

2:34:59

Retu, your status also have updated to presented and ready to submit.

2:35:04

So now you can see that in the tracker.

2:35:08

Let me know if you are able to see my screen.

2:35:11

Yes, we can see it.

2:35:12

So the name of my product is Decipher.

2:35:15

And Decipher is basically a one-stop solution for all the data enthusiasts like me.

2:35:23

So basically the idea comes from like I working

2:35:26

data domains would be data analyst data engineer data scientist or any

2:35:31

ML engineer that particular person would be able to go to this co-pilot engine and solve their day

2:35:39

to day problems which they are facing in their work day on a daily basis.

2:35:46

So this is like how the page looks like.

2:35:50

It's very pretty simple which tells you that this is a co-pilot for data.

2:35:56

scientists and cloud engineers and it can solve problems from query Azure,

2:36:01

AWS, SQL documentation with zero hallucinations and exact page level citations.

2:36:07

These are like some contextual things.

2:36:10

It provides like data science, cloud infrastructure and data engineering.

2:36:15

So once you set up your law account, like you can create an account or you can log in if you are already signed up.

2:36:23

You sign in.

2:36:25

So this is how you're like after signing looks like you have your first name appearing,

2:36:32

like just like we have a chat GPT or Gemini.

2:36:35

So what are you deciphering?

2:36:37

So you have like four options like the purpose it solves.

2:36:41

Data analyst and the data analysts, you would be able to see

2:36:45

like whether you want to solve any advanced Excel or VB operation or PowerPI or Dash operation

2:36:50

or any taboo visualization.

2:36:53

And the search bar is also.

2:36:54

bar is also automated accordingly.

2:36:57

Like it can, you can ask about Excel formulas, BBA macros, DAX, power BI or tablo.

2:37:03

Then if you are a data scientist, then it can cover your Python, R Studio, predictive analytics track.

2:37:10

And the search bar is also updated accordingly.

2:37:14

If you are a data engineer, then it can perform a SQL query ETL pipeline or AWS or Azure thing.

2:37:23

Or if you are an ML engineer or you want to solve any predictive analytics,

2:37:27

then MLLOPs, model architecture, XE boost, hyperparameters, model training, etc.

2:37:33

It can do. And every time the search also happens.

2:37:37

So you can also see your conversations, what you have like done previously.

2:37:43

And here is your account.

2:37:46

Then the free tier is like how many words you have used as of now.

2:37:52

So as of now, I want to incorporate the feed three year up till 100K words only.

2:37:59

And in case you want to use more than that, then you need to have a subscription of my website.

2:38:05

For that, I haven't done like a paid version thing as of now, but I think I might have

2:38:12

to use Stripe for the same to authenticate it.

2:38:17

And it, as I mentioned, as of now, it can perform basic functions without any

2:38:22

documentation, which I would be providing with the help of Defi, as of now that is not yet done.

2:38:28

But say, I put this command under Python, when I selected the data scientist and Python,

2:38:38

that I want to write a function which removes all the null values from my data set.

2:38:43

And it has given Python. You can see the Python code it has given, and all of this has utilized

2:38:52

91 words as of now. So this is also like updated accordingly how many births you are using.

2:39:02

And obviously like it can make mistakes, but it is verified by cited sources. So you can like

2:39:09

obviously verify your sources before you use anything. So this is.

2:39:17

Can you help me a function to remove all null values? But what is your data set?

2:39:22

So as of now, I haven't mentioned any dataset.

2:39:27

Obviously, you can put your data set as well, but sometimes you can't put any client-related information or client data sets,

2:39:37

but you need some function or some help with your thing.

2:39:43

Like, I work with SQL a lot, and sometimes we are stuck at a query.

2:39:48

So you can't put the client data on chat GPT.

2:39:52

or Gemini, that is not allowed. But if you want to like optimize your query, so it would

2:39:58

help you to solve those kind of problems. If you have a data set, so you have those particular

2:40:04

options as well, I think it is not yet integrated. But that is the plan. Like you can attach

2:40:10

your data sets and stuff like that, but it can create a kind of cedo code for you, which can help.

2:40:18

As of now, since documentation is not provided to us.

2:40:22

So it is like providing solutions on its own, which are not purely correct, but somehow, like, if you want to remove null, so this is the correct code as well in Python.

2:40:37

So that's like about the product.

2:40:41

I know there's a lot to do in this one.

2:40:46

But yeah, this is all I have.

2:40:49

One thing I wanted to do was like connect.

2:40:52

this to my super base as well so that I'm able to see who all have like signed up using my website so that I can like send them automated emails as well.

2:41:09

Like we usually get whenever we sign up to any account, hey, like this is some new feature or like telling them about the website or just

2:41:22

just to like see what they are doing. And considering today's class as well, if you can create the LLMOPS thing where I'm able to see what prompts users are giving to like maybe enhance it for future use, like whether I need to incorporate some other tools or functions which this particular website can solve.

2:41:52

Yeah, sorry.

2:41:53

No, go ahead, complete your thought.

2:41:56

Where I would be needing your help because I see like when I go to my lovable and I try to see the connectors.

2:42:07

So it shows me that my super base is enabled and when I see everything, so I think it is connecting my overall lovable to my super base account and not this particular project.

2:42:22

to my Superbase account and that is why nothing is happening on my Superbase.

2:42:28

So if you can guide me, how can I connect this particular Decipher project to my Superbase.

2:42:34

I also created the Decipher.

2:42:37

So it has enabled the Cloud Superbase.

2:42:40

Close this.

2:42:43

Go to your lovable, click on that cloud button.

2:42:47

Yeah, click on the database here.

2:42:51

here. See it's already stored here. This one is stored. So this is the wrapper of Superbase which is used here. And you can see the users listing here.

2:43:02

Who all are signed up and what all is there. Yes. Yes. So this is also Superbase only. It's a wrapper just for lovable.

2:43:10

Okay. So do I actually need a Superbase?

2:43:15

If you want, is it? Like what It was showing, it can get conflicting. I don't.

2:43:21

don't want that to happen right so if you don't want that then you can use this

2:43:26

use this native one itself right now i think rather than solving the super base there are a lot of

2:43:31

other things that you need to solve like there is no component of rag in this one yeah it's

2:43:37

just a ui that is answering queries for you plus if i want to write queries in python in vb script or

2:43:45

in let's say SQL queries itself that functionality should also be there and very

2:43:50

And when you start asking that it will not be able to give you queries,

2:43:53

because it has database's not even have the schema.

2:43:59

So I think all those need a lot of improvement before you solve the SuperBase thing.

2:44:05

So that would be done with the help of DFI documentation.

2:44:09

When I provide those like documentation that I have.

2:44:14

But that integration needs to happen, right?

2:44:16

Yeah, yeah, yeah. That I know. I was actually I didn't get time.

2:44:20

So I was working mostly on the front end first and then I go to the back end.

2:44:28

So there needs to be worked done before the submission on.

2:44:32

Yeah, yeah, yeah. Yeah, I plan to work a bit more on this tomorrow.

2:44:37

Maybe I have some progress by Monday.

2:44:40

And in case we get some time, we can re-look it at Monday. I let you know.

2:44:46

Okay, okay, sure. But this is good. I think the use case is very particular.

2:44:50

There is a lot of power that you can add to this.

2:44:52

But when you showed me Excel, VBA, PowerBi, Dax, Tablu, I was very excited.

2:44:56

But this is all UI.

2:44:57

Like there is nothing integrated.

2:44:58

Yeah, yeah.

2:44:59

As of now, it's not integrating.

2:45:01

Yeah.

2:45:03

Yeah.

2:45:04

Yeah.

2:45:05

Let's see this again on Monday.

2:45:06

Right now, I'll keep you in not ready state because the backend, the agentic workflow.

2:45:10

Yeah.

2:45:11

Yeah.

2:45:12

But we can come back and see it again.

2:45:15

Yeah, yeah, sure, sure, sure.

2:45:19

Okay.

2:45:20

Okay, this is very good. Thank you for starting it off. And thank you all for demoing, whatever you have done.

2:45:25

We are at 16 people who are ready to show their demos. The statuses are updated in the portal.

2:45:31

So thank you and we'll meet on Monday and deploy all our projects to GitHub. Have a good one. Have a good weekend.

2:45:40

Thank you.

2:45:50

