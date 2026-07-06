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

Thank you.

4:54

Thank you.

5:24

Thank you.

5:54

Thank you.

6:24

Thank you.

6:54

Thank you.

7:24

Thank you.

7:54

Thank you.

8:24

Thank you

8:54

Thank you

9:24

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

Thank you.

9:46

Thank you.

10:16

Thank you.

10:46

Thank you.

11:16

Thank you.

11:46

Thank you.

12:16

Thank you.

12:46

Thank you.

13:16

Thank you

13:46

Thank you

14:16

Thank you

14:18

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

Thank you.

14:38

Thank you.

15:08

Thank you.

15:38

Thank you.

16:08

Thank you.

16:38

Thank you.

17:08

Thank you.

17:38

Okay.

17:42

Okay. Good evening, good evening everyone, everyone. Hello. Hello.

18:08

I hope everyone is doing fine.

18:14

Hello, hello.

18:19

Just one sec. I'm just one sec. I'm just.

18:38

I fix this.

18:41

One second, guys.

18:42

We'll start in just a minute.

18:44

Sorry to interrupt.

18:46

Can you please make yes as co-host?

18:49

Hey, these are the company that I work here.

18:53

Hello.

18:54

Cool.

19:03

Is everyone able to give me out?

19:07

My audible? Okay, awesome. Take it. I hope everyone is able to see my screen as well.

19:14

Okay, okay. So, welcome to today's session. I hope everyone is doing fine.

19:22

Awesome, cool. So the agenda of today's session is to discuss on sorting algorithms. The most basic sorting algorithms basically are bubble sort and selection sort.

19:35

We will discuss over them.

19:36

over them. So today's class, today's class is going to be a very lightweight class in my opinion,

19:42

but from the fact that, you know, we are going to learn something new here.

19:48

As in, see, there was a question in the chat that yes, why are we learning bubble sort,

19:53

selection sort, even though there are sorting algorithms, solidly present in languages.

19:58

The main agenda is to develop the intuition of how do you code.

20:05

Okay, that is the main intention. Once we start with these two sorting algorithms,

20:13

we will get a fair idea of how do you build a basic level of intention in coding?

20:20

And once you have an intuition, you can start with the code.

20:24

That's the main point here, not to, you know, learn about something which is already there and all of that part.

20:31

So, why are we learning these two algorithms?

20:34

these two algorithms. Is that clear to everyone? The main agenda, is that clear?

20:43

Yep. Okay. So the first reason is, I'll just write it for everyone's comfort.

20:50

The first reason is they build intuition.

21:04

Okay. The second thing is we will understand how do you, how we can trace our code by these two algorithms. At least we will have a basic level of understanding that if I want to debug my code, if I want to trace my code, how do I do that?

21:20

So train to trace the code.

21:34

you know important points as well is they help us understand the big O notations.

21:41

For example, do you guys remember the big O notation that we discussed in the previous session on the time complexity?

21:47

So these are the entry point for, you know, understanding some basic to medium, to medium level complex cities, how do you determine all of that?

22:03

That is the main agenda for them. Okay. Now, before we start, before we even start with today's session, I just quickly want to take two minutes to discuss quick recap of the previous session.

22:19

So, where did we left previous session? What did we discuss and what did we left? Anyone can please help me out with the topics?

22:33

Okay.

22:35

Okay. And what functions did we covered? Like what did we covered?

22:43

Unfunctions specifically? How do you create a function? Am I correct?

22:49

How do you call a function?

22:55

And what is the main benefit of creating functions?

23:01

The main benefit is the main benefit is.

23:02

The main benefit is reusability of my code. Can I say that?

23:08

Reusability of my code. Can I say that? What do you guys think?

23:14

Yeah? Okay. Then we also saw that there can be two type of functions. One which do not return anything.

23:26

And other types which can return value. Can I say that?

23:32

Can I say that?

23:34

Right? And then at the end of the day, we also saw that I can pass some parameters in my function.

23:41

Okay. So this is a highlight of what we discussed in the previous session.

23:59

Okay. Now let's just a highlight of what we discussed in the previous session.

24:01

Now let's start with sorting algorithms.

24:05

Okay. Now, what is sorting?

24:25

What is sorting?

24:28

arranging numbers in a format. Absolutely correct.

24:37

And arranging numbers in either ascending order or descending order. Can I say that? What do I think?

24:51

Arranging things in ascending order or descending order?

24:57

agree right okay now there are multiple type of sorting algorithms

25:05

multiple types okay the most common ones being bubble sort

25:13

selection sort

25:19

merge sort

25:27

and there is one more which is called as heirsort.

25:33

But today the agenda is to cover these two.

25:40

Okay?

25:43

Cool. Now, let's take one problem statement and then let's try to conquer that problem statement from sorting algorithms point of view.

25:54

Okay, so let's start with bubble sort.

25:56

okay now imagine a row of people standing in a line

26:14

okay and you want to arrange these these people from shortest to tallest to tallest.

26:26

Okay? Now what bubble sort says is you start at one end and compare every pair of neighbors with one another. That means you start with any one of the sides.

26:41

So if I start with A, I will compare A with B. Then I will compare B with C.

26:50

So every time you compare B with C. So every time you compare each of the side.

26:56

neighbors. If the left person is taller than the right person, then they will need to swap the places. Can I say that? Can I say that? Does everyone agree? I will repeat one more time. You start from left to right. Compare all the neighbors one by one. If as part of the comparison, if any person on the left to left,

27:25

is taller than the person on the right, then you swap.

27:31

You say that, okay, the shorter person will go on the left, the taller person will go on the right.

27:36

Right? And we walk down the street doing this thing.

27:41

And by the time I reach my end, by the time I reach towards the end, can I say that the end position will be taken by the tallest person?

27:55

Think and tell me. By the end, the tallest person will be swapped in the end. Can I say that?

28:09

So can I say that the person was actually present in the front, maybe, and we bubbled up that person to the last position.

28:19

Can I say that? Like, okay, if two of them are not at that position, you swap them. You bubble the taller one.

28:25

the right. Again, you bubble the taller one on the right. Again, you bubble the taller one on the right.

28:31

So, I have to repeat this entire walk every time. Every time I repeat this completely. Every time I repeat this

28:44

completely, I can make sure that the tallest person will go towards the right. Can I say that?

28:55

Can I say that? Does everyone agree?

28:58

Can you all of the same? I've said what I've said?

29:01

So, if I'm algorithm to talk to, it's very simple.

29:06

Okay?

29:06

First, my algorithm, I will write algorithm meaning plain English words.

29:10

Then we will take one array example, do a dry run.

29:14

And then we'll then we'll then we'll see it.

29:15

And then we'll see it.

29:17

Does that make sense?

29:19

Okay? So bubble sort.

29:22

Algorithm.

29:25

what the algorithm says is start at the beginning of the array.

29:55

Right? Then compare each pair of adjacent elements.

30:16

That means, compare 07 with 1.2 with 1, 2 with 2, 2 with 3, and so on.

30:25

If they are in the wrong order, then what do I need to do?

30:40

What do I need to do?

30:46

Any thoughts?

30:49

If they are in the wrong order, what do I need to do?

30:52

If they are in the wrong order, what do I need to do?

30:53

If left-wala-in-in-sha-ha-ha-ha-right-wa-ha-ha-ha-ha-right-wa-le-sa.

30:54

Then what do I need to do? I need to swap.

30:59

Everyone agrees with me.

31:03

Okay.

31:05

Continue this thing till the end of the area.

31:22

Okay. If I continue, if I continue, till the end of the area.

31:24

the last of the array, this is called as one pass. So as soon as this one pass is

31:35

completed, can I say that the largest person will be bubbled up towards the right?

31:42

In the right part, like towards the last index of the array, the right person will go there? Can I say that?

31:50

Right? Now, this is about the tallest person, that the tallest person has gone towards the end.

32:03

What about the second tallest? Second tallest can lie on the second position. So I will have to

32:09

repeat this step again one more time. Right? Does everyone agree?

32:15

Now, this job this, he's just the tallest person to last in move to. But what about

32:20

the second tallest person. Second tallest person, I will have to repeat this step one more

32:25

time. So how many types, how many times I will have to repeat this? The number of elements. Can I say that?

32:50

This algorithm is basically called as bubble shot. Are we good? Everyone. Are we good here?

33:07

What is algorithm? Algorithm means basically the series of steps that I am going to code. Okay Alvin?

33:20

you go from your home to your office, you follow a route. That route can be an algorithm that

33:27

okay, you have to take straight, then right, then go straight, then take again right, then take a left,

33:32

and then finally stop. What is this? This is a series of steps that you will follow to reach

33:38

your end goal. Okay? Similarly, in order to solve a problem statement, we have to think through

33:46

different steps. All of the steps combined together is called an algorithm. Make

33:53

sense? Okay, awesome. Now let's take one example of array.

34:02

Yeah, Prashanth, we'll take one example of the array and then do a drier on that.

34:07

So, that we'll make idea like actually what's what is actually what is. Make sense? Okay. And still, if it is not

34:16

clear then we will discuss one more time. So let's assume that I have an array or a list in

34:22

Python 51428.

34:46

though this is not sorted. Okay? So as per my algorithm, what I will do? I will start

34:52

at beginning. I equals to 0. Okay. So what is A of I of I? In this case, 5. Does

35:06

everyone agree? Does everyone agree? And compare this with the next element which is J.

35:16

So what it will be? A of J. What it will be? Can anyone please tell me? One. Does everyone agree? So 5 versus 1. Is the number on the left greater than the number on the right? Is the number on the left greater than the number on the right?

35:42

Yes, this is the number on the left greater than the number on the right?

35:44

So I will swap these numbers with one another.

35:48

Okay, you have all of them?

35:50

So I what I will?

35:52

After this iteration, right? When I become 0, after this iteration, how my array would look like?

36:00

1.5, 4, 2, 8. Is everyone comfortable?

36:13

What?

36:15

I have?

36:16

All right?

36:20

Now I'm next item

36:25

now my I is equal to 1.

36:29

Okay?

36:31

I will be

36:32

A of I equals to 5.

36:36

A of J equals to 4.

36:40

5.

36:41

5

36:42

versus 4.

36:44

What will?

36:45

Who will me to tell me?

36:46

will repeat again.

36:48

Okay, let me cut this part. I will repeat this one more time.

37:06

Okay, so I'll repeat this one more time.

37:09

So, what I did?

37:11

I and J.

37:16

Can I say, I equal to 0?

37:18

When I say I equal to 0,

37:20

then J my 1 will do.

37:22

Do you have to compare the neighbors?

37:25

If I say I equal to 0,

37:28

I is an index, hypothetical index.

37:32

So J will become 1 because I need to compare the indexes.

37:35

Can I say that?

37:38

Does everyone agree?

37:39

Okay.

37:41

So I will have to compare 5 with equals to 1.

37:46

In this case, what will happen is 5 is greater than 1?

37:51

Yes, yes, 5 is greater than 1.

37:53

So what we will do?

37:54

I will have to swap.

37:56

When I compare 5 with 1, 1 is smaller than 5 and 1 should come on the left of 5.

38:02

Can I say that?

38:05

When I just compare 5 and 1, 1

38:08

One is one first.

38:10

Right?

38:11

So ideally, my array should look like this.

38:16

Does everyone agree?

38:20

After swapping, my array would look like this.

38:23

Does everyone agree?

38:26

All of all of them?

38:29

Alright.

38:30

Now next time,

38:32

next time,

38:33

I will now,

38:34

now I'm compare to 5 and 4.

38:37

Right?

38:39

Okay.

38:40

What will happen here?

38:42

5 versus 4?

38:43

Is 5 greater than 4?

38:46

Is 5 greater than 4?

38:49

Yes, absolutely big.

38:51

So ideally what should happen?

38:53

Ideally what should happen?

38:56

Swap.

38:57

Because 5 is 4 is, so 4 is,

38:59

so 4 5 to be before before

39:00

to 1.

39:01

Does everyone agree?

39:03

Right?

39:04

So I will swap.

39:06

Okay, so after swapping, how my array would look like?

39:11

1.4, 5, 2, 8.

39:16

Do you?

39:18

All right?

39:20

All right?

39:21

Everyone comfortable?

39:26

Yeah,

39:29

you can take the variable name you?

39:31

Prasan, do you remember?

39:32

When we for loop,

39:34

So we'll write for I in range, for J in range, right?

39:40

Right?

39:41

Right?

39:42

So sorting algorithms are implemented only in R&A.

39:45

Uh, so you know,

39:47

you have sorting on just an integer?

39:50

Can you have sorting on just an integer?

39:53

If I have just a number,

39:55

4, that,

39:57

can I sort that?

39:59

No.

40:00

So ideally, sorting should only be done when I have list of some people.

40:03

Can I have some people?

40:04

Can I say that?

40:05

Sojanya?

40:06

Okay, make sense.

40:08

Okay?

40:09

Okay?

40:10

Okay.

40:11

Okay?

40:12

Now, at this point, my array will look something like this.

40:18

Can I say that?

40:20

145-28?

40:22

Correct?

40:23

Right?

40:25

Right?

40:28

Now?

40:29

Now, next time I will do

40:31

this versus this.

40:35

I will become 5

40:38

and the neighbor of I will become 2.

40:42

Can I say that?

40:44

So 5 versus 2.

40:48

Is?

40:49

5 is bigger 2 to say?

40:52

5 is a big?

40:54

Now we are the algorithm

40:55

we are how to code how to

40:56

I will tell you to tell you

40:57

don't worry about it.

40:58

Code not.

40:59

Code is the simple.

41:00

simple. Okay?

41:02

Make sense?

41:04

If we're just

41:05

if we're going to discuss

41:06

then it will become a problem for everyone.

41:08

Because we're confused

41:09

So first we're

41:11

our algorithm

41:12

then we once are 100% sure

41:15

that,

41:16

then code is a cakewalk.

41:18

Okay?

41:19

So here,

41:20

so here,

41:21

that what will happen here?

41:22

Will we swap?

41:24

Will we swap?

41:28

Yeah, we'll do.

41:29

Yes, swap.

41:30

So I will swap.

41:31

So at the end, how my array would look like?

41:33

1.

41:34

4.

41:35

2.5.

41:36

8.

41:37

Does everyone agree?

41:52

Now I'm going to compare

41:53

5 versus 8.

41:55

Now you guys tell me

41:57

I becomes equals to 3

41:59

J becomes equals to 4

42:02

Okay?

42:03

5 versus 8

42:06

What will happen?

42:07

Do we need a swapping here?

42:08

What is?

42:09

Do we need a swapping here?

42:10

Do you?

42:12

not?

42:13

No, right?

42:14

58 is small?

42:15

Everyone agrees with me on that?

42:18

Right?

42:19

So swap can't

42:20

because

42:21

8 is big

42:22

so 8 right right in

42:23

and 5 is

42:24

and 5 is

42:25

so

42:27

no solving.

42:28

So your array

42:29

after this iteration

42:31

will remain as it is.

42:33

Okay.

42:34

So if I'm now

42:36

my arrow to look

42:37

so can I say that

42:40

till 5

42:42

my array is actually sorted?

42:44

Can I say that the

42:47

array is actually sorted after 5?

42:51

can I say that?

42:52

that?

42:53

So actually I can say that my array is divided into two halves now.

42:58

One half where the array is not sorted.

43:01

Second half where the array is sorted.

43:05

Yes, you have all

43:06

is

43:07

said?

43:08

Does everyone agree?

43:11

Yes,

43:15

okay.

43:16

Okay.

43:17

Do you?

43:18

Okay,

43:20

my sorting completed

43:21

have?

43:22

Can I say that my array sorted?

43:23

No,

43:24

no,

43:25

my sorting complete

43:26

not.

43:27

I have just

43:28

just a number

43:29

bubbleed last.

43:30

I still need to bubble four, and still need to, you know,

43:34

left side the array is,

43:36

the orange one, I need to fix that.

43:38

So now I will start with pass to.

43:41

Pass 2.

43:46

Okay.

43:47

In past two, what will happen?

43:53

This is my array.

43:54

In past two, what will happen?

43:58

Again, I will start with 1 and 2, 1 and 4.

44:02

Okay, do 1 and 4

44:04

is, is the right?

44:06

Yes, so do I need a swapping?

44:12

Do I need a swapping?

44:14

No swapping?

44:16

No swapping.

44:17

Right? Okay.

44:19

Second iteration?

44:21

This time, 4 with 2.

44:27

Here, in this case, 4 versus 2.

44:33

Do I need a swapping here?

44:37

Absolutely, yes, 100%

44:39

so we'll swap.

44:41

After swapping how my array would look like?

44:44

1, 2, 4, 4, 4.

44:46

5, 8. I will just swap these two numbers.

44:54

Everyone agrees with me?

44:56

I was at index 2.

45:00

So, index 1, J2.

45:05

What will happen?

45:07

I now becomes 2, J now becomes 3.

45:10

So I will compare this with this.

45:13

Are they sorted?

45:15

Hi Esh, this is sorted.

45:19

Everyone agrees with me, 4 and 5.

45:21

So, no swap needed.

45:24

Okay.

45:28

Similarly, next time, I will become 3, J will become 4.

45:42

Do I need a sorting?

45:44

Do I need a sorting?

45:49

No.

45:50

So basically, this algorithm what is

45:52

what you have observed is?

45:54

The highest value is in every pass,

46:08

one highest value

46:13

is bubbled to the right.

46:20

Can I say that?

46:25

Everyone agrees with me?

46:28

Yes.

46:31

Okay.

46:33

So, this is the algorithm

46:36

we've got

46:38

now the time comes to start with

46:41

the code.

46:42

code.

46:43

Once we write the code they will, then we'll

46:46

see how many comparisons we have

46:48

are we doing.

46:49

Are we good?

46:50

Logically, the algorithm is

46:53

clear?

46:54

What are you?

46:55

Now let's try to understand the same thing with code.

46:59

Now, now we're logically in the

47:01

Dima'am in clear, how is it?

47:02

Writing code will be relatively easy.

47:06

Okay, okay?

47:08

So let me go to my code screen.

47:11

One minute, I am just sharing my screen.

47:22

Okay, is everyone able to see my screen.

47:38

Is everyone able to see my screen?

47:41

Everyone?

47:42

Okay.

47:43

So now,

47:51

we're going to

47:53

Okay.

47:54

So first of all, I'm this

47:57

run and see

47:58

Okay, hello world print

47:59

that means the compiler is okay.

48:02

Okay.

48:03

Now, let's start.

48:06

So first thing, I have an array.

48:10

which example date we took 51428.

48:17

So 51428.

48:18

So 51428.

48:20

This is how I define an array or a list.

48:23

Does everyone agree?

48:26

Right?

48:27

Now, I can create a function

48:32

which is doing the sorting for me

48:36

and returning the sorted array.

48:40

So what I can do?

48:42

Bubble, sort,

48:44

and I can pass the array here.

48:47

What do you guys think about this?

48:49

And finally I can print sorted array, right?

48:52

Does everyone agree?

48:53

Now if I'm going to a function

48:55

then I have to have to define it here.

48:58

Def, bubble sort.

49:01

And start with the code here.

49:03

Does everyone agree?

49:09

code for bubble solve.

49:16

Right?

49:17

Okay.

49:18

So first of all, first things first,

49:21

I'm going to take a array

49:23

length because I have to start the traversal on that array.

49:27

Right?

49:28

So how do I find out the length of array can even sell me?

49:31

A-R-R-R-Lent.

49:36

Lent

49:37

How do you?

49:38

How do I find length of array?

49:41

LEN of array.

49:44

Can I say that?

49:46

Does everyone agree?

49:50

Using the length function.

49:52

Now I have to iterate on an array.

49:55

Now I have to start with the iteration.

49:59

How do I iterate on an array?

50:05

How do I iterate on an array?

50:07

So for I in range

50:11

A.R Lenn,

50:15

I just for N for simplicity.

50:17

N minus 1. Can I say this?

50:21

Can I say this?

50:23

Can I say this?

50:25

Why I am doing n minus 1?

50:27

Who will me tell you please?

50:32

Why I am doing n minus 1?

50:36

Because

50:37

Index starts from 0.

50:39

Okay?

50:40

Now here what I have?

50:41

What do?

50:42

Now,

50:43

I basically

50:46

Wapest comparison

50:48

this is for every pass

50:51

for every pass I have to compare

50:55

the neighbors.

50:56

Does everyone agree?

50:58

This loop will run for every pass.

51:02

But in every pass I have to compare the neighbors.

51:06

So for one by one.

51:07

So for that, I will need another loop for J in range 0 to n minus 1.

51:16

Can I say that?

51:20

Does everyone agree?

51:24

If A.R of J is

51:33

greater than A.R.

51:36

A.R.

51:38

of J plus 1.

51:41

If this is, then what do?

51:43

What do?

51:44

If this is the case, then what I should do?

51:49

Swap.

51:50

So, if I'm simply

51:53

to write,

51:54

left index

51:56

equals to J

51:58

right index

52:06

Here I'm going to write index.

52:09

Is it better for all of all?

52:12

Okay.

52:13

If left index is greater than the right,

52:16

if left value array

52:18

is the right value

52:19

than the right value is

52:20

better, then I should swap.

52:23

Okay.

52:24

So I swap how can

52:25

whatever is present on the index of 1

52:30

should be swapped with whatever is present on index of 0.

52:34

Can I say that?

52:35

Okay?

52:36

So A.R.R. of left, comma, A.R. of right.

53:02

Now

53:05

you can't.

53:06

You are swapping the values using a single line in Python.

53:12

Okay?

53:13

If you have a normal swapping code

53:15

to look at,

53:16

then you can it

53:17

during the break,

53:18

you can see.

53:19

But if you're normal swapping code

53:20

then how do you?

53:21

How do you?

53:22

If you have to swap

53:28

two numbers, how will you do it?

53:30

If you have to swap two numbers, how will you do it?

53:32

If you have A comma B and you need to

53:34

and you need to swap.

53:41

So

53:43

A temp

53:45

a temporary available

53:46

to be a

53:48

Then A

53:50

I'm B

53:51

store

53:52

and B in A

53:53

B in A value store

53:54

Do you

53:55

agree?

53:56

So,

53:57

so I can swap

53:58

two numbers

53:59

can

54:04

agree.

54:05

So you either you

54:06

you can

54:07

this is a

54:08

temporary

54:09

variable

54:09

by

54:10

or then

54:11

there is a

54:11

provision, you

54:12

you

54:13

can it's a

54:14

completely up to you

54:15

I have

54:16

you, you

54:17

you can't

54:18

you

54:19

agree with me?

54:20

Okay

54:25

so

54:26

I'm

54:27

swapped

54:28

I'm

54:30

after I'm

54:34

in which you

54:35

this

54:36

you have

54:37

okay

54:38

okay

54:39

so

54:40

this one

54:41

now

54:42

what we're

54:43

this

54:44

this loop will be

54:45

completed

54:46

this loop will be completed

54:47

here

54:48

here

54:49

I'm here

54:50

can everyone

54:52

agree with me on this

54:53

on this

54:54

okay

54:56

okay

55:04

if it

55:04

if it's

55:05

if

55:06

it's

55:07

we're

55:08

it

55:09

we're

55:14

here

55:15

here

55:16

here

55:17

here

55:18

print,

55:19

input

55:20

A

55:21

and

55:22

and

55:23

sorted

55:24

sorted

55:25

and sorted

55:34

Input

55:34

input

55:35

isn't,

55:36

not,

55:38

and sorted,

55:39

are

55:40

Is this

55:41

all

55:42

all

55:43

question

55:44

what is

55:45

we're

55:46

we're

55:47

We're

55:48

we're

55:49

we're

55:50

again

55:51

once again

55:52

again

55:53

I'll

55:54

again

56:04

not find how many iterations I have to run.

56:06

Does everyone agree?

56:10

Because the length of the array is not given to me in the question, so I will

56:14

have to find it out on my own.

56:16

I will find out the length and I will start with the traversal here.

56:21

Okay, so print

56:22

iteration

56:25

I.

56:30

Okay?

56:32

So in iteration

56:34

What I will do? This internal loop will executed completely, will be executed completely. Can everyone agree with me?

56:42

For iteration zero, this internal loop will be executed completely. This internal loop, what it is doing? It is swapping two values at a time.

56:54

Right? It is swapping two values at a time.

56:57

Every time it is checking these two values, these two values, these two values, these two values,

57:03

These two values, these two values.

57:05

And if the left value is greater than the right value, then it will swap.

57:09

Else it will move forward by, because it will not go into this if conditions.

57:15

Is this if conditions?

57:17

Everyone.

57:21

Just like we are putting the inner loop in the range zero to and why are not putting outer loop?

57:27

Can you, it is the same thing, San Yuta.

57:30

It does not matter.

57:32

You can do that.

57:34

Okay?

57:36

It should be the same.

57:38

Okay?

57:39

Okay.

57:40

Okay.

57:41

Is why we took left index as J?

57:46

Because I have every time

57:48

two values to compare

57:50

So the left index will,

57:52

that's little right index.

57:54

Right?

57:55

The index is 5 is 0 and 1 index is 1.

57:59

So if I'm these two values compare

58:01

so left the index is my small and right index my big.

58:04

Make sense?

58:06

So here we are starting from left.

58:18

If you're right start to,

58:20

then your greatest value is,

58:22

the left in bubble up.

58:24

Okay.

58:27

Now what I will do is

58:29

Now let's discuss on the time complexity.

58:34

Now you have one of the time complexity.

58:36

Now you have one of this time complexity

58:40

what will take, think and tell me its time complexity what are.

58:44

Okay.

58:45

O of n square.

58:58

Okay.

58:59

N do you have answer of question like answer for that as well?

59:03

O of n, okay.

59:05

By O of n square by O of n.

59:07

Two loops.

59:08

That is the problem.

59:09

Whenever there are two loops, we should never, never, never assume that it is a O of N square.

59:14

I think we have discussed this in the last session as well.

59:18

Kabi be whenever there are two nested loops, we cannot assume the time complexity of

59:23

of square.

59:24

The outer loop, how many times it will run?

59:28

The outer loop, how many times?

59:32

N times, roughly.

59:35

N minus 1, basically n.

59:37

And the internal loop, how many times it will run?

59:41

Again, n times.

59:43

And that is the reason, because both the loops are running n into n times,

59:46

and that is the reason time complexity of O of n square.

59:50

Are we good here?

59:51

Now, you can perform some optimizations on this.

59:57

on this, that optimizations, I will leave it up to you.

1:0:04

Okay?

1:0:05

Think about what optimizations you can perform here.

1:0:08

The internal loop is actually we do not even have to run this n-1 times.

1:0:13

Because if you guys remember, we have to

1:0:16

two parts divided array.

1:0:18

One was sorted array, one was unsorted array.

1:0:21

So what if I run the loop only on the unsorted array of my

1:0:26

of my statement.

1:0:29

Okay, think about it and try to optimize this specific bubble sort.

1:0:35

Okay, let's take a break for 8 to 9 minutes.

1:0:38

Let us come back and let's start with the next question which is

1:0:42

selection sort.

1:0:45

No,

1:0:46

that generally coding languages there is a in-place sorting algorithm.

1:0:50

We always use that.

1:0:52

And that sorting algorithm very fast

1:0:54

and log n, probably n log in and or that's even more time complexity and run

1:0:58

it.

1:0:59

Okay?

1:1:00

We are this because we're going to

1:1:02

idea that's how swapping how to

1:1:04

we can't, how we can't

1:1:06

that is the reason we're putting.

1:1:08

Yes, Nisha, that's absolutely correct.

1:1:10

Okay, let us take a break.

1:1:12

Let's come back by 10 and

1:1:14

let's come back by 9, sorry.

1:1:16

And then let's start with selection sort.

1:1:19

Okay.

1:1:49

You know,

1:2:19

You know,

1:2:49

I'm

1:3:19

I'm

1:3:49

I'm

1:4:19

I'm

1:4:49

You

1:5:19

I'm

1:5:21

I'm

1:5:23

I'm

1:5:25

I'm

1:5:27

I'm

1:5:29

I'm

1:5:31

you

1:5:59

I'm

1:6:01

you

1:6:03

I'm

1:6:05

you

1:6:33

I'm

1:6:35

you

1:7:03

I'm

1:7:05

you

1:7:33

I'm

1:7:35

I'm

1:8:03

I'm

1:8:07

I'm

1:8:11

I'm

1:8:15

I'm

1:8:19

I'm

1:8:23

I'm

1:8:27

I'm

1:8:31

I'm

1:8:35

I'm

1:8:39

I'm

1:8:43

I'm

1:8:47

Thank you.

1:8:49

Thank you.

1:9:19

Thank you.

1:9:49

Thank you.

1:10:19

Thank you.

1:10:49

Okay, everyone, I'll be back.

1:11:04

Okay, everyone, I'll be back.

1:11:19

Yeah.

1:11:26

Cool.

1:11:29

So let's start.

1:11:30

I hope you guys are able to see my screen.

1:11:35

Take it.

1:11:38

Let's start with Selection Short.

1:11:49

Okay.

1:11:57

Now, the thing is, this is yet another type of sorting algorithm.

1:12:04

That means the output of bubble sort and selection sort, it will exactly remain the same.

1:12:12

Does everyone get that point?

1:12:15

Just this is another apple.

1:12:19

to sort the arrays in general.

1:12:24

So everyone might have played cards at some point in your life.

1:12:37

Most of the, if not everyone, that significantly people would have played cards, right?

1:12:45

Or at least you know about cards that, okay, what cards are.

1:12:48

are? Can I expect it? Okay. Now, the thing is how it is related to cards is because

1:13:02

I'll just, huh. So what happens is that, assume that we are playing cards and if I get these cards for, one,

1:13:18

three, two. If I get these cards. Okay? Now, it is one of the most easiest sorting

1:13:27

algorithms by intuition. Okay? This algorithm says that if these cards are sprayed in front of you and

1:13:36

you could pick only one card at a time. How would you basically arrange the cards in

1:13:45

sorted order. Anyone would like to answer that? If I ask you that, if you can pick only one

1:13:52

card at a time, which card you will pick to start with? Well, does everyone agree that I will pick

1:14:02

one and I will move one here? Correct? Okay, absolutely. Then what do you do? Then you do? Then you will

1:14:14

again start scanning the remaining set of cards, 4, 3 and 2 and again you are allowed to pick

1:14:22

only one card. What is something that you will do here? Which card you will pick? Which card you will pick?

1:14:31

2. Does everyone agree with me? Yes, yes. Two. I will mark 2 here. Okay. Done. You will again

1:14:40

scan the complete remaining set of cards in your hand.

1:14:44

And you will, you have the flexibility to pick up one card at time. What you will do now?

1:14:50

You will pick up the next card, which is 3. You will put 3 in another hand, something like this.

1:14:55

And the last time, you will basically check another card, which is 4. And you will put 4 here.

1:15:03

So this is something that we generally also do whenever we are playing cards.

1:15:10

That we like to sort the cards from one place to another place. Does everyone agree with?

1:15:14

me, right? This is the idea over which this sorting algorithm runs.

1:15:25

Okay? So the core idea here is that on every pass, okay, select the minimum element,

1:15:44

select the minimum element from the unsotted portion.

1:16:14

Okay. Does that make sense to everyone? So if I have to define the algorithm for this,

1:16:28

how would I do that?

1:16:36

First of all, is the idea clear to everyone? That is very important. If the idea is not clear, then we cannot move forward.

1:16:43

Any questions here? Now, the thing is, here we have assumed one thing, that this list that I have created, this is a new list.

1:17:01

But generally, in selection sort, what we do is we modify the existing list only.

1:17:08

We do not have the flexibility to create a new list. That is in selection sort, we do not have the flexibility to create a new list.

1:17:11

that is in selection sort. If I have two hands, this is my unsorted and this is my sorted. I do not have the flexibility to use this hand. I only have to swap the cards on this hand. Basically, if this is the card, swap it from here to here. If this is the card, swap it from here to here to here. This is the only way I can sort the cards. I do not have the flexibility to move card from one hand to another hand. Is that clear?

1:17:41

everyone. Are we compatible?

1:17:50

With that case, let me define the algorithm. Then we will do a dry run, followed by code linking. Okay.

1:17:59

So, assume that.

1:18:11

So step number two, scan the rest of the elements in the array and find the actual minimum element.

1:18:41

Okay, find the actual minimum element.

1:19:00

Then swap the actual minimum element with the element with the element at the current position.

1:19:11

Okay. Now, now, now, now?

1:19:41

Basically, repeat this until you have done the complete steps.

1:20:01

Okay. Now, when you see the algorithm, it may feel like, yes, it's a little up uproper's.

1:20:07

Okay. Okay. Let's take one.

1:20:11

For example, let's do one dry run. And then we

1:20:15

we understand that this algorithm actually

1:20:17

come, how is doing? Make sense?

1:20:21

Okay? So, if I take this algorithm, if I

1:20:25

same array, if I take, if I same array, 51428,

1:20:41

According to this algorithm, what will? I have this array.

1:20:53

According to this algorithm, what will?

1:20:55

We?

1:20:56

We, the minimum, we have a column,

1:21:08

Let me create a column,

1:21:10

minimum, and then action. And then finally, and then finally, array after as well.

1:21:25

Okay. Now if you see this array, what is a minimum value here?

1:21:39

Minimum value what is?

1:21:42

1, correct?

1:21:46

And we assumed what

1:21:49

what?

1:21:51

What we assumed what?

1:21:53

minimum value?

1:21:54

What the first element?

1:21:56

Correct?

1:21:57

The first element?

1:21:58

So we assumed that this is that

1:21:59

this minimum is, but actual minimum is this is this is.

1:22:02

Does everyone agree?

1:22:03

So minimum is

1:22:05

1, index 1.

1:22:07

Can I say that?

1:22:08

say that? Does everyone agree? What I will do? Swap index 0 with 1. I will have to do this.

1:22:21

Does everyone agree with me here? I will have to do this. Swap index with 0 and 1. Correct.

1:22:28

So after swapping, my array would look like 1, 5, 4, 2, 8. So of

1:22:38

what you got? After swapping, my array would look like this.

1:22:44

Okay?

1:22:45

This is our first iteration.

1:22:49

Now let's discuss on the second iteration.

1:22:53

Okay.

1:22:54

Now my second iteration will be on this 5-4-28.

1:23:08

1 is already sorted. So I will not count it. Okay?

1:23:13

Now, here,

1:23:15

I assume what I have my minimum what should?

1:23:19

In this case, I assume what my minimum what should?

1:23:24

This value is already sorted, so I will not count this.

1:23:28

Now this is the array that I have.

1:23:30

Assume that this is the array.

1:23:32

So what?

1:23:33

I assume what my minimum what should?

1:23:36

The first element.

1:23:37

Right?

1:23:39

Algonism has what you said?

1:23:41

Assume first element is your current minimum.

1:23:44

You will assume.

1:23:45

Then you actual minimum to find.

1:23:48

So, if I ask you, 0, 1, 2, 3, 4.

1:23:55

Which index I will assume as the current minimum?

1:23:59

1.

1:24:00

Now, all of all of the right?

1:24:02

So this is my assumption that this is my current minimum.

1:24:06

Okay.

1:24:07

But what will be the actual minimum?

1:24:11

What is the actual minimum value here?

1:24:14

2. Right? So 2 is the actual minimum.

1:24:19

Index 3.

1:24:26

So I will swap index 1 and 3.

1:24:30

Do you?

1:24:31

Do you all understand?

1:24:37

Is everyone clear?

1:24:41

I will swap the values between 1 and 3.

1:24:44

After swapping, how my array would look like?

1:24:46

1.2, 4, 5, 8.

1:24:54

So this part of my array is sorted and this part of my array is not sorted.

1:25:03

Everyone comfortable?

1:25:06

Right, guys? Yes, no. Pucka.

1:25:13

In the next part, what will happen?

1:25:16

I will use the same array.

1:25:20

One, two, four, five, eight.

1:25:30

01,1, 2, 4, 3, 4.

1:25:34

Now, between my unsorted part,

1:25:36

what is the minimum value?

1:25:39

What is the minimum value?

1:25:42

My unsorted part in the minimum value?

1:25:44

What will be?

1:25:46

4.

1:25:49

What is?

1:25:51

2.

1:25:52

Shreya, what is what is?

1:25:54

What is?

1:25:55

Any specific thing that you did not understood or

1:25:58

what else?

1:26:00

Any specific thing that I can help you with?

1:26:05

you with?

1:26:06

Models.

1:26:07

Models?

1:26:08

Models, what I did not got to you, Shreya?

1:26:12

What do you mean by models?

1:26:17

Okay, make by dry run, through, quickly?

1:26:19

With that help?

1:26:20

Shreya?

1:26:21

Okay, guys, please, please,

1:26:24

dhya.

1:26:25

Okay, I will do one last time from start.

1:26:28

We will start with this line.

1:26:41

I have this array.

1:26:44

This algorithm says, in your unsorted array, whatever is the first value, assume that that is the current minimum.

1:26:57

Assume it.

1:26:58

So, this is my current minimum.

1:27:00

Does everyone agree?

1:27:01

I will assume that my this is the value is my current minimum.

1:27:05

It can it is the right.

1:27:07

Okay?

1:27:08

Shreya, clear here.

1:27:11

But what is the actual minimum here?

1:27:14

If you my array completely look, then what value is my actual minimum value?

1:27:19

1, right?

1:27:22

So, 1 is my actual minimum.

1:27:25

But I assumed that was 5 was.

1:27:27

So, do actual minimum my 5 is my 5 is my actual minimum smaller than the 5?

1:27:38

Yes or no?

1:27:44

No.

1:27:45

Why?

1:27:46

Actual minimum is 1.

1:27:48

What I assumed is 5.

1:27:51

So the actual minimum is smaller.

1:27:53

Okay?

1:27:54

So what is something that I will have to do?

1:27:56

have to do?

1:27:57

458.

1:27:58

4.58?

1:28:00

Where from?

1:28:01

Saojania?

1:28:02

We are discussing this, the first iteration.

1:28:04

We are discussing the first iteration.

1:28:06

Everyone, please focus here only.

1:28:10

Okay?

1:28:11

Okay.

1:28:12

So, one is my smallest value.

1:28:16

I will have to move one to my left.

1:28:18

Can I, can everyone say that?

1:28:21

I will pick up the card number one and I will put it on the other side.

1:28:25

Does everyone agree?

1:28:26

So what I will do?

1:28:28

I will swap this with the current minimum.

1:28:32

And after swapping, this is how my array would look like.

1:28:36

Yes, you know, 5-428.

1:28:39

4-2-8 is untouched because obvious reasons.

1:28:42

Okay?

1:28:43

Now I will consider this as my next array.

1:28:48

Okay?

1:28:50

In my next array, there are two subparts.

1:28:53

One which is sorted.

1:28:55

One.

1:28:56

which is sorted and one which is not sorted.

1:28:58

So in my unsorted array,

1:29:02

the first value I will assume it to be

1:29:07

the first value is assume to be current minimum.

1:29:11

Is this clear?

1:29:13

And what is my actual minimum? Can anyone please tell me?

1:29:17

What is my actual minimum?

1:29:20

2.

1:29:21

Is my actual minimum smaller than the assumed minimum?

1:29:26

Yes, absolutely. Correct.

1:29:30

Are Huanchu ha ha.

1:29:32

Actual minimum is smaller than the current minimum, right?

1:29:36

Okay, everyone? Actual minimum is 2.

1:29:41

Current assumed minimum is 5. It is smaller.

1:29:45

So I will have to swap the two values.

1:29:47

So what I will do?

1:29:48

I will swap the two values and after swapping my array would look something like this.

1:29:53

Does everyone agree?

1:29:55

Okay, now I am unsure that my second part of the array is sorted or not sorted.

1:30:03

Coincidentally, in this case, it seems to be sorted, but unless and until I have executed my code completely, I am not sure.

1:30:12

So for now, I will assume that my current part, the right part is not sorted.

1:30:16

So now, this is the sorted array, this is the not sorted array for a moment.

1:30:23

I will assume that the different part.

1:30:24

I will assume that the first element of my unsorted array is current minimum.

1:30:29

And what is the actual minimum here?

1:30:33

What is the actual minimum here?

1:30:36

Actual minimum is 4 with index 2.

1:30:42

Can I say that?

1:30:44

So is my actual minimum less than current minimum?

1:30:52

Is my actual minimum less than the current minimum?

1:30:57

No.

1:30:58

That means it is already at the right place.

1:31:02

So no need to swim.

1:31:10

1.2, 4, 5, 8.

1:31:15

Is this clear?

1:31:21

everyone?

1:31:23

Similarly, I will check again, one, two, four, five, eight.

1:31:35

In my right array, I will assume that this is my current minimum.

1:31:41

What is the actual minimum?

1:31:44

Actual minimum with index 3, value 5.

1:31:49

Is my actual minimum?

1:31:50

Is my actual minimum?

1:31:51

smaller than the current minimum?

1:31:53

It is not.

1:31:55

So it is already at the right place.

1:31:57

That means this one, two, four, five is sorted.

1:32:02

And similarly, I will check for last.

1:32:05

So basically, this is how you one by one pick up the elements and you swap them.

1:32:11

Kya's what you all of the

1:32:15

all of them?

1:32:18

Okay.

1:32:20

Okay, now what is a change that has happened here?

1:32:25

Bubble sort me, we were moving the larger elements in the last, right?

1:32:31

Gradually, we were moving the larger elements towards the last.

1:32:35

In selection sort, we are actually what doing, we are finding out the minimum element and putting it on the left.

1:32:44

Correct, putting it on the left.

1:32:48

Does everyone agree with me?

1:32:49

Right?

1:32:51

Okay.

1:32:53

So with this case, let's start with thinking on the code part.

1:32:58

So I'll start sharing my screen.

1:33:00

So it will start sharing my screen.

1:33:03

Sought on it will be alteration. Yes, Prashant.

1:33:07

Okay?

1:33:08

Because your code is not know that it is sort has.

1:33:11

Okay?

1:33:12

So iteration to it will be.

1:33:14

Okay.

1:33:17

Okay.

1:33:18

Okay.

1:33:19

they are also applicable to strings.

1:33:25

Absolutely.

1:33:26

They are applicable to strings also.

1:33:28

Okay.

1:33:29

So, if I'm going to write a code to,

1:33:31

what I can start with a function?

1:33:33

Can I?

1:33:35

Everyone.

1:33:38

What I will do?

1:33:40

Def.

1:33:42

Selection sort.

1:33:47

A.R.

1:33:48

right?

1:33:55

No, there is no specification.

1:34:01

Okay, San Yankah.

1:34:02

Okay.

1:34:03

Now, because the length of the array is not given, what I will do?

1:34:07

N equals to Lenn of array.

1:34:10

Because eventually I have to iterate over my array completely.

1:34:15

Can I say that?

1:34:17

Eventually, I've got to iterate

1:34:20

so I will have to find out the length.

1:34:22

Does everyone agree with me?

1:34:25

Okay, then what will I do?

1:34:27

For I in range 0 to n minus 1.

1:34:33

N minus 1?

1:34:34

Why did I?

1:34:35

Are we clear on this?

1:34:39

Are we clear on this?

1:34:40

I have a minus 1?

1:34:42

Now I will do, I will assume that my current value is smaller.

1:34:46

So, min assume equals to I.

1:34:51

I.

1:34:52

I assumed that the current index is smaller value.

1:34:58

But at the end of the day it can happen that my assumption is wrong or my assumption is right.

1:35:06

Okay?

1:35:07

Now what I will do?

1:35:08

I will scan the remaining elements in the list.

1:35:12

Okay.

1:35:16

Okay, how do I scan the remaining elements in the list?

1:35:20

I am assuming the index halvin.

1:35:22

Okay, this is the index.

1:35:23

Not the value, this is index.

1:35:26

Okay.

1:35:28

How do I scan the remaining elements on the list?

1:35:31

Anyone can answer that question please?

1:35:34

Now, I'm going to be able to iterate

1:35:37

that means 1, 2, 3, 4, 5.

1:35:39

I assume that this is my current minimum.

1:35:42

I have to start my iteration on this, 2, 3, 4, 5.

1:35:45

So what?

1:35:46

what will I do?

1:35:47

For J in range, I plus 1 to n.

1:35:53

Can I say that?

1:35:54

What do you guys think?

1:36:04

If my I is 0th index, then my J will start from 2.

1:36:08

If my J is 0th index, then my the next will start from J plus 1.

1:36:13

What do you guys all have?

1:36:15

everyone comfortable?

1:36:17

Okay

1:36:31

Okay

1:36:35

Now what I will do here?

1:36:38

If my array of J

1:36:43

is less than array of min-assume.

1:36:51

If my current element

1:36:54

my minimum assumed index is

1:36:57

then what do you have to do?

1:36:59

What do?

1:37:01

I will have to tell that my minimum

1:37:07

assumed index was actually J.

1:37:10

Do you?

1:37:11

I got to say,

1:37:12

I'm going to say that I was the

1:37:15

actual minimum.

1:37:16

Can everyone agree with me?

1:37:17

Okay.

1:37:18

Now what I have to do?

1:37:31

I have to swap also.

1:37:32

So if Min assume is not equals to I, then what I will do?

1:37:40

Then in that case, I will swap of I with ARR of Min assume equals to

1:37:48

A.R of men assumed with A.R.R. of I.

1:37:54

And finally, I will return.

1:37:58

Is,

1:37:59

Are we good here?

1:38:01

Are we good here?

1:38:09

100%

1:38:16

all of them all

1:38:19

938.

1:38:24

Okay.

1:38:25

So,

1:38:27

I assumed this is my current.

1:38:30

Okay, this is the star is

1:38:34

I assumed that this is my current

1:38:36

Shreans. Okay. Actually, let me take the same example again so that we are able to relate with that. What was that example? 514 to it. Okay.

1:38:48

So initially I assume that this will be my minimum. Correct. Right, Shrean's. But what was my actual minimum? This value.

1:38:58

So me, my code in this

1:39:00

this is the actual minimum. Correct. Does everyone agree?

1:39:06

and once I find out that this is the actual minimum, I will check that,

1:39:12

what I am I that is the

1:39:14

minimum assume,

1:39:16

if that is not

1:39:18

in that case, my assumption is wrong.

1:39:21

Can I say that?

1:39:22

If minimum assume is not equals to I, which I assigned it here,

1:39:30

if that is the case, then can I say that my assumption was wrong?

1:39:34

Do you all of them?

1:39:45

Everyone?

1:39:50

Guys, yes, no.

1:39:54

Okay?

1:39:57

In that case, I will have to swap.

1:39:59

Swap's logic we've already

1:40:00

have to have to have.

1:40:01

So there is no problem with that.

1:40:02

Okay?

1:40:03

Once we have this code run and look

1:40:05

it, it's going, or not it?

1:40:07

Okay?

1:40:08

So I will, what I will do?

1:40:09

I will comment this.

1:40:11

I will write sorted ARR equals to selection sort of error.

1:40:17

Okay, let's run the code and see whether this works.

1:40:20

One, two, four, five, eight.

1:40:22

Okay.

1:40:23

There is a question from people that yes, why you have not used n minus one here?

1:40:26

This is an minus one?

1:40:28

Or if we'll look, or not?

1:40:30

It's all right.

1:40:31

I think you can use n minus one.

1:40:32

It's completely fine.

1:40:33

Okay?

1:40:34

I made it.

1:40:35

I missed it.

1:40:36

But you can use n minus n and it's completely fine.

1:40:38

Okay.

1:40:39

Is everyone comfortable?

1:40:40

Line number 39 already repeated min assumed to j.

1:40:53

Why?

1:40:55

How will my code know alvin that my minimum assumption was wrong?

1:41:01

And that is the reason I will have to

1:41:02

I will have to minimum assign the value to J.

1:41:06

So that I can check it later that was my assumption right?

1:41:10

If my assumption was right, then this code will not execute.

1:41:14

Line number 39 will not execute.

1:41:17

Correct?

1:41:19

Right, Alvin?

1:41:22

If my assumption was wrong, then this line number 39 will execute.

1:41:27

And I will check it here that, okay, was my assumption right or now?

1:41:31

If it was.

1:41:32

right? No need to serve. If it was wrong, then you need to serve. Okay? So let me add a print

1:41:38

statement here. My ARR of J. Arr of J. Arr of J. Arr of men assume. Okay? Now let's see what happened.

1:42:02

So error of j is 5 and I assume the value is 5.

1:42:07

Is that the value is 5?

1:42:23

Is that clear to everyone?

1:42:32

Now, if I talk about the time complexity here, what will be the time complexity?

1:42:43

What will be the time complexity?

1:42:46

Any thoughts?

1:42:48

Think, take your time and tell me.

1:42:53

It will be O of n square.

1:42:59

Why?

1:43:00

The outer algorithm almost runs for n times.

1:43:03

Almost.

1:43:04

It is n minus 1.

1:43:05

Actually it is n.

1:43:06

The internal one almost runs for n times.

1:43:10

Okay?

1:43:11

When the input becomes very large, like 10 million records,

1:43:14

so minus 1

1:43:15

can't do that more benefit

1:43:16

does everyone agree?

1:43:18

10 million versus 10 million minus 1.

1:43:22

No.

1:43:23

And that is the reason we are saying that it will be n-square.

1:43:26

Now there can be a very valid question.

1:43:28

That yes, that if bubble sort and selection sort, both of them are n-square.

1:43:33

Then why would you prefer one over the other?

1:43:36

See.

1:43:38

A very, you know, sophisticated answer for that should be,

1:43:42

bubble sort, if you remember, we in bubble-sort

1:43:46

in an array in push-carra he, bubble-kruhe

1:43:48

elements towards the last.

1:43:50

Do you guys remember that?

1:43:52

We're bubble doing the elements towards the last.

1:43:56

So, if you know, already array sorted is already array sorted is,

1:44:01

if already are sorted,

1:44:04

then my bubble sort will terminate early on the nearly sorted data.

1:44:10

Because already all elements sorted are.

1:44:13

But selection sort what will?

1:44:15

For the selection sort for every element for

1:44:17

an assume a minimum value and one find out the actual minimum.

1:44:21

minimum.

1:44:23

And then he basically check

1:44:26

that for every assumed minimum is my actual minimum is smaller or not.

1:44:34

Okay?

1:44:39

So the thing is, generally between these two,

1:44:44

bubble sort performs better.

1:44:50

If I talk about space complexity,

1:44:54

do I here,

1:44:55

any extra space use are I am I using any extra space in bubble sort

1:45:01

or in selection sort?

1:45:07

No.

1:45:08

That means even if my input increases by 10 million,

1:45:12

will my space increase by 10 million?

1:45:15

Will my space increase in accordance to that?

1:45:19

No.

1:45:20

Does everyone agree with that?

1:45:21

And that is the reason.

1:45:22

Can I say that my space is constant here?

1:45:27

Can I say that my space is constant?

1:45:29

Does everyone agree with me?

1:45:33

Yeah.

1:45:34

Cool.

1:45:35

So the space complexity for bubble sort and selection sort is O of 1,

1:45:41

while the space complexity is the time complexity is,

1:45:46

worst case, O of M square.

1:45:48

Does everyone agree?

1:45:49

Okay, so I'll just open a sheet.

1:46:00

Allow me a minute.

1:46:03

Okay, let me start sharing my screen one more time.

1:46:13

I need to just...

1:46:15

I'll share the quotes.

1:46:16

Don't worry, I'll say the quotes.

1:46:18

Okay.

1:46:19

sheets.

1:46:20

Okay?

1:46:23

So in today's class we have

1:46:28

bubble sort and selection sort

1:46:31

how to do it.

1:46:33

Then we have it implemented

1:46:34

Bha

1:46:35

B.

1:46:36

Right?

1:46:37

Then we

1:46:39

that algorithm

1:46:40

execution to dry run

1:46:41

on sample error.

1:46:42

Can everyone agree with me?

1:46:47

Right?

1:46:48

and we have their time complexity

1:46:50

analyzed,

1:46:51

everyone agrees with me on this?

1:46:53

Okay?

1:46:54

Okay?

1:46:55

In the last class, I think I

1:46:58

think I'll just do it right now.

1:47:01

We've defined functions.

1:47:02

How do you define functions using dev keyword in Python?

1:47:07

Right?

1:47:08

Then we have arguments how to pass in functions?

1:47:11

We've seen that we've seen that.

1:47:13

Then how I can call multiple functions within one function?

1:47:17

We've seen that.

1:47:18

function from one function, the other function

1:47:20

the third function.

1:47:21

We've seen that.

1:47:22

And at the end of the day,

1:47:24

we've seen that we actually

1:47:26

function use

1:47:28

to do

1:47:29

if I'm

1:47:30

repetitive code to

1:47:32

a place to

1:47:33

use them to reuse

1:47:34

so I can use my functions.

1:47:36

Does everyone agree?

1:47:38

Right?

1:47:40

In fact,

1:47:41

if I

1:47:42

this one

1:47:44

quote,

1:47:45

can actually I call

1:47:47

I call sorted selection sort on some other array here, array 2 without writing

1:47:57

the code of selection sort one more time.

1:48:01

Can I do that?

1:48:03

And this is actually a benefit of functions.

1:48:07

Does everyone agree?

1:48:17

Okay, so I'll just provide you the code.

1:48:22

That is for internal use case, Devere.

1:48:47

Okay, can everyone please confirm that you

1:48:51

are able to see the code?

1:48:54

Everyone?

1:49:02

Okay.

1:49:04

With that note,

1:49:07

I think that's it from my side.

1:49:09

I hope everyone

1:49:11

enjoyed the session.

1:49:14

Thank you,

1:49:15

everyone.

1:49:16

I hope everyone enjoyed the session.

1:49:18

Have a good weekend.

1:49:20

Let's meet on next Thursday.

1:49:23

I'll just hand over the session to Vijay now.

1:49:26

Thank you, everyone. Have a good day.

1:49:28

Bye.

1:49:29

We have good to you.

1:49:31

Okay, thank you.

1:49:34

We can start with the quiz.

1:49:36

Let me share my screen.

1:49:46

Yeah, so you can scan this QR code

1:49:49

or directly go to the website and pass the code.

1:49:51

Just do a thumbs up here once you will join.

1:50:07

I will wait for 30 seconds more.

1:50:16

Okay, last 10 seconds.

1:50:28

Okay, let's 10 seconds.

1:50:32

Okay, uh, let's start the quiz.

1:50:39

Okay, so first question.

1:50:45

Okay.

1:50:46

Okay.

1:50:48

Great, like most of the students have answered it correctly.

1:51:15

Let's see.

1:51:16

have given the answer like first.

1:51:24

Okay, yes seems to be on the top.

1:51:28

Let's move to the next question.

1:51:34

Second question in front of your screen.

1:51:46

Okay. Why at the beginning, middle or unknown? Like in the bubble sort, like it was clear in the session, right? Like it will be going to be at the end after the first pass. Let's see.

1:52:16

Again, EJ seems to be on the top.

1:52:21

Let's move to the next question. Just do a thumbs up here post. You will answer it.

1:52:26

Yeah, third question in front of your screen.

1:52:46

Okay. Fine.

1:52:57

Okay.

1:53:02

Nishanti is at the top. Elvin have given the fastest answer. Let's move to the next question. Just do a thumbs up post providing the answer. So you will be redirected to the next question.

1:53:15

Oh.

1:53:45

is changing like multiple times now she says is at the top let's see who will

1:53:50

will fix this quiz final question this one is a easier question this one is a easier question

1:54:15

Okay, for these two like, like a lot of students have given order of one, order of an order of any square, right, like for both bubble sort and selection sort.

1:54:31

Let's see who is at the top in the leaderboard.

1:54:34

Oh, today I think like in each question the winner is getting updated.

1:54:41

Okay, so final winner is Rohit.

1:54:44

Yeah.

1:54:45

Let me launch the feedback ball. So all of you will see the feedback questions in front of your zoom screen. So just provide the feedback we are done for today. Feel free to drop up after it.

1:55:15

Okay, only 50% students have provided the feedback.

1:55:45

Fine, got the feedback from everyone.

1:55:51

Thank you, thanks everyone.