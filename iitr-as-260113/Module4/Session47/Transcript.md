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

Thank you

5:20

Thank you.

5:50

Thank you.

6:20

Thank you.

6:50

Thank you.

7:20

Thank you.

7:50

Thank you.

8:20

Thank you.

8:50

Thank you.

9:20

Thank you

9:50

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

Thank you

10:38

Thank you

10:40

Thank you.

11:10

Thank you.

11:40

Thank you.

12:10

Thank you.

12:40

Thank you.

13:10

Thank you.

13:40

Hi, everyone, very good evening.

13:45

Hi, everyone, very good evening, folks. Am I audible to all of you?

14:10

I think the chat is not enabled, enabled, okay, greater.

14:14

Okay, folks, we'll start in a few minutes.

14:16

Let's wait for more people to join.

14:18

I can see the strength is a bit on the lesser side.

14:21

Let's wait for two, three more minutes and then we'll start.

14:24

In the meantime, I'll also share my screen.

14:40

Thank you.

15:10

Thank you.

15:40

Thank you.

16:10

No, no, no,

16:13

No,

16:14

No,

16:16

No,

16:17

No,

16:18

No,

16:21

we have not started

16:39

not started yet. I'm just setting up my N8N dashboard. We'll start in a few minutes. Okay, we'll start in a couple of minutes.

16:50

Yeah, I'm just waiting for more people to join the class and then we'll start.

17:09

Thank you.

17:39

Thank you.

18:09

Thank you

18:39

Guys, the strength is very less.

18:46

What could be the reason?

18:48

There are only 15 people, usually the strength is around 40.

18:52

What could be the reason for me?

18:55

Are people, people are not able to join via the dashboard?

18:57

I'm not sure.

18:58

I also have pasted the link so that or if you can share with your friends.

19:04

If they are trying to join, they can join, they can join by it.

19:07

Yeah, yeah, correct, correct.

19:08

Because the strength is even

19:09

less than half.

19:10

Yeah.

19:11

Wait for maybe two, three more minutes then.

19:39

Thank you.

20:09

Thank you.

20:39

Thank you.

21:09

Thank you.

21:39

Thank you

22:09

Thank you

22:39

Thank you

23:09

Hi,

23:12

Can everyone, can everyone, can everyone, uh, can everyone hear me, can everyone hear me,

23:15

am I,

23:17

to all of you,

23:19

can everyone hear me?

23:37

Can everyone see my?

23:38

as well.

23:41

Okay, great.

23:42

So folks, today's class is again based on N8N.

23:46

And we will have two classes on N8N now.

23:49

Like we have already, we already had one class on N8N, where we just went through the basics of N8N,

23:56

what all the features, like some of the features does it provide, how can you create a basic workflow

24:00

workflow, etc., the nodes etc. we talked about.

24:03

Today's class is going to be based on, create a basic workflow on a basic workflow on.

24:07

N8N. Okay? Make sense, everyone? Today we are going to create a very basic, a starting level of N8N workflow. And we have one more class on N8N on Friday now, right?

24:19

Unfortunately, because of some important work, I could not take class on Monday, right? So Somer took the TA session or the tutorial session in place of my session.

24:29

So now, instead of having class, like the Monday's class, we have moved to Wednesday, and Wednesday's class we have moved on Friday.

24:36

So just manage for this particular week, right? So we will have class on Friday now. Sounds good, everyone.

24:43

So the pending class that we could not have on Monday, we are having today. And today's class, we are moving on Friday. Okay. So thank you so much for that. And sorry for the, sorry for the schedule change. That was something that was not in my control. Something unexpected happened and I had to, I had to be there. Okay. Great. Now, first of all, everyone tell me that how

25:06

many of you were able to run N8N on your local. That is very important.

25:10

Because today's class is going to be completely hands on. And I want all of you to also participate in the

25:16

discussion and do things parallelly. Okay? Because guys, N8N is not like coding that you can understand and

25:23

implement later. N8 is kind of a step by step process. Okay. If you miss any step, you might have to start

25:29

from the beginning. Understanding this point. So I want all of you to participate in the discussion in today's class,

25:35

specifically as much as possible and try to do things parallelly in the class.

25:40

Everyone, clear?

25:42

Then it will be the best learning for you specifically if you talk about N8N.

25:46

Okay. And once you build one or two or maybe two three workflows on N8N, then you will be very, very

25:52

comfortable. Okay. How many if you were able to run after last class that we had on Wednesday,

25:58

last week, one week back, how many of you were able to run N8N on your local using Docker?

26:05

Tell me. How many of you were able to run?

26:13

Guru Prith, okay? Great. Good work.

26:17

How many other people were able to run N8N on your local? I explained the process, right?

26:22

Kishore, good. First, everyone, you have to install Docker. Correct or not?

26:28

See, guys, for learning purpose, for building small projects, running N8N on your

26:35

local is very easy and very convenient also. You don't have to pay any money, use any 10

26:39

as much as you can, build any number of workflows. There is no limit. In your local, it is free of cost.

26:45

So please, please make sure that you do it right away. Install Docker and then create, just you have

26:54

to execute these two commands by changing the time zone. Remember that? First, create a volume.

27:00

Now, do we already have a volume running in my laptop? Did we already, did we, did we, did we

27:05

create a volume actually. So let me show you the dashboard. And if you go to the volumes,

27:09

if you see, we already have this N8N data volume created. Okay? Also everyone, if you go to

27:15

images, we also installed this image. Do you remember we talked about volume? We talked about

27:21

image. And that image you run on a container. So kind of your laptop, inside your laptop,

27:26

you create a small virtual machine where you are going to run this N8N host. Where you are going to

27:32

where you are going to host N8 and server on your local. That's why it is going to be

27:36

completely free of cost. You can use it any number of times. You can run it as many times as

27:42

you want, create any number of agents. It is going to be completely free. Okay. Let's try to do that.

27:47

Like, volume is already created in my laptop. Now, we will copy paste all these commands.

27:52

The only thing that you need to change is the time zone. How to get the time zone? If you remember,

27:56

we took the time zone of Kolkata, right? Asia slash Kolkata.

28:02

Just copy this value everyone and you just have to replace it.

28:05

Okay. So what you can do everyone is, just copy paste this command.

28:09

Feel free to do it parallel everyone. And if you want me to take a pause anywhere, do let me know.

28:16

Okay? Copy paste this and just change the time zone.

28:19

Go to time zone part. And this is the time zone, folks.

28:23

Remove this. Right? And copy paste this Asia, Kolkata. This value.

28:32

Okay. And there was one more place where we need to change. My Docker is not starting

28:40

and says WSL not installed. WS.S. Not installed. How did you try to install Docker?

28:51

Let me check what this error is all about.

29:02

Which operating system you are using, Sandhya? Is it Mac, Windows Windows.

29:20

Okay. Let me share this documentation with you. I think if you just follow this documentation, it should work. It should work. So the error is this usually happens on Windows desktop.

29:32

needs WSL to install before it runs Docker. Try running this command and restart.

29:40

Okay. Okay. Okay. So guys now our application is ready. Kishore, do you have any doubt? You have raised your hand? If yes, if yes, we'll feel free to ask. And guys, now, now I will pray to ask.

30:02

press enter now. And if you remember, if you don't have the image installed already, what,

30:08

what it will do? You are also getting the same error, Kishot? WSL not installed. Share which command?

30:18

This command? This is present on N8N documentation. Okay. Now if you see everyone, if you run this entire

30:29

command in your in your terminal, what it does is everyone, it actually downloads the image of

30:35

an A10. Now, if the image is not there in your laptop, it will download it, it will pull it,

30:40

and then it will install it. So if you're doing, if you're doing this activity for the very first time,

30:46

it is going to take few minutes of time, two to three, five minutes, three to five minutes of time

30:49

it is going to take. But if you have already installed it, if you remember in the last class, we did it,

30:54

and if you see everyone, it is already there. Okay, it is already there on port number five, six,

30:59

And the server is now ready. It is now running. Now what I can do is, I can go to this link.

31:09

Local host, colon, 5678 is a port number. And if you see, the N8N workspace is ready for me.

31:16

Can you see that, everyone? It is ready. Can all of you reach to this state? You need to use the bash

31:24

command to enable and configure WSL2 for the first run on Windows Docker desktop. Yes, I was not aware of this

31:29

because I have never installed in Windows actually. So, install WSL everyone. This is all the people

31:36

who are using Windows laptop. Then you can check the status using this command, WSL-h-hy-i-S-S-status.

31:42

And then, then, if it is, ideally, it should be running. That's it. I think, this is what you need to do.

31:59

Okay. Perfect. So guys, now, our N8N server is now ready. So what we will do now,

32:07

everyone, we will, sorry. What now we will do is we will create the first workflow.

32:15

Guys, should I give you two minutes of time to start the N8N local host? Because it is very important

32:20

to create the workflow parallelly. Because I will show you the commands, I will show you the way of

32:28

setting up the authentication today. And that is probably, that is easy, but it is confusing.

32:34

Right? There are a lot of steps involved, although we have to follow the documentation, but people get

32:39

stuck in that. Quite possible that I might also get stuck in that because there are a lot of steps.

32:43

We might end up forgetting steps. So please make sure that and those steps are very, very similar to

32:47

other accounts as well. I will give you the demo for Google account. There are going to be similar kind

32:53

of steps for other accounts as well. But if you understand one of them, like everyone, every other accounts

32:58

setup with N8N to give the permissions will be very straightforward for you. So please run the

33:02

command. How many if you have run it right now now? How many if you have the N8N running on local

33:08

host right now? Everyone? Tell me yes, no. Okay, there are two, three people, more people.

33:16

Say yes, no, if you are having the running instance of N8N ready with all of you.

33:22

Okay, just waiting for 30 seconds, one minute.

33:25

you need to be a bit quicker in today's class. We try to do it a bit faster so that we

33:34

don't wait for a lot of time. But I want all of you to do hands-on right away. If you remember when

33:41

we were writing a lot of code, I was not expecting you to write code in the same class right

33:46

away. Because coding is something that you understand first, then you can write it down later.

33:50

But this is something that is like a theoretical process, right? You have to follow certain steps.

33:55

Better if you can do right now.

33:58

Ideally, everyone, all of you should have downloaded Docker and installed the any time image over the weekend.

34:05

That is what I did in the last, that is what I said in the last class.

34:10

Restart the terminal, I think. Is it asking you to restart the entire laptop?

34:14

Entire machine. You might have to.

34:19

Okay?

34:19

Kare lo. It will take two minutes of time.

34:25

Should we start creating the workflow?

34:34

Okay. So guys, now, this is the first page that you will see on your home page of N8N. Okay, how many

34:40

if you're able to see this screen? How many of you are able to see this screen?

34:49

Click on Create Workflow. After click on, after you click on Create Workflow, you will be able

34:55

to see this kind of dashboard or this kind of sheet where you can basically this is the

34:59

working sheet where you can actually work on the workflow, right? So guys, you can give some name

35:03

to this workflow. Maybe let's say sample workflow for today's class, which is the date of the

35:11

today's class is, let's say, 8th of July. Okay. And then everyone, we will click on add first step.

35:18

What should be the first step in any workflow? Tell me. In any agentic AI workflow, in any auto

35:25

information workflow, what should be the first step? We discussed in the last class. Tell me.

35:34

Very good, Pratius, Pratush. Gathered details. What do you mean by that? Mokul, very good. Assume that we

35:41

already have the details. Form is not mandatory, right? Form is just one way of workflow. Correct? What if you

35:48

don't need a form? What if, let's say, you need to write an agent, let's say if I send you some email, right?

35:54

And you want to write an agent that that agent will read your email. And whenever you receive any

35:59

particular email, then it will do certain action. Correct. For example, let's say if you receive an email

36:04

from your manager, then you want to prioritize it. You want to set a reminder. You want to, let's say,

36:10

send a DM to you to yourself about the email so that you won't miss it. So in that case, form is not

36:16

required, right? Kishot? In that case, form is not required. Correct or not? Yes. So guys, you need a trigger.

36:22

Basically, the trigger is the starting point of the workflow, right?

36:28

Trigger is the starting point or starting node of your workflow. It can be a manual trigger. It can be an

36:34

automated trigger. It can be a webhook trigger that if you receive a payment from Razor Pay,

36:40

right? Let's say you are running some business on your website. As soon as a payment gets confirmed,

36:44

the workflow gets automatically triggered and it should make an entry in the table.

36:49

Correct? It should make an entry in the table or in your Google sheet.

36:52

that the payment has been received. Correct? The student details, the customer details and the

36:58

payment status. Simple workflow. So guys, you need to add a trigger first of all. Click on first

37:03

everyone and there are multiple type of triggers you have, right? First of all, always it will

37:07

recommend you because this is the first node that you're adding in your workflow. It is asking you to

37:12

add a trigger. What triggers the workflow? Can you see that? What triggers the workflow?

37:18

What triggers the workflow? First node is always going to be the trigger. It can be a manual trigger.

37:22

that if you click on execute, if you click on execute, if you click on execute

37:26

workflow, then only it will get triggered. It will not execute by default. It will not get triggered

37:30

by default. It will only get triggered if you click. Then everyone, on some event of the app,

37:34

right? Runs the flow when something happens in an app like Telegram, Notion, etc. On a schedule,

37:40

you can schedule a trigger that every day run at 9 a.m. in the morning. Do that. On a webbook call

37:45

and so on. So guys, I will click on on trigger manually. Is everyone clear? Let's say I want a

37:52

simple workflow initially where I want to create a workflow that I can execute manually. Can

37:57

you see that? There is an execute button here. Okay? Or everyone, we can do this or we can take a better

38:05

example. Let's say for example, in the last class also I showed you this thing on form submission.

38:10

Basically, you can create a trigger in which you are giving a form to the user and user will fill that

38:16

form. And what you want to trigger everyone is, like you will obviously you will like if a user detail,

38:22

If a user enters the details in the form, if a user fills the form, then you want to trigger some next steps.

38:29

For example, as simple as that if user is filling the form, then you want to create an entry in the sheet.

38:37

Makes sense, everyone? Let's say a feedback form. Okay? So for example, everyone, as of now, there is no authentication required, none.

38:45

Okay? Then form title. Let's say maybe everyone may be agentic or let's say maybe not agentic.

38:52

Let's say product feedback form. Same you can give in the description. Is everyone

39:01

able to follow me till now? I will give you two minutes of break, two minutes of pause after every

39:05

step so that you can also replicate the process. Okay. And here everyone, you can add some form elements,

39:10

just like we did in the last class. For example, you want to gather the email idea of the user.

39:14

And text input should be email. It will automatically validate the email like Pidentic, right? And

39:20

it is required field. You can enable the

39:22

required field. Then another element is, let's say, name, name of the user. Name can be the

39:28

text input. And then add attributes, name is also a required field. Okay. Then everyone, let's say you have

39:36

the next is, let's say, feedback or, yeah, feedback. Feedback may you can give, let's say,

39:41

maybe three values. You don't want any random input in the feedback. Let's say drop down. Drop down,

39:46

may, user can select one of the, one of the feedbacks, let's say positive, or maybe.

39:52

Okay, let's take a simple one. Positive feedback. Negative feedback. And let's say the

40:00

neutral feedback. Neutral feedback. Everyone clear? So these three values you have, name, email and

40:09

feedback. Is that clear to all of you? Is that clear to all of you? Now, can we add any other thing?

40:17

Maybe no, right? These three fields are good enough. And everyone, what we can do is respond

40:22

when form is submitted. As soon as the form is submitted, you will respond with something.

40:27

We'll see that. What can you respond with? Right? So you have created this form, everyone. And what

40:32

you can do is you can execute this step. As soon as you execute this step, this kind of form will be

40:36

visible to you. Let's say you can provide an email, Deepak Kasera 18 at the rate, gmail.com. And the name

40:41

is, let's say, Deepak and feedback is, let's say, positive. And click on submit. And as soon as you

40:46

submit the form, everyone, can you see that? You have got this data. Can you see that? You have got this

40:52

up. Correct? So name, email and feedback you have received in your agent, in your workflow.

41:00

So now what I can do everyone is, I can close this. And if you see the form is there, I can click on this

41:05

execute workflow. And whenever you execute the workflow, you will be able to see this form again and

41:09

again, right? So this is the first node which is ready for all of you. Is that point clear to all of you?

41:16

So first node is ready for all of you. Okay? So take one minute of time, create the node.

41:22

How many if you're creating it right now?

41:27

Create this node. Take 30 seconds of time, one minute of time.

41:31

It should not take more than one minute of time. Do this and let me know in the chat.

41:52

Done. Wait till 32.

42:22

Okay.

42:29

Okay, should we go to this node everyone. That what does this node, right? If you want to do that, right? If you want to do that, right, if you want to see that.

42:51

So double click on this node everyone and you will be able to see this kind of window, right?

42:55

That what are the fields of this, right?

42:58

What are the fields of this, what do you say?

43:02

This particular node, right?

43:04

Now, okay, fine. And you can see this data in different types. Fine.

43:10

Now, what do you want to do everyone is? You want to, as far as a response comes in,

43:15

in this node, as soon as any user fills the form, you want to create an.

43:21

entry in the Google sheets in your Google account. Correct or not? So guys, what you do

43:26

is you click on plus button here or you click on plus button here, does not matter. You can

43:31

select the next items. Clear or not? You can select the next items. What are the different options

43:36

you have for next item? You can build, you can add AI, like LLMs, right? You can, for example, if you

43:43

click on AI, you can add an AI agent, you can add like you can use different kind of LLMs, Anthropic, Gemini.

43:49

you can add guardrails like the restrictions, etc. You can have a support of Olama. You can add

43:55

open AI and whatnot. But for now, we will not go with LLM for now. We will come back to this. We will

44:00

add LLM as well. But also everyone, you can take some action, right? Do something in an app or service

44:06

like Google Sheets, Telegram, Notion. For example, let's say if you, if someone fills a form,

44:12

right? For example, let's say you are building an agent for sales team. And you have floated a form

44:17

for all the people on LinkedIn, for all the people who are interested in the course, they can fill

44:22

the form. Now, guys, don't you think as soon as some user fills the form, your sales team should

44:28

get notified about it. First of all, the entry should be created in the sheets, as well as your sales team

44:34

should get a instant notification in the Slack, in the Slack channel. That this user has filled,

44:39

these are the details. So please contact this user. Correct or not, everyone?

44:42

Folks, people are not doing, you guys are not doing parallelly. I'm not getting

44:51

enough responses. What happened? Very easy. If you have understood langchain, langraph, memory,

44:59

all these things, these are very easy things in comparison to that. It is nothing in comparison to those

45:03

things. Correct? Okay. Actions you can do. You can do some data transformation if you want to manipulate the data, filter the data,

45:12

convert the data, transform the data, you can do that. You can create flow diagram also,

45:16

like where the data should go. I'll talk about this flow in detail. This is also very important. You can

45:21

make HTTP request. For example, as soon as the user fills a form, let's say you want to make

45:27

a request to database to save the data. You want to make a request to the API to trigger something else,

45:34

right? So you can run some code. You can make HTTP request. Okay. Also, you can add a human in the loop.

45:41

Okay. If you, let's say if you're building an agent for refunds, right, you can add human review

45:47

that if the refund amount and also human review also, conditional human review, if the human, if the refund amount

45:54

is less than 500, let's say the human review is not required. Agent can take the decision

46:00

autonomously. But if the refund amount is more than 500, then human review is required. Correct, everyone.

46:07

If feedback, if the return amount is greater than something, then human review.

46:11

is required. We will do these things in the next class when we will build a complete,

46:15

when we are going to build a complete end-to-end workflow. For now, what we are going to do,

46:19

everyone is we are going to create an action in the app, and we are going to add Google Sheets.

46:24

Google. Search for Google Sheets. And, guys, you can say that. What I can do is I can create a

46:30

spreadsheet. Create a new spreadsheet. If you want, it can also create a new spreadsheet, but I'm

46:38

creating this new spreadsheet. Let's say, the name of the name of it.

46:41

the spreadsheet is customer feedback data. Okay. And guys, what all the columns we should have

46:48

in this spreadsheet? What data do we want to maintain in the spreadsheet? What data do we want to

46:54

maintain in the spreadsheet? Form data, right? So in the form data, right? So in the form,

47:01

what all the details we have? Email, name and feedback. The field name should be absolutely same.

47:09

So it is email, name and feedback. Take it as it is to avoid any discrepancies later.

47:17

Email, name, and feedback here. Clear?

47:26

Clear, folks? We have created the spreadsheet. Okay? Now what I can do is, see, it is very interesting now.

47:35

Now what I'll do is, I will again, I'll go to this action in the app, Google sheet.

47:39

Google Sheets. Okay. Now what I'll do is, what action do you want to do in this node? What this

47:47

node should do? Should it create a spreadsheet? Should it delete a spreadsheet? Should it append or

47:53

update a row? Yes, it should append a row. Right? Append row in a spreadsheet, right? Any one of them,

47:59

let's say append row in the spreadsheet. Correct? Now, what do you think what should be the next

48:04

action, action item here? You have selected the action. That what action you want to do in the

48:09

application. But what should be the next step now? What do you think? What action you should

48:16

add right now in this workflow? We need to connect the sheet. Absolutely correct. Very good.

48:26

So guys, as of now, is my N8N workflow connected with this link of the sheet, connected with this sheet

48:32

in my Google account? Is this connected? No, this is not connected. So what should we do everyone? If you see,

48:39

see sheet with document, okay, append row operation we want to do. Now we need to choose

48:47

the document, correct? But everyone now, what do you think? By default, will N8N be able to connect with

48:54

my Google sheet? If I don't share this link with all of you, if I don't give you the access,

48:59

I will have to provide the access to all of you, right? If I, I'll have to provide the access,

49:04

then only you can get the access. And even if I give this access to all of you, I can select what kind of

49:09

do you want? Only read access, comment, comment access or edit access? Correct or not? Correct? So

49:17

for that, everyone, what do you need? You need to give the credentials. Can you see that? Add your

49:22

credentials. You need to provide the authentication to Google. You need to provide the authentication to

49:27

N8N to access your Google account. Is this point clear to all of you? Most important step in building

49:32

workflows. Most important step. And this is going to be required, whether you connect chat GPT, whether you

49:39

connect Gemini, whether you connect maybe anthropic. The way of authentication can be different,

49:44

but this is what you need to do. Everyone clear till now? Okay. So guys, what you will do is

49:53

here, you will have to provide the access. So click on add credentials. Everyone is able to follow me till

49:59

now. Guys, this is the most confusing step of the entire journey if you are going to build automated

50:07

workflows. Using any platform, be it N8N, B8CrioAI, B8 Autogen, be it make.com,

50:15

all these platforms follows very much similar kind of steps for adding authentication. How many

50:22

if you are, how many if you have reached till this point of time? Do you want two minutes of time

50:27

to reach till this point of time? Because I don't want all of you to miss the steps. If you miss

50:32

the step, it is messed up. It will get completely messed up.

50:37

Take two minutes of time. Reach till this point of, till this page where you have to add the

50:44

credentials. To add the credentials, everyone, you just need two things. Client ID and client secret.

50:50

But how will you get it? That is tricky process. From Google. Google will give you a client ID. Google

50:55

will give you a client secret. Kind of you can say that, everyone, that N8N is going to act like a client

51:00

to Google. Can we say that? Because N8N is going to act, N8N is going to access your Google sheet.

51:06

So don't you think N8N is going to act like a client for Google? And N8N wants to access your

51:13

Google account? Yes or no everyone. So it is going to act like a client. Now, whenever you use

51:19

Google credentials, for example, even if you use Google login, if you log in, if you log in by Google on any

51:23

platform, for example, let's say if you go to Masai, although Masay does not provide that support,

51:27

but let's see if you go to LinkedIn. And LinkedIn pay, if you say login by Google, can I say that

51:32

LinkedIn wants to access your credentials on Google. So don't you think LinkedIn

51:36

acts as a client for Google to access your credentials. So LinkedIn becomes a Google client

51:42

for your account. Correct? Exactly what we need to configure here. Now, there is a good documentation

51:48

given here, but still people make mistake. So go to this documentation, everyone. And in this

51:54

documentation, you have to follow step by step. So what you want to do everyone is, this process,

51:58

when you give the excess of third part, when you give the access of any of your account to any third party,

52:04

this is done via Oauth2.

52:08

Oath2 is the protocol, is the authentication protocol on internet, which allows the access to a third

52:14

party account of another account. For example, I want to provide the access of my Google account

52:20

to N810. So don't you think N8N acts like a third party client for Google?

52:26

Google is the first party, I'm the second party. But I want to provide the access to third party

52:31

of my Google account. Who is the third party here?

52:33

any time. So this is Oath 2. Anyone knows the full form of Oath 2? Kishore, if you have any doubt,

52:39

you write it in the chart. What is the full form of Ooth 2? Open authentication. Okay. O means open.

52:48

Auth means authentication. And this is the second version of Oath, which is more secure, more reliable.

52:53

Okay? Great. Now go to this documentation, folks. And what you want to do is just scroll down and you have

52:59

to follow these five steps in order to provide.

53:03

access of your Google account to N810. Clear or not?

53:09

Clear or not? So let's follow the first step. Go to the first step. Okay. Now, guys, after every

53:15

step, I would recommend all of you to do this parallelly. First, create a Google Cloud Console project.

53:21

So basically, you have to create a project for N8N. Via that project, you will provide the access to

53:27

an ad. Okay. If you already have a project, jump to the next section. No, we don't have a project.

53:31

So what I will do is I will log in to my Google Cloud Console.

53:35

Click on this link, open this link in the new tab.

53:38

First of all, you have to log in here.

53:40

Am I already logged in to my account?

53:42

If you see, Deepak Kassera, 18 at the rate, Gmail.com, I am already logged there.

53:46

Correct or not? I am already logged in.

53:49

Okay.

53:50

What do you need to do after that is using your credentials, okay?

53:54

In the top menu, select the project drop down.

53:56

First of all, you need to create a project.

53:58

Guys, if you see, I already have some project, but what I will do,

54:01

is I will create a separate project for N8N.

54:03

I will not mess up with my original, with my other projects, right?

54:06

What I will do?

54:07

Click on new project and create a new project.

54:09

And let's call this project as N8N project.

54:13

Okay?

54:14

N8N project.

54:15

Clear?

54:16

Click on create and select this project now that you want to be present in this project.

54:21

It will take few seconds of time.

54:23

It is creating right now.

54:25

Now the project is ready.

54:26

Click on N8N project and please, please do, don't do this mistake.

54:31

this is why everyone I said in the beginning itself that this is why even after having

54:35

like even after having a good documentation people make mistakes because what do they do

54:39

they don't select the right project here unfortunately they miss it even I might miss it

54:43

sometime right please make sure that you are in the correct project okay clear or not

54:48

now what do you need to do after creating the project everyone enter the project name fine

54:53

created and the project is ready once your project is ready what do you need to do is

54:58

access your Google Cloud Console library, make sure you are in the correct

55:03

project.

55:03

It is also saying that make sure you are in the correct project.

55:06

Go to APIs and services and then library, okay?

55:09

So click on these three dots.

55:11

You will find API and services in this side menu and go to library.

55:18

Click on library, everyone.

55:19

We are in N8N project and this is the library.

55:22

Now, okay.

55:23

The next step is search for and select API.

55:28

you want to enable. Now tell me everyone, in this Google account, I have all the projects,

55:36

right? I have all the APIs. For example, Google Maps API, Google Maps API, then everyone

55:45

there is Gmail API, Google Sheets, Google Sheets, Google Doc, Google Drive, Google Images, and whatnot.

55:51

Google has hundreds of services, right? Now, I can provide the access to multiple things,

55:57

right? So guys, guys, tell me, does.

55:58

N8N needs my Google Images access.

56:02

Should I provide my Google Images access?

56:05

No, not required.

56:06

Should I provide my location access to N8M via Google Maps?

56:10

Not required.

56:11

What do you need?

56:12

You only need to provide the sheet access.

56:15

Google Sheets.

56:18

Press Enter.

56:19

And you will see Google Sheets API.

56:21

Click on this, everyone.

56:22

Very careful.

56:23

You need to be very careful.

56:24

Absolutely correct.

56:26

Then enable.

56:27

That in this project, in this project,

56:27

In this project, I want to enable this access.

56:31

I want to provide, I want to enable the access of Google Sheets API to this project as of now.

56:36

It will take a few seconds of time to get it enabled.

56:38

But, but, there is one catch here.

56:41

What is the catch, everyone?

56:42

It is written here also, everyone.

56:44

That if you see, search for APIs, for example, for Gmail node, search for Gmail API, fine.

56:50

Some integrations require other APIs as well.

56:53

For example, Google Sheet does not only need Google Sheets only.

56:57

It needs Google Sheets only.

56:57

Drive access also.

56:58

Why?

56:59

Because ultimately everyone, don't you think your Google Sheets gets stored in your Google Drive?

57:03

Correct.

57:04

So if you see Google Drive, it is specifically mentioned.

57:07

We are in Google.

57:09

If you see, we are in Google Sheets, right?

57:11

Google Ooth.

57:12

For example, yeah, it is written here.

57:14

Google Drive API is required.

57:16

Google Drive API is required for these things.

57:19

Google Docs, Sheets and Google Slides.

57:22

Don't you think even all these three things, Google Docs, Google Sheets, Google Drive,

57:26

Drive, Google Slides.

57:29

All these three things will get stored in your Google Drive.

57:33

So you need Google Drive access.

57:35

Yes or no?

57:37

People make this mistake also.

57:39

And, like, trust me, if you once miss it, it is

57:43

hell difficult to identify what is missing.

57:48

You might have to delete the project and start everything from scratch.

57:52

But it is extremely difficult to identify out of 50,

57:56

things, what is missing?

57:57

That's why it is very critical to provide all the access appropriately.

58:01

Right?

58:02

So guys, you need to provide Google Drive access also.

58:05

Okay.

58:06

Now again, everyone, go back, right?

58:08

Google Sheets is enabled now.

58:11

Go back and I will search for Drive.

58:14

Search for Drive, Google Drive API, okay?

58:17

And enable this as well.

58:19

Now let me see if any other thing is required.

58:22

Select enable, take it.

58:24

Any other thing is not required.

58:25

required. But maybe, for example, just to give you an idea, for example, let's say if you want to

58:31

provide Gmail access also, right? Gmail access also, go to library, search for Gmail,

58:38

press enter, Gmail API, you can provide the access. And guys, N8N will be able to read your emails

58:45

now. Isn't this interesting, folks? Isn't this interesting? Isn't this interesting?

58:53

Now, one very practical thing.

58:55

When you log in by Google on any platform, for example, LinkedIn, for example, on any other platform, do you see a consent screen that this application, let's say, LinkedIn, is trying to access your email ID, your location, your drive, etc, etc., then you can select what all the access you need to provide.

59:15

Okay? Today also you will be able to see the same screen.

59:18

Now, once you provide the access folks, what you can do is you can go to enabled APIs and services, the first option.

59:23

Let me zoom it a bit.

59:24

You can go to the first option and you can select what all the things you have given the access.

59:29

Gmail API is enabled. All these are my previous APIs. You don't have to worry about it. Gmail is

59:33

there, drive is there, sheet is there. All the three things are there. Okay? So guys, this enable part

59:38

is done. How many of you are clear till this point of time? We are going very slowly because it is very

59:43

confusing. How many of you are clear till this point of time?

59:51

Okay, done.

59:54

complete till this point of time. If you have the instance ready, do you want to complete

1:0:01

the first step? Or let me, a question, do this API access stay inside the respective project?

1:0:10

Yes, correct. Different projects go you can give different access. That's correct. So

1:0:16

guys, now, let me show you a second step also. Then you can do, and then we can take a break.

1:0:19

Okay. Access your Google Cloud console library. Make sure you are in the correct project.

1:0:24

Basically, what you have to do is, if you haven't used OAuth in your Google project as of now,

1:0:29

we have created a new project, so we have not used OAuth as of now in this project. You need to

1:0:34

configure the OAuth consent screen. Go to the consent screen. And on this consent screen, folks, what do you

1:0:39

need to do is, okay, this is just the documentation. What do you need to do is go to branding now. Go to your

1:0:44

project. We are in the correct project. And now, go to library somewhere.

1:0:54

Branding is where?

1:0:59

API console, go to menu auth platform branding.

1:1:03

Scroll down somewhere you see.

1:1:09

It must be written here.

1:1:19

Left navigation, go to API Services, Oath Consent screen, okay.

1:1:23

API services, OAuth consent screen. And here everyone, you will be able to see the branding page.

1:1:29

Okay? Now go to branding. Okay. Branding in branding once you go inside the branding, select

1:1:34

get started on the overview tab to begin configuring OAuth consent. So basically you are providing

1:1:39

the consent to this project now. As of now you have just provided the API access, that this project

1:1:44

can access this API. But as of now, you have not enabled the third party access via OAuth.

1:1:49

So you go to the consent screen and here,

1:1:53

Click on get started. This is the first time we are doing. Give the app name.

1:1:57

Whatever app name you want to give, let's say N8N project or N8N client.

1:2:01

This is the app name. You can give the support email. Prefer your email only. Click on next.

1:2:07

Now, what kind of audience you want to trigger? Internal, external. As of now, there is no internal,

1:2:13

like an organization, for example, let's say I have a domain at the rate, massey.com.

1:2:18

So guys, don't do you think? I just want to provide the OAuth consent to only the people with email ID

1:2:23

at the rate, masai.com, or at the rate, Google.com, at the rate, Microsoft.com.

1:2:27

As of now, do we have any domain? Do we have any organization? No. So I will go with external.

1:2:32

Right? So this is just used for testing purpose. External access, generally you don't give

1:2:37

as an organization. Obviously, if Masai has their internal project, they will not give you the access

1:2:43

or me, the access, right? Because that is their internal project. They will only provide the access

1:2:46

to the internal people. So we will go with external. Click on next. Email address. Again, give your

1:2:52

email address, Deepakasera, 18, ad the rate, gmail.com. Give the email access.

1:2:58

Agree, continue. Create. It will take few seconds of time and it will create a consent for you, right?

1:3:05

If you see everyone, for audience, select internal for user access within the organization,

1:3:09

external for any user with a Google account. It means that now this N8N server will be applicable,

1:3:15

will be used, can be used by any Google user. If you have Gmail account, you can do that.

1:3:22

Select the email address, done, continue, and create. Once you're, this is ready, you have

1:3:29

not, yeah, as of now, we have not configured, we have just created the consent. The next step everyone

1:3:34

is, what you need to do is, again go to the branding, again go to the branding, okay? And if you

1:3:40

see all the details, what you have filled here, you will be able to see. There is no logo of the app.

1:3:45

There is no app logo. Right? App domain. What is app logo everyone? Generally, you might have

1:3:51

seen that on LinkedIn, have you seen that if you try to log in by Google on LinkedIn,

1:3:57

the consent screen, the new pop-up window that opens up, there you can see the Google logo and the

1:4:02

LinkedIn logo. If you want to provide that logo, you can do that. As of now, it is not required. We

1:4:07

don't have any logo for now. Now, app domain. Do we have any domain? At the rate, LinkedIn.com,

1:4:12

at the rate, Microsoft.com, no, no domain. Right? So let's just follow this branding. In the authorized

1:4:18

domain, select add domain. Now tell me everyone, as of now, we don't have any domain. If you have

1:4:24

any domain registered on N8N, right? If you have any project running on N8N, then you can add

1:4:29

n8n. cloud. If you're self-hosting, then domain of your N8N instance. As of now, my N8N instance

1:4:36

is running where? As of now, this N8N workflow is running where? Where it is running for now?

1:4:44

It is running on local. And everyone, local may, if you are running this, do you see that, it is

1:4:48

giving you this URL. So you can copy this URL and you can give in the authorized domain,

1:4:56

authorized domain, add domain, and you can provide this. That I want to provide the access

1:5:01

to this local host server. Everyone clear? I want to provide the access to this local host server.

1:5:09

Guys, everyone is able to follow me right now. As of now, yes or no? Very step by step process.

1:5:18

must not specify authorized domain must not specify the scheme.

1:5:33

Where did I get the domain from? In your N8N page, this is the domain.

1:5:48

Okay, Pratisha, on your N8 page, this is the domain. Why this is not taking the domain? Add domain, paste. Strange. And then everyone, developer contact information is this. Why this is there? Earlier, this issue was not there. Let me check.

1:6:18

Let me check everyone. I'm checking on chat GPT that do we need to give the domain in a particular way, why it is not taking this value.

1:6:48

Thank you.

1:7:18

Okay. I think everyone we don't need this domain. Let me try. Yeah, but okay, let's, let's not give the authorize domain for you. Let me try. Yeah, but, okay, let's let's let's not give the authorized domain for now. Because it is not taking HTTP. No worries. Then what do we need is, is, if you're

1:7:48

posting at the domain of your N8N instance. I think it is local host 5678 only. It might be.

1:8:18

Okay, let's do one thing, everyone. Let me check this. How many if you are, how many if you were able to follow the steps till now?

1:8:25

Till the authorized domain. Read and accept the Google continue, create, left and manual branding, authorized domain,

1:8:32

select domain. If you're self-hosting, add the domain of your N8 instance, save, yes.

1:8:37

Okay, so yeah, so we have not made any changes. So we can, no changes made. Okay, let's go to the branding.

1:8:46

Overview may go to branding.

1:8:48

So any client is there. It's fine. So the next step is Google.

1:8:53

I think we can go to the next step. So let's take a break, everyone. All of you try to do till

1:8:57

this point of time. Okay? Okay. So let's take a break everyone. It's 9 p.m. just two minutes.

1:9:03

Let's take a break off. Maybe 10, 12 minutes. Try to reach till this point of time. Then we will

1:9:07

continue our discussion. Okay. See you after the break, everyone.

1:9:18

Yes.

1:9:48

I just got a response from chat GPT that if you are running N8N on your local, domain is not

1:9:54

required. Okay? Domain is not required. So we are done. So we are done with these two steps. The next

1:10:00

step that we are going to do after the break is configure your Oath consent screen. Okay. Sorry, this is

1:10:06

done. We will go to the next step. That is create your Google Oath client credential. This is technically

1:10:10

the last or last second step. That's it. Okay. We will do after the break. It's exact nine. Take a break of

1:10:15

maybe 12, 13 minutes. Try to do it right now. And then.

1:10:18

Then we'll meet after the break. See you after the break.

1:10:48

Thank you.

1:11:18

Thank you.

1:11:48

Thank you.

1:12:18

Thank you.

1:12:48

Thank you.

1:13:18

Thank you.

1:13:48

Thank you

1:14:18

Thank you

1:14:48

Thank you

1:15:18

Thank you

1:15:48

Thank you

1:16:18

Thank you

1:16:48

Thank you

1:17:18

Thank you

1:17:48

Thank you

1:18:18

Thank you

1:18:48

Thank you

1:19:18

Thank you

1:19:48

Thank you

1:23:48

Okay

1:24:18

so let me share my screen. Can everyone. Can everyone see my screen. Can everyone see my screen?

1:24:24

now. If the image is pulled,

1:24:29

so there you just need to execute the Docker command, image will be pulled and after that you will get the local host link.

1:24:34

Local host link. Local host 5, 6, 7, 7, 8 and your anytime instance is ready to run on local.

1:24:39

Okay, perfect.

1:24:40

So we are done with till this point of time, save button, our instance is done. Our instance is done. Our Google

1:24:46

Oath consent screen is ready. Now one thing that I'm repeating once again is that you don't need this domain

1:24:53

if you're running on local host. Okay? Perfect. Then the next step everyone is create your Google Oath client credentials. Almost the last time. We are very, very close now. Access your Google Cloud Console. Fine. Go to this. Go to APIs and services. Select credentials.

1:25:14

Fine. After selecting credentials, go to Oath client ID ID. Client ID. Create credentials.

1:25:23

Okay.

1:25:24

Create credentials. After going to create credentials, you will go to Oath client ID.

1:25:31

In the application type drop down, select web applications. Fine. Select web application.

1:25:37

Then you need to give the client name. Let's say if you're an 8.N client.

1:25:42

Anything, you can give any name here. Fine. Then Google automatically generates a name.

1:25:48

Fine. It is not generating the name for me.

1:25:51

or anyway, Google, uh, N810 client. And after giving the client everyone,

1:25:57

uh, fine, from your N810 credentials, copy the Oath redirect URL. This URL everyone that we

1:26:04

got, click on this, copy the URL, and copy the URL, uh, paste it into the authorized

1:26:11

redirect URL. So basically, this is the URL where Google will redirect you. Basically

1:26:15

the, uh, the, the, the consent screen that will open up, right? This is the URL for that. So, uh,

1:26:21

This is not the page. This is the page.

1:26:24

Right. Authorized, where we need to copy this, copy the Ooth direct from your N8, paste it

1:26:31

into the authorized redirect URL. Authorized redirect URI, paste this URL here and just click

1:26:37

on create. And you are done.

1:26:40

Right? Click on create. We are done. Almost we are done.

1:26:47

Oath client created. Client has been created everyone. So this is the client ID.

1:26:51

Obviously, I don't want to show this to all of you. This is something critical.

1:26:56

Anyways, after the class, I can delete the credentials. Now what we need to do, everyone is,

1:27:01

with the Google project and credentials, fully configured, finish the N8N credentials.

1:27:06

From Google, Oath, client created model, okay, what you need to do is copy the client ID, copy the

1:27:16

client ID, and go to your N8N, paste the client.

1:27:21

ID. Done. Everyone clear? Pasted the client ID. I'm hiding it for obvious reasons.

1:27:27

Client secret, go to this and put the client secret. Okay, everyone. Is this point clear to all of you

1:27:34

folks? Yes, no. Okay? Then client ID, client secret, sign in, then click on sign in by Google.

1:27:51

Click on.

1:28:05

Custom scopes are not required.

1:28:06

Click on.

1:28:09

Once you do this, everyone, you will get this kind of banner, sign in with Google.

1:28:13

Click on this.

1:28:14

And everyone, you will get this kind of screen.

1:28:16

Now tell me, everyone, whenever you log in by Google on any account, on any platform,

1:28:20

Do you get this kind of screen or not?

1:28:23

Do you get this kind of screen or not?

1:28:26

Yes? So almost we are done.

1:28:28

Click on the email ID, that which email you want to select.

1:28:31

You might have logged in with multiple emails of your Google account in your laptop.

1:28:36

So click on this.

1:28:39

Still, it is not there.

1:28:41

We are very close, but still it is saying XS blocked.

1:28:44

N&M client has not completed Google verification process.

1:28:47

The client has not created.

1:28:48

Google has done.

1:28:49

client has not created.

1:28:51

The only problem left is now.

1:28:53

Now, by the way, there is a complete video for it if you want to watch it.

1:28:57

The only thing everyone is that go to troubleshooting.

1:29:00

And here you will see that if your user type is external.

1:29:03

First of all, did we select the external user type or not?

1:29:07

Did we select the external user type or not?

1:29:09

There were two options, right?

1:29:10

Internal external, external means organization.

1:29:13

External means any user can log in.

1:29:15

Yes, we selected external.

1:29:16

Then you can add your email in the list.

1:29:19

of allowed things, right?

1:29:21

So what you can do is go to audience.

1:29:23

Go to audience page.

1:29:26

And you need to select the project for which project you want to do, N8NN project.

1:29:31

And here everyone, you need to add a test user.

1:29:35

That which user you want to provide the access?

1:29:37

Deepak Kassera, 18 at the rate, Gmail.com.

1:29:41

Okay.

1:29:41

Click on save, folks.

1:29:46

Click on save.

1:29:48

The user has been added.

1:29:49

And now what do you need to do is go to go back to your N8N screen and again click on.

1:29:55

Yeah, just close this.

1:29:57

Again, click on sign in with Google.

1:29:59

Do this.

1:30:01

Again, follow the process.

1:30:02

Click on the email.

1:30:04

And now it should be able to access via this email.

1:30:06

Can you see that everyone?

1:30:07

Now we are not getting access blocked.

1:30:09

Can you see that?

1:30:10

Now we are not getting access blocked error.

1:30:13

Correct?

1:30:14

Now it means that our N8N server is successfully able to connect.

1:30:19

with my Google account.

1:30:21

Now, click on Continue.

1:30:23

And everyone, can you see that?

1:30:25

Have you seen this kind of screen on multiple websites when you try to log in by Google?

1:30:30

What kind of concern do you want to provide?

1:30:32

What all the access it is asking for?

1:30:34

It is asking for Google Drive, like I can select all as well.

1:30:39

It is asking for Google Drive, Gmail, etc., and Google Sheets, right?

1:30:44

Click on Continue.

1:30:45

And now your configuration is ready.

1:30:48

Now, once your.

1:30:49

access is provided. Once you provide the access, the next step is, from the sheet,

1:30:54

you can actually access.

1:30:57

Okay. Ideally, it should represent all these things here.

1:31:00

So what you can do, everyone, is you can click on, uh, cancel this because it might take some time

1:31:06

to reload.

1:31:09

Double click on this again, append row.

1:31:12

And here everyone, from this, why it is not able to fetch the data.

1:31:19

No, no, actually, it should be able to fetch, actually.

1:31:29

It is searching, right?

1:31:31

Now, can you see that, everyone, all these sheets I have?

1:31:34

Correct?

1:31:34

Now it is able to access all my Google sheets.

1:31:37

Now, which sheet I want to provide the access?

1:31:39

I can provide the access as, I will only provide the access of customer feedback data.

1:31:44

Can you see that, folks?

1:31:46

Here it is not required, just from the list, document, I will select.

1:31:49

this. Just everyone now we are done. And now if you double click on this, now the data is,

1:31:55

now the sheet is selected. Is everyone clear? Folks, yes, no. Now this Google, this node, which is taking

1:32:06

an action on some event, it can access my Google sheet and it can append a row whenever the form

1:32:13

will be submitted. But can you see this error icon here?

1:32:19

sheet is required. Append sheet.

1:32:26

What is sheet 1?

1:32:30

Email, name, ad.

1:32:36

Customer feedback data from the name name from the name.

1:32:41

on list sheet one values that we want to send okay correct now we are very close to

1:32:52

this as a sheet one actually everyone the uh i forgot about it sorry this is sheet one now if you see

1:33:00

this is called a sheet one okay this is the entire document this is the feedback this is the sheet right

1:33:05

you can create multiple sheets inside one google spreadsheet right so you can give some name to it let's say

1:33:10

customer feedback then it will be more readable okay then everyone here you will be able to

1:33:17

see right if you close this and if you double click on this again then you will be able to see customer

1:33:23

feedback then you then it is better okay values that you want to send why it is not taking the feedback

1:33:30

name email why the feedback is not coming folks uh name and email is coming

1:33:40

yeah feedback is also coming right just click on refresh guys automatic also you can do but i

1:33:45

want to show you this as well you can select automatically also it will automatically map the columns

1:33:48

right but sometimes if the column is not visible you can just click on refresh button here you will

1:33:53

be able to see the refresh button can everyone understand till this point of time is everyone

1:33:57

understood till now now we have connected any time with my google sheet okay now here i need to provide

1:34:04

the id email value i need to provide the name value i need to provide the feedback value but where

1:34:09

these values should be coming from now this is also a very interesting step where these

1:34:15

values should be coming from from the form it means that can i say that for this google sheet node

1:34:23

the form form submission node should be uh should be added as an input that should be added as an input right

1:34:32

so as of now we have not done that right as of now these two nodes are not connected with each other so

1:34:36

so what you can do everyone is you can just you can just do this that now can i say that

1:34:43

now this form submission node basically the trigger node is acting like an input to this node can

1:34:49

you see that everyone now if you double click on this everyone here okay you execute the previous

1:34:55

node and that data will be visible here but everyone clear till now that we have connected these two

1:35:00

nodes as of now they were not connected right now the output of form submission node will be

1:35:06

acting like an input to the google sheets node okay then everyone you can give some better

1:35:10

name to this as well okay we'll do that what is happening okay yeah one more thing everyone that we need

1:35:24

to do is if you double click on the form submission can you see some data here can you see some data here

1:35:36

we fill the form right remember that we fill the form my email my name and some feedback

1:35:42

at the beginning of the class we fill the form but still the data is not visible because everyone

1:35:47

what happens is by default when you execute the step whatever data is coming here that is temporary data

1:35:52

you know let's say if you fill the form with deepak asera 18 at the rate gmail.com name is let's say

1:35:57

the perk and feedback is let's say positive take it now this data everyone comes temporary if you

1:36:03

close this you will be able to see this data but as soon as you close this

1:36:06

this data will not be this data is visible here but everyone what happens is if you refresh

1:36:11

this page this data is not permanent you have not saved it right so what you can do is for now it is

1:36:16

visible also if you want to test the data if you want to retain the data at least for the testing purpose

1:36:21

what you can do is double click on this and do you see this this pin data icon so that while working

1:36:28

on the workflow if you want to have some data already there you don't want to lose that data temporarily for

1:36:36

you can pin this and this data everyone will always be available for you okay so now everyone

1:36:41

if you see double click on this you will be able to see this data can i say that in the sheet now

1:36:45

for the email value i want this value i want name value and i want feedback value so guys should i

1:36:52

copy paste this value here that email may select this name may put the perk feedback may write positive

1:36:58

should we do this should we hard code these values should we hard code these values in the sheet no right

1:37:05

don't you think whatever value is coming from the previous node that is form submission

1:37:11

can i say that those values will be present here those values will be present here so can i say whatever

1:37:18

value is coming in the form coming via form that value should be present in the email that value should

1:37:24

go to the name and the feedback value should go to the feedback can we say that or not can we say that or not

1:37:30

So guys what you can do is you can drag and draw any 10 is very good in this case what

1:37:38

you can do is that i want the email value from the previous node from the form to be presented here

1:37:44

this is a simple javascript code that from this jason give me the email value and put it

1:37:50

inside the email column in the sheet then name value put it in the name column and feedback value put it in

1:37:57

the feedback column can all of you do this

1:38:00

Is everyone understood?

1:38:03

I don't want to hard code the value right.

1:38:05

I want to put the variables that whatever email value is coming from the previous step, put it in the email.

1:38:10

Whatever name value is coming from the previous step, put it in the name.

1:38:13

Whatever feedback value is coming from the previous step, put it in the feedback.

1:38:16

Is that point clear to all of you, everyone?

1:38:19

Is that point clear to all of you? Yes or no.

1:38:21

Now what I'll do is I will execute this step.

1:38:24

As of now, can you see any value here?

1:38:26

Deepak, my email, my name, my feedback.

1:38:29

Is this value there? No.

1:38:30

So let's say everyone, if I execute this step now, let's see what happens.

1:38:35

If you execute this step, it is executing the data and if you see everyone, this is the output,

1:38:40

this data has been written to the Google Sheets.

1:38:42

Can you see this data in the Google Sheet?

1:38:44

Automatically, can you see this data in the Google Sheet?

1:38:51

Correct?

1:38:52

It means that we have successfully connected our Google Sheet with N8N node and whatever operation we are doing in N8,

1:38:59

that data is.

1:39:00

is being transferred to Google Sheets successfully.

1:39:02

Let's do one thing, folks.

1:39:03

Let's execute the complete workflow, not individual step.

1:39:06

So what I will do is there is a button here individually on the bottom, execute workflow.

1:39:12

It will execute the complete workflow, all the notes, right?

1:39:14

Execute workflow.

1:39:15

It will execute workflow. It will first give you the form, right?

1:39:19

Form is not coming.

1:39:30

Okay, it is actually, sorry, it is actually creating the duplicate entries, right?

1:39:34

My bad, because currently this node is selected here, right?

1:39:38

So what do you want to do is click on this button here, execute a workflow.

1:39:44

Okay, got it. Why this is happening? Can you tell me?

1:39:50

That whenever I execute the workflow, whenever I execute the workflow, it is just creating a duplicate entry.

1:39:58

If you see, it will create one more entry.

1:40:00

Again, if I execute, it will again duplicate the entry.

1:40:04

But ideally what should happen everyone is if you execute the workflow, don't you think a new form

1:40:09

should be launched?

1:40:10

Users should enter the details and those details should be entered inside the, should be inserted in

1:40:14

the, should be appended in the Google Sheets, correct or not?

1:40:17

not the duplicate entries, right?

1:40:19

Not the cash values.

1:40:21

We did something just now.

1:40:23

Because of that, this is just putting the same value again and again.

1:40:27

We pinned the data.

1:40:29

If you double click on this.

1:40:30

You only think we have pinned this data and we can unpin this data.

1:40:34

And once you unpin this, see guys, if the data is already pinned, then it will not ask for the form

1:40:39

submission.

1:40:40

Now if you execute this, now if you execute the workflow, is it asking for the form or not?

1:40:46

Is it asking for the form or not?

1:40:48

Yes.

1:40:49

Now, let's say I will insert one more value, Neserg at the rate gmail.com.

1:40:55

Name is Nesarg.

1:40:58

feedback is, let's say, neutral.

1:41:00

Okay?

1:41:01

And click on submit.

1:41:02

As soon as you click on submit everyone, can you see that?

1:41:05

the roundabout, it is rotating around the Google sheet, the node.

1:41:11

As soon as the data goes, data flows from form submission to Google sheet, it will start executing.

1:41:16

And now you will be able to see, let's close this form.

1:41:19

Now you will be able to see this data inside the Google form.

1:41:23

Can you see that, folks?

1:41:24

Neserk, neutral feedback.

1:41:26

Again, let's execute the workflow.

1:41:28

So, again, it will start running.

1:41:31

And let's insert one more data.

1:41:32

Let's say maybe Guru Prith.

1:41:35

Guru Prit at the rate, gmail.com.

1:41:38

Name is Gurupreith.

1:41:40

Feedback is, let's say, positive.

1:41:42

Click on Submit.

1:41:43

Can you see that automatically the workflow is getting triggered?

1:41:47

And Google Sheet starts executing.

1:41:49

This node executes.

1:41:50

And if you see the tick mark, it means that data has been, basically the operation,

1:41:54

whatever operation you have configured in this node,

1:41:56

that operation has been triggered successfully.

1:41:58

and if we can see another value.

1:42:00

Can you see that everyone?

1:42:01

Yes, no.

1:42:03

So we have built a small workflow.

1:42:06

Guys, it's not about how big or how small workflow is.

1:42:09

It's only there.

1:42:10

We are only creating this workflow to understand basics of N8N.

1:42:14

How to create a node.

1:42:17

How to create the data.

1:42:18

How to get the data.

1:42:19

How to put that in the sheet.

1:42:20

How to add Oath credential.

1:42:22

That is more important.

1:42:24

Is everyone clear with this?

1:42:28

How many if you're clear?

1:42:31

Only two, three thumbs-ups are not enough.

1:42:38

How many of you're clear?

1:42:40

Do you want to take two minutes of time to try this maybe on your own?

1:42:44

Just two minutes of time.

1:42:46

Then I will go to the next step now.

1:42:48

Then we will add one more note.

1:42:58

Perfect.

1:43:02

I think we are good enough.

1:43:03

Now let's say everyone, you want to do some transformation on this data.

1:43:07

You want to maybe add some more information in the sheet based on the feedback.

1:43:11

Let's say if the feedback is positive, do this.

1:43:15

If the feedback is negative, do this.

1:43:17

If the feedback is neutral, do this.

1:43:20

Correct?

1:43:21

Correct or not?

1:43:21

Let's say you want to take some action on the data that is coming from the user based on the feedback.

1:43:27

And here.

1:43:28

we want to add conditional node.

1:43:30

Click on plus everyone.

1:43:31

Here also you can click on plus.

1:43:33

And here you will see that.

1:43:38

Flow.

1:43:39

If you see flow, branch, merge or loop, if you want to do any of these,

1:43:43

click on this and you will see if condition here.

1:43:46

If you click on if here, then everyone you can see these values, right?

1:43:50

Now you can actually, if you see the previous node, the latest data is this data, right?

1:43:54

Guru Prith.

1:43:55

What do you want to check everyone is, here you can put the if condition.

1:43:58

Correct.

1:43:59

Let's say I want to check the feedback.

1:44:01

If the feedback is equal to less than, greater than, etc., whatever values you can check,

1:44:06

if the feedback is equal to, let's say, positive, then you want to do this.

1:44:10

If the feedback is not positive, then you want to do something.

1:44:14

Everyone, clear?

1:44:15

Click on, just execute step.

1:44:18

Okay?

1:44:19

So if you see everyone here, feedback is positive and let's say close this.

1:44:23

Can you see a conditional loop here?

1:44:28

Yeah.

1:44:34

So can you see a conditional loop here?

1:44:38

That if you see chain, right?

1:44:39

In Langchain also we saw the same thing.

1:44:41

That data flows in a chain.

1:44:42

So formca data will go to sheet.

1:44:46

From the sheet, whatever data is being entered in every iteration, that one item, if you see one item,

1:44:52

we will pass to the next node.

1:44:53

Next node is if condition.

1:44:54

Now, if the condition is true, we want to do something.

1:44:57

If the condition is fine.

1:44:58

false, we want to do something.

1:44:59

What do you want to do if the condition is true?

1:45:01

For example, let's say if the condition is true, if the feedback is positive, let's say everyone,

1:45:05

we have some value, which is, let's say, send voucher.

1:45:12

Right?

1:45:13

If the feedback is positive, we want to send some voucher to the customer, else not.

1:45:17

So value will be, let's say, yes.

1:45:19

If the feedback is positive, we will say yes.

1:45:21

If the feedback is neutral, the value should be no.

1:45:24

If the feedback is positive, value should be yes, and so on.

1:45:27

Are you guys getting this value?

1:45:28

So this, this column, I want to, I want to enter manually.

1:45:34

I want to, not manually, based on the feedback value, I will check the feedback.

1:45:38

Basis on the feedback, I want to fill this value.

1:45:41

Can you see that?

1:45:42

Let's just give me a second.

1:45:42

Let me open the door.

1:45:58

Dear everyone, we want to fill the basis on some basis on some condition automatically.

1:46:28

I can add a simple node here? Can I say that everyone? If the item is true, what do you want

1:46:32

to do? Can I say that you want to take some action? On what action you want to take? Sheet action,

1:46:37

Google Sheet may. Go to Google Sheet and what do you want to do what? You want to do what? Append

1:46:44

a row, clear sheet, create sheet, delete sheet. On row added, triggers. Append or update a row.

1:46:58

Hmm. So what you want to do here is?

1:47:12

Append row, right? Upend or update row. Don't think even I were looking for the column, right? It is not

1:47:17

column operation. It is update row, right? So this row I want to update. What value in this row I want to update? What value in this row I want to update? The value of send voucher. Correct or not?

1:47:26

This is update row operation, not append operation. Update row. So append or update

1:47:32

row. And what do you want to do? Select the sheet, customer data, feedback data, select the sheet, customer

1:47:37

feedback, and map each manually. That is correct. So what do you want to do is, column to match on,

1:47:43

send voucher. So what do you want to do, everyone, is that using to match, not match actually.

1:47:51

Okay, just close this.

1:47:56

credential. Okay, okay, okay. So map.

1:48:03

Column to match on feedback, right? We want to match the feedback.

1:48:06

No, feedback already matched. And what I want to do is match.

1:48:11

Now, what value I want to send? Yes. Okay. So this is my positive part. Okay? So what I can do is

1:48:18

is, are you guys able to follow until this point of time or not? So what I will do is, I will do is, I will

1:48:26

So I will select this with, I will connect this with this, correct?

1:48:34

That in this, what we are doing is, I will put the value of, can you see that everyone?

1:48:41

I will send the value, yes. Can you see that?

1:48:44

Can you see that?

1:48:56

value yes to send voucher. In the yes case, correct? So I can just create a copy of this.

1:49:03

If you want small changes, you don't have to create the node from scratch. You can just create a copy

1:49:07

of this, create a duplicate, duplicate this. And in this everyone, what value do you want to send?

1:49:14

in the no case? Send voucher? No. Can you see that, folks? That. Now, with the false condition, you can

1:49:21

connect with this? Are you guys getting this point? What we are doing?

1:49:26

See what we are doing?

1:49:29

Submit the form, send the data to the Google sheet, append a row in the sheet.

1:49:33

Okay?

1:49:34

Once you append the row in the sheet, we will check the if condition.

1:49:37

What condition we are checking? If the feedback is positive, we will go in the true direction,

1:49:41

yes direction. If the feedback is negative, we will go in the no direction.

1:49:45

If the feedback is positive, we will send the value yes to send voucher of this column.

1:49:50

We will send the value yes. If the feedback is negative, if the feedback is not positive,

1:49:54

either neutral or negative, we will send.

1:49:56

the value no to the send voucher column. And that's it. We can just execute the workflow,

1:50:01

right? Now what I can do is I can just execute this flow because the previous value was

1:50:06

Guru Prith, right? Let's execute this workflow. We already know that the value is true. Feedback from

1:50:12

Grupreith was positive. Can you see that now? The value has automatically been filled. Okay, it is

1:50:17

not correct actually. Let's do this from scratch. For now, let's do one thing. This is yes by default.

1:50:22

because this data is already there, you are filling it manually, right?

1:50:26

Now let's enter one more value here. Let's execute the workflow from the beginning.

1:50:31

Execute the workflow. See, it is very interesting now. Just everyone focus on the flow as well.

1:50:38

As soon as I flow, as soon as we enter the value, you will see that what step is executing one by one.

1:50:43

You will also see that after the sheet, after the data has been inserted into the sheet,

1:50:48

you will go to one of these directions, right? Just focus on that color also.

1:50:52

For example, we have, let's say, Navdeep. Navdip at the rate, gmail.com. Name is Navdib.

1:50:59

Feedback is, let's say, negative. If the feedback is negative, see this. Executing Google,

1:51:05

data is getting inserted, taking time, why it is taking time.

1:51:18

Has the data been inserted? Maybe, guys, N8N is not a

1:51:22

able to reach to Google server. It might be taking some time. Because again, everyone,

1:51:25

it is running on local host. It might be not very up to the mark. Otherwise, we have to run it again.

1:51:33

Okay. Can you see that, folks? The green part. Once the data got inserted, if condition may,

1:51:39

you got false, because feedback is negative. And we executed this workflow. Can you see that? The green

1:51:45

color? This is not highlighted. This is highlighted. The positive arrow, the true arrow is not highlighted.

1:51:50

negative arrow or the false arrow is highlighted. And everyone, you can see that here.

1:51:55

For Navdi, the value is not filled. Why?

1:51:58

Execute to ho. Execute to ho. But the value is not getting executed. Why?

1:52:06

For Nafdib, map column manually.

1:52:13

Send voucher's value no.

1:52:17

Why it is not writing it?

1:52:20

using to match.

1:52:22

No, we are not using it to match, right?

1:52:24

Column to match on.

1:52:33

It is not inserting the value.

1:52:36

I think we are missing something.

1:52:38

Column to match.

1:52:40

Yeah, correct.

1:52:41

Column to match on email.

1:52:43

Absolutely.

1:52:44

This is what I was thinking.

1:52:45

In this case, the column to match is email.

1:52:50

Email. Email is used to match. And whatever data, we will send the value. Yes, absolutely. Thank you, Chinme. I made this mistake. So use this column email to match. And then send the value of yes here. And here also I will do the same thing. Column to match is on email and value is no. Okay. And then.

1:53:20

execute the workflow again.

1:53:28

For now, let's enter manually no. Let's execute this one more time.

1:53:34

Name is, let's say, Chinmet. At the rate, gmail.com.

1:53:43

Feedback is, let's say, positive. And data will be inserted in the sheet.

1:53:50

True condition execute.

1:53:52

Problem in node, append or row update, the column to match on parameter is required.

1:53:55

Absolutely correct.

1:53:56

Now there is one problem here because we have not provided the value here.

1:53:59

What to match with.

1:54:00

So I want to match with this value.

1:54:02

Okay, if the email is this, then I want to do this, right?

1:54:05

And here also, everyone, I will copy paste this and I will have to copy paste this here as well.

1:54:11

Okay, now we are done.

1:54:16

Now we are done.

1:54:17

So here also, the value will not be inserted.

1:54:19

Let's say yes, we are insert.

1:54:20

Manually. Now it will work absolutely fine. Okay. So now execute the workflow. We will insert

1:54:27

the data. For example, let's say Goro. Gorov at the rate gmail.com. Name is Goref. Feedback is

1:54:36

positive. Submit. It will insert the data. Go to the positive direction. And now if you see

1:54:43

everyone, workflow successfully executed. Correct? Now if you see here also there is a tick. And

1:54:48

for Goref, the value should be yes.

1:54:50

for send voucher column, ideally. Can you see that value automatically getting filled everyone?

1:54:55

Can you see that value automatically getting filled in the send voucher column? Let's test one more time.

1:55:02

And if you execute this one more time with, let's say, maybe one more student name.

1:55:10

Chirag. Chirag at the red g-g.com.

1:55:19

It is, let's say,

1:55:20

Now, neutral also, what should be the send voucher value? Yes or no? What should be the value

1:55:26

for send voucher? For neutral? We have two conditions only. If positive, yes, else, no. Okay? Execute

1:55:33

the workflow. Data will be filled. It will go to the no direction and data inserted successfully. Can you

1:55:40

see that for Chirag? Again, data got inserted successfully. This is our first workflow, everyone,

1:55:45

that we have just created with the help of Google Sheets. With the help of N8N.

1:55:50

Is everyone clear?

1:55:53

Is everyone clear? Yes or no?

1:56:05

That's it. This is what we wanted to discuss everyone. And in the next class, we will go a few steps ahead, not only one step. We will go two, three, four steps ahead, and we will build a end-to-to-end workflow workflow with multiple things, with LLM, with AI, with agent,

1:56:20

with some task, maybe some email reading, right? Basically, as of now, how we are triggering

1:56:26

the workflow? How we are triggering the workflow as of now? Manually, right? We are clicking on

1:56:31

this execute button. But this is not the real life case, right? In real life, workflow automation should

1:56:37

be done, should be triggered automatically, isn't it? The workflow automation should get triggered

1:56:42

automatically. We will do that. For example, if I receive an email from you, from a particular email

1:56:47

address or a particular type of email. Then my workflow should get triggered and then it takes

1:56:51

the data. Then it takes the flow. How many of you are 100% clear till now and how many if you

1:56:57

enjoyed the class? Everyone? Everyone enjoyed? Got it? Good. Okay. Awesome. Everyone.

1:57:07

So I will launch the feedback poll everyone. I hope all of you enjoyed the class as much as I did.

1:57:14

please do this practice on your own. Is the integration of N8N possible with LangChain and Langraph

1:57:20

absolute yes. See, Shivam, did you attend the last class? As Lang, so what Shivam is asking

1:57:26

is integration of N8N is possible with Langchain or Langraph as any time is no code. N8N is not no

1:57:33

code. N8N supports no code. But N8N supports code as well. If you click on plus here, if you want

1:57:40

to add, if you execute, if you want to execute some code, you can search here. You can write some

1:57:44

code as well. You can write code in Python, whatever code you want to write. It supports

1:57:48

coding as well. But major use case is non-coding. Okay. But that does not mean it does not support.

1:57:54

It supports coding. Okay. So if you see code in Python, that after this, you want to execute some code.

1:58:00

You can do that. Okay. Everyone? Okay, Shibam. Okay. So guys, I hope all of you enjoyed the class.

1:58:09

I'm launching the feedback poll. Please take the feedback poll and we are done.

1:58:14

so much for attending the class, folks. Have a good day. Take care. See you on Friday now.

1:58:20

See you on Friday, everyone. Thank you so much. Have a good day. Bye-bye. And good night.

1:58:24

Take care. Take care, everyone.

1:58:31

Thank you so much, sir. Thank you, everyone.

1:58:34

Good night. We'll have the next class on Friday.

1:58:44

So do you want to say anything? You can end the session?

1:58:46

No, no.

1:58:48

Feedback is going to.

1:58:49

Oh, I thought.

1:58:51

Okay.

1:58:52

Feedback pool, are we in progress.

1:58:54

Ah, okay. Okay. Okay.

1:58:57

Take.

1:59:03

Meanwhile, if anybody has any doubts, please field three to drop your doubts.

1:59:07

Please, we'll drop your doubts.

1:59:09

Yeah.

1:59:14

So I'm deleting these credentials for obvious reasons, because my credentials were visible on the screen, right? All of you can actually type those characters and have access to my Google account that definitely I do not want.

1:59:39

So delete it. Okay. Here, there is no all.

1:59:43

Here, there is no Oath client to access. And now, if you try to do this, now, if you try to execute the workflow, because now I have deleted the credentials, see what happens?

1:59:52

So let's say if I enter Somiya at the rate gmail.com.

2:0:02

Feedback is positive. Enter this. And if you see, workflow executed, oh, it is still.

2:0:13

Let's refresh this.

2:0:15

It should not be able to do so. Why?

2:0:18

Hmm.

2:0:20

Okay. So it is still able to use the credentials. Why?

2:0:36

So go to audience.

2:0:39

I don't know.

2:1:09

Okay.

2:1:39

need to delete it from somewhere else also.

2:1:47

This is challenging folks. If this is not happening, this is not happening, this is not good.

2:2:05

Client ID delete who then how it is then how it is able to access.

2:2:08

is strange.

2:2:38

Okay, it does still has the excess, right?

2:2:54

So disable.

2:2:57

If I disable this,

2:3:08

And I also disable the drive.

2:3:15

Now, so definitely it will not be able to access.

2:3:22

Disable.

2:3:38

Done. Okay, now I have disabled all the access and now I will try to do A at the rate gmail.com.

2:3:53

Name is A, feedback is let's say positive, submit. Now it is filling. Now can you see that everyone?

2:4:00

Forbidden. Check your credentials. Okay. Everyone clear. Now I have removed the excess that we gave.

2:4:08

Thank you so much. We can end the class now, Samia. Thank you so much for your support. Have a good day, everyone.

2:4:21

Thank you so much, sir. And yeah.