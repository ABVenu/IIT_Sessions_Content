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

Thank you

5:00

Thank you

5:30

Thank you

5:32

Thank you

5:34

Thank you

5:36

Thank you

5:38

Thank you

5:40

Thank you

5:42

Thank you

5:44

Thank you

5:46

Thank you

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

Thank you.

9:48

Thank you.

10:18

Thank you

10:48

Thank you

11:18

Thank you

11:20

Thank you

11:22

Thank you

11:24

Thank you

11:26

Thank you

11:28

Thank you

11:30

Thank you

11:32

Thank you

11:34

Thank you

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

Yeah, guys, we can wait for everyone to join and then we can start.

14:13

I think the voice is clear to everyone, right? Can you hear me?

14:22

Yeah, let's wait for everyone to join and then we can get started.

14:36

I have uploaded the today's class code also.

14:46

So you can see this that code is present here.

14:49

You can check out this particular repository and this code we will try to do today.

14:54

That particular thing we will do.

14:56

Yeah, we can wait for other folks to join and then we can start.

15:06

Thank you.

15:36

Thank you.

16:06

Can you see me? Yeah, guys, can you see me?

16:36

Yeah, I think let's start. So yeah, Purajan for me it is working. So if you fix your setup, it will work for you as well.

16:45

So yeah, you can try that and you can ask that out in the other sections and other sessions started there.

16:50

You can ask Maasai team to schedule other sessions for that part and then we can do it because like for many of us it is already working.

16:58

So yeah, I think we can get started.

17:00

So let's start with one by one. We can discuss all the things that we are having today.

17:05

that we are having today and yeah let's get started so yeah first what we will try to do is we will

17:11

start with what is the agenda for today you will see this that what we will try to do is we will try to do

17:16

we will try to create a complete pipeline that is there so that particular pipeline of rag we will

17:21

try to see today whatever we have discussed in the last class kind of similar code only we will try to do

17:27

so you can see in the last class we wrote this kind of code that was present in which you can see this

17:32

this that we were like seeing a basic structure of rack today what we will try to do is

17:38

today we will try to see a complete pipeline of rag so you will see this that i've already

17:42

written the code you can check out the code on get up also like for example if you open this particular

17:48

repository you can see here coding examples are present inside these coding examples multiple

17:54

folders are there in one of them you can see the current code base is already present so you can

17:59

definitely check it out so yeah one by one i think we can do that

18:02

part and then we can go ahead so let's get started so we can see here first of all like if you

18:09

see like since it is a big code it's a 400 line code that is there that is why i've already written

18:15

it if i write it in the class like in the entire class i will be just writing the code so that is

18:21

why i've already written this particular code that is there so yeah one by one let's try to

18:25

discuss this code in detail so whenever you are having such a big code how you will try to read it is you

18:32

will try to actually ignore all the functions that are there you will just scroll down and you will go

18:38

to the main function that is present so you can see here everyone can go to line number 4004

18:44

currently you can just focus on what we are discussing so i think everyone is able to see my screen right

18:50

and everything that i'm writing on the screen is clearly visible so can you focus on line number

18:55

4004 so you can see this that here we are creating a model what do you think which is a free model that we can use

19:02

for this particular program whenever we are building any particular rag system generally

19:08

what is a free embedding model that we are having guys we can see this that we can get a hugging face

19:14

model like we can get a bg model that is there which is provided by bging artificial

19:19

like intelligence institute that is there and you can see this that we can use that particular model

19:25

for creating all the embeddings and all so if you see here that what i can do is i can like prep

19:32

where like put the model name here so if you see the model name value is bg small and i am creating

19:38

this particular model so we have written some like this is a inbuilt function that is there which is

19:43

create the model which will create the embedding model that is present so you can see first time

19:48

trying to do basic setup i'll even write down the steps that are there so that you are able to relate

19:54

so you can see the first step is that we are trying to load the model and then what we will try to do is

19:59

we will try to actually see this particular part let me just go to this part we can keep on

20:05

writing here also till now we can see that first what we are doing we are creating a model or we can say

20:14

we are doing the setup of the model that is there in the next step that in the next step what we

20:20

will try to do is we will try to actually set up the chroma db so you can see we can call it as a

20:26

a section that the first section is what the first section is set apart the first set up will

20:32

be embedding model the second section will be chroma collection what we will try to do is

20:41

we will try to create the entire chroma db this chroma db why we are creating in order to

20:48

store the embeddings is this idea clear this part everyone is able to understand

20:56

still here are you able to relate so you can see before actually starting the class if i just

21:02

show you that what actually we have covered till now like in all the classes that we have discussed

21:09

till now we have seen what are memory we have seen different different tools we have seen the

21:14

rack part that is there we have discussed the theoretical part of embeddings and everything

21:18

today we are trying to see the entire rack pipeline so you can see this that using this rack pipeline we can

21:25

later on build a lot of AI agents we can see this that how are AI agent it will actually try

21:30

to use the complete retrival system so whenever we are building any AI workflow any AI workflow any

21:36

AI automation tool or anything related to AI you will see this that generally the retrieval part

21:43

will be handled with the help of RAG system so that rag system we are building today so you will

21:48

see this that later on as we go whenever we are using any agent whenever we are building multi-agentic system

21:54

whenever you are making your final project you will see the retrieval component will be done with the help of

21:59

rag so today we are studying about the rack pipeline that is there is that part clear this part

22:05

are you able to understand guys this part are you able to relate or not

22:15

so we can see here like currently what we are doing in this particular program one by one let's

22:20

talk about you can see first i am doing this thing that i have done

22:24

them the setup part in setup i am doing two steps what are the two steps the first step is

22:29

creating an embedding model the second step is creating a chroma collection that is there the

22:34

third step will be that we will build the entire knowledge base building this knowledge base

22:39

means what that what we will try to do is we will try to actually add all the necessary data so you can

22:46

see the third step the second main step that we are having is building the knowledge base for building this

22:53

particular knowledge base what we will try to do is we will try to do the first thing that we

22:58

will put all the documents that are there whatever raw data we are having we will try to put we will see

23:03

this that whether chunking needs to be done or not do you remember chunking that whenever we are having the

23:09

raw data we will try to clean that particular data we will try to normalize that data once the data is

23:15

normalized then we will try to divide the data into different chunks and then we will try to do or like something

23:21

called as embedding so currently we are not sure like we will see the data and then we will

23:27

decide that whether chunking is required or not so we will see that part so you can see the first

23:32

main step that we are having here is the setup part once this particular part is done we will

23:38

try to build a knowledge base for this we will be using the raw data that is present is this part

23:43

clear this part are you able to understand

23:51

chroma collection will store all the embeddings right we have seen this in the previous

23:55

classes that all the embeddings they are stored inside chroma db and we have even written a program

24:01

where we were doing the peak of the chroma db and we were able to see all the necessary

24:06

embeddings and ranking and everything that is there so yeah let's try to go to the next step that we

24:11

are having so we can see now i'll show you that how we will do everything we will load the files

24:17

we will chunk the data we will embed the data and we will store that particular

24:21

data so we will understand this particular function so you can see this function has four

24:26

stages so let's write down one by one all the four stages that are there the first stage is

24:32

that we are importing the raw data so you can see we will import raw data the second stage will

24:39

be what what will be the second stage guys we will try to chunk the data that is present so you can

24:45

see we will chunk the data once that particular part is done we will go to the third step where

24:51

we will embed the data so we will do the embedding and the fourth step we will we will

24:56

store the embeddings where we will store the embeddings we will store the embeddings we will

25:00

store the embeddings in this chroma collection that we have created correct i think this part

25:05

is clear so one by one let's start discussing all the four phases that are present so you can see the

25:11

first step is that we are having some policy documents so all these policy documents they are

25:17

present inside our policy folder that is there i'll show you where this policy

25:21

folder and wherever things are present so you can see inside this policy folder we will try

25:27

to load all the documents that are there i will create a policy folder in which i'll add the

25:31

necessary documents once that is done we will try to extract the name of the file and we will add

25:38

all the docs like we will add all the necessary docs that are there we will add the textual docs if the

25:44

doc is a PDF we will add it all the docs will be added up and you can see even we are printing those

25:49

documents that are present once we have done that we will go to the next part where we will

25:55

do chunking in chunking you can see currently i have made a default chunk size that i am

26:01

chunking with 100 words it's a fixed strategy that is there later on we can change this chunking

26:07

strategy to multiple other strategies that we studied in the class we can do something called

26:12

a cementing chunking we can do recursive chunking we can do paragraph based chunking we can do any

26:18

chunking currently since this is a small program that is why i am doing basic chunking that is

26:23

there i have written some code which will help me with the chunking part like what it will do is

26:28

it will divide all the words that are present and it will take 100 words 100 words one group or we

26:35

can say 100 words one chunk another 100 ones or another 100 words another chunk this way we will create

26:42

all the chunks that are there once all these chunks are created then then we will go

26:48

to the embedding part but before this what we need is we need all the documents that are present

26:53

so let me see where have we written the documents part i think we will need the documents and

26:58

everything so let me open a new window and move the documents very quickly till here this part

27:03

are you able to understand guys still here this part is clear

27:18

yes right all the documents will be this thing you will see this that all the

27:34

documents that we have written here right they will be the sample data so i'll just try to

27:39

copy paste the sample data so that we can use it we are chunking the words that are there like what we are

27:45

doing is as soon as we get 100 words we will put them

27:48

into one chunk as soon as we get another hundred words we will try to put it into another

27:53

chunk is that part clear you can write it with a year you can write it with a i you also

28:04

sahil hundred words in a paragraph right doc will have multiple paragraphs so as soon as we hit

28:12

hundred words we will keep it in one chunk that particular part we are doing

28:18

let me just paste the raw data i'm just pasting the necessary

28:47

raw data that is there once that is done then we can go so i am trying to generate the raw

28:53

data that we can use for this particular program so let it generate and then we can go ahead

28:59

till here this part is clear

29:13

so you have to install that particular module that is there right if anything is there right if anything

29:17

is not working then you need to install that particular part otherwise it will not work

29:47

you know

30:17

I'll push the data for you also so that you also so that you can find out the data for you also so that you can find out the data but if you see here in this particular part what I did is

30:39

I have created another folder which is policy documents inside which all the raw data that I have added

30:46

so that our rack can work without this the rag will not work right because we need some raw data that we will try to actually push so once we will run this program we will need this law data so i'll run the necessary command i'll just say git add i'll write git status first i'll just try to add this particular folder and i'll push this folder also so you can pull in the latest changes you can write git pull and the latest changes can be pushed up or even you can download the folder from there as well so if i have

31:16

right here so we can see that this latest folder is present here which will contain the raw data so if we see

31:32

rack pipeline this contains the raw data all these files contains the necessary raw data and i have added it with the

31:40

name of policy documents so if you see whenever we are doing this like

31:46

if you see this particular code that is present up uh i think this is the code right

31:53

so we can see here that in this code once this particular part is running let's try to see building

31:59

knowledge base so you can see this function is running what is this function doing it is loading all

32:05

the documents it will try to load all the documents from where it will load all the documents from the

32:11

folder path and what is the folder path let's check that we can see this that folder path that folder path

32:16

is written by default so probably i think you can see it's policy documents only and i have

32:22

created the same folder here policy documents so the exact folder name should be created then only

32:28

it will run otherwise it will not run so now it will load the documents properly it will load all the

32:33

files that are there once all the files are loaded it will store all the files once that particular

32:39

part is done then what we will try to do we will try to create chunking we will try to take all

32:46

all hundred words into one chunk once that particular part is done we will try to

32:53

index all the chunks indexing means that we will extract the particular row id the document and the

33:00

metadata we will call the embedding model that is there that embedding model will create all the embeddings

33:06

and then we will store all the embeddings that are there so till here only we will try to do

33:11

like first we will try to run only some part of the program so if you see i can go into my

33:16

main function and what i can do is i can connect i can comment everything like till building

33:23

knowledge base only i am putting and i'll try to run that part so that we can see our knowledge

33:28

basis building or not so i'll just go here what i'll try to do is i'll just type in here

33:37

python three so i cannot directly run it i need to find out the exact path the path is

33:44

coding examples inside coding examples it is present right so i'll write here coding example

33:49

or i can directly go to coding example also after that i'll go to the specific folder which is

33:56

rack pipeline inside this program is present you can see code dot pye is present i might have

34:03

to install multiple things in order to run the program like for example if you see here this

34:08

program requires roma dv sentence transformer grock dot env and pipe

34:14

so you can see this that this is python pdf in order to read the pdf starter there so i can

34:20

simply write a command pip install by pdf if my pip is not working then i can write the

34:29

same command using pip three so you can see this that it will install this particular part so you guys

34:35

can try both the commands you can try pip three also you can try pip install

34:44

Pi PDF and you can try pip3 install this once you have installed this you can

34:51

try running python 3 code dot ty if you are in the correct folder you will see this that it will

34:57

try to run if any error is coming we will try to fix that error that particular part we will do

35:03

so let it run and we can check if everything is working or not so you can see this that it has

35:08

loaded all the documents it has loaded four documents that are there it has indexed the

35:14

documents that are there and we can see this that the knowledge base is up and running till

35:19

here this part is here right guys still here are you able to understand this command you are able to do so

35:29

you can see this that currently i have commented so probably i can comment the code also for you like

35:35

and i can push it so what you can do is you can write here i'll just add here so that you guys can see

35:44

get add i'll just do git status get add code.py

35:53

so you can check out the latest code so once you have checked out the latest code you can

35:59

copy paste the latest code that is there make sure that you have the policy documents if you don't

36:05

have the policy documents then the program will not run so you will have all these documents that are

36:09

there i have pushed in the latest code where i have commented everything right now

36:14

so you can see all these things are commented only knowledge based building is present

36:18

is that part clear and now what is the command that i wrote for installing that pdf thing

36:24

like if pdfs are there then also it will work so what is a command for that if you are using pip

36:31

then you can write pip install p y pdf and if you are using pip 3 you can write here

36:37

pip 3 install p by pdf you can run both the things any one of them will work are you able to understand

36:44

much guys are you able to do this much or not

37:14

this can you try running it right now the building part is clear right right

37:22

right other people are you able to run it is this installation working for you guys this

37:28

installation working or not

37:33

guys this installation is working or not

37:44

sile in the folder i have added the raw data so if you see all these currently this is a main folder

37:55

rack pipeline it contains policy documents contain the raw data in which raw data have added and this

38:01

is the main rack program that we are writing correct it will not work without chroma db

38:07

sentence transformer groc everything you have to install so whatever we installed in the last

38:13

class that do you have to install apart from that you need to install pi pdf that is there

38:19

correct right i think harsall is able to run other people are you able to run it or not

38:27

chroma db you have to install properly right you can watch the last class recording that is there

38:33

and you can install that so you can see currently

38:37

here we are able to do like if i run the program again you will see this that this

38:42

particular thing will happen that you can focus on my output you can run it later on after the

38:48

class also currently you can see here that this kind of output will come if you focus and use the latest

38:55

program that the four documents have been loaded all these four documents they are

39:02

chunked once the chunking is done you can see here that chunks are chunks are chunked you can see here that chunks are

39:07

are created all these chunks they have been done with embedding also and all the

39:13

embeddings they are stored into where they are stored into chroma db where is chroma

39:17

db present if you try to see here this particular part right you will see this that here

39:23

chroma store is present inside which all the embeddings are there so we can even write

39:27

peak command and then we can see all the embeddings also till here this program are you able to understand

39:37

so if you see that we are loading the database right earlier this program or this

39:42

rag system is not having any data you will always import or load the raw data that is present

39:48

once you have done that then you will chunk the data then you will create the necessary

39:52

embedding and you will store all the embeddings is this part clear without data how can you

39:59

build rag without data we cannot build a rag system right

40:07

is clear till here this part are you able to understand

40:16

yeah we can wait one more minute and then we can start with the next part so you can see this that

40:30

two steps we have done till now the first step is that we have done the setup part in the setup part what we did is

40:37

that we created the bg model that is there we created a chroma store then we did

40:43

the knowledge base in the knowledge base what we did is we imported the law data

40:48

we chunked the data we created the embeddings and we are storing the embeddings

40:52

i think that part is clear till here is everyone able to understand

41:00

Pratig what is not clear in loading the data we are loading all the data that is present

41:08

in the raw files in raw file in raw file we can see right that this data is present all this data is

41:13

present here we are just loading that right is this thing clear to everyone

41:23

so this is raw data right raw data will always be given to us whenever we are building any rag system

41:30

raw data will be given to us so you can download directly this particular folder or you can clone

41:35

this repository and then use it is that idea clear

41:46

i am running the program in order to load the raw data right we can see here that if we go

41:52

here we have run this particular program right we are just writing a for loop we are picking all the

41:58

files that are present inside this point

42:00

folder one by one all these files will be picked and whatever data is present

42:05

inside this file that will be added into all documents this way we are loading the data

42:09

right what is not clear here this part are you able to understand

42:23

i think till here we are good to go so let's start with the next part that is present so we can see

42:28

here the next thing that we have done the chunking part we are currently chunking with the

42:33

help of 100 words whatever data is having 100 words will be one chunk next 100 words will be another

42:39

chunk next 100 words will be another chunk then we can see this that we are creating a policy like

42:46

once this all the chunks are extracted we are embedding all the necessary data this part we have already

42:52

seen in last two classes so you can watch the recording for that and then we are just inserting all the

42:58

embeddings into the chroma db so you can see once this is done we will be good to go

43:03

and we can see we will print that knowledge base is complete so again if i try to run it you can see this

43:09

that the four chunks that were present they are added and the knowledge basis up and running now what do

43:18

you think will be the next step guys what will be the next step now like if we have done till here then

43:28

what do you think will be the next step?

43:45

Correct, right, once we have done the embedding part, what we will try to do is, we will try to go to the next part.

43:50

In the next part, let's scroll down. And we can go to the main program. Let me show my BS code quickly.

43:58

So you can see here that if we go here to the next part, we will try to build GROC, GROC

44:05

we will need the API key. So API key, you remember right, in the last class I taught you how to add API key.

44:12

So if you see in my already an ANV file with API key is already present, so I can just paste that particular part here.

44:21

So you can see this that this already, do you remember that in the last class we created API key and we entered API key?

44:27

I told you to go on GROC platform, add your API key in your ENV file.

44:32

Same API key we will add here so that that particular API key will be used in this particular part.

44:38

We will try to extract the API key and we will create a GROC client.

44:42

So you can see this that this GROC will be used for generation purposes.

44:46

For generating the final data it will be used.

44:48

I think this part is also clear.

44:54

Guys, this thing are you able to understand?

44:57

remember the ENV part. So after that, you can see what I have done is I have created basic demo queries.

45:04

So these are the demo queries that I have written. The first demo query is that I received my phone

45:09

yesterday unopened. How many days I have to return it? This way I have written four queries that are there.

45:15

For each of these queries, what we will try to do, we will try to print the rag system. We will try to run the

45:21

rag system. So we have written the same kind of function that is there that we studied in the last class.

45:27

that particular function I'll go.

45:29

But till here, this part, you are able to understand the highlighted part that I'm showing right now.

45:36

Do you remember the ENV key? Do you remember creating Glock client?

45:40

You know, right, that GROC APIK, how do we get it? We get it from Grog.com. Do you remember that part?

45:48

So if you see here, we can see, we can go to this platform. We can go to Grog.com.

45:53

We can click on free API key. Once we click on free API.

45:57

We can click on create API key and you can type in any name and API will be created.

46:02

Do we remember this? Once we create the API key where we will paste it. So if you remember in the last

46:08

class we pasted it in the dot env file. So in dot env file we will paste our API that is there. So you can

46:15

create a dot env file. You can click on plus button and create it and then you can type in groc API

46:21

key equal to and you can paste it. So if you remember in the last class I showed you right that in this

46:26

format we need to create it. We need to create a new file. I can show you again that we need to

46:32

create a new file which is dot env. Inside this we will type the exact same thing that GROC

46:39

APIE equal to and we will paste the API key. Is this thing clear? Currently focus on what we are

46:46

discussing right? Don't focus on the errors that you are getting else you will not be able to

46:51

understand everything that is there. Till here this part is clear.

46:56

Till here are you able to understand?

47:00

So you have to paste the documents correctly into the proper folder.

47:05

If your folder should be policy underscore documents, inside which all the folder should be present.

47:12

If you don't do that, then the program will not work.

47:15

So do you know how to clone a repository?

47:18

Can you clone the entire repository and then open it in Visual Studio code?

47:22

You can watch the GitHub code.

47:24

You can watch the GitHub section.

47:25

the GitHub section recording in the GitHub section recording we discussed it how to clone the repository.

47:30

You have not done the revision before. Do you remember we had a say like class on GitHub? Do you guys remember that?

47:39

So we can see this right that in that I showed you how you can clone a repository as well. So if you clone the repository, you will get the documents.

47:49

Otherwise with this code, all these four documents will be required.

47:54

Correct.

47:55

Yeah, this particular command in terminal you can run and you can open that particular folder that is there, that part you need to do.

48:02

Otherwise it will not work.

48:06

Till here, program is everyone able to understand running part you can do it after the class also.

48:11

Currently till here the program meaning is clear, right?

48:16

Guys, program are you able to relate?

48:25

see here this particular part that we can create a GRO client. We can add all the demo queries that are there.

48:31

For each query, we will try to run it with the help of rag. In the rag, what we will do?

48:36

We will retrive the policy chunks that are there. We will print the retrieval chunks,

48:41

and then we will generate the grounded answer as we did.

48:44

For generating the grounded answer, what we will do, we will write a system prompt.

48:49

So what's the system prompt? We will say this. If you remember, this is the same part.

48:54

that you are the shopping customer support assistant try to answer everything from the context block this is the user question

49:02

and this same prompt we have written in the last class same prompt I'm writing right now also

49:07

this particular prompt will be given to GROC

49:10

GROC will get necessary chunks

49:13

GROC will get the necessary chunks that are present or retrieved from here

49:18

those necessary chunks will be sent to GROC

49:21

it will get the user query

49:23

it will get the necessary chunks and it will try to generate a final answer using the prompt that is present

49:29

once we do that particular part you will see this that we will write a system prompt we will get the resources

49:36

we will get the response once we get the response we will try to print that particular response that is there

49:43

and you will see that will be our final answer so now if i just save this program

49:48

if i show you this particular part i'll just push this program also

49:52

So you can see I'll just add here code.py.

49:56

I'll say update content and I'll write here my email.

50:01

I'll just push it.

50:03

So once I push it, you can see my latest program is present here on the GitHub as well.

50:08

So if you see on the getup part, the latest program is up to date.

50:13

Once we see this particular program, you can see this is a program that we are having.

50:18

Once we have this program, what particular thing we can do?

50:21

we can do here this particular part that if I try to run it like we can say here we can write here

50:29

Python 3 code.p. So let's try to run it and see the output. So you can see for everything we are able to get the responses. Let's try to understand them. I'll scroll up. You can see that you can see for everything we are able to get the responses. Let's try to understand them. I'll scroll up. You can see the

50:51

that till here we did it in the last part, that we were able to load the necessary data.

50:56

Now what we are doing, we are just retrieving the necessary data that is present.

51:01

How we are detriving the data?

51:03

My question is I received the phone case.

51:05

You can read the question here also.

51:07

We are finding out the rank one, which is matching.

51:11

So you can see this is a matching one and this is a text that is present.

51:15

This is another matching one which is matching.

51:18

This is another matching one.

51:20

And the final.

51:21

answer is, according to expert, I think this spelling is wrong.

51:25

Like, I think it should be expert, right?

51:28

GROC currently very bad model we are using.

51:31

That is why spelling with Stiggett has done.

51:33

But we can see here according to expert one,

51:35

since the item is unopened, you have seven days

51:38

from delivery date to raise a return request.

51:41

So we can see this that according to, I think,

51:43

this thing, we can return seven days.

51:45

So it is telling in the correct manner only.

51:48

The response that it has generated in correct manner.

51:50

manner.

51:51

If I see the second question, the second question is,

51:54

will express shipping reach my address by tomorrow?

51:59

So you can see that the delivery part it is able to match the best.

52:03

That is why we can see this that the final answer is

52:06

express delivery is paid and arrives in one to two days in metro cities.

52:10

However, there is no guarantee express shipping will reach by tomorrow.

52:14

So this exact answer it has given based on this particular policy that is there.

52:19

You can see here it does.

52:20

is written express delivery is paid and it arrives in one to two days so there is no guarantee whether it will come in tomorrow or not correct answer it is giving

52:29

same thing we can see that if i run it for this particular part we can see my wireless earphones stopped working after 10 months is the repaired covered

52:38

so you can see this is that this is a policy this is matching very closely the distance is bare minimum that is why the final answer is something like this

52:48

same way we can see this that i think if i see the next part that if i have a defective kit

52:55

will refund by a you like will refund reach by a upi so you can see refunds are credited after

53:02

like these many days cash on delivery are refunded to original upi or bank account

53:07

so this is the closest one and the final answer is again this that refund for cash delivery are

53:14

coded like they are given within seven to five business days

53:17

yeah so this response is coming up after warehouse verification is done so i think this is good

53:23

like these responses it is generating and it is able to answer this particular part now i'll just

53:30

i have pushed the latest program so in this latest program we have just built same rack pipeline

53:35

that we built it in the last class so if you see only thing is that i have changed here is that i have

53:42

built a knowledge base all this knowledge base where we are getting we are getting knowledge base from

53:47

all the files that are present all these files are present in this particular part so

53:52

this part you need to understand that all these files they are picked up one by one they are read

53:59

chunking is done embedding is created once chunking and embedding is done then we can see we are

54:06

trying to retrieve the data for retrieving the data what i am trying to do i am trying to find out

54:11

the nearby chunks that is there currently top k is set to three by default if i see here all

54:17

also you can see top three ranks we are getting once we get the top three ranks then what

54:22

we will try to do we will try to print all the ranks so you can see distance everything we are printing

54:29

we are generating the grounded answer with grok so if we open our grok also we will see this that

54:35

the API calls will start coming up in some time so if you see in last 30 minutes since my grok is

54:41

running i can see all the API calls in the dashboard also if i open grok i click

54:47

here on free API key you can see here API keys are present and dashboard is present

54:52

in this dashboard after some time once you have run the rag like after 10 15 minutes you will see

54:58

such API calls will also start coming up so you can even see that particular part and you can see

55:04

yeah prompt also we can see once we can see this is a prompt that we are writing and we can see this

55:11

is a final response that we are getting is this part clear

55:17

yes right it is that i can ask you to fix it i think probably there is a spelling

55:25

mistake that is there three one three me can't clear you can see this that where three one three

55:35

yeah i think here you can see that i have written a wrong spelling mistake no policy exports

55:42

retrieved what is this word i think that

55:47

only llm is generating okay expert it it basically means a short piece of text

55:54

that is there so expert is not that expert that i was thinking it is actually a short piece of

56:00

text yeah so actually uh i think it is writing in the correct manner it is not making a mistake

56:07

i just checked on internet it's a correct word only so it is writing the correct manner because

56:13

we have written it in prompt right that is why it is giving this

56:17

format got it right so you can see in the prompt since this part is written that is why

56:22

it is doing it if our policy contains it then only answer that particular part it is not

56:28

generating everything by itself it is generating everything from the policy

56:33

guys this program are you able to understand it is pretty similar to whatever program

56:38

but you can see that how now you are able to understand how to read a big code that first of all

56:44

you will go to the main function you can see the main function you can see the main function

56:47

is create embedding model so this part of code everyone has understood this are you able to

56:54

understand yes or no guys this part are you able to understand now we can see the next part is what

57:05

we are setting up the chroma db same thing we have written that we will create a chroma client and we

57:10

will create a collection this part we are writing from the last two classes that are there in both the last

57:15

classes we have written this thing then we are building a knowledge base we discussed all

57:20

the steps in detail that we will load all the documents that are there once we loaded we will create

57:25

the necessary chunks once chunks are created we will try to store all the chunks we will create all the

57:30

embeddings and we will store them once that is done our knowledge base is created this part are you able to

57:37

understand guys this part are you able to understand or not

57:45

Till here are we good to go?

57:50

Can you try running this program once and then we can probably discuss it?

57:55

Are you able to run the latest program?

57:57

So for running this program you need two things.

58:00

The first thing very important is policy document folder should be present in the same place

58:07

where code.p.i is present.

58:10

Remember that particular part.

58:12

The next thing is that you should have installed this particular

58:15

part. PIP install p.p.3 install p.p.p.3 install p.d.f. So you can download this folder

58:23

or create all the files like I have created. You can create one by one all the files as I

58:28

have created in the policy documents. That particular part you can do. If you are not able to

58:33

download and move it, then just create a folder with exact spelling correct. Policy documents,

58:39

create all these files and copy paste whatever is written. Even that thing you can do.

58:45

Anyone who is able to run the program and successfully able to execute it?

58:51

Here, 230 is a function that Bahrain we have created, right?

58:55

It will do three steps. It will first load all the documents that are there.

58:59

Once all the documents are loaded, it will chunk the documents.

59:03

Chunking means dividing the data into different, different small groups.

59:07

So here we are grouping the data with 100 words.

59:10

First 100 words in one group. Second 100 words, another group.

59:14

Another 100 words.

59:15

another group this way. And then what we are doing is once chunking is done,

59:19

we are trying to create all the embeddings and we are storing all the embeddings.

59:23

Is that part clear?

59:29

Guys, still here are you able to understand it or not?

59:45

so chunking we have done basic in the last class we did not do a chunk right if you remember in the last program that we wrote already chunk data we were putting putting this time we are putting different data right so if you see this

1:0:14

If you see this particular program already data was present in chunk format.

1:0:19

So I did not do any chunk.

1:0:20

I just picked one thing which is one chunk, second thing another chunk, second thing another chunk.

1:0:25

In this program, Rakesh, we are trying to divide the data into 100 groups, right?

1:0:30

Like not in 100 groups, like once 100 words are done, then it is one chunk.

1:0:35

That part are you able to understand?

1:0:37

So you have to install sentence transformer, right?

1:0:41

Pratik.

1:0:42

Once you install it, then only it will work.

1:0:44

So if you see all the things that I have written here, right, you need to install one-by-one chroma-db, sentence transformer, groc, dot env and pi PDF.

1:0:54

All these things if you have installed, then only the program will work.

1:0:57

Otherwise the program will not work.

1:1:02

First of all, how many people are able to understand the program now?

1:1:06

Program are you able to understand?

1:1:09

Anyone who is able to run the program, can you let me know?

1:1:13

let me know. Have you run the program?

1:1:17

Ajya, are you able to run it?

1:1:20

Harshal is able to run other people. Manish is able to run.

1:1:25

Mayur is able to run.

1:1:27

Rakesh, you are also able to run.

1:1:31

Have you installed everything, Rakesh?

1:1:33

Vareen internet connection should be fast.

1:1:38

Then it will install.

1:1:40

Other people are able to run it.

1:1:42

Program is clear, right?

1:1:46

So once again, let's try to discuss all the things that are there.

1:1:49

Till I think knowledge-based part we have understood.

1:1:52

The next part is creating a GROC client.

1:1:55

Inside the GROC client, what we have done is, we are importing the API key.

1:1:59

Why this API key is important?

1:2:01

Because if you remember to connect with GROC, right,

1:2:04

like whenever we need to connect with GROC or any third-party application,

1:2:07

we need an authentication token.

1:2:10

That authentication token is nothing but to connect.

1:2:11

token is nothing but an API key.

1:2:13

So you can see GROC is a third-party application.

1:2:16

Since you need to connect with GROC, you need an API key that is present.

1:2:20

Is this part clear?

1:2:22

This part are you able to understand?

1:2:25

Same way we can see all these demo queries are there.

1:2:28

I have written one by one all the demo queries that are present.

1:2:31

Once we see all the demo queries, what we do is we are trying to run this particular part.

1:2:37

We are trying to generate everything with rag.

1:2:40

We can see this that.

1:2:41

we have retrieved the policy chunks that are there.

1:2:44

Once we retrieve the policy chunks, we are printing all the chunks.

1:2:47

So retriving part you are aware of, right?

1:2:50

Like the sentence is, when I will get my refund.

1:2:54

In the data part, we have some refund related sentence.

1:2:57

If you see this is an entire sentence, we will calculate the distance of both of them.

1:3:02

We will see this that, okay, this has some embeddings, this has some embeddings.

1:3:07

The distance will be calculated, which you can see in the terminal also.

1:3:10

also if you try to see here this particular program what we are doing is we are trying to

1:3:16

calculate that what is a distance of this line the user question with the actual return

1:3:22

policy that is there so you can see this that the distance is 0.48 that is why it is given rank 1

1:3:28

this is having again distance 0.65 that is why it is rank 2 based on all the chunks

1:3:34

LLM will read the customer query it will read all the policies that are there and

1:3:40

then it will tell me the final answer. Is this part clear? This retribal strategy, are you able to understand?

1:3:51

Where is this retribal part is clear?

1:4:05

So here you can see what we have done is, like let's say if the answer,

1:4:09

say if the answer is not coming from one of the rank like we are sending two three

1:4:15

ranks here we are sending top three ranks to the LLM if LLM is not we are not just

1:4:21

directly saying that pick from rank one we are sending from all the three ranks that are

1:4:26

present all these three ranks will actually help us understand that okay if there is a

1:4:32

overlapping answer that can be generated overlapping answer means that some information is

1:4:38

coming from rank 1 answer some information is coming from rank 2 answer some

1:4:44

information is coming from rank 3 answer once we combine them then we generate the final

1:4:49

grounded answer that is there this part are you able to understand this part is clear to everyone

1:5:08

also you are able to understand.

1:5:11

Till here guys are you able to understand the entire program.

1:5:27

Let me know if any doubts are there in the program.

1:5:31

So were in right, bro, did you not paste it?

1:5:34

Did you paste it?

1:5:35

Did you paste the folder that is there?

1:5:38

Is your policy folder present?

1:5:42

Like policy folder and program, they are present in the same place and ENV file is also present, right?

1:5:50

.

1:5:51

Yeah, we can discuss those doubts if your program is not running, but till here the program is clear to everyone.

1:6:03

Varine, are you able to understand the entire program?

1:6:08

Ndh, it is running, right?

1:6:11

Only a warning is coming, everything is running up.

1:6:14

You can copy paste the latest program where I have uncommitted this part and run that also.

1:6:21

Yeah, till here the program is clear to everyone, right?

1:6:24

What is the question, Raju?

1:6:29

So I'll help one person and later on other people can also share their screen and I can help you.

1:6:36

I can help you what is the issue?

1:6:38

So wherein, are you 100% sure, right?

1:6:40

You have done all the steps correctly, whatever I am saying.

1:6:47

Can you quickly share your screen, Maureen?

1:6:55

Can you share your screen?

1:6:57

Share Gana, screen, Vareen.

1:7:08

Guys, other people, what is it out in the program?

1:7:14

Program, other people are able to understand.

1:7:16

How many are able to run the program?

1:7:18

Can you write yes in chat quickly?

1:7:20

And everyone can see what you need this.

1:7:24

This way.

1:7:25

Policy doctor, guys.

1:7:28

I do.

1:7:30

There is so much noise on your end.

1:7:35

You are watching TV, I guess.

1:7:38

So probably just to minimize the terminal, right?

1:7:42

What is there?

1:7:43

I think copy paste you have not done correctly.

1:7:45

Click on cross in the terminal.

1:7:47

Terminal in the terminal.

1:7:48

Just scroll down.

1:7:51

Scroll, scroll, scroll, scroll.

1:7:53

Scroll.

1:7:54

scroll.

1:8:00

Main function to go.

1:8:01

You have done the command.

1:8:05

Scroll to.

1:8:08

You are running file.

1:8:14

P. Right.

1:8:16

Policy documents is correct.

1:8:19

Yeah.

1:8:20

And dot Envy,

1:8:21

click on a one.

1:8:24

So now what you can do, like open the terminal.

1:8:34

Terminal is going in which part?

1:8:38

This is wrong, right?

1:8:39

Type CD and go to rack pipe, like rag pipe.

1:8:45

You have written the folder name as ragpipeline.

1:8:49

Right?

1:8:50

That is incorrect.

1:8:51

How will you do that?

1:8:52

Just type here.

1:8:53

Yeah.

1:8:54

pipeline.

1:8:56

p.y

1:8:58

Enter.

1:9:00

Type here, Python 3.

1:9:02

Python you are using or PIP you are using?

1:9:04

Like Python 3 or Python?

1:9:06

So Python 3.

1:9:08

Python 3 type file.

1:9:10

PY.

1:9:12

And delete the other terminals

1:9:18

that are opal.

1:9:19

Okay, sorry.

1:9:21

So I think Python you are using, right?

1:9:23

are using right?

1:9:24

Why your BS code is coming that small?

1:9:38

Can you big it?

1:9:40

Like it is coming very small.

1:9:42

Yeah, just increase the size.

1:9:45

Just delete the other terminal

1:9:47

which up Python's terminal

1:9:48

right side in right side

1:9:49

is,

1:9:50

delete it.

1:9:51

Delete it.

1:9:52

Delete it.

1:9:53

well C.

1:9:54

C.M.D.

1:9:55

So, Vareen, now it is running.

1:9:58

If you see completely knowledge-based part is running, what is the error that you are getting, bro?

1:10:03

Now you can see that it is complete, knowledge base is complete.

1:10:07

Now, if you're the latest program copy-paste kind of.

1:10:11

Yeah, sure.

1:10:12

So.

1:10:13

Now, right?

1:10:14

Then, you're not going to run.

1:10:16

Now, screen share, right?

1:10:17

Now, you're going to run.

1:10:21

how do you?

1:10:23

Sir, actually, I think in folder in folder

1:10:26

in the folder.

1:10:27

Ah, I was in the folder

1:10:28

I was that I was

1:10:29

that I'm going to go

1:10:30

that's in the folder in

1:10:31

all the folder to run

1:10:33

you.

1:10:34

Now you're now copy paste and run

1:10:35

to run it.

1:10:36

Okay,

1:10:37

so.

1:10:38

You're not

1:10:39

here.

1:10:40

You're going to

1:10:41

you?

1:10:42

You're right?

1:10:43

Why?

1:10:44

You're right?

1:10:45

You're just,

1:10:46

you know,

1:10:47

you know,

1:10:48

you're going to,

1:10:49

you?

1:10:50

Delete.

1:10:51

Go on CMD

1:10:53

go and type

1:10:54

Python file.

1:10:55

PY.

1:10:56

Oh,

1:10:57

they're

1:10:58

they're

1:10:59

they're

1:11:00

they're

1:11:01

then you

1:11:02

need to

1:11:03

do

1:11:05

and then do it.

1:11:06

And then do it.

1:11:08

So other people

1:11:09

are also able to

1:11:10

run it, right?

1:11:11

Right?

1:11:13

Just type

1:11:18

where Python

1:11:19

and type

1:11:20

file.

1:11:21

It will automatically run.

1:11:26

That is using a different version of Python.

1:11:29

Most probably that is why it is not working.

1:11:31

If you click on that run button and then do it.

1:11:33

But if you will run from here, you will see entire output will come.

1:11:36

Correct, right?

1:11:38

In one minute output will come.

1:11:40

Yeah.

1:11:41

Other people is everyone able to run.

1:11:50

Yeah, Garima, you need to watch the last class recording.

1:11:56

This is just a continuation of the last class.

1:11:59

Those who are present in the last class, are you able to understand the entire program?

1:12:06

Guys, anyone having any doubts in the program that is there?

1:12:15

Yeah, just download everything by writing these program, like these commands.

1:12:19

I'll tell you all.

1:12:20

the commands you can write like for me pip 3 works so i can install pip 3 install then i can

1:12:26

write here dot env i can install other things also that are there like for example

1:12:35

by pdf i can install sentence transformer i can install groc that is there i can install chroma db all

1:12:45

these things you have to install for sentence transformer check out the other ppt where i showed you

1:12:50

it should be i think sentence dot transformer that is there so after this everyone will

1:12:55

be able to run it i have pasted the entire program there as well and yeah i think that particular part

1:13:01

we can see let me just open the google chrome till here guys this part is clear right this part is

1:13:08

everyone able to understand the program is also clear right it is just a continuation of last class

1:13:14

like in last class we have discussed that so yeah i think till here we are good to go right any doubts anyone

1:13:20

having till here guys still here any doubts anyone is having

1:13:36

generally in windows laptop that is required part those who are absent in the last class

1:13:40

you will watch the recording and then we can discuss yeah we can discuss like we can have a short

1:13:46

break and then we can discuss the doubts that you guys are having that thing

1:13:50

only we will do so we can have a short break and then we can probably discuss all the out starter

1:13:55

there not much theory is there today whatever we have discussed in the last class kind of same program

1:14:01

but just uploading the data we have done so that is the entire rack pipeline which we have created

1:14:07

and last three classes we have done the same thing so if you see first we did this particular project

1:14:13

where we actually i showed you with basic data that how you can create embeddings and everything then i

1:14:19

increase the project scope what i did is that i created different different chunks and

1:14:25

we understood each and every part today we have made entire pipeline which is picking the raw data

1:14:30

from the folder and then it is making the rack pipeline that is there so you can check out all the

1:14:35

three codes all the three classes are in continuation so one by one you have to watch all the recording

1:14:41

first you need to understand how did we do this vector search project then how did we do this rack

1:14:46

project and then how did we make this rack pipeline that is there

1:14:49

yeah i think after the break style we can discuss that so yeah we can have a short

1:14:56

break you can drink water and then we can discuss if you are stuck with the setup till then you can drink

1:15:01

water and you can try like going into the correct folder and running the necessary command

1:15:19

you know.

1:15:49

You know,

1:16:19

You know

1:16:49

You know

1:17:19

I'm

1:17:49

I'm

1:18:19

I'm

1:18:49

I'm

1:18:51

you

1:19:19

Thank you.

1:19:49

Thank you.

1:20:19

Thank you.

1:20:49

Thank you.

1:21:19

Thank you.

1:21:49

Thank you.

1:22:19

Thank you.

1:22:49

Yeah.

1:22:53

Yeah, guys, can you hear me?

1:22:55

Use the voice key to everyone.

1:23:19

here the program is clear to everyone.

1:23:21

Program is everyone able to understand.

1:23:24

Guys, program are you able to understand?

1:23:29

Guys, program are you able to understand?

1:23:34

Have you understood the program or not?

1:23:38

Yes, almost same thing is there.

1:23:44

Like, I think they have planned almost the same thing that is there.

1:23:48

So yeah, I think two times.

1:23:49

we have discussed so it will be more clear now that how to handle drag and everything.

1:23:53

One by one we can discuss the doubts if you are stuck.

1:23:57

So GROC API, you will need to download it, right?

1:24:00

Pankaj, your GROC API you need to add.

1:24:03

You don't have to type in my GROC APIE, right?

1:24:06

I showed you the necessary steps that are there.

1:24:08

But if you try to see GROC API you will get it from here.

1:24:12

Did you create a ENV file?

1:24:14

So if you create a ENV file, you will get your GROC API from here.

1:24:18

from here, Pankaj.

1:24:20

So that part you need to write down.

1:24:22

Pratig, what is the error you are getting?

1:24:24

Did you install everything and run the program correctly?

1:24:27

Are you able to install everything?

1:24:30

Can you share your screen very quickly?

1:24:36

Let's see what is the error you are getting?

1:24:40

Pratik.

1:24:44

Yeah, so this is correct only, right? Pratik.

1:24:47

just copy the entire program and run it.

1:24:50

Copy the latest program and run it.

1:24:52

It will work.

1:24:53

It's right.

1:24:54

Like it is coming correct only, right?

1:24:57

Output out of right?

1:25:00

Okay, sir.

1:25:02

Yeah.

1:25:08

Other people like what is the issue?

1:25:12

So you can see this that we can write a basic.

1:25:16

we can write a basic prompt.

1:25:18

If you see Manish Monday, right,

1:25:20

that we can write a basic prompt based on all the prompting techniques that we have written.

1:25:25

And we can give that kind of prompt to Claude or Cursor and that will generate similar kind of program that is there, right?

1:25:31

We just have to write a basic prompt whatever we learned for prompt techniques and we can write the entire program.

1:25:46

don't have to write, right?

1:25:48

Scratch, I mean, nah, you will see this that we can see something called as later on once we go into the AI agent part, right?

1:25:55

I'll show you what is context engineering and everything.

1:25:58

Using that particular part, you can actually see that how you can write all the programs from wipe coding.

1:26:05

So you can even check that out from all my videos that are present on this platform, right?

1:26:11

I think I'll share you on YT also tomorrow in the next class.

1:26:15

class, but you can probably see all these things here.

1:26:19

Like if you go to Maasai Live Right, you can see that I think for some days my videos are open.

1:26:26

I'm not very sure, but if you go to the previous section that is there, this one.

1:26:32

So you can see all the videos I've uploaded here that how you can write code with cursor, Claude and everything.

1:26:38

So you can probably go to this particular link and you can sign up and everything is free of cost only.

1:26:44

free of cost only there. So you can watch all the videos that how you can like build it any program from cursor as well. So you can even do that.

1:26:55

I'll share you the YouTube link of these videos also. So you can even do that.

1:27:02

Let me share that also.

1:27:10

So I've shared that link. You can get and see that how you can do something called as We

1:27:14

coding, how you can generate all these codes with wipe coding as well. So you can even see that particular part.

1:27:25

You can even see that if you want to generate the same code using cursor, you can watch the YT playlist that I've shared.

1:27:34

In that particular part, you can see everything.

1:27:44

Go on, Pankaj, what is a doubt you are having?

1:27:49

Are you able to run the program, Pankaj?

1:27:52

Mm-hmm.

1:27:59

Hello?

1:28:03

Pungaj, can you hear?

1:28:05

Shahendip output is coming.

1:28:11

I'm not able to hear you, Funketch.

1:28:16

I'm audible right now.

1:28:18

Yeah, now you are audible, go on.

1:28:20

I have just created the dot env file and just want to know how to write the Brock key in.

1:28:27

Here you are free.

1:28:29

Holder.

1:28:30

Yeah, in dot env.

1:28:32

example file that is uploaded on GitHub, right, same way you need to write.

1:28:35

So if you see, I'm giving you a link also, you can see this actually contains the entire

1:28:41

format in which you need to write.

1:28:43

So I'm pasting you the link also in the chat.

1:28:45

So if you open that link, right, you can see that you need to write Brock APIE equal to

1:28:50

and then you need to paste your API key that is there.

1:28:53

That way you can do it.

1:28:54

So if you open the link from the chart, you can see or apparently on my screen also, you can see that part.

1:29:00

Getting my point.

1:29:02

Yeah.

1:29:03

Yeah, I have done. Thanks.

1:29:04

Thanks.

1:29:05

Yeah.

1:29:06

Go on, Rawe Barma.

1:29:07

What is the route you are having?

1:29:09

Mm-hmm.

1:29:11

Hello.

1:29:15

Can you share your screen?

1:29:16

Mm-hmm.

1:29:17

Okay.

1:29:18

Just a minute.

1:29:19

What is failing for you in the program?

1:29:23

Actually, I recently saw the class in which you installed chroma DB, right?

1:29:29

You have not installed the other packages that are there.

1:29:32

I think PKG resources, which program.

1:29:35

Just show me your screen what you are running.

1:29:37

Oh, one's okay.

1:29:40

Actually, I'm on this on the web.

1:29:44

So I'm not getting the option to share screen.

1:29:47

Let me rejoin or let me rejoin.

1:29:51

Sorry.

1:29:52

Just give me, wait, wait, wait, wait.

1:29:55

I'm promoting you.

1:29:56

Can you share your screen now?

1:29:58

Are you able to see that option of sharing screen now?

1:30:06

you are able to run right

1:30:16

barth and muskhan are you able to run or not

1:30:19

you can run it on other ideas also even that thing can be done up

1:30:23

raoul verma can you share your screen

1:30:26

yes is it visible now

1:30:29

yeah it's visible

1:30:32

so just to

1:30:34

I am inside this and then

1:30:36

I try to.

1:30:49

Terminal to increase the terminal.

1:30:52

It's full size right now actually.

1:30:54

No, no, you can increase it.

1:30:55

Just to make it that bar

1:30:57

it's on the terminal on top of it.

1:30:59

It's a terminal.

1:31:00

Yeah, yeah, yeah, yeah.

1:31:02

Just told down now.

1:31:06

So this is failing you are saying.

1:31:11

It fails, it gives this error I shared.

1:31:15

Yeah, yeah, yeah, that error I know.

1:31:16

Just go back, go back.

1:31:18

Let's see.

1:31:20

Scroll down.

1:31:22

It's running.

1:31:24

So PIP3 is there?

1:31:27

PIP3 is there?

1:31:28

Did you try?

1:31:29

Yeah, try.

1:31:30

Same error out.

1:31:36

Let me check there.

1:31:39

Ah, it's just run over.

1:32:06

So this is a fix. I'm sharing you the fix in the chat. You can run this command that I've shared.

1:32:12

Most probably with this command, you will not see this particular error that is there.

1:32:17

So probably if you copy that command and run it right, then this error will not come up.

1:32:22

And usually this one, this was the error I was getting.

1:32:27

Ah, I have seen this error. So I have pasted a command at the chart right.

1:32:30

If you see that command, if you run that command, then it will work.

1:32:35

Okay.

1:32:36

Yeah. I will try.

1:32:38

Yeah, yeah. Just try right now. I think it should work.

1:32:41

Cancel.

1:32:42

Cancel.

1:32:43

Yeah. Cancel.

1:32:44

You cancels.

1:32:45

And once that command, look.

1:32:46

Look, look.

1:32:47

Okay.

1:32:52

Just paste in the command that I shared.

1:32:54

Directly only you can paste. Just paste it.

1:32:57

Just paste it.

1:32:58

Ah, good. Just do.

1:32:59

Paste it, enter.

1:33:01

This command is working. Right.

1:33:05

This command is working, right?

1:33:06

Wait, wait.

1:33:07

Don't.

1:33:08

No, no, close.

1:33:09

Up the upper one.

1:33:10

Okay, let it.

1:33:11

Kill.

1:33:12

Do you.

1:33:13

Yeah.

1:33:14

Now run the command again.

1:33:16

PIP install, like.

1:33:19

Pip 3 try this.

1:33:23

PIP install.

1:33:24

PIP install, comma, D.

1:33:26

I mean,

1:33:36

it's a more up uproper scroll

1:33:37

so the terminal all

1:33:38

bigger.

1:33:39

It's more

1:33:40

bigger.

1:33:41

How much time does it take?

1:33:44

Ideally, it should not take

1:33:47

much of a time.

1:33:49

It means

1:33:51

less than a minute in

1:33:53

a minute.

1:33:56

I'm going to

1:33:58

you know

1:34:02

it's going to

1:34:03

I'm going to

1:34:06

all right

1:34:17

fix here

1:34:20

right.

1:34:21

Yeah, baby,

1:34:22

yeah,

1:34:23

so you can try the other command also I've given in the chart.

1:34:27

Probably if we run that

1:34:29

that will might work,

1:34:31

but yeah, we can see.

1:34:32

Do you can see.

1:34:33

commands you can try if you run it with

1:34:35

pseudo also right then also I think

1:34:37

it might work and

1:34:38

I'm listing that also

1:34:40

we can check both these commands

1:34:43

if this command does not work

1:34:45

just go back and see if it is

1:34:49

working only quickly

1:34:51

no it got stuck

1:34:53

but

1:34:54

a little time like it will proceed

1:34:57

now

1:34:58

with all

1:35:00

you can try

1:35:02

then

1:35:06

other commands also that I have given

1:35:08

I'm sharing you this chat thread

1:35:10

also here you can see this

1:35:12

that this package is missing you can run the necessary

1:35:14

commands

1:35:15

and once you run it I think it should be good to go

1:35:18

ideally it should work

1:35:19

then we then we then

1:35:20

then we then

1:35:21

then we'll then

1:35:23

which I also missed at the command

1:35:24

set up to its ID1 version

1:35:26

version

1:35:27

you can try

1:35:28

all these things I really should work with these.

1:35:32

Okay.

1:35:33

Yeah.

1:35:34

Okay, I will.

1:35:41

Yeah, just try out the screen share.

1:35:43

I'll update once it's done, right?

1:35:47

Done.

1:35:48

Yeah.

1:35:49

Are you able to run?

1:35:50

Yeah.

1:35:51

Are you able to run?

1:35:54

Parth are you able to run?

1:35:59

Other people watch the scenario,

1:36:02

Muscar and Sonia.

1:36:03

Hello, sir.

1:36:04

Mr.

1:36:05

Fungg you need to install GROC, right?

1:36:07

PIP install GROC

1:36:08

can have to run

1:36:09

Gohan, Parth.

1:36:10

Yeah, hello sir.

1:36:11

No, sir, actually, now it's saying that,

1:36:14

okay, now it's done.

1:36:17

Sir, it's just, sir,

1:36:18

it's done now.

1:36:19

Okay.

1:36:20

Earlier it was showing that

1:36:23

it cannot find policy documents

1:36:25

but then now it's saying that knowledge base built complete.

1:36:29

Now the first step is done.

1:36:31

Yeah, so now you can run copy page

1:36:33

page the entire new program.

1:36:34

that is there and then you can run that even I think that will work.

1:36:37

Yeah.

1:36:38

Yes, sir, now I'll do that but I just need to set up the dot ANV.

1:36:41

Correct.

1:36:42

Correct.

1:36:43

And GROC API is as same as the particular file.

1:36:48

Yes, sir?

1:36:49

GROC API key is as same as this particular file, right?

1:36:53

Yeah, yeah, sure, sir.

1:36:55

Yeah.

1:36:56

I'll do that.

1:36:57

I let you know.

1:36:58

Thank you, thank you very much, sir.

1:36:59

Go on.

1:37:00

Mouskan.

1:37:01

Mouskan, are you able to run?

1:37:03

are you able to run?

1:37:04

Sonia, are you able to run?

1:37:10

Sonia, are you able to run?

1:37:13

Other people, I think everyone has run this program, right?

1:37:17

Yeah, hi, suction.

1:37:20

Am I audible?

1:37:21

Mm-hmm.

1:37:22

Go on?

1:37:23

Uh, I'm getting errors.

1:37:26

Like, I have taken your code exactly.

1:37:30

Hello?

1:37:32

Yeah, share your screen.

1:37:34

I think it is clearly saying sentence transformer is not installed.

1:37:38

I saw your error which you have pasted in the chat.

1:37:43

Sentence transformer did you install?

1:37:46

Yeah, I did.

1:37:48

So if you see...

1:37:49

I have given those commands to install the sentence transformer.

1:37:54

So if you see in the last class we saw this, right?

1:37:59

Like if you open here from this.

1:38:01

this in this particular PPD the commands are there in the 9th in the 20th PPD I think we wrote or in 19th PPD also we can see PIP install commands will be there.

1:38:13

So are you running this command right PIP install use and tense transformers?

1:38:17

Can you share your screen?

1:38:20

Yeah, I'll just share my screen.

1:38:24

Raul Verma just try other commands that are there which I've shared, try and running that and delete that and delete the terminal.

1:38:30

delete the terminal and then open the terminal again and then try.

1:38:34

Oh, where did Sony go?

1:38:37

Other people, I think everyone is able to run now, right?

1:38:48

Other people, errors are getting fixed or not?

1:38:51

So you can see the main thing is that if you need the commands, they are present in the 20th PPD that is present.

1:38:57

So you can open the 20th PPDs and you should get

1:39:00

able to see that.

1:39:01

Do you have the link? I'll paste the link of 20th Piquity also. You can check that out and you can do that.

1:39:12

API key command is already present in the link that I've pasted. So before you can check out the GitHub link there is present.

1:39:21

Nearer screen is not visible.

1:39:29

Is it visible now?

1:39:32

Now it has come on.

1:39:35

Okay. So now can you see my screen now?

1:39:41

Yeah, I can see your screen.

1:39:43

Just type here the command, correct command, which I've given PIP install use sentence transformer.

1:39:49

Can you type that?

1:39:50

Hmm.

1:39:53

Something did you rejoin?

1:39:55

It's been here in the chat.

1:39:58

Just go on.

1:39:59

to terminal and type PIP you are using, right?

1:40:03

Yeah.

1:40:04

I'm using Python.

1:40:05

Just type PIP.

1:40:07

Okay.

1:40:08

Install

1:40:12

hyphen U capital U.

1:40:16

Sentence.

1:40:17

Sentence.

1:40:18

Sundance.

1:40:19

Transformer.

1:40:20

Transformers

1:40:25

and Transformers

1:40:27

Transformers.

1:40:28

Transformers.

1:40:29

Enter.

1:40:30

Sentence transformer is installed.

1:40:39

Now just type other things also you have installed, right?

1:40:44

Yeah.

1:40:46

This PDF I installed and then the initial commands which you gave in the last class also.

1:40:52

Just type here, just type here, Python.

1:40:56

Just type here, Python.

1:40:58

Then code.

1:40:59

P.

1:41:00

CROV is also installed, right?

1:41:10

scroll up, up, up.

1:41:13

So it is saying from sentence, scroll up.

1:41:16

From here, the traceback error is here.

1:41:28

Just run that command of for.

1:41:29

the just run Python 3

1:41:31

with one.

1:41:32

Python 3, code.

1:41:34

p.y, just type that.

1:41:35

PIP3 is working for you.

1:41:50

Just type that.

1:41:55

No, no, no, pip 3 not this.

1:41:58

install, just type PIP3 install the same thing.

1:42:03

PIP 3, install, hyphen U, capital U.

1:42:08

sentence, hyphen transformers, hyphen transformers.

1:42:25

Just try to run this upgrade command of PIP that is there.

1:42:27

Copy.

1:42:28

Do you have to upgrade command of PIP and run

1:42:30

run.

1:42:31

Ideally, issue not should be

1:42:33

because the requirement is already satisfied

1:42:35

so, or the environment not going to

1:42:37

it's not going to,

1:42:38

this environment activate.

1:42:39

This PIP install, upgrade PIP.

1:42:41

Just copy that and run it.

1:42:44

Just copy that and run it.

1:42:58

Okay.

1:43:00

Now I have to run the PIP code by or Python code by.

1:43:08

You just have to copy paste and run it.

1:43:12

Huh?

1:43:13

Python type you,

1:43:16

Python's run it.

1:43:17

Python's run.

1:43:19

If you're not running,

1:43:26

we're not going to have we

1:43:27

environment to activate

1:43:29

it.

1:43:30

It's not it not going to

1:43:31

for activating the environment.

1:43:33

You will have to create an environment

1:43:35

and then install everything and then do it.

1:43:38

So you can type here this command which is there,

1:43:41

like Python space,

1:43:43

Python type.

1:43:44

Then type my space.

1:43:48

Then type my space.

1:43:49

5M

1:43:51

5M

1:43:53

VE NV

1:43:55

V dot ENV

1:43:57

V.

1:43:58

VE NV

1:43:59

No dot nv

1:44:01

And then

1:44:02

Thenv

1:44:03

space my ENV

1:44:05

My EnV

1:44:06

My

1:44:08

EnV

1:44:09

B

1:44:10

NB

1:44:12

Okay

1:44:19

right?

1:44:20

Let it run.

1:44:21

So VNVA is virtual environment.

1:44:26

Correct.

1:44:27

Yeah,

1:44:28

one Google

1:44:29

that how to activate the virtual environment,

1:44:31

and one

1:44:32

once virtual environment activate

1:44:33

then you have to install everything and then run it.

1:44:37

Because what is

1:44:38

multiple versions of sentence transformers installed

1:44:40

away,

1:44:41

which because that

1:44:42

correct version

1:44:43

do not.

1:44:44

But,

1:44:45

but you'll,

1:44:46

you'll first run

1:44:47

to run to environment

1:44:48

and then.

1:44:49

That's a

1:44:50

command

1:44:51

that you

1:44:52

don't

1:44:53

you

1:44:54

will

1:44:55

then you

1:44:56

will

1:44:57

then

1:44:58

how to activate

1:44:59

the environment

1:45:00

that

1:45:01

you're

1:45:02

that

1:45:03

you

1:45:04

scroll down

1:45:05

and

1:45:06

you

1:45:07

you'll

1:45:08

that

1:45:09

you

1:45:10

and

1:45:11

once that is activated

1:45:12

then

1:45:13

you have to

1:45:14

you have to install PIP install

1:45:14

PIP install

1:45:15

Sentence Transform but

1:45:16

PIP install all

1:45:17

things that are coming

1:45:18

and

1:45:19

then it will work.

1:45:20

So that part you need to do.

1:45:23

Okay.

1:45:24

I'm going to

1:45:25

fine.

1:45:26

So I'll check that.

1:45:27

Yeah.

1:45:28

And how do we know

1:45:30

Saxon, like PIP or Python

1:45:31

what

1:45:32

both the commands are equal, right?

1:45:34

No,

1:45:35

that

1:45:36

if we're

1:45:37

on

1:45:38

3.12

1:45:39

If we

1:45:40

PIP Python 3

1:45:41

3

1:45:42

if it's

1:45:43

if the version use

1:45:44

then

1:45:45

that's

1:45:46

like PIP's

1:45:47

okay.

1:45:48

Okay.

1:45:49

That it will

1:45:50

then

1:45:51

It will

1:45:52

then

1:45:53

you can

1:45:54

activate

1:45:55

and then

1:45:56

you're

1:45:57

try to run it.

1:45:58

It will work.

1:45:59

Okay,

1:46:00

yeah.

1:46:01

Thank you.

1:46:02

So

1:46:05

Nupur

1:46:06

we have

1:46:07

need to create

1:46:08

then only it will

1:46:09

work.

1:46:10

We have an Envi file

1:46:11

create

1:46:12

then only it will work

1:46:13

MKDIRs

1:46:14

file

1:46:15

create not,

1:46:16

it's a folder create

1:46:17

so you are doing it

1:46:18

in the wrong way.

1:46:19

to create a normal file by clicking on the plus button and then doing it.

1:46:24

Share Kanda, Pankat screen.

1:46:29

Just let me rejoin.

1:46:33

My zoom is actually stuck.

1:46:35

Let me rejoin.

1:46:49

You

1:46:51

You

1:46:53

You

1:46:55

You

1:46:57

You

1:46:59

You

1:47:00

Thank you.

1:47:30

Coppel, can you make me the co-host? I was speaking that only. Can you make me the co-host?

1:47:47

Yeah, sure.

1:47:49

Burajan, have you installed everything correctly?

1:48:00

Do Rajan, did you follow the steps correctly? Can you share your screen?

1:48:07

Steps, I see, did you install everything?

1:48:13

Hello, I have installed.

1:48:16

Share your screen.

1:48:22

I'm not seeing where the share?

1:48:26

You have declined the permission of panelists, right? That's why.

1:48:29

that's why yeah join a panelist

1:48:33

yeah this command which i think nitesh has shared right soon yeah you can use that

1:48:49

to activate the environment install everything and then it is done

1:48:53

yeah open visual studio code

1:48:59

Just type here, did you install everything?

1:49:02

Python.

1:49:03

Don't run this password.

1:49:09

Did you create a folder here?

1:49:11

Where is the policy folder?

1:49:14

Where is the policy folder?

1:49:29

Policy document folder?

1:49:36

Where is there?

1:49:37

no, then how can't it?

1:49:39

just run Python drag file 2.5.5.

1:49:43

Let's see what is error coming.

1:49:44

Just type Python, drag, space, rack,

1:49:47

write file 2.

1:49:48

2.

1:49:49

Here itself.

1:49:50

Ah, here itself.

1:49:52

Python

1:49:54

space

1:49:55

drag

1:49:56

drag

1:49:58

drag.

1:49:59

File 2.

1:50:01

Reg file 2, F-I-L-E-2.

1:50:06

Dot P-Y.

1:50:11

Enter?

1:50:12

Enter Maro.

1:50:17

We can see, right, you have not installed Sentence Transformat.

1:50:24

Did you install Sentence Transformat?

1:50:27

So Koppel, ma'am, given some command, I did, and I think,

1:50:34

Sentence Testimon was installed on that day.

1:50:38

And I have got a message also.

1:50:41

Currently it is not installed, you need to install it.

1:50:44

Without that, it will not work.

1:50:46

It is clearly saying that no module name Sentence Transformer.

1:50:49

So run here the exact command that is present in the PPD

1:50:53

and in that PPD you can see, right?

1:50:55

Just see my screen.

1:50:56

I'm changing your role and showing you.

1:51:00

Tell me the command. Shall I run it here?

1:51:03

Sorry to interrupt you, Purinjan.

1:51:06

Did you created virtual environment and not activated?

1:51:10

Ma'am, on the day you have given some command to install virtual environment also.

1:51:16

I have done that one also.

1:51:17

But you need to activate that virtual environment, right?

1:51:20

Then only it will work. Currently also you need to activate it.

1:51:23

So find out what is a command for activity.

1:51:25

the command for activating the virtual environment?

1:51:29

Do you have the command?

1:51:31

Did you say the command?

1:51:32

No, I don't have.

1:51:33

Can you please tell me?

1:51:34

I am sharing in the chart with you.

1:51:36

What is the command?

1:51:39

So this command, which I just pasted, right?

1:51:41

So if you see this, that if you have created the environment,

1:51:44

then you need to run this command,

1:51:46

which I am pasting in the chart.

1:51:48

So run that particular command after which your environment will be activated

1:51:51

and then type.

1:51:52

But then also you have not created the policy folder.

1:51:54

the policy folder.

1:51:55

So if you watch the recording and see how everyone has created the policy folder.

1:52:00

So you can see this folder policy document folder is not there.

1:52:03

Without this, it will not run.

1:52:05

Currently you can act.

1:52:06

Where I have to create this folder?

1:52:08

Where the program is side.

1:52:10

My document.

1:52:12

Okay.

1:52:13

Policy document.

1:52:14

Okay.

1:52:15

Policy document and then all these files should be present.

1:52:18

So you can create all the files and copy all these files which I have written here.

1:52:22

That particular thing you can do.

1:52:23

thing you can do.

1:52:24

Getting my point.

1:52:27

Okay.

1:52:28

Where I will get this information?

1:52:29

You will get this information.

1:52:31

You will get this information.

1:52:32

You have the link of this Generative AI notes, right?

1:52:35

In which every information is present.

1:52:37

Open that particular link.

1:52:38

Everything is present.

1:52:39

Open the coding examples there.

1:52:41

Everything is there.

1:52:43

Okay.

1:52:44

Correct.

1:52:45

So see that one.

1:52:46

So first thing I have to do the policy amendment.

1:52:49

Yes.

1:52:50

Policy document.

1:52:52

Yes.

1:52:53

Okay, then I think other people also do try.

1:53:01

I think we have discussed that particular part.

1:53:03

So you can check out whatever errors other people are getting.

1:53:07

You can take help from that and just try to do this part that is there.

1:53:12

Okay, then.

1:53:15

Yeah, Rakesh, we have just discussed everything that we discussed.

1:53:18

In the last class, same thing only we have discussed, right?

1:53:21

If you try to see, we build an entire.

1:53:22

we build an entire Rack pipeline in which what we are trying to do is we are trying to upload all the policy documents that are present.

1:53:30

And one by one, what in the program I did is, like if you try to see in the program,

1:53:35

first I imported the knowledge base, then I imported GROC, once that GROC importation was done.

1:53:41

Like if you see from the main part, we will try reading the code.

1:53:45

We created an embedding model.

1:53:47

We set up a complete chroma collection that is there.

1:53:50

Once we did that.

1:53:51

we did that we created a knowledge base. Inside that knowledge base, each of the files that are present in the policy documents is present.

1:53:59

Then what we did is we created a GROC client. We entered all the necessary queries that are there.

1:54:04

Once we entered the queries, we need to get the response of all these queries.

1:54:09

So what we did is that we retrieve the data. How do we retrieve the data?

1:54:15

We use retrieval policy chunks that are present.

1:54:18

Using which we were able to retrieve the data. We printed.

1:54:21

the retrieval data, we generated a proper grounded answer.

1:54:24

That proper grounded answer we are displaying to the user.

1:54:27

So that part only we saw in the output, right?

1:54:30

So you can see in the entire class we have done that only.

1:54:33

Correct.

1:54:51

okay then i think opal you can take over raoul what is error you are getting

1:55:03

mm-hmm

1:55:07

same error is coming you need to probably restart your laptop once again and then open terminal and then try

1:55:13

because i think in python or these things need to be added in path

1:55:17

so try that like all these commands you need to read to read

1:55:21

start your laptop and then try once again and then you can see

1:55:25

or you can raise a ticket where a TA will get in touch with you they will share your

1:55:31

screen and then they will figure out because i think we need to figure out exactly that

1:55:36

what issue is coming up or which step you are not creating did you i think you are using

1:55:41

mac only right in mac environment and everything is not required

1:55:51

you know what did you follow the exact same steps that are there

1:56:13

yes i did you share your screen one by one we can see and then raoul you can share you can share

1:56:21

we can end go on sure i'm not getting the share screen option right now

1:56:31

now should you should be able to see it go on yes

1:56:51

yeah so this i'm able to run the command screen is not it's just that that dot

1:57:00

in if i did the right thing or not i'm not visible screen is not visible

1:57:04

screen is not visible okay uh i'm only getting the option of stop sharing otherwise

1:57:12

from my screen is stuck just share again we can only see black screen

1:57:21

this year again now can you see my screen guys are we able to see the screen

1:57:34

oh i think it's taking time to load

1:57:51

so the code has run properly it's just that dot env if i did right or not i'm not

1:57:58

you have created a dot envi folder that is there just delete a dot env folder and move that

1:58:03

file apart me that move that file click

1:58:06

on the file and drop and drop and code the dot p by the side me just

1:58:09

this go

1:58:11

this click and drop and drop and go to code the side to go okay done

1:58:16

No, it's not done it.

1:58:19

It's not here.

1:58:20

This file is it.

1:58:22

Clicked.

1:58:23

Okay.

1:58:24

Okay, open.

1:58:27

I'm just selecting it, yeah, now.

1:58:30

Upur.

1:58:31

This code.

1:58:32

p.wai to drag

1:58:33

here.

1:58:34

Okay.

1:58:35

Okay.

1:58:36

Okay.

1:58:37

Again.

1:58:38

Then copy paste.

1:58:39

Okay.

1:58:40

Clicked.

1:58:41

Code.

1:58:42

Code.

1:58:43

Pye on.

1:58:44

Click on code.

1:58:45

P.

1:58:46

Now you up the file creation button

1:58:49

is in policy documents can't.

1:58:51

This can't it.

1:58:54

The biggest folder is the name policy documents here.

1:58:57

It's the side of a plus file button

1:59:00

are over.

1:59:01

Yes, yes, yes.

1:59:02

Click here.

1:59:03

Create and type.

1:59:05

. . .

1:59:07

Enter.

1:59:09

Enter.

1:59:10

Enter

1:59:16

do.

1:59:17

The program is going to

1:59:18

Yeah,

1:59:19

program

1:59:20

is

1:59:21

So,

1:59:22

the

1:59:23

problem.

1:59:24

Actually,

1:59:25

I don't understand

1:59:26

why are we doing this

1:59:26

dot envi thing?

1:59:28

Dot Envi

1:59:29

here.

1:59:30

That API

1:59:31

is used

1:59:32

our project

1:59:33

for GROC to

1:59:34

talk to

1:59:35

GROC is a

1:59:36

LLM is the third-party

1:59:36

application is

1:59:37

used to

1:59:38

use is.

1:59:39

Currently, you

1:59:40

what is the

1:59:41

D.NV folder

1:59:41

made that.

1:59:42

That folder

1:59:43

and you have to delete.

1:59:44

And that

1:59:45

I had

1:59:46

that

1:59:47

I had

1:59:48

I had

1:59:49

I had

1:59:50

I made

1:59:51

this

1:59:52

this

1:59:53

file I

1:59:54

did

1:59:55

that

1:59:56

and then

1:59:57

Go

1:59:58

Go

1:59:59

and

2:0:00

click and

2:0:01

delete

2:0:02

and

2:0:03

right click

2:0:04

delete

2:0:05

right click

2:0:06

delete

2:0:07

now

2:0:08

now

2:0:15

But

2:0:16

without

2:0:17

it's

2:0:18

it's

2:0:19

because

2:0:20

he

2:0:21

that

2:0:22

I'm

2:0:23

I'm

2:0:24

I'm

2:0:25

I'm

2:0:26

just

2:0:27

just

2:0:28

button

2:0:29

and then

2:0:30

run

2:0:31

to run

2:0:33

and run

2:0:35

so

2:0:36

so it's

2:0:37

I'm not

2:0:38

can't do you

2:0:39

it's

2:0:45

I'm

2:0:46

that

2:0:47

you

2:0:48

it's

2:0:49

you know

2:0:50

you know

2:0:51

that

2:0:52

you

2:0:53

can't

2:0:54

write

2:0:55

that's

2:0:56

okay

2:0:57

that's

2:0:58

okay that's

2:0:59

that's

2:1:00

so

2:1:01

you're

2:1:02

I'm

2:1:03

I'm

2:1:04

I'm

2:1:05

okay

2:1:06

okay

2:1:07

thank you

2:1:08

right

2:1:15

I'm

2:1:17

share

2:1:19

Ganna

2:1:20

I'm

2:1:21

right

2:1:22

I'm

2:1:23

I'm

2:1:24

no

2:1:34

I'm not

2:1:38

I'm

2:1:39

I'm

2:1:44

I'm

2:1:47

screen

2:1:48

screen

2:1:49

I'm

2:1:50

screen

2:1:52

scroll

2:1:54

scroll

2:1:55

scroll

2:1:56

scroll can't

2:1:57

scroll

2:1:58

right right right

2:1:59

you're

2:2:00

you're

2:2:01

this

2:2:02

I'm

2:2:03

it's

2:2:04

changed

2:2:05

command is

2:2:06

change to

2:2:07

change to

2:2:08

go to

2:2:09

you can't go

2:2:10

you can't

2:2:11

I'm

2:2:13

it's

2:2:14

it's

2:2:15

it's

2:2:16

it's

2:2:17

it's

2:2:18

right

2:2:19

it's

2:2:20

here

2:2:21

this

2:2:22

this

2:2:43

right

2:2:53

PIP

2:2:54

PIP 3 install

2:2:56

Sentence Transform

2:2:57

PIP 3

2:2:59

0

2:3:00

U

2:3:01

Uh

2:3:03

Chrom D

2:3:04

Proma DBB not?

2:3:05

Uh,

2:3:06

Chroma DBB

2:3:07

U need to

2:3:08

PIP3 install

2:3:08

Chrome ADB

2:3:09

DB got do just

2:3:10

C CromA DB

2:3:11

DB

2:3:13

Chrome

2:3:14

DB

2:3:15

not

2:3:16

install

2:3:17

not enter

2:3:19

I think

2:3:20

I think

2:3:21

you're

2:3:22

I think

2:3:23

you're

2:3:24

I think

2:3:25

have to

2:3:26

install

2:3:26

and

2:3:27

don't

2:3:28

do

2:3:29

or

2:3:30

do?

2:3:31

Yeah,

2:3:32

but

2:3:33

that

2:3:34

I think

2:3:34

it's

2:3:35

I think

2:3:36

it's not

2:3:36

because

2:3:36

PIP 3 is

2:3:37

we

2:3:43

right

2:3:44

right

2:3:45

right

2:3:46

here.

2:3:47

Yeah,

2:3:48

Brae install PIPX

2:3:49

to

2:3:50

it's

2:3:51

time

2:3:52

it's

2:3:53

enter

2:3:54

Morrow.

2:3:55

You're

2:3:56

I'm

2:3:57

doing

2:3:58

you

2:4:00

do

2:4:01

you

2:4:02

have

2:4:03

already

2:4:04

already

2:4:06

installed in

2:4:07

no

2:4:08

that

2:4:10

I'm

2:4:12

I

2:4:14

need

2:4:16

and

2:4:19

you

2:4:20

and

2:4:21

you

2:4:22

and

2:4:42

right

2:4:56

the command

2:4:59

it's

2:5:00

that's

2:5:02

it's

2:5:03

it's

2:5:04

that's

2:5:05

it's going to

2:5:06

it's

2:5:07

it's not not not

2:5:08

not not not

2:5:09

not.

2:5:12

And

2:5:13

this

2:5:14

once you know

2:5:15

know

2:5:16

what

2:5:17

Koppel you can't

2:5:18

you can't

2:5:19

and they

2:5:20

I'm

2:5:21

I'm

2:5:22

written

2:5:23

and they're

2:5:24

and you

2:5:25

you're

2:5:26

direct run

2:5:27

this

2:5:28

without

2:5:29

what I'm

2:5:30

that

2:5:31

break system package

2:5:32

package

2:5:33

and

2:5:34

the break system package

2:5:35

the command is

2:5:36

this

2:5:37

you're

2:5:42

I'm

2:5:43

I'm

2:5:44

scroll down

2:5:45

the

2:5:46

last

2:5:47

this one

2:5:48

this one

2:5:49

run and

2:5:50

this one

2:5:51

it's

2:5:52

this is

2:5:53

it's

2:5:54

we're

2:5:55

without activating the

2:5:56

terminal

2:5:57

without activating

2:5:58

PIP command

2:5:59

environment

2:6:00

we want to run

2:6:02

Chrome RDB

2:6:03

because I think

2:6:03

you're

2:6:04

in your environment

2:6:04

in

2:6:05

or you know

2:6:06

the environment

2:6:06

delete and

2:6:07

then create and

2:6:08

create and install

2:6:08

then

2:6:12

how

2:6:12

how to

2:6:13

this

2:6:14

then

2:6:15

then

2:6:16

then

2:6:17

I'm

2:6:18

just

2:6:19

that I'm

2:6:20

right

2:6:21

correct

2:6:22

correct

2:6:23

okay

2:6:24

okay

2:6:25

then

2:6:26

guys

2:6:26

I think

2:6:27

you

2:6:28

can start

2:6:29

the quiz

2:6:30

yeah

2:6:31

okay

2:6:32

guys just

2:6:32

just revise

2:6:33

whatever we

2:6:34

discussed in the last

2:6:34

last

2:6:34

and try to do

2:6:36

the setup

2:6:36

whatever

2:6:37

setup we have

2:6:38

seen and try that

2:6:39

part.

2:6:41

Yeah, I think

2:6:42

Opel you can take over.

2:6:43

All right, so

2:6:45

so I'm sharing the feedback

2:6:48

for a

2:6:51

short voice.

2:7:09

I'm re-sharing my Google Drive link.

2:7:19

Here you will find how to install

2:7:20

Python,

2:7:21

how to install

2:7:22

BS code,

2:7:23

how to create environment if you want

2:7:25

for both Mac and Windows systems

2:7:27

and how to proceed with

2:7:29

chroma DB and sentence

2:7:31

transformers.

2:7:32

So you'll get each and every step

2:7:34

by step

2:7:34

instructions there.

2:7:38

If you'll encourage

2:7:39

encounter any issue we can discuss in the next tutorial session.

2:8:09

All right, so let's move on to the last.

2:8:39

stage of the session. That is a short quiz. Let me share my screen.

2:8:46

So you can scan this QA code given here

2:9:05

here or just go to just go to this web site or just go to this website.

2:9:07

www.com.com.com.

2:9:09

and enter this eight digit code written here.

2:9:12

I'm pasting this in the chat as well.

2:9:39

Alright, so let's get started.

2:10:09

What are the raw documents chunked before indexing?

2:10:13

To make files larger to improve retrieval and reduce token usage to remove metadata to remove metadata to train the LAM.

2:10:39

Yes, the correct option is chunking is used to improve retrieval and reduce token usage.

2:10:53

Let's look at the leader one.

2:10:58

Moving on to the second question.

2:11:09

What is a document loader?

2:11:13

And the options are a model that generates answers, a database for storing embeddings, a tool that brings PDF for text files into Python or a chunking algorithm.

2:11:39

Yes, it's a tool that brings PDF for text file into file.

2:12:09

Which library is used to read or parse video files?

2:12:13

And the options are Pandas, Numpy, Phi BDA for requests.

2:12:39

Yes, the correct option is Phi PDA.

2:12:43

Let's have a quick look on the scoreboard.

2:12:53

Moving on to the fourth question.

2:12:57

Five is overlapped used during chunking and the options are to increase file size to create duplicate documents to preserve context across chunk boundaries or to reduce embedding

2:13:27

Yes, chunking, overlap during chunking is used to preserve context across chunk boundaries.

2:13:57

Let's move on to the fifth question.

2:14:04

Which metadata field is inferred from the file name?

2:14:09

And the options are embedding vector, chunk size, category, or distance score.

2:14:27

The correct option is Category.

2:14:57

Let's move on to the sixth question.

2:15:00

What does the build knowledge based function?

2:15:10

And the options are only document loading, only embedding generation.

2:15:17

Load, chunk, embed, and store, or generate final answers.

2:15:27

The correct option is, see, this function performs load, then it chunks, embeds, and restores.

2:15:57

Moving on to the 7th question.

2:16:14

If the rank 1 retrieve category is uncurrent, the problem is most likely in the Crock model, the generator prompt, ingestion or chunking, or the dot ENV file.

2:16:27

Yes, the correct option is C, ingestion or chunking.

2:16:56

Chunking.

2:16:57

Let's have a quick look on the leaderboard now.

2:17:00

Moving on the final question for the day.

2:17:15

What is the main purpose of metadata in a RRAG part line?

2:17:22

And the options are to increase embedding dimensions to track the source and category.

2:17:25

the source and category of retrieval information to generate embeddings faster to reduce storage requirements.

2:17:55

The correct option is metadata is used to track the source and category of retrieve information.

2:18:02

Let's see the final leaderboard now.

2:18:06

Congratulations, Rakesh.

2:18:20

So let's let's stop here.