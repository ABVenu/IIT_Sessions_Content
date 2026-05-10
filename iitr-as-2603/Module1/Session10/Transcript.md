0:00

Thank you.

0:30

Um, Pratap, am I audible?

0:41

Yeah, you are.

0:42

Yeah.

0:43

So Pratap, today new industry mentor is joining, right?

0:47

So like we did last time, today I'll introduce him during the first two minutes and we can carry on over the session, okay?

0:56

Yeah, yeah, okay.

0:59

Thank you.

1:00

Yeah, okay, no problem.

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

Thank you

5:30

Thank you

6:00

Thank you

6:30

Thank you

7:00

Thank you

7:30

Thank you

8:00

Thank you

8:30

Thank you

9:00

Thank you

9:30

Thank you

10:00

Thank you

10:30

Thank you.

11:00

Hi students, how are you?

11:07

We'll be starting in another four minutes. We'll be waiting for others to join, okay?

11:30

Thank you.

12:00

Thank you.

12:30

Thank you.

13:00

Thank you.

13:30

Thank you.

14:00

Thank you.

14:30

Thank you.

15:00

Good evening, guys.

15:04

My name is Mamsia.

15:06

I'm your program coordinator.

15:08

I hope everyone is doing good.

15:10

So today we have Mr. Sionde and we are pleased to introduce a highly accomplished leader in the field of artificial intelligence.

15:21

And he is currently serving as the principal AI architect at the Ministry of Defense.

15:29

Qatar, Armed Forces, where he is building sovereign air gap LLM systems for military intelligence.

15:38

His work focuses on designing secure RAG architectures and multi-agent AI systems,

15:47

significantly reducing manual analysis time by around 60%.

15:53

He has also led high-performance AI optimization initiatives, including

15:59

QAT and VLM, enabling ultra-low latency and large-scale deployments.

16:06

And also beyond his role in defense, he contributes to academia as a visiting faculty at Caltech

16:14

and Purdue University and our very old IAM Bangalore, mentoring senior engineers

16:21

in full-stack AI systems. And with extensive industry experience, he has built

16:29

enterprise AI solutions for global organizations,

16:33

global giants such as Cisco, Siemens, Walmart,

16:38

and his expertise spans, Generative AI, MLOBS,

16:43

cloud-native systems, and also large-scale AI architecture.

16:47

With that, we are excited to have him with us.

16:51

Today, we are excited to have you, sir.

16:53

I'll now hand over the session to you,

16:55

looking forward to your insights and learning from your experience.

16:58

Over to you.

16:59

Yeah, thank you. Thank you so much, MAMC. So welcome everybody. Welcome to the session. And we will be starting on here.

17:10

I think mostly everybody has joined in. So good to interact with everybody. And I will start on with a little bit of context setting in terms of what we'll be doing, how we will be, you know, going over the sessions generally. And of course, as Bamsi has already introduced,

17:29

myself, I'm going to quickly also share my screen. So, so here is a, here is a small LinkedIn profile about myself, what I do. I think, again, great to be interacting with all of you as part of this cohort.

17:50

Okay. So, well, today we have a very interesting topic called SQL, and I was told that all of you are coming from

17:59

you've all done quite a bit of quite a bit of the the Pandas aspect so far, right? So just along a minute. So everybody in this audience has already completed. You've already completed until here. You're all comfortable with the fundamentals of Python. You've all seen operators, loops. You're all comfortable.

18:29

comfortable with variables. And what is directly relevant to the data analysis part, everybody in this audience has seen a very, very important module called Pandas. And a large part of what we'll be doing going forward, especially pertaining to SQL, storytelling, plotting. And finally, moving on to machine learning, a large part of that will directly correlate with what you have done in Pandas. Because that's where we are actually starting to work with tables and data frames. Okay.

18:59

What we'll do today, generally as a practice in my sessions, I'll be obviously walking you through some basic slides in terms of the content.

19:08

And from there, it's going to be a very practical hands-on session.

19:12

I will be sharing with you a lot of, a lot of code, a lot of code specifically we'll be looking at in terms of how to write SQL queries.

19:24

And we will try to understand what databases are.

19:29

where SQL fits in. How it is similar to what you have already done before. That is Pandas. What are the similarities in terms of the syntax? And we will do a lot of hands on in the session. We'll do a lot of practical hands on in the session where I will share with you some demo exercises. And on top of that, I will ask you to do some exercises along with me in the class. So that is a general way how I do my classes. It's very, very hands on, very practical where I also do some coding and you will also be doing.

19:59

some coding along with me. So the very important part will be that everybody should have some clear

20:04

takeaways at the end of the class. It won't happen in every session. Some sessions will be a little bit more

20:08

theoretical. But this particular class will be very practical because SQL is all about practical. See, for example,

20:14

if I talk about select statements and all that, it will be a very practical session. So the objectives that we are

20:19

trying to achieve today overall. These are the objectives that we are trying to achieve. We are trying to

20:24

understand what SQL is. So absolute fundamentals of SQL. We will see. We'll see tables,

20:31

rows, columns, basic things, right? Basic things. I'm sure everyone already has a flavor of that in

20:36

data frames. You've already seen data frames. So this one is relatable, I'm sure. But anyways,

20:42

we'll summarize this part. Number one, number two, we will discuss something called a select query.

20:47

What is the select query? How do we select rows from a table? The same way that you, you know,

20:54

print out a data frame in Pandas, you know, you will say display DF or print DF. And there are

21:01

different ways to filter your data in Pandas, right? You've all learned different ways to filter your data.

21:07

So same way, we will discuss filtering data using Warecloths. So the operations are very similar.

21:13

You've all discussed how to, how to effectively sort your data in Pandas. You've all seen sorting.

21:18

And similarly, we can all, we can also go back and do sorting in SQL. And similarly, we can also go back and do sorting in SQL. And similarly,

21:24

if you remember in Pandas, there's a syntax called dot head, right? You do something

21:28

called df.f.head. So you have something very similar called limit in SQL. And we see those parallels

21:35

as we go along. So it's fairly simple, fairly straightforward. So I think the, if you look at the core topics,

21:40

the core topics are really simple. But what I have tried to do in the session is try to incorporate

21:45

lots of demos, lots of exercises across a variety of different use cases so that you get a very good

21:52

end to end understanding of how databases really work. Okay. And again, what we are

21:58

really trying to do is not to make you exports in SQL because you can see SQL is only two classes we

22:03

have here. SQL is massive. There is no end to what you can learn here. It is massive. But obviously,

22:11

you are here to learn about generative AI. And only as much as SQL is required for your role,

22:17

we are teaching you only as much SQL here. Now, how it connects, what is the relay, how

22:22

is this related to all that you will do going forward? So those are things we'll be discussing

22:27

as we go along. Okay. And again, I think general guidelines for the session, please be interactive.

22:36

I think it's always good to hear from everybody. So when questions are asked, do keep answering,

22:42

do keep responding. So I think your energy, you know, we'll keep the session interactive.

22:47

And also on the chat, I always recommend keep your settings to everyone, right?

22:52

So when you're typing something, everyone gets to see who is typing.

22:56

Otherwise, it is like a blank canvas. You use the staring at me and I'm staring at an empty board.

23:01

So let's try to make it a very vibrant session going forward. Okay. All right. Now, I wanted to check one very important thing with all of you.

23:11

My team did tell me that they, you know, they did share with you how to install something called MySQL Workbench.

23:18

Do you have any idea what is MySQL workbench? You guys, you guys know that?

23:21

like again i'm not saying that you have to know but

23:25

i'm just trying to understand do you have you have you ever heard of this thing called

23:29

my SQL workbench and have you guys installed this thing have you guys installed this thing have you just

23:34

wanted to check you you know this you have some of you have might you can just let me know if

23:40

it's a no you can take it's a yes you can say it's okay it's not a show stopper but i just wanted to

23:45

just wanted to understand if some of you have uh so so in the previous tutorial

23:51

that i got them to install d b uh d beaver and db so they won't have my sq

24:00

they would have a pg admin from post gray sq and db gate uh and db gate or d bv

24:07

assuming they're going to be learning like the basic sqq commands that's a basic SQL in that

24:12

case yeah yeah so that's fine so in that case prath what we can do is okay no problem it's not a show

24:16

stopper not a show stopper don't worry uh well in that case we will look at some online editors

24:21

and we'll do some queries that's okay it's not a show stopper and i think i think it doesn't uh so they

24:25

have done one session on sql with you you have already introduced them to uh basic database set up

24:30

already right yeah just the database set up nothing nothing good wonderful okay yeah so again

24:36

that's okay that's okay it's not a show stopper um what you guys can do is please keep this link handy

24:44

please keep this thing handy everybody just go here forget about the setup let's let's ignore that for a minute

24:51

just keep this link handy and all if you can go to this page and this is where we will try to

24:56

do all our demos together okay simple straightforward and as and when i keep sharing the

25:01

snippets with you you can go and copy and paste it here and you'll be able to do all your exercises

25:06

and demos here okay so straightforward this is the way how it will basically work out uh

25:12

access denied let me just check okay we'll see this one okay so now uh moving on

25:21

just give me once again i just want to check if this is fine you guys can

25:32

yeah the database part you can ignore i'm just going to share this one with everybody so that

25:36

people can can work with this thing going forward and another thing that i'll be doing in all my

25:43

sessions is i'll be sharing with you uh i'll be sharing with you you know a google drive link

25:48

where all the contents will be neatly organized so this is your this is your cohort uh

25:55

google drive link that i've created it's a one time thing i'm sharing so that going forward

26:00

everybody knows what session what contents i'm sharing right so every session there'll be

26:06

one set of snippet files i'm i'll be sharing with everybody so let me copy the link

26:12

and let me quickly share this with everybody on chat okay so i'll quickly share this with all of you on chat

26:18

there's just one small edit i'll be doing

26:31

please do confirm to me if you are able to see the google right that i have been right now all good guys

26:41

okay wonderful wonderful everyone everyone i just want to

26:58

i will also upload the sq file don't worry what this is i'll explain to you what is the dot sq

27:03

file in a moment i just want to make sure all the files and everything is shared so that we can uh

27:08

we can walk through it together everyone's able to access my drive link so you can enter into the

27:13

main drive link and uh based on the session dates today's 27th april i'll be sharing with you

27:18

the files with respect to each and every individual day

27:28

so now let's continue our conversation and understand to start with why do we need

27:53

databases what is this concept of relational databases and why relational databases are

27:58

required because everybody in this audience is coming from a world where you have seen

28:05

possibly CSV files right that is majorly a specific type of file format that most of you have

28:11

been exposed to everybody in this audience has seen a CSV files you have a CSV file and you're

28:17

loading that into a data frame that is the framework you're all used to or an excel file right but see the

28:23

problem with CSV files and the problem with excel files and all these different different file formats is

28:28

that they typically tend to break so at a high scale at a large scale these kinds of

28:38

tools will typically tend to break so if you look at it if you look at the left-hand side if your

28:46

excel crosses beyond a certain number of rows right if you so excel is such a popular storehouse of

28:53

data right when you want to save something what is the first thing we do we think of Microsoft Excel i'm sure

28:58

everybody is using excel but have you ever realized have you ever realized that when you go and

29:05

open up excel i'm just opening up excel in front of you right you know the number of rows in

29:12

excel the total number of rows in excel how many overall number of rows you have you can hit shift control

29:18

down and once you do that you can see how many total number of rows we have in excel this is the total

29:23

number of rows excel supports one million one zero four eight five seven six

29:28

surprising fact right and you know how many columns excel supports excel supports again you can do

29:33

control right control down control right you can do excel supports xfd and this is a again a different

29:42

you know a math but you can do some permutation combination which supports basically that many

29:47

number of columns so this is the total number of columns that excel is supporting right so close to

29:55

a million rows of data we have so close to a million rows of data we have right now

30:02

and we have this many number of columns so that's the basic idea okay now

30:12

another very important aspect of Excel is that you cannot store your data

30:20

if you look at Microsoft Excel you cannot

30:25

like you can store your data of course but you cannot make modifications and it's not

30:29

in the format that you want it oftentimes so for example if i go all the way to the top

30:36

and these are things everybody has worked with see i can type let's say uh 14 here so imagine

30:43

imagine this is a typical employee stable i'm trying to create okay everybody has a flavor of

30:47

data frames by now so all of you can relate to it we have employee name we have employee salary

30:51

okay so this is what i'm doing right now so i can type

30:55

employee name is iron salary is let's say 10 employee name is let's say john salary is 20

31:01

okay i can actually have another thing coming up here like this i'm just saying like sham can come

31:06

somewhere here now excel is not a place where you can actually set these kinds of constraints

31:15

now there are ways to do it you can do data validation there are ways to do it but it is not a place to store

31:20

data. Excel has historically been very popular for you know performing basic spreadsheet

31:28

tasks and all those kinds of things but it is not a great thing to store data. So these kinds of

31:33

integrity checks it will fail. Number of rows and number of column checks it will fail. I already

31:38

told you what is what is a million rows of data? Million rows is actually very small. I mean if you

31:43

think of if you think of a real world application, I think people will agree with me a million

31:50

rows of data is actually very small very small million rows of data is very very small

31:54

scale we are talking about you know real world applications we are you know we are talking about

32:00

hundreds and millions tens of millions and if you're talking about transactional data imagine we

32:05

have got credit card transactional data credit card transactional data can go into several

32:09

billions of those tens of billions hundreds of billions in a month how do you store that in exit

32:14

you cannot storage limitations number two if an excel file is very

32:20

big i'll give a i'll give a very practical example if you have ever seen excel or imagine a c sv

32:26

files you guys have worked with in your prior sessions right try opening up a c sb file that is very

32:31

big it will take a long time to open retrieving the information is very hard right so imagine

32:38

you have a massive excel file and we can simulate one actually if you even if you end up creating

32:44

a massive excel file retrieving the data from there will take a lot of time because the file is so

32:49

big retrieval is not efficient it's one thing to have the data right it's one thing to have

32:54

information about all these employees and like that and i can have it right i can actually go and simulate

32:59

a data set for you like shy and john sign john like this and i can simulate this data set for you

33:04

right but my point is retrieving this data will be very difficult so we so this is

33:11

so this is exactly how the concepts of databases was conceived so databases are not a new

33:20

thing so flat files we call them flat files you know what is the term we use so i'm calling

33:25

i call it flat files so flat files are basically files like excel files c sb files

33:31

they're called flat files typically notpad a notepad made

33:35

now notepad is again a simple very raw file format right you can write any text anything you can store there

33:41

these are called flat files in practice so they break at scale if you are storing a massive

33:48

amount of data you cannot they're slow to open hard to query they don't handle billions of transactions

33:54

and this is exactly what led to the origin of databases databases are not new databases have

34:01

been around for a long long time there's been decades since we have been using databases the initial

34:07

the idea started around 19 1980

34:11

that's when databases were invented i would say and and and that is exactly what we are talking about

34:19

in this session so databases they handle billions of rows we are not facing that 10-lack row crash

34:26

anymore like what we saw in excel we don't have a memory limit issue

34:31

single user coalition this is a very interesting thing uh what am i talking about

34:37

now look concurrent users what if you have ever worked with excel uh let's say you and i work in the

34:45

same team okay you are from hr i am from hr and we are trying to hire some uh candidates

34:51

okay so excel open so let's open it out see because when you are studying a topic people should

34:58

understand what are we doing you know like sq1 to tickeye okay

35:01

two queries sql go get there's nothing in sql i always say the concepts are very

35:08

important why we are learning something it's not that ki be just learning sq are the topic

35:12

you know spend two hours and go home no you should know why we are learning it that is the

35:19

see once you know why you're learning something that will motivate you the history the background

35:23

the origin this is very important okay because sql is very easy i'll tell you today's today's

35:28

session believe it or not i'll start with the syntax in a moment

35:31

today's session is maximum 15 minutes to 20 minutes it's actually very easy so the topics

35:37

are very simple but it's more about the case studies and all that we will add towards the end so

35:42

that's why i want to dedicate the initial time to the context setting like what is it how they are

35:46

helpful and all that okay so imagine we are working on a hr department okay see i'm i'm an hr

35:52

team and let's say we have one of you i'll take like let's say one of your one of your names here let's say

35:57

we have uh uh uh pranjal is also from hr so me and

36:01

we are working on the hr department okay so now what are we doing we are trying to hire candidates

36:07

okay now the candidate's name his salary is what salary we are offering this information

36:13

okay let me just let me just let me do this so i am you know i i am starting to hire a person

36:21

and i have entered some details he's name this salary is like let's say we are offering 10

36:25

lakh location and all this take and i'm trying to update the details and selected criteria

36:31

selected will yes or no okay i'm saying selected yes now

36:35

parallelly what is happening and let's say uh this is only one xl5 now

36:40

parallelly what what will pranjal do we he is also from the same hr team he will have his own

36:45

excel file you see the problem see the disconnect this this has been a huge issue

36:49

historically if you go back to the 1980s the pre-1990 era this this was a big problem people were

36:56

having different different versions of excel file you know like i am from hr

37:01

i will have my own candidate list john 10 lakh me select okay and pranjal will have his own

37:07

excel file sham 15 lakh me select now very interesting okay i will have my version

37:16

pranjel will have his version now we come to now what happens is pranjal will not have a real

37:22

time visibility can i interview here okay so what he does he will also talk to john parallel because

37:27

he will not know that i interview john so let's i'm going to maintain this

37:31

to maintain this two parallel version just for your reference so let's say this is a my

37:37

excel sheet and i will i will just create uh one more excel file just to simulate the

37:43

similar the demo for you and let's say this is a runger's xcel sheet he'll also have a very similar

37:52

kind of a structure he's also talking to multiple people so he hired sham at nine dacks

37:57

and he will have a different process people will interview they will interview sham they will

38:04

offer and let's say uh shams expected salary was this much and selected yes ticket whatever okay

38:10

okay now many such row entries we create like this now this person pranjel will have no idea

38:18

about my sheet right because my sheet is in my system in my local machine so pranjel also rings up john

38:25

duplicated who got hired from me also with a salary of 10 lakh but john is a smart

38:33

person now john to understand here pranjal go to know the same company two people are there

38:39

one person doesn't know what the other person is doing now john who's

38:42

with him negotiate with him so there negotiate and john made his salary 15 luck

38:45

selected yes he the problem these are both one and the same people so i don't know what my colleague

38:53

is working on and my colleague doesn't know what i'm working on and my colleague doesn't know what i'm

38:55

working on and benefit con will take a candidates

38:59

so john will now talk to both of us

39:01

both of us both of us

39:04

that creates a problem this was a huge issue

39:06

when it looks it looks it looks impossible today

39:12

but if this was a real issue back in those days

39:14

it was a big problem because people are different different

39:17

versions of files duplicate updates used to happen

39:20

and i will use a very important term right now for you

39:23

integrity, consistency, single version of truth.

39:29

okay? Integrity, consistency, single version of truth.

39:33

Problem is there was, there is no single version of truth.

39:37

If you are having physical files like this,

39:39

if you have an Excel file, CSV file,

39:41

note pad, you have data save for you,

39:43

what single version is right?

39:44

Now, a team in a new HR, let's,

39:46

let's let me, we're going to go,

39:47

our Excel to go, no.

39:49

I'm giving you a very practical thing.

39:51

See, companies will have ways to

39:53

duplicate the data whatever right but i'm just saying as an example let's say you are very angry

39:58

with the company for firing you okay at the end of it all you delete all the reports what is the

40:03

track of it so tracking was very difficult back then auditing was very difficult okay these were real

40:08

challenges so these all led to the origin of databases okay so databases help enforce these things

40:17

billions of rows possible permanent disk storage okay there is not nothing for temporary

40:22

permanent everything is permanent thousands of concurrent users can

40:26

parallelly do it it is not like only one person at a time can update it no there are

40:29

thousands of people concurrently who can update so if you talk about my setup right now

40:35

it you know i i am part of the operation hr team and i have 10 colleagues who are

40:39

parallelly working all 10 of them can parallelly access that database and finally the last

40:45

point that i also demonstrated is strict data rules

40:48

if you have a column he that column in that column you can store text you can store

40:55

other things no in that column only number will get stored so you can set very specific rules of how

41:00

data can be stored in a particular table so this is basically the concept of a database what

41:06

databases really are okay now now that you guys have done a little bit of uh pandas in your

41:14

sessions and i wanted to draw this connect with all of you

41:18

if you talk about excel if you talk about c sb you know and if you talk about pandas data frames

41:24

also like whatever you have used in python so far what what are we talking about there these are

41:31

only temporary right a data frame is not permanent right i hope everyone's aligned on that a

41:36

data frame is not permanent store of data whatever data frame you are using a data frame is not a

41:43

permanent storehouse of data right it is only temporary but a

41:48

but but a database a database is permanent it is stored on the disk as an actual file

41:58

okay so that is a very important thing to keep in mind otherwise when you're doing something in

42:02

pandas it is only temporary it is a variable in python but it is not stored in the disk

42:08

if it is a file it is stored in the disk but otherwise it is just a variable in python you are

42:12

saying you remember the syntax df equal to pd and dot read c sb i'm sure you have seen this code

42:18

in your funder sessions right what are you doing you're creating a variable temporarily if you close

42:24

your vs code or collab you might have worked on vs code or google collab so far right if you close your

42:30

vs code that variable is gone can again concurrency single user access the same issue that i talked

42:37

about multiple people cannot do it right in your python environment three people cannot update

42:43

your data frame right these are issues three people cannot uh

42:48

do it multiple you know overall so but we will see in databases these things can happen

42:55

you can do a simultaneous read-write multiple people paralleally can access in an hr department

43:01

we have some logg here so log so log sat me access can integrity so you can have you can have

43:10

text in a salary column for saudas is very flexible and uh say i think it's best if i show you

43:17

be an example because i don't want to make it a panda session but if i think if i show you it

43:21

will it will make a lot more sense so let me go and uh just take a small two minute digression okay

43:29

so i will open up my i'll take a simple data set for you just so that you are able to

43:37

understand the case study better let me take a simple data set for you

43:47

people in this audience have you worked with uh you guys have worked with bs code or collab what are you

43:53

comfortable with in the classes are you are you comfortable with bs code or collab just wanted to

43:57

understand so i'll use that platform only bs code okay okay okay okay just wanted to check everyone

44:02

has used bs code right okay okay okay okay done because i don't want to use collab because you guys have not

44:05

seen it okay okay no problem going forward in the classes i will teach you collab is is is is amazing right

44:11

so collab is actually part of the plan so going forward in the entire agentic AI course we will do the entire

44:17

on Google collab because collab is very easy it's easy to use it easy to code in okay so we will

44:22

see collab we will learn collab in the upcoming sessions for now let me go and uh

44:32

let me one second i'm going to go ahead and create a small demo notebook here right now

44:47

So here it is and I'll just open up my BS code here.

45:17

a jupita notebook right now let me go and create a quick jupita notebook and here what i will do

45:24

i will import pandas as pd everybody has seen this code straight forward and pd dot read underscore

45:32

c sb pd dot read underscore c sb i will read the iris dot c sv i will read the iris dot c sb data frame

45:39

okay so yeah so simple's syntax that you guys have all seen okay now think about it it it's a

45:43

demo here demo here demo here what is this demo is a temporary

45:47

variable and now iris dot c sb is a file it's a flat file that we have been discussing so

45:52

far this has many limitations there number of rows concurrent users all that at a time only one

45:57

car at this is not the right way to store data okay and also the data frame that you did

46:02

data frame is just in fund us it is not a it is not a way to store data it is only a temporary

46:08

storage of here so if i if i show you the data frame right now this is your data frame one second

46:17

this is a simple data frame we have right now and this is a local storage

46:39

that's what i meant by that is exactly what i meant by the concept key it is stored only by the

46:46

stored only while running but single user access because this is your python

46:50

our python is our python we have demo you are loading it you will call it df

46:56

okay kis some variable name did you anybody can give any variable name it is only

47:01

present in your system and we're demo to do anything so i can go and create a new

47:06

column everybody has seen those things now you can create a new column you can delete a row

47:09

you can delete a column so we are all creating our copies see the challenge there is no

47:16

single version of truth okay so data frames are a way to analyze data please remember data

47:24

frames are a way to analyze data then you go up here it is not a way to store data it is not a

47:29

data storage medium okay so that is just one thing i want to clarify and and the other thing is it depends

47:36

on your ram limited by local ram because whatever data you're storing it depends on your memory

47:42

main memory okay so these are all

47:46

all limitations that you have right now and integrity very important you can store anything

47:51

abe your sepal length column here these are all numbers right you have a text me store

47:56

can't say very flexible if you have a column you can store number text anything for that matter

48:02

the only difference is what is the difference if you go back and do demo dot info

48:11

right now it is floating point it will become object type type that's the difference right now it is floating point it'll become object type that's the difference

48:16

right so these are all limitations i want to talk about speed

48:20

okay scalability okay security there is none these are the areas where databases

48:25

actually are very very important so this initial part of the conversation is to let you know

48:29

and help you appreciate why databases we needed a specialized form of storage

48:34

where we can store can't not just one table iris to a table here we're talking about

48:41

hundreds of tables in a typical enterprise schema you typically have hundreds of tables in a typical enterprise

48:43

schema you typically have hundreds of tables at your story hundreds of tables spanning

48:49

hundreds and billions of rows and it can literally be worth gbs a typical enterprise level database

48:56

can be worth gigabytes in store in size that's what we are talking about with all the beautiful

49:02

features like concurrency and all those things that we talked about you can just keep this at the back

49:07

of your mind a guy this is our discussion of go ya but this is just a bit of a context setting in terms of what

49:13

databases really are and the type of databases that are that are the focus of the session

49:20

right now is relational databases this is what we are focusing on in our session okay again we are

49:25

not getting into databases as a topic here because that is a massive thing who our contentment

49:32

we are not getting into no sequel and other things you don't have to worry about these parts this is

49:36

just for your information for our understanding we are only concerned about this

49:43

relational databases is like a tabular structure where data

49:48

data a table kind of stored in terms of rows and columns okay so we are basically

49:53

storing data in terms of rows and columns straight forward

49:57

just your example here I'm an employee data for name salary data

50:00

name salady Irish data frame okay it's the same way that you have learned things so far

50:04

this is the kind this is the way how we will basically store your data in a typical

50:08

database rows and columns here is clear I don't think I don't think I

50:13

to explain to you row what are column here guys and like but everyone can understand

50:17

this is your row is or you your column here data frame concept exactly the same way

50:22

you're your table here the same thing we will be storing in a database in terms of rows and

50:27

columns so remember database is a storehouse of data database is a stored house of data

50:33

here we're we're stored here we're stored here and sqr

50:36

we're looking we're from there data retreated that's the thing okay so next time anybody tells you

50:41

what is an RdbMS what is an RDBMS? What is an RDBMS? J relational table is,

50:46

what is what? RDDMS is it? RDBMS is stands for relational database management system okay.

50:52

So what is the term I'm using right now? I'm using the term RDBMS and RDBMS stands

50:58

for relational database management system. Let me just write it down. It stands for a relational

51:05

this one

51:08

look guys

51:08

relational

51:09

database management system

51:13

the R stands for relational

51:14

this is the very common term

51:15

that you will hear in the industry

51:17

and here we are storing data

51:19

only in the form of a table format

51:21

okay

51:22

so you're putchews

51:24

so the other thing

51:25

is the non-relational

51:26

what are only differences

51:27

here here are

51:28

other type of data stored

51:29

which we're not in

51:30

you can store images

51:32

you can store text

51:33

and all that

51:33

which is a very different thing all together

51:35

So here you can also store something other than tables.

51:38

But the focus area right now is just RDBS

51:42

where you're storing data in a table form.

51:45

From tables, how can't you are wondering

51:47

how do we store data other than tables?

51:52

We'll look at back in.

51:53

When we come to agent K AI, we'll discuss vector dbs.

51:55

Vector databases are also another kind of databases.

51:58

What are other kinds of databases which are not relational?

52:02

We will see some of those things later in the course.

52:05

So this is the way how we look at a typical relational table.

52:08

You have rows, you have columns, and very important, you have something called a primary key.

52:14

A primary key to be concept.

52:16

Okay, so what is the meaning of a primary key?

52:18

Primary key is a unique, unreadable, unrepeatable record.

52:24

That's your primary key.

52:25

So whenever you look at a typical relational table, you have a, you also have something called the primary key.

52:30

If I have to give you a simple example of this, okay?

52:33

So we're in Excel in the start in.

52:34

And then we'll come to the implementations in MySQL in a moment.

52:40

This is your ID, this your employee ID here,

52:44

this is your employee name and your salary name and your salary is and your salary is and

52:48

more information.

52:49

This is the typical employee table.

52:51

If you think of a typical table, this is your table and these are the columns.

52:56

Colombs in columns in you will have the data for the table.

52:59

And rows may, he will have the data for the table.

53:02

So employee ID has 1.01.1.

53:04

and name is John and salary is 10 lakh.

53:07

Okay.

53:08

Employee ID is 102.

53:10

Name is sham and salary is 25 lakhs.

53:13

Okay.

53:14

Employe ID is 103.

53:16

Name is Ravi.

53:19

Employ ID is 30 lakh.

53:20

Okay.

53:21

Employ ID is 104.

53:22

Very interesting.

53:24

Person can same.

53:26

Agreed.

53:26

A person can have the same name.

53:28

But employee ID will never be the same.

53:31

And interestingly, salary be same.

53:34

I mean, apparently, it was that he be John and this John

53:37

also be 10,000 in recruited.

53:40

So this is the interesting case.

53:41

This is what we call a primary key.

53:43

Okay, so I'm going to color that column.

53:45

This particular column is what you call a primary key column.

53:48

So primary key is the primary key is meant that particular column never repeats.

53:52

A name can repeat, salary can repeat,

53:55

two people in the company can get the same salary.

53:57

Like, John is.

53:59

Now, company in two people's name be same.

54:01

Two people's name John.

54:03

Okay.

54:04

then employee ID will never repeat.

54:06

Employer ID will always be unique.

54:08

Like, your Adhaar number,

54:09

customer ID got,

54:10

you know,

54:12

you know, banks in data

54:13

how are stored that same way?

54:14

Real world scenario we're talking about.

54:16

How do banks store data?

54:17

Banks have a customer database.

54:19

Okay.

54:20

That's got a database management system.

54:22

Banks also have something called

54:23

our DBMS.

54:25

So let's say ICICA bank.

54:27

ICIC bank has a RDBMAS system

54:29

and in that DBMS,

54:30

in that database,

54:31

there will be many, many tables.

54:32

a table will be customer's table.

54:35

There'll be transactions table.

54:38

Multiple tables will be there.

54:39

And in each and every table,

54:40

you will have the records.

54:41

The same way that we're explaining.

54:43

So customers table in Kha

54:44

ICACBanker, you will have the same thing.

54:46

Customer ID will have.

54:48

You know, the customer ID,

54:50

you will have the name of the customers.

54:52

You will have the bank accounts of the customer,

54:54

things like that.

54:54

And I think everybody knows that customer

54:56

for a customer is always unique.

54:59

Very interesting.

55:00

A person can have multiple bank accounts.

55:01

your multiple bank accounts

55:03

can, but it's always related to one single customer ID.

55:07

So for banks, typically,

55:08

customer ID is always unique.

55:09

Two people cannot have the same customer ID.

55:12

Okay?

55:12

So for every table, whenever you're creating tables in a database,

55:16

always remember the concept of a primary key.

55:19

This is what is called a primary key.

55:21

Unique.

55:22

Always unique for it.

55:23

Okay.

55:23

Now,

55:24

now you're,

55:25

you ask,

55:25

you ask, sir, this is common sense.

55:28

Some part of this is understanding of your data.

55:30

So, whenever you're working on a problem statement,

55:33

you have data to summarize.

55:34

The data set is what is the meaning of the data?

55:37

That you need to understand also, right?

55:40

Okay.

55:41

So now, let's move on.

55:43

And this is pretty much the entire piece and the focus area for today is select statement.

55:51

And let us see, this slide is telling a lot of story in terms of what we have done so far and what

55:57

we will be talking about today.

55:58

And now we will be beginning our demonstration.

56:00

from here onwards after the initial context setting, okay?

56:03

So this is what we call a database.

56:06

You have a database, okay?

56:07

All of you can see, this is what is called a database.

56:09

Okay, one second, guys.

56:11

This is what is called a database.

56:13

This is called a database.

56:14

This is where all your information will be stored.

56:17

And remember, a database can contain more specifically,

56:21

I'll call it a relational database.

56:25

Yeah, then a more specific term is called RDBMS.

56:30

Okay, it's go. Actually, RDBMAS, it's going. And this typically contains multiple tables.

56:41

A typical RDBMS typically contains multiple tables. Please remember, it doesn't contain just one table.

56:46

It contains multiple tables. Now, on one hand, we have a database. Now, one more thing, guys,

56:54

just one thing quickly.

56:56

Database made tables. This is like a massive vault.

57:00

very secure. This is how we tried to visualize this whole thing.

57:05

And it's in there are many tables.

57:07

This table. This is. This table. This table. This is. This table. There are hundreds of tables.

57:14

Now, you think, sir, this is, what is? This entire thing is like one file.

57:20

This whole thing is stored internally as files.

57:23

As you know, just we create a text file, Excel file, CSP file.

57:27

You have a word document, ppt, berno, downloads, save.

57:30

You save it in the computer. You all do that, right? You create a document and you save it.

57:36

You know, demo. Dot doc, whatever. So same way, this is also stored in disk. This is

57:46

a hard disk. So this is permanent. This is very secure. Okay? Nobody will have access to me.

57:53

It's not that our computer file system is that any computer downloads may go and access to

57:57

I know. This is very secure. People cannot access it. For people to access it, they need a password.

58:03

So this file system is very secure. So this is how the data is internally stored. So database

58:08

in kahi sara tables and these tables are internally stored as files. Let me put it a little bit more

58:15

clearly to you. These are basically, maybe in a bit of a non-technical way, these are basically

58:23

stored in hard disk as unreadable file.

58:27

as unreadable files, as unreadable files. And why do I say unreadable?

58:40

It means no people cannot just go to the, this can open that file like a not pad file

58:46

or call Khol Kekli. No, it doesn't work that way. You need a very specific way to access those

58:52

files and that I will talk about now. So file to access can say. And that is exactly where SQ

58:57

well comes in structured query language.

59:01

SQL, look and we're going to find of it that way. That's the, that's the big picture idea

59:05

of what databases really. So SQL is the interface to interact with the database.

59:14

Okay? Database in tables. Tables are internally stood as files. Those files are not readable.

59:18

A human being cannot just read the file. It's not like a word document that you open it up and

59:22

you see what you see what you can't read it. You can't read it. So to read the contents of a database,

59:27

it's in this. You have a customer stable? You know, you look at it? So,

59:32

that's, we use it. So what is SQL? SQL stands for structured query language. So this is a

59:39

beautiful analogy that I wanted to share with you. You do not search the vault yourself. This is a

59:44

long, a vault. Volk, obviously you can't open it. As we've said, that files under up, you can't

59:49

see into the vault. You cannot see into the vault. You don't search the vault yourself. You speak to

59:55

the librarian. An SQL is the universal request system. SQL used to access

59:59

access. And SQL is the universal language that you use to interact with every relational database

1:0:07

in the world. Every. So there are many relational databases out there. I think you guys have done

1:0:14

like Pratap has helped you with DB2 or whatever. Whatever database you have got. I was talking

1:0:21

about my SQL. There is something called SQL server. There is something called post-grathe.

1:0:25

SQL. Doesn't matter. What we are focusing on is not a database. What we are focusing

1:0:30

on is the language. Do we know the language? No way. It doesn't matter. You have DB2 have MySQL

1:0:36

has SQL. Some, some variations are. But we are talking about the universal language for SQL.

1:0:43

I'm SQL use and that data query to try to understand what is inside those tables. Okay.

1:0:49

So that's the basic idea. And the most important part,

1:0:55

of the conversation we'll be doing is something called a select statement. This is the major focus for today.

1:1:00

A little bit more things will be thinking, but the major focus is select statement.

1:1:04

Select statements from data query. This is called data query language. So we can query our data

1:1:08

using a select statement. So select start from a table. You have a table and you want to select

1:1:14

select that table in the table. We can use a select statement to see the rows in the table. Very

1:1:19

simple. We'll see select statement. You can use it. Okay. Similarly, other other

1:1:25

things are there. You can hear something called DDL. These are basically some

1:1:30

theoretical ideas that you can remember. The last part of the theory we are basically discussing. We

1:1:34

go to hands-on norms. So DDL stands for data definition language. Here here you

1:1:38

you can create. You can't. You can't. And usually, it's permission's not. You're not. I told

1:1:46

you that this is your database. Here's already five tables being. You already have five tables

1:1:51

created. Now, you want to create one more table. You have one more table. You have one more.

1:1:55

table. So you are to write a create table. But as you can imagine, this is very

1:2:00

sensitive and usually people will not have access to this. So this is a very, very sensitive thing. You are

1:2:06

allowing somebody. Now, manu, this is a bank database. Imagine this is a bank database system.

1:2:11

If this is a bank, a database, you think anybody will have access to right? No, right access

1:2:17

not. He'll create access. So DDL is a very sensitive to. Only few people in the enterprise will have access to it.

1:2:25

Usually, DDR you will not do, and that is not the focus area.

1:2:28

Even in our typical analytics role or GNI role, DDR is not something you will do.

1:2:32

This is the work of, you know, those database administrators, who companies in DB admin

1:2:38

are, you know, admin roles, right?

1:2:42

Who user access, these are control. They are the ones who are doing this word.

1:2:46

He will a table that, you know, that is the way how it works.

1:2:50

It's basically not our edict. You're not going to worry about creating tables.

1:2:53

But just no.

1:2:53

Next time anybody asks you,

1:2:55

what is the meaning of data definition language.

1:2:59

I want everybody to know that what is what?

1:3:03

Second, we have something called data manipulation language.

1:3:07

Data manipulation language is basically where,

1:3:09

now you want to insert rows in a table.

1:3:13

Now you want to insert rows in a table.

1:3:15

How do you do that?

1:3:16

You can write insert statement.

1:3:17

This is data manipulation language.

1:3:19

That table in you have insert.

1:3:20

Even this is very sensitive.

1:3:23

Create table and insert.

1:3:24

Both are very sensitive.

1:3:25

sensitive. If you can insert or delete be. Now imagine you are I say say bank.

1:3:30

This is actually very, very, very dangerous, right? Bank in bank, in the transactions table

1:3:36

will be. All your UPI transfers, you pay, money transfer from person A to person B, whatever you do.

1:3:43

Those sara transaction table in a, what day, how much you transferred, from whom to whom, how much amount,

1:3:49

everything, mode of payment, everything. Now, imagine, if somebody has something. Now, imagine, if somebody

1:3:54

has, it writes a DML statement.

1:3:57

In a, a, a, a delete statement marred via.

1:3:59

A update statement marked here.

1:4:01

And we have heard these stories, we have all heard these stories.

1:4:04

He's all heard these stories.

1:4:04

He's a account in 10-corroar got.

1:4:06

Some, some small businessman,

1:4:10

he, who's got, up, a $1.00 account in it was.

1:4:13

How's how are?

1:4:15

Because at the end of the day, it's a table.

1:4:16

It's a database.

1:4:17

That's a transaction stable.

1:4:19

A customer's table.

1:4:21

And, the, galties, one up there's a update statement

1:4:23

went to go. Now, it's, it can't, kisn'n't have done-posed-keyed, whatever.

1:4:27

These things actually happen.

1:4:28

So you can see how sensitive this is.

1:4:30

The inserting data, updating data, again, you will typically not do.

1:4:35

Our session will be from the next upcoming.

1:4:38

We'll just look at all the, write the code.

1:4:41

Just, our main focus is there.

1:4:44

We will not worry about creating.

1:4:45

We will not worry about creating.

1:4:47

We'll insert values insert, and now your objective will be to read the data from there.

1:4:53

Exactly how you were doing in Fandas, right?

1:4:55

Pandas in the data made.

1:4:56

It's not as if you go and go to that data create correct.

1:5:00

You've worked with different data sets, right?

1:5:01

CSP files, you went up worked with different Excel files also.

1:5:05

You did not create them.

1:5:07

Team gave you and they said, okay, guys, take this data set,

1:5:10

you're up to say column, rows, rows, bring, grouping caro, filter, you did that, right?

1:5:14

So same for us also.

1:5:15

We are not going to worry about creating those tables.

1:5:17

We'll make them table and then I will just ask you to,

1:5:18

and then I will just ask you to pitch, retrieve the records from there.

1:5:23

I'll tell you what data in table.

1:5:25

Okay?

1:5:26

And finally, obviously, DCL do not.

1:5:28

This is again, a typical database admin room.

1:5:31

So DCL, data control language,

1:5:33

we are talking about, you know, user access, who can access what,

1:5:37

which table can be accessible to home.

1:5:39

So this is again, completely not in the focus.

1:5:41

But just something you should know.

1:5:43

Is there are different types of languages we have?

1:5:45

And our focus is only on DQL.

1:5:47

Okay, everybody's fine.

1:5:49

So now we get into the, the course.

1:5:52

the core blueprint will be seeing that and this is the broad agenda of what we'll be covering

1:5:58

from here onwards.

1:5:59

Now we say, we're going to go to the demo in

1:6:01

until now everybody is okay.

1:6:03

So of course the context is clear, everybody.

1:6:05

You understand what is database, what is SQL, what is what?

1:6:08

The big picture idea is clear, everybody.

1:6:11

Okay?

1:6:12

Okay, so on all of you.

1:6:13

Anybody wants to ask me any general questions,

1:6:15

something from history, something from how life was back in 1980s and something of that sort.

1:6:21

You know, because I've worked across this whole stack, you know, so there's something you want to ask just of curiosity.

1:6:27

Nothing to do with the course.

1:6:27

And I always say that, see, see, learning is not just about a course.

1:6:31

I mean, it's not just how we are just learning a course for two hours and we are going, no.

1:6:34

I mean, you know, you should, you should be curious.

1:6:36

You should, you know, you feel free to ask general questions also.

1:6:41

Okay. So anything you would like to ask, let me pause for a minute before we start getting into these five four queries.

1:6:47

I told you, I promised you in the beginning, today's session is only these five queries.

1:6:51

these.

1:6:52

We'll select, from, we'll seeking, where, seeken, order by limit.

1:6:55

Plus, there's nothing.

1:6:56

This is 10 minute to 15 minutes topic.

1:6:59

That's it.

1:7:00

Nothing.

1:7:01

Very simple.

1:7:02

Believe me, it's very simple.

1:7:03

We will do more case studies on that, now.

1:7:05

Now, anything, anybody wants to ask me anything?

1:7:08

These are all shared with you, by the way, okay?

1:7:13

Everything is shared.

1:7:17

Before I start my sessions, I share everything with all of you.

1:7:19

all of you. So you can't, so that there is nothing pending because usually what happens is

1:7:23

this class is pending there's. I want to make sure I share everything before the class.

1:7:27

So this is your, ah, this one, 27th April, PDF, and these are some session notes and this is the

1:7:37

SQL script. So this we'll, we'll see. Okay. Okay. Okay. Okay. Let's, let's, uh, let's, uh, what

1:7:48

Yeah, uh, back in, what is that? Back in 1980s, did people record the records and registers or in PC.

1:7:55

Ah, no, no, PCs were there.

1:7:58

1980s, many organizations had already moved records onto computers and mainframe database systems.

1:8:03

That's time in mainframes.

1:8:03

Many frames are there.

1:8:05

Aby mainframes, eh, right? But plenty of operations still use paper registers.

1:8:09

Registers, registers take, ledgers, physical forms, especially smaller offices, where workflows were not fully digitized.

1:8:16

But, huh, computers were already quite.

1:8:18

established. If you're up Apple's history, Steve Jobs and all.

1:8:20

Macintosh came.

1:8:22

Yeah, see, Indian market is very different.

1:8:24

Indian market, you will look at stories of Infooses, Naran Murti.

1:8:28

When they founded Inforces, there are stories where he had to, you know, I think, he tells those

1:8:32

stories. I don't know how far is true. It's debatable. I don't want to talk more about it.

1:8:36

But he said that he waited outside an office. I don't know, like 24-hour wait here,

1:8:40

office-in-bara. That's a different thing. So getting computers in India was very difficult.

1:8:45

But, yeah, it was there. The computing revolution.

1:8:48

was already there. But still, it was very manual back at time.

1:8:52

Okay?

1:8:53

Okay. Okay. Any other questions?

1:8:58

Okay. So guys, going forward in the classes, all of you, some topics.

1:9:04

No problem, Arnica. We were just talking about some general theory.

1:9:07

We haven't really started the core of it. So I will just summarize at a very basic level.

1:9:13

All that you need to know, just so that you don't miss out anything. All that you need to know,

1:9:17

you're recording soon later. But all that you need to know is a database.

1:9:21

Database is a storehouse of data. It's in it. It's in the tables. And you will access

1:9:27

these tables using SQL. But it's just that you have for now. So you have something called

1:9:33

the database. And we will have many, many tables. Okay. And we will use something called

1:9:40

SQL. From SQL, we'll click, yeah tables to access. This is all that you need to know going forward.

1:9:47

And what we will discuss now is the syntax to write this SQL query.

1:9:51

This is what we will see.

1:9:55

So now everybody, as I said, please navigate over to your one compiler, this one. I will also do this side by side with you.

1:10:08

Is this, this is editable. That's my question. One second. If it is editable, then,

1:10:14

then just a seven.

1:10:17

I think, can you guys, can you guys take this? Can one of you take this? Just

1:10:24

want to check this out because I think I need a permission to. Can, can one of you update it?

1:10:30

Just wanted to check. Can one of you update? Just wanted to check if it's, if it's, if it's, if it's

1:10:34

updating real time. You're able to access this, right? This part.

1:10:42

Ah, so quite type caro. I'm just trying to check if it's, if it's happening real. I'm just trying to check

1:10:46

if it's, if it's happening real time. If it's not, then it's fine, but just wanted to check.

1:10:52

No, real time, I guess.

1:10:56

That's right. You can't, you can't, you can't, you, you just type something, could be. Just type,

1:11:01

start, start, dot, dot, dot. That's what I'm trying to check.

1:11:06

Ah, Pratap is also confirming, no, no, doesn't seem to. I think I need to, I need to, I need to, I think

1:11:10

I need to log in, I guess. Okay, no problem. Let's not, let's not, let's not complicate it. Let's not

1:11:15

complicated matters. You just go and, because I've already shared the script with you,

1:11:20

okay? I've already shared the complete script with you. Please keep that handy. Please keep the

1:11:26

complete script handy. Is it that complete script which I've shared with you?

1:11:45

Yeah.

1:12:03

Yeah. So all if you can, uh, please open up the script, just download it.

1:12:11

easy way to do it is, now you download it.

1:12:14

So just to understand what you can do.

1:12:16

You can just go and download the script.

1:12:18

And what I'll, so what you can do is just go and download the script.

1:12:22

Or this script download

1:12:23

and just go and open it up in notepad.

1:12:26

Now, now note pad, now open it.

1:12:28

This a dot sql file, okay? It's a simple dot sql file.

1:12:32

And just to understand the thing correctly, what you can do, just right click and open with

1:12:36

notepad. That's it. Just open with notepad.

1:12:38

That's it.

1:12:39

Now, you just go back in notepad.

1:12:40

And nothing does.

1:12:41

Just open in Notepad.

1:12:43

So you can't put a pooha dig jay.

1:12:44

What had done?

1:12:45

Okay?

1:12:46

Everybody's okay.

1:12:47

This is a simple thing.

1:12:48

So we'll see,

1:12:49

sart-sa-s-s-s-s-sa-s-s-s-s-s-s-sa-s-s-s-s-d-all-the-thing.

1:12:50

And then, we'll understand the code line-by-line, number one.

1:12:55

And number two, we'll go to the online compiler and we will do the demos.

1:12:59

We'll make it full-cheats, okay?

1:13:02

So everybody open up the demo.

1:13:05

In your systems, all of you.

1:13:09

Okay, all of you do this.

1:13:11

Open up the thing.

1:13:11

Okay? Okay.

1:13:19

Okay.

1:13:20

Starting, what are all these things?

1:13:21

These are basically called comments.

1:13:24

Now, you have Python in Python?

1:13:26

Hash is used for commenting in Python.

1:13:28

Python, VS code.

1:13:29

How do we do comments?

1:13:31

Everybody has seen commenting in Python.

1:13:33

We can do something called hash, right?

1:13:35

Commenting in Python.

1:13:36

Same way, you can also do commenting in MySQL in SQL in SQL using disking.

1:13:41

This is called comment.

1:13:43

So in the editor, this is completely ignored.

1:13:46

Here comments are.

1:13:47

Comments is done for documentation and readability.

1:13:49

That's it.

1:13:49

This is comments.

1:13:50

It's called Ignor.

1:13:50

Okay.

1:13:51

Now, the first, the main query I'm starting out is from here.

1:13:56

Because we're from sure.

1:13:57

Otherwise, I already have some stuff here.

1:13:59

So let's start from the beginning.

1:14:03

So let me go and start from here.

1:14:07

Everybody can see.

1:14:08

So I will go and

1:14:10

take this thing and I will create the table.

1:14:18

I will create the table.

1:14:19

Let me just open a editor once again.

1:14:26

Okay, I'll open a new one.

1:14:31

All of you just type this one.

1:14:34

So, now, I'll write it out.

1:14:36

Okay.

1:14:36

Please ignore the previous one.

1:14:38

Okay.

1:14:38

Sorry, please ignore the previous one.

1:14:39

I want you to start a new editor.

1:14:41

All of you please do that.

1:14:42

Please go to this link, everybody.

1:14:44

Start a new editor and please delete this part.

1:14:49

Okay.

1:14:51

Yes, all up my system.

1:14:52

Everybody go to this link and just delete the original query that was there.

1:14:57

So your screen should look like this.

1:14:59

Exactly how I'm showing.

1:15:00

So you can do this along with me.

1:15:03

Okay.

1:15:05

Simple, you have an empty, a clean canvas right now.

1:15:08

And here you can do the code.

1:15:09

So, you can create your tables, you can insert your rows, and you can also see the outputs.

1:15:15

That's up, you can actually do the whole thing.

1:15:18

Now, first thing that I will do is this.

1:15:23

Just copy this command first, everybody.

1:15:27

Let's do step by step.

1:15:29

I will explain to you.

1:15:31

I will explain to you in detail what this query is doing.

1:15:33

We will talk about that.

1:15:34

But first, a small hands on, everybody just take the first part of the code from.

1:15:39

here you can just copy this part and just paste it here all of you and after that what

1:15:45

you do very simple just click on run control enter is for running just click on run and what has

1:15:52

happened right now is that table actually got created so table got created now remember this is the

1:15:59

online environment this is not a proper database management system environment that we have seen

1:16:04

so that's why the interface is very basic you a coffee basic interfaces this pay

1:16:09

out of views and all that you will not be able to see.

1:16:11

If you have tables and all take need to, that is a, you know, a bit of a limited thing that you

1:16:18

have here.

1:16:18

So you cannot see all that.

1:16:20

But just enough for learning the concept, it is good enough.

1:16:23

Okay.

1:16:24

So everybody please run this first part of the query.

1:16:28

So this is for creating the table employees.

1:16:32

And this particular table will have a column called employee ID, name, department.

1:16:39

Salary, city, and joining year.

1:16:42

And you can see these are the data types of the column.

1:16:46

Like, Pandas in we have data types of the different variables, different columns.

1:16:52

Data frame in data type, right?

1:16:54

So same way, employee ID is int type.

1:16:57

Salary, inch type, integer type.

1:16:59

Like, Python inch type, this is inch type.

1:17:02

And similarly, like Python in string type is.

1:17:06

Or pandas in the object type is.

1:17:08

Python S.

1:17:09

and Pandas object.

1:17:10

Similarly, in SQL, we call it WarCare 50.

1:17:15

So Warcare is like a spring type data.

1:17:17

You can this go like this is like this is how to say.

1:17:20

So what is where care 50?

1:17:22

Weir care 50 basically means that you can store up to 50 characters.

1:17:28

Maximum 50 characters are store to, okay?

1:17:32

And if 50% or if 50% percent is,

1:17:35

imagine somebody's name, you're assigning maximum 50 characters.

1:17:39

for somebody's name.

1:17:40

You have a limit set.

1:17:41

If it, if it's name 50% or not going.

1:17:44

If it's 50% than you will, obviously, it will take lesser space.

1:17:48

It is variable character.

1:17:49

VARCARM is variable character.

1:17:50

So my SQL in where he's all data types.

1:17:52

So you don't have to get into that right now.

1:17:56

Just know that this is like a string data type.

1:17:58

We are trying to draw parallels.

1:18:00

Because the whole course will be in Python.

1:18:02

SQL is only two modules.

1:18:03

So we want to draw that connect with all the two.

1:18:05

That means, what you did in Python does, how does it connect to SQL?

1:18:08

So integer type here.

1:18:09

This your like similar to string type go.

1:18:12

Or similarly of other kinds of data types like date, time,

1:18:15

these other types we have.

1:18:16

So when you run this query, what happened?

1:18:20

It did not output anything because nothing got created.

1:18:23

Now.

1:18:24

And just remember, every time you write a SQL query, you always end with a semicolon.

1:18:30

You always are always semicolon.

1:18:32

So everybody has written the, done the query.

1:18:34

You are all seeing this output program did not output anything.

1:18:37

Everyone is in.

1:18:38

able to see that.

1:18:41

And now what I can do?

1:18:45

I will go and take the next line of the code and insert the values into the table.

1:18:53

And finally, I will select star from employees.

1:18:58

Just like you write a code in Python and say print of data frame.

1:19:02

This is exactly what I will do.

1:19:05

Okay, all of you can see.

1:19:06

Now it should be, it should be.

1:19:08

very clear what we are doing.

1:19:11

Let me just take the entire thing.

1:19:14

This upro to all the comments.

1:19:16

You can remove this part and see.

1:19:19

First, I create a table.

1:19:21

Next, I insert values into the table.

1:19:23

So create table, employee ID, name, department, salary, city joining here.

1:19:28

Insert values into the table.

1:19:30

Again, this syntax you please ignore.

1:19:31

Don't worry.

1:19:32

You don't know you.

1:19:33

Because I told you, create or insert up in practice,

1:19:36

not going.

1:19:37

Our focus is on select.

1:19:38

So create insert you will typically not do.

1:19:40

So this is just a demo thing that I've given you.

1:19:43

So after table made or table in the table in the values insert here.

1:19:46

For example, employee ID 101, name are up, department sales, salary 40,000,

1:19:52

city, Delhi, joining year, it's.

1:19:53

Okay, you've inserted.

1:19:56

10 rows.

1:19:58

Bonaer, insert you.

1:20:00

And finally, show me everything.

1:20:03

Just like Pandas in, how do you display?

1:20:06

Pandas in display how?

1:20:08

You all know, right, but how do I display?

1:20:11

Very simple.

1:20:13

What do you do?

1:20:13

You simply type demo, right?

1:20:15

Displayed go.

1:20:16

Same thing.

1:20:17

We are doing select star.

1:20:19

Just say you type the variable name and you display the data frame.

1:20:23

That's the thing we are being select star from employees.

1:20:27

Okay.

1:20:27

Everybody's with me.

1:20:28

Now, all you do is please, please select the whole thing.

1:20:35

Control A and run.

1:20:37

And you should be able to see this.

1:20:38

entire output. Please confirm to me if everybody is able to see the output.

1:20:43

Yeah, we're going to go. Different different queries, but output, we'll see what output are

1:20:46

looking. Please let me know. If this output is coming, you are all able to see

1:20:53

this employee table, name, ID, name, department, salary, city, joining here, and you are all

1:20:58

able to see the 10 rows that are inserted. Okay, I will pause for a minute. Allow all of you to

1:21:03

complete and take here. And if you're done, once you are able to see this result, please confirm

1:21:08

to me on chat.

1:21:16

I'm again repeating this is not a full pleasure DBSS.

1:21:18

I'm of course of the demo so that you get a real world feel that actually

1:21:22

how it's okay? Because everybody doesn't have it installed. So I don't want to

1:21:26

disconnect in the class. So I will, we're keeping it simple so that you are using an online

1:21:31

editor. But if you have a database there, so you're up to see that. And I'll show you that also how

1:21:36

it is done. That we'll be back in after.

1:21:40

Okay, everybody please confirm to me. If you're all done.

1:21:46

You're all able to see the table. Let me.

1:22:06

others all of you are okay let me know guys everybody everybody if somebody is struggling any

1:22:27

questions please don't hesitate to ask okay everybody should be able to do it I've got

1:22:34

Only four responses so far. Others are all able to seek the table. Let me know.

1:23:04

And it's important, everybody does the setup.

1:23:06

If we, if we're going to some class exercises, we'll do, 10, 50-bilt exercises we'll do.

1:23:12

So all of you, please ensure that you're able to see the outputs.

1:23:20

Okay, great, great.

1:23:23

Thank you. Thank you. Thank you, guys.

1:23:29

Okay, seven responses. Others.

1:23:32

Hello, guys.

1:23:34

Everyone should be attentive. Let me know.

1:23:37

Yes, e-se type to type. And just set your chat settings to everyone.

1:23:41

I told you, like, go to your Zoom chat.

1:23:43

Set it to everyone, right?

1:23:44

So, see, I can see your responses, but like there are so many participants.

1:23:48

So each person can see everybody's answers, right?

1:23:51

So if you're asking a question also, just type to everyone.

1:23:54

So that everybody feels engaged in the class.

1:23:57

So if any, if somebody will know, everybody will know who asks that question?

1:24:02

Because you have two settings.

1:24:03

a post-panelist so if you're just just try to set to everyone okay okay okay

1:24:09

great um next and if you're still facing any doubt please let me know okay so i'm here

1:24:16

ratha is here we can guide you okay if you're facing small issues basic issues let us know okay

1:24:21

we'll guide you okay let's move on so uh next we will see we will go and do this so i have actually done

1:24:31

uh this thing right you can see

1:24:33

demo number two. So demo number one, we've seen, so we

1:24:37

we, so we, so that you get a real world feel of everything.

1:24:42

So demo number two, we are doing this.

1:24:45

Select specific columns from a data frame.

1:24:48

Pandas in how do we do it.

1:24:50

That is how we do in Pandas, right?

1:24:53

SQL in how do we do.

1:24:55

Select name, department, city, from employees.

1:24:59

Now, this is something to have,

1:25:00

something to have, simple.

1:25:01

I think you are realizing.

1:25:02

How you are realizing how?

1:25:03

easy this is.

1:25:04

You know?

1:25:05

Nothing.

1:25:06

Simple, right?

1:25:07

All easy.

1:25:08

Okay?

1:25:09

We are able to see name department city from employees.

1:25:13

So we have named department city from employees.

1:25:16

So that is what we have right now.

1:25:19

So we can do control enter.

1:25:21

We can again run the code.

1:25:24

And as you, as you're going to run

1:25:26

you, your output is like.

1:25:28

The first one is, it will,

1:25:29

and this one out of the output will.

1:25:31

So, okay, let it be.

1:25:32

guys, make sure, so you just, you just, just hit run, okay?

1:25:37

You come here and just hit run,

1:25:39

you just hit run, and you will see this kind of an output.

1:25:43

So here, first output was, see, this is going to give you all the outputs.

1:25:46

So whenever you say select star from,

1:25:48

you are trying to output something.

1:25:51

So first output is this.

1:25:53

Star, you're selecting everything, you're selecting all the columns.

1:25:56

Star means you're selecting all the columns in the table,

1:25:59

okay?

1:26:00

And if you only want to select specific columns in the table,

1:26:02

you will say select name, department, city, from employees.

1:26:05

That's it. This is your second output we are getting.

1:26:08

So all the rows are coming. Remember, we are not doing any row selection.

1:26:13

We are only doing column selection.

1:26:15

And what is the issue you're facing? Can you tell me?

1:26:20

I think you don't have panelist access.

1:26:22

So if you can describe the issue a little, it will help.

1:26:25

So can you, or if you can post a screenshot either way,

1:26:28

can you try to describe the issue a little bit?

1:26:32

Yeah, it is more easy, exactly, exactly.

1:26:37

And there are a lot of tools out there.

1:26:40

And you know the best part is you can also write SQL within Pandas.

1:26:44

I will show you that at the end.

1:26:47

I will show you that at the end, how you can write SQL within Pandas.

1:26:50

You can't do Pandas in Pandas' end.

1:26:53

There is a package in Python called Pandas SQL.

1:26:55

That we'll last make it.

1:26:57

So if you find this syntax easy, you can actually write SQL code right using

1:27:02

ah, Pratap, I think you can help Parnika once.

1:27:05

So, yeah, so you can look.

1:27:07

Okay, I'll show that at the end, okay?

1:27:11

Let's move on, guys.

1:27:13

So this is how we can select three columns from our table.

1:27:17

Now, moving on, this is basically how we write our very first wear clause.

1:27:25

Demo number three, I'm clearly segregated here in terms of demos.

1:27:31

So this is the code.

1:27:32

how we are able to select star from employees where department equal to IT.

1:27:37

I'm not run, but I think the answer is obvious.

1:27:41

This is what is like a filter in Pandas.

1:27:44

That means you're selecting all the columns.

1:27:48

Select star means you're selecting all the columns from the employee table

1:27:52

where you are selecting all the columns

1:27:56

where this is equal to IT.

1:28:00

And if you scroll down,

1:28:01

And if you scroll down, this is the final result in table you're getting.

1:28:07

This is the final resultant table you're getting IT, IT, IT.

1:28:10

Now, look, the original table you're fetching all of this from the original employee table.

1:28:14

This is your original employees table, right?

1:28:17

So you are selecting all the columns from this table where department equal to IT.

1:28:22

This is your filter.

1:28:25

All of you can relate to it.

1:28:28

Its equivalent Python code, what will?

1:28:31

it's a general question what is the equivalent Python code of this?

1:28:35

Imagine your employees are the data frame and somebody type what is the Python code for it?

1:28:40

Imagine employees the data frame.

1:28:42

What is the corresponding Python code for it?

1:28:44

What is the Python?

1:28:46

How do we?

1:28:49

How do it?

1:28:50

This is the way how we'll do it?

1:28:53

Let me, let me ping this to all of you.

1:28:55

Okay?

1:28:56

So this is the way how we'll do it, right?

1:28:59

All of you recall?

1:29:01

Boolean indexing, right?

1:29:03

But see how simple it is in SQL.

1:29:05

SQL is almost like English.

1:29:07

Almost like English.

1:29:09

Structured query language.

1:29:10

The equivalent thing in Python is like this.

1:29:13

You've already seen this, how to do it.

1:29:15

So, we try to filter the rows.

1:29:18

And the same way, we can filter the rows here.

1:29:21

Okay?

1:29:23

Okay.

1:29:24

Moving on.

1:29:26

So this is called a wear clause.

1:29:28

So until now we have learned three things.

1:29:30

Three things.

1:29:31

Select from where.

1:29:33

Going back to our slide, select, what data do you want?

1:29:37

Specific columns?

1:29:38

Selects are we are able to select key, what are the columns we want?

1:29:44

Select start or select some column names.

1:29:47

That is where we specify the specific columns.

1:29:49

What are the columns we want?

1:29:52

Next we studied from.

1:29:54

From.

1:29:55

From, what type?

1:29:57

Next we are looking at from.

1:29:59

And finally, we are looking at from.

1:30:00

looking at where? What is the condition?

1:30:02

Filter here?

1:30:03

These things we have now.

1:30:04

Select, what you want to retrieve?

1:30:06

What columns you want to retrieve?

1:30:08

From, where you want to retrieve?

1:30:10

Which table?

1:30:11

Or where?

1:30:12

what filter? Which rows you want to retrieve?

1:30:14

Select is column or where is rows?

1:30:16

row filter.

1:30:18

Okay?

1:30:19

The other two things are.

1:30:20

Order by limit.

1:30:21

That there is not.

1:30:22

You are looking.

1:30:23

Order by is used for sorting.

1:30:24

And limit is basically used for head.

1:30:25

Top and rows.

1:30:26

We will see that at the end.

1:30:28

Okay.

1:30:29

So now we look at some more clauses.

1:30:30

We'll look at some more demos of select and from and where.

1:30:33

Let's see that.

1:30:34

Next one.

1:30:36

Okay.

1:30:37

So let me take all of this together.

1:30:39

Okay?

1:30:40

Then, then class exercises.

1:30:41

So demo four, five, six, seven, eight.

1:30:45

We'll load together.

1:30:46

Okay?

1:30:47

So, let us speed up a little bit.

1:30:52

We have done until three.

1:30:54

Now I will load all the four to eight

1:30:57

we load all the four to eight.

1:30:58

And we'll load together.

1:30:59

Let us do. Let us do this. So demo four, what are we doing? It's a maths comparison.

1:31:07

I don't think I need to explain this. This is simple again. Select what are the columns you are selecting?

1:31:15

From where you're selecting and what is the filter condition you're using?

1:31:20

Yeah, your salary greater than equal to 70,000.

1:31:25

Okay, salary greater than equal to 70,000.

1:31:28

70,000. So we've all done

1:31:30

everything.

1:31:31

So you can see this is the output of the demo number four.

1:31:35

So I have got the name, salary and city from the employee table

1:31:43

where salary greater than equal to 70,000.

1:31:46

So these records in salary 70,000 is more.

1:31:50

And again, this is the same thing you can do in Pandas data frame also.

1:31:54

The same way that you do a filter in a Pandas data frame.

1:31:57

data frame, we are selecting a certain number of columns and we are also applying a filter

1:32:04

on the rows.

1:32:07

That's how we are doing this.

1:32:10

Demo number 5 is a and or logic.

1:32:16

You have panda's data frame and or

1:32:19

key when multiple conditions have to be satisfied.

1:32:22

That's salary 70,000 is more and city banglough would.

1:32:25

You have done that, right?

1:32:26

Same concept.

1:32:27

Nothing.

1:32:28

But Pandas, you have to write some more syntax.

1:32:31

You have to use those logical operators and operator or operator use.

1:32:36

Everybody has seen that in Pandas, right?

1:32:38

Similarly, SQL in little easy.

1:32:40

Because it's almost like English.

1:32:43

You are just using and and and or all.

1:32:45

Straight forward.

1:32:46

So select start from employees where department equal to IT and CT equal to Bangalore.

1:32:52

Do I have to explain this, guys?

1:32:55

Straight forward.

1:32:56

this is the answer to the query.

1:32:59

So you want to get all the columns from the employee table where department will be IT and city

1:33:07

is Bangalore.

1:33:08

You can see this is selected.

1:33:10

And all this is happening on the main table.

1:33:12

For the sub which main table case are already.

1:33:14

Now the output is shown together.

1:33:17

So that's why if you look at the main table, from the entire main table, which are those rows

1:33:23

where department is equal to IT and city is Bangalore.

1:33:26

this one Rowe will be.

1:33:28

So, Meera and Roshan are.

1:33:30

Both IT and Bangalore's there.

1:33:32

No other thing is matching.

1:33:34

You're here here here, it is in Delhi and it.

1:33:36

And they're Bangalore and they can sales.

1:33:38

So which are the cases where IT and Bangalore are

1:33:40

only for these two people.

1:33:42

And that is exactly what I'm getting in the output.

1:33:44

Meera or Rohan.

1:33:46

Simple.

1:33:48

Next query is just using an or clause.

1:33:50

Same way.

1:33:51

Just like we have discussed operators in data frames,

1:33:53

same way we can use this or clause.

1:33:55

HR.

1:33:56

Yeah, finance.

1:33:57

Get me all the records by department,

1:33:59

either HR or finance.

1:34:00

I want to see all my HR and finance people.

1:34:03

Simple.

1:34:04

Okay.

1:34:05

Next, we are looking at something called the in-close.

1:34:09

In-close is a cleaner alternative to multiple or conditions.

1:34:15

So, what happens is select start from employees' web city in Delhi or Mumbai.

1:34:21

You can see if you want to write this query in a different way.

1:34:26

Let me share with you.

1:34:27

You can say select star from employees where city is equal to city is equal to Delhi.

1:34:37

Right?

1:34:39

Or intelligent say you can actually as you type the query, your help will be.

1:34:44

You type the query, you have the help coming up.

1:34:47

Or city equal to Mumbai.

1:34:50

You can apply.

1:34:51

And you always end with a semicolon.

1:34:53

Please remember.

1:34:54

This is the same answer you will get.

1:34:55

answer you will get. Now you will ask me to, sir, why we have to do it this way?

1:35:01

Why learn something you fall in? Because the query looks a lot cleaner. I think you agree with me.

1:35:08

The query in this case looks a lot, you know, looks a lot cleaner.

1:35:14

So the query here looks a lot cleaner. You are able to see.

1:35:20

Basically. So in is a simple way to do it. Now here it looks a lot cleaner.

1:35:24

Now, here it looks very easy, right? What if there are 10 cities?

1:35:28

What if you have? What's that?

1:35:33

What if there are 10 cities?

1:35:35

Delhi, Mumbai, Calcutta, Bangalore, and Hyderabad, can you imagine how big the city this will be?

1:35:40

So then what you're going to?

1:35:41

It's a city equal to Bangalore or city equal to Hyderabad or city equal to...

1:35:45

So it's redundant, now, barbara city like to.

1:35:47

I know, so it's pointless.

1:35:48

So this is the simpler way to do it.

1:35:50

So in is an alternative.

1:35:52

So get me all the rows of those.

1:35:54

on employee where city, you're either Delhi or

1:35:56

or Mumbai is.

1:35:57

City, both of one of the

1:35:59

and that's your answer will.

1:36:00

Now, look.

1:36:01

I'm getting all the columns from my employee table

1:36:04

where city either Delhi or Bombay is.

1:36:07

Straight forward.

1:36:09

Okay, guys.

1:36:11

Next, we are learning the between plus.

1:36:15

Between plus, select name,

1:36:19

joining year from employees,

1:36:21

where joining year is between 2018 and 2020.

1:36:23

2018 and 2021.

1:36:25

So this is the between clause in SQL.

1:36:28

So we are able to see the between clause in SQL.

1:36:29

So we are able to see the between clause in SQL.

1:36:32

Unfortunately, Python in between

1:36:34

nothing.

1:36:35

So Python in you have directly written.

1:36:37

So this will be a slightly more difficult code in Python, Pandas.

1:36:40

So that's an exercise is.

1:36:42

Pandas in how is it?

1:36:44

So, yeah.

1:36:45

But in SQL, you have a between class.

1:36:47

You have a simple between clause that you can use to,

1:36:50

you can use to write it.

1:36:52

You don't have to use to and condition.

1:36:53

So select the name and joining year from the employees table where joining year is between 2018 and 2021.

1:37:02

Okay, so this is one way to do it.

1:37:04

Its equivalent is what is.

1:37:06

If you're asking me, sir,

1:37:07

this is how can we can write it?

1:37:10

You can this way to do it.

1:37:12

Between is a simpler way to do it.

1:37:14

But if you don't want to write it this way,

1:37:16

no way.

1:37:17

You can say greater than 18 and joining year.

1:37:23

less than 2021.

1:37:25

Okay, so that's the way how you can write the equivalent SQL query.

1:37:29

You can say greater than less than.

1:37:31

Between.

1:37:32

It's in between.

1:37:33

Actually, it's like inclusive.

1:37:34

Actually, it's like inclusive.

1:37:36

To be more specific, it's inclusive.

1:37:38

It's greater than equal to, and it is less than equal to.

1:37:41

This is the way to, this is the equivalent way to write the query.

1:37:43

So these are all, so there are two shortcuts we learned today.

1:37:47

One, we've in the shortcut learned.

1:37:49

So in Delhi comma Mumbai,

1:37:51

either Delhi or Mumbai.

1:37:53

This is the shortcut.

1:37:56

Shortcut to multiple ors.

1:37:58

Similarly, if your between,

1:38:00

this is our between,

1:38:02

but you can this can do it as if you can

1:38:03

if your between then

1:38:05

greater than equal to 18 and less than equal to 22.

1:38:08

Both are in this in between.

1:38:10

So this is the way how you write that way.

1:38:13

Hope everybody is clear.

1:38:16

Okay.

1:38:18

And finally, the last demo.

1:38:20

demo we will see and after this we'll do some exercises.

1:38:23

So here we are using all the things.

1:38:26

I'm select use correct.

1:38:28

From use correct.

1:38:29

I'm order by using.

1:38:30

We're limit using.

1:38:31

We're not using because we have seen a lot of wear conditions.

1:38:34

So order by is used for sorting the data.

1:38:38

And limit is used for limiting the data to the top three records.

1:38:44

That is what limit is used for.

1:38:47

Okay?

1:38:48

So code, look back from.

1:38:49

Select the name, department, and salary from the employee table.

1:38:53

So from the main employee table,

1:38:55

Joha ha ha ha, my course.

1:38:56

Please, I'm sorry, I think the screen is not shared.

1:38:58

Sorry.

1:38:59

So from the main employee table, I hope all of you follow this part, okay?

1:39:03

This is the between part that I explained, okay?

1:39:05

This is the equivalent query.

1:39:07

Let we ping that on chat for all of you, okay?

1:39:09

So the part that I discussed just a while back.

1:39:11

So this is it an equivalent query for between that I discussed a while back, okay?

1:39:16

All if you can see, you can see, you can either use between

1:39:19

or you can use greater than equal to and less than equal to.

1:39:23

Now, both use can.

1:39:25

And this is your order by a limit.

1:39:29

The last of the basic conceptual things that we have today.

1:39:32

So order by is used for sorting the data.

1:39:35

So sorting, so you know,

1:39:37

you know, the same way you can go and do sorting in SQL also.

1:39:41

It is a table at the end of the day.

1:39:43

You can go and do this kind of a sorting here.

1:39:47

Effectively.

1:39:48

effectively.

1:39:49

So, it's quite simple.

1:39:50

Pandas in you have to sort values.

1:39:52

You might have used it, right?

1:39:53

It's a bit more difficult.

1:39:54

But in SQL is so simple.

1:39:56

So select name, department, salary from the main table,

1:40:00

from the employees table.

1:40:02

Order by salary DESC, this means you're sorting in descending order.

1:40:07

And limit, comma, 3.

1:40:10

So you are sorting all the salaries in descending order.

1:40:13

You have a table.

1:40:15

So topmost salary, 90,000.

1:40:17

top most salary is 95,000.

1:40:19

So, first, it will gore-go.

1:40:21

Then we have 90,000, then we have 85,000.

1:40:24

Where the data sought will.

1:40:26

And limit it to 3, that is only get into the top 3.

1:40:30

Its equivalent in Pandas may what will.

1:40:33

Sort values, descending and head of 3.

1:40:35

Head 3 means you are retrieving the top 3 rows.

1:40:38

So that's the way how you do it in funders.

1:40:41

So this is the same to same story that we are looking at.

1:40:43

Just that SQL is a lot simpler.

1:40:45

What is the final end result we are getting, guys?

1:40:46

result we are getting guys the end result that we are getting is this you have this

1:40:52

this record okay you want to see the equivalent pundas you

1:41:00

you can't these pundas in you can't do you

1:41:04

I'm sure you you know right you have a pandas me over sword values by equal to

1:41:10

salady ascending falls head three but it's it's syntax Python

1:41:16

So, here, it's plain English.

1:41:19

It's a lot easier to understand.

1:41:20

Because if you look at the evolution of SQL, SQL,

1:41:23

the time in the SQL is not meant for developers.

1:41:27

SQL is not meant for programmers.

1:41:29

SQL was invented to be an English-like language.

1:41:33

The origins of SQL, if you go back to the,

1:41:36

you know, back to when SQL was invented,

1:41:38

it was designed to be declarative.

1:41:40

It was designed to be close to English.

1:41:42

Unlike programming languages like Python, Java, C, C++,

1:41:45

which are more.

1:41:46

technical. SQL was not meant for that purpose.

1:41:49

SQL was more meant for business users, people who can just write simple queries.

1:41:53

It was, that's how it initially came about, right?

1:41:57

So it was meant for analysts, not just to ramage.

1:42:01

That's the important term.

1:42:02

Okay, that's why the syntax and the language is very English.

1:42:05

Like, okay, hey, select this, from this, order by this, wear this, limit this.

1:42:10

That's it.

1:42:11

With my head, okay?

1:42:15

What I will quickly do.

1:42:16

so that you get a very nice flavor of the whole thing.

1:42:19

Okay, so, so we'll do three class exercises,

1:42:25

and after that I have some real world case studies, okay?

1:42:28

So class exercises, this is here.

1:42:30

Ah, okay, here we have, oh, oh my God, I thought,

1:42:36

I planned this as an exercise, but we can,

1:42:38

we have a solution there.

1:42:40

Okay, I'll try to curate some exercises for you.

1:42:43

Okay, anyways,

1:42:46

Here, there's solution here I actually thought,

1:42:51

here we made a solution brought here.

1:42:53

Sorry, sorry, so exercise not be able to.

1:42:56

Okay, no problem.

1:42:57

I'll try to curate some exercises for you.

1:42:58

So I'll try to think of some exercises.

1:43:00

Before we, we'll take a short break in the moment.

1:43:02

But before that, I wanted to show you one last thing, okay?

1:43:05

One last thing I'll quickly show you.

1:43:07

I will open up my SQL workbench for you.

1:43:11

This is my SQL workbench.

1:43:14

This is a proper database management.

1:43:15

This is a proper database management.

1:43:16

management system.

1:43:17

So, the thing we're on online

1:43:19

All this while, just for you to understand the,

1:43:21

what is happening and all that,

1:43:23

that's the, I will run and execute the same thing

1:43:27

inside my SQL workbench for you.

1:43:30

Okay, so let us see how the same thing is working

1:43:32

inside SQL my world bench.

1:43:35

This is how a typical database management system looks like.

1:43:39

Okay?

1:43:40

So this is what it is.

1:43:41

This is our interface and

1:43:43

through, we can interact with.

1:43:45

So what is.

1:43:46

Whenever I was demoing all this file, I wanted to just show you.

1:43:49

You don't want to show you.

1:43:50

You want to show you what it is.

1:43:52

So I will connect to my database.

1:43:54

I told you our database is like a very secure vault.

1:43:57

That database in there are many tables.

1:44:00

So I can't read those tables as it is.

1:44:03

We have to log in,

1:44:04

password then that's the real world.

1:44:06

So I have to log into my database.

1:44:08

I have to give a password.

1:44:10

Now, this is our database.

1:44:12

You have to password enter.

1:44:13

Without a password you can't enter into a DB.

1:44:15

enter into a DB.

1:44:16

I have to connect to my server, where there's database there.

1:44:20

And this is how I get to see how my database interface looks like.

1:44:25

This is our database interface interface.

1:44:28

Okay.

1:44:29

So what I will do, let me,

1:44:34

so what I will do right now, just give me one second.

1:44:38

Let me table here.

1:44:40

Don't worry, this go ignore.

1:44:42

Okay.

1:44:43

So this our data data.

1:44:44

This is our database.

1:44:45

There are many databases.

1:44:46

We have already.

1:44:47

Remember, this is the database management system.

1:44:50

So in this database management system, I've got many databases.

1:44:53

New Schema, Sakila, Sayan, whatever.

1:44:56

Ignore these.

1:44:57

What we are concerned with today, today we are concerned with this, you know, a specific DB.

1:45:07

And I will create a table in that particular DB.

1:45:12

Okay, so we, we make that, here.

1:45:15

And we, same to same, whatever I did, we'll here here table, okay?

1:45:20

So some part of the code, you can ignore it.

1:45:23

I will go and use Massa Analytics.

1:45:29

This is our database.

1:45:31

And we'll suppose, we'll, okay?

1:45:34

Now, all that you need to worry about right now is,

1:45:36

you have here, left-hand side, this is our database.

1:45:39

There are many of the databases.

1:45:41

There are many databases.

1:45:42

There are there.

1:45:43

There are many tables.

1:45:44

These are there are many tables.

1:45:45

These are all our made.

1:45:47

Whatever.

1:45:48

ignore that.

1:45:49

This is just exactly what I can show you.

1:45:51

So this is exactly what I can show you.

1:45:53

So this is the more beautiful interface.

1:45:55

You can see a whole lot going on here.

1:45:57

So this is the code I will write now.

1:45:59

Create table employee and insert into.

1:46:01

This is the proper database management system environment you are seeing.

1:46:06

Okay?

1:46:07

Just wanted to show you.

1:46:09

So this is run.

1:46:10

Let me execute that.

1:46:12

As you run, you, you'll see,

1:46:13

you're left in the table.

1:46:15

Okay?

1:46:16

Execute it.

1:46:18

Table, then,

1:46:19

okay, it's hide the panels.

1:46:21

And you'll refresh it,

1:46:23

it's a more visual interface.

1:46:24

And it is a more visual interface.

1:46:26

You'll see what the table

1:46:28

here,

1:46:29

you can click, you,

1:46:31

you have the table structure,

1:46:32

the name, department, salary, city,

1:46:34

joining here.

1:46:35

And if you want to quickly

1:46:36

visualize your table, you can see the top thousand rows.

1:46:39

You can see the top thousand rows.

1:46:40

you can easily an interface better better.

1:46:42

So just for learning right now,

1:46:44

because it's set-up of our people have

1:46:45

not required also.

1:46:47

Just for two SQL classes,

1:46:48

you need,

1:46:49

but just to let you know that it's

1:46:51

ultimately we have select queries

1:46:53

make me.

1:46:54

But what's the select,

1:46:55

where you,

1:46:56

the concept is more important,

1:46:58

the environment is not.

1:46:59

Just wanted to show this to you.

1:47:00

This is how the environment looks like.

1:47:02

So whatever queries we were doing,

1:47:03

we are going,

1:47:04

go to this last one query

1:47:05

Okay,

1:47:06

now,

1:47:07

now,

1:47:08

we're the last one query

1:47:09

we're the demo number eight,

1:47:09

here you have your lesson here

1:47:10

here, okay,

1:47:11

RIA, Rohan, Eishan,

1:47:12

okay?

1:47:13

So same thing will come,

1:47:14

same to same thing will come.

1:47:16

So, I will go and run this query.

1:47:19

If I go and run this query,

1:47:21

now, see, same to same answer.

1:47:22

Answer, there's no difference

1:47:23

no.

1:47:24

Ria, Proshan, Eishan,

1:47:25

three columns and tree board,

1:47:27

same to same.

1:47:29

I hope the idea is clear,

1:47:30

that is what it is.

1:47:32

Now,

1:47:34

real world databases are extremely complex.

1:47:38

Here.

1:47:39

I'm trying to show you a simple table,

1:47:42

a table

1:47:43

a table

1:47:44

on it.

1:47:45

But it's not

1:47:46

in real world

1:47:47

you will not have one table.

1:47:49

Real world, you will have hundreds of tables.

1:47:51

And I wanted to show you

1:47:53

for a minute

1:47:55

how a real world system looks like.

1:47:58

A small example,

1:47:59

because we have loaded that thing.

1:48:01

A small example of how a complex real world schema,

1:48:05

schema,

1:48:06

a structure of a database,

1:48:07

where you have a

1:48:08

Kahi several tables

1:48:09

15, 20 tables, how it is,

1:48:11

how it looks like in practice.

1:48:13

Take this example.

1:48:15

So, we have a

1:48:19

circular database.

1:48:20

We have this made

1:48:21

and you can't see how

1:48:23

there are there.

1:48:24

Actor, address, category,

1:48:26

there's information,

1:48:27

address information,

1:48:29

category information, city information,

1:48:31

all this we have right now.

1:48:33

This is a small deal.

1:48:35

It's a simple example DB I'm showing you.

1:48:37

In reality, it is much more complex.

1:48:39

And just to give you a very nice visual feel,

1:48:43

whatever I've been discussing all this while,

1:48:46

I will do something very interesting.

1:48:47

You have to demo not required, okay?

1:48:50

I just wanted to show you.

1:48:51

So I just wanted to show this to you,

1:48:53

okay, reverse engineer,

1:48:54

visually I wanted to show you how it looks like.

1:48:59

So you can see,

1:49:02

I wanted to show you the schema,

1:49:05

what the schema,

1:49:06

schema,

1:49:07

and more specifically, if you're asking me for a more specific name,

1:49:12

we have a particular name we call it an ER diagram.

1:49:16

We call it an entity relationship diagram.

1:49:18

We call it an entity relationship diagram.

1:49:21

So I've got total 16 tables right now.

1:49:24

And we have this go a graphical intercourse

1:49:26

how are a real database are reasonably complex.

1:49:29

It's not a very complex, one is a reasonably complex database,

1:49:32

at least better than what we are doing, right?

1:49:34

We are only, our agenda today is only one table.

1:49:36

Because we're just learning as well.

1:49:37

at a basic level.

1:49:38

But this is how a real world schema will look like.

1:49:41

Now look at this.

1:49:43

This is,

1:49:44

you know,

1:49:45

it's going to one, one-dhurted,

1:49:46

what tables,

1:49:47

it's in there, columns,

1:49:48

what connection is.

1:49:50

This is called an entity relationship diagram.

1:49:53

Inside my SQL,

1:49:55

what is it called?

1:49:57

Let me type the name for you.

1:49:59

This is called an enhanced entity

1:50:02

relationship diagram.

1:50:05

Relationship,

1:50:06

relationship.

1:50:07

relationship diagram.

1:50:09

This is called an enhanced entity relationship diagram.

1:50:12

You are you, it's all tables, there are address, staff,

1:50:16

there, category, and you can also see how the tables are related.

1:50:20

One table, two tables are related.

1:50:22

You have some of PANDAs in a joint.

1:50:24

I'm not sure, maybe you might have, okay?

1:50:27

So, so we'll see that later.

1:50:30

So joins are important, how the data frames are related.

1:50:33

You have data frame A, data frame B.

1:50:35

You have table A, table B.

1:50:36

You have table B.

1:50:37

What relationship?

1:50:38

And you're looking, how complex it.

1:50:40

You know, in reality, you imagine a banking setup.

1:50:43

We have a customer's table,

1:50:45

where there's a customer ID information,

1:50:48

how not, how account balance,

1:50:49

how debit,

1:50:50

or a transaction table,

1:50:51

where debit credit is.

1:50:53

It is very important to link the two.

1:50:55

Customer ID in only customer details

1:50:57

that you provide,

1:50:58

that is your customer table.

1:51:01

You will have your customer ID, name, address,

1:51:03

phone number,

1:51:04

all details are there.

1:51:06

Transaction table in there.

1:51:07

You have only transaction details.

1:51:09

He, he know where from,

1:51:10

transaction,

1:51:11

how did the GPS,

1:51:13

all those things are cracked.

1:51:15

Relationship is very important.

1:51:17

They are not two independent tables.

1:51:20

Like you here here here,

1:51:22

the store is your store table.

1:51:25

The store table is very clearly linked to the address table

1:51:29

using something called CTID.

1:51:32

Here, this diagram is very big

1:51:34

so you can actually see.

1:51:36

I want to show you just one small example.

1:51:38

Now look here.

1:51:39

If you want to look at the link,

1:51:41

we're just two tables are you,

1:51:43

store table, address table,

1:51:45

you are able to see in the table.

1:51:47

But it's so simple, you know,

1:51:49

it's so simple.

1:51:50

And if you hover over this

1:51:53

relationship,

1:51:55

you are able to see which two columns are related.

1:51:59

store table in store detail.

1:52:01

store detail,

1:52:02

what is store detail?

1:52:03

What is store detail?

1:52:04

What is the name?

1:52:05

Registry registration?

1:52:06

and where are located and here

1:52:10

and here address details

1:52:12

address, the city, country,

1:52:14

so they are related with respect to the address ID.

1:52:17

So this is how, you know, real world data is organized.

1:52:21

Just wanted to share this with all of you in practice.

1:52:25

Okay?

1:52:26

All of you are able to get it.

1:52:27

Okay, this is not.

1:52:29

The complexity is incredible.

1:52:31

See, there's so many relationships actually.

1:52:33

This is a, this is actually a default database.

1:52:35

if you have worked on it or if you have seen it,

1:52:38

this is actually a default database.

1:52:40

Like, so many databases can actually work on.

1:52:43

But it's not required for now.

1:52:45

Let's move on.

1:52:47

Let's come back to our topics right now.

1:52:50

This was meant as a class exercise.

1:52:53

So there, no, we can go over it.

1:52:55

And you want to take a short break.

1:52:56

I know it's almost 9.45, but we have still some time to go.

1:52:59

I have some real world case studies I want to do.

1:53:01

Just to give you a flavor of some more examples shortly.

1:53:04

shortly. We can take a five minutes break.

1:53:07

Guys? Yeah.

1:53:08

Okay.

1:53:09

Small water break we can take.

1:53:10

Take a break.

1:53:12

And we'll see some more examples.

1:53:13

Mostly case studies and examples we'll be doing going forward.

1:53:16

Okay. Yeah.

1:53:34

Thank you.

1:54:04

Thank you.

1:54:34

Thank you.

1:55:04

Thank you.

1:55:34

Thank you

1:56:04

Thank you

1:56:34

Thank you

1:57:04

Thank you

1:57:34

Thank you

1:58:04

Thank you

1:58:34

Thank you

1:59:04

Thank you

1:59:34

Thank

1:59:36

So

1:59:38

Okay, so we'll come back, we'll continue on.

2:0:05

and i will continue on with the rest of the demos okay so we have talked about the

2:0:16

until demo number eight and let us see these some of these small exercises here

2:0:26

you can all do this along with me so what i will do is since i already loaded this in my

2:0:29

workbench i will i will continue doing my exercises here okay so don't worry you can go back and do it in the

2:0:35

compiler the same way i showed you okay just that this will be easy for you to see so it's it will

2:0:41

be easy for you to see hence i will run my demos here you can continue doing the demos in your

2:0:45

environment okay so now you know the flow how the flow will happen right so let me go and

2:0:54

take this entire code here

2:1:05

we are seeing is find all the employees in sales who earn more than 45 000 so how we are doing this

2:1:13

so first from the employee table remember the employee table let me show the employee table to all of you

2:1:18

that's my employee table right so in my employee table find all the employees in sales that means

2:1:24

i have to filter by sales and salary has to be more than 45 000 and what you want to show

2:1:30

you want to show their name salary and city find all the employees right that means you want to file

2:1:35

all the employee related information if you see that's how you're result to do so it's only

2:1:41

kabeer who is from uh sales and who's salary is this actually you can also say select start

2:1:47

of select start of select start so starts you of course a push but you can start is

2:1:51

so select kabar's whatever comes that is a selection for the columns

2:1:55

up the xakia it is uh kabeabit kabe is from sales and kabe's salary is also 45 000

2:2:02

there's no other person who is from sales and whose salary is 45 000

2:2:05

more than 45 problem so that is what we are able to see next find all employees

2:2:12

who do not live in deli and sought them alphabetically by name so we have the main employee table

2:2:20

so here we have to say get me all the columns from employee where city is not in delhi

2:2:26

and order by name a c is order me so first get me the information from employee

2:2:32

filter based on all those people who are not from deli and then order by name ascending order

2:2:39

that's the way how this information will look like see your information over so order by is nothing

2:2:44

but the sorting that we are doing so we are sorting by the name college okay your question number

2:2:49

two ho go and the third one very similar is find the two most recently hired employees

2:2:55

of the problem statement we'll say in reality so real world in um as a problem statement

2:3:00

end angle find the two most recently hired employee i have this to solve

2:3:05

solve how to solve most recently hired that means you will have to sort by joining year

2:3:12

find out who are the people in the company who uh who joined last so sort order by

2:3:23

joining year

2:3:25

let's descending may sort and limit to let me show the top two so here

2:3:30

so you here to be select start can't you don't have to only select those columns so select

2:3:34

select start and you can see this is the answer you will get so these are the two last employees

2:3:40

to join my company the latest two people okay i hope everybody's cleared you're all

2:3:44

comfortable with select statement from statement order by so i hope the clauses are

2:3:49

clear now so now we'll see some demos use cases but most importantly everybody's seen the

2:3:53

know select from where order by limit

2:4:00

okay this one example is just to help you understand what is going on so this is the

2:4:07

main table there are 10 000 rows imagine we have in the main table so the main table

2:4:13

there's the main table there 10 000 rows where so this is your order of execution

2:4:18

this is actually very important this is your order of execution here so squl

2:4:22

the order of execution is very important in what order the statements are executed so

2:4:27

so first we select from

2:4:29

I mean table in 10,000 rows are. Imagine you of the employee table,

2:4:34

there's 10,000 rows are. Now from that, only 2,000 satisfies the criteria.

2:4:42

10,000 blocks from only 2,000 tally 2,000

2:4:45

rose came out of which now you sort them from largest to smallest.

2:4:53

Now the rows are filtered this way. Now, it's sort kind of, it was sorted in an assembly line

2:4:58

in order, sorting.

2:5:00

Then, limit, allow only three, only three will come, and final output, select.

2:5:06

You're able to visually see how the flow is happening.

2:5:10

You can just wanted to show you a diagrammatic representation.

2:5:15

So these things we have discussed already.

2:5:16

Just wanted to cover up the slides, whatever I talked about all this file.

2:5:20

This is between clause.

2:5:21

We've seen in or between example.

2:5:24

In or between.

2:5:25

And this is the thing that we looked at.

2:5:28

There is something called like.

2:5:35

Like we are here to discuss.

2:5:36

We'll like example.

2:5:37

What is like used for we will see.

2:5:40

And these are some of the similarities that we have covered before.

2:5:44

Now, you see, too, Python 2 SQL's similarities.

2:5:47

What are you guys have done?

2:5:50

Left hand side, we have the Panda syntax, DF.

2:5:53

Select start from.

2:5:54

Whatever I told you, like, DF, name and salary.

2:5:57

Here here here here here, selects, select, name and salary.

2:5:58

from table.

2:6:00

This is like a where clause in Pandas, you know, you are selecting all the rows where city is Delhi.

2:6:04

So select start from table where city is Delhi.

2:6:07

Simple.

2:6:07

You have your equivalent Panda syntax here.

2:6:10

Okay.

2:6:10

This is the way how you do in Pandas is in, you know, so this is the way how you do in SQL.

2:6:17

Select start from table where city in Delhi, comma, Mumbai.

2:6:20

Yeah, or say be correct.

2:6:22

And select start from table, order by salary, DESC.

2:6:25

This is the way how you can do in Pandas.

2:6:27

And finally,

2:6:28

DF head 5, limit 5.

2:6:30

These are the equivalent ways how you can do this.

2:6:45

So now we'll look at a few case studies.

2:6:47

So what I've done is just to give you a small flavor, a small example of these things in action.

2:6:55

I have taken a series of a few case studies so that you get to under.

2:6:58

stand the floor a little better.

2:7:00

So first thing, we are taking a small case study of a ride-hilling operation.

2:7:04

Imagine we have OLA.

2:7:07

We are looking at a small example of a ride-hilling service called OLA.

2:7:13

And we need to investigate bad customer experiences.

2:7:19

Okay, so first, your table will.

2:7:21

So what I did here here?

2:7:23

This is our real-world case study.

2:7:24

The first one is that of OLA.

2:7:28

So I have created a simple table, okay?

2:7:30

Abhi, our database, there's only one table, which is the employee table.

2:7:34

So what I have done, I will now create a new table called OLA rights.

2:7:40

So first I will create the table.

2:7:43

And second, I will insert values into the table.

2:7:47

I will insert values into the table.

2:7:49

And see, the moment I run the code, you will be able to see that my OLA rights table is created.

2:7:56

This our OLA rights table, we have now made.

2:7:58

sample reports. So this table in the information, customer name, the driver rating,

2:8:04

distance, fair amount, right status, and payment mode. So this is customer level information.

2:8:09

So these are customers who have taken OLA rights before. So we are able to see who is the customer

2:8:16

and just one second, guys. So we are able to see who is the customer. What is the rating they gave

2:8:23

to the driver? Distance how travel? Fair amount, how is, status, how it's, payment mode, how paid.

2:8:28

pay here. This is actually how the data is getting stored in the back end. So real world

2:8:33

when we are booking OLA rights, we're just applications right book

2:8:37

but in practice, this is how the data is getting saved. If you see, in practice. So in the

2:8:43

backend, OLA Uber, they are having databases. What database in data store

2:8:46

permanently, right? So that's the way how it happens in the real world. Right? And guys, if you want

2:8:52

to run this at your end, you can go to your, you can go to your, you can go to your, you can go to your

2:8:58

my SQL one compiler. Okay. So now that we are done with the employees one,

2:9:03

you can just to make it easy. You have all delete. Okay. Remove the whole thing. Empty

2:9:08

clean. Clean care. And just start with OLA. This is the easy way to work. Okay. Okay.

2:9:14

Okay. Now we employ. Now just OLA. Now we're only on OLA. So you're just to see the OLA rights

2:9:23

table. This is the way how you can do it. It is select from OLA rights.

2:9:28

So first you create the table. And second, you insert values into the table.

2:9:32

These both you ignore because you have practice in any kind of. I told you,

2:9:36

all of this permission not give. So you will only be doing select. And then you finally run the code.

2:9:42

And you can see, yeah, your information is. Right customer, driver rating. So whatever I'm showing, you can also do.

2:9:47

You guys can all run this code as well.

2:9:51

So what is the real world use case that I want to solve? What is the, uh,

2:9:58

you know, very practical thing we can go and do.

2:10:00

So what is the problem statement?

2:10:03

These are some examples of problem statements that analysts will want to check.

2:10:07

Now your entire information table in.

2:10:09

OLA's table in, customer table. So this is the problem statement that a stakeholder might want to see.

2:10:14

I want to investigate bad customer experience. So find all completed rights where driver

2:10:19

rating was three or below.

2:10:21

So how can you? Find select start from OLA rights and you check where close.

2:10:28

Right status completed and rating less than three.

2:10:31

So this is how information is retrieved.

2:10:34

And you know what?

2:10:35

Let me add one more case.

2:10:37

This thing, we retrieve and we're in a chart in present.

2:10:40

We can that we can do that.

2:10:41

We're not going to be.

2:10:42

But you can also retrieve the data and you can present it to a, you can basically present it in a chart kind of one.

2:10:51

So imagine you have a, you know, you have the operations head of Ola.

2:10:55

Or the operations head of Uber.

2:10:56

It's a, he has a chart chate, he needs.

2:11:00

He has a dashboard.

2:11:01

You know, where they want to see.

2:11:05

They want to visualize.

2:11:07

See, one way to do it is you can, you can just write a query.

2:11:12

He select ride ID, customer ID.

2:11:14

We can this could show us.

2:11:15

It is that the rights where it's completed, but driver rating,

2:11:18

two or three from.

2:11:19

So we want to know what went wrong with these rights, basically.

2:11:23

But you don't want to see the data this way.

2:11:25

You know, you want to go back and kind of, let's say you want to go and show this as a bar chart.

2:11:37

You have this to a bar chart in a chart.

2:11:39

Or if you're visually you want to try.

2:11:41

Like, you guys have gone through it, right?

2:11:45

I think you've gone through the, you guys have gone through the, you guys have gone through the visualization module right?

2:11:52

No?

2:11:52

Visualization.

2:11:52

Okay, right?

2:11:53

Okay, now that you've done.

2:11:54

Okay.

2:11:54

So basically, you can.

2:11:55

can visualize your data.

2:11:56

Pandas may have visualization.

2:11:57

So these are cases where this will come in handy.

2:12:03

You have here you can't.

2:12:05

This is the use case.

2:12:09

Ah, we will see that.

2:12:10

We will see that.

2:12:11

Yes.

2:12:13

Now, moving on, food delivery marketing.

2:12:19

Food delivery marketing.

2:12:21

So this is another use case.

2:12:22

Okay.

2:12:23

So let's look at the two use cases here.

2:12:24

Use case number.

2:12:25

one, find all completed rights.

2:12:27

Use case number two.

2:12:28

Marketing is running a high promo, high promo for high value UPI users.

2:12:34

Okay?

2:12:35

So, so he's important.

2:12:37

If you're, if you're a heavy spender, we are looking at actual business problems.

2:12:43

It is not like we are just doing SQL to, you know, write some select query just for, no.

2:12:48

It's a, ultimately it's a business problem.

2:12:49

Everything starts with a business problem.

2:12:51

What is the problem that you are trying to solve?

2:12:53

Of course problem can solve.

2:12:55

So problem I have to solve is this.

2:12:58

Find the top three longest completed rides by distance paid by you paid by UPA.

2:13:03

I want to know who are my customers using Uber and OLA mode.

2:13:06

I don't want customers who are like five kilometer

2:13:10

or three kilometers to write book and complete

2:13:12

or $100 right book.

2:13:13

No, but can I really find customers which their average ride value

2:13:17

that's up to that is interesting.

2:13:20

Because these are my cash cows.

2:13:23

This is our pisa are.

2:13:24

So we want to go and focus more.

2:13:25

on those customers.

2:13:27

So using these kinds of queries, you can find out who those customers are.

2:13:31

So get me all those customers from the OLA rights table, where payment port UPI

2:13:36

has, right status completed, order by distance DESE, limit of three.

2:13:40

This is the way how you work towards the query.

2:13:43

Okay, so I'm just trying to give you a case study mode of thinking, how you look at different

2:13:48

types of data sets and how you have a problem and how you think in terms of a key.

2:13:54

Problem statements say, how do we think.

2:13:55

of the query, that query is what?

2:13:58

We can also look at a next case study.

2:14:01

Zomato Swiggy-Bala use case, food delivery.

2:14:05

This is a very interesting use case.

2:14:06

You can see, it's solved here because again,

2:14:08

first class I don't want to, you know,

2:14:09

get into too many exercises today.

2:14:11

But let's say Zomato is launching a budget campaign.

2:14:17

And pull a list of active fast food.

2:14:19

So, so first first, your restaurant's data

2:14:22

okay.

2:14:23

So Zomato restaurants,

2:14:24

first, you have to make it.

2:14:26

Okay, let me just first create the table.

2:14:30

I will first create the table.

2:14:31

Then I show the data to you.

2:14:34

This our Zomato's a table.

2:14:38

Here we can see the table.

2:14:42

Here it is.

2:14:52

So you can see this is my table right now.

2:14:54

So we have information about restaurant ID, name, cuisine, rating.

2:15:05

What is the name of the restaurant? What is in the name of the restaurant?

2:15:08

What is in day? What is the average rating?

2:15:11

What is the cost for two? Is it active? Which city is it is? It's like if you go to an outlet.

2:15:16

You have information as a day. This is the actual way. This is the restaurant's table.

2:15:21

So I'm showing this to in a very small scale.

2:15:24

So that is the way how learning should happen.

2:15:30

So I am showing you in very small scale.

2:15:36

But if you want to expand the analysis and get into some exercises by yourself,

2:15:43

you go ahead, I'm going to upload the Kaggle as you know, Kaggle is like a very good community

2:15:48

for, you know, data scientists.

2:15:50

there's many data sets share. And this is the data.

2:15:52

So matter to restaurants data. It's a huge data system.

2:15:54

this is a massive data set you've got.

2:15:57

You can say a core data set be it.

2:15:59

You can see Zomato, Zomato restaurants data.

2:16:05

This is a massive data set.

2:16:08

Search five datasets.

2:16:09

Now look, Zomato, Bangalore restaurants.

2:16:12

Many downloads.

2:16:13

And you click on it, this is a very good data set.

2:16:15

This is a much bigger data thing.

2:16:17

And I can see you, a file here, 575mB.

2:16:20

It's a massive data set, very detailed data.

2:16:23

And this is your data set.

2:16:24

You have address, name, online order, book table, can you book a table, like that?

2:16:31

This is real data, completely real data, rating, votes, okay?

2:16:36

This is how it is.

2:16:37

So this is the simple example where they are shared the thing in a CSV file, but in a real world scenario,

2:16:43

in Zomato's case, they will actually store this in a table.

2:16:46

This information, they will actually store it in a table.

2:16:49

In up to the proper table, they will be storing the information.

2:16:51

Database in a table may, this information stored in practice.

2:16:54

So you get the feed, you get the connect how it's actually done in practice.

2:16:59

Okay, all of you.

2:17:00

Now, coming back to the use case once again, so let us see.

2:17:05

So pull a list of active fast food or dessert places that cost 500 for food.

2:17:12

They are launching a budget bites campaign, right?

2:17:14

Budget bites, but a quick, quick food, budget bites.

2:17:16

Some of the people are looking for, you know, something where they can grab a quick bite at a low cost.

2:17:21

So how will you do it?

2:17:22

How will, how will Zomato, shot?

2:17:24

those restaurants that they want to promote.

2:17:27

Like Zomato's a co sales team, there, marketing team, and they have to promote those restaurants.

2:17:32

So, so it's going to be active on here.

2:17:35

Where is active true?

2:17:36

And cuisine in this and cost for two is this.

2:17:40

So there are three conditions we have applied.

2:17:42

Okay.

2:17:43

Active has to be true.

2:17:44

Wezine has to be either this or this and cost for two has to be this.

2:17:47

See how see the see the flow, all of you, everybody.

2:17:51

So the connect has to be clear.

2:17:52

Real world, you will have problem statements.

2:17:54

And the connect has to be clear, how we are solving those problems.

2:17:59

And very similar to PANDAs, as I told you, like, given you've already seen data frames,

2:18:04

you can see the connect, how simple, the SQL part actually looks like here.

2:18:09

Okay, so you have a zomato example.

2:18:11

Let's just wanted to show you an example.

2:18:16

Shared, all shared, everything is shared.

2:18:18

If you go to the Google Drive, 27th April of, go, here all shared.

2:18:23

Everything is shared.

2:18:24

Find the top three most expensive, active restaurants across all cities, ensuring

2:18:33

they have a rating of at least 4.4.

2:18:36

This is a very interesting use case.

2:18:38

This is actually a very interesting use case, isn't it?

2:18:41

See, this is like expensive be hey or rating be a lot.

2:18:50

It's a big deal.

2:18:52

People are rating it very well.

2:18:54

At the same time, it is very expensive.

2:18:56

Sometimes, if, people are the poor rating.

2:18:59

That's, you know, that's, so, you know, I'm just saying.

2:19:02

But it's a very interesting business problem.

2:19:04

Imagine somebody is thinking from Zomato's perspective,

2:19:07

some management stakeholder is thinking,

2:19:08

which are those restaurants in the city,

2:19:11

which are commanding a very high rating despite being very expensive?

2:19:16

Yeah.

2:19:17

So that's a clue.

2:19:19

Now Amazon may go.

2:19:20

I'll give you a very simple use case.

2:19:21

You go to Amazon, search for some very expensive products.

2:19:24

And you will sometimes see people have rated it very long.

2:19:27

You'll get it.

2:19:28

You'll get it.

2:19:30

People have given it one star.

2:19:33

Because you have spent so much money buying it.

2:19:35

And then maybe it's not worth the money.

2:19:38

And I'm just giving some simple examples.

2:19:40

But this is a very interesting business problem.

2:19:42

Right?

2:19:43

This how can solve?

2:19:44

First business problem and then translate that to SQAWL.

2:19:47

So select the details, name, city.

2:19:50

Here on the column select from the main table, Zomato restaurants.

2:19:53

is active true and rating has to be greater than 4.4.

2:19:58

Sort in descending order, please.

2:20:00

And limit by 3.

2:20:01

Because I have to find out top 3 most expensive.

2:20:04

Top 3 most expensive,

2:20:05

what's the sort kind of descending in head of 3.

2:20:08

Matumat of limit of 3.

2:20:09

If you want to see the corresponding thing in Fandas.

2:20:14

This is your top 3 restaurants are.

2:20:17

Okay?

2:20:18

Maybe what Zomato can do is they can come up with a restaurant campaign

2:20:22

you're rewarding these, you know, this restaurant people because they are doing a good job.

2:20:28

They're able to maintain a very high quality of food.

2:20:31

At the same time, they're able to keep people happy.

2:20:33

Because people are, you know, able to feel that, okay, you know, whatever money we are paying is,

2:20:37

what's the food we are getting?

2:20:39

Okay?

2:20:39

That's the intuition.

2:20:41

Okay.

2:20:42

So case study number three, let us see the next case study.

2:20:45

Netflix.

2:20:46

This is a very real problem, very interesting problem.

2:20:49

So, subsequently, Netflix's data created.

2:20:52

And again,

2:20:52

Netflix in the real world, they will store data in a table.

2:20:56

They will have massive tables.

2:20:58

It's not just one table.

2:20:59

Netflix's the user base, how much?

2:21:01

300 million, 400 million user base

2:21:03

are all data tables in.

2:21:05

Can you imagine 300 million rows of data are stored?

2:21:08

So Netflix's that only will,

2:21:09

500 million to be Netflix.

2:21:11

Netflix will easily have a 500 million user base.

2:21:14

Hundreds of millions, 500 million, 600 million.

2:21:18

So imagine if you have a user table,

2:21:21

that user.

2:21:22

table will have 500 million rows.

2:21:24

Every row will be one user.

2:21:27

Can you imagine the scale?

2:21:28

Can you get the dual as in Excel?

2:21:30

No, so this is so important.

2:21:34

Okay?

2:21:34

So this is a Netflix user's table.

2:21:36

Exactly how it is done in practice.

2:21:38

User ID, username,

2:21:39

what subscription type is.

2:21:41

How much watch hours have last month?

2:21:43

Month subscribed, country, which country you're from?

2:21:46

Because country's basis

2:21:47

on, okay, 205 million.

2:21:49

So this is all information Netflix to be stored

2:21:51

and this is stored will be.

2:21:51

okay and this is how your data will look like in practice okay this is exactly how your data will

2:21:57

look like in practice Netflix table

2:22:01

okay all of you can see first let me show the table to all of you how it looks like

2:22:05

there goes your Netflix users table so here it is so we have the information right

2:22:14

now and now let us talk about the equivalent business problem what is the

2:22:19

business problem that we are trying to solve out of this

2:22:21

So the business problem, the first one is premium tier users paying the high fee, but watching less than 10 hours a month are about to cancel.

2:22:33

Find them immediately.

2:22:37

What we are talking about is customer churned.

2:22:40

Customer churned means what is.

2:22:42

It's often, maybe,

2:22:43

imagine your, uh,

2:22:44

there are many people who are paying 200 rupees a month,

2:22:49

so the amount doesn't seem to be high,

2:22:51

but when you do it over a period of time,

2:22:53

you think,

2:22:54

you think,

2:22:54

so, okay,

2:22:54

so this is what is referred to as churn?

2:23:00

Churn means you are leaving the brand.

2:23:04

The churn basically means that you're leaving the brand.

2:23:07

That is the meaning of churn.

2:23:11

Okay?

2:23:12

so premium tier users paying the high fee but watching less than 10 hours a month and can we find some of those users who are paying a very high fee but we're using a correct they are not even watching Netflix

2:23:26

so these users any day they can cancel subscription because they will probably feel that okay i'm not getting any value out of it

2:23:34

they're not even watching Netflix okay so see they connect all of you okay so can we find those users very easy

2:23:41

plan type premium and watch hours less than 10 so this is the way how we are

2:23:46

solving a business problem this is not like writing a SQL query we are we are ultimately solving a business

2:23:51

problem okay so can we find out who those users are let's see let's run the query and we can see okay

2:23:56

here are the two users like user Zeta user C whoever these users are and then what is the next thing

2:24:01

you will do next thing what is the next thing you will send them an email and say hey like here was a

2:24:06

a 30% renewal discount for you okay so they didn't

2:24:11

ask for it but you are proactively trying to prevent them from churning okay so ultimately

2:24:16

everything is tied to a business problem yeah so that is an important thing you have to keep in mind

2:24:24

next use case we will see a small retail use case so i said just a second guys panels

2:24:31

me yeah okay what is that okay yeah so we'll do a small retail use case just two more i've got left

2:24:37

and then we'll do a couple of other things then then we'll go to the uh quiz

2:24:41

okay so let's do the use of e-commerce one so e-commerce

2:24:47

table let us see the e-commerce products table so there goes the e-commerce products table

2:24:55

product ID name category price so this is the way how amazon will have a massive table of products

2:25:03

imagine the number of products amazon will have in their catalog millions right millions hundreds of thousands to millions

2:25:11

amazon will have millions of products in his catalog and every single product that

2:25:17

amazon has whatever you see on the amazon website every single product that is listed

2:25:22

is ultimately stored physically in the product's table

2:25:27

uh images whatever alux is stored here that's a different thing i was talking about no sequel

2:25:31

that's a different way but the information that you are seeing product of price product a description

2:25:36

product uh whatever information you are able to see about the product all that is getting saved here like this

2:25:41

id name category price okay rating all that now what is the business problem

2:25:48

let's look at a sample business problem so business problem would be a similar business problem

2:25:55

here would be the inventory management team needs an urgent restock list

2:26:02

but of stock karni isn't it imagine uh you have a particular product

2:26:09

of customers go especially during offer periods when when when sale is going on it is very

2:26:17

very important to know especially during times when offers and sale is going on it is very

2:26:22

important to know key when i have to stock my products so stalking the products is very

2:26:27

important so how do you restock it when do you decide you have to restock it that's the problem we

2:26:34

are solving here so inventory management team needs an urgent

2:26:39

restock list how do you do it so find all electronic and apparel products that are

2:26:46

currently out of stock so this is the way how you can do it okay so find out all those products

2:26:54

which are out of stock and then you can immediately send it to the vendor team and you can restock

2:26:58

that's the idea all right next up we can look at a fintech and banking use case just two more

2:27:07

a left out you can see this is typically how a bank will do this in practice

2:27:17

let me just show you these are all very similar cases only this is the bank transactions data

2:27:21

i was already discussing this a while back that how does the bank typically store the

2:27:25

information so banks you will usually store your data this way transaction id

2:27:30

see whenever you transfer money to somebody as a transaction id and this is the way how they will do it

2:27:36

who is the user what is the type of transaction what is the amount status

2:27:40

what is platform yeah sometimes successful are sometimes failed pending

2:27:44

all this is actually logged so at the bank level whether it is i c s i sd fc svi

2:27:50

jvc svii joe be bank hey this is exactly how the data is got locked there is actually a transaction

2:27:54

table so so far we have been discussing about millions hundred millions netflix that they say

2:27:59

hundred million three hundred twenty five million rows of users can you imagine the size of this table

2:28:04

this will be massive this will go into trillions of rows more than that banks will

2:28:11

store historical data also right oh kabi kabi purge karek because you can't physically store so much data

2:28:16

but the reserve bank of india kabe mandate that you have to store transactions up to a certain

2:28:22

because see frauds and all can happen right so oftentimes when you're investigating

2:28:26

a police case if i are you have to go back 25 years back pull up somebody's records and all that so

2:28:31

banks will never never delete any transaction data

2:28:34

they will all store it and we are talking about what is the scale the scale will go into like

2:28:42

you know we can go into tens of trillions of rose trillions there's no there's no count of it every day we are

2:28:49

talking about if you look at the numbers right now every day upi credit card all the you know

2:28:54

if you look at all the uh modes put together we have so many transactions that happen so the volume is

2:29:02

enormous if you just look at the number of rows that they

2:29:04

table will have that will be that will go into trillions tens of trillions basically that is the

2:29:10

that is the that is the information we are looking at what could be a business use case

2:29:16

the fraud detection team wants to look at high value failures find the top three largest

2:29:22

failed or pending transactions this interesting business problem right oftentimes you have

2:29:28

seen that when users are transacting using certain modes the transaction fails and this is

2:29:33

is actually a bad customer experience and you have

2:29:36

flight booking or you have or or then hotel booking you want to do or some other

2:29:40

booking you want to do and if you're paying through uPI you might have seen many

2:29:43

platforms are implementing this so while payment payment they will actually

2:29:47

tell you that the gateway may not work upi may not work this may not work so they have

2:29:51

started incorporating analytics and they are giving you guidance so that is what it is about

2:29:57

okay so the fraud detection team is able to identify okay these things are likely to

2:30:01

fail can be analyzed why

2:30:03

query case how here where status in failed comma pending status should be either this

2:30:10

and order by amount de s c find the top three largest because this is concerning these customers

2:30:16

were doing very high value transactions and they failed or are in pending status and now you need

2:30:20

to investigate why that happened okay so this is a business problem okay okay this is what we have

2:30:30

and what i encourage you to do we have got a maybe a few minutes we can take on these

2:30:34

exercises this is pretty much like what we have here there's nothing much to talk about here so this is

2:30:40

pretty much what we talked about create table insert into select of broprint we

2:30:44

talked about so all these things we talked about operators we talked about

2:30:48

okay and one operator like like operator

2:30:51

I mean basically if you want me to show you like the demo detail but like is

2:30:57

actually very simple let me see if that is mentioned here so like would be based on a particular

2:31:07

but of something like this you so like would be based on a pattern right so look at us all

2:31:13

of you life checks if a text value matches a certain pattern that is what like is used for

2:31:21

because for example when you say this where name like a percentage which

2:31:27

means you want to get all those names which start with a and there are any number of

2:31:34

characters that can come after that so they are basically used for text matching

2:31:39

okay you don't have to memorize it but just remember what it is but just just just

2:31:42

just remember there's something called a like operator okay so that's what like operated

2:31:46

but basically this is pretty much what it is and is null is for missing value just say our

2:31:51

pundas may say if you want to you know select for you can use is null for that

2:31:58

okay now moving on guys what i wanted to do a couple of very interesting things number one

2:32:04

i want to share with you this link okay you pandas k all this way and uh

2:32:11

i think this this will be very helpful for you so that if you come across any pandas code

2:32:15

oftentimes we have this question how to visualize okay because uh you know visualizing you know

2:32:21

visualizing the information is very easy is very important right so there is something

2:32:25

called panda's tutor you have any of any pander's code you have here

2:32:29

down and you can actually visually see

2:32:32

how that it very nicely connects with what we discussed today right

2:32:36

you here herephe desksaicccied you can't you can't

2:32:39

particularly in python the syntax gets very complex as ql so okay it's very easy

2:32:43

right but python in particularly what you can do you

2:32:45

you can see that the first we've made

2:32:48

medium filter here okay so far out of all these rows we are only selecting medium

2:32:52

the first medium selected then then dot sort values sort values in

2:32:56

what we have that we've got sort here you can see how sorting

2:32:59

and then we're group by type dot median here grouping

2:33:04

so you can actually see how it's flowing so this is a very useful site where if you

2:33:09

you can try this out i'm sure you're doing pandas you have some complex code

2:33:14

you can put it in this editor and you can see visually how things are happening and so

2:33:18

Similarly, there is also something called Python Tudor. You can try this out, okay? I don't

2:33:21

know if you know this already, but even this is very nice actually. So you can start to visualize your

2:33:26

code. If you can type you can start to visualize it in a very nice way. Okay, so this is two tutor

2:33:36

sites you've got which will be very helpful for you going forward. And second is I wanted to share

2:33:41

with you this part, this thing. Similarly, in the world of SQL, you've got something called SQL

2:33:46

okay so you have explored can okay because i'm not stressing too much on

2:33:51

SQL because SQL we have only two classes this is not much in SQL we have but still if you're

2:33:56

curious you can use this thing called SQL flow but definitely Pandas tutor and Python

2:34:01

tutor you must bookmark because your entire course is in Python we'll be writing

2:34:04

Python code all through the course okay so but particularly for SQL you can keep this site as

2:34:10

reference okay and next thing what i want to do is

2:34:16

we will do a very nice interactive thing there is something called sequel bold.com

2:34:25

and what you can do at least we can write one or two queries before we close today right

2:34:31

so we've got something called sqlbolt.com you can all go to the site and what you can do

2:34:36

here you can actually go and click on begin lesson and you can start writing some

2:34:46

some sample SQL queries here okay so whatever i discuss today with you at least you can go and

2:34:54

write it's a very nice interactive way to learn you know so maybe up directly you can click on this

2:34:59

link so you can see there is a small table that is given you know you're simple it more simple

2:35:05

based on whatever we talked about you'll find this is like so simple okay but this is a nice

2:35:10

interactive way you can do some exercises okay so simple all of you can see exercise number one tasks

2:35:15

fine director if you want to go to a new next one maybe we can go to uh queries with

2:35:22

constraints filtering and sorting so we can actually see filtering and sorting

2:35:27

sorting lesson four me a less than four complex so we can maybe we can this will make more

2:35:31

sense so can can we can we can do this one number one you guys can try this

2:35:45

you don't look at the answers objective is to make you do it

2:35:49

so try this out based on whatever we covered today you can go to the link and you can see the

2:35:56

main table the movies table that is uh yeah yeah no then a sequel flow is just for

2:36:02

visualization yeah though but general links eh actually actually this is nothing to do with the

2:36:07

concept of sqql i'm just sharing which of some reference links which will help you to do

2:36:10

do some things yeah yeah this is nothing to do with sql per se these are just general links

2:36:15

sql flow is basically used to visualize your query you can you can you

2:36:19

how it's happening whereas this is mainly like an interactive lesson this is like a

2:36:26

somebody has created this website sql bold.com where they wanted to teach you

2:36:31

SQL in an interactive way okay so if anybody wants to see and learn

2:36:36

SQL in an interactive way you can just kind of use this thing it's just

2:36:40

resources that you have right now okay so okay so you

2:36:44

you solve not but just wanted to show this to all of you so imagine uh i'm doing the next

2:36:49

one list the this one list all directors or picture movies uh alphabetically without duplicates

2:36:58

how'd you do it how do you do it you just have to write the query and uh based on that it will

2:37:05

give the results to you okay so how's how can select select director select select director select

2:37:14

so first select from the table name which is movies so i think the table name is movies right

2:37:21

let me just check table name is movies so select star from movies and i want to select the director

2:37:31

director from movies and see as when you type very interesting can you see real time this is

2:37:36

happening and just as you correct you correct correct so answer will get okay so what will be

2:37:44

and you have to list all directors alphabetically

2:37:48

what select director from movies and what order by director order by director

2:37:56

aAC that's it but last take chee what is that what is that after order by go

2:38:02

director is sorted in ascending order just last take is a repetition for that this is

2:38:08

is something i'm not taught you it's not in the content also today it is actually for

2:38:11

distinct you can do distinct or abdh de for

2:38:14

matched or just matcho your next line again can you see very interesting right

2:38:20

this is a very nice way to practice if you if anybody is curious and if you want to like practice

2:38:24

some more as i told you skewer is not we don't have too much of SQL here but if you want to learn

2:38:29

some more SQL there's some very interactive uh lessons you can actually explore from here

2:38:34

okay but this is optional this is not part of our contact okay all right all right guys uh any questions

2:38:44

all clear and the last part that i wanted to share with you the final thing the final

2:38:48

thing that i wanted to share with you is how to connect uh how to basically connect

2:38:54

you know your your your your your python with sql your for this you can go and use something

2:39:01

called uh sequel alchemy okay or you can also write panda's sql up as up a python

2:39:08

under be sql except so i will not get into that today maybe next class i will show you a bit on that

2:39:13

because it will be too much to take in one one class okay so next class what we can do is i will i will

2:39:17

show you how you can write uh sql inside python because because so far you have worked with panda's

2:39:23

data frames you've been writing a lot of python code and sometimes the python code can get a little

2:39:28

complicated right so if you find sql easy if you find select star from easy if you find that

2:39:34

uh you know the sequel way of writing and creating data is easy okay then you can use squel write

2:39:42

within kanda's date of them okay there are ways to do it that that that that's some couple of demos i will

2:39:47

show you next class hello so uh everything is there action please uh some of you who join

2:39:56

late i'm going to share this once again with you this is the complete cohort link i've created

2:40:01

for you okay so whatever materials i shared will be available here please take this uh

2:40:07

complete cohort link okay and i will continue creating for every uh uh

2:40:12

session i will create the date and i will share all the resources within that date okay i hope

2:40:18

that's clear so you can find all the contents under the 27th april folder

2:40:25

but rest i hope everybody was able to do the demos along with me any questions anybody has

2:40:31

in the meantime i will also you know pass it over to prata prath will take care of the quiz and

2:40:37

other things and yeah so that's all from my end if there any questions guys guys guys

2:40:42

you want to ask me anything at this point in time

2:40:45

i hope everyone's able to see the contents so the PDF that i shared and the

2:41:00

it's a small handbook where you can kind of just use it for as a ready reference whatever we

2:41:06

cover today you can use it as a small ready reference pandas versus sq will what are the

2:41:10

differences okay some of the things i discussed today all that i covered today is a ready

2:41:15

reference that it's available here okay some of the mathematical operators what is select

2:41:19

from where order by limit okay so basic things and this is again the main agenda

2:41:23

what we discussed today so we talked about sql basics talked about select queries

2:41:28

filtering data order by limit and uh

2:41:33

found out versus sql how similar the syntaxes are next session we will meet on a day before

2:41:38

day after the aesthetic uh and a day after tomorrow and we will see uh the concept of joins

2:41:44

group by having okay again very similar to fund us you have seen group by having there also

2:41:49

and we will connect the dots and we will see how it happens in sql okay so we will see

2:41:54

some more interesting topics in the next to next session okay thank you everybody uh

2:42:00

yeah so i will thank you all of you have a good night

2:42:08

yeah uh thank you so much sir for the wonderful lecture and students i am going to release

2:42:16

the poll now and after that there will be the mentimeter quiz so please wait for the

2:42:24

mentimeter quiz okay the poll should be live now please answer uh and then we can

2:42:32

quickly start over the mintimeter quiz i'm sending

2:42:38

the link here and i'll also share my screen okay i hope you guys are able to see my screen

2:43:08

quiz. Okay, some people still have not completed the poll, so please complete the poll and join the metameter quiz.

2:43:38

I'll wait for about 30 seconds more and close the poll and then I'll start the

2:43:50

Menti meter quiz.

2:43:51

You guys have about 30 seconds to join the quiz link and complete the poll.

2:44:08

10 seconds left to complete the poll and join the Menti meter link.

2:44:38

Anyone is waiting to join?

2:44:49

Anyone who is not joined yet?

2:44:52

But if you want me to start, I can start them.

2:45:08

We have five questions in the quiz and it should be relatively easy given the contents

2:45:14

are covered.

2:45:38

Someone told me the last time the quizzes were too easy, so I made the options a bit more difficult to guess.

2:45:47

Awesome. Most of you got it correct.

2:45:53

Wait.

2:45:55

Oh, oh no, no, no. Okay. This is the correct one. I apologize. I think I ended up selecting this one as the correct. It should not be.

2:46:05

This is the correct answer. Most of you did get it correct.

2:46:07

of you did get it correct so the leader board will be uh leader board will be messed up

2:46:16

the answers are not correct apologies for that

2:46:26

starting the next question the other ones should be correct

2:46:35

what is select what is select star from employees

2:46:37

semi-colon dove.

2:47:07

Um, so yeah, okay, next question.

2:47:37

80,000 include. So this question is relatively I mean, I mean, I mean, deliberately.

2:47:53

I mean, deliberately made to trick you guys. Um, oh great, awesome, most of you did

2:48:06

get that correct. See, remember, it is, SQL is easier, easier meant to write, sorry, SQL is meant to be simpler than Python. And that is why when it says 50,000 to 80,000, you are not supposed to do any, uh, inclusive, 80,000 is included, not included, whatever. All of that nonsense you don't really need to do. So whatever is written, it's executed as it is. So even 80,000 will be included. If

2:48:35

there is some value at 80,000, it will be included. If some value is 50,000, it will also be included.

2:48:42

Okay.

2:49:05

Okay, I'm going to start the next question.

2:49:16

Last two questions.

2:49:19

What is the correct execution order of SQL clauses?

2:49:24

Also covered by Sir.

2:49:35

This one is a little tricky.

2:49:42

Okay. Let's see if everyone got that correct.

2:49:53

Yeah. Yeah. So, um, sir, maybe if you're still there, you want to kind of cover this.

2:50:01

Or if you're not, I can just.

2:50:04

I can just, okay. All right. So yeah, as Sir did explain in his, uh, in the order of SQL clauses.

2:50:17

So essentially you will be doing first from then you will be doing. So it is like you're selecting

2:50:23

which database or table, right? Then you will have the condition. Then you will do an order by

2:50:31

then limit and then you will be having a select just because you write.

2:50:34

select at the start of the, uh, start of the query doesn't mean that it is the first one that runs.

2:50:42

So this is how it, this is how it works. Okay. This is a tricky question and, uh, of course,

2:50:48

I'm not going to blame the rest of the rest of the ones that didn't get it correct. But yeah, great job

2:50:54

to those who got it. And the others, please make sure you understand why this is the case. Okay.

2:51:02

because the engine needs to understand where are you execute from which table you are executing.

2:51:08

What are the conditions? What is going to be the order? What is the limit? And then it will run the select.

2:51:14

Select command. Okay. Next question.

2:51:23

It seems Arnica has the answer key. She got the first one which was not right also.

2:51:32

correct. Anyways. All right. Last question. Which limitation is most

2:51:46

strongly associated with file-based tools like CSV or Excel in real world systems.

2:52:02

intentionally so that it makes guesswork a little difficult. Read the answers carefully

2:52:09

and selected. There's one very obvious flaw that CSV Excel systems have. Awesome. Awesome. Most of you got it correct. All right.

2:52:32

Okay. All right. So since the first question was actually wrong, we shouldn't really trusted. But then anyways, congratulations at Nica. And we are going to end this quiz here. And end the session now. All right, guys. Thank you for joining. See