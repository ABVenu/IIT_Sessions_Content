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

Yeah.

4:32

We can be it for everyone to join and then we can start.

4:36

I think the voice is clear and sharp, right?

4:40

Yeah, did you try whatever we discussed in the last class?

4:53

I think today we will just try to implement whatever we have discussed.

4:57

So yeah, that will be the main agenda.

5:02

Is the screen miserable to everyone?

5:07

I think we are good to go, right?

5:32

Thank you.

6:02

I think you can see me as well, right?

6:08

So yeah, I think we can quickly start.

6:10

And you will see that we will be done with the implementation.

6:13

Today is just about the implementation part that we are having.

6:16

So one by one we can get started.

6:18

I think everything is good to go, right?

6:32

Yeah, so let's start with today's part. So this class is just a continuation of whatever we discussed in the last class.

6:40

If you remember, like I'll start talking with this diagram that we are having and we have discussed this diagram like multiple times from last two, three classes.

6:47

So when by when we can quickly see this part, that how a rag actually works.

6:52

And then what we will try to do is we will actually try to implement rag today, like that's the main scenario.

6:59

So yeah, let's get started.

7:01

Unless and until you were not there in the last class, then this class will be a little bit tricky.

7:06

Because like the theoretical part in detail we have talked in the last class that we had.

7:15

So we can see this that let's talk about this thing, that what happens in a rag system.

7:20

So one by one we can see here this particular part.

7:23

The first step is collecting the data.

7:25

The data can be coming from anywhere.

7:27

It can be coming from PDFs, URLs and anywhere,

7:30

and anywhere the data is present up.

7:32

The next thing is that what we will try to do is we will try to clean that particular data that we are having.

7:38

Like whatever data is not necessary, we will try to remove that.

7:42

We will try to normalize that data.

7:44

We will try to store that data in a structured format.

7:46

So you will see this will be the second thing or the second step that we are having.

7:51

Once we have done this particular part, we will try to go to the analysis part where we will try to do complete analysis.

7:58

This is a new part that we are seeing.

7:59

that we are seeing that we will be using something called us chroma db or chroma lab we call it.

8:04

So we can see this is a new tool that we will be practicing today and we will be installing today.

8:10

So one by one we will see that particular part and all these steps you will try to see.

8:14

And if you remember the first two steps also we have talked about in the last two classes that

8:20

whatever data we are getting from PDFs, URLs everywhere, we will try to get that data.

8:25

We will try to clean that data and then later on as the class goes on,

8:29

we will try to see how chroma lab will actually work,

8:32

how it will store the data and how everything will be working.

8:36

So yeah, till here I think we are good to go, right?

8:39

Let's start with the chroma db part that we are having.

8:43

So let's talk about chroma db.

8:52

Okay, just give me one minute.

8:55

This is lecture number 18 only, right?

8:58

What is it 17?

9:00

17 we did it, right?

9:03

I have already updated the PPDs.

9:07

Like if you try to go here to this particular part.

9:10

Let's try to see.

9:12

In the last class what we talked about.

9:14

So I think who is there?

9:16

Purajan, you have missed the class that is there.

9:19

We already had 17 lecture on Saturday, right?

9:23

There was an extra class on Saturday where we have talked about everything.

9:27

We talked about.

9:28

Okay, I think this part we have already talked about, right?

9:32

All this program.

9:35

Yeah.

9:37

So Purajan, you missed the class.

9:39

You have missed the Saturday class.

9:41

First, you can watch the Saturday recording and then you can join this particular class.

9:45

First, you need to watch this particular recording because all these things we discussed it already on Saturday's class that is there.

9:52

The lecture is uploaded by the team.

9:54

You can contact Maasai team for that.

9:57

I have shared.

9:58

from my end, the class was already taken on Saturday.

10:02

Yeah.

10:03

So if you, those who have not watched the Saturdays class,

10:05

I think this class will,

10:07

you will not be able to understand what we are discussing.

10:10

So yeah, let's try to go ahead to the next thing that is there.

10:14

Let's talk about the next scenario that how we will be implementing everything.

10:18

So one by one, we can talk about that.

10:20

So first of all, I think you remember, right?

10:23

That whenever we are having related data, what we can use is,

10:26

we can use something.

10:28

called as SQL or relational databases that are out there.

10:31

These relational databases, they will try to store related data.

10:35

And we have seen different examples of relational database also,

10:39

that in bank system, in colleges, in universities, in companies as well,

10:43

whenever we need to store employee data, student data,

10:46

and the data which is relational, where data can be stored in form of rows and columns,

10:51

we can use these kind of SQL database that are out there.

10:55

But today, for storing the embedding,

10:57

along with embeddings, like embeddings are the numbers that we are having,

11:01

which are representing the semantic meaning that is there.

11:04

In order to store all these things, we will be using something called as ChromaDB that is there.

11:09

And today we will try to go to the setup part.

11:11

So rather than the theory part first, let's try to do the setup part,

11:15

and then we can come back to all these slides that we are having.

11:18

So that I can really show you that how the chroma DB actually looks like and how things are happening.

11:24

I think everyone has installed Python, right?

11:27

Is Python installed in laptop or not?

11:33

So you can open any particular folder.

11:35

Like I'll try to open the same project that we have been working on.

11:39

I'll just open that and share my Visual Studio code.

11:42

I think everyone has installed VS code as well.

11:57

Yeah. So you can see this, that this is a project that we are having.

12:04

Currently, this is the same project where I've updated all the lecture notes.

12:08

So what I'll do is I'll create another folder for session 18.

12:12

And yeah, one by one, I'll tell you the necessary steps that are there.

12:16

You can open any folder where you are doing basic coding and then you can try.

12:20

So I think my BS code screen is also visible to everyone, right?

12:25

So you can see here that,

12:27

the first step or the first command that you need to run is,

12:30

I'll share the PPD link also with everyone so that you can directly copy from PPD as well.

12:35

Or what you can do is you can even type in everything that I'm sharing.

12:40

So the first command that you need to run is PIP install chroma DV.

12:44

This will only work if you're like Python is installed in your system or not.

12:49

So you can check if Python is installed or not by just writing Python 3 hyphen version.

12:56

So you can see.

12:57

two hyphons I am writing. And I can clearly see here that Python is installed in my terminal.

13:03

This terminal you can open in VS code. How you can do that is you can go to terminal, like if I share

13:09

my entire screen very quickly. You can see right in VS code, there is a terminal option that is coming.

13:16

If you click on new terminal, automatically a new terminal will open. This particular thing you can do

13:21

and you can actually open a new terminal. Once you open a new terminal, once you open a new terminal, what you can do is you can

13:27

type any command. Like for example, if I write here Python hyphen hyphen version, then also

13:32

it will show me the version of Python. If I want to know the specific version of Python 3,

13:37

even that thing will come up. So this is a Python three specific version that is installed.

13:42

In your systems, if anything like anything Python version is installed, right, then it will work.

13:48

So let's try. What we will do is like since my Python 3 version is coming up, I will be writing

13:56

here, PIP3 install, and then I'll just type here ChromaDB. So once I type it, you can see

14:03

this that it will, currently for me, it is already installed, and that is why it is saying requirement

14:10

already satisfied. But for you guys, it will work. So you can try these two commands, like you can

14:17

either try PIP install ChromaDB. Pip will not, like for me, PIP does not work. So that is why I'm

14:26

typing PIP 3 install chroma DB and in my laptop it is already installed. Can you try

14:31

running this in your laptop? If Python 3, I'll copy paste this command also. The same command is there

14:38

in the PPD as well. Are you able to run this command? Yeah, let it download. I'll just face this particular

14:48

part. You can either run this or you can run PIP 3 that is there. Correct? Correct.

14:56

Thank you.

15:26

Guys, still here, this thing is everyone able to do. Are you able to run this command?

15:37

Pip is not working because PIP has three version. If you see right here, the version of 3.

15:43

So if I type here, Python hyphen version. So you can see this that it is 3.9. That is why it is not working.

15:50

It should be anything greater than, like if you see the version of Python 3, right? It is greater

15:56

than 3.10. That is why it is working. Is that idea clear? And in my laptop, PIP is not

16:01

installed. PIP 3 is installed. So that is why you can see this command is working up. Is that part

16:07

clear, Vareen? No, Puriya, you have to watch the previous classes. You can open any particular folder that is

16:18

there. Just create a new folder in your laptop and click on open folder with VS code. I can even share that.

16:26

If you see my entire screen, if you open BS code, automatically file option will come in Mac, where you can type open folder.

16:34

And you can select the folder that is there. You can select any folder and just run this command.

16:39

Is everyone able to run the command?

16:43

Guys, are you able to run the command?

16:54

What syntax error is coming?

16:56

what is the syntax area is coming? Like you need to type in the command copy based, right? Copy based it in a kind of way. Like here can you see that I, you need to write spaces also properly. So run Manish PIP command that is there, right?

17:17

How nothing is happening?

17:20

Like what is happening? Did you wait? Like if you run this command, you can you can see? You can see what is happening? Did you wait? Like if you run this command, you can see for

17:26

me pick three is working, but PIP can fail. So you can see here that it can feel and that is why it is really

17:32

to this particular part. If you have missed to yeah, sorry, I'll just fix the mic. There is some issue with

17:43

my camera. I'm not sure. But if you see here, now I think you can hear me right properly. So you can see here

17:49

this particular part that we are trying to today see whatever we discussed in the Saturday's class. So that

17:56

thing we will try to do. So guys, you have two options. In your laptop, right, it will install. It will

18:02

take some time to install. I think I'll share the link of the PPD once again. And you can try it

18:08

after the class also. I'll mention here that there are two commands. The first command is you can either try

18:15

this or you can try this command, which is PIP 3 install chroma DB. Any of these commands. Any of these

18:26

you can try. So whatever command works for you, you can try that. Once it is installed, run the next

18:33

command. So for me, PIP 3 command is working. So I'll run the next command. The next command is this one.

18:39

So I have pasted it. You can either try with PIP or you can try with PIP 3. Any one of them will work. So you can

18:46

either use PIP or you can use PIP 3 that is there. I'll show you like I'll run this command with PIP 3 and we can

18:53

see it will work. So you can see I'm

18:56

just typing here PIP 3. And once I run it, you can see for me it is already installed. So

19:02

that is also working up. Correct? Is that part clear? This part are you able to understand? It will

19:11

take too much time depending upon your laptop speed that is there. It depends upon your laptop speed.

19:16

So it depends upon that.

19:26

commands, then you can make a new folder. So today, since it's a new session that we are having,

19:33

you can paste this command. I'll paste it in the chart also. ChromaDB is kind of vector DB

19:38

Reju. That is correct. So the next command that we need to run, all these commands are mentioned in the

19:44

PPD also. So you can see directly from the PPD and after the class also you can do. So yeah, a lot of

19:50

things will be downloaded, right? Noopur, that thing will happen. So you can see MKDIR. We can create

19:56

a folder and we can move to that particular folder that is there. So you can see I have just

20:00

created a folder which is vector search lab and you can see here this folder is also created. This

20:07

is a folder and currently in my terminal I am on this folder. So let me know once you are able to run

20:13

first four commands. I'll repeat first four commands that are there. You can see on my screen also.

20:20

The first command is that either install you can type PIP install ChromaDB or you can

20:26

type PIP install PIP 3 install ChromaDB. Then for this also, you can type PIP 3 install this

20:32

if PIP 3 is working or if PIP is working, you can type that. So I'll just try it here.

20:56

I think this idea is clear. Till here are we good to go?

21:02

Is everyone able to do this or not?

21:06

So you can see chroma db is a vector db. This vector db, it will help us run all these commands that I've written here.

21:13

And sentence transformer, it will help us convert the sentences. So if you remember right, that in drag what we are trying to do.

21:21

The main idea is that if I have a sentence, let's say my sentence.

21:26

is something like this. I'll just write it here also and I'll tell you that if I write this kind

21:31

of a sentence that what is the remote work policy? So you can see this is a English sentence that we

21:43

are having. We want to get it converted into a sequence of numbers. This is what we are doing. That this

21:49

particular sentence should be converted into some numbers like 0.13.0.0.

21:56

670.0.32.0.45, etc. Is that part clear?

22:07

Is this thing clear?

22:26

Thank you.

22:56

Guys, till here are we good to go.

22:59

Till here is everyone able to do it?

23:02

Is the understanding clear?

23:03

How many of you are able to run these four commands?

23:06

Like if I copy paste the commands here also.

23:10

Now you can see for converting this right, what we need is we need all these commands which I'm telling you.

23:16

So can you write in chat if your four commands are working?

23:19

I'll just put this box here.

23:22

You can either run this command or you can convert it.

23:26

You can write here or PIP3 install ChromaDB.

23:31

Then you can either run this command.

23:36

Any errors like those who are facing errors, what is a error that is coming for you?

23:41

Can you type in the error also for me so that I can help you?

23:46

And these commands, so everyone has to run it.

23:48

So I think all these four commands are clear, right?

23:52

So here we are just installing things that are there.

23:55

Nothing extra.

23:56

doing, we are installing things, why we are installing things, so that we can convert

24:00

this particular part, whatever English sentence we are having, we are able to convert into a sequence

24:07

of numbers.

24:08

It will take some time.

24:09

You have to write the commands in a very correct way.

24:12

If you make a spelling mistake, then a error will come.

24:15

Like for example, if I write here something, the spelling wrong.

24:19

If I don't write the spelling correctly, then an error will come.

24:22

So you have to write the spelling very carefully.

24:24

make sure that sometimes pip three will work some like either pip three will work or

24:30

pip will work warning can come up don't worry about that so if python is not installed in the

24:37

path then no poor search that how to install python and path those who are getting this error right

24:41

python we set up in the first class that is there so i'll ask copel also to help you in the

24:47

friday session regarding the installation but i think we already discussed it right that how to install

24:53

python in path and everything

24:54

you have to select that particular option i think let's go to the next part i think most

25:01

of you of you have done it so let's go to the next step that how we can prepare our data and we can open a

25:08

collection and now we will try to discuss the theoretical part as well you can see my ppd as well so you can

25:15

see here that what happen what if we are trying to do this is a sample data that i'm having so what i'll

25:21

do is i'll try to insert this

25:24

data and this data we will try to convert it into a sequence of numbers so the main idea is

25:30

that i was showing you this example sentence right i was having this example sentence you can see this

25:37

that uh this is an example sentence that i want to convert it into numbers what i'll try to do is

25:43

i'll try to convert all the records one by one so you will see this that this kind of program we

25:49

will try to write and using this program things we will try to do so first

25:54

you can go to slide number 12 and you can copy paste this program i'll share the ppd also

26:00

with everyone once again just open the ppt and you can find out all the commands that are there

26:07

are you able to open the ppd and copy paste from the ppd

26:24

you know.

26:54

it's installed now right is everyone able to copy paste right so the second step is this that

27:01

first step is that you need to run all these commands i have pasted all these commands here also so

27:06

you can see this is one command and this is either you can use this or this or you can use this

27:12

command or you can use this command that is there whatever is working for you this only we have to

27:17

do and then you need to create a proper folder that folder step even if you don't do then

27:22

also everything is okay you can either run this command in this command a proper folder will get created up

27:52

now i'll tell you what is the next step i think everyone is able to open this code the first

28:01

thing is you can create a python file so what i'll do is i'll open my visual studio code i'll

28:07

create a new file you can just write here give it a name as file dot p y and you can paste in the

28:14

code are you able to do it just create a file called as python dot p y or any name you can give you

28:21

you can give it file dot p by name and then just uh copy paste this code are you able to

28:27

copy paste let me know once you are done you can type in chart

28:38

create a new file and copy paste the code from the this

28:41

they get there like the 12th slide that we are having let me try to just run this also and see

28:51

are you able to copy based so you can see that once you copy paste and just write in chat so you

29:09

can see you can again open your terminal and on terminal if you want to clear the terminal you can type clear

29:15

also and then what you can do is you can just write python three and you can run this particular

29:21

file once you run it you should see currently uh this kind of output will come

29:27

because currently the knowledge base we have not created but we will add that knowledge base

29:33

this part are you able to do how many are able to do how many are able to do can you write in chat

29:44

you can see a a chrome db store will be created are you aware of so you have to install

29:51

chroma db right those who are getting this error gore did you install chroma db if you

29:57

installed chroma dv then restart your pc yeah you can try it after the class and one more thing

30:13

other people can do like if you want to do it here right just search here chroma

30:21

exchange or just search here sql extension like because the data will be added in sql extension

30:28

like if you open this file currently it will not open but we can download a sequelite extension

30:34

that is there so if i go to extension and probably install the uh let me see squel viewer

30:42

squatter if i install it then i think it should work let me try this also installing this extension

30:50

this error

30:51

Pratig what is the error that is coming you need to select the file properly right you in your terminal you should be present inside this folder then only this file will work right because currently if you see my terminal very carefully can you see this like everyone needs to understand how to run these basic commands in terminal right that currently i am inside vector search lab and then i am running running python 3 file dot pye that is why it is working if you are in a different folder then it will not work right

31:21

is that idea clear i created a file right i told the steps right now kashish

31:27

that first you need to create a file in that file you need to copy paste the code what is the code

31:32

that you need to copy paste you will copy paste the code that is written in 12th ppt is that thing clear

31:38

guys is that thing clear or not clear are you able to do it

31:51

how many are able to do it can you write and chat

32:08

you have to open terminal in the same folder that is there right as we discussed

32:27

is the program running for other people now you can see i will try to insert the data also

32:36

i'll show you that how we will try to insert all the data and all so we can see this

32:41

that six records we need to insert these are the records that we are having these records i think

32:47

we can paste it in the same program let me just see yeah i think entire program we can keep in single

32:58

file otherwise you guys will be confused so what i'll do is i'll copy the content of 11 slide

33:06

and i'll paste it here i'll share the entire program also with everyone so that you can do a

33:10

copy paste very quickly so you can see the first thing i'll do is i'll write here this thing so

33:18

that all the records can be fetched and then what i'll do is i'll try to copy paste this particular

33:24

part uh that is written in slide number 14 and i'll paste it here once i do that you will see this

33:33

that we will be able to add the data into this chroma dv i'll show you that also and then i'll

33:39

share you the entire program on website right now so that you can directly run as well

33:48

let it load the data it will take some time so you can see in your here the output is coming total

33:59

records are six so that means six records have been uploaded

34:03

so what i'll do is since it will create a very much confusion and you guys won't be able to

34:08

copy paste i'll write up push it on get up also so i'll just configure my email address i'll add

34:15

here git add start and i'll say git ignore file is there because i don't want chroma db to be pushed up

34:33

just give me a minute i think by a mistake i'd triggered the wrong command

35:03

so i think everything is back and we can see our chroma db and everything is created

35:09

and here if i just install that extension also i can live now show you also

35:33

let me just push all the changes i'll make a git ignore file don't worry about

35:42

the get ignore file and everything you don't have to do that

35:46

and i'll enter here

36:16

let me just do all these commands they have to be run so that you can't do all these commands they have to be run so that i can push uh everything on gettub and you guys can directly copy paste so just give me one minute

36:44

till then you can try other commands that are there like every other command just try let me just

36:50

run these commands so that i can push everything on get up and you can directly copy paste from that

36:56

you understood right what i did what i did is that i pasted the record part here that is there on slide

37:02

number 10 then i pasted the other command that is written and after that i can see my data is inserted up

37:08

so only that thing i'm doing i'm sharing you the entire program as well that how it can be done up

37:14

so don't be confused after seeing all these commands these are normal commands that are there which we run in day to day life later on you will also understand them

37:44

so now we can see get get add and i'll run get status status

38:14

i'll just commit a bug i'll commit this session 18 and i'll write here git push

38:29

so once i do that everyone can see that program online so what you guys can do is just open this particular

38:36

link go to this link which is get get up dot com open

38:44

the iatr folder here you can see there is a new vector search lab created and copy

38:50

paste the program from this link so on this link what you can do is you can actually copy

38:56

paste using this copy button is everyone able to copy paste now you need to copy paste the result

39:04

into a file that is there just copy paste everything into file dot p y and then run file

39:09

dot p by then you will see that that that thing will open up is that thing clear

39:14

this thing are you able to understand just delete the delete i am talking about this

39:27

right just delete the content in the file dot pva and copy paste what i'm sharing

39:31

you have to copy paste in a new file that you are creating right no poor

39:40

is every eyes other people able to do it are you able to do it or not

39:44

after that if you want to view the data properly right then download this

40:00

particular extension that is there like if you go here click on extension tab that is there

40:06

and just type this extension which is sq light viewer you will see this kind of viewer will be there you can

40:13

install it to see the data and

40:14

all so dhraj you have to install everything that is there correct right authenticated it

40:22

will be unauthenticated right that is not a issue kashash once you download it you can see here this

40:28

particular part that you can view the data also in this embedding data will be stored later on so you

40:34

can see this kind of data will come up and you can see all the data that we have created right it is pushed

40:41

here now after this we will be able to see the embedding

40:44

and everything that is there how many people are able to do all the steps i'll repeat

40:52

all the steps once again from the start so please listen it very very carefully so you can see this

40:59

that first you need to run all these commands that are there these are the commands that i showed

41:04

you once you run these commands then what will happen is we can see here

41:08

once you run these commands then go to this particular link what is the link this is the link

41:16

i have uploaded everything on this file just copy paste everything from this this particular link

41:24

and run inside that folder only you need to run

41:27

copy paste everything from this file copy paste into file

41:38

dot by then three even python you can run file dot by you should get output that six

41:47

records have been inserted how many are able to do till here till here are you able to do

41:54

do guys still here are you able to do or not i'll attach the screenshot also in the ppd i'll just

42:08

create a new slide very quickly and i'll paste the screenshot that is there so you can see the

42:14

same thing i've written in the ppd also these are the all steps you have once you do this we will

42:20

see this that all the rows are inserted so now you can see that how to open the file the opening of the

42:29

file can be done with the help of this extension so currently you can see the extension on my screen

42:34

also go to extension part and type here sq light viewer this is an extension and after

42:41

that you can even view the chroma db file that is getting created this bin file will never open

42:47

this bin file is only for computer you don't have to open it open the sqa light and you can see here

42:52

this extension part are you able to download long warning you can ignore right warning is coming

43:03

for me also you can ignore that that is not important

43:12

those who have done it can you write in chat quickly then we can move to the next step

43:20

correct right is everyone able to see chroma sqlid b

43:28

even if it is not opening you can download this extension later on and then you can do it

43:32

correct right so we can see our data is inserted let's try to do the setup and then we can

43:39

understand what we are trying to do first let's complete the setup part so now what we can do is

43:45

we can copy paste these lines that are there these lines also we can copy paste in the same program so

43:52

what i'll do i'll keep on pushing in get up so that you can update but you can see after this thing

43:57

you can write here this particular part and once i write it you can say you can see

44:02

if i just go to my terminal i can write here python i can go to the folder i'll go to my

44:11

vector search la folder and then only i can write python 3 file dot by so once i write it i think

44:18

it will not be again inserted right again you will see this warning will come for me also so you

44:26

don't have to worry about the warning and everything let me see peak so we can see these are the

44:32

are the data points that are there these are the embeddings that are created these are the

44:38

ids that are there this is the metadata that is there exact fetch for doc four is also coming up that you can reset

44:46

your password and you can see everything is there so you will see a big output will come where you can see all

44:52

the documents you can see all the embeddings that are there and you can see all the idies and everything so

44:59

this thing will happen correct so that

45:02

particular part we can do and what i'll do is i'll just again push all the changes

45:12

so we can see here git ad star and what we can do is we can write git commit session 18 changes

45:21

and i can just write here get push so again you can even copy paste the entire program that is

45:27

there on github i have already uploaded it so just go refresh the space

45:31

this page and in this page you can see at last i have added this command where you can see all

45:37

the data so you can see all the yes all the ides that are coming right they are the chunk IDs that are

45:43

there so now you will see that embeddings are also created program we will discuss in detail that

45:50

what it is trying to do are you able to run it once we can complete the setup part then we can

45:56

actually understand what we are trying to do till here how many people are able to do it

46:01

can you copy paste the last like these lines that are there and just run this and you will see

46:08

a big output will come a small output will not come very big output will come as you can see on my screen

46:14

also so you will see the entire data will come up warning will come up everything will come up

46:22

and you can see the exact data part as well correct right

46:31

where can you see fourth cd is everyone able to see we are fetching the fourth document

46:40

this is fourth document i am fetching whose data also you can see and you can see here this is

46:46

the metadata is like some data we don't want to store in embedding part we want to keep it in a

46:51

filter part that kind of data we try to store it as metadata format is that part clear

46:57

we will discuss that metadata also

47:01

but it is used to understand the data like for example the first two documents are related to policy

47:07

the third and fifth one they are related to the help center and these are related to FAQ so those

47:12

things we are storing in the FAQ is everyone able to do till here

47:21

till here are you able to do now one more demo we will see that i'll explain you this demo also so we can see

47:31

this that if we try to go over to this puritan at which step you are stuck you can actually

47:37

do it later on after the recording because i think you will need personal help so you can

47:42

raise a ticket with masai team and they will help you but which step you are not able to

47:47

follow other people everyone has done it

48:01

follow can you write and chart no right we don't have time to share your screen

48:08

here hundred people are there how can i resolve your errors so let's go to the next part

48:15

that we are having other people are is everyone able to do right even if you are not doing just to read

48:20

these steps that i've given and are at your home you can try if then also you are not able to

48:26

understand then you can raise a masai ticket or friday they will discuss correct

48:31

till here this part is clear shall i go to the next step so you can see in this

48:39

step what we are trying to do right whatever data we are having let's understand a code

48:44

base a little bit so if you see in this code base what is the data that is there this is the

48:50

data that we are having now if user is squaring anything that particular data we will try to

48:58

find out from this data after embeddings have been created so if you see the next part of

49:04

code that i'm writing here that user is asking about if you see my screen very carefully

49:10

just see the screen part that is there i'll just minimize this so read this line we are saying that

49:19

user wants to ask about shoes that are there then we will convert that user question into

49:25

embedding embedding is nothing but a sequence of

49:28

numbers that are there those numbers we will try to query and then what we will try to do

49:34

we will try to find out what are the top documents that are there is that idea clear so now you can

49:39

see that if i run this program like for example if i just run this entire program that is there

49:45

you will see a lot of output now because everything will run right we can even write other programs

49:54

that are there but you can see this is a main output that we added

49:58

that user was searching about what like if i just decrease the size of the terminal

50:04

for one minute you can see that user is asking i want to return my shoes just focus on my screen so

50:12

you can see whatever return data we are having like here you can see this is a data that we are

50:18

having in this data it will find out where exactly return and return things are present so you can see

50:27

is that this line is related to return this line is related to return this line is related to return

50:35

so that is why these three docs are ranked so this way whatever user is typing we are searching

50:43

those sentences which are having similar meaning is everyone able to understand what this program is

50:49

doing are you able to understand this or not is the meaning clear i'll explain the program in detail

50:57

in the second half of the class but currently i'll just push again so i'll say

51:02

git commit session 18 changes and i'll just add them also you don't have to run these

51:11

gits command right only i have to run the git command because i am pushing the changes every time on

51:16

get up that is why so you don't have to do any get up changes that are there so what you can do is

51:22

is you can actually run this particular part and you can see here that this part and you can see here that this

51:27

part will be added up correct so you can see that this is a user query can you

51:32

copy paste the program from here or you can copy paste the entire program and run it

51:38

can you run it and do you can copy paste the entire this page right all the lines that are

51:46

there all the 82 lines are you able to copy paste

51:57

all right.

52:13

Guys, is everyone able to copy paste?

52:21

Right, can you see a copy paste from this button, right?

52:23

Can you see a copy raw button is there?

52:26

Are you able to see that copy raw button?

52:27

raw button or not just copy here and paste it you just have to copy button you just have to

52:34

copy paste it and then are you able to see rank and everything like for example if i run again

52:41

i'll just zoom my terminal and you can see here if i write here python 3 file.py

52:47

are you able to see rank and everything write in chat if you are able to see rank and everything

52:55

so you can see right?

52:56

this is the ranking part is everyone able to see

53:00

correct right great so now you understand right like little bit understanding you are

53:15

getting that what this program is doing this program is first uploading the data then it is

53:21

converting it into numbers then once user is asking some question we are converting

53:26

into numbers and we are finding which numbers which are the top three closest numbers

53:31

that are there and we are using a model here what is a model we are using this particular model

53:37

correct yes right it will be different the raj

53:45

is that idea clear is everyone able to understand the basic concept i'll write the basic concept

53:54

over this diagram also that we are having six currently for demo purposes i have

54:00

written here six things so you can see this that if i actually go here you can see six documents

54:08

or six english sentences we have written these six english sentences we are converting into numbers

54:19

correct so you can see this that all these six english sentences they are converted into numbers

54:24

and all of their numbers also you can see how you can see all their numbers you can see

54:30

if you run this program again right if you see my screen you can see right these are the six documents

54:37

these are the numbers that are there so i'll just copy paste the numbers also and they are having a lot

54:42

of dimensions currently only few numbers are visible to us but in realistic way there are a lot of

54:49

numbers that are present so if you see all these numbers part you can see these are the number

54:54

that we are having once we have these numbers what we are trying to do we are taking

54:59

a english sentence what is a user english sentence you can see user english sentence is this one

55:08

if you quickly go over to this particular screen you can see here that user english sentences

55:14

uh let me show you from the program it is this i want to return my shoes so this is a sentence

55:21

this user gave and what we did is that we converted it into number whatever user

55:30

english sentence is there it is getting converted into a number that is present up and that number

55:37

we are finding out top three closest numbers so you can see this that we are trying to find out

55:44

top three closest numbers and you can see rank one you can see rank two and you can see rank three

55:51

is the overall idea of program clear and then we can discuss it in detail also later on

55:55

but currently the basic meaning of program are you able to understand

56:03

basic meaning is everyone able to understand right that i converted into numbers numbers also

56:09

i've shown you that what are the numbers here we can see this that these are the numbers that are

56:16

present and once we have these numbers right we can see this is a sentence that

56:21

sentence is again converted into a number and using that particular number we are finding

56:26

out top three ranks so top three ranks from this data we are trying to find out i think this

56:32

is very much clear currently i've chosen a very basic model that is there so ridgum multiple

56:42

other models we can choose we talked about it in the last last different different models that are

56:46

there are open a i models there are chart gpd models then there are

56:51

this bg model artificial intelligence is there correct we will discuss the program

56:57

in detail right avinash don't worry about that one by one we will discuss each line of code

57:04

currently the meaning and flow is clear how many people are able to understand the flow of the

57:09

program and this screen that i'm showing right now this flow is clear right so this is the flow of the

57:18

program correct after that we will discuss

57:21

one by one line that what is each line meaning that we will try to discuss from ppd we

57:27

will be discussing that you have to copy paste it right right now after learning you can write it on

57:33

your own as well but currently to in life class for understanding the flow first time you can

57:38

copy paste right is that thing clear

57:51

another query this time we can see top two ranks that are there so again you guys can

57:56

copy paste either from 21 slide or you can copy paste from my program that i'll push right now so you

58:03

can see what i'll do is i'll add here more lines i'll open my terminal and i'll just type here python

58:11

file.py so now i am asking again another question and this time two other ranks i want to see so let it run

58:19

it will take some time to run and once the run is completed we can see other two ranks also

58:24

that are there so you can see this that these are the two ranks that are there from the first question

58:29

and these are the two ranks that are there so if you see the question that user has asked

58:35

user has asked question how do i change my login password and the nearest match that we are getting

58:41

is you can reset your password from the account setting page if the payment fails try another card or upi

58:49

so you can see these are the two closest sentences only the first one is the useful one

58:54

because only one line is related to password right so only this will match and others are also the

59:00

distance is calculated i have not printed the distance here but it will be very very large

59:06

is that idea clear so currently if you see each is a english sentence for every english sentence

59:14

there is a big embedding right this is a big embedding this is a big embedding this is a big embedding so

59:19

embeddings are there for each of them is that idea clear

59:21

rank one is the best priority right so since every time we will try to pick from

59:33

one two three ranks which are matching so currently you can see this rank is

59:37

matching we will pick it correct so i'll just push this command you guys can also copy-paste

59:43

and then you can run it so i'll just again write all the commands that are there

59:49

and we can see i have pushed the changes that are there so you can see

1:0:02

here that all the changes will be pushed up and you can see the changes here

1:0:08

so you can see these are the changes that are there is this part clear

1:0:19

we can see the ranks also right i'll just refresh this page so you can see the

1:0:26

second result also is there right second query are you able to run let me know once you are able

1:0:30

to run once you are able to run once entire program running we have completed right then i'll

1:0:36

teach you the theoretical part of the program as well till here i think everyone is able to do it

1:0:42

right till here only we need to do then we can start with a theoretical part of the

1:0:49

and again we will discuss everything from the pbd is everyone able to run 97 line of

1:0:54

code i'll share the link again here and just run it and let me know if you can see similar

1:1:03

output like if you run python dot three and you run this you can see this count of output will

1:1:12

come up other people what's a scenario where are you stuck at those people who are stuck at those people who are stuck

1:1:19

where are you stuck at?

1:1:49

come up right if you try to think here you can you see here this part that here only six

1:1:54

records are there correct so if you type question related to return then automatically the first

1:2:01

two things will be related to return now third one will also have some distance right so that

1:2:06

will also be there is that idea thing clear correct right right right why it is

1:2:19

we have written here three right can you see here i have written at line number 73 n

1:2:24

results is equal to three that is why three results are coming here i have written n results

1:2:28

equal to two so that is why two results are coming getting my point so now we can start the

1:2:36

theoretical part of this particular program so you can see this that currently i am using two libraries

1:2:41

that are there correct the first two libraries in order to run these programs these two libraries will be

1:2:47

be needed one is the chroma db and one is sentence transformer so how many people are

1:2:53

there who are still stuck on the installation part guys are you able to install this

1:3:01

how many people are able to install

1:3:08

currently we are not chunking right we are saying that every sentence is a chunk that is why

1:3:13

six embedding is there what is the issue in that part

1:3:17

and currently i'm printing all the embeddings so that is why six embeddings are getting printed right

1:3:22

are you just copy paste the entire thing right copy paste the entire program and then run it

1:3:35

shi and deep are you able to do that yes right nearest one it is printing so you can see rank one

1:3:42

is the closest one rank two is a little bit far for that rank three is more far than that is that idea

1:3:47

clear?

1:3:48

here.

1:4:18

chart studying this program you will see one by one we can start that part and how many

1:4:23

are stuck and what is the error you guys are stuck at now only three steps you need to do like you need to do

1:4:29

like you need to run the first step is this one so probably purjan you can also try you need to run this

1:4:36

part once you run it in terminal either of them then you need to run this then you need to run this then just

1:4:43

create a folder and create this after that you can even create a file also

1:4:48

so if you want just create a new file in vs code and copy paste everything from this

1:4:52

particular part correct those who are joining from phone can watch and try after the recording

1:4:58

as well right that you can do other people those who are stuck can you type in the error that you are getting

1:5:05

like we have five minutes we can fix it and then we can start with a theoretical part

1:5:10

other people are done right i think 90% people are able to do it

1:5:18

so those who have raised the hand like let me see manish ridju madushi pangkaj saurab archit

1:5:28

what is an invari what is the issue that you are getting

1:5:33

shiga is python installed if python is not installed then it will not work

1:5:38

archit is working fine manish what is the issue you are having then arvinda what is the issue you are

1:5:44

having you are getting any error

1:5:48

Archid for you also it is working fine right?

1:5:59

Suraj, Madhushri and Manish.

1:6:07

Soarab, what is the issue you are having?

1:6:14

Yeah.

1:6:16

I think yeah.

1:6:18

this you will see i think everyone is able to do the setup part only thing is now we will try

1:6:23

to understand what this program actually means each and every line meaning we will understand

1:6:28

each and every function that i have writing that we will try to discuss we can have a short

1:6:33

break and then we can discuss that so yeah let's have a short break and after that we can understand

1:6:39

the meaning you can do that punkage in the friday's class what is the exact error you can just

1:6:45

type exactly what is the issue i have told

1:6:48

all the steps and i have written a single program that you can directly copy paste and do

1:6:52

everything that thing you can do so yeah let's have a short break and then after that what we can do is

1:7:00

i think my voice is clear right yeah then let's try to understand the deep meaning of the program

1:7:06

line by line all the theoretical part we will try to do so those who are getting this error can

1:7:13

are did you install and like did you install these things

1:7:18

these things did you install punkaj this and this like if you search this particular

1:7:30

error you can see this that whenever you are getting this error right then you need to

1:7:35

install probably you can install it from the konda link that is there so probably run this command

1:7:42

so punkage if you are getting this error right just type in this command that is there

1:7:48

or run this particular command i pasted these two command i think other

1:7:55

person also was getting this error right shikha i think shikha and punkaj are getting this error

1:8:00

so just copy paste whatever i've shared from zoom chat or you can even type i'll type it here also

1:8:07

you can see here from this link open this link and from zoom i think you can open this link and you can see

1:8:14

how it will work probably environment variable issue is there

1:8:18

you need to add the file to the path i think python is not installed in your laptop

1:8:27

properly just try running these commands and try once again after the break let's discuss the

1:8:33

theoretical part each and every line in discuss each and every line in detail we can discuss

1:8:37

yeah with konda you can try just type here this command python uh install torch just type here this command

1:8:44

python uh install torch just type this command exactly if that is working

1:8:54

pip three installed torch can you try punkaj if that is working

1:8:59

paper install torch or pip3 installed torch

1:9:08

yeah let's have a short break and then we can discuss

1:9:14

you know.

1:9:44

You know,

1:10:14

You know,

1:10:44

You know

1:11:14

I'm

1:11:44

I'm

1:12:14

I'm

1:12:44

I'm

1:12:46

Thank you.

1:12:48

Thank you.

1:13:18

Thank you.

1:13:48

Thank you.

1:14:18

Thank you.

1:14:48

Thank you.

1:15:18

Thank you.

1:15:48

Thank you.

1:16:18

Thank you

1:16:48

Thank you

1:17:18

Yeah, guys, can you hear me?

1:17:25

Is the voice clear to everyone?

1:17:27

So yeah, that is not an error, right?

1:17:33

Muscan, you can see that is a minor warning that is coming.

1:17:37

And same way you can see output is also coming up.

1:17:40

Total record is 6.

1:17:41

Just use the updated program that is there and then you can do it.

1:17:45

Yeah, Erwin, what is the error you are having?

1:17:47

What is the error you are having?

1:17:49

Can you type in chat?

1:17:50

What is the exact error?

1:17:54

Till here, I think we are good to go, right?

1:18:00

Shall we discuss the theoretical part now?

1:18:06

So let's start with the theoretical part.

1:18:09

One by one, we can see the necessary things that are there.

1:18:12

So we will start from here, first of all.

1:18:14

And let's try to discuss the everything

1:18:17

in detail. The output part again, Garima, we will discuss in detail what is happening and then we can go on.

1:18:23

So you can see that first of all, like if you see everything what Chroma is storing, it is trying to store four things that are there.

1:18:31

What are the four things?

1:18:32

We can see the first thing is the unique name.

1:18:35

This name is just the ID that is there.

1:18:38

Like whenever we are storing anything in the data, right, you will see that there is a proper ID that we try to store.

1:18:44

That part is everyone able to understand.

1:18:46

understand. Then you can see all the documents that are there created, like the original text.

1:18:53

I'll show you directly from the output as well. What are the three things? So I'll just run the program

1:18:58

once again and I'll share quickly my terminal.

1:19:07

So if you see here this particular part, right? See it from here. You can see all the data part that you can see.

1:19:14

This is what? This is the real data.

1:19:16

that we are having. And how we are getting this data? This data we are getting by running this particular part.

1:19:23

If you see this particular program, right, and you see total, like you see this peak command that is there.

1:19:30

This peak command shows you how the data is stored inside the chroma DB that is present.

1:19:36

So using this particular peak command, that is why we can see the entire documents that we are having are present.

1:19:43

All the embeddings are there.

1:19:45

For each embedding, there is a proper ID that is present.

1:19:49

Inside which we can see that whatever things are included, we can even see the metadata that is getting stored.

1:19:56

So you can see everything we are trying to store.

1:19:59

Is that idea clear?

1:20:01

So this metadata is optional.

1:20:04

Like things like whenever we want to filter the chroma DB, right?

1:20:08

Then we try to put different different filters that are there.

1:20:11

Those filters are called as metadata.

1:20:14

And after that, the main.

1:20:15

important thing that we are having from this data which will always be there is the

1:20:19

embedding part these embeddings can you see here 384 what do you think this 384 means

1:20:28

this 384 is the dimensions that we are having this means that this particular

1:20:34

array is of size 384 these 384 numbers are representing the meaning of the

1:20:40

sentence like for example this sentence is that customer can return the product within

1:20:45

30 days of delivery. So 384 numbers together they are representing the sentence.

1:20:52

And why here 6 is written? 6 is written because there are total 6 documents, right?

1:20:58

Each of the 6 documents, they are having 384 numbers.

1:21:02

Is that idea clear?

1:21:04

Is that idea? Are you able to understand?

1:21:15

Guys, is that part clear or not clear? The first thing are you able to understand?

1:21:20

So we can see here in this particular part that four things are present. What are the four things?

1:21:25

we can see ID is there, document is there, metadata is there, metadata is there, embedding is there. All these things are present. Is that idea clear or not?

1:21:35

Shall we go to the next part?

1:21:40

You don't have to install torch or anything. Currently, till here, this part is clear or not clear.

1:21:45

So you can see there are different, different functions that I'm using in this particular program that I've entirely written.

1:21:54

So you can see the first function is get or create collection.

1:21:58

What do you think it is doing?

1:22:00

It is creating the entire program or it is creating the entire chroma div that we are having.

1:22:06

Like for example, if we see the code part that is present, can you see the first line, which is chroma dot persistent client?

1:22:13

and just read this particular function, which is get and create collection.

1:22:19

So you can see what does that function does is, it creates a particular folder.

1:22:24

Where is that folder? That folder is present here. Can you see this particular folder that we are

1:22:30

having, which is Chroma store? So inside this folder, we can see a collection is created.

1:22:35

That particular collection is what? It's a supporting knowledge base. And currently there is no

1:22:40

embedding inside it. Later on, while using this.

1:22:43

particular transformer or this particular model that is there, I'll convert it into

1:22:49

a particular embedding that we are having and then we will try to insert all the embedding

1:22:53

that are there. Is that idea clear? So currently multiple functions are there. One by one,

1:23:00

we can talk about all the functions that are present up. So I'll just go back to the other screen. So you can

1:23:05

see get or create collection is there, absurd is there, count is there, peak is there, get is there,

1:23:11

get is there. So get or create collection, it is like creating. In SQL, we create a

1:23:17

table, right? For creating a table, what query we were writing? We were writing create table query that is

1:23:22

present. Same way for creating in Chroma DB what we are using. We are using get or create

1:23:29

collection. Is that idea clear?

1:23:41

one by one we can see all the different functions that are there. So if you see,

1:23:50

the first step is installation that we have already done. Now, this is a sample data that you are having.

1:23:56

So currently I have taken data from e-commerce, all the FAQs that are present, right? Those

1:24:02

FAQs I have taken one by one. And what I'll do is, I'll take these FAQs and I'll try to insert it into

1:24:10

my chroma store that is present. So first of all, I'll try to create a chroma store.

1:24:16

And I am saying here, persistent client. What is the meaning of persistent client? That this client

1:24:22

or this particular chroma DB will persist in your laptop. Persist means that it will stay in your

1:24:28

laptop. Is that idea clear? So you can see this that here I have written a path as chroma store.

1:24:33

If I replace this chroma store to suction store, right, then you will see up another folder with

1:24:39

Saksim store will be created. That idea are you able to understand that this is just

1:24:43

nothing but a path. So let's say that if I try here and I just write here my name. You can see here

1:24:50

another folder will be created which will be storing this data. And what I can do is I can just run

1:24:55

this command again. I can write here the same command and you will see another store will get created

1:25:00

which will try to store everything that is there. Can you see automatically this is created and it will

1:25:06

store the data and everything. This part are you able to see? So this is just creating a folder

1:25:11

inside which your chroma DB will exist. Is that idea clear? So if you see now the first

1:25:19

we can see here like one by one let's talk about these are doing what they are trying to we are trying to

1:25:29

use all the existing libraries that are there. The first library is a chroma library. Then we are

1:25:34

having the sentence library that we are having, then we are trying to set up the data. So

1:25:39

so if you see this part is setting up the data that we are having. Then we are trying to create one client

1:25:46

that will locally store everything. You can set it to any name. Currently I have put here name as

1:25:52

Chrome a store. You can put even your name and you can see that I demonstrated for my name, right? You can

1:25:58

even put your name that is there. Then we will create a collection. That collection will store everything.

1:26:03

And if you see the collection name, like in the output, if we try to see here this particular

1:26:08

part, like let's run it again. And I'll just zoom less the screen and I'll show you the entire

1:26:15

output that will come up. So we can see here this particular part. The first line of output that you

1:26:24

will see right, collection name and collection ready, current count six. This means that totally

1:26:28

six IDs you are trying to insert. So you can see all these six IDs.

1:26:33

they will be added up. And till here line number 31, any doubts anyone is having,

1:26:39

this part are you able to understand? Can you write in chat if possible very quickly?

1:26:47

Archid, we will discuss it, right? How many people are able to understand the line number 31? So you can

1:26:54

see this is the collection name that is there. Count is just displaying that how many things are

1:27:00

inserted into the data. Earlier, if you remember,

1:27:03

If you will check the recording, do you remember that current count was coming as zero?

1:27:08

Once I was not providing the data, the current count was coming as what? This was coming as zero.

1:27:14

Do you remember that? And now we can see here this particular part that the current count is coming as six.

1:27:20

I think that idea is also clear.

1:27:26

Let's try to go to the next part that we are having. So we can see here, now we are using a model.

1:27:32

Currently, this is a model.

1:27:33

that we are using. We can use this and we can use any particular model that is there.

1:27:38

In this model, what I'm trying to do is I'm trying to from my data, like this is the data that you

1:27:44

are having, we are iterating in this data, like this is nothing but a loop that I have written.

1:27:51

Every time what it will try to do is all the documents that are there in the data, they will be

1:27:56

extracted up, all the IDs will be extracted up and all the metadata will be extracted up.

1:28:02

If I just comment everything for you, right?

1:28:05

What I'll do is I'll select this code and I'll just comment it for one minute and I'll show you what they contain.

1:28:12

So if I just run here this part, print documents, print IDs, print metadata.

1:28:25

So you can see if I do this particular part and then I run this program right, now you will see you can see you can clearly see.

1:28:32

see what documents are storing, what IDs are storing, and what metadata is storing.

1:28:38

So let's see that part also. So you can see this, right, that this is contained in documents,

1:28:44

this is contained in IDs, and all this data is contained in metadata. Is that part clear?

1:28:53

Yes, right? So if we see, this is a model that we are having. So you can even Google search and you can find

1:28:59

out different versions of these models also. Like, for example, if I quickly go to this particular

1:29:04

screen, you can see here that what I can do is I can search this model. This is one of the sentence

1:29:10

transformer model that is there. This is again free of cost. And you can see this that it will convert the

1:29:16

sentences into numbers. So first, what I am trying to do is I am trying to extract the document IDs and

1:29:23

metadata. Once I extract that, then what I'll do is I am doing encoding. So if you,

1:29:29

you see this particular line. Line number 39, 40 and 41. In this particular part, I am converting

1:29:35

all these English sentences into numbers. Correct, right? HF refers to hugging face that is

1:29:42

there. That is internally defined by the libraries. So we don't have to worry about that.

1:29:48

Till 41 line, how many people are able to understand?

1:29:55

Sentence former transformer is defining that kashish.

1:29:59

Till here we are good to go, right?

1:30:07

Pankaj, what thing is not clear?

1:30:14

Yes, right? The same thing we will follow. If let's say today we are doing it with six documents. The same thing can be implemented for 6,000, 6,6 lakh, 6 million documents also.

1:30:25

So then also the same thing we will do. We will extract the documents, IDs and

1:30:29

metadata. We will convert all the documents into numbers. And then we will use absurd. What is this

1:30:35

absurd meaning? This absurd will push everything where? It will push everything to the database that is

1:30:42

present. So now you can see if I see the count, it will come as six.

1:30:50

So this is nothing but a Python lambda function that we are trying to use. So you can see this

1:30:56

that I am creating a array. How I am creating?

1:30:59

array. Every time I am iterating into records. So I'll show you how it will work.

1:31:07

Just to see here another screen and let's discuss about it.

1:31:13

So you can see here this particular part, like you can see currently these are the records that I am having.

1:31:20

Inside these records, what I'm trying to do is I can see here that if I write a for loop, like for example, if I write for

1:31:28

are in records. And if I just print R, then you will see automatically what will happen.

1:31:34

All the records will be printed. Can you see here? Now, inside this records, what I want is,

1:31:40

I want all the text part that is there. So text part is what? Test part is this line that is written,

1:31:46

right? So now you are able to understand what that, that what is our text meaning? Is this thing

1:31:53

clear? This is just another way of writing it. Now, what I am saying is all

1:31:58

these text will be converted into a list of arrays. So what I say is I say, I give a variable

1:32:05

as Saksham, then I say R text, and then I say for R in records. And yeah, this part if I write down,

1:32:16

so you can see it will iterate in records. It will extract the text R there. And then you can see a

1:32:23

array will be created. So if I just write here, print Saksham. And if I just run this, you will

1:32:28

see this data, array will be created. Are you able to understand this now?

1:32:36

Other people are you able to understand this line? Now, if you see here, I am writing this

1:32:43

line, which is convert to Numpai. Numpai is a library, which is used to store everything in

1:32:50

numbers format. So you can see this encoding function, right? If I just over over it. So you can see

1:32:58

multiple inputs we can give. Numpai I am writing so that it is able to convert it into a

1:33:03

proper tables format. I'll show you also how it will look like. I'll just comment everything and I'll

1:33:10

show you exactly the output of this part so that you are able to understand. So you can see here

1:33:15

this particular part that if I write here this thing, print and then I write here documents

1:33:23

embedding that are there. And then I try to just

1:33:28

run this particular part. Let's run it with terminal only. So you can see this.

1:33:36

Once I run this with terminal, let's see. You will see this is a very, very big array. Why

1:33:46

this big array is coming? Can you explain me? You can see this right? This big array is there.

1:33:52

What is this big array? Each of the each of the each of the

1:33:58

text that is there. It is having how many values? It is having 384 numbers. Right.

1:34:04

So we can see if I just iterate, I can even iterate and print it. Like for example, I can say for

1:34:09

R in documents embedding and we can just print R. So let's run this. You will see that in different

1:34:17

different line. Each of the vector embeddings will be printed up. Is that idea clear? Every sentence is

1:34:23

converted into 384 numbers. All these numbers we need to add it into data.

1:34:28

Now, what thing is not clear here? So you can see one by one all these numbers are coming, right? Since 384 numbers are there, you cannot see the breakage part, but one by one, all these numbers are getting printed. Is that idea clear?

1:34:43

So we are using this encode model. We are encoding. Encoding. Encoding is converting all the raw data that we are having into numbers. Till here, line number 44, like till line number 44 are you able to understand.

1:34:58

Now we will see the absurd function that is there till 42. Any doubts anyone is having?

1:35:28

For every sentence, there will be 384 number. What is a doubt in that?

1:35:38

Dimensions are 384. That part is clear, right?

1:35:44

Guys, still here, this part is clear or not clear? What is the doubt you are having?

1:35:58

Oh, ho. Archit, were you there in the last class?

1:36:04

Guys, I think everyone remembers, right? That every model has a different dimension.

1:36:09

Currently, this model that we are using, it is having 384 dimension.

1:36:14

If I change the model, then the dimension will change. Like, for example, if I go to BG Large model, that is there.

1:36:20

Okay, and let's search about BG Large.

1:36:25

So you will see this, that this, this large model.

1:36:28

that we are having, it is having thousand dimensions. As dimension increases,

1:36:32

the accuracy will increase, right? Is that part clear or not clear? No matter the size of

1:36:38

the sentence, the dimension will be 384 only. Can you hear me?

1:36:46

Guys, can you hear me?

1:36:51

Correct, right? So you can see this that this, this BG model, the large model that is there. This large model that is there. This large model, it has a

1:36:58

like thousand dimensions that are there. Its smaller version has 384 dimensions only. Is that part clear?

1:37:28

Let's go to the next part that we are having. So let's try to go back to the program.

1:37:38

So if you see here this particular part, that we are using this model. This model has 384 dimensions.

1:37:45

We are getting the text, IDs and metadata. Then we are converting it into numbers. And then we are using upsert.

1:37:54

What is this absurd doing? This is pushing everything where?

1:37:58

into the chroma DB that we are having. So upset command main purpose is that once

1:38:03

you create a collection, then the data will be pushed according to what? The data will be pushed

1:38:08

with the help of upset command. So you need to remember that every time you are using

1:38:12

upside command, the main purpose is to push all the IDs, the documents, the metadata, and all the

1:38:19

embedding starter there. And embeddings also have shown you. After this command, you can see that

1:38:24

now the collection will contain how many embedding it will contain six embedding if you want to

1:38:30

print total number of embedding you can use the count command if you want to see all the embeddings

1:38:37

that are there you can use the peak command so if you remember all the output that i try to show you

1:38:43

right here all the data is coming with the help of peak thing that is there correct so you can see this

1:38:48

that if i try to run this command again we can see here that

1:38:54

you can see this right that currently total records are six because six data has been

1:39:01

uploaded and you can see once i run the peak command all the data the documents the embedding

1:39:07

ides metadata everything is coming here is the peak command also clear that peak command will show you

1:39:14

everything in the data it will show you everything that is present in the collection the idies

1:39:20

document metadata and everything till line number 57

1:39:24

are you able to understand so in order to view this particular file you need to

1:39:33

download this extension that extension nupura told right we need to type install this

1:39:38

xqlite extension then only you will be able to open the file is that part clear

1:39:49

till here is everyone able to understand

1:39:54

should we go continue the program now anyone having any doubts till line number

1:40:00

57 till line number 57 it is clear or not clear

1:40:10

let's go to the next part so you can see here now what we will try to do is

1:40:17

the next part is that if i want to extract any particular embedding of any particular dock then i can use a

1:40:24

get command as the name suggests right that get command will get embeddings of any particular

1:40:30

doc or the data of that dock so if you see the output once again you can see here using this that i am trying

1:40:37

to get what is a data that is stored for the fourth dock like fourth sentences you can reset

1:40:44

the password from account setting page so you can see if i see this is the same thing

1:40:50

currently embeddings are not coming up but you can see other things are coming here

1:40:54

because embeddings will come up using the peak command only directly it cannot display but

1:41:00

ideally internally it will show the embedding as well is that part also clear that whenever we want to see

1:41:06

any particular data we can use what we can use get command so you need to remember these

1:41:12

commands that are there the main idea is that you try to remember the meaning of all these commands

1:41:19

so one by one i'll just give you a recap till now we have seen these commands that are there

1:41:24

we can see one is the get creation get or create collection command then there is an

1:41:30

absurd command then there is a count command count command means it will count how many things

1:41:35

are there in your database absurd command will calculate how many things you can insert

1:41:40

command will find out the data like whatever data you have stored in the all the embeddings idies

1:41:47

document you can see if you want to select any specific thing

1:41:51

like you want to view any specific doc that is there

1:41:54

then we can use the get command the last command that we will study will be the query command

1:41:59

and that also we will discuss but first two five commands are you able to understand

1:42:24

that we will discuss in the next class once we cover the rack part then we will discuss

1:42:29

avinash that we will see later on this particular data we will talk later on once we

1:42:39

discuss the rack part right then only you will be able to understand that what this table is

1:42:43

actually storing like why here these many tables are there what is the primary key all these

1:42:49

things we will discuss in the rack class once we implement correct currently you can see only

1:42:56

one connection name is there this collection is actually storing the name of the collection

1:43:01

you can see here this value also dimension and everything are also stored up so you can see all these

1:43:07

things are stored in the databases part you can see default database is created in the embedding part we can

1:43:13

see for every segment some embeddings it has stored in a different way and you won't understand much things

1:43:19

from all these segments and all this part we will discuss later on that what it is trying to do but we will

1:43:25

discuss that that how it stores the embedding how it does everything that part we will

1:43:29

talk about is that thing clear or not clear till here the program you are able to understand

1:43:42

so you can see we have discussed all these commands like till now we have talked about

1:43:48

persistent client which will create a client after passing a name get or create collection

1:43:55

then sentence transformer then encode is there then absert is there and code will convert

1:44:01

into actual encoding absurd will insert into the data count will display the final count

1:44:07

peak will tell us the data how it is looking like get we can find out any particular

1:44:12

id if i want to get the embeddings and other things we can get it from get part now the last

1:44:18

command that we are having which we have written twice is the query command so whenever we get a user query

1:44:24

query which is a english sentence which command you can use to convert you can use encode

1:44:29

command to convert a english sentence into number so you will get the query embedding i can show you

1:44:35

this query embedding also it will also have 384 dimensions we will use query function and we will find

1:44:42

out top three queries so you can see how many queries i want i can write that currently i am writing

1:44:47

three to three query will come up if i write here five five queries will come up five ranks will come up five

1:44:53

results will come up is that idea clear so we can even see the query embedding also i can

1:44:59

demonstrate you that part uh so that part also we can quickly do so if you see here like

1:45:07

you can see here this particular part that if i run here if i run here query embedding and then

1:45:14

what i can do is i can just click on this particular button and let's run it so we can see the

1:45:22

query embedding lastly the last thing that will be printed will be a query embedding

1:45:30

so you can see this big 384 numbers right that are coming up this is nothing but a

1:45:35

query embedding that is there now this query embedding what we will do is we will find out the top

1:45:41

three ranks and those three ranks we have already seen we can find out the idea of the rank

1:45:47

we can find out the document of the rank we can find out the metadata we can calculate their

1:45:52

distance also that is there so if i run the entire program again you can see this that once i

1:46:00

actually run this particular part you will be able to see top three ranks using the query function that

1:46:07

we have done and i have run that query function twice so you can see that is why two times the ranks

1:46:12

are getting displayed the first time i am printing a lot of things i am printing the id document

1:46:17

metadata and distance everything so you can see currently first to

1:46:22

thing is very very close the second thing is a little bit far third thing is very very far so

1:46:27

generally as the distance increases as the distance is increasing the meaning will different the

1:46:35

meaning will be different like for example if user will be asking anything user is asking anything

1:46:40

related to shoes and return then that is why you can see currently this is not matching much because

1:46:46

the distance is very very high here the distance is very very small that is why they are matching

1:46:51

the same thing is happening again next time i am running how do i change my login

1:46:56

password i convert i use the same model that is there i again use query command this time i am using

1:47:02

only two ranks that are there that is why two ranks are coming up and you can see here i am printing

1:47:08

only the rank and the document if i want to print the metadata also i can do that if i want to print the

1:47:14

anything like whatever you want to print you can print it and you can see the out

1:47:21

that in the output again the ranks which are closer to that particular query are coming up

1:47:26

even if you want we can even paint the query so that you are able to understand it in a better way

1:47:32

like if you want we can even print the query message also like before printing it i can print here

1:47:42

query that we have written or we can say this is the second query that we are having

1:47:51

and we can even print before this the first query so that you can remember that okay like after

1:47:57

the first query this is a result that is coming after the second query this is a result that is coming

1:48:02

so you can see here i can print the user query that is there so now again if i try to run it

1:48:10

you can see this that the entire part will be coming up now let me know what is not clear in the program

1:48:16

now how many are able to understand the entire program are you able to understand the entire program

1:48:21

all the commands that we discussed so you can see this is a user query and these

1:48:25

are the ranks that are coming then this is a user query and these are the ranks that are coming

1:48:30

is that part clear guys is that part clear or not clear even if you want i can change it and i

1:48:42

can print here something like this also query and then user query or we can say it as first user user user

1:48:51

query and we can once we print it then also a line gap we can give so that better output is there

1:48:58

same way here also we can do that if i write print then i can say f and we can say second user query

1:49:05

and i can print a space also now i'll just push this command also so that you can see the output

1:49:12

in a better format as well and let me know if this program are you able to understand or not

1:49:18

how many people are able to understand the program now so you can see this is a second

1:49:24

user query and these are the results this is a first user query and these are the results correct right

1:49:33

i'll just push this program also like this is just a better way of like showing you how things

1:49:40

will work and yeah the same way here also this thing we can write down

1:49:46

i'll just push this command

1:49:48

on push this latest program get status get i think you don't have to put the

1:49:55

suction store and everything i'll just write here in git ignore

1:50:01

get ignore is that ignore all the files on get up since i want to ignore all these files

1:50:06

that is why i'm writing it i don't want those things to be pushed up right so if i write here

1:50:12

get status now only these two files are there i can write

1:50:18

git add star i can say git commish certain 18 changes and i can write get push so you can see

1:50:25

everything will be pushed up let me know like how many people are able to understand the command

1:50:31

here we have already discussed it right that why we are using convert to num pi as true because we

1:50:37

want to convert the data into proper vector we want the data to be present in a proper vector format

1:50:43

we want the array num pi is the library which we use to work with number

1:50:48

and vectors and all the like vector formatting of numbers that is why we are writing here

1:50:53

convert to num pi as true so that a proper vector or a array is coming up here we are writing

1:50:59

three results that is why we are getting three rank here we are writing two that is why we are

1:51:04

getting two rank mouskan is that part clear guys is everyone able to understand this program now

1:51:18

the distance is calculated using cosine similarity right archit the distance is

1:51:23

calculating while getting the results right like how do you think rank one and rank two and

1:51:28

rank three are coming up using the distance only they are coming up right here once we are

1:51:33

writing query command here you can see distance are calculated and those distances are

1:51:38

stored in this results that is why we are trying to print those distances is that idea clear

1:51:48

i'm not sure you can search like why probably a faster laptop will be required to

1:52:03

run that program that might be happening that is why this is coming up but ideally if you run this program

1:52:10

restart your laptop and then run it it will be fixed how many people are able to understand the program now

1:52:15

guys are you able to understand it or not

1:52:18

i'll push the notes also yeah just try to run it i think the program is clear right

1:52:25

how many people are able to get the program or get the output output also is everyone able to get

1:52:31

you need to follow these steps i'll just attach a screenshot of these steps also in the ppd so you

1:52:38

can directly go to this particular link and then probably run it and i think the main flow and idea

1:52:44

is also clear right that how i wrote the idea of this particular program

1:52:48

so it's a small exercise that i did so that you can see everything live in action also

1:52:55

so i'll just paste these two slides i'll just update from this slide to this slide and you can check

1:53:00

that out so same thing you can see i have written in the ppt also the entire program and theoretical

1:53:06

part all these commands are clear now right which sql part is not clear which sql part is not clear which sql part

1:53:18

guys still here are you able to understand so sqlite just open it again right if you have

1:53:31

installed sq light version then open it just go to here this extension and click on install

1:53:38

once you install it then click on chroma squlite click on this sqa light that is coming right once

1:53:44

you click on that sqa light part you will see that it will open you don't have to open the

1:53:48

bin file just open it it will open or restart your visual studio and then it open it will

1:53:53

open it again right restart it

1:54:00

install the extension and restart your visual studio it will be resolved

1:54:06

guys any doubts anyone is having till here i think we are good to go right and i think you guys

1:54:12

have requested that the session should be small so you will see this that every day now we will be

1:54:18

having just the two hour session like we will have like one hour 50 minutes of theory and the

1:54:23

last 10 minutes will be resolved for quays and we have increased the number of sessions that are there

1:54:28

that thing will happen so alchid this part is pretty much simple right you have all the numbers that are

1:54:39

there did you see here that all the numbers and everything are coming here if you see like if we

1:54:45

just run this particular program again so if you see all the numbers will be

1:54:58

calculated once all the numbers are calculated user embedding is calculated then we use

1:55:03

cosine search and we find out all the distances like what exactly is not clear you can see these

1:55:10

are all the embeddings user embedding also i showed you right that is also a number you take those two

1:55:15

arrays which are having 384 numbers and then you run a cosine similarity and you get a

1:55:21

distance so this is a distance that is coming what exactly is not clear here the less the distance

1:55:27

the better the rank will be as you can see this is the most matching one that is why it is having

1:55:32

least distance and rank one what is not clear here in this part it is using cosine similarity

1:55:39

search that is there right this is the efficient way only

1:55:45

this internally uses the efficient way only this is the extension name that i was

1:55:54

talking about this is an extension you can see on my screen as well we will create that project

1:56:01

right currently once we discuss the rag part then same code we will use and we will create a rack project

1:56:07

also currently it's a basic project to help you understand the embedding and everything is that part clear

1:56:15

still here this part is clear or not i have pushed everything on the like get up also

1:56:22

so just revise everything once again because i think today's class was very much complicated so

1:56:28

unless and until you try to do everything on your own after watching the recording you won't be able

1:56:33

to remember i think all these commands everyone is able to understand right are these commands clear

1:56:40

or not so just revise this particular part you

1:56:45

have a lot of time and just try to revise all these things and then we can see currently

1:56:57

it's not required rakesh because you will see with a i anyone can write that but you should

1:57:05

remember all the functions and how everything is happening same thing will be used are you

1:57:11

opening the correct file did you install the correct instruction did you install the correct instruction did you

1:57:15

install this exact extension and are you opening the sequel at file?

1:57:24

Share your screen. Can you share your screen?

1:57:34

Let's share your screen. Let's see. Because we have not created a sign in right?

1:57:43

We have not created a sign in right. We have not created a sign in request. We have not created a sign in request. We have not

1:57:43

created a sign in request that is there gharima currently we are not signing and you

1:57:49

have to be a panelist right to share your screen nopur i think other people is everyone able

1:57:59

to understand just share your screen

1:58:13

Can you quickly share your screen?

1:58:18

No, I cannot see your screen. Currently it's not visible.

1:58:27

Open VS code.

1:58:33

Go to the extension that is there.

1:58:39

Type in the extension name. Is this the extension name?

1:58:41

Is this the extension name?

1:58:42

Is this the extension name?

1:58:43

I'm showing.

1:58:44

Was this the one?

1:58:47

You have not typed even the name carefully.

1:58:51

You can see right the name is very different.

1:58:57

It's SQLite viewer that is there.

1:59:02

Did you type that?

1:59:13

Do you think light spelling is correct here?

1:59:16

SQL light spelling is correct here?

1:59:18

You are putting space.

1:59:31

You are putting space.

1:59:34

Delete that L.

1:59:37

Extra L you have put.

1:59:40

Second one that is coming right? That is a correct one.

1:59:42

that is a correct one. Did you install that? First one now.

1:59:46

Install it.

1:59:52

Let it install.

1:59:54

Now tell me, right, like whence I was showing you the extension, right?

1:59:58

Can you give me an explanation that why you were not able to find out the correct extension?

2:0:03

Just open first.

2:0:10

Open the file, let it install.

2:0:16

Now guys, to be honest, right?

2:0:18

Like, if you cannot even write an extension properly in a life grass, right?

2:0:23

Then it will be very, very tough to work in any company as an AI engineer.

2:0:27

To be honest.

2:0:29

They will not even spoon feed you, right?

2:0:31

Like with this kind of performance, you will definitely get did not meet expectation

2:0:36

and you will be like you will lose your job.

2:0:39

In companies, they will not be doing spoon feeding.

2:0:43

To be honest, I in class, right, every day I do spoon feeding with you.

2:0:47

In companies, they will not do this kind of spoon feeding that is there.

2:0:51

So you can see this, right? If you can't do these things, right,

2:0:57

then it will be very, very tough for you guys to actually survive in a company.

2:1:02

This is an honest opinion that I am giving you.

2:1:05

So just try to debug yourself and increase your problems.

2:1:09

skills that are there.

2:1:11

Because let's say that if you are not able to understand and follow the steps in a class,

2:1:16

you can watch the recording and then do.

2:1:18

In companies, if you ask these kind of questions, right?

2:1:21

They will give you a did not meet expectation and you will lose your job in six months.

2:1:26

That you don't want, right?

2:1:29

So only like these are very, very basic things.

2:1:33

Let's say that I understand that you are doing it for the first time.

2:1:38

Now, if you are doing it for the first time.

2:1:39

If anyone is doing for the first time,

2:1:41

you will do that research, right?

2:1:43

That what can be going wrong?

2:1:45

You understand that, right?

2:1:47

That you need to do that research, unless and until you do that research, right?

2:1:50

In a company, you cannot ask a doubt related to that part.

2:1:54

So let's say if this command is not working.

2:1:56

Did you do a complete research that why it is not working?

2:2:00

Unless and until you do that research, you will see this that

2:2:04

you will not increase your problem solving skills.

2:2:07

And if your problem solving skills,

2:2:08

problem solving skills are not improving.

2:2:10

Then how will you sustain in a company or how you will crack an interview?

2:2:14

I can teach you.

2:2:16

I can spoon feed you everything that is there.

2:2:18

But do you think with spoon feeding you can get a job?

2:2:21

The answer is no, right?

2:2:23

So make sure that try to do everything and try to do your research.

2:2:28

Because no matter whatever you learn, understand,

2:2:32

problem solving is the most important key

2:2:35

and problem solving no one can teach you.

2:2:37

no one can teach you problem solving you will only learn it

2:2:43

once you try everything on your own so try to focus in a class let's say if you're not able to do

2:2:49

anything i think a lot of people will not be able to do the setup today

2:2:53

but did you do that research that why it is failing let's say that

2:2:57

this is a error that is coming that torch is not working or pip is not working

2:3:03

and you are getting this kind of message that pip version is slow

2:3:07

or PIP version is not there then do you think you can upgrade that version right you can just copy-paste it and you can update that version

2:3:15

run the command and update the version of PIP copy the command and do that correct right automatically it will work

2:3:25

I think the idea is clear right did you get my intention what I'm trying to speak

2:3:33

that no one no one will be able to teach you that

2:3:37

problem solving part that is there so make sure that you do these things unless and until

2:3:43

you do these things right you will be stuck you will be in companies do you think with seniors you can

2:3:49

ask these type of things no right currently in class i'll help you i speak everything 10 times i'll show

2:3:55

you everything in detail 10 times but these kind of things you won't get in a company so try and do that

2:4:03

research if everything is not working just try that same thing

2:4:07

thing is with Purajan as well right if you are not able to follow do you do that research

2:4:11

that is there unless and until you do that research it will be very tough to survive in this

2:4:16

AI market that is there right so in the next class we will start with that that if you are not

2:4:23

able to set up i'll help you but make sure that you do that research and then you come to the class

2:4:31

so that if you do that research it will improve your problem solving skills you will be

2:4:36

familiarized with lot of things that no one has to spoon feed you and you can do

2:4:40

everything on your own that day if you get that understanding and meaning right that you can do almost

2:4:47

everything on your own then you can even learn better you can grow better and you will be able to sustain

2:4:53

better that's a main scenario so make sure that if anything is not working right no matter whatever

2:5:01

happens just don't give up and try to find a solution let's say that this program is not

2:5:06

working for me then what i'll do i can either skip this program or i can research about the

2:5:12

program and understand that what thing is not going wrong correct right only that thing we can do

2:5:17

if anything is failing any warning is coming those warnings without that warning also if everything

2:5:23

is working we are good to go currently you will see this that this warning is coming because sign in

2:5:27

with hugging face i have not done because if i do sign in with hugging face it will take 10 more

2:5:32

minutes so that thing we will not do it right

2:5:36

correct i think the idea is clear is everyone able to understand this idea

2:5:46

yeah i think kobel now you can take over just try this guys that you are able to do

2:5:52

these things and try that part oh all right uh it was well it was a very nice lecture today

2:6:02

so let's move on to the next section i'm just uh

2:6:06

rolling up the pole.

2:6:12

Please stay back after polls.

2:6:16

We'll have a quick quiz and then we'll wrap today's session.

2:6:36

You know,

2:7:06

You know,

2:7:36

You know,

2:8:06

I'm

2:8:36

I'm

2:9:06

I'm

2:9:36

I'm

2:9:38

I'm

2:9:40

I'm

2:9:42

I'm

2:9:44

Thank you.

2:9:46

Thank you.

2:10:16

Thank you.

2:10:46

Thank you.

2:11:16

your voice is not audible you are on mute your voice is not audible

2:11:23

you are on mute oh sorry so let's move on to the next question

2:11:46

What does count return and the options are total stored records, top K results, metadata only or distance scores.

2:12:16

The correct option is total stored records.

2:12:21

Moving on to the next question.

2:12:32

Which method is used for similarity search and the options are

2:12:37

Get, peak, query, count.

2:12:46

and the correct option is query.

2:13:16

Let's move on to the next question.

2:13:26

What is the purpose of metadata and chroma?

2:13:30

And the options are store passwords, store extra information, create vectors or install packages.

2:13:46

and the correct option is metadata stores extra information.

2:14:16

Let's have a quick look on the scoreboard.

2:14:23

Moving on to the next question.

2:14:31

What does peak help you do?

2:14:35

And the options are delete records, view sample stored grows, train the model, create embedding.

2:14:46

The correct option is it is used to view samples stored rules.

2:14:59

Let's have a quick look on the leaderboard.

2:15:16

And here comes the final question for the day.

2:15:23

What does lower distance usually mean in vector search?

2:15:31

And the options are less storage, wrong answer, nearer meaning in vector space or slower query.

2:15:45

And the correct option is nearer meaning in vector space.

2:16:15

