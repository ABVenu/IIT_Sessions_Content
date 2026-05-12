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

Yeah, guys, we can wait for everyone to join and then we can start.

12:17

I think the voice is clear to everyone, right? Can you hear me?

12:21

Yeah, we can wait for everyone to join and then we can get started.

12:40

Thank you.

13:10

Thank you.

13:40

Thank you.

14:10

Thank you.

14:40

Yeah, I think we can start. Can you hear me?

14:43

Is the voice clear to everyone?

14:50

Yeah, I think we can get started. So let's start with today's part. You will see this that in today's class we will try to discuss a lot about databases and everything.

14:59

So yeah, I think one by one we can get started and we can see this particular part that is there.

15:04

So yeah, I think let's start. Today you will see that we will see a lot in database.

15:10

like last time you were saying, right, that a lot of you don't know about SQL.

15:15

So you will see this week we will focus upon databases and we will try to cover SQL in detail.

15:20

That will be the main agenda.

15:22

So yeah, I think one by one we can get started.

15:25

So let's start with today's part.

15:27

We can start with first concept.

15:29

It's already 8.5.

15:30

So we have waited, yeah, for everyone to join and then we will start.

15:34

We will see today Nilema, what is SQL, what are databases in detail, everything from scratch,

15:40

we will try to talk about.

15:42

So yeah, I think everyone here is aware of CSV files.

15:46

Like, are you guys aware of what is CSV files that are there?

15:50

I think you can know, right?

15:52

Blad, have you ever tried it?

15:54

That if you open a very big CSV file,

15:56

which is having like 1,000 entries that are there.

15:59

And what you do is you try to open that CSV file in your laptop.

16:03

Then you will see that sometimes it becomes, it breaks.

16:06

Like if you open it in Excel, then it breaks.

16:09

And the results.

16:10

are very, very slow. So in real life, like whenever we are working with large amount of data,

16:16

you will see this that there will be no scenario in which we will be storing large amount of data

16:21

and big CSV files that are there. We can download the data, but generally in companies,

16:26

this kind of data or this kind of file format is not followed.

16:30

So you will see this, that CSV is nothing but that Excel sheet. I think have you seen

16:35

Excel sheets, right? That are there, Sahel. I think everyone here has

16:40

seen basic Excel sheets that are present up. Have you seen that or not? I can probably share. Just give me one minute.

16:48

This kind of basic sheet, have you seen? Like in which some columns are there, rows are there, correct, right? So this is one.

17:09

So this is one of the format of Excel that is there in which you can see this, that a lot of questions are written and a lot of things are written, right?

17:16

This is nothing but a basic Excel sheet that is there.

17:20

This kind of things is called as what?

17:22

It is called as what? It is the CSV format.

17:25

Generally, if you want to store data, we will not be storing data in these kind of sheet.

17:30

I think the idea is clear, right?

17:32

Is everyone able to understand this?

17:37

So you will see this that in company?

17:39

what we will try to do is we will not be using these kind of Excel Excel sheets that are there.

17:44

And it will be very, very tough. Let's say that if you are updating everything into SQL and I am

17:50

updating everything into SQL, then you will see this that there will be a lot of compatibility issues that

17:55

will come up. A lot of merging issues will come up. Like for example, if I do this, that if I give

18:02

this particular sheet to everyone, let's say I create a new sheet right now. And I just share

18:08

it with everyone and I give editor access to everyone. Let's say let's call it as test sheet that

18:14

is there. And what I do is I give anyone with the link and I give here editor access. So if you do this

18:24

particular thing that if I share it with everyone, then everyone will start typing. Okay, like you can

18:31

create here columns. Like let's say if I create a column, let's say marks column that is there.

18:36

then I create some other column which is name then I create another column let's say amount

18:43

and these things right so you will see this that whenever we are having such columns that are there

18:48

then there can be a lot of issues like if you also start typing in the first column if I also

18:54

start typing in the first column then a lot of issues will come up that is why we cannot use

18:59

excel sheets for storing the data is that part clear

19:02

Is everyone able to understand this part?

19:09

So I think this part is clear, right?

19:10

That these kind of sheets, they are not useful.

19:13

They are useful for very small amount of data.

19:15

Whenever we are having large amount of data, let's say that if I have 10 million rows that are there,

19:20

then I cannot use these kind of Excel sheets that are there.

19:23

Is that idea clear or not clear?

19:25

Till here, this thing you are able to understand, right?

19:29

So we can see this that managing our Excel sheet,

19:31

CSV,

19:32

file, ExcelS file, all these are different different formats in which Excel sheet can

19:37

store the data.

19:39

This will be very, very tough.

19:40

So that is why what we are trying to do, we are trying to use something called as databases.

19:45

So now we will understand what is the database.

19:48

A database is nothing but which tries to store the data in form of rows and columns properly.

19:53

It can happen that it can store it in any particular way.

19:56

It's not compulsory that it will use rows and columns only.

20:00

It is just storing the data in a organization.

20:02

manner and it is helping us to query the data properly.

20:06

What is the meaning of querying the data?

20:09

Let's say today you have a lot of data that is present in your system.

20:13

And you want to find out what are the marks that are stored by this particular person.

20:17

Like, for example, in universities, you might have seen this, right?

20:22

That there are 10,000 or even 1,000 students that are present all over India.

20:26

Then they want to find out marks of, let's say, any particular person.

20:31

They give the role number and they want to know.

20:32

the exact marks that are there. So in order to store such an information, we can see this

20:38

that like good amount of databases or we can say we need such a system which is able to store

20:44

data properly. The that thing is done with the help of database. Is this part clear? This part

20:51

are you able to understand?

20:57

Guys, this thing are you able to understand?

21:02

We will talk about it, right? But currently you can see that anything which is storing the data properly is called as databases.

21:11

I think that idea is clear, right?

21:13

CSV is just a format that is there.

21:16

I think that CSV format is clear, right? Like, for example, if you go here, you can download this sheet in multiple formats.

21:22

You can download this sheet in CSV format. You can download this sheet in XLS format.

21:28

You can download it in any particular format that is there. Like if I show you,

21:32

like this kind of sheet that I was sharing, right?

21:37

This kind of sheet. This is kind of a XLS sheet that is there.

21:42

Same way if I open another sheet that I'm having here.

21:49

Let's see this sheet.

21:52

So let's say that I'm having this kind of a sheet that I'm opening.

21:57

So you can see this right.

21:58

This is nothing but an XLS sheet in which data is present.

22:01

I think this idea is clear, right?

22:03

So let's say I can show you even one more example that is there related to this part.

22:09

Let me share another screen.

22:12

Are you able to see this particular CSV file right now?

22:17

Can you see here?

22:18

So you can see this right?

22:19

Do you think this way if I'm storing the data properly, is it readable?

22:24

Can I query the data properly?

22:28

No, right?

22:28

We can say this that here you can see.

22:31

CSV's comma separated values. So first title is written, then company is written,

22:37

then location is written, then URL is written. You can see they are separated with the help of

22:42

commas. Now storing it and querying the data on these type of sheets is not that much useful.

22:48

Here you can see only 40 rows are there. But if I have 4 million rows, then things will not be the same.

22:55

Is this part clear? Is the idea clear that why CSV is not that much useful?

23:01

Other people and everyone is able to understand, right?

23:08

The next thing that we are having is, like for example, if we go to this particular part,

23:13

we were seeing this that different formats are there.

23:16

Now, in today's class, what we will do is we will try to see that what is database.

23:22

A database is nothing but which will store data properly so that it can find out data.

23:28

Query means finding out a particular data.

23:31

that is there. Let's say that today, all of your marks are stored. And if I want to find out

23:36

what are the marks of this particular person, this means I am finding something in the data.

23:41

This finding thing in the data is called as query. Is that part also clear? You will see this,

23:46

that all these functionalities it will provide and we will study about all these functionalities.

23:52

It will store the data. It will help us find out the data. It will help us update the data.

23:57

If let's say in future any data needs to be deleted, then it will help us

24:01

the data as well. Is this part clear? Tell here, are you able to understand?

24:12

I'll show you one real life like how data actually looks like and how database actually stores the data.

24:19

So let's talk about that as well. I think till here the meaning is clear, right, that what database is trying to do.

24:28

So if you see this particular screen, like,

24:31

For example, if I share this another screen that is there.

24:34

On this screen, can you see this particular part?

24:37

That here, some bank data is stored.

24:40

This is some Chinese bank data.

24:42

So we can see this, that data is stored properly into rows and columns.

24:46

We can see there are different, different columns.

24:48

And in each column, data is there.

24:50

In bank, there are millions of customers.

24:53

Currently, for demo purposes, I am showing you like seven or eight rows that are present in the table.

24:58

But actually, million amount of data will be there.

25:01

So you know,

25:01

order to store all the branch data, customer data, depositor data, loan data, account

25:06

data, borrower data, all these things need to be stored in proper tables.

25:11

The software which manages all these tables is called as a database. Is that part clear?

25:19

It can store multiple tables like this is one table, this is another table, this is another

25:24

table. So we can have multiple tables and each table will try to store the data.

25:28

Is this point clear? This point, are you able to?

25:31

understand.

25:34

Guys, still here, this part is clear, right?

25:40

Correct. So we will see this that how speed, concurrency, integrity, relationship, and security will

25:47

be happened via database. All these things we will see, but I think the basic definition is clear,

25:52

right? The database is used in order to store the data properly. Correct, right?

25:56

It is similar to sheets only that are there, but it is storing the data in effective manner.

26:01

The storage and the structure will look at the same, but it will store the data so much properly that query, update, delete, everything is happening in a very good way.

26:11

I think the idea is clear.

26:12

So let's try to go to the next part that what are different types of databases that are there.

26:18

The first type of database that we will study, which I just now showed you is relational database.

26:24

In relational database, we will try to store the data in form of rows and columns that are there.

26:30

Correct.

26:31

you will see this that whenever we are storing structure data, structure means that whenever

26:37

the data is related. Like for example, today if I want to store all the iPhones data that is there.

26:44

I know that all these iPhones will be related, they will be having common features.

26:49

Like for example, they will be having features like camera, battery, then price, RAM, all these

26:57

things, right, memory, all these things are common in all the iPhone.

27:01

Even if the product name is changing, the size and everything will change up, but they will be related to one another.

27:08

So we can see whenever you try to see this, that whenever we store the data in form of rows and columns, we call it as relational databases.

27:19

In relational database, the data is generally related.

27:22

Like if I'm storing data of all the iPhones, this means that all the iPhones, they are related to each other.

27:29

Same way if I want to store all the phones,

27:31

together into a single database, that also I can do that. But if I ask you that today you want to build

27:38

Amazon database, okay, and you want to store all the products that are out there. Do you think

27:45

you will use a relational database to store all the products? Like in a single table, do you think it is

27:51

making any sense to store all the products that are out there? Why, right? Why we will not store?

27:59

because it will be useless. Why it will be useless? Because let's say that if I am storing the data,

28:07

like for example, today let's say that what I need to do is I need to store some data. So I'll just clear this part.

28:15

And we can see this that today let's say I'm going to store iPhone data. So probably it will have features like a model.

28:22

Then it will have camera. Then it will have RAM. Then it will have weight.

28:29

Then it will have battery. And it will have other features, right? So you will see this, that these kind of features will be there. And probably I can write, let's say if I'm having iPhone 17, so I can write that particular part. Then I can write it has a 48 megapixel camera. It has like 16GB RAM. It has like 1.5 kilogram weight and it has like 4,500 MH battery.

28:54

But let's say if I want to get a washing machine on Amazon, then do you think it is making any?

28:59

sense to store washing machine here. Like, will washing machine has features like camera,

29:05

RAM, battery, weight can be there, but you will see all other features will not be there. So if I try to

29:13

store them, like if I store here a washing machine, then you will see this that all these camera and

29:18

everything, right? It will be empty for that. It will have other things. Like for example, whether it is a

29:24

top load or a front load washing machine, then how much drainage is there and all other

29:29

things, right? So you will see this that it will not have a camera so it will be empty.

29:34

There will be no RAM. There will be no battery. There will be like it will be front load. But for

29:39

this, it won't exist. So you can see this that currently these products are not related.

29:44

Since they are not related, we will generally try to store them in different tables or we will try

29:50

to use a different kind of database that is there. So whenever the data is related, like for example,

29:55

today if you are working in any particular bank, where you see this, that, the data, the data,

29:59

data is related up. Like here you can see every information that we are having. All the information

30:06

that you try to see is related with one another, like branch, customer, depositor,

30:12

account, loan, everything is related up. That is why this kind of data, we can store in a proper

30:18

relational database and we can maintain the relational database for a bank, which will have everything

30:23

related to the bank part. Is this part clear? This part is everyone able to

30:29

understand.

30:38

Guys, still here, the idea is clear, right?

30:40

What we are trying to discuss.

30:44

So you can see here this particular part, like if we try to go ahead.

30:54

I think the first type of databases that we saw, they are called as relational database.

30:59

see this, that we will try to get the data with the help of SQL. Today in the class,

31:04

we will get started with SQL also. So even if you are not aware of SQL, I'll teach you SQL

31:09

from scratch. So currently, you don't have to worry about that. I think the idea is clear,

31:14

right? That whenever we have related data, we will always use relational database and they will

31:20

store the data in form of rows and columns. The next thing is that whenever we need to do some

31:25

like in AI, whenever we need to do structured training, like we need to do structure training, like

31:29

for example, if I'm training a model, let's say opus model that is there.

31:33

And I'm having structured data.

31:35

Like let's say I'm training the model for generation of images.

31:38

So I'll have some structured images that are there that using that, I am teaching the model.

31:44

So whenever we have structured data, what we will be using is we will always use relational database.

31:50

Whenever we are logging different outputs that are there, whenever we are storing transaction history,

31:55

generally in banks, universities, in colleges, in colleges, in.

31:59

schools, everywhere you will see whenever we have like quality data, right, where

32:05

root data can be divided into different, different columns and multiple rows can be created

32:10

where they will like store the input of all these columns that are there. Whenever we see this

32:15

kind of a scenario, we will use this relational database. In order to get the data from relational database,

32:21

they will be using a language which is called as SQL. So SQL is nothing but a structured query

32:28

language using which I can find anything from the data. Is this part clear?

32:35

This part are you able to understand?

32:40

Guys, till here, this part is clear?

32:47

Till here, this part is clear. Till here, this part, are you able to understand or not?

32:52

So if I show you other data, like for example, here you can see right, I have created, right, I have created

32:58

here like two tables are created where you can see some employees data is there generally

33:03

in companies also to store employees data we can see this that this kind of table will come up

33:09

in which I can write some program or I can write some basic line of code that basic line of code will

33:15

do something and get the data like currently where we can see this that here if you try to see

33:21

see currently these tables are created I'll show you how to create all these tables and all and all

33:27

the coding part also we will do in the last one hour of the class but i think currently the

33:32

idea is clear that whenever we have data stored in form of rows and columns we can write some code

33:38

we can write some program sql is nothing but a programming language that we can write using which we

33:43

can get the data like for example if i want to print only those people who have salary greater than

33:51

50 000 then i can write some program and after running that program i can see this

33:57

that currently all the employees are seeing right you can see this that currently all the

34:02

employees you are able to see but if i write something let's say i write in this way i'll show you

34:09

and we will study from scratch that how these things you can write down but currently you can see

34:14

that if i write this kind of a program i'm able to see only few people whose salary is greater

34:20

than 50 000 so currently this was the entire data that we were having but if i run some program after

34:27

after which let's i write this program and i run it i can see only those people will

34:31

come who satisfy the program that i have written is that idea clear that what is sql doing

34:37

noopur is this thing clear now right other people also i think everyone is able to understand right

34:44

you can open this kind of a compiler that is there but today i'll show you how to write sql queries

34:50

and we will create like sql tables and everything over suba base as well even that part we will try to do

34:57

i think till here this part is clear right should we go out to the next part

35:05

mouskan we will see how we will print everything tables and all commands also we will discuss

35:14

let's try to go to the next part that we are having the next kind of databases that are there

35:18

they are called as no SQL database whenever we see that the tables they don't have any particular

35:24

relation or there is no relation in the data in those cases we can use these sql database

35:30

that are present in sql database you can see this that like i was talking about this example right

35:36

where we were storing phone and washing machine if you want to store both phone

35:41

and washing machine together into a single place then what you can use you can actually use no

35:47

cql databases like whenever we see there is unrelated data the data is not related to each other in those

35:54

cases we can use what we can use no SQL databases that are there they are of multiple

36:00

times in next class we will see no SQL databases in detail currently we just need to remember

36:05

that whenever we have structured data in those cases we will use structured database whenever we have

36:13

not relational data the data is not related at all like for example you want to store

36:18

washing machine and phone together in those cases we use unrelational database

36:24

is not a good term so that is why we call it as no sequel database as you can see

36:29

this no sequel by the name is given because sql you cannot write over those databases

36:36

SQL you can only write on relational databases that are there is this thing clear

36:43

jason is as same as dictionary only right we have seen that part goreba i shared that sql file

36:49

right i'll share you today all the files that are there don't worry about that i think 10

36:54

here this part is clear right guys still here this part is clear today you will see we

37:00

will be using a super base so we will talk about that as well non-relational database also

37:09

you will see jason format though i think everyone is aware of jason format you remember we saw that

37:15

in past classes as well right like for example let's say if i have this kind of data

37:24

and this kind of data currently is not put very a let me format it

37:32

if i write any data let's say which is in form of key value pair this is nothing but jset format right

37:39

like let's say that you have an iphone and it has multiple features that are there like for example

37:45

this is iphone it has a feature which is let's say it has 816 gb ram that is there it has other

37:52

things like for example it has 48 megapixel camera then there is another thing called

37:58

as washing machine which has other things that are there getting my point so whenever we

38:03

have this data in this kind of a format it is called us what it is called as a jason format is this

38:09

thing clear this kind of data which i am writing it is nothing but jason format

38:15

correct right till here this is good to go you will see this that we will talk

38:27

about these kind of databases later on yeah examples of no sequel database also we will see

38:33

whenever we need to store unstructured data like for example i think everyone might be using

38:39

any social media application like instagram linkedin and these websites right if you need to

38:44

store that how many people are following how many people like for example you follow a lot

38:49

of people as someone follows a lot of people and then we try to see a lot of common things that are

38:55

there in those cases what we can use we can use we can use this no SQL databases that are there right

39:00

is this part clear this part you are able to understand because there will be no relation

39:05

between whom i follow and whom you follow there might be few people like 10 people or 15

39:11

people that might be common or worst case there can be like 50 people or 100 people

39:15

that can be common but after that you can follow like infinite number of people so whenever we need to

39:21

store that who people who person is following in those cases we can use this no SQL databases that are

39:27

there correct we will talk about graphs key value pair jason documents and everything later on

39:34

in the next class currently we don't have to focus on no SQL database currently this is a basic

39:39

definition that i'm telling you later on you will see this that currently the main focus

39:45

today will be relational database we will try to discuss that in scratch once that is done then we

39:50

will go ahead to the other databases that are there basic definition of no SQL is clear to everyone

39:56

right that part are you able to understand guys still here this part is clear is clear

40:09

Whenever we want to find out similarities, Rakesh, we can use SQL database to be honest.

40:17

It depends upon if your data is related or not. If data is related and structured, we will go ahead with SQL database.

40:25

If data is not structured, in those cases we will use no SQL database. That is a main POV.

40:31

Correct, right? Do you remember vector databases? I think I showed you last class all the vector

40:39

databases that are out there right that whenever we want to store big list of numbers

40:44

whenever we are building a rag application whenever we need to store embeddings that are there

40:49

in those cases we can use vector databases that are present so you will see this that whenever we want

40:55

to store a big mathematical expression a big sequence of numbers in those cases we will use these vector

41:01

databases do you remember all the embeddings that i showed you i can again open that project and show that

41:08

part but i think everyone remembers that right guys do you remember that or not

41:14

so i guess if you see here this particular screen whenever we have these big list of numbers that are

41:36

present up right in which you can see this that lot amount of numbers are stored you can see

41:41

later on we will see that even images and videos can be represented in these kind of number listing

41:47

whenever we have this kind of big list of numbers in which a lot of numbers need to be stored we use

41:53

something called as vector databases that are there i think that idea is clear correct you can see

42:00

that even text audio whatever we are converting this is text conversion only right

42:06

mouskan we discussed that in the last example also like if you remember the last class

42:11

that we were talking about can you see this that this is what data this is all english data all this

42:18

english data what i am doing is i am trying to convert it into different different chunks chunks

42:24

means breaking these into our smaller parts once the data is broken into multiple smaller parts i try

42:31

to create these kind of embedding start are there these are not understandable to use

42:35

to humans we won't be able to understand that what these numbers represent but you will

42:40

see this that computer will be able to understand what is the meaning of these numbers and using

42:45

these numbers it can identify that which words are closer like for example if there is a word

42:52

let's say dog and then there is a word which is puppy you will see that the list of the numbers that

42:59

are there right they will be very very close is the idea clear

43:05

is this thing clear or not clear rakash we will see that part right that you cannot

43:15

directly convert all these numbers like if a sentence is there right if you don't break it down

43:20

you cannot convert it into a sequence of numbers we will see this that why these embeddings are

43:25

required and why do we actually create them once we study about rag right correct in rack

43:32

part we will see that when we have to use vector databases and all

43:35

all in rag this is required right in rag but it is required that why vector databases

43:45

and all these things are present up in those cases it is required is that idea clear we will

43:52

talk about rag in the 15th session but i think currently this thing is clear that whenever we

43:57

have list of numbers that are present up in those cases what we can use we can use this

44:03

embedding starter there is the idea clear or not

44:05

clear.

44:07

Rakeh Muskan, what thing is not clear here?

44:12

Let me show you one thing is not clear here.

44:35

Thank you.

45:05

Let me know once you can see the screen.

45:12

You will see this screen.

45:23

You will see this that we will see this particular part later on.

45:28

But I think the idea is clear, right?

45:31

Correct that there are scenarios in which AI needs to understand.

45:35

the meaning of the sentence that which words are closer and which words are not that close.

45:41

In those cases we need to create these kind of embeddings because directly from sentences

45:45

it cannot understand.

45:47

Like for example if you create embeddings of can I work from home and what is a remote work policy,

45:54

automatically you will see since they are having similar meaning right, the embeddings or the list

45:59

of vectors that are there, they will be very very close.

46:02

But if I try to probably have two sentences that can

46:05

I work from home and what hardware new people are requiring?

46:10

In those cases, the sentence mean very different.

46:13

That is why the embeddings, they will be very, very different.

46:16

Is this idea clear?

46:17

So we will understand this, that why computer needs to understand that which words are actually

46:23

close and what is proximity that is there.

46:26

Those things we will talk about later on in the rack class.

46:29

But in order to store this list of big numbers that are there, right?

46:33

Which are called as embeddings, they need to be stored in some.

46:35

properly something called as vector database.

46:38

Is that part clear?

46:41

Till here, this part is clear, right?

46:47

Is the idea clear to everyone?

46:52

Correct, right?

46:57

So we can see this particular part that the next type of data, that also we will see later on.

47:02

Currently, you don't have to worry about because there is no sense.

47:05

such example that I can actually show you unless and until we start building AI agents.

47:10

You will see this, that there are a lot of algorithms or we can say machine learning algorithms.

47:16

Whenever we need to understand that how the data is changing with time.

47:20

Let's say that at this particular time, this thing is happening.

47:24

Like for example, if I give you this scenario, generally you will see that whenever a concert is live,

47:30

let's on book my show or anything, right?

47:33

Then a concert is live.

47:35

a lot of people want to purchase the tickets, and suddenly you will see that the website

47:40

comes down. This thing can be predicted with the help of different machine learning algorithms as

47:45

well as AI agents. In order to predict such anomalies that are there, right? We use something called

47:52

as time series data. We try to, like in case of websites, this thing can be done, that every day

47:59

we can store that how many customers are coming up. And based on that, we can plot that okay at 7 p.m.

48:05

this is a traffic. At 8 p.m., this is a traffic. At this particular time, this is a traffic.

48:10

So you can see these things can be predicted with the help of AI agents and different machine learning

48:14

algorithms. In those cases, what we use, we use time series databases. Another good example of this

48:22

is like, I think probably have you opened Google Maps. In Google Maps search for any particular

48:28

place that is there. Like, for example, search for any gym or let's say,

48:35

any particular restaurant that is there. Let's try searching. I'll just search for AB Callisthenics Academy,

48:45

Banlor. So I'll just search for this particular place. So can you see this? Can you see this?

48:51

That this time data is coming. That at what particular time, like it's busy, it's not that busy. At this

48:59

particular time, it is very much busy. Then here you can see this particular part, right?

49:03

whenever we want to store this kind of data with time, that how much load is there on any particular

49:09

website or let's say at any particular place, I want to find out that how much people are visiting.

49:16

Same way you can search for any restaurant that is there near your place and you will be able to find out

49:22

that how much the data is changing. So whenever we won't need to store this kind of data, what we use

49:28

is, we can use time series database that is there. Is this example also clear?

49:33

Even the screen time in your phones, you can see. And you can search for any restaurant also.

49:40

Like, I don't remember any such restaurant, but let's try.

49:45

I think you got the idea, right?

49:48

Till here, this thing is clear or not clear?

49:53

Time series data also you are able to understand, right?

49:56

Same way in weather cases also, you can see that they are also using time series data in order to do a lot of predictions that are there.

50:03

Correct?

50:10

Guys, still here we are good to go, right?

50:12

All these type of databases are clear.

50:15

So you will see that other databases we will study later on.

50:18

But currently the most today, the main focus will be on relational databases.

50:24

Then we will go to NoSQL database in the next class and the later on classes.

50:30

Then once we complete RAG, then we will study about vector databases.

50:33

databases. And then once, let's say, for different monitoring purposes, when we are building

50:39

AI agents, then we will actually be using time series database. But currently we need to understand

50:45

the first type of database, which is relational database that is there. Is this idea clear?

50:52

This part are, is everyone able to understand?

51:00

Reju, we will discuss that later on. Currently, no one will be able to understand.

51:03

to understand that part. So we will keep that later on. Other people will get confused.

51:09

So currently I think the format is also clear that relational database, they try to store the data

51:15

in form of rows and columns. No SQL databases, they can store data in multiple ways. They can store

51:21

the data in form of key value pair as documents in graph format. In case of social media websites,

51:27

there is a graph that forms. So that part also we will see. Whenever we are storing vector,

51:33

databases, you saw that list of numbers, right? That is nothing but the complete vector.

51:39

And it will be stored in something called as a vector database. Time series database example also

51:44

I showed you that any place, any restraw that you search, with the time they are storing number of

51:50

people that are visiting, anything which is used for monitoring purpose on any other scenario,

51:55

we can use time series data. So you can see this, that in no SQL database, it can happen that

52:00

sometimes I can store the data in JSON format, as you can see in this particular image also.

52:06

Vector database, they will be able to understand that which words are closer. We saw that example that

52:12

if I say that we are working from home and what is a remote work home policy that is there,

52:18

both these sentences are similar. So that is why they will be stored nearby. And if two things,

52:23

they are very, very different, let's say plan a trip to Goa and what is a work from home policy.

52:28

These two sentences are very, very different.

52:30

In those cases, they will be stored far apart.

52:34

And in time series, based on every time, we can manage and store that, how much load is coming,

52:39

how much traffic is coming, how the weather is changing, how this algorithm can predict,

52:44

all these things. For those scenarios, we use time series data, right?

52:49

So timestamp records are generally stored.

52:51

Is this part clear now, Sahil? Other people are you able to understand?

53:00

This thing is clear.

53:00

I think everyone knows all the PPDs are already present here, right? I can share the link of

53:05

this particular PPD also, but I think everyone has the main drive, right, in which all the PPDs are

53:11

present up. Yes, right, we will learn them in detail. Today, the main focus will be on this

53:17

first one, relational database. And then we will talk about one by one other databases that are there.

53:25

I think till here, this part is clear.

53:30

Guys, the meaning of all the four databases are you able to understand?

53:41

Yeah. So let's try to talk about the other things. Like one by one, we will try to understand

53:46

today relational databases. So let's start from that part. You will see this, that database is

53:53

consisted of everything. Today, I'll show you one table, but a database can have multiple tables. The bank

54:00

example that I was sharing, right, where you can see multiple different tables were present,

54:05

and each table was storing different, different information. So whenever we talk about

54:12

database, we need to understand it will not have one table. It will have multiple tables that are

54:18

there. This is a main idea you need to understand. And each table can have different amount of data

54:23

also. Let's see this part. We can open this PPD and we can see this example. Like here you can see that

54:30

I have a branch data which is storing everything related to all the branches. I have a customer

54:36

data which is storing everything related to customer part. I have a depositor data where

54:40

everything related to depositor is stored. I have a loan data and in this thing also something is

54:46

getting stored. If you see this carefully right, all these tables are interlinked also. Let's say if I

54:53

see here borrower table, in borrower table can you see this, that if you want to find out how much loan Adam

55:00

taken. What do you think you can do? What do you think you can do if you want to find out

55:07

Adams, let's say loan amount? Like what do you think will be the loan taken by Adams here,

55:15

L16, where you can find it out? Correct, right? You will take a loan number and you will

55:22

see this, that this column and this columns are same. You will check the loan table. You will search L16

55:27

and you will get here, this is the amount. This process.

55:30

is called as what? This process is called as joining the table. We will see this part

55:35

also that how two tables can be combined up and then they can give us complete information. This

55:42

idea is clear, right? So all these tables, they will be stored inside what? They will be stored

55:47

inside database. So you can consider this that database is complete office. Then all these tables are different

55:54

different floors and each of the row that is stored, it is nothing but each employee that is there. I think

56:00

this example is clear, right? This table, this thing you are able to understand that a database

56:06

can have multiple tables that are there. Is that idea clear?

56:15

Correct, right? So we can see this. Shall we go out to the next part, right? We can see this,

56:21

that each column will be representing what we are storing. I think that idea also is very much clear,

56:27

that each table will be representing one kind of data.

56:30

Like for example, if you saw in that PPD, each table was representing different, different kind of data that can be there.

56:37

So we can say whatever, whenever we are creating any particular table, it will represent what we are storing.

56:45

Then row will be representing one entry.

56:48

Like what if I'm storing employees data, like for example, if I go here, I delete this part and I go to directly tables.

56:56

You can see here this particular part, right?

56:58

that in this table, what it is representing, it is representing employees. Every column is telling me

57:04

about that this is the ID of the employee, this is the name, this is the designation. So columns, they

57:12

represent attributes. Rows they represent what are the different, different entries that are there.

57:19

And the table is a complete structure which is storing the complete information related to all the

57:24

employees. And same way I have here another table, which is the order table.

57:28

In this order table, you can see everything related to different, different order is present up.

57:33

I think this idea is also clear, right?

57:35

That each table will be storing one specific information.

57:40

Is this thing clear, guys?

57:42

Till here, this part you are able to understand.

57:50

Row column and table is clear, right?

57:55

Any doubts anyone is having with row column and table and table is clear, right?

57:58

table part.

58:03

Shall we go to the next part, right?

58:06

Now, there are some other terms that you need to understand.

58:10

The one of the famous term is schema.

58:12

Schema basically tells us that what kind of information is stored in a table.

58:18

I will show you schema as well.

58:20

Then there is something called as primary key.

58:22

Primary key is very, very important and it's very easy to understand.

58:26

The unique value,

58:27

that will help us understand that this row is unique.

58:32

That thing is called as primary key.

58:34

Like, if I just go to this particular table,

58:37

can you tell me that in this table what would be the primary key,

58:41

which can help me understand each row uniquely?

58:44

What do you think will be the primary key for this employee's table?

58:48

The name can be repeated, right?

58:50

There can be two people with the same name.

58:52

The ID will be unique, right?

58:56

Like, for example, you can see.

58:57

Currently, all the names are different, but names can be same also, right?

59:02

Generally, ID, role number, like if I talk about colleges, right, everyone has a unique college.

59:09

In banks, what do you think will be the unique ID that they can use to probably use your thing?

59:16

Customer ID, even bank account number, even Adhar number, it will be different for different, any people, right?

59:23

So anything which is helping us to uniquely identify a row,

59:27

that thing can be primary key, correct, right?

59:31

Like in order stable, what do you think?

59:33

What could be the order ID?

59:35

Like, what could be the primary key?

59:43

Order number, right?

59:45

Because you can see customer ID is repeated, salesman ID is repeated, like,

59:48

3001 is not present, but we can see 3,002 is present up twice, right?

59:54

Same way, salesman ID is also repeated up.

59:57

So only order number will be unique.

1:0:00

Anything that is helping us to do what?

1:0:04

Anything that is helping us to uniquely identify a row is called as a primary key.

1:0:09

Now, let's talk about schema.

1:0:12

After reading the schema, you can tell that what information a table will store.

1:0:18

I'll tell you about this also.

1:0:20

So let's try to read this particular schema and then little by little we will be able to understand.

1:0:25

But you can think that there can be more.

1:0:27

than one primary key in a table also. It can happen that two or three columns can become

1:0:31

a primary key. Even this is possible. Whatever way you want to define, you can define it. You can

1:0:37

keep even one column as a primary key. You can keep like multiple columns as a primary key as well.

1:0:43

I think this idea is clear. Is this particular idea clear to everyone?

1:0:57

is different for different table. In one database, there can be multiple tables and each table

1:1:02

can have a different primary key. Like, for example, if I go to this particular scenario, right,

1:1:07

you can see this that every branch, like the branch name generally will be different or there

1:1:11

will be something called as a branch code. That will be different in case of branches. For every

1:1:17

customer name, there will be a customer ID that will be kept unique. Then for each low number,

1:1:22

the low number will be unique, account number will be unique. And this way, any particular particular

1:1:27

thing that we can have in a table that will make it unique, that thing we can keep.

1:1:31

If let's say that anything is repeated, then we can combine two or three columns also to make a single primary key.

1:1:38

I think even that part is clear.

1:1:40

Till here, this part are you able to understand?

1:1:49

It can be auto allotted also, but generally we will only define it.

1:1:53

Correct, right?

1:1:55

Yeah, schema we will discuss.

1:2:01

We can tell it right that which columns to use as a primary key.

1:2:06

Let's say if I'm defining a table, right, I can say that branch name plus combination of branch city, it is a primary key.

1:2:13

So automatically, if you enter Bridgeton and Brooklyn, right, again, it will fail.

1:2:18

You cannot be able to update it. Primary key means that if you set two columns as a primary key, right, that combination of both

1:2:25

of them will be a primary key. If you try to enter another value with the same thing, it will fail.

1:2:30

Let's say that if I am entering account number as a primary key, only account number.

1:2:34

And if I keep again account number as one zero two, one zero one or one zero two, it will fail.

1:2:39

Is that part clear?

1:2:42

Now Nilema, this thing is clear, right?

1:2:44

Yeah, right, there will be 10 primary key.

1:2:47

Every table can have multiple primary keys, like it can have, it is possible that it can use two or three columns as a primary key.

1:2:54

as a primary key, it can, it is possible that it can use only single primary key,

1:3:00

it is also possible that it can have multiple options of primary key.

1:3:04

All these three points related to primary key are clearly, right?

1:3:12

So you can see here this particular part, let's talk about schema now.

1:3:16

You can see that schema is nothing but a line, using which we can understand primary key column will be unique.

1:3:23

column will be unique. Whatever we are setting as a primary key, it has to be unique.

1:3:27

Like for example, if I say this that primary key is ID, then all the IDs will be unique.

1:3:32

It's impossible that two IDs can be same.

1:3:35

Is the idea clear that every ID will be unique then?

1:3:39

Guys, this thing is clear, right?

1:3:46

Now we can see here this particular part.

1:3:48

The next thing is schema. Like once you read the schema, you can understand everything about it.

1:3:52

everything about a table.

1:3:54

Like schema is a blueprint of our table.

1:3:57

Like if you read this particular line, create table employees.

1:4:01

So what do you think employees is?

1:4:04

Employees is nothing but the table name.

1:4:06

So whenever we are defining schema, right,

1:4:08

we can say this particular thing that after create table, whatever is written,

1:4:13

that is a table name.

1:4:15

Then you can see there is something written as ID and then integer.

1:4:20

What do you think it represents?

1:4:21

It represents that there is a column ID whose data type is integer.

1:4:26

Integer means that it will try to store integer values.

1:4:30

Can you see here in the table that ID is storing integer values?

1:4:34

Same way other data types are also possible.

1:4:37

Like for example, name, it will be in text format.

1:4:40

So that is why you can see first name is written, then text is written.

1:4:44

Is this part clear?

1:4:46

Same way you can see designation is also having data type as text.

1:4:50

Manager has a name.

1:4:51

type in teacher.

1:4:52

So using schema what you can understand?

1:4:54

You can understand two things.

1:4:56

What is a table name?

1:4:58

And what are each columns?

1:5:00

So you can say what are each columns as well as

1:5:05

what is a data type of each column?

1:5:08

Is this thing clear to everyone?

1:5:14

Are you able to understand this or not?

1:5:17

Schema will be used. It can be written to create an entire table with all number of columns.

1:5:26

That part also we will see. Exact command we will be writing.

1:5:29

You will see it will be the, like this kind of exact command we will write and table will be created.

1:5:34

But the current table that will be created will be an empty table.

1:5:37

Correct, right?

1:5:38

After reading the schema, we can understand what are the tables, what is the table that we are creating

1:5:46

table that we are creating, what are the different, different columns in that table?

1:5:50

is that idea.

1:5:51

You can just get an idea of that particular table, Rakesh.

1:5:54

I think this thing is clear, right?

1:5:56

Nilema, the data types in Python and the data types in SQL are different

1:6:02

different.

1:6:03

So you need to understand that SQL is a different programming language.

1:6:07

Python is a different programming language.

1:6:09

Here in string, here for string or English words, we will not write string, right?

1:6:14

Is that idea clear?

1:6:15

Schema will not explain rows.

1:6:18

It only explains about the table and the column that you are creating.

1:6:24

Yes, right, a schema will define that how the data will look

1:6:28

and you will be able to understand that what kind of data will be stored inside each column.

1:6:33

Is this part clear?

1:6:38

Guys, these two keywords are you able to understand?

1:6:43

Primary key and schema is clear, right?

1:6:44

is clear, right?

1:6:45

So you will see this that generally it's recommended that primary key should not be a name

1:6:54

because name of two people can be same.

1:6:56

So you will see this that generally we try to use unique ID like ID, email,

1:7:01

there is something called as UUID also that we can keep, which is a very big ID which we can use

1:7:07

for creating any particular person.

1:7:09

Like for example, if you go to Google.

1:7:14

and you type here UUID generator.

1:7:17

So you can see this that every time I click on this tool,

1:7:20

it will generate UUID, like this kind of big ID that is there, right?

1:7:26

This is called as UUID.

1:7:28

So it can be used as a primary key because it's impossible that two people will get exactly same ID.

1:7:35

Getting my point.

1:7:44

this thing clear?

1:7:57

Let me share the other screen.

1:8:14

part here you can see this right that it can happen that branch name can be same right in a same city two ranches can be there.

1:8:22

So probably in order to keep a primary key, I can assign two columns as a primary key.

1:8:28

Then what will happen is that if you keep branch name and branch city and if you try to enter another value,

1:8:34

like if you could see here, the branch name is Bridgeton and the branch city is Brooklyn.

1:8:39

If you enter another value as Bridgeton and Brooklyn, it will not take it.

1:8:43

it will not take it because combination of them is a primary key, which makes that if you are writing branch name and branch city, together they cannot be repeated.

1:8:52

Is that idea clear? That is how two primary keys can exist in one table.

1:8:57

I think this thing is also clear, right?

1:9:07

Guys, still here the schema primary key row table column, that part is clear, right?

1:9:12

part is clear right now foreign key example to be honest we have already seen like whenever you see that two tables they want to establish some relationship in order to find out a data in those cases we call it as foreign key like a column can be called as foreign key how we can do that

1:9:32

let's go to the same example that we were seeing here can you see here that custom like borrower table and the loan table that is there

1:9:41

they have a similar column which is loan table now if i want to know what is a loan that is taken by adams

1:9:49

then i can see that low number of adams is l16 so i can find out where l16 is present and i can use that

1:9:57

particular part to find out the exact amount that is there is that part clear in one table there can be any

1:10:06

not like generally you will see so low number will be what low number here

1:10:11

will be a foreign key that will be there is that part clear guys this part is everyone

1:10:17

able to understand the column which is helping us to connect from one table to another table

1:10:23

and it is acting as a primary key in the second table that thing will be a foreign key like if you

1:10:29

see here in table number four and in table number six loan number is acting as a primary key in

1:10:37

loan table and loan number is helping body

1:10:41

table to connect with loan table so that is why it is a foreign key because it is helping us to connect

1:10:47

with a loan table and it is acting as a primary key in loan table as well is this thing clear

1:10:54

what is not clear in foreign key foreign key is very very simple whenever we want two tables to be

1:10:59

connected in those cases we can use something called as any column column that is there it can be used

1:11:06

in order to connect it like i'll show you one more example that is there let's talk about that

1:11:11

can you write in chart?

1:11:41

can you tell me that here you can see a lot of tables you can see here customer table and

1:11:47

order table what do you think is a foreign key here then we will add one more column right

1:11:54

we will enter the code of that particular branch that code will act as a primary key is

1:11:59

that part clear purajan guys what do you think is a foreign key in these two tables

1:12:11

customer ID right example is clearly shown you can see this that

1:12:20

yeah i am having a customer table in this particular customer table what is happening we can

1:12:25

see this that here multiple rows and columns are written there is customer ID first name last

1:12:32

name age country you can see in orders table also same thing is present order ID item amount and

1:12:39

customer ID item amount and customer ID so you can

1:12:41

can see this customer ID same in both the tables right if i want to find out john

1:12:45

ordered what i can find out okay customer ID is one one is present here in keyboard so that

1:12:51

means john ordered a keyboard which is having amount as 400 so we can see this customer

1:12:56

ID is a foreign key right because it is helping me to connect customer table with other other table

1:13:03

and yeah that thing we are able to do i think the idea is clear right

1:13:11

Any column which is helping us to connect one table to another table that will be repeated inside both the table that will be foreign key.

1:13:22

Column will be a foreign key, Nytesh. So you will see low number will be the foreign key, right?

1:13:29

What do you think our primary key is in customer table? What is the primary key in customer table?

1:13:38

It is customer ID, right?

1:13:41

What is a primary key in order table?

1:13:48

Order ID?

1:13:49

What is a foreign key here?

1:13:57

Yes, right, Shlok, they can be same, right?

1:14:04

Customer ID is the foreign key, right?

1:14:08

I think this example is clear, right?

1:14:10

Anyone who is not able to.

1:14:11

to understand this example. This example is clear or not?

1:14:22

Here, if you try to see this particular part, like, what do you think in borrower table and known table, what is a prime foreign key?

1:14:41

number 3 and 5.

1:14:48

Word is up foreign key in table number 3 and 5.

1:14:52

Account number, right?

1:15:01

Correct, I think this idea is also clear.

1:15:06

Now, you can see right, foreign key can be repeated.

1:15:09

I think, like, I'm not.

1:15:10

like I'm not very sure that if who asks that question, probably let me see.

1:15:15

Arvind, right? Like, you can clearly see, right, that which key has to be unique?

1:15:24

In customer table, what is a primary key, customer ID?

1:15:29

In order table, what is a primary key, order ID? But here customer key can be repeated, right?

1:15:35

Like you can see customer ID is repeated because John has placed two orders.

1:15:39

placed in two orders. That can happen, right? I think this idea is clear that foreign key can be repeated, but primary key will not repeat.

1:15:47

Primary key in customer table is customer ID which is not repeated.

1:15:51

Order ID in order table is a primary key which is not repeated. I think this idea is clear, right?

1:15:57

Varen, now you are able to understand.

1:16:09

I think till here, this part is clear, right?

1:16:17

till here are we good to go? Call me, we will discuss about that later on.

1:16:21

Currently let's focus till here only, right?

1:16:24

Till here, this part is clear or not clear?

1:16:27

Here also you can see this, right?

1:16:30

That if I have a student table and a marks table, then I can see that we have one column here student ID.

1:16:37

And here I have another.

1:16:38

again another column which is student ID. So student ID is helping me to connect students with their marks.

1:16:45

So what will be the foreign key? It will be student ID. I think that example is also clear, right?

1:16:51

Correct till here, this part is clear, right?

1:17:00

Now there is something called as constraints that are given and there are some data types also.

1:17:07

So first let's study about data types because that is very, very easy.

1:17:11

Do you remember data types in Python? What are the data types in Python that we studied?

1:17:20

Correct, right? We studied about something called as string.

1:17:25

Then we studied about integer. We studied about float. We studied about bull.

1:17:29

We studied about string. All these data types, right.

1:17:33

Same way.

1:17:36

In SQL also there are a lot of data types.

1:17:40

There are different different versions of data types that are there.

1:17:43

The first type of data type is integer data type in which normal numbers we can store.

1:17:48

Then whenever we have decimal number, we can either use float or we can use decimal.

1:17:54

Generally, since you remember float, so we will always try to use float that is there.

1:17:59

Now whenever we want to store text up to a specific limit.

1:18:03

Like if you remember that Adahar card and password,

1:18:06

PAN card, right?

1:18:07

Like a Dahaar card for everyone, it is having a limit.

1:18:10

That it will be of 12 letter only.

1:18:12

PAN card, it is generally of 8 letter or 9 letter.

1:18:16

Correct?

1:18:17

So you can see this that.

1:18:18

Whenever we want to store text which is having fixed length,

1:18:22

in those cases we can use something called as VARCAR.

1:18:25

Whenever you don't know length, you can use text data type that is there.

1:18:30

Whenever you want to store true or false as same as Boolean,

1:18:34

like in SQL we call it as Boolean.

1:18:35

we call it as Boolean. In Python, we write Boole, right? Same whenever you want to store true or false, we can use Boolean.

1:18:43

Then whenever you want to store time, you can either store it in date format. Like date means, like today is like, I think, 11th May.

1:18:51

So we can see here this particular part that whenever I want to store date and I want to store it in this kind of format, like 1105-2026.

1:19:00

This is date format. If I want to store it,

1:19:05

the time, let's say time is 20108, then whatever seconds will be there.

1:19:12

This kind of time if I'm storing, then it can be stored in,

1:19:16

like along with the date, it can be stored in timestamp format.

1:19:20

Sometimes I showed you, right, that for primary key, if I want to store such a big ID that is there.

1:19:25

For this big IDs, we can use, like if I'm having this kind of big ID, right,

1:19:31

which has numbers also, it has alphabets also, it has.

1:19:34

So it has like hyphons also.

1:19:36

I can either store it in text format or like since this is like in a lot of real companies,

1:19:43

UUID is used as a primary key so that each customer can be uniquely stored and identified.

1:19:49

They assign such a big number because they are having like a lot of customers that are there.

1:19:54

In those cases, we try to store the primary key in UUID format also.

1:19:59

So that is a specific data type which SQL is having.

1:20:03

But currently the first six data types that you are seeing, they are very, very important.

1:20:10

The first data type, which is this one, integer, which will store normal numbers.

1:20:14

Then there is float, which will store decimal numbers.

1:20:17

In Warecare, we can store text up to a specific limit.

1:20:21

In text format, whatever English words, sentence, letter we want to store right, we can directly store it.

1:20:27

And generally it is used for big paragraphs.

1:20:30

In Amazon, whenever you need to write, feedbacks, right?

1:20:33

Or in Uber, you are writing any particular feedback.

1:20:36

Then generally, whenever we need to store large amount of big text that is there, which is more than like 2,000 letters,

1:20:42

in those cases we can use textual data type.

1:20:45

Whenever you want to store true or false, you can go ahead with bullion data type.

1:20:49

Whenever we want to store just the date, we can use date data type.

1:20:53

Whenever we want to store both date and time, we can use timestamp format.

1:20:57

Whenever we want to store that UUID for primary key, in those cases, we can keep the data type.

1:21:03

as UUID.

1:21:04

I think this example is also clear, right?

1:21:07

Till here, this part are you able to understand?

1:21:10

Where current text can have both numbers as well as text.

1:21:22

It can have both numbers and text, right?

1:21:25

No right, Muskan, that is incorrect.

1:21:29

Foreign key can have duplicate value, primary.

1:21:33

primary key will not have duplicate value.

1:21:35

Primary key in one table, it will never repeat, but foreign key can repeat, and we have already

1:21:41

seen that particular example.

1:21:42

Because the same person can place multiple orders, right?

1:21:45

Did you saw that example?

1:21:47

Do you remember that?

1:21:50

Correct, right?

1:21:50

So the idea is clear, right?

1:21:52

That foreign key can be repeated.

1:21:53

In one table where it is acting as a foreign key, that can repeat.

1:21:57

But in the main table where it is primary key, there it will not repeat.

1:22:00

So that part is also clear, right?

1:22:03

Like if we see this particular example again, I think everyone can see this particular part.

1:22:11

So you can see here this thing, right?

1:22:13

That customer ID is a primary key here.

1:22:15

Is it repeating here?

1:22:16

No.

1:22:17

But here it is a foreign key.

1:22:19

That is why it can repeat.

1:22:21

Is that part clear?

1:22:22

Here order ID is what?

1:22:24

Order ID is primary key.

1:22:28

So it will not repeat.

1:22:29

If I talk about shipping table and I talk about customer.

1:22:33

table. How do you think like which is a foreign key here? Can you tell me that?

1:22:39

What do you think like in customer table and in shipping table? What do you think is a

1:22:47

foreign key?

1:22:51

This customer is a foreign key, right? Because you can see that I can find out whether their orders

1:22:57

have been shipped or not, correct?

1:23:01

I think this thing is also.

1:23:02

this thing is also clear. Till here, are we good to go?

1:23:14

Yes, right, Muscan, I think that thing is clear.

1:23:19

Data types also you are able to understand, right? Data types part is clear.

1:23:32

Yeah.

1:23:34

It will not be said, right?

1:23:37

If you try to update for primary key as duplicate value, then automatically it will not take.

1:23:43

Like let's say that by mistake you said, name as a primary key, then all the names in your table have to be unique.

1:23:49

If you need to enter two names same, then it's not possible.

1:23:53

Table will not take it.

1:23:54

It will deny that.

1:23:56

Correct?

1:24:00

Is this part clear, right?

1:24:01

Till here.

1:24:02

Are we good to go?

1:24:03

While creating a table, we need to specify that which column is a primary key?

1:24:11

That we will do.

1:24:13

Yes, right. Creating UUID is very easy.

1:24:17

Is this thing clear?

1:24:23

Till here, are we good to go?

1:24:32

UUID is nothing but a big ID that can be used to represent a lot of customers.

1:24:49

Like today on Amazon, you know right, 100 million orders are getting placed.

1:24:54

Every order has a unique key.

1:24:56

So what we can do is we can have a very big ID for each order, right, internally to store it.

1:25:01

Like I can have a very big ID for each order, right?

1:25:02

have a very big ID that will actually store what is order. So this kind of ID is good enough,

1:25:07

right? If you want a bigger ID than this, then you can probably create a 7 version ID, which will

1:25:13

be every time it will have a lot more connectors. So every time it will be unique. This part,

1:25:18

are you able to understand? Are you able to understand this particular part that in order to store

1:25:26

unique values, like 100 million orders that are there? I cannot keep 1, 2, 3, 4, 5, 6 that way, right? I

1:25:32

We need to keep unique IDs. So this kind of big IDs we can keep.

1:25:36

Is the idea clear?

1:25:41

UUID now you are able to understand?

1:25:43

URAGEN is this part clear or not clear?

1:25:51

Guys, other people are you able to understand or not?

1:25:55

Yes, right? UUIDs are very easy to generate, but they also?

1:26:01

but they only help us to store unique IDs. Like if I have like more than 1 billion customers,

1:26:07

in those cases I can use these IDs in order to like give each customer a unique value.

1:26:16

Now constraints are nothing but different, different rules that are there. So one by one,

1:26:21

let's try to see all the rules that we are having. So we can say this that currently if you try

1:26:27

to see here this particular part, the first thing that we are having is,

1:26:31

that if I keep a rule like not null, this means that all the columns, they will always have a value.

1:26:38

It will not happen that columns, they don't have a value.

1:26:41

Like, for example, if I go here, probably on this particular part, if you try to see,

1:26:49

let's see this particular table. So can you see here, like there is this commission column.

1:26:56

Can you see a lot of columns on this commission column, they are having empty?

1:27:01

they are having just a dash.

1:27:03

So currently this means that no rule is set on this particular table or no rule is set on this particular column, which is commissioned.

1:27:10

If a rule is set, that means if a rule is something like not null, this means that this particular column will not be null.

1:27:19

Correct, right?

1:27:21

Is this part clear?

1:27:22

Because it's not easy to store all the numbers, right? Gotham.

1:27:26

We will see that part later on that how it will work.

1:27:28

I think that idea is clear, right?

1:27:31

Guys, this rule part, are you able to understand that if I keep some rule, like for example, if I keep this kind of a rule, that the commission will not be null, then none of the value will be missing.

1:27:46

You will see all the values will completely exist.

1:27:49

So there are multiple rules that I can set.

1:27:52

One by one, we can quickly discuss all the rules that are existing.

1:27:56

Like, sometimes you will see that even if we don't refine any rule, right?

1:28:01

then also things work.

1:28:02

But if I want, if I keep, let's say, not null, then that particular column must have a value.

1:28:08

It cannot have an empty data.

1:28:10

Then if I keep any column as unique, that means that all the value of that particular part has to be unique.

1:28:16

If you keep primary key, then automatically that column will not be null.

1:28:21

And it will be unique also.

1:28:23

So it will be just a combination of both of them.

1:28:26

Foreign key, if you are keeping any particular column foreign key, that means that column,

1:28:29

that column should exist in some other table where it is primary key.

1:28:34

Like for example, if you are defining this kind of a table, right?

1:28:38

Like for example, if I'm defining this order table that is there,

1:28:42

then I can keep this customer ID as a foreign key.

1:28:45

So automatically it will access that, okay.

1:28:48

This particular customer, it should be present somewhere here.

1:28:51

Is this idea clear?

1:28:55

This part are you able to understand?

1:28:59

Generally, you will see we can keep default also.

1:29:09

Default basically means that if you don't fill any particular value of a column, whatever default value you set, it will be set.

1:29:16

Like, for example, in this particular table, I could have said this particular part that if, let's say no one is entering the commission, then I can set default value as zero.

1:29:26

So automatically, this particular value will be filled with.

1:29:29

zero data that is there.

1:29:31

Apart from that, if you want to check any condition, let's say that if you are taking any entry

1:29:37

in which it requires that age should be greater than 18, then let's say that you try to enter an entry

1:29:43

where age is not greater than 18, that automatically that row will not get updated.

1:29:49

It will fail that particular check.

1:29:51

So different, different basic checks we can keep.

1:29:54

Like for example, I can keep a check of age greater than zero because age can never be negative, right?

1:29:59

So these kind of checks can be added on a column so that there is no incorrect data in any particular database.

1:30:06

Like in order to prevent any incorrect data, these kind of checks can be added or these kind of rules can be added.

1:30:13

Not null means that data in that particular column will not be null.

1:30:17

Unique means that that particular column will contain completely unique data.

1:30:22

Primary key is a combination of not null and unique.

1:30:25

Foreign key means that particular column should be present in some other table.

1:30:29

default means it will automatically default to any particular value.

1:30:33

Condition or check will do what it will do is it will check for a specific condition.

1:30:38

That if that row is specifying that particular condition or not.

1:30:42

I think till here the idea is clear, right?

1:30:44

This idea are you able to understand?

1:30:48

Sail, the definition of foreign key says that,

1:30:58

a foreign key says that it should be existing some other table and there where it is existing it should be a primary key.

1:31:04

That is a definition. The vice versa is not true.

1:31:07

You will see this that here in this table we talked about right?

1:31:11

Like customer ID it is a foreign key because it is helping us to connect this table with this table and here it is a primary key.

1:31:20

Only this much is a requirement.

1:31:22

When we create a table there we can apply any particular constraint Burajan.

1:31:27

Burajan. So you will see this that once later on, once we set up the super base and all right,

1:31:32

you will see this that I will be writing basic operations on creation of database.

1:31:37

So at that particular time, I will be specifying all these constraints that are there.

1:31:43

Is that part clear?

1:31:47

Till here, this thing is clear, right?

1:31:50

Yes, right, so it's possible.

1:31:53

Default can be any particular text also Gotham.

1:31:56

also got them. So it can be anything, like any name, anything that you want, it can be a default value.

1:32:02

Till here the theoretical part is clear, right? Till here, whatever we discuss is that part clear.

1:32:12

Yeah, so we can take a short break and then we can talk about the next scenario. You will see whatever we have understood, right?

1:32:18

We will try to write the SQL queries and all, so that particular part only we will try to do.

1:32:24

One by one we will try to do.

1:32:25

will try to do. So yeah, that part we can see. Till here, whatever we discuss is clear to everyone, right?

1:32:33

Till here, this part is clear. So you will see now we will try to implement everything. Whatever we have

1:32:39

seen, we will try to implement that. So same way as the last class, we can keep a eight minutes break that is there.

1:32:46

And then we can start with the next scenario.

1:32:55

Shlogue, it depends upon whether we are connecting those two tables or not, right?

1:33:06

If we don't connect those two tables, then it won't generate error.

1:33:09

If you connect them and then they're using the same foreign key, then it will throw error.

1:33:13

You won't be able to do it.

1:33:15

So automatically you will see that if you try to do anything like that, right?

1:33:19

It will fail, so you can change that right.

1:33:21

And why you will create same primary key for two tables? Why?

1:33:25

will you do that if you have two same primary keys for two tables you will

1:33:30

store the data in the same table only right why you will create two different

1:33:34

table getting my point it will be completely useless right i think this thing is clear

1:33:42

right yeah so yeah we can start a break and then other things we can see

1:33:47

after the break we will try to implement everything that we have seen right

1:34:17

Thank you.

1:34:47

Thank you.

1:35:17

Thank you.

1:35:47

Thank you.

1:36:17

Thank you

1:36:47

Thank you

1:37:17

Thank you

1:37:47

Thank you

1:38:17

Thank you

1:38:47

Thank you

1:39:17

Thank you

1:39:47

Thank you

1:40:17

Thank you

1:40:47

Thank you

1:41:17

Thank you

1:41:47

yeah guys so we can start with the next part are you able to hear me and then you can see me as well right

1:42:17

let's start with the next part you will see this that what we will try to do is we will try to use this particular tool which is super base and one by one we will try to discuss so if you want like we will see this that for every like thing that we are discussing in class we will try to use this super base database that is present up and we will talk everything related to that but if you want you can even use something called as a mySQL traditional database that is out there if you want you can install it

1:42:47

like by following any particular youtube video and you can do that but you will see this that currently

1:42:53

we will try to create and every we will try to work with suba base in browser only so that we don't

1:43:00

have to install everything and same thing whatever we are doing in mySQL can be done in suba base as well

1:43:06

so on by one let's try to discuss that so i think everyone is upright so can you guys open this

1:43:12

particular website that is there i'll just increase the size of this as well

1:43:17

So let's try one by one we can see.

1:43:21

Are you able to open this particular website which is suburbase.com?

1:43:27

And what we can do is we can click on this particular thing which is start your project and you can create your account with GitHub.

1:43:35

Is everyone having GitHub account?

1:43:37

Guys are you having GitHub account? I think everyone is having GitHub account right?

1:43:43

So you can see this that your organization.

1:43:46

your organization and whatever you want you can enter that i'll just enter my name and we will

1:43:52

choose a free plan and yeah i think we can even click on company's account but yeah let's try we

1:43:58

can create a basic account that is there yeah i think everyone can create account can you create

1:44:07

right now can you open this particular website suba base click on start your project sign in with get

1:44:16

up can you do the first three steps that are there let me know once you

1:44:22

have done that are you able to do it so you might see something like the screen right

1:44:33

you can create a project also like creating a project also is very very easy you can give it any

1:44:39

particular name like this is a region that you can give i am sharing the steps also so that everyone can

1:44:45

follow from chart as well you can create a new project you can enter any password

1:44:50

whatever password you want you can enter that and you can select the region as as asia pacific

1:44:55

only will work if you want you can even select singapore and everything asia pacific will work

1:45:01

you can leave it as it is and you can just click on create a project so you can enter a

1:45:05

password that you will remember so i'll enter any password that is there

1:45:15

you can click on new project that is there is everyone able to create a new like are you

1:45:24

able to create a password and all i think project everyone has created right now once you see a

1:45:38

green status are you able to see i think here you can see this green status right status is unhealthy

1:45:45

let it let me connect uh why it is unhealthy let me refresh it

1:45:53

let me refresh it let it like load the database

1:46:01

yeah i think it is applying migration it will take some time but i think it's

1:46:10

green only so we are good to go no such error or warning is there so we are good to go so we are good to go

1:46:15

so yeah free of post free plan you need to select right i'm not sure why did you select

1:46:21

any paid plan i told to select free plan it won't ask for money and all once you are able to do

1:46:29

it you can see a dashboard will appear like this kind of dashboard will come up for you where you can

1:46:34

write SQL queries and all so you can see on your left part right here table editor will be there

1:46:41

SQL editor will be there are you able to see that

1:46:45

is everyone able to do this this is a you can see this is a database management system

1:46:57

abinash where what we can do is we can actually create real tables and we can practice sq so you

1:47:04

will see this that we can actually create real tables here i will share you the necessary commands

1:47:09

using which tables you can create and then we can start learning sql today we will try to learn

1:47:15

basic sql but with time in the next class we will learn advanced as well that is there

1:47:20

is that part clear till here this part is clear anyone everyone is able to do first three

1:47:30

steps anyone who is stuck i have shared the all the three steps also in the chat

1:47:36

are you able to do first three steps

1:47:39

Where are you stuck at Prati?

1:47:47

Here very basic steps are there right you need to open a website, start your page, sign in with GitHub

1:47:56

and click on new project even if the status is unhealthy don't worry it will work

1:48:01

you need to enter the password select any particular region and wait 60 seconds right

1:48:14

correct right is everyone able to do

1:48:23

i think yeah basic setup everyone is able to do

1:48:28

company type you need personally you can select

1:48:31

it won't enter company and all personally you can select sign in with get up you have to do i also

1:48:40

signed it with get up only

1:48:46

ragesh what are you doing just sign in with get up automatically it will click on authorize

1:48:56

you will again come back to super base link only

1:49:01

So I think everyone can see a lot of places and a lot of things are there one by one

1:49:08

whenever we are able to see like you will see that first do we need to understand what is our

1:49:15

table editor and SQL editor in tables editor we will try to create different

1:49:19

different tables in SQL editor we will write SQL queries to fetch the data so we will be

1:49:24

using it for practice purposes only correct organization you don't have to enter just

1:49:30

create a personal account that is

1:49:31

there correct the status does not matter be it healthy or not healthy

1:49:37

automatically it will work you don't have to worry about that

1:49:46

Pratik are you able to create it just create a personal account right just click on

1:49:50

personal there organization also you are doing just enter your name automatically it will

1:49:55

work that also does not matter no you don't have to click on that shan

1:50:01

No, we don't have to correct it.

1:50:08

Call me we don't have to do.

1:50:10

I showed the simple steps that are there, right?

1:50:13

We don't have to do that.

1:50:15

Currently we only have to use the first two things.

1:50:17

Is everyone able to see SQL Editor there?

1:50:20

Can you open SQL Editor?

1:50:26

You don't have to enable automatic RLS.

1:50:30

You don't have to enable automatic RLS.

1:50:31

We don't have to do that.

1:50:33

I have also connected with Asia region only.

1:50:36

You can connect with Asia region, no issue.

1:50:38

We don't have to select the third option of automatic RLS.

1:50:43

Correct, right?

1:50:45

So you can see this that different different queries we will try to enter.

1:50:49

So probably this kind of query you can, I'm not sure.

1:50:53

Are you able to copy paste from the Zoom chat?

1:50:56

Or probably you can open PPD, open the 21st slide that is there.

1:51:00

is there and any region that you want, I'll do that. Don't worry about that. So you can open the 21st

1:51:08

slide and then from PPD you can copy. Even I can share you the Google Doc that is there. From

1:51:13

there you can copy paste. But just try to run this kind of a query that is there. And we can like

1:51:23

currently security and is not a big issue. So we will just select run without RLS. Because security

1:51:29

and everything is not a big issue.

1:51:30

big issue. We are just creating a student database. So you can see you need to paste it in SQL editor. Can you paste it in SQL editor?

1:51:38

Once you paste it, are you able to see this success? No rows returned?

1:51:47

Is everyone able to do this?

1:51:51

I can create a doc also in which I can paste SQL query. So this is a first query that we are writing. By this query, what we are writing.

1:51:59

this query what we are trying to do we are trying to create a table so are you able to

1:52:07

understand this query like meaning we will understand later on you don't have to worry about

1:52:11

meaning today but i think basic operation you are able to do it right

1:52:18

you can copy paste from this doc also if you are not able to copy based there you need to copy

1:52:24

paste whatever i have written here this part you need to copy paste and i've bolded also

1:52:29

I am sharing the link as well.

1:52:34

You need to click on run without RLS.

1:52:38

I showed you just now right run without RLS.

1:52:42

And you can see this that success message is coming up. So if you see here, right,

1:52:46

your student database is created here. Correct, right?

1:52:50

No rows will come up because currently the database is empty. But can you see automatically

1:52:55

that if you go to table editor now, like if you click on

1:52:59

table editor there you can see this right that different different columns are created up and

1:53:05

currently there is no row now if you go to the second query that i've written i'll paste this second

1:53:11

query also i am pasting on this google doc so if you want you can directly open the google doc that i've

1:53:18

just shared in the chat and you can see this is a second query by writing this query what i can do is

1:53:25

i can insert different different elements i can insert different

1:53:30

different rows like for example if i go to sqel editor and i delete it and i just click on run

1:53:37

so you will see it will run and you can see it's again success first see what i am doing then do

1:53:44

it and if you go to table editor just click on refresh

1:53:55

i think this currently is working very slow by fail refresh yeah so we can see right

1:54:07

one row is if it fails you guys can also do this like just refresh that is a platform issue not

1:54:14

our issue but we can see right one row will get added up if i want to add multiple rows then i can do

1:54:20

that i can copy paste this particular command and i can go to my sql editor

1:54:25

i can paste this particular part and i can run this so once i run this you will see two

1:54:30

more rows will get added up so if i just again refresh here like here also refresh table

1:54:36

is button is there right just press this refresh table button and you can see that automatically

1:54:41

these people are editing up once you run the second query right then only you will be able to see

1:54:48

this kind of data did you run that i think if you run only the first query the table will be empty

1:54:55

this is the first query is for creating a table the second query is for inserting the data

1:55:02

that part are you able to understand you need to run on the sql editor are you able to

1:55:17

click on refresh right you need to click on refresh that is there once you click on

1:55:25

as you can see my screen for see my screen once you run the sql query click on run and

1:55:33

once you run that then click on refresh how many people are able to do it can you write in chat

1:55:38

i think shan has done it other people armor has done it shibhu has done it shill has done it a lot

1:55:47

of people have done it right this is the second query you can open the dock

1:55:55

the dock.

1:55:56

Varen you need to delete the previous query and then do it right.

1:56:05

You are running again and again.

1:56:07

You have to delete and first see right what I am doing.

1:56:12

Paste only this much part or copy this entire thing.

1:56:18

Delete the entire thing and then paste it and then run it.

1:56:21

That thing you need to do.

1:56:24

Getting this very now.

1:56:25

what you exactly need to do.

1:56:27

Till here this part is clear, right?

1:56:33

Guys, are you able to see the data?

1:56:35

Is the data coming up for everyone?

1:56:37

So you can see this, right?

1:56:39

A lot of data is there.

1:56:41

What is the error Nilema you are having?

1:56:44

Our table you are able to create?

1:56:52

How many people are able to create?

1:56:54

How many people are able to create the data?

1:56:55

like create the table first of all.

1:56:57

Coming right, Abinash now.

1:56:59

It will come in some time.

1:57:01

If you are Asia region is there right,

1:57:03

it takes like one minutes to get the data from Asia.

1:57:06

So it will take some time.

1:57:08

Nilema, what exactly you are not able to do?

1:57:12

Because Sonia you have already ran that.

1:57:17

Did you read that error what it is saying?

1:57:20

Duplicate key error is coming because you are running it again and again.

1:57:24

First, run the error.

1:57:25

Now, if you have already inserted this row right, you cannot insert it again.

1:57:30

So what do you need to do, you need to run this part in another query.

1:57:34

That part you are able to understand.

1:57:41

Follow me, you have to clear the above table, first of all.

1:57:45

Like, you need to clear the previous query that you are writing.

1:57:49

I think everyone saw that part, right?

1:57:51

That what did I do?

1:57:52

Like, first I deleted the entire query.

1:57:54

Like, you cannot.

1:57:55

not write something like this.

1:57:57

That if you do first you create a table and then you just copy paste this entire thing,

1:58:04

then it will not work, right?

1:58:06

You will see this that this particular part will not work because if I run it,

1:58:11

it will directly say that table is already created because you have to delete this part, right?

1:58:16

The first thing is to create the data, like to create the table that is there.

1:58:20

So we need to delete that part.

1:58:22

Once we delete that part, then you can run this part.

1:58:24

then you can run this particular part that is there.

1:58:26

Or you can run this entire thing in one go.

1:58:29

Correct, right?

1:58:31

Refresh your table editor.

1:58:33

Do a hard refresh with Control Shift R.

1:58:37

If you do with Control Shift R,

1:58:39

automatically you will see the table.

1:58:41

It will be there.

1:58:42

In table you can see here, in search table it will be coming up.

1:58:50

Rakeesh Patil we saw that, right?

1:58:53

That you need to enter.

1:58:54

a query in SQL editor. Once you enter a query in SQL editor, then only it will be able to,

1:59:00

you will be able to see the data in table editor part. Is that part clear?

1:59:07

Till here, this part is everyone able to understand? Run without RLS only you have to do.

1:59:24

on.

1:59:26

SQL editor we talked about, right?

1:59:28

That SQL editor is nothing but

1:59:32

if you need to write any particular query,

1:59:36

from which you need to do any particular program,

1:59:39

then in those cases what we can do is we can type anything in SQL editor

1:59:43

and it will run that query for us.

1:59:45

In table editors, everything that is there in the table, that part we can see.

1:59:50

So Rakesh refresh the page that is there, right?

1:59:53

If you take,

1:59:54

table is not there, press control shift R and reload the page. That is what I'm asking you to do.

2:0:03

Is that part clear?

2:0:24

What is not coming, Rakesh?

2:0:26

What is the error that is coming?

2:0:28

Table is not coming.

2:0:29

Did you run that query?

2:0:30

Did you run this query and after that did you saw that success message?

2:0:34

Did you do that?

2:0:36

After that did success message come up?

2:0:52

Did you refresh?

2:1:04

I think everyone is able to see the student data that is there, right?

2:1:09

Correct student data everyone is able to see.

2:1:12

So if you see that the first query that we are writing, right?

2:1:16

This first query, what we are trying to do, you need to click it, run without RL.

2:1:22

Rakesh, that thing you need to do.

2:1:24

How many times I told?

2:1:26

Run without RLS, just click on that.

2:1:33

So we can see here this particular part, right?

2:1:36

That if you see this kind of query that is there,

2:1:39

like this is a query that we are having.

2:1:41

In this query, it's a security level that is there

2:1:45

that we don't have to keep the data encrypted as of now

2:1:48

because this is temporary data, right?

2:1:50

No encryption, no level of security.

2:1:51

no level of security is required.

2:1:53

Later on, we will see how to work with encrypted data and all.

2:1:56

Correct, right?

2:1:57

So if you copy paste properly, you will not see any syntax error part, to be honest.

2:2:02

So I think everyone has run this query.

2:2:05

So are you able to understand what this query is trying to do?

2:2:09

Like, what do you think is a table name here?

2:2:12

From this query, what do you think is a table name?

2:2:14

correct? We can see the table name is students.

2:2:23

And then you can see there are different, different columns that are there.

2:2:27

The column is student ID, full name, email,

2:2:31

course, city, enrollment date.

2:2:34

These are different, different columns.

2:2:36

Each column is having some rules.

2:2:38

Like this has a rule which is primary key.

2:2:41

This has a rule that it is not null.

2:2:43

This has a rule.

2:2:44

that it should be unique.

2:2:46

This has a rule.

2:2:47

It is not null.

2:2:48

This does not have any rule.

2:2:50

This has that default is current date.

2:2:52

Automatically current date will set up.

2:2:54

So different rules are set up.

2:2:56

This is set with serial.

2:2:58

Serial basically means that automatically serial numbers will be assigned.

2:3:02

Like 1, 2, 3, 4, 5, 6, they will automatically come.

2:3:05

This query you are able to understand.

2:3:07

That primary key, it has a rule that it will automatically increment by itself.

2:3:12

So as you generate,

2:3:13

you generate all the values automatically serial numbers will be given.

2:3:17

Is this idea clear?

2:3:19

So that is why once you try to insert the data,

2:3:22

like for example that if you try to insert this particular data that is there,

2:3:27

then what will happen?

2:3:29

Like if I insert this kind of data, like full name is Ananya,

2:3:33

this is the email, this is the course and city,

2:3:36

so automatically you will see this that,

2:3:39

primary key will automatically be added.

2:3:41

That will be one.

2:3:42

And the name.

2:3:43

will be what? The name will be Annamia Sharma, email, course and everything.

2:3:47

Now you need to understand this particular thing.

2:3:50

That if let's say you have ran this particular part,

2:3:54

then you again run it, then it will fail. Why it is failing?

2:3:58

Like you need to understand some logical part, right?

2:4:01

That if I run it again, then it will fail with duplicate key error that is there.

2:4:06

Because same name cannot be duplicated again.

2:4:10

That is why what you need to do is you need to do is you need to copy.

2:4:12

do is you need to copy only this much part that is present up and then you need to run that particular part.

2:4:18

Is this idea clear?

2:4:22

This thing are you able to understand?

2:4:24

So Rakesh, are you able to understand now that why this duplicate error is coming?

2:4:28

Because you have to run the multiple row part. You have already ran that.

2:4:32

That part is clear, right?

2:4:34

guys other people are you able to understand this thing the create command is clear right

2:4:49

guys create command are you able to get

2:4:56

email there is a constraint on email there is a constraint on email email

2:5:00

cannot be unique the name can be have to one and yeah right but email cannot

2:5:04

be email you can see right email is unique so if you enter the same email then it will fail that is the scenario that email has to be unique getting the idea now

2:5:14

now

2:5:20

nupur only email we have kept unique right other things we have not kept unique that but are you able to see only unique is written only student idea will be unique and email

2:5:34

will be unique other things can be repeated right full name code

2:5:38

city all these things can be unique correct i think this thing is clear right

2:5:46

oh there is no noise from my end my voice is clearly audible

2:5:56

you can correct it via this particular part that if you try to actually run this thing right you can

2:6:02

first run this part then you run this part you don't have to run this part again

2:6:07

and again i think that idea is clear right nillima only one column even if both are

2:6:15

unique we can keep only one column as primary key we are keeping student ID as

2:6:19

primary key here right so can you see this part that what this query is saying this query is

2:6:25

saying that create a table students the column will be student ID full name email

2:6:31

course city enrollment date and is active then we can see different different

2:6:35

rules we have written that are primary key student ID if you want primary key as email

2:6:41

you could have changed that then two rules are given that they will never be

2:6:44

null the email will always be unique the course will always be not null city can be

2:6:50

anything enrollment date by default will be today's date if you don't enter is active is

2:6:56

by default entered as true is this part clear is this query clear to everyone how I

2:7:01

have written that date is also written in a single row only style

2:7:10

here in the table if you try to see this particular part here in single row only it has written right

2:7:18

yeah right gotham if i want we can do that

2:7:22

till here this part is clear right if you ran it together then you will see

2:7:33

three entries right why are you running again and again Nilima are you able to see three entries

2:7:38

or not guys this part are you able to do that

2:7:52

here i have written current date right if you try to see this particular part

2:8:01

you can see this that this is date and this part i can write it in the same line also not a big

2:8:08

issue if i write it in the same line then also the thing will be same only is this part clear

2:8:14

till here i think everyone is able to understand right

2:8:22

if you are not getting any one entry then you can paste it if you are getting two entries

2:8:28

right just run the an andya sharma line once run only this part

2:8:36

till here this much part is clear right to everyone this part is everyone able to understand

2:8:45

the first query create table query are you able to understand or not understanding

2:8:52

Create table is clear, right? Anyone who is still not able to create a table?

2:9:08

Create table is working. Now what is the second query that we have written? We can

2:9:22

see this that in second query what we can do we are inserting a simple row so whenever we want to

2:9:28

insert a specific row we can use what command we can use insert into command so you can see this

2:9:34

that we have written that insert into students and we are specifying that what are the columns

2:9:41

we are providing like the column is full name which is having a value on an anaya sharva then you can

2:9:47

see that email i have written the email is this particular email

2:9:52

Code says agentic system. City is Bangalore.

2:9:56

So you can see if I write something like this right, then automatically the value will be generated.

2:10:02

Is this part clear?

2:10:05

This query are you able to understand?

2:10:06

You can write it them in like these two lines also.

2:10:10

This way is also correct.

2:10:11

So rather than writing them in multiple lines is not important.

2:10:14

If I write it like this also right, then also it will work.

2:10:20

Correct.

2:10:21

Now, if I want to insert multiple rows, I can even do that.

2:10:25

Like for example, if I want to insert here multiple rows, I can write the same thing that

2:10:30

I am inserting into students.

2:10:32

I am providing this four data, full name, email, course and city.

2:10:37

And these are the values that I'm providing.

2:10:39

So you can see this is one value, this is the other value that we are providing.

2:10:44

So two values we are providing, they will be inserted up.

2:10:47

Is this thing clear, right?

2:10:49

So you can run them one by one also.

2:10:51

you can run them together also, whatever works.

2:10:54

Like if you run them together as well, then also it will work.

2:10:59

I think currently these two queries are clear, right?

2:11:02

The first query that we are writing, it is for inserting one particular row.

2:11:07

The second query that we were writing, like if you remembered this particular query that we were

2:11:11

seeing, this is for single row.

2:11:13

I think the idea is clear, right?

2:11:21

Here, only two queries we will discuss today because I think it will be too much confusing.

2:11:26

So these two queries you can try and you can run it.

2:11:30

And if you go into your table editor, right, you should see three rows that are there.

2:11:34

If you are not able to see, just press Control Shift R.

2:11:38

If your table is created, then you can hit this refresh button and you can do that part.

2:11:43

Other queries in the next class we can see.

2:11:46

Currently till here, this particular part is clear, right?

2:11:48

Whatever we discussed, basic queries you are able to understand.

2:11:51

Yeah, you can do that.

2:11:58

Guys, currently whatever we discuss till here, this part is clear, right?

2:12:03

Insert into other queries, select queries, we can do it in the next class.

2:12:07

You don't have to worry like we will take things slow only.

2:12:10

So in the next class we can discuss about select and other queries that are there from here.

2:12:16

That part we can see.

2:12:18

The first two queries are a little bit complicated, but

2:12:21

other queries are very, very easy.

2:12:23

Like if I write, let's say that I want to find out how many students are there in Bangalore and anything,

2:12:29

then I can write, or if I want to see the data, like if I write here, select star from students.

2:12:35

And if I try to just run this, you will see all the students will come up.

2:12:39

Correct, right?

2:12:41

So this way multiple type of select queries we will see and we will practice, but that part we will do it in the next class.

2:12:48

Currently, first two queries you can focus upon.

2:12:50

upon which I have written here.

2:12:52

So you can, I am sharing the doc again.

2:12:54

So you can use this doc and you can practice first two queries on Subabase.

2:12:58

Other queries we can take up in the next class.

2:13:03

Apart from that, you can see this is a website that I shared you for database part.

2:13:08

Then this is another website that I shared you for different, different foreign key examples.

2:13:14

Then this is the PPD that we had for today's class.

2:13:18

So currently till 22 slide, we have.

2:13:19

slide we have discussed.

2:13:21

In the next class, we will start from 23rd slide.

2:13:24

We will talk about select queries that are there,

2:13:27

how we can write it, update query, delete query, where query,

2:13:31

and all the patterns that are there.

2:13:33

That part we can take up in the next class.

2:13:35

Because currently I think we don't have much time.

2:13:37

So it will be a lot more complex because I see that

2:13:41

a lot of students are finding it difficult to actually create everything on super base and all.

2:13:46

So slowly only we can take.

2:13:48

I think table,

2:13:49

creation we have already done and data insertion part also we are able to do

2:13:53

till here everyone is able to do that right

2:13:56

I think everyone is able to insert anyone who is still how many people have in

2:14:02

like ran these two queries successfully did right

2:14:10

yeah we can see that style in the next class we can see that how we can convert

2:14:15

that also yeah so be ready for the set

2:14:19

because like this is a setup that you will require all the examples that we will practice of sql right

2:14:25

you will need this setup that we have done today so if you have done that setup you will be able to

2:14:31

write queries as i was showing you right this kind of query that i wrote here which was like

2:14:36

select star from students so then you can see the entire data and all so i'll explain you what this

2:14:43

select statement is doing and how does it work but once we do that we will be able to see the

2:14:49

this particular part that data is coming up so yeah only that much we need to do this

2:14:54

part we will study from the next class till here what we discussed were you able to understand

2:14:59

that so i think you are not copy-pasting correctly right krisch like if you see rakesh fatale

2:15:11

here only what are you doing like i don't know where is krisher written your call

2:15:19

and everything might not be incorrect that is why you need to update the data correctly like for

2:15:25

example if you need to date update the data for krish here right then probably you need to write

2:15:30

the data up here like this let's say if you are writing here kresh uh then automatically any

2:15:36

email that you are writing let's say kresh and other things right if you run it see it is working for me

2:15:42

and i can see the data also if i go here i can refresh the data automatically refresh will happen and

2:15:48

is updated correct right so you need to write the query properly see the like the braces and

2:15:56

inverted commas that you are writing is that idea clear i have pasted that i'll paste it here also

2:16:05

if you want to copy you can copy from zoom chat and identify that what you are writing is incorrect

2:16:11

because you are writing here double quotes so that double quotes that double

2:16:14

quotes that you are writing is wrong that idea is clear right

2:16:18

You have clearly written here double codes.

2:16:20

In the error also you can see that part.

2:16:26

I think this that thing is clear right, correct?

2:16:34

We will see that part Sanya why that is happening.

2:16:48

right till here this thing is clear in between nidh and other queries also that part we will see later on

2:16:58

once we delete our data how the numbers will update that part we'll see

2:17:05

till here this setup is clear right whatever we discussed are you able to understand that or not

2:17:12

insert into an create table are you able to understand you need to follow proper syntax like

2:17:17

like python if you don't follow proper syntax like python like if you don't do

2:17:22

colans and all right if you don't write inverted commas properly then it will not work

2:17:27

that idea is also clear right

2:17:34

till here we are good to go

2:17:41

yeah what is the doubt you are having what is the exact issue that is coming

2:17:45

go on like what is the exact issue you are having other people is everyone able to do

2:17:56

anyone else who is stuck which step you are stuck

2:18:03

which exact step did you not follow did you create a count

2:18:11

so why did you not create account when everyone else was creating the account

2:18:15

did you go to supabase.com and then create account right i shared all the steps that are there then

2:18:24

why did you not follow that so follow that from the recording and once you are able let's say after that

2:18:30

you are not able to do then we can start right these are the three steps everyone in the class was able to do

2:18:36

it so why did you not create account then

2:18:45

other people how many people are able to do the setup can you write a yes in chat if you are able to do the

2:18:52

setup yeah right yeah so those who have done the setup in the next class we will see different

2:19:04

queries we will try to write down and we will try to start learn the parts that are there

2:19:15

yeah share your screen purjan let's say if you create a free setup it will not ask for

2:19:23

payment and all probably i'm not sure if you were listening or not in the glass but free account

2:19:29

only everyone is creating right share your screen i have shared the syntax also right you

2:19:43

other people can watch the recording and then you can do can you share your screen quickly

2:20:13

yeah right in later on class we will bidia we will discuss that

2:20:23

gorevin this particular doc i've added that

2:20:43

open this project which is already created it's a free account only right open this

2:20:51

project where to open this project

2:20:56

this is already project that you created right just open this project

2:21:02

project

2:21:04

oh had to click on the project name this one yeah

2:21:13

yeah right it's healthy it's created go to sql editor that is there

2:21:23

where to go left side uh more left left left this one school up can you see escal editor here

2:21:35

school editor here school editor search where is the school editor

2:21:41

no ascal editor is not the table editor uh ascal editor is there shall i click it

2:21:48

yes right now follow the steps that we discussed in the recording watch the recording again and

2:21:53

then see what you need to copy paste and how you need to write it correct your screen is black

2:21:58

type is coming it is what type of screen that is dark theme right i'm using dark theme you are using

2:22:10

white this is very basic right like you know right in phones also dark theme and black

2:22:16

theme is there okay so now i have to copy paste this one know from where i will get it yeah right

2:22:24

you have to copy paste from the dog that i shared okay i think everyone is able to understand

2:22:36

right that much basic i think everyone is aware of right

2:22:40

guys is everyone able to follow the steps that are there i think you can try from the doc and

2:22:48

using the dock part you can see

2:22:51

uhurjan you have the dock link right i'm sharing the dock link use that particular

2:22:56

dock link watch the recording and then do that i think we are good with the setup in the next

2:23:01

class what we will be doing is we will be studying about the select statements that are very

2:23:08

very important like you can see the create table and insert into are not that important

2:23:13

because generally the data will always be created and we don't have to create the data every time

2:23:19

but we might have to search the data a lot of times so that is why that will be very very important

2:23:25

correct right i think till here this thing is clear right whatever we discussed

2:23:38

is everyone able to understand that part

2:23:46

yeah yeah so in the next class we will continue from the 23rd ppd only the 23rd

2:23:52

slide that is there that only we will start yeah yeah coppel i think you can take over

2:24:00

okay so all right it was an intense session today a bit of theory a bit of theory and lots of

2:24:08

So let's thank mentor. I'm sharing the feedback poll. Please stay here for the short

2:24:17

quiz that we'll be having at the last of the session.

2:24:38

Thank you.

2:25:08

Thank you.

2:25:38

Thank you.

2:26:08

All right.

2:26:12

All right, so I'm just sharing my screen.

2:26:38

Let's get ready.

2:26:43

So either.

2:26:45

Either you can scan this QR code or you can go to scan this QR code or you can go to W.

2:26:58

W.

2:26:59

Minti.com and enter this code.

2:27:02

I'm just copy pasting this code in the chat section as well.

2:27:07

Thank you.

2:27:37

All right, so let's let's start.

2:27:42

What is one?

2:27:44

What is one major problem?

2:27:54

What is one major problem of using CSV or Excel files at larger scale and the options are too much automation, automatic indexing, built in AI support or difficult current access?

2:28:06

And the correct option is it is difficult to have concurrent access.

2:28:36

while using CSV or Excel files at large scale.

2:28:40

Let's look at the leaderboard.

2:28:43

Get ready for the second question.

2:28:57

Which database type is best for Semantic search and the AIMMMMMMMM.

2:29:05

and the options are relational database, vector database, time series database or a spreadsheet database.

2:29:10

And the correct option database is

2:29:31

and the correct option is vector database.

2:29:34

Let's look at the scoreboard.

2:29:49

Get ready for the third question.

2:29:56

Which SQL command is used to retrieve data from a table?

2:30:00

And the options are, insert, select, delete or update.

2:30:03

or update.

2:30:33

is select comment.

2:30:48

Buckle up for the fourth.

2:30:50

For the fourth question.

2:30:56

In our relational database, what uniquely identifies each row and the options are,

2:31:02

options are, primary key, foreign key, column or schema.

2:31:32

And the correct option is primary key, which uniquely identifies each row in a relational database.

2:31:41

Let's look at the scoreboard.

2:31:45

Let's look at the scoreboard.

2:31:48

Get ready for the fifth question.

2:32:01

Which database family is most suitable for flexible JSON-like data?

2:32:07

And the options are vector database, relational database,

2:32:10

NoSQL database, or time series database.

2:32:31

And the correct option is no SQL data this.

2:32:56

Moving on to the 6th question.

2:33:01

What does the wear clause do in SQL?

2:33:11

It filters rows based on conditions, creates a new table,

2:33:15

deletes the database, or adds new columns.

2:33:31

And the correct option is it filters rows based on a specific condition.

2:33:48

Let's look at the leaderboard.

2:34:00

Moving on to the seventh question.

2:34:12

What is the purpose of a foreign key?

2:34:14

And the options are to delete duplicate rows to reference another table's primary key to encrypt the database to create backups.

2:34:30

Yes.

2:34:45

Quarren key is used to reference another table's primary key.

2:35:00

Now, get ready for the final question.

2:35:13

Which platform was used in the session for browser-based PostgreSQL?

2:35:19

And the options are MongoDB, SQLite, Superbase, Pinecombe.

2:35:30

and the correct option is supervise.

2:35:51

Let's look at the final leader one.

2:36:00

So Nicholas was the fastest one.

2:36:12

Let's stop here.

2:36:17

We'll meet on Wednesday for hands-on session on Python.

2:36:24

Till then, bye-bye.

2:36:26

Good night.