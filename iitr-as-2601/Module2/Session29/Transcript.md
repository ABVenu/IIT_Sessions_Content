0:00

Thank you.

0:02

Thank you.

0:32

Thank you.

1:02

Thank you.

1:32

Thank you.

2:02

Thank you.

2:32

Thank you.

3:02

Thank you.

3:32

Thank you

4:02

Thank you

4:32

Thank you

4:34

Thank you

4:36

Thank you

4:38

Thank you

4:40

Thank you

4:42

Thank you

4:44

Thank you

4:46

Thank you

4:48

Thank you

4:50

Thank you

4:52

Thank you

4:54

Thank you.

4:56

Thank you.

5:26

Thank you.

5:56

Thank you.

6:26

Thank you.

6:56

Thank you.

7:26

Thank you.

7:56

Thank you.

8:26

Thank you

8:56

Thank you

9:26

Thank you

9:28

Thank you

9:30

Thank you

9:32

Thank you

9:34

Thank you

9:36

Thank you

9:38

Thank you

9:40

Thank you

9:42

Thank you

9:44

Thank you

9:46

Thank you

9:48

Thank you.

9:50

Thank you.

10:20

Thank you.

10:50

Thank you.

11:20

Thank you.

11:50

Thank you.

12:20

Thank you.

12:50

Thank you.

13:20

Thank you

13:50

Thank you

14:20

Thank you

14:22

Thank you

14:24

Thank you

14:26

Thank you

14:28

Thank you

14:30

Thank you

14:32

Thank you

14:34

Thank you

14:36

Thank you

14:38

Thank you

14:40

Thank you

14:42

Thank you.

14:44

Thank you.

15:14

Thank you.

15:44

Thank you.

16:14

Thank you.

16:44

Hi, everybody. Good evening, all of you.

16:50

All of you.

16:53

So, first, quick check with everybody.

17:12

How many of you were able to solve the

17:14

advertising case study from last time. Remember, I gave you that exercise. There was a data

17:20

site I gave you. We'll quickly start over discussion from that. That will also act as a very good

17:24

recap from what we did last class, right? We did a lot of basic regression discussion, train,

17:29

test plate, fitting our linear regression model. So we did that at a basic level. So we will

17:36

quickly start from there. I want to understand how many of you were able to solve that.

17:40

Show of hands, folks who were able to solve. You can

17:44

let me know what accuracy you got. That was an exercise. Remember, guys, how many if you solved it?

17:53

So we'll start from there and then obviously we'll get on with the contents of today, which is regularization.

18:01

But as part of the quick recap, we will start with that exercise.

18:10

No, nobody's out.

18:14

it was an easy exercise guys you want to you want to do it right now or you want to do it

18:28

together along with me we can do it together I will also do you will also do yeah I

18:34

think that will be good right okay let's do it together yeah but but again I mean one of the

18:40

things is that guys whenever we have exercises try to do it try to dedicate

18:44

get some time after the class. This is hardly like a five, 10 minute exercise. Okay.

18:49

So we'll do it. We'll do it together. No problem. Everybody can please open up your collab.

18:57

So collab everybody knows already. Let me, in the meantime, first share my screen. Sorry, just one minute.

19:07

I'll come to today's content. But first, let us. Let us.

19:14

Let us quickly review the thing from the last session.

19:18

Because today's content is very much connected to the last session. Just to clarify,

19:22

and actually many of the things we saw in the last session, today whatever is the planned content,

19:26

many of the ideas we already, some of the ideas we already talked about.

19:30

The new thing that we are discussing in today's session is something called bridge and lasso,

19:35

which is a bit of a theoretical concept. We look at the intuition what it is.

19:40

All the math is not required. We are not getting into that, but just

19:44

help you understand what is regularization and how we compare models. And model comparison

19:49

is something very similar to, you know, what we covered in the last session. If you remember,

19:54

there was a very small case study we made here, right, where, you know, we built a linear regression

19:59

model and then we did a gradient boosting and we compared. That's it. That is what we will see,

20:04

we saw evaluation metrics, R squared, at a basic level, we were able to use core. The other

20:11

metrics I will talk about today. But error analysis.

20:14

and practical perspective is something we so it's kind of a many of the contents are overlapping

20:19

so what i'm planning to do today is obviously one part will be the case study-based approach

20:25

many of you are asking me to solve a case study so we'll do this advertising one simple one not a very

20:29

advanced one so we'll see that we learn some approaches there and then we will go back to the exercises and

20:35

take our typical uh theory notebook and uh go over this this is what we will be doing today okay

20:44

all of you please open up your collab google collab to start with

20:51

collab.research. google.com everybody knows how to launch google collab right

20:57

so just open up a new notebook just open up a new notebook nothing and i will be sharing everything

21:05

else with you whatever has to be done and at least just go and load the advertising data

21:10

you can absolutely have jemini on the side

21:13

so first set up karlow we will just do it together okay everybody you know we want to instill that

21:19

confidence in you exercise doesn't have to be some big thing you know we are sitting and

21:24

you know it's nothing it's very simple you realize how easy it is that's the whole idea i want to

21:30

instill that confidence in you not just at every class we come teach and go but the confidence is

21:35

important you know the confidence is important that yes you can also do it that's the whole idea

21:39

of right so everybody please open up the notebook i hope that the links all of you remember

21:47

so may i'll ping this to everybody okay let me ping this to everybody this is what you have

21:52

for lab.research.gogold.com and please open up the data set that i shared from the

22:00

last session last session of data set all of you have right advertising in case you don't

22:05

have it let me ping this again to all of you on chat it is a simple problem simple problem probably

22:10

by far the easiest of my case studies because we are in the introductory stages i'm taking a very

22:16

easy case study but then we will see some more interesting once later

22:22

the CSV file with you good download caro and please go to your folder just the first

22:32

part of the setup we are trying to do go to your folder structure and just upload the CSV

22:36

file most of the case studies this was not required most of you are opening up the notebook

22:44

and it was just running as it is so here you have to upload the file because you are trying

22:48

to access the CSV file right right so we are trying to upload the file right so we are trying to upload the file

22:52

the file we have to upload the file so make sure you upload the file on this particular section

22:57

okay files may here here upload k're gonna and this is just the basic setup we are trying to do

23:07

after that if you want to write code you can if you don't want to write code you can ask jemini

23:13

to write for you either of two people will write either you write or i write and i ping it to you or jemini

23:19

will write for both of us so we have all the options in today's world right anyways the initial

23:24

part is very simple people can do this along with me and since these are just very basic python

23:34

parts i'm going a little fast here because this to how to read a data from a sb and store it in a

23:40

data frame right we know this right all of you know this just i want to ensure everybody is able to get

23:46

this code up and running here to all execute for us rest what to do i will discuss

23:53

right this after we'll model we'll discuss that but just until here everybody should

23:57

complete please confirm to me if you're able to do it anybody

24:04

stuck at all any error file not found you're getting please ask me i'll help me

24:16

i will pause for two minutes take your time take your time open up your collab

24:24

jupita notebook right you have done these things we have done sessions with you revision sessions we have

24:28

done you're all comfortable with collab you're all comfortable how to load our data into collab right

24:33

everybody knows that how to uh load a data into a data frame and we are just seeing the top

24:38

five rows of our data frame that's it this is simple we're just loading the data

24:46

okay uh just a minute more i'll wait

24:58

and just in case people are trying to locate the file where upload

25:01

file you have to upload here by the way guys okay so file section here

25:04

click on it and then click on the upload button upload

25:08

upload this advertising here upload i've shared that on chat

25:10

you're from there from here upload for you okay

25:14

then go go go and look at it if you if you give a different folder it'll

25:20

will say file not found so make sure you give it exactly the way i'm showing you right now

25:29

is it okay everybody's able to run you're all able to see exactly what i'm seeing on the screen

25:33

right please confirm to me on chat if you're seeing exactly what i'm seeing on the screen

25:44

error is coming sanjita what is the error message

26:04

most likely you have not uploaded the file

26:11

you've not uploaded the file you've not uploaded

26:12

check make sure he look this the setup we're

26:16

this same to same

26:17

should be the same right you should be the same right

26:20

you should be connected to the collab which you are using already

26:23

make sure your file is here in the same place that i'm showing you right now

26:27

okay file upload

26:29

okay the setup should be exactly the same

26:32

then it will be absolutely fine

26:34

and you need to be comfortable with this everybody okay that's why i'm actually doing this

26:38

sir because going forward you know it will not be just like notebooks you have to be able to in real

26:44

world uh i'm up so you have to go and maybe you'll

26:49

you'll go and maybe you'll go ahead go ahead and you're going to be important for you to try

26:53

in practice okay even after uploading it's not showing the thot c sb

26:57

no so ankid it takes a while you should upload not can you try again

27:01

this is upload okay so if if it's not

27:04

if it's not refresh

27:06

just cross check if

27:08

if not do it again

27:11

this refresh it again

27:11

here refresh it okay if you refresh

27:13

we have to refresh be

27:13

and review one how to upload the file

27:16

please click on the upload button that's

27:18

click on the upload button that's it

27:31

what's that this run time files will be deleted when this is

27:35

any that is not an error that is not an error i think

27:39

that is not error not are you able to upload upload

27:43

upload in what you want to me to show you again

27:46

see see exactly what i'm doing okay i'll delete this once again

27:49

if file not

27:51

my code run k are you all right this up

27:53

this is okay this is

27:55

here here

27:57

if the file is not what will read

27:59

right

28:00

you have you've done in data frame classes in data frame i'm sure you have done it right

28:04

read c sv file is to read

28:05

you have done panda's data frame how do you read a file

28:08

your file has to be in the directory to read it right

28:11

so you're working directory

28:15

right if my file is not in the working directory

28:18

if my file is not in the working directory he will

28:18

this is it simple reading the data into a data frame right

28:22

so click on the upload button

28:23

or you can drag and drop

28:24

or you can't go

28:26

upload button click on it and just scroll down

28:29

and just scroll down

28:30

that's it

28:31

this 16th april our folder

28:33

today 16th april right

28:35

16th april right and then advertising case study

28:38

and here here we're

28:38

this for c sd

28:39

that's it

28:40

i'm just pointing to the

28:42

pie that's it

28:43

simple it

28:44

now look

28:45

there will be

28:46

just one time

28:48

process

28:49

okay most of this you're doing for the first time

28:51

okay

28:51

no problem these are small hiccups

28:53

next time onwards

28:54

no

29:00

everybody try and once you do that

29:03

you upload and then you a file upload

29:04

and then you're perfect

29:06

will be okay

29:06

this is all I'm looking forward

29:08

okay

29:08

right going forward

29:12

you

29:13

this is how you will be able to work with real data

29:16

now

29:16

now data

29:17

not just you're just

29:19

you know using my notebooks

29:20

that way load California

29:21

data

29:22

if you go to real data set

29:23

you go to Kaggle

29:24

in the Kaggul

29:25

what will be data

29:25

data is data

29:25

you'll download

29:27

you need to download

29:27

like I gave you a

29:29

advertising file

29:30

Now you want to work on case study.

29:32

Just say some of you are

29:33

and this is important

29:34

we should work on case studies, right?

29:36

Now case study

29:36

how do you have to go to some

29:38

external sites, right?

29:39

And you need to download the data.

29:41

So data

29:41

you have these of sites

29:42

it is given in a CSV file

29:44

or an Excel file.

29:45

So once you download the data

29:47

you go and you go

29:47

go ahead and upload the

29:49

other other way

29:51

but this is the simple way

29:52

to do it

29:52

what we are seeing right now.

29:55

Okay.

29:56

Okay, okay.

29:57

Good and Tribu1

29:58

you're able to do

29:59

Sangita working for you, please confirm.

30:02

And what about the rest of you?

30:02

I'm just trying to do a quick head count

30:04

to ensure everyone is able to do it.

30:07

Because here we're

30:07

this is 10 minute exercise.

30:10

By the end of it,

30:11

I want everybody to do a simple advertising

30:13

regulation, okay?

30:17

Please let me know on chat.

30:23

Where did you upload the file?

30:24

Are you able to see the same interface that I am seeing right now?

30:29

You're able to see the same interface.

30:42

And maybe I think

30:43

this is a small basic thing.

30:45

So I think I'm sure

30:45

something is wrong.

30:48

No?

30:49

What are you seeing?

30:52

Some other folder

30:53

are you showing?

30:54

Do you go to content or something?

30:56

This go to clicked.

30:58

Yes, BS code is.

30:59

Yeah, actually, yeah, if you are comfortable there is fine.

31:03

If you're comfortable in BS code, fine.

31:06

So let's go.

31:06

You want to do in BS code and fine.

31:08

What, what do you want?

31:10

VASC can be okay.

31:18

It is showing in the same interface.

31:20

Have you done a refresh?

31:22

Can you share a screenshot of your screen?

31:24

A screen shot, make us, take a snap and show me.

31:28

That will be easy.

31:29

then instead of just talking and chatting.

31:30

Just send a screenshot.

31:33

Yeah, post-refreshing

31:33

will be.

31:34

That's the refresh.

31:35

It's going to refresh.

31:36

Then it will be able to, right?

31:36

Absolutely.

31:39

And Yuvra is saying on VAS for absolutely.

31:40

It is up to your preference, what you want to do.

31:43

The reason I am we are using collab is because it's easy.

31:45

If you here, you can't access to, it's very, very powerful.

31:48

And going forward,

31:50

as I said, like I've said,

31:51

this collaboration and learning for learning for it.

31:54

If you're just from other side from

31:55

some files will get, it's very easy to work on collab.

31:59

So, having that confidence in collab is very important.

32:02

Okay?

32:04

And especially,

32:05

we'll back in Gen AIs in LLM in,

32:08

so collab is a lot more important

32:09

and it's quite easy going forward than BS4.

32:13

Yeah, but, but, but in BS4

32:14

the thing is right.

32:16

Absolutely.

32:16

You can just do it.

32:19

Okay, please try it out.

32:21

And same for you also.

32:26

No, file exploration,

32:27

you're not.

32:29

Basically, you know, I'll explain to you.

32:30

I'll explain to you where some of you might be making a mistake.

32:33

Basically, what I'll tell you, I'll tell you,

32:35

I'll tell you, I'll explain to exactly what here is problem.

32:39

It's a lot of you, this is a very common thing.

32:44

So what some of you are doing is,

32:45

you're doing is, you clicked it.

32:46

And you can't this is very common.

32:50

This is very common.

32:50

Now, as you've seen this one once clicked here,

32:53

that's it.

32:54

Now you're seeing something very different.

32:56

Now, these stuff is.

32:58

I'll tell you.

32:59

Very non-technical explanation.

33:01

This is basically Google system, right?

33:03

This is Google's machine.

33:05

Now, our machine is normal.

33:06

It's on Windows, it's, on this on, this on, this is my system.

33:12

But what you are using is not my,

33:15

this is not my system.

33:17

What you have to remember, Uvarj, is,

33:19

your working directory is,

33:21

in Python in you know, a command

33:22

of PWT of, I don't know, I don't know,

33:25

if you're aware, PWT is a command that you can use.

33:28

PWD is a command that you can use.

33:29

full form, what is? Present working directory.

33:32

You can hit PWD, and here what are you,

33:35

your present working directory, what is?

33:37

Content, slash content.

33:40

That is your working directory of collapse.

33:42

So, the other than any folders you have,

33:43

you ignore, your file's right,

33:46

that's in the content in there.

33:48

Now, you know, the view we're initially

33:50

looking at.

33:51

Yeah, this sort of messed up.

33:52

It's a bit up, because we've that up the upper

33:53

the navigation clicked.

33:56

But actually, whatever files you're uploading,

33:59

that's all right here on.

34:01

So if you go back to the other navigation,

34:05

so you can just upload your files in the content directory.

34:09

So this is not just to do anything.

34:10

If you're just refresh.

34:12

Collap to refresh it.

34:13

If you refresh it, okay?

34:16

Just refresh it.

34:17

If your view, just refresh it.

34:19

Just refresh your Google collab, exactly how I explained.

34:23

Because to the others also,

34:25

to the others also, if your navigation is something different,

34:28

for some reason, you, you have to get here,

34:32

and then you're confused okay,

34:33

so don't have to worry, what is it, forget it.

34:36

Just refresh your collab view.

34:39

Okay, just refresh your collab view.

34:40

A first browser refresh

34:42

and then you'll be able to see,

34:44

you'll be able to very clearly see the, uh, uh, this thing,

34:48

okay?

34:48

You'll have you, you'll be able to very clearly see the, uh, uh, uh, uh, uh, uh, uh, uh, uh, you can't

34:48

you can guys.

34:52

Okay, guys.

34:58

I mean, get, we're going to, we're going to use not use not here.

35:01

Get is something, huh.

35:03

Oh, that's a different thing.

35:04

Yeah, get is something.

35:05

Get, you can use can't.

35:07

That's a different thing.

35:07

That's a different thing, but, yeah,

35:08

get up use can't.

35:11

You, you have an option to connect to get to get also.

35:13

That's, well, where we are right now,

35:16

Git is,

35:17

get to you're a quite.

35:22

Okay, right?

35:22

Everybody's fine.

35:26

And Sangita and Libu,

35:28

how about you?

35:30

You were able to upload now?

35:32

It's, this is upload the button, just.

35:34

This is simple upload, just.

35:35

It's just simple upload.

35:36

And what are, what are you struggling?

35:39

Others are all done.

35:40

Can I get a confirmation to the rest of the folks?

35:46

Okay.

35:49

Let's.

35:49

We're, guys, file upload me.

35:50

We're going to be right?

35:54

Now, if there's any,

35:55

if there's any, if you're going to,

35:55

if you're going to send them,

35:57

send you, but I just want to make sure everybody is able to do.

36:01

So, okay, time, but at least give me the feedback,

36:05

that you're going to go or not going, I just want to make sure everybody's doing.

36:09

Nobody should be left out.

36:10

That's my idea, okay.

36:11

Because it's the first first time, it's okay, it's okay.

36:13

I'm not saying, you should not get stuck.

36:16

First time you're uploading a fight, it's okay.

36:18

But my thing is, if you're getting a mistake,

36:19

you're directly screenshot post.

36:21

That easy is, you know?

36:22

So instead of typing,

36:24

you next time from, what, anything.

36:26

Going forward, we will do.

36:27

lot of, you just a snap

36:28

of screen, or if you're just, just take that clipping.

36:33

Simple, it's just you take that snippet,

36:36

the sniffing tool, say,

36:36

that's the snap, that's it.

36:40

Easy way, right?

36:41

I'll give you one more solution, right?

36:42

Just in case, going forward,

36:43

your doubts or some share on screen on screen.

36:46

You will see something called sniffing tool, right?

36:48

I don't know if you know this.

36:49

Snipping tool is very simple.

36:50

Now, if you use through, okay?

36:52

This is a snipping tool, Microsoft's.

36:53

Okay?

36:54

You're a sniffing tool, use and you this part of snippet.

36:57

See, I'm teaching you that treat, okay?

36:59

Now, this one part of a snippet.

37:01

And it's not to capture, save, just copy it.

37:03

That's it.

37:04

Just copy.

37:05

Just copy can, and zoom in and paste it.

37:07

Okay?

37:08

Simple approach you can actually use.

37:10

Or you can just save it, and then you can just share that file with me.

37:15

Okay, so going forward, all of you can use this approach to share materials with us

37:19

so that you know, we have a more interactive way of talking.

37:23

Going forward, we're quite, so it will be good to interact.

37:27

So, very nice.

37:28

Now, what I'll do?

37:29

So what I will do?

37:33

Yes, very good.

37:34

Amit has already answered that.

37:36

Amit has done part of my work.

37:37

I was about to ping that queen.

37:38

So you have to drop the unnamed column, right?

37:41

So, what is the use case?

37:44

What are we trying to do here?

37:45

So we have to go and use the TV, radio and newspaper and predict sales.

37:51

This is our problem was last time.

37:53

Let me bring that up once again for you.

37:56

What is the objective?

37:57

here. The objective is that we have to, we have to look at the TV, radio and

38:07

newspaper, how much of advertising budget for TV, how much of advertising budget for radio,

38:12

how much of advertising budget for newspaper?

38:14

These three of me la, that's it. So these three inputs or output will. That's it.

38:20

That's it. That's it. It's it. It's just. It's right. This is y. This is y. Why are you? How we can't.

38:24

Well, the thing is, I'm kutk-kut-kut-seh, today. Today, we will use Gemini.

38:31

That is the reason I wanted you to use Collab.

38:33

Okay?

38:33

All of you are able to see this.

38:35

Now, all of you are able to see this. Now, we'll go ahead Germany in.

38:37

Let's use it.

38:39

So we will not do anything by our same.

38:41

Okay?

38:42

And I want to encourage this to all of you.

38:45

Okay. Now, please click on generate with air.

38:49

This peck click on.

38:51

You can. I don't mind.

38:53

You can code be can.

38:54

But you can do it through Gemini also, right? Either way.

38:59

So, generate caro.

39:02

And what I want to do? I want to drop the unnamed column.

39:06

Drop the unnamed column.

39:10

Drop the unnamed column. Drop the unnamed column.

39:15

And save in a...

39:18

In that, here we can't, we can't do, right?

39:20

This peat the Germany's not need.

39:21

Most of you already know this.

39:23

So what I will do?

39:24

I'll say demo. Drop.

39:27

And what is the code?

39:28

Unnamed 0.

39:29

This your column name.

39:31

Right?

39:35

Unnamed 0.

39:39

Axis equal to 1.

39:42

Axis equal to 1.

39:44

This is the code.

39:45

So I will drop the thing.

39:46

And what I will do?

39:48

I will save it back in demo.

39:50

This is the syntax for doing what?

39:52

This is the syntax for doing what? This is the syntax for dropping a column.

39:54

Okay.

39:54

So, this is our final thing.

39:56

Okay?

39:57

This is our final thing.

39:58

Let me ping this to all of you.

39:59

Age, what you you've done, the code to replace and just use this code.

40:04

And you will see this final data set.

40:05

This is your X, or your Y is.

40:08

Okay?

40:08

Age what I have to do?

40:10

Well, I will use the same template that I used in the last session.

40:14

Same template.

40:15

It is very important to start using templates in your classes.

40:18

Templates, what we have last class in your classes.

40:19

Templates, what we have used to use and you can solve for.

40:24

So last class template, how will be?

40:26

Go back to the, this one.

40:29

Our last session, if you go, last session was on 14th April.

40:38

Let me use that template.

40:41

So the idea is we will not code from scratch.

40:43

We will use the same template that I used in the last session.

40:47

And we'll, we'll go straight go.

40:49

Sida, we'll go to California housing on.

40:51

That's it.

40:52

This life is easy.

40:54

I will straight away take this data and work on it, right?

40:58

One second. Yeah. Yeah. This is the template I'll be using.

41:06

Min max scalar. And we will do this using a pipeline. Right. So let me, let me go and use this

41:11

template. So first, what we have to do? We have to load what is X? What is Y?

41:17

X or Y load kind of train test plate I will do. And then fit the model. That is the approach.

41:24

I will have to follow. And if you see all through the last session, it is the same approach

41:27

that we followed all through. Right? We took the data. We specified what is X and Y. And then we

41:33

build the model. If you, if you want to use this, we use it. Okay? Let's use the simple approach

41:40

for now. So let's go back. And I'm just copying this template and putting this here. That's it.

41:47

Nothing will change. Code, exactly the way's the way. All these comments and all,

41:53

this comments, you don't need require right now. Let's, let's remove all this. Just

41:59

observe, guys. I'm code in the code. I will change in the code. Now, look. Same code, right?

42:06

Only thing is that I will have to import the libraries. Whatever libraries I used here, I will have to

42:12

import those libraries. Now, this one I will have to do. But otherwise, from the code perspective,

42:16

there is absolutely no change that I did. Okay? So we just here here. Libraries import

42:22

correct but otherwise there is no other change. And what is X and what is why?

42:29

X. Okay. Demo of what? Can you see the code? Gemini is recommending me. Am I doing anything?

42:39

I'm going. What is happening here? So look. Gemini is recommending what code to type.

42:46

Okay? I'm they just saying. Are you seeing all of you? I have just imported these packages.

42:51

We have a template built. Last one class of file. We have to do. This is what I have to do, right?

42:58

SK learned the packages I'm importing. And I'm just hitting enter.

43:02

As we enter here, I'm just seeing X equal to. We have X defined right? Now, look. You know,

43:06

it's going to. Now, what? Hit tab. That's it. So Thora about spelling mistake

43:12

here. You say Y equal to sales. And that's it. There is nothing else to do.

43:21

The rest of the code is exactly the same.

43:23

If you're a little longer like it. Because of all these comments.

43:25

I'm here.

43:26

So, there is the complete code.

43:30

Okay?

43:31

Can you see?

43:32

This is our advertising case study.

43:34

Yeah, it's more be more than we can do.

43:36

But,

43:37

this per run.

43:38

What am I getting?

43:39

I'm getting a model which is giving us around 90% accuracy in training and around 90% accuracy in testing.

43:45

Okay?

43:45

If you're all this confusing look like, it, this 2F, 3F, all this nonsense, just remove this.

43:51

Okay, this is, this is used for formatting.

43:54

Most are many formatting options.

43:55

But I think this is too much confusing.

43:57

So, these stuff huddae.

43:59

This of all this.

44:00

See how I've removed all this?

44:02

There it is.

44:03

So this is just to use the formatting.

44:05

You are trying to show the data up to two decimal points.

44:08

You're both decimal point.

44:10

That is what we did in this code.

44:12

But it's not.

44:13

If you can keep it, keep the code simple.

44:16

This is our final model.

44:18

Can you see?

44:18

This our train accuracy.

44:19

If you want to show this.

44:21

a better way this is your this is your training accuracy and this is your testing accuracy

44:27

this is your testing accuracy this is your testing accuracy and more

44:35

specifically we will learn about this specific term today is it's technically

44:39

called R squared so in the last class we were talking about accuracy

44:42

dot score, so more technically we'll say R squared

44:46

so R squared I will explain to you a little bit conceptually today but this is our

44:51

all of you can see here our model here for now okay everyone can see let me ping you

44:58

the code i will explain this to you what it is but i'm sure everyone is getting a sense

45:07

all if you first run the code see if it is executing for you every part of the code is fine

45:15

concept is clear let me know

45:21

This is again the connect with the last class.

45:25

Take the data, train test split here.

45:27

Train in the model put here, linear regression.

45:30

We are trying to find the best fit line on train or we've made test

45:33

to evaluate here.

45:34

That's it.

45:35

We're getting two different scores.

45:36

Training score, testing score and we are trying to compare.

45:40

That's it.

45:40

This is what we are doing.

45:41

Okay.

45:45

Actually, you have random state one.

45:49

In case, people are using this code.

45:51

Just ignore. There's a reason I'm saying this. Don't worry. I'll tell you why this is this.

45:55

But just for now, people please take a random state of one. I just deleted that last four.

45:59

RPLL, okay? It will be easy to demonstrate some other things.

46:07

Everyone's getting it. Everyone's getting the results. Let me know, guys.

46:21

What did we do again?

46:26

If I have to explain to all of you what I did.

46:29

This is our data.

46:31

This is TV, radio, it, newspaper. This is part of my input X.

46:35

So these are my input X and this is my output Y.

46:38

So what we did?

46:39

First, X or Y separate here.

46:41

This code, you know, you know?

46:43

I mean, we're saying we drop and all the things part of my X,

46:46

this is what the code means.

46:48

Tamo.Drop axis equal to 1.

46:50

What is what is?

46:51

You're dropping the sales column.

46:52

Everything else is part of my X.

46:54

This standard syntax will.

46:55

Look, we've got the code from the other way from copy and I changed nothing.

47:00

I only changed X and Y.

47:02

And this is what I meant by the templatized way of learning.

47:05

You'll be using a lot of templates.

47:07

So this the template we're giving you to give you.

47:09

This is you can, you can't have in other problem in other Kagle external data sets

47:12

studies, you're here here.

47:15

Any data set, any problem statement you get from anywhere,

47:19

you can plug it here and you can solve it.

47:20

with, of course, with a bit of health from Gemini and all that.

47:24

Next, train test split, X train, Y train, X test, Y test, Y test, Y test.

47:29

For us k'abat, we are fitting the model.

47:32

We are getting the coefficients and intercepts.

47:34

This is your M and C values, remember.

47:37

And finally, we are getting the training and testing accuracy of our model.

47:41

Seems like a decent model, right?

47:43

Seems like a decent model for now.

47:48

Everyone's getting the results.

47:49

Let me know.

47:50

Okay, Uyraj is here, okay.

47:53

Results are matching with me,

47:55

all.

48:00

This on.

48:00

We'll go ahead two, three things I'll tell you just to extend the conversation forward.

48:04

This is a baseline model.

48:05

Want to make sure everybody reaches this point.

48:07

And then I will add a few more cells.

48:10

Just for fun, people who have done, like Yubraj, Amit, Garima, use a bit of Germany.

48:16

There on a prompt, make it better.

48:20

My result changed are because I think Trivoban, just, just, just use my same code.

48:26

You've maybe my word not made, so just use my same code.

48:29

I'll tell you the reason, because you have used a different random state.

48:31

Use my same code.

48:33

This go back and it will come.

48:37

If you remember, we have discussed about random state in the very first machine learning session.

48:43

What discussed was at that time?

48:46

We had discussed that, we had discussed that random state's training or testing data change.

48:50

changes, right? If you remember, when you use a different random state, your train data

48:55

becomes different, your test data becomes different, huh? So your trained data will be something

48:59

else, test data will be something else. That is what will happen if I take different random states.

49:05

So, so that's the reason. So, that's the reason. So, uh, so the random state change,

49:08

then, so answers will be different. No, no, I think, I think most likely, uh, your random state

49:16

is different. Now check caro, it should, it should not be different.

49:19

I'm also running the code multiple times to go one.

49:22

Your random state value is different.

49:24

Make it equal to one.

49:27

If you were, the first one I think you're using.

49:29

That's okay.

49:29

Just use my current code right now.

49:32

And just, just cross-check your random state value.

49:35

It should be equal to one.

49:39

Just use my code.

49:40

Again, just use my code.

49:48

Okay?

49:48

Other are all good.

49:49

Let me know.

49:52

Please confirm.

49:54

Everybody seen the same results?

50:19

Now, this is the baseline concept that I wanted to demonstrate to you.

50:27

We're going to go.

50:29

We'll go to same to same.

50:31

And let me do this here.

50:34

I am just copying and pasting the code.

50:36

Nothing I'm changing.

50:38

Just observe this very carefully, guys.

50:40

What I'm doing now, we here here here.

50:44

Only TV.

50:45

Look, we've no, we've just changed.

50:46

What we've just said, X equal to TV, Y,

50:49

to sales. Right?

50:56

Oh, okay, okay.

50:59

Everybody is able to see X is equal to TV, Y is equal to sales.

51:04

What do you think will happen?

51:05

We are going to get, so we are, sorry, what's that?

51:10

Oh, sorry, sorry, sorry, sorry. I have to use a double quotes, actually.

51:16

And if you take a look at the code right now,

51:19

what? It's TV. Oh, sorry, sorry, sorry. My mistake. My mistake, actually. It's a data frame, right? Yeah, my mistake. Okay. So this is, so we are actually using the TV and the sales, basically. Same thing. But the demo data frame consists of what? It consists of TV, radio and newspaper, right? And you can clearly see that when I use only one input to predict the output, I'm getting a very poor quality model.

51:47

Actual data, we have three features.

51:48

TV and radio and newspaper. So what I'm doing right now is I'm saying, see, I will only take the TV feature. X may just TV. Right now, my situation is like this where I'm saying,

52:01

that X may I only have TV, X may I only have TV, and Y may I will have sales.

52:14

This is the situation we have right now. This is your X and this is your Y. And then you are doing a

52:18

in test, and building the model, right?

52:21

Problem with this approach is that TV is not giving you the entire information about your output.

52:29

I'm an each thing in machine learning in discuss here that your output should, like, if you want to

52:35

build a good quality model, your input should contain everything for as much information as

52:41

is possible. If you input in all the things, then output, so output, you think so you're not predicted. So obviously, if you

52:48

want to predict, the company's sales, what you're only giving information about the TV.

52:54

So, your actual model not going. So again, the approach is the same, train test split. We're taking

53:02

the whole data. We are splitting into train and test. But the problem is that whatever final regression

53:09

model that we are getting, or you are here on regression model decks are you, coefficient intercept,

53:13

this is the final model we are getting. And you can relate to it now. We have seen all these things last

53:18

plus, this model is y equal to, this is and this is C, Mx plus C. But that model is not

53:26

able to learn the relationship perfectly. Why is it unable to learn the entire relationship perfectly?

53:33

Because we are only giving only a single input called TV. I'm only only only one TV input there

53:39

us to. So this model come what we're going to say. Sixty three percent training, 41% testing. It's like a

53:47

recap of last class. What do we ask you the question? Overfit, underfeit, good fit.

53:52

What do we call it, guys? When I only give the TV feature, what is the model we are getting right now?

53:58

Overfit, underfeit, good fit. Underfeit, very good. Underfitting. That means it learned nothing.

54:03

Training also, it did very poorly. Testing also, it did very poorly. That means the model has very low learning power.

54:10

Or more. Because we are only giving the TV input. Baki features are not there. Now look at the magic. Now look at the magic.

54:17

We will this. We'll improve it. This we'll put it. Okay. This we have only built a model with TV.

54:26

Second iteration. I will build the model with TV and radio. Now, look, we've just

54:31

copy-pasteed and I will just infuse radio. This is exactly what I meant yesterday. When I said we are

54:37

trying different, different iterations. So in advance, we don't know what data use

54:44

we will actually not know that. If you tell me that, sir, original data, there are three

54:50

inputs we have. So should I use all the three and build a model? Actually, we don't know. We have to

54:56

try out. We are trying to try it. We are taking TV trying to predict sales. We are taking TV

55:02

radio trying to predict sales. Or last may we will take TV, radio, newspaper and then try to predict

55:08

sales. That we'll be able. So these are all the different permutation combinations.

55:14

we will try. We are keeping the algorithm constant. If you try to relate this to the

55:20

concept that we studied, right? Machine learning core concept what is? Data, algorithm and model, right?

55:29

Algorithm, what are here here? Linear regression. We are sticking to the same algorithm, all this

55:34

file, right? Or data? Data form change. Algo is the same, right? It is the same linear regression I'm using

55:40

everywhere. Best fit line, what we studied yesterday. Algo, same.

55:44

is. But, but, but, but, but, but, yeah, correct, which feature might affect by.

55:52

So you've got your domain knowledge. If you've already from

55:54

know, you know, this input, this output, that's good. That is domain knowledge. But

55:59

then, then you will have to experiment. Not always when you know 100% sure that this will work.

56:03

Domain knowledge is definitely helpful. And, yeah, just you're trying to do IPL, like, you know,

56:09

you're trying to predict, what is the score predictor? What is the score predictor?

56:12

how score will team? Like, you should know what factors impact the score? And even

56:18

something as simple as, is it a day match, night match, evening match, is there a due factor, right? Which is

56:23

the team? What is their past historical data? What are the capabilities? What is the batting

56:28

lineup left out? Actually, they're using all of those factors to predict what the score will be.

56:32

So definitely you can use some domain knowledge, but ultimately you have to try

56:35

kind of. Just how we're here on. We will take TV, then we will take radio, then we will take TV, radio,

56:41

news, but all the combinations, we'll build multiple models and see which one works.

56:46

Okay?

56:46

So, let's go. So which TV? I'm getting a highly underfit model.

56:50

When I take TV and radio, what is happening? Let us see.

56:55

And to keep things simple, we'll make it. Okay? I think this is like,

57:00

it's, it's, it's, it's simple to make too much space. So that it doesn't take too much space.

57:04

So now, there's a lot of nothing. Simple, we've trained here. That's it.

57:10

And the code will look easy.

57:11

the same thing I'm doing about back. And finally, I will go and build the model with TV,

57:19

radio, newspaper. So can you tell me with respect to TV, TV or radio, what happened?

57:25

The model improved? When I took TV and radio together, model improved, so what will say?

57:31

Comparative, right? We will say the second model is more good fit than the first model.

57:37

Comparative, good fit. Thorough good fit, too. First model was highly under fit.

57:41

Relatively underfeit. Training become, testing become. It learned nothing.

57:46

Training also, it learned nothing. Testing also, it was very bad.

57:50

But next model is slightly better than the previous model.

57:53

Training may improvement to up or testing may be improvement to work. You can see this is better.

57:58

So this is a better quality model than what we had before.

58:01

Or if you can see, right, 89%, 89%. Now the interesting thing is,

58:06

now the newspaper in what? Newspaper in what are?

58:09

In newspaper, if you see, now you will have to tell me,

58:13

we've done done it. Now, you will have to tell me what is happening in newspaper.

58:18

Look at the numbers and tell you.

58:19

Now, numbers see and tell you, now. Now, numbers see and train accuracy or test accuracy

58:23

in the newspaper. So will I say, this is more good fit, more overfit, more underfeit?

58:29

And remember, overfitting, underfeiting is always a relative concept.

58:33

Not absolutely. I cannot say this is the perfect overfit model, perfect good fit model.

58:38

not. We have everything comparatively

58:40

is, that the first model say it's more good fitter.

58:43

First model say, it's more overfitted,

58:45

that is how I'm actually looking at the whole thing.

58:48

Okay, so anybody can tell me that the moment I use the newspaper feature,

58:52

like we this data,

58:54

the other thing is same,

58:55

which model been made, what can I say?

58:58

Is it a more good fit model, more overfit model, more underfit model?

59:03

Just see the numbers and tell me.

59:06

And this is all you will do in practice.

59:08

Now, in actual practice, in case studies,

59:09

you're doing, you'll take,

59:11

you're different models

59:12

and you'll inter-fit

59:13

how good it is.

59:18

It is showing underfit.

59:20

Look at the numbers very carefully.

59:22

I'll give a small hint.

59:23

Decimal points observe.

59:25

Okay, I'm a one more hint data.

59:26

Look at the third and four decimal point.

59:28

Here here,

59:29

3rd, 4th decimal point.

59:30

Here here, 3rd, 4th decimal points.

59:32

Look. Now you answer.

59:38

Remember, my question is, you know, let me, let me frame my question again.

59:44

If my question is not clear, let me frame my question again.

59:47

My question is as follows.

59:50

Take you time.

59:52

My question is, when I add the newspaper feature,

1:0:01

has my model become more?

1:0:08

overfit or more underfit or more good fit.

1:0:18

Okay?

1:0:19

Question clear.

1:0:20

Oftentimes the question has to be clear.

1:0:22

Now, now, let's just look at these two.

1:0:25

Comparison.

1:0:26

Compare the first one with the second one.

1:0:28

When I add the newspaper feature,

1:0:31

when the first one, when the newspaper aded,

1:0:33

then what happened?

1:0:35

The other model,

1:0:36

more fit,

1:0:37

Jada over fit, or more fit were?

1:0:39

What can you say?

1:0:40

I'll, I'll help you remember.

1:0:42

Yeah, so just,

1:0:43

Ankit says, underfeit, okay?

1:0:47

Ankit, remember, underfeit,

1:0:49

but,

1:0:50

yeah, if I answer, I'm actually answering only.

1:0:55

So, then to answer he will.

1:0:57

But I want people to think also, okay?

1:1:02

Yeah, I'm seeing some good answers.

1:1:05

But,

1:1:06

Now it is anybody's guess what is the correct answer?

1:1:08

Up to clear it.

1:1:09

I think when I framed the question,

1:1:10

up clear,

1:1:11

most of you are actually answering correctly now.

1:1:21

Okay, everybody?

1:1:23

What about the rest of you?

1:1:25

Let me hear from everybody.

1:1:27

Yugraj, what's your answer?

1:1:36

Underfit, overfit, good fit,

1:1:41

how do you know,

1:1:42

well, we did the class day before.

1:1:47

You've missed it?

1:1:48

Like, we talked about that in detail in 14th April.

1:1:51

That we did 14th April.

1:1:52

In fact, if you missed that session,

1:1:55

then, like,

1:1:56

our connect will be difficult.

1:1:58

I will ask Arshita to connect.

1:2:00

If you can help,

1:2:01

but I think he might have missed that last session.

1:2:04

So,

1:2:05

So, yeah, yeah.

1:2:08

So this full connected to Google, actually.

1:2:14

Yeah, we talked about that in detail, actually.

1:2:19

Actually, actually, I can explain.

1:2:21

I can explain, you know, like underfit model is that model,

1:2:25

which is, like, where the training and testing scores are both very low.

1:2:29

Training become and testing become.

1:2:31

That's the way you can remember underfitting.

1:2:34

Yeah.

1:2:35

Overfitting,

1:2:37

that's training is high testing is no.

1:2:39

That we're overfitting catering.

1:2:42

If you, if you want to think of a small analogy,

1:2:44

Tribhu one,

1:2:45

underfit models are those models where training accuracy is also low,

1:2:48

testing is also low.

1:2:49

That means the model actually learned nothing.

1:2:52

Kuch never seen.

1:2:53

Training may be come and testing may be coming.

1:2:55

So if you go to my 14-tapral folder,

1:2:57

we have here here here here and this is a good recap for others also.

1:3:01

Like, what is underfitting and what is overfitting?

1:3:03

This is the fundamental idea, right?

1:3:04

fundamental idea is.

1:3:07

So underfitting, overfitting,

1:3:08

I mean,

1:3:08

underfit models in

1:3:11

what are, train and test error both are high.

1:3:14

Train error is high, test error

1:3:15

is high.

1:3:16

That means, whatever model you're building,

1:3:20

revision may be fails,

1:3:22

it performs very poorly.

1:3:23

Revision in maybe,

1:3:24

it's a lot of mistakes are.

1:3:26

Or mock question paper

1:3:27

may be a lot of mistakes over here.

1:3:29

So the training and testing errors are both very high.

1:3:33

And error,

1:3:34

or, I mean, words of accuracy.

1:3:36

Training and testing error high,

1:3:38

meant training and testing accuracy are both low.

1:3:42

Two know accuracy is low, right?

1:3:44

Now, I'm saying you are you.

1:3:46

Overfitting,

1:3:46

mutter meaning.

1:3:49

I mean, underfit,

1:3:50

the model has learned nothing.

1:3:51

It's a bad model.

1:3:54

Overfitting on the contrary means

1:3:55

that the model has memorized the textbook.

1:3:59

One of a textbook memorized here.

1:4:02

So on the trained data,

1:4:03

the model has gone.

1:4:04

done very well. Training error is very less.

1:4:06

Kaffi come here. But testing

1:4:07

in the error,

1:4:08

it's like if I ask you questions from what

1:4:12

you learned, you will answer very well.

1:4:13

No error not.

1:4:15

But you actually studied nothing.

1:4:17

You've never realized not. If I asked you

1:4:20

some completely new topics,

1:4:21

you will learn be able to answer.

1:4:24

So that is overfitting,

1:4:26

growth learning.

1:4:27

Exam pre'a day, you just memorize the notes.

1:4:30

But you understood nothing, right?

1:4:32

So on the notes,

1:4:34

you will do very well.

1:4:35

But actually have you learned anything?

1:4:37

On the test, question paper, you will fail.

1:4:40

That's not correct.

1:4:41

So what we are looking for is the best model,

1:4:43

the good fit model, somewhere here.

1:4:46

And this thing we're comparatively

1:4:47

karm, that's the ideal.

1:4:51

Okay?

1:4:51

So Trigua, I hope, just wanted to recap this

1:4:53

for a little bit for you.

1:4:55

And to answer the question,

1:4:56

most of you actually answered it correctly.

1:4:58

This is actually a more overfit model.

1:5:01

Okay, now?

1:5:02

You know, the last one underfit was 63.41.

1:5:06

Now, you know, sir, this is underfit

1:5:07

can't?

1:5:08

It's a little bit more.

1:5:10

We'll do.

1:5:10

This is exactly what we try.

1:5:13

Yeah, yeah, yeah.

1:5:14

Hectic, it's just like that.

1:5:16

And the best part is,

1:5:17

Yubraj, this is not manual.

1:5:18

This can't be library is open.

1:5:20

So we're not going to that's another thing.

1:5:23

But it's for this for

1:5:24

we can program and do

1:5:25

everything, use,

1:5:27

you can just say that, please do it manually.

1:5:30

But we just say, that we do it this way.

1:5:32

Whatever you're seeing, we do it this with.

1:5:34

I'm to TV from the direct.

1:5:35

But you can actually start with radio.

1:5:37

Observe car.

1:5:38

63.41, right?

1:5:39

Now you see,

1:5:41

now if we're radio

1:5:41

from radio from, 32, 35,

1:5:44

this model is more underfeit than previous one.

1:5:47

Remember, it's more corrupt.

1:5:49

More crap.

1:5:51

Now, now, now, now.

1:5:52

Now, now, let's take.

1:5:53

Newspaper, can't,

1:5:55

more crap.

1:5:58

This is more, it's more.

1:5:58

It's more, too.

1:6:00

So, yeah, relative thing.

1:6:01

You try.

1:6:02

all possible combinations.

1:6:04

So, so, so this is more underfit.

1:6:07

Yeah, baseline, underfeit model, right?

1:6:09

This say be underfit.

1:6:10

This is underfit model.

1:6:12

When I add radio, more good fit work.

1:6:15

Training be increased, testing be increased work.

1:6:17

Right?

1:6:18

And after that, when I increase newspaper, what is happening?

1:6:22

When I include the newspaper feature, what is happening?

1:6:25

The training accuracy has increased from 89.58 to 89.59.59.59.

1:6:29

Training increase. Training increased. That means the model performed better on the trained data,

1:6:35

but on the test data, it actually become lesser. Can you see? On the trained data, the model became better.

1:6:40

Training accuracy increase. That means it is performing better on the textbook, but it is performing poorly on the question paper.

1:6:46

89.47, say 89.27. Okay, everybody can see this.

1:6:52

That's the concept. That's why we say it is more overfit. That's the idea.

1:6:56

No, 1.89, it cannot be. It cannot be. Because accuracy is always going to be from 0 to 1.

1:7:04

Look, these all values percentage in. When I say 0.89, this is the matter of 89.5%.

1:7:09

Accuracy cannot be like that.

1:7:11

Shire, your e to the power something, R-A, yeah, accuracy cannot be like that.

1:7:15

R squared will never give a value like this.

1:7:26

Yeah. No, no, 60 features, absolutely.

1:7:30

60 features, if it is there, if it's there, can we do one thing?

1:7:34

Our our use case is, today. Let's, let's talk about it then.

1:7:37

You know, in fact, I have another case study where I'm talking exactly that.

1:7:41

Okay, let's, let's pick up that discussion then.

1:7:43

I must pay, up that case study. Okay. But generally, 60 features, there are a lot of features, right?

1:7:48

A lot of features. So, your entire combinations, like you have to test.

1:7:51

You will ideally have to take all possible combinations and even have to test it.

1:7:55

X1, X2, X2, X3, X3, X4, X5, X6, X7, X8.

1:8:01

Take all possible combinations and try to test, which is the best combination.

1:8:06

That is the way how it works out.

1:8:08

Because if you remember, on the very first day I told you, in machine learning, we do not know the rules.

1:8:13

I'm a rules not. So, we have to test for me.

1:8:16

We have to try different, different combinations, and we have to see which combination works.

1:8:21

Okay, and what are the combinations we are discussing?

1:8:23

We are discussing combination.

1:8:24

with respect to data and we are discussing combination with respect to algorithm.

1:8:29

These two things I'm fixed.

1:8:31

Now we were discussing a small demo with respect to data.

1:8:34

We took TV, then we took TV radio and keeping the algo constant.

1:8:39

So we have made clear that TV and radio is the best one.

1:8:43

So we have data fixed the, okay?

1:8:45

Because when I take newspaper, I was getting overfitting.

1:8:47

So this is the best model.

1:8:49

Test accuracy highest tip.

1:8:52

Now we will try to choose the algorithm.

1:8:54

So, okay.

1:8:54

So far we are doing linear. Now we will do gradient boosting. Another algorithm we can try.

1:9:00

So let me. Yeah. Actually, yes. Again, it's not manual. There are libraries and methods for it.

1:9:09

And I think UBras, what you are referring to is a different concept. This is not related to this.

1:9:13

It's more like if you have too many features to model over three total here. So on the test score,

1:9:18

it will be low score. So on the training, it will be good and test data will be like, like,

1:9:24

it will be low sports.

1:9:25

So that's overpitting if there are too many.

1:9:27

But you know, it's like saying the same idea we are having here also, not?

1:9:30

Like, TV, radio, newspaper, you're, you're all the features

1:9:33

layer. But all the features important, in a data set, all the features are not important.

1:9:37

But if you take all the features and build a model, which is related to what you're asking,

1:9:41

you have all the features laid here, but

1:9:43

all the features important not.

1:9:45

So that also leads to overpitting.

1:9:47

So we are having too much of noise.

1:9:50

That's the thing.

1:9:50

Okay?

1:9:50

Okay.

1:9:54

Right?

1:9:55

Yeah, yeah, correct.

1:9:58

But if you have all used and model to make it, it overfeit are.

1:10:01

And if I go and write a comment, adding too many features as noise, add noise.

1:10:15

And these two overfitting.

1:10:19

Hence, we have.

1:10:23

have finalized TV comma radio for the model.

1:10:30

Okay.

1:10:32

And now, now we will try different algorithms.

1:10:41

So connect, connect, connect, take on change.

1:10:43

Everybody should connect the dots with what we studied.

1:10:46

Violet data, then we'll go.

1:10:47

Okay.

1:10:48

Now, look, different, different data combinations right here, TV, TV radio, TV, newspaper.

1:10:52

But first we've fixed, what data combination is?

1:10:55

If I take too many redundant features, then it will be a bad model.

1:11:00

Like, now, this concept is that, look, now, now, now, now,

1:11:03

newspaper, people don't know, so depending on how much money you spent on newspaper,

1:11:07

newspaper, in how much, you know, money you spent has no impact on sales.

1:11:14

Your TV budget is important.

1:11:15

People is worth watching TV, IP and all that is important.

1:11:18

Radio budget is also probably important because people still here.

1:11:21

But people hardly do it.

1:11:22

newspaper. So the amount of money you're spending on newspaper actually does not

1:11:27

impact the sales. This is the matter. So, this is important feature not.

1:11:32

Mani, here we have here we've made one more feature that, like, I don't know, like, you know, I'm

1:11:37

just giving an example. Solar flare.

1:11:42

But that, what this is? Solar flare, what's the sun's from the emission

1:11:45

are. It's a sales to take. I'm just saying, like, you might have a data set where you have

1:11:51

solar clear column. But that column has nothing to do with sales prediction, right?

1:11:55

So in a real world scenario, if you're practical data says,

1:11:59

if companies may, how we want, you will have massive amounts of data.

1:12:04

You have a lot of data. You have a very big table. Here there's

1:12:07

many inputs will, there are, many outputs are, right? But

1:12:10

all inputs important, that is what I wanted to demonstrate to this small case study.

1:12:15

So you have hundreds of inputs are. X1, X2, X3, X4, X5, up to X100. There'll be so many

1:12:21

you will have. But all these inputs will not be important. So you will have to keep trying

1:12:25

different, different combinations and try to remove some of these inputs. There is a better way to do it.

1:12:31

Part of that we will study in the session today. How do we solve these kinds of problems

1:12:35

where there are too many features? So that is the basic idea. So now, uh, feature engineering,

1:12:51

feature engineering to actually explicitly, you know, because, you know,

1:12:55

you know, Ubras, the only thing is that this is not ML.

1:12:57

Only what we are trying to do is give the general understanding of what is machine learning.

1:13:03

Ultimately, to be agentic AI course.

1:13:04

Ultimately, we'll get to that.

1:13:06

But so feature engineering is, like, it is just a fundamental idea that you should have.

1:13:14

Like, you have to try out.

1:13:16

Otherwise, there are many methods that you have.

1:13:18

If you look in the real world, how we do it,

1:13:21

there's a lot of data visualization you will do.

1:13:24

Correlations, you'll, visualizations,

1:13:26

some of the which you would have studied in Matt, plot, flip, C, bond, right?

1:13:30

You're plots carogue, scatter plots, you're.

1:13:33

You're, you'll take a call, what feature actually matters.

1:13:39

Okay?

1:13:39

So those are all the things that you do before machine learning.

1:13:43

But once you have reached machine learning,

1:13:46

we are trying to look at the workflow here.

1:13:49

Here, you have try to try to have.

1:13:51

be feature engineering or what you'll ultimately have to try out different combinations

1:13:55

and build the best model.

1:13:57

Okay.

1:13:58

Okay.

1:13:59

So now we will go and try different algos.

1:14:05

So we have to be the iteration.

1:14:07

With linear regression, I was getting this.

1:14:11

So this is using linear regression.

1:14:16

So this is using linear regression.

1:14:17

So this is using linear regression.

1:14:20

I'm getting this result.

1:14:21

So we've already solved here.

1:14:25

And now what I will do?

1:14:26

The only additional part I will incorporate is I will use a slightly different algorithm.

1:14:32

And you know we have seen this small demo last time using something called gradient boosting regressor.

1:14:40

So we will use something called gradient boosting regressor and we will be able to see this thing using gradient boosting regressor.

1:14:47

How it works out.

1:14:51

SKLearn. Ensemble.

1:14:57

Import gradient boosting regress up.

1:15:01

And you can what results I will get once I do it this way.

1:15:06

See all see the parts that I'm changing right now.

1:15:08

The parts that I'm changing, number one, I'm just importing this package.

1:15:12

I'm using a different algorithm.

1:15:13

Data is the TV radio.

1:15:15

But instead of linear regression, we use this thing use.

1:15:18

Again, do not worry.

1:15:19

This is not worry.

1:15:19

This is not.

1:15:21

not something we are seeing here, but just wanted to introduce how easy it is to try a different algorithm in psychic learn.

1:15:28

And what is the magic that has happened?

1:15:30

Now, now, what has compared to?

1:15:31

What has happened right now?

1:15:36

We have basically managed to build a more good fit model.

1:15:41

So, as we say we ML can't make in the real world?

1:15:46

Okay.

1:15:49

Everybody can take this phone.

1:15:51

This linear wall code is which most of you have done.

1:15:54

And finally, everybody can take this code and see if you're able to get the exact same results that I got.

1:16:02

Please let me know if you're able to see the exact same results that I got.

1:16:21

Oh, yeah, you know?

1:16:40

Same, you've Raj, 97% are you getting this?

1:16:51

Hello, excellent. Everyone's able to get the result? Let me know, guys.

1:17:21

get it. So simple workflow, how we try to take different, different permutation combinations

1:17:27

of data and we tried different algorithms and we were able to build a basic model.

1:17:33

All of you are getting the same result, 99%, 97% let me know. So we, we tried a few different

1:17:40

approaches. First one was highly underfit. Then us k'abahs slightly more good fit. Then,

1:17:46

huh.

1:17:51

this one is the best model that we got, 97%.

1:17:55

Okay? Yeah, good, good everybody. So let me share this with you.

1:17:59

So, okay, it's so simple. I'm I'm just share it. Okay. Advertising case study

1:18:04

will. Hardly just, uh, advertising case study.

1:18:11

Let me share this with everybody.

1:18:21

And I will just go and create the folder for up your house to access

1:18:29

connection, okay?

1:18:51

All if you can please take it from the folder advertising case study folder, I've uploaded the notes here.

1:19:12

Everyone can please take it from there, okay, all of you.

1:19:21

We didn't see the seed yet. We got the same values of accuracy.

1:19:26

Let me check.

1:19:28

Yubra, I'll take up your question.

1:19:29

But just for the rest of you, 16th April, I've uploaded the advertising case study here.

1:19:33

All of you can please look at a solution here.

1:19:36

Everyone can see this.

1:19:38

Please refer on to it and you can run the code as it is exactly the one that I discussed in the class.

1:19:43

Okay?

1:19:44

Yubra should take off your question.

1:19:45

First, uh, you're overfitting.

1:19:48

Nei, overfitting, never. Remember.

1:19:50

Overfitting.

1:19:51

is always a relative technique.

1:19:53

You are, you are just looking at the data as it is and saying,

1:19:56

sir, you overfitted because train is more than testing.

1:19:58

I told you don't to do it that way.

1:20:00

You always compare.

1:20:01

You always compare.

1:20:01

You know, make sense.

1:20:05

It is not that if train test is

1:20:06

more than overfitting, no.

1:20:09

See, let me give the analogy to you.

1:20:11

You're preparing for an exam.

1:20:13

If you're getting a high performance on your,

1:20:16

if you're getting a high performance on your textbook

1:20:19

and you're getting a low performance

1:20:21

on your mock question paper.

1:20:23

That is good, right?

1:20:24

Sorry, if you're getting a high performance on your textbook, 99%.

1:20:28

And on the mock question paper, you're getting 97%.

1:20:31

That's okay, eh?

1:20:33

Ideally,

1:20:36

textbook on a little jada ha, conceptually.

1:20:39

So that is not overfitting.

1:20:40

That's a good model.

1:20:42

Now, comparatively, you have to see what the other model kaisa.

1:20:46

The other model, when we are trying to train the model,

1:20:48

is my test going up.

1:20:51

No, no, why that way?

1:20:54

I already told you overfitting.

1:20:56

Overfitting is always relative.

1:21:00

Relative to the previous model, train jada had tests come.

1:21:02

Related to the previous model.

1:21:04

That's why we were discussing this, no?

1:21:07

That's why I was saying that when, moment you include the newspaper feature,

1:21:11

now, look, here here here 89.58, 89.59.9.

1:21:14

Hocke. Training increased work, but testing reduced work.

1:21:18

So we can say this is the more overfeit model.

1:21:21

overfitting? Right? No, no, no, no, no, that absolute comparison

1:21:28

is. I don't think I even talked about those in my sessions. No, no, no, there's no absolute. All

1:21:32

that is, some things, you know, some articles and all, they actually say,

1:21:35

that one person, 100%, 99%. But that is not correct. We always do it in the real world

1:21:40

practically. You're now, overfitting what? Overfitting what are. You, you know, overfitting

1:21:43

what? You'll do two, three definition may be. But that is not correct. Overfitting, underpitting

1:21:47

is always related. Always related. You ever, see, see, it.

1:21:51

If anybody asks you, what is overfit model? Never say, that's 100. No, that is not correct.

1:21:57

I'll tell you, I'll tell you, overrarch. This is very common thing. You'll Google

1:22:00

do, you know, every day will say, okay, train is 100. Maybe some notes also they will be given.

1:22:04

That is not correct. Why? Because your train be 100 or test be 100. Have we thought about it?

1:22:10

Now, you're preparing for an exam. You're revision here. You're revision here.

1:22:15

Your training data in accuracy, 100%. That means you're brilliant.

1:22:19

Test maybe 100%. So, yeah.

1:22:21

overfitting. So overfitting can never be judged just by looking at training.

1:22:25

Of course, training or testing both are right? Am I making sense?

1:22:32

So training accuracy, 100% is not overfitting. That's not that. It's not that

1:22:35

overfitting. So train may be 100% on it. Test may come on. Then we can

1:22:42

relatively say it is overfitting. Just because train is 100 does not mean overfitting. Okay. Yeah.

1:22:51

Okay, Hankit, just to answer to your question, we didn't use the seed yet. We got the same as accuracy.

1:23:02

Can you help me understand that? What do you mean, seed? Help me understand that. Sir, I meant both linear and gradient.

1:23:10

Yeah. Yeah, yeah, absolutely. Give us the same result. Absolutely. Because we've all same seed value used here, random state.

1:23:16

Remember, random state? We had some first discussed.

1:23:18

Random state, I mean, your train and test same.

1:23:21

If you different random states use, then our train test is, our train test is, that's the idea. That's the idea, okay?

1:23:33

If you, if it's okay with you, you just stay back for a while. So we can separately connect with you. So, okay,

1:23:39

are quite good questions. But let's move on. I'll take it up.

1:23:42

Last step, I always encourage these discussions with everybody. So, sort of. I'll stay back for everybody to do some doubt clearing.

1:23:49

General questions, leakage, what are connected?

1:23:51

Let's take it out.

1:23:52

Let's take it out. Okay. Okay. Okay. Okay. Yeah. All right. All right.

1:23:58

So now, uh, any other questions I'm missing out? Generally?

1:24:02

Yeah. So. So feature engineering.

1:24:06

Okay. So feature engineering up to us. We're a question type of. See, I'm, see, I'm, I'm

1:24:10

I'm going to do. Machine learning is a part. We've made. So all that we had here was

1:24:17

just this portion. So we actually didn't even have all these polynomial features and all that. I agree

1:24:22

with you. There are many approaches of feature engineering. But as far as our sub-topics, we are

1:24:26

actually covering only that. So as I told you, we can arrange a separate master class where we can talk

1:24:31

about it separately. But I'm 100% aligned with you that there are many other feature engineering

1:24:35

techniques. So I'm aligned with you on that. But this is all that we had in terms of data preparation.

1:24:40

So just to kind of just to be on the same page.

1:24:42

But yes, I agree with you, that there are other be methods.

1:24:44

But this, because it's not ML's course not, so we're not going to those things in

1:24:48

which is introducing you to basics.

1:24:50

And then we are getting into gen AI and agentic AI.

1:24:53

Just to answer your question there.

1:24:55

So this is our one feature engineering module.

1:24:57

Encoding, scaling, it's right?

1:25:00

Okay. And I agree with you on that.

1:25:02

That there are other methods there.

1:25:04

Okay.

1:25:05

Okay. Let's go. Let's move on.

1:25:10

And guys, I want to make all of you very comfortable.

1:25:12

Now, going forward, you do any data set, these two Kagle's very interesting data sets.

1:25:17

This is a very big data set.

1:25:18

It's a very big data set.

1:25:19

You can see. And you will find this so simple now, actually.

1:25:23

So this is what I want to encourage, how do you think through the problem?

1:25:27

We'll have the problem.

1:25:29

So, this is your data set.

1:25:31

Housing prices, data set.

1:25:32

It's a very real world data set.

1:25:34

There are like many, many features.

1:25:36

Now, look, you have to predict to the property of sale price.

1:25:40

This is the output column.

1:25:42

So we will look at all the different features of the property.

1:25:45

He was the street, locality, size,

1:25:48

how many number of bedrooms, rooms, bathrooms,

1:25:50

we want to predict what is the sale price of the property.

1:25:53

It's a regression problem, right?

1:25:55

Now, if you want to connect the dots, can we do it using the template?

1:25:59

We can do it, right?

1:26:01

Your X got, your Y, train test split, and you can build a model.

1:26:06

So you have here data in data, now, now CSV file download caro.

1:26:09

Very simple.

1:26:10

This is your CSV file.

1:26:12

Data set got, train.csv.

1:26:14

You go here.

1:26:15

You can pretty much put in the same template.

1:26:19

And this is what I encourage people to do now.

1:26:21

Now you can go to different types of these competitions and see how people are solving it.

1:26:25

You can get a cheat in the high level.

1:26:28

Okay?

1:26:28

There are many things.

1:26:29

This is, again, as I told you, machine learning is another monstrous thing.

1:26:33

But this is to get you started so that people get to know what it is.

1:26:37

Under what it is, basically.

1:26:39

Okay?

1:26:40

So this is one thing.

1:26:41

And the other great thing about Kagal is,

1:26:44

you can go to the code section.

1:26:48

These all competitions of code are.

1:26:50

So people have already solved it.

1:26:52

There are many people who already solution they're doing.

1:26:55

So you,

1:26:56

so you filter based on most voted kernels.

1:26:59

Just like I am sharing my notebooks with you.

1:27:01

There are thousands of people from across the world who have done things way better than me,

1:27:05

in fact.

1:27:06

There are a lot of data scientists better than me who are sitting here.

1:27:09

and they have given you some amazing solutions which you can follow.

1:27:12

Now, look, here here,

1:27:13

some stack regression here.

1:27:15

This is so many votes, 14,000 votes.

1:27:17

It's a very good notebook.

1:27:19

And the best part is, this is why I was telling Colab is so nice.

1:27:22

You can directly in Collabre can open to.

1:27:24

So these are downloads, VS code, all that nonsense you will not have to do.

1:27:28

Straight away, go to Kaggle, open in Collab.

1:27:30

So this is the wonderful way to learn going forward.

1:27:33

So you, you have any notebook low,

1:27:35

any competition in go and you can just see that notebook,

1:27:37

and you can just see that notebook, or you can't run it.

1:27:39

Okay, so this is a nice way to proceed ahead.

1:27:46

In real world, we will drop the columns, fill the missing value, and then input.

1:27:51

When will it come in the flow?

1:27:53

That's after.

1:27:54

Remember, first we do data cleaning, then model machine learning, right?

1:28:00

That's a thing.

1:28:01

See, that's a very good question.

1:28:03

I can take that up, you know, very briefly for you, you know, Uncate.

1:28:07

I can take that up very briefly for you.

1:28:09

Let me show you once again, the workflow.

1:28:14

Now, I help you connect the dots with that train, test, plate, and that thing that we talked about before, right?

1:28:20

Let me help you connect the dots once again with respect to whatever we talked about there.

1:28:24

Okay, so yeah, so your data got, okay?

1:28:26

Yeah, your data got.

1:28:27

So first what we discussed is you will have to split your data into training and testing, okay?

1:28:32

Yeah, your train over, you, your test, okay?

1:28:35

Any problem that you have, be it advertising, be it gaggle, any data set,

1:28:39

First, identify X, what, Y, what, okay?

1:28:43

That's the first thing that we did today.

1:28:45

For this, we tried many, many different things.

1:28:47

We first took TV, then radio, so all that will happen in the X and Y combination.

1:28:53

Once you do that, train test split, okay?

1:28:55

Us-keh, what do we do?

1:28:57

We apply all our transformations on the train.

1:29:01

Okay?

1:29:02

So, if you remember, I taught you the imputation ideas also, right?

1:29:06

And if you remember, one of the important thing that we cover,

1:29:09

there was we apply imputer dot tweet underscore transform what we did

1:29:22

imputed we did imputed we did one hot encoding um, dummies, in fact, this kind of

1:29:29

method is we do one hot encoder.

1:29:39

actually, but it's how you can you can't fit transform.

1:29:45

And finally, we have min max scalar

1:29:47

we do min max scalar. We do min max scalar.

1:29:52

Dot, pitt underscore transform.

1:29:58

These are the things that we do, right?

1:30:01

And this is what we are doing on the,

1:30:04

this is the things that we do on the training data.

1:30:06

Remember, here we're training data.

1:30:08

And we're going to what we'll, we're pre-processed.

1:30:14

Now, you'll say, sir, how we'll say, sir, how we'll do it?

1:30:17

We've discussed it, the pipeline discussed it, right?

1:30:19

You have this whole pipeline in down.

1:30:22

This is the real world way how we do it.

1:30:24

We take data, split, we're, we're in pipeline in all.

1:30:28

That's before, we data in normal experimentation

1:30:30

that, okay?

1:30:30

That's random experimentation, then we put all this in the pipeline.

1:30:34

Train may sara things do.

1:30:36

This is the processed train.

1:30:38

Okay, now it clear will all.

1:30:41

And whatever we do this,

1:30:42

now we'll read color,

1:30:44

we'll, we'll, we're same thing we,

1:30:45

we're, we're, we're, we're,

1:30:46

we're just like this clear

1:30:49

now there's nothing

1:30:49

there's not, you can go and do it.

1:30:50

You can go and do it.

1:30:54

It's all templates.

1:30:55

Same template you can do for every problem, actually.

1:30:57

Okay?

1:30:59

Now you can go and do,

1:31:01

what?

1:31:03

Dot transform.

1:31:07

So,

1:31:08

So this is all the thing

1:31:09

pipe equal to

1:31:09

go get, okay?

1:31:11

If you remember,

1:31:12

we remember, we

1:31:12

we've made

1:31:12

the pipeline

1:31:15

made, so as you

1:31:16

simply say

1:31:17

pipe dot transform

1:31:18

on test.

1:31:20

Okay,

1:31:20

so this is

1:31:21

processed test.

1:31:27

And if you

1:31:28

connect the dots

1:31:29

back to what we talked about,

1:31:31

whatever missing values

1:31:32

you learned on training,

1:31:33

you are using that

1:31:34

to substitute in the testing.

1:31:35

Whatever missing values,

1:31:37

whatever scale,

1:31:38

whatever

1:31:38

whatever min-max values you learned in training,

1:31:41

you're training in training

1:31:41

you know the main-max values

1:31:43

of the thing,

1:31:44

you're substituting

1:31:45

are we're doing.

1:31:46

You know,

1:31:47

we're seeing?

1:31:47

0 and 1

1:31:48

we've seen you

1:31:48

saw you

1:31:48

all right?

1:31:49

And now to answer

1:31:51

your question,

1:31:52

where is this

1:31:52

algorithm coming in?

1:31:54

Remember?

1:31:55

Data for pre-process

1:31:56

after your algorithm

1:31:57

is right?

1:31:58

So your algorithm

1:31:59

here will go back

1:32:00

to the black color

1:32:01

again.

1:32:02

Here it is.

1:32:03

Here it is.

1:32:03

Here you are

1:32:03

your, you're

1:32:04

your linear regression

1:32:04

dot fit

1:32:05

okay?

1:32:06

Okay?

1:32:06

Okay,

1:32:06

right?

1:32:07

Here, here,

1:32:07

here,

1:32:08

let me just say

1:32:09

linear regression.

1:32:15

So,

1:32:16

you're LR dot fit

1:32:17

you build a model.

1:32:22

Okay,

1:32:22

and here you're doing a dot predict.

1:32:25

And whatever model you are building on this,

1:32:29

here you're doing a,

1:32:30

so you're always here here pit

1:32:33

and whatever you learn,

1:32:35

you are doing a dot predict here.

1:32:36

Here here we are doing an LR dot predict.

1:32:40

We're never

1:32:41

test

1:32:41

fit not

1:32:42

we're

1:32:43

always predict

1:32:43

and we are getting

1:32:45

predictions.

1:32:50

I hope this clarifies.

1:32:51

So to answer your question,

1:32:52

Ankit,

1:32:53

you know,

1:32:55

the algorithms

1:32:56

work work

1:32:56

linear regression,

1:32:57

gradient boosting,

1:32:58

all those things

1:32:59

we are doing on the train data.

1:33:01

We are not doing that

1:33:01

on the test data.

1:33:03

So after the processing stage,

1:33:05

we are doing this.

1:33:06

Does it answer your question?

1:33:08

Here we can LR. Dot fit

1:33:09

be can't, GV.D. Fit

1:33:10

be can.

1:33:12

If you try to connect this back

1:33:13

to our advertising exercise,

1:33:15

we've

1:33:15

in advertising

1:33:15

in the way

1:33:16

we were only focusing

1:33:19

on this part.

1:33:20

So we were

1:33:20

only focusing on this part.

1:33:22

We were only

1:33:25

last week in

1:33:25

we saw,

1:33:26

we've seen

1:33:27

this one thing

1:33:27

in advertising

1:33:27

in advertising

1:33:27

not did.

1:33:29

Does it make sense?

1:33:30

But we

1:33:30

briefly

1:33:31

this could

1:33:31

make this

1:33:31

we've seen in

1:33:31

in Max Kailer

1:33:32

the pipeline

1:33:33

if you remember.

1:33:36

Connect is clear.

1:33:39

Everybody?

1:33:40

Chalo,

1:33:40

okay, move.

1:33:41

Good.

1:33:44

Let's move on.

1:33:45

I hope everybody

1:33:46

managed to follow the exercise.

1:33:49

Idea is clear.

1:33:51

And, you know,

1:33:53

let's move on.

1:33:59

And there is another very interesting, you know,

1:34:01

medical cost,

1:34:03

personal data set.

1:34:04

This is also a very,

1:34:05

very nice, you know,

1:34:06

real world.

1:34:06

case. Very nice real world use case I want to share. And now that we

1:34:10

discussed, you know, one small variation of

1:34:14

case study, if you see, medical cost personal data search,

1:34:20

joe ha up. Okay. Medical cost personal data. So this is also a very

1:34:25

interesting use case, actually. If you see here, what are we trying to do

1:34:30

primarily? What is the problem that we are trying to solve? We are looking at the

1:34:34

different features of a person and based on the different features of a person and based

1:34:36

on the different features of the person, we are trying to predict. We are basically

1:34:40

trying to predict what are the medical costs that you will incur on health insurance.

1:34:45

But the premium, what the premium? Again, the approach will be very similar. In case you want

1:34:50

to work on this data set, same way you can. Right? You're same way can do you. You can do,

1:34:54

you have data go download car. You, you're same way this way work can. So this, this is a

1:34:58

different language made. But you will realize it is such a similar kind of data set.

1:35:04

So again, the idea is that I want to, I want to.

1:35:06

encourage you to practice these things going forward.

1:35:09

So you have your data set. Can you envision the approach?

1:35:14

So much we're how to do? It's easy. It's a little. But you can see this is all your X and

1:35:19

this is your Y. This is your Y. This is your Y. This is your input X. So X. You have defined

1:35:24

Y. Y. You have defined for. Y. You train test split. Linear regression. Gradient boosting.

1:35:29

So and this is actually you can use it as an exercise. You have this to try. Use my same approach

1:35:35

that I discuss for advertising and that you look at it. So based on the different features of the

1:35:40

person, can I predict his insurance premium? How about? Now you, you have India in India.

1:35:45

What is India in India? Now, now, now, now, machine learning use not. India has. If you have

1:35:51

health insurance, it's a very rule-based system. Depending on your age, depending on your

1:35:58

medical condition, there is a fixed insurance premium you have to pay for. 10,000, $1,000,000, $1,000,000, fixed.

1:36:05

But what we are saying here is something very interesting.

1:36:07

We are saying, based on the data, we want to build a model.

1:36:11

And now, given a new customer, let's say I want to buy a premium today.

1:36:16

So if I'm a new customer or other hamco premium, then I want to go and use my features and predict

1:36:24

the premium what is the predicted premium that I will have to pay.

1:36:29

That is the problem that we are trying to solve.

1:36:32

Okay. So this is again how you can model it.

1:36:35

Yeah, yeah, absolutely. I mean, again, the approach will remain very similar.

1:36:40

Try to pick up any data set that you want related to your area of liking, that's a thing.

1:36:46

And connect, hey, Uvraz, because everything is based on it.

1:36:48

Agentic, you know, we know a lot of people who are studying LLMs and Agentic AI who actually know

1:36:52

nothing.

1:36:53

This reality, actually.

1:36:54

Industry's reality, yeah, but you guys are different because your basis in ML in.

1:36:58

And believe it or not, if you go for interviews and agentic AI, they actually ask you ML questions,

1:37:03

basic level.

1:37:03

They expect people to.

1:37:05

have some background in ML and deep learning to some extent.

1:37:08

Rather than somebody just going and using Gemini, chat, GPT,

1:37:11

he goes to go and interview, we just know GPT, chat, GPT, prompting.

1:37:16

Those are useless people.

1:37:17

Nobody will hire them.

1:37:18

But at the end of the day, people want that background.

1:37:21

So, that we are very clear that we want to give you that grounding in Python, basic data

1:37:26

science, not at a very deep level.

1:37:28

Like, machine learning, we are not trying to teach you in detail, what we are trying to at least

1:37:33

to give you the grounding key so that you know what it is.

1:37:36

And then going forward, we will see transformers, a bit of deep learning,

1:37:39

so that you have the connect, the concept what is.

1:37:42

And then you are able to build agentic systems.

1:37:45

Okay?

1:37:45

Agentic AI, you know, I'll give an example to you.

1:37:48

I do many corporate trainings also.

1:37:50

We're a one day course for a day.

1:37:51

The people who come there actually, like,

1:37:54

some HR background,

1:37:54

or some sales background in.

1:37:57

They don't know.

1:37:58

They can only a tool learned.

1:38:01

Excel like a tool learned.

1:38:02

Okay, but obviously you don't want to learn that way, right?

1:38:07

So you have to build.

1:38:08

You're a developer.

1:38:10

You are not trying to be an off person.

1:38:12

So that is the whole idea why we are looking at these fundamentalists.

1:38:15

Chalo, let's go.

1:38:18

Now we will see a very, very interesting concept called regularization.

1:38:22

And I told you from the beginning,

1:38:23

that's the day, there's a very strong connect with the last class.

1:38:27

So all this recap will be very helpful because you will be able to connect the dots.

1:38:31

So first first,

1:38:32

what is the meaning of overfitting? Let us see that. And let us start with this case study.

1:38:37

Today I will drive the session in a very case study oriented manner. So case study

1:38:41

means a notebook laying in the same way as we have done before. So we'll take a simple data set

1:38:46

right now. And I have already uploaded this one. Okay. So everything is. You can please go and

1:38:53

navigate to the 16th January folder, a 16th April folder. And you can please refer on to it.

1:39:02

So first thing that I will do is I will show you the data set right now.

1:39:11

And here I've just simulated a data set.

1:39:13

What we've just created a sample data.

1:39:18

Something very similar to what you were as you were saying.

1:39:21

You were actually telling me that, sir, I want a very big data set with lots of features.

1:39:25

So we've got this is how things will be in the real world.

1:39:29

You have 80 features.

1:39:31

But this is how things will be in the real world.

1:39:32

This is simulated data. So actually, Python, a function is called make underscore regression.

1:39:41

You don't have to get very deep into it. But just remember, we're this function use

1:39:45

and we can use something called make underscore regression. And we have something called make underscore

1:39:51

regression. And we have something called make underscore classification. So you have this function

1:39:57

use and you can actually create synthetic data. So, you can actually create synthetic data. So

1:40:02

You can here down sate how many rows will be there, how many informative features will be there.

1:40:08

All this you can see me that.

1:40:10

Anyways, what I wanted to show you is the end result.

1:40:13

That there are 30 features and there are 30 inputs that we have right now.

1:40:18

And based on these 30 inputs, we are trying to predict some output.

1:40:24

Or output, if you want to see, this is how the output will look like.

1:40:26

They see how the output is.

1:40:28

Output is, let's say the price of a house or something.

1:40:30

Now, when there are this.

1:40:32

This many number of features, what will happen guys is, I'll get back to the technique that

1:40:38

we have studied before, train test plate and we build the linear regression model. We've already

1:40:43

talked about this part. If you do this right now, what will happen? Your training score is coming

1:40:49

100% and your testing score is coming 85%. This is kind of like an overfit model.

1:40:56

That means we have learned the patterns on the training very well. But on the time, on the

1:41:02

data we are lacking.

1:41:06

So this is what is going on right now.

1:41:08

We are seeing a tremendous amount of overfitting.

1:41:12

Right?

1:41:14

So now,

1:41:15

this pe concept is what happened behind the scenes.

1:41:20

And what happened is exactly what we saw in the advertising data set.

1:41:24

Advertising in the advertising in the thing in actually.

1:41:27

You took TV, you took radio, you took newspaper.

1:41:30

Now, in newspaper, the amount of,

1:41:32

of money that a company invest on newspaper will not have the amount of company,

1:41:40

the amount of money the company invests on newspaper advertising, I'm sorry, will not have

1:41:45

too much impact on sales.

1:41:46

That space sales pay impact not.

1:41:49

So similarly, when we built the model using all the features overfeit, because newspaper was a

1:41:55

useless follow.

1:41:57

Similarly, here here the data set, there are so many features we have.

1:42:00

One feature, one cell, features 80, a feature.

1:42:02

80 features have we have, right?

1:42:05

If you look, 80 features have we try to take all the 80 features and build a model,

1:42:12

we are getting a tremendous amount of overfitting.

1:42:14

We're getting a tremendous amount of overfitting, right?

1:42:17

Because these are all features important not.

1:42:19

That we have we made, we simulate here, right?

1:42:21

Only five are important.

1:42:23

The other, the 75 useless features.

1:42:25

We have already argument there.

1:42:27

That back 75 features are bad.

1:42:30

So we are getting a highly overfit model.

1:42:32

And the reason what happened here is because if you look at the weights, right?

1:42:41

Just remember this part.

1:42:42

Just remember.

1:42:43

This pay jada of mathematically merge out.

1:42:45

So this is again that, you know, I'm just trying to talk about in terms of the content that is frame,

1:42:50

but you don't have to get into this in detail, a mathematical change.

1:42:54

If you get a little deeper into this right now, the model tried to memorize the training data.

1:43:01

And if you don't have to wait.

1:43:02

the weights have become kind of like this.

1:43:07

So the weights have to some extent become something like this.

1:43:11

See how wildly the numbers swing.

1:43:13

Some are massively positive.

1:43:14

Some are massively negative.

1:43:18

See, I'll give you a very small, uh, intuitive understanding.

1:43:23

We're,

1:43:24

we're not going to give you, but I'll give you an intuitive understanding to you.

1:43:28

So let's say for a minute,

1:43:30

Now, you have our four data points, okay?

1:43:34

One, two, two, three, three, four, nine.

1:43:37

Somebody had discussed here last time, right?

1:43:39

This is a very nice website.

1:43:41

Here we interactively see things, dexed you.

1:43:43

Desmos calculator.

1:43:44

We can try this out later.

1:43:46

So, we have four data points, okay?

1:43:49

One comma two, two, two, three, three, four, four, nine.

1:43:53

And our objective is that you want to fit a, you want to fit a linear regression model on this data.

1:43:58

This is your objective, right?

1:44:00

So how do we fit a linear regression, you know, modeled on this data?

1:44:05

Best fit level.

1:44:07

So what you need to do?

1:44:09

We will have to, we will simply go and type the, type this thing.

1:44:13

Okay?

1:44:14

Again, don't worry.

1:44:15

I mean, this is what it will do.

1:44:17

Now, if you take a look at it, best fit line is, or maybe you can tweak.

1:44:22

You can tweak it.

1:44:23

You can tweak it.

1:44:24

This is not best fit.

1:44:27

But if you try to fit all the point.

1:44:30

points perfectly, if your objective is not, sir, we're all the points

1:44:33

fit to fit all the points perfectly, what you will do?

1:44:38

You will want to build a line like this.

1:44:40

Then you are trying to fit everything perfectly, right?

1:44:42

So if you are trying to fit everything perfectly, see what is happening.

1:44:47

I'm intuitively, again, this is the mathematical concept.

1:44:50

If you're trying to fit everything perfectly, your model could be this is

1:44:53

that's the line's slope is, the weight is, the value of M is increasing drastically.

1:45:00

Can you see 2.8?

1:45:01

So just because there is an outlier data point,

1:45:05

just because there is an outlier data point to cover that particular point,

1:45:09

just to make sure that you are able to model that point accurately,

1:45:14

the slope is getting drastically impacted.

1:45:19

I'm just trying to give the intuition.

1:45:21

This is what is happening in a simple linear regression model.

1:45:25

Slope, jada ho-jada.

1:45:28

Same thing if you try to collect the dots.

1:45:30

here. This is the same data set of back.

1:45:32

80 features and output we are trying to predict.

1:45:34

We are already seeing overfitting.

1:45:36

There are many useless features.

1:45:38

Why it is behind the scenes, why it is happening?

1:45:41

Because if you see, if you see the weights,

1:45:46

which the coefficients, weights, much the coefficients,

1:45:48

M, you will see it assigned massive, crazy weights to the features that actually

1:45:54

don't matter.

1:45:56

Yeah, we're trying to.

1:45:58

So it actually,

1:45:59

assigned massive, crazy coefficients to features which don't matter.

1:46:03

The slopes are very high for some of those features.

1:46:06

And if you take a look at it, some features, the weights are 51,

1:46:09

one, 19, or 20, or 2, 23, it's all a co-ecentcore.

1:46:12

Coefficient say, M1, M2, M3.

1:46:15

This is the problem.

1:46:17

This is exactly where the concept of regularization comes in.

1:46:21

Code in case, there is a line to substitute

1:46:23

kind of, regularization, the topic is.

1:46:26

We'll try to see the intuition.

1:46:27

What is the idea?

1:46:29

Okay.

1:46:31

Regularization is a way.

1:46:33

And if I take you back to my, you know, the content that we discussed before, just a second.

1:46:40

If I quickly take you back to my content before, just a minute.

1:46:49

Let's try to draw the connection with respect to what is regularization.

1:46:53

So this was what we saw last session.

1:46:55

If we're here here here regularization to add, just remember.

1:46:59

Just remember, again, it's not that we are doing a new topic.

1:47:04

It's a whole connected, okay?

1:47:05

This is.

1:47:06

It's a new topic not.

1:47:07

Just remember,

1:47:09

you know, you this thing ignore

1:47:10

and you

1:47:11

and you this thing ignore

1:47:14

that's it.

1:47:17

I'll help you

1:47:17

see this for a minute.

1:47:22

Just ignore these two terms.

1:47:24

Because it's not connected

1:47:24

is more things.

1:47:27

And neighbors is something we are not discussed here.

1:47:29

So.

1:47:31

And, and this is where the regularization part will come in.

1:47:36

Everybody can see.

1:47:38

Now, look, now if I go and add the feature, this is, this is where we are doing regularization.

1:47:48

So I will say this is less regularization.

1:47:59

And this is high regularization.

1:48:09

Okay, this is exactly what I want you to remember for now.

1:48:13

So regularization is a way to reduce the power of the model.

1:48:17

Now, your question is, sir, regularization is what, sir, regularization is to, okay?

1:48:22

Regularization in simple words, is to reduce the, the, the,

1:48:29

power of the model.

1:48:36

Reduce the power,

1:48:36

what I mean, reduce the complexity.

1:48:38

So we go home overfitting, underfitting,

1:48:40

underpitting, so let us discuss that.

1:48:43

So,

1:48:43

let's say that example, I want you to pause and just look at this for two to three minutes also.

1:48:50

We have 80 features, okay?

1:48:52

Acki features, many features are useless features,

1:48:55

which will be in the real world.

1:48:56

Like, the newspaper-wala feature.

1:48:58

It was a bad feature.

1:48:59

When I use all the features together and build a model,

1:49:01

that model overfit will.

1:49:04

That model is a lot.

1:49:06

If you don't put any constraints,

1:49:09

you're all features like a model

1:49:11

are you, right?

1:49:13

So when you do that,

1:49:15

when you don't have any constraints,

1:49:17

the linear regression model will be highly overtly.

1:49:20

As we're just as we've seen in visualization in,

1:49:22

I told you that if you have the outlier,

1:49:25

the weights will increase too much,

1:49:27

the coefficients will increase too much.

1:49:29

it will overfit.

1:49:30

It will try to do whatever it can to fit all the points perfectly.

1:49:36

So when you have an overfit model,

1:49:39

if you have a powerful model

1:49:41

have,

1:49:43

but powerful means that it's not that it's doing too well on training.

1:49:49

But not good on training, but not good on testing.

1:49:50

It's memorizing.

1:49:52

That much power I don't need.

1:49:54

So I want to reduce the power.

1:49:55

I want to constrain it a little.

1:49:58

So what we'll do.

1:49:59

I'm its power reduce and that process is what is called regularization.

1:50:05

Regularization is the process of reducing the power of the model.

1:50:08

Now, content, we do we know,

1:50:09

it's for linear regression topic in discuss here.

1:50:11

But remember, regularization is a generic concept.

1:50:14

Machine learning, regularization gets used in many other places.

1:50:18

So conceptually, you should understand

1:50:20

it is a way to reduce the power of the model.

1:50:25

If model is overfit, we can make it more.

1:50:29

towards good fit.

1:50:31

If we've got more power reduced

1:50:33

then we're underfeit

1:50:34

to make it.

1:50:35

There's no power

1:50:35

he can not learn on me.

1:50:39

So two extremes are.

1:50:39

One extreme is that.

1:50:41

There's a lot power.

1:50:42

Model has a lot of power.

1:50:44

Let me, you know,

1:50:45

let me use two other high power model.

1:50:48

And I will say no constraints.

1:50:50

You can,

1:50:50

you can, you know,

1:50:51

all the terms, right?

1:50:53

No constraints.

1:50:54

This is like a, you know,

1:50:55

this is like a small kid.

1:50:57

You don't, you don't have any

1:50:59

discipline around the field.

1:51:00

So the kid is jumping here and there and, you know,

1:51:02

weights are high like that.

1:51:05

Think of it that way.

1:51:06

Temperature is very different thing

1:51:07

is similar to that.

1:51:09

Correct. It's similar to that.

1:51:27

your analogy is correct. I mean, correct. So, uh, regularization, I mean, correct. So, uh, so, the regularization,

1:51:28

mightlap. So, uh, no constraints. Uh, less regularization. Good constraint in here. You know, it's jumping up and down and all that. That's, that's, that's, that's, that's, that's actually an overfeit model. And that's, that's, that's, that's, that's, that's, that's, that's actually an overfeit model. And that's, so data.

1:51:29

right like that. Okay, that's the intuition.

1:51:32

High regularization,

1:51:33

I mean, lot of constraint.

1:51:35

Now you tie the kid.

1:51:38

Now you tie the kid with, okay, yeah, even as, let me repeat.

1:51:46

Before I repeat, I think it'll be good if everybody sees the diagram.

1:51:52

Then we'll repeat.

1:51:53

This is the whole topic in the area. This is the only theory you have for today's session.

1:51:57

That's it.

1:51:57

Okay, there's nothing. RMAC's just five minutes discussion. So that's okay. Take in it.

1:52:02

Take your time. Take five minutes. Go through this diagram, everybody.

1:52:06

Go through this diagram. Then I will repeat again again. Just go to the diagram all of you.

1:52:18

Just give it a glass. Just give it a glass. Take my diagram. All of you, then I'll discuss again.

1:52:27

Thank you.

1:52:57

Thank you.

1:53:27

Thank you.

1:53:57

Okay.

1:54:04

Okay. I hope everybody is with me.

1:54:27

once again everything else in the diagram you know we have already

1:54:31

started this last session if we have made

1:54:33

put the only new term that we are adding right now is called regularization

1:54:38

so regularization is a technique that is used to reduce the

1:54:43

overfitting in the model I'm regularization

1:54:47

you use to reduce the overfitting in the model

1:54:49

so regularization

1:54:54

is regularization.

1:54:57

We are trying to reduce the power.

1:55:00

So on one hand, we have a highly

1:55:02

overfit model.

1:55:04

And you know overfit model means a very complex

1:55:06

model, right? Very complex model.

1:55:08

Lots of twists and turns, right?

1:55:10

It will try to remember and memorize the training data

1:55:12

perfectly.

1:55:13

I've seen what is the meaning of overfitting.

1:55:16

Overfitting means it will try to memorize the training

1:55:18

data perfectly.

1:55:19

That is how we understand overfitting.

1:55:22

Very complex model.

1:55:23

high power model, very powerful model, and there are no constraints.

1:55:29

No constraints,

1:55:30

if there are some outlier data points, it will try to fit it.

1:55:35

And a warm net diagram every day.

1:55:37

The weights will increase.

1:55:39

There are no constraints.

1:55:41

Okay.

1:55:42

It's like, it's like having a small kid without any discipline.

1:55:46

So no constraints, right?

1:55:49

What do you do in scenarios when you have an overfit model?

1:55:52

So overfeit model must have less.

1:55:53

regularization.

1:55:56

So we try to reduce the power.

1:56:03

We try to reduce the power.

1:56:07

And this is the high regularization model.

1:56:10

On the other hand, underfitting.

1:56:13

Underfitting, matter, matter of no learning, simple model, very basic model.

1:56:17

The amount of regularization is very high.

1:56:21

And a lot of constraints are there.

1:56:23

So this is the other extreme.

1:56:25

I mean, here here, there's not learning in any order.

1:56:28

So on one hand, too much learning, overfitting.

1:56:31

On the other hand, no learning underfitting.

1:56:33

Regularization is that knob.

1:56:36

I told you on the very first day that there is a knob, right?

1:56:40

So think of it like that knob, that you're rotating.

1:56:44

You're your knob.

1:56:45

You're rotating that knob.

1:56:47

If you increase the regularization, if you're regularization,

1:56:51

if you're regularization, if you're barraignment, then you're underfit.

1:56:53

that means you're putting too much of constraint.

1:56:56

Model will become very underpicked.

1:56:58

You know, your, your, your, your, your, your, your, your, your, your, your, your, your, your,

1:57:02

less regulation are you're doing, then you're not imposing any constraint model will over fit.

1:57:07

So the objective is to give just about the right amount of regularization to make it a good fit model.

1:57:16

So we have just learned a term called regularization today.

1:57:20

And yeah, we'll go ahead.

1:57:23

It's like a regulator machine.

1:57:25

Think of it that way.

1:57:25

It's like a hyper parameter.

1:57:28

And specifically for today's session, just this year, you know what if you, we will see something

1:57:32

called alpha.

1:57:34

So when alpha equal to zero, this is less regularization.

1:57:42

And alpha equal to very high, this high regularization is.

1:57:50

And what is the optimal value of alpha?

1:57:53

This is exactly what we will see in the code today.

1:57:56

So connect the concept with the code.

1:57:59

Okay, all of you.

1:58:03

So all of you are all of you?

1:58:04

Clear.

1:58:06

Okay?

1:58:06

Nothing.

1:58:07

This is not new.

1:58:07

We already saw this last session.

1:58:09

I only introduced a new term today.

1:58:10

What is regularization?

1:58:11

Regularize.

1:58:12

What is regularize?

1:58:12

I mean power to reduce.

1:58:16

A knob use the power to reduce using alpha argument.

1:58:20

Alpha argument.

1:58:20

Alpha go zero.

1:58:21

So, then regularization ain't.

1:58:22

It's the top-se-combe-over-fit over-fifah-a-go-a-a-go-a-a-go-reduced

1:58:26

power-reduce-reduce.

1:58:29

And objective what is, if zeroed, then over-fit-h.

1:58:32

If it's a very high-per-fit-huged, we have to find out something in between.

1:58:37

Okay, clear is. Everybody, let me know.

1:58:39

Please confirm on chat.

1:58:40

Yeah, alpha is a regulation hyper-parameter, you've reached.

1:58:44

Specific to linear regression that you're covering right now.

1:58:51

All of you're okay.

1:58:52

concept. The term, the terminology is clear. What is it? I'll go back to the code now, but I want to make sure this diagram is okay with all of you.

1:59:00

This diagram, okay, we'll go. If all of you are okay with this, I'll move on.

1:59:05

Please let me know on chat, everybody.

1:59:16

Okay, thank you, Ankeh. Others, others are all fine. Let me know, guys. Okay, Rajdi.

1:59:22

Let me know, all of you.

1:59:25

Just one terminology we have discussed, right?

1:59:27

Any doubts are down.

1:59:28

Please let me make.

1:59:29

Okay, eh, right?

1:59:30

Wait, guys, all of you?

1:59:31

Okay.

1:59:32

Okay.

1:59:37

See, going forward, you should build these mental models, like, uh,

1:59:46

less regularization, matter?

1:59:48

High regularization, but, underfeiting.

1:59:50

Just remember these mental models.

1:59:52

And going forward, we will try to find the best value of alpha.

1:59:57

That is what we will do.

1:59:59

Okay?

2:0:04

Let's move on, guys.

2:0:08

Okay, thank you, all of you.

2:0:10

So, we're going to connect the dots,

2:0:13

we have seen already, 80 features, model overfit.

2:0:17

Okay, so now we're, we're going to,

2:0:18

we're regularization.

2:0:21

And there are two types of regularization.

2:0:22

that we have. One is called ridge regression and there is another something called lasso regression.

2:0:28

We'll both will look from a court perspective. I mean, from a quote perspective, we'll see how it is.

2:0:35

Now, don't know the difference what is. In ridge regression, you are basically penalized for having large

2:0:41

weights. So we've already seen, when the model regularized over here, whenever the model is getting

2:0:47

regularized, see, the weights were becoming very high, right? Very high weights. That means

2:0:52

when there are outliers in the data, I just now show this to all of you,

2:0:57

when model in the outlier, the line swung up drastically.

2:1:03

This is exactly what I will penalize using something called ridge secretion.

2:1:09

So we will use ridge regression and we will use something called alpha, which I'm

2:1:13

have you. And alpha, we'll tune

2:1:17

we'll alpha to tune and if you remember,

2:1:21

how we've got, if alpha equal to 0, that means no regularization. This is the

2:1:25

regulation parameter. Alpha is a regulation parameter. If alpha is a very high

2:1:30

value, that means strong regularization. That's the idea. I think the best way to

2:1:37

understand is through, is through examples. There's nothing better to learn than through example.

2:1:42

Straight away code may change.

2:1:43

Again, you know, here we've got code way,

2:1:47

we've been having linear regression.

2:1:52

Here we are having something called ridge.

2:1:54

If I say alpha equal to zero, what is happening, guys?

2:1:58

If alpha is equal to zero, ridge will behave just like linear regression.

2:2:02

Overfitting, right?

2:2:03

Exactly the same. No impact.

2:2:06

Alpha equal to zero,

2:2:07

if you remember this diagram, alpha equal to zero means there is no

2:2:11

regularization. Overfitting.

2:2:15

There are no constraints. The model remains high power. How do we enforce the

2:2:19

constraint? We try to increase the value of alpha.

2:2:22

Now you have d'allpha to 1. We're

2:2:25

we're doing. We'll do alpha to 1 k. Alpha to 10 kore.

2:2:29

NACD, other extreme. We have you

2:2:31

one extreme if alpha is 0, that means there is no

2:2:35

regularization. There are no constraints. Model is still overfitting. It is jumping around.

2:2:39

powerful model. Okay, overfitting. But if alpha

2:2:44

more than alpha, what does it mean? That means you're exerting too much control.

2:2:48

Too much discipline, too much constraint. You are reducing the power too much.

2:2:53

So alpha, meant constraint. Regularization.

2:2:56

Alpha does, it means, you've got downed. So if you do this, what will be?

2:3:01

5742. You see the connect all of you? So we are making the model less,

2:3:06

more underfeit.

2:3:09

Okay? Now, now you.

2:3:09

can understand?

2:3:10

Now, abh, abh, if we're 10 to 10 to 12, then, we will see, if we increase the alpha more,

2:3:18

now, now, see, scores more come again.

2:3:20

50 to 38. Can you see?

2:3:22

This go more, more, more, more, more, barang.

2:3:24

Look at this, 46, 33.

2:3:25

This go more, 25, then, okay, what will?

2:3:28

Look at this, 34, 23. Can you see the connect all of you?

2:3:31

As we increase the value of alpha, as we increase the regularization, the model is becoming more and more

2:3:37

underfit.

2:3:38

Can you see?

2:3:39

Now I will make.

2:3:39

it 35. Okay. I will further make it 55.

2:3:45

Okay. Now I will make it 65. I will make it 95.

2:3:50

Yeah, what happens? Look at this. 12%, 7%. Can you see? So this is a highly, highly constrained

2:3:56

model right now. I don't even think anything will happen if I do this. And look at this, 8%, 5%.

2:4:02

This is the highly constrained model.

2:4:04

I mean, we have made this kind of, that we have made, that the train score and test score is almost,

2:4:09

close to zero. The model is learning nothing. Alpha is so high, regulation is so high,

2:4:15

this is also bad. This is exactly what I was demonstrating to you. If you make the alpha too high,

2:4:20

up to model up to simple, very low power, that he doesn't, which is what is going on right now.

2:4:25

So this is one extreme, and this can be like, you know, it can go up to infinity theoretically. And this,

2:4:31

and in the other hand, you can have zero regulation. Okay, yeah, be a bad. So what is it that you're looking for?

2:4:38

What is it that you're looking for? What is it that you're looking for? You're

2:4:39

looking for a value that is somewhat in the middle. Something like, let's say, you know, I'm just

2:4:45

giving a ballpark number, 0.2. Isn't this good? This is better than what we had before.

2:4:51

I'm a little regularized here. Zero, but we're overfitting. We've made it overfitting. We have just

2:4:57

made it 0.2. And when I get 0.2, you are seeing that the test score has increased.

2:5:03

First test score was 85%. Now, a little bit improved over, 93%. Everything in the world of machine.

2:5:09

learning is comparative. Now you have your connect go from the last example, right? Everything is

2:5:14

comparative. We try one model. We do another model. We try another technique and we see how the

2:5:19

improvement happens. So you're going to right. And this what we're doing, you might be wondering,

2:5:24

sir, do we do it manually? Actually, we don't. Okay. Your curriculum in the grid search

2:5:28

we're not. But this is, this is something that we will do programmatically over multiple iterations.

2:5:34

We're not manually not. So we'll try to programmatically do it. And we'll use

2:5:39

a loop to try different different values of alpha and we'll find out what is the best value of alpha.

2:5:45

So ideally, we're going to. So this is very basic stuff I'm talking about until now. But this is just to

2:5:50

help you understand that alpha is what? Everybody. So ridge and what is it technically doing?

2:5:57

Now what is what? To infinity is. Infinity. Anything. Which could. And so thousands to millions

2:6:03

infinity. Theoretically, there is no limit. Okay. Minimum zero will. Maximum will go to infinity.

2:6:09

So what you're going, it's going to be constrained over.

2:6:12

Okay.

2:6:12

Now, beyond the point, it doesn't matter because beyond the point, to score zero

2:6:15

but you can't

2:6:18

be constraint can't, okay?

2:6:20

Think of it that way.

2:6:22

Now the thing is that

2:6:23

the thing is that,

2:6:23

so

2:6:25

what happened. So when we had the linear

2:6:29

model, the coefficients were too high.

2:6:33

And now, you see, here on the coefficients for 51, 44, it was

2:6:35

extremely high. If I show you

2:6:37

the top 50 records,

2:6:39

Now, look, it was very, very high, right? Can you see?

2:6:42

The top 50 records, you can see? The weights were extremely high.

2:6:45

Extremely high weights we had.

2:6:47

Okay?

2:6:48

So he 111, 246, you can see. This is the problem.

2:6:52

This is exactly why linear regression was overfitting.

2:6:55

But if you go and take a look at rigid regression,

2:6:58

what it has done is it has smoothed the weights.

2:7:01

It has smoothed the weights.

2:7:02

You can see, it forcibly shrinks the weights of all the features down towards zero,

2:7:07

smoothing out crazy swings.

2:7:09

that is the reason why it is able to reduce the overfitting.

2:7:14

So when I increase the regularization parameter,

2:7:17

intuitively, it is like, I'm just trying to show you intuitively.

2:7:22

Intuitively, it is as if we are reducing the slopes.

2:7:25

Now, you this is a way, we are saying the best fit line,

2:7:28

but in a way we are reducing the slopes.

2:7:30

Best fit, abe.

2:7:32

Abibh, but we are reducing the slopes.

2:7:35

So ridge is ensuring that slopes will not be high.

2:7:38

Slopes will be less.

2:7:39

So we're going to reduce basically.

2:7:42

And you can see here here after doing rigidization,

2:7:45

uh,

2:7:45

the weights our area right now,

2:7:48

whatever weights we got right now,

2:7:49

you can clearly see the weights are a lot smaller compared to what we had before.

2:7:53

So we will not have those drastic swings that we had before.

2:7:56

Okay, it will be much smaller compared to what we had before.

2:7:59

The swings will not be, uh, will not be as drastic.

2:8:02

So that is what ridge regression will do.

2:8:04

And again, obviously from a court perspective,

2:8:06

we are able to see that the testing score is higher.

2:8:09

So definitely,

2:8:09

ridge is better than linear.

2:8:11

So normal linear regression say my scores were 85% testing accuracy.

2:8:16

But the moment I use rich regression, my scores have increased to 93% is better.

2:8:22

Now there is something else called lasso regression.

2:8:26

Yeah, be similar.

2:8:28

The best part about Rassow is that this is that this way it's going to shrink.

2:8:31

Let's see here here.

2:8:31

There's here here to work.

2:8:33

Now compare to feature one, say like a feature 10, you can compare.

2:8:37

Let's look at the top 10 features here.

2:8:39

look at the top 10 features here.

2:8:40

You compare per.

2:8:41

Feature 1 of 51.

2:8:43

Right?

2:8:43

Feature 1 of 51.

2:8:44

So how it's, it's 29.

2:8:46

Okay?

2:8:47

Feature 2 of 17.

2:8:49

17 to, you look.

2:8:51

6% reduction, right?

2:8:53

Reduction was, right?

2:8:53

Reduction was features of weights.

2:8:55

Now, what will lasso do?

2:8:57

Lasso goes to another extreme.

2:8:59

So ridge is only,

2:9:01

the ridge is only shrinking the weights.

2:9:03

That just weights for shrink are, right?

2:9:05

But what will lasso do?

2:9:06

Lassow will go to one more extreme and it will,

2:9:09

basically shrink the weights and it will crush it to zero.

2:9:17

So rich weight shrink but it keeps all of them.

2:9:20

All the features are there.

2:9:22

It is not as if any of the features are getting eliminated.

2:9:24

All the features are there in the data.

2:9:26

Right?

2:9:27

But what will lasso regression do?

2:9:29

Lasso regression will mathematically crush all the weights to exactly zero.

2:9:35

The features important is,

2:9:36

that's not the features to exactly zero.

2:9:38

And that is one very good thing.

2:9:40

So in practice, we don't use rich that much.

2:9:43

We practice, we prefer using lasso.

2:9:45

And because of this, lasso acts as a feature selected.

2:9:49

It basically deletes the garbage features.

2:9:53

I mean, you have you have 80 features, which our equation is,

2:9:56

we have made linear models made and overfitting going to,

2:9:59

so if we'll lasso can automatically remove the unimportant features.

2:10:05

So if the features are important, the lasso is automatically hathes,

2:10:07

it automatically hathed.

2:10:08

All the same to same.

2:10:09

That same alpha is, that same hyperparameter, that same overfitting, underpitting.

2:10:13

Nothing is different.

2:10:15

Only difference is, the ridge or lasso in the same.

2:10:18

Ridge in, ridge maybe weights are reduced.

2:10:20

Lasso maybe weights are reduced.

2:10:22

But lasso in what happens is,

2:10:24

the unimportant features are, its weight is full zero.

2:10:28

It's just.

2:10:29

You're back.

2:10:30

You're back here.

2:10:32

Experimented here.

2:10:33

Zero.

2:10:34

When I take alpha equal to zero, back to this, we are getting overfitting.

2:10:38

And as I increase the value of alpha, as you increase the value of alpha, we get an even better accuracy.

2:10:44

Can you see?

2:10:44

This is the best part.

2:10:46

If you look at the accuracy right now, 98% to change.

2:10:50

Actually, it's even better than ridge.

2:10:52

Okay, at ridge in the ridge may we were only getting 93%.

2:10:55

But lasso in, it is also acting as a feature selector.

2:10:58

So the moment I take point to, it is acting as a feature selector.

2:11:02

And this one, we've talked to, I told, this one is a standard thing.

2:11:05

If you try to increase it too much, what will, model will.

2:11:08

reduce, power reduce. So we'll not do. So alpha, you have to decide

2:11:12

what value you want. If you, if you, if you, if you, if you try to, you know, go back and

2:11:17

kind of increase your alpha too much, the model will basically become overpitting, underpitting.

2:11:22

Now, look, look, you know, alpha 20% are you. It's not constrained

2:11:26

did it, it. It's a lot of regularized that the sara feature zero.

2:11:30

A great example is this one. You know, so here here. So here, basically,

2:11:34

some features back in here. So, all the zeroed. So it's extreme, right?

2:11:38

we will never do that. So this is, this is the underfitting, super underfitting.

2:11:42

So we will have to find out what is the right value. So zero be

2:11:45

corrupt. So find out what is the value in between. So the approach is clear, right?

2:11:50

So they go 95% accuracy here. Now, I'll show you the data frame and show you what are the coefficients

2:11:55

right now. You see, beautiful, right? We same feature one is. We same feature two.

2:11:59

Now, look, the features important, it's zero go. We have crushed it down to zero.

2:12:04

Which the point one, point to nine. Whatever features are not important as zero. So this is.

2:12:07

So this is acting as a very good feature extractor. So that is why lasso regression is very good.

2:12:13

So it's doing two things for me. One, it is like, it has reduced the power. It has, it has kind of

2:12:19

reduced the power of the unimportant features.

2:12:22

I mean, let me show all the 80 features. All right. You can't. Let me show you all the features for you.

2:12:30

If you look at all the features right now, you look at all the features right now. You're like, so if I show you

2:12:36

all the features, okay, you can see that all the features are effectively kind of reduced

2:12:42

overall. Okay. So this is the benefit. So again, linear regression, normal linear regression

2:12:56

will be overfitting. And if you're using some variant of region lasso regression, it is used for

2:13:01

regularizing the model. That is the idea of. So if lasso use, our model, our model to regularize,

2:13:06

that is the idea behind what lasso is. And alpha is basically the hyper parameter that is

2:13:12

used for regularization. Now alpha increase after, model for jada regularize

2:13:16

can you. That is what we are able to achieve right now. So linear overfitting, ridge.

2:13:21

The whole better was, lasso or better work. Because we here on here peaches for remove. There are many

2:13:26

unimportant features. We're having that hata deer and we are getting an even better model. And to summarize,

2:13:30

what is this thing? Overfit model, I mean, alpha is usually.

2:13:36

very low.

2:13:37

Bailqul regulation. And if I increase the alpha too much, it will go to the underpitting zone.

2:13:42

Too much regulation. So that is what we, just to summarize the conversation for all of me in the

2:13:47

class, what we talked about. Now, moving on to the code, we will see. So we have been using

2:13:56

the dot score method to see how well the model captured the mathematical pattern. Abita come

2:14:00

a dot score used here. So basically, what is that dot score? Just to, you know, intuitively understand

2:14:06

you know, that, you know, that dot's for, just to clarify what. And I hope everybody

2:14:11

kind of, just to kind of show you the visual depiction, whatever I explained right now,

2:14:15

this is your overfitting etiquette. Just to clarify. If your data points

2:14:20

is this last time also, if your data points are like this, right? If your data points are like this,

2:14:24

okay? If all, if, if you're, here point's exactly same. If your, if your model is

2:14:30

unregulated, if it's an unregularized model, then this is how the model will,

2:14:36

learn. If your non-linear model, then it will jump around everywhere. Okay, so it will try to be

2:14:42

highly overfit. It will be very, very overfit. So that's why the weights were very high. The

2:14:46

coefficients are very high. So when we do regularization, we apply a penalty. So we constrain it.

2:14:52

So that is the good thing. That's the intuition behind what regularization is as we discussed.

2:14:58

And as I told you, L2 is a, you know, is like ridge and lasso is what we discussed right now. And most

2:15:04

importantly, lasso acts as a feature selector. It acts as a feature selector. Okay. And what is the

2:15:11

parameter that we discuss? Alpha. Alpha is the parameter that we discussed. Now alpha

2:15:14

alpha go brawga, so the features that were not important, those kind of weights, that means its

2:15:21

coefficients zero will go and the features that are important, they will become strong. So that is why

2:15:27

it is, it is acting as a kind of a feature selector. That is the general idea. When to prioritize

2:15:32

This regularization, Yubraj, is when you see overfitting happening.

2:15:36

If your model overfit not, then you, you know, you don't.

2:15:39

Please remember, this is also a very important ground rule.

2:15:42

If your model in overfitting, then you don't do this. You will not do this.

2:15:47

You will do this only when you see overfitting is happening.

2:15:49

If your model in, if your data in both

2:15:52

many features, then only this is relevant. If you have only a very small amount of data, then

2:15:56

this is not very useful. Okay? Because this is to help you to reduce the power.

2:16:01

If your modely simple, underfit model, then it will not help.

2:16:07

Lasso is preferred, as I told you.

2:16:09

Rassow is preferred.

2:16:11

Lassow is preferred because you're trying to do feature selection also here.

2:16:15

Ridge generally, we do not use UBRAG.

2:16:18

And it's over over there are something called elastic net regression.

2:16:22

I can keep talking about it.

2:16:24

Elastic net what is. It combines ridge and lasso together.

2:16:27

If you're you ask, what you can't do it, actually, we're going to ask, actually, we're elastic net

2:16:30

but then again, that takes us into a different entity. But, yeah, if you generally

2:16:34

you're going to, which Rage or Lassow in a preferred, then Lassow preferred. But if you're

2:16:39

practically, what is it that you recommend, I will recommend Elastic Net to you.

2:16:45

Which we're released, Ridge or Lassow, both combined and cut. Okay? That is the key. But practically

2:16:50

Lassow is preferred because we are able to. And see, there is a cost factor also, right? As a

2:16:54

Barney, you have you have a Ssi features. If you have, if you have five features, if you are

2:17:00

having less amount of data, right? If you have less number amount of data have,

2:17:03

that's the idea. That is the idea. So that is generally appropriate. Now, let us get a little

2:17:14

deeper into what we have been discussing so far and the concept of something called R squared and

2:17:21

all this we will discuss right now. Okay. So whatever we have been discussing so far, dot score,

2:17:28

I'm conceptually you you have to help you understand.

2:17:36

So R squared is a kind of accuracy. It is basically referred to as coefficient of determination. So what is it

2:17:46

called? Just remember, yeah, you have y'adr squared is referred to as coefficient of determination.

2:17:54

Okay, you don't need to remember the mathematics. So it kind of tells you how.

2:17:58

good the model actually is. How good the model actually is. It is, it tells you how good

2:18:04

is the model overall. Okay, this is what we have been using all this while. So the moment we are

2:18:09

using dot score, dot score, we have been calling it accuracy of the model, but technically it is

2:18:15

called the R squared of the model. It tells you how well we are able to predict the Y is using the

2:18:21

excess. We have our past input access. We have put outputs Y. So how well you're able to explain that

2:18:27

variance. We are able to explain the relationship between the inputs and the outputs.

2:18:31

That is what R squared is intuitively telling you. And as you can see, one matelof perfect prediction,

2:18:37

100% accuracy and zero means very, very poor, very poor predictions. And sometimes even negative can

2:18:44

happen, which is actually even worse. So just remember, just remember. So next time, you know,

2:18:50

we have, we have a model with 85% R squared.

2:18:53

If you have model made or R squared a 85%, then that means that, you know, one way to

2:19:00

intuitively say is that the accuracy of the model is 85%. Another way to, you know, look at it would be,

2:19:07

okay, my model is able to explain 85% of the variance. So one way you can say is, okay,

2:19:14

you know, my model is 85% accurate. That is one way. So my model is 85% accurate. 85% accuracy.

2:19:21

That's a general way you can understand.

2:19:23

If you have you be able to be able to, the 85% of the variance is explained.

2:19:28

That means, let me write one more line. Let me write one more line.

2:19:34

You can see, you can intuitively say, 85% of the outputs are explained.

2:19:53

using the inputs.

2:19:56

So the way, we're explained variance. Just remember this intuitively all of you.

2:20:00

This is up our formula. There are,

2:20:02

many things, SSE, SSR, which you do not have to get into the curriculum, does not get into the

2:20:07

mathematical formulas of this. But concept is important. You should know from our

2:20:11

implementation perspective, dots for what is it? And then what is the idea? What do we mean by R

2:20:17

squared? So if anybody asks you an interview, what is R squared? Okay, it tells you how well

2:20:22

we are able to explain the outside.

2:20:23

using the inputs. Okay, 85% R2% of the time, we are able to explain the outputs

2:20:29

using the inputs. That's it. Okay? So this intuition, you know, everybody should understand

2:20:35

this basic idea. Now, yes, all right. But dot score and R squared will only tell you how well the model

2:20:44

captures the mathematical pattern. Okay. Okay. One query, we did linear and gradient progression, got overpitting.

2:20:53

Now we need to use lasso. Correct, correct, correct. Absolutely. If your overfitting,

2:20:57

no, it's not. Ani, it's not. But what I'm saying is, if you got overfitting, then you will use lasso to

2:21:04

reduce the overfitting. That understanding is correct. So if your model overfit

2:21:08

then you go to go to reduce it, to reduce the power. Now, let me give you another related idea.

2:21:14

Okay. Let me give you one more idea, Ankit.

2:21:19

If your model already is very basic, if your money is, it's a very, already a very basic, if you're a lot of

2:21:23

basic model, which has no power no power. It's a very basic model. The train accuracy, test accuracy,

2:21:29

both are 30%? 30%? Which, you're, right? Are you with me? So you cannot do lasso regression

2:21:35

on that data. Right? I hope the idea is clear. Let you see, I can, I can help you connect the dots

2:21:42

very briefly, okay? So good, good that we are asking questions. Good that you are asking questions,

2:21:47

actually. Let me help you connect the dots very briefly. So this will connect all right. Okay. Let's see that.

2:21:53

16th April, where is that?

2:21:55

This we have discussed here, advertising case study.

2:21:58

All this is. And show, show one example so that you can, you can connect the dots nicely.

2:22:02

Let's see.

2:22:06

Where is my phone? So I already got around about it.

2:22:15

Empathizing case study. Let me take this.

2:22:20

I'll just do it in my Vsport itself, right? So, so.

2:22:23

There it is, Python 3.3, 3.14. So read the data. Working drop tree is already set.

2:22:33

I just wanted to show you the concept part to all of you, okay? What is it? So that everybody is clear

2:22:37

with the basic idea. Okay. So just a, uh, okay, you have a dataset. And imagine we are only taking.

2:22:52

imagine we are only taking radio.

2:22:55

Ankhid, imagine you are taking radio to predict the same.

2:22:57

I'm giving a very basic example.

2:22:59

Now you tell me, this model what is? Overfit or Underfit model? It's very basic, right?

2:23:05

Crane be a bad, test be a bad. So this is already a very low power model.

2:23:10

Think about it. If you're

2:23:11

conceptually thought, the model already doesn't have any power.

2:23:16

We're doing demo. The train 100 was test, that.

2:23:19

I mean, it was already high power model.

2:23:21

That's got to come.

2:23:22

So regularization works in those concepts.

2:23:26

I have to adjust the levers and reduce the power.

2:23:29

If a model already less powerful, it's what do you? It's like saying if you already have somebody that is very weak.

2:23:37

We have to make it strong, right? We cannot make it weaker.

2:23:41

Got it?

2:23:42

You?

2:23:43

You have demo? Let me show the demo to you.

2:23:46

Let me add lasso here.

2:23:49

It's got lasso added.

2:23:50

There's no. There's nothing in the code.

2:23:51

code is one line.

2:23:54

So I will, so here we have reached here, sorry, here we have

2:23:57

linear regulation here. And we are getting 30 to 35, right?

2:24:01

Underfit, very bad, very, very, very low, powerful model.

2:24:05

Here you should not do regularization.

2:24:08

Because if a model is already less powerful and you try to regularize it more,

2:24:13

it'll become even less powerful.

2:24:15

Right?

2:24:16

Make sense.

2:24:16

So, now you up here here, if lasso, if you can see, you can see,

2:24:21

see it for yourself, you'll look at the math for yourself.

2:24:23

You're here plasso for two or some parameters say.

2:24:26

What will happen?

2:24:27

Okay, lasso will reduce the patterns even further.

2:24:31

Actually, here there's one feature, so it's not impact

2:24:33

not it.

2:24:33

So maybe I can take TV and radio and do it.

2:24:36

So that will be a better demo.

2:24:37

We've only a feature here, right?

2:24:39

So that's another thing.

2:24:40

You take TV and radio and radio and

2:24:42

yeah, so maybe I can take radio and newspaper and then do it.

2:24:48

This better will.

2:24:49

If I take radio and newspaper,

2:24:51

or maybe it's not the best example, actually,

2:24:53

but that's okay, that's okay.

2:24:55

So here we have a radio newspaper, okay?

2:24:57

And here if we're radio and newspaper

2:24:58

and lasso can,

2:24:59

so my model,

2:25:01

my model performance will not be that good.

2:25:05

Okay?

2:25:06

My overall model accuracy will not be that good.

2:25:09

You're here on three features load, okay?

2:25:11

So my model is not a very good fit model.

2:25:14

So here if we're lasso can, I will not get a very good result.

2:25:18

Right? Or maybe what I will do,

2:25:20

it's not the best demo, actually.

2:25:21

not the best demo.

2:25:23

What I will do?

2:25:25

This one, it's just on.

2:25:27

14th April, I did this one with you, right?

2:25:31

14th April's the notebook we shared

2:25:33

here we will see the idea very nicely.

2:25:37

Let me, let me discuss this one, briefly.

2:25:41

See this, this one.

2:25:42

We'll go all the way to the end.

2:25:47

We will go all the way to the end right now.

2:25:49

and I will

2:25:52

just a minute

2:25:53

yeah we'll go all the way to the end

2:25:56

and I will quickly show you

2:25:57

this all we've discussed

2:25:58

scroll all the way to the end

2:26:01

and we did that real world case study

2:26:06

on California housing right

2:26:07

all of you remember

2:26:08

basic California housing data set

2:26:11

we had we had many features

2:26:13

these are features

2:26:15

income housing age

2:26:16

average room bedroom population

2:26:17

and

2:26:19

we built a basic linear regression model on the basis of our data line.

2:26:24

What can we say?

2:26:25

Underfit model is the highly underfit model.

2:26:28

There were many features we had, right?

2:26:29

We had around eight to nine features.

2:26:32

And when we built a model, we got underfitting,

2:26:34

so should we apply,

2:26:36

should we apply regularization on this data?

2:26:39

We should not.

2:26:40

Because if you're you if you're

2:26:41

if you're regularization

2:26:41

can it will become more underfit.

2:26:45

It will more underfit will.

2:26:47

This we're more underfit.

2:26:48

This we have a pipeline's done.

2:26:49

So all I will do is, if I just from a code perspective,

2:26:56

show you this one,

2:27:02

regularization, if I show you,

2:27:04

if I show you, will it work?

2:27:07

It will not work actually.

2:27:08

It will give me even bad result.

2:27:10

It will remove everything.

2:27:12

If we're alpha 5 or alpha 10,

2:27:13

if you're, you know, you're, you know,

2:27:15

you're number take, look at this,

2:27:16

zero.

2:27:17

This is the perfect example.

2:27:18

So model was already under,

2:27:19

658.

2:27:21

That means when I take all the data and build a linear model,

2:27:24

it was already underfeit,

2:27:25

but it was already less power.

2:27:27

And we're here here

2:27:27

lasso and it's power more come

2:27:29

and then. So model underfit

2:27:31

is. Does it make sense?

2:27:32

Now, look, here we're alpha 1

2:27:34

if it's underfit is underfit.

2:27:35

Can you see?

2:27:36

Look at the impact it is creating.

2:27:38

So, we'll point one

2:27:39

can go, so

2:27:40

go back 4%

2:27:41

can you see? Can you believe it?

2:27:42

Can you believe the numbers?

2:27:44

So this is where lasso regression

2:27:45

does not work.

2:27:46

So if your base,

2:27:48

so this we say

2:27:49

baseline model.

2:27:50

You're the first linear

2:27:51

are linear.

2:27:52

Linear from, if the normal model,

2:27:55

if the completely basic model itself

2:27:57

is underfitting,

2:28:00

so then you will not do regularization.

2:28:02

Because, see, if you're,

2:28:04

if your,

2:28:04

if your model is already in this territory,

2:28:08

if you're further

2:28:09

power reduced, then it,

2:28:11

then it will be more underfeit

2:28:11

does it make sense?

2:28:13

That more underfeit would.

2:28:14

So my model was already,

2:28:16

you know,

2:28:17

uh, uh,

2:28:17

underpid.

2:28:18

So if you do regularization, it will become more underfeit.

2:28:21

Correct.

2:28:21

That's the, that's the, that's the, that's the conclusion of it.

2:28:24

It should not be applied to underfeit models.

2:28:27

So sometimes we think that regulation

2:28:28

so we're using, so we're all right thing.

2:28:31

And many books also have seen there.

2:28:33

They say, say, say,

2:28:33

Ridge lasso, he's brilliant, no, it's not correct.

2:28:36

Now, look here.

2:28:37

Lassow is not applicable in these kinds of cases.

2:28:41

Right?

2:28:42

This is something to be remembered.

2:28:43

All of you do.

2:28:44

And these are things you will actually do in practice.

2:28:46

When you're problem solving

2:28:47

do you know, these things are all,

2:28:49

when you'll see, sometimes these books and videos and colleges

2:28:51

in, like, you will not get the connect.

2:28:54

But you will have to solve problem.

2:28:56

That's why you have to get out of all that and you have to actually do the exercise.

2:28:59

You here here, you have to alpha values put

2:29:01

and you will get that connect.

2:29:02

You will get that connect here.

2:29:03

Alpha to, here alpha, here.

2:29:05

Alpha could be here.

2:29:06

So we should not do it.

2:29:09

Okay?

2:29:10

Make sense?

2:29:10

All of you?

2:29:11

Okay.

2:29:12

No, R programming's a lot connection

2:29:13

is another language, actually.

2:29:15

Sorry, Kunal, I did not get you a question.

2:29:17

I didn't understand, actually.

2:29:20

Our first sector, what you are trying to ask me?

2:29:24

Okay, okay, Ankit, I hope you are clear now.

2:29:27

I wanted to just talk about this to answer your question.

2:29:30

I hope everybody understood this.

2:29:32

What is it?

2:29:33

What is the correct?

2:29:39

Correct, absolutely.

2:29:41

You are correct.

2:29:42

Linear, gradient, overfitting, water, lasso, correct, absolutely.

2:29:46

Brilliant, yes.

2:29:47

Once model reaches accuracy of 85 to 90% then we should do regularization to understand

2:29:55

whether our model is good or not.

2:29:57

They 85 to 95% percent must have kha-pahe, test-me, yeah?

2:30:00

You're asking about test data?

2:30:02

Or on what data are you applying 85 to 95%?

2:30:08

Regularization, you will have test-pe, yeah, test-pay, that is your call, right?

2:30:12

If you want to apply, test-pay, if you're getting 85-95-person accuracy without

2:30:16

that, yeah, that you'll have to look.

2:30:21

See, ultimately, all the methods you will be applying together.

2:30:25

At the end of the day, all of these are indicative things that we are talking about.

2:30:29

That train data, test data, you're, you know, accuracy make on, up.

2:30:33

If it overfitting, then you have regularization care.

2:30:36

But at the end of the day, you know, what you do in practice,

2:30:39

you have a built-upon-a-template record.

2:30:42

All the things that you are doing in the class is learning.

2:30:45

you know, if you're going to be a company join, there's a made-upon-the-bara

2:30:48

there's all the thing here.

2:30:50

Linear, lasso, ridge,

2:30:53

everything will be, template there'll be.

2:30:55

And as a data scientist, you have to just know,

2:30:57

that, yeah, this applied, so it's it, so it's not.

2:31:00

You have to interpret it.

2:31:01

It is not that,

2:31:05

that ultimately,

2:31:06

all the things will, right?

2:31:09

Make sense?

2:31:11

So even if you're getting,

2:31:13

even if you're getting, even if you're getting a accuracy,

2:31:15

of 85% you will still have to try lasso and check,

2:31:19

is my accuracy reducing?

2:31:21

Yeah, increase over.

2:31:22

At the end of the day, the best model is that model

2:31:26

which has the highest,

2:31:28

highest test accuracy.

2:31:30

That you have to evaluate

2:31:31

all this while I was trying to show you,

2:31:33

that, okay, you're lasso use

2:31:34

and accuracy, if you're not using,

2:31:36

so you're not using, simple.

2:31:37

Okay, yeah, just, we're,

2:31:39

we're explaining to explain to do.

2:31:40

But, you're back you're

2:31:40

something to understand you're actually

2:31:42

implementing problems.

2:31:43

problem implementation,

2:31:45

so bugs,

2:31:46

just you will use it.

2:31:48

Linear, laso,

2:31:49

gradient boosting,

2:31:50

three, four things,

2:31:51

use, whichever gives the highest result

2:31:52

is your answer.

2:31:54

This is all this is for understanding.

2:31:55

What is it?

2:31:56

What is it doing behind the scenes?

2:31:58

Okay.

2:32:06

So, again, as I told all of you,

2:32:08

score is to help you understand the accuracy,

2:32:11

the performance of the model.

2:32:13

But stakeholders don't understand abstract scores, right?

2:32:16

If you're talking to a business stakeholder,

2:32:19

you're up,

2:32:20

up,

2:32:20

uh,

2:32:21

boss's about

2:32:21

that how good is my model,

2:32:25

right?

2:32:25

So oftentimes you'll be doing these real world problems

2:32:29

in your company,

2:32:30

in your enterprise.

2:32:31

You've got a task

2:32:32

to do something, right?

2:32:36

So what do you do in that case?

2:32:40

You cannot just say my model is 85% accurate, right?

2:32:43

Right?

2:32:44

Now,

2:32:44

85% accuracy

2:32:45

what is?

2:32:46

Yeah,

2:32:46

we've said that

2:32:47

is the R-squared

2:32:47

and percentage

2:32:49

of explained variance

2:32:50

that is something

2:32:51

we understood.

2:32:52

That 85% accuracy

2:32:53

means

2:32:54

85% of the time

2:32:56

the X is able

2:32:57

to explain the Y.

2:32:59

That is our understanding.

2:33:01

But in practice,

2:33:02

what does it mean?

2:33:04

What does it mean?

2:33:06

In terms of

2:33:07

dollar,

2:33:08

minutes, points,

2:33:09

what is the impact?

2:33:11

That boss

2:33:11

to this doesn't

2:33:12

so that is where we use something

2:33:15

called MAE,

2:33:17

mean absolute error

2:33:18

or average dollar error.

2:33:20

We're this

2:33:21

MAE

2:33:21

and what is MAE?

2:33:24

MAE stands for

2:33:25

mean absolute error.

2:33:27

So two types of metrics

2:33:28

are.

2:33:29

Okay, mean absolute error.

2:33:31

So concept

2:33:32

very simple.

2:33:34

We have residuals

2:33:35

read the last session,

2:33:36

if you remember.

2:33:37

Residual is nothing but

2:33:38

actual minus predicted.

2:33:41

So you take the whole

2:33:42

data and you build a model,

2:33:43

TARPEX best line fit

2:33:44

fit, and

2:33:46

on that basis

2:33:46

you have residuals

2:33:47

calculate

2:33:47

what is actual

2:33:48

minus predicted,

2:33:49

actual minus predicted,

2:33:51

actual minus predicted,

2:33:52

all the residuals

2:33:53

you can calculate

2:33:53

on the test data

2:33:54

that's absolute

2:33:56

value,

2:33:58

because if

2:33:58

something negative

2:33:58

or something positive

2:33:59

or something positive

2:33:59

and then you take

2:34:02

the average.

2:34:03

That is what we call

2:34:04

mean absolute error.

2:34:08

See,

2:34:08

I'll give you a real use case.

2:34:09

Let's say

2:34:10

poor delivery app.

2:34:11

We've made

2:34:11

this example

2:34:12

discussed

2:34:12

tomorrow, right?

2:34:13

So what kind of

2:34:14

regression

2:34:15

problems are

2:34:16

possible?

2:34:17

So like

2:34:18

Swiggy in

2:34:18

it,

2:34:18

we can

2:34:20

look at

2:34:20

the different

2:34:20

features

2:34:22

and we can

2:34:23

predict

2:34:24

how much

2:34:25

time it will

2:34:27

take for the

2:34:27

food to

2:34:27

be delivered

2:34:28

to you.

2:34:30

E.T.

2:34:30

estimate a

2:34:31

time of arrival

2:34:31

is.

2:34:33

This actual

2:34:34

problem you

2:34:35

solve

2:34:35

right?

2:34:37

So

2:34:37

you have

2:34:38

made a

2:34:38

model

2:34:38

and your

2:34:40

test

2:34:40

data in

2:34:41

you are getting

2:34:42

an accuracy of

2:34:43

89%

2:34:44

of the

2:34:44

means

2:34:44

what is

2:34:45

the business

2:34:47

problem

2:34:48

to have

2:34:48

that

2:34:48

Swigie

2:34:50

I'm

2:34:50

eating

2:34:51

and

2:34:51

how much

2:34:52

time

2:34:52

is

2:34:52

this business

2:34:53

problem

2:34:53

you.

2:34:54

You have

2:34:54

ordered

2:34:55

and

2:34:55

Sugi

2:34:55

is telling you

2:34:56

estimated

2:34:56

time of

2:34:57

arrival

2:34:57

is

2:34:58

this business

2:34:58

problem

2:34:59

and

2:35:00

that is

2:35:00

what

2:35:02

we are

2:35:03

discussing

2:35:04

so how do we

2:35:04

convert

2:35:05

that to

2:35:05

something

2:35:05

that has

2:35:06

meaning

2:35:06

so that

2:35:08

your

2:35:08

business

2:35:08

stakeholders can

2:35:09

understand

2:35:10

so that is what it is so we can so we can so we can say

2:35:16

on an average

2:35:17

the application is off by 4.5 minutes

2:35:20

I mean

2:35:21

what's the predicted values

2:35:22

our Swiggy

2:35:23

app

2:35:23

is that

2:35:24

can't

2:35:25

10 minute

2:35:25

in

2:35:27

20 minute in right

2:35:28

so if I have to explain to you

2:35:29

maybe

2:35:30

we can a example

2:35:31

we can

2:35:31

give

2:35:31

we're a very simple

2:35:33

thing

2:35:33

maybe two three data

2:35:35

points we can take

2:35:35

so

2:35:36

first step

2:35:36

we have taken the data

2:35:39

we have taken the data

2:35:39

and we have taken the data

2:35:39

and

2:35:40

we have built the model.

2:35:42

This we have already done.

2:35:43

This is done.

2:35:44

Now, whatever model we have built right now,

2:35:47

remember, we are using that model for doing predictions on test.

2:35:53

Predictions on test data.

2:35:58

This is we always try to find out the predictions on the test data.

2:36:04

So,

2:36:04

so this your why predicted and this your why actual cell?

2:36:09

This is the

2:36:10

predicted time

2:36:11

application

2:36:13

in Sviggi

2:36:13

what are

2:36:14

okay.

2:36:15

If you're

2:36:15

ordered

2:36:15

so

2:36:16

the app

2:36:17

you're

2:36:17

predicting

2:36:17

and this

2:36:19

are actual time

2:36:20

that

2:36:20

actually

2:36:21

the rider

2:36:21

our

2:36:21

home

2:36:22

this means?

2:36:23

That's

2:36:23

you know?

2:36:24

So,

2:36:24

your model

2:36:26

you made

2:36:26

the machine learning

2:36:27

model

2:36:27

when you're

2:36:29

evaluating

2:36:29

that on

2:36:29

real food

2:36:30

orders,

2:36:32

that's

2:36:32

in practice

2:36:33

the actual

2:36:33

food

2:36:33

are

2:36:34

we evaluate

2:36:35

and we are

2:36:35

seeing

2:36:36

okay

2:36:36

that we are

2:36:37

making 20 minutes

2:36:38

application

2:36:39

and predicted

2:36:39

but

2:36:40

30 minute

2:36:40

back.

2:36:43

This is

2:36:43

it's actually not a good

2:36:46

thing.

2:36:47

And this is

2:36:47

another thing.

2:36:49

And on the other hand

2:36:50

here

2:36:50

here

2:36:50

said it's

2:36:51

50 minute

2:36:52

will

2:36:52

but it

2:36:54

came in 20

2:36:54

minute

2:36:54

is a problem

2:36:56

maybe sometimes

2:36:57

it can happen

2:36:57

that you're

2:36:58

ordering from far away

2:36:59

so

2:36:59

Swigie

2:37:00

is saying

2:37:00

that's

2:37:00

a 50 minute

2:37:01

but

2:37:01

will be

2:37:01

but

2:37:01

he's

2:37:02

a

2:37:03

minute at

2:37:03

so that is

2:37:04

actually not a good

2:37:05

thing

2:37:05

so these are all

2:37:06

business problems

2:37:07

right

2:37:07

so if your

2:37:09

if your model

2:37:09

accurate

2:37:10

that

2:37:10

not

2:37:10

this is the

2:37:11

issue that

2:37:12

you will face

2:37:12

so

2:37:14

predicted

2:37:14

value

2:37:15

and the

2:37:15

actual value

2:37:16

is

2:37:16

that

2:37:16

differ

2:37:17

all this

2:37:19

is connected

2:37:19

to the

2:37:19

business

2:37:19

and

2:37:21

this

2:37:21

you can

2:37:21

you

2:37:22

make

2:37:23

recidual

2:37:30

you know 30 minus 20 plus 10

2:37:33

20 minus 50

2:37:35

this is minus 30

2:37:36

okay

2:37:36

now

2:37:36

take one

2:37:37

example

2:37:37

let's

2:37:38

application

2:37:39

in predique

2:37:40

it

2:37:42

is 40

2:37:43

minute

2:37:44

but it

2:37:44

actually

2:37:45

50 minutes

2:37:45

so

2:37:47

residual

2:37:47

and

2:37:48

these are your

2:37:50

residuals

2:37:50

on three test

2:37:51

data points

2:37:52

and now we can

2:37:53

calculate mean absolute error. So what

2:37:55

what is mean absolute error?

2:37:58

So

2:37:58

this

2:37:59

we're

2:37:59

this

2:38:00

we're just

2:38:02

memorize

2:38:02

it's a very simple

2:38:04

way you can

2:38:04

remember the formula

2:38:04

first you

2:38:06

calculate error

2:38:07

error

2:38:07

error

2:38:09

means

2:38:09

residue

2:38:10

calculate

2:38:10

you take the

2:38:13

absolute

2:38:13

value of the

2:38:14

residual

2:38:15

absolute value

2:38:15

means

2:38:15

sign

2:38:16

to hurt

2:38:16

just

2:38:16

absolute value

2:38:17

and

2:38:18

finally

2:38:19

you calculate the

2:38:20

mean of the

2:38:21

residuals

2:38:21

mean of the

2:38:22

absolute value

2:38:23

okay?

2:38:24

I'm

2:38:24

back from repeat

2:38:24

first

2:38:26

first

2:38:26

your data

2:38:27

you

2:38:27

you're

2:38:27

out

2:38:27

out the

2:38:30

errors

2:38:30

errors

2:38:30

we're

2:38:31

we're

2:38:32

get the errors

2:38:34

next

2:38:34

you please

2:38:35

take the

2:38:35

absolute

2:38:36

value of the errors

2:38:37

so absolute

2:38:38

value of

2:38:38

errors

2:38:39

what

2:38:40

10

2:38:40

plus 30

2:38:42

plus 10

2:38:43

we are

2:38:45

removing the

2:38:45

sign

2:38:46

and then you

2:38:46

take the

2:38:47

mean of it

2:38:47

divided by

2:38:48

3

2:38:48

50 by 3

2:38:48

50 by 3

2:38:50

50 by 3

2:38:51

15 by 3

2:38:51

what is 16

2:38:52

16.67. So if we're 16.67, so if we have our boss

2:38:57

so I will tell my boss that on an average, whatever Svigi application we have built right now,

2:39:05

on an average, our, our, our, the predicted times are 16.67 minutes of the actual.

2:39:16

That's, we don't care, because we have absolute failure.

2:39:20

But we are off by 16.5 minutes.

2:39:22

16.67, that we're like, like, you can put our numbers here.

2:39:27

Okay,

2:39:27

somebody's able to connect

2:39:28

into the business context.

2:39:30

Accuracy is for model development.

2:39:33

We are used

2:39:34

model to make model.

2:39:36

We are saying model is 90% accurate,

2:39:38

95% accurate.

2:39:39

That is for our development purpose.

2:39:41

And I also explained to you the other day

2:39:43

that accuracy and error are inversely proportional.

2:39:46

If your model

2:39:47

score is

2:39:48

more,

2:39:49

if R squared

2:39:50

is, then error

2:39:51

come, okay? So score and R squared are for model building perspective.

2:39:58

This is for model evaluation perspective.

2:40:01

So M-A-E have here. This is what it refers to.

2:40:05

Is it fine? Is the concept here? All of you?

2:40:09

Yeah, mean of residual error is called M-A-E. Correct.

2:40:11

Mean absolute error. Residuals low, absolute value low.

2:40:15

Then mean, make-lako. Okay?

2:40:19

Okay. You brush?

2:40:20

Clear-end?

2:40:21

You can connect it to other business cases also.

2:40:26

Imagine in Uber you are trying to predict what is the fair of the right?

2:40:31

You're in Uber in right booking

2:40:32

are okay.

2:40:34

Now, source location

2:40:34

you have to go here.

2:40:36

You have right booked here.

2:40:38

And there Uber is going to give you a predicted fare.

2:40:40

Uber,

2:40:40

you're your prediction data,

2:40:41

that it's how fair will right?

2:40:43

Same idea.

2:40:45

Predicted fare up,

2:40:47

actual fare you'll be,

2:40:49

residuals are, right?

2:40:50

The error is.

2:40:51

So mean absolute error, a business context,

2:40:54

I have to understand.

2:40:56

So, if error is, that means it tells you,

2:40:59

that it can be frustrating, right, money over,

2:41:03

you're booked you.

2:41:04

Your predicted fare is $200.

2:41:07

And you're, you know,

2:41:08

it's not a good thing.

2:41:11

Uber should tell you the exact fares.

2:41:14

I mean, there are many ride-hilling apps if you are starting,

2:41:16

they might initially give you a very high pair,

2:41:17

but if you're paid to fare come got.

2:41:19

So estimate should be correct.

2:41:21

is very good at it today.

2:41:23

So error in that case would mean that my predicted fare is

2:41:27

100 rupees of the actuals.

2:41:29

Oh, both caravent.

2:41:31

So that is the way we can interpret it.

2:41:32

So the concept should be important.

2:41:34

The idea should be important what error is.

2:41:37

So just to summarize the conversation,

2:41:39

we talked about two core ideas.

2:41:40

We talked about score.

2:41:42

We talked about score.

2:41:44

Okay, so we use R squared.

2:41:46

We need to compare two different models.

2:41:49

We discuss linear regression.

2:41:50

We discussed gradient boosting.

2:41:51

aggressive. We discuss linear. We discuss lasso. Comparison.

2:41:56

We're model comparison for a dot score.

2:41:58

Yeah, your dot score. And we use M-A-E when we want a business-friendly

2:42:03

explanation for every mistake that counts.

2:42:08

And R-MAC is also a very similar kind of metric. I'll come to this one in a moment.

2:42:11

What is it? Okay. So I hope the difference between R-squared is and M-A-E is absolutely clear.

2:42:17

When, what do you use are?

2:42:19

This we'll show you.

2:42:21

This is code make as a particular. Let us see that.

2:42:26

Let us see a small analogy here in the code, how it is actually implemented.

2:42:42

I'm just going to know, just a small thing is left out. We're going to see that.

2:42:51

So we'll see in the notebook how the M&E concept is implemented.

2:43:16

So we'll see in the notebook how the M&E concept is implemented.

2:43:21

compare all the training testing what we did was using sport. And here is how we are using

2:43:27

something called mean absolute error. So you can see a built-in function.

2:43:30

You have a put-in function. What I did was just explain the concept to all of you. What is

2:43:35

going on behind the scenes. I'm conceptually explained it. He was what thing is here. But you don't

2:43:41

have to get into that. You can just understand it. What is it? So we are simply computing the

2:43:46

so we are we are simply computing this particular mean absolute error.

2:43:51

So you can see the moment I run this code, you can clearly see that the linear regression

2:43:56

model is the standard linear regression, the standard linear regression, 403.55 error on average.

2:44:02

Okay, if you want to put a story around it, it's like the predicted fare is $43.55 of the

2:44:08

actual. Okay.

2:44:11

But the lasso model was better. You can't see.

2:44:15

Better model, it means less error.

2:44:17

Understand, I'm right?

2:44:18

Accuracy rather than lasso in. We already saw that. We already saw that model model.

2:44:21

better than it. So errors are lower. This is the connect. So it is business-friendly language.

2:44:28

Okay. Error for business-friendly, I explain not can't. So we're

2:44:31

what we can't understand the business stakeholder. But 16.73, you can say that the predicted

2:44:37

fare, the predicted delivery time is very different. Is 16.73 minutes different from the actual

2:44:43

delivery time. That's the intuition.

2:44:47

Okay. Everybody's with me. And finally, finally, we are using the pipeline.

2:44:51

the pipeline that we talked about before as well. If you see,

2:44:55

min-max tailor and we can't lay-said. This is the same idea that we have seen before.

2:44:59

No, we've seen here. Okay, this one thing. And the last thing that I wanted to show you

2:45:04

is to incorporate this in California housing. So this is a very interesting one again. So

2:45:08

California housing data set us that we last used. There are 20,000 640 houses. It may district

2:45:15

say. And what we have done, we have done something very interesting. We have this. We have

2:45:21

a little complicated here. So, last exercise, I said,

2:45:24

a little complicated here. So if you remember,

2:45:27

the original California housing data set here, okay, we can we

2:45:31

see them all together, let's see. The original data set here. You only had

2:45:35

you only had eight features. We only had eight features. But what we have done

2:45:41

is we have done some mathematics. We have done something called polynomials. So

2:45:46

this is a function in Python in which we can use to create complex combinations.

2:45:51

I mean, you know, you can. Some of those features actually mean nothing.

2:45:58

So actual features, we're we know, age, bedrooms, there, total rooms, that we already saw

2:46:03

day before yesterday. What we are now trying to do is, we're a data set simulation

2:46:09

we are trying to create 164 features. Okay? 164 features I'm

2:46:16

now obviously many of those features will not mean anything.

2:46:21

So we are trying to create many features, which actually mean nothing.

2:46:26

These features actually no matter. But we are trying to create all these features.

2:46:30

Now, if you take a look at it, when we build the linear regression model, it is highly

2:46:36

overfit. This is what I wanted to show you. On the last California, you know, this problem,

2:46:43

if we try to create 164 features,

2:46:47

allah, different features, some of which may not have any meaning. We are getting a highly

2:46:51

overfit model. These kinds of scenarios, lasso will work very well. So first I did linear,

2:46:58

then I'm doing lasso. And if you see, lasso is giving me an exceptionally good result. It will take a while

2:47:03

to train. Okay, the pipeline, main max scalar with lasso. Lasso will work. Why will lasso work?

2:47:10

Because the original model was a highly overfit model. Okay. So lasso will work very beautifully right

2:47:15

now. You can see. It will take a while. And you will see that the model will see that the model will be more

2:47:20

good fit than what we had before. And please remember, this is not the original

2:47:24

California housing. We have actually created a transformed data with 164 features.

2:47:30

We have a lot of redundant features had key, noisy features add here. Like, let's say, age into room

2:47:35

into income. If I ask you, it's what is the meaning of age into rooms into income? It's

2:47:40

no meaning. This feature has nothing to do with like any common sense. This we have

2:47:45

actually created polynomials. We have actually created polynomials. And school in polynomials,

2:47:49

this is that xS square, x cube, x into y. So we have actually created features like that.

2:47:54

The original columns are, we've, we've multiplied

2:47:56

made new features. And if you understand many of these features are absolutely useless.

2:48:01

And this is exactly what I'm trying to simulate what we discussed in the class today.

2:48:05

If you're up linear, overfitting it will, you're getting a much better model.

2:48:09

Now I'm not saying this is the best model. Fifty-seven percent is still very bad.

2:48:12

But this is the wonderful improvement, right? You're seeing that linear was so bad.

2:48:17

That there's nothing is right. And if you're able to, right? And if you're able to,

2:48:19

to use lasso, many of those redundant features got dropped out and you're actually getting

2:48:23

something which is really good. That's the magic of lasso regression that we got here.

2:48:29

I will pass it over to Arshita. Arshita wants to take the quiz and then I will stay back for some

2:48:34

of you if you have any questions, I'll be here, right? So machine learning is always a fun topic.

2:48:38

You know, there's always endless questions. So I'll stay back. But Arshita, I think you can take

2:48:43

over for the quiz in the meantime. Right? Yeah. Yeah. Thank you very much.

2:48:47

So this feedback poll is already live so you can fill that as well. And I will be sharing my screen for the quiz.

2:48:57

Yeah, yeah, sure. And let me just stop sharing. Thank you so much. Yeah.

2:49:05

If some of you have any questions, please stay back. Okay? I'm here. Yeah. After you done.

2:49:17

Mm.

2:49:47

Okay, let's start with the quiz now. As always, if anyone is left, you can join from the code in the chat books. You know the rules. Same as always.

2:50:11

What does Ridge Regression mainly do?

2:50:17

L2 penalty. Set some coefficients to zero. Removes outliers or uses polynomial features.

2:50:30

If you're not sure of all the options, just pick the best choice.

2:50:38

These are MCQ, so only one answer is correct.

2:50:44

Yes. Ridge adds L2 penalty.

2:50:47

Second question. What is a key effect of laser regression? Eliminates all error. Always lowers bias to zero. Only works for classification or shrinks coefficients to zero.

2:51:17

That is correct. Lazo usually shrinks some coefficients to zero.

2:51:47

Which metric penalizes large errors more strongly?

2:51:52

M-A-E, M-S-E, R-squared or median. M-A-E is mean-absute error.

2:52:01

M-S-E is mean-absolute error. M-S-E is mean-E-squared error.

2:52:04

Rest out, self-explanatory.

2:52:17

Okay, most of you are right.

2:52:24

MSC penalizes more strongly because it takes the square compared to something like MAE, which takes the absolute value.

2:52:32

Fourth question.

2:52:38

What does a high R squared usually indicate?

2:52:43

More prediction error.

2:52:46

Better.

2:52:47

scale units, no need to test or more variants explained.

2:53:17

That is correct. More variance explained. R squared is a measure of explained variance.

2:53:24

So option D is correct.

2:53:30

Which patterns suggest your model may be missing structure?

2:53:38

Residuals show a clear pattern. Training error is small. Residuals are randomly scattered.

2:53:46

or all predictions are positive.

2:54:16

a clear pattern is not. Okay. So let's look at the leader vote.

2:54:23

Croc has won the wish for today.

2:54:31

Who is Croc? Can you please put your name in the chat?

2:54:46

winner for today. Congratulations, Kashi. So thank you students. We will end the quiz here. I will hand it over back to Shianz.

2:54:57

Yeah, yeah. Thank you so much. Yeah, yeah.

2:54:59

Thank you very much for your time. I'll take your right now.

2:55:02

Yeah, sure. We will definitely look into your feedback.

2:55:05

Yeah, yeah, sure. Absolutely, guys. Yeah. So any questions? I just wanted to stay back and, you know, just take up any questions if people have here.

2:55:16

R squared is basically, to answer your question, R squared is basically more of a model, you know, R squared is basically more of a model, you know, R squared, in a way, it's more of a model evaluation metric. You're building the model and you are trying to evaluate the model on some test data. So that R squared is, whereas MAE is, you're building.

2:55:46

is an error method.

2:55:47

One is the accuracy, and the other are error.

2:55:50

Remember accuracy versus error.

2:55:51

Accuracy is giving you a score, 0 to 100%.

2:55:55

How good is the model, how accurate it is?

2:55:57

That our accuracy has.

2:55:58

Whereas error is more like telling you how

2:56:01

actual and predictor is how different.

2:56:03

Okay, right?

2:56:04

MAE is more like giving you the difference between accurate and

2:56:07

wherever the error matrix comes,

2:56:09

or MAE or RMAC,

2:56:11

that was a theoretical question in quiz

2:56:13

so RMS is another kind of error metric.

2:56:15

where the error are error is telling you the difference between actual and predicted

2:56:20

and why are we doing that because we are trying to understand from a business

2:56:25

interpretation perspective which one can be easily interpreted which one can be

2:56:31

interfered in a better so so R squared is our score is you know is is from the

2:56:38

perspective of building a model comparing whereas M is M is more from the perspective of like

2:56:45

you know, error.

2:56:46

Actual and predicted in the

2:56:47

right?

2:56:49

Yeah, yeah.

2:57:07

How to know using lasso?

2:57:10

Yeah, one second.

2:57:11

One by one, one, one, I'll take it up, take up.

2:57:14

How to know using lasso with a particular alpha doesn't underfit the model?

2:57:17

You have to try.

2:57:18

You have to try a minute, absolutely.

2:57:20

Remember, on the very first machine learning class,

2:57:23

we've made a term used here, hyperparameter.

2:57:25

You'll you know, we'll have, we had a hyper parameter, a term used

2:57:28

right?

2:57:29

And we've made one other term used called hyper parameter tuning.

2:57:33

Alpha is actually a hyper parameter.

2:57:35

So to answer your question, sir, how can't know what will know what will try

2:57:39

to try to the same way that I was manually doing a little for you,

2:57:42

that one, two, three, four, four.

2:57:44

So, by the topic, never, you know, we can, I'll show that to you in the future,

2:57:48

that we'll show that you in the future, that we can't do it.

2:57:50

We're just to tell you, that alpha, but you know, but you're just to tell you, but

2:57:54

you're just to a porridge looper run to, you can take different values of alpha and see, which is the best

2:57:59

one, or then what you can actually try to do is, you can go and kind of use something called

2:58:05

hyperparameter tuning, which will automatically try thousands of different values of alpha

2:58:09

and find out what is the right balance.

2:58:11

So that you're not to do not. It is not something that you will have to pay.

2:58:14

out and check. You don't have to do. The machine will do that for you.

2:58:18

For you, the understanding is important, that alpha to zeroed, alpha for both high

2:58:23

to underfit. What is the right balance in between the machine will figure out? That is not something

2:58:27

for humans to do. And that process, we're hyperparameter tuning. Okay. Yeah.

2:58:34

Score told already. The accuracy, then what's separate is it?

2:58:38

Yeah, so actually, correct. That, look, that's a theoretical thing. M-A-E or M-C. Absolutely right.

2:58:43

If your question is very valid, so we've

2:58:45

generally, that error means one-winous accuracy.

2:58:48

That we've generally

2:58:48

said. But it turns out that error

2:58:52

can't ever, other metrics

2:58:53

have. Now, in curriculum, we've

2:58:55

two things we've made, M-AE and M-AC.

2:58:57

And there are. I can keep talking

2:58:59

about it, RMSA, logarithmic error,

2:59:01

there are many other types of errors that we have in practice.

2:59:04

So, kher, just to stick to the content right now,

2:59:06

that M-A-E or M-C in

2:59:07

what I'll let me show you.

2:59:09

Let me show you. Because

2:59:11

the case in a question

2:59:12

I think I should,

2:59:14

let me show that to all of you.

2:59:16

Okay.

2:59:17

What is M-A-E and what is R-M-A-C?

2:59:19

What is that?

2:59:21

Let us see that.

2:59:26

So,

2:59:27

what happens behind the scenes is,

2:59:30

if you see,

2:59:32

one second.

2:59:33

Let me take you there.

2:59:38

So what is happening behind the scene says,

2:59:41

in M-A-E is

2:59:42

M-A-E is a kind of

2:59:44

error metric.

2:59:46

That means it is giving you

2:59:48

the difference

2:59:49

between the actual

2:59:51

and the predicted value.

2:59:53

Okay?

2:59:54

If you're you

2:59:54

from the formula

2:59:55

to say we first we

2:59:57

we're error

2:59:57

calculate

2:59:57

then we're

2:59:59

absolute value

3:0:00

then we make

3:0:00

then we're

3:0:02

the mean

3:0:02

make out.

3:0:04

So the way we do that

3:0:06

is we first find the error.

3:0:08

Okay, so I'll get

3:0:09

just to explain to you

3:0:10

error is basically

3:0:11

nothing but actual

3:0:12

one is predicted

3:0:12

if we're

3:0:13

it's a formula

3:0:13

if we're

3:0:14

okay,

3:0:15

because you know

3:0:16

this is

3:0:16

this makes no

3:0:18

sense actually.

3:0:19

You have to

3:0:19

understand the

3:0:20

formula also

3:0:20

because

3:0:21

you know my

3:0:21

point was the

3:0:22

quiz question asked

3:0:23

on that

3:0:23

so you have to

3:0:23

know the

3:0:24

formula

3:0:24

we're not

3:0:25

covering the

3:0:26

formula here

3:0:26

but let me

3:0:27

talk about it

3:0:27

so that you will

3:0:28

understand

3:0:28

which one is

3:0:29

penalized more

3:0:29

okay?

3:0:30

so error

3:0:31

was predicted

3:0:32

then we're

3:0:33

then we have

3:0:33

us

3:0:34

absolute value

3:0:34

and then

3:0:35

then we are

3:0:36

mean

3:0:37

we are doing

3:0:38

the mean of it

3:0:39

this is the intuition right this is how we are calculating

3:0:43

now if you talk about RMACC

3:0:46

RMAC in what we are doing

3:0:47

we are first calculating the error

3:0:50

okay this is the way to interpret it

3:0:53

okay first error

3:0:54

then we

3:0:55

we're square

3:0:56

then we

3:0:58

we've got

3:0:58

then we've got his main

3:0:59

then we

3:1:00

then we've got his

3:1:01

so if you

3:1:03

if you're

3:1:03

if you're

3:1:04

error always means

3:1:05

actual manner as predicted

3:1:06

so

3:1:09

it, okay, then it's square here, then

3:1:12

it's the main deal, I equal to 1 to n, and then its root layer.

3:1:17

This is how we define RMSC.

3:1:19

I think it's not visible once again.

3:1:21

Let me just write it above.

3:1:23

Okay.

3:1:24

So that is the same color.

3:1:34

So error.

3:1:36

Actual minus

3:1:39

predicted, then we square it up.

3:1:42

Then we take the mean of the squared errors

3:1:45

and then we take the root of it.

3:1:47

This is how we calculate the RMSC.

3:1:50

That's the intuition.

3:1:52

But if you think about it,

3:1:54

the concept is the same for both.

3:1:57

Here also we are trying to understand

3:1:59

what is the error on an average.

3:2:03

Here also we are trying to understand

3:2:05

what is the error on an average.

3:2:08

That is the error on an average.

3:2:09

is the general idea.

3:2:11

Okay.

3:2:11

So, so in both the cases, we are trying to, in a way,

3:2:14

intuitively understand which error is,

3:2:17

which is the error that we are getting in the model.

3:2:21

That's the way we are looking at it.

3:2:22

And remember,

3:2:24

squaring the error, this is what I explained in my slide here.

3:2:26

You have a slide in the slide here.

3:2:27

This is my question asked right.

3:2:29

Squaring the error heavily penalizes the massive mistakes

3:2:32

before taking the room.

3:2:35

But look, because we here here here

3:2:38

a square lay right, all of you can see my screen,

3:2:40

we are taking a square, right?

3:2:41

Because we are doing a square of actual

3:2:43

one is predicted, if you end up getting

3:2:45

scenarios where predicted and actuals are very far away,

3:2:49

if, mani, if there's difference

3:2:50

more, that is why we are

3:2:53

penalizing it more.

3:2:54

You have a question.

3:2:54

If you're a question about the answer to

3:2:58

say, this one of theoretical thing,

3:3:00

it's actually no relevance

3:3:01

is what we are getting into, but anyways,

3:3:04

this is the answer to the question, basically.

3:3:06

Okay, but I hope that that explains

3:3:07

to you, it's for you, what is, what is MAE versus what is RMAC?

3:3:12

So MAE and RMAC both are used to compute the error, okay, but in different ways.

3:3:17

So MAE is basically taking the average of actual to predicted comparisons, whereas RMAC is effectively

3:3:24

taking the square and then taking the room.

3:3:27

Okay, this is the way how it's done.

3:3:28

Again, it's a formula.

3:3:30

I, you know, honestly, just one of remembering one formula is useless.

3:3:34

So don't worry about the formula in detail, know the idea, know the concept.

3:3:37

Concept important.

3:3:39

If formula, just one of one or two formulas will actually not make an impact.

3:3:43

Don't worry about the formulas here.

3:3:44

The idea is clear, that R squared we're using, how we're using, model benchmarking,

3:3:49

how do they, dot score, where it is, you know, that, that concept will be clear.

3:3:56

Okay, okay.

3:4:04

Whether I hope that answers your question.

3:4:07

So here was clear. We are squaring it and then we are rooting.

3:4:13

So so, you know, right? So, so many things. If you want to get to the theory of ML, I mean,

3:4:20

this is a massive thing. It's like a deep ocean. We are not even covering one percent of machine learning

3:4:25

in the course. It's not an ML course. We're not. Our idea is to get into Gen AI. You have to remember.

3:4:30

Machine learning is a very small part of what we are trying to do. So this is only scratching the

3:4:35

surface of what it is. Okay. So there's a fourth.

3:4:37

whole lot of things out here. And again, you don't need to get into all that.

3:4:42

You know, you know, just say model what is, what training and what testing

3:4:45

are, how to bet kind of, score what is, error

3:4:50

what is. So the core idea should be clear.

3:4:52

Algorithms, what are what are trying to do. So some things are a bit of a disconnect.

3:4:57

So it may formulas and theory is not required. But the core ideas should be absolutely

3:5:01

clear to all of you. Okay. So also just to finally summarize the conversation,

3:5:07

these are the things that we broadly saw today.

3:5:09

So we were able to see the intuition,

3:5:11

that bridge or lasso regularization,

3:5:13

what are we were able to see the model comparison,

3:5:17

impact of regulation and model behavior.

3:5:20

Here we were able to see the concept that alpha

3:5:22

to increase and reduce

3:5:24

to do what it? We were able to see that

3:5:26

particular hyperparameter primarily.

3:5:30

Evaluation matrix was a little bit of theory,

3:5:32

but the intuition part of it we saw

3:5:34

how do we interpret this?

3:5:36

What a R squared?

3:5:37

score and MAE and RMAC both are errors.

3:5:40

So score we use are primarily to evaluate the models.

3:5:44

Whereas, you know, these things we are using primarily to interpret the model for our stateholders.

3:5:50

So when we talk to my manager and some business stakeholders,

3:5:53

we can tell us that the actual values are predicted from here,

3:5:58

or not off it.

3:6:00

Okay.

3:6:01

And obviously these are predictions and analysis.

3:6:03

You look at errors.

3:6:04

Where there are more than improve, let's say, for example.

3:6:07

there is one particular trip.

3:6:08

Uber in a co-trip.

3:6:10

Predicted price a lot, actually, actually.

3:6:12

So that's a lot more error.

3:6:13

Then you need to figure out that error why are there.

3:6:15

So that's the iterative process that you will have to do.

3:6:20

Again, of course, I think we have done too many case studies already,

3:6:23

like the advertising, the California, where you were able to choose this.

3:6:27

So please navigate over to the drive.

3:6:32

Contents are all uploaded.

3:6:33

The slide that I used, guys, the case study, we did, the notebook that we saw.

3:6:37

So please refer on to it.

3:6:39

And I think the notes will also be uploaded in your dashboard.

3:6:43

So next topic that we will be doing, we'll be starting off with classification.

3:6:48

I will see all of you next week.

3:6:50

So take some time to practice the concepts also in the meantime.

3:6:54

The next session will be on classification.

3:6:56

And the same approach that we discuss for regression, you'll have the same connect.

3:7:01

So same thing will very similar.

3:7:03

Most of these things will be here.

3:7:05

Again, you will see very practical.

3:7:07

concepts here. So next week will be totally on classification. Okay, take care.

3:7:13

I think that's all from my end. Okay. Thank you so much, guys. And I think tomorrow you have

3:7:19

further this revision. So yeah, so hopefully you have a good session. If you have any questions,

3:7:26

do bring it up. I want to keep aside, you know, the initial part of the classes for some questions.

3:7:31

And I think obviously as I say that your questions, keep the class interactive, keep the class, you know,

3:7:37

so do keep asking questions as many questions as you have yes much take care guys all

3:7:43

of you have a good night and i will see everybody next week take care all of you

3:7:52

so yeah thank you so much thanks thanks

3:8:07

Thank you.

3:8:37

