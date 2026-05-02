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

Yeah.

12:10

everyone to join in then we can start i think the voice is clear to be everyone right can you hear me

12:40

Yeah, let's wait for everyone to join and then we can start.

13:10

Thank you.

13:40

Thank you.

14:10

Goatom Python can not directly be used for calculations and assumptions, right? It can do only mathematical calculations, it won't be able to do right.

14:40

intellectual predilections in those cases, LLM only we have to use.

15:10

Thank you.

15:40

Thank you.

16:10

Thank you.

16:40

Thank you.

17:10

Thank you

17:40

Thank you

18:10

Yeah, I think my screen is

18:17

Yeah, I think my screen is visible now, right?

18:24

Can you hear me?

18:25

Yeah, I think one more minute we can you hear me?

18:40

Thank you.

18:47

Thank you.

18:48

Thank you.

19:10

Thank you.

19:40

I think we can start. Is the voice clear to everyone? So let's start with today's part.

19:45

In the last class, I think you remember that we discussed how to write a prompt. We discussed about how prompt can be written in an advanced way. What is advanced prompt engineering and a lot of different things we talked about.

19:59

Today we will start with a new topic. This particular new topic, we will talk about what is reflection and a lot of different concepts we will try to understand. That will help us improve

20:10

the prompts. Like today also the main thing that we will try to cover that whatever

20:15

prompts we were writing till the last class, right, that how can we actually improve it and what are the

20:21

different things that we can do? So yeah, that is the main idea and agenda for today. So one by one,

20:27

we can get started and we can discuss. So yeah, let's start with this particular part that I think

20:33

the idea is clear, right? That till the last class we talked about different, different things that are related to prompt.

20:40

like advancing techniques that are there, different techniques that what a prompt should have.

20:45

Today we will try to see that how a prompt can optimize itself, what is self-reflection, what is self-correction,

20:53

what is iterative prompting, all these things one by one we will talk about. I think the idea is clear to everyone, right?

21:03

Yeah, so let's start with this particular part. First, let's see different examples that are present and then

21:10

we can talk about what all is happening. So we can see here this thing that, for example, if a customer

21:16

is saying that I ordered a jacket 10 days ago and it hasn't arrived, what should it do? So AI can directly

21:23

say that please contact customer support for assistant. So this is not what AI is actually saying.

21:30

This can be hard coded as well, right? You can write a basic program also, which can give this kind of

21:36

output. AI should give everything, like AI should be able to give actionable steps that are

21:42

there. It should give complete steps to the user because these kind of standard messages, we can hard

21:49

code also. So you will see this, that we will try to understand that what thing, reflection is doing

21:55

and what is reflection? One by one, we will talk about it. So you can see when AI is not giving

22:01

any actionable step, it is not showing any empathy or your agent.

22:06

is not giving correct answers, right? Like, for example, it is giving some answers, but it's

22:11

not the best answer that is there. In those cases, what we can use is, we can use this self-reflection.

22:18

As you can understand that it is made up of two words. The first thing is self. The next thing is

22:24

reflection. So it's basically a mechanism in which a AI agent, what it will do is it will try to

22:32

review, evaluate, and revise it only.

22:36

output without delivering anything. Like, for example, I ask any question with charge

22:42

EBT, it gives me a result. Rather than giving me the result directly, what it will do is, it will

22:48

first understand whatever it has generated. It will try to review that. And based on that review,

22:54

it will try to evaluate whether everything it has answered or not. And then only it will give

23:00

the result to the user. Is this part, are you able to understand? That, like, if you are

23:06

giving any particular exam, you write some answer. Then you try to review it, that any particular

23:10

point you missed or not. If you feel that you haven't missed any point, then more points you try to add.

23:16

Is this part clear? Is everyone able to understand this thing?

23:23

This idea is clear, right? That what idea we are talking about?

23:29

Correct. So let's go to the next point that we are having, that what will happen with reference?

23:36

and what will happen without reflection? Today also you will see that these some classes,

23:42

right? I think first 15 classes that we are having, they will be a little bit theory oriented.

23:48

So these kind of examples only I can show you and I can help you relate with all the real life

23:54

examples that are there. Later on, once we go into the cohort right, we will try to see that like

24:01

how we can actually implement these. But currently understanding theory to

24:06

part is also important. So these sessions might have a lot of theory, but we don't have to worry.

24:12

Later on, as we go into the course, we will try to see the optimal part as well. We will try to see

24:17

the live implementation of these things also. So yeah, one by one, let's discuss these examples.

24:24

Like for example, if I ask AI that generate a healthy routine that is there. Like for example,

24:30

if you see here, this box that I have written, that I want to generate a healthy morning routine,

24:35

which is including waking up early exercising, eating a good breakfast, staying hydrating

24:41

is also important. So if I write something like this, then a lot of things are missing that what kind

24:48

of exercises needed, any skincare mental wellness, or a lot of things are not there. So how I can

24:55

optimize my prompt that I'm giving to AI is or basically how reflection we can add is that you

25:03

try to specify AI what all things you need. Like for example, in this prompt only, I'll say

25:10

this that after writing check four plus actionable steps, whether it is beginner friendly or not,

25:16

time per step that we want. And what is the output format? Like if you remember in prompt also we

25:22

talked about, right? That like if I actually combine this thing with this thing, then this kind of

25:28

output we will get. So due to which the results will be very, very good.

25:33

Like only one thing we are doing is whatever prompt we have written, we will ask

25:39

AI to check some specific measures. So if you remember in the last class, we talked about a lot of

25:44

things. Let's try to actually reevaluate. Let's say that today I am writing a prompt, like any prompt

25:51

I can write. If you remember that these four things generally we try to create, that we ask

25:57

AI to create a specific role that is there. Then we will try to add task. We will try to add task. We will

26:03

try to add different, different instruction. Then we will try to do other things. Like if you

26:10

remember, we talked about output format and we talked about different, different constraints that are

26:16

there. Okay. Now, this part is writing prompt that what you have done is you have written everything

26:24

that is related to the prompting part. Once you have done that, right, what is the next thing that you

26:30

will try to do. The next thing that you will try to do is, guys, what will be the next

26:37

thing that you will be doing? The next thing will be that you will try to actually evaluate like what

26:44

we will try to do is we will try to add some checks that before giving the entire result, you try to

26:51

evaluate all the different checks that we have added. Like it could be anything, checks related to

26:56

output format or checks related to whatever.

27:00

you want. It could be any real scenario that if let's say this kind of problem is given,

27:07

how do we check that? So everything related to this particular part will be present up. So the main idea

27:13

that you need to understand it and the main thing that you need to understand that once we have

27:17

written a prompt, what will happen is that AI will generate some output. Let's say that this is a result

27:24

that is generated by AI. Now what we are asking is that AI only should check.

27:30

whether this result is meeting all the criteria or not. And if it is meeting, then only

27:37

it will generate a final output. So this output will definitely be better, right? Correct. Is this

27:43

part everyone able to understand that first I will evaluate the put like whatever prompt we have

27:49

given. It will give some you can say intermediate output or we can say even you can say that this is

27:56

output number one. If this meets all the checks and based on all the checks,

28:00

it will give the next output, which is output to correct. Is this part clear?

28:10

Guys, this part everyone is able to understand.

28:18

Aditya, we can see this, right? We are discussing here that based on whatever prompt we have written,

28:23

I think everyone has the understanding of what kind of prompts we can write down, right?

28:27

Like for example, I can write good prompts using that.

28:30

prompt some output we will get. Now in that prompt only we will mix and we will add some

28:36

checks. Using those checks, what will happen is that AI will evaluate the output based on checks

28:42

and will improve that output. And then we'll try to give the final output that is there. Is this part clear?

28:50

Guys, still here, this part everyone is able to understand or not?

28:55

correct? So we can see the same example I'm showing here as well that you can see that

29:00

rather than writing this prompt only which is written here, I am saying that after writing

29:07

check all these conditions. Adding these checks will improve my output for sure. I think this part is good

29:13

to go, right? Should we go ahead to the next part?

29:30

all the reflection part that is there. This check is separate, right? This has nothing to do

29:37

with CFO and SICO. That CFO and SICO we are already checking while writing the prompt.

29:43

So I think, Raju, this part is clear, right? That if you see, yeah, it's nothing but an

29:48

advanced version of constraints only. You can see this, that here we specify everything.

29:53

But a real life scenario can have multiple checks which you cannot write directly in the constraints.

30:00

So here in this particular part you will check for CFO and CCO.

30:04

You will check for both these mechanisms that are they followed or not.

30:08

Correct, right. Once they are followed, you have written a prompt. You add some checks as well so that

30:14

that thing can be optimized. Is this part clear?

30:18

This part are you able to understand?

30:25

Yes, right.

30:30

Harsall, we will talk about that. What are self-improving prompts? We will talk about that.

30:34

I think currently till here, this part is clear, right? Is everyone able to understand a reflection part?

30:41

That what is reflection? We will try to add different, different checks after writing a prompt.

30:46

So that AI generates a intermediate output, then checks that, and then again writes the output in a different

30:53

way after following all the checks that are there, correct?

31:00

No, right, that is step-by-step thinking, Suraj.

31:02

I think everyone is able to understand, right, that in COT, step-by-step thinking happens.

31:08

That generates the first output.

31:25

Final output will only be one. This output, this output we will not be able to see.

31:30

is temporary and we will not be able to see.

31:32

We will see this final output, which will be better than output number one.

31:36

Is that part also clear?

31:40

Guys, still here, this part is clear?

31:54

Let's try to go to the next part is clear. I think we can, Gotham, you caught it, right? Only one out. I think we can, Gotham, you

31:58

got it, right? Only one output will be coming. The check will be written at the prompt only.

32:05

So if you remember, Madhushri, right? We can see this that you don't, I think you understood,

32:11

right, that in the prompt, you add checks also. So that earlier, if let's say today we don't add

32:17

checks, then what will happen? We will get only output one. Getting my point, right? We will get only

32:24

output one that is there. But let's say if I add checks, I'll get a better output.

32:28

Like here in this case, you will get this output if you just write this.

32:33

But if you write a combination of this, then you will get better output, right?

32:36

Because it will check also a lot of things.

32:39

So we can clearly see this that output two will be way, way better than output one.

32:43

Is that part clear?

32:58

Let's try to go to the next part that is there. That what are the three different stages and what will happen? I think we can go to the next part.

33:13

It will show only the final one that is there after the checks are performed. It will only show the final one. It will not show the final one. It will not show you the intermediate thing that is written. I think Muscan, that also is cleared up right? I think this reflection part is cleared. I think this reflection part is cleared.

33:28

that what we talked about, that we are adding some checks in the prompt only so that output can be generated in a better way.

33:36

I think we are good to go with this particular part, right?

33:44

Let's try to go to the next thing. Let's try to understand what are self-correcting prompts and then we can go to the next part as well.

33:52

So we can see here that if we try to see, like, let's go.

33:58

and understand the structure and all. So you can see this that there is a three-step structure that we are

34:05

having in self-correction prompts. This is another concept that we are talking about. That prompts

34:10

will automatically try to correct themselves. So let's see how it happens. So first thing is that once we

34:17

are writing a prompt, it produces a initial response. Then what will happen is there will be some

34:24

review that will go on that will understand that what is missing.

34:28

what is incorrect and this will be the turning point like the same concept is there

34:34

whatever we were discussing in the previous part if you remember the self-correctness prompt

34:40

only thing is that there will be some review going on based on that particular review a new version will be

34:47

generated now how this particular thing will happen let's talk about so one by one let's try to see this

34:54

all the three steps with the help of example like for example

34:58

If I write this kind of a prompt that is there, that you are having three stages.

35:03

Like, for example, in stage one I'm saying, explain why sleep is important.

35:09

Stage 2 is

35:12

critique your answer, what is missing.

35:14

Stage 3 is rewrite and fixing the gaps that are there.

35:18

So let's try to understand this, that how everything will happen and what AI will try to do.

35:25

Let's try to discuss it one by one.

35:27

So we can see.

35:28

here, like if you, if we try to give this kind of prompt, let's say if I have given this

35:35

prompt that why sleep is important, then we will try to think that what things are missing

35:42

or even we can ask AI that what things are missing.

35:46

AI can help us rewrite those prompts that are there and using that if I try to give a better

35:53

prompt, I'll try to get a better result that is there.

35:57

Like for example, if we.

35:58

talk about this stage one that why sleep is important then this is very weak like a lot of

36:04

things are not practically given whatever things are missing we will try to add those things

36:11

and then we can see this that the response that will be generated with the help of AI it will be much

36:18

better let's try to see the other example because I think this example you can understand

36:23

only after these stages that are there so first let's talk about it and then we can

36:28

actually go and see what happens.

36:32

Now, like what totally we will try to do, let's try to understand that what's overall picture

36:39

here.

36:40

So first let's talk about this slide and then we can draw a diagram and we can understand.

36:45

So as you were seeing, right, that I am writing three stages.

36:48

Like for example, if I don't specify three stages, then AI will not understand that it is a self

36:55

correction prompt that is there.

36:58

or it's a self-optimizing prompt.

37:02

Now, how can we do this is we can do this in this particular way.

37:07

We will ask you to find out all the issues that are there, like a lot of things we will try to do.

37:13

Just give me one minute.

37:15

I think there is too much background noise.

37:28

Can you hear me? I think you can't hear any noise and all right. I think the voice is clear and all right. I think the voice is clear and sharp, right?

37:58

Let's try to see. I think probably let's go ahead and then see. One thing we want to talk about is.

38:10

I think this is not that much detail I have added. Let me see how we can discuss it in a better way.

38:17

We can see that if any particular prompt we need to write down, then what we will try to do, we will try to add three stages in those prompt only.

38:25

Like for example, this is the prompt.

38:28

normal prompt that you write, you write it. You ask AI that critique your answer that

38:34

what is missing or what thing is not working. And in that stage three only we will say,

38:41

fix all those gaps that are there. So what AI will do is whatever output AI has created,

38:48

AI will try to understand that what things are missing and if anything is like, let's say not

38:56

added properly, it will try to fill those gaps. So probably using diagram only, let's

39:01

try to discuss and understand what will happen. So what I'll do is that today, let's say if I want to

39:08

write a good prompt, like for example, I say that I want to write a prompt using three steps.

39:15

I'll say that my stage one is and I can write a prompt. Now, any prompt you want, you can write it.

39:23

Let's say my prompt is that plan a trip to Goa.

39:26

Now, I'll say stage two, like this will be my entire prompt.

39:31

Earlier I used to write only this much prompt, but this time I will be writing prompt in this kind of format.

39:38

Stage two will be that critique your answer, what is missing or not added.

39:44

Like anything that you want, you can write down.

39:46

Like for example, currently we are writing, critique your answer, what is missing.

39:51

And once that is done, we will go to stage three part.

39:54

in stage three part what particular thing will happen.

39:58

We can see this that we will try to rewrite the answer and we will try to fix all those gaps that are there.

40:04

So we will try to do that.

40:05

We will say that rewrite the answer and fix all the gaps that are present up.

40:12

Now, this kind of way will actually determine what and this kind of way will actually make what.

40:19

It will make a prompt self-correcting.

40:23

So any prompt which is written in this particular format is called as a self-correcting prompt.

40:30

Why?

40:31

Because in this process, what happens?

40:33

I'll tell you the entire process one by one.

40:36

So we can see here that what AI will do is it will start with the first prompt.

40:41

It will generate some output.

40:43

This output is not shown to the user.

40:45

So we can see this that it generates some output, which is I am clearly writing here not shown.

40:53

to user. User means us. Then what it will try to do is it will try to understand all the mistakes.

41:00

So this is another output that it will generate and using which what it will try to do is it will try to

41:07

identify all the mistakes that are there. Like it generates second output and in this output what

41:13

particular thing is happening it understands the mistakes.

41:21

Now once this particular part

41:23

is done then what it will try to do is once this entire part is done then we can see this

41:29

that it will try to combine everything and it will try to rewrite the answer so we can see

41:35

using this entire part rewrite step will happen so we can see here that we can go to the next

41:42

part and we can see final output will be generated which will be visible to the user as well

41:47

so we can see this will be our final output which will be

41:53

visible to user as well. Is this thing clear? This diagram is everyone able to understand

42:01

first of all. I think we can attach these diagrams also in the slide so that it's very easy because I

42:08

think that slide is a little bit complicated to understand. So I'll just update that slide after the

42:14

class but yeah, currently this part are you able to understand? I'll just take a screenshot of this

42:20

diagram also and I'll show and add it.

42:23

Yes, right, Aditya, you have to watch the recordings of previous classes that are there to understand this.

42:32

So probably I'll just attach this diagram so that we can understand this example.

42:41

Previous diagram also I'll attach so that everyone can see that.

42:46

I think the diagram is visible, right? In the PPD also I've added and I'll write the heading the heading and all.

42:53

Now this step is clear, right? So what AI will do is that we will be writing this prompt.

42:59

AI will automatically understand what things are missing and this will be the final output that it will generate.

43:05

So for example, first it will generate some output which will not be visible to user.

43:11

It understands the mistake and using that mistake part, it will combine both the things.

43:16

Like it will combine whatever output user has shown, it will combine this particular part,

43:22

this part as well as this part that is there and then it will generate the final output.

43:28

I think this part we are good to go.

43:31

This part everyone is able to understand.

43:50

Guys, still here, this part is here, this part is later,

43:52

Here.

44:05

Stage 3 is rewriting the prompt right?

44:09

After combining them, final output will be generated.

44:12

So you can see this, that in stage 3, the final output is getting redwritten and better thing is getting added.

44:19

Is this part clear?

44:21

So as a user,

44:22

we will do is that whatever prompt we are writing, we will try to write that prompt

44:27

in this way, that first we will write the prompt, we will tell the step 2, and then we will tell

44:34

AI that rewrite also by understanding what thing is missing.

44:38

So using this particular part, we will try to solve it.

44:41

Gotham is this part clear?

44:46

I'll go to the slides once again so that we can understand it.

44:50

So you can see this that there are 3.

44:52

things. The first thing is, I'll write in chat also so that everyone can see.

44:57

The first thing is generating output 1. That is generated with the help of basic prompt

45:03

right. Then we are trying to critique the answer. That is done with the help of second step.

45:10

The third thing is that we are writing and that is done with the help of step 3. Correct?

45:22

Yeah, I think chat is not visible to everyone. Let me write it again. So you can see this right. Step 1 is generating the output.

45:34

Step 2 is critique. Critic means that AI will review the answer. AI will review what it has written. Correct? Is that part clear?

45:49

Correct. Right. Once this thing is done.

45:52

Then it will try to rewrite the same output. So these three steps will happen.

45:57

I think all these stages is everyone able to understand. So you can see this that first step is

46:03

producing the initial response, which we talked about is stage 1. The second is stage 2 in which

46:11

critique is happening, which is the main turning point. And then there is step stage 3 in which

46:17

improved version we are trying to have.

46:20

So we can see this that.

46:22

three stages they are explicit and they are not like they are not overlapping. First

46:29

it will generate a response as we can see in the diagram. Then it will try to critique

46:34

whatever is missing. It will understand the mistake and then it will try to combine the

46:40

output and the mistakes and then it will generate the final answer. I think this thing

46:45

is also clear. This part is everyone able to understand or not understanding

46:52

Same thing is happening in this diagram also, which we already discussed.

47:00

Let's see a example also. We can open chat, GPD and we can try that. So earlier we used to write a

47:07

prompt, which is what was a structure of the prompt? That plan a Goa trip, right? So we

47:16

can say that plan a Goa trip for three days. Okay.

47:22

Now, rather than this, I'll say that what is stage two, review what is missing.

47:33

Okay? And something like what is missing. Let's say as of now only this thing. We can optimize this

47:39

also. And what will be stage three, that rewrite the final response.

47:48

So rather than writing only one single line prompt, we are asked to,

47:52

it to do all the three steps. Let it do. It will take some time to actually do it.

47:58

But ideally we should have written rewrite the answer fixing those gaps. Let's write that only.

48:05

I'll just copy this and I'll say rewrite the final response.

48:11

Fixing all the gaps. Okay. So this thing I'm writing. I think this example is clear,

48:18

right? Is everyone able to understand? You guys can also try. I have pasted that in

48:22

the chat. You just have to see the final output three that is there. This output we need to see.

48:32

Is the diagram clear to everyone? Anyone having any doubts in the diagram part? I think diagram

48:38

you are able to understand, right? So we can add a text walks also. This is the diagram for

48:45

self-correcting prompts.

48:52

I think this diagram is clear right to everyone. Same way we can add a diagram for this as well. I'll just add a diagram for this also. The diagram that we were drawing.

49:22

So we can see this is the diagram and in this diagram we can see.

49:33

I think the changes might not be getting saved but yeah, let me try to save them also.

49:52

So we can see prompts with reflection also. I've added the diagram and I'll just save it also. I think in one minute it will be saved.

50:01

Yeah, right? You can do any one of them. You can do any one of them which is there. So you can see the output that it has generated is much, much better, right?

50:11

If you try to just say plan a trip or go up for three days, it does not generate a good output.

50:18

But now you can see everything is so much detailed that what I should.

50:22

should do, what all things are there. It has even showed me what is an analysis that was there.

50:29

Like it is showing me what analysis it did and then it is generating the final plan.

50:34

So even this thing is also there. So now we can see every output. Like for example, this is the first

50:40

output it generated. This is the second thing, the gap analysis that it did. And then this is the

50:46

final output. So everything we can see here right. Correct. Generally the first output.

50:52

final thing that matters is this thing, the improved version. This is the final output that we are getting,

50:58

which is very, very good. Like everything, plan and everything is there. Correct?

51:19

Guys, is this thing clear? Is this example clear? That all.

51:22

So one more example we can discuss, right?

51:52

Guys, still here, first of all, this example is clear to everyone, right?

52:01

Same thing we can try with reflection also. With reflection, only thing is that we need to add different, different checks. Like, for example, I can add a check that I need to visit South Goa, I need to go to a lot of beaches, all these checks you can add. And same example, we can write down.

52:17

Like for example, if I say, plan a quarter for three days, correct?

52:21

Now, if I want to add reflection here, I'll say all the checks. That, for example, first check is that visit many beaches. We can specify different, different budget that you are having. Then probably visit South Goa for more days. All these things or more time. Anything that you can write down, you can add all the checks. So this is nothing but self-correction that will happen. I think this thing. I think this

52:51

thing is self-reflection part that will happen that it will try to check whether all these things are written

52:57

correctly or not. I think this part is also clear. So only checks part we need to specify here. Is that part good to go?

53:21

Shall we go ahead? Purachan, can you write in chat? What is the doubt you are having?

53:39

Rakeh, they can happen simultaneously. I think we discussed it.

53:42

LLM counts internal output. Internal output and input will be counted as token usage, right?

53:48

Nytesh, so that thing will happen.

53:51

No, right, Malay, that will not be considered. Because in one prompt only we need to enter the correction and everything. If we enter it in a separate prompt, then that is considered as the entire chart. So that thing won't come under this scenario.

54:12

I think this three stage process is clear to everyone, right? So you can see even chat GPD shows this. Like I think this thing I've added in the diagram.

54:21

Like some AI agent that we will be building, we will not try to show this particular part, but chat GPD will show you.

54:28

Like chat GPD shows this also, it shows this also, and then it shows the final output.

54:34

But the kind of AI agent that we will make, we will not probably, we will just try to show the final output that is there because user does not want to see what is the first output.

54:44

Like you understand this, right? That this stage one is meaningless for me.

54:49

Why I want to see this? I don't want to see this.

54:51

So probably if I write a prompt in a better way, right, that I only want to see the final output, then it will not give me stage 1 and 2.

54:59

Ideally, we should write that also in the output format that we only want stage 3 output.

55:04

So then only that part will be coming up.

55:09

I think this thing is clear, right? Should we go ahead to the next part?

55:15

So Malay, what you wrote in the chat, right? That is called as iterative prompting and one by one we can see that part also.

55:21

will happen. I think these two concepts are clear, right? Yes, Raju. By adding

55:28

constraint and output format, we can remove the intermediate step. That is absolutely correct.

55:35

Gotham, we will see later on how tokenization is working. Generally, Purjan, we will not try to write

55:44

anything negative. So where did we write anything negative? Like, we will write it in a positive way only, right?

55:51

Like here also, whatever I was writing, I think I was writing in positive sense only.

55:56

Like, what is missing? I think all these things in positive sense we are writing.

56:00

Right here also, you can see everything in positive sense we are writing.

56:04

Negative sense we are not writing.

56:07

Restiction though we will write, right, right, purjan. Like in constraints, we will say write it in 200 words.

56:13

That thing though we used to write and we have to write it.

56:16

Like sometimes, yeah, I will give a lot big responses.

56:19

is if I require only 200 or 300 words, then that part only we will try to write down, correct?

56:40

So I will be discussed it in the last class, so you can check out that part.

56:49

Urajan in one shot only we are giving all the three stages that are there, right?

56:56

I'm not writing it in multiple steps.

56:59

I am writing multiple steps in a single prompt only.

57:03

I think that thing is clear, right?

57:10

Whatever test cases, Harsall, we want.

57:13

Like, for example, whatever checks we want, right?

57:16

For that scenario to happen, that we will write.

57:18

So it won't become irrelevant.

57:19

event for LLM. That particular thing will not happen. I think all these steps we have

57:26

understood that, for example, we can write whenever we are writing anything that is

57:32

self-correcting right, we can write all the stages that are there so that AI understands that,

57:38

okay, this is a self-correcting prompt. The second thing is that we will tell it, check for

57:45

missing facts, check if everything is clear or beginner-friendly, what

57:49

by checks we want we can are

58:19

Hi, guys.

58:49

section has some issue at their end. He'll join in a moment. He'll rejoin.

58:55

He'll rejoin.

58:56

Tihil section has dropped out from the meeting. He'll rejoin.

59:19

Thank you.

59:49

Thank you.

1:0:19

Thank you.

1:0:49

Thank you.

1:1:19

Thank you.

1:1:49

Thank you.

1:2:19

Thank you

1:2:49

Thank you

1:3:19

Thank you

1:3:49

Thank you

1:4:19

Thank you

1:4:49

Thank you

1:5:19

Thank you

1:5:49

Thank you.

1:6:19

Actually, there is some issue at sections end, so we are trying him to re-log in, but let's see.

1:6:49

there is some rain outside in Bangalore I think I have no proof

1:7:19

Thank you.

1:7:49

Thank you.

1:8:19

Oh, is it? It's raining heavily in Bangal.

1:8:26

How long it is raining from?

1:8:29

How long it is raining from?

1:8:34

Oh my god, it's two hours.

1:8:38

Meanwhile, I'm sharing the link for the slides for today.

1:8:46

You guys can have a look on it.

1:8:48

All right?

1:8:52

Pahel, I'm not the right person to respond to your query.

1:9:18

on LMS, the curriculum team is more appropriate people to look on to you.

1:9:48

Yeah.

1:10:00

Hi guys.

1:10:01

Sorry, I think there is Wi-Fi issue on my end every time it is like restarting that's a main issue.

1:10:07

Can you hear me now?

1:10:08

Like I'm not sure.

1:10:10

Yes, you're audible and your screen is visible as well.

1:10:14

Yeah, let's see if it goes again, then we can see what we can do.

1:10:17

But I think.

1:10:18

these two things we were discussing about.

1:10:21

We were seeing about the reflection part that was there and then we were talking about this thing.

1:10:26

We were actually talking about the correction part.

1:10:29

I think these two diagrams were clear to everyone, right?

1:10:32

Whatever we talked about.

1:10:37

I think all the four steps were also clear that rather than writing a prompt,

1:10:42

what we will try to do is we will try to like, I think the diagrams, they are probably

1:10:47

they are probably not saved in the PPD. I'll add them after the class.

1:10:51

But on the screen we can see this that rather than writing the prompt normally, what we will do is we will write the prompt.

1:10:58

We will say this that whatever answer we are getting, like we will ask AI to think very closely

1:11:05

that what are the mistakes that are present and based on that it will try to generate another output that is there.

1:11:12

So let's try to see that part.

1:11:14

I think these two things are clear, right?

1:11:16

I think this diagram, okay, it's there already.

1:11:19

So yeah, I think this part is clear, right?

1:11:22

To everyone.

1:11:23

Guys, any doubts in last two concepts that you are having,

1:11:28

self-correction and self-reflection part?

1:11:37

Chinme, let's discuss it towards the end.

1:11:41

Do remember to just post this question towards the end,

1:11:44

and let's talk about that towards the end.

1:11:45

about that towards the end of the session.

1:11:47

Because I think that will take too much time of the discussion.

1:11:50

So let's do it towards the end of the class.

1:11:53

So we can see here this particular part, like let's try to see the next part that is there, which is iterative prompting.

1:12:00

Now what will happen is we can see here that rather than, like this is another technique to help us fix all the prompts that are there.

1:12:09

So one by one, let's talk about that.

1:12:12

We can see here that

1:12:14

that what we will try to do, we will try to ask AI.

1:12:18

Sometimes after writing a prompt, right, it's not 100% guaranteed that the results will be great.

1:12:25

So what we try to do is we try to ask good questions or good follow-up questions that are there

1:12:31

so that our result can be optimized.

1:12:33

Like for example, it's like directing a film only right,

1:12:37

that if you are trying to shoot some particular scene, in one way it does not come up.

1:12:41

So you will probably ask to change this particular part.

1:12:43

change this particular part, change that particular part, so that best output we can get.

1:12:49

Same way, it's not every time.

1:12:52

Like if we are building a complex AI agent, right, and we are writing a prompt for that.

1:12:57

In one go, things will not happen.

1:12:59

Like, for example, if you try to generate a business proposal, then in one go things will not be,

1:13:05

everything will not be correct.

1:13:07

Good iterative follow-ups are needed.

1:13:09

If I remember, like someone asked this question in the chart also, that if I am asking,

1:13:13

questions again and again with AI, that is like reflection or correction, that's not a case.

1:13:19

That is iterative prompting.

1:13:21

And I think everyone knows the meaning of iteration part, right?

1:13:25

Iteration part are you able to understand, guys, that multiple follow-up questions we try to ask,

1:13:30

that is called as iterative prompting.

1:13:33

And we can see this that a lot of scenarios, like if I'm generating architecture for any project.

1:13:40

Like, for example, I'll show you different, different projects that later on,

1:13:43

we will be building. If we are building architecture or implementation plan, which is

1:13:48

very, very big. Then in those cases, it's not 100% guaranteed that the result will always be correct.

1:13:55

So let's try to see that part. Let me share another screen and show you another example.

1:14:02

Let me know once that particular file is coming up or not.

1:14:10

Can you see my particular screen?

1:14:12

So I think you can see this kind of a screen, right?

1:14:16

So you can see here, like, a very big architecture is being generated.

1:14:21

So these kind of architectures cannot be generated in one go.

1:14:25

Like, there will be a lot of things that we have to fix.

1:14:28

A lot of things we need to specify.

1:14:30

In order to generate such complicated real-life application or a real-life project,

1:14:35

multiple prompts are needed.

1:14:37

So whenever I'm writing multiple prompts and saying something right,

1:14:41

this thing is called as,

1:14:42

iterative prompting. This example is clear, right? That generating such a big file,

1:14:46

it can have a lot of things wrong, right? A lot of things can be wrong. So rather, in order to

1:14:52

optimize it, what we will do, we will write different, different iterative prompts that are there.

1:14:57

Is that part clear? Is the example clear, first of all or not?

1:15:04

Guys, is the example clear?

1:15:12

Is everyone able to relate or not? I am just saying that whenever we are generating a complex architecture for any project, you don't have to understand the architecture here.

1:15:22

Did you get this meaning that if any particular thing we are having, any big complex thing we are having, in those kind of cases, we cannot do it in one single prompt.

1:15:34

Many different things we will try to have, right? Is that part clear or not clear?

1:15:42

Yeah, so let's try to go back to the slide part and see this.

1:15:47

Like, we can see here this thing that what are the things that are happening and one by one, let's try to see that part.

1:15:54

So what we will do is, we will send an initial prompt that is there.

1:15:59

We will get the first version response that is there.

1:16:02

Now that response might not be correct.

1:16:05

Then what it will try to do, we will try to review that what is missing, what is happening, what is happening,

1:16:11

what are the things then we will try to refine that like we will try to send proper follow-ups

1:16:17

that okay this thing is missing let's say from the architecture python is missing any other

1:16:23

language is missing any other thing that we feel is missing once that is done like let's say in

1:16:31

first go such a big file might not be correct like generally you will see once we are building a

1:16:36

agent we will be doing something called us phase-wise development what is phase-wise development what is phase

1:16:41

development that today if you are developing a complex project rather than making the project in

1:16:47

one go you try to divide the project into multiple different parts you try to divide a project into

1:16:53

five parts and then for each prompt you for each phase or in the five parts right in each part

1:17:01

you will try to have multiple iterations so that particular part can be fixed up is this part

1:17:07

everyone able to understand let's say that today

1:17:11

we are building a complicated project let's try to take another example and let's draw

1:17:16

it out we can see we are building a complicated project in one prompt we generated the entire

1:17:21

architecture now this architecture it has multiple phases let's say there is phase one which is

1:17:27

handling the data part then there is another phase which is let's say fixing the data part then

1:17:33

there is another phase which is in which we are writing something in python then there is some

1:17:38

phase which is building the website okay it's not hundred

1:17:41

percent compulsory that every part that is generated is absolutely correct one by one

1:17:47

what you will do is like this is you can say the part one of the project then what you will do

1:17:53

you will try to write sufficient prompts so that this part one can be fixed up then you will write

1:17:59

sufficient prompt so that part two can be fixed up this part are you able to understand

1:18:04

guys this particular part is clear or not clear same way we can see here this

1:18:13

particular part that part three and part four whatever parts we are having in a project we will

1:18:19

write iterative prompt so that each of the part can be later on fixed upon i think this part

1:18:24

is clear right so initially a big output will be generated that output has multiple parts each part

1:18:32

might not be correct or might not be completely correct so what we will try to do is we

1:18:37

will try to write prompts so that each individual part can be fixed up correct now we will try to write

1:18:44

different different like we will try to review the entire parts that are present up we will try to refine

1:18:50

this particular part and then we will repeat unless everything is done up

1:19:02

there can be any other scenario right prompting cycle means that

1:19:18

one by one you are giving different different prompts so that everything can be fixed up that's a

1:19:22

scenario is this scenario clear or not

1:19:32

after reviewing only we will understand right that if let's say anything is missing

1:19:37

we will judge AI and we know all the things right we have studied a lot of things how we can write

1:19:43

best prompt i am currently talking about that scenario in which your best prompt is also not giving

1:19:49

good result like for example some things are still missing because you are building extremely

1:19:55

complicated stuff with AI so in those cases you will write multiple different prompts for different

1:20:00

parts of a project so that this part can be fixed up this part can be fixed up

1:20:05

is this scenario clear context window we will talk about goreve in these kind of cases what happens and

1:20:10

all yeah right generally there is serality of parts that is their purajan so you will see this that

1:20:21

generally once our architecture is built right it has like phase one first you will try to implement

1:20:27

and you will try to understand phase one then you will

1:20:30

to phase two then you will go to phase three these things will happen this part is clear

1:20:38

or not clear guys this part are you able to understand should we go ahead to the

1:20:47

next part so we can see this that today if we are making a ATM for village students right

1:20:53

then probably if i try to make the entire project with AI in one go everything will not

1:20:58

be correct in one go

1:21:00

everything will not come up we will try to add multiple prompts like for example if we see

1:21:06

this kind of a scenario that even if we give up bigger like prompt which has almost everything

1:21:16

that is there then also it's possible that complete solution is not generated some edge cases are missed

1:21:24

some scenario is left up so multiple different prompts we will try to give so that the entire thing can be

1:21:30

I think this part is also clear right?

1:21:38

Guys, this part are you able to understand or not understanding?

1:21:46

Other people like what's a scenario?

1:22:00

correct right i think this part is clear so we can see this that generally this thing

1:22:09

we will try to follow that whatever thing is missing like for example if you have five issues that are

1:22:15

coming with AI one by one you will try to fix all the issues that are there you will try to tell it

1:22:22

in a specific way what is going correct and what is not going correct so that it is able to understand

1:22:29

the issues we will be completely specific that if anything is going wrong we will try

1:22:34

to specify exactly okay this phase is not working out this part of the project is not working

1:22:40

out this thing is not working it will automatically fix all these issues that are coming up

1:22:47

something related to context also we will try to study that how it will take the context and everything

1:22:53

like for example if you are building a AI agent with something called as cursor

1:22:59

you will see this that generally we will create a docks folder like if you see on the left

1:23:04

side right i have created here a docks folder in which architecture context everything i am storing

1:23:10

so whatever project we are trying to build right what we will do is we will try to store the

1:23:17

entire context in the docs file that is present so in this entire dox file whatever context and

1:23:25

whatever things related to the project we are having right we will try to

1:23:29

to keep so that if any issues comes up then all the context related to that particular

1:23:35

issue what is happening in the architecture is already stored up and AI understands that okay what

1:23:40

thing is working what thing is not working this is how context management can be done this part

1:23:46

are you able to understand later on we will see this that how to do the same thing in visual studio

1:23:51

code but i think idea everyone is able to get

1:23:53

guys are you able to understand or not yes right reju we can do that

1:24:07

let's go to the next part like we can see this that

1:24:19

generally we will give harsall this process we will use that we will use that first

1:24:23

first we will give one prompt in that particular one prompt we will understand what is happening

1:24:29

correct based on that what will happen is right like based on the result that it has generated

1:24:37

some things can still be incorrect then we will add iteration that's a scenario but every time

1:24:43

whatever prompt we are writing we will try to write it in the best possible way that thing we

1:24:49

will try to do i think this part is clear enough right

1:24:53

guys is this word clear let's try to talk about the next thing which is feedback loops and

1:25:07

let's see how we can convert a chat conversation into an autonomous agent let's try to discuss

1:25:14

that so you can see this that currently if you try to understand that currently if you're talking

1:25:23

with chart gpt correct then this thing will happen nearly by let's take that like just

1:25:30

ask this question towards the end and then we can discuss let's talk about everything and then you will

1:25:36

understand that how agents will behave currently we were talking about if we are talking with a chart

1:25:41

what kind of a scenario like for example in chart i can ask different different questions that are

1:25:49

there and iterations will work because you are the

1:25:53

loop like you are asking different different follow-ups you are asking different

1:25:59

different feedbacks you are asking a lot of things so that things can be improved in the

1:26:04

chart part but for a production agent this thing might not work because you are not there

1:26:10

let's say that you created a agent which is already running how you can improve it are you

1:26:16

getting my point in chat gpd you can improvise the prompt every time

1:26:22

you can specify the

1:26:23

that okay this thing is not working fix this this thing is not working fix this but in a production

1:26:28

agent you cannot do and there will be a lot of like that will be used by a lot of customers so you

1:26:35

cannot actually do that so what we do is whence we are building an AI agent we try to add something

1:26:42

called as a feedback loop this feedback loop every time the output AI is generating it will try

1:26:49

to check that okay this is the output that is coming and how we

1:26:53

we can actually optimize this particular output like what are the things that we can do so

1:26:58

that this output can be optimized in a better way this part are you able to understand

1:27:08

guys this thing are you able to understand or not

1:27:23

we will see the example rakesh i think the theoretical part is clear right now

1:27:37

let's understand what are the two types of feedback loop and then we can see the next part so we can

1:27:43

see first of all their first type of feedback loop is that user reads the output and it gives the direct

1:27:52

recommendation like for example let's say today if i've created a AI agent and i say summarize

1:27:57

this then it creates a vague summary after which the user says that this is very very vague

1:28:06

vague and like generate in three points so the agent is writing so you can see this that here who is

1:28:12

acting as a feedback loop can you tell due to whom feedback is working

1:28:17

user now what we will do is that let's say user has said three specific fact next time

1:28:28

we will feed in memory of the AI agent that if someone is asking summarize this right

1:28:33

then AI agent will remember that summarize in points it will automatically decide a number

1:28:39

let's say 5 10 or 15 based on whatever user feedbacks are coming right it will keep on storing them in the

1:28:46

memory

1:28:47

and using that it will try to generate every time summary in points that are there

1:28:53

this is how it will improve now let's say if there is no user input then how can we add feedback loop

1:29:01

we can tell the AI agent some criteria or something called as evaluations i think everyone

1:29:08

understands what is the meaning of evaluations right that evaluation will be that like

1:29:17

for example today if AI generates some output we can write something called as

1:29:22

evaluation.md file or we write a evaluation file as of now you can consider every time

1:29:29

AI generates some output right it will evaluate that particular result and it will generate a score

1:29:35

like for example it's like giving AI some marks it has some rules using that rules

1:29:42

AI will get some marks that okay if this output is generated let's say it got 90 marks

1:29:47

If this output is generated it got 99 marks.

1:29:51

This way with the time it will try to achieve an average of 95 or 99 whatever you set.

1:29:58

So based on all the rules that you have written in an evaluation file, every time things will be evaluated.

1:30:05

The output given by the AI will be evaluated and using that with the time it will try to achieve

1:30:12

achieve something called as a golden score or like whatever score that we have kept, it could be

1:30:17

95 or 99 it will automatically based on the rules part it will try to generate the

1:30:22

output so that it comes closer to that particular score this part is everyone able to understand

1:30:31

guys this part you are understanding that is not given in the ppt

1:30:34

AI will evaluate itself we will write some evaluations using which it will evaluate its

1:30:41

answer it will give some score that score we will try to improve later on is that idea clear

1:30:47

Idea are you able to understand implementation we don't have to worry about.

1:30:51

Abbe we have to think we will do this but I think the idea is clear, right?

1:31:17

If the score is too low, it will automatically rewrite and re-evaluate.

1:31:30

Next time the answer that it will generate, it will try to rewrite so that it achieves a good score.

1:31:37

Yes, right?

1:31:38

Long term, it will become stagnant only, like, because if an agent is running today with customers,

1:31:44

right?

1:31:45

you will see that it will try to keep on improving but after a point it will also stop right

1:31:50

because once it achieves the score of 99 then it will not stop so with the time what we do is

1:31:56

like after we see that okay this response has become stagnant then we try to update the evaluation file

1:32:02

with more rules and then it will try to achieve that so with the time what our job is to fix the evaluation

1:32:08

file or to fix the evaluation starter there so that thing comes under internal feedback loop starter there

1:32:15

like for example we are writing this kind of a prompt and we can see this that currently

1:32:22

let's say this is the attempt that we get so we will add some evaluation that if it is less than 30 yes

1:32:29

if it is something than this then other scenario so next time it will take care of that particular

1:32:36

assumption or the self-evaluation and using that it will try to understand and try to generate the answer in a

1:32:44

correct way is that part are you able to understand like for example if you see here

1:32:52

I am writing all the rules under 30 word yes or no includes results may vary recommends doctor

1:32:58

so you can see if anything is no it will rewrite and re-evaluate so first time it generates some

1:33:06

output then it will evaluate if everything is less than 30 words or not if it is varying or not

1:33:12

doctor recommendation is not again it will try to rewrite and it will check that if all the

1:33:18

rules are met or not so and you can see that currently we want to achieve 100% of the rules

1:33:24

that if anything is coming no it will rewrite and revaluate so this kind of prompt if i write right

1:33:30

it will keep on working in a self-loop kind of a structure it will keep on repeating its job

1:33:36

unless and until all the things are met or not this prompt will be written by

1:33:42

programmers evaluation file with the help of AI is written by programmers only.

1:33:49

Is this part clear? This part are you able to understand?

1:34:12

You guys still here this part is clear right?

1:34:42

now let's try to see what are the four parts and components of a feedback loop and one by one let's try to see this part

1:34:53

so you can see this that first we will try to generate a normal prompt we will try to add measurable

1:35:01

criteria these things we will try to write in a complex application we will be writing it with the help of

1:35:07

AI but currently if we are having a very small scenario then we can write it

1:35:12

ourselves also then we will ask AI to revise and revaluate that if any of the criteria is

1:35:19

failing then try to revise and revaluate everything and then it will try to deliver the final result that is

1:35:25

there so like for example today if i say write a professional email applying for a data scientist

1:35:32

internship or data analyst internship then applicant is someone who is the second year BCA

1:35:38

student with all these skills that are there evaluate based

1:35:42

on confident opening python excel example under 150 words if anything is not

1:35:50

met then rewrite and revaluate so you can see this is the entire prompt i'm writing i am saying that

1:35:56

task is this you need to write it based on an applicant this is the role you evaluate on these things

1:36:04

so these things are nothing but kind type of constraints only right that everything should be met

1:36:09

if anything is not working out then rewrite and re-evaluate so it will keep on going

1:36:17

through in a loop unless and until proper result it has generated so same thing we will try to see

1:36:23

like for example in first attempt it will write something like this so you can see the evaluation will

1:36:29

be that it is it confident no examples are not there less than 150 word yes and like does it clear no

1:36:39

does not clear so it will rewrite in this part you will see everything it has written

1:36:43

like for example there is a confident opening all the skills in example it has mentioned

1:36:50

everything as per whatever we have specified it has written that and it has generated this kind

1:36:56

of attempt and this attempt we will use and this will be the final scenario correct we can see this

1:37:03

like for example i can show you the exact same part in chart gbd as well let's try to take that

1:37:09

example also but this diagram is clear right that rather than writing a prompt i'm

1:37:15

saying uh like this is a task this is the evaluations that we need to write down and we can say here

1:37:22

this part that generate give me the final output don't give me all the attempts let's give it like

1:37:31

like let's see all the attempts but you know right that if i write an output format here give me the

1:37:39

final output it will only give you the final output currently we are not writing so it can

1:37:43

give us anything but if we want we can write that so let's see that example also uh

1:37:49

theoretically everything is clear in this part right feedback loop are you able to understand this example

1:37:55

also you can see right same example we will see on chart gpd so you can see everything it has come up

1:38:01

so it has evaluated also it has written a mail for data analyst internship it has checked

1:38:09

confident opening python less than 150 words since everything is good you can see no

1:38:16

rewrite is needed but let's say if anything was missing then automatically it will try to like again

1:38:23

write it guys is this part clear or not clear this part are you able to understand

1:38:39

yeah right i can paste the prompt with everyone as well you can check this

1:38:59

you guys can also try this particular prompt and then see i think i think i think i'm not able to chat with

1:39:09

just give me one minute i think yeah i don't have that permission can you make me co-host

1:39:15

or something like that koppel yeah yeah now i think you can do that now i can do that now i can do that

1:39:39

guys you guys can also try i think the theoretical part is clear right that what is

1:39:46

happening here so you can see like you guys can try and let's try to see this also

1:39:55

that if we are generating some summary or very small scenario right in this user will already

1:40:01

give evaluation so we don't have to give anything like we will just be writing the basic

1:40:09

parts that are there like creative like whenever we have very small task right in those cases

1:40:15

use where feedback loop works like for writing email also you can see right user can specify

1:40:21

everything that is there but generally if we are building a complex project in those cases we can

1:40:27

use a internal feedback tool we i was talking about that evaluation file right i'll see if i have

1:40:34

some complex project where i can show you how the evaluation file looks like an actual real

1:40:39

real AI agent if you just give me one minute i can probably see that also

1:40:49

yeah i can show you i've just opened a complex project that i built some time back so

1:40:57

if you see right that if we are building a very complex project then a lot of scenarios and a lot

1:41:04

of things we need to evaluate because a i is writing a real code right

1:41:09

which is very very big so in these kind of projects what happens is that a lot of

1:41:15

of edge cases a lot of things say i can do the mistakes and i don't want so you can see here

1:41:20

that i have opened here multiple phases now each of this phase is one component of a project

1:41:27

like it's a very big project that is why i've divided into like you can say currently the seven

1:41:33

parts each of the part has something called us evaluation dot md can you see that

1:41:39

this evaluation.md is checking that whatever code AI is writing right is it able to meet

1:41:46

all the criteria or not like everything that it is seeing it has added a evaluation file so

1:41:52

that everything can be checked up is this part clear so these kind of files we generate so that

1:41:58

AI does not do any mistake because if we are building a production level agent right then a lot

1:42:04

of things can go wrong so in order to understand

1:42:09

that there is no issue at all in order to achieve that 99% accuracy right we try to

1:42:15

have these evaluations file so that everything can be evaluated and AI does not make any

1:42:21

particular mistake that is there is this part clear now are you able to understand that in a

1:42:26

real project how evaluations will look like for different different phases

1:42:34

you don't have to understand the meaning of this code and all but i think normal

1:42:39

I think everyone is able to relate right what is happening.

1:43:09

this part is clear right we will be building these kind of projects later on this

1:43:20

is just an example to show you that how evaluations can be added or eval part can be added on a very

1:43:26

complex AI agent and this will become a feedback loop every time AI write some code it will try

1:43:32

to evaluate based on the evaluations and if evaluations look good then only it will proceed to the

1:43:39

next task so we can see in our AI agent for sure evaluations we will add but

1:43:47

sometimes user will also try to tell the direction because whatever we do everything it will slow

1:43:54

down a process a little bit for sure but you will see that all the edge cases will be covered once

1:44:00

these edge cases are covered right then a lot of issues that are present can be resolved so customer

1:44:08

experience is very very good and that's a high priority even though if anything still

1:44:14

AI is not working then user can guide it in that particular direction and whatever feedbacks user is giving

1:44:21

right then we will try to store them in the memory and every time we will try to use them so that

1:44:27

AI is able to improve that response so both the things together also we will use sometimes we will

1:44:32

store the user feedback and using that particular feedback we will try to keep on improving the

1:44:38

If not, we will try to keep that evaluation file so that every time the agent that we are building it is using the results from evaluation file and then running and generating the final output. I think both the things are clear right to everyone.

1:45:08

Should we go to the next part, understanding how the agent prompt will entirely work.

1:45:15

Till here, all the three concepts are clear, like we talked about till now, self-reflection, self-correction,

1:45:23

iterative prompting, feedback loops. All these four concepts are you able to understand.

1:45:30

In self-reflection, what is happening? We are trying to tell AI to give some checks that are there.

1:45:37

In self-correction, we are saying three stages. Do we remember all three stages?

1:45:43

Stage 1, stage 2 and stage 3. In stage 1, we will write a prompt. In stage 2, we will try to review it. In stage 3, we will say rewrite it.

1:45:53

Iter prompting means that even though we do everything, later on it can happen for a complex project, like if we are generating architecture or something, more prompts we need to write.

1:46:04

Because in one prompt, it cannot happen.

1:46:06

So more prompts we will write to improve the output.

1:46:10

Feedbacks we will add so that our AI agent is working in a more better way in production.

1:46:15

It is able to evaluate itself on a particular score and based on that, it will keep on improving to get that particular score that is there.

1:46:23

All these four concepts is everyone able to understand until now.

1:46:27

Then only we will go to the last two concepts that are there.

1:46:36

I think this part is clear, right?

1:47:06

Guys, till here we are good to go, right?

1:47:36

Let's try to go to the next part, which is complete agent flows.

1:47:47

Let's understand how everything will be working.

1:47:50

So we can see this that there are four components of a agentic prompt.

1:47:55

We can see this that we are having this scenario, that we are having a role that is there.

1:48:01

Like, you remember right, every time whenever we are writing a prompt.

1:48:06

We always try to give a particular role to AI that if you're writing coding, we can say you are a computer software engineer that is there who is writing a code.

1:48:15

These kind of roles we can give.

1:48:18

Now once I'm giving this kind of rules, automatically tone, behavior, all the default constraints, all the job description, everything is set up.

1:48:29

So this actually helps AI to set better context for the job.

1:48:33

Like for example, if it is writing code, it should be a software.

1:48:36

per engineer. If it is writing or teaching something, it should be a teacher. This way

1:48:41

things can be changed up. Then whatever task we are having, like for example, any task that we want

1:48:48

agent to do, then it will like, we will specify that do this particular task. We will try to add

1:48:56

reflection and criteria also. Like for example, all the checks and everything that we want AI to perform,

1:49:04

we will do that.

1:49:05

if it is generating some result and later on, if I want it to improve on that,

1:49:11

like you remember that, right, that we talked about that if it is less than 150 words or not,

1:49:16

and all those things. So we will try to check on that. Yes, no criteria. And then what it will do is

1:49:23

we will try to give output format. I think these things we have already talked about. So same

1:49:29

thing we are talking. Like if you remember this diagram that I was making, right?

1:49:35

In this diagram I was writing that we will write a prompt in this way, that you ask, like you add roll,

1:49:43

you add here role, task, instructions, output format, constraints and everything.

1:49:49

Now these things we have added up, correct?

1:49:52

Now we can see here this particular part with this multiple other things also we will try to attach.

1:49:58

Like in the prompt part, what we will do is we will say this that add different different checks.

1:50:05

So one by one, I'll write them. The first thing is that we will add checks. We will try to add

1:50:11

the exit criteria or the evaluation. And it will again, based on that evaluation, will probably

1:50:18

rewrite a lot of things that are there so that the result is finally good. These things we will try to

1:50:24

add. I think, yeah, checks, evaluation. It will try to rewrite based on the evaluations that are there.

1:50:31

There is something called as edge cases also. Like, for example,

1:50:35

well, we will try to think of any real world scenario in which our AI application can fail.

1:50:42

It can happen right, that AI application is failing.

1:50:45

So in order to handle those particular parts, we will try to add some edge cases also that are there.

1:50:50

So both the things we will combine together in the prompt so that the final result that we are getting is next to perfect.

1:50:59

Like it's a 90% chance or even 99% chance that the result that we are,

1:51:05

are getting is very, very good. So this way only we will try to optimize the prompts.

1:51:10

We will try to write the prompts in this way and using all the evaluations and the measures

1:51:15

and all the checks that we have kept, we will try to do that.

1:51:21

I think this thing is clear, right? This part are you able to understand?

1:51:35

Till here we are good to go, right?

1:51:54

Let's go and you can see this that each component is the main important component that is there.

1:52:05

If you miss any particular component, the results will not be great.

1:52:08

So the main idea is that every time whatever response we are generating, we will try to write it in the best possible way that is there.

1:52:18

Correct.

1:52:19

Later on, we can see this that, like, the main thing that we need to understand is that if I just give a vague prompt,

1:52:26

like for example, if I say explain machine learning simply, then only this kind of output will come up.

1:52:33

But you can see this that.

1:52:35

I can write the prompt in this way, that you are having a role of a teacher who explains

1:52:39

people of tech background or tech concepts, which have zero background of tech.

1:52:46

You don't use any jargons or like any analogy that is there.

1:52:50

You try to tell the task, then you try to evaluate or you add different, different reflections

1:52:57

or exit criteria. Like, for example, if this thing, this thing, this thing is not met, then

1:53:02

rewrite and reevaluate.

1:53:04

And you'll specify.

1:53:05

the output format. So these will be the final kind of prompts that we will be writing every time

1:53:09

so that the output generated is very, very good. Like if you just say explain machine learning simply,

1:53:15

then this kind of output will come up. But if I write this, then good output will come up. So let's try that

1:53:22

also. I'm not very sure my Gemini will work right now or not. But yeah, let's see. Probably we can

1:53:30

try this demo and then we can see. So I'll just say that.

1:53:35

explain machine learning simply. And here, I'll open a new chart window.

1:53:43

And what I'll do is I'll say that I'll give this kind of a prompt. So you can see this, that this

1:53:50

result will be way much better than this result. Let's see. You guys can also try with different

1:53:55

AI agents. I have copy-pasted the prompt as well. So you can see this that here it is

1:54:01

explaining machine learning and everything. But here the model is also very great.

1:54:05

But here we can see real-life examples and this thing is coming. This is very short.

1:54:11

Like this is a bigger example. I need to spend a lot of time and everything.

1:54:15

But here only three, four paragraphs are near and I can explain and understand what is machine learning all about.

1:54:21

So both the prompts you guys can also try after the class and then see.

1:54:26

The prompts are already there in the PPD. So you can even copy base from the PPD.

1:54:31

I'll share the link of the PPD. I think everyone has the folders and everything.

1:54:35

right guys this example is clear right that how do we write prompts using

1:54:44

everything we have seen like it's a combination of last three four classes that we have

1:54:49

seen same thing we are trying to do

1:55:05

I think this thing is clear, right?

1:55:24

Guys, should we go to the next part? This idea is clear, right?

1:55:31

So you can see this, that same kind of output will come up, like which I have to the next part, this idea is clear to everyone, right? That what will happen? So you can see this. That same kind of output will come up, like which I have.

1:55:35

written on chat GPD that this explanation that it is writing is very, very good.

1:55:42

It explains me with real world scenarios that what is machine learning. It is very easy for any

1:55:48

non-technical person to understand. It is only having three, four paragraphs. So I will not be

1:55:54

confused. It is having no jargons and all. And there is complete summary also that is provided.

1:56:00

So this is how a prompt can be written in a better way. This can

1:56:05

be understood only by a technical person or like a lot of things it has added. So even this is good.

1:56:12

Like currently the models are good. So even this result is also good. But I have to spend a lot of time

1:56:18

understanding and everything. I can quickly read this part and understand that, okay, what thing is

1:56:23

happening and what's the scenario?

1:56:30

Correct.

1:56:35

I think this thing is clear. So let's start with the next part. Let's go to the next part that is there.

1:56:46

Guys, still here, this part is clear, right?

1:57:05

Now let's try to see the next part. The next part is strategies, quality and optimization. Let's understand what will happen and how, like these things we will try to pick.

1:57:29

So you can see this that there are three strategies that I have written.

1:57:35

For example, you can write a one short prompt if you remember, basic prompt that we were writing.

1:57:40

It will just give us simple results. Like whenever we want, we are working in a company.

1:57:46

And whenever we see this particular part that if we feel this, that, like, we need to write anything very simple or we need to ask a very simple part, then simple prompts also we can write.

1:57:59

But if we see that we are working on a very, very complex application.

1:58:05

then in those cases, iterative prompts are required.

1:58:08

Like the real life projects that I was showing you, right?

1:58:11

They're very complicated part.

1:58:13

So in order to like build those,

1:58:18

in order to like get all these things, right?

1:58:21

We will use iterative prompting that is there.

1:58:24

Those things we will try to see.

1:58:26

The next part is the reflection based.

1:58:29

Like whenever we see that we are building a AI agent,

1:58:33

which is getting deployed in product.

1:58:35

then and it's an autonomous agent. Autonomous agent means that it is handling everything on its own.

1:58:42

There is no human approval or human thing that is needed.

1:58:46

In those cases, what we try to use is we use something which is reflection based.

1:58:51

We will try to add all the evaluations in AI so that with time it is able to improve.

1:58:58

We will try to store all the human feedback also so that using that particular feedback part

1:59:04

it understands what needs to be done and how things are happening.

1:59:08

This part we will try to see.

1:59:10

Is this thing clear?

1:59:15

Guys, this part is everyone able to understand?

1:59:23

Correct, right?

1:59:24

So we can see this that, let's say,

1:59:29

if we like now, this is the strategy part that we discussed,

1:59:33

that once you go inside a company, how you will use AI, these three things you will try to

1:59:39

remember that very simple task, directly write a prompt. Don't think much. If you are building

1:59:45

a complex architecture, then try to write iterative prompt. If you are building a entire AI

1:59:51

agent, which is very, very complicated, then try to add different, different evaluations and these

1:59:56

things that are there. Those things we will try to see. Correct?

2:0:03

Now what thing we can see is, let's try to see the next part that is there.

2:0:13

What is safety part? How we can check for different, different safety scenarios. These are basic

2:0:20

safety scenarios I've added as of now. But later on, once you see we start coding AI agent, we will

2:0:27

talk about that. Realistically, how can we make our AI agent more safe and safe.

2:0:32

So we can see, we can see.

2:0:33

first of all, like, if I ask AI that tell me about online safety right, then if I write this

2:0:45

kind of a prompt, then the result will not be that great. It will be like very basic result it will

2:0:50

try to give me. But let's say if I say you are a school teacher and you need to explain three safety

2:0:58

rules to like eight class people in these kind of languages, then this is a better prompt.

2:1:03

like this is a better scenario. Same way or this is a better prompt that we can write so that

2:1:09

AI understands that what is happening. We can give different different examples. I think this also

2:1:14

we talked about that how different examples and everything can be written. Then reflection part we

2:1:21

can add that try to check all the scenarios and try to add the output format. So using all these

2:1:28

three things we will be able to like get better results that are there.

2:1:33

This is better results in terms of safety. Like if I am checking for normal safety scenario,

2:1:39

then how can we get better results? Once we are building AI agent, then we will talk about

2:1:45

what is authorization, authentication, how we will prevent any particular like hacker to probably

2:1:53

breach in in our AI agent. Those things we will talk about later on that how it can be done.

2:1:59

This is just a minor example on writing prompts, but correct.

2:2:03

we are not discussing the safety of AI agent. We are discussing that how basic things

2:2:08

related to safety part also we can add up because sometimes AI agent it gives bad responses related

2:2:15

to the safety part. So if we try to specify the role and audience, we try to specify the examples.

2:2:22

We try to like add reflection, reflection means nothing but the checks that are there.

2:2:29

Those things if I add format if I tell up, then automatically go.

2:2:33

results it will try to add. So one by one we can see, like let's say sometimes this thing

2:2:42

AI does that it can tell you a confident lie that Python was invented by something else. So

2:2:49

it can misplace that, right? So these things it can do. Like for example, verification is not

2:2:56

there. It can give sometimes half answers also. So all these things can be actually optimized.

2:3:03

We are discussing how safe are AI responses that are there.

2:3:09

And what can we write in prompts? What to understand the safety thing? Is that meaning clear?

2:3:20

Rakesh, I think this meaning is clear, right? I was talking about authentication authorization and other things.

2:3:26

They are part of safety of AI agents that we are building.

2:3:31

Or the product that we are building.

2:3:33

But here we are talking about that if we write a prompt, then how safe is that prompt or the responses?

2:3:40

they are incorrect also, right? How we will know whether the response is correct or not?

2:3:45

Because today you can see that AI can give this kind of result, right? That who invented Python? It can

2:3:51

give a wrong answer. How we will know that the answer is correct or not? This part, are you able to

2:3:59

understand?

2:3:59

Yes, right? Like safety as in like how much responses are actually safe? Because we might be printing that response to user also. So if it is not accurate, right, then the data is incorrect and incorrect data ideally no product should show. So that's a scenario.

2:4:28

So you can see this.

2:4:29

that all these things can be fixed up. If I write better prompt, like for example,

2:4:34

if I add reflection, output format, scenario, role and audience, then all these things will not happen.

2:4:41

Like you will see that hallucination will not happen, non-answer it will not give,

2:4:46

incomplete answers it will not give, wrong format it will not tell, anything logical that it is

2:4:52

saying, those things it will not do. And we can say this that evaluation automatically will chill for

2:4:59

like based on whatever evaluation that we have added, right?

2:5:04

It will check whether exactly this is very like exactly this is the scenario or not.

2:5:11

Whether the answer that AI has generated is valid or not, whether it is deep enough or it is having the proper layout.

2:5:19

So this Eval thing we can use, the same Eval file that I showed you present in cursor as well, right?

2:5:26

This Eval file.

2:5:27

This Eval file also checks.

2:5:29

the same thing in an AI agent that if everything is properly validated, like for example,

2:5:35

here you can see it is checking a hard card and at the other things. It is checking for almost

2:5:40

every scenario that humans can think of. So in evaluations, by adding evaluations, this kind

2:5:48

of thing we can have that the entire exactness, the validity, educacy, layout, everything can be

2:5:56

strongly checked up. I think this part is also clear, right?

2:5:59

Right?

2:6:15

Guys, still here this part is good enough.

2:6:29

how we can optimize different and different feedbacks loop.

2:6:32

Like we have already talked about feedback loop.

2:6:34

I think this slide, I can move it before, because ideally it should be present here, right?

2:6:40

After the feedback loop part we discussed.

2:6:44

I think it is incorrectly present here.

2:6:46

I'll just fix it after the class.

2:6:48

But I guess you understand like what we did.

2:6:52

We can see this that generally any particular prompt that we are writing.

2:6:57

We can see here this.

2:6:59

part that we can reuse a particular template that is there.

2:7:03

We can tell whatever task AI wants us to tell, we can tell that.

2:7:08

Whatever thing is not working, like whatever exit criteria we are having, we can add that.

2:7:14

Loop also, we can add that if let's say any of these criteria is not met, then revise and revaluate.

2:7:21

Then we can add maximum cycles also like till how many times you want that loop to run because let's say that first time

2:7:29

is not meeting. Second time if it is not meeting. So that thing we can specify

2:7:35

in the cycles part. And we can even say that after three cycles also, if it is not able to meet the

2:7:42

results, then it can explain us why it is not meeting. And then we can specify the final output format.

2:7:48

So this will be the final structure in which we will be writing all the prompts. We will start with

2:7:54

rule. Like this is nothing but already we have talked about. What are the different different

2:7:59

and everything. We will specify the task. We will specify all the criteria, all the loops that we are having. Output format, constraints. We will add.

2:8:10

Using this kind of template, you can write any particular prompt that is there.

2:8:15

So probably whatever we have discussed in last, so many classes, right? The entire template only I have built from today.

2:8:24

Whatever prompts you are writing, try to write it in this particular format.

2:8:29

And you will see automatically the results will be better. Like for example, today if you need to plan a Goa trip, then we can say to AI, like we can give, I can open a new chart here.

2:8:43

And you can see this that you can say that you are a best trip planet in India. And what is a task? And you can specify all the details. Like for example, I can say here this particular

2:8:59

part that what will be that us that plan goa trip now you can specify all the measures like for

2:9:09

example budget beaches hotels north or south goa anything that you want you can tell whatever

2:9:16

loops you want you can tell that and output also whatever you want you can tell that in that particular

2:9:23

format so use this kind of a template and you can even remove whatever i have written here

2:9:29

like for example you can remove here role task and everything you can just specify

2:9:35

the things like this first line is nothing but the role part the second line is nothing

2:9:40

but the task part the third line is nothing but the reflection part you're going to add here

2:9:45

loop as well like you can specify the scenario and this is output format that you can tell so this

2:9:51

kind of template you can use and from today you will be using these templates only in order to

2:9:57

write different kind of prompts that are there correct right same thing will

2:10:04

happen justin that reflections plus loop is kind of instructions only but it will help us

2:10:11

evaluate better so whatever step-by-step instruction you want you can write it in this way that

2:10:16

is just a improvisation on that correct automatically you will see that this particular part will

2:10:24

evaluate i can keep evaluations in single

2:10:27

file also i can keep them in multiple files as well like if you remember the example that

2:10:32

i was showing we were keeping it in different different files that are there

2:10:57

Evaluation files are interconnected right like they will be used in reflection

2:11:04

only for reflecting whether every criteria has been met or not

2:11:08

so Richoo they are interconnected only right

2:11:27

this part are you able to understand?

2:11:35

guys still here

2:11:38

Nilema what examples on which scenario

2:11:43

like here we can see this that this is a template i'm showing right

2:11:47

like let's say today you need to write a prompt for building a AI agent so what do you think

2:11:53

what will be the role and everything we can see that example also

2:11:57

like for example if i need to write a complete AI agent that is there then we can specify

2:12:03

that you are a

2:12:05

AI engineer that is there who is having very good expertise in writing

2:12:09

AI agents that thing we can specify same way the next thing will be

2:12:16

that whatever task you want like for example i want to do this kind of a task that you need to

2:12:27

you need to make complete AI agent based on whatever requirement is there do you remember

2:12:32

i gave you five six projects last time so you can specify that you are an

2:12:36

AI agent who is building a resume application or let's say you apply on behalf of me for this particular

2:12:44

part so you can say that in reflection whatever criteria you need those criteria only you need to

2:12:50

add right like for example you need to apply let's say 10 jobs in a day 10 different jobs for

2:12:56

or sd2 role data analyst role data engineer role whatever role you want you can tell that so you

2:13:02

can mention all these things in the criteria part in loop part if anything is waiting no you

2:13:07

it will automatically revise and revaluate you can keep maximum cycles generally a lot of people

2:13:14

keep two and three only so same thing we can keep and whatever output format you want like for example

2:13:20

you want format something like this that this is a job application link and did you apply

2:13:26

or not so in apply part it will write here the link that is there and in the apply part

2:13:32

it will answer me in yes or no format whether it has applied or not is this thing clear

2:13:41

guys this part is everyone able to understand

2:13:56

link and apply you remember right last time we discussed it that what does link and apply

2:14:03

actually mean so we talked about right that let's say there is a job link that is there so that link

2:14:09

will automatically come up whether a i agent has applied to that job yes or no it will give

2:14:15

the output so this is the output format we are talking about correct

2:14:18

it guys is this thing clear like i know a lit today session was a little bit

2:14:26

hectic and the Wi-Fi was actually creating a lot of disturbance but were you able to

2:14:32

understand what we discussed the theoretical part is clear or not clear

2:14:35

yeah later on later on as we go into the course multiple different things we will try to see

2:14:48

so those things we will actually talk about that what will happen like once we go into the

2:14:56

practical applications part right i think probably from the next class prompt engineering should

2:15:01

be done and we will go to later on scenario yes right nilema you can come back everyone should try

2:15:09

right do you remember like in the last class i gave you this thing let's open and let's talk about

2:15:16

that also did you do this exercise i told you do this particular exercise right

2:15:25

so today i'm telling you that use this particular template that i'm sharing and try to

2:15:31

write the same prompt or probably uh build a ii agent or just try to prompt that is there

2:15:38

agent part we can see in the next class but yeah just try to write the prompt and everything

2:15:46

Go on, Suraj, what is a doubt you are having? Can you write and chat?

2:16:16

till here we are good to go right yes right we will be learning on how to build a

2:16:29

AI agent and all that part we will see you will see in the next class we will actually

2:16:34

talked about the memory in the AI agent like if you remember in today's class we were talking

2:16:40

here right that how feedback loop and everything we will be storing so in the next class we will talk

2:16:45

about memory and AI agent then we will talk about long-term and short-term memory then after

2:16:53

that we will talk about SQL and then we will start with actually how the data stood once we have

2:17:00

done that then we will start building the projects so probably in this module only you will see but

2:17:07

after like how many classes yeah currently also three three three

2:17:15

theory classes are there on memory part once they are done then we will start with the agent part that is there

2:17:45

we discussed are you able to understand that other people like what's the scenario are you

2:17:50

feeling the glass is tough or what's the scenario i think today there was too much rain

2:17:57

going on here and so that is why like wi-fi was key it kept on restarting right and even though

2:18:04

it had a power backup but if the main plug only goes right it restarts every time

2:18:11

yeah so with the time only you will be able to remember like every time

2:18:15

though you will forget a lot of things that are there but with time only you will be able to

2:18:20

remember so probably after the class next day if you are having you can read the notes that are

2:18:26

there let me push the notes for today's class also that particular thing we can go

2:18:34

yeah shay andy but the course flow structure i cannot change i also know that too much theory is

2:18:40

going on i'll also talk to the professors and all if we can change the syllable

2:18:45

us a little bit but to be honest it's a little tough but yeah i can try that let me try

2:18:52

if we can do that or not but that permission and everything needs to be taken so yeah i'll try that

2:18:59

if we can do that so that some practical things we can see and then we can see the next part that is

2:19:05

there so yeah let's see how we can actually do that probably from the next class some basic basic

2:19:12

demos on AI agent we can see and that

2:19:15

we can try i also feel that too much theory we are discussing so i'll just talk with

2:19:22

that team and let you know by tomorrow's class like in the next class that if we can actually

2:19:28

see a lot of more examples that are there i'm adding the notes of like 11th session also so

2:19:39

let me do that

2:19:45

yeah if you check here this particular part i think the folder should

2:20:04

be updated you can see here the ppt links are same only if you open this drive link you can see all

2:20:11

the ppts that are there and if you go to here this ppts that are there and if you go to here this particular

2:20:15

part all the lecture things that we have seen right everything also have written here so you can

2:20:22

check everything that is there that how like this is just for revision purpose so you can read this

2:20:28

article and then revise you can check out all the other articles also at this particular page so

2:20:33

you can go here and check that particular part any other doubt anyone is having i think here this

2:20:45

part is clear right i think i think till here we are good to go guys any other thing anyone is having

2:21:15

there but yeah i'll try to see if more examples we can add like probably demos we can do

2:21:22

and theory part we can do later on some little bit of course formatting part if we can do i'll speak

2:21:28

up with the professors and i'll try that in the chat i've pasted right

2:21:45

I should ping them in the google drive itself that part you are saying these articles

2:21:53

they are written in an MD file right and these are programs so you can see here this particular

2:21:59

part that they can be opened in GitHub only so you have only two links that you need to save

2:22:06

one is this particular link okay okay that part you are talking about yeah let me try that

2:22:15

also i think i can share you youtube links that works

2:22:18

youtube link can you watch binae yeah i'll add that in a google log only i can share you the

2:22:30

youtube links as well just give me one minute i'll share you a playlist only let me

2:22:41

know if you can see that particular playlist are you able to open this particular playlist

2:22:47

that i'm sharing can you write in chart if you are able to see you can open both the

2:22:58

videos directly right yeah right then though i think it's sorted then yes winners you can

2:23:06

directly open the playlist and see and other videos get and get up videos also i'll add

2:23:11

in the youtube playlist only so you can directly check out from another playlist i'll

2:23:15

create and i'll share you the playlist that is there

2:23:17

rakesh like this notes one time to you have to go through because first time you are studying right

2:23:31

so that is why going through will take around like i think revision since you have already

2:23:37

studied all the examples right so probably it will take

2:23:41

one hour only to revise through the notes that we are giving so one hour revision

2:23:45

so you have to spend right that thing so we need to do less than one hour is impossible

2:23:50

yeah no no no now i told you right the updated thing that is there this is there this is only

2:24:12

like prompt engineering is done now we will focus on memory part and once memory part is done then we will

2:24:18

start building agent the entire course will not focus on prompt engineering this was

2:24:23

the last class for the prompt engineering part that is there yeah so yeah like now to good

2:24:29

prompts also we will try to write down in the next classes and those things we will see

2:24:36

okay then i think this is it from today's class and let's meet in next class and discuss more examples

2:24:42

i'll also see if more demos we can add rather than the theory part that thing

2:24:48

we will try to do so yeah i'll just speak up with all the professors that are there in iatirutki

2:24:54

and we'll let you know so probably from the next class i'll just speak with them and change the course

2:25:02

curriculum a little bit so that more demos we can see right now and theory part we can do like later on

2:25:09

that particular thing we can do yeah i think that is it from my end let's meet in tomorrow's class

2:25:16

in the next class that we are having and we will try to see other things i think everyone

2:25:20

is having the get up link i'll share the get up link again and the people link yeah kubl i think

2:25:26

you can take over all right so it was an intense class today indeed

2:25:33

moving on to the next section let me share the feedback poll

2:25:46

We'll have a quick quiz to summarize what we have learned today.

2:26:16

Thank you.

2:26:46

Thank you.

2:27:16

So all right.

2:27:32

Let me share my screen my screen.

2:27:46

So either you can scan this QR code or you can go to www.minti.com and enter the code here.

2:27:54

I'll just paste this code in the chat as well.

2:28:16

Thank you.

2:28:46

So all right, let's start.

2:28:56

What is

2:28:59

What is?

2:29:13

What is self?

2:29:15

options are writing code, searching the web, reviewing and improving its own output or giving fast answers.

2:29:45

And the correct option is reviewing and improving its own output.

2:29:52

Let's see the leaderboard.

2:30:15

Why is self-reflection important and the options are?

2:30:20

Makes answers longer, improves answer quality, makes answers faster or reduces computation.

2:30:30

Yes, self-reflection

2:30:45

answer quality.

2:31:02

Get ready for the third question.

2:31:15

write, generate, critique or evaluate.

2:31:19

And the correct option is generate.

2:31:45

Moving on to the fourth question.

2:32:01

What happens in the critique stage and the options are final answer is given.

2:32:08

Errors are identified, prompt is changed or output is deleted.

2:32:15

And the correct option is critique stage involves in which errors are identified.

2:32:45

Get ready for the fifth question.

2:33:07

What is iterative prompting? And the options are one time prompting, one time prompting,

2:33:15

Rangam answers, multiple improvements step by step or skipping corrections.

2:33:20

And the correction

2:33:35

and the correct option is a iterative prompting refers to multiple improvements, step by step by step.

2:33:45

What is a feedback loop and the options are?

2:34:07

Evaluating and improving output, repeating errors, writing multiple prompts or ignoring

2:34:15

mistakes.

2:34:16

And the correct option is feedback loop refers to the process

2:34:43

process of evaluating and improving.

2:34:45

Let's look at the leaderboard now.

2:34:50

Let's look at the leaderboard now.

2:35:06

Which loop involves user input?

2:35:12

And the options are internal loop, auto loop, hidden loop or user feedback loop.

2:35:42

Let's look at the leaderboard just before the final question.

2:35:58

Get ready for the final question.

2:36:12

are creative tasks, emotional writing, storytelling or measurable criteria terms.

2:36:42

And the correct option is measurable criteria tasks.

2:36:51

Let's look at the final leaderboard.

2:36:57

Congratulations, Rohan.