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

Hi, everyone, very good evening.

15:47

Folks, I am I audible to all of you all of you.

16:06

Hi, everyone, I'm audible.

16:09

I'm audible.

16:10

I think somehow the chat is not enabled.

16:12

Yeah, it is enabled.

16:13

Thank you.

16:14

Hey, folks.

16:16

Good evening, good evening.

16:17

How are you guys doing?

16:20

All good.

16:21

All good.

16:25

Great.

16:26

OK, so guys, welcome to the class.

16:28

And in this particular session, we are going to build the rack pipeline.

16:32

And we are going to add a more, like a bit more functionalities

16:35

in the pipeline that we added that we built in the last class.

16:38

that we, whatever concepts we learned in the last class, we are going to extend that particular

16:43

discussion and we are going to follow a slightly more advanced approach in today's class, okay?

16:48

Now before we actually get started with the session, you must have received an email and

16:54

about the link, right, for the feedback form.

16:58

Have you received it?

16:59

The monthly feedback form from the Maasai team, correct?

17:04

On your dashboard or on your email ID, correct?

17:07

How many of you have you?

17:08

have filled it? If not, if you have filled it, please let me know in the chat. If you have

17:14

not filled it, please make sure that you are filling it right now. Take two minutes of time. I'm giving

17:19

you two minutes of time and please make sure that you are filling it right now. And because definitely

17:25

everyone, if you're sharing your honest feedback, it is going to help the team to make the learning

17:31

experience even better. If you have any feedback to share, please do let us know. And if you have

17:36

something to appreciate about the team, about the platform, about the overall

17:40

massive platform, then that also do let us know so that the team will get more more like more

17:46

motivation to do better things in your learning journey. So please make sure that you are filling the

17:51

form right now. Mukul, I was, we were talking about the form, the feedback, the monthly feedback

17:56

form you must have received over your email and the dashboard. So I was just requesting all of you

18:01

to fill that feedback form if you have not filled it already. If you have filled it all

18:06

please do let me know in the chat that yes, Deepak, we have filled the form.

18:10

Okay? Guys, take two minutes of time, fill it right now. Okay? And then we will get started with

18:15

the session and in the meantime probably people, more people will join and then we'll get started.

18:23

If once you feel it every month, let me know in the chat.

18:31

Once you complete the form, please let me know in the chat so that I'll get a,

18:36

a nerve like how many of you have already filled. In the meantime, I'll share my screen with all of you.

19:06

Done, done, okay. What about other people?

19:36

Thank you, Bishik. Okay, thank you, Shimonsh.

19:42

Folks, please do fill if you're not filling it already. Thank you, Ravi.

19:47

Thank you, Ravi.

19:47

Thank you, Ravit.

19:49

We have not started yet. I was just talking about the feedback form. You must have received over your email, the monthly feedback form.

20:06

Okay, so if you have not filled it, please do fill it right now. We are just about to start the session.

20:19

Okay, thanks everyone. I hope all of you have filled. If not, then please make sure that you are filling it after the class. In case, if it is spending, please make sure that you fill it. Definitely, it will help us to make your learning journey even better. Okay. Great. So I hope my screen is visible to all of you. And let's get started with the session for today's. Right. Let's get started with today's session. Okay. So guys, now, if you remember, what we have discussed in the previous classes.

20:49

In the last couple of classes, if you remember, we talked about introduction to Rack.

20:54

First, we talked about what Rack is, different components, different things about Rack.

20:59

Okay? And also we saw the complete flow with respect to Rack.

21:02

And then everyone, in the last class, right, particularly about the last class, that happened on 29th of April.

21:09

We talked about implementation, right?

21:11

Remember that? That we had a brief discussion on the Rack components and then we actually implemented it.

21:17

Remember that?

21:19

Correct or not? We actually implemented the whole Rack system.

21:26

Folks, correct? Okay. Now everyone, in the last class, when we did the implementation,

21:30

we majorly focused upon these things, embeddings, Vector Database, Retriever, Generator.

21:37

Now everyone, today we are going to talk about the production rag. In the last class, you can say that we built a minimal

21:43

rag application, kind of a basic Rack application with small policy snippets. Now,

21:49

in the last class, did we have the complete policy documents altogether? Did we have the policy

21:55

documents? Okay, that's fine, Ravie. Did we have the complete policy documents? No, right? If you

22:05

remember, in the last class, when we had the policy data about refund policy, return policy,

22:12

we had simple, you can say that simple dictionary kind of thing, right? Or simple list

22:17

kind of thing, right? If I show you some, not even that, simple strings, okay? Let me show you

22:24

visual studio code.

22:42

So I think this is the one that we built. Correct everyone? If I'm not wrong, because I have multiple projects, I sometimes forget the exact project name. This is the one, right? E-commerce rack. In this, if you see, this is how we define the policy documents, right? Simple string values in a dictionary that, okay, this is the return policy. It is nothing but not even a dictionary. It is a list, right? List of values, list of these values, right?

23:10

But even now, in reality, right, when you build a production rack system, the real Rack system,

23:16

do you think that the policy documents will be given like this? In the form of simple string values

23:21

or JSON values? Answer is no, right? In what format you can expect the policy documents to be in?

23:31

In what format you can expect the policy documents to be in? You can expect the policy documents to be in.

23:40

data, like to be in file format, right? To be in file format. Now, files can be

23:46

PDF, files can be text, files can be doc, and so on, right? There can be multiple types of files.

23:55

It means that everyone, now you will be given, let's say, a PDF file, which is the most common one,

24:00

common use case. You will get multiple PDF files. So you will have to read the PDF files using

24:06

some library, right? In Python, there are multiple libraries, which allows you, in every

24:10

language, you have some libraries which allows you to read the data from given files, right?

24:15

For example, PDF reader, etc. So you read the document, you read the PDF file using some

24:21

library, understand it, understand the text, load it, and then use it to answer the user queries.

24:28

Is the flow clear to all of you? Is the idea clear to all of you? Right? So guys, what is the goal

24:35

for today's session? The goal is to build

24:40

build a multi-document. Build a multi-document. Build a multi-document.

25:10

of you? Customer support system.

25:19

So this word is very important, multi-document. Because everyone, if you just have strings in your

25:26

system, it is very easy to understand. It is very easy to use. But when you are using documents

25:31

from external sources, right, let's say the PDF, right? You are getting PDF documents. Now you need

25:36

to read those documents. You need to clean those documents, etc, etc. So,

25:40

Whatever are the different steps involved in building a multi-document e-commerce customer support

25:47

system we are going to talk about in today's class? Is the idea clear to all of you?

25:56

Folks, yes, no. Why you are not answering in the chat today?

26:03

People are not happy today?

26:06

Maybe because of some election result or maybe you are super happy?

26:10

How many of you follow, how many of you did follow the election results today? Of any state.

26:18

Of any state.

26:22

Right? I think everyone. A lot of you, a lot of you. At least I followed a lot.

26:28

Okay. So which particular seat or which particular constituency or which particular state was the most

26:35

interesting one to see today?

26:38

Bengal.

26:40

And now I think the results are very, very surprising. In fact, Tamil Nadu also. No one was talking about Tamil Nadu before today. Like people were not as curious as they were for Bengal. For Bengal, people were more curious to know the results. But after knowing the results, people are now more curious about Tamil Nadu. Right. I was also not having a lot of idea about the Tamil Nadu politics. But now after today's result, I did some research, then found out that how

27:10

the actor Vijay came into politics and just in like, in last two to three years, he, like, he won't, like, he is one of the majority party in the entire state, right? That's a big thing. Okay? Anyways. I think now, I was just looking at the results just before the class. I think Mamta Panerjee is also behind. Is that correct? By some 500, 600 votes in the latest, in the latest result.

27:40

She is behind. Let's see how it goes. By the end of the class, it will be clear. So let's focus on the class. Okay? And by the end of the class, we will be clear with what is going on. Okay? Fine. Now everyone, when you're building a multi-document system, so please be very, very energetic in the class, okay? As usual, so please participate in the discussion.

28:00

Now, guys, when we have multiple documents, right? There are different steps involved when we build a rack system. Now, guys, if you don't have a document, if you just have the file or if you just have the file or if you

28:10

you just have the policy data as it is into the system, if you just have the policy data as it is into the system,

28:16

into your program, as a list, as a string. Do you need to load those documents from somewhere? Do you need to

28:21

load, do you need to use any library to load the documents? Answer is no. Right? So it is pretty

28:26

straightforward, pretty simple thing. But when you have documents, the flow changes. So let's talk about

28:30

the high level architecture of multi-document e-commerce customer support system. So, guys,

28:36

first of all, you have documents. Correct, everyone?

28:40

Now, generally what happens?

28:42

Documents are generally present at some location, correct?

28:48

Correct?

28:49

These might be present on some cloud.

28:51

These might be present in some other place, right?

28:54

They might be present in some hard disk, they might be present in some other laptop,

28:57

or they might be present in some other folder in your laptop, correct?

29:00

Now, can I say that wherever your Python program is running,

29:05

you need to load these documents into your Python program?

29:09

You need to load these documents into your Python program.

29:10

these documents into your Python program? Yes? So these documents we will load.

29:16

So the first step that comes everyone is document loading step. The first step that comes

29:27

is document loading step. After document loading everyone, document loading means that you have

29:33

read the documents and you have loaded those documents into your program. Now you can access those

29:39

documents from your program, from your Python program. Once you have the documents

29:43

within your Python program, can you directly use them? Do you think so? Can you directly use these

29:48

documents as it is? Answer is no. So here comes everyone, the document parsing step. The next

29:57

step is document parsing. We will talk about all of these steps one by one, don't worry. It is not

30:03

mandatory to convert these into MD files until or less you have a hard requirement, right? Otherwise, it is

30:09

not a mandatory thing to do every time. So another step, the next step comes

30:13

is everyone, document parsing or cleaning. Document parsing and cleaning. Now guys, on a high

30:22

level, can you tell me what is the meaning of parsing and cleaning or parsing or cleaning?

30:28

Sometimes everyone, you might have seen that in document. There are a lot of redundant things,

30:32

right? For example, let's say you must have seen some document. There might be some header things, right?

30:36

every document contains some header, company name, company address, etc, etc.

30:41

Then below also some footer, right? At the foot also, there is some content which is already there,

30:46

company address, contact number, etc. Now, because every time, do you need this header and footer data

30:51

into your final content? Into your final content? Into your final content? Answer is no. So you can

30:58

remove unrequired or the data which is not required. Can I say that? That is called as parsing

31:04

and cleaning step. Parsing means parse the data, read the data. And after that,

31:09

everyone, if there is some redundant content inside the data, inside the document, just remove it. So

31:15

parsing and cleaning. Is the idea clear to all of you? Right? So you remove the redundant content

31:20

from the data from the document so that you have only the required data so that you can use it more

31:25

efficiently. Now next comes, everyone. We will talk about all of these things one by one in detail

31:30

also. As of now, I'm giving you the complete workflow. Okay.

31:34

on a high level. Once you parse and clean the data every one, the next step comes in,

31:39

the next step talks about if the document is very big, I think I talked about in the last class

31:47

also, but we did not talk about in detail, right? Because this is the topic for today's class.

31:51

If the document is very big, let's say the document is of thousand pages. Now, because

31:55

don't you think that creating a chunk or creating a embedding of thousand pages of document

32:01

or storing the entire document at one place, searching from the entire document of

32:06

thousand pages in one go, in one shot, will be a not, will not be, will not be, will not

32:11

be a very efficient thing because the document is itself very big, right? So what do you do

32:16

everyone? You divide the document into small, small chunks. Now there are different chunking

32:20

strategies we have. We will talk about that. So what do you do? You divide the document into different

32:24

chunks so that you can store the data more efficiently, you can store the chunks more efficiently,

32:29

and you can retrieve the required information more efficiently. So the next step is

32:34

chunking process. Is that point cleared all of you? It is called as chunking process. Once you create

32:47

the chunks of the document even on, how to create chunks, what are the different strategies? We

32:51

will talk about it. Don't worry. So chunking is nothing but splitting the data, splitting the document

32:55

into small, small pieces for better efficiency, for better utilization.

32:59

Once you create the chunks, everyone, you have to store them into database.

33:03

But do you store the data or the text as it is into the database?

33:08

No, right? What do you do? You create embeddings. So the next step is to generate

33:17

embeddings. And finally, everyone, after embeddings, what do you do? Once you create the

33:26

embeddings, you store these embeddings into vector database.

33:29

Vector DV storage. Once you store the embeddings into vector database, what

33:37

do you do? The next step is, after storing the embeddings into vector database, what do you do?

33:43

Then everyone, the next flow comes in, you get a user query. You convert the user query into

33:53

embedding.

33:59

You convert the user query into embedding. Then everyone, you perform similarity search.

34:10

You perform similarity search and then you give the context to the LLM and then final response.

34:19

Is the final, are these steps clear to all of you?

34:22

After similarity search, whatever chunks you will retrieve, the relevant chunks you will give to LLM.

34:29

Why do we give the relevant chunks to LLM, everyone? Why do we give the relevant chunks to the LLM?

34:36

LLM? Why don't we return the chunks directly to the user?

34:48

Folks, from similarity search, you find out top three, top five, top 10, relevant chunks, the chunks, the chunks which are matching with the

34:59

For example, if the user is asking about the refund, you will probably find out

35:04

top three chunks which are matching with the user query, which are talking about refund, money

35:08

back, etc. Now you will give these three chunks, these three relevant chunks to the LLM, and

35:15

LLM will try to generate the answer in a user-friendly way, in a polite way. You cannot just directly

35:20

give the policy documents as it is to the user. Is that one clear to all of you?

35:24

So when LLM generates the final answer, you must have written a proper prompt.

35:29

In the last class, I showed you the example, right?

35:31

You write a proper prompt to the LLM.

35:33

You give a proper prompt to the LLM that is generally called a system prompt.

35:36

You give a system prompt that is already there, you just change the context and the user query,

35:41

and LLM will generate a like a relevant answer using the context and return to the final response to the user.

35:50

Is that point clear to all of you?

35:52

This is the complete flow that we have.

35:54

And this is what we are going to build in today's class.

35:59

all of you.

36:00

Okay.

36:01

Now guys, let's talk about the first process which is document loading, right?

36:09

This process is also called as document ingestion.

36:13

Whenever you ingest, whenever you insert, whenever you insert any data into the system,

36:17

that step is called as ingestion step or loading step also.

36:20

So let's talk about the first step which is document loading or ingestion step.

36:29

Document ingestion step.

36:39

Right?

36:41

So this document ingestion step means that loading the raw documents.

36:58

into the rack pipeline.

37:00

Correct?

37:01

Loading the raw documents into the rack pipeline.

37:13

Is that point clear to all of you?

37:15

Now what is the meaning of raw documents?

37:19

What is the meaning of raw documents?

37:22

What is the meaning of raw documents?

37:25

The documents which are, which have not been

37:28

cleaned yet, which you have not parsed yet.

37:31

These raw documents can have the data as well as can have some redundant data also.

37:36

As it is, it is coming from the source.

37:38

You have not performed any cleaning on top of it.

37:41

Now these raw documents can be in the form of text, can be in the form of PDF, can be in the form

37:49

of any other format also.

37:51

Makes sense everyone?

37:52

It can be the text format, it can be the PDF format, it can be any other format as well.

37:57

Now for example, even the mode.

37:58

The most common way is the most common type of documents are PDF documents because most of the companies generally stored or most of us also, we store our document in the form of PDF.

38:09

Now guess for PDF, there is a library called as Pi PDF.

38:14

In Python, there is a library called as Pi PDF Python library, which we're going to use to load the raw documents.

38:23

Make sense, everyone?

38:28

This is the Python library that we're going to use.

38:35

Okay?

38:37

Then everyone, inside this library there is a function or there is a class called as PDF reader.

38:42

Okay?

38:43

So inside this there is a class called as PDF reader which helps us to read the PDF document.

38:49

Okay?

38:50

PDF reader.

38:51

We will use this particular thing.

38:53

Then everyone, the next step, once you ingest the raw data,

38:57

ingest the raw documents into your Python program, the second step, the next step that comes is that process and organize the document data.

39:22

Now what is the meaning of?

39:26

Now what is the meaning of document data everyone?

39:28

What is the meaning of process and organize everyone?

39:30

It means that parsing and generally cleaning also.

39:33

That you need to read the data, you need to read the data, you need to parse the data, you need to clean the data.

39:39

So guys, raw documents are generally messy.

39:56

are generally messy and contains some redundant information.

40:05

Now, what kind of redundant data.

40:22

Now, what kind of redundant data or messy?

40:25

means that even sometimes there might be some header data, there might be some footer data,

40:29

there might be some, for example, between two lines, there might be more than one space, extra spaces,

40:35

extra line breaks, extra new line characters, some let's say page numbers, headers, footers, etc.

40:42

Is that concrete to all of you?

40:44

Could you please suggest which dependency is good to use of OCR?

40:51

Or should we use LLM?

40:52

Nowadays, I think LLM is one of the best way.

40:55

If you don't have the problem of budgeting, right, elements are very, very powerful nowadays for OCR, right?

41:02

Just to give you some context to everyone, this particular thing is not related to our content.

41:07

Once he is asking about a feature called as OCR, right?

41:11

Anyone knows about OCR?

41:13

Although it is not related to today's class because just he asked the question, and I have worked on this particular thing,

41:18

that's why from experience I'm telling you, OCR stands for optical character recognition.

41:23

Okay, okay?

41:24

Optical Character Recognition.

41:25

So this particular approach or this particular you can say that the topic talks about when you read the data which is written inside the image.

41:34

Okay, so for example, if you have an image, let's see you are standing here and behind the image, right, there is some restaurant name written, hotel name written.

41:43

Now if you want to read this data in the text format, so there are multiple libraries which are there, which are out there, which we can use for OCR, but nowadays you can directly give to LLM and you can give the prompt in such a way that,

41:55

read this image and tell me the text written inside it. So you can read the text.

41:59

I have worked on this OCR very, very closely. I will give you one very good use case of OCR feature,

42:06

which I have worked at Microsoft only. Guys, I have worked at Microsoft security. Okay. So my team basically

42:13

manages the entire security of Microsoft products. You must have used Microsoft Teams,

42:19

Microsoft just like Google Meet, etc., right? Microsoft Teams, Microsoft Teams, Microsoft Teams, Microsoft Outlook,

42:25

SharePoint, OneDrive, etc., etc. Now, for example, let's say, if there is a company,

42:30

let's say American Express, okay? Let's say American Express. There are like thousands of companies

42:35

in the world which are using Microsoft products in their organization. I'm not talking about the personal

42:40

usage. I'm talking about the enterprise level usage. For example, there is a company called as American Express,

42:46

which is one of the world's biggest financial company in the terms of credit cards. Now, if they are

42:52

using Microsoft products like Outlook, SharePoint, OneDrive, Teams, etc. Do you think we should

42:58

let, we should provide them the secure features. Like, for example, if someone is sending an email

43:04

outside the organization, then we should let the admin know. We should notify the admin that this

43:09

particular person has sent this information outside the organization. So you tell me what to do.

43:16

Should we block the email or should we allow to send the email, send a warning, etc, etc.

43:20

Correct, everyone?

43:21

Right?

43:21

a simple feature, right? Looks like a simple feature, although it is not, right? Although it is not.

43:26

Now, also everyone now, based, like, we cannot block the emails always, because a lot of customers

43:33

also gets the email from American Express. So we need to identify that, that this is very high severity

43:38

email. In this, there is a risk of some crucial information. This is okay, that okay, we can share

43:46

this email. So for that, we need to read the text written inside the email. Now, whatever text,

43:51

is written inside the email. It is very easy to pass. It is very easy to read. But what if

43:57

someone is sending an image inside the email? For example, let's say everyone, if someone is

44:01

sending a credit card image in an email attachment. Now, that is one of the biggest red flag,

44:08

right, for a financial company. If the image of the credit card is being leaked outside

44:12

organization, correct? That is a very big red flag. Now for that, what we need to do everyone is,

44:16

we need to identify that, okay, we need to, first of all, we should be able to read the image.

44:21

then we should be able to understand that what is written inside the image. Because we cannot

44:24

block every email with the image. Because a lot of times the emails can also contain some

44:29

images which are legitimate. For example, company logo. Correct? That is a legitimate mail. We cannot

44:35

block it. We should not block it. So for that, we need to, first of all, we should be able

44:39

to read the image. We should be able to parse it. We should be able to read the text written inside

44:44

the image and so on. Then we should take a decision. We should block it or we should not block it.

44:48

This is what I have worked at Microsoft in the field of.

44:51

of optical character recognition, right? Is I declared all of you? Although not related

44:57

to today's class, but a five-minute discussion must have given you a good small understanding

45:01

of what is OCR. But what about the images in the PDF? That is also covered, right? So that's what

45:06

that is what I was telling you, right? That this particular feature looks very simple. But

45:11

there is an entire like people, like there is an entire team of thousands of people at Microsoft

45:16

who are working only in the security thing. Right. So as sure I mentioned, what about the images,

45:21

images which are present in the PDF. Absolutely correct. There can be PDF inside the document,

45:26

then there can be image. Inside the image also, the text might be very minute. So we need to understand,

45:31

we need to make sure that nothing, like none of these are getting missed from our, from our code base.

45:37

Right. So that's why it is very complex thing. Okay.

45:48

It should be Vishanath, if it is supported, it should

45:51

be. Is the idea clear to all of you? That was just out of the context. Okay. So guys,

45:58

process and organizer data, that is document parsing and document cleaning. So this is

46:04

called us document parsing and document cleaning. Everyone clear till this point of time. Let's

46:16

come back to our content.

46:21

Then everyone, the next step is what? Once you have cleaned the document, once the document

46:27

is clean, what should we do now? Since there are PDFs which are highly protected, especially

46:36

from Evinox documentation. Correct. So that is other thing that you can put passwords on the

46:44

PDF that is a separate thing. Yeah. The next process, everyone, is chunking process.

46:51

Okay. Now let's talk about everyone that why chunking is required. Now tell me everyone,

46:59

for example, let's see you have documents, right? Now you have not performed chunking. You have

47:03

refund policy document. You have return policy document. You have shipping policy document. And

47:09

you have other documents also. Okay. You have other documents also. Now, once you have stored the

47:14

documents as it is into the system and now when the user query comes in, you find the relevant document, the

47:21

entire document. Now, let's say, when you got two documents, or let's say three

47:24

relevant documents for the user query. Now, guys, don't you think this is the context. These

47:29

are the relevant information. These are the relevant documents which you have found for the

47:34

user query. Now, don't you think you will have to send these documents to the LLM to generate the final

47:40

answer? These three documents will act like the context to the LLM. So LLM will generate the answer

47:46

based on these three documents. Yes or no? Correct?

47:51

So whatever similar documents you have found, so LLM, you will pass these documents to

47:55

the LLM. LLM will use these documents as a context and will try to generate the final answer.

48:01

Folks tell me, if you're sending the entire document to the LLM, don't you think you will

48:05

end up consuming a lot more tokens if the document sizes itself thousands of pages, thousands of pages.

48:14

And you are sending multiple such documents to the LLM again and again with every user query.

48:18

Do you think you will end up consuming like a lot of redundant, lot of like much more number

48:25

of tokens from LLM and the cost will be very, very high? Tell me yes, no. The context window will

48:31

pass very soon. You will consume the entire context window in just few queries, right? Absolutely.

48:36

Right? So guys, we can say that. First thing is searching through large

48:48

documents is an expensive process. Searching through large documents is expensive process.

49:04

Is expensive. Then everyone also sending

49:18

to the LLM is also expensive. Correct, everyone? It is also expensive.

49:34

Correct. So what could we do everyone? What should we do, everyone? What should we do? Let's discuss at the end. I'll have, I will also have to

49:48

that particular thing. Okay? So yes, that's why is the problem statement clear to all of you?

49:53

That why we should not store the documents as it is into the system. So definitely, one, what

49:59

should we do? So it's better.

50:18

So it's better to split documents. It's better to split documents into smaller chunks. How many of you are clear with this? So it's better to spend documents into smaller chunks.

50:41

Folks, is the idea clear to all of you that why do we need chunking? This is very important that why chunking is required.

50:46

So we have discussed.

50:48

Why chunking? Now tell me everyone, we have talked about that we will split the documents into small chunks.

50:55

Now, what is the definition of smaller? On what basis should we, should we split? Correct, ever?

51:04

So we can say that here, definitely. Chunking helps.

51:18

Chunking helps the retriever to find the relevant documents.

51:48

Chunking helps the retriever to find the relevant information more efficiently.

51:52

Now the point comes to everyone that how do we chunk?

51:56

So if the very simple approach of chunking is fixed size chunking.

52:03

Correct?

52:04

So there are different chunking strategies which are there, which are present out there, but the simplest one and the easiest one to implement is fixed size chunking.

52:15

That you can define the chunk size chunking.

52:18

Now, you can say that, okay, for example, example, you say that, okay, let's say the chunk size is,

52:26

for example, let's say 100 words. Just an example, 100 words. It means that even the first 100

52:31

words will go to chunk number 1, 101 to 200 will go to chunk number 2, 200 1 to 300 will go to chunk number 3,

52:39

300 1 to 300 will go to chung number 3, 300 1 to 400 will go to chunk number 4 and so on.

52:42

Is the very basic understanding clear to all of you? This is how you can chunk, correct?

52:48

So if you have, for example, if you have, let's say, 1,000 words, okay, let's say 100,000 words in a document, you have 1,000 words, so you will have 1,000 chunks.

52:58

That document, you will divide into 1,000 chunks.

53:01

Now, tell me everyone, what do you think about this approach? Is this a very good approach? If yes, how?

53:08

Do you see any disadvantages of this approach? If yes, what? Think about it. I'm not giving you that, okay, this is the final answer.

53:15

You tell me, what do you think? Is it is a very good approach?

53:18

Yes, why? It is a very bad approach. Yes, why? It is a convenient approach? Absolutely correct. Very easy, very

53:26

convenient, very simple, straightforward to implement. It's very flexible. It's not flexible. Not flexible. Okay, yes, correct.

53:33

Basic approach, but not flexible, absolutely correct. Disadvantages of losing the information. Absolutely correct.

53:38

Now, first of all, everyone, the biggest disadvantage of these approaches, we can lose context which are longer than 100 words.

53:47

you can take 500 words. Now, this is just an example. What if you can take 500 words? You can take

53:53

1,000 words. It's up to you, right? Right? So 100 is not fixed number.

54:03

Still, okay. Let's say everyone, first of all, this number is not fixed. You can take it 100, you can take it 500,

54:09

you can take it 1,000, whatever you want, whatever works best for you. So first of all, everyone, why this approach is most frequently used, most widely used.

54:17

right? Absolutely, how to decide is a challenge. We can identify the sections for better embeddings.

54:23

Very good. We'll come to that. Now, let's discuss this. So this number you can decide. But still,

54:27

everyone, if you are having a fixed size chunking, right? Let's say even there is some document, right?

54:34

This is how the sentences are written. Whatever this number you have chosen, 100 or 500 or 200 or 120 or 5,000, 1000 does not matter. Let's say, everyone, this is your

54:47

starting point, right? Whatever limit you have chosen, so you start hydrating, start

54:53

hydrating, start iterating, start iterating, start iterating. Let's say at this moment, your limit

54:57

completes. For example, let's say 100 words. So from starting, you have completed the 100 words here.

55:03

So this goes to chunk number one. Is that idea clear to all of you? So let's say everyone,

55:07

this particular thing goes to chunk number one. Then from the next thing, everyone, from the next place,

55:15

let's say from here, you start chunk number two, okay? And here, everyone, let's say,

55:22

your chunk number two gets completed. So this is your chunk number two. And from the next place,

55:31

everyone, your chunk number three starts, okay? And so on. Now, do you say that everyone,

55:38

that if you just keep on dividing from anywhere, you might end up losing the context about the

55:44

information. For example, even, let's say there was a sentence which started from here.

55:49

So this is the sentence, same sentence, same sentence, same sentence. That sentence is getting

55:54

completed here. If you just randomly divide in between, it means that half of the sentence, some

56:01

part of the sentence went to chunk number one, some part of the sentence went to chunk number two.

56:07

Now, don't you think you want that you will end up losing the context?

56:11

So for example, you were reading a book, right? You started.

56:14

a topic. Now, just in between the topic, the book gets completed. Now you say that, okay,

56:19

go to that page to read that remaining part of the topic. Don't think it will lose the context,

56:24

right? You will lose the interest of reading that complete topic. So if the topic is getting

56:29

started, ideally, the entire part should be present at one place, ideally. Yes or no? Correct,

56:36

everyone? So this is one thing, right? This is the disadvantage of this approach. Apart from that,

56:40

there is no disadvantage. Now everyone, this number can be chosen, like,

56:44

there might be this idea that how to choose this number, 100, 200, 500, 1000, how?

56:51

There is no fixed answer to everyone. No one in the world can tell you that, okay, 500 is going to work,

56:55

thousand is going to work, etc. So what do you do, everyone? You start with a guess.

57:00

That, okay, let's say, based on my documents, let's say my documents are very big. So I will go

57:04

with, let's say, maybe 500 words per chunk. Then you analyze the quality of the answers.

57:09

Because don't you think, everyone, that if your chunking approach is very good, then your

57:14

quality of answers will be very good because you are not losing the you are not losing

57:19

a lot of context. Your quality of answers will be decent. It means that your chunking is very

57:24

good. But everyone, if your quality of answers are not good, if the quality is not very good,

57:29

it means that you will try to tweak the process of chunking. So you might reduce the number,

57:35

you might increase the number. So after some point of time, after certain experimentations, you will

57:40

find out that which chunk number is working best, which chunk number is not working best.

57:44

So you will come up with a final chunk size. So there is no straightforward answer

57:49

that 100 is going to work or 500 is going to work. So you will have to find out with the proper

57:53

experimentation process. Idea clear to all of you? Okay. So guys, now, although there is

58:01

a disadvantage of this approach, but still fixed size chunking is used a lot. There is other

58:06

approach that we don't, that we will not discuss in a lot of detail because that is not required,

58:11

that is not used very frequently, and slightly more complex to implement.

58:14

But what that approach says is, that approach says the idea is, that is called a semantic chunking.

58:27

Okay? I will just give you the idea that is called a semantic chunking. Now, what is the meaning of

58:31

semantic chunking, everyone? As the name suggests, that don't chunk, though, don't create the chunks

58:36

from the fixed size. Don't create chunks randomly. Create chunks based on the semantics, based on the

58:43

understanding, based on the meaning.

58:44

For example, try to implement some algorithm in which you can figure out that, okay, if there

58:51

is a sentence starting here and that sentence is ending here, don't create a chunk in between.

58:56

Complete, try to complete as much as possible till the end of the sentence. Once the sentence gets

59:01

completed, then create a new chunk. Obviously, everyone, in the semantic chunking also,

59:06

you decide some chunk size, but that is not strict chunk size. You say that, okay, I will not go

59:11

more than thousand words. But if there is a chunk less than thousand words, I'm okay?

59:14

If there is a chunk slightly more than 1,000 words, I might be okay. But I will give more

59:20

priority on the semantics, on the meaning. Makes sense for all of you? It is very difficult

59:25

to implement. Because it's very difficult to find out that where the sentence is getting completed.

59:30

What is the complete meaning? Because everyone, there might be some paragraph. In that paragraph,

59:37

let's say there are multiple sentences. All those sentences are connected to each other.

59:40

So, it's not 100% possible with 100% probability that you will put all the correct

59:46

all the connected statements or all the connected, what do you say, sentences in the correct chunk,

59:53

in the same chunk. So it is not 100% proper algorithm, but still it is better than fixed size chunking,

59:59

but at the same time, it is very difficult to implement.

1:0:02

Ideally, can't we assume that heading based chunk? Very good. That is also one approach.

1:0:07

That is called a hierarchical chunking. Okay? What shows?

1:0:10

I saying that, can't we just create chunking based on the, chunking based on the paragraphs,

1:0:17

chunking based on the topics, based on the heading? You can do that, that is called as heretical

1:0:21

chunking. There is other approach which is called as hierarchal chunking. But the disadvantage of

1:0:27

this approach is hierarchical chunking. Some topics can be very small, just two lines, some topics can be

1:0:33

two pages. So there will be a very big difference between the size of the chunk, right? Some topics

1:0:39

can even span up to three to four pages also. So the document, the chunk itself can be

1:0:45

very big. Okay? That is one disadvantage. But apart from that even like different use cases,

1:0:50

different things works for different companies, different type of documents. But I hope the idea

1:0:55

clear to all of them. Right? So guys, we are going to follow fixed size chunking, easy to implement,

1:0:59

and serves our purpose. Okay? Idea clear to all of you? Okay. Now folks, forget about

1:1:09

Semantic chunking, forget about hierarchical chunking. Focus on fixed size chunking.

1:1:13

In fixed size chunking, you decide some number. Let's say, I decide number 100. 100 words per chunk. Idea clear.

1:1:20

Folks, idea clear to all of you. Fix size chunking per chunk, 100 exact words. But now tell me,

1:1:29

everyone. Still, in the fixed size chunking, we saw that. Let's say from here, you start and 100 words are getting

1:1:35

completed here. But the sentence was not complete. Let's say sentence is a sentence.

1:1:39

is getting completed here. So don't you think that some sentence which started here,

1:1:44

some part of it going to chunk number one, some part of it going to chunk number one, some part of it

1:1:47

going to chunk number two. So it is definitely a bad idea in which we will lose the context.

1:1:55

Correct? Some part chunk one, some part chunk two. Can we find out some workaround, some

1:2:01

some jubar, some different approach in the same, can we do something else?

1:2:09

in the fixed size chunking also, so that we can try to retain some context.

1:2:15

We can try to retain some context.

1:2:19

That particular approach is called as chunk overlap.

1:2:30

Chunk overlap. Overlapping is a very beautiful, very simple, but yet very powerful idea. I will give you

1:2:37

first analogy to all of you, then it will make 100% sense. For example, everyone,

1:2:42

this is me and I'm working in a team. I'm working at Microsoft in a team. And let's say everyone,

1:2:50

there are 8 to 10 people in my team. And now let's say everyone, I have decided to leave Microsoft.

1:2:55

I have put down my papers. Now let's say everyone assume that I am a very critical resource to my team

1:3:01

and my manager knows that, okay, if Deepak leaves, then this particular part of, like, Deepak has a lot

1:3:06

of idea about this particular component. And if Deepak leaves and if some work comes to that

1:3:11

particular component, then it is going to be a very difficult thing for a new engineer to

1:3:15

understand in a very short span of time. It will take a lot of time. So what my team manager can do?

1:3:20

Maybe they will hire a new person from other team, from externally, or they will allot the member

1:3:25

from the team. So they will find one replacement. Maybe externally, internally, same team,

1:3:31

other team does not matter. There is some replacement for my role, okay, that I will leave

1:3:36

and this person will come to my place in my team. Correct? So guys, what my manager

1:3:40

will try to do? My manager will try to have at least maybe two weeks of overlap or one week

1:3:46

of overlap where I'm working and this person is also there. So this person will work closely

1:3:52

with me just for one way and my responsibility is to give you, is to give him or give her the

1:3:59

complete context about the work. Correct?

1:4:02

Huh? So that when I will

1:4:06

leave, this person can take over. This person has the entire context of my some work,

1:4:11

of my previous work, some part of my previous work. Definitely, I cannot give the entire

1:4:15

context of my, let's say, if I've spent five years at Microsoft, I cannot give the entire context

1:4:20

of five years. At least what I can do, I can give the context about the recent work. This is what

1:4:26

exactly overlapping also means in chunking process. So folks, if you have created chunk number one

1:4:32

from this part, and chunk number two is this part.

1:4:36

Now, guys, definitely we know that when you create a fixed size chunking, some context

1:4:42

gets loose, right? You will end up losing some context. Yes, no, everyone? So let me write

1:4:49

it down that in fixed size chunking, some context will get loose. We will lose some context.

1:4:57

Some context will be lost.

1:5:02

Some context will get lost. Some context will get lost.

1:5:06

Correct, even? Some context will get lost. Now tell me everyone, we can implement a small

1:5:13

overlap. That okay? Although it is a new chunk, this from here, we have a new chunk, but everyone,

1:5:19

we will store some part of the previous chunk along with the new chunk. It means that in chunk

1:5:23

number two, we will store last, let's say, 10 words, or 20 words or 50 words, right? For example,

1:5:29

if the chunk size is 100, we can say that, okay, let's say we will spend, we will store 10%, that is

1:5:35

10 words of the previous chunk. So that at least we will have some context about the previous

1:5:40

chunk. Are you guys getting this point? This is called as chunk overlapping.

1:5:46

Right? If let's say the chunk size is 500. It means that these are 500 words. Okay. Now abruptly,

1:5:54

suddenly we created a new chunk that from here, this is a new chunk. Now this new chunk will not

1:5:59

have any context about the previous chunk. Now you have completely detached the chunk number two from the

1:6:05

entire document. How this document, how this particular chunk number two will get the context

1:6:10

about the previous chunk. So what you will do? You will say that okay, this is chunk number one. Although

1:6:15

I cannot store the complete chunk as it is, but still what I will do, I will store only,

1:6:19

let's say maybe 20 words along with chunk number two. From these 20 words or one sentence or two

1:6:25

sentences, depending on the length of the chunk, at least the next chunk will get some context

1:6:31

about the previous chunk. Exactly the example that I gave you. If you,

1:6:35

if I am leaving the team, you can hire an, hire an alternate person or hire a replacement

1:6:40

that will spend one week of overlapping time with me in the office so that I can give them the context

1:6:45

about my work. Is the chunk overlap meaning making sense to all of you? Yes or no. Is the overlapping

1:6:53

part clear to all of you? Sometimes I think I get very good analogies right at some point of time.

1:7:02

Sometimes I ruin also, right? We can kinder turn them into Legos. Yes, we can

1:7:10

we can say that. But what exactly do you mean by that? Shaura, if you can elaborate. It would

1:7:16

be good. I did not get the complete idea.

1:7:27

Absolutely, correct. It is the kind of same thing. Okay. Kind of the same thing.

1:7:32

thing. So they are still connected, absolutely correct. So guys, now, very good.

1:7:39

So we are clear with chunking and the overlap part. Now, tell me, should we have very small chunks

1:7:46

or should we have bigger chunks? What do you think about it? Should we have very smaller chunks?

1:7:52

Or should we have large chunks? Let's talk about that if you have very small chunks.

1:8:02

If you have very small chunks, what is the advantage? It is easy to search, easy to store,

1:8:08

easy to retrieve, correct? Searching will be fast, creating embeddings will be fast, everything

1:8:14

will be fast. But don't think even if the smaller chunks are there, if you're creating chunks

1:8:19

which are very small, then accuracy can be a problem. Absolutely correct. Because in smaller

1:8:24

chunks, you might not be able to store the entire context of something. Right? You will end up losing

1:8:29

the context, correct or not? So at the same time, everyone, if you have large

1:8:37

chunks, then you will be able to store more context. The chances of losing the context in larger

1:8:43

chunks can be very, like, the chances are very less. You will not lose a lot of context. But at the same

1:8:48

time, everyone's searching or retrieving from the larger chunks is time consuming. So that's

1:8:53

when you try to balance the chunk size. You don't go very small, you don't go very big. You don't

1:8:59

choose very small chunk size. You don't choose very large chunk size. You try to balance

1:9:03

maybe 200, 300 words, not more than that. Generally for small documents, maybe 100, 120,

1:9:10

150, maximum 200 words works absolutely fine. And a chunk overlap of maybe 10 to 20%, not more than

1:9:17

that. Okay? For example, if your chunk size is 100, then maybe having a overlap of 10 to 20 words

1:9:24

is good enough. Make sense, everyone?

1:9:29

folks clear also about the overlap aren't we dealing with duplicate data we are dealing

1:9:37

with that is the disadvantage that is a trade off right because the fixed size chunking is very easy

1:9:41

to implement so you are giving the like your trading of some part of space that there might be

1:9:47

some duplicate data that is okay but what benefit we are getting out of that the easy implementation

1:9:52

again there is no fixed percentage generally it is 10 to 20% not more than

1:9:59

that okay there is no fixed number generally 10 15 20% is more than sufficient it's okay to have

1:10:06

okay so after chunking everyone first what did you do loading the documents load the documents

1:10:14

parsing plus cleaning then chunking right after chunking everyone you create the embeddings

1:10:19

and embedding is something everyone which we have

1:10:22

talked about n number of times correct embeddings is something which we have

1:10:33

talked about i think 10 times okay so it's exact 9 p.m we can take a break and after the break we

1:10:39

will talk about embeddings we'll spend 10 to more 10 to 15 more minutes on the understanding part then

1:10:44

we will directly move to the implementation okay so in today's class we will focus on the implementation

1:10:49

as well so it's 9 p.m sharp everyone let's take a break off maybe maybe

1:10:52

10 12 minutes yeah time to check the election results also right okay so it's 9 p.m

1:10:59

let's meet around 912 9.13 okay 10 to 12 minutes of break after the break we'll start with the implementation

1:11:04

okay see you after the break everyone

1:11:22

Thank you.

1:11:52

Thank you.

1:12:22

Thank you.

1:12:52

Thank you

1:13:22

Thank you

1:13:52

Thank you

1:14:22

Thank you

1:14:52

Thank you

1:15:22

Thank you

1:15:52

Thank you

1:16:22

Thank you

1:16:52

Thank you

1:17:22

Thank you.

1:17:52

Thank you.

1:18:22

Thank you.

1:18:52

Thank you.

1:19:22

Thank you.

1:19:52

Thank you.

1:20:22

Thank you.

1:20:52

Thank you.

1:21:22

Thank you

1:21:52

Thank you

1:22:22

Thank you

1:22:24

Thank you

1:22:26

Thank you

1:22:28

Thank you

1:22:30

Thank you

1:22:32

Thank you

1:22:34

Thank you

1:22:36

Thank you

1:22:38

Thank you

1:22:40

Thank you

1:22:42

Thank you.

1:23:12

Thank you.

1:23:42

Thank you.

1:24:12

Hi everyone.

1:24:16

Hi everyone. I'm audible.

1:24:42

Okay.

1:24:49

So guys, let's talk about the embeddings.

1:24:51

I think everyone knows about embeddings.

1:24:53

Embeddings are nothing but a vector of numbers.

1:24:57

So after chunking, we convert each chunk into embedding.

1:25:12

After chunking, we convert each chunk into embedding.

1:25:37

Make sense everyone?

1:25:42

Okay, now folks, for embedding also, do we need a separate embedding model?

1:25:51

Correct?

1:25:56

Yes, we need a separate embedding model.

1:26:01

So folks, for our use case, as we have used previously also, we will go with the same GPT small

1:26:08

text embedding model.

1:26:09

What is the exact name for that?

1:26:11

Text embedding 3 small.

1:26:12

Small.

1:26:26

Text embedding 3 small.

1:26:27

Everyone clear?

1:26:32

How many dimensions does it give you?

1:26:35

Anyone remembers?

1:26:37

How many dimensions does it give you?

1:26:39

1.5, 3, 6.

1:26:41

6. Correct? And there is a large model.

1:26:48

Right? There is a large model. This is a large model. And this large model gives you how many embeddings?

1:27:04

Double of this. This is 3072. Correct?

1:27:10

So, this is one component, everyone.

1:27:12

Everyone knows about embeddings.

1:27:13

Then everyone, finally, we are going to store embeddings into vector database.

1:27:19

Okay?

1:27:20

So vector database, we will store the embeddings internally.

1:27:23

Now, in vector database, everyone, what all the details we store?

1:27:28

If you remember, we store the chunks, we store the chunks, then we store their corresponding embeddings.

1:27:39

Correct, everyone. Then we store their metadata also. Yes and everyone? We store the chunks, we store the embeddings, we store their metadata as well. Correct or not?

1:27:59

Everyone clear? So yes, whatever we have seen as of now, document loading, parsing, cleaning, chunks.

1:28:09

and embedding and storage. All of this is kind of a pre-processing step, right?

1:28:15

So as of now, user is not involved anywhere. So as of now, you have just prepared your system.

1:28:20

Now here comes the retrieval component, retriever.

1:28:23

Retriever. Here comes the retriever component.

1:28:31

Correct, even? Now in retriever component, what do we have? We get the user query.

1:28:37

Then we convert the user query into the user query.

1:28:38

user query into embeddings, then perform similarity search to find similar chunks, then return

1:28:43

top k chunks. Corrective one. So we have the user query. We have the user query. We convert

1:29:05

query into embedding.

1:29:08

Then find chunks relevant to the query.

1:29:23

Or find relevant chunks relevant chunks.

1:29:37

Find relevant chunks and we will return top k chunks. Is that point clear to all of you?

1:29:53

Correct. And then everyone, we will have to write some prompt as well. Okay? If you remember in the last class also, if I show you, we wrote some prompt.

1:30:02

Let me search for prompt. Yeah. So this prompt everyone, we gave.

1:30:07

that you are a helpful, helpful customer support agent. And everyone, if you see, answer

1:30:11

the customer's question using only policy documents, right? Using only policy context. Do not make up

1:30:17

the policy details. If you don't know the answer, just say, I don't know the answer. Don't try to make up the

1:30:22

answers. Keep the answer simple, clear and customer friendly and so on. This is called as the prompt,

1:30:28

the rag prompt or the system prompt. Makes sense? So this component we are going to use today as well.

1:30:35

Is that, is that point clear to all of you?

1:30:37

So now everyone, we are ready to build the project. If yes, we can start and

1:30:44

writing the project, writing the code. We can start writing the code now. Okay? Okay. So what

1:30:52

we're going to do everyone is that we will, we have e-commerce rap. So should we create,

1:30:58

actually we can create either we can create a new project or we can create the same file, like in the same project.

1:31:07

we can use the same project and create a new project. So what should, what name should we give?

1:31:17

I think name will be confusing then for all of you. Maybe in the same project, I can create a new folder

1:31:22

internally to this, let's say, production rack or let's say advanced rack. Okay, and inside this

1:31:32

we can create a new project, a new file, let's say advanced e-commerce rag.

1:31:41

Okay, and inside this we will create a folder which is policy documents.

1:31:48

Okay, and here we will create all the policy documents. Is the, is the project cleared all of you?

1:31:54

So that both the rack components are in the same, are in the same project folder. Okay.

1:32:02

Okay, so we will create, we will go inside the advanced rag now and inside the

1:32:07

advanced rack we will create a new, what do you say, the virtual environment, Python 3,

1:32:13

M, V-E-N-V, V-E-N-V.

1:32:16

V-E-N-V-N-V.

1:32:18

Yes, and initiate this, activate this.

1:32:32

Okay, activated this.

1:32:37

And now we can start writing the prompt, we can start writing the code here.

1:32:41

Okay, so folks, we will have to install multiple libraries here.

1:32:44

We will have to install OpenAI, ChromaDB, then what do you say?

1:32:52

The OpenEI API, I can store in the environment variable.

1:32:55

Then we would need Pi PDF that we will use, that we will keep on installing whenever we need it.

1:33:00

But first of all, we can import Open AI.

1:33:02

Sorry, not import opening what I'm doing, Python 3.

1:33:09

Python 3.

1:33:11

Folks, what I'm doing, PIP3, I'm doing.

1:33:32

Guys, first of all, do you know that?

1:33:34

For example, let's say in any project, you know that, okay, I have to install 10 dependencies.

1:33:40

You will have to install all the 10 dependencies one by one like this.

1:33:44

Do you know how can we install multiple dependencies in one go?

1:33:48

By having a Requirements.TXT file?

1:33:52

Okay, let me show that to you if you're not aware.

1:33:55

So inside this folder, everyone, you can create a new file, which is, let's say, called it requirements

1:34:00

dot TXT file.

1:34:02

Okay, this is a general convention, naming convention.

1:34:05

And here, everyone, all the, you can mention all the dependencies that you want.

1:34:08

For example, I need OpenEI dependency, I need ChromaDB dependency, right?

1:34:14

Then we need a Pi PDF dependencies, right?

1:34:18

Let's say we need these three dependencies for now, okay?

1:34:21

And what you can do everyone is, you can do like this, PIP3, install,

1:34:25

hyphen R, requirements. TXT. What this PIP3, install,

1:34:31

R does this, hyphen R means recursive, that it will go inside the file and it will keep on installing

1:34:36

all the dependencies which you have mentioned inside the file.

1:34:39

So if you just press enter, you will see that all the dependencies will get installed automatically.

1:34:44

Now, assume that if you have 20 plus dependencies, so you don't have to install 20 plus dependencies

1:34:49

one by one, one, just mention all the dependencies in Requirements.tXT, execute the command once, and

1:34:55

all the dependencies will get installed in one shot, right?

1:34:58

If you see, all the three dependencies have been installed automatically.

1:35:01

It's a good way, right? It's a very common way that is being used out there. Sounds good?

1:35:08

Sounds good? Okay. So, folks, what we will do? We will import from OpenEI, import, open AI, from Pi PDF, import,

1:35:31

Okay. So for now we are using these two things and we will, we can also import ChromaDV.

1:35:41

Okay. So first of all, everyone, we need to create the Open AI client. For that, we would need

1:35:46

the API key. For that, I will go to my Open AI account and show you the API key.

1:35:55

Go to the API key.

1:35:56

create a new API key. Let's say 4th May. Copy the API key. Stored it as an environment

1:36:10

variable. How do we store an API key as an environment variable? Simply export OpenAI underscore API

1:36:17

underscore key is equal to this. Do that. Right. And that's it. And that's it. And now you can create

1:36:24

a client open AI. So let's say client is equal to opening. That's it. Now, once you

1:36:33

define that in the environment variable, you don't have to put the API key inside this, inside the

1:36:39

open AI function. So that it will automatically read it. Makes sense? Folks clear.

1:36:44

Then if you want, we can define the LLM model. I think, have I told you that when do we use

1:36:48

these variables generally? And we can also define the embedding model.

1:36:54

Okay. So that if you're using the LM model at multiple places, you don't have to

1:37:00

change it again and again in case in future you are, you are required to change this model. Just

1:37:05

change at one place. And you can use this variable everywhere. And for the model, everyone,

1:37:10

for the embedding model, you have text, hyphen embedding, hyphen, embedding, hyphen, small. Does it

1:37:17

make sense to all of you? Folks, makes sense?

1:37:24

Okay, then everyone now, what we're going to do is we will have multiple folders.

1:37:33

I already have a lot of data curated before the class so that we don't have to spend time in

1:37:39

the class in this simple thing. So folks, what we're going to do is, for example, this is a refund

1:37:46

policy data. I will copy paste it. And in fact, the code itself is very big. So we will create

1:37:52

a file, let's say we will have this is return policy, return underscore policy dot PDF.

1:37:59

Okay, we will create this as a PDF and inside this PDF.

1:38:22

This is return policy. Save it. And now I think I can rename it.

1:38:52

here. So what we can do is, what we're going to do is, what we're going to do is, I think it should be fine. Okay. So what I can do is, let's go to Google Docs. Return.

1:39:22

policy and folks I can download this other PDF.

1:39:52

supporting the PDF documents. I think we'll have to download some login maybe.

1:40:22

So the document is valid. So how VS code is not able to you,

1:40:37

you, VS code is not able to display the content of that file. Okay. Let me restart VS code now.

1:40:52

Yeah. Do you see that now? After installing that, after installing those plugins, it is able to show the content.

1:41:10

Folks, clear to all of you? In fact, now I think we should be able to create it from there only, from here, from here, from VS code only. Let's say next is refund policy. Let's see.

1:41:22

here, refund policy, refund underscore policy.pdia. And once you do that, it is not

1:41:34

allowing like this. Yeah, so what I can do, I can create a document separately, refund policy,

1:41:42

and then copy paste here.

1:41:52

For now, I think for testing purpose, only two documents should be good enough.

1:42:00

Later on, we can create any other number of documents as well.

1:42:04

Done and copy and paste.

1:42:11

Yeah, if you see everyone, this is a refund policy document. Is everyone aligned? What we are doing here?

1:42:20

So let's assume that for now we have just two sample documents. Okay? We can have more documents as well. Let's take one more as well.

1:42:28

Okay, so we can go to...

1:42:34

Thank you.

1:43:04

Yeah, this is shipping policy. Everyone, clear? Okay, what I'm doing, Pratiyush is

1:43:14

saying, no, not visible, how you are doing? I'm going to Google Docs, creating a new document,

1:43:20

downloading it as a PDF. It will come to my download folders, then copy and then paste it here,

1:43:25

simple. Okay, that screen was not shared actually. Yeah, that is very straightforward process.

1:43:31

Okay, so after this everyone, what we're going to do is.

1:43:34

the next step is. Okay. Now, folks, we have around half an hour remaining.

1:43:50

We will not have the, like, the code is very big. So what we are going to do is, I will copy paste some

1:43:56

of the code wherever required, and I will keep on explaining you everything with step by step. Okay, so instead

1:44:01

of writing everything from scratch, we will follow a slightly fast,

1:44:04

forward approach. Okay? So folks, first of all, we will have the function to load the documents.

1:44:14

Okay? So this is a function to load the documents. So let me copy paste it and we will try to understand one by one.

1:44:34

So first, everyone, what we are doing is, we have this function called as infer policy type.

1:44:47

If you see what this function does is, we have the name of the file.

1:44:51

So for example, the name of the file is refund policy.

1:44:55

So what this refund policy, infer refund policy type does is, it will get the name of the file,

1:45:00

let's say, refund policy.com, it will get the name of the file.

1:45:03

Now, what we find is that whether that name contains return, refund, shipping, warranty,

1:45:11

cancel, exchange, whatever, right? For now, let's say we don't even have this much of task. We can

1:45:15

remove this or let it be. Now, what we do everyone is that whatever name contains, if name contains

1:45:22

if name contains return, it means that document is of type return. If the name contains refund,

1:45:27

the document is of type refund. If the name contains shipping, document is of type,

1:45:32

shipping. Is that point clear to all of you? Simple. Okay? Inferce policy type from the file

1:45:38

name. That whatever file name contains, we will take the name of the type of the document from

1:45:42

there. Make sense? So from here, we will pick refund, return and shipping. Folks, please give

1:45:48

me thumbs up every time if you understand something. Ask your doubt if you don't understand something.

1:45:55

Makes sense? We have a lot of code to write. This is very simple straightforward code. We are taking

1:46:00

the name of the file, getting what word is there, and we are just, we will just assign

1:46:05

this word while loading the document. Then everyone, the next function is load the PDF file. Let

1:46:12

me copy paste that as well. And this is the function to load the PDF file. So everyone,

1:46:18

first we give the path, path, path of the file. So how do we give the path? Copy pay, right

1:46:24

click on this. Copy path. So this, for example, this is the path of this file.

1:46:30

Okay, you can also give the relative path as well. So for example, if you are currently

1:46:33

in this folder, right? So inside this folder, you can directly give only this path as well. Policy

1:46:38

Documents slash refund policy. So what do, everyone? In this function, what you're doing

1:46:43

is you are loading a PDF file and extract the text pages by, a text page by page. You will

1:46:49

go to page number one, then page number two, then page number three, and so on. So what does that mean,

1:46:53

everyone? You are using here the function called as, or the class called as PDF reader. And PDF reader,

1:46:59

if you see coming from Pi PDF. Sounds good. So this PDF reader is coming from

1:47:05

Pi PDF. So this PDF reader functionality allows you to read the document or read the PDF document

1:47:12

page by page. How let's see? If you see, you are creating a reader and you are creating a

1:47:17

document's empty array. So what are you're doing? You are iterating through each page and enumerate means

1:47:22

this gives you an enumerate function. Python gives you an enumerate function in which you can actually give

1:47:28

an index to something. For example, it's a in PDF reader, in this reader, you, what you have?

1:47:35

It gives you, it gives you a list of pages. So you are saying that, okay, enumerate. I iterate over

1:47:41

this reader dot pages. I iterate through all the pages of the reader and start from page number one.

1:47:48

So you are just iterating every page one by one. Don't worry about the syntax a lot. Okay? You don't

1:47:54

have to remember the syntax. You just have to understand it. Right? So what you're doing is you are iterating

1:47:58

over all the reader pages, reader is coming from here. So you are creating a reader over

1:48:04

the file path, over this file. Let's say policy dot, refund policy dot PDF. You are creating

1:48:09

a reader, iterating through each document, each page one by one. And what you're doing? Creating, getting

1:48:15

the page text. So from each page, you can extract the text out of it, right? And then what you're doing?

1:48:21

Clean text. So guys, you are writing another function clean text. We will come to this function as well.

1:48:25

Assume that this function cleans the data. And everyone, if you have some clean text, you're

1:48:30

just appending it, you are just appending it at the end of the array, this array, documents

1:48:36

array. So basically everyone, if you see, if you understand this for loop, what essentially you are

1:48:42

doing. Can I say that, you are reading the PDF and each page of the PDF, you are considering

1:48:48

one document. And you are adding inside this documents array. Is that point clear to all of you?

1:48:53

So you are saying this is the source, the source type, the file type is PDF, the page number

1:48:59

is this page number, and the policy type is you are getting from inference policy, right? Whatever is

1:49:05

the name of the policy, name of the document. Now, coming to these two functions, make document and clean

1:49:10

text, right? So these are two separate functions that I have written separately. So let me write it

1:49:15

down them, let me write them, write down them as well. So this is the document everyone for cleaning the text.

1:49:23

Now, to clean the text even, if you see what comment in every function, I have written

1:49:28

proper comments as well. So what it does? It cleans the raw text by removing extra spaces

1:49:33

and line breaks. If there are extra spaces or line breaks, we are just removing them. So whatever

1:49:37

text you are giving it, this function, right? You are doing what? Just every line break, every

1:49:44

new line character you are replacing with space and you are finding extra spaces and removing

1:49:49

it from, you're just doing what? You're just stripping it.

1:49:53

Is this function clear to all of you?

1:49:58

Right? And then everyone there is a function called as make document. What this make document does?

1:50:06

You are passing the text and you are passing the metadata. So what this make document does is, it will create a document with this text and this metadata. How? Let's see how.

1:50:17

This is how. So what do you do? It creates a standard document dictionary because if you'll see,

1:50:23

If you're not following a standard template for every document, it will be very difficult

1:50:29

for you to find out the right document if you have thousands of documents. If you just have one

1:50:34

or two or five or ten documents, it is okay. But if you have thousands of documents,

1:50:38

then it will become very difficult for you to find the relevant documents. So what do you do

1:50:43

everyone? For every document in your pipeline, in the rack pipeline, what you're doing is every

1:50:48

document you are making sure that it will contain the text, the page, text, the actual text, and it will

1:50:53

contain the metadata data. Metadata simply means that type of the document, type, you can say that,

1:50:58

the policy type, whether it is a refund document or refund policy document or return policy document,

1:51:03

etc. So what do you do? You're just creating what? A simple JSON object. This is the text of the

1:51:09

document. This is nothing but a dictionary. This is the text of the document. This is the

1:51:13

metadata. And finally, everyone, you are adding all these documents after creating these documents

1:51:18

in the form of dictionary into this documents. In this, this particular thing. I remember,

1:51:23

Are you guys getting this point? So for example, even, if you call this function on this

1:51:27

file, refund policy.pdf, let's say this refund policy.pdf has 10 pages. So essentially what

1:51:33

you're doing is, you are having 10 documents now because every page is considered as one document.

1:51:38

Is that complete all of you? And for each document you are containing, you are storing some metadata.

1:51:43

So that you can easily filter something, you can easily find out something, and you are storing

1:51:48

a bit more information about every document internally. How many of you are clear with this?

1:51:53

As of now, this is the loading phase and cleaning phase.

1:51:58

Everyone clear till this point of time? Yes or no?

1:52:01

Okay? Perfect. So loading is done and cleaning is done. Then what is the next thing, everyone?

1:52:07

What is the next thing?

1:52:10

Now you can write one function like this so that,

1:52:16

yes, chunking also, we will, the next step is going to be chunking. But don't you think even now, for example, let's say you have 1,000.

1:52:23

and all the documents are present in this policy documents folder.

1:52:27

So don't you think you will have to call this load PDF function thousand times for each document one by one, one by one?

1:52:34

Correct?

1:52:36

You'll have to call this function thousand times for document one, for PDF1, for PDF1, for PDF2, for PDF4.

1:52:42

Why can't you just write a simple function which can just iterate through all the documents, all the PDFs present in this folder?

1:52:51

You just give the folder path.

1:52:52

path right and you will automatically load all the documents from that folder right this is the function for that right so what do you what do you do you give the folder path and what it does it loads all the documents right for now we are only supporting PDF right all the PDF files you can remove this so load all the PDF files from the from the given folder path right so what it does simply everyone

1:53:22

If you see, go to that folder, go to each file in that folder, and call the load function, call the load function.

1:53:32

So remove this text.

1:53:35

We are only supporting PDF for now.

1:53:39

Is that point clear to all of you folks? Yes or no?

1:53:42

So you don't have to go through all, like, you don't have to load all the PDF documents one by one, one by one.

1:53:49

Okay, simply.

1:53:51

Okay?

1:53:52

Now, next step is chunking step.

1:53:55

Folks, how many of you are able to follow me?

1:54:00

How many of you are able to follow till this point of time?

1:54:02

Very good.

1:54:10

Okay, Pradush, let me give you one more quick overview.

1:54:13

Okay, what we have done.

1:54:15

So initially first, what we did is we created all the policy documents.

1:54:18

Assume that you have thousands of policy documents.

1:54:20

All of them are in the form of people.

1:54:21

are in the form of PDF and all of them are present in one folder.

1:54:25

Make sense Pratush?

1:54:26

Pratush.

1:54:27

You have thousands of PDF documents.

1:54:29

All of them are present in one single folder.

1:54:33

Now what do you need to do?

1:54:35

You need to load all these documents and how you are loading these documents?

1:54:38

This is the logic.

1:54:40

So to load each document, you are creating a PDF reader.

1:54:43

This is coming from the Python library,

1:54:46

creating a document's empty array,

1:54:49

and you are iterating through each page of the document.

1:54:50

each page of the document.

1:54:51

And how do you iterate through each page of the PDF document?

1:54:55

Like this.

1:54:56

This is the internal Python function which gives you.

1:54:58

Now, even if you don't understand this particular thing, even if you don't know that, always whenever

1:55:04

you are going to implement these things, you are going to take help from Google, chat, GPT, etc.

1:55:08

That how to read a PDF file.

1:55:09

You will never remember this code.

1:55:11

And nobody is expected to remember this code.

1:55:13

Even I don't remember this code.

1:55:15

So you read the page text, then you clean it.

1:55:19

How do you clean it?

1:55:19

By removing extra spaces, extra lines, etc.

1:55:23

This clean text is other function that we have written here, which is just removing extra spaces

1:55:29

and extra lines.

1:55:30

After that, what do you do?

1:55:33

Then you, the array that you created, the empty array that you created documents, you add all

1:55:39

the documents, all the pages, each page is considered as one document.

1:55:43

You add each page one by one to this documents array for each PDF file, right?

1:55:47

So what do you do?

1:55:48

Text is this.

1:55:49

And this is the metadata for each page.

1:55:51

Metadata means that what is the file, path of the file?

1:55:55

What is the type of the document?

1:55:56

What is the page number is this?

1:55:58

This is page number one, two, three, four, et cetera.

1:56:00

And then everyone, what type of the policy this is a refund policy document?

1:56:03

This is a return policy document.

1:56:05

This is a shipping policy document, et cetera.

1:56:08

And you create a document and you add it inside this documents.

1:56:12

This make document function is nothing but this is creating a simple dictionary.

1:56:16

And in this dictionary, you have a key value pair that for each page

1:56:19

or each document, this is the text, this is a metadata.

1:56:23

Is that point clear to all of you folks?

1:56:26

Pratushya, is that clear?

1:56:27

And this function, what it does?

1:56:30

If you have thousand policy documents, thousand policy PDFs in one folder, you will have

1:56:35

to go through each and every.

1:56:37

So basically you'll have to load all the PDF documents one by one.

1:56:40

Instead of that, you just wrote one function so that you will iterate through each file in that

1:56:45

folder and load automatically.

1:56:48

So that you don't have to call the file.

1:56:49

the load function load PDF file again and again manually make sense so you just call

1:56:54

this function and you're done everyone clear till this point of time yes or no

1:56:58

okay so this chunk text is very simple straightforward approach chunking process so

1:57:12

we are we have written a function chunk text so what it does you everyone we are

1:57:16

following a fixed size chunking

1:57:19

in which we will give the text that we want to create chunk for, for example, one document,

1:57:24

one entire page, text.

1:57:26

Chunk size we are creating by default 120 size, chunk size is 120, and overlap of, let's say,

1:57:32

30 words.

1:57:33

Makes sense everyone?

1:57:34

Overlap of 30 words and chunk size is 120.

1:57:38

Make sense everyone?

1:57:39

Nothing as such, Shantanu.

1:57:42

Okay, so what this function does?

1:57:44

Splits text into overlapping word-based chunks.

1:57:48

So chunk size is 120.

1:57:49

overlap is 30.

1:57:51

It means that chunk 1 will have words from 1 to 120.

1:57:54

Chunk 2 will have words from 91 to 210.

1:57:57

Why 91?

1:57:59

Because chunk size is 120, but still you are taking from 91.

1:58:02

Why?

1:58:03

Because overlap of 30 words.

1:58:06

120 minus 30.

1:58:08

Are you guys getting this point?

1:58:11

Right?

1:58:11

1 to 120 one chunk, then 91 to 91 plus 120 is another chunk.

1:58:17

Then 2.10 minus 30.

1:58:19

From there, the third chunk will start and so on.

1:58:22

Okay?

1:58:23

So this is a simple, very simple, very straightforward Python function.

1:58:26

Okay?

1:58:27

Create, finding the number of words, finding all the words in the text,

1:58:31

using the split function, splitting based on the space.

1:58:34

Okay.

1:58:35

Then everyone, what you do?

1:58:36

You are iterating from the start, from the first word.

1:58:40

Then end is equal to start.

1:58:42

Let's see you are starting from the first word.

1:58:44

The end of the chunk will be add the number of chunks, add the chunk size.

1:58:49

Right. And then everyone, what do you do? You keep on, in each chunk, you keep on adding

1:58:55

the every chunk word one by one, one by one by one, one by one.

1:58:58

This is something that I think you need to understand by spending some time. Okay.

1:59:03

So essentially what you're doing is if I give you this task manually, right? Let's say if I give

1:59:08

you a document, a page, and I tell you that, okay, write down manually, pen and paper, let's say you

1:59:12

have, write down every, divide this document into chunks where chunk size is 120.

1:59:19

and overlap is 130. So what do you do? This is one document I have given you. Let's say

1:59:26

it has thousands of words. So what do you do, everyone? You start from the beginning. You take the

1:59:30

first word, write it in chunk. Take the second word, write it in the chunk. Take the third word,

1:59:35

write it in the chunk. Fourth word, write it in the chunk. You keep on doing that till 120. Once,

1:59:40

and you are also maintaining the count right that how many words you have already written. Once you write

1:59:44

120 words, you will stop the chunk number one and then you start with chunk number two. And then you start with chunk number two.

1:59:49

And chunk number two, because your count has become 120, you will subtract 30 from there,

1:59:54

that is 90, you will start from there. Getting the point. So if you see again, you will start

2:0:01

from, end means how many words you have already added, 120. And overlap is 30. So you will start

2:0:06

with 90. Getting the point. Manually, literally if you write on pen and paper, this is how

2:0:13

you will do. Word one, you will write in chunk one, right? Increment the count.

2:0:19

And if you see, you are doing end is equal to start plus, end is equal to start plus, start is,

2:0:26

let's say, initially one. Chunk size is 120. So it means that you will end at 121. Make sense?

2:0:34

Folks, yes or no? Guys, you'll have to spend some time on this. Okay. If you do that manually,

2:0:42

on pen and paper, you will 100% get it and it will be good exercise for you. Okay, if I start explaining

2:0:48

this thing, probably here it will take 100%.

2:0:49

half an hour. Okay, but I hope this is not the logic that we should focus on in the class.

2:0:54

Rather, we should focus on the AI related thing more. Okay? This is something simple data

2:0:59

structures that you should be able to understand. What if we don't have comfortable hands

2:1:04

on Python? It's not about Python. It's not about Java. It's not about anything. It's not about

2:1:07

the language. I think first of all, before starting this course, you must have gone through

2:1:15

some basic Python classes, right? Is that understanding correct?

2:1:19

So, unmole, I think that is your answer. That is answer. If you see here,

2:1:26

honestly, this is not very difficult Python for everyone. If not everyone, if this is something

2:1:34

that is bothering you, right? If this level of Python you are not very clear with, do not worry

2:1:40

about it. First, what you should do is maybe go through those first week of classes. I think,

2:1:46

what are those classes? What are those called as?

2:1:49

the first few weeks of classes, right, before the actual course started.

2:1:55

Python essentials, right? Go through those classes, everyone, introduction to Python,

2:2:00

and then you will be able to understand this code. But my opinion is always that you should focus more

2:2:05

on the logic. If the logic is something that is making sense to you, then it will not be very

2:2:10

difficult. Is the logic clear to all of you? If I give you one document of thousands of pages,

2:2:17

thousands of words, how will you convert that into chunks?

2:2:19

take first word, write it in the chunk. Go to second word, write it into the chunk. Along

2:2:25

with that, you're also maintaining the count. Count is 120. So once you reach the 120th word,

2:2:30

you will stop it. Then you will start from the chunk number two. Then you will start writing

2:2:33

chunk number two. But because there is a overlap of 30 words, although you are currently at 120,

2:2:39

you will go 30 words behind, that is 90. So we'll start from there and start writing in chunk number two.

2:2:44

This is how you do that. Okay? Very good. Once you create the chunks everyone, right? Once you

2:2:49

Once you create the chunks, okay? This is to create the chunk for one page, right?

2:2:57

One text. But don't you think even now, you will have to, because see, assume that you have one policy

2:3:02

document, let's say return policy, one policy, one policy, PDF only. This one PDF policy,

2:3:07

a one return policy, has thousand pages. Don't think these thousand pages, you are converting

2:3:12

into thousand documents? One PDF, you are converting into thousand documents first. Then for each

2:3:19

document you are creating a chunk right so you will have to write this function

2:3:23

as well create chunks okay this create chunk function what it does is if you see it will go

2:3:33

through each document it will go through each document and create chunks in each document

2:3:38

are you guys getting this point okay makes sense so this is something that you can go through

2:3:47

this. This is simple, simple thing everyone, not very difficult. Even if you don't understand

2:3:51

this point, it is completely okay. Even I can remove this particular point here, right? Here also

2:3:59

everyone, if you see, I'm giving some chunk ID and instead of this, you can create some random number.

2:4:05

Okay, instead of doing this difficult thing, you can create some random number here.

2:4:10

Okay, give some, assign some,

2:4:17

random number. But folks, what you can do is the chunk ID because every chunk you will assign

2:4:24

an ID. So what you can do is every chunk you can assign some incremental ID, 1, 2, 3, 4, 5, 6, or you can assign

2:4:32

some random number here. Okay, for simplicity, you can give some random number here. And even if you go

2:4:37

to chat GPT, everyone, right, if you ask chat GPT or even if you ask Claude here, okay, how can you

2:4:45

write the function of writing, getting a random number, right? So you can just ask Claude, GPD,

2:4:51

Gemini, etc. That give a Python program to create a Python program for generating random number

2:5:07

to be assigned as an ID. Give a simple Python program.

2:5:15

generating a random integer number. Otherwise, it can give you a very, very big, very,

2:5:19

very complex logic. Just give it everyone. And it will give you this two lines of function. Can't you just

2:5:27

use this function as it is? You know that for simplicity, if it will give you, let's say, you will have

2:5:32

10,000 chunks. Just create a random number and give it. Okay? For simplicity, it should be okay.

2:5:39

Okay, for now, I'm passing it. But I hope this is making sense to all of you, that how you have

2:5:44

created the chunks.

2:5:45

Okay, then everyone, we will create the embeddings. Embedding is super, super simple that we

2:5:50

have done, I think, 10 times now. Create embeddings, converts a list of text into embeddings,

2:5:56

and this is something that we have done already, right? OpenEI, client. We have given a different

2:6:02

name. We can give the same name. OpenEI client.D. Create Embedings, give the embedding model, give

2:6:08

the text, and it will give you the embeddings. You will return the embeddings. Sounds good, everyone.

2:6:15

Then everyone, you will have to set up the vector database now. This is how you can set up

2:6:21

the vector database. If you remember, we have done this already, right? Have we done this already?

2:6:25

ChromaDB. Persistent Client, then create a collection, give the name here, and metadata you don't

2:6:33

need to pass as well. Just give the name of the collection, okay? And get or create the collection,

2:6:38

it will return the collection. This is the collection where you can store your data, right? Yeah.

2:6:43

This is a collection where you can store your embeddings, okay? Fine. Then everyone,

2:6:49

finally you can just. I have added a lot of code in the document, in the notes, right? So, you don't

2:7:06

have to go through all of them. I'm just writing the relevant here. In the notes, I have added more information as well. If you want, whatever we have learned in the class,

2:7:13

If you understand that, you can try more hands on. For example, let's say, in the class,

2:7:17

we are just discussing how to read PDF files. In the notes, I have also added how to read

2:7:21

text files. There is a small different way because the library that you are going to use to read

2:7:27

a PDF file is going to be different than the library that you're going to use to read a text file.

2:7:31

That's it. Okay? Then everyone, if you see, what do you do? You are building the knowledge base.

2:7:38

Knowledge base means database. So first you have the collection, the folder path, the chunk size, the

2:7:43

So what do you do, everyone? First, you load all the documents, then you create the chunks,

2:7:48

right? Then you do what? Then you create the sources. What do you do? This is doc, metadata,

2:7:56

end sources. This is something that we can skip also. Not required. Sources can be skipped. Then everyone,

2:8:05

if you have some older data that are not required anymore, you can delete them. This is also something

2:8:11

that is not required for us for now.

2:8:13

Okay.

2:8:14

Okay.

2:8:15

And finally, everyone, what you do is knowledge base complete, knowledge base, creation completely.

2:8:20

So here everyone, what you are doing is you are just creating a knowledge base.

2:8:23

Let's say we are building the knowledge base.

2:8:26

Build knowledge base.

2:8:27

Knowledge base means database, right?

2:8:29

All your policies, documents, you are storing that.

2:8:31

So what you are doing?

2:8:32

Loading the documents, cleaning it, chunking it, embeddings, right?

2:8:37

And store it into vector database.

2:8:40

Store into vector DB.

2:8:42

vector DB. So if you see everyone, loading the documents, inside loading, if you see,

2:8:47

we can, we are cleaning also, enough? Inside loading, we are cleaning also. Correct? So loading

2:8:53

and cleaning done. And after loading and cleaning, we are creating the chunks. And when

2:8:58

you're creating the chunks, everyone, if you see, okay, creating the chunks, are we not creating

2:9:04

the embeddings?

2:9:12

created chunks.

2:9:13

Yeah, I think, uh, yes, so we need to create the embeddings of these chunks,

2:9:41

Correct even, create the embeddings of these chunks.

2:9:44

And finally, we need to store these chunks into the collection, right?

2:9:48

This is how you can store these chunks into collections.

2:9:51

Is that point clear to all of you, collection dot upsert, IDs, documents, documents are nothing

2:9:56

but chunks.

2:9:58

And in these chunks, everyone, we are storing the metadata and we are storing the embeddings.

2:10:03

Is that point cleared all of you?

2:10:04

Okay, actually in the document everyone, we are writing a separate function for that.

2:10:11

Let me actually write that function only for simplicity.

2:10:16

This entire logic, we have moved to a separate function.

2:10:23

That function we are naming it as index chunks.

2:10:26

So in index chunks, everyone, what we're doing is we are generating the embeddings and storing

2:10:30

into chroma div, storing into vector dv.

2:10:33

So what we're doing, iterating through each chunk one by one, getting the chunk IDs, getting the

2:10:37

text from each chunk, getting the metadata, creating the embeddings, creating the embeddings, and the embeddings,

2:10:41

and storing the embeddings into database.

2:10:43

And here everyone, in the function, this build knowledge base, you will simply call this thing,

2:10:51

right, index chunks.

2:10:54

Is that point clear to all of you?

2:10:57

So index chunk functions, it is taking care of embeddings and storing.

2:11:03

Folks, is that point clear to all of you?

2:11:07

Guys, I know the code might be looking a bit overwhelming.

2:11:11

to some of you quite possible, nothing to worry.

2:11:15

You will have to spend maybe half an hour to one hour by going through the code.

2:11:19

If you're not going through the code first and writing on your own, like things will become a bit messy

2:11:24

to all of you.

2:11:26

If you just iterate through the code yourself one by one, it will not be messy.

2:11:30

It will not be difficult.

2:11:32

Is that complete all of you?

2:11:38

And then everyone, retrieval logic we already know, okay, that we have already know that.

2:11:41

already written in the previous class. If you want, I can again write it down. So this is the

2:11:45

retrieval logic. So what we are doing in the retrieval logic? We are retrieving the top K

2:11:49

relevant chunks for the user query. So we are getting the user query, everyone. So we are

2:11:53

creating the embeddings. If we have any filter, we can add. So what we are doing everyone,

2:11:59

we are executing the query. This is performing the similarity search. Performing the similarity

2:12:07

search. And in this similarity search, folks, what we are doing, we are finding the results.

2:12:11

and we are retrieving the chunks and we are returning the data in a particular format, okay?

2:12:16

And we are returning this retrieved chunks.

2:12:18

Now folks, these retrieved chunks, what do we need to do?

2:12:21

These retrieved chunks, we need to send it to LLM, correct?

2:12:26

To generate the answer.

2:12:28

Yes or no?

2:12:29

Okay?

2:12:31

To generate the answer, everyone, what do we need to do?

2:12:34

We need to first give some prompt to the LLM, okay?

2:12:38

For that, we need to write the prompt.

2:12:40

So for that, we have written a separate function to build the prompt.

2:12:44

So guys, because see, the point is that if you're getting a user query, you'll, you are finding

2:12:49

the relevant chunks.

2:12:50

Do you think those relevant chunks, you will have to embed?

2:12:53

You'll have to insert inside the context, inside the query, inside the prompt, correct?

2:12:58

So what you're doing if you see?

2:13:00

You are adding the context inside the prompt and query so that LLM can answer in a better way.

2:13:06

If you see, the same kind of prompt we wrote in the last class.

2:13:09

You are a helpful customer support assistant for e-commerce company and do this, this,

2:13:14

this, this, this, and finally, return the prompt.

2:13:16

This prompt, we will pass to LLM to generate user-friendly answers.

2:13:20

And this is the function everyone that we're going to use finally to generate the answer.

2:13:24

And if you see, it will look very, very simple.

2:13:31

Okay, generate answer, we are giving the final, we are giving the query, the chunks that we are

2:13:36

retrieving, and finally we are getting the prompt, we are building the prompt.

2:13:39

and giving the prompt and the instructions and the model to the LLM and we are done.

2:13:46

Right? We are getting the response and returning the response.

2:13:50

Folks, how many if you're clear? Exact same process. Only you need to discuss, you need to think

2:13:55

about the Python implementation. Logic-wise, we have discussed in a very detailed way, what logic

2:14:01

we are following here. So we are more concerned about the logic. Is everyone 100% clear with the logic

2:14:07

part. Implementation, I have explained some part, and some part, I would want, I would expect

2:14:14

all of you to go through that. Okay? If you get any doubt, do let me know in the next class.

2:14:24

Okay? This is the complete thing, everyone, that we can club at one place. How to answer the question,

2:14:31

right? No need to print for now. What we're doing? First, we are retrieving the chunks while

2:14:36

retrieving the relevant chunks, everyone, we are creating the query embedding. This is the

2:14:40

retrieval model, retriever model. If you see, this is what retriever is, right? Retriever, and this is

2:14:49

generator. And rag is nothing but two things, right? Retrieve and generate. This is how we can

2:14:56

simulate the entire process. Fuchs, is that point clear to all of you? Yes or no.

2:15:06

Folks, is that point clear to all of you? Now, folks, if this is clear, if you understand

2:15:12

till this point of time, after the class, maybe tomorrow, day after tomorrow, over the weekend,

2:15:17

spend some time. Once you're comfortable with this, then I have added some extra reading material

2:15:22

for all of you in the notes. In the notes, you will find out that there are some extra functions

2:15:27

like text processing, text cleaning, right? For example, chunk processing, like chunk comparison also.

2:15:33

For example, let's say, if you create a chunk size of 100, that is working better, or chunk

2:15:39

size 120 is working better, chunk size 200 is working better. I have added that comparison logic in the

2:15:44

notes. But that is not the priority for all of you at this moment. For all of you, the priority is the first

2:15:50

priority is to understand what we have written in the class. Everyone clear? What we have written in the

2:15:55

the notes is the second thing that you should do. What we have written in the class in this visual studio

2:16:01

code, that is more important. So let me come.

2:16:03

submit this code, everyone, before I forget about it.

2:16:07

So we have successfully completed a very, uh, you say, what do you say, like, a very complex topic and very important topic as well at the same time.

2:16:33

First thing that you need to understand is this advanced rag part, okay, this thing,

2:16:38

these three things you need to understand first, these three folders, okay?

2:16:43

Everyone enjoyed the class. Do you want to have a quiz? If you have five minutes of time,

2:16:49

if you have energy, can we have the quiz? Okay, perfect. I think we did not have quiz in the last

2:16:56

class as well, right? Because I think we spent more time. Correct? We did not have quiz in the last class.

2:17:02

Or did we?

2:17:03

Did we have the quiz in the last class?

2:17:08

We didn't, right? Okay. Then it is good.

2:17:12

So let me just find out the quiz and let's have the quiz right now.

2:17:20

So may you launch the poll?

2:17:24

Yeah, it's done so I thought of it.

2:17:26

Okay, okay. So let's have the poll first, everyone.

2:17:33

Folks, please take the poll first and then we will have the quiz and then we can end the class.

2:17:45

First poll, then quiz.

2:18:03

Folks, please take the poll. I think there are around 10 people who have not taken the poll.

2:18:33

Thank you.

2:19:03

Folks, around seven people are there who have not taken the poll. Please take it.

2:19:08

And if you have taken the poll, you can join the quiz.

2:19:11

We can start it just in two minutes or one minute.

2:19:18

Kushel, I think that is very minute detail about the model. I'll have to check that particular

2:19:24

thing. I'm copy-pasting your question. I'll check this maybe after the class.

2:19:28

Okay, I have copied your question.

2:19:31

Folks, if you have taken the poll, please join the quiz from the QR code that you can see on the screen.

2:19:42

Sure, Cushul.

2:20:01

I've done mostly with the feedback poll. So it is not moving. So folks, please join the quiz. We'll start it right now.

2:20:13

Should we start the quiz now?

2:20:17

Okay. So here is the first question, everyone.

2:20:31

Folks, very straightforward. Which

2:21:01

for finding, searching, retriever, retriever component, right? Second question.

2:21:08

In which database generally the story?

2:21:31

Oh, sorry, I should not.

2:21:46

I thought the question is over.

2:21:48

Almost all of you got it right, vector database.

2:21:55

Third question.

2:22:00

Thank you.

2:22:30

RAD helps to reduce.

2:22:45

Very good.

2:22:47

Hallicination.

2:22:49

Fourth question.

2:22:59

Thank you.

2:23:29

What is the process of finding relevant content called retriever?

2:23:36

Last question, everyone.

2:23:41

What converts text into numerical meanings?

2:23:59

Very straightforward embeddings, right?

2:24:17

Okay, almost all of you got it right. Very good.

2:24:20

So let's finally see the...

2:24:29

I think there must be some mistake. I created only five, five questions, right?

2:24:38

So how nine questions?

2:24:40

I think there is some overlap. There is some mistake. So total there are five questions only.

2:24:54

Okay, anyways, right? So we are done with the quiz. So remaining questions are just overlap of previous ones.

2:24:58

Okay.

2:24:59

Anyways, so I hope all of you enjoy the class. We are done with the feedback. We are done with the quiz.

2:25:04

I have uploaded in the notes as well, everyone.

2:25:07

So you will be able to find the notes at the same link.

2:25:10

If you go to the GitHub account and agentic design batch, you will be able to find the notes here only.

2:25:15

I just upload it right now.

2:25:18

Where, where, where?

2:25:29

So these are the notes for today's class.

2:25:35

Okay. Thank you so much everyone. We can end the class now and feel free to drop off.

2:25:41

Have a good day. Take care and bye. I hope all of you enjoy the class. Thank you.

2:25:46

Have a good day. Take care and bye.

2:25:48

Okay. One last thing. Let's mark the topics as well.

2:25:51

Finally I can recall that.

2:25:54

Okay. So expand the knowledge base. This is done. Ingesting the documents.

2:25:59

done. Processing, organize the data done. Applying chunking policy to documents done.

2:26:04

Configuring chunk size and overlapping done. Comparing chunk size outcomes done. We compared small and

2:26:11

large chunk sizes. Generate embeddings to policy. Policy chunks. Yes. Done. Storing policy data in

2:26:18

the vector database is done. Retrieval layer done. Construct prompt template. Yes. We wrote the function

2:26:25

build prompt for L.D.

2:26:29

them, done. N-to-end multi-end multi-document rack system done. This is what we did as well.

2:26:35

Handling updates to the policy. This is what I have added in the nodes. This is nothing but when

2:26:39

you have any update in the policy document, when some policy document gets updated, you might have to remove

2:26:45

the previous chunks and add the new chunks. Okay, create a new chunk. Remove the previous one with

2:26:50

the chunk ID, metadata, and add the new chunk. I have added in the nodes. You can refer that. Okay.

2:26:56

That's it. So this is what we wanted to discuss everyone.

2:26:59

a good day. Take care and bye-bye. See you on Wednesday now. Thank you, sir. Thank you everyone for