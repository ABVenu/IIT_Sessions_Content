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

Thank you.

14:10

Thank you.

14:40

Thank you

15:10

Thank you

15:40

Hi, everyone.

15:44

Hi, everyone, welcome to the session.

15:48

Good evening.

15:50

Hi, everyone.

15:52

Can you please make me co-host.

15:54

Hi, everyone.

15:55

Can you please make me co-host?

16:08

I have.

16:09

Okay, I cannot see the name of the students, that's why.

16:14

Okay, you have already done?

16:17

Okay, sure.

16:18

Yeah.

16:19

Okay, thank you.

16:20

We'll start in two, three minutes.

16:22

Sure.

16:39

Thank you.

17:09

Thank you.

17:39

Thank you.

18:09

Thank you.

18:39

Thank you

19:09

Thank you

19:39

Thank you

20:09

Thank you

20:39

Thank you

20:41

Thank

20:43

You

21:11

Hi everyone, very good evening.

21:28

Folks, am I audible to all of you?

21:33

Let me share my screen.

21:41

Can everyone see my screen, hear me, see me properly?

21:45

Link for the session we have already shared.

21:48

Let me share once again.

21:59

This is a link.

22:01

Okay, so very good evening and welcome to the class so we can get started.

22:07

So everyone, as of now, if you see, in the last class, we actually built a very small,

22:12

you can say that a starting agent or a small AI automation workflow.

22:18

That was not an agent, I guess, right?

22:20

Maybe you cannot call it as a completely agentic AI application because it was not doing

22:25

something autonomously.

22:26

The only action that we added in that workflow was that, that

22:31

based on the data given by the user, based on the feedback provided by the user,

22:35

we were just providing them whether we should give them a discount watcher or not or like

22:40

something, some discount or not, right?

22:42

So we were adding a new column.

22:43

So but that was not a complete full-fledged workflow.

22:47

Also, everyone, if you remember that, how we were triggering that workflow?

22:52

Basically, what was a trigger node?

22:55

Was that an automated workflow getting, was that an automatic trigger or that was a manual trigger?

23:01

That was kind of a manual trigger, right?

23:05

That you have to click on the execute button, then the form will come up, you enter the form,

23:10

you enter the form, you enter the retails in the form, then something will take place, right?

23:13

So that was a manual trigger, that was a manual trigger.

23:16

But in the real life folks, do we actually go with manual trigger?

23:21

Do we go with actually a manual trigger?

23:24

Answer is no, right?

23:25

So guys, today we are going to build an automated workflow which should get triggered automatically.

23:31

Okay, so today we are going to build a workflow which should get triggered automatically based on certain event.

23:37

Can you give me some of the examples like when an event or a workflow should get triggered?

23:42

Some examples.

23:44

Maybe any automation workflow you might have come across or you can think of some idea.

23:50

Tell me.

24:00

Can I say that?

24:01

Like the workflow might get triggered if you receive some email, if you receive, let's say,

24:05

if the latency is very high, if let's say the deployment fails, then automatically some steps

24:11

should be taken care.

24:13

Correct?

24:13

You should execute certain steps if some event happens.

24:17

When we receive an email for a meeting, it should be the, it should take the Zoom link.

24:21

Absolutely correct.

24:22

Very good example, Nisert.

24:23

So guys, we are going to build something similar that if I receive an email from a certain user,

24:29

like let's say, for example, if I receive an email from my manager.

24:31

then I need to execute some workflow.

24:34

Is the idea clear to all of you?

24:35

So we are going to build a completely full-fledged AI automation pipeline today with automatic trigger

24:41

as well as with the help of LLM.

24:44

Clear or not?

24:47

Is everyone clear?

24:48

Yes, no.

24:50

Okay.

24:51

So if this is the, if you see the local host, N8N where N8N locally is locally is running on my laptop.

24:58

So what we will do is we will add the first step.

25:00

Now, guys, just for today's class demo, what I have done is, let me show you, that I have

25:06

sent a sample email to myself.

25:12

Okay?

25:12

So this is a sample email that I just sent a few minutes ago before the class to myself.

25:17

And if you see everyone, in this email, we have some Python code.

25:20

Okay?

25:21

If you remember, this code is actually from one of our classes where we actually added the memory in Lankchain.

25:26

Remember that?

25:27

Agenic AI application with Lankchain memory, with memory.

25:30

Okay, just a sample code which we have already, which we wrote in one of the previous

25:34

classes, right?

25:36

And this is the email that has sent to myself, right?

25:38

If you see, this is the same email ID, right?

25:40

My own email ID.

25:42

Now, what I want to build is, what we want to build in today's class is that, for example, if I

25:47

receive an email from this email ID, right, that is my email ID, you can change the email

25:51

ID, obviously, if you receive an email from your manager, from client, from customer, from

25:56

user, from support team, from finance team, etc., etc., obviously.

26:00

So we are going to build a sample demo agentic AI application where if you receive an email

26:06

from this email ID, then you should trigger the workflow and maybe, let's say if I'm getting

26:13

this code in the email, then I want to summarize this code, right?

26:18

Otherwise, everyone, this code will be very, very difficult for me to understand.

26:20

This might be a very big code, right?

26:22

I will have to spend a lot of time in understanding the idea of this code.

26:26

So I want automatically the agentic AI workflow should get triggered.

26:30

It means that, everyone, that the agentic AI workflow should be able to read my email, correct or not?

26:37

It should be able to read my email, right?

26:40

And as soon as I receive an email from this email ID, automatically the workflow should get triggered,

26:45

correct?

26:46

folks, can we have more thumbs-ups, please?

26:49

I think only a couple of people are responding in the chat.

26:51

Can we have more people a bit more active in the class?

26:54

It will be very interesting class, trust me.

26:57

Okay?

26:58

Yeah.

26:58

So, guys, first of all, the agentic AI work.

27:00

should be able to monitor your email and it should keep on checking continuously that do we have a new email,

27:06

do we have a new email, do we have a new email from this email ID?

27:08

If there is a new email from this email ID, then it should be able to read that email and maybe,

27:14

let's say if there is a code, if there is some Python code in that email ID, then I want to summarize that code.

27:19

Also, I want to add some comments in the code, clear or not everyone?

27:23

Let's say, for example, I just want to summarize the code, that's it.

27:25

I just want to summarize the code.

27:28

Clear, this is what we want to build.

27:30

Okay?

27:30

everyone, yes, no?

27:32

Okay.

27:33

So everyone now, first of all, tell me what should we do.

27:35

Now, guys, always you should do what?

27:37

Whenever you have to build a workflow, don't directly start, don't directly jump on building

27:41

the workflow.

27:42

Always do one thing, everyone, prepare a proper documentation.

27:45

So what you can do is either you can create a proper, you can say that, a Google Doc, where you can

27:51

write all the requirements that what you are going to build.

27:53

Or if you want to do that in the local host, in the N8 itself, it provides you,

28:00

sticky notes. Can you see the sticky notes, folks? Can you see the sticky notes?

28:06

So this sticky note is nothing but kind of a small documentation that you can actually use,

28:11

that what you are actually building here, so that everyone, you don't forget, or you don't miss something.

28:16

So it is always very good practice to start your project, to start your workflow, whatever work

28:22

you are doing with a small documentation, clear or not? So let's say everyone, and this is a markdown

28:28

file, right? So you can say that.

28:30

Let's say this is an agent, automated agent workflow.

28:43

Right?

28:44

So what it should do everyone is, let's say the first step, right?

28:46

That agent should be monitoring the Gmail application.

28:55

And once there is an email, once there is, once we receive an email,

29:00

email, from a particular email ID, the workflow the workflow should get triggered.

29:17

Is that point clear to all of you? Is the first point clear? And these are the steps.

29:24

Okay? The first step is clear to all of you, folks. Sorry. Okay. Okay. Okay.

29:30

So now this is the first step. And once everyone, the agent should, once the trigger happens, right? Once the agent, the workflow starts, what should we do? Right? So agent should be able to, agent should call an LLM API. Any LLM API, whether GPD, Anthropic, Gemini, whatever, agent should call an LLM API to provide

30:00

summary of the code and maybe add, let's say, summary of the code.

30:07

Okay?

30:08

Summary of the code.

30:10

Correct?

30:11

Now everyone, once you generate the summary with the help of LLM, what should we do then?

30:16

Agent will read your email.

30:19

It will get the code from the email.

30:21

Then it will send the code to the LLM to generate the summary.

30:24

Once the summary is ready in the agent, what should we do?

30:30

We should send the summary as an email, right?

30:37

Send the summary to the user in email.

30:43

Is that one clear to all of you?

30:44

This is what we want to build, folks.

30:47

Can you see that?

30:48

Make it a bit smaller.

30:50

And this is everyone.

30:51

We will keep on referring this throughout the class.

30:55

Okay?

30:58

Okay.

30:58

Okay.

30:58

Everyone clear with the small idea.

31:00

that what we are going to build today.

31:03

Okay?

31:04

Perfect.

31:05

Then we will add a couple of more functionalities towards the end once we are ready with this.

31:09

So what is the first thing, everyone, that we should take care of?

31:12

What is the first step that we should take care of?

31:23

I think on Friday evening, this looks a bit weird, right?

31:26

That's what I'm drinking.

31:29

Right?

31:30

because of like the color.

31:35

Don't worry, everyone.

31:36

This is not something else.

31:37

This is just green tea.

31:38

Okay?

31:38

I'm in a hotel, so I don't have the cup, actually.

31:41

I forgot to ask them the cup.

31:43

But yeah, this is just the glass of green tea.

31:48

Yeah.

31:49

Okay.

31:49

What is the first step?

31:50

What is the first step we should take care of?

31:54

What is the first thing we should do?

31:56

Guys, you have to help me today.

31:58

We have already seen all the things, right?

32:00

In the last class.

32:00

We just have to build on top of that.

32:03

First, we should add a trigger.

32:05

Now, what should be the trigger everyone here?

32:07

Trigger should be the Gmail API, right?

32:10

That something should be like some node that should automatically get triggered when we receive an email.

32:17

Can we say that, folks?

32:20

Can we say that or not?

32:27

Correct.

32:28

Now, click on plus.

32:30

Trigger. Now, everyone, inside the trigger, we can have, we can have, yeah, on app event.

32:39

And here we can search for Gmail, right? Yeah. Gmail may, if you search on message received,

32:44

can you see this event, everyone? That trigger, execute the trigger on message received.

32:51

Can we select this, everyone? Can we select this? Yes, I think this is good for our use case.

32:56

Select this. Now, everyone, if you want to allow.

33:00

this agent, this workflow, to read emails from your email ID, from Gmail, will you have to

33:08

provide the access to your Gmail account?

33:11

Will you have to provide the access to your Gmail account? Obviously, yes, right?

33:15

So if you see everyone, as of now, we don't have credentials. On Wednesday, did we set the credentials?

33:21

Yes, right? We saw all the steps. How can we set up the Google credentials? But everyone, at the end

33:26

of the class, if you remember, I deleted those credentials because those credentials were now public.

33:30

For obvious reasons, I had to delete those credentials, because you can watch the recording

33:35

and type. Those were not very random, not very big, right?

33:38

So now we will set up the credentials once again. It will not take a lot of time because we have

33:42

already done that just one day back. Okay? So we will go to set up credentials, everyone. All of you

33:46

remember that, after setting up the credentials, we get client ID and client secret. Correct?

33:51

So we will go to the documentation, folks, read our documentation, go to that. And we will do all

33:56

the steps one by one. And it will be a good revision for all of you, right? So let's say, everyone,

34:00

we want to provide, yeah, we want to, like for any Google set up, Google credentials setup,

34:08

can you show this step again? How did you get the email trigger? Email trigger? Email trigger

34:12

you just have to do what? Close this, close this, click on plus, go to triggers. Okay, there is one

34:20

thing. Let's delete this for now. Click on plus. Now, first you have to add the trigger on app event.

34:26

Go inside on app event. Search for Gmail. And I think you can search.

34:30

from here only. If you search here, you get to Gmail, and here you can select on message

34:35

received. You will reach here, then we will click on set up credentials. Now everyone, we will

34:40

go to the documentation and we will follow these documentation one by one very quickly. We have

34:44

already done that yesterday, day before yesterday, right? Go to Google Cloud Console. Either I can

34:49

use the same project, folks. I'm already logged in. I can use the same project, but I will show you from

34:54

the scratch, right? That how to, even if you don't remember the steps from the last class, we will create

34:58

it from scratch. So let's say everyone, N810 test application. Give the name, N810 test,

35:04

no organization, done. Create a new project. After creating the project, everyone, then project name

35:10

and create. Now, once you create the project, go inside test project, the project that we have

35:15

just created, N810 test. Once you are inside the project, everyone, go to APIs and services,

35:20

then library. Click on these three bars on the left, top left corner. Go to API and services. Close all

35:28

apps, API and services, and library. Go to library. After you go to library, everyone,

35:33

you have to select what all the access you want to provide to this project. So let's say everyone,

35:39

we want to provide the Gmail access. Search for Gmail. Gmail. Gmail API, provide the access.

35:45

For now, I think we just need Gmail. And maybe just for the, just to be on the safer side,

35:49

we can provide the sheet access because we might need it. But for now, Gmail is good enough.

35:55

Provide the Gmail access. It will take few seconds of time.

35:58

Okay? Then go to library once again search for Drive. Google Drive API.

36:07

Enable this as well. Done. Again, it will take few seconds of time.

36:28

Google Sheets and again enable. Okay. Again, everyone, we have provided three accesses here,

36:33

Google Sheets, Google Drive and Google Gmail API, right? Done. Once you are done with this folks,

36:37

then what will you do is you will select enable, enable all of them. Then we have to configure

36:43

Oath consent screen. Fine. Access your library, go to library. Click on this link, folks, go to the library.

36:50

And once you go to the library, what you'll have to do is make sure you are in the correct project,

36:55

fine. Open the left navigation, go to Oath consent screen. Again,

36:58

go to this, go to this and Oath consent screen. Once you go to Oath consent screen,

37:07

Google will redirect you to the Oath platform. Click on get started on the overview.

37:15

Get started. Fine. Here you just have to enter the app name. Let's say N810 test. This is the app

37:20

name. Email ID. I will enter my email ID. Click on next. Externally user, click on next. Again, email

37:27

email ID, deep upka say right in at the rate, Gmail.com, click on next, finish and

37:37

continue. Click on create. Okay. Internal access, internal is for only for organization. We are not

37:43

an organization. I selected external. Selected this, provided the email ID, accept terms and

37:50

conditions, select continue. In the left-hand side, now we have to go to branding. Okay. Now the next thing,

37:57

is we have to go to branding. In the branding, folks, what we have to give is, after you have

38:02

gone, you have set up the Oath consent screen, this is done now. After that, you have to provide

38:08

the authorized domain. If your N8N is running on cloud, you have to do this. Otherwise, you have to

38:14

give your hosting link. But everyone, are we hosting our N8N project on any domain? Any external

38:20

domain, are we hosting that? No. So it is running on your local instance. If it is running on your

38:24

local instance, this authorized domain is not required. So you don't have to do any thing

38:29

in this step. So this step is not required if you are running N8N on your local. Clear,

38:34

everyone? Clear folks? Okay. Then everyone, create your Google Oath client credential. This is the

38:42

last step. Access your cloud console. Go to cloud console once again. Select the project. Make

38:46

sure you are in the correct project, N8N test. Fine. Go to services and go to credentials. Go to

38:51

APIs and services, go to credentials now. Once you go to the credentials, everyone,

38:56

in the application type, select the web application. Application type may. Now you have to

39:01

go to create credentials. Now you have to select on Oath client ID. Go to client ID. And once

39:08

you go to the client ID, you have to select the web application because of web, because our application

39:12

is web application. You can give whatever name you want, let's say, NA10, client, one. Whatever name you

39:18

want does not matter. And now, now.

39:21

Now the last thing everyone that you need to give is, name is fine. You have to give

39:26

the Oath redirect URL, right? Basically the URL of the top-up window, the pop-up window

39:32

that opens up when you click on login by Google or authorized by Google, right? So you

39:37

have to go here and click on this link, copy this link, folks, and provide this link in authorized

39:42

redirect URI. Provide this link here and click on create. So after you give this everyone,

39:48

from your N-8-10 credential, copy the O-O-O-O-O-O-R-R-R-R-R-I.

39:51

URL. Oath redirect URL, done. Copy this and paste it into the authorized redirect

39:58

redirect URL and click on create. Click on create. Done. Once you do this, everyone,

40:03

now your client credentials are ready. So what I will do, folks, I will, if you see this is the

40:07

client ID, this is the secret key. So I will copy the client ID. I will give the client ID here, fine.

40:13

Then I will copy the secret key, client secret. I will copy this client secret and paste it here.

40:19

After that, folks, you will see that once you provide client ID and client secret, automatically

40:23

this kind of banner will come in front of you, sign in with Google.

40:27

Okay?

40:28

Click on sign in with Google.

40:29

This kind of screen will come up.

40:31

Select the ID, select the email ID with which you want to log in.

40:34

But excess is blocked.

40:36

We got this error yesterday also, in the last class also.

40:39

How did we resolve this error?

40:41

Can some of you recall?

40:48

Can you recall this?

40:49

We got this error last time also.

40:54

How did we resolve this error?

41:00

Adding the email, absolutely correct.

41:01

Absolutely correct.

41:02

Guys, you don't have to remember this.

41:03

I'm just, I was just, I just wanted to think, I just wanted all of you to think that what error did we get and how did we resolve it.

41:11

But if you go to troubleshooting, right, this is the second point.

41:13

It is already there.

41:14

That what kind of because your user type is external, you can add your email ID in the list of test.

41:19

us. Okay? So you go to your audience, click on that link. And in the audience link in your

41:26

project, obviously you have to select your project, N8N test. And you have to add the email,

41:32

add users, and provide the email. Deepak, Kassera, 18, add the rates, email. Okay. Done.

41:39

Once you save this everyone. And now go back to your N8N credential.

41:46

Close this tab. Click on sign in with Google.

41:49

Once again, select the email. Now it will ask to continue. Now it will ask what all the excess

41:56

you want to give. Let's say I want to give all the access. Right. So guys, if you see, this is

42:02

very important thing to understand, right? Can you see that? Because we are providing the Gmail

42:07

access, if you see, you are providing read, compose, send and permanently delete all your email

42:12

from Gmail. It means that this access gives the privilege of reading the email, updating the email.

42:19

deleting the email. It can manage drafts also, send emails also. It can view email

42:23

messages when you interact with add-on and so on. A lot of excesses we are giving. And once you

42:29

select all of them for folks, you just click on continue. And now your credential is set up. Now,

42:34

everyone, once you go to this screen now, now let's again come back to our discussion. What I will do,

42:40

I will delete this node now. And I will click on this plus again. I will select for Gmail once

42:45

again, click on Gmail, on message received. Now can you see that if you want.

42:49

already the credentials are there. Earlier, if you remember, just 10 minutes back, here it was

42:54

mentioned no credentials present. Can you see that? Here, everyone, if you see Gmail account

42:58

credentials are present, right? Everyone clear with the setup of credentials. I think now it should

43:04

be crystal clear to all of you. We have done this two, three times now. At least a couple of times

43:08

we have done. Okay? Google Killate is slightly tricky, everyone. For other applications, I will show

43:14

you today for chat, GPT also. For GPD also, it is very straightforward. You just have to copy paste

43:18

the API key, the secret key. Okay. Now everyone tell me, once you have this node and you have provided

43:25

the access to read your email, you have provided the access to read your email, can I say that now

43:31

you have to set up the frequency also, right? Basically, if you see the pole time, poll,

43:35

poll meantl, frequency that at what interval, this node will keep on polling your Gmail to read

43:43

the email, correct? So guys, you can set up the frequency that do you want to read every minute, every hour,

43:48

every day, every week, every month, every X, like, you can select the frequency and custom.

43:53

Can you see that, folks? Let's say I want to check every hour. Every minute will be very fast,

43:58

right? Guys, unnecessarily you have, if you see it every month now. Let's say if there is every minute

44:02

you are selecting. Or let's see if there is a option of every second also. Guys, don't you think

44:07

you, if you're checking, if your agent is making a API call to the Gmail server to check about

44:13

the email every second, don't you think it will make, don't you think it will make too many network

44:17

calls and it will increase the load on your agent, it will make too many network calls, right?

44:23

So that's why always be very, very cautious about what frequency you are selecting.

44:27

For now, let's say we are selecting every hour, okay? Every hour or let's say maybe every minute,

44:31

fine. For now, we don't have to worry about that a lot. Now, what event you want to check?

44:36

Message received. Okay, this is what we have selected. Simplifyco, you can put it off and

44:42

max emails per poll, maybe let's say 100. Okay? How many emails you can,

44:47

read per poll, right? When you are, when your agent is making a call, how many maximum

44:53

emails it can read? We can set it up 10, we can set it up 5, we can set it up 20. It does not matter.

44:58

For now, we are just going to test with one single email. So for now, let's say 10 is okay. Now everyone,

45:02

this is also very important that. Now, on what basis you want to read the email? Does it read all

45:08

the emails? Should my agent read all the emails from my Gmail account? No, right? It should read the

45:14

email only from my email ID. Right? So you can say that sender. So you can put the sender here.

45:20

That sender should be Deepak Casera at the rate 18, uh, Deepak Casera 18 at the rate gmail.com.

45:25

That please read the email from this sender. Can you see that everyone?

45:33

10 different emails. What do you mean by one thread?

45:39

10 different emails. Okay. 10 different emails. I got, uh, I got the thread.

45:44

Now see what this agent will do. It will check with your Gmail API. It will make a call to your

45:51

Gmail API, Gmail account every minute. And if there is a message, if there is a message received

45:58

from this sender, from this user, then this node will get triggered. Clear? Is this node clear to all

46:05

of you? Is this node clear to all of you? Is this node clear to all of you? That this, we have provided. We have

46:14

is the Gmail access? It will check every minute. If there is a message received from this email

46:19

ID, this node will get triggered automatically. Now everyone, just to test, let's click on fetch,

46:23

fetch test event. Click on this everyone. Let's see whether it is able to fetch or not. Can you see

46:28

that folks, that it has, it is able to fetch actually the latest email from my Gmail account. Can you

46:35

see that or not? That email ID, like, like what do you say, the unique idea about the email, the thread ID,

46:42

right? Then everyone, if you see, size estimate, header, this email I just sent before the class

46:48

at 7.52 p.m. Some message ID is there. Subject Python code. Can you see that? Subject is Python code. And

46:55

the subject is Python code only. Can you see that everyone? Then everyone, there is a code here. Right? This is

47:01

from my email ID to my email ID. Then can you see the code here? From land chain, open AI, import,

47:08

chat, open AI, then line break, from land chain, core. So basically it is able to

47:12

read the email. Can you see that anyone? If you see all the code is available here, it means that now

47:17

we are successfully able to read the email from our Gmail account. Yes or no? Would you like to try till

47:25

this point of time? Because if you, like if I cover two more things, then you might end up forgetting this.

47:31

Do you want to take five minutes of time? This is not a break. Don't consider this as a break. Do you want

47:36

to take four, five minutes of time and reach till this state? How many if you're doing parallelly with me?

47:42

How many of you are doing parallelly right now?

47:45

Guys, yes, no.

47:57

Okay, some people are doing good.

47:59

Take three, four or maybe five minutes of time.

48:02

Reach till this point of time.

48:03

If you get stuck at any point of time, do let me know.

48:06

Okay, set up the credentials, give the Gmail access, see whether you are able to read the email or not.

48:10

Okay?

48:11

Done everyone.

48:12

Or, thumbs up. I'm here only. This is not a break.

48:15

Please let me know if you get any, if you get in it out or if you get stuck at any point of time.

48:20

Okay? Then we will move to the next step. Now we will add the LLM here.

48:42

Thank you.

49:12

Thank you.

49:42

Thank you.

50:12

Full content is not coming. Only snippet is coming. What do you mean by? Like I'm not getting. I'm not getting.

50:23

What exactly snippet is? Ideally, all these things should come, right? Sender, receiver,

50:29

timestamp, value, text, everything should come. If you see, actually, the content is in the text

50:35

column. Can you try to do it from scratch? Ideally, it should not happen, actually.

50:48

Maybe try to do it from scratch. I was not able to download WSL2 because of storage issues. Can't upgrade

50:54

storage either. Planning to buy a new machine soon. I'll be trying this. No worries, no worries, Pila. That's

50:58

fine. Perfectly fine. Okay. Take two more minutes even. I think people are trying. Very good. Just

51:05

one or two more minutes, then we'll get started. Okay? Then we will move to the next step now.

51:35

Thank you.

52:05

Okay, so how many of you are able to reach till this point of time, till this stage in your agent workflow?

52:24

At least few people. Should we go to the next step now?

52:30

Okay, very good. Very good, everyone. Keep it up. Let's go to the next step now.

52:33

Once your workflow is ready.

52:35

and guys, can we pin this for now? Because this particular thing we are going to use

52:40

for testing, right? So we can pin this data so that we don't have to read it again and again,

52:44

right? We can pin this data, right? And this is the first workflow. This is the first node that we are,

52:50

that is ready for us. Can you see that everyone? This is the first node that is ready for us, which is

52:55

the Gmail node. After this, what should we do? After this, what should we do? Once you have the data, once you

53:04

have the code ready. What should we do now? Connect to LLM? Absolutely correct. Now what should we do everyone is? We should add the LLM support here. We should add the LLM support here that this code, whatever we are getting from the Gmail, this code we should pass it to the

53:34

we should pass it to the LLM and give some prompt that this is the code. Please summarize this

53:40

code. What we are doing is we are writing, we are actually trying to summarize the code, right? Can you see that? We are trying to summarize the code.

53:47

Correct? So pass this code to the LLM and then ask to summarize. So click on plus everyone. Now we will click on

53:55

AI and now folks what we will do is we will do what? Actually what we will do is

54:04

flow. Yeah. So guys, we will select basic LLM chain. Okay. And this LLM

54:15

LLM chain basically like a chain, right, right? That you give the prompt, you give the input,

54:19

you get the data back. That's it. Right? Basic LLM chain, everyone. And actually, just give me a second.

54:24

And overflow action A.I. Not AI templates. Yeah. This is what I was talking about. Basic LLM chain. A simple chain to prompt a large language model. Simple. Click on this everyone. And here we can do what? There are two options you have. Right? First is everyone. Connected chat trigger node.

54:54

Connected chat trigger node, right? What is this? Looks for an input field called chat input,

55:02

that is coming from a directly connected chat trigger. Define below. Use an expression to reference data in the previous nodes or enter static text.

55:11

So guys, what do you think? As per your understanding, should we use the connected chat trigger node or define below?

55:16

What use can? Maybe try to guess.

55:20

Try to give it a guess. What will?

55:24

Should we provide the chat input or should we connect this? Do we want to connect this with the previous node?

55:31

Define below? Absolutely correct. Very good everyone. We will connect, we want to connect this node with the previous node and the data from the previous node will be coming as an input to this node. So we will use defined below. Define below. And here everyone, we will provide the user message. What is the user message? Okay, here here? It is already written. This is nothing but prompt. Correct, everyone? This is nothing but prompt. Now, what do we do is?

55:54

Let's try to connect this with the previous node.

55:58

Okay? Actually, there is no previous node. So what we will do is we will connect this node first of all.

56:04

Basic LLM chain now. So what we're doing, this to delete.

56:08

Arre, why there are two chains here? Okay, there is a confusion. Let's do one thing. Let's select basic LLM chain once again.

56:15

Go to AI, select basic LLM chain here. Select this, right?

56:24

Basic LLM chain.

56:28

And what we will do, everyone, is we will connect this node with this node.

56:32

Can you see that, everyone?

56:34

Now what we will do is, can I say that now? Now, what we will do is, can I say that now?

56:37

We were not able to see the data in this basic LLM chain node, right?

56:40

Because it was not connected.

56:42

Now, whatever data we have pinned in the previous node, will we be able to see that data in the basic LLM chain node now?

56:48

Will we be able to see the data? Yes. Now it will be visible.

56:51

Now if you double click on this node, can you see the data here?

56:53

Right? The ID, the thread ID, right? The headers, the subject, right? From email to email,

57:01

content type, HTML value, and more importantly, the text. This is the text that we are looking for.

57:07

Correct everyone? Now, because it was not connected, right? Now what we will do is we will use

57:11

defined below. And here we will provide the prompt. What prompt should we give?

57:19

What prompt should we give? Can I say that, we are giving you the code.

57:23

Right? You can expand this prompt window, everyone. This is very small window.

57:27

You can click on this window and this window will get expanded. Can I said, we should give the prompt

57:31

that given the Python code, right, given the Python code, and here everyone, you have to add the Python

57:40

code. How will you get the Python code, folks? Here you have to attach the Python code. How do we attach

57:46

the Python code? From the email, how? From the email, how? From the email, not HTML tag.

57:51

HTML tag, there is a lot of other data.

57:53

But if you just go to the text, text, we just have to drag and drop. Absolutely correct.

58:00

If you just drag and drop everyone, and if you just click on this window, can you see that given the

58:05

Python code and it has attached the complete Python code? Can you see that? Can you see that? See how easy

58:12

it is to use anything. Just whatever field you want, just drag and drop in the prompt window

58:19

and the entire code will be added. Once you have the code,

58:22

what prompt instruction we want to give to the LLM? Given the Python code, please summarize this

58:30

code in a beginner friendly manner, make sure that make sure to include to include all the technicalities, technical

58:52

about the code. Please summarize this code in a beginner friendly manner. Make sure to include all the technical details about the code and technical details about the code and what we can do. And that's it. I think good enough, right? But everyone, let's say we don't want to edit the code. So we can say that just provide a proper summary of the code. Do not edit it. Do not edit it. Do not

59:22

make changes in the code, okay? Good enough everyone. Do not make changes in the code.

59:30

Clear or not? This is the instruction that we are adding. Clear everyone?

59:36

Right? The prompt is ready? Correct. Okay. Then prompt is ready. Defined below. Save an example. Fine.

59:47

This is the code we have and do we need anything else? Add batch processing. It is not required.

59:52

Now, we can actually provide some system prompt also. From Langchain classes, do you remember system prompt?

1:0:00

That every, like, some prompt that you are basically some kind of restrictions you are giving to the LLM as a system, right?

1:0:06

That all these are the rules or the settings that you have to always follow.

1:0:12

So system prompt me, you will write. You are a helpful coding assistant.

1:0:22

and a coding assistant who is who can write or let's say you are a helpful

1:0:31

coding assistant who is very good at Python.

1:0:40

That's it. I think this is very small way in which you can provide the system prompt. Can we say

1:0:46

that everyone? Okay, that's it. And now everyone, I think we can execute this step.

1:0:52

Let's see what kind of summary does it generate? Everyone clear till now?

1:0:56

But as of now, everyone, there is one thing that we have not done.

1:1:00

Okay? If you try to execute this, a model is not associated, right?

1:1:05

You have given the prompt, but have you added the model? Have you added the GPT model or any other model as of now? No.

1:1:11

So you will close this and guys, you will click on plus here and you will add some model.

1:1:16

Now, guys, we are more comfortable with OpenAI. So I will go to OpenAI model, OpenAI chat model, and I will select this model.

1:1:22

GPT 5 mini, any one of them I can use. If you see, there are no credentials set as of now.

1:1:28

Correct? There are no credential set. We will first set up the credential.

1:1:32

Click on set up credential and we have to give the API key, right? Just like I think we have done

1:1:36

this hundreds of times. Go to platform.a.com. We have done this hundreds of times, everyone.

1:1:44

How to generate the API key. Go to API key. If there is anyone existing, deleted.

1:1:52

Revoke.

1:1:53

Revoke.

1:1:56

Create a new secret key.

1:1:58

Let's call it as demo key.

1:2:00

Create a new secret key.

1:2:04

Copy this.

1:2:06

And paste it here.

1:2:09

As soon as you paste it everyone, and nothing else is required.

1:2:13

This is very simple, straightforward way of giving the credentials in GPT.

1:2:17

Click on save, it will verify the credential.

1:2:19

And once it verifies the credentials, everyone,

1:2:21

credentials successfully created inside your personal space.

1:2:24

Now, N8N will store the credentials safely.

1:2:27

We don't have to worry about it, right?

1:2:29

And if you see folks, the N8N is, this GPT model has been added with our basic LLN chain.

1:2:36

Now guys, one more thing, we can give some better name to this.

1:2:39

Let's say code summarizer.

1:2:41

Okay, we can give them a code summarizer.

1:2:44

Okay, and this is OpenAI chat model.

1:2:46

Now everyone, what we can do is, if you see, we have the data, we have given the prompt,

1:2:51

Now if we try to execute this, ideally now it should be able to execute because we have given the access to the model, right?

1:2:57

If everything looks good, it should be able to execute, right?

1:3:00

Click on execute.

1:3:01

Error in subnode, open AI chat model.

1:3:03

What is the problem?

1:3:09

Okay, okay.

1:3:11

Use any model, open, okay.

1:3:13

We have set up the credential, open AI account, fine.

1:3:16

Use any model, let's say GPT 5.2 we use always, right?

1:3:20

right?

1:3:22

GPD 5.2.

1:3:25

Response is API.

1:3:28

Not required, not required.

1:3:31

That's it.

1:3:33

Credentials are given now.

1:3:37

Execute this node.

1:3:42

And now if you see everyone, now it is making a call to LLM.

1:3:46

Can you see that?

1:3:47

It took few seconds of time to refresh the credentials because we have set the

1:3:50

the new credentials, right?

1:3:51

It is executing the node.

1:3:52

Let's see whether we are getting the code summary or not.

1:3:57

It will take some time everyone.

1:3:59

It is making an API call, sending the data, then it is receiving the data.

1:4:02

It will take some time.

1:4:04

It will take few seconds of time.

1:4:06

And the data should be ready within few seconds.

1:4:10

Can you see that everyone?

1:4:12

We have got a proper well-detailed summary of our code.

1:4:15

If you see, this script builds a small customer support chatbot using language.

1:4:19

bot using Langchain and OpenEi chat model with one, a tool for looking auto status per session

1:4:27

conversation memory and so on.

1:4:28

The summary is ready.

1:4:29

Is everyone clear with this?

1:4:32

Now if you see, green tick mark, green tick mark, the model is ready to run.

1:4:37

Clear?

1:4:38

So what we have done as of now?

1:4:40

We read the email from the Gmail account.

1:4:43

Correct?

1:4:44

We automatically read the email from the Gmail account.

1:4:46

The node got triggered.

1:4:48

Whatever data we got from the email.

1:4:49

email, we pass that to the code summarizer.

1:4:52

Correct?

1:4:53

And this code summarizer made a call to the LLM to summarize the basically to execute the prompt.

1:4:58

And now we have the data ready.

1:5:00

How many if you're clear till this point of time?

1:5:02

That yes, we are able to make an LLM call via N8N application.

1:5:06

Clear or not?

1:5:09

Okay?

1:5:10

Now we will take a break, take maybe 10 minutes of time, try to do till this point of time.

1:5:15

Okay?

1:5:16

So it's 855.

1:5:17

Let's have a break of maybe 13 to 15 minutes.

1:5:18

minutes, 10 minutes, try to do this on your own.

1:5:21

If you get stuck at any point of time, do let me know after the break, okay?

1:5:25

So this is the screen I'm leaving you with.

1:5:28

Please try.

1:5:29

See you after the break.

1:5:48

Thank you.

1:6:18

Thank you.

1:6:48

Thank you.

1:7:18

Thank you.

1:7:48

Thank you

1:8:18

Thank you

1:8:48

Thank you

1:9:18

Thank you

1:9:48

Thank you

1:10:18

Thank you

1:10:48

Thank you

1:11:18

Thank

1:11:20

Thank

1:11:22

Thank you.

1:11:52

Thank you.

1:12:22

Thank you.

1:12:52

Thank you.

1:13:22

Thank you.

1:13:52

Thank you.

1:14:22

Thank you.

1:14:52

Thank you.

1:15:22

Thank you

1:15:52

Thank you

1:16:22

Thank you

1:16:24

Thank you

1:16:26

Thank you

1:16:28

Thank you

1:16:30

Thank you

1:16:32

Thank you

1:16:34

Thank you

1:16:36

Thank you

1:16:38

Thank you

1:16:40

Thank you

1:16:42

Thank you.

1:17:12

Thank you.

1:17:42

Thank you.

1:18:12

Thank you.

1:18:42

Thank you.

1:19:12

Thank you.

1:19:42

Thank you.

1:20:12

Thank you.

1:20:42

Thank you

1:21:12

Thank you

1:21:42

Thank you

1:21:44

Thank you

1:21:46

Thank you

1:21:48

Thank you

1:21:50

Thank you

1:21:52

Thank you

1:21:54

Thank you

1:21:56

Thank you

1:21:58

Thank you

1:22:00

Thank you

1:22:02

Thank you.

1:22:32

Hi everyone. Am I audible everyone? What did we give the system prompt? Just a simple sample system prompt, nothing much. Just we have written this.

1:23:02

You are a helpful coding assistant who is very good at Python. That's it. Okay, nothing

1:23:06

much. Guys, how many if you are able to reach till this point of time, till this stage?

1:23:11

How many if you have reached here till this stage that at least you should be able to read

1:23:16

the content from your email? You should be able to summarize the code. You should be able to attach

1:23:21

the LLM. And after that, you should be able to get the summary. Now, once we have the summary,

1:23:26

what should we need to do now? Once we have the summary ready, what should we do now?

1:23:32

Once you have the summary ready, what should we do? We should send an email. Okay. Now, everyone,

1:23:42

before we send an email, let's maybe write one more LLM. Just like, let's add one more LLM use case, right?

1:23:49

Just to make it slightly more complex. Okay, as of now, it is slightly simpler. Let's say, everyone,

1:23:54

this agent is actually, take care. If you see, this one basic LLM chain, can say,

1:24:02

this is used to summarize the code? Correct or not? This is used to summarize the code.

1:24:09

Correct or not? Yes. Now, everyone, let's say I want to add comments in the code also. So as of now,

1:24:15

can you see that? There are no comments in the code? There is no commenting here. Right? Let's say,

1:24:21

everyone, we want to add proper comments also. So what I can do with the help of LM, now one more thing,

1:24:26

one very interesting thing. Can I summarize the code and add the comments parallelly?

1:24:32

Can I summarize the code and add the comments parallelly?

1:24:37

Yes, we can do that. We can do both of these things parallel, right?

1:24:40

These are asynchronous operations. These are not dependent on each other, right?

1:24:43

So why should we do them one by one? Obviously, you can do one by one also. There is no harm.

1:24:47

There is no problem. But obviously it is going to be slow. So what you can do everyone is,

1:24:51

is you can create a copy of this. You can duplicate these two nodes as it is. Okay?

1:24:59

Character not folks. And guys, now to this

1:25:02

node, you can actually give a separate name here. So let's say this is not code summarizer,

1:25:09

rather this is a code commentator, right? Code comments. That's it. Now everyone here,

1:25:17

what we will give is we will have to change the prompt slightly, right? Given the Python code,

1:25:21

this code, please provide proper comments in this code.

1:25:32

manner, make sure to include all the technical details about the code in the comments.

1:25:39

At the same time, at the same time, like we can say that comments should not be very long, right?

1:25:49

Commence should not be very long. Comments should not be very long.

1:25:55

Okay. Just provide a proper summary. With this, we can remove everyone.

1:26:02

And this restriction we can still add, do not make changes in the code.

1:26:10

So let me show this to you. See, this is what we have given. Given the code, please provide proper

1:26:15

comments in the code in a beginner in any manner. Make sure to include all the technical details about the code in the comments.

1:26:21

Comments should not be very long. Do not make changes in the code. Can you see that everyone? Like very simple.

1:26:27

Do not make changes in the code. That's it. This is what we have given everyone. And system prompt, we don't have to change.

1:26:32

It can be given as it is. That's it. And everyone here, we have already, because we have C, in LLM, everyone, you can copy the nodes so that you don't have to set up the credentials again, right? Can you see that?

1:26:44

Model you don't have to select, credentials you don't have to set. Everything is there. Okay? If you have given some custom properties also, those are also going to be there.

1:26:51

So, guys, this also you can connect from here to here. Now, if you see everyone, from this Gmail trigger, can I say both of these steps will run parallelly?

1:27:01

Correct or not? Both of these steps will.

1:27:02

run parallelly. Okay? So now everyone, what I can do is let's try to run this step also, execute

1:27:07

this step. It will take some time, obviously, because it is going to add comments. And let me show you

1:27:11

that whether it is able to add the comments or not, right? And if you see, because we have pinned the

1:27:16

data in the previous step, we can see, we can still access the email content here. We can still access

1:27:23

the email content here. Okay. If you see everyone, import,

1:27:32

the open-a-chat model. Can you see that? Hash? It is giving the comment. Hasch prompt building

1:27:37

utilities and hash agent utilities. Can you see everyone? It has given the proper comments. As of now,

1:27:43

it might not be very much readable because it is in the JSON format. I think if you see in different

1:27:49

format, it might be visible. But I'll show you that. Don't worry. You see that? Hash import the open-A-I

1:27:54

chat model. So it is running fine. Now, what do we need to do? As soon as the email will receive,

1:28:00

we will receive an email from Deepakasara 18 at the rate gmail.com. This node will automatically

1:28:04

get triggered and read the email and it will pass the input to these two nodes, code summarizer and

1:28:12

code commentator, right? Code summarizer will summarize the code and code commentator will give the comments.

1:28:18

Guys, just give me some.

1:28:30

Thank you.

1:29:00

Thank you.

1:29:30

Thank you.

1:30:00

Yes, everyone. So now once we do both of these things parallelly, doing parallel is very important, right?

1:30:06

So guys, as a developer, you should also identify that what things I can do parallelly. Because if you can

1:30:11

perform task parallelly, then obviously it is going to be very good for your performance, very good

1:30:16

for the performance of your application, isn't it? Okay. Now tell me everyone, once you have the summary

1:30:21

ready, once you have the code comments ready, what should we do now?

1:30:26

Once you have the code summary ready and once you have the comments ready. Once you have the code summary ready and once you

1:30:29

have the comments ready. What should we do now? What should we do now?

1:30:39

Don't you think we should merge both of these outputs and send it on the email? Can we say that?

1:30:47

merge both of these things and send it as an output, send it as an email? Now one more thing,

1:30:53

everyone, see. Before you send an email, see, one more thing.

1:30:59

Because both of these LLM chains, code summarizer and code commentator, both of these things

1:31:04

are going to run parallelly. Now, when things runs parallelly, can you actually control

1:31:08

in which order they are going to execute? Can you actually control in which order they are going to

1:31:13

get executed? No. It's quite possible that summary might be ready first or comments might be ready

1:31:18

first. You don't know, right? Because things are happening parallelly, it's a network call,

1:31:23

right? Depending on the network speed, depending on the busyness of the API and whatnot, right? How much

1:31:27

heavy task you're doing. Anything can happen.

1:31:29

anything can get completed first. But everyone, before you send an email, do you want the output

1:31:35

from both of these things? Summarizer as well and commentator as well? Yes or no? Do you want the output

1:31:41

from both of these things to be ready? Yes. For that, everyone, we have a node called as merge node.

1:31:47

Search for merge node, everyone. If you see, merges data from multiple streams once the data from both

1:31:52

is available. It means that everyone, you should merge the data from both of them. Right?

1:31:59

Correct or not? That let's say, if this is the merge node, let's delete it. Let's create a merge node first.

1:32:05

Create a merge node. Right? Just close it for now. This is the merge node. Can I say that everyone? You want to merge the input, the output from LLM1 and output from LLM2. And guys, what it tells you, and if you see everyone, if you search about it, what it tells you, merges data of multiple streams. Once the data from both is available.

1:32:29

It means that everyone, it will only merge the data once the execution of summarizer is also done and commentator is also done.

1:32:38

Is that point clear to all of you, everyone? Is that point clear to all of you? Is that point clear to all of you? Summary is also ready and comments are also ready. Then you will merge the output of both of them. Yes or no?

1:32:51

Guys, yes, no. Then only you can merge right and merge node will automatically take care of that. Now if you double click on this, everyone,

1:32:59

How many things we are passing in the input to this merge node?

1:33:02

How many things we are passing in the input to this merge node?

1:33:05

Two inputs, right?

1:33:07

Double click on this, everyone. Can you see two inputs here?

1:33:10

One is, yeah, if you see code comments, right?

1:33:14

Two inputs, one item and code summary, another item.

1:33:17

Can you see that, everyone?

1:33:19

Let's execute this once again.

1:33:22

Because actually we did not pin the data now.

1:33:24

That's why.

1:33:25

So one can do can do.

1:33:26

Let's close this for now.

1:33:28

this for now. Okay, it is generating the code summary. So in code here, let's pin the data here.

1:33:35

Okay. Let's pin the data here. And once the summary is also ready, we will pin the data because we don't

1:33:40

have to execute it again and again. Unnecessary to consume the tokens. Okay. So once we have the output

1:33:45

ready, we can pin it so that we can use it for the testing purpose. Clear everyone? Are you guys

1:33:52

able to relate right? Perfect. Now we will pin this also. Now close this and if you see merge everyone,

1:33:57

merge, what is doing? If you see, it is taking, it is getting two inputs.

1:34:01

Can input are you? One, it is getting the input, input number one, one item. If you see input one,

1:34:09

first input, which is the summary. Can you see that if you want, the summary is coming in the input?

1:34:14

And the second input is the Python comments. Can you see that? The Python code in the form of comments.

1:34:20

And now everyone, if you see append, we can do actually multiple operations on these two items.

1:34:24

We are getting two inputs. One is a summary, one is a comment. So we want to append.

1:34:27

both of them. So number of inputs are two and we want to append them. So can you see that

1:34:32

even as of now what is happening? We are getting two items in one list. Can you see that? Two items

1:34:37

we are getting in one list. First list is the summary list. One is the JSON object. Scroll, scroll,

1:34:44

scroll, scroll, and there is another JSON object which is the code with comments. Can you, can all of you

1:34:49

see this or not? There are two like two JSON objects we are combining into one list. If you see this is a list,

1:34:55

can you see that? This is a list where there is one JSON object which is the summary of the code

1:35:00

and another JSON object which is the code with comments. These are the two outputs that we are

1:35:06

getting. Take everyone. Done. And let's pin this also. Okay? Folks, yes or no?

1:35:21

Yes or no. Now it has combined the input of both of them.

1:35:25

But everyone now, as of now also, have you combined actually, like as of now, what do you have

1:35:31

is, don't you think both of these things you have individually now?

1:35:34

One is one JSON object, another JSON object, right? You have two JSON objects. The only thing

1:35:39

that merge node has done is that merge node will give me the output of both of these things in one

1:35:45

list. Can we see that? The output of code summarizer and code commentator, merge node

1:35:52

node will give me in one list. And that list will have two items. Can you see that?

1:35:55

here? Just see this. That list will have two items. It will give, it will take input one,

1:36:00

it will take input two and that will have two items in the output. Fine. But everyone now,

1:36:05

can we send these two items individually in the email or should we aggregate both of them?

1:36:11

You can send individually also, but do anything better, we aggregate both of them? First we add the

1:36:17

comment and then we add the summary. Then everyone, there is one more thing, one more type of node

1:36:22

that we have, which is called us aggregate node. Now we even, again, again, again,

1:36:25

aggregate node me, what you do is, you have the individual fields, get the individual fields.

1:36:29

And if you see folks, here, in this individual field, what I can do is, yeah, comment, connect,

1:36:35

aggregate node with the merge node. And aggregate node will get two items in the input, right? It will

1:36:41

get two items in the input. One is the code summary. If you click on this, the text. Can I say that

1:36:47

this text will have two things?

1:36:53

This text will have two things. This text will have two things.

1:36:55

things? Correct or not? So basically what you want to do is just a second.

1:37:05

Here you have two items. Uh, JSON may. Look in the FEMA. You can say that in the way of JSON.

1:37:13

It will be easily understandable. If you see everyone, in the field of JSON, you are getting two fields,

1:37:18

right? One is the text field you are getting. And another is also the text field. So basically,

1:37:22

you are getting two text fields, right? So do only thing you need to aggregate.

1:37:25

both of these text fields one by one. You need to aggregate them, right? In one unit.

1:37:30

Correct? So as you have, let's say, first you want to aggregate input field name. You want to aggregate this.

1:37:40

And add field to aggregate. You want to aggregate this. Is everyone clear? And guys, now let's do

1:37:51

just one thing. Enter the field name. Rename field is not required.

1:37:55

all item data into a single list. No, we don't want single list. We just want to aggregate

1:37:59

both of these things after one and another. Okay, so input field name is text. And let's try

1:38:09

to execute the output.

1:38:19

Fields to aggregate. Okay. Just a second. I think, just a second, I think there is a different

1:38:25

to aggregate.

1:38:35

Correct. What we want to aggregate everyone is that we don't have to give these two things,

1:38:41

right? Just one thing, text. That input field name is text. We want to aggregate text fields. Okay? So just

1:38:47

give this here, drag and draw and nothing, and just execute the step. Yeah. Now if you see everyone,

1:38:54

Can you see that now? What we have done? All of you understand this, that this aggregate

1:39:00

go, this aggregate node will get two text fields from the previous nodes. One is the summary,

1:39:05

one is the comment, correct? One is the code summary. One is the code with comments. Yes or no? It will

1:39:10

get two things in the input. Everyone understand? Two JSON object. One is this JSON, the code summary.

1:39:18

Folks, yes, no? One is this code summary. And another text is the code with comments. Correct?

1:39:24

Now, what we have done is we have just said that, add these individual fields, which are named text, into one thing.

1:39:31

So if you see everyone, in this text, first we are getting the summary. We are getting the summary.

1:39:36

Okay? Yeah. This schema is better. In one text, inside this, we have two inputs. Basically, we have two things.

1:39:45

One is the summary and one is the code with, like code with comments. It means that now inside the text, we have aggregated both of these outputs.

1:39:54

Can you see that everyone? Inside the text, we have, what do you say? What we have done is we have aggregated? We have aggregated both of these things. Summary as well and output as well. Clear? Summary as well, comments as well. Now, pin this is also. Now, what do we need to do?

1:40:14

Now you tell me, once the aggregate is ready, once the aggregate is ready, what should we do now?

1:40:22

We should send the email now?

1:40:24

We should send the email. Now everyone, we will click on this.

1:40:33

Okay, this is our workflow looking very beautiful. So we will click on plus again.

1:40:38

Search for Gmail. Click on this. And what kind of action do we want to do now? We want to do

1:40:45

send message. Send a message. Okay. So guys, credentials are automatically there.

1:40:51

Resource is message we want to send. Okay. Operation is send operation.

1:40:54

To whom? Which email? My email only. Deepak Kassera 18 at the rate, gmail.com.

1:41:00

Subject is, let's say, uh, Python code. With summary and comments.

1:41:08

Okay, no? This is the subject of the email. Email type is text. For now, we are just sending the text email.

1:41:15

Everyone clear or not? Folks, yes, yes, no. Okay. Now, tell me everyone.

1:41:24

we send inside the message? What should we send inside the message? Can I say that?

1:41:31

we should connect this node with the previous node. That is, we should put it here.

1:41:38

Hanna? So that we can see the input from the previous node. Output of the previous node we can see

1:41:42

in the input, right? Can you see that now? If you see the schema, we are getting two things, right?

1:41:47

Text 0 and text 1. Text 1 is code with comments. Text 0 is summary. Is everyone able to understand

1:41:54

until now. Text 0 is summary and text 1 is, text 1 is the code with comments. So guys,

1:42:00

what message I want to put? Expand this. Let's say we can say code with comment, right? Code with

1:42:08

comments everyone is present in which field? It is present in text field. Can you see that? Can you see

1:42:14

that everyone? Code with comments is present in text field. Then code summary. Code summary will be present

1:42:21

in what field, everyone? It is present in text 0. So I will just drag and drop here.

1:42:28

Can you see that everyone? What we have done? Now execute this step and this is how you will be able

1:42:34

to see the output. Let's see. Okay, why you are not able to see jason text 1 labels?

1:42:51

If you execute this step, I should have received an email, right? Okay, let me see everyone

1:42:58

if the email has been received. Great. So as soon as I executed this everyone, I have just

1:43:10

received an email. Can you see that? Can you see that? I have just received an email.

1:43:16

Python code with summary and comments 931, zero minutes ago. Code with comments. This is the code with comments, everyone, right?

1:43:26

folks, yes or no? Can you see that? Proper comments have been added everywhere? Guys, yes, no, yes, no.

1:43:33

Just last 15 minutes of the class. Please be very, very energetic. Right? And then everyone, after all the comments,

1:43:40

then at the end, you will see code summary. Can you see code summary as well?

1:43:44

proper code summary, detailed summary you have, code summary.

1:43:52

It means our workflow is running absolutely fine. What we will do now is we will do it from beginning

1:43:56

also. Okay? So let's do one thing, everyone. Let's go to the code. And there is one more thing,

1:44:01

everyone. If you look at this email, right, here you will see that. This email was sent automatically

1:44:07

with N8N. Can you see that? Just to verify that, yes, this is not the email that I have sent manually,

1:44:12

right? There is not a manually.

1:44:14

email, this email has been sent automatically by N8N. If you want to remove it, you can remove it,

1:44:19

actually. If you see add option, add option, add option, add option, yeah, append N8N attribution and you

1:44:28

can disable it. As soon as you disable this everyone, and you again execute this step, now this send with,

1:44:34

okay, we have, I by mistake, clicked it. Now let me show this to you. I'm not actually showing you

1:44:40

the complete email list for obvious reasons.

1:44:44

Okay? Let me show you one more email, everyone, that I just have received. See this everyone

1:44:50

now. Can you see that, everyone? I have received one more email now at 933. At 933. Can you see

1:44:58

that? At 933, zero minutes ago, I have just received one more email. But here you will see that.

1:45:03

Code sent with N8N, that this email has, this email was sent automatically by N8N. This is not there.

1:45:10

Everyone clear? This is not there.

1:45:14

yes or no? Okay? Everything is working fine. Very good. Very good. Now what we will do

1:45:20

everyone is we will connect this. That's it. Our workflow is ready. Can you see that everyone? Our workflow

1:45:26

is ready. Okay. Now let's have a quick demo. Okay. What I will do is I will go to this and I will

1:45:37

unpin this data. Okay, unpin. And we will execute the complete workflow. I will go to all the data nodes and I will

1:45:44

unpin this data. Unpin. Unpin. Unpin. And there is no pin here. And what I want to do everyone is,

1:45:59

let's say, just to give you a glimpse, let's say I change this. Python code with, I'm just adding new email

1:46:07

so that I can identify that. We can identify that this is a new email, right? Okay. So should we execute the

1:46:12

Should we execute the complete workflow folks from the starting? Okay? Let's execute.

1:46:19

Actually, we will have to do one thing, everyone. Let's delete these latest emails, right?

1:46:23

Otherwise, it will keep on reading the same email again and again. So what I'm doing is I'm reading,

1:46:28

I'm deleting these new emails from my email list, from my email, right?

1:46:42

Done. So guys, I have deleted these emails from my email. Now I just have one same email

1:46:50

in my email list, okay? Python code. So what I will do now is I will again execute the workflow.

1:46:56

Let's see what happens. And you will see that. All these things will execute step by step.

1:47:01

Code summarizer is running. Parallely code comments is running. Okay?

1:47:04

Okay. If it is running like you will see this motion. Okay. It is running like you will see this motion. It is generating the comment. It is generating the comment.

1:47:34

So. Merge, aggregate, send a message. Now let me see everyone whether I have received an email or not.

1:48:04

Can you see that everyone? I have just received a new email at 936, 0 seconds ago.

1:48:13

And everyone, if you see, the new email subject, new email, that we just added.

1:48:18

This is the proof that this is the brand new email we have just received.

1:48:21

Code comments and code summary.

1:48:26

So our workflow is ready. It is automatically getting triggered, automatically getting executed,

1:48:30

automatically generating the summary, automatically generating the comments.

1:48:34

automatically sending an email back. Can we get the subject line also rather than

1:48:38

hard coding it? Can we get the subject line also? Yes, you can do that, absolutely. For example,

1:48:44

let's say you can get the subject from the, from the previous email, from the email that you are reading,

1:48:50

and that you can keep on propagating and that maybe let's say you can have the same subject.

1:48:55

Okay? You can do that. In fact, you can reply on the same email also. That is also possible.

1:48:59

If you see here, there is an option, right? Delete, get, reply.

1:49:03

There is a reply also. If you want to reply in the same email, all these things are possible.

1:49:09

Guys, how many of you are crystal clear till now that what we have done? And this complete thing

1:49:14

is completely understood to all of you. Please let me know.

1:49:22

Everyone clear?

1:49:33

One more thing everyone actually you can do here is because we have just maybe 10 minutes of time.

1:49:51

Let's say as of now, the email that you are getting, is this email actually coming in a proper code format?

1:49:58

Proper formatting is it coming? No, right? It is very difficult to read, right? Because code should come in

1:50:03

proper formatting, right? So actually, can you put, can you give proper formatting to your

1:50:07

code? Answer is if you can do that. Once you have the aggregate data ready, you can actually

1:50:13

add a new node here. Click on plus here and go to Edit node. Go to Edit node. And you can say

1:50:21

that, edit fields. Click on this node. And you can do manual mapping. And manual mapping, if you see

1:50:28

what data we are getting. So what you have done everyone is we have written Edit Fields node. Can

1:50:33

see that? In this edit fields, what do you think? What should we do?

1:50:38

What should we do?

1:50:38

Now, can I say that, whatever data we are getting from the previous aggregated node, if you see

1:50:54

what is the input for this. Okay, now actually, the data is not pinned now, right? Okay, actually,

1:51:00

we can see the data right. Script, text, zero we are getting. Edit field in, text,

1:51:06

one we are getting? Are we getting both the fields, everyone? So what we can do is, uh, fields to

1:51:12

set. Okay? So you can do, so you can do manual mapping, text, string, and value. Name is, let's say,

1:51:30

fields to set. Okay, I think we can do name with code with comments and the value

1:51:45

is this. Okay, this is the result. And we want to add one more field here. Include another input field.

1:52:00

Add field, code summary. So we are getting the summary. This is the value.

1:52:12

Sorry, so we can delete this. So we have two things, code with comments and code with summary,

1:52:19

and code summary is text 0. Can you see that everyone? Now if you execute this step, are we getting both of

1:52:26

these things here in the edit field node that this is code with comments and this is

1:52:31

code summary. Are we getting this thing or not? Folks, yes or no? Now everyone, how can we give

1:52:40

proper formatting to this code? Can we use again, can we again use LLM to give proper formatting? Again,

1:52:47

everyone, we are just, I'm just adding this optionally. This is not mandatory what we are doing. Okay,

1:52:51

in fact, in fact, everyone, you can modify your previous LLM in such a case in such a way.

1:52:56

that it will give you code with proper formatting. Correct or not? That why to use another

1:53:01

LLM here once again, but I'm just showing you the easier way of doing this. Okay? So basically

1:53:07

what happens, everyone, the email or any data that you sent on the internet, if you send this, as of

1:53:12

now, if you see everyone, when we are sending the email, right, sending the message, in what format

1:53:17

we are sending the message? Can you see that we are sending the message in the text format?

1:53:21

And that's why the code is displayed in the text format, right? But ideally what should happen is,

1:53:26

we should display the code in the HTML format. Actually, what we can do now? Let's do one thing.

1:53:31

Why to delete? Why to have this edit field? Let me try to do one thing. While aggregating the

1:53:36

data, when sending the email, we have this as well. We have this as well. Let's do one thing.

1:53:43

In the code summary, can we change this in such a way that please give the output, please give the output in HTML format.

1:53:56

HTML format, which can be easily sent over the mail without losing the context.

1:54:08

Clear everyone? We have just added one more line. That I don't want the data in the textual format.

1:54:12

I want the retina in the HTML format. Okay? Clear or not? Folks, yes, no. Okay? Similarly, everyone,

1:54:20

I will again give the same value in the code commentator also. In this,

1:54:26

other agent also, I will give the same thing. That please give me the output, please give

1:54:30

the output. See, please give the output in the HTML format which can be sent over the email without

1:54:36

losing the context. Clear or not? Folks clear? Okay? Now what I will do is, now everyone, for example,

1:54:47

if you just execute this thing, right? Let's say for example, if I just go to this and execute

1:54:52

fetch event. If I fetch this event, okay?

1:54:56

it has got this. And can you see that everyone? We are getting this in the text as HTML.

1:55:03

Code with comments, you know? Code with comments. Text as HTML, fine. And now, let's run this

1:55:11

code summarizer. Also, let's pin the data, whatever data we are getting, pin the data, and code

1:55:17

summarize it execute. Let's see what data it generates. What output it generates? We have just added one

1:55:23

line. That give me the output in the HTML format. That's it.

1:55:26

we have done. And now we are just executing it again to see whether we are getting the output in the HTML format or not.

1:55:45

That also we can try. I have not. I have not tried that Nyserk, but I think that should also work. That's correct.

1:55:56

Okay. Can you see that if you want, we are getting the data in the HTML format?

1:56:02

We are getting colors, line, height, CSS properties also, okay? Let's execute, let's pin the data.

1:56:11

Let's execute this node also.

1:56:21

I think that this node also. I think that this, in my hunch, it should work.

1:56:26

The only change that we have to do is that in the while sending the email, we are sending the data as a text.

1:56:32

We will have to select this as a HTML.

1:56:39

Okay, now we are again getting the HTML data. Very good. Merging me, there will be no problem.

1:56:45

Merging may, let me pin this data also so that we can use it again. Merging in, we can execute the step

1:56:50

and we are just schema. We are merging both of these things, text and text.

1:56:56

two items we are getting code summary and all. Merge, fine. Two items we are passing to aggregate.

1:57:01

Merging maybe everyone, just pin the data so that we can use it again. Aggregate also. Execute the

1:57:07

aggregate step. Aggregation done, text 0, text 1. Very good, very good. Text 0, text 1. Now while

1:57:14

sending the email folks again, aggregate may be just pin the data. And email may just change one thing

1:57:21

that instead of sending textual data, I'm sending the HTML data.

1:57:26

text 1 is the comment, 0 is the summary. Very good. Now I will execute this.

1:57:35

Let's change the subject a bit everyone. Let's say this is latest email. I'm just changing the subject

1:57:41

so that we can identify that this is the latest email and execute the step. Now email sent. Now let me

1:57:47

see whether we have received the final email or not and in what format we have received the email.

1:57:56

This is the final email, everyone, what we have received from N8N. Can you see that now, we are getting proper textual, proper HTML formated data. Can you see that now? Code is much, much more readable. Not only that, just look at code summary. Proper highlighted bullet points. Correct or not? Can you see that? It was not there earlier. This is what we wanted to do.

1:58:26

Folks, how many of you are clear with this?

1:58:31

How many of you are clear with this?

1:58:34

How many of you enjoyed the discussion, right? That we have the agent ready,

1:58:38

which is, which gets triggered automatically. We don't have to do anything.

1:58:42

Automatically it will get executed, automatically.

1:58:45

Okay? Now everyone, that's it for today's class. I hope all of you enjoyed. How many if you enjoyed?

1:58:50

Just a couple of people I have got the response, three people.

1:58:53

Out of 25 people, only 20, 25 people.

1:58:56

Only three, four people enjoyed the class.

1:59:01

Okay, guys, what I can do is, let's do one thing.

1:59:04

Let me take a screenshot of this and put it in the same GitHub repository so that you can refer.

1:59:17

What I can do is I can upload this on GitHub and how can I do that is Visual Studio.

1:59:26

Thank you.

1:59:56

Actually, let's do one thing.

2:0:06

Let me, how can I upload this on?

2:0:09

Let me go to recent.

2:0:13

The screenshot must be present.

2:0:16

The screenshot must be present in recent.

2:0:19

The screenshot is there.

2:0:21

Let me go to GitHub.

2:0:26

a genetic design batch.

2:0:56

the file on the GitHub account.

2:1:00

Okay, I think there is some error everyone.

2:1:02

But anyways, I think you should be able to create it.

2:1:06

Okay.

2:1:07

How can we see and access this workflow?

2:1:11

Maybe publish this.

2:1:12

After publishing, let's say version 01.

2:1:26

But publishing I cannot show you, right?

2:1:30

How can I share this with all of you?

2:1:47

Where is the export button?

2:1:55

Where is export? I cannot see that.

2:2:02

Yeah, let's try to download this and then.

2:2:18

Okay, so this has been downloaded at JSON.

2:2:24

JSON say downloads, email workflow.

2:2:29

JSON.

2:2:30

Guys, JSON, I'm not sure that how many few will be able to understand JSON.

2:2:35

Okay, let's try to upload and let's see how JSON looks like.

2:2:39

Okay, so in the nodes part, I have uploaded this JSON.

2:2:44

Guys, this is how the workflow looks like.

2:2:50

Yeah.

2:2:57

I think you can directly upload this on N8N also if you want to take a reference.

2:3:02

For example, let's say somewhere you will be able to see download, rename, favorite, import, import

2:3:08

from file.

2:3:09

So I think you can import it here.

2:3:11

Right?

2:3:12

Correct.

2:3:13

I think this looks good.

2:3:14

Okay, so you can directly import this as a JSON file on your N8N server and it will be

2:3:20

as it is, you will be able to see all the fields. Very good. Okay, that's it for today's

2:3:24

class, everyone. I hope all of you enjoyed the class. All of you like the class. Thank you so much.

2:3:29

Have a good day. Good night. I'm launching the feedback poll now. This file can be imported by

2:3:35

others. Okay, yes, I think credentials will also get imported. I have not done that earlier. Credentials

2:3:43

in.

2:3:47

Ah, open. It is. It is not actually exposing

2:3:50

the credentials as it is. But anyway, right after the class, I will delete all my credentials, right?

2:3:55

No worries. Okay? So yes, here is the feedback poll. Please take the feedback poll. We are done with

2:3:59

the class. Thank you so much. And have a good day. Have a good weekend. See you in the next week now.

2:4:05

Take care. Goodbye and good night. Good night, everyone. Thank you so much. Thank you.

2:4:20

Key revoked, done.

2:4:24

And also I'll go to branding.

2:4:50

Guys, someone has given one rating.

2:4:55

Is that intentional?

2:5:09

Obviously, I cannot see the feedback?

2:5:11

That is completely anonymous?

2:5:14

But if there is any feedback, then do let me know, right?

2:5:18

Is that intentional?

2:5:19

anything you did not understand from the class?

2:5:49

Thank you. Thank you everyone.

2:5:53

Some, are you there?

2:5:55

Yeah.

2:5:56

Yeah.

2:5:57

You can end the poll, right?

2:6:01

Yes, now it is 100%.

2:6:04

Okay.

2:6:19

I've sent a message. Can you check if that is accessible to you?

2:6:26

Can you see the feedback comment? I cannot see that, actually. So I just wanted to see that if someone has given one.

2:6:32

No, actually. I mean, I also cannot look at the, I mean, the feedback that they have given in terms of text.

2:6:43

Okay, okay, no worries, then. No worries. Okay.

2:6:45

Yeah, I think you can ask Benu or Bianca once they have been.

2:6:48

Okay, okay, sure.

2:6:49

Sure, sure.

2:6:49

I think one of the reason can be sometimes the orderings are different, right?

2:6:53

One, two, three, four, five, or one, two, four, five, like that.

2:6:56

If that is the case, then I think it is okay.

2:6:59

But if that is the case, then maybe the person can let me know so that I can discuss with the team and get this.

2:7:05

Is that the case, everyone?

2:7:06

I don't think so.

2:7:07

Maybe that might not be the case.

2:7:09

Okay.

2:7:10

Maybe you can just ask maybe if he or she has given any comment in terms of feedback, that we can have a look at it.

2:7:17

Yeah.