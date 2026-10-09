0:00

Thank you.

0:30

Thank you.

1:00

hey good evening everyone good evening can everyone please confirm in chat you are able to hear me folks am i audible

1:23

is everyone able to hear me good evening how's everyone doing

1:30

how is it going folks good evening good evening how is everyone doing

1:43

yes i am also doing good thanks for asking yes i am better now i have recovered from my fever

2:00

learning good to see that how's the classes going on folks oh sorry just give a minute

2:13

anyone has any doubts related to previous class

2:21

let's discuss that is anyone having any doubts related to previous class

2:30

Did you practice creating tables, patching data from those tables?

2:38

Did you practice that?

2:43

Did everyone try running queries, folks, whatever queries we learned in the previous class, let me know.

2:50

Cool, I hope everyone did.

2:55

So let's first understand today's today's.

3:00

learn to raise learning objectives. Let me share my screen. Just give me a minute.

3:09

Okay. So these are the learning objectives of today's class. In the previous class,

3:28

you remember first we understood why database is needed what is a relational database what is non-relational

3:33

database then how do we store data in relational databases where we understood what are tables

3:40

how to create tables how what are keys in those tables primary keys if you remember then we

3:46

understood constraints in the table then we learned about how to fetch data using select and then we saw

3:52

how to insert data how to add data using the insert command today what are the learning objectives are

3:58

First, we will understand how to update the existing records.

4:02

Let's say there is already an existing record that we have created an existing row.

4:06

How do we update it? How do we delete a row? Then we will understand how to create relations.

4:12

This is a very important part that how to create relations, one to one relation. What does this

4:16

even mean? That also we will understand. What type of relations we can create,

4:22

why relations are mandatory in relation, like why relations are helpful in relational database.

4:27

that also we will see then we will see multiple types of queries that we can do using the wear

4:32

clause these are very important so this is a if you see the class name itself is fundamentals

4:39

because these are very very important for the things that you gonna do after these classes

4:44

basically creating any project for any project you will store the data you would want to face

4:49

the data if you see there the classes that we are learning of the database what is the

4:55

practicality of that how do we use it in the industry right now is all of the things that you're

5:00

learning is being used daily the reason is because every company every product-based company

5:05

every service-based company any company which is providing a tech service they store the data

5:10

in database and if they are storing the data in the database they need some ways to insert data

5:16

fetch data all of this that is what we are learning right now so that's why it's very very important

5:21

and very very helpful for what's coming next in the next upcoming up coming

5:25

classes you will be creating projects as well and in that also you need to understand database

5:29

fundamentals if i show you the mental map of today's class if you see before this module the yesterday

5:35

is the previous class we learned about sql fundamental one where we saw how to add data how to create

5:43

tables and everything today is the important part where you will see how to update data

5:48

delete data how to create relations that is the most important part of today's class so this we will be

5:54

be revolving the class around this whole content of today that after the class at least

5:59

you should have the proper knowledge of how to update and how to delete and how to create relations

6:04

and what type of queries you can run right using where clauses that all we will see is everyone

6:09

clear with the learning objectives and the mental map let me know is everyone clear with

6:17

that let me just open the board as well and then we will

6:24

get started and let me open the project as well just give me a minute

6:54

you can't be able to see the board now you should be able to see the board now is everyone able to see the board folks

7:24

i finish having a doubt there are various types of programming

7:31

language like c sharp c plus plus python etc likewise how many types of query

7:35

language there are multiple types so that's why see the main goal of me teaching you is because

7:44

i know what is relevant right why i am here because i know you don't have to learn all of that you

7:50

have to learn the one which we are learning already right sql is

7:54

is the predominant like we have multiple programming language there are not much options for

7:59

query language sql is the most predominant and almost 99% people will use SQL only because they do

8:07

not want to over burden their mind think about this as an engineer why i have to learn 100 languages

8:14

then for query language also we have 100 languages that's why we have we don't have that many options

8:19

itself for query language because people don't want to have that overburden in their mind

8:24

so that's why you can assume for query language at least you will only study sql you will

8:32

only hear about sql no people no person is going to talk about some other query language okay it's a

8:38

good question i hope i helped you answer that so if you see let me just uh open our database

8:49

folks first of all please help me in understanding honestly i

8:54

answer this did you create everyone super based project and did you create the table and

9:00

the database and then you did select command insert command did you do that tell me honestly everyone

9:06

let's be honest with yourself

9:24

there only four people are there in the class is it everyone do we have only four

9:32

people in the class who are listening to me people are answering no and yes see they are honest

9:39

they are answering at least there are at least 25 students who are not even answering

9:49

yes it's fine if you can say no but let me know in the chat

9:54

okay i see almost everyone say no there are a couple of students

10:04

four five students who are saying yes it's fine see sometimes you can have personal uh work also

10:12

but since you will having you will be having a weekend right after this class there will be a weekend

10:17

saturday sunday you will have please try to do that okay it's completely fine i cannot say anything for

10:24

those students who did not even answer i'm not sure they are themselves themselves

10:29

they are not even answering i'm not sure what they want to do but for the people who answered i'm very

10:35

you answered you are true to yourself there is no point of lying to yourself when you are preparing

10:41

it's for your benefit only if you are lying to yourself that's the worst thing you can do to yourself

10:46

when you are preparing for an interview right so thanks for answering but again i would say we have a weekend ahead

10:54

i completely agree like we had like what we had the class on tuesday and now we have

10:59

on thursday so you only got wednesday right it's completely fine you did not get time and you will have

11:05

a weekend so please do that right but always be honest with yourself in the preparation that is the

11:11

most important part cool now let's get started just give me a minute

11:24

okay so we will open the project that we created in the previous class so let's go

11:35

here i am already logged in i will just go to my dashboard and i should see my project already

11:42

there this is my project

11:48

iatna database learning and in that we can see that in the previous class we created the student

11:55

table and in the student table we added some data also around six entries each student is having

12:02

email city marks right all of that is present this was the default value that we added not given

12:09

and here we were typing all the queries in the previous class in the sql editor i hope everyone

12:15

remembers that we did uh do

12:18

and then we did insert we do a create table so three queries we did in the previous class that is

12:25

let me do that create table then i did then we did basically select data from the table and then we did

12:42

insert data in the table let me know everyone remembers that these three

12:51

things we learned in the previous class the main important things creating adding data

12:57

fetching data today we are learning how to update data right everyone today we will see how to update

13:05

data so let's say there is a for updating data updating data updating updating updating updating updating

13:12

the existing entry in the table let's say i can open the table actually in the other tab so you can see

13:22

side by side okay let's open that it's opening if you see let's take the example of raman

13:37

city is puna right let's say this is an already existing record right raman is an existing

13:43

record and we want to update raman right let's say we want to update raman how will we update raman

13:50

first of all we need to select raman do you agree right first of all you somehow you need to

13:57

select raman and say this is the row i want to update so how do we update the syntax for updating is

14:03

first understand the syntax right you write update that table name which table you want to

14:12

update then you will say what i want to update so i will say set please update this column the

14:20

which is the column name to the new value right where now why i am adding where using this where i

14:29

can select the row let me explain you how does this work

14:33

so what does this command mean is it says please update in this table select please set let's

14:43

say i want to change city puna to agra let's say i want to do that so i will say set city equals to

14:50

agra where to which rows till now everyone if i remove this line let me know if i let me zoom in i think

14:58

people are saying let's see folks if i remove this line

15:03

it will update the complete table or not let me go it will update every entry in the table

15:10

yes or no folks right now what will happen is it will go and update every entry in the table

15:16

because did we mention which row i want to update let me know did i mention any time that which

15:22

row i want to update let me know folks did i mention this no so what it will do it will go to this

15:28

table student table and update every city to puna let me actually show you so this is a

15:36

syntax i wanted to show actually let's do this you can say update student set city equals to

15:45

pune and if i run this query success query has run this run

15:55

reload this do you see something what happened it updated everyone to poohne

16:03

let me know is this clear because in the update command we never told which row i want to update

16:10

are you clear on that let me know you see that here we never said which row i want to update

16:15

to update it so it updated everything now how can i say i want to update a specific row so i can

16:22

say please update so whenever see oh sorry whenever you feel like your query is becoming bigger you can

16:32

break it down into multiple line you can break it down anywhere in multiple line to make it more readable

16:38

people do that often to make it readable because query becomes bigger right then they will say where

16:45

please update city to puna where email is this raman so it will upon it will

16:54

update only the raman entry let me show you where email is this you see that what is

17:02

what is happening folks what does it mean it says please update the student table set the city

17:10

equals to puna in which rows where email is this only those

17:15

rows will be updated i can say let's say agra if i select this and run this success only this

17:25

raman will be changed to agra you see that everyone is clear let me know can't we do that using

17:32

id we can i'm just showing you here you can use anything i am using email you can use any column name

17:40

so you can say where id any unique thing you can use where id equals to one

17:45

so it will update only that row where id is one so i can say uh let's say uh bengalore

17:56

you see that and if i run this let's see reload this it will be changed to banglor are you clear sri

18:07

let me know make sense can we mention that particular row and column we are mentioning that particular row and column

18:14

we are mentioning that right say yukta we mentioned the particular column we want to change the

18:19

city column and then how we are mentioning the row the row where id is one this is what we are doing

18:24

correct say ycta let me know okay now let me know everyone has any doubt in this take your time

18:34

and then please let me know take your time please throw your questions in Q&A

18:44

i like when students ask questions so if you have questions you can always ask questions

18:50

okay so this wear clause this is called wear clause and how it is useful what where

18:58

clause does everyone what do you think what is the responsibility of where clause

19:02

what is the responsibility of where clause let me know correct where clause

19:14

is used for selecting rows filtering rows basically out of all the rows you can filter

19:21

rows using wear clause in the wear clause whatever condition you mention those rows only will

19:26

come right make sense are you clear on this is it mandatory to add semicolon at the hand yes

19:36

it is it's the best practice also so it's it's a good thing to because otherwise how it will know

19:42

that okay the query ends here or the query ends here it can also think right the query

19:48

query ends here let me know rzdeep correct sq can think okay the query is ending here only in

19:55

these two lines it knows how when query is ending using this only right that okay query is these

20:01

three lines correct raddip let me know are you clear can we update three rows at a time

20:08

folks again i'm happy to answer questions

20:12

but please put your questions in quana everyone do you want me to ignore your questions do you want

20:19

that i want that to happen i want to answer everyone question but please come your questions in quen

20:27

i would be very happy to answer someone is asking that can we update multiple rows together we

20:33

did that right if you see let's say i want to update every puna every row where puna is there i want to

20:40

update every row where puna is there i can say where city is puny updated to bengal you see that in this one line

20:51

in this one command how many rows will be updated five rows do you agree in this one command

20:58

five rows will be updated yes so if you see if i run this reload this every puny will change

21:10

to bangalore you see that five rows are updated in the one command also you can do this also if you

21:18

want to mention okay i only only want to change id 2 and id 5 row you want to mention that let's say

21:26

that only yaman and hamanshu should change the city then what i can do i can say where

21:32

id is 2 or 5 id is 2 or i'd is 2 or i i

21:40

idea is 5 please update it to let's say uh any city we can take let's say or we can say

21:48

ahemdabad uh whatever name is coming into my mind i might have written the spelling also wrong

21:57

let's see if i want to update 2 and 5 himansu and year 1 let's run this query

22:05

and let's see only these two should change 2 and 5

22:10

Are you see that? Do you see that? Let me know. Are you clear on this 2 and 5?

22:16

Jaman and Hwanshwa is here. Let me know. Elvin are you clear now?

22:24

Except Python, we need to put semi-collar after every statement in any other programming language.

22:29

It's not every other program. JavaScript is also semi-colon is optional.

22:34

It depends on programming language to programming language.

22:37

Instead of updating, we can replace as well.

22:40

or is it the same function what do you mean by replace update is replace only kind of right

22:47

we replace city with this right update is replace only like first what do you mean by replace here

22:54

okay you got it cool now let me know anyone else has any doubts everyone is clear

23:00

anyone here has any doubt sir one time if i want to update two fields in the same command

23:08

yes i will come to that i will explain

23:10

you that just in a minute till then i will come to that so it's a good question it is

23:16

asking sir in the same command can i update ct and some other column also in the same command we can do

23:24

that and i will come to that in a minute we can use multiple conditions at the same time like

23:31

logical operator yes we can as i explained you in the previous class also here you can keep

23:36

adding multiple conditions here you can say if i do

23:40

is this and name is this like the python way same way of mentioning conditions right

23:48

wherever wherever the name is this or id and id is this here you can mention or also like this you can

23:54

add multiple logical condition make sense name and email is content it can't be updated what

24:04

do you mean by that shalini everything can be updated name can be updated email can be updated

24:09

anything can be updated it's a column only right these are not constant what do you did we ever

24:15

mention something as constant no right when we created the table there is no concept of constant

24:23

in the tables right let me know so if i show you let me show you let me show you that by changing

24:31

name let's say id1 want to change name from raman sing to

24:39

uh raman let me say where id is one i want to change the name to raman sing uh

24:53

two i'm just adding random name so it will change raman sing to raman sing two and let me just run

25:00

this query students oh it's called full name full name full name

25:09

change to raman sing two and if i reload this and show you you see that are you clear let me know

25:19

charlani are you clear now

25:24

let me know okay you are clear now coming to that can we update two columns at the same

25:38

time basically in rows let's say here i want to change name i want to change the name to raman

25:46

sing and city to puny of this id one so how can i do that if i want to change two things at the same

25:53

things at the same time i can do that set full name as raman sing and i can say comma

25:59

city as pooh name so you see that in one update command this raman sing will change this row

26:05

will change two things what are the two things city and name are you clear on this let me know if i run

26:10

this you see that raman sing two will change to raman and city will change to puna if i reload this

26:20

are you clear on this let me know in the same command we updated two things

26:23

are you clear himanshu let me know everyone is clear on this now let me know anyone has any

26:33

doubts take your time and let me know from a table can we also change a

26:42

specifically first or last name if it's required from a table can we also can be also

26:48

change what do you mean by that if there are two columns first name and second last

26:53

name you can change that shares what do you mean i i think i did not understood your

26:57

full query i showed you by changing the name right let me know what do you mean by that

27:07

shianch if there are two columns called first name and last name you can always change

27:13

that take first name and change it take last name and change it okay if someone only want to change the

27:23

name then it will happen in programming language see what srians is asking sir can we do

27:30

something like this right now full name is there in that someone wants to change raman only they

27:36

want to keep the second name same they want to change raman only then it's a logic do you agree

27:42

in the first class also i explained two things what is programming language and what is query

27:48

language programming language is something which can have logic do you agree now this becomes

27:54

a logic that from full name i want to update only the first name this is a logic this will happen

28:00

in programming language so what will happen programming language your server will ask database tell

28:06

me the full name then programming language will apply the logic key to extract the first name

28:12

updated and then call database to write the full name make sense riance did you get this part

28:18

can i change a whole column what do you mean by that whole column i showed you

28:26

right everything changed to puna when i did this what else uh sanukta do you mean by a whole column

28:33

let me know in qa how we change inside raman sing at one column is this possible or separating

28:43

in terms of part am i'm unsure sorry i did not understand can you please explain your doubt

28:47

whenever you ask doubts everyone please write take your time and write fully do not try to

28:53

write shortcut doubts because it is not understandable for someone right take your time take one minute

28:59

and write fully like explain your doubt in the full form whenever you answer ask doubts in short

29:06

forms like short sentences it is not understandable generally okay take your time i'm happy to

29:14

answer questions take your time and let me know once everyone

29:17

will be clear then we will move forward anyone here has any doubts if i want to

29:27

change let's say the email column all the email can we do that yes san yukta i showed you right

29:33

when we changed every city to puna if you remember if you don't add this the first query which we run

29:40

was this only right the first query that i read using update was this only if you don't mention

29:47

don't mention which rows you want to update it will update everything set let's say you want

29:53

to update every email to let's say hello at the rate example if you do this it will

30:02

update everyone's email the first query we ran this only right okay you are clear cool

30:10

nita says sir can an id be updated and can id be also deleted if an id is deleted can it be

30:18

updated again first of all deletion we have not seen right nita i have not explained deletion yet

30:24

deletion once we understand then i will explain you deletion now update you can update the id also

30:30

id updation is possible i can update

30:40

equals to 10 where the name is reman sing so i want to update the row id to 10 let me

30:50

done this query where full name is roman sing let me reload this now raman sing

31:02

you see that roman sing id will be 10 you see that roman sing id is 10 are you clear let me know

31:10

Nitesh, are you clear?

31:16

Cool.

31:19

Now going to reading others doubts.

31:24

Himansu says, full name inside Raman Singh is there, then can we update, Raman only can be update?

31:30

That is what I was explaining Ramanjou.

31:33

Folks, when you are asking doubts, please hear to answers of other doubts as well.

31:39

Shrayans asked this example.

31:40

exact question which I answered, right?

31:42

Manshu.

31:43

That is a program, that is a logic you want to implement.

31:45

SQL is not a logic language.

31:47

It's not a programming language.

31:49

Okay, this is just one thing first before I answer it.

31:52

I just want to set it loud, loud.

31:54

What is the point of Q&A?

31:56

The point of Q&A is learn from other questions also.

32:00

When somebody is asking questions and I am answering,

32:03

please hear the answers and questions.

32:05

Because you are asking the same question which I just,

32:09

just one minute back,

32:10

and Sastred, right?

32:11

What does it mean is Hamanchu?

32:14

When you take full name and you only want to update one thing, right?

32:18

In this full name, in this string, you want to, first of all, you want to split the string by spaces, right?

32:25

First name, second name, then you want to update the first name and then you want to write it

32:29

again in the database.

32:30

That is a programming logic, right?

32:33

That is a logic.

32:34

You want to split it using space.

32:36

It goes into programming language.

32:37

This is not programming language.

32:39

This is query language.

32:40

It can query the data. It can update the data. It can update the data.

32:44

So what will happen?

32:45

Your programming, your Python fast API server will call database and say,

32:50

Give me full name.

32:52

Python will get the full name.

32:53

Python will write the logic from the full name, split the full name by space.

32:58

So you will get first name, second name.

33:00

Then you will say, okay, change the first name to let's say Naman.

33:04

Then it will append first name and second name together and call database to write it.

33:09

You got it, my name.

33:10

part let me know.

33:18

Okay, cool.

33:20

Shian says if some user or client have inserted their first name incorrectly and later they need

33:26

to change it, then the first name will be need to change use the programming language.

33:30

But if they want to update the entire name, they can be done using query.

33:33

Am I reading correctly?

33:36

Anyways, in both the cases, query will be run by your server only right?

33:40

Let me know.

33:42

Correct, Shriand.

33:43

In any case, database, client cannot directly go to database.

33:47

They will always go by a server.

33:49

Server anyways, in both the cases, when they want to update only the first name or they want to

33:55

update the full name, they have to come by a server only.

33:58

They will hit an API using that API.

34:00

You will update either the first name or the complete name.

34:04

You're getting my part, Shianz.

34:10

Okay, it's cleared. Very good.

34:13

I have a question, sir, that when we do log in to any application, it is possible for us to log in by

34:19

two or three emails.

34:21

If we have, then is it possible that all the emails we use to log in are stored in database?

34:26

Every email is stored in database.

34:28

And yes, you can log in using multiple email addresses.

34:31

That is allowed, Syyukta.

34:33

Generally, there are different types of websites.

34:37

Some websites allow login using mobile.

34:40

number right so one mobile number one log it some allow using email one email one log it

34:46

and their email your email will be stored in the database it's a correct understanding

34:52

your emails are always stored in database using which when you try to use the same email for sign up

34:58

let's say i created a account using my email hello at the rate example.com when i try to create the

35:04

account again using that email it will go to database and see is there any account

35:10

already with this email it will find the entry and it will reject your request that you cannot

35:14

create it makes sense every email must be unique by default yes it depends on the table here we are

35:24

creating student table every student should have a unique email okay now let me know anyone else has

35:34

any doubts good questions see if you will ask questions you will understand better

35:40

right you are you might be seeing this so please ask questions

35:48

take your time now is everyone clear with update anyone here has any doubt with update

35:52

okay you can also do this okay i think everyone seems to be clear anyone i don't see anyone's

36:05

anyone is having any doubt okay you can also do this let's say i want to update every

36:10

student who is let's say there this is student exams let's say every student was giving

36:16

exam this student gave exam in ahmedabad this student gave exam in banglore this student gave exam in

36:21

banglore this in amdabad banglor puna and let's say these were the marks they got but later we figured

36:28

out okay in puny sorry not in not in amdabas exam got leaked or not leaked

36:35

or not leaked let's say in amdabad one question was wrong

36:40

in the exam exam said was different banglore ms said was different puni said was different

36:46

in ahemdabad we got to know one question was wrong itself so we want to give grace marks so we want to

36:54

update each student marks by three numbers that you will get three three numbers because in exam one

37:00

question was wrong so what i want to do is i want to update every student marks who belongs to amtabar

37:07

and increment three marks by three plus three i want to do then how we will update do you

37:13

understand the problem statement first let me know are you clear with the problem statement first

37:18

every student which belongs to ahemdabad they have to get plus three marks extra

37:24

they scored these many marks but they want they should receive extra three marks because their

37:30

exam was wrong one question was wrong for how we will do is we can simply say

37:37

that update students where city is first of all haemdabad

37:53

set marks equals to whatever marks they have plus three they will get three extra marks you see that so this is how you can run

38:04

query languages also can i zoom in more oh i think it might not be writeable then

38:11

like i will not be able to write but is it fine now okay i can run this query success so you will see

38:21

that ahmdah bar 88 and 12 this will become 15 this will become 91 let's reload this

38:28

you see that 91 and 50 are you clear everyone let me know

38:34

is clear anyone here has any doubts then we let me know take your time and do let me know

38:48

know if anyone is having any doubts is everyone clear okay now should we see delete command then

39:04

thing should we move to delete if this is clear update is clear okay now let's learn

39:13

how to use delete command if you want to delete any entry from the table so the syntax for delete

39:20

command is that generally when you want to delete again it's very similar to update command

39:26

to be very honest you can say delete from which table i want to which table i want to

39:34

from table name if i don't mention anything then it will delete the complete table

39:40

itself right everyone it will delete the complete table itself then i can mention which rows i

39:47

want to delete where the condition this will tell which rows i want to delete

39:53

whatever condition i will pass the way i was passing in update command those rows will only

39:59

be deleted something like i can say let's say i want to delete the entry of rammer

40:04

whose id is 10 i want to delete it so i will say delete from student's table where

40:12

id is 10 and if i do this it will delete success and let's see the raman entry should be deleted

40:22

from the database do you see that is this clear the delete command update updates the entry delete

40:34

completely and in one delete command you can delete multiple rows as well so this right now

40:40

we deleted only one entry in one delete command delete from students where let's say i want to delete

40:48

every student who belongs to ahmedabad right i want to delete every student who belongs to amtabad

40:56

or let's not delete amtabath because we will have less data let's delete every student who received

41:02

less than 30 marks okay so only this will know i want to show you multiple deletion

41:08

let's delete every student who received marks between 80 to 80 to 90 okay how about that

41:18

delete every student who received marks in the range of 80 to 90 so this will be deleted and

41:24

this will be deleted correct this and this two students should be deleted let's see where i want to say

41:32

marks is greater than 80 and marks is less than 9 let's run this query now we should not

41:42

have any student from 80 to 90 marks that means these two should be deleted and you see that it is

41:48

deleted let me know everyone is this clear both the students are deleted of 80 to 90 marks in this

41:55

range so delete is a destructive command that means once the data is deleted it cannot

42:02

be recovered so you have to be very sure about deletion you cannot allow deletion from any

42:08

user that's what the concept of admin user comes in you will have an admin API which only admin

42:14

can access and using that API you will delete in the database do you understand the meaning what i

42:20

mean delete command should not basically any API which deletes should not be accessible to everyone

42:27

like this it should be accessible to admin users basically for an

42:32

let me take an example of school in school the delete command should be accessible only by the principal

42:39

principal can remove the student can remove the teacher so the API should be accessible only by principal

42:48

principal authentication token will access only that delete API and that delete API will go to

42:53

database and delete the data using the delete command are you clear let me know is everyone

43:02

clear is everyone clear with select update and delete

43:12

okay if i don't mention any condition in this it will delete every entry from the student table

43:24

from the student table every entry will be deleted if i don't mention a condition i will not do that

43:31

i need the data but you got it right you can run there simply remove this and it will

43:36

delete every entry from the table that means when we delete our account from any application

43:44

the data inside the database are also deleted like this correct san yuctor it is deleted like this

43:49

it's up to company when you when you do sign up in a company you have to read the terms and

43:55

condition of their company it will say that whether they want to delete it or not it's up to company so if

44:01

you are if you are doing checkmark when you read the terms and condition you say i accept

44:05

terms and condition they mention conditions like this whether they will be deleting your data

44:12

after you let's say go away from your platform from their platform okay for delete is there no

44:20

requirement of star star is used for selecting columns

44:24

srians star is used for selecting all the columns here are we selecting columns we are we selecting

44:29

we are deleting the data right why we will use star can we retrieve the data

44:34

after deletion no rasdib you cannot delete you can not get the data after deletion it's deleted

44:39

permanently deleted shyan's and rasdib both are clear with your doubts let me know

44:50

take your time and let me know if anyone has any doubt

44:59

folks before you move forward are you clear with select update and delete

45:03

is everyone clear here here that is a column

45:18

that is a separate thing that is a separate concept we will talk about that

45:26

is a separate concept we will talk about that that is a separate concept all together we will talk about that but

45:29

separately anyone here has any doubts i just want to make sure before moving

45:37

forward because if this is not clear anything going forward will not be clear so take your time and ask

45:42

your doubts we can go slow take your doubts and then only we will move forward

45:49

if anyone has any doubts let me know

45:59

anyone anyone okay everyone seems to be clear i think then we can move forward

46:11

now we will understand the very important concept of relational database that is called

46:16

relations the name itself says relational database that means it has to provide the functionality

46:21

of relation and what does it mean let's go to board and understand first of all why do we need

46:27

relation itself like what is the concept of relation itself let me show you

46:36

what happens is folks generally you cannot keep all the data in one table because the table

46:45

will let me explain just give me a minute

46:51

now way i was showing you one example in the previous class about user and courses right which

46:56

student is enrolled in which course so user data is in user stable courses data in course

47:01

table similarly take an example of orders let's take an example of blinket in blinket first we

47:09

will have table users which all the users data will be that which users are there on the platform

47:16

something like this they will be users table in the user's table you will have the data like

47:26

then user name user email and when this user signed up let's say signed up at

47:37

the date at which user signed up signed it or it can have multiple things right but those will

47:46

be use related information yes everyone like one one one information could be

47:56

is this a active user not these kind of multiple information can be there

48:03

like in the user id1 this is let's say i was the first user at blinket and i can say hello at the

48:09

rate example dot com signed at let's say 2017 and active yes i am active user right and then there

48:18

can be other user let's say it's second user was amman

48:21

amman at the rate example.com amman signed in 219 and it's an active user

48:28

these are active users now there will be one table which will have orders data when the user is

48:36

making any order there will be one table like orders table in that we will maintain all the orders

48:43

data so every order is done by any user only right everyone everyone agrees

48:48

every order will be done by some user so you will have to like this is the order id and this is

48:56

order amount like what is the amount of this order is this a cote order or not basically right and then

49:04

there will be address on which address this order has to go and which user place this order

49:12

id correct basically let's say order id 1 this is of 523 rupees it's not

49:18

a COD order that which is the online order and this is the address and user ID to place this

49:24

order that means this order is the phone among's order right this is a month's order similarly

49:31

there will be order ID 2 let's say which was for 1069 and this is let's say falls again online

49:40

order address user ID 1 and there is another order third order 223 calls

49:48

addresses this or ready to now let me know let's say we have arranged the data in two tables

49:54

like this can you tell me how much money amman has spent on blanket so far how much money amman has

50:04

spent on blinket so far how much money amman has spent on blanket so far can anyone tell me take your time

50:18

how much money amman has spent folks correct san yuqta elwyn you missed it nishant

50:26

why it will be 1069 amman i am asking aman 1069 for tanesh right everyone

50:34

1069 is placed by which user the order for 1069 is placed by which order everyone

50:42

let me know nishant salini 1069 is placed by whom

50:48

it's placed by tanishk right not amman amman has placed two orders one is 523 and one is 2 23

50:58

so how much amman has spent everyone let me know total how much amman has spent

51:09

let me know everyone total how much amman has spent 746 correct that's why now let me know

51:17

you tell me how much amman has spent only using this table is it possible only using the

51:24

orders table can you tell me how much amman has spent only using the order's table is it possible

51:31

if i don't show you the user's table let's say if i scroll it away will you be able to tell

51:36

how much amman has spent no right because order's table is related with user's table that is called

51:43

relation there is a relation between these two tables do you agree

51:47

these two tables are related with each other they cannot exist without each other do you

51:54

agree yes or no they cannot exist without each other because the data is related with each other

52:04

yes everyone this is called relationship in relational database that you can create

52:11

relationship between relational database and if you see there are multiple

52:17

types of relation first of all if you see here one user can have multiple orders do you agree

52:25

one user can have multiple orders this is called one too many relationship one to many

52:35

relationship do you understand that one entry here can have many relationship here basically

52:41

among you see that among has two relationship here do you see that you see that

52:47

you see that and this tanishk has only you see that one user can have one to many

52:55

relationship but how user id is being pointed currently that i will explain you that is a

53:01

separate concept inmanchu that we will understand for now you understand simply by seeing don't

53:07

assume it is connected i will show you right that is a separate concept it's called foreign keys i

53:12

will explain you that right now you don't have to worry about that this is the map

53:17

of database it's not mapping of database it's a relation between table that we create we will

53:22

only say once we are creating users table and orders table we will say to database please create

53:28

connection between these two tables okay this is for our understanding this is one type of

53:33

relations we are seeing this is folks everyone agrees that this is one to many relationship

53:39

there will be one entry here and for that one entry you can have many entry relationship here

53:44

this is called one to many or one to n also we can make

53:47

mention makes sense are you clear with one to many relationship the concept of one too many

53:58

tell me everyone i need answers from everyone from customer to order if you go from if you

54:09

have been given one customer data from that you can find multiple order this is called one too many

54:14

right everyone agrees one too many or one to n

54:17

we can see do you agree now someone was asking sir how these two will be actually

54:26

related right now we are able to see through our eyes that sir user ID is actually related to this

54:33

ideas let me everyone agrees correct this user ID is connected to that ID do you agree as or

54:40

no this brown arrow makes sense this user ID makes connected to that ID user's table dot ID do you

54:47

agree

54:47

this is called the concept of foreign key

54:57

focus on this what is a foreign key everyone understand this what is the foreign key

55:03

when i was creating the orders table when i did the create table command for

55:09

orders table then i would have mentioned id column i was integer amount amount integer amount integer

55:15

the COD true or false address is a string user ID is an integer when i was saying

55:22

user ID as an integer there itself i will say in creating the table i will show you also when you

55:28

were creating orders table and you were creating user ID column there itself you will say user

55:34

ID you are connected to you are connected to user's table dot ID in the user's table dot ID you are

55:42

connected to that that is called a foreign key that this

55:45

this key is connected to this users dot ID this we will say while creating the table

55:51

you make sense let me know are you clear now ankur has asked a good question anchor says

56:01

sir why we can't keep every data in one table itself right that's a good question that sir let's

56:09

keep orders data also in users table anyone can think why we should not do that what are your thoughts

56:15

let's take thoughts from everyone what are your thoughts why do you think we created

56:23

separate tables like this anyone in chat let's i need thoughts from everyone makes sense it will

56:30

become complicated good any anyone else nishanth is answered correct anyone else let me know

56:39

duplicates very good elvin very good answer now anyone else

56:45

if you see let's see if you would have kept everything in one table users

56:57

table itself then the data will be so much duplicated let me show you the table would have

57:05

liked the table would have looked like this this is user ID

57:15

then name, user email, signed at, is it an active user user, then you will have order ID, then you will have order

57:34

amount, then you will have COD, address, address, address, address, and you will have COD, address,

57:45

and user ID. Now we don't need user ID because it's connected, right? Now see. I think Rahul was asking, right? This was Rahul. Yes, Ankur. Angkor now see that. Now how will the data look like? For Amun, you have two orders, right? Just let me add the entry of Tunis. User ID 1. Tanishk, Tanishk, Tanishk ID, Tanish signed at 2017. Yes, it is active. Tanishk order ID is one. Amish, amount.

58:15

is 1069 and COD is, let's say, true, addresses this. This is fine.

58:23

For Amun, I have to, Amman has two orders, right?

58:30

For Aman, I will create two. Aman, I will create two. Aman, email Aman ID, signed at 2019,

58:38

true, order ID to, Aman placed in order of 523, true, same. Amon created another order.

58:45

First problem now, can you create another entry with two?

58:50

Because two is the user ID. Amin is creating one more order, but this is a primary key.

58:55

Now you cannot, first of all, duplicate two. Do you agree? You cannot duplicate two. For Aman,

59:00

do you want to create another order? In this user ID, can you say another two? Because Aman, for Aman,

59:07

I want to create another order, order ID3, of $223. Can I make an entry like this? What do you think, Ankur?

59:14

Ankur, are you getting let me know?

59:17

Correct? We can't do that. Let's say, if we don't make user ID as the primary key, if I don't do that,

59:25

first problem will be, there is no uniqueness in the row. Let's say if we forget about that also,

59:31

you see that this much data is completely duplicated in across the rows. Do you see that? So much wasted.

59:38

And assume these are only two orders right now, but Aman can have 10 orders, 20 orders, 30 orders.

59:44

If you see you use, if you use blanket, every day almost, every two days you make a blanket order.

59:50

How much data duplication will happen? Do you understand now, Ankur? Do you understand the problem now?

59:55

Everyone understands the problem now. That's why we create separate data like this, so that it's maintainable.

1:0:04

And once you start separating data, you need a way to connect data that is where foreign keys comes in.

1:0:10

To create relation, that's what I explained. When you will create the order stage,

1:0:14

When you are creating user ID column, you will say user ID, you are actually connected to userstable dot ID.

1:0:24

Users table dot ID. You see that? When you are creating this user ID column, here you will declare user ID.

1:0:32

You are actually connected to userstable.d. ID. You see that? I will show you also. I will show once I will start creating.

1:0:40

Are you clear everyone? We can create relation from primary.

1:0:44

We are creating, right? This is a primary key characterally. Let me know, Hamishu.

1:0:48

User.jsu. User. ID is a primary key only, right? We are creating the relation of that only.

1:0:53

Are you clear everyone? Let me know. Take your time and let me know. Is this clear everyone?

1:1:03

Anyone here has any doubt?

1:1:07

Primary key pointing to another. Then what is the point? What is that relation?

1:1:13

When you create a relation?

1:1:14

Manshu, that means you are creating relation between two same things, right?

1:1:18

If this is, you create order ID to user ID, what is that relation mean even?

1:1:24

What do you think? I will explain you, maybe. I will give you an example, but what does this even mean?

1:1:30

order ID can be anything. Does it depend on user ID? Let me know. Order ID can be 100.

1:1:36

Does it mean 100 user has to be there? No, right? Correct. Now are you clear? Okay.

1:1:44

Cool. Everyone is clear. Let me know. Is that makes sense?

1:1:50

All everyone seems to be clear. Okay.

1:1:55

We will see how to create foreign keys. I will show you. I think before we do that, I think we just crossed an hour mark.

1:2:02

Let's take a small break. Let's take some break. Get some water and we will start at 9.

1:2:08

9.15. Okay, folks. Let's be back at 9. 9.15 and then we'll start.

1:2:14

Thank you.

1:2:44

Thank you.

1:3:14

Thank you.

1:3:44

Thank you.

1:4:14

Thank you.

1:4:44

Thank you.

1:5:14

Thank you.

1:5:44

Thank you.

1:6:14

Thank you.

1:6:44

Thank you

1:7:14

Thank you

1:7:44

Thank you

1:8:14

Thank you

1:8:44

Thank you

1:9:14

Thank you

1:9:44

Thank you

1:10:14

Thank you

1:10:44

Thank you

1:11:14

Thank you

1:11:44

Thank you

1:12:14

Thank you.

1:12:44

Thank you.

1:13:14

Thank you.

1:13:44

Thank you.

1:14:14

Thank you.

1:14:44

Thank you.

1:15:14

Thank you.

1:15:44

Is everyone back, folks?

1:15:51

Should we start?

1:15:52

Is everyone back?

1:15:55

Let me know.

1:15:58

Okay, so let's see, should we learn how to create foreign keys then?

1:16:05

So what we will do is right now we did users table and orders table.

1:16:10

Similar to that, we can create a customer's table and orders table.

1:16:14

We will keep a very smart table we will create.

1:16:18

Let's create a table.

1:16:23

I want to create customers table or I can create users table also.

1:16:28

Just not to confuse.

1:16:31

And then we can give columns.

1:16:33

This user's table will have ID, which is an integer type, primary key.

1:16:40

Then we can create user's name.

1:16:42

I will keep it very short.

1:16:44

for now. Let's create this user's table.

1:16:52

It's running. User table is created. Let's see whether it's created. Then we will create the

1:16:57

orders table and then we will create the link between them.

1:17:00

User table is created. You see that. User table is done. Very short user table.

1:17:06

And then we can create an order table. Create table. Create table

1:17:14

order stable in orders also i will keep it very short for now id integer primary key

1:17:23

then amount integer right and we can say not null amount has to be there and what you can do is i can say

1:17:35

user id now user id is an integer here right user id column that i want is integer here but i want to create

1:17:42

but i want to create a relation everyone sees that first i want to create a relation here

1:17:48

right now these two are not related everyone agrees is the user ID in the customer table related to

1:17:55

in the orders table related to customer what do you think right now it is a normal column do you agree

1:18:04

we agree everyone it's right now it's normal column right now there is no relation between them right now we have

1:18:11

we have not connected them so how will you connect you will type that a foreign key i want

1:18:19

to create a foreign key i will say this user id column will reference to what everyone

1:18:27

references this user id column references what user's table dot id do you agree user's table.

1:18:35

dot id i will say in the user's table id column id column this is how

1:18:40

this is how you create a foreign key do you understand this line user ID if you don't write

1:18:46

this line this user ID is not related to the user's table at all so i say in the order's table

1:18:52

please create a foreign key this user ID should reference should connect to user's table

1:19:02

and the ID column you see that everyone now if i create this let me create

1:19:10

this table is created and you will see very interesting thing let's go here you see that

1:19:19

order stable is created okay now what i will do is let me create an entry user

1:19:27

user's this order stable is created and user's table is there let's create an entry in user's

1:19:33

table what do you think let's do an entry in user's table first insert insert insert

1:19:40

to users i want to insert let's say simply one comma tanish this is the user i have

1:19:51

and i can do second user as well first let me do this only only so far and i can say two comma let's see

1:19:59

two users now i should have in the user's table let's see user's table has two data that is completely fine

1:20:08

now you will see the magic let me make an entry in order stable insert into

1:20:19

order stable we want to insert values now if you go to order stable we want to

1:20:27

insert what id amount and user ID I can see this is order ID 1 amount is 101 and placed by user ID 1

1:20:36

let me make an entry and show you entry is done let me reload this

1:20:40

now very interesting thing if you see this is the orders table right

1:20:48

order ID 1 amount is 101 we placed by user ID 1 do you see something arrow here everyone

1:20:55

do you see an arrow if you click this arrow it will take you to the user which plays

1:21:02

this order in which row it is connected to you see that if i

1:21:06

click this it is showing you this row is connected to this user you see that this is coming

1:21:11

because of foreign key there is a relation here now do you understand this that users and orders

1:21:17

tables are connected with each other and it gives you a very beautiful feature let me show you

1:21:23

if i create an order order id 2 amount 201 do you what do you think will happen with this

1:21:30

insert will it work what we are trying to say we are trying to say order id

1:21:36

to amount 201 placed by a user whose ID is 3 this 3 means placed by a user whose ID

1:21:44

is 3 is there any user with ID 3 do we have any user with ID 3 i we don't have that that's

1:21:53

where it will help you also it will give you an error let me show you you see that that's how

1:21:59

helpful foreign keys are it says this column is connected to a column which does not have even order ID3

1:22:06

a user ID 3 how you can connect that that's why it's very very important foreign keys

1:22:11

otherwise if you don't connect them anyone can say 3 here even though 3 user does not even exist

1:22:16

that's the wrong data and here database is giving you an error that's why foreign keys are very

1:22:22

helpful are you clear let me know everyone is everyone clear in this example it's called one to many

1:22:30

example one customer one user is connected to multiple

1:22:36

orders one user to multiple orders right is everyone clear please do let me know

1:22:44

one user to orders correct hamanshu one user to multiple orders

1:22:50

anyone has any doubts in this take your time and let me know

1:22:53

any here has any doubts

1:23:07

take your time and let me know one to many examples this is the example that i gave right

1:23:14

hamanshu this is one too many example only right what will happen if we select orders table you

1:23:20

you will get orders data only you will not get that is a separate

1:23:23

this is a whole topic called join in which you join the two table and get the output that is a

1:23:28

separate class all together right now if i do select on orders you will get orders table data only

1:23:34

let me show you select star from orders you will get orders table data only you see that elvin

1:23:44

how to combine two tables and get the data there is a separate concept called joins we will have a

1:23:49

separate class on joins that will be a separate class on joins that will be a separate class

1:23:53

let me know everyone

1:23:59

what is a real life this is a real life example admin is not a real life example that is not

1:24:07

one entry is connected to multiple entry that is one to many not one admin can do multiple

1:24:13

operation that is not that is not database right imanshu that is one api can do multiple that is one

1:24:19

to many in an API right in database right in database one record

1:24:23

is connected to multiple record that is one too many are you clear let me know

1:24:34

are you clear on this you man shu everyone please drop your questions in qna

1:24:53

like admin you caught at both back and deb different behaviors yes it's a separate thing

1:24:58

altogether now let me know everyone now let me know everyone now let's take an example of many to many

1:25:11

can you can you can you can you imagine any example of many to many right now we saw one to many

1:25:18

many and if you do oppose it will it will become many to one but what is the example of many to many

1:25:23

can you think of any example many to many relationship we saw one to many

1:25:32

that same itself you can do opposite many many many to one just do opposite right now we

1:25:39

are doing user to order you can do order to user right can you think of many to many

1:25:44

many let's see anyone can think of many to many please drop your questions and Q&A

1:25:53

any examples of many to many can anyone think of it take your time and let me know if you're

1:26:02

able to think of many to many see in which cases many to many make sense

1:26:13

there's a very good use case

1:26:23

explain when you go to college each student can enroll in many courses everyone

1:26:31

what do you think each student can enroll in many courses so you will have a student table

1:26:40

in which you will have student data this is student ID student name student name and let's say student gender

1:26:58

and then you will have course table in which you will put all the courses which university

1:27:05

has to offer what all courses are supported in university the university the course ID

1:27:09

course name and course how many months it will take so let's say there is

1:27:22

two students one tanishk male second uh maybe shawani female and there are three courses present in the college

1:27:39

course is a complete physics course complete mathematics course complete

1:27:47

mathematics course and completes economics course it takes four months four months six

1:27:56

months now tell me how will you represent let's say tanishk want to enroll in

1:28:01

in course number one and course number three how will you represent that first of all how would you

1:28:08

represent that data tanishk want to enroll tanishk has enrolled in the university

1:28:12

and want to enroll in two courses one and three basically physics and economics how will you

1:28:18

represent that any ideas everyone let me know what do you think how will you represent even that

1:28:30

folks you understand the problem right let's shawani want to enroll in all three courses

1:28:35

where will you store this data how will you store this data how will you store this data

1:28:38

Data. Student ID 1 with course ID 1 and 3. But how will you store this?

1:28:45

In DV, how will you store? Let's say if I create a new table in which I will store, then how will I store that student ID this?

1:28:56

Course ID 1, course ID 2. Will you store like this? That Tanishk is enrolled in course ID 1 and 3. Will you enroll in

1:29:08

the second student shewani needs three courses so will you add third column now course ID3

1:29:14

like this will you add like column this for other students it will be empty that's where you will

1:29:19

create a table of many to many relationship like this you will create like this a many to many

1:29:27

relationship just a mapping table student ID course ID that's it's it's it's it

1:29:38

that one student ID has enrolled in one course ID, one student ID has enrolled in third

1:29:46

course ID second has enrolled in one second has enrolled in all the courses so you will

1:29:53

have second student ID as enrolled in two course ID second and three ID. Now can you let

1:29:57

me know everyone from this table can you let me know Tanich has enrolled in which courses

1:30:08

courses, what do you think? Can anyone tell me from this table?

1:30:16

Tanishk has enrolled in which courses? Correct. Tanishk has enrolled in course ID 1 and 3, which is

1:30:21

physics and economics. You see that? This is Tanishk user ID, right? Tanishk has enrolled in

1:30:28

physics and economics and Shavani has enrolled in all these three courses. This is called,

1:30:35

you see that many entries here many to many Tanishk one entry itself is many times coming here so there is

1:30:45

no primary key in this table do you agree there's no primary key in this table because this is a

1:30:50

many to many relationship now do you understand that two times one is related to one and three

1:31:00

you see that many to many on this side also many this side also many

1:31:05

Now does it make sense? Let me know. Everyone is clear.

1:31:11

Going to questions, when we use join, then do the tables are connected with foreign keys?

1:31:16

So we get the result of applying join. Maybe yes, Nishan. Joins are using foreign keys only.

1:31:22

I will explain you in the joins class. Joins works on foreign keys only.

1:31:26

Joins join the two table using the foreign keys.

1:31:30

Many records in one can be related to many records in another.

1:31:33

Karash Halini, I hope you are clear now.

1:31:35

What type OLX will be using?

1:31:37

What do you mean by that?

1:31:39

What type would OLX be using?

1:31:42

What is your question?

1:31:46

Let me know everyone is clear with this.

1:31:48

This is called many to many relation.

1:31:52

What if we have different students with same name?

1:31:55

That's why we are using ID.

1:31:57

We are not using student name Tamanna. You see that?

1:32:00

That's why we use student ID.

1:32:01

Student ID will be different.

1:32:02

Tanish can, Tanish Gupta and another

1:32:05

Tanish Gupta will have different user ID, right?

1:32:08

Let me know the manna.

1:32:11

Okay.

1:32:14

Folks, if you will not ask questions in Q&A, if you are asking question in chat, I will ignore those

1:32:19

questions.

1:32:19

I have told this multiple times now, almost 100 times now.

1:32:23

Can't repeat it any further.

1:32:25

So if you keep dropping your questions in chat, it will be ignored.

1:32:30

Hewanshu says, is it mandatory that many-to-many relation does not contain primary keys always?

1:32:35

You can, but there is no point of that, Himanshu.

1:32:39

I can create, for this table itself, I can create a this table ID, right, which I can

1:32:45

give unique.

1:32:45

But what you will do with that?

1:32:47

This table can have their own separate ID.

1:32:50

You can make this a primary key.

1:32:51

Correct, Himanshu?

1:32:54

You can do that.

1:32:55

But only when you need it, right?

1:32:58

Because how will you query this data?

1:33:00

The query in general will look like.

1:33:02

Tanishk has enrolled in which course.

1:33:04

That means you will query on.

1:33:05

student ID and course ID.

1:33:06

You will never query directly using this ID which you are creating a primary key.

1:33:10

Correct, Hamanshu?

1:33:11

Yes.

1:33:13

Now everyone let me know, folks.

1:33:15

Anyone has any doubts?

1:33:20

Take your time and let me know if anyone has any doubts?

1:33:26

Did you understand relations?

1:33:29

Using these relations, there will be a separate class that we will have called joins.

1:33:34

We will join.

1:33:35

two tables and then query the data.

1:33:37

Right now you are doing visually right.

1:33:39

How you are querying the data?

1:33:41

Can you tell me Tanish is enrolled in which all courses?

1:33:44

You are manually seeing through eyes and then telling me how you will do it using SQL.

1:33:48

That will be a separate class altogether.

1:33:51

That will be joins class.

1:33:53

Is everyone clear on this?

1:33:55

Please do let me know everyone.

1:34:00

Anyone here has any doubt.

1:34:01

Take your time and let me know, folks.

1:34:05

But still we will be using one to many relationships, student table link to details table,

1:34:12

details table link with course table, both are one to many.

1:34:16

Elvin, sorry, I did not understood your question.

1:34:18

What is details?

1:34:21

This table is many to many, right?

1:34:23

If you see, in this table, what is the relation you see that, Elvin?

1:34:28

What is the relation you are seeing?

1:34:31

One student entry is multiple time.

1:34:35

That is map to many courses, right?

1:34:38

One student entry many times are mapped to multiple many courses.

1:34:44

If there would have been one student to multiple, see, say only one student entry here.

1:34:49

If there would have been only one student entry here and map to multiple courses, that will be one to many.

1:34:54

But one itself is coming many times.

1:34:56

You see that, that is many to many courses.

1:35:01

It will know, Alvin.

1:35:03

In the previous, if you see.

1:35:05

Here, if you ever see the orders table that we were creating, one user had one entry, one at a time,

1:35:10

map to multiple orders.

1:35:12

You see that, Elvin?

1:35:14

One user map to multiple orders.

1:35:16

That one user was only one.

1:35:18

It will never repeat.

1:35:19

Correct, Alvin.

1:35:20

Was any user ever repeating here?

1:35:23

No, because one entry map to multiple orders.

1:35:26

Now, here you see that one student, there is no one student.

1:35:30

The student still is repeating, that means many students map to many courses.

1:35:35

Are you clear, Elvin, let me know?

1:35:38

Is everyone clear on this?

1:35:40

Please do let me know, folks.

1:35:45

Cool.

1:35:46

This is called relations.

1:35:47

That's why this whole database is called relational database,

1:35:52

because you can represent relations between table like this.

1:35:55

And relations are very important.

1:35:57

That's why you are able to organize data into multiple, multiple tables.

1:36:00

And when you want to query, you can connect these tables together using the concept of join.

1:36:05

which we will learn later using the concept of joins you can join these tables and get the data

1:36:12

now anyone here has any doubts do let me know everyone

1:36:21

so what all things we have cleared out how to create tables what are the types of columns we can create

1:36:29

what constraint we can give on every column constant is very important i hope you practice that

1:36:35

how to create table what type of columns what type of constraints we can give then how to

1:36:41

select data using where clause i have everyone is clear with the where clause that in where clause you can add

1:36:47

multiple conditions multiple type of conditions you can add at the same time you can add multiple

1:36:53

conditions different types of condition in where clause then update then insert data how to insert

1:37:00

data in a table how to update any row any column that you want to update that you can do

1:37:05

then we understood how to delete that's the important part then we understood

1:37:10

what is relations with the table one too many many many in the next upcoming classes we will also

1:37:16

learn how to use these joins to join two tables right because we don't want to learn a topic

1:37:23

just because even if we don't use the topic then what's the point of learning so i will show you that

1:37:29

how why did we even learn these this is the complete whole relations right that

1:37:35

that's where you will understand the the relations that you learn will help you to join

1:37:40

two table and then the query will become much more complex queries are coming up once you start learning

1:37:45

joins that is a set next class altogether in the next week we will be having a class the first class

1:37:51

will be joins and then we'll understand very interesting things coming up which is called aggregate

1:37:57

functions let's say if someone give you a table and say tell me how many students

1:38:05

have scored more than 95 how many students have more than 80 in the same query i want to

1:38:11

ask this question tell me how many students in the same query give me this result how many have

1:38:17

scored more than 95 how many have scored more than 80 how many have scored more than 70 in the same

1:38:22

query give me this result so all of this comes in aggregation that will be a next class we will learn

1:38:28

about aggregation that how do we aggregate data multiple data into one answer like this that's the

1:38:34

aggregate function we will learn those two classes the next two classes are very important

1:38:38

but those two classes will not make any sense if you have not practiced these two class of this week

1:38:48

the previous two class of the previous week if you will practice that then only because those classes

1:38:54

are itself called advanced as well those comes in advanced part where you learn joins and aggregate

1:39:00

so please do practice fundamentals then only advance will make sense

1:39:04

also once we cover the next two class then we will start integrating the whole database

1:39:10

with our fast API server that is also pretty interesting once we cover those two class we will

1:39:16

integrate our database with the fast API server that we created in the previous classes

1:39:22

very interesting classes for so i hope everyone do practice that please do the fundamentals

1:39:27

practice and then it will be very fun to learn okay cool now anyone

1:39:34

has any doubts in any of the concept i think we learned a lot today did you enjoy a database

1:39:39

folks let me know did you enjoy the learning okay cool so let me share this and just give me a

1:40:04

things that we wanted to cover today if you see these are the learning objectives that we

1:40:09

had update commands delete commands using wear explain one to many and many to many relationships

1:40:16

how to use wear in all the operations this we have already seen actually right how to use the

1:40:22

complete wear operations how to modify like how to combine multiple conditions in the where

1:40:28

clause that we have already seen in the select commands the link for the excel later all let me share

1:40:33

that if i can create the link for that can i share okay yes this is the

1:40:47

excel you draw link everyone can if you want you can see this okay okay i hope you enjoyed the class

1:40:56

i think we can start with the poll debu and then we will start with the quiz

1:41:06

books we have launched the poll if you enjoyed the class please do let us know by participating in the

1:41:13

poll take your time it's a one-click feedback poll so if you are enjoying classes to share your

1:41:19

feedback in the poll folks i hope everyone enjoyed the class do let us know you let us know

1:41:26

know in the feedback.

1:41:56

us know your feedback focus and if you have any doubts.

1:42:10

you have any doubts that also you can ask.

1:42:26

okay i think everyone is clear then

1:42:38

cool i see a couple of students are still yet to left the feed fill the feedback form

1:42:46

so if everyone can fill it that would be helpful

1:42:52

okay i think everyone has filled it cool thanks let's start with

1:42:56

the voice then over to you dapu thank you sir thanks for the session uh can you please

1:43:10

quickly join the mente middle we'll start the quiz

1:43:26

okay last one minute i can wait and then we start

1:43:56

let's start with the first problem shipment and there you go

1:44:26

So the question was which SQL command is used to modify existing records in a table

1:44:32

right so it should be update command right perfect and here is the quiz leader board

1:44:43

board

1:44:45

take it now let's go with the next problem segment

1:44:52

so here is the next question on

1:44:56

screen.

1:45:08

Okay, so the problem question was what happens if you execute

1:45:22

if you execute an update statement without a wire clause right so it is actually a risky

1:45:32

statement always try to avoid to like run the delete or update

1:45:41

without wire clause right so the correct option should be all records in the table are updated

1:45:52

Okay, here is a quiz leader code.

1:45:59

Next question. And there you go.

1:46:07

Okay, spell command is used to remove existing records from a table.

1:46:22

Okay.

1:46:23

So the options were remove, drop, delete are clear.

1:46:35

So we have a query called delete right?

1:46:38

Right.

1:46:39

Here is a little good.

1:46:45

Next question.

1:46:49

Next question.

1:46:50

What does a one to many relationships mean in a database?

1:46:58

Okay.

1:47:16

So the correct answer would be one record in a table can be.

1:47:19

a table can be related to multiple records in another table, right?

1:47:24

Okay, perfect.

1:47:26

All of you guys are correct.

1:47:28

And here is the later about.

1:47:32

Next question.

1:47:44

Which query retribes employees whose salary is greater than 40,000?

1:47:48

Okay, everyone voted? Yeah.

1:48:02

Okay.

1:48:04

So select star from this are the same, you can see this both the queries, right?

1:48:11

And the employees should be the employee stable.

1:48:15

And here you have the wire clause, right?

1:48:17

loss, right? So where the salary is greater than is 40,000.

1:48:24

So we have the difference between having and where and we'll learn it, I think, in upcoming

1:48:31

sessions. And here is the final leader put.

1:48:38

Nishand is today's unit.

1:48:47

Cool. If you guys have any questions or anything you want to ask, please put it in chat.

1:49:00

Else we can end the session here.

1:49:02

Thank you so much everyone for joining in.