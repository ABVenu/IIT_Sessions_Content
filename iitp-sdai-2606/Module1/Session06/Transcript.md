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

Thank you.

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

Thank you

9:48

Thank you

10:18

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

Thank you.

11:06

Thank you.

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

Thank you.

14:36

Thank you

15:06

Thank you

15:36

Thank you

15:38

Thank you

15:40

Thank you

15:42

Thank you

15:44

Thank you

15:46

Thank you

15:48

Thank you

15:50

Thank you

15:52

Thank you

15:54

Thank you.

16:24

Thank you.

16:54

Thank you.

17:24

Thank you.

17:54

Thank you.

18:24

Thank you.

18:54

Thank you.

19:24

Thank you.

19:54

Thank you

20:24

Thank you

20:54

Thank you

20:56

Thank you

20:58

Thank you

21:00

Thank you

21:02

Thank you

21:04

Thank you

21:06

Thank you

21:08

Thank you

21:10

Thank you

21:12

Thank you.

21:42

Thank you.

22:12

Thank you.

22:42

Thank you.

23:12

Thank you.

23:42

Thank you.

24:12

Thank you.

24:42

Thank you.

25:12

Okay.

25:19

Hello.

25:20

Hello, everyone. Good evening.

25:22

Hello, everyone. Good evening.

25:42

Hello, hello, good evening.

25:49

Hello.

25:50

How is everyone doing today?

25:54

Nice. Good to hear about it.

26:01

Cool. You guys are able to see my iPad screen.

26:11

Awesome. I'm also good. Thank you, Straits.

26:15

Okay. Cool. So welcome to today's session. Today we will be learning about nested loops, nested conditionals.

26:26

Then we will be, because now we are, you know, going a little bit more into, like we are going more, we are discussing more complex topics.

26:38

And it is the right time for us to, you know, discuss.

26:41

what happens when you use nested loops.

26:45

And why should complexity matter for a work?

26:49

So with that note, we will be also seeing Big O notation.

26:53

How do you represent complexity? How do you find out complexity?

26:57

And yeah, if time permits, we will actually create some mini project kind of thing.

27:04

Mini project as in which contains like a question which contains all of the things.

27:11

together as in four loops if conditions all of them together cool so does that make

27:18

sense to everyone okay so with that thought let's start and I'd like just like to take five

27:29

minutes to discuss what we discussed in the previous session so quick summary can seven

27:34

please tell me on the chat from what topic we discussed in the previous

27:41

session? Anyone would like to be discussed about dictionaries, okay?

27:57

And we also discussed about hash maps. Basically, dictionaries and hash maps are the same thing. Can I say that? Right? Okay. Okay.

28:10

Okay, absolutely. Then we discussed about how do you create dictionaries?

28:18

And we discussed about how do you basically, there are multiple ways to create a dictionary, right?

28:24

As in you can initialize and create the dictionary or you can just create the dictionary and initialize it later.

28:32

And there was a more approach. So we have seen things about dictionaries and how do you use dictionaries? Then we also saw some

28:40

functions on dictionaries, am I correct?

28:50

Okay, can someone please tell me what kind of functions did we actually saw in the dictionary?

29:10

items. So now if I ask you to iterate over a dictionary and print the key

29:21

value pairs, can you guys do that? Can you guys do that? Can we guys do that? Awesome. Cool. That's

29:31

nice. Okay. Now let's start with today's topic, which is nesting of conditionals.

29:40

okay okay uh when i say condition conditional statements what is the

30:10

When we discuss about conditional statements, what is the first thing that comes to our mind?

30:15

If else, absolutely correct. So till now, we have learned about that, okay, I can use if else.

30:21

If else.

30:40

let's say nesting. Nesting is basically one thing, one if condition inside the other.

30:55

That means there can be two, there can be two if conditions inside other. When I say, there can be two if conditions inside other. When I say,

31:09

what do I mean actually in Python? Whatever code is going to be executed inside the if

31:16

condition. So can I say that I can write the code in this way if customer? Customer has ticket. And I can have one more condition inside this. If

31:39

is VIP. Now, what is happening here? We are actually having two nested conditions here.

31:51

The outer nested condition checks for whether the customer has ticket or not. And the internal

31:58

nested condition only checks whether that ticket is VIP ticket or a normal ticket. Now, does it

32:08

make sense to check for VIP ticket at the first place, like without even checking whether the customer has ticket or not, I will ask customer. For example, you are trying to book a concert and you are in the queue, right? Now, if you have a ticket, the first person would ask you that, okay, if you have a ticket, remain in this queue. And once you pass that first check, then there is multiple sub entrances, that okay, VIP entrance is this.

32:38

normal entrance is this. And on the VIP and normal entrances, they check your ticket.

32:44

During that time, during the second check, do they ask you that, okay, do you have a ticket or not? No.

32:50

They just tell you that, okay, scan your ticket and go inside. Am I correct? So that internal check

32:58

basically happens only when the external, the outer check has passed. Can I say that?

33:05

Can I say that? That this condition, this code will only be triggered when the outer or the above a condition is successfully validated.

33:18

Everyone agrees with me?

33:27

Okay. So if I want to discuss on the syntax part, it is quite easy, but let's still discuss this.

33:35

If I want to discuss on the syntax part. So what would happen? I have to basically check whether a customer has a ticket. And if the customer has a ticket, I want to check whether the ticket type is VIP or not. So how I would do it? If has ticket.

34:05

Then I will check here if ticket type equals to equals to VIP.

34:22

If that is the reason, then I will print okay, granted access.

34:35

else I will just print normal access.

34:50

Now this internal if, these internal if, these are the internal if statements which are inside your outer if statements which are inside your outer if, can I say that?

35:04

Can I say that? The internal conditions are inside your if condition. And if the customer does not have a ticket, then you write here else. Print. No ticket. Does that make sense? So this is called nesting of conditionals. As of now, I have nested two conditions.

35:34

But if needed, can you nest more conditions, multiple conditions?

35:42

What do you guys think?

35:45

Everyone. Can you nest multiple conditions with like, if needed, definitely we can.

35:52

Right? Okay. So this is how nesting of conditional's work. Now, that does not mean just a one thing for everyone.

36:04

That does not mean that we should always, by default, try to nest the conditions. No, we should not try to force fit the things inside our code. Never.

36:16

If needed. Because the more you nest, the more complex code becomes. It becomes hard to read. It becomes hard to maintain.

36:25

Because the more you go inside like if, then if, then if, then you will have to think through all the conditions that, okay, first if, if, if, if.

36:34

second, if failed, what will happen? First two ifs, then the third if failed, what would happen?

36:39

So what I want to say is that always, always, it is a tip that always try to keep your conditions

36:47

unnested as unnested as possible. Does that make sense? I can take one example to understand actually

36:56

that part. Let's try to take one example and understand actually with example.

37:04

Okay?

37:05

Assume that I am writing a code here with some.

37:09

Okay, Priyansu, I'll just discuss a little bit in Hindi as well.

37:13

So assume we have to write a code for, you know, withdrawing some amount from the ATM machine.

37:23

A very simple function.

37:24

We have to just withdraw some amount from the machine.

37:29

So the first condition what I will check if card is valid.

37:34

Okay? If card is valid. Okay? If the card is valid, then what I will do? I will basically go inside and then what I will do?

38:03

Okay. If the balance is greater than input amount, then what I will do? If input amount, if input amount, if input amount, actually I can write this above, what I will do is, we'll move this here. If input amount.

38:33

is greater than zero, then I will check whether the balance is greater than the input account in the account.

38:45

Okay?

38:46

What?

38:47

here to us all come here.

38:49

Okay?

38:50

If this condition is, then I will allow my customer to withdraw the balance.

38:56

Is this all the problem what is here?

39:11

If you guys see, we have, we have these two conditions unnecessarily

39:16

different

39:17

are

39:18

ideally if you see,

39:21

ideally, normal,

39:23

Both the conditions have to be true if I need to get my money out from the ATM.

39:32

Can I say that?

39:33

Two conditions true are true.

39:35

Can I say that?

39:37

Does everyone agree?

39:39

So instead of I this nested code, can I write a simple code in a way?

39:44

Where I can it?

39:46

something, this can I?

40:16

Now this looks a little bit more easy to understand.

40:21

The second condition is if that will pass then and only then I will go inside.

40:28

Now someone can say that yes, in that case I can actually club all the three conditions as well.

40:34

What is stopping me to club all the three conditions then?

40:39

Here and here.

40:44

What do you guys think?

40:45

Any thoughts?

40:48

If I'm just, so I will need only one condition?

41:02

What do you guys think?

41:08

So the thing is, if there are multiple sub-conditions inside one condition, just say one condition is this.

41:15

Second is this and the third is this.

41:19

Then also it sometimes becomes a little bit difficult to understand.

41:22

So at the end of the day, the thought process is that we should keep our code as simple as,

41:30

like as simple as we can.

41:32

So that whenever we are trying to read the code, it becomes easy for us to understand.

41:39

If I want to make any change in the if condition later two months down the line, it should be easy enough

41:45

for me to understand the code and then I change can change.

41:49

Is this you all of them?

41:51

Everyone comfortable till now?

41:57

Okay, 100%.

42:00

So this is if condition.

42:02

Sir, do we have to also maintain the indentation?

42:05

If you are doing a nested if condition, then you will have to maintain the indentation.

42:11

But here because there is one condition is,

42:13

so users have to maintain this special condition.

42:14

to maintain this specific indentation.

42:17

Okay, indentation is the heart of Python.

42:19

Okay?

42:20

Can we nest in the else or you can nest.

42:24

You can nest in, you can not nest in else.

42:27

Because else we have a condition not,

42:29

you can nest in if and else if, LF.

42:33

Okay.

42:34

Nest method there is no condition generally.

42:36

So there is no need to give anything there.

42:38

Okay, everyone comfortable till here.

42:41

Now, we are loops about loops.

42:43

Loops can also read.

42:45

So when I say that we are able to nest if conditions,

42:50

then we can actually also nest the loopings.

42:55

Whatever loops we are writing,

42:58

we can also nest can also.

43:00

So let's try to understand that as well.

43:13

Okay. Now, what is nesting? Nesting means one thing inside the other.

43:24

Does everyone agree? This is called nesting.

43:28

Right? Now when I say that nested loop, what does that mean?

43:34

That one loop inside the other loop.

43:42

Okay, yes, can you please tell an example?

43:54

Let's try to understand.

43:56

I write a loop for I in range 0 to 3.

44:10

make sense. Then I write another loop for J in range 4.

44:25

First of all, if I have to tell what it will produce, it will produce 012.2, can I say that?

44:36

Can I say that?

44:38

Can I say that?

44:39

Can I say that?

44:40

Does everyone agree?

44:45

Does everyone agree that the outer for loop is

44:49

0,1,2 produce correct?

44:52

And the inner for loop is what it will produce?

44:54

Can anyone please tell me?

44:57

What will be 0 1, 2, 3?

44:59

Absolutely correct.

45:02

Now, when the code line comes here, that print i.

45:07

What is going to happen?

45:13

Let's try to understand that.

45:16

In iteration number 1, when i is equals to 0, your code will come here, J will become 0.

45:24

Does everyone agree?

45:26

Does everyone agree?

45:28

And we will print 0, 0.

45:32

Does everyone agree?

45:34

We will print 0,0.

45:36

Correct?

45:37

Okay.

45:38

Then what will happen?

45:39

Is the internal loop completed?

45:41

Is the internal loop completed?

45:43

Is the internal loop completed?

45:46

No.

45:48

So next time, what will be the value of J?

45:52

In the next iteration, J's the value can be?

45:55

1.

45:56

But i.

45:57

It is still 1.

45:59

Does everyone agree?

46:01

I, that is still 1.

46:04

Sorry, I is still 0.

46:06

Does everyone agree with me?

46:08

Because we have not exited this loop.

46:11

Correct?

46:13

We have not exited this loop yet.

46:17

So I will be still 0.

46:20

So this time what we will print?

46:22

0.1.

46:24

Can you all understand?

46:26

Everyone agrees with me?

46:29

Right?

46:31

Yes or no?

46:33

Next time what will happen?

46:35

I will be 0.

46:36

J will become 2.

46:39

What we will print?

46:41

0.2.

46:43

Next time what will happen?

46:44

I will be 0.

46:47

J will be 3.

46:48

What we will print?

46:51

0.3.

46:52

Is everyone comfortable till here?

46:55

Now, J-ki range is

46:58

Does everyone agree?

47:00

J-ki range has over now.

47:02

Like it is ended.

47:04

So what will happen?

47:05

From here,

47:06

you will go to this loop again and now I will become 1.

47:12

Can I say that?

47:14

Now I will be incremented.

47:17

So as soon as I gets incremented,

47:21

it will come inside this.

47:26

What will be the value of J?

47:28

It will be 0.

47:30

Does everyone agree?

47:33

So you will print 1

47:35

1.

47:36

0.

47:37

Then the same thing.

47:40

I will be 1.

47:41

J will be 1.

47:42

1.

47:43

J will be 1.

47:44

1.

47:45

I will be 1.

47:47

2.

47:48

I will be 1.

47:50

J will be 3.

47:52

So 1.0, 1.1, 1.2, 1.2, 1.3.

47:58

Kya is clear.

47:59

This is how the nested for loop will work.

48:05

Is everyone comfortable with this?

48:06

this.

48:07

Do this?

48:08

Do we have?

48:09

Do we have someone with us?

48:10

Do we have someone with us?

48:25

Okay.

48:26

So can I say, can I make this statement,

48:31

that for every iteration of outer for loop?

48:35

For every iteration of outer far loop, the inner far loop will completely run.

48:46

Can I say that?

48:49

So to note for every iteration of outer far loop

48:57

of every iteration of outer

49:02

of outer for loop, inner loop will run.

49:07

inner loop will run

49:18

Does everyone agree with me on this?

49:34

Does everyone agree with me on this?

49:36

agree with me on this.

49:38

Pucka 100%?

49:40

Okay.

49:42

So if that is the case,

49:45

iteration means

49:47

when I becomes 0, J is 0.

49:50

That is called one iteration.

49:53

Like one loop.

49:56

Okay, Khushu?

49:57

That is called iteration.

49:59

Does that answer your question?

50:01

Khudhu?

50:05

Okay.

50:07

Okay?

50:09

Okay?

50:10

Now, the thing is,

50:12

if someone will tell you,

50:14

this loop,

50:15

assume that outer loop will run n times.

50:20

Inner loop will run m times.

50:24

So total number of iterations, how many iterations will happen?

50:28

Can anyone please tell me?

50:30

The outer is 0 to n.

50:32

The inner is 0 to m.

50:34

Total, how many iterations will it happen?

50:37

Will it take?

50:40

Think and tell me.

50:43

How many iterations in total?

50:46

No, number not.

50:47

N and M key terms, if outer loop will run n times and inner will m times.

50:54

How many total number of iterations approximate it will run?

50:58

Can I say n into m?

51:03

Can I say?

51:04

N into M? Because for every outer iteration, the internal loop will completely

51:12

rerun. Right?

51:14

Take it.

51:16

Now, there is one more thing that I would like to discuss.

51:19

Everyone knows that this is a list.

51:22

Correct?

51:31

Everyone knows that this is a list.

51:33

Okay.

51:34

care. But can I do something like this?

52:04

What do you guys think? Can I do something like this?

52:12

Actually you can do.

52:15

This is called as 2D list.

52:20

Basically, a list within a list.

52:25

A list within a list. A list within another list.

52:29

So outer list is what is the outer list? This is the outer list here.

52:33

And internal list can see?

52:36

Internal this, this and this.

52:39

Is everyone clear with this?

52:41

So if I ask you,

52:44

List within a list within a list?

52:46

Yes, Ayush.

52:48

Okay?

52:49

So if I ask you to tell me

52:54

if I ask you to iterate over all the elements in this list,

53:02

It can be anything. It can be 150. How does that matter?

53:06

It is a number unki.

53:08

It can be anything.

53:09

Okay?

53:10

Now tell me one thing.

53:12

If I ask you to iterate over this list,

53:16

think for two minutes and tell me how you will do it.

53:20

Don't write code.

53:22

Just think, how do you iterate over a list?

53:25

And now with this, how will you iterate?

53:28

I can give you two minutes to think on it.

53:31

Think.

53:32

tell me. Don't give answers without thinking.

54:02

Okay, let's discuss.

54:17

For

54:18

I in range,

54:23

list, for

54:29

0.

54:30

First of all, can someone tell me how do I iterate over a list?

54:37

I don't know.

54:38

I'll not tell you.

54:39

How do you iterate over a list?

54:41

Can someone please tell me?

54:44

For I in,

54:45

this we do we like a trace?

54:47

For I in list.

54:48

There are multiple ways to iterate over a list.

54:51

Can you all know?

54:53

Do you all know?

54:54

There are multiple ways to iterate in a list, right?

54:57

So we're the simple example.

54:59

For

55:00

R in list.

55:07

R means row.

55:10

Initially, what will be the value of R for the very first iteration?

55:14

What will be the value of R for the very first iteration?

55:17

0.

55:20

The first list.

55:22

Can I say that this will, this complete list

55:26

will be the value of the first iteration because this is at

55:30

index 0. This is at index first. And this is at index second. Can I say that?

55:37

Does everyone agree?

55:39

Does everyone agree?

55:41

Do you know that?

55:43

No one of the index is the first list.

55:47

So, if I do for R in this list, print R, what will be the output?

55:57

What will be the output?

55:59

10.

56:00

20, 30, 40, 50.

56:06

Then in the second iteration, when I is 0,

56:10

when I is 1, 1, 2, 3, 4, 5, and when I becomes 200 and 150.

56:19

What this?

56:21

Everyone agree with me on this?

56:23

Ok, 100%.

56:27

So, now because

56:29

Because this R itself is a list right now.

56:33

This R itself is a list right now.

56:37

So, can I also, I iterate on that as well?

56:40

Can I iterate on that as well?

56:43

What do you think?

56:45

This R itself is a list.

56:47

So, can I say that I say that

56:49

for

56:59

See?

57:03

Okay.

57:04

Now, if I'm this to print to try to try to understand,

57:08

let's try to understand.

57:11

When I is, when R is 0, then what will?

57:16

So what will?

57:19

10, 20, 30, 40, 50.

57:24

Internal fall loop will completely run.

57:27

The inner-for loop is, that

57:29

everyone agrees with me on that.

57:31

So C will become 0,

57:35

C will become 1,

57:37

C will become 2,

57:38

C will become 3,

57:40

C will become 4.

57:41

When C becomes 0,

57:43

what output do you need?

57:45

10.

57:47

When C becomes 1, what output

57:49

What output do you should?

57:50

20, 30, 40, 50.

57:54

Here, internal for loop is completed now.

57:57

internal fall loop is completed now.

58:01

What?

58:02

What are?

58:03

R can be?

58:04

R can be 1.

58:05

As soon as R-bana 1,

58:08

our list will be 1, 2, 3, 4, 5.

58:11

Does everyone agree?

58:16

And as this is,

58:18

we'll run again.

58:20

And next time it will print 1, 2, 3, 4, 4, 5.

58:26

What?

58:27

So this is how,

58:28

we are

58:30

how we are

58:33

a 2D list

58:34

up, 2D list or matrix

58:38

on

58:39

iterate

58:40

can.

58:41

Okay,

58:42

Sanyupta, please pay attention this time,

58:44

okay?

58:45

Initially,

58:48

R's what are

58:49

saying,

58:50

Sanyukta?

58:51

10, 20, 30, 40, 50,

58:53

50,

58:54

can I say that?

58:55

Right?

58:57

When this one

59:02

the internal loop run

59:04

is this one,

59:07

the value

59:08

what will be

59:09

10, then 20, then 30,

59:12

then 40, then 50, then 50.

59:14

Can this is,

59:15

Sanukta?

59:16

C is basically the current number.

59:20

C is basically the current number.

59:21

C here is

59:23

This is C.

59:27

Okay.

59:28

Now, next time, R will change,

59:31

R will become 1, 2, 3, 4, 4.5.

59:34

And then C will again become 1, 3, 4, 5, so we will print.

59:41

And similarly, as we'll

59:43

we'll fully list click, is this clear to everyone?

59:51

Is this clear to everyone?

59:52

Is this clear?

59:53

Now we look at code and one

59:55

one in the code

59:56

also dry run

59:57

so that we have

59:58

idea.

59:59

Okay?

1:0:00

Okay?

1:0:01

Okay.

1:0:02

Okay.

1:0:05

Okay.

1:0:09

So,

1:0:10

are you

1:0:11

can

1:0:13

see my screen

1:0:14

can

1:0:16

everyone is able to see?

1:0:17

Everyone is able to see?

1:0:23

Yes or no?

1:0:25

Okay.

1:0:27

So, let's create two lists.

1:0:32

List number one, shirts.

1:0:35

Okay, let's create first list.

1:0:37

First.

1:0:38

One, two, three, four, five.

1:0:41

List number second.

1:0:43

Eleven, twelve, third, or let's say, six, seven, eight, nine.

1:0:52

seven, eight, nine, ten.

1:0:56

Okay.

1:0:57

Now, if I want to nest the two list together,

1:1:03

how can I?

1:1:05

I in first?

1:1:08

Can I say that?

1:1:11

For J in second.

1:1:14

Print I

1:1:18

J

1:1:19

J.

1:1:21

Yes.

1:1:22

Okay,

1:1:23

what this is all of

1:1:24

all of them?

1:1:25

So we'll run it and see what

1:1:28

we'll

1:1:29

see what print it.

1:1:30

Okay.

1:1:47

So,

1:1:48

1.6 print is

1:1:50

Does, is?

1:1:51

Is, what are you?

1:1:52

all this?

1:1:53

1.7, then 1.8, then 1.9, then 1.10.

1:1:58

Now, this is the loop is

1:2:02

outer loop finished.

1:2:05

Okay?

1:2:06

Okay?

1:2:07

In the loop.

1:2:09

We'll back on it, so that we'll back idea will.

1:2:12

If you'll go back,

1:2:13

if you'll look,

1:2:14

if you'll see, 1.6, 1.7, 1.8,

1:2:17

1.

1:2:18

9, 1.10.

1:2:20

Inner loop finished.

1:2:22

Okay?

1:2:23

Then 2.6, 2.7, 2.8, 2.9, 2.10.

1:2:30

Is this clear?

1:2:32

Then again, your inner loop finished.

1:2:34

Everyone clear.

1:2:36

How this works?

1:2:38

Does that make sense?

1:2:41

Sir, if we want to print the third list again,

1:2:44

then we will have to run.

1:2:45

If you know, you have one list

1:2:47

third.

1:2:48

which says 0,000.

1:2:55

Okay?

1:2:56

Let's let's have this list.

1:2:57

Now, if I have a third list

1:3:00

then I have to run

1:3:01

then what I have to do

1:3:02

K in third

1:3:08

and something like this.

1:3:10

I, comma, J

1:3:12

comma,

1:3:14

K.

1:3:15

Right?

1:3:17

So.

1:3:18

J loop finished.

1:3:23

Print.

1:3:24

K loop finished.

1:3:27

Now, we'll look

1:3:28

see that this is how it?

1:3:30

Alright.

1:3:32

Sorry.

1:3:33

Right.

1:3:35

Come on.

1:3:38

Alright.

1:3:40

Okay.

1:3:41

Now,

1:3:42

if I look,

1:3:43

when I was 1,

1:3:45

J,

1:3:46

my 6th,

1:3:47

I'll take minus 1 comma minus 2

1:3:49

so it's a little clear

1:3:51

So I'm again

1:3:53

Now if I

1:3:55

look

1:3:56

I was

1:3:57

I was

1:3:58

J6

1:3:59

K minus 1

1:4:00

was

1:4:01

I was

1:4:03

J6

1:4:04

K minus 2

1:4:05

I mean

1:4:06

the internal loop

1:4:07

it's

1:4:08

complete

1:4:09

complete

1:4:10

for the third list

1:4:11

for the third list.

1:4:12

Do you

1:4:13

see that

1:4:14

all

1:4:15

this

1:4:16

The

1:4:17

then

1:4:18

the

1:4:19

second

1:4:20

the loop is

1:4:21

and then

1:4:22

we're

1:4:23

same thing

1:4:24

and then

1:4:25

eight with

1:4:26

same thing

1:4:27

then

1:4:28

and then

1:4:29

we're

1:4:30

then

1:4:31

we're

1:4:32

then

1:4:33

the

1:4:34

last number

1:4:35

and then

1:4:41

Is

1:4:42

all you all

1:4:43

all

1:4:44

you know

1:4:45

everyone

1:4:47

I'm

1:4:50

okay

1:4:51

okay

1:4:52

so

1:4:53

I'm

1:4:54

I'm

1:4:55

comment

1:4:56

I'm

1:4:57

now

1:4:58

we're

1:4:59

I'm going

1:5:00

let's go

1:5:01

I'm

1:5:02

I'm

1:5:03

we have

1:5:04

two lists

1:5:05

shirts

1:5:06

white, black and pants

1:5:15

black

1:5:18

black

1:5:19

khaki

1:5:21

and that's a gray

1:5:24

I want combination of every shirt with every pant how will you do it?

1:5:28

I will give you three minutes to think

1:5:32

write code and tell me the code in the chat once you're done.

1:5:35

Okay?

1:5:36

2050 pay I will come back and we will discuss. I want, what I want? I want combination of every shirt with every bander.

1:6:06

You know,

1:6:08

I'm

1:6:09

a

1:6:10

You know,

1:6:40

You

1:6:42

You

1:6:44

I'm

1:6:46

you

1:7:14

I'm

1:7:16

you

1:7:44

Okay

1:7:48

Okay

1:7:52

Okay,

1:7:53

Okay,

1:7:56

Okay,

1:7:57

Okay,

1:7:58

all

1:7:59

all

1:8:01

they were

1:8:02

to

1:8:03

do

1:8:04

it was

1:8:05

to do

1:8:17

to do?

1:8:18

What?

1:8:19

What?

1:8:20

We have two nest-a-a-toop

1:8:21

,

1:8:22

right?

1:8:23

for I in

1:8:25

for shirt in shirts

1:8:28

in shirts

1:8:32

for pant in pants

1:8:34

in pants

1:8:36

print

1:8:37

shirt

1:8:39

shirt

1:8:41

shirt

1:8:42

and

1:8:47

Pant?

1:8:49

Correct?

1:8:50

Yeah,

1:8:51

and what?

1:8:52

Am I correct?

1:8:53

Run the code?

1:8:54

White, black, white khaki, white, gray.

1:8:57

Black, black, black

1:8:59

black khaki, black, black gray.

1:9:01

Can you all

1:9:02

have all

1:9:03

said?

1:9:05

Everyone?

1:9:07

Now, do you guys remember,

1:9:10

we have

1:9:11

some special keywords

1:9:13

when we were

1:9:14

discussed

1:9:15

continue,

1:9:16

break,

1:9:18

do you guys remember that part?

1:9:20

Do you

1:9:21

that

1:9:22

kind of

1:9:23

actually,

1:9:24

we

1:9:25

we

1:9:26

use

1:9:27

for example,

1:9:28

for example,

1:9:30

if

1:9:32

shirt is

1:9:33

equal to

1:9:34

white

1:9:36

or black

1:9:37

and

1:9:39

and

1:9:40

pant is equal to

1:9:44

print

1:9:44

if that is the case, then what I will do, I will continue.

1:9:49

So,

1:9:50

what is the

1:9:51

combination print

1:9:52

What

1:9:53

that

1:9:54

combination print?

1:9:55

No,

1:9:56

so let's see,

1:9:57

look

1:9:58

black with black print

1:9:59

but if I

1:10:00

here

1:10:01

break, then what

1:10:03

it would?

1:10:04

If I use a break here,

1:10:05

what it will do?

1:10:06

It will actually

1:10:08

break the loop from that point.

1:10:10

It will internally

1:10:12

this internal

1:10:13

he break

1:10:14

outer iteration will still work.

1:10:17

Am I correct?

1:10:18

The outer iteration will still work, but the internal will fail.

1:10:23

Let's run the code.

1:10:25

White black, white khaki, white white.

1:10:29

Does that make sense?

1:10:31

Do you

1:10:35

have all

1:10:36

everyone

1:10:37

clear?

1:10:38

Okay?

1:10:39

Okay?

1:10:41

Okay.

1:10:43

Okay.

1:10:45

Okay.

1:10:46

Okay.

1:10:47

So,

1:10:48

now we

1:10:49

discuss

1:10:50

two-d-d-list

1:10:51

things.

1:10:52

We

1:10:54

can

1:10:55

how

1:11:01

2D list.

1:11:03

Like,

1:11:05

1, 2, 3, 4, 5,

1:11:07

comma,

1:11:08

11, 22, 32, 34, 45,

1:11:13

comma,

1:11:15

100, 200, 300,

1:11:17

400, 400,

1:11:18

500.

1:11:20

Okay?

1:11:21

This is my a 2D list.

1:11:23

This is how I can define a 2D list.

1:11:26

If I have this is how I can define a 2D list.

1:11:27

If I have it to print it, then how I can do

1:11:28

I will do the list.

1:11:30

Let's run the code and see.

1:11:32

Do you can see?

1:11:33

Do you can see that

1:11:34

the two-d list is actually as a list

1:11:36

printed is?

1:11:38

This is iteration number 0,

1:11:40

index number 0,

1:11:42

index number 1, index number 2.

1:11:46

What are all

1:11:47

people are?

1:11:49

Everyone?

1:11:50

Right?

1:11:54

So, basically,

1:11:56

what is

1:11:57

What it has, this is how you can define a 2D list.

1:12:01

Now, if I have to look at 2D list,

1:12:05

so how I will do?

1:12:06

For I in...

1:12:11

How can I will, please?

1:12:14

For current?

1:12:16

So, what we'll tell you?

1:12:18

For current?

1:12:20

So, what we say?

1:12:21

For row in 2-day list.

1:12:26

For column in row.

1:12:30

Print?

1:12:32

What I have?

1:12:34

Print?

1:12:35

Row.

1:12:36

Row.

1:12:38

Column.

1:12:39

Column.

1:12:40

What do you know?

1:12:41

What I have?

1:12:42

What I've done?

1:12:43

What I've done?

1:12:44

Now, if I've got it?

1:12:45

Now, if I'm print to do,

1:12:48

this, okay, I've something

1:12:51

I've done.

1:12:52

And what's what we've done?

1:12:54

What we've done?

1:12:55

What?

1:12:56

I've done?

1:12:57

I've got what?

1:12:58

I've done.

1:12:59

That,

1:13:00

this print, what is,

1:13:01

it's not really,

1:13:02

it's not really.

1:13:03

Anyone would like to answer?

1:13:08

What is?

1:13:09

what I've got it?

1:13:11

This is,

1:13:12

this is,

1:13:13

this is,

1:13:14

actually,

1:13:16

I've,

1:13:17

the row,

1:13:18

that's

1:13:19

all right

1:13:20

all of that

1:13:21

all right?

1:13:22

I'm actually

1:13:23

actually,

1:13:24

no,

1:13:25

because row is a

1:13:26

complete list

1:13:27

right?

1:13:28

So,

1:13:29

do you

1:13:30

do

1:13:31

everyone agree?

1:13:32

One, two, three, four,

1:13:33

five, then we

1:13:34

a break-d-prent-for-five

1:13:35

one,

1:13:36

two, three, four, five,

1:13:37

hundred,

1:13:38

200, 300, 400,

1:13:39

If there is a, there is another easier way to iterate over 2D list, what

1:13:46

what is, for I, comma, v, sorry, for I,

1:13:54

for I,

1:13:56

j,

1:13:59

enumerate of 2D list,

1:14:04

this

1:14:05

what will,

1:14:06

what will give you,

1:14:07

print,

1:14:08

I,

1:14:10

comma j

1:14:12

now we

1:14:13

we

1:14:14

see this

1:14:15

what

1:14:16

he

1:14:17

will

1:14:18

this

1:14:19

and

1:14:20

this

1:14:21

and

1:14:22

the

1:14:23

I can

1:14:24

I can

1:14:25

index

1:14:26

and

1:14:27

and

1:14:28

what do you

1:14:29

what do you guys think?

1:14:30

so

1:14:31

so internal list

1:14:32

and

1:14:33

index

1:14:38

So this

1:14:39

internal,

1:14:40

this is

1:14:41

this

1:14:42

and this list,

1:14:43

this is

1:14:44

this is

1:14:45

this list.

1:14:46

this is

1:14:47

all

1:14:48

this is

1:14:49

line 37

1:14:51

we

1:14:52

we've

1:14:53

we've

1:14:54

we've

1:14:55

in code

1:14:56

if you remember

1:14:58

right,

1:14:59

right.

1:15:00

line 37 on

1:15:01

for

1:15:02

for column in a row

1:15:03

row.

1:15:04

for

1:15:05

for I in anything

1:15:07

anything which is a

1:15:08

2D list.

1:15:09

So when

1:15:09

iteration I

1:15:10

0

1:15:11

will

1:15:12

then

1:15:13

this

1:15:13

value I pick

1:15:14

my 2D list

1:15:15

right

1:15:15

Vichal?

1:15:16

Now this

1:15:17

this value is

1:15:17

it's a

1:15:19

list is a

1:15:19

list

1:15:19

so can I

1:15:20

can I

1:15:20

say that

1:15:21

I

1:15:21

have that

1:15:21

I

1:15:22

iterate

1:15:23

to iterate

1:15:23

and that's

1:15:27

what I'm

1:15:27

doing here

1:15:28

and that's how what I'm doing here.

1:15:31

No no

1:15:32

this row comma

1:15:33

column these are

1:15:33

variable names

1:15:34

okay these are

1:15:36

these are

1:15:36

we're

1:15:37

here we're

1:15:37

right,

1:15:38

index,

1:15:38

internal

1:15:39

list,

1:15:39

these are

1:15:40

variable

1:15:40

names.

1:15:40

Okay?

1:15:41

Everyone

1:15:43

clear?

1:15:44

Everyone clear?

1:15:45

Line number 43.

1:15:50

Yeah,

1:15:51

okay.

1:15:52

So line number 43

1:15:55

what is?

1:15:56

This is a

1:15:57

a different type

1:15:57

syntax

1:15:58

is.

1:15:59

If I want the

1:16:01

index

1:16:02

as well as

1:16:04

the complete row,

1:16:05

then I

1:16:06

will use this

1:16:07

enumerate function.

1:16:09

So instead of

1:16:10

you

1:16:10

use

1:16:10

or

1:16:11

then

1:16:11

or other

1:16:11

print

1:16:11

you

1:16:12

you

1:16:12

you

1:16:13

you

1:16:14

can

1:16:15

fetched

1:16:16

using

1:16:17

this

1:16:18

yes

1:16:19

mapping the

1:16:20

number

1:16:20

and the

1:16:20

items

1:16:20

so

1:16:21

you

1:16:21

here

1:16:21

you

1:16:21

see

1:16:21

here

1:16:22

you

1:16:23

are

1:16:23

and it

1:16:23

complete

1:16:23

area

1:16:23

and it

1:16:25

is

1:16:26

here

1:16:26

is

1:16:36

control back slash, control backslash. If

1:16:39

if Mac in Mac

1:16:40

if the data type of the output?

1:16:41

What is the data type of the output?

1:16:43

Uh,

1:16:44

this output

1:16:45

the output

1:16:46

and if I'm

1:16:48

up the

1:16:49

output

1:16:50

then the data type integer

1:16:51

will

1:16:52

this

1:16:53

single value

1:16:54

integer

1:16:55

right

1:16:56

makes sense?

1:16:58

Can

1:16:59

here

1:16:59

here

1:17:06

So,

1:17:07

we are why it is called

1:17:09

2D list?

1:17:10

Because

1:17:10

it's nested

1:17:11

is

1:17:12

which

1:17:13

single list

1:17:14

we're

1:17:14

we're

1:17:14

we're

1:17:14

called

1:17:15

1D list

1:17:15

and

1:17:17

because it

1:17:17

is two-d

1:17:17

list

1:17:18

is

1:17:18

two-d

1:17:19

is nested

1:17:20

so we

1:17:21

we're

1:17:21

we're

1:17:21

we're

1:17:22

we're

1:17:24

repeat

1:17:24

what

1:17:24

you

1:17:24

specifically

1:17:25

you

1:17:25

will

1:17:25

you

1:17:26

want

1:17:27

to

1:17:27

what do you want me to

1:17:27

repeat

1:17:28

specifically

1:17:29

specifically

1:17:29

any

1:17:33

specific line

1:17:34

that you

1:17:34

want me to

1:17:35

or anything

1:17:36

I'm sure there.

1:17:51

Cool.

1:17:52

Till here, everyone comfortable.

1:17:54

So I will give you some times,

1:17:56

I will give you some time

1:17:57

to play around with list.

1:18:00

Let's come back by

1:18:01

2108 in 8 minutes.

1:18:06

line number 36.

1:18:13

This is our

1:18:15

normal line, right?

1:18:18

This is our normal line.

1:18:19

We're in row

1:18:19

we

1:18:19

we're in any list

1:18:20

we iterate

1:18:21

how

1:18:22

we're

1:18:23

so we're

1:18:23

for I in

1:18:25

any list

1:18:26

correct?

1:18:27

This is a

1:18:27

normal line.

1:18:31

If I

1:18:32

if I

1:18:32

would have a

1:18:32

single list

1:18:33

then I'd

1:18:33

would be

1:18:34

I'd iterate

1:18:34

for example

1:18:36

this list

1:18:36

So this

1:18:37

I'm

1:18:37

how I iterate

1:18:38

for I in first?

1:18:40

Right,

1:18:40

Sadeik?

1:18:41

Right, Saddik?

1:18:47

If 4 times nested, no,

1:18:49

No, no Prashat.

1:18:50

Okay, guys.

1:18:51

Let's come back by

1:18:52

9.8 PM IST

1:18:54

and then let's discuss.

1:18:55

Okay?

1:19:06

You know,

1:19:08

You know,

1:19:38

You know,

1:20:08

I'm

1:20:38

I'm

1:21:08

I'm

1:21:38

Thank

1:21:40

You

1:21:41

You

1:21:42

I'm

1:21:44

I'm

1:21:46

Thank you.

1:22:16

Thank you.

1:22:46

Thank you.

1:23:16

Thank you.

1:23:46

Thank you.

1:24:16

Thank you.

1:24:46

Thank you.

1:25:16

Thank you.

1:25:46

Thank you

1:26:16

Thank you

1:26:46

Thank you

1:26:48

Thank you

1:26:50

Thank you

1:26:52

Thank you

1:26:54

Thank you

1:26:56

Thank you

1:26:58

Thank you

1:27:00

Thank you

1:27:02

Thank you

1:27:04

Thank you.

1:27:34

okay so are we back everyone

1:28:04

Is everyone back?

1:28:05

Okay, so let's resume the session.

1:28:09

So, what we've seen what?

1:28:11

Basically, how do you deal with multiple nested loops?

1:28:17

Now, at the same time I would like to also discuss, can you also nest while loops now?

1:28:24

Can you have two wild loops nested?

1:28:26

Definitely yes.

1:28:27

Now, now you're nesting anything,

1:28:29

a while loop, a four loop, two four loops, two wail loops, and this nesting can

1:28:34

go into multiple levels.

1:28:36

Now we have just two levels of nesting

1:28:38

discuss but it can happen that you have a multiple level listing.

1:28:41

Does that make sense to everyone?

1:28:48

Correct.

1:28:51

So now we actually discuss

1:28:53

complexity analysis.

1:28:55

Efficiency, why efficiency matters when you write code.

1:28:59

So let me create a heading.

1:29:04

Complexity analysis.

1:29:15

Now,

1:29:32

Here,

1:29:34

if I give you a book, a telephone book.

1:29:39

And ask you to find you a telephone book.

1:29:44

And ask you to find my phone number in that.

1:29:50

Yashka phone number, find out the Yashka phone number from the telephone book.

1:29:57

Now there are two people.

1:29:59

One I've Tamanna to have asked,

1:30:01

and second I have asked Sanyukta.

1:30:03

Sanyukta.

1:30:04

Okay?

1:30:05

So way number one is you go through every page and every name until you find the name.

1:30:18

Right?

1:30:19

Go through.

1:30:24

Every page.

1:30:26

Every name.

1:30:30

Until you find my name.

1:30:32

until you find my.

1:30:34

All right?

1:30:40

This is the first approach.

1:30:42

Second approach can be.

1:30:44

This is a little smart approach.

1:30:48

The phone book are always sorted.

1:30:50

So what you do?

1:30:53

You find the middle of phone book.

1:30:56

Then you see, okay, you are at what character?

1:31:03

Are you at S or are you at Z?

1:31:07

Depending on that, you will either go left or you will go right.

1:31:10

Correct?

1:31:11

So basically what you have done is you have divided or you will have a look at the index.

1:31:21

Yes.

1:31:22

Y can start with it.

1:31:24

So what you have done is you have narrowed down your search space.

1:31:29

Can I say that?

1:31:33

So if that is the case, probably I will need 10 to 12 checks only.

1:31:47

If there are 1,000 pages, for example, and yesh is at the, why is at the last page.

1:32:01

So how much?

1:32:03

So how many names are there on the last page?

1:32:05

You just have to go over them and then finally do it.

1:32:09

Here, what you will have to do?

1:32:11

You will have to go through every page A, B, C, all of that.

1:32:15

And when the Y by the page comes, then you start going through my name.

1:32:19

So the problem is, what is better approach?

1:32:22

Way number two or way number one?

1:32:24

What better?

1:32:25

How's the way number two?

1:32:31

Why?

1:32:32

Because way number two fast.

1:32:34

We're searching in here in this.

1:32:36

Actually, we're searching it.

1:32:38

So search kind of the way can't that you open the book and start one by one.

1:32:43

And second way is you directly go into the index, check why the page number and you search there.

1:32:49

So way two is better.

1:32:51

Two programs, two different methodology.

1:32:54

Two different methodology.

1:32:55

same answer.

1:32:57

The answer is same.

1:32:58

Is it?

1:32:59

Is there the phone number is a different?

1:33:01

in the way one and phone number two

1:33:03

will be?

1:33:04

Can it be?

1:33:05

Can't it?

1:33:06

Here is my phone number 70105, something, something, something?

1:33:09

Or here here at 98, 935, something, something?

1:33:11

Is this?

1:33:12

No.

1:33:13

At the end of the day, the phone number is,

1:33:15

the same he will.

1:33:17

So two ways to find a solution

1:33:20

and both of them vary completely.

1:33:23

this, you have a very time

1:33:25

will.

1:33:26

This, comparatively, less time

1:33:29

will.

1:33:30

Right?

1:33:31

If

1:33:32

this same thing if

1:33:33

if we have

1:33:34

we have to do

1:33:35

how we will,

1:33:36

how we will we

1:33:38

do?

1:33:39

Even though

1:33:41

you are using a get function, Prashant,

1:33:43

then also,

1:33:44

way 2 is always better.

1:33:45

Correct?

1:33:46

Way 2 is better eventually that I want to say.

1:33:48

Now you use a get function

1:33:49

or you narrow down your search,

1:33:51

whatever you want to do.

1:33:52

Yeah,

1:33:53

then O of 1 in it

1:33:54

can do it.

1:33:55

Okay?

1:33:56

So what I want to say is that

1:33:58

if the same thing

1:33:59

I have to do

1:34:00

the same thing in my code

1:34:01

also,

1:34:02

I can do the same thing in my code also.

1:34:05

I have a list of 1 lakh characters

1:34:08

and in that 1 lakh numbers,

1:34:10

I want to find a 1 lakh number,

1:34:12

like I want to find a specific number.

1:34:14

Way number 1 can be that you start by 1 by 1

1:34:17

or second way can be

1:34:20

you create it as a dictionary and then find it

1:34:22

and then find it. Am I correct?

1:34:26

Correct?

1:34:27

Correct?

1:34:28

Does everyone agree?

1:34:33

So there are multiple ways to solve one problem that I want to say.

1:34:36

These are two problems.

1:34:38

So,

1:34:39

now,

1:34:40

we have same in the

1:34:42

code's complexity

1:34:43

be find out

1:34:44

because if there are multiple ways to solve one single problem,

1:34:50

we always want to solve one single problem,

1:34:51

we always want to solve

1:34:52

the problem using optimized way.

1:34:54

If a problem

1:34:56

a problem to solve 15

1:34:57

there are

1:34:58

I need the best way.

1:34:59

Does everyone agree?

1:35:01

Is this all

1:35:03

all that we should always go ahead with the best way?

1:35:06

It's not not that

1:35:08

if a specific problem I can solve

1:35:11

in one minute,

1:35:13

I am using a way which is taking one hour to solve

1:35:16

it.

1:35:17

Is this is first of all?

1:35:18

No,

1:35:19

this not.

1:35:20

Does everyone agree?

1:35:21

agree?

1:35:22

Okay.

1:35:23

So written some piece of code,

1:35:28

written some piece of code,

1:35:33

how do you measure the complexity of it?

1:35:51

Any thoughts? How can we?

1:35:53

Any thoughts?

1:35:54

How can say,

1:35:57

yes, okay,

1:35:58

you're here,

1:35:59

you here,

1:36:00

start time,

1:36:01

and you can compare how much your algorithm took?

1:36:04

No, that is not correct.

1:36:07

Why?

1:36:09

Because

1:36:10

your system

1:36:12

in your system

1:36:13

is how much process is

1:36:15

running,

1:36:16

all of these things will affect

1:36:18

that start time and end time

1:36:20

I want a general solution which is acceptable worldwide.

1:36:25

I mean that any computer

1:36:27

I run it.

1:36:28

Well, I run it on Windows

1:36:30

Mac, run on,

1:36:31

high processor computer

1:36:32

on low processor computer

1:36:34

on,

1:36:35

I should be able to say that this

1:36:38

algorithm is this much complex.

1:36:41

This specific way to is this much complex.

1:36:44

Is this much complex?

1:36:46

How many steps does one function take to complete?

1:36:49

This is this much complex?

1:36:50

overall, a standard way to

1:36:52

right?

1:36:53

So,

1:36:54

for computer science

1:36:56

in big O terms

1:36:57

like,

1:36:58

complexity,

1:36:59

we're in average cases

1:37:01

in the

1:37:02

So in order to analyze the complexity,

1:37:05

what we do

1:37:06

do we do?

1:37:07

three cases

1:37:08

in our algorithm

1:37:09

divide

1:37:10

the

1:37:11

case number

1:37:14

we're

1:37:15

best case.

1:37:16

Case number two

1:37:19

we're going to

1:37:20

average case

1:37:21

and case

1:37:23

number three, we

1:37:23

we're

1:37:24

both

1:37:25

case.

1:37:26

Okay,

1:37:27

they

1:37:28

what

1:37:29

means?

1:37:30

For example,

1:37:31

I have

1:37:33

this.

1:37:34

I have this.

1:37:39

I have this

1:37:43

I have this.

1:37:48

Okay, what just happened?

1:37:50

Yeah.

1:37:51

I have this.

1:37:52

Now, if I ask you,

1:37:54

find me the value of 10,

1:37:57

find me the value of 10, what will you do?

1:38:02

What will you do?

1:38:04

What will you do?

1:38:05

As you get one

1:38:07

you,

1:38:08

you'll,

1:38:09

you'll stop

1:38:10

can I say that?

1:38:11

Just as you

1:38:13

you'll stop

1:38:14

stop you.

1:38:15

Can you all?

1:38:16

All you get,

1:38:17

So, best case is, that you

1:38:20

the value that

1:38:22

the first value

1:38:23

in your algorithm

1:38:24

or your input in

1:38:25

the

1:38:26

first value if you

1:38:27

if you got

1:38:28

you got

1:38:29

your algorithm or code

1:38:29

where you stop

1:38:30

can I say that?

1:38:31

Can I say that?

1:38:32

Will you go over other numbers in the list?

1:38:35

Then

1:38:37

will you go over other numbers in the list?

1:38:39

Is that needed?

1:38:40

No, because whatever was needed, you have found it.

1:38:43

So that's the best case

1:38:44

is that

1:38:45

the first step in you

1:38:46

your

1:38:48

what you were

1:38:49

did

1:38:50

that you

1:38:51

all of

1:38:52

we all

1:38:53

we're saying

1:38:54

best case.

1:38:55

Is that

1:38:56

is the

1:38:58

best case means

1:38:59

the luckiest input.

1:39:00

Okay?

1:39:02

Target is the

1:39:08

very first item.

1:39:09

Target is the very first item.

1:39:16

Everyone comfortable with this part?

1:39:22

Average case is

1:39:24

basically

1:39:26

a random place

1:39:29

somehow somewhere here.

1:39:32

A random case,

1:39:34

it's here

1:39:35

here here here

1:39:36

a random

1:39:37

in my code

1:39:38

where

1:39:39

where I can

1:39:40

where I can

1:39:41

my search result

1:39:42

somewhere around the

1:39:43

middle

1:39:46

What this is

1:39:47

So,

1:39:48

that we're

1:39:49

we're

1:39:50

where the

1:39:51

target

1:39:52

sits

1:39:53

somewhere in the

1:39:54

middle.

1:39:55

And

1:39:56

the

1:39:58

And

1:40:00

the

1:40:01

third

1:40:05

is

1:40:06

worst case.

1:40:07

Worst case

1:40:08

basically

1:40:09

target

1:40:10

our last

1:40:11

towards the last,

1:40:13

towards the last.

1:40:14

Now,

1:40:15

400

1:40:16

be

1:40:17

it can be

1:40:18

So even though

1:40:19

that

1:40:20

it is

1:40:21

last

1:40:22

but it is almost last.

1:40:23

If I

1:40:24

say,

1:40:25

I have

1:40:26

10 lakh integers

1:40:27

of

1:40:28

that

1:40:29

that

1:40:30

my input

1:40:31

I got

1:40:32

9,000

1:40:33

99,000

1:40:34

So

1:40:35

this is

1:40:36

almost as good as

1:40:37

last

1:40:38

can I say that?

1:40:39

This is

1:40:40

almost

1:40:41

as good as last only

1:40:43

does

1:40:44

Does everyone agree?

1:40:45

I mean

1:40:46

I mean

1:40:47

$9,000

1:40:48

that means

1:40:49

it's

1:40:50

I have already

1:40:51

searched in my list.

1:40:52

It's

1:40:53

I had already

1:40:55

searched in my list.

1:40:57

Okay,

1:40:58

so in

1:41:00

Bada input,

1:41:01

when the

1:41:02

input size is really big,

1:41:04

the

1:41:05

generally

1:41:06

approximation works.

1:41:08

When we say best case

1:41:09

means, okay,

1:41:10

in the first half of the input.

1:41:12

When we can average case,

1:41:13

probably

1:41:14

somewhere in the middle of the input.

1:41:16

And when we say worst case,

1:41:17

probably

1:41:18

it's a good

1:41:19

bura

1:41:20

what is

1:41:21

what?

1:41:22

Worst.

1:41:23

Everyone.

1:41:24

Everyone.

1:41:29

Last of input, yes.

1:41:32

Now,

1:41:34

Sir,

1:41:35

first list

1:41:36

50,

1:41:37

what will

1:41:38

still be

1:41:39

average case,

1:41:40

Arun.

1:41:41

Again, it depends on input.

1:41:42

If I'm a list

1:41:43

there's 10 lakh words.

1:41:45

Okay?

1:41:46

If I give you a list which has 10 lakh words.

1:41:47

Now, if I give you a list which has 10 lakh words.

1:41:50

Now, in this 10 lakh words, you find a word which is somewhere 1,000.

1:42:04

What will you call this? Still an average case for you.

1:42:07

Right? Does that make sense? Still a average case for you.

1:42:11

Now, as an engineer,

1:42:14

we don't know best case

1:42:16

because best case, anyway, it is fine only.

1:42:19

We are fine.

1:42:22

Always the complexity of algorithm is measured in the terms of worst case.

1:42:26

In the terms of worst case,

1:42:30

that you've written, whatever code that you have written,

1:42:34

he will the worst case in how perform

1:42:37

can't?

1:42:38

Is this you all of the same

1:42:39

that you know, if your code is, if it was in worst case

1:42:44

in a good perform it is, then it means the code algorithm is easy.

1:42:51

If your code worst case in a

1:42:54

perform not, then it means we have a problem.

1:42:58

Make sense.

1:43:01

Okay.

1:43:02

So now, as you see, what happens is,

1:43:06

the one thing that which we cannot control is the

1:43:09

input size.

1:43:11

Input size could be

1:43:12

for example, input size can be 1 lakh,

1:43:16

input size can be 2 lakh,

1:43:18

input size can be 10 lakh, correct?

1:43:21

So the algorithm we

1:43:23

find out the time complexity,

1:43:26

we discuss this

1:43:27

discusses that if

1:43:29

if the input size is a big

1:43:30

so,

1:43:32

then your algorithm

1:43:33

has a more time is

1:43:34

time is?

1:43:36

Do you have your algorithm

1:43:37

the algorithm has

1:43:38

that time is

1:43:39

or then your algorithm

1:43:40

more time

1:43:41

longer

1:43:42

we're going to

1:43:43

discuss.

1:43:44

For example, if I made

1:43:45

a function

1:43:46

for example,

1:43:48

I made a

1:43:49

def first item.

1:43:52

Okay, and I am

1:44:00

taking a list of

1:44:01

items here.

1:44:05

and what is items list?

1:44:06

Items list is an is a list. Okay? So what I will do? I will return here,

1:44:16

return items of zero.

1:44:21

Okay?

1:44:22

Okay,

1:44:26

this you have all of

1:44:27

understand?

1:44:29

So now,

1:44:31

if you know,

1:44:32

if I say,

1:44:33

if I say my input size is a

1:44:35

size is 200.

1:44:37

The size of my input is 200.

1:44:40

How many

1:44:42

numbers I will have to scan if I call this function?

1:44:47

How many numbers I will have to read from the list if I call this function?

1:44:52

One.

1:44:54

Why?

1:44:55

Because it is directly accessing the index and returning it.

1:44:58

If I increase my input size from 200 to 20 lakh,

1:45:03

how many numbers now it will

1:45:04

numbers, now it will read. Still one.

1:45:08

Because it's your input size basis

1:45:11

it's not doing.

1:45:12

Right? So this function is the complexity

1:45:15

is constant.

1:45:17

This is called as complex constant

1:45:28

time complexity where the time complexity

1:45:34

does not increase with increase in size.

1:45:50

Is everyone clear with this?

1:45:56

What is constant time?

1:46:00

So how do we represent constant time?

1:46:03

we represented using big O of 1.

1:46:06

This is how we represent a constant time complexity.

1:46:10

Everyone clear?

1:46:13

Do you?

1:46:17

Is this up to understand?

1:46:19

Do you all know?

1:46:24

Do you know?

1:46:26

Yes, no?

1:46:33

Okay?

1:46:35

Now, I'm another thing discuss

1:46:37

which is linear type.

1:46:40

Linear means what?

1:46:41

What is?

1:46:42

What is?

1:46:43

What do you mean?

1:46:47

What do you mean by linear?

1:46:49

What do you mean by linear?

1:46:52

A gradual straight line.

1:46:56

Can I say that?

1:46:58

A gradual straight line?

1:47:00

So if I have a function,

1:47:02

A function def sum number and I take list as an input here.

1:47:13

And what I am doing?

1:47:15

Total equals to 0 for

1:47:28

in list

1:47:32

Total

1:47:34

plus equals to I

1:47:36

and print

1:47:41

total

1:47:46

So,

1:47:48

this function is going

1:47:50

over your list

1:47:52

and

1:47:53

all numbers sum

1:47:54

and here are

1:47:55

here print

1:47:57

with this

1:47:59

All the numbers

1:48:00

sum

1:48:01

sum and print

1:48:03

if I say the input size is

1:48:07

1,000

1:48:09

1,000 numbers in the list

1:48:12

How many times your function will access the elements of the list?

1:48:18

How many times your function will access the elements of the list?

1:48:23

How many times will every element be accessed here?

1:48:26

1,000

1:48:27

Okay, if the input becomes 20 lakh

1:48:30

Now how many times your function will access the elements of the list?

1:48:36

20 lakh times.

1:48:37

Does everyone agree?

1:48:38

So here what is

1:48:40

here,

1:48:41

the

1:48:42

function's time

1:48:44

the number of steps that my function would like to do

1:48:49

is increasing significantly with the size of my input.

1:48:53

Can I say that?

1:48:54

If my input's size is a

1:48:55

small,

1:48:56

it will take less time.

1:48:57

If my input's size is medium,

1:48:59

then it will take less time.

1:49:00

If my input time is

1:49:02

very much time,

1:49:03

it will be a very time

1:49:04

because at the end of the day I have a loop

1:49:07

and this loop what is

1:49:09

I trade on my list's elements

1:49:12

everyone comfortable.

1:49:15

Is this all this is called

1:49:20

linear time complexity?

1:49:22

Linear we represent

1:49:23

we represent

1:49:24

O of N.

1:49:28

I am trying to read all of those inputs.

1:49:30

I am trying to read all of those inputs.

1:49:35

Make sense?

1:49:38

Everyone.

1:49:41

Now the third time complexity

1:49:44

we are,

1:49:45

we call it,

1:49:46

we are non-linear.

1:49:48

And quadratic.

1:49:52

How?

1:49:57

Assume that, I have a list

1:50:01

2, 4, 6.

1:50:06

And I need

1:50:07

output

1:50:09

and I need

1:50:11

every number of every number

1:50:12

multiplication.

1:50:13

I mean 2 into 4, 2 into 6,

1:50:17

4 into 6, 4 into 6, 2 into 6, 2 into 2, 2

1:50:21

2, 4, 6 into 6.

1:50:25

I want this as the out.

1:50:26

this as the output.

1:50:28

So, I'm how can do any thoughts, first of all?

1:50:31

So, how do I will it?

1:50:33

Any thoughts?

1:50:35

I mean, one loop, I'll think,

1:50:37

DEF, nested Sun.

1:50:42

List. What I will do?

1:50:47

for

1:50:49

Yes.

1:50:52

So.

1:50:55

I will do.

1:50:56

enlist for J inlist print I multiplied by J.

1:51:13

K.

1:51:14

K

1:51:18

inlist?

1:51:19

Alright, we'll try run

1:51:22

When I becomes 0.

1:51:25

When I becomes 0.

1:51:26

I, itration number is 0.

1:51:28

So what will?

1:51:29

I's the value?

1:51:30

When I is 0, the iteration, what is the value?

1:51:33

What will be?

1:51:34

Who will me to tell me, please?

1:51:38

2.

1:51:40

Okay?

1:51:41

J is 0, so J2 will be.

1:51:43

So 2 into 2, 4 print

1:51:45

then J is 6,

1:51:48

J is 4, so 2 into 4 print

1:51:51

because I is 2 is 2

1:51:53

be 2.

1:51:54

Then I 2 will be,

1:51:55

J6, then 2 into 6 will.

1:51:58

Then my I will

1:52:00

then J 246 will

1:52:02

So similarly,

1:52:03

here here here,

1:52:05

here my nested loop is

1:52:07

Do you?

1:52:09

all get it?

1:52:10

Here, my nested loop

1:52:12

is

1:52:13

So the thing here is

1:52:15

given an input

1:52:19

Now,

1:52:20

the function is

1:52:22

how many times

1:52:25

The first loop O of n times.

1:52:29

Do you all of n times?

1:52:31

Do you all of n times?

1:52:33

Do you all of n times?

1:52:35

Yes.

1:52:37

And internal loop, how many times access

1:52:39

The internal loop

1:52:41

how can access

1:52:42

the elements?

1:52:44

Can't you?

1:52:46

Can't do?

1:52:47

How do you?

1:52:48

Every iteration for internal loop

1:52:49

how will

1:52:51

For every iteration

1:52:52

for internal loop

1:52:55

When I becomes 2,

1:53:00

J's what are

1:53:02

what are

1:53:03

values

1:53:04

what will

1:53:05

J's what

1:53:06

will

1:53:07

2 for 4

1:53:09

6 for?

1:53:10

that means J

1:53:11

my

1:53:12

value

1:53:13

that means J

1:53:14

J be

1:53:15

O of n times

1:53:17

is

1:53:18

am I correct?

1:53:19

So

1:53:20

total time complexity

1:53:21

is code

1:53:22

of

1:53:25

which is O of n square.

1:53:28

K.

1:53:29

Kya

1:53:31

this is all

1:53:33

that means

1:53:34

that means

1:53:35

if I have two nested for loops

1:53:39

if I have two nested for loops

1:53:43

then the time complexity will be O of n square.

1:53:47

Can I say that?

1:53:50

If I have two nested for loops,

1:53:53

my time complexity will be o of n square.

1:53:54

Can I say that?

1:53:55

be O of n square on a very high level. Can I say that? Does everyone agree?

1:54:01

Okay. Okay. If I say I have three loops like this for I enlist for J enlist.

1:54:25

for K in list. And list has N elements. How many times these all forloops will run?

1:54:41

N. N. So the time complexity will be O of N Q. Is everyone clear with this?

1:54:55

Now, I would like to also discuss one more thing, which is a very important thing, actually.

1:55:04

Okay?

1:55:05

Assume that this last four loop is running on a fixed number set.

1:55:20

Now tell me, tell me, if this this is the case is the case,

1:55:24

what will happen? The outer four loop will run O of n times. This will run O of n times.

1:55:31

This will run how many times? Any thoughts? This will run how many times? Two times.

1:55:38

That means, with the increase of my N, the K-wala for loop does not have any effect on it. Can I say that?

1:55:46

The increase of n, the decrease of n, the decrease of n, the K loop does not have any effect on that.

1:55:52

So can I say that?

1:55:53

that this is constant? Can I say this is constant? Because even if I increase n to 1

1:56:02

1,000, or if I keep n to 10, it will not matter, at least for this loop. Can I say that?

1:56:08

Guys, how many of you agree with me?

1:56:16

Sublook, everyone agrees with me?

1:56:19

There are how many people, 80, 60,000?

1:56:22

80, 62 people in the chat. Yes, no, tell me. This, this you have to get it cleared.

1:56:29

Right? Definitely, it is quite, repeat.

1:56:33

Manath, do you agree that this loop will iterate over all the elements of the list, the yellow wall?

1:56:42

So if there are 10,000 elements in the list, the yellow walla loop will run for 10, 10,000 elements. Can I say that?

1:56:49

that? Manat? You know? The pink-val loop, how many times it will run? For 10,000

1:56:57

elements again? Correct? But the red-val loop, how many times it will run? Only two times.

1:57:06

Right? Now, if I say that instead of 10,000, I have 10-lack elements in the loop.

1:57:14

The outer loop will run for 10-lack elements.

1:57:18

The middle loop will run for 10 lakh elements, but the last loop will only learn for two elements.

1:57:25

So can I say that the last, the most internal loop has no effect on the size of n?

1:57:33

Can I say that? Has no effect on the size of n?

1:57:37

So when I'm doing a time complexity calculation, it will be n.

1:57:43

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . , which will

1:57:48

be O of n square. Is everyone clear? Is everyone clear with this? Pucka 100%. Does that make

1:58:00

sense? First of all.

1:58:05

Okay. So, now with whatever we have discussed today.

1:58:18

Let's quickly take five minutes to revise all of that.

1:58:22

Okay? From where we started today, can anyone please tell me?

1:58:26

From where we are now, from where we started?

1:58:35

On the search for

1:58:39

nested conditions, right?

1:58:42

Okay, so we nested if conditions, we started.

1:58:46

Okay, then we saw nesting actually.

1:58:47

And then, nesting actually what is?

1:58:49

We had main, we had to know what nesting what is.

1:58:52

Right? That was the main agenda.

1:58:54

So, we had it was the nexting what is.

1:58:56

Then we quickly jumped onto loops.

1:58:59

Then we understood what we can do

1:59:01

loop, and we can nesting how can we?

1:59:03

So we have that we understood.

1:59:05

So we can this one loop in another loop

1:59:08

we can't and then we can one more loop

1:59:11

that means

1:59:13

nesting can.

1:59:15

And its behavior is this behavior is that

1:59:16

that's the internal loop

1:59:19

unless and until that is completed,

1:59:22

the outer loop will keep on run.

1:59:24

Can I say that?

1:59:25

What do you guys think?

1:59:28

Unless and until the internal loop is completed,

1:59:31

the outer loop will keep on running.

1:59:34

And that's where we discovered

1:59:37

discovered something like 2D lists.

1:59:40

Do you remember?

1:59:42

That's where we discovered 2D lists.

1:59:45

list, correct?

1:59:51

So 2D list what would be?

1:59:53

someone will tell you, please?

1:59:55

2D list what is a list within a list is called as a 2D list.

2:0:00

Can I say that?

2:0:01

List within a list is called as a 2D list.

2:0:12

So we've said that

2:0:13

2D list

2:0:14

And 2D list we can iterate

2:0:16

how can we?

2:0:18

Using nested foreloops, right?

2:0:21

Can everyone agree with me?

2:0:24

Okay.

2:0:29

And then we then

2:0:30

then we've then

2:0:32

actually time complexity what is

2:0:35

I'm so sorry

2:0:37

actually time complexity

2:0:38

we learned about that

2:0:40

so we learned about that.

2:0:41

So we can this

2:0:42

that time complexity is basically how much time my code is

2:0:49

taking to execute.

2:0:51

Correct?

2:0:52

That is the time complexity.

2:0:54

Okay, Ash, we have this also

2:0:56

then we've got this

2:0:58

discussed

2:0:59

that

2:1:00

how we can

2:1:02

we can say

2:1:04

we can start pointer

2:1:05

and end pointer

2:1:06

and we'll

2:1:07

start time and time and time

2:1:08

and we'll measure

2:1:09

we'll measure

2:1:10

but that is not helpful.

2:1:11

Why?

2:1:12

Because,

2:1:13

all the laptops

2:1:14

can't

2:1:15

all of all the laptops

2:1:16

can't

2:1:17

for

2:1:18

some

2:1:19

program a little

2:1:20

for

2:1:21

for some

2:1:22

program a little late

2:1:23

but there should be some standardized way.

2:1:24

So that

2:1:25

standardized way is

2:1:26

big O notation.

2:1:27

We've

2:1:28

we said,

2:1:29

we're

2:1:30

finaled

2:1:31

So we

2:1:32

then we then

2:1:33

there are three subcategories,

2:1:34

best case, average

2:1:35

case,

2:1:36

we don't care.

2:1:38

We don't care,

2:1:39

but it's

2:1:40

important,

2:1:41

it's still fine.

2:1:42

But the worst case

2:1:43

whenever software engineers

2:1:44

algorithms

2:1:45

about

2:1:46

always,

2:1:47

always we talk about worst case.

2:1:49

And that is what is most important.

2:1:52

Okay, makes sense.

2:1:53

So we learned about how do we find out

2:1:55

time complexity for looping constructs.

2:1:58

Right?

2:1:59

Does that make sense?

2:2:01

Everyone comfortable till here?

2:2:04

Okay.

2:2:06

So I will just share my screen one more time.

2:2:10

And we will discuss what things

2:2:12

have discussed?

2:2:13

Do you, are you able to see my sheet, the sheet that I've opened?

2:2:17

Can everyone see that?

2:2:19

The sheet that I have opened?

2:2:21

Yes, no.

2:2:24

So,

2:2:25

do we have this

2:2:26

this

2:2:27

Right, nested conditional logic for multi-step decisions?

2:2:30

Have we discussed this today?

2:2:32

Yes, multiple if conditions.

2:2:33

We have discussed it.

2:2:34

Okay, so we will take it up.

2:2:36

Implement nested loops to process 2D data.

2:2:39

Have we learned this?

2:2:41

2D data?

2:2:42

2D arrays.

2:2:43

Have we learned this?

2:2:44

Definitely, yes.

2:2:45

We've discussed this.

2:2:46

Explain best, average and worst case.

2:2:49

This we've discussed.

2:2:50

And then in the last, O of 1, O of N and O of M square patterns in simple code.

2:2:57

Now we have simple code, complex code, not

2:3:00

is that also clear to everyone.

2:3:03

There are only these three types of complex.

2:3:08

Complexities can be multiple types.

2:3:10

O of N cube be

2:3:12

Then there can be some code which can be O of N square

2:3:15

plus there is another loop which is independent of the above two loops.

2:3:19

So it will be O of N2 plus O of N.

2:3:21

WOM.

2:3:22

We're going to go and then the right time comes.

2:3:25

Okay?

2:3:26

But I am pasting a video link

2:3:32

with everyone today.

2:3:35

You guys can go through that once to understand

2:3:38

that time complexity analysis actually if you can

2:3:40

figure out how it? Although we have discussed it, but if you want to actually go into depth,

2:3:45

if you figure out how it, I want to learn it.

2:3:47

Go through that, it is a really nice video.

2:3:50

Just have a look once and we will also discuss it when the right time comes for more complex

2:3:55

code.

2:3:57

So, till here, is everyone comfortable?

2:4:10

100% are we good?

2:4:17

Cool.

2:4:18

Code I have shared the way, please check.

2:4:21

Previous class, I will have to check whether I have it or not.

2:4:24

I'll check and let you.

2:4:25

Okay.

2:4:26

So I'll just hand it over the session to Vijay for if there are any doubts.

2:4:32

Thank you guys.

2:4:33

Have a good night. Happy weekend.

2:4:35

Bye-bye.

2:4:36

Take care.

2:4:37

Thanks, yes.

2:4:38

Bye.

2:4:39

Okay, we can have a quick quiz. Let me share my screen.

2:4:46

Is my screen visible?

2:4:48

Okay, everyone please like do the scan of this code. We will start with the quick quiz.

2:5:03

I will wait for 15 seconds more.

2:5:08

I just do a thumbs up once you will join.

2:5:18

Last five seconds I will wait.

2:5:21

Okay, let's start the quiz.

2:5:33

Yeah.

2:5:36

So you will see.

2:5:37

So you will see the first.

2:5:38

question on your screen answered it fast to gain more points

2:6:02

okay the question was what is a nested condition what not what is a nested loop

2:6:08

So, nested condition will be decided by if and if.

2:6:15

Okay, only nine students have given the correct answer.

2:6:17

So please read the question very carefully before you answer.

2:6:21

Just do a thumbs up like you still have a chance to give the like to be on the top of the leaderboard.

2:6:27

Yeah.

2:6:30

Just do a thumbs up. You will get the next question on the screen.

2:6:38

Okay, next question is on your screen.

2:7:08

be possible via single condition. Maybe it is possible via single if but not with the single condition.

2:7:13

Let's see who is on the top of leaderboard.

2:7:23

Okay. Yes is on the top of leaderboard. Let's move to the next question.

2:7:32

Just do a thumbs up on the on your screen. I will start the next question. Yeah. So

2:7:38

next question is on your screen. This is easy like all of you will be aware about it.

2:7:47

Okay, order open is linear is linear complexity, not constant.

2:8:08

time complexity. Anyways, next, let's see who is on top of leaderboard.

2:8:13

Okay, Art is on top of leaderboard.

2:8:27

Yeah, next question on your screen.

2:8:38

which among that like following is fastest for like fastest time complexity

2:8:47

order of one square is not fastest I like that will take a lot of time

2:8:57

time order of one that is fastest

2:9:01

today like a lot of students I don't know like please read the question first and then

2:9:06

like try to answer

2:9:08

Okay, now I use it on the top of little code.

2:9:13

Final question.

2:9:38

Okay, fine, let's see who's like at the top.

2:9:45

Okay, so Iyush is the winner, Nish was the second winner. Yeah.

2:10:01

Yeah, so that's it for today. I will launch a quick feedback poll.

2:10:07

Just provide a feedback and then maybe you can drop off.

2:10:24

Please provide the feedback and then we are done for today.

2:10:28

Feel free to drop off once you will provide the feedback.

2:10:37

Okay, 10 students remaining, please provide the feedback.

2:10:54

5 students remaining./