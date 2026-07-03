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

Okay. Hello, hi everyone. Good evening.

16:54

I hope everyone is doing fine.

17:00

Good to hear about it.

17:02

Cool. So welcome to today's session.

17:06

Just one thing to note for everyone is

17:10

the title of the class may be misleading.

17:14

We are not going to work on the Python installation and all of that part.

17:19

We are going to instead, you know, learn about functions in Python.

17:23

and the agenda is basically how do you create functions in Python?

17:28

How do you modular programming in Python?

17:31

What are arguments?

17:33

What are different types of functions?

17:35

That's the agenda.

17:37

So if you see a different title as part on your LMS,

17:42

please ignore that for now, okay?

17:45

By the way, what is the title that you guys are seeing on LMS?

17:51

Can you please share that?

17:52

share that?

17:53

What is the title that you guys are?

18:03

Python installation?

18:04

Yeah.

18:05

So I believe that, you know, the title is a little bit wrong there.

18:13

So please ignore that for now, okay?

18:17

The team will fix it later.

18:20

So we will not discuss about VS code set up Python installation because that is something that I believe everyone should be able to do it by yourself.

18:27

Okay?

18:28

We will discuss about the main thing which is functions.

18:31

Cool. So anyways, let's start with the session.

18:36

What did we learn in the previous session?

18:50

Anyone would like to answer that question?

18:55

Yeah, we learned about nested conditions.

18:58

Okay, and what are nested conditions?

19:07

Basically one condition inside another condition.

19:14

Am I correct?

19:16

This is called nesting.

19:18

Now this nesting.

19:19

nesting can happen with this nesting can happen with your conditions as well.

19:29

And this nesting can happen with your looping construct as well.

19:34

Am I correct?

19:36

Does everyone agree with me on that?

19:39

Yeah.

19:40

Okay.

19:42

When it happens inside a loop, what happens?

19:47

For example, if I write a loop inside a loop,

19:49

what happens? The internal loop, the inner loop, runs completely for every iteration of the outer loop. Can I say that? Right?

20:07

That means if the outer loop is running for n times and the inner loop is running for m times, then the total number of iterations will be n into m.

20:19

This is something that we learned in the previous session.

20:23

And then we also discussed about time complexities.

20:25

We discussed how do you find out the time complexities for, we discussed how do you find out time complexities

20:32

for nested loops and for basic, basic code cases.

20:39

This is something that we had discussed in the previous session, right?

20:45

so warmup done.

20:46

Now today, let's start with functions.

20:52

Okay.

20:53

So let me create a heading.

20:58

Okay.

21:03

Now, the thing is, imagine that let me create a heading.

21:14

And then we'll understand functions by some analogical example.

21:15

we'll go and check out the syntax of it and see the actual use case. Okay.

21:23

So, assume that you're making a tea and you every day you wake up in the morning and you make tea.

21:30

You know how to make tea. Okay. So the thing here is, do you have to learn every time that

21:38

you have to boil the water? Do you have to learn how to do that? No, you had to learn it for the very

21:45

first time. And once you knew, once you know, once you learnt about it, then you just basically

21:51

follow the routine. It is the very basic thing, right? Because we learnt it. So the thing here is

21:57

now you know that boiling water, how to boil water. So you do not have to actually see the recipe of

22:04

it and go through the recipe. So instantly you go, wake up, boil the water, make the tea. So

22:11

boiling water is a reusable thing every day for you. Can I say that? It is something common

22:18

which is part and piece and part of the recipe for making tea. Boiling the water. Can I say

22:24

that? That every day you have to boil the water. The same thing is happening every day.

22:30

Okay? That reusable thing is called as a function. Okay? So anything, any piece of

22:41

code that you write. If you feel that yash, maybe I can reuse this piece of code.

22:50

What you do, you create a separate specific code block for that and that code block is called

22:57

as a function. How do you define that code block? We will do that. Why are we so much stressed about,

23:04

you know, repeating the code and don't repeat the code? So there is a principle called dry.

23:11

DRY. And it states that don't repeat yourself.

23:18

So as a software engineer, we generally follow this principle that we try to maintain the guideline that we should ideally never repeat ourselves.

23:38

Okay. So for a moment, let's try to see that, okay, this is my main.

23:50

And I write here print, hello, and the input. Or for example, for a moment, let's forget about this.

24:07

about this, I write hello yes. Okay. Now the thing is, if I want to do this print

24:17

statement, if I want to run this print statement multiple times, essentially, am I copy pasting

24:27

here? Essentially, am I copy pasting the code here? Essentially, am I copy pasting the code here?

24:37

What do you guys think? Yes? So the thing is, now assume that if there are 100 people in the class,

24:47

assume that I have to say hello to each and every one of you. If there are 100 people in the class,

24:52

I will have to write this print statement 100 times. Am I correct?

24:59

Right? Yes. One solution is that, okay, yes, why are we discussing all of this? We can actually use a loop and print it. That is one way to do it.

25:07

you can apply a four loop and then do it okay actually what you can do is but if you see

25:16

even if you apply a loop this name will always change so this hundred lines will actually never go away

25:27

from the code maybe it can go away if you take the input from the customer and input from the

25:33

user and then do it okay but what I can do here is I can actually

25:37

actually do one thing that whatever is this piece of code. I can say that this piece of code

25:45

has a single responsibility that I want to print hello world to the specific user. So what

25:52

I will do? I will create a specific function in my Python code which is responsible

26:01

for greeting the user, hello world. So what I will do? I will

26:07

create a function called as greet user okay and I will pass here the name of the user for example or as

26:23

now I will not pass anything I will do something like this and whatever I write in this function

26:37

whatever I write in this function is scoped to this specific function only.

26:50

That means if I want to use this specific code block, if I want to call this code block, I will have to call this function.

27:00

How do I call this function? We will see it. How do you call this? From your actual code, what you will do you do?

27:07

you will just write greet underscore user and these brackets.

27:16

Okay. Now this is how you define the function.

27:25

This is the definition of the function and this is the definition of the function and this is the declaration of the function.

27:37

Is that clear to everyone?

27:42

Everyone comfortable?

27:45

Okay.

27:46

Abhishek, what is not clear?

27:52

Any specific thing?

27:54

Please repeat.

27:55

So Abhishek what you will do is you will create a specific code block.

28:00

Okay?

28:01

A very specific code block which is responsible just for greeting the user.

28:05

What is the responsibility of that code block?

28:06

of that code block, just greet the user.

28:10

So if I want to trigger that code block, whatever code is written in this code block, if I want to trigger this.

28:17

How do I trigger this?

28:19

I will have to write this piece of code in my editor.

28:24

Okay, we will see the complete code of it.

28:27

I am just telling you that this is the functionality.

28:30

This is the use case of a function.

28:32

Okay.

28:33

Now what is the syntax?

28:35

How do you define the function?

28:36

we will see that. Make sense?

28:40

Okay.

28:42

Sanukti, it is already high.

28:45

I think, can you increase your volume?

28:47

Is my voice audible to everyone clearly?

28:50

Yeah, no?

28:54

Seniqa just check, there's some problem maybe on your side.

28:57

Okay?

28:58

Okay.

28:59

Okay.

29:00

Now, actually I wrote, if you see this function here,

29:03

there are some new new things that yes, you have you have some new things that yes, you have

29:06

written here.

29:07

First of all, there is something called as DEF that you have written.

29:10

Then there is something this.

29:12

Then there is something this brackets.

29:14

What do you mean by all of this?

29:16

We will discuss one by one.

29:18

What do you mean by DEF?

29:21

DEF means DEF is a keyword in Python.

29:24

It means that we are telling to Python that I am defining a function.

29:29

Okay.

29:31

It means that whatever is now I am doing, I am defining a function here.

29:44

Greed.

29:46

What is this?

29:50

This is the name of the function.

29:59

or alias.

30:03

Okay, everyone knows what alias is naming.

30:07

For example, my name is Yash.

30:09

Your name is Nandkeesh.

30:11

Someone's name is Shalini.

30:13

Same.

30:14

We have to give a name to a specific function.

30:17

Then what do you mean by this?

30:19

This means that parenthesis.

30:22

After the function name, it is part of the syntax that you have to use the parenthesis.

30:28

Okay?

30:29

Is that clear to everyone?

30:36

Followed by a column? Absolutely, yes.

30:41

So if you see here, this is a column, very much similar to if.

30:46

After if also we add a column.

30:49

And this should be the indented code, right?

30:54

A little bit inside.

30:56

So now the thing is,

30:58

The thing is, yes, you discussed about naming a function.

31:02

Now, how do we decide that what name I should give to my function?

31:07

Like, how do you decide that?

31:10

No, no, no, I am defining it.

31:12

We are the one who will define it.

31:14

Okay?

31:15

So how do you define an actual function?

31:17

Def, this is something that you will write in your code.

31:20

Def, greet user.

31:27

Print.

31:32

Hello world.

31:35

Okay. Now how do you call this function?

31:42

How do you call this function?

31:44

You, after this is your code file.

31:48

Okay, once you have defined all of this, then you will just call greet user.

31:56

As simple as that.

31:58

Okay.

31:59

Greet user is not fixed.

32:01

You can give any name to the function.

32:04

Is everyone clear with that?

32:06

Okay.

32:07

So there can be one thing about functions that can come to you that yes, what should I name my function?

32:14

Like should I name my function anything?

32:17

Should I always name my function as greet user?

32:20

No.

32:21

Okay?

32:22

The function name, there are no conventions for function.

32:25

for function name, but there are some guidelines.

32:29

Okay?

32:30

That the function name should be, like the function should be named after what it is doing.

32:37

For example, if I am adding two numbers, so the function name can be add.

32:42

If I am multiplying two numbers, then the function name can be multiply.

32:46

If I am printing something, then the function name can be print something.

32:51

Does that make sense?

32:53

If I am sending an email.

32:54

If I am sending an email, so the function name can be send email.

32:58

Everyone comfortable?

33:02

Okay, so let's actually go in the code and see how do you define a very first function of Python.

33:11

Okay, so I'll just go back to my code screen.

33:16

Okay, everyone is able to see my code screen.

33:20

Okay?

33:22

Now, print hello world.

33:23

Print hello world in fact is also a function in Python.

33:28

But this function is a predefined function, like it is available in Python itself.

33:34

So Python knows about it.

33:36

But now, if I come here and if I tell greet underscore user, and if I run the code,

33:45

my Python will give me an error.

33:48

Why? Because it will tell that, okay, what do you mean by greet user?

33:51

I don't know what great user is.

33:52

is?

33:53

Everyone agrees with me?

33:54

I am calling a function which Python is not aware about.

34:00

Is everyone comfortable?

34:02

Okay.

34:03

So how do you define a function?

34:06

Before you call the function, in Python the function should be defined above the calling line.

34:12

Okay, so if you are calling the function on line number six, the definition of the function

34:18

should be above line number six.

34:20

So how do you do?

34:21

Def, greet user, this, and here you write print hello world.

34:33

Okay, is everyone comfortable?

34:35

Now if I run this code, see, it prints hello world and if I do some edit here from function.

34:45

If I run this, hello world from function.

34:49

So essentially what is happening is happening is,

34:51

whenever you run the code, what happens?

34:56

This piece of code, Python will go through it.

34:59

Okay, Python will understand that, okay, you have defined some function.

35:03

Till line number four, have you called that function?

35:07

Till line number four, have you called that function?

35:10

No.

35:11

On line number five, Python will come and see that, oh, you are calling a function which you have defined above.

35:17

So from here, the code pointer will go to line number one.

35:20

go to line number one, it will execute the function completely, and then once it is completed,

35:27

then it will continue from the next line.

35:31

Is that clear? So if I run the code, see, hello, from function, continue from here.

35:40

So at line number 5, the code pointer goes to the function and whatever code you have written inside the function will get executed.

35:49

will get executed. Once the complete function is completed, like the execution is completed,

35:56

then the code pointer resumes from the very next line.

36:00

Is everyone comfortable with this?

36:03

Any questions?

36:11

No, it is not similar to list. List is a data structure.

36:14

Function is a behavior in Python.

36:17

Okay?

36:19

Gautam, it is 80% 90% English and rest 10% is Hindi.

36:27

Okay?

36:29

Now, kya, I can just print anything in the function?

36:35

No, you can do anything that you want.

36:38

For example, if you want to add two numbers,

36:40

then you'll what you'll do?

36:42

A equals to 10, B equals to 15,

36:46

c

36:47

equals to 10 plus A plus B.

36:50

And what you can do is you can print this as well.

36:53

So the thing is, if you run this code,

36:56

whatever code, whatever code you've

36:58

in the function in the function in there

37:00

will execute.

37:03

Yeah, after your function is executed,

37:07

a 1-1-1-complete-complete-go-gia,

37:09

then the next line run will-he-he-he-he-he-he-he-he-he.

37:12

Okay?

37:14

Without calling the function also, we can do the work.

37:16

we can do the work. So what is the benefit of calling function?

37:19

Assume that, Sanyukta,

37:22

I'm going to this piece of code

37:25

by-bar call with different values.

37:29

So I what I'll do?

37:31

Instead of copy-pasting all of this code again and again,

37:35

I'll what I will,

37:36

I will define it one by and I'll

37:39

use it and I will use it again.

37:41

So I will define it one time

37:43

and I will keep on reusing this code block.

37:45

this code block. Does that make sense?

37:50

Okay?

37:51

For example, let us take a better example to understand the use case of function.

37:56

Okay?

37:57

Def, take...

38:00

Actually, we will wait for 10 more minutes

38:03

and then the example that I'm going to take will make more sense to you.

38:06

But till now, everyone comfortable?

38:10

Yes,

38:14

you can use you. For example,

38:16

for example, let's take one more example.

38:19

If, add two numbers by taking input.

38:25

Okay? I defined this function, what I will do.

38:29

A equals to int input, enter A.

38:34

B equals to int input, enter B.

38:37

Enter B equals to int input, enter B.

38:41

C equals to A plus B.

38:43

to A plus B.

38:44

Print sum is C.

38:52

Now, I have to run this piece of code two times.

38:57

What I will do?

38:59

I will just call this function two times from my code.

39:03

That's it.

39:04

It is that simple.

39:07

One bar I'm here from here

39:10

and second time I will call it from here.

39:12

I will call it from here.

39:14

Is everyone clear?

39:15

So, now if I'm this run it,

39:17

then what will?

39:18

This is the first one.

39:19

Let's run the code.

39:21

Enter A.

39:22

A is 1.

39:23

Enter B.

39:24

B is 2.

39:26

So sum is 3.

39:27

That means this whole function

39:29

a one execute here.

39:31

Then I've moved on to line number 10.

39:34

So line number 10 again called the same function.

39:37

It is asking me enter A.

39:39

I will tell 3.

39:41

4.

39:42

It will still sum is 7.

39:44

Now this line,

39:46

the line number 10 is executed completely.

39:49

Do I have anything else on line number 11?

39:52

No.

39:55

That means, here my program over

39:58

does that make sense to everyone?

40:01

Does that make sense to everyone?

40:05

Now, if I want to do the same thing 10 times,

40:10

how would you do it?

40:11

If I want to do the same thing 10 times,

40:22

very simple yes, this you have

40:23

for I in range 10,

40:27

call the function from here.

40:31

As simple as that.

40:33

Am I correct?

40:34

Right?

40:38

So if I'm to do to do

40:40

So it's two times call

40:41

that means enter the value of A1,

40:43

enter the value of B2,

40:44

sum is 3,

40:45

enter the value of A4,

40:48

value of B5,

40:49

sum is 9

40:50

then the code over.

40:52

Everyone comfortable?

40:54

So, how I have saved myself,

40:57

this this,

40:59

instead of duplicating that code,

41:01

I made it one place

41:03

and I am calling that again and again.

41:06

Can you all of

41:07

understand?

41:10

Okay, everyone comfortable?

41:15

Any questions till now?

41:20

Okay.

41:21

So, we now, now,

41:26

now, now,

41:27

next thing up on the next thing is,

41:30

basically,

41:31

basically,

41:32

what we've seen,

41:33

what we've seen,

41:35

whatever function you have defined,

41:38

in this,

41:39

In this parenthesis, we are not taking any input.

41:45

That means this function is it does not take any input.

41:49

But will it always happen that this function will not take any input?

41:54

Like it is taking input from the user here, but this function is not taking any input from the code.

42:01

So will this happen that I do not have to pass any value?

42:04

Will this have, will this going to ever happen?

42:09

Everyone?

42:11

No.

42:12

Khabi or it will have to pass some value for here.

42:15

For example, if I say that I want to pass the value of I here.

42:21

For example, I say, I want to pass the value of I here.

42:26

So how you will do it?

42:27

For that, there is something called as parameters in function.

42:32

Parameters and arguments in function.

42:35

So what is it means?

42:37

That means whatever is the value of I,

42:41

if you have to your function in a value pass

42:44

then how do you?

42:46

Just pass the value here as it is.

42:49

So if you pass here I,

42:51

now what will?

42:53

If I run the code,

42:55

my code will actually throw me an error.

42:58

Okay?

42:59

The problem here is that you are telling

43:03

I am passing a value I to the function.

43:06

But this function says that, okay, what Python will do?

43:11

Python will try to find this function in the code.

43:14

That, okay, is there any function which has this name and is taking a parameter?

43:19

It will say that, oh, no, there is no function.

43:22

There is a function with the name, but that function does not take any parameter.

43:26

So that is the reason it is taking that, it is taking zero arguments.

43:30

That means there is no argument defined in the function.

43:34

So how do I fix it?

43:35

So how do I fix it?

43:38

If I want to fix it, how do I fix it?

43:40

I can just write here that number.

43:43

This number is going to be the argument.

43:47

So if I run the code now, my code will compile completely.

43:51

Does that make sense?

43:55

Does that make sense?

43:57

So what is I here?

43:58

Now if I print, print, argument, argument, parameter, pass.

44:05

number. If I run this code, see, parampassed is 0. And what was 0?

44:16

0?

44:17

This was the value of 0. So if I enter 1, if I enter 2, the sum is 3, next time in the 4 row, I becomes 1.

44:27

This 1 as a value is passed to this function, or that is the reason it is printing here, parampast 1.

44:34

Does that make sense?

44:41

Any questions on this?

44:45

Now, yes, I have one more question.

44:49

That you have passed only a single parameter now,

44:56

can I pass multiple parameters?

45:01

Definitely you can pass multiple parameters?

45:03

So what you can do? You can pass, for example, if you want to pass here 10, you can pass 10.

45:11

And if you want to run this code, it will give you an error. Can anyone tell me what is a problem here in the code?

45:19

Can anyone please tell me what is the problem in the code?

45:23

Like why I am getting this error? Any thoughts? Any guesses?

45:27

Yeah, the problem is that when you are calling the function,

45:33

you are sending two parameters. But when you are defining the function, you have not defined the second parameter.

45:43

So I will name it as number 1 and number 2.

45:47

Now if I run the code, what is the problem? Okay.

45:53

So now what is the problem? Can anyone please go through the error and tell me that what is the problem here?

46:03

Why I am getting this error? Any thoughts?

46:08

So the thing is, there is no variable called as number in the function. Does everyone agree?

46:18

Do I have a variable called as number in the function?

46:22

Do I have variable called as number in the function? There is no variable called number.

46:28

Number one is there, but number is not there. So if I run this code, now it runs.

46:32

Now it runs. Okay. Now, if I do not pass 10 here, what is going to happen?

46:41

If I do not pass the second parameter here, what is going to happen?

46:47

Any thoughts?

46:55

So the thing is, when you have defined a thing from the point of view of the point of view of

47:02

of compiler.

47:04

Okay?

47:05

Compiler will read this function.

47:07

It will say that, okay, add two numbers.

47:09

It is taking two parameters. Fine.

47:11

Compiler will come here. It will run the loop.

47:14

It will check that, okay, there's this line.

47:18

And I'm passing a single parameter here.

47:21

So now, compiler will try to find a function with a single parameter.

47:27

Will my compiler get that function? What do you guys think?

47:31

Will my compiler get a function with a single parameter value?

47:41

No.

47:42

My compiler will not get it.

47:44

Hence, it will throw an error.

47:48

It will tell that you are passing two parameters.

47:52

Deweil, it is already zoomed out.

47:55

It is better now, the way?

48:00

Okay.

48:01

So what it is telling here is that you are missing one positional argument.

48:08

That means, you are passing only a single value, but ideally it should be two values out there.

48:15

Okay, all of the problem?

48:18

Is everyone comfortable with this?

48:22

Okay, 100%?

48:24

Now tell me one more thing.

48:26

If I pass I comma I, what do you think?

48:30

do you think? Will it work? If I pass I comma I, will it work? Definitely it will work.

48:38

Definitely it will work. Why? Because this is number one, there is one parameter and this is number two, which is second parameter.

48:45

So in the first iteration, it will pass 0, 0 and in the second iteration, it will pass 1.1.

48:53

Does that make sense?

48:59

Everyone comfortable?

49:01

So this is how you define functions in Python.

49:05

Now let me come back to my code screen, sorry, iPad screen.

49:10

I hope everyone is able to see my iPad screen.

49:15

So what we have learned now that it can be any data type element.

49:22

What we have learned now is that this is your main function in Python.

49:28

Everyone knows that whatever code you are writing, there is always a default function called as main in Python.

49:37

Whatever code you are writing, even though you do not define a function by yourself,

49:45

there is always a main function in Python, always, and that is created by Python.

49:50

Either you have to create it or Python will create it for you.

49:54

If we use online compiler, Python creates that main function for you, direct.

49:57

function for you directly.

49:59

Okay.

50:00

Now, so how the code flow works, that from this main function, first of all, I will run some code in my main function.

50:12

Then from my main function, I will call another function, which is grid.

50:25

Okay. Now this code of grid function will execute completely.

50:29

And this grid function will return back the execution to the main function.

50:35

And from next line onwards, the main function will start executing again.

50:40

This is how it will work.

50:42

What do you all?

50:44

This is how it will work?

50:47

Everyone.

50:48

Now from this, can I call any another function again?

50:54

Like add to you?

50:55

two numbers, what do you guys think?

50:57

Can I call any other function?

51:05

Absolutely.

51:06

I can call any another function from here as well.

51:09

Okay, yes.

51:10

So, line number one, line number two, this is line number three.

51:15

So at line number three, the execution will go to greet function.

51:19

Greed function will execute all the code.

51:21

It will come to line number four, line number five.

51:24

Line number five.

51:25

six, the execution will go to the green function.

51:29

The green function will execute.

51:31

Line number seven, line number eight, line number nine.

51:35

All of this will execute.

51:37

Is this clear?

51:39

Is everyone comfortable?

51:42

Now, there is one more thing out there.

51:45

Can I do?

51:48

Like this is L1, this is L2, this is L2, this is L2, this is L2.

51:54

This is L2.

51:55

3. From L1, from L3 in this five function, can I call any another function from here?

52:02

What do you I think? Is this allowed? So basically that means you can call any

52:20

function if you have defined that in the same file. If you have defined that in the same file, if you have

52:25

want to call a function of any another file, then you will have to import that file,

52:30

and then call the function. Make sense? Is everyone comfortable? Okay? This flow,

52:41

where we are passing execution from one function to another function to another function.

52:47

So eventually what will happen? This will be called. This will return the execution state.

52:52

Line number four will be called. And after line number four,

52:55

I will return back to this function. Am I correct? Everyone?

53:02

So this is how function execution works.

53:08

That you can call one function from another function and one function inside another function as well.

53:14

Okay? So this nesting can go to any level.

53:18

There is no limit for that.

53:21

Okay.

53:25

Does that make sense?

53:29

Okay. Now I wanted to discuss one more thing.

53:33

Before we go on to the next part of the session.

53:39

Just one second, I'm just checking.

53:44

Okay, I wanted to discuss one more thing.

53:48

Now, as of now, I have defined a function add two numbers.

53:54

And I am taking argument A. I am taking argument B. Okay? What I am doing here?

54:08

A plus B equals to C and print C.

54:17

Correct?

54:21

Everyone?

54:23

Now, how I will call this function?

54:32

Add two numbers.

54:37

9 comma 9.

54:41

If I call this function, deaf I will have to use.

54:44

Okay?

54:46

If I call this function via this flow, what will be the output?

54:50

Can anyone please?

54:51

Like what will be the printed output?

54:52

printed output?

54:56

80.

54:58

Okay.

55:00

If I call this function with this, what will happen?

55:14

Error.

55:19

Why error?

55:20

Because the function is expecting two parameters.

55:21

two parameters and you are passing only one. But in case I don't want to error out.

55:30

I want to set a default value for this. What if? I want to set a default value.

55:36

That if the user is passing the value, honor that value. If the user is not passing the value, then use the default value.

55:49

What do you guys think?

55:50

I think? Is everyone comfortable with my thought process? That what I want to

55:57

do, I want to set a default value of the function argument. That if a user is sending the value,

56:04

honor that value. Awesome. If the user is not sending the value, don't error out. Instead, use

56:11

a default value. So how do we do that in Python?

56:15

Very simple. What you do?

56:20

Copy, paste. Here what you do? For whatever argument, for whatever argument you want to set the default value, you will do equals to 10.

56:37

Or, sorry, equals to 0. Now if you set it equals to 0, what is going to happen?

56:47

Now when you call, add 2 number.

56:49

add two numbers. Now when you call add two numbers, what is going to be the output?

57:02

A becomes 10, B becomes 0, C becomes 10. Does everyone agree? So output will be 10?

57:14

10. Okay, hey, good.

57:16

If I pass add two numbers, 10 comma 10.

57:24

What will be the output? A becomes 10. B, now the value has passed.

57:32

So B will take the value of 10. C will become 20.

57:37

Okay? So if the value is passed, then we will honor it.

57:42

If the value is not passed, then we will use the default.

57:46

Does that make sense to everyone?

57:50

Can you all of them?

57:55

Okay.

58:01

Now, that means can you set default values for all the parameters in the function?

58:07

Like this is a parameter, this is a parameter.

58:09

Can you set default values for all the parameters?

58:13

Yes, you can set.

58:14

So if I want to set the default value,

58:16

of A also. What I will do?

58:23

Copy, paste, A equals to 0, whatever value I want to set.

58:36

If I want to set a default value of 10, I can set the default value of 10.

58:40

So it is up to completely up to me.

58:42

And B equals to 0.

58:45

Now,

58:46

If a user calls add two numbers with no arguments,

58:54

will my code still work?

58:58

Will my code still work?

59:02

It will still work and the output will be 0

59:06

because now my function expects 0 arguments.

59:10

Even if you are passing 0, I will work with that.

59:15

Does that make sense?

59:16

So let's see this actually in the action and let's understand what is happening there.

59:29

Okay, are you able to see my code screen?

59:35

Just a minute I am getting a phone call.

59:46

One minute guys, huh?

1:0:03

Yeah.

1:0:05

Okay.

1:0:07

Now let me, now tell me one more thing.

1:0:13

If I have defined this function and

1:0:16

If I never call it, for example, if I just do print hello,

1:0:22

will the above function be ever used if I just define the function and never call it?

1:0:28

Will this piece of code be ever used?

1:0:31

No.

1:0:32

In order to use this piece of code, I definitely will have to define it.

1:0:37

I definitely will have to call it.

1:0:40

It is very much similar that there is some person in the room but I never call that person.

1:0:45

call that person.

1:0:47

But is the reverse also true?

1:0:49

As in, I call that function, I call a function but that function does not exist.

1:0:54

Is that reverse true?

1:0:56

In that case, I will get an error.

1:0:59

If I am calling a function, that function should exist.

1:1:03

Does that make sense?

1:1:05

Everyone compatible?

1:1:10

For example, if I comment this function, will my code still work?

1:1:15

If I run this code, now it will not work.

1:1:19

It will tell that, oh, you are calling a person, but that person don't exist.

1:1:24

Okay?

1:1:25

Everyone comfortable?

1:1:28

Okay.

1:1:29

So for now, I will just keep this function.

1:1:32

I will never call this.

1:1:34

So that it does not get printed.

1:1:36

I am fine with that.

1:1:38

Now let me define another function.

1:1:40

Def, add number,

1:1:44

you with default.

1:1:51

What I will do?

1:1:52

A equal to 0, B equal to 0, C equal to 1.

1:1:56

Okay?

1:1:58

Now what I will do?

1:2:00

D equal to A plus B into C.

1:2:05

Can I do this? What do you guys think?

1:2:08

A plus B into C.

1:2:11

Right?

1:2:12

Everyone?

1:2:13

Okay?

1:2:15

What I will do?

1:2:16

Print

1:2:17

Output

1:2:19

D.

1:2:21

Okay.

1:2:23

Now if I want to call this function

1:2:26

Now if I want to call this function,

1:2:29

add number with default

1:2:31

1 comma 1 comma 2.

1:2:33

What will be the output?

1:2:38

Now if I want to call this function, what will be the output?

1:2:43

What will be the value of?

1:2:47

Let's try to print nc.

1:2:48

Okay?

1:2:50

Print A.

1:2:52

P

1:2:57

C.

1:3:02

Okay?

1:3:03

Run the good.

1:3:08

Now I had passed 1.1.1.2 and the value is exactly on it.

1:3:12

exactly on it. Okay.

1:3:14

If I don't pass this, what will be the output?

1:3:19

What will be the output?

1:3:21

2. How to?

1:3:25

Because it is C is 1.

1:3:28

C.

1:3:29

A1, B1, C1, but yes, you did not pass C.

1:3:34

Why?

1:3:36

C is coming as 1?

1:3:38

Because the default value of C is 1.

1:3:41

Does that make?

1:3:42

sense? Can I do something like this?

1:3:46

Okay. Now, can I do something like this?

1:4:00

If I just pass 1, what will happen?

1:4:03

1 plus 0 into 1.

1:4:08

Okay.

1:4:10

Yes, if I don't want to pass 1.

1:4:11

If I don't want to pass the value of B, is that possible?

1:4:17

Is this possible?

1:4:20

Let's try to see.

1:4:23

This will give you an error.

1:4:26

Why?

1:4:27

Because you have literally passed nothing here.

1:4:30

Okay?

1:4:31

So in the break, I am going to give this question to you.

1:4:35

Why error?

1:4:36

Because Himanchu, your Python gets confused that,

1:4:40

dude, what do you want to?

1:4:41

want to do? Do you want to like why there is a semicolon here?

1:4:45

So Python gets confused.

1:4:47

That do you, it is like, it is something like that you don't want to pass the value?

1:4:51

Or it is a typo.

1:4:52

So there is an ambiguity and whenever there is an ambiguity,

1:4:55

the compiler will give you an error.

1:4:58

Make sense?

1:5:11

Everyone clear?

1:5:26

Okay.

1:5:27

Okay.

1:5:28

Okay.

1:5:38

Yes.

1:5:39

But what if?

1:5:40

Yes.

1:5:41

but what if I don't want to pass the value of B?

1:5:44

How I will, like how do I do that?

1:5:46

I don't want to pass the value of B.

1:5:48

So how can't do you explicitly will have to call it out.

1:5:54

That A equals to 1 comma c equals to 2.

1:6:02

This way your Python will know that okay you do not want to pass the value of B.

1:6:10

Okay, so if I run this code now, now it will tell me a proper output that, okay, B was 0.

1:6:15

Can you all you have?

1:6:17

So, unless and until you specify, your Python will not understand.

1:6:26

Everyone clear?

1:6:28

Let me take one more example.

1:6:30

Assume that I have this function.

1:6:33

Okay?

1:6:35

Where I have defined parameter 1, parameter 2, parameter 3.

1:6:40

And if I want to call this function, so what I will do?

1:6:44

I have this code written.

1:6:47

I will call this function using my function, parameter 1, parameter 3.

1:6:51

What will be the output?

1:6:52

Can anyone please tell me?

1:6:54

What will be the output here?

1:6:57

Parameter 2 will get a default value of banana.

1:7:00

Can I say that?

1:7:02

Parameter 2 will get a default value of banana.

1:7:05

Can I say that?

1:7:06

If I run this code, watermelon, banana,

1:7:09

banana.

1:7:10

mango. Everyone comfortable?

1:7:18

Take it?

1:7:19

So this is on the basics of functions.

1:7:22

Okay.

1:7:23

Now, what I will do is let's go, let's take a break for 8 to 9 minutes.

1:7:28

Please repeat.

1:7:29

Prashant, what do you want me to repeat?

1:7:31

We have just discussed the same thing Prashant

1:7:35

with a different example.

1:7:37

Here, I have passed parameter one.

1:7:39

and parameter 3, I have not passed the value of parameter 2.

1:7:44

And parameter 2 had a default value for banana.

1:7:48

So if I call this function,

1:7:50

the default value of parameter 2 will be banana.

1:7:54

And that's what it is printing here.

1:7:56

Make sense.

1:7:59

F is just formatting, like if you want to format the output

1:8:02

for that purpose you mentioned.

1:8:04

Okay, for example, first argument is Param 1,

1:8:07

second argument is Param 2,

1:8:09

So if you want to just print it in some beautified way, for that you use F.

1:8:14

Okay?

1:8:16

Is everyone comfortable?

1:8:23

Okay?

1:8:24

Awesome.

1:8:25

Let's take a break for 8 to 9 minutes.

1:8:27

In the meantime, I will request each and every one of you

1:8:29

to please create some functions, try out some things.

1:8:34

And if there are any questions, we will discuss after the break.

1:8:37

If we pass parameter to,

1:8:38

If you pass parameter 2 and 3,

1:8:40

if you pass parameter 2 and 3,

1:8:44

then the output will be apple watermelon mango.

1:8:48

Apple watermelon mango.

1:8:51

Why Apple?

1:8:52

Because the default value of parameter 1 was Apple Rajty.

1:8:55

Does that answer your question?

1:9:02

Okay guys, let's come back by 908 p.m. 909.

1:9:07

8 p.m. 9.m. Let's take a break for 8 minutes. And from that, we'll resume how do you return values from our function.

1:9:37

Thank you.

1:9:39

Thank you.

1:10:09

Thank you.

1:10:39

Thank you

1:11:09

Thank you

1:11:39

Thank you

1:12:09

Thank you

1:12:39

Thank you

1:13:09

Thank you

1:13:39

I'm

1:13:41

I'm

1:13:43

I'm

1:13:45

Thank you.

1:14:15

Thank you.

1:14:45

Thank you.

1:15:15

Thank you.

1:15:45

Thank you.

1:16:15

Thank you.

1:16:45

Thank you.

1:17:15

Thank you.

1:17:45

Thank you

1:18:15

Thank you

1:18:45

Thank you

1:18:47

Thank you

1:18:49

Thank you

1:18:51

Thank you

1:18:53

Thank you

1:18:55

Thank you

1:18:57

Thank you

1:18:59

Thank you

1:19:01

Thank you

1:19:03

Thank you.

1:19:33

okay uh everyone are we back

1:20:03

hello hello yeah nice cool okay so uh now let's discuss the remaining two topics for

1:20:16

the day uh sorry what happened yeah so what's our topic here next huh okay

1:20:33

Now the last thing second last thing that I wanted to discuss today is returning

1:20:38

value from a function. So till now you can you can

1:21:03

discuss that in the doubt session saddick okay uh now for what i wanted to discuss is

1:21:11

returning value from function okay now whatever functions we have returned till now

1:21:18

did they returned any values for example this function did this function

1:21:25

did this function returned any value when i say return any value i mean to say

1:21:33

that this was the call stack this was the main function and from main i called this function called

1:21:43

as add two numbers correct now as soon as this specific function got executed the control

1:21:56

came back here and we resumed the code from here am i correct we resumed the code from

1:22:03

here okay but this main function it passed some value for example we pass 10 we pass 0 we pass 2 we can pass any value to the function

1:22:15

as of now this function did not return back any value to the caller function correct whatever we were

1:22:23

doing we were just printing the value inside this function am i right with that am i right with that

1:22:31

but is that always going to be the case that okay i will pass some value but i don't

1:22:38

expect anything from the function is that always going to be the case no okay main means outside the

1:22:46

function yes alvin main means outside the function okay so the thing is whenever we call a function

1:22:53

most of the times we expect the function to return the value back to us for example

1:23:01

what can be one use case yes assume that i want to add two numbers so what i will do i will define a function

1:23:09

diff add number a comma b a plus b equals to c now i am calling this function add number two common four okay now if i want

1:23:31

i want to print if i want to work on this function for example this is my editor i am writing

1:23:37

all of the code here okay now the thing is as of now this function call specifically redirects from

1:23:48

here to here am i correct this function call specifically redirects the code pointer from here to

1:23:55

there tk ehs boh badi the code pointer runs this function and here and here

1:24:01

once the function is executed this line is will be executed but as an output of this line

1:24:13

can i say c equals to or can i say sum equals to add number 2.4 if i do that right now

1:24:24

am i going to get any value in sum?

1:24:28

am i going to get any value in sum if i do that right now no why because the add number

1:24:37

function as of now does not return anything am i correct it is calculating the sum of two numbers

1:24:44

but it is not returning anything back to me is that clear right so if i want for example if i want to

1:24:56

do here some other calculation sum into sum plus 1 by 2 if i want to do something like

1:25:11

this sum into sum divided by 2 and this is called as n and if i want to print n here

1:25:26

how do i do that how do i achieve that in order to achieve this i will have to use this sum am i correct

1:25:36

that means this sum should be returned from this function does everyone agree the value of c

1:25:44

should be returned from the function unless and until c is returned from the function i cannot

1:25:49

use it here right plus my compiler will also give me an error it will also give me an error it will

1:25:56

say that yes you are saying the function will return something but actually your function

1:26:02

is not returning anything so it is wrong okay so how do you return something from function you do

1:26:08

return see so what is return here return is the keyword that is used to return any value from the

1:26:19

function whatever thing you want to return from the function you use a

1:26:26

return keyword that's what you do if you do not want to return anything do not use

1:26:33

return keyword if you want to return anything then use the return keyword is that clear

1:26:40

everyone comfortable if you are using a print statement then the value is not returned

1:26:52

himan chum print statement will just print the value from here that okay till here

1:26:58

whatever is the value okay but if you return the value back to the function see i will repeat this

1:27:06

one more time abyshek please pay attention this was my main function from my main function

1:27:15

i executed some lines of code and then on line number three i called the add two numbers

1:27:22

now add two numbers date a plus b and i print here c now this add two number

1:27:33

is not returning anything back to main am i correct that means it is printing the value here

1:27:39

then and there itself is that clear okay now if i want to return the value it means for

1:27:47

example after this line number four will be executed in this function main does everyone

1:27:52

even agree once the line number three is executed completely line number four will resume

1:28:00

do you guys agree with me on that

1:28:04

so if i want the value of see here on line number four how do i get that is there any way

1:28:14

the way is only when the above function returns you the value if that function is not

1:28:20

returning you the value then you can not not

1:28:22

get the value of c does that make sense everyone comfortable okay let us see that

1:28:34

see that in action in the code and then discuss

1:28:52

to see my code screen okay so i will comment this part i have functions okay now what i

1:29:02

will do is i will define another function deaf let's say add number a comma b c equals to

1:29:18

a plus b return c now as soon as i do return c what is going to happen

1:29:26

sum equals to add two number one comma two print sum is sum is sum now what will be the value of

1:29:39

sum here it will become whatever has this function returned what this function has returned it has returned

1:29:45

it has returned you the value of c for example c is now let's try to print the code

1:29:55

run now if you see here c is three first of all let me add a print statement here print

1:30:02

print executing the function okay run the code so this line got then you do c equals to three

1:30:15

then you return the value of c so this line will be executed as soon as add two number function is executed

1:30:22

whatever is the output of add two numbers it will be captured into the sum variable and then i have

1:30:31

printed this sum here yes can we do more than printing definitely for example if this is uh

1:30:40

if let's say this is something like if i want to do something like if i want to do more than printing definitely for example if for example if this is

1:30:45

to do some if i want to find okay i have do you guys know the mathematics

1:30:52

formula of sum of first and natural numbers it is n into n plus 1 by 2 do you guys remember

1:31:05

number n into n plus 1 by 2 right now assume that i want to find this sum of

1:31:18

n natural numbers and whatever is returned here is n so what i will do n into n plus 1 by 2 and i

1:31:30

will do this sum of natural numbers and i will do this sum of natural numbers

1:31:35

and then i can do print sum is sum of natural numbers so what i did here is

1:31:49

is i called a function which added two numbers the output of those two numbers was n and i wanted

1:31:59

to find the sum of first in a natural numbers so in this case if i pass one comma one

1:32:04

the output will be 2 does everyone agree the output will be 2 does everyone agree

1:32:12

right now what i will do sum of first n natural numbers so n into n plus 1 by 2 that

1:32:20

means 2 into 3 by 2 makes sense so if i run this code sum is 3 does everyone agree

1:32:29

with me some will be 3 first in natural numbers how many for

1:32:34

what are the first and natural numbers 1 comma 2 okay if i pass here 1 comma 2 then the

1:32:41

sum will be 3 and the output will be 1 plus 2 plus 3 does that make sense so if what i wanted to say is

1:32:54

this is only possible when i return something from my function what do you guys think unless an

1:33:04

until i return i don't return anything from my if i don't return anything from my function

1:33:11

can i do something like this no then i will have to put this line of code inside this function only

1:33:18

do you agree do you agree

1:33:34

okay now let's take one last example for the day okay what i want to do is

1:33:48

i want to basically uh the way we will do that don't worry actually uh the way we will do that

1:33:57

don't worry actually we will do this example and as part of that you will understand it now what i want to do

1:34:02

do I want to basically create a billing system at restaurant which will take the quantity

1:34:16

of item in input based on the quantity we will find out the total bill

1:34:32

including okay note we also have to add tax 10% on the total amount is this problem statement clear

1:34:49

what i want to do i want to take the input from the user that whatever you have ordered and

1:34:54

what is the quantity of the item that you have ordered based on the quantity of the order i will

1:35:00

multiply with the base rate and then i will find out the total value make sense everyone okay

1:35:08

so assume that there are three items item one which has a base rate of 200 item 2 which has a base rate of

1:35:20

300 item 3 which has a base rate of 400 okay so what we will do we will take the input from the user

1:35:28

item 1 quantity in input enter quantity of item quantity of item 1 copy paste paste item 2 quantity item 3 quantity enter quantity of item 3 okay now if i do not use functions what is

1:35:58

something that i will have to do item one quantity into 200 that will become

1:36:08

sum for one or total for item one can i say that i say that total for item one can i say this total for item 2

1:36:22

will be item quantity 2 into 300 can i say this what do you guys think

1:36:28

total for item 3 will be item quantity 3 into 400 correct then what i have to do total for item 1 plus total for item 2 plus total for item 3

1:36:46

all of this code i will have to write it in the single file can i say that and then this will be the total bill

1:36:58

right as of now i am not using any function then what is the next thing that i will have to do

1:37:06

tax equals to total amount into 10 percent can i say that into 0.10 which is my 10 percent right so

1:37:23

final amount will be tax plus plus total amount will be tax plus total amount

1:37:28

can i say that and finally you will do print this is your total any doubts in this

1:37:40

this code i have returned without using any functions everyone comfortable now if i have to

1:37:47

use functions how do i do that if i have to do if i have to use any functions what will i do i can do one

1:37:57

do one thing very simple i can create a function which takes the item and passes the item into that function for example what i can do here def total for item one okay and what i will do quantity and what i can do here is

1:38:27

item.

1:38:28

If item equals to item 1, then quantity into quantity into 200.

1:38:42

L if item equals to item 2, then quantity into 300.

1:38:54

else quantity into 400 now if i have to call this how do i call any thoughts if i have to call this

1:39:06

any thoughts if i have to call this how do i call any thoughts i will have to replace these

1:39:14

three lines can i say that i will have to replace these three lines in my code does everyone agree right

1:39:23

so what i will do here total for item one total for any item i will pass here item one quantity

1:39:33

comma item one does that make sense similarly item two item three item two item three item two item three does that make

1:39:48

sense so this function i am now reusing again and again

1:39:53

okay what else i can do can i create one more function for finding out the total amount so def calculate total right

1:40:07

one two three and i can do default value as okay yeah this now what i will do return one plus two plus three

1:40:23

okay so what i will do instead of using this i can do calculate total total for item one total for item two total for item three what do you guys think about this does that make sense everyone right yes or no and whatever is the total amount i will

1:40:53

multiply it with this and i'll get the final amount so i can create one more function

1:40:57

which can tell me the final amount so dev final amount what it will do it will do it will take the

1:41:05

sum return sum plus sum into point one zero can i say that sum plus sum into 10 can i say that

1:41:17

sum plus sum into 10% basically this is the 10% of my sum right everyone so can i say that

1:41:27

instead of doing all of this i can just call final amount equals to final sum or total amount to be

1:41:39

collected what i will do final amount and pass here total amount what do you guys think about it

1:41:47

this is how you use functions in python okay so let's actually try to run this code and see whether it if it works or not run okay actually let me stop why it is printing all of this

1:42:03

okay i'll just comment it out okay let's run enter quantity of item one one enter quantity of item two two enter quantity of item three three oh there is some problem what is a problem what is a problem

1:42:17

one plus two plus three calculate total total for item one total for item one total for any item

1:42:29

uh what we are doing here i think we have to convert oh i think we have a problem i can even tell me what is a problem here i think you guys would be able to do it so as soon as you do total for any item you will come here but are you will come here but are you

1:42:47

you returning anything from this function so return return return return does that make

1:42:55

sense everyone let's run the code again one one one one total will what is the problem

1:43:05

amount will be collected let me run one more time one one one one total amount to be connected

1:43:17

how 990 is getting yes 200 300 300 what is the total 900 900 900 plus 10% of 900 how much is that

1:43:30

90 rupees is everyone comfortable yes imagine line number 78 yeah let's discuss cool so are we good with

1:43:44

functions in python now uh let me give

1:43:47

this code to you guys.

1:43:51

Okay, can you please? Can you please check how you able to access it or not?

1:44:17

is everyone able to access it okay take it so before we leave quickly revising from where did we started today we started with functions right we learned about what are functions we learned the use case that what do you mean by a function right then we discussed that okay how do you create

1:44:47

function what is the syntax of creating a function we discussed that then we also

1:44:51

discussed about that okay how do you set default valuables like how do you give a value a default

1:44:58

value how do you give a parameter a default value we learned about that and we also learned about what

1:45:08

could you explain this why is not print anything sorry rohitha i did because you are not

1:45:17

printing anything unless and until you print rohith anything it will not print you will

1:45:22

have to print right so what you will have to do you are doing add number 10 comma 12 right you are

1:45:29

returning a value but are you printing that value which is returned from the function no okay

1:45:39

make sense roit okay cool so that's it

1:45:53

that's it from my side I guess everyone enjoyed the session thank you everyone

1:45:57

advantage what is return use can't

1:46:01

hey Devi we have seen what advantage here?

1:46:03

if I'm not use not if I return use not do so

1:46:07

So if I'm a function to use a value use for example, this is total, right?

1:46:13

So if I return this value return from the way, then do you can't this value

1:46:17

are going to use this value again use can?

1:46:22

No.

1:46:23

This is it's a benefit.

1:46:25

That if you want to use the value later in your code, return helps you achieve that.

1:46:35

If I return not return not return, then if I return not return not, then if I return not return to return, then

1:46:36

So do I have this all of all of the code in one place, Divya?

1:46:41

If I return not have to, then do this all of the code

1:46:44

one place to write?

1:46:47

Right?

1:46:48

Yes, return throws a value out of the function.

1:46:51

Absolutely correct, I mean.

1:46:57

Make sense?

1:46:59

Okay, so are we good, everyone?

1:47:05

Cool.

1:47:11

Awesome.

1:47:12

So that's it from my side for the day.

1:47:16

Thank you everyone.

1:47:18

I hope everyone enjoyed the session.

1:47:21

I'll just set up in VS code.

1:47:25

Chandan, it is something that I can give some links to you, but you will have to do that by yourself.

1:47:31

Okay, so just Google about it that how do you set up VS code?

1:47:39

Just Google about it and you will get to know.

1:47:41

You'll have to download it.

1:47:42

If you are on Windows, you'll have to download a EXC file.

1:47:46

And if you're on Mac, you'll have to download a DMG file and just casually install it.

1:47:49

Okay?

1:47:50

Just check how do you run your first program in VS code and that should help you out.

1:47:56

Cool.

1:47:57

Thank you guys.

1:47:58

I hope everyone enjoyed the session.

1:47:59

Bye-bye.

1:48:00

Have a nice day.

1:48:01

ahead. I'll just give a word to which I.

1:48:03

Sure.

1:48:04

Bye.

1:48:05

Okay.

1:48:06

We can start with the quiz.

1:48:08

Is everyone ready?

1:48:11

Okay. So the Mentiometer code is in front of you?

1:48:20

Please do the scan.

1:48:22

Or you can directly go in the browser and like put this code.

1:48:27

Just do a thumbs up once you will join.

1:48:31

I will wait for 15 seconds more.

1:48:35

Last 5 seconds.

1:48:36

for 15 seconds more.

1:48:49

Then we will start with the quiz.

1:49:06

question in front of you.

1:49:21

Answer it quickly to get more points.

1:49:36

So, here the question was how you will be going to call, not how you will be going to define.

1:49:42

So just read the question before you will answer.

1:49:45

Your correctness matters more than time.

1:49:49

Let's see who have given the fastest correct answer.

1:49:56

Okay, beyond so on the top.

1:49:58

Let's move to the second question.

1:50:00

Just do a thumbs up on your answer screen.

1:50:06

Let's start with the second question.

1:50:13

Five seconds more.

1:50:36

Okay, this time like most students have given the correct answer.

1:50:42

Let's see who is at the top.

1:50:47

Okay, yes was the fastest answer.

1:50:53

He is at the top.

1:50:55

Let's move to the next question.

1:51:06

Answer it firstly so that you can get more points.

1:51:13

But make sure to read the questions and all the options very carefully.

1:51:17

If you will give wrong answer then anyways, you will not be going to get any points.

1:51:31

We don't use function to write the code faster.

1:51:35

And here, like the case was increase, not decrease.

1:51:38

So it will decrease the court repetition.

1:51:41

So as I said, please read the answers very carefully.

1:51:45

Let's see who is at top.

1:52:05

Five seconds more.

1:52:26

Yeah, this time like most of the students at the top of the list board.

1:52:35

Okay, Ayush is at the top.

1:52:44

This is the final chance to be on the top of Leaderboard.

1:52:48

So read the question very carefully and try to answer it correctly with minimal time.

1:53:05

Okay, yeah, again, like most of the students have given the correct answer.

1:53:26

Let's see who is the final winner.

1:53:35

Yeah, rest like please try to be on the top of the leaderboard from next time.

1:53:43

Yeah.

1:53:44

Let's do a quick feedback.

1:53:51

Yeah, we are done for today.

1:53:53

You can just provide the feedback and drop up.

1:53:59

So you will see the feedback questions on your zoom screen.

1:54:04

We are done for today. You can provide the feedback in like drop-up.