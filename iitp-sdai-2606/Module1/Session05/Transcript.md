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

Okay.

23:47

Hello, hi everyone.

23:49

Good evening.

23:50

Hello, hello, good evening.

23:54

Am I audible?

23:56

Namaste, good evening.

24:00

I hope everyone is doing fine.

24:03

Nice.

24:08

Okay, how was the last week for everyone?

24:12

Nice.

24:19

Cool.

24:20

Good to hear about it.

24:22

Okay.

24:23

So let's start with today's session.

24:26

Welcome to today's session.

24:28

We'll start with dictionaries and hash maps in Python.

24:33

Okay.

24:35

What are dictionaries?

24:36

What are hash maps?

24:37

Very, very interesting topic to cover.

24:41

Okay.

24:42

We'll start with that. We'll start with understanding the problem, what are dictionaries.

24:48

Then we will see some methods by default built-in methods which we can use from Python for dictionaries.

24:57

Then we'll write some code so that we get our hand dirty on them.

25:02

Then we will see what are hash maps.

25:04

And we will try to understand that, okay, is there any difference between dictionaries and hash maps or are they the same thing for Python?

25:11

That's the pretty pack agenda for the day.

25:15

Okay. And with that note, let's get started. So a quick revision time from the last session.

25:24

Can anyone tell me please what did we covered in the last session?

25:29

List. Okay, what about lists? What are lists?

25:40

What are lists? What did we discussed about lists?

25:46

That they are collection of multiple values. Am I correct?

25:51

Collection of items? Absolutely correct.

25:55

Okay. Is that a collection of same data type or there can be multiple data types involved?

26:01

There can be multiple data types involved.

26:07

And that is very specific to Python, I would say.

26:09

I would say. In other languages, in Java for example, C++ for example, a list can have a single data type only.

26:18

But we are based on anyways, we are discussing Python, so we'll stick to Python.

26:23

Okay.

26:24

Then what did we discovered about list?

26:26

There was something interesting.

26:28

I think it was related to indexing if I'm correct.

26:31

That even though whatever values you add in the list, the indexing would all

26:39

start from 0. Am I correct there?

26:46

So indexing will always start from 0.

26:49

That means, can I say that the last index will always be the number of elements minus 1?

26:56

The last index will always be number of elements minus 1.

27:02

And what would happen if you access extra index as in a number of elements minus 1?

27:08

as in an incorrect index, what would happen?

27:14

It will give you an error.

27:16

Okay, awesome.

27:18

And can you iterate on lists?

27:21

Like, how do you iterate on lists?

27:23

Can anyone please tell me?

27:26

If I ask you to print 50 elements of a list,

27:31

like all the elements of the list, not 50, all the elements of a list,

27:34

how do you do that?

27:36

Either you use a far loop,

27:37

a far loop or if the question basically is that, okay, get me the top three elements, get me the last three elements, then you use something called as slicing, right?

27:47

What is slicing? Slicing is basically you create a sub-list from the main list, and that is called slicing.

27:56

Now that sub-list can be created in any logic.

28:01

For example, I want alternate elements, I want first five elements, I want first five elements, I want

28:07

last five elements, I just want the first element, I just want the last element, it can be any logic.

28:13

Depend on what you are passing in the parameter for slice.

28:18

Here, everyone clear?

28:22

I think we have this all in the last class.

28:26

Okay, okay.

28:28

So with this context, let's start with today's session.

28:32

Today we start with Dictionaries.

28:35

Okay? Now, what about Dictionaryce? Okay. Now, assume that, if I have a phone book of one, 10,000 contacts.

29:05

And if I ask you to get me yeshs number, how would you do?

29:20

How would you do it?

29:24

There are 10,000 contacts in your phone book, which is the hard phone book.

29:33

I'm not talking about your phone book.

29:34

phone book, I'm talking about the paper-wala phone book. Now if I ask you to find that tell me

29:41

yesh's number. Ah, directory. How would you do it? You can search it, okay? How will you search it?

29:53

Approach number one is you will start by one. You will start by one.

30:04

That okay, I will start with from the very first contact and I will go till the last.

30:09

If there are 10,000 contacts, probably I may get yes towards the last because my name starts with why.

30:17

So I will already scan now 9,000 contacts and probably somewhere between 9 to 10,000 you will get my number.

30:24

Okay, so you start one by one.

30:34

sounds fine to me, but there is still a problem. What is a problem here? In the worst

30:40

case, you will still check 10,000 contacts. Am I correct? In the worst case,

30:47

because you are not sure whether that number would lie. Assume that there is no dictionary,

30:52

there is nothing. So in the worst case, what would happen? You will have to scan all the 10,000

30:57

names. Okay, and this would take definitely hours for you as a human being. Am I correct?

31:04

Definitely it will take hours for us to do it.

31:09

Yeah, this is problem.

31:11

Okay.

31:12

Now if I give you a list, assume that I ask you to write a computer program for it where there is a list given to you of 10,000 people.

31:21

Then what would you do?

31:23

You will run a for loop from I equals to 0, from I in range 0 to size, and then you will start matching the values.

31:33

In this case also, it is just that now you are doing it via code.

31:38

So your code will do the work for you, but still you will do 10,000 searches in the worst case.

31:45

Does everyone agree?

31:47

Right? And this seems out to be a problem.

31:51

As of now, it is 10,000. Can it happen the number is 10 lakh?

31:56

Can it happen the number is 1CR? For example, a city like Mumbai.

32:00

Definitely you will get 1CR people there.

32:02

CR people there.

32:03

Right?

32:04

For a city like Delhi, you will get 2 CR people.

32:07

So will you run your 4 loop for 1,000 or 10 kore people?

32:11

No, yes.

32:12

That does not sound right.

32:14

I mean, that code will take days.

32:18

My code also will take some time, like hours or days for me to return the output in that.

32:23

I cannot wait till that.

32:25

And that is not the right usage.

32:29

Approach number two.

32:32

Any thoughts, what you can do?

32:38

What is a better way?

32:40

You can use binary search.

32:42

Okay, that's fine.

32:43

We'll not discuss about binary search because it is a DSA specific topic and many people,

32:47

many among us may not be aware about DSA.

32:50

Logically, what will you do?

32:52

If I give you a hard discovery, how do you do?

32:55

Okay.

32:56

If I ask you to, I just tell you that, okay guys, I live in Indoor.

33:01

live in Indoor come visit my house and some of you really take it up and you want to

33:06

visit my house I haven't told you my house number I haven't told you my address so

33:12

will you search each and every house in Indore to find me probably yes because you

33:16

are so you're so desperate to beat me so you will search each and every house but is

33:22

that wise no that is not wise instead what is better that there

33:31

is an address that I give to you, you directly come to that address.

33:36

You know that, okay, this is the address of yes and I will find yes here definitely.

33:41

Now, will that save your time, will that save your effort?

33:46

What do you guys think?

33:46

Does everyone agree?

33:48

So what we are doing is instead of, you know, now what there is a mapping created that Yash is

33:56

living on at this address.

33:58

So this is the address and this is the person.

34:01

So this is a mapping that which is getting created. Can I say that? Can I say that?

34:08

Can I say that? Right? So what is the second approach that you store the mapping?

34:15

That means this is the phone number and this is the name. Right? So you search here that okay.

34:30

You search here. Where is yesh? And this is the number of yesh. You directly use this number. Does that make sense?

34:44

Everyone agree with me? Okay. So this is what dictionaries are used for in code. What is a dictionary? The key idea here is. Dictionary is a data structure. For example, list is a data structure, right? Which is

35:00

helping you to store the data.

35:02

Right?

35:03

Similarly, list is a data structure which helps you to store key value pairs.

35:10

Key value pair storage.

35:22

Now when I say key value, what do I actually mean here?

35:27

Let's try to discuss that.

35:29

that. Okay? For example, when I say I want to create a list, list will store some values here.

35:42

At index 0, at index 1, at index 2 and so on. This is a list. This is how you create a list.

35:50

Now, the key is a dictionary stores the items by key and a value.

35:57

A dictionary stores the items in the code by key and value.

36:04

For example, this is an individual entry in list. Can I say that?

36:10

This two is an individual entry. 0 is an individual entry. Can I say that?

36:15

Everyone agree? These are individual numbers in the list.

36:18

Every item is an individual entry in the list.

36:21

Similarly, in your dictionaries,

36:26

What are individual entries?

36:33

The individual entry is defined by a key and a value.

36:38

That this is the key and a value.

36:42

Okay?

36:43

So it is a pair in dictionary always.

36:46

Everyone comfortable?

36:48

For example, if I want to create a list of scores for students, how would I do that?

36:54

Scores.

36:55

equals to list 80, 90, 100.

37:03

Okay? Now, as of now, can I say that this specific score is for what student?

37:13

Can I say that? Do I have that information in the list?

37:16

That okay, this 85 is a score of yesh.

37:19

90 is a score of Spuniti. Can I say that?

37:22

I cannot say that.

37:23

Because it is an individual.

37:24

it is an individual value.

37:26

And if I print this score, 80 will be printed.

37:36

Does everyone agree?

37:39

Now when I compare this to a dictionary, what will happen?

37:43

Dictionary scores.

37:46

I will store a mapping now.

37:49

For example, now here you use a curly braces.

37:53

Yes, score 85.

38:00

Then comma.

38:02

The next person, Himanshu.

38:07

Score 90.

38:12

The next person, Smriti.

38:15

Score 100.

38:19

And then close the curly braces.

38:22

Now what represents an individual entry here?

38:25

This complete record represents an individual entry because it is a key and a value.

38:36

Is this clear to everyone?

38:40

Okay.

38:41

And if now I want to print the value of Ravi, what is not clear Abhisheek?

38:50

What is not clear here?

38:51

Can you please tell?

38:53

Difference between?

38:57

Difference, what is not clear in difference?

39:00

Yes, yes, pointing to 85, correct.

39:03

List and dictionary.

39:05

List stores individual entries.

39:07

Abhishek.

39:08

This is you have you?

39:10

For example, list in, you can you

39:12

can store single value, right?

39:14

Single as in multiple values but all the entries are independent to each other.

39:18

Dictionary in a map.

39:20

as a mapping store key value pair.

39:23

For example, you can say that for Yash, I will store value 85.

39:29

Mapping means mapping, how do I explain you mapping?

39:33

Mapping means...

39:35

Hey, rar.

39:38

Okay.

39:39

Can I say that if two values are associated to each other?

39:45

For example, in your phone book, in your mobile,

39:49

your mobile? Right? Abyshek?

39:52

Your mobile in your phone book.

39:54

So, do you search numbers in your phone book via number or via names?

40:01

You search it via names because name is easy to remember, am I correct?

40:05

But when you click on name, does that number also comes up?

40:10

That, huh, for your papa, this is the number.

40:12

For your mummy, this is the number, right?

40:14

Correct.

40:15

So that is a mapping.

40:17

That for papa, this is my number.

40:18

For mommy.

40:19

this is number for yes, this is the number, that is a mapping.

40:22

Correct?

40:23

So if you want to store this kind of mapping where one value is related to other value,

40:29

then you will have to use a key value pair data structure, which is called as dictionary.

40:35

Make sense?

40:37

Okay.

40:38

Now, if I want to print a value here, how do I print?

40:42

print, print of scores

40:49

scores of yes what will be the output anyone

40:56

what will be the output here? Output will be 85

41:01

Everyone agrees with me on this

41:05

Okay, so syntax

41:13

Okay, if you want to create a dictionary in Python how do you do it?

41:18

you do it? The syntax is you write the variable name student.

41:22

Assume that I want to store all the details about a student, all the details, as in the name of the

41:31

student, the age of the student and the marks of the student. I want to store these three things.

41:38

So how will I do it? I will create a dictionary.

41:41

I will have a key here which is which will be called as name.

41:48

Because name is a string, I will have to represent it in a text.

41:53

Age, again a string, I will represent in a text.

41:58

Marks, again a string, I will represent it in a text.

42:03

Now coming to the value part.

42:05

Name will be a string, so I will write here yesh inside the text.

42:10

Then age.

42:13

Will age be an integer or a string here?

42:17

Will age be a integer or a string here?

42:18

be a string or integer? What do you guys think?

42:20

Int? So I will write here 29, for example.

42:24

And marks, it can be integer again.

42:29

So I will write here 86.

42:34

Okay, so if I say how many keys are there in my dictionary student?

42:40

Three keys, key number one, and value number one,

42:45

key number two, and value number two, and value number two.

42:47

and value number two?

42:49

Key number three and value number three.

42:52

Is this clear to everyone?

42:54

Okay, so a very important thing is you should be using curly braces here.

43:04

Okay, you should be using curly braces here.

43:08

Okay, each pair is represented by key and value.

43:13

Pairs are separated by commas. For example, pair one.

43:16

pair one, comma pair two, comma pair three. And the last pair because it is the last one,

43:21

you do not have to give a comma there, obviously. Now there is one very important thing that you

43:27

should, yeah, curly braces are must. There is one very important thing that you should note for

43:33

dictionaries. In dictionaries, keys should be unique.

43:46

and values can repeat.

43:53

Okay.

43:59

So Q, any thoughts? Any thoughts?

44:07

Any thoughts?

44:10

So, if I create a dictionary with same keys, what is going to happen, yes?

44:24

Assume that I create name again.

44:40

duplicated value? Is there a key with a duplicated? Is there a duplicated key, first of all? In this, is there, yes, there is a name which is duplicated. Now, how will computer know that actual name is yes or actual name is Aman? So what will your code do is whatever is the latest value of the key, it will honor that. So it will actually discard this value.

45:10

It will not give you an error. Instead, it will update it to whatever is the latest value.

45:20

Does that make sense? So even though, even though you think that, okay, I have four keys, no, actually, you only have three keys in your dictionary.

45:30

Does that make sense? Because logically also, assume that you are finding an address for yash and you find two yushes. How do you find two yushes? How do you know?

45:40

what I said is that there cannot be duplicate in the keys in dictionary.

45:49

That's it.

45:51

Keyes should always, always be unique.

45:55

So whenever you are creating a dictionary, you have to be really careful that keys should always be unique and the values can repeat.

46:05

I am fine with the values repeat, but the key should be unique.

46:09

Does that make sense?

46:10

to everyone.

46:11

Discard as in it will ignore that.

46:20

Assume that you have given a new key with the same value as in a new similar key, then it will

46:28

honor the whatever is the latest value.

46:30

All key must be unique.

46:32

In fact, we will see that example.

46:34

Don't worry about it.

46:37

Yes, it should be like ID because it should be unique.

46:39

because it should be unique.

46:41

And that is the reason how you will be able to differentiate that oh yes, yes.

46:46

Makes sense?

46:48

Everyone clear till now?

46:54

Take it.

46:58

Now coming to the next part, which is, well, you can repeat.

47:02

Absolutely.

47:04

Creating dictionaries, how, what are different ways in which you can create dictionaries?

47:08

Okay.

47:24

Way number one.

47:31

As I mentioned, you create student.

47:38

and you mention here, whatever details you want to store for student.

47:45

Name, yes, age 29.

47:56

Now what is this called?

47:57

This is something that you have done initialization of your dictionary.

48:03

All the key values are inserted in the dictionary.

48:07

This is one of the most common ways in which you create a dictionary.

48:11

Second way is you create an empty dictionary and then you later add the values in that.

48:16

So what will you do?

48:17

Student equals to something like this.

48:25

Okay?

48:26

And then what you do?

48:28

Student of name equals to

48:36

equals to yes.

48:38

Basically you define the values later.

48:42

Is that clear? This is way number 2.

48:45

Everyone?

48:50

Guys? With me?

48:55

Yeah, yeah, you can do that. Okay?

48:59

Way number 3

49:02

is basically you can use a dicta.

49:05

a dict. There is a keyword called as dict in Python.

49:09

For example, student

49:11

equals to dict.

49:15

And then define the key value pair.

49:19

So this will be the key

49:22

and this will be the value.

49:25

Okay?

49:28

This will be the key.

49:35

And this will be the value.

49:38

Now notice that in this format, you do not have to give these keys in the double codes.

49:46

There is no need to do that.

49:49

Okay?

49:51

Everyone, clear with this?

50:05

Prashant, we did,

50:07

we have a student variable defined

50:10

and we said that,

50:12

that it will be a curly brace.

50:15

We said that,

50:17

I don't want to put value inside that for now.

50:21

Later, I will put the value inside it.

50:24

Assume that you take this value as an input from client.

50:27

We have customer with input and insert

50:30

can I do that?

50:32

Definitely.

50:33

This is how we do it.

50:34

Okay?

50:35

Make sense?

50:37

Everyone clear?

50:42

Okay, okay?

50:45

One quickly, we will just see the code part and then we will come back.

50:50

Okay?

50:51

So let me go to the code screen.

50:56

Everyone able to see the code screen.

50:59

So how do you define a dictionary?

51:14

Okay, what will I do?

51:20

Student equals to something like this.

51:25

And then what do you do?

51:27

Name equals to yes.

51:28

equals to yes

51:30

age

51:32

equals to .

51:35

marks

51:40

equals to

51:42

91

51:44

now I have defined a dictionary here

51:47

if I print this dictionary

51:50

what will be the output?

51:52

any thoughts?

51:53

The complete key value pair will be the output.

51:57

Okay?

51:58

to see.

51:59

Run the code.

52:00

Can you see complete key value in output?

52:03

Can everyone see it?

52:14

Okay, okay?

52:17

Now let's define dictionary using way number 2.

52:21

What you will do?

52:23

You will say student 2 equals to empty dictionary.

52:29

Now I want to take value as an input.

52:32

as an input so what I will do student of name equals to input enter the name.

52:45

Student dot marks input and enter the marks.

52:56

Can I do this?

52:57

What do you guys think?

52:59

Student dot age.

53:01

age.

53:03

Student.

53:05

dot age,

53:06

int

53:08

input, enter the age.

53:11

What I have?

53:13

What do you have?

53:15

Now if I print

53:17

student, what will the output?

53:20

Oh, sorry, I think we

53:23

here we have got this

53:24

student underscore 2, student underscore 2,

53:26

student underscore 2.

53:28

And this.

53:30

Now, now I have all right all right

53:33

am I clear?

53:35

Okay.

53:37

So, let's try to see what

53:41

what is?

53:42

Run the code.

53:44

Okay, way number one is printed.

53:46

Enter the name Yash.

53:48

Enter the marks 82.

53:51

Enter the age 21.

53:54

See?

53:55

Name Yash, marks 82, age 21.

53:59

Okay.

54:00

is a different dictionary than student one.

54:04

Am I clear with this?

54:06

So as you said, key should be unique, but we can write name as name one.

54:12

If you create a new key here, okay?

54:20

Let's see what is the output.

54:22

Okay?

54:24

Let me comment all of this part for now.

54:30

Now, what is the name coming here?

54:34

What is the value of name coming here?

54:37

Is that yes or is that Subam?

54:39

So whatever is the latest value for your key that will be honored?

54:44

Make sense?

54:46

Overwrite.

54:48

Absolutely correct.

54:50

Clear, everyone.

54:52

Okay, now let's discuss way number three.

54:57

What is the number three?

54:59

Very simple.

55:00

what is something that you will have to do?

55:02

Student

55:04

0 0.3 equals to dict of name

55:11

equals to let's say Himachu.

55:16

Age equals to let's say 22.

55:21

Max equals to 91.

55:27

Print

55:30

current fee.

55:32

Okay?

55:33

Let's try to see what happens here.

55:35

Run.

55:36

It should be dict. D-I-C-T.

55:41

Run.

55:42

See. Name Hymanshu.

55:44

Age 22.

55:46

Marks 91.

55:50

You.

55:52

If you name one, if you

55:54

if you name one,

55:56

is the key on line number 4 and the key on line number 7.

55:59

Are they different?

56:00

Are they different?

56:04

Are they different?

56:05

Are these two keys are different?

56:07

So, if I try to print this, then I will get two different values.

56:11

Okay?

56:12

So that key will be a little bit.

56:14

But, Ankina, use case, it's not just for your information.

56:21

Is everyone comfortable till here?

56:24

Any questions?

56:29

You can create as many keys.

56:30

as you can.

56:31

Up to you, Abhishek.

56:32

As you, how you you can.

56:33

You can do you, how you can't.

56:34

Okay?

56:35

Okay.

56:36

Okay.

56:37

Now, let's discuss one more thing.

56:38

Let me go back to my iPad screen.

56:53

I believe all of my iPad screen

56:54

will be able to be able to be able to.

56:58

Okay.

56:59

Now, what I wanted to discuss, we can create different values or keys.

57:05

You can create different keys and different values.

57:07

That should be completely fine, Imanchu.

57:11

Error is coming in Vyan Smythi, you are doing something wrong, okay?

57:15

Check it out.

57:16

You're something wrong, okay?

57:18

Now, how do you access and modify the values in your dictionary?

57:29

Okay.

57:30

Okay, let's try to understand this.

57:51

So, assume that I have a dictionary for fruits.

57:59

prices.

58:02

And I create here banana, 20, apple, 40, 40, 40, and I have three, mango, and I have three fruits here with me, 50.

58:26

So I have three fruits here with me.

58:29

Now if I just want to print the price of Apple, how do I do it?

58:35

Print.

58:39

Fruit prices of apple.

58:49

Okay, and the output will be.

58:52

Okay, and the output will be 40.

58:55

Okay.

58:56

Is this clear to everyone?

59:00

Okay. Now can anyone think and tell me if I do something like this print of fruit prices of watermelon?

59:26

What will happen? Any thoughts?

59:31

First of all, kya this key exists in my dictionary?

59:36

The key does not exist. Now because the key does not exist, it will give me an error.

59:48

Okay. Now what happens is, here this is a problem.

59:54

This is a problem.

59:56

Because many times when you are writing code, it can happen that you are not aware about

1:0:01

that this key exists, or not does exist, if the key does not exist and you try to get the value,

1:0:11

the program will crash here.

1:0:16

Because there is an error, your program stop-hojah because your Python compiler with throw an error

1:0:22

key does not exist.

1:0:23

So ideally we should never let our program stop due to these kind of situations.

1:0:32

So we will actually use a better way to get the value from the hash map which is get method.

1:0:44

We will use get method here.

1:0:51

Okay, so what we'll do?

1:0:58

Am I audible guys, everyone?

1:1:03

So what we'll do?

1:1:05

Fruit prices

1:1:12

dot get.

1:1:14

And what should I pass inside this?

1:1:17

What should I pass inside this?

1:1:19

Any thoughts?

1:1:21

I should pass the key here.

1:1:25

Okay?

1:1:27

Always, always I should be passing the key because in dictionaries you get via key.

1:1:32

Okay?

1:1:33

So what you'll do?

1:1:35

You'll pass this watermelon.

1:1:37

Now, do you?

1:1:41

Watermelon exists?

1:1:44

No.

1:1:45

If watermelon exists not, if watermelon exists not,

1:1:49

so it will return none here.

1:1:56

Which is better than throwing a error.

1:1:58

Does everyone agree?

1:2:00

that's faking it's a good.

1:2:02

I should return some specific value.

1:2:04

Right?

1:2:05

And if I do fruit prices

1:2:10

dot get Apple.

1:2:16

What it should give the price of

1:2:18

of Apple, which is 40.

1:2:22

So that means if a value is there, it will return that value.

1:2:27

If value has, then value will return that value.

1:2:30

If a value, then it will run throw.

1:2:33

Which is very good for me, right?

1:2:35

Because at least I am not, my compiler is not stopping at the code.

1:2:39

Is this all this all of the

1:2:41

has?

1:2:42

Everyone.

1:2:45

So whenever you are writing,

1:2:47

whenever you are writing in your interview code,

1:2:50

like as part of, whenever you are doing code in an interview,

1:2:54

bauds, for example, if you are solving some DSA problem,

1:2:57

it's a lot of,

1:2:58

that the value did not exist.

1:3:01

So you will use a get method there,

1:3:03

so that if the value don't exist,

1:3:05

it will return you a none,

1:3:07

and then you can apply a if condition,

1:3:09

that if the value is not none,

1:3:11

then you do something.

1:3:13

Can you all understand?

1:3:14

If the value is present, then do something,

1:3:16

if the value is present, then do something,

1:3:17

the value is not present, then do something.

1:3:19

So we'll that if else logic

1:3:21

and we can play it.

1:3:22

Everyone clear?

1:3:24

Okay,

1:3:25

okay?

1:3:29

We have a use case,

1:3:31

we'll a very small problem solve

1:3:33

but before doing all of that,

1:3:36

let's just see some more things here.

1:3:40

Okay?

1:3:41

Now, second thing that I would like to discuss

1:3:45

is a method is

1:3:46

is keys.

1:3:48

This is also a function which is provided by Python by default.

1:3:56

So keys what it will return you all the keys in your dictionary.

1:4:13

Matla, if a dictionary has these values,

1:4:23

then my output will be fruit prices,

1:4:31

dot keys.

1:4:35

The output will be

1:4:43

banana

1:4:45

and this will be a list

1:4:57

does everyone agree?

1:4:58

this will be a list

1:4:59

just single name of fruit

1:5:01

all the keys in your dictionary

1:5:04

all the keys are all

1:5:05

they return

1:5:07

make sense

1:5:09

so and this will be a list

1:5:11

list.

1:5:12

Because at the end of the day, your dictionary

1:5:14

in multiple keys

1:5:15

are

1:5:16

not written all the things,

1:5:18

return just the keys of a dictionary.

1:5:21

Okay, Imanshu?

1:5:22

Yeah, the clear has

1:5:26

everyone.

1:5:27

Okay?

1:5:28

Okay.

1:5:29

Okay.

1:5:30

Okay.

1:5:32

Now our third function.

1:5:40

Which is values.

1:5:42

Okay.

1:5:44

Anyone would like to take a hint and tell me that

1:5:49

the values can return?

1:5:52

Sir, why are you mentioning fruit.

1:5:55

Because this is the keys part, right, Shalini?

1:5:59

This all keys are my.

1:6:01

Am I right, Shalini?

1:6:03

So I what I said,

1:6:04

fruit prices dot keys?

1:6:07

I've function used, dot keys.

1:6:09

Dot keys, right?

1:6:11

Shalini?

1:6:12

This is me

1:6:13

output in the

1:6:15

key, whatever are the keys as part of my dictionary, they come in the output.

1:6:20

Clear, Shalini?

1:6:22

Make sense?

1:6:24

Yes.

1:6:29

Now, if I do dot values, what should be the output?

1:6:32

Any thoughts?

1:6:33

It should return me all the values.

1:6:38

That means, if my dictionary is something like this,

1:6:57

and then if I do print of fruit prices

1:7:08

dot values.

1:7:13

What will be the output?

1:7:16

What will be the output?

1:7:18

Any thoughts?

1:7:20

It will be a list of 20.40.50.

1:7:26

Is this clear to everyone?

1:7:29

Okay.

1:7:32

So we have,

1:7:33

so,

1:7:34

if I need to get a single value,

1:7:37

a single value, I will use a get method. If I need to get all the keys, I will use a dot keys method.

1:7:45

If I need to get all the values, then I will use a dot values method.

1:7:51

Here, everyone clear.

1:7:54

But if I want, if I want one by one key comma value pair,

1:8:06

I want to get the key value pairs of my map.

1:8:12

How do I do that?

1:8:15

So the fourth function is called as items.

1:8:23

And these items, it's what it will give you key and value together.

1:8:35

It will give you the key and value together.

1:8:43

It will give you basically how it will be how do?

1:8:49

If I do, now tell me,

1:8:53

if I want you to iterate over this

1:9:00

on the elements one by one,

1:9:04

how will you do?

1:9:05

Very simple.

1:9:07

Yes, what we'll do?

1:9:09

For

1:9:10

I comma j

1:9:15

in fruit prices

1:9:22

dot items

1:9:32

print

1:9:36

fruit

1:9:41

I

1:9:45

price

1:9:58

I will go to this index

1:10:01

I will get I comma J

1:10:04

So here here I comma J

1:10:06

anyone would like to take a guess

1:10:08

I comma j what would like to take a guess

1:10:12

key and value

1:10:15

so what I will print as an output

1:10:19

fruit

1:10:22

rice

1:10:25

rice

1:10:31

because I am running this on a loop. Is this clear to everyone?

1:10:35

What

1:10:44

it's all

1:10:46

what would

1:10:47

what would

1:10:48

what

1:10:49

is

1:10:51

20

1:10:52

Apple

1:10:54

price is

1:10:55

14

1:10:56

mango

1:10:57

prices

1:10:59

50

1:11:00

and there is no

1:11:01

last fruit so I'll just remove this

1:11:03

everyone

1:11:04

clear with this

1:11:05

You know

1:11:07

all

1:11:08

you

1:11:09

know

1:11:10

Abish

1:11:11

When we

1:11:13

When we

1:11:14

we're

1:11:15

When we

1:11:16

we're

1:11:17

If we

1:11:18

If we

1:11:19

will

1:11:20

How many values will

1:11:21

I get

1:11:22

when I iterate on a

1:11:23

dictionary?

1:11:25

A

1:11:26

A

1:11:27

A

1:11:28

record

1:11:29

how many values are present

1:11:31

in a dictionary?

1:11:32

Two values

1:11:35

Right?

1:11:36

Now,

1:11:37

Now, if I'm iterate

1:11:38

for

1:11:39

example, when I

1:11:40

I

1:11:41

used to write,

1:11:42

for I in range 0 to 10,

1:11:45

what I used to represent the value of that list,

1:11:49

the current value of the list, am I correct?

1:11:52

Am I correct?

1:11:54

Here

1:11:55

I am iterating on this list.

1:11:59

So for this iteration, current iteration,

1:12:02

I comma J will

1:12:05

get me the key and the value because this is the key and this is the value.

1:12:12

This is the key, this is the value.

1:12:15

This is the key, this is the value.

1:12:18

So if I ask you,

1:12:20

if I ask you, print all the key values of a dictionary,

1:12:24

can you do this using this?

1:12:26

Can you do this using this?

1:12:28

Okay, so this

1:12:31

so this

1:12:35

This mostly we use

1:12:37

We use

1:12:38

Okay?

1:12:39

Abhik, write a code one time

1:12:44

and then you'll clear

1:12:45

Okay?

1:12:46

If you can,

1:12:47

you can more clear

1:12:48

Okay?

1:12:49

Anyone having any other questions on list?

1:12:52

Ah, sir, if we want to have some specific key

1:12:55

and value from a dictionary,

1:12:57

can we apply slicing to it?

1:13:00

Slicing dictionary

1:13:01

I don't think we can apply.

1:13:03

No, San Yukta, we cannot do that.

1:13:04

cannot do that.

1:13:05

Sticing is only applicable to list data structure.

1:13:08

I mean, yeah, if you know, if you, for example, now there is a very interesting thing that's

1:13:14

Anuta Haqabob.

1:13:15

What I am telling is I am defining a dictionary here of student.

1:13:24

Now I will define a key and a value.

1:13:27

Does everyone agree?

1:13:29

So, can I say,

1:13:32

that my key is name and my value is yes.

1:13:41

Can I say that?

1:13:43

Everyone agrees with me?

1:13:45

Key is name, value is yes.

1:13:47

Then I say my key is marks

1:13:50

and my value is a list of marks.

1:13:54

What do you guys think?

1:14:01

Can I do you guys think?

1:14:02

But value is a list of marks.

1:14:09

At the end of the day, we are we just discussing

1:14:12

that only primitive data type can be value

1:14:15

not. In fact, any data type can become your value.

1:14:20

Is this clear?

1:14:22

So if I print

1:14:25

student of marks, what will be the output?

1:14:32

What will be the output?

1:14:39

If I print student of marks, what will be the output?

1:14:43

The complete list.

1:14:46

Now if I tell you, sort this and tell me the top two marks.

1:14:52

Can you do that?

1:14:54

Can you do that using slicing?

1:14:56

To yash for tell me the top two marks.

1:14:59

You can sort this and apply field.

1:15:01

And apply filter and get me.

1:15:03

Right?

1:15:04

Try it out.

1:15:05

During the break time, try it out.

1:15:07

Take it.

1:15:08

Guys, let's take the break for 8 minutes.

1:15:11

Let's come back by 907 p.m.

1:15:16

Let's write some code for dictionaries.

1:15:19

Then we will move to what are hash maps.

1:15:22

Make sense?

1:15:24

Oh, okay.

1:15:30

Okay.

1:15:31

Thank you.

1:16:01

Thank you.

1:16:31

Thank you.

1:17:01

Thank you

1:17:31

Thank you

1:18:01

Thank you

1:18:31

Thank you

1:19:01

Thank you

1:19:31

Thank you

1:20:01

Thank

1:20:03

You

1:20:31

Thank

1:20:33

You

1:21:01

Thank you.

1:21:31

Thank you.

1:22:01

Thank you.

1:22:31

Thank you.

1:23:01

Thank you.

1:23:31

Thank you.

1:24:01

Thank you.

1:24:31

Thank you.

1:25:01

Thank you.

1:25:31

Okay, I'll be back, everyone.

1:25:35

Hello, hello, are we back?

1:25:40

Hello, are we back?

1:25:44

Are you guys able to see my port screen?

1:25:50

Everyone?

1:25:54

So let's try out whatever we have learnt till now.

1:26:00

Right?

1:26:01

So I have a student dictate here.

1:26:04

Okay.

1:26:05

Now if I want to just print the keys of the student, how do I do print?

1:26:13

Student dot keys.

1:26:16

Okay?

1:26:18

And let me write something like this.

1:26:21

And similarly, if I want to print values, what will I do?

1:26:28

values, student dot values.

1:26:33

If I want to print a specific key of a student, how do I do that, print name, student dot, student.

1:26:52

Let's try and see whether this works or not.

1:26:55

run the code.

1:26:56

Okay, keys, if you see, dict, it is giving me dictionary keys and it is giving me an

1:27:04

array of name, age, marks, name one.

1:27:08

Values, yes, 291, that means all the values.

1:27:13

And if I try to see that, okay, I want to print the name of the student, I get the name yesh.

1:27:18

Now if I say I want to print the first name of the student.

1:27:25

Now first of the student.

1:27:25

does the first name exist? Does the first name exist? There is no first name here.

1:27:32

So let's see what happens. So first name. Oh sorry, my word, should be first name here.

1:27:42

Now if I run the code, see, it tells me none. So can I have some logic on the basis of the output?

1:27:49

For example, if student dot first name,

1:27:55

is none, then print, first name, not present. What do I think? Can we have

1:28:11

something like this? Else, print, print, first name, present. What do you I think?

1:28:25

Can we have something like this?

1:28:27

Are you guys not able to see the code screen? Everyone?

1:28:35

See, first team not present. Because the first team was not present.

1:28:39

Everyone clear till here?

1:28:45

Any questions?

1:28:51

Okay, okay, okay.

1:28:53

Now let's do a mini exercise.

1:28:54

mini exercise. What is first name? First name is a key. First name is not present in the

1:29:01

hash in the dictionary. Hence I'm trying to print it. So this is a use case that we discovered. Get.

1:29:07

Okay, Manchu? Now if I want to print all the keys, all the pairs. How do I do that? For

1:29:18

key comma value in.

1:29:24

for key, comma, value in student dot items. Print. Name is key.

1:29:54

value is okay let's try to see key is name and the value is yes key is name age

1:30:04

and the value is 29 key is marks and the value is 91 so if I ask you ever to iterate

1:30:11

over the dictionary can you guys do it now if I ask you that okay we we have to create a

1:30:19

dictionary and I have to iterate over it can we do that definitely make sense

1:30:24

Actually, let's see one problem, a mini problem and try to solve it.

1:30:28

Abhishek, we will solve one problem and you can see use case.

1:30:31

Count the characters in a string, okay? So what we are going to do, I'll just, for now, I'll just comment all of this part. So that it is not cluttering, okay?

1:30:50

Assume that we are taking a string in the input.

1:30:54

Enter the string.

1:30:56

Okay?

1:31:00

And what I need to do is I need to count the number of characters in the string.

1:31:05

For example, B-A-N-A-N-N-A.

1:31:09

Now, how many times B has occurred here?

1:31:12

1.

1:31:13

What is the count of A? 3.

1:31:15

What is the count of N? 2.

1:31:18

This should be the output.

1:31:20

Is the question clear to everyone what I want to do?

1:31:23

Is the question clear? What I want to do?

1:31:30

For given any string to me, I want to count the frequency of all the characters.

1:31:38

Okay?

1:31:40

So if the string is banana, how do I start it?

1:31:43

First thing first.

1:31:44

If you remember from the previous session, string indexes also start from zero.

1:31:49

Right?

1:31:50

So either I can use that or I can

1:31:53

do something like that for care, current care in text in STR.

1:32:02

As soon as you, I'll just use this, STR input.

1:32:07

As soon as you do this, what this loop will do is it will go over character by character.

1:32:12

Okay?

1:32:13

And then what should I do? Any thoughts?

1:32:16

What? Okay.

1:32:18

Now, the first thing is that I will have to use a dictionary here.

1:32:22

Okay. Now, guys, tell me one thing. What should be the key and what should be the value of my dictionary? What do you guys think? What should be the key and what should be the value in my dictionary?

1:32:36

Any thoughts from anyone?

1:32:43

Key should be alphabet. Does everyone?

1:32:45

Because that is going to be unique. And value should be the count.

1:32:52

Does everyone agree with that?

1:32:54

First of all.

1:32:56

Everyone? Because key is going to be unique.

1:33:00

So can I say that I want key as my alphabet and the value is my count?

1:33:04

So what I will do?

1:33:06

I will define a hash map.

1:33:08

Can I define a hash map something like this?

1:33:12

Definitely yes. You can define a hash map and then you can add the values later.

1:33:15

So what will I do?

1:33:16

Counts of CARE equals to...

1:33:20

Now I need to first think that.

1:33:22

that I will need to check is that whether the count for that character already exists.

1:33:30

If the count for that character already exists, then I will have to increment the count by one.

1:33:36

Correct?

1:33:38

So what I will do here is count dot get care.

1:33:44

Current care.

1:33:45

What is current care?

1:33:47

For the first iteration, current care will be B.

1:33:51

Print.

1:33:52

Current care.

1:33:54

Okay?

1:33:57

If I pass here comma 0, what it means is that if there is a current care present in the hash map, get me the value of it.

1:34:09

If it is not present, then get me 0, which is a default value.

1:34:14

Is this clear to everyone?

1:34:17

Is this clear to everyone?

1:34:20

What I just did.

1:34:21

I just did.

1:34:22

What I did?

1:34:23

What I did?

1:34:24

I said, I said, that counts hash map, counts dictionary, I want to get the value of current

1:34:32

cap.

1:34:33

Till here, everyone clear?

1:34:35

Okay.

1:34:36

Now for the very first time, in your dictionary, do you have anything?

1:34:41

When the character becomes B, here, do you have anything?

1:34:45

You don't have anything.

1:34:46

Right?

1:34:47

So what this will return?

1:34:49

What will this return to you?

1:34:50

What will this return to you?

1:34:53

Why it will return zero?

1:34:57

It will not return zero.

1:35:00

It will not return zero.

1:35:01

It will return you empty.

1:35:03

Everyone?

1:35:04

Because the value is not present.

1:35:06

So it will return you empty.

1:35:08

Am I correct?

1:35:10

Now, if that returns you a non value, can you add any integer to that?

1:35:17

No.

1:35:18

That means, can I?

1:35:19

It means, can I say that if the value don't exist, does not,

1:35:24

if the value not, if the value not, then,

1:35:26

then the default values, key, zero,

1:35:28

can I say that?

1:35:29

So that I can increment it.

1:35:31

Can you all understand?

1:35:33

Okay.

1:35:34

Okay.

1:35:36

Okay.

1:35:39

Okay.

1:35:41

Okay.

1:35:42

Okay.

1:35:43

Okay.

1:35:44

Okay.

1:35:45

We do.

1:35:46

First, we first,

1:35:47

this loop, print,

1:35:48

the loop in print.

1:35:49

I'll run this code.

1:35:50

If you see this output, if you see this output,

1:35:53

do you see this output,

1:35:54

do you, what have?

1:35:56

B-A-N-A-N-A,

1:35:58

I mean,

1:35:59

every iteration in loop,

1:36:00

a character picked up.

1:36:01

Is this clear with everyone?

1:36:03

Is this clear with everyone?

1:36:05

Yes,

1:36:06

Pucka, 100%, Prasant?

1:36:09

Fine with you?

1:36:12

Okay.

1:36:13

So,

1:36:14

now,

1:36:15

if I will,

1:36:16

every letter, okay?

1:36:18

Now, if I say,

1:36:19

counts of current care,

1:36:22

this means what is the current care,

1:36:24

A, B, or N, what you will do?

1:36:28

Get me the value of

1:36:32

current count,

1:36:35

if not?

1:36:37

If a value not, then get me a default value of zero.

1:36:40

Do you?

1:36:41

All right?

1:36:42

All right?

1:36:45

Current value.

1:36:46

I will create a variable.

1:36:48

Current value.

1:36:49

Okay?

1:36:50

Now, whatever is the current value, I need to increment it by 1.

1:36:53

So what will I do?

1:36:55

Current value plus equals to 1.

1:36:59

This all of what will I?

1:37:02

Then what will I do?

1:37:04

Counts of current cap equals to current value.

1:37:11

Okay?

1:37:12

Now my work is done, but I will print.

1:37:15

print counts. Let's see what

1:37:17

Let's see what it.

1:37:19

Run the code.

1:37:21

Okay?

1:37:23

So if you look,

1:37:24

I can do

1:37:25

a kind of, I'm a kind of

1:37:26

I'm this kind of

1:37:27

this kind of

1:37:28

so that we'll get

1:37:29

here.

1:37:30

We'll do this

1:37:31

print current care was this.

1:37:33

Okay?

1:37:35

Current value

1:37:37

was this

1:37:39

okay.

1:37:42

And then

1:37:44

We have, now let me.

1:37:48

Okay.

1:37:49

So current care was B.

1:37:51

Okay?

1:37:52

Current care was the very first time the care value will be B.

1:37:57

Is this all the

1:37:58

all of the

1:37:59

all of the

1:38:02

Let me comment all the print statements

1:38:08

so that

1:38:10

now if you see,

1:38:12

if you see,

1:38:13

if I say current

1:38:14

carries B and the current value in the dictionary,

1:38:17

let me print the dictionary as well.

1:38:19

So print

1:38:20

counts.

1:38:21

Okay.

1:38:22

Okay.

1:38:23

Now if you see, for the very first time,

1:38:27

the very first time

1:38:28

dictionary

1:38:29

what is?

1:38:30

Empty.

1:38:31

Can this all

1:38:32

what this

1:38:33

of all

1:38:34

what this is

1:38:35

initially

1:38:36

dictionary

1:38:37

value

1:38:38

empty.

1:38:39

Then we have current

1:38:40

character

1:38:43

B, can I say that?

1:38:45

Can I say that?

1:38:46

Dictionary in the

1:38:47

Dictionary in the

1:38:48

number one.

1:38:49

Then next character

1:38:50

A

1:38:51

Right?

1:38:52

So the dictionary in value

1:38:54

what

1:38:55

B comma 1

1:38:56

A,

1:38:57

everyone clear?

1:38:58

Then next character

1:38:59

a N.

1:39:00

Dictionary in value

1:39:01

what

1:39:02

What is the value

1:39:03

B, A and

1:39:04

Can?

1:39:05

Can?

1:39:06

Everyone clear?

1:39:09

Then

1:39:10

Then the character a

1:39:11

So now

1:39:12

So,

1:39:13

now,

1:39:14

the only value already

1:39:15

there in my dictionary?

1:39:16

What

1:39:17

A

1:39:18

key value already?

1:39:19

This time,

1:39:20

A key value already

1:39:20

then

1:39:21

I took

1:39:22

and it plus one

1:39:23

here.

1:39:24

Okay,

1:39:26

so I will leave

1:39:27

this code

1:39:28

in the chat

1:39:29

so that you guys can

1:39:30

write it

1:39:31

and debug it once

1:39:32

at your piece.

1:39:33

Make sense to

1:39:35

everyone?

1:39:36

Okay.

1:39:42

Now, with this,

1:39:44

we let's

1:39:45

go to

1:39:46

court screen

1:39:47

we're last topic

1:39:48

discuss

1:39:50

which is hashmaps.

1:39:51

Okay?

1:39:53

Everyone is

1:39:55

able to see my iPad screen.

1:40:12

Okay.

1:40:13

Now,

1:40:14

So, what are hash maps?

1:40:17

Check it out online San Yubta, okay?

1:40:23

What are hash maps?

1:40:25

Hash maps basically are key value pair.

1:40:28

Now you will basically ask me a question,

1:40:37

yesh, if this key value pair,

1:40:39

then what is,

1:40:40

actually,

1:40:41

actually,

1:40:42

In Python,

1:40:44

dictionary is a hash map.

1:40:55

Okay?

1:40:56

Basically, key value pair

1:41:01

in Java

1:41:02

it's a hash map

1:41:04

and Python

1:41:05

it's it's a dictionary.

1:41:07

C++,

1:41:08

we're ordered map

1:41:09

in.

1:41:10

JavaScript in

1:41:11

we are object

1:41:12

Okay?

1:41:13

So different languages have different naming conventions for this data structure.

1:41:18

But the universal logic is same that it is a key value pair.

1:41:25

Make sense?

1:41:27

So if you are you

1:41:29

able to understand that they mean dictionary?

1:41:33

Or if you are you able to

1:41:35

understand that they mean a hash map?

1:41:38

Basically a key value pair.

1:41:40

Can I say that?

1:41:41

Make sense?

1:41:43

Okay?

1:41:46

Now the intuition here is

1:41:48

why do we use hash maps?

1:41:51

The reason is the advantage of hash map.

1:41:56

The advantage is

1:42:01

hash maps are very, very, very first.

1:42:07

As in the time complexity of hash map is

1:42:10

is O of 1, which is constant.

1:42:15

Yes, this is how?

1:42:20

Hashmap is what then dictionary is hash map?

1:42:26

Himancho, dictionary and hash map are the same things.

1:42:29

Like, our home

1:42:31

house name versus actual name,

1:42:32

a different name is, right?

1:42:34

Similarly, a different names.

1:42:36

The thing is say.

1:42:38

Okay, Imanchu?

1:42:39

Does that answer your question?

1:42:44

Now, why do we use hash maps or why do we use dictionaries at the first place?

1:42:50

Why there is a need to it?

1:42:53

There is no need.

1:42:54

Arre, we're has a hash map because people use hash map as a general term.

1:42:59

Okay?

1:43:01

Because many people will tell you that,

1:43:02

okay, for example, if you are working somewhere

1:43:04

and your colleague tells you that, okay, create a hash map out of it.

1:43:07

Now you will ask that, okay, there is no hash map out of it.

1:43:08

Now, you will ask that, okay, there is no hash map.

1:43:09

hash map but they mean that create a dictionary out of it.

1:43:13

Okay?

1:43:14

So you should know about it.

1:43:15

That is the reason we are discussing it.

1:43:17

Make sense?

1:43:19

Hashmab is a very common term.

1:43:22

That is the reason I am discussing this.

1:43:24

Now, guys, you have to understand this part

1:43:27

that hash maps are very fast.

1:43:30

Why? Because they get you the data in constant time.

1:43:34

How yes?

1:43:35

We took the example, right?

1:43:37

Assume that this is your city and there are

1:43:39

so many houses in the city.

1:43:45

There are so many houses in the city.

1:43:49

I live in this house.

1:43:52

Now if I ask you to visit my home,

1:43:57

you, if you are using a hash map, that you know that Yesh lives in ABC.

1:44:04

This is the address of Yash.

1:44:09

So what you will do?

1:44:14

Instead of searching all the places, you will directly come to my house.

1:44:18

Am I correct?

1:44:19

Everyone.

1:44:22

Instead of searching all the things,

1:44:25

if there are 10,000 values would,

1:44:28

so instead of searching all the 10,000 values,

1:44:30

you can get to me in just one search.

1:44:34

Can I say that?

1:44:35

Because we are directly pointing to the exact value.

1:44:38

Do you?

1:44:39

Dohit?

1:44:40

If I had 10,000 values, then you would have 10,000 times search

1:44:45

to 1,000 times.

1:44:46

First you have to here, then you have to here, you have to, here to go, here,

1:44:51

you would have to, basically, you have to,

1:44:53

you have all the place, and you would have to,

1:44:55

last in or at a time, right?

1:44:58

So, if I would it as a list represent

1:45:02

city, then you have O of end time complexity

1:45:07

complexity. What is N? N is the number of elements in the list. Can I say that?

1:45:12

That,

1:45:13

O of N, I mean all the elements I will have to search and then get the value.

1:45:18

But if I'm using a hash map, because I have a mapping,

1:45:22

I will directly search can. I will say that,

1:45:24

Okay, Yash, you know,

1:45:25

you know, I'll tell you,

1:45:26

I'm at one second.

1:45:27

Does that make sense?

1:45:33

Everyone clear?

1:45:35

Okay?

1:45:36

So this is how it?

1:45:37

So basically, I'll just go a little bit into the internals of the language.

1:45:42

Thorda very, not go, not go, so that it's all to understand.

1:45:45

Okay?

1:45:46

Whenever we write price or whenever I write fruit,

1:45:54

banana is equal to 40.

1:46:04

Whenever I write this,

1:46:06

So, Python what does,

1:46:08

it makes a hash map in an entry

1:46:12

everyone agree that for this banana,

1:46:15

the price is 40.

1:46:17

Does everyone agree?

1:46:19

That hash map, Python is an entry, right or no?

1:46:23

Am I correct here?

1:46:26

Is not?

1:46:27

So Python what is, whatever is the key,

1:46:31

Okay, please hear me out correctly,

1:46:34

whatever is the key,

1:46:35

that Python compresses

1:46:38

and it's a hash

1:46:41

makes it.

1:46:42

Okay?

1:46:44

Python will create a hash value out of it internally

1:46:49

which converts this into a number.

1:46:53

Okay?

1:46:58

Now, this number basically tells Python

1:47:04

Okay, this number basically tells Python that if this is your memory, okay?

1:47:15

If this is your memory, this number basically tells Python that the value is exactly stored at this specific location.

1:47:27

This number is responsible to tell that.

1:47:31

Okay, so what happens?

1:47:33

What happens? You create a key.

1:47:40

As soon as you create a key, internally a hash function is called.

1:47:45

That hash function will generate a number, a random number.

1:47:50

Something like this, for example.

1:47:54

Then Python will figure out that, okay, this hash number is stored in this specific slot in the memory.

1:48:01

And then in this slot, the value of that specific thing is stored, which is 40.

1:48:12

Makes sense. It is very much similar to your car valet system.

1:48:18

Car valley system.

1:48:19

What we go?

1:48:20

We go, we go to our car park car park

1:48:23

the valley,

1:48:24

we have our car-car-park-car-car-car-car-car-car-car-car-car-corresponding a key

1:48:27

gives.

1:48:28

And whenever we come back, we want our car.

1:48:30

We want our car.

1:48:31

car, do we search the car everywhere? No, we do not search it. We just hand over the key

1:48:38

to the valet. Valle will go in the memory, get your car and give it to you. Make sense?

1:48:46

So instead of all the parking in search

1:48:51

the valet exactly knows that this car here parked here. Make sense?

1:48:58

Okay.

1:49:01

Okay.

1:49:02

Is this clear?

1:49:03

Okay.

1:49:04

Now, there is a one caveat here.

1:49:06

Okay?

1:49:07

Now, there is a one caveat here.

1:49:26

Okay?

1:49:27

Exactly, Himancho, exactly.

1:49:30

Okay?

1:49:31

give a key to my code. Am I correct? If I give the key, then my Python compiler will

1:49:37

generate the hash out of it. Right? So what are valid keys? Valid key data types.

1:49:46

They are basically string, integer, bullion, these are the things.

1:49:58

string, integer, bullion, and there is something called as tuples in Python.

1:50:10

Tuples in Python.

1:50:12

I can share some reading material on them.

1:50:16

So these are valid key of data types.

1:50:19

As in, for example, if you create a key of a list,

1:50:24

if you want to create a hash map,

1:50:27

where the key data type is a list.

1:50:32

And the value data type is string.

1:50:36

Now, in order to make your hashing work, the hashing function is

1:50:41

in order to make that work,

1:50:44

list data types is not supported.

1:50:47

Right?

1:50:49

So, whenever you try to dictionary to

1:50:52

with key as list, you will get an error here.

1:50:57

Make sense?

1:50:58

Okay.

1:50:59

All this is up to say.

1:51:01

Alright?

1:51:02

Okay.

1:51:03

Now there are some extra functions provided by Python for dictionaries.

1:51:08

I'll just discuss that in five more minutes and that should.

1:51:13

We will conclude the class for the day.

1:51:16

Okay?

1:51:17

Some good functions to know on dictionaries.

1:51:20

Okay?

1:51:27

The first function is basically LEN.

1:51:41

Any thoughts?

1:51:42

What will?

1:51:44

Any thoughts?

1:51:45

What will?

1:51:47

Lenn of variable name?

1:51:54

Any thoughts?

1:51:55

what will tell me how many pairs are stored in your dictionary?

1:52:10

Everyone? Okay.

1:52:15

Okay.

1:52:16

Okay.

1:52:17

Second function is called as sorted.

1:52:23

Okay.

1:52:24

That means.

1:52:25

I do, sorted of variable name.

1:52:32

It will sort the dictionary on the basis of keys.

1:52:51

It will sort the basis of keys.

1:52:54

For example,

1:52:55

For example, if my dictionary is,

1:52:59

ah, yeah, if my dictionary is, prices,

1:53:05

Apple, banana.

1:53:23

If I do, sorted of prices, what will happen?

1:53:36

What is the data type of my keys?

1:53:39

What is data type of my keys?

1:53:42

Key to sort, value not it will not sort values.

1:53:47

It will not sort values.

1:53:48

That is the reason I'm discussing, this key to sort

1:53:50

so what will be the order here?

1:53:52

order here, Apple, banana, mango.

1:54:01

Now if I pass, sorted off,

1:54:06

prices, dot values, what will happen?

1:54:15

Any thoughts?

1:54:17

Now what will happen?

1:54:21

values are not, that sort?

1:54:23

10, 20, 30.

1:54:25

Everyone clear with this?

1:54:29

Okay?

1:54:30

So these functions are common functions

1:54:36

that you can use for example,

1:54:39

if I do max

1:54:41

of prices of value,

1:54:44

output what will?

1:54:46

Any thoughts?

1:54:48

Any thoughts?

1:54:50

Max of prices of value?

1:54:52

30.

1:54:53

And if I do minimum output, what will?

1:54:56

10. Okay?

1:54:58

If I do sum, output what will?

1:55:03

60, absolutely.

1:55:08

Okay?

1:55:09

So this is all about dictionaries and hash maps in Python.

1:55:14

Okay?

1:55:16

Just allow me two minutes.

1:55:17

two minutes I'll just open a sheet and we'll just discuss one more thing.

1:55:23

We have what topics covered?

1:55:25

We have them clear and then we will drop for the day.

1:55:45

Okay, do you?

1:55:46

Do you see my sheet screen?

1:55:48

Everyone is able to see my screen, the sheet screen?

1:55:55

Okay.

1:55:56

So, if I'm about,

1:55:59

the last class,

1:56:01

so,

1:56:02

we've seen that we can create

1:56:04

list and manipulate

1:56:05

can,

1:56:06

do we have this part?

1:56:07

Right?

1:56:08

Right?

1:56:10

Okay.

1:56:11

Okay.

1:56:12

Part, we've seen that we can accessing elements access

1:56:15

list and strings both.

1:56:18

List and strings both, list maybe, string maybe.

1:56:20

Yes.

1:56:21

Do we have seen that we format strings if I want?

1:56:26

Yeah, this also.

1:56:29

Then we've seen that built-in functions are some.

1:56:32

For example, slices.

1:56:35

I cannot, yeah.

1:56:37

Then we've seen that built-in functions are.

1:56:40

We can't use.

1:56:41

slices, you can see.

1:56:43

If I've seen, if I'm

1:56:45

If I've seen,

1:56:46

how we've seen

1:56:47

how we can create dictionaries

1:56:48

can create

1:56:50

everyone?

1:56:53

Yes.

1:56:55

Have we seen all of these functions?

1:56:58

Get keys, values, items.

1:57:02

Yes.

1:57:04

Do you?

1:57:05

Intuition of the dictionary

1:57:07

that when I should use dictionaries

1:57:10

and when I should use dictionaries?

1:57:11

Like when I should be using dictionary and hash maps,

1:57:13

whenever I want to do fast lookups.

1:57:15

Right?

1:57:16

When I have mapping,

1:57:17

whenever I have to fast look up

1:57:19

at that point, I should use them.

1:57:21

Then we've seen

1:57:23

built-in functions.

1:57:24

For example, how built-in functions

1:57:25

say, Canseman, please tell me?

1:57:27

Which built-in functions did we saw today

1:57:31

for hash maps?

1:57:32

Sorted, max, Lenn, all of these types.

1:57:47

Okay?

1:57:48

Now, I'm here here here

1:57:49

some links there.

1:57:50

This link, sorry.

1:57:52

Uh,

1:57:54

Vijay, there.

1:57:56

Yes, yes, I'm just updating it.

1:57:59

Yeah.

1:58:00

You write it now.

1:58:01

Yeah, it's updated.

1:58:02

Cool, I just, yeah, thanks.

1:58:04

So the first thing that I'm giving here is

1:58:07

for going through tuples, what are tuples in Python?

1:58:10

Like we have a list,

1:58:12

like we have hash maps,

1:58:13

the dictionary,

1:58:14

like similarly a data structure is,

1:58:16

tuples.

1:58:17

Okay?

1:58:18

So,

1:58:19

you know what are tuples in Python?

1:58:22

Can everyone do that?

1:58:23

Can I expect you guys to do it?

1:58:25

Hello, my audible?

1:58:31

Okay, okay?

1:58:35

We'll, we'll take a couple's what

1:58:37

what?

1:58:38

Then, then, I think,

1:58:39

you know,

1:58:40

this one thing,

1:58:41

which will explain you what is a difference between

1:58:44

tappel and a list.

1:58:46

Okay?

1:58:47

And there's some interview questions

1:58:49

that will help you out.

1:58:51

Okay? Does that make sense?

1:58:54

So, can you do this before the next class?

1:58:59

Can I expect you guys to do it before the next class?

1:59:00

Can I expect you guys to do it before the next class?

1:59:01

everyone

1:59:03

paka 100%

1:59:05

awesome

1:59:10

so that's it from my side then

1:59:12

thank you everyone have a good day ahead

1:59:14

I'll just hand it over to Vijay

1:59:16

and thank you

1:59:19

okay thanks

1:59:21

okay we can go through the quick quiz

1:59:24

let me share my screen

1:59:25

is my screen

1:59:29

is my screen visible

1:59:31

to everyone just do a thumbs up and scan this QR code

1:59:38

do a thumbs up and scan this QR code like now like everyone is aware about the process right

1:59:42

so yeah I see only 10 students join

1:59:49

I will wait for 15 more seconds

2:0:01

Five seconds more.

2:0:16

Okay, let's start.

2:0:31

All of you will see the first question we have like most of the players ready.

2:0:37

Let's start the quiz.

2:0:38

Try to answer it quickly.

2:0:54

Answer it quickly and like just do a thumbs up.

2:1:01

Okay, let's see who is the winner. Most of the students have given the correct answer.

2:1:07

Let's go to leader board.

2:1:08

Oh, great, dummy is the winner. Let's move to the next question.

2:1:15

Everyone do a thumbs up on your screen.

2:1:21

We will start for the second question.

2:1:24

To get more points answer quickly.

2:1:29

To get more points answer quickly.

2:1:30

answer quickly.

2:1:33

Perfect.

2:1:47

Let's see what is student.

2:1:49

Okay.

2:1:50

It's still like some student have given the wrong answer.

2:1:52

Student dot name is not the right way.

2:1:55

Let's move to the next question.

2:1:59

Let's see who is the overall winner.

2:2:06

Oh, even this time too, like Domini is the winner.

2:2:09

Okay, everyone do a thumbs up.

2:2:11

We will move to the next question.

2:2:13

Let us start the next question.

2:2:16

Anybody who have given the answer, just do a thumbs up to get the question on the screen.

2:2:29

Okay, still seven students have given wrong answer.

2:2:43

No worries.

2:2:44

Let's try in the next question.

2:2:46

Let's see who is the winner.

2:2:49

Okay, so this time I think Calvin is the winner.

2:2:53

Bavie have given the fastest answer at this end.

2:2:58

Let's move to the next question.

2:2:59

Everyone do a thumbs up post providing the answer.

2:3:03

This one is a easy question right?

2:3:29

most of this, like some students have answered yes, but it cannot be duplicated, right?

2:3:33

Fine, anyways, take care next time maybe.

2:3:36

Okay, still anvil seems to be at the first place.

2:3:43

Let's move to the last question.

2:3:47

Anybody who is not getting the question on the screen,

2:3:52

please do a thumbs up. You will get the question.

2:3:59

this is the final question to be like final chance for all of you to be on the top of leaderboard

2:4:13

so answer it quickly let's see who is the final winner

2:4:29

is the final unit uh thank uh yeah i will just launch a quick feedback poll

2:4:37

uh everyone will see you the questions on the screen just provide the feedback

2:4:45

uh you can provide the feedback and like drop after the call yeah after providing the feedback

2:4:51

yeah that's it for today

2:4:59

Requesting everyone to please provide the feedback like it's very important for us to know like how well we are performing and like what are the area of improvements we need to see here.

2:5:11

Anyone who have provided the feedback like they can drop off. We are done for today.

2:5:23

Okay, 67% students have provided the feedback.

2:5:28

Yeah, students can drop up whoever have provided the feedback. Feel free to drop off.

2:5:35

Just provide the feedback and then you can drop off.

2:5:39

Okay, I think that's it for today. Thank you, thanks everyone.

2:5:54

Sure, I will like check with the team to provide the team.

2:5:57

check with the team to provide the handwritten notes.